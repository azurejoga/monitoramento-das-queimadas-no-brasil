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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da24254f-eb58-365a-b77b-fb15fa08135e | -4.30202 | -48.06645 | 2025-10-18 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 3fe9579c-68f4-34c1-a8b3-44e7b53dc9b2 | -3.83679 | -47.41234 | 2025-10-18 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f35ddf37-22e4-32fc-9d9d-adaf534003c2 | 0.99645 | -51.18962 | 2025-10-18 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8ece88d5-2d8d-3a55-b3c9-d8dfceb9ef75 | -5.16873 | -48.59976 | 2025-10-18 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 76972c1c-ab3a-3fed-83b3-6e5c1014ba0f | -2.91819 | -52.7243 | 2025-10-18 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ca831292-2839-33cb-ad3b-71aae2730a8e | -1.94739 | -56.85666 | 2025-10-18 00:54:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| be5a31b5-76c9-3f20-ae26-b77d6a609292 | -3.86426 | -51.90522 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5087a879-a8bc-31af-9d5d-db9f382a2278 | -3.46723 | -50.03062 | 2025-10-18 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3614c86b-a7af-3e61-8a2c-31169b1e275d | -7.1927 | -49.94236 | 2025-10-18 00:54:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8b378ba8-43b6-3d0a-b0c5-bd8eab74175c | -1.94795 | -56.66106 | 2025-10-18 00:54:00 | TERRA_M-M | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 408481d2-92a8-3b42-8b67-8b0f2d03a1ce | -5.71349 | -49.10096 | 2025-10-18 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b69446d5-fdd3-305a-b79e-98bc66fa77d4 | -6.76481 | -56.86606 | 2025-10-18 00:54:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 533eca95-aed3-3771-956b-98015eb3e9ce | -1.4175 | -60.40009 | 2025-10-18 00:54:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 51bd6639-e4dc-38b8-b53b-5441be1b4c87 | -3.79396 | -51.77343 | 2025-10-18 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 53fff9f3-5de0-3962-937c-c4399e93ebef | -3.99393 | -45.49172 | 2025-10-18 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 113a9387-155e-3103-a215-fd1ae7dbdfad | 1.80504 | -55.71378 | 2025-10-18 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7706ef37-2e41-390a-a248-72e6dd99f8c6 | 1.77088 | -55.96047 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ea94f78a-7b3c-3dd2-9fcf-3d8240c2c51b | 1.76693 | -55.92411 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c80d1f33-51b1-3a2d-9d73-0f0b8035f307 | 1.76966 | -55.96925 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 191597e0-3a59-3b9e-b542-4c530723940c | 1.50029 | -56.04744 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cc2eeb3-514c-36aa-a618-68843858fc45 | 1.76085 | -55.96802 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| abb34a8f-a087-3d54-a27b-949d584f6647 | 1.76207 | -55.95924 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8a4c70f4-63ed-3434-8d0d-abb58386b38b | 1.73584 | -55.75812 | 2025-10-18 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1caf0aeb-8f70-3208-87ac-1e08465d0cc0 | 1.76601 | -55.73534 | 2025-10-18 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ce8813c-7317-3b1d-b45f-5171acc634ca | 3.16907 | -60.32701 | 2025-10-18 00:56:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4e2dfaab-e453-3a09-be0c-5c3baa9a4813 | 1.77209 | -55.95169 | 2025-10-18 00:56:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76e9fa1f-9c4c-30bb-bac7-f4621b08ebd8 | -14.277 | -51.8593 | 2025-10-18 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e6843cee-628e-3bc8-b062-4e60755bcc66 | -10.5132 | -43.4289 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| d68a7fac-c1d5-3514-b53b-96d60513c183 | -4.4445 | -43.2397 | 2025-10-18 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 46bdd866-ad6c-341f-b0d6-d9c0e29f683f | -10.4941 | -43.4315 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 501.4 |
| 0e843d3b-a0b9-323c-80e0-7da204815213 | -2.9128 | -52.7146 | 2025-10-18 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f59bacf9-8e71-3b31-9edc-7e9b266ad0e7 | -2.9127 | -52.735 | 2025-10-18 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d03d636f-1b61-35fa-b1c3-1a8434015d1a | -3.1431 | -50.2464 | 2025-10-18 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d0d3e5dd-219a-3edf-984e-337ebc134755 | -10.4937 | -43.4552 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 3eb8b066-0203-3191-bc54-9d1c6b9b3405 | -11.6109 | -44.0678 | 2025-10-18 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 7a7c344b-7c67-3f67-851e-e1553e67640a | -11.6104 | -44.0913 | 2025-10-18 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9a8a2952-3b30-3894-ba1c-3b08d9a384d0 | -10.9944 | -44.3217 | 2025-10-18 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9a0b11e8-2b9d-30ed-89af-05214b6d1d48 | -4.4633 | -43.2152 | 2025-10-18 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 054dbfa9-11fe-395e-bf51-d7288b0b30e8 | -10.4945 | -43.4079 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| c8f9d012-9697-3730-9786-a45e5588ccd9 | -11.204 | -47.8318 | 2025-10-18 01:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0dc3b948-f1fe-3320-b0dd-0aa2ae1bd623 | -5.0029 | -46.0108 | 2025-10-18 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 38e747d2-db61-3942-b74a-29236e5faba1 | -10.9564 | -45.4579 | 2025-10-18 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4cfc3036-c6d7-33c7-91c5-9bc4f229362a | -5.0214 | -46.032 | 2025-10-18 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 835646a3-0b8a-3e0f-bc7f-1762c2c316e7 | -8.9498 | -46.5789 | 2025-10-18 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7368399e-df20-3321-8aa3-fe5433ad045f | -10.0874 | -47.6547 | 2025-10-18 01:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0296dfa6-026a-30b9-9dde-f0aaa47430b0 | -4.0007 | -45.5054 | 2025-10-18 01:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b584d163-1d1f-3303-8fbf-9017cfca11bd | -10.475 | -43.4342 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| f5263e60-1152-3a18-8c8e-104c085f21ae | -5.0215 | -46.0097 | 2025-10-18 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 4f2d3920-b599-3975-9cb5-c307997f979d | -10.5128 | -43.4525 | 2025-10-18 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 607a848b-0c43-3348-92c0-dee50df120e7 | -4.4632 | -43.2386 | 2025-10-18 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 91a87c2d-ba94-33a8-b27e-c213b0b558b1 | -18.3934 | -55.477 | 2025-10-18 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 6df410dd-4298-35c6-b990-4a275e06c31f | -10.9752 | -44.3244 | 2025-10-18 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d6459961-2ced-3467-9122-c2e2ff3a2317 | -5.0027 | -46.0331 | 2025-10-18 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 87cd6bdd-a442-35d1-a49d-dbbf43f5a920 | -2.9257 | -49.1747 | 2025-10-18 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 55c71519-560d-3e37-9a27-8e03317e9fc8 | -13.4663 | -43.7617 | 2025-10-18 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 370dd9fe-22c8-32a1-afe1-6460d57a6b88 | -3.8572 | -41.5719 | 2025-10-18 01:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| d8f7703a-7253-368e-ad6d-50e22995aa5d | -4.4446 | -43.2164 | 2025-10-18 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c6e2f50a-eada-3784-b1dc-2b7c532877b6 | -11.5917 | -44.0707 | 2025-10-18 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4fb03ee1-feba-3ff2-b1b3-e9622b0b96c3 | -12.398 | -47.2056 | 2025-10-18 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 38cacbb1-0bbb-32a9-b2d3-09bf77e6b7a7 | -8.389 | -46.2333 | 2025-10-18 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fa05b76d-25ea-3bb9-b97a-bf5c24d67820 | -13.2296 | -43.9692 | 2025-10-18 01:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4e750494-f399-37b7-b538-c73d29584a04 | -5.0029 | -46.0108 | 2025-10-18 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0186cf44-fea5-32ec-a14a-df2b7507f690 | -2.9127 | -52.735 | 2025-10-18 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 532dadaa-1100-373d-95c7-63162bd360a8 | -10.1528 | -44.5289 | 2025-10-18 01:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 937e7997-93d0-38fa-801d-f8ae4f7c1800 | -5.0214 | -46.032 | 2025-10-18 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a2e36742-a15a-3a71-97ba-1f7bcfa75480 | -11.204 | -47.8318 | 2025-10-18 01:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 0867bf8d-6aa0-3990-90a8-4241bbae6890 | -10.4945 | -43.4079 | 2025-10-18 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 04284a12-ed97-3bb5-81a3-fb0cd7457534 | -11.6104 | -44.0913 | 2025-10-18 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 78279dfb-0c56-3e46-b358-e6bb7dec467a | -8.6029 | -40.2083 | 2025-10-18 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 86.6 |
| daf90405-0988-37fc-bb36-02dcdfc296dc | -10.4941 | -43.4315 | 2025-10-18 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 401.2 |
| 5619ec6a-d4e5-32e4-9279-1127826e9560 | -13.4663 | -43.7617 | 2025-10-18 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 7de0afdb-b781-3c27-9115-c3bd5256688b | -18.3938 | -55.4559 | 2025-10-18 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.4 |
| e6707ae6-9d29-3c0f-8660-44490c1bf48b | -3.8572 | -41.5719 | 2025-10-18 01:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 67cb379e-f56b-3746-871d-df0f067f831a | -10.9564 | -45.4579 | 2025-10-18 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 7641c6ae-350a-3713-b339-b5478ea26bb8 | -12.398 | -47.2056 | 2025-10-18 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 01ec473b-6a89-3c4d-a258-f677e99b3fad | -2.9257 | -49.1747 | 2025-10-18 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 121e79ff-7caa-307f-8ec2-18561617463c | -11.5917 | -44.0707 | 2025-10-18 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c181a134-7685-3afb-8d8f-fda190fe99db | -10.4937 | -43.4552 | 2025-10-18 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 0321de4e-3678-3739-9738-390938a15241 | -11.6109 | -44.0678 | 2025-10-18 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 5a1940ac-1d50-3f04-bcff-58b3ce4dd357 | -5.0215 | -46.0097 | 2025-10-18 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1faf1804-37de-350b-8ace-7e86f81f2e54 | -10.9567 | -45.4349 | 2025-10-18 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 692c33ae-d445-3a38-b58e-634a81257bf2 | -10.5132 | -43.4289 | 2025-10-18 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 63e7b5ad-db0e-3a81-862e-92b0733f5b10 | -3.1431 | -50.2464 | 2025-10-18 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ed671954-250c-3d80-811d-98eaae24cbc9 | -18.3735 | -55.4798 | 2025-10-18 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| c97d18a9-d1e8-3c78-88e0-64619ece72d3 | -14.277 | -51.8593 | 2025-10-18 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| df3f794d-a548-3470-b4b0-11be15e50312 | -8.6032 | -40.1834 | 2025-10-18 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 83947e9a-6964-3334-90ef-0a6dc10cbee2 | -13.2296 | -43.9692 | 2025-10-18 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 817966f0-e134-3118-9ec0-4d2de42ff403 | -2.9128 | -52.7146 | 2025-10-18 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b47e3893-e540-3a66-be79-15c358903334 | -18.3934 | -55.477 | 2025-10-18 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 67d26213-50d2-3a6f-a828-517fd6080185 | -10.9752 | -44.3244 | 2025-10-18 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a721be0f-d9ba-3411-935c-07e1672823f5 | -10.9944 | -44.3217 | 2025-10-18 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6e3caa65-96f6-3dab-a6b9-8aafad11362b | -8.389 | -46.2333 | 2025-10-18 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c28102d5-f3cf-311a-8d1a-ac86965efb9c | -10.9755 | -45.4553 | 2025-10-18 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 5dbb7c10-e8d3-3fee-bf0c-7f0e43f7db66 | -10.5128 | -43.4525 | 2025-10-18 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ff5990b2-36c6-3882-828e-54563be4a88c | -10.1528 | -44.5289 | 2025-10-18 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2a28f943-85e7-35e7-a3b4-1cfe60e6a9c1 | -10.9564 | -45.4579 | 2025-10-18 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e4926f51-079a-33c9-9456-93341a5500d9 | -10.9567 | -45.4349 | 2025-10-18 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 35eec454-be7a-3e73-8ba4-bb56cf1282ca | -5.0214 | -46.032 | 2025-10-18 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5e15339f-36b9-3245-a576-43eee9ae0572 | -3.8572 | -41.5719 | 2025-10-18 01:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| c86e9838-6fda-37e6-94af-996f10bff04d | -10.4941 | -43.4315 | 2025-10-18 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 308.0 |


[Clique aqui para ver as próximas entradas](README7.md)
