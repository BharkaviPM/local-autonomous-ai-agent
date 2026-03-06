import os
from ddgs import DDGS

def search_web(query):

    results = []

    tavily_api_key = os.environ.get("TAVILY_API_KEY")

    if tavily_api_key:
        from tavily import TavilyClient

        client = TavilyClient(api_key=tavily_api_key)
        response = client.search(query=query, max_results=5)

        for r in response["results"]:
            results.append({
                "title": r["title"],
                "url": r["url"]
            })
    else:
        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for r in search_results:
                results.append({
                    "title": r["title"],
                    "url": r["href"]
                })

    return results
