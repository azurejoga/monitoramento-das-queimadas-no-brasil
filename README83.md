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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a622b2b9-7aa5-33b5-887f-a0f387921241 | -22.02849 | -42.89643 | 2025-09-10 04:46:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c03cf8ee-dab6-3af4-a101-6762a1ba458b | -20.98358 | -48.00453 | 2025-09-10 04:46:00 | NPP-375D | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e5521c1c-dea1-39e2-9815-6acd119ebea3 | -22.76351 | -50.35886 | 2025-09-10 04:46:00 | NPP-375D | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aeccabb6-d07d-3af5-8062-15ab18e9ffad | -20.06635 | -47.54089 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23389980-8760-3c4f-a409-2fd58c1a1dee | -20.0599 | -47.51675 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f95860c3-5d21-320a-85ce-a10b42870641 | -20.81117 | -55.34516 | 2025-09-10 04:46:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5d9650e-1682-39c5-ae29-443d24835fb1 | -23.40478 | -47.26656 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ac40f193-49a8-3251-9203-d2829cd78545 | -23.36018 | -47.20419 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1b2ee51-de04-37f8-b099-bffd08c82838 | -22.1029 | -56.56338 | 2025-09-10 04:46:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e9035e5-1880-3f40-8c33-08236f32e4ca | -20.10664 | -47.82505 | 2025-09-10 04:46:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d84d66f8-8460-3535-a9e5-6bc36872c4c6 | -22.87791 | -48.13481 | 2025-09-10 04:46:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0768847b-bf5b-3a1b-9a92-7d5fea651961 | -20.10733 | -47.81977 | 2025-09-10 04:46:00 | NPP-375D | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3620f094-112f-30bb-aa77-a070035d6c34 | -20.00326 | -47.6076 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cead77e-1669-3d45-b46e-f0b070be015b | -20.99744 | -47.99032 | 2025-09-10 04:46:00 | NPP-375D | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c979b6c6-e6c9-3a14-991a-e6f1ee3c93bb | -20.37858 | -46.63847 | 2025-09-10 04:46:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b61bd2c-49b1-3427-a66a-01a07c9bb13b | -20.00976 | -47.62004 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dd661d2-c5d0-313c-9d21-52b482436242 | -20.46131 | -43.95539 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| d2736c43-2379-33a6-9222-885aee4ad982 | -21.02428 | -48.42192 | 2025-09-10 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e816dc96-3ec3-322b-b364-68f30c682d64 | -20.00175 | -47.61927 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38bff19b-a95a-3e94-802d-407c4d895fb6 | -22.87742 | -48.13384 | 2025-09-10 04:46:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16f87ef0-3fed-3316-9395-1e59d77f37d4 | -21.40259 | -43.87886 | 2025-09-10 04:46:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 646409f9-b852-3774-9176-09a392083f06 | -22.58099 | -46.71984 | 2025-09-10 04:46:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34b9ab79-5871-3c08-aa23-28a8189ae6b6 | -20.45671 | -43.95037 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| df0d0907-a589-349e-b555-04118535da08 | -20.46579 | -43.96151 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| f9d4bb74-c01d-3404-baca-c4f152530de3 | -20.89732 | -55.18266 | 2025-09-10 04:46:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1561d32b-c8f8-3b23-ad2d-ff9168c3896e | -21.20077 | -44.03054 | 2025-09-10 04:46:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3ced7e99-c06a-3a57-9c5e-f08affc8c0b5 | -21.92616 | -45.64162 | 2025-09-10 04:46:00 | NPP-375D | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 535107e5-5ee0-376d-a2ea-1ba848206ee8 | -20.0892 | -47.35629 | 2025-09-10 04:46:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f8393d-4b95-3b60-9a2c-b0d391fadf3a | -20.20004 | -41.54749 | 2025-09-10 04:53:00 | AQUA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| 06d20b73-5f41-3ba2-bbac-18ec59a62964 | -20.45947 | -43.92587 | 2025-09-10 04:53:00 | AQUA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| d3a78d90-c17d-37c4-99c3-2e82646b5a9c | -20.46158 | -43.93555 | 2025-09-10 04:53:00 | AQUA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 9484a7de-a7d4-3c00-8004-fd3527b5cecb | -20.19837 | -41.54001 | 2025-09-10 04:53:00 | AQUA_M-M | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.1 |
| 18502bf8-2c78-3b51-a121-316140d915a9 | -20.44997 | -43.97162 | 2025-09-10 04:53:00 | AQUA_M-M | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| 1b2afa23-4ae8-3865-9951-0a2acd101041 | 4.19105 | -59.77 | 2025-09-10 04:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2437921f-941f-30cd-aa4a-cb8b04a10919 | 4.19122 | -59.76797 | 2025-09-10 04:59:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a6281fd-12f3-39a3-ba76-c5edc8dda96e | -6.5587 | -43.1493 | 2025-09-10 05:01:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5582e4d-ff24-3ffa-b92f-71ff156d2bc1 | -5.5339 | -42.65729 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6f16f08c-080e-374c-a680-24c9bddc7cfa | -4.09315 | -41.57179 | 2025-09-10 05:01:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f52d3e2b-819f-355d-a0ac-16c552d6b007 | -3.24634 | -52.8533 | 2025-09-10 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5ebd88d-a695-3340-8d14-e70be39ee12f | -5.42429 | -43.98887 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa486c50-6e72-314c-b0e7-244393e624b0 | -3.63791 | -49.20709 | 2025-09-10 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7beb3d6a-f56b-321b-a9bb-b1201b905226 | -6.1875 | -43.50692 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7dc61f-a36f-3d26-8ab7-374a4eab4b72 | -4.83982 | -45.35913 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b73bfb4-94b8-3fcf-b79b-c63b1b69ef0d | -4.19965 | -55.1342 | 2025-09-10 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0061beff-b3a0-345c-a169-d34eb285c4ca | -5.22717 | -43.69652 | 2025-09-10 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6333992-7eb1-3013-9326-615c9b5c4dcc | -5.96494 | -45.80856 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c526737-896b-39da-9fdb-0d9f05e1b732 | -4.86487 | -42.76614 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f8f98b5-ae74-33ed-a69d-a1bdfabb874c | -5.748 | -47.46414 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d00303a7-952e-35e2-9dcb-683a652d029d | -4.84033 | -45.35546 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c5bc79f-33fb-3a45-9706-0098bb4637d4 | -5.53936 | -42.65764 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6e6d0967-ea62-3a83-8f11-24c3b6e6dd4d | -6.19422 | -43.50486 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f63d335-9c48-376a-bcf4-4385baae6849 | -5.66143 | -43.90412 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 275fc117-90ce-3dbd-9b47-99c1db55bf4e | -4.56217 | -56.23721 | 2025-09-10 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f065e2c2-13ba-3166-9d64-9127f5d1fbfe | -2.91659 | -48.67563 | 2025-09-10 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f99a63-3072-3344-b70e-3b7919c8c70e | -5.57209 | -42.93211 | 2025-09-10 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 078292f9-01e1-3f98-ab96-809f37682bba | -4.83752 | -45.35884 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e24b671f-23db-34b9-8913-b2f7891ef049 | -6.19352 | -43.51008 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a6f0857-a2e5-3e04-b937-a66a47240ed2 | -3.88731 | -54.24691 | 2025-09-10 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cdf6ea8-f617-3dba-b770-f4f5788f7169 | -3.86153 | -52.00383 | 2025-09-10 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad9d22f-e1e7-3c50-afd9-795a78ff0da6 | -5.64317 | -42.63075 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 32699830-52de-3202-9d9f-d59ca18a6217 | -3.96521 | -43.2449 | 2025-09-10 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eefae4e9-595d-3dae-a542-6950182eaa21 | -5.74257 | -47.46646 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 962017c1-a5fd-3476-819c-0c0b5577c4b0 | -5.88516 | -46.08704 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 416d4e73-b7ec-334e-8298-ffba3d2552cb | -5.79816 | -43.88979 | 2025-09-10 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a6f486-f460-36a3-b992-9b8d923fdbd3 | -5.68086 | -43.33677 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6cbfe43-bdeb-364c-b80f-5ff04eb4db8d | -5.74096 | -47.4778 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6233a206-846e-3585-9253-3b6389dedb04 | -6.05948 | -43.13535 | 2025-09-10 05:01:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c4d60ba2-fee7-348e-ae7a-bda51da4b216 | -3.96597 | -43.23949 | 2025-09-10 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b01872f1-d15e-303a-9900-f663e160dbc6 | -5.58401 | -45.03504 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8ed8ed79-6493-3d38-b257-eb53d2f3beac | -3.51543 | -52.74879 | 2025-09-10 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6719df5-e4a2-3d21-bbb7-076614e7bc06 | -5.42449 | -45.88257 | 2025-09-10 05:01:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73bfeb32-c60f-3e90-b154-349b9a1c25c4 | -6.20135 | -43.50127 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fef870be-c1f3-3c0a-81e4-660b7fc9db31 | -5.67662 | -45.46479 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44ecf293-74aa-3717-835e-4eec0b473292 | -6.20717 | -43.50738 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f8cd0d3-d2b2-327b-a175-e78812189d53 | -6.25733 | -43.42324 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7462afdf-6e02-397b-ae6b-6cb5fea60a39 | -5.72042 | -45.41462 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c19988a-479e-3386-9567-3e9c50e6f7ca | -6.1877 | -43.50393 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 325b6128-dd01-3361-ac5a-44b773d29171 | -5.67157 | -43.36227 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7283780-8ce9-363b-9b55-1ebb4e17adb5 | -5.66667 | -43.34988 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 896749cd-88b2-32cf-a7dd-45da8a33acae | -5.85909 | -48.15905 | 2025-09-10 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b4aaf43-1282-3100-8f9e-892454650c81 | -5.12111 | -44.6697 | 2025-09-10 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce02d547-d15c-37a6-9862-ce22188bb9df | -6.20816 | -45.61603 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75466c9e-c7de-3aa7-9e70-be9b764ed312 | -5.4197 | -43.45566 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2dcf4e8d-db09-3b64-bc80-9bcba378d53e | -3.3211 | -54.91177 | 2025-09-10 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f18b27d3-dc13-386a-991b-ffdf5a0e45f6 | -4.09024 | -50.69132 | 2025-09-10 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b59917a5-106a-37fd-9396-a46aca7a24d2 | -5.74638 | -47.47561 | 2025-09-10 05:01:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63715a33-0a7d-39f9-a004-c4d617d58cfc | -4.49535 | -47.82396 | 2025-09-10 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713355b4-d400-3bb6-9717-38285045d013 | -5.58284 | -45.04341 | 2025-09-10 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cb088794-ddb0-3b61-a8c9-333c2530df76 | -5.45137 | -43.46652 | 2025-09-10 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| afa652f8-faab-3055-b795-e5c9e1f77650 | -2.91218 | -48.67497 | 2025-09-10 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 966a5c99-8a00-3df0-a89e-387a8f1158a9 | -6.20631 | -45.61674 | 2025-09-10 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f9609b-1acf-3119-bead-d14f4a74ff95 | -6.26107 | -43.40556 | 2025-09-10 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dcc0866d-fb25-3e7e-94f9-a986bc7573b4 | -5.53219 | -46.49741 | 2025-09-10 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ceefbe6-2a43-3f68-8846-7fb10912f0cd | -3.68747 | -49.57244 | 2025-09-10 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08dc0df6-e18d-37eb-a8a9-3f84d5d1d011 | -5.4083 | -42.85857 | 2025-09-10 05:01:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0cedc03e-491d-3487-b378-ad6feedb48d2 | -5.64966 | -42.62354 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 65ac9b02-7e21-34c5-b236-e4fc119d2bfd | -5.96439 | -45.81235 | 2025-09-10 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19b0de8e-c59c-35f0-b21a-972a8e1dc5c5 | -5.5317 | -42.6628 | 2025-09-10 05:01:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 66cecc52-bb9b-3064-8e2c-e8e18c7d231d | -5.41174 | -43.46526 | 2025-09-10 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed27920e-af61-34e1-a632-883c22826177 | -4.32829 | -48.39523 | 2025-09-10 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README84.md)
