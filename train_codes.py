import pandas as pd

def merge_excel_files(file1, file2, output_file):
    # Load the specific sheets from the Excel file
    df1 = pd.read_excel(file1, sheet_name='10_11_ICD')
    df2 = pd.read_excel(file2, sheet_name='Sheet1')  # Assuming the relevant data is in Sheet1 of the second file

    # Merge the two DataFrames on 'Code' from df2 and 'icd11Code' from df1
    merged_df = pd.merge(df1, df2, left_on='icd11Code', right_on='Code', how='outer')

    # Drop the 'Code' column from the merged DataFrame (it's redundant after the merge)
    merged_df.drop(columns=['Code'], inplace=True)

    # Reorder the columns as specified
    columns_order = ['icd9Code', 'icd10Code', 'icd11Code', 'Title', 'Definition', 'Inclusion', 'Exclusion', 'IndexTerms']
    merged_df = merged_df[columns_order]

    # Fill missing values in icd11Code with NaN
    merged_df['icd11Code'] = merged_df['icd11Code'].fillna('Null')

    # Write the result to a new Excel file
    merged_df.to_excel(output_file, index=False)

# Example usage
file1 = '9_10_11_ICD_CODESxlsx.xlsx'
file2 = 'en_icd_results.xlsx' 
output_file = 'output.xlsx' 

merge_excel_files(file1, file2, output_file)
