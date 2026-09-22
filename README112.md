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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a9f535c-8e3f-3ada-a1c4-02d49dcb4b8a | -6.18937 | -57.7754 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4f5ec96-ad99-35d7-bfc0-9452cd17b6ec | -3.06975 | -61.0841 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9be2e255-5043-3fd2-8086-fcd7afc1168b | -6.92124 | -62.91257 | 2026-09-22 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4895c0b5-9afd-3636-8c39-46802be67755 | -6.63975 | -59.9252 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 506f75c8-2c40-3fce-ac47-6f6804efc67f | -7.39771 | -55.22242 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea898f97-2724-37c2-aa61-d04b51aa1afd | -5.82206 | -57.74235 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 073e8657-22bd-3969-b3d3-9b0934a780df | -2.41391 | -58.27889 | 2026-09-22 05:42:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b848b9f-da94-3a3b-97f8-58003c7a908f | -3.34204 | -59.85289 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78e0f490-5c25-36c6-b56c-c876454f1edf | -6.73607 | -55.09253 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29a368ed-125a-3175-9ab5-49ceab4fe657 | -3.13266 | -61.3969 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e15e739-7c66-37c2-8f29-654fcde04b66 | -5.38256 | -55.90357 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a070e557-529d-34c6-b199-ecc3619a529c | -6.10087 | -57.62096 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86e96dff-7382-3d6b-8745-0a7901785d4d | -8.59813 | -54.63653 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06935729-49b9-37e5-96ea-98b1531587d2 | -6.73298 | -55.07635 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9838c51b-3236-3b50-894f-26579e7ab3ef | -2.86738 | -57.79716 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8be57147-9821-39ff-97d2-5b3c4c4210a2 | -8.60466 | -54.63003 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87cf677e-75b6-3f29-aa86-f385753fd73e | -6.62391 | -59.92996 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a14a048b-8b79-3192-9a41-f79bf474e054 | -4.87357 | -55.84387 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d473e850-0629-310d-a9a3-fad47c93478b | -3.06256 | -54.40711 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c22e795-becc-3652-a71e-6cc6c208dad0 | -3.32905 | -59.81595 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd8b089a-18d8-3f1d-91ee-d757eb6f3afd | -3.18637 | -59.70049 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 552eb3d7-0f81-31de-8f5e-d613f375723c | -2.86156 | -60.91417 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3777bd4-6da5-3883-8041-cb6ef633b69e | -7.6099 | -55.35438 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2523d1b3-4cc9-398a-953d-9e7913c19c1b | -6.70005 | -59.96244 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e358b84f-ac7a-34e5-8d4f-c53d2a047572 | -3.24659 | -60.18396 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13918b2-a300-36e4-9b4a-e658779c39d5 | -3.55474 | -59.42625 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be11b1b0-446b-3ed6-9997-9976f909a870 | -3.42223 | -61.31573 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebbce61e-7bab-3df7-b776-4e99d8469db9 | -6.72993 | -55.09817 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29557bc1-5ae6-349a-b75d-decbf42c4d61 | -3.60705 | -60.56851 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8529694-7430-30b4-b62a-57425526af53 | -3.90025 | -60.59084 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2444802-b14f-3a23-b469-a81dbd977a9f | -7.33268 | -55.6083 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb7074b-3953-366f-87b7-54260436c339 | -6.31235 | -57.74281 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a87a3ca6-1d99-39b7-b408-f84aae5ea76d | -3.60583 | -60.57645 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d446e9a-59f2-37ce-a8a9-480247585a2f | -3.7982 | -59.70814 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 761d897d-0a3b-3d22-a720-57b076eb680a | -6.4271 | -59.97815 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b83cd1bd-06df-3862-94db-b929a1f012ef | -3.51173 | -59.57938 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40749631-f4f8-3f17-92b5-42659a259eee | -6.2402 | -51.0154 | 2026-09-22 05:42:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d53b1f0d-db9b-3a75-99c6-2e490009b77b | -6.09562 | -57.6523 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c66ae18-1e4a-3d7c-bbdf-7b06524a2d6f | -3.38344 | -61.29457 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bb8ee37-453f-3a47-9462-b8cc671e31b9 | -3.70145 | -60.63565 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39ea7c9a-91fe-3322-b463-4a87204f26ff | -6.08511 | -57.63317 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b62cebb-6fa0-3709-ad77-817ecc5924e0 | -3.47492 | -59.59628 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65aedffd-0dc8-3902-b483-cd2442e48fee | -3.68381 | -60.63295 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9c5719-7b3b-3d19-9fcc-8eb841d9d957 | -6.30653 | -57.74446 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9a623aa-2f1d-315b-b483-07c9578ab4c7 | -6.77839 | -59.00281 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57e803aa-ddcf-383c-8fbd-dc1accce499a | -6.4318 | -55.62064 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3f22891-e794-370d-a11d-bd2e22c195b5 | -7.57004 | -61.15244 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23fa548c-735a-3cae-95d9-84cb80cf716f | -6.44799 | -59.96735 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 237ef87d-f2d4-3c24-a6aa-69634f678cd0 | -6.10026 | -57.62521 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bdca2d2-776a-38a3-a01a-397209d5c04b | -2.41867 | -58.27438 | 2026-09-22 05:42:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dabd326-84d0-312a-ba91-016b795deeaa | -6.30916 | -60.01832 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 353d2451-a5eb-3d83-a488-c4f0bbd4b7fe | -6.19876 | -57.78436 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e124728f-2d40-35a7-9fc0-47f5161a1257 | -3.70461 | -60.63916 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe6bbb05-30d6-3c1d-a866-0efca00cce2c | -7.39651 | -55.23094 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3cfd7a9-15fd-3496-b52e-8cfe0e899268 | -2.85694 | -57.8106 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbd280e3-12da-3855-bcfd-6a3389596030 | -6.81052 | -55.83309 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5439b74-c0ab-3787-b968-b526096cf304 | -3.58343 | -59.06754 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dc913e8-8d74-3f03-b839-b9aa66348545 | -7.23779 | -55.59612 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 526919cf-fe39-33c6-aa93-a8de75c49388 | -3.12838 | -61.06603 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 069d8d5e-a9bc-3a11-9dea-21ae938f7b1a | -5.72394 | -53.46188 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aad8301-7c49-3d13-bc4b-8b63cc044820 | -5.93855 | -59.98495 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b44660-9565-3cf1-b87e-0667297bc0d2 | -2.93023 | -57.79916 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae8211fa-009f-3b15-a10c-c8eafd3ef888 | -6.43727 | -55.61836 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d7336a8-99c6-30a5-9505-64d7d03960ab | -3.22561 | -53.95553 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 430c1f52-83e0-3c54-bc24-9ccc15357110 | -3.06118 | -61.27289 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8be5195-23a7-3450-8c36-327c07cbe467 | -3.90317 | -60.59536 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e610f48-b393-3b27-a292-ea5695c67a52 | -3.46102 | -58.32484 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b3d9cf3-f64f-3b80-a9ff-f8fa030bd70d | -2.95179 | -57.71524 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09a3e284-ee8d-3995-872f-aa394684e417 | -8.11446 | -54.80465 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6b4f8e-bdd3-3a40-aeac-aa3b39fe37ab | -2.92201 | -60.99662 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6ba76e-7228-3f5b-880a-ab77f7cdb268 | -6.1017 | -57.67764 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 201dd119-59ed-3577-af13-7c18d25d7609 | -6.241 | -51.0095 | 2026-09-22 05:42:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3c48a46-2fd9-3c54-9aab-72ab592a0423 | -6.35216 | -57.77438 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b4b83a8-79f4-345d-984e-25cd05a42066 | -6.52391 | -58.3091 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f939ff18-58f9-3ae3-b352-8fa15fc5702b | -8.59958 | -54.62556 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9ded86-4f92-3326-96aa-30920b1b1f32 | -7.72886 | -61.25522 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d0e4b74-7309-3c1b-ab36-7f1c762814d1 | -3.39377 | -59.51884 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ae699c8-adf2-3456-99a1-950f9f17ac52 | -3.90284 | -51.89289 | 2026-09-22 05:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 200ee82d-728f-3018-af39-791b15cfaf3d | -3.05189 | -61.264 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5974fe9-8d46-33cf-82e7-c8bb7c929a51 | -4.77737 | -55.70195 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| febf7452-5c33-3daa-9832-89ef7ae8b1d1 | -4.43005 | -55.08705 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1221e67-ab8b-3590-850e-18c211b166cf | -3.05592 | -54.41596 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8d2ebab-f85e-37e7-bdcc-5c7a4328ee6e | -6.06703 | -57.87179 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d126a6-37a2-3d0d-95b3-bc2350ca5f83 | -5.93634 | -57.69819 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9adc3455-bff7-3e59-9b2d-ed7fa8e64811 | -7.69914 | -61.54224 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 797d2ade-1c67-3702-94aa-567c3913b6fa | -6.62223 | -59.91556 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| f5b354af-6530-36f1-943b-56dae45a1fea | -3.43769 | -60.10156 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 857648a7-00fc-34aa-9f16-bd7830b1f640 | -3.97137 | -59.63332 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee5fc12e-3aa6-3f63-88fd-cc1ef1708ac5 | -6.65112 | -59.92691 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 0460455d-3208-31f3-9532-c590ca55d31f | -6.1068 | -57.70403 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e30d13-13be-3967-bece-89c243b1c3ba | -6.30366 | -57.74149 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f4a4f5-5f41-3d26-bc0a-3f2077a9f23a | -6.67947 | -59.1095 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93a854a3-dc77-3412-89b7-5c378f6a68ca | -3.46885 | -59.53664 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a6a9114-4d11-3fbe-99a9-06111992f79b | -3.81531 | -58.8918 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05fce6c9-f174-31a8-9116-f8d70c4e17e8 | -6.72728 | -55.07871 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba3be51-6b62-3bb5-bdb7-32112f3e3dc1 | -3.04564 | -61.25925 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f74524f-e5b3-30a4-9349-15fd906ca803 | -7.29061 | -59.52776 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bf12f0c-d48f-3af4-801d-267c778d60bc | -6.70136 | -60.00487 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86a6f87b-7a10-3b98-bcd0-88d1d6f014e1 | -3.89963 | -60.59481 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eaa54c1-4ad8-3485-b2d3-6db2b090c9fb | -6.10519 | -56.10781 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README113.md)
