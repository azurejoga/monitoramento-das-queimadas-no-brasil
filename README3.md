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
| f6b731d4-40e2-31c6-b1b4-4343e41c8982 | -4.75102 | -44.452 | 2025-11-25 03:46:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5db20419-80a3-321c-9dca-e9bffba951b5 | -6.83846 | -46.27072 | 2025-11-25 03:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff93e9c-47f9-34e2-8b61-626a3e796c2a | -4.81417 | -43.82417 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c7ff465b-9ab6-3a25-8a12-34c1efd5de2f | -6.89557 | -42.8461 | 2025-11-25 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 536045f7-47ed-3e12-a010-dd83c8767cb4 | -4.65173 | -45.68872 | 2025-11-25 03:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d857507-4c1a-399d-a05a-b293284f6132 | -5.96159 | -44.7254 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f81ce8f-e41c-3b2f-abce-fa3e3e1ae9ca | -8.54585 | -40.21577 | 2025-11-25 03:46:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 19047574-52a1-3b31-a51f-236c28fdd849 | -5.11816 | -40.80869 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbf187d6-a990-3427-980b-1f6cd94aa587 | -5.9018 | -44.52128 | 2025-11-25 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b88b6af5-e0f8-339b-9bf6-8760a0f59986 | -5.58346 | -45.17523 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c26195-a0ee-3fa6-936b-aedea83c949f | -4.94324 | -41.16267 | 2025-11-25 03:46:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89733648-1375-3e43-adca-cc449840acb6 | -5.35168 | -44.88367 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 460f3463-29ab-31ba-85a5-c8c5f33d427b | -6.95384 | -36.81081 | 2025-11-25 03:46:00 | NOAA-21 | JUNCO DO SERIDÓ | PARAÍBA | Brasil | 2507804 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a15130e6-72d3-382c-88cb-a6e3571b11db | -6.68416 | -43.94724 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| add38560-257f-31d6-8c1b-89217a7fa22d | -6.0783 | -39.54958 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7eeee7b5-d4cb-3fc3-ad87-d1638930c686 | -4.75168 | -45.10864 | 2025-11-25 03:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76e0e3a1-a84b-3c2b-9505-7ab8d5c30129 | -7.28387 | -45.11861 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a22a293e-0a95-376e-8993-7b08f902f62c | -8.06813 | -43.13175 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| afb80a24-b1cc-3994-9e16-4ca95dac03a6 | -7.1663 | -44.99617 | 2025-11-25 03:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09ec05e9-2ac5-3bec-93f0-287a52398d50 | -5.85004 | -42.93233 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a0e85b4-15d5-382c-868c-9b1facf5e93e | -6.12359 | -42.94475 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fad24fde-9a9d-3784-81cb-11829d0aba63 | -5.95965 | -44.7292 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f7c60c6-9e1b-3996-8826-a8c68d4d141e | -7.07217 | -45.20804 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bc853a7-158a-357a-bf0e-bc921bde8592 | -6.67923 | -42.47907 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e857de74-af1a-36d5-84e7-98e799b9a489 | -6.68498 | -43.94249 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b682619b-df36-3efd-abf7-571a83dc8f94 | -7.46739 | -45.18994 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4095b801-c72e-32d9-bc36-f80826783bca | -4.33412 | -44.32989 | 2025-11-25 03:46:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aafce633-3dac-3e95-9812-1ad321a520f1 | -5.57993 | -45.16519 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07e89072-4a59-3afe-b1f1-981d63d8c56b | -6.50564 | -38.8261 | 2025-11-25 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1ca8a15-4015-30ae-a18b-810e8b4dac00 | -6.8439 | -46.27155 | 2025-11-25 03:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d4cfcff-f11f-3f26-a284-db0bc9da1471 | -4.81266 | -43.8271 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3b631617-b151-3674-a729-faa0bf7ccc87 | -4.08463 | -47.09761 | 2025-11-25 03:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 609fd198-aafc-33b4-b5d6-0d2656ae187e | -4.37462 | -46.11103 | 2025-11-25 03:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5d916f0-8730-33f2-862b-6b71db8eba0d | -5.58667 | -45.15693 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df9de7a7-d1ba-35bf-b84b-9e74954557df | -6.45765 | -38.37834 | 2025-11-25 03:46:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 804a0cdc-b9c8-3823-9155-cb2812c01bbd | -7.3011 | -45.28358 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c909089-35c8-39a7-8f80-558e23e11b2b | -6.69064 | -39.80222 | 2025-11-25 03:46:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1f895e56-64c0-3fbd-84c9-363a52997498 | -5.54398 | -39.23868 | 2025-11-25 03:46:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 842d8cc6-3711-327e-bd40-ab2e4c3ecec7 | -6.69291 | -39.80243 | 2025-11-25 03:46:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 957ac14a-2757-39ca-baf5-b78d1a696ba1 | -4.82301 | -43.82352 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| be726c3a-c16a-37fe-8270-a0d2071f0e8c | -8.06025 | -43.12615 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 98d3a72b-7477-3434-ae1d-26ac92c172af | -6.60159 | -43.68917 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c086d16a-220f-3a05-85fe-685909459915 | -8.06454 | -43.12689 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f390f7c8-f55f-3d29-8194-64476d50595b | -8.06672 | -43.14003 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b1036043-6792-351f-bdb3-489a90335146 | -6.08706 | -41.68818 | 2025-11-25 03:46:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a1242a81-cac7-3d1f-82b4-be47dfc3ea3c | -6.6858 | -43.93776 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1b5f07da-8dee-3690-ad01-46198d7a8317 | -5.31549 | -40.87284 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7d44dea-a347-3fdb-bb00-f849684196b9 | -8.04529 | -43.13623 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 610e3746-20ad-3764-a9fc-1f25eaf403de | -6.89627 | -42.84201 | 2025-11-25 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 60bc395c-b5dd-34a6-991b-cf8dd7fbdabe | -8.05098 | -43.12878 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 64a5ca60-5e7f-3362-95c6-09ccc1f1c800 | -8.16542 | -43.19805 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| aca7af63-c376-3756-b4e2-f2aa4d8af0c6 | -7.32844 | -37.32746 | 2025-11-25 03:46:00 | NOAA-21 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c28bd506-29a4-3065-b058-9cf441db5642 | -4.7286 | -44.73492 | 2025-11-25 03:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9530489b-6e7e-3658-a967-458248bf6043 | -4.81804 | -43.83003 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a24e819b-3cc9-387b-9068-0f50202103e7 | -5.05106 | -44.19617 | 2025-11-25 03:46:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1be4ea25-9a44-31fa-a759-c8e78c0ec74a | -5.83287 | -42.92531 | 2025-11-25 03:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ceee0a68-528e-3060-98c0-99a7e8aa9458 | -6.68335 | -42.48027 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 54353ef3-9892-3d84-b0e3-d9630598d0c4 | -6.39492 | -39.67318 | 2025-11-25 03:46:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bd9accd-ff9a-37cc-9ec8-59f30cecd6a9 | -4.72807 | -44.73801 | 2025-11-25 03:46:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d984f040-773a-34ef-a71b-45d4d2b4450f | -4.55202 | -43.29542 | 2025-11-25 03:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 38c4cefd-b61d-341d-8227-7e5e8e451654 | -6.68796 | -43.95288 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7a04c92-288d-398b-8af5-2ee9d1bbdda6 | -6.68268 | -42.48438 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| be42e99f-7bb7-3b98-84f9-a47ffa0d821c | -7.04294 | -37.30331 | 2025-11-25 03:46:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ef6c703-65e0-3b2b-b3fb-c27442d32060 | -5.57339 | -44.97324 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c9d3d50-6c2c-353e-bdfa-82d5020cbd1a | -8.05527 | -43.1295 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b8896687-cff1-3035-a746-4bb20083e300 | -8.05597 | -43.12542 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4cfac56d-d014-3bae-a2df-d7c01017a7ff | -8.04599 | -43.13214 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| b24ab931-0a13-34ff-8bbc-d524bad3476e | -4.60118 | -44.87973 | 2025-11-25 03:46:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da17188f-daab-36a1-8bbb-f67ba6cb3878 | -6.67854 | -42.48328 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ba2e3b2e-b998-30e0-8493-cd73f46b2df4 | -5.58614 | -45.15995 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e4bb3a0-480d-3c37-a096-e98c2fb568a6 | -6.80982 | -38.57293 | 2025-11-25 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d25156d-1d88-3aa4-8be4-5764df856259 | -5.5932 | -45.18 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 462031ea-3d9a-322d-9eb3-6888f6d9a1db | -7.566 | -42.86412 | 2025-11-25 03:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| baad2f24-839c-3e66-bb9a-566074bbe49c | -4.83317 | -43.82716 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ac7e38f-4806-3b37-b72f-3a0681652219 | -8.05956 | -43.13025 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bf993c63-a0d0-3cee-825f-0ab149997eb0 | -4.8293 | -43.82129 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27a51eca-fc34-3a3b-b13e-c894b2ad8e78 | -7.46192 | -45.19183 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cf44724-5e6f-3de4-b6b4-49b0e991be13 | -4.82842 | -43.82642 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cbb14cbb-2fe8-338e-bf68-0f73269477e9 | -5.3175 | -40.87055 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32558f43-1c5b-33a0-a90e-1404be5dd346 | -7.71851 | -35.09616 | 2025-11-25 03:46:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7680d764-c19d-324b-ac28-8b82acc3f43a | -8.05168 | -43.12468 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8d73c456-ea06-3cd7-9b21-f9ab8f27933f | -4.83405 | -43.82205 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 716e100b-8e51-3beb-893f-12875cd27902 | -7.56371 | -45.86882 | 2025-11-25 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 060a6e73-901c-30d4-96bc-c14a1f7e5362 | -5.58507 | -45.16604 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 233f5f11-1892-389c-946e-b213844b0808 | -4.81825 | -43.82277 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1f008aa-34c1-36ee-8bab-9d05d2c05de8 | -5.5856 | -45.16299 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b3d9c28-99a4-3cd5-bdb5-f509aceddd6a | -6.09425 | -39.44953 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3e9feac-5d7d-3abb-9159-b286d91837e7 | -6.85847 | -39.36496 | 2025-11-25 03:46:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98412083-e194-3ecb-abe4-f3502a6f4f7f | -4.58561 | -44.06521 | 2025-11-25 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60c75506-d1fc-3d9e-837f-f320f6b80cb0 | -6.31495 | -43.82175 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08975d33-33d4-36d5-b172-6093b8609da2 | -6.07761 | -39.54916 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b5d9db44-cbba-3c4f-a5c1-f60ff97cfe39 | -6.85497 | -39.36441 | 2025-11-25 03:46:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a028d151-dd95-3437-b9b7-dca019b7c131 | -5.63768 | -43.92606 | 2025-11-25 03:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a439e7f8-2128-32d5-9962-d86a393abe41 | -6.70791 | -39.66747 | 2025-11-25 03:46:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 45143a27-7d96-3713-9beb-a63c97158feb | -7.46296 | -45.18593 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b325a182-c1a1-3a41-a309-15594ffc0161 | -5.03311 | -43.261 | 2025-11-25 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b47a5d3b-8a50-3c59-a4c2-6ae18479a343 | -5.42631 | -44.83678 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b3c14e4-0f22-31cb-b3a5-3bfa1ecbdc92 | -6.07476 | -39.54891 | 2025-11-25 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ac69e16-f6e3-3270-822b-73d13ed968d8 | -6.73084 | -42.94178 | 2025-11-25 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf357472-6d07-3044-a2e3-abd43141d316 | -3.82379 | -40.69529 | 2025-11-25 03:49:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README4.md)
