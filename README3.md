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
| a54326b4-18eb-38ba-bc46-885f51b26df8 | -4.4261 | -47.75803 | 2025-10-12 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4bf2d07c-b0c5-3a3c-a005-40e0ccac2b1b | -8.33477 | -46.23687 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ed8fe39e-3f5e-3322-9471-c3dc7129e0f5 | -7.3366 | -44.04321 | 2025-10-12 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 35ed8da8-9a9e-3801-aa45-7beac260e0ba | -6.76889 | -42.82917 | 2025-10-12 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 92acd707-1ea5-3705-91df-94e8198732af | -6.75973 | -42.83035 | 2025-10-12 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| fb6e1a58-6030-3522-890e-2c9e5a092773 | -6.47535 | -44.15511 | 2025-10-12 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6686e84a-57b7-340a-b1ca-6fe953ff0993 | -5.20406 | -44.35837 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e6508f10-45fc-3434-adf1-95ab7d4684a0 | -6.69931 | -44.29392 | 2025-10-12 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9307f402-c2e5-3c89-b20e-41a13b909b70 | -6.47094 | -44.64147 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f97bf14b-6a2a-3ac2-90b2-96bb721a25e2 | -3.60555 | -41.63785 | 2025-10-12 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| dcb1eaa4-86ca-311c-9422-8a4f79bdee76 | -7.33784 | -44.05207 | 2025-10-12 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55f990c4-0e87-3885-a6c1-eac292c01cdf | -4.42698 | -43.47644 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fbe4b40a-0ed6-3e7d-b9a1-3278efce95f5 | -5.59272 | -45.8365 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 728b0783-cdea-36e8-ab95-6ed6760fa558 | -6.7611 | -42.83982 | 2025-10-12 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 9d10937d-73d0-30f3-af11-26e3e30a0e2f | -8.32764 | -46.23362 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 44e309e0-fe45-31e9-8839-e4473f06176b | -3.95599 | -44.2608 | 2025-10-12 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 48b0d3ed-9260-3a02-b1c7-d0cf1aecb86a | -6.25046 | -42.74483 | 2025-10-12 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a5ae70c3-1ce1-3bbf-973e-5a6278d9eb20 | -4.27795 | -46.92597 | 2025-10-12 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| de0a9f2c-8530-315f-9a0e-6ce1316dca1b | -3.73969 | -42.58641 | 2025-10-12 00:13:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5d219939-02cb-37e6-985c-21d86c28aae7 | -8.21583 | -43.33863 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 22dc2bc8-5d1c-39a4-95c8-3f4f90d08c88 | -5.29318 | -44.46547 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 945ed066-0ee0-3fc3-9ab2-8c96c1a31fbd | -6.17739 | -44.86021 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0405a4a2-e25a-3cae-bc1b-b9b531c0bb35 | -9.56322 | -43.02278 | 2025-10-12 00:13:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |
| c9b47244-9f0b-33ab-8027-573c9d84a390 | -10.17898 | -44.54286 | 2025-10-12 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5547a1d4-9c33-3652-b019-7b8ecc67865b | -7.5158 | -44.60598 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d4bb420-911a-394e-b89b-73050d1845cf | -6.59847 | -44.57218 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 78f51a0e-71da-3124-a397-8a1e05229500 | -4.73747 | -43.52179 | 2025-10-12 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77159e91-1154-3eb9-a570-e081f1532a65 | -6.43038 | -43.36642 | 2025-10-12 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 231175dd-06d7-3955-baae-677421d439d9 | -7.05695 | -45.22426 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| ba55c043-8ef6-30c4-8524-5549824e97ac | -5.40175 | -40.97379 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ed771b04-9aad-3de4-a7c8-4331d76f0821 | -10.16887 | -44.53508 | 2025-10-12 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be3eb604-29cf-3e42-a66f-81544932dcc2 | -5.75615 | -46.4909 | 2025-10-12 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0c6a0b50-bc9e-3e82-938a-9557542061be | -8.48407 | -46.16911 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2343eb46-85e2-3454-b3af-2b180ec6c424 | -7.05572 | -45.21531 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6bf94608-620f-33d0-bec2-d7ea93d6bba2 | -4.38139 | -43.74488 | 2025-10-12 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b36e42ca-69da-3c34-8be1-ac1bbe6208c2 | -6.80599 | -47.0531 | 2025-10-12 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5b2094fe-b611-375b-b3d4-6f79f0aaff9a | -7.74867 | -43.16806 | 2025-10-12 00:13:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f44775b9-8712-354b-b63d-08c962abb0df | -7.0646 | -45.21407 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f80726c7-e771-3db2-8523-6b888dfea064 | -6.19645 | -44.26719 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 9f4b3296-5169-3d96-b1f1-f837afe8db10 | -7.43424 | -45.15598 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 241a43b2-857a-35eb-8293-d2bf8a902909 | -5.34313 | -43.43628 | 2025-10-12 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a868967-a818-3222-8180-17ff0676b397 | -9.40479 | -45.76625 | 2025-10-12 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3b326310-72d6-3440-9312-fe5fbabaafdb | -5.3654 | -44.92177 | 2025-10-12 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95a3e4e0-f8f3-3d89-a2f0-cee414512530 | -4.41184 | -43.11342 | 2025-10-12 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4103575e-eec0-3c1c-9366-21abc8a6e009 | -7.34719 | -43.86052 | 2025-10-12 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| edcfc555-1b3f-3cc1-a95f-fc72f8c25d5d | -8.4962 | -46.25908 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 630c39e7-c368-381d-97c2-3d01f54ada0d | -6.58695 | -44.61873 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 5a5f472a-0f64-3441-a776-6e812c542784 | -7.40214 | -46.94655 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a6ea9d9b-eb44-3e05-9df5-8625e8fc52c6 | -5.81397 | -44.03836 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 21af1a50-dfa3-3cea-abc3-87d9a71ce5ed | -4.3836 | -43.29966 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 66f20415-91ff-3aee-87ac-00cc8f6db111 | -4.27006 | -46.93693 | 2025-10-12 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8bab218c-2452-3888-982f-13521c82e04e | -7.36321 | -45.31016 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3d8b796b-947d-3d49-a876-0d4b3bdbe80d | -3.6123 | -42.74863 | 2025-10-12 00:13:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9afb6a2f-d8c2-3bdd-ae32-4e64a8b2873b | -7.80166 | -42.43333 | 2025-10-12 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 05097717-7f24-3a5f-8c36-6ea2857918ab | -4.6294 | -43.47342 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f18961b-7bd6-3934-b258-352a9a5e5b26 | -8.63767 | -46.99929 | 2025-10-12 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa37dc3a-705c-33e7-9298-e54b8c24d1c4 | -8.02063 | -44.45259 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33b45461-6ef8-39ca-8bad-66dc2d72e643 | -9.52623 | -47.86765 | 2025-10-12 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bab2403c-51d2-3161-b32e-0d7191831a72 | -7.70117 | -42.37473 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3c29ce43-65f6-355a-b514-4c54f9769dfc | -8.48277 | -46.15946 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33fd0166-9ef3-32a7-b6b9-d4e38bf6051b | -7.14744 | -42.50298 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bdd65d36-a303-37c8-bd16-a98cdb2c1351 | -6.77024 | -42.83859 | 2025-10-12 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| ba46f1d2-5d9a-3958-b036-ddbb11ccbbe0 | -6.28037 | -44.40229 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f6e7e1c1-36a5-3985-8f20-87f06786702b | -6.65645 | -43.72881 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25d84568-56e1-36dc-b5e9-bcdfb24dfffc | -6.95883 | -42.47286 | 2025-10-12 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c0db1e7c-d0ee-39e7-b5bd-6b9eb89f6ddd | -7.49689 | -42.76084 | 2025-10-12 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 178d896b-529f-34da-8fbd-6215e5a1c9d4 | -6.96253 | -42.43209 | 2025-10-12 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 8c6ed74a-32d1-34f7-99a8-4ce1634c0093 | -7.52038 | -46.53132 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fee1be1e-a1d6-3b8b-88e0-e962cb545f4a | -7.51237 | -46.54263 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d8df1b26-9dfb-36d7-b0b7-3dddd376d036 | -4.91055 | -44.30057 | 2025-10-12 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c493568-baf9-3ccb-bec2-793d5cb80ae6 | -6.75822 | -44.65413 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f80bf9eb-5918-3209-9a56-4bd4bb992bdf | -5.97423 | -44.38293 | 2025-10-12 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a519b354-516e-3aaa-9737-a8f4cb033ded | -7.26451 | -46.13978 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca3ff6a7-0230-3a9d-be93-77bb214e98c1 | -6.69506 | -44.66946 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e7c7db7-34e7-3d01-b572-458a4b5e51d3 | -7.26322 | -46.13017 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61eae5ec-7cd7-36cb-a716-1ce3af3ef1f6 | -7.49825 | -42.77034 | 2025-10-12 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 336d8e37-367a-3386-a95e-0e53892b692d | -5.37065 | -46.2983 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28856c49-f2ea-3f69-8675-cf23c07df1e1 | -7.88186 | -44.45739 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| caf13910-fbe0-3880-8258-4865e7f51d26 | -6.58817 | -44.62754 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b101c70f-86e1-3aa9-baf3-66a3c851949f | -6.26241 | -42.76286 | 2025-10-12 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 29615836-466c-3b34-ae7f-b6d76b5a5efd | -7.29716 | -45.56647 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcea47ec-68d7-355f-b6cc-e64e64c704be | -9.56192 | -43.01368 | 2025-10-12 00:13:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| d9c6aa50-5c56-393e-b254-a29b1a965d64 | -7.204 | -45.49266 | 2025-10-12 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 56d95239-3fc7-325b-91d6-2ed26a4dc7b8 | -4.67309 | -43.25949 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7e6b17c2-b5c1-3c5d-9f4d-83a82608e8a8 | -6.72794 | -42.07728 | 2025-10-12 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6e9cf6fa-603b-3e2e-9bd3-d6afa320ebb4 | -7.86625 | -44.88233 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 448bcfb3-4e00-3c71-b73c-85e28bee9a70 | -7.86398 | -44.52313 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d8fc3805-707e-3345-acb0-b8b0fc017d3c | -6.76754 | -42.81972 | 2025-10-12 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 582c2cd6-7339-349e-85e6-4ce958e783f0 | -4.57996 | -45.69967 | 2025-10-12 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea98ca3d-d2c0-324e-858a-575259a9bac4 | -6.11997 | -42.23465 | 2025-10-12 00:13:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f01d6101-3c3e-3467-a453-d3e23085f981 | -5.59546 | -41.10881 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8e5c4354-5d6c-347f-b9e4-82181cffcffb | -6.07524 | -44.31765 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27b03618-303b-37ff-bb88-007a5865145f | -4.77042 | -40.84578 | 2025-10-12 00:13:00 | TERRA_M-M | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 54113ad4-36cb-393e-9362-ef70e64c395a | -7.54881 | -43.84026 | 2025-10-12 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8299e11-2d4b-33d6-8cb7-e737400207bb | -8.70502 | -47.05754 | 2025-10-12 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f79a9dd1-8fcb-36b8-814e-2f49294a6afd | -8.22095 | -43.37478 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0406fc6b-4a0d-3148-ab6b-e71890209da3 | -10.16244 | -44.5543 | 2025-10-12 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0aa4e3d-07fb-38bd-9d0d-fa8fbabbfb3b | -5.26794 | -44.47804 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b4ad1e9-9b46-32de-89fd-5cf94ee4b3f9 | -7.35307 | -45.30239 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e4c3da74-3d90-39fb-821d-b7240e3e17cb | -5.973 | -44.3741 | 2025-10-12 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)
