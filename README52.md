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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0054d966-4642-3c1e-9245-51b49bed92f3 | -13.15372 | -54.91658 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 019121c4-2ba3-3da4-a2d9-37e2d1bff5e2 | -14.97353 | -54.80656 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 32be2451-7825-3c76-80c8-8c86db26e61f | -13.17466 | -54.95116 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf0037c-fc95-38a5-af0d-3b251f9fa0f7 | -13.1391 | -57.1623 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf7c015-3fe1-3a47-a2be-c134fb4df5a5 | -14.96788 | -54.80325 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cd500d0-aab2-35be-baac-a35bb0c16d24 | -12.97854 | -56.85783 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5477290a-4d39-3aff-b520-e20872e6394a | -13.16472 | -54.93005 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28b02e9f-98d4-3a14-8bf1-0dddcce3a312 | -14.86605 | -48.06792 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4982d991-84a8-3c1d-9165-b46cdfbb3687 | -12.99442 | -56.86715 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09fa7357-26bf-3966-8ee1-cf4ac9ed513c | -11.09105 | -58.94351 | 2025-08-19 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd58e589-ad0c-32ee-b8e4-a0ae631c6831 | -9.88759 | -64.2663 | 2025-08-19 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9927beb5-cf65-39d9-9708-a7cf0680f637 | -15.39965 | -49.13223 | 2025-08-19 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dac14cae-6e7c-3c98-b34c-1919e673a3f9 | -14.97973 | -54.8134 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3252236f-5ed9-309f-a7e6-9cecf4fcdbc8 | -12.97681 | -56.84377 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70f6d24f-3053-3ee0-a4e7-1e72399f4907 | -12.97985 | -56.84885 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a60e217-248d-3b2b-a9c9-7c2bbd1bafbf | -14.98516 | -54.80573 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d069abc-238d-38f5-a08d-ed61d51b5b7d | -13.01743 | -56.83836 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25945e78-17d1-372d-938f-9cbf4effc348 | -13.14954 | -54.91597 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e015114f-481f-34f6-b116-977d83fbdc8a | -13.59161 | -47.00109 | 2025-08-19 05:18:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08f55089-31da-36c2-a221-cef5047c2802 | -16.8122 | -49.36736 | 2025-08-19 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74fc06c2-d364-3e0f-8ecb-d4b59e654c85 | -11.74178 | -58.32394 | 2025-08-19 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 015e432b-4444-326f-864f-2b96360c04ac | -12.37517 | -54.16253 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92b85123-b4e6-3bf6-aa38-f83e0917b55d | -14.96523 | -54.78999 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56179f60-d291-318e-ab6e-37aeb1965cab | -14.64696 | -54.91081 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 493b41b8-ebfb-3dc8-9b70-305d546822c4 | -13.30176 | -50.82034 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ff90d87-0911-303a-9cfc-a22a8646a5a7 | -14.64372 | -54.91121 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9380aa25-e554-33e6-ad65-5fc44e735e73 | -13.17884 | -54.95175 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1fdcd9e-7aa5-3253-aab8-e2fc1f33bee5 | -10.92031 | -68.43491 | 2025-08-19 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c47bd2ab-6c6c-3e96-9f79-e4521723ea0d | -14.61861 | -54.90371 | 2025-08-19 05:18:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dd9a936-6f5c-3fa2-8b2b-baf6e5f3c203 | -13.17571 | -54.94337 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a7f6a77-2875-38a2-89d7-add14a4f3927 | -13.18719 | -54.95293 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4937634-0858-3680-8f24-07de268eb9fb | -11.8499 | -51.57428 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40dbc011-2374-3cb9-bf1a-158583795d72 | -13.2533 | -50.803 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34eaf12a-f8b3-3ab1-bf78-5543fa4e46fd | -13.00193 | -56.84076 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e5d5df4-3b17-38eb-806d-8d0d0ebd1a87 | -15.16087 | -48.78083 | 2025-08-19 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93f88d17-f518-3b90-ae86-2e39274ee41d | -13.15321 | -54.92043 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d495b51-87fc-3e7c-893d-a7736c3d4d36 | -11.85229 | -51.57961 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2362698e-5a03-356d-b3a6-b481f7f6ac75 | -9.51047 | -60.53294 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe546a0-ce40-38da-b857-536f778d4b7c | -11.85665 | -51.58633 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2020613c-cd1f-336a-93ad-5a7a2b2b2a3e | -10.03623 | -59.35499 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ecf193e2-3884-3db9-92b6-cf3779c02895 | -13.14403 | -57.15417 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c32fec5-f458-3cec-a70b-021b366df3b7 | -12.98701 | -56.86607 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29cc7ad9-c3ce-3aba-8982-95b6f14139cd | -13.3022 | -50.81664 | 2025-08-19 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28a4a9ef-feae-3737-ae5b-30b3ec07c2e1 | -15.01666 | -54.81351 | 2025-08-19 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6f1d75c9-2f3e-3769-9ccf-6b203444fef4 | -10.42884 | -60.29247 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e343d41-c7c7-3e80-91ad-490cb1051bb8 | -12.99812 | -56.86769 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4fcd7e2-c592-3519-b89f-cc64a274878a | -13.18823 | -54.94521 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df3c272e-befb-3ffd-9ac7-cf86476f4c21 | -12.98274 | -56.84256 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9382e22-73a1-331c-bedd-a97e64c8022d | -13.13974 | -57.15798 | 2025-08-19 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6334b23-457d-3631-847f-e70af6dd1ec4 | -9.9375 | -60.49723 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 637e5567-e81e-3dc0-a3c6-111214742edd | -11.85705 | -51.58329 | 2025-08-19 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61be00ad-07bb-33ea-bd26-29cdb32986a1 | -14.84553 | -48.07027 | 2025-08-19 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffb7947f-fbe4-3fbc-99d5-c8ee80a06216 | -9.5116 | -60.5259 | 2025-08-19 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e319e30-1bf6-335f-ba7b-9c000df41a9f | -9.88844 | -64.2614 | 2025-08-19 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62253f66-4e83-306f-b41c-7223839257b9 | -13.74225 | -52.02554 | 2025-08-19 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0eca2d-11f0-325e-9cd8-0f46bf456204 | -13.16157 | -54.9217 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7f75c7-8c6c-3db2-aa9d-9bf8a898d50d | -9.52799 | -63.57631 | 2025-08-19 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4e4e16b-5eb9-394b-9653-720a09b5a1e4 | -13.15688 | -54.92494 | 2025-08-19 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f466836-ae64-3349-bbd1-3f6a70840114 | -6.9524 | -43.6083 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 682e76fa-b4b8-31f9-ac9e-0ee7ce98bfd7 | -6.9712 | -43.6066 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 323d8d57-0e97-3d0d-ba7b-207f3f0a5ca9 | -6.9527 | -43.585 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b1515783-5c7a-370a-8c1f-26a9203bbd33 | -6.9339 | -43.5868 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| cb987d1b-7e3d-38f7-8eeb-83285f97bfe7 | -6.9336 | -43.6101 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 824b0af5-def1-38d0-b418-481f0b09599f | -6.9715 | -43.5833 | 2025-08-19 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f39508a8-993d-3e8b-87de-c85edcf69620 | -20.86673 | -56.91625 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88bb82cd-8fa7-33d8-84cc-37031b8b72a7 | -20.87169 | -56.90977 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d5e5a21-020f-3ff4-9d1a-505c071be98e | -20.9879 | -56.90528 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 834f8287-7bf4-301c-9c1c-5dde752437b1 | -23.57879 | -51.63727 | 2025-08-19 05:21:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 397bc225-a9db-3ac9-91e4-4aad40bae270 | -20.82652 | -57.76918 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2a9fb070-642c-3c62-9e4a-cd1728506a4e | -20.85951 | -56.90718 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccc24635-cb82-31e6-bf7a-2b3a4b93ebb2 | -20.8702 | -54.98213 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77cc667b-8585-3a4a-9fac-aa33ecbb5dfb | -20.87427 | -54.98775 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d9aa29-2217-3829-9427-45b086126d58 | -20.86762 | -56.90899 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe9f2fa2-a953-313e-b701-94a61aa008c1 | -20.85893 | -56.94572 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd13a237-cb24-3acd-a613-186f65d56107 | -20.85904 | -54.96697 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ea1c6c7-4c59-3d66-9063-30833541d0ee | -20.82765 | -57.76571 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 89535f3d-2aba-3cb5-b16f-88206b74fbe7 | -20.84446 | -56.92813 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adea2287-9bbf-3b61-af74-f401038d08a9 | -18.36932 | -49.36048 | 2025-08-19 05:21:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13bc0ac5-fe87-3d81-8c2a-e4a18817a385 | -22.23122 | -56.0724 | 2025-08-19 05:21:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6098d032-f3eb-394f-a646-3e03abf4079a | -20.32958 | -51.70928 | 2025-08-19 05:21:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a87d69a-277a-3e65-864d-bddeae7ce518 | -20.84081 | -56.92395 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2387de95-2065-3ded-a0bf-84366fee07c2 | -20.86498 | -56.89662 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea5b3f69-19be-32c4-84a3-b9275daafe24 | -20.85987 | -56.93815 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ecb3848-8792-3180-8f16-a64ce1fb9094 | -21.02725 | -56.89108 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c64abe7-8f26-312b-b5d1-90c0c4a098f8 | -20.85497 | -56.91028 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ce4f54b-9bed-35ba-b69e-5fdc590224d5 | -20.89223 | -56.91203 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84fb1d16-aa6b-34ac-90d8-d28134692483 | -20.33211 | -51.70676 | 2025-08-19 05:21:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5f1075a-9965-315b-9835-7d7b1c393956 | -20.87839 | -54.993 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ffa468-8e0d-39ce-941a-dce135ea2f53 | -20.85404 | -56.91785 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2586b63-cbf5-3bb4-a933-750544ac1a77 | -20.8749 | -56.9175 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10df543a-ab40-3570-9d32-3e1cfee7dcc8 | -20.87949 | -54.98317 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9bd5269-fdb3-3c10-b2d9-555af4fce441 | -20.8545 | -56.91408 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ca34837-a4c8-3639-b18e-5d6c93187477 | -20.85998 | -56.9034 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75e0f3a2-c9b4-3544-804a-fdc5c4f0e64b | -20.87124 | -56.91343 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a296d70-fb5c-30cb-add0-f98d6e64a23a | -20.81427 | -57.65089 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4f8d92d8-c292-3c11-a21f-fb91559f37f2 | -20.86807 | -56.90535 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c54a54b7-6f94-349a-a10d-b924448a6c53 | -21.0277 | -56.88747 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43048da6-fccf-3102-8470-84cfa2d5b14b | -17.33549 | -47.17075 | 2025-08-19 05:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c50aab2-0078-3fec-9bf2-3a2e71a26f21 | -20.85847 | -56.94951 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e748c5bc-0cb5-3b80-aa52-a14d531ea6c6 | -20.33173 | -51.71088 | 2025-08-19 05:21:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README53.md)
