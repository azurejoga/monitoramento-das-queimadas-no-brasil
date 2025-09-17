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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ec52593-6e3d-3a88-a377-1a5b8181047c | -22.32043 | -49.12757 | 2025-09-17 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89231b3c-602b-39d8-bbb3-a4f1b69dd3b6 | -19.00955 | -49.92862 | 2025-09-17 04:36:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d753d247-cf32-3dfa-b1d9-22ecc28fd9d4 | -21.57915 | -50.31219 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f1dcf136-fe50-3fb5-9372-9ffd10e5a1af | -19.553 | -47.69744 | 2025-09-17 04:36:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54e4e72c-2589-3c18-b778-abafcb014c31 | -22.19316 | -51.28216 | 2025-09-17 04:36:00 | NOAA-20 | REGENTE FEIJÓ | SÃO PAULO | Brasil | 3542404 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54d7a4d6-12a3-389f-9a08-1b8dae6158db | -20.83385 | -49.49754 | 2025-09-17 04:36:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cedca3d5-d4db-31c4-97f7-35248bc2e27d | -20.75358 | -56.95004 | 2025-09-17 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e88d71e-4d5a-3210-887b-2e1c9933b6ea | -22.94985 | -47.12433 | 2025-09-17 04:36:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4fe4a16-f6f5-368b-8183-cd74a21aef1b | -21.60334 | -50.32345 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 54d32d95-7fe6-3292-a028-20e8a5d53b98 | -21.56296 | -50.1225 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| bc0e9bdc-1223-3975-8b1b-a810d6ef2e7d | -22.31695 | -49.12702 | 2025-09-17 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f3b6f4d-1089-3f3d-813c-5bae88620b64 | -23.45353 | -49.25178 | 2025-09-17 04:36:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f92a33f3-e0ae-354d-99a5-7b38931f69bf | -23.45763 | -49.24811 | 2025-09-17 04:36:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a75cf1b0-232c-3950-b28f-9261a17caeca | -21.56632 | -50.12308 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| e02a10fc-3d9e-351e-8890-51c6a34d7dd3 | -19.77626 | -48.31087 | 2025-09-17 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7629ca1-6753-3173-b64f-f9b06ff1e6f4 | -21.42249 | -45.46955 | 2025-09-17 04:36:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 98ec8429-794d-3c74-aea1-eef0d7baca60 | -23.50497 | -47.05117 | 2025-09-17 04:36:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0219c59-4ec0-3caf-89d1-869a97001fee | -22.31847 | -49.12623 | 2025-09-17 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f9dfb1a-dead-3327-9165-c17423e0272f | -23.48777 | -50.36857 | 2025-09-17 04:36:00 | NOAA-20 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f18ce606-bf11-3695-b4bc-8e48f2f67497 | -20.91732 | -49.26116 | 2025-09-17 04:36:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad00911c-0389-3415-aeb3-61920827eba3 | -22.35973 | -49.03557 | 2025-09-17 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c70e7b83-5b39-3cf4-94ee-ce44a5ada17c | -23.48439 | -50.36799 | 2025-09-17 04:36:00 | NOAA-20 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 610c37ef-8ee2-3553-bff4-06ddb0d1bd6b | -19.72733 | -54.42628 | 2025-09-17 04:36:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 183ffd97-f16b-3c81-9c2e-e654ec6b7a53 | -19.5524 | -47.70175 | 2025-09-17 04:36:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dfce25f-3b80-367a-b6f1-8a4470eece04 | -19.55361 | -47.69312 | 2025-09-17 04:36:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6527c235-acfa-3cc6-b831-9e0bef110ace | -22.66514 | -53.12224 | 2025-09-17 04:36:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d97b36be-baa4-37d9-b6dd-26c7bb8813d0 | -23.58446 | -54.98613 | 2025-09-17 04:36:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 11320796-a99f-3ed3-9e04-a0c2c3ab0b31 | -21.59025 | -50.32964 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d0c96a91-97a2-3a07-885e-1a456ed55f37 | -23.50884 | -47.05202 | 2025-09-17 04:36:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 242a0020-3a58-350f-b169-c6dc43c7d71a | -19.77567 | -48.31496 | 2025-09-17 04:36:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96388bb5-1bb1-31be-b253-29cf2a956477 | -22.32682 | -50.15764 | 2025-09-17 04:36:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 69c04b1a-2c28-3499-b78a-7ca5766154a6 | -23.54378 | -52.90578 | 2025-09-17 04:36:00 | NOAA-20 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fdb9a0e5-1d12-3e76-9b84-e9c5af95933d | -21.55903 | -50.12573 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fd388e64-3aec-3dd5-9cda-d96a1feb9e39 | -22.35915 | -49.03971 | 2025-09-17 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e75d8e0-09d5-30c5-a3c6-e55d456b9501 | -19.5518 | -47.70606 | 2025-09-17 04:36:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ca73498-1a3f-38f3-b4e1-bd2ea21ad679 | -23.45703 | -49.25235 | 2025-09-17 04:36:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7459c837-8482-3b44-9ffe-2c1334001691 | -24.32989 | -50.6534 | 2025-09-17 04:36:00 | NOAA-20 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89c76081-9143-3ad8-b104-02f6e1d5327a | -21.42298 | -45.46546 | 2025-09-17 04:36:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d10d5e6-9d6f-30ad-ba90-cbbd3a114b6c | -21.56575 | -50.12689 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e92f0d9d-0d1a-3a16-8430-60f396af10db | -23.80989 | -50.97776 | 2025-09-17 04:36:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 416ee758-affb-3623-ba2c-d4b63e7708d0 | -21.56353 | -50.11868 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| d13a2f75-6417-3e7f-a378-d71a8701bfba | -21.56239 | -50.12632 | 2025-09-17 04:36:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13bb5f81-9726-33c3-ba20-47656d54cdf0 | -21.59083 | -50.32586 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e3b10f95-2216-3ed2-b8e1-035598668630 | -23.21388 | -47.05127 | 2025-09-17 04:36:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85b74404-012b-3f5b-adb8-ed8d058f63a4 | -21.60612 | -50.3278 | 2025-09-17 04:36:00 | NOAA-20 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| dece45c7-373c-3168-919e-e1c15d602ebd | -23.48175 | -46.40057 | 2025-09-17 04:36:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e562efc8-aa0b-3eb4-a8e1-b21d50c264d7 | -23.12892 | -49.7137 | 2025-09-17 04:36:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e47f2448-c8a1-336a-b08f-1774f5ab9eb9 | -29.71849 | -51.10319 | 2025-09-17 04:38:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 67d9b21c-4458-3dd6-a11a-973edea48e2d | -24.75662 | -51.99302 | 2025-09-17 04:38:00 | NOAA-20 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dd373c84-00f1-3f15-bd38-063350f2c7c0 | -25.18407 | -52.40749 | 2025-09-17 04:38:00 | NOAA-20 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 279b354d-658a-3cae-bad0-1e87827ce89a | -25.11943 | -51.99594 | 2025-09-17 04:38:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4367f8b5-0751-329b-9976-2662f3ac7373 | -29.71671 | -51.10551 | 2025-09-17 04:38:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 6dd499d8-b213-38c8-b8e9-a51ae4c33004 | -24.43562 | -53.96068 | 2025-09-17 04:38:00 | NOAA-20 | NOVA SANTA ROSA | PARANÁ | Brasil | 4117222 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91241f7e-52bb-3cb0-8421-a40f6fec3c0b | 4.97099 | -60.29819 | 2025-09-17 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3640110-7f45-31cb-8cda-070c07651043 | -8.72167 | -62.43987 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d639c48a-bce2-3121-b0ed-6c633b71d124 | -2.92147 | -48.30851 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dbe51e62-2840-3d8f-b72f-888ec12ffa66 | -2.37739 | -47.63068 | 2025-09-17 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ccdbeba-2235-3bcc-a9f8-a390b2e2b140 | -8.44218 | -55.60975 | 2025-09-17 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef33fa43-1984-34c1-8fea-f2556a202c1e | -9.56217 | -66.73489 | 2025-09-17 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7529660e-c9c3-3a64-ac8f-7457b513a3e3 | -5.61875 | -51.7251 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69a1ff13-b063-302e-8ff9-4cd720ba7ffd | -10.80816 | -50.65286 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 871f7a12-ec36-3523-a624-39394dcba8f6 | -10.55621 | -51.47453 | 2025-09-17 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31655429-589f-3b03-8eca-90c8665258ae | -11.35153 | -50.85678 | 2025-09-17 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee1f6dec-0b8f-3b01-a346-030a7366da1a | -3.68874 | -49.01772 | 2025-09-17 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6eef20dc-9a34-34e0-9f21-8de46a036e16 | -8.8446 | -62.92732 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5df295b3-a8f4-3468-bae6-5291f2de1785 | -8.61784 | -54.66502 | 2025-09-17 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c2fa2a6-5144-32cb-99c3-50b198141e3a | -7.5336 | -63.60913 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13fcf892-ad5f-34b7-bc6b-917f6bba60dd | -10.63495 | -48.75325 | 2025-09-17 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a914dc59-7ff8-314a-a5d7-eb2574a9a6b8 | -3.23735 | -46.79512 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f94d75c4-8d8c-3794-8816-13de35150778 | -10.63208 | -48.74964 | 2025-09-17 05:23:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f6a93fc4-00e4-3997-9f3f-61e261d8e27c | -10.79984 | -50.72443 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 59e0f537-c8ac-349a-b7b5-4b477ba7c6ae | -8.65307 | -62.67614 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1bb8fb6-423b-3f11-abab-ccbed82bf03c | -2.37387 | -51.91079 | 2025-09-17 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ae48d1-47d3-3c61-9ad7-abdc8c1a2723 | -8.77636 | -62.83364 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad07b0fb-334c-36af-8d3f-f32bf817e3fc | -8.72224 | -62.43628 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbf8f53e-73ea-3057-bd71-a5f698df881f | -2.377 | -47.63079 | 2025-09-17 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 064cab1c-3292-3ca3-8b8d-9d7a00f11701 | -3.17912 | -48.81151 | 2025-09-17 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 710bf1ff-5494-307d-80f4-fe74c8503d4a | 2.94708 | -60.30566 | 2025-09-17 05:23:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce2109b6-9d27-362c-8019-9c7947062977 | -2.91921 | -48.30874 | 2025-09-17 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cce6592e-e309-32d4-9746-1e8c375cc384 | -2.26742 | -47.8835 | 2025-09-17 05:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9745c7d-dac7-305c-ab60-1f3a3c4544d6 | -5.81344 | -53.43968 | 2025-09-17 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cbc5e81-9e47-3ca0-877d-bff42628b970 | -8.72111 | -62.44344 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0a840c-f505-3521-9326-1b4b86fbdc68 | -3.23827 | -46.79272 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 16ae3090-f573-313d-b43f-3a8e37205773 | -10.81092 | -50.6572 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceb7d91f-e4a9-315e-8544-b74f949b66dc | -2.71392 | -54.9562 | 2025-09-17 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f09f23c-95f2-32d9-87d3-832683f28cc0 | -8.23353 | -71.03134 | 2025-09-17 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 940e2654-ebb2-3fe8-8a94-127382d82a25 | -7.93015 | -63.51774 | 2025-09-17 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 583ce5b6-59a2-321f-b379-97a20d40f27b | -8.11242 | -63.69151 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72125010-3c8e-3ba8-8ded-284f8ea64a91 | 2.62402 | -60.4182 | 2025-09-17 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7cbfaf3-7a70-338c-9c1e-679ef9018501 | -8.65759 | -62.66944 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710162ab-22b5-381f-9a8b-afef672943a1 | -3.0184 | -51.34692 | 2025-09-17 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3998d947-41bc-3262-b51a-9c37ab977ae4 | -3.50795 | -48.45179 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85ca2c97-d666-38ea-955b-5bee4b6841ae | -10.41993 | -50.65248 | 2025-09-17 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84d2661c-7698-3039-bc7e-d964a81befc8 | -7.53776 | -63.60574 | 2025-09-17 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db4bbe4-2e56-3304-bb78-fb7d3ea26fe4 | -8.84401 | -62.93098 | 2025-09-17 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2efa15fe-9dcf-3a36-a803-efc0b614fb71 | -2.83193 | -48.6578 | 2025-09-17 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a6418fd2-d6a5-3ded-96c6-95499ab559d8 | -10.79668 | -50.72333 | 2025-09-17 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b3a68288-df5b-30af-ae7b-87799aaf3b27 | -8.65028 | -62.67197 | 2025-09-17 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6be05b1-37e2-3bcb-8da8-f26eb08a1861 | -3.23916 | -46.78632 | 2025-09-17 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bf4bec3-d09d-339e-b2d7-af8cb2d58a57 | -4.05553 | -47.50178 | 2025-09-17 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README52.md)
