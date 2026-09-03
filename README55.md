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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e9625b8-56c0-3d62-9b2e-2b0778b39373 | -1.51602 | -54.95631 | 2026-09-03 12:29:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 716fb9eb-1fb7-3610-a9b5-b861dca79484 | -7.21556 | -56.76636 | 2026-09-03 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| fffd7b16-ed06-3df3-8918-f1de4352d5ba | -3.39508 | -59.36224 | 2026-09-03 12:29:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5278ffc9-b72e-322c-8d67-e76665c40015 | -8.44008 | -54.68707 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 864c2c47-4bd3-3475-bffa-a776af5d9d6b | -1.51154 | -54.2577 | 2026-09-03 12:29:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 481d27c5-00f1-3d66-9550-e2de86c1c246 | -9.22404 | -51.51301 | 2026-09-03 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 18d7adcf-a30a-3db6-849f-502865fb4c8d | -4.70826 | -56.04873 | 2026-09-03 12:29:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d9c08395-446a-3836-b4e3-9671ae5d6156 | -7.02697 | -62.97372 | 2026-09-03 12:29:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1104d7e3-a8fd-3a15-ac83-9b8ff6c0c24e | -5.47158 | -60.0622 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b3797ffa-b4d7-346f-989f-aaebade3397d | -6.67163 | -58.77283 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aa4932cf-b61a-3ae9-bd91-1971169ee9f6 | -3.50044 | -56.89548 | 2026-09-03 12:29:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eb1d8bb7-9c66-3e59-afaf-1d345dcea76a | -6.68563 | -59.95579 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 50c401f8-c08e-3132-88c2-180b2319a308 | -6.7702 | -59.43475 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1e4a6bf8-f30a-37ae-89ef-595dc136aef6 | -11.1477 | -51.53369 | 2026-09-03 12:29:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 5ea94761-3d9b-32b0-bf7d-d0462b297aab | -9.23016 | -51.50822 | 2026-09-03 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 1482458d-73f4-33a3-9873-e2ffff8cdb54 | -6.37199 | -58.2895 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ada30f26-c6e2-3aff-9d35-d0e82053d1fe | -8.45274 | -54.75227 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| debc02b0-2acc-3c9b-bb78-b37709568521 | -6.63996 | -59.44146 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 9dbc387b-ae81-30f2-9bd7-91ca44183c22 | -7.54053 | -60.7192 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6f171337-106b-3aed-8475-4ed1c4e6dbe7 | -8.79305 | -54.58321 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 19b4e1e8-609c-3eaa-a366-e0d8ab9649fa | -4.70692 | -56.0583 | 2026-09-03 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| db75bcdd-9850-3b06-b8b3-fc7c5d52948c | -3.61848 | -60.56273 | 2026-09-03 12:29:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3254939e-131a-37cf-a4c8-eaafda5d3ebe | -6.41856 | -58.29347 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 98d1f976-896b-3c38-908a-566721ae1971 | -3.18607 | -61.14909 | 2026-09-03 12:29:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c6239f19-de24-333a-b186-3b7767c19410 | -1.50932 | -54.25144 | 2026-09-03 12:29:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 30a26da7-13e8-311b-9e33-051c73cd136e | -8.7825 | -54.58182 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 74e79e8c-58cb-3708-8cef-8153a2f7fbd0 | -5.56198 | -60.18032 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b12acb62-4622-30a3-a278-78dffcfc9009 | -8.47632 | -54.6531 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 2151a590-109a-3c31-9c0e-59d4f441a6d8 | -6.76885 | -59.44397 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 63683602-594e-3fd9-8108-f13a2f0458a6 | -7.60657 | -49.9504 | 2026-09-03 12:29:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| c0515ba2-3649-30c5-b685-e56be14b8216 | -10.27379 | -50.0552 | 2026-09-03 12:29:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e7dad936-4158-3848-8109-e28d434c4818 | -6.94681 | -58.98301 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a2f628d3-5d96-39fc-bef9-8d9e3752fabd | -3.12127 | -61.22924 | 2026-09-03 12:29:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 033fec99-58b4-3ea9-bd14-59e88b52b749 | -3.75155 | -59.31907 | 2026-09-03 12:29:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8713421-8775-3074-8d52-9e0bc265b8f6 | -8.90431 | -62.35465 | 2026-09-03 12:29:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 86297725-51ee-31fe-8522-67866542dc6b | -6.15363 | -57.75505 | 2026-09-03 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 55789370-cc3f-3ad4-bbbd-94d846748448 | -5.4622 | -60.06086 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f1d08e8-8d6b-3b34-8597-bea8fa71e116 | -6.6838 | -58.76271 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4b908560-ecd4-36ab-a333-3fe16c6bb22a | -6.6386 | -59.45083 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e0365006-e214-33a4-b438-7f371cae3fe4 | -7.61024 | -49.92191 | 2026-09-03 12:29:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 84301a7a-14ea-368a-95fe-bd7c606157d0 | -3.38658 | -59.42064 | 2026-09-03 12:29:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 007f5def-4191-366c-8b98-587b0660e7ce | -11.57044 | -50.47724 | 2026-09-03 12:29:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f71ec667-d4e5-31e2-9535-8efdedb0d580 | -6.68509 | -58.75381 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 051c1540-a96e-3c1a-8e9a-0f15fcb44bd6 | -3.59589 | -55.37194 | 2026-09-03 12:29:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f7494af7-e7dc-3a5d-a739-74994e0fad46 | -10.26976 | -50.06005 | 2026-09-03 12:29:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ae3b45ac-b06f-3e16-b989-14a3c5ce0448 | -6.65033 | -59.43347 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bf485eb9-6178-3700-873c-5147be53a3be | -7.56002 | -61.34147 | 2026-09-03 12:29:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 8aa5ee17-f3a9-3b15-92b3-bcee245557cd | -5.21466 | -60.03346 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| bbaa26fa-cd5f-34bf-82f7-92125afb9bca | -11.3052 | -45.1344 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 221eea9f-4d5e-3c03-b15d-ea1eb1dc7150 | -11.3243 | -45.1317 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 31ebc7c8-aea2-300c-ae90-64f006367745 | -10.8635 | -45.3101 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 15214b43-61df-38bc-8335-b9f18e768a4f | -10.8822 | -45.3305 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| 1a42eab0-43c6-376d-b26d-a5567ef9b582 | -10.8826 | -45.3075 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 19003586-9d88-3e04-93ba-a58350b3bd66 | -10.2815 | -50.0464 | 2026-09-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f824a7e5-db2d-3848-92a5-d407cc7257ca | -11.3247 | -45.1086 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 85e71cc7-afe9-331b-9f83-b4e17cb1e23b | -10.8631 | -45.333 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 06b3219e-529c-333b-acdb-6b3de23a4f66 | -10.9013 | -45.3279 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 55ab14a8-b857-31a6-aed1-22caefa992f2 | -10.8818 | -45.3534 | 2026-09-03 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1cdedcc8-5bae-38fa-9d82-fbf5b182256c | -11.5634 | -50.464 | 2026-09-03 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 90d62b1d-b506-3aa8-9c54-1f0b3054ec26 | -12.4033 | -44.8089 | 2026-09-03 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 84d8460d-54de-36c9-a1ac-c705c0ef821f | -13.37731 | -51.3588 | 2026-09-03 12:32:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 39f4bc09-a0ea-32c0-b311-462c8ee28951 | -13.38035 | -51.33131 | 2026-09-03 12:32:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3281f5ee-adb2-35de-bc70-255fb1c8d830 | -19.43103 | -54.55668 | 2026-09-03 12:32:00 | TERRA_M-T | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 10eecd80-6a69-360f-a99d-cf16a3fa2f4d | -12.88178 | -58.27962 | 2026-09-03 12:32:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7903f10b-95ab-3d50-b725-a1c646dbe6fb | -16.76577 | -53.36333 | 2026-09-03 12:32:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a5e36b1b-3b67-39ec-8191-afcf75ade06f | -18.14638 | -51.81764 | 2026-09-03 12:32:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| cf09e586-23ec-391a-8be3-ed5e26296c81 | -18.16243 | -51.79588 | 2026-09-03 12:32:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6b2825f8-0a92-3887-b30f-2fe14a635d9d | -18.16454 | -51.7888 | 2026-09-03 12:32:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| d35f41f2-313b-3fc3-93aa-33671863aec8 | -11.79625 | -61.32488 | 2026-09-03 12:32:00 | TERRA_M-T | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 32f918c4-c1f8-32c6-9b0c-93ad8497df6a | -14.14451 | -58.87318 | 2026-09-03 12:32:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a24be83f-e879-36f6-8b57-7a2119646d42 | -16.75323 | -53.37687 | 2026-09-03 12:32:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 66faf639-2e0d-3afb-8af2-436deb676a56 | -18.16148 | -51.81952 | 2026-09-03 12:32:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 90e6f4ee-d019-3fa8-8fa5-11e93fc37eda | -11.3243 | -45.1317 | 2026-09-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 53d24ab6-eb8e-3d3f-9ccd-503206d90bc4 | -11.1312 | -51.5306 | 2026-09-03 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c11ca4d2-647a-3fd3-8fb7-cc7327945125 | -11.5825 | -50.4618 | 2026-09-03 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 625a575b-b0f1-3c5e-9ebd-edd4617163a5 | -10.8822 | -45.3305 | 2026-09-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e623d4f4-de11-3a70-ba63-cddef6ae17ab | -11.5634 | -50.464 | 2026-09-03 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9c6e841b-c1c8-3dc3-827f-0d045bfb9874 | -8.7853 | -54.5808 | 2026-09-03 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d50779ff-1a14-33a7-94b8-6dff11ff8c99 | -12.0553 | -47.0966 | 2026-09-03 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ae6130eb-a90d-3d70-ba19-9b2c8c600e22 | -8.7819 | -46.4399 | 2026-09-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 86f28eda-c3c0-3687-abae-54af4bf1cc1c | -8.4481 | -54.7452 | 2026-09-03 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6b39a9c5-01de-3981-89c8-6a8337369fcf | -10.92 | -45.3483 | 2026-09-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 0a9cb448-4385-3be8-913e-984f4c742418 | -10.9013 | -45.3279 | 2026-09-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 5cf3d8c8-7364-38e9-a33b-4615d5640597 | -12.0557 | -47.0741 | 2026-09-03 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ba8869dd-8234-36b0-8fa3-9060004f11d0 | -8.7631 | -46.4418 | 2026-09-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d77ea913-afaf-33ec-b6f4-f33971c5930b | -10.9009 | -45.3509 | 2026-09-03 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e6faef26-e267-3fb8-9b65-cb747c71e3a5 | -10.2815 | -50.0464 | 2026-09-03 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d9d722aa-d192-311d-8b3c-e3e4be9e322a | -11.3056 | -45.1113 | 2026-09-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e8efb125-ed5a-34c7-9136-560dfe62d7ec | -11.1312 | -51.5306 | 2026-09-03 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a5807489-4375-3875-9d96-b99f04724470 | -10.92 | -45.3483 | 2026-09-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5b165446-f38b-382a-a341-907d259dad5f | -7.6171 | -49.9226 | 2026-09-03 12:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9e98d6a6-a2d8-3677-b0db-12de20eb86bb | -12.0557 | -47.0741 | 2026-09-03 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3e1a5922-e5ea-3f9c-83af-35e739d8c3fb | -11.5634 | -50.464 | 2026-09-03 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e33c0941-860f-39b3-8fd0-e12a41e8739d | -8.7819 | -46.4399 | 2026-09-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 8ccdf945-6a65-3fa6-9fe2-d655f59560d9 | -11.3247 | -45.1086 | 2026-09-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| df9f3c21-26d2-3f0c-b534-3cd6768eb23c | -10.1842 | -50.27 | 2026-09-03 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 22d00552-df68-3aa5-aa1e-8251dfd71c71 | -1.4752 | -54.8157 | 2026-09-03 12:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 613af048-eb88-3250-b255-2b7a412ceeff | -10.9013 | -45.3279 | 2026-09-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1bf99984-37bb-3627-8485-243a64196b73 | -11.3052 | -45.1344 | 2026-09-03 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 736b3a32-9de6-31e6-85bd-4eb722e86442 | -10.2815 | -50.0464 | 2026-09-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |


[Clique aqui para ver as próximas entradas](README56.md)
