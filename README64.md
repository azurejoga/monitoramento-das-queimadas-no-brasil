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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b238722-f5a2-35fe-bcf2-a6762ef517cc | -6.60977 | -58.38646 | 2026-08-23 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65dc5870-57b1-3654-89e5-46db51abcf5b | -7.55224 | -61.18456 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55aa272d-a397-372c-a59d-0e1b857206d2 | -8.89633 | -60.5478 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e91eafe2-0ad7-3418-ab37-ec170df674c2 | -9.08239 | -65.41217 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c02a6a-b43d-343c-9b31-f35511d14f3b | -6.6895 | -58.74239 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28f60494-24d5-3265-99fe-4b60ad043fc6 | -6.8071 | -58.66632 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75479a33-1f5d-37d3-b7e1-29b68eb32493 | -6.65594 | -58.8003 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be31b504-6967-3071-bc15-93acdb6ed6d5 | -6.973 | -59.05976 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96d60b5b-dfe8-38c5-bf7a-0ac63f55071a | -6.80166 | -59.66224 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e159359d-af6b-335c-a9dc-ce3a02c57ac3 | -8.40733 | -63.80111 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb49a77e-49f2-3d76-8078-5f810816d41f | -8.521 | -55.3258 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7c7c2eb-ad6f-3fb2-8844-3877e85f4734 | -6.6899 | -58.73945 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea1e06eb-2b7c-3ef7-a417-c8315858e3d0 | -6.80131 | -59.41906 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7325e4fb-181e-3880-9099-6dca3d8f53c5 | -7.78048 | -61.43448 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defa155b-687c-3fdf-96f7-ad377cca5db2 | -6.68182 | -58.72329 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0656f8dc-a336-3cbd-b632-2e486fe3aa0f | -6.80916 | -58.65128 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61635007-3cf4-3a27-bdf0-9ff1f7788d54 | -6.80834 | -58.65728 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 77fc0165-e256-339f-9bbb-c20cc69c1af9 | -6.97146 | -59.07095 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 92dbb722-9138-3b27-92eb-4a3104130144 | -7.66338 | -63.33765 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9bde636-c5a7-393c-b927-fcad6e9fe796 | -10.0674 | -60.50696 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f542aa9-f75d-33bd-9b5d-a31801f7045d | -6.75959 | -58.68363 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df29b511-d089-3d9b-ae15-8f2aae1c0116 | -6.7991 | -59.4351 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13688feb-7707-3a5f-83d2-8b94b822f691 | -8.52542 | -55.34317 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ad903a65-e685-3017-8db5-73dd4d9d048b | -6.81444 | -59.67451 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 062bf77c-5bb7-33a3-acdb-ace0a804eff4 | -7.78106 | -61.43044 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91b3110c-035e-3d66-a95f-41f96220ca13 | -8.53959 | -54.84318 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c44e6732-fd42-37d3-8901-07b2506fb87f | -6.77832 | -59.44608 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 850db5f7-3f27-3a19-a737-37ad9188fa3c | -8.53433 | -54.83056 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44d2089a-2044-3eda-8ac2-b388becfac87 | -6.65053 | -58.80245 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23968794-d05a-3aff-b4ba-49a6b32ba4e5 | -9.59461 | -60.50478 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa1eebcb-3134-3353-bfef-f0cd595460d5 | -7.48779 | -55.32782 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f40fcc78-e5b9-3568-956d-adaa17743010 | -6.70746 | -58.72416 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e908370c-2a02-353e-910c-e0af7639268e | -6.78949 | -59.43349 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f8e501a-a551-38f0-99db-d71bb8e8f635 | -9.17917 | -58.33487 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e37e068-c0cf-36f3-ab60-87698e853f57 | -6.77466 | -59.75168 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f158f247-d353-349a-b8d5-5bbecaa2b078 | -7.10874 | -59.77381 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b607620d-15dc-3357-83c0-c8d60739d14c | -9.40987 | -65.94086 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cfa25bb-df39-350f-b6e0-354ee97bc0c6 | -6.80326 | -58.6565 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2682568a-1fb0-3855-8114-295528cd460a | -7.57088 | -61.20837 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b9eb135-1ee2-3f77-977b-2f38c65f85d7 | -6.54711 | -58.52002 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b23a26-cb3a-309d-9909-7e45ae7e9154 | -7.78165 | -61.42643 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50010108-c2c5-34a7-9646-ef78e5d115dd | -7.6131 | -60.9754 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d586e692-2c00-3c5c-ba95-2c2d14b05749 | -6.83972 | -59.95384 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74053620-3ced-3b5a-a7b4-55954b0b289a | -8.52977 | -54.81191 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb1fbc5b-81d7-3a2b-8ed6-599ab58f5965 | -6.76466 | -58.68437 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91dc739c-424f-3a9f-815c-f56b7e9dd94f | -7.57263 | -61.19609 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b2b2b56-c278-3dde-b9ea-f4aa93b89c94 | -6.70283 | -58.72037 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9594a4f-1b7e-3afa-a4e4-7fcccdffa3d3 | -6.75072 | -58.67318 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ca88e4-de3c-35cd-bba4-3f21b55707ca | -8.53156 | -54.85386 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f952388d-d0d8-39c5-bf3f-4c5bcefe372d | -6.97565 | -59.07722 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e015641-a4c1-38d2-87d8-c26a557e90e8 | -9.17334 | -59.45474 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6025f02d-e42e-3cb9-b591-fcc458841388 | -6.80947 | -58.98196 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e45cc76b-912e-3fcd-acb8-246d1128c486 | -9.07095 | -60.43618 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad60f435-37aa-3438-b94c-231aa34c2cb9 | -6.76043 | -58.67774 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a11a82-6560-330b-a8d9-b9ce36c0cac6 | -6.69191 | -58.72483 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f622a451-3667-31e2-91b4-903b78f76670 | -9.16761 | -59.45975 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d759045-9b0d-3f97-b7f5-ef6c7efc857b | -8.70875 | -62.90035 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2a8a5c1-1c1d-39ce-bda2-a37b52f3426d | -6.68686 | -58.72405 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47837af4-e392-307a-915c-7de2292625e9 | -6.80495 | -59.67318 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18bcec03-56f1-37d8-8178-7cf22048694e | -6.80244 | -58.66252 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db47ad97-389c-3d51-add4-794c1c61aeed | -6.95585 | -59.07432 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9ec8832-cf91-397b-9d6a-09c9278017a8 | -6.95014 | -59.07916 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 31d298ec-6a01-3793-9aa3-ae04e969ed2b | -9.40064 | -60.55788 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e09c8066-76b3-31c4-9ed6-f6f7de172301 | -9.13107 | -65.95171 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a2b0154-7f94-32b5-97ee-bf6829fbd2c0 | -7.65518 | -63.3411 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08eafaea-778c-3e9c-ba5d-a115bfb1fb1c | -6.86524 | -59.02622 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b723c3b6-57f0-3cf1-8fa0-f84f7500123b | -7.43761 | -59.80014 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca29d4b4-656a-3028-8f68-4a3bd0a6c310 | -6.8344 | -59.95801 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c29e901-a489-3eb1-aa2b-7519b64918c0 | -6.70662 | -58.73021 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e08caf8-4eda-34c8-81a2-01c6f557a940 | -6.78556 | -58.67242 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba51c34-0eb0-3136-b2ca-53b7e4e81b30 | -7.77983 | -61.06886 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 406cac75-562c-304f-a363-8d2436c40453 | -9.21911 | -59.76936 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd8fe57e-6e5a-395b-8d97-2ae8bb431423 | -6.82132 | -59.41668 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb7dd6cf-74ce-30f3-928a-21e344acfae6 | -9.04854 | -65.44987 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a9065b-51d4-386e-8913-f6ad7c54bfe0 | -6.86369 | -59.03753 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15a7d079-6ec4-3588-993b-7a8544d4fec2 | -6.803 | -58.62029 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83dcf53e-9fce-3334-8def-a89bab36e6af | -6.68062 | -58.73209 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 253be323-4992-3fe4-911f-59736ce93a7a | -6.69695 | -58.72563 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8faf06d0-e9f4-3ca5-bcd1-338a43fdebc3 | -9.45274 | -56.90688 | 2026-08-23 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64f8490a-15de-32fb-88a5-4711c6d0de7a | -8.92298 | -60.72915 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36eefa28-e8df-39a7-b98f-7dbf56dba019 | -8.5417 | -54.82551 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a74fce9-9587-3ca7-808a-21b2cdc1d08b | -6.76592 | -58.6755 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18f49882-8ca4-309a-89fc-5e85359be500 | -9.50687 | -60.49949 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be23dfed-9567-37a7-b4ad-d46a7ebbbd0f | -6.65056 | -58.80261 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1e1f76-a899-356e-9a54-b0ed567d1967 | -8.54099 | -54.83141 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd34fcad-c62b-3266-aabb-4092e2a28fd3 | -6.95433 | -59.08545 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1758061c-762c-3cb4-a8f2-db3fda7f1485 | -6.9608 | -59.07502 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2ae6b124-3f13-3384-8fbe-c8f1b4234130 | -6.67597 | -58.72839 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbc33322-85e7-35a2-98db-d4bf2114cd86 | -6.69252 | -58.94202 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 746aa4c3-8a04-31f3-b475-e50860cbb539 | -6.67314 | -58.7492 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d8c76b2-6376-3653-a844-e239f7aa5994 | -8.51894 | -55.34252 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 668d6db4-60ec-3949-9593-1d6a65bfbae4 | -6.79709 | -58.62553 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dd940c3-c4f0-3530-a832-295a3937b45c | -7.8515 | -56.57235 | 2026-08-23 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f22ab96-db2b-34b9-b907-85e5c45cbaf8 | -6.76407 | -58.67834 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39753f3d-d707-3878-bb7f-e29f31d33fac | -7.60359 | -60.94791 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 558df1b5-a44c-36a6-9dea-d1c071697ef8 | -9.17503 | -70.89459 | 2026-08-23 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c57836-82da-3be1-8201-ae6a765b0e98 | -6.80052 | -62.9177 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9e777405-18cc-390b-8fc5-45477422a98f | -6.76001 | -58.68069 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ad6f34-76d9-3517-adaa-f6df904a93a9 | -6.76339 | -58.69331 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d1ecfe-2672-30aa-9570-2d1117d02626 | -7.56774 | -61.19952 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README65.md)
