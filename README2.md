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
| 0126bce6-e3b8-39d5-9939-be867f5adcfe | -3.6032 | -50.5876 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 89851732-af0b-304d-99a5-920db65e82b9 | -3.1983 | -50.2867 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 9021c2f2-f2f5-3b1c-b807-3fff6f352fce | -2.2504 | -46.5282 | 2024-11-11 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 049223a8-abc5-3df0-ad58-5afe09f46f9d | -1.4057 | -52.3758 | 2024-11-11 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e112574c-896a-3067-880a-ea999921e764 | -17.2737 | -57.488 | 2024-11-11 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 13f8c8a9-35d5-39e2-8976-914f21b7d79d | -4.0293 | -46.9703 | 2024-11-11 00:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d8746496-4c9e-3bae-8d4e-d5b69347e310 | -3.0296 | -50.9607 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 27004419-cdaf-39f2-b062-29c93bb6cd9c | -2.9716 | -46.9907 | 2024-11-11 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6e7af4e1-8460-3f38-ac72-450c03e97d29 | -4.1101 | -49.0888 | 2024-11-11 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7071e00a-b2a5-3e28-8e52-57dae11386a5 | -2.4504 | -47.6399 | 2024-11-11 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e52bc398-61af-3b9d-8891-60341a2aa6ef | -3.2427 | -53.0722 | 2024-11-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 922564cd-4f59-3ba4-98b6-20f1c07907a4 | -2.6662 | -49.3948 | 2024-11-11 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 91aadd38-2f6d-3247-af36-c310c360c3b8 | -3.6954 | -50.6262 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 738c76b6-38ee-31ec-b19b-001756444085 | -2.8508 | -49.432 | 2024-11-11 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 2754fa22-3cdd-3348-a3e6-dc10497ba637 | -4.1285 | -49.1094 | 2024-11-11 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e31b0c9b-a80b-3d3e-8fec-08b66c8b659f | -3.048 | -50.981 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f8ea7469-903a-3fdc-94e9-c4c854115418 | -3.6789 | -50.2074 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 764a9836-5144-3931-bbb1-7031e2895c9b | -6.1325 | -44.9199 | 2024-11-11 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0de1de59-11d1-3b48-9b9e-38529b8912eb | -6.1323 | -44.9426 | 2024-11-11 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6d46549a-983b-3137-aa35-5cc59552feaa | -3.0295 | -50.9815 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| b098bbaa-43d3-3de0-a765-1e944b00f899 | -1.3402 | -47.7284 | 2024-11-11 00:10:00 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 194fa73b-17cd-34bd-850f-08db41530110 | -3.4725 | -43.4074 | 2024-11-11 00:10:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ce166b3b-1175-35cb-a4df-b1cb372418cf | -1.2201 | -53.6364 | 2024-11-11 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| dffc6e94-1381-3106-889c-939043a6079d | -17.2933 | -57.4857 | 2024-11-11 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 176.1 |
| 3e092472-7741-36bb-ac7c-8e91d4401dd1 | -3.2428 | -53.0519 | 2024-11-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f828ebaa-0bb4-3171-b905-5ea76e9ce5ed | -1.2018 | -53.6366 | 2024-11-11 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 07a0a8af-612b-3154-b822-300bc7b4dea9 | -2.8856 | -45.395 | 2024-11-11 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 0c71df61-6f84-3dbf-90ad-f61e7c4a8c84 | -1.5164 | -52.1491 | 2024-11-11 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6f9bba59-ed35-3d5d-b1de-e99c0b7d7f56 | -3.2772 | -53.6989 | 2024-11-11 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| be63b067-a136-3b61-8d5e-72ce35ee3cd8 | -3.5346 | -45.7061 | 2024-11-11 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 506b5dcf-b7b5-3dec-9095-70472a8af861 | -2.5139 | -45.4522 | 2024-11-11 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b26cf2c0-0053-306d-ac97-61643107c6a4 | -3.32 | -44.0377 | 2024-11-11 00:10:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b356f9bb-3c65-3366-87c3-75b20122437c | -3.6604 | -50.2081 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ba5c43e6-2d4e-3fbc-ac6b-f25a31eb07d2 | -2.189 | -48.3815 | 2024-11-11 00:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 9ad79c4b-b7f8-3d0c-8e3e-6756fb05cd63 | -3.4538 | -43.4083 | 2024-11-11 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d2a6235f-6b78-333f-b066-9207f28f679a | -17.6083 | -57.4482 | 2024-11-11 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| fd53a5e9-d014-3bca-a646-df856935b361 | -3.0214 | -53.2404 | 2024-11-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 18e27d26-0d4a-3499-b6e0-2ab88561ca30 | -3.2949 | -45.312 | 2024-11-11 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 54de5097-0efb-3e7a-9f06-fe1ad872ebe1 | -3.6859 | -45.2502 | 2024-11-11 00:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6f055b20-5d04-3e22-a7da-7cd6a3bcb066 | -2.2504 | -46.5061 | 2024-11-11 00:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9565cf8b-2a06-35f6-bbf7-d21e54cc6324 | -17.5889 | -57.43 | 2024-11-11 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 146df67d-1371-3836-87b0-bd6685b9e361 | -17.2936 | -57.4652 | 2024-11-11 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 7eaabdd2-eb98-3f8e-94fd-b96168d08bd0 | -3.0324 | -45.8154 | 2024-11-11 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| fc02ce38-2de3-3678-b760-5bfd1b80b438 | -3.0138 | -45.8161 | 2024-11-11 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9dbc55d1-2408-350c-befc-b5f0f2003789 | -2.9901 | -46.9901 | 2024-11-11 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| d99b2427-8fcf-3402-888c-969f9732a683 | -1.3402 | -47.7067 | 2024-11-11 00:10:00 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3afe1540-3b36-3f07-bcd6-0a3b336fb815 | -3.6218 | -50.5661 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 8b3f59bb-b818-39be-a378-16243e5b51f5 | -2.514 | -45.4298 | 2024-11-11 00:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6cef6efc-538a-3e35-8022-7aead154d6eb | -3.4537 | -43.4315 | 2024-11-11 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3ca8a1dd-0875-32ee-bfa4-689c678f163a | -4.2865 | -50.6662 | 2024-11-11 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| cd81cf46-8c77-359b-8c0c-845a72508d30 | -3.2948 | -45.3346 | 2024-11-11 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 5e1a33a6-cdea-31a4-9839-437b5b2d8ad2 | -3.1984 | -50.2657 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 267ec43f-4e41-3375-b274-7a2da81abcc4 | -3.6217 | -50.587 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 4c67dc8f-1484-3f07-a837-ed4bcad7814f | -2.8508 | -49.4108 | 2024-11-11 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 799a91f5-8d7c-3c02-9051-8b1ea6316670 | -2.4319 | -47.6404 | 2024-11-11 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2404b4db-7dbb-3f1f-ad9f-bd8772a620e5 | -3.0111 | -50.982 | 2024-11-11 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e4a3b666-dfba-3b36-97b8-c2bc0a93555c | -5.9788 | -45.3621 | 2024-11-11 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a837e5e6-c1eb-3722-9f86-12597da2cf39 | -3.8674 | -46.0486 | 2024-11-11 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3d999e77-1d15-30a7-819c-1db7eea0d65b | -3.1458 | -54.4659 | 2024-11-11 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| dcf86a2d-d062-3abe-8be6-a217e552fd63 | -2.8323 | -49.4325 | 2024-11-11 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d0a9c4d4-a2d1-3f62-99fb-b8c671c94d82 | -3.2588 | -53.6994 | 2024-11-11 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fb7d6490-ec6e-3782-961d-7a1c5e3bacf5 | -3.3836 | -50.1336 | 2024-11-11 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 07f7f194-7d5f-3d40-a536-a4762b2701b0 | -3.8672 | -46.0708 | 2024-11-11 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b0afab40-785f-31c9-b4e1-62f0bebdc922 | -2.8857 | -45.3726 | 2024-11-11 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8ef5425b-de2d-3960-ace0-91c97e999606 | -2.6662 | -49.3948 | 2024-11-11 00:20:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f81ef6d1-5cc6-3f00-8e05-4cfef9e46cbf | -2.9901 | -46.9901 | 2024-11-11 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9129dca7-9083-3c5d-a2c7-fced7449b4c4 | -17.6086 | -57.4276 | 2024-11-11 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.3 |
| f4b90554-80ec-3803-87a7-0d3963ffc5a9 | -4.0293 | -46.9703 | 2024-11-11 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5445007a-5a79-301e-8b62-49971f391c07 | -3.2949 | -45.312 | 2024-11-11 00:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 58736d09-5a9b-30f0-9028-9ed08ce2bf9f | -3.5347 | -45.6837 | 2024-11-11 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 287a2582-1d54-34bb-bf73-50d1ca8e898b | -1.2018 | -53.6164 | 2024-11-11 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b17c38be-f71b-3d8f-a1b2-53077b731a8c | -3.0324 | -45.8154 | 2024-11-11 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 479aeaae-3901-33b6-86a5-0e41139d3991 | -3.2603 | -48.7582 | 2024-11-11 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 44a6ca7b-52ec-3b86-b0d7-a0c8cb810e24 | -3.0845 | -51.0631 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cbacf6f6-9efd-3c71-b89e-79114b6547f4 | -2.8692 | -49.4314 | 2024-11-11 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1a629253-0853-3093-bd82-bf8f73a8eeea | -1.4057 | -52.3758 | 2024-11-11 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 847213f5-05c7-3376-b93d-7c79c4ccbb7b | -4.1246 | -43.5833 | 2024-11-11 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| e8e258bc-b071-3b5d-8ee5-2a82003c6ea4 | -15.9791 | -59.3468 | 2024-11-11 00:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 492f5112-8170-3e4f-a4dd-71e2595ed81a | -5.8216 | -44.1196 | 2024-11-11 00:20:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3d015e7a-86f0-365e-97c0-7873a0a7355e | -3.2948 | -45.3346 | 2024-11-11 00:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 59e1205d-f043-3c1a-88a7-c6e57cf36bd9 | -3.1423 | -50.4352 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0f1e873a-a99b-34a6-af2a-7eafd93cad0c | -2.1891 | -48.36 | 2024-11-11 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a07242c4-bb51-3620-ad22-5930c8292aeb | -3.2774 | -53.6585 | 2024-11-11 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| db652a0d-4009-3fe2-84f6-da030f1a6c5d | -3.2428 | -53.0519 | 2024-11-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e443965d-3e3e-3ab1-80ba-4777a32beab1 | -17.313 | -57.4834 | 2024-11-11 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 6ec18e59-2e23-3922-83ca-c75924e94c82 | -3.2588 | -53.6994 | 2024-11-11 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9fdbd045-132a-3727-94ab-1d3a247d3066 | -2.2075 | -48.3811 | 2024-11-11 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 57132c7e-2c83-3da0-9fa1-ebc3b0bda761 | -4.0294 | -46.9484 | 2024-11-11 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5d42bbf3-ae6c-362e-b813-13b796ab9d53 | -7.41864 | -39.75857 | 2024-11-11 00:20:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e335afe5-5b2d-31b3-a2bb-5112ce7ac017 | -3.0844 | -51.0839 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1ab8149f-194a-33c9-a965-d8015270ec1d | -15.9982 | -59.3649 | 2024-11-11 00:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 03bbc8dd-2da5-30fb-83af-992fb897cb81 | -4.1101 | -49.0888 | 2024-11-11 00:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 31790472-c476-32f9-9f75-d06c44bcdba8 | -3.6789 | -50.2074 | 2024-11-11 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5f572265-2cb9-3eff-bfde-5730f90589fe | -3.0111 | -50.982 | 2024-11-11 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9216e060-cdd7-30b9-bbc6-790d10cdefb5 | -1.2201 | -53.6364 | 2024-11-11 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 78a04fbb-74f7-3d83-bcd9-ca76f881cc19 | -15.9985 | -59.3449 | 2024-11-11 00:20:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 3c4a9d77-fcc8-3157-8254-16dc97707c1c | -17.5889 | -57.43 | 2024-11-11 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 652d6627-aa02-32fb-92b0-668f9facc5b7 | -3.4538 | -43.4083 | 2024-11-11 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 3fd5c28c-a156-3208-afb8-f2598dd6c0e7 | -3.2773 | -53.6787 | 2024-11-11 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e6949ddf-b01d-39bf-ad44-176ea11263e1 | -2.8508 | -49.4108 | 2024-11-11 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |


[Clique aqui para ver as próximas entradas](README3.md)
