-- PRIMEIRA QUERY (QUARTO TRIMESTRE 2024)
SELECT cad.razao_social,
       dem.descricao AS descr, 
       ROUND(SUM(dem.vl_saldo_final - dem.vl_saldo_inicial)::NUMERIC, 2) AS resultado_periodo
FROM public.relatorio_cadop AS cad
JOIN public.demonstracoes_contabeis AS dem
     ON cad.registro_ans = dem.reg_ans
WHERE LOWER(dem.descricao) LIKE LOWER('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO%')
     AND dem.data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY cad.razao_social, descr
ORDER BY resultado_periodo ASC
LIMIT 10;

-- SEGUNDA QUERY (ANO INTEIRO 2024)
SELECT cad.razao_social,
       dem.descricao AS descr, 
       ROUND(SUM(dem.vl_saldo_final - dem.vl_saldo_inicial)::NUMERIC, 2) AS resultado_periodo
FROM public.relatorio_cadop AS cad
JOIN public.demonstracoes_contabeis AS dem
     ON cad.registro_ans = dem.reg_ans
WHERE LOWER(dem.descricao) LIKE LOWER('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO%')
     AND dem.data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY cad.razao_social, descr
ORDER BY resultado_periodo ASC
LIMIT 10;