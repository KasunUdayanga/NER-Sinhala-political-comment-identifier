# File paths
input_file = "sinhala_dataset_balanced.conll"      # your file with B-Other
output_file = "clean_datasets with O.conll"   # corrected file

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        line = line.strip()
        if not line:  # keep blank lines (sentence boundary)
            outfile.write("\n")
            continue

        try:
            token, tag = line.split()
        except ValueError:
            print(f"Skipping malformed line: {line}")
            continue

        # Replace B-Other with O
        if tag == "B-Other" or tag == "I-Other":
            tag = "O"

        outfile.write(f"{token} {tag}\n")

print("✅ Dataset cleaned and saved to", output_file)
