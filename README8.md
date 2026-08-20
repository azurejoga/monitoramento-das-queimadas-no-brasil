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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3f98102-20bd-3215-8701-e7d6642d9355 | -11.1865 | -54.0084 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a44bd5c6-a4cb-3b76-8742-eeb24a965376 | -12.4857 | -54.732201 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d855c35d-4bfa-3d14-b47d-f86d4ac97f20 | -6.6217 | -56.3172 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afa09b44-4946-3eb8-89f1-aa1839224cab | -20.8937 | -50.499802 | 2026-08-20 00:38:00 | METOP-B | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94c95675-bbf5-3044-aa63-658eb609df60 | -9.126 | -51.129601 | 2026-08-20 00:38:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e0ae24-6755-3e51-a9bc-1214a0dbf081 | -23.0665 | -49.143501 | 2026-08-20 00:38:00 | METOP-B | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1cd22535-8c77-31de-8f72-206c9fb9fb02 | -6.8179 | -58.9883 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46ee602e-152f-3d0a-9133-b92d9fca266d | -12.4729 | -54.176998 | 2026-08-20 00:38:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80f21980-d325-3200-9c77-dff75015d316 | -6.0954 | -57.9128 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1310bb18-c00e-3b92-a6de-7249718d17de | -6.3602 | -54.900299 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 065705d3-3315-3821-b198-65f7b14b6464 | -13.4125 | -54.3652 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8df27a07-ba69-3efd-b37e-e0b078a142aa | -6.6951 | -58.944302 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34e02401-8096-3642-aacf-c32865d89dc1 | -8.557 | -55.311901 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a71e04-6d8d-3e05-899c-0e1e83ceb60d | -6.7169 | -59.0896 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 673a3590-3d04-3ac5-afb9-098a4cfb2e50 | -14.0224 | -53.647499 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7a74842-993c-3272-9151-28269c9c5421 | -4.3875 | -55.465599 | 2026-08-20 00:38:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad54cd4c-216a-311a-9287-8e748b97b63d | -13.4251 | -43.828899 | 2026-08-20 00:38:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b3ed66-215b-3754-888b-ff203212dc8f | -7.7556 | -49.219299 | 2026-08-20 00:38:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1465eb7d-5f2f-3c07-9bf8-ed916a4cce49 | -6.6436 | -56.413898 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46a4397-afbb-3845-8998-e7803ced4c54 | -7.5693 | -55.544899 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ddd847-8aed-3a26-b1d1-fc2c4d17a403 | -8.0996 | -51.666801 | 2026-08-20 00:38:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1796f735-8b75-3a2f-887e-394672b0064d | -8.5014 | -54.887798 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 706ce5f8-1f7e-3ea0-ab8b-39cff85a4008 | -8.8967 | -60.5294 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8327f83b-12cb-3d97-8a0a-47698ee43e2d | -8.5466 | -54.770302 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f738f4d-21a0-3625-a1f9-d39dfc023419 | -17.320299 | -43.629002 | 2026-08-20 00:38:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b51f471-db2b-3378-bfcb-33a4272d85e7 | -9.1756 | -57.006699 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae51e47c-8733-3c4e-9e48-a9a91aaa670b | -8.6733 | -54.648602 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c1be4a-d1ba-362a-976d-d4093b4b6cbc | -6.4347 | -52.7346 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b79d5d-526c-3f65-84c2-f2b62d4a12bd | -10.4503 | -54.6651 | 2026-08-20 00:38:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 640f0bdc-0682-308c-8935-bd3cd4a2e0e7 | -6.4303 | -52.7159 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b39f970-164d-37d7-a695-4b20522382d2 | -13.5804 | -51.665001 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4bce707b-a88b-3b0e-9a0a-57e10e18ef8e | -8.4866 | -54.868301 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6fb3e34-8d2e-3eb9-8cdb-c946d72a1132 | -6.3819 | -54.950001 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac4fadb-06c9-3681-b996-47a14112b710 | -7.7519 | -49.2043 | 2026-08-20 00:38:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 44faab77-03e8-3bea-a64d-4f728fc377b6 | -14.4352 | -45.614601 | 2026-08-20 00:38:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28df7ccb-9338-3df4-9de1-487ba1a37a9d | -18.0275 | -44.607601 | 2026-08-20 00:38:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cbf3d96c-f820-38f2-a117-638c34df8780 | -10.2449 | -54.353401 | 2026-08-20 00:38:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb4fd178-f1d9-3873-aa79-e54e3ac0698d | -6.3785 | -54.9352 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58bd3eb9-504d-37c5-a4b9-9ed68636f3b8 | -8.2906 | -62.876999 | 2026-08-20 00:38:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df284891-1997-3015-8c2b-b562c66a4265 | -9.4214 | -60.446899 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d43b12ec-8c14-3595-8668-3a116b00b7db | -6.3802 | -54.9426 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e54cc1-44a2-3d4e-80ef-d811581b0e3d | -14.1523 | -53.046299 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4e7d399-5a36-31bd-b1c6-8b2370e9b59c | -11.2043 | -53.996399 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82e77d4c-7caa-3a01-8e03-d77bbeb4acc9 | -14.4448 | -45.611801 | 2026-08-20 00:38:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fdd8f9b-9d42-3405-9758-9065a8764240 | -7.8361 | -61.597599 | 2026-08-20 00:38:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81c3a1ec-b022-3d2d-aaa1-61298b98b28a | -5.7964 | -55.723999 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa2a2f11-3269-3ebc-940f-90f36bf90fed | -6.3768 | -54.9277 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aecdfcfe-219e-3c19-bbb7-41c9e2e64aa6 | -14.2215 | -52.899502 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 878daeb4-6839-37c6-a30c-368853718346 | -7.7482 | -49.189201 | 2026-08-20 00:38:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c7d4998a-bb9e-378b-8b70-11d334f7ac4b | -11.1784 | -54.018101 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7baf1c-3746-379b-bf4d-a6fe8432f3fc | -6.2406 | -55.412601 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3510e7-2b4b-3bd9-a070-91cac82ecf90 | -9.1235 | -51.118801 | 2026-08-20 00:38:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92616ebb-9a3f-37e6-8d18-05345fd5ea43 | -5.7932 | -55.709801 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f1238a-2068-3e6b-bf39-652d9e29b642 | -12.001 | -53.4258 | 2026-08-20 00:38:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 422340f0-8775-3b2b-b68f-8e1da3bef32d | -17.322901 | -43.601398 | 2026-08-20 00:38:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 271611ba-059c-3892-a899-842ed6372c50 | -8.576 | -54.7635 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974df6a1-1980-3ed4-a41a-0c3943c37e63 | -14.1639 | -53.051498 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58ca22ae-9501-390e-a826-8d1a8b6f2477 | -8.5335 | -54.757999 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2227beec-2020-3e28-bea2-7cdbeed63d84 | -11.798 | -44.781799 | 2026-08-20 00:38:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e3f5d8a-692b-3db4-93c2-85105f6f5395 | -6.7136 | -59.074501 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24a400af-16fd-34b0-a09d-92bb1f0bea98 | -8.5679 | -54.772999 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ffb865-886e-3406-b41d-d52850ec1899 | -14.1754 | -53.056801 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c899c4ea-9f1f-3b56-9625-9ecd6f7357d7 | -6.6015 | -58.9651 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 89038088-8d73-3c79-b718-f26ba3ae26cc | -9.4256 | -60.4353 | 2026-08-20 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| bfa5a4cb-93c5-304a-b207-78e80e844849 | -9.207 | -59.7903 | 2026-08-20 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f168a488-0f37-367f-9682-1c0a6a91a188 | -1.8425 | -54.4917 | 2026-08-20 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 551b1941-0020-3f7f-a50d-1928005d9a95 | -6.6938 | -58.942 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 49caf86a-7b23-3808-94a7-21bad82cb9c0 | -5.7904 | -55.7103 | 2026-08-20 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b8c538cb-e13a-385e-9637-ae0606453f96 | -11.8377 | -58.8445 | 2026-08-20 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2073ec05-2d9e-3a6f-8288-87f2177ca7d6 | -6.4391 | -52.7343 | 2026-08-20 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3c97cf2b-0c5d-38c2-9780-6ae71f47fcfc | -6.6929 | -59.0966 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a98e1936-fa9a-37c6-9321-69f523330c31 | -6.5829 | -58.9851 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0963f180-0850-381f-8c23-bdceb529158e | -7.3413 | -45.8377 | 2026-08-20 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 303.9 |
| 385b3bf5-6bde-3959-8bed-9c4c92b90ba5 | -9.4257 | -60.416 | 2026-08-20 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 156.7 |
| c87eb37f-7734-30ce-89fc-3935804e80e0 | -6.7123 | -58.9412 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d875392b-ce76-3dfd-a30b-cf212bb31d1c | -9.4069 | -60.4362 | 2026-08-20 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 6264813b-1fa3-3204-ba32-bd4a7e0f5884 | -5.8087 | -55.7293 | 2026-08-20 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a1390246-b9ea-3af7-9f0c-745f304fbfb3 | -11.2128 | -53.9976 | 2026-08-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1212c69a-40b2-346e-8974-df52d8e1799f | -6.9128 | -59.3578 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| fa75daee-fd4b-3fac-906f-85f8eef40097 | -9.2071 | -59.771 | 2026-08-20 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 318bd3ca-fa2b-3b1d-b574-5b296bc8f364 | -9.12 | -51.1534 | 2026-08-20 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e99d3871-0b5c-3eeb-8f70-62d0368b7eb4 | -9.2258 | -59.77 | 2026-08-20 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b54f2619-f2ad-33da-85ad-5bd54f3b9887 | -6.3863 | -54.9451 | 2026-08-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 49aab675-2612-38ce-b336-082d8d3f52e0 | -9.4254 | -60.4545 | 2026-08-20 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 08adf04d-1378-344e-ac0b-024f7ecfc0b1 | -11.8083 | -44.8072 | 2026-08-20 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 34dc732c-b419-33d6-a506-3bac81d38593 | -14.1607 | -53.0587 | 2026-08-20 00:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 0a418715-5b1c-3f73-874e-2b2b045dd313 | -8.6727 | -54.6492 | 2026-08-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| f00a0da0-5147-38d3-8d12-0dc3a63ed5e1 | -7.3603 | -45.8136 | 2026-08-20 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.6 |
| 06d4031c-6950-3746-a2a3-6deeb28e5d28 | -8.6729 | -54.629 | 2026-08-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bdb42dd6-ce44-3c50-95e7-5f2544d7fb4a | -2.5814 | -47.2439 | 2026-08-20 00:40:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 82f70a37-5fb9-3e97-aeb0-1bf2303ee2c1 | -12.4914 | -54.7569 | 2026-08-20 00:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e9e5e271-847c-3f7c-897f-b4e5d1e9267f | -17.3372 | -43.6139 | 2026-08-20 00:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 236.0 |
| 87acaf71-a694-3627-95f5-6186200f50bd | -9.2256 | -59.7894 | 2026-08-20 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c49ee195-e409-3db9-a317-83e45b7f9743 | -9.4071 | -60.417 | 2026-08-20 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 113017b5-8f18-37d1-8953-d4249c33d787 | -23.0838 | -49.1511 | 2026-08-20 00:40:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9e186ef3-61a8-37d1-9628-8252ccd59c34 | -9.12 | -61.6011 | 2026-08-20 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1c693207-d1a0-36f2-acc1-3696e4950fe2 | -14.4559 | -45.6019 | 2026-08-20 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e0367af2-956a-3819-8639-40b6cb4f1f2b | -6.583 | -58.9658 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d4e36c02-bef9-3260-a7bb-1290f42d45e2 | -6.7114 | -59.0958 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f690043d-f4a3-34f5-bf04-7f4bf0f1dd1f | -7.3415 | -45.8152 | 2026-08-20 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.0 |


[Clique aqui para ver as próximas entradas](README9.md)
