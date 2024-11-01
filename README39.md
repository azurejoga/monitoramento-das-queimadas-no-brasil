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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ada16bc-268e-3e17-bdba-f01482da3d66 | -2.42376 | -51.9629 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfb266a3-7e1f-399f-9727-6bbcacaaaa2f | -2.42318 | -51.96642 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce531f66-0802-3573-8251-377f0c130ec0 | -2.41917 | -51.96577 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59a397a4-8cfd-37e0-8285-b24710194a7b | -2.4186 | -51.9693 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b3dbfea-4501-3cc9-9f9e-82b38187bba9 | -2.41743 | -50.50006 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98465f2e-6dd9-377f-b2e7-166ad5e1f4da | -2.41718 | -50.49787 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c26217f0-4898-3d5c-b9ce-b39a031decce | -2.41443 | -50.49516 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4b215e2-0aa8-3bb6-a288-0321dc2e05ba | -2.41375 | -50.49948 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5890fd14-5109-3940-9d5e-27d8b010f0bd | -2.4135 | -50.4973 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4a5d115-d392-3b8c-8462-85bf54510240 | -2.40556 | -50.43187 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8555f7a4-47fc-3758-9ad9-e05d62a47b33 | -2.35621 | -50.69688 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe6ca333-ebea-32e5-addc-a828d9a70beb | -2.29049 | -50.77329 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cb3b142-6184-3d5b-9993-990db896d78b | -2.2659 | -50.63008 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 623216a9-f408-327d-9675-d25fdba36ec6 | -2.26057 | -50.68823 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d200e721-3aac-319a-a4f9-1bd14e506e0f | -2.25312 | -50.68703 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f3ef77d-9e6e-3d44-9b44-e44039b36d97 | -2.24568 | -50.68584 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ff0169-ee6c-349e-b6a5-29cf94a8b252 | -2.24498 | -50.69028 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| befa01c8-a7b9-3ce8-8c51-9f3854279620 | -2.24287 | -50.70364 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d297bc9-cced-3b86-b6d5-f66836352060 | -2.23702 | -50.71643 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7446e029-b0f2-3573-8303-1f8665ed1f89 | -2.234 | -50.71137 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 912944f4-591c-3777-b18f-87ff5da34ce9 | -3.25701 | -50.96016 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c487184d-f86f-33bf-a5bb-f5b03986ee92 | -3.20453 | -51.16552 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da0462cc-225e-3ed8-b6cd-846f7b073e63 | -3.20378 | -51.17013 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55dc6bee-701b-3a67-991d-529e32724385 | -3.20076 | -51.16488 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12f719b4-20f2-3279-b4cf-9ceb34241fd2 | -3.20001 | -51.16948 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f36c1f59-7502-3b9c-a119-c39727b958ed | -3.18082 | -50.59471 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cee0b23-8594-33e9-a58d-a83d837576f1 | -3.17716 | -50.59412 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 629d21b2-5862-3c72-b56b-291abbbc5e2a | -3.1735 | -50.59354 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b83133ca-6bac-3aaf-9c83-d8b3bbc3efcc | -3.15562 | -51.13123 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1134db90-f693-3a8e-8700-a56f75fb14b2 | -3.14079 | -51.03082 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e32fdda-bd27-3f87-b9f3-003066a6e315 | -3.13705 | -51.03019 | 2024-11-01 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e8407ad-3a58-3c78-b5cf-5cba7ca84511 | -3.08487 | -51.28119 | 2024-11-01 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f71ff166-3063-3384-8b7e-1a516b62d4da | -0.68925 | -51.67262 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52887f9-585c-33ef-a36c-893b2173df5b | -0.68869 | -51.67619 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13bb3d22-ee69-3dc3-81a6-00b5aa3fdf72 | -0.68814 | -51.67975 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06aa8088-ad92-3068-95f1-692dc64c80ee | -0.68648 | -51.69043 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34ca80af-172f-33c5-b08f-fc894a539ab4 | -0.68465 | -51.67554 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99889624-fcfc-3008-866a-2144a015d64e | -0.68409 | -51.6791 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39c54f63-5318-32d8-94cb-94e588a0f572 | -0.68354 | -51.68266 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1aef515b-28df-3817-b1ae-50dd19f434e0 | -0.68298 | -51.68622 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec520a4c-d4cf-373c-88fc-3487c29d15ee | -0.11981 | -51.63889 | 2024-11-01 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcfdb71a-d4f0-3417-8ed6-df77abffe612 | -1.88962 | -52.06716 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ea3bc97-b78f-38bc-b66b-2ec7422c2db5 | -1.88736 | -52.1338 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c9739f3-a65c-31d6-8f2e-6b425cafaab2 | -1.85364 | -52.31854 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5caf058-9f0d-350a-8f10-82fff55ea14b | -1.73837 | -52.36264 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51831680-30b7-38af-b1c3-81d4a6baa00f | -1.7342 | -52.36197 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40def6ce-178b-379e-87cc-b188582692ea | -1.73186 | -52.34993 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f21f8f22-9fce-3b2f-b109-1f74775bd45a | -1.66254 | -52.13197 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46e20c0f-e0e1-330f-a570-f5367aaafeaa | -1.66195 | -52.13564 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0145841-030a-382f-b7f2-9725d875648a | -1.6388 | -52.25398 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fef94c0-eef6-3369-953e-8971bac79fdb | -1.63466 | -52.25332 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c0c6e30-de21-3d7e-99d2-7393c6034d2c | -1.60629 | -52.37675 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee2d5a5c-15db-3cb2-a50e-212d6eeaca34 | -1.60506 | -52.3844 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90567274-bd99-38d1-8430-6869660b03fa | -1.60211 | -52.37608 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 066f4e02-c0e1-3eba-a0ee-5323cd73cdc7 | -1.6015 | -52.37991 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19d71346-92fc-3cd0-85b8-34c3b7f56048 | -1.60088 | -52.38372 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36883200-40af-3bc1-a111-b9187084df08 | -1.60026 | -52.38755 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d1a2566-d794-3dd3-9b59-4f3f5a98af2c | -1.59793 | -52.37541 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0e645b0-5874-3107-8c8e-0f9143ebb349 | -1.59732 | -52.37923 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc7bd23-79b0-3176-b52f-0fd0d335c787 | -1.58315 | -52.13609 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 955c3e9f-53a8-3743-a510-73b20fea59cb | -1.58257 | -52.13977 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 66888905-84d9-314c-8950-186f8c19990b | -1.58199 | -52.14345 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 035718e0-2541-3f19-aff4-0362dd9e1e13 | -1.57962 | -52.13174 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dc3c716-a8e6-347b-bc8c-bc099485a43a | -1.57904 | -52.13541 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac6b198c-fa3d-395a-81d3-fdcdd5e47a7e | -1.57846 | -52.1391 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2220997a-1130-3c45-be75-f3242700fc79 | -1.57502 | -53.10306 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b43f5bf9-ae3d-3f0b-a2c1-d334515566d7 | -1.54617 | -52.07737 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af1e999-3933-3d83-b5b7-cbb16372ed6a | -1.54326 | -52.04322 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85a9fcbb-1a56-3cd0-90b9-bb5f421f53e6 | -1.53511 | -52.01584 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28b4316f-59e5-3a51-9450-e769132f04a7 | -1.53379 | -52.12815 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d71753b1-e6ff-33fb-82ba-d3e7421c5b76 | -1.53103 | -52.01519 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bbd0327-6fe4-3579-a7e1-bc073d33eedd | -1.52967 | -52.12749 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b92f90f9-aa39-386e-9581-ff41279ed5a5 | -1.52675 | -52.11946 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f070eea9-43cf-32a3-87cc-e3b594688ec8 | -1.52615 | -52.12315 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f502bcd-8ee7-3f17-94e6-321ecc74b907 | -1.52264 | -52.11881 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66818d0e-c834-3c9f-849f-1d156aa0176f | -1.45928 | -52.31606 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58c6a6a8-091f-34fe-a9fd-068420d7363c | -1.4338 | -52.20745 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7d856352-fa59-39aa-85b1-24e8da031ff8 | -1.43026 | -52.20305 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1f3d5d8a-5d2b-3c56-bb71-c99480df998f | -1.42966 | -52.20679 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 334b9d5c-10f7-35eb-a473-0a66f7343224 | -1.42612 | -52.20238 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28577f76-05b1-3730-95d7-8ee443d883bd | -1.42552 | -52.20613 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 12feee0f-81d0-350d-b229-ebd160bbeb29 | -1.42198 | -52.20172 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 818b9c32-f69f-3c43-9b48-7f9c40c72372 | -1.41837 | -52.22421 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af819e2f-9198-3c1d-afe5-3dbb8e646b40 | -1.41783 | -52.20105 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec88e46c-6d2c-36df-a7db-f872520140e0 | -1.41723 | -52.2048 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 589a13ac-e888-3728-a8b1-3115bbcfa184 | -1.41663 | -52.20855 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b077474-d762-36a6-aec0-404120ef1efa | -1.41249 | -52.20788 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2965a496-07a1-34c7-95f7-0b54622a18e0 | -1.40472 | -52.22971 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7185d541-028b-358d-a618-dbc90d38317f | -1.38713 | -52.95469 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88fb0de-945f-3c36-84a1-278f1870e7d0 | -1.27169 | -52.93923 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cad8f261-c9a0-374d-baa2-bcb45ac736e2 | -1.26822 | -52.93702 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d53c909-1a64-3064-9a8e-2da3c8044e24 | -1.27686 | -51.93738 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca5aaede-ffb3-3555-82a7-06d013db56e1 | -1.27278 | -51.93672 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0042df19-77e6-3ec6-95ca-f1966335228f | -1.22889 | -51.7651 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 519004ae-f6f2-389b-96ac-7a7e46dc53e6 | -1.22834 | -51.76864 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93e7a185-62fd-37ef-8a0b-b53d6ef8a486 | -1.22779 | -51.77218 | 2024-11-01 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcde1218-c19a-3981-9e2b-057349e39d2c | -2.07752 | -52.29997 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317df363-a0ba-332a-b52e-e99a47c2466b | -2.05381 | -52.03104 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1c23f41-f943-3cf1-b368-2dcb18e32935 | -1.88613 | -52.0629 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8fd56c3-2be2-3970-8271-df230cbaa24c | -1.88326 | -52.13319 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README40.md)
