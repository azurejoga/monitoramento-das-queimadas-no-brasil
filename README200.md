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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b60dbfc-d705-3ead-b306-2103e1c9e429 | -8.59709 | -67.30209 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0385a5b5-09ac-39ff-a970-9417d4c6e718 | -8.07801 | -55.3022 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc62b8ef-3d49-3d9d-80be-375aff666d34 | -8.54326 | -67.07767 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d58125f-b7c3-3c10-98b9-46a3a14fe9cd | -9.17405 | -65.75675 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09da96b4-eb78-341a-9d17-d91d3cca4ea1 | -8.53805 | -66.97552 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc3e1358-6eb4-3809-9b9b-2210182549ba | -9.10255 | -65.35478 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba3f0b57-8bb1-30f1-a4d3-94f55bbd5998 | -9.05204 | -65.92559 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7318a112-f476-308d-8e09-6c216f1712c4 | -7.43967 | -63.54542 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 486f5db8-3639-384d-9f7d-168fa589ab24 | -8.765 | -61.38421 | 2026-10-08 05:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97676bac-c061-3350-8153-e00ee51909e2 | -9.47963 | -64.35175 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18ea3006-a9fe-305d-951d-74467fe14f60 | -8.0736 | -55.29506 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39ca4769-badc-3559-a56e-1a1af3aced94 | -8.2512 | -54.72785 | 2026-10-08 05:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ecbb76-4a41-3093-a01d-663f0a0da422 | -7.44244 | -63.54943 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 83f7ad87-3cc6-38a7-9bd1-b654d56fc01a | -8.59917 | -67.04617 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9f24a26-fcb1-3669-9162-0a81f6def062 | -8.08638 | -55.31962 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e33a3675-66a4-3b24-948a-ec40b36662e9 | -10.53474 | -68.01132 | 2026-10-08 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce8b9d38-f31e-370a-9fd8-1f1d3ba055fe | -9.68955 | -58.10287 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7744faa2-e64a-3e6d-a99d-6e0268a27974 | -9.51231 | -54.74786 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5d1cbff-4ca2-3ee8-8c98-29ae155c7779 | -11.74841 | -61.06236 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63509c51-19f4-3173-a32d-cf291fa7217c | -9.13658 | -65.2916 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a83e61a4-c199-384e-8786-179d073c54d9 | -9.05146 | -65.92921 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bc56365-d2f3-3775-a3b6-bef92876f047 | -9.06036 | -65.48946 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a3ae0d0-4a8d-303a-bdcb-b33ea0fba87c | -9.06427 | -65.48646 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb085ba2-894a-3fdc-8d27-2ae8c53e3053 | -8.99829 | -65.72444 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bb49cd5-9e62-36fc-a532-c6e724691d63 | -9.49111 | -66.78525 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da3ee300-947c-3fbd-80d2-439bfc17f28a | -7.44189 | -63.55292 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7ed43cd8-ea76-3f20-807b-5b0bc9c7c675 | -8.08726 | -55.31318 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42acbaa9-33e5-3d55-9335-39b665b3285b | -8.52872 | -67.01054 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35fd813f-7842-38a3-ad70-e79cf55625ad | -6.92188 | -63.01153 | 2026-10-08 05:44:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b5e5624-65ff-36d3-a5ee-f7befb7d29ca | -7.43413 | -63.5374 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1af556c5-1354-382f-87f8-fce13fbe9144 | -9.04809 | -65.92867 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43f67210-f134-36b4-97a2-c5e2f989f43c | -9.48184 | -64.35925 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de19f52b-f0db-3902-a5fe-d6758e35c568 | -8.62132 | -67.0214 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2643c217-e345-36c7-b476-6ce47ea7eeab | -9.48349 | -64.34879 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0456c6d7-a001-33e9-a618-bb8dfe9efbc7 | -7.43744 | -63.53792 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e3592c3-a8d4-3e25-b493-4d8da63d27bc | -9.14446 | -66.05612 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7632763-c140-3508-938d-00c50b95108c | -8.60421 | -67.30332 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74346b49-4446-3166-ae0c-480c62f0c13d | -8.62541 | -66.75687 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9563049-4037-38f8-9f10-67d58793318b | -9.34371 | -65.46304 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21f5160f-f8ed-3f2e-b79a-e30761c0fa7e | -8.51947 | -67.00084 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 568d6e1d-8093-3a54-8c78-390bde4fdc48 | -7.44298 | -63.54595 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e860ac19-4d8e-32cb-a2ca-1b38d3c41748 | -9.10978 | -65.35233 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da74ad9f-f761-3eb9-9ee3-28340742d633 | -7.43467 | -63.53391 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ec1eff7d-df43-3ba1-8634-cf9639cb9e2d | -9.52622 | -65.6599 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45d26853-8fd7-34ff-9448-495f6f585fc1 | -9.45588 | -65.45905 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0475d181-9370-3c67-8c50-813fbbe668ca | -7.44466 | -63.55693 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec2c2b87-2f2b-35c0-add3-9b5ed076b24d | -9.11926 | -66.01082 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a459519-b871-3af9-9c76-ac19bbed4d33 | -8.07933 | -55.29249 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31427bbc-b9c6-3458-89df-dc7e538066a7 | -10.23236 | -58.22199 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5687456-77b9-30c7-88c4-297d35534576 | -9.48736 | -64.36728 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3872ffc1-483f-3879-81d1-eccc79672347 | -7.43912 | -63.54891 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 99113e55-e5c1-3ddc-8ac4-6257749090ab | -9.54975 | -65.65623 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd80646-4303-30f1-ba97-7f0789e87597 | -9.49123 | -64.36431 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3b4c31-2814-3027-9e98-bc6897ac57e3 | -9.08984 | -61.14071 | 2026-10-08 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7043e7f1-9a65-394c-b0ce-2574a0c0c4c6 | -10.36397 | -67.94013 | 2026-10-08 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23197b9a-a70d-34ee-b71d-230ab06b7256 | -11.75664 | -61.05884 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 90d28773-93a3-3bbf-af08-d322c7731951 | -9.1421 | -65.29972 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5055213d-6efa-3697-a398-d919a10369a9 | -8.6165 | -67.02872 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 185799db-8c26-30d0-a2da-9d5bed1c0dd0 | -9.03622 | -65.74539 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2adf1ba3-454a-3842-8e9a-b095bf1a0413 | -8.84598 | -66.8037 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe70045d-9e73-3ff1-b7d1-95157bdc7a9d | -9.46517 | -67.11502 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23ecd332-8a38-3b3b-b522-58df47c01144 | -9.4868 | -64.34932 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21e1cb75-6340-3b9b-bb59-4d54eb0d6ff3 | -11.34257 | -51.87643 | 2026-10-08 05:44:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 997283aa-763a-3dce-8c69-54e92f1a6578 | -9.11644 | -65.35342 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98cc48c3-6889-31bf-a3f6-7a36ab872ff1 | -9.54142 | -64.81891 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c42305e4-05ed-3cf4-981b-71e7e85ca940 | -8.25072 | -54.73143 | 2026-10-08 05:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa6227ea-36a6-36fe-8836-34105f51e81f | -10.36564 | -61.22317 | 2026-10-08 05:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b98599cd-bcfc-3c56-b47f-719523544112 | -8.06307 | -55.2935 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f0c292b-e51e-382f-a2c0-6e2d61999173 | -9.1707 | -65.7562 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27555f2c-850a-3135-8942-f9920991b70f | -8.52991 | -67.04749 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ca3ae5-67d3-3f0a-9849-9cf8728caa84 | -9.6891 | -58.09678 | 2026-10-08 05:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f670974-21ca-370c-a9ff-2d753cf8f632 | -9.07762 | -65.48863 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847f3cbd-67da-3a55-b0ab-e2d76ce8131b | -9.46749 | -64.34267 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b7855e-e368-3a09-a6cd-ac01442580bd | -7.44521 | -63.55344 | 2026-10-08 05:44:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 941db177-da89-397e-a7b6-6aa0a6b16c04 | -9.48956 | -64.35334 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af222a2f-9654-3c8c-aebd-c4632b8c4247 | -9.14161 | -65.42623 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e513cca4-9a3b-3d8f-8de0-4935efbbe747 | -9.4857 | -64.35629 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40c50634-8255-3276-be18-57b1c9005038 | -9.22601 | -67.26792 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b71ae995-8384-3411-9c25-73c1a0efc1d3 | -9.48129 | -64.36273 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d09b9550-5e7a-3596-8d72-c4502def2f89 | -8.6529 | -67.18073 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5476f8c-403f-3c94-9e6b-33712ae73e3f | -9.13601 | -65.29512 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 582a5952-a5f9-330f-acff-5641c87b9e63 | -12.19938 | -57.12632 | 2026-10-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee372ec8-4eaf-3f54-b396-85577fea6e0e | -8.08285 | -55.3061 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb3d4d9-1ddd-32d5-96ad-47281213a13f | -9.04867 | -65.92505 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d0efbdc-d72c-3fb9-a230-d3b306aae38f | -9.22248 | -67.26733 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef19abb-8028-31d1-a10f-d5b95b93331f | -9.68653 | -65.0174 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5a85f86-b4b0-3d71-8155-ab8cf929f2c4 | -9.22529 | -67.52925 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 001bd14f-0df1-314a-8c73-5f8f590fba04 | -9.48625 | -64.35281 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18201843-4948-3df7-9ba5-547e0f4f9d94 | -9.39587 | -64.51694 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 117184fd-9003-37eb-aaa4-13988aa232f4 | -9.0576 | -65.48537 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a12f50-5ba6-3eb2-b0cd-83c135182ea5 | -8.5374 | -66.97945 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc00d6e7-5223-3f4e-a162-d674fd1cf55d | -9.51674 | -54.74856 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09c5074e-3924-3cb2-8b87-7b5af5357572 | -9.09048 | -61.13643 | 2026-10-08 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14488eba-90c1-3a60-b846-4dcc8c6e15cb | -8.08769 | -55.30998 | 2026-10-08 05:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fcbab6f-f2ea-3d74-baf4-68bfea1c8853 | -9.0532 | -65.91835 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8236e1df-827b-34e4-acae-34a90ec0673c | -9.49288 | -64.35387 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b93681c6-e0e6-3adc-9aad-882e3f735ea1 | -9.35153 | -65.74895 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12f9a05b-d734-3c21-888f-212525ebb442 | -9.04413 | -65.93174 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcaecacd-1483-3d7d-9432-ab2819e0bea3 | -9.47191 | -64.35766 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2594e11b-5a69-3118-9701-6db1c2bbd9d2 | -10.90045 | -57.08367 | 2026-10-08 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README201.md)
