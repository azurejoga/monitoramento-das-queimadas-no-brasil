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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ef4e17e-5f89-3d56-8d2a-7850c12297db | -4.6085 | -46.5002 | 2024-11-23 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 287.3 |
| 7ec52037-f857-30b7-98a5-c3bfe708a264 | -2.6963 | -46.2719 | 2024-11-23 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 92710f4e-4115-3f30-9afb-225f0796ac96 | -3.2544 | -50.1168 | 2024-11-23 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7c66e48e-1935-3f48-b766-ddf712e08afc | -4.706 | -45.8493 | 2024-11-23 01:10:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d87a198d-4d4e-3351-9879-f5985be3eef5 | -1.7891 | -53.6495 | 2024-11-23 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a5a2c088-8d94-3954-b422-4900cba0c9a7 | -6.5054 | -47.0414 | 2024-11-23 01:10:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 44a67f4f-bc0e-3140-8e24-e6d0f9b4495a | -4.4196 | -44.1204 | 2024-11-23 01:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c03ee996-45b1-33bf-a648-fbe5956aaba1 | -4.5402 | -42.93 | 2024-11-23 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b38c585f-efe2-35db-9500-197a9d5cf6c9 | -6.4867 | -47.0428 | 2024-11-23 01:10:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ae92359f-e41b-3c7f-b660-51ed9177802e | -3.2385 | -54.2431 | 2024-11-23 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 3204fc79-4456-3a13-ad32-4de744a5a83a | -2.8309 | -45.1493 | 2024-11-23 01:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 209.7 |
| acd416c0-b605-3423-b479-0fbc5d4b1c64 | -4.5216 | -42.9078 | 2024-11-23 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d0a217c4-383e-3a9a-93b5-45d1d7b299de | -3.2569 | -54.2426 | 2024-11-23 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 55a962d1-a760-37ac-a4a8-4a097e8cd139 | -2.7149 | -46.2713 | 2024-11-23 01:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e3c5ab85-69e0-3d22-b7ce-c5ad14e0b659 | -3.2543 | -50.1378 | 2024-11-23 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9905ce6d-d29d-33a0-b480-0f63213026f2 | -2.8123 | -45.1725 | 2024-11-23 01:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| c07a0f0d-b808-3a87-899a-108c2398f229 | -2.8308 | -45.1719 | 2024-11-23 01:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 170.8 |
| d38a67fb-7a20-3a9f-abc3-248b68060f47 | -4.67 | -45.6722 | 2024-11-23 01:10:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2e505dc0-6219-39a1-a6d5-08a574b19149 | -3.2386 | -54.223 | 2024-11-23 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 3f8ddcb3-ccc7-31bb-bfab-fd093c7b38e4 | -4.1133 | -42.4614 | 2024-11-23 01:10:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 52b3080a-a81a-37ca-bc26-6004273ea383 | -2.8124 | -45.1499 | 2024-11-23 01:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 0654cb1f-d611-3f08-8334-5202071dd650 | -4.6086 | -46.478 | 2024-11-23 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 134.5 |
| d74be2a2-a870-39c9-bf98-d6acde36da8e | -2.6061 | -45.6287 | 2024-11-23 01:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 20a3c801-49be-3193-94a6-4e10078c11b8 | -3.1831 | -54.3247 | 2024-11-23 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 363a10b4-1390-3f07-b709-49bd6c83deae | -3.2359 | -50.1174 | 2024-11-23 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 517620c5-650e-3550-a445-aa544723fca3 | -3.7538 | -50.0152 | 2024-11-23 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 7edc2c32-6f17-3f84-887d-10ae7f02d464 | -4.5403 | -42.9066 | 2024-11-23 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 52aaefb8-42b7-33af-98c3-d079627bacf8 | -1.7175 | -52.7184 | 2024-11-23 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 80bbbc88-702c-31c5-b222-8a8f50f2ce91 | -3.2569 | -54.2226 | 2024-11-23 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 42b57be5-87c0-399a-8622-f2c1321c8d1f | -1.7359 | -52.7181 | 2024-11-23 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 10795dce-ba3b-3fe7-8d4a-5105d9553f30 | -3.2569 | -54.2426 | 2024-11-23 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d9a6d258-373a-33f0-9f70-28b56c624a4b | -3.2385 | -54.2431 | 2024-11-23 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| a9ac380e-92ed-3363-99fd-481eb2739c9e | -4.5402 | -42.93 | 2024-11-23 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 548d11f2-b663-330d-8da2-b99cf66775ef | -4.5215 | -42.9312 | 2024-11-23 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e01a0b63-2f08-3b2f-b568-43be8ced2f99 | -6.5054 | -47.0414 | 2024-11-23 01:20:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9d64122c-52f7-3514-bbe8-7cfc35d1d700 | -4.5403 | -42.9066 | 2024-11-23 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 829e2a99-cacf-355a-848e-de686364f2ac | -2.8124 | -45.1499 | 2024-11-23 01:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 004e6aad-941e-3e5a-b5ff-13a8dc521f91 | -1.2495 | -46.7468 | 2024-11-23 01:20:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3d6dee23-8fac-33fd-bc15-f20270323d26 | -5.0912 | -44.217 | 2024-11-23 01:20:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 884df578-218d-387b-b3c4-b69baae54d32 | -2.8308 | -45.1719 | 2024-11-23 01:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 2341b25e-b7ce-3c18-9648-9e7a154d123d | -1.7359 | -52.7181 | 2024-11-23 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 1bb60311-fe35-3438-be18-805c50fe7e69 | -4.67 | -45.6722 | 2024-11-23 01:20:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7133f8d2-ef5f-304e-ab36-1a8e2a08e0a5 | -2.6963 | -46.2719 | 2024-11-23 01:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5fec7a15-473f-3552-85d8-63139d1d99f8 | -4.6086 | -46.478 | 2024-11-23 01:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 48bcdb82-1b32-3c3e-9b6d-0854cc8508d3 | -3.2543 | -50.1378 | 2024-11-23 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d6a1b696-93f9-3b04-be52-08832758fac8 | -3.7539 | -49.9941 | 2024-11-23 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e5afd558-cd1c-32cf-9cdd-e6506411586a | -4.706 | -45.8493 | 2024-11-23 01:20:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e6de5b9f-ed11-3138-9363-69c24dd00a83 | -3.7538 | -50.0152 | 2024-11-23 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 817a9b41-1678-3f5d-9415-2b05e98d0f40 | -4.5568 | -45.88 | 2024-11-23 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3ec760ad-aff4-3f80-bea7-3c4c9c63ec8c | -3.2386 | -54.223 | 2024-11-23 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 9f6fbb97-dd1e-3615-82e8-8222ededc2dd | -4.6085 | -46.5002 | 2024-11-23 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 93ece0cd-e13c-3755-8652-bb297c233dd1 | -2.8309 | -45.1493 | 2024-11-23 01:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 96dccce9-89df-3f8d-94ae-c4cdbffdaca4 | -2.8123 | -45.1725 | 2024-11-23 01:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 628352d7-bdec-3e9d-948d-2deecff2783f | -3.2544 | -50.1168 | 2024-11-23 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| b805897a-bd0c-329a-8857-3ffbc1d2ef1b | -4.5216 | -42.9078 | 2024-11-23 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a9bb0e72-0944-31a6-8adf-b4b1f865169f | -1.6075 | -52.5977 | 2024-11-23 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 97a787c4-003e-33aa-aeb1-9dd7648c227c | -3.2569 | -54.2226 | 2024-11-23 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 66436685-eeaa-3e7d-aa8e-ec198cba9483 | -3.7538 | -50.0152 | 2024-11-23 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b6ff0099-bf0d-3b1e-9424-971d687b1610 | -3.2543 | -50.1378 | 2024-11-23 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 594f2127-d704-304c-b855-f4e4215b6ecc | -4.6271 | -46.4992 | 2024-11-23 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 46a9c8fa-0786-3776-8d09-fc6ea6b4a575 | -10.201 | -36.2386 | 2024-11-23 01:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 9c8f48ea-bda6-350e-86c5-1ad0a7149ea8 | -3.4662 | -48.2565 | 2024-11-23 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7f3d5706-c8a5-3128-984e-98e778d34ba3 | -6.5054 | -47.0414 | 2024-11-23 01:30:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1214961d-0457-3a76-80cf-b673cc1bc90b | -2.8308 | -45.1719 | 2024-11-23 01:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 11016387-9b92-356f-9f4a-a6ca9272f7a6 | -3.2569 | -54.2426 | 2024-11-23 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 39a31b4a-bc61-3f18-b47d-1d806402ff42 | -3.2569 | -54.2226 | 2024-11-23 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d7f7e284-010c-3d49-9ba8-760ed76b913e | -4.59 | -46.479 | 2024-11-23 01:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3b3be91c-295c-35e8-9b31-663e854ec96f | -4.706 | -45.8493 | 2024-11-23 01:30:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7d73a474-512f-379d-ae5a-3c6e68acebd1 | -1.6075 | -52.5977 | 2024-11-23 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f4e4205f-7f32-317e-b76c-75f68135c8fa | -3.2385 | -54.2431 | 2024-11-23 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| ef5ff38c-0d3b-3284-b8ff-32f1aa90f020 | -4.5215 | -42.9312 | 2024-11-23 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| aa2a4fa0-2f3e-31fb-9d04-f50551c4cc11 | -4.6086 | -46.478 | 2024-11-23 01:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 6c2b8b17-4471-3945-a413-f6cf0f89b65a | -3.5159 | -53.8132 | 2024-11-23 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| aeea5ba3-33b0-3663-a6e9-c014ee2827b1 | -2.6963 | -46.2719 | 2024-11-23 01:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 91cd363f-df75-3174-8ab9-e542eba8bcf2 | -3.4747 | -50.4245 | 2024-11-23 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6dfd1ed9-4ba8-3db3-b55e-438f717ed23c | -3.2386 | -54.223 | 2024-11-23 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 29dc22d3-f2ce-36a2-8bf9-521b83c8c3d8 | -4.5402 | -42.93 | 2024-11-23 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2553b3eb-a14d-3c9d-b991-afa3e9893a17 | -4.5568 | -45.88 | 2024-11-23 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ac6f6574-d5c6-379d-90cf-555d12328206 | -3.2544 | -50.1168 | 2024-11-23 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 61e166d7-cbee-379a-ab87-1b763da46ca5 | -4.5216 | -42.9078 | 2024-11-23 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 67097d19-7228-38f1-a21d-de54383cf16e | -3.6306 | -45.1399 | 2024-11-23 01:30:00 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 30db941d-7012-3604-99f3-3f317000c751 | -4.5403 | -42.9066 | 2024-11-23 01:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 5bba7677-eb57-34a7-86a9-5e797d59766c | -4.6085 | -46.5002 | 2024-11-23 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 214.5 |
| 636a63cb-7e50-3301-812f-3ed254a97c56 | -4.5898 | -46.5012 | 2024-11-23 01:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5f9b247c-9e5e-3217-bf04-1dbb88228ff7 | -3.9755 | -46.6424 | 2024-11-23 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 87cc5594-7a03-3c35-958f-f799719fec0c | -4.5403 | -42.9066 | 2024-11-23 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| e7723781-89a8-36e6-8f02-d1868aed8234 | -3.2569 | -54.2226 | 2024-11-23 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| d8f82c74-beae-3d06-8fcf-b3152eb3689f | -3.5159 | -53.8132 | 2024-11-23 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4e376133-ede1-38aa-8f99-27156096b995 | -3.2386 | -54.223 | 2024-11-23 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| bd64ed9c-5a6e-3635-a49d-e8141d1e89c8 | -4.5382 | -45.881 | 2024-11-23 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f36a42d1-fa98-30f1-841a-5896e41b3e0c | -3.1831 | -54.3247 | 2024-11-23 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 31505cef-1e39-37d4-8d3b-a1700843d9eb | -3.2768 | -53.8199 | 2024-11-23 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c913bf7e-736e-34db-bf8b-13e3e481ec73 | -3.2385 | -54.2431 | 2024-11-23 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 1f725181-4fae-3e12-86dd-d3ccd2a30993 | -4.5216 | -42.9078 | 2024-11-23 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 10715fb7-98b8-3d05-955f-b37dfc4464f8 | -3.516 | -53.793 | 2024-11-23 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a1965c58-705e-31f9-9ddd-cda6ef832fd5 | -3.2569 | -54.2426 | 2024-11-23 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 30ec8b2d-5028-3d09-a411-4f30920835dd | -2.7149 | -46.2713 | 2024-11-23 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6be70dc1-e215-3c16-9d5f-eb2df7e34766 | -1.7175 | -52.7184 | 2024-11-23 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7aa3d16a-099b-36e7-a654-573582990cb7 | -4.706 | -45.8493 | 2024-11-23 01:40:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8691d19d-de45-33b1-a50c-63b7ae414aa1 | -2.2059 | -48.9168 | 2024-11-23 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |


[Clique aqui para ver as próximas entradas](README17.md)
