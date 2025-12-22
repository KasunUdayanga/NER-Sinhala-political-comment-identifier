import csv

def convert_locations_to_labeled(input_csv, output_txt):
    """
    Convert locations CSV to labeled text format with B-LOC tags
    
    Args:
        input_csv: Path to input CSV file with id,name_si columns
        output_txt: Path to output text file
    """
    with open(input_csv, 'r', encoding='utf-8') as csv_file, \
         open(output_txt, 'w', encoding='utf-8') as txt_file:
        
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            location_name = row['name_si'].strip()
            if location_name:
                txt_file.write(f"{location_name} B-LOC\n")
    
    print(f"✅ Conversion completed! File saved as '{output_txt}'")

# Example usage
input_csv = "cities_name_si.csv"  # Your input CSV file
output_txt = "Locations_labeled_space.txt"  # Output file

convert_locations_to_labeled(input_csv, output_txt)