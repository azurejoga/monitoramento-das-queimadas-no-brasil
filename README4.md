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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f79a6a59-6ad3-35e1-8f6d-ef1afea6df4e | -7.2013 | -52.6066 | 2026-10-02 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1b10facd-6ded-38d3-ab09-12d9d4701af7 | -3.1299 | -53.7633 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| d07da888-95de-3bc0-8d89-6ce0b302c91a | -6.0072 | -53.5528 | 2026-10-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| dcd99ceb-8d43-3847-9c58-e66c078b3ed8 | -11.4695 | -43.4062 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 309ca950-fe59-3fe6-a380-bfe032088bc0 | -4.2953 | -49.1021 | 2026-10-02 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 212.0 |
| 4f08d0fe-5994-3ed2-9a89-4f3506944040 | -12.8059 | -51.4489 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2ec2f7c9-8fe5-393d-8c6f-688013aab3b0 | -3.2951 | -53.8395 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 57239b61-e5d1-3acc-b9da-c8c461576a83 | -11.4955 | -47.462 | 2026-10-02 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 152849cf-b9c2-3044-b989-bc4ca22bae40 | -11.1424 | -44.6029 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 446.3 |
| 32fdf17e-cc4c-3638-af0b-43c768f77ce1 | -11.142 | -44.6261 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| e24d4b40-e403-3c86-81b1-84e4b47307b3 | -13.3287 | -43.8573 | 2026-10-02 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e89e9239-361f-3a91-85d0-a6e8489ce3bd | -2.0394 | -56.8593 | 2026-10-02 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| f17dbc31-ce2c-351b-b326-c7595df0b40e | -6.8952 | -43.6833 | 2026-10-02 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 84e60688-20b2-3674-87c2-db4d7c46e396 | -11.7738 | -43.5482 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 61705f38-20ae-3cf6-9497-75acd9f50f91 | -5.8966 | -53.4975 | 2026-10-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e6fadf80-ec31-38ab-9670-c485d4ed118e | -9.5146 | -45.3427 | 2026-10-02 00:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 88064097-d13f-3aac-ae4a-dda7c4ce8b27 | -11.7541 | -43.5749 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e9ed4b4b-0d5b-3bfd-8e41-47382ae6d580 | -6.9143 | -43.6583 | 2026-10-02 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 70697a4e-30da-33bf-8c44-51d44f2c3a15 | -12.8247 | -51.4679 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 2798802e-8493-3e0d-b52f-6a365174e609 | -11.4764 | -47.4645 | 2026-10-02 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 178.4 |
| d7bad960-98e1-3fd7-bf3b-5a2f10a98cc3 | -12.825 | -51.4466 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1e956132-dbc4-39ca-9670-fb93095fbd7e | -7.0478 | -55.6302 | 2026-10-02 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 83a71a2d-6db0-3475-98b5-6cde14ff0609 | -11.7733 | -43.5719 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 9ced34c1-550c-3322-be62-b1851e6db585 | -12.8056 | -51.4702 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e454e920-7a35-35f9-bd1f-9a49743b9009 | -11.1427 | -44.5796 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6d4ac586-a8c3-377a-8705-13aeb920a16c | -3.1483 | -53.7628 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7ad5141d-d12d-33a9-b3f0-b9b26b24dddf | -11.1232 | -44.6056 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b7f13122-7b4c-3977-8d7f-e8d0d67a9f23 | -3.1299 | -53.7431 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| b4ba0a95-8bdd-398c-b5e9-5e914d4718e9 | -2.0393 | -56.8789 | 2026-10-02 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c2403f35-5e99-3d4a-b1f7-b4143f7e0a03 | -11.4768 | -47.4422 | 2026-10-02 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 18ea0ce8-c252-32a1-bc09-4779ec72198d | -11.6977 | -43.5128 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| ef082a8b-8bda-3bb4-ad6f-dfefed1570c8 | -3.2767 | -53.84 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| fad6e1a7-5012-325c-ac44-c51d2832ba6c | -2.8897 | -54.1313 | 2026-10-02 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 27f3ff54-68b2-3c23-838b-ed8bf911cb2c | -4.2676 | -50.7506 | 2026-10-02 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| c88edad1-7364-3e86-8c76-b51df4052d1c | -3.0008 | -53.8874 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 41e2ebb9-89ba-3869-bc80-0912acc1aec6 | -7.7219 | -54.8114 | 2026-10-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| f02f8ea9-7e4a-3b1d-b47d-c1f472e8ce61 | 1.8037 | -55.6051 | 2026-10-02 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f4bbb082-9553-38fc-bef3-4736e8f2b00e | -11.1611 | -44.6234 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 65f045e8-a251-3017-bbb6-a41e7770417e | -13.3676 | -43.8504 | 2026-10-02 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2433a493-a1bc-329c-a804-f7d12bd845ca | -3.0192 | -53.887 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| b45c102f-d06d-356a-b020-cc168dc2d025 | -13.3486 | -43.8301 | 2026-10-02 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 997d83b4-289f-31f9-af07-5938556d898a | -2.8897 | -54.1514 | 2026-10-02 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 611a6d6d-428c-3e2d-973b-d825938ec96f | -3.1483 | -53.7426 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 9da50a3c-db58-3505-8d5c-11814ef117e4 | -4.2954 | -49.0807 | 2026-10-02 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| ec995d11-7b50-35a4-b338-2f2fa6a49076 | -7.0477 | -55.6501 | 2026-10-02 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 69cdc48f-5927-32de-9dc4-691e705db58a | -3.1839 | -54.0839 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ec05cd52-ed02-3455-9303-e8c802c56341 | -4.286 | -50.7707 | 2026-10-02 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d4331067-5f07-3fc5-93f2-b5cf55022aaa | -6.3952 | -56.4158 | 2026-10-02 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7005a318-f1c8-30f2-b088-45eb6b206cbf | -18.6573 | -41.6456 | 2026-10-02 00:40:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.4 |
| 4e0bf793-a34b-3eaf-9984-6e80b31091c2 | -2.0576 | -56.8786 | 2026-10-02 00:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4fcfa0d5-48db-3b7a-b9af-da97c2ebe578 | -9.5149 | -45.3199 | 2026-10-02 00:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 9b2a91e9-6576-334e-9de9-1fd28f1f8a8e | -11.4499 | -43.4329 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 46d01e54-c356-3796-9312-d0d8170df0a9 | -11.6964 | -43.584 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| bade5648-b035-33d3-962c-a55f6250ff2b | -11.1615 | -44.6002 | 2026-10-02 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.1 |
| ed2d1912-974c-3f69-a3eb-fe4afc2d581d | -11.4691 | -43.4299 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| bcb5825d-3b6f-385b-85c7-4905dd1f6f15 | -11.7375 | -43.4356 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| bf98a9cd-158d-3c6d-9792-b2ea68df70c5 | -11.7926 | -43.5689 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 520570dd-459d-3df0-afb9-c55e18339840 | -4.2677 | -50.7297 | 2026-10-02 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ff3e405e-3857-31af-b42d-322bcdd7f159 | -3.295 | -53.8597 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 42c15bc6-1f70-30d9-a502-08f2744f519a | -3.1655 | -54.0844 | 2026-10-02 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 66f71c32-01a3-3999-859c-2ba50171fa22 | -13.3481 | -43.8538 | 2026-10-02 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 301.8 |
| 2ba66356-e7f8-3c6c-9c31-5433030ae049 | -11.8118 | -43.5659 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fc864e31-bbf0-35c6-924a-d21dba28bb86 | -11.6959 | -43.6077 | 2026-10-02 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 308ea24c-de6f-3e6d-a542-93490ed584f7 | -13.3476 | -43.8776 | 2026-10-02 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 176805f5-d3c9-3436-8dfe-05c5a45eaf38 | -7.7405 | -54.8103 | 2026-10-02 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 17a7c980-f6f6-333b-a286-82e1cd19a0a4 | -12.7877 | -51.3873 | 2026-10-02 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 129be14c-fb65-3197-a8b7-786aaca19f7c | -8.0853 | -54.9034 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e227bd7d-f5b9-398a-98cc-6738c26ab0ee | -6.4354 | -55.8214 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dcb8473-b664-3239-93d9-24d5c78ff40c | -8.245 | -54.664799 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a32131-8771-33f3-8447-2fcc98e1cd78 | -5.9063 | -53.5051 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e3ec947-eb48-3b0d-9e1d-e23df2a134ae | -5.7499 | -55.7556 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439784a8-8572-3653-b4f8-039098f4a0b7 | -8.5449 | -54.5811 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3474774-5ea5-3158-86c1-3ef2dd6e880f | -10.8173 | -51.106701 | 2026-10-02 00:48:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1e9cacd-2914-353e-8471-f402d6b82fba | -7.5484 | -55.031799 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76bcf8e-8748-3024-91c0-87dc134170a0 | -4.689 | -55.8018 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f8ffdf5-bb9a-3f3b-9ff5-a02e8d85c295 | -7.0518 | -55.6357 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1ff857-6529-378f-8b5b-58d31d5d2e7a | -7.3384 | -55.233398 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb105ee-f53c-3115-ad1b-7339ee636594 | -4.255 | -50.788502 | 2026-10-02 00:48:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f23957c-379f-3d04-a65e-19f811927ecb | -7.4051 | -55.6031 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cddcbac1-db74-330c-a663-b604d52c3336 | -12.8005 | -51.3922 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c944ce7f-953c-3c37-bdc8-d3f7afe928cd | -8.2555 | -54.751999 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f207d745-213c-3f52-a634-928c1220ef49 | -6.3426 | -55.3396 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4ca35f-1bfe-3dfc-866c-79e982eb2d67 | -7.6388 | -55.0648 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840b5948-6497-3ffe-9aa8-756389f06199 | -5.7401 | -55.7579 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f48f944-cb60-39a1-a9a8-e6cdbebc7359 | -6.6645 | -55.087299 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a21394a-9573-3a07-81aa-527823dea1a9 | -8.0731 | -54.895401 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec049d7d-48d4-373a-992e-0a5bd9cae9a3 | -6.2494 | -57.771 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5470dba4-d410-3f8d-a8aa-cc072b001ecf | -8.2678 | -54.760201 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c627df-9378-305f-9d01-63952fde0b62 | -4.2895 | -50.804001 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac66a03-8a2a-30e1-bbf5-d4c2a0a97386 | -8.0828 | -54.893002 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d31a1075-4198-3537-bfe8-d8737cc42b6d | -5.8698 | -50.197399 | 2026-10-02 00:48:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef6ef9f-f0c5-30eb-8ffc-e2f69502a713 | -5.7378 | -55.748001 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ccd938c-7890-3ddd-8d82-6c7115c80385 | -8.1966 | -54.721401 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c3b06-51aa-3f68-abf0-3dae324b1238 | -7.4995 | -54.999599 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb3de22-38c8-3658-a543-c9da053ea825 | -11.4756 | -47.510101 | 2026-10-02 00:48:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b49d9f8-145a-3738-bed5-65940fb5f5fd | -5.9813 | -55.381001 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3634dc4a-69f5-3b99-afd7-cf8f7d1970b2 | -7.3212 | -55.2481 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb60b7f-c959-3f03-892b-7bf5c209f6dc | -7.8216 | -55.139702 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05c35a2e-0080-3bbc-bc93-ea4fd375be18 | -4.0633 | -51.137501 | 2026-10-02 00:48:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55deb2ca-a59d-3986-9c6b-ac52fa9c2e36 | -7.0466 | -55.657299 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
