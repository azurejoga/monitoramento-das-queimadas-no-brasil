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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de5fab7-6c56-324f-b657-287028de8939 | -2.5758 | -49.82154 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b662640-3ce3-3cb6-aea8-cb3deb3d9199 | -2.5658 | -49.7989 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e2177a-ba01-3f2e-b014-7879137f71b5 | -2.5625 | -49.79839 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd1779a7-c220-3e0b-a714-43aad75aaadd | -2.55973 | -49.79444 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4d4e29-b5b5-3e36-a9d4-fe35a90d57e8 | -2.5592 | -49.79788 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecb939a1-1234-3d28-a992-661db8f439de | -2.55643 | -49.79393 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d26ace57-3b75-38ac-b939-059b2a469b97 | -2.5501 | -49.8563 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a89315-9a4c-3241-a7d8-74087d877797 | -2.54956 | -49.85973 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 336c0d3c-1f02-3c82-a07d-a501e89bc50a | -2.54872 | -49.66939 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6cce5f-7966-3d3a-82df-beeaad15b826 | -2.5468 | -49.85579 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5de26b50-e2d7-3039-96a2-59e68638188f | -2.54573 | -49.86267 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5389c391-4726-31a3-b532-a813fd93298b | -2.54438 | -49.80616 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fc46a15-eded-3e69-8818-c9cb76df3be2 | -2.53145 | -49.8675 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cfdea80-15d4-3802-a243-853c3ac478a9 | -2.53101 | -49.65255 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcd73506-0a17-3d54-a3cc-c4943b05223e | -2.53091 | -49.87094 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4f9d0a5-d8ae-3215-bd31-f23551b1bf11 | -2.52805 | -49.84587 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9fd634d-e8e9-38dd-badb-34cecb877b3e | -2.50369 | -49.65124 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d27f01-d98b-3323-9412-39778d611855 | -2.501 | -49.82411 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0078ff59-e784-3405-a3b7-5fb6b1de4256 | -2.49222 | -49.81154 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01a0435c-226c-3e58-ab21-829e8a3ab1be | -2.48945 | -49.80759 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0e7cd17-a86f-32f0-86ec-377d469d18c5 | -2.47196 | -49.83305 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67e871c8-246f-3508-995a-dcf729484dcc | -2.46241 | -49.78584 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d13fad-1049-344a-9217-842497ef67c1 | -2.4591 | -49.78533 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a44fc62-1b47-3be4-aa59-5e5f0f52ba5d | -2.44284 | -49.71593 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8281994f-5767-33d0-b06f-9d49f1c3d29e | -2.43758 | -49.77146 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c336e963-6353-351f-94d1-a742ba33d15a | -2.42315 | -49.86421 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 979c292d-fa5a-3caa-987c-5438d54d127e | -2.42261 | -49.86765 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6729db-72f8-3bb1-b81c-3b5c8504425f | -2.41931 | -49.86714 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a61833-a426-32d6-b572-508253a3d127 | -2.41805 | -49.83179 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d2be63-d588-3d51-a8df-cac85414fbad | -2.41421 | -49.83472 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76129477-533b-3ada-a478-c717ea759cd8 | -2.41091 | -49.83422 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17cb1342-5f75-30a9-b349-646e6f74f78c | -2.40255 | -49.70977 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca7e1e6-d4de-3b5e-b994-30db7db0d845 | -2.39634 | -49.77568 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc773ea2-2f83-37b8-a599-8fbb88598b27 | -2.39236 | -49.7751 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00cd1d2f-f3f3-3cd8-a32b-c009f073ac9f | -2.38149 | -49.89296 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c003ee2-1aab-35a7-af1f-fc6e6a7d7595 | -2.88632 | -49.46689 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32fcb3ff-78bb-326a-a4eb-edd890a1f81c | -2.88578 | -49.47036 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c5be27-b4ee-3025-91cf-0e7b3ea2f465 | -2.88496 | -49.40923 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 657e7439-cb5c-32ce-813f-7d32e9edf37a | -2.88441 | -49.41271 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63113fb6-5d18-37aa-afaa-f788cd42aebb | -2.883 | -49.46637 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 277bf787-ff2a-31f6-824d-ecc7be6ae1d0 | -2.88247 | -49.46985 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 47df1fa9-941a-345e-8c17-e6a9dcb6eb2a | -2.88193 | -49.47332 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 338cbee5-0dc3-38b9-b81c-db3bfef3a885 | -2.88029 | -49.33003 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4693947c-81cc-3d16-8f8b-1a7b9ccb3f9e | -2.8775 | -49.32603 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21028433-89b2-3260-9efe-79f1f5f4d857 | -2.87696 | -49.32951 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3896e5b-70a0-3d8b-9477-a5e5163a248f | -2.87418 | -49.32552 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03560ac3-6c0e-35e2-b870-900c97670bcd | -2.87384 | -49.39326 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e098e241-2f3b-3d89-82d9-c67929b977f2 | -2.87364 | -49.32901 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac17ab23-1cd8-3d4f-ad8d-0fb83edb301d | -2.87309 | -49.33249 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ff2a007-6f52-3b7d-8aef-8f91067305da | -2.87085 | -49.32501 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03f13933-2010-38ae-af5d-2d45e74c65e7 | -2.87031 | -49.3285 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2317a5f9-e96d-37c1-8996-292720d03b58 | -2.86984 | -49.35342 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9d96261-b6ed-3372-8b0d-aa6ff6f153cc | -2.86977 | -49.33199 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0156a220-5e3d-387c-ae64-8f38cbbdab72 | -2.86929 | -49.3569 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56a5fbd6-67d3-37b6-b064-ed4c429c4c33 | -2.86774 | -49.38876 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa55a053-75ce-3b67-9750-1aa41de1a02d | -2.8672 | -49.39224 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 444d8a73-6d14-3e5b-a691-fc0ff8549840 | -2.8655 | -49.38129 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 412212fd-11a4-36a6-b5fd-42495af5ae4d | -2.86496 | -49.38477 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 698d0b20-2c9a-3423-b0a9-57a8aa504012 | -2.86442 | -49.38825 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07c6e97f-4f4d-3b40-8876-bc831418e995 | -2.86434 | -49.36684 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d82eb1b-48be-3510-94dd-3c2f7da5aba2 | -2.86387 | -49.39174 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c479067-2589-3eda-ad42-9444322b6d2b | -2.85467 | -49.45084 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce5a2ab3-4d9e-32c8-aa2e-3336962e2150 | -2.85445 | -49.38672 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62caf06-b075-3073-9128-d1f7fa926f1c | -2.85251 | -49.46474 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412b361b-0edb-3a85-b280-da1924474269 | -2.85243 | -49.44339 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eee7577-e16b-3173-bba6-b7a778a2ab8a | -2.85197 | -49.46821 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950b9fe8-eba4-38b6-92f1-7016f12d85a6 | -2.85189 | -49.44686 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1813caf2-f390-3d40-a364-7c6fa039b121 | -2.85113 | -49.38621 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb8a4e5-cbd7-3dba-bcfc-2bb9056be619 | -2.85111 | -49.5391 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77e8b7ae-8933-385d-997e-89b7953ea986 | -2.84927 | -49.48557 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c4a59e9-de07-32e2-89fa-c18a8d6ff4d3 | -2.84873 | -49.48903 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db8f5a22-bc82-3eb5-892a-18980dd48ca4 | -2.84834 | -49.53513 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be7954ef-97d2-30b4-855e-427e031ba63a | -2.84819 | -49.4925 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59831aa9-3d0c-3a5f-8c3e-766155c2b4d0 | -2.8478 | -49.53859 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 572d92dc-b1ac-35b7-8745-e37000a39ab0 | -2.8478 | -49.3857 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f5430c-a9c8-34bd-ac08-7b229ddaeac1 | -2.84641 | -49.46024 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf6e070-74a5-320b-b8d9-e5ada8f3c968 | -2.84595 | -49.48505 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7fb6c73-d986-379f-94df-1ab3b93f3b64 | -2.84556 | -49.37822 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4e2dc08-5268-3b3d-9f6d-283693ab67b2 | -2.84541 | -49.48853 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e78bf378-f6e9-3416-b8e0-32d37bccb911 | -2.84502 | -49.3817 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a40de479-f3f4-3987-804f-1d1d566c74b7 | -2.84487 | -49.49199 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9addfbc7-d272-3db1-91d7-d7bf50451507 | -2.84448 | -49.38519 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e277c33-4fae-375e-a49d-3254d4424146 | -2.84263 | -49.48455 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28ef1b1a-5caf-3ab7-b926-0fbb748bb01f | -2.84224 | -49.37771 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21a49b52-e509-32b1-8ef1-3982bc22ec00 | -2.84209 | -49.48801 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66854771-eeeb-3e08-9925-427a5fb43d32 | -2.84208 | -49.33487 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a38526-88c7-3a39-98bf-5d1f0f50f65a | -2.84032 | -49.45575 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9776309-4d52-3408-8844-3789c6c878b5 | -3.07362 | -49.5738 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9212abe-0f7e-39f5-b3d4-042ec876e2e4 | -3.07085 | -49.56983 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfcd4cb9-df0a-3259-87f7-91328b613569 | -3.0703 | -49.5733 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 961e0477-1c29-3978-bf1b-3ede43370cc2 | -3.06753 | -49.56932 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8c0e97a-24f5-30a6-b7fc-98599c929559 | -3.06529 | -49.56187 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b2413a7-c984-3e10-a480-48a6e31deb3f | -3.06475 | -49.56534 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7be4398e-af16-3ec4-b9c1-425141ebb499 | -3.03442 | -49.71653 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b096f7b8-3c89-3fad-8e76-62ae8cdc4289 | -2.9968 | -49.23738 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f4759887-e6b9-352a-bbdd-ce0bdca80b03 | -2.99625 | -49.24088 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95b4b2da-c1e3-31e6-9150-d7a7163b2657 | -2.98721 | -49.51791 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 91da180f-e879-3a10-a609-672bd58f6bd3 | -2.98443 | -49.51392 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58201990-b7a2-3c43-9ca0-d3ec03beaf17 | -2.9839 | -49.51739 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4437f950-6a40-3150-b919-c1ff449ff80c | -2.95247 | -49.56583 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README46.md)
