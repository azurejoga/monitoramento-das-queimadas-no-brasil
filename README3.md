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
| 2db669d2-8b09-3dd5-8a22-07cf5f8556f6 | -12.5531 | -45.0174 | 2026-06-20 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 8b1ae9d8-c013-33f7-af4f-3d0cba232177 | -9.0339 | -63.5593 | 2026-06-20 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| baf31797-a6fa-35e9-9f49-91569e82b1a2 | -12.5531 | -45.0174 | 2026-06-20 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| aac19725-1412-3409-835b-f446013640b6 | -9.034 | -63.5404 | 2026-06-20 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9d264b0d-9c9d-3e1c-aa2f-116892dbfbb0 | -9.0155 | -63.5411 | 2026-06-20 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 79bc145e-7cce-3f97-b3d0-cf757b285b2a | -12.5339 | -45.0204 | 2026-06-20 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d1f22525-81e5-3f04-a6a4-08cbc6e40239 | -13.2066 | -50.3492 | 2026-06-20 01:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 25563250-4398-35e3-a2fd-2d480a71e130 | -9.0154 | -63.56 | 2026-06-20 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d8888039-4a5c-3d7c-917b-82257dc7e882 | -13.2066 | -50.3492 | 2026-06-20 01:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f4cd25f8-d9b9-3fb4-a626-ec2e0e7192e2 | -9.0155 | -63.5411 | 2026-06-20 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6d57986a-a1b2-3044-856b-c1abe0396359 | -9.0154 | -63.56 | 2026-06-20 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 47fc03ea-41ec-3381-8931-4abf6cf9cd6b | -9.034 | -63.5404 | 2026-06-20 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 80fa63c4-e861-32a4-85d1-76e5492071b5 | -8.6526 | -47.7602 | 2026-06-20 01:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b60313c8-9a7e-3959-881b-debf456cdf15 | -12.5531 | -45.0174 | 2026-06-20 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| eafced72-09a1-35df-a56a-22d34551b6e1 | -9.0155 | -63.5411 | 2026-06-20 01:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 707dedd7-865a-3e60-bb8a-7f6faa5c1203 | -12.5531 | -45.0174 | 2026-06-20 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 13aa54e3-498c-38ec-ad3a-77b447d5434e | -9.0154 | -63.56 | 2026-06-20 01:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b7089026-4a05-31ee-ba35-81c690d89188 | -13.2066 | -50.3492 | 2026-06-20 01:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3123df7e-39e5-3ea6-a78d-1622bbbc1788 | -9.034 | -63.5404 | 2026-06-20 01:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| e689f857-0be9-315b-a648-c5d9070a019d | -12.5531 | -45.0174 | 2026-06-20 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2273f359-47cb-37ad-a761-c9d58cc5e7f3 | -9.0154 | -63.56 | 2026-06-20 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ad795940-f3ae-3306-9880-1ee9192ceb35 | -9.0155 | -63.5411 | 2026-06-20 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9316bfc6-b8c2-306c-a254-ce9b2df36d1c | -13.2066 | -50.3492 | 2026-06-20 02:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 4ee6ed95-bd73-3fe1-b68d-789428c2e7c3 | -14.091 | -59.4569 | 2026-06-20 02:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 95ce1ab3-3153-3f95-b296-444868315657 | -12.5531 | -45.0174 | 2026-06-20 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0ab80b19-5acf-3aea-96b2-fbecd4b1b374 | -9.0155 | -63.5411 | 2026-06-20 02:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 437881be-0c36-3e4f-b008-92536e7f104b | -13.3988 | -42.3817 | 2026-06-20 02:20:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 48.3 |
| b3ac15dd-0d9b-31ba-8d96-d72784fb417e | -12.5531 | -45.0174 | 2026-06-20 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 2568dece-9150-3c1c-86e8-758af1502244 | -9.0155 | -63.5411 | 2026-06-20 02:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| dd012e11-4591-3a7a-afb1-4d2b713e484f | -14.091 | -59.4569 | 2026-06-20 02:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 91704b33-ea11-381c-add9-f68eb6d694eb | -12.5531 | -45.0174 | 2026-06-20 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 725bafac-9d5a-30e2-806c-ae1deb1d1dbc | -12.5339 | -45.0204 | 2026-06-20 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6917c018-03f9-3382-84e7-6349551aa553 | -12.5531 | -45.0174 | 2026-06-20 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c120e1ce-bea4-3186-8dfa-7285a107f3d9 | -9.5534 | -40.3254 | 2026-06-20 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 9b83398b-24ee-3799-8183-a988b5b0813e | -9.5343 | -40.3282 | 2026-06-20 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| acdc8a23-2e8d-3a80-82e8-ca957898d2d4 | -12.5531 | -45.0174 | 2026-06-20 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a2dcf3d3-3905-3d93-bd2e-d2d1a05bbcc5 | -12.5531 | -45.0174 | 2026-06-20 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 2c866d78-0f4a-34c3-8f7d-04b917ff2904 | -17.69267 | -40.1736 | 2026-06-20 03:06:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| dc3550fc-042f-3d1e-96fb-978ada892e52 | -17.69443 | -40.16624 | 2026-06-20 03:06:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 463e8959-c7c6-34ad-a39f-44f031893ac8 | -17.70157 | -40.16806 | 2026-06-20 03:06:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a530ae5-afcc-3e91-8882-68893caf97bf | -12.5531 | -45.0174 | 2026-06-20 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4f512f30-dc26-3f65-a1e3-316d3fbce1a6 | -13.1336 | -53.7833 | 2026-06-20 03:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1c62c915-9461-3d6a-9578-8fa42537cdf6 | -12.5531 | -45.0174 | 2026-06-20 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 41d28935-c7fb-327b-b79f-d10cc3367726 | -11.89128 | -43.83754 | 2026-06-20 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6995017-89aa-32ec-bdb4-eba236220e8e | -13.3852 | -42.3879 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 321c45f1-cb18-31b9-bb1d-a84de39d2ab7 | -13.38417 | -42.3928 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 2a63dbf7-cd24-39a2-9daa-75be261bafe3 | -11.89272 | -43.83084 | 2026-06-20 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0309be8-d872-32af-a1e9-7bf82ea3231d | -11.88581 | -43.83311 | 2026-06-20 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0660be4d-40a8-372a-be24-ead74a8ae806 | -11.8844 | -43.83603 | 2026-06-20 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f61c96e6-5b28-3b2d-ad60-aa8450b71074 | -11.89269 | -43.83464 | 2026-06-20 03:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e17d251-d351-31c8-a2a8-c97e99a23e4a | -13.38645 | -42.39005 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 2df346c6-c2bd-32c4-ab6b-b017ee0d0012 | -9.01385 | -40.9856 | 2026-06-20 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8797fef-0f63-310c-ab99-5d6cb8ca6fc0 | -13.38545 | -42.39496 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 2e6b205e-5443-3e51-b7e9-5edd3f47999f | -13.37923 | -42.39378 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| cf768b83-d952-322e-b0f0-ea9b7c03435e | -9.01292 | -40.99035 | 2026-06-20 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fc10272-450b-3574-a2b5-4fd96db55178 | -13.38024 | -42.38889 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| fd4a2f58-b053-3a09-b5ea-7cf64b241242 | -13.38314 | -42.39767 | 2026-06-20 03:21:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| d8bd2444-9d6b-3c2c-a0ad-eed97fb6f627 | -17.35002 | -42.62304 | 2026-06-20 03:23:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1318aae9-3de4-3c17-a153-0849bd3580ee | -17.69753 | -40.16248 | 2026-06-20 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b88dce85-818b-326a-824e-b9746dc9eeea | -17.69691 | -40.16552 | 2026-06-20 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 41809adc-8325-3398-98fd-5d90bbc9cc22 | -17.69254 | -40.16146 | 2026-06-20 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f35d106f-1a03-388a-a6e0-7d26ed264dea | -17.69315 | -40.15848 | 2026-06-20 03:23:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6aec15cb-c99a-35f3-9c44-b5d0ca93cee8 | -17.35114 | -42.62543 | 2026-06-20 03:23:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 27cdb725-e4b4-3b67-9a2e-585465f3753b | -17.34908 | -42.6273 | 2026-06-20 03:23:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ff2f2d2-14d5-3eac-bf72-323a87429e3b | -22.85619 | -43.37758 | 2026-06-20 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b9511cb8-1921-3196-a742-a854b9fd6fae | -12.5531 | -45.0174 | 2026-06-20 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| bf4d51e6-bc87-3369-ae5c-936a53a4675c | -12.5339 | -45.0204 | 2026-06-20 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 59408af5-c1bb-3b56-9205-d85ea7d01154 | -13.3794 | -42.3854 | 2026-06-20 03:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 51.3 |
| a9dd0ecf-c2d7-3ec5-923f-887927a71071 | -12.5531 | -45.0174 | 2026-06-20 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5703aac2-4370-3f96-b755-67d1a85267d1 | -12.5339 | -45.0204 | 2026-06-20 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 2e2d74e4-40eb-375f-a472-defe81b866b6 | -12.5531 | -45.0174 | 2026-06-20 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| be346242-66a6-3511-abe3-0b3db94cf5c8 | -12.5531 | -45.0174 | 2026-06-20 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c9aae99f-6da8-37c8-8b81-07c04870b7cf | -12.5339 | -45.0204 | 2026-06-20 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 22e78ce6-7084-3597-8091-4d2cf355ea15 | -3.86457 | -42.96542 | 2026-06-20 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04552e55-8645-3aa7-8d36-20e3650e46d2 | -3.86801 | -42.96595 | 2026-06-20 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c32cbc7-4cb6-3d04-979e-4460f7c71b90 | -3.86517 | -42.96167 | 2026-06-20 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b720ad1b-6623-3146-a2b0-529217c24435 | -3.86861 | -42.9622 | 2026-06-20 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 187e1ff1-cfa3-37ef-9cc4-64d9f8187d7f | -5.81632 | -45.07013 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c44e0565-314a-3005-ba02-5dcabfeb5b2e | -8.68629 | -48.30936 | 2026-06-20 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95b4d7dd-92dc-393e-84ce-81c36c67bd74 | -10.60053 | -44.32454 | 2026-06-20 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9d742e1-452d-32f4-b53e-56cc43c42dfc | -6.3613 | -43.59177 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ef2d014-75e1-3ef7-b84e-67c86808ea99 | -9.7211 | -48.8849 | 2026-06-20 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c66b2bb8-d2fd-3432-b504-7fe48a395b6f | -11.03532 | -45.07676 | 2026-06-20 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c604e874-ef07-3a7f-acb2-387095eb695a | -6.37162 | -43.59351 | 2026-06-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 86865ada-c873-3d5d-8221-5707c3ace544 | -8.07948 | -46.24157 | 2026-06-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f87e9233-5700-333f-a27b-124206ec955c | -10.50661 | -45.26096 | 2026-06-20 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11e255a8-2850-32e7-89cb-e55ae77eae40 | -8.64962 | -47.76656 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1eeb8f41-1fcb-3957-bcaa-1d9e9681dae5 | -6.99485 | -42.76834 | 2026-06-20 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7aad0dc-97a4-391c-8ff7-921c555d2ff0 | -4.05889 | -43.24452 | 2026-06-20 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecd9cb40-c1e2-3425-87bb-7be44b55f7e7 | -6.32556 | -48.42183 | 2026-06-20 04:08:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4148e538-b4ef-3f54-b11d-f645512f6a53 | -9.72191 | -48.88039 | 2026-06-20 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c715fed8-4a6b-35eb-af5b-2dc0cf6a7675 | -6.99207 | -42.76425 | 2026-06-20 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cebd5120-a826-3926-b85e-3d641d712cdc | -4.0548 | -43.2478 | 2026-06-20 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0485f4bd-af0d-3459-a708-f37d660a8c4b | -11.19779 | -46.56762 | 2026-06-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3535ab40-0b93-3695-8078-762044a7ebdf | -5.81111 | -45.07846 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a25b0dba-ef3d-3c41-bd0c-74d77002c6b6 | -6.50291 | -42.22066 | 2026-06-20 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5c8530c9-0929-323e-8d77-e6c062e76762 | -5.81037 | -45.08296 | 2026-06-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 921a6f41-4e6a-3e9d-9c06-ba09f8971368 | -10.46819 | -49.09286 | 2026-06-20 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c33ed03c-3af1-324b-a7f4-c98981157b0e | -5.80021 | -43.79635 | 2026-06-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3401e096-a1a4-3826-89a0-0c72ff783793 | -8.65031 | -47.7626 | 2026-06-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README4.md)
