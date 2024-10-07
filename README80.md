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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aff7d1bf-f43f-3cef-b9a2-ffc165f3265c | -2.74599 | -48.69321 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11bed8c2-caaa-36da-9529-50e7f5e00475 | -2.7424 | -48.69264 | 2024-10-07 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c40816d7-e616-38b4-97a7-d8ad41b5d457 | -4.77173 | -48.89539 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac21c877-ae81-342e-9cb3-00be5fe8a3b3 | -4.39222 | -48.70494 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a63f7ee-c251-36ee-b36b-588438a59916 | -4.39052 | -48.69144 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8927ed53-2168-3108-992c-ae20d1550152 | -4.38427 | -48.708 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f44f8f95-bd58-3847-b58d-c832d9fffd5b | -4.3819 | -48.699 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 85616fa9-c232-3f42-b95d-a0284346edfc | -4.38125 | -48.70324 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08a45251-5a44-359b-a44c-1a650b2267be | -4.37523 | -48.69358 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44545c35-209a-3ca7-aab9-670adcce5221 | -4.16666 | -48.61166 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03923838-d3ed-3ce4-a1f5-f7d42431eadb | -4.16601 | -48.616 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d96b2f2d-ae56-34ce-b256-807304ea97e7 | -4.163 | -48.61108 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48c2aae6-70a3-3cf5-b73d-54c6286cc31d | -4.16235 | -48.61541 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0584767d-5e92-3490-a221-6b30e3c59e90 | -4.09789 | -48.27099 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47506e94-c14b-3193-a921-24c0a14bc66d | -4.09549 | -48.26152 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c6259b91-f79a-3980-be77-09eb1c5adb81 | -4.09309 | -48.25197 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19de4b00-9585-3a8d-b81d-b20d21ff42ac | -4.09175 | -48.26097 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e742a400-3565-35e6-88d4-570d79160c8d | -3.91131 | -48.34617 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b4c568a-d4df-3c3f-8916-ea39f11550fa | -3.90627 | -48.35439 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fc8e270-d80a-3e64-ab94-447f67da9b23 | -3.90388 | -48.34515 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32f94e5b-b99a-38dd-bc6b-552f5da46072 | -3.90322 | -48.34951 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd511cc8-5c08-3900-84d5-0a36d1714028 | -3.90018 | -48.34456 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 413757c5-a953-31cf-93df-b43a2ef42f53 | -4.77537 | -48.89596 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c02d68ba-fbaf-381d-9c17-5cecc504bd81 | -4.69676 | -48.62123 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0dc5f0-deba-3544-bcb5-27743dde910f | -4.39352 | -48.69639 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7de091e7-a9ad-3cc5-a883-a76560eaaea0 | -4.38986 | -48.6958 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4de40fc-808c-3c7a-be74-674bb1c984f3 | -4.37953 | -48.6899 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7fd6e95-7173-3333-b346-cd401416cee4 | -4.1617 | -48.61974 | 2024-10-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b52f8619-89b6-3442-8152-894e7e12f969 | -4.09615 | -48.25706 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b511c4c-2240-324a-89ba-696beb30b94a | -4.09482 | -48.266 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6959ceb9-a4c0-30d9-a8bc-7068f30db0b6 | -4.09415 | -48.27047 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92e9ae66-c8bf-3650-aaf6-7fabdc2e1952 | -4.09283 | -48.27937 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c13e2f7-e394-3638-bab6-ff9ac1d52130 | -4.09242 | -48.2565 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2d96015-c885-3bf1-bc5c-6322a414c28d | -3.91064 | -48.35055 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73eaf55c-6906-3f73-9a0a-dd4dbc31aff9 | -3.9076 | -48.34567 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae7079c4-2ae8-36dc-b53e-bc54eefcc045 | -3.90693 | -48.35003 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0af9f92-e116-3c16-8639-e04ec228d1f9 | -3.90256 | -48.35384 | 2024-10-07 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d1f982d-6d6b-3c69-9ba1-a012ee85355e | -5.83785 | -49.14976 | 2024-10-07 04:51:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6295a5c5-dfbc-3838-9050-2642a1183895 | -5.49083 | -48.94234 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e473d16-34a9-3dc6-8315-51ef22107567 | -5.09561 | -48.88297 | 2024-10-07 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1afaec2a-7e73-3761-9383-0e83dd236fb9 | -5.64946 | -48.9581 | 2024-10-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21adab4-7eb1-33ba-8f7e-746a99a42d35 | -5.49514 | -48.93862 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b17dd1e4-cb6d-3f23-a19d-9a30690d2daa | -9.87672 | -50.14707 | 2024-10-07 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c3659ce-ad94-32d0-8040-253d3191e2c4 | -3.38502 | -49.25013 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3263a878-3f00-3dea-abba-ca3cf2b024c0 | -3.32859 | -49.14828 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26d7c489-eb2a-3d3a-a302-7a7038827dbc | -3.32738 | -49.15622 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 047247e1-8c5f-3645-b0db-31a37cf86cc0 | -3.32627 | -49.13978 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a1533c4-69bd-3ca3-9d82-1f3211dab2af | -3.32506 | -49.14773 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 383023c3-2dfd-392a-bd3f-844121c484cf | -3.32445 | -49.1517 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19b413de-8908-3d2e-bdb3-f7ca1d5b94d0 | -3.32385 | -49.15567 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f27d589-e2eb-33e0-b2c1-e2eea7e09c37 | -3.32274 | -49.13924 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52c1505b-9304-36af-a997-fa3115ce5906 | -3.32213 | -49.14322 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f98e936e-67bd-396d-a049-631bc8d4b0e5 | -3.32153 | -49.14718 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2988ed1c-6662-3366-9a23-2882b347f1b2 | -3.3186 | -49.14267 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9c68ef-b03e-3737-a91d-2a1e2211727a | -3.29638 | -49.14394 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d416af5-428f-33a8-a823-aceaeac618e8 | -3.29285 | -49.14339 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37987e8c-6461-310a-a16f-1f8306242352 | -3.29223 | -49.14735 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c6caf4-222b-3ca4-9972-98e14a89a76d | -3.27105 | -49.1441 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d58d11bf-967f-306d-b113-00c1198d6ae4 | -3.26813 | -49.1396 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06ce4b2c-5139-3123-9bb9-f0d52baa407f | -3.26707 | -49.12313 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4970b715-ea55-3403-92df-5dbd259954db | -3.26645 | -49.12712 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 439178df-ab72-3db0-ac37-68702dec038b | -3.26599 | -49.10669 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8fbac3c-3571-3d58-ba1b-ebfaddef3904 | -3.26583 | -49.13112 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d52f8589-e31a-327d-a54f-6a5f8077de3c | -3.26521 | -49.13509 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0119e2a8-0f8f-3b5d-b199-86abcf7bada1 | -3.26476 | -49.11464 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af67bf5a-c375-36be-a380-f7a0fc5e947d | -3.26415 | -49.11859 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b92714f5-cdf8-3b31-b319-b23d668ed912 | -3.26291 | -49.12658 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4bfa089a-9d3c-3416-be29-ea7b932d8878 | -3.26245 | -49.10613 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bd7711e-3de0-3716-9876-0a063f2604e1 | -3.26184 | -49.11012 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec287515-ee1e-359a-b7f0-7877d93f78f1 | -3.26123 | -49.11409 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ead6a9-678b-3ecc-b978-0f6b75cb7039 | -2.87955 | -49.47235 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84abce41-26b2-3957-bb8f-6364bfb51156 | -2.87896 | -49.47617 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efaa54c7-79ec-3540-8a56-fa1a102460ae | -2.85295 | -49.0351 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 655701ed-3b80-3e3e-8aca-952fbde1fe83 | -2.82993 | -49.13679 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e76a2413-3814-3cc7-a620-b832482df907 | -2.79069 | -49.52587 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e1793c6a-0dd2-380b-9e29-10735837c7c3 | -2.7515 | -49.52757 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fe266b5-8fa3-3da7-80a1-cce6324f68bc | -2.74746 | -49.53082 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3686be11-f1ba-3078-bc52-b7f5f6503510 | -2.69574 | -49.06876 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ddde576-d683-343c-9a9f-c91841d2486b | -2.67586 | -49.33694 | 2024-10-07 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa5126d-6952-32c6-8e38-20e1b4364ddb | -3.59392 | -49.95712 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb1487f-f781-3c96-b668-92973e44ff4e | -3.5068 | -50.27084 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7dc29463-8f92-30f8-b289-a45c41d12317 | -3.50624 | -50.27447 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 158ea59f-4a40-3f48-8da1-36fb117adf12 | -3.50341 | -50.27032 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd8545e6-2353-34ac-a791-78f4b9f79852 | -3.50285 | -50.27395 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebd7c9f-b14f-333d-b988-c454abaeb683 | -3.50003 | -50.2698 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc03edea-7b4c-3c1d-998e-46de0cdce43e | -3.49947 | -50.27343 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bead6481-12ef-38da-b04d-ac05ecf473bb | -3.42539 | -50.3838 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07c38811-b473-3bfb-a090-bd113157cc2f | -3.42202 | -50.38327 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc6864b2-93ed-340a-b208-baf4debb1597 | -3.42145 | -50.38687 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4f44253-af35-3371-8490-3a6d300384a7 | -3.4119 | -50.38169 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bfaafd31-c851-3c6c-b8ae-a974c7d6bded | -3.40797 | -50.38476 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a1232e9-ac77-34b9-a848-5c2b2e049411 | -3.35847 | -49.9139 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38221c93-dc90-3cf9-b51e-7566a48466d8 | -3.3579 | -49.91762 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cb63d83-9975-3300-8f20-3c68328ded61 | -3.35447 | -49.9171 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d63473d7-9032-34ee-9e0c-e404d1c2f641 | -3.27609 | -50.17597 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59abcf3-6ecf-39d3-9ae5-0e993661996d | -3.2727 | -50.17544 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab65658-da2c-35a0-b914-fb3cf95cf72c | -3.2653 | -50.13324 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 538d04bb-19c1-3072-84e7-7f1d875a69bc | -3.2619 | -50.13272 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1def5968-18e0-3ec4-9d52-c1189b543a56 | -3.14847 | -50.23095 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcf79d50-49cb-3ce1-b3b5-5c4f00703d86 | -3.1462 | -50.22317 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README81.md)
