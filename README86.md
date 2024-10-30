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
| 5f5f0703-1ebc-379c-9d06-d7d9e4fe6442 | -3.52114 | -49.234 | 2024-10-30 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1eeb57c-99d9-3841-8af7-fa9f95bdc81b | -3.37558 | -49.54801 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1313419f-248d-36f1-85c3-864be055dc33 | -3.28767 | -50.00602 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d8f842-26e7-3a97-ac59-7e55bd8520fa | -3.22448 | -50.18363 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7d6a91e-0628-3590-8fd6-81d2e5c9f010 | -3.12433 | -49.29652 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2fa07bc-e567-3089-ae37-4417de324fee | -3.00408 | -49.58476 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c101ddff-fdff-35ff-abe0-ecd1a522e1bd | -2.97243 | -49.10605 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211453ba-0ac1-32d6-b64b-62e4f757fad0 | -2.96765 | -49.10532 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d846fc3-766b-3b0e-bed5-adaadb4d8b6e | -2.89123 | -49.47044 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4e1863a-6c42-31b1-8f55-0c31c7c5e17d | -2.85865 | -49.4656 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcbf398d-02b7-3ae7-95aa-b6495db74886 | -2.85622 | -49.45041 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 344e8d63-bb5e-3c40-8765-640979501bff | -2.83994 | -49.24055 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1aaa5b7-c932-3e80-8f5f-3983aae354a0 | -2.83919 | -49.24558 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8388ec65-4783-3414-a21d-7215363c2477 | -2.83521 | -49.23985 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2c17536-07e2-3d95-8a7c-1fee59a46916 | -2.83049 | -49.23913 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3a4e9e4-5702-3e4a-8977-b0145c5fa0f8 | -2.82651 | -49.23339 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45692e15-126d-362b-b7a1-8420a6c618db | -2.82576 | -49.23842 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87fa1d0d-b454-310a-ab14-230719784acc | -2.78921 | -49.48479 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21efb4cd-6896-3a54-af39-597b5860f6bb | -2.78527 | -49.47935 | 2024-10-30 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ae18b4-f65c-3303-92df-aa40b546aa07 | -2.63226 | -49.09101 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a10d126d-7c4e-3096-918d-1c847e58b1f6 | -2.62474 | -50.07741 | 2024-10-30 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 305267db-949b-38f3-a64f-c9b114736c31 | -2.52491 | -49.08796 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8810d27c-e471-34a4-a39e-98e1793bfcd5 | -2.51939 | -49.09241 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2fef6ef-5400-37b3-8030-005ed61518ab | -2.51463 | -49.09171 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 033aec4b-bfc8-36a1-a1fc-ca58f66b1881 | -2.5091 | -49.19415 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9eff703-44d1-3320-8b3d-9fde8e111944 | -2.50771 | -49.16242 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa86e0d-4e8c-3806-bd28-7ed1a621ecce | -2.38911 | -49.18042 | 2024-10-30 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19571ba3-882e-37b6-92d6-e24c7b4a3416 | -3.55317 | -50.30341 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad25961-c64a-39d0-84c2-42acd6e3c3bc | -3.52511 | -50.37037 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc09e58-b988-3d90-9176-fe8e75c0a5ae | -3.51433 | -50.47336 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc72f180-61a9-3d7d-be02-e227952fd1cb | -3.51368 | -50.47774 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2ec7a30-4977-3b00-9d47-e9c19bce87bc | -3.50995 | -50.47268 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c209f4-18dd-3f79-a85e-f5572cb1ae30 | -3.50932 | -50.47697 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9afe4566-7093-35b4-9184-7775e8737df6 | -3.35606 | -50.26925 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 136fcac5-8132-3958-9e96-f9a50c8f49b7 | -3.31939 | -50.24138 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b29dc25f-46aa-369f-aafa-d3b326f6149e | -3.31924 | -50.30354 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d74e3534-faac-389d-b963-b297dbd77ec7 | -3.31548 | -50.29839 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6b81603-86f3-3e71-b27f-5de4867d1ab2 | -3.28971 | -50.23349 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 982a8eb3-e47c-320e-8ab6-a741ad3ae2b0 | -3.28902 | -50.23803 | 2024-10-30 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2664267b-6f74-3eb4-bccb-2db00897bc46 | -3.27239 | -50.34638 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d875cf-7a4c-34c4-8ed1-3eacfc6253b8 | -3.27173 | -50.35065 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b315dd50-a325-38df-9293-0216009914db | -3.27107 | -50.35494 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d50edbd4-a97a-3f41-ab4c-b10f505d36f6 | -3.26864 | -50.34142 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf440b51-3179-3544-acb4-182d420e9e7b | -3.26601 | -50.35857 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 881fd935-15b3-3ff9-92e3-96e383aa1169 | -3.26358 | -50.34505 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2748d551-b041-31a2-9317-b6c6ff86acb4 | -3.26227 | -50.35359 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f03afc6-3c94-3618-bdb9-5259f34916a5 | -3.26095 | -50.36222 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee8659cc-a73b-3c74-acbd-445a0bd3eada | -3.25983 | -50.34008 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d6dc383-b540-33bd-b25b-726867a3f3de | -3.25852 | -50.34867 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c7852135-d9f4-39be-90c3-b6fecbed005f | -3.25787 | -50.35295 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ab515038-5910-3ec9-94d0-8b9c9ca04b69 | -3.25542 | -50.33943 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 922cd6a0-b044-39d0-9404-79fb87f95150 | -3.25412 | -50.34801 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3dc09ac7-318d-35f8-bb88-fd9f4c1b48b8 | -3.24972 | -50.34734 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eee8d5b-1e3d-3627-8f88-0d56a0a65e7c | -3.24906 | -50.35166 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 804e608c-3dee-33b2-95c8-8907e5d06a09 | -3.2484 | -50.35597 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5de725d-edc7-3fd3-8529-f8eb9da19972 | -3.23057 | -50.58965 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b485c78b-af4b-3fe4-adda-e52c45ca0f01 | -3.22688 | -50.58488 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62a837a0-63ef-3fee-a63f-c5fb1270640d | -3.22625 | -50.589 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f49abe4-9f9e-33fe-9261-209365a5f291 | -3.18072 | -50.3867 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed80fab-f4cb-3406-a15d-cd5beb84f36d | -3.17941 | -50.39518 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c16e12-b558-3cc6-a47a-d011ae8af320 | -3.17875 | -50.39939 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3cb0226-0669-3985-91a5-c9e793afa8d5 | -3.1774 | -50.5901 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 702ca901-7914-3c0f-9988-58890c00706a | -3.17487 | -50.39724 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b26c3c3-99a3-35e7-99ca-d4fbc813b3d0 | -3.17369 | -50.58533 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbac004d-994a-3164-980f-44460546f765 | -3.16936 | -50.58468 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 660be6d9-6bd3-3ead-bf19-58f2c08ea1bf | -3.16875 | -50.58879 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c6f0c8e-d28f-376d-91f5-655f541bfe67 | -3.16442 | -50.58815 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9bcb169-c9ac-3168-aec5-83f9b93705eb | -3.06427 | -50.50671 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45db1b52-431d-3f86-ad52-f38c7180a598 | -3.04641 | -50.41073 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 513903a8-448f-32d0-bec2-a50666bc6804 | -3.04513 | -50.41905 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 488e5ed3-37b5-35bc-8ffb-8d7e30d3ed36 | -3.04013 | -50.42251 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84b82ace-0efb-3f5d-86d0-187652cfd999 | -3.03575 | -50.42189 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bb0c124-ac1d-3aad-b740-dc9d26674ea8 | -3.02828 | -50.41233 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d678507c-afed-3571-b189-e9e7c1640ec4 | -3.02391 | -50.41171 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84f2ab42-e839-3fe9-8e39-2286ef379a81 | -3.02327 | -50.41591 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78f7f2a-a308-3c56-984c-e7949d39f129 | -3.00681 | -50.49471 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cae642b4-4a54-3d4f-bd50-5fe26641e06a | -2.95969 | -50.48314 | 2024-10-30 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeeb67fb-8875-38f3-94e4-16073adc8cd6 | -2.35788 | -50.32399 | 2024-10-30 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56157f21-c19a-396e-a982-ad5a9972d0b6 | -2.35725 | -50.32817 | 2024-10-30 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8aa882b-5554-30b3-8e24-e6184c9daa24 | -4.84698 | -50.76441 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a46517c-4f11-366c-84a8-938ec21a65c4 | -4.84649 | -50.76598 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445384cf-762c-3a8b-8942-f91775f68dec | -4.84635 | -50.76879 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e870c54-5f09-35db-8477-7fb830e17f6a | -4.71125 | -50.73806 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55063ba-d8be-333a-9eea-68ebef9651dc | -4.70469 | -49.50265 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f8bdf6d-d8cf-32db-87e6-fbc3a847e801 | -4.70387 | -49.50547 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86b6a0e-3317-3a78-a362-760165638727 | -4.60275 | -50.56141 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 189b8e45-c35e-305b-8b1f-c132f2118188 | -4.6021 | -50.56575 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29509b8c-ddcd-3e2a-a193-6d4d52b05fef | -4.56536 | -50.41211 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81813690-f066-3cbe-bab4-12619bbfdbcb | -4.56473 | -50.41652 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67ba0684-b077-335a-b134-f53059e8c9c4 | -4.56236 | -50.41333 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66ce0f15-e09d-3c79-84de-a4c9dd3c0db1 | -4.55653 | -50.51195 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb2dbc52-55df-3af3-a166-8114b2f119c9 | -4.55581 | -50.51036 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6e9bb7d-dcde-36bb-a31c-08a0eeeb3a64 | -4.52529 | -50.41679 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5c51304-9826-3d95-8cbf-5df590f618d6 | -4.50294 | -50.19223 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0406e0fd-88b3-319a-937c-1eb2ad12fd37 | -4.50212 | -50.19093 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8f2de46-9317-3ff9-8e85-bd05902bdafb | -4.49841 | -50.19149 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e57cfb1-e3be-3283-9f90-df35961c8b08 | -4.49759 | -50.19022 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f626228-c78d-31bb-8fa6-5545d099db3c | -4.47297 | -50.26117 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8250fb3-8ccb-3732-9f30-505bd9fe60f2 | -4.42425 | -50.46341 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef666a9-28c5-35f0-997a-8b0f4c5adaf7 | -4.4236 | -50.46778 | 2024-10-30 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README87.md)
