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
| 6097cbd6-ee63-3d85-8e81-a0347ef59d57 | -7.9175 | -61.2718 | 2024-09-27 00:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 8ed9e90d-e1cc-3200-bfc1-d3a54085aae3 | -7.9359 | -61.2901 | 2024-09-27 00:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e9290ef0-72a4-399c-8503-4e907e6a05bd | -7.936 | -61.271 | 2024-09-27 00:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0355cc14-499d-3627-b2aa-27c953acdb73 | -8.3004 | -41.4477 | 2024-09-27 00:15:53 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| fa958ba9-79a1-3491-bb06-3e51b68cbd4b | -8.3008 | -41.4234 | 2024-09-27 00:15:53 | GOES-16 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 1b8ff898-90a5-39e7-ae1f-7fd7f9b22239 | -8.3153 | -55.0157 | 2024-09-27 00:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 93f19a03-9bcc-3bf5-9d3c-1858ac070fc2 | -8.3155 | -54.9956 | 2024-09-27 00:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 182b8b58-bfb4-3e5b-aecf-de92cb15b204 | -8.556 | -49.6112 | 2024-09-27 00:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| aa1874ec-6e98-3a33-af20-2377492d8b31 | -8.5562 | -49.5897 | 2024-09-27 00:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 081f0b5f-047b-3b51-a558-791269faa3be | -8.5748 | -49.6095 | 2024-09-27 00:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 06c4ebd7-fca6-3640-b6ab-fa9d6db7382c | -8.61 | -63.1415 | 2024-09-27 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5f3abb83-f0a0-3540-a319-7c581525dd56 | -8.6101 | -63.1226 | 2024-09-27 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 100.5 |
| eabbca0f-355e-3861-ac79-1c6eb42a1e21 | -8.6285 | -63.1408 | 2024-09-27 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 329c7305-feb4-3e6d-826f-cc5b60302d2b | -8.6286 | -63.1219 | 2024-09-27 00:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| e6df2770-75ba-3d74-b33c-b2f5d9c994a3 | -8.6661 | -67.0287 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| be40e210-2151-3b3d-be73-67951ca72526 | -8.6847 | -66.9911 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e67bad44-8c7b-30ff-bfbd-8d7d523f6787 | -8.7032 | -66.9907 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 80d2164a-cd75-3656-bc63-da65f3a931f0 | -8.7033 | -66.9721 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 02903b62-c47d-3c75-af64-ffa7f7b69571 | -8.7034 | -66.9536 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| fc7894e9-f204-3f2f-81c9-ff23ecc2d66e | -8.7218 | -66.9716 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e12dfd11-483b-3094-b48f-e22417a1adfb | -8.7219 | -66.9531 | 2024-09-27 00:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0bcdf603-8bd6-36e3-b5e5-4d3df0d0db93 | -8.8774 | -70.6005 | 2024-09-27 00:15:57 | GOES-16 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6e9c01a5-b668-3dec-a43a-590ee82ba9cb | -9.047 | -61.3943 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 7023bbe4-caa4-3030-a4a0-80e5b3e4926f | -9.0472 | -61.3752 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b62b555f-62b6-3948-bfbe-e2235864c45d | -9.0656 | -61.3934 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 7b40f6ec-5d79-3ca5-8b5f-7d08cf9f41d8 | -9.0657 | -61.3743 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| e4804451-d3c5-3a31-a6bf-81db78eca71f | -9.086 | -61.1245 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a32e5c80-214d-345c-9b04-bc0a71950f35 | -9.1046 | -61.1237 | 2024-09-27 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f52ee544-614b-30b6-899a-93bcc629ae29 | -9.107 | -67.8881 | 2024-09-27 00:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9c56067e-c4bf-3288-b425-bbb75cc19843 | -9.1255 | -67.8877 | 2024-09-27 00:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b87a6b2b-19fd-33bd-bef2-2e97f10b9138 | -9.3028 | -65.3528 | 2024-09-27 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| ed628e40-df62-3054-82bf-e60de4e051fd | -9.3029 | -65.3341 | 2024-09-27 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fa36471f-a98b-3555-8485-b8f9ac9783c8 | -9.417 | -51.4426 | 2024-09-27 00:16:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0cc6021a-83f7-34aa-b038-983642af17fd | -9.3214 | -65.3522 | 2024-09-27 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| bd64f428-e625-3a97-bb8f-0359a9a50ebd | -9.3215 | -65.3335 | 2024-09-27 00:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cc503bc5-e2ac-3ff4-bc8a-f4f903727d58 | -9.3763 | -65.5 | 2024-09-27 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cbcd7fa3-a38b-3c9a-b03a-f592d6de763a | -9.6018 | -50.1352 | 2024-09-27 00:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 59318f83-3c51-368b-958d-82be234ac8d8 | -10.0139 | -53.4464 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9235fae1-bde5-31af-b88f-0761ce88856a | -10.0322 | -53.4859 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| cfcb15ea-1f9a-3724-aebf-7219cb046872 | -10.0324 | -53.4654 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 07b80f9f-9328-335b-91fe-38f99d22951d | -10.0327 | -53.4448 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 7aea7557-2daf-30f4-a6e2-170bd4583150 | -10.0513 | -53.4638 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f7168f00-a9ec-3fad-81b7-91fb8474d370 | -10.0515 | -53.4432 | 2024-09-27 00:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 78323f9c-1667-31a1-bceb-5eae14fa0786 | -10.3672 | -53.7858 | 2024-09-27 00:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 96cb6312-10be-3902-8bb8-14d8e12df98d | -10.6434 | -45.9772 | 2024-09-27 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 39b79b32-3d4d-3a12-a13e-d0df4427ae09 | -10.6438 | -45.9544 | 2024-09-27 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 7d21dc1b-f2b9-3d1a-b23b-2276f1fc7035 | -10.6452 | -45.8635 | 2024-09-27 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 314a6df1-a6a6-3a7f-b258-299287ebfddc | -10.6629 | -45.952 | 2024-09-27 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 23530967-cca0-3d17-bb8d-828884a65956 | -10.6643 | -45.861 | 2024-09-27 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 9065dce1-b49b-3eb2-8e7d-407c97b929db | -10.461 | -50.7529 | 2024-09-27 00:16:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 11e3b6f9-a668-3755-bf98-86c6eecf0af7 | -10.4797 | -50.7723 | 2024-09-27 00:16:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 424013c9-ddf0-3409-9a51-ee457d5774c4 | -10.4799 | -50.751 | 2024-09-27 00:16:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 182.2 |
| b6ac622b-49dc-3458-8fa1-12edd89dfd24 | -10.7056 | -64.1516 | 2024-09-27 00:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 30407c49-594b-3957-a6e6-d49c34e7b69a | -10.7057 | -64.1327 | 2024-09-27 00:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 10dc54fa-763e-3029-b19c-49869f0a1d0d | -10.8541 | -57.435 | 2024-09-27 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| a55241f9-b2a3-3bb6-bf23-c4500bd12450 | -10.8729 | -57.4336 | 2024-09-27 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| bf31fb32-bece-344e-8a7a-3f65de2a85bf | -10.8731 | -57.4137 | 2024-09-27 00:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 76170cd7-679e-34f5-8c00-a778b5ae55e8 | -10.9264 | -54.2692 | 2024-09-27 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 373.8 |
| eff25362-c8ce-3b0d-a98b-9a61d39abcad | -10.9267 | -54.2488 | 2024-09-27 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 403.7 |
| 25412b04-4bb1-35fa-b7e4-9e60860c5cfd | -10.9453 | -54.2676 | 2024-09-27 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 17f8275b-70ee-3cc0-85c3-6b978c552bea | -10.9456 | -54.2471 | 2024-09-27 00:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| f692e86e-b7b9-3db9-9564-41de5012dd0d | -11.2034 | -54.7752 | 2024-09-27 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 61c3a032-e403-3c78-9574-bbbac5612567 | -11.2036 | -54.7548 | 2024-09-27 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3a1fc32b-d5d1-3a89-b316-eb9fc6304212 | -11.222 | -54.7939 | 2024-09-27 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0bb6b150-25cc-3311-b216-731d0b65ccc0 | -11.2223 | -54.7735 | 2024-09-27 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| a41c26ff-a6ee-35bf-b87b-dfb9355e38d5 | -11.2412 | -54.7719 | 2024-09-27 00:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| abe35c6e-01df-337e-b06d-b4f079c6b8c0 | -11.2788 | -65.2793 | 2024-09-27 00:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3f7ff7f8-cb96-323a-a865-aabe42f9a7aa | -11.5872 | -63.9596 | 2024-09-27 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 83c9894b-cdba-3242-a906-6fafbe01a227 | -11.5874 | -63.9406 | 2024-09-27 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bc56e19a-6ce8-3d52-af58-4f0e4b7d1ace | -11.606 | -63.9587 | 2024-09-27 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a0242449-e42c-32f9-b484-9f9816cb451f | -11.6061 | -63.9397 | 2024-09-27 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e414339d-f520-3436-b2bf-2f24e791921a | -12.1538 | -40.8445 | 2024-09-27 00:16:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 8163bd0e-710e-3dab-b7dc-ebb8cb50a5b5 | -11.7541 | -64.2746 | 2024-09-27 00:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3ee72e21-20ca-3805-b87c-d0d5d2bf0a1e | -12.1859 | -50.8195 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| abb99a81-c80b-3912-bb63-d698cacf1874 | -12.1863 | -50.7981 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 335.0 |
| 895e67ba-5edf-3301-b61f-dc15527e0e82 | -12.1866 | -50.7767 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 165.8 |
| faa45010-fc50-3745-b5a6-8203f5903868 | -12.205 | -50.8173 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0c8c60aa-b1d7-38d6-983f-8216fb0f40ce | -12.2053 | -50.7959 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 71dc07bf-2717-32bf-8327-dc970cc8f4e4 | -12.2057 | -50.7745 | 2024-09-27 00:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 66eb64f9-003c-370f-9c9b-d65f9b7b401f | -12.8437 | -54.0422 | 2024-09-27 00:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 9a7a82a4-b508-3357-a5e1-e946969db89c | -12.844 | -54.0215 | 2024-09-27 00:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 09549e65-e3d5-33b6-ab2e-a984e371b4cf | -12.8628 | -54.0402 | 2024-09-27 00:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 199.0 |
| d2ee65e7-fead-3454-a1a1-320306d3414f | -12.8631 | -54.0195 | 2024-09-27 00:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| a4635085-cccb-3f4d-a3de-86d4333b84ec | -13.4413 | -44.0267 | 2024-09-27 00:16:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 571dea3f-c062-360c-8073-893a9d63e9cc | -13.4418 | -44.003 | 2024-09-27 00:16:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 98a5dcb7-53b5-3afc-9169-149a707b5be8 | -14.0521 | -57.927 | 2024-09-27 00:16:26 | GOES-16 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 44cf74cb-a004-321b-b465-7b23a7551d36 | -14.0524 | -57.907 | 2024-09-27 00:16:26 | GOES-16 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5228d2ef-01cf-3831-8f50-f34c8ed35a08 | -16.713 | -55.847 | 2024-09-27 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 6d21d16e-2b8a-377c-b7cc-7c2df7fe4a6a | -16.7133 | -55.8262 | 2024-09-27 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 54199ab3-1afa-3bbc-b148-6adc8618e4c0 | -16.7325 | -55.8445 | 2024-09-27 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| e0f4cff5-1880-31bb-991d-2eefeccc253e | -16.7329 | -55.8237 | 2024-09-27 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| eab789c8-1ed5-3ead-8884-82c875853caa | -17.0988 | -56.1919 | 2024-09-27 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 8dbba1d0-117a-38b9-9941-dfadb341c3e8 | -17.1184 | -56.1894 | 2024-09-27 00:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 438d58ce-3da8-3559-9750-15433049ece7 | -19.6136 | -42.8159 | 2024-09-27 00:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 220beead-7ddf-3161-bfc4-dc738d21d692 | -19.5266 | -47.8952 | 2024-09-27 00:16:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1a3636ce-191b-394c-815e-c4fd49cb470d | -19.5272 | -47.872 | 2024-09-27 00:16:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 94.4 |
| bfdd90b6-abdb-3140-adeb-39b24f65cf81 | -22.7442 | -44.7785 | 2024-09-27 00:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 127692ef-34c3-3068-a37c-8df8069674a1 | -23.5816 | -47.3408 | 2024-09-27 00:17:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.1 |
| b33b389e-4ca0-3fe8-95eb-ff1af921c6d0 | -1.7494 | -55.2495 | 2024-09-27 00:25:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a39b6102-a27a-3c47-8735-66d2a9d9737a | -1.7494 | -55.2297 | 2024-09-27 00:25:16 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |


[Clique aqui para ver as próximas entradas](README4.md)
