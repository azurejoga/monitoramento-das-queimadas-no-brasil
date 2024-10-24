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
| 4b6a7843-9585-3708-9c28-71686c38635f | -3.82597 | -51.35893 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11c6a17d-2085-3c9d-a8f2-7b087a043782 | -3.82221 | -51.38219 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec6a1353-1c65-3584-a3c4-06c519d2a0f6 | -3.74738 | -51.05376 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39a5c979-5e42-3e63-b2ad-4fe64fd69365 | -3.71387 | -51.14128 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 385d863c-2751-3d76-bbf0-5aa9ac2cd370 | -3.6831 | -51.08713 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc42250-fb1a-31fd-b4e5-e9732d9de139 | -3.67727 | -51.92904 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8db56e7d-a1c2-389b-958e-0bb0152117ac | -3.67652 | -51.93098 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87620300-a06a-3ae0-afb0-b4b2fa5c3204 | -4.66291 | -50.93958 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb9140cd-f3f4-32a0-b9c7-d6d6235fa712 | -4.64601 | -50.92789 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5a0adb8-9662-3259-bc02-aba279a3bd26 | -4.64445 | -50.91441 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d51b767f-5524-376a-8a19-e303163b08c8 | -4.64077 | -50.91393 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6013750d-fade-37eb-8910-c166f52dba89 | -4.613 | -50.92279 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 067dea4c-fefd-3933-892e-1407b5298296 | -4.61018 | -50.91859 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d819e1df-0364-306e-aede-2fed9ccb5ed5 | -4.61005 | -50.9179 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7220782-cb21-309d-8ae8-1bcbdc11c137 | -4.60949 | -50.92292 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87a09356-64d4-349e-b187-1701151bfc52 | -4.60933 | -50.92223 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3504865-b880-3ec2-b615-ebdd2b71bd06 | -4.57025 | -50.95655 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d4a0002-938c-3030-9e42-374870211115 | -4.10408 | -51.03198 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfb02c73-31c2-3304-9aac-726bf86269d7 | 2.8029 | -50.93871 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f2aa3c2-80d1-3bad-8037-1b634e38dd53 | 2.80236 | -50.93512 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af9a0699-2a94-381c-a971-a1b86684a8c0 | 2.50005 | -51.00321 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 068024f9-16b1-3d02-8996-c838a6e80f3f | 1.00968 | -52.21975 | 2024-10-24 04:32:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e199ad9-dce3-3f75-a67d-2129d3daae73 | 1.00904 | -52.21568 | 2024-10-24 04:32:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11cb6000-1e56-3ece-a5ab-80de9e4989c2 | 0.50285 | -51.67693 | 2024-10-24 04:32:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f487d0a-07a4-36ec-80f9-2ac62581bb8f | -0.53523 | -51.87481 | 2024-10-24 04:32:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a566b4ef-289c-3f69-bdef-2461ec4611c4 | -1.60234 | -53.31199 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 156403e7-857b-39ab-93f4-41dd5cf98c22 | -1.59859 | -53.30675 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2f427bf3-4376-390b-b170-2a5a3924c9f8 | -1.59789 | -53.31123 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a8c336f-e0d4-32e3-86ac-a23f32eaa643 | -1.59413 | -53.30605 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2b0ade71-6c2a-3d2d-82fe-3f719f4e07c9 | -1.59342 | -53.31051 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 210cffe6-010b-3531-9881-4bd0b878f375 | -1.59271 | -53.31499 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 86624bf3-1fa0-3210-ac7a-fce23b0646c7 | -1.58966 | -53.30532 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3555d6f3-bf30-30e2-b8c0-4ab5a53e014b | -1.58896 | -53.3098 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 112890a7-43df-37ce-99be-bd12bb4f8660 | -1.58824 | -53.3143 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e706dc3-081d-3947-bed7-17501e82f2c7 | -1.58753 | -53.31878 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56a1ced8-45c2-3cd0-9c66-24c33c8a0327 | -1.5852 | -53.30462 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bb503a0-7f84-3717-a792-cce8a4892565 | -1.58449 | -53.3091 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64dc2278-2187-374c-8db1-eb1d99f9cdc3 | -1.58378 | -53.31359 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2029ea5-b519-369a-8ef9-b4f36243a957 | -1.57931 | -53.3129 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0942acbf-8ddc-33b9-b899-788fe3246df1 | -1.57859 | -53.31739 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed55de99-e6a2-3d28-8a87-fa091a2ca8f0 | -1.57413 | -53.31665 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedd1778-199b-31b3-97b9-0cb803649fc8 | -2.05352 | -52.0351 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 756a01f9-104c-32fe-bc63-eb2ccd03e35f | -1.9808 | -52.02007 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 032829ea-436b-323b-b866-5fe69908655f | -1.87381 | -52.30186 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1692572-d9ba-3bf7-ba15-c7beab1533d4 | -1.76755 | -52.23442 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afdc864d-bd0d-3014-8e53-81728a45e41c | -1.66156 | -52.21827 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65ab387-68b3-3483-bd37-d46fa72b37e9 | -1.52229 | -51.93687 | 2024-10-24 04:32:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee68fb3-2332-3e4f-b325-7a47cd6c7da8 | -1.52171 | -51.94048 | 2024-10-24 04:32:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8a3fd2d-280b-3cd4-a7f3-114613161954 | -1.47443 | -52.95265 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d44138-221c-3bb6-8da6-f4584a2d5399 | -1.41961 | -52.95407 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b488d24-89fd-3a2c-b533-6fed755569a5 | -1.05352 | -53.01405 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acc689c5-db8b-3189-8e6e-5d5bba1e03a6 | -0.88507 | -52.00602 | 2024-10-24 04:32:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb0c3a2-de0b-384d-9bb2-e119c560922d | -2.99868 | -53.43911 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0714c49e-4c21-38ac-8616-f8d19962b879 | -2.99851 | -53.44069 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 330c9e90-0cb7-3113-aeb9-3d87d818bc01 | -2.99794 | -53.44355 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c31b3b5-a7ac-3896-a427-d71ecb41e6fe | -2.84595 | -53.32433 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d454d817-4cb9-342a-b05d-39d674b46f24 | -2.78121 | -52.10357 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a48bae6-987e-35b9-a41f-e66848365905 | -2.77772 | -52.0994 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bc54f74-035c-3710-808f-cdd70826557a | -2.77716 | -52.10295 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4133f6c8-5471-3300-acb1-e479d5d1dc79 | -2.7766 | -52.10651 | 2024-10-24 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 92f8c41d-6b51-39c3-b270-118b739c40c5 | -3.22309 | -53.36848 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f512c8-b36b-38ca-be12-6cb0fb3f7a47 | -3.2228 | -53.36432 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f15459-becb-3bba-a3cc-78207fd007d2 | -3.22212 | -53.36855 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde4b660-2ae6-343e-ba6b-eaa22e81c5f3 | -3.21844 | -53.36354 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d81d32a4-3f74-35f0-a27d-b696e4d3f56c | -3.21776 | -53.36776 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 164f4221-2383-36da-ba58-df7f73f85e43 | -3.2122 | -52.46192 | 2024-10-24 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2781d262-6f5a-3e98-bd23-40112d968ec0 | -3.11157 | -53.13407 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 89af5004-6195-36ed-b17a-314de490a589 | -3.1079 | -53.12947 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07f059c1-6762-3c44-87aa-d47bb9cf15b8 | -3.10725 | -53.13343 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 00492bc8-b1c6-3cdd-9a80-9dbce8049f5c | -3.07671 | -53.23893 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a9a5ed02-44d9-3b4c-9352-1a6d50045b8b | -3.07604 | -53.24302 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| be35a4d3-5c87-38ca-99a2-13d46ee79bee | -3.07537 | -53.24712 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ede4fb8-ef88-3e89-87ff-75a0d0f24e96 | -3.07469 | -53.25122 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee23ec50-91d1-385d-a468-f02710b3d642 | -3.07235 | -53.23833 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7a2fd7c4-28e7-3f24-8014-c1a4b05112d3 | -3.07101 | -53.24649 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5fd4246-a2ef-3891-88ed-138597219eb4 | -3.07034 | -53.25058 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 518bc5a0-039c-3c13-a4f6-03c9d0d3e5d8 | -3.068 | -53.23771 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c1422ae-89eb-35ee-bf3f-7c7a5237130d | -3.06298 | -53.24112 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a7f6d8d-18aa-303c-a762-d41247338015 | -3.63337 | -52.28933 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1605b35-0d65-3a48-817b-b31103487a0e | -3.63279 | -52.29286 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a3e108-7cb2-3897-a82c-08d4a7767778 | -3.6322 | -52.29641 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 725f6b7f-39e0-3d20-9c4a-0bc1c77d43b6 | -3.50999 | -52.89806 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3daa9da9-fda5-30c5-af9f-4f764d7b6453 | -3.47413 | -52.80047 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec81e2f6-cb3f-38fb-b6e2-c66af49cefe5 | -3.41025 | -52.87074 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05df411-d9f4-3b63-b315-88810f3e0256 | -3.39444 | -52.88852 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d4b0d8-bd3c-3e89-a9af-9b36fa288adc | -3.70898 | -53.71108 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f8fd8b8-b3db-3265-b5b7-14f8d41a661d | -3.59044 | -53.4947 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a1fbb39-7cc8-3a1b-8b9c-645cc6c4e053 | -3.56215 | -53.75064 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 924152e2-6961-3413-bd5c-208ab0a5f274 | -3.56143 | -53.75505 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc3c1163-b737-37a2-b78f-ef1074658de6 | -4.01578 | -53.73879 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9984d47-92b0-366b-991b-f43231b45914 | -4.01507 | -53.74314 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d3bb5a8-84d0-33b6-8b2a-81fac26bd59e | -3.92869 | -53.66421 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a65336b-ad36-311d-ba6e-fe07dec22aef | -3.928 | -53.66848 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d519de47-729b-34b1-9823-4e629dda7a3b | -3.92358 | -53.66781 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6840fa4-f1ba-3b7f-8d7a-d8a7c6c72810 | -3.91266 | -52.39213 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae1bf85a-eafb-3836-b4e8-b46c0f9c5c24 | -3.91209 | -52.39564 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 742fe2c9-4d26-3cba-b650-132ae455282a | -3.9086 | -52.39157 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7b8d1f6-1f5a-3cb7-bd9e-e7d8c96de7ae | -3.8825 | -52.34796 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb6ae947-d145-32dd-9ec6-2e1fe973656a | -3.81411 | -52.68839 | 2024-10-24 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b413041-6e2a-3ae5-a80e-b0b465252e95 | -3.81351 | -52.69206 | 2024-10-24 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README37.md)
