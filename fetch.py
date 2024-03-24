def query_entscheidsuche(query_term):
    url = "https://entscheidsuche.ch/_search.php"

    #"fields":["title.*^5", "abstract.*^3","meta.*^10","attachment.content","reference^3"]
    
    # Adjusted query with query_string for more flexibility
    query_term = f'"{query_term}"' # to work around a bug in entscheidsuche
    query = {
            "size":1,
            "_source":{
                "excludes":[
                    "attachment.content"
                ]
            },
            "track_total_hits":"true",
            "query":{
                "bool":{
                    "must":{
                        "query_string":{
                        "query": query_term,
                        "default_operator":"AND",
                        "type":"cross_fields",
                        "fields":[
                            "title.*^5"
                        ]
                        }
                    },
                    "filter":{
                        "terms":{
                        "hierarchy":[
                            "CH_BGer",
                            "CH_BGE",
                            "CH_BVGE"
                        ]
                        }
                    }
                }
            },
            "sort":[
                {
                    "_score":"desc"
                },
                {
                    "id":"desc"
                }
            ],
            "highlight":{
                "fields":{
                    "title.de":{
                        "number_of_fragments":0
                    },
                    "abstract.de":{
                        "number_of_fragments":0
                    },
                    "attachment.content":{
                        
                    }
                }
            },
            "aggs":{
                "language":{
                    "terms":{
                        "size":3,
                        "field":"attachment.language"
                    }
                },
                "edatum":{
                    "date_histogram":{
                        "calendar_interval":"quarter",
                        "field":"date"
                    }
                },
                "min_edatum":{
                    "min":{
                        "field":"date"
                    }
                },
                "max_edatum":{
                    "max":{
                        "field":"date"
                    }
                }
            }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(query))
    
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
    # Fetch the HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:
        # If the server does not provide the charset, you might need to set it manually:
        # response.encoding = 'utf-8'

        # Alternatively, decode manually using the correct encoding
        html_content = response.content.decode('utf-8')

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract text from the parsed HTML
        text = soup.get_text(separator='\n', strip=True)
        
        return text
    else:
        return(f"Failed to fetch the document. Status code: {response.status_code}")
