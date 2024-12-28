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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38b9e05e-20cb-3941-87dd-c185cecd681a | -2.21542 | -53.65047 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cfb25815-d5fc-3573-ae22-838f8dd45a8b | -2.52116 | -51.85897 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12213465-49a7-3956-b09e-e55cd933e6ad | -3.86705 | -47.01461 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e543d4f-e88b-3fe9-828d-b683e992990a | -3.74647 | -47.20526 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76cc4b8c-d1f4-340a-8115-36bbf686e4e8 | -3.98256 | -46.9202 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a26aeb9f-b4b5-3049-9ee6-4f5afbe23c4c | -4.1281 | -46.68098 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2e40013-9012-363e-9b05-d828fee81710 | -3.91901 | -46.65815 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1def3238-2e1c-30e5-b495-07e7acf661ee | -3.94563 | -49.44599 | 2024-12-28 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3074a9f1-bf6b-35c0-9552-53466801871d | -4.01143 | -46.91695 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6391a344-5f48-306c-b462-4d252a9c8976 | -3.9693 | -46.89141 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4418960c-127e-37e0-978c-174a1c264efd | -4.25898 | -46.41537 | 2024-12-28 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b90746a7-ab07-3a7b-8bde-dde4f5829f9f | -3.9018 | -46.98497 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5350597b-5991-3f1b-96b4-6096d2a9d121 | -3.85548 | -46.67591 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc8d949-8a82-3bc2-80af-98781bd95d1d | -5.57595 | -46.13142 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 26811257-51b3-351b-a5e5-7abd9b33a610 | -5.42643 | -44.83395 | 2024-12-28 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28fda7a8-96ef-3ab8-a439-240344b4846a | -3.89269 | -46.68951 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396e7c65-222f-38f7-a5b3-27081b9055e9 | -3.80477 | -46.85586 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0b67c03-9f08-3361-973d-6b15af7a585d | -3.9889 | -46.92503 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18888ca6-2932-3068-9d98-7da1c6e23415 | -3.77021 | -47.20847 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 454e4001-b103-3310-b406-3dfcc4032f13 | -4.05253 | -47.03096 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aaedca5-c86f-3655-a040-804ffae63124 | -4.23497 | -46.80264 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75e1cbe5-a44f-3321-a22c-0c2a0aac5ae6 | -3.19181 | -45.99591 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e2aeab7-dfaa-3c9a-b3d4-5b473364d6f1 | -3.958 | -47.97074 | 2024-12-28 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69882ced-c7c1-3d4a-b1fb-c648393603b3 | -3.92081 | -46.88375 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0170617-7722-3388-a181-997de356b7a1 | -3.90468 | -46.93227 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 118f59cd-4cc0-31fc-b52e-09fdf55bcbc6 | -3.87982 | -46.95538 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c778802-cf7c-3750-b0f9-e74c10258cf3 | -4.04355 | -46.71175 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a4b0f4a-fb5c-3e33-9693-e449d70a8422 | -3.23908 | -45.97419 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04c0ee4-556c-3610-9141-03ca61784a5d | -3.88446 | -46.94834 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2679b332-5998-3826-a108-306563dff2b4 | -5.93335 | -45.57191 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47b65c3d-2251-39d0-9451-b780e2e32a83 | -3.74478 | -47.1937 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3027f7f-a724-36b8-a2b8-1945f912ac96 | -3.77485 | -46.82013 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8063f7b-b7d5-3225-b396-4d7bd3337a03 | -3.99502 | -46.58551 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92f0a7e9-2bce-3940-93d3-53cdc22e57bc | -3.97592 | -46.33849 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f65b7e8d-9678-32dd-a482-7fe29e6157f2 | -2.28528 | -45.5924 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99577b3a-da02-36d5-a8b3-a2a724b6a01b | -3.99005 | -46.68781 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 927d2dab-75c8-3f02-9dd1-1a8788adfc84 | -3.8918 | -46.99184 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c187236b-efd3-3dfc-bba5-4b1e3260e0b5 | -5.57533 | -46.13552 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6319f03-9a0e-3175-83d0-b2ad3ca403cf | -3.96329 | -46.67571 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0150330-362b-374c-b3ea-331861e18309 | -3.92655 | -46.98483 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7768a18-6cc3-33f9-a89f-4d1ce8178763 | -4.08582 | -46.81569 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d59e98d4-d7aa-3d8b-bd1c-3704f371fe8e | -4.00343 | -46.69378 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eb0a8e9-555d-35ed-9153-3d6485a8baaa | -4.53524 | -45.56593 | 2024-12-28 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7286f582-df9a-3958-86df-246712e0d9d4 | -2.22063 | -53.64402 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c947ce-eb6a-339d-885d-6643c86817b4 | -4.01975 | -46.1976 | 2024-12-28 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 735a9fbf-6e25-3981-9b0e-74cc60349ee7 | -3.75997 | -47.22948 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b304e268-044a-31be-94b4-8eb1b9dafb80 | -3.9083 | -46.88653 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38ca00ed-3cc1-33a6-880b-223d003ce02a | -3.73851 | -47.18897 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98019115-9d66-38e0-ba5a-ed1cbf54a76e | -3.91225 | -46.90655 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dddb2a4d-efd8-3d10-b783-288892a001cf | -4.07542 | -47.08806 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| cb137290-d751-3480-a98c-92adc7015989 | -3.79136 | -46.7138 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a11a8914-1e16-3402-a616-726a78603472 | -3.90242 | -47.027 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6bd9c24-bd1e-3b7e-b08e-6e497225d7cc | -5.64097 | -43.7157 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68982439-6ec8-35e3-9991-532db2ff806c | -3.91793 | -46.87941 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0fcd9f2-b030-3936-9c10-f468b1bd3690 | -4.01851 | -46.71185 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f851bea9-2099-36d1-872f-f46ed8cd1dda | -4.49997 | -44.23204 | 2024-12-28 04:38:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afac59e3-333b-35fc-902b-6af7071be3fc | -4.03777 | -46.70299 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ecb9d00-082d-3ba0-bbb3-a298afca5de5 | -2.16747 | -54.42654 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57c34bb4-11e1-32dd-ae92-9e8383047704 | -3.19287 | -46.0016 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33f5293a-cc40-33bf-b2ae-d1152b999663 | -3.73109 | -47.19159 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abe21a70-6ae1-30e8-8c41-661af23cafa4 | -3.97176 | -46.3419 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 669555a8-27ff-3da9-8251-e0314eb49e79 | -4.00095 | -46.93861 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d78742-5b12-3484-85bc-90653f8478cc | -2.28788 | -45.56888 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4143f3e6-be06-3e53-a7fe-2bcb67858a37 | -3.99123 | -46.91002 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e1d452-86b0-3f38-91c1-0bd5de1f19e2 | -1.34802 | -53.52363 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ef36484-a6d2-3c10-9f10-3b5311dc5543 | -5.48375 | -46.4416 | 2024-12-28 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d88327a-a041-3df0-af7e-0aa351483ee5 | -3.9726 | -46.68502 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 595066ad-f8f2-3f29-ac7c-97669153eecc | -6.44832 | -44.38755 | 2024-12-28 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89db5228-0636-349f-a5af-c46b4299cadc | -1.12337 | -54.13216 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3f45af7-2de3-3d47-8366-d4c5c936c26e | -2.73782 | -46.86871 | 2024-12-28 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74800e2f-faa5-310e-8e0d-842e115a0ac1 | -4.01618 | -46.19702 | 2024-12-28 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 469738de-1ae3-3aba-bcb1-ec4c4a05e49a | -3.82253 | -46.62827 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb2b4894-f41e-3f5e-9a88-cf7dbcd8bca0 | -1.35209 | -53.52435 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e8d998d-df03-316a-898e-d6079ab70aa0 | -3.8186 | -46.72211 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7527e89-745c-319d-9761-730973caadf2 | -4.00046 | -46.71301 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9d692c-eb57-3169-a057-2a6122c68093 | -2.51754 | -51.85838 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2029529-ec63-3680-bfad-d0d82857e1d4 | -3.18885 | -45.99131 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd89254-f9ac-3a42-9413-8ed0940166e6 | -3.89578 | -47.01148 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5903301-49cb-33e0-9a68-48c9eb61f67b | -3.92427 | -46.88431 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e712225e-a9e7-37a6-9c33-016f2c7fd797 | -3.99578 | -46.72015 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d53953-f053-3ad2-a9ec-89c09510f1a0 | -3.90123 | -46.98871 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b465b7e-7d92-3658-a52e-79012b124a50 | -3.80884 | -46.85257 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a290ecb-bb72-3dc8-be1c-424c8207db33 | -2.39325 | -51.9134 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273a56f5-79ba-3bba-b90b-42b3e0f598d0 | -4.10092 | -46.81016 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd5add79-9b87-3cdd-b52f-bcae266aca62 | -3.93894 | -46.7592 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 537d8ba5-4408-3b8b-86dc-a2c53fdbae80 | -3.90813 | -46.93282 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b89f584-827c-3135-bfeb-89fd5850af1e | -3.44161 | -53.29698 | 2024-12-28 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d649bb8c-9010-3654-9634-23e1b36e2120 | -4.1015 | -46.8064 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b7c9fd2-1eb8-30a7-a3c8-b5a53f9043d9 | -3.97609 | -46.68558 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebd18a0f-a75d-3534-9a96-9d34890be5f1 | -4.0864 | -46.81191 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c91b4b-4c85-3ace-a014-6b105c856acc | -3.74136 | -47.19317 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbc0a550-2467-3016-bc4e-fa9a79860317 | -3.53284 | -53.79812 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e57818df-ce1a-38bd-ae24-bd8e322b8525 | -3.88428 | -47.01731 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2dfb030-a400-3380-b5bf-70289ee86893 | -5.94452 | -44.10061 | 2024-12-28 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6f5ab2b-7e01-3a5e-95de-8901c51a42e2 | -3.84614 | -46.69026 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c94e0962-124d-3969-9b1f-f9fbef1d76de | -3.73966 | -47.18163 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1db84994-1c09-345c-9e4e-26c47dc5256b | -4.12112 | -46.35065 | 2024-12-28 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea1c276a-efb1-3d74-8a6d-aefa8e261c98 | -3.98886 | -46.69554 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 016fe102-9e85-324e-87a2-27b64d34f0d1 | -3.88387 | -46.95214 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0f90895-2d98-3de2-892d-193a1bbe3774 | -3.89465 | -46.99617 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README18.md)
