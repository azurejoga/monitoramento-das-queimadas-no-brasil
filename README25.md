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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50fda121-b413-3906-82e4-b134a5c3b2b3 | -10.16093 | -45.42207 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aec3d4b-5ee9-3f58-a702-e5ef11f874f0 | -6.99099 | -42.86295 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 500c6b13-f9ad-3fe0-855e-4ce0d8684455 | -10.74591 | -50.48102 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f93be4ab-663a-302b-894e-af463412f62f | -4.87475 | -50.89764 | 2025-10-07 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0c38527-0572-31c6-ab99-6f78850be950 | -9.9229 | -49.96276 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5350c429-700e-3ed6-a95f-2c00c2e88257 | -11.8869 | -44.95825 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd19385d-038d-30bc-9eca-b425e28681f9 | -8.84545 | -46.09972 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c249bbd-8902-3dd9-a2e7-aecda9ebcc25 | -11.12427 | -47.22083 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8895426-310d-3a31-bfb6-b315b5e32cf8 | -8.60687 | -44.9131 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a067b320-4226-34c7-ae12-c41df46116d5 | -11.94724 | -46.42314 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c039ca0-140e-33c4-bff4-a9390e816de4 | -6.28712 | -42.94057 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0d51bdd-e4cf-319d-9a91-7d5c63106ed6 | -5.21648 | -43.67571 | 2025-10-07 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbeabebd-ff6c-3282-9124-92fcf25f268c | -10.45341 | -50.40901 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7cceb3b-e70d-3f58-bd84-5361fc3f7113 | -8.27706 | -43.82932 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e622e3c8-8195-3c41-91c1-76da1d54f9a5 | -5.25556 | -46.56672 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0748db1f-b382-34de-894d-e099fc59bc73 | -8.88027 | -47.66306 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f50532e8-1608-39af-a5a3-35805448fabc | -8.55341 | -46.26147 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9a0a2ff-bb9b-3181-bc1e-7ecd085f511c | -8.54622 | -46.26187 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f296434d-332e-35b2-908c-b5fdecd787d6 | -11.47683 | -43.49154 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f66d8047-d462-3a61-b11c-82b99415901c | -10.72577 | -44.923 | 2025-10-07 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14312fee-6aa0-3f0b-87d6-b9b9ba62d794 | -6.39328 | -43.59093 | 2025-10-07 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb6243c5-e950-313e-bbe9-990a163308aa | -8.60333 | -44.91251 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b65ff03b-7010-3e2f-a057-ece70b8c212b | -8.18843 | -44.11772 | 2025-10-07 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 651040a6-f0f9-3af0-a28b-9ad33a21ca30 | -6.23989 | -43.25623 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c05d3a72-2804-3f36-b72e-0615f74d2761 | -7.70567 | -42.3917 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41d2045f-350c-3534-a783-69b0c907de21 | -8.17848 | -50.29773 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5415bc41-c255-309d-aece-a2cb498ea294 | -5.42257 | -46.00274 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 523a8851-3e9c-38c4-bf50-3e0e09048d37 | -8.58123 | -46.23607 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c71817c0-5240-383e-8347-99b1e42d1ddd | -6.23871 | -43.26351 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8381d278-57ea-3359-a4e4-aedde3363662 | -5.80013 | -45.21285 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bac9293b-1d00-3692-8f8a-3939eea1a9cd | -11.95586 | -45.49061 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5359db7-85e3-3bfa-a556-07b696ad78fb | -11.12899 | -47.21674 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ad7878b-cb25-3238-a8b6-10d21728dc1b | -9.03506 | -50.58529 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00f02ac4-df83-36a2-992a-3c86ec20bb99 | -10.25195 | -44.3771 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20ba93e0-7fd4-3303-8b0e-31305c90d5e3 | -11.0991 | -47.19912 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 136263f7-2c1c-3fd6-9317-20ccc86fe46b | -6.29048 | -42.94111 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3bde300-9bf1-35a3-9ad2-bee84925dfa2 | -11.2372 | -47.77011 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37473a05-82da-3c14-8e49-5d47d891d902 | -5.63877 | -45.96079 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 994e9e9e-ef35-3948-8203-db3873d62966 | -12.24139 | -43.77776 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a90b54c9-b339-384a-8b24-6483fb87e4cd | -12.24203 | -47.0205 | 2025-10-07 04:08:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7452ae6b-afb8-3ec2-b1d4-afc421a0ceed | -11.8813 | -44.94933 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc8d139c-a054-3f1c-a5eb-1630db6f938b | -11.23613 | -47.76871 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6b63869-a3b5-3778-97db-f0e8dc8b9525 | -5.55765 | -42.66793 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f5cdda11-72e0-3eed-b607-29ee1c52a00a | -6.75383 | -42.23223 | 2025-10-07 04:08:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4b4b0d2f-730a-390b-805e-a2744b388575 | -6.46273 | -44.58935 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4251e0eb-3710-37c7-a620-9b6873b71e80 | -8.95328 | -44.59823 | 2025-10-07 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2361331-7ac5-303a-90ab-c029b5057686 | -8.88855 | -47.6645 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 889db6c1-ac6a-300c-ba4c-867ae5f1e7b1 | -7.02174 | -42.75538 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 232a554d-bd71-34b3-8e0b-f28acc8be51d | -7.68584 | -42.40999 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| bef6a9b5-cedb-3693-8d10-4d7ebec35702 | -12.61667 | -44.74988 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5881c59a-357e-3e29-b089-53e733cce0cd | -9.00846 | -49.21187 | 2025-10-07 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 723b5af1-5b1b-320a-b1c3-c728e0520025 | -8.41732 | -50.69695 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd319de2-0537-356d-bd3c-cff2c3278bb4 | -8.10823 | -55.08409 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8b1673f-36e2-39c5-8659-2b66a922a2c8 | -10.9546 | -51.18455 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d55cfd89-0987-32af-a2d9-c130fc4fe20f | -7.52475 | -49.91224 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3637e986-a21b-3fc6-a5af-69c2fb8bae01 | -8.84843 | -46.10498 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25f9158f-7ba8-3ef7-b861-27a402e1895a | -9.51645 | -51.35926 | 2025-10-07 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 452d6d7d-5441-3979-849a-7d9638d7d257 | -6.01725 | -40.30207 | 2025-10-07 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d279a1d-18bd-3940-9868-dde78e127547 | -6.23813 | -43.26716 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a639f6e0-b0ae-33a8-a117-1d9da4e0c04d | -7.00772 | -42.84381 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 01afe8ff-4f10-3b30-ac30-f3d1491d1acf | -6.7022 | -42.86048 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d9cd77cc-38e7-305e-9445-b213303745f2 | -8.87742 | -46.69746 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b1c08c98-9812-3151-bece-823ab58eb7a5 | -4.77488 | -45.32379 | 2025-10-07 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfb7565-8b4c-35cb-b10e-2788ffbac1c0 | -7.42105 | -41.1199 | 2025-10-07 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e9e360c9-09a9-3506-8dc6-adaa46403e7b | -5.4607 | -42.89531 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d650ad00-a19e-362b-8546-d1959a3e7ce1 | -9.18504 | -47.83712 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 50c4de42-aa97-381d-addd-23f418124253 | -8.17938 | -43.34982 | 2025-10-07 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0e8e9553-0316-3a02-8a5a-07099afe8127 | -6.28318 | -42.94366 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c281c7b-0873-3184-8aa2-b093cf439bf1 | -6.25392 | -43.2771 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7a8c4e95-6f5e-3605-afc9-eb5989b748fe | -11.13288 | -47.21735 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 291af649-70fe-3763-8937-3f3040814d30 | -7.67333 | -50.20739 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1891b346-830a-3796-b933-03a04d23ff27 | -10.81461 | -48.5983 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5dce01-bec1-3dbb-8a01-b65a67d8635d | -10.43422 | -50.32951 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1ac18f7-1277-3f47-b008-e92fd2a7f1ab | -7.68915 | -42.41051 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d2791037-7d66-3100-8346-e9fdf83a969c | -11.84168 | -44.91165 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56c0fc69-7bc9-3e8d-ab2c-deadafb074d0 | -8.18112 | -43.33905 | 2025-10-07 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2ab04991-e4f4-3e0d-8cb0-a0bb7ac0bf8a | -8.65556 | -46.28278 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3ad6284-ba3b-3aa4-8af3-9718dab181de | -10.73547 | -50.49248 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b06997a0-43d1-3fb3-b971-0bf17a904600 | -11.65202 | -44.26481 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2baa6553-2ce6-380a-a8be-7f105b74a6c3 | -8.6519 | -46.29953 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df06b8cb-4225-38a0-9d17-a2b76cbf0d26 | -11.94854 | -45.48554 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0264056-9ec1-3889-89f5-92c7e6c97b9e | -8.61499 | -54.96739 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60d0ef7e-40d8-3b38-963c-b3f9e4579e15 | -6.72157 | -42.84224 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d47ce7de-3476-3438-9434-6fbf16c14c4d | -7.89149 | -47.81808 | 2025-10-07 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9cb0423-129d-3cd2-954d-1e41b8113a0d | -11.94307 | -43.04129 | 2025-10-07 04:08:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aabc1298-8893-3d4f-852f-58dbb41682fb | -9.67202 | -45.67289 | 2025-10-07 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6587128d-4064-3603-a0de-391cdc35a3c7 | -10.26802 | -44.36434 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edefcb4f-d418-3750-90ad-440e803ba2b5 | -5.64736 | -45.95719 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3af15f0d-33fe-3b5b-856f-12f7d7768d8a | -5.7127 | -44.83283 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 08a41bb2-dc0a-37a6-977e-57e40ad677ba | -5.33555 | -43.1062 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5968943c-ee78-3850-9a36-6b49596433bd | -10.74615 | -50.48882 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bf66e512-bf30-394b-bf4f-01a14090d7c2 | -5.71201 | -44.8371 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 665da5b7-8556-3aa0-992e-47904e30e8f5 | -10.45725 | -50.41534 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34bcd6e6-d316-378d-8cf8-d027929315c6 | -11.39151 | -43.49237 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f84b6f2d-7c8c-398c-9827-d10f035f8277 | -7.72056 | -42.40474 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c24f2c62-7e1f-31db-a4b8-abc1959fb107 | -6.71113 | -42.84734 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6942d862-46f2-358e-9dc8-e119f52b411b | -8.18054 | -43.34264 | 2025-10-07 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1c73c933-6481-3266-ac6d-ec4ab0358590 | -5.03596 | -45.5579 | 2025-10-07 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6eeb85-a1e0-30d2-87bc-ad6e92ac0623 | -11.17122 | -47.73772 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a933cf3-9bec-3529-ad95-be396afdc116 | -10.61213 | -44.34331 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README26.md)
