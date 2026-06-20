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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67145de8-c80e-3ed4-bc26-7933c7c68bc3 | -8.63511 | -47.74897 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ac3949-4d04-3cfa-9c44-2e87d81032f7 | -6.3649 | -43.59748 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88cf277b-947b-35e7-99ef-b5e80c8abffd | -7.63138 | -50.02501 | 2026-06-20 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ca02984-2621-3e2f-841c-cef4a597ed19 | -10.76584 | -54.10616 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 176fd83a-9b4a-3c36-91db-a1eb1156159f | -8.68546 | -48.30919 | 2026-06-20 05:01:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2269547c-07a9-3a46-b71b-ff6a111f3022 | -6.78541 | -46.33376 | 2026-06-20 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9ef3e9e-4b8e-33f1-add2-952b6140d090 | -9.20599 | -58.06294 | 2026-06-20 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e9475e3-1b43-3972-9e84-43d6c0d5aff2 | -10.77699 | -54.10057 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d28999be-2f2e-32a3-abad-138966a74cd7 | -10.76864 | -54.11028 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae549c35-1ec8-39a4-918f-e2c1f4865ce5 | -5.81192 | -45.08154 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c132631-cd77-3730-9b99-6a5645c6ee45 | -4.45782 | -48.02193 | 2026-06-20 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db8a5434-643d-3281-9f7d-46b999b9ba2e | -5.81237 | -45.07826 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a1d621d-ee5a-389e-b66b-ae72f91cce33 | -8.64431 | -47.75033 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ac5ce4e-9c8e-36b5-974f-8c3cffaeeb77 | -10.23032 | -46.51273 | 2026-06-20 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d8a1530-e13a-37fe-afc0-75185db6973a | -10.58601 | -51.77652 | 2026-06-20 05:01:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 595d25d7-2250-369a-897f-fa571a43a90b | -10.13008 | -52.10721 | 2026-06-20 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e165303-06e4-3430-9ccf-53b641deaf6a | -8.64686 | -47.76319 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5c41be8-bede-3e35-9eab-e971c0c036bf | -9.85379 | -61.42921 | 2026-06-20 05:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a62b9c4-1dcc-37d2-8a1d-4fb0b288dceb | -8.64363 | -47.75507 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96a5b028-e869-3dd2-bace-ec470d3a3228 | -7.9249 | -48.25644 | 2026-06-20 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5afdbd17-0ae0-3ff3-a37f-cf81b4b2b2d6 | -6.3966 | -44.18754 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a7baaf5-1c55-37a6-b36b-9ff0fcc86c0c | -9.74845 | -47.87489 | 2026-06-20 05:01:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73df68c8-a242-3ddc-b2ad-3c553047a4d0 | -8.63971 | -47.74964 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 97888cb5-2d7c-33de-a3b8-2dca4a38e4b8 | -6.36549 | -43.59315 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5526f0-1ceb-3dca-b9c2-80ec5e87c25b | -10.22993 | -46.51581 | 2026-06-20 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfbb3ee8-0ad3-3bd1-bbf1-5ddd77e808eb | -8.88616 | -46.96305 | 2026-06-20 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138a04a8-1e82-3159-a400-1b1c2397421c | -4.35304 | -47.76566 | 2026-06-20 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6cd1e52-9540-364d-b5ae-6dbded5d3367 | -8.6442 | -47.74816 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cac9018a-6f68-3afb-a850-7e6facb8ec8c | -12.54881 | -45.023 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| e9b2a00d-e97e-3609-bd62-672513dfbcc3 | -12.42942 | -58.41243 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecb4c62c-0d27-33bf-be04-b65fc4dc0d78 | -17.44892 | -47.16355 | 2026-06-20 05:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 559dbb0f-bd16-3c62-936c-e0ca06e151f9 | -12.54358 | -45.02411 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 034866b7-5e7a-3065-82ec-7a1e43ebd021 | -13.19583 | -50.34478 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08107759-7e0a-316d-8649-da43569f4622 | -12.91781 | -49.4795 | 2026-06-20 05:04:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2316347d-77b5-33fc-aa0f-5566f99fb340 | -12.31141 | -46.73498 | 2026-06-20 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b72b716-701e-3702-981c-6af76089e57c | -13.83236 | -47.12553 | 2026-06-20 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86e049b2-ff85-37af-9adb-b90a9a08b92e | -11.31172 | -54.72438 | 2026-06-20 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 909aa6bd-268c-3f8b-b169-033e30f4c101 | -10.90665 | -56.85599 | 2026-06-20 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 83530fe2-0af2-33ee-a630-1c99d6fb48a8 | -11.44194 | -57.78511 | 2026-06-20 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc7d74ef-5cb8-336f-9af4-01caa49fb5c1 | -13.29789 | -45.22314 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff17008a-5cb3-3aee-a868-0df3859f2b4a | -12.91723 | -49.48376 | 2026-06-20 05:04:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42098f1d-c2ee-3fb9-af02-9e9d7f7bc1e6 | -13.29351 | -45.20987 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85f958da-abbb-3e98-bae4-37a91861daad | -18.42619 | -47.3928 | 2026-06-20 05:04:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1581178-3f47-38e1-8680-1288e8722139 | -12.51633 | -48.2966 | 2026-06-20 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5794d58-6163-3960-abb9-07896a4d8491 | -13.38644 | -42.39183 | 2026-06-20 05:04:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 94b624cc-f636-3798-a480-838a9972a948 | -13.20047 | -50.34163 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7e1666a-823e-3e39-94ca-c08e8b0fe9b2 | -12.51833 | -48.28141 | 2026-06-20 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cb48242-df41-3513-8960-28ecb562cc24 | -12.54893 | -45.02888 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 510a36af-7105-37a1-81cc-4a039bb59c8f | -13.29303 | -45.214 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef8175db-49c4-3833-9091-df59b44e4aa7 | -12.13648 | -48.26541 | 2026-06-20 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3671a44-6bd5-3573-bf3a-c4d74ecdea32 | -12.53876 | -45.01511 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbdb7a2c-810b-313f-80c0-6fb5afc5db9d | -12.43227 | -58.4171 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 617560c6-a69e-3ec8-bbde-c57bd1e62f05 | -12.54392 | -45.01401 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b515ab12-a74c-330c-9631-87ca50bafec1 | -12.43077 | -58.40432 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40eaf414-e588-3fa8-9871-4084614d3438 | -12.42874 | -58.41648 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69be003b-ffea-30f7-b258-767aeae5569a | -12.54343 | -45.01821 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3cf29c86-52c7-3ff5-b19f-6569fdfe3711 | -12.54307 | -45.02832 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| ca3e3b63-e49e-347b-b0e1-0969e3e48ed9 | -12.54245 | -45.02664 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| f5a759bc-8997-366c-abd2-b2fa072f3968 | -13.29885 | -45.21485 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6d0c8c7-d5ec-35ab-a374-e754ea6aa391 | -12.54294 | -45.02242 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| e8106b11-24e2-3709-a465-a3ffc802e19d | -12.54462 | -45.01571 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| e4141cb9-36f2-37d6-ad60-4a16c8e3dd2e | -12.42521 | -58.41587 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c128d9fa-dec6-3bda-b180-560a0523378d | -17.10941 | -49.75352 | 2026-06-20 05:04:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2a6474e-7b3b-3b2c-af82-cc4d942292b9 | -12.54945 | -45.02467 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 368281b5-8946-3fb4-b028-1e1a9b05de94 | -12.3162 | -46.73885 | 2026-06-20 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe732c86-a32f-37ea-8e90-4f4f7f05ff4c | -11.6627 | -56.76358 | 2026-06-20 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6082d78-b2ff-39a8-a693-f88c3bf94bda | -10.27766 | -60.54249 | 2026-06-20 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58b53448-e7ec-3b92-9241-206fad7c57f9 | -12.79099 | -44.4818 | 2026-06-20 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8404328e-6b58-37af-8238-60d57748fdc2 | -13.20408 | -50.34599 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9de38041-63bf-3a2d-96d2-65459d43c403 | -18.42406 | -47.39302 | 2026-06-20 05:04:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e20eea29-173a-3cc7-8f50-7c53f08a0b3a | -13.38599 | -42.39699 | 2026-06-20 05:04:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8bd89b11-27ae-342b-a50f-847817ed7b13 | -10.68674 | -60.7611 | 2026-06-20 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4994015-9f90-378b-afa5-ba76fa803cda | -13.38674 | -42.39023 | 2026-06-20 05:04:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 44f400b5-b3aa-31ce-9d25-8219348614ac | -12.91345 | -49.47887 | 2026-06-20 05:04:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c7bc339-91b1-30ea-9ce3-dad8b4724044 | -12.43565 | -58.39682 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15a96288-11e8-31ef-9a40-3f4936a69dcd | -14.90972 | -51.99628 | 2026-06-20 05:04:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8261df38-31d8-3da1-8bec-1c0edab514dd | -13.2046 | -50.34224 | 2026-06-20 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d431f3df-f08b-3115-bf7b-b47e50444bde | -12.54255 | -45.03254 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b5621f60-64a9-3704-b5a8-c87d7acc0e08 | -12.54832 | -45.02722 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 709085c7-cc5d-3376-911f-dfe78e3a15e8 | -11.3084 | -54.72385 | 2026-06-20 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 542730d6-9879-3306-9d04-e22f9df9b20c | -12.43009 | -58.40837 | 2026-06-20 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4be79983-56b7-32d0-8430-869a9616f789 | -11.79249 | -52.51164 | 2026-06-20 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95293d38-f78a-3fdc-bbbe-983088774e10 | -13.29933 | -45.21071 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d569890-ff54-3795-9ebe-e249a4e39759 | -10.70721 | -60.74144 | 2026-06-20 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dcebb5c-7313-347f-a6a4-a6e1f24bdb8b | -13.30369 | -45.22406 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca88bb62-65df-3b3f-b876-ac8b74c95d97 | -13.29256 | -45.2181 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e02b97c1-704c-39c0-b56f-0970fdda3262 | -12.79154 | -44.47717 | 2026-06-20 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07c297ff-3316-3f19-98fd-0f2509fefce2 | -12.55049 | -45.01626 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ae6ff7e9-78fc-3f17-94e6-c9cd2541e964 | -17.35202 | -42.62331 | 2026-06-20 05:04:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8019c14-1670-3dcc-82bb-ae9cc9631f60 | -11.30785 | -54.72738 | 2026-06-20 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7448eb67-0711-3be8-8d9e-0b21f55d832f | -12.311 | -46.73816 | 2026-06-20 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 509b469c-573c-34a0-8ee9-a8d6d0c11223 | -13.29208 | -45.22223 | 2026-06-20 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fd2e2d7-2856-38e8-a780-7d597e1d60fe | -10.90725 | -56.85233 | 2026-06-20 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48436467-5f59-3a5a-af75-d0668673b0f0 | -12.54978 | -45.01459 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f846c834-ff8d-3ac5-8630-7b73d96348fe | -12.55516 | -45.01941 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f49597fa-d0fe-3790-aaf0-6172586156f3 | -12.5493 | -45.01878 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ced6b3d9-8af2-383a-a7cb-a751f47cecc7 | -12.53824 | -45.01931 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e0b94b9-8804-364e-9fd9-76d13d8fefb4 | -11.79964 | -52.51273 | 2026-06-20 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 637457cc-c884-3f4c-b425-73f0422c9fa8 | -12.54196 | -45.03087 | 2026-06-20 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e0450748-ce7a-3efa-8252-93f113e928fb | -14.85548 | -48.12086 | 2026-06-20 05:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
