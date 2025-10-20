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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68c57e58-cda5-39cf-96e5-c6e8779a27d9 | -3.3278 | -50.2405 | 2025-10-20 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1ee57a84-33ca-3c1f-8f0f-bb63af5e5ae0 | -8.0676 | -48.0112 | 2025-10-20 01:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6bd9d238-fa3d-351c-a429-e86fab96fe27 | -2.2527 | -51.9108 | 2025-10-20 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 7e452e39-302c-38d4-9636-0b9ee3f7d58a | -2.2527 | -51.9313 | 2025-10-20 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 38f682d9-d8e6-33c1-a8f3-2b2e30b05d50 | -2.2343 | -51.9111 | 2025-10-20 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e1a9d45a-4c9a-3838-89b1-9ed5e66056bf | -9.5721 | -40.3475 | 2025-10-20 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.7 |
| b41b1160-7294-3be7-a6ed-76fe42edbfcc | -4.4066 | -43.3118 | 2025-10-20 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2e623ffe-d99c-31b4-bfd9-4495016135fd | -9.5534 | -40.3254 | 2025-10-20 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.7 |
| c5d53b04-2cf6-32c7-be46-ecbfad3a8e82 | -9.5725 | -40.3227 | 2025-10-20 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 2dc56d62-549e-3b23-a7da-46ad13b86100 | -9.6401 | -64.7411 | 2025-10-20 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1f4fbef5-aeac-368d-8dc1-5bc9ce79e766 | -9.553 | -40.3503 | 2025-10-20 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| b2c81ca2-10c4-3f5d-afc8-5f9abb2e7a8a | -10.0204 | -47.0414 | 2025-10-20 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3ecfcd5d-a5e2-37b2-beb8-744554d2064c | -2.2343 | -51.9111 | 2025-10-20 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f8e5c8ec-528e-30a0-a143-e0bbccb54617 | -9.6401 | -64.7411 | 2025-10-20 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bf5c1d1d-4166-37cb-bba5-58a0a5ec4edb | -4.4066 | -43.3118 | 2025-10-20 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cad5280d-250f-3e12-80a3-758be17d975d | -10.0204 | -47.0414 | 2025-10-20 01:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c655f654-3ea9-32d9-96dd-90a8174afa6a | -2.2527 | -51.9313 | 2025-10-20 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b5f90b99-5d26-3c00-afe5-e49fdb91b4a1 | -9.5725 | -40.3227 | 2025-10-20 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| c26673dc-b688-3e90-b296-95381f84c446 | -2.2527 | -51.9108 | 2025-10-20 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| be14d654-86dc-3f5e-81c8-9fcc8b77eacb | -9.6401 | -64.7411 | 2025-10-20 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c307cd27-65ca-37b8-9b9e-d1d346948005 | -4.4862 | -45.3001 | 2025-10-20 01:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4bb7fff4-a89c-3ce8-81d6-9170e54a11e8 | -2.2527 | -51.9313 | 2025-10-20 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4a7f369a-ca2a-36c7-9111-d67f7dfe21c1 | -2.2527 | -51.9108 | 2025-10-20 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 50051800-820e-3862-b43e-1d58fe0e934a | -2.2343 | -51.9111 | 2025-10-20 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 39c511d6-cbc0-3ce2-9aa1-267d48970c8e | -2.2527 | -51.9108 | 2025-10-20 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 849dbb73-236f-3b36-8bd7-f7385a23ec64 | -7.1334 | -44.2402 | 2025-10-20 02:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d051fc51-c548-3052-84d7-5e62aae7c05b | -8.4348 | -44.1092 | 2025-10-20 02:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 58ad1a01-4d06-39fc-8861-a94a7d39640a | -9.6401 | -64.7411 | 2025-10-20 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7d3fe732-fa8a-3054-a4d1-b2d49cd53dd2 | -2.2343 | -51.9111 | 2025-10-20 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d642be6c-28d8-3bed-b94b-e99c368699c8 | -2.2527 | -51.9313 | 2025-10-20 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b432d95e-ffe2-3bc7-9ec0-bba075f3caaa | -9.6401 | -64.7411 | 2025-10-20 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3cd9285a-0a14-3a6b-ab72-2f9971876441 | -2.2527 | -51.9108 | 2025-10-20 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| cc91e3a4-2e43-3e83-a29a-c8a8414a3dc1 | -2.2527 | -51.9313 | 2025-10-20 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4174ff65-9480-3dff-84db-b707715daa36 | -8.4159 | -44.1112 | 2025-10-20 02:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a6043942-eab7-352c-afe8-59a1d959eff3 | -7.1334 | -44.2402 | 2025-10-20 02:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 754f9fed-16e9-3135-9d75-9cba55322daa | -9.5725 | -40.3227 | 2025-10-20 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 2f6bd3c0-90fc-3e55-9ca2-a20b313c7c0f | -4.8957 | -42.9307 | 2025-10-20 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 10ccaa2d-bfad-3144-a475-df0dc45f4530 | -8.4348 | -44.1092 | 2025-10-20 02:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1ee28042-b8a0-320b-9e48-91c26a5c5503 | -2.2343 | -51.9111 | 2025-10-20 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fa428c47-1003-340b-8c09-68bf44edb9ba | -2.2527 | -51.9313 | 2025-10-20 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 88376b69-5e82-395b-a77c-e30c3ad9a5c4 | -2.2527 | -51.9108 | 2025-10-20 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 80dca5a1-7399-3a57-a0c3-5a0ed368588d | -8.4348 | -44.1092 | 2025-10-20 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f5e00946-ec97-3220-92e2-4762200971e0 | -8.4159 | -44.1112 | 2025-10-20 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7a8b9db9-329e-38e4-a19f-987b41406ec8 | -2.2527 | -51.9108 | 2025-10-20 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e9fca210-3e60-373f-bf1e-d26b33ceb171 | -9.5917 | -40.3199 | 2025-10-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.1 |
| a4ac15ce-910a-3979-bf8d-8a33d09b6580 | -2.2527 | -51.9313 | 2025-10-20 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 75850372-5b87-3a25-ad26-20e657c24d79 | -9.5721 | -40.3475 | 2025-10-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 345.5 |
| 587eda57-f7fa-39b5-92fd-5dc2c1c314aa | -9.5725 | -40.3227 | 2025-10-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 529.3 |
| 901cd9dd-20b0-320f-8979-98f8bc68ac7e | -8.4348 | -44.1092 | 2025-10-20 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 61f7b2d8-68a9-304f-b5aa-c3426bf2b600 | -9.553 | -40.3503 | 2025-10-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 8d43bd76-4198-311e-b7bd-1099183e7b54 | -8.4159 | -44.1112 | 2025-10-20 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 405c061c-c5d8-30a2-8d61-bd74301fb702 | -9.6401 | -64.7411 | 2025-10-20 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2aecc6c5-e0d4-3649-984e-0ab4b9d6aed4 | -9.5534 | -40.3254 | 2025-10-20 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 190.2 |
| ffa99086-4a88-3d36-a61f-1133f671de69 | -9.5721 | -40.3475 | 2025-10-20 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.9 |
| a26e6529-7357-32c0-8bea-643e78175c9e | -4.8388 | -43.0282 | 2025-10-20 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cdd61ed7-0dfb-35d1-a49b-372e6edeb18a | -4.8389 | -43.0047 | 2025-10-20 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 6652744a-62f0-3aae-bd56-e1f1ea795d36 | -2.2527 | -51.9313 | 2025-10-20 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 37b4a2bd-f006-3702-a1bd-68c940e22f89 | -9.5725 | -40.3227 | 2025-10-20 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 164.7 |
| bdcc7f8c-8567-36cf-ba84-2e976730b6db | -2.2527 | -51.9108 | 2025-10-20 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 12a0081c-4fb9-3216-ac10-05e370589889 | -2.2527 | -51.9108 | 2025-10-20 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 1aae111b-272e-3640-b741-fa95a8b00b93 | -9.5725 | -40.3227 | 2025-10-20 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.8 |
| 422e4052-4bec-3cbf-9f2f-9bbb5d6d89b0 | -2.2527 | -51.9313 | 2025-10-20 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 952f2a90-2683-363f-9aba-d33d5999b4b2 | -9.5721 | -40.3475 | 2025-10-20 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.5 |
| f4ba0ab9-1ace-37a5-ac15-5953706ea863 | -14.2395 | -51.8004 | 2025-10-20 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 61b1b9fe-aa57-33c7-935d-a77a272933da | -9.5721 | -40.3475 | 2025-10-20 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.6 |
| f1b67925-f52e-32d3-ba16-a83ee7468246 | -2.2527 | -51.9313 | 2025-10-20 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 63fd1384-8301-30e8-a220-4dea147d5b2f | -14.2201 | -51.8029 | 2025-10-20 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e9b8cbba-c355-399d-9822-edc03128df73 | -2.2527 | -51.9108 | 2025-10-20 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| f81a4fa5-3ea3-3b9f-bfd8-b60e04494d52 | -14.2398 | -51.779 | 2025-10-20 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 78dff9d8-2577-3009-bbdb-c724793fca91 | -9.5725 | -40.3227 | 2025-10-20 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 162.6 |
| f71f993a-e4b8-300e-a9e0-d91690fc3d95 | -9.5725 | -40.3227 | 2025-10-20 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 193.8 |
| a7766815-d510-3b17-bb2f-49d57fcacc29 | -9.5721 | -40.3475 | 2025-10-20 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.6 |
| 62098c9c-0bc9-3556-b791-8746d74317e3 | -7.1334 | -44.2402 | 2025-10-20 03:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d56cb1bf-4c83-3587-98b1-efc41a119202 | -2.2527 | -51.9313 | 2025-10-20 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a9676de2-90df-39d1-93ea-6954f73f9d54 | -2.8644 | -50.7361 | 2025-10-20 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8b11c443-0088-3e41-99e4-d9c129c81774 | -9.5534 | -40.3254 | 2025-10-20 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 208d5523-d95f-3e4e-b1c8-32b0f7b935cf | -2.2527 | -51.9108 | 2025-10-20 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 000ad882-4fdf-3763-bcda-23c1d4c4dfce | 1.7118 | -55.7643 | 2025-10-20 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 95a825e0-234f-3cd6-8531-43aaad8af904 | -9.5721 | -40.3475 | 2025-10-20 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.3 |
| fe008078-884b-3a87-bf67-fd58c5ca1757 | -9.6401 | -64.7411 | 2025-10-20 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c8b23b02-efac-34ac-92f1-5e409330b788 | -7.1334 | -44.2402 | 2025-10-20 03:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b57a32b7-8ee2-3906-a738-da9be8532ae4 | -9.5725 | -40.3227 | 2025-10-20 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 51524597-01e9-3036-93d2-64d73274c87a | -2.2527 | -51.9108 | 2025-10-20 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 65c0e6a6-1f5f-30bf-af2a-339456f6e54a | -5.6265 | -43.64952 | 2025-10-20 03:21:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dad3b038-5c63-3526-a3e9-fe3329c781e6 | -6.2169 | -40.96948 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31e64d17-8a4c-3386-8a8e-a2013d4fabc5 | -7.11393 | -39.43506 | 2025-10-20 03:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3879854a-aa1f-30a1-abcd-06fe48024c3f | -7.5036 | -38.81696 | 2025-10-20 03:21:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74042e04-325c-3879-9597-45fe4894b531 | -6.30287 | -40.89218 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8ff77b4f-8d32-3e8d-8535-b5ac4b056724 | -7.0097 | -36.75182 | 2025-10-20 03:21:00 | NOAA-21 | JUNCO DO SERIDÓ | PARAÍBA | Brasil | 2507804 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8806813f-c2a0-3ec2-a2d1-96b193e091a3 | -3.59594 | -41.65302 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c271562f-7464-358f-80e3-a429d78acc25 | -6.51085 | -39.71888 | 2025-10-20 03:21:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b36365d3-a004-30e5-b273-2392d2c946bb | -6.31274 | -40.90379 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5b8ff648-d84a-3ed9-bbd6-9afb5b6eb795 | -7.29976 | -39.27103 | 2025-10-20 03:21:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e62d857-93b5-3116-8920-1c851dadaaf4 | -4.39692 | -43.32819 | 2025-10-20 03:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4697b1cc-b1d0-3221-8f93-708181ad02a7 | -6.30262 | -40.8932 | 2025-10-20 03:21:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1ae5f4cf-0c1b-34c4-a38e-050cf7f43340 | -7.01427 | -35.22644 | 2025-10-20 03:21:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 70328ff5-7882-3eac-9580-9efe727345d1 | -5.1024 | -43.2002 | 2025-10-20 03:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a26f4b11-24ad-3755-9be7-da8f1ebcc741 | -7.04248 | -39.21902 | 2025-10-20 03:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 58de2e5a-8e71-3136-8761-dd830465d978 | -3.59118 | -41.65685 | 2025-10-20 03:21:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c839c5f-375d-3137-8265-d181c1335ce2 | -4.18014 | -42.18394 | 2025-10-20 03:21:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README5.md)
