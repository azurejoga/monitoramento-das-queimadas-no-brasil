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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c75628ac-61f2-3489-a235-6df007b26c7f | -23.95156 | -54.04411 | 2024-11-07 04:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6da2531-2e18-3565-a7ea-7cb9f4b1373e | -23.95681 | -54.0515 | 2024-11-07 04:25:00 | NOAA-20 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 87ae6d3d-e5ed-318f-b978-9a5f6fa8ab2b | -3.6049 | -50.2311 | 2024-11-07 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ec1f8c3d-91fa-3cf3-ac89-5c6968374d6b | -6.1495 | -47.1771 | 2024-11-07 04:30:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| c6227a6c-bca4-3c30-91c4-65b2081570d8 | -2.8537 | -48.6642 | 2024-11-07 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 35092296-fba6-3d64-b5e7-977dd9c6fd94 | -2.8201 | -52.9206 | 2024-11-07 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| db0411ad-4c18-3294-8787-56401df2861f | -2.8386 | -52.8998 | 2024-11-07 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f9b335e1-7976-35b3-9bf3-8ec0c311e164 | -5.9788 | -45.3621 | 2024-11-07 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e40e38af-8959-334b-9593-3c8c40fdd55b | -3.5864 | -50.2317 | 2024-11-07 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| a929d098-8a99-3d2d-8b02-2a3a34bdcf45 | -1.1466 | -53.7177 | 2024-11-07 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e7e2a31d-99cd-3a5f-9cc2-31a88d272642 | -2.6228 | -51.3038 | 2024-11-07 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 34cb15ad-71de-37f0-af1d-0eeaf93bab65 | -2.8536 | -48.6856 | 2024-11-07 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 9cad4e8a-4a8a-365f-927b-b5fd9aeb260e | -2.82 | -52.9613 | 2024-11-07 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 5fc6a324-766d-3bc3-b028-d49d4e1bf474 | -5.9975 | -45.3607 | 2024-11-07 04:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| e9a31c4f-79d6-3796-9852-b23ef5ef41dc | -2.82 | -52.9409 | 2024-11-07 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5fb9184d-0db2-3495-882a-296623d514ba | -2.82 | -52.9613 | 2024-11-07 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 094f5c93-eab7-3740-af4a-f3811cfc956e | -2.8201 | -52.9206 | 2024-11-07 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a250ebcf-4c86-386c-af58-df8129eb22e6 | -3.0396 | -53.2805 | 2024-11-07 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 09620bd7-07dc-341d-af8a-5350b2a8ebe3 | -2.6228 | -51.3038 | 2024-11-07 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 1a2e6420-791c-362d-8518-2461560255fa | -3.5864 | -50.2317 | 2024-11-07 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 270.7 |
| e3509096-b3ba-3c73-8a26-aaba29203ff5 | -3.5865 | -50.2107 | 2024-11-07 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2cb2a35f-6b5c-31ab-8c4c-3b1ef4874587 | -5.9788 | -45.3621 | 2024-11-07 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 5a274e45-a90a-356f-864b-e30913f5026f | -6.1497 | -47.1551 | 2024-11-07 04:40:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| efe21f9f-6f0f-384a-9aa4-15cdc9a5bc9b | -6.1495 | -47.1771 | 2024-11-07 04:40:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6d3b20c7-6201-3e09-a1d3-79dbc41ab758 | -3.5863 | -50.2527 | 2024-11-07 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b4a4b5cb-176c-384a-83b1-f3e81538c158 | -2.8537 | -48.6642 | 2024-11-07 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8f3ec548-bced-31a9-9390-e83874a036f4 | -2.8536 | -48.6856 | 2024-11-07 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4cd95d4a-10e5-337c-9d2b-331c5de32d60 | -3.6049 | -50.2311 | 2024-11-07 04:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 780973cf-15ab-3aa8-807f-8a3ecc24d741 | -6.1308 | -47.1784 | 2024-11-07 04:40:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 32928559-0c77-32a1-b8b0-be949d92afa2 | -5.9975 | -45.3607 | 2024-11-07 04:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| edb0a553-8353-308f-b5da-bcf2a0be74ea | -3.7033 | -48.9986 | 2024-11-07 04:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fa9ed063-c81f-341b-ad2b-2e848d45ec01 | -2.82 | -52.9409 | 2024-11-07 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| aac9cee7-1133-3a97-9149-71c023ba68dc | -5.9975 | -45.3607 | 2024-11-07 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 83230688-fd55-30ac-8608-c6d2d59c92c9 | -2.82 | -52.9409 | 2024-11-07 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3bf6135b-e197-3baa-86c8-6b86da85ddd1 | -2.8537 | -48.6642 | 2024-11-07 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ce5bf2d3-cf38-3118-ac1b-21289c7492d3 | -3.7033 | -48.9986 | 2024-11-07 04:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| edd38306-88ec-3372-8a65-e26c840cc4f1 | -6.1495 | -47.1771 | 2024-11-07 04:50:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c3e61f2c-38fe-3c87-a997-6d9399d5258a | -2.8201 | -52.9206 | 2024-11-07 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9aa8abd0-8aac-34a2-a052-e4d3ee456906 | -3.6787 | -50.2494 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 33610781-bc82-3b04-a6eb-93386f7bb888 | -3.6048 | -50.2521 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9a8d78ad-59d3-3aa6-89eb-dbaa34874df4 | -2.6228 | -51.3038 | 2024-11-07 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 2eed07e9-06fd-3d06-b5de-8c5cc38a1d75 | -3.5863 | -50.2527 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 7ef92746-92c5-3530-bc80-a30af5a6d4b1 | -5.9788 | -45.3621 | 2024-11-07 04:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| b09d7be1-d7fc-3990-8a7b-1e258961d4cf | -1.1466 | -53.7177 | 2024-11-07 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c4902ad4-da21-3fc8-b412-9f0d1c444d6b | -3.6602 | -50.2501 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6ec50192-0728-36bb-9c68-16550aa0f884 | -2.82 | -52.9613 | 2024-11-07 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 38a621c9-88c9-3d58-8e07-5a51faf6366c | -3.7218 | -48.9979 | 2024-11-07 04:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 61a840cd-67f4-31e1-9ec1-e920c28475b8 | -6.1497 | -47.1551 | 2024-11-07 04:50:00 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 8c419e39-8370-33ad-89c2-2d167d49c717 | -3.5865 | -50.2107 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ea774514-20aa-3109-8a8a-171adfbf889e | -3.605 | -50.21 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 6bc688f3-e2c2-3ace-8567-5395932db00c | -2.8536 | -48.6856 | 2024-11-07 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b162b4e5-9b8f-336f-b734-8af79fd083ed | -3.6049 | -50.2311 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 56e45646-2a11-3dd4-a4d7-c569d153948f | -3.5864 | -50.2317 | 2024-11-07 04:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 207.2 |
| 6d398242-060e-3350-a938-4e42f6f04fb0 | -3.6602 | -50.2501 | 2024-11-07 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ee449240-d990-33d6-8422-08005a45a5ae | -2.82 | -52.9409 | 2024-11-07 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fa0920ce-6c35-3d11-bd7a-0e73abd633e1 | -2.6228 | -51.3038 | 2024-11-07 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dd568583-7f03-36a6-b960-0da431ac5360 | -1.1466 | -53.7177 | 2024-11-07 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8c9a8f9d-38c8-30f0-a3fa-0c7d746ea561 | -2.6645 | -49.8814 | 2024-11-07 05:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 7e590e6e-a903-3c56-a411-a5c708194c70 | -3.7033 | -48.9986 | 2024-11-07 05:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 91bac88a-f519-3203-bedc-f580d63f505a | -3.5864 | -50.2317 | 2024-11-07 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 254.6 |
| a1e29a9e-49f3-3d27-b0b4-dad0c53d2e88 | -5.9788 | -45.3621 | 2024-11-07 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 471e8384-c7af-36e8-9c92-3d806012b25c | -3.5865 | -50.2107 | 2024-11-07 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| dad49c28-26a1-32f0-869f-86cd5c1a6f0a | -3.5863 | -50.2527 | 2024-11-07 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f700aaa9-2c16-3a89-9656-5cac9133d7a9 | -3.6049 | -50.2311 | 2024-11-07 05:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 366fdec4-05c1-37bd-a74e-66247f0797c4 | -2.8536 | -48.6856 | 2024-11-07 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9d6d0b97-55f7-3c3c-b54f-f8a68d7ce461 | -2.8537 | -48.6642 | 2024-11-07 05:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 10e16164-e557-31da-9da9-f786daf953af | -2.2298 | -53.6623 | 2024-11-07 05:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| d606fa36-eb06-3e8f-a91b-12354601a0da | -5.9975 | -45.3607 | 2024-11-07 05:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 232df3a6-632b-3f15-83ee-6af7ca75092a | -2.82 | -52.9613 | 2024-11-07 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 19ab5dfd-b32c-3f76-a781-a5777f5a3a71 | 3.52701 | -51.23976 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53a43eb-e8e2-3bb1-a150-ad2a5a130431 | 3.35415 | -51.27724 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54fea393-ceaf-3446-8bc9-a4cc58b04c56 | 3.60334 | -51.30693 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d87e76a-1947-32ad-94d5-564aa6036eaf | 3.35488 | -51.28181 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8be4520b-1cd2-3319-9bdc-1f960e99db93 | 3.49585 | -51.48349 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0a2d4b9-526f-3701-8457-579b3e6453e3 | 3.60033 | -51.31219 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daebe052-1161-3f60-975e-86f49101f81b | 3.52324 | -51.24037 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ea8761-7c26-32a8-9db1-0ef4dc3579f0 | 3.60709 | -51.3063 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b45edd71-33e0-3d93-a008-bd282b2bdc5b | 3.36011 | -51.29036 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b167e165-9a1f-35e1-84aa-63e2679c08c2 | 3.36084 | -51.29493 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d326647a-3810-38ab-b591-2a2a41cbd316 | 3.35865 | -51.28121 | 2024-11-07 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f64562-420e-319c-af7c-4294d35360bc | -2.6228 | -51.3038 | 2024-11-07 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 58a7bd2f-f63e-3743-a43b-28f5d38c3165 | -5.9788 | -45.3621 | 2024-11-07 05:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 173.1 |
| a76a5652-f6a7-312a-b051-ea074f8e981e | -2.82 | -52.9409 | 2024-11-07 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b072eb66-09bb-30a0-9231-4f1d14b66296 | -5.9975 | -45.3607 | 2024-11-07 05:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 5c238226-582c-3d54-bcc7-181a7f4957d1 | -3.5865 | -50.2107 | 2024-11-07 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6f4343d5-32be-3bed-ae1b-3499841a6c31 | -1.1466 | -53.7177 | 2024-11-07 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4b40ff34-5a03-3989-9bc2-e0dfde2947ed | -3.5864 | -50.2317 | 2024-11-07 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 07fb9a41-b1fa-3cb6-900d-2c0c7cecd0df | -2.8537 | -48.6642 | 2024-11-07 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3bb2993a-0305-38ac-b91f-5a932bc31fbd | -2.2845 | -53.8023 | 2024-11-07 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 87467171-3bd5-3f2a-b75d-221ce630c115 | -3.7033 | -48.9986 | 2024-11-07 05:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 91866ea0-ac68-3fd5-944e-a1f31ba30318 | -2.8536 | -48.6856 | 2024-11-07 05:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d8bfaa0d-2896-30b6-8827-cad7aeb68f7e | -3.6049 | -50.2311 | 2024-11-07 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 12767dab-fcd3-3628-8ead-d3ba05b0d910 | -2.82 | -52.9613 | 2024-11-07 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e6fadb72-991b-3e30-b68e-f043be9321c8 | -3.5863 | -50.2527 | 2024-11-07 05:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a93f04e0-e7b7-3947-b39e-6d8e69e3341e | -2.6645 | -49.8814 | 2024-11-07 05:10:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| af983f44-c4cb-30d0-a8a8-81ee8e1157d8 | -1.29082 | -54.5637 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c73d5f6-ffdd-34c5-9ce2-6a7f7e6e6c46 | -3.20343 | -51.198 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e3044f-63e9-389c-9bd9-2b9132d55e6d | -2.98845 | -51.45889 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93c82f31-0853-3694-bebf-2781ea528ab2 | -2.81219 | -51.80483 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c37dfc9-cd6a-3204-b5d6-1622b905d082 | -1.11327 | -47.28167 | 2024-11-07 05:10:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README40.md)
