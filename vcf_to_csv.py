import os
import pandas as pd

def vcf_to_csv(vcf_file, csv_file):
    with open(vcf_file, 'r') as vcf:
        lines = vcf.readlines()

    # Separate header and data lines
    header_lines = [line for line in lines if line.startswith('#')]
    data_lines = [line for line in lines if not line.startswith('#')]

    # Extract column names from the last header line
    column_names = header_lines[-1].strip().lstrip('#').split('\t')

    # Parse the data lines into a list of dictionaries
    data = []
    for line in data_lines:
        fields = line.strip().split('\t')
        data.append(dict(zip(column_names, fields)))

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Converted {vcf_file} to {csv_file}")

# 사용자로부터 경로 입력받기
vcf_path = input("VCF 파일 경로를 입력하세요: ").strip('"')  # 입력값에서 큰따옴표 제거
output_folder = input("CSV 파일을 저장할 폴더 경로를 입력하세요: ").strip('"')  # 입력값에서 큰따옴표 제거

# 자동으로 CSV 파일명 생성
csv_filename = os.path.basename(vcf_path).replace('.vcf', '.csv')
csv_path = os.path.join(output_folder, csv_filename)

# 변환 함수 호출
vcf_to_csv(vcf_path, csv_path)

