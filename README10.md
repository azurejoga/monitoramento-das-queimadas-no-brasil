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
| cd427036-3017-33e8-b0b9-6e361975fe97 | -11.3116 | -43.6664 | 2025-08-31 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3cc65d11-377a-3f30-928d-487f328db369 | -9.4618 | -60.5682 | 2025-08-31 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7387a450-d10f-3dd6-8ab2-469d1f3b059a | -10.6128 | -44.3284 | 2025-08-31 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 227373bb-7170-35dd-be80-7af9b3a63a2c | -9.4495 | -62.3675 | 2025-08-31 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 115.1 |
| eb3bee91-0e04-3ddf-83e1-0d186dc0ad22 | -16.2225 | -52.6565 | 2025-08-31 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 3f699a0e-976f-316b-b6b4-696c9bcc94e3 | -19.0926 | -48.3106 | 2025-08-31 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f3cda013-feda-31b8-a19f-8dadd44358cd | -9.5913 | -40.3448 | 2025-08-31 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 3d20a5c9-f5c1-32da-b75a-728e18339a61 | -19.1128 | -48.3063 | 2025-08-31 01:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e03408e8-9c59-37bb-86b3-2ad733af9186 | -7.1139 | -44.3111 | 2025-08-31 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 35ac720c-87e9-3ed6-93e6-2e6d77e50cdf | -9.4246 | -60.5701 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 917a28a0-179b-375c-b61c-8fe76f00129a | -7.0951 | -44.3128 | 2025-08-31 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4002e55e-3c6b-33e3-b179-ab2219c6be49 | -14.5448 | -51.9943 | 2025-08-31 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 33e17442-37c7-35e8-afa1-03062d58165f | -10.9702 | -50.8489 | 2025-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 008d04b6-f1c3-39a2-909d-ac4265a84a4f | -11.8181 | -46.4314 | 2025-08-31 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 471ba92c-a757-3b69-b8d9-d60c1e83716f | -8.744 | -62.379 | 2025-08-31 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1e074c31-de9f-343e-9e9e-1e5a900b79e2 | -10.3126 | -59.2023 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 184c3fbd-a35d-3c92-b4b7-2dff223ccc25 | -11.3696 | -43.6341 | 2025-08-31 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0e6b852b-f380-366d-a8d7-4918b0376e37 | -13.3636 | -46.95 | 2025-08-31 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 307.0 |
| ec521045-554c-3bcb-964a-6d073ae6f25d | -10.9699 | -50.8702 | 2025-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 469289f8-4be8-3bb8-8d17-909a9875aae0 | -10.7567 | -59.8175 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 89d2e5b2-af4e-3418-af86-cceeb3b95870 | -13.3632 | -46.9727 | 2025-08-31 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 1f9861d5-422c-3f6e-873a-52d7d4dbc492 | -9.0799 | -65.4349 | 2025-08-31 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 3e3644d2-2b70-38e5-880c-64d422a10bba | -13.3443 | -46.953 | 2025-08-31 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fd111e93-7b63-3fcb-9b8b-668fd6cb879a | -8.6538 | -61.9647 | 2025-08-31 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0ac0180f-242d-3855-a615-4231c560f948 | -11.4233 | -63.2444 | 2025-08-31 02:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| dcd1af71-123b-3390-b584-bac897dda9d5 | -12.3099 | -45.7 | 2025-08-31 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2881573a-e252-38b7-8212-1fe269d98661 | -3.5995 | -47.5142 | 2025-08-31 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d780dc77-78f8-339b-bd8d-73d8b41b7df3 | -9.4683 | -62.3476 | 2025-08-31 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 3f9b2af1-06f2-3e96-a76f-7758fda48d2b | -19.1128 | -48.3063 | 2025-08-31 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1525bd06-9dca-3215-aae2-94c24a8b0350 | -9.4432 | -60.5692 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 8a37a95f-733a-30d3-aef6-c9f21087bfd7 | -19.0926 | -48.3106 | 2025-08-31 02:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a4664a4f-2761-37cf-89e1-0ef80b582770 | -11.8357 | -46.5194 | 2025-08-31 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 36337e34-f92d-38a3-a67d-53c252267861 | -14.5452 | -51.9729 | 2025-08-31 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 604ef06c-be04-3c61-9f70-404c814947f2 | -16.2221 | -52.6778 | 2025-08-31 02:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fa59cfd2-bd3e-3eac-85b6-abc317a4f560 | -9.0614 | -65.4355 | 2025-08-31 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 74042d46-44fc-3968-88db-9be57ab4abb1 | -11.3701 | -43.6104 | 2025-08-31 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 76ef31b2-f755-386a-8f7f-5c3aafd738aa | -11.4044 | -63.2644 | 2025-08-31 02:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 94e7edba-be43-3425-b4ec-4f80783221d2 | -6.7093 | -51.4165 | 2025-08-31 02:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 33a8ce92-d979-3281-aa64-ec9ec3d8cc98 | -16.2225 | -52.6565 | 2025-08-31 02:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| aec9159e-41fc-327c-b82b-a7a41e0d5df7 | -9.5913 | -40.3448 | 2025-08-31 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 3a688445-b4b5-368d-a7f8-78fdf7c7a9b9 | -11.4232 | -63.2634 | 2025-08-31 02:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| aa0749e0-51df-39cd-ae36-4e667d66a569 | -12.3095 | -45.723 | 2025-08-31 02:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4a8e02e1-686f-3e93-b5e7-fd2ea9e40032 | -11.4045 | -63.2453 | 2025-08-31 02:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| c6bea2ea-089f-3953-8fd3-92cecfc7c55c | -11.3116 | -43.6664 | 2025-08-31 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| db3a7fc7-ee6e-3f5a-861b-eccc68281b2e | -9.4497 | -62.3485 | 2025-08-31 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 661500c3-dca6-3190-9fde-ea9a51798576 | -13.383 | -46.947 | 2025-08-31 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 222cc65f-d4a5-3677-954a-6da80569214e | -11.3509 | -43.6133 | 2025-08-31 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 61762774-f0c5-3228-be94-b37a949a6e10 | -18.672 | -49.0793 | 2025-08-31 02:00:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c8539cab-06ef-3114-8e68-80dca6853321 | -6.1665 | -43.3273 | 2025-08-31 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| beadc2f4-36b3-3ab5-8bd1-9a01eae7451a | -9.4681 | -62.3667 | 2025-08-31 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0c5f7c9e-df82-3dc9-8dc5-d023af8ded1e | -9.4431 | -60.5884 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0a1f56d7-0592-370a-9993-cb46b8aa07fb | -7.1139 | -44.3111 | 2025-08-31 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 521cd74b-d08c-3335-9e8c-e5d89aaaf455 | -8.7439 | -62.3979 | 2025-08-31 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 2bf82451-49bf-33db-8648-3c7fcc3c16cb | -9.0615 | -65.4169 | 2025-08-31 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ffb8415d-6cec-3341-b5bd-3662f4f5fad9 | -10.3313 | -59.2011 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d395aa6f-f265-377d-b1d6-f86890799ef9 | -6.1853 | -43.3257 | 2025-08-31 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 78a6310a-154e-3cc1-b0f8-a1c35b4ff408 | -9.4618 | -60.5682 | 2025-08-31 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3ba8aab1-1eb6-3457-a7b7-db24220ae79c | -11.3504 | -43.637 | 2025-08-31 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 2a841432-22e4-306d-a6da-cde7de566ce7 | -9.4495 | -62.3675 | 2025-08-31 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 122592ec-3617-3aa4-bc9a-89138123076d | -12.0976 | -44.717 | 2025-08-31 02:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 395737ed-b12e-3568-8cb1-e813a887f3b9 | -12.43135 | -63.92162 | 2025-08-31 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 9f5249a4-a282-31a6-b1a1-3ec92ab17acb | -12.43726 | -63.91491 | 2025-08-31 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ed318a9d-b7ff-392e-9251-4492e7446662 | -12.44133 | -63.93855 | 2025-08-31 02:06:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e4501b15-a149-3d1b-b4ba-3c7b1472f14d | -8.69064 | -62.4247 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e46c6939-ce24-31ce-8713-058efacb5953 | -9.06229 | -71.25693 | 2025-08-31 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2fc5d8a1-4577-3b15-beb3-5c8e29cfe25e | -8.74545 | -62.4084 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 0d7a3ab8-766c-3e95-96d8-57173100222a | -7.74841 | -72.74884 | 2025-08-31 02:09:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3477946-8b43-3bfa-a81d-256084e26559 | -8.73904 | -62.37164 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3ae29d31-fc2c-3c58-83ee-c0af32a93115 | -8.75054 | -62.37689 | 2025-08-31 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 35.7 |
| c39c9c06-dea5-317f-960f-e94a78ed3d3b | -8.65201 | -62.8308 | 2025-08-31 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 31f7914d-5c94-3631-b1a4-c92875693db6 | -7.4641 | -70.13307 | 2025-08-31 02:09:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5014d094-7f11-361b-a647-2255950ae4bd | -8.74014 | -62.41633 | 2025-08-31 02:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c18758c5-c758-3e20-bc88-d73654b8591c | -7.74719 | -72.73995 | 2025-08-31 02:09:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0328e2c6-9be0-33a3-a06e-c6ae102e322d | -9.67954 | -65.0339 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a0208ffc-6c1c-3564-8e91-b7618e96afd6 | -9.46105 | -62.35104 | 2025-08-31 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 366.8 |
| 38b394e0-5762-3022-b798-aa802875e61d | -8.68513 | -62.43078 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 390fabcd-ab2d-33f0-9c23-2ea92a1987f2 | -8.66867 | -62.43379 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 0c1ef680-ffd7-39db-af7b-84b7cbc4cbc0 | -8.64708 | -61.9674 | 2025-08-31 02:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 3b8074b6-7aca-389f-8d27-77f3c87f49aa | -9.46718 | -62.34256 | 2025-08-31 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ef7d7ead-523e-3a54-bedf-7c935e9ed0d7 | -8.67416 | -62.42758 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ffda095e-763b-3e47-bfb5-f579e5624529 | -8.734 | -62.37971 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b4a7e8dc-0fd6-3d29-bf45-402199fd315f | -10.30511 | -68.27081 | 2025-08-31 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 17.2 |
| eb6f4371-99e5-3c20-9882-8f2eec43803e | -9.5689 | -66.68811 | 2025-08-31 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8c065e75-8dc9-3558-9584-2f6d8e921e89 | -10.30327 | -68.25866 | 2025-08-31 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4419aa96-46ad-3122-8624-28b4b39d6a67 | -9.27741 | -67.64672 | 2025-08-31 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 517203b9-84fa-34f0-b799-e5e88a913cea | -8.98002 | -70.74374 | 2025-08-31 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 20875e70-2442-3f78-9bf3-f9b50a772326 | -8.87185 | -71.27835 | 2025-08-31 02:09:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aeb6169d-d23a-3105-a7ed-32f2799f4d5d | -8.23595 | -72.81231 | 2025-08-31 02:09:00 | TERRA_M-M | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 49bbcdc7-627c-3023-8e02-f3329c50457d | -9.26656 | -67.6484 | 2025-08-31 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 96ef4b36-8a06-32b8-a031-7c50f38e260e | -8.38467 | -70.83627 | 2025-08-31 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 26374b8e-db71-3558-b4b4-142c0b7df7eb | -10.11918 | -67.65398 | 2025-08-31 02:09:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b2b4e2d-7d71-3f47-bfcf-0971a2ff3379 | -8.64453 | -61.97292 | 2025-08-31 02:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| ffd14d51-ff38-357b-8e1c-40e6628f4bd5 | -8.65997 | -62.83633 | 2025-08-31 02:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ce6060d0-60d0-3f07-a0cb-cee9362026c0 | -9.43863 | -62.35999 | 2025-08-31 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 1cc8a7b2-7cf0-3f86-8c1b-0d157c60b47c | -9.44469 | -62.35384 | 2025-08-31 02:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 130.2 |
| b163750d-12b7-3ebb-a888-bd99c4921525 | -6.91948 | -71.75121 | 2025-08-31 02:09:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e007f6b-35b1-3589-a02b-1e9afc6bcb68 | -6.1665 | -43.3273 | 2025-08-31 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 06db10b9-94c3-38e4-a725-0d07a3adb22d | -11.8181 | -46.4314 | 2025-08-31 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4f8e4f09-1ce9-347e-875f-97ccd195bade | -10.9705 | -50.8276 | 2025-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 6044226e-485c-310a-87ea-acb1b77aba63 | -6.1853 | -43.3257 | 2025-08-31 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |


[Clique aqui para ver as próximas entradas](README11.md)
