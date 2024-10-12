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
| 9c0ba4fb-0adc-3a1e-ba76-a8cec2014e95 | -17.84 | -57.31 | 2024-10-12 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 032dabf2-c2c6-36e3-894d-faa3f8f7420c | -17.87 | -57.41 | 2024-10-12 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 14d976a9-4034-3c0e-80f1-0da0938b3786 | -17.87 | -57.34 | 2024-10-12 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ba012a5f-d595-399d-b304-d7381fb58ad3 | -17.9 | -57.36 | 2024-10-12 00:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 41fb864d-e22b-3388-a22c-7386a4ad62cf | -17.84 | -57.39 | 2024-10-12 00:03:44 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf9fdbd0-82f0-3551-bc59-196a54cc3fd2 | -1.6061 | -53.3492 | 2024-10-12 00:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| efb8dd51-cb8d-3809-a251-fde751abfa80 | -1.6169 | -48.0269 | 2024-10-12 00:05:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 18113f23-0199-3361-b03c-c6c89f966320 | -1.6354 | -48.0266 | 2024-10-12 00:05:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 9c6cead4-2ee7-3c5f-b144-cdf8492f0c79 | -1.8977 | -54.4309 | 2024-10-12 00:05:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 58b82875-c228-3cc7-ae0b-43651e814d6f | -2.7701 | -51.3622 | 2024-10-12 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 725014e0-d7c2-32d2-bd07-deb444917c8e | -2.7884 | -51.3825 | 2024-10-12 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 9075c276-1ea4-36fe-9ed2-30a204b9d665 | -2.7885 | -51.3618 | 2024-10-12 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 5508f9d9-3642-39a7-86f9-f0e2a6656c46 | -2.8319 | -49.5385 | 2024-10-12 00:05:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1f597afd-9960-36a0-b25d-8f56ca32d661 | -2.832 | -49.5173 | 2024-10-12 00:05:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e5ceb5dc-94e0-365a-8915-f29ba0e1ef3f | -2.8611 | -51.6699 | 2024-10-12 00:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| bebf0f84-2282-348c-98d1-52e4aa0c179e | -2.8795 | -51.6695 | 2024-10-12 00:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 995b6875-abb9-3ddb-b271-bd527d5d3a9a | -3.0311 | -50.5642 | 2024-10-12 00:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 14773b6d-c82a-319b-8d40-8fc08e856d25 | -3.1426 | -50.3724 | 2024-10-12 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 70873630-e063-3da7-b09d-dabeb89bd932 | -3.1427 | -50.3514 | 2024-10-12 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ea8228fe-95d0-3ef4-9d32-23b31b7228e4 | -3.161 | -50.3718 | 2024-10-12 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fb582de8-f986-39a8-b50e-aa894906646b | -3.1611 | -50.3508 | 2024-10-12 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 721b429e-9021-3f43-918b-32fd822d63b0 | -3.2136 | -46.7843 | 2024-10-12 00:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4c0f24b4-1606-3846-acaf-5b8230c644b4 | -3.6978 | -50.1225 | 2024-10-12 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 8455841e-ad34-344f-a109-5dd61a1b0d28 | -3.6979 | -50.1015 | 2024-10-12 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 08602dc0-bc47-394c-87d5-f70280cc4aca | -3.7163 | -50.1219 | 2024-10-12 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 24f27216-4eb3-35b4-bb80-524b2bc0d281 | -3.7844 | -51.3312 | 2024-10-12 00:05:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b3f4d8fe-fe1f-3c70-a156-8f2ccf1ac0be | -3.7845 | -51.3104 | 2024-10-12 00:05:28 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 98a741c2-af76-3d06-871a-6d0571a2ad61 | -4.0062 | -60.3869 | 2024-10-12 00:05:29 | GOES-16 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 33026196-4e31-3869-ad79-883199f83c62 | -4.1148 | -48.2515 | 2024-10-12 00:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3a404efc-f53c-387f-9c51-f0da2061405a | -4.3782 | -50.8087 | 2024-10-12 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| b6de6582-e134-3620-8096-79c0daca3d19 | -4.3967 | -50.8079 | 2024-10-12 00:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c68d5e2f-a6fb-339f-a34d-f80c03770381 | -4.7188 | -60.8072 | 2024-10-12 00:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 434cccf6-aa80-3abd-b412-594419d48813 | -4.7188 | -60.7882 | 2024-10-12 00:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 6069cb44-e3b1-371f-9d7a-2650887b509d | -4.7189 | -60.7692 | 2024-10-12 00:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| aa521f70-8aec-3d46-9cff-b16139037706 | -4.7371 | -60.7877 | 2024-10-12 00:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 3e37d52b-2fed-3000-ad32-942803e23435 | -5.5547 | -44.689 | 2024-10-12 00:05:38 | GOES-16 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b5091d67-5614-35d4-a075-c80cbc94b43c | -6.0791 | -44.6276 | 2024-10-12 00:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c80c030e-7978-3c67-834f-c8f216bf4a4d | -7.1097 | -48.3296 | 2024-10-12 00:05:47 | GOES-16 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 85e54fd8-abeb-3e23-a21b-eaaba51a2f3d | -7.292 | -64.6676 | 2024-10-12 00:05:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8ec7a097-8a8d-3db6-a46d-2dcb57e7cb85 | -7.3105 | -64.6671 | 2024-10-12 00:05:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4cd8ef97-9e3f-3801-bf34-8b6ddc74d5b9 | -8.2046 | -62.8357 | 2024-10-12 00:05:53 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2f025b81-ee0f-33e2-869c-2da71ad08ef8 | -8.214 | -61.1831 | 2024-10-12 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 58884699-aff1-3393-b798-dc1b0655d9de | -8.2324 | -61.2014 | 2024-10-12 00:05:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 92a4fe7c-03bc-3d84-8618-f8bffa015b58 | -8.2325 | -61.1823 | 2024-10-12 00:05:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 5c42e82b-1321-39d0-89d1-c9121f1497f3 | -8.9667 | -62.3506 | 2024-10-12 00:05:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 91a422e8-fd3d-30f3-a0e1-bed6b51781c9 | -9.5687 | -64.1983 | 2024-10-12 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 19599a75-205d-3285-a9a0-cc4f913b8c8c | -9.9243 | -63.8256 | 2024-10-12 00:06:03 | GOES-16 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6c662bc0-da11-3b7c-aad8-15ab15917cba | -9.9244 | -63.8067 | 2024-10-12 00:06:03 | GOES-16 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 836eba27-3c2d-3401-9265-6a4f34091354 | -10.3708 | -61.232 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 37f7ab67-21f2-3e7c-bbaa-954295fefe06 | -10.371 | -61.2128 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 79be1ef3-d3fb-3983-9de0-c26eff7281cf | -10.3892 | -61.2695 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f66abb55-1e08-36ce-9c07-289ae36e3128 | -10.3895 | -61.231 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c7685d3e-fb93-3781-9ed1-e6105dc6f65a | -10.3897 | -61.2118 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bcdef4a1-8c37-33ba-964a-4f2adc03cd02 | -10.3898 | -61.1925 | 2024-10-12 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 26a044d9-0506-3a98-ace5-630d2dbc78a4 | -10.8398 | -44.4365 | 2024-10-12 00:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ca119e98-41c3-3d99-b388-655ec7c30e72 | -10.6535 | -58.7698 | 2024-10-12 00:06:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| de2f5314-ac7c-38d1-a01b-3cab1abe8322 | -10.6537 | -58.7502 | 2024-10-12 00:06:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fd187546-ab95-3ec8-9a76-c131b278dd49 | -10.9506 | -44.653 | 2024-10-12 00:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 43205eb6-3b5d-3f49-a545-1721d9dd5eb8 | -10.8568 | -63.8988 | 2024-10-12 00:06:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5838f672-d1e7-3d3a-99b6-183ee63cbc05 | -11.2912 | -50.9208 | 2024-10-12 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0d0bb9d9-dae9-3a23-9b17-3b2410e30c8a | -11.3102 | -50.9187 | 2024-10-12 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 2f90a17f-6062-38cd-9364-7d74d254fb9a | -11.3105 | -50.8974 | 2024-10-12 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c14d0f6a-8b5a-3cc2-8ee8-e7c92880d1a0 | -11.3292 | -50.9167 | 2024-10-12 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| bad462c0-f0a6-3aba-baa0-e4fb5d2174f5 | -11.3295 | -50.8954 | 2024-10-12 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c3b16826-fb79-3216-9485-6bc369dc41a8 | -11.2761 | -60.5038 | 2024-10-12 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| f672910c-2b2b-332b-99fd-35800affd855 | -11.2763 | -60.4844 | 2024-10-12 00:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2a3b9093-fdff-3ccd-a45f-d5dff6136250 | -11.8188 | -58.8459 | 2024-10-12 00:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| da757a75-af14-3188-827d-4a06e6d3c3e5 | -11.8375 | -58.8642 | 2024-10-12 00:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1f69e2c3-23fc-3a46-afaf-9d42244bb1f7 | -11.8377 | -58.8445 | 2024-10-12 00:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 8420cd76-14d4-3cd4-9fe2-992c4fe480e2 | -11.8927 | -58.9979 | 2024-10-12 00:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 4fd13cec-11ea-3082-a01a-efc56e6a1579 | -12.7793 | -43.3114 | 2024-10-12 00:06:18 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4bbc4e42-7396-3115-8101-da4c1d99b3cc | -12.7678 | -44.8671 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 088984e4-add1-3643-8543-7bc04fcfa9e6 | -12.7682 | -44.8437 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c83ae2c0-010c-399d-8a1d-1b0adc91988e | -12.7871 | -44.8639 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 0d1f13aa-c76c-3bd5-b61b-3f38fb4875c5 | -12.7875 | -44.8406 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 333.1 |
| 9d09bd74-622a-3066-b9ae-7a25944988f3 | -12.8064 | -44.8608 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 6a96177a-c0a0-3652-9a49-0d8f9a96d545 | -12.8069 | -44.8375 | 2024-10-12 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 95ca0d28-75e3-351a-9784-662e0f860912 | -12.5994 | -55.2162 | 2024-10-12 00:06:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f10fac36-e2ea-35f3-81af-bdec9a2bf7d2 | -12.6184 | -55.2144 | 2024-10-12 00:06:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e71b4cd9-31e7-3071-92ab-0232383477c2 | -13.2322 | -51.1192 | 2024-10-12 00:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 44d27b31-e707-3ac2-bf43-ec08659782d0 | -15.6225 | -59.9784 | 2024-10-12 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 948c1a1f-1a77-3a77-b723-cc2c3937b59c | -15.6228 | -59.9585 | 2024-10-12 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0b5aef67-1136-3070-b299-12f5b0578961 | -15.6419 | -59.9767 | 2024-10-12 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8dd3070c-d67a-32c3-990b-1388482b8710 | -15.9823 | -59.106 | 2024-10-12 00:06:37 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8b88374f-3497-3949-aa39-70eb213ec0b1 | -15.9826 | -59.0859 | 2024-10-12 00:06:37 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9d626dda-0f0c-37cf-936a-473131042451 | -16.9802 | -57.4609 | 2024-10-12 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 79056d4d-436f-35a5-8fe5-65ac43e0d0f2 | -16.9805 | -57.4404 | 2024-10-12 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.9 |
| 64d29400-6f36-3d10-b75b-3853bb9835de | -16.9998 | -57.4586 | 2024-10-12 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| d0df28db-7529-38eb-8245-f2d437f8a228 | -17.0001 | -57.4381 | 2024-10-12 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| a993dfdf-be9a-3a3c-b2fc-6c58892c1c15 | -17.0426 | -56.0333 | 2024-10-12 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| c3b76eee-a020-3fbd-8774-1ae93eaafceb | -17.1761 | -57.4585 | 2024-10-12 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 1b59a51f-3762-38d8-88d9-77449ca0c93d | -17.6679 | -56.2435 | 2024-10-12 00:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 8fa3f9cf-f79c-3551-a8e5-707f93960c72 | -17.9837 | -57.3819 | 2024-10-12 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| f9458bf3-3946-3bd3-a817-ae9c4b26cdbb | -17.9841 | -57.3612 | 2024-10-12 00:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 26036169-140b-3c54-9501-9beafe3b3432 | -18.0793 | -56.4182 | 2024-10-12 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| b847e4a0-023a-321a-ae78-a8df82b6948d | -18.0991 | -56.4156 | 2024-10-12 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| e431ccb7-244a-35ba-acc6-a5ded65baf4a | -18.138 | -56.452 | 2024-10-12 00:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| f1f75368-22b0-3dc1-ac90-6189ab824380 | -1.6169 | -48.0269 | 2024-10-12 00:15:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ab1f2235-85e9-3de6-a7a0-2c74bcb8561e | -1.6354 | -48.0266 | 2024-10-12 00:15:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0b1667df-2fdd-3d92-8b8f-f1b34db2ec84 | -2.7701 | -51.3622 | 2024-10-12 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |


[Clique aqui para ver as próximas entradas](README2.md)
