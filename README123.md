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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea5d79e3-3a27-3009-8d4b-3603b342476a | -6.12141 | -53.7476 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 35f8ea83-6cef-366d-9c94-38ff82ef2008 | -10.50629 | -64.51277 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c89391a-e460-3dc4-8a0a-5ba7eded8a7c | -6.15788 | -57.78642 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e428eb20-47b2-3bf0-b3ba-bdede88447d8 | -6.20669 | -55.41234 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 89627627-eb9c-31df-bcbe-13a499bcb9a9 | -7.57847 | -61.38747 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91142a9c-ae1e-3f38-8a30-d4e054ffc20e | -7.59106 | -61.33388 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 66f9f2c6-78ae-3986-aa4a-a9ef5567ff62 | -4.30289 | -59.47614 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 943fcea9-646d-3f30-8909-0ff0d5011bfb | -3.94567 | -56.01424 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f497e431-558f-3d8e-b7ac-0f0a0b12bb2c | -6.15947 | -57.79695 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 417504e9-f1cc-3a8a-9aa6-1694641a627c | -9.87116 | -60.29847 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| c936e5af-36ff-3560-9b4f-826ff4814407 | -7.62488 | -61.34446 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ff4eba74-73de-377e-b28c-64e467167cb2 | -7.00485 | -59.52278 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 294ff768-0975-3b22-896e-9bba260bbf5c | -8.7903 | -62.47808 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9576a0b1-458a-312b-a28a-dccda22b5e2a | -5.78632 | -57.60144 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d803dfe5-e7b2-3dd0-b913-f088d0ae3a6e | -6.84083 | -55.60759 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 000dda03-bdd4-3d37-8b97-9ebcfbf3902a | -6.3755 | -54.95624 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ec41802d-8dfd-341d-b1f8-850946140a4c | -8.24994 | -70.10573 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 469705c2-7f11-3b2c-80ef-5a74af00f4f5 | -6.43003 | -55.52529 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cca8f913-04bf-3147-99ca-c6edd079fe95 | -6.28254 | -53.14007 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 99acd0c0-829b-3b3a-b58b-c4a130ace197 | -10.76366 | -53.9733 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 27f26233-a5f7-354a-a07c-ed28aaa635dd | -8.60428 | -54.7882 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f3981a78-5662-35b5-96b2-61b9ef8d56b8 | -8.58889 | -54.77929 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2e626c33-2404-383b-980b-f1cd546ea8cb | -7.5019 | -55.28018 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1b947232-d3f6-37bc-92ef-f4663303fee2 | -6.1574 | -57.79789 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2360bacd-e37c-3b4f-a74a-60e81066623a | -9.2592 | -57.07342 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 5f81a314-6f61-3e8c-9e46-907b0a1e7a81 | -6.51189 | -53.60223 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| eebb1ce2-e358-327f-b463-ee0eb95354e6 | -7.55337 | -57.72822 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f3a8d5ab-65ba-3540-9ad0-f88a5be9a63f | -6.04388 | -57.96342 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5b81a76c-81a2-39f1-8935-307cf13a0dde | -6.18374 | -57.75377 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 64a63e1e-c890-3460-af5f-e075e131f2df | -6.93399 | -42.72394 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 2fe502db-62bd-33cc-82f5-2094feb02622 | -9.02972 | -69.57861 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 02176c25-1f45-39f3-befb-8f1f7c59b015 | -6.97582 | -55.64539 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95fd8006-f42a-3569-a174-92880dae8196 | -6.22801 | -55.61711 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 048219ae-4cbf-3328-85b8-d2d08f0b66de | -6.52406 | -55.25312 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| beac88d4-53cd-3de6-8976-c50e5aae3c51 | -9.47098 | -51.69878 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4f140f93-e728-3338-b36e-b5dcdabafb86 | -4.97103 | -44.89095 | 2026-08-28 17:28:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cd51f743-af7c-3695-81e0-9b6e29b40be4 | -6.52752 | -55.25583 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ffdc1e2-314c-37e0-9869-fadf8318699f | -7.49504 | -55.28533 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 567fcade-50a0-3023-83fd-3e6fd00ee9b7 | -6.06925 | -62.00139 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae0aaf97-d5f2-3c3e-a13d-05f68f86724f | -10.51101 | -69.35178 | 2026-08-28 17:28:00 | NPP-375 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b82f0021-98d1-3059-aaba-c49942f0948c | -6.21402 | -55.48209 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 85c05203-ad94-3740-a486-bc42d8cfbd2d | -7.55282 | -57.73252 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 9bbd63be-679c-33a1-b2c7-27890a2b8a8a | -1.87798 | -44.82851 | 2026-08-28 17:28:00 | NPP-375 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 70780af1-3e47-342a-8e12-b98a8a13565e | -6.51552 | -55.24316 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 86ee0e1f-49c0-3a54-8597-7d6512b29cbe | -8.97967 | -50.78224 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 92978688-3108-3d58-b616-cbb9ec1fbb22 | -8.98769 | -65.43938 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 535f7558-c7a7-3fa8-915c-d0effb9e9cc1 | -8.5278 | -69.98299 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d1246cb5-e439-346e-a0bc-40377405a078 | -6.13256 | -57.67968 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eed2b1ae-e59b-34cc-becf-b8c9210507ca | -6.74717 | -58.72415 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f2576c87-da2a-3423-883b-4cf96bc74843 | -4.43676 | -55.63033 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ef422674-4e94-3344-90c9-db639436b2b1 | -5.99962 | -57.67198 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f73a7f8c-7f12-318b-83c5-67926d9abda9 | -6.80958 | -59.61259 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ecf90991-1b83-3921-a9e2-ed8b7ecb0b64 | -8.767 | -50.49309 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 96897812-f48a-3a4b-b3ba-579c2a787a5c | -8.53231 | -55.26639 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7ddcbf04-0c12-3929-b42c-257109eb86ea | -6.76019 | -55.69422 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a843194-354a-334d-9ef2-2f56566e1e13 | -6.79697 | -58.98938 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 63df3b8d-205b-3b42-9292-ca88a4d2b03c | -6.33481 | -57.74518 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6aa77061-f405-389d-8868-7b2db1a78223 | -6.24423 | -57.70158 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| f750d9d5-50e2-38a1-99e1-80be537dea53 | -4.05924 | -56.23249 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f9a8b637-b7d0-3785-8cc8-242b1b487ceb | -4.31037 | -59.47887 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48cc3a1a-c8b1-3463-a245-89cc58ac7c2a | -6.80543 | -59.6091 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b535d56-6692-3bb1-98b2-66c81c7e612a | -3.71083 | -57.22544 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 689700a8-f307-3420-a0db-f93ebd202111 | -6.28181 | -53.13549 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 44c0620b-b42c-3ee4-aa70-49a00771d1ca | -10.14295 | -68.59805 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ec5b5b4d-46d8-36cf-b656-06df0c0f695e | -9.17429 | -59.56038 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4336be0-88a8-36fa-bb75-ad5f055c243e | -6.52064 | -55.23106 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a93c143f-0f31-3386-8844-f02a0b17c7b5 | -6.58012 | -55.43478 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| cb2ff040-a7f3-390c-aeba-2edc47f21d62 | -4.51973 | -55.93858 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 18c4c7cd-71c9-3f11-9265-a4b943cc6c8a | -7.02825 | -55.68773 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 232b721d-9398-3093-9819-82346d683205 | -10.57006 | -59.6074 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 93bbaad1-cfd8-31fc-aedc-cdf1c84cb476 | -3.93542 | -59.32916 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0d9571c0-8752-321f-9f73-1262e618fed8 | -6.5453 | -55.10171 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42615fdb-9c21-3707-bd85-dc61dfc21784 | -7.48975 | -61.40781 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 94e09531-46ab-3711-938f-24bccf8fe2ca | -6.14534 | -57.85367 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 899c6564-d3a5-3f89-9a44-29bdf729b5b5 | -8.99302 | -65.43867 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f91dda1f-9436-39d1-aee9-a1f978c71bc6 | -6.36497 | -54.75579 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1aae776-941e-31bb-8ed4-764eda1841ac | -6.79796 | -43.55917 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 97f5e0f2-a4f9-364a-9652-a2786c16803b | -6.07616 | -59.98123 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca6e2260-1622-3108-83ff-fe1f18af355e | -4.19737 | -55.23395 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b6ab8da-cb24-3fb1-b7d3-92e763658684 | -8.76337 | -50.49774 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b1a7ddb3-bf32-31e7-8b29-fccafd197be7 | -8.33752 | -70.28405 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8a6988ba-9a3e-36da-883e-9abd2c484e1a | -6.65012 | -58.49396 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e0f93340-b308-35d7-989e-24ffe2dc4535 | -9.91664 | -60.42839 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 34d80a05-63fb-33e6-9eb4-1518e812d8a1 | -7.48181 | -61.40893 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8926a232-83d9-3f44-b312-6ee5a82fac11 | -8.08973 | -51.66703 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1cb0fa2a-deae-3965-92e4-14a62b89a5df | -7.50247 | -55.28378 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a7cc43ca-47d7-3df6-9591-987ff9d4e8f5 | -7.61374 | -61.35126 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c2d65bc0-1816-362d-86c2-354796de0c59 | -8.10751 | -45.4739 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd267182-1359-38d8-8fe5-c360270733a5 | -6.18002 | -55.46499 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a619a42c-92a0-3793-b358-e7d97e826749 | -5.91511 | -61.29808 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8aaa6c8c-4da8-397c-b3a6-d10f2e435e55 | -8.21522 | -54.95704 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 47a795a5-500e-37e5-944d-09c0d717637b | -4.14561 | -60.76473 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7478fd16-3335-3029-a419-05a92908c74c | -8.50367 | -55.32612 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bf8bff9e-ada4-3b2b-ac92-442d3cab8fac | -6.72678 | -59.65729 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8715fabc-7f3e-3951-b598-7fa1342602ed | -6.53602 | -55.24322 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| ff8f5a9c-0845-3315-9e62-c0f4b910217a | -9.92572 | -60.43699 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 17538a64-bf0b-3858-b3d0-08cd036c113d | -7.45912 | -61.39148 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| cc16f1b2-242c-314c-ab55-ba6605b944b8 | -10.51493 | -59.63206 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0e985c8d-9946-3af0-8488-aa1038eeae77 | -6.94574 | -58.95535 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 95a8a702-4d5a-3e54-b697-8a858079c9b8 | -3.70803 | -57.22942 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |


[Clique aqui para ver as próximas entradas](README124.md)
