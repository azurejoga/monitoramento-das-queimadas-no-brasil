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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 971bc02c-d36a-3fdd-a6d9-66a56d34e045 | -15.26731 | -60.20401 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9da3045-1ebc-32d3-96c4-79df61cdff6f | -15.25841 | -60.21452 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e748cb7-5413-3b65-9ac8-75ef053bb76f | -15.25558 | -60.21002 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebab83e3-972d-3c0d-80fb-7f5bd78e22b8 | -14.70721 | -56.81192 | 2025-01-01 05:08:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ae8fe5-b723-3193-99f1-ac48f01597ee | -15.26253 | -60.2112 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 082037fb-50ab-3664-b35d-2694374f7ffd | -15.27078 | -60.2046 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8bf2551-fcea-36a2-96ad-57177a1ea960 | -15.26188 | -60.21512 | 2025-01-01 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e69adfec-71b6-35f6-95fc-e7c9cb5b1ef4 | -19.55424 | -54.67788 | 2025-01-01 05:08:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb46d72f-a142-37be-a331-93b8e4c03f16 | -19.83533 | -57.4615 | 2025-01-01 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 86dbc3bf-26b9-3100-a33c-5301740bb2de | -16.31709 | -58.19875 | 2025-01-01 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 86469733-81ca-39d2-bba6-02cadc8f28ad | -19.71795 | -55.36234 | 2025-01-01 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9c28656-ca56-3d58-84c5-aaed3df73e65 | -20.47698 | -53.6754 | 2025-01-01 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bf7ca8f-46e2-319b-840c-e4f66762ad38 | -24.03756 | -50.40252 | 2025-01-01 05:10:00 | NPP-375D | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e232a580-0bf1-39bf-b2f4-1948f6adf1b9 | 4.07884 | -61.14293 | 2025-01-01 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7b4dc1-ce13-31e4-8614-99c47dd4b810 | 4.07603 | -61.14708 | 2025-01-01 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efe55a9e-725e-305a-bdfb-ac4c6e4b1636 | 4.07547 | -61.14349 | 2025-01-01 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ae0529-cfe9-39d1-989f-f783983f8439 | 3.57238 | -60.9158 | 2025-01-01 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40ab7551-a8a4-3f60-b11c-8e3965369c7b | 3.57572 | -60.91529 | 2025-01-01 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9518f2f-0f36-3b20-a496-19321c116e38 | -15.25827 | -60.21409 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd780705-9117-3e52-b6f5-c9df8bc9dc7c | -15.43855 | -59.06298 | 2025-01-01 05:29:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c60491c9-a7ef-3a18-8108-5306d30f4004 | -15.25893 | -60.2094 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4e55c81-49f7-363c-9e72-8d7d50179de3 | -15.57279 | -59.41967 | 2025-01-01 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11fbdefd-9e5b-3513-997e-5b6850727de4 | -15.27084 | -60.20648 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 357e255c-05c0-3fbb-996d-8d1d3a9fde37 | -15.26202 | -60.21468 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a62a5bc1-46dc-31d4-a9a7-156fc9c72257 | -15.52014 | -59.42238 | 2025-01-01 05:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef10c111-b76c-35aa-9e61-3d30bbdd4a6b | -15.27017 | -60.21117 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54469666-200e-308b-80d4-ea4a5b2b2808 | -15.26334 | -60.20528 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7929ac0-9f53-3f56-9cbe-191cf7a63814 | -15.26643 | -60.21058 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5b61027-113c-36db-ac78-bb172bdbddbb | -15.26709 | -60.20588 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53646a72-d39e-3b2f-8bc5-ed82ddfb3958 | -15.26268 | -60.21 | 2025-01-01 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7db1386e-a508-37db-8ee5-bc6c250db49a | -14.70599 | -56.81441 | 2025-01-01 05:31:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09eee02b-70a1-3559-86b0-d03db4522045 | -19.72062 | -55.36472 | 2025-01-01 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3dbdb01c-835a-3028-ac5c-1c8813a80b22 | -19.76632 | -55.40302 | 2025-01-01 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2f339a2d-da65-38d7-b090-fa1c1c887016 | -19.76559 | -55.41011 | 2025-01-01 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| abae33c6-451d-3c1b-99a0-5fcc24af83d8 | -19.77139 | -55.40722 | 2025-01-01 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0725537f-2300-395b-bd13-5e2acf93f891 | -19.76596 | -55.40653 | 2025-01-01 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cfe8dfc7-d9d7-37d0-80e8-395e09071b16 | -15.25743 | -60.20508 | 2025-01-01 06:16:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 07a2a835-8cf0-36f5-a789-c827e4412765 | -15.26626 | -60.20646 | 2025-01-01 06:16:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b274905a-33d2-3703-9239-213d8ce54b55 | -15.26762 | -60.19738 | 2025-01-01 06:16:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d5f6e1c-ffb2-344e-810f-26549f45bf26 | -15.25606 | -60.21417 | 2025-01-01 06:16:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c7925eb-dddc-3a7c-90bb-fe6c07b24c98 | -3.30035 | -42.14489 | 2025-01-01 12:12:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| db3a564d-eadc-3407-a79e-617644271b09 | -4.29643 | -40.94071 | 2025-01-01 12:12:00 | TERRA_M-T | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ed1a10c4-a77e-3c2d-a999-39e0756c2c81 | -3.02519 | -39.6483 | 2025-01-01 12:12:00 | TERRA_M-T | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ce90e6ee-ac78-3861-ae6c-c00b339b097e | -5.05957 | -37.98685 | 2025-01-01 12:12:00 | TERRA_M-T | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| eb2c9721-27c5-3c74-82e4-88dffda3746f | -3.02392 | -39.65712 | 2025-01-01 12:12:00 | TERRA_M-T | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 19d971ad-081e-37ed-a39c-d0eab54f5ac1 | -3.77545 | -42.29012 | 2025-01-01 12:12:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2811a6c9-2068-3a32-8848-c8133492dcb0 | -3.57697 | -41.13328 | 2025-01-01 12:12:00 | TERRA_M-T | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 7cba7818-446b-3df8-a083-3cce3fbe0fde | -10.73595 | -40.47337 | 2025-01-01 12:14:00 | TERRA_M-T | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 1ad87f57-2db3-3c86-935d-774d7c3564e6 | -8.81682 | -37.40707 | 2025-01-01 12:14:00 | TERRA_M-T | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| be3364a7-119a-3a1f-9fa4-1537d753742c | -11.56175 | -42.42696 | 2025-01-01 12:14:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8860dba7-f426-34ee-8f7a-e8ebb2a3d4d0 | -10.61354 | -44.3259 | 2025-01-01 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c1ef41ac-eb8e-3c55-b525-b164814bf5bb | -7.04552 | -41.57946 | 2025-01-01 12:14:00 | TERRA_M-T | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5875e408-d513-395d-9225-44ce9323f6f7 | -7.70871 | -37.7532 | 2025-01-01 12:14:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f8b30826-0e5a-33d1-9c4e-572c64c68e2f | -11.16062 | -40.40154 | 2025-01-01 12:14:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d91f4732-2824-317a-b4d4-7b1f3169311b | -5.64065 | -37.92164 | 2025-01-01 12:14:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3a45ef1c-9dd5-3cbf-80d7-c4841b4d69ea | -6.16175 | -37.7878 | 2025-01-01 12:14:00 | TERRA_M-T | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 09a9c74b-79bb-3e15-8997-f775ca5345de | -7.70713 | -37.76469 | 2025-01-01 12:14:00 | TERRA_M-T | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 68e3d96a-8358-300e-942e-33313d31475b | -4.89428 | -40.1211 | 2025-01-01 12:14:00 | TERRA_M-T | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 70c8c2f4-1de3-3cac-94da-cd29695d8ea0 | -6.13548 | -43.29925 | 2025-01-01 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1d9ec81d-405d-3683-b2c6-b9574dab86a6 | -11.56043 | -42.43599 | 2025-01-01 12:14:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| f245d494-247f-3997-b071-8ef2261420c3 | -11.24416 | -39.54026 | 2025-01-01 12:14:00 | TERRA_M-T | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |


