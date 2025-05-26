def load_data_from_csv(file_path):
    """
    Load data from a CSV file and return it as a list of dictionaries.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    import csv
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    
    return data