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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9f3fe2f-2e28-3e8f-bd18-cc0bf7a9c713 | -8.45286 | -70.72422 | 2026-09-01 05:36:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04491b3d-5107-356b-b402-53e5a5affe4c | -9.21011 | -60.87772 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce26f781-2a46-3679-b81b-3aea3f6fa36b | -9.93646 | -60.51233 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cada8fa8-ca26-3144-8816-9616181628ba | -8.62155 | -54.8555 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 275a4a69-fe8d-3815-8667-702cf307a14b | -6.86578 | -59.47672 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fb541d2-1068-36bb-bcdd-c72f6136f7d1 | -5.88949 | -57.75452 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 547b4ff6-1db8-32c7-9c86-7ec74bc112dd | -9.15099 | -59.5342 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5a2c8c-6c1e-3ddd-a3b3-c402afb1a9cf | -8.48484 | -60.5453 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2ea628-2647-353b-9a00-4c0aac4888ca | -7.56956 | -60.46094 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11fb0dec-2ab1-3db5-8ef6-4862d3774286 | -6.9552 | -55.64613 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9fe89017-49d1-3c98-ae9c-00e04611b784 | -7.33616 | -60.59124 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da63fc7-8c2b-37a4-bc76-aaddbcbe5d9e | -5.581 | -60.23281 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6831a9d-8212-3e43-a2d9-575bcaccbf2f | -6.11845 | -57.69504 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e39967b-e963-3d7a-a438-aeda5eebe81d | -7.34758 | -60.58543 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c354288-ae50-351b-82c5-55418bb09f26 | -6.72435 | -50.46951 | 2026-09-01 05:36:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b5d5aa0-078a-3faa-a797-606eddfa0471 | -7.34871 | -55.20252 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b51fd59-e8fe-312d-b761-3c502dbc824f | -7.58676 | -61.34599 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f56c988-c3a9-3e4b-81dc-8a64c936aa47 | -7.31328 | -60.58021 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a443603b-31c3-3de5-9b12-3f9ce9699d23 | -8.71682 | -67.11408 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc12527f-5b49-3b23-960b-7e76123c56f0 | -7.73209 | -60.97613 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13529b07-ea8a-31f3-8750-b4971153bc99 | -6.12545 | -57.67561 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0017afa2-0021-393c-97bd-17832ba82e9f | -9.88855 | -60.27575 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 329a393c-e920-3d44-a708-80c3c6e61dab | -9.15702 | -59.54393 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9257fd2-9507-3226-b3ef-4891eb1de645 | -5.95976 | -57.684 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10908234-13ed-3b30-82a1-95c82a9b440b | -7.34472 | -60.58115 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 640113e1-e53e-3688-b029-399c70341903 | -9.4675 | -57.025 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ca6180-9abf-3a9f-862b-07c9bab3afe0 | -9.45625 | -67.45964 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 229f6e49-f956-3131-93b1-4d1b268ad1c7 | -8.94812 | -62.3662 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2e21094-df01-3e88-aa99-de3adce56e76 | -8.79151 | -62.49889 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14a32e2b-afa1-375f-b4a2-f7a4c6830445 | -9.45151 | -67.4562 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5de8c034-ec07-394d-ab6c-694eee9a424c | -7.0255 | -55.64184 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98a6c696-2ba6-31c8-83a1-621646e7d570 | -8.68811 | -62.9389 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72701f09-d564-3882-9dfa-d137b724c3cd | -9.17356 | -59.60783 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55bc65e2-6d0c-3995-b05c-858f50188911 | -6.42019 | -52.20193 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d3038f-9bbc-3ba4-8620-1dd6d2b03c8e | -4.93033 | -62.42728 | 2026-09-01 05:36:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba0e156-af72-389b-bde0-72048aa64ffa | -8.50015 | -55.31296 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849fddca-6c9c-3fa8-8966-5c9a8b34fdca | -10.34137 | -50.00465 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90442fb4-188e-3fa0-9c75-606ca4a7e56c | -8.93484 | -62.3641 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fe1d8e6-4407-3c79-aaca-44fb11093611 | -11.25754 | -50.57269 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2be8947f-e550-32d9-8f73-506ba09363da | -6.56254 | -58.56226 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad0a0717-6e88-3fa3-913d-8f802bdd7487 | -6.1223 | -57.66998 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fc83761-5318-3396-95ba-1efa5dbef664 | -6.6064 | -58.60086 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7143dbc4-110b-30fa-9876-ac5ff6fab01e | -8.61826 | -54.69436 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6ea5c78-23d1-3705-ba16-befafc18b12b | -9.03281 | -65.43295 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fdb261c-6c21-3d84-9434-71acb461ac2b | -8.60247 | -66.96115 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3c893c9-6e8f-3ce5-9ac5-1cc95fd57473 | -6.7055 | -63.18452 | 2026-09-01 05:36:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a17b34c2-c29e-3324-ad31-8a846305b681 | -6.92418 | -55.62921 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa8cfd4e-c908-34db-bfd3-5ee3dc50e0c3 | -9.15091 | -60.94687 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7173e96f-a0ae-3e27-92f2-c78e567965a3 | -6.78653 | -55.64489 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4761368-2049-348f-b9e8-9edafa7a43fc | -7.57473 | -60.47334 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdfbeea3-b3af-3321-b636-51c75cba2eeb | -7.03135 | -59.22041 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f306113d-a2c4-3a27-97f1-ea35d3b543c1 | -9.02734 | -65.44411 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc502878-97ee-3360-ad91-4a24ff9b77da | -6.01577 | -57.82077 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f259983-e03e-3a3e-aeb8-1471fd1f56bd | -9.17761 | -59.6303 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9deb223e-9e6e-3680-8557-7495173baca0 | -8.71249 | -52.36296 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ad59ea6-d966-3b5d-95dc-01dd31a5376d | -7.57645 | -60.48518 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad55589a-8ef7-363f-8551-f079df899ba3 | -6.88171 | -56.5083 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d86170f-5c14-35b5-afe8-ecfa49ae9023 | -5.49173 | -57.14524 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 441f069d-d761-377e-b15b-34ea3863cf72 | -7.57835 | -61.33368 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e77c2db8-d1bd-342e-8747-8777180756f1 | -7.58394 | -60.45926 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e20320ce-18b0-3d33-8b8f-d5a24872eb64 | -6.69756 | -55.41571 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c99cc79e-850d-3681-b9b6-eb35cf83d1e5 | -7.567 | -61.20692 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9114b9a5-1163-36a9-8d7b-290856566f9e | -6.88802 | -59.45084 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 393f6b83-145b-3a11-96ea-4813addf090b | -6.93647 | -55.64051 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1d26674-fbbc-30fc-9d98-c8552d59d7bc | -7.56439 | -60.47172 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10237e1b-524f-3bfd-ab77-c7172f103d7f | -9.37006 | -60.31352 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 568d3e6e-a652-3d27-93f3-f40fb5a51e4e | -5.57307 | -60.19355 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81027aec-2539-31f7-bd94-2f31e28755fa | -8.72716 | -71.02428 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa04efdc-77a0-30f4-ae36-cfbe579f29ec | -6.96431 | -55.64735 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48530fc6-81d5-32b4-aaba-6f1889e1d09c | -8.80863 | -62.49804 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e98fac0b-d118-314a-b108-f29262a7a805 | -7.62878 | -55.28654 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cefdbef-bd94-3647-bf61-98f91fce2a75 | -8.5879 | -66.97783 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5864465f-d86f-34c9-a2c2-e46d52e5f9aa | -6.02447 | -57.68098 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59b8741c-42fd-3b37-9f5c-57d22adfa222 | -7.57947 | -61.32653 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f831ff-5a49-31ab-a764-4b80d9c8814c | -7.57301 | -60.48462 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e715bf6d-b253-3c23-a1ff-89ae3a839a4a | -6.31178 | -53.54749 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb1a5a30-962a-3d68-b74c-0ace26b1d2df | -8.79263 | -62.51336 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac0a96b6-1780-32b0-af43-6be3664e0ec4 | -9.93879 | -60.52082 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 407616f2-bae9-3750-b3b5-fb156d1b1847 | -6.94033 | -55.64584 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed2e1628-8135-3870-872d-b85560dd2510 | -8.79595 | -62.51389 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed904dc-8926-348e-b640-dfaace694a27 | -7.18403 | -55.48443 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faf78665-2544-3339-8cb0-f4c5a4f19883 | -8.99967 | -65.43237 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83d023b5-5c12-3afd-ac8b-a5a34c4bf371 | -6.59657 | -58.59013 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f3125d1-21a2-3402-bfa0-410caa7044e5 | -6.82552 | -59.5742 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 906e3e35-c3bf-378d-8f4f-65b77fd14129 | -8.265 | -62.75686 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2d213b0-b92a-3082-9225-7303165984ae | -6.95065 | -55.6455 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 143bca0d-aaca-3c94-a15a-ab6e13cffae5 | -9.13483 | -61.09765 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f0f539b-aaaa-3c77-952a-fea2df2aedf6 | -7.9296 | -61.34802 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04667c52-e16b-3210-96d1-14769e4871b9 | -10.32588 | -49.95726 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bca7e3d8-0aca-3f15-8e5e-b5f64603c581 | -10.36201 | -50.00723 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 39152386-b6df-33d4-b764-ed34abeee19f | -8.79318 | -62.50988 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd3c1693-e879-3d40-a649-ab5e0000f3b5 | -5.48212 | -57.1546 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b2e9616-01ef-3358-a066-dd196d501f6f | -6.59284 | -58.58957 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62a5df87-d1fd-33fc-b6bb-486cf84640fb | -8.04213 | -61.73357 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79891cbc-5ea2-3446-82ae-ba7eb8151c8c | -9.02537 | -65.4559 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef295b43-92b5-3ff2-b002-a408e296c6a6 | -6.14977 | -57.91233 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31e2c6f0-886c-3e9d-b88b-30060d01b05a | -5.59126 | -60.2344 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bafd600-6fd2-3c16-9b67-c2425f1cb913 | -6.95194 | -55.63622 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fca7e6d1-57a8-3dbe-9fd4-7ce34179def4 | -9.02987 | -65.4455 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c24a2d13-0e9b-31da-9e1e-5290cc93cf88 | -7.58173 | -61.35618 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README76.md)
