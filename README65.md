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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c27a7b6-ace6-3ab7-ab1e-7d2a547fa1f4 | -8.24432 | -45.5996 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b590152-9a31-3216-9c8f-9cb4f559ed37 | -7.69802 | -46.1075 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf1648d-d82b-3dfb-b231-62d54abf2de3 | -8.73763 | -52.35509 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86b09788-3153-340c-bd9a-32fb69009e20 | -11.88603 | -47.65388 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de2fe28-39a5-3945-bf4f-fc7c45c770e5 | -9.81675 | -46.39008 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee591169-81e0-3ca6-8297-39613d755d00 | -12.88091 | -51.00565 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9739dbcb-40a6-3386-9cc1-9eb27620636b | -11.74369 | -54.56471 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d71d01-ef37-3e4f-b49b-f5997d859196 | -5.74127 | -57.58334 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee91df80-4973-3971-a1d1-5e63c6f4df0b | -10.87661 | -53.98363 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a809318b-cea8-302e-b9d9-91be4f292d07 | -11.49636 | -47.73328 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f45e26e9-ccf4-34f1-8dbd-689e8c291eb8 | -8.45138 | -48.45482 | 2026-09-20 04:40:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c02e8512-a5e0-33d3-8581-1e14eccd4a2c | -8.77837 | -48.66397 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4af91fc3-a0b5-37ea-8831-d5098964dd20 | -10.54601 | -46.73066 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3e3befd-3139-3437-8634-734f3b90efaf | -9.03959 | -49.83747 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| adeabae8-b0e5-3db4-8a29-2cc98ce27253 | -11.94848 | -55.92369 | 2026-09-20 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9404f02a-13e0-331b-bc02-dfe8f371d736 | -10.2375 | -45.35671 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a23656b6-3afe-3092-8224-67b49e4d57c1 | -10.38689 | -48.99477 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 585db9e8-2f32-376d-90b5-eb48d212486a | -8.18173 | -54.75296 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80d8fd11-1091-342e-9626-91a42dfc4c60 | -10.93139 | -48.3152 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc2bbbca-1974-3460-9860-e025a45231a5 | -10.4772 | -46.29545 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65687d8-8a5e-3b6c-9ff8-dcecae389cf8 | -9.89951 | -46.5262 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d745a1ea-e58f-358c-926e-ccc4a849870e | -7.15873 | -47.47542 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44fa151a-889f-3b1a-82ef-1363eaf7a0e3 | -9.2403 | -46.23085 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fca635e4-4656-3a5e-a07c-b5c3cf6bda00 | -11.23935 | -48.38979 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22b7c3b2-137c-303f-83d7-5e9a517f3298 | -8.79802 | -60.8025 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1f8d585-a70a-32f4-99e8-172dc1b69137 | -11.68429 | -54.45281 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc3254fd-c919-3804-b59b-46ab50ad7ccd | -11.71154 | -54.55913 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3a4deff-df65-37fc-b3c2-f86d53a9b1f7 | -8.72574 | -52.35752 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9f2ac5a-ea98-3ea9-81ce-8c7e6d238334 | -9.78422 | -45.07125 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8d35b5a-37d8-3a5a-8263-8dbf951386ac | -8.8859 | -45.92147 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fa5b928-f777-3c3e-84c0-d02bc66ce292 | -11.84846 | -46.86169 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 895cf147-e256-38c8-89c2-9c219bb842e2 | -11.21983 | -54.07316 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b84311b7-0aa6-3dd0-8074-acda8cd1ce75 | -11.44339 | -45.32738 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ae60187-4674-3aad-b583-17e1052a4b7f | -8.32397 | -50.94529 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07f67da8-29a9-3439-b49e-5cfe3f3d0b40 | -10.39182 | -48.89854 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4397e407-317a-38ca-82c7-0e3240d2b717 | -8.41729 | -54.72285 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dbf2a84-7a89-3b3d-906a-fc00d993dbd3 | -7.55099 | -45.43198 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bd26312-26d9-3503-8201-72c3e0cd16f8 | -13.87935 | -48.58356 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d07dec0-e0e5-351f-9349-db7de7c3b918 | -6.3247 | -59.94497 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 654b051d-3398-3c17-8b5e-4c97f2c356df | -12.01785 | -51.47736 | 2026-09-20 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5f3ea77-41a0-3758-bb52-f9ca4ebc9dc0 | -11.74028 | -54.56031 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 054f2a77-90fa-37e9-85e1-c0c5c4c0749a | -6.08805 | -56.47319 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da57a2e0-caa0-3e3c-b35b-e26cbbc642f2 | -7.40956 | -46.62234 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5c48660-8327-3ebe-9298-aa5a17b07c45 | -9.28782 | -48.9421 | 2026-09-20 04:40:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a959397-9bd3-32e0-929c-9e70d0cf9265 | -10.77951 | -50.8781 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd13bb0c-39af-3b18-9181-84665f0245af | -8.71173 | -45.44696 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ba2c881-11e3-394f-a4ef-bdd590d5f401 | -11.85267 | -47.64473 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74b3cc4f-dc07-36cb-b3ed-3bb43e72ed91 | -7.15759 | -47.46088 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e8e312c-52b1-334a-b033-da714e969033 | -10.2836 | -50.23595 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10f20f00-caa5-3287-aa38-87699a9b6ca9 | -10.30942 | -50.23626 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85915585-8ffe-3e5d-b0dc-a402925c6865 | -7.53257 | -45.43332 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| fae54f2b-bc7a-399d-a691-5dcd6970d512 | -11.21675 | -54.06732 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a8a045d-bdc4-3c4a-b936-73d4880e8211 | -12.89543 | -50.98915 | 2026-09-20 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f41650b-1898-3d8b-b8b1-be75ba92ef8f | -9.9999 | -50.28208 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a927bd7-390b-379c-8f21-9f3b2904acc6 | -8.17589 | -54.76068 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3be0e255-0b06-3405-a927-23c78b30115a | -11.1145 | -54.03082 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6bdd0629-81c5-35b9-9c22-9a49939c4530 | -7.01494 | -45.24791 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 54a5a2fb-3b09-380a-af7b-88fb3b9b1599 | -11.07121 | -49.49691 | 2026-09-20 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e6480ed-646d-368e-bc2f-d2860422417b | -7.15208 | -47.47437 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d050a3f-2fa1-35d5-9e98-3aaea4885871 | -13.30654 | -51.77131 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 482f70ff-78b5-3c86-ba7e-8147a740e1fa | -11.44834 | -45.39813 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdbbccf7-f221-3e78-ba1a-c41879d2bc9a | -10.29555 | -50.2046 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 46bba4c9-aa35-3953-acbc-c47f127f0532 | -10.78239 | -46.33175 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b404355-ca30-36fb-971e-33d96a4c91e0 | -8.04053 | -46.2751 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7afaf99-7521-30c6-a670-9698b682bae2 | -11.22073 | -54.06801 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 962160ff-7b11-3c8c-91d3-8774ccc8d98c | -9.94142 | -46.52007 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7119cfd1-ff29-3cfc-8ae3-4222570ef67e | -11.74095 | -54.55664 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93ecf857-8858-3bf1-ae9b-f6c08c87c2a6 | -13.73281 | -48.7864 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ac41fbd-e7d3-3525-87e4-f3847eb42a6b | -7.74485 | -46.71852 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e51f24d-dd38-30d9-aed0-c0ca8bda8d65 | -12.31343 | -50.72689 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 00a864ba-62be-36d7-a248-7b6aed415362 | -9.27934 | -48.20099 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 431221b9-7eda-34fb-b6a0-d9eba9a88903 | -7.80137 | -44.94229 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb2e3412-9951-380d-b815-203310d850bd | -6.72849 | -55.06384 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8e5e9cf-b2e8-3c89-90eb-fb87ab44a80a | -7.32451 | -47.43656 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed121956-893d-323b-b998-4c4385fd2cbc | -9.03897 | -48.71258 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d14ae06-14f2-3854-9e0e-fda7e294e48a | -8.61191 | -54.59623 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9dca40b-d740-31f6-8379-d1b42b10a789 | -9.6583 | -54.32529 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f64a18f-6ce6-3870-b7a3-5118f3577ac2 | -11.09465 | -54.02726 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9c6d05c4-7662-34b3-9122-5342707700d3 | -13.03282 | -46.91107 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4253e4c6-6655-3551-9667-6950296319ef | -7.43325 | -44.73389 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cc3b2ab-796d-3de9-9038-f39c01b754e9 | -13.21081 | -51.75068 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44ad5522-484e-3c9a-8e61-53899945c16d | -10.78537 | -50.86377 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec4cce0f-a636-30dc-b5d3-4c493bd4a842 | -11.03568 | -48.30289 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab033155-34a5-3e09-97f4-8f2892e4aa3c | -9.78693 | -45.05318 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 537d8914-a3ee-3013-8538-55768b913e9c | -8.49521 | -47.4387 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afd1d03d-ffed-3b14-b9b9-63ca220f1a81 | -13.01332 | -46.97012 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc970633-f39c-3422-93a2-818a1ee9aac0 | -10.55981 | -46.56693 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb166786-ccfe-3415-afc0-ad7bd3f3ecbc | -6.64676 | -47.73002 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e37cd4ab-db07-3651-bd66-2e3070d55097 | -11.19773 | -55.03551 | 2026-09-20 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e4bd1cd-2bb8-3379-b2fa-0c9bae6342b7 | -8.797 | -60.80782 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b688339-d952-3c29-98c4-0ac37137d5f9 | -8.77175 | -48.70564 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6f39a1a-ea1b-3d3f-9aa5-190935fd55a5 | -11.49918 | -47.73746 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad313e16-a09c-38ca-ad8e-7db63a9c8402 | -5.84806 | -53.55807 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd8b9d8e-1244-3f6d-aea8-86616b40790e | -7.44691 | -46.51519 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4d8c0e8-5a29-3e14-9d3e-1d436a1e8315 | -6.44795 | -59.97752 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84488b37-0337-3f88-8fbe-a4d5cdf85c02 | -10.28186 | -50.24678 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67e12e1f-54f2-380d-887d-7cf65c9ca8da | -11.01731 | -54.12913 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07bc60f7-9727-391f-acd1-ddc6b51cd395 | -7.5451 | -45.42283 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 628816fe-5643-3f8b-8e67-75ecc8fa9905 | -10.27616 | -50.26069 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5b8d3bca-b9ef-3301-8689-667eddbe2784 | -6.06697 | -57.72961 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README66.md)
