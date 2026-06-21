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
| e5fd1608-e727-33d5-ab65-2ae6a6efe1fd | -10.53595 | -47.73385 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eaf3d35-914c-352a-8f82-be8d6b590eaa | -11.6363 | -48.53947 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e496a7d5-e7a2-3963-9a44-36af7357ac61 | -8.35615 | -50.50495 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fb7b590c-a06a-3805-9ab1-70047f694cc0 | -8.35745 | -50.49765 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4b474f67-93e4-33ed-b5d1-f1575ea093e5 | -11.94566 | -43.9619 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13cd41c0-9bff-362e-aaae-c90916bb5b67 | -11.55063 | -48.2682 | 2026-06-21 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ce6eee9-42ea-3ff8-b069-0700325f1503 | -10.05945 | -48.09 | 2026-06-21 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f65fe26-dc1f-3803-976b-0860d0b08505 | -10.69093 | -47.70082 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c01c1a7-de96-36b5-b10f-a133f00e0975 | -6.83788 | -47.92356 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4cb8a96-2569-3598-8f36-294547b20f61 | -10.58962 | -44.33231 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8491a014-584d-33c4-80ed-004736edd7c2 | -7.18649 | -44.87149 | 2026-06-21 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e1a1907-2354-39f6-8a58-d1f3ca9d9a04 | -10.54233 | -47.73088 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb373045-a79f-388c-8fa8-e70c91a48312 | -10.81163 | -44.56587 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c92659e-1411-30f5-965d-d108a3dba867 | -10.59492 | -44.32854 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c32317c9-7697-3798-8870-bbaed23c00cf | -9.80272 | -47.48546 | 2026-06-21 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b6d5dba-3316-3df3-b6a5-2f40f1e18afa | -8.35057 | -50.49706 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f16a743-9955-36d1-b377-d9c57e1ad320 | -11.5449 | -48.2672 | 2026-06-21 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1128cf68-fd0f-3899-8b5a-ffd2eb95b808 | -11.89031 | -43.83532 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f49e5024-8ca1-3be5-b21e-2d261664ad87 | -10.5396 | -47.71474 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6db4a44-128b-38ed-9ab0-9d7a44d6b1b0 | -10.05863 | -48.09428 | 2026-06-21 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0599ddd2-123d-3b6f-b656-03f9e215e989 | -8.34937 | -50.50266 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7dec5e69-31ff-348a-8cea-4445d733b6ea | -11.63788 | -48.53128 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4c5ed48-b739-36c2-8563-59da7134f92b | -10.58151 | -44.3261 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5eb5b405-7b2c-3488-a9e6-9b35087e1384 | -8.65044 | -47.76675 | 2026-06-21 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac8baa8-9398-3948-b674-803cbddf2f3a | -11.01168 | -45.21164 | 2026-06-21 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34bc78bd-2606-3bbd-9eaf-55fea541f9b8 | -8.05138 | -37.5627 | 2026-06-21 03:49:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c689d3c8-aca4-3fef-9842-e844b5a4603b | -11.1168 | -54.1294 | 2026-06-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 23ea44b3-9805-3d07-8d89-87191f06ea34 | -11.0976 | -54.1516 | 2026-06-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 641578aa-aab6-3521-a6dd-a7ec7fada0df | -11.0979 | -54.1311 | 2026-06-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 3768665a-fcdf-3929-aa32-6ffe9db2127b | -11.1165 | -54.1499 | 2026-06-21 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 22cebf28-17b5-3a91-9a5a-843ecdb50f43 | -20.52001 | -48.75146 | 2026-06-21 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f32b49f-e8f8-3025-ae6d-d0ffb1805f33 | -16.05986 | -42.08951 | 2026-06-21 03:51:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 66ecdbd6-77f7-30f4-a3ef-8e671c90a751 | -20.12326 | -40.76856 | 2026-06-21 03:51:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8438afb4-9296-38c3-8fa7-f64a5ceacb54 | -16.10939 | -39.2742 | 2026-06-21 03:51:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 559ac765-8380-3d8a-9a52-29fa295111ec | -19.44235 | -42.086 | 2026-06-21 03:51:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3f78aeb-6669-3e2c-bd9e-ea3416540551 | -16.49948 | -43.50025 | 2026-06-21 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a7b96bc-78a9-326d-8b30-265fb0d6e8de | -16.0606 | -42.08521 | 2026-06-21 03:51:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c518ef0b-254c-3d7b-9b1e-da98167f22ba | -21.46312 | -44.31907 | 2026-06-21 03:51:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7ed16c8d-d28d-3a45-b014-6af308e7b638 | -16.4072 | -42.30575 | 2026-06-21 03:51:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09c44c87-a39f-3ee6-9959-5d73010f368e | -18.7732 | -40.90216 | 2026-06-21 03:51:00 | NOAA-21 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f623d15-478f-35a2-9e75-157764a22380 | -15.95712 | -42.16192 | 2026-06-21 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df00f7a7-21ce-3b9c-a64c-f03102ec619b | -15.75056 | -43.02532 | 2026-06-21 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 593b3ca9-2d68-36fb-9ce6-8ab240fd215f | -20.8206 | -41.92709 | 2026-06-21 03:51:00 | NOAA-21 | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2649e9c6-ac77-3fc5-b699-c240270f9936 | -16.06345 | -42.09015 | 2026-06-21 03:51:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6830b1da-fd68-3f82-b797-a5cf0274ac1b | -17.61504 | -46.69851 | 2026-06-21 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fe304bc-f84a-3efe-8619-3611d5164337 | -16.49739 | -43.50184 | 2026-06-21 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c618c4f-c3cb-3e64-8406-fe2ffde09a2d | -16.48879 | -43.43777 | 2026-06-21 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0dda3d71-c8a3-3adf-a0e8-e4685475c45c | -18.77258 | -40.90592 | 2026-06-21 03:51:00 | NOAA-21 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c9b8316-deaa-3724-ac59-401c82920bb4 | -15.96074 | -42.16253 | 2026-06-21 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 179b03c6-caa3-3bfb-a5e7-33bcb523e312 | -16.50243 | -43.50588 | 2026-06-21 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13024935-5f33-3fba-a60b-a925b8469ccf | -16.50124 | -43.50252 | 2026-06-21 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28f7dadb-5d8f-3e27-a884-8b8b8c501924 | -16.09085 | -42.32801 | 2026-06-21 03:51:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 21e33beb-6a9c-31c6-9435-95474f53b62a | -21.46684 | -44.31987 | 2026-06-21 03:51:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7fb7f516-5abf-35c3-9676-5a4b8555890c | -16.09523 | -42.32431 | 2026-06-21 03:51:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a4ab3ca6-ad54-3c74-8fc6-42f2b361c921 | -18.84966 | -44.78573 | 2026-06-21 03:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdc02ff6-cb79-38c8-bb65-a0c5461ce502 | -24.94641 | -53.44762 | 2026-06-21 03:53:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34f991d0-6db1-3a1c-924a-6ff38bdcba32 | -23.45617 | -46.74637 | 2026-06-21 03:53:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 31782de2-d214-3d99-ae3b-4684053debbb | -26.61844 | -48.76754 | 2026-06-21 03:53:00 | NOAA-21 | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3c86f41e-30bf-3940-b4b7-accda3e1371a | -11.1168 | -54.1294 | 2026-06-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3b7070b7-fdef-3a5a-b5fd-3be1e8eede47 | -11.0979 | -54.1311 | 2026-06-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 2dc7ef6e-320c-3326-b005-99ddb1192b73 | -11.0976 | -54.1516 | 2026-06-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| cb1c0627-2c56-3482-9251-1f2524d1bebb | -11.1165 | -54.1499 | 2026-06-21 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 54086070-3b2c-3045-93cb-5b80ccc902b9 | -11.0979 | -54.1311 | 2026-06-21 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| de6b59f7-75b1-3e68-82e4-f47da64505b2 | -11.0976 | -54.1516 | 2026-06-21 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b981634e-03fa-31f0-b479-172573710a34 | -11.1165 | -54.1499 | 2026-06-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c3b00de2-7bb4-31c8-8b88-d8feff3025fc | -11.0979 | -54.1311 | 2026-06-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 1c53a1b9-2217-3bce-98b7-5f36fc7e0bcb | -11.1168 | -54.1294 | 2026-06-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 751f66ee-da4f-35a5-ba57-9b5f2780a270 | -11.0976 | -54.1516 | 2026-06-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| c6e41c67-7441-3a6e-9c01-cf21513ce50d | -4.06383 | -43.24621 | 2026-06-21 04:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e00e54c-c84b-3258-9f4f-ba54dd23d9d4 | -2.98747 | -40.03889 | 2026-06-21 04:21:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ceea750-6559-3bdf-ae21-3e550e463809 | -5.81411 | -45.08241 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6739bea-39fe-3f43-a2c0-f947e98301df | -5.81814 | -45.07927 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dde66605-4c5e-322c-9dbe-4fe2f9d8523b | -6.17474 | -43.35293 | 2026-06-21 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d82c9f4a-d0b6-3eb6-b5a7-e43e0a8b08f3 | -6.95719 | -42.06386 | 2026-06-21 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61b3acdf-d28d-346f-8def-d59f73c36a24 | -5.81531 | -45.07495 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cae66d0d-305a-33fa-8f7f-2795bb71a692 | -6.96058 | -42.06437 | 2026-06-21 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce4b3292-a60e-3fc2-9eb5-5439c92275a9 | -4.45901 | -48.02334 | 2026-06-21 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86a4a2f8-78b6-31a4-b3d2-4066ebdb6457 | -6.50372 | -42.21494 | 2026-06-21 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4c445ec4-27d2-3806-b44e-463a182d3831 | -5.81874 | -45.07554 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2cac45e-894e-3358-b8c6-623a6cbd78fd | -5.81651 | -45.06751 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c9a9742-80d9-3aed-848a-da8751f0102c | -5.81351 | -45.08614 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e2ceed5-1fdf-3ef3-932c-5ec3f25669ff | -3.85264 | -54.2248 | 2026-06-21 04:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43176120-da11-3e75-b41b-56f23f9286bc | -5.89536 | -39.25204 | 2026-06-21 04:23:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cbc6c07d-dad0-3e6a-b921-e94b168d9bb8 | -6.50036 | -42.21441 | 2026-06-21 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96ed3a79-829c-3cf4-bb41-fefb790f6efa | -4.45493 | -48.02269 | 2026-06-21 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5d27edd-1133-344f-b1e7-e1632771d639 | -5.81695 | -45.08672 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 056c95db-857c-35cf-aedf-b836ac3cc9a9 | -5.81754 | -45.083 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54b9fe57-9288-3134-81cc-586b54f6bcea | -5.96034 | -43.48992 | 2026-06-21 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27f5f66e-9eb3-39be-8e24-5db6eb64ff64 | -5.81591 | -45.07123 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 232d17ee-add4-3b8f-97b3-5daf77ec1e33 | -6.50317 | -42.21849 | 2026-06-21 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ee1d0c0-36d0-36ee-9363-0e9b1a5b9e77 | -6.17141 | -43.3524 | 2026-06-21 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76a23ff8-643a-34cd-9a9e-063a2dd9e0af | -6.50709 | -42.21546 | 2026-06-21 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c3857a9b-6a6e-3f32-a387-df8aca9fa168 | -5.82038 | -45.08731 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08a458e8-ed90-3cbe-951f-e3695f8869f4 | -5.95978 | -43.49339 | 2026-06-21 04:23:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e782f8fb-e377-3c26-acf7-12292cbf1263 | -5.58675 | -46.37241 | 2026-06-21 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3f1d617-c4c6-3b90-a491-c911d0f9b398 | -6.95663 | -42.06746 | 2026-06-21 04:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c673a2e-80bd-3dca-92fe-97157e5405bb | -5.89475 | -39.24932 | 2026-06-21 04:23:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a78d2a1a-dbb6-38b1-96f7-916b961c63f6 | -5.81934 | -45.07182 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d513f2d2-d783-3538-a5d5-86aefa9bd70e | -6.08159 | -44.00224 | 2026-06-21 04:23:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9b60cd6-4002-371b-8ec7-49d68d2cba46 | -5.81471 | -45.07869 | 2026-06-21 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
