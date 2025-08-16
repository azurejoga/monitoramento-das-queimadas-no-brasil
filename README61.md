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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96f129f-71f3-3c91-a590-29c39cbcc2fc | -6.65966 | -58.81562 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85e9abda-8974-3a93-be3f-b339dfca9999 | -11.35791 | -55.42159 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d2cb05f-9a36-33b4-8850-d00d87018fdc | -14.97752 | -54.71558 | 2025-08-16 05:25:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5dbd3170-450e-32e0-9217-30a264f4dc79 | -6.65224 | -58.81829 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2affe6-71d7-31e7-92be-bf063d685138 | -14.95025 | -54.69534 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 10817886-3be0-376b-ad1d-20e3facd4609 | -13.00426 | -56.86335 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 430044f3-4e66-3923-bc25-33fc47fe8d3c | -14.94336 | -54.75349 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 957d79b8-5d85-3709-8b60-fb60f0c765f8 | -9.55975 | -68.57768 | 2025-08-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bc2b1ec-3da5-363d-8255-bafd0d3e8f02 | -10.39793 | -64.50285 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e9830a6-4e00-33f3-8a28-adc47e883da9 | -7.53155 | -50.52583 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68d63e4b-a86e-3ac4-b90a-138451a656fd | -16.23718 | -51.11567 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 806f3c4d-19fd-388c-ae09-16c1ef6fb79a | -17.21532 | -49.59595 | 2025-08-16 05:25:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 874d1764-882a-36bf-b4d3-a1ea227395b1 | -11.34355 | -55.42829 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f217b9e0-7774-3a52-a4d6-0c966f0deda5 | -11.31372 | -55.20783 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76f3f267-e574-3132-bd89-778b87960683 | -11.35526 | -55.40787 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e66b61-c7bf-3875-99b3-6cc29823edc1 | -7.53739 | -50.52762 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38e350ba-6444-398d-9ad5-9302ed9d2071 | -12.30041 | -50.01505 | 2025-08-16 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f6a15e3-ca82-329f-8bda-46df5e914bda | -13.43447 | -56.68453 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b50a5ed-331f-39a3-a57e-a0c0fdd458d4 | -13.48038 | -56.65947 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4179ad9-5d8c-38e6-a2b3-7963eb514261 | -14.53328 | -48.58469 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19574072-314f-310a-b267-c73928d38913 | -6.07067 | -59.96827 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a283c9a-9ed3-381f-82ec-394f3c683468 | -7.53735 | -50.52673 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e651b1d8-0a64-31c3-a06e-31e6d769319f | -11.36057 | -55.43514 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1221351-bb6e-3395-a7bf-acda1ef25b7b | -5.45634 | -60.13544 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e444311-e0e7-3567-bd5c-20b209cbdb46 | -14.9508 | -54.73233 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1630b2b0-0875-322d-b24a-2cd4b28add01 | -13.14654 | -57.16192 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e46c06d-b883-3258-aeeb-074215e353e4 | -13.01145 | -56.87183 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bb4d815-5004-366a-a86e-cac809742087 | -16.2357 | -51.1304 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bf71615-3cd4-3add-bc29-4b6eaa012832 | -13.12261 | -57.12571 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11b3c868-cff7-3dcf-9eff-f46599b896c0 | -6.13557 | -57.9298 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e81400f7-720d-357a-99eb-2b01c858a1e3 | -14.53399 | -48.57759 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8ecdfae-cb26-39fa-9828-2b20e95e4465 | -14.94104 | -54.70323 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 70722aa6-f687-3552-bb43-e1a117d423cf | -5.93567 | -53.65327 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db914098-6e6e-3752-8de5-d9a8bf971003 | -13.12095 | -57.1691 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10bd07a6-8553-39df-b6b1-a80e88893964 | -14.87056 | -60.08688 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2eba0a3-b0cb-33b9-80cd-617cee80cd4a | -6.70422 | -58.82185 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ba7f6a6-8058-3c98-9ba8-95a7a56e52d2 | -14.95908 | -56.23896 | 2025-08-16 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cbe8dec-d600-3a55-92e3-a3bcf8ec6a01 | -14.94482 | -54.69938 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c8f70813-bfe9-37e9-af39-f016b0caac9f | -13.43498 | -56.68067 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1bbc7a9-80dc-3f3e-b62d-f98ff8340239 | -14.86998 | -60.09095 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2768fa05-15e2-3c6f-b179-69307f463039 | -5.9363 | -53.64879 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a55d5026-c190-3135-aeee-dce02b662881 | -5.62565 | -51.29849 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de72bee7-4b19-3698-a9cd-885de3a3574a | -13.41748 | -57.02975 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7f17317-b855-3f74-9f81-d670843ffe14 | -6.13911 | -57.9303 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0181c86e-0b22-353f-9091-6aa3bcfe5726 | -6.65566 | -58.81882 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6697ff9c-2c6a-3975-92cd-4266e42908ce | -6.64952 | -59.08576 | 2025-08-16 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de3d22a2-9c19-31b1-8fd1-080bfb23ddc5 | -11.34794 | -55.42897 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9719308c-9e3b-358d-babd-e83ced46958b | -6.08318 | -57.91772 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abca10d0-7759-36e4-938f-1e5405a6c8f7 | -13.00375 | -56.86707 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56204c21-2790-3c8a-a375-3a601cda41b8 | -5.3253 | -55.946 | 2025-08-16 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77d8cfc3-a93b-302a-9d5a-2a9213aeb533 | -13.00224 | -56.87811 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7995774d-a9d4-3c4d-b06b-651059d8768b | -13.1136 | -57.13166 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d7f92d8-3283-3a53-8de2-ea720324fc9b | -13.12545 | -57.16613 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5ce6f78-14a0-3b3c-b6ee-f26e19ec58f6 | -14.93622 | -54.70221 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2813b6ac-9ed5-383f-af42-47d37c7d89b1 | -5.62861 | -51.29671 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 827008cd-18b3-3b16-b55d-1ffd9166321d | -6.16716 | -60.09073 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02c58fec-786d-3677-ac2e-18ef6efd57c5 | -10.04654 | -64.89627 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a952d0ab-5226-3adb-b0e5-14ae51458635 | -14.5262 | -48.58365 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e059057-1caf-3d5e-a436-eafd8c13dc20 | -6.13497 | -57.93377 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 206faec7-24ab-30f9-9e8f-457f928c7834 | -12.29634 | -50.01384 | 2025-08-16 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b06a567-921a-31aa-a3ac-267e49b29ad2 | -11.65431 | -51.62454 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f69f1bb8-54bb-3db8-816c-1b0db3a98fba | -6.70085 | -58.84422 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f2b38a8-1161-3d8e-ba1c-287f20974e5a | -5.9317 | -53.64812 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 004edad4-e39e-3500-9ce9-535a1c86e6fb | -10.33724 | -64.47631 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e6de988-d609-33c4-9fbb-c08705b7f37c | -6.07176 | -59.96132 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36c04e9f-bc6d-34d5-8ff5-2f778cd4e064 | -6.08056 | -59.94841 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce65be5-cfa8-372c-9185-9563c032d68f | -11.34586 | -55.41096 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4454bfc-db5e-34c4-ae8e-c0557bde6be2 | -6.0723 | -59.95784 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1874f55f-cbff-3a18-bfae-9d9a01389e69 | -9.5608 | -68.57536 | 2025-08-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f3c9774-1fcc-3bbe-bcfc-07a6795c81b6 | -11.35235 | -55.4296 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 173c0805-87be-3041-9f7c-d20b050df6ad | -14.94541 | -54.69441 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ea919c56-9329-3c60-8155-760a86c73b12 | -6.07399 | -59.96877 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e2326e6-336b-3677-8ae4-010c31063a90 | -13.45218 | -56.67924 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d83a291-b9e8-3af3-8692-2a91b4b45752 | -13.11236 | -57.13255 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11220c0d-c76f-3c3a-b219-2e83d333243b | -11.34852 | -55.42465 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 336246b1-1f56-37eb-b1be-412d760b5642 | -6.07121 | -59.96479 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67b49579-74f6-3700-94e0-267dccbad25b | -13.44956 | -56.66702 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d06902f-7a9c-33c4-9d10-ca7a86cc0439 | -14.95852 | -56.24345 | 2025-08-16 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 029b4158-9958-3963-bd57-b68e01167979 | -12.89091 | -62.09064 | 2025-08-16 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed687e70-4541-322f-9f17-e5971d5a0f3a | -14.97127 | -54.72649 | 2025-08-16 05:25:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca895b35-00e9-3bf2-8458-e6661d4e5147 | -13.01196 | -56.86812 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01687344-240b-34a7-8043-9de9a31479d3 | -13.11645 | -57.17207 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4046d7b-8a9b-3bd0-81c7-a68dc203b2b9 | -13.13752 | -57.1679 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fca4343c-bd85-31a5-9e73-5c8cac029cef | -6.66708 | -58.81293 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9836a8b0-cb74-3090-ae76-5d34c40a3823 | -6.66308 | -58.81615 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d13fd4a6-c972-3ab6-9cde-0bc4df0d3102 | -13.12852 | -57.17385 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 180a4ee3-6234-3699-9a67-eb410be6696a | -11.34297 | -55.43257 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d081386d-6f6e-3cc5-bf48-41356134605a | -6.65908 | -58.81935 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 021571ea-89ea-3906-b0e4-d5225ad0f681 | -6.1491 | -57.93588 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07efd628-0a68-30d6-a6e4-fc67cf9fb239 | -11.66051 | -51.62121 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ea1931b-0a72-32ce-9580-921dc412f2d9 | -10.67411 | -60.77468 | 2025-08-16 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e91cda0-17a2-3d92-8fbf-b64940528433 | -13.14203 | -57.16492 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4a17b14-2c8d-331e-ae15-fa4a140cf099 | -11.36351 | -55.41338 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3b2d787-a479-3e7d-b49a-899c5374676d | -13.1129 | -57.16793 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a8dc1b-d6a3-30e2-9cbf-1172cdc43f8c | -16.24237 | -51.12694 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0663e4c2-7f97-3aa9-ad53-049d6a44bd5b | -11.3512 | -55.43813 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af14024e-f251-3d39-8660-aaa84f110992 | -14.87464 | -60.08343 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f706e1a1-9523-3dea-aef8-abc3983808b5 | -14.95306 | -54.7548 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec4a0829-28c8-35bb-95f1-9a809aaabaac | -13.00735 | -56.8713 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33da80b6-5ef7-30b3-9f28-e806e9c8e4a5 | -9.74197 | -65.32687 | 2025-08-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
