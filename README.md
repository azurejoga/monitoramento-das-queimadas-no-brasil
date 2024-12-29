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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f157487-f1d1-31f4-a5f3-bc725ab1dd2e | -4.80927 | -42.97791 | 2024-12-29 01:06:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 332ef89f-45f4-3c92-ba2e-500419618acb | -7.37751 | -45.83115 | 2024-12-29 01:06:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bd514168-6248-3e81-bbd5-81c57f68442c | -4.55004 | -50.18689 | 2024-12-29 01:06:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6990d3b9-8e26-3d99-bd0e-64a3d7344a37 | -5.49034 | -43.97708 | 2024-12-29 01:06:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1fca82c7-aff1-35fa-81e1-a9fe3556f4b1 | -6.95911 | -43.02328 | 2024-12-29 01:06:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 3a818359-2900-3346-8c55-fd1bbbf683ab | -4.80423 | -42.98552 | 2024-12-29 01:06:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7812af36-954c-3d34-9342-54ccdd4669e8 | -6.96745 | -43.01672 | 2024-12-29 01:06:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 5d1d52a9-cae6-31af-8edf-ef327a095c63 | -6.49 | -47.50983 | 2024-12-29 01:06:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ee51a33d-92a0-3b20-a943-f39044f7b2cd | -7.37767 | -45.83662 | 2024-12-29 01:06:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 3f023114-1062-3c33-b7cd-978290458d07 | -1.82354 | -53.84551 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26778b46-90b7-372e-a065-0a5ee14f54a3 | 4.18138 | -60.27967 | 2024-12-29 01:09:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 52f279cf-dc34-30b8-8555-6b5e25457b3b | 1.1048 | -59.20447 | 2024-12-29 01:09:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0dc89bff-eefa-3c81-b4f8-6d77cb6a883d | -1.27972 | -53.4556 | 2024-12-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1bf1572e-2950-3563-86b9-8d36064889da | -2.39031 | -51.90435 | 2024-12-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ce64930-452e-3769-998c-0748f81eebc0 | -1.27089 | -53.45684 | 2024-12-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 33fcb9fc-8c50-3f6e-ae42-7871007e75bd | -1.5342 | -51.97346 | 2024-12-29 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 10baa790-6ba8-3b93-af3b-9ec6b2b6ffa3 | -1.19026 | -53.73438 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ad788017-6fcd-39f7-b74e-cb62ec57b756 | -1.79641 | -53.131 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0cc7f46a-5f3b-3def-9df0-295a7755b7a8 | -1.82231 | -53.83665 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ae4f96b-c459-391c-abc9-38a4f27b8b6b | 1.10716 | -59.18847 | 2024-12-29 01:09:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7c5e0642-2c7b-349c-af7c-303d1b1607bf | -2.68743 | -54.03313 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 06f433f4-572b-37a1-b791-8a75ebaec78e | -1.63299 | -52.61851 | 2024-12-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 34fcae5a-9b95-31df-9dcc-e453fdbbf554 | -1.79763 | -53.1398 | 2024-12-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b938c258-82be-3956-8401-f7109487e371 | -1.27211 | -53.46563 | 2024-12-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| da3436ad-3e31-3e49-a172-37c291cec048 | -1.6531 | -53.36068 | 2024-12-29 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e5b1c56c-2d8b-3221-a2f4-7201d7e9772f | 1.10911 | -59.19879 | 2024-12-29 01:09:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ad8637e0-6423-3e5c-8ba4-7368c3e26463 | -2.58613 | -51.92068 | 2024-12-29 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 250b94c5-6628-364c-877d-3fada4a8c9fe | -5.42114 | -37.74036 | 2024-12-29 03:02:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 552bbaa6-17db-3ddb-883f-2b3f0bccd772 | -5.42767 | -37.74146 | 2024-12-29 03:02:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bd84a09c-e842-3e5c-8d1f-b7131b1e1c95 | -12.64019 | -38.56781 | 2024-12-29 03:04:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4f6cb39e-fa9a-3dc2-9f5e-303cc7ebab88 | -12.64048 | -38.56443 | 2024-12-29 03:04:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 58777a63-c774-3bf7-9323-e8a6ef6c961d | -12.63954 | -38.56916 | 2024-12-29 03:04:00 | NOAA-20 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7a507d81-1ca3-3c2d-8133-88620ba69d49 | -22.67581 | -42.8592 | 2024-12-29 03:08:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ddedb37e-033d-3db7-8cc6-61d58528eb36 | -22.77807 | -43.04921 | 2024-12-29 03:08:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e27bab5e-f629-3dcf-a528-eb832ae5669b | -22.67439 | -42.86497 | 2024-12-29 03:08:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8e5d8bd2-27b6-3467-992a-72b4ba93872f | -22.77951 | -43.04351 | 2024-12-29 03:08:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4961a33e-7842-3e13-b70a-ef358d7d31f2 | -2.96987 | -40.12467 | 2024-12-29 03:53:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93550fc5-0676-36e4-b32e-cb141fa7ed01 | -3.02321 | -40.20413 | 2024-12-29 03:53:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 240b0552-abf0-38ec-a575-966b9715cdcc | -2.94509 | -40.42004 | 2024-12-29 03:53:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abd3daea-5bf4-33fe-9d4d-edbf0c521274 | -9.65311 | -42.78536 | 2024-12-29 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5cc1b75c-1a92-33a6-a0dd-54a8e034e344 | -6.98567 | -47.08467 | 2024-12-29 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab3fa29a-25e0-3cb2-8bba-5c6b5a30abcb | -10.42915 | -44.89106 | 2024-12-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93a3a6b1-22b9-394d-ad70-511abc5a23f0 | -9.41034 | -35.92801 | 2024-12-29 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27900630-6b7a-36df-a28d-982b8f270394 | -4.82374 | -45.37197 | 2024-12-29 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 337bb190-19ed-347e-b453-7c0e4448b7a4 | -9.41313 | -35.92608 | 2024-12-29 03:55:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 92d694e2-c3d9-3279-a336-deb38b8f6ae2 | -7.37929 | -45.83551 | 2024-12-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2b120db7-1819-33d3-91b7-dc597518842d | -5.42318 | -37.73086 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0501ff8-5165-3c4d-ad12-7bd86d3f9a39 | -8.62929 | -46.02498 | 2024-12-29 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efe19311-82d4-3bea-a0d9-74efd4621f21 | -4.90711 | -41.10258 | 2024-12-29 03:55:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86b45a3b-6412-3ad2-95c4-e9d4e5e88135 | -6.42321 | -43.78047 | 2024-12-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05544317-55f0-3abd-a3dc-8cb22d4a074f | -8.40004 | -36.81023 | 2024-12-29 03:55:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31ec5329-5499-3f24-b60f-c0b3e9cd78b3 | -10.43391 | -44.88802 | 2024-12-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fba55832-7465-32af-9ce1-90f6caee49f1 | -8.73697 | -39.81553 | 2024-12-29 03:55:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 40cf066b-a04e-3e8b-95d5-779408b799d8 | -4.36749 | -38.17549 | 2024-12-29 03:55:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d85d4139-fb5b-3262-8a4d-fb192d7849ac | -6.49504 | -47.50497 | 2024-12-29 03:55:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f38fb0-9a8b-372d-92b2-777ebaed0ca8 | -6.49559 | -47.50182 | 2024-12-29 03:55:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00a336e9-4808-347a-9562-72d97125b677 | -5.1786 | -37.66415 | 2024-12-29 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 530aafae-2d9c-3512-bd18-35d4dbff12b6 | -5.4281 | -44.83118 | 2024-12-29 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c3c8e87-031a-3f9d-a6a1-deb13da8d76d | -7.37468 | -45.8347 | 2024-12-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28e39fa3-af43-3d1e-ae7d-98aa12d306bc | -3.66819 | -41.82602 | 2024-12-29 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c55d198c-ab01-3129-8421-79d5915fbd88 | -5.42541 | -37.7383 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 178a5310-e621-3566-8d31-cfe76e3621be | -4.5222 | -42.06884 | 2024-12-29 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 8a67e91b-0fd3-359e-9112-f09da25bf8cd | -6.00525 | -39.87363 | 2024-12-29 03:55:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23ab0a3c-d4cc-379a-a63b-808fef89e807 | -5.74623 | -38.88772 | 2024-12-29 03:55:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 97b69c51-9f6a-35be-81d1-ebc148da42f3 | -4.1995 | -42.89877 | 2024-12-29 03:55:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04877bc8-5729-3fcc-9226-f69b26bc73be | -5.43257 | -37.73586 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d9725f8-74a7-3943-a041-be632695b901 | -5.49609 | -43.98227 | 2024-12-29 03:55:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8a3c200-b47a-3fda-9d64-745863299bd9 | -5.76555 | -37.56355 | 2024-12-29 03:55:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 08ec1edc-889c-38bf-8b07-5c0c9790dcc1 | -5.2338 | -41.39534 | 2024-12-29 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eefa05dd-8b59-3be7-a20e-4e7d5c6d2960 | -5.42872 | -37.73881 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 23d95bac-7c14-398e-9792-f71db4a09dc2 | -10.43803 | -44.88872 | 2024-12-29 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711cb26f-ec8e-341d-88b4-b01bd762b7bd | -6.16111 | -44.42373 | 2024-12-29 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 049de4ce-01f1-30f0-9096-7ece2113db22 | -5.15648 | -38.48302 | 2024-12-29 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e16e13e3-ed63-38d0-afaf-037c8478b92b | -6.98515 | -47.08765 | 2024-12-29 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a63ffa1-6b4e-38df-a5a0-93e700ee52ea | -3.56236 | -40.84811 | 2024-12-29 03:55:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee316925-de2f-3968-97f9-e2ae3ee9bf19 | -6.16178 | -44.41973 | 2024-12-29 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36990d59-e36c-32a3-a99e-8776b12a55e5 | -6.18402 | -36.55784 | 2024-12-29 03:55:00 | NOAA-21 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a577cf80-6cdf-3336-aa98-b2e5b4920e81 | -5.17529 | -37.66364 | 2024-12-29 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 102f614c-aeb3-3e6c-858b-5064a8ff6d73 | -7.37888 | -45.83408 | 2024-12-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e6612c1-956d-3113-9b59-98f3ce804e66 | -5.49673 | -43.97838 | 2024-12-29 03:55:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d4b689e-beb4-3922-a3c8-2584f05eea71 | -3.97136 | -38.36005 | 2024-12-29 03:55:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d359bc75-96e6-328c-b16a-b936ddc23fe3 | -5.42595 | -37.73484 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e708891-1051-365a-a7e9-6798ad7ff654 | -4.52366 | -42.05968 | 2024-12-29 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b8e34c35-60bd-3380-b3bc-7e44c9a3505f | -7.37801 | -45.83898 | 2024-12-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| de95ed38-f8e2-3898-b023-eb2db0109fb2 | -7.14787 | -46.55022 | 2024-12-29 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b974cb77-3ae7-3705-bb30-32e03165800a | -6.45491 | -39.65647 | 2024-12-29 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 339d4aac-77c0-3122-936a-7e7ecd12a370 | -7.58859 | -46.45874 | 2024-12-29 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00af732f-4e28-3ba5-9be6-e0850b097915 | -5.45019 | -38.16968 | 2024-12-29 03:55:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1975fb6e-e822-3a8b-818f-86efa7e9789c | -8.63011 | -46.02026 | 2024-12-29 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72bd302c-475f-36ea-abfa-70f06e361339 | -8.05712 | -35.15615 | 2024-12-29 03:55:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| df568f3c-5557-3712-8e35-1c7875335c1a | -5.42926 | -37.73535 | 2024-12-29 03:55:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d229462-38ef-37ae-9523-526d9c61c56b | -7.2237 | -45.30849 | 2024-12-29 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de56c440-f5d0-3f1c-9c88-d3663b34f7f3 | -5.0426 | -37.77399 | 2024-12-29 03:55:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b70b18d-d652-3b7e-8d94-b4ae34006541 | -10.73038 | -42.69627 | 2024-12-29 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a246ba0c-bf5e-3a6c-a91b-8389e9d7fb5b | -6.70833 | -44.32056 | 2024-12-29 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4919532-de5e-3436-a31a-375968930c31 | -7.45152 | -38.07274 | 2024-12-29 03:55:00 | NOAA-21 | PEDRA BRANCA | PARAÍBA | Brasil | 2511004 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ba5209a9-375e-3b6a-bd5c-3eb87e25768a | -7.83713 | -34.91554 | 2024-12-29 03:55:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eef86adb-e57c-39ed-8daa-6a5012cb3a0e | -9.65385 | -42.78099 | 2024-12-29 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5da049bb-23a3-339f-a159-0bd65394cf77 | -10.73399 | -42.69688 | 2024-12-29 03:55:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd53746d-c215-3660-ad46-fc874fa4acff | -7.37846 | -45.8404 | 2024-12-29 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README2.md)
