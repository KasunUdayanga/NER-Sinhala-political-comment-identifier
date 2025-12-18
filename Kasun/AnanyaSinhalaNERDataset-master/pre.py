import re
from collections import Counter

def preprocess_conll(input_file, output_file):
    """
    Preprocess CoNLL file for NER training
    """
    sentences = []
    current_sentence = []
    label_stats = Counter()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            if not line:
                if current_sentence:
                    sentences.append(current_sentence)
                    current_sentence = []
                continue
            
            parts = line.split('\t')
            if len(parts) != 2:
                print(f"⚠️ Skipping malformed line: {line}")
                continue
            
            token, label = parts[0].strip(), parts[1].strip()
            
            # Skip empty tokens
            if not token:
                continue
            
            # Normalize labels to BIO format if needed
            if label in ['LOC', 'ORG', 'PER']:
                # Check if previous token had same label
                if current_sentence and current_sentence[-1][1].endswith(label):
                    label = f'I-{label}'
                else:
                    label = f'B-{label}'
            elif label != 'O':
                print(f"⚠️ Unknown label: {label} for token: {token}")
                label = 'O'
            
            current_sentence.append((token, label))
            label_stats[label] += 1
    
    # Add last sentence
    if current_sentence:
        sentences.append(current_sentence)
    
    # Write preprocessed data
    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            for token, label in sentence:
                f.write(f"{token}\t{label}\n")
            f.write("\n")
    
    # Print statistics
    print(f"\n📊 Dataset Statistics:")
    print(f"Total sentences: {len(sentences)}")
    print(f"Total tokens: {sum(label_stats.values())}")
    print(f"\n🏷️ Label distribution:")
    for label, count in sorted(label_stats.items()):
        print(f"  {label}: {count}")
    
    return sentences, label_stats

# Run preprocessing
input_file = "combined_sinhala_ner_dataset.conll"
output_file = "preprocessed_sinhala_ner.conll"

sentences, stats = preprocess_conll(input_file, output_file)
print(f"\n✅ Preprocessed file saved: {output_file}")