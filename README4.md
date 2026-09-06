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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3ed73c9-2c37-3d94-a5f1-880d47b9b29c | -20.44496 | -57.40488 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 33.9 |
| f63249d0-6ab3-3817-8928-00e04e81b6e2 | -20.44328 | -57.38897 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 5c359561-5b9a-3921-b3d7-4afc98ad636f | -14.9155 | -44.70107 | 2026-09-06 00:22:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 1da9a86f-3e8a-3ae0-80de-63d1f7ab8bf6 | -16.4032 | -49.19986 | 2026-09-06 00:22:00 | TERRA_M-M | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0c613a06-44a4-3f51-bf9e-d540c6d0142e | -15.7587 | -49.92458 | 2026-09-06 00:22:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 109ba411-ebc6-3c34-b064-c7a795594c8f | -14.90765 | -44.66609 | 2026-09-06 00:22:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5d30c54d-d59e-3c1e-9086-c21ab6d9d92e | -20.45459 | -57.38759 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| ef54dd5d-74d0-3b90-9120-2f4862efbb8c | -20.45562 | -57.39329 | 2026-09-06 00:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 9b06c524-1f25-3f3c-9fb6-2bd73f550144 | -14.91021 | -44.67092 | 2026-09-06 00:22:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 131.2 |
| fd2aa840-094a-3192-931e-0fdf1c88d72d | -5.3618 | -56.04394 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 55c155a1-4d4a-3779-9bf3-65cd0c8c210c | -13.80863 | -51.63877 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bc667ff-f2c6-38ae-8ecf-dd2678c5f5dd | -4.12238 | -49.08926 | 2026-09-06 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| acc91981-f022-3a3f-994e-07e1283e0fc8 | -5.30134 | -56.01369 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 55d45d15-a367-3a8b-91e5-93c3c1f3eb64 | -5.14245 | -56.26464 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d217b37-6fc1-31fb-9aac-5fe1abf2c779 | -4.92589 | -55.8153 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8ab484d3-b20a-33bd-a186-218d4c261df4 | -6.12563 | -57.74384 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 75da158f-1e09-33fe-b2cf-fff37c6da959 | -7.3759 | -47.03654 | 2026-09-06 00:24:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5c986ae5-84eb-30dc-b9bc-93759215b96f | -7.37171 | -47.0098 | 2026-09-06 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c6006287-8b55-3b1f-9314-a3a7746a358b | -10.6584 | -57.72257 | 2026-09-06 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cff7c021-cbcc-3c34-960b-fd5d78b8ad67 | -13.77923 | -53.83781 | 2026-09-06 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c0ab7a1a-6c5d-3daa-86ca-3395bf74cebd | -4.80976 | -49.38636 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| da93df12-9bc2-3a45-a60f-24dadec465f1 | -5.36301 | -56.05278 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5f1fe8cb-ff9b-31af-8cc6-1834927c13cf | -6.87094 | -55.62126 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| acaec9ab-beb6-3bf3-904e-47ec9ef34926 | -12.61873 | -52.53801 | 2026-09-06 00:24:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa64fb00-dee4-33ce-9b96-6e432eb7c2c8 | -6.65577 | -59.95471 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 44b0ba82-512f-362f-bacc-009356f7b1c2 | -10.75717 | -60.70813 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 733c445d-31d2-359d-9abe-3040a0768814 | -4.92468 | -55.80655 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dcd6571a-abb9-3a19-a6fe-8a9861fad2b7 | -7.44617 | -49.73748 | 2026-09-06 00:24:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0973bb1c-2e60-3ce0-abae-1c29fd571684 | -13.79935 | -51.64022 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a4db51cd-1de7-369c-a728-0e61af0601f5 | -13.74667 | -51.66916 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2e30ac73-1dde-3414-9338-81af656f8316 | -11.68871 | -54.59049 | 2026-09-06 00:24:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b5406a5f-4bbb-3725-b388-99659262a684 | -13.79154 | -51.65175 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| d7dd1ef0-68d8-390c-99cc-f7ef4dcbb74d | -4.3535 | -48.97081 | 2026-09-06 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a3bd3971-042f-3cd0-bd65-1997794678c3 | -6.86973 | -55.61242 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 69cec3f3-255b-3af5-83ce-a00998dd808d | -5.57109 | -49.04134 | 2026-09-06 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 89654925-9ae8-3aeb-815c-7c38c7a20d6a | -7.26701 | -55.1483 | 2026-09-06 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b0059bf7-9f9e-32f6-9b7b-d06bb70ce2f3 | -10.68464 | -45.93416 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 364.9 |
| 91a43cda-6167-3803-96b5-e169c6c97c00 | -10.75952 | -60.72752 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 05ef7fa7-a8be-3e04-9613-e1072b47b854 | -6.66691 | -59.95327 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8f1bf68a-f451-3086-be1f-df79157990ed | -10.6669 | -57.7096 | 2026-09-06 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 465dde68-8ef6-34eb-9c59-f2d19f013166 | -6.8393 | -59.43495 | 2026-09-06 00:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6e30e071-1aef-387a-8a67-91d832be3e48 | -5.16891 | -56.04707 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d47c91d7-8b54-37f3-b196-89d1a42a58f8 | -5.84752 | -52.05413 | 2026-09-06 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 15b8aee0-36d6-3d23-90e2-eb0ea7a76dba | -6.51526 | -58.30204 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1cf4bc2e-a4ec-35be-bbe2-4600e500300c | -4.35898 | -47.77929 | 2026-09-06 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bb307de8-a5b0-39a5-b4c0-e07023aa3a09 | -10.68929 | -45.96215 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 0fbac364-7771-36a8-aeb7-e7324a3ed119 | -6.0889 | -47.30179 | 2026-09-06 00:24:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| e30f31b8-f11f-319f-b2b6-9908ca5ffb89 | -10.66842 | -57.7213 | 2026-09-06 00:24:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d45fd70-61ed-33eb-b4ec-675a6569b4c9 | -14.42508 | -52.20564 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c373702b-79fa-3533-af76-d5857067d0b8 | -13.8267 | -51.65056 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5b8d8e2d-c34d-3007-83ee-0ba897fb7d8a | -5.17132 | -56.06474 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4e9c5f8-42ab-3879-b391-b4d8edbdbbae | -6.06038 | -57.80084 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b17beebf-95c1-3fed-b1c3-8e1f712f35e8 | -10.69834 | -45.92619 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 90f4c9bd-1641-3e1d-a75c-9c0dd26f0853 | -13.75445 | -51.65762 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2b23da55-9c17-38ef-b23b-6d867f1f96a2 | -10.68348 | -45.92893 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 302.7 |
| 93746598-c56c-3c17-9607-d5227a8ff089 | -10.73882 | -60.76992 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8e4ea369-e316-3197-91c6-a181f243c8eb | -13.80082 | -51.6503 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 044ab475-ad81-3b2f-aa56-3e8ce3cbc798 | -13.81936 | -51.64736 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8ea7a571-a64d-3fad-b27f-aad2f9949dd5 | -13.82819 | -51.66062 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88e0a96d-2b1c-3485-b2ca-792570b7a46c | -5.35056 | -56.02749 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6258c539-d6de-369c-9bbe-f71a34841204 | -5.14043 | -55.97012 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 170ff89c-85a3-3ad1-a080-12c7f39cf4cd | -7.45329 | -49.73063 | 2026-09-06 00:24:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5f9842c1-8da5-369a-beb9-9cd661b1cd8e | -5.36059 | -56.0351 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b7185e6f-19e0-3762-8407-f6420607279d | -6.07244 | -52.25929 | 2026-09-06 00:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 79f99461-d7ca-3ef0-ae82-b5f574ea9ffa | -6.06176 | -57.81113 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 803a1f7f-1683-33ee-825d-4ee8c4eb3837 | -5.14923 | -55.96888 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3fbb480e-7e28-31a5-8646-fd5e81ac06fe | -8.49853 | -54.65387 | 2026-09-06 00:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0ef668df-8ffe-3a57-8d5e-44732d021009 | -6.65553 | -59.96051 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 155a8174-a48c-3d05-be2e-0991a0e83ff9 | -13.81301 | -51.66895 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f5d64759-5e21-3e10-9e03-8097c0d43c05 | -5.13922 | -55.96132 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7930757c-755d-300d-ad97-a4fbdc1cdfa7 | -9.18952 | -59.69023 | 2026-09-06 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c11d24c2-ea87-331d-996b-9a9d75189ebb | -10.6995 | -45.93138 | 2026-09-06 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7b219c8d-8c05-3a10-8e29-a01d51f7ec85 | -4.89774 | -55.82553 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bbe6f0ab-91e5-3174-aac7-f802e53001d1 | -5.37183 | -56.05155 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3d75ef49-1fa4-3df5-a73f-e2666b943832 | -13.78227 | -51.65319 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e27c1de3-f5ae-3373-bf1c-75213d1ae38e | -6.66506 | -59.93861 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 5ae7ff17-26e1-3ff5-b857-ee4a48ccc851 | -9.1915 | -59.70555 | 2026-09-06 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f10313db-c8bc-3384-bfa6-3165934e558f | -10.74684 | -60.72911 | 2026-09-06 00:24:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| b3bef72d-5016-3b65-b63b-70468c60d206 | -5.34175 | -56.02872 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f18c5be4-28ad-3f79-8eca-b7704a3cda99 | -6.0171 | -57.69241 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a9558d7-7631-354f-b5e4-864fb1ef843f | -13.77043 | -53.8391 | 2026-09-06 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7360d2f2-b1f8-3d03-b386-df7b5b78b179 | -5.35938 | -56.02627 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 15138ce0-1148-3779-9b7e-0b065d841dca | -9.89482 | -57.50433 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ee36d491-350a-3b61-89ce-d2ac896a46e0 | -10.48786 | -46.03909 | 2026-09-06 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0fe6b132-7dc2-359c-b365-56b15577d3d1 | -8.98513 | -44.41328 | 2026-09-06 00:24:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9c38afa0-2288-3374-8477-db5d787eb505 | -13.82227 | -51.66749 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a58aed14-01f5-3d2b-9c2a-df084ca48e5e | -13.7652 | -51.6662 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ab61ce75-49ff-3610-8e7b-c28f49a470f3 | -5.14367 | -56.27353 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| eefd3fac-5f37-3ec2-8982-c066f309ce85 | -4.46028 | -46.15013 | 2026-09-06 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a0dfe4ef-5557-39c8-8969-a5f5810046ab | -9.18809 | -59.68475 | 2026-09-06 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4a0290f-ce48-31cf-9c7a-779928b7ce82 | -13.78079 | -51.6431 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 5f337880-0849-31ba-9ac4-3e4b292f4840 | -6.06984 | -57.7995 | 2026-09-06 00:24:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 23132c4f-e83a-3859-a1b3-98978ea5d2ff | -9.18994 | -59.70009 | 2026-09-06 00:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6878cafa-009d-3dc0-9891-f5fd08651f0c | -6.66277 | -59.92991 | 2026-09-06 00:24:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bba10939-c8ae-36c9-a244-ac20451c5200 | -13.76372 | -51.65614 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c0c6a040-5053-367a-ae4a-7cd7200dfcbd | -10.47792 | -46.07058 | 2026-09-06 00:24:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5943cbad-3916-392d-b370-e426d4a83af8 | -5.14682 | -55.95128 | 2026-09-06 00:24:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4b4cd141-d983-384a-afe1-d7e87defe220 | -7.37716 | -47.03075 | 2026-09-06 00:24:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 17a7d094-9fc4-358c-b3dd-b8d66d1daed7 | -13.75594 | -51.66768 | 2026-09-06 00:24:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 20f7af45-92ff-38c3-92eb-deff195e5d7e | -6.65361 | -59.94603 | 2026-09-06 00:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |


[Clique aqui para ver as próximas entradas](README5.md)
