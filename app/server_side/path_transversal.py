import requests
import lxml.html


def find_file_paths(url: str, session: requests.Session):
    response = session.get(url)
    html_content = response.content
    tree = lxml.html.fromstring(html_content)
    results = set()
    links = tree.xpath("//img/@src")
    for link in links:
        if "http" not in link:
            if url[-1] == "/" and link[0] == "/":
                results.add(url[:-1] + link)
            else:
                results.add(url + link)
        else:
            results.add(link)
    return results
