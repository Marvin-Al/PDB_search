import requests
import csv
import re

# Function that returns True or False if a sequence only contains A, G, C, U, T
def is_rna(sequence):
    if 'U' in sequence:
        return True
#exclude DNA patterns
    dx_pattern = re.compile(r'.+\(D[TCGA]\).+')

    while dx_pattern.search(sequence):
        return True

    return bool(re.match(r'^[AGCU]+$', sequence))

# With a given CSV file as input, this program generates a CSV as output that has the sequence of the specified entity as documented in the PDB Databank

input_file = "new_library.csv"
output_file = "new_library_seq.csv"
entity_number = 1

# Open the output CSV in write mode to create a new file and write the header
with open(output_file, "w") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=["entry", "sequence"])
    writer.writeheader()

with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        entry = row['entry']
        entity_number = 1  # Reset entity_number for each entry
        while True:
            url = f"https://data.rcsb.org/rest/v1/core/polymer_entity/{entry}/" + str(entity_number)
            try:
                # Send an HTTP GET request to the URL
                response = requests.get(url)
                # Check if the request was successful (HTTP status code 200)
                if response.status_code == 200:
                    # Parse the JSON response
                    o = response.json()
                    seq = o['entity_poly']["pdbx_seq_one_letter_code"]
                    # Append the entry and sequence to the output CSV
                    if is_rna(seq):
                        entity_number += 1
                    else:
                        with open(output_file, "a") as new_file:  # Open the output file in append mode
                            writer = csv.DictWriter(new_file, fieldnames=["entry", "sequence"])
                            writer.writerow({"entry": entry, "sequence": seq})
                        break  # Exit the loop when a protein sequence is found
                else:
                    # Handle non-successful responses here
                    print(f"Request for entry {entry}, entity {entity_number} failed with status code {response.status_code}")
                    break  # Exit the loop when a non-successful response is received
            except requests.exceptions.RequestException as e:
                # Handle request exceptions
                print(f"Request Error for entry {entry}, entity {entity_number}: {e}")
                break  # Exit the loop when a request exception occurs
