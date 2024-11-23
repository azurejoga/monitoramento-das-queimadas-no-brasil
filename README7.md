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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8014819d-803a-349a-bb3d-5924ae6d8c25 | -3.2544 | -50.1168 | 2024-11-23 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7aa78586-cfdf-3c42-9c43-97a0bfcbd3bd | -3.1831 | -54.3247 | 2024-11-23 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 13957fe3-e7f1-33f6-813d-4bcfbee4714f | -3.2201 | -54.2436 | 2024-11-23 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4e888be7-1d7e-3a5b-bc30-43c185676c5c | -3.7539 | -49.9941 | 2024-11-23 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 45003256-35fa-3293-901a-717b211a6164 | -3.2386 | -54.223 | 2024-11-23 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 68cc7fd8-c657-30a8-aa79-2a7b56c6bdfc | -2.8309 | -45.1493 | 2024-11-23 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 180.7 |
| d1e8fcc0-3d95-3da9-8a8b-bb3b5f86c86c | -3.2385 | -54.2431 | 2024-11-23 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 9bdfc085-885a-3fd0-911f-eb09ea866a3b | -4.5216 | -42.9078 | 2024-11-23 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 36d8f7a3-844f-3ddc-a3f1-870ae33ebe3f | -3.1831 | -54.3247 | 2024-11-23 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3286fa39-25ef-3842-9a9c-4b1f1c14aee5 | -4.5215 | -42.9312 | 2024-11-23 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e1e5610a-4b5d-3e59-944d-aa5b84e0d980 | -6.5054 | -47.0414 | 2024-11-23 00:20:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 552f0d38-5849-32a5-bbf2-04244ee24168 | -4.706 | -45.8493 | 2024-11-23 00:20:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| cb8166d3-cc75-3e68-8cce-cea38c81592e | -3.7353 | -50.0158 | 2024-11-23 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c33e0225-3d8a-3f54-9dd0-ed03da4674f7 | -3.6276 | -45.7021 | 2024-11-23 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| fbb07dad-d564-33b7-803f-5bf246459a2b | -3.2544 | -50.1168 | 2024-11-23 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 8292e186-bbe1-3b9f-8cd5-701f99d0929d | -2.7149 | -46.2713 | 2024-11-23 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| dc785565-9efd-3585-bb5d-0700eb16d1df | -4.1133 | -42.4614 | 2024-11-23 00:20:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 7803aa48-c176-374b-a6c4-4e00cc44abf7 | -3.7086 | -51.7888 | 2024-11-23 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c0bf0441-4baf-30ca-9c93-711d804d18b7 | -6.4867 | -47.0428 | 2024-11-23 00:20:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eb415a7f-55ff-3e2e-a049-900598056f11 | -3.2569 | -54.2426 | 2024-11-23 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| e21e8b50-6742-3bc7-89c4-d7b6e26326fa | -3.1138 | -53.1163 | 2024-11-23 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 4d459f37-fa93-35e7-a1a0-cfc458ad0e68 | -2.8308 | -45.1719 | 2024-11-23 00:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 223.8 |
| cdac99de-e36e-3538-86c0-610df74cfaa1 | -3.1138 | -53.096 | 2024-11-23 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 56eee8fb-8148-3af1-aa6e-c942e217b567 | -1.7359 | -52.7385 | 2024-11-23 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3ad71b7f-0676-320b-834b-2e237914ce2f | -4.6086 | -46.478 | 2024-11-23 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| c5de3dac-b0df-3475-a7ea-ffd968cf86fd | -4.5216 | -42.9078 | 2024-11-23 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 0d8b49e5-e85a-3869-a568-5808653b564a | -4.6085 | -46.5002 | 2024-11-23 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 2dda9f9e-f907-3ba4-b210-b47f20cadc02 | -3.7539 | -49.9941 | 2024-11-23 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a5b05d60-8529-3b4e-957b-bad9f50d0539 | -3.2385 | -54.2431 | 2024-11-23 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 32419e22-3ccc-384a-bd07-2efbad51629d | -3.5159 | -53.8132 | 2024-11-23 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| f156ad1e-5ff0-340b-b844-23f56c269d88 | -4.5403 | -42.9066 | 2024-11-23 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| ed40eceb-08e8-32de-960d-c8ea2afc8449 | -2.8123 | -45.1725 | 2024-11-23 00:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 196.5 |
| cc560703-feb1-3c87-a298-7f252130923d | -3.4662 | -48.2565 | 2024-11-23 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5df1e5d6-c5c2-3ff4-a007-7462268f37fa | -3.4663 | -48.2349 | 2024-11-23 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d8929213-9613-3536-99e4-341ad0f07c0a | -3.7538 | -50.0152 | 2024-11-23 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| b9b207e3-2e6c-3285-a14f-337240f85598 | -2.8309 | -45.1493 | 2024-11-23 00:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 272.4 |
| 606426b5-c683-3edc-8ffb-d0cecadd4d80 | -3.2768 | -53.8199 | 2024-11-23 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 71f37020-6102-3b26-9aab-c21a68578225 | -2.8124 | -45.1499 | 2024-11-23 00:20:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 84c746f2-d5c5-39e1-991d-4b5014383a84 | -4.5898 | -46.5012 | 2024-11-23 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b75f7af2-d879-3098-8a9c-971c321d6e2a | -4.5402 | -42.93 | 2024-11-23 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| af5f5edf-f954-3e75-bc9f-dbeec8082485 | -4.5614 | -48.0141 | 2024-11-23 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a768a095-eada-34e5-b3c2-bf0010e36c61 | -3.2569 | -54.2226 | 2024-11-23 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 1d414977-7ba8-3d09-b353-933f9b55a69c | -4.67 | -45.6722 | 2024-11-23 00:20:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 4afa582d-3592-36b6-9c74-5d48bfd57914 | -1.7175 | -52.7184 | 2024-11-23 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| aab5f8eb-ab49-38cf-9895-64495d4b915f | -2.6963 | -46.2719 | 2024-11-23 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 33837c63-57be-323c-b43a-122ac6c91779 | -3.2386 | -54.223 | 2024-11-23 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 60ebd23c-9be5-3a46-a7ab-c5c7cae1ba24 | -1.7359 | -52.7181 | 2024-11-23 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| c4b1f98e-58ea-336b-baae-4a531f085aa8 | -2.6963 | -46.2719 | 2024-11-23 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| acdf59fe-0561-390c-9a14-fc3ea5ee4385 | -6.4867 | -47.0428 | 2024-11-23 00:30:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| cfb26d4e-87ea-3982-abd8-c6f5cab4b88c | -3.7539 | -49.9941 | 2024-11-23 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| f117649e-0522-3ccc-93d8-4e625c0441bc | -3.2385 | -54.2431 | 2024-11-23 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| e036ba16-25a5-39f5-b787-2ebe24b8d9d6 | -4.67 | -45.6722 | 2024-11-23 00:30:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cb65bfa7-bc28-3385-9ac9-edec433bf96c | -4.5215 | -42.9312 | 2024-11-23 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f4854ae6-7c78-30c5-97c2-09c3576083ae | -3.7086 | -51.7888 | 2024-11-23 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| cfb7b257-9839-32d5-9865-670051e45589 | -1.1287 | -53.3951 | 2024-11-23 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 80418dff-72ca-398e-9ea4-e9fc5b2be487 | -3.1138 | -53.1163 | 2024-11-23 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c63abdce-b9e3-35a1-8484-9fe85eabac88 | -4.5403 | -42.9066 | 2024-11-23 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| d920e2a6-33ec-3427-b4b8-c16f60f019d2 | -2.8309 | -45.1493 | 2024-11-23 00:30:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 375.7 |
| ae494233-e3a3-3806-9093-d7501a6ae899 | -4.1133 | -42.4614 | 2024-11-23 00:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 3274eebb-5a09-3ebe-8c95-6f3ea6ffebe4 | -3.2544 | -50.1168 | 2024-11-23 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 33eeb833-bf2c-32d3-82c5-339f47b233e3 | -4.5216 | -42.9078 | 2024-11-23 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b8c2486b-e780-3bc6-a89d-28e9688f1e5c | -3.2569 | -54.2226 | 2024-11-23 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 8b56d4c7-627c-3f6c-98ef-6ce0aff612af | -2.8494 | -45.1712 | 2024-11-23 00:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 2edc6315-3f19-3850-992c-d7e5881a93d5 | -2.8123 | -45.1725 | 2024-11-23 00:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 24941a3a-e2e6-3b89-88f7-7043f3c4d3bc | -3.4663 | -48.2349 | 2024-11-23 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b23c4b19-1c40-3eca-af6f-323d91286ac4 | -3.7353 | -50.0158 | 2024-11-23 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 541cec4a-0bbc-3d73-9b92-6870fcde877a | -2.8124 | -45.1499 | 2024-11-23 00:30:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 242.6 |
| 0706cfef-bb62-3848-9393-700b25d39b63 | -3.7538 | -50.0152 | 2024-11-23 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| fe3db820-457a-3d09-9cb5-e151aed07cdc | -1.7359 | -52.7385 | 2024-11-23 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 04bed5c1-e270-367b-85cd-6bfc8dbaa1ad | -2.7149 | -46.2713 | 2024-11-23 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9c293d3e-b00f-378a-a63a-d520ba707036 | -1.7359 | -52.7181 | 2024-11-23 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 36603b1c-2ce3-3e8e-bc9a-ce400211a6bc | -3.1831 | -54.3247 | 2024-11-23 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 97e7d205-6a21-39d6-ac1a-d6abb342b099 | -4.5402 | -42.93 | 2024-11-23 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 583b151f-eaa5-3417-9e7d-2505a85cfdf7 | -1.7175 | -52.7184 | 2024-11-23 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 753a7def-abc0-3910-afb8-9e51142b2769 | -4.1131 | -42.4851 | 2024-11-23 00:30:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| f190eecb-bc43-3d25-b85d-ff608a68b7e5 | -4.706 | -45.8493 | 2024-11-23 00:30:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 2a73f3da-b907-30f6-82a4-fa7e917c6f1b | -1.7891 | -53.6495 | 2024-11-23 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 185a7229-6936-3004-8829-68b5c7629474 | -3.2569 | -54.2426 | 2024-11-23 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 12e64248-e910-3267-bbe3-ed8e3ba80be2 | -4.6086 | -46.478 | 2024-11-23 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 939d3ab9-3521-30b7-a5ad-42c4bd30c5be | -3.7354 | -49.9948 | 2024-11-23 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5a87e3a9-b558-3150-9c1d-72c882507233 | -4.4196 | -44.1204 | 2024-11-23 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0126b2f6-62bd-3766-8520-244cfb780fd1 | -3.5159 | -53.8132 | 2024-11-23 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| c51ffa8e-715d-3703-bebb-307e95c93bd9 | -3.2386 | -54.223 | 2024-11-23 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 50b4a024-5853-3f45-9b90-54221aa06b12 | -3.4662 | -48.2565 | 2024-11-23 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b57915ee-95a5-398f-909b-c91de735e899 | -3.7373 | -46.0322 | 2024-11-23 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c047787-23f9-37ff-9776-0d051da050b0 | -3.7372 | -46.0545 | 2024-11-23 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 057ada73-a7ec-3f03-bc97-c7b8de19badb | -2.8308 | -45.1719 | 2024-11-23 00:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 366.6 |
| c850320a-db34-3b3d-b477-b3b00f5343d7 | -6.5054 | -47.0414 | 2024-11-23 00:30:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b1e9ff15-7291-3e8c-991d-8121a324f7b4 | -4.6085 | -46.5002 | 2024-11-23 00:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 163.9 |
| c105d036-a510-31e7-9d8e-25bec502554e | -4.5403 | -42.9066 | 2024-11-23 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 47e26b35-b531-3372-8f50-9faeb763f47a | -4.1133 | -42.4614 | 2024-11-23 00:40:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 628a092d-0c56-33c7-9d8e-288c16b17d38 | -3.2386 | -54.223 | 2024-11-23 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 96d46d19-c924-3e33-92f1-7b798cdf2fe5 | -1.7359 | -52.7181 | 2024-11-23 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 270e7838-1c96-312d-89ad-bf8e734fd030 | -4.6086 | -46.478 | 2024-11-23 00:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 448c235d-f12c-3413-bf02-d915ac3082dd | -3.7187 | -46.033 | 2024-11-23 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 148.4 |
| f41e4c12-8ebc-357b-bf4f-ac143147c616 | -4.706 | -45.8493 | 2024-11-23 00:40:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| c26c6699-5e9d-30b7-8363-efd21ec7ce63 | -4.5215 | -42.9312 | 2024-11-23 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 711c9a62-021d-32f8-9403-f86bcc18c955 | -4.5898 | -46.5012 | 2024-11-23 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 243cee7a-010b-3d45-9436-0ec212e00c63 | -4.175 | -54.5761 | 2024-11-23 00:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 421cbd5d-a8e7-31b9-8d82-f29628824fd8 | -3.2569 | -54.2226 | 2024-11-23 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |


[Clique aqui para ver as próximas entradas](README8.md)
