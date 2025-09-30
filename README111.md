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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7318de21-0391-30ee-9224-5fce3f88cb2b | -11.30653 | -53.96694 | 2025-09-30 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ec7c87a8-d539-3c07-92f0-f06f22218142 | -9.28129 | -57.1494 | 2025-09-30 12:57:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 158f96ae-7725-3c43-93c6-9af0151d1768 | -11.27078 | -47.21521 | 2025-09-30 12:57:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f42e0702-89ea-3139-ab2a-cbe91758b0dc | -7.16542 | -52.81763 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c7706a1a-97be-3646-b4ea-0d65b3b1cebf | -9.94658 | -55.15374 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d46a07c7-aad0-34c8-9969-4cf249c26a07 | -12.23341 | -47.78924 | 2025-09-30 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 93b31fb1-252d-312e-8902-803c236bf1f6 | -7.16364 | -52.83089 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 47edeb6e-03bc-31bf-92d5-1c5070009e8b | -9.94519 | -55.16408 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fe8d56bb-ccb4-3b5a-b303-926b71c059e8 | -10.54495 | -47.88075 | 2025-09-30 12:57:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 982356ea-9472-307e-851a-afe0b8062c20 | -7.8715 | -47.24064 | 2025-09-30 12:57:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 2fa833d3-ba81-3b7b-ad7c-5bf6b2839a8e | -11.16525 | -54.12709 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 9a16c7ef-4749-37e4-adf4-440af0edb7a6 | -6.44561 | -51.84808 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e0b9966f-4e8c-3a28-8b10-3518977bcdb5 | -9.42019 | -54.719 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6aa91809-a5f4-3e85-ada9-464f1e85a200 | -11.61213 | -54.14025 | 2025-09-30 12:57:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 53ea944a-d303-31fe-9ee3-3ba40374dee3 | -7.83699 | -46.75233 | 2025-09-30 12:57:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| bf13f98e-727e-33de-878e-f3224624fbca | -11.03242 | -49.79945 | 2025-09-30 12:57:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d06f52a9-df81-3109-bdc4-b2356a2addf2 | -7.2422 | -49.51928 | 2025-09-30 12:57:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 58b9b403-8583-37be-b09d-67946faaf3d7 | -9.58249 | -54.58723 | 2025-09-30 12:57:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fdb5c2ee-8e99-30df-b41d-d1d9efe28914 | -7.24525 | -49.49526 | 2025-09-30 12:57:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6ef88e7a-ac75-334c-b803-9db60d255f08 | -11.17746 | -47.24318 | 2025-09-30 12:57:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2cdb3ec1-42b4-3d33-8d21-9b0ddc373c7f | -10.31099 | -48.27522 | 2025-09-30 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 9666c9f8-8c0c-3339-9036-1d43a18380a9 | -8.36823 | -51.32917 | 2025-09-30 12:57:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ec5970d6-c38d-3b6c-899b-544e1969da4f | -11.19952 | -47.20299 | 2025-09-30 12:57:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b87c2d69-1564-32eb-bba7-9c7e1de3991e | -10.84053 | -55.95559 | 2025-09-30 12:57:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7856e952-9154-3025-bc73-e75a9cd69324 | -9.82912 | -48.95528 | 2025-09-30 12:57:00 | TERRA_M-T | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| dfb4acee-1ded-30f6-af90-2ed5c94b8c24 | -10.05693 | -50.22744 | 2025-09-30 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d1596e95-2c02-3fe6-8471-f89fce7ff40a | -10.98666 | -54.16607 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4b597745-1fc1-3853-87c2-a0048cb76ca0 | -9.12735 | -47.62169 | 2025-09-30 12:57:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 84c883d5-15c8-3024-a11e-244b3d771790 | -9.42974 | -54.57702 | 2025-09-30 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 239.5 |
| 23f77957-9f80-3c95-a686-141eaa548620 | -11.1566 | -54.11341 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 24a3a942-dc98-3f94-af0b-01dafeb78c93 | -9.40088 | -54.7164 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 84ec0a86-e609-3d6b-982c-81866a4a9bd7 | -7.82691 | -46.99957 | 2025-09-30 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 713ebef8-b813-3387-9a07-ef5b6db092e4 | -10.88653 | -53.75028 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fb2ef7c9-0241-3aa2-ad10-048671e5d20c | -11.16691 | -54.11469 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| d7e909c8-4490-38c2-accb-a459b00c9762 | -7.67648 | -50.50896 | 2025-09-30 12:57:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 5434fa2d-7d85-3204-b6bc-b933bb7eb18c | -10.10193 | -47.79998 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 1fa57402-d8a9-378d-906e-6c4e48b0f524 | -10.9765 | -55.44607 | 2025-09-30 12:57:00 | TERRA_M-T | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 19a1e932-2dd6-3f68-ab7b-aebacdd79fde | -10.30287 | -48.26727 | 2025-09-30 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 14642bee-83d1-3466-8438-2af4270a3e0e | -9.43122 | -54.56611 | 2025-09-30 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 96856b96-86b1-31bf-89da-718575b6a504 | -10.1074 | -47.80564 | 2025-09-30 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 50a55919-e514-3f98-b70e-7551dce5f1f7 | -9.79039 | -54.02621 | 2025-09-30 12:57:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 102325a4-a617-3c50-84e9-f8261156027d | -6.43614 | -51.84052 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 58c6339e-71de-31c1-8f44-db761bb6e73a | -7.83025 | -47.00467 | 2025-09-30 12:57:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| ca6d541e-4cab-31ff-8814-a1bf6ce24c45 | -7.83811 | -46.75938 | 2025-09-30 12:57:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b43b8dc8-02ac-3d46-b52f-449d233fb428 | -11.26695 | -52.74512 | 2025-09-30 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 36cf486e-7d3f-397b-9c61-d98bca962a5f | -10.38709 | -48.18039 | 2025-09-30 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 11440e5b-29a4-3773-85a8-be253ec752b4 | -10.82844 | -47.97832 | 2025-09-30 12:57:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5c2067ca-75b5-35f9-9a2c-83057170e080 | -9.40233 | -54.7057 | 2025-09-30 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 9894aec8-9fc2-38f2-90c6-ecc6c234d294 | -11.15496 | -54.12576 | 2025-09-30 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8d1ffafa-d108-318f-82ea-8a644b0f03c0 | -12.23629 | -47.79735 | 2025-09-30 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 466670a3-9180-3b94-83a2-cfa77ee3632a | -14.56678 | -48.47998 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| cce938d2-0fef-3f24-a123-14649f2bb430 | -15.72617 | -59.51693 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e4bb3d8-b870-3bcf-9521-684ca7aa9368 | -17.9253 | -57.57843 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.1 |
| b4a331dd-48da-3032-a406-924821a24a01 | -15.26056 | -49.71727 | 2025-09-30 12:59:00 | TERRA_M-T | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 33c9ae40-5b64-32b6-a2ea-50ca4bebf44b | -15.26873 | -51.47917 | 2025-09-30 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| fc22f5e2-0e40-35ca-ad62-36d878c30fa0 | -15.86313 | -59.33599 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b58839f7-60a1-36dd-bf63-b1b32f672c2d | -15.27122 | -51.45632 | 2025-09-30 12:59:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 63a093a8-2aed-3980-8b8a-314e7c6bc3c1 | -16.74837 | -51.36415 | 2025-09-30 12:59:00 | TERRA_M-T | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 74556810-beeb-3efe-9f5d-96fe26781091 | -17.9161 | -57.5774 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 75502b07-2eb6-350d-9a45-7559c681f322 | -16.75109 | -51.33838 | 2025-09-30 12:59:00 | TERRA_M-T | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 24d0ecd7-9a3c-3e85-8d17-57ceb1529a47 | -14.59338 | -48.20449 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| acd0930e-db85-3e52-9971-c96a1fd896a3 | -18.22554 | -53.29979 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 82518ba3-b698-34a4-8250-897f62497f81 | -17.90558 | -57.58629 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| ebdf5c97-aefa-358d-9762-f2e381f27a60 | -13.81191 | -47.90701 | 2025-09-30 12:59:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 96e79a94-70f6-33fd-bb2a-ed13936d6f31 | -14.8517 | -54.76665 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4986718c-a315-368a-8248-1e24777d19e5 | -15.24436 | -56.79082 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1f209960-92fa-3197-b7a9-960094d13e7b | -16.02148 | -59.51456 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34e623c9-4999-35ed-9000-4e3db2891a47 | -12.95908 | -48.42115 | 2025-09-30 12:59:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1dc73b3f-0043-3594-be08-89eb1c87ef25 | -17.57016 | -52.17789 | 2025-09-30 12:59:00 | TERRA_M-T | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| adf552eb-eaa0-3fc1-ae74-c0754f0d067c | -12.2682 | -58.05413 | 2025-09-30 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 277a6603-8754-39cd-bbe5-30111d8c2da4 | -13.39666 | -48.07449 | 2025-09-30 12:59:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a8bdf13f-3924-39c8-812b-1514fd96ae7e | -12.96521 | -48.42725 | 2025-09-30 12:59:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4ff757b3-7b02-3c73-a5b3-06bd4d2cf232 | -12.46253 | -58.56106 | 2025-09-30 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ca87ef25-0455-394f-ae6e-9ac677f75142 | -12.15718 | -54.56643 | 2025-09-30 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a605576c-cbfa-3a9b-985f-61be17d78fdf | -15.84307 | -54.02783 | 2025-09-30 12:59:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8858782b-6259-37f7-be0b-f9390dbafe4e | -15.25495 | -56.78207 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7171b527-1d3f-3884-b91b-8d398fe99e92 | -18.22361 | -53.31662 | 2025-09-30 12:59:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 7968b2a8-c618-31ec-8825-7f4f2dcb2bd7 | -16.56555 | -50.06847 | 2025-09-30 12:59:00 | TERRA_M-T | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 99330510-1223-3a0e-94f5-9a32f77ebf11 | -15.59272 | -53.13516 | 2025-09-30 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| d8113a70-e828-317f-b45b-2db8c9abe722 | -13.5621 | -56.85379 | 2025-09-30 12:59:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b628625-1e6d-30ce-9a60-3b3926d0e94f | -15.35068 | -56.9626 | 2025-09-30 12:59:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6c1d43a6-e797-3e42-bb58-5638a06f4a87 | -15.16763 | -52.81536 | 2025-09-30 12:59:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 6a7f898b-8cb6-30a8-9992-c5225cc0e821 | -16.56235 | -50.07328 | 2025-09-30 12:59:00 | TERRA_M-T | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 4b1c3b4e-3d20-3775-a40f-9710bf5881a1 | -15.25722 | -49.74833 | 2025-09-30 12:59:00 | TERRA_M-T | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 380e832a-ddc8-371f-bdcd-6fae92ff2572 | -14.28187 | -57.70566 | 2025-09-30 12:59:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 73f379ea-4179-3585-958a-6a68b306989f | -15.59872 | -53.12927 | 2025-09-30 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| cd9fccff-9b1e-30ef-b3a5-6ccd92ef903a | -15.25636 | -49.7243 | 2025-09-30 12:59:00 | TERRA_M-T | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 275ba091-8b0e-3b58-ac48-b7ca1154dfdb | -19.57723 | -49.42125 | 2025-09-30 12:59:00 | TERRA_M-T | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 48e580b8-1895-3ec6-bc9c-31922d760183 | -15.63032 | -49.17624 | 2025-09-30 12:59:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| a14dc0a6-4479-3327-8a14-ff0e451f0aff | -14.51137 | -48.42345 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 82e0c950-2ca4-3198-8b8d-f78555233a9c | -15.85421 | -54.02908 | 2025-09-30 12:59:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 43e7986e-2c34-3658-8f86-25046f3b4345 | -14.54986 | -48.47936 | 2025-09-30 12:59:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| cddfea6d-d147-3e4a-8873-cc286cef4ff4 | -15.59663 | -53.14655 | 2025-09-30 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8475837f-d699-3d0c-8e69-af1bbad22a0f | -17.91477 | -57.58733 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 86b5636f-3a66-308f-8eda-a17509f67878 | -15.86447 | -59.32683 | 2025-09-30 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f1bf7ef2-7d56-343b-87fe-171d641a7951 | -12.59242 | -57.92413 | 2025-09-30 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 75b131bc-32ac-3568-b822-79cd66ac0071 | -12.07164 | -54.75216 | 2025-09-30 12:59:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 08cf961e-950e-35e1-ae14-bc0ca0c113fc | -15.85439 | -54.03568 | 2025-09-30 12:59:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 30aac6f4-ed59-3b07-9b9a-a461a86dca92 | -15.25757 | -56.8325 | 2025-09-30 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dd1116ee-21c1-34eb-8636-86151fdbc818 | -17.9345 | -57.5795 | 2025-09-30 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |


[Clique aqui para ver as próximas entradas](README112.md)
