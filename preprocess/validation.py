# File paths
input_file = "clean_datasets with O.conll"   # original dataset
output_file = "sinhala_ner_dataset_cleaned.conll"  # cleaned dataset

# Allowed labels
allowed_labels = {"B-PER", "I-PER", "B-LOC", "I-LOC", "B-ORG", "I-ORG", "O"}

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    line_num = 0
    errors = 0
    for line in infile:
        line_num += 1
        line = line.strip()

        # Keep blank lines
        if not line:
            outfile.write("\n")
            continue

        parts = line.split()
        if len(parts) != 2:
            print(f"[Line {line_num}] Malformed line (not 2 columns): {line}")
            errors += 1
            continue

        token, label = parts

        # Replace B-Other/I-Other with O
        if label in {"B-Other", "I-Other"}:
            label = "O"

        # Check for unknown labels
        if label not in allowed_labels:
            print(f"[Line {line_num}] Unknown label '{label}' for token '{token}'")
            errors += 1

        outfile.write(f"{token} {label}\n")

print(f"✅ Validation finished. Cleaned dataset saved to {output_file}")
print(f"⚠️ Total issues found: {errors}")
