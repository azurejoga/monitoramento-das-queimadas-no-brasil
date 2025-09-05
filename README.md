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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43ba61f4-82dd-319b-beb2-faa82cab0089 | -7.5273 | -61.6678 | 2025-09-05 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| bd2a2852-e78a-320e-ab8a-045a3d7d9d40 | -15.7569 | -53.6113 | 2025-09-05 00:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ccee955d-dd77-3fbe-9d38-ea547d0e8565 | -19.6843 | -54.7971 | 2025-09-05 00:00:00 | GOES-19 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 72f130df-5a8d-32f8-b1c1-39e5ff6582ab | -6.6044 | -44.5624 | 2025-09-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f759f6cb-3835-3112-b7ed-07807a5e38c3 | -5.6081 | -45.0038 | 2025-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| c9e1b213-d704-3f17-b63f-b19baa55222b | -13.1079 | -57.1109 | 2025-09-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 0397a1fe-b773-36ed-8e5a-f312f127721f | -10.2373 | -50.5417 | 2025-09-05 00:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ab42fd9e-e8a4-3b72-a5bf-b9e96c1e35a1 | -11.8343 | -51.4339 | 2025-09-05 00:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e014c6e2-e66d-3b14-a36a-d7a7bf307c24 | -16.3149 | -52.9415 | 2025-09-05 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 2262456f-714a-3d49-905d-f1f659e990a6 | -5.7227 | -49.2842 | 2025-09-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 5767d966-62ee-3dc9-a2e9-ae84c560d26b | -8.0988 | -45.3371 | 2025-09-05 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5779fe30-a083-3cfb-84cf-afafecab77fe | -5.5101 | -60.1183 | 2025-09-05 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2987b94b-23f9-3430-b48a-6419842fd296 | -5.6079 | -45.0265 | 2025-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 59e6e20d-d7c0-3e7e-a758-12bdc4bd9709 | -8.0035 | -45.4373 | 2025-09-05 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 41404953-6470-3125-9170-0e8e2ef6c3aa | -5.0264 | -45.3587 | 2025-09-05 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 30d6e93d-c4c6-34f8-9c74-bec260ac7c11 | -9.4497 | -62.3485 | 2025-09-05 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0e234c7d-3305-3b07-a2b5-c47289c1c7bd | -5.0079 | -45.3373 | 2025-09-05 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 77eb0cc9-7909-3a08-8be7-c6af92ee86db | -14.2892 | -45.2134 | 2025-09-05 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7b8fceaf-0b3b-3ded-9aba-0e0e288d9c16 | -9.2102 | -57.0918 | 2025-09-05 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cfc4f3e3-bcd8-3aec-969e-7c0b015baffb | -5.0268 | -45.3136 | 2025-09-05 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c4ad2c40-76c4-3059-9381-8aa68e0b133b | -13.1082 | -57.0908 | 2025-09-05 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 402809ee-3528-3659-b52a-4ed284f4b8f9 | -6.2672 | -53.4379 | 2025-09-05 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 15ce9916-bde8-3b78-b1fb-6697ce6073ef | -5.0452 | -45.335 | 2025-09-05 00:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 251f45aa-f37b-324e-b9bd-023aee330484 | -9.4683 | -62.3476 | 2025-09-05 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b5745ae7-1cb7-3ef9-a591-6a71f48a2876 | -7.8921 | -45.312 | 2025-09-05 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 871906d2-2c61-3909-9758-f3b79d680d3d | -5.7413 | -49.2831 | 2025-09-05 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 65996204-d039-3e6c-ab01-1cdf9544569f | -19.6838 | -54.8185 | 2025-09-05 00:00:00 | GOES-19 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 31ad6eb2-be72-38fb-84c7-ec79e25a0dab | -5.4917 | -60.138 | 2025-09-05 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| df34cef9-91e5-32e1-ac02-bb05b3804b32 | -5.5609 | -46.1765 | 2025-09-05 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d48f4933-7aa2-3ea5-b557-a926aeee04e7 | -5.0266 | -45.3362 | 2025-09-05 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 321.7 |
| a39de7e6-0ab9-3002-a2b5-7d73dd7a1f7e | -8.0223 | -45.4354 | 2025-09-05 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 52f8e2f6-c4e4-3270-85dd-d3ea03df8362 | -5.4918 | -60.1189 | 2025-09-05 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ffa88296-7216-3567-9d01-a3afc6e1e7ab | -9.2288 | -57.0906 | 2025-09-05 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b3ecb2b1-16cc-382f-a399-41f2952f2d70 | -6.5856 | -44.564 | 2025-09-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ba44e9f5-6c8c-3d78-8858-ffd167ca2c5a | -7.8923 | -45.2893 | 2025-09-05 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3f1f4e90-44a6-302f-9d4e-d09775fd84e7 | -5.5608 | -46.1988 | 2025-09-05 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 974c79f8-2796-3e39-afea-4138eee90146 | -11.6409 | -54.5315 | 2025-09-05 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| acfec7d2-b3b3-3479-98ef-737557e81d05 | -5.5892 | -45.0278 | 2025-09-05 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 66847fb4-320a-3765-8c20-535b0c56b16f | -9.2477 | -57.0697 | 2025-09-05 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 70f451be-3390-3a86-bd73-3bab964dbc33 | -15.7565 | -53.6324 | 2025-09-05 00:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 216c9d85-043d-3fcc-a753-84d6cdfb725d | -10.2373 | -50.5417 | 2025-09-05 00:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| eeb0c2ea-f16c-3dff-80dd-9e521679da1f | -23.605 | -52.8732 | 2025-09-05 00:10:00 | GOES-19 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 158.3 |
| eb11eba4-22b7-371a-8705-2f3ca5590fc7 | -23.6057 | -52.8507 | 2025-09-05 00:10:00 | GOES-19 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| ecb2f783-8cb9-37df-910f-11c68e8b7b61 | -5.6081 | -45.0038 | 2025-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0a4485d3-8190-39cb-b044-9518d697d9ca | -15.7569 | -53.6113 | 2025-09-05 00:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3a9e9ec5-3d17-373c-9002-c69387679c29 | -5.4917 | -60.138 | 2025-09-05 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2468c5dd-7a7e-3d5b-b8cf-15d57cff8f5c | -15.7565 | -53.6324 | 2025-09-05 00:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 53e2aabb-e64d-3532-bd4e-be89e56df4d4 | -14.2892 | -45.2134 | 2025-09-05 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 92fd62fd-f986-3793-8cab-ab6725bda181 | -9.4497 | -62.3485 | 2025-09-05 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0e5f5b0f-660f-3242-b3d8-be65cb6b302c | -5.7413 | -49.2831 | 2025-09-05 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6d7c2926-2d9f-34c3-915a-5852c7a2b53f | -4.3033 | -42.0474 | 2025-09-05 00:10:00 | GOES-19 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 2c24b6cf-689c-3ab3-b427-1e3530f1933c | -9.2477 | -57.0697 | 2025-09-05 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| aa390c9d-a092-32d0-9bcb-b7504066f282 | -5.5608 | -46.1988 | 2025-09-05 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c3190ee5-9e8e-307c-bed3-77ccc664e60c | -9.2102 | -57.0918 | 2025-09-05 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ea0381db-886d-3456-b384-c83508b83736 | -5.5894 | -45.0051 | 2025-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8bfba4dd-5b36-395e-ac50-a000930e0fb8 | -7.8921 | -45.312 | 2025-09-05 00:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d003f25d-d056-3385-923f-bf88a6d501b0 | -9.4683 | -62.3476 | 2025-09-05 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2c5a59e5-edb9-394d-aa95-d40da82d30d1 | -6.5856 | -44.564 | 2025-09-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| cadbd374-051b-3ed7-a285-4ee94761b6b3 | -23.584 | -52.8777 | 2025-09-05 00:10:00 | GOES-19 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| baf5ae23-d4bb-3ac0-b146-7f20f5470ad0 | -5.6079 | -45.0265 | 2025-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 255.9 |
| e4f83d7d-fb1c-34e2-9f31-379f5ba2f70c | -13.1079 | -57.1109 | 2025-09-05 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| c5d3e642-1e58-3970-abd7-f2b378559483 | -5.0266 | -45.3362 | 2025-09-05 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 43f6a31e-5026-36ee-ba61-073b6118c1f6 | -5.5892 | -45.0278 | 2025-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| ff8a03d8-bfb3-33e3-854d-8ce166bd77b3 | -5.7227 | -49.2842 | 2025-09-05 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7a583dc4-31e1-3939-b9c8-70001e5a97c4 | -5.5101 | -60.1183 | 2025-09-05 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 49cfc932-c01b-3548-884b-7bafc6f2a496 | -5.0452 | -45.335 | 2025-09-05 00:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 48ed2383-1305-3260-b4dd-379ba7cc7dbe | -5.0268 | -45.3136 | 2025-09-05 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bb98dc0b-12d8-3f18-8358-821140a8d0e9 | -5.0079 | -45.3373 | 2025-09-05 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f6bd0786-cf23-3c77-96b3-105dbbe5f12a | -5.4918 | -60.1189 | 2025-09-05 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ae643061-911b-3d83-9cab-eca6cdd8ce18 | -8.0988 | -45.3371 | 2025-09-05 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a638f609-c9a5-37ce-92ac-bb9ec161d7e3 | -9.0765 | -46.9891 | 2025-09-05 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7803581c-ed1f-3629-b7b4-5088a1690925 | -5.0264 | -45.3587 | 2025-09-05 00:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6bd3e21b-3525-3ba4-8888-247f35f82347 | -8.0799 | -45.339 | 2025-09-05 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| cc00445c-babe-305c-ab0c-e4f5761b2a97 | -5.6266 | -45.0252 | 2025-09-05 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4c65e3b7-b13f-384c-8e83-9d4b0bbcf14c | -13.1082 | -57.0908 | 2025-09-05 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| b9e89512-46b1-3602-a54c-07e958bae439 | -11.6409 | -54.5315 | 2025-09-05 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| aed9d9da-7b70-3928-9983-44e6cc5dd861 | -7.8923 | -45.2893 | 2025-09-05 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fda2da2d-3ad9-3b80-a6ac-c1c32d240406 | -9.0765 | -46.9891 | 2025-09-05 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5cfe30a2-9464-33a8-8a60-b03c47090a01 | -5.7413 | -49.2831 | 2025-09-05 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d8932f8b-25ff-3d8c-8294-7e6462307202 | -14.2892 | -45.2134 | 2025-09-05 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| c86fb2cd-0ff1-327f-8cba-839e49019282 | -9.4497 | -62.3485 | 2025-09-05 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8b9d8872-bb1b-3ac4-8813-a6ba8dbb53ef | -5.4917 | -60.138 | 2025-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3c795e94-8d60-3493-97cb-19535c9b1065 | -9.0762 | -47.0113 | 2025-09-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7e6d7c6c-7183-34de-8068-be4397f64dc5 | -5.4918 | -60.1189 | 2025-09-05 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| baa39076-0937-3616-9d17-d6c578f61bb4 | -16.3149 | -52.9415 | 2025-09-05 00:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 00790c60-f914-367c-9a57-7e5f91e50504 | -5.5892 | -45.0278 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 6349d861-a0b7-31e2-b59a-f3cf3c8211a9 | -8.0988 | -45.3371 | 2025-09-05 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5ef601a6-2a8f-33c9-8e9b-ce155278e616 | -5.7227 | -49.2842 | 2025-09-05 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3a757054-2efd-3ee2-b229-a4a1d3abbd42 | -5.6079 | -45.0265 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 3e3587a8-4a1f-3423-b20f-bddedd30b95c | -6.5856 | -44.564 | 2025-09-05 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 34cc1e96-a713-39d2-873e-ba6476a20bae | -9.7034 | -51.0591 | 2025-09-05 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ef9de1e4-4238-3017-a56a-d8d32143fc72 | -8.0799 | -45.339 | 2025-09-05 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 32035c4f-2e14-3787-8340-8b3d9b79fe1a | -11.6409 | -54.5315 | 2025-09-05 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9fa4a55b-36f2-32ce-b811-7639867758d3 | -5.5608 | -46.1988 | 2025-09-05 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 378809f3-4117-32e9-94d3-2e0ffbf42965 | -5.6081 | -45.0038 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| e8e69a65-d223-386c-9ebb-b2a583e9b0ad | -9.2102 | -57.0918 | 2025-09-05 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 06d5203b-e0d7-3459-a34d-1479ffec3255 | -13.0889 | -57.1126 | 2025-09-05 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 6893c442-af5c-3b60-b290-d545d0e967e4 | -9.2477 | -57.0697 | 2025-09-05 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1124ca20-021b-3add-ac59-93aece77d929 | -9.7031 | -51.0802 | 2025-09-05 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 362f8733-f6e4-38d1-b4b6-92f5983d3131 | -5.6266 | -45.0252 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |


[Clique aqui para ver as próximas entradas](README2.md)
