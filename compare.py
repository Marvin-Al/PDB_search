import csv
import sys

old_library = []
search_library =[]
old_library_file = "/workspaces/133378046/PDB/new_idea/old_library.csv"
search_library_file = "/workspaces/133378046/PDB/new_idea/list_pre2017_library_final.csv"


with open(old_library_file, 'r') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        entry = row[0]
        old_library.append(entry)

with open(search_library_file, 'r') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    for row in reader2:
        i = row['Entry'].lower()
        search_library.append(i)


matches = 0
wrong = 0
count = 0
for i in search_library:
    if i in old_library:
        matches += 1
        count += 1
    else:
        wrong += 1
        count += 1
        pass

missing = len(old_library) - matches

print("Number of matches: " + str(matches))
print("Number of wrong PDBs: " + str(wrong))
print("Number of entrys missing: " + str(missing))
print("Number of entrys in Library: " + str(count))


if len(sys.argv) > 1:
    if sys.argv[1] == "print_wrong":
        for i in search_library:
            if i not in old_library:
                print(i)

    elif sys.argv[1] == "print_matches":
        for i in search_library:
            if i in old_library:
                print(i)

    elif sys.argv[1] == "print_missing":
        for i in old_library:
            if i not in search_library:
                print(i)
else:
    pass
