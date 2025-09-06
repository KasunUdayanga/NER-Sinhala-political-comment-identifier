import random

# Load dataset in CoNLL format
def load_dataset(file_path):
    dataset, sentence = [], []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if sentence:
                    dataset.append(sentence)
                    sentence = []
                continue
            token, tag = line.split()
            sentence.append((token, tag))
    return dataset

# Count entity types
def count_entities(dataset):
    counts = {"PER": 0, "LOC": 0, "ORG": 0}
    for sentence in dataset:
        for _, tag in sentence:
            if tag.endswith("PER"):
                counts["PER"] += 1
            elif tag.endswith("LOC"):
                counts["LOC"] += 1
            elif tag.endswith("ORG"):
                counts["ORG"] += 1
    return counts

# Oversample smaller classes
def balance_dataset(dataset):
    per_sentences = [s for s in dataset if any(tag.endswith("PER") for _, tag in s)]
    loc_sentences = [s for s in dataset if any(tag.endswith("LOC") for _, tag in s)]
    org_sentences = [s for s in dataset if any(tag.endswith("ORG") for _, tag in s)]

    max_size = max(len(per_sentences), len(loc_sentences), len(org_sentences))

    def oversample(data, target_size):
        return data * (target_size // len(data)) + random.sample(data, target_size % len(data))

    balanced = oversample(per_sentences, max_size) + \
               oversample(loc_sentences, max_size) + \
               oversample(org_sentences, max_size)

    random.shuffle(balanced)
    return balanced

# Save back to CoNLL
def save_dataset(dataset, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for sentence in dataset:
            for token, tag in sentence:
                f.write(f"{token} {tag}\n")
            f.write("\n")

# Run pipeline
input_file = "deduplicated_dataset.txt"
output_file = "sinhala_dataset_balanced.conll"

dataset = load_dataset(input_file)
print("Before balancing:", count_entities(dataset))

balanced = balance_dataset(dataset)
print("After balancing:", count_entities(balanced))

save_dataset(balanced, output_file)
print("✅ Balanced dataset saved to", output_file)
