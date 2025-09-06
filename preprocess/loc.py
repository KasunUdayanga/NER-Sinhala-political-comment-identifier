import csv

# Input and output files
input_file = "../cities_name_si.csv"       # your file: 2146,තාරාපුරම්
output_file = "loc.conll"    # NER dataset format

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    for row in reader:
        if len(row) < 2:
            continue
        location = row[1].strip()
        
        # If location has spaces (multi-word), tag first as B-LOC, rest as I-LOC
        tokens = location.split()
        for i, token in enumerate(tokens):
            tag = "B-LOC" if i == 0 else "I-LOC"
            outfile.write(f"{token} {tag}\n")
        
        # Sentence boundary (blank line after each location)
        outfile.write("\n")

print("✅ Locations converted to NER dataset format:", output_file)
