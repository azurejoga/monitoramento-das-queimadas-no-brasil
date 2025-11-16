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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72ff4061-2abf-3a20-81e4-e6f78a791915 | -4.19278 | -51.0265 | 2025-11-16 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b65d00f-7d8e-3a68-9ed0-a10836112a96 | -4.73987 | -46.38854 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe0fad5d-8176-38c4-8ce8-74c7c2e08a48 | -3.88909 | -46.13272 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803f4684-3cb0-3f9d-9e3a-70b9e46ab97b | -5.20674 | -43.47193 | 2025-11-16 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0fe93be-cacc-3bd3-b467-44e8dc1f0fd1 | -3.37288 | -41.16283 | 2025-11-16 04:06:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c578f36e-5bda-3122-8073-d6d5014fb28a | -4.01528 | -48.80889 | 2025-11-16 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45eff736-28d0-31f6-b15b-07d72ba079f9 | -5.41709 | -43.25457 | 2025-11-16 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1479b646-0430-3847-8caa-6dc6db211a64 | -2.80202 | -52.96552 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 004dd4ef-cf87-3399-ae5b-12862465a45d | -5.7203 | -41.40414 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a763585-7782-3dc2-a524-3134daa4b695 | -3.68338 | -40.87419 | 2025-11-16 04:06:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 540eafa2-f877-3c4e-b23d-d4253137b389 | -3.58236 | -41.66387 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bcd820d7-0bc8-3afc-9f0c-46dadd78606b | -5.42565 | -42.57155 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 94a3516b-cf8b-316c-8e9c-807ca7bd2214 | -4.65657 | -46.73859 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 992ea41a-5afb-342e-808c-8ee049490249 | -5.23869 | -44.34554 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6fe06d52-3153-38bc-ba54-682bd6dc01c3 | -3.89046 | -47.18866 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1868851-abb1-3936-8563-01459504ab5a | -5.53272 | -41.77399 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5499470c-4fd8-3d14-8fa5-c21442381551 | -3.58568 | -41.6644 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d64a57fb-f46e-3be7-9ba3-f1df8f3e47fa | -3.86734 | -46.06287 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e0a9583-8aed-3bb2-9959-9eb819b4e450 | -5.23375 | -44.3532 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee808190-cf79-305d-a00e-4a91905cbac4 | -2.54494 | -47.46014 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8bc5489-bab7-31d9-b758-a8924e4edeb7 | -2.17396 | -52.09494 | 2025-11-16 04:06:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bc58bf5-355b-3e3d-ac0e-fb1afe45af71 | -4.61004 | -43.30168 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd2a7610-6c7f-3e31-9030-ffdc4e7011cf | -3.96049 | -44.84607 | 2025-11-16 04:06:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dbfae87-8f4b-3fc6-8cb2-7a55c6be576b | -2.2563 | -47.19325 | 2025-11-16 04:06:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd5990f2-11a4-3c2a-b172-6bb9f5bc7ab0 | -2.42329 | -45.70865 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7082ece1-dfdf-3bc0-aa99-84891d186934 | -5.53382 | -41.76707 | 2025-11-16 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49d839df-390c-3355-80f4-99eb20baccf7 | -5.28682 | -44.29876 | 2025-11-16 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2495c2af-4b42-3211-bd9b-350921bb9708 | -2.81818 | -48.33061 | 2025-11-16 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d552744b-8f3c-3306-b90b-86a10187e0bc | -3.79806 | -43.37668 | 2025-11-16 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9606ac7-49b4-3f3d-af8a-df1f01968112 | -4.60446 | -41.73298 | 2025-11-16 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74f4efbc-1d03-3998-a019-663db94c2c0f | -5.33874 | -43.04594 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ab7a2ef4-2f66-3951-aedc-b596721933c4 | -4.6133 | -41.74147 | 2025-11-16 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24a37e9c-f3be-3b4a-b3cc-75be3b8d00bc | -3.09121 | -49.50736 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3655ccf-fc82-3128-a12e-8a398796cf0e | -2.91883 | -45.23446 | 2025-11-16 04:06:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ed55fba-d47e-3216-ab40-13479d689648 | -3.58673 | -43.13988 | 2025-11-16 04:06:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9363746-6d2d-3c39-97b8-75735797cde5 | -5.46903 | -40.97232 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aee22480-0946-377e-b3b8-b205968d1ac8 | -4.69431 | -46.31046 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 087ea7a6-1b17-33b9-96ba-5f234b941a42 | -3.85618 | -52.0852 | 2025-11-16 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa036738-6d18-393b-8dfd-504bbfe40ed3 | -5.33135 | -43.04848 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9b7c419-5be5-37da-ac60-371404a58dd3 | -6.04371 | -39.66346 | 2025-11-16 04:06:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 29e801f6-fdf8-3e2e-93b5-688a3524e2be | -3.21719 | -49.2247 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 557ae9b9-99c3-397c-ae62-9209175290fb | -2.5232 | -47.82413 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 95c40958-7c23-3722-94ae-7de6f9f16679 | -2.78785 | -43.3498 | 2025-11-16 04:06:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3486d4d4-7de9-3b67-bebb-8150145e01f4 | -5.43456 | -42.58026 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07b75c22-95b3-367e-a874-0124e2f9c8cb | -4.63305 | -46.22724 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48eeadd7-f8b6-3565-9f95-04a7da00a3c7 | -4.65948 | -46.7469 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8bde3f8-9c49-3238-a7c0-c25153debc26 | -2.95892 | -53.22153 | 2025-11-16 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83e8504b-d736-352f-a602-fb022e00a4df | -4.64716 | -47.95027 | 2025-11-16 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e719b58d-1b4c-335d-94cd-b36b8444dfb7 | -4.52095 | -43.39252 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38aab2f5-daf4-3bd3-a84c-a231185c8a6d | -4.00643 | -42.88633 | 2025-11-16 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8698062-8699-3ab7-acad-8d078bc5b546 | -5.72085 | -41.40069 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef855897-5f70-354d-b621-987cc80dfbff | -5.71315 | -41.40654 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5dc05e3a-b221-33d7-9322-87b47d395ba7 | -4.68339 | -46.52636 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1034b81a-8ee8-3b47-95fa-5dfe36f9bb31 | -5.10499 | -42.57865 | 2025-11-16 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3cb937d6-5144-3e77-a857-d5ce11755356 | -2.51469 | -47.81769 | 2025-11-16 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| b5ea44fa-8034-33ce-8017-c5c30729929e | -5.53404 | -42.702 | 2025-11-16 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1516c07-3695-36d6-9771-c3c7222e205a | -5.41313 | -41.02322 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 520ad511-3bfd-3e18-8a8b-beb630c7c1fb | -4.41919 | -40.45264 | 2025-11-16 04:06:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba1d3c3a-5a94-3d93-b357-56bb28e1603c | -4.65174 | -46.74182 | 2025-11-16 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0c3aa3b3-b451-37b9-afc4-0b8fb3434c7c | -5.32796 | -43.04792 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fe91efe-70ee-342f-bd96-30cbf3ebff70 | -4.42568 | -43.39759 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b1ce553-d043-3927-8797-c1633b5b51bb | -4.29996 | -46.27252 | 2025-11-16 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11759449-7c15-343b-ae8c-46a8f4fba5c6 | -4.54395 | -43.22923 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93f8babd-f43f-3e4f-b6dd-311954aeaa4b | -3.59286 | -41.66172 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 73d995b0-4195-31c1-a04b-521bb1c2ef89 | -3.72093 | -49.53562 | 2025-11-16 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9b1fac8-cdeb-34b0-8950-99b0f470dae7 | -4.41974 | -40.44917 | 2025-11-16 04:06:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2e3ffeb-ac63-3f25-8f7b-e6fc3a5ec533 | -4.36445 | -45.51273 | 2025-11-16 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f64c62b-85c8-336a-b7ad-c3979cbeb703 | -5.4295 | -42.5904 | 2025-11-16 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d64dc287-75e8-301f-9d26-b8f2be2f8780 | -4.21283 | -45.58094 | 2025-11-16 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4180982-f01c-34d9-a025-956574f8796b | -4.49447 | -47.65444 | 2025-11-16 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb473a69-2908-3537-8e47-56a1c1562be5 | -3.30492 | -45.80115 | 2025-11-16 04:06:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6152001f-bb61-3f7e-bde7-bca4b3c4f715 | -2.13995 | -45.35079 | 2025-11-16 04:06:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 97f08a70-9caf-3119-a36d-2492a093c703 | -2.47015 | -48.86316 | 2025-11-16 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cb39bec-0441-33ea-9ec5-fdcb0f283581 | -5.02936 | -42.84831 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1acff9e7-cd10-3f42-b6d0-2a3f6619fb71 | -5.32834 | -41.00289 | 2025-11-16 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 79d630c4-df55-368d-8237-9e201897bbec | -4.05487 | -50.73503 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8d100e7-b2d6-3e6f-9790-cfac561d57b4 | -3.66153 | -44.82192 | 2025-11-16 04:06:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a93ae5d2-8a4c-38e3-9646-3d01632bab42 | -2.831 | -48.43568 | 2025-11-16 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a08e734-c866-3a04-a5b0-b94ed1ecd110 | -5.47288 | -40.9694 | 2025-11-16 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ad845b95-ce81-3cc3-aad3-cf7b1ceead56 | -3.94228 | -47.20443 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee6e7e95-d6b0-3a32-9413-928e07a5a20b | -3.58899 | -41.66467 | 2025-11-16 04:06:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fd1bd861-c794-327f-9295-049fe718db8b | -3.22047 | -49.22684 | 2025-11-16 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a481e9ed-568e-30f1-b544-1a21841ca743 | -4.73926 | -46.39223 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fbef8d2-77b4-3498-8857-9e4b131f9e38 | -3.49168 | -54.05077 | 2025-11-16 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ac0ce9f-b3e6-30e1-97b2-d4af272342d1 | -4.05616 | -50.73121 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c8a34dd-1d48-37ff-8c41-cfd97a905b34 | -4.43466 | -46.06454 | 2025-11-16 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a271a4a9-4e72-31da-87d9-23878bcef243 | -1.98982 | -47.34772 | 2025-11-16 04:06:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43d806bf-3313-39cc-b97d-b753b8ec8f1e | -4.3962 | -49.78748 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53dc477a-bb74-3c68-9850-14930e7d86ec | -4.64531 | -45.47039 | 2025-11-16 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c694a27-b809-3521-a4f3-80a3780f98dd | -3.8753 | -44.24531 | 2025-11-16 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e909bc8-c69d-38e7-8cc7-06976363f2ee | -1.19431 | -53.72731 | 2025-11-16 04:06:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1a1cb8f-2043-39f3-9fc8-73cb22eae3b2 | -4.24869 | -50.05685 | 2025-11-16 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06cfabf0-4107-3ab0-8600-c305e3e897c8 | -3.89136 | -47.18721 | 2025-11-16 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2743477e-bce2-353c-b118-d652e4814098 | -4.4175 | -43.40413 | 2025-11-16 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1392425b-8eaa-379d-9657-824a0f09f912 | -5.33534 | -43.04538 | 2025-11-16 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f0ab81b-a6b3-37cd-b008-9f23182429aa | -4.09682 | -40.51597 | 2025-11-16 04:06:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a57a49c-c9ea-34cc-b18b-be05ef65e781 | -3.78883 | -44.1765 | 2025-11-16 04:06:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc53a382-4c94-3132-b868-665fc2fa3a5d | -0.87583 | -48.0865 | 2025-11-16 04:06:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a6e7b40-388d-329f-95e6-88da9467a55b | -4.73292 | -46.37988 | 2025-11-16 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f67cca24-9838-3189-aec5-ce504230d161 | -3.99748 | -44.27641 | 2025-11-16 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
