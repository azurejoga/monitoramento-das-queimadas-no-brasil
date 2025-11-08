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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d7b1301-54d3-3123-b892-84c2f2718ebb | -7.96939 | -38.27886 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| beef663f-d3bd-3b88-ad8c-c52141961473 | -3.97976 | -46.03106 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d0581c7-b490-3e12-85f6-2d75fd13c9bc | -3.53238 | -47.54391 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 35a6b19f-96b9-31d8-b957-861d846db2cd | -4.59978 | -49.54842 | 2025-11-08 04:06:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f032545-d39e-3de1-9c53-89bcc0464cc8 | -6.09466 | -41.7115 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04fc059e-9411-3cbf-9378-1974c952d69e | -6.67846 | -38.55655 | 2025-11-08 04:06:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06688fdf-503e-35b4-abae-bed967b59ed0 | -6.33188 | -41.69571 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05b3b549-7089-35ab-b89c-f6cae1f62e54 | -3.40472 | -45.43579 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3dddd89c-3263-3ce1-b938-daf9487c3f8b | -5.05618 | -43.31323 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f44ca771-afbf-35af-9de8-944e612e8a2b | -4.03386 | -49.27691 | 2025-11-08 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3df5185f-ad30-3770-a225-8b7034c4c6df | -6.08971 | -41.72139 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9cfd9831-e13d-3c1a-aee7-cc4896302318 | -3.45242 | -48.84109 | 2025-11-08 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35af1077-7594-3c7e-9c7e-d45d1ee10ea9 | -3.09487 | -49.25396 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93de704d-3969-374f-ab75-ef65668391bd | -3.84807 | -49.80913 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac9c8900-61cd-38fa-bd9e-4e2627e797e7 | -3.83411 | -49.8329 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b91845b1-2a2c-3dd9-82cc-8ae5248eb854 | -6.34371 | -39.84423 | 2025-11-08 04:06:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6dc6d4d1-1198-33a9-aebe-cf232c67818c | -3.38954 | -49.55482 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6a486a-c1cc-3d57-800e-1e0660d328de | -7.24121 | -41.90839 | 2025-11-08 04:06:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ebc0b5e0-cada-3feb-87fe-3a70c0f1980e | -4.59032 | -45.9987 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 731a31b2-44a7-3675-a299-9f63ff58dfaa | -4.63716 | -46.20114 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7670f35d-8ff9-30dd-bea4-2b9c4c3d26bb | -4.9859 | -43.57053 | 2025-11-08 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0644d93-b077-3d43-813b-98fdde10df97 | -3.64017 | -45.88495 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c37804c2-efba-3290-a220-53608251f8b7 | -3.43725 | -51.52018 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89cf0024-ea9b-3cf1-85c7-045e7dcbd705 | -3.31648 | -50.12087 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5511912-18f5-3303-bb2f-6396f77be147 | -4.21709 | -44.22573 | 2025-11-08 04:06:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0db38213-9b34-3539-8155-d65e080b83a4 | -6.34427 | -39.84057 | 2025-11-08 04:06:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6476c3d5-8ea6-3cc2-923f-74f3af13ee91 | -5.93766 | -38.18219 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4060517c-abe5-3e7b-9a09-90cb6e688528 | -4.20655 | -46.39923 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f354ef6b-f422-39d3-a2b0-9a6d7ffbe71e | -6.33848 | -41.69675 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ebdf338-4088-31c7-a664-c23b4c12dd27 | -2.62728 | -50.07492 | 2025-11-08 04:06:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f2a485e-9555-3c90-8cb2-d5a9ce854d90 | -3.31605 | -49.13107 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcb89c5e-c05d-3caf-b157-0085e295f47e | -6.0919 | -41.70751 | 2025-11-08 04:06:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba79e22d-8f1a-3a64-ab79-22cde1deeb46 | -6.1175 | -41.56643 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 972a3621-5e51-358c-af66-4d435c7e7d6e | -3.65412 | -50.26882 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5672028-f029-390b-87de-7018d7063ac3 | -3.54356 | -49.43892 | 2025-11-08 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cc29195-7041-3db4-b770-34f3b5944502 | -3.31819 | -49.13005 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6854f25b-ca65-3047-99e5-3de6116df9d3 | -6.3407 | -41.70419 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fa81169-bbbe-3187-9242-19fe417a5c64 | -3.31554 | -49.13406 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e7cef61-c1c8-3266-8122-53b51760f3d6 | -4.28791 | -45.88761 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8930d62-3445-36f5-9f1a-0cc65dfab9a8 | -5.16029 | -41.22748 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e506169-bce0-3aba-bc26-b23c58ea64ef | -3.91265 | -50.0423 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 81279a47-619e-3de8-a007-4d1019a8a2f8 | -6.65247 | -44.48373 | 2025-11-08 04:06:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b1203f3-5066-345c-853a-7b9622c0e2cc | -2.9881 | -52.81959 | 2025-11-08 04:06:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4b09f34-01d3-3081-885a-d10ecccb99f8 | -4.49923 | -45.13605 | 2025-11-08 04:06:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd9973a7-6055-3399-a111-c91ef9158366 | -4.96766 | -44.34083 | 2025-11-08 04:06:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b01d1b9f-cafa-34a5-9319-109834c8625c | -5.12177 | -40.75592 | 2025-11-08 04:06:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ca395dd2-ceba-3afa-9476-2899a2c68282 | -5.86222 | -44.705 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8c91ae8d-a96b-39ba-b335-022f501b2610 | -5.94585 | -46.65084 | 2025-11-08 04:06:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e90cc031-e9cd-313b-8643-da5924a47ad6 | -6.44012 | -39.62086 | 2025-11-08 04:06:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b7cf30b-9157-3f9c-953d-802dabe30383 | -4.64241 | -47.95257 | 2025-11-08 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 38245e10-3ca8-3d5a-a340-7ff226110889 | -5.74758 | -40.79796 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30fba2bb-a9ef-35a3-bf44-22859a9591fa | -3.84159 | -49.82053 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf49670-0aa3-3931-a8f9-39ca8ef220fc | -4.68732 | -46.40324 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 399a77ea-6a8d-3e0f-955c-71a1d39733c3 | -3.67521 | -50.4485 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8727d10-237d-3fe8-b0bd-d6d73b2ea37d | -2.7062 | -49.54313 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a6bea3e6-56e8-37af-81b5-b545256542fb | -4.63869 | -43.17856 | 2025-11-08 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1465e1a5-6b50-3ea6-9583-7611bf2b0788 | -6.26602 | -43.68134 | 2025-11-08 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a87e441c-7302-3338-a1df-5bfa1a77019f | -3.92031 | -51.00775 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 687c6f6c-80e9-39b3-8e36-33526985a790 | -5.94124 | -38.18273 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3a3c3ab5-f1c7-3479-86b6-6e3fd70ac9ee | -8.03178 | -38.53746 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| a7426f6f-c526-326f-a6b1-11b71dc55ebc | -3.01474 | -49.43959 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71cdca39-449c-38dd-b113-531a99c7feec | -4.20488 | -46.39925 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fbe771c-2128-3ee7-88da-b9488ae34fa6 | -6.46866 | -43.22726 | 2025-11-08 04:06:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec733abc-06a1-32dc-a475-88140159f0d6 | -6.344 | -41.70471 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 250a1dc1-74b7-3fae-aa89-a7661eff9fc0 | -5.22325 | -40.97673 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d2886081-3827-3dc0-a457-a4bbff9846b6 | -3.32375 | -49.12799 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33e83c30-fcc3-3df5-ab4e-4eec76fc4ef9 | -5.0436 | -40.07641 | 2025-11-08 04:06:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0967462d-2af2-369f-a72f-faa6cdf7d631 | -4.46468 | -45.32683 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 11915bc9-9ca5-386f-b70c-81097fcaec61 | -5.77283 | -40.79142 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4718b4d-f7eb-3598-9edc-69fbf00a1907 | -4.45963 | -43.22488 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 116fb4f5-bbb5-36b7-94c4-1d2559051c5e | -6.85421 | -39.11612 | 2025-11-08 04:06:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1445770a-68ed-3eda-afd2-c191f4001c6c | -7.88929 | -38.36729 | 2025-11-08 04:06:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d76c488c-a2da-37a1-92d2-e29cc77f0d9f | -4.46309 | -43.22542 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ec7e671-a468-3d10-a528-1eb5bdd8d06d | -7.43497 | -39.0347 | 2025-11-08 04:06:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b06114ab-4440-3fee-a165-05c4bccf41ee | -4.91377 | -45.91184 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b67e258-88cd-3624-ac3d-15b68aae19e5 | -5.11589 | -45.30866 | 2025-11-08 04:06:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19fcbfae-8ef9-3563-a316-ad0ca92365ad | -4.40821 | -42.32863 | 2025-11-08 04:06:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db6938a2-12d3-348f-9015-996381da989e | -4.90842 | -45.10188 | 2025-11-08 04:06:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbff2eb5-b851-32ee-843c-3f6661f5cdc5 | -4.97731 | -44.81887 | 2025-11-08 04:06:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33983def-5406-3ab8-baf2-7695b6b3ddb1 | -5.15538 | -41.23728 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b993ecc-4201-30f0-87d6-f6cc34c7d547 | -5.41553 | -44.82312 | 2025-11-08 04:06:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d791de41-10a4-3cd7-892e-7a2cde1cfe3c | -3.44122 | -45.58823 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09314611-39bc-34c5-a0fb-f18a497bab3b | -5.77559 | -40.7954 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3ea628e1-a366-3dde-8ad2-00d50e8857f3 | -5.67461 | -40.85382 | 2025-11-08 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b585ac19-e8a2-37cb-a5a2-150860bdc7d1 | -4.9122 | -45.10253 | 2025-11-08 04:06:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff366ea-c64b-36d9-bb5e-0af7fcfe0995 | -3.35256 | -50.21239 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f84c677-37e5-33a3-97f3-fda3967000dd | -5.47523 | -46.11433 | 2025-11-08 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf1c05e-ef72-389d-a508-428c2ec00381 | -3.91208 | -50.04578 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 52c69e0e-c436-31fa-bfae-8f23584abdbb | -5.92489 | -44.11272 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47ebb01d-5323-3d15-9a09-a672d3838531 | -4.22754 | -46.89506 | 2025-11-08 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dde8022-43b6-3bcd-aae5-d7707427919e | -5.39344 | -44.23764 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3ff6d2-3c33-3e59-9255-a7435cecb4fc | -6.10923 | -41.55451 | 2025-11-08 04:06:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 72aa06d6-aebd-3ad6-9fe8-08b3c9675f57 | -3.14613 | -50.29148 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95337684-a3ce-3565-86c9-8ca928c9bd70 | -5.60425 | -37.35896 | 2025-11-08 04:06:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d94f93d2-e156-3ec6-807d-e4bad9c8f04e | -3.84751 | -49.81238 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6f445d-cd76-3af0-8d9a-d761353b35fa | -4.46023 | -43.22106 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 688fc95c-8763-383b-a85d-ee10e08059e4 | -4.22366 | -47.21205 | 2025-11-08 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 216e0bb1-f1b8-3836-8e36-a284c585eb5e | -3.06056 | -48.72512 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad3f6185-9d46-3b68-afbf-9defd37ba89e | -4.29769 | -45.69045 | 2025-11-08 04:06:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80f87796-7e4a-3fcc-87c0-001be17f6dbc | -5.22658 | -38.60598 | 2025-11-08 04:06:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README13.md)
