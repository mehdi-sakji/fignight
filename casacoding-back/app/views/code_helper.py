from app import app, api, bigquery_client, bigquery_job_config
from app.parsers import *
from app.utils import *
from flask_restx import Resource
import pandas as pd
import time
from datetime import datetime, timedelta
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime
from pytz import timezone
import humanize


@api.route("/api/allcategories")
class AllCategories(Resource):
    """
    """

    @api.doc()
    def get(self):
        """
        """

        query_job = bigquery_client.query(
            """SELECT DISTINCT category FROM {}""".format(
                app.config["GOOGLE_TABLE_ID"]))
        results = [row.category for row in query_job]
        return {"response": results}, 200


@api.route("/api/alltags")
class AllTags(Resource):
    """
    """

    @api.doc()
    def get(self):
        """
        """

        query_job = bigquery_client.query(
            """SELECT DISTINCT tags FROM {}""".format(
                app.config["GOOGLE_TABLE_ID"]))
        results = [row.tags.split(",") for row in query_job]
        flat_results = [item for sublist in results for item in sublist]
        flat_results = list(set(flat_results))
        return {"response": flat_results}, 200


@api.route("/api/codeHelper")
class CodeHelper(Resource):
    """ 
    Class for indexing and searching code hints.
    """

    @api.doc()
    @api.expect(index_code_helper_parser)
    def post(self):
        """
        Indexes code hints.
        """
    
        args = index_code_helper_parser.parse_args()
        rows_to_insert = [{
            "category": args["category"],
            "tags": args["tags"],
            "purpose": args["purpose"],
            "code": args["code"],
            "created": datetime.now(
                timezone(app.config["TIMEZONE"])).strftime(
                    "%Y-%m-%dT%H:%M:%S")}]
        job = bigquery_client.load_table_from_json(
            rows_to_insert, app.config["GOOGLE_TABLE_ID"],
            job_config=bigquery_job_config)
        job.result()
        api_response = {"response": "New hint has been inserted."}
        return api_response, 200



    @api.doc()
    @api.expect(search_code_helper_parser)
    def get(self):
        """
        """

        args = search_code_helper_parser.parse_args()
        query_job = self.search_code_helpers(args)
        results = self.write_output(query_job)
        return {"response": results}, 200


    def set_search_query(self, args, page_order, page_size):
        """
        """

        search_query = ("""
            SELECT * FROM {}
            """.format(app.config["GOOGLE_TABLE_ID"]))
        if args["category"] is not None:
            search_query += """ WHERE category='{}'""".format(
                args["category"])
            if args["purpose"] is not None:
                search_query += """ AND purpose LIKE '%{}%'""".format(
                    args["purpose"]) # ADD tokenization and words cleaningfor search engine
        elif args["purpose"] is not None:
            search_query += """ WHERE purpose LIKE '%{}%'""".format(
                args["purpose"])
        search_query += """ ORDER BY created DESC LIMIT {} OFFSET {}""".format(
            page_size, page_order*page_size)
        return search_query


    def search_code_helpers(self, args):
        """
        """

        page_order = int(args["page_order"])
        page_size = int(args["page_size"])
        search_query = self.set_search_query(
            args, page_order, page_size)
        query_job = bigquery_client.query(search_query)
        return query_job
        

    def write_output(self, query_job):
        """
        """

        results = []
        for row in query_job:
            results.append({
                "category": row.category, "tags": row.tags,
                "purpose": row.purpose, "code": row.code,
                "created": row.created.strftime("%Y-%m-%dT%H:%M:%S")})
        return results
