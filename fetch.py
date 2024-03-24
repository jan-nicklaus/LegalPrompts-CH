import requests
import json
from bs4 import BeautifulSoup
def query_entscheidsuche(query_term):
    url = "https://entscheidsuche.ch/_search.php"
    query = {
        "size": 1,
        "_source": {"excludes": ["attachment.content"]},
        "track_total_hits": "true",
        "query": {
            "bool": {
                "must": {
                    "query_string": {
                        "query": query_term,
                        "default_operator": "AND",
                        "type": "cross_fields",
                        "fields": [
                            "title.*^5",
                            "abstract.*^3",
                            "meta.*^10",
                            "attachment.content",
                            "reference^3"
                        ]
                    }
                },
                "filter": {
                    "terms": {
                        "hierarchy": ["CH_BGer", "CH_BGE", "CH_BVGE"]
                    }
                }
            }
        },
        "sort": [{"_score": "desc"}, {"id": "desc"}],
        "highlight": {
            "fields": {
                "title.de": {"number_of_fragments": 0},
                "abstract.de": {"number_of_fragments": 0},
                "attachment.content": {}
            }
        },
        "aggs": {
            "language": {
                "terms": {"size": 3, "field": "attachment.language"}
            },
            "edatum": {
                "date_histogram": {"calendar_interval": "quarter", "field": "date"}
            },
            "min_edatum": {"min": {"field": "date"}},
            "max_edatum": {"max": {"field": "date"}}
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(query))
    content_url = None
    if response.status_code == 200:
        results = response.json()
        if results.get("hits", {}).get("total", {}).get("value", 0) > 0:
            for hit in results.get("hits", {}).get("hits", []):
                content_url = hit['_source']['attachment']['content_url']
                print(f"Document ID: {hit['_id']}, Score: {hit['_score']}, Content URL: {content_url}")
        else:
            print("No results found.")
    else:
        print(f"Failed to query documents. Status code: {response.status_code}")
    return content_url
def fetch_and_parse_html(url):
    if url is None:
        return "No URL provided"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content.decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text
    else:
        print(f"Failed to fetch the document. Status code: {response.status_code}")
        return None