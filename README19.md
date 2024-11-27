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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e96cc9-f784-3fd8-8acc-59c4d461866c | -3.0949 | -53.2385 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 28cf41c2-e538-39bd-80df-391a97697621 | -3.5411 | -52.1442 | 2024-11-27 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0f23693b-b82b-302a-b179-f4d2b40c81a7 | -3.0949 | -53.2588 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 398.0 |
| 44d37068-d268-33e6-9aad-ed853b569207 | -2.9967 | -45.4809 | 2024-11-27 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 706cfa5e-21e1-39ce-8a01-89b5997cdc9b | -3.9674 | -48.0851 | 2024-11-27 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ed77fdc2-b77e-38ff-b9ec-e50672bbd7aa | -3.058 | -53.28 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3b2a8d9e-4e13-32e6-9e47-816cfd7aaab5 | -2.9968 | -45.4584 | 2024-11-27 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b1bcf5c7-b9bf-3be2-8dbb-eca015bd2b57 | -3.1877 | -48.4172 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3f94747f-d2d0-3523-a709-3a4f0adc57d9 | -2.8347 | -54.1125 | 2024-11-27 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5d46a1b4-25f1-302b-a0ef-50c8f0656881 | -3.5226 | -52.1653 | 2024-11-27 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 32cac606-d654-39c4-8912-0cc80fcec574 | -1.6813 | -52.4333 | 2024-11-27 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 94adeaee-227e-3cf9-9aac-3861c6139392 | -1.9562 | -45.7137 | 2024-11-27 01:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5be5559a-ed3a-3e89-8ad7-ff0c8b3f3d63 | -2.8346 | -54.1326 | 2024-11-27 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8e8ab248-26a7-3255-b7e4-abb55dd47fc3 | -3.1132 | -53.2786 | 2024-11-27 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e628e0c8-4e9f-3704-836f-824865292b7c | -4.1417 | -43.8135 | 2024-11-27 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d48c15ae-73e2-3f7d-b1bd-296dd4531eb4 | -3.0392 | -48.5297 | 2024-11-27 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| fa3b5865-2be6-39bd-8d77-ddaf6fdad9c8 | -4.1604 | -43.8125 | 2024-11-27 01:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 20c58a2a-1eca-3b7a-84fc-4254163bbef4 | -3.1876 | -48.4387 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 3c98cc69-98dd-3de6-a883-290acc095e95 | -2.824 | -46.8199 | 2024-11-27 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b79a5d50-c51e-3d98-83ff-cbe58c29ade3 | -3.0578 | -48.5076 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 619ff305-bd6e-3d14-ae50-5a0f6b09dda4 | -3.1506 | -48.44 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 75165b44-ead1-3ade-abcf-12d4e03b9a52 | -1.6629 | -52.454 | 2024-11-27 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 869fee0c-8f27-353a-ba5d-4f15e4df36d8 | -4.7383 | -46.5595 | 2024-11-27 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1b077e69-84b7-39fe-b244-22b5edd584bc | -3.1691 | -48.4394 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| c7982629-b407-3b56-a6d9-7a1572ac3fe5 | -3.0577 | -48.5291 | 2024-11-27 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 7f3dfea8-9ba4-3617-ae12-817f0d25a589 | -3.0393 | -48.5082 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 219654dc-703a-3416-af02-4ce305d9e3e1 | -4.7195 | -46.5827 | 2024-11-27 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d14bd7fd-2c15-3eda-8e52-3364ce483373 | -1.9561 | -45.7361 | 2024-11-27 01:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 94552260-d241-398a-97f3-7bd5f8a72865 | -2.8424 | -46.8413 | 2024-11-27 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 50f549b7-99c3-3f66-807a-721a4df694cd | -3.1692 | -48.4179 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| f6d024f7-cdd2-3bd8-8090-151898500a37 | -1.6629 | -52.4336 | 2024-11-27 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 74274aba-0625-3ec7-94d8-173030935361 | -2.6988 | -45.6481 | 2024-11-27 01:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ecbfb332-c1a1-32e2-ab44-c0296084b36c | -3.9675 | -48.0634 | 2024-11-27 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 83c9f9c4-1d36-3169-b008-64aaabdfc7a9 | -4.2114 | -50.899 | 2024-11-27 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ad63749b-a704-31b1-9dd1-7e513fb8b0b9 | -3.169 | -48.4609 | 2024-11-27 01:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d8738e06-941c-38a6-a557-92a551c45138 | -3.5226 | -52.1653 | 2024-11-27 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 0676a49a-84a9-39cf-baf1-ce8c60bf7311 | -4.7381 | -46.5816 | 2024-11-27 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 585aeac7-d073-3184-ab27-243be3b1236a | -3.169 | -48.4609 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f9f5719e-4f9f-3911-95e3-eb066f7003e9 | -4.7197 | -46.5605 | 2024-11-27 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ac239570-f2c0-3086-91e1-45024bcc96a2 | -2.8346 | -54.1326 | 2024-11-27 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 52931cf1-3c6e-36ae-a473-dafeec43ee46 | -2.9968 | -45.4584 | 2024-11-27 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 47e387ec-552b-36e0-acf7-ef2185498219 | -4.7383 | -46.5595 | 2024-11-27 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 642ba0e6-1a05-30d9-9a6e-8e39ab4fd768 | -3.9675 | -48.0634 | 2024-11-27 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| adb4c485-07e9-360e-89e8-1f1b0b4d6af6 | -3.0948 | -53.2791 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8a2bf128-68a3-3612-b991-0d0f677b5894 | -4.1417 | -43.8135 | 2024-11-27 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| d685aada-16fa-3f7b-9de3-be64c21a5270 | -3.1691 | -48.4394 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 227.0 |
| 67482aaa-3550-3852-b636-d525da0dae01 | -3.0578 | -48.5076 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 55f17688-29c9-3266-a67f-2096497c0353 | -4.2114 | -50.899 | 2024-11-27 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f5cd67d0-3068-36fd-b199-1c1dc071f884 | -4.1419 | -43.7905 | 2024-11-27 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 30da9263-1d67-38d6-a6e4-a6cdd82560f8 | -1.6813 | -52.4537 | 2024-11-27 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| da7e3808-90c1-3de1-a5d9-1bede8dab2ed | -2.8347 | -54.1125 | 2024-11-27 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5aff0095-6c76-32ee-8193-80da41102d83 | -3.9859 | -48.0843 | 2024-11-27 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f79b918a-e707-36dc-8396-5a964b9b807f | -5.9788 | -45.3621 | 2024-11-27 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1408f8c0-ad58-3ce6-bd47-21eb0238a1ed | -1.6629 | -52.4336 | 2024-11-27 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3acb55a5-be4f-3f8f-9adf-e722a6c6b659 | -3.5226 | -52.1448 | 2024-11-27 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 8f817c48-76ca-37b7-9b27-587e598bee71 | -3.0392 | -48.5297 | 2024-11-27 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 353296de-50ae-330f-b420-10d689e66e07 | -3.1877 | -48.4172 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| de94aff2-473b-3cc6-b823-d3e28bceffb9 | -3.1133 | -53.2381 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| d8b8d3d2-172a-3a53-ab22-4d67b89e7e72 | -4.7195 | -46.5827 | 2024-11-27 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2af37ab0-0ca1-3c51-a2a1-4aac8e17344b | -3.9674 | -48.0851 | 2024-11-27 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5dafd686-1f43-335a-904f-a07caf6bedfd | -3.5411 | -52.1442 | 2024-11-27 01:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 10c1ce47-a33a-3152-ae6a-95a95995f9f0 | -4.1604 | -43.8125 | 2024-11-27 01:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fea2e05c-2188-384c-a0cd-daae01ebfbac | -3.1876 | -48.4387 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 70207016-ec57-3d5f-90df-8a84879a48dd | -5.9975 | -45.3607 | 2024-11-27 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b03640b8-c70a-38bc-868e-1941b1903ec7 | -3.1132 | -53.2786 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3145ca61-d3b7-3574-8f2b-b7556395806e | -3.1506 | -48.44 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b7c749e1-f791-31f7-937a-f76b41337806 | -3.0949 | -53.2588 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 371.4 |
| c861b049-8a40-3f48-9b93-8b7d8513f49c | -3.1133 | -53.2583 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 346.8 |
| df12973d-4840-3919-8c20-9d6e673799d5 | -3.0577 | -48.5291 | 2024-11-27 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f2b6e102-a7f5-3d09-be72-5ff8c8429fdf | -3.0393 | -48.5082 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c4433248-d350-364e-97ec-77de4494023c | -1.6813 | -52.4333 | 2024-11-27 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 08d3012a-8cee-3a17-93ba-d328774f2087 | -2.8424 | -46.8413 | 2024-11-27 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7478a8f3-ecfd-3aec-8c79-f6b64b8e12b8 | -3.1692 | -48.4179 | 2024-11-27 01:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| d4c2c0e3-261f-3b46-8b09-e4904294b1c7 | -1.6629 | -52.454 | 2024-11-27 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 24ad3a43-9fca-3482-a1fb-397e68e15b4f | -3.0949 | -53.2385 | 2024-11-27 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| f8a45ab8-a0ea-394a-bb48-d1117db91283 | -3.9675 | -48.0634 | 2024-11-27 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d68687ef-72a3-3503-a954-9dcc7d82aa63 | -3.1132 | -53.2786 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 56a55363-58e3-36fd-98ef-07855ccb0e2e | -3.0393 | -48.5082 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 24a15076-ba19-3265-8724-5ad307e31feb | -3.5411 | -52.1442 | 2024-11-27 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3de921e2-dd40-3142-b123-a3a52923ba4a | -4.2115 | -50.8782 | 2024-11-27 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8b17cd34-72c1-3f2b-8064-18b5c2d6f102 | -3.0578 | -48.5076 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| f070a132-3cba-3e14-88bd-526dcecdd2ca | -3.9674 | -48.0851 | 2024-11-27 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 239000fd-dce4-3d7c-99c2-91d3635a3426 | -4.1604 | -43.8125 | 2024-11-27 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8ba8aebe-1e1b-3017-92d2-aba8a22eb44f | -3.0392 | -48.5297 | 2024-11-27 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 65b3d00e-e0f2-3482-a050-8dfbc686c3d3 | -4.1419 | -43.7905 | 2024-11-27 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 12d9d497-ccb7-3a4b-9e01-22f4c28a766b | -5.9788 | -45.3621 | 2024-11-27 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 944791d6-6b7c-3f2e-b8f5-19adb7c00475 | -4.7197 | -46.5605 | 2024-11-27 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 597a0f19-68cb-3bda-b510-8b37842ad5de | -1.6813 | -52.4333 | 2024-11-27 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4bde9507-0c40-39b9-a813-9f82bea82938 | -5.9975 | -45.3607 | 2024-11-27 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| d558972f-5dc8-3db0-b50d-adfb94ffdb1d | -2.8424 | -46.8413 | 2024-11-27 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 63ef6726-14e8-39f8-a26c-e772706a4ae1 | -3.1133 | -53.2583 | 2024-11-27 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 285.4 |
| b50df4b1-482f-33ac-b1c2-d1d3f30a83c8 | -4.7195 | -46.5827 | 2024-11-27 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9b503bd3-acc5-31b7-8649-92524d83dad8 | -2.8347 | -54.1125 | 2024-11-27 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9179ce61-7f3b-3348-87b3-c9410f267ae1 | -4.2114 | -50.899 | 2024-11-27 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 45793ef6-a6e1-3b4d-accf-3b578160750d | -3.1877 | -48.4172 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b343c3fa-88a5-35fd-b228-ec955abfbf25 | -4.1417 | -43.8135 | 2024-11-27 02:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e9cf2370-9e92-3b35-b013-bceb56822768 | -3.1876 | -48.4387 | 2024-11-27 02:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 46970de2-8f06-38d7-af68-83b2e4800004 | -1.9376 | -45.7365 | 2024-11-27 02:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4f2f8179-9fe9-3798-9dca-9030dbf38a50 | -3.5226 | -52.1653 | 2024-11-27 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 017bf44d-45bd-320a-9208-db154bebd5df | -4.7381 | -46.5816 | 2024-11-27 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |


[Clique aqui para ver as próximas entradas](README20.md)
