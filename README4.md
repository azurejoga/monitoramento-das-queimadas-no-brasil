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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8d37706-9b9d-37a1-be59-efc850456423 | -3.02759 | -44.26598 | 2025-11-25 03:49:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adfe60ae-c195-349d-9f60-ee7363b93522 | -4.46838 | -40.76074 | 2025-11-25 03:49:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d5b5cec-6d46-31e8-bd05-d83414c3ebf9 | -4.17813 | -43.82949 | 2025-11-25 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6d0f7e8-3fd9-39d7-b7f2-0134155be42c | -4.17103 | -41.62732 | 2025-11-25 03:49:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ad973df-d57a-3044-ab01-b0364cae41a9 | -8.58132 | -44.108 | 2025-11-25 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa5ba217-a20d-337d-a51c-0d12211db319 | -4.17853 | -43.8261 | 2025-11-25 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5e01398-ead5-3176-8949-2ecc16b4734c | -3.59544 | -40.98352 | 2025-11-25 03:49:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 915a8ff3-904d-3187-b7f1-7aa1ebd9a4de | -3.98126 | -46.02701 | 2025-11-25 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23931766-7d29-368e-a914-066c2176a29c | -7.86601 | -46.75129 | 2025-11-25 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61b012f2-9ea2-3166-99a7-454f2084a52a | -3.42052 | -45.45252 | 2025-11-25 03:49:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b5b3c6a-7567-3a35-ad2b-e7a21a384c52 | -3.41994 | -45.45597 | 2025-11-25 03:49:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1c716154-e699-3c17-861a-384cea72a5c7 | -4.39397 | -40.67942 | 2025-11-25 03:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8873534f-ec9d-3711-b24c-92759b06ff26 | -5.63675 | -35.48166 | 2025-11-25 03:49:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f6e65fbf-2aa1-31f7-8a2f-29af9f0e5597 | -2.84474 | -46.77971 | 2025-11-25 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 331281a3-798a-3738-ac77-1f016fd038a0 | -3.83284 | -43.99053 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d2fd870-b350-3c61-8722-d470325b8df2 | -3.09838 | -44.49679 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48139ce6-c315-3e3c-825e-804ab0607937 | -4.18267 | -43.107 | 2025-11-25 03:49:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31ee46d5-83f4-39af-89dc-6311b545beb9 | -3.77899 | -44.04337 | 2025-11-25 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80412193-70de-3748-b0ba-028e354d9895 | -5.09698 | -37.88182 | 2025-11-25 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8444eb32-7f66-3e6a-83a6-71e373503997 | -1.48621 | -47.81226 | 2025-11-25 03:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48ea5588-7e4c-3a62-ab83-f33ea2499e56 | -4.17043 | -41.63102 | 2025-11-25 03:49:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4c0c98cd-0255-3a08-8d46-06316292ef12 | -4.18292 | -43.83033 | 2025-11-25 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43b90e2f-6812-39d8-9253-d9150f60817a | -3.10147 | -44.49541 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1decaae0-b6f2-3126-9d94-3f3e56b3d4ef | -3.98187 | -46.02338 | 2025-11-25 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3bc7e8b-cde2-3394-9c60-237a18a1ba3f | -9.90285 | -36.47374 | 2025-11-25 03:49:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 272d5e78-0c9c-3223-b43f-b58dfc2250b0 | -4.18243 | -43.83215 | 2025-11-25 03:49:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53c6450c-3e21-3785-9ba4-105d64f908e4 | -3.82443 | -40.68829 | 2025-11-25 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 24e2f008-3f34-322a-ace2-3e4491fa29cd | -3.09278 | -44.49897 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4fb03d8-cefb-370d-b932-145e67b03e3c | -4.04394 | -42.51485 | 2025-11-25 03:49:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d65658f8-aa26-3a5c-aa7b-7cb3b2fc7720 | -10.11036 | -36.35958 | 2025-11-25 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7622cfdc-c80c-367d-86ad-1bfe27b939d7 | -3.82308 | -43.9889 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8943b4d3-c0cc-3286-83be-0a9c41d5be3d | -12.19135 | -47.96909 | 2025-11-25 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c78f82c-fa98-3f38-90e1-d46de6d7e9b7 | -3.59198 | -40.97962 | 2025-11-25 03:49:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4987fa7-0733-3b6c-b4f4-d4edcab7dcaf | -3.52495 | -42.56473 | 2025-11-25 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05857b96-436a-38b2-9f59-4d03e9bc6a91 | -9.70913 | -43.93118 | 2025-11-25 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ce75245-6732-31e6-8dcc-5726141c7d08 | -3.83197 | -43.99591 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c459294d-1bde-3137-8f65-3f9f486f0d1c | -3.56582 | -41.60765 | 2025-11-25 03:49:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a6f1368-6ff1-3170-aba8-106071bd5db4 | -3.10096 | -44.49843 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78798306-2a85-314a-bfee-edd8dc3228f5 | -4.8013 | -38.6964 | 2025-11-25 03:49:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c31c8e98-c34a-3b8d-95be-e062826d35fa | -8.58019 | -44.10969 | 2025-11-25 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6bd5bb2-320c-3099-a0aa-26f93c556b03 | -3.09327 | -44.49595 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0004cf0e-246a-372f-ac0c-fe26da1c1646 | -3.99252 | -43.43355 | 2025-11-25 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 038406b0-9c5d-33e9-ad24-43cce41ceacf | -3.82365 | -40.69316 | 2025-11-25 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e2db5cc-be6f-3570-956b-a41b2bc1f95d | -12.12779 | -40.46229 | 2025-11-25 03:49:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a44dd3d8-b9e4-3cca-9dad-b76643263534 | -11.41973 | -40.77318 | 2025-11-25 03:49:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3fd1db86-818a-3f92-b32a-9206929f8409 | -5.05579 | -37.92332 | 2025-11-25 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f39f696-cb94-3e80-9c5d-e198e57e1bcd | -4.61063 | -38.68313 | 2025-11-25 03:49:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f67170e-5336-3224-bf51-bdf91993c34c | -1.48644 | -47.81104 | 2025-11-25 03:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e3b321-6a4e-3514-adff-54fff748f041 | -4.04833 | -42.51556 | 2025-11-25 03:49:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 615df957-472e-327c-a5f7-094203b40bef | -11.76665 | -40.41033 | 2025-11-25 03:49:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd28a4a4-1856-39bd-b1cf-5583120c8c40 | -5.63341 | -35.48113 | 2025-11-25 03:49:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6d1f8757-0a41-32bc-857b-24d317862e76 | -10.48343 | -36.80802 | 2025-11-25 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 3f81c16a-89bb-32ff-94df-32c52e3f998d | -4.04464 | -42.51056 | 2025-11-25 03:49:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a3c3476-a70d-3f39-b829-023ec20f5986 | -3.56752 | -41.60757 | 2025-11-25 03:49:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 434d632b-f1c9-3812-b2df-c36c30524af5 | -3.82053 | -43.99056 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a05f4767-e9ca-3f1d-b012-cada340d6d93 | -1.49272 | -47.81326 | 2025-11-25 03:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15585f25-7311-33e6-bcc8-ba6170fe0aff | -9.15212 | -40.08223 | 2025-11-25 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08646b2e-af86-3f16-9a51-7231c752c9e0 | -3.8303 | -43.99212 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfd0bd73-0c34-39a4-baa6-be9625a42dda | -10.11372 | -36.3601 | 2025-11-25 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 6f4d4f39-9f7f-3660-8790-77df279d7020 | -3.77315 | -44.04818 | 2025-11-25 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8cccb7d7-65b0-348f-aca2-67431aec9e5d | -3.77807 | -44.04893 | 2025-11-25 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72f2c02a-329d-364b-b2b0-7b5d53dca732 | -12.19202 | -47.96707 | 2025-11-25 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1e2a4ce-1ab2-3122-a5eb-98607c8ea71a | -10.48288 | -36.81155 | 2025-11-25 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9641c209-57d6-3c22-804f-d1677af23ae3 | -4.84833 | -37.7507 | 2025-11-25 03:49:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f109ab5-b252-3ef3-b69d-49ea0a19521f | -3.77407 | -44.04266 | 2025-11-25 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d933c12c-482d-3eed-815d-f3025f36307e | -1.49294 | -47.81204 | 2025-11-25 03:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4263cd5-13eb-315d-9a64-652261319463 | -4.18725 | -43.10764 | 2025-11-25 03:49:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72278137-b0b9-3f02-b2dc-74ebdd8b852b | -4.16751 | -41.62294 | 2025-11-25 03:49:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96690b06-d948-3740-85a2-70c376f4c8c7 | -3.09584 | -44.49761 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45ca61e6-4a1f-39e5-a3a0-0b83188a8795 | -3.12724 | -44.37365 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f62e607b-b8d9-3988-87c7-92b293f2ffe9 | -11.31962 | -40.56593 | 2025-11-25 03:49:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 27faaa97-95ce-3188-9e11-c96f4c2bbf03 | -3.52575 | -42.56657 | 2025-11-25 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7e23eb4-ecc8-3b61-a252-670911ade966 | -4.17164 | -41.6236 | 2025-11-25 03:49:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50757c3a-e97b-3df7-9b99-cafacf1e3523 | -3.02708 | -44.26566 | 2025-11-25 03:49:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f85e4c7-ca8a-3ee3-87fb-c94bddd7b600 | -10.11317 | -36.36368 | 2025-11-25 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| faa14a7f-25d0-37d4-9457-06c3c8287010 | -4.05204 | -42.52053 | 2025-11-25 03:49:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 389395ae-f2a5-3893-932f-910bef02ca7d | -4.1669 | -41.62665 | 2025-11-25 03:49:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18d40b71-7df4-38ad-85d6-856bfdc540ac | -9.95092 | -36.57973 | 2025-11-25 03:49:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 725be3b4-f525-34c5-ba50-926b72a140f4 | -3.82541 | -43.99134 | 2025-11-25 03:49:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5372ab0-ef83-3baa-ab5d-85c89b290e00 | -2.84548 | -46.77532 | 2025-11-25 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a60b676d-a7ea-311e-beab-f85dfbd5446e | -5.1931 | -35.75682 | 2025-11-25 03:49:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1700813e-0250-38bc-831e-6508351a664d | -3.65787 | -42.7767 | 2025-11-25 03:49:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e6deb23-6049-3eb7-9de9-bb798dda712e | -3.12773 | -44.3707 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9842570-70be-3a1d-8b0e-81277e319573 | -11.88399 | -40.94946 | 2025-11-25 03:49:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| db0b32f2-b747-3a91-8674-d4d1117ddcee | -5.05522 | -37.92693 | 2025-11-25 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b379cf62-ac06-306a-8276-d27396d5e46c | -9.89951 | -36.4732 | 2025-11-25 03:49:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 901f29fe-855e-3d38-8acf-e390527a158f | -10.48621 | -36.81207 | 2025-11-25 03:49:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 636a5a77-ec55-3fe6-843d-c3b003ab0337 | -3.82458 | -40.69051 | 2025-11-25 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b4767634-b700-3fab-b397-13d2000234e1 | -4.61125 | -38.67931 | 2025-11-25 03:49:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8dbb86a-2d96-346c-a2ed-17518f3c25c3 | -12.19129 | -47.9709 | 2025-11-25 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28c566e9-1b02-3e09-919e-bc87bebfee87 | -3.09789 | -44.49981 | 2025-11-25 03:49:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cefd0589-0a8a-3b39-9f37-5c99b92d10a7 | -3.76827 | -44.04724 | 2025-11-25 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e35f5be-c43a-3682-b564-28659f249257 | -9.9023 | -36.47729 | 2025-11-25 03:49:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 753a982c-cf0e-3ecd-9190-47751b412c52 | -4.04764 | -42.51984 | 2025-11-25 03:49:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd2dc56c-7127-3315-a71b-8a5b56a1f386 | -8.58214 | -44.10341 | 2025-11-25 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef8c7570-ebb5-3862-a4d6-0260a7823dca | -2.95892 | -41.55534 | 2025-11-25 03:49:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c91abed4-5761-32b7-8d67-c5948e3bb859 | -8.58098 | -44.10509 | 2025-11-25 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 40984ef0-8e1a-32ea-9122-8aca423cc141 | -12.19059 | -47.97289 | 2025-11-25 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa0d4162-4cac-337f-9d1e-fc009126fd61 | -3.81543 | -43.35706 | 2025-11-25 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a8490f7-a731-38c6-9d01-376143479662 | -16.76223 | -51.35376 | 2025-11-25 03:51:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README5.md)
