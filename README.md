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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c2accd2-e9d0-3f01-8aa7-e84c1abef040 | -23.61801 | -54.49316 | 2025-11-24 00:28:00 | TERRA_M-M | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 25dd0cf3-b14b-3c92-b753-a30d365fee4e | -23.6127 | -54.49897 | 2025-11-24 00:28:00 | TERRA_M-M | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 5db7f2c6-63f3-3b38-b8d0-d0ef59ffd00c | -19.51479 | -49.28962 | 2025-11-24 00:30:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93f48925-a4d8-3aea-9be3-b89c93722624 | -19.21076 | -57.33818 | 2025-11-24 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 90a37d44-15e3-3c4e-9506-bfbdfadbe70f | -17.13526 | -50.26006 | 2025-11-24 00:30:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d52cc9da-e744-3ec7-843c-cc737f26343b | -17.54851 | -54.04984 | 2025-11-24 00:30:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e19560dd-5016-30b3-862f-af98e3855157 | -19.20209 | -57.33417 | 2025-11-24 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 215bc438-b314-3a14-bcfc-c36d2a362be7 | -19.21832 | -57.33261 | 2025-11-24 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.4 |
| f08c43d9-9441-379c-b61d-5683a3f5eb27 | -17.54641 | -54.03085 | 2025-11-24 00:30:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b53f9748-4b89-30ea-adaf-595af9b58f41 | -7.29823 | -45.43023 | 2025-11-24 00:32:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 406f1588-168f-3bbd-ab92-098e0fb47557 | -11.7857 | -49.31787 | 2025-11-24 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e107e104-66aa-36ec-821a-8473434aba64 | -12.00881 | -49.27321 | 2025-11-24 00:32:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1ec954d1-ab3d-3fed-89b4-21c243f8172a | -8.73029 | -48.03123 | 2025-11-24 00:32:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 143223ba-d41e-3215-b7b5-fa3d85de4585 | -7.30041 | -45.44481 | 2025-11-24 00:32:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 63385c6c-8a2d-3490-a672-56e2f282611a | -8.67457 | -47.83911 | 2025-11-24 00:32:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 553b988f-d87c-3f01-ad92-142ef9d0a7b1 | -9.8217 | -47.25023 | 2025-11-24 00:32:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 414ebb89-e8c7-3f83-bb6c-fe582cc50c57 | -3.442 | -45.922699 | 2025-11-24 00:32:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b585990-df76-3892-a83d-f6e34eec2b35 | -2.8849 | -51.8125 | 2025-11-24 00:32:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5d9cdb-6436-390c-8ac0-8ca71419c012 | -3.2097 | -45.764999 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f69348ee-9371-30c1-bdb1-5dd22c69dbf1 | -2.2913 | -53.908501 | 2025-11-24 00:32:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9675bea5-0d9a-3173-80b1-527c94dc8ed7 | -0.8767 | -47.555401 | 2025-11-24 00:32:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2af0187-1c8c-3b5b-8275-23d8a016bb83 | -3.215 | -45.923 | 2025-11-24 00:32:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b383915e-172a-3242-a8ad-fc20687a963b | -3.7481 | -47.124802 | 2025-11-24 00:32:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4d9c5c-74cf-386a-a2a8-9b89a787ae97 | -3.2783 | -45.435799 | 2025-11-24 00:32:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2df703-7ce3-3bf4-b6d9-179dad7a1ddf | -2.2881 | -53.894001 | 2025-11-24 00:32:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b721469-3a81-316d-a7b0-13432ebe3f97 | -3.276 | -46.053501 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 70abc926-8414-3750-bba2-fd86b8b84817 | -2.4191 | -49.072601 | 2025-11-24 00:32:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e15b942-c5bd-3000-ab45-c583e4569fb9 | -2.7618 | -48.9492 | 2025-11-24 00:32:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 193e7954-553e-3e82-89cb-0bdfe3153173 | -1.7292 | -46.190701 | 2025-11-24 00:32:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0131318-f38b-36a2-901d-d313feffd381 | -1.3358 | -53.1717 | 2025-11-24 00:32:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d685d44-808b-364c-8cfe-6ea553f48aab | -2.7966 | -45.359699 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4795243-53bb-31cb-aec9-33dfb7a6128a | -2.7672 | -45.1427 | 2025-11-24 00:32:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b853b730-1c88-3f8e-aae4-bfc1e87fe1ac | -2.7271 | -45.9095 | 2025-11-24 00:32:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1ba6d48-8c4b-339c-af5f-c0263b68da5f | -1.4831 | -45.882401 | 2025-11-24 00:32:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b91a35fe-f3d1-3ec4-a481-272be58e3b8a | -2.5748 | -49.077999 | 2025-11-24 00:32:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad335ce-1e1b-3746-9bcc-4009f8269301 | -3.2264 | -45.9277 | 2025-11-24 00:32:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c539ff1d-6da9-3343-8309-c11b3378fbfe | -1.9491 | -46.249699 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26efca4-d6f4-347c-a9c2-f4a4b0553c58 | -2.8703 | -51.793098 | 2025-11-24 00:32:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 778976bc-c66a-3e43-a1a4-37f592ec286a | -2.8768 | -45.259998 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdd32de3-f6cd-3a26-9287-e9aadb0dd6b5 | -2.8751 | -51.814602 | 2025-11-24 00:32:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ee39a6-1475-364f-94d3-05914a308074 | -2.9143 | -45.333302 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 672d50c4-1c75-3168-bc04-0d9e574523d3 | -3.7497 | -47.131699 | 2025-11-24 00:32:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def907b3-b275-36ff-86ca-4f6b40837ce1 | -1.2199 | -46.398201 | 2025-11-24 00:32:00 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9b4ed8-7f7d-3115-8306-ba905b3ea263 | -1.4799 | -45.8685 | 2025-11-24 00:32:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58a14143-2ee2-3af8-896c-4bf9060fb498 | -1.3261 | -53.173901 | 2025-11-24 00:32:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c425a33d-ced3-35d7-8899-93ed93384abe | -1.7277 | -46.1838 | 2025-11-24 00:32:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b922a61-2ec9-3ab4-9f87-15cd49b03bac | -2.565 | -49.080101 | 2025-11-24 00:32:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98ce0976-4ac6-3e03-8397-9cc90f774532 | -3.2586 | -45.484299 | 2025-11-24 00:32:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88d2c843-690a-3f9e-94d3-5e31e90e9c79 | -2.7999 | -45.373798 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad3415f0-1a12-3c6e-9e10-43c2216b771c | -3.2767 | -45.428799 | 2025-11-24 00:32:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 628da758-3edb-3873-bddd-e36e55eed719 | -1.4897 | -45.866299 | 2025-11-24 00:32:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26718476-4c41-3d15-9a6b-04825d20f7da | -3.2166 | -45.929901 | 2025-11-24 00:32:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37a8f71e-db32-3f15-ae4a-e9a77b8a6c3d | -2.5475 | -45.622002 | 2025-11-24 00:32:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f40c3048-d4ca-387c-a627-b569ad03c278 | -1.2215 | -46.405102 | 2025-11-24 00:32:00 | METOP-C | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2755de8-4219-39b6-ac35-5d378ada692c | -3.2795 | -46.023899 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8edf5cdd-e197-3038-9058-b5ca61d654e5 | -1.7308 | -46.197601 | 2025-11-24 00:32:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 836f5b92-1d9f-3330-a6b5-8aebf5c856f1 | -2.7982 | -45.366699 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 889ea357-109f-33a2-a632-fd2b0d5f1e82 | -1.4815 | -45.8755 | 2025-11-24 00:32:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8670953c-1065-304d-b809-741842d1f671 | -2.1282 | -45.3237 | 2025-11-24 00:32:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffa2a8b-287c-3b50-b05f-925056c7f7f1 | -2.8784 | -45.267101 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc7490c7-edb3-36b9-b49a-d7d0d1b95c1d | -3.9253 | -45.3783 | 2025-11-24 00:32:00 | METOP-C | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c130a8e-ea33-3847-903a-3e5782e89a50 | -3.045 | -45.0951 | 2025-11-24 00:32:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed03a1fa-3701-3c64-b30b-396b60102b59 | -2.5871 | -47.368801 | 2025-11-24 00:32:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2576af-d942-3a0f-b790-04a66e123a01 | -1.8256 | -45.577599 | 2025-11-24 00:32:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2d38b4-a9e0-3805-a7a6-94760433da9f | -3.7399 | -47.1339 | 2025-11-24 00:32:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf794cf-4c98-33a7-8316-d4f0f3376fac | -2.795 | -45.352699 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdcfc5d6-07af-30d3-beb0-aabef2027934 | -2.5573 | -45.619801 | 2025-11-24 00:32:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08b9c095-d0dc-3ac0-a5c0-426ce7dc37d1 | -2.8833 | -45.2883 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8288aab-dbd7-3805-a4de-27bdb9d11f7f | -2.1402 | -46.4081 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32cdd36a-2bf2-3b22-82d8-7d5e2e150f07 | -2.2806 | -46.0312 | 2025-11-24 00:32:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e90b2e0d-8131-3d2e-bb15-fc159ed22a2b | -1.7136 | -46.481998 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 155248d0-4626-31a3-9ef4-8832d3114696 | -2.1433 | -46.421799 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d419616-a92f-3951-a078-9dbf9f9c0fe3 | -3.2744 | -46.0467 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5136c2f5-35a5-3853-8fe0-12219f352f67 | -1.3329 | -53.159199 | 2025-11-24 00:32:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d739cde9-41b1-3bf2-8a6b-02c4f352ec0c | -1.4929 | -45.880199 | 2025-11-24 00:32:00 | METOP-C | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2c39d51-f635-3ac8-9436-909ee605a2f1 | -2.1418 | -46.415001 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff1e702-1283-399b-8a52-5f5f99cb4572 | -1.0714 | -46.740002 | 2025-11-24 00:32:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b85a286-0e6e-33fc-af35-84836dd05cf5 | -2.2822 | -46.038101 | 2025-11-24 00:32:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4280c1fe-80a2-3e0b-8f89-c1ec4b83d41e | -2.8817 | -45.2812 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c51f057-0b22-3966-889e-3a6b63485aed | -3.2081 | -45.758099 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44265a54-d035-3d38-9ec6-39bdefac23ce | -2.5445 | -45.5639 | 2025-11-24 00:32:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81474bd7-4937-37e6-b689-463420b29ec7 | -2.5507 | -45.635899 | 2025-11-24 00:32:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 432136dc-8558-3b32-ae8a-ca775c2b2c58 | -0.8782 | -47.562199 | 2025-11-24 00:32:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce4dbf70-f192-3b90-9520-dafba95dfd54 | -3.2713 | -46.033001 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 149cbc03-c8fd-38d5-8664-5a5d36d984ae | -2.7635 | -48.956799 | 2025-11-24 00:32:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb723f87-12d5-3ef3-9a78-740e4dc985d0 | -2.5491 | -45.628899 | 2025-11-24 00:32:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91a57fa6-f831-339c-9e52-ab2c94f46e28 | -2.1304 | -46.410301 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb9619f-ec75-3ca6-b4c0-0f8aa3107837 | -1.4913 | -45.873299 | 2025-11-24 00:32:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 108f71af-fb72-346c-8af0-f580e82d9fd9 | -3.369 | -46.054199 | 2025-11-24 00:32:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44b18adc-9eb7-3f27-a896-fc379b4fc2f3 | -2.9126 | -45.326199 | 2025-11-24 00:32:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6a1676-96a2-3d7d-bcb3-ab52570582a7 | -1.824 | -45.570599 | 2025-11-24 00:32:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f51fe49-892a-32a0-b48d-74aa2c5a9742 | -2.1265 | -45.316601 | 2025-11-24 00:32:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5459691e-d20a-3ff2-9b3f-5adb7149322a | -1.712 | -46.475201 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b8c1ca-b7d0-3f8c-8b0c-4504f5f64b71 | -3.2602 | -45.491299 | 2025-11-24 00:32:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5ddeb01-8359-3fc6-9b0c-9d885f281cb1 | -3.963 | -47.660999 | 2025-11-24 00:32:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7302df36-2208-3c91-8a1d-dd01cdd19668 | -2.1298 | -45.330799 | 2025-11-24 00:32:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff61104-fdfc-38ca-831d-20fcb9665abe | -3.215 | -44.357498 | 2025-11-24 00:32:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff2033fc-a90e-3376-8be2-4d13c0f97566 | -3.168 | -50.242802 | 2025-11-24 00:32:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef74d5b1-3937-3845-976c-1f54f2f7da3a | -2.132 | -46.417198 | 2025-11-24 00:32:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5e75684-f5ec-318f-a033-5f53c1600afd | -3.3378 | -45.649101 | 2025-11-24 00:32:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
