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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56920bab-43a4-3a87-93ab-d03f8453bd24 | -3.81416 | -47.49849 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08c87bf-d2d8-302f-a71a-1f8a6d61a74d | -3.33323 | -50.27852 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 042dcea6-0e44-3fa4-b9a6-24ccea993183 | -4.12786 | -47.2903 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1831f03-518d-356b-bb4e-9911614421cb | -2.52293 | -47.81798 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7df5e08e-8626-35d5-86b8-2fdd19cd6b00 | -5.00221 | -42.42282 | 2025-11-17 04:38:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3fb2e89-2eb0-3002-8d4c-b57d4d027fa1 | -4.42107 | -45.55167 | 2025-11-17 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6830b52-6898-3ace-a326-e9695df09102 | -6.74248 | -42.95035 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 59ad4547-0504-363b-8eee-fc21b6234bf1 | -3.33978 | -50.17237 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a4fc0a7-c91b-3d6f-b3b8-4dcce68d3f8d | -3.07394 | -45.20133 | 2025-11-17 04:38:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43f944aa-2593-3307-8342-e3ccf2ccfc14 | -2.80634 | -48.68286 | 2025-11-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32e7abc3-9b8a-35a0-aa80-c0c13b14338c | -5.47328 | -40.96696 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e8c7bfa6-b902-39db-83a1-61285daa67ab | -3.11008 | -49.47688 | 2025-11-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 470c611a-96ea-3d87-be60-f5ecb59e1abd | -4.54756 | -50.43545 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8576cc86-17ed-3474-a2d1-e5b022def18a | -6.22621 | -47.2374 | 2025-11-17 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a309bc75-5d88-3371-bc24-2083197b62ce | -8.09789 | -46.0555 | 2025-11-17 04:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28bf386a-7bfa-3ca4-b737-916baa7fc1ab | -2.45529 | -50.27701 | 2025-11-17 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d0ad177-3297-374c-8c33-ead9db134137 | -3.23106 | -50.49858 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac0d7a31-e46d-3da3-beb6-84f41a3df630 | -3.38261 | -46.06907 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 499f362e-aa16-3bc8-9e6d-07d44e433166 | -7.63538 | -46.0529 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7f335f2-301a-37fd-ab2e-51546431118e | -2.13291 | -49.80407 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e60b03-d649-3663-94b4-e72acfd2dab0 | -3.46507 | -49.99036 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd670b8d-ac85-34e3-8f62-63e8553f31e1 | -7.03443 | -47.61775 | 2025-11-17 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 796fba3b-e71a-3ed3-86c5-17ad55ccef48 | -3.39599 | -50.18844 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 570f939d-07fa-3435-bf97-29609456f9a5 | -4.61878 | -47.26491 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f2f7dde-58a0-3d73-98d9-c1ded93eaa82 | -3.78104 | -49.2558 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35c13962-16cc-3f5b-bf2a-eb494c0ae9d8 | -2.01777 | -51.40393 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2d8421-393d-3ad5-9c24-5617939d144d | -2.89517 | -53.2874 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da57573f-112a-3d39-b25a-87fe7e70bdb6 | -8.51631 | -45.36128 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f067504-9701-3c09-b83f-f0998363eaf0 | -4.04836 | -50.48658 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f790f5f8-0b6c-34fd-8267-24b30d66e0d5 | -3.83384 | -49.80571 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e91c3d3-105d-35c2-a546-9665c28a44eb | -6.68152 | -42.05478 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b3d84d4f-0320-396b-9dba-2e4f653ae9c7 | -6.00136 | -51.51544 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a237ab48-e084-356f-991e-7c59019af8ff | -3.84066 | -48.1579 | 2025-11-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b361bb7-6f47-3b18-b3bd-a3ea35cb24ae | -3.3498 | -43.49665 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1544088b-c9aa-32da-8803-00fa86d7c518 | -5.96558 | -47.24487 | 2025-11-17 04:38:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186f40c6-b7df-3826-a085-67b0f3f00226 | -3.55228 | -41.71952 | 2025-11-17 04:38:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 63d6dda9-738e-3bef-a0cd-831344aeedfc | -3.33265 | -50.28214 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d93025aa-d2c1-3de4-9ed2-e28b029dba28 | -4.01745 | -48.81345 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba08a16f-8a4b-3241-8bec-7b894d78342a | -2.24812 | -53.62391 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af187cd1-c8c1-3d43-872b-eff4c6c14001 | -2.88106 | -53.9707 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b7c127-78b7-3289-96bd-9d2e5109ffe1 | -7.48116 | -49.32928 | 2025-11-17 04:38:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0801b7f-3d9f-3490-999b-c684cfdd4380 | -4.9761 | -47.81207 | 2025-11-17 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5c09a9-c552-3fc6-9f6a-bded83f08b54 | -6.68365 | -42.03973 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 325336ed-1e7d-3a20-ab9a-ef192071bbfd | -2.89122 | -53.28678 | 2025-11-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4d23bca-fe2a-3ab1-a384-36fc84855f26 | -3.39817 | -44.17745 | 2025-11-17 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 099b8def-c036-3c93-89c2-43828444e6c5 | -3.40956 | -50.12436 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4380eb9f-2de1-3f57-b039-6a1a946adec3 | -5.32566 | -43.04614 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61285d09-6af6-3c60-9a5f-aec3ea9251f7 | -8.29779 | -43.95445 | 2025-11-17 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d99bda85-1ce2-322d-bce9-5ad79f57e8c9 | -6.68438 | -42.03456 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a0bf46d5-5430-3891-b723-1d6fc2c3cd76 | -2.50058 | -43.24387 | 2025-11-17 04:38:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3539ece7-1816-32f8-bab9-9f0489e55ccd | -4.49976 | -50.43172 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03de66cf-3551-3b88-ae8d-3490753a1bbb | -5.69108 | -47.11269 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1793c49b-7f08-3877-b66e-e53a7b746193 | -6.36007 | -46.15318 | 2025-11-17 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1490cb99-7ae2-3a75-85bc-38bec0f97a01 | -2.16873 | -48.42776 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aaa3fd5-1bf5-3c29-ba1b-349b0f8441d9 | -6.68766 | -42.04546 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6ba6a41c-ea07-38db-a004-71b6da26b61e | -4.74436 | -46.40282 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03884739-285a-3bca-bab5-410b268f6b62 | -3.33698 | -50.16824 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f59f1b0-d7a0-3868-9990-903c079b9177 | -7.13007 | -47.12632 | 2025-11-17 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 167b26a0-cbb6-344c-876b-6347b0353c05 | -4.31339 | -53.7203 | 2025-11-17 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c81d934-aa13-30e7-8e59-76cbbeaa3d6e | -3.79988 | -51.09693 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f0bc568-8598-34c9-8e16-5e22a25b5fc2 | -5.61738 | -37.80734 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 467ad58f-95f2-3932-8e6d-597191bdf0d9 | -6.67423 | -42.03826 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 961044f0-97d2-3f52-823a-9d2973f76560 | -3.99237 | -47.27332 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5e3d145-bd10-339c-a8bf-add37165d901 | -3.87971 | -46.46265 | 2025-11-17 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 786a3f27-004e-34aa-9993-e28ee941bde1 | -8.21269 | -47.07828 | 2025-11-17 04:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d764aee-9860-380f-898d-fb00fd4d580c | -5.26427 | -46.10715 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17456f86-131f-3dc9-b60e-5d2cbf8fd2c9 | -3.38428 | -50.13148 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd37ae1e-ce0c-3806-b9c6-88b82f3a35d0 | -7.54754 | -42.52022 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81374b04-27c7-34b2-9192-d44ecdd1868e | -3.82252 | -45.56773 | 2025-11-17 04:38:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78c121d3-260e-38a0-af1b-f89f532ad5bf | -1.41404 | -54.46521 | 2025-11-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9620558c-c9ec-3c56-be17-7db9f012765d | -5.62391 | -37.80335 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 355e0530-18c9-3e7d-a6d8-4bb06549f05c | -6.10765 | -44.22131 | 2025-11-17 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8a813df-2589-3f3c-bd98-de0a2cbcbe78 | -7.7038 | -42.94946 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ca7ac7e8-8bc1-3c94-bf1b-d7833809754c | -5.88979 | -43.97392 | 2025-11-17 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8309db14-b331-3cdb-9387-9888f4e6d8ef | -2.51962 | -47.81747 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bfe9d065-d77b-3c01-9ff8-5d50dd014f25 | -3.5898 | -50.71682 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 801b65a5-ce88-33c7-ad33-07b8a11c2d59 | -7.49329 | -45.87141 | 2025-11-17 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 047588a3-4ecc-347f-9807-e61f8aee84de | -3.47568 | -50.24136 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78f8f932-74c1-3b5a-9c2e-e68842cf9c9e | -5.69899 | -45.98626 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 843a5b3f-8e2f-3530-ace2-5d57d6ca4cb4 | -7.9705 | -50.00706 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bf05507-a448-3a1e-a2bd-32afaf4d3a2b | -5.61773 | -37.8026 | 2025-11-17 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 80db077e-85a4-315f-801c-955d3e73ea83 | -7.97159 | -50.00012 | 2025-11-17 04:38:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d1ff745-b1a6-3db0-863e-b6df5194d40e | -6.91149 | -46.46331 | 2025-11-17 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a095de08-d75b-39df-9423-063b50e3f2f8 | -6.91211 | -46.45922 | 2025-11-17 04:38:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee0deb3-15c9-3ece-be55-757f625c493e | -4.24223 | -49.67663 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32da0c92-06f5-3eb7-a7f7-997b98a6399b | -5.34355 | -43.04435 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9f53214-98e0-34de-a96f-0f3eedb7b9ea | -4.71011 | -48.31893 | 2025-11-17 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9f9dd60-372e-3a54-836f-7319659bc2e9 | -5.34787 | -43.04497 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3dfb44ec-5f91-3d19-9bba-e3807d021cda | -7.18516 | -44.64793 | 2025-11-17 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81a8360d-8eec-37f6-8304-8cf6b5a18aab | -3.63025 | -44.18851 | 2025-11-17 04:38:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 927dccda-6ca7-3fb3-81ff-8304f71de472 | -7.29033 | -45.45692 | 2025-11-17 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6baa1f43-5ffa-35ce-9b2f-c27d12566fd6 | -2.46386 | -47.08378 | 2025-11-17 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c93c947-d69f-3a80-bfdd-1d36b869475d | -8.06631 | -46.47824 | 2025-11-17 04:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52ae62e9-da16-389b-abc7-1de15b731cc3 | -3.82197 | -47.4924 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64790914-844a-33a8-9e2f-c290d5717ef1 | -3.54869 | -41.99789 | 2025-11-17 04:38:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 706e1b7e-148b-3820-912c-f66f3e670d97 | -3.3757 | -46.04393 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfb268fe-3c60-3137-a564-d0431fdd9dba | -3.49433 | -54.04921 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d652ab2e-2ad4-3d03-b467-9f461226aa53 | -3.74476 | -47.59277 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00813847-9919-3679-916d-1766ea6089ca | -7.04003 | -45.92879 | 2025-11-17 04:38:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bfd3327-8017-3b55-9bce-df910bf99fd2 | -3.23672 | -50.507 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
