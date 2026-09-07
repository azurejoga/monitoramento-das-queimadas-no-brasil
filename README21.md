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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 963203b2-f934-3efc-ae78-66fc801062a4 | -11.52848 | -49.62724 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1987647f-dec1-3d6c-8570-e2c12160ad6b | -4.34491 | -56.28351 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 132dd3f9-ddfe-3abe-8e7e-d9d030f4378f | -4.97784 | -56.29099 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31922b91-9b14-31d7-854f-ef4c29f958dc | -8.73012 | -62.44233 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae41c53-ccdc-3193-951b-b785a08d0768 | -3.78707 | -58.8527 | 2026-09-07 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4df3b2cc-1034-3883-9e03-615e17e61c13 | -5.37235 | -56.02974 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 632b6d96-8cb9-3dcc-8b72-c81b9f576bbe | -11.03603 | -44.34332 | 2026-09-07 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dde662f-bfcf-3fb3-b697-29cf85a0e35c | -6.13079 | -57.74038 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5401d46-c291-37e5-97f7-694f339f297a | -6.43892 | -58.15431 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d19ba18-e97a-3b66-99df-cf2cf6edaa12 | -9.93812 | -48.04965 | 2026-09-07 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 533bda69-fc27-39d7-8264-142703f161a1 | -8.72416 | -62.44474 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb4783d9-e963-35a4-97b7-7a4fbd037107 | -3.70326 | -58.93379 | 2026-09-07 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a6f68bf-3756-3e82-a163-94327b95fd46 | -5.30271 | -60.14886 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2c556a6-2e5f-32a7-bdb0-564659adbe8a | -11.32635 | -45.05985 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1ef5c40-3fdb-3114-919e-271a46cdd397 | -6.64118 | -59.44266 | 2026-09-07 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e21a702e-d994-31d7-86c2-8a6d7c60b8cd | -4.66895 | -55.63341 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cca452ab-52f3-3e89-a434-b4747d2234c5 | -8.7648 | -62.41735 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eaedf2d-1f16-38dd-aef9-e32d61c7b664 | -4.09794 | -60.66589 | 2026-09-07 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b828e98a-b645-3880-b527-ccf22e2dcae4 | -9.743 | -43.40799 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fc7334d0-ea6d-3259-834a-b0526de4795e | -5.32368 | -55.8764 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f03bf444-cf26-3470-b3cc-f8d07eb17c0d | -8.75985 | -62.43055 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffb01f7d-b7fc-3eb5-b4c6-cfa07bf2f4e4 | -5.15881 | -55.96647 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c631bf7-32dc-35e7-9ecd-ee22eefeaae4 | -5.98861 | -57.6935 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be5950dd-121a-31b5-8432-f3d4b4972601 | -5.85076 | -52.04745 | 2026-09-07 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e7f1858-d2df-3ee1-9c4c-f742012aad3a | -13.30318 | -45.23375 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ee2be115-f48b-3d7c-9c21-85eb45c2cecc | -4.9779 | -56.28868 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24ca4b25-185c-3e99-96ea-a3a14cc7c13c | -4.46994 | -55.08924 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6249505-2fe1-35d0-b793-c2d2a8faa09a | -4.97481 | -56.28564 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 053708a4-6840-3f09-96d2-a571d3676159 | -5.35826 | -56.02288 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b01e49-4e76-3f96-aaaa-0acdbfe4f1ce | -6.06639 | -57.79991 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05dda88a-3cc8-3e66-b149-1ddb137b38ae | -6.34718 | -49.884 | 2026-09-07 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f970297c-083f-3d05-8159-948b378d6e78 | -5.29095 | -60.13042 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 110653cb-d9bb-3477-b7b3-7521017ead83 | -8.49961 | -54.6511 | 2026-09-07 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d157ab76-5b48-3b0a-9f68-3984ddd509b7 | -11.505 | -49.61704 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 443d1682-e84f-386d-a707-2184ace3e280 | -9.73726 | -43.40778 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 939fa2f5-4b92-3f0c-9cf7-1337d88ec328 | -6.44597 | -58.16318 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2854ab2-2d2a-3e4b-b0fe-9b7978d189db | -6.10669 | -57.65942 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f6263e5-2597-38f5-8c9b-e2a524f252c4 | -11.52421 | -49.61993 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b09e71a2-d2c8-3d22-8fad-b2bb57188ad4 | -5.55248 | -60.23913 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f2acdaf-92ad-3a5e-bd19-b3b61c018225 | -5.36865 | -56.02913 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c03f1ad-c47e-34df-84e3-235d4a125e96 | -4.3796 | -55.69218 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65da5255-0134-34cb-a553-b30781efbb55 | -3.78681 | -58.85447 | 2026-09-07 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031250af-4a2e-324d-bdbe-d6fc87290ab7 | -11.51338 | -49.61341 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a43e45ac-57ff-3e9b-af64-eac69dee721e | -13.30436 | -45.22389 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 20acd699-50aa-37d2-8cce-b9e67065eb7a | -11.51653 | -49.61878 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| df7f7761-6a88-3c57-bfc7-26baad013a57 | -6.13284 | -57.74776 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a86a30a-8a2b-3d6e-98f9-f23571dd31bf | -5.14174 | -55.95479 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c2d68c-9af2-35c9-8f1b-7fc15bf9a4a7 | -8.52792 | -63.88785 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 107dd0d4-ec89-3f2a-b23e-9502d167f549 | -3.7667 | -61.75537 | 2026-09-07 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65e81e0d-8175-3fc9-81a7-9400c91d98a0 | -4.66966 | -55.6291 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7991c00-c6fe-3765-8a4e-ac0a4152a62b | -8.76166 | -62.43404 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb39edd2-1eb9-38e9-9064-d4e493432a03 | -5.1551 | -55.96591 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bb8bc16-adc4-3ea6-954b-c535fb7df683 | -5.35607 | -56.03604 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb5528f8-46fe-3d57-ac96-f02bc6568956 | -8.52446 | -63.87397 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82680760-10b1-3927-bebf-ce1220dcfa46 | -5.36567 | -56.02413 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07bae2ec-abd4-397e-9ae8-f9daba14e661 | -11.27817 | -45.1013 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38e8e740-072b-3805-ac4e-78d03c9f5e46 | -8.75454 | -62.42942 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b513a2d5-0114-3a3a-a386-ceb2b7244bd5 | -5.15284 | -55.9566 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbe7c6d-1243-3eaa-b095-2444b105574d | -8.76516 | -62.43166 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a5587b-f756-3b98-987c-91f0abb207cf | -11.51723 | -49.61396 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 69b338aa-696f-385d-89aa-208bd1658ce4 | -4.67993 | -55.6352 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69c82e75-d5d8-3852-975f-e058a323839a | -9.24735 | -46.6908 | 2026-09-07 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c95e387e-23c1-3c47-a62f-f4d4e1c20f02 | -5.28469 | -60.12253 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bbc53b54-cc81-3abe-a0e5-7f4e7e885f77 | -6.01822 | -57.69127 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2b11e07-1044-308e-827c-8d7bba9149da | -6.0217 | -57.69545 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c3b78dd-505d-3932-8b01-256b3fe9d029 | -7.10215 | -56.5115 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bba34839-27d4-3be0-85e0-e149b56cb1cb | -6.44181 | -58.16252 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 636ac44e-da05-320e-8005-e14c53eb13cd | -11.94289 | -44.85954 | 2026-09-07 05:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50468281-6d12-3196-8aa8-968ceba3e494 | -7.10139 | -56.51596 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1465e488-56a6-3556-bb3b-fcd8e52ff715 | -9.72588 | -43.40647 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75e71b08-4ce2-3dbd-ad70-c7a94794670b | -6.05348 | -57.80163 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e3cb5e8-13d8-361a-89fe-14b3ebfe1d55 | -5.36051 | -56.03227 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9951d90-a403-3f8a-9853-51b950ee217f | -5.36639 | -56.01976 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b102ecb4-af2c-3bdc-8400-cd31e2ee984e | -9.73983 | -43.38767 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c140c612-79cb-34a8-bcf8-12ddc94e88c8 | -13.30377 | -45.23396 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| cb02a116-6456-3ee7-b43c-0fe392f9cd05 | -5.27195 | -59.96378 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1249a89a-ab27-3eb5-8872-365e2b48087b | -4.12158 | -56.34821 | 2026-09-07 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 26417144-d776-31cc-915f-63226a3d0756 | -11.65029 | -52.868 | 2026-09-07 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d40ce535-3033-3a59-af2f-9b41eaa082e4 | -7.10424 | -56.51381 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc0db59-36be-3cf8-bb22-e2a5c64b120a | -7.11034 | -56.50827 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b77c46e-9bc4-3b56-8844-2cdb13a3ecf2 | -3.61287 | -60.57498 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e6087dc-422c-3040-91c1-f860e3559006 | -9.73414 | -43.387 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d08e0084-8140-326f-979f-663000408787 | -5.29259 | -60.13488 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0436524d-a531-3c33-936e-5df407c6e82c | -11.65085 | -52.8644 | 2026-09-07 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 080b67f1-6fa8-3274-b92c-449dbe88dd00 | -4.95584 | -56.259 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 667d3b04-8b5a-3789-aa3a-61e4ed66ed16 | -3.61337 | -60.57195 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9d2939e5-f811-3c4c-929c-c3cc259199f9 | -6.13498 | -57.68964 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 378628ff-89a6-369c-a9d8-de19a06eba49 | -8.76103 | -62.43738 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eed23448-8af6-34ca-86ea-393e25e14e22 | -4.66602 | -55.6284 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbbaea90-fb24-3444-9c13-7b049c59e813 | -8.86978 | -62.35461 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69e26153-0a04-3d36-ba86-126136ca5cc4 | -9.51269 | -41.98806 | 2026-09-07 05:04:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9988da5-e88a-3801-9f30-c857263e47de | -9.96853 | -47.98379 | 2026-09-07 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df00ca2b-dbee-3ff9-ae38-80eef96be324 | -13.30336 | -45.23724 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 80c028d4-97ed-3b6f-9e59-462b8310785c | -5.14544 | -55.95538 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c026a225-3545-3529-81b1-d52a3fe3f091 | -5.59621 | -60.24689 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edbbc52b-55ef-3193-afa9-9e2fa83031a8 | -5.35978 | -56.03665 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc79183c-ab75-3d12-9405-419f220bc757 | -5.99325 | -57.69073 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e841d733-dcf2-310d-ba69-aec62d3551ca | -5.99089 | -57.70488 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a98e436e-20f9-329f-91f5-815edb0def8c | -4.6646 | -55.637 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e2ca4b-db62-338a-9060-c0764bb3eb6a | -5.36378 | -49.19924 | 2026-09-07 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README22.md)
