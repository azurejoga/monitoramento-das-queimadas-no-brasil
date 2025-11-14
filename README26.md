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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d910fa51-b19f-3afa-9e50-29854c54165b | -1.83572 | -53.7976 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd7e5ad7-7bf9-34b1-a558-082fd58738f1 | -7.55257 | -47.24469 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 565b9cc9-58ba-3fa1-a376-bca4879d5f65 | -7.93578 | -44.32592 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c2db261-8acb-3e59-8572-783cba8f835b | -7.47092 | -42.57926 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d6375ef-58c4-37c6-b4ca-e949fc1b5e44 | -9.31209 | -47.83461 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2aebb92-a50b-31da-8694-b872fa1dcdd9 | -3.47611 | -45.65298 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3600e41d-86dd-38e7-ba3b-103e68d1e99b | -7.02288 | -46.43443 | 2025-11-14 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e51beac8-bd24-3dfe-99f9-98dd8002ebcd | -7.39253 | -48.65426 | 2025-11-14 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a1c66c4-ed52-34b2-b430-8f52e4447e4b | -8.58878 | -44.11235 | 2025-11-14 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f04010f-0210-331d-90c6-03e291e516c6 | -3.25067 | -42.05927 | 2025-11-14 04:23:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70d49f5f-820a-3003-8684-137c15dc3c25 | -10.70055 | -44.492 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 429affd0-c9a1-38b0-9894-0efae1036124 | -7.93299 | -44.32189 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ba42f2-ac5a-3c34-bed5-b1775728c9ab | -3.24408 | -44.31883 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d9374d3-18ca-347f-b0a5-4471ff303667 | -6.88104 | -47.24624 | 2025-11-14 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 296600d8-75af-3515-822f-b28b3d625296 | -3.16752 | -42.97593 | 2025-11-14 04:23:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb6d8c10-acf0-3116-a3ad-471df9e772d7 | -1.10638 | -52.59609 | 2025-11-14 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3fce33c-5e9f-3ae5-8942-6191d438cd70 | -7.9266 | -44.34613 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9dcb7ce-e41f-3e9e-99a4-fe9f02acdec4 | -7.66693 | -45.87923 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c59a51a-9e61-3c68-bc77-e0143a18e39a | -7.8582 | -44.30301 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0557e13-feea-3dfe-8121-ccd48647218f | -1.83705 | -53.78976 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e113efa8-6c28-31a7-8690-24e3cba2b1b2 | -4.09782 | -44.16347 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1776077c-2f82-3d50-b16c-29f536fed98e | -10.32026 | -44.27351 | 2025-11-14 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9732a407-dfcb-3700-a2ae-341f085b5e82 | -3.98011 | -44.65155 | 2025-11-14 04:23:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93dc2817-2bcf-3139-8d20-d4e06819cfa6 | -4.07178 | -44.13463 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e999f5ba-ac52-3bb0-a34f-7c2e99b997fa | -7.67361 | -45.88033 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9fd6dd2-c4fd-3ec9-920a-8c0db501f498 | -7.92825 | -44.33561 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02def005-087e-318b-bf93-3c55bcdead87 | -3.34905 | -48.38787 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98639f96-5d1a-39c1-bade-318ba909d2e2 | -1.83439 | -53.80545 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a915466-9d85-3f78-8e6c-e6f4e355c12e | -7.45172 | -42.56441 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e624e2d3-9222-35d3-806b-67c4f5cbcd22 | -8.63658 | -46.69613 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ca65452-0939-388e-9642-478db34ea86c | -5.16023 | -37.57676 | 2025-11-14 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 10a23bd1-1e6a-30fb-8ce9-969092395991 | -10.92429 | -44.58925 | 2025-11-14 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| affb8f51-b485-3994-a499-27ea73aa32ae | -10.37321 | -47.68722 | 2025-11-14 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 595757dc-45d7-3a99-9b7c-d05613bd6417 | -4.71405 | -40.81263 | 2025-11-14 04:23:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 676b6343-7f24-3af8-9c10-64c61b12020f | -2.94175 | -49.3632 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ca734c33-4432-34a5-9901-8163907fb9c7 | -8.53952 | -49.58377 | 2025-11-14 04:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1885fa50-49ec-3508-8202-1e10a1787b1c | -4.60475 | -43.35341 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e1fb037-7314-3835-98d6-199fced34c97 | -11.17313 | -43.57539 | 2025-11-14 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7830735e-f700-3126-b5c9-9b5edad38726 | -2.88407 | -49.47879 | 2025-11-14 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645ca911-2114-3ec3-86a2-f60f67888af0 | -4.57543 | -43.16824 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37dffe9f-337f-34a3-b7f7-bd00936a9d56 | -4.57534 | -43.12467 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 868596c5-f7e1-388a-b3dc-1c6e3f2351d0 | -3.41613 | -41.18288 | 2025-11-14 04:23:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80e5410d-7b6a-3b62-a883-25d4cabb196f | -3.98661 | -48.00272 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3912cf1d-58e2-3822-a3e4-5acc3537416e | -7.45521 | -42.56495 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ef4ec12-7e3b-3f0a-8a6a-c2b8aafff877 | -7.86432 | -44.30757 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4745b454-a4fb-3cf8-bbfa-e0505974c7a5 | -3.25372 | -43.29008 | 2025-11-14 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdee2d0e-31d7-3724-92b4-22e661396833 | -4.10481 | -48.01299 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae524184-5afb-367f-9408-464375908d76 | -7.46106 | -42.54988 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36005593-b411-367c-8ad8-c91eca7757f9 | -7.93419 | -44.35802 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c04d92e-b94c-30ca-8560-246724b7a8c2 | -2.23779 | -46.07319 | 2025-11-14 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4330da39-6c03-3578-8ae4-d7088efbd94f | -9.05201 | -48.71701 | 2025-11-14 04:23:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21b0b7c9-a074-3ea4-8f01-eb49ee20b859 | -4.45382 | -43.21116 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0029e19-3190-3afc-a5b0-5bd934866d61 | -9.21786 | -45.1881 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85654ff1-394f-3683-a531-cc54390913e6 | -7.84263 | -44.29336 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 51b6f0a2-a1d6-3f63-8b32-ea2c5937ed34 | -3.63091 | -49.11315 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336fc5a4-077c-30a4-a188-c2a6470e5b18 | -2.45352 | -48.81743 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab42699-2fef-3e93-aa03-34956065e604 | -4.74799 | -41.07986 | 2025-11-14 04:23:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87f9d8c7-114c-371e-98ee-891d5da9be08 | -3.30497 | -42.4054 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee6282c0-a33d-310f-8399-2c1e4e098097 | -1.83506 | -53.80152 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c57a2dc-133d-331d-8c8b-534c5263a6f9 | -7.53866 | -45.8553 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 905b279b-9f2e-396f-b51e-9fa95f91ae70 | -9.85807 | -44.16529 | 2025-11-14 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 261785f6-6a0b-3979-acc0-fcfc8f20c0d8 | -3.62804 | -49.1053 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191015f2-0a62-32e6-90ce-d550f049e4a3 | -1.4974 | -47.80415 | 2025-11-14 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5d8c7a1-d025-3d90-a20d-856d8850b723 | -1.49665 | -47.80889 | 2025-11-14 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34225cb0-30a2-3806-a484-1295fce8acc1 | -8.90573 | -44.43778 | 2025-11-14 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4c71760-301d-3bbe-aa0a-5ac71683d0f3 | -7.87044 | -44.31213 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3be94c25-d599-34e9-89cf-14ce103d6e66 | -8.30144 | -43.80769 | 2025-11-14 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9a87de5-6a56-357a-ad2b-fdfbd9ff9e33 | -10.72713 | -45.08337 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e31fbd1f-7fa8-394a-a3af-f275e99f08ea | -9.31906 | -47.83896 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20dca7ad-d6e4-3ea1-832c-6eec7749e5c5 | -7.8493 | -44.29441 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d024937-47b3-3b3d-aec7-4bc313bdb5c1 | -7.67027 | -45.87978 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27933f2d-4e15-30e9-a9bb-5c8289c865b9 | -3.20429 | -43.47446 | 2025-11-14 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2727c6f-0c84-3371-9e08-78a233c5b047 | -3.80139 | -40.96235 | 2025-11-14 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91a6e384-a363-30fb-a819-748619e4acdc | -3.35745 | -45.34613 | 2025-11-14 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 837a55de-0353-304e-96ef-8fe8d8f05bd8 | -9.35223 | -46.59655 | 2025-11-14 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6899c5ba-8a05-35a5-8602-b62df7530f9f | -3.65812 | -45.93736 | 2025-11-14 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec82df3-a6ed-30ce-aca8-6e7f314634d6 | -3.98852 | -42.94376 | 2025-11-14 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 068dfb47-71a9-35d6-8b40-69a64d5c49a1 | -1.80278 | -45.60899 | 2025-11-14 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbbd3526-175b-3c0c-8524-108f1ab3b976 | -2.55053 | -47.80452 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| def3aef8-3d3e-3319-aa13-007a01509a45 | -3.80372 | -44.39695 | 2025-11-14 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d85835-1f6b-3dff-a839-367ff6771e31 | -4.45712 | -43.47422 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37bdbdb-43c1-3d92-be87-d44b2ad9a291 | -2.84501 | -52.36779 | 2025-11-14 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 373feded-0e73-3e73-b69a-6c392d0c9bfa | -9.67835 | -47.8927 | 2025-11-14 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83ca647d-8e9c-36b7-8d76-94a787f6e11b | -2.43115 | -48.04729 | 2025-11-14 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e5d41f-3a60-3223-bcb9-5bbb19076956 | -7.77103 | -46.3236 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119a1feb-adbc-3685-a6b3-6f5ea05362b0 | -3.25317 | -43.29356 | 2025-11-14 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ced130a3-bc29-3452-81f2-ce4e65da9674 | -3.39762 | -44.71662 | 2025-11-14 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b135ec-a73a-3030-93b8-82ef05fb5c65 | -7.84875 | -44.29792 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed12aba2-4b76-36a1-a572-d9a22ae99763 | -3.08149 | -49.27422 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3d936c6-1ff0-39a0-8678-1838f7a9a3e9 | -3.43428 | -42.42487 | 2025-11-14 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 249b4047-50ad-3abb-908f-89c23442971f | -4.60215 | -41.73727 | 2025-11-14 04:23:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c88411fd-89cc-3941-bc9e-67f27fabc2ed | -9.66607 | -43.89443 | 2025-11-14 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0f1f60b-a358-34bc-9788-deee4e576cdb | -2.82643 | -48.32787 | 2025-11-14 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad830947-22b8-354b-8f11-f5a740375c13 | -7.92271 | -44.34912 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e41aeb5b-7d7f-395b-bf1a-a03b134c2962 | -9.66947 | -43.89493 | 2025-11-14 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8656041e-1baa-3c23-be99-f127df1aaf74 | -2.95928 | -45.76031 | 2025-11-14 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96316122-9c51-3abc-ae9a-e4124468d4a8 | -7.06741 | -48.36053 | 2025-11-14 04:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3108cbec-396e-388d-bedc-569cc316dd04 | -10.05535 | -44.76718 | 2025-11-14 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8341a779-572f-3650-a7b5-18abf8117a0f | -2.96181 | -41.57993 | 2025-11-14 04:23:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 202d2728-4830-39b0-86bf-7b08954ed388 | -4.13151 | -43.00932 | 2025-11-14 04:23:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README27.md)
