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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b8db91b-ab9c-3fd9-a30b-8be12563fa29 | -6.6929 | -59.0966 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 8a340858-d2d3-3408-9f7b-061f9b19820f | -6.6014 | -58.9844 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8f4ab366-8280-3cc6-bbe5-9f08af10fdaa | -8.6913 | -54.648 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7f8b08aa-11e9-3e04-bf0f-9a307facd23e | -6.9128 | -59.3578 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e4af7d1f-b76f-3cb5-8169-20dafa04c5e4 | -18.0487 | -44.6066 | 2026-08-20 00:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 37c7971f-321e-3b99-85e8-75935294949d | -1.8425 | -54.4917 | 2026-08-20 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 4c13ca8a-f865-3ef6-a7ec-51b9d78a33b4 | -6.583 | -58.9658 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| e1d6cebf-f1d2-3a6a-947f-bba706e8c946 | -6.4392 | -52.7138 | 2026-08-20 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a5da240f-7bbb-31f2-a4eb-f14baafad121 | -17.3365 | -43.6383 | 2026-08-20 00:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 09864f78-2152-30e7-89d2-08a8edbdd155 | -12.4726 | -54.7382 | 2026-08-20 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| bf71906c-1d81-3e78-8280-18f9105b6389 | -6.4389 | -52.7548 | 2026-08-20 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| cd6d5f09-c9fe-3020-9d1b-33c67e344a9b | -6.7114 | -59.0958 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b1eb1fda-ea10-37ba-b859-f1b0bc41b3d2 | -9.2256 | -59.7894 | 2026-08-20 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| e602e58f-133c-32c2-bbc8-5b9001e53bbb | -7.9563 | -44.6667 | 2026-08-20 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 8c2ef570-df39-315e-81c7-58355308f0f3 | -8.6727 | -54.6492 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 242.2 |
| be7f4e13-9af2-3a9e-8a58-ca4aabdf8bd7 | -7.36 | -45.8361 | 2026-08-20 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 338.4 |
| fa4f86ee-cdc0-3560-a28e-f393df66a419 | -6.9313 | -59.357 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 0c2e37d5-55f4-366f-954b-eeb88d32e9fd | -9.2258 | -59.77 | 2026-08-20 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| bf8fe011-f6ff-3ea4-8c91-1f68f15963fe | -18.0285 | -44.6113 | 2026-08-20 00:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6cd5b743-005a-3f84-bc50-292d367853a7 | -6.8593 | -59.0318 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 4d6e0faa-6c08-3c6b-9931-9d4f27b1a81e | -9.12 | -51.1534 | 2026-08-20 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c6199451-0072-38c0-96eb-635946eb663e | -7.3413 | -45.8377 | 2026-08-20 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 1d6758ee-03b1-3421-80da-5d396919033f | -6.8778 | -59.031 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 168a00fc-6507-3e50-b7c0-b51e4adb4ab0 | -8.5401 | -54.8802 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 75e5f76d-131e-3049-9dfd-c3761d9ec209 | -9.2071 | -59.771 | 2026-08-20 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 1fd06182-424f-363f-85bf-4baa463f20d0 | -7.34 | -45.85 | 2026-08-20 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 796be1e1-0b40-331c-ae9d-8393e20c162f | -7.37 | -45.85 | 2026-08-20 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69579a20-c7a8-3924-9d1b-2b374d31a952 | -8.66 | -54.62 | 2026-08-20 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d67917-4ff8-3811-bad4-e2bdfe25b1aa | -8.66 | -54.69 | 2026-08-20 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71a38c9b-7e4e-3375-bfb1-3278760636ff | -7.34 | -45.8 | 2026-08-20 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dddb5f25-d5d5-377e-91ba-b6e7cbf417c4 | -18.0285 | -44.6113 | 2026-08-20 00:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b95b662f-79fd-3a9d-83ab-2e6d98829835 | -8.654 | -54.6505 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ed935d25-aa5b-30a2-abbf-da2727df907e | -6.4389 | -52.7548 | 2026-08-20 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b370f06b-f260-3cf6-a5eb-9d7da56d08ac | -9.2256 | -59.7894 | 2026-08-20 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6fae8d0b-56e4-3847-8b6a-4d16cdeb8f51 | -6.3863 | -54.9451 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ead7aa3e-88c1-313b-a8ef-b32e9606c98b | -9.2258 | -59.77 | 2026-08-20 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 1627f6f7-264c-3c8e-be0d-79966c373b82 | -8.6725 | -54.6695 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 01260a42-f956-30a8-8398-245d7c816ab2 | -6.4392 | -52.7138 | 2026-08-20 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 83054ca6-ad0c-3600-8013-0111192fe929 | -17.3365 | -43.6383 | 2026-08-20 00:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6a37f7da-e382-35e9-bc14-616be878c489 | -14.221 | -52.9041 | 2026-08-20 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| deffb7c0-2886-3adb-a0f4-0238722790b0 | -9.4071 | -60.417 | 2026-08-20 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bb8adb72-ce1a-37a0-9abc-7cfddf8d5a2c | -9.4257 | -60.416 | 2026-08-20 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 31e960c9-faa0-346d-87b1-ece3f4feb0c7 | -8.6727 | -54.6492 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 8ad81f29-d94c-3b75-b5e9-ba50d42d7778 | -8.5214 | -54.8814 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b4fec698-4f6b-3652-86b1-677b7f8f735d | -9.4254 | -60.4545 | 2026-08-20 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6e2f8bf3-fa09-3154-b783-729f706763aa | -11.1939 | -53.9993 | 2026-08-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f58383f2-9d31-3491-9f29-e0a8943a3102 | -11.1936 | -54.0199 | 2026-08-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 9b7a0a1b-c18e-33df-95d3-0335c20672b1 | -5.8087 | -55.7293 | 2026-08-20 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 645f7ebe-4de5-3791-9710-de48e4439b9e | -2.5629 | -47.2445 | 2026-08-20 00:20:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 03208abf-64b0-3f1b-a717-dfcdac4684ed | -6.9313 | -59.357 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 9856a5c9-84e3-3837-8028-35b3640d44cb | -6.6938 | -58.942 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 215a61f7-249e-3ef6-94a3-62f54da32acc | -6.583 | -58.9658 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9aa6fd12-226d-373d-a52a-e9d579a463df | -7.36 | -45.8361 | 2026-08-20 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 378.4 |
| c883f377-0fa1-3dfe-9adf-c3fb94a14c80 | -7.3415 | -45.8152 | 2026-08-20 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| a6300218-8c6c-3a37-ac90-abc2bfd5ef92 | -7.3413 | -45.8377 | 2026-08-20 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.0 |
| ba94aabf-345f-3ac8-a6d0-24b788d05af9 | -12.4914 | -54.7569 | 2026-08-20 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8f4270b7-d464-30c4-b7fe-c511f45a6c8b | -11.2128 | -53.9976 | 2026-08-20 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d19f26c7-7453-389e-a643-a1099da0aa68 | -11.2189 | -55.0585 | 2026-08-20 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 9e1f9d61-a6aa-3b36-8cea-a712ac104faa | -9.4069 | -60.4362 | 2026-08-20 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 1716adee-c869-3074-951f-17a0a7c36ace | -6.6015 | -58.9651 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1c528f27-5072-349f-b08a-571eaabaced1 | -5.7904 | -55.7103 | 2026-08-20 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1a5f051f-8c08-3c94-a93d-2a7fd60fd7a2 | -6.9128 | -59.3578 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 53dcca57-3138-32f6-93a8-e3a48b65397b | -6.4391 | -52.7343 | 2026-08-20 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 910d4610-c486-38ba-99f9-a9160b25e2ff | -9.1388 | -51.1517 | 2026-08-20 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 49998c56-4354-36ea-a4ba-7a4c0fbd0ae3 | -11.2191 | -55.0382 | 2026-08-20 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 019e7fd2-7581-3c5c-a0a5-6f10d5af66bb | -9.2071 | -59.771 | 2026-08-20 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 068c07d1-a770-32c8-b172-ddf2a3e9dff6 | -7.9751 | -44.6648 | 2026-08-20 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 53f9ccb7-edf7-3058-807b-6a8d0590519d | -5.8088 | -55.7095 | 2026-08-20 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9b1c70ae-8600-3613-bc20-4d73e8cdb739 | -11.8083 | -44.8072 | 2026-08-20 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| afcdf24f-6555-38d9-9b92-7b864bb314bc | -6.7114 | -59.0958 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3344d952-9838-3885-9a2e-153a1f3ecdc4 | -12.4919 | -54.7158 | 2026-08-20 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 527af8d9-0ac8-351f-8a37-e2687a614959 | -14.4554 | -45.6251 | 2026-08-20 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d0564c7e-27fa-3b76-9bfe-2ad117f894ab | -6.6929 | -59.0966 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 11af64c1-a882-31be-90c1-ca5e55c3705e | -7.3603 | -45.8136 | 2026-08-20 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 315.1 |
| 2ee2626a-068a-3a6b-9560-fe0cf493582d | -6.9129 | -59.3385 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| dc9d056c-e3b8-399b-9fc3-9b6ca7125ead | -6.8593 | -59.0318 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 910f7423-a3a4-347a-8591-2c28d5510e7c | -1.8242 | -54.492 | 2026-08-20 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fc3375a8-d60d-3001-bf69-0fca6bb7738a | -9.12 | -51.1534 | 2026-08-20 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e7372f24-c0f9-328a-b254-90016b5e5f31 | -17.3372 | -43.6139 | 2026-08-20 00:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 5d486e78-3f1a-31c1-b134-b0a50296938a | -6.6014 | -58.9844 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 61a81eec-2080-302c-9134-b233af58bb47 | -6.9314 | -59.3377 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| e1358711-d9d5-3c76-9d27-0cb6cc8a299e | -12.4916 | -54.7364 | 2026-08-20 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| b56a4d50-6ff4-3561-9ece-ceb86b34bdd1 | -1.8425 | -54.4917 | 2026-08-20 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 68e3ae81-1049-386b-a0e3-27cb3b9d6a68 | -9.4256 | -60.4353 | 2026-08-20 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 230.7 |
| 3ac9d0bd-7d9c-3ab6-90b0-a4df7decaf89 | -6.0923 | -47.3129 | 2026-08-20 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| e55c8c80-f290-385a-abc2-fc654aba527f | -23.0838 | -49.1511 | 2026-08-20 00:20:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| dce86889-d108-3f31-b71b-cc6b15feab45 | -8.6729 | -54.629 | 2026-08-20 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0ce42b90-80f2-3f14-b187-fe57c80f0516 | -6.6939 | -58.9226 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 3326a85e-f37b-3bf1-8058-18e49bb16ff8 | -6.7123 | -58.9412 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c2a6ce37-a6e4-341c-8131-ab931bdf4c84 | -6.5829 | -58.9851 | 2026-08-20 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6abe56b0-48bc-33d1-8f00-43e8ecedbe92 | -9.207 | -59.7903 | 2026-08-20 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 139d1b3a-d2bd-3b84-9300-5eada3706a43 | -14.4559 | -45.6019 | 2026-08-20 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| af8e96c7-914e-3457-befa-5f2b42e41bfe | -6.0737 | -47.3142 | 2026-08-20 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1b319bd7-e503-3d9a-9bbe-f37b96871a2d | -11.1936 | -54.0199 | 2026-08-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 0008f4c7-60a6-3404-ae2e-7272c4632968 | -5.7903 | -55.7301 | 2026-08-20 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 16b35373-3b69-3d1e-b12a-dd61c007bb44 | -14.4554 | -45.6251 | 2026-08-20 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e5054211-85ef-3b82-bcac-ce70a869b8e0 | -17.3572 | -43.6092 | 2026-08-20 00:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3929f071-f16d-333c-9e60-916f6a312172 | -7.3415 | -45.8152 | 2026-08-20 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 296.5 |
| dee3523b-1584-3f0e-98d6-4c64e036cd17 | -9.2258 | -59.77 | 2026-08-20 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 9ef0ec60-e8ce-3945-a799-b9bda71a9093 | -6.6938 | -58.942 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README3.md)
