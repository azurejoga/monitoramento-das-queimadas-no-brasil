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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec869160-d21a-3641-93ad-826afea9dc54 | -10.52171 | -57.44959 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e763cb71-7f2b-3028-beef-fd9d52c34811 | -9.86533 | -48.37218 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b613c577-d8e9-38fe-8888-856d389f236e | -5.82077 | -52.10873 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 460d0150-5f22-3d4d-8887-4795565b44a6 | -9.11872 | -45.73652 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73fcf31c-fa5c-37d9-bcb2-3667d63f4da8 | -5.4651 | -44.96181 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 513370e0-7f3c-3954-820e-b740ebd79533 | -8.13544 | -44.85419 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 778e3c34-c879-301d-a887-4c567f9760a6 | -9.18342 | -46.75599 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 667a417a-cf82-36ac-a829-b8da5b566ffa | -9.62184 | -45.37347 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0a9616f1-6d4e-301a-a69f-e04b6c67d314 | -7.07459 | -41.83072 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d3b348c8-a547-39e8-a21d-3f134bf7cceb | -6.94332 | -41.69771 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| afb6cb0c-05fb-3ccd-9292-084d9213cb6a | -9.45522 | -45.45458 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdbcba07-dc60-3c1a-82f5-4c782a11be11 | -6.08282 | -55.54541 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 591dfff9-1197-31c8-8240-8a41b2c0e70a | -7.94212 | -44.838 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1cbd5b0a-d3e3-3b7b-bf4d-75f72985c0c4 | -11.32092 | -46.784 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8cb2ddfc-6ce1-3097-9c04-e3b75fcd8d36 | -8.48768 | -57.63572 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 3c06e419-7c5d-364c-b9d7-be39d30d93de | -6.36334 | -58.28424 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a94a3ff4-de1e-3fe2-b2f1-62d4bc1b2ac1 | -5.64398 | -44.8088 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b7fb2d5a-8325-3270-80a3-b896ca85830a | -7.59603 | -46.13475 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16e2c386-e824-36fd-a3c6-2f2583ba83bc | -8.29336 | -45.64811 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dfbaf8fa-1bce-340d-a5b3-5722c2dfee7c | -10.3908 | -58.3024 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c88b8c21-ed68-3385-b411-3e31fd5c6fc5 | -11.88708 | -50.0719 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f89b1e4-721f-3beb-9030-12be52261e69 | -7.01586 | -43.37834 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2d60a767-cca9-3547-917b-7ba39cc1ee15 | -9.59463 | -46.65446 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4adf06a0-bf5b-35e0-9274-30209b32734d | -6.09847 | -53.54545 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34d5578a-864e-34f4-abef-077ea10baf8e | -11.8888 | -47.59063 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 594a28d9-d9a5-321b-a1da-4fe06c4bf1ca | -5.83682 | -52.03078 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd67f18-2b51-31f8-925f-5845057345b0 | -9.78677 | -46.48108 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77ea404-bf7a-3a1e-a349-3fdd872e60f8 | -6.78593 | -41.46876 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af4ed6b3-c601-377c-afed-c1ff43f7bfe2 | -11.20877 | -42.82504 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e47bdfd-99df-38f0-b355-2744f70aa740 | -6.14907 | -52.75256 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cebad243-620c-3530-98cf-e6d3c8a1cd22 | -10.97851 | -48.30859 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01dd678b-037a-3d26-8fcb-4b5769eca9fe | -5.65834 | -51.89708 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45b26703-6e9c-3fd9-a7b5-20f1b2bf765f | -6.70904 | -58.80429 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a85b24-1bf1-31d2-8c38-5abe635b42ba | -8.47883 | -46.89259 | 2026-09-17 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bdf7bc5-7728-383a-81dc-f42dfd6059b8 | -7.37664 | -44.52001 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbb8049f-bd29-3819-9037-31814839d06d | -7.37369 | -44.48167 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c25ce3a7-2790-3667-8438-70c4d70abf3f | -8.86148 | -45.87109 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8ea4d2c-5e07-3832-a82d-1a48ab0654a3 | -12.50766 | -45.92394 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0400d2b-5150-301f-835a-dc21ccc61175 | -9.12243 | -45.73044 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f683b973-b111-3023-9ca1-a299054362b2 | -10.46571 | -44.94781 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ff02880-e392-3b19-92b4-1acd0c8e9cd9 | -6.66002 | -50.91745 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 093c6d8e-87f1-3673-bb40-4a1536a653d6 | -7.46878 | -45.30427 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 806af4d0-da22-3f54-9da5-0bbaf3350e8e | -5.6408 | -44.80315 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b5456a9e-e673-3da4-8f76-321f5d540e91 | -9.60515 | -45.3463 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 533d3678-deb4-3426-b4ae-46f372e23c3b | -8.91812 | -62.40152 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6db1edcc-4279-3a14-8c44-3d05dfa568e7 | -11.89486 | -43.82323 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb80cb39-9c01-3599-a28e-f035942be93c | -8.83794 | -46.92341 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 473caced-5b97-341a-b588-6c3b657ce824 | -11.5722 | -46.8702 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec6e4792-7a47-3ddb-8d5e-94ed8fea8ac4 | -5.54428 | -46.60043 | 2026-09-17 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27efdb63-14aa-3412-a203-7eafd41f2807 | -7.38643 | -44.51012 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c380f29-33dd-3f4d-b197-13d91517e3fa | -8.02023 | -45.48155 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb1894db-c1be-3d1a-9d74-19f7a397079a | -6.79844 | -58.78765 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d041418-2796-38a6-b707-9ee70f0de8a3 | -7.94297 | -44.83715 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bf75d22d-bd81-3ea2-bee9-fd857b3520ea | -8.94456 | -44.39812 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 298bd710-900d-32bb-9849-80a34844e4b7 | -9.61622 | -45.35503 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4f9a2a2-4b31-3cf8-b005-f502f4749448 | -9.94423 | -45.4447 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf330b4a-566f-3654-badb-a6dc1324917c | -8.39191 | -42.21012 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cad3fbd5-597a-3aa4-97d0-6972d0c6ab58 | -8.37172 | -54.72791 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 242174e9-562a-33bc-94c2-6f0d4158915b | -11.89726 | -47.58316 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 202834ed-96d6-3408-b193-982bc918ab6f | -9.1226 | -45.73711 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9b45518-86b1-3e6c-a006-2537cb4e871b | -8.56458 | -44.5525 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a567b906-5e79-3bba-865f-58b02198de1f | -11.33222 | -47.6548 | 2026-09-17 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df82d4b8-1568-3d74-86ca-046399dba2e2 | -10.78295 | -46.19799 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4d8c8af-bab9-3d29-bc3b-3e972abce7b9 | -11.58154 | -46.88549 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81805d55-6684-323c-885e-51aa43e69017 | -11.5431 | -46.87811 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44e7137a-0dbf-3236-b078-624430e71d79 | -9.38912 | -60.29807 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9baf9e0-211f-375f-892c-6eaca49ef859 | -7.04536 | -42.04753 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 004e12f8-9a21-3bfd-acdf-37e9818b68ef | -11.3165 | -46.78804 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f1f3183-73ff-347b-9a8a-f75cd0bc4260 | -5.61628 | -45.24862 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 335d808b-42c8-356b-8568-c73ead6a3153 | -6.32391 | -41.76284 | 2026-09-17 04:40:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 728f4287-7c76-3c24-b038-06e6eba1732b | -9.48992 | -56.76115 | 2026-09-17 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 815ab268-4fc6-39ce-b067-593f8aeb6c0a | -10.57611 | -57.696 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b26939-20a7-3796-bdbf-2d9154dcc7ee | -7.08572 | -41.8413 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 417dfd68-a86f-3b54-915c-154b95e3777c | -9.9542 | -45.28356 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e2a612d-2d20-3651-9a82-2c8d66486547 | -9.62633 | -45.37057 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f0ada029-c5f0-356b-bb71-d9ae46dc53d8 | -9.25451 | -48.23964 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86ad5aef-ad75-3bd2-954d-c227f27b8da7 | -4.37593 | -55.02892 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f2d89b8-5ce0-3b1b-be41-4028dab3e2cf | -12.14664 | -48.2632 | 2026-09-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0d85eb1a-981b-3da1-956e-3c6c62b674cc | -9.87792 | -48.38181 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 60b6753f-51c2-3672-a9b0-5cfb02b29cc9 | -8.50869 | -47.42064 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c71b5361-6737-3926-a8c4-611d922d02e8 | -10.31358 | -45.26782 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cd2e10ea-0828-305c-a9c5-f1923ea99806 | -10.89948 | -48.36375 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d96ac1d-67dc-38e4-9f59-8df75fe0cf22 | -6.17209 | -44.62301 | 2026-09-17 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e322f3b-fbfc-367c-befb-627577d84de0 | -9.45918 | -45.45524 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b42a357-231b-3387-aa01-795777666e26 | -10.9138 | -46.30152 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8141252a-4229-3d26-9ea3-2b47a392299b | -8.61135 | -44.49271 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b8cdd7f-6526-312f-ab1f-60a9174b078a | -8.56207 | -44.54005 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b911c0f-fa35-393f-b8f4-85b7af4207b2 | -6.37253 | -58.29218 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f1c2861-0a5c-3b35-82a6-d51096dcaf57 | -4.51515 | -54.97344 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86970985-7c89-3066-b792-0e51ea0a15ff | -10.32837 | -45.28085 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd02c724-1bcd-3c70-bca8-9dd7074c64c9 | -5.76804 | -45.11274 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8c5e2370-9c48-3754-a591-eb986c0a4bd3 | -11.89364 | -47.58263 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4a12029-0b8f-3152-b095-3fc12879fa9a | -11.54403 | -46.88015 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 435b9422-c04f-3c71-b214-b806b0abe212 | -8.56595 | -44.48166 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d291eae3-3e85-3f17-8eb6-56e4a72280bd | -11.64478 | -47.33506 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48d9acb2-e22e-39cf-a6ba-d57068cfe854 | -8.37054 | -54.73507 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63ff23eb-584a-37d3-a145-6afc553b5239 | -5.3083 | -56.09758 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 087cfdcf-77ba-3940-9639-bcdcf21e27a1 | -10.39463 | -58.30863 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2c46d0c-d280-3e76-826c-0bd737041b36 | -9.8562 | -48.3863 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d4c498b-a75d-3ecb-8001-8e53c6c9974e | -6.88382 | -45.47086 | 2026-09-17 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README48.md)
