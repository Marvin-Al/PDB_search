PDB Library search Project - as of 01.12.2023


Overview: This code makes a specific API request to the Protein Data Bank (https://www.rcsb.org/) and retrieves a list of sequences matching a specific search query.
          Further code then retrieves the seqences and returns a list of non-redundant entries with their sequence.

1. run get_new_library.py
This code retrieves a list of PDB entries matching a specific search query and stores them in a csv file.
    a) rename the output_file if necessary
    b) adapt the search query to other search parameters if wanted: https://search.rcsb.org/#search-api


2. run add_sequence.py
This code takes a csv of PBD entrys as input and searches for the first protein sequences it finds on the PDB server. It then saves a new csv file with the PDB entry and its first protein sequence.
    a) input file is the output from get_new_libray.py
    b) rename the output_file if necessary


3. run check_redundancy.py
This code takes a csv file as input with PDB entries and sequences. It then checks the sequences for redundancy using the hobohm algorithm.
It returns a csv containing only the non-redundant sequences.
    a) input file is the output from add_sequence.py
    b) rename the output_file if necessary
    c) sequence similarity cut-off is set to 0.8 and can be changed in hobohm.py

4. optional compare.py
This code can compare different csv files and compare the lists of PDB enties and returns the number of matches, missing and wrong entries
    a) rename the input files that you want to compare
    b) the code can be run optional with comands in argv[1] to print the entries by adding print_matches, print_missing, print_wrong
