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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66f46c22-cfa4-3ab7-9dc9-23e52168aecd | -7.3089 | -61.1053 | 2024-09-27 02:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ea38b6a8-46bf-325c-b062-619a6f5fd27f | -7.2906 | -61.0869 | 2024-09-27 02:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2c33c0ba-16ad-3ba1-b782-80bd5368bcb1 | -7.2905 | -61.106 | 2024-09-27 02:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7608e9fa-1761-3db6-983e-efe3f4521050 | -7.5289 | -61.3825 | 2024-09-27 02:25:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f9f320b2-cbc6-3c5e-9fbc-250cba0d645a | -7.5887 | -60.5976 | 2024-09-27 02:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d9406686-64c6-3233-9363-fc8c40b57cab | -7.7886 | -61.1817 | 2024-09-27 02:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 4e39f377-f2d1-341b-94ce-045a0b72d8b2 | -7.7885 | -61.2008 | 2024-09-27 02:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 8c12874f-25e0-38fd-9d79-64410aba4241 | -7.8156 | -54.7252 | 2024-09-27 02:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 6e308600-2d54-3f8f-ac57-8aa04aab3630 | -7.7701 | -61.1825 | 2024-09-27 02:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 7bb99a14-c356-3c35-9fec-62c3f128c35b | -7.77 | -61.2015 | 2024-09-27 02:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 2c4c3b28-06bc-3613-893a-570acbebe842 | -7.936 | -61.271 | 2024-09-27 02:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 81d3007b-929b-3610-8e0f-4e23c157f750 | -7.9359 | -61.2901 | 2024-09-27 02:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4f0ec6cb-3c5b-35c6-b671-76b270e1d9bc | -7.9175 | -61.2718 | 2024-09-27 02:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 39aca8d7-cf83-345b-ac32-6af716759f5f | -7.9174 | -61.2909 | 2024-09-27 02:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bcf46c4d-6ebe-3474-9612-5134ba42e813 | -8.1579 | -61.2809 | 2024-09-27 02:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| dfdb25e7-1548-34ab-92c8-5ace5d213abc | -8.1394 | -61.2817 | 2024-09-27 02:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 819523a1-b98c-3cad-8e2c-c58c728c842b | -8.1393 | -61.3007 | 2024-09-27 02:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f23627fe-0ff6-30e0-9f2a-13acea205154 | -8.556 | -49.6112 | 2024-09-27 02:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e715bd4c-5bf5-3a05-adbd-367c1be0b4ea | -8.7219 | -66.9531 | 2024-09-27 02:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 230271dd-f0ba-378e-8ea5-527a729c10bc | -8.7218 | -66.9716 | 2024-09-27 02:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 05f7751e-8406-347d-b0da-6af883c9ce6a | -8.8117 | -67.6732 | 2024-09-27 02:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 0a610bd1-d5ec-3294-88d7-e6a0d71d3072 | -8.8116 | -67.6917 | 2024-09-27 02:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.0 |
| d67dbad1-459c-39b0-b22e-6ef15c8cb179 | -9.1032 | -61.3343 | 2024-09-27 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 70793e94-796e-3170-a6ba-90ac415fe2a7 | -9.103 | -61.3534 | 2024-09-27 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a5814aca-2069-3464-81e8-1c4a640fabd8 | -9.1029 | -61.3726 | 2024-09-27 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 16e819d6-c28c-3e36-bf1a-0b188f485150 | -9.086 | -61.1245 | 2024-09-27 02:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5cc02143-09d5-357d-9c76-34ecbb87e5c6 | -9.0163 | -67.3534 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 3a7cc018-687f-33dc-8e34-0898f5e55d73 | -9.0163 | -67.3719 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 145.7 |
| f1ee9961-950a-3d89-ada9-c079d663760f | -8.9978 | -67.3538 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 082939da-4525-3457-8821-1cadfc6f9792 | -8.9978 | -67.3724 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 353.0 |
| 215f1b49-c12d-33a3-ac91-808737ceb4fc | -8.9977 | -67.3909 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 729ebf2d-91bb-3e3c-933a-7153d653fd9d | -8.9793 | -67.3728 | 2024-09-27 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f531bad0-beae-3bc4-ad0a-26aadb96dd15 | -9.1217 | -61.3334 | 2024-09-27 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 43355de5-afb4-3dc9-a89a-43b7c8f88130 | -9.1216 | -61.3526 | 2024-09-27 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9aba2749-29d4-38fc-b08b-39a49a62a73e | -9.1215 | -61.3717 | 2024-09-27 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f4550308-8e9c-318a-8082-9c23727d81dd | -10.3672 | -53.7858 | 2024-09-27 02:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| c8036387-347b-30b7-8d62-46205be77cc4 | -10.6639 | -45.8838 | 2024-09-27 02:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2d02b8fe-e6da-344f-b638-6581f9317164 | -10.6452 | -45.8635 | 2024-09-27 02:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 06230326-b24e-3b69-b264-7e88ac5def9a | -10.6449 | -45.8862 | 2024-09-27 02:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 9b9f9136-a5af-3b3d-ab9a-253b93432b83 | -10.6643 | -45.861 | 2024-09-27 02:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9815cab9-a1af-3851-ad68-5aac8b320e82 | -10.7214 | -51.0657 | 2024-09-27 02:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 6186b3f1-e646-39a8-85ee-2603703f576e | -10.7211 | -51.0869 | 2024-09-27 02:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| e79e4f1a-a359-30ad-9f18-ac30ca763b5b | -10.7036 | -50.9828 | 2024-09-27 02:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b34839a8-eb55-3e8a-86a4-0e0b602eaaec | -10.6846 | -50.9847 | 2024-09-27 02:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 887a063c-cd94-36da-9442-ce89f3e0c4cf | -10.9456 | -54.2471 | 2024-09-27 02:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3f8e6fc6-2019-36c1-a44b-48d7303c8da7 | -10.9453 | -54.2676 | 2024-09-27 02:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 48430f24-f979-34f9-a1a9-65bcf3daa791 | -10.9267 | -54.2488 | 2024-09-27 02:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 205.4 |
| 465e4dee-3ed0-327d-8715-8941c704e2ab | -10.9264 | -54.2692 | 2024-09-27 02:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 5e3ebca8-a3f6-3b84-a5b7-f7c8920e3b5b | -11.2223 | -54.7735 | 2024-09-27 02:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 680a17a8-12ab-3f1d-aab1-8abd1546253a | -11.2034 | -54.7752 | 2024-09-27 02:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b0c71f7b-c7aa-3443-834f-e00d38914e74 | -11.6061 | -63.9397 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2a66eae7-482b-3ac9-b705-5daebd8e2e43 | -11.606 | -63.9587 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 43631495-f372-335a-88cb-f11e4ea9462b | -11.6059 | -63.9777 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0ad91324-c4b1-327a-b5dc-e5442bbe6e4b | -11.5874 | -63.9406 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 359a236c-4470-375b-9300-3da9192ea267 | -11.5872 | -63.9596 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 100.7 |
| df449cc9-d36d-3a3f-b3c2-33398cd9c304 | -11.5871 | -63.9786 | 2024-09-27 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 94964e13-1fef-3a7c-b866-3a41579608cd | -12.1672 | -50.8004 | 2024-09-27 02:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 164d53af-3c63-3a47-be79-68a5fe44b4df | -12.6826 | -54.6763 | 2024-09-27 02:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fd65c688-99cd-3e50-b65b-4e488febb777 | -12.6824 | -54.6968 | 2024-09-27 02:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 33d7291a-0de0-3fdb-b16a-cfe3ecd3d638 | -12.8634 | -53.9988 | 2024-09-27 02:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9bd6c5be-805a-3c9e-8357-6d13d535f824 | -12.8631 | -54.0195 | 2024-09-27 02:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 23655e84-95ff-3ebb-9317-0aa36ccef200 | -12.8628 | -54.0402 | 2024-09-27 02:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 38f593f8-ef18-3b7f-abbc-67d8593e6e2b | -12.844 | -54.0215 | 2024-09-27 02:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a494926d-4f00-32dc-b423-2c9f8f5e4392 | -13.7837 | -56.5023 | 2024-09-27 02:26:24 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ebbe6672-3388-3d6c-a0de-21969afd8a79 | -13.7834 | -56.5226 | 2024-09-27 02:26:24 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 44e3a5df-f12b-3cf2-bf48-b69795afb999 | -14.922 | -51.4507 | 2024-09-27 02:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9e699310-e4f9-3d9d-8bf5-efa3bcb802d7 | -14.9216 | -51.4722 | 2024-09-27 02:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 386653a5-8981-3a8c-88d0-047734296e25 | -16.8933 | -58.0213 | 2024-09-27 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 071afd1e-9c01-3d48-930c-f6974ae4e51c | -16.893 | -58.0417 | 2024-09-27 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 544d4ff3-48b0-383d-bcfd-3868a4dbf146 | -19.6342 | -42.8103 | 2024-09-27 02:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 7c9dd084-2c4c-3f61-a42e-039261a99e2c | -19.6136 | -42.8159 | 2024-09-27 02:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| b6733238-4675-3c15-a684-b26d084cdf25 | -21.0658 | -48.8428 | 2024-09-27 02:27:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.5 |
| 103f3cc2-cb01-3b02-8def-7d78304cced4 | -21.0665 | -48.8196 | 2024-09-27 02:27:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.0 |
| 82fc827b-3d9c-3e5d-992e-80e422e33f08 | -21.0871 | -48.8149 | 2024-09-27 02:27:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| 60ebe78a-e283-3477-b27e-5934c26c99ba | -21.0865 | -48.8381 | 2024-09-27 02:27:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.8 |
| 6415897f-6cc3-3ae2-a440-3bb00b8a567d | -22.7653 | -44.7723 | 2024-09-27 02:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.2 |
| 826f6641-7c11-31f7-80b8-b2a41c84ac05 | -22.7645 | -44.7973 | 2024-09-27 02:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 221.4 |
| c307786e-87b9-3941-af17-5fd8651da103 | -22.7442 | -44.7785 | 2024-09-27 02:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 177.0 |
| f1336f1b-8c13-3868-baaa-9b5bbbbb9c67 | -22.7433 | -44.8035 | 2024-09-27 02:27:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 343.2 |
| e47c2f2f-5b48-3496-a43d-eb474eb7dfa0 | -23.5816 | -47.3408 | 2024-09-27 02:27:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| e076a55e-ef90-35ed-99d1-377571b402d4 | -2.3579 | -47.6206 | 2024-09-27 02:35:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 010d8658-e7e3-3fd7-8569-b5d702b496b4 | -2.358 | -47.5989 | 2024-09-27 02:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 055edb4e-de93-308b-88a6-3d309a4e38ed | -2.6783 | -57.6087 | 2024-09-27 02:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 55a6eb25-1237-3969-967d-7d095231012c | -2.6783 | -57.5893 | 2024-09-27 02:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 92ad7dad-9d45-38ff-8e4a-029f8e9b019e | -2.8795 | -51.6695 | 2024-09-27 02:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| de50b078-72f5-3418-b400-1680d95dec08 | -2.9339 | -57.8562 | 2024-09-27 02:35:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 7f586276-2c31-3dfe-bf71-3617c54f7f86 | -3.0107 | -51.0652 | 2024-09-27 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 496762c4-6e27-30bb-9598-11be5ed531e7 | -3.0292 | -51.0647 | 2024-09-27 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 32a0ee4e-a807-3ae8-b2fc-a720e68d9845 | -3.2136 | -46.7843 | 2024-09-27 02:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 1b6b40b2-f9e3-3bdd-9067-2d16449532ca | -5.397 | -43.4332 | 2024-09-27 02:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d6f803a5-b1ec-39e7-8d64-2c9d99f2baa7 | -6.8927 | -59.6475 | 2024-09-27 02:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 00edd502-a980-34b4-b831-c0a2e70ca327 | -7.2905 | -61.106 | 2024-09-27 02:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d2e949c3-e932-3aca-936a-b17f789882c0 | -7.2906 | -61.0869 | 2024-09-27 02:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c0e0de63-5ef2-33f0-95b4-b358768a2e8c | -7.3089 | -61.1053 | 2024-09-27 02:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| be6e2710-597c-3476-aac4-f62ef707177a | -7.309 | -61.0862 | 2024-09-27 02:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9abbbc90-ae76-3ca9-b1de-92cce65e5438 | -7.5289 | -61.3825 | 2024-09-27 02:35:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c8724d58-8fc9-3769-9237-45cfa0fdb09c | -7.5887 | -60.5976 | 2024-09-27 02:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| bf5157e4-f7dc-361a-a7b4-9f118c3cfa0f | -7.77 | -61.2015 | 2024-09-27 02:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 85621be7-3192-36c2-921f-a85a05b2742f | -7.7701 | -61.1825 | 2024-09-27 02:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 43b29ab4-03bb-3880-955e-2e85c971b2d1 | -7.8156 | -54.7252 | 2024-09-27 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |


[Clique aqui para ver as próximas entradas](README43.md)
