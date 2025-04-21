drop table if exists spd_grcl.query_impala_2153386;

-- Criação da tabela externa
CREATE EXTERNAL TABLE spd_grcl.query_impala_2153386 (
    cd_cnpj STRING,
    nm_tipo_estabelecimento STRING,
    dt_abertura STRING,
    nm_empresarial STRING,
    nm_fantasia STRING,
    nm_porte STRING,
    vl_capital_social STRING,
    cd_natureza_juridica STRING,
    nm_natureza_juridica STRING,
    ed_cnpj_esta_cep STRING,
    ed_municipio STRING,
    ed_uf STRING,
    nm_situacao_cadastral STRING,
    nm_regiao_politica STRING,
    cd_cnae STRING,
    cd_nivel1_secao STRING,
    cd_nivel2_divisao STRING,
    cd_nivel3_grupo STRING,
    cd_nivel4_classe STRING,
    cd_nivel5_subclasse STRING,
    nm_nivel1_secao STRING,
    nm_nivel2_divisao STRING,
    nm_nivel3_grupo STRING,
    nm_nivel4_classe STRING,
    nm_nivel5_subclasse STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' ESCAPED BY '\\' LINES TERMINATED BY '\n' STORED AS TEXTFILE LOCATION '/user/02246149592/cnpj';

INSERT
    OVERWRITE TABLE spd_grcl.query_impala_2153386
SELECT
    DISTINCT r.cd_cnpj,
    r.nm_tipo_estabelecimento,
    CAST(r.dt_abertura AS STRING) AS dt_abertura,
    r.nm_empresarial,
    r.nm_fantasia,
    r.nm_porte,
    CAST(r.vl_capital_social AS STRING) AS vl_capital_social,
    r.cd_natureza_juridica,
    r.nm_natureza_juridica,
    r.ed_cnpj_esta_cep,
    r.ed_municipio,
    r.ed_uf,
    r.nm_situacao_cadastral,
    r.nm_regiao_politica,
    c.cd_cnae,
    c.cd_nivel1_secao,
    c.cd_nivel2_divisao,
    c.cd_nivel3_grupo,
    c.cd_nivel4_classe,
    c.cd_nivel5_subclasse,
    c.nm_nivel1_secao,
    c.nm_nivel2_divisao,
    c.nm_nivel3_grupo,
    c.nm_nivel4_classe,
    c.nm_nivel5_subclasse
FROM
    serprodata.dm_pj_rfb r
    LEFT JOIN serprodata.dm_cnae c ON c.cd_cnpj = r.cd_cnpj
                                    and LOWER(in_principal) = 'sim';