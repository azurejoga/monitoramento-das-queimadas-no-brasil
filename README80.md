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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 733e211c-a8dc-33bf-a813-4b7fccf400c2 | -3.76356 | -54.81275 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ddbe6aad-133f-3599-8068-914338ffc9cf | -3.76677 | -54.82098 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c15c8b99-cc30-3709-ae17-3e78de7e1ee9 | -3.76219 | -54.82195 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f6aea32-7682-3e0e-844a-b1b6b516bd4f | -3.75666 | -54.81625 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 913ab318-4694-3774-83fc-77af027e47ea | -3.76288 | -54.81733 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e62916cb-86fd-3797-acfe-fc6c55c3fdf2 | -3.76743 | -54.81637 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daa621e2-97a9-3824-b3fe-3a35a80c1cfb | -3.76121 | -54.81525 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd9013c3-39ae-3e3d-a752-8eecd51c93f0 | -4.05255 | -56.33402 | 2025-08-28 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e171079-2efd-32bd-a44d-6a9022f01c79 | -3.76186 | -54.81069 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1417a513-9857-3e0b-8946-3a0a267c7c79 | -4.05823 | -56.33493 | 2025-08-28 05:46:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd6fd0b-e0c7-389c-bbec-9bd6d98f6770 | -3.76056 | -54.81985 | 2025-08-28 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6db49a6d-4915-3b26-8dd5-8155c97d3850 | -9.25706 | -65.90123 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03d3d661-abb7-33d8-a352-2d4f69e8183c | -9.13563 | -65.77699 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f75c5f6-3329-3505-9d6f-b478d3324550 | -8.9504 | -65.95926 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f49312c5-252b-3d09-9bd0-eb3910615d50 | -9.12427 | -65.78283 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6e2aaddc-a738-3917-bdfc-aa8a8708738a | -9.15209 | -62.35554 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b50fb159-4052-34fb-8720-1bf9b856b5c9 | -5.99829 | -57.85285 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e607dcc-c765-3c38-bdaa-c677f68e612b | -9.2001 | -59.54379 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711ba78a-6b71-3aaf-b24d-639d49930afc | -9.13613 | -65.28677 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65ec706c-a7bc-3dcf-a4bb-fa2559360242 | -7.46711 | -61.39937 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aa83462-e462-37ae-96b2-556b8e2ea4ec | -10.4606 | -57.96092 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e77c82cd-469f-3f92-8c18-af5d1b1879f5 | -8.57853 | -63.92711 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad49820e-65ac-3b06-8196-bd4d07799992 | -8.93003 | -65.93367 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5116e1a2-db8a-3146-beb4-7d271b7fa5cd | -7.59666 | -63.34566 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41caa47a-999f-3b64-9eb2-6a396cf1cf00 | -7.54282 | -63.83727 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 188e6077-1ffd-3075-9404-bd7621e94773 | -8.95773 | -65.95667 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da4172ea-f0f5-3fbc-b832-181dcb610348 | -9.41248 | -60.57687 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4ccf67a2-ed46-34f0-8318-49edb3925338 | -8.68146 | -66.91009 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c6e5a9b-88c5-3188-8f70-0e9ba39e3ea0 | -9.49489 | -62.39624 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 056c1b78-e489-3aea-b70b-5272a2d6f21e | -9.53521 | -62.40583 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f47dfbd-808e-3eac-803d-79c584dda062 | -9.11802 | -65.77808 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 66836a13-bb4a-3b25-a5ea-bcda17bd5f7c | -9.63556 | -67.34379 | 2025-08-28 05:48:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8588950-1829-39fa-82cf-efb8ff619b29 | -6.23834 | -60.00613 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 117831cb-4013-36ec-bc16-e2f99922d910 | -8.89857 | -62.47631 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e214ef-0f64-3a34-85b1-7a631c200641 | -8.94124 | -64.15279 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c88b72a6-5d4a-3408-879b-e082075971f0 | -8.88801 | -60.74994 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87039b88-92a5-3d75-955b-39847b198725 | -8.9272 | -65.92947 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26a30e17-e26e-3e03-acd3-da25c38b83f0 | -9.06677 | -66.06682 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce350f1f-eb40-3772-83d2-eb23a8258c22 | -7.46344 | -61.39481 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66810922-8414-3f38-b142-78571a48f0fd | -10.47863 | -57.9387 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e294084a-bce2-348e-a199-5020cd18e247 | -9.13266 | -65.28623 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ad6febb3-41f1-3c40-b185-833fe90e810b | -9.19821 | -59.5479 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ecbc63a-2624-3ba2-be14-498cc3eab89d | -9.15158 | -62.35915 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 417563d9-4d51-3d59-a671-488e6cae4ce4 | -8.94646 | -65.96238 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9882c6bc-ec5b-3bdf-9eaa-79728c1f4522 | -9.12257 | -65.77117 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 025bd53e-a2fa-32d6-aa24-3c3ce4065daa | -9.18112 | -60.86361 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2b1bf68-19af-3a7f-bb8f-54309b3c1359 | -9.53574 | -62.40218 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24eb09d6-16d7-3ace-8dc0-a83c886fb1b2 | -9.16437 | -65.79617 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a7e262e-b495-3cb6-abeb-f2b821336fb9 | -8.57175 | -63.92785 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0849456-fb08-37ef-a227-89882f1bb49b | -9.40184 | -60.51629 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b43fa6-f05d-3727-a45b-e1bb82ee1ae9 | -9.54036 | -62.39913 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab70110c-6a32-344f-8a72-488b962b4a66 | -9.19515 | -59.54316 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ec7b1b-3641-39cf-8a5e-794bea5e5627 | -8.9549 | -65.95249 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce2de46e-6167-38f8-92bf-eb025fb06f7d | -7.40337 | -62.29108 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3702449c-54cd-3052-9bdb-7770c15b72d3 | -9.46405 | -60.30373 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8676b989-6b6e-34a8-937d-879686b9776c | -8.9594 | -65.94572 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82a93d66-305a-3c35-b3ad-da88684bfc44 | -9.0634 | -66.0663 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92df2197-bc7b-36b4-a4cc-753c99ee4031 | -8.99462 | -65.41927 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97b4f8c9-33fe-35ef-8ee7-4908a1ea7598 | -8.34345 | -62.94494 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94e3a53b-c12d-3f5c-8e19-56c10d88d4ec | -9.19898 | -59.54239 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f151400-2da9-3da9-a452-b3d5cf28cb23 | -10.47235 | -57.95818 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dc8decd-7c37-3f7a-8e7d-8a23f4312126 | -9.12938 | -65.77223 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a391414-a164-3408-8f2e-dbd01d6b1ff0 | -9.1868 | -67.75768 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bd3b1ffd-d5a7-3f9e-b08a-7536007caff1 | -8.69649 | -63.83483 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7d94443-2e2a-31e3-bee8-c35e71402772 | -9.08504 | -65.74261 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 79fed1d3-71c7-3542-990c-49a1198aadf0 | -8.95661 | -65.96395 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de82e453-bb27-3595-b05a-eaabb2e2d5c3 | -10.47351 | -57.93399 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 74b59037-a8d1-3b06-871b-893b7d5ea36e | -9.4032 | -60.54112 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74937ba1-e7d1-3435-84ab-8ba63b1c713a | -6.23702 | -60.01543 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a7b167-0cc2-36f4-bae8-165fa3cef998 | -8.44695 | -70.14591 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2293d5c9-3799-32d9-a0a3-64fbd5de2196 | -8.95717 | -65.9603 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faa5cf4b-abdb-388a-bb64-10aa726e62c1 | -10.47384 | -57.94674 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5081f704-b61a-3654-99f2-0bef8e682499 | -8.88673 | -60.75902 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a502fe-917a-3dcd-a9b5-03cc369979d1 | -6.0135 | -57.85205 | 2025-08-28 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec673ef-7f1b-3145-92ff-2a85961fab08 | -9.41509 | -60.52309 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8381660b-dbd8-38b3-9cb2-ee2b0168a606 | -9.73497 | -64.90164 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 283600af-4d80-397c-8135-75a4be7d12f5 | -9.20949 | -60.85824 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7f27b28-759e-3d7c-8cd2-b15dbf83c99b | -9.16381 | -65.79988 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d83070d-0849-316e-b15a-aa69da995c58 | -8.93797 | -65.94985 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ea3e027-4577-3553-9f8b-2228c8c15ac4 | -9.40783 | -60.54179 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658aa5fb-4c37-3dd9-a1a3-b45fe63984d7 | -9.66476 | -64.98658 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43a0693d-4368-3d95-ac7b-a730e469c908 | -8.51487 | -69.7936 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21a695e5-d8eb-3a75-a864-c14a9123f098 | -10.31788 | -62.62069 | 2025-08-28 05:48:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 183d01a1-9664-3d2f-8c5f-c045b489c20e | -7.40228 | -64.34335 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 155114d8-1cc8-342e-b750-15dd0440422b | -9.54801 | -65.68968 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 630cbcd2-3ced-3d53-8b22-ab260c26d380 | -8.44472 | -70.13734 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3300f8f8-a5ea-372d-9d8a-623ecac319d8 | -9.12086 | -65.78232 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c66cd305-11f3-33ad-9378-fbc689408e27 | -7.45807 | -61.40208 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48d31921-651b-3225-ae35-13355c143647 | -9.46807 | -60.30946 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e6e03fe-f698-346e-8dcd-aadf21e0e7fd | -9.25762 | -65.89753 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7000a2cf-5fde-3dfe-b43e-eb3764f9506c | -6.23768 | -60.01079 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cebf971d-651b-341b-b52f-5fc405945d83 | -9.10892 | -65.74632 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57b87e26-3a07-374a-a830-06275bfd3712 | -9.66123 | -64.98605 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafa2000-ffed-3e1b-a15e-97fea2286635 | -9.10551 | -65.74578 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc531635-dbe5-3afe-a94c-65cafda54b9b | -8.94813 | -65.95144 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9203a514-0efa-3f67-9a2f-cf19641afbcb | -10.46926 | -57.93821 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c47e4f66-50cb-37df-af9b-3f05bd5063ac | -9.13728 | -65.27906 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ba99bcf-bf71-3fc4-9c5c-d91834151a31 | -10.47255 | -57.94176 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d3850b3-1c4f-34aa-b8d3-6c0fce1d2f1f | -8.94868 | -65.94778 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00042635-eaed-33e1-9cfc-d12cdb3d702f | -10.4641 | -57.96421 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README81.md)
