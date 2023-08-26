import os
import json
from tqdm import tqdm
import csv
import pandas as pd
import re

csv_folder = "D:\KULIAH\RISET STKI 2023\Web Scrapping\Scraping by Subjects\FileCSV"
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

cats = os.listdir('D:\KULIAH\RISET STKI 2023\Web Scrapping\Scraping by Subjects\output')

def extract_keywords(abstract):
    match = re.search(r"Keywords: (.+)", abstract, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

for cat in tqdm(cats):
    if not os.path.exists(os.path.join(csv_folder, cat)):
        os.makedirs(os.path.join(csv_folder, cat))
    
    json_path = os.path.join('D:\KULIAH\RISET STKI 2023\Web Scrapping\Scraping by Subjects\output', cat)
    
    with open(json_path, "r", encoding="utf-8") as f:
        data_list = json.load(f)
        
        csv_filename = f"{os.path.splitext(cat)[0]}.csv"
        csv_path = os.path.join(csv_folder, cat, csv_filename)
        
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            
            field_titles = ["division", "title", "abstract", "subjects", "publication", "date", "keywords"]
            csv_writer.writerow(field_titles)
            
            for idx, data in enumerate(data_list):
                division = ", ".join(data.get("divisions", []))
                title = data.get("title", "")
                abstract = data.get("abstract", "")
                subjects = ", ".join(data.get("subjects", []))
                publication = data.get("publication", "")
                date = data.get("date", "")
                keywords = extract_keywords(abstract)
                
                values = [division, title, abstract, subjects, publication, date, keywords]
                csv_writer.writerow(values)