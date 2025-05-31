import os
import yaml
import pandas as pd
from collections import defaultdict

DATA_DIR = r'E:\StockAnalysis\DATA_DIR'
OUTPUT_DIR = 'output_csvs_combined'
os.makedirs(OUTPUT_DIR, exist_ok=True)

symbol_data = defaultdict(list)

# Traverse through all subdirectories
for root, dirs, files in os.walk(DATA_DIR):
    for filename in files:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            filepath = os.path.join(root, filename)
            date_part = filename.split('_')[0]

            try:
                with open(filepath, 'r') as file:
                    content = yaml.safe_load(file)

                    stock_record = {}
                    for entry in content:
                        if isinstance(entry, dict):
                            for key, value in entry.items():
                                if key.lower() == 'ticker':
                                    if 'Ticker' in stock_record:
                                        symbol = stock_record['Ticker']
                                        stock_record['date'] = date_part
                                        symbol_data[symbol].append(stock_record)
                                        stock_record = {}
                                    stock_record['Ticker'] = value
                                else:
                                    stock_record[key] = value
                        else:
                            print(f"Skipped unexpected entry in {filename}: {entry}")

                    if 'Ticker' in stock_record:
                        symbol = stock_record['Ticker']
                        stock_record['date'] = date_part
                        symbol_data[symbol].append(stock_record)

            except Exception as e:
                print(f"Error reading {filename}: {e}")

# Save all collected records per symbol
for symbol, records in symbol_data.items():
    df = pd.DataFrame(records)
    df.sort_values('date', inplace=True)
    df.to_csv(os.path.join(OUTPUT_DIR, f'{symbol}.csv'), index=False)
    print(f"Saved {symbol}.csv")

print("All YAML files from all subfolders have been processed.")
