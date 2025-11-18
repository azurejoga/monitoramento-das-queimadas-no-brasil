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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba439381-6467-33e4-84e5-6aeffeefd6cc | -3.60669 | -43.61246 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ee86af4-018e-383c-9142-c63d633509ff | -9.39762 | -48.44726 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 330a1332-7778-3381-a6c5-3a855fa4d6a7 | -2.68717 | -49.1721 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b027a080-95a4-35f7-a42d-93419e6bcb35 | -2.86621 | -51.47326 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24446552-223b-3e42-b7b5-803f36366040 | -7.54087 | -47.05175 | 2025-11-18 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2e98dbd-4ef4-3ccc-98b8-de7efe408ecf | -2.47301 | -50.24577 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7287bca7-94fb-3f4e-aa23-3c8c331b7918 | -6.71487 | -47.79879 | 2025-11-18 05:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06800763-a880-3d1b-ae83-be3c228d3962 | -3.23906 | -50.50852 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0892b35c-d494-34d0-8f69-5eb7c6af54cf | -3.23969 | -50.50429 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323ba472-b3be-3cdd-8b9c-0021b5274e5a | -2.51578 | -47.8208 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96278898-6fec-3b7a-bb51-cc5882f16e27 | -4.17037 | -44.23491 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd4b7533-5877-3a13-b475-b4aa2fd17c89 | -3.23034 | -50.49956 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd0a2de9-9679-3463-a9f0-0e5f0a0a4c71 | -3.17583 | -48.03229 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7e05dde-9bb3-3cf1-8259-19e867878205 | -7.86023 | -46.87003 | 2025-11-18 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d8b5be6-e14a-3a5b-9418-9736cce0e0dc | -3.24405 | -50.50493 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce330003-6dac-382c-a1ea-b8ffb5dfb581 | -2.47432 | -50.23726 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 901a34ea-bdc7-3b42-90e5-49e877087c30 | -3.27155 | -50.02603 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 331b2347-378d-336d-82de-518b1c070b6e | -2.51013 | -47.82303 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc531025-51c7-3ab3-b522-0228a7ef74f3 | -3.6648 | -50.21853 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45516acb-d51f-3a92-88eb-01b5380358a3 | -6.09373 | -51.26892 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d9ed1b8-d004-3260-8f67-b828d309cff4 | -3.49627 | -50.44125 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8db10a96-bfad-3937-96b3-31ddd863c546 | -2.47739 | -50.24644 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97fb94ab-dda1-39c7-8462-243f556bdc06 | -4.26632 | -50.61374 | 2025-11-18 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ce6a105-5c9a-37f6-97f0-c40529d8295a | -2.33687 | -55.7997 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6cfa7f1-e57f-3246-aecb-ec3318c07c88 | -3.23537 | -50.49588 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 677ecbea-0a42-3449-b4ac-8bb3ce029dba | -3.17669 | -46.60793 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 364ea2ab-bea5-34b2-b116-b1583acb7636 | -4.17623 | -44.2415 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd53d9a3-99a9-3f56-871a-6fe909a8fc62 | -2.24485 | -53.625 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d93ab4d-b3e5-3b3f-8b3a-6dfc3155b691 | -2.88839 | -53.28478 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94400eb4-b251-31a1-a08f-bb20712af6d7 | -2.86668 | -51.47264 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 339e5fcb-c4fb-3da5-93aa-a39ce213263f | -3.46995 | -46.06976 | 2025-11-18 05:10:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 741c5e06-794a-3817-9577-97cf694bc0a4 | -2.91943 | -47.85157 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33d21e30-052c-3413-9dc2-bb9bc329e1d2 | -9.71946 | -48.91278 | 2025-11-18 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a85e5e-6f91-3ac0-b7c1-99dcdf8724e8 | -8.16038 | -55.10026 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b804fea-6e56-3790-bda9-d2795f49a344 | -8.15685 | -55.09972 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21f9d806-3321-3474-b3ca-060f779fd4a5 | -2.8249 | -48.55004 | 2025-11-18 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e29eb082-9ec0-3150-81da-1c8d8da2416f | -3.30248 | -50.07977 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9016f2e-4d47-31bb-a59c-05ae5d5a6ffd | -6.20392 | -54.72211 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbc565ec-74f8-35e5-a459-8f54df9d9f3c | -7.85427 | -46.86918 | 2025-11-18 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edcbc694-66a0-3bb1-8b23-cc30eb95361a | -3.22828 | -51.18132 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b308d8ba-ef8c-3914-88e2-b5f8fb0c9bdd | -7.33408 | -46.16935 | 2025-11-18 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 296638d8-e97b-3b89-b4b7-c6622288ec22 | -8.46532 | -47.97875 | 2025-11-18 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 770a2dbc-d0e7-3479-8dcd-23a13f27fad4 | -1.61536 | -55.85001 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05cf4b41-fe3d-3984-adcd-0093125e406a | -3.49343 | -50.33941 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13910e7e-77cd-3163-b3ae-81801efe6f41 | -2.49402 | -49.34319 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6d08ad1-0b26-3947-a054-06306c9ab0b3 | -3.5149 | -50.34712 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1cd9331-a83f-3cdb-b09b-7984d890dd75 | -2.98082 | -51.07889 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b6c6fd1-bfe8-378f-8367-32a0785c627b | -6.94129 | -49.66566 | 2025-11-18 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2caa7de-31f5-3771-88c8-1a54f3e1e6ad | -1.97957 | -56.46996 | 2025-11-18 05:10:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b77a050e-235a-3bd8-bdb0-ce0563a4cb3b | -2.47367 | -50.24152 | 2025-11-18 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bca39832-e030-3ccd-87ee-85b9ab4340b8 | -2.52287 | -47.80909 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdcbb25b-aea9-3c19-abe2-0d2069a2f3c1 | -3.02865 | -47.84002 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec066ab0-65e4-318a-939e-556fe082302b | -3.10541 | -53.14037 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebd861b-9425-3096-9864-c116c9237183 | -3.51137 | -50.27974 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e888999-282f-3619-9ed0-b7cdb7f1aa34 | -8.38501 | -44.06507 | 2025-11-18 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 700b436d-78e2-35cd-bb83-4493684ec5d8 | -1.48264 | -54.20045 | 2025-11-18 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1976de28-aeff-3983-a4b5-0c6e05f7d85f | -2.39969 | -55.7029 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbad90f9-e641-3249-bdb0-0700220981c2 | -4.17448 | -44.23181 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 065676ad-85c2-3ff0-b6ec-067780927ca7 | -3.02295 | -47.84246 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2eb8f24-5411-33d1-9d54-d2432b95b6ff | -3.0725 | -50.23749 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81acc1d4-dc88-3b7b-ba91-9be52df2f5e2 | -2.52363 | -51.18411 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90398823-3d83-3e16-b9c8-fb12c5a88e4e | -3.23659 | -50.49513 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c442353-5b57-3e60-8f30-d6f4699f3fbd | -2.24547 | -53.62098 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c3f608b-9389-3d04-b35d-bf65491240c1 | -3.23034 | -50.50725 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 681d4f36-d76c-30b3-9b45-b3f90d6706a0 | -2.53129 | -51.18907 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2a6ac1f-71de-388c-9de1-3231b3bef720 | -1.83648 | -55.35103 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995daec3-bc84-3593-be1d-bed261719c56 | -3.30314 | -50.07533 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75e328a6-4921-36b2-88c9-eeb4e2f9cbaf | -1.76855 | -54.18999 | 2025-11-18 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce8d0142-a887-3550-a969-6fa8d6bcf71c | -9.39118 | -48.45364 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 32165e67-5288-3de7-8c2f-d326f7514574 | -8.46483 | -47.98244 | 2025-11-18 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f8e829-4281-3149-aa92-afd0c0e793d0 | -9.53402 | -48.34916 | 2025-11-18 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eae51262-ca8b-3a83-9d05-37f023b62597 | -1.80413 | -54.7201 | 2025-11-18 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec4a15c9-c3d0-3f83-96ee-4c56eb10bf29 | -2.47441 | -48.2278 | 2025-11-18 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b1994049-95f2-3693-8172-a5fb9ecef070 | -3.39881 | -50.18779 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31153af8-1eab-3f4e-b907-85ae1b55d731 | -3.17726 | -46.60403 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4c6f360-93c7-3b22-a286-615178773c37 | -9.40311 | -48.44808 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7456396f-db52-3881-abcb-ead0e95304b6 | -3.01089 | -51.34232 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a7db261-d6e9-3e7c-827b-d21fc0ea7be0 | -3.07378 | -50.22895 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cdc73c5-2642-3972-8fe4-65d5466efebe | -3.23973 | -50.49651 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95a1daf-9cb0-3dbd-996a-a26b62726f62 | -2.33741 | -55.79624 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cc3d538-c5f4-34c1-933f-e3dff73c3e91 | -8.57736 | -46.49441 | 2025-11-18 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0829016-1d56-3f8f-b92f-dfb31cfa1527 | -3.14171 | -49.89692 | 2025-11-18 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98d52601-f61b-3210-9143-b67322dc1cec | -2.99549 | -51.01077 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e409d45e-2dd5-32ae-952f-88a50857eccc | -3.08191 | -51.2628 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dee232e-a8b7-33e0-9ad1-5af92a8c6ca5 | -4.22329 | -53.507 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad6ad54-bbd9-3377-9839-555c75119454 | -4.1954 | -44.22879 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42f22696-306e-3c16-95ab-6f7e3d01d0e0 | -3.28032 | -54.85437 | 2025-11-18 05:10:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 65fa9fbb-d481-3948-b0c9-fc5c020de634 | -1.8047 | -54.71648 | 2025-11-18 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5421b91d-90de-366c-b0dc-c3c8ba7cf705 | -7.54145 | -47.04741 | 2025-11-18 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eae4a06a-fa0c-34d0-a2d1-3cd0a3ce1429 | -2.75667 | -48.42587 | 2025-11-18 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebfa3252-426d-348e-a8e8-dc3829a94cfa | -7.94577 | -46.82264 | 2025-11-18 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daee3f3d-91fb-314c-bc59-a8b8519d95cf | -5.56855 | -51.20161 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990ebf60-f64e-391f-b41e-a7cc383cc1c7 | -3.2982 | -50.67419 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f1ebed7-85f4-35da-b557-881291f343c7 | -3.23404 | -50.50441 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf6ea75-2cbd-3ef0-9d29-d04319a356cb | -2.515 | -54.81653 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0313609-aa21-3dd9-a552-220051ab3e45 | -7.42814 | -45.20333 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f01a718-3345-35c0-8876-a39254a90eed | -3.78025 | -45.59631 | 2025-11-18 05:10:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7f4cb59f-7902-3f9d-9dc1-d1ad10845ec2 | -2.53525 | -58.02505 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c272daa-a6d8-306c-8e22-a058bda429f9 | -2.5059 | -47.81591 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d04b6c9-82bc-31fc-93c4-c2d6181021f9 | -4.64268 | -47.95039 | 2025-11-18 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |


[Clique aqui para ver as próximas entradas](README49.md)
