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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e050d40f-2b6e-3769-b986-614cf722e039 | -9.16726 | -60.77432 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7aa8d7a-9c2b-39f1-bd2d-e1f779a71d25 | -7.39035 | -64.34581 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 313d7001-62f7-3f75-8f71-40b825b0fa5c | -9.80511 | -64.25682 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41b71035-0923-3fc2-92e5-b7f2ab10ae19 | -9.81863 | -64.29003 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c25557-7a1e-3c8e-bb17-035ea3aa0b93 | -14.30414 | -60.36806 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd66dec0-6190-3865-9bac-c3edb18a33c0 | -9.2051 | -59.51946 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb0e752-5f36-3277-9cbf-d16af26f3305 | -9.31775 | -63.44089 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de232ab8-cf9b-307a-8b77-f0608471fae4 | -9.18794 | -59.45105 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8247840c-1d45-3737-8447-952b05ff0e34 | -9.04827 | -65.73212 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a95d45a-1ba6-33b3-974d-287151982744 | -7.38005 | -64.3565 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 591b1840-20ae-3b8a-a174-ab7cb6f8ed57 | -7.87886 | -63.01453 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6e478fb-b28a-37f5-ba62-9a82e60c3247 | -9.18279 | -59.53883 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 92ec6dd7-350c-34ac-8f9b-fb624fb899b1 | -9.18127 | -59.45477 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9a46385d-9460-3f2f-a88a-7ab2260c5d3b | -8.81074 | -69.29592 | 2025-08-26 06:03:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bb767f1-903a-3d1c-aada-0ceb97b9256a | -9.79176 | -64.25493 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a9c5475-6004-31e3-807c-fa27bc6f5f4b | -8.11946 | -61.46095 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a556572-79c4-331a-b08d-fd45b9e8fa3c | -8.5527 | -62.64998 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6d1156-9c06-381b-bd47-ad1b658f74db | -9.01064 | -65.69775 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67b5bdb3-b5dc-3e10-9efc-2879d448d8c4 | -9.17732 | -59.53349 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| df08a7ff-a897-3faf-a06e-115102fc07d2 | -9.02585 | -65.70525 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77fd9659-0a7e-3ded-8f81-88b25d10925e | -8.53732 | -62.6533 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8af6867f-2217-30f3-a16b-f8f37345eaa1 | -8.98669 | -65.40853 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6a6361a-4b19-3211-89ef-4ad67eb69b8b | -9.4993 | -64.75674 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73372866-ee74-3a1e-a1f6-f3501bbb5eb7 | -9.17761 | -60.80868 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ab13fdc-e6a3-3e07-a4bf-bc71496d69fc | -9.20397 | -59.51823 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2797c4f-b9c5-382f-9a51-2baf172cad46 | -9.18511 | -60.79454 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7982bb04-cd05-33fb-8ee5-817dc12e3a5a | -9.64254 | -59.63673 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69639f7a-cd5b-35e4-aa16-d7faf76764fb | -8.36028 | -63.95341 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f679d30-de52-3cc5-af75-ab2385fab628 | -8.98311 | -65.43367 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1082816b-0522-3a40-8cd7-3bfe6238c665 | -9.25389 | -65.6256 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64c244dc-5829-302e-b623-77c598d0f038 | -8.12284 | -62.87464 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950e2621-859d-3cf6-8c12-6a0304ea2052 | -12.33523 | -64.22619 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bc35d02-07ac-3c7f-a8ed-8473a10d15fe | -8.24033 | -67.36929 | 2025-08-26 06:03:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78d9490d-921b-3ad5-b6bd-14d69ae72af9 | -9.20014 | -59.50963 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eef21970-2041-3d5e-b1bf-6fea1f22d39c | -8.54519 | -62.63235 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f412199c-1f70-3aaf-9f2d-ad6510230903 | -9.02509 | -65.72334 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d64fc068-f96f-3f95-b7d3-4a2a8be5833c | -8.84601 | -62.44613 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c59ef252-f39b-34c9-9f76-4da262644ad3 | -7.38215 | -64.36041 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4be87ca2-d32f-3af3-aaff-a641b534dc5d | -7.28877 | -59.66743 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bde786b-aa31-3db7-a28b-3a5574ca3f22 | -7.39663 | -64.35036 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2688f8a-f69d-32be-a414-aab1bd5a9e0c | -9.15568 | -59.55815 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df3ffc95-4bb1-3af0-ad41-42af24a910cb | -9.18145 | -59.50147 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc55d20-4e9c-3bf8-9f05-091d6773b406 | -9.2419 | -60.92208 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63bd5482-e021-3cf9-96af-11ea5606857f | -8.98262 | -65.40794 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8184cfa2-1c32-3d6f-9510-2f55b2d59124 | -9.18751 | -59.50231 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd65ec73-cf88-39b1-a442-c3950796986d | -9.20215 | -60.92415 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57f7c31e-3999-33a8-946b-deb319173577 | -8.57689 | -62.6379 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de5d0f3b-41e4-39d4-9539-1d05b90d17a5 | -9.09937 | -62.67197 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9489ec9-5c67-3ebc-a566-a9f05a7ad882 | -9.15768 | -60.78685 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d958a90-c62d-3c45-a18d-e34a0029411c | -8.56135 | -62.62365 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 528e2239-17e2-3d0e-9a41-b75eb2fe9a84 | -8.88654 | -62.44604 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd1570f3-632d-304d-ae8c-948df9f1a9b3 | -7.74787 | -67.15352 | 2025-08-26 06:03:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1893e60f-12a8-3919-8281-4cd2efe85ddb | -9.18367 | -60.80573 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f30228-4589-3e57-b510-19f5023b8698 | -9.01829 | -65.39109 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712ce61d-b74e-37b8-baea-7f1e775a2fff | -8.8701 | -62.45523 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5557e4c7-9d65-3736-b093-3cb0f13b76a9 | -8.99941 | -65.40674 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| becab7b4-c63c-3bda-ae1e-8a769cd793d4 | -9.19064 | -59.52581 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 175853a7-c794-3f69-a816-718d7a23c73e | -9.20865 | -59.44038 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873b5a41-c6bc-335b-8676-98e10896a512 | -10.01285 | -62.38924 | 2025-08-26 06:03:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12ca7ebd-35d9-3dd7-a10e-257c86212b45 | -14.30329 | -60.369 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57939637-8666-3e1f-a04c-d9cf9d44161c | -7.3752 | -64.35986 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4bfb154-1488-31c9-8eca-9760823023cb | -8.12761 | -62.8753 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7f7a4e9-b4d9-3350-9c77-c272dabe87b6 | -9.16675 | -60.77806 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67ef64e2-cf03-38e7-bac4-ae0de6d39dd6 | -9.15684 | -59.54905 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 275895d0-2107-3363-a0c0-9dec3091bcc4 | -9.0403 | -65.73089 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e308a301-08d2-3213-bc98-c7b59dc33376 | -8.34302 | -62.93325 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39d4fd24-d0d8-3ea9-8160-c5792bc5cb36 | -8.97244 | -65.42111 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6cf6e8a-7331-302e-8dc4-6aff63ff0304 | -9.09369 | -65.72803 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32f05352-d1c1-3e31-b65c-bd0c41651d05 | -10.41992 | -64.39483 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c861b1b4-d0f5-32e0-a9ee-ad108eb517be | -9.63653 | -59.6356 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b34548a8-97d5-396c-94d8-0b768ecfb31d | -7.5291 | -63.375 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e238ffb-a090-32ca-8e21-7e68a23521bb | -7.37696 | -64.34794 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef31451e-6e62-3832-aa3f-8c9d65c4e61f | -9.17419 | -59.50988 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4f6f86c-3d7f-332a-8372-6e38a452bb27 | -8.97295 | -65.41753 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51fd287d-020a-3d24-8048-13baa8c2de3d | -9.16217 | -60.76984 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23354d4d-e746-3613-b7a7-53524bf6b5fc | -9.19419 | -59.49849 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84f94ff0-c741-3a8a-aad0-a7ea4b8ba99b | -7.62548 | -61.04501 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9e8344d-a30f-358b-92e8-0fb4cdf877d5 | -8.84525 | -62.45177 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 7e30c6c1-abb5-3cc7-b844-d7492823feef | -9.08048 | -62.66372 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f755a2-d9e1-3750-ad24-c294f3a9e4d7 | -14.75216 | -59.72363 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3c9b60d-5a5a-3e90-a511-54b0ea7d6f2c | -14.7521 | -59.72993 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02a8c609-2803-33af-ba3c-4515ba086f3c | -14.75158 | -59.72906 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 58ead51b-d5bf-37e0-9db5-b8cbae10f6aa | -14.75912 | -59.71934 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8d8c0283-926b-3c99-a3c9-7dbe0c7c8777 | -14.7585 | -59.72504 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a5b78f6-1934-39af-9c75-f85ab6e417f4 | -14.75264 | -59.72456 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 588a7fe8-57f8-31a3-b742-8ed565ffa41f | -14.75957 | -59.72029 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b125e4a-70b5-3ce7-b608-233551f1e57d | -14.759 | -59.72591 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f4b4214d-21a6-3f36-bf34-c0e18ffa7e32 | -14.75323 | -59.71878 | 2025-08-26 06:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66405582-9bfc-3260-b6c4-5cd54adbf1eb | -9.1904 | -59.5201 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c14f7981-56be-331c-800f-9e7ecf4d29fb | -11.1392 | -44.7886 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 4aa72e68-561b-3b77-be8d-775eb2fee63c | -6.2458 | -60.0365 | 2025-08-26 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c3dbe8f4-53c4-3634-be83-d9c6a2a3b5d9 | -11.1591 | -44.7395 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 36922339-5448-3470-b520-d1bea76d1bcc | -8.8363 | -62.451 | 2025-08-26 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 01d3edef-68a5-31ad-a57f-343ea2e586f6 | -8.855 | -62.4313 | 2025-08-26 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c09d2769-bbe3-39ee-a25e-83f1fe39b873 | -11.5397 | -52.14 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3d71d41a-0d0f-3705-b0a5-859a88a283bb | -11.5017 | -52.1439 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c3c9fee5-0719-3f08-9dc0-68a3c8377183 | -9.1717 | -59.5405 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a59934e4-a2dd-379f-950c-5d424e1bd0fd | -8.8734 | -62.4495 | 2025-08-26 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 34667fc6-bfe5-30a3-a0f5-cf08302a5e50 | -6.2459 | -60.0174 | 2025-08-26 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7ce509ea-f3f4-3f23-9e4f-c047131fe986 | -9.1909 | -59.4619 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README97.md)
