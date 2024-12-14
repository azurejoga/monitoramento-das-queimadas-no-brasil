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
| 6aa5bf74-ee22-300e-bd4e-8fdac2e3a8dd | -8.30739 | -35.35671 | 2024-12-14 03:38:00 | NOAA-21 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 99fe2081-dd57-3bcd-9bbe-78db7b308df5 | -6.03818 | -44.04477 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be54bc50-b11c-316e-a587-edb82320082c | -8.65481 | -36.91058 | 2024-12-14 03:38:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5352e757-58ff-378c-9103-26b689fe953d | -5.53664 | -42.85226 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 378007b4-fa52-3eea-9a28-88fc8a456841 | -9.21401 | -36.4552 | 2024-12-14 03:38:00 | NOAA-21 | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fb74ce89-c062-36a0-8c42-733b5f2302e0 | -5.96801 | -40.44128 | 2024-12-14 03:38:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 45d1f5fd-a0ea-3fbb-91de-0aceaa5ac436 | -5.05374 | -42.61668 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 414527da-8e3c-3785-89cd-6980f91862b0 | -5.54078 | -42.86024 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d30f680e-dc66-3134-adb0-d124f5efbd3b | -6.92997 | -42.848 | 2024-12-14 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b53ce4a2-e02d-3507-9266-8d08fe28f772 | -7.19989 | -38.4161 | 2024-12-14 03:38:00 | NOAA-21 | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ad9d32a-0634-39bf-9c1b-2e7427a8603c | -7.15014 | -37.94378 | 2024-12-14 03:38:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79818b32-86ef-3546-b0cd-b2c5f7df3205 | -5.04364 | -43.21581 | 2024-12-14 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a696670-d948-340d-a2c0-b8270f519ee0 | -6.29131 | -37.24312 | 2024-12-14 03:38:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aea427dc-e044-380a-b0f5-c9e7b9a95cf4 | -7.99489 | -39.42698 | 2024-12-14 03:38:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0995ce04-9989-3e38-b75b-a7fdccfc0ea9 | -4.93919 | -44.07082 | 2024-12-14 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e389ad21-5535-3da1-9779-06519416649f | -9.04287 | -35.35198 | 2024-12-14 03:38:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 066834ce-708e-3733-b2d3-e692803b9a39 | -12.69865 | -38.18985 | 2024-12-14 03:38:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4b46ac9-9d4b-34ee-a15d-fcf5f93873df | -12.70151 | -38.19458 | 2024-12-14 03:38:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd0fad6d-e352-3e75-9720-814a4b94f21f | -7.9328 | -35.2494 | 2024-12-14 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a38773c1-099f-33e4-ae90-dd45e042fde9 | -6.52134 | -41.28199 | 2024-12-14 03:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c118de94-63dc-37d9-85fa-bc048828cc83 | -6.51099 | -41.28558 | 2024-12-14 03:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 69506572-5aed-39d3-b58b-3b9d443c7c8b | -6.04468 | -44.04145 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 55383344-664d-39ad-8ffa-464e342ec522 | -6.62596 | -38.42392 | 2024-12-14 03:38:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a093f82-f8c3-3aa1-92f6-78f68acdb50a | -7.66675 | -35.01847 | 2024-12-14 03:38:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c85e4404-386c-34f0-be7f-41ff68ee657b | -6.51573 | -41.28632 | 2024-12-14 03:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 95d17497-fdb6-3a6f-abed-6ad3afecac14 | -5.53486 | -42.86266 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b459b365-c576-3739-b34e-8914c5b13a80 | -5.96582 | -40.44286 | 2024-12-14 03:38:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f50d7a78-bfc8-366e-b999-3f24e2f201e6 | -7.93223 | -35.25296 | 2024-12-14 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 74d1820d-29fc-35e8-a642-bb80ceaa3fb2 | -8.13313 | -38.2515 | 2024-12-14 03:38:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 565e20da-190b-38f1-a09d-c14770c02852 | -5.53605 | -42.8557 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bdcac910-3c79-3587-b669-b8e833ad1bc2 | -6.52608 | -41.28275 | 2024-12-14 03:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 40325adc-c5a6-35ac-8e56-a2206c967a47 | -6.03961 | -44.03675 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 76fa987d-546e-38b3-9cfc-f4ed3f3e93c6 | -7.15095 | -37.94199 | 2024-12-14 03:38:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2cff1d6-50a7-3fd4-b799-cbf3579f4405 | -7.99425 | -39.43067 | 2024-12-14 03:38:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d070307-7804-3a20-9935-0f40fe0d1f83 | -9.00641 | -35.23761 | 2024-12-14 03:38:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| edd0c4fd-2a35-3eae-8dc0-f74ed27f4568 | -9.21341 | -36.45898 | 2024-12-14 03:38:00 | NOAA-21 | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c3e752cb-136d-312c-94a3-c25579d2595d | -10.00849 | -37.68897 | 2024-12-14 03:38:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1daebc4-291e-3ec3-b311-fb684c71f78d | -5.05767 | -42.61799 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d4fe378-540a-3b58-bff7-1ec90bd61e7b | -5.05903 | -42.61762 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f524a072-1d5d-321f-853e-297636e00319 | -11.4837 | -37.92065 | 2024-12-14 03:38:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c3bb12b-cc98-31e2-8a82-6fb1e7c364a6 | -7.89135 | -42.44435 | 2024-12-14 03:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6eb2cf05-f2b8-3535-ac22-b8dc9958edf1 | -8.42009 | -45.1304 | 2024-12-14 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3bfd3a3-550c-335f-8f5a-8ff447e1b234 | -9.21682 | -36.45958 | 2024-12-14 03:38:00 | NOAA-21 | LAGOA DO OURO | PERNAMBUCO | Brasil | 2608602 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2afc5fb1-a082-36ab-acc2-3e1dc4f7f37b | -6.0389 | -44.04073 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2c6926d4-8f9c-3404-b55e-5f30667a70c1 | -9.28338 | -40.17614 | 2024-12-14 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 16ffe6d7-9928-3c78-9759-dc10b650ef95 | -6.93054 | -42.84475 | 2024-12-14 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1951c6e0-bcfd-379c-9e2b-7aa64ae5dbc1 | -6.08803 | -37.6207 | 2024-12-14 03:38:00 | NOAA-21 | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d9bc8abb-611d-3762-9158-92c37af497ce | -5.05958 | -42.61433 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5515918-725c-3954-9810-e8ae04f879a7 | -7.89115 | -42.44569 | 2024-12-14 03:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90634a96-4b93-31bc-8477-82769cb4dd6e | -8.21632 | -40.6021 | 2024-12-14 03:38:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3802e03a-1700-314f-8aed-f553a233c589 | -8.30405 | -35.35617 | 2024-12-14 03:38:00 | NOAA-21 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0ee2079-c546-38eb-823d-64c5e0f15f08 | -11.7976 | -37.97574 | 2024-12-14 03:38:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4df7fb09-8161-3662-b16d-26e041f6a24c | -6.7793 | -38.32829 | 2024-12-14 03:38:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0fdab0db-da9b-36a5-b890-c86b6bb4c900 | -8.07482 | -34.97618 | 2024-12-14 03:38:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3000703b-3a34-31e9-a3a9-63d52743f5a5 | -5.53546 | -42.85918 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e6573205-f84d-3063-98cc-e114f930cab4 | -9.04343 | -35.34845 | 2024-12-14 03:38:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ef15410b-43c8-3b02-857a-c73418caa0cd | -6.04394 | -44.04559 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2314f6ed-5c6e-3858-94af-89dcf31adf5b | -7.88672 | -38.73844 | 2024-12-14 03:38:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f645cf3e-bd25-39b9-b483-cbbd504c5a97 | -5.05238 | -42.61704 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc2da47c-9912-376a-8ceb-b6acd09bf5de | -7.69916 | -37.53782 | 2024-12-14 03:38:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a215861c-e6a7-31f7-bddc-cdd70d50f46d | -6.9352 | -42.84885 | 2024-12-14 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7ba0ec7-46ef-3139-8156-ee5b8aee7c02 | -5.05317 | -42.62002 | 2024-12-14 03:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bbf460e-a51b-34c4-a105-a635267c5fc9 | -7.88619 | -42.44461 | 2024-12-14 03:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5caed5d2-8d7f-32e3-a75a-b9f748ed800d | -8.21596 | -40.60335 | 2024-12-14 03:38:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52572cda-2855-353a-9f93-ffdfc0ac82e2 | -11.49838 | -39.04782 | 2024-12-14 03:38:00 | NOAA-21 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcbdd94e-10d1-3832-978f-f01187206660 | -7.99553 | -39.42325 | 2024-12-14 03:38:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6254444d-ba2b-3b41-a3ee-4129273ff098 | -5.14474 | -44.19372 | 2024-12-14 03:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eb7618d-d876-3ab0-ad81-8e420db7ca4a | -9.2589 | -40.95592 | 2024-12-14 03:38:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92e12a09-81f8-3d0a-af3c-a388a9152144 | -11.80117 | -37.97633 | 2024-12-14 03:38:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d360e5c-0baa-39ec-81f1-aacbdf2aeb21 | -7.88669 | -42.44173 | 2024-12-14 03:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5de2be0f-5830-38d0-90bf-a8e140b35b09 | -9.2792 | -40.1754 | 2024-12-14 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e07deb9a-a8e6-3b90-8b90-da66a15a750c | -6.05043 | -44.04232 | 2024-12-14 03:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99a753fa-3b79-3022-9cff-cdc10a3e0d64 | -9.49078 | -35.61341 | 2024-12-14 03:38:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7988b73b-7f70-3f20-8c28-aac24b2ce4cf | -9.81579 | -39.15323 | 2024-12-14 03:38:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9210c3d1-e34a-3322-892d-ad44b4ab8b72 | -6.56331 | -39.11514 | 2024-12-14 03:38:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d594b49a-9dec-3f62-a115-d1977da9c3ec | -7.99833 | -39.43137 | 2024-12-14 03:38:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 78e37876-6fa4-3ce0-b173-f7757d5ce402 | -7.99896 | -39.42768 | 2024-12-14 03:38:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 431190a7-8b01-31ac-b6c6-8f18865fc7b7 | -9.0462 | -35.35252 | 2024-12-14 03:38:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 3636df98-7923-38ba-9f9e-f95d0771e7df | -12.5687 | -57.718 | 2024-12-14 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ca0b5dd3-8bff-33b3-ae79-45ff849bd332 | -13.1793 | -53.2791 | 2024-12-14 03:40:00 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 03af33d6-f761-358a-aa8a-b30631ed2a3a | -4.1057 | -46.6142 | 2024-12-14 03:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8e9cfde9-d9eb-3e80-895c-c994cd0680d8 | -12.5497 | -57.7196 | 2024-12-14 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ea83451f-0816-335b-bb3e-ad3fac4ffb32 | -1.7178 | -52.5553 | 2024-12-14 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 550b571b-4d1f-371e-b696-668c0cf30d6c | -12.5689 | -57.698 | 2024-12-14 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 917c28e0-84e1-3e0b-abf4-65ed29cf8e25 | -6.0472 | -44.0331 | 2024-12-14 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 95da0cae-4212-3ca3-828f-e463be927e69 | -12.5499 | -57.6996 | 2024-12-14 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6a2e390e-488d-36ad-a7f7-486fcd3e3fe6 | -13.61548 | -43.9785 | 2024-12-14 03:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbb1441e-d186-3e59-ad10-106a8b55bba2 | -16.92281 | -43.59867 | 2024-12-14 03:40:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d136aae-b585-35bb-83a2-4a7a6ebf1bd1 | -21.20812 | -42.83472 | 2024-12-14 03:42:00 | NOAA-21 | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d65d63d3-36ef-3589-b3f4-862bde514149 | -12.5497 | -57.7196 | 2024-12-14 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7fef48e3-ff3b-3319-8ab4-74ed36dafb83 | -12.5499 | -57.6996 | 2024-12-14 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 83ad1ab4-7b3a-3a11-ab69-36c8a4503e20 | -4.1057 | -46.6142 | 2024-12-14 03:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4a826d46-224e-3c9a-8c09-3a16b73d0e8b | -12.5687 | -57.718 | 2024-12-14 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 27f5449a-3b1f-347c-934a-a8862bfc09ee | -1.7178 | -52.5553 | 2024-12-14 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f5144fa1-fe77-3dd3-88b5-d408bb40c8d1 | -4.25002 | -41.92301 | 2024-12-14 03:59:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2497afab-a60b-3598-a2df-f058c83d7675 | -3.73035 | -39.95543 | 2024-12-14 03:59:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7bffce86-e474-3ce7-8578-5fc46f6d3526 | -3.25233 | -46.8497 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 19376926-ea48-33f3-a368-955f7e70d66a | -3.25476 | -46.85625 | 2024-12-14 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c27584f5-c311-3d07-82dc-299eafe58fdc | -4.52434 | -42.0733 | 2024-12-14 03:59:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02f0acbf-939d-3e4f-a7c6-f35fc0d30953 | -5.53515 | -42.86222 | 2024-12-14 03:59:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
