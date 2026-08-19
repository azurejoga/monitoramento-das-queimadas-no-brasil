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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5990746e-44a8-3f72-ac5a-12db2b8d7441 | -15.64031 | -55.99513 | 2026-08-19 04:40:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbe454c7-78f7-334b-9fe9-bb9e4511c8c2 | -8.57729 | -54.72091 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eee0d903-9dc5-30a8-926d-6fd35bc7ba15 | -12.46683 | -54.19182 | 2026-08-19 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e7d6e09d-18b8-37ba-a61d-f33ffc486b7f | -8.54404 | -54.72508 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f80004f-d779-3f40-af3a-189008de6add | -9.46658 | -51.6035 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dab7e576-16ba-3186-99f8-c0adf1369d63 | -15.27785 | -56.50537 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d7a0cd6-4caa-3704-9ef7-6ae13c3c4bbe | -8.52531 | -54.75635 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f786118c-5127-3537-a956-59f9740bdb9d | -9.72944 | -46.78361 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5b37f68-1420-3897-9f2c-fd2eae11f1e4 | -8.52894 | -54.76127 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f66053b6-f795-3568-847c-a8f5024f3e7f | -8.54395 | -54.758 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a603d7fd-d05c-30c3-8be7-903ea6b47997 | -8.54678 | -54.76727 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0abb3c57-ef34-3876-8a61-cfe746250666 | -11.69401 | -54.5613 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8736c978-0d61-3bb3-9743-6a2c9903b1df | -8.57655 | -54.72515 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 424b2449-675a-34a1-91b4-86357ca3434a | -8.56641 | -54.75744 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee5c0d57-a91d-384c-848d-dab674c38ee4 | -8.56865 | -54.71934 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e902ce8-8ed0-39ee-b9da-521eabc7b637 | -8.53466 | -54.72774 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abba86b3-e692-34b7-a583-f8f5fe475c12 | -8.18836 | -55.00439 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c6c033d-b718-39f8-9551-ec51502d352c | -8.55347 | -54.72948 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29eceea2-7ad1-38e4-aaa9-a129856a9701 | -15.31964 | -56.45081 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b5929ce-2039-3342-8154-5e7eef2de4f4 | -9.7306 | -46.77607 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7fdba94-03ef-3298-9ff3-21b0c6a79c05 | -13.41064 | -43.86581 | 2026-08-19 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c36c754-4b75-3525-bf86-8f236bccd039 | -9.39377 | -48.24109 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6376f4f8-a5ba-372b-ab73-38e244154cac | -9.92991 | -53.63766 | 2026-08-19 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c0d03c5-fba2-3197-a6a1-dcf01dbe2a61 | -9.3949 | -60.57079 | 2026-08-19 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ae608b0-d747-3ed1-8284-587c841e44cb | -10.1276 | -52.11663 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41338f03-fef2-3cb1-ab06-bcd3e3fb2ba3 | -11.33247 | -51.11777 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d1f28c-1de8-30b8-9b2d-a0ea2c2c389e | -9.7612 | -46.80355 | 2026-08-19 04:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1121b74c-e14e-323f-a7e8-7909fcefab83 | -8.55089 | -55.31953 | 2026-08-19 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ce52010-d792-3e7a-a1c1-943337654492 | -12.00013 | -55.52769 | 2026-08-19 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2475414b-772d-3a01-b8cd-5438da50bb93 | -9.01148 | -60.51485 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07254932-c8d6-37a0-9348-5e050ad939ff | -9.16556 | -59.70348 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 632370d3-2bd2-335e-b7e6-15c2e262e6e9 | -8.63776 | -54.68028 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9069c728-912e-3326-b995-85cb66388412 | -7.60168 | -60.95133 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 582df3a6-3a4d-37aa-92a5-00d6f84f6be7 | -8.57297 | -54.72012 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d046a6f8-1ac7-360d-8d19-3a15ca0b1218 | -7.60056 | -60.95709 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94dea6f8-3e3e-310b-b2f0-5db70f9015f7 | -8.55775 | -54.75585 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eb8087b-df83-38ed-bce1-c7445d312fe8 | -9.45607 | -51.62292 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce31381-c83b-3dee-8ae4-db332f8b46fb | -8.54245 | -54.76644 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db4e8fcf-d082-352f-80a1-c7ae8c3d4583 | -8.53453 | -54.76062 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b599c0bd-6d21-3809-bf4b-f40fb25557ff | -11.641 | -54.52892 | 2026-08-19 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c93d084-3075-3b27-9929-5eb61d202f01 | -15.27704 | -56.50964 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9759c97a-6bb2-3f56-9eea-69a55dd7b833 | -15.31449 | -56.45436 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91a7714b-1c75-36c4-9094-c336da9c0700 | -8.55982 | -54.76951 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| db649045-8864-3f8a-8f31-6d77ad90d2e1 | -11.71494 | -54.63 | 2026-08-19 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8bb87d-2f9b-3d55-b862-338d72834c28 | -8.57518 | -54.68224 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99a66ae7-ff87-3193-b714-4425f7074655 | -12.37931 | -46.45095 | 2026-08-19 04:40:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b51d5c9-874a-3f11-95a6-57e92a52f292 | -8.54476 | -54.72088 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 034c3801-93a4-35f5-846e-7501fced0c0a | -9.38991 | -48.24405 | 2026-08-19 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c57ea7f-e6b9-3ea3-baf8-95f74f25bef3 | -8.56132 | -54.76096 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e82d4cd1-0a95-3eb8-a17f-ae99742c347e | -8.56287 | -54.72682 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b72cb09-e10c-369a-9fad-50fbadca5a10 | -7.42963 | -59.78603 | 2026-08-19 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4fbd974-c7e2-36f6-a241-b286f3fd6175 | -12.51665 | -47.85665 | 2026-08-19 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c984f9c-fd88-3f16-9d9f-b38013022306 | -8.58231 | -54.74323 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6f8f61c-106c-3b0f-8599-3806650935e3 | -8.56065 | -54.73941 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0df55ebb-7ef7-3ce9-a295-a775db647559 | -10.88093 | -57.12321 | 2026-08-19 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12c7120e-8393-366f-b102-9e608f4563f2 | -8.53692 | -54.76701 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74f745c9-3e4d-3b64-be7d-4b765eaba164 | -8.58666 | -54.71836 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 469b6cd0-bd93-3d6d-b5a5-0c350071a5ed | -11.12642 | -47.2844 | 2026-08-19 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4108c56-fc6e-3046-802b-13134ca2c846 | -8.5318 | -54.74454 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c89cb58-3965-3525-83f0-224bb756fda2 | -15.31799 | -56.45957 | 2026-08-19 04:40:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dfc6ca9-5a69-310e-bf39-ecbfb8b90059 | -8.55272 | -54.73371 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fc4c477-fe06-3281-96b1-f3b6a432a68c | -15.78447 | -55.55353 | 2026-08-19 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa8b4f68-e8d2-3ad3-bb59-5af57b00d3d1 | -11.99584 | -55.52681 | 2026-08-19 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3484e33a-e33b-3070-b1f9-5053dbe366c5 | -9.46723 | -51.59959 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba394ffd-1c7c-33d0-afba-099e38649672 | -8.56775 | -54.77533 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6244980c-a0df-3d2a-98c7-5392a050e62c | -9.93266 | -53.63956 | 2026-08-19 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef6adfc-afac-3b3c-8128-4ffb9e13910d | -13.46786 | -51.7892 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a0d3129-8643-3402-888b-33f0468633fb | -10.24647 | -46.99477 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e4fa8c7-c3b2-3088-880a-c5b5733987c9 | -9.05813 | -50.84513 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f95fd560-c743-3def-afd9-f4cdd482034b | -8.22058 | -55.02957 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4072a46e-706f-3a13-bcfd-57be95e5c856 | -11.20012 | -54.01748 | 2026-08-19 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d36c446-6e9d-3de5-b5ec-a61e4d1d162f | -12.83207 | -48.41892 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff12cb5a-cae0-33a7-a13f-e28198dabaf9 | -8.21904 | -55.03846 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc11f430-1b24-3e93-9b85-ca1d517b6cbe | -15.22973 | -57.66539 | 2026-08-19 04:40:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f0cdb27-23e4-3566-b470-b652e0530996 | -12.05174 | -46.46233 | 2026-08-19 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3871e31c-5603-3c0b-b22e-da1ba3c548ab | -10.81104 | -50.29963 | 2026-08-19 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef0a0dc9-aa35-3e21-9f5e-9c81a30f64f0 | -15.44271 | -41.38448 | 2026-08-19 04:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6afffeae-7f62-3fd2-99c3-d6e3e5300dae | -9.01104 | -60.50023 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42d947f0-594d-3c40-a9c6-4cc1f5923ad1 | -12.83095 | -48.42619 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b6e86a6-e688-31b1-9810-9c2bf50c3bf7 | -11.22149 | -55.07384 | 2026-08-19 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce8306e9-7115-3e89-baca-e5b482df7786 | -9.16553 | -59.6717 | 2026-08-19 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 169ca1bf-eab1-3bdf-8113-b0ef6c9d3c11 | -8.57087 | -54.68143 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcbd3cb3-9dde-3a25-8ecb-7a7708e619c8 | -7.60177 | -60.96265 | 2026-08-19 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e8dceb7-5d41-3066-8e63-607b2cfb9680 | -13.7308 | -51.87356 | 2026-08-19 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d21200-b712-3059-b582-55b972b77d52 | -16.71772 | -46.40628 | 2026-08-19 04:40:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64429532-1e12-3d8b-a533-d62365eba724 | -8.55907 | -54.77375 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 436e6697-58e7-3c73-bbf7-6059b7e3bec0 | -8.55051 | -54.7462 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 941c857d-6caa-3bac-ac34-7e8de95254df | -8.58087 | -54.72597 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5a39f13-6107-35c4-8e2a-9f6fe21f6135 | -10.28851 | -48.22826 | 2026-08-19 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af614383-ebf4-3ac9-90db-da51990bbb2e | -10.11217 | -54.2863 | 2026-08-19 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4b6f131-3b34-33a5-8e2c-4b570d5aa61b | -10.68023 | -48.99927 | 2026-08-19 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c62d3396-c37d-3f27-934b-a2d4b8a03932 | -12.84155 | -48.42416 | 2026-08-19 04:40:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 519b1af5-75f4-384f-9607-8692ca9e4e22 | -9.45963 | -51.62347 | 2026-08-19 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4397e920-7302-39ae-aba6-62dcdcbe2db6 | -8.55339 | -54.75518 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf1d9b63-b94d-3d79-98f2-4d5c10283a93 | -10.55797 | -56.33317 | 2026-08-19 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad72ba5a-17f8-3447-9795-1f87d6c9919e | -8.55061 | -54.72042 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51db475f-3dd8-3b81-aefd-7ad64d86a0a2 | -8.57446 | -54.68631 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51962be5-06a1-39c3-80ae-a4da87ac3091 | -12.35547 | -51.21477 | 2026-08-19 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 006f4c64-cc4c-32c4-96a8-f3bb366e303a | -9.06349 | -50.83398 | 2026-08-19 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b289c10-98d7-32b7-b18b-095df05a9153 | -8.58736 | -54.73989 | 2026-08-19 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
