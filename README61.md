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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 495e3766-bd2a-35e8-81b8-17af00426cb8 | -2.81415 | -54.12149 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8d30688-d06d-3ed6-8c72-4bfa4c8e1088 | 1.13355 | -59.52485 | 2026-10-04 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cca904e4-05e2-3a4f-a09f-5c4fc36b4568 | -2.89982 | -54.12912 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a24b57a2-1012-3e7a-bb72-2b4d2e20d9ac | -2.2171 | -53.70475 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c27e88d4-85e5-3ea6-9b38-f67d394ca955 | -4.26249 | -46.36282 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0933e919-2696-388e-992e-29cd795c90f4 | -2.88356 | -54.09438 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9be96a42-3891-3865-8d49-c29063192407 | 1.76235 | -55.63215 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4e1bc58-8dd8-3493-91dc-7e30459e93d2 | -6.07815 | -53.47578 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56193c47-c9a7-3611-ac8e-62c0dce8f1d2 | -2.92586 | -54.10089 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70d3790d-a44f-32a3-a818-f11e10afe237 | -4.8204 | -49.28618 | 2026-10-04 05:16:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19930fd6-8900-381a-b266-b94a078f93b0 | -3.77259 | -51.40333 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7eddf66e-cc0f-3263-832b-dab3bd6a10c9 | -3.27656 | -53.82354 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 303f060d-be8a-37f7-ac4f-6cde02543abc | -4.42992 | -55.74806 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c667af-4327-3ca8-b115-a5a43ceb4bbf | -2.81063 | -54.12095 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a82f5940-e93b-3465-8cc5-ab88d7ba2bf9 | -2.13385 | -56.69302 | 2026-10-04 05:16:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61722c22-362c-3fe0-9623-74fa80cf4d3f | -4.25819 | -46.36785 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1bb49b1c-77bc-3e09-bc87-b8381ca96763 | -1.74507 | -55.23908 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a815aa14-1599-33d8-a6dd-ee1ab79c7f23 | -3.12837 | -53.73583 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 131c5ab5-2979-3d2d-8e59-a5be06ea20ad | -2.81371 | -54.10131 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d15f7beb-99f8-31fa-b3ce-3deeeeebe531 | -3.53735 | -55.52305 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4427dca-110f-3259-a94f-cf4262ca89f0 | -2.80589 | -54.12825 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0729aae7-6e05-32a7-852e-38e212e1c550 | -3.2949 | -49.13013 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ff6b712-6542-345f-a20d-d6ef46c4c255 | -3.70099 | -50.66118 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2518c5a1-d782-3700-8fe7-68763af8ab86 | -2.90624 | -54.13413 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7a8f88a-3eda-3f1f-ae89-6affe77a93c6 | -3.0752 | -49.54321 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| abba4bd0-0116-3a0a-9dd9-44db80b96ab5 | -2.53884 | -58.03761 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6badcfa-7ca0-3b5b-8a41-5f8c1a64602b | -6.20853 | -52.80474 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3af645-a53f-31d6-86e1-7c238511b650 | -3.05283 | -54.16822 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4197bdd9-3243-33ea-b202-6581bb466cc1 | -3.1922 | -57.92248 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 627d8701-b84b-3642-a425-ca401c0ffab0 | -4.92787 | -45.69215 | 2026-10-04 05:16:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5151b1e9-77da-392d-a1ed-0d9d6876e4b2 | -5.99552 | -53.64045 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac897bb1-8827-3381-b42c-f220598808e0 | -4.4586 | -50.97793 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4c3cd24-2b60-3911-811b-38a5f086be77 | -3.14096 | -53.73646 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2dd7596-1e34-30aa-b69d-7360a06c45f2 | -3.11205 | -53.74596 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| ffc267b0-f84c-3569-9ba8-e50cff2304ef | -3.12153 | -53.75582 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 719092c8-c85d-38d0-8a70-ecd6ce75b0c1 | -4.29231 | -50.26477 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e684f92d-18d2-390a-83f6-e86e1d6da2d6 | -2.80851 | -54.08844 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83311b91-02a4-3969-a52e-2ce285dc2574 | -3.04583 | -54.23532 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f9f7d17-deff-3d0e-92d9-0cc90e528644 | -2.89644 | -54.10443 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26d60f04-59a3-3db7-b5c4-3b79a1f442c3 | -3.30393 | -53.83631 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4bae3e4-71c2-3341-be29-85849c30a074 | -3.78914 | -59.38313 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 628596f3-a58f-33c5-a003-9589c30c1e17 | -4.1552 | -47.53576 | 2026-10-04 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28efc5ef-a6b0-31c7-a631-80c4b4dca16e | -6.20894 | -52.79695 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 546afbcc-c60f-38e8-959c-00f8acc1be38 | -2.81354 | -54.12541 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96166f11-b6ed-3ae7-b2f0-9b7d2637586d | -3.46789 | -50.10387 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0d8c8ee8-aa7e-3567-8a87-bdc267c80b34 | -2.14847 | -57.19999 | 2026-10-04 05:16:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 340cd3f2-a77e-3f17-b645-d725b770aee0 | -4.45922 | -50.97376 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54b14809-b279-341f-8826-2bf01269d793 | -2.94682 | -54.12826 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b867142a-e949-3b5b-ad3a-82f0dd91406b | -2.89583 | -54.10838 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7444da2-9df9-3950-97be-6871a0b0a8b2 | -2.57668 | -51.87914 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 596adb0b-51a5-34fa-a288-cd662abfc081 | -3.8078 | -50.8511 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 784baef9-13e0-36b0-8291-6825cb4d18f4 | -3.00482 | -53.87614 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2936843-6cb0-3c78-8e0c-b23485667623 | -2.88077 | -54.06564 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa0beeb3-7f82-3a59-bd7b-20917eed72f6 | -1.27904 | -55.41588 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5ade55a-b860-33ac-8d62-2314f5740c59 | -3.11464 | -53.7295 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c7bfce9c-245a-3697-8c43-97d898c75d74 | -2.7961 | -54.0986 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecbeb0c7-0a18-3e68-87af-3057fffef856 | -4.45431 | -47.92691 | 2026-10-04 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79627c05-62b5-3969-b5f7-ba948296a3c1 | -2.83288 | -54.20816 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dac5cdfc-6aa4-3376-95ae-0cdcc6b553a9 | -2.96817 | -54.10737 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b2aa30c-2d80-3c9d-a7ec-7fafc15f580c | -3.07351 | -51.27748 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90a23ed5-aad8-30be-ad56-416631ee4529 | -2.81018 | -54.10077 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9e85b90-e354-3030-b9a8-514e354c42f8 | -2.44551 | -56.37614 | 2026-10-04 05:16:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 587e443b-1819-3b48-99d0-54d5594bf80e | -2.96174 | -54.10237 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a57368f-ec36-3ff4-815c-6d8c97ec20dc | -2.1523 | -53.6582 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a703adfd-c5cb-3c30-8be2-674d97d51d4e | -2.81661 | -54.10579 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12387376-ce92-34b5-bec6-7392f8bd8974 | -3.10664 | -50.28497 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e15782cb-4e70-3771-ad83-115eba2044e2 | -1.87466 | -50.61816 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f208f549-d5df-3776-bf7c-7730b480752e | -3.47244 | -50.10454 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4aaa0db-98dd-387b-b76f-b4cef73e6e76 | -3.96299 | -55.7782 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 532a11b3-0783-393e-9b7a-d7f8ac0e8b80 | -2.96942 | -54.09951 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe5247d4-a177-3061-99dc-341ec16d0964 | -4.26837 | -50.74559 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53986084-de74-3b69-ba62-d601d0940750 | -3.05986 | -54.16932 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3c2812f9-aef0-3855-979b-59d93192a5d2 | -4.20398 | -53.46001 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bebf5236-485f-3606-9677-f912e60c885f | -4.81781 | -54.72913 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f362dd4c-89d3-3402-960c-2cfbd12cf0cd | -3.04313 | -54.20689 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdee291a-4274-392e-a2d7-40a7385128ab | -1.20888 | -55.86026 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 755ecba5-79f2-33e4-888b-7f0b5dac9c6b | -3.13261 | -53.73226 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98479816-f312-3e73-bb20-6f65ad10332b | -3.00125 | -53.8756 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ecd19e2-93cf-36a1-badc-204b29902ca5 | -4.54267 | -55.9766 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 277d88ec-c721-3827-8682-518c413cc22a | -5.55164 | -45.27039 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bd9a23a-d9b2-348b-a033-e7f36c65cd55 | -1.6277 | -55.02063 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67b1ce8e-30d8-321b-9b50-8119aeb572c2 | -6.06304 | -53.47337 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82f39675-6b37-3517-997c-dfa55f1abaa3 | -2.58621 | -51.8701 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7f4e022-ff67-312a-a855-ae01b326ca12 | -2.24428 | -51.93034 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b7615cc-7f53-3e4c-9fd0-ca9dc3757b25 | -2.75157 | -51.55082 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1066923d-f070-3390-8da7-cfb4fbc93dbf | -2.97051 | -54.21144 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d9de103-8fc0-3980-8beb-a3b6f4b85680 | -3.13142 | -53.72658 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5cf4c74e-79b2-35bc-969d-28309f1c8fcd | -3.115 | -53.75061 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b1f3d26-a280-3f94-bcbd-e62ed85d9c9a | -2.81829 | -54.1181 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36e7f09a-1fd4-3721-b19d-f90b57834e0b | -2.36382 | -50.60819 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3589ecc8-cebe-33ea-89b5-423ead565185 | -3.46718 | -50.10851 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c0b53d56-14f6-3bfd-a37a-fedfa687e7a6 | -3.11334 | -53.73774 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d1bcb878-78b8-35fd-a213-bcdf13aef8e0 | -4.25758 | -46.37191 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 213b9ca3-77d3-306d-89cb-7751fdb1157c | -2.94045 | -54.19149 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7feddd01-810a-3e40-94a4-ca58735fb085 | -3.0705 | -49.5425 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| acd68816-19da-35ff-bd23-5a12e3362861 | -3.52504 | -54.61692 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e56e041-ca3e-3635-8fb3-c44e85962d32 | -6.20499 | -52.79636 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5dfcdb1-e05e-39d4-9785-373700e3a241 | -4.51084 | -45.89419 | 2026-10-04 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e87c20-05b5-31e8-8d40-1e2539968ac8 | -3.13799 | -53.7318 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09c6f0fe-305e-3da1-a11b-7d52580ac55b | -4.05078 | -51.08179 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
