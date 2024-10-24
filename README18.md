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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27f324d6-b145-33ac-87ca-f8470cc3adc3 | -5.16633 | -37.71343 | 2024-10-24 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d557ee65-11ba-3f89-b9e0-188e5550424a | -5.16279 | -37.71286 | 2024-10-24 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c4e89d3a-2396-3f08-afef-83c87b6b26d5 | -5.11914 | -39.30498 | 2024-10-24 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c763bb60-a960-3463-9c58-ca736951203f | -5.07824 | -42.56561 | 2024-10-24 03:40:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 776ea49f-5ad3-3728-8344-937ad59a37b3 | -5.01759 | -43.65924 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff3e7ff6-2e4c-35e0-a8ee-fe72e54f3b90 | -5.01706 | -43.66234 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2846ac7c-a7b0-3771-88ff-2117c0ec0bf9 | -5.01653 | -43.6655 | 2024-10-24 03:40:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bb2d6d3-e221-3e1b-86a1-0e5ff86919db | -4.86271 | -39.01286 | 2024-10-24 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ea91069-0130-367f-8ed5-6fb6b354b09b | -4.85393 | -43.25658 | 2024-10-24 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45ba2bd7-0183-3f89-a326-31752d5dd4ab | -4.85343 | -43.25954 | 2024-10-24 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6823e01-cf39-35e2-9237-eeb910dd9bc1 | -4.74668 | -42.77243 | 2024-10-24 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d600142e-6b6f-39c3-8362-42aa86e779c9 | -4.74229 | -37.80354 | 2024-10-24 03:40:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 63ba335f-1d5b-37c8-8938-07b1460a2663 | -4.72098 | -38.86131 | 2024-10-24 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f621d43d-70d6-300e-955f-1b2eaf9c43bd | -4.7172 | -38.86067 | 2024-10-24 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb827d07-83b9-3e8c-8ab2-436381b40a46 | -4.51006 | -42.6426 | 2024-10-24 03:40:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e1a65ad-63f2-35c0-8b10-d8329623cb2d | -4.44325 | -42.918 | 2024-10-24 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81ee62c7-95ee-3005-b1db-16266d2b5fb0 | -4.44277 | -42.92082 | 2024-10-24 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e9a799-b413-3c31-b983-64216a8419c6 | -4.43825 | -42.9172 | 2024-10-24 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 698ba200-bbd5-3fc2-b457-8ce3e2b8ac07 | -3.85464 | -40.69906 | 2024-10-24 03:40:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e9424cc5-62aa-30e9-89c4-2e2f9b76c4f3 | -3.85397 | -40.70314 | 2024-10-24 03:40:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 337d65d7-5f07-3949-abef-b0f28ff69842 | -3.80479 | -42.55221 | 2024-10-24 03:40:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96936904-ca3b-3ff1-a290-3946391a4b60 | -3.71522 | -41.68975 | 2024-10-24 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17a20d2f-1f15-3853-887b-6b2c5714bf0d | -3.71138 | -41.68411 | 2024-10-24 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ccc59493-a422-335b-8a1b-64fb3a17ffe2 | -3.71058 | -41.68896 | 2024-10-24 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 3808ff5f-abd2-32dd-b50f-b19b72af370e | -3.70674 | -41.68333 | 2024-10-24 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| a0918c0a-4107-37b4-9b27-cf808fe00f3e | -3.70595 | -41.68819 | 2024-10-24 03:40:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 4080453d-85ed-3381-983d-7d8a587c8bbc | -3.69855 | -40.79853 | 2024-10-24 03:40:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f47d24d-5288-3a77-ab50-9ad9f66fbe87 | -3.52767 | -43.61741 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 791ab8dc-57c0-3937-8c44-a4f2ab8becb8 | -3.52711 | -43.6208 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62759053-45ba-3f7a-af9f-aba244ec0eb0 | -3.52672 | -43.6149 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c344e7ee-303d-3d57-94df-207cd5d24528 | -3.52614 | -43.61827 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca8b52ff-f6ee-37ea-875d-6c8f0bd3d601 | -3.52292 | -43.61311 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4353d611-9928-34d1-9457-d3e44e9dd3ee | -3.52236 | -43.6165 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 280c0310-90eb-3fcf-98a6-86839194367d | -3.5218 | -43.61989 | 2024-10-24 03:40:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05b87dcc-86e5-3d57-86cd-2c0ac42d4ff0 | -3.16326 | -40.20958 | 2024-10-24 03:40:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc1dc54a-80cc-376e-9802-f91940334505 | -2.89417 | -40.2423 | 2024-10-24 03:40:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 261fce36-230c-3236-9555-8aa867364829 | -7.53416 | -45.84268 | 2024-10-24 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 515742fa-b45a-3810-9e23-941bdce3de0e | -7.53343 | -45.84673 | 2024-10-24 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c4e2ce2f-ef97-3e58-88f2-ab671cb67649 | -7.53271 | -45.85072 | 2024-10-24 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eed0abf4-a2b3-36db-b5be-0e49a966eadf | -7.53199 | -45.85469 | 2024-10-24 03:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6596889-cb69-3179-b13a-23a52f76fa7f | -7.20468 | -46.37377 | 2024-10-24 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2011ab09-cf04-381a-869d-e1d0d4dd3875 | -7.19939 | -45.8756 | 2024-10-24 03:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6c57f2ed-04c1-336c-bf08-962a9ff78869 | -7.1989 | -46.37157 | 2024-10-24 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24265188-e578-38cc-a318-1a49e7bfe363 | -7.17501 | -44.99957 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4147bee9-2626-3927-b392-4ca5883e5a52 | -7.17399 | -45.00252 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fa0ffae-f596-3419-856a-ee14d7ff861e | -7.16955 | -44.99853 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0918ed6f-a788-38b2-a8b2-7492c3e46325 | -7.16942 | -46.33052 | 2024-10-24 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 992bf701-51e7-3a2e-9dfd-ddea2212c479 | -7.1504 | -44.81819 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 491406b9-c303-345a-8c31-4a2cced57ca5 | -7.14978 | -44.82166 | 2024-10-24 03:40:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 562f8ca8-b880-305a-848e-21b12ca90e68 | -7.07495 | -45.30371 | 2024-10-24 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b82b1fb6-a26c-369c-ad66-09b2ae29e3b4 | -7.07007 | -45.29868 | 2024-10-24 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 647f33bd-082c-3618-88cb-0d908003daeb | -7.06939 | -45.3025 | 2024-10-24 03:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf480d4c-6073-3bc1-aea9-a61f6bee23c1 | -7.0101 | -45.03222 | 2024-10-24 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 349ca4af-2861-354c-9b6b-0c42254f40d4 | -6.93533 | -45.07038 | 2024-10-24 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 66569df8-d03c-30fe-8801-b6b90b1eef5a | -6.93472 | -45.07388 | 2024-10-24 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 703512f7-58fe-3e13-b595-63969b88603d | -6.9345 | -45.07246 | 2024-10-24 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c999ede4-9bed-31d1-a17e-03ac110e046a | -6.93388 | -45.07589 | 2024-10-24 03:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1415c9ee-2b5b-33dc-a06c-b674e849daf9 | -6.82829 | -44.38668 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1dc4828d-9263-34e8-b71f-29f8514bbd13 | -6.82771 | -44.38996 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e62fceb-e09c-3925-99e6-0102939c218f | -6.82303 | -44.38551 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4addfa77-3626-3eec-9275-9a7a192c2382 | -6.81345 | -44.47159 | 2024-10-24 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7dc3fab-e6e6-3d50-a3e4-e7dca7340f06 | -6.80755 | -44.47399 | 2024-10-24 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 516ffb94-d3fb-3a3f-886e-4b8d898d1945 | -6.73514 | -46.55903 | 2024-10-24 03:40:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cff21f96-f7b1-3646-8c62-0a126d053efe | -6.72025 | -44.68587 | 2024-10-24 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15573138-87a1-3765-bd9b-6d2e93d5eaf2 | -6.71962 | -44.68937 | 2024-10-24 03:40:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 17516f4e-5859-342e-bc59-c52f1a48a162 | -6.58872 | -44.18228 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3da45ac9-5d5b-3782-ab65-6669c4806911 | -6.5841 | -44.17786 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee1483fa-3fd6-3c72-b74c-e605f8dc0301 | -6.58352 | -44.18113 | 2024-10-24 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6ee2058-9acc-3d1f-a8a2-3a206860c775 | -6.53938 | -46.0813 | 2024-10-24 03:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c75decba-0d22-37cd-8470-18fe8923e8db | -6.5366 | -46.0775 | 2024-10-24 03:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4a1b412-aea5-36de-9a34-6e276faf98f3 | -6.53416 | -46.07636 | 2024-10-24 03:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af662f3-165e-3a7d-b094-f2de483d35ce | -6.51809 | -47.26979 | 2024-10-24 03:40:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce22be6b-9fe6-3146-84c4-353d349ee971 | -6.19039 | -44.52728 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5afa9c1-da03-3fc3-b88d-6ed9c26b562c | -6.18498 | -44.52639 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f687e85-918e-3ff7-b875-afea7d194590 | -6.07181 | -44.63036 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6727df0-130f-3c38-9e35-baf5b6271b9b | -6.06703 | -44.62568 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d1898e50-c65b-3320-aa84-524ed301ef6f | -6.06639 | -44.6293 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f0856a2-31cb-3072-9fbc-720f80dae496 | -6.06599 | -44.62593 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb18068e-97b8-378e-9167-8d8c2d95d364 | -6.06537 | -44.62953 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51823fa6-3c42-374a-a6fb-abe76fe21451 | -6.06095 | -44.62831 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d28d7801-6524-357f-bcb8-514e29747d50 | -6.01858 | -44.86979 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2a03934-d635-3647-9f56-b659301f7af3 | -6.01785 | -44.8689 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7db4af60-0f58-3ef6-ad20-e88eca97a464 | -6.01368 | -44.86509 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af59b052-0d7f-3cfd-90de-7a494972f758 | -6.01304 | -44.8688 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e635d55-f4f0-309e-9e2d-f6b0ed3390ae | -6.01299 | -44.86421 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd3c73a1-073c-3813-91a9-eaac5c6e2ae6 | -6.0129 | -45.96902 | 2024-10-24 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3026d07-1a0b-3ea1-ae09-e0553042f8a8 | -6.01232 | -44.86794 | 2024-10-24 03:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9601919c-c2c8-3da3-b705-c039300f36f6 | -6.01059 | -44.52587 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ac75a70-5bfe-3c6d-a63c-ea05ebf0022a | -6.00995 | -44.52948 | 2024-10-24 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a785397e-1a96-3c88-a5ff-a0d31b3f9f43 | -6.00707 | -45.96732 | 2024-10-24 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0c3d4a9-9b6b-3a16-a052-a14d845a2320 | -6.00627 | -45.97183 | 2024-10-24 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74a08bea-87b2-3a31-82f0-3cc68d9b21cf | -5.84587 | -47.28881 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1139a338-4e9c-36cd-8cc8-0677b1fd4174 | -5.83943 | -47.28751 | 2024-10-24 03:40:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6821d02f-897e-3c7e-9ea4-b7f646a088fb | -5.76307 | -45.55562 | 2024-10-24 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e78384b-2467-33ca-b7f8-55b228f7d96a | -5.70559 | -45.00231 | 2024-10-24 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7e11386-f9ce-3b14-ad8e-945718c2e2d4 | -5.70494 | -45.00597 | 2024-10-24 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7a1a6f6-57a1-304a-a25e-55b4842d02c8 | -5.70105 | -47.35014 | 2024-10-24 03:40:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265e7692-0791-32ae-9add-c472b27aa408 | -5.69533 | -47.34644 | 2024-10-24 03:40:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 336a80b0-ba9c-3af8-a31c-bf27e9f513d7 | -5.69457 | -47.34888 | 2024-10-24 03:40:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad4aa66-5a29-3f02-9675-d1b1c1407aeb | -5.69435 | -47.35201 | 2024-10-24 03:40:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
