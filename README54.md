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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d0ed739-2067-3069-9016-f51a5d2222d8 | -8.2493 | -46.50248 | 2026-08-30 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd17791f-fcf4-3cd8-997b-dcc5d80f3ca5 | -10.73793 | -54.04526 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b726d567-fbff-3ed4-bb1d-fbb931054748 | -10.75826 | -54.05668 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07469111-8f06-3e23-bf47-dd5156fb152d | -6.42312 | -55.52635 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3242bcd-d828-3883-9b95-2173cc4b31f0 | -11.16226 | -51.30404 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 33efaad1-e9e8-321b-910f-d46892f71e4e | -9.8706 | -60.29957 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 466af15a-7541-3029-9dc2-80a14cee8f64 | -10.55844 | -59.61873 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 087bdac1-a549-30f3-b07d-9e58582b3198 | -6.932 | -55.70092 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a7e251c-295f-3348-8a28-b3aa92595ade | -5.76663 | -51.68007 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b8d783-777d-3d42-8814-109a4b2e3907 | -11.16206 | -51.31442 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e72290f-315e-3342-9d90-12d07faded0b | -7.5217 | -55.32071 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7c10305f-0e86-3e37-af2d-97bea29fb4ef | -7.48367 | -61.40346 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb525a08-451d-3aa1-9154-4bd613de8d46 | -6.12089 | -57.69238 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf5b3ba-753b-333e-b7b8-5cb88a01c326 | -9.9817 | -60.26402 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2afcd0db-8f4f-3503-aed1-9f6afc996eec | -6.94176 | -55.71118 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 44660105-9e13-367b-93aa-853b5903c3d7 | -9.71471 | -60.74692 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae04164c-f310-3e0a-9f9a-c59ea3bef584 | -8.96547 | -62.40432 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b93752c0-531b-3141-a2b4-a2ed649bdb7b | -9.17567 | -59.63477 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ea365dc-8dbd-3676-b4e4-89255e73b22a | -6.93808 | -55.71065 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a433312-59cd-3f02-b2e7-3a984e1f7d3c | -8.24971 | -54.96799 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deb69a00-983a-3cdb-b72b-39d9f10eb60f | -6.62246 | -58.38454 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3458989-3f01-3897-9fdd-a996ee2702fb | -5.88966 | -57.75921 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eb70a32-db9f-3ee6-8445-78e2b4cd7c59 | -9.18337 | -59.62886 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbea783a-a9ae-3c05-82dc-7fd6c7115450 | -6.78007 | -55.66828 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3ec2ca3-2d6b-3fdd-958d-ae61ac12e5af | -9.89188 | -64.98684 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b090166-8bf8-3d74-aa81-ef586aeedf20 | -6.17905 | -57.70829 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3b533d0-a51c-300c-a04b-e49d7e4e1c58 | -7.552 | -61.30641 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac3ac058-4585-307e-80f3-fc5734be0a07 | -10.5059 | -59.62844 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bebc992-3a0a-39d8-b47a-72095892b1a6 | -7.24322 | -60.628 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 05f4de2f-d28d-3d92-9f4f-176d44bb9740 | -6.17569 | -57.70779 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc96707c-31c2-3b17-b43b-49bc7612ccc8 | -6.93568 | -55.70146 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 50f73593-4970-3a1c-819b-c00f37bbe3b2 | -6.16596 | -57.79404 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c29c4364-1572-3f5c-9ea0-c72c24e031f1 | -6.94847 | -58.95866 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3339161b-b393-3467-9ec6-8a0e00b39154 | -7.5148 | -60.72299 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24061575-c5e6-3765-b04a-3f2aeec428da | -5.96488 | -57.68694 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05ba1b46-8110-39f0-91b4-82006959a0dc | -5.87913 | -57.783 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 11598b8a-745c-3e7b-8754-c5c5cf7c1938 | -6.61357 | -55.4481 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04d77535-7a35-37a9-9c91-1a405c056ccd | -6.82518 | -59.4211 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b99af31-8448-300d-bae3-81c37a44de7c | -6.16034 | -57.78587 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 146c4a41-6653-38cc-872d-366ab41847a5 | -8.65008 | -62.8428 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ecfd663-f38b-3aa7-99c5-5c7c1fa5bda3 | -9.07627 | -64.24547 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9a9e6a-7f4f-3b2d-a334-6ee0b7c41e9c | -8.50455 | -55.28983 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f9cc22f-962a-307c-9700-4c6d9c00b6d5 | -6.18879 | -57.9357 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74e5569-751d-39fd-b624-a9cfdd087133 | -11.19841 | -55.1086 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2630e227-6abb-3076-bba6-25d209976f45 | -7.12755 | -56.55329 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f90ba056-599e-32d9-8149-ae3f861f31f6 | -8.02512 | -61.89636 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1fca583-e04d-3899-a457-a86fbfcd78e3 | -11.79905 | -51.04321 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 321a37be-18c0-38bf-a927-703ea1fb99bb | -10.84467 | -50.49236 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d53ba562-e9cc-391f-b845-659931332adf | -7.55542 | -61.30696 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f16548a2-38eb-3e57-ac99-5c768fd2a2e4 | -6.18858 | -55.44156 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7094f163-f4b4-3a29-87d2-8726d362d770 | -5.96706 | -57.6726 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9a2b3c0-99a6-365b-af5b-739e9a8c9fc1 | -8.61438 | -54.77413 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17d94ba5-e7e6-3355-85c9-4848dbaa1b04 | -8.58325 | -66.9581 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebe4d537-2355-392d-b98a-dac05bec93e9 | -7.57698 | -61.391 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e2db931-4d69-3cce-a5a3-9fad01cd0399 | -9.51433 | -65.575 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63e16555-4754-376f-826f-a8074958a685 | -11.29934 | -54.04091 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ca15322a-4eb1-3e03-a7cc-5c14929282bb | -9.12695 | -50.58761 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2c6970e-ebb9-3bd0-9410-791afb445896 | -8.58414 | -66.95312 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0bcc7f0-7e8d-3fad-a29e-c6e5c4da2d34 | -8.62108 | -54.72751 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0273624c-de97-3462-89b3-9b9ad877794d | -7.31277 | -60.60229 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e83394e9-788c-3474-8eba-c5e7fb14ca12 | -8.94404 | -62.38029 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6eefc12-938d-36b8-bddf-8df8b211b9ab | -9.70801 | -60.74948 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dcba36d-a2e4-374f-969f-9d628b939025 | -8.50386 | -55.29463 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f2695fd-5840-3f23-b346-9ab792beb7b9 | -7.56328 | -61.32351 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6a13ec6-245d-3ea7-9b38-e4e59a79d27d | -11.81552 | -51.04195 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5e2ef3ab-4f99-3d74-bb8a-ead879b18e2a | -7.45165 | -59.93701 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fbc8a39-2b37-3308-b3aa-b1287434762c | -11.15979 | -50.58535 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4ff7b986-511b-3cf5-874b-c991bf04c69a | -6.88562 | -59.44839 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6580333-80a4-3a31-b487-18f16dd0b427 | -9.79331 | -59.44379 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf5607f3-02b6-3567-8e45-ca45dda586b0 | -9.71527 | -60.74338 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45efd74a-06f8-3304-9f7e-8cb9b2bf3d24 | -6.16315 | -57.78996 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85a317ee-41e7-3a01-9189-6b62fb97aaef | -6.27707 | -53.14392 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 573617cf-6d46-3f68-b510-80f54c4fc52e | -10.55289 | -59.61067 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dcec29c-7a2b-3f7a-b709-c65cdf7e9671 | -6.78741 | -55.6694 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9512cc68-10d0-3fb9-a68d-60865052cca3 | -9.93485 | -60.51873 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d6ff366-8f1b-3048-95cc-d60b3d361c5e | -6.94414 | -55.72045 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e78036e-7946-3a33-ac66-8fffb847850d | -6.72892 | -58.7075 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a8b1323-7243-38bc-88d4-e7068568eb61 | -5.25872 | -55.91127 | 2026-08-30 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89575f11-4f72-3bb7-a2e1-56132d2d6a4a | -9.05835 | -65.42169 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32c17abc-c438-3513-ab1f-e1f570e64012 | -10.49205 | -59.60832 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8dcd2496-693f-35d0-ac93-8320be9356fc | -7.30714 | -60.6161 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 073f105c-2066-306d-ad87-5fb7e0d6658f | -5.98894 | -57.687 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f22822b0-018b-322c-8cdf-d1f9c3eeac74 | -6.69674 | -60.12936 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a9ec71-316d-3bcb-ae9a-245a7c75563f | -5.90081 | -57.7536 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06cd0218-1770-30c7-aa18-d2e0e392c153 | -5.96206 | -57.68285 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b638e136-234b-3916-bcd4-47612563c396 | -6.10527 | -55.82391 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cd659db-3cfd-3016-9a2d-e98cb756cb64 | -6.76906 | -55.6665 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 408e288e-ba23-3cce-962e-24460f235885 | -8.61372 | -54.69366 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c09a85-2ee3-34ca-8018-3767dfebb8da | -7.40049 | -60.58306 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3e24183-15e4-3db3-8e11-d9816729515b | -5.48286 | -57.14074 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d09188c1-8313-30b2-a883-dbd529191d3b | -5.97378 | -57.67365 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e1a98f4-5f26-3ecc-a9d0-482ed794fbc8 | -9.89452 | -60.2788 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5e502714-590c-31e2-80fd-c99550b92a43 | -8.25915 | -62.75285 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bebee30-3202-3a27-90a9-f0e037ce2d65 | -7.54899 | -55.55318 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbd8ebfb-7820-32c4-a249-f80785f6fe5a | -7.26396 | -60.62764 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4ecf159-e86a-3e7c-bbed-432e3129b094 | -9.13213 | -60.77641 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6690ab28-433c-3b11-b105-a2b63d01968c | -9.66329 | -55.08696 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e36fbb54-e088-34c7-81b6-05b4e48f5259 | -7.29934 | -60.60016 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69085013-2237-3600-8d14-e4c26b180681 | -9.79968 | -60.16649 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7610382-3ec9-3b7a-8e26-a85d03316635 | -7.32734 | -60.59725 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
