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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fb7641c-e556-3452-9d29-1d4fd8a63744 | -2.6718 | -48.28803 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c6058f5-78f8-3bba-a42b-b359319e37f4 | -1.78304 | -53.61209 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9330655-d434-3cc8-8f6c-1c9242312163 | -1.25284 | -51.76142 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e616bdac-aac2-30e6-af35-5497ec717f3c | -1.47815 | -51.13225 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13e1bc71-28a9-3f99-aa8d-d7759c37ecb9 | -2.26317 | -50.45713 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d41294a2-6f48-3fb5-9eb3-86873e88078d | -2.88996 | -48.27752 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b6d9f3c-a0dc-31f1-9953-bd18bcf5571f | -2.65655 | -46.14504 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56189281-85ae-3152-9e33-0b4c62f6e43c | -3.00786 | -51.30229 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e549ad88-26e4-39c7-ac5f-c3b1159293e9 | -2.60533 | -48.24818 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bcfb862-fabe-3d7f-a4a7-8f0f42814715 | -3.33888 | -50.49352 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 543f3117-abf6-388e-b0b4-f608e84b3566 | -4.21146 | -45.65032 | 2024-11-21 04:29:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c71c4cdf-4e6d-35a1-aa89-67b9b4fac10c | -2.67223 | -46.23648 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41ccc2ce-8c5f-338b-84ed-2324486967d1 | -1.34031 | -52.92472 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53a1f387-4e77-38df-b995-8f947a199bb1 | -2.01579 | -51.17364 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85975d4-087b-3610-801f-733d3cae0a6c | 0.75305 | -50.24393 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ec92702-0830-3cab-92c5-7717ea01dc3b | 0.41198 | -50.81836 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f340955f-0ac9-3923-9863-6e52dd33a3d5 | -2.68928 | -46.19284 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00f58655-25fe-3dea-a2c9-e73a5256bddd | -2.5191 | -45.62033 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9db39eb0-5a3a-3030-a013-d760c14128b7 | -2.6471 | -46.14 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42742981-5456-3fbe-9947-fd93d6be643c | -2.33197 | -45.66361 | 2024-11-21 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb9857e6-97b8-3aeb-8370-6c52f0c3b153 | -1.46151 | -55.45115 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59cb240d-8047-3484-b9a0-c3a4e96b420f | -2.18918 | -46.40575 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f1825d3-7a62-3813-9c97-a0b041867aab | -3.06949 | -49.2002 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f33abca-a450-3d19-a65f-1427bf8a5a1a | 0.1849 | -51.21791 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b6ab5a7-482c-378e-9c9f-4294049f82c2 | -2.2791 | -48.40829 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d6971d-5cc4-37f6-bd1f-6cb8db708e9d | -2.83716 | -51.81891 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ceaf6978-c688-3aaa-a3e7-2d6e71fedcb3 | -3.54175 | -50.53134 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e121bf56-97c8-300d-a436-f33cefca2873 | -2.25373 | -48.70177 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c567762-8abd-3749-95e0-d0fe8d10159d | -1.59312 | -50.44451 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b3c0971-72e8-3a48-b8c6-b3b764f5a0f0 | -3.47987 | -50.31277 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91478471-fc3a-30ae-ac20-d7b13c3fcbe7 | -3.55438 | -50.243 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b539648f-c45d-3f9b-924a-943a48fcd7d4 | -1.92765 | -49.5133 | 2024-11-21 04:29:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 372b2d66-6717-3225-98f7-97a9abb1b200 | -4.20806 | -45.64979 | 2024-11-21 04:29:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de76d30b-e012-3926-96f7-b2383d2c8873 | -3.27912 | -50.21512 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f674e458-816a-39b5-8f46-3d6499287287 | -3.06599 | -51.36314 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c243be5c-23fb-3772-a04f-4fa18b1b24aa | -2.01531 | -54.53088 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 5fe73ede-2afd-3365-a44e-ca382d757905 | -2.18111 | -52.12457 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baa1067c-994b-3905-a377-339b8544b77a | -4.06218 | -46.84698 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a60fe571-397c-3d5c-8a57-4dedf4bc0086 | -1.39384 | -53.57975 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5fe6c50-a783-30a0-8abf-fec05c66b5ab | -1.45898 | -52.69046 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62da5cc8-bee9-3034-a341-f458a3fb3ee6 | 0.05232 | -49.51611 | 2024-11-21 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0231c9f4-69ea-392a-a330-906084b739e1 | -2.91675 | -46.83425 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf884a0-6736-30bf-8b4e-7fdf4b9c96cd | -1.36687 | -55.69537 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca8003f-292e-3e04-a98e-9cbc02f10ece | -3.18468 | -46.5505 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65269a6d-8b16-36a1-97ab-76cd7b44ee69 | -2.71598 | -49.33971 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 356ecfe1-a550-3252-a3be-6256becd7fd9 | -2.61922 | -51.80575 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21d1c8c5-0ccc-3109-a187-c15b9bcb73d2 | -3.95961 | -46.72481 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43fb1097-be82-3a08-b6f6-ab14b33c8dee | -2.14524 | -53.56952 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c186806-a7cd-309e-95df-fdf7619c1c5f | -1.36631 | -55.69873 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30366c65-4f16-3012-9317-cac70748ad51 | -3.63937 | -46.00612 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61a2c897-3c34-3862-b556-b98899f01397 | -3.81123 | -47.79644 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e5c1b92-4df9-3c18-9877-94a004ed677d | -0.86129 | -51.84348 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e8e0e56-db9e-3419-bffb-fdc71ec35865 | -2.51652 | -46.28357 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8dd9c3f-59c0-30d9-9a0d-19ccac89b17d | -2.21045 | -53.7192 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dfdb9205-cf53-3746-8fd8-fb100892bc37 | -3.9058 | -46.48542 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9125a98-59da-311d-a8f9-587a9b774323 | -1.65707 | -45.44061 | 2024-11-21 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a38b55c-2ea5-3c47-b7c0-a695272a9030 | -1.41058 | -52.10565 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4214e903-ad29-364c-9e05-4c896220d948 | -3.94075 | -46.71479 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fe18e5c-8230-36c0-9059-7347479fb430 | -4.48328 | -44.75386 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed550fb8-3237-396d-8f94-63d0d12af336 | -2.54369 | -47.29173 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a14974c-3ed6-3be8-a1d5-428a87d6b435 | -1.62329 | -52.25972 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74241d7-70fb-3bf2-bbff-4ae2ccddf960 | -2.57675 | -46.54421 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 588f3be5-0f8f-3690-bb1e-c9b7c0a4e426 | -2.65793 | -46.60991 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11215b26-0788-3c84-a5b7-87c3a033b79f | -2.6677 | -46.16101 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd93c5d0-10d9-32d3-aa70-5ed82503cfe1 | -0.92664 | -51.64309 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13b32edb-2bcf-3b37-853f-eb7329991e2b | -2.92402 | -53.07383 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c948a99-d491-3aa3-85e7-6db8b6a0c51e | -1.20074 | -51.77172 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79cfa44c-3e06-33c7-8473-a2d5daf50b8c | -3.7925 | -46.94664 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b581630-ad48-3bc4-b94c-e0e07ada628f | -2.75426 | -52.10108 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b24630d-9049-3106-a78f-afe50ca9c32b | -2.84061 | -51.82315 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51f14cd1-3bd8-317a-8743-3bf13e98325c | -1.36575 | -55.70208 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a594b118-4502-34bb-843e-3754d3868697 | -1.51895 | -51.154 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b702cd93-be94-3f29-84df-f5e72a6b645e | -2.21702 | -46.39948 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a3c88bf-acf7-3ba8-8f12-d57bc9c54a4e | -2.67835 | -46.24098 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06d330af-299a-3af7-8c56-a891d6c0fca3 | -3.67446 | -45.24413 | 2024-11-21 04:29:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f24c108f-e058-3325-83c1-74ae8a446309 | -3.29259 | -49.19112 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6d14e212-46d6-368b-9dfd-39ffee940604 | -3.27549 | -50.21453 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d190e28-0866-363c-9e92-b37e4b4d5679 | -0.93805 | -51.72287 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb57771-c774-33f4-8b45-963f93b90c24 | -3.74828 | -47.35695 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c001742c-fab4-3654-865a-e16c52e53082 | -1.14299 | -53.66771 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d3fbc7c-f997-334e-85ba-a12ff5b74694 | -4.25193 | -43.80713 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aceb1a4-aff1-3b40-8ebb-7ea438b0413a | -3.09695 | -53.17117 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117e586e-a6b6-3806-b818-9fc117af11ff | -2.85006 | -46.67917 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1e10849-4e32-3930-8c62-8ed2233a682b | -2.73333 | -48.65036 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 500e5b4d-5da9-3458-b0dc-04f4aee981d2 | -2.244 | -49.20061 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f58d707b-d387-362a-94b5-36077e27f8f4 | -0.77206 | -51.7541 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e05c74a-08d1-3592-8d40-6cdb5bc3f1f4 | -2.63617 | -46.20956 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8415fe28-2545-3124-849c-cc83da3a9f52 | -2.62416 | -48.06461 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d4a86b-3102-36ff-8788-1550db84e303 | -2.74025 | -51.72542 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 356a2eea-d7c6-3bd4-898e-be40df306ef7 | -2.69108 | -46.84862 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931ee41d-b89f-3e01-87c4-66d8b8b7391d | -0.17496 | -51.62458 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724cfd59-51a1-3b9e-b33f-50f1ce1c2fa9 | -4.2445 | -46.11354 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea5aa14d-4f80-3316-afe0-93fd3421e05c | -1.2134 | -47.61687 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10b3bf9b-4dcb-3a57-921c-5cbc515fd489 | -1.51502 | -51.15339 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7071019c-d546-3445-a359-d06160038e4a | -2.70707 | -47.97597 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f71b2f7-4422-3ffd-a970-6abcad322784 | -2.65546 | -46.15199 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b51242a-0d6d-3f49-ba2f-736434b3b22b | -2.14434 | -53.57543 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 275db6b9-49a6-3d95-8b85-f87a9121188f | -4.57577 | -43.44644 | 2024-11-21 04:29:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47d86a38-6c75-3b0b-b990-f57a1764aea9 | -1.73005 | -52.70561 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1e28574-6c1d-3c0d-889e-9f54ae5ef832 | -3.2932 | -49.18733 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |


[Clique aqui para ver as próximas entradas](README38.md)
