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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e27152a6-323a-3600-91e4-9aa222247647 | -2.61704 | -48.33636 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 978ce79c-d04a-31ee-9860-ee6a482dd417 | -2.6165 | -48.31748 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d77d7e-281d-33b8-a564-b13ccf4e2fbb | -2.61593 | -48.32116 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e597cc2e-cb98-36e9-bf55-6af011805478 | -2.61421 | -48.33217 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e49e697-6640-3bfd-b08e-447aa5aca6b9 | -2.61364 | -48.33584 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003e233d-2015-327c-a423-f2edbba9f937 | -2.61309 | -48.31696 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9c0c9a-da49-33ee-86de-eecb04e8a53f | -2.61252 | -48.32064 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 517d4482-3c94-3ef8-86ce-5b7921a7cf6d | -2.61225 | -48.37255 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b7eb8f1-69de-36a9-aed6-64e12e5178e8 | -2.61195 | -48.32431 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23311de8-0577-33cd-997b-2c981d3d2e22 | -2.61132 | -48.37302 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fffee36-044e-3c74-a7f9-79d096b81554 | -2.6108 | -48.33164 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c30daf-6bdb-32ca-84f0-a290f09fd04c | -2.60854 | -48.32378 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9899071f-2c9e-3ddd-8395-1d274610ec4e | -2.60456 | -48.32692 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f427ee6b-cd4f-3678-a628-883fd527a0fe | -2.5881 | -48.32061 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0539f186-d014-347e-a76d-d2f2cdeb2000 | -2.58357 | -48.28224 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97e74741-e19b-3518-833e-0e8616d035cc | -2.47437 | -48.48666 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e5c73fe-310e-3d85-a10c-08900ec520a2 | -2.47155 | -48.48251 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 198e9703-bf62-38d6-85df-3bf5c2919b0e | -2.46591 | -48.49651 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52dc43d7-f9ff-39cd-b29d-73e844361122 | -2.46421 | -48.50737 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1938b725-8c71-3cae-abb0-2517f118300f | -2.46252 | -48.49599 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae63e8ff-0d82-32b5-9e4b-7787cefdfad8 | -2.45745 | -48.48402 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ae17a8a-a945-3a0c-bb01-04b5f9f2719a | -2.44278 | -48.48919 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1303a6b0-d008-3e7a-995d-f46675ced600 | -2.44222 | -48.49281 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d39a8047-3eed-3894-a750-a9897170fb07 | -2.43995 | -48.48504 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e52eee6-8bd3-3b3a-9d32-f7574bc94371 | -2.43883 | -48.49229 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc86bf7f-0186-30bf-967b-d563563bad29 | -2.43771 | -48.49953 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f01d257f-14ed-377a-b238-a74a511539d1 | -2.43657 | -48.48452 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f77b015-2bdf-3261-ab21-43955db6e05b | -2.43488 | -48.49539 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e0b92f9-b4da-309e-9218-9a57f02b0b7d | -2.4315 | -48.49487 | 2024-11-03 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 049f9a1f-0179-3791-945d-a495631f1998 | -2.42979 | -48.48348 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50f7f98a-c413-39cd-b1f2-9b409f73dbb7 | -2.42302 | -48.48244 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a123b9-2a39-3371-9ca5-563c68dbe7cc | -2.39977 | -48.43058 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1499a1d1-ee9d-3900-9f04-60864af9b6dd | -2.39922 | -48.43422 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4165716-dbf2-3741-b14b-899657ff86ce | -2.56404 | -47.39976 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe924c2-3be4-3e7d-9bb5-ed47c785200d | -2.54692 | -47.36939 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ce8a5f-50a8-333c-b3a2-b9d624f01718 | -2.53859 | -47.37629 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fe221fd-1806-37b2-8902-d381762d9ed5 | -2.53665 | -47.509 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e82372e-9852-33ab-a8c6-1c4c28bfba70 | -2.53605 | -47.51294 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7004ac15-bd4a-3354-a443-4689a0aac7c4 | -2.53443 | -47.37973 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061032cd-ec40-3b9f-8398-85fbd4601218 | -2.52149 | -47.46292 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c06b0f2-aa0a-35fa-af1d-54f940d17028 | -2.51796 | -47.46241 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c9cb0a7-cd5e-3857-a59e-04bc522a3473 | -2.51443 | -47.46189 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee083e5-eb7e-3ed1-9a87-e83a7f3138df | -3.50019 | -48.23264 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4bd9dd1-213b-3b89-8d1c-fc84ff23c379 | -3.49675 | -48.23209 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43c6f75-860e-3bbd-9d0f-4542a7fe641f | -3.45782 | -47.66637 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 884069c4-28f2-365a-bffa-396c106fe4ff | -3.45721 | -47.67031 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3de76cc7-8cbf-342a-a7b8-5c3473d05570 | -3.40867 | -47.58587 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15fc20eb-24e5-3f0d-8d42-4fc7dcb0d219 | -3.07653 | -47.57867 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76a60051-dc42-330a-bffa-f27779ca3fb3 | -3.07593 | -47.58263 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d9173ec-25b9-3838-8354-233b7bd6d06a | -3.073 | -47.57813 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6da05fc-7983-3397-bf24-2f84da96b079 | -3.0724 | -47.58208 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e1b600e-26e5-37f3-83f6-0ccf06178bec | -3.06888 | -47.58153 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c355960-a452-32ba-9084-560849952ec5 | -3.06555 | -48.00146 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d486cdb8-e905-369f-8a26-0bb61330a704 | -3.0435 | -48.07574 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d48add69-27c9-37ca-abf7-b6897c1fadb9 | -3.03659 | -48.0747 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c3efb6-1119-3115-b206-410db5ce95c8 | -3.02403 | -47.94831 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcb48ca5-6e75-32ff-a82b-41778691a4ef | -3.02173 | -47.94012 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f237938-7b89-38d7-86fe-5d755ca15eb6 | -3.01991 | -48.06826 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b1703c7-3139-32b8-bfb2-1fae2c17e0b5 | -2.72692 | -47.99025 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9642686-686e-33cd-8b70-66b40af78d98 | -2.72634 | -47.99401 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eed170b-dab8-33cd-88d5-0c40627e9407 | -2.72289 | -47.99349 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6a0ab82-9ec8-32ac-a55c-b4d1449ec8cd | -2.72231 | -47.99725 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c61ca814-7227-37ba-a5f7-004a5252fee3 | -2.71886 | -47.99672 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ac05bd-696a-3f2e-af98-7e45b320016e | -2.68032 | -48.13313 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12d37e68-cb44-3b47-92ab-67d51865fe60 | -2.67974 | -48.13686 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 971d3bae-eaac-36f6-ab4e-134d6dfc7046 | -2.67688 | -48.13259 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09260ecf-866e-38bc-87ae-078b4e3ec6ab | -2.67631 | -48.13633 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06a2d57-1476-3647-8382-8f6e1cebaf08 | -2.67574 | -48.14006 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 053c38e6-6dc4-389b-8886-ea5270fb6c79 | -2.67288 | -48.1358 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6659b547-745a-3545-8a1b-7c544d662add | -2.67231 | -48.13953 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15df195e-5e25-3a2b-a58b-71b7c1643165 | -2.66945 | -48.13526 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34346422-ca33-375b-9c78-1d2dd4dc7650 | -2.66888 | -48.13899 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1895ed5f-229a-3ce3-8ea6-f42a74b671a5 | -2.59955 | -48.22421 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecbb58f9-963a-3a29-9a1e-5678fd14cd19 | -2.59897 | -48.22791 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5950e6e-bd3b-34cd-9f53-2296ff6144e6 | -2.59555 | -48.22739 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1798031-73c4-3743-8fc8-418ef5fb6f21 | -2.59498 | -48.23108 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3548e3-2bc5-374a-be94-6277fa1c55d7 | -2.5927 | -48.22317 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a18b0680-7f70-3cc2-91e5-831fc4265e40 | -2.59213 | -48.22686 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4efe16b0-c13f-3af9-a719-bc96675289ac | -2.59156 | -48.23056 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b165e0-3e53-392f-8366-00914b76ba1d | -2.54878 | -48.16706 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 469fb22e-c198-3faf-8755-0a5b37cdcda5 | -2.54821 | -48.17077 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed853fb2-b3b9-3fd5-ae3d-aceb38b3142c | -2.54764 | -48.17448 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2f7cc5f-fd83-39cb-a544-f465202148d5 | -2.54535 | -48.16654 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a085977-51fc-3977-8245-6e30e0280b0b | -2.54478 | -48.17026 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 938d7d8f-f968-3459-bc0d-25c498d796e3 | -2.53912 | -48.20732 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5e95cc-fd02-3b23-a4c8-1e2ba678eade | -2.5357 | -48.2068 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 833ba728-b75a-34b9-be08-fb9c11c99729 | -2.50876 | -48.13099 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80dc448f-898c-336a-9c7a-9db00c7cefe2 | -2.49913 | -48.05694 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2aed067-5507-3850-89de-8b25f89512fd | -2.49855 | -48.06068 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 724b1bb5-fe35-3be3-b066-339bfb412186 | -2.49381 | -48.2274 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd7c591-b8b2-330a-8146-bc88749794f7 | -2.49324 | -48.2311 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edaba541-ed81-3b2d-851d-a391e2dedf5a | -2.49039 | -48.22687 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56bd823d-727e-39bf-afc2-c1b5c60c338e | -2.47278 | -48.0452 | 2024-11-03 04:46:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87b2acc3-ed03-318d-befc-cafb40cdced7 | -2.4722 | -48.04895 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40850e6b-aa6b-37c3-9ff5-c1126d9a5137 | -2.47163 | -48.0527 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 718f0cc6-e648-3cd8-a93d-f5b22cef17d5 | -2.46876 | -48.04842 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f0c8ed66-ba29-319c-81c1-bfdaa640e814 | -2.46819 | -48.05216 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b89ea933-2637-312c-95ad-4b4be727dc62 | -2.43173 | -48.19891 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21785324-bce4-3e3e-8f90-a66352132dd7 | -2.41925 | -48.23484 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88277293-263c-36ff-a956-48a9a24b7758 | -4.10685 | -48.50658 | 2024-11-03 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README41.md)
