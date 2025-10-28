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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb4e789e-dce0-3c1f-9c5c-4d0c89b6cc5f | -7.06892 | -47.36396 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b958ebb4-e734-360e-97b8-86af811cdccd | -7.96492 | -46.75212 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32cac8c3-1f43-36dd-ae25-e4fc6aa0c07b | -7.83815 | -46.40792 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8301c6e-8bf4-3cb0-a660-e9dd4e43ccda | -7.92618 | -45.69275 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 318312a6-b300-35f4-85c0-1904db1ea7ff | -4.63763 | -48.69851 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa5fade-b624-3ec7-9b90-606dbc9f386e | -3.60104 | -47.51604 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebb1cb24-3981-3370-81c6-32caad0c71a1 | -7.45475 | -49.41199 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5773c23d-3126-3d67-8e96-204c68bd70b5 | -3.57156 | -51.33264 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c245ff2d-f0b5-3aba-a130-feac8a3f887f | -6.6223 | -44.62476 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e6f3cd2-52b4-3344-84c9-67bf31596fea | -7.00271 | -46.99858 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f413ebb7-d6e5-37ec-9431-89453fff69cb | -7.23466 | -44.99505 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91305e41-fd39-3281-8a86-1e8fef595b6c | -4.43688 | -45.97872 | 2025-10-28 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f263adda-2c51-311a-89ff-6a424ce0b824 | -7.35613 | -47.63868 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9aecab65-d081-3031-91bd-284f32025de0 | -3.38292 | -50.15265 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c7761e3-67d7-3c2c-93c7-0b113700a492 | -4.887 | -45.74036 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6ce9486-65f4-37f0-9053-f395a0f5efe9 | -3.46838 | -49.96849 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b118d7c-2755-3443-b27e-7fe62842fc7e | -4.3457 | -41.82613 | 2025-10-28 04:42:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 081242ed-f281-3b90-a923-f883e3c7d7f1 | -3.70539 | -47.65274 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d7f35bf-6f1a-317a-b6c2-048574402229 | -3.13765 | -52.99754 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed95bd3-5c42-38a6-9f67-ae71689dcc93 | -3.44211 | -50.22038 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6819b1d9-1098-3a8c-b773-bcfa812f7fcc | -3.08448 | -51.28715 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54711335-b60a-31ca-875b-4d735c878236 | -4.95406 | -43.6988 | 2025-10-28 04:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c8136af-aafd-3da0-bde0-d8fc6e3e2d67 | -5.49103 | -47.7487 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2a8fdba-c814-3f08-8c9f-809ebcc0785b | -4.34418 | -41.8241 | 2025-10-28 04:42:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ae6ba1f5-6b55-315e-afb3-e97d8f270cae | -5.47143 | -50.16113 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda4174b-e4d1-37f8-87b8-82b9cec7947b | -2.45048 | -48.62025 | 2025-10-28 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cc880dd-dd27-3bd2-b38b-0d4b4d797d7f | -5.58321 | -45.34219 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ebebf68-e642-31f0-9114-c9ea93ef8604 | -2.74799 | -45.40897 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe341510-a2e9-34bb-bbe5-32aa9e4f1be7 | -6.58924 | -42.69103 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a11a5bd1-db12-30ec-88fe-5388aeb2b603 | -5.65453 | -41.14852 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 834e0bc6-db3d-32e8-bb26-bf1901a362b2 | -4.25785 | -53.54487 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4105b9a-cf69-3981-9f08-f0ab003ff287 | -7.45353 | -47.15929 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff2a3ee2-fdbb-3167-9838-6bfeb0d060b3 | -3.14071 | -50.16218 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e0aa757-1f93-3a81-9c80-a4bc959247b6 | -7.53497 | -46.764 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d606317-41f4-3a4e-8ead-1c8eb8a71869 | -7.86587 | -46.39868 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6789b19f-d6cb-34ae-a11e-f0ea282da69a | -6.99917 | -46.99806 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00bbabb0-1a94-324f-a2c2-1b3ac79eb6fd | -2.91805 | -48.72558 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d77d00bb-1189-359c-8ccb-065f642444d1 | -7.89929 | -45.68937 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 004dc9ec-0e73-3b24-9e84-d7d3e2c27da1 | -7.89547 | -45.68871 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ffebb6d-6e76-3179-86d0-df5d64572397 | -5.57942 | -45.34161 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 156a0bb8-6123-3857-b4ab-5a25e17322f9 | -6.84621 | -50.11766 | 2025-10-28 04:42:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a7453a6-3a30-3b00-b194-4107d76b80ba | -6.08666 | -47.00596 | 2025-10-28 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 380a4524-6cfe-3222-82ca-001aadbd1bd4 | -5.61645 | -51.78859 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3110a83-4309-3a45-aea1-4a14b8cf3db6 | -4.90675 | -47.42107 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07b40253-00a4-3b67-acd6-2e1ac890f7f9 | -3.57963 | -43.61597 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a33baf6f-05fd-336a-bc4f-c2dc17c6e7eb | -6.06572 | -49.82896 | 2025-10-28 04:42:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf342317-ce0d-35cc-8ebb-acb69a4cbc1e | -3.53196 | -50.31556 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72bd60a7-0921-350e-9d53-7ea6047ecb56 | -3.58562 | -43.63189 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 562fe5b7-82c2-3af1-9d57-23e4cf8954fb | -4.7271 | -43.19658 | 2025-10-28 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62f70832-f81d-3e84-98ed-d4f21f3217ff | -7.79076 | -46.4488 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 054cb8e5-3299-345a-8182-db383d6f9983 | -5.73392 | -45.26298 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82dd4d72-f20b-342e-9e12-17e9e1161b48 | -2.89381 | -52.58833 | 2025-10-28 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff902cba-1c3c-393c-a1aa-0057906da782 | -8.16089 | -47.00712 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b083d280-5c85-390c-8949-7a1b76ff705a | -3.75315 | -51.7541 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f45115a2-ca70-3152-a024-9e909c287c03 | -2.5824 | -48.40459 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b1b16e-9adb-3fc7-8fb3-e4d0953e3cc1 | -7.45584 | -49.40502 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c2ede94-5ab9-3c22-82d1-c3c4c40b6cf1 | -7.12913 | -47.01678 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c5e03f1-3430-33ec-a4e3-2d5199ad68fb | -7.2976 | -45.06127 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d4bcfff-032d-3eb1-b5ff-d3f4d5929eaf | -4.9675 | -47.5915 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23df0a10-92ea-3ed1-8d4a-ce2d42903719 | -2.76022 | -45.40226 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4190c5e7-34d5-3e32-99ff-3279288b759e | -7.49393 | -47.03559 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac6e621f-94d7-3024-a050-d79e8247c6f6 | -4.3076 | -48.06442 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f8f192d-ee60-3274-9bcf-9634cb242a72 | -6.62181 | -44.62817 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4035ef65-5ad4-3c58-82c2-b1346ef33fe4 | -4.45737 | -43.64679 | 2025-10-28 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6cbe3aab-d9a3-3bd7-aefa-7ad2cdd60119 | -4.50685 | -42.84293 | 2025-10-28 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6e787d7-0b84-3aa0-b946-97a9303ac097 | -8.05181 | -45.15791 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 432521a4-dda7-3b61-94d2-5c9a564ad580 | -3.38686 | -50.14959 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92259c86-6638-3e75-b84e-2faef9cee547 | -7.6124 | -46.47247 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1cbf192f-38a9-32fa-a50a-194c4f6396f8 | -5.30303 | -47.02147 | 2025-10-28 04:42:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e16ab3d-c6a4-3899-aebf-dce0dc57e1ea | -3.23813 | -48.77604 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 933ad212-fa5e-31ee-bfb8-713264682c75 | -2.75228 | -45.40533 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b51b5b-23d2-33c3-b641-5a94b8f69ba3 | -6.61776 | -44.62774 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fd85d1c-75aa-380c-b5f1-ac11c4daa7f1 | -7.86651 | -46.39447 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4e94f9d-a3f0-3ab7-8e0b-8723461383fa | -5.49046 | -47.75232 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b6d2fdc-fb17-34ed-9dc7-74c7b75a8118 | -3.13689 | -53.0023 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd494a5c-bec4-3463-ae95-c8d6c686038e | -7.98691 | -45.9557 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14faff34-007b-393d-ae30-575be2c0806d | -3.25134 | -52.91111 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33541a9e-9b6b-39f1-b8f1-4c89ad25234a | -5.43795 | -47.39534 | 2025-10-28 04:42:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13290946-8e2b-3562-aa27-88005c50914b | -8.15141 | -46.99716 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5775a950-f065-33dc-9351-7d05bd043454 | -6.95937 | -46.23633 | 2025-10-28 04:42:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 086d7e3d-2563-38b1-b171-f4aacd700653 | -6.89297 | -44.90345 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 339ca9e3-4b6b-3278-8836-89a61e446398 | -7.83514 | -46.40303 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05299b6b-fd6c-345c-9fc3-d8b94f805633 | -2.97784 | -51.3428 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a9afdd-2b12-38c0-8467-72a4c49ece17 | -7.88576 | -45.70164 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c23abada-29fe-3739-9e85-a7f07fb4ef1e | -5.65645 | -46.4546 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10d904b1-6a24-30c8-9a33-cbb75da28a7b | -3.86405 | -43.35686 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f5d840c-635e-31bf-9634-2bd4e5df3eea | -7.94643 | -45.52948 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0d83aa2c-ad38-3677-b36e-db28779d6cb9 | -2.91027 | -49.81578 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcaf121c-c9d5-3983-a04b-85c04e140ef0 | -7.67673 | -47.42004 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1090f70-dc1e-3d2b-8031-823dd279186c | -2.86398 | -44.38188 | 2025-10-28 04:42:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52056b87-f99b-32ea-8d4b-9296658135c0 | -7.82308 | -45.39043 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3864361d-f275-3b7f-824e-980b5e099750 | -7.16044 | -47.00111 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d803df7-e315-3aec-84e6-47c30f226be0 | -7.98427 | -46.74639 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3e273cd-bbb3-37c8-9be8-509384955787 | -3.70312 | -47.64515 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf93e2ee-daa8-35f4-902a-2aeb98b4fd07 | -7.09612 | -47.26023 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6ce6c2e-9b49-37d3-8d0a-390509bba27d | -6.89076 | -44.90065 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04008559-191f-3292-8219-8821ecc1493b | -4.68488 | -48.26677 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2cc6d5a-1e36-3085-aab6-efa203070350 | -7.45552 | -47.02558 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fabf6f8-acfc-37a3-bea6-779b99d70415 | -7.8518 | -46.39227 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e18d041f-0864-39e1-883f-c7236f84643c | -4.45791 | -43.23702 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |


[Clique aqui para ver as próximas entradas](README51.md)
