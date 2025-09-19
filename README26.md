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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4a90ba1-6c22-383b-96cd-cc73605915cc | -5.96492 | -53.5831 | 2025-09-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb07de05-1542-31da-8b47-536a66eafb2b | -8.03995 | -45.71856 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7404fee9-5f3c-3303-9c76-bef2e2d13957 | -6.10932 | -48.02414 | 2025-09-19 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25146a24-ab84-3344-a3c3-daed43371399 | -8.02396 | -45.74034 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bf9cc6c-9df4-37b7-ab39-7c8170beb4b8 | -6.25573 | -43.45071 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 27e00993-7762-3fcb-bee5-f107636da79a | -7.57365 | -45.47355 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 74a93a91-1e6e-3e52-a804-c140545c8722 | -10.92143 | -45.64809 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33de4a6b-d489-3243-87be-cc7a0e2bc9af | -12.09176 | -44.84922 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75d1f729-07c4-33d2-bf54-9b532dc1cc9f | -5.54952 | -51.36755 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77134a23-8d5a-394b-95cb-2067a6ea88b2 | -11.18576 | -45.36884 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a40abd6e-9d0e-3d31-b63d-a4af5499fef5 | -8.47366 | -44.71751 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdfc5a28-3dec-3917-98ed-597fddaac08f | -7.70444 | -44.3904 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e16148b-209f-3269-8b47-f4ae4bb4108d | -10.92082 | -45.65251 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c479773-15a8-373f-ac27-cd93a618caa6 | -3.94444 | -55.84917 | 2025-09-19 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d6c827-a823-3769-aee8-c683b7a00d45 | -9.17133 | -44.65061 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 903191c1-6d5c-3e52-b1b7-74ec265ba81f | -7.55803 | -45.4913 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12118559-c563-31a7-9b70-bf5ff537e0b5 | -8.04698 | -44.07564 | 2025-09-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 893b98e0-8047-3a16-9da3-c9679b67d17f | -7.71298 | -44.39662 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50fc9f3c-218c-33bd-9320-b5bc435883ba | -8.7437 | -46.1515 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4772225b-575d-3ef2-8f8d-fe2cad4be395 | -8.95426 | -44.99934 | 2025-09-19 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c07873f-90a8-3ba0-a7d3-d2d223ff0c0b | -6.95272 | -42.43973 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d68f9ee-595a-3be3-947b-b17bc5cd0112 | -7.31141 | -44.05118 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05f7cfed-3da1-33cd-a908-e7c795a44ae4 | -5.13204 | -47.82841 | 2025-09-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b41710c4-69b9-3f5d-aff2-485e76a6957e | -10.28961 | -50.24115 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5852da2-48f7-327a-82e5-fc3d792c3d85 | -6.26695 | -43.92076 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d1e4e972-0a2b-3cc4-a09c-0301d3ba84ce | -7.04975 | -42.00655 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0f59088-75b7-39e6-85d8-fc12afb5a00f | -8.05971 | -44.08848 | 2025-09-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67b723c0-5d43-339b-bfca-609ca548a328 | -8.14206 | -43.63102 | 2025-09-19 04:46:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 520c5a65-336f-3d8b-8b15-4962b9900e2f | -6.62112 | -45.63838 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b04527a-c069-3a55-b335-29883104e235 | -5.80692 | -43.64028 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c4c07af-9860-3f5b-9322-1ecf43c57123 | -8.02625 | -44.94489 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 428165ff-eb7d-3243-9cb0-e73f30465abd | -5.9867 | -45.85776 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3449bf6a-d8b7-3324-a8e7-4a1398d2b24a | -12.09556 | -44.81853 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ac9485c-8a64-3dc3-b2fa-dc8c5d93e3ce | -7.58276 | -45.47084 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e071e52-cc55-3bc0-a5ee-3d93f486b9c9 | -7.30738 | -45.16489 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c09bfeee-97a4-3195-8000-e596393db93d | -9.02921 | -44.97131 | 2025-09-19 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5393b4a5-a15c-3060-805d-0803b553b4f0 | -6.42226 | -43.55191 | 2025-09-19 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ecbb5c9-cbad-3d1d-9c7f-02b98bf230c7 | -10.34385 | -47.86603 | 2025-09-19 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8df31848-cc78-3f29-8195-260deb241636 | -4.25864 | -54.84364 | 2025-09-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53a887c-60eb-3fa6-ab4f-afdbcebf65a7 | -11.21133 | -49.63322 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4843997f-da96-339f-8ab9-3c9e90e6feb3 | -7.26136 | -46.3448 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27a0789f-c10b-3650-bdd2-80361c94b09b | -8.63275 | -45.71273 | 2025-09-19 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 238ddaac-dcb6-3a54-bf0c-37c1c1e8b524 | -10.92205 | -45.64363 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3adec2b-fd8d-3dfd-aeb9-752fe28155ef | -7.81468 | -46.10957 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 553890ee-f2f1-36ca-b066-fb9f3ee1a86c | -5.82229 | -45.90308 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f05da85b-6c0e-360d-8c67-760f6944cda6 | -5.96247 | -47.09221 | 2025-09-19 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6328adc3-172a-3522-a5b0-a1b0b6bb81da | -8.47411 | -44.71917 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c09b60-4950-37e9-97a6-f923f4068c0e | -5.70756 | -49.0965 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2ebacc3-5c29-30e7-b6c6-6c375b9be13e | -8.04418 | -45.71918 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01898317-6dcd-3a6a-813b-2a6fdff5f48f | -10.91981 | -45.65429 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c85ab09-b291-3b0f-b23d-52ccd1455c1c | -4.94416 | -49.92546 | 2025-09-19 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 032bbcab-59c6-3145-942b-949509c3f927 | -7.58106 | -45.48264 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 483f7989-f80a-3b51-9171-e0e866424cbc | -5.98616 | -45.8614 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d12bcff8-1b70-3574-b6d1-cff7cb657fe3 | -7.27427 | -49.28801 | 2025-09-19 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb540efb-15c6-32b3-857a-871e0da899ac | -6.9601 | -44.76067 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46f3edbc-9e4a-3f4b-ad18-8c138844c762 | -7.56512 | -45.47225 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8563878e-3a45-32d7-807f-ebf12b9ac218 | -5.79969 | -45.36487 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c2305a1-7f7f-3d86-b0a8-26d3fb5279a8 | -6.42384 | -44.36457 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168c33e2-6fb9-3a35-8597-c76c2dbe27b4 | -8.01498 | -45.74295 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff5a4413-9318-30ce-8312-4627d0539f76 | -8.21791 | -45.80571 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24c95674-6d22-3f0e-ba56-d4bcda6e7c7c | -7.26186 | -46.34125 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 954e2565-520c-3b3e-92de-8f22fa3a78f7 | -9.16474 | -44.62952 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 699e8fed-a9ff-3c92-b397-3e5b4c9e1e3e | -5.87134 | -45.90686 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 523560e9-b020-31bb-993c-21065c6868ae | -9.03102 | -44.89085 | 2025-09-19 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ea5c5d-e8d2-31ef-896e-13555d146dc3 | -8.9022 | -46.12551 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97e98b4e-5ca5-3069-9406-0847c44fbf7c | -5.82804 | -46.28252 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb86acce-7187-399e-b836-2cdcf3da8360 | -6.32165 | -43.99453 | 2025-09-19 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eddb6be5-9a70-37a4-8972-97ac5f89fae9 | -11.21834 | -49.63429 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fadb757-88dd-3708-bd94-14e947e8ab6a | -10.91822 | -45.63858 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a658fb4-8e7e-3584-ac49-4b88286eb956 | -6.5843 | -45.58744 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a3c2f55-0c39-3faa-afa1-8199628cd113 | -5.79104 | -43.9029 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30eee0ca-e98b-3778-a462-70f733644477 | -3.94505 | -55.8455 | 2025-09-19 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5540d55-587f-3c11-913d-559c0acfec62 | -7.33314 | -44.56892 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b964673a-15c4-372d-b7bf-07d3ee36839a | -11.21894 | -49.63032 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a87935fc-dc2a-38ec-8681-ca16a2b83374 | -8.15431 | -46.77787 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97d660e3-f61c-3576-ac30-91bd5bd0ebbe | -7.71795 | -61.51671 | 2025-09-19 04:46:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be38cf04-5835-30aa-8073-2cd1fcf1037a | -7.56569 | -45.46827 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf31f6d1-da15-3b9a-afe4-256a8ae617a3 | -5.79604 | -45.36044 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a4d0e16-8e62-3d3d-88ce-1e5c8462f5d0 | -8.23742 | -45.88117 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9207096d-985f-339b-934c-f3548aa4d71a | -6.0109 | -44.33139 | 2025-09-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c566048e-fad6-3c44-9f10-140289afcd47 | -12.15237 | -44.94337 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| caf557e0-496f-373c-880b-17bcfd35ac6e | -5.92001 | -46.47248 | 2025-09-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c9d7896-b237-306b-a2d6-cff88331bf16 | -10.34766 | -47.8666 | 2025-09-19 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92212fc3-407a-348f-b842-3fd4a1e97cd4 | -5.97345 | -45.86315 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7123f223-f02e-32b1-afbb-724816cb6a88 | -8.32294 | -47.55255 | 2025-09-19 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af8a4f89-98e2-36e5-94bb-89c2d0cdf163 | -7.28506 | -43.928 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36ab678b-e50a-36b2-a414-d14d0dc52390 | -10.29579 | -50.22311 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1bdc6714-4788-38d7-b922-4eb8ba2dad1c | -6.82239 | -47.01722 | 2025-09-19 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d278c3cb-4a69-30d7-9683-8255480c3072 | -6.38334 | -43.33479 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 847ec6af-bacc-3cf4-a842-a014ea04e393 | -5.82178 | -45.90665 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28df5420-03ec-39c5-aea3-74af4a20b96b | -7.99665 | -43.94078 | 2025-09-19 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4d531d9-def1-3dc1-a1f3-c37adc9a4127 | -7.87563 | -45.62841 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c0ee48e-4f40-343c-9fe8-f9c3d0f605b1 | -7.57309 | -45.47747 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1e99911c-8921-304c-a683-70b6772ce6fe | -4.47814 | -54.85555 | 2025-09-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c25a4f6-3df1-3337-8c55-432ad3906d7a | -8.88914 | -46.12767 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa2d74a7-bb38-31ce-94f8-713be61ead66 | -5.80388 | -45.36547 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 009602ba-49b8-3d70-b39b-5b47be6b9c18 | -7.65361 | -45.13391 | 2025-09-19 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9f51c05-f5aa-3593-a3a8-26b923118d14 | -6.25287 | -46.11825 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9eeef4f2-313d-35a6-8fd9-7779059d6982 | -12.09198 | -44.84312 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f22f286f-abe2-32fe-bc53-983a06718dc4 | -5.79914 | -45.36865 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
