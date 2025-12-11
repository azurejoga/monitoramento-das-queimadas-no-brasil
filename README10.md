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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7967e9a8-09b8-3aa7-accb-73de6af5d55a | -5.35371 | -39.71079 | 2025-12-11 04:18:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2657809-5136-3171-83e8-680754da0c83 | -5.13656 | -37.6884 | 2025-12-11 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ec45d07-f8e3-312d-9730-6e687172c4b7 | -1.57279 | -53.12262 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a98d81b-1d78-307e-b389-058b2484b5c4 | -3.75582 | -45.4904 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fa2f8d98-350c-3e77-b878-f6fa4b2c5c9a | -1.59026 | -53.7636 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a691200e-f6a1-390f-a392-91168d30cefd | -4.20572 | -44.4744 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12299a11-bd64-3a5c-9874-f10b5c1fd187 | -1.59398 | -53.76285 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b224238a-8140-33eb-b5ac-4ae4b5a6604d | -2.21001 | -51.89849 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90cfb209-7159-345c-b3b3-bf99f4894678 | -3.75809 | -45.49908 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 183d34b8-f53e-3cb3-8015-ebf0206244b0 | -3.84613 | -47.82879 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed07834e-f9ba-3144-b89f-d0c9c14f5316 | -6.02206 | -43.70776 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 157719b0-da14-34c0-9704-82084f7b875d | -3.40517 | -44.17312 | 2025-12-11 04:18:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40b63b91-141a-30ca-9950-924c9320d01a | -2.69548 | -51.64766 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 397de8aa-1abf-3f91-b6b0-1bbc4b5cba99 | -5.24452 | -35.48239 | 2025-12-11 04:18:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c1130f1b-5699-38c5-b886-a9774905234a | -5.59785 | -44.37595 | 2025-12-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00b5b000-cadb-3a5b-8aea-5174f01e9993 | -3.34481 | -46.21638 | 2025-12-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 429fad6b-1bae-3d17-95b2-6be7c17d7dc2 | -6.94453 | -38.61751 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8d3b92a-3c01-3d74-85a9-96d157cc681b | -4.87075 | -45.53949 | 2025-12-11 04:18:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8daa0d4-e076-3185-b337-be1b63ce86cb | -3.23076 | -47.47224 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d8d9bee-af6f-3766-88e2-299fbda2c728 | -3.95797 | -41.51986 | 2025-12-11 04:18:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 38483777-7176-344f-90f1-fb3fb5b586e6 | -2.02613 | -52.05102 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7246c75-89bb-37cd-a41f-35c56ed7c927 | -6.28446 | -39.88528 | 2025-12-11 04:18:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7bafdcb6-7b8f-333c-bf20-ee508db0e35c | -2.08128 | -52.05192 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90777410-fa44-3f71-a896-01703b3c0fc7 | -6.43351 | -39.13703 | 2025-12-11 04:18:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0f4edfb3-2f6c-39b4-9909-06b5a8b65891 | -4.46048 | -44.95041 | 2025-12-11 04:18:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd5f9cdb-a601-31a1-b8ff-6ba8dc5b23f6 | -5.1606 | -37.69577 | 2025-12-11 04:18:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2daa943c-281b-35ce-ace7-4c7f8e9be260 | -6.1917 | -44.61821 | 2025-12-11 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd536f75-d985-321a-ba93-3b7b0ef179b4 | -3.25489 | -46.41483 | 2025-12-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9acc4e9d-f512-33a6-88f3-8d6d8a021841 | -2.21615 | -51.89576 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d76c0c35-3d43-3928-bfa0-94acf7a77555 | -3.48374 | -51.53439 | 2025-12-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8bff563-15d2-3d3b-b85e-3a60cb7ff617 | -6.9068 | -38.0989 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e46cc03d-c2ea-3aaf-8f78-327ec4ed1b13 | -3.18331 | -48.03075 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14b566f9-8838-3f38-9955-49e4f7884791 | -5.32476 | -40.54879 | 2025-12-11 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db58968c-50b4-319c-912e-704124360c91 | -2.21422 | -51.8978 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 913d26e0-67d8-3ca1-a51b-c7468c1a416e | -6.03196 | -44.32736 | 2025-12-11 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eb3d691-6d0a-3a71-880d-ddaa82807841 | -3.79089 | -42.60182 | 2025-12-11 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6be8f5ae-013d-368b-9ba0-be743eb5a05e | -3.22373 | -45.29896 | 2025-12-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce63a144-6640-3e03-ab61-b0f69eb4b253 | -2.69665 | -51.64723 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70de5587-09a8-3c71-852b-2d65fb8a65b5 | -2.85131 | -45.80101 | 2025-12-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6280b02f-ac77-358b-b713-675834ac5326 | -4.41971 | -44.79731 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 373e442e-3ed7-3a64-9eb1-6c01b6553c12 | -3.39502 | -45.41923 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb5f2ec8-6795-3ff0-bf4f-e84aa1ac8cdc | -4.27334 | -42.1819 | 2025-12-11 04:18:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7de52c9-89c8-3890-8a51-9278923b9bfe | -7.62713 | -39.0714 | 2025-12-11 04:18:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b3d5824-e22a-3046-98e7-b1665349f329 | -5.01019 | -41.28919 | 2025-12-11 04:18:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e82a86bd-e9a3-3677-aa08-c760e0d8b1bd | -1.58772 | -53.76145 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88ce7375-2ae3-3530-b75a-ce5607cf852e | -6.02872 | -43.70882 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15d5e0d3-4d61-3eb5-84ef-40581421ea9d | -4.41566 | -44.8005 | 2025-12-11 04:18:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2d6a230a-7731-30be-b6df-f262b095582d | -5.57848 | -43.75177 | 2025-12-11 04:18:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee4e6f5f-fd54-3ee2-b75f-fea1871f375c | -7.56913 | -49.40094 | 2025-12-11 04:18:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8a72a06-5fd4-3105-b6d6-4a2523e82dfe | -2.65159 | -51.64374 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff9eac94-e9ea-31cc-804b-641971f077c2 | -6.43617 | -39.1356 | 2025-12-11 04:18:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed68e5be-e22b-3ae2-b0ca-b3d5f35e98dc | -5.6785 | -39.7332 | 2025-12-11 04:18:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e00156b-f6b2-388b-a16f-3ad5f7c911ed | -7.86494 | -38.72945 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1681bd3f-3be7-3812-9ddc-b7b5b14e2322 | -3.09114 | -44.89029 | 2025-12-11 04:18:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3a06c2e-ba26-3cd1-a151-d99e05789737 | -3.52512 | -47.20643 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a14eed81-11f5-3a56-a79a-3a82a171dd37 | -7.62732 | -39.06441 | 2025-12-11 04:18:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 148b336e-1f5c-387e-bdc8-17e90c8c7480 | -7.62785 | -39.06643 | 2025-12-11 04:18:00 | NPP-375D | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c91c6b8-9627-3529-bd6d-b4dce830c0de | -1.11579 | -53.69011 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d193cb48-4761-36a8-b736-ff7f43bbbeec | -3.48849 | -51.53854 | 2025-12-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b0bd45-a599-3b39-8c76-da4dcc2c0e03 | -2.93747 | -53.02756 | 2025-12-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2275878-27ef-3e3f-9825-4c44f12dea6a | -1.57188 | -53.12586 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65069b4b-dac6-3bf3-b383-3096d55ef126 | -3.54367 | -45.46315 | 2025-12-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3227e606-1bb1-32f4-9d9f-30c0d611f7e6 | -6.22974 | -44.16565 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0041f50-f761-31b1-80d5-dae0edc564d8 | -2.08355 | -48.37058 | 2025-12-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da0040f-fd56-344c-9fd2-4390bc0d7ec9 | -8.23238 | -37.75347 | 2025-12-11 04:18:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30852543-9b2b-3704-84b2-560aca8b5315 | -3.2594 | -46.41096 | 2025-12-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2380db8e-3bc3-3ece-9385-6ae46a651aca | -2.30028 | -49.31208 | 2025-12-11 04:18:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ca0a020-ff6d-381d-bad7-8aad64a29638 | -3.59947 | -47.53121 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d2f5ed6-3065-3433-9992-4a0c20edd0b1 | -4.93929 | -43.95747 | 2025-12-11 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e04708-7fe1-3a1f-b22b-dcbfc794ba24 | -3.17975 | -48.02936 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46747b1b-2c63-3647-8a59-9c361bf14128 | -5.98945 | -44.59339 | 2025-12-11 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fad94733-9b92-332c-8185-23a59dc1c879 | -2.0205 | -52.05016 | 2025-12-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04e0444c-4fb7-3c7e-b43f-c936e7a9e3e0 | -2.65216 | -51.64029 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5baa9570-6338-398f-951a-c8dc7c513376 | -3.84318 | -47.82104 | 2025-12-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5616e9f-b3de-3736-aae8-8e33d38717e5 | -1.30715 | -53.48605 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d29e6f8e-536a-3647-b63e-ff6826b28bc7 | -2.31385 | -46.48111 | 2025-12-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b381f3d-7bc2-3561-8500-5eb6eaf902aa | -4.93593 | -43.95694 | 2025-12-11 04:18:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0385681a-3018-3d5d-8265-387c108590db | -6.02262 | -43.70427 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ebe260-6b61-3dae-a416-3eabf0df9156 | -7.86571 | -38.72429 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b46f5fde-6d50-3ff9-9fb3-82533db00825 | -4.46144 | -41.93655 | 2025-12-11 04:18:00 | NPP-375D | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8cfe34c4-b502-3c50-b2ff-e35f07e452e9 | -2.2106 | -51.89484 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 385b8aea-8501-3b0d-97e0-aedf1e09a4a3 | -3.67225 | -45.77729 | 2025-12-11 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7041c9a0-67f8-3df8-ba4f-ebb95a8bf492 | -5.55899 | -43.80975 | 2025-12-11 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ada78b06-27bb-38f1-9ee9-6735fedf13fe | -4.39305 | -45.4094 | 2025-12-11 04:18:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 64f7d93d-c94a-3184-ba95-81b74f515e7d | -3.73708 | -48.89154 | 2025-12-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 895c70d0-04ae-3eb6-b717-9547a4452d3f | -3.52119 | -47.20565 | 2025-12-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73c9ec79-98ac-30f8-8065-2f77dfbd1ba2 | -3.49521 | -44.89233 | 2025-12-11 04:18:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddd4a805-5c60-39f2-b8f2-7e7d6c9cfc87 | -3.34927 | -46.21245 | 2025-12-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a58ab6b-5fba-34a0-a5d4-e7bdd09b9466 | -6.02595 | -43.7048 | 2025-12-11 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 44caf5ad-779e-32d7-a9ec-4534f4cc963e | -5.00029 | -44.55343 | 2025-12-11 04:18:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfe00646-3f88-3101-9cab-152bcd78a160 | -3.26245 | -46.4161 | 2025-12-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1ea778-dde0-3e6c-b8df-8f31a55a4151 | -3.75874 | -45.49503 | 2025-12-11 04:18:00 | NPP-375D | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 544afadf-0f9f-38c0-b1fc-0ea35c44a6b8 | -1.11493 | -53.69532 | 2025-12-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c098d2c-53be-301d-824b-befb21cde17a | -3.0415 | -50.48873 | 2025-12-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2390787-c692-38a9-ba72-c704b38c1f5f | -6.93737 | -38.61134 | 2025-12-11 04:18:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6fb5c325-afa6-32c8-8cd2-8441ff833370 | -3.44882 | -44.72871 | 2025-12-11 04:18:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb64eeed-c5ae-3d80-bfd0-22492ac0d445 | -6.74088 | -35.01543 | 2025-12-11 04:18:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8c526963-7b16-3ecc-9009-03307111e7ec | -5.58777 | -46.82286 | 2025-12-11 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cf5b05c-8494-3db2-925e-284941597812 | -2.77383 | -45.51741 | 2025-12-11 04:18:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c60192a4-3b5b-3ebb-8d30-69409e537884 | -1.5787 | -53.12228 | 2025-12-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
