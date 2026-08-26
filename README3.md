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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3af9c62e-dabd-3999-b53d-19101f349b39 | -10.3918 | -45.0512 | 2026-08-26 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 288c4e5c-34a5-3e0c-be47-d8b7ba51f149 | -7.767 | -44.7543 | 2026-08-26 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a7c1b831-b6bb-32a2-9a27-5a1aaf5a803c | -10.7787 | -54.0163 | 2026-08-26 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 803843aa-0d83-39c6-943c-6c54740d2a04 | 1.4734 | -55.9642 | 2026-08-26 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e7f3cb39-3bf5-3523-b679-1e24506a2449 | -13.2451 | -51.5016 | 2026-08-26 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6641fd89-5097-3e94-8794-adb543337f9b | -12.7797 | -44.2576 | 2026-08-26 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 38d84e9a-90b4-3016-a9ba-215360c4a02a | -13.2835 | -51.4968 | 2026-08-26 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 8c5cb556-315e-37a2-a3ed-211abfc16da3 | -11.4302 | -44.5382 | 2026-08-26 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a9ca1015-698c-318c-b177-322ff7419757 | -10.76 | -53.9974 | 2026-08-26 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1a6558b1-c6ce-3ed1-9aba-db427ec86ae5 | 1.4917 | -55.964 | 2026-08-26 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ed36456c-b060-3afb-b6e6-bf1f3d83e1fe | -6.6225 | -58.5189 | 2026-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f5adf6d0-f67c-38ca-aa6a-e08b5fe02a72 | 1.4917 | -55.9837 | 2026-08-26 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a9578ca5-c0b2-3871-8de0-61c26947a2ae | -6.6595 | -58.498 | 2026-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| eda6c9aa-5d37-3003-9e0b-7d77a9034dd0 | -13.2839 | -51.4755 | 2026-08-26 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| afb13bba-f41f-308d-8cd4-b329e76ea808 | -12.7603 | -44.2608 | 2026-08-26 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 28a796ac-e231-3a20-89ae-afaba295134d | -7.5289 | -61.3825 | 2026-08-26 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8a415340-954d-30e7-bf8a-e8e365960359 | -10.7596 | -54.0384 | 2026-08-26 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 337.2 |
| 20a54fdd-c2f3-3bbf-bfec-0124d85e0b49 | -10.7598 | -54.0179 | 2026-08-26 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 293.9 |
| 9a9b6dcc-13b9-3bc8-8265-c5fef1c5e68c | -7.5104 | -61.3832 | 2026-08-26 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 8ac9c71c-89cf-33b0-b539-88220d5c0be1 | -6.641 | -58.4987 | 2026-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| c95af5f9-e019-3c59-9e4d-8228939d0d20 | -6.6226 | -58.4995 | 2026-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 431e1d14-2042-3982-b808-5d310d2f0e2b | -6.1286 | -57.8198 | 2026-08-26 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6b1077b0-9cc2-3d56-aa2b-d5413b2983e2 | -9.6212 | -55.1064 | 2026-08-26 00:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c9f5b2a0-dc48-3172-8cbc-59e4bd7fa0a1 | -10.3723 | -45.0767 | 2026-08-26 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c524856e-b8fa-3abc-bf70-1a8931914862 | -7.3034 | -49.5414 | 2026-08-26 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b6846de3-48a3-34a9-8890-a2d18ad7e45f | -10.7784 | -54.0368 | 2026-08-26 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 275.6 |
| e88d5b78-29ce-3ec0-9315-1e0a606b6d01 | -2.5042 | -48.1366 | 2026-08-26 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c70ff10b-2d02-3e30-8443-5551b6386a63 | -10.3727 | -45.0537 | 2026-08-26 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 01b923ba-47ef-3060-9c3a-bc5a5b431eda | -7.2856 | -44.0875 | 2026-08-26 00:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 15fae416-cc5f-37ef-8a6f-280cef69a04a | -13.2448 | -51.5229 | 2026-08-26 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 33060fc6-a432-3ce8-874b-2cc26b551605 | 1.4918 | -55.9443 | 2026-08-26 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 1fae5d06-69d2-3d80-9bf7-82e83b00745e | -10.3914 | -45.0742 | 2026-08-26 00:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d8e7b018-221c-3a62-884b-380a6d3df85f | -7.7481 | -44.7561 | 2026-08-26 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 82fdedfa-25c4-32df-9d7b-35ac8eb40fce | -6.6409 | -58.5181 | 2026-08-26 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| b19d1fb6-fa42-3d0a-a6b5-ebd211da35b6 | -10.9848 | -51.1655 | 2026-08-26 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 72ce4236-8e64-3c0b-a255-0575a591eff1 | -6.2491 | -53.3778 | 2026-08-26 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 2394f862-2ba6-3937-87d5-7b84a7ffa223 | -6.641 | -58.4987 | 2026-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 990ccf91-aabf-301a-b2be-c36ff6c0cb49 | -10.9845 | -51.1867 | 2026-08-26 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| dc0f2d0f-318f-383f-887c-39d5e58d77ae | -12.7797 | -44.2576 | 2026-08-26 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 85721015-6fba-32ff-80d6-785bd81e5b23 | -6.6409 | -58.5181 | 2026-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 54d51d01-cb03-3bdc-826b-74c5d59af76e | -10.7596 | -54.0384 | 2026-08-26 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 318.3 |
| d7244730-72a6-3989-812d-f9704dbcad94 | -7.3034 | -49.5414 | 2026-08-26 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 572c8856-7a16-3196-adcd-fc9fed0501aa | -7.2856 | -44.0875 | 2026-08-26 00:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e49e9c46-06aa-3457-9bc8-2ae5fcf7e5bb | -13.2256 | -51.5253 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 52058861-481c-32b9-98e3-639ecb16ccad | -10.3918 | -45.0512 | 2026-08-26 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d1f55957-de36-346b-822c-ce5903bd940a | -2.5042 | -48.1366 | 2026-08-26 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6a4fd294-ae24-3ef9-804f-0877f1f338e8 | 1.4734 | -55.9642 | 2026-08-26 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 32de9c95-f4bd-35fa-99d1-bd61ff5508c7 | -7.767 | -44.7543 | 2026-08-26 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 84b76b4b-f343-3e3e-b2d9-b84b4149f399 | -7.5104 | -61.3832 | 2026-08-26 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 267f4951-7453-30c1-a151-cc09b876aea2 | -10.3914 | -45.0742 | 2026-08-26 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1679f974-5076-3454-a60e-26c3683ed0e5 | 1.4918 | -55.9443 | 2026-08-26 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 60cd9d3d-2067-38d1-b7d4-374b93f3556c | -6.6225 | -58.5189 | 2026-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 9e6a6624-c5cf-3d67-b47b-23c32c7805de | -7.7481 | -44.7561 | 2026-08-26 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 36fa0387-1bdc-37aa-9bae-bc54ab9549dd | -10.7787 | -54.0163 | 2026-08-26 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 44018303-89c5-335b-a8ca-2be0a69895b9 | -9.6024 | -55.1078 | 2026-08-26 00:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 682c76a1-71dc-3c12-a81d-712346a66d72 | -11.4302 | -44.5382 | 2026-08-26 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 66489260-e8d3-35c0-ae7e-bd39203c1d74 | -13.2277 | -51.3973 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c760fc1d-e527-3c7b-b536-4443606941f3 | -6.1286 | -57.8198 | 2026-08-26 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| da950a79-f13f-39a5-a62f-f4a0f02e8e0b | 2.58 | -60.6973 | 2026-08-26 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ac3742ee-71b9-3ddc-a5e9-59415c331ed7 | -6.2677 | -53.3565 | 2026-08-26 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c74f8c4d-631f-35b6-bb34-553691f5fc02 | -6.6226 | -58.4995 | 2026-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| f69a5dbc-0014-3aec-b3bb-2c68a25e0714 | -13.2448 | -51.5229 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| cf0e27a1-2d21-387a-b5f1-c69a04a6c973 | -10.3723 | -45.0767 | 2026-08-26 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ad05eea7-dbbc-3522-9c51-77c0545c2802 | -7.5289 | -61.3825 | 2026-08-26 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c90a36bf-7948-375a-8fa0-4f215e5487e0 | -6.2676 | -53.3768 | 2026-08-26 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2166395b-421d-3b6e-9f22-c5313e3f11d2 | 2.5983 | -60.697 | 2026-08-26 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3e79b9c0-25fb-3863-80b8-4bace2ac6ac3 | -6.2861 | -53.3758 | 2026-08-26 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 3b9b0779-673d-3174-894d-6973ca311cef | -8.8184 | -62.3379 | 2026-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| c9b12841-2fea-3294-9a08-07a7cdb01a83 | -13.2835 | -51.4968 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 21b945ef-aa57-38d7-81cf-326c4cca5395 | -12.7603 | -44.2608 | 2026-08-26 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| ca904be3-ac4d-38b3-b021-d95ec55285c9 | -10.3727 | -45.0537 | 2026-08-26 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 033474fb-14ef-31f1-b56d-3b5afef511e9 | -10.7598 | -54.0179 | 2026-08-26 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 260.0 |
| a458b0c3-8dc2-3a33-8e4b-93b075e67d8e | -6.6595 | -58.498 | 2026-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b2a7c053-9ea9-30ec-80c2-f1763289c6a9 | 1.4917 | -55.964 | 2026-08-26 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d494ffb1-7e9a-3d07-b92e-c4470ae7162a | -13.2259 | -51.504 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b3b11e3e-5754-34bb-8625-0be3ff411e22 | -10.7784 | -54.0368 | 2026-08-26 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 232.6 |
| 0f464452-ca65-3c74-bc34-79713e2e635a | -13.2451 | -51.5016 | 2026-08-26 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1aea7722-4083-3afb-ba90-ec8748a10c85 | -10.9845 | -51.1867 | 2026-08-26 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 474ac7e1-2ad1-34e9-b336-d07b8a37abed | -15.6936 | -53.893 | 2026-08-26 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3fcebfab-72f7-3844-9072-cbab889a1e58 | -6.1286 | -57.8198 | 2026-08-26 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ca556489-f2bf-3335-8b33-fb9ca6fc9ab6 | -10.3914 | -45.0742 | 2026-08-26 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 169637f6-66ae-3054-a0bd-9a4cb1ff0324 | -6.6409 | -58.5181 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 72296d18-bf90-3daa-aab0-a6086bda6cd1 | -13.2277 | -51.3973 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 863ae7c5-0d19-3a1f-b5b8-0473a7c89479 | -9.6022 | -55.128 | 2026-08-26 01:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 93e06d59-69a8-32fd-924c-e77b6f43dbe4 | -6.2677 | -53.3565 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6b54c7a0-7dc9-3571-9c73-56bc34e7f7e6 | -10.3723 | -45.0767 | 2026-08-26 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f6cfa5c5-eece-3f23-b78e-9f0159fbcd62 | 2.2333 | -60.7018 | 2026-08-26 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9fcc4d09-6de9-35f6-a37b-e1ca441cbbdd | -13.2273 | -51.4186 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 366f2a65-e0e1-302f-9b2a-9e2f100c6e8c | -7.767 | -44.7543 | 2026-08-26 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 60a0fc6d-459e-345b-ba75-d9efe8db4bb9 | -6.6594 | -58.5174 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6cf0a4a5-f89a-34d3-9da5-367c73393fd1 | 1.4917 | -55.964 | 2026-08-26 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b46ca20a-b783-3c9b-9ffd-f5cb3bc8ce38 | -10.3918 | -45.0512 | 2026-08-26 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 430b4753-c059-3c27-9550-5ad04fd3ce07 | -10.7598 | -54.0179 | 2026-08-26 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 240.1 |
| 40c45d8d-36db-3b95-8840-d40f5c3ccd67 | -13.228 | -51.3759 | 2026-08-26 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f20bbc94-ab31-3723-9565-3a80bcf7f45a | -6.6595 | -58.498 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9ccfdf18-5c71-3b58-a011-1707c8a9d348 | -10.7787 | -54.0163 | 2026-08-26 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 7b4428e6-45d3-39fd-bda4-eee38b4ead5b | -10.9848 | -51.1655 | 2026-08-26 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b040edef-08f7-3cbc-8db6-f3f5279c93e5 | -6.2861 | -53.3758 | 2026-08-26 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 97730f62-0d0c-3dea-b187-5ac876fd05a1 | -6.641 | -58.4987 | 2026-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| e4393ee9-f4df-30b4-b5a4-83faec41c104 | -2.5042 | -48.1366 | 2026-08-26 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |


[Clique aqui para ver as próximas entradas](README4.md)
