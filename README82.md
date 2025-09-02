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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13b28fe1-477c-34b5-b464-4d0af3226639 | -7.48058 | -63.82344 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9051831-8e6e-32dc-8de0-364ec1b180b1 | -8.67055 | -62.85075 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f3a5866-4148-3266-b765-e3dd6e57a287 | -7.53411 | -63.84909 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3656419-3b0a-3cd2-a54a-5e7e0ce3b034 | -7.66435 | -61.10032 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a4ecfed-b947-31c5-83eb-d159de13614b | -9.46293 | -60.31433 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 005f4d16-e716-35bf-b21e-28d662bebcf4 | -8.65911 | -62.82868 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8fef33-2704-3866-ae95-c125d7424ffe | -8.68759 | -62.40729 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6702baa0-2978-3a38-bc36-0a245bd3b4d0 | -8.68373 | -62.4022 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba7730eb-d9da-3dec-b5d4-f76ac24f1e1e | -8.66346 | -62.8293 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16eb999c-8316-3cfd-a32c-74f79a62418a | -7.50754 | -63.49136 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd14648-f0ac-365c-8640-0ff89145af3c | -8.51449 | -63.91233 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e93b0f88-39ca-3fb0-8591-d1a6af9d4103 | -7.56231 | -63.07439 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2014aaf7-8d86-3a9f-9333-6947a8df6a9e | -8.6662 | -62.85011 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a10d1fb4-3605-39b1-b55d-c32222f68729 | -7.69896 | -61.09976 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b5f366b-25d5-34cc-9a45-10c436f8371d | -7.73346 | -67.0583 | 2025-09-02 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61a498c5-1a0c-33cf-8323-5c2531948e3e | -7.56244 | -63.07089 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fafb6567-5468-3dc1-bec9-84158dc7f9cd | -8.73179 | -62.41821 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0339174b-1ac3-3e70-8731-b508074a7897 | -7.08375 | -63.18485 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f093f18-cd9a-3631-b9c3-01ec2eb76190 | -8.6685 | -62.83331 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d116b75-45fa-393e-88d6-bc9494950473 | -6.15315 | -62.52307 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07638844-0c0f-3e54-bfa4-e45f33de3354 | -7.25388 | -57.54574 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8bcf571-cb4b-36c4-872e-e0120255241e | -6.98797 | -63.01572 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92d5b74a-c28b-3a04-bcd9-baa72b2bbc70 | -8.50976 | -63.91141 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc5cc9d4-3140-3a70-bcfc-d719741499e8 | -9.08781 | -58.89244 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0af63576-15b2-3755-b41c-34d04e839c90 | -6.92842 | -63.13198 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fa5f13a-1493-3db9-81b5-83dd455be753 | -8.66257 | -62.92707 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f563e5a7-b08f-3c5c-99ae-ed09ca08f7f1 | -7.44242 | -64.51616 | 2025-09-02 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d67f3377-fd21-3243-b5f7-66789fb8361a | -6.40437 | -58.21178 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0dd87e6f-f5f4-3eb4-9eb9-fc85d5e7c8e7 | -7.53915 | -63.84272 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eff040d8-8ca4-300a-ae5c-319f6b38eb3c | -6.3375 | -58.18082 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 716c2edf-1d97-30a2-8064-e6364360cbac | -8.42671 | -62.29444 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152f6c43-4cb3-32b4-819f-25eb00e910f7 | -7.7038 | -61.10043 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d003512-b074-3844-8f81-8b77ffa06bfe | -8.73772 | -62.42661 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b2636a1-1149-39c7-94f9-f12a642c5109 | -6.39878 | -58.20597 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13b6c47f-1aaf-3465-9fc5-70641c432293 | -8.65007 | -62.60926 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76825be3-328d-3bc7-acf3-222badee9124 | -9.08977 | -58.88747 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac0c383a-0daa-3953-99a6-62f392315d76 | -8.71003 | -62.41037 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb387f4a-bbb1-30cb-9e96-b53a206bacd1 | -8.72997 | -62.41637 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d7bb269-809e-320f-88af-a4621e156e58 | -9.46251 | -60.31758 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25180fc0-e44f-3043-859f-3df566939e4e | -8.6666 | -62.83832 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3b82667-0d83-345f-b7d6-80f8593b0703 | -7.53359 | -63.85257 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c365347f-1795-3b9c-bff0-65b5c203deb7 | -8.75055 | -62.43303 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f1923c9-bdec-307f-8775-919b67ec31b7 | -7.58651 | -61.62444 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 332eba6d-9085-3ec4-b570-eb7c2714f713 | -8.5138 | -63.91199 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b1a8ea7-5202-345f-a4bc-a1c1c7af306e | -7.67477 | -61.09635 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec06e341-f749-3914-b7f9-75dbcf697cda | -8.63558 | -62.61605 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c867cfb6-6c4a-3bf8-9cc3-3d901fd7ae46 | -8.6368 | -62.60736 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d884e11f-c4c3-36df-988e-7cc8a47e973b | -6.15257 | -62.5271 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fdec37d-85d9-37c1-8f0e-df20e72062df | -6.4034 | -58.21498 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a75f14b1-925c-359d-897f-e07afe0738a2 | -7.09101 | -63.13559 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87bc9966-a464-311a-92d0-a30de74ff7be | -8.7261 | -62.41116 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc9cd32d-682f-31a4-98e6-6d02d929c2f3 | -7.79023 | -61.56754 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 936867d7-b956-3a89-94f5-072d0af916a3 | -7.56519 | -63.84292 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abad6588-421e-360e-be31-6f7021b0624d | -6.40396 | -58.21099 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd8a78de-f236-389d-a163-1ff37139360d | -7.56119 | -63.84233 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 810f4680-075c-31ca-a971-6a7a2353c335 | -9.43877 | -60.5802 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f665de3e-ea96-31b3-a05a-ed9cbe82e227 | -8.73563 | -62.42332 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e4af3fa-5ff0-37f2-9084-2f5268ab438f | -8.66913 | -62.85152 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5033792f-3548-35e8-87de-b0d488b64eed | -8.73051 | -62.42712 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b50c2d79-680e-3691-bbec-1ce5600bc763 | -7.68035 | -61.09171 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f408f778-0c61-3261-8ef1-2190a527715a | -8.67476 | -62.4009 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc513b9-e65d-3e3c-8581-306869f78582 | -7.59446 | -61.63551 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1020d7d5-e4bd-31b3-824d-09b6ebe4ce20 | -7.53966 | -63.83924 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7cdec26-fb73-310e-9f32-edf8489925ee | -6.92426 | -63.13137 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1092232a-05c5-3a52-8f46-135f573b7ae0 | -8.70105 | -62.40917 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2799adf-eda6-3682-ad66-f23c820fd495 | -7.47607 | -63.82634 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ef4c562-830d-36bd-b551-8096924bff0c | -9.27076 | -59.75032 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82bcf2cd-3506-3338-94c9-adb9f3dc9897 | -7.5746 | -63.04831 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7861933a-540e-3ef1-9fcf-e96394e6b272 | -9.16366 | -58.90229 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f93d9d4e-a5c3-3e55-9932-3cdca3b947eb | -9.27028 | -59.75389 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 551a0cfb-23fd-34cd-8521-6c9669341f5f | -8.85776 | -64.23457 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 153618a9-62be-3a34-9f64-3a5282c3bd09 | -8.67924 | -62.40152 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23ae2dd6-74b1-3172-97b8-7baee302b69b | -6.33226 | -58.17597 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0aa5339-d452-3a1f-8c5a-946f4f21754d | -7.66026 | -61.09426 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f986805-e706-3c62-a26d-a7c76b01f63c | -8.73444 | -62.41709 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9df6ce92-7eaf-33b4-b8d7-fef2ba06b8af | -8.72936 | -62.42086 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ba7d741-b39c-35b9-b59c-273727dc4d49 | -7.70305 | -61.10576 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 729d1f3b-1925-3194-a194-336592c69f1c | -8.75503 | -62.43372 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 478d9abf-2bd6-3ad0-bb81-733ca7e61e01 | -8.67988 | -62.39701 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d36cd58d-4c82-39a6-83b8-ca5c8f7aac28 | -8.69207 | -62.40795 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f33270e-af43-3ef9-bb96-abbbe5325638 | -8.66454 | -62.92649 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d360ab3-2342-387e-bfd1-d61142060a62 | -8.75627 | -62.42469 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e37e3191-588c-3f5d-8783-51a515c31662 | -7.54726 | -61.34298 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| db2988d2-5517-3b90-98e5-a868dbc73b06 | -8.65261 | -67.24934 | 2025-09-02 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a0769b-9c83-31e6-9b50-0be52ce719ac | -8.66286 | -62.83351 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba8b1c06-5e02-3e43-a1ef-3e96cc1c59c6 | -7.47557 | -63.82983 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01065737-49b0-3800-9488-1386a20b7a20 | -7.36272 | -61.65343 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65595805-e512-3c6f-918e-061c53feae76 | -9.43917 | -60.57715 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e16d904-84a0-3aea-a1f5-e391df54bfd2 | -7.0879 | -63.18544 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f245128d-9718-3e28-aaa6-22924cdc9ef7 | -8.68435 | -62.39774 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd370d56-1682-3d5f-82cc-6c08cfd6c3d3 | -8.6927 | -62.40351 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07aaeaac-d0a4-3857-ba28-8707607e7f17 | -8.73499 | -62.42774 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a50762c-727f-3b86-9336-9eed85f8c8eb | -6.40454 | -58.20687 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6586570c-41e7-3522-8507-093e84fe375f | -7.54322 | -61.33725 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 428afc80-6a71-3ddf-92b0-122563f79151 | -7.45539 | -63.15818 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef819607-6fbe-38ad-844f-f7f881abf253 | -8.73893 | -62.41777 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79fa53e3-e124-3b1f-a948-f4390abca8da | -6.98854 | -63.01186 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee15ae51-5a53-3411-adf0-147a40d0d113 | -7.0843 | -63.18107 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd32867d-addc-3d51-9753-3546af9af7b5 | -6.75564 | -56.39447 | 2025-09-02 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 036eb9db-ccf3-3a98-895a-394ed091be32 | -6.33859 | -58.17278 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README83.md)
