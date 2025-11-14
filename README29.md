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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad3e45f6-b6c1-3e1f-83b4-46f9ca28be03 | -3.35527 | -48.39878 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15d5b88-c389-31ea-ae9f-ff5f0d6a8534 | -9.11672 | -43.95186 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9693d60-1b43-3f39-b83e-b8dcae69a9ef | -3.30501 | -50.10776 | 2025-11-14 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80ad88b4-c86d-30c8-b893-98c9c39f74d4 | -7.87656 | -44.31669 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c887c15f-8653-3fdd-981e-4fab5dfca93a | -7.3463 | -46.01355 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 195a52a2-4fff-36c2-971a-1c77a2165d3d | -3.81833 | -44.24001 | 2025-11-14 04:23:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ec7b95e-611e-3af0-ae66-43510bd3b255 | -8.75684 | -45.66504 | 2025-11-14 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95fc70a0-85db-33ac-bbef-686b73948232 | -3.82001 | -44.25089 | 2025-11-14 04:23:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b499237-84d2-3d51-a997-8bd486f357a6 | -4.0092 | -48.8099 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a22d42e-ac73-3173-9ae5-1088c5dec76e | -4.40969 | -42.32811 | 2025-11-14 04:23:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 104fe34c-e566-3916-a9c8-41465964b3bc | -8.30481 | -43.80822 | 2025-11-14 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34133ead-f4b2-3bdb-9618-abca95a65153 | -3.99325 | -47.18686 | 2025-11-14 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e269b2d4-74cf-37fe-9e1d-020f4de2c0a0 | -7.84651 | -44.29037 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b77aaa9-76ff-3510-b84f-add85cb053fb | -2.94652 | -49.36012 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddb4d6ba-6517-3977-a50c-2a39a0bbcfeb | -9.06194 | -44.7802 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b18e206c-90e5-313b-92c5-1c4e8c276742 | -2.83941 | -45.48338 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5d8f3c02-eb7e-35cc-8d05-37ec37ae3279 | -7.93469 | -44.33294 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0054c7b7-dece-3105-b667-47712e943cb8 | -7.75157 | -45.90003 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffb50221-f8e4-38a2-afbf-07057e47c77b | -9.01174 | -44.06421 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b0ed5e6-eabe-3db5-9529-23f96ccf7ba6 | -9.00785 | -45.44787 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b4eb593-b934-3ae6-8450-7749d07e7f37 | -3.81615 | -44.25382 | 2025-11-14 04:23:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0cc96a9-9eea-3824-99c0-d495f996d2ad | -7.48494 | -45.91198 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b8c2d61-40e4-3cf5-9272-7c2b5551844a | -7.77715 | -48.05117 | 2025-11-14 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98209ccc-2552-3500-8de9-dab60cc67590 | -9.93997 | -45.09547 | 2025-11-14 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18e514fd-9696-34a6-a928-c8baae33a6dd | -3.95472 | -47.49877 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cebd3b0-e580-38d0-9eb9-b98d598d68dc | -4.47666 | -42.87909 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84d9b630-ad9c-3c7a-8191-6eb87603d5f0 | -2.71324 | -47.39702 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9798b341-4146-3ae0-ad84-b8bd47e05732 | -7.51439 | -43.00557 | 2025-11-14 04:23:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b17e43f0-7a27-3f1e-be28-43e385276351 | -2.46617 | -48.22792 | 2025-11-14 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58d469e1-23ad-3f59-b6aa-eeb2758d8650 | -4.64585 | -42.96034 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f08556a7-7fa2-3848-b6bd-9a79c781ddbb | -3.34594 | -48.38241 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 640e69b5-8c97-35de-bbe3-900db6cea64f | -7.54909 | -47.24411 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a34fce7-dc16-37c3-92a1-f80d1fb241ff | -7.06853 | -48.36258 | 2025-11-14 04:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baaf3acd-b56c-368d-a36c-2e0f89a8f614 | -6.6861 | -47.7993 | 2025-11-14 04:23:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42724b9a-84fd-3537-9dc3-1d70f1db19f1 | -4.52873 | -44.62423 | 2025-11-14 04:23:00 | NPP-375D | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3be7d7ea-dcf2-3584-8c54-5fa1a59640b3 | -7.44764 | -42.56774 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3614f27e-f6ff-3ca4-88ef-e9cd213dc387 | -8.61436 | -48.53907 | 2025-11-14 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a123adac-0c95-3c91-840d-a9caa0f2a1d9 | -9.00729 | -45.45136 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0162817e-66ba-3493-b155-ac6e068ce524 | -7.45288 | -42.5804 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7372d758-a12b-3fa3-b18b-b419ababe03f | -7.45753 | -42.57324 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecdd1eea-a1bd-3984-96c8-f87ac66f865c | -7.45988 | -42.5577 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a193de3a-3c6c-33dc-aad0-4e2405a07700 | -9.94145 | -44.93372 | 2025-11-14 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1abeb132-7bd6-3168-988a-e39650bd9cce | -10.36977 | -47.68663 | 2025-11-14 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2442dcd1-d3d5-3e6b-8e43-46de95b7c28d | -9.68185 | -47.89327 | 2025-11-14 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b9567ae-83fe-315d-8157-f56313979535 | -3.15369 | -50.26707 | 2025-11-14 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8daea379-6ab0-3713-8a9b-07cc989ac9cc | -8.30915 | -43.646 | 2025-11-14 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 567aa96f-a417-3926-9f74-ab3c85c70d85 | -2.11727 | -45.36728 | 2025-11-14 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f8512fe-1e0d-3c73-9f99-299f6faa2f0e | -2.6547 | -46.99632 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e653644-aaea-31dc-8595-83380d58748b | -4.00608 | -48.80422 | 2025-11-14 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96bb48eb-357d-3575-9e2b-e5a4baaf38a8 | -9.1201 | -43.9524 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e263d3a-c92b-3793-9ef9-83584623444c | -3.17028 | -46.5765 | 2025-11-14 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd13b1b9-a353-3407-b552-d2b966d089bd | -10.75037 | -44.913 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 928ee036-0a75-3072-982f-ec4e3fcc2bc5 | -2.467 | -45.18876 | 2025-11-14 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 52bc287a-775a-3f04-9a90-b4bbcf8cca8d | -3.61745 | -45.94989 | 2025-11-14 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5359b6-3a51-3ac0-9277-685ca7d98bd1 | -2.46982 | -45.19287 | 2025-11-14 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434da441-99ba-3233-8ae4-0360036cde56 | -7.1467 | -46.29375 | 2025-11-14 04:23:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a88bb55-945a-3c72-ad6c-3fb9e33a0053 | -10.28872 | -44.35755 | 2025-11-14 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e99fc21-a10a-3ff5-b070-360e2b7952fa | -2.83992 | -52.36677 | 2025-11-14 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0aecb99-608c-38ec-987b-42b92ac0415d | -3.41491 | -42.68008 | 2025-11-14 04:23:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9deb1d9f-7ee3-31af-9134-81d1d582831b | -4.58222 | -40.48471 | 2025-11-14 04:23:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea3e78bb-094e-3c28-8acb-2265132accbd | -3.34516 | -48.38723 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9063c81-c761-3fa8-b7cc-c675deef2f18 | -10.32307 | -44.27775 | 2025-11-14 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f71a9fd-1b16-3ca0-9a76-2f4b42f8a61d | -7.45986 | -42.58149 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| caa45720-5178-3bde-ad88-3c62eea253ca | -8.94475 | -49.81977 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2210cf-641b-32a7-b710-4366c572c0a2 | -8.94168 | -49.81411 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2fc7efa-0aef-3712-95f4-f01dd1e207e0 | -4.45069 | -44.0067 | 2025-11-14 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59b21b38-f429-3950-b1af-059378b7abf4 | -4.40625 | -42.32758 | 2025-11-14 04:23:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a4862b31-a1be-331c-9d3b-4ee79b84e2fd | -3.01587 | -49.44046 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8977580-22a8-3247-b7c6-6867b960d9ba | -4.41534 | -46.02793 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 147738a6-8469-38c7-a5dd-1745a649e3b0 | -3.35992 | -48.39466 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2f60ee8-620e-3d47-9f5c-964537161243 | -9.09426 | -44.31901 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45db40f3-6383-3e3e-964c-d17ae65a5029 | -9.8547 | -44.16477 | 2025-11-14 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e2178fb-bf6e-3faa-89f3-c9eae64f7a1d | -3.76834 | -47.72842 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 883c5668-4f2c-3eec-aedd-6916b0c7c410 | -7.66636 | -45.88277 | 2025-11-14 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba093009-d063-3c70-ba27-07ed932616fa | -7.38131 | -48.65252 | 2025-11-14 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9a0baa6-2d3d-3bc1-85c5-09f9c3932b48 | -7.46335 | -42.58203 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1ebbc20c-ac3e-31c6-a0c9-4e78559b7e67 | -4.59148 | -44.40023 | 2025-11-14 04:23:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc9039fe-4bf3-3e3d-a818-6b86fae9c6f6 | -0.86545 | -47.30967 | 2025-11-14 04:23:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a73c8338-0a2f-3765-87bd-9721c8b769f3 | -10.62679 | -45.00955 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79d91431-2aa5-35d2-bdca-437b7054737d | -4.0751 | -44.13515 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b55308e-7fb7-3cb3-8463-fe764abe07ca | -8.68891 | -44.39691 | 2025-11-14 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e0811b1-3320-3487-89bc-9a57a3566bda | -3.36257 | -49.5101 | 2025-11-14 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ae4f48e-5427-31e8-bdb7-db0d007763af | -4.57479 | -43.12822 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35cf2edd-cf98-37a5-b2d6-63167c6a1a34 | -7.92605 | -44.34964 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94e01049-eb35-3289-be9a-e5fc10ad44be | -8.3131 | -43.64291 | 2025-11-14 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e351e8a7-6c51-3714-a0ee-86fec07f7d22 | -11.09028 | -43.17026 | 2025-11-14 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9bb93f6-53b0-3825-97da-ecf38ee56f8e | -9.00619 | -45.45835 | 2025-11-14 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3d52864-b4cb-36a7-9787-6f6538f41b18 | -3.76178 | -47.74539 | 2025-11-14 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8451b8c8-9600-3cca-b35b-1016bdee4325 | -7.86766 | -44.3081 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e8c63a8-37b4-3390-a524-994b5487d4aa | -3.46301 | -43.18353 | 2025-11-14 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad169b1f-618e-34e9-8d63-995451361040 | -3.48067 | -45.64625 | 2025-11-14 04:23:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9ad760-8491-3ff1-9a1a-d6f5561ee2d2 | -4.13095 | -43.01286 | 2025-11-14 04:23:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 210a9122-578d-315e-b0ef-e9e0404a17db | -9.09309 | -43.94815 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b611096c-13eb-37bd-9947-cb852c6d7b19 | -7.88935 | -44.3223 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25d88bf6-2a8c-30bc-b5a6-ab21405c1204 | -8.93693 | -49.81841 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80361bc4-b77c-33df-ba14-130156991e90 | -4.00342 | -47.1462 | 2025-11-14 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1636c565-5f13-35a8-aaf6-0fc547f956d1 | -9.93665 | -45.09494 | 2025-11-14 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1517edaf-6ad9-3fb6-bebb-15b003857d7b | -2.11444 | -45.36311 | 2025-11-14 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41c92bca-b40b-378f-b138-40638147598d | -4.71912 | -42.94202 | 2025-11-14 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b8f4c03-d851-309d-9379-e303c50581d5 | -7.71797 | -47.18792 | 2025-11-14 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
