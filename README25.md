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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92d8677f-7f20-3278-867d-e2d15fa37f66 | -10.2659 | -45.8206 | 2026-08-08 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 77e6782d-ccd6-3544-955d-528130a2fe0d | -6.9791 | -42.9034 | 2026-08-08 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 5eb1c4fe-59cb-3e3f-a142-afa90a28919e | -14.9254 | -48.2523 | 2026-08-08 12:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ed9f1c43-b2ba-39fa-a42b-8ac7071e1b52 | -15.6968 | -54.8534 | 2026-08-08 12:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 978470db-6274-3abf-82b0-a1f3f9aafbbc | -8.5687 | -45.4252 | 2026-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 7ecb450a-21b8-310f-9b26-7b2aafb83540 | -8.5501 | -45.4044 | 2026-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| fb5b4e07-a555-3049-916f-907ed18afc5f | -11.3099 | -44.8569 | 2026-08-08 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f21d84d2-8635-37fa-9761-d2e4866316b1 | -6.9791 | -42.9034 | 2026-08-08 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| aef873ab-0b5e-349a-b625-05029b56d4bd | -15.6968 | -54.8534 | 2026-08-08 13:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e95e5439-3166-3543-b17d-76e06fac518e | -15.7163 | -54.851 | 2026-08-08 13:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 178e2aa1-1749-3eb0-84ad-411c43982285 | -8.569 | -45.4024 | 2026-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| af1fc2d9-e5a1-354e-b291-5394aece66a3 | -15.6968 | -54.8534 | 2026-08-08 13:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| dc2598a3-6f2f-3932-9003-96dc6ecdafa9 | -10.2468 | -45.823 | 2026-08-08 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 8201c646-7bd1-3320-807d-172df148314c | -6.9791 | -42.9034 | 2026-08-08 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 061dd78e-dc88-3210-9bfb-f64e2a30de96 | -11.3099 | -44.8569 | 2026-08-08 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 69b3ce3e-fefc-36c8-bc20-da99b480e53f | -10.2472 | -45.8002 | 2026-08-08 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 19308422-c275-3141-a8c0-745e56f85b31 | -10.2659 | -45.8206 | 2026-08-08 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b2020c52-f61e-37bc-a2c3-dcc342ff6f71 | -6.9979 | -42.9016 | 2026-08-08 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| bc6453cf-a428-3079-aa47-4e5ebc701cbb | -10.2662 | -45.7979 | 2026-08-08 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 6dc5d60a-0d62-3f4d-a68d-fa1d4a68f98e | -11.2908 | -44.8596 | 2026-08-08 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 722eecfb-1dcb-3dd8-bccb-73961818d7e5 | -6.9763 | -41.4971 | 2026-08-08 13:20:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| 731a6363-097b-387e-9038-bfae5d05821e | -8.5501 | -45.4044 | 2026-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 849cb02b-fe23-3c92-8ac5-da635c7de4cc | -7.3751 | -42.8647 | 2026-08-08 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 9cb7493e-210e-3167-b4c3-9e67580319b9 | -17.8805 | -40.0424 | 2026-08-08 13:20:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.0 |
| e11443f2-a57c-3044-bddf-aa739acd279b | -11.2908 | -44.8596 | 2026-08-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d9f874e7-e262-399a-b121-7e332ce3c6ac | -6.9979 | -42.9016 | 2026-08-08 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 8e6b0dbb-bb10-3be7-85ed-f6f3e593b61e | -15.6972 | -54.8326 | 2026-08-08 13:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 199c6141-933c-3e82-a414-6c5e02639a47 | -15.6968 | -54.8534 | 2026-08-08 13:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 761.7 |
| 06ce599a-9548-32bd-a1c1-88c039092ad2 | -15.7163 | -54.851 | 2026-08-08 13:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| ea952674-e2bd-3c73-955c-38eee824b4d8 | -11.3103 | -44.8337 | 2026-08-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 86feac20-8687-36bd-b2bf-76f90c7fee17 | -6.9791 | -42.9034 | 2026-08-08 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 0d10b163-e893-3a52-bf7f-de5ee5dfc644 | -14.9254 | -48.2523 | 2026-08-08 13:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 87d7b5df-72a6-3a55-b494-c7bc05c635ff | -8.569 | -45.4024 | 2026-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 83e5c276-e98d-32c3-81e3-4766b3f1fe7a | -11.3099 | -44.8569 | 2026-08-08 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 414.8 |
| 2d8fa76c-2fea-3196-8506-4481da67b67a | -7.3562 | -42.8666 | 2026-08-08 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| f5459b5b-e899-3925-a72c-998632219ef9 | -14.925 | -48.2747 | 2026-08-08 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 50cb3050-061c-3090-8734-d173384a5299 | -15.7163 | -54.851 | 2026-08-08 13:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d734b2a3-d054-34e7-8280-01e95e570b22 | -6.909 | -42.4372 | 2026-08-08 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| a4d3aa84-fe8a-333d-bdb2-ae0e2dbdc666 | -6.9791 | -42.9034 | 2026-08-08 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.4 |
| 8cb6d368-6474-333d-96ef-13e3f4355912 | -17.8805 | -40.0424 | 2026-08-08 13:30:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 164.6 |
| 53f91a3b-effa-33f9-9943-988fa2c5c253 | -17.8797 | -40.0685 | 2026-08-08 13:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 0cd29937-bd10-385b-a060-3dae372413b5 | -14.9445 | -48.2715 | 2026-08-08 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5947676e-b0e2-3b8e-87ee-ebaa3939a56d | -15.6972 | -54.8326 | 2026-08-08 13:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b60372e4-64c5-3acb-8f92-114f60de3efc | -15.3848 | -53.7862 | 2026-08-08 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 34e11256-6251-3bcc-bd9d-f05224b41320 | -15.6968 | -54.8534 | 2026-08-08 13:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 240.1 |
| 69e60684-4456-320d-a755-d4439ed8e92f | -7.3562 | -42.8666 | 2026-08-08 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| c6183e86-f755-3fda-aed9-78a377a4a8e1 | -11.3103 | -44.8337 | 2026-08-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8e357db9-c12f-3457-97e5-3654a0516bd9 | -14.014 | -53.8292 | 2026-08-08 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 23e2bbb2-65a9-3f56-bd7f-ba194df74d93 | -15.1124 | -52.7257 | 2026-08-08 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 849b3b58-3fa8-3bec-96f6-2d01bc896a1a | -11.2908 | -44.8596 | 2026-08-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 511ee46d-6a56-35b0-89a7-368e5acb9bd6 | -6.9278 | -42.4354 | 2026-08-08 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 0710e3ca-3121-33c0-84c4-52bb053b01ee | -14.9254 | -48.2523 | 2026-08-08 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 3e88bdf7-0a8e-34ae-ae8b-ed14990a0298 | -11.3099 | -44.8569 | 2026-08-08 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 660.0 |
| bff0742a-f7b6-357b-b80b-df19127b7dfa | -7.3751 | -42.8647 | 2026-08-08 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 490f2cfd-0ef7-3e94-8d47-bf44909a8a49 | -15.3848 | -53.7862 | 2026-08-08 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3d032a56-bdc5-3bdc-9081-9995f5bf3b35 | -14.9254 | -48.2523 | 2026-08-08 13:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 5fb9f475-1cdf-36aa-afd3-7b06f182531f | -6.9979 | -42.9016 | 2026-08-08 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 43a5a40f-afcf-30ed-840f-24d69ba4f686 | -14.925 | -48.2747 | 2026-08-08 13:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 187.9 |
| eb01bc88-1d25-38d0-8296-e384a681b126 | -7.3562 | -42.8666 | 2026-08-08 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 4597e115-8b03-3c3f-a7b2-e504ca160bfe | -6.9278 | -42.4354 | 2026-08-08 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| e41c4232-743b-337a-8a47-a613763148f9 | -7.3751 | -42.8647 | 2026-08-08 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 16e8e4ff-db24-32c8-8771-f8df5c37d7d5 | -15.6968 | -54.8534 | 2026-08-08 13:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 168.9 |
| f42b66f6-798f-3528-b1e0-2b6ebbf70275 | -14.3422 | -54.9929 | 2026-08-08 13:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1dfa8a8a-642a-3e78-b873-79b0c2120f9a | -15.4039 | -53.8047 | 2026-08-08 13:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e928f8c8-627c-3e4c-a7a4-e33fc6f89212 | -15.7163 | -54.851 | 2026-08-08 13:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6ab89492-b0a0-3b7a-b39f-081f32cc801b | -14.9445 | -48.2715 | 2026-08-08 13:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 998f4c93-da75-3f8c-b84b-9862fc2a97a4 | -17.8797 | -40.0685 | 2026-08-08 13:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 119.8 |
| 66fb9e14-759a-3ae7-a466-9a65862aff95 | -6.9763 | -41.4971 | 2026-08-08 13:40:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 44a66f22-35a8-3ed6-a2b1-e3ef0c19a293 | -11.3099 | -44.8569 | 2026-08-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 496.8 |
| 32573323-2887-3332-8820-df7c1c31991e | -11.2908 | -44.8596 | 2026-08-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 83b77e7b-3be1-3a89-ade8-a8425d03e216 | -6.9791 | -42.9034 | 2026-08-08 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| 54c3558a-44a7-3b8c-9247-b59fdedfa3cb | -17.8805 | -40.0424 | 2026-08-08 13:40:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 274.3 |
| eaa8f6ae-2dde-3e63-a41e-7f91c38c38bb | -11.3103 | -44.8337 | 2026-08-08 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cfabef54-175c-3a3a-b711-cb42b3a3366b | -17.8797 | -40.0685 | 2026-08-08 13:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 140.5 |
| 6804d86b-967f-3b97-b41f-3ad405f103b3 | -14.9254 | -48.2523 | 2026-08-08 13:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| d2559e22-6803-3a08-9868-5f3ee509170f | -15.6972 | -54.8326 | 2026-08-08 13:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 89f6275e-70ed-3893-87a6-7901a02c0bcd | -7.3751 | -42.8647 | 2026-08-08 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| f55b2a77-0082-381d-a7da-f044dd100c8f | -6.9791 | -42.9034 | 2026-08-08 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| 6b21586a-6e7a-376f-b687-6288aa5b5c5d | -11.2908 | -44.8596 | 2026-08-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ef225fb3-23d6-3f28-9c14-f9ef0dd835d4 | -7.3562 | -42.8666 | 2026-08-08 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 4aa438bc-c2ad-3c72-89a0-f4f4280c969b | -10.2472 | -45.8002 | 2026-08-08 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ac520484-3ffc-3867-9ac6-c55da471a564 | -15.1124 | -52.7257 | 2026-08-08 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6a5b0580-33b8-3f0b-a8ca-0bbb0d92ab64 | -15.3848 | -53.7862 | 2026-08-08 13:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c6290f2b-3fb9-36ac-89c7-9be92192a302 | -6.9763 | -41.4971 | 2026-08-08 13:50:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 49d559a2-a84c-390f-85cc-f77b632f5f5f | -11.3099 | -44.8569 | 2026-08-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 597.0 |
| 816268ce-118e-333b-91dd-fce1326fcdf2 | -12.342 | -53.1625 | 2026-08-08 13:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e035984f-5143-3ba4-b6f1-474c34ae5011 | -8.569 | -45.4024 | 2026-08-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 55f45d17-001e-36b8-bb18-1be7191d722c | -17.8805 | -40.0424 | 2026-08-08 13:50:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 284.3 |
| ae92e554-2ed2-34ea-9050-ee0a24ab8617 | -11.3103 | -44.8337 | 2026-08-08 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 744735b7-0de0-3e41-bf13-aebaebcaf2df | -15.6968 | -54.8534 | 2026-08-08 13:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e45ceec8-ea21-30bc-93fd-f28f97f00661 | -0.9797 | -55.3962 | 2026-08-08 13:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 8da1e6d6-796b-357e-9c43-9144624811f4 | -10.2662 | -45.7979 | 2026-08-08 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a976b652-3f3c-3f5b-86bd-976359d32d72 | -11.2026 | -54.8363 | 2026-08-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 173db9fd-3eba-3f78-998d-c09d6de27217 | -8.569 | -45.4024 | 2026-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 9aa19031-b3b9-365e-bb38-2d9e2c0f36fe | -17.8805 | -40.0424 | 2026-08-08 14:00:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 383.4 |
| 9dd7fe1c-b2ec-3321-8dd5-082ef7a1de27 | -14.3422 | -54.9929 | 2026-08-08 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f2249738-2715-37b1-ad7b-2c499276c0f4 | -8.5687 | -45.4252 | 2026-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 2aa9f8bc-6a66-3cc7-8e11-c4b089c33b25 | -15.6968 | -54.8534 | 2026-08-08 14:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 151.0 |
| a3b91928-7683-3d5d-aa83-752b60efafa2 | -12.342 | -53.1625 | 2026-08-08 14:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 18a1e235-c896-3b75-a30b-33c09f3e0b14 | -6.9278 | -42.4354 | 2026-08-08 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |


[Clique aqui para ver as próximas entradas](README26.md)
