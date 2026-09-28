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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 336b6c2b-c3b9-362b-9a47-d1b3262dfcf5 | -14.79871 | -45.95483 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1e07828a-d410-3bc3-96d1-b79af4c98013 | -15.16704 | -46.14115 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2e56ce1-72b3-34ff-ba1c-9556122d69e6 | -13.1061 | -47.41529 | 2026-09-28 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d15604a1-01c9-3be4-b833-7b71f1ed4af8 | -14.71633 | -45.57804 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fc12ce6a-d315-39de-95cc-e916530f01a0 | -15.18325 | -46.15298 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7791270f-d757-3011-b7be-b319df7c8dbc | -15.16424 | -46.15933 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 89505aae-3f2b-3665-bac5-543f3310776c | -15.17585 | -46.14248 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| de86c3c4-39c7-3027-bbbf-2c7327055f1c | -14.59448 | -45.59818 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 31c947d2-8589-3f25-aad3-54489fad6fa4 | -15.16564 | -46.15023 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06918e07-3e13-3d5a-8d99-6788ea3df35b | -15.17445 | -46.15158 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ea942d73-bfe0-3985-9f16-eeee336d1123 | -15.55416 | -47.91811 | 2026-09-28 06:35:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b374c02c-b385-3435-ab29-c16bf69ce99a | -15.40329 | -47.91873 | 2026-09-28 06:35:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| be2b064e-1b85-365d-a0ff-9380b06b1775 | -14.11686 | -46.29706 | 2026-09-28 06:35:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d185468b-5d95-30e9-9563-669810adde5f | -14.7177 | -45.56903 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 325b6a81-e326-337b-9a39-f6d314a722e5 | -14.72646 | -45.57041 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e9a9cdaa-6a3d-394c-a02b-c5e987c128b7 | -13.10778 | -47.40483 | 2026-09-28 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e848d82-c72b-3cd8-b36d-94b073b57adb | -14.51652 | -48.30403 | 2026-09-28 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ec49061-17de-30a9-96af-82ac604ad918 | -15.17304 | -46.16071 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f69c26b7-3e0b-3c87-b7af-feeefc132a99 | -14.52619 | -48.3056 | 2026-09-28 06:35:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dcee47a4-cda3-3041-b461-bddbb489a5c7 | -13.10442 | -47.42574 | 2026-09-28 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 96174fe3-ba8f-3c74-98c8-ea90a5499a94 | -14.73523 | -45.57179 | 2026-09-28 06:35:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 74a564a1-ec8f-3b52-8e74-af9b3f0438c0 | -15.40498 | -47.90842 | 2026-09-28 06:35:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7cb00e75-edae-3711-aab6-57ff64dbbbd1 | -13.71027 | -48.8197 | 2026-09-28 06:35:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3afa2480-576f-3f50-a0af-397c3396cb6e | -13.16026 | -48.53828 | 2026-09-28 06:35:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cadf6b74-f452-3890-8a7a-c93fb4de6fd3 | -15.02346 | -49.58653 | 2026-09-28 06:35:00 | AQUA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 727e9e77-2952-35bb-8d08-64244dde484b | -13.15811 | -48.55102 | 2026-09-28 06:35:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8c198bec-2948-3464-bbe9-bd493cf25f00 | -19.14891 | -43.82254 | 2026-09-28 06:37:00 | AQUA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d2149753-fb3f-30e1-93c2-4786acf9d46d | -18.11692 | -44.37619 | 2026-09-28 06:37:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8f503d6e-ab1d-3832-b775-95fc5713985e | -19.1474 | -43.83385 | 2026-09-28 06:37:00 | AQUA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bbf7838b-fb09-3c30-91f2-018841c7b3bc | -20.17684 | -48.58653 | 2026-09-28 06:37:00 | AQUA_M-M | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4cd0ada3-c315-30d4-9cd5-65068f817f79 | -19.14415 | -43.82626 | 2026-09-28 06:37:00 | AQUA_M-M | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6c264310-f3f8-3eef-b2fb-bd86f9db74ff | -18.10635 | -44.38487 | 2026-09-28 06:37:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 78c5490a-78c9-3a40-ac88-f265f0c56576 | -9.1584 | -61.4082 | 2026-09-28 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0a0222a9-931c-39ee-b82c-481e69173199 | -9.177 | -61.4073 | 2026-09-28 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 374c08f9-832a-3dfd-b297-7ab09cfe882f | -9.177 | -61.4073 | 2026-09-28 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 30e36b4f-a5a1-3086-baaa-38b8550cc863 | -6.98091 | -71.68556 | 2026-09-28 06:52:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 000ca598-bdec-3c58-8e8a-b1fde42afb89 | -9.177 | -61.4073 | 2026-09-28 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d9584e17-c58a-38f4-9ec5-a795f34e599a | -9.1584 | -61.4082 | 2026-09-28 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ce83eb64-2c19-3615-b9bd-af66ccc5cd62 | -11.19 | -44.8 | 2026-09-28 07:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0c87990-5583-3c9f-a75f-87cc13d17a46 | -15.1842 | -46.1642 | 2026-09-28 07:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ddca7567-50ce-356a-9af4-cd3fc64a4d9c | -15.1847 | -46.141 | 2026-09-28 07:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 318b729d-c9f4-3059-8d0f-f01c2325d64a | -15.1847 | -46.141 | 2026-09-28 07:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f7a8e8eb-ca87-33d1-b6a7-f721e2af9b7b | -9.177 | -61.4073 | 2026-09-28 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 190dd8b7-67aa-3036-9fa3-ec6c8b7c7109 | -15.1842 | -46.1642 | 2026-09-28 07:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 14e7fabc-0bf5-3af5-b864-582953063954 | -9.177 | -61.4073 | 2026-09-28 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 0ba1c494-1952-3fa2-9be6-531891d8d96b | -9.1584 | -61.4082 | 2026-09-28 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| af7d6557-9b3d-377b-8cff-ee2909856e43 | -15.1842 | -46.1642 | 2026-09-28 07:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b0eb781e-e434-32c4-be2f-aaa2266ee17f | -15.1842 | -46.1642 | 2026-09-28 08:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fd1afe92-e0cf-338a-91b4-c3d756abaa4a | -9.16781 | -61.39663 | 2026-09-28 08:11:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 267985b3-12c7-3b40-a7ba-18039d1b0354 | -11.19 | -44.8 | 2026-09-28 08:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 065fe051-cf8f-33b4-a05c-532eaa723972 | -9.177 | -61.4073 | 2026-09-28 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 833c8f20-f36f-3a19-bf65-cb789fb54718 | -9.1584 | -61.4082 | 2026-09-28 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 71ce4d8d-0099-3bb2-9975-f2f6bd0c945f | -9.177 | -61.4073 | 2026-09-28 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e478d033-a11c-3101-ab0f-f686adb81202 | -9.177 | -61.4073 | 2026-09-28 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2e1ecf5c-0cca-322b-94cd-83be1524a292 | -9.1584 | -61.4082 | 2026-09-28 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a4180f8c-5d81-31ad-90f6-2d4899594256 | -9.177 | -61.4073 | 2026-09-28 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 762ce208-4cfd-3923-ae45-3bb74b3f47c2 | -9.1584 | -61.4082 | 2026-09-28 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b6e87330-49af-3aae-9f7a-cac6f0723782 | -9.177 | -61.4073 | 2026-09-28 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5906aa02-7620-381c-bc68-9a51d23f44ef | -12.6263 | -47.3075 | 2026-09-28 09:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 890986ac-ecf7-3823-ab26-de7369069523 | -11.1962 | -44.8037 | 2026-09-28 09:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 159c381c-50cb-332a-a28a-080fe9ff3f8a | -9.1584 | -61.4082 | 2026-09-28 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e8c46802-920f-3eaf-980c-265e24f6cf91 | -9.177 | -61.4073 | 2026-09-28 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e33f88c7-a0cd-3e76-988d-fb12e14b0daf | -11.1962 | -44.8037 | 2026-09-28 09:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| f091724f-6342-31e3-b9e8-ace62314964b | -11.1771 | -44.8064 | 2026-09-28 09:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c4e5ea6d-92f7-3200-8218-3b52cc6815c1 | -11.1962 | -44.8037 | 2026-09-28 09:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3fc4df9a-5221-34e3-9d6d-d2796a2831f0 | -11.1962 | -44.8037 | 2026-09-28 09:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 95086952-5b1e-3764-a1c4-fae8170e04c1 | -11.1771 | -44.8064 | 2026-09-28 09:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| fca8a9b3-7894-31f2-b517-e4e7eb518fe1 | -11.1962 | -44.8037 | 2026-09-28 09:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| bfc475fe-34f0-3d97-bb8b-f1155b4115aa | -18.7996 | -52.1623 | 2026-09-28 09:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 32b360cd-7d91-3366-a0b1-c329477c4dbc | -12.6643 | -47.3245 | 2026-09-28 09:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 9cc8a924-d2d1-3632-8f5e-b0983770269c | -15.2038 | -46.1606 | 2026-09-28 09:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 124.9 |
| b2c3c60c-2194-3a5d-8eba-8bb7a529c60d | -12.6263 | -47.3075 | 2026-09-28 09:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 303a53de-9f89-3a25-b452-c7ce0d3eadef | -11.1771 | -44.8064 | 2026-09-28 09:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 03d39072-7c84-3478-a93b-4ab48b10a512 | -11.1962 | -44.8037 | 2026-09-28 09:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| fadf59a2-c06d-3c3b-b683-aeb21dbb2acd | -12.6643 | -47.3245 | 2026-09-28 09:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 89e7d427-eff7-3f9b-b491-42318b503d11 | -11.1771 | -44.8064 | 2026-09-28 10:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 8933b336-c6fa-3969-88ea-5764f81ec000 | -15.2038 | -46.1606 | 2026-09-28 10:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 656b8b1c-5056-3fc0-8b35-712217d132f5 | -12.6263 | -47.3075 | 2026-09-28 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2fe3bdad-55eb-35a1-ac3b-5595a05151f2 | -11.1962 | -44.8037 | 2026-09-28 10:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 1bba7a2c-995f-3948-9fb4-4f0f403d96de | -12.6647 | -47.302 | 2026-09-28 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| d21f1146-a232-3d0e-9479-9ac29d121796 | -12.6639 | -47.3469 | 2026-09-28 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9bc48ed0-2b47-3432-8940-663c4a4471d7 | -12.6643 | -47.3245 | 2026-09-28 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 396.2 |
| eb489cef-773d-3d17-9cd6-1bae05293a6a | -12.6263 | -47.3075 | 2026-09-28 10:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c0177553-5b7a-3b38-a548-95a4a2005bbe | -11.1771 | -44.8064 | 2026-09-28 10:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| ca9c91fb-f787-3ac3-8ead-a69c205eeded | -12.6643 | -47.3245 | 2026-09-28 10:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 37d3818e-9535-3710-adaa-c4e55bb4195d | -11.1962 | -44.8037 | 2026-09-28 10:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| d3d71192-7a5a-31f7-a37a-3ed72047afcc | -11.1775 | -44.7832 | 2026-09-28 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f206b3f1-73b0-3244-af93-24ada1d34609 | -11.1771 | -44.8064 | 2026-09-28 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ab298da7-5b50-3942-9eba-89fae878a418 | -11.1962 | -44.8037 | 2026-09-28 10:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 829ed9a8-e913-368e-bc9a-55b7db4fb0ac | -12.6643 | -47.3245 | 2026-09-28 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 92ab5d14-2e91-3d28-ae66-721fbf3887ec | -15.2038 | -46.1606 | 2026-09-28 10:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 93d50e10-be59-3f08-8388-a6a7701de861 | -12.6263 | -47.3075 | 2026-09-28 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1df4f21a-07ab-387b-96a0-815640a734e1 | -15.2038 | -46.1606 | 2026-09-28 10:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 659e828b-d6d3-3369-8d53-a66c46474ba6 | -12.6643 | -47.3245 | 2026-09-28 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2599f25b-b575-3b9a-97fd-3292def1d6e2 | -11.1962 | -44.8037 | 2026-09-28 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| bbb0bdd6-a96a-3f28-aaff-9c6881462e69 | -12.6836 | -47.3217 | 2026-09-28 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 3c0fd727-d3b8-3f90-b9a0-3e42a22069d5 | -15.1842 | -46.1642 | 2026-09-28 10:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 838d0c53-27bc-3062-a0b4-62ae74657edd | -11.1771 | -44.8064 | 2026-09-28 10:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 5bf1b8db-22e1-3999-af04-c887d558a2fd | -13.4873 | -48.5853 | 2026-09-28 10:40:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |
| a536b978-b855-3336-b34c-830fb846e0e8 | -11.1775 | -44.7832 | 2026-09-28 10:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |


[Clique aqui para ver as próximas entradas](README69.md)
