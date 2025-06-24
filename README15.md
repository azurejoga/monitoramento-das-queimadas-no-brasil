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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d3bb7e-3e6d-389a-a341-03c753748462 | -17.75458 | -42.89352 | 2025-06-24 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fa88e06-aed0-3a3b-a108-763ba2ab10e7 | -19.41099 | -45.14083 | 2025-06-24 04:27:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f2d453b-53c1-334d-906e-9bcfd24bc1c3 | -19.33887 | -42.16022 | 2025-06-24 04:27:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0bba28b-5888-31be-99ef-76b702cc4a34 | -17.09594 | -43.806 | 2025-06-24 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd65c575-2249-3a04-8d51-284ad58aedaf | -16.43484 | -44.52439 | 2025-06-24 04:27:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 229aa8b9-dcd7-3614-b7d3-fc95429963a7 | -16.99294 | -42.82971 | 2025-06-24 04:27:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5eaef4e-6e64-3e36-92e3-a2bc54b0ac26 | -14.50181 | -43.12408 | 2025-06-24 04:27:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb227d89-5506-34f6-aae9-76146a86e0a1 | -16.68211 | -43.88457 | 2025-06-24 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47805d7d-2fd5-387a-8c2e-c11e9a5ad413 | -14.43488 | -48.91101 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fb7fcc0-397c-3395-b9e0-74931156beec | -20.31082 | -45.58206 | 2025-06-24 04:27:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a95c17d8-97b0-38d9-97a6-21b5ff349bd9 | -15.0786 | -48.94498 | 2025-06-24 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b418566-217d-37b6-94e0-0f17565c3f0c | -14.7312 | -48.4183 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b29e5e5-7932-3a1a-87d8-3b282e366218 | -17.20281 | -46.07793 | 2025-06-24 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c49bc2ab-ac4d-3456-ba1d-01e5329ed3cd | -14.38331 | -46.14044 | 2025-06-24 04:27:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddca079d-9aae-3621-bb30-dc9e213587e3 | -14.38388 | -46.13664 | 2025-06-24 04:27:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bd1046-8883-36e2-9845-e6e260303939 | -14.43877 | -43.7559 | 2025-06-24 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ae7751b-69bd-3cd4-aa47-0bd2619f4495 | -17.49881 | -45.17421 | 2025-06-24 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 45826776-448c-3e69-a8c0-f49beb85f30c | -17.33684 | -42.66365 | 2025-06-24 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16872fd5-40d8-3181-bef4-9c313fe7c704 | -14.43821 | -48.91158 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce5eb9f7-428c-32b3-91bb-069f02fe791c | -16.68217 | -43.88123 | 2025-06-24 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b61eb1fe-36ad-307a-8069-1bf192676be5 | -18.92838 | -41.93398 | 2025-06-24 04:27:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbe5aff8-adc8-3e0b-9791-44f37d378288 | -20.49939 | -45.58603 | 2025-06-24 04:27:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 542204ae-db78-33e1-826a-a6a42c4a9f7a | -14.43705 | -48.91876 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f6509b3-8a5d-390a-9c7b-812d4dbc9012 | -14.66674 | -41.91147 | 2025-06-24 04:27:00 | NOAA-20 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9b1cb3b-d518-3079-b520-7908b130e9e1 | -14.66156 | -46.94207 | 2025-06-24 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c379450-2255-374c-8885-5ef26d115790 | -14.38617 | -47.87017 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6e14e7b-9169-37a6-a503-398f948b6429 | -14.1573 | -50.42957 | 2025-06-24 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 100d5393-6f68-367f-abea-3a7a80e666cb | -14.19761 | -44.27106 | 2025-06-24 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 023415d0-b996-325d-ad95-89c6caf5da0e | -18.61107 | -44.26385 | 2025-06-24 04:27:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 221ed86a-4dbf-3698-8647-bcb1f6ce9eb0 | -14.44095 | -48.91574 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41daef97-8641-370c-b26f-8f16dfea4afc | -16.43172 | -44.51908 | 2025-06-24 04:27:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c134080-dc96-3a63-9421-248782a4b49a | -16.46436 | -45.00605 | 2025-06-24 04:27:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 237e51e7-1897-31c5-8e9c-230cf027d4b2 | -16.06971 | -44.45956 | 2025-06-24 04:27:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d002f3c9-419f-3b3e-a8d2-09f5b0db9558 | -14.16077 | -50.43017 | 2025-06-24 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09149722-5144-3874-b247-0a1971ef4f30 | -14.16272 | -50.42994 | 2025-06-24 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a858b4a-bd9d-3953-90c5-57a7cd178387 | -14.66491 | -46.94261 | 2025-06-24 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b2eaefc-46cf-3bc1-ae72-1eea206fd002 | -14.39553 | -47.87538 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60097d6f-aacb-33f7-bdea-d1b6da5f200d | -19.41162 | -45.136 | 2025-06-24 04:27:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 562f3612-ac6e-3745-9a18-a6e5efa0c615 | -14.44427 | -48.91631 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc41a1b-af50-37a7-945b-bdb0bfb4b2aa | -14.43431 | -48.9146 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0996baab-820d-3c75-bafc-bce16794e646 | -16.68146 | -43.8867 | 2025-06-24 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99f7a17-8c71-3bfe-9dfe-a499e1d889ba | -16.58323 | -43.64289 | 2025-06-24 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7f80ff6-d691-395c-a69f-60e08bb8e9f8 | -13.73729 | -47.74217 | 2025-06-24 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9589e51-9c40-3810-b99f-f3ffc1b57648 | -20.81075 | -55.73581 | 2025-06-24 04:29:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49dbd977-636c-3684-bb0c-c8743dead8b0 | -21.43594 | -57.26443 | 2025-06-24 04:29:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 051eb2d8-9dee-3573-9b05-6dca36f5d4a9 | -22.78682 | -43.75753 | 2025-06-24 04:29:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71652b98-8bbb-3f56-8715-b3e422042b10 | -20.47732 | -53.67545 | 2025-06-24 04:29:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5d94108-bdba-3273-a2e0-0ab130a73a9a | -22.67718 | -42.85513 | 2025-06-24 04:29:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ac604a0d-73d2-3b54-8a96-173e673a44a7 | -25.19173 | -49.32708 | 2025-06-24 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0bba7828-fb9d-356a-ac9d-49f016ecf88f | -8.5722 | -51.5761 | 2025-06-24 04:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ba02d0c5-db60-3d46-ad0d-0717161ec5df | -8.0703 | -43.0981 | 2025-06-24 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 6211ee14-1376-3f23-8c14-763c4775c365 | -8.5724 | -51.5552 | 2025-06-24 04:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7827a3b9-2129-32e2-8db9-c6aba5304346 | -8.5537 | -51.5567 | 2025-06-24 04:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 53950814-26c5-32df-95b1-78afff3592c5 | -27.78895 | -51.91463 | 2025-06-24 04:32:00 | NOAA-20 | SÃO JOÃO DA URTIGA | RIO GRANDE DO SUL | Brasil | 4318424 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aabfae5b-2a3b-3b91-b374-92249c721d55 | -30.15049 | -52.024 | 2025-06-24 04:32:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 3b327d69-d71e-37ad-ac56-dbf6ddc330a7 | -8.5537 | -51.5567 | 2025-06-24 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 10a162e6-dd74-3d53-9649-47f3334a6df0 | -4.5429 | -48.0151 | 2025-06-24 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a15462fc-5892-3e07-99b6-801b51c75693 | -8.5539 | -51.5358 | 2025-06-24 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| ec1cf4a8-c207-3ccc-8b5b-f62caf1aa627 | -8.5724 | -51.5552 | 2025-06-24 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8569acc7-192b-3a4b-9577-0e84169f8c14 | -8.5535 | -51.5776 | 2025-06-24 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 76bc449e-c389-314a-a35f-0b48ae58ce42 | -8.0703 | -43.0981 | 2025-06-24 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 0bd5eb29-bac7-3bf0-aff3-63e62cbc4a23 | -8.5722 | -51.5761 | 2025-06-24 04:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| b31aa3ee-5d78-3850-aa1a-c933c00c1510 | -8.5722 | -51.5761 | 2025-06-24 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 59215309-3163-3739-8ff1-b14d93c23075 | -8.5535 | -51.5776 | 2025-06-24 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 5fc1a7e5-3d86-3845-ad8d-cd83fd5cb531 | -8.5724 | -51.5552 | 2025-06-24 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1872a5fe-62cc-378d-a2c2-ec120c979ea6 | -8.5539 | -51.5358 | 2025-06-24 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d026452b-32bc-3430-bfd4-4326a0228484 | -8.0703 | -43.0981 | 2025-06-24 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 2c2a1cd9-5cf6-341f-af19-44cb4e97224a | -8.5537 | -51.5567 | 2025-06-24 04:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| db0a3698-8d61-3fab-b653-92e9e9487ab2 | -8.5722 | -51.5761 | 2025-06-24 05:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ac2efed0-763f-3a03-a1a5-73a3b2b32e43 | -8.5537 | -51.5567 | 2025-06-24 05:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 193.0 |
| 8e032c8d-aec6-3980-82cc-ca9e091306e4 | -8.5539 | -51.5358 | 2025-06-24 05:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 595a2e52-3355-36aa-a9a5-7bba7e795437 | -8.5724 | -51.5552 | 2025-06-24 05:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 2909fd94-270e-3a78-969f-6992f5f239c5 | -5.78501 | -43.60427 | 2025-06-24 05:08:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d27527e6-1d31-36a4-9000-cbdd9a93f752 | -5.9107 | -43.47257 | 2025-06-24 05:08:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| d3eebed9-9b42-370c-b669-ffac418c6920 | -8.5724 | -51.5552 | 2025-06-24 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 8ce8d536-955c-31ca-9c5e-ea6ac43a8b38 | -8.5722 | -51.5761 | 2025-06-24 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2402d208-139c-350e-862f-58bd2e9e8765 | -8.5539 | -51.5358 | 2025-06-24 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d6751f18-a21e-38a4-9112-a280c028d5c4 | -8.5535 | -51.5776 | 2025-06-24 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bdda1493-64ce-3d91-a345-00beae3384d6 | -8.5537 | -51.5567 | 2025-06-24 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| b440d008-eeff-3c6e-b024-ba54cf0cc843 | -8.05598 | -43.11268 | 2025-06-24 05:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| cad6ba00-4f40-3169-bd63-6fcfcd69e6c8 | -8.06769 | -43.11459 | 2025-06-24 05:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 4f985a6c-d289-3f3e-a6c1-b25bd03aa694 | -8.0597 | -43.10785 | 2025-06-24 05:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 8c9d850b-4deb-397e-a4c5-14e22785ac63 | -8.05871 | -43.09644 | 2025-06-24 05:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| a48c9ae7-d25c-3aa9-9d4e-447d9bad56c2 | -12.75668 | -44.40043 | 2025-06-24 05:12:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c69cdc17-17e5-3f76-bfc8-972cd9b7aa1f | -18.61464 | -44.26086 | 2025-06-24 05:14:00 | AQUA_M-M | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 54cc9ab9-7229-365d-9662-0708545f73e0 | 2.75021 | -60.36629 | 2025-06-24 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b31b9c38-3a06-3d81-b0a8-1fce8c058e91 | -4.27542 | -48.18311 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 730c26d2-103d-35f3-9b16-2eb7c08ed52d | -4.54408 | -48.01081 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01199bcf-500c-3a35-9714-32c7d3ef80fe | -4.53822 | -48.00969 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7a0d5eab-118b-395e-b509-f5090f21c59a | -6.63753 | -47.85257 | 2025-06-24 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfe4e085-a620-3280-8806-328d783a8d53 | -4.53886 | -48.00531 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56687e65-a45b-3f76-9134-47c0a92df2f3 | -6.17055 | -47.27316 | 2025-06-24 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 919be4f9-397d-314a-8793-a401f85a8c99 | -4.53697 | -48.00642 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 743342fb-0293-3226-b949-b50c79c60492 | -4.54471 | -48.00647 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f3acc74-3c7e-322c-ab36-772b468ce1bc | -4.54282 | -48.00761 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6256a90b-8fed-3995-aac4-54dc427fee4d | -4.54222 | -48.01198 | 2025-06-24 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 81ff553f-c699-3b32-a075-d4197e165d7a | -6.63689 | -47.85737 | 2025-06-24 05:16:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a95594d0-6bca-362b-91d9-6e82d0bd2988 | -8.57272 | -51.5829 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99dca40d-aeea-3343-81f8-f27ad84e3cf3 | -8.5602 | -51.56385 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a70cfc9b-9cb7-3c31-83e7-9ac26a30e198 | -8.56736 | -51.54764 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README16.md)
