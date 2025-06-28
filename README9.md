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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68e43ad1-d66c-3a8b-8116-566dd76a2a70 | -11.2664 | -52.7527 | 2025-06-28 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| a9c89688-ec76-3e55-8d07-7044da71d09a | -11.0455 | -55.3773 | 2025-06-28 03:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 7d7fdcb5-d589-3763-8124-8b7e848d9292 | -11.2853 | -52.7508 | 2025-06-28 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 756bfaf8-f808-31dc-9602-63e91b3c93cf | -16.2761 | -49.9608 | 2025-06-28 03:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 68f25ad5-a9d1-36ef-a5f5-1881769d5a46 | -9.1208 | -49.4743 | 2025-06-28 03:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9ce59919-94e7-341f-ae53-e9c792c0bfbb | -9.7041 | -56.1843 | 2025-06-28 03:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 83c53d61-0bec-37ea-b37d-b1417fc83e30 | -9.7041 | -56.1843 | 2025-06-28 04:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2c389774-dc40-3624-8152-24e0c02ca50c | -11.2853 | -52.7508 | 2025-06-28 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 333a03f5-de3d-3f6e-a69a-aac3a501ffed | -11.0644 | -55.3757 | 2025-06-28 04:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7bb54082-5df8-3da8-a3db-f50c07576d5c | -11.2664 | -52.7527 | 2025-06-28 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 8104ef29-f0cf-3e09-8d4e-d9a25406cfa1 | -11.0455 | -55.3773 | 2025-06-28 04:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| c38d2423-91c5-35a7-98d3-083d26dbfdbe | -4.5429 | -48.0151 | 2025-06-28 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a13af4e3-d871-32c2-8ef8-95bb12f4a8ec | -9.1208 | -49.4743 | 2025-06-28 04:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 5d89457f-421b-3cee-b61b-157d94988787 | -6.9108 | -43.9834 | 2025-06-28 04:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d0355209-f749-3456-9b2e-65c1be1f04e5 | -4.38675 | -37.98006 | 2025-06-28 04:00:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e30ca286-051b-3cf1-b037-e5142edf0fda | -4.12614 | -43.06928 | 2025-06-28 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8014e70-7fd8-3fa9-a1dd-401100daebc9 | -4.51668 | -42.07735 | 2025-06-28 04:00:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7cd2ca95-5482-3c06-b19e-d570063edfa2 | -4.90973 | -37.40855 | 2025-06-28 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77628b4c-a7be-377a-8268-a9865d28aa63 | -4.24863 | -38.12452 | 2025-06-28 04:00:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 816085e4-7350-360e-8a7e-e673e22a8841 | -3.38275 | -43.12389 | 2025-06-28 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb3b1dec-aa08-3ac0-bd38-49731157e554 | -3.46894 | -42.86296 | 2025-06-28 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a64d22e1-d02f-3a41-b0e8-f5fb9e48bf86 | -4.8221 | -43.21997 | 2025-06-28 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28ebfa00-9c10-317d-8cc2-0e5d2f315f67 | -4.18461 | -48.14112 | 2025-06-28 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71be339d-ac5f-332b-ac65-ca7ebf429847 | -2.44173 | -47.48424 | 2025-06-28 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a338ea-28f5-388a-90f8-be79a95721b6 | -4.12981 | -43.06985 | 2025-06-28 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce6c0bdc-7db2-3541-8971-4312822e4ff0 | -5.04825 | -38.53905 | 2025-06-28 04:00:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6fcf5748-4679-3dda-8781-ace380dcacae | -5.24832 | -35.68712 | 2025-06-28 04:00:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d1fb146a-644f-3c82-a070-ad411250a8c8 | -3.42386 | -43.16494 | 2025-06-28 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70a1f2c-31a6-3568-8123-64502657bd6a | -5.24168 | -37.32343 | 2025-06-28 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27425662-d9c6-38a7-b57a-8df1029252be | -4.81985 | -43.2107 | 2025-06-28 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a690073c-1a73-364a-99b1-bdb92ce4071c | -4.89213 | -37.61504 | 2025-06-28 04:00:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f3935b4-74dc-3f1b-aa0f-a4155f3a8dfc | -10.81964 | -53.74628 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43a5bb0c-20a9-361d-ac46-c91d755795e3 | -11.57252 | -47.62436 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cab95223-c143-3911-842f-979b965cff11 | -10.95489 | -48.15463 | 2025-06-28 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 72019473-6911-3e72-84ac-edd3eded305d | -7.18744 | -45.32836 | 2025-06-28 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d0bdaad-5f48-3741-a35c-2da40b26ee45 | -6.90539 | -43.97703 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34cdfa9d-ec11-3e5e-9865-6bf3a3f93a5b | -7.20679 | -43.08973 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c91c9a7b-bccc-3291-afa3-97dca16445d2 | -8.57006 | -51.57244 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 866dd474-116a-34ba-940a-20537e062c76 | -7.21651 | -43.07396 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d4eb1bd1-4b44-36e7-8825-8e3566aea223 | -8.0425 | -47.64359 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab2336f2-3d10-3aec-8838-c88798b95f89 | -7.54613 | -45.8249 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 67f8dcc0-b760-31b8-86be-4ce742ab00e5 | -9.09018 | -47.96773 | 2025-06-28 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bad5646f-88a7-34bb-895d-89a2033ae34b | -7.22161 | -43.0871 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b0f9f7a2-fc51-3dcf-9afc-8078ea8b3bd1 | -9.37042 | -47.6323 | 2025-06-28 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57a0f773-af6e-3619-a44b-42dd3c67cd80 | -6.94675 | -42.88075 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| cd34ff7a-df0b-302b-b98f-b295163bbed1 | -6.90613 | -43.97258 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d335d722-528a-3aaa-9b1b-927f70799eb3 | -9.11061 | -49.47965 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ab922a12-4bd3-390f-acf9-3278af4fafc0 | -7.55027 | -45.82557 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 09215519-2327-3fb4-91d9-21d5b612462e | -9.51619 | -43.24504 | 2025-06-28 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 35ee09ac-cfd6-3743-a98c-24578f038e28 | -5.45684 | -43.07489 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11fc9b4d-ec4b-3bf8-b1a4-91a27e88a375 | -8.56571 | -51.57935 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0643aeac-8d80-3147-8c6d-4b841a880e57 | -10.27547 | -44.64296 | 2025-06-28 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4bfe4724-1190-3852-ab60-5384b111ed95 | -9.69354 | -48.32952 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e18e355-4ed4-30f8-82f4-1da443c58778 | -10.52819 | -53.62303 | 2025-06-28 04:02:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c22f14f9-e070-339c-980a-2153cb67dddf | -8.13213 | -49.59357 | 2025-06-28 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6917135-3a33-34a0-a1e2-a8e4439eea54 | -9.69638 | -48.33399 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23ac4021-b9cb-3dda-b3e5-f350e59be0b4 | -6.90545 | -43.99996 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 987c40a1-4494-3019-943a-0224c07e59bb | -11.67255 | -46.72448 | 2025-06-28 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74ace39a-bde4-3ec4-b515-2624b29a5f94 | -10.53242 | -42.52875 | 2025-06-28 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e260b43-6147-3748-a598-4172acd814bf | -5.46769 | -43.07656 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 019bdca3-cacf-322f-99f1-aeb977d3d397 | -6.94963 | -42.88525 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 6df5c5b3-78b6-3eba-8695-35ad2adc03ad | -6.7345 | -47.37528 | 2025-06-28 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cfaa8cc-55e7-3fad-8342-4873a25b1260 | -9.11579 | -49.48048 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 04474fdc-56c6-37ce-bbdc-3f1cf29bae56 | -11.84374 | -43.79885 | 2025-06-28 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 141cd59f-63c1-3d6a-9e58-6bc3b99b7323 | -11.55138 | -48.77898 | 2025-06-28 04:02:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefdfcb3-649f-36a8-b6c1-be4758397d9b | -6.90167 | -43.97641 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9410845f-d6e0-385b-a431-d96397544575 | -6.23469 | -44.52643 | 2025-06-28 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fffbb17a-3e4d-3013-8b8c-d42097f08021 | -6.91583 | -43.98332 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a1a1e5d-f520-308e-8d76-00f53df2a4ab | -6.91064 | -43.99163 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c6e614b-6623-36e9-b40c-b1c22e6de947 | -8.31028 | -46.31305 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8ad5474-190b-3312-ad9c-70eaa6f79648 | -6.23079 | -44.52584 | 2025-06-28 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a77b7995-ca6d-368a-9e8d-54cf75efe107 | -7.54964 | -45.82922 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 00e4bee7-b7d6-3602-ae12-15812722f78e | -6.95342 | -42.90628 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 522d8f98-5518-327a-b33f-fabfd1821ee9 | -6.9461 | -42.8847 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 52eeafd8-4292-3ecd-8002-c33485d5e08b | -9.1204 | -49.48441 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c2004a1-c6af-3c3d-b46d-f3d842cb7ca3 | -10.83153 | -53.75481 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 05b9b14d-89aa-3a57-bd2e-866325fb8b1c | -11.56815 | -47.62361 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 534590ff-97d3-3485-b2a0-08cbd418b2a2 | -10.83694 | -53.76182 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3bc0531a-5b4f-38b2-a166-4d6db48f598e | -9.44049 | -47.96214 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd4dd1dd-6c51-387b-a0bb-cd3c6b5fb69e | -7.10284 | -43.66586 | 2025-06-28 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1a5acff-746e-39fd-b30d-84abdbb572aa | -8.32473 | -46.2268 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cc717b6-6e83-3f28-9821-30be72cb880e | -7.21226 | -43.07827 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8b754b39-18b9-34fc-810d-5c2f3ccfd214 | -9.11466 | -49.48671 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0afc27d9-5704-30c8-8e38-29ecf6c2f750 | -9.87297 | -48.45191 | 2025-06-28 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 983a292f-1119-3827-b272-3f5ae4b89103 | -9.43585 | -47.96137 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de1a7f09-53e3-3fd7-85e1-d32c8cc6944f | -9.74079 | -48.33778 | 2025-06-28 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 575a42c4-9210-3d2e-99bf-a7e22e5c2320 | -9.97015 | -48.24343 | 2025-06-28 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dadc8e95-5f0e-38e3-9ef2-91fd498c12e9 | -10.82074 | -53.74076 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85168423-a9a3-37e5-97ff-f6e8977a3cef | -8.04166 | -47.64846 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5681638c-2063-350f-bcbf-b0f89396be8a | -8.0463 | -47.64927 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f0a1903-72dd-3270-9730-24298011eb63 | -8.56738 | -51.57063 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b7064e8-2283-3177-9368-a945aadda9e2 | -4.54754 | -48.02563 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3b36bc3f-f65b-3653-8f04-814b9a981004 | -8.07456 | -34.97579 | 2025-06-28 04:02:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53e7c19d-79ac-3dba-9233-662fd3442540 | -7.2129 | -43.07426 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 3cd41938-ac5b-39b6-82c2-76fa50ad3569 | -8.90982 | -49.83797 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5bd2421-e7aa-35c2-9003-1d8f2aa36d5c | -6.90618 | -43.99549 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d76f1ef-3f69-34a9-a215-5d67fc792ee7 | -10.0317 | -54.32611 | 2025-06-28 04:02:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a97a8e52-8704-3cbf-b1f9-a714ffcb38da | -6.90765 | -43.98656 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 594ca7d2-9db6-317b-97d9-6ae720d18635 | -8.3116 | -46.30577 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d8b7f9b-7185-319d-9e07-07427af9d78e | -6.90692 | -43.99102 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README10.md)
