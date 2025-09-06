# Input and output files
input_file = "../PoliticianNames.csv"       # each line = full name
output_file = "persons.conll"  # formatted NER dataset

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        name = line.strip()
        if not name:
            continue

        tokens = name.split()
        for i, token in enumerate(tokens):
            tag = "B-PER" if i == 0 else "I-PER"
            outfile.write(f"{token} {tag}\n")

        # blank line after each person
        outfile.write("\n")

print("✅ Names converted to PER dataset:", output_file)
