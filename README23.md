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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d7d0b0-ca23-3fd6-8715-25d5c5c7fa34 | -6.70646 | -58.94691 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74fcb424-ec72-3e7f-9a59-4c4106dce816 | -6.14598 | -57.71942 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81d80e9f-9795-3605-a996-40506b9bf39b | -7.55287 | -61.15639 | 2026-08-09 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5ad925-7acb-3e3a-9586-6dcd727790c3 | -6.88806 | -59.9026 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7e89cfa-3f65-347b-a3da-645628b66109 | -6.83352 | -58.93158 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65224917-b242-34cc-ab16-f3e7c050fa3e | -6.88244 | -58.93666 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb99e5d1-bfcd-3c46-bdc5-3e57acce981f | -13.95004 | -58.11346 | 2026-08-09 06:08:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d30f873-a1af-3116-b762-63a8d456e13d | -8.1567 | -64.08987 | 2026-08-09 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c91e179-ddc9-3ace-9635-e4eaebfa7c32 | -9.33297 | -63.45348 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58993d85-fb7c-396a-ae1c-fedf248095d0 | -8.6804 | -62.87389 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 66389bf9-52ef-38d0-bbd7-a665d11730b8 | -8.67314 | -62.8707 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cfbc419-c37d-35a5-8ef9-e5f4f7db7774 | -14.84455 | -60.0688 | 2026-08-09 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0960a8c-fd1f-32b6-b786-c5e3d7329a79 | -8.15224 | -64.08923 | 2026-08-09 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cfe149a-af66-3bad-bea8-016ff92f3fe9 | -8.63873 | -66.53179 | 2026-08-09 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50993fa8-17c6-35b9-97a3-d48e65b538e7 | -8.72368 | -62.88548 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa6427a0-43a6-3628-8b03-39305b5d90f8 | -8.6349 | -66.53122 | 2026-08-09 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 453cd96c-f1cd-30cb-8a2f-f0bd094d81f8 | -8.91997 | -64.30119 | 2026-08-09 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d176bb9-06d0-362c-87e7-23c728d56a4c | -8.78526 | -64.21311 | 2026-08-09 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bb23316-fb43-3ec2-811b-a0e37b2dd7f2 | -8.67803 | -62.87142 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac3ff60c-3782-3825-9a15-f47bef4cf647 | -9.33426 | -63.45015 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb9fbea-b24b-391e-a3fd-f90f73297fef | -8.63038 | -66.53539 | 2026-08-09 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51b51c8d-e309-3ed8-8549-ba8569692ffe | -8.67624 | -62.86768 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f76d1a5-0128-3637-8053-e38e78724759 | -8.68603 | -62.86911 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfb4d46e-cd15-382b-9896-044b4e96a44f | -8.67551 | -62.87316 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ba1aa9d-31c2-336f-8120-af177db988ef | -13.94223 | -58.1199 | 2026-08-09 06:08:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e3feb76-d68f-3152-a991-b98169dcd330 | -8.45094 | -72.78498 | 2026-08-09 06:08:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dc4b2ef-b3ab-30df-9ca1-5046f64a668e | -8.68529 | -62.87458 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f593b44-a7b2-3194-93e7-32bb974747bb | -8.44751 | -72.78442 | 2026-08-09 06:08:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6abb23d-ce6b-3883-bb20-e8f97cd4e06e | -10.9441 | -68.72599 | 2026-08-09 06:08:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d81a6e60-a88f-34e5-83ab-907ce784cc51 | -8.87695 | -70.80573 | 2026-08-09 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 471e8a39-9f26-3064-aea9-e0694faaaab1 | -8.68114 | -62.86839 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a9e279a-c2b7-3e71-b6af-c4f7db8f8a33 | -14.85147 | -60.06424 | 2026-08-09 06:08:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 235290c0-d3f9-3d56-a58c-fc9e35619fea | -8.87365 | -70.80521 | 2026-08-09 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 659098e5-e19e-3556-b052-d3186ef90d15 | -10.15009 | -69.31964 | 2026-08-09 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe7a10e-d144-326e-8c3e-e42ed61e85d6 | -9.19202 | -65.8735 | 2026-08-09 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1018c8dc-ea0e-3667-931b-515267bad87d | -8.8742 | -70.80173 | 2026-08-09 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27db159f-4573-33d0-81f7-5f9cec7ee493 | -8.51159 | -63.36182 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76397d83-1789-3a1b-a496-3ef263af802e | -8.6342 | -66.53596 | 2026-08-09 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c420ba7-1d29-37f3-b4da-d44377acea6f | -8.69092 | -62.86978 | 2026-08-09 06:08:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5ae0c72-2059-3de6-8e19-aef0c9b37c3c | -6.14197 | -57.71669 | 2026-08-09 07:37:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b8a379ff-bf66-3161-9c1b-0ab65118aa0c | -10.92127 | -57.11525 | 2026-08-09 07:39:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ad747e83-3214-389c-98a5-e5ef3cd44ab8 | -8.68065 | -62.86729 | 2026-08-09 07:39:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 716db7ef-bc94-3597-96f0-f7a42d0b32f9 | -6.84376 | -56.40001 | 2026-08-09 07:39:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ec5b6754-d10e-3fe2-b107-1594fb97384e | -6.82976 | -56.41466 | 2026-08-09 07:39:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 94b11f7b-25da-3acc-a1e3-5e2f6df168e9 | -8.67184 | -62.86596 | 2026-08-09 07:39:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfd22a41-4bdf-369e-b93c-866f0e82daf6 | -10.5198 | -46.6018 | 2026-08-09 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d2499eb2-aab7-3450-aafd-43c22d602fa6 | -18.1583 | -42.8514 | 2026-08-09 08:10:00 | GOES-19 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 9317c4f3-f9e2-362b-ab1a-249b87fc3478 | -18.1793 | -42.8214 | 2026-08-09 08:10:00 | GOES-19 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.1 |
| d1268bcf-5224-3341-a71a-853fb6b375c5 | -18.159 | -42.8265 | 2026-08-09 08:10:00 | GOES-19 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 264.4 |
| 693d37ce-e692-31eb-a131-f1f3b8deb829 | -18.1598 | -42.8016 | 2026-08-09 08:10:00 | GOES-19 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| 4fa3abd2-c7f5-31ed-af8b-fda583539d29 | -18.159 | -42.8265 | 2026-08-09 08:20:00 | GOES-19 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 45a43c83-a885-36bb-a487-90181c60aabb | -8.85331 | -44.17595 | 2026-08-09 11:00:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 21bf405b-22fe-309e-b2cf-90685c177ce0 | -7.79854 | -37.66668 | 2026-08-09 11:00:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| e01a613b-3066-365c-ab9e-a8226433a043 | -8.86023 | -44.1712 | 2026-08-09 11:00:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0932748b-6898-3415-ae39-1a543feea9dc | -19.33376 | -40.02574 | 2026-08-09 11:02:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| fe471fea-3334-32d4-b1c1-e36177fd028e | -19.59097 | -42.59121 | 2026-08-09 11:02:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 05e4ca62-f744-38c9-aa31-2092020436a2 | -20.58572 | -41.9116 | 2026-08-09 11:02:00 | TERRA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.4 |
| 893a64ca-72eb-3b0c-8ddf-8847a0059edd | -17.24157 | -42.53957 | 2026-08-09 11:02:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 905c8183-ab48-306b-9fa3-d83856372135 | -20.57513 | -41.9094 | 2026-08-09 11:02:00 | TERRA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 3a9d8435-f2d4-3ed6-9dc1-3862f0e5ee4f | -17.23848 | -42.5574 | 2026-08-09 11:02:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3c2ee597-11fb-3451-bf47-1956f23bc50b | -11.2716 | -44.8624 | 2026-08-09 12:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0126ba5e-ac18-3ea0-af65-99b31061dde1 | -12.1105 | -47.2234 | 2026-08-09 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0ca4002a-00c5-31e4-a83c-4ba6fb7b50fc | -12.1109 | -47.201 | 2026-08-09 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| af77edf4-18eb-39f2-97dd-90a443f27cfe | -11.2716 | -44.8624 | 2026-08-09 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4e38a5ca-1fa6-3429-b662-22a049565aee | -10.5195 | -46.6243 | 2026-08-09 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f2efbbff-720f-3dbe-9218-1e907dfbed3e | -1.83499 | -54.66005 | 2026-08-09 12:34:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 679e26e2-0f1a-35cf-a5ff-6d0aa23a041f | -1.83333 | -54.6719 | 2026-08-09 12:34:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aff993e5-5958-35e7-a62d-499d57560e2b | -6.85147 | -56.3909 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e706f1cb-27c8-338d-875e-a615daddd53b | -6.42264 | -55.78891 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 772e8b8d-607e-30e5-969e-4db27739b7c9 | -6.14145 | -57.72198 | 2026-08-09 12:36:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 76d8ff64-6b4a-3451-8a14-a16b0bb19640 | -10.92137 | -57.12227 | 2026-08-09 12:36:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3fc5f4ab-e841-3d96-a5b3-2a8835e3d1e4 | -6.14276 | -57.71273 | 2026-08-09 12:36:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9a67db04-5510-3b56-9fad-ad90422070cf | -12.32544 | -53.15492 | 2026-08-09 12:36:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ac5b1823-d9b7-3f11-9b81-c8bc7204f50f | -8.68654 | -62.86785 | 2026-08-09 12:36:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7c03295d-3a72-3fac-b119-1c608b55509b | -6.609 | -56.36201 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 820ae489-4b60-395d-a309-262d719c232b | -6.34207 | -53.53105 | 2026-08-09 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6753cdab-63ae-3b94-af6c-c7d878638f2f | -11.48345 | -50.56543 | 2026-08-09 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| b0577bad-3419-3e14-84e8-084a8014c663 | -7.38907 | -59.96687 | 2026-08-09 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1b8b26f-6aa7-35cd-9a25-236de7a34fee | -6.62651 | -58.40599 | 2026-08-09 12:36:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7a6e8927-9c30-3820-b881-f7c5f36d1a7e | -6.88144 | -58.94027 | 2026-08-09 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2471a110-0480-33aa-be27-3f5e4aeaf750 | -10.91988 | -57.13329 | 2026-08-09 12:36:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5c962eb9-1581-311d-8a6c-df2544b38764 | -6.71368 | -58.94941 | 2026-08-09 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9ee44f72-9e2e-361e-afdd-87066464db3a | -11.78377 | -54.24391 | 2026-08-09 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c8daee75-a859-3d1f-9882-787aa35dec58 | -6.83731 | -58.93412 | 2026-08-09 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34d403e3-ad72-3b81-95a8-3c72826b6cc6 | -6.71242 | -58.95823 | 2026-08-09 12:36:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bd5046dc-383d-331f-92d2-f4eca9f4fc22 | -6.82617 | -56.43154 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b854ba8e-a08e-3990-8f74-efa544e3905f | -5.88445 | -57.64907 | 2026-08-09 12:36:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| db7fd85c-18fe-3aeb-9053-8b18ed69448e | -8.15862 | -55.40081 | 2026-08-09 12:36:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6f675a78-b170-32bc-a56d-0fa1c8c110b6 | -6.84997 | -56.40184 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2e8c9287-7440-3ed6-94a4-04314f3bea5f | -5.75575 | -55.73297 | 2026-08-09 12:36:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9d647519-8e44-3d10-b9c3-d4ad34bec4f2 | -8.67653 | -62.86638 | 2026-08-09 12:36:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2ffd8d7f-4794-3cd5-b44b-ff10431fb047 | -13.86997 | -53.66603 | 2026-08-09 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d1b08e0f-4ca4-3df3-bb7c-7242ffd9ee2f | -14.8529 | -60.062 | 2026-08-09 12:38:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 01ac191a-f591-3204-ba9b-cde715e5b7e2 | -14.43821 | -58.57672 | 2026-08-09 12:38:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 53c5a8ea-f0da-34d7-b75f-04ac44eb0a5a | -14.84714 | -54.22503 | 2026-08-09 12:38:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 191.7 |
| e1622ac8-5d5c-3adf-ac0f-6cc0e69d753e | -14.01991 | -54.06535 | 2026-08-09 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f99a4f40-b4e1-308f-841d-fd79cdfbae23 | -14.84614 | -54.24058 | 2026-08-09 12:38:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| dab5da45-07b5-3486-bd15-299a17cf975d | -14.84856 | -54.2197 | 2026-08-09 12:38:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 5564ea32-de92-3d97-b3b4-16fdbe4ecc0f | -14.84488 | -54.24588 | 2026-08-09 12:38:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4592df0b-7a75-3fe4-98c9-72f170a69a6d | -7.3748 | -42.8883 | 2026-08-09 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |


[Clique aqui para ver as próximas entradas](README24.md)
