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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb47d05a-065c-3cc1-952e-d5829eb99e06 | -1.53676 | -52.11024 | 2024-10-30 00:35:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 965d6a33-55fa-35af-b799-fb7f5597187d | -1.05545 | -47.65003 | 2024-10-30 00:35:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 70ed5f35-3bc6-362b-b7d3-358ff64f82ec | -1.05358 | -47.63677 | 2024-10-30 00:35:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 99b4d6bf-ca7e-32c2-951f-c8986719f7a8 | 3.54992 | -51.27911 | 2024-10-30 00:35:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 423716df-9812-3129-8788-42ddad8ac7ca | -1.063 | -47.6452 | 2024-10-30 00:35:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8e790209-9e4e-3f43-8e2b-852a4136d317 | -1.1654 | -53.3745 | 2024-10-30 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 633d389d-dc21-3e3d-b59e-b88ea52475e4 | -2.2011 | -50.5852 | 2024-10-30 00:35:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d669abad-6e6c-3cef-89d9-a25de627a6b2 | -2.3906 | -48.9337 | 2024-10-30 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 79fb181d-7277-301f-81a5-8938bda45bfc | -2.833 | -49.2413 | 2024-10-30 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 99354536-340f-37ef-9041-a37cb7cd2ff1 | -2.8331 | -49.22 | 2024-10-30 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 9bc9316d-64fe-3e8b-90b3-5596dac6ef39 | -2.8515 | -49.2408 | 2024-10-30 00:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| b24e3116-f647-367a-bd71-4f96057407da | -3.0734 | -54.167 | 2024-10-30 00:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4a6c5d21-c782-30c4-aa0d-bff26b5a2502 | -3.0913 | -54.287 | 2024-10-30 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 8d016ff2-13e1-3010-9e1d-8d5259dccce9 | -3.0914 | -54.2669 | 2024-10-30 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cd86358b-b622-3998-a2a8-77a8c0c24b31 | -3.1028 | -51.1041 | 2024-10-30 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e2763f9b-2914-30e1-bc96-458e85961b55 | -3.1097 | -54.2865 | 2024-10-30 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| fc431b95-b82f-3f9a-a1c4-1754761f404d | -3.1098 | -54.2665 | 2024-10-30 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 07adedab-7c95-3e12-a419-37bddd5aba01 | -3.1281 | -54.286 | 2024-10-30 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1e909a90-14a2-3275-b1c6-9a032e9207a0 | -3.1281 | -54.266 | 2024-10-30 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 463f588a-3195-3795-aa67-be3a373ca987 | -3.16 | -50.6231 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 41cece4e-1c62-3805-a990-b28d6d9b33c3 | -3.1601 | -50.6021 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| d86afa77-4c0b-3ece-ae26-e21842146b07 | -3.1602 | -50.5812 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1290cc95-9fb4-30a2-81f1-ca7258f02093 | -3.1786 | -50.6016 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 1b00a2ad-c71e-3ae5-b12f-5d86703fff6b | -3.1787 | -50.5807 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| f4c2b74f-1134-37fd-9d4f-ffcb4a4ed517 | -3.2172 | -50.1811 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 84c7cfd0-e136-3dc9-a90b-67d894e479d0 | -3.234 | -50.5999 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b9a0e374-0674-3d3e-ae42-16d5c3cf8cd2 | -3.234 | -50.5789 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 49e39a9f-e6b1-3054-ba61-b7112706284e | -3.2534 | -50.3689 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 98cc82f4-c8f8-3030-96d1-f5a17321bf49 | -3.2535 | -50.3479 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.6 |
| f222f4d3-2066-3fd9-b338-50ba4bb8ce63 | -3.2535 | -50.3269 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 5218ee92-3d59-3fb7-8ee1-98c0dcc94ac3 | -3.2719 | -50.3473 | 2024-10-30 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| c2e4e211-d815-38af-8925-3a6ed71d69cd | -3.5171 | -49.2402 | 2024-10-30 00:35:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5e6472c4-525a-3074-9fbc-5c44dcc56b3b | -3.5172 | -49.2189 | 2024-10-30 00:35:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b66c644e-45a7-3657-96bb-00b78ab90c9f | -3.5356 | -49.2395 | 2024-10-30 00:35:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2b9174ad-be12-371f-8a12-3207390eba2e | -3.5357 | -49.2182 | 2024-10-30 00:35:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2ad09888-b658-3d4a-8fc3-8bf9fc6ef3d0 | -3.563 | -47.4066 | 2024-10-30 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7d7dd1ba-4381-3f91-af95-8daaaf822fcf | -3.5631 | -47.3847 | 2024-10-30 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 310.8 |
| 71fc1e97-33d7-306e-b59e-11724e9d58fa | -3.5632 | -47.3629 | 2024-10-30 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| e59b4c3f-a211-3a14-8393-ec2e7e33fcdd | -3.5688 | -50.043 | 2024-10-30 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 40bf95de-64a5-3b4f-b9f8-243f89b3d3f3 | -3.5689 | -50.0219 | 2024-10-30 00:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a8767fdf-d1e3-37c6-bdc8-8ba9baca1afe | -3.5817 | -47.384 | 2024-10-30 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| c07e0290-50c1-3c8c-a2fb-7f65927deff7 | -3.5818 | -47.3621 | 2024-10-30 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 08e91852-1f05-3e63-b2ec-16abb05c6f5b | -3.8036 | -51.1852 | 2024-10-30 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d5653bcb-90d8-3284-86c4-1f9943bd3342 | -3.8037 | -51.1644 | 2024-10-30 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 271.6 |
| 3424c8a7-9475-3b7a-a30f-703cf9fde0f8 | -3.8038 | -51.1436 | 2024-10-30 00:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b4714063-ece1-3744-983f-33d3695a7aaa | -3.9326 | -41.4957 | 2024-10-30 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 19babb2f-2b71-30c8-b578-f3a31c551936 | -3.9327 | -41.4717 | 2024-10-30 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 1a0c2bf4-2181-3d9a-aba3-8a5710cf3bac | -3.9513 | -41.4946 | 2024-10-30 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| ba74944a-c6e2-327e-8150-8e513d4346a4 | -3.9514 | -41.4706 | 2024-10-30 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 36fc318a-b073-3b4d-9c80-7bab6d272869 | -3.8221 | -51.1637 | 2024-10-30 00:35:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 958793c4-ea52-3af5-8340-b50afff07446 | -3.9486 | -48.1291 | 2024-10-30 00:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| f481a50b-b244-3cd0-a39b-047448995ebd | -4.0705 | -46.2836 | 2024-10-30 00:35:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d2fb7efa-8210-3dd7-b549-e9fbd4796dfb | -4.0911 | -45.9488 | 2024-10-30 00:35:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 68079a4a-3c07-3465-8ff5-19f735e255e0 | -4.2561 | -43.46 | 2024-10-30 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e890b0e6-8776-384b-a63b-d12acce7c887 | -4.2563 | -43.4368 | 2024-10-30 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| ae8eed94-9fd7-3bf7-842c-9608c0bf672f | -4.2748 | -43.4589 | 2024-10-30 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f7d95838-2a05-379c-ad5d-82f512e6ae34 | -4.2749 | -43.4357 | 2024-10-30 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| f846d89a-33e9-3876-81e0-25230c4e4e76 | -4.3473 | -43.779 | 2024-10-30 00:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 680d43af-65d7-3f3d-a1b0-d702c1600e19 | -4.2496 | -50.6677 | 2024-10-30 00:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 1315a9db-da3c-3caa-ac1f-026602e3b3d5 | -4.2679 | -50.6879 | 2024-10-30 00:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 73dfa06b-9450-317a-a749-bcad2cc43dce | -4.2681 | -50.6669 | 2024-10-30 00:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| d7861d47-5d7e-3586-9cda-5b23f1f2b28c | -5.2306 | -47.9566 | 2024-10-30 00:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 67dee8a8-8f71-3074-91ec-03d2ea6f0a3b | -5.2308 | -47.9349 | 2024-10-30 00:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1a133f50-3c63-3195-a8dc-1272141b4dc4 | -5.9788 | -45.3621 | 2024-10-30 00:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 141463e8-41bd-36aa-80e0-07daf6a8d1f8 | -6.8408 | -59.0519 | 2024-10-30 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ad6204cd-9f9e-3245-a361-24deb93c36eb | -6.8592 | -59.0511 | 2024-10-30 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.6 |
| a2d089e9-81a5-3868-bcb3-947a440bdd53 | -6.8593 | -59.0318 | 2024-10-30 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 045d2176-fd13-37fd-b65d-ce5a61b7663b | -7.8736 | -46.9065 | 2024-10-30 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 3fcaaa64-fd58-36b5-822f-ae02ed834f42 | -7.8739 | -46.8843 | 2024-10-30 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 6f523a96-f83f-3422-8c0c-a610d09572df | -7.8924 | -46.9048 | 2024-10-30 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b9d1941d-e316-380c-9c04-692ece41ef13 | -7.8927 | -46.8826 | 2024-10-30 00:35:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5c09bda0-e582-3f20-83cb-31da0c335143 | -9.5563 | -63.1411 | 2024-10-30 00:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 34c8a43b-0c97-3304-be74-221bf396ba70 | -10.6984 | -44.9186 | 2024-10-30 00:36:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e52b5dc8-e77e-3e50-aa0b-526c65d58da2 | -10.7171 | -44.9391 | 2024-10-30 00:36:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 8568d7e4-df0c-3fab-b54b-ce2eab9b47ed | -10.7175 | -44.916 | 2024-10-30 00:36:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 159.7 |
| e966bc0d-11cb-34d4-8b12-1dd3f4c56c8a | -12.899 | -45.0549 | 2024-10-30 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2a88917e-a045-3e72-8e66-7cba070dfce9 | -13.6891 | -46.1017 | 2024-10-30 00:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4c184d08-11dd-378f-b60a-4e6d9543841c | -19.5862 | -56.7136 | 2024-10-30 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| eef7dfe1-6cef-39ef-9e5e-80be02ce48a4 | -19.6063 | -56.7108 | 2024-10-30 00:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| c53af191-87bb-34fd-a404-3e5489482c78 | -23.9923 | -54.1106 | 2024-10-30 00:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 2c1f839b-b43a-3037-b254-35aa8ced88a9 | -2.2011 | -50.5852 | 2024-10-30 00:45:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 11b07aa4-2706-3849-8c09-8784c7626898 | -2.833 | -49.2413 | 2024-10-30 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 198.6 |
| d1410eec-3c3e-312e-b3d8-66a001809593 | -2.8331 | -49.22 | 2024-10-30 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| a1acca7c-73ee-3f68-8d68-9af1f162d9d1 | -2.8515 | -49.2408 | 2024-10-30 00:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6077d094-f400-381a-8ea7-0f198653d131 | -3.0734 | -54.167 | 2024-10-30 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2b77ff3f-dbb1-3bb3-8f1a-5505cabb69f4 | -3.0913 | -54.287 | 2024-10-30 00:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| cc4df875-f69b-3060-aa35-35f679786db8 | -3.1028 | -51.1041 | 2024-10-30 00:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 19a09a54-25a7-314f-811c-3bf2030889f5 | -3.16 | -50.6231 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 769d4c5b-1ff9-3675-bd05-1b7dba2b066e | -3.1601 | -50.6021 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e4a4ef1e-8b20-3b41-b66b-c6d3b38f5e37 | -3.1602 | -50.5812 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 58e840fb-2c7e-3bf2-9333-98569d9cf976 | -3.1786 | -50.6016 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d1ac51d5-7523-3068-bd8b-bf69356a23fa | -3.1787 | -50.5807 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| c9b5d878-04b4-39b6-a2e5-d8f6c6df587e | -3.2172 | -50.1811 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b54bfbf3-c14f-3dd6-89ef-7d58d819967a | -3.234 | -50.5789 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 74d3a9ad-50ed-3d9b-9233-611cd7873021 | -3.2357 | -50.1805 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ad42e242-b572-3ab9-9627-123df831e7fb | -3.2534 | -50.3689 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3b2797e7-8005-334f-bb47-c8be3da279ad | -3.2535 | -50.3479 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 3233ec16-4583-3d61-a30b-931df6994c09 | -3.2535 | -50.3269 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 44191193-3995-305c-8f13-22e6fb66abfc | -3.2719 | -50.3473 | 2024-10-30 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b1b6541c-06d1-30fa-8741-178c19aa471a | -3.5631 | -47.3847 | 2024-10-30 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 267.8 |


[Clique aqui para ver as próximas entradas](README12.md)
