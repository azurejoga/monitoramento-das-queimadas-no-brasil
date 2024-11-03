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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 882a44b2-3d9c-351d-bfa0-0ab9b198065c | -2.8245 | -57.7031 | 2024-11-03 02:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9cd5b2f4-cb36-3846-96d1-457bd6c1633f | -2.8333 | -49.1562 | 2024-11-03 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 43cd8d8f-fa11-3990-b896-ddc4be75e504 | -2.8148 | -49.1567 | 2024-11-03 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f0c36642-76c7-332d-b4ec-235202a733fd | -2.7603 | -54.4149 | 2024-11-03 02:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 12a24b6b-f098-3d99-9516-07b5cc56e10d | -2.7602 | -54.4349 | 2024-11-03 02:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 5435a73c-f186-3b90-9d2a-be908cdec8e4 | -2.7419 | -54.4153 | 2024-11-03 02:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 6d0a9c3b-42cc-31c3-b2c5-ed5d96d1697a | -2.7419 | -54.4353 | 2024-11-03 02:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 8e4eea99-00c6-3bf5-8d7a-5d5e0d4f0bf0 | -3.055 | -54.1474 | 2024-11-03 02:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b525bd21-b47a-34b3-a0dc-9b7a660733e1 | -3.2415 | -53.3967 | 2024-11-03 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| dd0e5036-3384-39e3-a6d7-63ef3ef0f3fa | -3.1213 | -51.1036 | 2024-11-03 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a6fa59a5-eb0a-303c-ad59-9e13b626c891 | -3.1061 | -50.2686 | 2024-11-03 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 59c651c8-e727-3e82-aaf4-038bdb9a792b | -3.106 | -50.2896 | 2024-11-03 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 5ec376d1-bfca-311d-98ff-61345dcf3350 | -3.1059 | -50.3105 | 2024-11-03 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 7f459831-b370-3b21-8f1a-2a1c6483c5e0 | -3.0918 | -54.1465 | 2024-11-03 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| de2d53e0-cccb-3e0c-bd42-3718816e91be | -3.0734 | -54.147 | 2024-11-03 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 4d0710a1-2ce6-3dad-a479-05e11fc14a8e | -3.0734 | -54.167 | 2024-11-03 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| c7648cc0-7d92-3d0e-a60a-91c1fbfa4fc1 | -3.4749 | -50.3826 | 2024-11-03 02:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a726934e-1e10-392e-9a84-83c2e6a1981b | -3.967 | -48.15 | 2024-11-03 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 526c3642-2312-3776-ab89-22f0c8c51b0a | -3.9474 | -48.3451 | 2024-11-03 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9c7aeb4c-0763-376a-a982-f744b8e90b6e | -3.9473 | -48.3666 | 2024-11-03 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 99d2dd29-dc5b-36e0-8d55-9843c2d00ed2 | -4.4243 | -43.4503 | 2024-11-03 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 55f90746-18c3-3c20-b4a7-0cc38cba194c | -4.4241 | -43.4735 | 2024-11-03 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9dc1fae7-433c-3bc0-a14a-26fb88add65b | -4.4056 | -43.4514 | 2024-11-03 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 7e0c5ced-c669-3084-b272-c9da73841c84 | -4.4054 | -43.4746 | 2024-11-03 02:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c03c9ef8-369e-391e-af20-dfbdc0750be1 | -6.5239 | -41.4929 | 2024-11-03 02:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 15b00204-5645-30ec-b9cd-70d7e365455c | -1.2572 | -53.3938 | 2024-11-03 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| dd645874-b08a-3b03-b029-da741a8797b0 | -1.2755 | -53.4138 | 2024-11-03 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| f2131d04-6c8c-32f1-a3b8-d9d4fd5a5406 | -1.2755 | -53.3936 | 2024-11-03 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| ec2f544d-2fa8-358f-acbb-bd4c0cea29f1 | -1.2756 | -53.3734 | 2024-11-03 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0401109a-1c1a-39f1-87bc-aec453770f37 | -1.2939 | -53.3934 | 2024-11-03 02:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fa0f3012-4a90-3f27-ae6a-f0d488e993ad | -2.1746 | -53.6834 | 2024-11-03 02:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7e3e9c7d-e2ee-3d75-bc0e-883675492d51 | -2.2802 | -48.8082 | 2024-11-03 02:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cb6a9948-003c-3b87-b8b2-253ef788d9ef | -2.7033 | -49.33 | 2024-11-03 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ba2a23b8-6c5d-3c61-9ee4-a434b9967aa3 | -2.7218 | -49.3295 | 2024-11-03 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 01dbfc68-625c-344d-bb2c-5e9592f7591a | -2.5696 | -57.1242 | 2024-11-03 02:35:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 6acc4a53-8606-3efd-83b3-bcc762fda291 | -2.5796 | -53.3927 | 2024-11-03 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 914de5a0-d4e6-34aa-83ea-39b49fbf91a3 | -2.5797 | -53.3724 | 2024-11-03 02:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4f5f9de1-22c6-39eb-b6eb-227b3ae0214f | -2.6321 | -48.5849 | 2024-11-03 02:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ed772698-28bc-3b7c-adf5-a25c383ae4e7 | -2.6322 | -48.5634 | 2024-11-03 02:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c8927edb-cb73-32f0-9587-76372bca9f07 | -2.6506 | -48.5844 | 2024-11-03 02:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1b922fb1-baac-3d0e-9e94-a606f6cce052 | -2.6507 | -48.5629 | 2024-11-03 02:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3a4d4313-5f87-3c91-abce-f89df68852d9 | -2.7419 | -54.4353 | 2024-11-03 02:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 39a9dac5-f2de-36fa-8afb-7c30f1638377 | -2.7419 | -54.4153 | 2024-11-03 02:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 696676ee-b5e0-3c72-9ec7-b7f908f45c61 | -2.7602 | -54.4349 | 2024-11-03 02:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 832330a8-ea1a-3ef2-b61c-5d3032e65f8b | -2.7603 | -54.4149 | 2024-11-03 02:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 370810bc-eeaa-35f7-9e1d-b1b52d07500f | -2.8148 | -49.1567 | 2024-11-03 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 40bf8ab9-f73a-36eb-93df-af2b10db182b | -2.8333 | -49.1562 | 2024-11-03 02:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 52b04c8d-4a11-32c0-a359-e1a67224d374 | -2.8244 | -57.7225 | 2024-11-03 02:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 8c4ffe23-85a2-34db-9208-5efd9f4da026 | -2.8245 | -57.7031 | 2024-11-03 02:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 3c301b9b-c894-3440-a3d9-d144949d2cd9 | -3.055 | -54.1474 | 2024-11-03 02:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7c46d1f6-c369-3308-a4bf-709d7e88416c | -3.0734 | -54.167 | 2024-11-03 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 3c6792f8-cdf5-323b-80fa-0ff8d865aca2 | -3.0734 | -54.147 | 2024-11-03 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| c88f4d6d-9f3b-3ab2-8730-b93efc306881 | -3.0918 | -54.1465 | 2024-11-03 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f273415e-3590-36ba-a1b1-61f095bb6324 | -3.1059 | -50.3105 | 2024-11-03 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9231c8e4-96ea-3bdb-973e-461bc2506797 | -3.106 | -50.2896 | 2024-11-03 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| f4af6751-d657-3ca7-a182-11804a9478c9 | -3.1061 | -50.2686 | 2024-11-03 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c4d2f276-f99b-3153-b63b-827032b50458 | -3.4749 | -50.3826 | 2024-11-03 02:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5bebf55b-1293-3060-94ee-04043a2ef602 | -3.9473 | -48.3666 | 2024-11-03 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| afcedb6e-d9f7-3d05-9f3c-60686821d97f | -3.9474 | -48.3451 | 2024-11-03 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f163228b-e4f4-31db-ae43-0b5ee7fab94e | -3.967 | -48.15 | 2024-11-03 02:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e3d8e128-b512-3662-a532-f4c7a7358c6d | -4.4054 | -43.4746 | 2024-11-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d71e9096-651c-385c-a821-4d3f8cfb041a | -4.4056 | -43.4514 | 2024-11-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ba618851-0a35-36f5-93e6-eed82d62e1dc | -4.4241 | -43.4735 | 2024-11-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 454c7a9e-7942-3d10-9d72-b3c28211a288 | -4.4243 | -43.4503 | 2024-11-03 02:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 9fbd178b-0fd3-335f-b356-7387e7f48297 | -6.5239 | -41.4929 | 2024-11-03 02:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 4ed813e0-d6cd-314a-b402-e501ba5ff8bf | -1.2755 | -53.4138 | 2024-11-03 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 8350ba4e-a2cf-3adb-b125-bdeb5b0a1a89 | -1.2939 | -53.3934 | 2024-11-03 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 0e956e3e-b6d6-316d-9b4c-81bcc8abad7b | -1.2939 | -53.4136 | 2024-11-03 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b906dc40-5d80-3e6a-867a-343130b599db | -1.2756 | -53.3734 | 2024-11-03 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3830d292-f24d-3bdb-9acc-7979afcfca79 | -1.2755 | -53.3936 | 2024-11-03 02:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 7158a01e-b1a8-3957-8567-a21753e661ca | -2.1746 | -53.6834 | 2024-11-03 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6dc9ddfd-25f0-385f-9b15-4858ae408347 | -2.2802 | -48.8082 | 2024-11-03 02:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 88a2710d-ebbc-382c-a480-3090597ae318 | -2.7218 | -49.3295 | 2024-11-03 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7b0b72a2-eabc-3af1-bc35-1b727ee5d519 | -2.7033 | -49.33 | 2024-11-03 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5d85a719-be23-3d82-980a-d98bb6af7df7 | -2.6506 | -48.5844 | 2024-11-03 02:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 54428c4f-b9cf-3fac-ac95-91f9b954d270 | -2.6322 | -48.5634 | 2024-11-03 02:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1c3f41f4-d705-3c63-9dca-34c69a5df2b6 | -2.6321 | -48.5849 | 2024-11-03 02:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 387c57fe-dc02-3341-8fad-afabd32410af | -2.5797 | -53.3724 | 2024-11-03 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 27758f9b-77d8-3c2b-9155-10837e82ba22 | -2.5796 | -53.3927 | 2024-11-03 02:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d5570dff-26d5-36ad-933d-f59e1b7cbaed | -2.8148 | -49.1567 | 2024-11-03 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| aa2447d4-0ae1-3c86-80fe-07584ccfdc5c | -2.7603 | -54.4149 | 2024-11-03 02:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 4489672a-0d39-3c81-b5fe-d1eea2a2aa2b | -2.7602 | -54.4349 | 2024-11-03 02:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 10dad0b9-c04f-3f02-a8e9-24bc728fdf51 | -2.7419 | -54.4153 | 2024-11-03 02:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| f2b29015-17f9-32fb-9b32-9d580ef7e901 | -2.7419 | -54.4353 | 2024-11-03 02:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| fba4c151-1aa6-3c81-8603-537639fd5f7b | -2.8245 | -57.7031 | 2024-11-03 02:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| dfba2766-bb46-34e6-b468-bfa946a6d0e1 | -2.8244 | -57.7225 | 2024-11-03 02:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 414c49f9-0e5b-3a64-9748-00e7bc4785b1 | -2.8333 | -49.1562 | 2024-11-03 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| db60dba3-a76d-30bb-b957-3f08f51fda6f | -3.055 | -54.1474 | 2024-11-03 02:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8f8174a8-09b0-3c33-8eaa-6f372ce929d3 | -3.1213 | -51.1036 | 2024-11-03 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e0dbcc2d-5446-3f1c-839d-c41cbbeb5ac9 | -3.1212 | -51.1244 | 2024-11-03 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 2fa459ec-9105-3ce0-a29a-de9445abdf12 | -3.106 | -50.2896 | 2024-11-03 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 6b5fc2d1-88df-322e-a6a5-964bed2ff6b6 | -3.1059 | -50.3105 | 2024-11-03 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 168378c8-4ee4-3c06-99bb-599925bde591 | -3.0917 | -54.1666 | 2024-11-03 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2f3fe0bf-997a-323d-a0de-953898928a76 | -3.0734 | -54.147 | 2024-11-03 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| ef06d1a9-f875-349b-a813-605d26775353 | -3.0734 | -54.167 | 2024-11-03 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 0e15c020-6cfa-3f14-818b-c7839ba6fafd | -3.4749 | -50.3826 | 2024-11-03 02:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d467211e-e18c-3061-8d4d-4f954121eb27 | -3.967 | -48.15 | 2024-11-03 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 15764855-9c0c-3308-98e6-017ebd4abbe8 | -3.9474 | -48.3451 | 2024-11-03 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 335c1b8e-f95c-3cdc-a06c-ec626439854e | -3.9473 | -48.3666 | 2024-11-03 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 440880e3-9110-3e81-8176-5a36784d9ae0 | -4.4243 | -43.4503 | 2024-11-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |


[Clique aqui para ver as próximas entradas](README19.md)
