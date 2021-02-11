from app import api

index_code_helper_parser = api.parser()
index_code_helper_parser.add_argument(
    'category', type=str, required=True)
index_code_helper_parser.add_argument(
    'tags', type=str, required=True)
index_code_helper_parser.add_argument(
    'purpose', type=str, required=True)
index_code_helper_parser.add_argument(
    'code', type=str, required=True)

search_code_helper_parser = api.parser()
search_code_helper_parser.add_argument(
    'category', type=str, location='args')
search_code_helper_parser.add_argument(
    'purpose', type=str, location='args')
search_code_helper_parser.add_argument(
    'tags', type=str, location='args')
search_code_helper_parser.add_argument(
    'code', type=str, location='args')
search_code_helper_parser.add_argument(
    'page_order', type=int, location='args', required=True)
search_code_helper_parser.add_argument(
    'page_size', type=int, location='args', required=True)
