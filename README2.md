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
| 009839a8-1130-38f1-b211-4b339bdab100 | -7.83863 | -35.20342 | 2025-01-31 04:01:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a003a9a4-29fb-32f3-9d09-84966660712f | -11.55126 | -37.79678 | 2025-01-31 04:01:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 13130d8e-db7b-3002-8c25-07837799cd93 | -9.5629 | -35.69275 | 2025-01-31 04:01:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee592c45-bd53-3d17-a0aa-b822a5fcd517 | -9.43421 | -35.55627 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6b5594c2-2893-3717-997d-915be9920976 | -9.43277 | -35.55538 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| fd3a43d2-ac6d-36f2-a069-56649d661107 | -11.62074 | -37.72418 | 2025-01-31 04:01:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aecd66a3-25c6-3fd3-aa57-06807f89e80f | -5.39341 | -36.78476 | 2025-01-31 04:01:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6fda029e-a9d8-3b76-ae17-06c4a02ec528 | -9.43636 | -35.55964 | 2025-01-31 04:01:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 27c423ec-bcc0-3ad7-aa85-d085a8d99299 | -7.35273 | -35.21462 | 2025-01-31 04:01:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ae59c69-d1ca-3b0e-ab8a-f564c5e45f7d | -7.84272 | -35.20411 | 2025-01-31 04:01:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 1f75daee-8759-319e-bda2-3e689673aa8e | -5.00588 | -37.30034 | 2025-01-31 04:01:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ab663187-5ce5-35bd-a327-07ab0c04e952 | -6.35229 | -43.37594 | 2025-01-31 04:01:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3783ecc4-df31-35f5-b127-776ee47c15b8 | -12.64643 | -43.81976 | 2025-01-31 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c2c2007-7360-39f8-acba-fb153378e8e7 | -13.92094 | -41.80046 | 2025-01-31 04:04:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f21b49bd-4925-3dc8-85dc-b67c3ab5c845 | -12.4077 | -38.86123 | 2025-01-31 04:04:00 | NPP-375D | SÃO GONÇALO DOS CAMPOS | BAHIA | Brasil | 2929305 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4dab7be-86e4-363f-8ef4-6136e350721b | -17.80037 | -40.16458 | 2025-01-31 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 707d94f2-57fb-3224-a7a0-a4d6988f392b | -17.79625 | -40.1681 | 2025-01-31 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e354d2b2-c9eb-3a0e-8b5f-1e5bf90abb0e | -17.50792 | -39.27321 | 2025-01-31 04:04:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b3984655-c250-3473-ad2a-5f01d9919eec | -13.92427 | -41.80101 | 2025-01-31 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4f445aa-da2d-3aa8-b6d9-865fac76db7a | -14.46411 | -43.35256 | 2025-01-31 04:04:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4bf704bd-a1f3-3a43-bddc-ea4d910588d1 | -16.07447 | -43.63325 | 2025-01-31 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6b4918e-2816-3088-87c9-6de017b35df5 | -14.72355 | -39.3723 | 2025-01-31 04:04:00 | NPP-375D | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d190c57-6e19-3359-8b89-c06c3b97a525 | -17.79685 | -40.16402 | 2025-01-31 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a070e167-f6cf-3107-824b-71a4e23f3d02 | -17.06808 | -39.42313 | 2025-01-31 04:04:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1a53458c-5ed4-3659-b0da-ea7485266952 | -17.50861 | -39.27563 | 2025-01-31 04:04:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 325bb23e-d2fd-3bdd-9e10-603ef0190568 | -16.0361 | -42.1339 | 2025-01-31 04:04:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cb79b281-63b1-33ed-ac35-bcb78a41671e | -16.03942 | -42.13446 | 2025-01-31 04:04:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05056c7b-71d5-3ce2-baa1-194c6ddcd304 | -15.44928 | -41.69071 | 2025-01-31 04:04:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| acc48bd9-3dbc-34fd-a9c5-37c6d0723a76 | -13.97372 | -38.94881 | 2025-01-31 04:04:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3341e7d5-1845-3e4e-8609-d3af62a2a83d | -12.86166 | -38.36802 | 2025-01-31 04:04:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5f3ed639-ca12-35ca-9f11-b6e66788f1f1 | -16.84379 | -39.17207 | 2025-01-31 04:04:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b37ec6c6-aea0-3c16-b297-e590b3c4c02d | -13.4797 | -44.02205 | 2025-01-31 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f35d51-d290-3800-9990-008a141efd41 | -13.48035 | -44.01814 | 2025-01-31 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6acc7518-5de7-3aac-850c-9b2196aa23ed | -20.3475 | -40.36126 | 2025-01-31 04:06:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac1d84fc-1b64-37b7-b385-caeffdbf54fc | -21.29439 | -55.90528 | 2025-01-31 04:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79db237e-b535-32c0-8159-06d4b68cb354 | -19.83712 | -40.08266 | 2025-01-31 04:06:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 276c3a52-9d5d-300e-b458-44b1e255d3de | -20.35108 | -40.36184 | 2025-01-31 04:06:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4858932-c840-3959-ab82-7a771d5f0ff2 | -29.10135 | -51.11757 | 2025-01-31 04:08:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5c1a5e2e-2a90-3497-85f0-c5116265bc29 | -29.10244 | -51.11874 | 2025-01-31 04:08:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6e5f6431-702b-365a-bec8-8d546b7a1cba | -6.42318 | -40.0213 | 2025-01-31 04:23:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fd55a00-c4b4-3e3b-88cf-67b29d9bc93a | -6.32298 | -43.73793 | 2025-01-31 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f0bf2a7-0116-3f51-b348-97c41c6463e4 | -7.83911 | -35.20509 | 2025-01-31 04:23:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 86efa8d6-94fd-3957-9f97-5f45848c4993 | -7.17457 | -44.98878 | 2025-01-31 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd80af7-3159-3164-97d8-4ac335f0a152 | -7.83975 | -35.20014 | 2025-01-31 04:23:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a41db279-f12f-3a35-b51c-351235653cb2 | -7.84133 | -35.19853 | 2025-01-31 04:23:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0b296a2f-d34e-3482-93b8-5025783f65ee | -7.84067 | -35.20346 | 2025-01-31 04:23:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 2d8a8be3-1cd1-386f-b5b3-d6b561167144 | -13.48026 | -44.0197 | 2025-01-31 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88c660f7-e355-31be-a14f-7a03bd3f2753 | -13.92219 | -41.79866 | 2025-01-31 04:25:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6795a210-0a42-3c66-97c6-79ce3a733a1a | -9.43511 | -35.55499 | 2025-01-31 04:25:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 19eeac81-50f3-38bc-b37d-06bd183b59b2 | -2.58605 | -51.9206 | 2025-01-31 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34c52398-e2a0-3e88-b1b0-189d3f6fe6f6 | -9.43449 | -35.55986 | 2025-01-31 04:25:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 68108956-ec70-3bfb-bc25-665caac3af82 | -9.37727 | -35.76657 | 2025-01-31 04:25:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 895764db-6e3c-3f98-bfd2-e1413e8cdf8a | -11.25795 | -44.49023 | 2025-01-31 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3179d5c6-3d36-3f56-afc9-3fddada6d6a5 | -9.37786 | -35.76188 | 2025-01-31 04:25:00 | NOAA-20 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e4cfac24-edcf-3dd4-8ff8-cf37b56129b6 | -2.92842 | -48.23938 | 2025-01-31 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 925ad8f6-d064-3533-93f6-5c32040a75f1 | -13.92337 | -41.80114 | 2025-01-31 04:25:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d3f026a-4282-3bf6-a4b2-edc31ba80e50 | -11.25856 | -44.48611 | 2025-01-31 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734233d6-a3ec-32bd-b9f3-b21208bf36a3 | -2.92489 | -48.23882 | 2025-01-31 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6a95c23-c930-3f51-abd8-7102a06bc8d8 | -11.45368 | -52.92773 | 2025-01-31 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66b5f8aa-7864-3894-8eaf-fa032e819fdc | -13.92157 | -41.8032 | 2025-01-31 04:25:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 273bfd04-202b-3b08-b739-088137615390 | -2.58089 | -51.92432 | 2025-01-31 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c54238f-462a-3a35-a560-88b62df5d91a | -11.54778 | -37.79551 | 2025-01-31 04:25:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d8f8035c-9523-3504-8bd5-7a34d19d1ece | -3.82942 | -41.56357 | 2025-01-31 04:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 965bb4bf-33f5-332e-b650-9e7b69b1d5c5 | -11.55327 | -37.79643 | 2025-01-31 04:25:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d97b2999-dcd2-3719-8fdc-c1ea40a03960 | -16.68163 | -43.88488 | 2025-01-31 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dc75eee-86c0-3eff-9f77-3067510aa08d | -16.27404 | -56.79106 | 2025-01-31 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2f67484-dff5-346e-9312-95653c10b86b | -16.27999 | -56.78658 | 2025-01-31 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a2c71c77-fbb6-3a97-847d-304d6621ec03 | -19.02164 | -57.62142 | 2025-01-31 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0583045b-842a-3ef1-947d-41951d6b35c6 | -20.54565 | -55.8414 | 2025-01-31 04:27:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| def731f8-8fc0-3e96-bc34-09b8daeead09 | -18.99085 | -57.66227 | 2025-01-31 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2b837770-3683-3c11-9622-8b2aef1aa2bb | -16.27889 | -56.79208 | 2025-01-31 04:27:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 156d3188-ddc1-31d1-9bb2-396f118312c7 | -17.06914 | -39.42374 | 2025-01-31 04:27:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8ebe342-9bd9-369d-952a-b7c7a8bd34fc | -24.24207 | -50.73977 | 2025-01-31 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea7fa4de-2355-3acc-be10-a2e95ada88d2 | -23.47992 | -55.15044 | 2025-01-31 04:29:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94dce3f6-0f40-3e5c-974b-6a354a3216f8 | -32.11285 | -53.27534 | 2025-01-31 04:31:00 | NOAA-20 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| cac50e69-a0f5-3990-89dc-a5c59c9376c3 | -30.15001 | -52.02605 | 2025-01-31 04:31:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a3e084c0-f7d2-3a8c-8ca4-73e37076716a | -30.39362 | -54.25397 | 2025-01-31 04:31:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 35f5ab55-dba4-324b-921a-b9673ab32f96 | -29.86508 | -51.16451 | 2025-01-31 04:31:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 8b3e0cf0-2fab-3284-a45c-e228df62e636 | -29.95156 | -51.61754 | 2025-01-31 04:31:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 354eae49-bce9-3e9d-9f5e-95f81bf4533f | -29.73622 | -52.44896 | 2025-01-31 04:31:00 | NOAA-20 | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 49b20f11-69d9-3d75-bf4e-061e54625a57 | 1.42844 | -60.7999 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d378509-0c86-3b4a-9f9a-318264ea1b40 | 1.42297 | -59.95113 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 68c0d0cf-4dc5-3d23-a671-04f6f95e597d | 1.42234 | -59.9471 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c8e0879-5f34-3f0f-a1ec-1d213d76c58e | 1.4236 | -59.95515 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 359a9c32-be1d-363d-abfe-98e946ca1ebf | 1.42651 | -59.95058 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 45a9c943-137d-3bcb-acad-ef86eb6cedac | 1.42005 | -59.95569 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d2f73c0-cb37-3115-b4ca-182e377e88b7 | 1.41942 | -59.95167 | 2025-01-31 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d669c9c-575e-3092-9d1f-9e2aeb420995 | -6.51598 | -47.59454 | 2025-01-31 05:16:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6eb8d65-cfc9-3feb-adc1-9a3279248fb4 | -11.6636 | -58.26333 | 2025-01-31 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d9b2396-a4fd-3b97-a81a-5dcdbb000bf4 | 1.4134 | -59.9504 | 2025-01-31 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c46871ff-7c78-3ad2-8a40-036953d307f7 | -16.11088 | -58.20066 | 2025-01-31 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 27136bb3-c3f7-32af-8c77-da5065285c39 | -20.55006 | -55.84227 | 2025-01-31 05:20:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a286ee4a-42e4-374c-830e-699c95e00c11 | -20.54576 | -55.84171 | 2025-01-31 05:20:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3177d48a-baf6-3f76-a867-0fb4dd849aeb | -15.9582 | -57.94781 | 2025-01-31 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 55bce08d-44d0-3b1b-bba9-f81b60f97214 | -16.28205 | -56.79042 | 2025-01-31 05:20:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4ddd82ec-798d-3dd7-aa39-b7d31758bdcb | -16.27822 | -56.78987 | 2025-01-31 05:20:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f14066c6-9ea0-35c8-8b49-2b7015e7d5aa | -23.48094 | -55.15138 | 2025-01-31 05:22:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f62d0041-8013-3b89-b865-e24aa073a0a6 | -30.39595 | -54.25303 | 2025-01-31 05:25:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6a7ca67e-1499-3255-bcff-14dd66651226 | 4.22155 | -60.59581 | 2025-01-31 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16569e45-084d-3d5f-a8c3-bf1bf4a3e0c3 | 1.42449 | -59.95404 | 2025-01-31 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README3.md)
