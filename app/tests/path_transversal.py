from generic.threads import run_threaded
from generic.crawler import get_accesible_urls
from requests import Session


def file_path_traversal_simple_case():
    url = "https://0acd00ed04f9b8bd863aefb800e8003a.web-security-academy.net/"
    url = "https://cyberdatalab.um.es"
    links = set()
    s = Session()
    aux = get_accesible_urls(url, url, s)
    while links != aux:
        links = aux
        aux = run_threaded(get_accesible_urls, links, base_url=url, session=s)
        print(f"AUX :{aux}")
    print(f"RESULT: {links}")