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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9085010e-053b-3786-baee-aa6adc233255 | -13.82 | -44.54 | 2024-10-10 00:04:05 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91bd0533-1d4a-3f5b-beac-82a1fd0a672e | -11.01 | -57.25 | 2024-10-10 00:04:23 | MSG-03 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581900ce-3ef5-3923-bd5e-0ab834b4f026 | -4.48 | -46.61 | 2024-10-10 00:05:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5d44f54-2692-38cb-99ca-2d8dd1195fb9 | -1.2541 | -55.7101 | 2024-10-10 00:05:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6cb31a5d-3556-336a-b620-f78c8bbc299d | -1.2541 | -55.6904 | 2024-10-10 00:05:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2223119a-72a1-3c88-b0b9-ea15fa9d6674 | -2.67 | -53.35 | 2024-10-10 00:05:13 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23983938-7fb6-3f4a-a8c5-873dfdbb441a | -1.9847 | -56.7428 | 2024-10-10 00:05:17 | GOES-16 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4b56e184-b718-3645-83cb-15075ca7fddf | -3.2571 | -54.1824 | 2024-10-10 00:05:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| eb3de682-492d-33e9-a768-38ec9f943433 | -3.3341 | -53.232 | 2024-10-10 00:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 57e6a924-c677-3821-b7cc-9e6ba953c3b0 | -3.3342 | -53.2117 | 2024-10-10 00:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| b73e595e-cbc2-3184-abad-eb76509e321a | -3.6746 | -51.1274 | 2024-10-10 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b755d508-475d-3f7b-b4ac-0b387a165d30 | -3.6747 | -51.1066 | 2024-10-10 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| fc72d1fc-e84c-35b7-bda7-9fdd881c9c41 | -3.6931 | -51.1268 | 2024-10-10 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 7d2df5d9-9ecf-31eb-ab57-43f5a6fdac04 | -3.6932 | -51.106 | 2024-10-10 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a3db652b-28d0-34bc-95bf-7a2b968777a1 | -3.7246 | -44.9773 | 2024-10-10 00:05:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8c9cb843-0fdb-30d2-b006-17c7fdaedcfb | -3.7247 | -44.9547 | 2024-10-10 00:05:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3accd57c-d062-32ed-8c75-5ec26de5c4f9 | -3.796 | -45.5151 | 2024-10-10 00:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e2d924e7-1f83-3a47-bc72-f067ce2fc4a8 | -3.7961 | -45.4927 | 2024-10-10 00:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9df276fa-690a-3343-9914-dfa02af76bdf | -3.8146 | -45.5143 | 2024-10-10 00:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b5a4e77b-64ae-3a5f-83ac-de1d7eb8832e | -3.8147 | -45.4918 | 2024-10-10 00:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 157.1 |
| d6fcee5c-2b74-3d38-bcc0-681dfd878669 | -4.0814 | -51.0292 | 2024-10-10 00:05:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c8f858de-fc8a-3859-97f2-0e2eda5ee170 | -4.0961 | -48.2739 | 2024-10-10 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 577a96b9-ab1b-37d9-8e11-97a5116f0a3a | -4.0962 | -48.2523 | 2024-10-10 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 01a658fd-7ff3-3683-833f-2b81d99d673a | -4.1102 | -49.0675 | 2024-10-10 00:05:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5f83434c-64ac-3e72-b0cd-436ad3686a21 | -4.1146 | -48.2731 | 2024-10-10 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 7273c7b7-d6dd-3791-bbaf-787b15661867 | -4.1148 | -48.2515 | 2024-10-10 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 2aa35598-01fa-375b-831e-c9156f03100c | -4.2802 | -45.4688 | 2024-10-10 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e4f81836-0171-3bf4-a428-33541f2b42ca | -4.4775 | -46.6177 | 2024-10-10 00:05:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5d0575b5-2dbf-3b27-9a81-2ae7997a4e1b | -4.4776 | -46.5956 | 2024-10-10 00:05:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 266.4 |
| feb33d47-debc-3f18-b3cf-a0edd6b15eb5 | -4.4778 | -46.5735 | 2024-10-10 00:05:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 5b111e1d-a0ca-358d-a267-4556157aee2c | -4.9513 | -42.9973 | 2024-10-10 00:05:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f359c659-2278-3209-8e5b-60bb685002c3 | -4.9515 | -42.9739 | 2024-10-10 00:05:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2496ac5b-a009-3caa-a154-f353c0cf78d7 | -5.3946 | -45.9865 | 2024-10-10 00:05:37 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d887ab0c-d41f-32b6-b7ec-3e263b2e26e0 | -5.4833 | -44.2822 | 2024-10-10 00:05:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8a97f007-7150-3c32-affc-69d0e5664b48 | -5.9962 | -43.4809 | 2024-10-10 00:05:40 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cdc05bac-fdf6-3c2c-93d0-7e6d15f744b6 | -5.9034 | -45.4353 | 2024-10-10 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| f426534f-3fb0-3153-b4a7-18705d93a904 | -5.9036 | -45.4127 | 2024-10-10 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 7f8870cf-03a6-30da-968d-fc3cc4cbc181 | -5.9221 | -45.434 | 2024-10-10 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 92e73527-b2bc-3c22-a995-302a60308a9c | -5.9223 | -45.4114 | 2024-10-10 00:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| e9b1346a-7291-3420-a82d-b5f19e32f3c5 | -6.5218 | -60.0649 | 2024-10-10 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| aa079702-a668-3ff8-96e7-8c9ecebfe578 | -6.5219 | -60.0457 | 2024-10-10 00:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 15c70e5e-6862-3699-ba6d-e5c8deff3e67 | -6.7809 | -45.638 | 2024-10-10 00:05:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d1d0c550-3c75-3f53-92e5-7900795860b3 | -6.747 | -59.3259 | 2024-10-10 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 20c9cf50-dcf2-3971-a131-afc621e2f32d | -6.7654 | -59.3252 | 2024-10-10 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 194c7dad-e3cc-323b-be48-8770c52aecf7 | -6.7655 | -59.3059 | 2024-10-10 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 64b1457c-631d-36e0-8ac7-dc8ac7d32a69 | -6.7798 | -60.0552 | 2024-10-10 00:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 8fc247bc-5d08-3bec-bd94-714ed4a9a05f | -6.7799 | -60.036 | 2024-10-10 00:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0c831c8c-4a2c-358f-b959-02a8a1190185 | -6.7839 | -59.3245 | 2024-10-10 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 198f2550-41a1-3203-a840-ff452e88a376 | -6.784 | -59.3052 | 2024-10-10 00:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 904296e8-9c4a-3d1f-a671-1348960d470b | -6.9532 | -45.2846 | 2024-10-10 00:05:45 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 0f0e16ab-47bc-30be-bff6-f37ce9ab7f6b | -7.0416 | -59.4296 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| dfdb8e45-b4b7-35f0-a63f-41db6707280c | -7.0417 | -59.4103 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 2f344340-05ea-30c4-bcf0-e4da5fc936fb | -7.06 | -59.4288 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| cf07626e-d722-3b3d-9e3d-3e83b9a0e9ae | -7.0601 | -59.4095 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 7479533f-26c0-3c77-bd10-d2716dec821f | -7.1341 | -59.3871 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4938c8bc-6fc6-3040-a341-28063673ec81 | -7.1342 | -59.3678 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 777e7e92-470f-3ef1-ac78-78260bb478b0 | -7.1346 | -59.3099 | 2024-10-10 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4ddedae7-1e83-3779-b019-7b64ae6d4713 | -7.3754 | -46.1489 | 2024-10-10 00:05:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f7f1b57a-4bb4-3c1b-b479-9246a75f1ca4 | -7.3942 | -46.1472 | 2024-10-10 00:05:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c3f88d8c-61a4-33e1-aedc-aea49bfec5a6 | -7.5744 | -46.8222 | 2024-10-10 00:05:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f72f6173-d2d8-3c9b-86dd-b033aadc6bbd | -7.5746 | -46.8 | 2024-10-10 00:05:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 69a0dd0c-a020-3cdd-ba8c-1852f440003e | -7.5934 | -46.7984 | 2024-10-10 00:05:49 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dd213917-a11c-323b-9971-66b8653b523e | -8.1475 | -42.9717 | 2024-10-10 00:05:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| a92189c7-9490-3838-b835-89531a00cb13 | -8.2325 | -61.1823 | 2024-10-10 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4eefe562-c243-39fe-bcea-a086e2688c98 | -8.6843 | -63.1009 | 2024-10-10 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2ef1d075-b8df-388a-87e2-acb4b20d955d | -8.6844 | -63.082 | 2024-10-10 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 83063353-e0f0-3d09-87eb-8ac95b234aa9 | -8.7028 | -63.1002 | 2024-10-10 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 770bff27-e1d1-37fe-a435-019fe184782e | -8.7029 | -63.0813 | 2024-10-10 00:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2ac51cff-44a4-3787-b553-2985d482b470 | -8.7762 | -63.2295 | 2024-10-10 00:05:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 67bbf089-d317-3848-ba60-cc62267af0af | -8.8422 | -61.4992 | 2024-10-10 00:05:57 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 3f09778a-c666-3cbe-94c8-c52a82ce4bcb | -8.9898 | -61.6261 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7a708ac9-a46f-31ad-ad9a-53fa8b1ec8d4 | -8.9899 | -61.607 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| dfa55e33-2fa5-3700-b3c8-1223cc69a25e | -9.0084 | -61.6253 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8e68674a-2e10-3b70-9474-0c9a13a540eb | -9.0085 | -61.6062 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6e286d00-8bd4-3572-999c-c51a96f645fd | -9.027 | -61.6244 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 067c59e9-f57e-3f8c-acbb-82ea3b510a14 | -9.0271 | -61.6053 | 2024-10-10 00:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6578cddc-9225-34a0-8752-47feb68c17b4 | -9.0656 | -61.3934 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 8a24c505-c50e-30fe-9f5e-88ff79ea8ebd | -9.0841 | -61.4117 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| e70b5a92-5823-3947-8f16-266bceb43d95 | -9.0842 | -61.3925 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 1bea8e59-f433-3442-9c82-a19319f6c2b7 | -9.0857 | -61.1629 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 77b3ccd9-1842-3e82-93a2-0eb451473a90 | -9.1028 | -61.3917 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ad27700f-ed2a-3d4e-93e1-b29fc300585b | -9.1035 | -61.2769 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e373e5a7-9af5-30b5-8cba-9eb2d7b89142 | -9.122 | -61.2951 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f036890c-3d20-38fe-83f5-320bbcfcfbdf | -9.1221 | -61.276 | 2024-10-10 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| feaf41c4-fa36-3444-9ba7-783487ecf06d | -9.3548 | -48.8043 | 2024-10-10 00:05:59 | GOES-16 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f1275d0c-e742-306e-9990-6ba910ab226b | -9.3736 | -48.8025 | 2024-10-10 00:05:59 | GOES-16 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b9ad3647-b2f2-3ad8-8aea-9aec04ef9d77 | -9.775 | -36.368 | 2024-10-10 00:06:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| 22146397-f881-3ca8-83be-6732710cf058 | -9.8551 | -60.3159 | 2024-10-10 00:06:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 73507577-436b-38c2-a515-954e682ab4e2 | -9.9105 | -58.1313 | 2024-10-10 00:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 1d9e939e-fa8b-301b-887e-ed94e07d364d | -9.9107 | -58.1116 | 2024-10-10 00:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| bf1c8e32-3de9-3156-8a09-47c103027161 | -10.352 | -61.2523 | 2024-10-10 00:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b979daef-57d3-37e6-9a4b-69eb3fc82889 | -10.3707 | -61.2513 | 2024-10-10 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ed444b05-406c-3134-8f67-c0eaeb6ef8a0 | -10.3708 | -61.232 | 2024-10-10 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 59973f59-8286-3d1f-841a-5115f368df47 | -10.3894 | -61.2502 | 2024-10-10 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c9f75407-a6b7-38e5-8a82-f9d8cb75d9da | -10.4287 | -60.9979 | 2024-10-10 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 219861c7-2aa7-3fee-b473-323e7b76341b | -10.5743 | -48.0399 | 2024-10-10 00:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 14f9461a-6e13-3392-b931-a476c9540cd3 | -10.5746 | -48.0178 | 2024-10-10 00:06:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b3fa9912-d477-366b-90cb-5ebc5d33d122 | -11.0252 | -57.2436 | 2024-10-10 00:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d438cd1c-382a-348b-be8d-6cbc94450b24 | -11.0254 | -57.2237 | 2024-10-10 00:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 262.8 |
| 108223a1-aef6-311d-91dd-1852e684d6c8 | -11.0256 | -57.2038 | 2024-10-10 00:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 241.9 |


[Clique aqui para ver as próximas entradas](README2.md)
