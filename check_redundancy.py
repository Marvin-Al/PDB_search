import csv
from hobohm import hobohm1
from tqdm import tqdm


input_file = "new_library_seq.csv"
output_file = "nr_new_library_seq.csv"
#parameter: in hobohm for sequence similarity set to 0.8


entries_and_sequences = []
# Read entries and sequences from the input CSV
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    for row in tqdm(reader, desc="Reading CSV", unit="rows"):
        entry = row["entry"]
        sequence = row["sequence"]
        entries_and_sequences.append({"entry": entry, "sequence": sequence})

# Process the sequences using hobohm1
nr_sequences = hobohm1([entry["sequence"] for entry in entries_and_sequences])

# Create a dictionary to map sequences to their corresponding entries
sequence_to_entry = {entry["sequence"]: entry["entry"] for entry in entries_and_sequences}

# Write non-redundant sequences and their corresponding entries to a new CSV file
with open(output_file, "w", newline="") as outfile:
    fieldnames = ["entry", "sequence"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for seq in tqdm(nr_sequences, desc="Writing CSV", unit="sequences"):
        entry = sequence_to_entry[seq.seq]
        writer.writerow({"entry": entry, "sequence": seq.seq})
