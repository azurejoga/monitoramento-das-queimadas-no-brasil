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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bc50fea-bdc7-3b5e-a494-1c8d693d4283 | -12.8363 | -44.3186 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 1dcae948-854c-387f-8943-b43159daf291 | -12.7557 | -44.4959 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 431.2 |
| cc89b3e1-b44d-38dc-bfde-3ff33a6b1009 | -12.8359 | -44.3422 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 707.7 |
| 1db363f2-7d0c-353f-965d-7f5d14141bfb | -12.8354 | -44.3657 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 305.3 |
| c4449e8c-18e7-3401-99ce-505196b3321b | -11.4338 | -56.0509 | 2026-07-01 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 264.5 |
| b8a1d6dd-b7b2-37ec-a31a-3749615e8a7a | -12.7553 | -44.5194 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bce81d5d-0856-3c5d-87af-e1f5b50a5f6f | -10.9209 | -43.0384 | 2026-07-01 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| d59a7358-71ab-3879-91dd-65e09c23dad4 | -11.5528 | -47.4546 | 2026-07-01 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bf1761f9-8b80-3ca3-a323-612f9afc63c0 | -12.776 | -44.4458 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| ec06fa02-7372-369c-8b26-86d70472a865 | -12.7755 | -44.4693 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 772.6 |
| 31f43b4e-e1e0-3ef6-bed6-96ba4968e6fb | -11.4336 | -56.0711 | 2026-07-01 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 298.5 |
| 0515a845-101a-30d8-9f06-11977202a009 | -12.7751 | -44.4927 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1030.7 |
| e3392e06-4f36-34e1-b47c-4a6bfd4d00c2 | -11.4147 | -56.0726 | 2026-07-01 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 4016fede-3c78-3b4d-8fe1-f7b4ee8da93e | -10.9205 | -43.0622 | 2026-07-01 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 506c9fe8-16ee-30bd-83b8-de8a76d75c3e | -11.6286 | -59.0169 | 2026-07-01 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| e08e3a92-e622-3d44-a16f-3b5efdb7bbe2 | -12.7562 | -44.4724 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 340.3 |
| 0e4cfa8b-a426-32f5-9383-c593cc30bcef | -12.8548 | -44.3625 | 2026-07-01 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 81f53e15-56f2-306c-8a6a-927f76fbf546 | -12.8165 | -44.3454 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 182bfb33-8e27-3282-aea9-7ce6f3d75fed | -11.6286 | -59.0169 | 2026-07-01 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| eff4ab9b-e422-3d2a-a1da-040d80429862 | -10.9397 | -43.0593 | 2026-07-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ff21c652-96bf-37f6-be70-f8bbbbd9be8a | -12.8354 | -44.3657 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 257.7 |
| 463b6cc2-96f1-3a37-bc95-69038f1f0b6a | -12.8363 | -44.3186 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4d03da9d-d432-37aa-a229-9b4580e99c88 | -10.6784 | -54.5356 | 2026-07-01 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a0a024a8-18c3-3444-ab85-c4689ef61d9f | -12.8548 | -44.3625 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 0625fad1-1ec8-3a29-8586-bfe2134ed346 | -10.1237 | -52.0905 | 2026-07-01 03:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3cea9380-bc37-3761-a97d-ccdb6c4a6345 | -11.4149 | -56.0525 | 2026-07-01 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3427fdea-4286-3261-9e0b-8609e2732aa1 | -11.4336 | -56.0711 | 2026-07-01 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 267.3 |
| b330ca85-8211-3da8-95e2-a9cc8dbd7f14 | -12.776 | -44.4458 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 9e8ca9fc-35bd-361f-bc8b-4c927962b5e3 | -12.8359 | -44.3422 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 650.1 |
| a7ed099a-103d-355d-9894-3235526d816b | -11.4338 | -56.0509 | 2026-07-01 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 219.1 |
| 8e0f0fde-26ff-3e36-81bd-f1de30415f48 | -12.8552 | -44.3389 | 2026-07-01 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 309.6 |
| 0949ae35-6132-3c89-b2a6-5764c881754d | -10.9209 | -43.0384 | 2026-07-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 7d7fc960-dfde-3d90-a7f1-82a2acfb997f | -11.5528 | -47.4546 | 2026-07-01 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7ecadf5e-9f7d-3ce3-84b2-681f1fd87cfa | -10.9205 | -43.0622 | 2026-07-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 442d44df-3d52-3545-86ec-0740f3560625 | -10.9401 | -43.0355 | 2026-07-01 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9f9a3dd9-e796-31ec-b15e-4f88a3f64134 | -11.4147 | -56.0726 | 2026-07-01 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 0f251e66-d4b5-38bc-beaa-8db4268d8b88 | -10.9401 | -43.0355 | 2026-07-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8f6fa3ca-fd4a-3fca-84c9-380027caef83 | -10.6784 | -54.5356 | 2026-07-01 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b7163082-a4d7-394a-9e44-6da25bc61392 | -11.4147 | -56.0726 | 2026-07-01 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 54f7d3f4-0204-32b5-a268-160bb5826399 | -10.6787 | -54.5153 | 2026-07-01 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 54cb0aad-4993-3fb7-b811-6bd1bdfeeef0 | -11.4149 | -56.0525 | 2026-07-01 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 740deba5-e12a-3fbd-8baf-e9c79a4dadc4 | -10.9209 | -43.0384 | 2026-07-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c8ce3105-ecde-3622-9bda-b5a36f5168e9 | -8.5933 | -48.0069 | 2026-07-01 03:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| fc85eba9-5a8e-34be-8ab8-187b00c9303c | -10.9205 | -43.0622 | 2026-07-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| d25b05f6-780d-3a29-8a82-5a202d87ca83 | -11.5528 | -47.4546 | 2026-07-01 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 60d09004-7248-3691-8ee9-3687fc79ba57 | -10.9397 | -43.0593 | 2026-07-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 27f10909-261b-3ed5-8b87-fd1435f8f598 | -10.1237 | -52.0905 | 2026-07-01 03:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 123d7881-699a-30db-8eb6-cfb1bf01f85b | -11.4338 | -56.0509 | 2026-07-01 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 193.7 |
| b34fbe49-4ff9-327a-906a-a1acc1cdb539 | -11.4336 | -56.0711 | 2026-07-01 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 208.3 |
| fd5c9301-d2c2-3589-bd01-64e1651297ff | -11.6286 | -59.0169 | 2026-07-01 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4e4aa392-8fab-3975-a09e-1c7ee31ccb77 | -5.13479 | -37.84236 | 2026-07-01 03:15:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 23.1 |
| ec627cd0-dba6-354d-a284-0d2aa1a30491 | -5.12887 | -37.84128 | 2026-07-01 03:15:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42496182-c738-3cf5-b7ce-725cc283ce8c | -5.13403 | -37.84668 | 2026-07-01 03:15:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5be96ce9-67c5-35ac-b06c-fa39e805338e | -10.75985 | -42.11194 | 2026-07-01 03:17:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4431cb7f-67ee-37fa-a79a-13fa1ffb0071 | -13.08681 | -42.14064 | 2026-07-01 03:17:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8332002d-4134-3fdc-96cd-e716a4a42af7 | -10.75291 | -42.1104 | 2026-07-01 03:17:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea3b2cee-0103-3311-b80e-8513a2482a10 | -15.21911 | -42.598 | 2026-07-01 03:19:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9451554c-39b6-363e-b073-f3902a350b60 | -15.21581 | -42.59767 | 2026-07-01 03:19:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f65871-c471-3c1b-b38b-4b11840401a9 | -15.2171 | -42.59185 | 2026-07-01 03:19:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e8e390-ea31-3956-a0b0-ea95f79c65b8 | -12.7746 | -44.5162 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cc42143b-ea48-3e21-8ef6-8c8d9615c929 | -12.7755 | -44.4693 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 668.3 |
| 2b721e31-bfb8-3819-9068-4fc2912fd407 | -12.8354 | -44.3657 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 30d44bc6-b426-373c-8b27-471d51486619 | -12.7557 | -44.4959 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 441.6 |
| aabe32d0-322b-3af9-99ae-77a728361221 | -12.8548 | -44.3625 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 89deb445-9f1f-3181-8f13-65be1247ea94 | -12.7553 | -44.5194 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c440bd3d-f85a-317b-8425-1dc6ea79bdbb | -11.4147 | -56.0726 | 2026-07-01 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| fe7485d4-a21c-301d-876f-d0b30ee61d5d | -8.5933 | -48.0069 | 2026-07-01 03:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5ae70eb1-40d4-327c-9b84-2f494a3947e4 | -11.4338 | -56.0509 | 2026-07-01 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 8e83c634-b123-3bba-9368-b2f36e0c83eb | -10.6596 | -54.5372 | 2026-07-01 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| cedc2068-c8cf-3782-a825-180639260ed4 | -12.8165 | -44.3454 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2a716cf5-9e3c-3d25-8c6c-b93c79e847c2 | -11.4336 | -56.0711 | 2026-07-01 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 2a9c1542-107f-31ad-8660-f12fddeb9264 | -10.9209 | -43.0384 | 2026-07-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 8d31d720-9a0a-3587-9dc3-59ad5c61a20d | -11.4149 | -56.0525 | 2026-07-01 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| def82b99-6df1-382c-8346-71f994b5ad93 | -12.7562 | -44.4724 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 316.4 |
| c54a4137-8fd7-36af-94ce-e1f5833f6912 | -10.6787 | -54.5153 | 2026-07-01 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b3f4df2e-df48-3646-b4d9-da303e4e8cb3 | -12.8359 | -44.3422 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 595.8 |
| 80da4e6c-dfe8-3ec1-bbbf-c955f9d288fa | -11.5528 | -47.4546 | 2026-07-01 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 35b57e87-15d1-3502-b144-f3a16f618521 | -10.9205 | -43.0622 | 2026-07-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f8af9215-5c09-374e-8d15-11058a89211d | -10.6784 | -54.5356 | 2026-07-01 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ef85e398-ac1c-3126-ba8a-cde8544374a5 | -12.7751 | -44.4927 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 958.9 |
| 57768c4c-a4fb-3ceb-9621-896fa23c7181 | -12.8552 | -44.3389 | 2026-07-01 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 277.3 |
| d49c897e-f69c-3a45-b320-c3aff82f5cd6 | -12.8354 | -44.3657 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 6711d4dd-702b-37a0-922c-004b0443d5d6 | -10.9205 | -43.0622 | 2026-07-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 63deb954-44fb-3828-bbdb-eb5ed6734667 | -11.4147 | -56.0726 | 2026-07-01 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 1b2c7515-ff01-3c18-a203-9e43b0b10431 | -12.8359 | -44.3422 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 577.5 |
| 7ee4346d-beae-339c-8905-f00514897fce | -12.7557 | -44.4959 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 398.6 |
| 0469e5b6-faff-3123-97a1-734a9ff1c44f | -12.8363 | -44.3186 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 018f0655-c8c7-32c9-8e15-ef377f3b2093 | -12.7562 | -44.4724 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 277.7 |
| e662b97e-c54d-33d5-a1ae-58ee93f87070 | -12.7755 | -44.4693 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 634.9 |
| ff8e369f-5009-348d-bbba-8a69934acd37 | -11.5528 | -47.4546 | 2026-07-01 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 238931c8-bb47-32ca-9b34-1c81904ba789 | -11.4338 | -56.0509 | 2026-07-01 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 7c2b7df3-5006-3de9-b7fb-fa218cbc91b2 | -12.8165 | -44.3454 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 69faa41c-db66-3b74-ab04-acea8581648a | -10.6598 | -54.5169 | 2026-07-01 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d2d72c88-de73-368f-bb0b-bdf403d736ad | -11.4336 | -56.0711 | 2026-07-01 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 250.7 |
| fa5386f5-d6c5-3e95-9070-74029782fbc0 | -12.7751 | -44.4927 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 979.0 |
| a013e6c7-eae9-3928-a011-12328cb61797 | -10.6784 | -54.5356 | 2026-07-01 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2a26e724-9261-3375-8d10-fc8112b0c82d | -10.9209 | -43.0384 | 2026-07-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1ca42f79-e06e-3a33-84d0-9ece69c3f4ae | -11.4149 | -56.0525 | 2026-07-01 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1873e223-ed3f-3dd0-8000-f22faf083eb9 | -12.8552 | -44.3389 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 83eaf991-0f68-3fc4-b175-3313cede1504 | -12.8548 | -44.3625 | 2026-07-01 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |


[Clique aqui para ver as próximas entradas](README8.md)
