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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3e8e06c-67c7-303d-841c-d19f0800c6e5 | -9.3278 | -46.5385 | 2024-10-06 00:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 242.9 |
| 0971f8d6-ed44-3a5e-b3a2-03b7e85beb19 | -9.3464 | -46.5589 | 2024-10-06 00:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 4b0865bf-3af6-3020-ad9b-e177ebe3a65c | -9.3467 | -46.5365 | 2024-10-06 00:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 268.4 |
| cd6c972b-7b83-3880-b60a-116888434bbf | -9.3637 | -64.3378 | 2024-10-06 00:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 492b5d39-ce2e-3b19-84ea-3b5857c7e768 | -9.3638 | -64.319 | 2024-10-06 00:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 5fc2bd1b-0afa-3ac8-a5ac-3cc002a97b8a | -19.6605 | -56.424599 | 2024-10-06 00:46:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e1fdb1bf-8f2b-33ea-a93f-8611281259b3 | -17.641701 | -46.386501 | 2024-10-06 00:46:00 | METOP-B | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d42f7831-4a18-3e4c-b9ac-135407dc087a | -17.6437 | -46.394901 | 2024-10-06 00:46:00 | METOP-B | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0f2d6a1-75ea-36f8-9d70-60753b14f7aa | -9.6691 | -47.8328 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 23784db6-a194-39b3-97f9-01b70da276f5 | -9.6694 | -47.8108 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3b60369e-9d0d-3eac-9dc8-aea30eceba3a | -9.688 | -47.8308 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 209.4 |
| e52c75da-c1c0-356d-8401-01954bf8bd69 | -9.6883 | -47.8088 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 2d73a834-d645-3b17-95ee-7a6366895448 | -9.7069 | -47.8288 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 7a770fdd-9e9f-346a-a6b1-3409afb4d740 | -9.7072 | -47.8068 | 2024-10-06 00:46:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 02a7a0a6-bf05-39e7-a224-c791343aa9bf | -9.8552 | -60.2966 | 2024-10-06 00:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 97a224bf-9d30-3d04-89dd-6e4aadaeb16d | -17.619499 | -46.954899 | 2024-10-06 00:46:02 | METOP-B | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c45ea1e8-c192-38a9-8316-74a784e28e59 | -17.6213 | -46.962898 | 2024-10-06 00:46:02 | METOP-B | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6da089b8-f970-3d3c-9abb-28666e9c1ac1 | -18.819901 | -53.745499 | 2024-10-06 00:46:06 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c99be473-9c60-367e-a00d-b77b3fb072d2 | -18.810101 | -53.747501 | 2024-10-06 00:46:06 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5a286284-1f97-34be-af46-cd7670a64540 | -10.8153 | -44.7643 | 2024-10-06 00:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| feb35063-dfab-3da4-bb7b-d996f7b5fe20 | -18.9051 | -54.508301 | 2024-10-06 00:46:07 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b267dbd8-bb72-3e76-804e-8bcaf136c873 | -18.8953 | -54.5103 | 2024-10-06 00:46:07 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 21941eb0-f639-32a4-8478-06e39b763f77 | -18.8855 | -54.512299 | 2024-10-06 00:46:07 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 85a7681e-571d-3938-a843-207661cff915 | -18.887699 | -54.523602 | 2024-10-06 00:46:07 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b79da458-69e2-387b-a77c-2696f39f540a | -18.8757 | -54.514301 | 2024-10-06 00:46:08 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dd436eb4-a760-387c-b125-d325ab7ef675 | -18.877899 | -54.5256 | 2024-10-06 00:46:08 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 90c5e85e-fde9-3144-954d-a0da0d6bcbc5 | -18.853201 | -54.448799 | 2024-10-06 00:46:08 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aec78a03-b2a3-3d13-9557-167c3dc2ba9a | -11.0966 | -54.2336 | 2024-10-06 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ee05aaf8-6876-3584-8969-826d418340c4 | -11.1155 | -54.2319 | 2024-10-06 00:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 20d537d7-c25a-3bc3-8423-ae8767a5f143 | -16.963499 | -47.111401 | 2024-10-06 00:46:13 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df829cf0-208d-37f0-b426-9ec3e96f8251 | -16.952 | -47.105801 | 2024-10-06 00:46:13 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9baf0e79-935a-3624-acfe-1d5e2c963874 | -16.9538 | -47.1138 | 2024-10-06 00:46:13 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a4049817-d094-3842-9514-7a125c5a5e23 | -16.944 | -47.116299 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e7138d27-06d6-34c2-875b-b0a403cce570 | -16.908701 | -47.141899 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 50461e73-8424-37fe-99d3-e928e13cd624 | -16.9105 | -47.149899 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4208c91a-8dc1-360c-9709-0f338ec0fe9d | -16.912399 | -47.157799 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79f29a88-bc58-3caa-afbc-1586de87624a | -16.9007 | -47.152302 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eaabb218-3eb7-3f4f-810e-de47c19ae6aa | -16.902599 | -47.160198 | 2024-10-06 00:46:14 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5649e44b-3c52-3590-a788-3880a4c25caf | -12.0211 | -63.7478 | 2024-10-06 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 4b5def9a-8ddf-365c-81b6-0494f0f09b31 | -12.5093 | -45.3017 | 2024-10-06 00:46:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| a09cc12a-4e45-3e30-987f-326737d5a320 | -12.5098 | -45.2786 | 2024-10-06 00:46:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1e79ce87-74a3-307b-aed3-e0d721954374 | -17.307899 | -49.3158 | 2024-10-06 00:46:16 | METOP-B | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac1be5c3-6052-37f8-9c9c-e42c221c71f3 | -12.6089 | -53.1338 | 2024-10-06 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 942864b2-6a6f-3409-be5e-575d8542c227 | -12.6092 | -53.1129 | 2024-10-06 00:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a1cb7088-22e7-341d-b2ff-0b5db344fa73 | -12.628 | -53.1317 | 2024-10-06 00:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 8cdee4ca-0330-3302-81a7-26e8c1e3b831 | -12.6283 | -53.1108 | 2024-10-06 00:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 78f97a98-f693-355b-aaa3-8ff193671af7 | -12.6474 | -53.1088 | 2024-10-06 00:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 14d633a2-09d3-368e-8e12-db13d769c46e | -12.6532 | -54.0415 | 2024-10-06 00:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 640cda0c-9aeb-3754-b8fa-1b9c642a6f49 | -12.6535 | -54.0208 | 2024-10-06 00:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9b0623d6-ac58-3a89-91dd-f80506150f0f | -12.7627 | -50.5567 | 2024-10-06 00:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7ae4adc3-140c-3043-b05a-8c8d3d05b504 | -12.763 | -50.5352 | 2024-10-06 00:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 997bf0ea-1520-3210-99b1-babcc805f6bc | -12.7634 | -50.5136 | 2024-10-06 00:46:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9e12cdcf-2b75-3de7-acb6-9742ebed5e7f | -18.7066 | -57.2388 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfbfc4ea-42cd-3d16-a018-d9365cd395bc | -18.709499 | -57.255699 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1a9a341-b617-372b-9a88-db9f5e2b2e3d | -18.7185 | -57.306499 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d09fce78-5848-3a1b-9b1c-b3537a73eaa9 | -18.7215 | -57.323601 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e943d1d5-3033-389e-9890-c0158463006d | -18.724501 | -57.340698 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 74cca961-b547-3241-b6c7-7d72bf345ad4 | -18.696899 | -57.240601 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a057f69b-82d2-30bb-ba4f-788530ea68e7 | -18.6744 | -57.227501 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c301c33b-2f37-3ab9-85c4-818461cae68e | -18.6646 | -57.229401 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f672e89-e014-31cd-8bad-a25dfcbed7ab | -18.6549 | -57.231201 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 664d9b28-9a3d-33fd-a6e4-7c1fc12a452a | -18.6579 | -57.248001 | 2024-10-06 00:46:19 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4f3e490f-626b-3973-97d8-c12f30948602 | -18.645201 | -57.233101 | 2024-10-06 00:46:20 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40b65d6a-4227-3ee5-a618-66d364e3127e | -18.648199 | -57.249901 | 2024-10-06 00:46:20 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6e698076-7306-3ad7-acc2-e5f35412ec46 | -18.6511 | -57.2668 | 2024-10-06 00:46:20 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6dcb58bd-b6f5-3411-8680-9f1a71587ef7 | -18.638399 | -57.251701 | 2024-10-06 00:46:20 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 36ea87a8-a121-3330-9af9-35663480cedd | -17.822399 | -53.747398 | 2024-10-06 00:46:22 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d89038cb-ceef-3a5b-8815-b114a67fb9e5 | -17.824301 | -53.757301 | 2024-10-06 00:46:22 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce62e763-d71f-30d8-b6f8-175bdffd1b44 | -17.8263 | -53.7672 | 2024-10-06 00:46:22 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96fb080a-6b0f-361b-a1df-d14e1624281c | -13.6724 | -51.1911 | 2024-10-06 00:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ca6389ca-2629-3b38-8453-aa6d294d1d45 | -17.812599 | -53.7495 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 183fca34-acaa-3ee2-abb8-9bfee9f569b2 | -17.814501 | -53.759399 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a577185-ee10-377d-9d76-d238594d9468 | -17.8165 | -53.769299 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3722a90c-bd0f-38a4-bc5c-bff366c24071 | -17.818399 | -53.779202 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7efa308-68b2-3066-a4c3-b772866a54cb | -17.804701 | -53.761398 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b563f67-2210-3797-9623-e3a5796a41fb | -17.8067 | -53.771301 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 717279d8-b0e3-3fbe-944a-e27ad425dedb | -17.808599 | -53.7812 | 2024-10-06 00:46:23 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35001bdd-8f6f-302b-b34e-dc314c3bc833 | -15.7251 | -46.024799 | 2024-10-06 00:46:29 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66ffc692-08bc-33d7-a481-9712e787d712 | -17.8533 | -57.647999 | 2024-10-06 00:46:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6fc625bb-3195-331d-acea-50a08a3d333d | -17.8405 | -57.6325 | 2024-10-06 00:46:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c1106bbd-e699-33ed-8a96-49b8b43ec1a6 | -17.8435 | -57.649899 | 2024-10-06 00:46:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9c5ae7e3-f336-32e2-9850-3f15a553d360 | -16.3959 | -57.3641 | 2024-10-06 00:46:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| bc707be6-4c1a-3924-910d-53827e082f5e | -16.3304 | -51.258701 | 2024-10-06 00:46:38 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a173b93-9782-3322-b95a-200ec6c201af | -16.332001 | -51.266102 | 2024-10-06 00:46:38 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4103f53d-d055-3cec-acea-45b12a5fd8b2 | -16.333599 | -51.273499 | 2024-10-06 00:46:38 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf15540b-66d2-3b0b-9e81-6d577bdac163 | -16.4158 | -57.3415 | 2024-10-06 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| a05b17e1-49a2-34f3-b6d2-18ad6e5d79cc | -16.4362 | -57.278 | 2024-10-06 00:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 33322f9d-6b3d-3e70-b93d-22ccbe705e2c | -16.5553 | -55.9287 | 2024-10-06 00:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 1856c592-8455-31e4-b458-f4f954c4370a | -16.096901 | -50.2229 | 2024-10-06 00:46:39 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f21140ec-1546-3484-a34c-1ed106214569 | -16.0984 | -50.23 | 2024-10-06 00:46:39 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4b942f-d05b-3d35-a2bd-6b5025f73ce9 | -16.0742 | -50.2131 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8493eb06-4cea-3327-bf81-c6784fda817f | -16.0758 | -50.2202 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d021faae-6fb6-3ca8-b64c-21d2b8d32c1b | -16.077299 | -50.227402 | 2024-10-06 00:46:39 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2761ba-8f56-3b10-a158-b01c90a0c35e | -16.078899 | -50.234501 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3c436d-6e18-3dd6-9442-b5b6d1b8f5ac | -16.066 | -50.2225 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 39209bc6-2e4c-3da2-a95a-f71640823e76 | -16.067499 | -50.229698 | 2024-10-06 00:46:39 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d3abf3b-166b-37a2-9604-70b7a0733d50 | -16.320601 | -51.260899 | 2024-10-06 00:46:39 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2fce608a-0489-36d9-ba73-12d1ef671604 | -16.322201 | -51.268299 | 2024-10-06 00:46:39 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 247938f8-c866-3cca-af01-1686747361ec | -16.323799 | -51.2757 | 2024-10-06 00:46:39 | METOP-B | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d394467-1060-3fdd-9c7c-75719bf0fbd6 | -16.124001 | -50.441898 | 2024-10-06 00:46:39 | METOP-B | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
