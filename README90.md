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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49d85268-dde3-3fa7-a2f7-b34ddf923ebe | -6.8755 | -59.4364 | 2026-08-21 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7fdc4250-1de7-397a-a0a5-31b5a10235e4 | -17.9546 | -44.3882 | 2026-08-21 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 715a0a43-2932-3ec8-a876-aae98f223478 | -5.6168 | -43.9965 | 2026-08-21 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e46653d7-904f-3803-9b17-f935e4e4ebbe | -6.1177 | -59.9069 | 2026-08-21 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 85738f7a-98a0-301f-90da-4259eeffcc0d | -6.2487 | -48.6506 | 2026-08-21 12:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c57a4dc7-656d-3cb6-b811-ad76e6a01d2a | -16.7194 | -47.6887 | 2026-08-21 12:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 05959bfb-7eda-33df-b5e9-d285e53af10a | -22.8482 | -49.3487 | 2026-08-21 12:40:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 113.2 |
| cc950bca-aab2-37a6-a827-aad0b1e39901 | -5.598 | -43.9978 | 2026-08-21 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 307.8 |
| 3be12530-69e4-3e82-b47e-b0cd86debb18 | -14.7346 | -47.1354 | 2026-08-21 12:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 269dd99e-10a0-3530-9349-055474dfb7b5 | -6.8755 | -59.4364 | 2026-08-21 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3c728d23-efc9-34a4-b8bb-03e1e792ddf8 | -6.1177 | -59.9069 | 2026-08-21 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 824191f6-dbcf-3e4b-9fce-4590e57286a4 | -6.857 | -59.4371 | 2026-08-21 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 109eb938-41b4-33a8-bf01-58e66b895c9d | -6.2487 | -48.6506 | 2026-08-21 12:50:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| df671f76-4204-381d-afa7-5b744432d5d5 | -8.8856 | -60.5394 | 2026-08-21 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 08c65966-983a-3018-90e8-5f6401c0a489 | -11.175 | -54.001 | 2026-08-21 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 11dbb61c-767d-361a-89f2-48a954c2f9fd | -5.598 | -43.9978 | 2026-08-21 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 350.1 |
| 725a1990-b8d4-3016-bcff-862303f3f59c | -14.3343 | -51.8944 | 2026-08-21 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 0bfdc7d1-23f5-369a-8970-3ca2772152a1 | -14.3149 | -51.8969 | 2026-08-21 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| afc578eb-0a61-3083-9e7e-6e6c2869596b | -5.6168 | -43.9965 | 2026-08-21 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 93846b66-adb0-39d6-9fe7-49b59f1f8478 | -8.9042 | -60.5385 | 2026-08-21 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 14527e59-c87a-3a46-b3ea-14e2ac1523fc | -5.6166 | -44.0196 | 2026-08-21 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 1994848c-4eb4-3900-80a1-e50c088b876f | -17.9546 | -44.3882 | 2026-08-21 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b0d9f3f3-d838-35ff-8908-8c5e0c1e5dd2 | -13.6624 | -51.7897 | 2026-08-21 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7132209d-17a3-398d-8876-6db5dacdb8a7 | -6.8756 | -59.4171 | 2026-08-21 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1a3c9e3c-a477-3e11-ae93-a1bbf01ce3d0 | -22.8482 | -49.3487 | 2026-08-21 12:50:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 17b70da3-4b48-3f16-9048-743a40ec15a8 | -9.4071 | -60.417 | 2026-08-21 12:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| dafe7352-7ba7-3c65-acff-18872c8da0cf | -19.6591 | -46.0388 | 2026-08-21 12:50:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 1227d90b-95fd-34b2-ab0b-b2dcc681533b | -11.1747 | -54.0216 | 2026-08-21 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 943c1d3b-93b2-30f5-a697-7d33094d4932 | -6.1361 | -59.9063 | 2026-08-21 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 01984ff8-7b3e-3350-ac4b-2fc0561cdc99 | -8.9041 | -60.5577 | 2026-08-21 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 2bfb1e23-bf1b-3fce-94f6-cb50151cc076 | -5.598 | -43.9978 | 2026-08-21 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 423.0 |
| c1de92eb-047c-3714-803c-d57ba4db5dfa | -6.8756 | -59.4171 | 2026-08-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ee64b2fd-6f18-363e-bc3b-b211824a4c23 | -6.8755 | -59.4364 | 2026-08-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 1f254eb7-b8b6-3e16-a785-8cea85adb566 | -5.6168 | -43.9965 | 2026-08-21 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 557577e2-392b-3bb1-9463-1cded1c83984 | -13.2427 | -51.6508 | 2026-08-21 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 19ade5ea-418b-363d-b73b-a4a38afa8b83 | -13.2431 | -51.6295 | 2026-08-21 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f3968d56-21e4-367e-94ca-e8e14cd2db13 | -13.738 | -51.8651 | 2026-08-21 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 773127eb-ba36-33e0-b65b-e199cfc9dad1 | -11.1747 | -54.0216 | 2026-08-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b6ccf14d-8c0b-3ec3-9d45-82367057b905 | -19.6591 | -46.0388 | 2026-08-21 13:00:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 4bdbd728-b298-38c9-9a70-217fe9e9e657 | -6.2673 | -48.6494 | 2026-08-21 13:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| f516356e-50bd-3378-9be1-b45276894620 | -8.9042 | -60.5385 | 2026-08-21 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 90c306dc-74c1-3507-9f1b-9ccf5edf422b | -9.4071 | -60.417 | 2026-08-21 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 09404e3c-f082-3c05-8757-df5971aa0afc | -5.6166 | -44.0196 | 2026-08-21 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 379605e9-5e7e-302d-bb9b-502b70e7c2da | -6.857 | -59.4371 | 2026-08-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 255a9322-b339-3def-a5fc-7cd63ac8bfe4 | -14.3343 | -51.8944 | 2026-08-21 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 39a7b424-64db-38eb-a3cd-5cf361b58bcf | -6.1361 | -59.9063 | 2026-08-21 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4e8144e5-c445-3a1d-937f-800150b8c6d8 | -6.5828 | -59.0044 | 2026-08-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 71180c01-9275-3a18-be84-c549c33eb639 | -17.9546 | -44.3882 | 2026-08-21 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 98bca3b4-ddc9-32ff-800e-5ff878c9982e | -17.9345 | -44.3929 | 2026-08-21 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 98873ebe-d787-378d-925f-083b2eaf0cb3 | -6.5829 | -58.9851 | 2026-08-21 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f1cfb5e9-56f7-3a04-996b-9252b8840ae5 | -6.2487 | -48.6506 | 2026-08-21 13:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a86fb650-91c5-3e84-b46d-8f6501e15d22 | -11.175 | -54.001 | 2026-08-21 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 16a96365-720e-3972-90b9-f30aa1d183c4 | -13.7384 | -51.8438 | 2026-08-21 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0565202a-de5c-3d00-8b90-8bbde1daf6e5 | -6.1177 | -59.9069 | 2026-08-21 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 0845f6ae-162f-33f6-8a3c-a66cb9106e48 | -20.6802 | -45.2557 | 2026-08-21 13:00:00 | GOES-19 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| 7c5e11bd-83e6-39f8-acad-ff81525a740a | -14.715 | -47.1387 | 2026-08-21 13:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 56036f1d-fc88-3231-a49f-0fee32da4133 | -19.6795 | -46.0339 | 2026-08-21 13:10:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 095c277a-2b4e-3f61-844a-30ff70f0c292 | -6.1361 | -59.9063 | 2026-08-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7c2043c0-6bce-3c35-adcf-461519b547da | -6.8755 | -59.4364 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 34e7c433-c865-375e-b9b5-7e3820315073 | -9.4071 | -60.417 | 2026-08-21 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 37c919a4-298f-38e8-9bdb-f04406de37ba | -8.3718 | -62.697 | 2026-08-21 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e1e922cd-0919-38d4-b0e4-e216c665356d | -17.5978 | -45.8002 | 2026-08-21 13:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 26dc19b2-82ed-3fe9-a3c0-b20d64a005fa | -8.3903 | -62.6963 | 2026-08-21 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 28e22cce-9e78-31e1-a711-7d5ffe3cb37d | -6.857 | -59.4371 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0341cbf3-9a79-338c-b1c8-b993e44ceb75 | -8.8855 | -60.5586 | 2026-08-21 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| cd1fdd1e-32b4-3099-87a4-0b2cf4db5149 | -12.7797 | -48.3983 | 2026-08-21 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| aa2c9e6a-40c5-3a36-a314-82e079a821d8 | -6.2673 | -48.6494 | 2026-08-21 13:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 170555f0-f018-3b4d-a099-550aee38e466 | -19.6591 | -46.0388 | 2026-08-21 13:10:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 79f5aefd-7f90-39f7-8bcc-856e37f1146a | -6.2341 | -55.6109 | 2026-08-21 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1e391a76-cf50-34ba-b99c-6927126ed840 | -6.5828 | -59.0044 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 76a9f6d9-e2c6-3ef2-ab50-a9edfd233dad | -13.3926 | -54.3758 | 2026-08-21 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e82f9f30-9afb-3076-bc0c-239e23aeb134 | -11.1747 | -54.0216 | 2026-08-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 657ee7e7-7abb-36da-bc50-7afc447d70cf | -6.2487 | -48.6506 | 2026-08-21 13:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1a4559f5-e245-3449-bc49-0a1685289cb4 | -6.1177 | -59.9069 | 2026-08-21 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| de6592d6-9c5a-34b0-b489-962db2fdc1f2 | -6.8756 | -59.4171 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f6372f80-8551-3909-9df9-7456e4af65ab | -8.9042 | -60.5385 | 2026-08-21 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fce82669-4bf0-302d-b0bc-450b573e7cd2 | -13.738 | -51.8651 | 2026-08-21 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 5ae9dd63-9389-3398-bfb3-ac44b252699d | -5.598 | -43.9978 | 2026-08-21 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 388.5 |
| f008b977-e5e7-3939-be45-b10091bd6a24 | -8.8856 | -60.5394 | 2026-08-21 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 5ba7a16e-7446-3b1d-b298-9ad97334183a | -6.8939 | -59.4356 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a765bfa9-9608-31e2-954b-84effb20d787 | -11.175 | -54.001 | 2026-08-21 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 12c8dce3-05a6-335e-8ba9-a61a1833afe0 | -13.7384 | -51.8438 | 2026-08-21 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 9d172aa4-37ec-3fc2-babc-e253ae63ab23 | -5.6168 | -43.9965 | 2026-08-21 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 4eba05f5-7295-31d3-b69e-9e12becb3e42 | -8.9041 | -60.5577 | 2026-08-21 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ce672ae9-a9a5-3852-a9ea-d4ce0ddcadc1 | -5.6166 | -44.0196 | 2026-08-21 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 388.1 |
| 1471de31-cb58-3715-93d4-589484294b7b | -8.3717 | -62.716 | 2026-08-21 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 25d63769-c8e4-3ee3-8688-b91589b170dc | -13.6624 | -51.7897 | 2026-08-21 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9ca627e2-b626-3dc5-833d-0211f90cf69d | -6.5829 | -58.9851 | 2026-08-21 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c7d8db16-daf8-3416-8d8c-7f9dc3c6be72 | -5.6 | -43.97 | 2026-08-21 13:15:00 | MSG-03 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35cf357b-9b6f-35f2-916f-b852fdcce2f0 | -9.32 | -48.11 | 2026-08-21 13:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5071e22-7bc7-35ae-b4f6-8f2aa95e7b7f | -5.6 | -44.02 | 2026-08-21 13:15:00 | MSG-03 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6beb0737-181f-36e9-a3ca-0a3241ab94a2 | -17.5978 | -45.8002 | 2026-08-21 13:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a58efd63-9392-3efc-9427-ac0d1e136338 | -8.3903 | -62.6963 | 2026-08-21 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 73649a06-9017-38a1-9b0e-e688f0d8fb96 | -6.1362 | -59.8871 | 2026-08-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d08a6926-a44d-3305-af65-99a6c04ddac9 | -9.4372 | -48.2518 | 2026-08-21 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 56443c87-07b6-31a2-b227-51f942822b2a | -5.6166 | -44.0196 | 2026-08-21 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 265.4 |
| b3b9a82e-d35e-3bd9-8394-303c59eae901 | -7.0191 | -48.0323 | 2026-08-21 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2ff4f57c-6c40-3ef9-aa6b-6c75f7a948c4 | -13.2431 | -51.6295 | 2026-08-21 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c0e8d040-1f6e-382e-85c4-df0b8ce9dc6b | -13.7384 | -51.8438 | 2026-08-21 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 80be2e8b-175e-3385-b8a0-e71385b9016d | -6.2673 | -48.6494 | 2026-08-21 13:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |


[Clique aqui para ver as próximas entradas](README91.md)
