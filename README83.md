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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4496247b-3acc-3ebc-966e-b1e5bb4ef025 | -16.64202 | -55.91348 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bcab0ece-f850-37d7-9fce-eccb55bc43d1 | -16.62234 | -55.90588 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| eb57992f-bf27-3bc5-aa8f-f9cf1b17d4ea | -16.61878 | -55.91112 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 33babc2c-7d51-3878-9ee8-f40145b2e0ef | -16.61753 | -55.9174 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a0a3fc65-da93-37a4-af03-fdac313303e0 | -16.61691 | -55.92054 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 75cc55cd-d862-3719-b41f-085f8ce990a1 | -16.61307 | -55.91314 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8a825034-be8e-340b-9ef5-5b9fdf5ae8c7 | -16.61182 | -55.91943 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e1c37aa8-f710-347f-921b-5a7f2edf0aeb | -17.14602 | -56.47962 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bf7d4f17-0952-36bf-a1aa-805606a046f9 | -17.08802 | -56.68344 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 6fad13be-75fc-36cf-818b-21bfb281a6b2 | -17.08731 | -56.68689 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 4e9ce548-4d7c-3530-bc7b-3a6f4c8a0fa4 | -17.08344 | -56.67877 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 73b78bd4-1711-3451-ac54-015de831affe | -17.06616 | -56.68204 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f92e0a15-c835-3a22-88c4-239b82c97002 | -17.06087 | -56.68083 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3d883093-c5ea-3152-ab6e-b153084562cf | -17.04286 | -56.68755 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a1ff263-deea-3bfb-a320-646b60a792e8 | -17.02699 | -56.6839 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9774bd4a-df81-336a-bbfc-32b91285b9ef | -17.02097 | -56.68616 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4e031ec3-c0cc-3431-9ed4-abaf04039e35 | -17.02025 | -56.68961 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 90a303a6-d133-3840-ac2c-cdab7309a4fb | -16.93674 | -55.84528 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 756ac49e-5989-3414-b273-a0306541fe89 | -16.9317 | -55.84416 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d7eb272c-ef36-3c20-8f70-604ad4045f4a | -16.92975 | -55.82769 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2aa4a5ad-1650-3945-9fd9-8bda5a335caf | -16.92853 | -55.83381 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aa6e10d6-16ab-3687-926d-62552991eb2e | -16.92791 | -55.83688 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cb94689d-9c69-3317-b661-f6453dd5b88b | -16.92534 | -55.82352 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34f7198f-4025-33fc-98c3-d0cb05d08815 | -16.92473 | -55.82656 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e1fc3777-b927-330c-89f4-ea169a7f7351 | -16.9235 | -55.8327 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 110606c6-5253-3cee-9a9d-6f1aef4ef1f2 | -16.9197 | -55.82545 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2037b4b8-863e-3400-a13f-fe94287c630f | -16.86634 | -55.85523 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 57144dd0-a130-3499-967b-66d11e792725 | -16.69008 | -55.54985 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| fb941cde-bb55-31f5-ae63-ee709ee08ddf | -16.68631 | -55.54271 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 02024d85-9524-32dc-8ce1-149ed7c13a0d | -16.68616 | -55.5436 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7482b292-0df9-3e46-9888-1c1aa4d451c9 | -16.96415 | -56.14433 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a666e5ee-db92-3e6b-b78e-5accac5301d8 | -16.88965 | -55.87011 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7f5f6a18-03cd-319f-9f9b-2f63e458f48b | -16.82252 | -55.89975 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7ef2d414-2631-3fac-a6f7-5496dc8c0d66 | -16.81683 | -55.90176 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 685f4b1d-58a4-35f9-9c35-9aa5469b55c2 | -16.81239 | -55.89754 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1309d9c3-62d9-3b3c-8dba-8d4c42d42d18 | -16.81177 | -55.90065 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| be78598a-c3e3-355d-b2ce-e8d85efb106f | -16.69851 | -55.92273 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1e450598-b232-39eb-8943-6d3992e17949 | -16.69469 | -55.91538 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9d0bd680-606b-36e2-8d0d-42aa3105b467 | -16.69343 | -55.92162 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4fe7d914-825f-3cbf-99bd-012177262222 | -16.68962 | -55.91423 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 93cd9266-b9d5-3b43-84c9-b17cbe3d7130 | -16.68899 | -55.91736 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| b693f444-cb40-3d21-ae57-c0b81427c1ff | -16.68831 | -55.89438 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c1752f0-f24c-354c-81b3-3a4a0d769e74 | -16.68706 | -55.90059 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8ae6dbd1-022c-3baa-ae24-afcf4c3d5f9c | -16.68643 | -55.90371 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 8939102d-2177-3de8-bc66-ebdd032106c6 | -16.68257 | -55.87035 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cd6d94c7-100b-3149-a796-63310d0944df | -16.68136 | -55.90259 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e91c2f16-311f-3b40-aa21-57db4eb4a245 | -16.68131 | -55.87657 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 657ad0c7-2e7f-33a5-aa0e-79b378be4fd5 | -16.68073 | -55.90572 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 69ccd61f-2f5a-3e6d-850b-1db5ae52fdcb | -16.68009 | -55.90886 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 676583ef-d242-3116-9b4c-572268132cc4 | -16.67057 | -55.90349 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9d1e518d-f726-3b08-aee1-02b8bd185379 | -16.6433 | -55.90721 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cfa8ac20-231e-3426-9200-fb38f7d98a4d | -16.62448 | -55.90912 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4476973b-a7c7-38e9-a37d-59f73d41950b | -16.6217 | -55.90899 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cabb4776-e3f6-3969-83aa-858da3054e62 | -16.62041 | -55.91523 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2d647786-61aa-382b-80ed-7ef7f054f140 | -16.62002 | -55.90487 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ea81d183-5e92-3902-a0cf-5a2d0115b221 | -16.6194 | -55.90799 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 35bb9550-e067-3df7-8ff4-490c8265aae2 | -16.61369 | -55.91001 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 1898fac0-26fb-3f07-a5d8-f10062504d32 | -16.61057 | -55.92572 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0f079981-6233-3983-8827-d3c5350a5747 | -16.60736 | -55.91517 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2364a2af-e031-38a0-b0e0-1caa7fbdfdd6 | -17.01781 | -56.68452 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 8efcaedd-2882-34bb-afd8-2e0743c9f326 | -17.01711 | -56.68799 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 00203b21-4942-3c74-b1f2-ac99adb90263 | -17.01568 | -56.68494 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 08fd523d-c7c7-3316-b376-dedf2072a319 | -17.01351 | -56.6953 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f822c041-b883-35a4-980a-69de72ba2561 | -17.01182 | -56.68676 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2ec92bc0-1fbf-3766-a83f-1ca56292f7c5 | -17.01042 | -56.69369 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6cdedb27-089e-3a12-b465-c1af913e3e5d | -17.00966 | -56.68719 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| d13b97ce-354b-3ed0-a32b-490f225c9abf | -17.15375 | -56.15037 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bd9097ef-878c-3005-ad42-98c5e13cec74 | -17.1531 | -56.15355 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 32c0f9cc-87fd-333a-83b4-3029b124c772 | -17.15048 | -56.16632 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4a8eb414-307b-31b0-8f50-9061f5f32ebd | -17.14982 | -56.16952 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 64709655-8ce9-32c5-9538-d17294798e4e | -17.14864 | -56.14923 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f3cfaf4c-bfd9-3ad5-9060-5074ce2045dc | -17.14668 | -56.1588 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 49c8245c-56ba-39d8-9ac1-4c4b2b4811f1 | -17.14602 | -56.16199 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1174307-6e52-31ad-9ad5-5941c4d389fa | -17.14536 | -56.16519 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aca749d6-42e4-3f1b-9a16-3f968ff16eae | -17.14471 | -56.16839 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ebaaa9fb-5afb-3bfa-8dee-e1ec4b743b33 | -17.14157 | -56.15767 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 60c3afe1-7313-3f8a-b8db-9160f3cedea6 | -17.10798 | -56.10223 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 416a62ff-b7a1-3cfd-95c8-005a12aaa549 | -17.10289 | -56.10107 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7e03a184-8bb1-348a-9e73-28927744e9d3 | -17.06219 | -56.06549 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 11331377-640e-3c72-ae7c-9be33b1a13de | -17.05775 | -56.0612 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| df1d8f01-8766-3ae1-93d0-fa87ef7676af | -17.05331 | -56.05691 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2ccc82e-3050-303a-91cb-68df74cc8dbf | -17.05266 | -56.06007 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bf5255dd-1a29-3617-b8ba-c59c7f8913cf | -17.04619 | -56.09161 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7fab0f90-78e0-3cf1-bb45-337f33e52a84 | -16.96992 | -56.14226 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d8889003-13f7-3319-bf51-4759ae7ba874 | -16.96927 | -56.14546 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23779dd9-8268-314b-925d-bd4fca0d19c1 | -16.93294 | -55.83801 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d0b95cec-7231-3547-920f-ba768073c675 | -16.93232 | -55.84108 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64b3e3bf-d4b6-3ccb-8f3d-2afbe9ef6813 | -16.93109 | -55.84724 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba5ffb39-2c19-369c-84f2-8bfebe1e11b5 | -16.92914 | -55.83075 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 221e1c5b-17ae-356b-a78c-88a7ecc0cd5b | -16.92595 | -55.82048 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b5cb65d0-16e7-3087-bf33-ae16d447b089 | -16.92411 | -55.82962 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4c23126d-cf20-3882-9580-d2a044d823cf | -16.92288 | -55.83579 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 51bdfece-ddf3-3c63-a37d-79a11767c18f | -16.92226 | -55.83887 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2c8f3864-4c0a-3c8f-b18c-790af3b96c44 | -16.92164 | -55.84195 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 18af0288-b17b-36d5-aa84-4d3f08ff3d0d | -16.91909 | -55.82851 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d2b8a29f-95b6-3e06-b9c6-2f60a17a803f | -16.91405 | -55.82745 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e418d21-747e-349c-875f-722e481e0552 | -16.89469 | -55.87121 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dff49574-3980-390a-beb0-ff8e5c3d5e05 | -16.87894 | -55.87094 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 03d70926-f55c-3fc1-8c9c-53d85b65b253 | -16.87327 | -55.87288 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0aaf16a0-833b-3301-8a11-d6906a4b7686 | -16.87137 | -55.85634 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README84.md)
