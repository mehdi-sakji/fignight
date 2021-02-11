import requests
from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from google.cloud import bigquery
from google.oauth2 import service_account


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.url_map.strict_slashes = False

CORS(app, supports_credentials=True)

api = Api(
    app=app, doc="/doc_api", version='0.1', title='Casacoding API',
    description='Casacoding API', validate=True)

# Google BigQuery client
credentials = service_account.Credentials.from_service_account_file(
    app.config["GOOGLE_SERVICE_ACCOUNT_KEY_PATH"])
bigquery_client = bigquery.Client(
    credentials=credentials, project=app.config["GOOGLE_PROJECT_ID"])

# Google BigQuery job config
bigquery_job_config = bigquery.LoadJobConfig()
bigquery_job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
bigquery_job_config.schema_update_options = [
    bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION]

from app import views, parsers
