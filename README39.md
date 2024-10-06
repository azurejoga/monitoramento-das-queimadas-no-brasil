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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e102aa58-32e4-3691-9c9d-3a925ab66494 | -9.6779 | -64.6269 | 2024-10-06 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2d4473f9-4b39-3864-ab22-ed167bb63082 | -9.6964 | -64.645 | 2024-10-06 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.9 |
| bde6e568-a488-389f-9734-7338c0707ac8 | -9.6965 | -64.6262 | 2024-10-06 03:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a82e6af2-ae41-3654-a8b1-df3d50d7076c | -9.8552 | -60.2966 | 2024-10-06 03:16:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1720ee7a-44f0-319b-8092-119083d68192 | -12.2645 | -41.0969 | 2024-10-06 03:16:14 | GOES-16 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 0f23d751-0a3a-3cea-8ea3-32e46e6f210c | -12.6089 | -53.1338 | 2024-10-06 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 75fefee5-3141-389d-a322-55f2b0527b99 | -12.628 | -53.1317 | 2024-10-06 03:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 81f1145a-3cfe-3452-8fdf-283dd3573e00 | -12.6283 | -53.1108 | 2024-10-06 03:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3efecadd-8248-3154-b10a-ffa5c15b85b3 | -12.6532 | -54.0415 | 2024-10-06 03:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9ce8b558-bc17-3256-b9d1-8fb63ac194c2 | -12.6535 | -54.0208 | 2024-10-06 03:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 20c04ee3-a779-3aa8-a36a-706ff213092a | -12.7439 | -50.5376 | 2024-10-06 03:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3255259e-47c5-3d3b-9085-e4cea5395a2b | -12.763 | -50.5352 | 2024-10-06 03:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 94e9972f-a5e8-3413-8a8f-dfec25d2e05e | -12.7634 | -50.5136 | 2024-10-06 03:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 437bb3cb-c6b4-37fb-87e0-105e48ba05bc | -12.7822 | -50.5328 | 2024-10-06 03:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.1 |
| f0aec3a5-513d-3e67-90e3-77e8c422f238 | -12.7825 | -50.5112 | 2024-10-06 03:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 91e827e0-fa2c-392b-9373-6cd84579cd74 | -13.3786 | -61.9582 | 2024-10-06 03:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c58c1660-e0ec-3711-888b-04171b6fa3db | -13.3976 | -61.957 | 2024-10-06 03:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a69827bb-6a3c-3bed-962b-424c7144e1cb | -13.8943 | -44.6058 | 2024-10-06 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f1f2316c-717e-38f0-82c0-bf38f2182bb1 | -16.7647 | -57.4856 | 2024-10-06 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 0e2c8b84-12d5-3f56-bae6-e146af37b352 | -16.9545 | -56.6226 | 2024-10-06 03:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 0ce51d53-3720-3d6f-8faa-bbe9cf046aaf | -17.0003 | -55.0817 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 045c1ac5-1195-3d9d-a1f0-4aba611210d6 | -17.0007 | -55.0607 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 345.5 |
| 12559269-29af-390c-8b7c-88b5761c104b | -17.001 | -55.0398 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 5d38c27a-8d5a-3a3f-9b4d-dc6c0810d35f | -17.02 | -55.0791 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 92c493fb-cc83-3b05-a42f-4b399ebc4e5c | -17.0203 | -55.0581 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 442.5 |
| ad02171a-730b-3ded-9ccb-8ba5a42066ca | -17.0207 | -55.0371 | 2024-10-06 03:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 1872e9f5-9762-3f32-a3fa-47a5524e6c0e | -17.1182 | -57.4039 | 2024-10-06 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| cd32eba1-9e7f-3c0a-97a6-44f04d2dae6e | -17.1375 | -57.4221 | 2024-10-06 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 2d155ad6-ea93-3c71-be67-ab953f6eaf61 | -18.6387 | -57.2785 | 2024-10-06 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 62b78a89-cda3-35f8-8690-62582c332c4a | -18.6586 | -57.2759 | 2024-10-06 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 087368f6-6170-313c-9318-af59566efc03 | -18.659 | -57.2552 | 2024-10-06 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 0685632f-bee4-355b-9e42-f97dc509d697 | -20.5813 | -49.3865 | 2024-10-06 03:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 5dfb4ccf-d02c-37bc-8217-dd5fb64ef252 | -20.582 | -49.3635 | 2024-10-06 03:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6d4012be-1e01-3a3c-8adb-7f8d4ea6bea6 | -20.6018 | -49.3821 | 2024-10-06 03:17:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5c53f31b-f37d-35d2-bad1-f3d91f0db349 | -20.6024 | -49.3591 | 2024-10-06 03:17:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 85d77770-a827-34f8-a072-84df81aacdda | -21.5012 | -50.9132 | 2024-10-06 03:17:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 8912f55c-ffef-3b6d-a234-ede200719623 | -21.5218 | -50.9088 | 2024-10-06 03:17:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.5 |
| 06ba3cc0-9e9d-320d-8bb5-669f0e0a0591 | -2.8166 | -48.6867 | 2024-10-06 03:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 1af79e19-3222-3f95-8da0-ba56b5c90fae | -2.8165 | -48.7082 | 2024-10-06 03:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d66641f1-74ff-308d-8c82-4a15df2ed4ae | -2.7981 | -48.6873 | 2024-10-06 03:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3662ddc4-5bc6-3a49-8835-24588197ad5e | -3.2329 | -50.8504 | 2024-10-06 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| caa11b0e-e814-316c-a951-393aac69e86d | -3.1315 | -48.591 | 2024-10-06 03:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ea3f42c5-68cb-3b87-88f5-ba9eefe2cccd | -3.1314 | -48.6125 | 2024-10-06 03:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 2d15ff69-057a-3d0c-9cf0-cbe0638609ec | -3.1129 | -48.6131 | 2024-10-06 03:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 1517f613-6571-3638-8d76-80a81264eec5 | -3.4195 | -50.3844 | 2024-10-06 03:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 68afa0f5-31b1-3bd8-8849-7c532fb494e1 | -3.8465 | -46.4492 | 2024-10-06 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2ce479e1-f5b1-3857-bc04-118841bd042a | -3.8464 | -46.4714 | 2024-10-06 03:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 236af0bd-2e69-3713-b92c-a517804c20d1 | -5.0139 | -49.7696 | 2024-10-06 03:25:34 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6fab6791-0e91-3253-b811-b754af1b9ae8 | -9.1449 | -60.6612 | 2024-10-06 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 18838be1-0c0d-3f04-bb7e-279ae44c94df | -9.3647 | -51.0898 | 2024-10-06 03:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 420bb4d1-bc38-3642-ac77-c6b5b2c6092f | -9.3467 | -46.5365 | 2024-10-06 03:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 839b027e-31e4-3770-8a1e-4e4a0f917c3a | -9.3464 | -46.5589 | 2024-10-06 03:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 14900d6d-9e7c-3adb-a0c8-9a2804fe6d88 | -9.3278 | -46.5385 | 2024-10-06 03:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 50e91b1c-47f2-3077-b66e-a97c436bb690 | -9.3638 | -64.319 | 2024-10-06 03:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 49925aa1-ae7c-305f-b157-da6fae516f26 | -9.6883 | -47.8088 | 2024-10-06 03:26:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 58363ffd-cd20-3f97-8505-a847d3ec052b | -9.688 | -47.8308 | 2024-10-06 03:26:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| bd9694ea-f5bd-3522-814e-9dc38852d127 | -9.8552 | -60.2966 | 2024-10-06 03:26:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0384b1d0-1cb5-3ca3-afc2-b5e62ec77c55 | -9.6965 | -64.6262 | 2024-10-06 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 135.0 |
| bb302de6-fbce-36ba-9f79-6f1e49ff4ce5 | -9.6964 | -64.645 | 2024-10-06 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d7ffbeff-2b63-31e0-a584-1a397dcf2e00 | -9.6779 | -64.6269 | 2024-10-06 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 152.3 |
| af155051-3d83-3251-b5f3-61a3b7287e13 | -9.6778 | -64.6457 | 2024-10-06 03:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8cae1c61-0905-37c5-be77-52ac54c711bd | -10.234 | -47.9908 | 2024-10-06 03:26:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e6ff5608-e56e-386c-ace9-7847fee8ac78 | -10.2337 | -48.0128 | 2024-10-06 03:26:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7d385dda-d780-35c9-b0ba-483886060c31 | -10.2151 | -47.9929 | 2024-10-06 03:26:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 367eb392-6781-3227-9b56-1a2f01afddb7 | -10.2148 | -48.0149 | 2024-10-06 03:26:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 272c73f5-d0da-3710-9be8-15a5591fa3c4 | -12.6092 | -53.1129 | 2024-10-06 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e2f7d7c1-f7da-35e0-a5e5-15b74697d114 | -12.6089 | -53.1338 | 2024-10-06 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 25b5d42e-59ae-3d91-bb03-b694937875be | -12.7825 | -50.5112 | 2024-10-06 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d9aa29d2-b8ac-3f92-80b3-d5b9d95c43bc | -12.7822 | -50.5328 | 2024-10-06 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 96bf357e-22df-38b7-b609-0edcd8b73a29 | -12.7634 | -50.5136 | 2024-10-06 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 206.6 |
| a727b7ba-551f-3542-8681-b49dcce3bed0 | -12.763 | -50.5352 | 2024-10-06 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 411.2 |
| 42944137-5a22-39a4-9632-34f6878058c1 | -12.7627 | -50.5567 | 2024-10-06 03:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b8f2cad6-e2fb-36b5-abce-bbc56206ac35 | -12.6726 | -54.0189 | 2024-10-06 03:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ab694aa6-31ba-367c-be2a-9b2dc9901f8d | -12.6535 | -54.0208 | 2024-10-06 03:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ac45fe05-e18b-3df8-8884-185f34d3967e | -12.6532 | -54.0415 | 2024-10-06 03:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 01478074-4c5c-3718-af52-d5e095f7374f | -12.6283 | -53.1108 | 2024-10-06 03:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 97229dac-b104-368a-9832-9071b17cfbfd | -12.628 | -53.1317 | 2024-10-06 03:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| dd49b63b-08c3-3506-aaf4-03364e5e47dc | -13.3978 | -61.9376 | 2024-10-06 03:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f795efa0-5239-3bf5-9e2e-29b728376ec4 | -13.3976 | -61.957 | 2024-10-06 03:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fd4d7e1b-4a13-3f0d-95ef-218d6a4d01f0 | -13.3786 | -61.9582 | 2024-10-06 03:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 170e5ffe-cc7f-330f-bd6b-6a24fe0e4fcb | -13.6724 | -51.1911 | 2024-10-06 03:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 7941489c-2f20-378d-b90c-d27d36f4f2a0 | -16.8238 | -57.4584 | 2024-10-06 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 60a137bf-fd54-39b7-ad21-2205e5285148 | -17.0688 | -56.8145 | 2024-10-06 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 2fd7c1a4-27a6-310a-9ab4-f81644893ab0 | -17.0885 | -56.8122 | 2024-10-06 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| a95be477-a0b6-32ec-8a36-a5f1d4caadd6 | -17.1081 | -56.8098 | 2024-10-06 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 9c17788d-9add-334e-8531-9f5488771508 | -17.1182 | -57.4039 | 2024-10-06 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 26923bfb-077e-3e7e-9e4a-5af207f98dd7 | -17.1185 | -57.3834 | 2024-10-06 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 6ecd6c67-f294-3bd4-ba37-54539e9b3c2e | -17.0203 | -55.0581 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 293.2 |
| a1477bdc-4bec-30f5-9f84-862937453024 | -17.02 | -55.0791 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 247cd0bd-2059-325c-b6c1-c5cbbec6618d | -17.0207 | -55.0371 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 155.5 |
| b3c9ee47-c3be-3f7d-ba8c-f604b41b5cb2 | -17.001 | -55.0398 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| bdee9a42-09ee-360d-a686-5d6d932736c7 | -17.0007 | -55.0607 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 7a3013f3-f815-37bc-8945-26f68c0317f3 | -17.0003 | -55.0817 | 2024-10-06 03:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| ff328d89-debb-309e-9ee5-69dabadbf048 | -17.1375 | -57.4221 | 2024-10-06 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 7e42a0de-f891-344e-95ff-0efaaaac4027 | -17.812 | -53.7859 | 2024-10-06 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 224.3 |
| be58fb5d-1697-3d09-8499-ff856f9d743b | -17.8125 | -53.7645 | 2024-10-06 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 2103979d-6417-33a4-82bb-e10e59a66d1f | -17.8319 | -53.7829 | 2024-10-06 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 7f318e4c-028e-37a4-a85e-5b25b9c183fc | -17.8323 | -53.7616 | 2024-10-06 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 8e4d8dba-c01a-3644-b9d2-a6a0b441bc12 | -18.659 | -57.2552 | 2024-10-06 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 15bbf282-c67a-38a2-81e8-39334f71e1aa | -18.6586 | -57.2759 | 2024-10-06 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |


[Clique aqui para ver as próximas entradas](README40.md)
