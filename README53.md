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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61a4ef11-ae9e-393e-b086-b2ff235c36b3 | -6.09051 | -42.44672 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc22bfec-2641-3a0e-b8e5-120b5a1cdeb1 | -4.58105 | -50.68894 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c229f222-01fd-3baa-82e6-50980b7c62fc | -5.5233 | -42.72628 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36e13694-6ffe-3d71-9825-8c3a8efb9903 | -7.01625 | -44.46628 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d63edb-63aa-3e8c-97f4-de7d43a545a2 | -5.77409 | -42.85221 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9e910fbe-9b26-3514-8a5f-cdf4653d8829 | -6.6888 | -42.79543 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3eb7eb51-8be5-31e3-a747-1d06cfd0792b | -6.34012 | -43.74971 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f1f50d-bada-335c-8c1e-4adaba67529d | -5.73779 | -42.81985 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 36752c87-31a8-3e8f-a2c7-50e5d4af6138 | -6.21306 | -44.20702 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f7f7511-63eb-3c16-a377-72c3a5dbe451 | -6.17037 | -44.15955 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cbd8a04-9d3e-33e8-b9a2-fe39d66e3c8a | -6.69349 | -44.5973 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6e3e68c-4f33-3697-a4ec-8366d316d894 | -6.28962 | -43.46481 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ed62533-2681-3fe4-9cf3-5c03b8199d17 | -6.51166 | -45.20845 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1555c9-716e-3417-82e8-578dea21fac8 | -5.25341 | -44.45734 | 2025-09-30 04:38:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da591732-d8fe-3744-96aa-68f474934a64 | -5.24143 | -43.74084 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2fd3d8c-dece-37e1-9ff7-738b586720a2 | -4.40768 | -44.39866 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cfca546-9ec9-3b55-92f0-f6d33828e183 | -6.50811 | -44.12048 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcdf5612-7025-3bc1-a4ae-7fb1a0e9b92f | -6.50711 | -45.21264 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37cf9430-93ee-373d-949b-21cd8a306157 | -3.4921 | -48.93976 | 2025-09-30 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f24b61b-7eb0-3440-9dec-509b9fc16949 | -5.77853 | -42.85293 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d1399a25-b46f-36ed-ac72-00131f1b17e1 | -5.82574 | -42.77953 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01b9d365-5627-33cb-93ef-a3e927e711d9 | -5.24973 | -43.74212 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8a684ad4-431a-3d26-9b59-094c56cbd549 | -6.27958 | -43.65783 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30fb2c55-a29c-3044-b1de-b8e725f11395 | -5.8046 | -45.73826 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30893423-fe16-3c2c-b47b-39eb454ce791 | -6.2422 | -44.88608 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ce3ddb8-d443-336c-bfa4-b896c9de120a | -6.18519 | -45.37402 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ed8b94a-5b38-38a8-bfa9-d99622335e7d | -7.17842 | -41.69944 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6595567a-a95e-3519-9591-1b5682c3a520 | -6.84039 | -44.83125 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 30c2f8ac-79c7-3427-a09a-cea01dab5f77 | -6.8388 | -44.83736 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 92b8ca75-1401-3ce3-adb8-f2b31bfed568 | -5.70111 | -42.64308 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b0b0565-07df-3e8f-b31e-859799464a2b | -3.38298 | -52.71572 | 2025-09-30 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9915c9ff-eaed-3542-a17f-d9d25a7409cf | -5.72081 | -42.87563 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ebd95a5-9b7c-3f3e-ada6-dbfb54c59575 | -6.81138 | -44.20853 | 2025-09-30 04:38:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa191d30-1cb4-3c6b-bf31-d0f6a7221ecf | -5.27921 | -43.16143 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11dc73ee-15e1-31c1-a2d0-e1bc6250596b | -3.93813 | -51.33053 | 2025-09-30 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3effd36e-aeef-3551-bc95-45c44365be21 | -6.27592 | -43.65316 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 217315a4-846c-3cd4-ba9a-cda3081b129c | -5.82127 | -42.7788 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| abd9dc31-acd0-3c4d-9efd-5424dd7cdc84 | -3.47857 | -51.59592 | 2025-09-30 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8edc1e9a-0091-39c9-a40c-83d47c6c432d | -6.4666 | -44.21077 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efa463ad-6e63-352f-a5ef-f1e4198904f7 | -5.31066 | -43.15792 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9a488a8-6f94-3652-834e-81861d54fb20 | -6.30508 | -43.8089 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6536fec7-c611-3c2c-b9f3-f10a85f876e6 | -5.75124 | -42.8531 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da301235-1a31-3aa8-95f4-3b2ca6602990 | -6.26742 | -43.65199 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e6ee62d-994f-37e9-8508-4597b3e14651 | -6.50092 | -44.25949 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66bf53af-eebd-3caf-a466-eb2da687a5a2 | -5.91372 | -43.91748 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25027d4d-6310-3b52-9da5-496364da5d4e | -4.81387 | -42.77139 | 2025-09-30 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7fb5d3b7-0af3-3fde-b500-1536b655d563 | -5.62817 | -42.83261 | 2025-09-30 04:38:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 60ca2dc6-20dd-37d4-923f-6af6fd77c731 | -6.15005 | -42.79339 | 2025-09-30 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1e0850d-2bd4-320f-bbb9-4638bfa28705 | -0.39361 | -52.04668 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa4b405f-317d-3885-92f3-cbee9f5b7a85 | -6.67154 | -46.17292 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45f042be-4d88-321d-9143-57bcc2fcf8e9 | -12.85261 | -47.01167 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d6129c51-5937-3fdc-a6a2-da7832a0a5bb | -11.20603 | -47.21267 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecbacc46-251c-39d3-9a02-e34542f3a519 | -6.82814 | -46.62923 | 2025-09-30 04:40:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec914411-2637-3380-ac57-f86ec53003ef | -13.78722 | -47.95757 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 519a4d4f-1d26-342b-999c-2ef64326be9e | -10.61961 | -54.95406 | 2025-09-30 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4774d400-13f7-3aeb-a068-08700532b068 | -11.07036 | -47.82072 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f007161-60ab-3866-a9ef-28ef422147e9 | -12.78684 | -46.90059 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10adb757-65af-3e2c-873f-d7c37a611904 | -7.47672 | -49.46309 | 2025-09-30 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 145d3ff0-5e3c-3bb1-8031-e6d51a8b237e | -10.64867 | -48.59316 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83dfc668-b6e3-3d8c-b7d6-e6fc33713b70 | -11.94411 | -43.92105 | 2025-09-30 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ce63672-7217-3a84-a0d8-9f9d5e416a30 | -15.00196 | -42.42271 | 2025-09-30 04:40:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0648d608-da09-3024-8eb2-7bc7bb2016a3 | -13.0041 | -49.4403 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c850eb83-a7f9-3b01-9290-bbd260c131ea | -12.17974 | -48.35255 | 2025-09-30 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72f92597-34b6-3d19-8591-78697fd1f2f9 | -7.23485 | -46.76571 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a1867af-9426-3990-9621-f28e0e565697 | -7.13045 | -45.50229 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21e14cee-9d23-3373-bee7-8b54c7330199 | -7.50371 | -45.44343 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c958712e-f21e-3230-9f87-1ff09d202982 | -8.06223 | -54.86658 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9fc549a-7059-3eec-863e-5e9ad0319965 | -9.02785 | -46.71003 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e140834-3cca-3208-89fd-8c75ffa30c48 | -12.94287 | -46.75632 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e0b0b3-69de-309f-8af2-823ea0f187e3 | -8.85486 | -46.58914 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e8fc31f-64e6-310e-8cb5-35ee71abc93e | -13.39672 | -48.16448 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6407de2d-f2d2-3112-abfd-4bb7b07a631d | -11.45859 | -45.0155 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b42840d5-db4b-3263-9425-095ab0bcb577 | -7.76099 | -45.76853 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0c268ae-fd8b-3f6e-b3c7-fd638b02417d | -10.71076 | -53.79702 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6afb7a15-6993-3d1f-b721-adebcf5650b7 | -11.2481 | -47.23527 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1cf49ae3-511d-36d9-b597-5db62e63a701 | -11.46297 | -44.98426 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9630283-f601-39f1-b2bb-df8b50829015 | -9.55244 | -54.63872 | 2025-09-30 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 765a0ab4-ca84-3ba0-a853-7928f10a439a | -7.11395 | -47.77932 | 2025-09-30 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1163a7c-405b-321b-bf65-2beb25169e5f | -11.61813 | -52.23957 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87e859a1-efcc-30dd-83b6-e3b0fcd92990 | -10.8075 | -45.35901 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b52403c-2391-372a-919f-2f5361e93467 | -12.82699 | -47.00299 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64bab8d1-11cf-3f99-8986-31d8e1c47c8c | -13.41644 | -48.19963 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d5ed53-f9c7-35b4-a0e8-9f937000b53c | -9.96161 | -48.80232 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3f381a3-6f39-3d09-b684-e182e3954428 | -10.83733 | -47.95551 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f3660ac-e049-3946-b709-2e764e793a11 | -11.64874 | -47.49284 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35325b68-ebda-3362-b150-8d1a815acc9b | -13.72941 | -48.68274 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0ec7fc42-a9c8-3f81-bacd-6ab1684ea9c2 | -11.45937 | -44.97947 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c831e1a6-8a12-3eef-ab6f-6a6d88806236 | -12.96605 | -48.41407 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a94f7c1-80c1-3a13-ba32-0d49386c3853 | -11.16379 | -54.12024 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a2c5ee3d-bf2f-3d55-b332-6158b67bf430 | -10.84721 | -47.96131 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 198ae77f-1e13-34c8-9ead-b3305a615449 | -11.43762 | -55.03775 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dc7db0d-f7a6-32e7-94e3-ddea7a629ebb | -7.65423 | -49.5694 | 2025-09-30 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea2a7247-25e6-370a-ae72-c1f5566e379a | -8.84434 | -46.66217 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7b5afdb-6a1b-37ba-95e3-e87ecb451aa7 | -10.19505 | -44.8876 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5dc94dbb-1e12-31a6-95dc-fd63297315eb | -9.42169 | -54.71932 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6063d2b1-fead-3c7d-abf7-87cdeeb20245 | -10.19453 | -44.89143 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f675e5fc-1201-30e7-ac04-1ca632d2001c | -13.25229 | -48.43811 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8a66a05-13c1-311d-aec8-17093320f3eb | -12.83513 | -46.99961 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b262d1b-22f2-37d2-90b4-38f70fe72e94 | -9.51772 | -47.69638 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 073c93cc-4200-3037-8ad4-4e9da4b237cf | -12.95202 | -48.4121 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README54.md)
