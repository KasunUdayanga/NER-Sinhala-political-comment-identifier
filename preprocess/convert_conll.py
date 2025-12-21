import json

def convert_conll_to_jsonl(input_file, output_file):
    dataset = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_tokens = []
    current_tags = []

    for line in lines:
        line = line.strip()
        
        if not line:
            if current_tokens:
                dataset.append({"tokens": current_tokens, "ner_tags": current_tags})
                current_tokens = []
                current_tags = []
            continue

        parts = line.split()
        if len(parts) >= 2:
            token = parts[0]
            tag = parts[1]
            current_tokens.append(token)
            current_tags.append(tag)

    if current_tokens:
        dataset.append({"tokens": current_tokens, "ner_tags": current_tags})

    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in dataset:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

convert_conll_to_jsonl("./sinhala_ner_dataset_cleaned.conll", "Sinhala_NER.jsonl")
print("✅ Conversion completed! File saved as 'Sinhala_NER.jsonl'")