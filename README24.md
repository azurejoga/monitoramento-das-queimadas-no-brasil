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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906f3fd9-c44f-3014-919c-d7c3aa23fce4 | -14.5316 | -47.38705 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dfadf72f-040b-336a-adea-73d275cd5173 | -14.53332 | -47.35452 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 333eebcf-0ac1-387d-8489-dff88c8b11ff | -16.69004 | -49.7718 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16b6e65e-a4e2-3f91-86fd-bb23f7e7a352 | -18.61254 | -48.20433 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a21fba09-6797-33ed-82b0-c23fea269704 | -12.63263 | -48.00595 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec27704-b144-339c-aa9e-df0caffb5c01 | -17.11499 | -43.59313 | 2025-09-16 04:04:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba68d350-0e95-3a3e-9310-7953c7072085 | -12.2901 | -46.40759 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0aef64c1-c34c-3e85-b0f4-cda0124942f1 | -12.6753 | -47.92312 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44645c99-5e6c-3c34-a8f4-f8d3a5105d74 | -12.66779 | -47.93571 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef58b1dd-5005-3a3f-b209-035c70bb234d | -15.16158 | -52.46242 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95866654-0d58-3140-9a51-6abb39620183 | -15.85608 | -47.32765 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cc91f84-c83a-36c4-b8cb-8014af5eac89 | -12.78234 | -47.92927 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 63de0882-1c1b-3eff-9e5c-6c805c93c4f0 | -12.97593 | -47.96244 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c14fa084-ad46-3db3-9d43-4c8c172beca4 | -12.82396 | -47.23047 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb0a3dd3-8ef0-3738-925d-c196390d6ea7 | -19.15822 | -48.73007 | 2025-09-16 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe030dbe-3250-3c68-99ee-910461606d8d | -15.11763 | -43.64493 | 2025-09-16 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1529bae4-a06b-3b3e-8838-05bdd19abcc7 | -15.41313 | -47.33993 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2462081c-4442-39a3-80eb-1626e5677e1b | -12.78785 | -47.25545 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f60a3ce-ceb8-3248-b2da-69442c82b25c | -16.51597 | -43.54686 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| aa36b039-38fb-3431-a82e-bc4ed21dae6c | -19.53501 | -45.38749 | 2025-09-16 04:04:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a007480-7939-32f7-9258-a41847cd6e76 | -14.61129 | -46.38375 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 052fb4e6-e592-3f25-a672-72febf0459cd | -12.76682 | -47.96586 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e843bb51-55c5-36a0-8d17-9523a5944945 | -12.82881 | -47.22738 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6aded8bd-811e-334b-b763-8002efa2c565 | -15.82283 | -53.47131 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f290366-bd81-3a61-9129-b9dd72fdc431 | -15.80888 | -53.46053 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee930052-7d9b-39b9-8279-229f8e3b000b | -19.88986 | -42.04407 | 2025-09-16 04:04:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3d8ee2b-9e8d-3f78-86e6-bcce69b1ec7b | -17.94319 | -45.25207 | 2025-09-16 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b51ac6ce-b4dd-3f01-a7f6-751e9e8b0be3 | -12.79611 | -47.25743 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3aa48cb7-798a-3f6f-8201-d84b068b7a3b | -12.79198 | -47.25644 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b142c950-a66b-3e89-a622-cc275780d98d | -15.46717 | -47.31599 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca862b64-7b61-3e3a-8720-b03a949a603d | -12.79592 | -44.74573 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8442f2f-4e09-3f97-be2e-12486452f193 | -13.20565 | -47.28283 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42f78e85-9903-3e27-b5df-3cf17f6a3878 | -12.82466 | -47.22656 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fb353de-610f-3d66-aeb0-80734ec85b81 | -14.51455 | -47.39129 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 467106cf-ecbd-3dcd-a7b4-ebea95319fec | -16.28493 | -45.68042 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 783c6b9c-a767-36ec-8ebb-42bbcca62b6b | -14.51122 | -47.38316 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39834a0a-e11d-3264-af02-299d1c0ee29a | -19.62456 | -43.73752 | 2025-09-16 04:04:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 912f2db9-8f60-3fc5-a7b1-979958b63c8e | -12.61261 | -47.96616 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76b9b891-836b-3afe-b28a-c138b4c386e9 | -16.67815 | -49.75927 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a870bdd-67cd-3cc9-8516-6d8694ddb5fd | -16.53012 | -43.73491 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35f29073-362b-33a5-b8df-155aa467c6f4 | -12.80235 | -47.25479 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58888387-dce1-37f2-a962-5686f12b225b | -13.18947 | -47.30161 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27dd5697-1942-3f87-b204-40ec70793c58 | -12.54382 | -45.87245 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e6c7477d-9e72-3bdb-ac4c-e845a9abcc60 | -12.81012 | -47.23568 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a36d10c9-3669-339c-aa21-19c6187b1b79 | -13.74399 | -48.76645 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba39815f-53fd-390f-9f4e-d65287339210 | -14.82801 | -51.66389 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c14ff390-4c48-3b3c-815b-cbd1da1e197d | -13.19707 | -47.30711 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 098fad98-7c6e-3be6-8be0-80b8258aea49 | -16.42868 | -45.67363 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ff1a91a-db0a-3a77-b3b8-598c3e764a48 | -18.61186 | -48.20803 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 49cf1c8d-af22-32b0-ace9-7152e4eb2b7e | -14.51251 | -47.37899 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85dafcc3-cce9-3cb1-8ac3-dd3068b26447 | -16.6344 | -49.41442 | 2025-09-16 04:04:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2d4f6f8-8eb8-3dae-ae5f-0bd69ab88a8d | -12.80889 | -47.18424 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 164b6ad7-2353-3915-a304-36fdb8fe33bb | -12.64563 | -47.95868 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8682c81a-1941-39ff-b488-2fc4ae4bb9fb | -12.79424 | -44.74395 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fe59dab-d75e-3a7e-8830-c6eb7034947a | -19.08175 | -43.12628 | 2025-09-16 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6696aa3f-2563-3100-b539-992a0ec252ae | -12.80862 | -44.74646 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec2c51b8-0855-34b9-9801-bb2b66f84060 | -12.67514 | -48.02205 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f79f512-5a6a-3c34-b59d-baf8cdfa5db9 | -16.59208 | -42.90446 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 052397c4-720b-3ec5-83d4-73ff539eb2c7 | -12.92541 | -47.96809 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bce147a-8aab-3066-a2b7-2df02c4dc10a | -12.69476 | -47.93998 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c040863-ff8e-32b9-9606-e76374925d32 | -16.52402 | -43.73003 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f83f5c1-b4d2-33d7-bbcf-f1b7ec9f06ab | -12.8454 | -47.13527 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 781ef6f9-ad40-32d6-9ab3-1070fbe0c5be | -12.6642 | -47.93055 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 87de16ba-4f0f-3762-9248-dad9bbd002fb | -14.91784 | -51.6468 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 133d3681-3c5f-33a4-b72b-c20e6b37a5b3 | -16.47885 | -55.10913 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ced35e90-6846-3e13-94fb-8c6f1096d07a | -18.98959 | -44.22935 | 2025-09-16 04:04:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8e8bcbd-da59-3325-abfb-b5a15dfefe77 | -15.21954 | -41.80704 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22e39cc2-1e0f-332b-925c-a88b8612e1f4 | -12.69318 | -47.99797 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d561227d-d2d2-304e-9034-770664a0e4f9 | -14.97482 | -46.56072 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6b4a0ad-4107-384c-9dd2-dd2b0ff3f2b8 | -13.20913 | -47.28732 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ac3c2c1-6b95-3720-9bb3-212638629d14 | -12.61965 | -45.75175 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| beadb401-ec0d-3d4b-bf35-fceba01ca238 | -16.15846 | -42.28756 | 2025-09-16 04:04:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51cc628a-50c7-3e44-ab31-d4ac6ebccf82 | -18.8692 | -43.35119 | 2025-09-16 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5cf47dc8-06fa-30a0-98e9-7509736096c7 | -15.40214 | -41.70525 | 2025-09-16 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5a99063e-dd05-36b1-8414-2c8085cc9173 | -12.65824 | -47.71384 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 86e3404d-c03d-3bf0-8379-11bdb20518e7 | -13.20224 | -47.2779 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77325a1c-3eea-3536-94fe-4f2f5e8ac577 | -12.69919 | -47.98989 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cbcff96-2aeb-3a82-ad24-bd5068667230 | -12.82325 | -47.23436 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3358474e-59e0-3714-8e7c-63ecdea2e678 | -14.52423 | -47.33514 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a69d0e5a-b38d-3196-b2b5-6a68b7a4f828 | -15.80305 | -53.45899 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d19a08d2-1993-33e2-b7d6-98ccccbdc941 | -13.00264 | -47.94495 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5178fff5-a5a9-3cd8-9f3d-60200bba0c3a | -17.07504 | -45.82943 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0166a9af-d08e-3b51-8ddd-ebf670045a17 | -15.85674 | -47.32401 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 731213d3-58f0-385d-8480-708337e1db7e | -13.76381 | -48.76071 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 878af258-3dc3-3f76-99f4-e93c100e5f1f | -17.07648 | -45.82906 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3fca15a5-b1b1-3d4f-a3fe-3d734e476ce5 | -15.16431 | -52.46101 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c1109ec-ef73-36a0-932f-24d0a5054a77 | -12.76831 | -47.95748 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab723d36-ebb1-359d-a32e-b70e3c320631 | -12.67139 | -47.94084 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51af3b3c-7859-3d40-bdaf-d13896887ba2 | -12.76745 | -47.96466 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8957bf3-7b13-36a6-8ff6-902c76c31b7c | -17.73207 | -46.76533 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26ed73b3-8419-3e2c-87c4-1b9587c47b16 | -15.16356 | -52.46474 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a77ad69-8241-35fb-a1a0-72ed4f26dd63 | -18.55342 | -44.11047 | 2025-09-16 04:04:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 513fc16c-e3b3-3ef0-8f39-6083e0ebb5de | -14.51361 | -47.32522 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 44d28981-5cf2-371a-a509-3c3841c5513a | -16.93257 | -44.06803 | 2025-09-16 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f710ad2d-f0b1-336b-90fe-be5b9801ce13 | -12.4428 | -49.70306 | 2025-09-16 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a26aff6f-dd41-30db-b06a-9fea980626b2 | -14.52609 | -47.39411 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9cf6af45-eacf-31a7-baae-81a0aed2a243 | -15.84039 | -53.47551 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7afb3c8-9b5e-33db-9c06-2ce194f801db | -14.35928 | -52.92394 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98b39c38-383b-3dea-8958-0f33f32f7573 | -18.62448 | -43.90091 | 2025-09-16 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb3f6170-0f4a-3bc4-b55e-55da3c72586e | -14.45855 | -47.28099 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
