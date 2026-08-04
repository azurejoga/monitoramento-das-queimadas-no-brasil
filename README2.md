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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356ade80-5ffb-3416-a462-6f2153c100f5 | -11.24775 | -54.8361 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e8c06b7f-3e42-3a9d-9c5b-b5ebc8d95a2e | -7.73454 | -55.34699 | 2026-08-04 00:13:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9fb8fca9-6779-3bde-8892-92cfc4527560 | -6.54785 | -55.17091 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c658ad1e-d8fb-350b-9f90-82f3926a4947 | -6.57654 | -55.16063 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b1c9f4d3-f724-34a2-b1a4-2ec4a812111b | -6.72787 | -50.95204 | 2026-08-04 00:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b267e987-0b1a-3d74-b3ed-4ca386d3a55e | -11.1995 | -54.88287 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 6784f5bd-e4ec-3e2c-9d9f-a145a064b7cb | -6.55626 | -55.16341 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 192cc125-ce63-3c7e-afa8-066974c7ba14 | -7.61382 | -46.46303 | 2026-08-04 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2b9f24cc-2bc4-3b5a-977f-004fdda4bd32 | -7.11215 | -46.72678 | 2026-08-04 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 54e60799-5018-32e4-8ff3-f9b22e04b44f | -11.21182 | -54.89503 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d8c2a83-f4ca-3c00-b6f8-33455088b3ee | -6.54613 | -55.16479 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8cfd76eb-6ec5-3008-b41b-f06513c27bf9 | -9.60727 | -47.76839 | 2026-08-04 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2c32b7da-3dad-31fc-83be-83dafc2c1138 | -7.62635 | -45.31785 | 2026-08-04 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| cd96a4d2-8325-314f-8ed4-e05645e479f6 | -8.92319 | -45.21609 | 2026-08-04 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b538a1af-9c78-3bdd-88db-81c8916a4b43 | -5.13387 | -46.19405 | 2026-08-04 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 24556d75-59d0-3d76-864c-08f2a64bd331 | -10.61224 | -49.99753 | 2026-08-04 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d4fef74-67b7-3f15-914e-004b3e781a1d | -9.47469 | -48.87834 | 2026-08-04 00:13:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d85a78c5-580c-3ecf-a844-eeea07840674 | -6.53771 | -55.1723 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7f4b4d01-0cd6-3ba1-bf78-c6bf7785a43e | -5.42831 | -43.43007 | 2026-08-04 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 064a7c31-7fc7-37fe-bf6b-4427dacec23e | -8.98174 | -51.46756 | 2026-08-04 00:13:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6c2a1109-c273-3639-b7d7-59b6f2494121 | -6.99786 | -51.30893 | 2026-08-04 00:13:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 26f8925a-9721-3867-ad23-7f66c767675c | -11.75884 | -50.29002 | 2026-08-04 00:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a51f7e9a-bb7e-3a8f-b8d0-e50149848b0a | -7.60243 | -46.46482 | 2026-08-04 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 65f4fd2f-75e2-394d-85b0-bc80aa4d4ed8 | -7.11083 | -46.71743 | 2026-08-04 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 22336385-c9d5-395b-9cd8-5c03c59d4489 | -8.98296 | -51.47644 | 2026-08-04 00:13:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c46ae9c9-93aa-302b-9556-91c0fcdbb0a7 | -11.19536 | -54.88933 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4942ae0f-9760-3305-8bef-c4623edc0179 | -7.62772 | -45.312 | 2026-08-04 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b0a356b8-9814-394c-978e-3f0e6196f123 | -5.63757 | -47.10168 | 2026-08-04 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9f8fceb0-164d-3ed9-b0ad-e9312474ad28 | -9.4732 | -48.86813 | 2026-08-04 00:13:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 9781c8dd-f822-3169-addc-5f0e5d7de8e4 | -6.719 | -50.9533 | 2026-08-04 00:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 643b654a-92d5-3dfd-a906-d5be6ecc605e | -6.47709 | -42.2396 | 2026-08-04 00:13:00 | TERRA_M-M | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| e426907f-5d81-3e4c-a040-2cb06cc74757 | -8.35434 | -48.23917 | 2026-08-04 00:13:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b7cd3c00-baac-32b5-ab4f-4b910af44ea0 | -6.54624 | -55.159 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a7916bbe-968f-3e79-961f-4ff2d5306513 | -11.20114 | -54.89633 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 74502f87-b349-3592-bd9e-91244b2a4eaa | -11.21749 | -54.85332 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c95044bf-4603-3b71-9aef-f390ddd2aee9 | -6.5446 | -55.15293 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d75ecbe1-bcc1-3cd6-866e-9e9147d69da3 | -6.72662 | -50.9431 | 2026-08-04 00:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e942509-29a6-3ccf-97f7-7eba7396b317 | -5.62634 | -47.10322 | 2026-08-04 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b770fedc-9d22-3097-ad0b-d56db0a854ff | -6.5664 | -55.16201 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a6ffb2f2-ef03-3294-a46f-e4301c5791c6 | -4.63962 | -43.14319 | 2026-08-04 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 9afb85a5-7c28-3230-8b0a-33800c77a8b6 | -9.18039 | -49.13024 | 2026-08-04 00:13:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6fce9aa-62ad-3837-b589-ba602c590526 | -4.63394 | -43.13721 | 2026-08-04 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9c5213c3-a85d-34e1-9e8d-9b1e632e7b1d | -11.21586 | -54.8401 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2ddd7747-a649-38ef-b3d8-a42544d7a230 | -10.56386 | -46.77519 | 2026-08-04 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2117fe5a-2576-348e-a436-dfaf11267691 | -11.91662 | -55.89157 | 2026-08-04 00:13:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| dce541dd-af19-384e-819f-2d3004c09bb0 | -5.25639 | -46.69382 | 2026-08-04 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| cd1bfbae-2e36-3e53-a63c-bc9395d83e3f | -11.20524 | -54.84155 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 48fe9804-d8e0-3396-bfe3-3c4accd62f6d | -6.54765 | -55.17669 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| d4e701b9-d7b2-37f8-83d0-662f8893482f | -11.91858 | -55.90771 | 2026-08-04 00:13:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a65eef1d-be8f-3f73-b361-74a80cf2f00f | -8.35846 | -45.98423 | 2026-08-04 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d68e1e91-7b1c-3852-81fa-ccc75e250f82 | -9.93194 | -53.33146 | 2026-08-04 00:13:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9b366b74-c5cb-3e04-bd8e-f7cfa10d5222 | -5.63369 | -45.93356 | 2026-08-04 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 79b1194f-c737-3edc-83aa-4ac16bb7b12b | -11.12877 | -50.39729 | 2026-08-04 00:13:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d31aece3-c6fa-3a69-a826-1eb68c0c5f87 | -5.62826 | -45.92222 | 2026-08-04 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4de323eb-1142-381e-940e-78922822ae03 | -7.9355 | -50.9545 | 2026-08-04 00:13:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 98de111f-61f3-3131-b4ce-ebdba49f7db9 | -6.53612 | -55.16045 | 2026-08-04 00:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8c528fe1-cea6-3b27-b91b-ceb7d9dbc383 | -11.2085 | -54.86802 | 2026-08-04 00:13:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6ee39dbf-df4c-372e-94e1-cef05d9d0aa1 | -4.2709 | -48.60319 | 2026-08-04 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f016fd83-350e-3043-961e-ebadca146e5e | -4.45845 | -47.9224 | 2026-08-04 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d21127b1-f9d0-3b43-b647-f6a021399c57 | -3.23986 | -47.92824 | 2026-08-04 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cf299eff-a816-30c3-9288-9b74cae9474d | -3.03026 | -48.42228 | 2026-08-04 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6fc8fec5-faed-3848-8215-d716c9cad9a7 | -6.10017 | -55.81644 | 2026-08-04 00:16:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4b4ff358-47b8-3b30-8a12-4f077eddc86a | -3.96818 | -48.12548 | 2026-08-04 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| a297a8b7-2857-345a-8280-d73465010fa6 | -3.03518 | -48.4151 | 2026-08-04 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0eaf2d43-b319-3b50-82dc-f266d3e8720d | -3.11002 | -47.91658 | 2026-08-04 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a35a5dd4-f7e5-3498-ae67-3266b719a814 | -3.67252 | -49.49447 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f1a158f6-c1d1-3925-a4c9-e5cf5a0633ec | -3.67915 | -49.47141 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f7d293e0-4dd8-35a3-b0f4-a560b68d3391 | -3.66788 | -49.46198 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8c4d8102-bc24-33ac-b7de-7aee7c5a25aa | -3.67097 | -49.48362 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| d7dcc693-d8ad-3567-b01d-cb3d57d3315c | -4.89281 | -49.96121 | 2026-08-04 00:16:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 83aafd88-7dc9-3646-9701-065c296c3638 | -2.4638 | -54.67135 | 2026-08-04 00:16:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e5c47476-00b7-3ee7-965d-c4cea335ba87 | -2.75657 | -49.46325 | 2026-08-04 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| adc0a1eb-ca32-3fb6-83b0-1684299543b0 | -2.98108 | -47.73641 | 2026-08-04 00:16:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 65376163-0fec-3e63-8390-b83f5dae2a9a | -2.75814 | -49.47435 | 2026-08-04 00:16:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 43a9b5ce-a4e8-3312-abb6-cfd6fc8441c6 | -4.36505 | -47.76227 | 2026-08-04 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c448bcd9-2215-3e4f-8a69-ca580b101704 | -3.66943 | -49.47281 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 44e747b1-e46b-3d79-b977-eb2a83dadcce | -3.57882 | -50.2652 | 2026-08-04 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 05dc762a-2a72-3eba-9ba5-ee78f929e6ae | -3.65971 | -49.47421 | 2026-08-04 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 30596f1e-ca6d-3594-a554-937d0d7190b5 | -2.46514 | -54.68119 | 2026-08-04 00:16:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 56d5d051-7054-35b0-9460-fbaf3dede4c5 | -4.36705 | -47.77602 | 2026-08-04 00:16:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d2a56dce-3de6-3941-83c4-b365337dad51 | -4.27266 | -48.61529 | 2026-08-04 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c8ab6cae-50be-3b3a-bc3b-2ba3d39b0fe7 | -1.63336 | -54.45562 | 2026-08-04 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0c22ba73-14a3-35fc-b2bf-6be5f509686c | 2.53854 | -60.36904 | 2026-08-04 00:18:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.5 |
| f4e217d0-c968-34a1-8e6f-ec06b5eea142 | -1.65166 | -54.45314 | 2026-08-04 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25ff1927-13ae-36e2-a560-8134a7286a7c | -1.64251 | -54.45438 | 2026-08-04 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a582e5fb-c71d-3c8b-98a7-88f70b0ba4a0 | -1.64382 | -54.46385 | 2026-08-04 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0790dc04-6c1c-398a-907c-f888af786355 | -1.63467 | -54.46515 | 2026-08-04 00:18:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f8b14b89-8805-317c-ab8a-0f20269ee163 | -6.5512 | -55.1769 | 2026-08-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6267c8ad-a6d0-3305-8f18-c9064fb133b6 | -11.2213 | -54.855 | 2026-08-04 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 307b05fc-3d73-3039-b4de-54b43ad1489d | -6.5697 | -55.176 | 2026-08-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b739e1c4-7a7c-382d-a8fc-84e90fdc7e03 | -5.1319 | -46.2037 | 2026-08-04 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 130ce35b-697d-3233-9184-ed22a6b1a891 | -8.3544 | -45.9897 | 2026-08-04 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e3e26558-4f36-34ea-aa05-f68e0ee5ffa5 | -6.5329 | -55.1578 | 2026-08-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 259143bf-b87f-3a23-aeda-9ed60f75d019 | -8.3546 | -45.9671 | 2026-08-04 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 66d3c371-bd36-3d05-9793-9a5199a39bca | -3.6639 | -49.4686 | 2026-08-04 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 54411ea6-1d69-36c1-9c5c-d11fafb697fc | -5.1506 | -46.2026 | 2026-08-04 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 6ad1133f-3043-3795-9095-5629fed3125d | -6.5699 | -55.156 | 2026-08-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 08828178-b52d-3b26-8c4a-fddee466beae | -11.2019 | -54.8974 | 2026-08-04 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 431f973c-408c-3cf5-8a34-6a1e39fb6246 | -11.2024 | -54.8567 | 2026-08-04 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| db12da5e-ed1f-30f6-8ca0-1b6c0f94863b | -11.2211 | -54.8754 | 2026-08-04 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |


[Clique aqui para ver as próximas entradas](README3.md)
