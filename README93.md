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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 768d14e7-5b40-3601-9886-8d432c8e037b | -9.0348 | -49.78872 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f5484f39-e3cf-3d22-8b0d-343a55a4af99 | -12.00371 | -50.98683 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 123e91d0-0f7d-3578-9a2d-7e38f321100f | -10.57498 | -52.03384 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27c75f31-81ea-3fb9-9946-82f3adcaaaca | -9.44554 | -46.71238 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea6da837-ed61-35d6-a803-aa181da7a40d | -9.06447 | -45.75769 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd7757e-3273-3c36-85f4-a34b84bf38c6 | -10.29914 | -48.82542 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87bc7610-1eee-3a26-8959-c72753554106 | -8.28165 | -47.46613 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bf4c0a1-551b-3c23-beb5-0bb46b0ac8d2 | -6.19881 | -53.2743 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9bdb082-f7a7-3802-aded-82d496f59760 | -11.11859 | -45.11924 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 949f7e35-7f53-38ae-87d0-d4ce8f8bdbf3 | -8.07908 | -54.75368 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34c827f9-f3b0-3ad9-bcb5-762a9cb0f5fb | -11.25215 | -61.56573 | 2025-09-10 05:04:00 | NOAA-20 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 949e21a0-0f3f-378c-8a83-082ec46e3c73 | -6.84946 | -47.91739 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3525494-080b-3c5a-9496-20ddf5b16152 | -10.01469 | -51.67357 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 868e04f6-f956-3067-971d-09596cb15ae4 | -12.99263 | -48.03197 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c3c2c04-f860-3e24-a16d-d948d9c13918 | -10.56488 | -51.9906 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0a813d7-532b-3ddd-a081-4b15dfd1bafd | -9.09392 | -46.96605 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 38a90228-32ef-3797-ae1c-0971356c435a | -7.70575 | -44.84782 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4672a9f-5865-3455-a366-70f22364badd | -11.20733 | -54.9936 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7fb6c0a-dd0e-36c4-af41-dece93b77235 | -13.19283 | -45.28255 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d7794e9c-680b-3cd6-994f-0564340765ef | -9.44601 | -46.71632 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dce7159-3417-3626-b489-ab12ee6e8261 | -9.05429 | -50.4777 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92b078b-e9d4-3866-b836-817526534de4 | -9.04684 | -50.4921 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8b3705d-52db-3171-9213-dbde887e3cfd | -7.74025 | -50.74049 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffcb9fcb-48bc-3440-97e3-ffdb017fb5bc | -10.5775 | -52.04455 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8495658-db92-3e6b-926f-5f20472fe159 | -11.93909 | -51.0743 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dff5e3cd-b079-3ff0-b659-02b145403530 | -9.21339 | -50.53762 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 525ac9a8-e23d-3015-beee-7311b91e384c | -10.72214 | -48.28929 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 843ebe94-b44c-334b-87fb-e39a9f90ff18 | -11.46327 | -49.27197 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d7b76b6-dcbc-3e79-8f11-899b2d7277b7 | -11.3231 | -46.52503 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe73a838-6645-3069-acb6-015810813b9c | -9.03662 | -49.79108 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e882d719-5ed6-3d37-9675-0de555907edc | -9.0816 | -45.70735 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8aee99e-71c7-3a60-a2d2-f4af40eb49dc | -9.05273 | -50.48098 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5841380f-dc29-3ac6-bda8-11c008f7369d | -9.05369 | -50.48188 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6706b070-e289-31ac-9d35-879f1eb9bd48 | -11.11661 | -48.42619 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd27d966-6a19-3eea-bd4d-2b8559e889b9 | -8.72295 | -50.03946 | 2025-09-10 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774f557f-e097-3805-a231-4db3e8e212a5 | -8.85142 | -47.27701 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52e1ed89-2b75-304b-a7d4-998092123b55 | -8.04405 | -48.66438 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 99df94f3-8cf3-3693-ac85-eef008157674 | -10.72254 | -48.28626 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2a250a2-48d2-3a58-9048-4a0639ffb46e | -8.49207 | -51.33875 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 544446c8-011a-3814-b24d-753be59b3bf5 | -11.12243 | -45.1156 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f386641-64af-38c1-a1db-4c508fa19d6b | -8.08638 | -54.75112 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dabec791-ae7f-3b8f-80de-b4a670e563e7 | -11.16238 | -48.35346 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b91e08-219e-3d64-9dc8-f57234f5ddfd | -9.44786 | -46.70242 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6682d873-a6da-321e-9fda-1a409d10b69a | -7.88903 | -46.26834 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6653099-05c9-37c8-add0-54710a1aebf6 | -12.15352 | -50.61935 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 758751bc-58a2-303b-81e8-806c9f331282 | -7.55071 | -48.22097 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 354c1011-cee2-3018-b7f4-8a2d2e1d583f | -9.21169 | -50.54967 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a296cfff-0640-3e41-ab49-74a9287d07a3 | -12.83873 | -52.94143 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a42cabb-009c-357f-acb5-f68d7b735731 | -5.71904 | -51.66059 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53b1f2f1-3512-34f7-b0de-c6239d010be6 | -9.99427 | -51.70246 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88ed7bd2-2cea-3f62-ba6a-4a83db6a3a72 | -9.75602 | -45.4071 | 2025-09-10 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 48ab175c-b04b-359b-995a-deec63e78d2b | -7.54581 | -48.22035 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0da1402a-a994-3ebb-a273-0ce3037098b4 | -8.08582 | -54.75473 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d9e9001-eab6-35f4-a696-83e295f112ee | -12.00774 | -50.97384 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3b57845b-ec61-310b-a02a-54c10a07625d | -9.99825 | -51.70312 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950834b4-3ffe-3a2a-82b4-5556dbf70d5e | -10.72566 | -48.30177 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea282b42-b0e7-3bf3-9a46-bc73c7583136 | -6.85211 | -47.93457 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 847c7d1c-f834-3bed-ada4-bc8dce544653 | -11.18898 | -48.37227 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7f8a5fa-b9eb-3da6-b685-5ab66b8f58ad | -11.45644 | -43.6314 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5642dde1-2c08-3a98-acaf-571a86b7c59a | -9.15977 | -45.56901 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cf31b4e-851d-38de-afd3-f27690966c6a | -8.05084 | -52.33205 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3014684-3a28-3f2c-abcf-016898876373 | -10.95309 | -46.80038 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5e9e2f4-cebf-3d61-aef2-3eb49e674d95 | -8.98422 | -45.73039 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb3f4c1b-7fe0-360c-a950-60a264778da9 | -6.74568 | -51.95649 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b774cac-6c93-3723-b04e-e245e879aa75 | -8.20008 | -47.15816 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8590f1a4-947f-3d06-97d6-8d0e95ae8fd2 | -13.15344 | -45.28801 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3da17417-f538-3bfe-9fa5-18fba3df29f9 | -8.08976 | -54.75165 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca0aa033-9233-3f95-8fe1-4db20fba869b | -8.05459 | -52.33259 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ff4da9bd-a33e-3c09-940c-65a3dce8a1dd | -13.17699 | -47.25371 | 2025-09-10 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1299acc6-b289-3b27-8259-87b22b642319 | -9.10222 | -46.98759 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df27c2a1-d44d-3e3e-8031-f7549eeed509 | -11.66496 | -46.90116 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64047220-6df4-365c-82b1-ee0aaaab925d | -11.66218 | -46.90259 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be883285-0cda-36ed-90a6-f08b98b7fe21 | -8.51934 | -45.72257 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb7d60e3-097f-3852-8e90-ae6c387d1ac2 | -7.98153 | -46.33199 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08b53c38-e649-387f-b1d1-103de26f12d7 | -7.86259 | -46.25294 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 046f3f7c-0a27-3c23-bc3c-3515ab8a3306 | -7.54198 | -48.24697 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99038799-dd1e-385b-a035-59dda3ffa1b5 | -7.5494 | -44.66116 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66d49921-3b97-3373-9ec1-c7e87416da5c | -9.06125 | -49.82891 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c633f209-4a1e-3ee3-88a2-775c94fcd2be | -8.15757 | -46.0934 | 2025-09-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b13c02d-1521-3bb9-9c7f-76c45abfe7da | -12.02543 | -51.00593 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496935d3-34dd-3817-90aa-f3a5722f91b6 | -11.34471 | -46.53992 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 735a884b-f869-3ee6-9e32-2e32b5bb25ef | -7.75777 | -50.76484 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd2fa1fb-9e07-35c5-8db2-293b29c5071f | -6.19531 | -53.27377 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e385d22a-5632-3dac-b973-20467ed0abf1 | -10.00271 | -51.70044 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cc8e35a-fc45-3294-af14-66938047c165 | -6.85245 | -47.89579 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28e89056-5096-34f0-b19b-39d14de15431 | -11.1594 | -45.28883 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d137cdcd-eb13-3388-8f27-deba0e72c2d5 | -9.31025 | -46.72171 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d347b24-aa72-3729-9c75-489525da0022 | -7.8631 | -46.24911 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7da1ba77-5fd1-3cf3-8af0-0c093410296b | -8.0744 | -48.65598 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e355d96a-ce44-3fd6-a480-86fdb00c4aec | -11.11996 | -48.44 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c70cb7-1b97-3c2d-8bef-f57df8fcf9fd | -8.50175 | -44.72448 | 2025-09-10 05:04:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a6e1a53-e103-3170-85ef-4c3f7336e647 | -7.07547 | -45.2053 | 2025-09-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26cb1120-3307-3586-b306-67a73f4ea596 | -6.486 | -55.51932 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0442b748-a72d-37ce-972e-228c634232e0 | -12.04305 | -51.03788 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9aec635c-f5af-305b-9291-0d3156b1a1d0 | -12.41828 | -44.72968 | 2025-09-10 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81601835-c808-3896-8da6-56a7fd97271b | -9.08202 | -47.05925 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4521857-79ac-341f-b3f0-c87125e27f15 | -8.03996 | -48.65877 | 2025-09-10 05:04:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4655529b-a1f7-3b4e-945e-3b0af1e91e33 | -11.41379 | -43.57382 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d693cfa9-c04a-3371-86d3-006426ef803a | -6.88442 | -47.88345 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 708735bf-d235-32ae-a8da-eadfa2989716 | -10.00487 | -48.08818 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README94.md)
