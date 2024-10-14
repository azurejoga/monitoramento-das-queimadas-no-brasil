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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df60e0d0-9da8-3a7d-a3fb-dbb147197670 | -12.3997 | -53.1147 | 2024-10-14 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| caa25807-8c9b-335e-a6f7-4c540e17562c | -12.4981 | -63.0148 | 2024-10-14 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1af6758a-2ad9-3c14-ad67-b9c82c675dbd | -12.4983 | -62.9956 | 2024-10-14 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 16f16e61-a5de-3a65-aa91-cecdb45bbce0 | -17.0823 | -56.0076 | 2024-10-14 01:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| e9f12e48-b0ca-3b6f-a664-bc8911a7cc52 | -17.6471 | -56.3084 | 2024-10-14 01:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| fce06080-d69d-3d29-accf-127f27ea4703 | -18.1905 | -56.8394 | 2024-10-14 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| c40e11a2-089f-30bf-8853-69d4bd1a5c94 | -2.4344 | -46.9195 | 2024-10-14 01:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 50b6a2c4-2488-3706-a07c-aa3093c21b0a | -2.4529 | -46.919 | 2024-10-14 01:55:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1955c489-720c-3cd2-aea4-bd70f8e5eff7 | -2.6117 | -49.1198 | 2024-10-14 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a2191f45-5929-3c66-9563-8d2a94fbb5c0 | -2.6118 | -49.0985 | 2024-10-14 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 4f9f0973-6ec9-388f-a781-9c66e9c412d6 | -2.6303 | -49.098 | 2024-10-14 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9eb109f7-517b-383b-a6a4-7218b4e4c435 | -2.6303 | -49.0767 | 2024-10-14 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8f626d4e-a1a9-3a46-947d-3ad9f0fc67a3 | -3.289 | -42.8327 | 2024-10-14 01:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| c2c3cf3a-2d55-3a60-9a46-44e3fe5844ef | -3.3076 | -42.8553 | 2024-10-14 01:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| a280e0e1-b242-3e25-8316-31144f678caf | -3.3077 | -42.8318 | 2024-10-14 01:55:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| c0af9d53-2d4a-33c8-b2fc-7f1ddad123de | -4.3718 | -37.9175 | 2024-10-14 01:55:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 69.9 |
| f3fb779d-a1fb-3ee4-b536-57c601069aa7 | -4.372 | -37.8918 | 2024-10-14 01:55:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 0245b955-04e6-3585-bf47-350351f0db09 | -4.3428 | -50.5172 | 2024-10-14 01:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5d6540c3-8ec3-3d5e-bbd2-0bc385877704 | -6.2141 | -48.329 | 2024-10-14 01:55:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 28.1 |
| fa1559e2-7f45-321b-8131-db9d2fb9bc1f | -6.3933 | -59.9929 | 2024-10-14 01:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| c2e5e456-6170-3a99-a6ec-7c3f67321faf | -7.6917 | -43.1854 | 2024-10-14 01:55:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 2be8863e-bf38-36bb-8941-fc98919a9796 | -7.9625 | -49.0607 | 2024-10-14 01:55:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 5562a4b4-5164-3d7a-bd35-d90ea092fc21 | -7.9418 | -63.6365 | 2024-10-14 01:55:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c11eb568-821e-3aa1-b0f6-4680a1e6203f | -7.9419 | -63.6177 | 2024-10-14 01:55:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fabb1463-c8ac-3d3b-961a-63d20f602b4f | -7.9603 | -63.6359 | 2024-10-14 01:55:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ce33ca48-3013-3352-9ad5-e7e21ba21a55 | -7.9604 | -63.6171 | 2024-10-14 01:55:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 38c6edfb-fdf8-3bb3-8b2e-50cf32c75f54 | -9.1021 | -47.9355 | 2024-10-14 01:55:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2a4cc09d-7654-38a7-b866-e2bd43970c7c | -9.1042 | -61.1811 | 2024-10-14 01:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0af13bb2-96c8-39fe-8981-3b7ad3dbf3d5 | -9.1043 | -61.162 | 2024-10-14 01:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 3291c188-3214-3792-8a85-c25ab68da5c5 | -10.0622 | -44.2391 | 2024-10-14 01:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 618d3c1b-3830-3c7b-9cce-86365c58710c | -10.0626 | -44.2158 | 2024-10-14 01:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2975896d-12ea-3349-8df5-cf674b30cc74 | -10.0813 | -44.2366 | 2024-10-14 01:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 44cc9c26-f6a4-3203-9131-bda091938de9 | -10.0816 | -44.2133 | 2024-10-14 01:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 76c7b54b-5a5d-3efd-a8a1-d53a107a34da | -10.0163 | -47.3308 | 2024-10-14 01:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 73fa2669-ce30-31f2-984f-f67b038d14ec | -10.0166 | -47.3085 | 2024-10-14 01:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a8fecf33-64f3-35cd-bcd6-824ae18a3949 | -10.0352 | -47.3286 | 2024-10-14 01:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f86307f9-0287-3601-9a1d-2328e4634421 | -10.4504 | -44.9516 | 2024-10-14 01:56:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 5825a255-6ba2-3752-b3f9-e0aff9846d3d | -10.4508 | -44.9285 | 2024-10-14 01:56:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 78fa644b-f553-32b0-97e7-ef74adc4bbcb | -10.4918 | -42.433 | 2024-10-14 01:56:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| f3cdc6cd-10d2-317f-bf04-903becd5a476 | -10.5118 | -49.7863 | 2024-10-14 01:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b7d1f4d8-f8ce-3366-90bb-0edeb6c78847 | -10.5307 | -49.7843 | 2024-10-14 01:56:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4db63645-47be-3c7a-af5b-ef42c6ce0708 | -11.17 | -39.9192 | 2024-10-14 01:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| eb9674dc-4d94-3120-8ce5-9ae3a425c258 | -11.1705 | -39.894 | 2024-10-14 01:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 97cdfd8a-acc1-3e92-8cc4-520c61013dc5 | -11.1893 | -39.9159 | 2024-10-14 01:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| ad0a215b-f58f-32a6-a0d5-570cf4777c2c | -11.1898 | -39.8906 | 2024-10-14 01:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 6a3c6efe-3a83-34d5-aa3e-9eea4f40c329 | -12.3804 | -53.1376 | 2024-10-14 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 29ce8fb2-f4ae-3533-a553-feb9337e1e59 | -12.3807 | -53.1167 | 2024-10-14 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 4abcaecc-28a5-3006-b7ad-a60169f47e09 | -12.3994 | -53.1355 | 2024-10-14 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 356d6a79-c627-3133-b3eb-c3c0cc84f938 | -12.3997 | -53.1147 | 2024-10-14 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 4b6ccb67-701f-3b10-8f7b-0a0bd01c19cd | -12.4188 | -53.1127 | 2024-10-14 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e9f8f83b-44aa-3ac0-befe-15c8f7a376b5 | -12.4981 | -63.0148 | 2024-10-14 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e33b9922-3079-37f8-9e0c-9b0c0994d4cb | -12.4983 | -62.9956 | 2024-10-14 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8152af00-1c42-3f7a-b02e-ef66590c92be | -12.517 | -63.0137 | 2024-10-14 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2d5144e9-2eeb-3058-9c1a-914247677da1 | -13.1273 | -51.6861 | 2024-10-14 01:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a81bde2b-1175-347f-ae27-b9d67f57c7fe | -17.0823 | -56.0076 | 2024-10-14 01:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| aabed58e-b18b-304c-8db0-33489fc28692 | -17.6471 | -56.3084 | 2024-10-14 01:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| b5955608-42ee-3c99-b1f8-418258f52f12 | -18.1905 | -56.8394 | 2024-10-14 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| ebe49944-2db5-39d1-b556-88f19c338069 | -18.2562 | -56.478 | 2024-10-14 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.0 |
| bca24355-ef01-30c3-ad8e-25f90f141c9c | -18.2555 | -56.5196 | 2024-10-14 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 9a92b0f0-2ecd-3277-bec5-e4ac4cd8f3b5 | -18.2559 | -56.4988 | 2024-10-14 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.6 |
| d66b1c5d-b063-3fd4-aed8-8333218f77cd | -18.2757 | -56.4962 | 2024-10-14 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.2 |
| ef040120-1bbc-3b59-8565-08f2ea2e6efc | -18.2761 | -56.4753 | 2024-10-14 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 7eb2a17f-568f-3f31-bc09-a0481d0d298a | -22.3685 | -48.6973 | 2024-10-14 01:57:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 05f9379f-ce7d-39d9-aa4d-7907eb4815a2 | -17.93 | -57.3 | 2024-10-14 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0a925506-c913-36e0-84ff-1cc5d071ba06 | -17.9 | -57.28 | 2024-10-14 02:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 23724afc-f438-391a-ba4c-8c322e5bcbce | -10.05 | -44.22 | 2024-10-14 02:04:27 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e6fe5e5-88f4-3db7-98ca-84a65e4e4db4 | -2.4344 | -46.9195 | 2024-10-14 02:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9a28d2fc-7e05-3dec-85e4-0937de495e22 | -2.4529 | -46.919 | 2024-10-14 02:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| aa3bb9da-b7f6-3fb0-a8f3-71cd8ac66d6f | -2.6117 | -49.1198 | 2024-10-14 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9a27d3ec-e97d-3157-aebc-77fa25832a98 | -2.6118 | -49.0985 | 2024-10-14 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 2199665a-5550-3c0c-8dfb-f60b40fae70d | -2.6119 | -49.0772 | 2024-10-14 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| bb448f16-a2d6-3df1-be4c-95e1a10d6e67 | -3.2889 | -42.8561 | 2024-10-14 02:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 1bf04c52-8d6d-3ff4-b1b7-7a29ccf9f9f1 | -3.289 | -42.8327 | 2024-10-14 02:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c98cfcfd-4fb5-38c1-b849-c559035571ee | -3.3076 | -42.8553 | 2024-10-14 02:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 029b51e5-4e8e-3044-ba01-2af75598a887 | -3.3077 | -42.8318 | 2024-10-14 02:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 65d2b86e-ab3c-318d-ba03-f101f4da4a5c | -4.3718 | -37.9175 | 2024-10-14 02:05:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 68.7 |
| d3e903d1-a813-37b2-bea3-99d695670c68 | -4.372 | -37.8918 | 2024-10-14 02:05:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 792d1f61-b113-3521-af3c-cabf4823ec08 | -6.2141 | -48.329 | 2024-10-14 02:05:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5fbc97e4-58ea-3513-9dc5-382ccf7e433b | -6.3933 | -59.9929 | 2024-10-14 02:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 52d76266-d120-3893-8294-0327ed28f36b | -7.9625 | -49.0607 | 2024-10-14 02:05:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 19c581af-3022-3669-8525-f5abc58032e6 | -7.9418 | -63.6365 | 2024-10-14 02:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1615267f-9e77-3b5d-aa5f-83dde9665698 | -7.9419 | -63.6177 | 2024-10-14 02:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 62de3a51-5e40-3a08-8138-c613bbc41206 | -7.9603 | -63.6359 | 2024-10-14 02:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| eeb1e428-9557-33aa-97f8-49d52a31b0cb | -9.1043 | -61.162 | 2024-10-14 02:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| bd83ca39-d5d8-36aa-89ea-46cff17b9e6e | -9.4699 | -45.8249 | 2024-10-14 02:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 212.9 |
| c7856508-d5bc-3f98-abf2-ac40452d539c | -9.4702 | -45.8023 | 2024-10-14 02:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| cd6d416a-6ee4-3544-9086-6744b95ede08 | -9.4888 | -45.8228 | 2024-10-14 02:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 0655db78-4861-3030-ada7-c2ef78da6e53 | -10.0619 | -44.2624 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 88dcfd58-ccf2-3469-acc2-d21ff0d7cead | -10.0622 | -44.2391 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 5ccd66ad-8c5f-380c-ac00-56deb7b5456e | -10.0626 | -44.2158 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| af2af266-9baf-3bbb-ae7a-d2a12b0ee988 | -10.0809 | -44.2599 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 57e5f90b-cc3d-3e77-95be-5a775cf78681 | -10.0813 | -44.2366 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 982a90f1-57e3-3765-ab92-4b626578cc7e | -10.0816 | -44.2133 | 2024-10-14 02:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 636912b2-ece2-3467-86ab-1bf86fa32871 | -10.0163 | -47.3308 | 2024-10-14 02:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| a1889300-1a6e-3d4f-9da0-af1189002ed4 | -10.0352 | -47.3286 | 2024-10-14 02:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 366c9648-1e94-3eed-9318-1aa3fa3b9d49 | -10.0166 | -47.3085 | 2024-10-14 02:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4b0cd4e0-5208-3a92-b583-a5ec43079dce | -10.4313 | -44.9541 | 2024-10-14 02:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 567d2875-f0be-382d-849f-2fe9bfd91fa7 | -10.4504 | -44.9516 | 2024-10-14 02:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 55c5f49b-0675-381a-9221-7be1ea385d19 | -10.5307 | -49.7843 | 2024-10-14 02:06:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f27e2a54-a6d1-34ff-bd1d-712b2e9ccd62 | -11.1705 | -39.894 | 2024-10-14 02:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 60.8 |


[Clique aqui para ver as próximas entradas](README26.md)
