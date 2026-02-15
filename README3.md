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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08e6038a-7c3e-39bc-8f63-9735e0279290 | 1.91759 | -60.57597 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c36f4221-abca-32dc-bbfb-1d082d99003b | 3.98135 | -60.53748 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a378bc3-e99f-3a52-93ef-5cd7bfe0fb48 | 4.54697 | -60.711 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c47d1a67-9ef0-3204-8e00-3e19024c334f | 3.93696 | -60.24412 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d85859db-f5f8-33cd-aa94-2782082187b3 | 3.72284 | -60.91506 | 2026-02-15 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07e03d7a-eec3-3e05-ab21-0eb65c45751a | -6.22327 | -55.63663 | 2026-02-15 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cee2a44c-5212-39b3-a2c9-8a6e2e955246 | -2.73708 | -58.1964 | 2026-02-15 05:22:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f9f7a1f-68d9-3669-9223-be11d9587576 | 0.90107 | -60.43653 | 2026-02-15 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1bc7188a-6a27-3c3f-a912-3e9c936129e2 | 0.8932 | -60.43353 | 2026-02-15 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bd6c512-d9d6-323f-834d-d7bb6dbc4406 | -4.36761 | -55.77158 | 2026-02-15 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5f20951-8661-3956-a6ac-900ee39aef91 | -10.99157 | -53.98881 | 2026-02-15 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 476d7246-17e4-37c8-b48f-accbf09eacc8 | -12.29174 | -49.03793 | 2026-02-15 05:25:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8739477e-3bd2-32a0-8954-8db17ca853ac | -20.47373 | -56.72748 | 2026-02-15 05:27:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d309f444-5bd2-3a41-8054-9ef1e7ec0834 | 1.8683 | -60.8383 | 2026-02-15 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9bd4819e-ad0b-36f5-91fe-98921b6b474f | -10.5937 | -44.331 | 2026-02-15 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 04b318bd-c16b-3345-8f7e-e9815b752728 | 1.8683 | -60.8383 | 2026-02-15 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c63d89fc-75a6-31c8-93f5-afd845226472 | -10.5937 | -44.331 | 2026-02-15 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 5c487362-2499-392d-94bc-6bfb2d5df0b5 | 4.39929 | -60.05979 | 2026-02-15 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c416f1c-4188-346a-94a0-90bc5843b8f9 | 3.81925 | -60.8923 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3c3a589-4359-3eb0-87f6-77019b6dcfb2 | 3.9411 | -60.25014 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8873a2db-cbee-31e1-9395-31b30eeb4aa7 | 3.72408 | -60.90999 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b276ae2-f310-3b37-997c-05f2e0c2485b | 4.03777 | -61.16184 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c7444ba-92d1-3c37-9d32-20fee2996cc5 | 4.54356 | -60.70615 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d7337e-8ebd-3bf1-8f25-599e45b32385 | 3.41658 | -60.34467 | 2026-02-15 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d6af2bc-7b77-3748-b784-90dca60bdd9e | 4.60277 | -60.75054 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 078cec8b-15d8-37ed-a33c-2c7f72d5c0d1 | 3.45393 | -60.26521 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a4bc5ed-1210-36d5-be7f-61a3c07408ef | 3.98323 | -60.53582 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fcc37ea-c4a6-3c97-86fb-c9eb814ea81a | 4.00561 | -60.3801 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926cdc9b-2dad-3130-baed-62ad7ec5bcf3 | 3.92322 | -59.6709 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89c2e24b-7f66-3b55-9e5a-fe10bdee936d | 3.93755 | -60.25068 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831f70f3-48bc-378d-bbd3-4808119d1e4b | 3.93629 | -60.24284 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 824eb3be-b24f-37c1-b890-d74bc7759217 | 3.73039 | -60.90511 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96f1f8d-6f01-35c1-9f1d-aa0c0f1e82a0 | 3.72243 | -60.92192 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7758eabc-5069-3c10-bb45-b27bb8bd50be | 3.93691 | -60.24667 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf262596-9734-3e8b-a578-144157cb7b26 | 4.54476 | -60.71363 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6ec207a-e968-3c8c-9bbc-860a14c6db26 | 4.20271 | -60.52635 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fb600c9-5b6e-347a-95d0-e5036a0c202b | 3.72122 | -60.91433 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02fa417b-f026-3186-a062-94a2bd92126d | 4.00498 | -60.37621 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bb1aad6-7e57-3658-aac3-bfe8ff15d2ab | 3.41722 | -60.3487 | 2026-02-15 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bbb7300-86e4-3ab8-9d4a-f4e5c1f0a30d | 3.72753 | -60.90944 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91be879f-479a-3fbf-b6ff-6a303b6cb764 | 4.24286 | -60.79952 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2bfb047-3187-38da-a189-ab55ea44b08d | 4.54416 | -60.7099 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25a5813d-1327-3167-9155-d28604b05813 | 3.45102 | -60.26982 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85b57048-1b45-30c2-b040-d093f77f9683 | 3.71613 | -60.92682 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21302b34-d17e-3004-9710-bd3ca5890435 | 3.72468 | -60.91378 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8040fac-351c-31ff-91be-b83a8e0dde66 | 3.80705 | -60.88252 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f5eb3fb-186d-3a51-8014-205c3e13f625 | 3.80359 | -60.88308 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5da2601-24dc-3985-bc4b-c595b943629d | 4.5407 | -60.7104 | 2026-02-15 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85ff5041-db22-3a58-a207-72596d837245 | 3.72183 | -60.91812 | 2026-02-15 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 517296c8-47cf-3ee0-b5f1-3c0a6901ffdf | 3.94175 | -60.25415 | 2026-02-15 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b28f81cd-48b2-3ee2-86c2-2a17f4c729e5 | 0.90319 | -60.43683 | 2026-02-15 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 182c5c90-6ad1-3630-b3f2-83cf2139468d | 1.91684 | -60.57079 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71f0e703-635a-329d-9019-dab9f587dcbd | 2.71467 | -60.1931 | 2026-02-15 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c101357-eb61-3399-8dab-3e3341622032 | 1.86852 | -60.83718 | 2026-02-15 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 31084560-ad68-3cfb-b39b-c03749cf0f76 | 1.91749 | -60.57486 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8478736-b85c-3ce7-9af4-c17d6f3f7f24 | 1.91456 | -60.57949 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e723685-f0e2-3569-8c8f-acdad7cffb80 | 3.40855 | -60.65504 | 2026-02-15 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37b925e9-be3d-3289-b1fd-04c788b629a3 | 3.40918 | -60.65894 | 2026-02-15 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20750ad8-64e2-363f-83c6-5f01d90f577b | 1.66769 | -60.5323 | 2026-02-15 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd648c2b-1ec0-3cef-843b-8b72a4d5390b | 3.41268 | -60.65838 | 2026-02-15 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5135a2-3901-37e9-9897-6fb96e4d1b94 | 2.48877 | -60.4372 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ba490b2-930e-3c1e-9e79-0438b966e4f8 | 1.91098 | -60.58005 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c814084-2a50-3025-b59c-c192552a90d0 | 1.91391 | -60.57542 | 2026-02-15 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd2b7b8e-ebf0-32b8-905f-cd48cf48a6a4 | 1.8683 | -60.8383 | 2026-02-15 05:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6bf388f8-9957-3620-95b4-fbe9bfb1178c | -10.59365 | -44.33062 | 2026-02-15 06:14:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 99f5c6a5-cdb8-3e4c-9d8b-99518045d67a | 3.7119 | -60.9246 | 2026-02-15 07:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c9f02977-1a75-3f63-b0e5-42390a5ed021 | 3.71918 | -60.90799 | 2026-02-15 07:50:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d11b437d-3266-3542-b4ed-92b2889c403d | 3.7119 | -60.9246 | 2026-02-15 08:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| eae99a5d-eb52-3f37-a368-b0ea56f1b259 | 3.7119 | -60.9246 | 2026-02-15 08:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9e5baa32-6313-3b58-87cf-691860d4249f | 3.7119 | -60.9246 | 2026-02-15 08:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| f0c97f70-63d8-30fd-94c5-21e41a1e1ea3 | -16.27419 | -40.51254 | 2026-02-15 11:34:00 | TERRA_M-M | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


