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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad4175c0-765e-3c29-aef5-9b47290590f8 | -1.57298 | -53.83181 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aab61ac-5aef-3412-b380-01716418826d | -2.36892 | -56.12218 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2fa95c0-bc30-3119-839a-06cb7a93394e | -1.24292 | -51.6062 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98290b6a-e190-38f9-86cf-0c3a05738921 | -2.9096 | -54.18253 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a51f4ed-489c-33bf-8252-45507b196134 | 1.89355 | -55.72872 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a234136c-a400-301a-8f9f-d04ee72739a6 | -1.07128 | -53.16948 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba7a7621-1ad4-394e-b0dd-d1ad8bedcde9 | -3.17663 | -54.32379 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84b0b195-77ad-396f-befd-4c2f6cc92127 | -3.00091 | -53.72818 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d88d3c-56fa-3dda-bb6c-f0683affddf8 | -3.09942 | -54.0361 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c3d28d-ea1c-3fd0-a360-c788fddf264a | -1.24648 | -53.35512 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f0cb4f2-c1af-3af2-b40e-c2ed0184103b | -1.13937 | -53.79857 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ab8aa49-4481-3814-81eb-110019da7024 | -2.25161 | -53.62497 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09270b8e-e8aa-3aa5-b44e-9ef1e0782ae3 | -3.96333 | -48.08507 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc144cb2-8cb6-3c99-aa77-a71ced62cba2 | -2.59906 | -53.97141 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d776eebe-0bcb-36e9-af4e-1518019b5ccd | -1.42795 | -55.2572 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c19c8cd-5f46-383a-99de-359c3830e666 | -1.1248 | -53.73997 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcfd7375-acaa-3f06-b847-defa956051f8 | -3.5665 | -55.43349 | 2024-11-29 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 191a3a35-e691-35df-8759-88743e4cad27 | -4.08309 | -47.02815 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b07de6cc-46fb-38e8-a27c-9d0502578af6 | 0.99122 | -50.26296 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3aeb73f-a105-3433-8ba3-c122024e4e03 | -2.53001 | -54.02061 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc04539b-261d-3b8e-b77e-ea1fa75d0ab2 | -1.53421 | -52.68498 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01e27245-5790-3af7-940a-f2258ec3862a | -2.78522 | -54.04324 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 350015cd-1856-3297-9760-644e4855b74a | -2.96303 | -53.88412 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19d00569-2c16-3658-8e49-e6aeaee02bfb | -2.65708 | -48.79323 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6fbea810-d203-3173-9b98-10493b3e771d | -1.30031 | -55.74039 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e71eb11-bcb4-32ba-aef6-79af107c4b16 | -3.3498 | -49.91964 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db6418cc-a8ff-3cd7-8586-caa8db333405 | -2.41195 | -53.66745 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21f15716-86fd-31ba-8f72-c4ba0a66346d | -3.03061 | -54.01783 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650961f2-00be-3a1b-8e5c-7990c926e63e | -1.30096 | -51.73314 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39c6e4e4-ea31-3281-af84-746a2a13a957 | -1.74755 | -50.83242 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024d3fb8-9144-36ef-99ce-57457b4b4f77 | -0.27689 | -51.63195 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4f9d253-21a2-3192-884f-a8b73ff73383 | -1.49778 | -52.04524 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4fb5ac8-0606-3737-ad97-03f865a3660d | -1.65947 | -52.73253 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d0f33b9-43fb-3fb0-9369-b29dada2981e | -1.71214 | -52.63485 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72d4163b-38ad-3d16-be40-f78d1302e606 | -1.25254 | -51.78868 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e196a27d-06b1-3e15-8b31-3c9fe562fa83 | -1.031 | -53.1843 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0319425a-b64d-3225-82b4-776397d055df | -3.09371 | -53.28512 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c028f731-b514-3a7c-aa72-024449114fc4 | -2.74249 | -54.03234 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b60fab5-55ff-39e2-b16d-2fc7d7e4e75c | -2.84406 | -54.01354 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc819e23-691d-3607-84bc-536e525709b8 | -1.88214 | -52.65736 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd70530a-e296-3083-b1c7-be0f7fda584e | -3.49255 | -50.08359 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2f300e-72cc-32f4-8968-ac27268c4019 | -2.85513 | -54.02935 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c601d1ff-17f9-3af2-a60e-b9bd8e61c0d1 | -3.09828 | -53.73629 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63d42b74-3d30-3e80-a8f8-c607c06cfe0f | -2.9434 | -51.59042 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efefede8-42b8-3997-a1a2-a8fa48eea562 | -1.23401 | -51.79682 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b076153-7e02-3752-bdf6-85ee83b2a156 | -1.32598 | -52.4499 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc962b1-9efb-3bf4-bb0c-913da5f26f9c | -3.06019 | -54.4156 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 269169db-223d-3ac1-ad22-5b14647c8994 | -2.82453 | -46.84465 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd651100-1c42-334b-a8c7-30d5bc5453e8 | -3.48666 | -54.6677 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d698a6-72e3-3dfb-b93e-33d66136f04c | -3.53481 | -54.07963 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71831856-06c8-36cd-a660-c5f40a3bda68 | -3.27223 | -49.89186 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1253395-0e9d-3142-8834-9dbd49d18f0d | -3.35573 | -53.74159 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfc0f6e2-e829-3cf2-9941-d15ce9568b04 | -1.88266 | -48.54688 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d5df0c8-ad99-30db-8894-396142d6b1e4 | -1.46488 | -54.50261 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1a370e-5689-3436-8ada-caf4b0ced2e6 | -2.53593 | -53.9827 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86b8d998-c3b6-3e0a-915d-2429c1c9f5f8 | -2.03326 | -53.49924 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 526f9b1b-7091-316c-9892-7d436079a9a1 | -2.27652 | -53.77301 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22f19726-321a-3614-955f-4838f12f73fc | -2.66326 | -48.77938 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e42fd4bc-2383-3d3b-8515-a703c211b42e | -3.71316 | -47.14272 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0459fed-6aae-35bd-ab05-eae97357b764 | -2.46039 | -53.96756 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1511ff7f-9a00-3186-a73a-7c8c97927e73 | -1.27837 | -52.16684 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfafd7af-afe8-32eb-bc58-2fa7d796e9a8 | -1.27168 | -52.16582 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a57e6fbd-6c01-3c82-8aff-6df4d2216854 | -2.76518 | -55.32375 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927aa90a-41a0-3429-abc9-43f6dec89306 | -1.37081 | -53.62377 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f644d03f-d85c-340d-a5fa-56312e6ad964 | -2.8546 | -54.03279 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e10f121-3e5e-3bff-831b-97087e08f466 | -1.79573 | -52.75407 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3c01aff-b966-3faf-8eff-6f24b2639f52 | -1.21741 | -53.38511 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c781d23f-1339-30eb-bb24-675d438e1765 | -3.77107 | -51.02859 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51a2ea63-9df6-39ca-99d5-70f1d115714f | -3.96751 | -48.91655 | 2024-11-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75d4432e-8310-33ca-ab1a-42edb8c6d08a | -3.2332 | -53.91966 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27fe6413-1266-32a6-bc87-7bbea0d05c24 | -2.6617 | -48.78962 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 91f888c6-d2a6-3ef0-b6f7-bcb7f0ee56c7 | -2.81884 | -54.0449 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a6eadcf-e4d3-3959-a078-851cd1fe76c6 | -2.82484 | -54.0282 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95e2551c-b22a-3242-a96a-e3a6b0b05cae | -1.92066 | -52.89013 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59ea268f-98da-3efe-af43-d0a5b4248f8c | -3.86397 | -50.15683 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2572a4f-ccde-3ed3-b68d-4fbe4ee7abba | -1.6896 | -52.45264 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d2bfc5a-d23e-3e91-802e-8e88f39a11ca | -1.19736 | -53.88586 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09267d94-0b72-3818-9cf8-79f93cbb45ab | -3.08048 | -53.28308 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37a66036-ddf0-3033-b993-456880bc144d | -5.73612 | -46.62878 | 2024-11-29 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e74fca-e513-313b-9fe1-163a54b4ba6a | -5.17122 | -46.16287 | 2024-11-29 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e647c45a-e85c-3978-b4c3-f44fb9ea4fe3 | -1.49492 | -52.01935 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5576856-f954-37d8-868e-77b85ed08fb5 | -3.77277 | -51.99179 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fe71355-42ab-3b44-a3c7-339d211f9e2d | 0.99182 | -50.26685 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc5a658f-5832-3ffc-bbbf-4322f2f9de17 | -2.86228 | -54.02693 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e271cf1-1ed7-39d0-aa62-2fc64f2f0c69 | -3.7938 | -50.13022 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a5d538-5641-3702-8c04-74fa6535bf8b | -2.87543 | -54.0078 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bd6d86d-0263-35f5-9d37-719daa892b67 | -2.69285 | -52.91151 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a1c45e0-9d5b-3734-af9e-516d1e244df8 | -3.34912 | -53.74057 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b782e371-eb89-3006-8eaa-5313687a9da4 | -2.83537 | -54.04745 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb70ae82-88c1-3f06-9387-13ef464f7da8 | -1.44959 | -52.68253 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 465954d9-7ddc-3483-9fc0-21bf132117d3 | -4.04696 | -48.33562 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4895f157-1b67-38de-8000-fcc62cf228c7 | -1.1907 | -51.76446 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4507999e-436b-3434-b93c-b48aee85628c | -3.67797 | -54.44471 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f579460-0d41-32eb-8254-dd33cde4eebb | -1.12183 | -53.40887 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97597f2a-fe1c-33f4-8fd9-476cac40ddef | -1.49875 | -48.02752 | 2024-11-29 04:57:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7760e17-5275-3a0d-8896-e0a9b3281377 | -1.94524 | -52.97157 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c08671-0d1a-330d-8fc7-e7e7ec7eb802 | -2.73454 | -48.89001 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a85ae74e-434f-35a2-881e-28eeb94495fe | -3.20007 | -54.62987 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d367bbf-e5c4-3b43-b520-285e0e60b823 | -3.88458 | -54.21225 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2678d997-c98e-3ec7-8589-6c110d2170c9 | -2.7378 | -54.10573 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README69.md)
