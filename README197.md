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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 026d6027-2e8b-32be-92d0-8a062d55763a | -10.61281 | -68.67433 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eea9c87-ed28-356d-acc8-538ee5c11375 | -10.61429 | -68.82288 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ace88b6-a4e7-3bab-bbf3-1e572d7c8dfd | -10.62061 | -68.80554 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a87c6ef-ef17-370b-8a93-40eb04ca3223 | -10.62495 | -68.72288 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e06d923-c741-3b21-b26c-c2cc77e9f98c | -10.63111 | -68.73309 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2d78881-af60-3e1e-ad51-7d4a8b9a4bd9 | -10.6393 | -68.48867 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 810bee4a-bafe-3437-abdf-930f31e52ff9 | -10.68144 | -68.89916 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 577a84d7-951a-3a93-a21c-9289b259bb38 | -10.68514 | -68.89973 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8955f86b-2949-3ae5-92d6-d8220267fdea | -10.71171 | -68.89922 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34c69034-db63-351c-96d7-586c1fbcc847 | -10.71541 | -68.89977 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a52bdee-1605-3e35-8fad-2780f90b7739 | -10.26136 | -68.01707 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5626f3ae-133b-31b7-b937-6049826d4d2b | -10.26524 | -68.01765 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a9e1f90-adc7-3e75-9afd-1a6fd0114cde | -10.26594 | -68.0127 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f239e05-50c7-3f17-914b-de7104dcca64 | -10.279 | -67.74767 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f835d12e-b3e5-309e-bb3d-692cac084f4f | -10.27972 | -67.7425 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e99cf196-9311-3187-997b-883c3d8709b2 | -10.27998 | -67.74557 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 841edbb9-2057-3793-a265-d0c952d99edb | -10.30791 | -68.02407 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4f0f1e6-75c6-306b-8502-8fe7d75774d6 | -10.31465 | -68.0048 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52487d6f-2a7c-3129-8f2c-5c8f01d87b52 | -10.31537 | -67.99981 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56d484e-c04f-3453-909c-5b3405615222 | -10.31782 | -68.01031 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e34ce731-c7fc-3b93-a0e8-7402d012049d | -10.32314 | -67.74899 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e652d13a-1889-317b-afd0-bb0259cc4e60 | -10.32781 | -67.74449 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ab597f3-e0ff-3274-9935-9f4587a38559 | -10.33839 | -67.97791 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fde5c7d-f04f-3ad0-9d8f-e9a89c6de6b6 | -10.33986 | -67.97445 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06a1866d-cc2d-36d4-b94f-4489dcbffdc7 | -10.35034 | -68.00499 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52d709e2-fc47-3f52-943e-16410d523979 | -10.38506 | -67.87872 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68f3b7b7-b740-3911-a605-686b025b23e1 | -10.39013 | -67.95639 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2668ca1b-cae0-334e-a000-a1097a4efbae | -10.39219 | -67.88497 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e775261b-16f5-3d30-a57e-fec6de0ce1f6 | -10.39611 | -67.88557 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b1e0fbd-793a-3b05-9a99-5e2b9e6a052c | -10.40184 | -67.95808 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20ce61fb-b9bc-3c79-8373-f4c53d3bfe49 | -10.41568 | -67.94479 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dc048e8-c0f3-3282-817f-884febb8d274 | -10.41822 | -67.8424 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f78ceb-aa60-3fa9-915d-e812ec692294 | -10.43879 | -67.92278 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 472dd447-eeb4-37c9-b3f9-8d463bb9c856 | -10.45471 | -67.95073 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91e9b6b-ddf4-3bd7-a6be-89783a5a5d22 | -10.45491 | -67.95242 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e1d4d46-19ab-3ab3-9077-219eaa5faf17 | -10.46195 | -68.04491 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d245a3f1-d0f9-364a-9c01-0337dbd62529 | -10.47648 | -68.08246 | 2024-10-03 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fad9fe2-6dd9-3bdd-9671-c9508fdc5252 | -10.48302 | -67.80677 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8406e9ef-185f-38b5-bfba-51782f7a2843 | -10.48308 | -67.81046 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4756ea3-1572-3987-b728-f62c077332ee | -10.48465 | -67.91074 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 180d7aa7-0479-369b-bda1-56af5058017b | -10.49852 | -67.89741 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 304585a8-fe40-39bc-94b3-de2722b8c58e | -10.50244 | -67.898 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9961eaaf-0455-3349-9fd5-714bb393de68 | -10.50315 | -67.89293 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f07c68a-3e38-3b57-82f8-f5c784deb79a | -10.50636 | -67.89857 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac598d03-04d9-30a1-93e0-1a0401f4c382 | -10.50707 | -67.89351 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01f65849-a9bb-345a-8e8b-071b74001515 | -10.51099 | -67.8941 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f79248e2-c3cb-3fc6-a230-4aff5f62b4e4 | -10.51491 | -67.8947 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaf2ae33-7c0c-34f3-bed1-04f30e2bfd64 | -10.01341 | -68.5613 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 325e26f4-df16-3646-abf1-3e7c8197b696 | -10.03291 | -68.78237 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfe31c32-ce2d-3164-9021-c081ee3f2a34 | -10.03431 | -68.4707 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18cc5883-0236-35d0-b21a-9750f877125f | -10.03807 | -68.47129 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5f6f531-d87a-3831-8c39-83518765db50 | -10.0537 | -68.58324 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d854c6-7cc6-371a-99b9-ca5f8886c479 | -10.05744 | -68.5838 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4af4ea0-5289-37af-b330-b051db74add3 | -10.06621 | -68.03401 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d244bf-93f7-3a7c-a9c3-9c8bbb80a7ca | -10.06691 | -68.02911 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b7fbfdc-ba31-3e1b-96e3-54af943466a3 | -10.07711 | -68.31036 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 764328ba-a287-3f6d-9d2e-dcb1ef8d59c2 | -10.07721 | -68.30723 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb239b3-d199-389d-8dd8-291e735ef3f2 | -10.08035 | -68.31254 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f229960a-581a-3de4-a9ed-10b9deff0acd | -10.08091 | -68.31091 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7df8acf2-aa28-3879-98a1-9a54754b05ca | -10.08814 | -68.74059 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51fc18ef-4ace-3406-b627-242dfcd84084 | -10.09185 | -68.74117 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dba9198-bfe9-3de2-ac84-23e9ab04f64c | -10.10255 | -67.91857 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b30567b7-382e-3c28-a36f-d6b955fd2a8d | -10.10453 | -68.62808 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 771ef202-7c9a-3a4e-826c-7515ca066d9a | -10.10557 | -67.72896 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4431d47a-6f84-3352-99a0-51566e2092de | -10.10879 | -67.73466 | 2024-10-03 06:10:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b80ce7c-1671-3f48-a423-69a4687096a3 | -10.10951 | -67.72959 | 2024-10-03 06:10:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87cce5cf-335d-30db-a9d3-ab557f827c29 | -10.11002 | -67.89433 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a973e7ef-b504-39fc-bba3-296fce7b1ff2 | -10.11273 | -67.73524 | 2024-10-03 06:10:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d11ac126-ce82-36f5-ace2-ee0858462a05 | -10.12145 | -68.00733 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cb6f6ef-54e6-3c50-98c1-b72a6219e981 | -10.12273 | -68.00895 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c69bcd32-3235-3633-9fda-52efd7be36fa | -10.1246 | -68.01281 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fd4f0b9-8132-3350-9866-1291525c29be | -10.12517 | -68.0629 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f6be9e-5e4e-3fb0-8058-132c190f46d3 | -10.12532 | -68.00791 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1ce4549-4bfc-32eb-a731-70a6b3215d77 | -10.12592 | -68.01446 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e591c2c8-72cc-3059-b224-728560e9a4f0 | -10.12728 | -68.00464 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e7d1e7c-aefd-3c88-8db1-426aeab1560e | -10.12847 | -68.01341 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 918155d6-41d8-395c-b69f-f0598d0015a6 | -10.12979 | -68.01506 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94169c52-ecbf-3898-bf36-7ccb1373e8ff | -10.13366 | -68.01565 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e70b60c-e81f-3d31-9cbc-2f1da92a909e | -10.13753 | -68.01624 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36e4f366-3340-3c25-979f-391cce167027 | -10.15233 | -68.02349 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 592ebaf2-1372-36d0-a926-c3c020a9aceb | -10.17008 | -68.17516 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e844af9-ce8f-39ad-b925-8182d2db0a49 | -10.17166 | -68.43158 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a67a9a68-35bf-3f7e-816e-c9c8271798ee | -10.17209 | -68.42959 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7432e58f-bc17-384f-99b0-8bb2222da130 | -10.17234 | -68.42691 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0b1c24b-340f-3a23-9e2a-c76967e27b57 | -10.17274 | -68.4249 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30130edb-745f-35d6-92ea-3c6d6e96c7e3 | -9.84451 | -68.79483 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05dbc38a-2535-3a2b-8890-732f49bb3cfd | -9.88561 | -68.32294 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570b79af-cdd2-3924-841a-bd39ab826131 | -9.95417 | -68.75962 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7043f1f-367b-3f14-97a0-fd6fd9815d17 | -9.9827 | -68.74547 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5909aa92-e4bd-3041-b357-044859c55d7b | -9.92431 | -68.50839 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07f76b38-9d23-349f-b2e5-9ae6b869c343 | -9.92056 | -68.50784 | 2024-10-03 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9219d43-bb03-3251-a41e-b9242872f3d3 | -9.91013 | -68.82971 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 050ce4bc-1dfd-3e5d-a4bd-d9ab1c3ca089 | -9.8482 | -68.79537 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37f516d-367e-3bdc-8fe8-979de8c414e5 | -9.83097 | -68.91355 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f7abb0-ac10-332a-9751-a6f6eee677dc | -9.82794 | -68.90863 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a57f45e-224c-3134-ad43-ead56dc3195b | -9.82731 | -68.91299 | 2024-10-03 06:10:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25ce4d77-d36f-381c-be3b-4efdc6f37950 | -10.52923 | -67.85016 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7588e8d-3fe8-38ef-b014-15e0d4f14431 | -10.52851 | -67.85519 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd4c9429-9178-3bbe-8cb8-d46e013c462a | -10.52529 | -67.84962 | 2024-10-03 06:10:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14b3cdbe-3b1b-3a33-8d58-c288c633dc10 | -14.40619 | -59.55898 | 2024-10-03 06:10:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README198.md)
