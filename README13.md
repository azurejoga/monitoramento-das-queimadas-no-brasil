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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da57cab1-7ff7-37fb-a61b-9a8351cffea0 | -5.5338 | -35.614399 | 2024-10-02 00:31:58 | METOP-B | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| b02c2564-4cab-32c2-b593-11ad114cbbec | -5.5161 | -35.584499 | 2024-10-02 00:31:58 | METOP-B | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 1259d074-6bb5-3162-bbf7-6cf76dc97dee | -7.6992 | -44.9105 | 2024-10-02 00:31:59 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4dc5b5-0887-3c57-be1a-9f4ac675a560 | -7.8091 | -45.4785 | 2024-10-02 00:32:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c00c43ba-01ff-3ec0-b421-b7a237a8628d | -7.7976 | -45.473499 | 2024-10-02 00:32:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70df4a5e-1d03-3bd9-8652-5fc497752463 | -7.7023 | -45.417801 | 2024-10-02 00:32:01 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa85859-cbe3-3956-922c-57285d116827 | -7.7057 | -45.432598 | 2024-10-02 00:32:01 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 954c4d7a-2e96-385f-88bd-96df9444f647 | -6.9508 | -42.501801 | 2024-10-02 00:32:02 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f6431a0b-7f34-37aa-8207-36bf39644c38 | -6.9483 | -42.491299 | 2024-10-02 00:32:02 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10b75c36-7442-3f5f-beb1-fbc4aa98e1f8 | -7.5664 | -45.005901 | 2024-10-02 00:32:02 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 031553f9-084b-3de5-80ce-b234b66a87d2 | -7.5566 | -45.008099 | 2024-10-02 00:32:02 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f6cae369-b12f-3bce-88db-652c36a402a5 | -7.2596 | -43.816002 | 2024-10-02 00:32:02 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e9ffaa3-f940-3b6e-9368-e4f3fad9ff8c | -6.9386 | -42.493599 | 2024-10-02 00:32:03 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a014cff1-1686-3f2b-94cf-6e281ea9431f | -6.9411 | -42.504101 | 2024-10-02 00:32:03 | METOP-B | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2255df8e-fec1-33fe-acef-465790b12c90 | -7.2543 | -43.881401 | 2024-10-02 00:32:03 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba8d5d3b-1a40-39e9-9b17-f8e1f8f004b3 | -7.5784 | -45.281898 | 2024-10-02 00:32:03 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c5b306eb-61b0-3476-b407-da90bf9eab69 | -7.4356 | -44.840801 | 2024-10-02 00:32:03 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b75710c-ee00-388a-b4ff-de98ae70b98c | -7.6179 | -45.499199 | 2024-10-02 00:32:03 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1567623a-3506-3d21-a940-d3aea88f4c4e | -7.5966 | -45.4963 | 2024-10-02 00:32:03 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de7da813-d573-3cc0-93b9-12a08597dcdc | -7.5983 | -45.5037 | 2024-10-02 00:32:03 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a723949-120a-3008-bfd3-5946d5be85e2 | -7.7119 | -46.1371 | 2024-10-02 00:32:04 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d84fdb4b-a248-32bf-bd99-c7db9e67731d | -7.7135 | -46.144199 | 2024-10-02 00:32:04 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed1727c-8a52-3733-980e-e827bf473647 | -7.7152 | -46.151299 | 2024-10-02 00:32:04 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 241ebd6b-0431-3dc0-8497-809434f75d2b | -7.7168 | -46.158298 | 2024-10-02 00:32:04 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aead078e-dc38-3d2f-ab72-9a8e562ddc5a | -7.3986 | -45.172699 | 2024-10-02 00:32:05 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d643f3e-1d59-3062-8a98-08a7b29e8232 | -7.2888 | -44.9646 | 2024-10-02 00:32:06 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3db1608-8de7-38c7-8a11-adb4f3ea5afb | -8.9615 | -52.797401 | 2024-10-02 00:32:07 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb232d9-5032-3b18-96c1-b8d1d40abbf4 | -7.2238 | -44.9958 | 2024-10-02 00:32:07 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a336fd9-b9cd-3627-85a9-93cb4bca199b | -7.2256 | -45.003502 | 2024-10-02 00:32:07 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5349e1b9-5225-391b-8ff3-690f43947b3c | -7.0356 | -45.343399 | 2024-10-02 00:32:12 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 753ac7fc-2832-3e52-9513-f5e52c151230 | -7.0874 | -45.659302 | 2024-10-02 00:32:12 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e8ac431-cbcc-3f44-be02-83c5db07c859 | -7.0891 | -45.666599 | 2024-10-02 00:32:12 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 968badfd-4d1d-3a09-8dd1-0211e23e2338 | -6.993 | -45.337299 | 2024-10-02 00:32:12 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 861c674a-f61a-32b3-afb5-a70fe00281b7 | -7.2521 | -46.8363 | 2024-10-02 00:32:14 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09e30b76-7c95-3b6c-87c5-e0e840faa03a | -7.1002 | -46.438999 | 2024-10-02 00:32:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd65046a-1527-387e-a471-a4a7ef58dd46 | -7.1018 | -46.445999 | 2024-10-02 00:32:15 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa3afa6d-d611-3dd4-94b2-01d1e4cde6aa | -7.181 | -46.932301 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2b817a-e19c-31e3-8686-33840fe72352 | -7.1826 | -46.939201 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c24c4ed-8ca4-3b8c-b0b4-2f94ecc6a18e | -7.1842 | -46.946098 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3131dc0-6bae-3cbe-85bc-f820ab9bab47 | -7.1728 | -46.941399 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d65c1fca-91ec-3a9d-839c-9aee2c60f09a | -7.1744 | -46.948299 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee9f30f-1498-3ea7-a7aa-a30b2441f3e5 | -7.1759 | -46.9552 | 2024-10-02 00:32:15 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f57c923d-0c96-3915-b13a-3ed3d28a1589 | -6.4398 | -43.9701 | 2024-10-02 00:32:16 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8251bdfc-23fd-351a-8f64-3fc36e5a23cc | -7.1387 | -46.927299 | 2024-10-02 00:32:16 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a65d6fb7-6faf-3182-9ae7-7693200eeb93 | -7.1402 | -46.9342 | 2024-10-02 00:32:16 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8232e655-71b9-33ae-b997-bd71abca127b | -6.1454 | -42.887798 | 2024-10-02 00:32:17 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de2e9d84-2d2b-34fb-9429-c102736430a6 | -6.1477 | -42.897999 | 2024-10-02 00:32:17 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d0a1f5bf-a128-34f4-b2aa-12e6d1ed1a1c | -6.1379 | -42.900299 | 2024-10-02 00:32:17 | METOP-B | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff4d9391-dade-3da9-84a9-0a6be48ad499 | -5.9071 | -41.9659 | 2024-10-02 00:32:17 | METOP-B | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 23e5656e-8242-38cc-a8d9-d21a2278a72e | -6.7797 | -46.027 | 2024-10-02 00:32:18 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4927f8c-9357-306b-841f-db328cb73bee | -7.1012 | -47.860298 | 2024-10-02 00:32:20 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82cc5ffa-354e-3ef0-9db1-cb0dd8172e1b | -7.1028 | -47.867199 | 2024-10-02 00:32:20 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d2c7f43-abe5-3fb4-997f-18966b25d18b | -6.3914 | -44.740101 | 2024-10-02 00:32:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4fa53e4-7856-34b7-a3ad-8e88ca3bccef | -6.3933 | -44.7481 | 2024-10-02 00:32:20 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b6b965a-8850-327d-8896-3407fd4f948e | -5.9441 | -43.259998 | 2024-10-02 00:32:22 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 829fe3aa-8c37-30c7-b388-318f030b4d13 | -6.2917 | -44.754601 | 2024-10-02 00:32:22 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46372148-a1b3-3440-af85-a8ba9da8f435 | -6.2935 | -44.7626 | 2024-10-02 00:32:22 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56283b46-26af-372d-8289-2738105218f5 | -6.9507 | -47.648399 | 2024-10-02 00:32:22 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e19471de-1eae-30bc-b829-3a76a84d6cdd | -6.9523 | -47.655201 | 2024-10-02 00:32:22 | METOP-B | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f31438ab-c779-393f-adb9-aae21628acf3 | -6.0933 | -44.031898 | 2024-10-02 00:32:22 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 587c0b9c-a8c6-30f6-8e07-f231bea3142d | -5.875 | -43.7141 | 2024-10-02 00:32:24 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20510474-924b-31bc-a85b-0f4360819ded | -5.8772 | -43.723301 | 2024-10-02 00:32:24 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac9b781e-cced-3e47-be2b-ac9e457704b9 | -5.8808 | -43.960201 | 2024-10-02 00:32:25 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c96d2ae-f0d6-3203-858e-7539cc8e681e | -5.8829 | -43.969101 | 2024-10-02 00:32:25 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c6e123c-bf85-3a7a-ac4f-36e67f19d179 | -6.1235 | -44.919498 | 2024-10-02 00:32:25 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25633f56-4c70-3d22-88b8-5c4a67c50bac | -5.8158 | -44.123901 | 2024-10-02 00:32:27 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 911036ca-6c6c-35ce-ad28-6d190367448d | -5.8472 | -44.660099 | 2024-10-02 00:32:28 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e65511c0-eb7c-358b-aa89-d16861751681 | -5.6979 | -43.927299 | 2024-10-02 00:32:28 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b382c6e-f82c-35e6-a828-4ab7cc2a771b | -5.7 | -43.936199 | 2024-10-02 00:32:28 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8edb56-a0e5-31ee-8db1-42631d6002d1 | -6.2289 | -46.3694 | 2024-10-02 00:32:29 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e477b3e5-b898-37e1-93c4-8638f949e931 | -6.2305 | -46.376499 | 2024-10-02 00:32:29 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0f2d329-ced7-3b52-b4c8-ab05792277e0 | -6.2321 | -46.383598 | 2024-10-02 00:32:29 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5416042-08dc-3807-ba82-ba2b418a3e91 | -6.2337 | -46.390701 | 2024-10-02 00:32:29 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7057b2fc-c45d-3217-aadf-f9c90d5ac171 | -5.978 | -45.362301 | 2024-10-02 00:32:29 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b106158f-6829-307a-a4cc-c84956a7aba9 | -5.9797 | -45.3699 | 2024-10-02 00:32:29 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3730845c-1a65-33cf-a779-fae4d2ef2a8f | -5.9682 | -45.364601 | 2024-10-02 00:32:29 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e38cdb3-f238-3e03-b8d3-ae310c2a657e | -5.9699 | -45.3722 | 2024-10-02 00:32:29 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75a591bd-4797-398d-beff-0197c8870a1a | -5.6751 | -44.183899 | 2024-10-02 00:32:29 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72431ad6-ea5b-308d-b720-9b735b8e5297 | -6.2755 | -46.983601 | 2024-10-02 00:32:30 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31508275-75eb-3c7f-9849-4017369274f9 | -6.277 | -46.990601 | 2024-10-02 00:32:30 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6058037-1c2b-36e8-9131-af9fb321c732 | -5.9014 | -45.387798 | 2024-10-02 00:32:30 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0351a1c6-32f7-307c-b591-5174ed035c02 | -5.9032 | -45.395401 | 2024-10-02 00:32:30 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef019df2-ea3a-3235-adbd-ae63c8af55aa | -5.9049 | -45.403 | 2024-10-02 00:32:30 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ee53703-5ce5-39a1-9190-febf5b823bdd | -5.8934 | -45.397701 | 2024-10-02 00:32:30 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff9614ae-9119-3096-97a4-c36a07e8df0a | -5.8951 | -45.4053 | 2024-10-02 00:32:30 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cefae861-bf65-3791-9005-23647e384f76 | -6.1323 | -46.443298 | 2024-10-02 00:32:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70ff8b5f-8034-3d39-b9ab-75130fec2121 | -6.1339 | -46.450401 | 2024-10-02 00:32:30 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8089954f-9619-3a66-b56f-5bc15ccbdae3 | -6.4181 | -48.258499 | 2024-10-02 00:32:32 | METOP-B | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 91ff5873-16e1-31a5-b4a0-9ef7714266cc | -6.4196 | -48.2654 | 2024-10-02 00:32:32 | METOP-B | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 630cb5a2-0598-3149-8a9c-8bafd0d42a78 | -5.8893 | -46.281601 | 2024-10-02 00:32:34 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6be88c7-c3cb-3c54-b87e-e695b3189496 | -5.8909 | -46.288799 | 2024-10-02 00:32:34 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3762895f-854f-3f34-8bd1-8c13146793a8 | -5.8483 | -46.418201 | 2024-10-02 00:32:35 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86133189-e7f1-33e8-8f94-41040b250842 | -5.8499 | -46.425301 | 2024-10-02 00:32:35 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 258db058-5611-3716-b9ec-e6793a1d6529 | -5.8515 | -46.4324 | 2024-10-02 00:32:35 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b709aa02-7eb0-35a9-b1ca-70fc403c6780 | -5.4402 | -45.175499 | 2024-10-02 00:32:37 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d7e2600-2f81-3c41-9306-d618d31ae1e4 | -5.442 | -45.183399 | 2024-10-02 00:32:37 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5636e5-3e64-3571-8ec4-9f27a1b3f864 | -5.4017 | -45.996601 | 2024-10-02 00:32:41 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a55ed02-c702-3cef-b95a-3549395d2c63 | -6.0889 | -49.3218 | 2024-10-02 00:32:42 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faccf89d-5bf2-3333-9880-52feb885545f | -6.0905 | -49.329102 | 2024-10-02 00:32:42 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 261fdd65-777c-3804-89d1-2e52e90a1d2e | -4.6573 | -43.750301 | 2024-10-02 00:32:44 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
