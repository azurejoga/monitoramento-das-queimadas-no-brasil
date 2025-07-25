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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3ac39b2-616e-36b1-b26a-2a2fc2061b5e | -2.28293 | -48.56163 | 2025-07-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6d0625a-6c01-3a6a-8744-c0188311aeb4 | -4.64813 | -46.46664 | 2025-07-25 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033ecd51-a565-3b06-a72f-19e4501c38a5 | -7.91617 | -44.09306 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2884e24c-d177-3f8f-84df-ecbda14650da | -8.30337 | -44.9735 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ae25ee3-6a93-37a2-b61c-71fbc1d358e1 | -7.92021 | -44.09887 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f5f60f6-71c2-3c9d-9c5a-9a941fabec14 | -7.85614 | -48.22323 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f021736f-317f-3e95-81f7-f63cda542466 | -7.90739 | -44.08665 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3da38e13-7ddb-3913-9178-b82de0afc418 | -6.40263 | -53.33372 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40354d8c-0a91-301e-addd-7a39f699e54e | -3.11953 | -47.01329 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02401d2b-b2d3-3877-94f6-42e7483be74a | -7.92408 | -44.09755 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 30a88361-518a-3a5b-b062-be11d66c2202 | -2.80361 | -48.61159 | 2025-07-25 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93996f54-b0de-3dbf-ba56-78b2d44dfefd | -7.88982 | -45.53962 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc85f08b-cb46-32cc-805b-e232cd2f2113 | -7.90669 | -44.09177 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c677a5b-9679-39de-8211-a240894d9882 | -7.16554 | -43.48314 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d455e729-9af9-320e-ae26-0469e4c4a4de | -7.2581 | -43.07264 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f9eccfe2-27a1-37d1-8af3-2f0c67e44504 | -7.24928 | -43.06225 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7450d7a1-a642-3046-89bc-72510758e38c | -7.94056 | -44.09132 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61d54f4d-bccc-3877-b2f9-8d33e8c64b70 | -6.6683 | -43.96661 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 400bc947-9868-3bb8-b4ae-942d29b1e6f9 | -6.90042 | -44.21414 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c83ecfee-6d00-341c-be4e-f55813f3f9ab | -8.29438 | -44.9724 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 254adbf6-a414-36e3-a234-aa3ab4a5f7f7 | -2.91317 | -48.24917 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25668abc-294f-3625-9784-a18bb642a1e5 | -8.33633 | -44.95228 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb6fed8-65bd-330d-8357-f97eaa67f802 | -6.18586 | -40.8776 | 2025-07-25 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 867b324f-c7e7-354c-9e50-832169c96727 | -8.33183 | -44.95171 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ddfe925-88b0-312e-8732-79f723ad5eda | -4.10599 | -47.93142 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 876255a5-9ba4-3fd3-81dc-d9b48d989d5e | -6.22267 | -44.52354 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24b41532-e73f-3cac-b246-de6733f332e8 | -7.92232 | -44.08338 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc4bdb39-8b28-3b10-b99e-157ed5473946 | -4.9941 | -56.29889 | 2025-07-25 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3cfacd3-7808-3d94-af3d-1ceadaf2f609 | -7.25894 | -43.06666 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1d85074d-47b4-3f82-b2c6-b27c666cb92e | -7.86401 | -48.22015 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f48b821c-8eaf-339f-bcf2-412bfa10f0f8 | -6.4059 | -53.3301 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d8f616c-bd04-35f0-8711-4514e14112ac | -4.77906 | -45.3398 | 2025-07-25 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fd60447-a706-392f-84fd-bd95ff5f1c29 | -8.0735 | -43.15457 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 408f530f-7023-3023-9ecb-4b9c6ef1559e | -5.77506 | -51.87254 | 2025-07-25 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a545af4d-f394-38bc-bad5-73903b01df85 | -3.17626 | -49.45742 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d5332e0-4f4c-3abb-bf41-7e95d2db0ca3 | -7.91283 | -44.0821 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35e94c8b-9676-375b-9edf-fb6a1a30760e | -6.64769 | -43.05286 | 2025-07-25 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db39575a-e9a1-336a-bc8f-6f6e76fb86de | -6.89352 | -42.83562 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8796021e-925b-3f7c-9ef5-28401f49b782 | -7.85931 | -48.22059 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bc43037-d8ba-3f7c-9224-8c284db93aed | -7.85251 | -48.22266 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f966b8e6-5a25-3a75-abe3-b2af65178be0 | -3.05122 | -47.38266 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 058e74b0-22cf-35cd-829c-0d9f7728d053 | -6.11954 | -41.83062 | 2025-07-25 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dcc8b04d-cfe8-3b87-b76b-8da0f6b8232c | -7.88614 | -45.53488 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de6dccb0-4c50-307f-9e24-854b72b0068c | -7.85207 | -48.21947 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca3c5565-df3f-3279-9734-f0c7e77a643b | -7.92565 | -44.09435 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cc7ce4aa-cc0e-389b-9bce-fd352942343a | -7.1663 | -43.47767 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96886fa0-4b3a-36ab-af88-d601517f35cc | -3.03509 | -49.42451 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92ee48f4-9fc6-3d8c-8240-291c669f414c | -7.11396 | -47.83737 | 2025-07-25 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b2b3327-05a1-37b0-b56c-b7af2bc51584 | -3.17681 | -49.45393 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71b4049-8f46-381c-bc18-f230b10cf4e6 | -3.39743 | -46.90477 | 2025-07-25 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73508931-faef-30c1-bf92-a99bc79cc78d | -3.17403 | -49.44992 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32633047-0d09-3da8-8402-89d111463606 | -8.08907 | -43.1539 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5644ac30-94f9-3657-89d0-efc14d1f21ad | -3.74299 | -49.04327 | 2025-07-25 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2be18c1-a601-383b-b2cc-7bed1d40e4b2 | -7.86038 | -48.21957 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 660560cd-f813-38b9-b415-b0bb859a2747 | -7.10279 | -43.55531 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1563ee24-9d83-3bfb-8fbd-5dd049ace9c3 | -4.57765 | -48.01608 | 2025-07-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 937c73af-80a2-3e28-8bbd-b8eae8c26c3c | -3.32305 | -48.72029 | 2025-07-25 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94537e34-39e5-330d-9abc-73896959c4eb | -6.58035 | -45.60785 | 2025-07-25 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c3a37e-8b8f-3dfe-86c6-8bdd37093d0d | -8.21043 | -44.93515 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c35c5061-acb0-3b4b-a1e5-4bd6a2bb0638 | -7.99173 | -43.82621 | 2025-07-25 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9d2d0e31-67d2-3e97-b17b-b7323d00e8ce | -4.77961 | -45.33611 | 2025-07-25 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9fae3a1b-5efe-3ecf-aa7b-5e9806d42b02 | -2.90628 | -48.2481 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ab7aadf7-b189-3a1a-95ae-1146a82c98bb | -6.98779 | -43.32585 | 2025-07-25 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1929aac0-9410-3b05-a621-f1268dd8c0ff | -8.29055 | -44.99932 | 2025-07-25 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6bae96ce-60f4-3e10-8fc2-e40e51f8edb5 | -7.24845 | -43.06823 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 95973740-08d1-3dc8-ba9a-12603d369aca | -6.40668 | -53.33049 | 2025-07-25 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fb97dad-bc51-3843-bdea-4469e320d306 | -4.66723 | -48.86604 | 2025-07-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06657e18-aaa1-3876-8307-e72c173ee7df | -3.10856 | -47.01162 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f12155f-3831-3e5e-a72e-16da02b9b0e7 | -7.8935 | -45.5444 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a9579a-448a-3c55-9979-83a6d97655b2 | -4.0345 | -48.06643 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb7dbf33-fc80-3ae2-aaf6-7c7c8533020e | -7.08678 | -44.87799 | 2025-07-25 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 901877df-cd89-3a2b-af9a-a7217f3a324b | -7.91461 | -44.09624 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd93f17b-33b4-39b0-af72-32049f9969e5 | -2.90972 | -48.24863 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5d9f9d6e-5ebf-344c-b718-c341df33384e | -8.06845 | -43.15376 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6d706ff4-1068-3fdc-82e6-565517dd215d | -6.63133 | -56.29179 | 2025-07-25 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7da7d303-a428-331a-98b2-8b713f72f3d0 | -7.91535 | -44.09113 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 166334cc-641a-3571-9c96-c799f33095cf | -7.98373 | -49.93899 | 2025-07-25 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5793b8b-d6e0-30ba-9565-b798e155a694 | -7.88495 | -45.54311 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f49166bb-45fd-3e10-a73d-2597469929ca | -6.34124 | -43.75025 | 2025-07-25 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49bd9924-dcbe-3f4b-9ca0-79e0a8e29204 | -6.6737 | -43.96226 | 2025-07-25 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 629c27fd-5ab7-3de0-ba20-34a1f7e6f820 | -4.31502 | -47.98301 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1b33c68-cd2d-345f-b684-9d885f43117a | -3.04047 | -47.38107 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ff8781-7f0c-3ceb-8bc3-cab73823c45d | -9.04918 | -46.62278 | 2025-07-25 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5577f29c-cdd9-3d86-9a91-5800101c9af1 | -8.89261 | -45.57134 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 4555f3ce-4f83-37cc-8662-9dd1aa3646a0 | -8.06689 | -49.71911 | 2025-07-25 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13501101-e6fb-3a04-bc6f-27b78bf90d0b | -8.36773 | -51.07492 | 2025-07-25 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7158e378-eb03-37af-992c-02b627ca6deb | -8.89162 | -45.59723 | 2025-07-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fc7c841-b0f1-3868-bad1-dac6860e47e4 | -10.50111 | -44.88019 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7bba1ee-df6f-35a8-965d-e7c9681852a6 | -13.40175 | -46.80667 | 2025-07-25 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 594ee08b-d4d8-318f-ad18-6cca802dc14d | -11.4626 | -45.11635 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 176c18ee-4df5-34ac-8afe-4fec3c9a1b17 | -14.17108 | -45.35361 | 2025-07-25 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2532133-a78f-30d5-9a06-fa1f6e2e1077 | -9.4311 | -44.73472 | 2025-07-25 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f444a26-4d39-32b7-93ea-5c239e8152c1 | -10.03861 | -59.0991 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d19cd6-62a5-37e0-bc62-f0f134b7af7c | -10.05154 | -59.1064 | 2025-07-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3a8542a-e119-3ff8-8e6d-19e66046a24e | -14.94201 | -46.97684 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd04ee40-6cc3-3f13-946d-31a7167cdd82 | -12.43168 | -45.38056 | 2025-07-25 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44645ccb-046e-36d5-98b9-5ac437e1b69d | -14.9534 | -46.97546 | 2025-07-25 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceb0d55d-204d-397a-8dba-d025363867b7 | -10.63648 | -44.76228 | 2025-07-25 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 812b7b86-ad30-3630-99f5-bb729c642c94 | -13.70689 | -45.6851 | 2025-07-25 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcddd0a2-8499-31c0-a66b-b24a4941762e | -11.44737 | -45.12436 | 2025-07-25 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README23.md)
