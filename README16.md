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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f476a91f-0af5-3631-9eb8-74db5229f83c | -5.03444 | -56.12399 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1435caa-9e60-3f61-b38c-3fdd50149e46 | -5.68813 | -60.23183 | 2026-08-10 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13f2325a-bbab-3e94-b170-667f25f84930 | -7.69586 | -55.16852 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca96d396-f694-3b4c-a2a9-ac6b9cf7ab5c | -7.39213 | -59.97463 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324ac2a1-97a8-3127-b844-efe729c05dfe | -6.8342 | -56.41439 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eee37f7f-53b5-3e90-b4f8-292e17d64be6 | -6.83481 | -56.41035 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfc986d2-cef2-36c6-b2f7-ea742b905061 | -7.55222 | -55.56268 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d22a8662-3d74-3e05-abaf-03669cc0bf3f | -8.89613 | -60.58216 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 247c4163-19ca-3dd2-999a-cd44de973b44 | -8.96145 | -60.53831 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0af17d8b-0635-34f4-9648-f261d17951a1 | -6.65408 | -49.61516 | 2026-08-10 05:27:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d765d39e-ce91-3475-b564-569e54a2c723 | -7.65853 | -62.55119 | 2026-08-10 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2acc403e-0158-3a3b-8999-223f70bb97c3 | -5.73424 | -49.13643 | 2026-08-10 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14cb4f08-c9cd-3492-ad76-9b43ac5c300f | -7.54779 | -55.56663 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bee8b8a-c74e-3952-8ae9-0a8c0915e611 | -6.84008 | -56.42359 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68987ee9-8d89-32bf-88b4-cd6fb13da7e4 | -6.16656 | -57.91844 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bdba32c-487d-3ff2-bfe1-30678209eec6 | -6.87896 | -58.94184 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e187a08c-0251-3ba7-8cc8-d9dbeb584c3e | -6.09674 | -57.69577 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9608acd-75c2-3a11-8339-3107c8f0725d | -6.83125 | -56.40979 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 976a23a0-cf3e-35f3-a4d3-6d63c1a70fb7 | -4.40069 | -54.7905 | 2026-08-10 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f7103c5-ea23-3773-946e-2c7a9113d570 | -8.90004 | -60.57917 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 637afd63-8c1f-399f-8c9e-a80183709e83 | -8.95811 | -60.53776 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f7a2cdc-c6b4-36b5-b8b4-91999e519c2e | -6.88946 | -58.93998 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36fe1706-edf0-39f8-b953-86766467889c | -7.54268 | -55.57508 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8499817d-6662-3cea-835c-fdb67f2d47ef | -6.84842 | -56.41659 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f405e5c5-61cb-324b-a2eb-6fd1716cf67f | -8.89442 | -60.59278 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 298aa91e-af9a-30bd-813a-a9420a350aba | -6.13948 | -57.70974 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e21eb7f-299f-33e6-9177-522a042a96d0 | -8.89173 | -60.56691 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 629fe163-931e-38c5-9c23-e4494c1acdc0 | -8.96668 | -60.53886 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1398893d-c587-3bc6-ac3e-8a79ffa6fe5e | -3.83693 | -54.31992 | 2026-08-10 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f52a5da-ae44-3132-828d-084a196b7ca3 | -2.97734 | -51.68592 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1dbb0a3-88f5-3779-b5ee-490aa2ddfa70 | -6.71865 | -58.93024 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3ab3ccb-1fb3-3e23-909e-e148be2bede4 | -3.02599 | -54.52396 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d016ea4b-db15-3545-9981-8e3ebf74e8eb | -6.85088 | -56.40047 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa980317-29db-3512-a698-bb3cf52fd45e | -8.94866 | -60.53259 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a835a5b3-e3f6-3a09-aae2-23816dbfddfc | -6.80981 | -56.43129 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0418dc7c-b0b3-300a-b151-9f3bcf815147 | -6.82404 | -56.4334 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56e938f2-b61e-3cd1-9907-c65f03c24529 | -6.87578 | -56.63977 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad6000df-c640-303d-814e-84c2cc93d191 | -7.66284 | -62.54762 | 2026-08-10 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54a58172-4c85-3edd-a660-59d696d36a73 | -4.4605 | -47.91892 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54465bb5-b3b9-35a5-9445-67e361bfcd73 | -6.82942 | -56.42191 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8dd9988-9c82-37c7-a37c-1c6f80770432 | -2.65241 | -54.6239 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55d8ddbd-b9df-3583-833b-e261fbaf9afd | -8.95698 | -60.54485 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 155eaa3d-399b-3c53-afac-694802d84833 | -6.24726 | -55.62315 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75336803-6aa0-3ed8-a6f1-6c650d062a32 | -6.64857 | -49.61435 | 2026-08-10 05:27:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b2f1824-a571-3f78-b9a4-4f65fc6774ed | -8.95086 | -60.54022 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ba6df8a-44e4-3367-8ac0-af82292e8be6 | -7.55481 | -61.15904 | 2026-08-10 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df66c2c-af47-33bc-bd44-ecf61292a0df | -7.39269 | -59.97113 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29c4d2c0-6f73-3721-ab5e-a2483b4bc979 | -8.96105 | -60.55246 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0548ede1-a5bb-3c26-880b-4baeed3b9030 | -8.97727 | -60.53694 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b08a4db-e316-34f0-9b1d-d675ca4d3e31 | -2.98117 | -51.69104 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39b242c7-566a-3f88-bbc4-ed19da5934e6 | -3.93292 | -59.12061 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3c9108d-5c11-3cac-b267-8ca350e00a5f | -8.8945 | -60.57099 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d7bf14cb-33b0-31e6-8870-375f5b778ed6 | -8.89841 | -60.56801 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f982b538-55c9-3143-bcc5-1602dffaf079 | -6.70927 | -58.94653 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d8f5404-42c4-3955-ae75-8c9d29c650b9 | -2.97665 | -51.69034 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c208435d-636e-3ff5-b8cd-435dc8c5ac03 | -6.85445 | -56.401 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ee066be-c486-337e-aeba-cbd676ad3d8b | -8.95641 | -60.54839 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6ef3e7f-ee43-3c5a-973d-81d82d921183 | -8.95528 | -60.55545 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9479d98c-2b62-3c22-8fdc-e0a6e5ddb15c | -8.89279 | -60.58161 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c7533eb-a1df-3546-8e3e-517da91aa130 | -6.87638 | -56.63583 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7d8b5ca-81f5-361f-befd-8be1437a28ce | -8.95876 | -60.5666 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb506b52-5108-364f-8db5-fa0d676e992a | -5.02735 | -56.12301 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61af35f1-80e3-3ac6-8b06-07f9e73354dc | -6.85198 | -56.41713 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f44cd6-12e9-33ed-bdbd-8a0e49332e49 | -8.89385 | -60.59632 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47aebf95-eb2f-333a-b505-de368fc1b3bf | -6.82526 | -56.42536 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 156e530b-efea-323a-8de8-3220db8cd721 | -6.82575 | -56.44605 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d11ec242-b284-3e83-a3e8-2ff330f73428 | -6.1632 | -57.91792 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab3e99d7-845a-3ba9-88c3-fd05a6a4bebd | -6.84069 | -56.41957 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d86e433-0999-3d22-9e92-d681f0913568 | -8.95862 | -60.55599 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5f249a42-43aa-30ae-a0ea-798a9cdb70d0 | -6.82281 | -56.44146 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd875963-2940-39bb-a102-e3efd7de072e | -8.89947 | -60.5827 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1da1417-2fc3-3ed2-a890-e4ed43b3ee50 | -7.66182 | -62.54883 | 2026-08-10 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7a02bda-9ab8-38a3-becb-657e177e6636 | -6.83898 | -56.40686 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee2920f2-9656-3e4d-8755-f452c7b0c4c8 | -8.97336 | -60.53994 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67470578-c69a-3345-b78d-753d8290b190 | -3.93126 | -59.13102 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dcb9fe0-d43f-3d99-b127-2211ea1179eb | -6.8396 | -56.40282 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ececf01a-07e2-3bc7-8c32-8937d38127ac | -9.9525 | -53.31264 | 2026-08-10 05:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 530de9d1-ff8e-370d-ae92-f13f1c33fe9e | -2.35998 | -67.21836 | 2026-08-10 05:27:00 | NPP-375D | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a698f4-ebb3-317b-a544-99e638f468c1 | -7.55154 | -55.56721 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1496880d-6a08-3bed-ad53-ff7263851e44 | -4.30344 | -59.47228 | 2026-08-10 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5516ddb-555b-3b63-8171-d5fb6f58d9e4 | -9.81625 | -54.89163 | 2026-08-10 05:27:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51a443cc-0e64-3a32-bfe5-b146b79027bd | -8.94752 | -60.53968 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2441e5de-4b82-3fe6-a964-5f2d20518abe | -9.37468 | -57.3582 | 2026-08-10 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 336c42d0-136e-3519-9539-abd59a709eb3 | -6.85739 | -56.40557 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22be4e02-24d1-3c3b-8bf8-380e108ed582 | -3.4894 | -50.05233 | 2026-08-10 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03976380-90ea-3c07-9dc6-9f4d958d940d | -9.95313 | -53.30803 | 2026-08-10 05:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b6e82d-40b4-3c3d-9703-eed720bcf6b1 | -8.94809 | -60.53613 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1cd5aaa3-54ee-3860-8c10-bff616707e66 | -8.95919 | -60.55246 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| af6b3b59-eb47-3e59-b921-62fb1f3ff6a8 | -2.6568 | -54.62006 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6a03b72-16c8-34e1-8345-ae912f5ba00c | -3.93569 | -59.1246 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5e7aa19-8ce4-3e35-a562-7479589a9394 | -6.1604 | -57.91384 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f3dfac7-d70f-3041-bd43-e6d57bbabb17 | -6.13328 | -57.77124 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9bfd7bc-d648-306b-9728-6ffc7bd867d0 | -6.15984 | -57.91741 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a3f76d-4420-392a-adaf-c88f0182ba12 | -2.91102 | -54.14904 | 2026-08-10 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9769609-04ec-3d01-966c-f62d09b8e960 | -4.86539 | -55.81683 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e88ef56-0911-3e56-9d61-ccbdfba3e471 | -8.94368 | -60.5209 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10331fd4-9483-3c18-a5da-94c2e69a4332 | -8.95754 | -60.54131 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2b1e1f5-43c9-3e2f-b013-b79113213c5b | -6.41518 | -55.79044 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7084765a-970b-3058-9143-844175db498d | -6.88228 | -58.94237 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 221a0ff2-f53d-3556-8ece-b8f630c7ec61 | -6.10011 | -57.6963 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
