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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e1340b-2f76-3eb7-8dbd-eaf1e75666e0 | -4.11075 | -46.95122 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6809da-8b54-317c-a014-94efea2f1eea | -3.85049 | -46.65887 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b99a8d98-933a-39fd-964e-0f2be40da022 | -2.99481 | -46.91291 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947885a5-d1b6-3b09-99bd-1ae093116072 | -1.1958 | -53.86438 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 063e50c8-ec97-3eea-9e33-1b5c20f8eb2b | -2.57682 | -47.00859 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9251383-bca2-3791-8b2f-283f58c175e7 | -1.1596 | -53.56669 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9af6a3a4-98e7-3813-888b-61ca7327e78c | -1.91964 | -52.6594 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eccfd1a-6b62-3aeb-a5c1-9a002e875ba6 | -2.72045 | -48.58845 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2bddd00-9993-37a5-9029-5d2ed8a6b17e | -6.91251 | -43.5349 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60861e02-baeb-3705-a867-842c494382b5 | -3.89287 | -46.68512 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ead83e1-4bf1-3136-8f09-eb30f29a0a65 | -2.2293 | -46.38997 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f40836f-63e1-37c0-8605-6ae2c34e36d9 | -3.57868 | -50.33856 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5e044c-3854-31ae-aaea-3aca65df9da3 | -2.81929 | -46.84444 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f24d8b07-2817-3064-b449-b73c22631546 | -6.12548 | -44.92477 | 2024-11-30 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50cbc486-36d1-3176-99fd-2d4d6740b32b | -2.14646 | -46.61401 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2360d6b-b451-3963-8918-367d0e720d0a | -1.47685 | -55.12947 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65e26bc0-a48c-3563-9ab5-c80251fb6156 | -3.70283 | -47.1435 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3469186-b975-3632-9493-6085d269cb50 | -4.82441 | -41.28192 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e4193716-0659-315f-99e5-524b1b8057b8 | -3.96586 | -49.91341 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 933f2813-5bae-3d8f-82b6-2b52a5d8e4fe | -1.49278 | -52.44192 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fc5749e-598c-3208-afdd-f3c1047976d7 | -2.5849 | -49.21823 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df41f026-d017-3b26-a525-0cb633983186 | -1.88494 | -48.6479 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86c9b769-e097-3e6a-8424-52789ae5271f | -3.16336 | -49.02058 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ed0d5a1f-9bb5-3f3b-bde8-719415922ee0 | -3.73539 | -53.37218 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 130af671-6246-3359-a4d5-9fdbf5c3ee99 | -2.92163 | -48.95787 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f74ee845-8b77-35e5-8ce4-f4f4cf399b7e | -3.73187 | -50.18892 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d30a5ff-ec4e-3073-b608-e35c64197910 | -2.89797 | -51.5766 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a946e19-1491-3276-8161-771af9ba563a | -2.62001 | -48.16344 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7787ab0-230e-3a65-9a50-1e604f112daa | -5.41253 | -49.08013 | 2024-11-30 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b18dc88-c73c-3077-af1c-440e8885182c | -3.27015 | -48.76975 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0e5234-4d2f-3513-b210-840210811d12 | -2.43439 | -50.4181 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c3bcbbd-41b4-3677-8e62-b22ac02c1777 | -2.31755 | -48.55375 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c39898c-5d53-3c3d-a9d0-269dfefa8637 | -3.27518 | -50.19306 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6fc7bed-e199-3286-b8b7-12d6d6493434 | -3.79566 | -58.97677 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed0ea155-8180-3f58-9f3f-4b28a7aa6dc0 | -2.30429 | -51.98678 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e035dd90-1dab-33e5-bd1b-5037a4511579 | -3.25628 | -53.62905 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 4cb86019-6cee-3263-9984-9431e30b96cc | -3.78635 | -46.69361 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 550aff64-9438-383a-8310-00f2c1f49b9b | -2.72849 | -48.66707 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ae75183-9c02-3203-97f6-8e1d10022bd9 | -3.0636 | -50.32793 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d8e9507-daaf-3b9e-9ce3-ea860a1ab4fb | -1.59429 | -52.28428 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00a4ec61-73f9-3fa2-a6b7-c65146bf668f | -3.79751 | -49.59959 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 603b1d23-abc9-3f39-99d8-0a823249ff33 | -3.97918 | -46.73752 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa5d5fef-f8e4-3926-905a-c696a10e38a9 | -4.19439 | -50.6838 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b33cac4-2c2c-3be6-b3f9-e9d42cdc3723 | -4.1207 | -48.48523 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c621790c-c117-3354-938a-f93cd2e24c49 | -1.72579 | -52.48862 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582fff7f-01a3-3095-b1b2-332cf9952a50 | -1.48045 | -55.37903 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64edd870-81d3-3240-8043-8389e2cdabbc | -1.69345 | -55.01372 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9835e07-8483-3503-a4a3-451f50d98de9 | -2.7794 | -54.21676 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e2cb3a7b-0c90-34fe-897c-de623eb8d40f | -2.61902 | -54.20591 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3478ddde-7ace-3889-9335-9145e53438ef | -3.93508 | -46.72291 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71d4a6f3-bc9c-35a2-968b-3c0ce4ce6014 | -3.12473 | -45.98009 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0758cb-b455-35f7-bc12-fcc3211ae07f | -2.37978 | -53.68394 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 710d5d40-2a67-35af-8e35-8945d6fe6cf7 | -2.23864 | -47.1324 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 714ffd4c-3b9a-34e8-995b-e15a7ed26150 | -3.38969 | -50.11382 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dccfe562-ca0f-3f7d-ab94-32f092b3633d | -3.94071 | -46.91901 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e789c7-b638-3dde-a2a8-7a12ea42ba27 | -2.69215 | -48.66148 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f86f52d-fd16-36a3-aed3-5dfbb6531647 | -3.35691 | -49.56539 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c023241-99cd-32f1-bd3a-8df0f19592b3 | -2.32453 | -46.34969 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcf736c4-e5ab-34a3-b1d4-4185479a3986 | -1.30378 | -55.74199 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df770442-b385-327f-aa60-4bb51d347619 | -3.85677 | -47.05595 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc6643de-507e-3799-ad78-c6bcaeb69547 | -3.99919 | -43.25439 | 2024-11-30 04:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38360579-3e54-3a68-b71b-0a6221c49e01 | -3.13162 | -54.18201 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a66bf32f-14c1-389e-96d6-8d0e56ae40f0 | -3.83784 | -46.52945 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ac0e2b-a512-3636-a84d-ca0ae11c641b | -2.60066 | -54.08294 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64d9e3a0-ee67-3cd0-8a2c-fa5e53f8755a | -1.655 | -52.25214 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0753f64d-e4d0-34d2-adb7-9c6b5bb9a3a3 | -3.49331 | -53.80576 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74f0c38a-1d22-304f-9531-3e33a7e69370 | -6.14067 | -43.94975 | 2024-11-30 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c702a30-b5ba-3b1d-abe4-2b82272c0949 | -3.15599 | -50.5853 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b28d403-1d1b-3c24-8d56-08219250923b | -3.99248 | -49.9389 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2e66fdb-c05b-3b15-b606-17a86ae914af | -1.05441 | -53.21672 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c7e412c-6213-3968-9ab7-3ccf17faf64c | -3.8169 | -52.24595 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68a5385b-4484-3a0d-a69a-ae4222238268 | -1.56192 | -51.26462 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bcab7da-e7dd-397a-9710-514c3574133c | -2.28594 | -46.43781 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 204d7284-fba1-3297-b7d1-eab02393620b | -2.16713 | -50.60098 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de8c0c06-f320-3a8c-a13a-91808deaf833 | -2.98032 | -53.28929 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d973096c-ee02-3386-b1a4-00ac449a1a7f | -3.94549 | -49.76081 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c5b248e-f7e1-3487-8333-898a7f3efeae | -2.29492 | -50.59098 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55814c24-8f9c-310e-91b2-d8dda14b33ab | -2.06429 | -46.53298 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983bd143-f3fd-3a74-8c56-7abc7c5c94f4 | -2.69373 | -46.12011 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89938f65-654f-3980-afbb-5a11ab85537e | -2.46256 | -46.56456 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c933367-5080-30cf-a1fc-f591f75dbd86 | -3.74904 | -50.05846 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3565a8a6-e970-3a42-901d-7791bf91a87f | -5.38947 | -46.36427 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab6fac4e-834c-3611-a6b1-ac08e2cafd2c | -2.96149 | -51.06184 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c58cb37-ad27-31c0-ad62-3efaabd87934 | -3.95367 | -49.92575 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7157c4b7-29b4-3629-a7b9-97e8c70d2ee0 | -4.78913 | -45.03059 | 2024-11-30 04:40:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 633c4909-c33d-335d-bdd7-0d548b8b04b4 | -3.79501 | -58.98049 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd498d17-5afb-3753-9a4d-15b0f0f12227 | -3.0494 | -48.96711 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1488368e-283a-327c-9559-7cb7e9f49050 | -5.42579 | -44.85425 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f3c5d3-58d0-389b-9e06-50566cabdfbf | -1.1999 | -53.8651 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a4fa594-c7a2-3e75-b3eb-8d8814f728d4 | -2.59485 | -46.57295 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f9ddd69-65c5-303c-9afa-fe712e3ef95e | -1.44491 | -55.12874 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5a672605-3dd1-345c-ade2-02dcd8b90bca | -2.14495 | -46.48645 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d665e52c-c419-3c34-8fa6-fd0e646e7b03 | -3.85932 | -52.35052 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b51d4557-e3ad-3d95-8404-f805ff99ed8e | -2.90256 | -54.17867 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19723556-e3d7-39ed-9cc6-0a32b9004087 | -3.42394 | -53.89182 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16965be9-01a1-3f14-a777-611406580af1 | -2.27324 | -46.42803 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e89149df-0213-34e3-a908-b4a61d87e8eb | -2.70376 | -48.67381 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb4b541a-e889-35e5-95a2-2884a9bae8cc | -0.98514 | -51.74883 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b1da99ee-e394-3a5e-887f-bcdd5aff21f0 | -3.2744 | -50.43733 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9750692d-dfd0-3379-8c30-8c6dc97e2a3d | -2.26545 | -50.35894 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
