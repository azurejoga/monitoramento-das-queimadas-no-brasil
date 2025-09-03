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
| 4d808b8c-2486-3f15-8404-a88c87d6e5cc | -11.05162 | -45.40061 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75ef2018-1124-385a-b2b3-a3509b90e59b | -11.04559 | -52.0555 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e2661a7-2b49-3f91-8068-856d22e33763 | -6.46973 | -55.88865 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 633af33f-7290-358f-a456-13154f0a70be | -8.36145 | -52.52916 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7a31d7-b09b-3475-9411-bfd03e98c3ba | -6.84281 | -44.27441 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a100c70-1668-3c89-a4b5-64e4f6959414 | -7.71067 | -48.72197 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ca3fee-8a7e-3064-8851-867286606dd9 | -7.50304 | -45.3426 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfdc45cf-1f1e-37cf-a0a4-2067ca1a4753 | -8.88945 | -45.8016 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6af68c-0d37-3503-95ab-195665b875ec | -9.96291 | -51.62438 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d1d8f8f-c626-3719-8719-1dccc9699dc3 | -5.69411 | -45.94819 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71f06086-cd0d-352c-a823-4ff9f5269df2 | -6.35069 | -45.6665 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f96ffbc5-9a31-3539-a089-a18e683c1cf8 | -6.69159 | -48.39678 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 62c9206d-3ccc-3c4b-a657-1c60fec1444c | -11.63633 | -52.0603 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6f3f8e8-1a2d-3046-91f6-e4dab052283b | -7.9284 | -44.94412 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d0d5db3-6b73-39cc-b05a-6368d615ad63 | -7.7221 | -48.74305 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c9d9fef-c4d5-339b-a574-1699501c3287 | -8.43447 | -45.08215 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 856866cf-c64d-344e-a49e-b4f20e3abc09 | -10.45336 | -54.78643 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2ae3291-9a30-378c-b5ad-508ec428c7f4 | -7.11412 | -44.31194 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb40ff2-f053-3d62-90ac-8cc2fb805951 | -7.12292 | -43.76201 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e99895dc-b536-3a30-a3cd-55f4d312d679 | -10.97217 | -50.91553 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5274261-3821-33b5-ab62-25b8d6ee1ee0 | -11.0835 | -52.00776 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b35e03-b6a7-3a4b-9a12-99d41d503de9 | -11.09676 | -52.03139 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9993ff48-7c62-37de-9c40-b5b79848b23f | -6.73013 | -42.24878 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 726ec60c-efb1-3c47-9ec5-40dc12f5b240 | -11.61002 | -52.14233 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d73d4d8b-94e6-3b6f-be1e-573d7756cb59 | -11.066 | -52.07659 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b545fec-f255-3ae3-bc87-2b66c7dbedb2 | -5.91198 | -57.72189 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7997c81c-26ea-3675-9843-86a42c98902a | -11.64567 | -52.04381 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7dfb5ba-bc81-3096-96b0-44157571fbea | -6.224 | -43.40439 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4474f7d6-c63c-3575-89a2-0fff4ce26082 | -9.62658 | -47.86046 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 230a7025-033b-3611-a711-09fdb7398aca | -11.08816 | -45.12514 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39e338c0-656d-3223-8251-7a4de2d9765e | -6.5281 | -56.20848 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17eb4c44-48bf-329e-89e3-28ff99384733 | -6.70217 | -44.17747 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 506b8c74-b1e0-3fbc-b9af-b8d794a5eb76 | -11.43641 | -46.91364 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 963be34c-578a-3f99-9c6b-f12cf5c0b8d6 | -11.11628 | -44.65139 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb1f2c05-4858-372e-b76f-38df2c2acc22 | -11.79818 | -51.49655 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 848d182d-f6e3-3689-aef5-f5242ab04d96 | -6.85024 | -52.79107 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55743f37-2943-3573-8e4c-20f344da50b4 | -10.48156 | -53.63663 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc088a68-0687-3118-bbc4-be836a0aaaa0 | -6.12699 | -44.13668 | 2025-09-03 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dae193e6-02b6-3e92-9fcf-518e8fc04d2d | -7.80167 | -45.45798 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e5ffb16-70b2-32a9-9ca1-133654503f10 | -11.5918 | -52.1071 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a1193a8a-5735-3b0b-8c1e-d90d1af573a0 | -11.61323 | -52.07817 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 420e9231-19b9-37a2-8ff9-139fa4b4c3ca | -10.96663 | -50.92947 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 813e1b9c-44f6-39c3-9db9-09aefc717549 | -8.45525 | -45.05192 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ca992c-863b-3103-9df6-54e4715f3913 | -11.42615 | -46.89699 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bb13e30-3cea-38e3-af02-ba2cf7ec4d34 | -6.8429 | -44.27668 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9dd8af0-72ab-30ab-a372-e300ec1b93c3 | -11.60393 | -52.11622 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d39ffbf3-411c-3daa-8c0a-155b1c73c8a5 | -5.94172 | -43.0396 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5b41e2a0-b353-3868-9618-4a1495e31997 | -11.59786 | -52.11166 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d3975b4-e34f-384f-a016-c90c403fb14e | -11.63688 | -52.0568 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3c0e222-538f-3305-9441-e493e13907a8 | -10.46925 | -53.62714 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af58f9f9-aef6-357d-a5c1-141348c50f7f | -6.28042 | -44.51405 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f29787ea-3baf-365b-a933-d8be789c0e90 | -9.28268 | -48.55694 | 2025-09-03 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90c00862-bf06-36fc-8e98-59edd22cebf8 | -8.00828 | -50.08022 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b7570fc-aafb-3c1d-abe1-71fd50ceef59 | -7.63051 | -46.54514 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83f6b541-699c-356b-ad41-d34bc300d91a | -9.64701 | -48.07295 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fecd6fc3-dc55-3883-b9ee-e14261e02cfe | -6.26913 | -42.59692 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8bde28fc-2735-3f1e-84d5-d8ad79ad0de4 | -8.88821 | -45.80352 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00983e79-b589-30e4-9fa9-5ee8955b2c66 | -6.19742 | -43.35606 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0224247f-f325-3b6c-93b7-0a8907300587 | -11.5724 | -49.91568 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1023a450-4504-3173-8570-1be35df476c7 | -6.33839 | -53.44342 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eafc0465-1ed9-3a32-b719-750e47ac4c10 | -6.83996 | -52.83405 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a41dfcd-3b62-3620-bfa9-4ebe822a8c39 | -11.67827 | -52.2076 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ef401d9-53a8-3de0-96f7-0b5b70608b27 | -11.64458 | -52.05083 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08dd6e77-0f53-3be6-bc04-b85cb6a0aa97 | -7.13001 | -44.57027 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465504f0-5d88-323d-9ad1-2cb70d6ea1af | -5.78327 | -46.45782 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e7c439c-a07c-3f0e-b101-c5d62256dd08 | -11.19234 | -55.02015 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 142ae98f-9bcd-3391-9d4c-35b7553c9a05 | -7.49244 | -44.81563 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 67183fe2-ce21-30a5-a6db-c6da67445fa1 | -7.50795 | -45.33912 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f7d3211-df16-3050-be21-34cfcade0af9 | -8.06221 | -45.36103 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ef9ec601-334f-3f27-b5b4-4ba98b2a6539 | -6.65345 | -45.90387 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9895bfb-e5e9-3401-8a05-795cee44e050 | -8.01165 | -50.08073 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f042c741-a266-3b07-a7b3-b6864917ecad | -8.85976 | -52.02534 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fef1b8f6-e8a2-3aa4-8078-f0a4993d4919 | -6.80014 | -52.80168 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9734d78-024b-3003-9a8c-4b23cdbf2c71 | -10.99493 | -46.83078 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5e81762-57da-3eb4-a27c-e61da994b625 | -6.2023 | -43.35664 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92761560-d800-31d6-903a-0f45af4b6936 | -12.18894 | -48.24859 | 2025-09-03 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca2bf975-50cf-31b4-a0e4-d570da07f863 | -7.70569 | -50.25494 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dd8533e1-da55-3f65-acee-ee883f67ce5f | -6.8096 | -52.82912 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ba62c12-4398-302e-8d84-2be9d55ecc1f | -11.6793 | -52.15748 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c423c4f-50c9-3ed7-9367-6b5936f1ded3 | -6.20309 | -43.35115 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6a85162-3586-35d8-b95f-1ab291114a1c | -9.39643 | -48.03306 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc549708-120a-37e9-b99e-c8069ab18de4 | -5.92319 | -57.70985 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b66010c1-2e95-3fad-8c20-e37aeab617fd | -7.94584 | -45.90575 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e032210-91e3-3ec0-9cf8-f064b99a5914 | -5.38545 | -45.94957 | 2025-09-03 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c7269a0-77b2-3170-8caf-5709201c56d9 | -6.83387 | -52.80708 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb024e2-1b7c-322c-ae8e-6a6e6d317f95 | -6.37507 | -43.00904 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f635c67-85af-3e16-ba06-e5fca2d023ca | -5.82069 | -45.37958 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ac1e54b-bd1b-3180-b538-1ff1084d5f61 | -10.54698 | -50.42825 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ebf0432-c19f-334c-a919-cbbb5c68456c | -11.67551 | -52.20357 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66527271-7a03-391e-8f0b-36d0fd4be29b | -11.67381 | -52.17098 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6391d2cb-2256-39a0-b10a-75019845de04 | -9.79694 | -49.98516 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20ff0ca3-75af-3259-93ad-8eb0965ff605 | -7.5617 | -45.71888 | 2025-09-03 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bb7fae8-9bb9-393c-99b7-fabb9acf5de3 | -11.59844 | -52.12971 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99595452-7fd8-39c2-95f2-6120dd9cdeba | -5.90259 | -43.23107 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2369bd2-9062-3d34-bddc-3416d1c582fd | -5.50257 | -42.62981 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d785d30a-c693-3497-82f0-441d4bdefce8 | -5.80371 | -43.23853 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93d933c9-e0f1-381b-9ade-e75ab1f0da3b | -10.00378 | -46.90268 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c37812cc-25e5-316b-9b4c-adfebab42c50 | -7.00195 | -43.25118 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e74974fc-a7eb-3bf2-b849-8fe931c6e0e1 | -5.86779 | -57.7651 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 170ce63c-20f5-3a3a-87d0-08f200b170f8 | -7.99984 | -50.06779 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README62.md)
