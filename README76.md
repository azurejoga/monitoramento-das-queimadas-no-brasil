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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 934fcfcb-7124-32c0-9aca-f2150e58abf3 | -7.85821 | -61.1679 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5faee4ef-b76f-3e62-8ed3-618b10efd811 | -8.42687 | -47.24124 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8de5f94-8983-32d9-9277-097288d2da02 | -9.9563 | -51.68343 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449df207-f837-3610-b335-29d2ce7bf867 | -8.40912 | -47.26503 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f52daba-0a4c-35dc-8911-3104e0ed59c1 | -9.01034 | -45.78003 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a81a5985-cf3a-3862-9e68-cb5845a42094 | -7.90633 | -55.2687 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 417ddc20-929f-380a-ab8b-208d814f3e22 | -10.23135 | -48.638 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56d5aa66-f3ed-39c7-99cb-ca77bea22c0b | -8.10047 | -50.17644 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23639f4f-a708-39ae-9250-f60c031ef42d | -10.34107 | -48.8209 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9d373619-5cb6-3be0-8d8a-e7d299ece43e | -6.39271 | -45.64513 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e3ee69b-d74f-376f-9edd-0a74c7761659 | -4.91408 | -56.00813 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb8716e-04a6-3325-ab2a-6923e2904ef1 | -8.87788 | -49.93333 | 2025-09-13 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25453257-f1e0-3782-b8a7-35abe046f692 | -4.93212 | -55.78362 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e66b0b-794e-3bd3-9e8a-bc0cfe61abdf | -4.53668 | -55.68443 | 2025-09-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 625f678a-a610-3205-b70e-a97d7a1e53f5 | -9.80023 | -48.90452 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0554a354-2970-3707-8974-7037a0cb502e | -9.23866 | -51.24971 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b8251d7-7975-3cc6-935e-cb00ad467596 | -9.97818 | -51.71291 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c430b47-c4cf-315c-ba66-dc607c696b04 | -8.09126 | -50.18494 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2090a50-b8a5-38c3-8046-8842cb03cefe | -4.92309 | -47.86375 | 2025-09-13 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76964bfb-4073-3cc8-9bbb-a405551d2cc3 | -7.43778 | -44.40284 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40829cc4-7407-3d6d-9270-309295106d47 | -4.38424 | -55.76223 | 2025-09-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d0df4f3-9778-3f1d-8747-e5d149da4fa2 | -5.65967 | -42.61154 | 2025-09-13 04:57:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0687e03d-83ab-3517-a99b-cd323944530f | -8.09268 | -50.17525 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f608e4a-910a-3223-9baa-256bab19917b | -5.85721 | -48.15664 | 2025-09-13 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e420761a-6300-387e-a968-4abd124f3830 | -9.66548 | -47.54462 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aeeb3f45-99b3-3d2a-9f67-fcccd5e962e8 | -9.50133 | -50.88596 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65b0b91e-d260-3ec4-8026-f61a945dc150 | -6.56753 | -50.87046 | 2025-09-13 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ade5a129-924a-3ad7-892b-92851b55ff0b | -9.8155 | -48.88971 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2bd6d89-5321-3a37-bda6-00ff1a9129af | -4.28266 | -56.33458 | 2025-09-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 799150b8-2c94-3273-9925-9d659140b95d | -6.20225 | -43.45531 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baade76d-2532-366e-be7b-98df528fe81e | -5.6463 | -45.9428 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a26def0-699d-3505-b96d-dc2e8bfccdd7 | -7.41492 | -44.35539 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30bb3cbf-e354-362b-a04e-8b63bd98874a | -3.51459 | -47.21818 | 2025-09-13 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a5a4002-31c9-3522-89d5-d5b926253938 | -7.76138 | -61.12517 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4d3be5-85ef-3edf-a6d8-fd6ec3fcc09d | -9.25414 | -51.24759 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f49e726-d24a-3ec1-a73f-62892a8f81b4 | -9.96211 | -50.3906 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cd85af0-9bc6-3ab6-a045-5f3dddcba162 | -5.20597 | -44.31149 | 2025-09-13 04:57:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 194ee63c-4563-3e36-8a16-fb5d94bee8a9 | -8.52611 | -54.76737 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df3e47c9-2267-38c7-a191-c8cace159b3b | -7.54159 | -52.51498 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b222708d-465a-35d9-931e-8133afb42edd | -9.79585 | -48.90415 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b69eda9f-9791-3236-a69a-c9275f2cfe86 | -8.43773 | -55.63014 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b8dab9a-9474-3320-b5ea-f4630cc5c34a | -10.33184 | -48.82146 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18661cb5-5602-3e59-b7af-666471bc5d97 | -10.00426 | -51.73866 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d9a0eb0-d65b-3994-a2aa-f418aa865dfe | -7.02393 | -44.8936 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f5d4453-f118-3374-8fdf-7643f5a63e4d | -9.24236 | -51.25028 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0952c06d-8ed0-3a32-898d-f424c711b9f5 | -8.09701 | -50.17774 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e563f4fa-e126-349a-9365-b6449b5ab6ae | -9.2548 | -51.24318 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71c8d9ae-b24f-37c2-b5a3-5c0c25a9804b | -9.96854 | -50.40204 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b84137f-9bc8-3581-99d7-4cfe789c3336 | -8.84833 | -49.58804 | 2025-09-13 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d557ac3-4f0a-346c-be13-54589f082ef4 | -9.72634 | -46.91666 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dcd93fae-25f0-3c98-a18e-9add9e655cf0 | -9.82748 | -48.89947 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db367980-8c8c-3b1c-9e50-945c422d4748 | -9.54821 | -53.58983 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2f0ed5-1e0a-327c-909a-96a194cd8588 | -5.72354 | -43.19343 | 2025-09-13 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7bda45d-1fa4-33ab-9d28-1184ed5554e5 | -7.07154 | -44.12324 | 2025-09-13 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2435fee3-06e0-349c-85ef-be14c598137e | -10.14924 | -47.90373 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83e654b2-7a6a-30e7-8494-a10396b77bf5 | -5.7708 | -46.1528 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30b1895d-96c3-35cb-a2a4-0998e033f3d3 | -9.24221 | -51.26624 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62198f70-766e-306b-a530-a08388eb1234 | -7.43255 | -44.39842 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a85e168-1428-364e-b4ba-1c9570a74197 | -5.10998 | -46.07144 | 2025-09-13 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1b34bc4-3505-3222-a04d-42ca9193cd6f | -9.51438 | -54.6258 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad2cb851-869b-3db1-ba2c-b29df6de0057 | -7.07726 | -44.12452 | 2025-09-13 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2cd2657-155c-30e3-a137-c838602be720 | -9.70714 | -47.52984 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5d9694f-2c07-38de-ac35-0b9e47abbf83 | -7.90688 | -55.26522 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e34782cd-4d49-31f8-9774-a8ea93745aac | -7.3223 | -44.5989 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b2dfd72-a60c-3b71-b4cd-993f5adfcf59 | -6.84612 | -45.65969 | 2025-09-13 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe9aaf29-0217-3139-a377-415624b5ecd9 | -3.23694 | -46.78188 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 050c711d-e265-3508-956d-aaca29503181 | -9.24475 | -51.25977 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e907f434-fd68-315e-8bd3-cf1acd15b44a | -6.39227 | -45.64843 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59e167cc-2120-33d8-9f7a-39fbca86f39a | -7.43677 | -44.41044 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1562809-a8b7-38e6-8411-5b54074eadfb | -6.98951 | -43.80694 | 2025-09-13 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 590c9f0f-db26-369e-a6a1-44d209fefa14 | -9.24673 | -51.24642 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99e7c822-4fb0-3200-9d73-7ee9da60f1af | -8.05082 | -52.32096 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35a17cd-8ade-3b0e-bac2-69f7b8c87e0a | -3.90087 | -54.68578 | 2025-09-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ab720cc-2af9-3e41-b70d-1a1cb52e4b1c | -9.73212 | -48.34925 | 2025-09-13 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd4475bc-7269-325b-aabc-b198215422c7 | -9.95689 | -51.70527 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e670a8b6-2893-34b3-939f-cee8ec536e6f | -9.24284 | -51.26176 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ed203688-4604-37d7-961f-1e5f219a5872 | -3.48599 | -48.43511 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 714b50f8-f0c5-3e18-99b7-04d24b58cd4a | -5.66036 | -42.60649 | 2025-09-13 04:57:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 74422255-64a1-3487-80e6-dceb886e7c58 | -9.88802 | -51.86666 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0c9c70b-3366-39a5-8a15-22830beadaaa | -8.52281 | -54.76685 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0785ff-a9dd-3776-b81a-b02c43843c0d | -10.00061 | -51.73812 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfc4dec7-aa1d-3d80-8643-7d92dcfcda6d | -7.43102 | -44.41 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94f2fb2b-adc4-3aeb-b38e-7c51f877176c | -6.85177 | -45.65716 | 2025-09-13 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5522cff-77b8-3396-b8a6-60a3612eac39 | -10.33247 | -48.81691 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe5671f4-3744-3035-84cd-7b7461d1da52 | -9.73867 | -51.00927 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be4063de-933c-332f-8d77-6b7ccc1d091e | -8.40838 | -47.26414 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2935249-e223-3429-aa04-7fde82a435c2 | -9.25714 | -51.24123 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| deba6bae-4327-3d7e-9361-577e161a0c14 | -9.03277 | -47.05867 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50fe4b00-897a-35dd-9911-c934fa5f7923 | -6.12553 | -42.95932 | 2025-09-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6dd33506-c668-3fa3-80f8-4542444ff9ec | -9.2365 | -51.21292 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 464455b0-6907-395a-ac67-1c53819a5cbc | -10.22748 | -48.63309 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bb37bcf-56d8-3879-b21a-70017669b164 | -6.83557 | -47.8572 | 2025-09-13 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ef5cc7d-5018-3e72-8d4c-53e8304ae8d8 | -9.50064 | -50.89069 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d1518e4-2b9f-3af9-96c9-f4af8ee5810d | -8.10618 | -50.19167 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e099cd16-00df-3ff6-b66e-43aacb1516de | -8.09433 | -50.19667 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c34cde2-6f85-320a-8f63-833d24b35df6 | -7.75696 | -61.12443 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e565ec4c-1d16-35c3-916e-4341036a20c1 | -6.46764 | -46.03264 | 2025-09-13 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc3a9b1a-ea79-368c-9e6f-c17a4ac61287 | -7.42113 | -44.35245 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0ba7f0e-bd93-39f8-9382-d39c26765f89 | -9.52105 | -54.64821 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25e14b60-4310-3c85-87c3-2c3d525cb5f2 | -10.11563 | -45.50524 | 2025-09-13 04:57:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
