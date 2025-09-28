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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73923c4d-20e4-34a9-81f9-58b1019d8610 | -7.79225 | -47.01035 | 2025-09-28 06:37:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| e652cae4-f254-3759-aa3b-daa909280c64 | -11.1461 | -54.30964 | 2025-09-28 06:37:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b5d8398c-4a6e-3621-89c2-271a917b4d4f | -7.80295 | -46.97951 | 2025-09-28 06:37:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 50f9dc6b-fa1a-34eb-8dba-26253a1a4f99 | -9.92832 | -59.92408 | 2025-09-28 06:37:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a2077c1-c29a-3107-b6fd-d9ba9a987bf9 | -9.64665 | -62.82541 | 2025-09-28 06:37:00 | AQUA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 88f5f28d-2aaa-3068-a387-80426e866b09 | -9.64374 | -62.84266 | 2025-09-28 06:37:00 | AQUA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 456398d5-c77b-30bb-92b1-fbe0ccc0fa5b | -11.97379 | -47.98942 | 2025-09-28 06:37:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ff697714-b1ee-3b11-9199-8488121228af | -11.96957 | -48.02582 | 2025-09-28 06:37:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9b785bf3-ca33-3d48-9718-f90bdd95fafb | -16.9864 | -53.6947 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0f1c6d8c-72c5-31cb-96e1-37687f20d790 | -16.9667 | -53.6975 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 75c1c3c6-683b-3bd0-8732-6ddd78e0ba8a | -16.9868 | -53.6734 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| cbc4bf2d-4fee-3040-8454-51ed9e519b27 | -16.9474 | -53.6791 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| dbef70af-18dc-389a-a8b8-13e660d35ac6 | -16.947 | -53.7003 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4646273c-9879-3caa-9ae9-9842f8a5cfeb | -16.9671 | -53.6763 | 2025-09-28 06:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 169.9 |
| bf3e2182-5874-3973-891c-3a36daf6b76a | -18.1977 | -53.3208 | 2025-09-28 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 1e2be366-cd42-3373-9b95-8c476214eca5 | -15.83547 | -59.60154 | 2025-09-28 06:40:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9a884488-44fa-357a-ad34-5e98e37fa30f | -18.19944 | -53.32895 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 42eb0b83-ca6a-3741-9b16-1c815697ad61 | -18.18748 | -53.32775 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 219db3be-43a3-3c6a-a1c1-ac27e293c42c | -13.61093 | -48.06315 | 2025-09-28 06:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 49095b19-c758-3e8c-9cfe-762f400a4c80 | -16.95206 | -53.69728 | 2025-09-28 06:40:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 7a3767a0-d1c0-3d61-8eb5-5698391566ad | -16.96342 | -53.6987 | 2025-09-28 06:40:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2ddb9d6b-6253-32d6-8154-15a7bc5883de | -15.94196 | -57.48166 | 2025-09-28 06:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d2ab65b-ddcc-3ac1-905f-4bd23fee7d08 | -18.18941 | -53.31172 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 845b4b47-d5c3-31c6-9115-9aeafc39d3b6 | -12.98635 | -49.422 | 2025-09-28 06:40:00 | AQUA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 625e7d84-5cf9-392c-9894-0d5c4beb1bac | -16.9654 | -53.68306 | 2025-09-28 06:40:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 301.0 |
| ace49077-ba62-3c84-a244-d22d1670d135 | -16.95403 | -53.6816 | 2025-09-28 06:40:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 99d6cd9d-9a23-3679-8951-f73e50675698 | -13.59995 | -48.06607 | 2025-09-28 06:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 4240ba2a-ed02-3924-9a98-ebd29192a553 | -18.17554 | -53.3264 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 769510fd-1fa4-3db1-a8b7-bc82a564fd23 | -13.60681 | -48.09999 | 2025-09-28 06:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 17edca0d-3d62-3a4e-9cee-a56bed46afc3 | -13.59616 | -48.10255 | 2025-09-28 06:40:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b6c18b47-8b8f-3874-b70f-bddb3d680606 | -18.20667 | -53.31898 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e06786bd-91ac-366f-a728-580fd2ae34bb | -12.98298 | -49.45071 | 2025-09-28 06:40:00 | AQUA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8360f474-1dbd-3391-86cc-5c4cc9f013be | -16.96739 | -53.66733 | 2025-09-28 06:40:00 | AQUA_M-M | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 31faaae4-edf1-39c9-92a4-178cef5f4629 | -15.95091 | -57.48295 | 2025-09-28 06:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 98838cac-2da9-3201-8c97-67e07198b886 | -18.20473 | -53.33587 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d70c2fb9-467c-3b48-b03c-84513358cca9 | -18.20149 | -53.31212 | 2025-09-28 06:40:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c8232daa-991b-3fc9-9a60-f7aaf31c3271 | -14.38179 | -54.93849 | 2025-09-28 06:40:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06b9bc61-8e9a-3234-8b23-f6959f6b4dc6 | -15.27415 | -56.80024 | 2025-09-28 06:40:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1d6644a-acaf-3c22-8f16-564fad8ad4a0 | -16.9667 | -53.6975 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 316.9 |
| 61b296de-94b7-3701-814c-fdee12fc778b | -18.1977 | -53.3208 | 2025-09-28 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 05bf1bf2-4e84-3a8f-8a4c-b6ab95e1fb92 | -16.9868 | -53.6734 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1ec3fc7c-3cf2-3b7a-a161-92467fd59765 | -16.947 | -53.7003 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 14b363be-abcb-3f0f-9803-0dcb0e1581a4 | -16.9864 | -53.6947 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| dafcb12f-d715-38bb-ab11-743461e104c8 | -16.9671 | -53.6763 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 16f75f7b-5f06-3c85-8b55-910af69cc797 | -16.9474 | -53.6791 | 2025-09-28 06:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 01f65370-0adb-3bb3-9569-52b8c3a85098 | -16.9864 | -53.6947 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 711fa661-72f7-3be7-b450-8fba447a54c8 | -16.9671 | -53.6763 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 277.7 |
| bcd314cb-a86a-3078-b649-0dcfd18a131b | -16.9667 | -53.6975 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 455.7 |
| 9270ac85-6c43-31e1-a830-88246366319e | -16.947 | -53.7003 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| e8a964cf-7ee1-32b5-879d-36b8bcb88479 | -16.9868 | -53.6734 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| d9e541bc-60d1-3396-b73f-291551d1f0e6 | -18.1977 | -53.3208 | 2025-09-28 07:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 234a670e-49ef-36cc-a262-25194eeaa545 | -16.9474 | -53.6791 | 2025-09-28 07:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 661cdfd8-f6cc-3840-b1e1-fdeac2f7b1ec | -18.1972 | -53.3423 | 2025-09-28 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| dbcc29f4-b3fb-313d-aa28-8c7aef1389e2 | -16.9667 | -53.6975 | 2025-09-28 07:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 8388fbff-1cf9-3478-84aa-9e88a71285a0 | -18.1977 | -53.3208 | 2025-09-28 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 34b2a76b-09e3-3ba3-8eec-d84696fc56b1 | -16.947 | -53.7003 | 2025-09-28 07:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9b07b082-a3da-3e4a-9090-03eeb7540776 | -16.9474 | -53.6791 | 2025-09-28 07:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 83e68a5d-2439-3560-82cb-4eb33d6455e0 | -16.9671 | -53.6763 | 2025-09-28 07:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 678e2c75-c0b3-374f-ae9b-0e345b3dedca | -16.947 | -53.7003 | 2025-09-28 07:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 15dc9538-37dd-3672-8a8f-dd72bdda8c86 | -12.9918 | -49.4448 | 2025-09-28 07:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1ec41bf6-0fab-339f-9e5d-7f45f176c17d | -16.9671 | -53.6763 | 2025-09-28 07:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 4e110f37-19f6-38e3-bf02-350788007604 | -18.1977 | -53.3208 | 2025-09-28 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 7e48f399-fd8b-32c1-ab2c-3d95ff38cfa9 | -16.9667 | -53.6975 | 2025-09-28 07:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 166.2 |
| b83f00f1-bae1-3011-bd99-cb9641e9e6f9 | -16.9474 | -53.6791 | 2025-09-28 07:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3a60e3ab-6014-35f8-854b-05fa892fc3f1 | -16.9474 | -53.6791 | 2025-09-28 07:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| abfe5a4e-b398-30f6-b38c-bd8ea1e0eb79 | -12.9918 | -49.4448 | 2025-09-28 07:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 0491e83d-b22d-302e-a68c-ae8c53cd5f93 | -16.947 | -53.7003 | 2025-09-28 07:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b0f31f85-b18c-3fba-9fa7-21a16e1d3f61 | -18.1977 | -53.3208 | 2025-09-28 07:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3e38fc85-3362-3b69-9a23-eb7558b6908b | -16.9671 | -53.6763 | 2025-09-28 07:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 79561bc1-4984-31d8-a1bd-3c24d588d2e2 | -18.2176 | -53.3177 | 2025-09-28 07:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 423bb13f-f5b5-319e-8748-58f3f32c6054 | -12.9914 | -49.4667 | 2025-09-28 07:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0d6b7c44-1773-3feb-ad98-3b02d2048af5 | -16.9667 | -53.6975 | 2025-09-28 07:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 224.9 |
| e0e42a34-7372-3119-9844-601733cc5e79 | -16.9667 | -53.6975 | 2025-09-28 07:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 0362d4a0-12d1-394d-80b3-2535a16466a8 | -15.6092 | -53.1669 | 2025-09-28 07:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2ba474af-8d95-3be8-832e-dc9c24f3abd1 | -12.9918 | -49.4448 | 2025-09-28 07:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a6173911-ca56-340f-9007-5a12baac4a4a | -15.6286 | -53.1643 | 2025-09-28 07:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 956c051a-51ac-31dc-8fa1-344604ec1f7b | -18.1977 | -53.3208 | 2025-09-28 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 120.8 |
| c66ce269-c0e4-39dc-989e-4690647698ea | -16.9671 | -53.6763 | 2025-09-28 07:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 11146c84-3a55-328d-aafa-a76880e12508 | -16.9671 | -53.6763 | 2025-09-28 07:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f2679ce4-7b71-3c3f-8f2d-abbbe44252ae | -16.9667 | -53.6975 | 2025-09-28 07:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e04aa5f7-5f27-3f37-bf06-f0ddc9545bd8 | -18.1977 | -53.3208 | 2025-09-28 07:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 504d4d33-8f65-3e6a-be68-5e44bdeb0d84 | -16.947 | -53.7003 | 2025-09-28 07:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9613354b-58de-3209-995c-92016fd5b5f8 | -12.9918 | -49.4448 | 2025-09-28 07:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c595e7b9-4dff-34ac-b69c-c85a12bf902f | -16.9667 | -53.6975 | 2025-09-28 08:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ec9ef172-187d-3cc4-bea5-8a8593b5da65 | -18.1977 | -53.3208 | 2025-09-28 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 490e6e14-74f8-3bd4-85bb-9a6a8b14d21b | -15.6092 | -53.1669 | 2025-09-28 08:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 79bb07bc-fc13-340d-80da-9664f5e13a41 | -12.9918 | -49.4448 | 2025-09-28 08:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 65ae7a64-de37-388b-b885-e26ce99a0234 | -13.011 | -49.4423 | 2025-09-28 08:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 10f48946-147c-32c3-9f0b-2d4930135c58 | -12.9918 | -49.4448 | 2025-09-28 08:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f7c3b055-bece-32ee-ad8b-74ae39d32cd4 | -18.1977 | -53.3208 | 2025-09-28 08:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 18e73221-38c9-3816-af32-d0cb60ac2cbb | -18.1977 | -53.3208 | 2025-09-28 08:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9209ebbf-f7a3-35fb-a3d7-b6295fa387bd | -12.9918 | -49.4448 | 2025-09-28 08:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b1ad8057-5013-3329-b5b8-674ca706106b | -11.9824 | -48.0197 | 2025-09-28 08:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3af6df48-4e8e-38a0-931f-9a1a89784f17 | -18.1977 | -53.3208 | 2025-09-28 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 38198fc6-28bd-3566-9e22-de65d2de3b68 | -18.1977 | -53.3208 | 2025-09-28 08:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 111.8 |
| d90584fb-19ed-3b72-921d-b651f330694b | -12.9354 | -45.1649 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 47ac2106-2df4-328a-834b-14a013f1571b | -12.9156 | -45.1912 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 299.1 |
| 003e7046-9f95-3203-8e53-c9c8a42124e3 | -12.9161 | -45.168 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| c4b3e56e-2a71-30a9-85fb-923ad375bdf0 | -12.9547 | -45.1618 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 2973ff30-d934-30f5-9914-19a666979e22 | -12.935 | -45.1881 | 2025-09-28 09:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |


[Clique aqui para ver as próximas entradas](README94.md)
