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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0ecd3b-dd92-324e-ac6d-67df6f1ca5d1 | -5.18382 | -44.95584 | 2025-07-19 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b860baff-0dde-3710-8b5f-5c81be5ede56 | -2.91738 | -48.25952 | 2025-07-19 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 362b5673-4d47-32a1-b447-fcb24ce39114 | -6.16518 | -48.04616 | 2025-07-19 00:07:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 396.7 |
| 3b1b0211-2d3a-3451-a3ee-11ad92130ac5 | -5.65113 | -43.72058 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 630.9 |
| 744c526b-e8c3-3403-abf3-ef794796e882 | -3.04411 | -49.42167 | 2025-07-19 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4261e7ee-1e0a-3cd4-8964-a882763f8227 | -9.81334 | -47.72485 | 2025-07-19 00:07:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| a8a7b9a9-1985-3a4c-b9fe-7457245666d5 | -3.61041 | -43.53677 | 2025-07-19 00:07:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 58e1c4b7-5039-3551-a0b4-645ca7f1c8cf | -2.90438 | -48.26143 | 2025-07-19 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| a46e8ec0-852b-3ee9-88d8-e5405d885cb2 | -3.50968 | -47.21656 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e2fc84a6-cae2-39f6-bb1e-f0539a152358 | -2.91464 | -48.23919 | 2025-07-19 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 24d8097b-8d2b-362d-8ba3-b7935a566101 | -8.52477 | -47.84726 | 2025-07-19 00:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 207e9eb5-0fa7-3a13-9b5e-e4dd933cb2e8 | -4.6725 | -41.96291 | 2025-07-19 00:07:00 | TERRA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 431e7b79-256d-30ec-8eff-7a70bc4532f7 | -5.66073 | -43.7192 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7d9be311-13ac-336c-a7c1-dff3a4bb45e8 | -3.80607 | -43.2253 | 2025-07-19 00:07:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30de54f2-d12e-3149-bae6-2b8b0bab75f8 | -9.8062 | -48.54852 | 2025-07-19 00:07:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b4893310-1861-3356-945d-f09eb53ad3ad | -3.062 | -40.05388 | 2025-07-19 00:07:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 367312bc-2f71-3040-97c6-7f357ac1cffb | -4.66238 | -41.95525 | 2025-07-19 00:07:00 | TERRA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 60b44f79-ef26-3d25-b5aa-19c4d6a78202 | -5.76276 | -39.20823 | 2025-07-19 00:07:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 05639d9e-e7d4-3c43-82b1-459b4bfe1be6 | -5.64969 | -43.71007 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 44c09cd9-1ddb-3ae3-be98-58c1c233996f | -4.08772 | -43.4042 | 2025-07-19 00:07:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 989267b5-1f1d-35ae-b377-990285bd8254 | -3.82951 | -47.74685 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9d0d96d4-b7c1-310a-941b-30b3c1226495 | -3.82649 | -47.73417 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 76e915e0-92b3-3d9d-93b0-c7bcef392ec6 | -3.12848 | -47.01853 | 2025-07-19 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 9db36ff5-f72c-3c21-a2e4-c6850abd30c4 | -9.04969 | -40.57594 | 2025-07-19 00:07:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 02c0a689-bac9-3356-83e2-f47aefa538d0 | -3.59204 | -47.5237 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5690f03e-41e6-3cfc-9422-6721e32b6fec | -7.1741 | -44.10107 | 2025-07-19 00:07:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d7605429-436b-3439-b1ed-c7abeaee5a4c | -7.95057 | -43.95328 | 2025-07-19 00:07:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f65314c4-29a0-3d8b-ac55-caef836fd244 | -4.87256 | -42.87886 | 2025-07-19 00:07:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 11f73b8a-ca9b-3d6a-b768-a6df8c4e9d22 | -5.80376 | -43.6342 | 2025-07-19 00:07:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7496868f-479d-3e1b-ae73-e235b0048ce7 | -3.04124 | -49.42737 | 2025-07-19 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| aefa2a8c-ea3b-3e75-bb0b-01349502ce03 | -5.41539 | -40.74217 | 2025-07-19 00:07:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 67f05548-1c0a-3a82-9567-06970dc5997a | -8.53855 | -47.8453 | 2025-07-19 00:07:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 82a09aa1-f2b8-36cd-8a73-2d3ca77cc70c | -4.67126 | -41.95401 | 2025-07-19 00:07:00 | TERRA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0a8864c7-b322-3993-9046-2b88fc6d5874 | -9.61826 | -49.02643 | 2025-07-19 00:07:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8f9ce67f-0810-30f7-9f3b-2974d5166de0 | -3.82917 | -47.75347 | 2025-07-19 00:07:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f3a7dcac-eb84-3369-8729-59c9e0bb9caa | -7.71261 | -47.28496 | 2025-07-19 00:07:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c1b158b8-4dc4-30cd-8357-16baa4e7a4d2 | -5.65929 | -43.70876 | 2025-07-19 00:07:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 345e1a73-3e5e-35fb-b36e-e12157761e59 | -6.22079 | -45.8912 | 2025-07-19 00:07:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0ffbee09-7a70-32d5-86b8-6b86f9e34ef4 | -7.47918 | -47.50198 | 2025-07-19 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 53ebd8a2-bd35-33e0-9479-216ce4edfeea | -6.1602 | -48.07511 | 2025-07-19 00:07:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| bc0b07af-3983-3c2e-aa53-2c6a8e1c0b66 | -7.29847 | -46.26471 | 2025-07-19 00:07:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 70f734f9-9d50-33f4-aac7-134b29daa1b4 | -5.10418 | -43.15674 | 2025-07-19 00:07:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a26db1a7-a591-33fb-9d6f-21c6abd3cc6c | -3.11668 | -47.02011 | 2025-07-19 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 24e38ae6-fa2e-3eba-bc52-f4c974629048 | -4.24849 | -48.54225 | 2025-07-19 00:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7be12141-c1a7-3494-835d-16d2d3c4464e | -9.80953 | -48.57677 | 2025-07-19 00:07:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8f92af6c-0af1-3420-bbae-f99feb57c885 | -6.1572 | -48.05257 | 2025-07-19 00:07:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 0cc2b78f-0dc7-3fe7-873b-3c430d25f330 | -9.04846 | -40.56703 | 2025-07-19 00:07:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2fbb5515-8b7e-3b4a-8bec-3f7e5aae81c3 | -3.14027 | -47.01694 | 2025-07-19 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 59960e90-eecc-3ee6-83cf-c4793dae7904 | -7.49503 | -47.52119 | 2025-07-19 00:07:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d31af951-34da-3e7f-83a5-93585e1d610e | -7.48948 | -43.94021 | 2025-07-19 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9d91c568-6627-36f9-8794-0a00f95c1572 | -9.8104 | -48.5622 | 2025-07-19 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 78d89764-b9f7-354a-81ea-2ea8c8328758 | -5.6379 | -43.7175 | 2025-07-19 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 3db5c93b-6f07-3828-9f68-2ec998afa308 | -3.1384 | -47.0068 | 2025-07-19 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| b60a4ef3-76fe-3cf6-8812-be210614d8dd | -10.8531 | -47.1648 | 2025-07-19 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e6b98825-3200-31a2-9300-41b08aa5baa4 | -7.492 | -47.5134 | 2025-07-19 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 3723e6e4-205e-3e74-8614-f5fd74243c1a | -11.4977 | -47.3281 | 2025-07-19 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 29dc1ed9-b685-3580-ab48-a111836ad8a3 | -2.9109 | -48.2325 | 2025-07-19 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| cc3dba05-35be-346d-986b-e3361c775225 | -5.6567 | -43.7161 | 2025-07-19 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 370.5 |
| 1d465082-e532-338c-af7e-4497ae4ea67f | -11.7508 | -48.1825 | 2025-07-19 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 59ecd220-3a6a-3395-bb0e-78f315c4a763 | -6.1792 | -48.0494 | 2025-07-19 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 7d47f9b7-e1c4-30ba-bb8d-824c58675fab | -6.1606 | -48.0507 | 2025-07-19 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 039fed3b-6d3f-3f95-878e-8ec4c9d5087b | -11.7317 | -48.1849 | 2025-07-19 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 1ae1a33d-234e-3dff-837d-d58c56d63b44 | -6.1604 | -48.0724 | 2025-07-19 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d78b96a8-a8c0-3578-a380-a15744b3edd5 | -7.4733 | -47.5149 | 2025-07-19 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 30edce2e-95e2-3791-9247-f588b970f4ba | -10.6247 | -44.767 | 2025-07-19 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0545a685-566a-3007-b904-9b7bc5cffd3f | -11.7126 | -48.1874 | 2025-07-19 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4a593c20-816a-3fc7-865d-deb8c49dfd46 | -2.9108 | -48.254 | 2025-07-19 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| b38834d4-a2f0-3201-93c0-f91463abf358 | -7.4923 | -47.4914 | 2025-07-19 00:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 698e11c0-950d-3bf8-ae16-748718b70ab5 | -3.1383 | -47.0288 | 2025-07-19 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 5716a839-ad4a-33b1-995a-534504b153bf | -11.4786 | -47.3306 | 2025-07-19 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e324507c-d6a1-3149-aa05-5cc005f99c34 | -5.6569 | -43.6929 | 2025-07-19 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a778a84e-7334-3fdc-a164-8399fbf0dc1c | -7.4735 | -47.493 | 2025-07-19 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0977fbfc-dd7f-33d5-b3f9-b38db779f993 | -6.1608 | -48.0289 | 2025-07-19 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0fb48ada-36b9-330b-8fda-90a6a8ffd295 | -11.7313 | -48.207 | 2025-07-19 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 15655b0d-b1c7-3fd1-8671-e077862887d4 | -5.6565 | -43.7393 | 2025-07-19 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 47750c26-7f58-354f-a55c-724375c19142 | -10.8722 | -47.1624 | 2025-07-19 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e73787b8-44e3-3ed9-b382-74737f773045 | -3.1198 | -47.0075 | 2025-07-19 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| eae88275-9c94-3cb5-a260-d46ee1029a97 | -19.7822 | -48.1621 | 2025-07-19 00:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5b0c01e8-d53c-3f8a-915c-4af757705f8f | -5.6565 | -43.7393 | 2025-07-19 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7e081842-7014-3523-95e6-e6348b2f135c | -10.651 | -49.2967 | 2025-07-19 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ceedd8c2-6728-3f85-9cdd-453e87b0a5f3 | -6.1792 | -48.0494 | 2025-07-19 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 97b84e44-df3e-3b90-b4a7-5d0e16d43058 | -7.4733 | -47.5149 | 2025-07-19 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 801b4e23-360b-310c-beb6-580623e37963 | -11.7313 | -48.207 | 2025-07-19 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c3f18978-d910-3a33-9423-acef5886c8e6 | -7.4735 | -47.493 | 2025-07-19 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ef5f6853-54fc-392b-b5a4-7ff01d8966fa | -11.7508 | -48.1825 | 2025-07-19 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 4d504fc1-03d5-3f9d-9d61-76c125cc7594 | -3.1198 | -47.0075 | 2025-07-19 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| cb23121e-0a7a-34a9-bfe1-ecb49c75dfef | -3.1384 | -47.0068 | 2025-07-19 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c3c97626-f39a-31f1-a96e-b804bea2592d | -11.4786 | -47.3306 | 2025-07-19 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e7ecf9ab-dbeb-39be-8542-3c4f3d324318 | -7.492 | -47.5134 | 2025-07-19 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| df7630f9-7945-3dcc-8fc3-e2fb28f20364 | -10.67 | -49.2947 | 2025-07-19 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 1b80dd4c-4fcc-30fc-a23a-91e481f3184c | -5.6379 | -43.7175 | 2025-07-19 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 228.2 |
| fff848b6-ed90-3edc-9e31-b37546fa0919 | -6.1606 | -48.0507 | 2025-07-19 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 55773a30-b94f-36ec-821a-f0adb9876c80 | -7.4923 | -47.4914 | 2025-07-19 00:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 635b9824-b2c7-3f97-9580-84d878d74f6b | -6.1604 | -48.0724 | 2025-07-19 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b0f8192e-b10a-3eff-819e-09a1166afee5 | -11.7126 | -48.1874 | 2025-07-19 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d00b3815-fe78-3b04-9193-dfaf2d34fa88 | -10.6247 | -44.767 | 2025-07-19 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bff963a7-21a2-3611-a26a-b2918d40bac3 | -17.7776 | -40.1226 | 2025-07-19 00:20:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 6e09d5f2-cae3-315c-97d5-77b763e0a6f1 | -5.6567 | -43.7161 | 2025-07-19 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 368.6 |
| a4d32198-0e9e-3f71-9b82-4fc2c13b4b0e | -9.8104 | -48.5622 | 2025-07-19 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f332538f-255d-3b3c-a77c-3a5f11da0b38 | -5.6377 | -43.7407 | 2025-07-19 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README3.md)
