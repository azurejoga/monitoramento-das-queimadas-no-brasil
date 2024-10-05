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
| fa4386ed-8509-345f-bdf8-a2efd96d5a8f | -16.97 | -56.82 | 2024-10-05 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4612bde-1809-3731-87cd-be546d8dd2b3 | -16.96 | -56.74 | 2024-10-05 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b73c3b7-cf5c-33a9-bd2c-0467ca37c7ab | -17.0 | -56.76 | 2024-10-05 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6bda994a-3831-3826-98bc-395895abab25 | -17.03 | -56.71 | 2024-10-05 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf06bb6a-f962-3b29-9ca9-9b5c4aab0260 | -12.62 | -53.18 | 2024-10-05 00:04:13 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c030f0b-5bf7-31de-a604-0c7550253bbd | -12.62 | -53.12 | 2024-10-05 00:04:13 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87373c8d-a08d-31c3-8840-96e038aa138a | -12.65 | -53.13 | 2024-10-05 00:04:13 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8306a60a-e332-3bfd-88b3-140715f2f1e5 | -7.72 | -49.22 | 2024-10-05 00:04:42 | MSG-03 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 561a9d93-911c-3212-8dbc-c00d7a94fc7d | -7.75 | -49.28 | 2024-10-05 00:04:42 | MSG-03 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04254d72-e91a-3c9b-aa3f-78814381d782 | -7.75 | -49.22 | 2024-10-05 00:04:42 | MSG-03 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cc87bfc5-ae83-300c-af96-69410fc6ef93 | -4.08 | -47.95 | 2024-10-05 00:05:03 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202b1b04-0666-392a-99e5-55c3f7ebd875 | -3.61 | -47.5 | 2024-10-05 00:05:08 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7b8024-645c-3cac-ac7a-839aa7e9a5ad | -1.1942 | -46.5935 | 2024-10-05 00:05:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| c8852f9c-f1c9-38f1-8072-b4c86590c442 | -1.1942 | -46.5714 | 2024-10-05 00:05:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 584f1921-5d59-3d97-bad6-9881b5e46cc3 | -1.2127 | -46.5932 | 2024-10-05 00:05:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6d49e320-2117-3e13-a400-5653faeab774 | -1.2663 | -47.6643 | 2024-10-05 00:05:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5181bef6-a008-3fd6-93e9-2b3e9af124dc | -2.5749 | -49.0782 | 2024-10-05 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| cea4ac76-965e-3ab1-9ece-05a42e0e258f | -2.78 | -48.5806 | 2024-10-05 00:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ba10ecc2-b22e-3293-96f9-2f3e82cabe12 | -2.8829 | -50.7147 | 2024-10-05 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 519fe20d-9548-3b2c-b0b0-700a2e1353de | -2.9014 | -50.7142 | 2024-10-05 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| b831b871-a228-321b-8e53-2bdfe7e321a0 | -2.9015 | -50.6933 | 2024-10-05 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f4788fde-bc32-3dd6-b512-e921821590ca | -3.1432 | -50.2254 | 2024-10-05 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 8cf1bcfc-202a-3336-ba58-a7381675ec03 | -3.2349 | -50.3695 | 2024-10-05 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ef90ddfe-ec3f-33bd-bd19-410e39595e0d | -3.239 | -49.3986 | 2024-10-05 00:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| b3542526-1271-3cab-90db-be2ea18d8cdc | -3.2534 | -50.3689 | 2024-10-05 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 81ced10f-d762-3485-b75c-2500ddd0c8e5 | -3.2574 | -49.4193 | 2024-10-05 00:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| e4d2827a-62f3-3fdf-8316-1dfe8c3eece1 | -3.2575 | -49.398 | 2024-10-05 00:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| cd217488-2270-3c49-b0be-d8ddaa3aaf98 | -3.2899 | -50.4725 | 2024-10-05 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 9bf48ce5-7e7c-3102-ab13-9eb12ad792dd | -3.2899 | -50.4516 | 2024-10-05 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4b85e115-0658-3e56-9680-c9afe1f94761 | -3.3083 | -50.4719 | 2024-10-05 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 296ff401-a25f-370b-b49d-4cec8db8faa1 | -3.3084 | -50.451 | 2024-10-05 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| e01fca6e-5a5a-3322-91ea-92b675c79ca7 | -3.5994 | -47.5359 | 2024-10-05 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| c90bf7f0-1897-3195-ba65-66bc3ef4689b | -3.5995 | -47.5142 | 2024-10-05 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2101aea8-f5cc-344e-b2bb-8abc29bbe065 | -3.618 | -47.5352 | 2024-10-05 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| d0a16fd3-d0de-3ef8-bc5e-181a518646b3 | -3.6181 | -47.5134 | 2024-10-05 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 406250e6-109f-30e2-8de9-837157de3dbb | -4.0608 | -47.9511 | 2024-10-05 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 248c97b2-7be0-3801-88bb-26bdc4fb3f8e | -4.0793 | -47.9719 | 2024-10-05 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 451f79ed-c789-3938-bd2e-d9ff699d2a98 | -4.0794 | -47.9502 | 2024-10-05 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 238.8 |
| 6b9291e0-25ff-358f-a370-916d2df12e94 | -4.0795 | -47.9285 | 2024-10-05 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 03bcedc6-0a2b-372d-8c1d-1ab1f74d9f75 | -4.0979 | -47.9494 | 2024-10-05 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 4bf0bb5f-b149-3660-a3d8-4126e8c46020 | -4.6633 | -49.5322 | 2024-10-05 00:05:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 14500a28-9438-3586-8a46-16298fa7c684 | -4.7851 | -50.8117 | 2024-10-05 00:05:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| cfcfa4df-74c6-31e0-afd7-0ce8aed0d624 | -4.8036 | -50.8108 | 2024-10-05 00:05:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d51570b9-acb5-3b72-abf7-3b2fb9639856 | -5.3911 | -46.4322 | 2024-10-05 00:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4cca8433-a272-3619-9f4a-2f8b38932fb7 | -5.8214 | -44.1426 | 2024-10-05 00:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 97472342-8392-33ce-a1c2-d383ef524897 | -5.8216 | -44.1196 | 2024-10-05 00:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| a0495bf3-2603-3a3f-a7b1-116b6bc2f4fc | -5.8403 | -44.1181 | 2024-10-05 00:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 97eb5f9f-33fa-321d-88e5-c82b0521136c | -6.9514 | -59.0666 | 2024-10-05 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ddf97b54-26ed-3e1b-9fd6-43ecff9a202d | -7.0233 | -59.3918 | 2024-10-05 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b4f6634d-f562-3e76-ba47-1c8982701b37 | -7.1346 | -59.3099 | 2024-10-05 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b62480cb-c93c-34f4-8a8c-c5df99dc74bc | -7.1347 | -59.2906 | 2024-10-05 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6225ecd3-a27f-3682-82b0-c023b65779c4 | -7.8979 | -61.4631 | 2024-10-05 00:05:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 81cb59bb-d687-3516-bea4-641bfab9ad7a | -8.2323 | -61.2205 | 2024-10-05 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 9cc16645-c626-3ae0-b5fb-77ac904ff672 | -8.7769 | -49.9763 | 2024-10-05 00:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 78d24ddf-a25e-3ff9-ad0c-bb07f14867be | -8.7772 | -49.955 | 2024-10-05 00:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 615a27f0-f372-3406-853a-d471252037a8 | -8.7957 | -49.9747 | 2024-10-05 00:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| aa0952eb-bb78-330e-87f7-8a3de3d2b7ca | -8.7959 | -49.9533 | 2024-10-05 00:05:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 7a22b8e2-cbf3-3056-b986-127a816d4684 | -8.9665 | -49.81 | 2024-10-05 00:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 59447fc8-e152-3771-9ae2-cfba0c569805 | -8.9853 | -49.8083 | 2024-10-05 00:05:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d2c47a1a-e74b-3e22-b378-21fb51287914 | -9.5686 | -64.2171 | 2024-10-05 00:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| f6412d3b-1924-3105-b658-ef5a448edca7 | -9.8802 | -59.5008 | 2024-10-05 00:06:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a9a514d6-6653-374b-8b46-94d7724b7b93 | -10.3933 | -54.8034 | 2024-10-05 00:06:05 | GOES-16 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 741a0611-4538-36ba-865a-812a2defe72a | -10.4418 | -50.7761 | 2024-10-05 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 92a947f3-7c89-3eb7-bdc1-bd2989fd72aa | -10.4421 | -50.7548 | 2024-10-05 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| e2a38d61-e831-36b5-81d6-71401f59e447 | -10.4424 | -50.7336 | 2024-10-05 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7f6b802a-4840-33e8-b602-ef2747a9f9b1 | -10.4427 | -50.7123 | 2024-10-05 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 7d7426cb-72b1-3b6a-bdda-8f8d3193bd07 | -10.5757 | -64.0248 | 2024-10-05 00:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 8e0d3843-048f-36e1-9328-d687856f44b7 | -10.5943 | -64.024 | 2024-10-05 00:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 06de78c2-94b3-34dd-8fd6-1d3831101dc2 | -11.0712 | -54.7868 | 2024-10-05 00:06:09 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 30eb6d2f-2858-3fa4-a123-cfbc886625e1 | -11.0966 | -54.2336 | 2024-10-05 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 66ebf4a8-85eb-3eab-a848-19808288b62b | -11.0969 | -54.2131 | 2024-10-05 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2f9650b4-84e5-3d27-984f-aecacd3d4164 | -11.1155 | -54.2319 | 2024-10-05 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 23c5c8b0-3a78-3973-98e2-38f65af4be86 | -11.1158 | -54.2114 | 2024-10-05 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 809aa498-eb54-37aa-969d-7bd644b08306 | -11.7187 | -47.8107 | 2024-10-05 00:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 385f5794-b5c5-379f-9316-961e9fa7188f | -11.719 | -47.7884 | 2024-10-05 00:06:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 3dd12cba-2ac1-379a-99e3-3a39b23f3124 | -12.2668 | -45.958 | 2024-10-05 00:06:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 64e29d21-bba4-37a0-9868-c0ac8fb33b42 | -12.7623 | -50.5782 | 2024-10-05 00:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 7f7e1d15-c023-3164-9c71-6068f2884bb7 | -12.7627 | -50.5567 | 2024-10-05 00:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| b17b805a-c628-3b60-b4b1-955e082ddede | -13.1358 | -51.1527 | 2024-10-05 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 9129cf44-e346-33d7-8ab3-c944b72b0c22 | -13.1543 | -51.1931 | 2024-10-05 00:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| af2b22c0-5b55-3303-8a9c-cd52aeaa2718 | -15.5594 | -57.4756 | 2024-10-05 00:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4f0baa37-94a7-339a-92fa-3f47b08a550d | -15.5597 | -57.4553 | 2024-10-05 00:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 40d3e51c-eb40-397d-96f8-d8612a2ab997 | -15.5791 | -57.4532 | 2024-10-05 00:06:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 29eeded2-4632-3a25-ada4-15a65a00d787 | -15.7149 | -57.4388 | 2024-10-05 00:06:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6dbcde28-57db-3aea-9e66-e69720b01538 | -15.7151 | -57.4184 | 2024-10-05 00:06:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 45e5ee26-0225-38af-b6ad-774b3a57d4f6 | -15.7343 | -57.4367 | 2024-10-05 00:06:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 1c02701f-b130-370d-a611-4ef9c03ca95e | -15.7346 | -57.4164 | 2024-10-05 00:06:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 124ad00e-5206-3dfd-a281-1fb5536bc242 | -16.5345 | -57.2259 | 2024-10-05 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| af22bf96-a6e2-32b0-ba7c-a42605170812 | -16.554 | -57.2237 | 2024-10-05 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 240.3 |
| cb16c2fa-de28-3118-8504-83c4378e55bc | -16.5544 | -57.2032 | 2024-10-05 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.0 |
| b62768eb-674a-3c5b-9ecf-213269a018c9 | -16.5736 | -57.2215 | 2024-10-05 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 3e331504-ed5d-377c-8729-d94e4464ec89 | -16.5742 | -57.1805 | 2024-10-05 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.1 |
| 7f39e8e9-1822-333f-a9b9-b21374bfddc6 | -16.5745 | -57.16 | 2024-10-05 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.6 |
| e26922ab-5818-31c8-9f0b-99ddc533f18e | -16.5938 | -57.1783 | 2024-10-05 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| d3349c27-8681-3128-abc8-f610d2451900 | -16.6871 | -57.4536 | 2024-10-05 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 730d52a8-e2d6-380b-a347-736ac7ec4642 | -16.7647 | -57.4856 | 2024-10-05 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.6 |
| a230f531-7f9d-35aa-9dce-989af3abf9bc | -16.765 | -57.4652 | 2024-10-05 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| e8e85e37-c3da-35dd-bfb8-1d3ca710f4b5 | -16.7843 | -57.4834 | 2024-10-05 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 0f4edca3-46b9-323e-aa98-46adccc075ad | -17.4587 | -40.0547 | 2024-10-05 00:06:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 3eec61fe-47c1-3c4d-9635-40a11404358a | -17.0695 | -56.7733 | 2024-10-05 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |


[Clique aqui para ver as próximas entradas](README2.md)
