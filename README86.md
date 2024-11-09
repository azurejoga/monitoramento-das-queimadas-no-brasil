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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6bab257-85e3-30e5-8f37-6e447c9f5105 | -2.94814 | -46.75553 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aebe65a-dec0-3769-8bfa-ec62e736baaa | -5.35645 | -44.14194 | 2024-11-09 04:55:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9012b7-62ad-3cf4-b2d3-522b79892807 | -1.51283 | -52.16999 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30c3d35b-be1e-3806-ac19-a006f040d083 | -2.71952 | -51.70883 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55894b57-b120-3318-95e7-2f86cca9c1f8 | -3.85864 | -54.08107 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd5d69bd-fdc4-3214-9a98-ea4bf316ae13 | -3.97629 | -48.17757 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f2db5a9-9f16-31fe-8185-033bba792d10 | -2.84399 | -49.44138 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ebfae7c-d7eb-37a6-a5e3-9c7af907070c | -2.66455 | -49.87343 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32418274-97b8-3130-8f2c-374d8a0f1c6a | -1.55698 | -52.28032 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02e8e7b6-d52b-36bd-b223-f099a925d5aa | -2.24135 | -48.38062 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f2b0db0-6ad9-3bce-99f5-ad5e677d4571 | -1.14714 | -53.71715 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1d96e1c-81c4-3b4a-9b78-f250a22402f1 | -0.22116 | -51.64717 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80e40edd-c407-338e-ae8a-6312b7826a44 | -4.09539 | -48.51379 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b70e3310-237a-3a36-bdb1-16093e433fa3 | -3.54527 | -43.5642 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 960b4b9d-9ca5-3582-a081-5db592e06ce4 | -3.19179 | -48.65861 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76c2fe0a-2dfc-32a9-8b4f-c21a428067f0 | -2.72573 | -51.71349 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54908e28-e85d-333f-bc21-56a9f80197be | -1.9895 | -52.29731 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db56c56f-2762-3d57-a720-61582b61c4f0 | -2.94454 | -54.12358 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26f9c62a-58bd-33ae-8f02-0c19f9d1c9d1 | -3.09112 | -53.32384 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6104e290-409b-3c06-8e89-6ebcbc111d62 | -3.58315 | -51.20019 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a2981103-10c1-3359-81ce-223b17c69e00 | -2.87497 | -51.87656 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d928d767-ca42-3c46-97be-ae15ab458444 | -2.97542 | -56.88653 | 2024-11-09 04:55:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c307c1f-559a-31e8-a5af-3c8409b0cce6 | -1.50498 | -51.52754 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f968f972-d117-3db7-845f-564fc6b90165 | -3.2198 | -50.37802 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb0ec0bd-75d7-3881-949f-6fb63c0bcc17 | -5.1964 | -44.92181 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c961e5eb-ed73-35d7-8c7b-2852d0012d2a | -5.26989 | -44.76955 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15f25c47-6acb-359d-b008-ac87e712ab38 | -3.1782 | -50.59931 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 945ce685-fa36-3266-b745-b2e624a224d7 | -2.5984 | -48.1927 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48ad3785-0b19-343b-81f5-96953294bf9f | -2.63188 | -51.7138 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc1706b9-ac59-34db-b9d8-c5dba0283940 | -3.27299 | -51.06031 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a877811-b542-3d01-acfe-d501e83c591d | -2.80505 | -52.94667 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a83f0c-415d-3e90-a127-d90d358d351d | -1.52703 | -51.11679 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc984d1b-f200-3ba3-b260-66033bc08b8d | -3.07816 | -51.3571 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a20fa112-002e-3885-8630-3fdf6d799852 | -4.08303 | -49.28811 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d491128f-d0d2-3867-8a28-8f42958d1fba | -1.12025 | -54.21457 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85dbd6ec-222a-3e66-a1e8-8c19d9987aab | -3.96443 | -48.17196 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b70aca7c-15c1-3bc1-aa81-f5123bb3d2ae | -3.15956 | -54.48109 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7699c3bf-aafc-3d36-99f5-2c482b249413 | -3.04403 | -48.04499 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b82b2c7b-2d46-3ab0-9428-94d3ca44e209 | -2.42728 | -46.30311 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d05d9a84-ccd0-30c1-a6f0-8cc84874486f | -3.03223 | -48.03944 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b20a05bc-c423-3007-a59a-a7d72e5df442 | -3.47808 | -50.80511 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcec1368-252e-32fa-816f-74ddf9a12cfd | -2.45413 | -46.31216 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce634ab1-0b0b-3af4-9666-8b74824e7f60 | -1.94997 | -54.40165 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b028c782-056d-333c-af66-9255008fc57f | -3.59568 | -47.34207 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| f5f1749f-2d60-31ce-9fe0-1ef41bfe481c | -3.56946 | -47.36803 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e68cc44-25cd-33bd-b6a5-c1a0bf768c84 | -1.5668 | -51.28847 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8860407-ef6d-3d2c-baa1-b92953c08a9e | -3.8686 | -51.97225 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04def4c8-468b-3321-95d4-e6a8db4c859d | -4.2009 | -48.5583 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d5eed9-4570-3f3b-a992-b6236e0feccf | -2.12705 | -50.82568 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 226e46bc-b2b8-3bec-9622-e62e4131a8b0 | -2.0786 | -54.69446 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 797984ee-06da-3a2b-85fd-5bb74da312c3 | -3.78198 | -50.14029 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 553bf5d9-73e3-3c29-8191-1834088a90b5 | -4.08935 | -48.8559 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c3c4fe7-334a-3e9c-80df-feac2ab8e788 | -2.94195 | -49.50488 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4877cc94-cfa9-3ed0-9cfa-002aa1be636d | -1.85812 | -47.82718 | 2024-11-09 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc666f3f-52b9-3a2f-baaa-2a5f0b82a8b3 | -2.31038 | -50.66321 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf132f5-701e-32aa-8499-315bdd670f21 | -3.72186 | -53.40126 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8c07c87-076c-33ff-84f5-f3351076609e | -1.65995 | -55.08609 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 477e9591-7cce-38c7-8a7e-cae16ac5bae5 | -1.44144 | -54.48425 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2618c2b-59fa-360e-91f9-4a8c0242cb27 | -1.51951 | -52.17103 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5c556df-b972-32ae-8268-17e504c29696 | -3.02624 | -54.20409 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3fe88535-a816-394f-a883-a7f8df59e821 | -4.22889 | -50.43117 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aeb48521-e4b8-302b-9da0-b54eafb1ab84 | 0.84761 | -50.16962 | 2024-11-09 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3632bf12-67b8-3056-b123-aaabf4e5244a | -2.4692 | -48.44746 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5144684-38ff-390c-a312-f3d9d3cdad10 | -3.24792 | -53.40115 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71713b68-faa1-33af-b2af-8a79999dd9a0 | -2.27926 | -50.67834 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27045368-c7b7-3204-8a55-ba6438a84399 | -2.8836 | -53.97421 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 991aa88a-04a6-39af-8fac-142a6a6ef2e1 | -3.64847 | -50.13456 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee931d22-1033-30f4-9c1a-27395a0acf1f | -2.61563 | -51.29929 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97bff060-d088-3b62-ab1b-69fd83ca855b | -2.32656 | -50.51304 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be099990-0720-3a28-89d3-999c34503c77 | -1.52509 | -52.17904 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5d1099-a9d5-3b10-8b65-cf7e86e3f7cb | -3.01404 | -53.42482 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56097b2f-16a7-33dd-8668-4114e99b0119 | -3.27235 | -52.72849 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 754ac164-e13b-316f-8812-eeb5521ece4a | -2.18556 | -53.63787 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed624181-f409-3d61-b20c-504fb65b626c | -3.01003 | -53.23644 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9583704-99f3-3c39-972c-f2e97c7357e1 | -0.21947 | -51.6361 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3f043b-e041-30d1-b6ab-1412c747bb13 | -3.8214 | -49.85782 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 87d98abd-9f47-3252-94ea-ca3e4228f0f0 | 0.79368 | -52.01054 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bfef316-e1f2-376f-9016-5341e0fb3cb8 | -2.25249 | -53.72631 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3a248f2-6c35-3d02-8e2d-06b62752c5e0 | -2.17582 | -48.32858 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37acddda-fea0-32ff-838f-47f16edad726 | -2.77049 | -54.04954 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff0aa2e0-7c42-3a79-afd7-5f1c0b4454e4 | -2.73231 | -51.73993 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a854e15c-0a21-31a8-a85e-065a760f6615 | -2.65398 | -48.63243 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c324b085-0376-3249-b6b7-38b89a03a460 | -3.03264 | -50.3096 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 01deecaf-d87d-3e9d-8589-706284686dc4 | -0.3595 | -51.41457 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58c09ff7-cc9b-3baf-b8fc-3588ef9fa40f | -1.51908 | -51.52604 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf85c89a-5906-3df4-8776-4564e7bc10c6 | -3.07915 | -52.42656 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53015421-fdde-3c4a-8898-214340c99233 | -4.73734 | -43.24804 | 2024-11-09 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7afe5dc8-051b-3c92-a76b-ddce9314e08f | -2.43159 | -54.00712 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 438692a2-eff9-3215-a2ce-ae493f996b9d | -5.13973 | -60.36314 | 2024-11-09 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41043b01-4612-390d-9c9f-62798ed935fa | -1.34098 | -51.41386 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9883a663-a02f-3b4c-b186-da4b0d794508 | -2.41303 | -48.84334 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10ccc504-bc96-3138-95f0-2f932bcf724f | -2.63721 | -46.77013 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec1524b2-750c-366e-89b4-cf668f913e7b | -4.61157 | -49.57616 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcc61f06-6c16-39e3-9aac-b99d58c421b7 | -5.55475 | -45.83109 | 2024-11-09 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497c3f4f-660f-30b0-8b39-f3546b0e7040 | -3.9727 | -48.17331 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0613f91c-b6de-37cc-a486-29944fd22b84 | -6.1278 | -43.41809 | 2024-11-09 04:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 250501ee-32c9-36d4-afbf-8f9a22b399e1 | -3.67141 | -54.23352 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7252f6d4-82ce-3041-a018-d4f5bba32da7 | -6.1795 | -45.44122 | 2024-11-09 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4148d644-de13-3052-8231-9de5d63bc488 | -3.01735 | -53.42533 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72250760-6b8f-3ef7-9597-9f36c8a1d7af | -1.14038 | -53.65185 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README87.md)
