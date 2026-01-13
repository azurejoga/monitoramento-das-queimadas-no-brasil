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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06766a72-ef15-324c-ad25-6a15c6ec7f7b | -2.87453 | -45.22108 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5dc9b206-db5f-3c5f-be4e-5386e66c2739 | -4.25773 | -48.84007 | 2026-01-13 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40699035-2af2-3f93-9022-19724f605166 | -2.87174 | -45.21701 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7c70cd-382b-34a3-af9a-65ef4d8e307a | -5.10005 | -43.2319 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d025bc1c-1013-3a86-ac07-a611adcaac8a | -4.42533 | -43.10262 | 2026-01-13 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 781488a7-47cd-3343-917f-4ec136d57878 | -5.10733 | -43.22935 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aa5de837-8937-3fd9-a2a6-af1297508fbd | -3.54242 | -43.66166 | 2026-01-13 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af7152d9-fc74-3fb2-9fa0-dcf3e34953c6 | -5.49392 | -42.15211 | 2026-01-13 04:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 63c194d6-58b6-3249-93ff-371522a088b3 | -4.75077 | -43.25077 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 698f63ac-de53-38b6-a5e8-dfdcc99549e5 | -2.86949 | -45.23117 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a0d96b8-24a9-3d94-ad8c-0763e35358a6 | -5.10341 | -43.23241 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bd2bc505-9280-31cd-b44d-4041d8016538 | -3.29311 | -42.54699 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad962ccd-4ee0-3e82-b8aa-0d82a9da8f94 | -3.89301 | -38.37942 | 2026-01-13 04:21:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dd5d0e8d-1910-368f-bdc7-6794a7b08837 | -2.87284 | -45.2317 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da9ee4bf-59fb-37d8-bc5c-7099ca411c00 | -3.29318 | -42.43549 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e85d30c9-bdd7-3b1b-bae3-be30b912b287 | -3.59942 | -41.86306 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 033f23d8-52ce-3305-ad36-c18b9647e11e | -4.18952 | -40.11447 | 2026-01-13 04:21:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bef65b83-40b1-3763-9242-b872dd7966ae | -5.49683 | -42.15654 | 2026-01-13 04:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0b5ea2a4-0392-3320-a28b-2596b7022064 | -3.82284 | -41.26283 | 2026-01-13 04:21:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1960012e-d93d-3a49-a7b8-e29c11bdb050 | -4.50202 | -46.09804 | 2026-01-13 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb532ff5-edf9-3f22-874a-586f86f5fcaa | -5.09332 | -43.23088 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a41f0d8-47a8-3176-aadd-edb16b794b79 | -4.4259 | -43.09906 | 2026-01-13 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74e92003-de86-3e6d-859a-c7c0f3c2226d | -0.10724 | -51.43447 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d300eda0-1a2c-3f89-8680-174b0029a711 | -4.07199 | -43.38422 | 2026-01-13 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 494ed84d-1ce5-332a-ad1c-b6804a22ab9c | -3.5391 | -43.66114 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54d06236-1de2-38b7-b351-74bd78e5200a | -2.86724 | -45.24535 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c862017-8481-3e42-ac17-6140a06ef0f0 | -2.51825 | -44.12484 | 2026-01-13 04:21:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 423ea61d-166d-35f3-8c31-09f80251d33a | -1.64167 | -45.96402 | 2026-01-13 04:21:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f0f244d-7daf-3255-b033-a304d91579de | -4.92118 | -43.42573 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfc6dfe1-727d-3b2c-918a-634243f18770 | -5.10507 | -43.22168 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a305c6f-95de-3b1d-a1cc-0e9f544ad050 | -3.29876 | -42.53305 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 75e1287d-74d1-354a-ac5b-25bacdf3c0e4 | -5.62584 | -43.25423 | 2026-01-13 04:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e72d4b-532a-3fa8-8930-e023aa41943a | -4.25952 | -48.41941 | 2026-01-13 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f05c104-f0c7-363d-8f0e-f99ac65b2f4a | -5.52923 | -46.84227 | 2026-01-13 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65769322-f5ef-32a5-b2df-33839e0b7e81 | -3.60637 | -41.86415 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ceaed892-e05d-32ea-91df-1faee23106b6 | -2.92714 | -40.59863 | 2026-01-13 04:21:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 941c0406-445b-3bd5-9da8-8978195f7ac4 | -3.89729 | -38.38002 | 2026-01-13 04:21:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 76814b4e-1606-3ba0-8f79-517b12c3188f | -5.41603 | -38.16715 | 2026-01-13 04:21:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6c7a75c1-c8cd-34b0-899e-de23cafca2c4 | -4.76056 | -41.79438 | 2026-01-13 04:21:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e0adf51a-9618-3b4a-b43c-619eef135ee8 | -3.60578 | -41.86796 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0efa929b-0d30-35d8-ad03-d2d30084ada7 | -5.09668 | -43.2314 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 96db1a40-6c06-378c-a3d5-43b275920c3b | -5.41738 | -38.16589 | 2026-01-13 04:21:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a2a52e90-0088-3096-aef3-38f75108b75a | -5.46002 | -46.90556 | 2026-01-13 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3135e2e4-5e38-33f9-865d-7843fae988b2 | -5.09277 | -43.23444 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95be0a4a-e081-34da-9191-eb0531669895 | -5.09949 | -43.23546 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3caf42ab-e5b0-3217-a515-5a1b382322e8 | -2.86501 | -45.23773 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57218337-90b4-320b-af55-e638878e33f0 | -3.55123 | -43.64885 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f2fad08-0fe6-3d0f-a1ae-cfe0e4dcb787 | -3.30497 | -42.53772 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21652df8-994c-3e2c-82f7-7a74532347e1 | -2.7091 | -45.49194 | 2026-01-13 04:21:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff12673-d0e5-3c7f-b05c-d1b777a04a48 | 0.62556 | -50.77517 | 2026-01-13 04:21:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98229c3e-955f-3e40-8500-7a798c5f5fc1 | -2.95826 | -40.47056 | 2026-01-13 04:21:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68a67619-38f1-397b-a586-2f59e480a587 | -5.92893 | -43.33324 | 2026-01-13 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1563ae56-0098-3dc8-8fb9-e1c718187137 | -1.90445 | -46.27069 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47232d13-ad22-30c2-8721-cfe1cf316dec | -5.09723 | -43.22783 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| bd8b2b11-9ae6-3ca4-841f-94c8e3889572 | -2.8734 | -45.22816 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7585528d-20eb-3b7a-80e9-75b02ebf1d4d | -1.29277 | -53.69114 | 2026-01-13 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae683618-7ab8-39e4-911e-2f77159d3ee3 | -1.34022 | -49.09347 | 2026-01-13 04:21:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3665dbb-564d-3776-8bd9-e439ca1daa8c | 0.62078 | -50.77595 | 2026-01-13 04:21:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dafdaa90-e1fb-3eb0-a51a-430624bdca6c | -5.28263 | -43.5646 | 2026-01-13 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef53f7a1-403b-3b16-9af3-de41dcda4723 | -6.06016 | -43.25394 | 2026-01-13 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88f560f7-4120-3b7c-879f-c9cc5ddd3507 | -3.44306 | -49.00773 | 2026-01-13 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d143749-6a49-374f-902e-373cbd3f5d16 | -3.34812 | -46.82077 | 2026-01-13 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b34ba84a-12b7-3306-b5d1-d9b717189656 | -4.42198 | -43.1021 | 2026-01-13 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b4244e4b-c925-3f92-b0bc-e42e6fac924b | -3.28915 | -42.55008 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04d3941e-6986-39b2-a6e3-19c9f308bed7 | -5.10396 | -43.22884 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c8d0131-53f7-30f0-aab3-75ec69651166 | -3.30101 | -42.54081 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 08f4dc50-9e05-33a8-8c23-8607f859a592 | -4.59891 | -45.99799 | 2026-01-13 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 762ec2f1-5a3c-36a1-a3b1-d01e6db0fec4 | -4.95372 | -43.69347 | 2026-01-13 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e04b1328-08d1-366d-9da5-8aa0f0760cfc | -5.53324 | -43.67946 | 2026-01-13 04:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044f0915-9bfb-3e43-9798-e5272dbfe570 | -4.41862 | -43.10158 | 2026-01-13 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| bd3ce142-5bda-3b82-8b02-0c8a9870d122 | -3.55014 | -43.65577 | 2026-01-13 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb3c6309-28aa-32d6-b8ee-2f7fb19fdb6b | -3.54682 | -43.65525 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e4e6a0e-5f48-3d00-a990-fc61b9648fa6 | -0.51524 | -49.13 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32732324-79cf-3deb-832c-37b7f7d2310b | -5.10452 | -43.22526 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fc3497ea-f4c2-3fd4-8fe9-a65fb91fda35 | -4.7326 | -45.79758 | 2026-01-13 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 664015cd-ac2a-3263-a7c7-ffa50e647967 | -5.09443 | -43.22374 | 2026-01-13 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 158e5b6e-45da-3ab2-886a-aaa725478c21 | -0.39109 | -48.54312 | 2026-01-13 04:21:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3547a45e-334c-333b-acb2-a6d364e6cd99 | -3.92359 | -42.41451 | 2026-01-13 04:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76199266-a2e8-349d-84f0-484d2e7a3e8e | -2.51879 | -44.1214 | 2026-01-13 04:21:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7bc2ab0e-0214-3db8-a133-bada7bb1af7c | -3.42368 | -43.16493 | 2026-01-13 04:21:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60319369-90ec-3c73-bc29-82a1ef7d63ed | -3.554 | -43.65283 | 2026-01-13 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b665858-ddb5-37e4-84c8-e454bea90db4 | -2.86445 | -45.24127 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19cabc91-819d-33a2-814f-4964a3b04241 | -0.0453 | -51.65992 | 2026-01-13 04:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d8b62c4-65ac-3bc2-977d-d47a3f74ae7c | -1.01719 | -48.9602 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 214d04ee-9cd7-3e9d-aa37-bff9021be3bb | -2.87061 | -45.2241 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d421007-869e-3874-bdd6-0db8ace43b53 | -1.90507 | -46.26683 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad650832-113d-3486-b452-b5ccb88424af | -3.55455 | -43.64936 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aefd075f-69c4-3177-98bb-f583bde0806a | -2.87396 | -45.22462 | 2026-01-13 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa8f2268-5634-3787-9a2d-58e65e87435e | -3.63124 | -43.09639 | 2026-01-13 04:21:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d358fe5-d62d-3603-9f1b-8b27a1bf0893 | -3.29375 | -42.43185 | 2026-01-13 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1f43a22-d75b-3863-a52f-076f8f2ae732 | -5.24516 | -37.50363 | 2026-01-13 04:21:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7ac9024-362a-3b66-bbc8-49ec4852ca52 | -5.15868 | -36.59215 | 2026-01-13 04:21:00 | NOAA-20 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c749484-b895-3218-9c10-69d652d36f96 | -3.8873 | -42.58146 | 2026-01-13 04:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93cb32bf-d48e-3231-8c42-e85b2e54e95f | -4.70355 | -44.48386 | 2026-01-13 04:21:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c3376e0-4c07-34ac-8157-6b4e33897f29 | -4.6137 | -48.05112 | 2026-01-13 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0032ea1a-90db-3108-8316-574ba91f96ee | -5.92514 | -43.3255 | 2026-01-13 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b21c9ab-5ef7-3d13-ac82-47a5d1eaa26b | -6.21718 | -38.3136 | 2026-01-13 04:21:00 | NOAA-20 | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1bf5f995-2a11-3214-ba13-0e55fa0c83a1 | -0.51944 | -49.13067 | 2026-01-13 04:21:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84313749-c82c-3a5b-8750-727a3312f5eb | -3.60171 | -41.87123 | 2026-01-13 04:21:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0336b6fa-b793-33a9-beaf-eec43155fe3b | -5.92795 | -43.32962 | 2026-01-13 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
