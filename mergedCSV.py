import pandas as pd
import os

cats = os.listdir('D:\KULIAH\RISET STKI 2023\Scrapping by Subjects\File CSV')

data_frames = []

for i in cats:
    # print(i)
    cat_folder = f"D:/KULIAH/RISET STKI 2023/Scrapping by Subjects/File CSV/{i}/"
    for file in os.listdir(cat_folder):
        if file.endswith(".csv"):
            csv_path = os.path.join(cat_folder, file)
            df = pd.read_csv(csv_path)
            data_frames.append(df)

merged_df = pd.concat(data_frames, ignore_index=True)
output_csv_path = "merged_data.csv"
merged_df.to_csv(output_csv_path, index=False)

print('done')