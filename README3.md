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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cec094b6-c58e-353d-b59a-5c2b7a157a40 | -2.07657 | -45.17637 | 2024-12-25 04:16:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64919212-9d4a-3082-8a00-ff1b4b240dbf | -4.86971 | -38.33466 | 2024-12-25 04:16:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 075c40ad-e010-380a-b5e1-bcbcbc74bf09 | -2.34077 | -53.88542 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2ff1e54-9de6-3981-8206-1f9dd508e8ec | -1.51756 | -54.95585 | 2024-12-25 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90543f0b-1069-3917-bc4b-9edd1024c0b2 | -3.79139 | -41.61055 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dff8b4e2-fc84-3da6-968a-b7d0c023f246 | -1.51136 | -54.9548 | 2024-12-25 04:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d68f8d60-a232-3eb1-947f-e840cce81be0 | -2.344 | -53.89228 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78fb863e-ae88-354f-a54a-1e55cf01ce22 | -1.83391 | -46.25123 | 2024-12-25 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 776cac2c-e25d-3488-89c3-4683593dc684 | -3.78383 | -41.61333 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85a39590-529a-32ae-b37e-c3da6fe00306 | -2.07319 | -45.17584 | 2024-12-25 04:16:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6843d7c6-6173-38fc-95f5-249c804ea5d1 | -2.94197 | -51.48422 | 2024-12-25 04:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91f0f4b0-15e9-3cab-b9cf-381283084f64 | -2.99292 | -45.67578 | 2024-12-25 04:16:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 304e484d-8870-3a52-8748-fb3555f428b7 | -3.78092 | -41.60897 | 2024-12-25 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1faa51b-d800-35c2-affe-3cb8a0885370 | -1.69549 | -52.61456 | 2024-12-25 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a21fc0c4-4ad9-3c16-a274-26ba17652da8 | -2.28824 | -53.6633 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb71e7e9-c1ca-31cb-9ddc-585ff26d9131 | -3.21469 | -42.08281 | 2024-12-25 04:16:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a8db397-8a1b-3cfe-b6c0-543f6caebb7e | -2.94553 | -51.48713 | 2024-12-25 04:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f0e796c-44f2-36cb-8bd2-81a5d4918229 | -3.22702 | -39.66721 | 2024-12-25 04:16:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2ffa582f-ac0c-3f96-9b4f-ce4fc002d107 | -1.69387 | -52.61538 | 2024-12-25 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d38eba8f-38d2-3d47-9790-18fd975d883e | -2.81586 | -45.93024 | 2024-12-25 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b521d227-b31d-306b-85b4-da3e99dc80e1 | -2.41273 | -54.23497 | 2024-12-25 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4af4ce35-96e1-3cdd-a30b-5e73a304628f | -2.31093 | -45.06892 | 2024-12-25 04:16:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1599a3-212e-3434-90c3-e8f6f5b15b05 | -3.9118 | -46.9322 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b0854a-1113-382a-8ea9-692e19bbb231 | -4.08931 | -46.79869 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5eb930f-2657-3502-9cb8-cf921d830d26 | -3.89768 | -46.99622 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b1156b0-8cd1-38b4-b829-42b11b80856a | -3.90424 | -46.98561 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 701b6fc0-aee6-3d3c-afb2-5fe6fc4d05dc | -4.00586 | -46.70984 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9069af0d-46de-3060-9be2-6285c23b08d9 | -2.84748 | -52.80326 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4c2695f1-2c94-3734-9952-7ce783af437c | -3.91317 | -46.929 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb04882-b08a-38e6-8c42-3e5d8e44c77a | -3.91088 | -46.92035 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46833733-1c6b-3bd2-b019-ff708ce5fe40 | -3.90125 | -46.99679 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51f44ce-9c04-3da0-aab4-a8ece2d28c76 | -3.91351 | -46.89935 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c19bbf23-cf8a-3e1d-9d04-e43546bd5002 | -3.91444 | -46.91602 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 302db2b4-ef5e-3121-ab13-9bba248bf725 | -5.47627 | -39.66301 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f0bc586-0587-315d-a42f-cc99363cb490 | -2.88257 | -52.5526 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5b20ff8-8131-3508-812f-d1d7505f7046 | -5.47489 | -39.66543 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1bde5b3-67bc-3146-8f3a-b313cd752f73 | -4.10376 | -46.8216 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4b3222b-b08c-3ef7-a8b8-4e307f6a366c | -4.11985 | -46.69844 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08a35ef4-1f60-3a74-809e-b67c9b38595d | -3.91575 | -46.90797 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c222d4-3acd-3c5c-859e-37ae7c7e32c0 | -3.90614 | -46.98925 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23009a0-5c44-35cd-8b2d-b9e6a161e64f | -3.8863 | -46.68732 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5dbdbc4-1fee-3fd8-98b2-d9131e578186 | -5.4754 | -39.66868 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7ac6582-f822-388f-b863-9c9c01e73452 | -3.91635 | -46.90885 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ce27e5d-60bf-37e2-a883-06425c5a16db | -4.05244 | -47.02778 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da55386c-38a1-3e7a-a450-5397d3bb681e | -3.1481 | -53.19073 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6f105082-d924-3e0c-ad1e-81989270ad5a | -4.03487 | -47.04575 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fcb5974-769f-392d-8bd8-241fc1fe0681 | -3.90231 | -46.99781 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dc2716e-583f-356e-a2e5-6c03e1c99be9 | -2.88336 | -52.5532 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c164b8c2-e28d-3879-92c5-f911eeeafc92 | -2.88387 | -52.5502 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95151f99-b7ab-3f78-a0f8-6fab08707cc5 | -3.5248 | -52.13374 | 2024-12-25 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b16e0ea-f263-3c84-9efe-966704ff2c71 | -4.02028 | -46.91064 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5431827-46b7-32a2-8ddf-198cc84bb3d4 | -3.91343 | -46.90423 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f341c7-0fee-3223-9dab-b47a48823088 | -2.85327 | -52.80103 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8baffa15-2e45-3a3f-82d5-3d19d1588aee | -4.04887 | -47.02716 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d671577b-d7b5-36e5-a85c-a771987269ba | -2.90905 | -52.38862 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61b337b-78c3-3e16-b994-7c8a6a62d0d4 | -3.05832 | -53.79541 | 2024-12-25 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c3fb04c-de90-32f0-b269-b5b6f7f332f4 | -3.15518 | -52.98488 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ee54f8f-990a-332d-a439-cd4f18f104dd | -3.91508 | -46.91691 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99db6003-1ab8-3ba2-874b-0de09ec00416 | -3.06393 | -53.79644 | 2024-12-25 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2db68466-8b10-3003-b17c-8a9e91b62589 | -5.9057 | -46.23022 | 2024-12-25 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50a441e5-2cb9-3cb7-bedc-852ef6212942 | -4.03977 | -47.03814 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475b3c40-8459-3e1a-8219-60bbf7466e75 | -4.10855 | -46.81435 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d81c222d-e798-3f4d-831e-026d5550bcb5 | -4.10311 | -46.82564 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e53847d-2597-395e-9204-e307db37e261 | -4.03911 | -47.04222 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 449416e4-0b99-3476-a5af-d11e0781500b | -2.84693 | -52.80017 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71b60736-c844-34d6-bd44-1d6490d40e24 | -4.04756 | -47.03529 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f92cb0-a759-344d-b80b-ae383e8810c8 | -4.03553 | -47.04164 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a8a69a-747f-36c8-a282-44af314ad8a6 | -5.48759 | -39.66154 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c6a2f34-1e99-3fca-9d72-c6ecd279a8e4 | -4.04334 | -47.03875 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d92779b-34d5-3b06-b0fc-bf9b4e876478 | -4.11857 | -46.70641 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ba23d1-4c7f-3b0e-ac4f-c80c9ae150c2 | -3.91286 | -46.90336 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b4c10d-307e-3799-8437-25a87e09deec | -3.91394 | -46.98639 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb4b2adb-2b7e-3b13-951f-c6a5cdec7db8 | -4.02497 | -46.90905 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76888dce-c4bf-30c4-a08e-584e9f44b760 | -2.90953 | -52.38566 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15118525-97c2-351f-8b7e-fa01f629b0ea | -4.34702 | -45.95688 | 2024-12-25 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afdac39c-aace-384f-8924-0226700dc9ff | -3.15043 | -52.98059 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f716e43-b47c-3828-88dc-87e1d5b52e8a | -3.43747 | -53.28957 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c697380-1d12-3f27-859d-374546bf7b14 | -3.99021 | -46.73985 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee8d7825-9a65-3959-ad6f-9044ae2af232 | -3.92105 | -46.98766 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 983981f7-b320-3b92-9fb1-852ee066ad44 | -4.04952 | -47.02311 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93938b90-07e5-31eb-8987-08c8d4005c5f | -3.91381 | -46.92495 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9752097-3f91-3b0c-9db9-1549d6c801db | -3.91114 | -46.89563 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfe95456-39a6-3bf2-83aa-52a3001f8419 | -5.47936 | -39.42743 | 2024-12-25 04:18:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d39614b1-a85e-3530-98c5-d921c3c936e8 | -3.90257 | -46.98868 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b355fab7-91e6-300f-b54c-ab8ad919ba6f | -3.91313 | -46.92404 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d44edde-06a9-3870-983c-58d7bf03043f | -3.90296 | -46.99373 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36da9bfd-20af-3a5b-a451-278cc1d57da8 | -3.89808 | -47.00142 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bf8f473-8b27-332f-8793-105623035071 | -3.91641 | -46.90392 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c49f6409-0fbd-30e9-bea1-8cd3512d15cd | -5.47887 | -39.66586 | 2024-12-25 04:18:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c415515f-adcb-3f14-bc9a-e62e222410b8 | -3.9218 | -46.93808 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eac83c3-1e53-3483-bf33-d7a258e08728 | -4.10344 | -46.64361 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60cb11ed-5fbf-3cc6-891a-7675b37968e1 | -4.04399 | -47.03467 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c972f6e-2997-3b44-95c3-1d0c5d99fd84 | -3.15385 | -52.1426 | 2024-12-25 04:18:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76e2a843-8325-3865-88c4-946ccd0d331f | -3.91252 | -46.93314 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e78354-2e51-36d4-9bee-e94418fecfeb | -4.10792 | -46.81829 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbdf36f2-193e-38ef-9b4c-e814807f14d3 | -2.85276 | -52.80415 | 2024-12-25 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05ff734a-9e7a-3df9-a09b-f6461f8aa98b | -3.4315 | -53.29201 | 2024-12-25 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe384e6-9ea0-39b0-a3bc-186d0c7f3a7d | -3.89874 | -46.99725 | 2024-12-25 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b899d509-9c8f-3aa4-9b22-da8d494f24de | -3.81215 | -46.72098 | 2024-12-25 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f0e6dba-7268-3af7-a54d-0d00f0e6e9fb | -3.94691 | -46.76138 | 2024-12-25 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
