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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7da39cf5-f8d8-3f0c-bc1d-363e76fb0f37 | -11.22564 | -45.0302 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14010113-c797-37ed-8eb5-a566af5bb86f | -13.63627 | -48.13528 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6911bb7b-ef55-385d-9bf5-86caed2499ba | -9.60393 | -48.26532 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95a64874-71bf-3030-b704-48564c4a0428 | -13.36935 | -46.98478 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 570f05ab-1fd1-3f5f-b98d-721ac1e4d9f0 | -9.94146 | -44.02269 | 2025-08-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a02bc5d-9170-307a-8ac5-e04b6d6d78a1 | -13.58294 | -46.90347 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3436cf6a-6b6a-3321-8af5-9e19bbaa90d8 | -14.25378 | -45.24482 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ca4571-690d-31ed-94b1-bd8957d06e88 | -10.99759 | -46.96249 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29545c6c-160a-385d-ae53-e6b327dbf370 | -14.03952 | -44.52139 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a214d84-aeb5-3eec-861b-d058a9ed874a | -13.39452 | -46.95597 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22004029-048c-3bad-a704-1fb3afb3e972 | -11.31019 | -43.65321 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f28212f-93d1-31c9-b78e-a7a0e7a36f28 | -13.41111 | -46.95855 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4be2cd7a-3e26-38e4-abbf-9474cbc68af7 | -12.92282 | -46.36427 | 2025-08-30 04:21:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90c2c479-ce15-30de-9383-e2a0587377c9 | -12.93267 | -48.1136 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0d85c89-3c25-3028-84e8-87c96e61d5bd | -11.22339 | -45.0226 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7071fc35-7f39-3e81-98e7-8dac906a1841 | -11.86517 | -46.38621 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ba6c6e3-f516-366b-b161-1248fd068af2 | -12.93207 | -48.11729 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09803433-adf2-3fde-9d0d-5e021fadcb5a | -13.58793 | -46.89339 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c6eec4-47e0-3957-9fe3-9c50e580f77a | -11.86509 | -46.4511 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ae4438e-6021-3ee3-8e37-3c51b1cc6ae8 | -8.70183 | -50.36201 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f523f0d-4817-3a32-a70f-0260b26a8352 | -11.32059 | -43.65479 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bf7e871-0093-37af-b228-f3913b966723 | -13.35371 | -51.77932 | 2025-08-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6af42ee-3393-31f7-91c1-48b392fa5da5 | -10.88321 | -45.13584 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b63374fe-46a5-383f-9719-b0d8ab0a5e68 | -13.96413 | -46.33877 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5af2af25-c001-3668-bd4a-1609c9e73e08 | -9.70575 | -49.4721 | 2025-08-30 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 903057e3-d550-32fa-b0c9-deb574324f9f | -11.00306 | -46.86458 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4db5e662-96fc-3d1f-b76a-fbb0d8b97347 | -13.37553 | -47.01119 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 832364b8-b0d6-35e9-9ce8-e102cc754d38 | -15.10612 | -48.19009 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c6888ca-98e8-3838-a57a-e5de514a98a4 | -13.37828 | -47.01529 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b023233-8759-317f-9fbf-4ac5064e0e3f | -11.22285 | -45.02614 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b2dafb-369e-3550-b33d-9655e5efd882 | -11.5683 | -46.34855 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e97c7fa-25e7-362b-9d25-6b478c7ac5bb | -11.85526 | -46.38459 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc38956f-286b-3a7d-afa4-d6612c6da9d5 | -14.24084 | -48.06604 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9d92423-936c-3c47-a009-e61972abea0d | -13.55525 | -46.94977 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d851d51a-7224-3aa5-9d09-aecba796cc90 | -12.88732 | -48.15595 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 944f757b-eeb7-3480-b48e-fc7ad500b567 | -12.01329 | -43.98975 | 2025-08-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 4fb8817e-4048-3271-9e80-9a0585866cd5 | -8.68193 | -50.40572 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07ca45e-990a-3fc0-80a3-6ae95f333558 | -11.86958 | -46.37971 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 693287f8-f558-3769-ae98-4bdda952ca14 | -11.85029 | -46.39459 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f08e6c49-ad2d-36c7-89ef-fb9cd7cd5af2 | -11.92164 | -44.8561 | 2025-08-30 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ca21c59-91ec-3f76-afd1-1326f656c803 | -12.84962 | -48.12674 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7bf1687-207e-3c6b-b773-0f3686e600b0 | -13.39009 | -46.96249 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b6733913-4bd2-3c30-9667-a644ba9f7988 | -10.49563 | -51.63199 | 2025-08-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb8af855-3c4c-3451-a57a-896290b7c88f | -10.99655 | -46.94765 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ef1af61-5e22-359c-99ea-3579ffec9754 | -10.27421 | -54.24036 | 2025-08-30 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c60bd0d0-ada7-3396-bf95-bcd2330316d2 | -13.37041 | -46.99956 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7e40db8a-2562-35fd-9853-47b755191f4f | -10.75895 | -46.36815 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 583cc338-f72d-39a2-921f-95e0b4fb60a5 | -12.45187 | -47.69934 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5462ce17-8a15-3652-8554-986e2b12fd11 | -11.00421 | -46.85746 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005f4304-499f-34b7-a34a-63fec9c3e58f | -9.69149 | -48.30757 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b1e06a9-e6da-3dd1-abf2-9f7907def6d0 | -9.24833 | -56.89588 | 2025-08-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0762d732-801e-3245-bc6a-9d1acad13eda | -11.08501 | -45.12738 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f51d8686-13d5-3699-b4ab-6615fa803a8e | -13.97294 | -46.3257 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e8d2c40-1d32-3f6d-88af-7eb52e9426a0 | -9.58073 | -54.46726 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcb11a66-a149-39cd-b4d5-6e15c374607d | -11.07173 | -52.04406 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea69c95f-178a-3507-bf95-53af7128fa56 | -14.02289 | -44.4912 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff29721e-88e3-3d8a-bee4-0b77f246786c | -11.31941 | -43.63882 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92d961e3-a20f-3634-b005-1b62fc123266 | -10.67981 | -48.36944 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a46fcc9-0eaf-377e-ba79-983d28536d8a | -11.83147 | -46.44925 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6703db54-ef70-3ffc-877d-64ca65c493b3 | -13.65993 | -46.86933 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 535b69c4-60ee-340a-8487-02aafd560cad | -11.3298 | -43.6165 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0183c3a-5797-3f04-84d0-1efa163ecc2c | -14.00702 | -44.57504 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 252bdb26-8c65-3a7d-a06e-0107461611b5 | -14.04295 | -44.52193 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4378e06c-9444-3e6e-b491-b46e9dc7f870 | -11.88446 | -46.37133 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e76b53b0-5157-37b3-ac01-7ce8e59b4e60 | -9.58715 | -54.48476 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a46df56d-521b-3edb-babb-2e8d16fddeb8 | -11.83783 | -46.85921 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 201f82a0-fa9d-3628-b4c6-7f052f3e34d4 | -9.53754 | -45.85148 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab725f32-d6fc-3eff-a30e-72645bdd25b1 | -11.31594 | -43.63828 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7c6b906-953a-3444-b249-cea7e206f009 | -14.25097 | -45.2406 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a41a9eab-ea50-3a69-b221-9f1880ccfd4c | -13.65602 | -46.91569 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4da2b8e-fe5a-30cc-8920-6d31ef301161 | -14.53414 | -52.00069 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84a29905-4905-3302-8234-238fd919be98 | -13.67141 | -46.92565 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 473a0018-5780-3b5a-992f-b393acefee55 | -11.30783 | -43.62107 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 653c0eda-e1de-37d8-8cab-96d316399af8 | -12.84097 | -48.09402 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1ea35b4-e2f0-3bee-b777-b741c4cec05a | -11.86405 | -46.39327 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6617eac-3ddf-3d58-9cad-6f62688ee038 | -9.24848 | -56.89828 | 2025-08-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac478c44-d287-3fe7-b096-bfe71b091250 | -13.68146 | -46.88351 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b049a6a-00a1-3c3f-bfa2-5d35836373bf | -11.78408 | -51.44004 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2137f04-c013-3a02-897f-12d6b5f88c50 | -12.83327 | -48.11993 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06eb6927-3f2a-3001-b4a7-2f7dc73c8a36 | -13.40834 | -46.95455 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b981149-0377-3bab-8639-f28b6612c753 | -11.32395 | -43.55976 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65f1c949-0cd1-3a7c-b47d-4c53e05b9a94 | -11.27977 | -44.92195 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4adcaef-9bab-3118-b16c-78b8147b2083 | -12.84973 | -48.16921 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee3ba43c-1c29-3459-b5ca-9c99d0ffff20 | -11.22332 | -45.00077 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d30315a-7259-3004-8cf0-32ab76848f23 | -11.84251 | -46.44381 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 58a19ad2-e9f8-3c57-816f-c58156c3cb23 | -9.14273 | -49.6244 | 2025-08-30 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72b868ed-9ac2-3537-a0e5-6f67dcabd020 | -14.45584 | -48.45312 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 213815bf-7ee2-3589-8c5c-746b64039895 | -9.15039 | -59.55724 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f932e0ab-2626-3786-9901-e442f0eb0bf4 | -13.35693 | -46.86995 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a4babf3-d127-3c56-9f12-fc07eb74681a | -9.71026 | -49.46815 | 2025-08-30 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8a1277a-42ca-39e1-b7d8-1ce767fed366 | -14.47833 | -48.3801 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8fde4cb-462a-3e22-a70d-a5966a5cc16b | -14.00529 | -44.56304 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eafd6dc4-dfd3-3a01-a5ff-da2bd3057fbf | -13.19522 | -45.28412 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5349996-38bd-3c3f-9ab8-3b2b7db87c8c | -15.18657 | -53.78159 | 2025-08-30 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffc62264-0a08-3994-9cfa-0461680adec5 | -13.39767 | -47.00026 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 595096b6-3405-3cdb-a057-d0167cb28189 | -15.82539 | -45.76904 | 2025-08-30 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8287cdf5-e6a9-33c7-a40b-7f436f9fc869 | -11.87887 | -46.44974 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e1dc31-b288-3063-852e-a09aa73c0173 | -14.61973 | -48.07689 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c28df50-adb0-3224-9a02-9ac257affad6 | -13.56467 | -46.93317 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9720b5b7-030a-3cce-82c5-50be04c30e2e | -9.62235 | -45.96136 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
