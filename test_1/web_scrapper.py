import requests
import os
from bs4 import BeautifulSoup
from zipfile import ZipFile
from typing import List

class WebScrapper:
    content: str
    file_paths: List[str]

    def __init__(self, url):
        self.file_paths = []

        try:
            response = requests.get(url=url)
            if response.ok:
                self.content = response.text

        except Exception as e:
            print(f'Bad request: {e}')

    def download_pdf(self):
        #pasta para download dos arquivos
        pdf_folder = os.path.join(os.getcwd(), 'web_scrapping', 'arquivos_pdf')
        os.makedirs(pdf_folder, exist_ok=True)

        #criando um obj de html para extrair os links com facilidade
        html_obj = BeautifulSoup(self.content, 'html.parser')
        links = [link.get('href') for link in html_obj.find_all('a')]

        for link in links:
            if all(keyword in link for keyword in ['Anexo', '.pdf']):
                #donwload dos arquivos
                try:
                    pdf_content = requests.get(link).content
                except Exception as e:
                    print(f'Bad request: {e}')

                file_name = link[(link.rfind('/') + 1):]
                file_path = os.path.join(pdf_folder, file_name)
                self.file_paths.append(file_path)

                with open(file_path, 'wb') as file:
                    file.write(pdf_content)
    
    def compress_files(self):
        zip_path = os.path.join(os.getcwd(), 'web_scrapping', 'pdfs.zip')

        #comptactação em um zip
        with ZipFile(zip_path, 'w') as file:
            for path in self.file_paths:
                file.write(path, os.path.basename(path))

                

if __name__ == '__main__':
    downloader = WebScrapper('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
    downloader.download_pdf()
    downloader.compress_files()