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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a349e4be-1cff-3552-b715-0320555b3aec | -7.89799 | -61.17412 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bb811ae-5838-33f1-9f1f-84f75151cc6c | -9.2245 | -67.38963 | 2026-09-24 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86e4d8a3-3912-3479-bc19-5fb613ae67b9 | -8.93878 | -68.55969 | 2026-09-24 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f38926eb-cc6e-3d97-b810-cccd9d225b0c | -9.05109 | -65.42154 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bb16c5a-c6fd-397c-814a-497b30572f83 | -7.88313 | -61.17162 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f44e3d06-3c82-3f12-b059-7a16ba3624f2 | -9.03171 | -61.66117 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec2eada1-c876-38e1-ab4e-1b62518b36f3 | -8.00872 | -71.31158 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 439862fc-69c3-3f60-940d-a4479a8a70c5 | -5.11125 | -60.26192 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e856b986-8c27-382e-9238-ed0fa778dbfa | -3.6912 | -60.54782 | 2026-09-24 06:25:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0998921a-492a-3a1b-aedc-64781ae6789f | -7.91795 | -72.94688 | 2026-09-24 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c0cc2c3-7102-3949-99c8-74b70c567635 | -7.87676 | -61.18233 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a08e7d7-6047-32ee-b8b7-6e540a339cbc | -3.68315 | -60.55761 | 2026-09-24 06:25:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c56d43ed-2717-356b-9d26-c80e4d22fd59 | -7.65835 | -70.50848 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56bfe221-dc70-3534-b56e-615d6af3c501 | -9.49696 | -64.03578 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb42a275-8f1f-30a1-9491-69e4776720fb | -8.31607 | -70.53711 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21f70a6f-bf8d-3364-bce1-5ea73c9a4288 | -7.88334 | -61.18334 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d115014e-5692-3367-b8ad-3b0518a31c16 | -9.0456 | -65.42381 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a1557de-d8e4-3784-9dab-780eb2998667 | -7.88899 | -61.17833 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c58f268d-028b-371e-8a14-45b3a89ae268 | -7.90355 | -61.16943 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5896085f-65b9-3126-81ae-19570fcb1e12 | -9.93825 | -60.71444 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 130eb28c-af60-343a-8090-2ac08857c5a2 | -6.77348 | -63.14721 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06a4557d-8be4-3b3b-a1fa-f8d698b07154 | -9.0452 | -65.4268 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9eb77d-e9b0-3845-a88e-d9caeb9b636a | -7.90284 | -61.17496 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8d28f32-57e9-3e86-8317-cdec7eb1d980 | -7.8945 | -71.69394 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00151c21-7f1d-3796-a93c-418f1a503f8c | -9.03821 | -61.66207 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c809f70c-f145-34d2-a733-bac22541fe73 | -8.92938 | -61.48299 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2f9a010-c7c8-3bed-bb72-84016439745a | -3.80903 | -58.88392 | 2026-09-24 06:25:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63f93950-52e3-3128-bebe-7557d0126588 | -8.00582 | -71.30721 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdd0e4c3-3e97-3f47-bb03-f4f6835ba8b7 | -7.87082 | -70.67715 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e73c2491-6908-36ef-bfc8-c8a9f711f4ed | -7.66765 | -66.99262 | 2026-09-24 06:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997c6dbc-1c0f-327a-9140-5bcbfa211b7a | -3.68393 | -60.55222 | 2026-09-24 06:25:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7725292-b288-319e-a8eb-a723316ba73e | -7.05076 | -62.93539 | 2026-09-24 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6285bb4b-bf22-38c6-9126-6132efebec21 | -6.76829 | -63.14248 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68be9c9d-5321-3269-b90e-5c8dcd26e764 | -7.76979 | -72.98474 | 2026-09-24 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d470847-2656-3d26-b477-604258b83d62 | -7.71326 | -73.08339 | 2026-09-24 06:25:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 652800f6-8927-398d-a61f-38fc6a656527 | -7.55877 | -69.9052 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64187380-c2d9-3294-9d78-05c7b29517b2 | -8.36549 | -70.8046 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcfc93d1-aa9e-3937-baa3-f057725347e0 | -7.66701 | -66.99706 | 2026-09-24 06:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f63eb6d-d0e0-3103-aef9-173115a509f6 | -7.52201 | -70.39764 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c83ab31b-3ddb-353c-80e8-eda3ccf00616 | -8.95411 | -71.53271 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d5a9916-4676-345d-90ff-c3eb58694baf | -7.37083 | -70.1192 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c74e921-0568-3a1e-a80a-ca9cc2ead635 | -8.38949 | -71.07959 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daa248b2-12c0-35fe-9edb-2d8782114d53 | -5.10453 | -60.26092 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 841a09a3-c5f8-37ed-aea7-114e08a89e69 | -8.90745 | -71.34378 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99beeca2-9bf5-3bb1-a6d8-d3f669128fc7 | -8.91053 | -68.64088 | 2026-09-24 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3eb5a93a-d202-3352-b98b-fdbf8a79e625 | -7.52137 | -70.40182 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8678f7f-ba9a-3442-a29f-48ff1a6d8cf8 | -3.81179 | -58.88663 | 2026-09-24 06:25:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9f809fd-e2a1-3df4-a1d4-42ad7649d2a3 | -7.6623 | -69.93214 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d11cf06-e825-3db8-9126-4f4cfd1702f3 | -8.79245 | -71.05538 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea790074-2fab-31e3-9c16-4aa875a0c150 | -8.39009 | -71.07561 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cd2e2a8-e6aa-335c-9e63-ccf620b5afe8 | -9.04599 | -65.42083 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08cf3e7-1386-372a-a38f-047575fa422e | -9.72584 | -65.02822 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0e54510-1b0d-3707-848b-09a2d1d48326 | -7.88486 | -61.17186 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8da082a3-2c6f-3230-8ed0-c6f2fa9e6c2e | -9.04759 | -65.40886 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a41bc1d9-23a5-36b7-aff9-9f418622d93e | -6.53141 | -62.93745 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf8ba41-9035-37ca-a862-1d0d9d94cf4f | -7.89067 | -61.17863 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23fb2e08-828d-39f7-9f67-eebc5b758695 | -8.92329 | -61.48678 | 2026-09-24 06:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1a9efe3-960e-3c0f-81d3-bf5fc08c829c | -9.04249 | -65.40815 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b817768-f50e-3358-bf05-e7c29cbb6f10 | -9.22388 | -67.394 | 2026-09-24 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2be7b1cb-5897-348c-abe9-ad160f69a0d8 | -7.51903 | -70.39294 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a0baac2-1e6b-3e43-a02b-a8915a89f9dd | -8.88829 | -62.54357 | 2026-09-24 06:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c91f011-1524-391f-ba16-109224ee8806 | -3.68471 | -60.54685 | 2026-09-24 06:25:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260e9c8e-7268-3401-b719-dd9a150d55c7 | -7.90852 | -70.19978 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc170454-6135-3ef7-a577-8f47f9d96919 | -9.93748 | -60.72105 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6575ae67-04a4-3016-9cdb-862a16d33f0d | -6.53084 | -62.94157 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c180dca-88e5-3a2c-8296-292b2b6c59e7 | -9.93282 | -60.71494 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcc3fa02-819d-356a-9ea1-517ba0378b27 | -8.90805 | -71.33986 | 2026-09-24 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 696010ee-7a25-3794-8e7d-46607cf4cba4 | -9.22004 | -67.38898 | 2026-09-24 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517b1d58-1c6b-3f27-9a54-ec9ecba26e68 | -7.89218 | -61.16737 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 371eceae-62a0-302c-820a-4b5f4b3877be | -7.04491 | -62.93459 | 2026-09-24 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a223ff5-ac7a-3737-975d-7f2228445c57 | -9.93896 | -60.72235 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67452b06-6784-3ad3-81c5-33479e42c743 | -7.88241 | -61.17733 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec83da7-c609-36e3-94f9-76a9dafeb42e | -9.51057 | -66.76627 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e3daecb-6376-33d6-a161-ece86d5afad4 | -7.69331 | -69.92779 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a384a0cd-88be-336f-aaba-e7fbc25c5582 | -8.36208 | -71.18835 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5143e0f-f1ac-3d48-96dd-fab5d2cca2a5 | -6.01127 | -59.94091 | 2026-09-24 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 712e1f39-0e71-3582-8be0-3687bbfb0440 | -8.63259 | -66.99192 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c98f05c-bb6d-3db0-b4aa-ce51e747f2c7 | -8.77311 | -72.77317 | 2026-09-24 06:25:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6855868c-5881-3de0-90ea-47bcfbee75dc | -9.72627 | -65.02493 | 2026-09-24 06:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e19797d7-4f21-36bf-b099-226129652bdf | -9.0409 | -65.42013 | 2026-09-24 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b061e6b3-4b12-3b0b-a6bf-aa9986264bbe | -9.10522 | -61.43565 | 2026-09-24 06:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89b3d13d-a5b9-3e28-be65-00d09714b985 | -7.89794 | -71.69447 | 2026-09-24 06:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c920ebc5-3b30-347b-974b-c2a82af286aa | -7.04547 | -62.93045 | 2026-09-24 06:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334577c9-3f02-3926-8ee6-58b93dd20cba | -9.93672 | -60.72756 | 2026-09-24 06:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a7cb061-4256-3e2b-95d3-0785fa25d0b3 | -6.77489 | -63.14576 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5843fc3-de80-337e-8902-3c574a6548ec | -7.51541 | -70.39242 | 2026-09-24 06:25:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 845e879e-8b40-3209-bca8-8a5d6f4c79dd | -6.77404 | -63.14328 | 2026-09-24 06:25:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fbe878a-c53e-36e6-b13a-3ed0bf8acf21 | -10.24199 | -68.29961 | 2026-09-24 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acd56ad4-8b93-3c31-a5c0-cb48f3aea796 | -10.24254 | -68.29565 | 2026-09-24 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53d61b7-1fb7-3412-852e-f343d358dff0 | -10.46297 | -68.25186 | 2026-09-24 06:27:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 727caa15-fb3b-3bd3-81ae-29ffbf1e10a9 | -10.23955 | -68.29661 | 2026-09-24 06:27:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3b11038-ca9a-373e-a06e-c5ad0704646b | -8.31473 | -70.5371 | 2026-09-24 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 774ce97b-4954-3d5b-aceb-23c09c77a538 | -10.24203 | -68.29948 | 2026-09-24 06:46:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23d2bd53-62a4-3fa7-974e-a91a04806061 | -8.38706 | -71.08002 | 2026-09-24 06:46:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a62742c-c9f4-3c80-87ea-e87937749587 | -8.38662 | -71.08328 | 2026-09-24 06:46:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed570541-3968-3c8b-b39f-790009a9bd77 | -8.38752 | -71.07666 | 2026-09-24 06:46:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebfada83-dc8a-3a22-af79-a5744288f5b9 | -8.64313 | -67.03203 | 2026-09-24 06:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9c251a2-5d2a-3d35-9b49-10bcff549161 | -8.11094 | -70.13812 | 2026-09-24 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 351dafb1-6e0d-3c28-8afa-6e2d58e1a685 | -7.95078 | -72.93506 | 2026-09-24 06:46:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84366a15-0634-31c2-8702-419995d4ecc1 | -7.95278 | -72.93402 | 2026-09-24 06:46:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README88.md)
