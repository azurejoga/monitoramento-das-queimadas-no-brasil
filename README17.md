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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fbe6f68-2396-363c-ad58-f20b19e75721 | -7.86631 | -47.87113 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d698b31-df15-3da4-8fd9-608b2abcbbbb | -8.5535 | -51.5776 | 2025-06-24 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8587f1a4-1783-3e58-b64a-4fb84169f7bd | -8.5722 | -51.5761 | 2025-06-24 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6e301d96-a66d-398c-bf7d-7966eecb369c | -8.5537 | -51.5567 | 2025-06-24 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 6f5ebc6c-75ee-3983-b802-daa5e5224dbf | -8.5724 | -51.5552 | 2025-06-24 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 0d0a6df5-e7cb-3f2c-b339-86f6ae6b11e8 | -8.5539 | -51.5358 | 2025-06-24 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3e43b9b6-2105-3f85-af9f-a01358680c0f | -14.16081 | -50.42957 | 2025-06-24 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b10a784-b28c-31b8-a7bd-671bbbc90266 | -14.43377 | -48.91892 | 2025-06-24 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9aaeedc8-d82d-3f8d-ae7f-43b0f99071ee | -14.44011 | -48.91951 | 2025-06-24 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7fa9de21-4e39-3290-a292-ad866b98f8fa | -14.16126 | -50.42543 | 2025-06-24 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3bea5b3-0ae1-3dd9-abea-38fbed6919ae | -20.47947 | -53.67611 | 2025-06-24 05:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a1fa0c4-0d08-3972-98ea-190b1ef72b2d | -14.66489 | -46.94213 | 2025-06-24 05:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af57f58e-3868-3535-9966-a0f9d598b374 | -14.16035 | -50.43372 | 2025-06-24 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5ca776dd-f54d-32fe-b97b-6a2908c3b3d0 | -14.72917 | -48.41253 | 2025-06-24 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ebb4ac7-1e69-3ef8-915d-97743d5ddac6 | -14.15508 | -50.42875 | 2025-06-24 05:21:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbd5a2bc-e890-3b08-96d5-8b3606564fd2 | -14.4343 | -48.9138 | 2025-06-24 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01ae7bfd-ffbd-3dc4-bfbb-8950a9b4e5a7 | -14.44065 | -48.91435 | 2025-06-24 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e02ff6be-f2c5-3cc7-b374-9a186f8c7763 | -20.8124 | -55.73604 | 2025-06-24 05:23:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9a2e3e0-5b54-3f90-ade6-9da244a3faee | -21.43908 | -57.25969 | 2025-06-24 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d897ab86-ed1d-3c23-aedb-ccd519a4b36b | -21.43862 | -57.26336 | 2025-06-24 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 625c568b-69a9-3ddc-81a9-22ac2c92a50b | -8.5537 | -51.5567 | 2025-06-24 05:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| fe9ae256-4fe8-3866-8e82-f2a2e0011f5b | -8.5722 | -51.5761 | 2025-06-24 05:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d205db1a-f19c-3a7b-8347-91b4a9775514 | -8.5724 | -51.5552 | 2025-06-24 05:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 945c0a7e-9b59-346a-b309-d25649d6a3aa | -8.5722 | -51.5761 | 2025-06-24 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 81c04710-9f65-3a90-a7e5-a9512680581e | -8.5724 | -51.5552 | 2025-06-24 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 63e0b9cd-dc0d-3600-b17d-0733ee5c5cfd | -8.5537 | -51.5567 | 2025-06-24 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 4a4a7267-1d91-307d-811f-cedff81c4951 | 2.7503 | -60.3651 | 2025-06-24 05:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf807848-35ff-39e4-a83b-1eac152f608f | 2.75095 | -60.36914 | 2025-06-24 05:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 833ba7ea-f6a1-3631-965c-b132b4c61eb5 | -10.86127 | -53.76842 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d999b30-53ef-3e51-9544-6ee2269f65f9 | -10.86059 | -53.77404 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34f0068d-3e5f-3eff-8ae9-7b33e032d2ee | -10.08181 | -52.74713 | 2025-06-24 05:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a4b65ef1-dc42-355f-bb9d-94352a5e7565 | -10.86537 | -53.76258 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7fa5d6e-92f1-3faa-9f9e-71f61da27625 | -10.07483 | -52.74614 | 2025-06-24 05:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d1a489ad-8fe6-3ca7-9f04-bb886bd725c2 | -10.8587 | -53.76192 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4607c90d-44ef-3ae0-b47a-1c3e76ddac7c | -10.86793 | -53.76911 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab82f1bf-e7bf-3970-b46f-ada9e529a22f | -7.91757 | -61.54699 | 2025-06-24 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c260439-8873-3974-9a4d-160c7623b68d | -10.86472 | -53.76827 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 667c822b-034c-3e8e-a774-16a0100b7f2e | -7.91921 | -61.54924 | 2025-06-24 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22da71fa-8aad-3f80-87a6-8a261c558361 | -10.86656 | -53.78038 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed115bf3-7717-331c-8df0-787ef03dc92a | -10.86195 | -53.76278 | 2025-06-24 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 935c5805-23b5-3eb1-b2f2-7bdfc086476b | -7.94552 | -62.99923 | 2025-06-24 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eadb6b5-916c-37d1-8ab9-a1dc6d0d991a | -8.5722 | -51.5761 | 2025-06-24 05:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 8100865d-1686-35a4-961a-acb9a87c622c | -8.5724 | -51.5552 | 2025-06-24 05:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| cd3b5907-3a5b-3d87-862b-f0b0bc21c267 | -8.5537 | -51.5567 | 2025-06-24 05:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| cece1d2e-72e1-3fcd-883a-7eb4415f854c | -8.5724 | -51.5552 | 2025-06-24 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 72f5f191-d832-3bea-a1ee-0c63f0087dee | -8.5537 | -51.5567 | 2025-06-24 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 62a4bce2-cb7c-37ec-941d-8ea49bfe8208 | -8.5722 | -51.5761 | 2025-06-24 06:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0bb8c9b9-26b1-3aea-a707-508fa9ae1722 | -8.5537 | -51.5567 | 2025-06-24 06:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 9aefeee5-874a-3805-8101-c92039e5289d | -8.5724 | -51.5552 | 2025-06-24 06:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 82d466cf-8edc-3cad-825a-04dba74c3e25 | -8.5724 | -51.5552 | 2025-06-24 06:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| deff4e24-7827-3813-8c4a-752c1f2e8809 | -8.5537 | -51.5567 | 2025-06-24 06:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| a1d61eda-56e3-3fcd-90b5-eac269e009b8 | -8.5537 | -51.5567 | 2025-06-24 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 56836d4a-e103-3dff-9910-c64a053b052f | -8.5722 | -51.5761 | 2025-06-24 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 590667c3-2c34-3e58-b8c0-94b8f61134f7 | -8.5535 | -51.5776 | 2025-06-24 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6b5c6ff8-2266-33d3-ac0f-454ac893fbc0 | -8.5724 | -51.5552 | 2025-06-24 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 4fd7d7c9-74cf-3514-a162-1ca7ed63554c | -8.5726 | -51.5343 | 2025-06-24 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e9b50b04-5e6c-3700-bc6d-c55dd6aae1cb | -8.5535 | -51.5776 | 2025-06-24 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 6c65a807-71cb-3cf0-9716-c30a9596a36b | -8.5724 | -51.5552 | 2025-06-24 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 80846ec1-14a8-3b01-a85c-b08d5b4f1b96 | -8.5722 | -51.5761 | 2025-06-24 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 221eebc1-e9f4-37ad-ada0-bc038c666aae | -8.5537 | -51.5567 | 2025-06-24 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a8e7a458-a782-3ce8-8c4d-c0a090005210 | -8.5535 | -51.5776 | 2025-06-24 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 91f34b1f-4fe7-3a33-befd-f357655c86fc | -8.5537 | -51.5567 | 2025-06-24 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 192.0 |
| ef8a8cfa-6748-3270-999a-4b04b63921e7 | -8.5722 | -51.5761 | 2025-06-24 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3650a6e7-bf01-32f8-9dd4-d7346f57d2ec | -8.5724 | -51.5552 | 2025-06-24 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| b783adc0-96fa-3ba5-9ed2-539b03649221 | -8.5535 | -51.5776 | 2025-06-24 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4bc7ae9e-6091-3836-8fac-8f19ae35a6ad | -8.5537 | -51.5567 | 2025-06-24 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 3599c14c-7320-34b0-8289-ecf7077806a0 | -8.5724 | -51.5552 | 2025-06-24 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 178.8 |
| e590fc50-1d14-3346-ad67-b00b2e58c5e6 | -8.5722 | -51.5761 | 2025-06-24 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c23fabad-743f-34ba-abc0-aa408d3a35cb | -8.5724 | -51.5552 | 2025-06-24 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| d23403ed-196d-3ec8-b04a-783a09a79ca5 | -8.5535 | -51.5776 | 2025-06-24 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| dd3fb995-094a-35e3-8afc-0037a7bb6223 | -8.5537 | -51.5567 | 2025-06-24 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 8fe3e9e7-9961-3140-9421-52381d4e81f5 | -8.5722 | -51.5761 | 2025-06-24 07:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a99bc716-719b-3884-896d-fae59e93cc86 | -8.5537 | -51.5567 | 2025-06-24 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| a6e5157c-c4df-3e94-a3f2-640ffc428e32 | -8.5535 | -51.5776 | 2025-06-24 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a8f25127-6db8-3c3e-bc9d-048257570e2c | -6.5631 | -51.1126 | 2025-06-24 07:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b6feb700-86f2-3ef6-b4de-760fdc4845ed | -8.5722 | -51.5761 | 2025-06-24 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 650ef181-afae-3d36-a3cd-c710dd46bb68 | -8.5724 | -51.5552 | 2025-06-24 07:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| c4f5e211-4ae0-3df4-ae14-b04e603f9c29 | -8.5724 | -51.5552 | 2025-06-24 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 3dc7b014-3bd4-3521-914c-73641061b694 | -8.5535 | -51.5776 | 2025-06-24 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3f96e6fa-ca6b-391f-b6da-d55cb1209358 | -8.5722 | -51.5761 | 2025-06-24 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4e49103a-6d7d-38b3-b86e-297f577ce2ad | -8.5537 | -51.5567 | 2025-06-24 07:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 401a769b-c208-3999-8b26-165e71bfdd24 | -8.5537 | -51.5567 | 2025-06-24 07:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 73e3f03e-e2a4-3d4a-942a-2ab36f219935 | -8.5722 | -51.5761 | 2025-06-24 07:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 764494d6-7310-3c10-b441-5e022ac46556 | -8.5724 | -51.5552 | 2025-06-24 07:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 83ffc542-1ab2-345b-895f-f1b0d35718ee | -8.5724 | -51.5552 | 2025-06-24 07:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 6b1e5292-9128-3542-b472-6f4bc883149c | -8.5537 | -51.5567 | 2025-06-24 07:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5ab62299-9451-3db6-b5eb-f183ee14f230 | -8.5722 | -51.5761 | 2025-06-24 07:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 041115e5-1f30-30d3-a818-15260b8e578b | -8.5537 | -51.5567 | 2025-06-24 08:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 12583714-a4c5-3791-a3fd-83782ee7d401 | -8.5722 | -51.5761 | 2025-06-24 08:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b360902f-31b3-362e-b817-65fe92a4c2e5 | -8.5724 | -51.5552 | 2025-06-24 08:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b02c0f5b-6fd9-37a5-8a10-e64ba749a315 | -8.5537 | -51.5567 | 2025-06-24 08:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b836aec0-62ea-3af9-859f-eed71ef6a0f6 | -8.5724 | -51.5552 | 2025-06-24 08:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 98a5867e-8e94-393c-b732-e1d36765290d | -8.5537 | -51.5567 | 2025-06-24 08:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0ffb5a90-c43e-3b3b-9e8a-737faff1aa14 | -8.5724 | -51.5552 | 2025-06-24 08:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 513c04e4-8cff-3403-a818-d58e7387a8fb | -8.5537 | -51.5567 | 2025-06-24 08:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bb20fdd7-f728-3ce5-940c-ab7a86f6c7b0 | -8.5724 | -51.5552 | 2025-06-24 08:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9a44cf38-0a10-3ead-8e24-db3fcdd8e6d3 | -8.5724 | -51.5552 | 2025-06-24 08:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8b61152e-55d0-3781-b57b-ae3840ec5459 | -8.5537 | -51.5567 | 2025-06-24 08:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c27c6fa6-ee6b-38a2-a771-73922d3fe79a | -8.5724 | -51.5552 | 2025-06-24 08:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c1940a8d-d546-30b8-9771-defd23eb92b6 | -8.5724 | -51.5552 | 2025-06-24 09:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |


[Clique aqui para ver as próximas entradas](README18.md)
