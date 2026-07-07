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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73d35f8c-ea98-3de0-bec6-6230f8bce62d | -6.66935 | -50.91319 | 2026-07-07 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 169361c8-27ee-351e-98c1-3d3504d3f58a | -10.6955 | -49.6078 | 2026-07-07 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e7e6955-c2eb-3bca-848b-e0c89a604518 | -8.11949 | -47.11106 | 2026-07-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6622c9cf-414f-3217-8402-fa5d9afc6202 | -6.90614 | -43.71055 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73ee1ffb-c089-34b9-98bc-f76aa20218de | -9.20318 | -45.31839 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9b5bb8d-af10-3fb0-bf6f-8e83b8c09261 | -11.67813 | -44.55598 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e46f45de-20dc-3e4f-9657-60a138c60b02 | -6.92743 | -43.70459 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d155fa3-18e8-3ca0-a75e-ff32954235f8 | -11.3089 | -54.47143 | 2026-07-07 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f2dd0cd-9bd9-32ee-9415-ad44405dbbc0 | -11.69173 | -44.5536 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c89df6de-81a2-31ef-bcbb-d26add224350 | -12.36236 | -47.4275 | 2026-07-07 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421e2b2d-b5bf-3170-a851-e64586d45a84 | -12.78402 | -44.49751 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35df4637-1154-36fc-8073-60deaa65328d | -6.09882 | -49.59314 | 2026-07-07 04:44:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25a03b66-bc4c-3388-bfc4-7029d34f279d | -11.67756 | -44.5602 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b9e2015-46a9-3abc-8e44-369ecb785428 | -12.79407 | -44.48987 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0d7fa235-bcb8-32c4-ad0d-5c528e539bb2 | -11.48621 | -52.91692 | 2026-07-07 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2b0f48d-ced3-3893-a64c-075fdedfba18 | -6.91026 | -43.70214 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d845700-c991-3f1e-8309-35e41e1173a2 | -6.4968 | -42.22499 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c6ee887-37f5-3ebb-a9f3-2ae11bca6d73 | -6.90675 | -43.7065 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b09286bb-df69-383f-9733-a64bf191098e | -11.69115 | -44.55782 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87536cc9-229e-3c8f-925a-be433b8336fd | -12.35933 | -47.42257 | 2026-07-07 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae193f0d-d1d8-39a3-bddb-b381a704a97a | -6.93231 | -43.7011 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b880170-ca2d-3434-b72d-4028d25fd0bd | -6.49544 | -42.23462 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b532496c-6c7f-3012-8163-4f21c9311e85 | -6.4197 | -43.51554 | 2026-07-07 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 118bf54f-edc4-3ee9-bc02-b4d3aa647669 | -12.50708 | -48.26361 | 2026-07-07 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fabbb487-9ab4-37b7-8e82-c3046c67ce54 | -11.69886 | -44.13241 | 2026-07-07 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00b96b9b-3a69-3edf-a05a-04ad911964e8 | -10.76208 | -46.63192 | 2026-07-07 04:44:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f94797b7-b2a2-369c-90b6-2ab2d3d76308 | -8.03924 | -45.03713 | 2026-07-07 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf9aac87-f572-3c35-9754-59f3b9711630 | -5.80464 | -43.79991 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d72571c-fb5a-3f47-9c5b-12f10730aa80 | -7.63689 | -50.02986 | 2026-07-07 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5989f2b-7960-3a65-a75a-2e29ea5d437a | -10.11988 | -52.09142 | 2026-07-07 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb9add0-461f-3c9e-b8e8-5bd9ad419c6a | -11.28209 | -47.31057 | 2026-07-07 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c325366-b0b1-350d-9ea7-0180b9175241 | -11.67093 | -44.57644 | 2026-07-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e10f760-a8c0-3953-ac54-cbcea9c69de2 | -9.40352 | -48.02122 | 2026-07-07 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fad791af-812f-3536-97ae-64a71c2ad4d2 | -6.50363 | -42.21083 | 2026-07-07 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7f19a932-38e0-3fbe-81d6-60c13442eb5d | -12.79288 | -44.4987 | 2026-07-07 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f41b79ae-f617-3de3-bad1-2ced59cd2380 | -5.80342 | -43.80099 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1b1f0b2-08af-31d3-a12f-e13d2ec96b3c | -11.64356 | -50.36683 | 2026-07-07 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 05f06e1b-3731-3cb0-8f93-393a6cad1fc8 | -9.28419 | -49.58006 | 2026-07-07 04:44:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c883ead0-e2ae-3126-bbc9-df4180a7d364 | -10.9315 | -43.06 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9b907703-bbab-317f-b8a8-0451abc8199a | -7.00432 | -42.76804 | 2026-07-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2989b034-6e6a-3a28-9850-9f745a996202 | -9.368 | -48.80294 | 2026-07-07 04:44:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2130c6b7-db3e-32f1-a796-3b0d3e0d5688 | -10.53558 | -44.12347 | 2026-07-07 04:44:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39499060-c00f-340f-89c0-7c27ffff5516 | -5.90893 | -43.85385 | 2026-07-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12160fc0-c603-35df-9c92-47566e803965 | -10.90182 | -56.85805 | 2026-07-07 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc5c8d0f-2387-35a7-a0b8-323f8f55d873 | -5.43619 | -49.25114 | 2026-07-07 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05b5e4a3-bb7e-3e99-b47b-b9a9ad75a00e | -6.90446 | -48.04379 | 2026-07-07 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce5d101-86dd-3780-bcf3-5965163185b7 | -10.94032 | -43.06647 | 2026-07-07 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ae30ff2-439c-3a5a-907e-09b7af455978 | -8.07152 | -46.69212 | 2026-07-07 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb53a95d-5956-346e-bdb8-1047e919ac79 | -6.90482 | -43.70963 | 2026-07-07 04:44:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1aeee4d1-e828-3dd0-8a32-006263f01780 | -13.2115 | -54.36843 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7692cc66-251b-362e-94af-0dc2ec554c2a | -13.22668 | -54.3014 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb39b07-9aa3-3c5d-98b0-2e55905fbf5b | -13.32394 | -54.36985 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26aba8f-8054-31a3-89c3-394cc7939f83 | -13.53369 | -52.91571 | 2026-07-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee4b9405-21ea-30f7-a639-f65cad01127e | -13.08071 | -48.16548 | 2026-07-07 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60a58e09-f82a-3238-aa40-9d366afc086d | -13.25979 | -54.34638 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09855d17-82a5-3561-9791-85e53e5b6509 | -13.27559 | -54.34058 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf087025-e809-3cec-b56d-468ab256b0da | -13.28155 | -54.33608 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f57e5aad-f3c2-3541-ad93-f832a6390f44 | -13.27502 | -54.35231 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769419ea-2da0-346d-8e61-7d5de8a2f20f | -18.08903 | -54.02858 | 2026-07-07 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2831593d-80c3-3257-9af3-8055052e457c | -13.28869 | -54.35908 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a73a8e2-e4a2-33d9-abe9-c225999a7287 | -18.50413 | -51.592 | 2026-07-07 04:46:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e302f220-2f8e-3462-87a3-ee93d699e66b | -20.52595 | -43.96895 | 2026-07-07 04:46:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2ce9e0d-6ea7-3781-a5eb-79ff338324b6 | -13.27935 | -54.34876 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f10de1-fa5c-3cba-915f-6f509014dc4f | -13.28279 | -54.34185 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7075752-68db-3727-b4df-b443946dc02b | -13.27429 | -54.35651 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55fdc843-1252-304e-824f-ea8259b264dc | -13.2641 | -54.3428 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 977366c5-0541-33e5-a685-7e66b9a4707a | -13.27575 | -54.3481 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6419636b-bc5d-380b-b6b6-db15030c8548 | -13.27789 | -54.35716 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeae8985-4060-3f8a-a707-30741f365d25 | -13.27565 | -54.3623 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c78cf66-c8d1-346d-9c81-4d3b9e681c8b | -13.60021 | -56.61061 | 2026-07-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e38114f-b6e3-32aa-b57d-b71ab5c14b42 | -19.85388 | -49.07192 | 2026-07-07 04:46:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e27534-e366-3cb5-8d0d-6bbcbf9b3d54 | -13.26916 | -54.35677 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42bbe59-0833-312a-b8e0-366bdd29914a | -19.0614 | -52.8863 | 2026-07-07 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a120a1b3-82ff-3608-bd70-aed77f065ada | -13.27113 | -54.23549 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b7600bd-2081-3567-88ad-b060419eaa35 | -13.27493 | -54.36654 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c871deb4-4d9d-3f3e-864d-d851155393b5 | -13.27721 | -54.33968 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b9b57ab-0e0e-3565-b54d-b688544dca2b | -13.27706 | -54.35389 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3856c975-edb1-3226-83b4-822a1aac5320 | -13.272 | -54.33993 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a620cfd6-908a-300d-863e-0385f46e6ed2 | -13.31748 | -54.36425 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79e0377d-a880-35b7-b71c-4f370276017d | -14.01507 | -47.37646 | 2026-07-07 04:46:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e73e7152-7069-3879-9e65-82bea15f44f9 | -13.26897 | -54.22645 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5a8f569-fd1c-3399-8a4e-d2657f9ea6eb | -13.28515 | -54.33668 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bc76781-731a-3230-8c72-b04830839f3c | -13.30596 | -54.36649 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d33f46a-8e26-3579-8f8d-aa08e0e97321 | -19.06471 | -52.88689 | 2026-07-07 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf5bba5d-e3eb-3267-a784-1aa1f08d68e0 | -13.25824 | -54.22454 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc04fa77-67f9-3869-94cc-c6685359d367 | -13.28926 | -54.39873 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce784206-8472-378c-b2d6-6b0b333f6e1d | -13.28002 | -54.36626 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4dd7f9-0016-3a10-af38-69bd25424e3b | -13.28875 | -54.33729 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9178e51-0a88-38a9-a174-416f56418c81 | -13.29074 | -54.39017 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e95a4ce2-fadb-3ee2-8408-9df773272ef8 | -13.26698 | -54.34769 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42b75ec5-61b5-3125-a006-6a1ac005c197 | -13.28442 | -54.34092 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f839c91b-d611-3166-8409-fee1c4ca3a92 | -13.25395 | -54.22807 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26a5fc0e-7614-3e01-a401-920ee00162cd | -13.28655 | -54.35 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3aab6be1-fea1-388d-baa5-548eda34a6ab | -13.25753 | -54.22871 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c738089a-e695-330c-8b8c-303bc4687fd1 | -13.53431 | -52.91198 | 2026-07-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83c352f1-d2ef-36b5-8cca-3695247597a5 | -13.28295 | -54.34938 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97eb8acd-c939-3505-81cc-d6ee4d91aa99 | -13.28582 | -54.35423 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59767d57-b7e4-3e44-842c-5b525def5edb | -17.64637 | -46.41388 | 2026-07-07 04:46:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4faa4fb-38d8-3183-9df2-05f1dd86e8f3 | -13.24824 | -54.30522 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 510f0efe-4897-37ab-85f3-886419721b5d | -13.31888 | -54.37772 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
