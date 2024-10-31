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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70e3cbc3-3913-30aa-8168-e711721b1a35 | -5.0464 | -45.1768 | 2024-10-31 02:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 70f75f97-7abf-3c95-a95c-438395c22e80 | -6.1416 | -43.9563 | 2024-10-31 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6cc81c34-b232-3fe2-bf73-6c4c1d674b49 | -6.1229 | -43.9578 | 2024-10-31 02:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| b22cb611-dbcf-3aa1-acc4-d3bb864a5cf5 | -10.0118 | -64.8023 | 2024-10-31 02:16:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a634ccac-8aa1-398a-99f6-031df902db04 | -12.4433 | -43.7242 | 2024-10-31 02:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e6786419-cfa2-300f-8fa1-6121b43b7860 | -19.5087 | -56.5779 | 2024-10-31 02:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 4b2cfdf2-f07c-32ca-85ef-bb02e11fc7e6 | -1.4426 | -52.273 | 2024-10-31 02:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9a4fc1ed-cd62-3554-a359-e591e03179da | -1.8475 | -52.1236 | 2024-10-31 02:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 144fa1e0-9a76-3bbe-85a5-08c86906c28d | -1.9684 | -47.9552 | 2024-10-31 02:25:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 48d35c1f-4650-3ae4-bc2c-54cec51b5cdc | -2.5216 | -48.4591 | 2024-10-31 02:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 7145a12e-5946-3e7b-a2fa-bb875da7f7f7 | -2.5215 | -48.4806 | 2024-10-31 02:25:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| c395c292-b0e1-301e-9ca0-e7c340769a91 | -3.242 | -53.2751 | 2024-10-31 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 835b1b7c-62b4-3cd0-8bea-6cbf1ff9cbfd | -4.2749 | -43.4357 | 2024-10-31 02:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5443b423-2667-3184-8ca3-525b1dbb07c9 | -4.6051 | -44.2932 | 2024-10-31 02:25:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| abd5aa36-d32e-3f95-84ac-c0e651b3b60f | -4.6049 | -44.3161 | 2024-10-31 02:25:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a84942a9-890f-3e80-b3de-b3b0dc81a3ca | -5.0466 | -45.1542 | 2024-10-31 02:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7bbfa15a-7223-3a73-b5ef-3357ca9eb96c | -5.0464 | -45.1768 | 2024-10-31 02:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3aec16ff-9e25-36c4-910c-baf3085a7f32 | -6.1416 | -43.9563 | 2024-10-31 02:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 837ae345-698e-3ce7-80c3-0df9e76fc2cb | -10.0118 | -64.8023 | 2024-10-31 02:26:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 88af135e-e822-3627-b838-7b0cc18e69d2 | -2.5215 | -48.4806 | 2024-10-31 02:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| afdcba3e-bf99-3113-8cb4-41ea55738a1b | -2.5216 | -48.4591 | 2024-10-31 02:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| cbf59f4a-aa52-3f2f-bb98-f0f781bff9bf | -4.2749 | -43.4357 | 2024-10-31 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 621193e4-9a9b-3beb-be34-8fbd357f918a | -4.6049 | -44.3161 | 2024-10-31 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 710e25bf-e7a1-319f-99bb-864424910f08 | -4.6051 | -44.2932 | 2024-10-31 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 020daa55-2867-3e9e-a820-f57ae523728a | -4.8176 | -45.8653 | 2024-10-31 02:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1a7d4872-e808-3e9e-97d9-bd32452a6ebf | -4.8178 | -45.8429 | 2024-10-31 02:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 09c0be0c-ea08-3491-86db-b39beb402f17 | -4.8364 | -45.8418 | 2024-10-31 02:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d13eb57c-a45f-3492-8fb1-cfbdae1263c3 | -5.0466 | -45.1542 | 2024-10-31 02:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 020a5f31-8921-3105-825b-1b468347d73c | -6.1229 | -43.9578 | 2024-10-31 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ac5a3ca8-21ef-3c9b-954c-2e09e3ff5584 | -6.1414 | -43.9794 | 2024-10-31 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ed5e97f1-b3a2-38ce-99da-8fb52c82daad | -6.1416 | -43.9563 | 2024-10-31 02:35:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 99a618a4-5669-32cf-bbdf-da5a38f3c85b | -6.521 | -35.2488 | 2024-10-31 02:35:42 | GOES-16 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 149.0 |
| 24d24d7e-4d2c-34b8-93ef-9c207acb42c2 | -6.54 | -35.2465 | 2024-10-31 02:35:42 | GOES-16 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 808395ee-2d81-3f10-8fee-7b45043d206e | -10.6819 | -65.002 | 2024-10-31 02:36:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| e2da11a0-8b84-3394-8f77-9f4ef9e66fd1 | -7.83605 | -35.21861 | 2024-10-31 02:43:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1f7f0909-2eb6-339c-baa2-5014339b7c05 | -9.40272 | -35.77061 | 2024-10-31 02:45:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6a8c7531-8a73-36db-b8da-cb097a6ce329 | -9.39555 | -35.76886 | 2024-10-31 02:45:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b322589f-8754-3de3-af93-5539f8e6ff99 | -9.3941 | -35.77602 | 2024-10-31 02:45:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f33a8e40-ee03-33e1-a074-475ff1e77a64 | -2.5216 | -48.4591 | 2024-10-31 02:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 05434a0d-056d-3b45-af7c-0a71474a9a7c | -2.5215 | -48.4806 | 2024-10-31 02:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 9d7990d5-6cc8-3558-9c93-b313b23f9cf3 | -4.6049 | -44.3161 | 2024-10-31 02:45:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 084bb629-7c4d-389a-93a7-5af4f6bb49aa | -4.8364 | -45.8418 | 2024-10-31 02:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 3d97bb8c-5536-32b7-92a4-f0808576286e | -4.818 | -45.8205 | 2024-10-31 02:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| cf8a444f-ef83-3d71-9b2b-4784c00662d5 | -4.8178 | -45.8429 | 2024-10-31 02:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 271.2 |
| 5611bc28-71c0-3725-bc77-caf657019fbe | -4.8176 | -45.8653 | 2024-10-31 02:45:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d154c4d3-7921-389f-971d-681aa8c70676 | -5.0466 | -45.1542 | 2024-10-31 02:45:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 847b06a8-c7f2-3a27-919c-cca6c02df663 | -6.1416 | -43.9563 | 2024-10-31 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b4e448d5-087e-3002-ac07-46d15d528226 | -6.1229 | -43.9578 | 2024-10-31 02:45:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 88ddf5ac-7354-331e-bdf5-7429968ff1bc | -9.9497 | -36.2836 | 2024-10-31 02:46:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 548a7595-991c-3412-a86c-8d576e34332b | -9.9304 | -36.287 | 2024-10-31 02:46:01 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 5a0262ff-29e1-32fb-bb9a-e1db245e8b9d | -10.0118 | -64.8023 | 2024-10-31 02:46:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 7168a517-33cf-34b9-8e6a-1eb24f3e01dc | -10.6819 | -65.002 | 2024-10-31 02:46:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 56be3f25-7920-37ed-b3bc-348c364d0084 | -4.6051 | -44.2932 | 2024-10-31 02:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 6a6feda2-83bc-3632-a34d-b780d3e58653 | -4.6049 | -44.3161 | 2024-10-31 02:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 3e9c55a6-d705-321f-bbef-82ccd8ac93cb | -4.8364 | -45.8418 | 2024-10-31 02:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d0324079-1e00-3500-af93-d6a22eb410e7 | -4.818 | -45.8205 | 2024-10-31 02:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| def6265d-0a95-38e2-acf6-c56213ce893f | -4.8178 | -45.8429 | 2024-10-31 02:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 1d6b0483-ccb7-3fd7-a6e7-6b3f2c659692 | -4.8176 | -45.8653 | 2024-10-31 02:55:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e40d9af5-90c5-3014-8857-0ebe377517b7 | -6.1416 | -43.9563 | 2024-10-31 02:55:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 77671300-10af-3f92-942a-e15300419031 | -10.0118 | -64.8023 | 2024-10-31 02:56:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f3d4f890-7446-3593-a86a-f829c06799c3 | -10.6819 | -65.002 | 2024-10-31 02:56:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 85f78588-6326-346e-a3b6-19ce932e5cec | -4.1942 | -38.9731 | 2024-10-31 03:05:29 | GOES-16 | GUARAMIRANGA | CEARÁ | Brasil | 2305100 | 23 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 82ae512d-3ec5-36d2-bbaa-f40ba0ac37e2 | -4.2749 | -43.4357 | 2024-10-31 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 5a540c35-f1d0-3c18-a5f3-6dcd8970c316 | -4.8176 | -45.8653 | 2024-10-31 03:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 95d49d41-ee40-3e38-94ae-bcc90a567e2e | -4.8178 | -45.8429 | 2024-10-31 03:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 134.4 |
| c1c2bf5c-5293-35ba-9e20-e4f23fe08ec7 | -4.8364 | -45.8418 | 2024-10-31 03:05:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7c38553a-33e1-3dbd-a315-3269afab9a3e | -6.1229 | -43.9578 | 2024-10-31 03:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b1aad130-4315-3483-8f23-a80064fae1ec | -6.1414 | -43.9794 | 2024-10-31 03:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 09df1c6d-c856-3248-b3f5-fa3dd90a741e | -6.1416 | -43.9563 | 2024-10-31 03:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 67da4452-7667-38e1-8bf4-2945346c08dd | -10.0118 | -64.8023 | 2024-10-31 03:06:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9aa8cc22-1f5a-389a-bb1f-3ee972531007 | -10.6819 | -65.002 | 2024-10-31 03:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 45943307-4d81-33ec-8c88-66dade63eb9a | -6.79249 | -35.22839 | 2024-10-31 03:08:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9cc78ef7-ec91-353d-85ea-84a2fbeb8262 | -6.78078 | -35.13526 | 2024-10-31 03:08:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b21cb18f-aad3-3acd-9806-16a49f1b2aef | -5.30088 | -40.50854 | 2024-10-31 03:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ed68a761-dcf6-3bbc-b190-fa0be7a73d2f | -5.29967 | -40.51526 | 2024-10-31 03:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 72887c86-f88c-3dd2-bea8-1ba2ffb99afe | -5.29935 | -40.51022 | 2024-10-31 03:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8480d3ef-71db-3983-8c0e-f18c4b0f5733 | -5.2981 | -40.51694 | 2024-10-31 03:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4eddfa03-b574-32c4-b84f-ad3ffb456a22 | -4.19196 | -38.97701 | 2024-10-31 03:08:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 31334325-69b2-3ff2-9e95-251ccd793860 | -4.19097 | -38.98289 | 2024-10-31 03:08:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ae8f014a-c4fd-3244-b413-1712bbd0dd16 | -4.19066 | -38.98425 | 2024-10-31 03:08:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d5338548-9fc6-3faa-b44b-3f8dd8ab6da8 | -9.94871 | -36.30553 | 2024-10-31 03:10:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c2ebc42e-a3b7-37a1-ab51-c8a83f8ccf5b | -9.94481 | -36.29871 | 2024-10-31 03:10:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| ae8a8c99-af67-340e-8c6b-0ea07b953f89 | -9.94376 | -36.30453 | 2024-10-31 03:10:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| 21e03356-fbb9-35a3-b592-6c659e8ce25c | -9.39555 | -35.93651 | 2024-10-31 03:10:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 34acede5-c040-3c32-8dc2-46cb2dc1bc0a | -9.39366 | -35.93252 | 2024-10-31 03:10:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9484b2bd-c9d3-3959-9457-4b3c7349303b | -9.39266 | -35.93801 | 2024-10-31 03:10:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 51e84c0d-1113-3823-a4cd-73ade620a16a | -9.39067 | -35.93562 | 2024-10-31 03:10:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 481fd50d-497b-3539-bc55-8b50bfa38029 | -7.98883 | -39.94281 | 2024-10-31 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| df543877-4233-31c5-9503-9c9770cd19fc | -7.98805 | -39.94546 | 2024-10-31 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9a9e097-ed92-3e51-b808-5629bcacba65 | -7.98776 | -39.9483 | 2024-10-31 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3aa1c241-88fc-3f10-9876-ecb980c0302f | -7.98702 | -39.951 | 2024-10-31 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 234a297a-f3c4-35a8-a2a5-7fe127dc7063 | -7.56463 | -38.75635 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0dceabd5-81ac-3e5c-9937-dd81dbad428f | -7.56413 | -38.75274 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 618ab312-e442-345b-ab32-387db461d360 | -7.56326 | -38.75748 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87498460-f058-3237-b8e7-ba84628930f1 | -7.56192 | -38.77068 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ae99e3f-09c4-385d-8c6d-3d970f1447d3 | -7.56093 | -38.77592 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 18328e05-0254-383e-a35c-c1ed5c640c6e | -7.56064 | -38.77195 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ec67a8f2-1d8a-383f-b5ff-134e659b7d9e | -7.55968 | -38.77724 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05f76be7-1bdd-31f0-9584-e019243e3913 | -7.54932 | -38.76533 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71b15983-eef3-3937-895a-d9659dd4c5db | -7.54842 | -38.77024 | 2024-10-31 03:10:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
