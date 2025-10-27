# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56933b1d-1ce1-3b39-bc03-3bc63e6e6568 | -3.93153 | -50.02645 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8862cbbe-9a7a-3b11-b30e-c1aa8117e3ac | -3.1554 | -50.33516 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ae0a9216-7556-39a7-965c-434524e9a433 | -4.8322 | -48.54993 | 2025-10-27 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c22c5a0-5b06-3903-9640-da7893886417 | -3.60599 | -43.55998 | 2025-10-27 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ab73e46-ed45-3a7c-8962-4f3c8df4a2a0 | -7.88081 | -47.24856 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5fdab0d-1faf-3fd8-bdc9-63cd40194af7 | -7.23712 | -46.94707 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50afac5c-35f4-3250-8d9d-4c277d942e2f | -4.20625 | -48.35377 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e62adff-857c-37ea-becd-7efdff4c91ea | -6.42983 | -44.12261 | 2025-10-27 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3574a71f-b175-3e2f-9f49-26766bd88eed | -7.16456 | -44.85112 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f94f4e2-f61b-37c5-ab1d-db23079b42f6 | -3.36884 | -53.10702 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44351e42-8848-348e-ba4c-6f64acf66338 | -3.39505 | -45.09653 | 2025-10-27 04:32:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 489a011a-8b03-3b7d-be06-e94a182dab37 | -8.96462 | -47.18936 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9df93dde-5a21-34cc-9155-2a2b3c4f94b2 | -4.15962 | -51.08643 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d1796cc-9681-3c4f-b753-c78961d3d154 | -6.1636 | -41.56874 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d367cc64-21da-3fe3-a45e-dd3c30aa808d | -6.55519 | -41.59221 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34823353-852b-3d08-a120-4fb84f9dcd92 | -8.06904 | -46.95288 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 237f10b1-73bf-3b79-b49e-fab5e1949798 | -8.03321 | -46.7459 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d3ad82e6-98be-35bf-966b-98be597ccd80 | -5.97048 | -42.7627 | 2025-10-27 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5378881a-c658-340e-a0bc-9f9bd4c8d9a4 | -6.67567 | -41.51224 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22d0536e-744c-3bf7-abbf-318c393efe85 | -4.4737 | -43.4135 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7546df2-780b-3779-9e9f-87410a7d38fb | -7.85547 | -46.46392 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4296c40-0228-3266-adb7-e66535df079a | -4.09987 | -48.91933 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09ae34f4-ba9f-3e94-a897-4502f99945e8 | -7.03185 | -47.37265 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4d71f16-ff82-34c5-82ab-5a0004ffdee6 | -7.06304 | -46.75344 | 2025-10-27 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| de28bdd3-e9cc-397c-83eb-a467c37c8716 | -8.73842 | -49.60492 | 2025-10-27 04:32:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3012dc12-7894-3e78-87b1-746648d9c9bc | -4.70919 | -46.81968 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 339fce4a-1141-3c31-95c7-9ac1a554ccee | -7.23381 | -46.94648 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98eeca4c-3468-31f6-af34-fa38714b3c66 | -4.89445 | -48.58574 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a247accc-9f72-399b-9339-54189ee785d3 | -8.65972 | -44.7543 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3e04c09-25e5-3665-9ff3-5e0e5b61b540 | -3.42257 | -52.43198 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b8e9cba-1cee-3276-9a7c-f899666b89bf | -10.00831 | -47.11826 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74af730b-7c52-3df9-8cab-3b4a91a51400 | -9.23258 | -45.84206 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 79dd7b31-99db-34ce-b7aa-018666fc0845 | -3.94807 | -48.09117 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c72a75c-2bae-37d7-8715-06f299ecef39 | -7.84295 | -46.40994 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0314a3a9-499e-3f0a-9e5b-50a3db6406ab | -5.10666 | -43.19896 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0062c41a-9e43-3434-909a-5bd9de0a2835 | -3.09786 | -54.61611 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0500b5f-9110-3206-8f38-98618e07847d | -8.96407 | -47.19292 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d7e12d3-5a02-38c4-8800-4dd315c8a206 | -7.04623 | -43.41466 | 2025-10-27 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 723252cf-0388-31e1-b866-e905237c0b1d | -3.32513 | -52.62782 | 2025-10-27 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4eecb2a-a3d4-3a0d-a6ca-28d5f4b12462 | -7.12897 | -39.43488 | 2025-10-27 04:32:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 55bd96e9-446f-3c7b-8fa3-8ea6492a96b1 | -3.46877 | -41.30736 | 2025-10-27 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 62016e7a-999b-33ea-bae9-2a39d5430722 | -5.77938 | -42.97373 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ecba7491-ada2-3144-a7ae-7be20628ff20 | -4.4938 | -50.23011 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55abe83e-f8a0-3027-9a64-44d9e66d6ad6 | -2.97219 | -51.03044 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ab30c11-1b3d-3df2-95f1-130a9917acb0 | -5.64373 | -47.62983 | 2025-10-27 04:32:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3baaf96-5da6-32bc-a2da-38e487ec2d74 | -4.52139 | -44.04295 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 72242d1e-0fa9-31e2-b5fc-1834323c1d13 | -10.03197 | -47.16636 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d5bc9a-071b-3438-b1cc-e15d774ad415 | -8.71672 | -49.40308 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75baf7fd-b84e-3ed0-97cc-0acf1c191899 | -7.6851 | -46.33718 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90977177-7cc9-382f-89c2-d65dec5ffe49 | -7.83305 | -46.49755 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2bb6bfbb-1ba0-3edb-a470-06bece6acfe2 | -3.95137 | -49.01603 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353d5224-e63b-31ec-a494-78b73af0efff | -4.37168 | -46.8022 | 2025-10-27 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37a603b8-3674-3b57-8215-7aa299dafc90 | -4.78755 | -42.78677 | 2025-10-27 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204e7d8c-d4ad-394d-9307-f6a151bb028a | -5.15846 | -47.03541 | 2025-10-27 04:32:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3058aa40-526d-3767-b05a-67e486a1d1b8 | -3.55569 | -49.90385 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1ed80c9-15c8-30ef-a602-d9fe1e13ec07 | -6.34809 | -44.62458 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f192cb1c-8e58-3560-a3f9-b536aef089f6 | -4.47745 | -43.4141 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94dd7764-3dd8-3e48-aea2-0492f9b66768 | -9.83009 | -46.92771 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da6da287-d011-3642-87c2-a8f7c2eed330 | -1.69356 | -55.67104 | 2025-10-27 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 823ec410-733e-3293-9899-1859a8fff9bc | -7.36193 | -42.43473 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17682075-257b-3eae-9f0b-17044c4cdb39 | -4.44098 | -45.98294 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 280b05fe-4165-38bc-94cf-cca5bc8d2180 | -7.53796 | -46.26997 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d544f689-b2b2-3b68-9aa3-6fa205617eaa | -9.06032 | -45.10464 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1b21610f-da89-3a45-b6bf-652f100936e4 | -4.28668 | -49.66703 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9cde4c1-2329-3730-b65f-2c8133d8fcfa | -5.01101 | -49.99276 | 2025-10-27 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a865fa85-3321-3474-8b9d-892a575b57b3 | -8.67013 | -44.75986 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3d66f51-2ac3-3a78-a5cd-6120f482825c | -3.25087 | -50.04015 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57a6a7aa-79a3-3db3-b14a-fcaf3c9a1455 | -9.63604 | -46.86443 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7049a7a4-28f5-32b3-bded-e1b732b1a80f | -4.81212 | -38.6487 | 2025-10-27 04:32:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5af9f25a-cad3-30d6-b943-1f3573e12996 | -3.86211 | -49.8012 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c2caf68-72fe-3376-9053-1fd9e232c9bf | -3.12791 | -50.15233 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 454e17ed-0bf5-39bd-9560-ba7d2b0bd82c | -4.47231 | -46.0461 | 2025-10-27 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3211cff-b2f9-35f4-972b-7c6f2670fb24 | -7.83291 | -46.45316 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29332a8c-c4f4-3652-913d-74b3a8511520 | -7.83636 | -46.47585 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 45d46aa3-a7c9-31fd-b4fa-cf9280e67b30 | -7.59363 | -45.69175 | 2025-10-27 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb54f8f9-6ff6-3abe-bbff-4228d49218cf | -9.30146 | -45.22704 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4453e91e-e4af-3f93-a669-7de2e1082c71 | -6.49995 | -44.33118 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8ed6fe2-7e73-38c5-9296-45a1707173fa | -8.02931 | -46.74896 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5803c651-21f3-3e46-b511-30e41ed4b289 | -2.67866 | -54.65004 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f6a41e8-a788-3336-b4d7-772403681d05 | -5.8688 | -43.20584 | 2025-10-27 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 129e400d-bb08-358d-9d11-1354d28af6e8 | -4.8086 | -43.29797 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5973c537-fb07-3d76-b049-6ac4e4ac4d20 | -9.79375 | -45.6194 | 2025-10-27 04:32:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f5f4668-dc0f-3321-93c3-33d638bc908f | -6.11325 | -41.73705 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 73d24e50-e8ab-303f-9723-b9393bcb19a1 | -8.02876 | -46.75254 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01bcfec9-a9a5-3cb4-8769-462eddf71445 | -3.78908 | -49.83004 | 2025-10-27 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f7b3e08-ed1b-37b0-bd74-ed03739fde5d | -8.09994 | -47.06303 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31925bc6-46be-3d50-92d9-f2315afa7c0c | -3.27443 | -51.62517 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ddce089-66fa-3ff8-9945-2a9459472d6a | -5.62047 | -42.6679 | 2025-10-27 04:32:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa9aecf1-69c4-3767-80ec-2fb7f87bd4e9 | -9.98726 | -47.18903 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9acd41b1-65c5-321f-999e-714f59a17d4b | -6.89501 | -45.15356 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eae34cf8-2281-332b-b0f3-d55fe5848f4f | -7.0676 | -47.36044 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d13c475-fe7b-3229-9a2e-bbc6d147e861 | -8.07183 | -46.95697 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c65d4e35-ca3f-3366-a193-b11b01074ce4 | -5.64255 | -48.24548 | 2025-10-27 04:32:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80f9eca4-63f2-347e-bbff-df770bf9a33b | -5.60782 | -47.09873 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37fe31a4-90e8-385d-9cb3-57df307ace00 | -6.37836 | -44.26786 | 2025-10-27 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9419ed42-5b52-3316-87e2-5c700a6a73f9 | -7.50935 | -45.06668 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19c36415-f366-313e-a095-80cfb7b77d91 | -6.17172 | -41.57377 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53a069c3-e6cc-355e-a380-fe34f3c08f7b | -5.33028 | -49.51126 | 2025-10-27 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a65b25e6-8471-3d88-a2ac-fbb67dce25db | -7.84023 | -46.45049 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 808e5ac5-bf93-3eb6-87a8-0efaf6de462f | -3.24123 | -48.77454 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README37.md)
