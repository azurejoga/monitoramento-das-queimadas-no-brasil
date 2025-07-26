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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 502b6f83-3a23-341f-8fb7-5eaab2743490 | -4.75779 | -38.4832 | 2025-07-26 04:02:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0addbd28-b5b2-3a16-8953-d2ac640696c9 | -3.62992 | -43.0695 | 2025-07-26 04:02:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d273290f-797c-3327-8b77-de2e5ca3cf8b | -6.70319 | -43.05645 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 860baa51-109c-352f-b792-3d1cdbeddb33 | -6.15931 | -42.59282 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b5fcc4e0-c987-3fe0-ae84-3de8209c14c3 | -3.12973 | -47.01326 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 147fea5c-8e4b-3cae-8d0a-3702a923fa05 | -3.38571 | -47.49573 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d93d9b3b-d0f2-308e-8c82-5bbe7be4c8c7 | -7.25018 | -43.07206 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7300eab3-e490-3c8e-855f-604935f025d5 | -4.0597 | -42.52848 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| caf09405-c2cc-3dcd-86b8-931ee369ea62 | -4.06563 | -42.53799 | 2025-07-26 04:02:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43f6a405-9421-33d4-a1da-ab59bf35728f | -5.73906 | -43.96898 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75359d50-bc06-39b7-adbf-f86c366af93a | -6.64892 | -43.04475 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61f2dc95-af1a-3264-b910-153d9565dbe3 | -6.4146 | -41.16938 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2363145f-d0be-34b8-865d-e573f265abb8 | -3.12837 | -47.0113 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a754192-5acf-3b50-934c-cc59fd148caa | -6.1622 | -42.59742 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7ca8e686-119d-3284-b8e7-fe55ff3a2bcd | -3.59031 | -41.65179 | 2025-07-26 04:02:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91ba062f-f562-38f6-ae8b-67c5265e70a3 | -5.48745 | -42.15342 | 2025-07-26 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cb0af207-1749-305c-966d-df10f9c8e26f | -7.07849 | -44.04871 | 2025-07-26 04:02:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fc4d83f-bcf4-3cdd-bfbb-d04c983e9392 | -3.11768 | -46.80043 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29ae8af0-35ce-3e99-9879-3537e9968cf7 | -3.05254 | -47.38429 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 966b3825-9f13-3f4f-a247-dc3770e139f4 | -2.90664 | -48.24479 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8447476e-44e9-3c2b-ba2b-0e9fcacfbfa3 | -3.58444 | -47.53056 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5c9f4d9-52e3-32b9-9899-3a0e3a026a68 | -6.56487 | -41.49631 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43b31833-24fe-3c2c-8134-cb76d61daf25 | -3.12482 | -47.01244 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7b439f2-e747-3253-bb8a-db3be7580245 | -6.87184 | -43.68621 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a8a6088-6497-35c6-9776-b65382f145c0 | -3.82512 | -41.5621 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06934d06-ea88-351b-9ff7-a2e65ff7c942 | -3.82388 | -41.56974 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3434cf9b-7822-377a-908a-cc6890ba5b08 | -6.42084 | -41.15192 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a48c6f9-71e3-354b-9749-915c587ea33a | -3.99384 | -43.23111 | 2025-07-26 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f244254-4987-3a5e-9910-fcea4195aaf3 | -2.57463 | -49.10844 | 2025-07-26 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05ce4a18-36d2-34fa-942e-77508100f642 | -7.28832 | -43.08673 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a80597a-0b42-380a-b456-e1b2aff7674e | -3.75777 | -49.0524 | 2025-07-26 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45d1e81c-61b6-3b32-b1cd-d9d7593f4b29 | -3.3973 | -47.48864 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b34a47-224f-3a08-a5b5-159a1b5d7847 | -6.8711 | -43.6907 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 285326a6-fa75-375c-b788-871cd58e7349 | -3.98501 | -47.88885 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d6dc86e-4129-3a35-a8bb-6b81c153f064 | -6.42363 | -41.15606 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8efb377a-d976-389f-8eac-a4998d80709f | -7.23471 | -43.06676 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60d965a1-6e5e-3b79-ad13-e79722752299 | -5.73986 | -43.96412 | 2025-07-26 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 236e92f6-bd33-3be3-8d28-7105e3bba639 | -6.14865 | -42.59114 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b1351b63-7075-320b-8fb2-752afff57809 | -3.43245 | -43.14141 | 2025-07-26 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3fc5a37-d9df-3216-b2a6-f1d40d4b0518 | -5.91399 | -44.97325 | 2025-07-26 04:02:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed68b414-f331-375a-b914-f44979fb1c20 | -6.86958 | -43.67672 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81495ca3-35bc-342f-9093-5f8f790bcc5b | -6.87257 | -43.68176 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0eaa4c0-70d7-3da2-ba23-a1016d0849b8 | -3.43321 | -43.13683 | 2025-07-26 04:02:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 807bc89f-da6a-3f55-a500-d4696cc1516d | -6.87631 | -43.68233 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8188e256-e4e2-3532-ab37-d6a92cd66276 | -7.23513 | -43.07382 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| fc6a0888-0f54-3189-9766-000d3ce0913f | -5.14134 | -45.17565 | 2025-07-26 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e95e2a4-f2db-316e-94e5-a10fd78be91c | -3.81418 | -42.54801 | 2025-07-26 04:02:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e223b061-c9b7-3379-aea8-88bc993aecc5 | -4.07383 | -46.90487 | 2025-07-26 04:02:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c4c2d5f-0e2c-35d9-b767-6b75f387a3c4 | -3.65881 | -48.44668 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fccc8289-6334-358f-957b-6b3bcb4073c7 | -6.20521 | -43.74389 | 2025-07-26 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1a29ec2-6f4a-3095-a5ed-30a550e5b0c0 | -3.05713 | -40.02321 | 2025-07-26 04:02:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dc4234c4-7084-3cb7-8909-7c806823d48d | -3.0475 | -47.38336 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abb033a0-0694-3534-8c08-bc1963413d78 | -6.41411 | -41.15083 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 421b2f02-78ac-3068-bd64-e21895fdc04d | -6.20901 | -43.74433 | 2025-07-26 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 40705942-6d26-3d40-ae35-13a43a32ce42 | -6.7018 | -43.06477 | 2025-07-26 04:02:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d1914e94-ffae-3ef3-9597-b8187dbee3d6 | -7.2495 | -43.07616 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| cf68386e-a6ad-39ba-afe7-03f4a58edcd4 | -3.39681 | -47.49155 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0f9ab21d-fb9a-31a8-b83d-b666409885ea | -5.48395 | -42.15284 | 2025-07-26 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9530a2b8-9e99-3e8a-b7ec-9003573a32e7 | -6.22184 | -43.73693 | 2025-07-26 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1157f588-09a9-35d2-85df-3fd91181d7b5 | -3.8245 | -41.56591 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 26e944f8-4cbc-33ec-92ee-7075e4a2c076 | -3.39582 | -47.49738 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8b383f01-ecb8-3a13-a5ce-5c5626355c40 | -6.88598 | -43.12369 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53075275-223f-3727-94ff-56bd0b7025eb | -3.58681 | -41.65123 | 2025-07-26 04:02:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 709ece74-ec55-3ad8-998a-16fdaa044d8d | -6.77856 | -44.10759 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5bf93b5-b15c-3b6d-9a67-3293d7090192 | -5.45431 | -42.65215 | 2025-07-26 04:02:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bba45e85-c678-3db3-b657-72e423629bd2 | -6.40738 | -41.14977 | 2025-07-26 04:02:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23ba6df7-ccbc-3240-ac27-b93691016143 | -6.1522 | -42.59172 | 2025-07-26 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 90e066ef-1ea6-3a8d-bd59-06a810094ac0 | -6.88733 | -43.11538 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bef40a4-3d3c-3c69-bd88-ca87704af0bb | -6.32714 | -44.09954 | 2025-07-26 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58e4d4e6-bd43-3ec1-82f8-13ab3ebf92b4 | -7.25309 | -43.07674 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 17215e7a-7353-3344-ab6f-c246f0c4b8ea | -7.23872 | -43.07441 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 21930cc6-7301-3491-b75b-e068c11a8e54 | -3.74859 | -49.05211 | 2025-07-26 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12d2de84-b5ba-3bb9-93e7-090833c6d702 | -3.99007 | -43.23052 | 2025-07-26 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9704cce4-5adb-3beb-acf3-6bd18d3b2202 | -3.58125 | -47.52986 | 2025-07-26 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4344d748-eb78-3a8d-b9ea-9ed61dd66380 | -7.74179 | -40.25463 | 2025-07-26 04:02:00 | NPP-375D | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9b1fde3c-3e37-3543-8299-b74fa0b90f42 | -3.65603 | -43.05061 | 2025-07-26 04:02:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b700718-d3ed-37e9-a243-1e565726326e | -6.86511 | -43.6806 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 054506f4-0664-301c-b4bf-bfff83e625a1 | -5.48809 | -42.14952 | 2025-07-26 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56161183-bfd0-3b92-9280-f00fc6f9f0ba | -6.22885 | -44.52381 | 2025-07-26 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6f436c32-8a2c-3435-8cd7-50ee3c240ca1 | -4.30358 | -48.10059 | 2025-07-26 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71b4c739-1ffa-3325-99b4-5cb6b60251db | -7.10107 | -44.38377 | 2025-07-26 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ec80e70-b629-3074-afff-56066f59fade | -6.87777 | -43.67344 | 2025-07-26 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7055464-eac0-3f3b-87a4-f6253b86dd60 | -3.12346 | -47.01049 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70b1d533-58a7-31f9-a505-b172a5114d0d | -3.05658 | -40.02671 | 2025-07-26 04:02:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f1c00952-2aa1-3d10-820b-ef7bcd7e57a3 | -3.82635 | -41.55448 | 2025-07-26 04:02:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32db2084-9858-3be5-bf14-ef999a18b38c | -6.56885 | -41.49321 | 2025-07-26 04:02:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9e1cea7-193e-3700-a1a7-0fbee5bacd24 | -7.19591 | -44.02094 | 2025-07-26 04:02:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5b0b511-b8aa-3c6f-82c6-2c32f701c82a | -7.23697 | -43.07558 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a24399ca-1d5c-32e9-8205-b00675b36a14 | -7.24368 | -43.0668 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f9199316-9776-3e67-8959-46801a7b24a3 | -3.38672 | -47.48977 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 630351f3-34b1-34df-89c2-f754f5d527fe | -3.048 | -47.38032 | 2025-07-26 04:02:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7598d06-c630-3d0d-a4b2-e6b5d9eccf38 | -6.90862 | -44.23846 | 2025-07-26 04:02:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7857093b-f966-3552-9100-e520ab3ab51f | -7.23941 | -43.07029 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3ac8901d-2a41-3b51-9e4d-badc732e9bfd | -6.91322 | -38.5625 | 2025-07-26 04:02:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9096fbe5-9b99-3abf-bf08-7badf0ccbdfd | -5.77318 | -43.64423 | 2025-07-26 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6e40255-6eeb-3e5b-9655-d97583cb67c8 | -3.42805 | -39.04582 | 2025-07-26 04:02:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14b78f97-c289-3c3f-8045-4ed54dcbec75 | -7.2383 | -43.06736 | 2025-07-26 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5e6ea433-e79c-3810-978a-fa9b80e44a87 | -2.91145 | -48.24905 | 2025-07-26 04:02:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bed9bb10-4116-31f0-9bd0-4b7fff280278 | -7.78786 | -37.59954 | 2025-07-26 04:02:00 | NPP-375D | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 127df34d-3ad0-3d35-b775-56926b8757af | -3.74921 | -49.04839 | 2025-07-26 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README9.md)
