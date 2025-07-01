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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e02cc9-62bc-3e64-83cb-4d40a467df7a | -9.17982 | -48.84284 | 2025-07-01 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b299c3ce-5201-34bf-aa06-3b05a3c6b7f9 | -9.23473 | -58.75096 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e14f4e6-74db-3bbe-90c3-37e062e83b91 | -9.25374 | -58.74948 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1317bce5-fb3a-3170-bb1d-13ee55fe8494 | -10.28513 | -52.83081 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e57e2fc8-4a03-3121-a570-b2efb771df8a | -5.14848 | -49.34195 | 2025-07-01 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d67b8e16-4094-38be-ae69-4368de3d4605 | -6.54382 | -54.9712 | 2025-07-01 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9cc8b92-8476-3c42-a52f-b79b5e5a815b | -9.26085 | -48.20742 | 2025-07-01 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd03ea7a-1878-318d-b9da-ca4c4631f454 | -9.97397 | -48.23743 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 53850e8d-91e3-37a0-bbdc-61fe0d13c736 | -11.204 | -55.91795 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b739f96-ad41-38b1-9dba-d489ff7ad882 | -8.72404 | -47.9919 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 28d788e1-0cb1-3f53-9c8d-aec5ad08ce7a | -11.57965 | -54.57065 | 2025-07-01 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c13d291c-0389-3f5e-bc53-77b341166145 | -8.86059 | -47.95533 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bc84748-0d96-3e0d-a215-5caf4bf5912f | -10.87158 | -53.73932 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b5537d7-f77b-3afb-9df6-10db9d38e82b | -10.30284 | -57.12545 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb3f423-7585-3384-ac14-8e257dc47979 | -10.55032 | -52.03408 | 2025-07-01 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a42b4387-5ae2-3d07-84d5-671f8df4c509 | -6.29215 | -43.68355 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 83b18ffd-99a8-31c8-911c-f5508984d4e3 | -7.31983 | -46.73139 | 2025-07-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c904b88b-9435-3753-ba51-70702f21d0e8 | -9.13088 | -49.67834 | 2025-07-01 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc09b169-96f6-3ec0-8c6b-f12733f66a71 | -7.16456 | -49.5118 | 2025-07-01 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4030694-9726-364b-8911-85668b012852 | -10.0851 | -52.74022 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f4aecb31-93a9-3237-8c27-79f4d01f1e15 | -10.87579 | -53.77764 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e0658b-252f-3c61-a4e4-66ddd663fc7c | -6.21471 | -43.36359 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10dbd311-68a2-3633-b245-e4e0c2fa28d4 | -11.13748 | -43.32479 | 2025-07-01 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88d5c64e-6419-35db-8fae-15316c5b97c8 | -10.03159 | -48.66209 | 2025-07-01 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70fbbe83-05b1-3b05-bf4c-7ed4e655bc95 | -10.62194 | -51.79154 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e43e09be-d04b-3e02-96e5-ae77fedee326 | -10.12986 | -52.34884 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33be46c7-8cc1-34de-9b41-63e3f1db5578 | -7.62072 | -45.75513 | 2025-07-01 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 502ec78b-6941-3bd1-a789-6639cb17788a | -6.56902 | -47.37009 | 2025-07-01 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9df47ec-2e39-3135-a95b-1b85cfbf1f1a | -6.54753 | -54.9718 | 2025-07-01 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a2f4fd6-abf4-3815-838b-51975583ca4a | -11.83421 | -47.50345 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c4b99a2-45fb-31ec-91d1-7bee6cc0fe51 | -11.20031 | -55.91734 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61148ad1-3f80-3543-9b2f-84bfdf853fe1 | -7.01501 | -49.18042 | 2025-07-01 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71929e70-c7d7-334d-8a31-1b74e3a18a29 | -7.2483 | -46.40172 | 2025-07-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0bba4d8-d430-365c-ab85-32c03d41d3ea | -10.65465 | -44.48914 | 2025-07-01 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3706c8c4-1c47-3306-84f4-203766987d5d | -12.01765 | -47.76524 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0c1e1503-2d05-3327-b0ef-0e56824a985f | -6.29691 | -43.68417 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7464d734-55f8-378c-a70e-b09d13f5ed6d | -10.88126 | -56.45243 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7bcbc318-52a9-3037-a9af-4f029a5ccdf1 | -10.87935 | -53.75561 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f1d05c1-75b4-372d-8c1b-37a6adf0e679 | -11.12533 | -55.44447 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f22062f-2009-3bb5-b4d6-8528487f14b1 | -6.28667 | -43.68802 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 712435e5-c563-387b-abac-7c2f03cc1e43 | -10.8742 | -53.76606 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 622b4190-4dce-3de8-88d3-0b1d86b2806c | -12.28598 | -50.10852 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df0f46a7-05d6-39a4-a8d0-736b92ab2242 | -7.61708 | -45.75061 | 2025-07-01 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f54a0f1a-f96d-38cd-a4b1-15b801306771 | -7.97006 | -45.9373 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7dc53ff-a0ef-3c59-9c18-d26590fae1cb | -10.12916 | -57.77856 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b7a6bee-a466-3643-9da1-757a87356ca3 | -8.08495 | -46.87423 | 2025-07-01 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6fb3a7e-a6e2-3aae-a7f2-b091f4a4d449 | -11.57663 | -48.14533 | 2025-07-01 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15761340-2d1a-3c70-85ee-4b8b7e40a9a9 | -6.21141 | -43.35174 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7f19f825-a85f-33ca-b5c9-4efcb52d5086 | -10.87875 | -53.75927 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fe10815-b1f9-3bd0-8c96-1e3b227e2bed | -10.08786 | -52.74428 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 46fbfddd-0cf0-340b-aa8e-078a5b7ef93f | -9.65814 | -50.74086 | 2025-07-01 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab455b0d-8aea-3c1d-a1a0-ccf717ef3608 | -10.87496 | -53.73987 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa3e723-6ae6-34e6-8139-a41fef4c3d5e | -10.87892 | -53.73678 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 466f01df-3eb5-328e-8a61-37b48a2ff367 | -11.14021 | -53.92673 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c21f694-6830-3cb5-b37b-38b70fdd543b | -9.68264 | -48.33973 | 2025-07-01 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4384a8ad-45fe-3f41-abc9-e604532e3802 | -11.19662 | -55.91674 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0275d501-94ca-3a0f-8ef1-145e0ea9bf9b | -6.57027 | -47.37231 | 2025-07-01 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1f3a082-80ec-3a8c-9131-03ca27cdd6e0 | -9.2492 | -58.74864 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42bd9c1f-2505-38b4-ac99-d70f81f43817 | -12.29427 | -48.80909 | 2025-07-01 04:46:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce01dae1-1671-3d5a-97d5-35a667256666 | -5.67458 | -44.82965 | 2025-07-01 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd6f8feb-5d88-3377-b4da-67cf7a6a3e28 | -8.97726 | -49.85909 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfbe67af-b690-3a53-b207-6cc71661d55b | -10.1238 | -52.34429 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c08e3a7f-2222-3b50-b605-eed13f1d1397 | -10.82118 | -56.95058 | 2025-07-01 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac47492-a6d0-32a2-9e35-4cff8e3feb6f | -10.17106 | -51.65187 | 2025-07-01 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9b641ab-9e7b-31f0-ba6c-4656b389a77d | -10.07791 | -52.74268 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b97f1a8e-1dcc-3b84-b1de-715d22423e38 | -9.97464 | -48.23284 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3325078c-888f-3fa7-90d1-aac6eecc066d | -9.24466 | -58.74782 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa76ea3e-3d41-390c-a540-70653688787e | -12.29362 | -48.81357 | 2025-07-01 04:46:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebb6b2e0-cfef-39ac-8b29-4fb0b915e20a | -10.35031 | -57.50451 | 2025-07-01 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e34e6c-416a-3ab1-9f68-72714c984295 | -8.37681 | -51.071 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8007d2b4-03e4-384b-8f48-0c01cd7adfe8 | -10.87524 | -56.4416 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c8b3c097-e6af-3952-9d23-9acee96d04c3 | -10.82005 | -56.95361 | 2025-07-01 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e607e5-6dc9-3ce2-be65-76276a625162 | -10.07459 | -52.74215 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 772fc8fd-e4a7-3ce3-a8ab-3636015fccf3 | -10.88272 | -53.75617 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0a9241e-7506-3409-9902-30133563b6ee | -12.02012 | -47.77606 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f9d727e0-1f4b-3298-b358-2b389fa08e63 | -9.25002 | -58.74401 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1a3de54-ef01-3f52-86a2-e386d5232049 | -6.54309 | -54.97565 | 2025-07-01 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9888db6d-72aa-3177-b540-357b0f890229 | -10.12655 | -52.34831 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19a30341-1817-37a7-b23f-4cc20633dfd5 | -10.28838 | -46.72905 | 2025-07-01 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1daf22c4-4238-33af-b040-2585705b7a77 | -10.06895 | -49.65929 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21f92681-f676-3bd1-b93d-7056e990efb2 | -9.08504 | -59.47675 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff40b737-ebd1-3c24-ad64-64581668e5d0 | -10.6866 | -47.20676 | 2025-07-01 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c94ebe97-4856-376e-85d1-695c51a68472 | -9.24975 | -48.33233 | 2025-07-01 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e942c350-0756-3247-b964-a30c55b9bf1f | -9.02846 | -49.58995 | 2025-07-01 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fe3b7b-42f9-3e34-8b90-7e6a7fd04933 | -10.65238 | -46.82914 | 2025-07-01 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d85d5a02-a1e8-312a-bac8-664e3b008f9d | -11.83746 | -47.50922 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a2bbfe8-6b77-3635-944c-40abe34b2119 | -7.54658 | -48.5861 | 2025-07-01 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea94e87d-0400-30c1-a7fd-60f3ca674cdd | -11.1427 | -43.32553 | 2025-07-01 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1dbf20e7-11e0-3376-8666-03f53f6b9671 | -11.58183 | -52.11395 | 2025-07-01 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6a0558e9-af1a-36ff-8496-3be9007889fb | -10.07846 | -52.73915 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68cef345-444b-3884-a242-de23ed63706f | -10.02564 | -54.31794 | 2025-07-01 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55bc5ef9-dc40-3d83-9cd1-956834601d0c | -9.23723 | -58.73692 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7dca625-6b61-3daa-8ed8-bc09ead52c2b | -12.28251 | -50.10799 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51a44376-af44-3cde-a32b-773400832688 | -7.71666 | -47.84509 | 2025-07-01 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c33365-8a5f-31c3-9e28-0b49c28ef896 | -9.08982 | -59.47762 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5987fe11-3d39-3dd4-9434-fd41c2e74130 | -10.88213 | -53.75984 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f49c7aa3-9915-3444-b94e-431ba5d02bbb | -11.58028 | -54.5668 | 2025-07-01 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c46de26-6bc6-30e2-b763-df0861c1db13 | -12.28656 | -50.1046 | 2025-07-01 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d25b65-29c9-3f07-b541-77953eecc6bf | -9.5715 | -49.10836 | 2025-07-01 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 218aac80-a6cd-3102-b362-dba5edec8765 | -10.54978 | -52.03757 | 2025-07-01 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
