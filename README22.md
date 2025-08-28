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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28aada73-a477-35d8-9366-79cd3158a303 | -6.8636 | -43.62115 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b185b3c-c8cc-34ed-9842-8db022931852 | -6.19106 | -44.15657 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 421e38e3-d8b6-3a90-be73-b42d2f269a24 | -6.17959 | -44.06553 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4f12eb0-5e21-3145-b119-f535a85b8b65 | -8.43986 | -41.44535 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b2ba468e-7353-36d1-b2b9-d2fe9bb33efa | -8.43994 | -43.68767 | 2025-08-28 03:45:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23aca069-ebd5-3c18-b3f2-ea052da71f5e | -4.80342 | -47.26418 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0a407b35-8637-3409-80ab-3c2c7451172d | -6.21936 | -43.37298 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c08fe580-b167-3fcb-8819-d739a462d7ee | -6.15472 | -44.05162 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c792f3f4-de57-3838-a7db-5c78db7c9b8d | -6.88908 | -44.39763 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad213410-9292-3bf1-957a-4da250b9248b | -6.184 | -44.00958 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bfb21f0-091c-335a-bf67-3fe59293e3cd | -6.18346 | -44.01263 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ac11669-f535-3b6a-bcc0-bc49eac3ff37 | -6.87641 | -43.62389 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07db4d8c-79b4-3aaf-a3e7-1861d7419473 | -6.95023 | -44.08282 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 085ef7e8-ae5e-3144-a649-30aea6589ad7 | -7.05756 | -44.36502 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f7da9bf-678c-370b-965a-612d857a7598 | -6.32505 | -42.87645 | 2025-08-28 03:45:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c41a156a-dc2e-310a-81ae-82be0a91a5db | -8.02116 | -44.80112 | 2025-08-28 03:45:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f9cc3bd-b255-30f0-b6d8-579153394ccc | -6.1894 | -44.16605 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c31bc3f2-5a5c-3cab-88f2-350da82d0036 | -6.87239 | -43.61699 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b75a0239-989f-38e6-b5a6-d395c920206d | -6.18343 | -44.16873 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52b66fb9-0dbe-3a3a-afb3-bee31371df2c | -7.19552 | -44.06343 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4897952-76da-3ca6-8d0e-9082a007d509 | -7.71327 | -43.96631 | 2025-08-28 03:45:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 470fe25f-ee14-3d80-938d-e4ac44853dd6 | -6.88965 | -44.39445 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a8a0f7f-fca8-3089-969b-d66773de7bfe | -6.16476 | -44.05661 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13e683ff-46f0-37da-a392-edcc5c736b29 | -6.4391 | -44.57758 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31483d5f-8a07-34db-850b-52542347e906 | -4.79567 | -47.26932 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| cd1f961a-3c78-3ab6-9458-4abf9e29970f | -3.23309 | -43.43715 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5ea35ff4-119e-3534-a786-d43a00177054 | -6.08335 | -44.00036 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be67f30-3d63-3a6c-b14b-bd7d812b2cb1 | -8.28391 | -45.16137 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2af04028-fa3e-32d9-aeaa-ffcf296e2000 | -6.32575 | -43.75344 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb696bb7-d43b-3053-b8dd-61ef45440e63 | -4.6692 | -41.02277 | 2025-08-28 03:45:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3c0c4f0d-4e2b-3a1f-a05c-d5bde72b9791 | -7.76504 | -44.06825 | 2025-08-28 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 535f6e1d-ef44-342b-bef9-7e7aea45b313 | -7.39305 | -44.07082 | 2025-08-28 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9717054c-a3f0-356b-a4dd-79e5b13a1ebc | -8.0962 | -45.01131 | 2025-08-28 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dab5a33-aaca-3e39-975f-ee627308bb7d | -5.68881 | -40.97247 | 2025-08-28 03:45:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c6baaa7-50e2-3279-8c08-c74bf1257033 | -5.53712 | -36.84957 | 2025-08-28 03:45:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec6b86d4-0bbe-376a-84a6-35e109d906f0 | -7.39747 | -39.68505 | 2025-08-28 03:45:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1b564eb0-b353-366d-b6df-c4b9e6363a2d | -6.22645 | -43.36205 | 2025-08-28 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efee9c97-d8b7-31df-9f82-68a6f1e12f01 | -6.19532 | -44.16368 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9eb52cd2-5b07-3e59-99eb-2da5ca570981 | -6.1882 | -44.01664 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37fd7533-5df5-34b9-b15c-5ff00fccf9d9 | -3.22951 | -43.43967 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5dcf9278-adf8-3590-b4fe-f618ecf6980d | -8.47779 | -43.64725 | 2025-08-28 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| badbdf06-f29a-3e36-91a7-9eaae36772f4 | -6.17314 | -44.07112 | 2025-08-28 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13a482e0-2dc6-3c23-a825-c0ab8048d185 | -5.64655 | -45.25801 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94140458-5511-3f8c-b65d-7f5f95ecae27 | -5.20153 | -46.06511 | 2025-08-28 03:45:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69aba0c7-f33d-349e-ba3b-d03e5ff80b94 | -6.81048 | -44.36114 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd09f667-a394-3a8a-84e4-bece45634580 | -5.84653 | -45.3047 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bc080ed-349b-33ec-8ccb-2a5427c9aa51 | -6.12626 | -45.06979 | 2025-08-28 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5b248bb-dee0-3fa1-ae5e-07ef05883449 | -6.92499 | -39.56478 | 2025-08-28 03:45:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 33bd0c55-8341-339d-a3e7-aabf6a74f6db | -7.3925 | -44.07392 | 2025-08-28 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e3f10b-7d52-3892-9b44-f946a55b17f2 | -4.80106 | -47.25773 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c4e5938-b39c-36c8-a161-7ecf5d5fc1e9 | -6.71864 | -43.09232 | 2025-08-28 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d54088f6-2256-3fdf-b093-cc53d72fe3f7 | -4.79226 | -47.26834 | 2025-08-28 03:45:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1a25c36c-42ba-3a6f-91a3-520475b92ebc | -6.28066 | -44.48154 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8fc0af5-9971-303c-8469-c78c44f9375b | -6.86516 | -43.61204 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6871c7f9-3020-3f5b-8ca6-b4d558724d5c | -7.63292 | -42.67227 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64ea5898-f2ea-332d-bcea-3edd49a623d7 | -6.88019 | -43.60269 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1ceb8c86-1b72-3f4f-b206-1924c7038383 | -3.22897 | -43.44298 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f7407f01-a427-37a0-931e-9a994aa0fcf6 | -5.41293 | -41.14608 | 2025-08-28 03:45:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| c2473d34-6006-3b5f-b455-6522f6e4a86d | -9.65242 | -40.59772 | 2025-08-28 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 68178b07-e8a1-3beb-9aea-dbc2b0ee9446 | -7.78485 | -43.1804 | 2025-08-28 03:45:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e91959d-9a40-3f67-8490-2460dcd5a34b | -6.44458 | -44.57846 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb8511a3-3846-3bb2-9330-15513dcc0ee1 | -6.8062 | -44.35412 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c1b16e8-fd73-304b-9fd3-80b3a09c3421 | -6.86273 | -43.61231 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75068cfa-9610-39ea-bcb1-d6eae8438884 | -6.87293 | -43.61396 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f7c36928-919b-3a99-8cd5-578cb0096735 | -5.53428 | -36.84527 | 2025-08-28 03:45:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46c8f68a-caf6-39df-9ea1-40f681be2477 | -6.33037 | -43.75755 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50107b92-4400-3d35-bbca-f03ca7653859 | -6.43704 | -37.13643 | 2025-08-28 03:45:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5eeb4c13-cfa6-3bb8-aedc-4461ddec0336 | -5.84579 | -45.30889 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3042202a-70b5-3c23-956d-d7085752c05c | -7.89553 | -44.77668 | 2025-08-28 03:45:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1100cb45-c0ab-335e-9794-5403e6739fcb | -7.75241 | -44.04981 | 2025-08-28 03:45:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb63ba6-de9d-3b58-9ccb-607ba5af4b25 | -3.23005 | -43.43637 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e209921-6f5a-3582-b9a4-ef7b7e3e08b7 | -5.83996 | -45.30806 | 2025-08-28 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08af6a3d-aa91-339f-ac90-40cf922ad60b | -6.32519 | -43.75664 | 2025-08-28 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b102acff-fcae-3059-8891-d01ef73d3d0f | -6.40915 | -45.22232 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c36de7-100f-3466-92bc-0b34a45b305f | -7.23423 | -45.43464 | 2025-08-28 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbc7b80d-f0ed-327f-a9cb-2980a25e6303 | -9.65384 | -40.5995 | 2025-08-28 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e0aa68fb-6e43-347b-80c6-fd1e36ee56b1 | -7.13654 | -44.81811 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5fdaecd-14e7-39df-97cd-dbdb24b42a39 | -6.86512 | -43.62827 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bceda585-df83-3170-bb8e-ca5467c10372 | -6.81638 | -44.359 | 2025-08-28 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c41afce0-ab63-339b-ad1b-526cf5f5c8a1 | -8.43841 | -41.45361 | 2025-08-28 03:45:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| e447db9b-0e1f-3ed2-b336-03818a439de5 | -7.63763 | -42.67313 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6504c7af-4197-3f49-baa1-f77f04a4f873 | -6.87749 | -43.61781 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 93520c73-87fc-35a6-b9e2-8e01a6e8ab54 | -7.18262 | -44.87326 | 2025-08-28 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52784d4f-e6a3-3c13-83b4-5aae7c3b2568 | -7.24582 | -39.17688 | 2025-08-28 03:45:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ab98643-bd5c-3b17-8d02-3c10f8cf66ba | -3.2373 | -43.44467 | 2025-08-28 03:45:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e68609b-745d-32dd-9e9c-fb539fd6902e | -6.86729 | -43.61617 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bb1ba6d-57ad-3072-8076-56f32214b9b3 | -7.56453 | -42.00861 | 2025-08-28 03:45:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9330abb5-8827-3ff9-a5fe-8412ca039713 | -7.62857 | -42.69731 | 2025-08-28 03:45:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a197c801-ffdc-3cbf-9f47-435021a91035 | -6.85954 | -43.61425 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c9c5df0-4f57-3f88-9230-ce51d9e1ddd8 | -7.94513 | -42.62799 | 2025-08-28 03:45:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 812534be-39e8-3ea3-8dc4-ee24fb8c1996 | -7.24051 | -45.43251 | 2025-08-28 03:45:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cadd08e-9457-3d4f-a4e5-74bb6b9603d9 | -7.20083 | -44.06496 | 2025-08-28 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7007490-dc9b-3ff3-ac0f-ed718831c879 | -6.86566 | -43.62524 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e06eb654-5801-359b-ac46-509dd440c7d6 | -6.87347 | -43.61093 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 61a763b2-6c1a-3d12-8682-950a7a4b0520 | -6.44094 | -44.56717 | 2025-08-28 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 609dde04-b83e-3e3b-9352-6b0ba6584894 | -7.43224 | -42.04416 | 2025-08-28 03:45:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c7e05ca-004f-3df5-9284-d8a04ef2ec32 | -7.06548 | -44.36639 | 2025-08-28 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db3304c4-ee68-372d-96f3-d15c93087b8e | -7.55552 | -42.007 | 2025-08-28 03:45:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84bba92c-ebe0-31ac-947b-d37dcd3373c7 | -5.53367 | -36.84902 | 2025-08-28 03:45:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0561d37a-4d42-3394-ae91-491c566df24d | -6.86838 | -43.61009 | 2025-08-28 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
