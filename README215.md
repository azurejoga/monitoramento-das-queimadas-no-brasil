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

## Dados Diários - Página 215

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ec86c9c-c41e-3cd6-a4cb-15ef63dc5301 | -13.1639 | -54.3385 | 2026-10-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 5d993174-a3ff-3250-8f33-b666830b227e | 1.7672 | -55.5463 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8eba9938-a29a-3b93-b585-a310b031c731 | -11.3986 | -47.5635 | 2026-10-08 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f1aecb98-f2ec-3ad3-b5aa-6acc482a9654 | -8.5426 | -54.5975 | 2026-10-08 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ef0b61f8-b804-326f-95e6-c2fb97a73bab | -6.895 | -43.7066 | 2026-10-08 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 518ec22b-9b72-3f86-a1d0-8dde117c38da | -3.1951 | -42.9538 | 2026-10-08 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| de1ff2ee-4ccf-35bf-9dcc-b530065c8138 | -9.475 | -64.3525 | 2026-10-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1c87029c-9566-3afd-82a5-6415f71a560e | 2.7641 | -60.0106 | 2026-10-08 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 7a55a160-6a96-35b4-a963-ce06a7bd5333 | -10.6912 | -47.8278 | 2026-10-08 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 6369c0c7-d47a-3d40-9315-bd4201024503 | -13.1833 | -54.3158 | 2026-10-08 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 410.0 |
| 0bd826df-3947-3f93-8f89-75a0febff76c | -11.3103 | -44.8337 | 2026-10-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 37e10a8a-4f7d-3540-bf57-3ea9908fd040 | -9.4496 | -44.5936 | 2026-10-08 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 39cb0277-17d5-3476-9c21-0013d8694597 | -8.2181 | -46.362 | 2026-10-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 4ce1f98a-613d-3544-ae6f-25bacabc2e17 | 3.0733 | -60.557 | 2026-10-08 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 539969a5-7555-3777-bf0b-625e42d8edef | -9.7689 | -64.9992 | 2026-10-08 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 110.7 |
| edead99a-2bbf-3ab1-b6cd-af7bbdf8917d | -8.6107 | -67.0116 | 2026-10-08 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 2ab24b98-7738-31e2-9957-b16faab2fd7a | -10.6722 | -47.83 | 2026-10-08 14:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| d73737a3-d603-344a-bde9-da7d7718a1c7 | -8.9501 | -45.1334 | 2026-10-08 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 217.9 |
| b58cd811-bd94-36bf-8f23-149b3e685165 | -12.1738 | -44.7517 | 2026-10-08 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| c9f7e00c-1151-3f90-b3c1-909129e81ace | -7.0454 | -45.4351 | 2026-10-08 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 83eb09e6-31cc-3f18-b905-85cf33316b35 | -11.9832 | -57.5867 | 2026-10-08 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 279ada72-560d-32b1-9c61-61a4d7fd98c4 | -6.8952 | -43.6833 | 2026-10-08 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 9e7289e3-b036-3c2f-8d58-dd86882e541a | -15.5222 | -42.6342 | 2026-10-08 14:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 317.0 |
| d9aadb62-1f98-318a-8375-f61803ac5ec0 | -11.9643 | -57.5882 | 2026-10-08 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2ae0d31b-2979-35e3-af88-f38045602771 | -10.9384 | -45.3916 | 2026-10-08 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 91c05b98-dcd0-3089-82b7-0e5be539d1fc | -8.1996 | -46.3415 | 2026-10-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 7c53214a-1415-31a4-9a2e-f8afc88b769a | 2.764 | -60.0297 | 2026-10-08 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 164668cb-8b62-3567-a73c-57943beab746 | 2.7458 | -60.0109 | 2026-10-08 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 133.7 |
| ec42d7a3-d671-3e12-9779-9430219a9a26 | -7.4697 | -42.8315 | 2026-10-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 050acea5-6d4a-31ae-a5e0-f179b6f8cc59 | -3.7818 | -41.6479 | 2026-10-08 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| ae36f3ef-c668-3fbd-aa63-388b32dc3263 | -11.619 | -43.6196 | 2026-10-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 358.7 |
| e6031b95-8204-314a-b49d-8221fd4ae95a | -6.9328 | -43.6799 | 2026-10-08 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 232793d4-e73c-39c4-bb5b-88f2c267fe7a | -9.4492 | -44.6167 | 2026-10-08 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 69d5a8da-5bae-32eb-aa91-d3efa71df472 | -7.0065 | -59.1223 | 2026-10-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 268.6 |
| 90855c4b-7491-3ee3-8c07-48348b3e0d73 | -11.8595 | -47.3694 | 2026-10-08 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 26451dc7-7a07-3a14-adc0-64453ee96fce | -9.4306 | -44.5959 | 2026-10-08 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e4858b40-8094-398d-9f11-1fd834ee3fa0 | -8.6107 | -67.0301 | 2026-10-08 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 316.8 |
| eebaadc5-95ac-3618-b5c4-5dff41f1a4ed | 1.7121 | -55.6063 | 2026-10-08 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f09259b6-aceb-3209-8a11-03e94b04aede | -8.3532 | -47.6568 | 2026-10-08 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| be117ef2-baba-3e29-873e-33f2e1b2b74e | -8.6106 | -67.0486 | 2026-10-08 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 198.5 |
| 147294f5-685a-3251-8a65-6ed41f1e3a3a | -11.983 | -57.6066 | 2026-10-08 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a8d1cdf5-21a1-300d-b5e1-821f6bd57492 | -11.8595 | -47.3694 | 2026-10-08 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 8ce31e41-42a8-336c-aa4f-8404fd3947a0 | -8.1113 | -50.9417 | 2026-10-08 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1e900f36-38ac-3f1d-af6a-52b59f22d52d | -7.4697 | -42.8315 | 2026-10-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| 87d8ce42-fc86-3244-aa0c-f22cc9b54fa0 | -8.5921 | -67.0491 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0304b54a-65f9-31ff-95ba-e1201eee4bd0 | -7.8878 | -54.9822 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 856aca94-37c6-3626-9e2e-30d3cc641ffd | -10.4724 | -47.2333 | 2026-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 21b24a5a-e733-3bad-b826-e3946160d68b | -1.4756 | -54.5565 | 2026-10-08 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 7f2ade64-8eed-3a6e-84ae-12a3f83afba3 | -1.4756 | -54.5365 | 2026-10-08 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e2423a0f-e716-3b81-8b13-16372123010a | -8.2621 | -54.717 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 143ebec4-e6af-3a54-9184-a0ee886431c1 | -9.8442 | -47.4608 | 2026-10-08 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 6ea295e1-30e6-3422-87d2-977f910d8700 | -7.3286 | -50.8314 | 2026-10-08 14:30:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6459d679-0bf6-3cc4-9e9f-05d032d4a3fc | -6.7368 | -55.1074 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| be28f374-0034-36e2-8d6a-d2e86d45cd60 | -10.4727 | -47.211 | 2026-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| f583835d-4abe-3cef-8444-a4120da4b98c | -13.1639 | -54.3385 | 2026-10-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 89744a24-b80b-3a80-be19-4e30f2cb7dd1 | -11.2661 | -45.1859 | 2026-10-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c22ba56f-84cf-3ed9-9752-1a9e67418de1 | -8.1115 | -50.9206 | 2026-10-08 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 11de8f43-422f-3868-89a5-dd56d019f893 | -10.6912 | -47.8278 | 2026-10-08 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 9961a083-4bfc-332f-9c1d-67d58a939134 | -6.7366 | -55.1274 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0f63a0bf-4d0a-30c5-b3ed-bef2772e633a | -8.2184 | -46.3396 | 2026-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ea3bca62-62cc-3b3a-a339-2e96840ab71d | -9.4751 | -64.3336 | 2026-10-08 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3ee3ebc4-65ee-3a63-a4fe-4f4de4089359 | 3.1463 | -60.5937 | 2026-10-08 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3dabe463-11a6-305d-86e8-ba677cba8aa1 | -8.2826 | -45.7038 | 2026-10-08 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 31e7b3b1-13fe-3c52-b9d7-38c0c10318c4 | -10.9575 | -45.389 | 2026-10-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 1b4d3bf9-252d-3fef-8962-d41ccdf4108d | -10.5094 | -47.2956 | 2026-10-08 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| bcc86342-20c8-382b-971e-49d1fe57810b | -8.1876 | -54.7219 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3a1fe8db-b37c-3cc0-9e6b-48fbe4c8c772 | -1.4569 | -54.7562 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3d72b181-6ee6-3237-95e1-0a7ed716bd24 | -7.3472 | -50.8301 | 2026-10-08 14:30:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 625517af-b568-397d-8f70-e9e26a103be8 | -13.1833 | -54.3158 | 2026-10-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 429.0 |
| 0ba598e5-c1ea-3908-9703-39fa3f4fe96f | -9.9018 | -44.7917 | 2026-10-08 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c7070113-0c2f-3411-9305-89d63b93d963 | -11.8415 | -47.3048 | 2026-10-08 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4783fc85-c301-38ab-8f81-a8430c868a25 | 1.6937 | -55.6263 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7a13a438-971b-38c7-93b6-0b1d53dfdc6d | -7.8876 | -55.0023 | 2026-10-08 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1d2aaee5-a58f-3653-8df8-bbb24e396b10 | -11.3103 | -44.8337 | 2026-10-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| b25b227f-c5a4-36b7-b2e9-01e4d943bf2a | -7.0454 | -45.4351 | 2026-10-08 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| fafa325a-a700-3332-b2a9-a46cde8dda27 | -3.1951 | -42.9538 | 2026-10-08 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b2253a79-d71f-3b66-8f62-79ce515ad69c | -8.6106 | -67.0486 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 8bdce438-59c0-36ba-9fd7-5e00481bfa8f | -9.0046 | -65.6988 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c0ffb091-5721-3807-b971-4cfa240c2a57 | -6.7096 | -45.2824 | 2026-10-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 21995619-d33a-322d-882b-e1cf408c6572 | -3.8198 | -44.6095 | 2026-10-08 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| eaa8c82d-180b-3dd4-9285-bcb6c8b232a4 | -6.9881 | -59.1037 | 2026-10-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8bcee8a3-1e67-33f3-8f59-17c3c3e63c27 | 1.7121 | -55.6063 | 2026-10-08 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d81dafbb-c050-30f7-b569-3b6810206e0e | -13.1641 | -54.3178 | 2026-10-08 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 218.6 |
| 3efc69c3-8963-3e73-92b4-d8e103de14bd | -1.5118 | -54.8153 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ea42f418-c3b1-393f-b807-1474b086b305 | -9.0592 | -65.9209 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 5a5b1d96-b429-3713-b2cd-5ad0dc357567 | -9.9589 | -43.5516 | 2026-10-08 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 51f489a5-88da-391d-a7c8-d64fc79df47c | -1.4569 | -54.7761 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| befb0fd3-dde1-38eb-bdd2-8e35c92d0d99 | -10.9384 | -45.3916 | 2026-10-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 546214f6-1f8a-3b19-acf2-93808dedfcae | -6.6901 | -45.3519 | 2026-10-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 7ce07585-e053-35d4-bb41-f4184759f504 | -6.988 | -59.123 | 2026-10-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 84ff3c26-4e1f-326b-928d-fa42c714d8ac | -8.6292 | -67.0111 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 434e6667-68d1-324a-893a-e3446631e7ec | -11.9832 | -57.5867 | 2026-10-08 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d55f16e1-35f1-3116-8c7c-cb99d29587cd | -6.9328 | -43.6799 | 2026-10-08 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| ef3719bb-bb76-3d66-9215-431fa9939fdc | -8.5922 | -67.0306 | 2026-10-08 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6e655c1c-730d-3430-bad2-11f97cac2abb | -9.475 | -64.3525 | 2026-10-08 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 2d4001e6-0d7c-3f34-9f4c-4d6555f0a067 | -11.2462 | -45.2347 | 2026-10-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0cb0de09-3bb2-3a9e-a6d9-f00543b714c9 | -4.3473 | -43.779 | 2026-10-08 14:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 226d1942-4e3e-3aa0-a0f9-0924c016c034 | -6.6716 | -45.3308 | 2026-10-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 0bcf105b-248d-312b-a25a-f9f02549da6d | -3.195 | -42.9772 | 2026-10-08 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| c9ec5cc0-d9ca-3ce8-a607-47a6e347a5ff | -1.4752 | -54.7759 | 2026-10-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README216.md)
