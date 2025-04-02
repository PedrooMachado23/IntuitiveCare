CREATE TABLE relatorio_cadop(
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf VARCHAR(255),
    cep VARCHAR(255),
    ddd VARCHAR(255),
    telefone VARCHAR(255),
    fax VARCHAR(255),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(255),
    data_registro_ans VARCHAR(255)
);

CREATE TABLE demonstracoes_contabeis(
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans INT,
    cd_conta_contabil INT,
    descricao VARCHAR(255),
    vl_saldo_inicial DOUBLE PRECISION,
    vl_saldo_final DOUBLE PRECISION,
    CONSTRAINT fk_reg_ans FOREIGN KEY (reg_ans) REFERENCES relatorio_cadop(registro_ans)
);
