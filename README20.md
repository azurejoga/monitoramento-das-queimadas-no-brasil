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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9cc800f-fc41-3b3d-9f8c-327465b1f189 | -11.8368 | -51.2641 | 2025-05-31 08:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 74ed6420-8379-32e7-99e3-f043ce72b903 | -7.983 | -50.699 | 2025-05-31 11:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1e68e990-9b05-34c0-a40c-ceed68f75725 | -8.0017 | -50.6975 | 2025-05-31 11:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1e6de452-fe9a-3a64-81e9-0c051c156029 | -8.0017 | -50.6975 | 2025-05-31 11:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| bffa4b5b-5e54-3df2-a1b3-638195d73690 | -7.983 | -50.699 | 2025-05-31 11:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5fd935df-3754-36b2-a27f-54969d1c009e | -8.0017 | -50.6975 | 2025-05-31 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| c67c6e41-711f-3734-a338-9bb147bfb561 | -7.983 | -50.699 | 2025-05-31 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 2fd9e2bf-933a-355a-ab14-078e889cc187 | -7.983 | -50.699 | 2025-05-31 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| e4883818-d9ee-3542-a39e-7bbde913555b | -13.1068 | -45.276 | 2025-05-31 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f0c4cbf0-f60b-3bc9-ac27-e82c1ee4c989 | -8.0017 | -50.6975 | 2025-05-31 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 9f7a8fd5-0b51-3b64-91a0-50fc984225e4 | -7.9832 | -50.6779 | 2025-05-31 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 139d669d-a98f-3114-87d1-3adc927c7810 | -7.983 | -50.699 | 2025-05-31 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| e9a744bc-0c5c-3a5a-9ce6-a2addcf9594b | -7.9832 | -50.6779 | 2025-05-31 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| a5f6ae98-dd89-367e-9924-2e2f9e4ebe39 | -8.0019 | -50.6764 | 2025-05-31 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3cf145ac-cd35-391e-8b3c-12e85f9c61c7 | -8.0017 | -50.6975 | 2025-05-31 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1e284253-b566-3c98-ae85-4e429869d801 | -13.1068 | -45.276 | 2025-05-31 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d6902183-6bfa-36c1-959f-573ae6bd32d7 | -8.0019 | -50.6764 | 2025-05-31 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 81e1f5d4-cea9-3038-97a9-c4e705b8fa6e | -8.0017 | -50.6975 | 2025-05-31 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 6f117400-015a-37a5-9e3b-d6d49adf4f57 | -8.0019 | -50.6764 | 2025-05-31 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| cddff064-eaba-38f9-afc5-84a7cd686b73 | -13.1068 | -45.276 | 2025-05-31 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 293132c6-6720-3367-b0d9-918e06de1af3 | -8.0017 | -50.6975 | 2025-05-31 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 0f98eab6-1639-3f76-9af0-f209c657ecf4 | -13.1068 | -45.276 | 2025-05-31 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9bf31be2-c016-3e84-b028-14983c49641f | -8.0017 | -50.6975 | 2025-05-31 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| ee769781-3777-3573-8a50-d28a0f582b95 | -7.983 | -50.699 | 2025-05-31 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f113dad5-bac5-3b02-aace-b9dd1520f2aa | -8.0019 | -50.6764 | 2025-05-31 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| cf130d75-845a-3914-b8ae-cb795cdbdb23 | -8.0019 | -50.6764 | 2025-05-31 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 31bb8020-1e68-3030-80f0-f48b3d8ac682 | -13.1068 | -45.276 | 2025-05-31 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e451a1dd-2436-3961-9905-bdc7106f3dc2 | -7.983 | -50.699 | 2025-05-31 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c2f009c3-3669-3a0e-8a3b-2d435f1d2ed4 | -8.0017 | -50.6975 | 2025-05-31 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| a46915b8-14e9-3d56-a7c9-cc2ae017ca0f | -7.9832 | -50.6779 | 2025-05-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3db2a414-6ab5-3992-814a-834d17ec92fa | -7.983 | -50.699 | 2025-05-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 86d20942-119e-33f3-90ab-bbef44d87151 | -13.1068 | -45.276 | 2025-05-31 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5266f913-afa1-39e9-9d90-88c92ba33ce1 | -8.0019 | -50.6764 | 2025-05-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 8c0808fa-8889-3ebb-8d8c-bacd30e3bf09 | -8.0017 | -50.6975 | 2025-05-31 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 08a3ec94-fae9-3c43-9ea3-8d261827a8f9 | -8.0019 | -50.6764 | 2025-05-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 9534fd9e-f1e2-3e02-8c1b-8a9167fd88a5 | -8.0017 | -50.6975 | 2025-05-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| e3a997fe-8990-370e-8381-a6521ebab07b | -13.1068 | -45.276 | 2025-05-31 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 462fde0f-9384-3a48-93f0-a9634139b41a | -7.9832 | -50.6779 | 2025-05-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fc9a05b2-b8b8-3320-86e7-4e04786cd570 | -7.983 | -50.699 | 2025-05-31 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f3b108a4-d599-3106-8954-8feec0f4f15a | -7.983 | -50.699 | 2025-05-31 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| dcc9c763-4be4-33c3-8399-8eea939f1100 | -8.0019 | -50.6764 | 2025-05-31 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| d32b4d77-64c5-3671-927f-2912708fa983 | -8.0017 | -50.6975 | 2025-05-31 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| b7605fbd-5893-3840-94ac-8244fd6a3095 | -7.9832 | -50.6779 | 2025-05-31 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 764a06cc-c999-34d4-8ff9-9d4f5c149afc | -10.1503 | -47.2266 | 2025-05-31 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f0a9ad87-67d3-3968-957a-d19dc1454db5 | -13.1068 | -45.276 | 2025-05-31 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 2054def1-26e4-3efe-83fd-d6596b589411 | -8.0017 | -50.6975 | 2025-05-31 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 47aaef86-8892-3eab-9bbe-9df9a4eb7202 | -7.9832 | -50.6779 | 2025-05-31 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| df4a3fc4-2545-3f8c-a89b-1084e926ea76 | -13.1068 | -45.276 | 2025-05-31 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 075c141a-e4f0-3eb2-8105-56923ffec020 | -7.983 | -50.699 | 2025-05-31 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0411b026-2f2c-3527-850a-bc22e2f85146 | -8.0019 | -50.6764 | 2025-05-31 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 138db8cc-1183-32a6-b6ae-31674a90e92c | -8.0017 | -50.6975 | 2025-05-31 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ab765437-2f35-3ce4-b815-b708daa90ffd | -8.0019 | -50.6764 | 2025-05-31 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ccd2925c-af4c-374b-a6db-0470607ef572 | -10.1506 | -47.2044 | 2025-05-31 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 421f2cdb-640c-35d6-b008-9b41abd98df4 | -13.1068 | -45.276 | 2025-05-31 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 899a5d06-c58a-374a-9121-8892664f0ae1 | -3.5483 | -43.1945 | 2025-05-31 13:40:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b997c5a3-086c-389e-8496-649afb07aff6 | -8.0017 | -50.6975 | 2025-05-31 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e25abc8e-e98a-32b7-8ecb-3de4dea48130 | -10.1503 | -47.2266 | 2025-05-31 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d32f59bd-a19e-352e-948a-86623ce94c20 | -8.0019 | -50.6764 | 2025-05-31 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f8902542-df89-3d8d-b811-92ca2801c96c | -13.0874 | -45.2791 | 2025-05-31 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| a15f58bb-cbc3-3968-b319-103a63ebdcf4 | -10.1506 | -47.2044 | 2025-05-31 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f472cc01-3cbc-317c-9002-de01bcdecfd0 | -10.1506 | -47.2044 | 2025-05-31 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 65c8a7ac-9ed2-3739-9329-e767db2025d3 | -8.0019 | -50.6764 | 2025-05-31 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 61c7a5d0-eb50-3f4b-ba4c-feeeb338f73b | -3.5483 | -43.1945 | 2025-05-31 14:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8fb6b0af-3a5d-3094-9a94-2d7c86ac91b0 | -10.1506 | -47.2044 | 2025-05-31 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 2c7734d4-7ceb-3d16-ad57-c750df11c735 | -10.1506 | -47.2044 | 2025-05-31 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b9dc97c0-3de7-30e4-b2fe-9154691828f4 | -3.5483 | -43.1945 | 2025-05-31 14:20:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 44ba5acb-900f-3193-8291-9e16c2b8a385 | -10.1316 | -47.2065 | 2025-05-31 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 83e73484-cff7-31d1-8507-29201ce71036 | -10.1316 | -47.2065 | 2025-05-31 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3badd66f-19af-3c3e-bb87-11a9994867cd | -10.2747 | -46.4969 | 2025-05-31 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 16acac35-4d7d-3dde-be8f-ad85ff287170 | -10.1506 | -47.2044 | 2025-05-31 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |


