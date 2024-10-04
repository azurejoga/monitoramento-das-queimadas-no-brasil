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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c9a1d83-0818-3a67-8fe0-6d4b4810f844 | -12.563 | -53.13779 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14d39e56-de94-3ac0-bd51-8e94f10f298b | -12.55952 | -53.13725 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e4a40ad-2b32-33b2-8913-95cee6931b03 | -12.55836 | -53.14513 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12a44d8f-361d-30e1-937c-eac2e64c8d10 | -12.55489 | -53.1446 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f14c4f0-b4c8-354d-83d2-6c3ae1b1b761 | -12.55198 | -53.14012 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3b592a2-42de-3754-9d3f-13b3ab5ee876 | -12.55173 | -53.47587 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea0d3fd2-ceae-3bbd-8ba5-820521210ac6 | -12.54886 | -53.47153 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bebdd1b-9a12-3886-8193-10637a693368 | -12.54851 | -53.13959 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b78309d8-7de6-3a98-b44c-fe57ebd79819 | -12.54503 | -53.13906 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5145a7dc-a2a2-36b1-8db3-649089618cba | -12.53079 | -53.26044 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae504d82-5bd0-3ee2-bc7c-9ff07f35211f | -12.52789 | -53.25603 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47d30aab-aba7-3f52-9f72-2bd7d7563de3 | -12.52732 | -53.25991 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbadfa05-a803-3467-ab1b-c63d94749c9c | -12.51422 | -53.14296 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15989d7c-93a9-3c8a-bbae-bb062748a707 | -12.51133 | -53.13849 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 698fe49b-66c0-3f67-93d9-9b6bff51b916 | -12.51075 | -53.14241 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199b4513-366e-36a8-afde-a5fba5a1c8d6 | -12.50786 | -53.13794 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59c2954d-6cca-354d-b14f-f3ceefd695da | -12.50727 | -53.14186 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19aa47b-2023-3880-a1b7-24530833e941 | -12.50032 | -53.14078 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30bb3d05-7a6a-30e2-926f-b776d5e52009 | -12.49919 | -53.5222 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c61aa2dc-661c-3daa-8a40-681621361e7a | -12.49862 | -53.52599 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45eaec36-5521-366b-8d58-388160866344 | -12.49463 | -53.52925 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89bbb61b-d96a-3834-8e9f-aa533cb01a14 | -12.48989 | -53.13917 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 502b5aee-cc79-3aa8-b9dd-8630a207ccf5 | -12.48756 | -53.17875 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2580f10f-5e1f-3158-b1a8-88f080017410 | -12.4496 | -53.45652 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0aa3cfc-a70f-3870-802a-9b61b39c8054 | -12.32028 | -54.08404 | 2024-10-04 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afad0229-e0ac-3f8e-a87c-ad94ef68650a | -12.31973 | -54.08768 | 2024-10-04 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf329112-03e2-3bff-9800-172fea3b929b | -12.31526 | -54.09445 | 2024-10-04 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5976d406-3f3e-32f7-b37c-db1024071a22 | -12.66382 | -53.18844 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3ecbd0-5502-327b-bc0c-80027a27a0d0 | -12.65687 | -53.18739 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde70fa5-319b-3aea-b4c9-f59b20b2a5c5 | -12.61401 | -53.15371 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e7bda5d-b36f-3419-84d2-af6a7b5e2bbd | -12.61053 | -53.15318 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 212151fe-1f08-3555-a950-482edad35b7d | -12.60706 | -53.15263 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 991ec7ad-ea30-3323-a5e7-d7a636e4ad40 | -12.59722 | -53.12299 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2acf98a3-dddf-331f-a5e7-703b2bd73a95 | -12.59432 | -53.11854 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| eaeb200a-061a-379f-a0c5-54866b5be47c | -12.59431 | -53.14264 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf38bc0-5fdc-3c36-9079-ddaa9e895832 | -12.59374 | -53.12245 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3670bd18-6b65-380c-9c03-73a4e61bebf2 | -12.59258 | -53.13029 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bc67b16-4f9b-3d3d-a31f-2de5b8b1f0d6 | -12.592 | -53.13424 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8428a521-3e6c-33b6-baf5-27359e6cd9ff | -12.59084 | -53.118 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0e8ed5a-ee54-3d9f-9dfb-6556a889d898 | -12.59083 | -53.14211 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1497b098-7f6c-31a4-82d1-bd8ca835fadb | -12.59026 | -53.12191 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a26313c3-933c-3800-a829-c6e698ba3f85 | -12.5891 | -53.12976 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa6baa4-9ccf-3715-84d8-138421115357 | -12.58793 | -53.13765 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdb27efa-20ab-3d83-b4b3-8ee3e25ef634 | -12.58678 | -53.12137 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c563f97-753e-3502-87bc-48222db711f7 | -12.58387 | -53.11693 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 772d45b8-ba8c-3536-af7f-dd8d6ce2963b | -12.58329 | -53.12084 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec5d87ea-d28d-378b-8a21-e28a14f9974f | -12.58271 | -53.12476 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d9d04bb-3542-3ad5-b575-afdac89884d8 | -12.58039 | -53.11639 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfc145cc-61cb-3195-94ce-094097087eb6 | -12.57981 | -53.1203 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f240ab1b-3df8-36fa-9476-9dd30081c8b3 | -12.57866 | -53.12815 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24ebc81a-cf50-3423-a27c-80334999aa4f | -12.57633 | -53.11977 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f749dd5-110c-3690-9a10-de3354f120c8 | -12.57575 | -53.12369 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76013a85-a8aa-3357-abac-e2865d8fe1cf | -12.57401 | -53.13549 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baa6a5a6-2970-3c87-b982-3acb6244eb6b | -12.57342 | -53.11532 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ecc2a59d-cc09-3e2e-8a29-a43120c19c76 | -12.57285 | -53.11924 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83b97556-9ed4-3e26-bdd1-00d54d5c4da9 | -12.57227 | -53.12315 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb413bfa-787b-3dec-a6bc-09799d9ee5ac | -12.57169 | -53.12707 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a6bacd7-6619-3337-8a14-4c20af46333c | -12.57053 | -53.13495 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66e916c2-3182-35ae-b846-5ea0a7b3de0f | -12.55604 | -53.13671 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa7bc449-6726-3d6e-a0a0-55f02ab4492f | -12.54904 | -53.11158 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d9dc738-3dcb-3770-9847-b43dc95249fe | -12.54556 | -53.11105 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7be798-4ddf-3bf9-884c-fc7e7d54af42 | -12.54264 | -53.10662 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 432428b7-6862-3f96-ab3e-ee0d1d088d07 | -12.54212 | -53.13459 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f251ecf9-d291-345d-8983-6bfb7a875bf6 | -12.51192 | -53.13456 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a306cb43-8de6-3d85-a736-8c250e03cff7 | -12.5038 | -53.14132 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b23abd4-86eb-35a2-8d7b-1e5c9091aad7 | -12.70127 | -54.10604 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24a46ac7-9960-30dd-8c73-efa48ccbdbf3 | -12.69846 | -54.10184 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c68ae91-c6fa-30cc-b277-d8aad458bd60 | -12.6979 | -54.10551 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6106a727-d0b0-3d4f-b8e4-d4933888032d | -12.69453 | -54.10497 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a635178b-1ca6-3dd5-b1cf-dc0fa57301f9 | -12.6708 | -54.03363 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 535ee7bf-70c9-391b-a7ba-ff673faf9d21 | -12.67025 | -54.03731 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a61e830-b431-3ba1-a42d-9cc5fdef939b | -12.6652 | -54.04781 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e980f9f-abdd-353c-af8b-accb6b66b95b | -12.66183 | -54.04728 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ea5e56f-5583-37b8-a053-ba1194f0f661 | -12.66127 | -54.05095 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d174d0d-17d9-392f-ae11-6e72b6dc016f | -12.66076 | -54.07717 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc173870-a40b-31dc-9fca-6a93da621291 | -12.6579 | -54.05042 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f8adcb12-515b-3345-8ee7-1c6e6519c9b3 | -12.65734 | -54.05409 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a96842e-b94c-3026-9dda-aa402d581325 | -12.65341 | -54.05724 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b26f8ff-3a61-3ddb-af54-08ec2898b0c6 | -12.65286 | -54.06091 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03bd0860-cec8-3c53-a3bf-ee8fe4b012de | -12.61082 | -53.49981 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5222d82f-db75-3c7e-b80f-5eb928c7b6a4 | -12.54543 | -53.47099 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf69be48-6865-3666-bf9d-4aa9b0fc1194 | -12.49632 | -53.51786 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 816797a4-1ea0-318b-b4dc-caeadeb8d725 | -12.31917 | -54.09134 | 2024-10-04 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c614820-b5ec-30cb-b5e7-b32828fe5c5b | -12.31581 | -54.09081 | 2024-10-04 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 30ceec80-b6df-3d2f-8078-64f6f4785175 | -12.26967 | -53.99861 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4337a9a-d7fe-344f-a574-5442d2e60005 | -12.2663 | -53.99807 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e83bf69e-7df7-37b8-b4f6-f89cac5119db | -14.79631 | -53.90371 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01fa84d5-a002-341d-b4ce-604aedfae7de | -14.79287 | -53.90317 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4533a7bc-398b-3417-8829-4a7b3e2a689a | -14.79229 | -53.90705 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e41deb7-0c00-3ad0-8b2c-98ab907a008e | -14.78884 | -53.90651 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae53b0f0-94c1-3c1b-bef9-4c4474511762 | -16.12345 | -53.54947 | 2024-10-04 04:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13e1f9ee-ac43-3862-a9cf-7c362cf4a9b5 | -16.1211 | -53.54071 | 2024-10-04 04:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b308ce52-7f3d-37c4-82c2-8b3a85bfbf9f | -15.79022 | -54.20201 | 2024-10-04 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27684d7d-13e5-3d4f-a206-bbc88bcf0a7d | -15.7759 | -54.2038 | 2024-10-04 04:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dcd80a5-5664-3bbb-8762-d4994b9b1f33 | -10.45551 | -54.23203 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6b826aa-6d89-3445-be71-e06fc9b66151 | -10.38329 | -53.79338 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 332300ec-e5dc-311b-9714-51e11dfdad3e | -10.38274 | -53.79699 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27b08ad6-850f-3dc0-8c6c-501043e2af9e | -10.34099 | -53.76491 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aad172f-cf12-34f7-9bc9-bf9b710f78dc | -10.34044 | -53.76851 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fbca634-7de7-30e3-af5e-d32a6e2b1735 | -10.33764 | -53.76439 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README159.md)
