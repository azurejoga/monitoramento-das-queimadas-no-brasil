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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f10eda9-ea91-38d6-83f8-ca428fbc25b6 | -3.3685 | -59.5036 | 2026-09-03 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 9c30d25d-f74a-3567-8ae8-ca6e3a92ecc4 | -7.3117 | -60.6089 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 87e56854-98e9-3dad-934e-b28e9e81d468 | -10.6472 | -61.7741 | 2026-09-03 15:30:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 66082582-704d-376d-b365-9e7ad13f2d87 | -3.6215 | -60.585 | 2026-09-03 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| daabacea-8efe-3368-bb56-e565857eda68 | -9.4352 | -45.6022 | 2026-09-03 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 19600308-7526-3335-a201-141cb0622286 | -13.382 | -51.3352 | 2026-09-03 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 177.3 |
| a9b28b1f-baf0-3155-84ad-8631e7b9c9d4 | -10.5281 | -49.9778 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ef8c1ebd-c90e-3356-8aaf-078438f5f654 | -3.5528 | -59.0397 | 2026-09-03 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9b82e32c-e597-3fac-b9d9-c6395108fbad | -10.8635 | -45.3101 | 2026-09-03 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e4efabd1-a7a7-3a1a-ba7f-a2e8d31ee2a8 | -10.5278 | -49.9993 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f8672c60-d685-3825-926d-8af14060c20a | -11.7722 | -50.4829 | 2026-09-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2bf8ae2d-68c5-3276-b2d6-eb3e1f0a2868 | -10.8058 | -45.3407 | 2026-09-03 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6a77a530-0248-3e42-8a42-2c647c384174 | -8.7968 | -62.8695 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 61935cfe-7421-35ee-bd8f-e35a9bf0dd86 | -8.911 | -62.372 | 2026-09-03 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4946691b-fa3b-3d65-b8b2-e7712c6ed221 | -7.5326 | -60.7147 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 184255db-cdf1-3772-af6c-e1d845f4a6c2 | -13.6233 | -51.8371 | 2026-09-03 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8f26db74-ff59-3bd8-ba9a-f18945868aab | -17.1227 | -55.9402 | 2026-09-03 15:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 223a7ddb-22e3-3966-9442-2e6c6168f6e5 | -7.5137 | -60.7919 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 81e9016a-12d3-363d-879b-fdc095fb3da2 | -14.2989 | -51.7072 | 2026-09-03 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ce61be77-00cc-3980-8c5d-981b5a81c2dc | -20.8377 | -57.6681 | 2026-09-03 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 125.2 |
| 0a7587ed-fecc-34e5-ae74-880fe3cb1b7b | -14.4201 | -52.5201 | 2026-09-03 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ebf0cdb6-ef91-3201-8c5b-d4b5be9d501e | -7.5852 | -61.2089 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2979fc51-3505-301b-a3d8-85df9288ce3f | -11.6773 | -50.4724 | 2026-09-03 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 59f9e26a-2b5a-3b16-bbd2-441d2de4d1c6 | -8.449 | -54.6442 | 2026-09-03 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6225c7a1-6137-3271-872f-d92edb025c5e | -8.5542 | -63.1814 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 46dc7866-5fd6-35a3-b319-7d2d28bb07dd | -3.1815 | -61.1424 | 2026-09-03 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1b6c3308-55e4-3a88-a362-45b5d708eb01 | -3.1267 | -61.1811 | 2026-09-03 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6a4ee930-f010-3d19-b8ae-d9da63d4d58c | -9.4813 | -60.4516 | 2026-09-03 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8ddc45f3-0da4-3686-840e-f2af86dbdd4c | -8.7785 | -62.8324 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1ebf01b1-3872-3aa7-a13d-bc2480ebe6d0 | -6.6015 | -58.9651 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 2f6dd361-13fa-3d9a-aa0a-c19e58ab1c27 | -10.651 | -50.6697 | 2026-09-03 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| a334b10a-db56-3291-bb77-f57a17b67699 | -11.0566 | -51.4539 | 2026-09-03 15:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4ceeda58-9047-3998-9d95-3ad4d2e2ae61 | -3.7533 | -59.3231 | 2026-09-03 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 37e165aa-232f-3fc1-ae2f-dc0510ad4566 | -7.0242 | -59.2374 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 240e6521-7fd0-315f-beee-5cab6a611d70 | -3.6232 | -54.5931 | 2026-09-03 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7fff0bd5-be2d-345a-95c4-aa8af753b396 | -8.1711 | -45.5792 | 2026-09-03 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f7a8ce39-42b3-3620-ad5a-e6775bd21f80 | -7.3118 | -60.5897 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8c77aea9-65dc-38aa-acd2-53ce53ea4b46 | -3.0164 | -61.4848 | 2026-09-03 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 237c8de3-c055-3be0-a560-10074de66bd3 | -7.5325 | -60.7338 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c4a25bd3-89f7-32e9-8701-a1af171df0ae | -14.2985 | -51.7286 | 2026-09-03 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4296f34d-ffb8-3b07-a9d7-29bbd98504d8 | -7.0427 | -59.2366 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1e700425-c402-3852-a53d-c68ba062e106 | -3.3504 | -59.4465 | 2026-09-03 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3e84be82-43d3-3ef0-8767-4616f0b719d1 | -13.3817 | -51.3566 | 2026-09-03 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b9551435-fd73-3aee-a348-67d6fa6266f1 | -10.2217 | -50.2876 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 4461a6f9-91c7-3e8d-b424-65193bd8a6b4 | -17.0878 | -56.8534 | 2026-09-03 15:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 188.4 |
| abd0cf7c-16aa-370e-b198-33d49a5a3474 | -8.7989 | -62.5095 | 2026-09-03 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f1a7bdfb-c6b9-31a8-ba8c-086890f8dc6b | -8.7613 | -62.5869 | 2026-09-03 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 09a0d986-6f1e-3134-b96d-bb96a7bd01c7 | -9.6676 | -47.9429 | 2026-09-03 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f84c7dfe-6751-327f-a33b-8a37d398d11c | -7.2006 | -60.6706 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 0eb9e9ac-36e0-3d3c-962c-67600311e53b | -7.3487 | -60.5883 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 86e25eec-7e8d-3e83-aaec-7f99a4997a66 | -7.5511 | -60.714 | 2026-09-03 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 07bfbd40-f377-39bb-afa3-6c5381abd98b | -8.5541 | -63.2003 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| eb1378bf-823b-3694-86c2-d9460a8c807f | -6.8386 | -59.4379 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ba9efb05-95d5-3edb-bba2-24c49d7f365a | -20.8174 | -57.6709 | 2026-09-03 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 223.3 |
| ea381330-33c9-398f-9d92-b8c30a791e3d | -3.2179 | -61.2174 | 2026-09-03 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cdb21757-d9d3-32b0-af90-eddba3e99d24 | -3.0347 | -61.4846 | 2026-09-03 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 137.3 |
| c9509347-425f-351d-a005-b2a16565b2a2 | -14.3818 | -52.5039 | 2026-09-03 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8a31850c-5f6c-39e0-afeb-3ec4692e63ee | -10.4636 | -45.317 | 2026-09-03 15:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c9133a6e-f269-3f24-9ec8-a048869dd9be | -8.9111 | -62.353 | 2026-09-03 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d6f093ef-2953-3c0f-980b-18fc5fe3813b | -8.7615 | -62.5679 | 2026-09-03 15:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 7381cc4b-460e-340a-af41-d391c32dd331 | -3.6215 | -60.566 | 2026-09-03 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 7df2e91b-6ed8-3d76-9864-59f0fb562b41 | -9.4541 | -45.6 | 2026-09-03 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9112fd06-d11c-38b9-ad76-e0b48497001a | -9.6673 | -47.9649 | 2026-09-03 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 7aa37768-4784-3c47-9b23-a518f8d90000 | -11.4892 | -50.344 | 2026-09-03 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 26d092d9-794f-3127-82b5-785adf56b4f5 | -7.3301 | -60.6081 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5127f8ab-74d9-30e9-9e24-2817c9befc78 | -9.6293 | -54.3158 | 2026-09-03 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 0634eb74-157a-3b83-aabf-4ddcc6ae0b64 | -3.9251 | -49.0539 | 2026-09-03 15:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a8db1127-fbe8-3e06-b2fb-1c6ea16a1a01 | -10.5467 | -49.9973 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 98d04a75-d468-3ed3-b40e-487f10a69fad | -10.5254 | -50.1709 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 8085446f-06e6-3793-afa1-56e3dc7572d2 | -6.6542 | -59.426 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6f1860d2-4564-3dfe-97d7-d6b0a2a93f9d | -9.4814 | -60.4324 | 2026-09-03 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ae1191a4-963f-37f5-bfdb-bc0824b4fe70 | -3.6216 | -60.547 | 2026-09-03 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d93f40b7-f66d-3ea3-a080-f1b37af2ec31 | -17.0875 | -56.874 | 2026-09-03 15:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| c4a50ba5-354f-3e4f-a80a-ff299612addb | -8.6853 | -62.9307 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5133e9d2-5f93-3530-b419-b08fb1e88694 | -6.7463 | -59.4416 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 227.6 |
| 0c8f5499-e9ce-38eb-ab52-6b7222126f4f | -7.0428 | -59.2173 | 2026-09-03 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1b3955bc-416a-353b-a8bd-19a26ff40468 | -17.0881 | -56.8328 | 2026-09-03 15:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 935fd39d-d5ee-3e37-a4d4-86443a72dd9d | -10.6473 | -61.7549 | 2026-09-03 15:30:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 67419a80-4f2f-319c-a4a0-3fa66609a6df | -10.1324 | -45.8598 | 2026-09-03 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| c8d60a31-a227-3068-8d87-b57bc31a7173 | -10.3583 | -49.9528 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 18253374-034f-39b7-bb77-b575ff548df3 | -10.4334 | -49.9878 | 2026-09-03 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 70665819-e780-37fd-861e-e3f46bd21565 | -10.1134 | -45.8621 | 2026-09-03 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 56d51daf-d931-391c-af49-cece90b14ff5 | -17.123 | -55.9194 | 2026-09-03 15:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 13e9d4c0-0527-3148-a6e6-ee7051fc500a | -13.4325 | -57.061 | 2026-09-03 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 4f9df112-f7ec-33e2-aade-e979b4e68fdf | -10.1538 | -45.6982 | 2026-09-03 15:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ba9b8d6f-5e58-310d-800e-83b47afafa83 | -8.7967 | -62.8885 | 2026-09-03 15:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 92ecd3f9-0373-3d67-beee-d9fbac8f4fcb | -3.3321 | -59.4469 | 2026-09-03 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| fcca8262-2897-386e-8f12-3d38afa05c86 | -8.6317 | -62.5732 | 2026-09-03 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6c31be79-03fe-31aa-a8aa-69140fe95ebe | -10.9592 | -50.2744 | 2026-09-03 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e1c87507-8479-3002-aba4-75e0e2fdaa45 | -7.0058 | -59.2382 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0ae09471-f534-363e-ad70-a982c4922762 | -10.8058 | -45.3407 | 2026-09-03 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 21abb222-8821-3eb2-aebc-48e5b81641ee | -14.5755 | -53.6157 | 2026-09-03 15:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 4e9930b2-9ce4-3859-bfd4-747b57eb14db | -8.7989 | -62.5095 | 2026-09-03 15:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6696a4cd-eed6-3acd-9795-95edf785ae31 | -8.7599 | -62.8332 | 2026-09-03 15:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b7763dad-fa5d-3b52-ac4e-9b36b7e741ce | -10.5467 | -49.9973 | 2026-09-03 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 284dcf48-b71c-3de4-bb21-34c011be2206 | -3.0721 | -61.0685 | 2026-09-03 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8c2d376e-b392-3a83-aa62-c342f4d7f0bf | -6.8386 | -59.4379 | 2026-09-03 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 728c12bd-e121-3fb7-81d1-1707ff73c16e | -3.9492 | -55.7965 | 2026-09-03 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9ade6cf0-aef2-3100-a819-20ef7fff4f69 | -10.7649 | -50.6366 | 2026-09-03 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8490677b-edac-394a-ac07-28a7ac0ffc8c | -13.4005 | -51.3756 | 2026-09-03 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |


[Clique aqui para ver as próximas entradas](README67.md)
