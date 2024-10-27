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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a266d51c-aaba-35cc-97a6-aa32a0bc7bbc | -6.68908 | -40.89349 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7b0fdcb-d8e9-3e37-875b-6b5323c7186f | -6.68741 | -40.89058 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 214d1d10-5498-3c0e-aca0-869906e34fe2 | -6.68442 | -40.89264 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| abd3ec53-bded-3787-9355-d77012097570 | -6.6836 | -40.8975 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69fa91c4-e4f0-3df7-811c-ba2730ff2bc4 | -6.68196 | -40.90726 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d99401a9-5432-316e-9012-c192e3abde1e | -6.6819 | -40.89458 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 012bb143-66e0-38e5-af82-b1219433c745 | -6.68104 | -40.89943 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4193f81a-e615-3cbd-b51f-2ee01a80a59c | -6.68018 | -40.90429 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c0031251-501a-342e-8979-f603c90b65b9 | -6.67932 | -40.90922 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a918cea4-930d-346f-a39b-8b2d329fd030 | -6.67812 | -40.90152 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e1aa4d07-8f51-33ba-ab45-bc077a957bab | -6.67729 | -40.90642 | 2024-10-27 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 220330f4-5080-3843-a730-4ca70cbfd6b6 | -4.85184 | -42.46866 | 2024-10-27 03:36:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 99d328d2-1f51-34dc-8a23-be253c3dd8d8 | -4.42266 | -42.52119 | 2024-10-27 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05b2e476-6e65-302a-841d-b2090bce965b | -4.42207 | -42.52467 | 2024-10-27 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86476431-1dcd-372d-8b7f-9b99b2abf7f6 | -4.41664 | -42.52382 | 2024-10-27 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 937a0162-870f-3efa-bd23-3135b693d295 | -4.41605 | -42.52729 | 2024-10-27 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3a07cd2a-c74b-3dd8-a1eb-8bc9b374b6dc | -4.34072 | -43.03824 | 2024-10-27 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 44abd903-343f-3ae7-a42a-d0eced0cf01b | -4.34006 | -43.04215 | 2024-10-27 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8a959709-b842-3423-aff4-f93c538317da | -4.3351 | -43.03737 | 2024-10-27 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c35e4737-f366-390f-9717-9ce74f172ef8 | -6.60266 | -42.06882 | 2024-10-27 03:36:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3d80186-06a4-3077-9a21-9fd6def0bf6c | -6.59758 | -42.06798 | 2024-10-27 03:36:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f295e23-2e9b-3554-bb1d-aaeae08e4cc4 | -6.50735 | -42.35553 | 2024-10-27 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 22a7bc88-41dd-3144-ac81-bc7812e72935 | -6.50678 | -42.35881 | 2024-10-27 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 33a258fb-6743-3198-b1e9-30574813f239 | -6.50218 | -42.35459 | 2024-10-27 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3712d139-8e66-315b-9e4a-66f5538b3e94 | -5.97545 | -42.12313 | 2024-10-27 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 448c3b39-4cea-343d-97bd-a9dd643be293 | -5.97083 | -42.1193 | 2024-10-27 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 445fcf1a-883b-3479-9dd0-c2017ca8f525 | -5.9703 | -42.12231 | 2024-10-27 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28cbe710-d884-3de1-b051-435444dd4908 | -5.96978 | -42.12527 | 2024-10-27 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0f4f1c97-3232-318e-8865-128a3ba7cdee | -5.88703 | -42.56714 | 2024-10-27 03:36:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eab953be-b6fd-38ab-986d-ace5c4cb9b4e | -5.48248 | -43.3424 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ef2fc3b-b11a-37f3-9010-c5d20fb99da1 | -5.47907 | -43.3404 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe0ed792-c767-36a4-86ff-1781d7a45516 | -6.66745 | -43.54577 | 2024-10-27 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2b7f7a2f-51be-3923-a8e6-9f70f8e70071 | -6.9836 | -42.45022 | 2024-10-27 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0b06ce2d-3a51-3756-bd9f-e53b5d102794 | -3.06759 | -44.33378 | 2024-10-27 03:36:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9edd4fc7-d492-3e08-a2d0-0713334ed68e | -3.06677 | -44.33871 | 2024-10-27 03:36:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14e4f412-c6e1-38d6-b6b7-bf8453f17584 | -3.06606 | -44.3333 | 2024-10-27 03:36:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ba4c10c-5bb7-3dfa-8148-5b6c3537c2ce | -3.06521 | -44.33823 | 2024-10-27 03:36:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d008585f-2f8f-3214-aba9-fe7fa050eca8 | -4.71023 | -43.88017 | 2024-10-27 03:36:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9bae67f6-5c3a-322f-b778-63d4db90fb79 | -4.70949 | -43.88439 | 2024-10-27 03:36:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b45f4d2-20d4-32b5-b93e-84f72ca2691a | -4.70359 | -43.88346 | 2024-10-27 03:36:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5a64962c-df9f-3fd3-ac3b-e4856601255b | -4.15585 | -43.70701 | 2024-10-27 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 274a2d75-3d43-3a9c-a51b-e1d2b87dbf5a | -4.15519 | -43.70314 | 2024-10-27 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22b94d4e-ec6d-3d0a-ad27-0d76f0449ca6 | -4.15445 | -43.70737 | 2024-10-27 03:36:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e25692f-a41c-302d-9550-10f9adf8c19c | -5.73238 | -43.81429 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45316c26-e770-31dd-99b4-cc232e1488a5 | -5.73136 | -43.81716 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2013e0c-cdfe-34f8-82e7-2e198896bc28 | -5.7266 | -43.81335 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f430987f-9998-38df-8cb7-6c3801cf99eb | -5.72629 | -43.81215 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 361db0f7-f43c-34ed-a02b-0340542915e9 | -5.71633 | -43.83709 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 93278419-13f1-3ed1-9efd-bd2096042664 | -5.71558 | -43.84123 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fc7c4f2-98a2-324d-93f1-8d93a2a63b48 | -5.71549 | -43.84001 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eb9ad5ed-e6c7-38bd-9953-e83cf149f0d8 | -5.71483 | -43.84535 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| beceb635-bffd-3bc8-80bb-55ed6b547f2b | -5.71477 | -43.84414 | 2024-10-27 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 52e08c37-088b-3e65-9e9f-a6019afab26f | -5.4211 | -43.3737 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f18094c-3ff6-3961-b2cf-816c9c77be9d | -5.42044 | -43.37744 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a9d9249-3484-3765-a152-e03bf64d47fb | -5.41978 | -43.38121 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b7a21d9-35e5-3435-87e1-fe5811f269b1 | -5.41911 | -43.38497 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6067fae5-6bbb-37b6-99bb-b1222cd6649a | -5.41547 | -43.37271 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 686c29e7-920d-39a9-a98c-96d03667375a | -5.4148 | -43.37649 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ceb28342-80e2-330e-a6ec-25e008b3b63e | -5.20081 | -43.30222 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c00f0eb3-a2c6-3fa4-ab60-ffb9ceb51712 | -5.20013 | -43.30602 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8c202f2-5d5a-324e-90d7-556735a42228 | -5.19947 | -43.30978 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3b89609-ce21-35d0-a952-4ab833576c04 | -5.1988 | -43.31353 | 2024-10-27 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2762867d-9554-3d00-a67e-7a7df5f2c860 | -5.19384 | -43.30877 | 2024-10-27 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0bd76127-61c1-31d5-a37f-4be9d36b9abe | -6.37257 | -44.01517 | 2024-10-27 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd1c8a60-7d13-33d7-886e-42937ad6bd90 | -6.36687 | -44.01375 | 2024-10-27 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9ed4777-d4f8-377d-8bcd-3878f42cdf20 | -6.36613 | -44.01782 | 2024-10-27 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 538d00db-b8bb-3ee2-910b-f79aabb4a664 | -5.81371 | -44.12699 | 2024-10-27 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66e26479-9917-3c74-b301-7f3a1e13ca15 | -5.81295 | -44.13123 | 2024-10-27 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37f2790f-0c88-37b1-b73a-37b6da255b34 | -5.81217 | -44.13556 | 2024-10-27 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1725691-bd9f-3f57-9c07-50650e2e968d | -5.8078 | -44.12618 | 2024-10-27 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57dee0d6-13a5-3bcb-9600-f91ece02b2e6 | -5.80703 | -44.13042 | 2024-10-27 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2be7028-55fe-364a-a4e5-fc8fa01cdca1 | -5.62349 | -44.83105 | 2024-10-27 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7d53c5a8-00c8-3936-a690-6253e1e63155 | -5.62265 | -44.83578 | 2024-10-27 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4d048c07-914e-322a-b4d4-fb05c3220393 | -5.61731 | -44.83007 | 2024-10-27 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c18a624b-e40d-388e-afc6-e1ff147c3746 | -6.88264 | -44.76005 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45cbd965-2e99-33e9-8867-cd2c46c54e39 | -6.8767 | -44.75864 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a0fa29-0613-33c5-be94-a44275a976ee | -6.82232 | -44.47013 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d456a994-f832-3858-8485-657cdfc0dc6c | -6.81815 | -44.47093 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb980fb3-e0b8-3503-9ac4-c508b533941b | -6.81644 | -44.46895 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7b807b7-d86d-311c-9578-8cd546ed5360 | -6.81562 | -44.47339 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3073c791-32da-3ea7-8755-26c0929c2a0d | -6.81226 | -44.46972 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8713f70-059d-304f-9a33-714b2a25d31a | -6.81148 | -44.47416 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1d8de52-9077-3802-a50e-bc9fd74c8926 | -6.80973 | -44.47221 | 2024-10-27 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc1ad380-5096-3c57-8cc0-07fde823d326 | -3.60059 | -44.79008 | 2024-10-27 03:36:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08e86d78-ab0e-3e0f-a28b-e2d7da4f9a0c | -3.40115 | -44.98187 | 2024-10-27 03:36:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 46c7d2a7-b0c4-38fd-a61a-b2f26cfe9a7a | -3.40022 | -44.98721 | 2024-10-27 03:36:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4b08d737-896c-37ad-92f4-ccd3fb820dd6 | -3.39968 | -44.98533 | 2024-10-27 03:36:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| cf5f6312-4b2a-3810-a36e-357da907c300 | -2.86968 | -44.99992 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d13b557-f7dd-395e-a0a8-7d14c57fe026 | -2.86949 | -45.00127 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f07a00c0-4eff-355d-b527-0077c9f43038 | -2.86877 | -45.00542 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f933ca5a-ae36-3c25-b20b-bb15773bc1d3 | -2.86317 | -44.99891 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe30d77e-5be9-3af8-877a-84fb0d7561d5 | -2.86298 | -45.00026 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfbffda0-e066-3a63-b91c-3f59f6d7122d | -2.86227 | -45.00434 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81661be9-aecd-3003-b9ea-0954093169c4 | -2.86204 | -45.00569 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dc619ab-b9f0-362a-a626-4331c2fcef50 | -2.85668 | -44.99784 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33bd6f4a-b267-3c6b-b304-738ca5e4e41b | -2.85648 | -44.99921 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d53543f-1cb9-3bdf-a5f2-7248e8896abc | -2.85578 | -45.00326 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 153bc98c-f4e2-34fe-81c6-847b785992cd | -2.85554 | -45.00463 | 2024-10-27 03:36:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d5c0e45-aadc-39cf-98a3-530622560124 | -2.45965 | -44.93652 | 2024-10-27 03:36:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9baa0d84-ff85-3c6b-8df4-b972f60affc4 | -2.45871 | -44.94202 | 2024-10-27 03:36:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README28.md)
