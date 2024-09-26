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
| d47d1a47-73bd-3aae-91e5-bd9a097fd8f3 | -20.6284 | -51.4945 | 2024-09-26 02:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| 667e0017-db16-39cc-b8d0-8f2f9aa0cfaf | -21.9374 | -48.5688 | 2024-09-26 02:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9e0452f8-3ed2-3f2a-8566-ab2f428f872f | -21.9381 | -48.5453 | 2024-09-26 02:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b6ad6fe0-543c-3205-bd65-1c6ed60100e2 | -2.6601 | -57.5507 | 2024-09-26 02:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 13c39b52-82f7-3a47-bc16-ad2d03387f5b | -2.6785 | -57.531 | 2024-09-26 02:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9e5a1ca8-610c-3d42-8662-79b068b8fed8 | -2.6968 | -57.5307 | 2024-09-26 02:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ab4ac4d7-63e3-3070-bd5d-a19381552b13 | -3.5488 | -50.38 | 2024-09-26 02:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c0167648-10ba-3b62-8ca5-fe8e651289a4 | -3.5673 | -50.3794 | 2024-09-26 02:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 3a692a2b-8376-38af-914a-49485f8f2060 | -3.9208 | -46.4459 | 2024-09-26 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 37d9cb63-ede6-3a8c-a626-47c039e97c49 | -6.784 | -59.3052 | 2024-09-26 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 25e520e9-1b17-30f2-b6fd-15df13c93ce6 | -6.8024 | -59.3044 | 2024-09-26 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| be0d3f3f-2d54-369c-aef1-7fe301f1238a | -6.9305 | -63.1241 | 2024-09-26 02:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| df1ede81-3f14-37b5-9c42-ccb35bf0c320 | -6.9306 | -63.1053 | 2024-09-26 02:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a7fea989-1e8d-3690-935c-c23d37e6f84b | -6.949 | -63.1048 | 2024-09-26 02:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| add04f6a-aef4-3bd5-a32a-b1e72a966dff | -7.3637 | -55.5134 | 2024-09-26 02:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 237.7 |
| 3b777c1d-f7e0-3dfe-a17d-979207f54c9e | -7.3639 | -55.4935 | 2024-09-26 02:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| fb0988a5-ce77-39e8-9b44-ee65baa4a041 | -7.3823 | -55.5124 | 2024-09-26 02:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 7b4839a3-cc17-31b1-a41d-60659049c08d | -7.3824 | -55.4924 | 2024-09-26 02:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| cf9120f8-41b2-355a-82a5-11bd1beb1d37 | -7.5894 | -42.2971 | 2024-09-26 02:35:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 94456693-748d-351a-848b-b8d91e628057 | -7.5705 | -55.1617 | 2024-09-26 02:35:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 86919beb-5135-30f7-ae8e-2cac276ad556 | -7.5768 | -62.8017 | 2024-09-26 02:35:50 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 326866f5-2594-3605-9036-947b82104c1e | -7.5769 | -62.7828 | 2024-09-26 02:35:50 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1e241a0d-e469-33c8-a411-6379eac639bc | -7.7968 | -54.7464 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 439ab2ef-296d-3155-a056-d3fea1bc5810 | -7.797 | -54.7263 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 59ec1090-c510-39ff-9f14-0ca9fe080353 | -7.8154 | -54.7453 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 49320c36-8fb6-3bef-930d-2701472d737d | -7.8156 | -54.7252 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 238.4 |
| 3f203ea1-dbc5-321e-9a9a-58ad4fc6795b | -7.834 | -54.7442 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 5feeb27f-5b2b-348e-84d5-903955583c96 | -7.8341 | -54.724 | 2024-09-26 02:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 091a9c66-15d1-3acc-b01f-0d4874f07761 | -7.9353 | -71.4725 | 2024-09-26 02:35:52 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6a5173f4-52e3-33c6-9916-cfb9f72871f3 | -8.1394 | -61.2817 | 2024-09-26 02:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2c8353d9-0c1b-361c-9513-5eddb8f9c464 | -8.1757 | -61.3946 | 2024-09-26 02:35:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 51268fc3-3941-3ed3-9867-8fa29bc023ee | -8.3155 | -54.9956 | 2024-09-26 02:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a563f636-de49-350d-bc12-5ac17032d804 | -8.6847 | -67.0097 | 2024-09-26 02:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| cc96986d-e099-35c0-9d49-17fd32686bb7 | -8.8096 | -58.2367 | 2024-09-26 02:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e4f13f87-8f0c-3a5e-84c7-9b9de3a22d5b | -8.8098 | -58.2172 | 2024-09-26 02:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d0c1d2c9-c822-3fc8-bdb8-281dfaf8b092 | -8.8284 | -58.2161 | 2024-09-26 02:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 13ca99e4-1742-39f6-8150-a00c8660bfea | -9.086 | -61.1245 | 2024-09-26 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c88c821b-88ce-313f-b950-e993eb796361 | -9.1046 | -61.1237 | 2024-09-26 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3c6b79f3-78ce-3d8f-b061-f4bf7280a573 | -9.4136 | -65.4614 | 2024-09-26 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| d540b60d-3f1f-3118-a65c-27353c992b03 | -9.4322 | -65.4607 | 2024-09-26 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d22ffd23-14af-36dd-bb46-8bb77e5af075 | -10.3882 | -67.8737 | 2024-09-26 02:36:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2008e6f0-82f4-385b-a1e3-c09b0ffdab84 | -11.222 | -45.536 | 2024-09-26 02:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c28d9a28-f6d9-3beb-b6af-2b4e43929134 | -11.2412 | -65.2997 | 2024-09-26 02:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 43ffe924-12bd-365b-b060-82dabf1fe33f | -11.2599 | -65.299 | 2024-09-26 02:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 9e790e86-a09f-3a16-b73d-2d57f23207fe | -11.26 | -65.2801 | 2024-09-26 02:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 47d93829-ab7e-3fbb-90a9-dd675e767462 | -11.2786 | -65.2982 | 2024-09-26 02:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| b11e0d20-3886-34d3-a551-512a6ac19d13 | -11.2788 | -65.2793 | 2024-09-26 02:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cfb44cb5-7f6d-397f-b8c1-e1a4d869f334 | -11.7179 | -47.8551 | 2024-09-26 02:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 8f9fbb99-c597-366e-9dd8-fe6c917a7573 | -11.955 | -60.363 | 2024-09-26 02:36:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f1dc4a71-fbd5-3bc1-8621-72b9ed50c00a | -12.2175 | -45.5074 | 2024-09-26 02:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 02ef8f96-31ed-3466-816e-871ff3bfcd42 | -12.2367 | -45.5045 | 2024-09-26 02:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5065f2bd-cbe5-3270-accd-36b4bc3bef2e | -12.5273 | -53.5168 | 2024-09-26 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 33719c82-7de4-3446-b6f4-317d9347693d | -12.5276 | -53.496 | 2024-09-26 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 9d4caaff-ca5f-3f61-842f-2f6a3461650b | -12.5279 | -53.4752 | 2024-09-26 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a981d4d3-be7f-3957-9fef-c017798ac41e | -12.5464 | -53.5147 | 2024-09-26 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 162eb573-a17e-30c1-b599-8f309aefacbb | -12.5467 | -53.494 | 2024-09-26 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 204.2 |
| e5cd3236-3c9a-3a5b-b48d-dc81f5379442 | -12.841 | -62.7067 | 2024-09-26 02:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 3dcdd189-2d1b-3564-baa3-44e2cdbd2764 | -12.8411 | -62.6874 | 2024-09-26 02:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |
| ed83d65a-798b-374e-90ea-5b0876af28f5 | -12.8599 | -62.7056 | 2024-09-26 02:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6bf796d7-1ec5-3b26-b696-e77e0510310c | -12.8601 | -62.6863 | 2024-09-26 02:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 193f6503-a529-3f3a-964e-17fb4fe0bcd8 | -14.8957 | -58.0074 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fe2cce6b-b5b7-3450-bcb4-ccba7fb7acdf | -14.896 | -57.9873 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 275d8b5d-1439-3d80-bc5d-2558ecc9506a | -14.915 | -58.0055 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1ba0f79b-a362-385a-a280-e75034967b0a | -14.9153 | -57.9854 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 76917033-2ba8-3689-8b89-7f15ab7e736e | -14.9156 | -57.9653 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 12bb9827-0203-37d3-a822-9c3f6b3bd66d | -14.9348 | -57.9634 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 6d96eea8-3224-3aee-8977-e084ec554733 | -14.9544 | -57.9413 | 2024-09-26 02:36:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b952cb90-9744-3482-8865-4ea7f41a370e | -15.3175 | -58.1872 | 2024-09-26 02:36:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 861e5414-cbe0-3047-ad39-7f5837427dcf | -15.3371 | -58.1651 | 2024-09-26 02:36:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d43291e4-ad61-315c-8b6c-9bf0d1b4ae40 | -16.098 | -52.0111 | 2024-09-26 02:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| e349932b-1f8c-31bb-a898-d3fa43760b01 | -16.0985 | -51.9896 | 2024-09-26 02:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| b5dca974-c2e9-3ff7-8c45-db7e50e3a604 | -16.1176 | -52.0082 | 2024-09-26 02:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 172.3 |
| a770ea06-3c29-38b1-8ee1-8a1a11695f33 | -16.118 | -51.9867 | 2024-09-26 02:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 169.7 |
| cd660acb-613e-3633-9b7c-93995428e6fa | -16.593 | -56.0067 | 2024-09-26 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| c1c664b6-2259-3bf1-879a-bbd75e517a2d | -17.0795 | -56.1736 | 2024-09-26 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| d13c9cee-ee12-3711-939d-2ed5b178c2f3 | -17.0798 | -56.1529 | 2024-09-26 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| bbdb2560-66de-382b-b5e4-527ff2eec10c | -17.0991 | -56.1711 | 2024-09-26 02:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 01d4b1b6-fbe6-3436-b07d-2b08b8fd06cd | -21.9374 | -48.5688 | 2024-09-26 02:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 38bbef83-444b-3ea2-aa2b-df55bf239440 | -21.9381 | -48.5453 | 2024-09-26 02:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d6582ffb-e77d-33cd-aef2-8442de6d24fa | -2.6785 | -57.531 | 2024-09-26 02:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f6a497c7-cb28-3de5-abd6-ab65797b2a93 | -2.6968 | -57.5307 | 2024-09-26 02:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a0cfbd27-905f-39d9-a253-4774e3e6ef5f | -3.5673 | -50.3794 | 2024-09-26 02:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 3f4c2b4d-1f79-3380-827e-3e20baafec62 | -3.9208 | -46.4459 | 2024-09-26 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| efcc0d7c-f4a1-3c82-89d7-4853975d2b02 | -6.8024 | -59.3044 | 2024-09-26 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 69932a5c-3366-3590-836e-8187c189804b | -6.9305 | -63.1241 | 2024-09-26 02:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 1940af4a-996e-39c3-aebe-3162cfee6159 | -6.9306 | -63.1053 | 2024-09-26 02:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 09078a77-8b7f-3798-998d-aaff1a9c5bb2 | -6.9489 | -63.1236 | 2024-09-26 02:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8bdf7620-4b36-330b-8b8b-e6485ca36caf | -6.949 | -63.1048 | 2024-09-26 02:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| bca2cd95-49ea-365d-bbfa-08110a9d4681 | -7.3636 | -55.5334 | 2024-09-26 02:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c80271c7-9bb9-3186-b345-e8f569378ff0 | -7.3637 | -55.5134 | 2024-09-26 02:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 266.7 |
| 72f79669-c432-3b50-a778-35595ff088bb | -7.3639 | -55.4935 | 2024-09-26 02:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| e35f5af3-098b-36c7-9432-c6b079318160 | -7.3823 | -55.5124 | 2024-09-26 02:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 198.3 |
| cd683bc0-7b4f-3b40-894b-d545a684b310 | -7.3824 | -55.4924 | 2024-09-26 02:45:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 181da3b6-eb8b-3bd1-89d2-d025d3980aec | -7.5894 | -42.2971 | 2024-09-26 02:45:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 8285a7f9-dd7c-35bb-96c5-3676d1b98bf4 | -7.797 | -54.7263 | 2024-09-26 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 93d5fedc-1b28-3519-a384-299a2ca27ae7 | -7.8154 | -54.7453 | 2024-09-26 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| f235cf36-b518-368f-9763-f6eea0ef7ef9 | -7.8156 | -54.7252 | 2024-09-26 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 235.7 |
| e2beb05d-e0b4-3213-b29e-e8418f5727db | -7.834 | -54.7442 | 2024-09-26 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 549cc5a0-c5a7-3c1e-89a5-43a344292502 | -7.8341 | -54.724 | 2024-09-26 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 02753841-e872-34a0-8a32-904793ca4d93 | -8.1757 | -61.3946 | 2024-09-26 02:45:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |


[Clique aqui para ver as próximas entradas](README47.md)
