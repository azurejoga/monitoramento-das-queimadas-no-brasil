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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ee42436-1b38-375b-89ac-0c491eb3b137 | -5.5662 | -35.5993 | 2025-11-14 01:10:00 | GOES-19 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 70.9 |
| e70a2605-466c-3c9b-a325-e9768400e416 | 3.0912 | -60.7464 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 017f1d3e-f2f3-3e10-b179-1c056986ec79 | -7.8479 | -44.2865 | 2025-11-14 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 3c02ea9f-93e8-3b48-815c-f1f127231c2e | -7.8476 | -44.3096 | 2025-11-14 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 16007e84-fbf8-3354-a350-2a77d661929f | -11.8677 | -49.2195 | 2025-11-14 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 83ea2564-e9fc-3df9-9253-51b7c3d78ae5 | -4.702 | -46.4286 | 2025-11-14 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2430746b-2cd5-361c-a3ef-d38dacc4dfa2 | -11.8486 | -49.2218 | 2025-11-14 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 307.3 |
| 6a88a70a-4f05-3c70-8d8e-bdd690ec8b80 | -11.8681 | -49.1976 | 2025-11-14 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2e6280c6-4bb4-3e6f-be55-b940ede981d2 | -4.7204 | -46.4497 | 2025-11-14 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7f354310-9fff-3578-be02-1807d00cd3f7 | -7.8668 | -44.2846 | 2025-11-14 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 4f6716b1-a465-3da2-be40-b7dd1e1895d1 | 3.0911 | -60.7653 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 288.3 |
| f7fd84da-f3e3-3d5b-b9ee-292a7e7e59a1 | 3.1094 | -60.746 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c413bf37-25f1-38fd-a198-fd48493c3601 | -7.8476 | -44.3096 | 2025-11-14 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7c39a8f5-3834-3691-8e53-48ae1c7324ca | -12.6749 | -46.7378 | 2025-11-14 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9f736141-67a1-3453-a052-1265edaaba92 | -2.9434 | -49.3655 | 2025-11-14 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 96ee6bb4-1951-3c4b-8915-7fe4e94937c7 | -12.6745 | -46.7605 | 2025-11-14 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e9ab9422-2507-3eab-b8c2-bf02296ef128 | 3.1278 | -60.7078 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2e2d5b09-b78a-3848-ad0d-5e990c16b07e | -6.8856 | -42.8416 | 2025-11-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 39e52347-d7c3-334f-b299-eb8f76938b71 | 3.1094 | -60.746 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4eb622fa-8edf-3971-8355-7cd7a8db26b8 | -5.5662 | -35.5993 | 2025-11-14 01:20:00 | GOES-19 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 125e8bf4-7c37-33d7-9431-2eb7dff722e4 | -11.8486 | -49.2218 | 2025-11-14 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 6ee8e9d7-831f-3a11-95ea-c2e1b36687a9 | -4.7018 | -46.4508 | 2025-11-14 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 70c18047-7d38-330f-863e-054c92803266 | 3.1094 | -60.765 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 277.1 |
| 10c7dea6-6719-361f-9fc9-522e14c9a861 | 3.0911 | -60.7653 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 935cb32d-390d-337d-a6f8-14189a932899 | -7.8479 | -44.2865 | 2025-11-14 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| aeb1bad2-452a-36be-974b-0bdfadf933dd | -11.8681 | -49.1976 | 2025-11-14 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d880312f-d8c8-326e-a0ef-036d6f6cba69 | -11.849 | -49.2 | 2025-11-14 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| c7bc57d9-8b82-3502-b1c4-6376971faa0f | -2.4669 | -48.2238 | 2025-11-14 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 39101015-d686-3678-88a2-5c557d51ab6b | 3.0911 | -60.7843 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ccfcd816-0a17-3d83-9a66-20a20b9df5b3 | -12.7189 | -45.4074 | 2025-11-14 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| fb26c04a-ac5c-3388-be16-478211dfe885 | 3.1093 | -60.784 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 100.6 |
| ce2bd228-d475-3509-9088-8a62e2ccd6d1 | -11.8483 | -49.2436 | 2025-11-14 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9e72067c-6c82-301e-ad0e-f82278cc6354 | 3.146 | -60.7075 | 2025-11-14 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9e9aa2fb-80fa-3438-96f3-c28d9f01f78b | -6.1606 | -48.0507 | 2025-11-14 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2d753d83-a34f-3e3d-95c1-5e7044089f7f | -7.8665 | -44.3077 | 2025-11-14 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| eb4aeb09-d0c5-34af-b6da-8ee483a15441 | -11.8677 | -49.2195 | 2025-11-14 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 165.6 |
| cbae36d6-bece-39fe-a3d4-d2ba9c5ae8a9 | -12.6992 | -45.4335 | 2025-11-14 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3d31683a-be06-32d3-99d4-75736383e355 | -6.8854 | -42.8652 | 2025-11-14 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| a0f18d45-3ea3-358e-ba1d-83589d3b0ad4 | -4.7204 | -46.4497 | 2025-11-14 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 83920fb9-c887-3d61-a45b-4ae356239c12 | -7.8668 | -44.2846 | 2025-11-14 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b4dabd37-5bb9-36ad-97a0-82e14f9e607c | -12.6996 | -45.4104 | 2025-11-14 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 207a3c92-6245-389b-a376-4854b845da4d | -4.7204 | -46.4497 | 2025-11-14 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| cd91bcd6-d5bd-35cb-957e-679e325d682e | -2.4669 | -48.2238 | 2025-11-14 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| dfb54d13-a134-3b8e-8a7e-171ccde317f0 | 3.1094 | -60.746 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 18345266-d63c-38f4-91ee-eb135d04fe02 | 3.0911 | -60.7843 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 05512b06-0e41-35ba-9f03-c73ee267e985 | -12.6992 | -45.4335 | 2025-11-14 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 99e235f7-d435-3ee5-88f7-d2f1b958eb0e | 3.0912 | -60.7464 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| e4412b69-4da2-37fc-972c-16eb9584a71e | -12.6996 | -45.4104 | 2025-11-14 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 186c6e1b-8976-3b5a-be78-12ab43177670 | -11.8677 | -49.2195 | 2025-11-14 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 78cbf1a6-604d-3246-86be-6c778aec4bd3 | -9.6487 | -40.3364 | 2025-11-14 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 2c64a0b1-e1fa-31d3-8483-b8607c93066b | -7.8476 | -44.3096 | 2025-11-14 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 582a8117-dc36-3d13-9b15-463844bb8800 | -9.6295 | -40.3392 | 2025-11-14 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 186.8 |
| d17fb624-c2de-3c17-b812-602bf512034f | -11.8486 | -49.2218 | 2025-11-14 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 324.3 |
| 30a3e506-bb73-3ed3-9594-1f6432cbc09e | -2.9435 | -49.3443 | 2025-11-14 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 341ddeb3-fe34-37da-b7c3-c74f278139f0 | -7.8479 | -44.2865 | 2025-11-14 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 950c2aad-f308-314b-b911-dd4a9e6270f0 | 3.0911 | -60.7653 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 243.0 |
| bc589c25-5177-3dba-889a-9df20b237dde | -6.1606 | -48.0507 | 2025-11-14 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3422c434-ace0-3d44-9e76-20f946e3160a | -12.7189 | -45.4074 | 2025-11-14 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 6ea49add-e73a-321c-84c4-f449bb118a23 | -2.9434 | -49.3655 | 2025-11-14 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bc6999b4-3bd2-3c06-9de5-2d223d66808e | 3.1094 | -60.765 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 175.5 |
| ab9a732d-d679-3350-8cb6-ed76f7306799 | 3.1093 | -60.784 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6a73dc64-ea5b-3d44-9d75-612e15e40724 | -12.6745 | -46.7605 | 2025-11-14 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 08105b16-6f87-3b08-a522-631724691477 | -4.7018 | -46.4508 | 2025-11-14 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ee2644e1-0fe6-35e5-93bc-12ca242d27cb | 3.146 | -60.7075 | 2025-11-14 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b4509bc0-7d68-376b-b48b-6ca71bea6fec | -12.6749 | -46.7378 | 2025-11-14 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e3d13e02-6565-3d81-9b8c-aa60fd1246c4 | -11.849 | -49.2 | 2025-11-14 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8e787c31-aa1a-36bb-a62b-1f0566ab7b06 | -7.8668 | -44.2846 | 2025-11-14 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4b385bea-5b83-3d12-84f9-75f27fcf4d79 | -11.849 | -49.2 | 2025-11-14 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ecba126b-7241-3622-bb1c-d26c701aea72 | -12.6745 | -46.7605 | 2025-11-14 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 61b49e5a-dcec-3222-9f21-84e608525e14 | -9.6487 | -40.3364 | 2025-11-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 257.3 |
| 4cbf9837-59a6-30e2-864d-756fb5fa8775 | -11.8486 | -49.2218 | 2025-11-14 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 248.2 |
| 076ca088-1e30-3faf-b7fa-7b4afe6e400b | -2.9435 | -49.3443 | 2025-11-14 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| eb23616f-8324-3da2-b6ac-fbc9d7703f73 | -2.4669 | -48.2238 | 2025-11-14 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d784b698-3d51-3286-9da9-65a2b2180ae1 | -9.6295 | -40.3392 | 2025-11-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.6 |
| acb1e4bb-aef5-3776-a85d-08d05054a39d | -12.7189 | -45.4074 | 2025-11-14 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| ea59b889-9677-3376-bfea-049d480989f3 | -12.6553 | -46.7633 | 2025-11-14 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8b3d2532-4e3d-39c4-946f-22793fd24b80 | -7.8665 | -44.3077 | 2025-11-14 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e6f6fdb0-456b-3fc6-b11a-9db2e29abe7b | -9.6482 | -40.3613 | 2025-11-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| ab1f345c-c291-3fbc-8fac-d92456dd4732 | -4.7018 | -46.4508 | 2025-11-14 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9c593c88-e4ad-3e9a-8554-4216e41ccd9a | -11.8681 | -49.1976 | 2025-11-14 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1feaeec6-6515-3960-8f78-d9d3886fba78 | -7.8668 | -44.2846 | 2025-11-14 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| cf0aab4c-2a64-352b-9b13-376824dc13ec | 3.1093 | -60.784 | 2025-11-14 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 53f99a3a-8028-3b76-bdb4-8b4b4075ad2f | 3.1094 | -60.746 | 2025-11-14 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| aedbb883-f0a5-38e5-ad09-1587e300ded3 | -12.6749 | -46.7378 | 2025-11-14 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f8bf152d-6678-3a78-9a96-d32b25bd8aab | -2.9434 | -49.3655 | 2025-11-14 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5cc80a67-7cfa-335d-80a9-2f0d6251cf16 | -4.7204 | -46.4497 | 2025-11-14 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a6ef6348-3a96-3499-aa0e-4cdda6abf733 | 3.0911 | -60.7653 | 2025-11-14 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 26274b38-98fa-3855-8556-a3f1548a8000 | 3.1094 | -60.765 | 2025-11-14 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 251.4 |
| 8d368133-7eff-36f0-8d72-bb185b693954 | 3.0911 | -60.7843 | 2025-11-14 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 647708bf-46f2-3cb4-9387-1d4cd5de042f | -9.6291 | -40.3641 | 2025-11-14 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 7844e3d1-e48b-3ef1-a4aa-c9b7470c17d4 | -11.8677 | -49.2195 | 2025-11-14 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 6b372cb5-94f6-3574-9067-6b3dacec4dfa | -7.8476 | -44.3096 | 2025-11-14 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 421adfe4-0ef2-3f7c-b0bc-97f76b6219ac | -3.4576 | -50.11 | 2025-11-14 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 1bf05206-cce6-3b94-94cb-e6808cf5cdbc | -7.8479 | -44.2865 | 2025-11-14 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c829c644-b417-30d1-9f13-6277a176157b | -7.8668 | -44.2846 | 2025-11-14 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ef0e057c-5b22-3cc8-8e0b-2bf783643890 | 3.1094 | -60.765 | 2025-11-14 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 223.4 |
| daef9ec7-ed28-3d5c-8108-bb13daa07405 | -11.849 | -49.2 | 2025-11-14 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 47fe5cc7-0c22-3830-8fb4-cea543490545 | 3.1094 | -60.746 | 2025-11-14 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 651540df-3261-33e8-a907-d15e223ba77a | 3.0911 | -60.7653 | 2025-11-14 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 4bbd61b1-1a5e-3e1d-9de5-3daa6f35128a | 3.1093 | -60.784 | 2025-11-14 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |


[Clique aqui para ver as próximas entradas](README12.md)
