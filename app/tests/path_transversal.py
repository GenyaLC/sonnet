from generic.threads import run_threaded
from generic.crawler import get_accesible_urls
from requests import Session


def file_path_traversal_simple_case():
    url = [""]
    s = Session()
    aux = run_threaded(get_accesible_urls, url, url, s)
    print(f"RESULT :{aux}")
    # print(f"RESULT: {links}")