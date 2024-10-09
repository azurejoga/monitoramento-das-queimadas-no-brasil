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

## Dados Diários - Página 227

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29464aa1-d3d2-35e7-b303-e263d9972383 | -16.9094 | -55.8014 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 5e938b06-bd56-3dbf-a8f7-6f18bb76a32e | -16.9091 | -55.8222 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| d1a081cb-22be-3057-9b7b-d689efec3db9 | -17.0623 | -56.0308 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 162.4 |
| 6301f753-9748-3c65-aa9b-1fa5ca405f9b | -17.0626 | -56.01 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 068b848a-75c4-35d8-aa54-7d368f8c3194 | -17.0819 | -56.0283 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 6bb493a2-d2e8-38f7-b626-6cc1811e78c8 | -17.0795 | -57.3674 | 2024-10-09 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 0446a1be-487b-36c7-8dba-0dbd8bbe030b | -17.0799 | -57.3469 | 2024-10-09 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 93f6f625-e1b0-3de2-b32b-9cfac2ed25ab | -17.1467 | -56.8463 | 2024-10-09 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 2425087f-cfe6-3702-9c4d-7a790eeaa82d | -17.1471 | -56.8256 | 2024-10-09 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 5764cc9d-c7f0-3746-a62f-c7a78f80c4a3 | -18.1193 | -56.3921 | 2024-10-09 07:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| cbc2225e-ed67-3e4c-928b-37699dae61fa | -22.1362 | -48.1461 | 2024-10-09 07:47:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 3806f645-4ee7-33ac-9078-f3573c02fa7f | -22.1369 | -48.1224 | 2024-10-09 07:47:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 19423801-8a29-3d9f-ba15-f36db1f614a8 | -22.1578 | -48.1172 | 2024-10-09 07:47:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a0550ce9-1941-3d18-b75f-95a14da1b9de | -10.8754 | -63.9169 | 2024-10-09 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| d7d5e8ca-b76c-3c89-8829-4b8e3079c703 | -10.8755 | -63.8979 | 2024-10-09 07:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 4fc0a4e8-3aa5-308c-988c-927d970a0c7a | -11.6806 | -64.0312 | 2024-10-09 07:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 28ce5ca6-805d-3ace-ad41-4ab70ed39a0f | -12.6676 | -63.0819 | 2024-10-09 07:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c584963f-3bd5-30fa-9b89-de747aec0576 | -13.3786 | -61.9582 | 2024-10-09 07:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f407040c-ebc1-3655-a679-5f3f072fc858 | -13.3978 | -61.9376 | 2024-10-09 07:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 0c5ccbf6-8ddb-3d58-acbe-9b03ab128624 | -13.398 | -61.9182 | 2024-10-09 07:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b6917cc4-942c-3a9c-80e1-d50c6ff337cb | -15.7076 | -59.3726 | 2024-10-09 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fc8e4f7a-00ae-3416-a241-a702dd67908c | -15.6683 | -59.4163 | 2024-10-09 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dc3571b3-a00b-3757-91bc-715b66a3b742 | -15.6686 | -59.3963 | 2024-10-09 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9af6f4a9-c75d-374d-8ba5-974df272e7fb | -15.6882 | -59.3745 | 2024-10-09 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 698ecbe4-993f-3abd-92b5-3c3b9d804383 | -15.688 | -59.3945 | 2024-10-09 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 77c88ea7-92ef-3259-8646-817f67f93c78 | -16.8898 | -55.8039 | 2024-10-09 07:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| a453f3f4-f5a8-3929-8aa2-9d55798d4288 | -16.9091 | -55.8222 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 3559d7a3-6947-3864-bb3c-67b96797bacf | -16.9094 | -55.8014 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 76618963-4c22-36f0-85dc-37af8c47fb48 | -16.9098 | -55.7806 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a5999de4-c517-3784-afd7-fdea81a3936a | -16.9287 | -55.8197 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| cc7adfac-6dc6-3988-8da8-d8276ee90996 | -16.929 | -55.7989 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| e38fa8fe-6862-310e-a72d-5a2bfab1bc97 | -17.0426 | -56.0333 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 11d737d8-aefe-3532-bbe7-8f77b4337335 | -17.0623 | -56.0308 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 14d50356-96ed-3441-a293-dd0eab2ecb44 | -17.0626 | -56.01 | 2024-10-09 07:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 2d2b960a-87cb-3b0e-a20d-cbbad9dc2143 | -17.0795 | -57.3674 | 2024-10-09 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 576ba2cb-da77-3430-9e53-a705e6c4db25 | -17.0799 | -57.3469 | 2024-10-09 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 028efc05-9e63-33e1-82dc-d304b4773f18 | -17.1467 | -56.8463 | 2024-10-09 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 62876c93-32f4-357c-9b8a-f8be4d696d02 | -17.1471 | -56.8256 | 2024-10-09 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 87f07954-7a35-3493-8593-6da1893e0c32 | -18.1193 | -56.3921 | 2024-10-09 07:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 34f8493f-63b2-3e49-a4a3-23a9a6ab7be1 | -13.94 | -44.53 | 2024-10-09 08:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b40e2a7-1bb7-3588-9031-6de125b74624 | -9.4435 | -67.1008 | 2024-10-09 08:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| ee336b10-461b-3165-af8b-0568b63a9079 | -10.8754 | -63.9169 | 2024-10-09 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 912e31cc-b57c-3b72-ae5f-ae31410c939d | -10.8755 | -63.8979 | 2024-10-09 08:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0097dcf6-9d1a-3e16-9611-532d89c76088 | -11.6806 | -64.0312 | 2024-10-09 08:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 971d9554-b0e9-33bd-acc7-f18902a5f964 | -13.3978 | -61.9376 | 2024-10-09 08:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 70e0f26a-ef71-30e2-8ae3-e2d7cb843b13 | -13.398 | -61.9182 | 2024-10-09 08:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 094a15be-bb6c-3b66-98b9-630c755b8383 | -15.6882 | -59.3745 | 2024-10-09 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 003e8cbe-bfa7-3ad4-8a24-628a9cd7d0ed | -15.7076 | -59.3726 | 2024-10-09 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 46f64e00-61fa-321d-92ce-1b5cc5e74a04 | -15.6686 | -59.3963 | 2024-10-09 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2c409de9-ffa5-33e3-b4f8-6859bb81f91c | -15.688 | -59.3945 | 2024-10-09 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ead42b47-a1e1-3353-b291-f8723b4b5088 | -16.1196 | -56.3521 | 2024-10-09 08:06:37 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 386cdb1f-5aec-3b54-966f-916a7a75efb9 | -17.0623 | -56.0308 | 2024-10-09 08:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 5b4bd493-4842-36ad-a4ab-7afaacbe6ff8 | -17.0626 | -56.01 | 2024-10-09 08:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 6f376f48-9a0e-3447-a420-96d0bfcbed18 | -17.0795 | -57.3674 | 2024-10-09 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 941cb932-9002-3bf3-81d5-3b47c964b9e2 | -17.1467 | -56.8463 | 2024-10-09 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 4d2e9e5e-7294-36f6-b4ee-cb6b75ebcc92 | -17.1471 | -56.8256 | 2024-10-09 08:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 1d6b71ce-c3d6-3c52-8d58-8ed98815c46a | -17.1588 | -56.1222 | 2024-10-09 08:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 09d79a78-1fd8-36a8-a9b7-79db463d89e0 | -18.1193 | -56.3921 | 2024-10-09 08:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 2e4e5ca5-b4c3-3cb6-8735-478c779dfc09 | -10.4287 | -60.9979 | 2024-10-09 08:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| aea7e88a-d373-3295-a8df-018fa9844530 | -10.8754 | -63.9169 | 2024-10-09 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 8e677720-0f04-34b7-8207-cee7a3a8f851 | -10.8755 | -63.8979 | 2024-10-09 08:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 0b1d3608-dddf-3701-9fb0-7cdc5bbe7d8e | -11.6806 | -64.0312 | 2024-10-09 08:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| eee32909-8f7d-309e-9860-0f2b6bc1563b | -13.398 | -61.9182 | 2024-10-09 08:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b856e3da-abf6-3379-9347-d0bb0d488324 | -15.7076 | -59.3726 | 2024-10-09 08:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f834d908-971b-3533-afd3-e073236a2565 | -16.8898 | -55.8039 | 2024-10-09 08:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| bea9b7d6-0e1e-383a-a413-037796e592b2 | -16.9091 | -55.8222 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 69547872-495f-31ba-848e-6ebbc61582bf | -16.9094 | -55.8014 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| e95be9b9-8be1-3d4f-938c-fbdbe3415e12 | -16.9098 | -55.7806 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 1c573912-3120-3c71-818b-37ec2f5cf061 | -16.9287 | -55.8197 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| c0494bd4-db03-303c-a2a4-fa4638974234 | -16.929 | -55.7989 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| d6d6d081-3287-36ef-a8e4-9df7cfb5211e | -17.0623 | -56.0308 | 2024-10-09 08:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 7193c21f-672f-3f71-a850-4cf1c713ecf1 | -17.0795 | -57.3674 | 2024-10-09 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 254e27b2-90a7-342a-be1f-3955a472c70b | -17.1467 | -56.8463 | 2024-10-09 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 9dd98bdf-3500-32d1-bc06-51ced537f528 | -17.1471 | -56.8256 | 2024-10-09 08:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 8253d8e4-a799-3c35-a705-ad1ac67e10c7 | -18.1193 | -56.3921 | 2024-10-09 08:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| f08ba3ad-d1a1-38ee-a83a-5664abf48b63 | -18.1196 | -56.3713 | 2024-10-09 08:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 3ba1d2bc-85b6-318d-aca2-cd4eda84b6af | -10.8754 | -63.9169 | 2024-10-09 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 90b77c02-1ff2-34a5-b836-05d7ae75048a | -10.8755 | -63.8979 | 2024-10-09 08:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 86d7fc29-dd62-3fa9-9a0d-04c0a06220de | -11.6806 | -64.0312 | 2024-10-09 08:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3321d62d-5e2f-37aa-b438-d68b568ee653 | -11.6808 | -64.0121 | 2024-10-09 08:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| f15af62c-56f2-3ed5-b5e7-10c625c79afa | -13.398 | -61.9182 | 2024-10-09 08:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 43.2 |
| a5d276b3-e9c1-339d-8e04-4b286fb9616e | -15.7076 | -59.3726 | 2024-10-09 08:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d66fd43f-50f4-3fec-8856-b9216361b05a | -16.8898 | -55.8039 | 2024-10-09 08:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| b5166cef-2b8e-3994-b812-d3fa04997879 | -17.0623 | -56.0308 | 2024-10-09 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 06db24f2-4c34-3770-891c-b79e6a41e85f | -16.9091 | -55.8222 | 2024-10-09 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| c41ee559-cef9-3e4e-b561-424eda9bad9a | -16.9094 | -55.8014 | 2024-10-09 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| be4f7ad4-58f7-31e9-88b7-a75da8b4ad61 | -16.9098 | -55.7806 | 2024-10-09 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 69e29f04-37e4-3516-9a47-9713f06f56e0 | -16.9287 | -55.8197 | 2024-10-09 08:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| ea757c7f-96a9-318d-a4f6-a34dc5c45d42 | -17.0795 | -57.3674 | 2024-10-09 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| cd2f7c88-88b8-340f-9286-5f95f60cafef | -17.1467 | -56.8463 | 2024-10-09 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| d6fe266e-c70c-3259-85d0-0412ad6e7946 | -17.1471 | -56.8256 | 2024-10-09 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 4a0e563f-7b9e-34e1-80f7-10f62c6ecb46 | -18.1193 | -56.3921 | 2024-10-09 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.8 |
| 49f4b1d0-8374-34cd-be5d-db44ca6d4244 | -18.1196 | -56.3713 | 2024-10-09 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 10623bd5-5632-377d-a0ad-761885f3c2f0 | -18.1391 | -56.3895 | 2024-10-09 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 165.9 |
| 8aabd646-3da6-3e5b-b03f-a81218e63859 | -18.1394 | -56.3686 | 2024-10-09 08:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| c0bc5f1e-0bf9-32a8-82e6-ca85760b796f | -10.8755 | -63.8979 | 2024-10-09 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 4bec7caa-acf7-32f3-8012-6d7bba79373b | -10.8754 | -63.9169 | 2024-10-09 08:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b40f1280-1674-30fd-9b50-04745364e80d | -11.6806 | -64.0312 | 2024-10-09 08:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 361447bc-7247-3eb3-9c59-e2d79eccfd47 | -13.398 | -61.9182 | 2024-10-09 08:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 89bb2765-fda1-3bbe-a7e1-afb58b57e40c | -17.0623 | -56.0308 | 2024-10-09 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |


[Clique aqui para ver as próximas entradas](README228.md)
