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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49412081-11b0-3b02-a18d-a1e825e6fd50 | -3.62172 | -41.15232 | 2025-10-04 04:12:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0240811-e857-325f-bffb-17f86a4375ab | -6.4575 | -44.56969 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bfb27d6-2e9f-32c9-b486-f814b8490d22 | -7.26794 | -45.48245 | 2025-10-04 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9697455-f784-3d35-92fa-b8461be076ac | -7.06514 | -43.23376 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fa6ba5a-229c-3190-be02-5aaba67bd8f4 | -3.09001 | -48.49305 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509277d7-af37-32e0-801c-fc00b26bfe6a | -4.9547 | -45.07374 | 2025-10-04 04:12:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1dce075c-9553-3df4-a415-50ee6c76bcc9 | -5.35828 | -45.2879 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69882b64-8652-36a1-a737-06a87691b77b | -3.96762 | -41.59323 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d58d908-cd29-393d-abde-71af6f578933 | -6.99427 | -42.80047 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6238adc-615b-3ede-8587-e049e63459c6 | -6.37109 | -45.14507 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a007327-b907-3c12-bd76-6608411608e1 | -4.43319 | -43.2494 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 487ee2e6-6396-3c06-aa16-cbb5bcb3a294 | -3.86053 | -51.81646 | 2025-10-04 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ab6207e-1932-33f8-a271-a6a1610770ae | -7.24776 | -48.48124 | 2025-10-04 04:12:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 510918ef-fcdf-3b8f-b12f-9a47fac6cd81 | -4.43826 | -43.38966 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef337ccf-584c-3d91-a0bd-e54ede0d274f | -5.82973 | -42.88225 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d5b6c013-f5ba-34a3-916c-8186e3dabf2d | -5.66837 | -42.72245 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 294229c3-2d56-39a6-b271-ae936b60996a | -6.37267 | -43.89388 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19020da-3b46-3997-9e6a-9459601c318b | -7.72553 | -42.57692 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9ae126e-47e2-3b8d-b2b9-d2b949fd3fec | -5.48358 | -45.54245 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce2eada5-a03f-374a-806d-2e3393ca6c88 | -5.9059 | -42.52957 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1004d84e-01a5-3f84-987c-0606553a5b7d | -6.38373 | -46.50525 | 2025-10-04 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dd6f3f6-9b50-3590-b873-8d21effb799f | -4.75304 | -46.60556 | 2025-10-04 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d518179-feb5-363d-b0e7-8fa6d98eca11 | -6.70365 | -42.79012 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3bbd7eb0-bef0-3660-b9fd-ca68498685f3 | -5.83412 | -42.87587 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cb64043c-7529-36c3-9bbe-88d9d5e9c4de | -5.76701 | -42.93604 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b31ce4bc-dd77-34e9-89f8-59311056e43b | -5.77927 | -44.90203 | 2025-10-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad44438f-055f-3982-bd3a-4c8990166068 | -5.8707 | -44.11931 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 356498d0-5da5-312e-a9f8-37b96102b4b8 | -5.47372 | -43.15831 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c73b4876-049c-3a91-84d8-c46fd89f3883 | -7.7668 | -42.61558 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7693e823-1a08-3d6a-97c8-35e11eb91bbf | -5.64762 | -43.62447 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6492c1df-4243-3f31-82e2-99759863dbba | -6.70867 | -42.82282 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b5a8a94-00fc-3ff0-b0d0-074df663822a | -5.46655 | -43.16072 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59b139b2-8507-3cc6-acc6-2127fbf7300c | -7.25184 | -48.48203 | 2025-10-04 04:12:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2858d621-e6d4-3c4e-a699-dc39c598e930 | -5.39112 | -43.46543 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29be8206-b3ee-3fe5-93b6-600938956582 | -7.72721 | -42.58794 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbfbcc04-9108-38c8-b8ad-2c0fc161262a | -5.01955 | -43.665 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a768faf-e1da-3da5-beb1-8d09d8bcdbb2 | -3.22068 | -47.12872 | 2025-10-04 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ba665b1-fb6f-3aea-ab57-1b44420ac51a | -7.47843 | -43.04742 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d98f27cb-e79b-3a00-a0a7-857944b516b7 | -5.77981 | -45.74874 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 058555a8-5e3c-3c98-847f-d8da3a37b656 | -5.62675 | -43.22187 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9636d80a-a677-3de2-b4c7-6ab3060b60cf | -5.88473 | -44.26814 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8864fcdf-80dc-3f0f-b791-00c31a336866 | -5.70787 | -42.64377 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cd0bf93f-0784-3536-8cda-a03442dd52a3 | -5.40986 | -41.33886 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56c7bd99-116f-334e-a367-22b37c933c0f | -7.65125 | -45.47157 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fb233cc-1850-36a8-a43d-9b5e93df56c6 | -5.83943 | -42.86589 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d828d575-0334-32db-bd45-7f79a06c2e98 | -6.84391 | -40.71507 | 2025-10-04 04:12:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e1ffdbb-3ff7-31a4-9fd9-1edf2a181804 | -6.66127 | -42.82244 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a66dbd24-f95c-3a15-8981-65bd34b96c79 | -7.70282 | -42.56977 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8785b31d-a4ee-3244-adb6-4fa7c5e8c14a | -6.09956 | -43.43184 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 400df992-6bb9-3605-874b-1f7210d07645 | -6.87465 | -44.49865 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ac692796-1509-34ab-bb60-efc8a7db1d93 | -5.22725 | -43.70474 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f20b2aa4-f038-3fd6-937d-18764fe3bb9f | -6.70151 | -42.82524 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f8669340-2a76-3856-9fd3-0c93536a677a | -7.73691 | -42.6109 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8a3c12ec-34a7-3bce-ab61-0a3823af0c29 | -6.2741 | -44.04426 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59e9cabd-2e7b-3b06-bc76-5246524e52bb | -4.31449 | -48.09053 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7188c03-26a3-31a6-94df-6abfdbae10ea | -5.49171 | -44.11431 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3115b0ad-1435-33b2-9a4a-7a042b88d061 | -5.45494 | -43.1695 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09c8bbd5-1e6a-3b34-a640-4cfce4245be9 | -6.66843 | -42.82004 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a92f908f-7bab-3120-a6ea-fa9d14f961e6 | -6.34704 | -43.43531 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 005ce131-1c51-3694-a0bf-0e5702a3221e | -6.59144 | -44.62826 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a88ce23-1eb9-38d0-9a02-b902a060c46a | -7.57367 | -42.39478 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f624f164-68b9-3a82-b8ca-f759b543300d | -4.71798 | -46.13054 | 2025-10-04 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1859d452-e2c5-3641-bdec-90aa6bff9536 | -4.44039 | -43.24697 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b6ebed75-c19c-3f1d-b2ce-ebbd9d9b40fa | -6.34429 | -43.45263 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e24dfe27-d617-3f9d-8165-b09cde83fbdf | -3.84695 | -41.56056 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c42eb065-09df-3155-8efc-af05d4bf53b9 | -5.7756 | -45.75212 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0360bf8-9f4d-3659-8ae9-12f834788b7b | -4.60925 | -43.14582 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a313201c-17c2-30ae-8ade-472fd618972a | -7.76272 | -42.53251 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e69d1290-1e7d-30f9-bc06-50db87128dd0 | -5.48293 | -45.54646 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cc109e4-68a4-3a85-8712-93e39d1d6171 | -6.71416 | -42.80949 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 908f8ce0-05b5-3c28-9054-fdd4141b4d38 | -5.69119 | -42.83564 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 317f13e4-4e4d-3016-aab5-747be7bc2909 | -7.0494 | -42.77364 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d23f1998-daa5-336a-8eea-e1a57b6a55f1 | -7.76877 | -42.51548 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 577ccd82-885a-3d42-9c65-2ca3a4b63ceb | -5.4093 | -41.34246 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 853d4f0f-c364-3682-be8f-34ba3e71cbb0 | -4.43706 | -43.24645 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90efc232-9c1e-3bea-9cab-6f25444bfd11 | -4.25507 | -42.27016 | 2025-10-04 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e53edc88-215f-3908-aa23-bf84ce838db1 | -5.87913 | -42.52561 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0172870c-344c-3eb2-abc8-edc2a9f4a4d8 | -6.94251 | -43.12923 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e07cf4db-f823-3e26-b900-f119cb0bd18f | -4.31386 | -48.09435 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b2fc4a9-feed-3bbf-bb78-4b046375abe7 | -6.76889 | -42.24438 | 2025-10-04 04:12:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dfe2599b-b98c-398c-9254-94d591dd26b5 | -4.31866 | -48.09125 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9da13a41-0ccd-3896-a6db-7d942bc3d433 | -5.95765 | -43.49133 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5c104f5-38ce-3532-b167-eaaa01452031 | -7.04221 | -42.77604 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 17245dd3-47ee-3145-ab5b-9451311c5a3f | -5.69832 | -49.30292 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a98c92f-03a7-3716-801b-8c4baaaccf50 | -5.95986 | -43.49882 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee24d3b6-6612-3394-9621-563393910492 | -5.19681 | -45.07605 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 80c15d0c-964c-3326-b749-dd6e5a72d06a | -6.72092 | -47.43491 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e2296f-a145-32d1-aee9-8407af4ad2da | -4.26296 | -48.55465 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3370341-ef62-31a8-95cc-5c870962a8c2 | -7.71779 | -42.58287 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f9b00114-6aec-3cc2-b8a9-b6f110203389 | -5.90145 | -42.51469 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c1cba1f-76a8-3f2c-8e78-44a16d23de8a | -4.43762 | -43.24297 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfd3d343-612a-3f1c-af8a-42a8b9567e37 | -6.17587 | -46.311 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9ccf0bf-9584-35b0-8a0b-8d9b14b1998c | -2.24736 | -47.88147 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5ac8105-e2f7-396c-a72c-bd326e0f18ec | -5.93274 | -43.30556 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e89971fa-233a-367e-82ab-589bf30d4d0c | -6.99221 | -44.20661 | 2025-10-04 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac93ed4c-b8a3-3bc6-bb04-c0ec9bc2934d | -7.5526 | -42.39872 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1205ff4e-5056-3be7-9ba0-bb85abb3e4b4 | -3.84308 | -41.56353 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 721e729d-0c8f-3e53-8550-df8b742c614b | -7.78445 | -42.58973 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 378a9302-c79c-3cfc-a3ba-e0f3bb197d6b | -6.06905 | -43.21754 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0b32f12-7447-3e6c-84e1-a176afaf292d | -6.87252 | -47.23475 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |


[Clique aqui para ver as próximas entradas](README63.md)
