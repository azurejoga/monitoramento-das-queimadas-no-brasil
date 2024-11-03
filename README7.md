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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 028de171-8b0b-32ea-aa4d-c7a8a0131569 | -2.7361 | -54.445702 | 2024-11-03 00:26:16 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b7b1dd-8646-33b2-b977-ba98b1d7b21e | -1.8737 | -52.102798 | 2024-11-03 00:26:22 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06007cb1-f34f-381d-8545-f0a7ea8709ce | -1.8779 | -52.121498 | 2024-11-03 00:26:22 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 568931c9-e623-3f02-9d5d-73b1716508a5 | -1.8682 | -52.1236 | 2024-11-03 00:26:22 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9642fb-b9b8-3a8d-8339-6075d9603c72 | -2.1604 | -53.641499 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46444e8f-cbbc-3dec-97f5-974fbb1bcc72 | -2.1658 | -53.665699 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b1a731-3a8f-3e47-9647-ed7b1f913094 | -2.1713 | -53.689999 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 308e0173-f2e7-35d8-9faa-56ec7fcfa61a | -2.1508 | -53.6436 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb2cc473-26df-34a2-9c81-ce81c907b50e | -2.1562 | -53.667801 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e29c87a-1e5f-325c-91ac-342073c48431 | -2.1617 | -53.692101 | 2024-11-03 00:26:23 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7274c46-b1a4-3d4b-b40d-624470b5ee2f | -0.6268 | -47.667198 | 2024-11-03 00:26:26 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb2c0ee-0240-3c0a-9237-38eef2bfb91a | -0.6289 | -47.6763 | 2024-11-03 00:26:26 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d08fc86-ccaf-3752-b099-e419470e969c | -0.631 | -47.685398 | 2024-11-03 00:26:26 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bda40e4b-964d-3cf9-b2e3-d9f5ad2aa21e | -1.564 | -52.131599 | 2024-11-03 00:26:27 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97476493-7a0b-3bfc-9db7-bee917fab5c7 | -1.5682 | -52.150101 | 2024-11-03 00:26:27 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 363716bd-c525-3381-b1cb-ee3dabc32db9 | -1.5543 | -52.133701 | 2024-11-03 00:26:27 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de7a8ea7-f6e6-3f21-8444-5e259748ec5f | -1.5585 | -52.152199 | 2024-11-03 00:26:27 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea22a7c-141a-3806-94f9-db1c1703a14b | -1.8549 | -54.666302 | 2024-11-03 00:26:32 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fde6e3d7-8801-3433-9ac5-ed424b110b25 | -1.2612 | -53.3507 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d11e0e-c28f-3495-9128-09cb8f135cf8 | -1.2663 | -53.373001 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99ad582c-ef1e-3f83-8471-dfbd14882a7d | -1.2714 | -53.3955 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728e7ff0-b79b-37a9-9af2-aae5c58917da | -1.2515 | -53.352798 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0dc5dfc-58c9-3741-b959-6c1638143825 | -1.2566 | -53.375198 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11d7ee5-4535-31be-adf8-e548cc6f4ff9 | -1.2617 | -53.397598 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9738782c-2a4c-3a7a-915b-cbb63cd1404b | -1.2469 | -53.3773 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5caed2c3-4346-3f16-8105-c4feaed02aed | -1.252 | -53.399799 | 2024-11-03 00:26:37 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6994b449-ed69-3624-8500-a13a99f307f9 | 0.0253 | -49.528999 | 2024-11-03 00:26:43 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faeb82f3-457d-3661-a219-6d6a15a5d2e6 | 0.0226 | -49.5406 | 2024-11-03 00:26:43 | METOP-C | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b377f7f1-a5d2-32fe-ab9f-439005b016d1 | -1.2572 | -53.3938 | 2024-11-03 00:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| bcdd9f0b-f077-3a97-ac8e-11fd29b8758f | -1.2755 | -53.4138 | 2024-11-03 00:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 945ecfad-2dbd-3d40-aff3-8e64bd56633b | -1.2755 | -53.3936 | 2024-11-03 00:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 6a1fd628-d219-32da-be1e-2b39e1dab078 | -1.2756 | -53.3734 | 2024-11-03 00:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 5444db75-d508-38b6-aec3-5373bbc4f226 | -1.284 | -48.1401 | 2024-11-03 00:35:13 | GOES-16 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 157029b4-94ab-38f2-a182-3096285174ae | -2.1746 | -53.6834 | 2024-11-03 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 31bf877e-8bea-380a-917d-40b0e48f2b52 | -2.193 | -53.6831 | 2024-11-03 00:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b297cf42-cfed-3305-a5a0-a5ea8158974b | -2.2802 | -48.8082 | 2024-11-03 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 99f21d27-60c1-37e7-9c16-865fc018b934 | -2.2802 | -48.7868 | 2024-11-03 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 85675e0e-ddb9-3ab8-9725-15edfe00c36b | -2.2986 | -48.8078 | 2024-11-03 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 328.9 |
| eb6ebe73-4ed3-3252-857a-7b90e70e8da8 | -2.2987 | -48.7864 | 2024-11-03 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 23095f4d-6b4b-3a2a-84ce-6594df65d87b | -2.5797 | -53.3724 | 2024-11-03 00:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9a070a8b-6579-32c3-b2a4-7474e7060e5c | -2.6321 | -48.5849 | 2024-11-03 00:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1bf760e1-5a5d-371e-b237-549d443ccbc2 | -2.6322 | -48.5634 | 2024-11-03 00:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b6403d9f-2e06-319a-9e43-47b904ad078a | -2.6506 | -48.5844 | 2024-11-03 00:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 62ea1e5c-acce-379a-89a2-accb9b13ab20 | -2.6507 | -48.5629 | 2024-11-03 00:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1ad1c4b2-777b-3ff6-83ef-b1d1db0af7f2 | -2.7218 | -49.3295 | 2024-11-03 00:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| a56d9e5c-6216-38f1-be76-badd46bcc001 | -2.7419 | -54.4353 | 2024-11-03 00:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 252.5 |
| 06553c6c-bfa0-3bd0-8152-9e95eb1b4419 | -2.7419 | -54.4153 | 2024-11-03 00:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 9f91856f-9b4b-3c50-bf0c-658452eb96e7 | -2.7602 | -54.4349 | 2024-11-03 00:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| bbd5b4f9-f009-38f7-bcb3-8e5688897add | -2.7603 | -54.4149 | 2024-11-03 00:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 944f5a3c-e744-37a8-9753-ea56b80b0433 | -2.7876 | -51.6099 | 2024-11-03 00:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 5b744ed1-0c01-37c2-9b00-e071d5a8eff3 | -3.0732 | -45.0275 | 2024-11-03 00:35:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f8f0a25b-c3a2-3e92-9b72-a857e3862a03 | -3.055 | -54.1675 | 2024-11-03 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 65cf000e-08c0-353c-81e3-d0a517a6260c | -3.055 | -54.1474 | 2024-11-03 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 6608f061-f873-3aed-b216-4f64a1ea9696 | -3.2415 | -53.3967 | 2024-11-03 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 125a2785-9189-3000-aa2f-75aa6377c3e2 | -3.0734 | -54.167 | 2024-11-03 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| bfce2697-1d55-3f96-9b7b-3f18f9dbd0c7 | -3.0734 | -54.147 | 2024-11-03 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| d328d41a-5f8a-330c-890f-b08f7d98bac6 | -3.0918 | -54.1465 | 2024-11-03 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 954214d9-7b60-356a-9af2-a40fbe7668b9 | -3.1212 | -51.1244 | 2024-11-03 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c7ea0280-cf54-3f82-b513-d71741cfb3fb | -3.1213 | -51.1036 | 2024-11-03 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9e7b1e62-7123-368b-af06-5738473b62d7 | -3.1282 | -54.2459 | 2024-11-03 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a5bf06cd-2fac-35c5-b190-1485cc1f8db2 | -3.2231 | -53.3972 | 2024-11-03 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7807e78b-366c-358d-8e6b-087131cdc532 | -3.2808 | -52.7251 | 2024-11-03 00:35:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| e48a45f9-3ff1-3926-a65c-be75aa96fdfc | -3.3276 | -50.2825 | 2024-11-03 00:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 6faed3bf-80c3-3822-ae4a-2bdc1906a944 | -3.3277 | -50.2615 | 2024-11-03 00:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 405ce501-a319-36ff-a0d9-b338edbb6150 | -3.2599 | -53.4164 | 2024-11-03 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3d4cf03d-61dd-39f5-8d8d-feb3bdce96e3 | -3.2624 | -52.746 | 2024-11-03 00:35:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 032c7435-2849-3597-9bcc-629dd46d6461 | -3.2624 | -52.7256 | 2024-11-03 00:35:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 102c4954-24a1-3f66-984b-b88dcc06cdea | -3.2808 | -52.7455 | 2024-11-03 00:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 01b7b1f5-9e18-3724-ad36-eecd3b66eb37 | -3.4749 | -50.3826 | 2024-11-03 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| f3072ff4-b7fd-3b55-9e00-367f0175d74b | -3.475 | -50.3616 | 2024-11-03 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c00d2987-5733-3212-82f2-f2ab0f0fb15a | -3.9473 | -48.3666 | 2024-11-03 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 95c50212-7b1d-3fb1-aeed-c4c96f106714 | -3.9474 | -48.3451 | 2024-11-03 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 10d32b67-5a5a-331a-9152-7230a77c7120 | -3.967 | -48.15 | 2024-11-03 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d222167e-150f-36eb-9616-d0c0eac14ebf | -4.8723 | -48.7318 | 2024-11-03 00:35:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e1adfc51-2950-3715-a05e-4cc5a68351a6 | -8.7059 | -48.0181 | 2024-11-03 00:35:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e6b364d2-6b2b-3c33-bc6e-094035d5f2c3 | -8.7247 | -48.0163 | 2024-11-03 00:35:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 45e7e532-59ac-3498-8dc3-b4ef3411de35 | -9.3073 | -40.2116 | 2024-11-03 00:35:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.7 |
| c25dec14-9710-3fe9-bbff-cf511ac296df | -10.8423 | -49.167 | 2024-11-03 00:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8d07f113-9dd4-392e-86c8-bc557b03249a | -10.8426 | -49.1453 | 2024-11-03 00:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 155e6939-8edb-3ddc-9eca-ba08fc31c3d8 | -11.2819 | -56.144 | 2024-11-03 00:36:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 02b6baf8-0030-3091-b076-b2293abb1552 | -1.2572 | -53.3938 | 2024-11-03 00:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0bf70194-dcef-39aa-940b-7b089856e241 | -1.2755 | -53.4138 | 2024-11-03 00:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 085a807c-c831-38fe-8b12-c9b967935a7c | -1.2755 | -53.3936 | 2024-11-03 00:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 5de09dce-9d8b-32c1-944c-b14e1525c2d8 | -1.2756 | -53.3734 | 2024-11-03 00:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 5b7ba52d-0d47-35e0-bd37-227baf5c36e9 | -2.1746 | -53.6834 | 2024-11-03 00:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d000ad73-9ab2-39e6-800d-7ff6da65d41b | -2.2802 | -48.8082 | 2024-11-03 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 819519fe-cf07-3a64-a72b-1cc5b58a1c2a | -2.2802 | -48.7868 | 2024-11-03 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 284bbced-3c4f-3c8b-b5d3-79c54e656660 | -2.2986 | -48.8078 | 2024-11-03 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 8d633599-3ca0-329d-8565-029761e41697 | -2.2987 | -48.7864 | 2024-11-03 00:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2ef75a3b-e2cf-313f-bb25-c6ece2edba8b | -2.5796 | -53.3927 | 2024-11-03 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0a69cc13-d265-3751-bf64-015bdc52c0c9 | -2.5797 | -53.3724 | 2024-11-03 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c57b62a4-e9cc-3873-99dc-9dbb697154fa | -2.6321 | -48.5849 | 2024-11-03 00:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| edce36b1-f9cf-3eea-8efc-b2261eaa28ae | -2.6322 | -48.5634 | 2024-11-03 00:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 95496b79-32aa-3e40-b6bc-294fdebb1690 | -2.6506 | -48.5844 | 2024-11-03 00:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 91af11b7-4a9b-3d00-8616-c04a6d413448 | -2.6507 | -48.5629 | 2024-11-03 00:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 72877d4d-9c19-33d6-a6e3-052146f3e5ce | -2.7033 | -49.33 | 2024-11-03 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 68c9f868-b2dd-3054-8ab9-e573b276c588 | -2.7218 | -49.3295 | 2024-11-03 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| c43e5f6e-7ecf-3a35-9711-fc97d0949895 | -2.7419 | -54.4353 | 2024-11-03 00:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 221.6 |
| 7f0855c0-4693-3101-908c-7c8da2f1c421 | -2.7419 | -54.4153 | 2024-11-03 00:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 166.9 |
| d8ba1dcf-7090-37b6-91ff-da21876ef88f | -2.7602 | -54.4349 | 2024-11-03 00:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 180.1 |


[Clique aqui para ver as próximas entradas](README8.md)
