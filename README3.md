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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d12d27fb-e9e6-3a7b-9db9-871ca9940442 | -3.89171 | -52.20874 | 2025-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 99130203-0666-3018-8390-91f31a7cd282 | -1.9655 | -52.10052 | 2025-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a27fe882-5b11-3ac6-a405-c9175dfdfd93 | 0.14791 | -51.42953 | 2025-11-02 00:54:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 73a3b9d2-22e8-35a4-9717-bafae4137b29 | -3.45837 | -50.22824 | 2025-11-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| b2a6a213-4cc3-3999-9beb-4eec905f6250 | -3.44184 | -52.63776 | 2025-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 24e9723c-18c9-3795-9201-dd9519c80713 | -3.55967 | -54.57335 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3cf92fcb-0926-3e59-8607-6fd24111108c | -3.71246 | -53.37391 | 2025-11-02 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 21308d0c-452b-3761-b062-7202b41a7354 | -3.58606 | -47.52042 | 2025-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 07b2fff6-5967-3d4d-92a5-54d8e07d5695 | -3.61451 | -51.47334 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ea6ca058-a20c-3690-8079-d6e199bf4526 | -4.58984 | -48.6771 | 2025-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ba97a333-212f-3b65-a6d4-baa9afe175e5 | -3.31996 | -52.57085 | 2025-11-02 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3f8e9cec-1e73-3b09-ae14-a9a03c5a86c2 | -2.44153 | -49.03827 | 2025-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0b5b9ed5-8696-3376-93f7-d193dba0e7df | -3.24395 | -50.80168 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 8710d3b1-4336-3fe3-9d77-f7676ca534c4 | -1.26281 | -54.09464 | 2025-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 33d0b240-a5fc-3b38-9612-0595e80256dd | -1.25634 | -53.84387 | 2025-11-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a2710c57-2480-3ce2-862a-d036e660161c | -2.94042 | -54.16429 | 2025-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 54fe948a-449e-3c7c-8ccc-1498e5e81a8d | -2.04639 | -54.22692 | 2025-11-02 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d134fddd-2db2-37d8-a8ea-c33fd50ea19a | -3.08221 | -52.9294 | 2025-11-02 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67d790fd-5ad4-30e1-9213-c1dfbd5d66ed | -3.02775 | -51.22374 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 8188739d-bc55-3eaf-a536-2c706c6a857e | -3.57112 | -54.59015 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c2f8d915-7ec9-3b3c-a6f2-272071a2473e | -4.71344 | -45.68793 | 2025-11-02 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a852da1e-8eca-3071-8a1b-f006f67e6fc0 | -3.22635 | -50.59401 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b46f4d88-4318-3b02-8c7f-e45cb84691f4 | -3.56986 | -54.58113 | 2025-11-02 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 457b7d1f-e2fa-34aa-9eb9-87649e933fda | -2.44499 | -49.04339 | 2025-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1cd3204a-9d78-360d-a7af-2489471a497f | -2.93133 | -54.16558 | 2025-11-02 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a56fddd-8758-3817-9731-ea85597ff55e | -4.13074 | -51.1441 | 2025-11-02 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| e676464b-3ced-3750-a687-e2a1378dbda0 | -3.91268 | -50.02997 | 2025-11-02 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 21567a9c-ae01-33d1-b0eb-1f6d4659a48d | -3.38309 | -52.37135 | 2025-11-02 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 630829e7-59ce-3ec8-9bbb-3b9c72e4a0d1 | -3.89569 | -52.09508 | 2025-11-02 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af26c0e9-debd-3c2b-a042-f1cc957bc0f9 | -3.24477 | -50.80722 | 2025-11-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c1951904-0f98-3df3-9368-0f4fdb53c800 | -1.963 | -52.10767 | 2025-11-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 78471f48-b364-34da-8e6f-4319f687b98c | 1.61634 | -55.6553 | 2025-11-02 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3f58c2a1-12ff-3248-a226-01d4fdaf0523 | 1.6265 | -55.64755 | 2025-11-02 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3908a930-83b4-3e93-9f58-73ca8b6e5080 | 1.63668 | -55.63978 | 2025-11-02 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0fbc028-e494-3bc4-88f3-850225c03024 | 1.6151 | -55.66431 | 2025-11-02 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f6e6079c-3ce9-35fe-b0b4-02af8733dbd8 | 1.62527 | -55.65656 | 2025-11-02 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ff0299d9-6ca5-3bae-828e-22a237541fe8 | 3.28004 | -61.15376 | 2025-11-02 00:56:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| fe426771-1237-3fbc-b4c3-3ba29102cec0 | 3.21087 | -60.20133 | 2025-11-02 00:56:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9815d649-57e5-3a84-9d43-2442eaaa75ec | 3.12698 | -60.71314 | 2025-11-02 00:56:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3f9b835a-b998-3d80-b6b5-355dde09ac6a | -18.5121 | -53.4856 | 2025-11-02 01:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 454445f9-f930-327e-9e81-fc297bc13760 | -4.6773 | -44.6317 | 2025-11-02 01:00:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 35b01989-97d3-3877-94cc-fba85ca64fda | -14.0351 | -43.4906 | 2025-11-02 01:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 511b9fbd-4c40-3757-832a-4baaf2a59796 | -4.1361 | -51.152 | 2025-11-02 01:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2bd6ec64-6d4a-3ac1-b6a5-61675a389687 | -14.0356 | -43.4666 | 2025-11-02 01:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 0ebcaee1-2a77-3356-a74f-016a410db8bf | -18.5321 | -53.4824 | 2025-11-02 01:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9639fdcf-ba61-31bf-8b7a-cb80ca9e5a1a | -14.0161 | -43.4703 | 2025-11-02 01:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2ceee768-9b24-3086-9d6c-38812f3178f0 | -3.5497 | -54.5752 | 2025-11-02 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 2e0662d1-e9c1-3135-944e-5c1bf000c013 | -4.5944 | -48.6813 | 2025-11-02 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| dc15a8bd-96dc-32b6-9de7-e3a0f6cb3be2 | -4.6775 | -44.6089 | 2025-11-02 01:00:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ebb7814f-a67e-362d-9314-fc0eda06f051 | -9.5156 | -40.3061 | 2025-11-02 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| c28e0914-d97d-3b88-a1eb-79af64f68259 | -4.7257 | -45.6914 | 2025-11-02 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1d348540-194e-3904-b993-39b6a2db19c5 | -14.0161 | -43.4703 | 2025-11-02 01:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fa5ab0b0-10cb-37f8-a6cc-66f930d5401c | -9.5156 | -40.3061 | 2025-11-02 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 245.2 |
| b9a49f89-e4de-3cc9-85f9-5c2f8a6f4113 | -9.5152 | -40.331 | 2025-11-02 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 36133175-5352-31b3-88e9-2b97f918d8fe | -4.7257 | -45.6914 | 2025-11-02 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 912ac8c8-edac-321c-8db8-dd99007eb39b | -9.5343 | -40.3282 | 2025-11-02 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.7 |
| b6fcb847-bc25-356e-9184-9678d9309fea | -14.0351 | -43.4906 | 2025-11-02 01:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 640c852e-8895-3927-b9ea-1c05c2b1f627 | -9.5347 | -40.3033 | 2025-11-02 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.7 |
| 01dcd579-5d7c-3bb7-8d28-846e1f489d9a | -4.6773 | -44.6317 | 2025-11-02 01:10:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 4fb770c1-a537-361f-84b4-9bc7ed58f24d | -14.0155 | -43.4943 | 2025-11-02 01:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 12a28ace-b213-3e5e-a69a-86ec32ad1aa4 | -19.0992 | -50.455 | 2025-11-02 01:10:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.8 |
| 99daccec-48e7-3c04-8fe4-b0aa127a104b | -14.0356 | -43.4666 | 2025-11-02 01:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2e978bfd-bc35-3898-ac7c-788e41f72520 | -4.6775 | -44.6089 | 2025-11-02 01:10:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 805ca4bb-443f-3c64-babb-0064d4f123ac | -18.5321 | -53.4824 | 2025-11-02 01:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9c126815-306d-3519-91cd-ea7659751c0c | -14.0161 | -43.4703 | 2025-11-02 01:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| d11aa427-39f1-3b4c-82cb-bb3b56fe0929 | -4.7257 | -45.6914 | 2025-11-02 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 89566678-c326-3cdb-a890-8d09e61352df | -10.413 | -44.9104 | 2025-11-02 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c23b73a4-a5b6-3eec-a1d9-c4cff724741f | -14.0356 | -43.4666 | 2025-11-02 01:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 9cc5b722-c058-32e8-a564-55041d60e4ec | -10.4134 | -44.8873 | 2025-11-02 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 81c4b27c-3a0c-3572-be6d-d69add162f1b | -10.9254 | -51.3619 | 2025-11-02 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 213b67c8-6b97-36cc-a996-43591fa8f03b | -4.7071 | -45.6925 | 2025-11-02 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ec4b55f7-e701-3854-aa78-6e9bb3424bda | -14.0155 | -43.4943 | 2025-11-02 01:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 9c3cf7c3-d632-3d61-8f71-ee697f998242 | -4.6775 | -44.6089 | 2025-11-02 01:20:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7d896665-f7b5-3a22-b566-dac9b2f10969 | -14.0351 | -43.4906 | 2025-11-02 01:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| c7b3cba4-1893-3e69-bd43-79df6ec5d08f | -19.0992 | -50.455 | 2025-11-02 01:20:00 | GOES-19 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 886a107d-9cef-38bf-808e-f382b2e692d9 | -4.6773 | -44.6317 | 2025-11-02 01:20:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 18884bde-f085-3317-ae2d-48a7174b4387 | -10.9251 | -51.3831 | 2025-11-02 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7a04db3b-162d-3671-96f0-e09ab50c2dbf | -10.4324 | -44.8848 | 2025-11-02 01:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| acdb98a9-12cc-33f4-a2d6-5e145bea3958 | -14.0351 | -43.4906 | 2025-11-02 01:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ad8a2db4-56ee-3540-ae94-8f9f44a046c9 | -13.3177 | -43.4552 | 2025-11-02 01:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 7c5b6522-0060-3505-b85a-5eb2a62ecbae | -4.6775 | -44.6089 | 2025-11-02 01:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3106d485-bb7e-3f19-baf3-debe6a0937ca | -4.6773 | -44.6317 | 2025-11-02 01:30:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 6b683602-91f4-3475-8586-8e677105ff47 | -14.0161 | -43.4703 | 2025-11-02 01:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f6c76ce3-b98c-3bd4-ad75-de0d751c1f8b | -14.0356 | -43.4666 | 2025-11-02 01:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| eb62ef29-e8eb-3e92-8f6b-db9e8c32c318 | -5.0399 | -43.6205 | 2025-11-02 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 15e05701-96a1-3817-8abe-2bf1442eb89d | -10.4134 | -44.8873 | 2025-11-02 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 49dfcafb-9ba4-3970-a6b7-8c0c356c1ad5 | -10.413 | -44.9104 | 2025-11-02 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 9b9cd099-23d8-308f-9640-76d005e5390c | -4.6773 | -44.6317 | 2025-11-02 01:40:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| fabdfa1e-8e3a-32ee-b619-9ae5e7812bb2 | -4.5944 | -48.6813 | 2025-11-02 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 51c22964-acd3-37b7-823e-1b867f42f394 | -14.0161 | -43.4703 | 2025-11-02 01:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1a7b80e6-24b7-3bb8-8a45-83eeedaefbbe | -4.7257 | -45.6914 | 2025-11-02 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 457804e7-6e61-3d59-8e60-10b32ebad0e1 | -4.6493 | -38.5615 | 2025-11-02 01:40:00 | GOES-19 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 2e287a5c-7451-34f7-ae12-af7e322bf473 | -4.7071 | -45.6925 | 2025-11-02 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 781e0905-1ca9-32e1-8e72-4588478b3741 | -14.0161 | -43.4703 | 2025-11-02 01:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9b7b813a-065e-3ea5-9232-f6ab5c671766 | -14.0155 | -43.4943 | 2025-11-02 01:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0b0857d5-8500-377d-b839-0928b89f57e8 | -4.7257 | -45.6914 | 2025-11-02 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 282ea6f3-55b2-33c9-9e3d-97770c6ac743 | -14.0351 | -43.4906 | 2025-11-02 01:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 780f2160-76f2-313d-a023-949a8dd73d4b | -14.0356 | -43.4666 | 2025-11-02 01:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5ddce9a8-ef10-3b92-b4a8-acdf2a4ba9d3 | -4.3349 | -45.6456 | 2025-11-02 02:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a29fd567-1ebd-302e-b4a5-ee13718044de | -4.3164 | -45.6241 | 2025-11-02 02:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |


[Clique aqui para ver as próximas entradas](README4.md)
