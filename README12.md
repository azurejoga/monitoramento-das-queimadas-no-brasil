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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e8a3ec8-4e27-392d-b3f8-600764943152 | -6.9527 | -43.585 | 2025-08-19 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 09484d18-8ced-3028-82e0-6eaec23b0117 | -6.9715 | -43.5833 | 2025-08-19 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 444a3a41-6969-32a3-9106-501c2afbe6a1 | -6.9712 | -43.6066 | 2025-08-19 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c9567206-0f19-3869-8332-8a902fb861e2 | -5.7887 | -43.6134 | 2025-08-19 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3799093d-f74d-3e28-ad0c-4035b64953d1 | -14.9812 | -54.7951 | 2025-08-19 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f19947a1-5791-36fc-9bff-5854666afc53 | -14.9809 | -54.8158 | 2025-08-19 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| f617b299-f93b-3704-9fbd-82d597d41d1a | -6.9339 | -43.5868 | 2025-08-19 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 71f64bb3-36cf-3172-a1a0-bd01723bdea9 | -23.189 | -52.0174 | 2025-08-19 03:20:00 | GOES-19 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 75727662-ec4a-3ed2-9fce-93a5899b30e4 | -15.0389 | -54.8089 | 2025-08-19 03:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 35bf8292-dbaa-344c-83f5-d39a656395f4 | -6.9524 | -43.6083 | 2025-08-19 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b0d4a591-cae9-361d-acbf-9f080d6a9d77 | -15.0196 | -54.8112 | 2025-08-19 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 0513056c-2abc-3610-9464-d132c4b10c4d | -6.9712 | -43.6066 | 2025-08-19 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 067a4869-cd38-3644-90a4-45964e0c5ed1 | -6.9527 | -43.585 | 2025-08-19 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0e1fded6-110a-366d-bc4e-4bcaa70acc97 | -18.518 | -53.2054 | 2025-08-19 03:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 40b53b03-2d01-3ec7-a6a1-f5d4c29ecffc | -15.0389 | -54.8089 | 2025-08-19 03:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 81d24239-8f5e-383f-af0e-76680ffdad9c | -6.9339 | -43.5868 | 2025-08-19 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 53b050c3-2611-3aa3-b465-0f9f934e4944 | -6.9524 | -43.6083 | 2025-08-19 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 18fef18c-364f-372f-bb02-a36986ac7a6b | -14.9809 | -54.8158 | 2025-08-19 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| e6ba290f-edfb-35c4-9e61-ed73bf8f50ed | -6.9715 | -43.5833 | 2025-08-19 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 85ca3961-03b0-315d-878a-a84dd5bb3442 | -14.9812 | -54.7951 | 2025-08-19 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a44d3589-a4b6-3fbf-a8ac-0466f58dcc61 | -4.00095 | -43.26524 | 2025-08-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e07fe0d2-8278-3f41-8d40-ee4a81cf2d50 | -3.98633 | -42.51929 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6ea911a6-b860-30de-be0c-c13a63530ead | -3.82019 | -41.5695 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 028482c1-e060-3b3b-96e0-4a906609c255 | -3.98575 | -42.52279 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7566ff0b-a814-357a-b011-4836b2741b68 | -5.78372 | -43.89325 | 2025-08-19 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 242d84f1-90b8-3bdb-8065-83ae61ddfe77 | -3.97607 | -42.51399 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d06f8afb-ea65-3bf9-af88-285e469d2439 | -5.78443 | -43.88913 | 2025-08-19 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dbf3134-b4e4-3795-9ca0-d3d97327fcad | -4.1472 | -46.4591 | 2025-08-19 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b996cd0-3624-318d-a544-544cf00adb0a | -4.33698 | -38.64375 | 2025-08-19 03:34:00 | NOAA-20 | BARREIRA | CEARÁ | Brasil | 2301950 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0038f0c5-3208-3b8d-a4d2-566d70369616 | -4.60319 | -43.31017 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e727cdc2-4935-3ea9-b87c-3b94886b89f8 | -3.97549 | -42.51748 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca6db1fe-e058-3e58-a2d3-d0156383d24b | -3.98149 | -42.51489 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7bb31bbe-eaa1-3088-aa59-99007cc68215 | -3.81726 | -41.57291 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd926b35-9bee-3f02-a843-410d0286b440 | -4.91708 | -43.24168 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7af0953a-e873-3d2f-81b4-17d76ee13aa2 | -3.2531 | -43.27752 | 2025-08-19 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 947a2390-8382-3911-a545-c1db429d760a | -4.60251 | -43.31399 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ee29859-3715-327d-807f-f83a43cce069 | -4.91085 | -43.24439 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0627ee18-cb9c-3575-8d9b-53c69b2a6db7 | -3.81984 | -41.55792 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84451a3e-6997-3598-8534-905b0d7ea551 | -4.72251 | -37.84686 | 2025-08-19 03:34:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e393b608-996c-32a6-ae92-54bdf71bf2e0 | -5.66207 | -43.3772 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86906fc0-896a-33cd-832c-027f21a810ad | -5.65118 | -43.38388 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a289f2a5-16da-387c-9237-8b275c64d8df | -4.25574 | -40.28591 | 2025-08-19 03:34:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f6273fd-8bb5-352a-b3a9-5c7eeedf6094 | -4.60047 | -43.31079 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b00a603b-a74b-3e26-88da-686f14b94e70 | -3.98033 | -42.52187 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9f0270af-0661-39b9-9397-fe53017afca7 | -5.65449 | -43.38734 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de989b41-a743-3d28-b2a0-63b1309e60cf | -5.1661 | -36.56863 | 2025-08-19 03:34:00 | NOAA-20 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 860bbbc4-792d-306a-83c2-b3d50cbed5df | -4.72403 | -38.39931 | 2025-08-19 03:34:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2158f7dd-db85-326c-9bad-587d62ddbee5 | -3.24872 | -43.26842 | 2025-08-19 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79cd21e-8b9f-3e6f-bca2-2a888f124037 | -4.91579 | -43.2492 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2885801-81c0-3d3f-a00f-8011b51b9c1a | -3.6458 | -43.95948 | 2025-08-19 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cc61ed4-b819-3218-9d70-1f33053ef163 | -6.53652 | -38.81644 | 2025-08-19 03:34:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04af6bff-ed5f-3212-91da-8dffec063853 | -3.64216 | -43.95847 | 2025-08-19 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cb9bb93-c5a2-38f2-88cb-ad4f55a19e9c | -3.26405 | -39.39579 | 2025-08-19 03:34:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fd64d3d-3c63-30a5-b8be-2a4829f87010 | -5.78409 | -43.89405 | 2025-08-19 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c98d3ef-63cb-31c7-8826-597482af2ee6 | -5.78484 | -43.88993 | 2025-08-19 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d8bfdda-6493-3a6f-81d8-dab26bc8d193 | -3.98008 | -43.23878 | 2025-08-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae120ce9-8aad-35bb-9e78-c9959a69315e | -5.57079 | -44.08374 | 2025-08-19 03:34:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5738a692-90b7-3980-836d-b45f843061fb | -3.98792 | -42.52038 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a907bd3d-3779-37c4-964c-65936f5738a5 | -4.25876 | -40.28715 | 2025-08-19 03:34:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7f8173b2-07ef-37da-99e8-55e273a9ec86 | -4.14667 | -46.46085 | 2025-08-19 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cb18330-6d47-315f-b4c0-6b75a1c6c855 | -3.97064 | -42.5131 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 411bd475-a171-36d8-b401-709da7f01a7e | -3.98517 | -42.52629 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 53b5a7de-f3c2-31fa-b5b4-dd1ffd9deb47 | -4.91643 | -43.24546 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e46f0d4-f9e2-3153-98f0-974489b5ee3a | -3.8197 | -41.57253 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3af669c0-2d42-379b-90ff-5962e4a5c2c2 | -5.57662 | -44.08488 | 2025-08-19 03:34:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 68193822-9687-34cd-a540-2f302fcbf0ed | -5.42359 | -42.35614 | 2025-08-19 03:34:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 75640f83-5523-31ba-824f-cbe1b906ab05 | -5.65344 | -43.40416 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81f376c5-fcfd-30a7-bc62-26d0543fae68 | -3.98091 | -42.51838 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ed8bcc9c-bb8f-3b78-8ae0-64141a8bf6a1 | -3.99117 | -42.52372 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 31f33848-9a31-3b9e-81ed-ccdd42d05bab | -5.6129 | -43.47136 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ac2480-420e-316b-9bea-aea2574e52ed | -4.59052 | -43.31593 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8ec8fee-b6ab-3b6e-9baa-511c915f51c9 | -5.42884 | -42.35696 | 2025-08-19 03:34:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 653114bb-acf6-3006-8c3d-bfaf3a51218a | -5.65582 | -43.37997 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1d0be5c-b991-35ad-a875-4d01ca228a87 | -3.9816 | -43.24176 | 2025-08-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25cb4721-d8c0-3f8c-9e9f-4496a43d2c80 | -4.59351 | -43.31752 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3a508f9-36d0-3a12-bfc2-0ab422e0172e | -4.64929 | -43.12376 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22760e0d-8076-3f8d-bb39-52ba051a5be3 | -4.92138 | -43.25024 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0dfe65f-25a6-3518-b9ee-940859f8ebb9 | -3.81933 | -41.56089 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a797884-59bf-3788-9109-2ba5100554fb | -3.9825 | -42.51948 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e034a13f-4fab-305f-8199-86a1792709dc | -4.14823 | -46.45317 | 2025-08-19 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 128694c2-be8c-3c5c-8444-63e350b65c73 | -5.64987 | -43.39143 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4210dc5a-26b3-327a-ba68-1c9bcd53d620 | -6.55569 | -38.80096 | 2025-08-19 03:34:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4a4fb4eb-a0d4-355c-b143-508172b12fe6 | -3.98671 | -42.52737 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 984b39fb-5cb9-332a-9a1e-8479423d4859 | -3.64813 | -43.95955 | 2025-08-19 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5391a060-bf68-3305-a849-68d87b327bee | -3.97491 | -42.52096 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4c88214d-2435-332f-8715-366e1ee508f7 | -3.82035 | -41.55495 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7202e845-cc27-3d2f-b31f-f47d688bc8a2 | -6.55625 | -38.79757 | 2025-08-19 03:34:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 90d73e9e-9ca1-3e6f-b6c6-319a8fc9306e | -5.64721 | -43.40684 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a69eebcf-ca72-3ac3-9136-7dbf8acb5157 | -3.81707 | -41.55663 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e066bebc-9ee7-3ad6-9f95-d62b5d4a439a | -5.64921 | -43.39527 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e863a924-d5b9-391a-a118-adbff884a12f | -4.58983 | -43.31982 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd5fc99b-2f35-3a70-b397-fd2a9b526ea6 | -3.97708 | -42.51858 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 108fd94f-b8a4-317d-ac81-10d20020e12e | -5.78516 | -43.61633 | 2025-08-19 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| da288505-f79e-3ee5-b70e-c6b1761ac936 | -4.58852 | -43.31265 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b19e933-4ff5-3233-84d7-bfe0829adc22 | -3.81658 | -41.5596 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 015b0066-63ca-3164-9ae3-56b37a88789d | -4.26038 | -40.28667 | 2025-08-19 03:34:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3a1f6684-5349-3ea9-81e6-0d439f16c182 | -4.72462 | -38.39571 | 2025-08-19 03:34:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69c36604-caa2-3dcf-9499-a8e33663a9cc | -3.07336 | -40.3481 | 2025-08-19 03:34:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59ec4f74-1961-362e-b0ff-bf6184767773 | -4.64774 | -43.12269 | 2025-08-19 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fd3bee2-78c9-3dab-9c5e-21b06698a115 | -5.36842 | -42.33281 | 2025-08-19 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README13.md)
