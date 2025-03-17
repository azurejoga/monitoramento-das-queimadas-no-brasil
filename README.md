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
| af62e9b1-11a7-31dd-9dcf-42755f868c35 | -8.1075 | -43.1411 | 2025-03-17 00:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| f14b93e1-71ac-39b1-bbfe-b8ed2ede7ad5 | -8.1075 | -43.1411 | 2025-03-17 00:20:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| f94706b4-b53e-31a6-a656-714e5b0f884a | -10.57817 | -45.15395 | 2025-03-17 00:20:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5f8a53a6-8300-36cb-b875-7f82b2b65fc5 | -13.4488 | -41.32147 | 2025-03-17 00:20:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 3ee5c46d-a969-35e7-84ab-e4fa2b16b59f | -13.45006 | -41.33065 | 2025-03-17 00:20:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 73e7b779-22c9-3a27-84d7-f6d2d3ef1ad3 | -14.53498 | -45.51424 | 2025-03-17 00:20:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 76cc8d8b-146c-3e5a-abde-5f88a9f8b502 | -14.53482 | -45.52454 | 2025-03-17 00:20:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 0c5d2d05-83ef-3e15-95a2-d6dcf7f4bc97 | -10.57658 | -45.14131 | 2025-03-17 00:20:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 491034c3-682b-3328-9099-bd98cd00f6a9 | -11.82194 | -41.2011 | 2025-03-17 00:20:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 86a559cd-b1f1-3ae8-8f36-ffd0f71b8959 | -14.53689 | -45.52984 | 2025-03-17 00:20:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5026bf34-082a-37ad-ae10-eb2c72e8d7e8 | -12.54839 | -45.35341 | 2025-03-17 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 453cd93e-8cbf-3a2d-a50f-9e17dcfb510a | -11.79914 | -41.23196 | 2025-03-17 00:20:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 432a873e-efb2-3414-8211-b58445ec23cb | -17.66256 | -40.77722 | 2025-03-17 00:20:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e05cd1ab-309c-3186-b907-856eae150cb6 | -8.1219 | -43.137001 | 2025-03-17 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96864ab4-bae5-3767-a8b2-9e73cf535688 | -14.543 | -45.5191 | 2025-03-17 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7d65120-e173-36d8-9d6b-e94d0ac5f37b | -9.4882 | -40.337101 | 2025-03-17 00:44:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e40e9347-d13c-32a9-a656-b83d09b4d7dc | -21.974899 | -53.658401 | 2025-03-17 00:44:00 | METOP-C | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b44ec260-9c6f-3117-9e6a-bdd1fe0e946d | -14.5413 | -45.5116 | 2025-03-17 00:44:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaa11ec7-0185-38d8-ab57-9459bca9ce5b | -10.5887 | -45.141998 | 2025-03-17 00:44:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af67a3de-ab19-3aac-8a44-572264b23235 | -13.4675 | -41.3134 | 2025-03-17 00:44:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c0e9a331-6350-342a-9333-b14c5bc6ab08 | -18.676399 | -44.361401 | 2025-03-17 00:44:00 | METOP-C | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 31c0de2f-bda2-3d5d-8f07-59b7e94e131b | -10.5789 | -45.144299 | 2025-03-17 00:44:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96c1df2f-be0d-346a-9d6f-5a6721322823 | -10.5769 | -45.135899 | 2025-03-17 00:44:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9514463-252d-3441-8897-a9648f500568 | -13.4578 | -41.315899 | 2025-03-17 00:44:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f865fe8a-493c-370c-a3da-4d8b112e2328 | -9.4926 | -40.354401 | 2025-03-17 00:44:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a9167ea7-dc7f-3bdb-b159-de313828246b | -8.119 | -43.125198 | 2025-03-17 00:44:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a635046-85f0-308d-a046-8c137af6d819 | -21.986 | -53.6635 | 2025-03-17 01:10:00 | GOES-16 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 108.6 |
| eed8c26c-4c60-3645-ad02-da92756f53a5 | -21.986 | -53.6635 | 2025-03-17 01:20:00 | GOES-16 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 74aa4f24-00a5-34df-a05b-e2d2aa47d235 | -10.17916 | -37.45019 | 2025-03-17 02:51:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 28307731-b6d3-38e0-9388-c69a27207077 | -10.18012 | -37.4525 | 2025-03-17 03:17:00 | NPP-375D | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a711ee4b-239e-3c01-af15-671646412fec | -10.17527 | -37.45164 | 2025-03-17 03:17:00 | NPP-375D | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e36f65b-968d-3deb-b856-604a12970c8b | -15.79014 | -42.13308 | 2025-03-17 03:19:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce15a073-7ea8-3c2c-877c-5007f68c68f1 | -19.83332 | -40.11213 | 2025-03-17 03:19:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d030da86-0d64-36c8-b208-e3be38054e73 | -15.78427 | -42.13165 | 2025-03-17 03:19:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6bc437-6d23-32ec-9b5e-e402da541aac | -18.91722 | -41.48782 | 2025-03-17 03:19:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e32bc2f-1888-3342-9d96-8362bce77318 | -10.17839 | -37.45263 | 2025-03-17 03:40:00 | NOAA-20 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 061ba48c-b6f1-3948-9d7d-68068772f7fe | -8.10911 | -43.13763 | 2025-03-17 03:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 26aaf997-d643-31b7-a5bd-30acccd0372a | -8.11004 | -43.1324 | 2025-03-17 03:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d79ccc93-ec55-34d2-a888-0c0a0aaf67b7 | -9.76923 | -37.18545 | 2025-03-17 03:40:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56e19370-c14c-390d-9cfc-91c3b3f91912 | -8.10432 | -43.13679 | 2025-03-17 03:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6d73b0da-e7a6-33a8-9d25-f9575dcb27cd | -10.43192 | -40.50365 | 2025-03-17 03:40:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7506fcff-b651-3bf9-82c1-c5047a1b00ba | -10.92181 | -37.64933 | 2025-03-17 03:40:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 30bb1a83-bafa-313a-b63a-31e008437186 | -8.10525 | -43.13155 | 2025-03-17 03:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cb4b958b-a545-3ed7-a445-079dff960a27 | -10.17898 | -37.44899 | 2025-03-17 03:40:00 | NOAA-20 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09eb3f23-1dbe-34f8-b6a3-6906dcc37326 | -8.3898 | -35.02273 | 2025-03-17 03:40:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ced1bcbe-8189-3f63-ba95-0db8ac1c3583 | -8.38926 | -35.02622 | 2025-03-17 03:40:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1e8093c1-6e4d-3a54-88f8-f7e20fe85911 | -14.53961 | -45.51761 | 2025-03-17 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9d9de2b-5cc0-36d9-a022-0beabc970072 | -14.1197 | -41.67802 | 2025-03-17 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba9a489c-a62c-33ec-b0f8-91a3447cfdf4 | -10.57357 | -45.14597 | 2025-03-17 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95fd16ad-0479-3434-ad3d-0ec745756584 | -10.57418 | -45.14272 | 2025-03-17 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91bebca3-4d80-3297-a9ec-f677c98d3a62 | -15.98334 | -42.03925 | 2025-03-17 03:42:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 874294bc-2c88-3085-9134-45269895214e | -10.57296 | -45.14921 | 2025-03-17 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a6c10bd-2243-33c8-8ff0-4233d95ec6ee | -15.98364 | -42.03749 | 2025-03-17 03:42:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d2b88e-1c07-3082-9e74-d2c43a550a85 | -14.53348 | -45.52246 | 2025-03-17 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8153b035-abbf-3375-9eee-96fee587eca0 | -15.0023 | -39.05177 | 2025-03-17 03:42:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f7fd03c-52c5-311a-b828-dae70f60c4bd | -13.45244 | -41.32495 | 2025-03-17 03:42:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8a68474-3f4f-333b-9bdc-de7b102cde8b | -15.78511 | -42.13097 | 2025-03-17 03:42:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8577438f-a576-3689-b7d3-1b55a572207d | -14.53904 | -45.52057 | 2025-03-17 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9012735-4234-3de6-a991-570037a9b673 | -14.53847 | -45.52353 | 2025-03-17 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1769797-dcfc-32c4-96f3-a82250839998 | -12.86188 | -38.36509 | 2025-03-17 03:42:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76358e0c-7d40-35cc-a206-0f38122f3311 | -16.62861 | -46.95127 | 2025-03-17 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0572a03c-546a-3381-bf4d-67771efe378f | -17.67602 | -42.74434 | 2025-03-17 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ade2183-f479-3e38-960a-6cb0f8ca6248 | -16.68094 | -43.88527 | 2025-03-17 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1cb23f1-5563-39f6-81df-ec4940685b3c | -18.91878 | -41.48756 | 2025-03-17 03:45:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd282ab4-0c35-35e8-833d-55de6fd8eac8 | -17.74973 | -42.89314 | 2025-03-17 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e86d530-758a-3fb9-86c7-3afecc86a495 | -18.91514 | -41.48689 | 2025-03-17 03:45:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 13e36a8f-abb0-38cc-a7c9-6ea19e7d8b6d | -22.85662 | -42.98001 | 2025-03-17 03:45:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b9e1e2e-c618-3eaa-9d78-d5598f7d504b | -17.74908 | -42.8967 | 2025-03-17 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ded96901-c36a-3606-b86b-2e6f74dcab12 | -18.92995 | -41.93746 | 2025-03-17 03:45:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64925fbf-9cd5-35aa-85f9-ee60f63a56b3 | -18.93078 | -41.93279 | 2025-03-17 03:45:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 40f7a36f-a255-3dcb-b68f-1ee391391894 | -17.658 | -45.56851 | 2025-03-17 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dde905d-61a4-3c02-8546-8c9052fdaf08 | -23.98394 | -48.91737 | 2025-03-17 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5af1b4fd-ac8b-3ef3-97fc-75f0472b612c | -8.1075 | -43.1411 | 2025-03-17 04:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 92fdc2ea-a8db-3f03-9e2b-48329a3c9f5e | -8.1075 | -43.1411 | 2025-03-17 04:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 37dc7762-3584-3906-be7d-c3b7a3723d2c | -8.11117 | -43.13509 | 2025-03-17 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| a2e609ab-df07-3889-b6fc-4b77b8ca2a03 | -8.11522 | -43.1357 | 2025-03-17 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| c97a5200-988f-3a54-a791-2abf05d24323 | -8.10712 | -43.13448 | 2025-03-17 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c38b379c-6766-34c4-8063-c159eccb5986 | -8.10764 | -43.13088 | 2025-03-17 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a63c7e9e-884f-3383-8e75-05b9d72d7859 | -8.11169 | -43.13149 | 2025-03-17 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 00d7a6fb-4004-3e1f-9bc0-16d6150cb561 | -11.68469 | -44.88442 | 2025-03-17 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e77babc-e888-3ffd-8230-49f0438ea0ab | -13.27046 | -53.8924 | 2025-03-17 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7684271-cb7f-3d62-8981-774ba3bdf38d | -12.54592 | -45.3554 | 2025-03-17 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9accdcc1-ba9e-3200-8344-0f7559274bd0 | -15.78707 | -42.13172 | 2025-03-17 04:34:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1219fe6-bf79-3870-aee4-0d5eb68b8ba7 | -15.78814 | -42.13152 | 2025-03-17 04:34:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9403fe0e-8f71-3095-abd7-d88f3596a1de | -15.98398 | -42.03743 | 2025-03-17 04:34:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 672821ee-24b3-3a29-81d7-9b0de439027a | -14.53284 | -45.51337 | 2025-03-17 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b9a8454-8b3d-33cd-b58c-91ee42d41874 | -14.53153 | -45.52303 | 2025-03-17 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b952a574-e8e7-336d-a9ed-c7c20347882c | -14.53981 | -45.51932 | 2025-03-17 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38e4f69f-fc7c-3257-992c-4daa7716b372 | -14.53219 | -45.5182 | 2025-03-17 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fff6e92-9223-3350-8bd3-3743a671a95f | -14.53915 | -45.52414 | 2025-03-17 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3e26148-a4ef-3c64-82bc-8bee8a29914c | -16.34903 | -43.69444 | 2025-03-17 04:36:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1fd5f0c-abdb-339b-b1e2-df91b7508b8c | -17.65531 | -45.57201 | 2025-03-17 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa4919b5-38d3-3842-9f24-45ab5b335c87 | -17.66321 | -45.5733 | 2025-03-17 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02f507d2-74c5-34ad-9bee-bc8d0ad68e0e | -16.34869 | -43.69588 | 2025-03-17 04:36:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b99ab62-1a96-3cc8-b184-357f5532e351 | -15.56923 | -47.85704 | 2025-03-17 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00497bb5-6c07-3aff-86aa-935fcdb7c97c | -17.65995 | -45.5673 | 2025-03-17 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4cdd79d-d3d7-3bae-953a-2a07a2737c34 | -19.72109 | -40.35394 | 2025-03-17 04:36:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05249fb6-d7e6-3859-a5bc-f117a32d1bae | -20.47834 | -53.67707 | 2025-03-17 04:36:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14a7ce8d-66c1-3150-84de-aa61202b736a | -19.71538 | -40.35327 | 2025-03-17 04:36:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41f762b3-3b3e-30c9-a358-f38782e83420 | -23.98487 | -48.91966 | 2025-03-17 04:38:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
