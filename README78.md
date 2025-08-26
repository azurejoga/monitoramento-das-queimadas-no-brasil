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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14cfc5d2-90c6-3576-9ea9-e07895e4b50e | -7.35325 | -59.66215 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce930aed-3a0a-326c-a467-f73023750024 | -7.36028 | -59.66817 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b5bb3135-89f0-3ddc-a77e-4bde8817b34c | -7.39567 | -64.34486 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9af9ffbf-3900-3bdf-837d-dab6dc9df915 | -3.98337 | -51.06148 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af160a8d-95a1-3df0-8775-25cd1ed46197 | -4.96667 | -55.81954 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 49d241bc-1a42-395c-a559-3437b145e84c | -7.35712 | -59.66271 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a93af3cc-a35e-39ae-925b-bce4b581a0c4 | -7.38082 | -64.35317 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d66e78b6-3e46-30d0-acb3-3c231e8128ba | -8.22434 | -61.41722 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a02c80a-7a68-3937-bcd3-4fc8d7e33599 | -8.10944 | -62.87187 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62f29523-61dc-3b15-bc74-a94c53c2ce8d | -7.52936 | -50.5443 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc1cdfe1-617e-3575-afa4-4af724ac3011 | -7.38412 | -64.35369 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70fe0bfa-335d-3b77-aceb-d198065c2074 | -6.57772 | -59.88104 | 2025-08-26 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15770222-cd7e-3806-973a-b27136dd1ee8 | -7.39019 | -64.35819 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9257ffe3-27c8-3f26-a052-e838c048a38f | -7.88816 | -63.01019 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ae3fb8d3-3935-3266-910b-d5d7923a75c0 | -7.54343 | -63.85792 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0e78de3-3939-349c-a150-e3a31e549b02 | -4.70621 | -56.06627 | 2025-08-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93891c94-449a-3c08-aa5a-7ae522b8586f | -8.10685 | -62.87555 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24ed6e38-a944-3b8e-ad2d-72e959ba73c3 | -7.39513 | -64.34833 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa7cb1fc-5f3e-360e-a061-fd319412a5a0 | -6.24694 | -60.01958 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 346f7a38-3678-3bf0-9f3a-68b4cd396e27 | -5.3102 | -60.19868 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48183eb-3b84-3f09-ad81-2720fd105f2d | -7.28908 | -59.66785 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b79bb72-7a15-3125-a1d6-128e87e3f15c | -6.76805 | -59.66308 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 15fde043-cdff-3a53-8ef7-71e77d6b4af7 | -6.91587 | -59.36225 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1cfac514-7366-37d3-8add-94f097bf6a34 | -8.12627 | -62.87447 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e4e40c1-c10b-33a3-a2fa-f3525bb8929a | -8.1078 | -62.88268 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd9dc2ce-182f-33e4-8e40-4f9784d29f77 | -6.25292 | -60.01363 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb8c556a-648b-3ace-8a57-1611ce385929 | -6.774 | -59.64921 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e02ce71-b621-3d66-aaa3-28f9ec6c9278 | -7.88481 | -63.00967 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 46687d0a-be7d-3de4-81f8-96541a853dba | -5.32118 | -60.20034 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8731d6d5-d034-38ae-90e6-71a36c6b3a18 | -7.53308 | -50.53265 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 037660f7-7b2c-3ca7-bec1-1bdf43226820 | -6.70241 | -58.55614 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 885c4ed4-1c7f-329d-97cb-e3c8de83f7e9 | -7.38906 | -64.34383 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73b18bf6-ac70-3590-a52d-34c7e8e2c77c | -8.24384 | -61.45754 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0967b66-5d8c-3a15-a28a-17738c474984 | -6.76414 | -62.87365 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79b05424-487d-37ee-979d-d2004b275d14 | -8.11726 | -62.8657 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 768b1141-7e4a-3803-b823-240cd2d9cac1 | -8.11117 | -62.88319 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1776fc23-eaf2-3784-a0f9-9b29b5373157 | -7.62203 | -61.03549 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aaee04be-e1b6-3c9a-9167-37ec86c06555 | -7.47379 | -61.33278 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57e05841-608d-303c-93ea-c2b69729e4fd | -7.39236 | -64.34435 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d727d95-58d7-31fb-a67f-4fe275890952 | -7.62025 | -61.03616 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80bdeceb-627e-3ae9-abd6-3e32297e1055 | -6.24626 | -60.02407 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6d559aff-d95e-30a6-a381-ae32465f6cf6 | -6.63384 | -58.5455 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d83549bd-d4b1-3847-9cc1-f9e5f814f6d2 | -7.5382 | -61.38619 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52a0ce23-5bb2-3dd7-940b-6bcd7cc1f25e | -6.68821 | -58.85891 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 651eaa89-95f5-383b-b9a6-971c805f9e8e | -4.96107 | -55.82412 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7caeeab6-4a13-3072-b1b4-aadda4393cdf | -7.38965 | -64.36166 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d106774-7190-3ef4-bada-417041e99268 | -7.38136 | -64.34971 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27a0a181-b106-3c46-af06-b6976ff841b3 | -7.54558 | -63.84405 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cac06c00-1c1e-3b4a-b182-3baf1f41e4b9 | -5.52849 | -60.2153 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72b3fbc2-1214-39aa-b299-a8901845a2ce | -5.3145 | -60.19495 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cf9547b-0a45-3345-9e70-69b5331e6775 | -6.24252 | -60.02352 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3dd5b620-0b9f-3d6b-969d-c71f68c90146 | -6.26171 | -60.00578 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49458440-2a4c-3868-9289-d80742de210c | -6.77784 | -59.64985 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc5ced2a-9679-318a-82b9-456ab4d7d30e | -7.31693 | -59.61183 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d971ac-c1cf-326b-acbf-1b5336fd7d1f | -6.91515 | -59.36726 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 47758131-4d33-33fe-a351-32f46e950491 | -6.30935 | -59.86372 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88346112-2191-331e-bca2-0f7e4d90cf11 | -7.3786 | -64.34573 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 10541d74-3ceb-3c1f-a1f5-4e41b332d4ff | -7.48164 | -61.35305 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2a0fb33-a0ef-3a62-9ab3-586892bb9cb7 | -8.12908 | -62.8786 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48e2e602-258a-3e40-9081-fa226b28530c | -6.23638 | -60.01348 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bc55692d-06f1-3e66-8b3a-05334e1b6dab | -6.26479 | -60.01089 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6edfd24-bd3f-3e73-b9c5-27f04fcda33f | -6.91659 | -59.35723 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef93431a-952d-3c34-a0af-fe2b1d3984df | -6.69226 | -58.85946 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d963ed8-2b46-362f-8d31-d9f5a6b0dfe7 | -7.56381 | -63.85755 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 355070a0-9677-368a-9bcf-7694189f9545 | -7.53017 | -50.53766 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b1dbf41-78fa-33df-8946-bc37b3acad75 | -3.97787 | -51.0557 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e1e36f2-1803-3674-874a-62c19706f211 | -7.54997 | -63.83763 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 430c6806-0791-3ad6-b660-ae2c073a1c7a | -6.24999 | -60.02465 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdcf0494-850b-3089-a060-c995cb834301 | -7.62442 | -61.04436 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d59ebce2-4b92-368b-804a-ceb87cb9c881 | -7.90138 | -61.52334 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2ca8b30-f927-32c5-81fe-c32c370bb903 | -7.55773 | -63.85305 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9275e3-9596-3065-9f10-034fc05616b6 | -6.2602 | -60.00783 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ecc27da-b70b-32aa-94c5-ea6545c550ab | -8.24798 | -61.45406 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d128aa33-2795-3cf1-8f48-ce5405dde5ba | -6.83483 | -58.96305 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fdbb897-7abe-36ab-a825-ca34a9f9f7ea | -8.24739 | -61.45806 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ecf082a-7eaf-36f2-b784-08c30142635f | -7.35641 | -59.66758 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 194c6a93-66b6-31a7-8715-ad008c51ec40 | -6.7901 | -59.64675 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44be1a22-651b-38b9-860e-13ef44f5d77e | -7.47811 | -61.3525 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8058b5c0-7d48-36c9-95cc-84f07916a37a | -8.10293 | -62.87863 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad8587f3-eba1-30c1-804e-bfa56e4af8f2 | -7.62082 | -61.04381 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b294d6cd-b344-3b41-8eb7-aa9d9652bc10 | -6.91267 | -59.35663 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce42753e-26cb-3a49-92fb-692219246c74 | -7.47987 | -61.36502 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9dba1ca-3d7e-3bdd-9c3d-68360f7d8f7f | -8.1063 | -62.87915 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7993d357-4df8-3dbe-bef2-0063cb8afc79 | -5.30159 | -60.20612 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05854a71-fa34-3eb3-a268-4e9ab8a977a7 | -7.65317 | -63.52252 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcab4d79-b525-3f79-b0ea-e3c1ecd6307a | -7.38521 | -64.34677 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2207fbd-2214-3dc3-94f8-2437f8ac66e4 | -7.49941 | -63.50536 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4900dbc-9c34-3512-a7bd-eda84f2c7d42 | -6.25645 | -60.00726 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b5b7b9-d09d-3dc4-a9bb-7434ef3205e4 | -7.65594 | -63.52653 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a25fadc4-edf8-3c3e-84c1-27c611e05203 | -5.53346 | -60.20722 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048c5ba5-2ab5-3232-aea7-f4f0a1c6c05d | -7.31304 | -59.61124 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aa0e1d6-4dbf-34d8-8036-bf597f2e33ea | -7.56158 | -63.8501 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6333f311-3eb2-3a4b-a4cf-0cb5a9991efd | -6.34404 | -58.18766 | 2025-08-26 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbfbfde9-fb91-37bf-bb91-b73caff486a5 | -6.30868 | -59.86829 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1c49690-3731-35d8-a9d6-93cf47cc8537 | -4.70147 | -56.06548 | 2025-08-26 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a624bdcf-8b09-39f1-93c5-2ada42e4f3cb | -7.39074 | -64.35473 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7af9ed-3a0a-3fff-9b37-7b9344120db4 | -3.39155 | -59.45105 | 2025-08-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a169652d-836b-3fa8-9fd4-e0e46f3c354e | -7.53723 | -50.5385 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30115950-433a-3cb8-a0cf-93b28f7e499c | -7.65263 | -63.52601 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c102fcdf-afbb-3c58-b381-befa1760952f | -7.65529 | -61.4728 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README79.md)
