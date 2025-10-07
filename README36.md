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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00ab6d75-86a0-3012-b978-1a0e21022e4a | -12.34855 | -47.05755 | 2025-10-07 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e91c2f08-3264-3777-b364-073c618a8e9b | -16.10987 | -48.94442 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11bdc039-8d4e-362c-a794-6331ba1fc914 | -13.35845 | -47.56284 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 436f093d-fdbd-3301-bb3c-d5dbf35bd236 | -15.88484 | -46.25234 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26d4f7ea-7186-3e56-a7c3-e36c6b2693ed | -15.17126 | -52.77466 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdd63571-e6bc-339b-a3b1-de87823e65be | -14.7983 | -44.37332 | 2025-10-07 04:10:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1af5b1e4-2af5-36ba-bf56-38cadc51e9bd | -15.50656 | -46.83044 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dcaba82-6589-38fa-a1d7-c2aa717e63d2 | -13.28676 | -48.0571 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 751f1ecc-12b2-3641-ac71-fab7c475ea40 | -18.97291 | -47.82786 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1072c4cb-7560-3bc5-85ab-fb7fdfc71467 | -20.21021 | -43.92001 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a68e68f1-a24c-3484-936f-ac3d20ed086a | -13.2627 | -46.46988 | 2025-10-07 04:10:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b54ae95-f606-31a2-a4a2-d69501a860d5 | -15.58628 | -52.55606 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a488855-5337-34a8-81eb-1e131521418a | -11.15068 | -54.88372 | 2025-10-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8950b76e-bc0a-3e82-ac23-9e8c4123b757 | -15.29293 | -46.32988 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9d9ad18-6ef1-397a-a655-4df5402751b4 | -12.25594 | -47.16498 | 2025-10-07 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2fac0cd-4144-326e-902b-80424fa534d7 | -13.07247 | -47.83018 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cac0024c-485d-399b-bdd2-a8c6b8d72051 | -13.27847 | -48.47841 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59edfc14-0782-346a-b247-e36705655561 | -15.75979 | -43.59016 | 2025-10-07 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bac453cc-14dd-3640-a58b-23f0a3f7a7cf | -13.68924 | -47.95092 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f6de5ba-e3df-3110-b031-e20a1bf580fa | -16.2876 | -50.97752 | 2025-10-07 04:10:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcf666a3-1fff-338d-aa87-48307322d3df | -15.17419 | -45.73062 | 2025-10-07 04:10:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60e5b1c7-651b-3fe5-87bf-4359f58a549f | -16.34361 | -47.06046 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d4948b7-491c-308c-be7f-5c103037bff7 | -14.75541 | -46.02588 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e33d7101-3ba3-3628-953e-a0285388e5a2 | -15.21414 | -49.29577 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c62eaa3-9077-3484-91a0-e4b98b27d504 | -13.09392 | -48.00665 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d19a0ec-efe7-3dba-bf10-8940b25b2040 | -17.40384 | -45.04658 | 2025-10-07 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c8de15b-0fdb-31cb-9a2b-a7954ed3d6c8 | -12.25956 | -51.34264 | 2025-10-07 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 590f4732-bfef-318f-9d7d-d6ef6cee1f8e | -13.07235 | -47.87788 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e410a4e4-94c2-3790-b15a-84a9286e5940 | -18.10982 | -53.35041 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 567d1e36-5e51-37cd-9767-4282330fb50c | -13.71192 | -48.07382 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41ca726c-e951-351a-8cfe-7694de3755f7 | -15.27058 | -48.05687 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82fda261-8421-3685-a57c-15f3237405b0 | -15.96852 | -50.83608 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58a2e42f-49b3-3da3-b2db-7226240d6d99 | -16.11054 | -48.94075 | 2025-10-07 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d416d211-cf9b-38ff-abe7-eae943f560f2 | -15.58044 | -52.57099 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adcc960b-70b1-30a2-912e-51aadee85af2 | -13.3282 | -43.7286 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eded253-106d-3a98-aa58-16ad001fcc55 | -15.57722 | -52.56034 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea24eec6-7e13-370b-84d8-bcebaaa52fca | -18.52284 | -43.41745 | 2025-10-07 04:10:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a48cd6f-ec4f-3fbf-a3df-8f320c2e445f | -13.34461 | -48.02946 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0941617-a4ff-3589-8e0b-d60657df5de5 | -19.11073 | -43.1663 | 2025-10-07 04:10:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 77659d9d-5ff1-3cd7-b94c-9ea948a072ec | -13.70705 | -48.07837 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d499c825-81df-32de-8a8a-919a09ddd5a3 | -15.49992 | -47.92732 | 2025-10-07 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 97f4b7fe-e560-3960-8a49-16cffdac9550 | -12.99366 | -46.79131 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9727c81-8631-388f-9b9b-6eacae7260d1 | -13.67372 | -47.94757 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ee086af-21e8-379a-9572-f9a28a9cf1f3 | -13.33826 | -47.56512 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc1916c6-4299-3bdb-a20f-3b391babe878 | -14.73656 | -46.01012 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2698305d-7d9a-3852-8b51-c4f9dd97b101 | -13.5818 | -48.14556 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24857d24-74e5-3a72-9dda-957a867d8dbe | -13.83679 | -48.03047 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd2151d4-f128-37c4-ac68-c4f870a4b50c | -20.10196 | -44.18464 | 2025-10-07 04:10:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2beb4bd5-0300-334f-813f-9cd20efc56d2 | -18.10471 | -53.37542 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4661f364-4aba-32d2-b5fb-29dee269c3fa | -15.3491 | -47.32866 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cda58803-e9ef-395c-aadd-5b88a3d029ac | -20.55637 | -41.70289 | 2025-10-07 04:10:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e967c934-2542-375e-a7e6-6dcd9e782b2d | -17.26101 | -46.79853 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e67e43e-165f-31b8-81f4-0f1a9a33db32 | -18.11229 | -53.36439 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aff63ee-bffa-3301-8826-4ab0465d71f0 | -13.05598 | -47.92576 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3cc13c0-9467-3923-b796-c9761c734a07 | -17.96166 | -44.40938 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90eb3a19-c0f2-3631-98bb-353dc38475ed | -11.15812 | -54.87963 | 2025-10-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b08a83d-b050-3952-b3a3-4771edd61471 | -17.97807 | -44.99183 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66f2f8c3-4d4e-3d8c-9b65-9b8b70b1c16c | -15.31625 | -43.09308 | 2025-10-07 04:10:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2518f6a6-d675-31f2-be8c-6303e4726fea | -14.65613 | -48.37505 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92b71dd2-aa59-33ad-a173-ee0f076f872b | -13.05747 | -47.89367 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 53e8b8e1-0824-3b30-9685-f451a8570d79 | -13.3255 | -47.5568 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3603e887-b839-37f6-ba3b-81ba9410956d | -14.76119 | -46.05563 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70a06b8c-d7e6-3302-8865-58463cec6c6b | -14.64286 | -52.53411 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bba8670f-3c90-3042-be86-f339271cc8c2 | -14.36607 | -47.72905 | 2025-10-07 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5630eb2c-1290-3a4f-af6f-8381a38f436c | -19.80925 | -45.33545 | 2025-10-07 04:10:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe083c6d-4626-32c1-a81c-504cbbf7ba02 | -18.04671 | -43.15166 | 2025-10-07 04:10:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 1cbcea23-38d4-35bb-bc47-75e84f4d8f4d | -13.22566 | -47.80921 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7dc27b33-2735-34db-9900-748668161a41 | -18.10619 | -53.36818 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 081cdf9a-adba-388e-b594-46631daaf1ed | -15.17192 | -52.77131 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e360c93-bca7-357f-99d7-b49660fef2bd | -14.92439 | -46.80637 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05405afa-189e-34ff-a715-f0cff9d0d5c8 | -16.01928 | -48.03149 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cccd3edd-55f8-30fd-8dbf-45de28521422 | -14.92808 | -46.80654 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0237cfa8-6f99-3781-a55d-b42ddadc9481 | -13.30437 | -48.04985 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd7bed03-1a0b-34b7-bbbb-f052831613ea | -14.93306 | -51.43345 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f3e95de-2cf7-3462-8756-315a6b16a800 | -14.77365 | -46.04548 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23b28cd0-720d-3ee2-92f1-44467b4c921a | -14.65103 | -48.3581 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b086caa-cb8b-3793-96b7-44037f4aedde | -15.50298 | -46.82983 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8149bc3b-b359-3ac8-95a2-349d112f5c5a | -17.16554 | -43.44836 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffe7e023-e7b6-3ace-bd95-73f98fe7e62c | -13.27131 | -47.57256 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58fcefe4-2a13-3b1b-ae28-6486be0d9bcf | -20.20965 | -43.92371 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eadf3377-a7a7-3438-ae3e-63814fc30b59 | -20.51618 | -42.84721 | 2025-10-07 04:10:00 | NOAA-21 | AMPARO DO SERRA | MINAS GERAIS | Brasil | 3102506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ac2e5906-e2b4-3b5c-a821-230ec5f84111 | -13.58901 | -48.68554 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed288aef-cbd0-3892-84ab-b33304b52ba7 | -14.75327 | -46.01729 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 181e1978-8570-355d-b3b7-8c0ea60ba0c9 | -16.01899 | -51.04393 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 207a8b3c-6762-31bf-8903-0ddbc8d222d6 | -14.93205 | -51.43884 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4be921a3-58cd-33e4-85b9-3154369d9480 | -15.5836 | -52.56928 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 083ba789-8d91-3c00-9c45-c3d9586e67ef | -14.28272 | -45.8482 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88acf8d2-eaf0-33d8-a4aa-24361db80c02 | -14.76386 | -46.03965 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ff7562-c9de-3872-994c-dde863cb9d47 | -12.99075 | -46.78612 | 2025-10-07 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1df74239-fb00-3a6e-a1ab-55dd67c8918d | -18.66959 | -44.03642 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91373d82-2381-3979-8f2f-5b970aafe2fa | -14.61913 | -52.49159 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9eec50bf-d104-33c3-a12f-e41c139fb9c9 | -10.55811 | -56.55357 | 2025-10-07 04:10:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bda73358-d083-30c4-948d-da2d3a39aa38 | -15.97307 | -50.83683 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74ec1ecb-a2d7-33a6-9c78-f662efd93061 | -13.25413 | -48.05687 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4016121-d488-37fe-95b4-d91cffb3f56e | -13.57479 | -48.14664 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f48200c-f675-3daf-af91-343e0b49ec68 | -14.74979 | -46.01668 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c42676a8-be12-3a70-8315-272300b1f2df | -13.23919 | -47.80085 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8785463f-1846-3732-bd69-ae39b7781173 | -14.75407 | -46.03386 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5746c2f-0c0d-3677-ae1b-6d560593f078 | -18.56878 | -49.25388 | 2025-10-07 04:10:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 87d1a3ef-0391-3ae6-a2b5-4617005f987d | -15.5631 | -52.44405 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
