import pandas as pd
import re
import pdfplumber
from zipfile import ZipFile
import os
from typing import List

class PDFDataExtractor:
    columns: List[str] = [
        'PROCEDIMENTO', 'RN(alteração)', 'VIGÊNCIA', 'OD', 'AMB', 'HCO', 
        'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO'
    ]
    data: List[List[str]]
    pdf_path: str
    csv_path: str

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.data = []
        self.csv_path = os.path.join('test_2', 'extracted_data.csv')

    def extract_data(self):
        
        with pdfplumber.open(self.pdf_path) as pdf:
            #primeira e segunda página não tem tabela
            for page in pdf.pages[2:]:
                table = page.extract_table()
                if table:
                    for row in table[1:]:
                        formatted_row = [
                            #remove '\n' de cada item
                            re.sub(r'(?<=\S)\n(?=\S)', ' ', cell) if cell else '-' 
                            for cell in row[:13]
                        ]
                        self.data.append(formatted_row)

    def process_data(self):
        
        df = pd.DataFrame(data=self.data, columns=self.columns)
        
        #mudando o nome de acordo com o requisito
        df['OD'] = df['OD'].apply(lambda x: x.replace('OD', 'Seg. Odontológica'))
        df['AMB'] = df['AMB'].apply(lambda x: x.replace('AMB', 'Seg. Ambulatorial'))
        
        return df

    #criando o csv
    def save_to_csv(self, df: pd.DataFrame):
        os.makedirs('test_2', exist_ok=True)
        df.to_csv(self.csv_path, sep=';', index=False)

    #comprimindo o csv
    def compress_files(self):
        zip_path = os.path.join('test_2', 'extracted_data.zip')
        with ZipFile(zip_path, 'w') as zip_file:
            zip_file.write(self.csv_path, os.path.basename(self.csv_path))


if __name__ == '__main__':
    extractor = PDFDataExtractor(
        pdf_path=r'test_1\pdf_files\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    )
    extractor.extract_data()
    df = extractor.process_data()
    extractor.save_to_csv(df)
    extractor.compress_files()