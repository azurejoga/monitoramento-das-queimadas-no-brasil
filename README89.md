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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4058b253-cb3f-3a48-9403-e3e8040be367 | -2.68055 | -54.25255 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87583665-9513-3721-a6c8-fa9a82a60281 | -1.36242 | -54.65287 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cd8ef0d-8777-35c7-aa4b-cffc91d3a563 | -2.90687 | -54.18258 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab8b973-0e99-3cc1-8c22-912487b187c9 | -12.08286 | -60.67934 | 2024-11-29 05:22:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8122dc37-7034-32d5-8158-86235d806f6b | -3.41654 | -50.16717 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39b5db31-81cb-3e91-b5e3-c7fc213b661f | -3.18081 | -50.28351 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd3fd508-be0f-3dfa-8ad9-77944e2f5116 | -2.43443 | -53.8929 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27199fad-535c-3110-b07a-b75fc64f0692 | -2.21097 | -52.47926 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd3d8a85-4673-3f5b-ba81-d6565ed67fcd | -3.10568 | -54.03753 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 203117d0-b501-30bc-8489-47077bf4e425 | -3.46475 | -50.52614 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0bc1b86-da57-3993-b4cc-51d3170b0f86 | -3.90451 | -51.04466 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b953111-5712-3900-b07e-0ba53d6d8f80 | -1.69303 | -52.43575 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2398f6f1-4b75-3fd7-9ecb-e3887c1014fd | -3.2213 | -54.06872 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93f45e96-abcf-3cb7-9800-dd7dc7e5192e | -3.4632 | -50.53645 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5626ddcb-5673-3877-9a17-4a0cdef8c803 | -3.74496 | -50.7914 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2397be59-21b2-36a5-881d-4fca8c8edb3a | -1.69224 | -52.45214 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d8624aa-82ab-37ff-9c8d-6edc1c572d9a | -3.04307 | -50.97999 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a8aa92-190a-3ec6-a43e-fd5bfa2dbcfa | -2.0294 | -53.50157 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05eec662-c476-38b7-9334-d8ac605f6c6d | -2.36512 | -55.70993 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d07c745-ae98-3f90-8f1b-1ecf2fe358de | -3.25277 | -50.40522 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caf7dc93-4511-3107-95bf-f628bb3d6bb2 | -3.32978 | -50.22362 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04723c0-9289-3b68-bfe1-efaeb4f3cfa9 | -1.98953 | -53.29712 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f81d60e3-f013-38e9-a835-3096ef5d1fd1 | -3.24662 | -53.6367 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dfc8b9f-b04b-362a-bd8a-910c2f7b38d7 | -3.54947 | -51.61063 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51a8e27f-f0c2-3181-8fba-fa0037f2fb32 | -2.8576 | -53.99826 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b50e9c19-aa0a-305f-85d8-778ef6ece458 | -1.89439 | -53.01247 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bc39ddd-87b1-3bda-8e52-9e746df45cd0 | -3.03079 | -54.01934 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60b079df-0db0-32f5-b43a-97db232b82ad | -2.66458 | -48.7821 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8646b2e3-1a94-379c-8b93-22212a0994d9 | -3.22493 | -54.07338 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b931dd7b-dfb7-3e69-8241-bf09d98de4bb | -3.19008 | -54.3302 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b172023-3833-3c51-8873-707bd8902a20 | -3.2221 | -54.17671 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71fcf282-c0c6-366b-9585-6700dac175af | -2.46182 | -55.27869 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d785d35a-3d7d-3880-8f40-18d0260f0bd8 | -1.9918 | -54.9011 | 2024-11-29 05:22:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2e4b6d6-0877-33fe-9a8f-7acce10e3142 | -4.48223 | -48.19073 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 487f26ac-55da-3e45-aeef-83c6dfe32036 | -1.52737 | -54.22385 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51c00494-daf7-3c8b-bdb9-f83107cf9a04 | -3.17036 | -48.43681 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6f86c3-8cdc-30b5-85fc-dfa1358b8ef6 | -1.91427 | -52.8843 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fe12503-2fdc-3cad-97c3-b6ee26b2c3f3 | -3.06901 | -53.91249 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a99b063-5db1-3f91-a95d-12e53d119fdf | -2.61258 | -51.80772 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 464ce1f0-ad40-3fc1-8b9c-e3483f41c9d8 | -2.45858 | -53.68246 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1a090de-e4cb-3302-8e77-955ac2e08323 | -2.73257 | -54.14041 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9855960e-b255-3474-8cbf-34766571bd70 | -1.67826 | -55.17062 | 2024-11-29 05:22:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab097561-186f-3beb-9b27-b9e7c5f099eb | -2.79974 | -54.03709 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a41fc4e4-84c0-3624-b458-7e5deace40cf | -3.02655 | -54.01871 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26dd7257-cf49-3bab-9057-cc824dc8ae06 | -2.75177 | -60.23359 | 2024-11-29 05:22:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0179b7-b98d-3cd9-b961-2276dd77b469 | -3.41809 | -50.16264 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de720c79-8d4c-31ee-b056-3cfd0aa3f09f | -2.88343 | -53.30982 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5676be-c1c9-3d3d-9898-159d92a718da | -3.07392 | -50.98803 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80ae2ade-7c8d-34e0-8b9b-f8947d927286 | -3.89578 | -49.82098 | 2024-11-29 05:22:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70a1be24-14d3-3106-9ea3-86a18331b1b1 | -1.71356 | -52.7619 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e28c3009-b168-334a-852c-678214c899c1 | -2.80402 | -54.06534 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42598313-72a1-3223-8e3a-6ef57394e39d | -2.69241 | -51.98478 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95c93cb8-095c-3fc7-8725-e4d6cac29e65 | -1.44421 | -55.16024 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7f13f5a-8044-3fb6-98a9-e34cdb6a28ad | -1.69089 | -52.45004 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7c5830db-59ea-39d1-9bdf-b77fa51ac43a | -3.4707 | -50.5235 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d05cab-d4c0-3a37-a366-0b4943aaa270 | -3.79246 | -51.25975 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f957493-7bf8-33f0-bfd7-266ba8a62f4c | -2.94147 | -51.58852 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef2ddf30-fe1c-326f-9e18-835959a6ce1d | -1.89606 | -54.54714 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e187b4b9-6708-3eba-a366-4c0ebb6144ea | -2.99647 | -53.72405 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b25b10d0-5d65-36d1-9d96-261d9f98382f | -2.78699 | -53.20819 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5733e10-f395-33bf-aa7e-d87707cacec7 | -3.6724 | -54.44989 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c65e26a-6d1f-3ad3-b5ba-1bc8699021ff | -2.83767 | -49.84564 | 2024-11-29 05:22:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 955f995b-959a-33d8-b016-2bf61565e55b | -3.24942 | -50.77423 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d20176c-74eb-3762-98d8-eaa9776506b7 | -3.1179 | -53.27083 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eceb9907-489a-3093-9e02-bd0ebf5bf3f8 | -2.59947 | -54.07865 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab5f895e-5d68-34de-935b-14c9c4fdd604 | -3.01452 | -54.04079 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eac11f7-ff70-34b0-a622-874334992306 | -2.83801 | -46.80154 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8504a26c-2ab4-33ea-908a-21131ba5a324 | -2.98399 | -53.29734 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| eb73d4f1-5291-371e-847a-135296af6eaf | -2.62042 | -54.20102 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d195d694-d2d1-3f9a-a80b-2348cf1bd7c4 | -1.42123 | -55.25734 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26a04de8-25ce-3410-9a23-aeb96c9aa275 | -3.53204 | -50.19215 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa6af76a-d159-31e3-b064-377c40dd78e1 | -2.88639 | -54.00666 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd21d12c-5654-31ac-a01d-860628cc3264 | -3.70306 | -50.51325 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7371355a-53ed-367a-859d-1ee8da92ddfc | -2.69564 | -51.99612 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3aee85d-da13-3fbd-88f8-e1f493fa8510 | -3.05741 | -54.04327 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d86091f9-ee14-3517-be03-f5b60bf5cd1d | -2.52277 | -54.13272 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24fc42b-d81d-3127-a17a-d20510561069 | -4.58881 | -49.56529 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d996e557-7338-3419-b489-b3c7f5ed9645 | -3.25097 | -53.63742 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 63f83d4a-7310-393a-8b6d-491d4841852a | -4.15655 | -54.81122 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9f34eb6-ae86-31d0-ae58-7980a1ac9aad | -2.88698 | -54.00276 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4500a1a0-e596-32ce-a369-e4770db032cd | -1.68345 | -52.53108 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c93b22bc-0539-38ff-b2ac-6f0c7074b265 | -2.36136 | -55.70932 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a965d15-30d0-389f-80e2-631059c92e5d | -2.82563 | -54.03702 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2e95617-65a0-36ea-865a-64c4a7c0f143 | -3.30171 | -50.75179 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41e00ae8-d27c-37a2-8de2-83e08425d8b2 | -2.83594 | -54.11337 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f983f509-886e-3c59-abf3-be8a6a5496c2 | -3.10119 | -53.81824 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0df37f57-6a3e-3b5e-95b8-c02aa7a1ae73 | -3.4114 | -50.16935 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f95e76b1-d8fe-3af4-bf02-ec8246ba1086 | -2.90327 | -54.17815 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 463ed253-0606-337f-bcb5-d9150407aadc | -8.28136 | -48.03096 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d79dc632-2758-350f-8682-c251404ca620 | -2.65578 | -48.7906 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| bdb6caba-1c4a-3aa3-81dd-fa999fcbed1e | -3.09586 | -54.13095 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24a59f93-cc71-395e-8595-cd994bf5662b | -2.60217 | -53.97755 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265fdd9f-3f5e-3bc5-9804-62b2a1d6bf86 | -3.10181 | -53.81424 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b2f9e2b-b34f-372f-a23b-47976e7a33fd | -2.58951 | -53.97563 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3121592-66c2-3bd5-87af-6174c6341f0d | -1.58839 | -53.8433 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 04da8adc-4f41-3ad1-8ce5-512da44f2b7c | -1.7197 | -52.63186 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c7205b1-cade-370c-8d1e-56d629f0c781 | -3.26825 | -49.89584 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6878826f-518c-3cf8-b71a-5ba8f8e6d3c2 | -1.71738 | -52.76712 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3446a3ab-26fd-315a-94f7-b0d1a7d47c2c | -2.57997 | -51.92355 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12a79eee-597b-3701-8b43-fe252ebb3a41 | -3.6883 | -50.23229 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README90.md)
