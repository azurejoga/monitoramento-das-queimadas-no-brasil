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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19aff341-4b50-3638-a484-48a02c4b316f | -2.7464 | -52.963 | 2024-12-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 0f492860-126b-3861-ad2b-155f7131a8fc | -12.5499 | -57.6996 | 2024-12-13 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d66438ee-f78b-342b-80f5-195a32cb8e50 | 2.5434 | -60.7357 | 2024-12-13 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 45f6b1fc-b0c3-3dd8-abec-1821831de3ea | -13.0641 | -52.0538 | 2024-12-13 00:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 73f32db7-a07a-3338-b3b7-cd4742598151 | -3.2686 | -46.9142 | 2024-12-13 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 3cd55d12-5b1f-3e9b-b2b4-cc566f835231 | -2.8196 | -53.0832 | 2024-12-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b0548ca4-b46e-37dd-95ab-767bdc7f33f0 | -14.7848 | -52.642 | 2024-12-13 00:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a2c84a35-bc6b-39ab-a568-92bf799da2bb | -11.2151 | -53.8125 | 2024-12-13 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 704718f0-4fa8-3cd1-a133-534772ca4358 | -6.9346 | -43.5168 | 2024-12-13 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 249.1 |
| d9e8a2fe-b3ee-3922-88a6-98847e03dcc5 | -14.7655 | -52.6446 | 2024-12-13 00:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c5983349-ca04-381b-a6d0-526c58f09bd0 | -6.9158 | -43.5185 | 2024-12-13 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 262.5 |
| a227926f-b214-3c68-a72d-31856b76922c | -2.5108 | -51.8023 | 2024-12-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 2f71fc0b-6a84-353e-9e66-b7df266ef2b1 | -3.2935 | -45.6041 | 2024-12-13 00:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| dabf8adb-15b4-341f-bd9b-131633606ea1 | -2.1173 | -54.6472 | 2024-12-13 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3291691e-65ba-3f0c-a0e4-5a4fa2c1bbaf | -2.0076 | -54.5092 | 2024-12-13 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 77b5265c-014b-3efe-9110-a05f5de9a919 | -6.9349 | -43.4934 | 2024-12-13 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| c88c912a-8260-3bed-8b1a-65744f3d89c2 | -2.1173 | -54.6671 | 2024-12-13 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1e10180d-f6ac-3d06-a52d-019ac08192de | -13.0644 | -52.0326 | 2024-12-13 00:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 400478a8-4a6f-3d31-aa8f-45de67dbb416 | -3.2685 | -46.9362 | 2024-12-13 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f72b19b4-9199-3c20-9fef-7bf6c1deadcc | -12.5495 | -57.7395 | 2024-12-13 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a77b87e2-9371-38c6-9dfa-f44f7af5e7c9 | -13.0453 | -52.0349 | 2024-12-13 00:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8805fd79-62ff-3d39-b35e-12bb575eb079 | -0.767 | -47.7567 | 2024-12-13 00:50:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3dda95bc-12fc-315d-bac1-4261f8164ebb | -11.1959 | -53.8348 | 2024-12-13 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 76d2c7dd-4af9-394f-bb6d-2fb6b8396590 | -6.9161 | -43.4952 | 2024-12-13 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| a0b52d8d-42bd-39a2-bdbb-dcb673808ded | -5.2108 | -43.3067 | 2024-12-13 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 39ebe5e8-36b6-3d5b-a8ae-9f283fc08633 | -11.1962 | -53.8142 | 2024-12-13 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8812d1e8-8bba-3741-bd7d-f2d032e0af89 | -12.5307 | -57.7211 | 2024-12-13 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bf0fafb8-1e9b-3b9a-ac4a-677a911bc769 | -0.7486 | -47.7569 | 2024-12-13 00:50:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ca684ab2-0256-352f-977e-83075d3a6d49 | -13.0836 | -52.0304 | 2024-12-13 00:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 04db0969-68e8-303d-9db9-cdc80c8254fa | -2.4923 | -51.8027 | 2024-12-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 0158ed8a-ce9f-3445-ab12-df460c920889 | -11.2148 | -53.833 | 2024-12-13 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 80448e7a-5e82-3b2e-a7b0-7fc2cd265efb | -2.8196 | -53.0629 | 2024-12-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f26ec26d-310a-3890-991f-8fd387d89098 | -5.211 | -43.2833 | 2024-12-13 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 900b6f1a-5091-34fe-a1f9-5d43156d99be | -2.8196 | -53.0629 | 2024-12-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7ed87172-4a89-3627-9fce-218c1b5c7b57 | -14.7655 | -52.6446 | 2024-12-13 01:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a7527640-23c8-352b-aefd-2ddb13c89f41 | -11.2148 | -53.833 | 2024-12-13 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 02accfcb-579e-360b-a15a-10c5aa9dec48 | -3.4784 | -45.7979 | 2024-12-13 01:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 35d3c56e-7807-34c9-be96-eda6cf84fa27 | -11.2151 | -53.8125 | 2024-12-13 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 50f21568-e7a5-310c-8c01-9bf017cf73f1 | -13.0644 | -52.0326 | 2024-12-13 01:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 5526e260-d958-387b-ab44-f346b56761f0 | -6.9158 | -43.5185 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 1e4e3e27-3df1-34a6-aa36-a6a7ff871c20 | 2.5434 | -60.7357 | 2024-12-13 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ef32e63f-598e-30e7-8bb1-5582ecc005d8 | -1.62 | -46.6747 | 2024-12-13 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1a2660eb-7823-3cc9-8540-2ca5c708377d | -11.1959 | -53.8348 | 2024-12-13 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| aa994805-b873-362b-9aab-191a8e709ae6 | -1.62 | -46.6526 | 2024-12-13 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| b1018ae9-e3cc-3037-b197-908366edf7ea | -5.2108 | -43.3067 | 2024-12-13 01:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ef5f58f0-dbf4-36b8-bd40-848b9327f58e | -2.7464 | -52.963 | 2024-12-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| eaa75a22-d2af-3c1a-9a52-7e574b520274 | -5.2296 | -43.3054 | 2024-12-13 01:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b208a7a7-2726-3569-9e51-799d20c0881e | -5.2298 | -43.282 | 2024-12-13 01:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 7fe8db6d-a3d3-3b37-9807-510a22345f37 | -3.3301 | -45.7146 | 2024-12-13 01:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9552158b-011c-3dbd-8f6a-47a94890911e | -5.211 | -43.2833 | 2024-12-13 01:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e8893653-8ae3-399d-8a1b-bbd022bb6848 | -13.0641 | -52.0538 | 2024-12-13 01:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 706d6799-216a-3aba-8e34-4cf29277339f | -2.5108 | -51.8023 | 2024-12-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0c905484-674e-3094-afc7-a3bdf95936b7 | -6.9349 | -43.4934 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 129ff0b9-42c5-3a50-88a7-fb531b02ccc1 | -4.4595 | -43.7494 | 2024-12-13 01:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1f0d8a92-aa52-3caa-ba3d-b6ff8c38b3b4 | -2.4923 | -51.8027 | 2024-12-13 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 38acbd09-8758-3fef-86f7-31e741c74f00 | -6.255 | -35.1982 | 2024-12-13 01:00:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| dfdd4b90-28c7-36a5-bf32-f7c7a004274e | -14.7848 | -52.642 | 2024-12-13 01:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 12151c21-6a99-3639-a493-d0b0a27e4573 | -13.0836 | -52.0304 | 2024-12-13 01:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1abd9e33-25cf-3321-8a9d-68429e4f16ae | -6.9161 | -43.4952 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 584b732b-1623-33f7-b9e1-fd796e80761d | -3.15 | -53.2776 | 2024-12-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 698c1f54-c65e-3774-801b-b5e37bcfd24c | -2.1173 | -54.6472 | 2024-12-13 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bc5e24b6-b080-3a9d-aad0-c3ec345c49a6 | -6.9156 | -43.5418 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 7c212a5a-a76c-3cfd-bc2d-5d18233cf1cf | -6.9344 | -43.5401 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c164762a-ca18-386a-8f59-d3ec4d53bf42 | -6.9346 | -43.5168 | 2024-12-13 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.7 |
| 2c0e9d25-67c5-361c-b67c-e9d7507f82e3 | -11.1962 | -53.8142 | 2024-12-13 01:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| ae16a1af-a8ce-347b-bbf8-2db6561ae7b4 | -12.5497 | -57.7196 | 2024-12-13 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bba9ad8a-bef4-3e79-a0eb-9dd98916544b | -2.8196 | -53.0832 | 2024-12-13 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a283bc77-5b74-3d5c-b8dc-b3c9c86771aa | -0.7486 | -47.7569 | 2024-12-13 01:00:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b2560f9a-85ab-3c6b-8875-602898906583 | -6.92 | -43.47 | 2024-12-13 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9c84d03-cad7-3541-b0f4-0ee4aa860f38 | -6.92 | -43.52 | 2024-12-13 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 924219e4-a109-326e-bdbd-34720236bca7 | -6.9 | -43.51 | 2024-12-13 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44f8984c-13e1-36d4-85b5-5a9812c353e0 | -5.2108 | -43.3067 | 2024-12-13 01:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e4d1cc57-4deb-3bf8-a858-1d76d0449f3c | -6.9158 | -43.5185 | 2024-12-13 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 406.6 |
| 0b59e37b-2254-3224-a604-c479d81f03f1 | -5.2298 | -43.282 | 2024-12-13 01:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| d3c0288e-5922-357a-bf5f-d43c11648c36 | -2.4923 | -51.8027 | 2024-12-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 8c1b54b2-ab69-312c-9aa7-ac82f61c5bbd | -2.8196 | -53.0832 | 2024-12-13 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 550391a9-4b6c-3a4f-a035-99c601206310 | -0.7486 | -47.7569 | 2024-12-13 01:10:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| cf081288-994c-379b-9399-3afffe5632a1 | -6.9346 | -43.5168 | 2024-12-13 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 283.9 |
| ca256dc9-9e78-3197-b2f2-088f7b570e8a | -3.3302 | -45.6922 | 2024-12-13 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0e86bb08-4c7e-364f-a4eb-4abe5dca5d32 | -3.3301 | -45.7146 | 2024-12-13 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 13c6207a-8f6b-3771-97cd-60d7c9b137fd | -1.62 | -46.6526 | 2024-12-13 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| eaa4cd0e-ebfe-3603-acb3-3ac463742da6 | -2.5108 | -51.8023 | 2024-12-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 401b2174-6302-307c-b319-298a40de8bee | -2.4923 | -51.8233 | 2024-12-13 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 4e508c27-629e-3298-bd30-8e2b67cccabd | -6.9161 | -43.4952 | 2024-12-13 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 05708ef2-e68b-39ae-b371-75840993a9a5 | -13.0644 | -52.0326 | 2024-12-13 01:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| f11c360a-22bb-3b50-8b32-1ad81ed95834 | -2.8196 | -53.0629 | 2024-12-13 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f9bed137-8008-3eae-9e51-7a650f158bd6 | -14.7655 | -52.6446 | 2024-12-13 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 48755fe3-77ed-3f49-a5b4-630924bd3dc8 | -6.9156 | -43.5418 | 2024-12-13 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e41064f1-c554-3645-a45a-21cb5b8174a2 | -11.1962 | -53.8142 | 2024-12-13 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 36ca5d64-7741-32af-ae5d-07b7312cc9e9 | -1.62 | -46.6747 | 2024-12-13 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 55a836cd-3135-361f-aad8-63898ce700f8 | -13.0836 | -52.0304 | 2024-12-13 01:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 16986c7b-867e-3a64-8f96-b925a51a1532 | -5.211 | -43.2833 | 2024-12-13 01:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| ca098f2f-20b7-39a6-9095-8dc357af78d0 | -11.2151 | -53.8125 | 2024-12-13 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 52cb0a43-3bee-3f23-8502-78a91ba873a2 | -13.0641 | -52.0538 | 2024-12-13 01:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1069378b-b3cc-3e9e-9203-6dad60a33cec | -11.2148 | -53.833 | 2024-12-13 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b02fc226-9a04-3b95-9033-8f65d59e4e5a | -11.1959 | -53.8348 | 2024-12-13 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| dc168de4-a193-399a-b90e-7d3893277876 | -14.7848 | -52.642 | 2024-12-13 01:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f6f9114d-48fd-35c5-b6ad-72da04f67d19 | -6.9349 | -43.4934 | 2024-12-13 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 0da0823b-3aca-30b0-b0bc-c5ce4eb4b733 | -2.1173 | -54.6472 | 2024-12-13 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 937349a9-4d14-3ad8-9799-469d62cb761b | -14.7848 | -52.642 | 2024-12-13 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |


[Clique aqui para ver as próximas entradas](README6.md)
