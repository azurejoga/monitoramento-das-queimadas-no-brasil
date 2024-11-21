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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3373e540-c18b-3480-baf3-b1292cd09dc8 | -5.01253 | -41.95728 | 2024-11-21 04:31:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6537a706-00c3-32a1-bf66-f1a67a09a740 | -3.84817 | -50.99673 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5ba2dd-7183-3ca0-a3b8-d8902b4fbd4a | -3.29749 | -53.85611 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77c62682-ccad-3314-a4ff-f9efa53b8fa8 | -3.72949 | -51.16437 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aef852d-63bf-3b23-9ba6-7e2e5eee551a | -4.49148 | -47.10523 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef6b7511-ab4c-301f-865a-d787f04b1265 | -4.42812 | -48.29565 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2a07d87-17e4-3a7e-bb03-e50c6c1fa440 | -10.69986 | -48.80639 | 2024-11-21 04:31:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6062e7a0-bbea-3e7e-8703-5b56f2b76032 | -4.38228 | -47.77537 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29c51e07-2084-31e9-a511-78eb878ae04b | -3.8468 | -50.69534 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55900974-95d1-3002-b102-93b8e95899de | -6.63962 | -47.34663 | 2024-11-21 04:31:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25eb438f-6e6f-371c-937d-71cc22baa004 | -5.17223 | -52.00083 | 2024-11-21 04:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc13b50-6ad4-36b6-86fe-703b6119cce5 | -5.95039 | -44.46807 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8c08d15-720c-38e8-8a47-d34a20bcd444 | -5.6635 | -47.33567 | 2024-11-21 04:31:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62554c2e-5803-3506-b272-9fa56282d1e5 | -3.76244 | -52.40821 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e862542a-37ae-38d9-b30a-5124ceb0a4a7 | -3.56537 | -51.4945 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a4e97f6-b69b-39d0-8c0a-97ebfb5ad6f3 | -3.75832 | -52.40757 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fd4ebf16-426a-3199-84e7-e06ff9918cf1 | -6.63629 | -47.34611 | 2024-11-21 04:31:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e02e45-065e-352f-b431-ef81bbd8be85 | -5.65519 | -45.1975 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38968690-b248-3529-8c93-f91381cfccac | -6.2997 | -45.33987 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff3d85b9-dfea-3e9f-8cb7-e80f3d7746a7 | -5.63904 | -45.98895 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a5dffb9-9476-3328-963a-58cbb07614b2 | -3.81442 | -52.34854 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b33ef7fd-a8e4-31c7-b98d-4070a0878b29 | -6.21683 | -46.222 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0bbc300-b290-3c99-954a-965edb330c22 | -3.51229 | -53.79882 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d2164a7-021e-3b46-a917-187295662f46 | -4.88587 | -50.93978 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa12a812-e198-328f-bed9-18fa90cab712 | -11.22599 | -45.57476 | 2024-11-21 04:31:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a5a80b-71d6-3b04-be11-936d3d2f244d | -3.55459 | -51.51081 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e9d357e-6009-3433-82f4-716c708f97df | -4.55564 | -48.00992 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1002176c-ba4b-331d-88b1-629a5d819f89 | -4.19493 | -53.49117 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ff85e47-a125-3996-841b-8bae119c252c | -5.30066 | -50.56968 | 2024-11-21 04:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcf05d1c-d5c8-3c86-b88b-91d41d6ff83f | -5.82607 | -44.10786 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e78cade6-7f32-39e8-a94c-3c072ec06b8f | -3.05208 | -54.41246 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d935d78b-f297-3cba-8ef3-26efb3c13674 | -3.6433 | -52.35915 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f23198-ed38-3170-89a3-fb20a96451ad | -6.95007 | -47.84744 | 2024-11-21 04:31:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e167e901-ded6-320f-b4d4-fcc8faf040ab | -4.5838 | -48.02156 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 00123107-7fc0-3d4f-8651-afe18994f94d | -3.11286 | -53.75217 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6cb2b30-73d6-304c-9ad1-5ab896eee51c | -3.86428 | -51.96596 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 61811f00-62cf-3a19-9f1c-4f4844751f64 | -4.63612 | -49.54431 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 904eed3b-1674-3ab8-bbaf-a2e1c2f8c542 | -3.2803 | -53.84061 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c95b1460-0e02-32c5-bef4-b0aa4bc7a9d8 | -5.8786 | -43.88269 | 2024-11-21 04:31:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43a4363-4511-302e-be5e-d3e70f41c29c | -3.86406 | -52.32742 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be1bcbce-f29a-36fc-8be9-b34c0484c560 | -3.28644 | -53.83204 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 898e6c22-6295-3c92-a036-d87be6c666fa | -3.51719 | -53.79664 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ffc3ce6-3d3c-3290-a6df-018401b13730 | -6.61617 | -42.38348 | 2024-11-21 04:31:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 719dba74-abca-32ed-94c9-859e1e50ab9f | -3.34094 | -54.07501 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1dcb4e90-b0f0-30dd-9e4a-9eab861e6030 | -3.2833 | -53.85065 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb24ec41-e4dd-34f9-9747-63445b404ba6 | -3.82964 | -52.25495 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4223523-d703-3a15-abce-15d2c70fb09a | -5.12065 | -46.17899 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677b27c0-b649-30b3-b17b-a4399c45d66e | -3.41849 | -53.2888 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b15ddabc-37d5-342e-b005-06e05fc57663 | -3.75115 | -52.32401 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c7474a-5d2f-36bd-99f7-8f13b55295b5 | -5.73629 | -46.19648 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a1b6299-eab3-3449-93e0-58525d9087e8 | -3.68184 | -52.3459 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab75ac6-2c60-3645-8ae9-167d6dcd00c8 | -4.9499 | -47.80442 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e54b767f-6ee2-31e3-89fa-875bbc107338 | -3.52071 | -54.17478 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 035427e0-ae67-311c-ac3d-ae48a0ea22f4 | -5.89648 | -46.64692 | 2024-11-21 04:31:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffbf63d1-f232-386f-a8fd-3f5248179185 | -3.53879 | -51.60627 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b49d3cbd-b366-3fc8-8681-730ef4bb48fc | -3.64332 | -51.4571 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af865b8d-f840-3cab-ba0e-7bba71e00636 | -5.18514 | -46.17051 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 222a7793-7771-3c04-8805-da38f7ed4a6d | -3.68623 | -50.21476 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 297bcc19-20a7-3866-8d3a-468846de60bb | -4.81936 | -45.75763 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a434fb-2e16-35c2-8f1b-2051f7c23efe | -5.8176 | -43.79774 | 2024-11-21 04:31:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61a58b46-7ab6-3537-96e9-635f50747a2c | -6.37116 | -46.48761 | 2024-11-21 04:31:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5e1d03a-4c1e-3682-991f-0a5661de017c | -3.817 | -51.35119 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa11b08e-de63-34aa-b7f7-6c2384a50e7d | -4.38504 | -47.75801 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca013b24-c11f-3185-82e6-140ddd7cef7d | -6.21345 | -46.22146 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7d649d7-89e1-3a1c-a10c-c0f5040972a4 | -4.63192 | -49.54054 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11092c2f-c68c-3f69-b6f4-b2c6e09c58cc | -5.29705 | -50.5691 | 2024-11-21 04:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6233d582-5a0d-3987-9ccd-5b2798d76053 | -5.948 | -44.23879 | 2024-11-21 04:31:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27cff8df-0c24-3908-9c81-0b2077aa3a32 | -4.36609 | -46.09282 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f49725a-5813-321b-803a-e6f57b6aeaa1 | -5.50825 | -46.493 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47b73691-16fb-3917-afb1-2cc334f3fb42 | -6.19943 | -44.37403 | 2024-11-21 04:31:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cea498c5-4398-3153-9e9e-10eb3d300d0b | -4.75163 | -44.3432 | 2024-11-21 04:31:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27117bd9-bbb7-375a-8537-b09f2074afbc | -4.41133 | -45.9575 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a5937e-7e4c-3b57-b75f-ee7b51a7ac93 | -3.74806 | -52.32702 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afd3bd71-c8d2-3e19-9ded-6a5f50ccce62 | -3.29626 | -53.85749 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd607147-3907-3f19-b908-210d79567e4f | -3.19771 | -54.32863 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6096bd20-23e5-3d2d-be24-5b392dfe6035 | -4.34214 | -46.13622 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0cb1907-543c-3d12-a92f-52946575be6b | -3.50666 | -53.80408 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f22fd3b9-8732-3192-931e-d733a9b350c8 | -3.11596 | -53.70543 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cfc1e85-8775-3ad9-9e42-eb952135bf8e | -4.61533 | -46.46622 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 123f8565-2635-36d8-9827-ef5488ddf5e9 | -4.81992 | -45.75401 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9bcc870-5506-35b9-9012-79f82beacb7a | -4.58269 | -48.02856 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acb3d034-38eb-3fa4-9032-960755111692 | -5.56417 | -49.38401 | 2024-11-21 04:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98b1b577-6be9-3fc9-8b0f-1e6777d07f97 | -3.18903 | -54.32211 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3162f689-e71d-3e26-b6b7-4c69ec22d17a | -5.54436 | -47.85989 | 2024-11-21 04:31:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a90ea9f-02a2-338e-8044-9debc6dd4e2c | -4.15766 | -50.22561 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9cbca19-c60c-327f-bfbf-80d2317a33bd | -4.68116 | -49.03109 | 2024-11-21 04:31:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac1e1af6-e1dd-3f32-b6e3-26b95e466a4f | -3.29674 | -53.86079 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 526c6a74-67e1-3680-8d3a-2b1914e3f9d1 | -3.51678 | -53.79983 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cebddcd1-53c2-3e40-9ee4-896f713dcbed | -3.22796 | -53.61694 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 476124fd-5751-3826-a1eb-46369b7e9a21 | -3.55515 | -51.50786 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 328a296b-278d-3ebc-b136-bd6277080bef | -3.10451 | -53.74607 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22812dd7-a927-3a69-8103-87958ba995c4 | -4.39497 | -45.59272 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e063d0b-9547-3cdb-afbb-5194a2879eab | -4.98473 | -48.75146 | 2024-11-21 04:31:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cd1139f-a130-3eff-8ad8-dbedc27ec66e | -5.44336 | -45.5845 | 2024-11-21 04:31:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddf3d88a-3ece-3936-9cab-88ee33924a90 | -4.63952 | -46.35498 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7a34e41-c65b-3120-b6fe-8c497db4c6b4 | -5.11983 | -44.1003 | 2024-11-21 04:31:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a80ae542-42fd-34c3-b701-f60d2ddb0d17 | -4.04611 | -50.34037 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3815329a-d2f5-39ae-a67e-df12e9a0cb20 | -3.86348 | -52.33107 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0376e927-7452-31f7-8203-134d2a570abf | -6.82273 | -46.77524 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14d2607b-73dc-3878-abc8-a627988f7c58 | -5.17788 | -50.63638 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README44.md)
