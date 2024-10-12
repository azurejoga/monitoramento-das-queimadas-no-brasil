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
| 80b4193f-8069-327d-ae89-f02dccf45be5 | -2.7885 | -51.3618 | 2024-10-12 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| dca46793-5f11-3761-9be4-6f67a6f38029 | -2.8611 | -51.6699 | 2024-10-12 00:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 23716706-dee8-3340-af5e-192455f2af9a | -2.8795 | -51.6695 | 2024-10-12 00:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 00b4f2dc-c267-32c6-aef4-e0a72a5c9368 | -3.0311 | -50.5642 | 2024-10-12 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 65b3206b-d759-373a-baf3-4fea68b8a5ac | -3.1426 | -50.3724 | 2024-10-12 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5cc61b82-eec5-3112-8c0b-aa2c36804a84 | -3.1427 | -50.3514 | 2024-10-12 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 291702e2-e600-3d98-832d-390516b29fae | -3.161 | -50.3718 | 2024-10-12 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| d22ad583-5879-33a3-8fe6-8efbe4a76d1c | -3.1611 | -50.3508 | 2024-10-12 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 6e9b8e8b-295e-36f8-b40d-0f7416b52fc5 | -3.2136 | -46.7843 | 2024-10-12 00:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 11131734-b657-3d2d-a3a9-e564a5d0805a | -3.6979 | -50.1015 | 2024-10-12 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 1429b759-da3b-3708-9bd1-14cc4bc35538 | -3.7163 | -50.1219 | 2024-10-12 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 90e5a632-f8e8-37fe-ac3d-ab31b5ea325d | -3.7164 | -50.1008 | 2024-10-12 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f88e79c0-6777-346a-84b7-797ddec607d4 | -3.5849 | -50.5673 | 2024-10-12 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 12fd086a-51a4-38df-9a8c-6651769a6214 | -3.6978 | -50.1225 | 2024-10-12 00:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 3e7cb402-10ae-39f4-a09e-700510290708 | -3.7844 | -51.3312 | 2024-10-12 00:15:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cd52d92a-e663-397f-9338-df1cd71d17bd | -3.7845 | -51.3104 | 2024-10-12 00:15:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5b6eb550-e814-31ef-9b80-3cb4d68016dc | -4.0062 | -60.3869 | 2024-10-12 00:15:29 | GOES-16 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fe889701-4a27-3239-890b-b23869d0335b | -4.1148 | -48.2515 | 2024-10-12 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 6872d7c9-1489-38ca-b00b-8863d982f966 | -4.2665 | -50.9594 | 2024-10-12 00:15:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 929f2e38-1ab8-325d-9151-0cd9d3bf1727 | -4.3782 | -50.8087 | 2024-10-12 00:15:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 85a64cb1-f867-3d15-affd-901fe8fd562d | -4.5957 | -45.6315 | 2024-10-12 00:15:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 6681daba-6593-31ad-8b4b-6ac01c90161d | -4.7188 | -60.8072 | 2024-10-12 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8cb05fbd-8993-3561-86da-199657b4714e | -4.7188 | -60.7882 | 2024-10-12 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 718d502d-2e82-3d53-b938-a1464e92f5e4 | -4.7189 | -60.7692 | 2024-10-12 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 48a9e603-493f-33d7-9c34-b6ca2f43a89d | -4.7371 | -60.7877 | 2024-10-12 00:15:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c7a161d6-06e9-36f5-ad10-d570204ab690 | -5.5547 | -44.689 | 2024-10-12 00:15:38 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5eb70171-2dbb-33b9-80b4-006405364bca | -6.0791 | -44.6276 | 2024-10-12 00:15:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ae973c14-9d5f-3422-8f58-96efae1f9c12 | -8.214 | -61.1831 | 2024-10-12 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b61fe23f-625f-3a91-8e7d-a7a63235a0f2 | -8.2324 | -61.2014 | 2024-10-12 00:15:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| ec2952d7-64c0-3233-9fbe-194d5d42e118 | -8.2325 | -61.1823 | 2024-10-12 00:15:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 458f4b99-8a9e-38bf-a71b-d85766ea6c1e | -8.9667 | -62.3506 | 2024-10-12 00:15:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 80242490-7411-3e42-9d36-48b4040d8a16 | -9.5687 | -64.1983 | 2024-10-12 00:16:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bb3546c9-4e0d-357e-97f4-060dd9bbf74b | -9.6594 | -56.9635 | 2024-10-12 00:16:01 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 47ca8e57-3ded-33f3-8689-26cfdb3c92af | -9.8554 | -60.2772 | 2024-10-12 00:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5e77e77c-6f15-3450-9d0f-238660aea1bc | -9.9243 | -63.8256 | 2024-10-12 00:16:03 | GOES-16 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| e9459d7d-6a03-39f0-8377-6f8f9910f237 | -10.8398 | -44.4365 | 2024-10-12 00:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a039aa45-3e3d-321b-aa99-e26fd92e9321 | -10.6535 | -58.7698 | 2024-10-12 00:16:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 59212009-e82e-3310-a768-1905ffee4091 | -10.9506 | -44.653 | 2024-10-12 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e2f471e9-8864-3f28-bc59-682970480c63 | -11.2289 | -51.3091 | 2024-10-12 00:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4e136c8d-2d75-331d-9ccb-8f6bb00fcef0 | -11.2761 | -60.5038 | 2024-10-12 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ca433793-d9eb-3073-b74f-f77c46e65510 | -11.2763 | -60.4844 | 2024-10-12 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0be923c0-089e-32b0-af47-032f771a3617 | -11.8188 | -58.8459 | 2024-10-12 00:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 33cf77f1-3808-3fda-94e6-a782005a737b | -11.8375 | -58.8642 | 2024-10-12 00:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d909003d-7cd7-3768-b02e-109e305b32e5 | -11.8377 | -58.8445 | 2024-10-12 00:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 34b5681d-fb82-3514-b207-a455041b0b5f | -11.8379 | -58.8248 | 2024-10-12 00:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 8c3a0f3c-3781-389c-ab6e-0bcd63e474f5 | -12.7793 | -43.3114 | 2024-10-12 00:16:18 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 6e5451a0-b24a-348c-a680-ce3ffd220380 | -12.7678 | -44.8671 | 2024-10-12 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 30490a13-8159-3beb-b49b-8907d16d99cf | -12.7871 | -44.8639 | 2024-10-12 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 328.7 |
| 0c275bc1-b351-3916-9be2-c37cb21e9063 | -12.7875 | -44.8406 | 2024-10-12 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 269.1 |
| d491cd4a-8101-35b7-b92e-0050aa0ad7b0 | -12.8064 | -44.8608 | 2024-10-12 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 46a73118-fc2a-32f0-a96d-deece640b6e7 | -12.8069 | -44.8375 | 2024-10-12 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 5ac292e8-323d-3b90-9b2b-cec6ee4fcbaa | -12.6184 | -55.2144 | 2024-10-12 00:16:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 324cdc3e-ce17-3a49-89ff-ca186442f545 | -15.0524 | -45.073 | 2024-10-12 00:16:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b3599538-e597-3b25-a0e5-d3c0b4af1c04 | -15.6225 | -59.9784 | 2024-10-12 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 02c69281-042a-3427-9e44-493c063edfe7 | -15.6228 | -59.9585 | 2024-10-12 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 1451f1c1-b897-33eb-a90d-ca29c35992e9 | -16.9609 | -57.4426 | 2024-10-12 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 03912e39-78b6-3cbb-bab4-17b419d163f0 | -16.9802 | -57.4609 | 2024-10-12 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 9aa1ac75-d314-3212-b170-e21f1afff286 | -16.9805 | -57.4404 | 2024-10-12 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 171.8 |
| b47e25cf-aa1c-3719-b8c9-e55036d98ef4 | -16.9998 | -57.4586 | 2024-10-12 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 031e42e7-b333-338b-964c-a441da9f8a7d | -17.0426 | -56.0333 | 2024-10-12 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| cad35780-812d-3244-abe8-84df83559ac0 | -17.1761 | -57.4585 | 2024-10-12 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| b8961a24-e321-3e01-89af-9ada8ac42e3f | -17.1764 | -57.438 | 2024-10-12 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| ffca6a8d-967c-3053-b719-ee086e5bf9db | -17.627 | -56.3318 | 2024-10-12 00:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.5 |
| 9997e7d7-091a-30ac-9fd5-bae21549a79b | -17.6273 | -56.311 | 2024-10-12 00:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 4a8e1706-4ca2-3590-b462-1d2d7afbe3e3 | -17.6467 | -56.3292 | 2024-10-12 00:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.1 |
| 8f49232e-c14d-363e-aef3-3d99e5dbd42c | -17.6471 | -56.3084 | 2024-10-12 00:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| af496d3d-01d1-32c0-bf69-7cd43188ec90 | -17.6675 | -56.2643 | 2024-10-12 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.2 |
| db9b16e3-c1d7-3354-ad37-d68504562238 | -17.6679 | -56.2435 | 2024-10-12 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 4a8c0658-940f-3272-948b-3088555e90f9 | -17.964 | -57.3843 | 2024-10-12 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 450ef70e-2627-3a68-bb30-f528e001e0e6 | -17.9837 | -57.3819 | 2024-10-12 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 573b9375-951e-3273-9659-8057c4dc6a08 | -17.9841 | -57.3612 | 2024-10-12 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 21617f78-c934-34b1-a25e-d1c300567343 | -18.0793 | -56.4182 | 2024-10-12 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 73efc5d5-c76f-3489-b068-096f939cad07 | -18.024401 | -42.855 | 2024-10-12 00:21:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0d2201e-6907-3629-8c01-96b7fdcaa6b2 | -18.014601 | -42.857399 | 2024-10-12 00:21:01 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ab4ad75-af0c-3fcf-9f70-76facf53cfb2 | -17.5485 | -42.291302 | 2024-10-12 00:21:06 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac16feb4-be7a-3f18-a38a-6e688a733fa0 | -17.5501 | -42.298599 | 2024-10-12 00:21:06 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2384c34e-bd01-3142-9585-552c40f8314d | -15.8348 | -42.149101 | 2024-10-12 00:21:33 | METOP-B | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b5be343-c876-3cc7-8cbf-7549c02a2f19 | -16.135201 | -43.626598 | 2024-10-12 00:21:34 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a9fcfe83-f396-390c-8911-c13c6cac5e5a | -15.2725 | -40.310299 | 2024-10-12 00:21:35 | METOP-B | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 422d90b4-f76f-3531-b67f-82a253837fb3 | -15.2745 | -40.319 | 2024-10-12 00:21:35 | METOP-B | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb2057d9-92b9-3cfc-a3c3-4ef0ebfc5f50 | -15.2766 | -40.327801 | 2024-10-12 00:21:35 | METOP-B | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab16768e-8980-3ec4-a6e0-0f96a14a8fda | -15.6085 | -42.560299 | 2024-10-12 00:21:38 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0354eb42-4003-3377-8880-0c59fbdf64d4 | -15.0186 | -41.251701 | 2024-10-12 00:21:43 | METOP-B | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7512d0af-818b-362b-9a39-df43950363ed | -14.7149 | -40.356998 | 2024-10-12 00:21:45 | METOP-B | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7469bd10-3422-3e3e-84df-8a06644453c9 | -14.2274 | -39.745602 | 2024-10-12 00:21:50 | METOP-B | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91baf0b5-5732-3f47-b817-270b94b374b0 | -14.2297 | -39.755299 | 2024-10-12 00:21:50 | METOP-B | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4517564f-5f14-3f01-afcb-d22a4ae2a2c3 | -14.7745 | -42.295502 | 2024-10-12 00:21:51 | METOP-B | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7702640f-114b-3ca3-b758-e5e344564888 | -14.7762 | -42.303001 | 2024-10-12 00:21:51 | METOP-B | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 23d852a3-073c-39d2-bec2-39547095289f | -14.7779 | -42.310398 | 2024-10-12 00:21:51 | METOP-B | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4bafe029-deae-31d0-b379-7a6821f8e915 | -15.0595 | -45.061001 | 2024-10-12 00:21:56 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb28a022-40eb-3548-bcd4-c18b12e99848 | -15.061 | -45.068298 | 2024-10-12 00:21:56 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e88d6d24-235c-347d-a3f9-5abb931a9755 | -15.0626 | -45.0755 | 2024-10-12 00:21:56 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 098f072d-8bc0-3ddc-a8c4-b95897d29c62 | -14.404 | -42.345402 | 2024-10-12 00:21:57 | METOP-B | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 45d2b71f-f649-38e8-b907-a686cde7daa0 | -14.4057 | -42.352798 | 2024-10-12 00:21:57 | METOP-B | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c2eef72b-66c5-3866-bf3d-2956291cce74 | -14.3668 | -43.5938 | 2024-10-12 00:22:02 | METOP-B | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c36df33d-3b41-3de7-a938-1573ac2e3503 | -14.3684 | -43.600899 | 2024-10-12 00:22:02 | METOP-B | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77ca071c-affa-3861-b912-eef4b22e1951 | -13.9272 | -42.381199 | 2024-10-12 00:22:05 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dd22e704-122e-367c-a105-a2350c4558be | -13.9289 | -42.388599 | 2024-10-12 00:22:05 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bbe92bd0-6ce4-3419-a908-5ab77d2b0f0d | -13.4736 | -40.832401 | 2024-10-12 00:22:06 | METOP-B | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e6fada88-e693-3a2d-babd-fdc3933ca10a | -13.4756 | -40.841099 | 2024-10-12 00:22:06 | METOP-B | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
