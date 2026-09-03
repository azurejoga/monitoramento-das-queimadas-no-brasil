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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 835f0a54-be19-36e2-99fe-cf4180b4c7b0 | -5.21127 | -60.0433 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7389b248-a021-3686-a502-b6b676b51795 | -6.8041 | -58.9801 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19906cdb-bd4b-3c77-b12b-7f36eee99bb8 | -5.26549 | -60.18836 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c4aef0b-7cd9-31f4-b7bb-a17f89fe504a | -6.65086 | -59.44842 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07702c6c-b6d6-3762-a39d-3bd3092d8328 | -4.41774 | -55.7743 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1599a80f-5802-3d47-b913-4e293e50c972 | -4.97144 | -55.8413 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 395c5401-9024-3aca-8ec8-0bccbc947522 | -6.76547 | -59.43411 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79b1fb52-ae4b-310f-ada0-fc8023aa1ffd | -7.34368 | -55.21171 | 2026-09-03 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259651e3-ca9e-3f00-a2af-4a9a4abcbb16 | -6.11258 | -59.96843 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e0b3a8b-03e2-3ad3-a466-77a42836ed3d | -3.62111 | -60.57015 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f8f6883-6ef3-3bf4-b3eb-b5fdae0e8a69 | -6.32305 | -56.05425 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa2728dc-1d82-35e3-9bab-93eeed01536a | -7.08401 | -56.51748 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c666b3d-596b-3348-916a-21e8a67e9313 | -5.20773 | -60.03909 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c0ac5c0-27ff-3109-a28f-eba2160cfd07 | -4.24194 | -62.23547 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4b1af15-60c3-36e9-9213-c9811968afea | -2.92719 | -54.09549 | 2026-09-03 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41ca6b5e-cd30-34ca-949d-35a7c1167d72 | -3.78588 | -59.71626 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5343884e-79ca-3297-9b89-943630dd035b | -3.74557 | -59.32309 | 2026-09-03 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5baecbfb-aa0a-34d5-9e87-5958ebccdd54 | -4.24134 | -62.23944 | 2026-09-03 05:42:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b73ed0c4-9c40-39a6-9f5f-d5c9a5cbc801 | -5.59221 | -60.20053 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e39ee939-db21-3642-b227-5fa572e88699 | -6.84593 | -59.34748 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0223f65f-9544-3c08-aa0b-21c77e812c2b | -6.69115 | -59.94193 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| afb15020-044d-304b-bd6b-668e09a771a5 | -3.6194 | -60.5553 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07dab526-be53-3734-ac3f-199a7153cf50 | -6.62922 | -55.24078 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787b3fe1-cc22-3d6b-9e38-c820b27f0618 | -3.61798 | -60.56481 | 2026-09-03 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1ec05d8e-f478-3159-b4c2-f91fd4b07335 | -5.47041 | -60.06325 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e8c3b13-a110-3e30-b930-e2ac96776b4e | -4.96949 | -55.85509 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6a61dc3-9ce7-3037-be79-7a6fc52fb911 | -6.76426 | -59.44241 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ed4bbcd-2821-3794-baa7-1f480b11be51 | -6.62295 | -55.24393 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7942792-2581-3db9-9fce-851dfe5231d9 | -6.68752 | -59.93759 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fb5d3800-3352-3208-a7e9-476e815e0f51 | -4.96901 | -55.85849 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edf5abde-51b9-37da-8a46-6a274fb18579 | -7.08486 | -56.51896 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70181390-7c67-333d-a00e-4d6735479c08 | -3.94695 | -62.97428 | 2026-09-03 05:42:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce4cf1fa-89cd-3c26-8110-da6bb2446b25 | -6.76054 | -59.43759 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3342193a-4d70-3371-989b-7add16b22a39 | -6.11312 | -59.96474 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b436b2b-8b35-3000-8216-222bfdfced53 | -4.3601 | -55.77214 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4608c6a0-2e88-379f-b646-4ec69b6f2895 | -6.67577 | -58.76728 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5adb2ece-fe76-3231-9d4c-c699bf7c1a1b | -4.9641 | -55.85439 | 2026-09-03 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a8ff56b-254f-393c-a1c7-3a0f7b542fa1 | -1.50885 | -54.96286 | 2026-09-03 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 555178dd-71ec-3aec-a502-07a51bcba6b4 | -6.68586 | -59.94894 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4d3b55db-ac36-3621-b960-23c1b804d9bc | -6.30772 | -56.04507 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5d45356b-cea0-3fb5-af44-6af30b5dd645 | -6.68545 | -58.76408 | 2026-09-03 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32677c0a-9e0d-3c21-875e-a39423c727e5 | -7.07872 | -56.51657 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 023c3ae1-5b9b-30ba-a7e1-c86e847b7168 | -6.11366 | -59.96106 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c2949dc-82c4-3ba0-bed8-adfb4b51608f | -6.76486 | -59.43828 | 2026-09-03 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09c32a34-9460-3abf-8876-3bada9ce57a1 | -7.08002 | -56.51486 | 2026-09-03 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aaa6f5e8-6ad3-3ea0-b2ca-45e3a9c0e744 | -5.25539 | -60.19126 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7bf7429-4fb5-362c-b629-ec90e3a32275 | -3.59451 | -55.3779 | 2026-09-03 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac795936-03f0-326d-97dc-5512dfff1aa1 | -6.68223 | -59.94457 | 2026-09-03 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 46582539-cf69-3c04-9195-d476bb87d4a9 | -4.97608 | -62.38464 | 2026-09-03 05:42:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f84a7bc-fea2-3ba7-900d-3e42cf04222d | -8.8734 | -66.67252 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26b7b2ae-ad16-3398-aac8-b551e501b3cd | -9.08616 | -65.37398 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce3bc5b-7b0e-34c3-b6e8-e0c3d1effd85 | -7.36837 | -60.5984 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70369c22-e656-3082-af56-207edf40d12b | -9.04218 | -65.74639 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71fe7b03-190c-3f3d-b2c1-f60fca1338eb | -9.09549 | -65.51176 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01e372e6-8ce3-3b77-9a60-2f897bff773f | -8.43374 | -54.69398 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fda3638-d3af-31c2-9b16-7e4973cfd246 | -8.60583 | -62.55831 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6b8fe83-d1cf-3b84-bda6-3e478f10cdb9 | -8.85251 | -70.6281 | 2026-09-03 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c1c1977-55be-3b24-8ec1-fbb0d9e84e0b | -8.46359 | -54.65478 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 79e7b116-9251-374e-872d-4ccb5bd511d8 | -8.79373 | -71.2853 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f068aa28-f485-3d17-b34e-133a46ce3707 | -9.10266 | -65.50931 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62736ddf-08f3-3077-9ff5-3481d305e1dc | -8.45566 | -54.66809 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3abd8922-5dd7-33c8-855a-bc8c2bc07ebb | -9.03887 | -65.74587 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1239a4c-a59b-3271-b545-6b5374e04d07 | -9.59393 | -60.52755 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99997ab7-dfcc-34c9-b30c-b7cd4c724510 | -9.09367 | -67.68626 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e41e36c1-cd3f-3bd9-b6f3-56745bb3cfae | -7.54226 | -60.72004 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c75ae15-5332-3727-943a-8ddfd74a44d6 | -8.44039 | -54.69045 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4fc825e-83ba-3d36-b574-c6a963be9efb | -7.84872 | -71.75478 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 968461b9-86e3-3b50-82c6-e734fea8be3c | -8.42706 | -54.69778 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f5ad7c1-b985-3f5b-b88f-65e673f6e67a | -8.45928 | -54.68828 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02578e0a-5162-330c-83f9-40b2c4bc376e | -9.87914 | -64.96268 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08275e17-13c9-31ef-b44f-30fb5bea84c0 | -8.43276 | -54.75031 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86f910f5-3ba7-30bf-a072-f52343a99482 | -9.70509 | -57.88524 | 2026-09-03 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8be62b3b-5b51-3a3e-94b4-a7f9891c060f | -9.88569 | -60.29368 | 2026-09-03 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ca665fa-979c-3128-b928-b3dd6dced0eb | -9.0361 | -65.74187 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db4e3b17-e0f9-3362-9711-ccc680b9c19d | -10.25438 | -68.2458 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1fb1169-c26b-3f59-b3d2-eb2baf4ce38b | -7.0299 | -62.97718 | 2026-09-03 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9ccf54-30b1-399c-9c9d-fb2d84eb943a | -8.46907 | -54.66053 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 503c0040-e540-346c-81da-7d72a2cb063f | -10.29021 | -68.84531 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e51624-b4e3-30e1-a3f4-31d745986df7 | -8.42228 | -71.08336 | 2026-09-03 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b094c70-2457-3e7e-904c-b96eadd7c341 | -8.44004 | -54.74164 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 912a065e-2861-3a58-8820-1de800671feb | -6.9475 | -58.98607 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2bdf371-f846-357f-bf14-5bc5c00a4d78 | -9.04711 | -65.73647 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1f2dc84-99c2-3b4a-aa6d-8c55618face2 | -7.50559 | -60.7753 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc329ab4-5646-3cb4-9123-e0e656f52fd0 | -9.09934 | -65.50879 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9094504b-ad2f-36ea-b4dc-1d39579b2673 | -7.24828 | -59.52277 | 2026-09-03 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb4ab64c-bae2-32e0-afbb-c84eeb314e83 | -9.71604 | -65.01163 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a33abe1f-79a9-346a-9957-d68d08fc2e2c | -8.43335 | -54.74566 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70f02b52-2305-3af5-a091-3c7a7bed2314 | -9.71379 | -65.00394 | 2026-09-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee47561f-1c4c-38cb-9097-24ba7f9c8934 | -9.70434 | -57.89109 | 2026-09-03 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e4098d4-c6d2-34c4-b073-b44d8bff1604 | -8.44553 | -54.74709 | 2026-09-03 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34d7f66a-c7f2-3c88-b41b-da643f476004 | -7.27865 | -60.64972 | 2026-09-03 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dd978bd-d5d6-3d0d-bd98-66a8eaa7a662 | -10.28764 | -68.86101 | 2026-09-03 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cf61a83-247e-3740-a599-4bcf89d9d95b | -8.8089 | -68.69183 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9e5d77e-f639-3225-99a2-726928de9492 | -8.59575 | -67.17905 | 2026-09-03 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2434f21d-96d8-3b33-ad92-f7d95a4f96ff | -9.10374 | -65.5023 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 741666ee-ee72-3e8d-afce-f8fb6864e1de | -9.02001 | -65.44987 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc04a4a-e758-3bc3-bf8e-17958e2bfac8 | -9.02332 | -65.45039 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c262c1d5-598b-32c3-9ade-bcf21d27ea31 | -7.45786 | -61.37526 | 2026-09-03 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c3494a4-fe23-3ff3-b136-f5d018df0677 | -9.04434 | -65.73247 | 2026-09-03 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fffc9552-306c-31e4-9808-bb95f9383e81 | -12.01009 | -60.52856 | 2026-09-03 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README47.md)
