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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95c3b514-652e-3659-8458-3d2c08a8fa05 | -12.7021 | -46.303 | 2025-10-29 12:20:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 4a6747c0-ca35-348e-890a-775bae2f4d50 | -21.3104 | -42.3266 | 2025-10-29 12:21:00 | TERRA_M-T | BARÃO DE MONTE ALTO | MINAS GERAIS | Brasil | 3105509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 04d3c6c0-c5ec-3ef3-8b02-621d33547f45 | -18.41121 | -47.41534 | 2025-10-29 12:21:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 66a7cdc0-cdc3-392d-b2f5-693693221d30 | -18.41264 | -47.40397 | 2025-10-29 12:21:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c37e19b2-69b8-3319-984d-14b599527158 | -18.99718 | -43.89441 | 2025-10-29 12:21:00 | TERRA_M-T | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 20353601-6878-34f2-a49e-a35270d51563 | -19.23773 | -44.95867 | 2025-10-29 12:21:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 21ce48a9-41df-3e8c-bd4d-0f9c1d32745b | -21.16717 | -41.43599 | 2025-10-29 12:21:00 | TERRA_M-T | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| b1a98a9c-841e-346d-8504-43f2789ecd1d | -19.78588 | -44.06168 | 2025-10-29 12:21:00 | TERRA_M-T | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| de5177d1-171c-3731-b79a-721d56cb1904 | -19.23005 | -44.9521 | 2025-10-29 12:21:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 609eea38-1780-3933-ae27-71f83a1298c8 | -20.63341 | -45.03026 | 2025-10-29 12:21:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.7 |
| 0525907c-b43a-38d3-9525-add3d28a3235 | -19.78959 | -44.51873 | 2025-10-29 12:21:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ee147fa5-a5cd-3472-a807-d434b41fcb5d | -19.3727 | -51.39933 | 2025-10-29 12:21:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 508c8c50-949c-3a03-bd41-b25c0aa848eb | -19.7867 | -44.06834 | 2025-10-29 12:21:00 | TERRA_M-T | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 9a7f63b6-57b6-3d22-94ae-ca44240cdc00 | -21.30972 | -42.32074 | 2025-10-29 12:21:00 | TERRA_M-T | BARÃO DE MONTE ALTO | MINAS GERAIS | Brasil | 3105509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 093aa93f-1fa2-32f6-b30a-f6b6d39ceefc | -20.63535 | -45.01237 | 2025-10-29 12:21:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 442b225d-0965-3aa8-8753-b148fa69ca42 | -13.2266 | -47.0614 | 2025-10-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 57e1a98b-2539-3d84-b99f-c1c14c004338 | -12.7021 | -46.303 | 2025-10-29 12:30:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9f75e299-8abd-339c-9ac8-5e05e5a52ee9 | -13.2073 | -47.0643 | 2025-10-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 937312f6-83f4-30a4-98c0-927e7dddc3c0 | -13.2078 | -47.0417 | 2025-10-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 37568e33-65f9-32c9-8627-667584789a2c | -4.5157 | -38.7741 | 2025-10-29 12:30:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 66509a89-e180-3549-9007-e9497115205b | -3.7261 | -41.579 | 2025-10-29 12:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| f62793e3-e607-365f-9af7-30bad689587c | -3.7403 | -42.3163 | 2025-10-29 12:40:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| d5e8476e-8f05-37cd-ad79-85ef78a0203e | -13.2266 | -47.0614 | 2025-10-29 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4e07cf7f-e336-3f68-a719-0f71511f8ce6 | -14.2842 | -47.3234 | 2025-10-29 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 87c45e9e-3c7b-365d-9301-764a81a5c91f | -12.7021 | -46.303 | 2025-10-29 12:40:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c1261996-f837-3be5-836d-2f1177d28515 | -3.6731 | -44.2053 | 2025-10-29 12:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ad5cdaa7-1bd0-3ca7-9e70-583aa623a006 | -4.5157 | -38.7741 | 2025-10-29 12:40:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 84da100b-04be-3573-82e0-9273b2bac0e6 | -3.7404 | -42.2927 | 2025-10-29 12:40:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| b39efd87-4b14-36f2-9b96-b536b3a81754 | -13.9337 | -48.4305 | 2025-10-29 12:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5999f75f-c7e9-36b4-8792-fa170332c93b | -3.6545 | -44.2062 | 2025-10-29 12:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9c11780d-4ab1-3dcc-8b9a-d6daacef0ee6 | -3.6731 | -44.2053 | 2025-10-29 12:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 6d026388-c741-3d40-a11c-57bcd2f4728e | -14.2842 | -47.3234 | 2025-10-29 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 56e74bce-a8c6-3e04-8d1d-774330ef6597 | -13.5682 | -47.3468 | 2025-10-29 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| db0780d2-a5ca-396e-ad30-0233b2a089f8 | -13.2073 | -47.0643 | 2025-10-29 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 211b2f5c-e8d6-3278-8989-68916f2ad56e | -14.9849 | -48.1978 | 2025-10-29 12:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 98f34b38-6f66-324e-9e31-8ce349c130ec | -4.5157 | -38.7741 | 2025-10-29 12:50:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 5a029090-d530-36aa-82df-3bf1a1e6fa53 | -14.2846 | -47.3007 | 2025-10-29 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6a8b2d2e-cc9f-37fc-b25a-93a8ddc3833d | -13.411 | -42.7185 | 2025-10-29 12:50:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 81.2 |
| a13374b4-a2a8-35ec-824f-679add341866 | -12.7021 | -46.303 | 2025-10-29 12:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1b6fc6f8-55ff-3260-b75b-a259200dd14c | -13.2266 | -47.0614 | 2025-10-29 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8d069964-9e6d-3418-8371-87a7368b7af5 | -3.6732 | -44.1824 | 2025-10-29 12:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 26ab828a-607c-3612-b1b6-32689ce311c5 | -4.903 | -42.0085 | 2025-10-29 13:00:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| fd0d2ae8-3b89-3a9c-9eef-b323b4737989 | -14.2842 | -47.3234 | 2025-10-29 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7e7966cc-5a04-307c-a7a6-3f1c915c1871 | -14.7287 | -48.3735 | 2025-10-29 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8e10c724-4399-33ae-a27c-31f0cb1a1fa4 | -14.9849 | -48.1978 | 2025-10-29 13:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 44c29e8a-f0ae-30c7-bd6d-bdc8af976985 | -3.6731 | -44.2053 | 2025-10-29 13:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 264.3 |
| ef48117a-bdd2-3da6-b5c9-8c23941b3439 | -12.3679 | -50.1539 | 2025-10-29 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 8aad540d-ae3e-367a-a1fa-b1c3e463e8be | -13.2266 | -47.0614 | 2025-10-29 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ea7cbdb4-6790-3828-b2c3-bc25121817a5 | -3.7261 | -41.579 | 2025-10-29 13:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 4e5245e1-813a-373b-97e3-112d52704b26 | -12.3262 | -48.0402 | 2025-10-29 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 01be7724-a517-36a9-a9f9-36c2ca19b9e0 | -3.7074 | -41.58 | 2025-10-29 13:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 95dbbdbf-5103-3d3e-a58c-07db53e2ad02 | -12.7021 | -46.303 | 2025-10-29 13:00:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 26b4956e-ac6a-37e9-bd27-4891fed98248 | -3.6545 | -44.2062 | 2025-10-29 13:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 4c5fe75b-3272-3a3a-bec9-c7ed157c6109 | -13.2073 | -47.0643 | 2025-10-29 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c1ca5b61-d4b9-37ac-a413-3919946ea9a7 | -3.6732 | -44.1824 | 2025-10-29 13:00:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 45897c86-a99b-3a67-a125-72db89dfe752 | -5.6392 | -41.5223 | 2025-10-29 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| b49a505b-b542-35f9-9dbf-9a4f69389ee8 | -4.4804 | -43.447 | 2025-10-29 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 371.3 |
| 7bb59529-57ca-3af8-aaa5-c795820fa141 | -14.2685 | -48.1118 | 2025-10-29 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5d025848-29d4-3aeb-b4a1-c67a0199e7f3 | -13.5682 | -47.3468 | 2025-10-29 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| de432d02-1eb5-34ac-8db0-c2a14951badb | -12.3679 | -50.1539 | 2025-10-29 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 48efdd9f-5e81-3c33-8a49-66a3609ee9d3 | -14.9849 | -48.1978 | 2025-10-29 13:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4a60623d-c7ce-32b2-a87e-a5aa54c63d20 | -12.7021 | -46.303 | 2025-10-29 13:10:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 95a798ec-31ed-3e4b-ba2f-e720588abfc8 | -3.7261 | -41.579 | 2025-10-29 13:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 0783cdbe-1819-3b41-ba00-8fd40b22746d | -15.0711 | -48.7415 | 2025-10-29 13:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| aad1ca6e-4fef-31b4-ba10-ef419b05bdf4 | -15.0706 | -48.7638 | 2025-10-29 13:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 920315ce-d33c-32ab-bb28-2c2025d7091f | -13.0446 | -47.5379 | 2025-10-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bfeb1394-67b7-35d7-8357-8711979358dd | -3.6731 | -44.2053 | 2025-10-29 13:10:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| dcf21891-22d2-3947-a6bb-a7c2a5609aee | -14.7287 | -48.3735 | 2025-10-29 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 952dbac2-9c1f-3d18-86a5-2a1c1f2efb53 | -15.4581 | -43.6408 | 2025-10-29 13:10:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 110.4 |
| a57e7baf-b112-36f4-b06f-13b3c133d60c | -13.0442 | -47.5603 | 2025-10-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 2092a42a-2bcf-3294-aaa9-2e06a3a1e93c | -3.6732 | -44.1824 | 2025-10-29 13:10:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 79821f02-51b1-31a5-a1a3-f57180afa02c | -14.2842 | -47.3234 | 2025-10-29 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 85f2abcb-4bb4-3a6e-877b-ebd501bd93e4 | -15.4581 | -43.6408 | 2025-10-29 13:20:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 113.7 |
| e88f2eb7-ba86-3a49-85e9-a1fe5875d2f9 | -4.5157 | -38.7741 | 2025-10-29 13:20:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 99.3 |
| c7e7a887-6ac7-375a-a4b9-be862ba0b177 | -15.0711 | -48.7415 | 2025-10-29 13:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7b8426fb-d78f-3128-a8e6-94775cade871 | -12.387 | -50.1515 | 2025-10-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| ded9b840-7f92-3945-b482-6ca2295c2038 | -14.7287 | -48.3735 | 2025-10-29 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bf3cd3d8-334a-3f85-a5fa-0f868ef6537d | -14.2842 | -47.3234 | 2025-10-29 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f7f6dfa9-4e1a-37a5-839b-2c4c276990c3 | -3.6732 | -44.1824 | 2025-10-29 13:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| a624b436-73e9-3694-930e-0231471de87c | -12.3679 | -50.1539 | 2025-10-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 451bbfac-3022-3052-b2a6-0218307aa273 | -6.165 | -41.5979 | 2025-10-29 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| a2cc0925-55fa-3077-b9d7-fd961cf9b56e | -13.2266 | -47.0614 | 2025-10-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4c925e79-7d5a-3db5-848b-9a94747c826b | -13.0639 | -47.535 | 2025-10-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| aaeee5a0-d432-3e40-b3b3-79b272466950 | -13.0442 | -47.5603 | 2025-10-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| cc42aa3b-70fb-31a0-a31e-34aeb8a6a8e9 | -14.2685 | -48.1118 | 2025-10-29 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a0a3d77b-912b-3c1b-99bb-1cb9e4947661 | -13.0446 | -47.5379 | 2025-10-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8dee472f-b088-3d94-afc5-b54cc8358f8d | -13.0635 | -47.5575 | 2025-10-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7e2ae87d-926c-3f98-822d-84f629d82045 | -14.2491 | -48.1148 | 2025-10-29 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b5040a0e-f18b-3818-8627-71284cf91ab1 | -4.903 | -42.0085 | 2025-10-29 13:20:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 698fb409-60cd-3152-b238-11eb5c0550e5 | -3.7262 | -41.555 | 2025-10-29 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| ff3121c0-4300-3c7f-ab12-333d4d438add | -13.411 | -42.7185 | 2025-10-29 13:20:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 5dc63bf3-b39e-3ba0-959b-549be6793d50 | -13.5682 | -47.3468 | 2025-10-29 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6ed977b2-412c-3928-998b-31f39bc22fcc | -15.0706 | -48.7638 | 2025-10-29 13:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 9aed7dd1-955f-3e8a-b898-bc7786bc96dd | -12.7021 | -46.303 | 2025-10-29 13:20:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4ec6318f-ac7a-3865-bc7c-5418c44f72c4 | -3.6731 | -44.2053 | 2025-10-29 13:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 1772eafe-3a79-34ac-82e3-643f19ccf6c3 | -3.7261 | -41.579 | 2025-10-29 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| a698dd0d-8841-3ce2-8933-b7a0e909cbdb | -13.0446 | -47.5379 | 2025-10-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 97f99e41-c6a4-3c7b-9534-86a99ead2673 | -14.2685 | -48.1118 | 2025-10-29 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2ecb052c-450e-3073-ac5d-bf5c6ccc21b1 | -3.7074 | -41.58 | 2025-10-29 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 9dabad19-9d2b-3c9a-9783-c5121fe3fcf6 | -3.7262 | -41.555 | 2025-10-29 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |


[Clique aqui para ver as próximas entradas](README86.md)
