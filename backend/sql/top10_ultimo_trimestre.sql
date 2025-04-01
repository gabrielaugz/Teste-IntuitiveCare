SELECT 
    o.razao_social,
    SUM(d.valor) AS total_despesas
FROM 
    despesas d
JOIN 
    operadoras_ans o ON d.operadora_registro_ans = o.registro_ans
WHERE 
    d.categoria = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND d.data >= (CURRENT_DATE - INTERVAL '3 MONTH')
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;