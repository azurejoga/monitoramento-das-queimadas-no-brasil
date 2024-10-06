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
| a6de1ad6-dfdd-30b6-b67b-394c5c7898ef | -10.6929 | -53.03727 | 2024-10-06 03:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de2da153-4cae-3548-a618-0615e5214516 | -12.63398 | -53.11684 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9523cbe9-f528-35a5-881f-f1e73d2d1359 | -12.63385 | -53.11593 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b51e71be-6eae-3328-864f-1e215aed4f51 | -12.63266 | -53.12315 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 67a9803c-b949-3db1-87e9-aa44c26c7acb | -12.63249 | -53.12224 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e5c55113-a862-37a5-be17-ecea86f9481a | -12.62716 | -53.11534 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b78d858a-3b64-33a8-98c4-c2442205d4be | -12.62704 | -53.11444 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 387607f3-3575-3c66-bbc2-db0c82df447d | -12.62583 | -53.1217 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6abfea01-fcb5-310b-ab28-8523a4eb3490 | -12.62567 | -53.12081 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 334d0b5d-9099-3c4b-a849-f40174a72eb1 | -12.62453 | -53.12792 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 58a2fddf-91b2-3327-a8d7-58dfb6031d7c | -12.62433 | -53.12703 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6101862-d59e-3057-8a12-b36a5649842a | -12.62037 | -53.11376 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c386f64-d6cc-3335-b0df-fcbb37496118 | -12.61903 | -53.12016 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6394d403-f89a-3acd-9006-3127bdcee19c | -12.61886 | -53.11927 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4041564f-d064-361c-9e0e-a09d76bc2aed | -12.6177 | -53.12646 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e55c6b3-eea0-3e7e-a693-592d113f2778 | -12.6175 | -53.12559 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f7e4a81-5e41-3d33-aa9f-c23741a7c5af | -12.61223 | -53.11858 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c33914d-cc2c-3006-9841-ede012373b30 | -12.61206 | -53.11773 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5329305f-3127-3dae-9602-ee3e7a491696 | -12.61088 | -53.12498 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de8d4cec-7aa0-3406-a8c8-a5503b6b4967 | -12.61067 | -53.12412 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa161449-9d1e-3e82-b095-2fc8e28bff89 | -12.60796 | -53.13665 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9498de20-a617-3d73-956a-63f3cec639c3 | -12.60407 | -53.12344 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4400cdb7-8839-35e8-9b89-993cb2f9e599 | -12.60386 | -53.12261 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dc1deaa-738e-3649-9054-12dc5491b6fb | -12.60274 | -53.1298 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f37509c5-51cf-3f82-8c5b-b5c8b8b4a1bf | -12.60248 | -53.12896 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1a50fbe-4867-3e0a-895c-601d1116d4a0 | -12.6014 | -53.13613 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9fe12030-e7d1-3c34-a26c-8cf65cef47ac | -12.60111 | -53.13528 | 2024-10-06 03:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e22b3fa0-c576-3bf5-8c19-df1536bac2d9 | -17.6277 | -44.41922 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e95ec87-b98c-37c0-805b-56c4c6fd1229 | -2.798 | -48.7087 | 2024-10-06 03:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| abbe9ee5-9bbc-374f-9577-ce322bff203a | -2.7981 | -48.6873 | 2024-10-06 03:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e7671d63-f551-3e62-91fb-6ba813adb635 | -2.8165 | -48.7082 | 2024-10-06 03:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 46aa3ec5-ff49-36a0-acfb-25dea38a776f | -2.8166 | -48.6867 | 2024-10-06 03:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a695e044-b9d0-39d2-97e7-c6411fe45a31 | -3.1129 | -48.6131 | 2024-10-06 03:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9c481dc6-b9e5-3ca7-a0d7-a12730f2ae3d | -3.1314 | -48.6125 | 2024-10-06 03:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 8ca76a43-ff98-3449-8be4-a476c1525cbe | -3.1315 | -48.591 | 2024-10-06 03:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 22c5d92e-5ff6-3d7d-904b-c66a4fad9fa6 | -3.8464 | -46.4714 | 2024-10-06 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a01c2d08-ef36-3e54-935a-b9bc3d292b2e | -9.3467 | -46.5365 | 2024-10-06 03:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 414f1088-bac1-30d7-91ab-33caf0448ec1 | -9.3835 | -51.0881 | 2024-10-06 03:55:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 124bb28c-a92d-3b0b-96ff-2e30a6374b10 | -9.688 | -47.8308 | 2024-10-06 03:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 01d388d1-3eca-3e1c-b02d-3a669dd8c8be | -9.6883 | -47.8088 | 2024-10-06 03:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d5c453fa-b484-33fa-a4d6-8d23cfe07a55 | -9.7069 | -47.8288 | 2024-10-06 03:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 332f650b-5dfc-3261-98f3-2a3769597667 | -9.7072 | -47.8068 | 2024-10-06 03:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| fab2ada6-a712-347f-b725-1e4c555ac07b | -9.6778 | -64.6457 | 2024-10-06 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| bd3c5c19-c04d-3ca6-9a6a-044c1fd376a7 | -9.6779 | -64.6269 | 2024-10-06 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 7ecf22a6-5e7b-3197-a12c-16499cfaee8f | -9.6964 | -64.645 | 2024-10-06 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| da4f5ced-2459-39aa-a865-bfa0a226f35e | -9.6965 | -64.6262 | 2024-10-06 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5a007b43-6065-3931-bb20-317d86fe2314 | -10.1955 | -48.0391 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| bc444f0c-7c59-3a72-a900-f0317da68108 | -10.1958 | -48.0171 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5b1d3f17-6f82-3131-9bb9-d09d0e38e88d | -10.2145 | -48.0369 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8a19874e-3feb-3dcb-848e-004f3fb83a5f | -10.2148 | -48.0149 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 2f03eaaf-e2a7-3287-b241-fe59e0b5f4a2 | -10.2151 | -47.9929 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 34e28cf2-442d-34cf-a1c2-681a4448f062 | -10.2337 | -48.0128 | 2024-10-06 03:56:04 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6e949a23-560e-3c75-a380-5c0eb3a1c9f9 | -11.5238 | -65.0615 | 2024-10-06 03:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 251bbb1b-ab11-349e-96fc-e517a2746418 | -12.6089 | -53.1338 | 2024-10-06 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f54546c4-090f-30e5-8605-120c45236956 | -12.6092 | -53.1129 | 2024-10-06 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2a30b6be-c605-3a86-b32a-e05335a63981 | -12.628 | -53.1317 | 2024-10-06 03:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 47b309cd-a360-300a-b12d-3038bf431072 | -12.6283 | -53.1108 | 2024-10-06 03:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 252a9a49-f492-34d4-88e5-445f9356d447 | -12.6532 | -54.0415 | 2024-10-06 03:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 38d8c2bf-a751-3a77-884b-8867dedc5cff | -12.6535 | -54.0208 | 2024-10-06 03:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| bfaff3cc-a367-39c4-9c06-6c9bb35aa6ac | -12.7439 | -50.5376 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 092c279d-61db-3685-a7e2-3e1d622c228e | -12.7627 | -50.5567 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 7af73e4e-1a39-3eb6-8bd7-e1965ab56f23 | -12.763 | -50.5352 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 748.7 |
| 71b6d2db-8434-3f16-8612-3aa67d8bbc46 | -12.7634 | -50.5136 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 9576cf1e-1ab5-3e6c-bbc9-06598ad1a75c | -12.7822 | -50.5328 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| b3a8a3c4-5686-34df-ad80-3784e60a0b26 | -12.7825 | -50.5112 | 2024-10-06 03:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| cd38651a-3eb6-362b-bc2d-3b66bedb7c42 | -13.3786 | -61.9582 | 2024-10-06 03:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fbaccc0a-0ad9-364c-a525-d7c10df72efa | -13.3976 | -61.957 | 2024-10-06 03:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 92bc66a3-6355-38f7-b1e3-c183a995526f | -16.3764 | -57.3663 | 2024-10-06 03:56:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 8786dda1-4aad-3a2a-9b32-c126b02656e5 | -16.554 | -57.2237 | 2024-10-06 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.4 |
| 38c6ba7b-bd7d-3f19-8bac-2accc6fdcd53 | -16.5544 | -57.2032 | 2024-10-06 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.8 |
| 6cf2b710-806e-336b-a078-36d94ace7de1 | -16.5736 | -57.2215 | 2024-10-06 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| eb964e39-a390-3e99-9e6c-f022eb89d834 | -16.5739 | -57.201 | 2024-10-06 03:56:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 9a2c8f25-32f7-3e08-91ec-4867a9aff3ad | -16.9092 | -47.1724 | 2024-10-06 03:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| bfd2b766-ab1c-3885-9e03-aa721ed5dccd | -16.8238 | -57.4584 | 2024-10-06 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| e14a0a78-25d3-39e2-afb9-de85b3eff294 | -16.8433 | -57.4562 | 2024-10-06 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| b51a0096-ed99-32b3-8413-37bfb12612af | -16.9714 | -56.7852 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| a07e2ebb-799a-3d7b-9624-17d986a41b1f | -16.9717 | -56.7646 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.2 |
| a6826b90-a183-313e-a99a-716184e2722e | -17.0003 | -55.0817 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 185.2 |
| c34a192b-67a4-3f53-8f55-0b7e93d712ff | -17.0007 | -55.0607 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 290.7 |
| 3f4f7eb6-0501-32ce-a0db-82962fa9a213 | -17.001 | -55.0398 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0c4716dc-ae8c-3da6-9106-c008a5732b4d | -16.9903 | -56.824 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 98ea666e-ccbf-3feb-bbe7-7232548b57e5 | -16.9907 | -56.8034 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| a693903a-7e9e-3dfc-ba9d-6a05d1445948 | -17.02 | -55.0791 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 7ab26409-45b8-34d0-884d-a9463ffb0fc9 | -17.0203 | -55.0581 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 439.9 |
| 4e4cbe52-9712-3652-9eb0-1e6237137918 | -17.0207 | -55.0371 | 2024-10-06 03:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| bbd32b88-4d01-3bea-b2eb-e67608d2e471 | -17.01 | -56.8217 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 42c851e0-c0a0-35d0-b589-c278cb7168e7 | -17.0885 | -56.8122 | 2024-10-06 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| b3437f40-9f3a-3ec8-b615-d23b1e490ff0 | -17.812 | -53.7859 | 2024-10-06 03:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f556130d-5c26-3afd-ad65-3e1a495d1f4a | -18.6387 | -57.2785 | 2024-10-06 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.4 |
| e61c8255-0cf4-3f60-962e-cc81e5e5dd4b | -18.6586 | -57.2759 | 2024-10-06 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| e98bc848-6722-3dc3-b342-61a1d66e065b | -21.85682 | -48.44407 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f340b38-e7a0-3612-80f6-9b2778d379a7 | -21.85249 | -48.44313 | 2024-10-06 03:57:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07a0f743-639d-335f-8b4f-cb545525b6fa | -22.29734 | -49.12111 | 2024-10-06 03:57:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7220f24-8033-333e-a251-30ec5f9ac87d | -22.54083 | -48.81189 | 2024-10-06 03:57:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e192616-5bd3-3af2-9eaf-7012bb4aac1c | -20.51164 | -47.49369 | 2024-10-06 03:57:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c59166f9-50cc-390b-882b-a0ea82366bc1 | -19.86066 | -47.85739 | 2024-10-06 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1102c52-a482-3188-a7b1-2bb24e2bfce6 | -19.85549 | -47.86089 | 2024-10-06 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce79ce3-c4ce-3a31-8a32-f8d47602129d | -19.85119 | -47.85981 | 2024-10-06 03:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54789889-e4f2-360b-a000-2f7ec10aa080 | -20.45376 | -49.98384 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bccfd90a-ec3f-37cb-9d6e-aea096e3b809 | -20.44164 | -49.94409 | 2024-10-06 03:57:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README59.md)
