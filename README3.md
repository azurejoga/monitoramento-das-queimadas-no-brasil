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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25948f7f-48ed-39fb-a190-6cb965564ac0 | -4.53059 | -42.94786 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49fb71e5-7e80-3f08-8602-e6ce900f62ba | -4.88645 | -38.38278 | 2025-01-11 03:36:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69ef1268-c023-34f2-bce7-da37db295d69 | -5.39956 | -35.69473 | 2025-01-11 03:36:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66e39b9f-9512-345c-8a00-db8dd54430d5 | -2.91297 | -40.43073 | 2025-01-11 03:36:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 98fc92f4-5a9a-38bf-8c61-e8d6b78e6825 | -4.65367 | -37.91 | 2025-01-11 03:36:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c746368-d387-3c3f-8ec4-de174ea9de34 | -5.40016 | -35.69094 | 2025-01-11 03:36:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30f9d791-6e44-3d97-8dde-ce63548cc589 | -4.64974 | -37.90937 | 2025-01-11 03:36:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7c60243-340a-3a42-a3a4-2cc3583d9117 | -2.91798 | -40.42815 | 2025-01-11 03:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4174babe-84d0-390b-bd7b-e5fe88dafaaa | -5.40363 | -35.69151 | 2025-01-11 03:36:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89812f57-2b0a-3b6f-af92-74f7565fcd35 | -4.53119 | -42.94428 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3047bec8-3372-3bac-9cd5-abfcc08b656f | -2.9138 | -40.42558 | 2025-01-11 03:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6459264f-95ca-37a1-88ab-e3c45cf078a9 | -4.53179 | -42.9407 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 070c7ce4-6b92-33d2-beea-e4b28bed12ff | -4.533 | -42.93357 | 2025-01-11 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7261dc7-332a-38a6-b606-db2f53264113 | -19.7026 | -58.0309 | 2025-01-11 03:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| c401eb32-0909-327f-a66c-710b0d047b10 | -21.17808 | -49.22324 | 2025-01-11 03:40:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 61896007-b21b-3b01-a1b0-455166c0f1db | -20.87675 | -49.86909 | 2025-01-11 03:40:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0c472eb-0072-3bc9-9090-75349b4b026d | -20.87435 | -49.86961 | 2025-01-11 03:40:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 309ab8d6-10bb-3aa3-88a5-9121c45f6599 | -22.78477 | -43.75938 | 2025-01-11 03:40:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d87d9ba-c994-3153-abee-1d614a088322 | -21.17089 | -48.55699 | 2025-01-11 03:40:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 873026dc-1ffe-312f-9941-cbcde48b734d | -19.30397 | -48.38794 | 2025-01-11 03:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76e1c263-4273-3562-90f0-ea35e8693503 | -20.87541 | -49.87461 | 2025-01-11 03:40:00 | NPP-375D | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3b543342-1aa7-3c1b-ab52-9052d6272000 | -21.16512 | -48.55548 | 2025-01-11 03:40:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e36d113-aa6d-32c8-af58-1d30f711a460 | -19.30208 | -48.38745 | 2025-01-11 03:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdd78cea-653a-3afb-bb64-551fe7e8a6db | -22.73688 | -42.95936 | 2025-01-11 03:40:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf91d0c8-5c28-3777-9efe-731f8fdef1a2 | -21.17208 | -49.22165 | 2025-01-11 03:40:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d0c273f-d004-3c7b-adf0-13d89c9d8294 | -22.83479 | -48.85553 | 2025-01-11 03:42:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14a5e343-06d1-3eb4-8a11-d5f35d003062 | -22.83577 | -48.85126 | 2025-01-11 03:42:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d94b64e2-2976-3f65-ab59-56068f5f0e44 | -23.33617 | -46.77192 | 2025-01-11 03:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89bb8990-1baa-3271-b435-6e245a0d1b84 | -23.40392 | -46.5565 | 2025-01-11 03:42:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa83722a-b833-33d9-8571-8e0195c55b52 | -30.38569 | -56.16533 | 2025-01-11 03:44:00 | NPP-375D | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 8e00866a-3abe-373a-ba13-1d385d37f86d | -6.07592 | -37.31865 | 2025-01-11 03:57:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8ccf9e5-9f85-3ee5-b06f-7991f67c1e9e | -2.9123 | -40.42796 | 2025-01-11 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 235fb443-e389-3ba1-8a14-45d8f6f1f2ad | -2.91287 | -40.4244 | 2025-01-11 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 584049fd-2c55-3d9e-9f00-e6c2aa3b4a62 | -4.18466 | -38.36401 | 2025-01-11 03:57:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bf1d9258-db8b-3a86-899c-a019e52ae83c | -5.70495 | -39.26221 | 2025-01-11 03:57:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df698b87-3c3a-3d36-9d18-7b5cf11ffc94 | -4.46177 | -38.52898 | 2025-01-11 03:57:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97628887-634e-3532-b44a-83c7b4cd0ff1 | -4.01293 | -38.81308 | 2025-01-11 03:57:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1b1bffd0-a2aa-3174-8ed7-a0e72ffc166d | -6.07943 | -37.31917 | 2025-01-11 03:57:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77cfa656-39fa-3e64-9a08-8df441166a26 | -5.85538 | -39.08212 | 2025-01-11 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05366b21-c5b8-3d6a-8b15-b5ff827c5adc | -4.88854 | -38.38131 | 2025-01-11 03:57:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4720861-b65b-3081-bf89-07a8307fc64b | -5.80817 | -38.09776 | 2025-01-11 03:57:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3cd9f573-fd33-3b21-bea3-5dd39c4e523d | -6.08042 | -37.3181 | 2025-01-11 03:57:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbca0610-17d9-3a80-9730-1ea60e0f0223 | -5.9514 | -39.68388 | 2025-01-11 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4b26e4b-f364-326c-b05d-d4be8f7eddd8 | -4.88463 | -38.38433 | 2025-01-11 03:57:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b6d7fa0-a376-3293-8137-78f62f1b1d7c | -6.08003 | -37.31526 | 2025-01-11 03:57:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5aa08350-5ad4-3da6-90ec-00ca905de6f0 | -3.71584 | -41.69958 | 2025-01-11 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 738f710a-de66-39df-b885-e8bf96f2d892 | -2.91566 | -40.42849 | 2025-01-11 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 30893d23-eeed-35b3-8b11-938a6bef8d4a | -3.86263 | -40.45393 | 2025-01-11 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 647d65bd-a91f-361e-b842-109b145793e6 | -6.07652 | -37.31473 | 2025-01-11 03:57:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 32075cee-f7f9-33d1-9917-7819e058694a | -2.91623 | -40.42493 | 2025-01-11 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 21a1eb37-8980-3abf-9feb-e5df63bf1299 | -4.65294 | -37.9117 | 2025-01-11 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5bd09834-d0b3-3206-bd45-21d0f604c663 | -3.85928 | -40.45341 | 2025-01-11 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8792503f-b191-37bf-8c57-9dbce7cf4dc4 | -4.12939 | -40.57507 | 2025-01-11 03:57:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| ef796034-eea0-36d0-81d8-e4957fbf71a0 | -5.02816 | -39.67968 | 2025-01-11 03:57:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dfdd2057-66bb-34cc-9f9f-cec56cc7216b | -4.64955 | -37.91117 | 2025-01-11 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de28c463-d9e4-39e8-a0fe-d4f5384ebc5d | -3.86206 | -40.45746 | 2025-01-11 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d155e32-6114-3f61-95ae-bb33135101c0 | -7.34574 | -38.93035 | 2025-01-11 03:59:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8d621d5-1c7b-3aef-b125-9629628ab1fd | -19.43598 | -44.34207 | 2025-01-11 04:01:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3cc5ecf-ea1d-3e86-a894-ffedfa5f7351 | -19.51223 | -44.27831 | 2025-01-11 04:01:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c58cfef8-a32f-324a-b9f9-fcee2ad28a4d | -19.30454 | -48.38718 | 2025-01-11 04:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93796d3e-2c50-3e2e-9898-3c4f3044c616 | -20.69352 | -40.61102 | 2025-01-11 04:01:00 | NOAA-20 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bce44581-4887-3493-9c17-0af226b8a36f | -19.30383 | -48.39099 | 2025-01-11 04:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b040b3dc-e130-31ba-8e02-60c38d4fcfae | -21.29196 | -48.99416 | 2025-01-11 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd6a2892-04fe-3807-b210-f93467b6a78c | -21.17594 | -49.22104 | 2025-01-11 04:04:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0b3d0a97-a8b5-39e7-9c5e-0e9e4c626f7b | -21.19423 | -44.93765 | 2025-01-11 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9bdc6dad-2438-3bbb-8d10-efee94f49c15 | -19.48553 | -55.34062 | 2025-01-11 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 35a14c02-e98e-3d37-a6b9-718b6dda6aea | -22.5395 | -48.81137 | 2025-01-11 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 790924c6-da6f-322b-955a-3da2f3684d5e | -21.16812 | -48.55874 | 2025-01-11 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60845a34-0f71-37ee-8347-236434589bad | -22.8346 | -48.85297 | 2025-01-11 04:04:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 18bdc124-69cc-3865-96ea-b58a49799e1e | -19.66712 | -54.41687 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44270520-5f50-30a1-9a82-20d5e7159105 | -23.98351 | -48.91903 | 2025-01-11 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 312701c7-8d3f-3a4a-ab46-0fc4a87984f8 | -19.66638 | -54.41182 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b493da4-131b-336c-9aba-fe88bc7826dd | -21.17828 | -43.98084 | 2025-01-11 04:04:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fac6c231-1cf2-366e-a06f-84e00f327d3c | -21.28792 | -48.99325 | 2025-01-11 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6888c8a-b3bf-3cca-a089-2334b37c1383 | -19.66538 | -54.41625 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 375070d0-079f-3e79-b1cb-1ebdd49440ab | -19.15861 | -54.84134 | 2025-01-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8927996-8faa-324e-8088-04b4ecf9c3f9 | -19.69077 | -58.03375 | 2025-01-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 457fe6d5-b206-3911-bb9f-78f07ef2685c | -23.89312 | -47.89687 | 2025-01-11 04:04:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 12b3575f-5202-3614-b525-60fa18483bb9 | -21.16913 | -48.55326 | 2025-01-11 04:04:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24843eed-31e9-3cb4-bb62-eea7c328a40f | -19.66065 | -54.41002 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ed253e9-7c75-31c7-b730-85f13d484385 | -22.67447 | -42.85625 | 2025-01-11 04:04:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c25d8925-c9bb-3f1a-b6bd-a46982363727 | -23.40393 | -46.55605 | 2025-01-11 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1d4f70c-9094-33e1-9e9e-fb213abdf279 | -22.6974 | -43.34742 | 2025-01-11 04:04:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64192c54-eb9d-37ed-8940-97e5a8d662d5 | -19.69528 | -58.02571 | 2025-01-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 56ef0824-9d2b-3521-b5bf-01dac3e9e2a1 | -19.66238 | -54.41052 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75342a0d-fd8a-3cfd-9df2-155020b34144 | -23.52027 | -46.97355 | 2025-01-11 04:04:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b00767fd-c098-36ef-93e7-61aa6d63338b | -19.34111 | -54.16658 | 2025-01-11 04:04:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d09f9f21-f9d8-37ea-959b-bfaf1f48ecbb | -19.48671 | -55.33549 | 2025-01-11 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| edd2e2d4-4e24-3ab2-8abc-fb8da6ac10d5 | -20.41783 | -43.554 | 2025-01-11 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 071a37a9-1901-3b3e-ae42-9f827fee746d | -21.62687 | -43.46677 | 2025-01-11 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f22380da-e91d-30e4-a8aa-87ce48a90aef | -20.87346 | -49.8722 | 2025-01-11 04:04:00 | NOAA-20 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e275b19f-32af-3830-8a76-5725dd38bbbe | -23.21877 | -51.15643 | 2025-01-11 04:04:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a340120a-0f41-3e11-9a67-925b16db3db3 | -20.76343 | -46.76805 | 2025-01-11 04:04:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd25c792-73fe-3e2e-b8e6-a313a063b6a2 | -22.85542 | -42.98063 | 2025-01-11 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 22712a6a-f18e-3353-9c94-bfc5566e15c1 | -19.48789 | -55.33037 | 2025-01-11 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 04d4bde6-dc0c-365b-9dc3-558eb6f32f28 | -19.65963 | -54.41451 | 2025-01-11 04:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f809b944-57cd-3b4c-842d-fdf5abd3bf59 | -21.17393 | -49.22178 | 2025-01-11 04:04:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 93e2178a-aa76-3b4d-9943-7f6b792e7e3e | -19.69259 | -58.02628 | 2025-01-11 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e3782733-d464-3184-bd24-536b326246d0 | -19.15753 | -54.84608 | 2025-01-11 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7296b43d-e297-321e-8386-b0c34a3b743b | -23.59243 | -47.43899 | 2025-01-11 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
