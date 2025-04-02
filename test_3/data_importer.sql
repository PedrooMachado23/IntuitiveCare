COPY relatorio_cadop FROM 'C:\Users\Pedro Machado\Documents\dev\my_repos\IntuitiveCareDesafio\test_3\data\relatorio_cadop.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', QUOTE '"', NULL 'NULL'); -- parametros adicionais por erro de formatação do arquivo original

-- é necessário identificar pois a database tem uma coluna a mais que o csv (coluna id que gera registros automaticamente)
COPY demonstracoes_contabeis(
    data,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
) 
FROM 'C:/Users/Pedro Machado/Documents/dev/my_repos/IntuitiveCareDesafio/test_3/data/demonstracoes_contabeis_wrapped.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';');