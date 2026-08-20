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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2156aaba-1311-309a-ad84-9018cefca5aa | -23.0838 | -49.1511 | 2026-08-20 01:10:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 5891dd99-d063-3a18-ad27-5e79494f1e0e | -9.12 | -61.6011 | 2026-08-20 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 9705a169-f8cd-39b7-a406-7d1cec444998 | -6.5829 | -58.9851 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ba04650a-37a6-3f80-bb4e-7a78863debc6 | -11.8377 | -58.8445 | 2026-08-20 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 54aa38bf-e705-3f71-904d-c5b11c8860fc | -14.4559 | -45.6019 | 2026-08-20 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| faa1af97-2c88-37a7-9b46-26f9e28b3afe | -1.8425 | -54.4917 | 2026-08-20 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c47cd7fb-64af-39ae-a46c-538502f4f0ae | -9.4069 | -60.4362 | 2026-08-20 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c2342047-5e3c-372e-b4c0-0e46efb38bcd | -6.6929 | -59.0966 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 51cd78e5-ef6d-3fb4-81de-2fe40c1a3cce | -9.4256 | -60.4353 | 2026-08-20 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 3714d0d7-9ba9-3744-97d3-dd72e760df10 | -14.4554 | -45.6251 | 2026-08-20 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 53849588-4dba-325a-97b6-1d1ab4809cd0 | -10.3274 | -57.5715 | 2026-08-20 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d6706c54-f1c7-3b51-99e3-5ef60069721c | -9.4257 | -60.416 | 2026-08-20 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 52d7123f-e434-3180-b009-4c3530272b2c | -7.36 | -45.8361 | 2026-08-20 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 288.7 |
| b9c82b53-589e-3862-9140-de1d59f361a2 | -8.6729 | -54.629 | 2026-08-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3cc1a546-59a9-300d-bdc5-efe0b84c7a98 | -6.4389 | -52.7548 | 2026-08-20 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 80a35083-eb9c-35d3-9a47-33229aeffdf7 | -9.4254 | -60.4545 | 2026-08-20 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 72745384-bd10-3d39-bc88-a98c3d0ddaec | -7.37 | -45.85 | 2026-08-20 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc6909af-0112-3274-aec2-ed644d00a6b8 | -7.34 | -45.85 | 2026-08-20 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b77acc7-8724-335f-8def-056b6140861a | -7.34 | -45.8 | 2026-08-20 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50815a73-f5de-32ec-8865-85dc6aef3027 | -7.37 | -45.8 | 2026-08-20 01:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9037fd1-f49d-36f6-8e14-25c392b48921 | -7.3415 | -45.8152 | 2026-08-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 0f0e1a47-5e9b-3f98-9cde-874f5188c0f9 | -9.4257 | -60.416 | 2026-08-20 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 67098f9b-e44c-3cba-b87d-4cdc0fa16796 | -1.8242 | -54.492 | 2026-08-20 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c6160a14-c8cf-3c7f-8b35-10fe01bc0caa | -11.8375 | -58.8642 | 2026-08-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| db6c38b4-443c-3b63-ba6a-7e60957812d0 | -23.0831 | -49.1746 | 2026-08-20 01:20:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 89.6 |
| dcc651a5-3ded-3765-acbf-71dcad72b615 | -6.6929 | -59.0966 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| c8741e8a-48a8-3a4b-947d-1eca630e2e3d | -6.6015 | -58.9651 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 17aa5801-96b1-33a9-a8af-cfe3f42c3443 | -7.3413 | -45.8377 | 2026-08-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 4058209f-cc46-3231-88d8-bca69e49e49c | -9.2256 | -59.7894 | 2026-08-20 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9dc111e1-31bd-3b51-b7c4-e56f8e1de5e9 | -9.2258 | -59.77 | 2026-08-20 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 39644a66-c9e4-31c1-b132-d0dd408a6ded | -6.6938 | -58.942 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e22c1079-2fa2-36ac-941f-6e3f78d8a7db | -6.4391 | -52.7343 | 2026-08-20 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3eac6754-8fb6-35af-9bc6-6e88b3626981 | -2.5629 | -47.2445 | 2026-08-20 01:20:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 42917a10-fb6c-3af5-a6ac-6b43d0250383 | -6.5829 | -58.9851 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 70c514f1-8619-38cf-b906-81f922313098 | -11.8188 | -58.8459 | 2026-08-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a2fc0cc5-80f6-3260-89d2-2b71cd79aa7d | -7.3603 | -45.8136 | 2026-08-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 316.6 |
| 341b7480-4743-3a1b-b76f-bdf4cf9eb61a | -7.9751 | -44.6648 | 2026-08-20 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 889d1f9d-f8b1-3428-8899-318c7a9ae429 | -14.4559 | -45.6019 | 2026-08-20 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f40a0ca6-5b17-37d3-847c-3d35f96807cb | -11.2189 | -55.0585 | 2026-08-20 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 89c8304b-8c08-336a-94ca-7fc9e12f9852 | -11.1939 | -53.9993 | 2026-08-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 67864a9e-d433-36d5-8da5-b06a50ca1565 | -9.12 | -61.6011 | 2026-08-20 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 49a008f5-1b7f-368f-91ac-6fe7a1ed804b | -11.8379 | -58.8248 | 2026-08-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6b515de5-2a22-3ae3-9df6-80595df45383 | -17.3365 | -43.6383 | 2026-08-20 01:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3d68945b-403c-3081-aa3b-f1089a245873 | -9.207 | -59.7903 | 2026-08-20 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 18e3342b-2361-3c57-86f2-d8ff89b71191 | -9.4256 | -60.4353 | 2026-08-20 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 1daa4fd2-5072-308b-97d6-54863c7d2ebf | -8.654 | -54.6505 | 2026-08-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1e89fb2f-ee6e-3014-9205-2747b8b86eb3 | -8.6727 | -54.6492 | 2026-08-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| f8f7a36a-0954-3bda-ada0-697a18872c1a | -1.8425 | -54.4917 | 2026-08-20 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0f1b2a8c-5190-30d4-8018-f57609b07527 | -11.1936 | -54.0199 | 2026-08-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 306dbc67-acb4-3e21-8b33-f844861625f0 | -12.4914 | -54.7569 | 2026-08-20 01:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 5165d138-26c0-3564-ad33-0eae83804961 | -9.2071 | -59.771 | 2026-08-20 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ffcd6895-389e-39e2-acd8-79380e5172d7 | -9.4254 | -60.4545 | 2026-08-20 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 4378e9b3-335a-3052-b746-01c3fd43a468 | -23.0838 | -49.1511 | 2026-08-20 01:20:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 93b4e574-5186-3ea9-9749-7169ae062482 | -6.583 | -58.9658 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 72cf92de-f73a-34cd-989d-5b0df8db6a26 | -7.36 | -45.8361 | 2026-08-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 29223b5c-b971-319b-9bef-9e1360adfd1b | -17.3372 | -43.6139 | 2026-08-20 01:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 604029be-d5e6-3578-8708-38146ec6c357 | -6.3863 | -54.9451 | 2026-08-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 569c2439-46de-3e2b-b55b-071e856e9c7d | -6.7114 | -59.0958 | 2026-08-20 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2ed9ca5f-9f63-31ae-84cf-ef99b74ac8a2 | -12.4916 | -54.7364 | 2026-08-20 01:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 93274354-fd5f-399d-a59a-3bdddd60aad9 | -11.8377 | -58.8445 | 2026-08-20 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 196.7 |
| f3ece594-be05-33c5-9aa4-7998c8528a08 | -11.8083 | -44.8072 | 2026-08-20 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 43fdc209-8f1f-34ff-a808-91f8f0d4e1ec | -6.4389 | -52.7548 | 2026-08-20 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 36661e88-156b-318b-bd72-b781c621222e | -8.6729 | -54.629 | 2026-08-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 9f234764-a39d-33ad-8590-42e0099f1497 | -8.6727 | -54.6492 | 2026-08-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| f97a09fb-2ce5-3ae1-b824-9153e55bcbe9 | -6.6938 | -58.942 | 2026-08-20 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 1b35016a-6290-30c7-9f4f-ffd6f95e018d | -17.3372 | -43.6139 | 2026-08-20 01:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 29780ded-3117-373f-aaeb-2497a331c728 | -6.4389 | -52.7548 | 2026-08-20 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 658e9f10-55f7-3032-8c13-bad5dc121a5a | -9.4257 | -60.416 | 2026-08-20 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| bd1cd70f-07cc-3464-b98d-197208a1a601 | -17.3365 | -43.6383 | 2026-08-20 01:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 04305974-4d1c-3e4e-b1f1-d66407f29e20 | -9.2071 | -59.771 | 2026-08-20 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| a13122c7-bb69-352d-acfb-c99394456ae5 | -11.8083 | -44.8072 | 2026-08-20 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 06fc9418-5382-33b8-9fc5-44e5896991cc | -7.3415 | -45.8152 | 2026-08-20 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| d4d82046-e604-37b5-9363-8eb5a3905819 | -11.1936 | -54.0199 | 2026-08-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d7db9b28-0bb9-3d07-a55a-f5e4cd9fe09c | -6.6015 | -58.9651 | 2026-08-20 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f39174bb-bb94-3351-8679-241f9f9d795f | -7.9751 | -44.6648 | 2026-08-20 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8e927ef3-724c-38f5-ba6d-0027341b2486 | -6.5829 | -58.9851 | 2026-08-20 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0140f367-c51e-3607-b605-c8a970478e2f | -6.7114 | -59.0958 | 2026-08-20 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 812885ea-9211-394b-9670-d5e47a089574 | -7.3413 | -45.8377 | 2026-08-20 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 6051385e-5e7d-35e4-be99-f2d94d973a5e | -7.3603 | -45.8136 | 2026-08-20 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 254.0 |
| d215359c-6fd0-3bdc-b869-7c1a14d596b7 | -9.207 | -59.7903 | 2026-08-20 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ff7a2812-aeb7-3f31-bb1d-a12c982db2f9 | -9.2258 | -59.77 | 2026-08-20 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 32bf857f-6b4a-3d11-9c4d-b149721903af | -9.4069 | -60.4362 | 2026-08-20 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8b4a30be-1af8-3e1f-9296-3d7e7ddd762e | -11.8377 | -58.8445 | 2026-08-20 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 61cad37f-0d0b-38b7-895b-c8e1983c4778 | -11.1939 | -53.9993 | 2026-08-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 27a43f52-b0b4-38a7-a1ee-956fdb9c6e89 | -9.4256 | -60.4353 | 2026-08-20 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 08bf56fd-5c5e-3160-b2e4-a35a007112ae | -6.4391 | -52.7343 | 2026-08-20 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 684142da-afe8-3e9d-9f10-df824eff6921 | -6.3863 | -54.9451 | 2026-08-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 551eca57-6db5-35d7-aeec-9cd7a8b9fc27 | -7.36 | -45.8361 | 2026-08-20 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 27f359bd-8fe5-3a04-b5ce-96e49b865942 | -9.12 | -61.6011 | 2026-08-20 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d575c1ec-44a2-3f9f-ad14-f91a844a99d0 | -11.2189 | -55.0585 | 2026-08-20 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b2efe070-c4bd-3d68-abbe-599edaf8bfe8 | -8.654 | -54.6505 | 2026-08-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8670f9d8-0f11-361b-8c72-4eaab7d46227 | -6.583 | -58.9658 | 2026-08-20 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f1d3ca54-1433-352d-af22-735686c2044c | -11.8379 | -58.8248 | 2026-08-20 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1c7bb012-faef-3dd0-aed1-546691928f4c | -23.0838 | -49.1511 | 2026-08-20 01:40:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 67678312-d0b0-35ea-8f89-a84af3accd73 | -2.5629 | -47.2445 | 2026-08-20 01:40:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e8dd34d0-74cd-36cd-a552-2baeb197916a | -7.9751 | -44.6648 | 2026-08-20 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e054b051-f2b1-3833-a6f0-fe7f807c10b2 | -7.3415 | -45.8152 | 2026-08-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 2184a661-f515-3564-9060-e3c4901799a8 | -9.207 | -59.7903 | 2026-08-20 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d770e327-651f-3b4d-98d2-9d9890f33dec | -6.7114 | -59.0958 | 2026-08-20 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fbd47d7a-e865-37b9-8aba-346d840fc44c | -9.4257 | -60.416 | 2026-08-20 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README19.md)
