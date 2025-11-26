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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a924997d-eae8-35d6-a03c-196aa1ea25a3 | -4.17227 | -49.87312 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 893a04df-8b2c-3203-a114-772cb1831b7f | -6.3521 | -45.81886 | 2025-11-26 04:21:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4826c1f9-266e-3895-aa5f-66a6ea676521 | -2.92326 | -48.2313 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eac166d5-9a76-3302-a50d-fe0fe9322bd5 | -3.96719 | -50.2217 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91f39bed-3bdd-3862-a2d2-d2f2f1547291 | -4.21668 | -49.14756 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 597b5acc-d5f6-3368-bb44-d03f3c8a5174 | -2.69575 | -49.51875 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45307250-f83c-3984-acce-e1b199446e05 | -2.47409 | -50.24656 | 2025-11-26 04:21:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04f8a3fa-ba0a-3b71-8d7b-dd2368d5905a | -6.4866 | -38.82261 | 2025-11-26 04:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a2c45a8-5cb3-3801-9bad-83e77e4a3be2 | -3.04068 | -51.03878 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3596fe0d-7acf-3004-bc33-8f3a54ac94b5 | -7.16932 | -44.9961 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2da34ed3-ff5a-329b-bb1c-925876cd7d94 | -4.1931 | -43.70144 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c27f5b27-adf2-3208-a6c0-41ee52cae630 | -7.75013 | -44.19389 | 2025-11-26 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d66877-4618-307a-a489-1a4dad6380b1 | -5.28966 | -43.64132 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 225ca015-4862-3f27-b0e6-86d5a8048679 | -3.21979 | -50.57239 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf2d4f8d-6ffa-32a3-bdb0-8fb024f8f311 | -8.04327 | -43.12956 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 18cfa30b-f33e-3a63-8420-d4295db5d298 | -3.28241 | -42.18011 | 2025-11-26 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 534eb244-f0f2-35ea-9102-740740399cc1 | -4.71085 | -43.99521 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7551e82-9f21-3edb-88a4-1362948b976d | -4.25558 | -45.13353 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49959f6e-4c77-3661-8e3c-8d3225269af9 | -7.31524 | -48.48615 | 2025-11-26 04:21:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 872ea23d-c6da-3476-b0fa-844599854c83 | -8.05299 | -43.11188 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 208f1f9d-f358-3ee9-8963-b5975876ee69 | -6.07993 | -44.87933 | 2025-11-26 04:21:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab22bda-6e6a-37ec-9285-bcb8ab02eb36 | -3.01819 | -51.14413 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2025bd99-9da4-305b-a42a-331cdbf7779e | -8.05355 | -43.13114 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 04d2ba97-608b-3d0c-ba7c-f2f3583dec5d | -4.56608 | -43.29543 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7060248c-7256-3b3d-9e1f-05fe2b30f722 | -8.04842 | -43.11885 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 54e599d3-e613-3404-a584-7b718a8c84f1 | -6.44633 | -44.21461 | 2025-11-26 04:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77076bc1-fda5-37d6-8960-01b56fb60d83 | -7.05567 | -38.85817 | 2025-11-26 04:21:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5373ca59-cddc-3963-8796-fed6a41ff8be | -4.99478 | -40.78717 | 2025-11-26 04:21:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9d500ab-bca2-379f-8fc4-b5eaa1362b69 | -3.01817 | -51.03711 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd65c12a-b5e4-3616-9fa9-7ce37dbaaae7 | -5.05832 | -44.16296 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3d53595-e2f3-3be8-8a4e-2684b7d81c17 | -4.71937 | -46.46618 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18d4735a-abf6-3758-80c8-da0108d3c006 | -3.85413 | -49.36706 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7216809a-4811-3e36-8a12-c4d028706137 | -3.59631 | -40.98819 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f0579bd-b671-3a41-8920-7452ef0fdad3 | -5.17339 | -35.70916 | 2025-11-26 04:21:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf9b19e0-6f2e-3146-b3fc-6dfb9cb5c00b | -2.48163 | -48.22993 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49c9d747-7ff4-3e24-8d87-aa8b9ccd9998 | -4.70863 | -43.98779 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba39c62e-fa97-3dc8-89e9-6a8d02e0d2dd | -3.23715 | -50.5947 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c669e072-c2f3-36a2-96cb-0eb442c173cf | -4.45235 | -44.30014 | 2025-11-26 04:21:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc083ab3-6b33-3a47-855f-1deef7a100c2 | -3.85436 | -49.36749 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c34a55-4f4c-39cf-a3f6-6997c08fdcb4 | -4.94978 | -41.16284 | 2025-11-26 04:21:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25a3f3b5-b272-3662-b9ca-1d170cb1f0e8 | -2.48086 | -48.23476 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5b4ad1d-a6d0-3908-9e9c-e97251318259 | -4.41594 | -43.49408 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c63ed65b-ec29-39a2-ace6-2129e72dafe6 | -7.51231 | -45.72358 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaa19911-55a5-37fc-b5db-446191cdc50f | -8.05814 | -43.10114 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d12b326-7722-3d7e-970b-f67a76cd8e79 | -4.02163 | -45.2154 | 2025-11-26 04:21:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 858405e5-9a39-3298-85b2-f0338b8e84c1 | -3.4711 | -50.79562 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd729c69-725e-35b5-bfa6-9c913f2e57f8 | -3.67136 | -43.56317 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c42361b-e9ec-330e-b17f-f3087c8f5b0f | -3.88053 | -50.30608 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8a77978-f428-356c-9ac5-0a8c0f46b9f4 | -2.49104 | -47.832 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 256d1caa-6f2f-3d57-89c8-5a2a797c0f81 | -3.48339 | -50.44407 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 824cb479-269e-386b-b223-dcdb81f26d19 | -4.21674 | -45.5281 | 2025-11-26 04:21:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8c423e-8743-38c1-a6be-38c1cd5c777a | -4.14329 | -42.54633 | 2025-11-26 04:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d173aa9b-c79d-3605-a1ad-b45ab82285ca | -4.65018 | -43.97159 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1812bd57-1b31-3158-bef5-5c431e24a01c | -4.17442 | -43.7339 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 794ea770-3282-32dc-b76b-c91b18d3cf04 | -5.8715 | -48.17369 | 2025-11-26 04:21:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d39285e-edbd-3e30-a489-622b875a2fba | -5.37487 | -43.72641 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e866be52-2433-3017-bad8-114f4b7354bf | -7.496 | -42.88215 | 2025-11-26 04:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b25d3eaf-1920-3b90-a4e5-c2a594f4c908 | -3.22003 | -50.58736 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 914aba8e-5651-36ca-9279-fa3a5c12da3c | -3.70262 | -45.89434 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22a2752b-9765-331b-ad61-0de950f980b9 | -8.05585 | -43.11616 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 6c3de07c-81b2-34c3-b0fc-f601f8e61239 | -3.30413 | -50.27341 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a24fbce-32eb-36ca-a4d2-37200d44901e | -4.97345 | -50.87317 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c7e7af4-077f-3b86-a4f8-977242c88a50 | -4.56022 | -49.69501 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a89558a-07a7-38ea-95a9-80e3b1f86fb9 | -3.36252 | -50.30019 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7381bac1-9fcf-31e6-a784-e5428c8d7596 | -6.03429 | -45.83012 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e4b397e-fafb-3853-9b3a-47a99cd3d888 | -3.66012 | -50.1669 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29fc47f8-4580-3992-bde5-1bd8c1d83ecf | -3.32116 | -49.72369 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98c698e3-7951-3f8d-899d-bedacc96449d | -10.20902 | -36.36353 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ac08c0f4-36a8-300d-ab62-53a4b580657a | -8.04728 | -43.10331 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79ab14f5-0951-3e64-af0d-d9e8cdbbf164 | -3.98922 | -43.39918 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f007959c-624c-370b-b6c4-d75670776fa0 | -5.74372 | -42.36738 | 2025-11-26 04:21:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 557e1d52-0593-346d-992f-121414fe8f6f | -4.26667 | -45.12812 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 96ea87aa-09d9-3aae-85e1-78d090f4ad8f | -8.05984 | -43.13592 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9e79549f-05d5-300f-b3ea-abbc148852cb | -8.05127 | -43.12312 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 1fd17b68-8def-3546-8152-717324d5b3d8 | -2.93479 | -48.23313 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 543f94e7-dcc6-3bfd-9e5d-7c744eafb93d | -4.61369 | -41.05804 | 2025-11-26 04:21:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6f17c19e-a536-35df-81c7-b6a3be60357b | -4.52911 | -46.42869 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749ab016-5d3e-3ffa-a5c8-f32d18e30d89 | -8.05698 | -43.13166 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 722a1af5-e8c2-3a93-8113-c38848d2b956 | -3.5181 | -43.69456 | 2025-11-26 04:21:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5645ee3-b2c6-3e48-a328-e6494436e65c | -3.6998 | -45.89016 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b2488a8-e3f8-3fe4-802b-74bd1d4aa4f3 | -3.45204 | -50.55007 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31f951d3-c0ed-3617-b327-567515fde720 | -2.40885 | -47.59871 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f45a74a-f430-38bb-b914-9bb67e18b55e | -3.65734 | -50.4852 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7523b981-f309-3632-aa96-55de7a99a588 | -4.55941 | -43.2944 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1db260d1-d78f-3c64-8545-ed3886919a6b | -3.32599 | -49.7205 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d288e4e4-af95-3f4c-83b0-62d5c88a21ab | -4.2262 | -48.37299 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e104a5b8-4b31-32c8-9b31-d906df910d17 | -4.16448 | -43.73235 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| eca64127-d0f6-3bf0-bc26-eeaa97160918 | -6.2449 | -46.94422 | 2025-11-26 04:21:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d16ce516-ec69-337d-9f83-43245db3d5b0 | -5.5904 | -45.18119 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07b51ca9-0196-35c0-80a3-be7ad325e5d5 | -8.05414 | -43.10437 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e38be99-b6ea-3c51-a90d-b8260b96ab5b | -5.17842 | -47.10359 | 2025-11-26 04:21:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ecc61cf0-9e1c-3fdd-a423-d50637bf3065 | -4.59115 | -47.89056 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46335e6e-2420-3e35-99ca-cd54acffb9d3 | -2.48424 | -47.82624 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a21ab09-ea84-37ae-8874-4e5f5c728adb | -4.26057 | -45.12358 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fda2df44-746d-367e-9940-ccf83d26d564 | -3.4485 | -50.5515 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa4d6fe2-c6a8-38dd-ae7d-b65223347799 | -4.28768 | -47.30682 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9182334-6ada-3cce-abc1-cc9cde4e2f9c | -6.55757 | -39.0195 | 2025-11-26 04:21:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 326003ed-1000-3aef-ab30-b6d435217fb0 | -2.92402 | -48.22655 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4db97278-0b77-3358-9332-0fb7cba78075 | -2.47464 | -47.83595 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db27e3b8-d293-30ca-a118-dac425732b28 | -3.26468 | -50.59468 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
