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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66bdd5b4-3c2f-3d6c-8a6a-17ce0aad7ef5 | -14.9317 | -41.15329 | 2025-09-18 11:38:00 | TERRA_M-M | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 77fdce10-4ec6-3c95-bfd0-28c0654ebc8b | -13.70614 | -42.01883 | 2025-09-18 11:38:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f90db1d6-4498-3277-9568-4ae48955b5ea | -15.48546 | -41.59973 | 2025-09-18 11:38:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 829846aa-a2c7-3fe3-9719-063051e14b8d | -13.07393 | -42.13447 | 2025-09-18 11:38:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| b8ca24be-c764-38c3-add4-94e69645da75 | -8.71827 | -46.37056 | 2025-09-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 465.2 |
| 07a63aec-1313-37e3-b9c5-a30958970a35 | -9.18959 | -47.07412 | 2025-09-18 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 78cecc40-5704-3713-9d11-649cb93f43e9 | -13.59884 | -41.53365 | 2025-09-18 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 3559cfb6-bf83-31c0-ba2a-3ee505dc6f58 | -15.32396 | -41.91232 | 2025-09-18 11:38:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ffaf211e-36a0-3411-9926-d8665e63a3d8 | -11.21732 | -47.4285 | 2025-09-18 11:38:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| efba326e-8926-3102-82a1-c3717b32df2d | -15.52642 | -41.99559 | 2025-09-18 11:38:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| f8ee27e0-bb9d-3208-a3c7-f81c5df79220 | -13.61697 | -41.54933 | 2025-09-18 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8bc392c6-c178-33af-9c36-54a3429a9714 | -14.69873 | -42.66421 | 2025-09-18 11:38:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 49a228ab-b37d-3aca-9cf4-deaeedcfd0b1 | -9.01303 | -46.31229 | 2025-09-18 11:38:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 57b2c678-d2d6-3e6e-ae91-a3d692177a49 | -13.68549 | -42.85571 | 2025-09-18 11:38:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 4d7efafe-6466-3934-9830-75bb8834e533 | -13.59693 | -41.5457 | 2025-09-18 11:38:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| fe18f8a6-dcca-3d1b-902a-ceb7a100af0d | -8.71022 | -46.37661 | 2025-09-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| b2789bb9-72d5-3623-be9a-6eb693796e18 | -13.7041 | -42.03153 | 2025-09-18 11:38:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 680c1fac-2138-34a6-86dd-e10eb11d8f01 | -12.69798 | -45.29176 | 2025-09-18 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d124f135-a43d-3eb1-a38c-35097057e50c | -13.15813 | -42.55408 | 2025-09-18 11:38:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 47e8daf2-00f0-3643-bded-e15b91db94f8 | -12.701 | -42.36913 | 2025-09-18 11:38:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 949defee-70f3-3c51-99aa-1fd53efac6fb | -12.10693 | -44.82114 | 2025-09-18 11:38:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 284a7936-9b45-34a5-87e3-7762db9197b0 | -12.09439 | -44.83587 | 2025-09-18 11:38:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| c2aac0c4-8add-3336-81f2-b8f2784866a7 | -15.5267 | -41.99004 | 2025-09-18 11:38:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 5501cf06-4e7e-395b-a3b5-9f38d9265400 | -8.95602 | -45.01006 | 2025-09-18 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| fe7e1d5d-38e5-35b0-8862-65242c7931a9 | -12.75914 | -42.44308 | 2025-09-18 11:38:00 | TERRA_M-M | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 58813507-52c7-37e2-b3f9-dd7629d36c68 | -13.592 | -43.35642 | 2025-09-18 11:38:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 134c5e34-7f63-3daa-b02e-931b2314fbcf | -9.00383 | -46.30504 | 2025-09-18 11:38:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 9bdd887b-f3e6-35c5-80db-20088a1eb17c | -13.98875 | -41.46801 | 2025-09-18 11:38:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 623e843f-e940-3da4-b707-f626af3b81dd | -11.56027 | -38.87381 | 2025-09-18 11:38:00 | TERRA_M-M | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| efb23b35-990e-358a-8c90-f7eee0eccb1b | -11.93641 | -38.3277 | 2025-09-18 11:38:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a5184170-946a-3dc8-ad95-a25c22182fbb | -14.69647 | -42.67799 | 2025-09-18 11:38:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c41bdb15-c659-3417-b0bc-7de2d69bbdb9 | -13.14724 | -42.55235 | 2025-09-18 11:38:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| cb230a5c-6f91-3e9b-9284-76150fdd65e0 | -11.21136 | -47.42197 | 2025-09-18 11:38:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 90a6b8b8-69d6-3240-8de0-34faf09f3641 | -8.98801 | -46.30266 | 2025-09-18 11:38:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a9653df0-1f74-369f-b194-a363ca2ad8be | -12.69122 | -45.28459 | 2025-09-18 11:38:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 922816cf-7551-3624-95db-4390701edb83 | -8.72613 | -46.37943 | 2025-09-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 374.0 |
| aad42f5b-ef3e-3e5b-9786-87c055e8b4c8 | -13.4713 | -42.4666 | 2025-09-18 11:38:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 296200a2-c704-33ae-abfb-e00899154798 | -15.4837 | -41.61106 | 2025-09-18 11:38:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.5 |
| 4a852dcf-4ae5-3a49-9523-6ae7d059f316 | -15.52477 | -42.00195 | 2025-09-18 11:38:00 | TERRA_M-M | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 73116341-6d4d-35bc-bc76-bd3677b3cf99 | -9.1973 | -46.99226 | 2025-09-18 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 43affa12-e93f-3fe8-bd88-9be3068d8d90 | -12.10299 | -44.84387 | 2025-09-18 11:38:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8385d0c7-641a-3a1b-af21-e52b22e21bac | -8.67502 | -46.43283 | 2025-09-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1341b170-af7a-30a5-a9f8-13a22d24930c | -15.80169 | -41.49225 | 2025-09-18 11:38:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0e719e76-2be4-3ee0-96ec-62a4f68d18d3 | -8.7023 | -46.36808 | 2025-09-18 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| b3f9575c-b78c-3870-9232-79e8364e1986 | -9.01 | -46.3039 | 2025-09-18 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| dbbfd0cf-add6-362f-ab3e-3be7d18d3c2d | -8.6502 | -46.431 | 2025-09-18 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 2275833f-cf82-355a-bba7-9c941192f340 | -8.9911 | -46.3059 | 2025-09-18 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 01fe2e3b-ac84-373b-8ea7-88a3c5843dcb | -8.6504 | -46.4086 | 2025-09-18 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 9b0bc7a7-5802-30b1-8f86-c72444aaa69d | -8.6887 | -46.3599 | 2025-09-18 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| c7894be8-0e60-3d2d-89ca-852ab3b44963 | -8.7076 | -46.3579 | 2025-09-18 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.3 |
| aa1d1998-24a6-3c2b-8598-126595d39f40 | -8.7073 | -46.3804 | 2025-09-18 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 256.6 |
| e110dbf5-d5cb-35dc-94f8-5582d0d64b1f | -16.2599 | -41.70402 | 2025-09-18 11:40:00 | TERRA_M-M | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 003f069f-5a41-3323-ae81-1071a1b663f2 | -17.64898 | -39.74424 | 2025-09-18 11:40:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 69eef2f1-15a6-34b5-82ef-5230ce708181 | -17.17279 | -45.91341 | 2025-09-18 11:40:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 2b970ee9-8f26-3740-90eb-b23b286ac968 | -18.39764 | -39.97982 | 2025-09-18 11:40:00 | TERRA_M-M | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c8d3f0d6-53b8-3a07-9adc-caa3e1c073f6 | -17.81811 | -45.34294 | 2025-09-18 11:40:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2c8b1202-bd02-3b9c-bb2f-d27f7e149ef1 | -17.81256 | -45.35526 | 2025-09-18 11:40:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 507657da-f719-3352-b634-6efe0df5efe0 | -19.73314 | -43.64109 | 2025-09-18 11:40:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6576aff7-1f0a-3965-aea2-adaaaf10229b | -16.11331 | -42.61843 | 2025-09-18 11:40:00 | TERRA_M-M | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f2f056e4-1b85-3c11-aed1-a382c6b32ac8 | -16.30924 | -42.03873 | 2025-09-18 11:40:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e1d6ebee-c76a-3010-b017-c5ce6befed96 | -21.88031 | -45.34469 | 2025-09-18 11:42:00 | TERRA_M-M | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 327c19f8-1326-395d-be42-d2db5eb88779 | -21.57553 | -44.00181 | 2025-09-18 11:42:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 375eb243-8f9a-3322-8751-b72dd2db2571 | -22.58641 | -42.05815 | 2025-09-18 11:42:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| e4903cc3-0d6c-33d4-b4bd-8eb5a968ceb9 | -20.96297 | -43.03521 | 2025-09-18 11:42:00 | TERRA_M-M | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| af2b9ca4-642d-348e-ae48-559a9a5a8100 | -8.7073 | -46.3804 | 2025-09-18 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 85930c51-0c2c-3ff6-9b34-5d5666d1e3e4 | -8.7076 | -46.3579 | 2025-09-18 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d39ad2e6-f2bc-34fa-b13a-181c2a9189d6 | -9.1901 | -46.9549 | 2025-09-18 11:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ac9420b5-6393-3a8c-943c-a307fa349a23 | -8.9725 | -46.2854 | 2025-09-18 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 17f426e1-0a42-377a-b100-618ed1bcd8c3 | -8.7076 | -46.3579 | 2025-09-18 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4586ce44-4180-3230-8e89-95ce38c3a7b0 | -8.9914 | -46.2834 | 2025-09-18 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9e888dc5-f0b8-3a74-8b12-bb5ab04d11b2 | -8.9911 | -46.3059 | 2025-09-18 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 175.5 |
| d9e8a613-3006-3ff7-a98d-64f46ccdb763 | -9.01 | -46.3039 | 2025-09-18 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 633b3905-afe3-3487-a9b9-8c83e3222d7c | -8.9722 | -46.3079 | 2025-09-18 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 776a9425-9d60-3182-840c-48b5e87c98e9 | -7.5162 | -45.3024 | 2025-09-18 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e363b16f-e690-38ca-bd3f-d5a2636b1db7 | -8.6887 | -46.3599 | 2025-09-18 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ef7b982b-d32f-3f03-9e1b-91fe55ee7d49 | -8.7073 | -46.3804 | 2025-09-18 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| f80474ac-0579-37b1-b126-689845a8ae31 | -9.1422 | -44.9057 | 2025-09-18 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6ab8edd8-4568-3acb-a72c-9ef63a91d8e3 | -8.7076 | -46.3579 | 2025-09-18 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 24eb9caf-664f-329b-b0c6-bfcfb26d7bc7 | -5.6233 | -45.41 | 2025-09-18 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 44a0f4e0-a287-38f8-9d77-df28561e19d4 | -7.5993 | -44.6102 | 2025-09-18 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 17e28c38-c942-3e93-af7c-f1c780b72b22 | -8.7073 | -46.3804 | 2025-09-18 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 283eef5f-88d7-36d4-aec6-a89a6e4bf2e1 | -8.9914 | -46.2834 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f7a3b167-89bf-3c84-b44c-c25b4dbda3bb | -8.9985 | -45.7418 | 2025-09-18 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 21c15701-802a-3b92-8675-4a142cea6f8e | -8.899 | -46.136 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fe7fc09a-ae3b-36d3-a953-0222656f16e1 | -7.5598 | -44.7743 | 2025-09-18 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d734a94b-f02c-366f-9f75-7699dd939453 | -8.9905 | -46.3508 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0907f2da-eac8-3e37-b798-22c9eedd9a8d | -8.7073 | -46.3804 | 2025-09-18 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 61a5b14f-7dba-3b41-826b-ef11a08efe1f | -8.7076 | -46.3579 | 2025-09-18 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b4c4d53a-73f6-3048-a42c-391b24bdb711 | -8.9725 | -46.2854 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f9d4245b-a80b-32a6-9a67-c4a26a55e299 | -8.9722 | -46.3079 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 61dd7b58-2978-3367-91e0-a0eaf65c8972 | -8.0281 | -44.957 | 2025-09-18 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| baa100fa-b92c-33aa-8a9c-45946a336582 | -9.01 | -46.3039 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| b4f40bee-70a6-3767-b996-cc825c8c57e7 | -8.9911 | -46.3059 | 2025-09-18 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 17681b4f-a623-3589-ae8c-f51bddfbc5ed | -8.6268 | -45.3054 | 2025-09-18 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 41bc39f1-e1f8-3e89-b548-c3cf67bddadc | -8.9796 | -45.7439 | 2025-09-18 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c1c59e60-5c8b-3f93-8339-13604c821ce2 | -8.7076 | -46.3579 | 2025-09-18 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 6371c8bb-6b3f-35f9-836c-efc873bdf4bc | -8.6885 | -46.3823 | 2025-09-18 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a405c93a-f995-3a3e-8bcc-f7eaf58ee9f1 | -7.5601 | -44.7514 | 2025-09-18 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5277d853-937f-3f99-abbd-5cdd8aad2866 | -7.5162 | -45.3024 | 2025-09-18 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 49535c37-6765-3d9a-a030-c419db8c840a | -7.5598 | -44.7743 | 2025-09-18 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |


[Clique aqui para ver as próximas entradas](README34.md)
