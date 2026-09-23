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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7e3f3da-3ad1-30cd-aa8d-66b030bc2701 | -8.46012 | -48.69385 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dcc18826-2e6f-3242-b2eb-76c4c8e83335 | -8.45241 | -48.70613 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c68e2d0-57ff-342d-ba66-9c9883ed61c4 | -6.45802 | -54.98785 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1304bedc-6fa4-3460-a740-efee3ac69e82 | -6.1967 | -57.78064 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54926389-f3a2-354f-86ec-e8b9bf3a9148 | -6.70149 | -59.96138 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 635fa4ab-1e77-30bb-aef3-b1f13a83bd14 | -7.56518 | -57.67686 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72ca64c4-cf5a-3152-9854-98f1f2c857d0 | -6.29707 | -57.74446 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22ebdbfb-edc2-3bb1-879a-a8fa4cf80d85 | -6.62482 | -59.93086 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| be2b8f46-1e78-31d1-89a3-7eb6170f81b6 | -6.08379 | -57.69698 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c99e3858-2206-366b-96f3-ab8c5059ddb3 | -6.68768 | -55.05651 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6515d79c-c11e-3cfd-bf1b-e972f71ed9f0 | -7.56168 | -55.02427 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb103a8d-620e-3c34-a2ee-251be9970d28 | -6.16016 | -59.94644 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8995140-38db-3018-8f6a-4b4180198435 | -6.64588 | -59.92706 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60808c6e-d2a6-35bd-a8d1-1595a3dd03ac | -7.02414 | -62.92756 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5804c8ac-70de-3ca3-9e60-5bbd26ac99e8 | -6.10793 | -57.67494 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e46a5617-544a-3b58-bae4-598bea2cf4e1 | -6.55191 | -56.0384 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebcb90e2-e471-325d-9e99-cab9919de0e2 | -6.83534 | -58.9906 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b29e38f-74a7-3b41-88b9-471cbc8d04ee | -6.44608 | -59.9639 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3933f24-9441-36ca-9f2d-fb5e3accf559 | -6.08432 | -57.62689 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c80e118f-6bbf-3121-a9ee-83c19317f726 | -6.36021 | -58.277 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57f43d82-c65c-38b0-8af4-e2ff266ef144 | -7.3304 | -55.58948 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27418b86-27d6-3e8d-905a-4020fdca3b42 | -6.29932 | -57.75215 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0fdcfe1-80c5-3433-a961-6d5379ef71e7 | -6.45822 | -59.99458 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ace6e6e-d247-32d0-92ca-9f8feee1d4c3 | -6.66278 | -50.9497 | 2026-09-23 05:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51a99408-60cd-3847-8991-787f970ab3d9 | -6.66791 | -55.05828 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d3c2d8a4-11c8-32d8-95f5-8baa43bc3c6d | -6.46667 | -53.55937 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eda02427-0933-3a90-af8c-93f6e510cf24 | -5.86722 | -60.16018 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4a0379-31ac-336d-ba42-f50079c9a60b | -13.84982 | -48.58196 | 2026-09-23 05:25:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 15ae8abe-acd2-364f-9de0-1b6dc805b782 | -7.03821 | -62.93444 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5f2af26-ec4a-306a-b8a9-685190c84fd1 | -8.90706 | -45.94931 | 2026-09-23 05:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c94c3d8-7845-3f00-bf35-a31b7b95c517 | -6.77661 | -58.60731 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc27af6a-f4af-3286-90a8-03a4bfdea98b | -6.31813 | -60.04031 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73cec5f1-6966-3dd6-bda3-8b8cca6f5c86 | -7.15793 | -59.59206 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a60fa63-e94a-3865-a32c-872f73211504 | -6.09501 | -57.62486 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b233b2c3-7e4e-3064-9e68-2214354310b6 | -6.59217 | -59.90057 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e1f8d67-873b-3193-844f-522503424e2e | -5.4586 | -60.14574 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51d79e0e-8b92-3790-ada8-38b83a0b14e8 | -13.92547 | -47.84146 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d121537-626a-3588-a0c7-381bb46e2c90 | -5.151 | -60.30988 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fc41a82-5ee8-3673-bc0b-85949cc17efd | -8.45613 | -51.48939 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d368eaf-a8fa-3b90-b7e7-5e9e401ca9fe | -5.9829 | -57.78054 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f67bd102-68ea-30ec-a5e7-ad563712b6ed | -5.45746 | -60.15284 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ba323b1-60ac-371c-9a24-f641ac20f31a | -8.45414 | -48.69291 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6a6c518c-2200-343e-8f11-4791b83a77f2 | -6.66719 | -58.56927 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 768446d8-ba4f-3b9f-a69a-366ce222fa83 | -6.13014 | -59.96322 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce477196-6f13-3666-bfec-ce5ae0434c50 | -6.3017 | -59.9981 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a48b6f-eeec-3dd1-a934-e47627d1e2ba | -6.31727 | -59.96466 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cc2246a-8f67-3706-a799-6feb586a841c | -6.7105 | -59.45643 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4bb949-83c8-31d9-8ba5-cc3b30b3428e | -5.84638 | -57.62711 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6241200b-cb79-3811-a1c2-8a745d5432ce | -7.4181 | -49.86042 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2202b7f-23f2-3aa1-b330-0fc7babf44b3 | -6.63368 | -59.93945 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8c3ecc30-6ffa-377b-b175-dd96ce70af56 | -7.33147 | -55.59259 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3b4fdf7-699e-30e3-90d5-a8876e673b23 | -7.98368 | -47.46987 | 2026-09-23 05:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d70c9ad-e3ad-3610-ae38-fd45598cbccf | -6.35334 | -57.77111 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4902850-194d-3470-ba8b-d57c7b6477dd | -6.89318 | -55.33776 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ccfeaff-1ecc-387b-bb56-82fa8bc1f5b0 | -6.28752 | -57.73929 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87b2903d-0fc3-3cf6-8aa9-c700dc5242bf | -6.84098 | -55.53256 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77aee9f-b839-3c16-9cd4-32879050e2ae | -7.04632 | -62.93128 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b623499-7f7c-3487-b67b-d97a444ae0cd | -6.81877 | -59.45978 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 358389a9-303b-3075-9c4e-00ede3c77fc4 | -6.00363 | -57.71407 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2062d1f9-06cf-3831-8349-f6e5b07616f7 | -6.61203 | -59.96826 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a444bbbd-3887-37f2-ad75-4059a0bbe035 | -6.61376 | -59.91475 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cf70522e-e68a-3603-8dd7-9d1966af2bc9 | -7.14999 | -48.45033 | 2026-09-23 05:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df2cbdfb-7fd2-38e8-b947-1ff280749eb7 | -6.4599 | -59.98408 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4edc6184-768f-308e-89ff-ce91b9d7ac34 | -8.76462 | -45.83857 | 2026-09-23 05:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0b00d69-f71f-332c-b93a-354c6563aa2b | -13.92249 | -47.83059 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ace53e34-1293-3237-9472-6ef0734d977d | -6.67789 | -50.95179 | 2026-09-23 05:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15aadd8e-9c3b-3265-86ef-d5da50c78329 | -5.4541 | -60.15231 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b63edd9-567e-3ecf-b56f-310c81f3a10b | -7.29142 | -59.49964 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21016748-be42-31ae-bc28-fd6379356a54 | -6.46544 | -59.99215 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3be3d48d-4190-3ad9-977c-3ab6bd9f6c6a | -7.43769 | -49.83948 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5109ea5a-b1a2-3390-bc58-e00da002c6af | -6.19333 | -57.78011 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6160dbf-1d59-3179-b336-ad69d52f3fb4 | -6.32004 | -59.96869 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 946081fe-a28f-3ea5-8ff0-a79b26ace532 | -6.55317 | -56.03008 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16aa8d2c-fb5d-35ef-8143-2db40339f08e | -6.42765 | -59.97503 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06741238-3fca-38c5-983f-ac411607d699 | -8.19015 | -54.72772 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98de1326-ab5d-310d-a339-8ac173e24c7e | -6.39374 | -60.01637 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e6ea3345-d63c-3925-9211-a2497093b131 | -6.68457 | -55.05116 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f97f2710-4eea-38f4-a600-b67756dc114a | -6.68387 | -55.05587 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9038dde-59bc-3699-baa6-ff65dd0a9a5e | -6.66605 | -58.55482 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d85b3c1-1658-31c6-825c-892e33de810c | -8.45298 | -48.70176 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed99b536-8c5e-3495-a339-0631cca88b8a | -5.41443 | -60.21607 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68c58ef-ef4f-30c1-bff0-f4cb7dc7b0b0 | -5.80595 | -57.7427 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9978db27-f6f3-384a-8564-f26192ed0a83 | -7.39785 | -55.21765 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a343a3ce-1dc6-3fa7-b6d7-7d362b6b0f0e | -6.30617 | -59.97007 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7c0c9ea-3dd8-35a5-a097-1a2bc81a9165 | -6.34573 | -57.88714 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5223961-0283-3dc6-b376-89797eaa924b | -5.57294 | -60.197 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 169f5ec8-c84b-3979-af81-483d96129dd8 | -8.31161 | -54.77387 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 963e341f-2ad3-316b-8641-b1a481879682 | -6.71827 | -59.00016 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3a9d88c-b41f-30ef-8c95-d2484595f600 | -6.74651 | -59.46605 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04f12ef3-b01a-3ea5-96d6-e3a787f9755d | -6.67269 | -58.55585 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0131fce7-fa32-3cee-b3b9-6d0c52143459 | -6.85461 | -63.01963 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010eca87-68f6-3157-bcd8-019c57f62470 | -7.04489 | -62.94009 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a3d9640-f258-39c8-bc72-63abadabe871 | -8.4607 | -48.68943 | 2026-09-23 05:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 688f58da-63e3-3b3d-8c36-ab443e6f2462 | -6.17726 | -53.29399 | 2026-09-23 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4630c64-5002-320a-a50e-7c3726f30c87 | -7.4602 | -59.99705 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e13be797-d47c-3380-9933-00a10e09313f | -6.30381 | -57.7455 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd6f59a-4864-3b0c-9747-dbee5406062d | -8.25059 | -50.86285 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea2b5ff0-eb6f-362a-9e1c-d75a8692e4db | -6.34942 | -57.77415 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3bdf29b-ab66-38a2-8d1c-e0bf70a89744 | -6.46215 | -59.97008 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be92f692-70e8-3ff2-895a-3661f6bf34d6 | -6.29595 | -57.75163 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README122.md)
