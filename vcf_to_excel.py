import os
import pandas as pd

def vcf_to_excel_with_meta(vcf_file, excel_file):
    with open(vcf_file, 'r') as vcf:
        lines = vcf.readlines()

    # Separate meta, header, and data lines
    meta_lines = [line.strip() for line in lines if line.startswith('##')]
    header_line = [line for line in lines if line.startswith('#') and not line.startswith('##')][0].strip()
    data_lines = [line.strip() for line in lines if not line.startswith('#')]

    # Extract column names from the header line
    column_names = header_line.lstrip('#').split('\t')

    # Parse the data lines into a list of dictionaries
    data = []
    for line in data_lines:
        fields = line.split('\t')
        data.append(dict(zip(column_names, fields)))

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Create a meta section DataFrame
    meta_data = {"Meta Information": meta_lines}
    meta_df = pd.DataFrame(meta_data)

    # Save meta information to a separate sheet or combine in the same Excel file
    with pd.ExcelWriter(excel_file) as writer:
        meta_df.to_excel(writer, sheet_name="Meta Information", index=False)
        df.to_excel(writer, sheet_name="VCF Data", index=False)

    print(f"Converted {vcf_file} to {excel_file} with meta information.")

# Prompt the user to input the VCF file path
vcf_path = input("Enter the path to the VCF file: ").strip('"')  # 입력값에서 큰따옴표 제거
output_folder = input("Enter the folder path to save the Excel file: ").strip('"')  # 입력값에서 큰따옴표 제거

# Automatically generate the Excel file name based on the VCF file name
excel_filename = os.path.basename(vcf_path).replace('.vcf', '.xlsx')
excel_path = os.path.join(output_folder, excel_filename)

# Call the conversion function
vcf_to_excel_with_meta(vcf_path, excel_path)
