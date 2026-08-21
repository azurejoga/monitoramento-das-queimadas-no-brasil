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
| 8389f9de-204f-3659-b4e0-796c7777c404 | -6.1178 | -59.8877 | 2026-08-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f1aabce5-52c0-3105-b61f-7f7a3621cf63 | -9.4558 | -48.2717 | 2026-08-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 295.1 |
| c79f3c4e-3633-390c-8ef1-d81702ae81ca | -6.857 | -59.4371 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 911303cc-1433-3a06-b334-374dfec07845 | -8.3717 | -62.716 | 2026-08-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3b338531-0b4f-314d-b714-7070d052439e | -14.3343 | -51.8944 | 2026-08-21 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 163af05d-8a25-3ec2-ae52-62175c5e7cb4 | -6.8937 | -47.4738 | 2026-08-21 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 1bf3a285-0c85-3c28-9803-a896014fc676 | -8.3903 | -62.6963 | 2026-08-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4270c2fc-12c1-364e-abcb-e7b28bdf7788 | -6.5828 | -59.0044 | 2026-08-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 3c750bef-6cf9-3044-80e1-76c5b25bf49f | -11.3658 | -47.2337 | 2026-08-21 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ad764e21-7e14-3bc6-9650-179c2e0af620 | -13.412 | -54.3531 | 2026-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 42bcc30a-834d-3559-8a52-c9ade6a7e7d9 | -17.6726 | -44.4776 | 2026-08-21 14:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 69a9fa1b-542f-34e1-bcce-b847720d45ad | -8.5175 | -55.324 | 2026-08-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 51915b88-10d3-393d-b853-ca0ad29a6fe9 | -6.5829 | -58.9851 | 2026-08-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 9f8a9280-dba3-3028-95d5-033e069606f1 | -9.4072 | -60.3977 | 2026-08-21 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 19535c5b-03aa-31ff-8d9b-3cd6dc8c10f5 | -6.1361 | -59.9063 | 2026-08-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 00df8f87-f0d3-33d1-8baa-09e11bdf919a | -11.3853 | -47.2088 | 2026-08-21 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| e3c22b5d-a856-36b6-a562-90c4c3ec5728 | -8.3903 | -62.6963 | 2026-08-21 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| da4664ee-ab77-3351-b502-e7c2396a3f98 | -9.4259 | -60.3967 | 2026-08-21 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 85ddda3d-b3f1-35e0-91b7-6841c6735e7a | -13.3926 | -54.3758 | 2026-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 39965498-1e58-3b0a-b047-3ee92d42845d | -14.997 | -52.6775 | 2026-08-21 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 006d94f4-e91b-3917-8143-0724c841eef7 | -13.7384 | -51.8438 | 2026-08-21 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1f11907d-a154-3d10-bc35-1d4e0046ccd0 | -11.3662 | -47.2113 | 2026-08-21 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7998ea73-3f4c-31e9-89ee-7df42062095e | -13.3734 | -54.3779 | 2026-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3f66c3c9-4d67-34fd-b29b-e83e6d1bde5b | -5.7854 | -46.1168 | 2026-08-21 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9afe09bf-0019-3429-a044-6a3ad13f0532 | -6.2341 | -55.6109 | 2026-08-21 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fdaf96a4-dbc0-334e-a45f-d5c6b98e1a63 | -9.4558 | -48.2717 | 2026-08-21 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 026504fc-9f98-3c27-89b4-b69a2fbe963c | -13.2431 | -51.6295 | 2026-08-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 179.2 |
| ba1985e7-a8a0-348f-b994-67a5e6b3b18c | -11.175 | -54.001 | 2026-08-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.6 |
| b5520be7-b031-3b61-81e0-46679f8cb7d0 | -13.4117 | -54.3737 | 2026-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2fe93125-6679-3191-8da7-6112ee52bb89 | -11.3849 | -47.2312 | 2026-08-21 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 598f978d-ea84-3483-9280-fa132148e23c | -11.1558 | -54.0233 | 2026-08-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7c040aef-36dc-3279-afe3-24a44ff63756 | -5.6166 | -44.0196 | 2026-08-21 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 258.3 |
| a022b2a2-8c4b-3a3c-ae69-1b3e626f112d | -9.4069 | -60.4362 | 2026-08-21 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a19ec03a-0e1e-30e6-bab2-af53172ccbb3 | -8.8856 | -60.5394 | 2026-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 40202d68-140c-3c39-b0f3-e7bac22553da | -6.583 | -58.9658 | 2026-08-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 267847b5-4999-3962-95f9-20883e63162e | -8.9041 | -60.5577 | 2026-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| e6afc8cc-dbde-3c3f-96f0-c5588b907c6e | -8.3718 | -62.697 | 2026-08-21 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 242aee80-e67c-3639-bd84-4b9bc2d10de0 | -6.1362 | -59.8871 | 2026-08-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d44e4385-82c6-3e9e-baf6-557a806a8ba3 | -6.2487 | -48.6506 | 2026-08-21 14:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 55d8d61b-d781-3eb1-8996-a22afce9a062 | -9.4257 | -60.416 | 2026-08-21 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 098e788f-517d-31bf-8c80-045a4c987557 | -13.7188 | -51.8675 | 2026-08-21 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d09e8bea-d185-3662-9d31-0edc5eba82e8 | -13.738 | -51.8651 | 2026-08-21 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 52c29c94-683e-3836-bfa9-871b5be19726 | -8.3717 | -62.716 | 2026-08-21 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fc6c1547-30e1-3979-9256-6ab468f51f62 | -5.6168 | -43.9965 | 2026-08-21 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 337e1fa3-ac9d-37aa-ac45-884ac46cb4a0 | -8.5173 | -55.3441 | 2026-08-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2854e289-afb3-3507-b8d8-b3b91727cc0c | -5.598 | -43.9978 | 2026-08-21 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 269.2 |
| 24ffa4d4-0202-3467-abda-da1cc374b914 | -8.3902 | -62.7152 | 2026-08-21 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| bcf5d30a-ea9d-3b31-ae63-1f9ccf7d2f10 | -13.2623 | -51.6271 | 2026-08-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 9c5d56dc-650c-3808-912d-b5b4bf8a522a | -11.1561 | -54.0028 | 2026-08-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f2af5aab-35ac-3cfc-899a-0961f05b8925 | -13.3929 | -54.3551 | 2026-08-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 061e960f-fddc-32ef-8d99-b769c399b609 | -14.3343 | -51.8944 | 2026-08-21 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9778bb28-55ea-3289-b8fd-0eafaa4fd722 | -5.6024 | -45.6815 | 2026-08-21 14:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 3c130c19-eb7a-3b59-915a-b3892e17c4b9 | -6.8937 | -47.4738 | 2026-08-21 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 95b0ecaa-6eee-3f9c-ae25-27e77487110a | -8.9042 | -60.5385 | 2026-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 9d4d676d-5332-38c5-adce-07e286224669 | -13.2626 | -51.6058 | 2026-08-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 81809c97-a97b-32ba-865b-b6fc8e110baa | -14.1174 | -58.8395 | 2026-08-21 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6ed7f438-2d44-36a2-b605-46aa9d176b11 | -8.8855 | -60.5586 | 2026-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 9ccb63f1-44a6-3a46-adb5-aa004d863271 | -9.4071 | -60.417 | 2026-08-21 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 3abd1090-09b1-3133-a66a-b5917a7720c9 | -14.5662 | -53.0081 | 2026-08-21 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 68dcb412-6af4-35e4-a4ae-d3496391af7d | -14.098 | -58.8611 | 2026-08-21 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0ab36b03-fe5e-3010-a80a-e8bf328f82eb | -9.4552 | -48.3155 | 2026-08-21 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| aba30b00-efa4-394c-9439-c9925b838c84 | -9.208 | -59.6548 | 2026-08-21 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 960c4032-627d-3962-8e27-e0e66268a997 | -6.1177 | -59.9069 | 2026-08-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| f1a4d3bf-fdba-3c80-af69-87db80132ffd | -6.2673 | -48.6494 | 2026-08-21 14:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ae0d3f94-5210-3b9a-8022-9045ce08d992 | -11.1747 | -54.0216 | 2026-08-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| f380aea0-b106-3b50-9a11-a7f8506d7729 | -5.6 | -44.02 | 2026-08-21 14:15:00 | MSG-03 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afbbf959-307a-39be-af5a-f0edde46c41e | -9.4552 | -48.3155 | 2026-08-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| f1318f1e-6d97-3397-86cd-5fa6fc3d806e | -11.3801 | -46.3558 | 2026-08-21 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 2b6038ee-b6e4-3120-9836-a4733e9b1b9c | -6.5828 | -59.0044 | 2026-08-21 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| d57cbd33-9e46-36ae-90c8-4cc6ed8fbae3 | -9.4061 | -60.5518 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a27fb210-0a5e-3ff4-b86e-5f79dd6517ce | -8.9042 | -60.5385 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 184e11cc-5371-3a45-8865-3082a793e56a | -11.367 | -45.9949 | 2026-08-21 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 0f7db093-bf14-3311-af67-ef74d6532c60 | -8.4742 | -46.9609 | 2026-08-21 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8bc8167b-ebc7-3281-863a-5f4c9d8ce212 | -6.1361 | -59.9063 | 2026-08-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 4ba081d0-07bf-3bdb-9525-2190d793cd3d | -15.2263 | -52.8587 | 2026-08-21 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e84f865b-840c-35a7-95fd-23dd709a6620 | -9.4072 | -60.3977 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 21b35524-c7f2-3798-8972-7baa3419409d | -6.5829 | -58.9851 | 2026-08-21 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| eda26a54-91db-3b73-a571-9112b92e4e96 | -9.4558 | -48.2717 | 2026-08-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| eb27a5ff-caba-30ce-a22a-413ee55cbd25 | -5.6168 | -43.9965 | 2026-08-21 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| a20b6d1d-c4f8-3e47-a1b9-51dbc20624d8 | -6.95 | -59.2984 | 2026-08-21 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 022b329b-ca4a-3bb8-b100-cc966bd741b5 | -13.6624 | -51.7897 | 2026-08-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 6f9d8f90-da62-34a1-9043-dcaf25f9f089 | -9.208 | -59.6548 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e118cc82-5163-3168-ad0c-4c17773f702f | -9.4069 | -60.4362 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5c49e800-086a-32bf-954c-37d76e2f3264 | -8.8855 | -60.5586 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| f37f63c2-7e86-36d5-a2a0-ff8a18223daf | -8.9041 | -60.5577 | 2026-08-21 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 2e9eb53c-4a33-3f04-852e-4cbb85534e85 | -7.3637 | -55.5134 | 2026-08-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0ad38715-299d-3376-a820-caaf0ea46cc5 | -9.4549 | -48.3373 | 2026-08-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0d25a191-0b4e-3223-957e-14094c89fda4 | -11.3667 | -46.0177 | 2026-08-21 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ac591a58-20af-33a2-b81b-067d8037b257 | -1.4188 | -55.7282 | 2026-08-21 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a1273884-7f57-3471-833d-92e80237f20f | -13.3929 | -54.3551 | 2026-08-21 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a0d0279d-777e-32ef-9fc9-108caa7cb422 | -8.5175 | -55.324 | 2026-08-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 69e3ee3c-594c-3100-8c57-7d51e38f523a | -9.4555 | -48.2936 | 2026-08-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8b5f3a68-50a8-3ad8-9426-6415a315df2b | -5.7854 | -46.1168 | 2026-08-21 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a518b5f9-e90e-3ca3-a873-c2665f5c7250 | -9.4071 | -60.417 | 2026-08-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.0 |
| fc2a1603-5a92-390e-b8cf-d8717acc502d | -14.3343 | -51.8944 | 2026-08-21 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ca6e5b72-eec9-397d-86f3-38e218de39e0 | -6.2341 | -55.6109 | 2026-08-21 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 73c401ea-ad13-3bc2-8a6e-77c5ad7b16ad | -6.3655 | -58.316 | 2026-08-21 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 57268fe2-7c8e-3c44-8889-1d96f418e70b | -6.583 | -58.9658 | 2026-08-21 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ab9e925e-04cd-3588-a433-a007ae2bded6 | -6.1362 | -59.8871 | 2026-08-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ffd7e160-64cc-323b-89ab-7eb755d3fa26 | -8.3902 | -62.7152 | 2026-08-21 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |


[Clique aqui para ver as próximas entradas](README94.md)
