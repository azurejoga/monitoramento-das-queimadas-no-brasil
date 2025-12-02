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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bafdaa54-f3bd-3abf-8286-dfb414543db3 | -11.1293 | -53.94259 | 2025-12-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| dfd19a38-320d-3f0b-b5e2-0caaf9d2670a | -12.87815 | -52.50647 | 2025-12-02 00:52:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| d09e81b8-b3b0-3be2-8dda-4bb539e5caba | -12.04464 | -54.23914 | 2025-12-02 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3f871310-9357-35ef-87a5-cf2b4afe2f45 | -12.41269 | -52.15219 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ccea3b3e-2ddf-374a-9497-cc7f8b2be183 | -13.03981 | -53.70688 | 2025-12-02 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 27ea59cf-abad-3ebe-a8e4-b861a9ba6c98 | -12.51321 | -56.91393 | 2025-12-02 00:52:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2e088967-4b2e-3876-8542-fe8af9fd2fda | -12.04588 | -54.24813 | 2025-12-02 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 3762133d-320e-3ef1-947c-d36563d372fb | -12.88861 | -52.51463 | 2025-12-02 00:52:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 40fef952-7a05-3b89-93d6-b197988c880e | -11.13815 | -53.9413 | 2025-12-02 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| fbca4549-7ebf-31f8-8af4-bf3130ab9834 | -12.06116 | -52.53006 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 602b41b5-6378-3421-942d-72103b552a62 | -12.50213 | -52.39221 | 2025-12-02 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c467588f-9347-3e56-a791-eccdef42fab4 | -12.85235 | -52.51678 | 2025-12-02 00:52:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 1b2f6b32-f6e4-352d-af20-ee4b471a5937 | -12.88723 | -52.50508 | 2025-12-02 00:52:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 363ac15e-e1f6-302d-acbc-dd251fab90e9 | -12.87954 | -52.51603 | 2025-12-02 00:52:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5be144ef-2f56-3291-92ec-1c79f05f1e71 | -13.04992 | -53.71461 | 2025-12-02 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18017d68-43b5-32d4-b702-a0a0499b348e | -1.35018 | -47.41373 | 2025-12-02 00:54:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b0701fcf-c585-317a-9e5f-c8cf01779ba6 | 2.01247 | -55.71215 | 2025-12-02 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb0a7551-9aff-37ba-8ef8-f412113bee9c | -1.34927 | -53.22777 | 2025-12-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd5ae15a-a3d6-322b-afdd-361717479062 | -3.79815 | -50.60364 | 2025-12-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 83cfb5b2-4092-374a-905b-b289e6679c30 | -0.96423 | -53.7747 | 2025-12-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d31050cb-debc-3fde-8d5f-497d86dd619a | -2.93389 | -49.35106 | 2025-12-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 313d061c-ae78-389f-8702-78347e1d6140 | -2.6946 | -49.31808 | 2025-12-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 896e103a-d703-34bf-a63d-1240cbc4b03a | -3.38212 | -50.00553 | 2025-12-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2779172b-e50e-3f68-ad6d-ee43641df4c8 | -3.15108 | -50.19933 | 2025-12-02 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 830a2630-fbf3-3ab5-9aeb-dbf2cc1afd88 | -2.91382 | -49.38099 | 2025-12-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| cdf9ae83-2751-38b5-8425-c4d2a202091b | -0.9667 | -53.76862 | 2025-12-02 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 59318b24-79cd-33eb-841d-bda461f62695 | -1.19749 | -53.09066 | 2025-12-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 63804f24-c1fb-33f7-ae5e-31d70f5d4450 | -1.93263 | -52.12005 | 2025-12-02 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e6d9c3b0-5e0b-3389-9509-61ac72f75391 | -1.19912 | -53.10234 | 2025-12-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97bd2be8-247d-397f-9c06-8ebbe09a79aa | -0.9885 | -53.2046 | 2025-12-02 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad80604a-d2fd-34cc-a8ce-0005c0434173 | -2.70386 | -49.31085 | 2025-12-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7e263dcb-7368-34ee-8e63-bdaaee8b0eb4 | 2.47836 | -60.72894 | 2025-12-02 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f300655a-006f-3144-a6dd-76bf2cda2226 | -3.46386 | -50.00005 | 2025-12-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 76374109-4683-3712-abab-4dc58eb61205 | -3.38445 | -49.99942 | 2025-12-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| be844a94-58b5-32c1-94dc-e11a1a923b2a | 2.01121 | -55.72131 | 2025-12-02 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9b9077c-34b8-366e-aa1f-c3ff8fd94bd0 | -3.85348 | -47.05636 | 2025-12-02 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 98f61f52-6f22-38cb-9def-9c0bbf3f2290 | -3.85856 | -47.06111 | 2025-12-02 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2bc0ba8a-85b3-3b4a-b21c-540b6d05182e | -3.46138 | -50.00675 | 2025-12-02 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 3fe31cb8-aeb7-3ae2-b192-3b46718d2db6 | -11.1379 | -53.9429 | 2025-12-02 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 89713fab-7eb8-3737-b633-c0ddbd87a909 | -8.1633 | -43.2055 | 2025-12-02 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 78dd6f5c-4439-3e63-a0a7-86cc117b4658 | -17.5335 | -57.2107 | 2025-12-02 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 12bd0ade-0b97-3aef-82dd-fe4ebd21f1f9 | -12.5023 | -56.9038 | 2025-12-02 01:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a7324c7c-e38c-36a1-b59d-2df2cec4e38d | -6.8538 | -42.3237 | 2025-12-02 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 459139c2-545c-31e5-af3d-2a41818e755e | -17.5138 | -57.2131 | 2025-12-02 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 295e786e-5393-30a8-8434-d9f4186b45bc | -12.5213 | -56.9022 | 2025-12-02 01:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 767aa568-c108-3b7c-a658-5cb7723fb69f | -1.4922 | -45.8127 | 2025-12-02 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| fe11fb18-5ad7-3405-b0a6-cff562dd9289 | -11.1382 | -53.9223 | 2025-12-02 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e8e5deea-7c15-3d29-9aa3-a2d6ffa6671b | -11.119 | -53.9446 | 2025-12-02 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b71b588f-2f64-3265-9c90-6ad3e1666767 | -12.5211 | -56.9222 | 2025-12-02 01:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f44e611c-94c1-31ef-8b13-2f6f9316a4c6 | -1.4923 | -45.768 | 2025-12-02 01:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 39e40185-58ba-3856-a464-cfb337f57bc6 | -1.4738 | -45.7684 | 2025-12-02 01:00:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 261bdff4-9393-312a-be84-9800d8941cdd | -1.4737 | -45.7907 | 2025-12-02 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 34811f56-03fa-309a-bfea-8ba7fff9ce22 | -17.5141 | -57.1925 | 2025-12-02 01:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 0c507ff4-9cbb-360a-81c1-2712545101ba | -13.0392 | -53.7107 | 2025-12-02 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 48af9a63-6735-3e43-8af5-28bb3e7d0e59 | -1.3593 | -47.402 | 2025-12-02 01:00:00 | GOES-19 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 97386772-cfd7-3959-a9cb-7cd4edb3a550 | -1.4737 | -45.813 | 2025-12-02 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4b4e3a6a-74be-31f4-b610-e8081990dc0e | -4.389 | -43.1497 | 2025-12-02 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 12e23560-5551-3294-987d-1880481fa8fa | -4.3703 | -43.1508 | 2025-12-02 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ca4cd5b0-daad-352e-a56b-ed2b38af175d | -3.4901 | -43.592 | 2025-12-02 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 78b96b98-d94b-3e43-9132-a34140d68d34 | -10.145 | -36.1406 | 2025-12-02 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| 9d32c9ac-a415-36b4-9597-be1f7c69365f | -1.4923 | -45.7903 | 2025-12-02 01:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 7bd9eebd-553e-3b85-8d8a-e4525c943e9e | -12.885 | -52.5172 | 2025-12-02 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0f9b56d7-f746-377f-97d4-b6ae7025ce07 | -12.8853 | -52.4962 | 2025-12-02 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ac18af06-3c85-317c-86b3-2defb9a661b7 | -0.9624 | -53.765099 | 2025-12-02 01:05:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e40929bc-0d2b-3a36-8454-97f7d94f500e | -11.1193 | -53.9241 | 2025-12-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9cdb448a-5b57-37d0-b121-1819780353a2 | -3.0172 | -45.0748 | 2025-12-02 01:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 7655a173-4754-3e00-b8bd-65336906070b | -1.4922 | -45.8127 | 2025-12-02 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a2467116-f02d-31d6-b461-cf83d6d2770e | -11.1379 | -53.9429 | 2025-12-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 73433b4e-4ff3-356b-b941-e0adafd928ba | -1.4737 | -45.813 | 2025-12-02 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| af96d647-5c9f-3929-9d35-b8da6c552aa8 | -8.0516 | -43.0765 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 559c8ceb-6278-33c9-ae8e-893c7ead1f33 | -8.0706 | -43.0745 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 1ada1aad-944f-3c86-b7a4-04321b03339d | -1.4737 | -45.7907 | 2025-12-02 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 2ea44a1f-203b-3a25-9ab6-236f135808fd | -8.051 | -43.1237 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 48696164-a6a8-3c46-9a5e-786e74ccebdc | -4.389 | -43.1497 | 2025-12-02 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bcf790b8-9d2c-360d-ad9d-33f543b57f62 | -11.1382 | -53.9223 | 2025-12-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 22b60acc-f882-3041-b6ad-8d27355b1980 | -12.5211 | -56.9222 | 2025-12-02 01:10:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 69d023b1-5d65-3e5a-99e3-fbaca9a75d4a | -3.0173 | -45.0522 | 2025-12-02 01:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d603cefa-df2d-32d4-8483-a8cbdf1baf7f | -3.4901 | -43.592 | 2025-12-02 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 19780a38-6488-3a58-9af9-71cb90c65df9 | -4.3703 | -43.1508 | 2025-12-02 01:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 7b44ad17-c1b6-365d-8e6c-858309a0faad | -11.119 | -53.9446 | 2025-12-02 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 73b687e5-dd28-3200-b172-822c52e5ca66 | -12.5213 | -56.9022 | 2025-12-02 01:10:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 24e019df-378f-3329-afcf-d63b5348dd32 | -17.5335 | -57.2107 | 2025-12-02 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| c3f04cd8-5fd2-3c4b-8134-c1d1c2889c46 | -8.0513 | -43.1001 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 388.7 |
| 24d3381f-1685-3b9f-a32a-6d4c6aed5a11 | -3.0358 | -45.0741 | 2025-12-02 01:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1ead000f-0f12-38c6-a275-8ea94fd3be1b | -8.0703 | -43.0981 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.3 |
| c1c3db60-8e2d-3b55-b726-5bc63874b998 | -12.885 | -52.5172 | 2025-12-02 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 32e8c31c-0c59-39d3-835e-3c5e904db696 | -8.0324 | -43.1022 | 2025-12-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| c6651d5d-da7f-30f2-9a33-798ca1f19b88 | -3.4903 | -43.5689 | 2025-12-02 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4f0a70ec-e24f-3f49-a89d-f832558d68cb | -17.5141 | -57.1925 | 2025-12-02 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| dbe6719c-6b48-300a-ade7-c3190c1cf961 | -17.5138 | -57.2131 | 2025-12-02 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| f8af4d3d-35f7-3af7-9695-7c7a66e97478 | -1.4923 | -45.7903 | 2025-12-02 01:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 29732fb3-38ec-3da8-8f1a-1743fbf9f7ea | -11.119 | -53.9446 | 2025-12-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| eae04062-6b35-31cc-9eb3-b475d8f5b7a4 | -4.3703 | -43.1508 | 2025-12-02 01:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a611dc92-edd5-3836-8695-0d9fa5ba2fa5 | -8.051 | -43.1237 | 2025-12-02 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 5e357bc5-a54e-3996-b96a-c5c33c8bc663 | -12.5211 | -56.9222 | 2025-12-02 01:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 173eb312-16a5-3d01-891c-59d820893d1d | -8.0516 | -43.0765 | 2025-12-02 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| a5a02883-f586-3440-90cf-0df399205900 | -11.1382 | -53.9223 | 2025-12-02 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| aa810bc7-385a-3d25-9191-71f97d9af8d5 | -1.4923 | -45.7903 | 2025-12-02 01:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ee85227d-8786-33c6-aa62-fd03bee679b2 | -8.0703 | -43.0981 | 2025-12-02 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 9bd5a6a3-7fa6-387d-b12d-aec0459f2a5c | -8.0324 | -43.1022 | 2025-12-02 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |


[Clique aqui para ver as próximas entradas](README4.md)
