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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 343e2072-e891-336b-a7cd-42963b2635f9 | -5.53139 | -43.88154 | 2025-07-19 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 29b0306c-cbe3-31dd-a2b0-24b04261d3b5 | -3.39182 | -47.47883 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5d2125-b5a2-323d-a6b5-6253086616a2 | -6.97155 | -42.8022 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 34424268-81ec-3345-8bea-c6c616e28f3b | -3.68727 | -43.14183 | 2025-07-19 04:08:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec7b1e7b-9d47-35dd-b352-0a94796e2f4d | -3.12889 | -47.00959 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6b32dbdd-2e34-3903-8bcb-8864b002f49d | -7.18 | -44.09527 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a752d0d5-b1b8-3049-9c74-66837cc075dc | -5.65438 | -43.71286 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e5aac9b7-b2d4-36d7-843e-925a1c0a45d7 | -9.48763 | -40.3831 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| aed759de-03ab-3d03-bfd7-3fc431a4b4a2 | -3.12457 | -47.00892 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 62447bba-8a31-364c-b8e6-219311b97b57 | -6.88824 | -45.24504 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64f6164-7e1b-3484-b1e2-1b12f920958b | -7.05474 | -42.98582 | 2025-07-19 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94db0413-7b7c-362f-8f9b-22d5576d18fc | -4.25703 | -48.54648 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d52869c-ba9c-33f4-a1e3-74200e35cef4 | -4.67242 | -41.95699 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7fd076cb-85d7-30f9-94a5-2a61161a14fc | -9.60371 | -40.61098 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 654133df-8b34-309e-b2a8-de083b4d3566 | -6.91872 | -44.83215 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 810d450a-5b6c-32c2-b552-6aef9fd575d3 | -10.4701 | -47.94431 | 2025-07-19 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c86b49a8-2500-31e6-b9af-4cd598ab33c7 | -3.68048 | -43.05317 | 2025-07-19 04:08:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f83e2bbb-e412-3e59-8c66-e0ceb7cc08ed | -8.41552 | -46.87514 | 2025-07-19 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0311d2da-fe4b-3e32-a836-93882a6c1ce9 | -5.77985 | -44.93092 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 457df10e-5cb8-3537-a290-5488c394fccb | -4.59088 | -47.27268 | 2025-07-19 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52b5184d-bf20-3048-a2ae-645216af0b11 | -9.61018 | -43.85941 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5acde433-c4ed-36c9-b02b-20cbaa8113e5 | -8.01777 | -43.66768 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7302dd0e-16c0-3deb-8392-5cb3a2cf63fc | -6.16316 | -43.75747 | 2025-07-19 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 827d73d7-b538-35ef-8de7-e7a8e5962c93 | -3.58764 | -48.93891 | 2025-07-19 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75d2b5a8-85e8-34bd-890c-5f1cb93a9c9b | -10.63601 | -45.23426 | 2025-07-19 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a0a41dd-6c36-3fc2-b530-1177626d3473 | -9.59393 | -43.85303 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd300954-7066-338c-a3ff-efcf2b21ea8a | -5.1045 | -43.15392 | 2025-07-19 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25e48580-dd32-3920-93a9-3f513bc66e54 | -3.03408 | -49.42826 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0322b1b1-3473-3a18-8bea-79cef2255aaf | -6.02958 | -44.04615 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 482d1ed5-10fc-34bf-83ca-70b538ec63b8 | -3.61595 | -43.54034 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a39b2509-02fe-3fc3-bf26-233b5e27a859 | -3.95162 | -49.44367 | 2025-07-19 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31308468-8c77-33d8-81ce-480db2a834a9 | -6.89261 | -45.24127 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be23f864-96dd-365d-b1b6-204d826705da | -7.71201 | -47.29139 | 2025-07-19 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 851df3e3-5179-3428-95e2-53a378abd18e | -3.92737 | -43.1562 | 2025-07-19 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b8185dc-84e7-3131-a3f8-e574abc9938d | -6.15902 | -47.7635 | 2025-07-19 04:08:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54b0643b-2bfb-3158-8813-8e59d7794fe4 | -9.81151 | -48.5575 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dd10c9c-c029-3e91-8521-5ae7bd247b9f | -7.21854 | -35.78137 | 2025-07-19 04:08:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3deb69dd-a97b-3500-b135-2dda571011c1 | -10.63486 | -45.23493 | 2025-07-19 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5bbf3367-80d1-377b-8973-2d5ba1719df9 | -7.03847 | -43.88396 | 2025-07-19 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d2c0408-db18-3823-bb78-1fe7195565b5 | -7.71264 | -47.28768 | 2025-07-19 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e43ca8e-8f5b-3833-b4be-8a9688f6a0ce | -3.2955 | -50.75336 | 2025-07-19 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61246d26-7edc-357f-8220-ded30971ab78 | -6.1547 | -47.76274 | 2025-07-19 04:08:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc1a062-41ae-3a37-b5f5-ef44684b0b07 | -9.60144 | -40.60305 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e56cf30d-0db8-3237-a254-c4583cfdf907 | -5.6592 | -43.72151 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8ed9d957-fc0b-3288-bb56-7da3bb58e186 | -3.13255 | -47.01436 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| acb61b3e-dbdf-3017-940e-a6a987991aba | -8.55051 | -47.85131 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba64144d-39f3-3b65-8fe6-a5c0178512ed | -8.0528 | -42.15688 | 2025-07-19 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e82025b8-0601-371d-aa90-2274768c1f07 | -6.16559 | -47.77749 | 2025-07-19 04:08:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7dd7b598-9ba2-3ffe-a401-eeb2e74ee3f9 | -9.94926 | -48.16766 | 2025-07-19 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2eda23e8-0d0c-30fa-86b0-e5b85387e847 | -4.0314 | -48.06348 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4ced9d0-c70e-3908-8b83-37cbfc7bd6ff | -7.22638 | -44.13032 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4759a9c9-f229-3f50-a938-cb0fea9d7b31 | -3.29451 | -50.75344 | 2025-07-19 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3ceacea-e762-324f-9675-8c5d5d829239 | -5.65378 | -43.71666 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0b37539b-6c15-3d65-9c58-17f628a21ada | -8.06875 | -50.07688 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 155878d6-3ed2-37e4-8c18-1d7ce80284ad | -11.41519 | -42.07256 | 2025-07-19 04:08:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ee38413-5f46-3d3d-9259-056fb23827a1 | -6.16265 | -47.76843 | 2025-07-19 04:08:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32bed3d0-e682-32c5-9c67-2d24da38bb8f | -9.7643 | -48.75104 | 2025-07-19 04:08:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c5bb445-f714-3d27-8273-c55b692d5816 | -3.12823 | -47.01368 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f787674f-23d3-3fb9-9860-546fae413de3 | -6.97432 | -42.80624 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2b672fa-2a32-3198-8f23-d4ff7b1d8831 | -10.62924 | -44.76799 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6d3a421-2311-39b8-a713-e884bea04da3 | -7.4841 | -47.50298 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b3911834-4473-3a75-9b27-3d273f04215c | -7.08864 | -49.1803 | 2025-07-19 04:08:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8b72e1e-7dd6-3e0a-a910-d0d480d44834 | -9.8156 | -47.73548 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07ff74d4-f1f6-3434-a349-36bb1c094c74 | -9.04487 | -40.57565 | 2025-07-19 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29445cdc-8670-338b-a1cc-0d7a6bb2718f | -6.16506 | -48.05119 | 2025-07-19 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e25cac3b-d2d7-361e-9a99-147818601781 | -9.60428 | -40.60728 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| efdeb804-f101-3d59-91f8-57743b982c4e | -10.6333 | -44.76475 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dc380911-da72-3471-abdd-ccef15e4fa3c | -6.97488 | -42.80272 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbe2abd0-a083-3642-88dc-b6177379aab9 | -8.07168 | -50.07615 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7db2055f-dcf6-386b-ba6e-9d6fa424d02c | -4.12653 | -47.65166 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf7734a9-11f8-3654-9add-109e60d8053c | -3.04529 | -49.42388 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bd887a81-1466-30e8-88a7-e10bd3e2771c | -4.9156 | -37.4888 | 2025-07-19 04:08:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2537be92-1008-3d83-8d30-6866b86dca78 | -6.51277 | -44.6068 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17c386c0-9720-3c8a-ba36-c28e0fa71bdf | -7.95124 | -43.95149 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2e224b1-fa8a-320d-89e0-2b1f6332028c | -6.76077 | -45.52294 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb6a625-6c5f-3ecc-870c-7388262e708f | -7.28636 | -43.89199 | 2025-07-19 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbe35392-087e-3d49-9fb4-a5cd9766bd4b | -5.41693 | -40.74039 | 2025-07-19 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8f384f23-0818-3079-a74e-09e89be84152 | -3.36582 | -49.16545 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8fa4ad2-ab76-3680-b208-592ed34f7049 | -7.34325 | -43.93193 | 2025-07-19 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0240458-92bc-388b-80c1-7c635999e14c | -5.64747 | -43.71179 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 521b354b-5b0d-3cd4-ba83-7e2a6476a912 | -10.69359 | -42.64751 | 2025-07-19 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 522e3335-a9aa-3b0c-bc3e-b59ecd698843 | -4.8715 | -47.76304 | 2025-07-19 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37a1f270-23f0-3454-bce0-457d3d64a0c9 | -3.14185 | -47.01159 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f293230d-4f8a-37fd-8bc2-b37a2cba5abb | -9.83837 | -48.37786 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b858bbe3-0be0-3e5a-a14c-a1cbfb5824cd | -8.98877 | -47.93792 | 2025-07-19 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bae9e11-8a7b-371b-a10a-65e12f0d6aa5 | -5.65982 | -43.71773 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 06ada62f-b94b-3a00-8bd3-062e81d49f00 | -3.14119 | -47.01572 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afde8266-cfad-376e-a73d-926648fd2ce6 | -4.25148 | -48.55074 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0595b21d-7a4d-3309-959a-a7159b4570bc | -3.61532 | -43.54419 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1be30088-fd29-39ec-a308-6a0c720cc4b6 | -6.75852 | -45.51328 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a09e835-2ae8-361e-ae34-77a93a1bc1d4 | -8.33367 | -50.49434 | 2025-07-19 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b345c2-dd2a-3ed9-aed3-816313d6299c | -7.07202 | -42.98497 | 2025-07-19 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 876e312f-46f5-3627-8f25-5d851e4cb61b | -6.44475 | -51.88662 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c3e1746-f8e6-3503-90ae-00fe05a441e5 | -7.48762 | -47.50743 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7ed4cbde-8382-39b8-9203-5dfffd9aa185 | -8.74486 | -47.73474 | 2025-07-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5c1ae44-60f2-3dd6-bd59-f0776a4c1cb1 | -7.06755 | -42.99153 | 2025-07-19 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4c14f43-f22e-3441-b032-bc50ed04208d | -2.91074 | -48.23848 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 81a67cdb-f5a4-3372-be18-6ec1e67f9cd7 | -9.59335 | -43.85666 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 889ab6b0-cceb-3173-9202-003ec5e9ec36 | -9.61262 | -49.02184 | 2025-07-19 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bb866fe-d74c-3b50-95b3-1a0697730e2f | -3.39041 | -47.48759 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README11.md)
