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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1424c69a-a53c-3d6b-b2a2-eb93c5de4e3b | -5.63644 | -43.72523 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50d37c4f-94bb-31ee-81c3-cc7a6b7a830d | -5.64305 | -43.71078 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bc88907a-dbfd-3fe2-ae11-cd59401b6ef8 | -6.06919 | -44.23646 | 2025-06-07 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7172c7ef-d206-3701-b075-d960fb856c57 | -6.37905 | -39.25362 | 2025-06-07 03:53:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d0fce90b-2e38-33e3-8593-c8e2d825e1f7 | -4.66881 | -41.9617 | 2025-06-07 03:53:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e61c8cab-e0ee-3874-84b7-2eb64dfff25f | -4.86009 | -37.60978 | 2025-06-07 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6008eb1e-eb33-3b62-8147-8f4cac6eca79 | -6.21622 | -43.32781 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cced1fd-05bd-32f7-a883-ed5e3cb2840b | -5.78265 | -43.61977 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab88a5e2-4ca5-3e94-a3c1-dfecf2641862 | -6.80795 | -41.73729 | 2025-06-07 03:53:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 177e99fa-66f6-3f14-b85d-be1fadc933dd | -5.77991 | -43.61552 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96491171-736c-3701-b86b-e69f36b7ce98 | -5.64244 | -43.71453 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| de32e1e8-cbe8-309f-8e10-c133be7bceb9 | -5.07128 | -37.71727 | 2025-06-07 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e63f8a4e-1e76-33c2-b331-f42adda97bb1 | -5.63891 | -43.71017 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57f7ce80-a0f6-397b-af1a-18e2bafd6a85 | -6.20824 | -43.32649 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2831290-96d8-3ef9-a42f-e3fb4f3b2370 | -5.78051 | -43.61185 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa1696d6-a168-37a4-b81e-1a1e384b7773 | -4.49585 | -40.63464 | 2025-06-07 03:53:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bc013cac-6129-3745-b8d2-5035efc2cd03 | -6.21224 | -43.3271 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 795c5884-6eac-303f-a900-86ba83c6fd3c | -6.20248 | -43.33646 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1b52eea8-8985-35af-b1ca-c3e41205bced | -6.20307 | -43.33292 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 75300197-c4cf-3451-9ce1-59db785d9433 | -5.6478 | -43.70768 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 03cbf1ec-e448-37db-aebf-507152dd3e35 | -6.29401 | -44.21737 | 2025-06-07 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0436c929-0bc2-3905-929d-ea1990984792 | -5.24345 | -36.20018 | 2025-06-07 03:53:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bdc7420d-9bea-360d-87c6-2f5783a34164 | -4.49648 | -40.63072 | 2025-06-07 03:53:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40b84102-b3aa-301e-9e92-538c41dc92e5 | -5.7828 | -43.62359 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9446fcb-2f9f-37cf-a91d-8e5381ed1de1 | -6.20366 | -43.32938 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5916d293-ba2a-3372-b7d3-33b69340b24f | -5.78202 | -43.62347 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f934657c-309b-31fd-a4a2-86596c84a2d1 | -6.21371 | -44.51159 | 2025-06-07 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac906ba5-46e0-3c10-b620-a3aec3c302ac | -5.77581 | -43.61486 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5963e88-0362-3f40-b7e5-c0367466d92b | -6.20423 | -43.32592 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 002a2806-b146-3708-93ff-fcf891d94783 | -5.63829 | -43.71392 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9d7984e-40f6-33fc-a23d-450e45246086 | -5.64121 | -43.72206 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a6ed721-6752-335e-8cb6-c72be681b7ae | -5.64058 | -43.72589 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e45702-9cd9-3129-ab51-6b13de64cab1 | -5.63768 | -43.71766 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f4ae8407-3c64-3e2b-b6af-c17ecba5fc93 | -6.21513 | -44.50322 | 2025-06-07 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 772c5a87-dcd4-3e89-bf55-49dd019d7458 | -6.20648 | -43.33708 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c30c12a-b1c4-3d64-b6c5-11668cf398ab | -5.64658 | -43.71515 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3d28720e-128c-3473-ba04-fde1434d7ba9 | -6.80726 | -41.7415 | 2025-06-07 03:53:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c4f58df-1beb-30b4-8d7b-04db5b5e3d2c | -5.64182 | -43.71829 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81110b24-af0b-3b90-97d6-737ed51e99ac | -6.19906 | -43.33231 | 2025-06-07 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d9bff22d-a52d-3ed7-97b5-03ebde7328ee | -5.6501 | -43.71956 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122ae1c5-75fa-32b4-be22-6c206ba509a4 | -5.63707 | -43.72141 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c3d62bec-9f5c-3f77-b647-e5eb311bd352 | -5.64596 | -43.71893 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d05df31-bf76-33da-b1de-2be0c39e1e30 | -5.64534 | -43.72272 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e79db770-9e9c-3d62-a12a-291df87f9cff | -5.04235 | -37.77269 | 2025-06-07 03:53:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2655aa93-2fd6-319c-8b92-09bec3409d8f | -5.64835 | -43.60104 | 2025-06-07 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d68e323-8009-34ac-92f1-9aeb4dfc18a1 | -5.64719 | -43.7114 | 2025-06-07 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 11ae581e-f9be-38f5-95c2-cfea6e05af07 | -7.85981 | -47.89881 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 711df5d8-047c-3441-b7e6-24c1ab1081c8 | -6.96923 | -42.91335 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e7c8f5a-5a23-30d1-a309-f7cabf5577c8 | -9.48924 | -40.31035 | 2025-06-07 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c53954a2-ce65-3795-a602-e9f7220354ce | -11.0213 | -45.23555 | 2025-06-07 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dcebb1c-81d0-3101-a9df-834bc889c51a | -8.7244 | -47.90219 | 2025-06-07 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 579f2d28-1a44-3f8d-b784-bd18f581d4d8 | -10.69711 | -37.04968 | 2025-06-07 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2dc1d1f-0f1a-3a37-8dc1-f2ca6cfa6a01 | -6.24243 | -48.55482 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 746c1d18-3f06-38ae-8632-0b3e3fe02833 | -7.01517 | -44.60766 | 2025-06-07 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e7fef1c-452a-3969-8730-7e3e4b6af9bb | -6.95996 | -42.92168 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00fe3598-1e97-3378-8344-1e309eaf0bfe | -8.17741 | -46.50298 | 2025-06-07 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 866cd9ca-0af6-370e-a0c5-6a54c9b4ce37 | -11.81988 | -44.25835 | 2025-06-07 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94337e58-5600-39d2-b7ce-53d0cd232a00 | -8.45057 | -46.49034 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14b20b61-9d8b-396b-aeb6-0554d5e9a8d8 | -12.38442 | -47.31781 | 2025-06-07 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ee9f11-a5d2-3418-a8df-ea868d737bb8 | -9.0719 | -47.14496 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7912ea14-59f2-369b-8059-8504491fbc5e | -11.77259 | -47.39453 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430de32f-a881-3019-b050-f7bfe474a0ab | -7.71783 | -44.17644 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8beae08c-f276-3eb2-910a-53ee4d540362 | -12.2759 | -44.6062 | 2025-06-07 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60d89c66-6f15-3b74-9635-91d8e790f2a1 | -13.33952 | -45.4842 | 2025-06-07 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c38b2a29-6100-314d-9066-192537dfbc27 | -6.94692 | -42.90487 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 766282dd-1fd3-3fa9-8f44-2c6fd65fd1b2 | -7.74026 | -44.16894 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1f085861-25a1-3ab0-b9f6-db0cbc28ab08 | -6.19617 | -48.53804 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cf98547-3608-31f2-8aab-541df3fe8195 | -6.23678 | -48.55373 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63182fe2-ebc3-3971-a4ee-84f2bb0ff7f0 | -11.90522 | -44.87537 | 2025-06-07 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40b99543-c7d6-3a57-8601-1a0bc27fba88 | -7.73494 | -44.17545 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e658860e-fe5c-3fbb-aded-de15ce3719d4 | -6.96618 | -42.90789 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2b206dc3-1aa4-3564-a5f6-43c749a6f3bf | -9.07681 | -47.14586 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73370068-18f0-3515-a4fc-5a634c51d73b | -7.72195 | -44.17711 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9769cd38-1295-3115-829b-185ffb1200e5 | -12.86295 | -38.36781 | 2025-06-07 03:55:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 776a967b-d2f8-3c64-a786-f682bb4d3e77 | -8.17264 | -46.50206 | 2025-06-07 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b67464f-6905-3ead-ad06-e9bd9e44a3d7 | -13.66151 | -47.70613 | 2025-06-07 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d85f679f-8ba6-3306-a465-337dcd1401fa | -7.73368 | -44.18294 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 05990d19-6fce-3f45-a93e-9ee46b7b4741 | -7.73556 | -44.17172 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0ac2caae-898d-371a-b002-1e729389339a | -7.72069 | -44.18462 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9a57deb-ffe9-3630-8118-64ced287f56d | -6.96696 | -42.90309 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 936da9a1-e1b8-3708-8d94-4d8e5303c41f | -7.72097 | -44.15777 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b4f644-e32d-3c4f-82bc-a8ba3875d1c2 | -7.73206 | -44.16732 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be4f780a-c885-3aab-b1d4-9c375ab6a8c4 | -7.71656 | -44.18394 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e42d96c9-7857-3c30-9bb0-c7cc1a48221b | -7.71497 | -44.16828 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6a14e38c-d0b9-318b-8754-a19812462191 | -6.96312 | -42.90246 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 251aebe1-da04-3908-b5e9-de9e31ae690e | -12.27898 | -50.10304 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91b059e4-a235-38e9-ba34-ffd9aad50ce9 | -6.94919 | -42.91507 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4b5b9195-da87-3829-a0f6-affe0532d342 | -9.55067 | -47.77225 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a27e9ddf-a927-30d8-9949-b70eb1f16c0b | -6.24035 | -48.55261 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b0b7ce98-50ee-3be5-8c18-9ebf0be2fa71 | -7.72733 | -44.1703 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1cc70021-a4b5-3a28-acf5-dfa60e98dd09 | -11.78113 | -47.40165 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3696d33c-64be-3b61-9d78-5b8bc4a55a12 | -6.96076 | -42.91685 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d105a62c-cef5-3839-84f8-290859f05754 | -7.73966 | -44.17255 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5ddc6cda-2a06-3da0-9b2b-296b98591547 | -6.2354 | -48.54753 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7ff666d-a0db-315f-8fe3-0df5bb75a644 | -9.07086 | -47.15061 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b7ac5c53-12a8-3bf1-ab4e-4aaae34cbf7a | -12.29178 | -50.09745 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 85b75ac5-54e7-36f3-873c-26280190f226 | -6.96006 | -42.89704 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91b07ec0-c4d7-3159-a0e5-ddc8379fa0c1 | -9.50127 | -47.39333 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b273b472-d244-3435-830f-0defa15df0dc | -7.72258 | -44.17336 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f1cd4662-cc94-3fae-afee-04d25631f916 | -9.40501 | -48.44068 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README8.md)
