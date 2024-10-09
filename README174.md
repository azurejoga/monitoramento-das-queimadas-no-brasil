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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f8f33d8-d651-3358-8042-b8f7c05a2c8b | -10.99765 | -54.25076 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f22f7b9e-78fc-3310-8ecd-1e7610fa7f06 | -10.99006 | -54.25366 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db1094d1-22a0-3400-849b-0db3bedf5982 | -10.98656 | -54.25313 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404856d6-e72d-3d4a-b032-a612459703a9 | -12.35166 | -54.15447 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b330395-5d69-321d-b311-4c8e2678bd4b | -12.34809 | -54.15393 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7bebbb4-d05e-3675-9796-502322f73ee7 | -11.44362 | -54.47977 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123b8ce7-babf-36b1-a015-c3f449f2102d | -11.44072 | -54.47532 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76b818b5-492b-3471-b1d2-9f62250ba0e9 | -11.44014 | -54.47924 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1077e86c-d6f1-3531-8fe3-d290540c6fbd | -11.28834 | -54.57999 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fae801f-0490-3050-8c16-9aac0ea82a49 | -11.28487 | -54.57946 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e4a778f9-376f-353d-b2de-e4de7808442e | -11.2843 | -54.5833 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10ec4f5b-a171-3e43-9810-a80501f6bd9f | -11.28373 | -54.58714 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f045b93a-8dd1-3c82-b150-84b0ae029630 | -11.28084 | -54.58278 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86302d13-faab-3008-ac32-7e6c4b4fd68d | -11.28026 | -54.58662 | 2024-10-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05cd0b29-a890-3f36-9a1e-5c98a5acd1d5 | -11.13528 | -54.3194 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c8df194-3610-3909-9c39-ed0e1ee84cb2 | -11.13439 | -54.00925 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d067e179-f9e5-396b-84b2-52a6d98c0273 | -11.1338 | -54.01328 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a65c6ea-939a-3aff-8418-dfff7fb90ec8 | -11.13321 | -54.01731 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1405d2a4-60de-3786-96a4-1faa934f661a | -11.13144 | -54.00468 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15bba382-a998-3a71-9cc1-5d3939591ffc | -11.1312 | -54.32282 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07761e61-65d4-3c86-b784-4dc8462727de | -11.13085 | -54.00871 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528da67d-fadb-38af-bdde-2b6e0316000e | -11.13026 | -54.01274 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be77648b-2ae6-32e9-82e3-3a0a1e388c06 | -11.12967 | -54.01677 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d4084ad-d840-3182-990e-0bea48555dd4 | -11.12908 | -54.02079 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9350248a-c76f-3919-b81b-188a86250662 | -11.12789 | -54.00412 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3f739d8-87c5-38ca-8cb8-cde905bf4231 | -11.1273 | -54.00816 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 180a8c2c-ad8d-30f5-be2d-17c830344ffa | -11.11728 | -54.02724 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3ff9721-89a9-3c57-9cee-0beb29d97f3d | -11.11374 | -54.0267 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b98bb94-0c0a-3853-9498-dd5a5cc99055 | -11.11316 | -54.03074 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33abe6d2-4ce7-3304-bab5-e1f9b4038b28 | -11.1102 | -54.02617 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b3a870b-6b57-3ee5-b027-1aa5084cc4dd | -11.10962 | -54.03019 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1150b424-6021-3e4b-a2c8-177508e6354b | -11.10725 | -54.02161 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3349da33-c952-3cf8-b175-3f7c73d2ee70 | -11.10666 | -54.02563 | 2024-10-09 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 994017d0-bf37-37e0-a352-030d80f2ea22 | -12.90922 | -55.64395 | 2024-10-09 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6450d11b-06be-3023-806c-f61b7cf26115 | -12.89092 | -55.44323 | 2024-10-09 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe8f4bd-463a-3696-b559-01dc702b2458 | -12.88751 | -55.4427 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4c51108-2326-3e3b-9552-e57061c04f94 | -12.88695 | -55.44644 | 2024-10-09 05:04:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4988705-07b9-3357-8def-e71cf9036e59 | -12.88411 | -55.44217 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89ac6d6c-5d8c-34d2-9120-02b747f1231c | -12.67281 | -54.72147 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b775228-c4a5-34f2-a1ca-75e367da1ef8 | -12.67223 | -54.72538 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4acb36e-f994-3392-83b4-90ef902d7a54 | -12.66932 | -54.72093 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 220ec146-b624-3cb8-838a-ec6aedd88bca | -12.66875 | -54.72484 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e545307c-d55a-3c1e-8e3f-67d53d2bcae4 | -12.66642 | -54.71646 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b152691e-8f88-3c9e-96ef-6729a0d7ea20 | -12.66584 | -54.72039 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d6eb160-b868-3fa5-afa0-e2211c51bd27 | -12.66293 | -54.71592 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697c6905-665a-3c59-a9f0-94f219c5edcf | -12.66235 | -54.71984 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae0b8a95-780e-387e-b9b3-923991a5717f | -12.65478 | -54.69851 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d362a991-0ef0-3b3f-b060-410a1d4dd22a | -12.64316 | -54.70479 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c740e129-62e2-3abe-ba2d-be01f9ee01f6 | -12.63442 | -54.69131 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61e99429-3065-33ef-8f2c-d8b56bcf86ac | -12.63385 | -54.69526 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c4d26ba-3407-3344-b409-28a006a01aff | -12.63309 | -54.69206 | 2024-10-09 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92010f85-96ab-35d4-a4c6-978bd75136e1 | -12.59506 | -55.22189 | 2024-10-09 05:04:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c8220da-bbd7-352a-905e-dbefdfe35542 | -13.96119 | -54.60026 | 2024-10-09 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28b2cfe0-b6be-32a7-b88a-5861ef8f9e38 | -14.8272 | -55.89822 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca0d3cc8-8c0f-3d83-a915-54a098acc681 | -14.78646 | -55.98408 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f806c91-585a-3556-b507-130d53aed7a6 | -14.7859 | -55.98783 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c552e935-5d8c-320d-9a97-bc76bf03e50e | -14.77679 | -55.9326 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d25bd1c-39c7-3c32-8924-eb4b9cb5145b | -14.77396 | -55.92831 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e456846-a9e3-3f2e-99da-de377bec1f48 | -14.7734 | -55.93206 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46844a79-a9a6-3dbd-871f-bbe53924b107 | -14.77112 | -55.92402 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 068a4351-d8de-308c-8877-5c85d7f0fed0 | -14.77056 | -55.92778 | 2024-10-09 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f054c827-2065-3c84-a8a1-e1eb84fe4d1b | -15.39398 | -55.87447 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ff6b2e2-136b-3916-8b54-bbf8ba00843d | -15.38425 | -55.86926 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c1a197c-0a8d-3329-b05b-4dcbb2027583 | -15.55532 | -55.98849 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 573364e2-4c1a-327e-8f33-54aeec1d3a24 | -15.39342 | -55.87825 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eed5e0a9-cb67-30d9-834a-290160c2e49f | -15.3911 | -55.87025 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95fcd233-6f0d-3a83-bac2-6ab64cd00530 | -15.39 | -55.87776 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2df8c427-c045-3e9b-a86a-8995f2bf731e | -15.38657 | -55.87727 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 808dba7d-17bf-322a-b5f5-fea46cc5d973 | -15.38408 | -55.87023 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83d51013-458f-3cc0-aef4-d0e94b833932 | -15.3837 | -55.873 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c0a45fa-393c-346c-a552-0dbe53813d25 | -15.38352 | -55.87396 | 2024-10-09 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 729600dd-e898-365c-a26f-b35ffe8195c1 | -15.93372 | -55.01211 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1478856-08c8-3f5d-bd1c-e4f30055d833 | -15.93017 | -55.01155 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f843d39-3f1b-3e07-b9e0-af8462a8e067 | -15.92599 | -55.01528 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e102a51-42eb-3a6e-8a4f-1084f77e2091 | -15.92537 | -55.01956 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82355d10-e976-35c5-ac48-36e83c5484d7 | -15.92244 | -55.01475 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 698bcdda-9de3-3356-bea2-92a59eeb0584 | -15.92182 | -55.01902 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4222efbe-9c7f-31f8-bf1f-2c37c868f45d | -15.92121 | -55.02323 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e3f4af5-33b3-3c4c-b8f6-e2ce278329c4 | -15.91889 | -55.01418 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc0ea20e-1930-3d85-ada1-66f13e0bad07 | -15.91827 | -55.01845 | 2024-10-09 05:04:00 | NOAA-20 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2b87caa-0c99-3ec2-993d-9e6777aa011e | -15.81737 | -55.31794 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 62cbd20b-61b6-3fff-92ac-e57911785c07 | -15.81387 | -55.3174 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b42825f-ccee-3113-b777-337c255460e8 | -8.32377 | -55.12021 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd59e97-6258-3bfd-83f8-323cdbb0cca6 | -8.30095 | -55.11302 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b05c3b21-82fc-3741-8ccd-449bbd5a2ae4 | -8.29761 | -55.1125 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 48d69099-6444-37ad-88af-cd4ec2f95ec8 | -8.25274 | -55.18172 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e732cb5f-2a6f-30af-808d-59a140e2fad6 | -8.69985 | -55.03226 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8bb7b0d-3510-3a10-8c8f-f6c5096a57b0 | -8.69705 | -55.02815 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32b40c89-9fc2-3d49-a1ac-f69735b1ccbd | -8.62099 | -54.92856 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe04768f-a385-3e19-894f-6a884501750a | -8.62044 | -54.93216 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee93da6a-66eb-3c3f-a77a-e4d5aac61b2f | -8.51198 | -55.15321 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dcbdea9-4f0c-3e30-9fc8-d637d6b59157 | -8.50865 | -55.15269 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3cc693c-a4d3-3db4-ac61-c3525fbdd5bb | -8.5081 | -55.15624 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be93747e-dfaf-3cae-a2b9-e77cdd8d036c | -8.50545 | -55.21752 | 2024-10-09 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 535eb027-105c-35ae-8b27-095a11ce5c44 | -8.48641 | -55.1638 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ecbaea4-f377-32e0-b96f-7be2f875bdea | -8.48586 | -55.16735 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15aec659-61ba-3f4e-9d9d-1b811b80187d | -8.48307 | -55.16328 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 946ec0f5-aa60-32e8-8631-9967e736b708 | -8.48252 | -55.16683 | 2024-10-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5ee3ebe-b490-30a3-9aef-c66f43b263c7 | -8.44717 | -55.24105 | 2024-10-09 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 865345c7-2f62-3bab-b6e8-f37c3b44b85c | -8.44384 | -55.24054 | 2024-10-09 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README175.md)
