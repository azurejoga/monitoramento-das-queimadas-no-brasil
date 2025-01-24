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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c96496d8-4f52-39cf-9438-2997c6ba306a | -7.7266 | -35.0071 | 2025-01-24 00:00:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| f7bfea7c-a592-3ef0-b988-40f62ddaca8b | -7.7262 | -35.0347 | 2025-01-24 00:00:00 | GOES-16 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 71905917-69a6-3ba5-8afd-bee0ec825b44 | 1.1037 | -59.4568 | 2025-01-24 00:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b5950b1f-54b5-374d-97d3-e294179ab8d1 | -12.7659 | -44.8386 | 2025-01-24 00:17:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50d95f7b-a9d3-3911-a483-3b2e793ee1e2 | -10.187 | -36.7061 | 2025-01-24 00:17:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 0d75df3b-89c4-356b-a632-8323252f3956 | -10.6323 | -37.046799 | 2025-01-24 00:17:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f943cb9e-44ad-3c22-b00d-f6eae6db7a7d | -10.7606 | -37.1064 | 2025-01-24 00:17:00 | METOP-C | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd9f4cab-312a-3f0c-8ce9-ab9e73f4455f | -13.4813 | -44.0163 | 2025-01-24 00:17:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2961d78b-c9c0-39dd-a436-f947c6926851 | -9.9111 | -36.050301 | 2025-01-24 00:17:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cea49c6e-ead3-3298-9c17-0adb1fc42da4 | -9.8482 | -36.2547 | 2025-01-24 00:17:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a785ff3a-612d-3fc8-aaea-5e9517793c03 | -10.1926 | -36.729198 | 2025-01-24 00:17:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c11e38f9-3715-3a8c-8c5f-011caf19421e | -5.5549 | -35.5149 | 2025-01-24 00:17:00 | METOP-C | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 948a4105-9318-3b05-acf6-ae2ea468e0bc | -6.443 | -35.0317 | 2025-01-24 00:17:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b2555bd-b2ad-3779-9ac9-7bb95d7a83cd | -10.7911 | -37.189098 | 2025-01-24 00:17:00 | METOP-C | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15fa077c-6b4a-38a9-8722-e92ec933b279 | -6.4485 | -35.012199 | 2025-01-24 00:17:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ed080b7-de26-3a5e-9189-2133aa2d4001 | -10.7579 | -37.095699 | 2025-01-24 00:17:00 | METOP-C | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33b448c2-dd22-316d-8836-e1ac0ae5ebbd | -9.8513 | -36.2672 | 2025-01-24 00:17:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f85bbf81-3198-3536-b087-85334abd5110 | -11.0263 | -45.046799 | 2025-01-24 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 176efa4e-26fe-39fc-a9d2-96e6d6ae6945 | -16.044701 | -43.389198 | 2025-01-24 00:17:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c97da410-9b05-3968-9031-2f4dc673e54f | -6.4388 | -35.014599 | 2025-01-24 00:17:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0728c59a-6779-38ad-837a-12eddcea64be | -16.042999 | -43.381302 | 2025-01-24 00:17:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 304a1a7e-8dcd-35c3-971f-42add3c605df | -9.9079 | -36.037399 | 2025-01-24 00:17:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f953bc2-890c-3a01-9bdd-462e24145457 | -11.0281 | -45.054901 | 2025-01-24 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe09e6a2-b08e-3884-a3ca-863ba1e12670 | -6.4527 | -35.029301 | 2025-01-24 00:17:00 | METOP-C | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8bfbeef-e71e-3551-b974-f0c2cd5f0ec6 | -5.5646 | -35.512501 | 2025-01-24 00:17:00 | METOP-C | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 0d4a6578-1ea0-3ce1-ac85-70f27b1cbf50 | -10.7885 | -37.178501 | 2025-01-24 00:17:00 | METOP-C | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8eb2f6bf-2dd7-37a9-bf56-3546dc9be678 | -10.1898 | -36.717701 | 2025-01-24 00:17:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 879a9461-50eb-3ee0-a0a0-9a49808ecfed | -10.6226 | -37.049198 | 2025-01-24 00:17:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9dea5ebb-561d-3999-842e-c19dd959fce0 | -10.1918 | -36.7236 | 2025-01-24 00:20:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 111.5 |
| e3187a69-0896-32b1-92e0-36561ce6f2a9 | -10.63222 | -37.04437 | 2025-01-24 00:20:00 | TERRA_M-M | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 57dc6178-f1e4-3ced-8064-5d51e8f0b3d9 | -10.1842 | -36.72816 | 2025-01-24 00:20:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 18.5 |
| ce8409b5-0156-3575-aa2a-d9d8b679deb1 | -5.68533 | -38.30371 | 2025-01-24 00:20:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| aea43f41-1277-371d-9da1-f269e4baf253 | -6.55834 | -35.26173 | 2025-01-24 00:20:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 18.8 |
| cbff7b69-d94d-3b8d-83d7-4eef11a6c26a | -10.55583 | -37.50278 | 2025-01-24 00:20:00 | TERRA_M-M | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| c260f65c-129b-32d1-944a-c1ade88ca497 | -7.22815 | -35.79053 | 2025-01-24 00:20:00 | TERRA_M-M | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 09d78ac0-3ee3-3a9c-9263-b913feb815fc | -10.19441 | -36.72654 | 2025-01-24 00:20:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 48.8 |
| d2f82962-559e-3098-ab3f-ee82aeb472d4 | -6.45435 | -35.02185 | 2025-01-24 00:20:00 | TERRA_M-M | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 1122ad58-38a4-3e6e-9117-0f05ccbd6fd1 | -6.55463 | -35.26863 | 2025-01-24 00:20:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 8c56bbbe-93ad-31ab-9f6a-9c63d7309c47 | -10.19255 | -36.71434 | 2025-01-24 00:20:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 40.0 |
| d8be5312-8f3f-3cbd-adfe-711acc2803d3 | -6.44189 | -35.02385 | 2025-01-24 00:20:00 | TERRA_M-M | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 204.1 |
| 71bd4dc2-d061-3f43-983b-3bd8373a6dd0 | -10.18231 | -36.71587 | 2025-01-24 00:20:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d7b73c19-3d26-3013-b623-a4e7536a42f5 | -13.47568 | -44.02563 | 2025-01-24 00:20:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 440a7d6e-f6c9-3c91-a699-0a8f2db2c340 | -5.56105 | -35.52013 | 2025-01-24 00:20:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 910737ac-2e49-3b50-a98e-ba6cf0e126a9 | -12.77215 | -44.84282 | 2025-01-24 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c4fe19d0-4a9a-30d6-a923-3719a8c5b597 | -6.44478 | -35.04254 | 2025-01-24 00:20:00 | TERRA_M-M | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 79ad6681-dd79-3d7d-90b9-26e63deee2b5 | -9.6409 | -41.570999 | 2025-01-24 00:21:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 47902a1a-2c46-3ff5-9ae7-7776b721fd88 | -18.6353 | -40.3181 | 2025-01-24 00:21:00 | METOP-C | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d992e804-96d7-3c6c-a8a8-9c23517e94bb | -17.069099 | -46.353298 | 2025-01-24 00:21:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5b54a61c-bf71-3a28-a6d5-12beec57d302 | -17.681499 | -42.309299 | 2025-01-24 00:21:00 | METOP-C | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0de7b0d7-06aa-31f2-b9d9-999d3910c197 | -20.8834 | -41.9286 | 2025-01-24 00:21:00 | METOP-C | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05400070-631e-3c7d-8d7e-ce9d13108625 | -18.2523 | -42.194302 | 2025-01-24 00:21:00 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5469eae-60a7-3634-bee9-e81281b4dab6 | -18.633699 | -40.310902 | 2025-01-24 00:21:00 | METOP-C | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c95374d1-ef6b-35a4-939b-bf8fb4c12da8 | -20.8818 | -41.9207 | 2025-01-24 00:21:00 | METOP-C | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a19f28d8-b5ef-3e82-b9e4-de13de02ab0d | -15.6443 | -39.1931 | 2025-01-24 00:21:00 | METOP-C | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57a847f2-dd15-38e0-86cb-a2f3c5cd1b3b | -7.7153 | -35.018101 | 2025-01-24 00:21:00 | METOP-C | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd3e140a-776a-34bf-85ef-b68258235e52 | -9.7938 | -36.201599 | 2025-01-24 00:21:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 766fa7cc-8323-3805-8345-b544e007dc1b | 0.8843 | -60.1441 | 2025-01-24 00:30:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3a9b636d-3e86-3c3b-8b8e-99282afe8960 | 0.8843 | -60.1631 | 2025-01-24 00:30:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 74ebeb47-9fb3-365c-a833-a6fa8bc33078 | -5.9867 | -35.3648 | 2025-01-24 00:30:00 | GOES-16 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 70.4 |
| c237d4d5-8597-322d-9c9d-a1dc535f7fb3 | -6.4474 | -35.0386 | 2025-01-24 00:40:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| 307cd97b-e6b6-32d3-aa68-8ac66d9dbf37 | -6.4477 | -35.0111 | 2025-01-24 00:40:00 | GOES-16 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 143.7 |
| c896cfc1-e3d1-3e8f-955a-f3e9067e2ca9 | -15.2691 | -51.4632 | 2025-01-24 01:01:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1753840-b531-3dfb-a4f2-43ba63a7cff0 | -19.371599 | -53.551701 | 2025-01-24 01:01:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5b7ad85d-78b4-38ce-acd5-917cab01369a | -9.2686 | -60.3064 | 2025-01-24 01:01:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35beb07f-fac0-3516-a228-ff51d8f2fa8e | -9.267 | -60.299 | 2025-01-24 01:01:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc33c02a-9bd3-3d6e-8cec-2377d8dd6100 | 1.3812 | -60.791401 | 2025-01-24 01:04:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5a0a5de3-f806-32d3-9d02-1851008f0360 | 1.1053 | -59.4548 | 2025-01-24 01:04:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d7feeced-9c8d-36df-8485-f978f93a4107 | -15.2386 | -60.219501 | 2025-01-24 01:04:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc8d4f5-b8d8-368d-8f62-588221986938 | -15.2368 | -60.210899 | 2025-01-24 01:04:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa3a736-ff92-302a-8713-dde2bda38612 | -15.2484 | -60.2174 | 2025-01-24 01:04:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e456267-b07c-33df-86ff-5ffe05200b99 | 0.8764 | -60.1507 | 2025-01-24 01:04:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdae064-d295-399c-b839-e99bfa642c49 | 1.1037 | -59.4618 | 2025-01-24 01:04:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ffab48af-e53a-3f1c-b3cc-651a5f129d53 | 1.3251 | -60.034302 | 2025-01-24 01:04:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 45748e03-f4ad-3b73-86ea-ac465ce0b014 | 1.1068 | -59.4478 | 2025-01-24 01:04:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7f295468-db92-30fb-8836-998918fffa42 | -15.2466 | -60.208801 | 2025-01-24 01:04:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37fce2e0-6665-3bf6-a87a-fc5a2e2e7fee | 0.8779 | -60.143902 | 2025-01-24 01:04:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fdf54424-5b7c-3afe-bbf9-1bb96971e0be | -10.1201 | -36.4417 | 2025-01-24 01:40:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 71.1 |
| c42adf82-d375-3624-842e-616a52cce6ab | -15.24642 | -60.23232 | 2025-01-24 01:58:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e8d8beb-6eaa-33d6-a85b-95f2ebfa3c07 | -15.24446 | -60.21983 | 2025-01-24 01:58:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 30de4099-bdf7-3d3f-ab80-f61bab5bde8d | -15.23621 | -60.23403 | 2025-01-24 01:58:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 30e5d543-8873-37ca-807a-0f1b70148a05 | -15.23425 | -60.22157 | 2025-01-24 01:58:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9a765644-6d4b-35c3-ac1b-e8fe87af766d | -12.37566 | -64.00574 | 2025-01-24 01:58:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f9747d5-5bd0-3f6b-8cbf-4be56de0ebf7 | -12.94575 | -61.33898 | 2025-01-24 01:58:00 | TERRA_M-M | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4dc45cad-8ff8-3570-b6bc-2961c2a64e64 | -6.5411 | -35.1643 | 2025-01-24 02:00:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| c4dd1c79-fed1-3f15-9c2f-7a13b3c86864 | -6.5407 | -35.1917 | 2025-01-24 02:00:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 119.9 |
| 64aaf3f8-463e-380b-9bca-f36a9fc14f7e | -6.55 | -35.19 | 2025-01-24 02:00:00 | MSG-03 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd8cc3ac-cb5e-3329-805a-1430555968da | -15.2382 | -60.223801 | 2025-01-24 02:00:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85153d65-8d09-33bb-8934-50f723874823 | -7.96919 | -35.21257 | 2025-01-24 02:51:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 08dc93d1-8f7e-33d9-a0ad-cc9f46786a74 | -7.96382 | -35.20572 | 2025-01-24 02:51:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 413547f2-6168-366e-bf43-48e6ea7c8df5 | -8.40265 | -35.32065 | 2025-01-24 02:51:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0a94c038-0af5-3e58-ba92-aaf9546bf57f | -7.9628 | -35.21107 | 2025-01-24 02:51:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3c7e32ae-2638-340e-a491-c6243961f616 | -8.40368 | -35.31522 | 2025-01-24 02:51:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 481d9859-3442-3d2b-bf97-712676b0cc04 | -7.96819 | -35.21782 | 2025-01-24 02:51:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4d803aee-2837-3821-a536-fdce28324ed5 | -9.41974 | -35.92706 | 2025-01-24 02:53:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e370b0c1-cf51-3ab2-a3e2-8654e900b1b3 | -10.07004 | -36.34511 | 2025-01-24 02:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fe2cb9f9-3dd3-3169-8b13-92ef1b3710e2 | -10.06737 | -36.34502 | 2025-01-24 02:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 551a47c4-a8b0-3f85-9c86-c3a31a7da206 | -9.41861 | -35.93275 | 2025-01-24 02:53:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4839d83f-1277-33a0-932a-c294a759cd94 | -9.42131 | -35.92918 | 2025-01-24 02:53:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 340c86e9-baec-3163-9ce0-9aa6849e08b8 | -10.06849 | -36.33929 | 2025-01-24 02:53:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6590bd27-5195-3edc-b9a3-be43eb0134b9 | -9.42023 | -35.93483 | 2025-01-24 02:53:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |


[Clique aqui para ver as próximas entradas](README2.md)
