import pandas as pd

def denevo():
    # File paths
    son_path = r".xlsx"
    father_path = r".xlsx"
    mother_path = r".xlsx"
    output_path = r".xlsx"

    # Load data 
    output_df = pd.read_excel(output_path)
    father_df = pd.read_excel(father_path)
    mother_df = pd.read_excel(mother_path)

    # Filter rows where FILTER column is 'PASS'
    output_df = son_df[son_df['FILTER'] == 'PASS']
    father_df = father_df[father_df['FILTER'] == 'PASS']
    mother_df = mother_df[mother_df['FILTER'] == 'PASS']

    # Select relevant columns
    output_variants = output_df[['CHROM', 'POS', 'REF', 'ALT']]
    father_variants = father_df[['CHROM', 'POS', 'REF', 'ALT']]
    mother_variants = mother_df[['CHROM', 'POS', 'REF', 'ALT']]

    # Remove duplicates
    output_variants = output_variants.drop_duplicates()
    father_variants = father_variants.drop_duplicates()
    mother_variants = mother_variants.drop_duplicates()

    # Find variants unique to the son or daughter
    denevo_variants = output_variants.merge(father_variants, how='left', indicator=True)
    denevo_variants = denevo_variants[denevo_variants['_merge'] == 'left_only']
    denevo_variants = denevo_variants.drop(columns=['_merge'])

    denevo_variants = denevo_variants.merge(mother_variants, how='left', indicator=True)
    denevo_variants = denevo_variants[denevo_variants['_merge'] == 'left_only']
    denevo_variants = denevo_variants.drop(columns=['_merge'])

    # Save the result to an Excel file
    denevo_variants.to_excel(output_path, index=False)

# Execute the function
denevo()
