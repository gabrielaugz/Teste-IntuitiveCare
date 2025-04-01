-- despesas.sql
CREATE TABLE despesas (
    id SERIAL PRIMARY KEY,
    operadora_registro_ans VARCHAR(50),
    data DATE,
    categoria VARCHAR(255),
    valor NUMERIC(15,2),
    FOREIGN KEY (operadora_registro_ans) REFERENCES operadoras_ans(registro_ans)
);