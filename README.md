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
| 5918b77e-570f-3d55-9993-a155d4dc93c4 | -2.8347 | -54.1125 | 2024-11-27 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 18ba8579-30c9-3c5a-a548-09eb071d3f5a | -2.824 | -46.8199 | 2024-11-27 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 09332118-cfb5-3370-bfec-d24d963927d0 | -3.9494 | -47.9776 | 2024-11-27 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7f0f4cd4-a0fe-3ccd-b965-cb4478c1a4f4 | -2.6802 | -45.6711 | 2024-11-27 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ffa512be-0178-3406-bf8f-b0ea9033c3e2 | -2.8424 | -46.8413 | 2024-11-27 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1c6860a6-e5ee-3bde-820f-5a0e167a47c6 | -2.8163 | -54.133 | 2024-11-27 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| cbb293a2-97e8-3210-b9f1-2391e744e1f0 | -11.7715 | -54.6828 | 2024-11-27 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f0828d05-df85-311b-8879-2f6274cb24a3 | -1.9062 | -50.612 | 2024-11-27 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 6b9cb999-242e-3da0-a38f-a14e5f7efa7f | -4.6458 | -43.8307 | 2024-11-27 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d6d9aa46-3bf4-3733-9b5e-6ad054bb65d8 | -2.9968 | -45.4584 | 2024-11-27 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 413.2 |
| c5b5c015-ee51-3d71-bcd0-f68d90f492cd | -2.8346 | -54.1326 | 2024-11-27 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 1267602d-16af-306f-9300-4db233744f26 | -3.5411 | -52.1442 | 2024-11-27 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 24d8dc40-9079-3248-8427-5973c9d22dcb | -4.1417 | -43.8135 | 2024-11-27 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| aa66d24d-e126-3ee0-a03c-6a830656f8bc | -1.6444 | -52.4951 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 99054f0e-0635-380b-858f-8b9d4e327d11 | -11.7905 | -54.6811 | 2024-11-27 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9e9ee185-300a-39fd-b03e-d945e21c1e55 | -11.7713 | -54.7033 | 2024-11-27 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4032aba4-976c-3fa8-8810-e987b54fb909 | -4.6646 | -43.8065 | 2024-11-27 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fe3e5439-51a9-38b1-b0ee-4767983db432 | -2.9967 | -45.4809 | 2024-11-27 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 9b9ca6eb-83fa-335d-82a0-d8e70caabaa8 | -4.2115 | -50.8782 | 2024-11-27 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7fca78cc-cb6e-33cd-a87e-d005a8c8d7a8 | -4.2114 | -50.899 | 2024-11-27 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| cbcb1dd8-ef76-3987-a414-46bbbd80cb81 | -3.0154 | -45.4577 | 2024-11-27 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 186.4 |
| 9b321573-6209-3671-8b46-b7289c481817 | -2.8425 | -46.8193 | 2024-11-27 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| cd5ccfce-176b-3d6d-9b4d-1fbf85a935c7 | -3.7796 | -52.403 | 2024-11-27 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c6a74dcc-a7c7-3494-8730-82902e673aff | -4.6644 | -43.8296 | 2024-11-27 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 354464c5-b1b2-31da-a8aa-8324db3abda5 | -5.0401 | -43.5973 | 2024-11-27 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 62ef9cd4-8831-3807-9744-24191aab6f84 | -3.9674 | -48.0851 | 2024-11-27 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6a6d1274-6489-3ee0-b9a1-31f16c1cfab2 | -3.541 | -52.1647 | 2024-11-27 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| cacdc12f-e3d2-3674-a5b6-772ceb848ccc | -3.2757 | -45.4477 | 2024-11-27 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b38d727e-b41b-32df-bd64-2bf1fb124f31 | -5.9788 | -45.3621 | 2024-11-27 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2a2d701f-8c46-3343-ae6c-df80c72dccae | -3.5226 | -52.1448 | 2024-11-27 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 274.5 |
| e3c31135-d1de-37d5-966f-852f80096a00 | -3.7348 | -54.2693 | 2024-11-27 00:00:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5f4f118a-d0b9-34ea-82e6-a25775459b59 | -4.6459 | -43.8076 | 2024-11-27 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8c8885b0-24f7-32da-9a1a-980bf194fa99 | -1.6813 | -52.4537 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 682b51b4-8553-3785-95ca-a16acd6f6484 | -1.6813 | -52.4333 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a33747a1-5a86-3f09-bc84-afbbeb61f53a | -1.6624 | -52.7192 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 174532fe-f6e0-3ca3-a243-9edc73bbe7e7 | -3.9859 | -48.0843 | 2024-11-27 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0677c7bc-6a20-3752-ae14-393e30402a25 | -20.3901 | -47.4668 | 2024-11-27 00:00:00 | GOES-16 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b8d4cbc6-ab5f-38b3-b4fb-ea8ae1c31e9e | -1.6629 | -52.454 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7bdeae3f-e38e-35d8-aff2-34569b620643 | -4.7197 | -46.5605 | 2024-11-27 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c8b834dd-ab96-3ff6-8103-eef9cafd8463 | -11.7902 | -54.7015 | 2024-11-27 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ceca5a94-f37a-3eaf-8fa9-792a3c4030cf | -3.3837 | -50.1125 | 2024-11-27 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 09c3defd-f6ac-3a90-824f-c15c2d22f034 | -3.9675 | -48.0634 | 2024-11-27 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f846a03a-17c8-301d-bdd1-bbbd34fa303a | -2.6803 | -45.6487 | 2024-11-27 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8e70fb4d-aa29-39cd-ae47-b0b5980239b7 | -3.5226 | -52.1653 | 2024-11-27 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 3a2f7437-9cea-3d16-ba66-1832baefc970 | -1.9562 | -45.7137 | 2024-11-27 00:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d8366136-537c-36c6-9801-b0d6d357936a | -5.9975 | -45.3607 | 2024-11-27 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ee2f3a90-c2d5-37e8-a485-5560dda7345d | -3.0153 | -45.4802 | 2024-11-27 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c7d69de7-c3c5-3026-a475-6a59c7abd49b | -2.8239 | -46.8419 | 2024-11-27 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5b17df57-773c-39a1-9ba3-d4a60fcaed33 | -2.6987 | -45.6705 | 2024-11-27 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 00a3ded0-6db3-314f-977e-b244eb8ea6bf | -1.6629 | -52.4336 | 2024-11-27 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 79a599ca-4056-3df7-91c1-8d05c01b62e9 | -2.8611 | -46.8186 | 2024-11-27 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e9653fe4-f637-3b60-8e14-296bec4f734d | -2.6988 | -45.6481 | 2024-11-27 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 136.9 |
| b837d543-9e3a-39a1-a152-7bc66f8ac25b | -3.2758 | -45.4253 | 2024-11-27 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 102.7 |
| c413742f-11d3-37b9-81d0-f73b33c13311 | -3.986 | -48.0626 | 2024-11-27 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4b622764-038c-3751-9bcf-e807596b4c40 | -4.7195 | -46.5827 | 2024-11-27 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5d2703e8-6f78-3528-9923-3090f5cc2419 | -4.7381 | -46.5816 | 2024-11-27 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| cbd97450-e383-35c6-a058-fb3c72a67307 | -3.3938 | -44.1722 | 2024-11-27 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 111b0886-3588-3218-9fb6-9d5541b960cb | -4.1419 | -43.7905 | 2024-11-27 00:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f8c1da1d-3118-342c-9a65-c431721a2e54 | -1.9062 | -50.5911 | 2024-11-27 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 79a13ed5-d2f6-34b0-8963-63b858ce95b3 | -2.5963 | -53.9771 | 2024-11-27 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c8035882-cdb2-3cf4-85c9-45fcc670bb1c | -3.11 | -53.21 | 2024-11-27 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c743df-35d8-3cbe-ad44-63c2f9268b80 | -3.11 | -53.33 | 2024-11-27 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4cf832-fe98-3394-92cb-b60ca6e8602b | -3.11 | -53.27 | 2024-11-27 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677b747e-cfcd-309a-9be5-38613dcec2e6 | -2.99 | -45.48 | 2024-11-27 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea80771-102a-36d1-bae6-e19f65f982bc | -3.16 | -48.42 | 2024-11-27 00:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 738c3f08-842e-3ed9-8639-eb0c7e71f1f6 | -3.08 | -53.26 | 2024-11-27 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5543ba-597d-34cd-9d52-a4d8b5628712 | -3.08 | -53.2 | 2024-11-27 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eae7b527-6f06-32f3-a113-c477fd018f1a | -3.19 | -48.42 | 2024-11-27 00:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e49309-32c1-31fe-9456-c87585286410 | -3.16 | -48.47 | 2024-11-27 00:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 800bbf89-5422-348e-8ec8-37599a4f65e0 | -2.99 | -45.43 | 2024-11-27 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d249d63-7722-3d60-aaa6-0b54ab683f05 | -2.6803 | -45.6487 | 2024-11-27 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 91fd52b2-e477-336d-84c8-4082a8bb455f | -2.6987 | -45.6705 | 2024-11-27 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 987f77de-cabb-365a-89c9-58844d61a1f2 | -4.2115 | -50.8782 | 2024-11-27 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0b7ab1d3-3a92-3c89-9e7c-7c0cea380dac | -3.1506 | -48.44 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f7118c70-8322-3617-bb13-ce3a3a9fd702 | -2.9967 | -45.4809 | 2024-11-27 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 282.1 |
| d33bb5b5-8010-3a03-a994-812613382243 | -11.7905 | -54.6811 | 2024-11-27 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| cede4727-4a6c-37d2-a983-2ddad15b34d2 | -3.169 | -48.4609 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| c1514e9f-2ea3-300d-b7c0-823469007ad5 | -3.541 | -52.1647 | 2024-11-27 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 540bc1c3-2157-36a2-ac2f-875233ecbee6 | -5.9975 | -45.3607 | 2024-11-27 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| dac249ef-4a3b-3876-97f4-1509438ea100 | -3.5226 | -52.1448 | 2024-11-27 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 1db3ec34-0daf-37bb-a5cb-bafc2a191583 | -4.2114 | -50.899 | 2024-11-27 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 1009f8bb-3319-3cbc-a843-3f0f99f8fdb3 | 1.3535 | -50.6207 | 2024-11-27 00:10:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4936e94c-5c9e-3715-a70d-e1af1f7a7233 | -3.5411 | -52.1442 | 2024-11-27 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| e30d24d2-effd-3ac2-b07b-53108f8895b0 | -1.9062 | -50.612 | 2024-11-27 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| dd2ab9f9-b252-3f3e-9ff3-9090536272a8 | -1.6444 | -52.4951 | 2024-11-27 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ef9cc6e6-73ea-3f11-bdcd-9e228bafaa8f | -6.9813 | -35.0267 | 2024-11-27 00:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 93.7 |
| 5f170b67-86b5-3c14-a32b-1d449559f360 | -4.1417 | -43.8135 | 2024-11-27 00:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ea6e3cc1-cdf3-3d34-9ab0-3b6b2fc7b08a | -1.9062 | -50.5911 | 2024-11-27 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ec5aee0e-6657-3112-baed-ae47a28b59b7 | -1.6629 | -52.454 | 2024-11-27 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bd813761-d251-313b-8bb8-ca452d5cb1fd | -2.8425 | -46.8193 | 2024-11-27 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2356c545-8249-3671-a3cb-e8ff6ace3df8 | -1.6813 | -52.4333 | 2024-11-27 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 16aac226-37f0-3d94-b168-35c4b572c6d1 | -2.8346 | -54.1326 | 2024-11-27 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| a90ae941-9c6b-3898-97a5-3ffca1545b20 | -2.824 | -46.8199 | 2024-11-27 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8e96015b-1eb1-3b12-a2f7-371320de4923 | -3.0154 | -45.4577 | 2024-11-27 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 278.0 |
| 048c122e-7c0f-3c41-a175-7113919512e7 | -3.9675 | -48.0634 | 2024-11-27 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f55ea942-21ea-397b-bbc5-9ffab44896ed | -11.7713 | -54.7033 | 2024-11-27 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| dc12a2d3-dc25-340b-a5a5-5488cedfa6c7 | -5.9788 | -45.3621 | 2024-11-27 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| be36c7ad-9b54-30e1-844e-a18719a2c23e | -11.7715 | -54.6828 | 2024-11-27 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f3d28a1c-f309-3dca-b3d1-7f74d8deb932 | -1.9246 | -50.6117 | 2024-11-27 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a2c081f0-bf8b-3b95-8fd6-42f7aad95f6b | -3.1692 | -48.4179 | 2024-11-27 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 232.8 |


[Clique aqui para ver as próximas entradas](README2.md)
