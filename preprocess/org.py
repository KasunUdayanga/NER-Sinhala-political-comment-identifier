# Input and output files
input_file = "../PoliticalParties.csv"   # one org name per line
output_file = "org_dataset.conll"  # formatted NER dataset

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        org = line.strip()
        if not org:
            continue

        tokens = org.split()
        for i, token in enumerate(tokens):
            tag = "B-ORG" if i == 0 else "I-ORG"
            outfile.write(f"{token} {tag}\n")

        # blank line after each organization
        outfile.write("\n")

print("✅ Organizations converted to ORG dataset:", output_file)
