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
| 7ce08116-500f-3a63-a1a5-aec7caa85de8 | -2.21984 | -53.78927 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd618537-ea7d-32c6-bc7a-e8890e319bda | -0.24692 | -51.61917 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23c63c40-fd6d-370b-86db-522439d95415 | -2.46029 | -49.04251 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa6ffabe-9b7d-3390-ab56-898a9a1b1ca3 | -2.86187 | -51.277 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe80266-d3a0-3a3c-98cb-d622248ad729 | -2.32334 | -51.30715 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6e61a13-897b-39ea-91e5-9fd6a69860a7 | -2.78719 | -54.06519 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be623773-4de4-367e-b6e7-5ebcb1e1400d | -2.29131 | -49.1982 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33acc579-e922-384d-871c-7d751ecffaf5 | -2.09165 | -50.63072 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d7972a6-426a-3306-b857-2df0e36c6d18 | -2.20436 | -54.50431 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79c83e5a-9a94-3b9e-bd7e-556e5bfa8069 | -2.91722 | -54.28523 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b6d52e6-9441-37a4-bd2d-1c9660bf7aa7 | -2.06973 | -50.31622 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19116d71-ca7a-32f6-87f8-40900e3b8011 | -2.75299 | -48.67423 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d3534b14-5291-3906-a708-acfde662d987 | -0.9641 | -52.38771 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17723d4f-9cdb-3bae-abfe-c62c6d1562cd | -1.43103 | -53.37984 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbb9aa4a-8ddf-34da-a217-9d79943ac976 | -3.55333 | -51.53349 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec351376-e568-32ad-9d71-10adbd51bb35 | -2.82375 | -54.03313 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73e45945-23bd-3031-aebd-f92b383f0676 | -3.38898 | -50.31831 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08a7dc5f-68ac-3ec9-bc3c-ecc8a89bd02e | -2.19633 | -49.55049 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa30f5d8-20d7-32b6-b427-fefd464e0368 | -3.00002 | -52.50808 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0654716f-20d3-37e2-8f94-238624bf2662 | -3.29477 | -53.85334 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58e5d3c0-a27e-3f20-9671-1a1e028a7d94 | -3.29816 | -50.36449 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13d55ec3-13a8-345a-902a-e45cf21235da | -2.10152 | -46.26661 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 728caeb8-8c4b-3319-b388-567e39b4348d | -3.00359 | -51.5476 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaa48843-c12f-3bfc-8000-a063a7df4e58 | -2.43638 | -50.42389 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df5f0a7e-a3b5-336a-aeb6-55f4f5edbba7 | -3.21894 | -53.93118 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 320aba7b-901d-313b-adb5-296a6a1be4f1 | -1.23892 | -51.73998 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbd80c5a-1292-3b5c-8ddd-b4a9c8ebf7d3 | -2.07787 | -48.89332 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b69a5a8-eaa2-3700-9898-721113cd6117 | -1.17049 | -49.46447 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75e596dd-e922-3e87-94e4-c2d8d52fd59d | -2.78609 | -54.04976 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5d6dbb8-ed8b-3d78-834b-09819f0eb93b | -3.96747 | -46.72809 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 253c28c4-53ac-3f4a-a98a-18c757102c4b | -1.22507 | -53.68517 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5615745d-4edc-3df3-9817-fe4602bdb87a | -3.10048 | -53.99197 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d552000e-4e65-3d78-b996-3cc1b93bd69f | -2.29095 | -51.09975 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa62489a-81c9-3d8f-b28e-e6986f37546f | -1.27053 | -52.69212 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 979a005f-6002-3473-adbd-0851f1bde34f | -1.98644 | -48.7587 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f7ee46b-bf8a-3fe2-a9c8-ad52db68859b | -2.60071 | -46.2588 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a67f3be-953d-3a5a-8c2a-1103cdc92fb4 | -2.22114 | -46.38919 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 22ca7af7-c154-3c6c-9de5-b9aac27005be | -3.79075 | -52.41021 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95eaf12-5714-358f-be7b-62e3b9cb573a | -2.16281 | -50.12648 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aede08d-b5c4-381d-91c1-3d65556c3c46 | -0.93652 | -52.41195 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76982221-8890-3249-bdcb-e18e3aeee8af | -4.0379 | -51.01949 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0375606-9934-3ae3-a63c-ba7f8e9bc232 | -2.44927 | -49.09033 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40ac047d-bb04-34b0-944c-6715ae7d20a5 | -1.31863 | -49.39382 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 858f6bc4-3bb1-39cb-8bed-b036ff472e5b | -2.14918 | -50.71891 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3c8ddb2-1909-3905-8454-9bf5a51e8c0c | -3.51773 | -53.82065 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10cb7e44-b516-314b-b7f6-689251d02e7b | -0.44253 | -52.06875 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f36f6ef-600b-3521-99dd-42fc860c97b3 | -1.14313 | -51.69994 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fea4981-9674-31af-9e94-3fa53d85293b | -2.38947 | -53.71369 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abb26a97-785a-3a5e-af06-e5a3aaa86cc3 | -2.8454 | -54.16281 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 134b4f23-0612-3fe6-a9dc-1e8222c14e37 | -2.18027 | -53.79416 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73d0424f-4412-335d-a596-27207fc5fe29 | -1.10891 | -53.39694 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d561ac9-a78c-3917-bec0-ef2cc2409fae | -2.99777 | -53.7329 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e79116-ac4a-3854-9bc2-703f6cb9fd6d | -1.86918 | -48.16576 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94f81c0a-bd9d-3e25-956f-a7a972494185 | -2.21491 | -50.69284 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51bb2c77-2416-369d-94df-006c3f52ca75 | -2.39604 | -49.05742 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f844e8b8-672c-3fb2-ba35-93480995695d | -3.47632 | -50.43325 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 751b0804-bb2c-3a4c-841c-163d9d9ca95c | -3.26673 | -53.82621 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94d486c2-6c07-3863-a78b-78e8afdc2f1e | -1.05133 | -51.74192 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1edbb6d9-0a2e-3e81-badd-e0ef3b95b17a | -0.25057 | -51.57411 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3f4f845-7e76-3208-af00-79ffe5614d11 | -2.14679 | -50.49724 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7947df60-d3aa-3e17-80bb-f8b96ff3c68a | -1.62961 | -52.43853 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbab211e-13f6-3dbc-845d-4f14278d2934 | -2.25662 | -49.00099 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10eac08e-da90-3333-9b6d-d25b2210e94e | -2.5476 | -54.04827 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b1c908-6de7-38f6-b8a5-2cc622b56d37 | -1.25659 | -51.75674 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5214cf9-3bba-3203-9f92-b1d3465c4e0e | -3.77547 | -50.0393 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9c51fb-2be8-3781-beb4-2744f9175a42 | -3.20376 | -52.57562 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eeee4fe-0eab-381e-ae39-5bb8f59d88dc | -3.28352 | -53.83671 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d1c2a1-f953-33ac-baba-c91b3b641b12 | -3.10175 | -53.74137 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 654b6668-0562-3140-af55-c1d68b713056 | -3.22691 | -53.92485 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 362c4405-93ca-3c59-9227-caa6b6370ba7 | -2.37056 | -50.39148 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9221715-8811-35b2-a987-7ed2b94f9e77 | -3.82538 | -50.17425 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c634c80-a52c-34eb-a054-102026f1c4f4 | -1.28951 | -51.74074 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4f21953-f999-3307-92d6-97c17c2462a4 | -3.36807 | -53.32578 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ead3667-585a-35fb-97f2-18a22f02973a | -3.03998 | -54.0204 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 738ed640-0c62-3416-9a94-c49f4c19907e | -2.97705 | -52.91577 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf7e400d-a16f-38f1-9d04-975444f229c6 | -2.70927 | -48.66754 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c5df564-4738-3818-aeed-0e00cc524f78 | -2.59604 | -54.05157 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0612b8c2-cca7-3f07-9ae4-33d7b4f8c9b3 | -3.0693 | -49.20342 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 977848f5-a161-30ed-92c9-d87cfe4daf08 | -4.56673 | -48.53267 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37c52da1-ae52-3d14-a9f6-715668905f2b | -1.83583 | -46.64518 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44083356-414d-3a65-83ed-ff64ca31b6b9 | -0.21586 | -51.18976 | 2024-11-24 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be2249e4-02c7-372a-a821-cb3b629dcdee | -4.63605 | -48.84608 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 794c193f-311f-3bc2-846e-d583fd6d5e60 | -2.37002 | -50.41719 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3160c903-a5e4-31b0-9d6b-54f2fb2e6f9d | -1.61835 | -53.3092 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c1fce6c-1872-351f-bee4-488f38cf6a5c | -2.7865 | -51.71811 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa818efd-643b-31e7-aba4-dfb63d1221b3 | -3.19196 | -54.32697 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7010c20-a9be-39a2-81a3-11515f251909 | -0.26791 | -51.6195 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce1e81be-2d75-3829-99ca-f9b1111bfeb6 | -3.52679 | -53.80725 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 928f4c0e-bb87-32d1-99bb-5185e7bdb318 | -3.24921 | -54.22812 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 870d68e5-4bac-3fe8-a90e-132bc5eda64a | -2.91775 | -50.32621 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ed75a81-0ccc-3e1b-9a0e-258bcd2a4610 | -2.51632 | -54.11253 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2345abb0-41b6-3249-b647-32d29b7f5eb2 | -3.69703 | -42.30731 | 2024-11-24 04:53:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f84ba27-e698-366a-b91d-435373a8435a | -3.38861 | -50.7308 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2ba8f0-f4aa-3a3c-bbc6-b69efd4f4b5b | -2.72534 | -48.82894 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 908b6095-3926-35a6-ad9a-5783339003fa | -3.28406 | -52.97482 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29cf2f3a-dafd-340c-a093-af61e549b9e1 | -2.56187 | -54.33233 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d975b90-1dd1-35d6-a8c6-aa73c9eeba68 | -4.02506 | -49.92014 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d926bc1-20b6-351b-8f6e-e8f9314f5f47 | -1.76986 | -52.71686 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6064b56f-ffdf-38ed-89ff-57bdcdb6842a | -0.37323 | -51.55513 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6125531-9c34-39ae-a331-1fa81bf5e7de | -3.67427 | -54.5838 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README40.md)
