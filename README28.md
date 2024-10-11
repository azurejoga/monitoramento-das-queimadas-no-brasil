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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd5d33bb-e4e8-3370-975a-5fb84caf4775 | -10.70143 | -64.11173 | 2024-10-11 02:34:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2ef92602-b675-3aef-b048-449b47fc01f1 | -10.58053 | -64.02883 | 2024-10-11 02:34:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 75a6b058-7e8e-368f-9b0b-38564e2f06c7 | -9.65198 | -64.98912 | 2024-10-11 02:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8890663e-9148-3c61-b09b-5fed23e211ea | -7.30637 | -64.67401 | 2024-10-11 02:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ceb03473-f6cd-38a4-9e64-61b6e3d225ca | -9.64813 | -64.96548 | 2024-10-11 02:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7841e07f-797d-3d2e-a121-75e2889f94a8 | -2.6533 | -53.3506 | 2024-10-11 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d7aa426c-a932-3bc1-b223-a2bc0b43ff88 | -2.6716 | -53.3502 | 2024-10-11 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| de12f30b-2603-3457-8265-dd92e60249b8 | -2.7395 | -49.5412 | 2024-10-11 02:35:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 27d1d663-76ac-37d3-811f-f0f2edb00b34 | -2.7847 | -52.4933 | 2024-10-11 02:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| aaee7da4-64a2-382d-ac4b-4949993489e5 | -2.9673 | -52.9169 | 2024-10-11 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| e41cf339-ed20-3cb9-a18e-7d3b799fa424 | -2.9673 | -52.8966 | 2024-10-11 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1528e478-da2d-34fb-a674-ee326e5eba45 | -2.9857 | -52.9164 | 2024-10-11 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| fac9c507-3b68-3d03-aad6-c409bff948b6 | -2.9857 | -52.8961 | 2024-10-11 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 8a36cfee-c83b-334c-8430-5b79371d871e | -3.0343 | -61.6918 | 2024-10-11 02:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 24b5a807-a8cf-33e7-a445-67d002ec84fd | -3.0343 | -61.673 | 2024-10-11 02:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| edaa2b4d-62eb-3277-ac72-650198e8fbef | -3.1422 | -50.4562 | 2024-10-11 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 344689b9-72da-323e-80ae-bac43646cbd4 | -3.1423 | -50.4352 | 2024-10-11 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ce44725a-c50b-39ee-8d13-37fe90bd0607 | -3.1607 | -50.4556 | 2024-10-11 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| d8147c7a-a717-3616-a769-e56dbcaa71ee | -3.1608 | -50.4347 | 2024-10-11 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c682dc44-05f5-32bd-83eb-21a3a9ba5e34 | -6.1301 | -47.2664 | 2024-10-11 02:35:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c0286e2d-c950-3d8d-9fb9-17aefc6fb511 | -6.5589 | -60.0252 | 2024-10-11 02:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 487fe063-f198-38f6-a4e5-84f4076ba83e | -8.4231 | -55.4704 | 2024-10-11 02:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 12178f5f-7f54-35cb-9169-00050a64b2b7 | -8.4417 | -55.4692 | 2024-10-11 02:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f6313325-4f55-35e2-a382-01a4c025e884 | -10.6962 | -53.0354 | 2024-10-11 02:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 30bf8fde-a081-3803-9fff-30173e5f735b | -10.6965 | -53.0147 | 2024-10-11 02:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| e014edac-f83d-32a7-a998-b122129e2feb | -10.7059 | -64.1138 | 2024-10-11 02:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9eee59da-bdeb-317d-a65e-32f5c781b7d6 | -12.1138 | -50.55 | 2024-10-11 02:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5b7bbb25-a3ec-3e79-9d27-a7c1bb0c110e | -12.1329 | -50.5477 | 2024-10-11 02:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 14f698c4-a07c-3acc-a4c4-6cd92624429d | -13.9857 | -45.7992 | 2024-10-11 02:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b2ccb96d-a4b0-3a99-9366-3113fdf66cda | -13.7348 | -60.5883 | 2024-10-11 02:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e6956a3b-dae9-3339-8475-e2638c5faf58 | -13.7346 | -60.6079 | 2024-10-11 02:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 49a519bb-8eee-3681-a26b-d8a25dcad377 | -13.9663 | -45.8025 | 2024-10-11 02:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a4bc4776-9128-3349-aa01-6a40a79f6d25 | -7.10548 | -34.98222 | 2024-10-11 02:43:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 84bc86dc-48a2-3e92-9ecd-6279957167ec | -7.10295 | -34.97366 | 2024-10-11 02:43:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e721b7bd-f4bf-3f26-9af3-25105d114f29 | -7.10157 | -34.98072 | 2024-10-11 02:43:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8cfdcdde-571d-3a81-a61e-56e9861ab936 | -7.09837 | -34.9808 | 2024-10-11 02:43:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 58eeb6ee-8d9e-3378-a728-6f9099c6dc6b | -2.6716 | -53.3502 | 2024-10-11 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e7a51975-ef44-34f1-8c05-b032208db878 | -2.6533 | -53.3506 | 2024-10-11 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 23502130-f23b-3099-b216-20cc4d35ecf2 | -2.8081 | -51.0084 | 2024-10-11 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cb0faee2-6652-3de0-8c8c-d86aae0d53fd | -2.7848 | -52.4728 | 2024-10-11 02:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 862017d0-5d55-3d04-93ff-11505198778b | -2.7847 | -52.4933 | 2024-10-11 02:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6754fc34-8ccf-3731-8bcf-c02e2e20947e | -2.9857 | -52.8961 | 2024-10-11 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 63f1a191-7193-3cfa-8f94-e940e3936f39 | -2.9857 | -52.9164 | 2024-10-11 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 18166e71-7492-3893-8a1b-5c9ce2950379 | -2.9673 | -52.8966 | 2024-10-11 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 5a29f6c2-9698-3809-82dd-e53f67b1bfbc | -2.9673 | -52.9169 | 2024-10-11 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b4f5194f-72bf-3287-bec5-7f46eaeaf60b | -3.1608 | -50.4347 | 2024-10-11 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 7dd5754c-e808-3f25-8d8e-f0a311834648 | -3.1607 | -50.4556 | 2024-10-11 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 2931661a-7aef-335d-971b-c979441e1815 | -3.1423 | -50.4352 | 2024-10-11 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f5b0d694-dcf2-30f4-aff9-014f5a733aae | -3.1422 | -50.4562 | 2024-10-11 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3b67e48b-d037-303b-9000-d1fb2fd6d82c | -3.0343 | -61.6918 | 2024-10-11 02:45:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 6971627f-a1ff-3ea6-9411-9ff8a12c9bab | -5.3265 | -60.1239 | 2024-10-11 02:45:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f25a6539-286f-31c9-af95-80919516a3d1 | -6.5589 | -60.0252 | 2024-10-11 02:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 24019bd9-0640-3df5-90ef-54b8e60e4952 | -8.4417 | -55.4692 | 2024-10-11 02:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b56c4563-5b81-336e-b4de-9eeeac075dbf | -8.4231 | -55.4704 | 2024-10-11 02:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 76392e9a-3e15-3e72-a772-7c1a702f8184 | -10.6965 | -53.0147 | 2024-10-11 02:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9facbd4f-c088-33d5-882b-97f6b638d5b9 | -10.6962 | -53.0354 | 2024-10-11 02:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3496333f-8726-339d-abe5-e44f91285c07 | -10.7059 | -64.1138 | 2024-10-11 02:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| aaa0df8e-0319-38f8-9584-e2a3dec76421 | -11.2912 | -50.9208 | 2024-10-11 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 07d90550-33f6-3e94-98dd-7760944c61aa | -12.7871 | -44.8639 | 2024-10-11 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 55b1b8b5-5bf1-3bdb-a2ea-96606c3cf4f6 | -12.7866 | -44.8873 | 2024-10-11 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 29c286de-ea02-3d60-8ec6-634db82fa693 | -12.7678 | -44.8671 | 2024-10-11 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| e83bcf05-ffd5-38bc-a319-57138c7ed0e6 | -12.7673 | -44.8904 | 2024-10-11 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b45b7fc3-b058-39f8-aa90-f1b3a5a0e27a | -13.7348 | -60.5883 | 2024-10-11 02:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0f3f3347-ccc1-33be-b1c4-ab9a7e0b6753 | -13.7346 | -60.6079 | 2024-10-11 02:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 65ae206a-261f-3a7e-8e08-88a7aa24907a | -2.6533 | -53.3506 | 2024-10-11 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 7769e8d0-0df5-30a7-a286-7a4aa9f14a58 | -2.6716 | -53.3502 | 2024-10-11 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 300f60bd-49d3-3eb2-8954-0e7f6f1d23d2 | -2.7847 | -52.4933 | 2024-10-11 02:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| daabb997-16de-3884-b525-b9268bb54cfd | -2.8081 | -51.0084 | 2024-10-11 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 88735edd-f6ee-3482-bb57-955710fe44bf | -2.9673 | -52.9169 | 2024-10-11 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 1e70cdfd-75b8-3b1c-9b4f-0c0aba014948 | -2.9673 | -52.8966 | 2024-10-11 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 69e0ffd2-dde0-3fc1-8d38-4b704ec3e04f | -2.9857 | -52.9164 | 2024-10-11 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| df6b890c-0813-30ed-ac11-d18065190fab | -2.9857 | -52.8961 | 2024-10-11 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 87b72c89-e912-30ad-9656-1894a4586cc0 | -3.1422 | -50.4562 | 2024-10-11 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8bdaccb5-4742-35ac-a257-69fe8bd36d26 | -3.1423 | -50.4352 | 2024-10-11 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1cef563a-39c9-3bf0-8fc6-20709c933acc | -3.1607 | -50.4556 | 2024-10-11 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 1b416e2a-e568-388d-a55b-4a00b0aa7716 | -3.1608 | -50.4347 | 2024-10-11 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 8b933efc-747f-3687-bc37-dce677fb689f | -6.5589 | -60.0252 | 2024-10-11 02:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d4ac8407-095f-3834-b43e-3cd7958fd18c | -8.4231 | -55.4704 | 2024-10-11 02:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eb5b87b1-bc2c-3a39-be45-40c7335a8fe2 | -8.4417 | -55.4692 | 2024-10-11 02:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6a33b10c-43c9-322b-a193-3e36af6df8b5 | -9.6389 | -64.9664 | 2024-10-11 02:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| eb06203b-1225-3083-a0c4-e3bec33adced | -10.46 | -46.7885 | 2024-10-11 02:56:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| bdaa4d6a-f866-3939-ae40-597de356ff9e | -10.6962 | -53.0354 | 2024-10-11 02:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 815dfa4f-902b-3dcb-a35e-264228705223 | -10.6965 | -53.0147 | 2024-10-11 02:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d24e67e6-0129-365a-a9b3-d9045e809cd9 | -10.7059 | -64.1138 | 2024-10-11 02:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 11a04fc9-c690-39f0-873c-46f62551dc78 | -11.2328 | -51.0333 | 2024-10-11 02:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 467f6ac3-5654-3f74-b2c8-761bcebae42d | -11.2407 | -53.2738 | 2024-10-11 02:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3ab6c17e-d1d8-365e-aa0a-d444e475e7d0 | -11.2597 | -53.272 | 2024-10-11 02:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5c335167-0d9a-32a8-923f-8df37ffc6c7e | -11.2909 | -50.9421 | 2024-10-11 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f7b88a27-d2c8-359c-ba3c-78d33a428747 | -11.2912 | -50.9208 | 2024-10-11 02:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| eea25e48-1a0d-33b6-b6e5-a992c1b364a3 | -12.7678 | -44.8671 | 2024-10-11 02:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 75af78a9-5ff1-3828-90ae-2e8af6e38292 | -12.7871 | -44.8639 | 2024-10-11 02:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f02f9726-1e52-35a9-8f82-693c1e4393a7 | -12.9855 | -53.4673 | 2024-10-11 02:56:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3b46ae99-e617-399e-9c5b-ef3be845e3f1 | -13.9663 | -45.8025 | 2024-10-11 02:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ac50f6ea-21fc-31ba-b947-290c4982245a | -13.9857 | -45.7992 | 2024-10-11 02:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 98d496ff-30e9-3d12-92e6-39dd4e40b804 | -13.7346 | -60.6079 | 2024-10-11 02:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1739a5ce-6eec-3b03-86b3-31d50250c89e | -13.7348 | -60.5883 | 2024-10-11 02:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3e18c9de-feff-3b15-abd9-581fe99d2a92 | -2.6716 | -53.3502 | 2024-10-11 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 8146b9b4-7f6b-34de-af82-9d09ef4604ba | -2.6533 | -53.3506 | 2024-10-11 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| fd5ffcad-b1bc-3e36-8ca2-d0ef8bd0dcaa | -2.7848 | -52.4728 | 2024-10-11 03:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e165014d-a3a8-3dc1-8f3b-f7d838252751 | -2.9857 | -52.8961 | 2024-10-11 03:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |


[Clique aqui para ver as próximas entradas](README29.md)
