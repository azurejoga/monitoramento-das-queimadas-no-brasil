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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27f15534-5b84-36c5-8f16-56c817ae2974 | -6.9421 | -42.888802 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee78823b-3376-3699-9544-817ba536ca03 | -6.2271 | -44.5173 | 2025-06-28 00:10:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c48cb80-91f9-348e-bf97-7d0ae5698c80 | -4.5352 | -48.028801 | 2025-06-28 00:10:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed5dfe47-d6d3-3394-bd29-db122756754d | -7.2115 | -43.0797 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb6c6462-cf83-3b4c-a9ad-d8821256788f | -11.254 | -52.7365 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dfa68a0-b523-3005-8a1c-bcf5390875f5 | -11.2636 | -52.734798 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f93b21c-cdf9-3252-9561-f8d229fd3328 | -4.5395 | -48.002102 | 2025-06-28 00:10:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f67dc1-5841-3c69-bd18-ebd65fe4345a | -7.2213 | -43.077499 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 159e5a8e-fbe2-3a91-b221-8ec026ebe7bf | -8.5481 | -51.557701 | 2025-06-28 00:10:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fa38a35-34f0-35e5-acb0-d0b725d301e2 | -9.101 | -49.471199 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f18aba38-4a56-3a7e-8e97-de6f4c0a0b46 | -11.2477 | -52.7034 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1802359-04c8-35c8-ad0c-65491393f925 | -4.5324 | -48.016499 | 2025-06-28 00:10:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca9649a-642a-3259-a09b-02c7899b9f50 | -5.6196 | -44.009102 | 2025-06-28 00:10:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73b2af7a-8eb0-389b-a1ee-edeb6507e8e5 | -7.2196 | -43.070202 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 848ff339-e784-39a8-880a-771c1d00ee47 | -9.1069 | -49.450901 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23eee9d9-a4fd-3d8d-8dc5-5c0d84ca6a84 | -6.9082 | -43.976101 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab80d740-1d52-37e4-b556-9e0a98020032 | -12.2482 | -46.7453 | 2025-06-28 00:10:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cbb0fe0-e40b-3d4b-b51f-737035406b1b | -7.1125 | -43.372101 | 2025-06-28 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bcd1a397-8631-342a-af41-4d4f5857f05f | -10.5248 | -42.5313 | 2025-06-28 00:10:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cbfef88a-69bd-375d-88ce-23e60f3e2600 | -7.2621 | -43.857601 | 2025-06-28 00:10:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7521788d-fbeb-35a1-b5c5-5f31f8ab4e6a | -6.9567 | -42.9081 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ef1a477-b1c5-30f2-9a47-690916394311 | -21.328699 | -45.4207 | 2025-06-28 00:10:00 | METOP-C | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16d6a628-3c32-31e3-bbc2-15d4b265597c | -9.1182 | -49.505901 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6118bdb5-95ad-39c0-904b-d40f1231db6b | -6.9404 | -42.881599 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c563f17-7b07-3105-9978-a70d427d11a6 | -6.9519 | -42.8866 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fd5a911-ae2c-3d0c-9bfd-1f5eca2246f7 | -11.2698 | -52.768101 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46ac1071-e0bd-333a-9d00-cb3ffaef7742 | -9.1241 | -49.4856 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e90e1c1-4eb0-3c46-86b8-68dbea60bfc0 | -7.2229 | -43.084702 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76567a9b-5d69-301b-b28c-bb397afb0e11 | -10.5363 | -42.536598 | 2025-06-28 00:10:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e6d1d536-d3cb-37c4-a25e-d65cbafc7091 | -6.9502 | -42.879398 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a603e46-9d16-3202-a479-e42c846d5f2a | -6.9117 | -43.991699 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbe2d8f-f2c2-392e-bc4b-d0a5eb80a9b0 | -9.1204 | -49.4673 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97641655-3c4d-3e3c-9185-966483fa92bb | -7.2082 | -43.065102 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef48457c-67e6-3bad-b2d9-a8f9a1dbe13d | -7.2702 | -43.847599 | 2025-06-28 00:10:00 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17d47213-6dbf-37a8-8b56-711e4002ead5 | -12.2536 | -46.771999 | 2025-06-28 00:10:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7578d637-3d45-343b-ad80-361257608b75 | -10.5232 | -42.5238 | 2025-06-28 00:10:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9eb8d7c6-ab92-3bb4-abe1-0cf9eca0b348 | -6.9099 | -43.983898 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5157d049-3e07-3d3a-9c48-03d4bca55262 | -10.533 | -42.521599 | 2025-06-28 00:10:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 01948fa2-767a-347f-9477-7c77738616cb | -5.8606 | -46.473701 | 2025-06-28 00:10:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65717e91-9146-3b8f-8506-d464c4193815 | -8.5578 | -51.555698 | 2025-06-28 00:10:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd1fbf7b-70a9-3d0a-8ea3-7b32c77b293d | -4.545 | -48.026699 | 2025-06-28 00:10:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474bc724-8436-3dd0-bc05-c19c7a544d35 | -11.2732 | -52.733002 | 2025-06-28 00:10:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0197f495-27fd-3d37-a400-a402e83640fd | -12.2607 | -46.756699 | 2025-06-28 00:10:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14621e22-a328-397c-b2d0-c256ff982dc9 | -6.9486 | -42.872299 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dbb82bb0-5ab3-36e1-84f2-27285554aa6c | -7.1108 | -43.3647 | 2025-06-28 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a479a0f-6017-352b-b793-1e7aed1a7a8a | -6.8949 | -43.9627 | 2025-06-28 00:10:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15d20592-538f-3065-87a1-cec741041704 | -7.2098 | -43.072399 | 2025-06-28 00:10:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b9da1c3b-84b6-328e-8bad-d2369a0d32c5 | -9.1047 | -49.489498 | 2025-06-28 00:10:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2a6448-51dc-3f38-aebe-a04722afc942 | -9.3668 | -47.620602 | 2025-06-28 00:10:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c47f3d6-a9d9-3bb0-bed7-d77744bb876f | -10.8385 | -53.7442 | 2025-06-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 53a60e26-fc26-346b-ab75-e21f69054e94 | -12.2527 | -46.754 | 2025-06-28 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3ab0a3de-1d87-3ba8-83ee-f9286555b1d3 | -7.2031 | -43.0701 | 2025-06-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 4454cd84-4afa-336a-9c94-e64da5c25ad6 | -6.911 | -43.9602 | 2025-06-28 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 78077a8c-e68d-39a3-8e9d-b2c8f978785f | -9.1205 | -49.4958 | 2025-06-28 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 290.9 |
| 14ecddd1-a472-3210-a331-011eb2966326 | -7.2217 | -43.0917 | 2025-06-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.7 |
| 3ad90269-2ef4-3a70-a8ae-859be6c2f95d | -6.8922 | -43.9619 | 2025-06-28 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e8b51c05-9f7f-3bb4-beda-c94b78bf6ec4 | -7.2028 | -43.0936 | 2025-06-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| d88b4436-3a79-3867-aa9b-b5f9ee541243 | -6.892 | -43.9851 | 2025-06-28 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2a1053ee-5e65-3619-b8c9-fb11e8f88640 | -4.5429 | -48.0151 | 2025-06-28 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1d24ec4e-d081-3122-9164-a60d822abaee | -9.1017 | -49.4976 | 2025-06-28 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 21e3ede0-3007-3129-bba4-a3005222e57f | -11.2853 | -52.7508 | 2025-06-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 3babf963-5c77-3352-bf2c-d80f721683ea | -11.2856 | -52.7299 | 2025-06-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 834a1c28-bf87-3ccd-9827-75239d0e065d | -7.2219 | -43.0682 | 2025-06-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 298.3 |
| 3f846a72-df3d-3f72-bdba-021ad13a96a7 | -4.5427 | -48.0367 | 2025-06-28 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 76a1c30a-b539-3fb9-9482-a39ead6d49de | -6.9105 | -44.0065 | 2025-06-28 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 05f994df-defb-31a6-bf50-672094574c06 | -11.5779 | -52.115 | 2025-06-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 938735cf-bb71-362f-a866-153ffe4856b2 | -9.1208 | -49.4743 | 2025-06-28 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| a0471943-4710-39ee-be7c-aff337634336 | -6.9108 | -43.9834 | 2025-06-28 00:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 266.3 |
| eb753fad-b226-37e3-8f56-587fa9e4074f | -10.8382 | -53.7648 | 2025-06-28 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e71de5da-8adb-38b3-8524-cd0af7f89e08 | -11.2666 | -52.7318 | 2025-06-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| cecec1fa-e09b-34a0-a92d-18b8355322dd | -12.2523 | -46.7766 | 2025-06-28 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ef31de41-a082-359c-8c54-3ff9f72dba94 | -11.2664 | -52.7527 | 2025-06-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 156.2 |
| c2c1aabb-c37c-3535-9966-43f2f851c85a | -7.2219 | -43.0682 | 2025-06-28 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 234.3 |
| f9fb2d4f-0190-3ba0-8ebb-cd3066e38ac7 | -11.0266 | -55.3789 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| c1470c70-57de-30aa-9fdc-39402a8efb77 | -6.892 | -43.9851 | 2025-06-28 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 951846ad-f2f3-30f8-af21-fb6654f7889c | -9.1208 | -49.4743 | 2025-06-28 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 7d6e423f-29ea-34a3-ba95-8f67916c07a6 | -9.102 | -49.4761 | 2025-06-28 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 90183063-acaa-3c4a-aece-c48290b40ec0 | -11.2666 | -52.7318 | 2025-06-28 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| c0ef22ce-9d9c-331f-bf27-1fcab4ec5692 | -7.2031 | -43.0701 | 2025-06-28 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| b43eb1ea-d68b-3679-bf1a-c320c672cd1c | -6.9108 | -43.9834 | 2025-06-28 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 305.5 |
| a499b604-c25a-3ad0-92d3-16f6a06b9a26 | -11.0453 | -55.3976 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 650f6bfe-fa03-3a80-8646-7079cc512eab | -9.1017 | -49.4976 | 2025-06-28 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a1da1055-9fe2-36f9-966a-76e8073f19dd | -7.2217 | -43.0917 | 2025-06-28 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 233.0 |
| 9ee96571-5eec-3c96-85e9-778454691d90 | -11.0644 | -55.3757 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 203.8 |
| 85e0531f-44e3-39f2-a72c-187d9886ee7d | -4.5429 | -48.0151 | 2025-06-28 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6aa28f76-d714-3264-b2e3-b14610d5d944 | -12.2523 | -46.7766 | 2025-06-28 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4816ac3a-fc0f-3d85-a3fd-54086ab9a1ee | -9.7041 | -56.1843 | 2025-06-28 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| f8943a74-3367-3db8-8a01-14cf55cf058d | -12.2527 | -46.754 | 2025-06-28 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c4ab9ffa-a48d-3dc4-95f4-2997923622a4 | -9.7039 | -56.2043 | 2025-06-28 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4211a4f7-c055-3f7f-9d41-8aa8b82796a3 | -11.0457 | -55.3571 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 60aaa8f5-7d62-3a46-b240-b7810c283486 | -11.2853 | -52.7508 | 2025-06-28 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 195.0 |
| 8e740c77-1aba-35ae-bf32-4735f6e03496 | -9.7228 | -56.183 | 2025-06-28 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a11ff5e1-ded7-3b6b-9a69-0f1ca5422d1b | -11.0646 | -55.3555 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| cbaf3f3e-3d95-3257-b362-3287c97a2529 | -11.2856 | -52.7299 | 2025-06-28 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6f26c40f-8711-3a02-8816-c0925e787e3b | -6.911 | -43.9602 | 2025-06-28 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| da574e08-af73-37b6-a461-c0337776ecbb | -11.0455 | -55.3773 | 2025-06-28 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 436.7 |
| e4f488e8-2817-3c18-9e63-21a01c4d06bc | -10.8382 | -53.7648 | 2025-06-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 726be4e3-ec2d-3111-90a9-aba6d8aab699 | -10.8385 | -53.7442 | 2025-06-28 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 0f3adf51-e5e3-320b-a459-e0d813a59818 | -6.8922 | -43.9619 | 2025-06-28 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ddebfd8a-ff4e-3ce1-bdd7-96a9f27c48d9 | -9.1205 | -49.4958 | 2025-06-28 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 249.6 |


[Clique aqui para ver as próximas entradas](README3.md)
