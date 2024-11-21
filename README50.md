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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01638f28-b299-3057-a977-070fd9c8f659 | -1.75515 | -52.37369 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83f3bc71-9a9d-3cff-8fba-4e159761c86d | -3.11792 | -45.44812 | 2024-11-21 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 745536b1-5c31-3a4e-bc63-ae65c749bc78 | -2.12463 | -50.27217 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc63af4-b7eb-3e0f-b8af-9a44d20919c2 | -1.06725 | -48.0101 | 2024-11-21 04:53:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21f86786-c234-3acc-a25f-7151d75ae495 | -2.94942 | -48.33509 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1693c5a-2e21-3eb6-b14f-12afed3e5c98 | -1.70955 | -52.49039 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d65bf0f-4e94-3688-ab27-dd0dd72a6b2d | -2.32909 | -45.6636 | 2024-11-21 04:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cc217d1-265f-3801-9b49-f5eb0d0ed555 | -0.92102 | -51.73599 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcc1596-6acf-3143-aa53-ad40035ac045 | 0.40703 | -50.81968 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cb612b9-4676-3244-8db1-0102bf209593 | -2.20213 | -50.54046 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c65e647e-6dcf-380e-a9cf-c7c591b6a15a | -1.70819 | -50.20461 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01c5f1a3-5fca-35de-af2a-12c894135b9b | -1.62264 | -52.59008 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61e414a2-9795-39b6-a913-763675cdb701 | -0.70989 | -51.67431 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f53a81cd-daf3-3acd-aa70-830f1251dac8 | -1.45865 | -52.68115 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6635dc68-e7f7-323f-9b6d-6cb256826ccb | -0.7749 | -51.7568 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0063c682-b6ff-3e3d-9d63-a4df198a2eb6 | 0.84738 | -50.13593 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ab0a03-fa71-3e09-9bee-1d68fd11a5b3 | -2.62801 | -48.06755 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e7d52f4-4c61-3844-a3bc-04ea6decee2f | -1.47236 | -53.4813 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23824ba5-e560-35e3-bd6c-b81f9be522f7 | -1.4501 | -54.50595 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 100a8cda-2b4b-3325-ada4-308aec499613 | -0.79778 | -51.78556 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9935d456-ec52-3c65-b8be-4e67965f21b4 | -1.22833 | -51.74706 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e01b354d-4002-35f9-a3bf-ba7242c1dc3e | -1.60326 | -52.41074 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3ea29eb-9e24-32ad-94e4-1426c8beb62e | -2.28667 | -51.0957 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d57cc78-2ca4-320d-a36d-c375931c64b1 | -1.78038 | -53.59719 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcad2330-1f14-38e2-b6fe-52968b0933e9 | -0.64277 | -52.33834 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae38055c-529c-349a-aae7-47c9da2332bd | -2.2734 | -51.13593 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d95a77d5-ca75-31a1-942c-681c622ed4e4 | -2.2788 | -50.58391 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4981b4e-a4a6-3c5f-be1b-887ba62d9708 | -1.4123 | -52.22092 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 378a58c0-102d-3e1f-821f-168bdda44784 | -1.44839 | -47.12212 | 2024-11-21 04:53:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86db9a2b-88c7-3f8d-8397-83563cf37c81 | -1.4937 | -49.68456 | 2024-11-21 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75fa120a-df9a-3f60-93e9-71d431d7d4f1 | -1.12928 | -51.68495 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9fe170c-7e90-306c-90f6-a9c379eda458 | -2.30803 | -51.27475 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3803d2c-debf-3741-bc9c-21a9342c5a9b | -0.82703 | -52.83221 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae3caa5-ebda-3cac-aefc-def2d649090a | -2.40142 | -47.64379 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed724479-8a7d-3823-b49a-2a6faddfb0e4 | -1.53797 | -54.90263 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a656a54-ead3-3d8d-86cc-2dc1b8774cee | -1.97697 | -48.68676 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 872376aa-5804-3f18-a063-5a2d807d2564 | -0.05322 | -51.25342 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5905e387-64db-3fef-ab7f-f71be33bec42 | -1.37657 | -46.51436 | 2024-11-21 04:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4784572-26e6-34d0-98b6-cdaf3b585ba3 | -1.25014 | -51.78303 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed9c0088-b6f5-3aac-a239-a1b0180c78c7 | -2.24693 | -48.16488 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b2fda654-1a7b-3211-a14c-1d59e099347c | -2.12887 | -50.12679 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57b6952f-b2cd-3289-8d2d-d1774d0f2d8a | -2.2792 | -51.09839 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc46b3ab-679f-3049-826e-93d1c4e0e484 | -2.61928 | -48.06994 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4931436-3464-3e2f-9556-7989029b0550 | -1.51716 | -51.15574 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bccaf9-e056-396d-9d57-67a4990c339e | -2.68404 | -46.24781 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5ae141f-3c2d-3a59-91f1-3aa8f1386c33 | -3.5935 | -43.6335 | 2024-11-21 04:53:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30089b1d-c12d-393f-b19e-fe199a56f3ca | -2.44392 | -49.03936 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b4d05e8-1892-334d-bc57-6824e3c54f61 | 0.44566 | -50.79496 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d67c0e0f-ffb6-3f40-bd56-928062da695c | -1.12983 | -51.6814 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11772ad8-ee07-36c3-ad59-41cdd027d020 | -1.62288 | -52.26457 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3c02b6d-b0fb-3591-bfd7-762dfb8903e8 | -0.63387 | -51.7282 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9472ce1-36b4-38ee-b6bc-02af453560e1 | -2.84364 | -46.68066 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b39d435a-0e84-31e3-a301-eddfdaa2f328 | -1.72692 | -52.70539 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa61f4d4-20f9-3733-b60e-6280151c9e5f | -2.26302 | -50.45184 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e7e58a9-cd44-3f6c-9191-6e8a87245f92 | -0.78717 | -51.7659 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b38b193-80e1-394a-8ab3-a88dbfb8c21e | -1.39633 | -51.99685 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17615f7f-8c28-30dc-aad6-8d8a5253a373 | -2.19991 | -53.67343 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4737d731-50c7-39c9-8310-56d782fca9a0 | -1.59451 | -55.12376 | 2024-11-21 04:53:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988d7e00-f2e8-34f6-9e10-ab8ca03dcaf7 | -2.0218 | -51.17859 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc9cc76a-341c-3d7e-bb87-2f3c94363079 | -1.36107 | -55.50734 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46e6341b-aaa7-316c-85b1-dbced63f32be | -1.46804 | -51.97559 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b03a58be-02cb-30fc-8cbe-d2b688050964 | -2.9322 | -48.33968 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e4d43f1-00c9-38bf-924e-5839758abf72 | -0.34011 | -51.5597 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86843bd7-b92c-3e64-beb0-5e754969329c | -3.22872 | -43.26889 | 2024-11-21 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5d7f4eb-5402-370b-aea3-ca94ee68465d | -1.58282 | -51.2746 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abdbda5-68b7-3e1a-ab55-535af21febd1 | -2.40587 | -51.99323 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 449abccf-0d1c-3067-8068-6fecdcc8a118 | -0.80246 | -51.49244 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e54b16d-10f9-3497-90e0-4460507a0172 | -1.29802 | -52.47278 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b043151-5423-39ea-8033-450a2eef2415 | -2.94484 | -48.33802 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6334361-5ee0-3dfc-9346-a882eaee8425 | -1.10698 | -53.60098 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feaa8ca4-f53b-327f-8313-8b6a34fb8dab | -1.42956 | -54.29462 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30494eca-f887-3dc4-9266-ed654c22a386 | -1.72469 | -52.698 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15e62970-cb23-334d-8d25-f12cd3124495 | -1.20101 | -51.7682 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def2b652-0de4-3094-9e2b-47a85bef306d | -1.19884 | -53.68602 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f16fddd8-f7ee-33e2-a5cb-074216f9900f | -0.42442 | -51.56915 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2dc3775-942b-3d21-bbcd-51978dc7eba1 | -2.14809 | -53.56975 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc6ddad-b33c-3afe-98a9-c238d6c7091a | -1.65712 | -52.69419 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f127872c-0bf8-3d64-814d-4c6b3f598e52 | -2.02789 | -51.18284 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d985fac0-ec66-3adb-b347-b905aef29169 | -1.68556 | -55.03477 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 625dd89d-ba6f-3e5c-95f0-2a2eff99c6c1 | -2.2648 | -48.40544 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01c40ae9-1896-3b62-8be5-d9ee35e5551e | 0.4036 | -50.79769 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7097814-3a43-3ee7-80fc-acc9e15e756c | -3.00624 | -48.04427 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b479660-5ff2-3070-a66f-9343c2249665 | -0.80818 | -51.60996 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6dd1b8a-2b30-3e3a-a0eb-7965308703de | -1.69145 | -52.54067 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e328b5f0-33e4-3061-845a-e3f5070dae7a | -1.58298 | -52.92898 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7a19746-7b46-3d44-bd0e-d02f36f3e82c | -1.45474 | -52.66293 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f97c795-5138-3270-ada2-0db317434ac7 | -1.3509 | -51.43645 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6476bc6c-0ecf-33fd-94a5-9419dac8f628 | -2.55783 | -46.05828 | 2024-11-21 04:53:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 872364ba-7dbe-39e6-a9de-53368de11b15 | -1.34153 | -55.44162 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4d62b16-a300-348a-965a-08d05a95c87d | -1.51753 | -52.09085 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d31572e-ecf1-345f-8074-c04c2db5afa9 | -2.69643 | -46.25234 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbaacd97-ca3a-38fc-8358-907f4cb8b67a | -0.8244 | -52.87042 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4909c3e3-b01f-34eb-86d4-eb193c1c2ebc | -2.06155 | -53.42943 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3e61f3-f8d6-3887-a36e-faa625dce380 | -1.71299 | -48.63177 | 2024-11-21 04:53:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d08fb85-4a1b-33a5-8799-52bf45714dff | -1.1375 | -53.66579 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed7802b-0a28-38f8-a8ee-77d03f135d02 | -2.60919 | -48.24823 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54166036-2035-39be-a2a2-39bf644cfabc | -1.32885 | -51.41483 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d99c50f0-99f4-3bd8-9bc4-73c175e3b2c9 | -1.04951 | -51.74162 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43e8b9e3-f83f-347b-b8c6-d168368a7d39 | -1.1239 | -53.40553 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9bfd40c2-3843-3d34-ace4-20ab3bcf7176 | -1.54789 | -54.29211 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README51.md)
