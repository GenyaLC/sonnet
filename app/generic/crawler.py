from lxml import html
import requests
import concurrent.futures


def get_accesible_urls(url: str, base_url: str, session: requests.Session) -> dict:
    if "http" not in url:
        base_url = base_url + url

    r = session.get(url)
    html_content = r.content
    tree = html.fromstring(html_content)
    links = set(tree.xpath("//a/@href"))
    results = {}
    for link in links:
        if (
            "#" in link
            or "/" == link
            or "?" in link
            or "http" in link
            and base_url not in link
        ):
            continue
        elif "http" not in link:
            if url[-1] == "/" and link[0] == "/":
                results[link] = {"status": r.ok, "url": url[:-1] + link}
            else:
                results[link] = {"status": r.ok, "url": url + link}
        else:
            results[link] = {"status": r.ok, "url": link}
    return results


def _get_links_from_domain(url: str, session: requests.Session):
    results = {}

    r = session.get(url)

    results[url] = {"status": r.ok, "url": url}
    new_results = get_accesible_urls(url, url, session)

    while set(new_results.keys()).difference(set(results.keys())) != set():
        new_links = set(new_results.keys())
        new_links.difference_update(set(results.keys()))
        new_urls = {new_results[x]["url"] for x in new_links}
        results.update(new_results)
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=len(new_urls)
        ) as executor:
            futures = {
                executor.submit(get_accesible_urls, i, url, session): i
                for i in new_urls
            }

        for future in concurrent.futures.as_completed(futures):
            thread_name = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"Thread {thread_name} generated an exception: {exc}")
            else:
                new_results.update(result)
        results.update(new_results)
    return results
