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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f9142b-f88e-3cbe-854d-29452eebfe59 | -6.9514 | -59.0666 | 2024-10-06 13:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d464999d-47de-3a29-ac8d-b1268ecdcd6e | -8.1478 | -44.4171 | 2024-10-06 13:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b1532589-9503-3d0f-b520-dfc514d461b3 | -7.964 | -54.7562 | 2024-10-06 13:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7170e7d7-4da7-3c0a-a9ea-37a3b8ee9346 | -7.9826 | -54.7551 | 2024-10-06 13:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 28bf6cde-164d-361c-a7bc-b24ed7bd343e | -10.0463 | -45.2785 | 2024-10-06 13:06:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 2ddf07ce-5406-3585-9757-8e6d86983f3e | -10.2711 | -45.4787 | 2024-10-06 13:06:04 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 890052e0-5da8-38b1-a00d-8faf1a381c6d | -10.443 | -50.691 | 2024-10-06 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 57cb0709-39df-3a39-8d01-378d275cce2b | -10.4049 | -50.7161 | 2024-10-06 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 71323ca4-04e6-3af5-beb6-55528e23d316 | -10.4235 | -50.7355 | 2024-10-06 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 2dad24d4-0f77-3311-9da9-46cde17c18fd | -10.4241 | -50.6929 | 2024-10-06 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 173.6 |
| a7612a84-42ce-3245-908b-3823cef452c3 | -10.4238 | -50.7142 | 2024-10-06 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 391.8 |
| bf3630b2-8602-387e-8e7c-cab5254bb0fd | -11.297 | -46.7724 | 2024-10-06 13:06:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ff82c294-ea60-3553-b8fc-8ab7a5cb1279 | -11.4238 | -47.1815 | 2024-10-06 13:06:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ee93c14b-c4b0-3680-946a-f04d39b23bb1 | -11.7378 | -47.8082 | 2024-10-06 13:06:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 3aa041e3-8406-3de8-a083-8fc620a7286f | -11.7187 | -47.8107 | 2024-10-06 13:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5666e076-9568-3ee1-9da0-3e7f95bafc46 | -12.5093 | -45.3017 | 2024-10-06 13:06:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 21d59201-f50f-3fe9-b053-7d8ec541177e | -12.42 | -47.0453 | 2024-10-06 13:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 5d45a24e-09b1-37f4-92e3-5f6516ad8d89 | -13.8943 | -44.6058 | 2024-10-06 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 9d71c776-9853-339b-9778-ca816afbbd3b | -13.8749 | -44.6093 | 2024-10-06 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 4e819778-c5cd-3c65-8a63-281169adc321 | -15.1435 | -48.0594 | 2024-10-06 13:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 875e4708-d061-3edb-9caa-09fa4ce96a4b | -15.1635 | -48.0336 | 2024-10-06 13:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 239.1 |
| ef29cf00-a0fe-37e2-b4ae-c4cb82b0760e | -15.163 | -48.0561 | 2024-10-06 13:06:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ee5cd4e4-96ed-377b-8a08-bef00e4e09d0 | -16.5474 | -49.2058 | 2024-10-06 13:06:39 | GOES-16 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 41c94df2-e1f2-3ba2-a569-3a774c289e7c | -17.6545 | -44.4097 | 2024-10-06 13:06:44 | GOES-16 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d14ed499-b070-3df7-a196-6ef9e6e8e81c | -18.889 | -54.5373 | 2024-10-06 13:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3511163b-432e-354a-bc59-4e581b73808b | -6.9699 | -59.0658 | 2024-10-06 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| cf5fd39d-b15d-3c80-8344-44c0c5e53bc0 | -6.9514 | -59.0666 | 2024-10-06 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 99a00034-7fb3-351b-abfa-0a02eda7eced | -7.0233 | -59.3918 | 2024-10-06 13:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 581f25eb-84f4-3332-86bc-51e0d4989a52 | -7.6249 | -42.4838 | 2024-10-06 13:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| d1f54934-ac2f-3975-850d-1c0d9471365a | -7.6438 | -42.4818 | 2024-10-06 13:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| ee3d8797-0ffe-38df-9640-8e004a70757f | -7.7684 | -43.0833 | 2024-10-06 13:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 59f3fa09-963b-3444-a90c-963ab7ffdc17 | -8.1481 | -44.3941 | 2024-10-06 13:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| eb26dd43-b6bd-3772-b693-1feceeca6e87 | -8.118 | -43.7951 | 2024-10-06 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| f9ed0e19-e73f-337c-9478-a9f439a3025e | -8.1667 | -44.4152 | 2024-10-06 13:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2329127c-fc78-36ce-8ae4-a8826eed2a44 | -8.1478 | -44.4171 | 2024-10-06 13:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| cbda1f7a-f882-3334-850a-be755e0062d4 | -7.9826 | -54.7551 | 2024-10-06 13:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 956507d4-688d-34e8-9193-fb2a916e967d | -7.964 | -54.7562 | 2024-10-06 13:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 65169470-3756-33a9-8dc4-3290956c6bc0 | -8.1945 | -43.717 | 2024-10-06 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 8f40ccd5-3b79-3917-839f-901b9eab3e85 | -9.2566 | -43.5241 | 2024-10-06 13:15:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 12939897-fb75-310d-8b98-a4dcab7d6255 | -9.2376 | -43.5264 | 2024-10-06 13:15:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 206.5 |
| 15fc7879-5c02-3b65-9bdb-db9b43ffb57d | -9.238 | -43.5029 | 2024-10-06 13:15:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| e731f8ea-b367-3bc2-807f-653e67033d37 | -9.9355 | -47.6937 | 2024-10-06 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 154b0845-2e50-3afd-b731-c16a18f81f66 | -9.8552 | -60.2966 | 2024-10-06 13:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| ab527c12-d8ba-3712-a322-cfd45b0aa6f8 | -10.4049 | -50.7161 | 2024-10-06 13:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 97e48dfc-15a6-3dcc-9bd5-d0641413b1b8 | -10.4235 | -50.7355 | 2024-10-06 13:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 9ff4a332-1bfa-38af-a340-eac90b1ee86d | -10.4241 | -50.6929 | 2024-10-06 13:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 190.3 |
| ee349fc5-fac3-3a51-8c3d-b70e00d83783 | -11.0802 | -54.0302 | 2024-10-06 13:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 1d0f6504-0cf1-3467-acdf-17160c9119ce | -11.3658 | -47.2337 | 2024-10-06 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 239f036e-54a1-3cf1-a938-4200fd7d6929 | -11.297 | -46.7724 | 2024-10-06 13:16:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 0cbd488e-e02d-34e5-948c-99c4e6088ee5 | -11.3158 | -46.7924 | 2024-10-06 13:16:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| a8115a49-a694-3847-a404-cf0f2721edbe | -11.4238 | -47.1815 | 2024-10-06 13:16:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| b68c4cba-d8e8-3cc0-99d1-9f5657be1e48 | -11.7187 | -47.8107 | 2024-10-06 13:16:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 7a6a25cd-61ad-3b93-a2a7-99c2c5917133 | -11.7378 | -47.8082 | 2024-10-06 13:16:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| be821cac-469d-3a46-b65e-e8f25b5462c9 | -11.8727 | -50.1277 | 2024-10-06 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 9d52a8b1-b037-3831-a7fd-50f47cd304a3 | -12.42 | -47.0453 | 2024-10-06 13:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 442.1 |
| d129b97e-d746-34bb-8752-18a0d5fe76c9 | -12.5093 | -45.3017 | 2024-10-06 13:16:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7923c93f-d9b2-31f4-8df2-1587c269001a | -12.9848 | -47.6584 | 2024-10-06 13:16:19 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 668213f4-65a0-38f4-adcd-4880a65256f9 | -14.0883 | -45.5274 | 2024-10-06 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 6a97e0fa-387c-3576-b114-de6410692818 | -14.0767 | -45.1579 | 2024-10-06 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 57042362-ba1d-3739-834e-ffa0693c6c81 | -14.0879 | -45.5507 | 2024-10-06 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 428.1 |
| 41949ad9-33dc-3063-a13c-9a983f22de0e | -14.0874 | -45.5739 | 2024-10-06 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| c2e9ae42-50af-3e2a-a77c-3f781219af3c | -14.0689 | -45.5308 | 2024-10-06 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c69dcd6e-5171-3c24-b7c3-2bd927a48d8a | -15.1435 | -48.0594 | 2024-10-06 13:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9676479a-b776-3626-abab-40a816588d12 | -15.1635 | -48.0336 | 2024-10-06 13:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| ad12a9a1-ff5e-3468-b64a-8e3ade1f83f4 | -15.163 | -48.0561 | 2024-10-06 13:16:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0140f2e4-1aa6-3dd0-8106-db059603ab95 | -18.8886 | -54.5587 | 2024-10-06 13:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 34b5ac4d-950c-384a-8b6d-a6548b96b528 | -18.889 | -54.5373 | 2024-10-06 13:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0e33a379-164c-3986-969b-2876f6953f18 | -14.09 | -45.58 | 2024-10-06 14:04:03 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 831bd429-f7ab-3bec-8663-e735f7d05951 | -14.09 | -45.53 | 2024-10-06 14:04:03 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2ac5894-303e-385c-a59e-9b1466523a01 | -14.08 | -45.19 | 2024-10-06 14:04:03 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35706a78-e4df-3c64-8b6e-0f9741d39ba2 | -14.12 | -45.54 | 2024-10-06 14:04:03 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02d718fd-d3bf-3c3f-a753-96d62b331e65 | -12.78 | -50.57 | 2024-10-06 14:04:11 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8605cfce-a7f5-313d-9782-7a3843902b0e | -6.8419 | -41.7032 | 2024-10-06 14:05:45 | GOES-16 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 239.1 |
| 3784e006-7000-31f0-86a7-411c27a50139 | -6.8608 | -41.7013 | 2024-10-06 14:05:45 | GOES-16 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 684ceb0b-3a76-38e8-a53c-507a93e4ba7f | -6.8422 | -41.6791 | 2024-10-06 14:05:45 | GOES-16 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| a1302cf4-7425-352c-a07b-82e1e158470d | -7.0049 | -59.3925 | 2024-10-06 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| dd785806-941b-3b47-ad36-6a704a13cdb5 | -7.1328 | -42.6288 | 2024-10-06 14:05:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| c230c6f8-f3e2-370b-9ddd-4a8cf4936052 | -6.9515 | -59.0473 | 2024-10-06 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| d46c4925-6dcf-349a-83b1-5334c4720007 | -6.97 | -59.0465 | 2024-10-06 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f961578e-25d8-31e1-a9f1-e6e91fa43b91 | -6.9699 | -59.0658 | 2024-10-06 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| cf21e382-68de-3045-aed3-f7642a4b970d | -7.1331 | -42.6051 | 2024-10-06 14:05:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 453a9983-ae6c-3b2d-ac4f-e4985e266df8 | -6.9514 | -59.0666 | 2024-10-06 14:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| a495eae6-7716-3669-97d7-5d9045de8bc4 | -7.0233 | -59.3918 | 2024-10-06 14:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 53f6fe0a-b839-3f24-890b-694e6ce7cf4f | -7.0232 | -59.4111 | 2024-10-06 14:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| faafe8ff-f99e-339b-ab1e-12ef2468a2b4 | -7.6249 | -42.4838 | 2024-10-06 14:05:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 8b16c2bd-60b1-39ad-a1f1-da44cb064fa8 | -7.6438 | -42.4818 | 2024-10-06 14:05:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 3c33b18d-f316-305c-bbf0-deca16ef562f | -7.7687 | -43.0598 | 2024-10-06 14:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 1fda521e-c58c-3f12-9e68-0f39d2c6966b | -7.7684 | -43.0833 | 2024-10-06 14:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| ad5d5592-1408-3b8d-98ad-f318c2de2d4e | -8.1756 | -43.719 | 2024-10-06 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 3d0fe1a9-3662-3a25-a739-295087d859ce | -8.1478 | -44.4171 | 2024-10-06 14:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 46cc4551-1038-3f9e-b125-77a86a21695f | -8.1948 | -43.6936 | 2024-10-06 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 1391c90c-ab94-333d-abc8-2df523d3f04c | -7.964 | -54.7562 | 2024-10-06 14:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 68029db1-bdf6-33a7-a69d-362513c881a8 | -8.1945 | -43.717 | 2024-10-06 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 12f817fa-537c-32ae-8551-7f3b1559566e | -7.9639 | -54.7764 | 2024-10-06 14:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 2ff8aa82-9622-3d38-90d5-174246003542 | -8.1759 | -43.6957 | 2024-10-06 14:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 85ac05d8-488a-32a2-9647-3808d8a22050 | -8.1667 | -44.4152 | 2024-10-06 14:05:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 944c4314-9cef-3ffd-9c86-96d3f5f049f7 | -8.7984 | -45.173 | 2024-10-06 14:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 45864efd-4cc6-31dc-89e9-7a0b9fb46fe4 | -8.7795 | -45.175 | 2024-10-06 14:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8f896912-7c6e-3b16-bfd9-d5bbc5448a1c | -9.2376 | -43.5264 | 2024-10-06 14:05:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 91e1d189-de97-37a8-96a4-ca44ddc483c1 | -9.3278 | -46.5385 | 2024-10-06 14:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |


[Clique aqui para ver as próximas entradas](README162.md)
