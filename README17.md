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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ec2741a-c3a4-3afb-9deb-17800c2becaa | -13.1028 | -52.0281 | 2025-06-03 07:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 315b4078-d164-3ae4-9e2d-aed37badbad5 | -18.8675 | -53.6434 | 2025-06-03 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 03a7826b-ae33-34ef-8a06-97d8becfc21f | -18.8679 | -53.6218 | 2025-06-03 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| a7db2dc0-58d4-3908-bfb7-e2a4e2e71daa | -18.8875 | -53.6402 | 2025-06-03 07:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 28e60e2c-f478-3b8c-8565-8f4e640743ea | -13.1028 | -52.0281 | 2025-06-03 07:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e36c70d4-4cf2-3979-a989-bc2cb25c2405 | -18.8875 | -53.6402 | 2025-06-03 07:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f81de526-4d66-3f3a-b06a-0ba974fad812 | -18.8679 | -53.6218 | 2025-06-03 07:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.2 |
| d82b4cd6-ceea-3f6f-b267-4c3383898ee6 | -18.8675 | -53.6434 | 2025-06-03 07:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2d217b96-e590-38dc-8622-3d8e448b359b | -18.8875 | -53.6402 | 2025-06-03 07:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2946f9fd-ce4f-31f9-b319-7d32dabfc92e | -13.1028 | -52.0281 | 2025-06-03 07:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 00145ea8-c5d2-3529-8197-1dbad14d1f4b | -18.8675 | -53.6434 | 2025-06-03 07:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 114.1 |
| db20764d-a6d5-3ea4-9f9d-eefcdaa3d91e | -18.8679 | -53.6218 | 2025-06-03 07:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9edab897-cc4c-3272-8c60-d1e1399dac5c | -18.8675 | -53.6434 | 2025-06-03 07:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ceb58c32-1120-3c8e-8028-1138bcffe163 | -18.8679 | -53.6218 | 2025-06-03 07:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6f2d33e8-15ce-3d49-b27f-eec87d9bc106 | -18.8875 | -53.6402 | 2025-06-03 07:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 430ded90-5274-3aaa-b30f-dbc58e14e3ee | -18.8875 | -53.6402 | 2025-06-03 07:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 651a6719-0136-38c0-868a-178fb4127f1f | -18.8679 | -53.6218 | 2025-06-03 07:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 31705834-3f8a-39db-9e39-725aa3e9c3ee | -13.1028 | -52.0281 | 2025-06-03 07:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 991bd597-540c-310d-a292-cd590d4ee184 | -18.8675 | -53.6434 | 2025-06-03 07:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 03849615-488d-3f14-8438-5a7012e383c6 | -18.8875 | -53.6402 | 2025-06-03 07:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a7f12a4b-0a70-31ba-a6b8-157da7486077 | -18.8675 | -53.6434 | 2025-06-03 07:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ca2f9242-6a74-33bf-a0d6-ea0bf8df449c | -18.8679 | -53.6218 | 2025-06-03 07:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c55b7a32-dbf3-3397-85b3-78244c4c0fcd | -18.8679 | -53.6218 | 2025-06-03 08:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 006fa79e-aaed-36c5-98c0-e85deeaee68e | -18.8675 | -53.6434 | 2025-06-03 08:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 115.9 |
| e192a61d-84d0-3c70-b9b4-e524ffb1b1f2 | -18.8875 | -53.6402 | 2025-06-03 08:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 56515295-4055-3bb3-bb74-db91a183cb66 | -18.8675 | -53.6434 | 2025-06-03 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 18bd9d48-357e-39b2-8562-78ba272053a4 | -13.1028 | -52.0281 | 2025-06-03 08:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 95cd3dcc-54c0-3e18-903c-b5246e5bc949 | -18.888 | -53.6186 | 2025-06-03 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7b4b5790-8df8-3240-b900-47cd8c36201c | -18.8679 | -53.6218 | 2025-06-03 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6fcb6997-e529-3c1d-bb59-6e65e558c57a | -18.8875 | -53.6402 | 2025-06-03 08:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ce818e0b-e49d-3ef7-aeb5-3500bb62ee57 | -18.8875 | -53.6402 | 2025-06-03 08:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9445159c-b24d-3eee-9b16-24b36200c0dc | -18.8679 | -53.6218 | 2025-06-03 08:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 93.6 |
| eaba08ae-14bb-30bf-9115-882f4f377b2d | -18.8675 | -53.6434 | 2025-06-03 08:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 156.7 |
| fe555846-24ab-3c7e-bd12-d0bde30eefa2 | -18.8675 | -53.6434 | 2025-06-03 08:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 1ef71871-9e18-30f3-a987-03d6a01799cb | -18.8875 | -53.6402 | 2025-06-03 08:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1902eede-2f75-3e41-aa48-463cd2fd4322 | -18.8679 | -53.6218 | 2025-06-03 08:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a57268e4-9c21-3095-b0ae-d45fe612f0b5 | -18.8875 | -53.6402 | 2025-06-03 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 881d3b1c-7c6d-33b2-8df5-ed779886802c | -18.8675 | -53.6434 | 2025-06-03 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 129.7 |
| faefafe3-db4a-3867-b3f7-0fa1b056411d | -18.8679 | -53.6218 | 2025-06-03 08:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2b36dfb8-48c4-376e-bf0e-40b1c9f73c77 | -18.8679 | -53.6218 | 2025-06-03 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.2 |
| eff62194-0cde-3ed1-9760-7503b787200b | -18.8675 | -53.6434 | 2025-06-03 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 161.2 |
| ef5d50f4-02b4-379c-8d66-c8694833c193 | -18.8875 | -53.6402 | 2025-06-03 08:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8053f6b0-f9bb-3ad1-bb18-b8306fa1f875 | -13.1028 | -52.0281 | 2025-06-03 09:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 41cd70fb-3d45-330d-b6f6-e38be39fcfb1 | -18.8675 | -53.6434 | 2025-06-03 09:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 052ea59c-92ec-3b1c-91f8-d9a1c000ede5 | -18.8875 | -53.6402 | 2025-06-03 09:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7cb25ac6-5dbb-33ba-9d6c-533d1ec13112 | -18.8679 | -53.6218 | 2025-06-03 09:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f66e55c9-1e22-3625-91e6-d2ec0493653c | -18.8679 | -53.6218 | 2025-06-03 09:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b4fd6bb7-3c76-3ec0-b07f-da8add38d3db | -18.8675 | -53.6434 | 2025-06-03 09:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 154.6 |
| e756419b-7788-3aca-a85a-8803bee3c54f | -18.8875 | -53.6402 | 2025-06-03 09:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 96913e09-8f9d-30db-b6f0-91b552f611fe | -18.8875 | -53.6402 | 2025-06-03 09:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ef789841-d189-3ae9-bad6-fe44d0c2bf79 | -18.8679 | -53.6218 | 2025-06-03 09:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2299ee3d-5411-38da-a593-c57a03ca4143 | -18.8675 | -53.6434 | 2025-06-03 09:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 537564c5-ec36-39a3-9e76-3b11373a4ac9 | -18.888 | -53.6186 | 2025-06-03 09:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d495149b-4ac6-3024-bb5d-0ae30fd9e5cf | -18.8875 | -53.6402 | 2025-06-03 10:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3b1be752-04af-3d51-ba70-1883bebca4ca | -18.8679 | -53.6218 | 2025-06-03 10:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 34615fab-8dbe-34d3-a7d1-0fda76703364 | -18.8675 | -53.6434 | 2025-06-03 10:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 191.3 |
| b6971424-cdae-3e12-ba8a-ccfdbdef7206 | -18.8875 | -53.6402 | 2025-06-03 10:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 7f0ba1f1-403e-3147-aa00-b007a4f805dc | -18.8675 | -53.6434 | 2025-06-03 10:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 170.5 |
| ee4d7bf7-db20-3b26-962d-69c325a757d9 | -18.8675 | -53.6434 | 2025-06-03 10:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 194.1 |
| d1b2e853-6b60-3c4e-984c-3881af57346f | -18.8875 | -53.6402 | 2025-06-03 10:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 154.0 |
| bf5593b4-7ee1-3ffe-8a39-58f39dd9ac8e | -18.8875 | -53.6402 | 2025-06-03 10:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 150.7 |
| fd503e92-fed9-3269-aa40-d08f8bbf50a7 | -18.8675 | -53.6434 | 2025-06-03 10:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 2adeb9af-3927-3a0b-b570-5d1fcb1f1669 | -18.8679 | -53.6218 | 2025-06-03 10:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 666be98b-e205-3032-8c6b-936489824ea9 | -18.8875 | -53.6402 | 2025-06-03 10:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 6c9ac863-1b48-3d86-829c-d6aed61877a2 | -18.8675 | -53.6434 | 2025-06-03 10:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 238.4 |
| efbd0d76-4ee3-3c1b-90b2-61dce7acfdc4 | -18.8875 | -53.6402 | 2025-06-03 11:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 4fdbc45b-e7ef-39da-951a-07ae80ca55cf | -18.8675 | -53.6434 | 2025-06-03 11:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 221.1 |
| e20b7298-f072-3fde-a3c4-2b0d33beda74 | -18.8679 | -53.6218 | 2025-06-03 11:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 178a0a30-c5ad-392a-8a81-c64d302b538c | -18.8675 | -53.6434 | 2025-06-03 11:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 177.4 |
| c08238e6-d951-39c9-8424-b067d84c25ce | -18.8875 | -53.6402 | 2025-06-03 11:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 296af47d-fd87-3527-90d2-9164dc26e848 | -18.8875 | -53.6402 | 2025-06-03 11:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6c32d2d9-5493-30c6-9574-1471a06a88a5 | -12.518 | -57.183 | 2025-06-03 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9c67e2d7-4f5d-3238-9dff-001ff1b8dbff | -18.8675 | -53.6434 | 2025-06-03 11:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 633bfb6b-0124-3636-be08-17b92e33a52f | -18.8679 | -53.6218 | 2025-06-03 11:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c1d57a0c-1303-3a87-a6b2-8494a4cc8c0e | -18.8675 | -53.6434 | 2025-06-03 11:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 75064c67-db79-311f-9ce5-f5b1d3492be4 | -12.5182 | -57.163 | 2025-06-03 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0f839d24-f454-363e-8db4-04dbb02d1fae | -12.518 | -57.183 | 2025-06-03 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5f684037-f810-3d12-ada4-bc6366c2c073 | -18.8679 | -53.6218 | 2025-06-03 12:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 119.0 |
| f2d4ef63-2e32-3485-9f6a-fe3890884c15 | -18.8675 | -53.6434 | 2025-06-03 12:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 214.1 |
| a5d5e170-da57-38fa-8987-6489ba79f91d | -12.518 | -57.183 | 2025-06-03 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 8f4eab91-f5c5-34d8-b737-55045d1718d2 | -18.8675 | -53.6434 | 2025-06-03 12:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 71dd0a4a-fa30-31ab-8ad3-85cecdc46453 | -18.8679 | -53.6218 | 2025-06-03 12:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 3baf2056-71df-3742-9eb9-a6ddea04038d | -18.8679 | -53.6218 | 2025-06-03 12:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5a6ee926-ffa0-314e-933d-85b8cb32ddd3 | -18.8875 | -53.6402 | 2025-06-03 12:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 152dae2e-27d9-3f8a-8c56-a810aefce6fb | -18.8675 | -53.6434 | 2025-06-03 12:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 165.6 |
| e916ee9f-de39-308b-b051-925d403818b1 | -18.8679 | -53.6218 | 2025-06-03 12:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 933be08f-b718-31a0-8dd7-392ed146c6dd | -12.5182 | -57.163 | 2025-06-03 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 8c566ef7-a2f7-3a2d-b7e7-95d83d493643 | -18.8675 | -53.6434 | 2025-06-03 12:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 257067ec-4b6b-3beb-a6da-0f397aef3321 | -18.8875 | -53.6402 | 2025-06-03 12:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 02079c42-ee90-3481-93e1-0accd5194b49 | -12.518 | -57.183 | 2025-06-03 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 6b27afaa-85b5-3ce4-b2a5-81966b150c21 | -12.5182 | -57.163 | 2025-06-03 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 83b9ad41-e1f4-3808-9740-e6ce6c3db544 | -10.6685 | -44.4137 | 2025-06-03 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |


