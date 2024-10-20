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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc3274e3-edf2-336a-99f9-c468665cf5df | -2.7958 | -49.3062 | 2024-10-20 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 50883f78-b90f-369d-9238-b5b351a6bc1e | -2.7959 | -49.2849 | 2024-10-20 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f818957e-ac60-3c0a-b04d-f206c2ad2bf3 | -2.7981 | -48.6873 | 2024-10-20 01:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4fb4acec-296e-3c23-8ad8-1ee968c95fb2 | -3.0293 | -51.0231 | 2024-10-20 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1fb6b64c-f92f-35c5-a62d-2a42d03a1bc3 | -3.0478 | -51.0226 | 2024-10-20 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3c79acc1-5d4c-384d-a18d-5201aae5e960 | -3.1462 | -54.3658 | 2024-10-20 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| de420d3c-5d6e-3c1b-a51e-eb3d12279753 | -3.3813 | -50.6788 | 2024-10-20 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5a39839f-0fdf-3df9-b87c-e3fef7eeb779 | -3.3814 | -50.6579 | 2024-10-20 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ce0ebfb2-3c42-3a00-acb9-be40f6b7d15b | -3.586 | -54.6941 | 2024-10-20 01:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5068e020-1fc6-323d-b3c5-d9f0d7ff1540 | -3.5861 | -54.6741 | 2024-10-20 01:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f8aefb7b-2b65-3e20-99d2-0a7bd8f8798a | -3.9062 | -45.7565 | 2024-10-20 01:55:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| dc6f2d67-9d56-3dc2-b7aa-f8629c028dd1 | -3.9248 | -45.7557 | 2024-10-20 01:55:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 26066aa9-cd49-3598-ad55-d10e04b98fee | -5.6977 | -68.679001 | 2024-10-20 01:55:33 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56f56e46-ecd5-3135-bdb4-b6b8ebf879e9 | -5.6996 | -68.6875 | 2024-10-20 01:55:33 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e28f514-52e1-3b78-a6f9-9174efc3f790 | -5.6898 | -68.689598 | 2024-10-20 01:55:33 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f350053-950c-32c5-8b66-8a9278cfab5b | -5.721 | -68.6862 | 2024-10-20 01:55:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 64621883-5110-3a7b-9929-b742dd7ae9da | -3.4773 | -62.751499 | 2024-10-20 01:55:47 | METOP-C | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0bb4327-c76c-3543-a416-824656427b8a | -3.0398 | -61.672901 | 2024-10-20 01:55:50 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cec32fa-7e93-35da-b2cd-52048c131864 | -3.03 | -61.675098 | 2024-10-20 01:55:50 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5f379df-afd9-3169-b684-fbf83d57227c | -3.0322 | -61.684399 | 2024-10-20 01:55:50 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c937142-8ab9-3d32-8cb9-0fa2cd73a5fa | -3.6766 | -64.455498 | 2024-10-20 01:55:50 | METOP-C | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1eadc335-b9f7-32b0-bc04-9cbf87b78b22 | -7.7679 | -73.079 | 2024-10-20 01:55:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b4c9838e-c350-39be-8c5e-010590e5304f | -8.5587 | -44.7414 | 2024-10-20 01:55:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e7d8c737-d238-3973-a75c-9b2856186c7d | -13.0082 | -55.9699 | 2024-10-20 01:56:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7448012c-aea0-3c6e-a994-1de6f1b77506 | -17.4136 | -40.2217 | 2024-10-20 01:56:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 9a71750f-cdb7-3da6-a4a2-3d936d44e686 | -13.0104 | -55.99018 | 2024-10-20 02:00:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b8b2959a-d61a-3e6d-bc1f-70a8444a3744 | -13.00611 | -55.96567 | 2024-10-20 02:00:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| cc543e22-58d0-3d73-8b54-0c42c5e86d1f | -13.00168 | -55.97205 | 2024-10-20 02:00:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c67fcb89-15c2-3815-ab20-f01f8df9cdae | -7.76662 | -73.07449 | 2024-10-20 02:02:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f7ddaf22-b5cc-3368-b32d-950d25e8dcb7 | -7.70389 | -73.05923 | 2024-10-20 02:02:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1f46218b-1f21-3aaf-a275-21c9f19ed364 | -7.70358 | -73.05408 | 2024-10-20 02:02:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 20c1bc6c-5689-357f-a899-1ae4f6500696 | -7.58178 | -73.05275 | 2024-10-20 02:02:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 28.7 |
| b7585c39-8aad-32bb-b50a-a2c3de077443 | -7.58148 | -73.04626 | 2024-10-20 02:02:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 313f48f4-d1ce-3f39-bcb2-040e7731a3f8 | -6.48626 | -60.02577 | 2024-10-20 02:02:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a4eebd25-29e7-3109-8b26-e59035e24e36 | -12.75091 | -62.70093 | 2024-10-20 02:02:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff6b7330-0ad1-3586-9c1f-e7a322091c29 | -12.71837 | -62.85671 | 2024-10-20 02:02:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa27b80d-6d82-3f1b-a904-893db8a9b13a | -12.27702 | -61.53445 | 2024-10-20 02:02:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0539305f-711b-3742-b37c-7130c837ac76 | -11.88286 | -56.22364 | 2024-10-20 02:02:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 8663e674-27f8-34e3-bc03-3ba1ca8b807a | -5.71933 | -68.69228 | 2024-10-20 02:04:00 | TERRA_M-M | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 63a0e003-685a-3d85-acdb-4ed0a9bbe196 | -5.71773 | -68.68037 | 2024-10-20 02:04:00 | TERRA_M-M | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 11ed57e4-f14c-3bc5-83be-4f89acf68d41 | -3.69816 | -64.45375 | 2024-10-20 02:04:00 | TERRA_M-M | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ee432d7f-6700-3fc6-9d2c-d9b95506f6fc | -3.04899 | -61.67111 | 2024-10-20 02:04:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 904ffb84-e2b3-3530-b4ca-f79d30a21673 | -1.165 | -53.6571 | 2024-10-20 02:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 1cc39651-cd40-3e7b-aaa6-7885398f9e8b | -1.1834 | -53.6569 | 2024-10-20 02:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 27ee627a-763b-3487-98b2-cf4c1cce7aef | -2.2993 | -48.5936 | 2024-10-20 02:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a127151f-3b4a-38d6-8d2d-a103671e4849 | -2.2994 | -48.5722 | 2024-10-20 02:05:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ab5e2772-817c-3ae0-b0f5-d05f4868d7fd | -2.7773 | -49.3067 | 2024-10-20 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7d07a6c9-f320-3af5-a63d-ab67ea067e13 | -2.7981 | -48.6873 | 2024-10-20 02:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 548a3ac4-d25b-3838-b510-a8301934c3b4 | -3.0478 | -51.0226 | 2024-10-20 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| fb783ba2-6787-37f1-b991-a82208528b17 | -3.1462 | -54.3658 | 2024-10-20 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 182fb39b-b6ac-34b3-b625-0fc02c60d4eb | -3.3814 | -50.6579 | 2024-10-20 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 18b4f2c4-7ba8-39b6-b65e-309c033995a9 | -3.3997 | -50.6782 | 2024-10-20 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 12270953-e2e5-3e62-b7ff-de676997b587 | -3.3998 | -50.6573 | 2024-10-20 02:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7381f05c-780b-3467-9f06-e167d4273cb7 | -3.5861 | -54.6741 | 2024-10-20 02:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d79c4e8f-5b27-3c30-b0a7-dc2da7a45768 | -3.9062 | -45.7565 | 2024-10-20 02:05:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e46d7252-c337-3ff1-8ac5-bd0dec2a9c49 | -3.9018 | -49.9884 | 2024-10-20 02:05:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d0f3c84b-cd9c-37a4-9598-0193ef5cda2d | -4.1985 | -46.6318 | 2024-10-20 02:05:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b5f6f8a5-15c3-3bc4-be03-41bef8f4f588 | -4.911 | -45.8374 | 2024-10-20 02:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9a2701ee-02a7-3868-a3ba-60b575ff29c1 | -5.721 | -68.6862 | 2024-10-20 02:05:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 17c00c82-2bd6-3e4f-9762-609aa5e8ab47 | -8.5587 | -44.7414 | 2024-10-20 02:05:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0623a601-10fa-3a0b-aeb7-bd471cc313b4 | -13.0082 | -55.9699 | 2024-10-20 02:06:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 98e77d31-4102-32b3-9591-8afca0ee56e4 | -1.165 | -53.6571 | 2024-10-20 02:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| ea8f95a7-e8b5-3c79-89b9-677b0df1e8c6 | -2.2993 | -48.5936 | 2024-10-20 02:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 9c59ba40-b919-3629-b481-a5bcb15b064b | -2.2994 | -48.5722 | 2024-10-20 02:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 885cd063-62d6-3121-9e22-fd682c2fb406 | -2.7981 | -48.6873 | 2024-10-20 02:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dc040759-26d8-32d4-8523-6b80139f4729 | -3.0478 | -51.0226 | 2024-10-20 02:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 78695edf-c92c-3a62-bd86-2a1f78b6d7ca | -3.1462 | -54.3658 | 2024-10-20 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5dc2956b-9bab-383b-aec8-ad85f191e3bd | -3.3813 | -50.6788 | 2024-10-20 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c1878489-0be1-3bb9-b974-af8b3cad90e8 | -3.3814 | -50.6579 | 2024-10-20 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ed3c980f-8ba2-378a-ac55-572e5bff5c8f | -3.3998 | -50.6573 | 2024-10-20 02:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 493c29ef-1454-335e-849b-365a134a43cd | -3.5861 | -54.6741 | 2024-10-20 02:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 285010ff-60cd-3b61-b8a0-c629cae520a1 | -3.9248 | -45.7557 | 2024-10-20 02:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8c8193f1-8182-3acc-b6f4-fb8a32fad264 | -4.2478 | -51.0018 | 2024-10-20 02:15:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c47e15d0-558c-39da-af0e-7cdaaa2c729f | -4.1985 | -46.6318 | 2024-10-20 02:15:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 30c9e2e0-cb37-3b0d-bd98-27e8f5f31407 | -5.721 | -68.6862 | 2024-10-20 02:15:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ae26cf1c-6138-3339-b639-be069dd3276a | -6.4852 | -60.0279 | 2024-10-20 02:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 136249e8-f3f5-3c83-ab21-ea82018b4b09 | -7.6815 | -47.3213 | 2024-10-20 02:15:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 49814f39-cee8-39c6-8a09-527e02c883a2 | -7.7679 | -73.079 | 2024-10-20 02:15:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9d0a0ee2-1792-3351-8b58-cddcd83ba664 | -8.5398 | -44.7435 | 2024-10-20 02:15:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 7626fbee-267f-3f53-ba9b-56560d2b5dfd | -8.5587 | -44.7414 | 2024-10-20 02:15:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9bf5d2df-71d9-3d5a-8745-85f52070a6f9 | -8.559 | -44.7184 | 2024-10-20 02:15:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d85083ff-8a13-3b5d-a7a2-577535d00709 | -13.0082 | -55.9699 | 2024-10-20 02:16:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8abf393b-2257-3994-ba31-de3aee06d4c5 | -1.165 | -53.6571 | 2024-10-20 02:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 48e801f0-6edd-36ec-98c0-b89c3ec7bea4 | -2.2993 | -48.5936 | 2024-10-20 02:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 201d1ae5-4ba1-3745-b0fe-6e03aaf3be4a | -2.2994 | -48.5722 | 2024-10-20 02:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 089c0046-5c33-3a4b-99d0-460762c85f7f | -2.7981 | -48.6873 | 2024-10-20 02:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e904bd85-99ee-336e-893d-16823144a84c | -3.0478 | -51.0226 | 2024-10-20 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 701cfea6-96b4-3090-9721-8da81933227d | -3.1462 | -54.3658 | 2024-10-20 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 46ef9d3d-aeea-3bb4-bb14-cbd48e307861 | -3.3813 | -50.6788 | 2024-10-20 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| cf999998-a4dd-392d-9195-cb224d3131e1 | -3.3814 | -50.6579 | 2024-10-20 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8fc980d1-0897-3efa-b7fe-dd1c3802d861 | -3.3997 | -50.6782 | 2024-10-20 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d13853aa-3f8f-3c9e-ae3e-4a87325ea3a6 | -3.3998 | -50.6573 | 2024-10-20 02:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a904f1c3-d1da-3769-801e-140e000d5748 | -3.5861 | -54.6741 | 2024-10-20 02:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e1775666-9691-3c0e-b2c1-978dbbe0b11f | -3.9248 | -45.7557 | 2024-10-20 02:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d3040602-1fcd-328d-a1b7-ec26977c01ce | -4.1985 | -46.6318 | 2024-10-20 02:25:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a42cab69-93bd-3d4a-9b07-a4b3faa03f42 | -4.2478 | -51.0018 | 2024-10-20 02:25:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| c29ee880-6ed6-3ffa-bf26-8a712f50a6cd | -5.721 | -68.6862 | 2024-10-20 02:25:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 31644ae6-9108-382f-974c-e7fef8cf8e01 | -6.4852 | -60.0279 | 2024-10-20 02:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2b6df4cb-9dde-376e-984e-3a2624396008 | -7.3638 | -72.8628 | 2024-10-20 02:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 914d8b12-df49-3d7c-8fab-b4fde11237f3 | -7.6815 | -47.3213 | 2024-10-20 02:25:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |


[Clique aqui para ver as próximas entradas](README14.md)
