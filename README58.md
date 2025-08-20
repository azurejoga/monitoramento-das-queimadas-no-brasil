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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ec8fafb-d590-3829-9602-f079dda52b0a | -10.821 | -43.2903 | 2025-08-20 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 6b88557d-92df-3561-83a4-b0abc9822262 | -10.8214 | -43.2665 | 2025-08-20 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 68ab6a6f-66c2-34dc-9df5-f3730efa18b8 | -20.339 | -51.7062 | 2025-08-20 06:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 627c8b6f-2e89-3ae0-95c2-482e08d3eb1e | -10.7043 | -48.2226 | 2025-08-20 07:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a2c393af-7569-3568-9dd9-dc0aad053e00 | -20.339 | -51.7062 | 2025-08-20 07:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| afb99d1f-481e-3d5f-afc7-4c88eaaf3c45 | -13.1555 | -54.9357 | 2025-08-20 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 3b881780-d1d8-3fb3-8c72-be88efa418c6 | -13.1558 | -54.9151 | 2025-08-20 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 84320590-efdc-3436-beb5-7f1125841348 | -11.6002 | -50.5454 | 2025-08-20 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4046a438-756a-39e6-aac9-abafa9fc2f43 | -10.7043 | -48.2226 | 2025-08-20 07:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 482b45aa-ac1d-3601-b77f-81345e9ad5fb | -11.6006 | -50.524 | 2025-08-20 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 37446922-5588-3d07-ae0b-54aae407d389 | -10.6853 | -48.2248 | 2025-08-20 07:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 38451986-5d0c-3fbe-beca-2261a18e06f6 | -10.7043 | -48.2226 | 2025-08-20 07:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b3d7abcb-6455-3520-9431-c845a03bf3a1 | -10.7043 | -48.2226 | 2025-08-20 07:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 48845787-468b-3fad-a593-edc23e0a2537 | -10.6853 | -48.2248 | 2025-08-20 07:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 969e8f31-c248-3845-a459-8b26af8813da | -8.55925 | -66.93926 | 2025-08-20 07:39:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3e1e8a5d-ea12-34dd-90c5-29a3f2dd9d4b | -10.6853 | -48.2248 | 2025-08-20 07:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0bdee809-215c-3485-99c9-9608c2efd9f7 | -10.7043 | -48.2226 | 2025-08-20 08:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c3d468fd-9f5e-3ffb-a406-d3358cc6f35e | -10.6853 | -48.2248 | 2025-08-20 08:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6dfd0cab-88d6-3905-b304-2936219cffcc | -15.426 | -46.7178 | 2025-08-20 08:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| c92192ce-2c9c-3baf-9452-418a4178255b | -13.1555 | -54.9357 | 2025-08-20 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e5520197-1249-3ec2-8d8c-cf8521397abe | -13.1364 | -54.9376 | 2025-08-20 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2eb5aaf3-71cf-3351-80d3-2661f490c3ed | -13.8743 | -45.5643 | 2025-08-20 09:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 1cddc65b-9dbf-3c82-a8f5-c544340915e4 | -13.8748 | -45.5411 | 2025-08-20 09:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| dacc11a2-eb6c-32d5-a68b-8257f6163c4c | -13.8743 | -45.5643 | 2025-08-20 09:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 74927cd0-5fd4-3024-8129-80849c8c3dc8 | -13.8748 | -45.5411 | 2025-08-20 09:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 77d3c6ef-3da9-3162-ace9-89a47ce68b86 | -13.8748 | -45.5411 | 2025-08-20 09:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| ad765cda-d2ce-395b-b4ec-da807f4b9b9a | -13.8743 | -45.5643 | 2025-08-20 09:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e48cdf69-173b-3018-b11e-8afe239e9808 | -13.8553 | -45.5444 | 2025-08-20 09:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6be15416-c944-38b8-a155-d4a4e1484412 | -13.8553 | -45.5444 | 2025-08-20 09:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 0cac990a-d847-3e57-aace-ee03d070f051 | -13.8748 | -45.5411 | 2025-08-20 09:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 4f6a78c0-9ca6-3af3-ac6e-f567bc1bb3e4 | -13.8743 | -45.5643 | 2025-08-20 10:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| fb9b5b80-9ada-336e-879c-1207c9c2f373 | -13.8553 | -45.5444 | 2025-08-20 10:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| b50a4f2c-fffc-3812-ab49-ca0bbbfb3fd4 | -13.8748 | -45.5411 | 2025-08-20 10:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| d7015ef0-16e7-3b2d-ae79-8e90df81273c | -13.8748 | -45.5411 | 2025-08-20 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 638ac9aa-40b6-3709-a032-b51397c03817 | -13.8553 | -45.5444 | 2025-08-20 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 9dfe8ec7-3cb6-379e-915a-bf69c3eec1bb | -13.8743 | -45.5643 | 2025-08-20 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 768e70e7-9c17-3c33-bd34-7ffaa78fe656 | -13.8743 | -45.5643 | 2025-08-20 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| adc35ccd-d2ab-3fea-b341-1f6febb7ad00 | -13.8553 | -45.5444 | 2025-08-20 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 193.0 |
| ab355373-d340-3597-9a2e-d68f49e97567 | -13.8748 | -45.5411 | 2025-08-20 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| e1db3796-f9a3-32ab-9e97-e8eb04b80ef2 | -13.8743 | -45.5643 | 2025-08-20 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 024f9cb6-f494-324b-8659-e8a58984787b | -13.8748 | -45.5411 | 2025-08-20 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 61bcb6cb-146a-3da3-bd59-0638af55c0f9 | -13.8553 | -45.5444 | 2025-08-20 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| ad704643-abdb-3f29-844c-5e5cd0598700 | -13.8553 | -45.5444 | 2025-08-20 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 8858e586-61ee-3316-85f4-af9c99138e2a | -13.8743 | -45.5643 | 2025-08-20 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9100c477-f469-35f9-bae3-09d55c70c180 | -13.8748 | -45.5411 | 2025-08-20 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 3faac8cc-2ba5-3d91-8d81-125128ff98a7 | -13.8743 | -45.5643 | 2025-08-20 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 160c20c3-f6d3-3531-aba5-ebebaa15417b | -13.8553 | -45.5444 | 2025-08-20 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a7649d0d-cb4d-3564-8c1b-7d14ec8b094e | -13.8748 | -45.5411 | 2025-08-20 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| fc438f29-4fb1-3146-98b3-b0c708e52ac2 | -13.8553 | -45.5444 | 2025-08-20 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 015e105d-0428-3b7a-8ea8-8a98650bf14b | -13.8743 | -45.5643 | 2025-08-20 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 71fc7207-89fa-3969-8957-1dbb6ee083a6 | -13.8748 | -45.5411 | 2025-08-20 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| c7eda969-5a0b-3d11-931e-eab8ebad1e91 | -13.8748 | -45.5411 | 2025-08-20 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| d9fc716a-819e-38c0-9d6e-f0ed5075d12d | -13.8553 | -45.5444 | 2025-08-20 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ccaed184-f2b6-3c98-9ed3-0b1b8176ee5d | -13.8748 | -45.5411 | 2025-08-20 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e8e91c2a-d12f-3e43-afc0-0796bc18de9f | -12.6698 | -44.9525 | 2025-08-20 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 78e5b499-509b-345d-ba0f-a9346e994cde | -12.6698 | -44.9525 | 2025-08-20 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 45b9375a-8aa2-3df5-8f56-b0d47f0bf2bc | -13.8748 | -45.5411 | 2025-08-20 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0ae50049-4f9d-3b96-ab04-4218b50ef16a | -13.8748 | -45.5411 | 2025-08-20 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d6552965-c783-373b-abbe-288f7b330a43 | -10.7043 | -48.2226 | 2025-08-20 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8b0f4764-5bb8-3d2b-a683-aa3c19679386 | -12.6698 | -44.9525 | 2025-08-20 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8e91b937-792d-3283-a590-84dd41391b73 | -12.9925 | -45.202 | 2025-08-20 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 91c82988-7ac4-3510-9374-b724c5145861 | -13.8748 | -45.5411 | 2025-08-20 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 293bee65-cb43-3254-8246-1b5b7a96b236 | -6.9607 | -42.858 | 2025-08-20 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| d3dc827a-00d8-3ad2-b612-8038ad3b656f | -12.6698 | -44.9525 | 2025-08-20 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| d25d137c-d9d7-3613-8ab1-50fc01a30d4b | -13.8748 | -45.5411 | 2025-08-20 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8acac41e-a127-3957-894f-4ceed25758e6 | -10.7043 | -48.2226 | 2025-08-20 12:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2291086d-3a77-36d1-a962-ad1b37eebbd4 | -12.9925 | -45.202 | 2025-08-20 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d376497e-8456-3642-b22a-cc5c329ad493 | -13.3346 | -54.4233 | 2025-08-20 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 43d0708c-a09d-3935-99b2-d8a8f0c072dc | -6.9607 | -42.858 | 2025-08-20 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| c893980b-c353-333c-adfa-20dc0fc12bc9 | -5.9711 | -44.1542 | 2025-08-20 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 197244b1-0037-33f5-8c7f-48bb0beb0f21 | -5.9713 | -44.1312 | 2025-08-20 12:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 90f79731-81ff-301e-b3e5-c91dbadabcb4 | -12.9921 | -45.2252 | 2025-08-20 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 61c26700-b6cc-3ff7-8fa1-d23db35d740b | -12.6698 | -44.9525 | 2025-08-20 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 703afb57-fa77-3142-a391-05000360e405 | -6.9605 | -42.8816 | 2025-08-20 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| ea59e34f-f5c2-3823-a032-52c9d4285936 | -13.8748 | -45.5411 | 2025-08-20 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e1ee21da-e958-3605-a8de-de4f3cf1c2d7 | -10.7043 | -48.2226 | 2025-08-20 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7d6a93cb-ca4a-3e08-bef6-87f202db0c7e | -12.9925 | -45.202 | 2025-08-20 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 239.0 |
| a4da7826-9c27-3f65-8546-ced5fb28d75d | -13.03067 | -46.80263 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f9c508dc-a4c5-35db-9783-2d4046d54a24 | -7.15593 | -43.49407 | 2025-08-20 12:14:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 50.7 |
| bba4f34b-16c3-3220-8aa2-744daa728717 | -10.69486 | -48.23566 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| d8d47e7f-4475-32ac-991a-b29228678559 | -6.10772 | -45.41381 | 2025-08-20 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 49fd7c8b-b637-3927-a119-82b7c99280e0 | -6.09957 | -44.6414 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e82d9be-1f7f-3336-ad48-0db7ee7695e7 | -4.17513 | -42.03068 | 2025-08-20 12:14:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 6eb57368-7e66-3921-919d-45895d6b721d | -10.99204 | -45.90039 | 2025-08-20 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9843338c-1d3f-37aa-9251-cbdc6764056c | -13.40807 | -46.35172 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 74595ca2-4faa-3cfc-a6b5-ab322e6b0f1b | -6.53666 | -45.51424 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 268cf580-8c28-3846-8719-ca9788303ac4 | -13.53384 | -40.69901 | 2025-08-20 12:14:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| aefd20d7-e604-32eb-bfbe-834ee22f88f8 | -6.62333 | -43.8762 | 2025-08-20 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 1d5cfa51-a4fa-3664-a5cf-ab4feb06d2fb | -10.82469 | -43.27299 | 2025-08-20 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 8623be3f-ef1f-39f9-8ce0-d11b0923c619 | -13.17417 | -46.8849 | 2025-08-20 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 883f065a-7dd9-32ed-abb2-1b8f24e004ee | -6.65457 | -43.055 | 2025-08-20 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3cda2c9b-c2e7-3bec-b7b4-1950ff5e5bb1 | -12.61935 | -46.89482 | 2025-08-20 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa067bc2-1a5b-3b71-85d7-281f89577543 | -11.79979 | -44.28358 | 2025-08-20 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8f43c8c0-9eb7-31d1-b761-3f633afe44f0 | -6.44457 | -45.45025 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 64c8a817-b055-31d9-81ba-d34f2c48d683 | -4.9173 | -43.22955 | 2025-08-20 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1827b921-4456-366d-b30f-e49302311d4f | -13.53122 | -40.69316 | 2025-08-20 12:14:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 7a3a0af1-6996-3af7-9965-eb8591b11b7b | -7.6722 | -45.2538 | 2025-08-20 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c776a4f3-71f8-3434-80c2-422a110e21de | -12.99695 | -45.21029 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8fbbfeb2-8ea9-3f13-81ab-d5b18d25cad8 | -7.27594 | -50.18734 | 2025-08-20 12:14:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 93a93dab-47d9-3f7d-8914-fa18f74ebd15 | -9.5257 | -47.23034 | 2025-08-20 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |


[Clique aqui para ver as próximas entradas](README59.md)
