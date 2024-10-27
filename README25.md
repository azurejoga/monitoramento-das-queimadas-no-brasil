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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa081ea7-5606-3327-8c14-8346addcef55 | -6.8722 | -45.8779 | 2024-10-27 02:45:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c08b82c8-ea4c-3c14-abaf-bf6c3fabb622 | -7.8531 | -45.4292 | 2024-10-27 02:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f3f2fd8c-74eb-396d-94e1-182ed8afdc5d | -7.8533 | -45.4066 | 2024-10-27 02:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 9d450a1e-1a21-30a1-b5a2-84a3a05649c8 | -7.8719 | -45.4274 | 2024-10-27 02:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c3e303fc-65e5-3112-b332-bbf0763fab18 | -7.8722 | -45.4047 | 2024-10-27 02:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 1acb145a-28d3-31ae-b9ca-7f3ee4e85a65 | -0.9815 | -53.7192 | 2024-10-27 02:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c755d192-f8dc-30ee-9a4d-c0717615b7cc | -0.9815 | -53.699 | 2024-10-27 02:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 181.4 |
| ad26cf33-4234-305b-a513-7da4242cc50c | -0.9815 | -53.6789 | 2024-10-27 02:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a38118a8-009c-3320-ba88-756ef9674f32 | -0.9998 | -53.719 | 2024-10-27 02:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 96d6cb80-d05f-3dcb-a5fd-62a48a58ab80 | -0.9998 | -53.6989 | 2024-10-27 02:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 4e206bbd-7844-330c-a0d9-8129c3c15f68 | -1.4407 | -53.4321 | 2024-10-27 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8576f3c4-1694-3a23-af07-28d8e0891bc0 | -1.6061 | -53.3289 | 2024-10-27 02:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3c6e775d-9c43-307a-87ea-4a37074d8802 | -2.4753 | -45.8561 | 2024-10-27 02:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 522f34e7-fa34-3f44-8b5f-cef1ff5b2310 | -2.4753 | -45.8338 | 2024-10-27 02:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4157c62d-4a99-35a6-a42a-a584f20561bb | -2.4786 | -50.2858 | 2024-10-27 02:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| e6a8382c-14ce-37ce-b659-66d2edb546d9 | -2.6482 | -49.2465 | 2024-10-27 02:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 4071fbc2-c347-3bd2-81e9-b93fd7b33ee3 | -2.6505 | -54.2971 | 2024-10-27 02:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a0dd406e-7449-3de4-80db-b22377e39fae | -2.8422 | -51.8148 | 2024-10-27 02:55:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a3f9bdf4-1bc5-3bad-80db-5241dde9e234 | -2.8514 | -49.262 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 25926be2-3119-3272-9f3f-63be13ce2fc5 | -2.8515 | -49.2408 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 353a3231-8dc6-3278-9d17-e45f76705492 | -2.8329 | -49.2626 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| c9aea1da-6284-3a14-9910-5a6ed9a29a1f | -2.833 | -49.2413 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| d232bdb7-33a6-315c-9276-aa704058312f | -2.7033 | -49.33 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 03e1aa9e-f4f8-3a68-af59-4cf98db56225 | -2.7034 | -49.3088 | 2024-10-27 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 25b00ad6-bc52-3f01-87c2-1eb8e02ca67b | -2.916 | -51.7716 | 2024-10-27 02:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ac92ddb3-e3f1-3b93-9fb1-65265f8f5b6f | -2.9161 | -51.751 | 2024-10-27 02:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b1a6fb0b-a23b-3c03-a1a4-bae71be032a5 | -2.9214 | -50.295 | 2024-10-27 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dbc5b8ad-d87d-3fb2-bc40-3f19fda18d20 | -2.9215 | -50.274 | 2024-10-27 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f8c1892d-7160-3b90-b919-14aa3c24797e | -2.9345 | -51.7711 | 2024-10-27 02:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b31e83da-2bdb-316e-8b2b-935e0286b7cd | -2.9345 | -51.7505 | 2024-10-27 02:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c1e41fb4-cd78-3fa7-a9aa-a899a527addd | -2.9399 | -50.2735 | 2024-10-27 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e97041da-cff3-34fd-81da-75e07a12dce5 | -2.9984 | -45.1207 | 2024-10-27 02:55:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 7fff6613-77fd-3c42-861e-31ae086e00e8 | -3.017 | -45.12 | 2024-10-27 02:55:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d87825a7-db4a-3656-9afa-ebe1bd843df6 | -3.1242 | -50.3519 | 2024-10-27 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c7dbd51e-47be-3117-b361-2c8a127c27d7 | -3.3256 | -50.7641 | 2024-10-27 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| c01e2e34-0a23-33f6-baf0-25971cfab04b | -3.344 | -50.7635 | 2024-10-27 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3f1abed8-5d8a-3336-aff5-2b6ea28a9a24 | -7.8533 | -45.4066 | 2024-10-27 02:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6d320770-71d0-3095-8598-94d1f9d1e715 | -7.8719 | -45.4274 | 2024-10-27 02:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 50f65c2a-4ae3-3d2f-a960-5b5533aa3832 | -7.8722 | -45.4047 | 2024-10-27 02:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| b61a255f-fcdb-32a1-8933-f599c720412a | -0.9815 | -53.699 | 2024-10-27 03:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 195.5 |
| bfd8eb35-727f-396b-8c12-9a9816988825 | -0.9815 | -53.6789 | 2024-10-27 03:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1b3cabc4-580f-3487-8967-d33ce2ecb808 | -0.9998 | -53.6989 | 2024-10-27 03:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 021237aa-819f-3b6b-93d7-88fbbc830f4d | -0.9815 | -53.7192 | 2024-10-27 03:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| baf60383-5ff8-38fa-b969-03c86dce833c | -1.4407 | -53.4321 | 2024-10-27 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cf7dbc13-80d7-37bb-b6f5-e514f2f1458e | -2.4753 | -45.8561 | 2024-10-27 03:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 3e3517fc-3da3-31c4-890a-ae1491d73e49 | -2.4753 | -45.8338 | 2024-10-27 03:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 247299a5-f1da-376f-a5b8-810ee36989dc | -2.6321 | -54.2975 | 2024-10-27 03:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 8ceacc4f-8d32-328b-9353-59cb60d4d46b | -2.6522 | -48.1324 | 2024-10-27 03:05:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 63d4eab4-e37e-3084-9594-771625311920 | -2.6505 | -54.2971 | 2024-10-27 03:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 0c78875f-b53f-3d15-ba11-6c5820a98d83 | -2.8514 | -49.262 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 964e7f57-06d3-39cd-8f73-40eb4c1afd07 | -2.8515 | -49.2408 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c0ba1937-b9ac-3ef3-b684-1c5baddf42db | -2.7033 | -49.33 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 31f6e79a-696f-360f-98dc-da1817a15747 | -2.7034 | -49.3088 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e8b10dab-f124-32f4-8d14-24f570d77cca | -2.8329 | -49.2626 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| e5f89b47-9f0a-3da4-b0f3-e183291dfaca | -2.8422 | -51.8148 | 2024-10-27 03:05:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| efead0a7-9e76-3ac2-b682-e95eeca96f90 | -2.833 | -49.2413 | 2024-10-27 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| b12c2f1a-bac6-3095-b88f-6a573a836d8c | -2.916 | -51.7716 | 2024-10-27 03:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| aa173ec6-8122-3598-894b-d5bfa08d8974 | -2.9161 | -51.751 | 2024-10-27 03:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1c51f53c-65d6-3b99-856d-4a05db9d29f3 | -2.9345 | -51.7711 | 2024-10-27 03:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 627caf15-d099-31e0-9313-35b47da5ee77 | -2.9215 | -50.274 | 2024-10-27 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 344be92a-120a-31a5-b4f5-12cd6e83d0ac | -2.9399 | -50.2735 | 2024-10-27 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b273d6e9-d1ac-3a6d-a08a-34a189f8af4f | -2.9984 | -45.1207 | 2024-10-27 03:05:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0b8e00c2-3964-30bc-b5bb-65e32d0cc35f | -2.9345 | -51.7505 | 2024-10-27 03:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8bd8d830-52d4-3e5a-ad8b-6c9309d7318b | -2.9214 | -50.295 | 2024-10-27 03:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 666b20a8-b519-3c5b-b8cd-9178010582f9 | -3.017 | -45.12 | 2024-10-27 03:05:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| a96a4de4-72e1-356a-85ad-5be2aa90b4e5 | -3.1242 | -50.3519 | 2024-10-27 03:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 26e7a282-3f86-3d49-b4c9-61e81a0b3074 | -3.344 | -50.7635 | 2024-10-27 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 819fb50e-2b12-3d72-9eec-3a943e72a830 | -7.8533 | -45.4066 | 2024-10-27 03:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b3185af8-46bb-34c3-960e-ee5e03c36a48 | -7.8722 | -45.4047 | 2024-10-27 03:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f3e66757-7ac6-3c4d-ad15-538829634abd | -0.9815 | -53.7192 | 2024-10-27 03:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f7b6aacf-8f11-3ff7-800a-6e461a241c2b | -0.9815 | -53.699 | 2024-10-27 03:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| d26b2308-bb42-3f26-a049-a5077d16c9f2 | -0.9815 | -53.6789 | 2024-10-27 03:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6e183281-105b-3d71-9678-5664ae8b4f6e | -0.9998 | -53.719 | 2024-10-27 03:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 00a07877-7084-3890-88ae-113a027a6126 | -0.9998 | -53.6989 | 2024-10-27 03:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5f2666d6-5cea-303e-871c-00dc6cccfbfd | -1.4407 | -53.4321 | 2024-10-27 03:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 10d0c575-479b-3402-a588-ab4b7c767ca0 | -2.4753 | -45.8561 | 2024-10-27 03:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 17dfa1e2-0a4c-3acc-9ba8-58904529ae94 | -2.4753 | -45.8338 | 2024-10-27 03:15:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a838ae8e-0c41-3c05-8aad-80e16138035f | -2.4786 | -50.2858 | 2024-10-27 03:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| fabc5818-bb22-3bd6-8048-b4ecbee63720 | -2.6321 | -54.2975 | 2024-10-27 03:15:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| ab921bae-f1e0-3b38-b842-d6be2056e6a5 | -2.7033 | -49.33 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cbddb561-5cfc-3893-aa8b-34bb3efd067c | -2.7034 | -49.3088 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d0e70b4b-9ad9-3361-9277-13ff8e4932b0 | -2.8145 | -49.2418 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 6b0585ef-b3f3-3d82-906d-63a0fdbeae07 | -2.8329 | -49.2626 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 8e1d996f-6705-3ea8-b62a-b2a3d7c818eb | -2.833 | -49.2413 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| e0f8e51b-0c29-371a-a5dd-46c2e3b694b5 | -2.8514 | -49.262 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8c9d7353-9d55-3f29-af0e-5e3704aade0d | -2.8515 | -49.2408 | 2024-10-27 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| abfc307a-eb53-3027-b4ad-df374fde5598 | -2.9161 | -51.751 | 2024-10-27 03:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 19468ba7-68c5-36b1-9ad3-304119e7eb95 | -2.9214 | -50.295 | 2024-10-27 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2211caed-48ad-33d3-8003-01147ebd2c83 | -2.9215 | -50.274 | 2024-10-27 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8a02f36a-4c9b-3231-842b-c1f9c14c2a6f | -2.9345 | -51.7505 | 2024-10-27 03:15:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c977e297-91fc-3b67-81a3-5e64f1035cbc | -2.9399 | -50.2735 | 2024-10-27 03:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7c19024c-e25c-334d-b52b-afe860dc1051 | -2.9669 | -53.0389 | 2024-10-27 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 348d0cc2-a495-377e-a2a0-d9f4f41eeb5e | -2.9984 | -45.1207 | 2024-10-27 03:15:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| bc215c33-4d59-3cad-9aa1-d5fd2438b9d5 | -3.017 | -45.12 | 2024-10-27 03:15:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 82891360-4c49-371b-818a-e3f2130eec11 | -3.1242 | -50.3519 | 2024-10-27 03:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 781c244c-e430-35dd-8456-cbdbdb41b8f8 | -3.344 | -50.7635 | 2024-10-27 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e5a6b02f-8dfb-38b5-969e-90b6e5ce4a5f | -7.8533 | -45.4066 | 2024-10-27 03:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 678f218e-9758-38a3-b1b1-f053740521bb | -7.8722 | -45.4047 | 2024-10-27 03:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| acb389f0-6947-3426-bcd4-8e569b77182a | -0.9815 | -53.7192 | 2024-10-27 03:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 45d65044-eb41-3366-86b5-408bd90f973d | -0.9815 | -53.699 | 2024-10-27 03:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |


[Clique aqui para ver as próximas entradas](README26.md)
