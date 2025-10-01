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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b00308-f66b-3e7e-90c2-8f0122ce14e9 | -9.9394 | -43.5777 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c443db9e-65cf-3dc4-83c1-6da911ea6139 | -13.7691 | -47.9435 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 8c6116a7-1f27-3bdb-b8ea-474368ab79ec | -15.9381 | -43.3223 | 2025-10-01 13:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 524.8 |
| ff607577-9cdb-3acb-8e7d-0e9ca6b79483 | -12.481 | -50.2476 | 2025-10-01 13:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 232c6488-d73f-3206-beea-6189ac6b7a02 | -9.4115 | -47.3308 | 2025-10-01 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ebbeba79-346a-3400-9896-7749a3b50db7 | -7.4412 | -47.0109 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 66b7b980-e1fe-342e-a9a2-72fe7aa263f7 | -7.6272 | -45.4507 | 2025-10-01 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 26813a8e-f67e-3210-8266-8765aeac82f8 | -12.2536 | -47.806 | 2025-10-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 628.4 |
| f8881e89-a12f-3ef9-a4ab-3ac31ef0b470 | -14.3714 | -45.9172 | 2025-10-01 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 582c558c-8cb2-37a1-a27d-9f6c7a112682 | -7.646 | -45.4489 | 2025-10-01 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 6a2ddffe-2c85-360e-8267-47bacd74c14f | -14.1926 | -46.1091 | 2025-10-01 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| b693254a-684e-3bf7-b0b6-33a0d71d725f | -11.4784 | -45.0637 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f00f726c-4f7a-39b1-90f9-e7942258df81 | -6.214 | -44.2272 | 2025-10-01 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 01353dca-7a9d-3a90-a71a-e76d1b7d517e | -11.8622 | -45.0075 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 4a0bbda7-ab69-35fa-9361-5533a03e694a | -11.9411 | -47.0675 | 2025-10-01 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ad38bbce-1284-385d-b32c-2c65a2e37fb1 | -5.9557 | -45.8588 | 2025-10-01 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 1c6ae270-9955-3e59-8032-16ff1fde590f | -8.6908 | -47.7126 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 50d5b7e0-d2dc-3e50-9be2-f40a4f2289d1 | -14.8021 | -45.7946 | 2025-10-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| b30418ca-0db8-3566-91ac-f04c75db4c21 | -8.8797 | -47.6502 | 2025-10-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| fb77d688-b1cd-3c09-83cf-538d1af79fe8 | -5.9368 | -45.8825 | 2025-10-01 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 18522509-785b-3146-9413-5cbd1910295f | -16.0225 | -50.8771 | 2025-10-01 13:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f2f9beea-8465-3ca3-990f-6d4a729d0d4c | -8.8543 | -46.6781 | 2025-10-01 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 191956b4-eea0-3599-98e0-678df2642bcd | -8.2105 | -47.0084 | 2025-10-01 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 594b6104-829f-3b8b-a0ac-9f0322b26cd7 | -13.3607 | -48.1382 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| d0eed91c-d0ce-3721-8d01-ee8cb981b0db | -8.5867 | -45.4914 | 2025-10-01 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 995ebd0f-f47f-3217-b1e5-7eab4fae006d | -15.2742 | -49.2852 | 2025-10-01 13:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 196.6 |
| d63da12c-b777-306a-8c9f-d0b0729936b1 | -8.5407 | -44.6745 | 2025-10-01 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| be9087ae-bb4a-33f9-ac2a-7bf0b9f8e561 | -10.9182 | -44.3092 | 2025-10-01 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e450b8d7-f639-3c7c-b0e0-3500799e3093 | -13.3611 | -48.1159 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| be7eab95-d1c0-3123-84c8-0cdf776d0634 | -11.4405 | -45.0461 | 2025-10-01 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7629bafa-fca3-345d-b3be-b4f3e31a3120 | -6.5546 | -43.9221 | 2025-10-01 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f1fb0cae-cbf0-37ca-b6df-740385a22c50 | -9.9391 | -43.6012 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f8152f95-d932-3323-8021-094df70e56f4 | -9.1246 | -47.6476 | 2025-10-01 13:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fc563a62-dfc9-3a49-a242-1c3d5b0147ce | -14.3514 | -45.9437 | 2025-10-01 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 4f77ec8f-41a5-3251-bb01-00779db6cfd6 | -13.3603 | -48.1605 | 2025-10-01 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5f3552b6-c4f1-32fc-8a3a-0054d456f2a9 | -12.254 | -47.7837 | 2025-10-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b32a2ed9-4330-39d1-8e22-782d13e462b3 | -14.1921 | -46.1321 | 2025-10-01 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 21bc3155-58b8-3a50-a9e7-cac457ca532c | -7.1815 | -41.6931 | 2025-10-01 13:20:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| fdc1a2f3-1efc-3483-8553-3dadcb1db976 | -11.9254 | -48.0051 | 2025-10-01 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d2ef503a-448a-39d6-b22b-8995f824d79b | -10.0906 | -50.2154 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| d6835ba8-a5e6-34b0-ad39-34d0ed5c15e6 | -6.2138 | -44.2502 | 2025-10-01 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b368c2ad-2d54-3094-93f2-2e80d5788d27 | -9.1248 | -47.6256 | 2025-10-01 13:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| b9560ee9-8550-3929-a828-c5fe3853eeb8 | -14.9084 | -47.1965 | 2025-10-01 13:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 67315332-865f-32f9-893b-3eeda0f3848c | -11.1757 | -47.2134 | 2025-10-01 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0a9d81f8-4f01-31d2-9e15-cf7ec2346672 | -11.8482 | -48.0595 | 2025-10-01 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| d773fae9-5458-37cb-a3ec-0e4b809ee0ac | -11.7797 | -47.5806 | 2025-10-01 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| bd5201f3-567d-318b-83ef-5755f4b2c8a9 | -6.0625 | -42.4422 | 2025-10-01 13:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 48653a5f-ffc4-348e-b7d8-4d5c4734cd22 | -8.5018 | -47.7965 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 930e0b20-f47a-31cc-b3b8-8acee79b20df | -8.6722 | -47.6924 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 46b67724-28e6-3d7e-91ad-2a98861bff86 | -8.4833 | -47.7763 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e212ad0c-55b0-3865-a737-491c4c1fd7cd | -8.5267 | -47.2879 | 2025-10-01 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 9fc21352-6808-33eb-a4d5-dbeae9e45011 | -7.8405 | -48.2053 | 2025-10-01 13:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 2a290601-301a-3c08-bf1e-7be7ee493417 | -14.3524 | -45.8974 | 2025-10-01 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 64b352da-f243-382e-ae7e-33a50c3c4e2d | -14.9733 | -46.8896 | 2025-10-01 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 8b821a42-e472-3ad8-8d51-238fe702a6af | -9.938 | -43.6718 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 325.6 |
| 346de1a9-9411-3952-b649-6443d33ecd49 | -9.9193 | -43.6508 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| a185082b-b696-3607-a18d-c000b695d925 | -10.1095 | -50.2135 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| a7687621-1185-3073-ab41-f85b65c2cd2b | -8.5584 | -44.7644 | 2025-10-01 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b4e461e7-6aaf-36fe-8ed5-42a30dfefe54 | -13.2973 | -50.6605 | 2025-10-01 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e1365132-1e34-3d99-b3ee-9e80db50d25f | -9.6441 | -45.5552 | 2025-10-01 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a04dd263-f55f-3f8f-a0c4-27c0da728a33 | -8.8354 | -46.6801 | 2025-10-01 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| e375a733-79d5-36fc-ae9e-219e59beb7f1 | -13.0307 | -45.2189 | 2025-10-01 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d93d3110-0069-3f94-8f67-3b582e11a039 | -14.9738 | -46.8668 | 2025-10-01 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 5bf98da7-adf0-39d6-93ed-c91c359169a2 | -14.3519 | -45.9206 | 2025-10-01 13:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 330bf1e2-3e0e-3fc2-a24b-0369039c105c | -11.8478 | -48.0816 | 2025-10-01 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 89c3ee15-b723-341c-b8b9-745210150390 | -7.4249 | -41.8601 | 2025-10-01 13:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| ccb57c76-1928-3ebc-b038-72e46359f40d | -8.9182 | -47.5803 | 2025-10-01 13:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7d278001-1704-34d4-a7dd-0c9ca3a11665 | -10.0337 | -50.2424 | 2025-10-01 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 98cafbbe-be9a-3c9f-851e-9ceefe47ea05 | -8.8609 | -47.6521 | 2025-10-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9eb13d25-c996-3d2f-9970-ee0a01d05de4 | -9.9383 | -43.6483 | 2025-10-01 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 2ff7d836-7837-3b62-bfb8-3bc486db504f | -9.4644 | -47.6124 | 2025-10-01 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6ffdbdb2-42c6-3242-ac29-be765054f836 | -9.9383 | -43.6483 | 2025-10-01 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| b5e91be8-9824-3e25-af57-3c4d258308f1 | -13.1747 | -47.7869 | 2025-10-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 72cd29dd-93d8-3262-a7b0-76d178871b9f | -7.8738 | -45.2684 | 2025-10-01 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 3c044afe-702d-339e-b0dc-1037b5917d12 | -7.4412 | -47.0109 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4237b172-6db3-34af-8060-e9c42c12707b | -8.483 | -47.7983 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 195.5 |
| bc851659-7a4a-3e2b-a30b-53a774ed8b09 | -11.8622 | -45.0075 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 2050a2a9-e283-3362-98e5-8e0aa6a5c4d2 | -6.5546 | -43.9221 | 2025-10-01 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4a9821cb-4e7f-3b58-bebb-28dfcb2c2b2c | -7.646 | -45.4489 | 2025-10-01 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| dc7edd22-f4e6-3488-aa49-dd9ab54c411d | -7.8884 | -47.259 | 2025-10-01 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3fc03026-a202-342c-9810-6eefbf1c3d0b | -13.768 | -51.2214 | 2025-10-01 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2fb68bc4-009d-37d7-b5de-a51aa6162f1e | -12.8967 | -45.1711 | 2025-10-01 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| b458e164-8d8e-3552-8044-920a9f921675 | -10.0337 | -50.2424 | 2025-10-01 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 58abb752-f6d2-3652-8b42-0dcf2fc08f23 | -16.9032 | -47.4255 | 2025-10-01 13:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d7181637-c81d-3452-9bdf-5f8626685a81 | -8.672 | -47.7144 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 43991434-212b-3b54-99b1-fb066ca1834a | -11.7793 | -47.6029 | 2025-10-01 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 6314a1c7-df4a-3703-9fd1-65255c835ed7 | -9.6441 | -45.5552 | 2025-10-01 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| cf47c8ce-cec3-3046-af63-f64f6a2213e6 | -6.0625 | -42.4422 | 2025-10-01 13:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 769ff1f5-57f8-3fcd-acba-4efa068d2a96 | -7.5749 | -46.7778 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 20b01fa1-7faf-3d98-8eb8-2e9358820744 | -13.7869 | -51.2404 | 2025-10-01 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 98ed0817-43e5-3049-b9fe-bb695d0c15fc | -13.3804 | -48.1131 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 81314f41-573b-3c43-b473-be71e6651193 | -13.816 | -47.5107 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 4e133c72-4c8d-3efe-8e8f-d55ab925478d | -13.2973 | -50.6605 | 2025-10-01 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| fed2ee92-867b-3a44-bb28-76a6aadf99a6 | -6.358 | -44.8339 | 2025-10-01 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 22bbb620-a618-3c92-be3a-1461cd5c8543 | -9.4458 | -47.5923 | 2025-10-01 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8e61a413-97b2-3ba9-bc87-91780f84c216 | -12.2156 | -47.7889 | 2025-10-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c66d6eaf-ba9c-3c53-93ce-031334e62e03 | -8.9115 | -46.6276 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d557ac49-d10f-34b2-bf93-f87ccffcb2c4 | -8.5587 | -44.7414 | 2025-10-01 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 529b2fc7-0576-3974-a3a4-0a8f2ccf99a7 | -11.4409 | -45.0229 | 2025-10-01 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 506466b0-1c45-30dc-bbe1-cf77a831875b | -8.6908 | -47.7126 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |


[Clique aqui para ver as próximas entradas](README154.md)
