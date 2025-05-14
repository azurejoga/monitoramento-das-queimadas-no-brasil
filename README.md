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
| 5ae5927c-1167-3c69-80d7-690c3bee9d93 | -13.9713 | -56.7874 | 2025-05-14 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 14662cec-f248-3ca0-8aa6-82cdfc934cef | -13.9521 | -56.7893 | 2025-05-14 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 584519ff-1908-32a6-8364-9d5cbd1c0d70 | -13.9713 | -56.7874 | 2025-05-14 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ff581fbd-1371-3ac0-9188-6fc6b1a3ad4b | -13.9713 | -56.7874 | 2025-05-14 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c9a228c7-c1f1-381e-85f5-68c38818bd8f | -13.9521 | -56.7893 | 2025-05-14 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8b5dc508-9b00-326c-a9de-32a31e6f04d4 | -13.9521 | -56.7893 | 2025-05-14 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f1b93882-efba-344b-9bb6-8acd17e9c034 | -13.9713 | -56.7874 | 2025-05-14 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 16765d8f-c783-392e-9a89-9afdfb3d0618 | -13.9713 | -56.7874 | 2025-05-14 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a385ef2a-f46d-3a12-b67d-aeba6040289d | -13.9521 | -56.7893 | 2025-05-14 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 291535b2-d37f-35ce-82d4-b68ce133b1f3 | -12.1626 | -48.007801 | 2025-05-14 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 472f8a66-713d-3297-9abc-0e7c5e6759d9 | -10.4939 | -49.151199 | 2025-05-14 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d63e0d4b-7992-3edf-a772-8cc1ea09e390 | -6.6633 | -41.994999 | 2025-05-14 00:41:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7fb6298-62a9-3c81-b64e-77efbf015cbf | -11.8005 | -47.370201 | 2025-05-14 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50fc6fff-ae97-34c9-8e74-6249091317dc | -20.825899 | -49.7841 | 2025-05-14 00:41:00 | METOP-C | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5032b78c-135a-37b8-bf10-22b15844a534 | -13.5723 | -52.865799 | 2025-05-14 00:41:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 751f1e61-2fea-31c9-ac76-7fbfa2171dc6 | -21.600901 | -56.029499 | 2025-05-14 00:41:00 | METOP-C | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 94352a8b-b005-3c0f-8e21-e8d8e3d9ce60 | -11.1711 | -48.681999 | 2025-05-14 00:41:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abd12b38-6897-321a-bdd5-a0d8c709e048 | -11.6434 | -48.127499 | 2025-05-14 00:41:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3119a09-7167-3804-bf1f-04dc53b8407b | -13.054 | -53.719799 | 2025-05-14 00:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 049027f9-3011-3899-a0c7-5b9f15979d8f | -16.048201 | -43.8069 | 2025-05-14 00:41:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5958ec-b58d-3ad3-b701-e54ffbb3955c | -13.0687 | -52.0149 | 2025-05-14 00:41:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53c99781-8155-3338-96c5-140b20e18760 | -11.8046 | -44.271801 | 2025-05-14 00:41:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01a2e16f-1f9b-36ca-94f9-febb8fa390c7 | -11.5801 | -47.443901 | 2025-05-14 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 638dc499-5cde-3ac4-9b45-614c7577f2ee | -12.1641 | -48.014801 | 2025-05-14 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1af6c59f-4d41-34f6-a593-933ded3f496e | -13.0442 | -53.721802 | 2025-05-14 00:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7881159-e218-310d-8365-6c7e00d94674 | -13.952 | -56.7929 | 2025-05-14 00:41:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f47b9654-4ab4-3885-8386-078aae33eddb | -9.2705 | -50.214901 | 2025-05-14 00:41:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18c4c771-4ce3-3479-8b8e-4f22bd8fa178 | -10.0127 | -47.851398 | 2025-05-14 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| acace083-de20-3adf-b167-bf2fc36665de | -11.7989 | -47.363201 | 2025-05-14 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 087548bd-3a71-30cf-a0ac-0190358bf939 | -11.8068 | -44.280899 | 2025-05-14 00:41:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb01a2b4-254b-3ef3-b65c-167c865189ea | -13.9617 | -56.791 | 2025-05-14 00:41:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee5c6f73-58d6-3f24-8bad-6be8b4ca0efb | -22.2209 | -48.637199 | 2025-05-14 00:41:00 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b01cee6f-ff56-341c-9c24-198b6d4292a9 | -13.6104 | -47.391399 | 2025-05-14 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57e26798-d00f-3e39-adcd-5d35dd7d0af9 | -11.5817 | -47.450901 | 2025-05-14 00:41:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6303c4d5-e4da-393f-9993-f6360248fcab | -16.046101 | -43.798199 | 2025-05-14 00:41:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bbf852db-3dd2-3b3a-892f-7e3983faafae | -10.0111 | -47.844501 | 2025-05-14 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8698b349-b344-37c7-b05b-d98da4284acd | -11.8143 | -44.269402 | 2025-05-14 00:41:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 430c7af9-e521-31a8-b2c0-6cb79d51a731 | -16.050301 | -43.815498 | 2025-05-14 00:41:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 308df09d-297a-33f7-b7fc-81f34b78114b | -13.5625 | -52.867802 | 2025-05-14 00:41:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4284eff6-dc91-3f89-8849-ec38f7b684b0 | -13.6088 | -47.384399 | 2025-05-14 00:41:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d53b5ea0-e86e-323e-8e24-5bd9af4a84e8 | -11.6418 | -48.120602 | 2025-05-14 00:41:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c407b60-e3ab-3dac-af9c-490c3f6c3c30 | -11.6965 | -48.819401 | 2025-05-14 00:41:00 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db1a2190-566b-3db2-b30b-a4bea710947e | -13.958 | -56.771099 | 2025-05-14 00:41:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a445d70f-600b-3591-91ab-98461b8f2ccb | -13.6807 | -53.950401 | 2025-05-14 00:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c36c956e-704c-35a7-a162-e52a57c5c48c | -13.9483 | -56.772999 | 2025-05-14 00:41:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32d13530-9fbc-32c1-bf73-f44a363e04be | -7.8149 | -49.333698 | 2025-05-14 00:41:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc90898-5ec1-3f27-91be-6fbe1e10c2f4 | -13.0707 | -52.024399 | 2025-05-14 00:41:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e622da7c-7b91-3267-bebe-cb50107ff8ad | -13.5647 | -52.878502 | 2025-05-14 00:41:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72fc8748-646f-33e8-8084-04461f0b1bcd | -10.4923 | -49.144199 | 2025-05-14 00:41:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82d6c7d6-80de-38d9-9bb1-7a92310716fc | -14.6386 | -45.097301 | 2025-05-14 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b856d99-a37a-3127-9caa-43ece0fe292f | -13.555 | -52.8806 | 2025-05-14 00:41:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c66e5c0d-5d4a-31ed-8556-2d35db5f9fcb | -20.827801 | -49.793301 | 2025-05-14 00:41:00 | METOP-C | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f322a74d-301d-3388-b721-4c23b73f7594 | -10.0095 | -47.837502 | 2025-05-14 00:41:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46521bdb-9ad9-362d-9ffc-d466b212e203 | -11.6336 | -48.129799 | 2025-05-14 00:41:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5d0054a-6d3a-3e2b-8398-0462294fecee | -8.809 | -49.810299 | 2025-05-14 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2efc7acb-123c-3913-aafd-5d1b84e5f6c3 | -10.188 | -48.030998 | 2025-05-14 00:41:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21c3ad2d-ee00-35bd-b2bc-8093dbed06cd | -12.1543 | -48.017101 | 2025-05-14 00:41:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98980cdd-bd0d-3a88-a894-59e1438655e4 | -7.9076 | -44.4799 | 2025-05-14 00:41:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2a060ad-7a22-39fe-a23d-9e55a7176b11 | -14.6404 | -45.105099 | 2025-05-14 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c278027-b12d-3eef-9e33-5be9e12fff97 | -6.9662 | -47.929501 | 2025-05-14 00:41:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d453295-8fbd-3b30-9c88-6feb2f080c5f | -9.5795 | -49.116501 | 2025-05-14 00:41:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99e7480d-b61f-3387-90c3-731c7c5ff52e | -8.8106 | -49.817299 | 2025-05-14 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7afb682b-d455-30c6-9edb-f3c37c54365d | -22.219101 | -48.6287 | 2025-05-14 00:41:00 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb2c5616-4936-305f-b9a7-f07174b1074f | -9.5779 | -49.1096 | 2025-05-14 00:41:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cf902b4-01d6-38a1-8d23-eab74e7ade7b | -11.8021 | -47.3773 | 2025-05-14 00:41:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e63e4980-4d60-320d-a249-ddc4b907389e | -14.6422 | -45.1129 | 2025-05-14 00:41:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e693c9de-2d88-3f42-a1b3-4afbdeca2c05 | -11.632 | -48.122898 | 2025-05-14 00:41:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99d1ad56-cc02-3fae-9ae1-9d60e6e1702e | -13.5572 | -52.891399 | 2025-05-14 00:41:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52f7648f-e55f-3c12-bb94-613230f3445c | -8.7218 | -50.2467 | 2025-05-14 00:41:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427b1a01-ae9b-32b3-a017-c5335fc43b36 | -13.6781 | -53.937698 | 2025-05-14 00:41:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 967da22f-7b88-3ce5-aef7-20022136aef4 | -13.9713 | -56.7874 | 2025-05-14 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3ee7f193-ef0f-39a3-bc0a-eb105483afac | -22.21881 | -48.62495 | 2025-05-14 00:50:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 471e49c0-0749-3f29-b0f6-4df2ba5a5d87 | -22.22011 | -48.63448 | 2025-05-14 00:50:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 7969a048-99f9-3506-8aa4-ae51de5065d7 | -21.60215 | -56.0502 | 2025-05-14 00:52:00 | TERRA_M-M | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7aa113ee-c62c-36d4-aba1-a041c6f9428f | -21.60963 | -56.04263 | 2025-05-14 00:52:00 | TERRA_M-M | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 60c4e38a-9c39-35fe-b5d7-bb42e02b40db | -14.8759 | -45.11647 | 2025-05-14 00:52:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 70dbb8fb-c9db-3e26-8006-595f16e2daaa | -14.63326 | -45.11565 | 2025-05-14 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 098d1468-de55-303d-9749-7e4e0ca4ac1d | -15.25766 | -51.45896 | 2025-05-14 00:52:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ff38c79-f8f2-3535-b843-165716d4c4b2 | -20.82078 | -49.79078 | 2025-05-14 00:52:00 | TERRA_M-M | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| c1f0f717-bc56-3bb6-9dc9-74525e1faa4c | -14.63081 | -45.10043 | 2025-05-14 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 47f2164e-df08-3fec-969d-ef3700adeeb4 | -21.664 | -48.81546 | 2025-05-14 00:52:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ee439979-54b7-3a1a-a169-b9aba9e7c0e5 | -13.55994 | -52.87621 | 2025-05-14 00:54:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 27df248c-c40e-3f32-b04f-a4efb4b8cfe7 | -12.14915 | -48.01953 | 2025-05-14 00:54:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 448d473e-4e76-313a-a092-e5b1f6fd6cc3 | -9.26712 | -50.21978 | 2025-05-14 00:54:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 504885ac-df2f-30cc-9f00-7bc17a790ae1 | -11.79694 | -47.37015 | 2025-05-14 00:54:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 20a583a2-9a09-3146-a8fc-d2b355f4dd55 | -8.80384 | -49.81699 | 2025-05-14 00:54:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 4e9ddd20-ece1-3416-972f-2399309782c9 | -12.50397 | -57.21651 | 2025-05-14 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| a364c049-3d3d-3b58-8750-dd7201acfc2f | -11.79607 | -44.26489 | 2025-05-14 00:54:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a09bb33b-f27f-3e21-8b03-6fd82ee453bf | -10.18503 | -48.03289 | 2025-05-14 00:54:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 84382bd0-9351-318f-9bf6-e0f26da43001 | -10.01244 | -47.83925 | 2025-05-14 00:54:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fb5ebc08-21a7-3492-a2d4-ea68bef1af49 | -10.48758 | -49.14569 | 2025-05-14 00:54:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 75cbd9d0-e33b-3ed5-91dc-5ff981c97b04 | -13.67671 | -53.94656 | 2025-05-14 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d2e37729-1d21-3961-958e-eb6507899aa7 | -13.05715 | -53.72165 | 2025-05-14 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c76bb1ec-5481-3740-9bcf-cea7bbfd8b8b | -13.98062 | -56.81173 | 2025-05-14 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d97bf4b6-afe3-34c2-a08f-55ce73bdf527 | -12.72577 | -54.9645 | 2025-05-14 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 15a97922-899d-3e79-8642-c13203f1efab | -13.06067 | -52.02135 | 2025-05-14 00:54:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1bb36021-ddf8-38f9-8034-575040a1abfe | -12.1587 | -48.01806 | 2025-05-14 00:54:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 5c1034b2-422d-3238-9ee0-051a37aaf126 | -9.57808 | -49.11699 | 2025-05-14 00:54:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 379e93a0-b53b-3196-906a-0e65768a2fef | -9.57662 | -49.10707 | 2025-05-14 00:54:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 52eb6036-377d-3786-b232-fc86756809a9 | -11.57298 | -47.44799 | 2025-05-14 00:54:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README2.md)
