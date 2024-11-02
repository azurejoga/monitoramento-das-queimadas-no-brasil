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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f70a3f61-290a-355c-8860-e042e7d80bd9 | -2.80508 | -49.32504 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2f4d81e1-3170-36d5-8d1a-8093da9e46b8 | -2.80238 | -49.22848 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99a5dc52-3867-3c8c-b39b-04fe7eac8f58 | -2.80116 | -49.21961 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac260133-7146-387e-ba86-ad2dea7498c4 | -2.79993 | -49.21075 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 911bc195-bbb6-36bc-acb5-3a3e7c3d97fc | -2.79744 | -49.33519 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2c9d4baa-e023-36df-b5f3-db0eccf31382 | -2.7962 | -49.32628 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 701b3b59-e77d-3517-a159-198e7c4e944a | -2.78855 | -49.33644 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c34ded8f-b32c-39dd-9188-220b038c0015 | -2.77966 | -49.33769 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f4ddfa8-3153-344f-bb40-a53c418e8336 | -2.75867 | -49.18676 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97007ba8-73e5-38bb-a3dd-a2cb5fa7aa3a | -2.75744 | -49.17789 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 395dbc10-b1ec-3715-9c96-20e5d2c69326 | -2.73919 | -49.30711 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e9e17082-555c-3d21-96d4-92cbbffb20cf | -2.72962 | -49.17278 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa6389ed-08c4-3c6a-8d31-b162c197696d | -2.72076 | -49.17402 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c992870e-679b-36a6-86a2-cca249bfedb7 | -2.71775 | -49.28293 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8b79fb6a-03bd-3933-8f5e-791abe697d02 | -2.7081 | -49.29012 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ab96366e-5f33-384a-b623-940ccbbc9bfe | -2.70686 | -49.28124 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1c5d4409-f313-341b-a536-440159f3356b | -2.67753 | -49.33067 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12341d9a-2771-33f9-9b89-f1e9b4e61f13 | -2.65854 | -49.32427 | 2024-11-02 00:54:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06814954-d8e9-3add-b372-54c94466d05c | -2.65756 | -49.25198 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e9ac79ad-522d-3b59-aab7-2e6d99cd1042 | -3.55052 | -50.31334 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a3a0b8c9-4a90-3089-b457-fad67761375f | -3.52418 | -49.92157 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be447d4a-7d9a-3d79-804e-71c3ec66e0c9 | -3.50862 | -49.94275 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f6a20d74-47de-35f2-a870-2e81ea01b5af | -3.4769 | -50.37921 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2deb3d76-bdff-3807-ab87-533282c00b41 | -3.47556 | -50.36956 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d683ef3b-5d3f-3191-ac1e-c22cc4bc31ea | -3.47422 | -50.35988 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 958526e4-bfcf-3cde-b977-f033c0228788 | -3.46766 | -50.38053 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d5887d8c-e203-3293-96c4-8ac5792c109f | -3.46632 | -50.37083 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4d0f5ea5-8717-37e7-b501-e5fd3fea6158 | -3.4649 | -50.29248 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| ee1e786a-2c29-31f0-b33f-b231b34ac42d | -3.46357 | -50.2829 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d5bee1fe-547a-319b-bc2f-969b61ff36a1 | -3.4582 | -50.17666 | 2024-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a7f4ed97-bd13-3ac6-9014-63c30b43b718 | -1.5899 | -52.1481 | 2024-11-02 00:55:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 27cf6c04-f75a-3369-ac7e-881096b2f20a | -2.195 | -46.4634 | 2024-11-02 00:55:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| dd5fed03-a877-3e8b-b902-5712a793f506 | -2.2135 | -46.4629 | 2024-11-02 00:55:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6ff3ff24-dc5b-3215-85e6-eafce1548ecb | -2.2568 | -50.4376 | 2024-11-02 00:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| aa90e704-08ce-3748-bf95-12655a92868f | -2.2663 | -53.7422 | 2024-11-02 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1d4d6d44-a290-3eb7-8686-4e9622c47393 | -2.2847 | -53.7419 | 2024-11-02 00:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 29aae86a-60a7-3acd-b948-946a9a55c73b | -2.8386 | -52.8794 | 2024-11-02 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 10a76bee-8b8d-3743-92df-0d8e1fafa62c | -2.8509 | -49.3895 | 2024-11-02 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 40bc6da5-aa5b-3e11-a619-a58cc397b012 | -2.8555 | -53.3459 | 2024-11-02 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8f53e764-f8ef-3d19-b54c-77f03332556e | -2.8808 | -51.3179 | 2024-11-02 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 98dd4f09-b1f5-3807-a25a-234a9153dc3f | -2.8809 | -51.2972 | 2024-11-02 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1ebcf566-2e58-306c-af1e-8d5dcef3637c | -2.78 | -48.5806 | 2024-11-02 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fa3dbfd4-6920-3976-bb38-fe5fe933cc72 | -2.8056 | -51.7539 | 2024-11-02 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 33385f69-147c-31c9-af21-4bb194238204 | -2.8061 | -51.6095 | 2024-11-02 00:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 82700daf-8bef-30ee-9f60-4250b8200adf | -3.0088 | -51.5834 | 2024-11-02 00:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 46bbdb6c-0b6b-3ff7-a06a-66b02e252ba9 | -3.0734 | -54.167 | 2024-11-02 00:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ee901d41-c77a-3ca5-8784-7cd804ce9bb0 | -3.1767 | -51.0812 | 2024-11-02 00:55:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7aaa99b3-9a27-3c8d-bb13-b80364fed51a | -3.2249 | -44.431 | 2024-11-02 00:55:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 488b1a22-fb57-3692-b48a-38ae6c230f55 | -3.1097 | -54.2865 | 2024-11-02 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f56b0cdc-f210-32de-84a3-b1a149674b98 | -3.1098 | -54.2665 | 2024-11-02 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f8b1469b-5356-3825-89cd-88f6f7d8b2e0 | -3.1212 | -51.1244 | 2024-11-02 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8e34e80e-e921-3b28-8234-62f183d10894 | -3.1281 | -54.266 | 2024-11-02 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 0a9e22bb-08af-3447-9ddc-ba350c8fca71 | -3.1282 | -54.2459 | 2024-11-02 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 848952c1-ea9d-3c26-86f7-fb0a8c8f178c | -3.225 | -44.4081 | 2024-11-02 00:55:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 04a684a3-b575-308f-b78c-a2412a5d6730 | -3.2436 | -44.4073 | 2024-11-02 00:55:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| cc3ba352-765f-3f69-9fa7-2291a631361d | -3.3461 | -50.2609 | 2024-11-02 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 10fc3fc8-0f53-3df6-bc9c-d02c0e87df30 | -3.6574 | -43.6998 | 2024-11-02 00:55:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 577fb2e9-d580-3a49-885c-903b3c0736e6 | -3.7701 | -43.5554 | 2024-11-02 00:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| b6f38d53-0c7c-3245-a1c5-431480f98575 | -3.7703 | -43.5323 | 2024-11-02 00:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3fa81697-3db6-327b-a7cb-7337de675850 | -3.7888 | -43.5545 | 2024-11-02 00:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e793a59f-1a24-3d7a-a871-7df30db7ba04 | -3.7372 | -46.0545 | 2024-11-02 00:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 104fcc96-604e-34f6-9ae3-7360249a48fd | -3.7373 | -46.0322 | 2024-11-02 00:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f70d9e41-28f4-3cd0-9063-03c572a954c9 | -3.7558 | -46.0536 | 2024-11-02 00:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 428854de-561b-3ea7-8681-06cd6e7a7518 | -3.9473 | -48.3666 | 2024-11-02 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 521c0a02-a572-3157-88b3-db0a97af4d01 | -3.9474 | -48.3451 | 2024-11-02 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e96fbca5-249b-37a8-8f66-47e9f98d3b8d | -4.3867 | -43.4757 | 2024-11-02 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3e9d2337-dfc6-369f-83c9-39f054235744 | -4.4054 | -43.4746 | 2024-11-02 00:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e6e61500-b8d8-34cd-b64d-dc0e4a8cef54 | -4.3537 | -48.6068 | 2024-11-02 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8424f842-8d0a-37d4-a67d-6c3d85b9515d | -4.5575 | -43.1162 | 2024-11-02 00:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a9c44022-bb38-3c92-8dfe-57e46ed0f859 | -4.5577 | -43.0928 | 2024-11-02 00:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 6aa1e349-ea9f-3899-bc8c-c8c03b7bc952 | -4.6837 | -46.3852 | 2024-11-02 00:55:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e301badc-e56f-3604-a252-579d7d4f8fca | -4.8253 | -44.805 | 2024-11-02 00:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1c6073db-5a67-3165-85d6-f88e9c737535 | -4.8068 | -44.7834 | 2024-11-02 00:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ece9de1a-fefa-3a0f-95e0-691f75738f03 | -4.8255 | -44.7822 | 2024-11-02 00:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5a759726-b9a0-3af8-9a68-e6d43e14ef31 | -4.8362 | -48.5832 | 2024-11-02 00:55:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 361a7de0-5211-3584-9c9e-357cb82ed4f5 | -5.1146 | -46.0264 | 2024-11-02 00:55:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fe4ec0d0-316a-3e36-8639-755ae7f29a14 | -8.0276 | -71.3254 | 2024-11-02 00:55:52 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 6a7182d3-1d3c-335a-a55a-1064070aec2b | 3.41039 | -51.27392 | 2024-11-02 00:56:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e4fe7913-c61a-36f2-ab56-8b97a93efadd | -1.5899 | -52.1481 | 2024-11-02 01:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c776bb4a-fe41-3e0c-8727-051318866dfa | -2.1949 | -46.4855 | 2024-11-02 01:05:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 415fa642-5e3c-370c-82f7-3d26bf6811b2 | -2.195 | -46.4634 | 2024-11-02 01:05:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 6172f29f-9ce5-3e67-9293-d7ae5f50652c | -2.2135 | -46.4629 | 2024-11-02 01:05:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6eb88e07-7b7d-3372-ac88-0138380d3708 | -2.2663 | -53.7422 | 2024-11-02 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| bd5177a9-2fcf-39bf-9952-50722b33f492 | -2.2847 | -53.7419 | 2024-11-02 01:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ac59243b-ea61-305c-9564-be3e4aa9c1bb | -2.2568 | -50.4376 | 2024-11-02 01:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b729b580-31e2-39c5-9b01-1e7596f1cd91 | -2.8056 | -51.7539 | 2024-11-02 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a51dd133-a630-35f9-b1a5-878ccca00dc7 | -2.78 | -48.5806 | 2024-11-02 01:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 17aaf5a6-1417-3230-8aae-1d528bab77d4 | -2.8386 | -52.8794 | 2024-11-02 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 348d6f89-4190-3bd2-82df-6d407808dc85 | -2.8555 | -53.3459 | 2024-11-02 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 848569df-82b6-3995-83f4-58e30aebc400 | -2.8808 | -51.3179 | 2024-11-02 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2e8cc571-1fb4-3350-8e2e-53519f149739 | -3.0088 | -51.5834 | 2024-11-02 01:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a4f65e3d-8c36-3a89-9b26-c1a2d11807e6 | -3.0734 | -54.167 | 2024-11-02 01:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 89fb8e4d-93aa-392a-a470-187e42902fc7 | -3.225 | -44.4081 | 2024-11-02 01:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 77413436-20cd-323f-bf1d-955b5ddf14b1 | -3.1097 | -54.2865 | 2024-11-02 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6803cb93-7b4d-384f-8e8b-dda7688d7ec7 | -3.1098 | -54.2665 | 2024-11-02 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 6f3dd475-858b-3e40-b1be-8fe90bdef9eb | -3.1281 | -54.266 | 2024-11-02 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 11483921-3795-393a-83af-f03c0743c92f | -3.1282 | -54.2459 | 2024-11-02 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 0cef9790-732b-36e6-8539-aa25335f5602 | -3.2249 | -44.431 | 2024-11-02 01:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 473e7c00-6058-3d71-b525-38859c8aa42e | -3.3461 | -50.2609 | 2024-11-02 01:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 96d67a61-8992-3ea9-a575-8f37f4ab7b38 | -3.7701 | -43.5554 | 2024-11-02 01:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |


[Clique aqui para ver as próximas entradas](README16.md)
