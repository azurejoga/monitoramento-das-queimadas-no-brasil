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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c786c2e-5f9f-343d-adfb-982d3c89cec2 | -12.40004 | -46.48592 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 617dace4-0614-3a31-afb5-1cb88708cfb0 | -7.75455 | -50.27605 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebfc35ae-98f9-30aa-9b73-b651ecdb9fd0 | -7.74518 | -50.271 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f840497-f863-33fd-a877-19a5a9d2088a | -12.8369 | -48.1602 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9ea6ef5-033f-360d-a9ee-19c7505ef29e | -8.88225 | -60.74701 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcd99535-8869-30de-b0c8-55aa27b5400d | -11.56732 | -46.3385 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aac056e6-0889-3d14-b525-e79089895ad3 | -7.4119 | -43.38487 | 2025-08-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9e2c163-c6b3-3248-8b93-1e7b0473b7ab | -12.70861 | -48.19589 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e04d34e1-c471-3e2c-8c7c-6033bc4e4f44 | -6.81403 | -44.99765 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ccf22a6-c316-32ec-81df-7a68c998c219 | -10.60916 | -52.32368 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed400815-9c75-36d3-b3c5-2d45652beee6 | -10.45376 | -57.97161 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc8dd9c3-88ba-3d12-8876-eef1269fecce | -10.93461 | -46.87075 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7bfbb68-c65a-305c-8ec7-b73681bca06e | -10.28689 | -64.49509 | 2025-08-29 04:40:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d05394c1-7ddb-3a01-97f3-5782fa3b2bd9 | -6.19273 | -43.32438 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d111395-bc4f-3240-995e-cd20f7c4c46b | -11.22648 | -55.05987 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a80f1d3-7b38-3ea8-b44f-18b5f95a772b | -9.67145 | -48.32111 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8920637d-8180-3206-9580-49074a48063b | -6.54203 | -42.67046 | 2025-08-29 04:40:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7d86757-4bbb-313f-b206-c03a40d3f663 | -8.45294 | -43.71584 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51221803-acc0-34f0-bfc0-99f479f7e0b4 | -9.50323 | -45.38169 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4829185-dc9d-306c-9d96-3841360a0b2e | -11.83868 | -46.79451 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37b44174-b579-34ec-b9a1-79ccbd14080f | -8.69193 | -50.39422 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e53ffa9-ddb1-37b0-af8c-4da93a7cecca | -6.47993 | -50.20501 | 2025-08-29 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 818f8707-05e0-3dcf-8980-e9cd610404c2 | -10.4917 | -51.61868 | 2025-08-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a73d880-545e-3972-8f21-e217c9ae86ce | -8.88351 | -60.74171 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf709e5e-1dcc-364c-91f0-fe7e6d0584af | -13.19066 | -45.27957 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1cfd2406-8f43-3d06-a80e-175e367538c7 | -11.23331 | -55.06603 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1095e9a3-27ba-325f-a88e-d5bbbac9b617 | -9.16295 | -59.56182 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d1913ff-37ab-379b-b751-e3dc5dd1d604 | -7.16099 | -44.14717 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25c53a0e-b4b0-3ce4-aceb-2f881329ee32 | -11.23248 | -55.07084 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 839063cb-c829-3a9b-9f52-2f2ab5a97f30 | -9.77104 | -64.25397 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6e243e4e-2319-3a2d-abd5-59f47a157f6b | -6.70463 | -43.14268 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccedc8e9-0e7e-3390-beff-956f95b1c082 | -10.37952 | -59.39668 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e0a0b27-f838-3cfd-a0bb-aadb7238a756 | -5.56765 | -52.0878 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f401069-5ab3-3641-9163-aa3dac9c512f | -12.81438 | -48.19 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7135b9d5-abb4-3a0b-9221-42ef3032355e | -6.22529 | -42.75619 | 2025-08-29 04:40:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2dcbc4ea-9aca-34e9-a71f-04b595eb0ab0 | -7.02911 | -44.67548 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38153523-640c-3cac-a6cf-0e45ca0e8971 | -11.22864 | -55.07019 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6065b46e-8aa4-3889-81fb-625a4d80249a | -11.06086 | -44.76479 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90116310-89b6-3f10-8079-46b8822767d6 | -10.98138 | -46.90339 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 33cf137b-b213-32aa-96b7-8ae2622762f8 | -6.37955 | -47.42098 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c41027f-fa5b-3c53-89b8-1efd7310c3bc | -7.6263 | -43.97613 | 2025-08-29 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66960761-cdbc-3999-9fca-dfddc5d93d6c | -7.05006 | -44.38546 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 229839fd-1897-3424-9185-4ff8064f9fca | -10.38058 | -57.82797 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6b8b5533-d06c-3f8a-98ea-78f3c18725fd | -6.43617 | -44.57145 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34cbea9c-f09a-3ffe-9dee-6c73d60f9ecc | -10.7027 | -47.07994 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c94a464f-95af-397b-ab66-98a7c706e93b | -6.48862 | -43.52922 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f596637-88a4-318a-aca7-39e1d7488325 | -8.74783 | -47.38961 | 2025-08-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb3f0890-5514-323a-a2dc-a701e4d52e95 | -6.14155 | -44.05468 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28351417-7533-3399-9370-7a0307ecfeaa | -12.08809 | -44.72106 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c534d16a-dfdb-37d9-a74a-45808b8b2097 | -6.26338 | -43.81149 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce15b90e-107a-3a65-bf18-7f388c9b3ef7 | -10.02486 | -51.11106 | 2025-08-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c326ab9c-a059-37a6-8950-f40d540bb1b9 | -12.83628 | -48.16444 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cadeac93-06be-3924-99ca-4ab78225666e | -12.83152 | -48.1721 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d6d85e9-27f7-3d36-a4da-f8f00a3e3845 | -10.98075 | -46.90788 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e1c2e2cd-3cf5-3e8f-b789-7c1385157037 | -11.5666 | -51.43052 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e9712cd-430f-32c5-a887-39375dcb0512 | -11.3241 | -55.21564 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6c8659-e860-3198-b420-c6fea31c2e59 | -11.31939 | -55.21984 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d581e5-d9a4-3dfe-b759-7f21ae222e9f | -11.61841 | -47.31177 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e029e83c-5520-3a78-832b-9a78e29987ef | -6.35053 | -44.47466 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a41151e1-6a92-3277-9979-00f87179976e | -6.51787 | -44.8518 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dabe405-4faa-3f2c-9b5f-97a81b877805 | -7.72371 | -50.27821 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0c4d45eb-2361-3cbe-862b-4398e30c7fee | -11.58178 | -46.37551 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64d54f12-2ac7-331b-a767-19ec78766269 | -11.26575 | -45.49557 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef355839-4083-30e6-a7bd-0a7686b53101 | -9.77804 | -64.25542 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 86ebbad5-d3af-34cb-b1a9-258f3e1c7992 | -11.22948 | -55.06535 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 301cb7f6-dd0e-351c-86b9-84f2c66c4e02 | -7.61937 | -42.7005 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9b805c9-093d-308c-812d-e47f56f28a08 | -7.7276 | -50.2966 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27750dc0-9054-3e98-83f9-2019eb8a58f6 | -6.02033 | -44.48329 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1eb6a48-4fd7-32bb-a5eb-d9ae5ad579e7 | -11.35209 | -43.55946 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f171cc4-6bee-3812-8cfc-bdc414aa13b9 | -8.18198 | -61.38506 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4d29b6fa-ee3f-39cf-8bf6-b30e362d04f1 | -11.35609 | -43.56506 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 834a4680-be34-3f39-ac85-91750fb1df67 | -12.7889 | -48.1653 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad2a4bf2-9aab-325d-881a-821e5ec9103a | -9.21932 | -60.86752 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 31d615a6-e5ef-342b-ac20-3cd09253a98e | -11.32302 | -43.5654 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f81820d-751a-3ff9-86ad-809c15c24731 | -9.46976 | -60.5641 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5df69dc-724d-3754-a0ec-024ff760be6a | -10.64588 | -48.64645 | 2025-08-29 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2be4027c-93db-3010-842d-4cdb4225cf6d | -6.14648 | -44.07903 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1aa26db-da81-3ce6-bd3c-c44049570508 | -6.49447 | -43.53559 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02b07d1f-28c3-39a1-bc6e-e46af0e4bca6 | -6.71111 | -49.46907 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c082ea01-e51c-329d-b743-0595ca699bfa | -7.02286 | -42.0252 | 2025-08-29 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f40ac35-5580-3f76-a567-4eab02e2766e | -11.30311 | -43.54598 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a6733e1-181f-32dc-9b69-4644fab83b04 | -10.98078 | -46.91884 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2a59483b-d501-3321-b5a9-76a1da77c1df | -6.31214 | -43.53155 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03670813-3c02-33f4-a156-c9020101664c | -12.69201 | -48.1854 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09c3518f-066c-3826-87d8-9de292768ede | -10.11975 | -47.43287 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fc7c66c-e883-3bed-8880-817ca4962a05 | -7.0454 | -44.38866 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e110c5d1-2903-36fd-ace4-4b193bfd8e91 | -9.19922 | -59.5443 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e91b113a-0a8d-3344-91ae-27b49fe209cb | -6.4794 | -44.07933 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1eaf19a-59f9-31b6-8eb4-4d3bc945568e | -11.32362 | -43.56913 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bb86cc3-8048-3113-9e4d-08ea0946f616 | -11.24366 | -44.97104 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d60666a7-8cad-317c-b918-dc4ed2e65279 | -11.56019 | -47.61409 | 2025-08-29 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17c09d6e-5f6d-3b38-a636-d118a7ae1825 | -9.30038 | -56.81448 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86f7f741-d1f5-3ed1-aa48-7fde53438ba3 | -6.51897 | -44.85067 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 876909b8-08b6-3492-9326-050c815a6af8 | -6.44314 | -44.57993 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89970725-10c6-3c16-9d59-9cde02e8c0e2 | -7.05168 | -44.3741 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e762041-7dfa-3fb7-ac87-876e426cc91f | -10.37134 | -57.82592 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| edfe6e0f-f353-3ee8-8010-05de433d7cc6 | -6.14147 | -44.42902 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a440083b-6fa1-365b-b400-00b54fda4413 | -12.89745 | -48.13862 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fdeb82b-104b-3327-9b21-456117811e0d | -7.79459 | -51.14263 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c004772e-1216-3264-b7e5-10c052bb1ae8 | -8.1007 | -45.0013 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
