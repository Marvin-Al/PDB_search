import json
import requests
import csv

output_file = "new_library.csv"

    # Define the base URL of the search endpoint
base_url = "https://search.rcsb.org/rcsbsearch/v2/query"

    # Define the search request as a JSON object
search_request ={
  "query": {
    "type": "group",
    "logical_operator": "and",
    "nodes": [
      {
        "type": "group",
        "nodes": [
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "entity_poly.rcsb_entity_polymer_type",
              "operator": "exact_match",
              "negation": False,
              "value": "Protein"
            }
          },
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "entity_poly.rcsb_sample_sequence_length",
              "operator": "greater_or_equal",
              "negation": False,
              "value": 10
            }
          }
        ],
        "logical_operator": "and"
      },
      {
        "type": "group",
        "nodes": [
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "entity_poly.rcsb_entity_polymer_type",
              "operator": "exact_match",
              "negation": False,
              "value": "RNA"
            }
          },
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "entity_poly.rcsb_sample_sequence_length",
              "operator": "greater_or_equal",
              "negation": False,
              "value": 10
            }
          }
        ],
        "logical_operator": "and"
      },

      {
       "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "struct_keywords.pdbx_keywords",
         "operator": "contains_words",
           "negation": True,
          "value": "ribosome, ribosomal, Ribosome, Ribosome"
        }
      },
      {
        "type": "terminal",
        "service": "text",
        "parameters": {
          "attribute": "rcsb_accession_info.initial_release_date",
          "operator": "greater",
          "negation": False,
          "value": "2017-06-01"
        }
      },
      {
        "type": "group",
        "nodes": [
          {
            "type": "terminal",
            "service": "text",
            "parameters": {
              "attribute": "exptl.method",
              "operator": "exact_match",
              "negation": False,
              "value": "X-RAY DIFFRACTION"
            }
          },
          {
           "service": "text",

            "parameters": {
              "attribute": "exptl.method",
              "operator": "exact_match",
              "negation": False,
              "value": "SOLUTION NMR"
            }
          }
        ],
        "logical_operator": "or"
      }
    ],
    "label": "text"
  },
  "request_options": {
        "return_all_hits": True
      },
      "return_type": "entry"
}


    # Convert the search request to a JSON string
json_payload = json.dumps(search_request)

    # Construct the complete URL with the JSON payload
url = f"{base_url}?json={json_payload}"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
            # Parse the JSON response
            results = response.json()
            with open(output_file, "a") as file:
                writer = csv.DictWriter(file, fieldnames = ["entry"])
                writer.writeheader()
                for result in results['result_set']:
                    writer.writerow({"entry": result["identifier"]})

    else:
        print(f"HTTP Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")

