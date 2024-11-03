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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e4a2cf-18e5-38d8-a610-10f829fcf636 | -3.0734 | -54.167 | 2024-11-03 06:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 9fb7a0a7-3b15-333f-a148-fd712d90e993 | -3.0734 | -54.147 | 2024-11-03 06:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 9695695f-2033-3e1f-b28c-ce2dffc54c2e | -3.0875 | -50.2901 | 2024-11-03 06:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f27d3022-69f4-32c3-b9a4-587dafafc900 | -3.1059 | -50.3105 | 2024-11-03 06:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fb2ed812-c022-3bea-a567-bf2c7bf3f3ab | -3.106 | -50.2896 | 2024-11-03 06:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8942b81f-3e24-35dd-86f3-343830eddb46 | -3.1061 | -50.2686 | 2024-11-03 06:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 42227351-ff80-375e-9692-1834ad8bbc1f | -3.1245 | -50.289 | 2024-11-03 06:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 5c1854d6-8a14-3d2a-8949-bcccfcb2ce14 | -3.4749 | -50.3826 | 2024-11-03 06:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3ac2feba-4c0f-3bcf-b171-1497fbeb3601 | -3.9474 | -48.3451 | 2024-11-03 06:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0062d931-c4d2-33ef-a507-4d31f0b63414 | -4.05825 | -55.53012 | 2024-11-03 06:29:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 6d951017-4157-35bd-83bd-51b4e77396d3 | -3.07603 | -54.14495 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2a173f5a-9866-3595-9b1b-85617f920de0 | -3.06128 | -54.13818 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7ef9ffca-da0a-3507-b870-0a282e415731 | -3.06108 | -54.14295 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 32088d0c-4bee-3b18-9963-ef2e138375e5 | -3.04634 | -54.13612 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 4174c25c-2c2f-33c0-80ed-cc55d1ae6878 | -3.04615 | -54.14089 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 331105b4-d2d5-3baa-8ccf-146860ba5bc9 | -2.74979 | -54.41274 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| ee24f0c6-5ab8-31a4-bdb5-3b5c84aae1f6 | -2.74906 | -54.40529 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 35dc3529-5811-3c3b-a106-9400877f6019 | -2.74526 | -54.43141 | 2024-11-03 06:29:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 55ac1b9e-16ce-3c38-b22d-6d82f7c3d704 | -2.57698 | -53.36933 | 2024-11-03 06:29:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| abf9d976-bc08-3f35-b0b9-c48d177b88f6 | -2.17108 | -53.65943 | 2024-11-03 06:29:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 6d8056c5-88de-3bae-aad9-5bef5ed2152c | -2.16692 | -53.68857 | 2024-11-03 06:29:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 30b04ede-8665-38ac-b4a9-bbbef0f23682 | -1.27169 | -53.37507 | 2024-11-03 06:29:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| bf09e682-aa78-3d02-b503-078ccc098a84 | -1.26727 | -53.38174 | 2024-11-03 06:29:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ac64ab31-2ee4-32fb-b653-da14ff1b7994 | -1.26723 | -53.40473 | 2024-11-03 06:29:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 80d4973e-1039-33ea-849c-5a5b27b4d4a1 | -1.26298 | -53.41177 | 2024-11-03 06:29:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 34608e0d-7937-37ba-954f-aad8d74f7e68 | -1.2507 | -55.69199 | 2024-11-03 06:29:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a60f007d-3b5f-3757-8b74-f3964e0a5850 | -0.74215 | -62.8951 | 2024-11-03 06:29:00 | AQUA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b37cfe0-1523-3446-806e-b81065939ee5 | -12.31762 | -63.63021 | 2024-11-03 06:31:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfbdb5ff-afcc-3054-afa3-874d4e8686ad | -1.0441 | -47.9272 | 2024-11-03 06:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 166876ed-1e4d-3d27-b5da-cbaff9c62b39 | -1.0441 | -47.9055 | 2024-11-03 06:35:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 93b34439-994e-3d57-a282-526a93fbca21 | -1.0626 | -47.9269 | 2024-11-03 06:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 51b561b7-da84-36f1-8384-9f6beff9b69b | -1.0626 | -47.9053 | 2024-11-03 06:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 0ef5afd4-fd8b-3687-acf4-852acc15abcf | -1.2755 | -53.3936 | 2024-11-03 06:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a8632634-ec0e-32f6-9080-c8e2096144cf | -2.1746 | -53.6834 | 2024-11-03 06:35:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 363772af-cb01-376e-8b84-2f245eb8ad7a | -3.1059 | -50.3105 | 2024-11-03 06:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4bf4dbf1-acff-3dfb-a026-d947ddb06900 | -3.106 | -50.2896 | 2024-11-03 06:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| cf1b90a9-936a-3b4c-b8b7-7749b4f072c9 | -3.1061 | -50.2686 | 2024-11-03 06:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 6d2da2d2-98eb-3e68-9020-a14e0979f829 | -1.0441 | -47.9272 | 2024-11-03 06:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| c9cf32d8-c79d-3ce6-843f-7387f4f81a57 | -1.0441 | -47.9055 | 2024-11-03 06:45:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d941f97b-1ab0-3ec3-b5cd-665c69dd1e3c | -1.0626 | -47.9269 | 2024-11-03 06:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f88e783c-905e-3719-9391-00d6d56ba2be | -1.0626 | -47.9053 | 2024-11-03 06:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ff76923f-e737-373d-b811-5fd219a847e3 | -1.2755 | -53.3936 | 2024-11-03 06:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b5a3bbb6-74be-30c8-b7b2-161ef3e039fb | -2.5796 | -53.3927 | 2024-11-03 06:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 57e32689-b324-39d8-aa00-23ae06f81bb5 | -2.7419 | -54.4353 | 2024-11-03 06:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c5306c74-621e-3865-abac-4cb32b2902dd | -1.0441 | -47.9272 | 2024-11-03 06:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 893185df-e86c-3a2e-9c6c-c11bd5a9e039 | -1.0441 | -47.9055 | 2024-11-03 06:55:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7f922b60-8e7b-34ad-8223-6ef577a02b2d | -1.0626 | -47.9269 | 2024-11-03 06:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1f5db501-a0d0-36de-846f-b8bbc14ceecf | -1.0626 | -47.9053 | 2024-11-03 06:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| bb723018-6046-3604-a3de-f309e0b3ff32 | -1.2755 | -53.3936 | 2024-11-03 06:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 0b6e7517-6401-330d-addd-c47f67dec0db | -1.0441 | -47.9272 | 2024-11-03 07:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5d41ea33-e33f-3dac-ac3a-db71f41a1b9b | -1.0441 | -47.9055 | 2024-11-03 07:05:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 73db96e2-c22f-39e0-84a4-d490ae767c8f | -1.0626 | -47.9269 | 2024-11-03 07:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| efaf6fa2-8c03-3f0f-b05e-c870f84645f4 | -1.0626 | -47.9053 | 2024-11-03 07:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7635cc30-5331-3371-827f-69c02d96a880 | -1.2755 | -53.3936 | 2024-11-03 07:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d7d95605-8a77-3bfb-882a-4854fb33db54 | -1.0441 | -47.9272 | 2024-11-03 07:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 2ae94a9e-0c01-384d-8eee-686d89bf604e | -1.0441 | -47.9055 | 2024-11-03 07:15:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| da131009-3135-32f5-b71e-d07269efd9e4 | -1.0626 | -47.9269 | 2024-11-03 07:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 7de98be0-e668-3002-abee-18b8ee58265e | -1.0626 | -47.9053 | 2024-11-03 07:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 79f2fb31-6c48-3748-b732-807cdedaa57f | -1.2755 | -53.3936 | 2024-11-03 07:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a1d46036-9a49-3b6f-b80d-c799bd89a090 | -1.2756 | -53.3734 | 2024-11-03 07:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a7654249-2a5e-3bcf-ae30-005aeb2c9475 | -1.0441 | -47.9272 | 2024-11-03 07:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 6598fd34-55d2-3b9d-949f-cde1899978bb | -1.0441 | -47.9055 | 2024-11-03 07:25:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2e107c75-24be-31fa-ac8f-b5342d86295e | -1.0626 | -47.9053 | 2024-11-03 07:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2dcbbb68-95b1-3517-b63c-6c4bdb37c66c | -1.0626 | -47.9269 | 2024-11-03 07:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c4347cd0-833b-3d59-aa59-434c24dd7c55 | -9.71 | -40.68 | 2024-11-03 10:04:28 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 985eeeb1-b534-3324-aca4-18ea61640b1a | -9.68 | -40.67 | 2024-11-03 10:04:30 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| df3aeba8-fbfd-3b7f-8b48-e8404e82ec1d | -10.14 | -45.31 | 2024-11-03 11:04:27 | MSG-03 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da19b6a2-7222-337a-a4b9-65e80f60d685 | -3.54 | -42.15 | 2024-11-03 12:05:08 | MSG-03 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2baf6ac1-6874-326d-b334-8d455316d473 | -1.4146 | -47.4882 | 2024-11-03 12:05:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 8c213c6e-b04b-3fa3-93e1-c5633937914c | -1.4331 | -47.4879 | 2024-11-03 12:05:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| b4e1bf7c-4a0c-3e55-a753-357d18a08029 | -1.4331 | -47.4879 | 2024-11-03 12:15:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ad430fe9-05d5-3681-99a6-22f4c1a0b22a | -1.4146 | -47.4882 | 2024-11-03 12:15:14 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 19693af4-fb07-3c50-b7fc-90a43e2fc29a | -2.3061 | -46.5046 | 2024-11-03 12:15:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c7c34cbf-9001-3e53-8af8-c5ec65ca1e84 | -3.32304 | -43.20118 | 2024-11-03 12:16:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0c2ee1b5-44ed-3b8b-8aac-34f2518ba9da | -4.41456 | -43.45108 | 2024-11-03 12:16:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| eb4ede03-9335-34d7-8499-a10b7d8d72ad | -4.41292 | -43.46199 | 2024-11-03 12:16:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6d95206e-4794-37c9-9642-e75a135f717a | -4.41128 | -43.47293 | 2024-11-03 12:16:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 56b8ee8e-3d38-31ae-b67d-429dda514d85 | -3.77583 | -43.54153 | 2024-11-03 12:16:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d28467e6-d317-3113-addb-edf5139aae1f | -4.01142 | -44.29205 | 2024-11-03 12:16:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eb184d70-7aeb-32f8-bf1e-71c266ceb826 | -4.00098 | -44.29057 | 2024-11-03 12:16:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9b777118-a0b0-3956-800a-479da26b5d9b | -3.99907 | -44.30314 | 2024-11-03 12:16:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fc477652-b428-3146-9cbf-a1481e29697e | -3.76757 | -44.43324 | 2024-11-03 12:16:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 16d6b839-fc82-38ae-aea8-183956081a0e | -3.69776 | -45.14476 | 2024-11-03 12:16:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bcf1ce85-eb69-31e3-b523-5bd7cddd3d60 | -1.74257 | -46.07761 | 2024-11-03 12:16:00 | TERRA_M-T | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 31335ce9-4407-3296-b308-e2453c89132b | -2.66402 | -46.75797 | 2024-11-03 12:16:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| aa348697-cee8-31d3-93ae-a7fd4188f583 | -2.30665 | -46.51678 | 2024-11-03 12:16:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 7d1a6e56-31ad-367e-b993-37d71cf4e153 | -3.04508 | -49.47198 | 2024-11-03 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 3d61fb12-bdc7-3925-bb57-13a374a8f902 | -4.92659 | -38.59305 | 2024-11-03 12:16:00 | TERRA_M-T | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 7dfac701-a47c-39b4-91e7-bd8de7f2dc06 | -3.43488 | -39.0463 | 2024-11-03 12:16:00 | TERRA_M-T | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f833a6fa-6734-35d9-95cb-eb05a3537e22 | -3.41094 | -40.17926 | 2024-11-03 12:16:00 | TERRA_M-T | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 03fa98f4-b536-3554-a20c-caf7d57b3388 | -3.6769 | -40.44135 | 2024-11-03 12:16:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 843a2b3c-c465-3e9b-b1a3-70c43ea239af | -3.67563 | -40.45013 | 2024-11-03 12:16:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 612cebf0-e008-3e89-a184-c7621cc0d212 | -3.42399 | -42.7374 | 2024-11-03 12:16:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 989b88ec-567e-3eb7-bc8f-bcdf1f4768a5 | -3.33232 | -42.60357 | 2024-11-03 12:16:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ca9729b9-691b-31b2-b8f2-3af9794d19a6 | -2.87192 | -42.66311 | 2024-11-03 12:16:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 27611d03-e25b-373d-8b14-fa2ad29dcb9d | -2.87039 | -42.67341 | 2024-11-03 12:16:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7f593c36-fe0c-3e06-b35d-026fc07251d5 | -2.85779 | -42.69272 | 2024-11-03 12:16:00 | TERRA_M-T | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 30c53ef6-1870-3366-aac9-21b9f7ba00cc | -3.54837 | -42.14925 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 829f287c-d8c7-3b1c-b853-701d2d38d527 | -3.54697 | -42.15889 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 289.3 |
| 6963e9d8-9bf0-3e9d-8f3c-9a1c82e00bca | -3.54557 | -42.16851 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |


[Clique aqui para ver as próximas entradas](README91.md)
