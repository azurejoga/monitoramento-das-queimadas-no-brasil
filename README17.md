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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dd92c11-bf5a-3ebe-ab76-21f966526ba8 | -3.98619 | -42.52297 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6863ae24-021c-3054-a9fe-7670a4f82839 | -2.89958 | -51.47261 | 2025-08-18 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 182645d5-c8ff-3cc9-901c-24607abc1edc | -3.9808 | -42.52502 | 2025-08-18 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 97bc7f62-533a-3d1a-bbb0-b28849b9634a | -3.59083 | -47.53108 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f0e3631-81dc-3b70-9921-8986c1375d58 | -3.58725 | -47.53055 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ce72b87-e97b-3638-ae20-819ed9dc0778 | -2.44806 | -47.33236 | 2025-08-18 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b12e27fc-5b43-3c3b-954f-d18395c5ac23 | -2.89903 | -51.47612 | 2025-08-18 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5cc797b-fafd-3a3f-a692-e75df8965e5c | -3.82664 | -47.73825 | 2025-08-18 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b27a02b5-fe69-3c7d-b6cd-61d973914fc5 | -8.81758 | -52.04013 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2528ae88-d67c-3b77-88e0-f0f708c11ebb | -10.87041 | -48.50705 | 2025-08-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14528cc2-756c-3efd-8ec4-0fb0c2d7bca1 | -9.49262 | -40.36918 | 2025-08-18 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 04c2a326-5e23-3c8b-8c8c-5cd1949ac830 | -6.5623 | -43.01453 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 719759bb-b038-398d-8260-3428e0f6e599 | -6.55108 | -49.51139 | 2025-08-18 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc6daa2-8440-3672-b0cb-2ef3f556e7fa | -6.4298 | -44.78785 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9410fa79-5434-3833-9a65-6e3123e6d962 | -6.03812 | -44.34114 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ca9369a-5713-358b-9404-03922f22d49b | -6.07805 | -44.60988 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9f8b680-2d80-3967-a4c6-3d9c2a0d1819 | -6.49423 | -53.39087 | 2025-08-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d81f9309-df26-3c78-ac5f-71fc223c2d60 | -7.01591 | -44.27683 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b93befa4-fe98-39f2-a665-ef8fa518cda1 | -8.88953 | -50.85464 | 2025-08-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7333db0-3757-3020-a1f6-42fae7586420 | -6.73559 | -50.95631 | 2025-08-18 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb9be69-0abd-348e-96d4-36f2e65f7667 | -6.43424 | -44.78841 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 913a105d-9d66-383c-bae9-404f8a1bed97 | -4.7805 | -45.32338 | 2025-08-18 04:46:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2aa82e8-4b72-37e7-a644-253604668ca9 | -6.56727 | -44.46622 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e0bf3d8e-7028-315e-8fda-8928bcd2e108 | -8.22718 | -47.30157 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb57ffaa-3e77-3b9d-92e0-5181b4808bcf | -6.56203 | -44.47037 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 723a439c-04ed-3810-a815-a5af27b7ec3c | -9.51058 | -60.52644 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 109ff136-f62e-3da5-be87-5bd9b79c4e8b | -9.29202 | -50.2738 | 2025-08-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74f67699-ffc8-33a8-b9ba-3e5a0cd59afb | -9.51786 | -60.51523 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07382cf0-a4df-30f4-8627-3f1759f76cd9 | -7.51668 | -45.46879 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13fabcca-dd53-375e-80e0-45303619e5c3 | -9.51966 | -60.53444 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60df4701-e5b3-3f8b-8488-477ed2ff4cbb | -10.9552 | -45.17151 | 2025-08-18 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d884c83a-62a4-3380-9390-1c899230327d | -6.54524 | -43.02557 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46c1461d-5daf-31dc-a9cf-e8479ef24a36 | -6.55065 | -43.02345 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2d92f96-0b0c-3058-af20-1e54a2449a6d | -6.73505 | -50.95977 | 2025-08-18 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159aa649-7dca-3793-b737-d9d201fabb35 | -9.63757 | -50.89449 | 2025-08-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f9c5dc1-af99-3623-8829-a8bb2fa765d8 | -8.51151 | -44.73625 | 2025-08-18 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f995d20-d3e5-3cd8-9d6c-488b0767710c | -7.01626 | -44.27959 | 2025-08-18 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afa1d09-5a7f-3aec-98d2-bce354390544 | -6.13728 | -57.93282 | 2025-08-18 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4af1da5b-84c3-3329-b652-0de169a3bc11 | -8.24033 | -47.85974 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5919264-f156-37bb-b086-abe03ef3d372 | -7.05864 | -44.91641 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ed81b9a-d669-395c-b703-c3dfbb34b007 | -8.97401 | -60.49927 | 2025-08-18 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc696e62-8bf9-33cb-a004-5d0fce09c04c | -5.75558 | -46.67049 | 2025-08-18 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e6ac597-fb5c-3bf8-9d24-94f83d054ea1 | -7.14348 | -44.1988 | 2025-08-18 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88eafb50-e6ab-36db-9652-8b9b12af6f4a | -8.78429 | -49.99419 | 2025-08-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b664e94-86d6-3974-a3ee-29f1874894e8 | -8.7159 | -47.85788 | 2025-08-18 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca9bb93-0be1-344e-8222-08f1846fcb02 | -9.51911 | -60.53747 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b8f0192-8d13-3165-9b0f-b70d2cbd1081 | -9.52075 | -60.52834 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fea3d98-291a-31d3-8304-2a8990a629d0 | -8.50172 | -44.73956 | 2025-08-18 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f66db4b8-24c5-355c-91cf-20e9f9e3454a | -6.56265 | -44.4768 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 302c667f-fb52-301e-b24e-80ff4315eb44 | -6.97849 | -41.63076 | 2025-08-18 04:46:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4c6587b2-c0da-3e37-85e4-3a4d59d2216c | -8.82364 | -52.04465 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ef1c51b-83eb-3335-adeb-827f4f7a89c2 | -7.55248 | -45.43243 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cbd2bc9-9d45-3f9d-87e7-ee8e4a8d3e14 | -8.22085 | -47.30361 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dee63a6-dc0d-3de9-a876-0cc3c2f5650c | -5.97981 | -44.12101 | 2025-08-18 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c6a99f2c-5a01-3554-b7dc-fbea687f10e9 | -8.11073 | -50.01995 | 2025-08-18 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949d613e-c673-34c0-b7b8-e3e532fe9911 | -5.76332 | -46.67163 | 2025-08-18 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a6de25d-d11d-37e3-b4c4-31e5b354f788 | -5.03435 | -56.12201 | 2025-08-18 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0de1a2c1-6d45-3ed6-a04c-6e6fb913e739 | -6.57239 | -44.47317 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d1feb9e-ddb5-32e0-8869-218a6c832b78 | -6.16168 | -47.2778 | 2025-08-18 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2257129c-7dbf-3244-bb15-1b74b143ee00 | -10.86 | -48.4733 | 2025-08-18 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec3e42a6-ab72-31b9-b48d-5c4975dab0eb | -12.18923 | -47.22972 | 2025-08-18 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4ea9a09-ec6a-30a1-92ea-811d8d810b50 | -7.55189 | -45.43658 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7ccf049-d572-3f0b-94ac-9e6cbe164a9b | -7.53548 | -50.53215 | 2025-08-18 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f0870d6-1cde-3c6d-9416-d428f9d3a67b | -6.16088 | -47.27553 | 2025-08-18 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 586fbcc7-04fe-3c4e-83f6-2f41326f91d0 | -7.20066 | -46.24044 | 2025-08-18 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 827a1684-f3bc-31bb-9cb5-90738994509f | -6.56592 | -44.47541 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f958328-51a4-301c-9405-c8c45784a7d1 | -7.14135 | -44.19259 | 2025-08-18 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ab46fbc-bddb-383d-8ec8-adfe3b041492 | -9.87011 | -44.69358 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ebcfd1d3-c058-358b-b198-0f156c2dd05c | -6.07767 | -57.91975 | 2025-08-18 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a3f2d89-8b78-3508-8565-18a1a0721279 | -9.51566 | -60.52742 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c291b082-4665-309e-a3d1-80a1d5e2fb9a | -6.32866 | -44.70845 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f81451d-012b-3d2d-8899-2ca34e5ec76f | -5.15016 | -48.10781 | 2025-08-18 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 571c9a5e-306e-3dc5-80a4-65db311db666 | -7.53269 | -50.52811 | 2025-08-18 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26201b7b-8095-3da5-b3fe-099ff75a4a26 | -9.51511 | -60.53046 | 2025-08-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3839d141-aa95-3be9-a430-ba0299770d5d | -9.87695 | -44.69567 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7b11ff8-ecb8-3e15-a45b-aa64f83613ff | -6.90578 | -39.54759 | 2025-08-18 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5ed2435a-42ff-3824-9ef7-1ad0e6ce098b | -8.82254 | -52.05162 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5986523f-7123-3013-b502-1c974ca8a822 | -7.14535 | -44.19785 | 2025-08-18 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 956fd336-b27a-3263-a5f5-1469c9b78c2e | -9.82963 | -45.96571 | 2025-08-18 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4dc2350-97e8-3b5e-9b8e-86ff06ef5357 | -9.39627 | -48.29179 | 2025-08-18 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df8164fe-1fd1-362d-842f-e332bd416478 | -7.53215 | -50.53163 | 2025-08-18 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83dfb6b4-7c7f-3d70-be3f-0ebafadb4bf8 | -6.90854 | -39.55241 | 2025-08-18 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e98eec67-c0ba-3973-88e9-e50b3c8de1d5 | -8.7953 | -52.0722 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 912c3a7e-efc2-3045-8608-d9e89ec6df46 | -8.11411 | -50.02047 | 2025-08-18 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad3ba307-1e8c-3a0a-a218-45887cf6aac8 | -9.21784 | -44.53447 | 2025-08-18 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5891180e-0381-3b69-a6d2-725d3d5046b2 | -7.80177 | -45.1616 | 2025-08-18 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdd4db32-6294-39dc-97da-a71e29e81b3d | -8.19391 | -47.35298 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e5b27c4-a40b-3655-b8b4-e1ff0b6f1fbc | -8.85332 | -48.99218 | 2025-08-18 04:46:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c9040b5-b089-393b-958a-7e260d025a28 | -6.54769 | -49.51086 | 2025-08-18 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec915931-201b-3494-8c95-b8615353701a | -8.21702 | -47.30294 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fde7311-3217-3c5c-b77f-574633943e03 | -6.47553 | -45.4437 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f63db16-255f-3e71-b5be-2c2b9fb7aee1 | -7.28662 | -43.68763 | 2025-08-18 04:46:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0cec45b5-3423-38e9-8217-50bd99858d0a | -8.81314 | -52.02521 | 2025-08-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee41737c-2a78-33f1-8582-6f5fedee7457 | -6.35742 | -43.27229 | 2025-08-18 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5334f94d-1dcb-3524-831f-4f977b158074 | -6.55226 | -43.48704 | 2025-08-18 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10cbc3d5-c402-3e70-9cff-21f2a0877f53 | -6.42598 | -44.78289 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e13b940d-15b2-3a3f-9d5b-24c2fc5c1268 | -7.55619 | -45.43727 | 2025-08-18 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a531f4b4-16c0-37a3-9310-b9965c258736 | -6.36197 | -44.53587 | 2025-08-18 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b86e0039-1a3b-3e7e-a8df-d49d26e138ff | -8.20392 | -47.32711 | 2025-08-18 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d259537f-c8e1-338c-a4ca-fb563902b05b | -9.86756 | -44.69443 | 2025-08-18 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
