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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4bd1ad4-765d-3d45-9b3e-5574841ed1ce | -7.566 | -61.343 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fb3ea8fa-8cdb-3c8e-bab7-e55f7097720d | -8.1126 | -54.7871 | 2026-09-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 92cf6924-01af-3f72-a1a6-27c9674b20a3 | -7.5475 | -61.3627 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6672bb17-e1c6-3c8e-b02e-37ee38ad0373 | -8.505 | -54.6404 | 2026-09-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 026a655d-4816-36d5-9a36-495512a34b51 | -10.6358 | -50.3943 | 2026-09-04 03:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 445dad10-f735-3f81-82d6-43d76a53319c | -8.4863 | -54.6417 | 2026-09-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 25352391-43c5-3be8-b0a2-6a1d9faad838 | -7.5476 | -61.3437 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| bba2c5a8-13f5-3c99-b9e0-77c0ee0227a1 | -7.5477 | -61.3247 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 1ca5be91-9068-3f76-92d3-098d03c8bd1b | -8.5048 | -54.6606 | 2026-09-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| bed794a5-6c6d-3aa9-a4cb-47b679fdef20 | -6.1543 | -59.944 | 2026-09-04 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 6374c0c6-8086-3cff-9969-b4a43b250f26 | -7.5659 | -61.362 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 5c5c69d5-53df-3a89-a180-79627c3c9a3d | -7.5661 | -61.3239 | 2026-09-04 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a76b7f40-5ec8-3a33-ad4a-e5e3cb01ab89 | -5.565 | -60.1739 | 2026-09-04 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 5ee39294-cf0b-3f17-8860-2f2d9f727437 | -8.4861 | -54.6619 | 2026-09-04 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| dd7714bd-e414-306e-91e8-ba498d734049 | -7.5659 | -61.362 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 1da3cbef-8908-361c-8ef4-aff0810a0374 | -7.566 | -61.343 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 3b2d8a6b-a378-3a20-a37a-62056eeeced6 | -8.1126 | -54.7871 | 2026-09-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 54d35888-6a7f-378b-96ad-4609794ee7c5 | -8.5048 | -54.6606 | 2026-09-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 21d521c7-b42a-33a5-9171-ee5f894380cf | -8.4863 | -54.6417 | 2026-09-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d1eb04f1-f79e-364c-8517-4604d683c541 | -7.5475 | -61.3627 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| a964770e-e8a5-34dc-9b80-f364d9173210 | -7.5661 | -61.3239 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 7f54a1d8-6de2-35b6-bb14-3862dcf74f46 | -7.5476 | -61.3437 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 4e83001e-c22d-3076-8081-51224b0cd6eb | -8.505 | -54.6404 | 2026-09-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| ee47cf2d-4654-38ca-a14c-a837cb11279d | -7.5477 | -61.3247 | 2026-09-04 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 8744ea9d-36e9-3c5e-84ab-fdf5a1d2b204 | -8.4861 | -54.6619 | 2026-09-04 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 55759887-2a36-35f2-ba40-d0d20eb7b95a | -8.505 | -54.6404 | 2026-09-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 47d0dd89-4795-327f-931c-2411aea0131a | -6.6697 | -59.9635 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 2f3c115a-1e90-3c76-a1b6-2501d64bd17b | -6.6696 | -59.9827 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a1810961-87b0-3c6f-beb1-4b16f1c58d53 | -8.4863 | -54.6417 | 2026-09-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0649f180-e5cb-3bc3-9c3c-5db8eb501d3b | -10.6358 | -50.3943 | 2026-09-04 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7fa718ac-edfc-3daa-896f-190fcfba9c7b | -7.5477 | -61.3247 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 10880313-ccaa-33d4-9111-ce90cd4d4887 | -7.5659 | -61.362 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a5f7f20e-6771-326a-ad58-8b6d1210ea49 | -7.5475 | -61.3627 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 32048abd-f005-31f6-a769-d26516249d80 | -6.6881 | -59.982 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 600b23c0-e5b7-3f2a-a925-cee98a8dc765 | -6.688 | -60.0012 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 9048af00-dc32-375d-b853-f295a586c528 | -7.5476 | -61.3437 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 549f0d09-01f0-3d8f-a277-429adc90c965 | -7.566 | -61.343 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 6b29258a-1a85-3eeb-84f0-ce1c9e024e05 | -7.5661 | -61.3239 | 2026-09-04 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 1f65077d-5a59-3ead-afbb-fb968bfa9026 | -8.5048 | -54.6606 | 2026-09-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| b277f740-9b3f-38a3-8e4d-c03424ee009a | -6.7065 | -59.9813 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 2fbfcda1-4429-3627-b659-18e3dda3ba06 | -8.4861 | -54.6619 | 2026-09-04 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 78c14b83-9185-38d9-88ab-29d07e3d0b41 | -6.6882 | -59.9628 | 2026-09-04 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 3fb2d1ab-dffb-30cc-a4bc-42149ff170fb | -7.566 | -61.343 | 2026-09-04 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 587ec125-ac22-344d-87f2-34d1a88f75d6 | -8.505 | -54.6404 | 2026-09-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 816919a2-1ebe-3158-a405-e5f4d5fc2df2 | -8.4861 | -54.6619 | 2026-09-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 826a3074-171a-3ec1-985b-5d137d72c911 | -7.5475 | -61.3627 | 2026-09-04 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 08c0844b-0f44-3500-86d2-84446fd37ae0 | -8.5048 | -54.6606 | 2026-09-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| f63d1d4a-9a62-3401-9ab0-8fcabbba3869 | -8.1126 | -54.7871 | 2026-09-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c1b1e208-d216-3d7d-a417-024661d93f61 | -7.5659 | -61.362 | 2026-09-04 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| fc152af0-930c-3b82-b341-3e6bfd0a72e7 | -6.6882 | -59.9628 | 2026-09-04 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 310213cf-20e3-3307-a3d4-192d3bb75a63 | -10.6361 | -50.373 | 2026-09-04 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 137e3a2a-dcf6-3c80-b2c9-11da40b0abe5 | -6.6696 | -59.9827 | 2026-09-04 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a3af29b5-6b38-354f-8f9c-dd61e8f17db2 | -10.6358 | -50.3943 | 2026-09-04 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 92bb700f-5bbd-3618-92ef-744200c6446b | -14.1169 | -58.8793 | 2026-09-04 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 7b8d7fce-5472-317a-b027-21b55bfc36f8 | -7.5476 | -61.3437 | 2026-09-04 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e6aa5d51-5d16-39da-ad2c-34edc40aa96f | -6.6881 | -59.982 | 2026-09-04 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ebd64f30-a87a-36e1-b6b7-f2877d0dc61c | -14.1361 | -58.8776 | 2026-09-04 03:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e367cb24-4c12-3ce7-a98c-51036d7a5e33 | -8.4861 | -54.6619 | 2026-09-04 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3170d050-a01c-3824-a1d4-fc8ca36722a8 | -7.5476 | -61.3437 | 2026-09-04 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 04e0d2de-0fc9-335a-a486-b642c412f7dd | -8.5048 | -54.6606 | 2026-09-04 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| f8a7f80d-0ed6-33d1-9aee-0f3be9cfc0ce | -14.1169 | -58.8793 | 2026-09-04 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e13480fd-51f9-35d2-b79b-9a814546ef9f | -8.505 | -54.6404 | 2026-09-04 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6624e6ea-2a72-3088-b3dd-ba68d63282fd | -15.7352 | -47.7775 | 2026-09-04 03:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 30296cac-ef99-3c6e-b62a-aa769a52c90a | -7.566 | -61.343 | 2026-09-04 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| ea559aac-4309-332e-a2fd-f6e003cc0374 | -6.6882 | -59.9628 | 2026-09-04 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 9aa9d4fb-cc7e-3b48-96cd-45b9bd72ed15 | -14.1361 | -58.8776 | 2026-09-04 03:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7b453445-8154-36a8-b034-d6efdfd2daf8 | -7.5475 | -61.3627 | 2026-09-04 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 026180ae-c28a-36f0-844c-f8345b83538e | -6.6881 | -59.982 | 2026-09-04 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 74b2f00a-d755-32e0-b982-e19bfb6936fb | -3.24651 | -47.25595 | 2026-09-04 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f04c8c4-8640-333a-a87a-7fe27df83c4a | -6.09975 | -44.14771 | 2026-09-04 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ffb3b89-e103-36d1-8074-3a476201d8d2 | -6.09506 | -44.14379 | 2026-09-04 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaeb12d7-cced-3c73-943a-8f711314d362 | -4.9041 | -43.47402 | 2026-09-04 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28609641-6663-3b59-ac18-1dc1b8cf6ef5 | -4.36528 | -47.77467 | 2026-09-04 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 132530f4-e1b5-34c9-8c70-c0b590d7ce04 | -0.92892 | -47.19752 | 2026-09-04 03:42:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44b3bdd6-f82d-3b9b-925f-8cda2f1da680 | -5.55077 | -43.43002 | 2026-09-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 868e52f1-e5e8-3d86-b1b5-f3fd7a49fe95 | -5.55001 | -43.43146 | 2026-09-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1ecfcb7-90a1-3823-868f-12922f6024f3 | -6.32849 | -43.81918 | 2026-09-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee196a61-93b6-3cbf-9fb8-f1865765ac18 | -6.64979 | -39.11566 | 2026-09-04 03:42:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a7acac2d-81cd-36e3-963d-1bcd964bfbca | -4.29666 | -38.52983 | 2026-09-04 03:42:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54d2a3e8-c235-3823-a748-3dd18e411225 | -3.33651 | -39.77565 | 2026-09-04 03:42:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96f50743-8155-3829-a03d-cb2310a49ccb | -4.45298 | -40.20449 | 2026-09-04 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39c07790-cea2-3211-a7e7-75c25a36fe58 | -3.42714 | -43.20366 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a229fa2f-0ec4-353d-a64c-73ab3c157fea | -5.54653 | -45.20184 | 2026-09-04 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12f089a7-6ed2-3887-a4b0-c8550b817a9d | -6.328 | -43.82203 | 2026-09-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d672904c-95b6-31d7-b598-fcdbd1b2d4fb | -5.80472 | -43.62971 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c09a1a80-00d3-31de-ba42-5e826071e940 | -2.89651 | -39.96492 | 2026-09-04 03:42:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24e68769-fd7d-3689-ab74-65809eaf0d48 | -3.33708 | -39.77205 | 2026-09-04 03:42:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35299819-bbb8-31af-b019-47757e23c606 | -4.29542 | -38.52783 | 2026-09-04 03:42:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d58ddeba-4fb0-3557-b12a-59588e7a3110 | -3.33709 | -39.77311 | 2026-09-04 03:42:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a4a12f7e-e6b5-3825-9f45-b29ce8e1df1f | -5.10462 | -40.60834 | 2026-09-04 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da52b5aa-6b1d-3945-b5f1-6f59bbbdb22d | -5.10879 | -40.60906 | 2026-09-04 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| be13cc36-b5d0-3d0d-a39a-32a46f0a8888 | -5.80221 | -43.64445 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5baa1989-9071-357e-a284-e2ea46eca34c | -6.32896 | -43.81641 | 2026-09-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64de1785-7dbb-37a1-88f1-dc9bbf267a09 | -5.55126 | -43.42707 | 2026-09-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a818c3ad-16ea-39e9-b04e-2567a0aeddb3 | -3.43175 | -43.20748 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 232f9be5-80b3-3e19-a62f-d5a0ef230a8d | -4.03241 | -38.23197 | 2026-09-04 03:42:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 276438b0-cbfc-354e-8de4-18c18f12f7b0 | -3.45001 | -39.63845 | 2026-09-04 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d386f2b-a795-3899-9ed1-1c6119f6795b | -4.49632 | -42.55655 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4f11ad3-b9f1-32c4-aa97-da251ce1fd66 | -4.36426 | -47.78062 | 2026-09-04 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4963ba3b-7cef-33a9-94cc-7ef93e05daf9 | -3.93642 | -42.9924 | 2026-09-04 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README9.md)
