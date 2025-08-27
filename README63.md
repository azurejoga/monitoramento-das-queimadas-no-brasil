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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c1f3f60-def7-3e24-b5db-898ab97213bd | -9.64452 | -64.98931 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb76d0f7-2536-3bdb-b41e-ffbfa9f2c971 | -5.61211 | -60.24017 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ea31e22-aef9-3d6d-b567-396c94fd19f7 | -9.27683 | -59.78514 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2a48edb-5b70-32b5-bfd1-586c2ba47059 | -9.16116 | -59.54613 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0ac970-0d2e-37c9-9d94-55f0ff520a1d | -12.75429 | -48.2011 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 27d46c75-82d6-365f-a9df-6267a030706a | -10.09144 | -62.90886 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4f7f50ff-3cb2-3dc9-976c-913c0cf078c3 | -8.86039 | -62.44828 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33846dc6-5876-3b3b-a1a7-0d635495c5b7 | -9.1688 | -59.51887 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e99a021-bb39-3ef7-aaed-379796e40370 | -8.89848 | -60.77966 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5812b22c-66ae-33e2-af5a-efbed16637c5 | -9.08446 | -66.06279 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621c098b-b50f-3b8e-8a2f-ad3544c96256 | -10.09213 | -62.90469 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4dccce27-6f96-3325-991f-315b01ea4931 | -9.17726 | -60.86485 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a557a04-535e-31da-bbf9-7a543cc9bceb | -10.42162 | -64.37547 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bcb5db5-7056-3f33-b6e3-01b8636ceb4d | -7.04282 | -59.23764 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86788ad7-f91a-3e6b-ae81-331b504db4aa | -9.067 | -66.05978 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e140c929-1eec-3aae-bc9e-ffc81e5f9e16 | -10.48995 | -51.60031 | 2025-08-27 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 519d3a06-b30b-3320-bb10-95df813d1c3a | -6.79334 | -59.63422 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2d2de2c-860d-3fb3-8b2d-5da92cf2f99f | -9.40969 | -60.51839 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41a29e3e-1487-3959-ac24-5745abd5bcf1 | -7.04323 | -59.19168 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787d52eb-0ab4-3c33-8ffb-b5bd78c35ec6 | -9.4025 | -60.52084 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 874813ee-b458-383e-8808-4f1e554a8ad9 | -8.56141 | -51.35525 | 2025-08-27 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 03f38a1c-4445-35ad-b318-d41e423e597c | -8.07472 | -61.53324 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91e3f2f1-e4db-3059-95c1-261226e300f4 | -7.38699 | -64.36141 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e8e1854-f6bc-3e19-b721-f1d97ab88102 | -5.62161 | -60.24531 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2cd51d-44a0-32d4-85d9-c84ad04fc89d | -9.28014 | -59.78566 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 819481e5-589c-3974-8669-8b8e8a234022 | -8.93519 | -65.9296 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dac055ba-4fac-3aa8-9907-15659e05a835 | -8.95593 | -64.13585 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f043ba0-d143-3370-b412-496d4bd5db9f | -8.21417 | -61.40993 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a714ac2a-640a-3478-b14b-c63f70cd828f | -10.09637 | -62.90114 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 247da1dd-2b8c-385f-9b9b-d24b8bea4870 | -7.4019 | -64.34588 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24485ff-b314-3c05-a5e2-10907dd7a502 | -8.06889 | -61.54768 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 046d8a83-3cda-3ef4-8831-bbb1364885dc | -9.5939 | -55.37464 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ecf3df75-90f8-3763-a3dc-396932ec84f4 | -7.5443 | -63.84835 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17add62b-5dd7-32eb-9447-fa29ffadc4f1 | -8.25011 | -61.46908 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 625af012-5c9c-346c-bad5-b988aa0bd955 | -8.11178 | -61.47783 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ec69d1d-1bcc-3cd1-b0c1-101ebedb922a | -6.90841 | -59.35809 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1869ed3e-4f0b-34c4-b893-ff062627135e | -8.90906 | -60.7777 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe73ecb-8ee3-3652-a65c-4125410aecb3 | -6.94414 | -59.562 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 474b28a1-526a-3394-a76f-c4672a248a7d | -9.18569 | -59.45378 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad91ce1-1b3a-361d-ab5c-1ab32686cbf9 | -7.35031 | -59.66212 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e5e40ba-5cc8-35da-b99b-e243dd96156f | -6.35685 | -55.8019 | 2025-08-27 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46a0c7e5-d925-315b-8b83-ef585f044aca | -13.38824 | -46.90881 | 2025-08-27 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d6d47cb9-a048-3968-9316-4f257995cc80 | -8.96123 | -65.96021 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8fc225b8-9c29-3b42-b257-bbc9b35ddc62 | -9.10108 | -60.31776 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4edbd584-6239-36cd-95a3-f99c8a54145a | -7.42487 | -60.00919 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5abb1e3-5e20-3187-8c52-a7619e1a8d62 | -6.94137 | -59.55803 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5325d91-719f-3c23-b49f-07a103384e59 | -8.93012 | -65.93309 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5eda2a97-5aea-3c46-87b4-8ecafd0baa64 | -9.19086 | -60.80141 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7390b24-e836-3d38-9155-7287dc98da6c | -8.88405 | -60.76276 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67898ead-d439-3a82-90b1-b0189423175f | -9.56444 | -55.37846 | 2025-08-27 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0cc5c3f5-0caa-3697-9f38-8d1f4f1b11a5 | -9.2345 | -60.9143 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb4727bc-096b-33ec-be63-f06686536639 | -9.92213 | -54.72118 | 2025-08-27 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5033206c-2dde-3a17-8edf-a8f5d70a694b | -6.78348 | -59.67531 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e362f83-c3b7-340a-94ef-8589c0b0bea3 | -6.78399 | -59.65051 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd796079-ca90-3f56-9f49-e541a8c2aca6 | -9.08051 | -49.58257 | 2025-08-27 05:18:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d5498b0-19df-36f6-bf27-41ddaff9edea | -9.12066 | -67.70509 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65c95551-5d97-35eb-81f1-9e91f3e86a35 | -9.02405 | -65.69462 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3557b6e1-d251-332c-b15e-5aea4f9a67d7 | -8.47458 | -63.92787 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 631d94dd-18c5-366c-ba6e-e5798f3815bf | -7.47949 | -61.34674 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb348a5-cf5b-3503-9a21-ece04528b681 | -8.34963 | -62.92814 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a08ff1c6-e41c-3756-abb8-cbdf48482d2e | -7.35263 | -57.62877 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74731aff-1825-3351-8e92-f9fbebca17cc | -8.92364 | -65.91895 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ca3358b-4709-3c20-aa21-942c8329c530 | -7.41567 | -60.62583 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5d0ea91-6084-3b8a-ae87-7554d3583dd0 | -9.17211 | -59.51939 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c0afb6-e9cb-38c9-bb62-3be8d1624659 | -9.14986 | -60.78392 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0768da6-ef44-3259-8aa5-75e73adefad8 | -8.88682 | -60.76685 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6293dd3-3d26-3d79-82d7-f9ccc72e0bdc | -9.2647 | -59.7761 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f4da27-4aed-363a-9a32-07b83baefefb | -8.30235 | -46.32792 | 2025-08-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6eb55a3d-e0d3-3419-a584-2fd18a270523 | -6.62738 | -60.01774 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39f6ffe9-90a5-3109-9b95-992da0bddfb5 | -7.3979 | -64.3452 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bffbeafc-630e-3c4f-a366-b2426bd1645c | -7.36331 | -70.14759 | 2025-08-27 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbe2a410-6c2f-3d51-af78-6290746447a2 | -9.18677 | -59.44681 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89f5f4bd-b705-3ec5-9c4b-baa94b1d8241 | -7.37437 | -64.36292 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bd46b3-09a9-3e1d-a672-7910b42a4eda | -9.19335 | -59.64384 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d03dc368-8203-34a9-9ece-19ea42a45e63 | -9.40804 | -60.50733 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 638a6850-fa24-3c30-a9ff-585c551b2153 | -6.79185 | -58.99239 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fcd889f-627e-319f-991a-170ee52600da | -8.92651 | -65.92815 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe06001c-0b81-313f-95a5-71dda86661f3 | -6.91117 | -59.36206 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aea4264f-82f9-3769-ace3-e1c4f52f28ef | -7.17915 | -59.73464 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51905351-7e66-32de-8e86-2febd0a0f8fe | -9.19752 | -59.79051 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00a1f0ca-6bcf-342f-981e-28762667a6a2 | -6.69986 | -58.55568 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807c0cba-ce7e-31e5-af19-fdadaa9919e2 | -8.95836 | -65.97699 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d389b69-1242-3e43-b31e-c74e533750ee | -6.82315 | -58.9654 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32ad391-0695-3f7f-9883-e2b7aec881e5 | -10.27715 | -64.49272 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 780114b5-7590-38f2-9ace-01d9f66b0396 | -9.08069 | -65.71596 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cb2b6be-e240-32bf-a0fe-0754155bc48b | -6.76748 | -59.66924 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee060d4e-0a77-3b57-800c-4aeabe2357e5 | -8.93951 | -65.95641 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 9ba1836b-788a-3f11-95bb-8c5a61cf75bb | -9.39586 | -60.51978 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c3e46e-bfda-3cbf-a83a-440e9175de2a | -6.94799 | -59.55906 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e8a1a88-75e5-35ac-8e90-e3af0d70ff4f | -9.63669 | -59.63594 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32976e0c-c25e-308a-a7f2-a17498196dec | -6.62461 | -60.01372 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef85d444-628f-3fb2-b4bc-c577d52b711b | -6.82207 | -58.97231 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3efb240b-733f-39cb-be7f-007552f94a9f | -7.62271 | -61.37312 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b5b28b4-1a5f-3d29-9060-16a8fcb0e8b6 | -9.41136 | -60.50786 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d39baee-e925-3cc3-917f-fa444a7b8872 | -9.03017 | -65.72836 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db9c0ff6-f5f2-346b-967d-3c1e99c2491c | -8.91858 | -65.92242 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff9689e3-9552-3430-8e62-c904055bb2ee | -10.27162 | -64.50188 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36dffce3-14d4-3672-95af-d853a4ccd219 | -9.79852 | -64.26795 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49f829be-4fca-37a3-a1c1-e8af139cf0e2 | -9.89322 | -64.09471 | 2025-08-27 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b115ea1f-de6f-3fc6-935e-3bfa13901119 | -8.85752 | -62.44369 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README64.md)
