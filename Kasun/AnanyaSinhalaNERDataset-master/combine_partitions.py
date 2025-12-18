import os
import glob

def combine_conll_partitions(input_folders, output_file):
    """
    Combine all partition files from multiple folders into one CoNLL file.
    
    Args:
        input_folders (list): List of folder paths containing partition files
        output_file (str): Path to save the combined CoNLL file
    """
    all_partitions = []
    
    # Collect all partition files from all folders
    for folder in input_folders:
        if os.path.exists(folder):
            # Find all .tsv or .conll files in the folder
            partition_files = glob.glob(os.path.join(folder, "partition_*.tsv")) + \
                            glob.glob(os.path.join(folder, "partition_*.conll"))
            
            # Sort files to maintain order
            partition_files.sort()
            all_partitions.extend(partition_files)
            print(f"Found {len(partition_files)} files in {folder}")
        else:
            print(f"Warning: Folder not found: {folder}")
    
    if not all_partitions:
        print("No partition files found!")
        return
    
    print(f"\nTotal partition files to combine: {len(all_partitions)}")
    
    # Combine all files
    total_lines = 0
    total_sentences = 0
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, partition_file in enumerate(all_partitions, 1):
            print(f"Processing {i}/{len(all_partitions)}: {os.path.basename(partition_file)}")
            
            with open(partition_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                # Count sentences (separated by blank lines)
                sentences_in_file = content.count('\n\n') + 1
                lines_in_file = len([l for l in content.split('\n') if l.strip()])
                
                total_sentences += sentences_in_file
                total_lines += lines_in_file
                
                # Write content to output file
                outfile.write(content)
                
                # Ensure there's a blank line between partition files
                if not content.endswith('\n\n'):
                    outfile.write('\n\n')
    
    print(f"\n✅ Combined CoNLL file created: {output_file}")
    print(f"📊 Total sentences: {total_sentences}")
    print(f"📊 Total lines: {total_lines}")

# Example usage
if __name__ == "__main__":
    # Define input folders
    input_folders = [
        "NewsPaper_41k",
        "Sinmin+UCSC_Final_69k"
    ]
    
    # Define output file
    output_file = "combined_sinhala_ner_dataset.conll"
    
    # Combine all partitions
    combine_conll_partitions(input_folders, output_file)