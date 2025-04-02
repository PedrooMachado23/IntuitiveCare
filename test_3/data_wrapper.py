import os
import zipfile as zp
import pandas as pd

def main():
    """
        Juntar todos os arquivos csv em um só e fazer as mudanças necessárias para viabilizar e facilitar as queries
    """
    zip_folder = r'test_3\data\zips'
    zip_paths = []
    dataframes = []

    #pegando os caminhos dos arquivos baixados
    for root, dirs, files in os.walk(zip_folder):
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(root, file)
                zip_paths.append(file_path)

    #montando os dataframes
    for path in zip_paths:
        with zp.ZipFile(path, 'r') as zip_ref:
            for filename in zip_ref.namelist():
                with zip_ref.open(filename) as csv:
                    file_dataframe = pd.read_csv(csv, sep=';')
                    dataframes.append(file_dataframe)

    
    def transform_to_float(string: str):
        #formata string e transforma para float
        if isinstance(string, str):
            return float(string.replace('.', '').replace(',', '.'))

    final_dataframe = pd.concat(dataframes, ignore_index=True) #junta os csv lidos anteriormente
    cadop_df = pd.read_csv(r'test_3\data\relatorio_cadop.csv', sep=';')

    #para padronização das colunas com o schema da database
    final_dataframe.columns = final_dataframe.columns.str.lower()
    cadop_df.columns = cadop_df.columns.str.lower()

    final_dataframe['data'] = pd.to_datetime(final_dataframe['data'], format='mixed') #transformação em data para facilitar filtragem

    #transformando as para ser possível fazer conta
    final_dataframe[['vl_saldo_inicial', 'vl_saldo_final']] = final_dataframe[['vl_saldo_inicial', 'vl_saldo_final']].map(transform_to_float)
    final_dataframe['reg_ans'] = final_dataframe['reg_ans'].apply(lambda x: int(x))
    cadop_df['cnpj'] = cadop_df['cnpj'].apply(lambda x: str(x))
    
    #removendo registros inválidos para viabilizar o relacionamento entre as tabelas
    valid_ans = set(cadop_df['registro_ans'].unique())
    final_dataframe = final_dataframe[final_dataframe['reg_ans'].isin(valid_ans)]

    #criando os csv
    final_dataframe.to_csv(r'test_3\data\demonstracoes_contabeis_wrapped.csv', sep=';', index=False)
    cadop_df.to_csv(r'test_3\data\relatorio_cadop.csv', sep=';', index=False)

main()