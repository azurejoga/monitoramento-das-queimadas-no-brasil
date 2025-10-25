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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0da958a2-b60e-3d2e-9658-ebce6691db73 | -4.96588 | -47.59802 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| d374d72e-2e10-3c76-b18b-5c9090eb44cf | -4.55524 | -46.68342 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| abffb628-8867-30b0-8d0d-96fa8a51ce86 | -4.8712 | -48.40453 | 2025-10-25 00:35:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| aa114347-398d-3cfc-8648-9283dec85f6a | -5.65112 | -45.96193 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f19ccb8a-d237-30bb-aa4c-84438481e513 | -4.8361 | -50.93621 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b697c086-3444-3d5a-94d0-69216e6ba2c3 | -4.99935 | -47.76197 | 2025-10-25 00:35:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3ad00151-5e8d-321b-ba9c-39d02cff32bd | -5.59913 | -45.19623 | 2025-10-25 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ca692abc-3d08-3034-9a5c-2f85b48a17c1 | -6.73236 | -44.1553 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 7c358e59-26db-37d0-a3cb-1722118d571f | -5.54706 | -46.525 | 2025-10-25 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b3d39698-22f6-351a-8881-37d24fa58d79 | -5.59709 | -47.09112 | 2025-10-25 00:35:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad983477-740c-31db-86dd-5c814717b668 | -6.89508 | -46.36605 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c7f287f4-d400-33cd-8d1b-938e3f7142d7 | -4.97635 | -48.36321 | 2025-10-25 00:35:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f2407bb-e4cf-333c-9e60-db490e42ef57 | -9.87126 | -47.4656 | 2025-10-25 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb768c7e-5658-3076-a588-0dbc12554f47 | -7.55411 | -47.10934 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b49d2a4a-c934-3199-8c04-9d1165ad913f | -5.00081 | -47.77209 | 2025-10-25 00:35:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5a71d06-c6a3-3e75-991e-cee9cc4739ca | -4.84499 | -50.93497 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 483d3967-7040-3ff3-a53a-5c99ec069e32 | -4.82599 | -50.9285 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 929a0beb-03ae-3026-a6c5-a7054d15311d | -5.14673 | -43.73465 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b8bd52af-c929-3ea9-a7a9-aa30faaa75f0 | -7.05564 | -46.75934 | 2025-10-25 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2f2e69b5-b91f-33ed-81ba-b536fcf7ec0a | -5.54656 | -46.53086 | 2025-10-25 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d38fa659-ae44-3dc6-b06b-7a646a90b328 | -3.01968 | -45.40719 | 2025-10-25 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| eb7f8791-5550-3c01-99e3-0d26d101174a | -6.76391 | -44.20282 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 3d5175e0-d8c8-3508-ae28-462fa05ee891 | -4.55699 | -46.69528 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ce30c48f-1186-397d-8103-f6803a802a60 | -4.09686 | -51.05192 | 2025-10-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5823f30e-4f04-3c65-a0f1-d423df92fb17 | -4.00267 | -48.32638 | 2025-10-25 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 59bd3acf-fbda-3d7a-b528-3100abc550bd | -7.48471 | -47.03414 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e70beb0e-dbae-3c1c-a166-fd397a1bd69f | -5.10933 | -48.65688 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 841f33e1-ccd1-33c2-9e53-1e27792a2fe9 | -5.57279 | -46.35353 | 2025-10-25 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c498c7f7-ad7b-3cc3-951e-b58e0b421b76 | -4.9111 | -47.65482 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8ad48c45-3a92-3fc3-b4c9-da5884f3ef55 | -4.90345 | -48.96291 | 2025-10-25 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b99f2bfa-2ae1-3f41-a2a0-1f3af26b6d4f | -5.65761 | -45.96788 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 163658e1-9601-360a-95b4-3dffff8a55b2 | -9.33103 | -46.98343 | 2025-10-25 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 47ec186f-84ba-30f2-af81-434b4e3335dd | -6.97601 | -46.43145 | 2025-10-25 00:35:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 57a26339-b284-307c-bf1e-b02b4b5abb18 | -5.33378 | -44.72367 | 2025-10-25 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 29ff7040-16c2-3406-b539-a5c2e25df813 | -4.9126 | -47.6653 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fc55f826-61ce-350f-b2f2-77118cdfebbb | -3.02896 | -45.38968 | 2025-10-25 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| dc47559c-0b95-3622-bc76-20969fdd0aaa | -6.75736 | -44.19825 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 44971ebe-fd10-36f2-b091-ab06eba7a14a | -4.10028 | -48.9537 | 2025-10-25 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2d1e05ca-ad97-3a56-b5f2-e70a3783a672 | -8.72232 | -48.00484 | 2025-10-25 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0169a3d6-b8f2-3f01-af7b-3b1268171ba4 | -5.37781 | -40.69313 | 2025-10-25 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 9ffa21a8-adc5-3f28-a5a4-3d2fc7414c44 | -6.93051 | -45.17076 | 2025-10-25 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fe53ea33-6d88-3f41-b2d2-40c73d9f55f7 | -6.55257 | -43.22868 | 2025-10-25 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 1d5b5c4f-5538-370b-8c77-62c7e17627e8 | -5.65298 | -45.97499 | 2025-10-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d16c67b1-161b-37dc-a4d2-6e722231fd6c | -4.69519 | -44.05067 | 2025-10-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| a3e3244b-0c0b-3f78-9d50-40dadab16fcb | -4.55483 | -46.60962 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 01c31d69-a9cc-323a-a5cf-a778032f91b6 | -3.90582 | -47.78141 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a1fa04d-be27-3128-9038-be4154eac333 | -9.09246 | -47.82058 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd759c23-74bf-3030-a67f-c31bc56391a7 | -9.71301 | -45.42389 | 2025-10-25 00:35:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2a71574c-f498-3f15-b3cc-6535c9c60bd6 | -8.28234 | -46.88155 | 2025-10-25 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b80c5f64-da12-3d9b-a871-a06ec14800ae | -5.24675 | -44.13843 | 2025-10-25 00:35:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 69eb205b-3eb6-3d99-b283-0637d9b3885c | -5.81412 | -52.09938 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 820658a1-d68a-39ec-8613-086c352c0a5f | -5.4465 | -45.41091 | 2025-10-25 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 38d5b73b-03d5-39e6-a404-af2dda7698c5 | -4.22664 | -48.60744 | 2025-10-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b35bba28-b5dd-3b2d-b396-1ea329f4cc30 | -6.11045 | -48.10986 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a67b1e2-6e92-397b-9f0f-3198f2ebc004 | -4.88917 | -43.25194 | 2025-10-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 15e8bcfd-e5ae-3f37-93ed-44aa5310dd66 | -9.19193 | -47.74208 | 2025-10-25 00:35:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d89cee72-6c2c-3b7c-bda5-d5b424b3f9d5 | -10.00201 | -47.60485 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8828cb14-493b-3de2-8e13-09cb6ba183fb | -4.22047 | -48.36307 | 2025-10-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1ff307ea-7481-356a-8239-a3635818f89a | -7.16813 | -45.85304 | 2025-10-25 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e6d36433-a9f1-3e68-9c51-98956eebb7dd | -8.19433 | -46.50368 | 2025-10-25 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 54dfecaf-3089-3395-9e8e-98ce86dd0173 | -3.69385 | -49.94019 | 2025-10-25 00:35:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c5c93f34-8d7c-3c14-997d-c53591c1b17c | -7.55559 | -47.11975 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 6b337807-a731-32d1-8f2b-d188f1ad07ed | -6.92842 | -45.15695 | 2025-10-25 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 557bce37-2639-39b6-8d50-26de4ab90947 | -3.60684 | -45.97149 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5979d605-d5ac-3446-820f-7c371419bc7f | -7.48224 | -46.88245 | 2025-10-25 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e857a98a-6097-3451-ab8b-6452898163aa | -9.95847 | -48.26955 | 2025-10-25 00:35:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98595941-1dfc-3f76-9be3-4f290bc4f529 | -8.8731 | -48.28779 | 2025-10-25 00:35:00 | TERRA_M-M | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7c1bfc3-dc66-33fe-9ab1-9ae56a884010 | -9.49206 | -47.45829 | 2025-10-25 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fb33911c-a708-37a9-b1c6-1424c7ce6535 | -4.72701 | -49.08413 | 2025-10-25 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c593cbb8-7661-3474-9835-61202c0008ad | -9.71657 | -45.42922 | 2025-10-25 00:35:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bce87d4e-bd02-310e-b2b7-3cfd8d362b72 | -4.70713 | -46.44227 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| e596cc5d-b4fb-3d0f-b419-374b9f27e494 | -10.00066 | -47.59539 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| dd1da11e-d872-3ae8-82da-07ed32f4c97e | -5.89207 | -43.20458 | 2025-10-25 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 8ac247cb-c7ad-331a-a6af-9095eb3b93bd | -9.61494 | -46.90207 | 2025-10-25 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23516a7f-7040-352c-a1eb-dba3fe52dab6 | -4.84622 | -50.9439 | 2025-10-25 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7cbf55ae-56c1-3334-a27d-49c1519ec82a | -4.96248 | -47.60484 | 2025-10-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1758077a-e43e-3353-866c-c7e9f14fcc54 | -7.92923 | -48.26181 | 2025-10-25 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31e07544-62f1-3510-96ce-d6f041e46a8f | -6.75999 | -44.21508 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9728d64c-91cc-37d3-bf9d-8dcc21c1a11b | -4.7283 | -49.09323 | 2025-10-25 00:35:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c4e36dec-2826-3991-a17c-5de4b7cabf05 | -6.76642 | -44.21975 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0fc44389-f863-33af-9a88-af4c80b82744 | -9.32016 | -46.97471 | 2025-10-25 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b9b9f567-9252-3ce0-b149-49c8072131a2 | -4.55614 | -46.6769 | 2025-10-25 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| dd3845d3-1aac-3401-81fd-ca02525bec8e | -7.7825 | -45.39213 | 2025-10-25 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0ab8380f-a8ab-3aa8-941c-957d57be0577 | -8.88788 | -46.83999 | 2025-10-25 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d4c566e8-84e0-3cce-851a-578f9dccc872 | -4.6035 | -49.58168 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 83b5e61e-e31c-3a27-8f64-d6a14ab553f9 | -3.91149 | -47.68378 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6b543bd1-bf50-3244-80b0-1e467a0ca338 | -8.72418 | -49.60281 | 2025-10-25 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 35b91242-d82e-343c-86e8-97fe90abe358 | -6.80426 | -42.40009 | 2025-10-25 00:35:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 25f28524-105d-3b1a-8942-3140c5ccddad | -5.25911 | -44.13675 | 2025-10-25 00:35:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 47cef4be-59c5-34c4-8970-4bc302b1f0f5 | -8.32392 | -49.50333 | 2025-10-25 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5222c76-e26a-35c3-b46b-d57f3626a51f | -4.70309 | -46.43705 | 2025-10-25 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 01839423-0822-3277-a4c3-e3468a93bd21 | -6.45186 | -44.28756 | 2025-10-25 00:35:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0093a552-3c5a-3f91-982b-d198e7529d55 | -10.62595 | -52.18605 | 2025-10-25 00:35:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ecc47fa3-7999-30b3-82e3-4e16b791abf1 | -4.27093 | -50.50407 | 2025-10-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 65a357d7-5963-3531-8387-e0bf86683120 | -7.16146 | -46.09348 | 2025-10-25 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 083f25ff-7de6-342c-afac-2c6f93b3a2f1 | -8.34193 | -46.18057 | 2025-10-25 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4764e6c3-52e3-3406-831d-8701da090284 | -6.55447 | -46.63036 | 2025-10-25 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dde16e4c-2a15-3b9f-9590-eccd923e1cf4 | -5.36911 | -40.68762 | 2025-10-25 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 1b6b5f75-3404-3aed-a37d-fb275ec64826 | -3.92113 | -47.68238 | 2025-10-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a12ea110-1c1e-37f0-b8ec-bed74f440761 | -4.00128 | -48.31656 | 2025-10-25 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |


[Clique aqui para ver as próximas entradas](README6.md)
