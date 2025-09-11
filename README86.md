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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8609e2cf-9eef-3848-80d0-9f3ebfee0543 | -6.41455 | -44.48835 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08b74b8f-7363-3d66-88ec-fd8dddf3f467 | -5.66828 | -43.33617 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 996b8835-4a55-3ccf-a8b2-5f938c96c02b | -3.42423 | -49.04921 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c508e3a1-a97a-3825-b636-bfb6b0b5c9b1 | -1.6278 | -55.35839 | 2025-09-11 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b900f27f-3fad-3017-ba30-33073c8bb309 | -8.56977 | -45.58648 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7f5101-5498-3b7e-ba88-300bc6698307 | -5.66243 | -43.89762 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0f9b56d-dd68-3269-b340-075b4e306023 | -6.25623 | -43.49317 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 305e1f11-09ca-3789-b4e4-f9f999e2c275 | -8.73432 | -47.10049 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99b9002f-c980-3fca-b34a-95de09694e76 | -7.48677 | -54.95139 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 034e56d6-ef72-36d4-ae6e-d244152832ea | -3.53711 | -52.19835 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9fb3d19f-677f-3467-ab88-0254e5b55b9e | -6.6096 | -53.34395 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62347d16-0202-3355-9a00-c5508dabd1c6 | -3.0806 | -48.82109 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e11f15e-b38d-3218-a3ab-06286ad4f2c3 | -8.03881 | -52.37546 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8ccd6ef-74ae-3010-9059-4e7885c6592c | -3.79496 | -51.16215 | 2025-09-11 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e909acc-1d9f-3964-ad7f-cc87177fc915 | -7.79008 | -50.76784 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb4f2cd8-7679-3246-8480-f73a1332aa2d | -9.05089 | -45.78594 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ff36117-ad8b-3f7e-8eb6-e89d484ca857 | -6.85953 | -47.85448 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4237e3ff-3510-305e-a22a-d0ce9fd7f9ce | -7.39563 | -47.37104 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57bbe027-e199-3ad4-a966-dc239477b786 | -8.08055 | -50.19161 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba7d0669-7772-365d-9581-a55ecca6ee84 | -9.06387 | -47.06574 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f30124fa-60ea-3453-b8d9-7e885f27e98b | -6.17118 | -41.08377 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 10ff1211-da9f-3948-b5d3-587ed228935b | -7.31342 | -49.61205 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b26475e-5d68-34a5-abbe-03d2d50ce53c | -8.0794 | -50.17692 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33197c9a-eb4e-3405-8964-2a43cdf81f16 | -6.25728 | -44.85396 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da72b075-9eba-3082-be49-8c9dd8dc9733 | -3.08224 | -48.82085 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d29de4e2-9c95-376e-ad44-67428426e711 | -7.49626 | -48.26077 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb78251d-6b93-3c7e-9694-daa34fa9be28 | -8.65751 | -45.72852 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f629c69d-a90d-3f2e-b79f-fb6d54e97f2d | -8.85835 | -47.27231 | 2025-09-11 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0853c66-67f4-3795-a73f-e798ad6cb183 | -6.56712 | -44.21244 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 43bb4a6f-8d42-3865-9f00-9faf984e333b | -7.49392 | -48.25203 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f5a15b0-1ea2-33db-b40d-5a8c5163dc6b | -6.49003 | -49.18007 | 2025-09-11 04:44:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eda8f49c-ea15-34be-8803-c902ad89446f | -9.1172 | -46.97179 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11b63abe-d492-3cfe-b464-3231a9641bb3 | -6.34614 | -45.18885 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba35ce2b-a9d4-3932-a3ef-ff0131f5e9a7 | -4.45756 | -55.05287 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af854328-dd04-3d4d-b579-2567ed753493 | -8.50824 | -45.68876 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22522a2c-bd86-3a48-9abd-7256aa080465 | -4.90047 | -45.67673 | 2025-09-11 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92a0b027-3666-3ec0-bb67-080296ca890d | -7.3725 | -47.42299 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adadd9f6-dd7e-333a-852d-285889eef2cb | -6.30128 | -44.58651 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9ee78be-d2b1-364b-9c6f-1430f60d078b | -7.20284 | -44.9641 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c20d4d33-95f5-38a5-9a62-dcefe47f9b07 | -8.48205 | -47.29089 | 2025-09-11 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18ea0ca0-03c7-38cd-b53c-520afa78fd3f | -6.19811 | -42.49186 | 2025-09-11 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2bbef736-794a-3f06-9dd8-a96eada3fdc6 | -7.18972 | -44.96214 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1088c028-6d4b-3a04-ae9e-f49418f0a497 | -8.5607 | -45.58888 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4537bbb-4be0-39f2-97c8-dc40360f8de2 | -6.31906 | -42.21618 | 2025-09-11 04:44:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 87d7074d-a2d7-3a8c-81bb-67c3e2b70634 | -6.8725 | -51.97552 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5695073f-1d72-3ebb-a25c-11682e9d04a9 | -6.83383 | -47.90213 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2999a8af-dc36-3c50-980f-caeb0224469c | -8.03645 | -48.6758 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7b888e3-64de-397e-a51d-322fbf5a7d29 | -6.53775 | -43.10653 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d52a3fc7-5366-3ee9-8e65-6c04842eb662 | -3.79606 | -51.15522 | 2025-09-11 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1aa6d18b-44ce-3bd2-a463-bb3206d72e61 | -5.22049 | -45.42976 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9c84938-02f6-3fe1-9b5a-3bffa5571987 | -6.61369 | -53.34069 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15b93e77-6901-3961-be1b-abb24500919c | -6.17129 | -42.66967 | 2025-09-11 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2cdd2df5-9d9d-3716-9690-6c05c472dfdd | -5.94583 | -45.71726 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ace09004-bd8b-3111-841e-ddc376f437ce | -6.32146 | -43.41437 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 094d84d3-7721-3510-8aa0-99d2339e0863 | -8.14027 | -49.5139 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 530ede0b-d5a0-306f-a234-358e0b220f18 | -2.78855 | -48.60663 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31746110-b772-3c40-ae5e-23198ec30ee5 | -8.96742 | -46.0681 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc2356aa-e1b4-3bfe-bb01-cf73a83b6c19 | -9.12751 | -46.19138 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ffbf208-5127-3494-a3ab-a5bbbc96bc41 | -7.31964 | -49.61675 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da5eef1c-1b5e-3506-87aa-a12e54bc6c31 | -6.73589 | -43.98923 | 2025-09-11 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61829205-b872-3ac0-87e9-60ffd9fe5969 | -5.76662 | -45.52185 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 396455f3-e11c-3eed-b7ce-f7c9e67667b0 | -5.40386 | -45.92594 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7502c821-04aa-3137-b58d-126f8045aa2a | -6.46711 | -53.40915 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526d29dc-c091-3247-908e-5144588b8473 | -6.40001 | -42.60295 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e7e90eb-20f3-32de-95eb-24cc1d67daec | -5.84259 | -46.15702 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c58a722c-aeca-3c45-b17d-7a6db6cd5e2d | -7.48347 | -45.28821 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79107be5-481b-3878-832b-948920a11059 | -7.46997 | -45.2905 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae23d51-e2f0-3ae8-b902-44bde726ca4c | -6.43683 | -44.04594 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e956725-c1fc-39fd-adf6-900957df56a7 | -7.70149 | -45.14928 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6dab1ca-aef2-3fbb-8378-ed9aae51aa7b | -3.94331 | -54.80481 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77400958-5f9d-3471-88ef-bade3073639b | -7.77376 | -52.12006 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ca5e677-7cb2-31df-8bb3-b1c77a77198d | -6.85464 | -47.86232 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78b507b8-5d99-3116-a3ff-dfabae8b1478 | -9.14288 | -45.55819 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc926787-422b-3aca-8da3-ac371f6145e7 | -8.01961 | -49.04634 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f165546d-6509-394c-bd50-4e89987630f3 | -6.4076 | -44.50463 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 235fb9ff-79eb-355e-b8f9-c3c8a76d927e | -8.51195 | -45.69307 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 506869b5-8757-3a7e-ae3e-099a9ede0c19 | -3.43953 | -54.63774 | 2025-09-11 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 022fbba5-f921-330e-a409-707d56933d95 | -8.03521 | -48.65996 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96b5b1b6-ff99-3fbf-bca2-adfc6e53113c | -6.31108 | -43.41835 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a79d329-4f61-3d5f-b497-19bc7fe57add | -6.53766 | -44.78276 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c937348c-cd1e-3f56-bc61-b910ca71a8d5 | -6.99413 | -44.79278 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de20d95e-6f15-35a9-88dd-45ea06c38a87 | -8.19967 | -47.13975 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aecd63a-b287-3119-87b5-b45e39119947 | -4.62029 | -47.41676 | 2025-09-11 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c66f9396-6f94-3201-8873-b0e90f606c49 | -7.63912 | -49.81446 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26205361-d510-3b0b-84d8-a7e601476b05 | -6.42016 | -51.7026 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b2096b6-bcc2-3f3c-abec-ae5a42e4b6f7 | -6.42348 | -51.70314 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81415c80-b0ff-3a5d-aa21-07927014b4e7 | -6.85085 | -47.88755 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3772893-2304-33ac-8084-683297132e39 | -8.01458 | -48.65272 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4460b5c6-1550-32da-ae34-64fc4f8e60b3 | -9.0495 | -46.97175 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3809d264-d151-33a0-ae9b-b4cd8d3d8c6a | -8.16671 | -46.09168 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 554b0ddf-428e-3ef6-8c19-234037eb7ba7 | -3.51606 | -52.74859 | 2025-09-11 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c903795-59b7-3709-a520-6be43a55663a | -4.33206 | -48.39601 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f67eb206-e49a-3fe7-bc12-9ff0feb8486c | -6.16018 | -45.81439 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2c900a4-a756-3f94-b0df-dbf85c72e53f | -6.49413 | -45.26622 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7894a2f-bbd1-3f2d-8ec5-13dbdcd769a3 | -9.18866 | -45.59234 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34a3c813-913d-38bc-98f2-0de992d52a19 | -6.30066 | -44.59067 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e426f98d-db4c-3196-8731-991c02a9bbfc | -4.93168 | -55.78364 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8033eeac-8011-301d-97ce-8170a9322ee7 | -7.77849 | -50.77678 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9397893d-fe60-3f0c-a5ff-aed88ffd24f9 | -8.10795 | -49.24751 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47382813-89c5-3818-adf5-9cdb17a98398 | -8.23558 | -47.86641 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README87.md)
