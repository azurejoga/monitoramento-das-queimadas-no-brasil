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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f15050b4-b769-3e84-a91c-4bbb312186a9 | -3.59271 | -53.78188 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f72aa3f8-a245-3ed6-9a46-4f9660fb638e | -3.59165 | -54.56691 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41d2782a-df53-33be-8c7b-fd921f849cad | -3.58941 | -53.78137 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0a2238b6-571f-3b06-9422-f190309e07d3 | -3.58887 | -54.56289 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aaaa493-b7b4-395e-ba17-67b65f6c5d84 | -3.58831 | -54.5664 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69e3a247-c346-3243-aa45-6d0d2cc70664 | -3.58712 | -54.65985 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac60cc09-d422-366a-a882-250b83b1bbd5 | -3.58656 | -54.66337 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fc9382-322c-31a7-81ba-a6a1b07504ed | -3.58322 | -54.66284 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d9ba7ff-7f69-3304-af05-2ebdf960b1a1 | -3.5704 | -54.67889 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28662ed-0f93-32b6-b33f-8f7ab365d1da | -3.56874 | -54.66781 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ae3280-fb20-368b-aeb7-9b2ca769a232 | -3.56818 | -54.67133 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2f8523-f4cb-3c1b-9b9f-f3d8cde3ae2d | -3.56762 | -54.67485 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0211e58f-2024-32c0-89e7-21658afeaa0a | -3.56706 | -54.67837 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0febe5db-22ce-3364-98f2-465bc6cebbe8 | -3.5654 | -54.66729 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6139ab46-18c8-3f42-a7e0-b039beecfeed | -3.56484 | -54.67081 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe37b7f7-cd64-3436-baac-6f909fb59857 | -3.55591 | -53.99466 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50968ca8-451a-3f3c-8328-5b6d56c9c1a2 | -3.54766 | -54.76168 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3131d19f-09a0-3f33-a780-353226ca2ee6 | -3.54765 | -54.73992 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1905d941-c46b-3e19-9bc9-243986a8495d | -3.54432 | -54.76114 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34213f58-40e1-3d63-9f5b-73c9ff6f7cc0 | -3.54431 | -54.73939 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650544ea-4c89-3261-b655-35d8ebc280fe | -3.54376 | -54.76467 | 2024-10-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f73891-ca6a-3b33-a6b3-aeab9514895a | -2.22092 | -54.84734 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a41259-68c5-3661-b0d8-bfa9cb332243 | -2.22035 | -54.85096 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b9b5136-c532-3be2-98ed-b8a3bb2a085b | -2.82466 | -53.90768 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9c6dd45-b585-3f1f-922a-752625cfeef7 | -2.8132 | -53.95884 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c7af5e3-422a-3271-b882-e1b31fd3dd72 | -2.81284 | -54.08988 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e771acfc-a30c-34c0-a8ae-b471ebf61baa | -2.81065 | -54.10375 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68a65435-14b4-3adc-8564-b47ff4495127 | -2.80733 | -54.10323 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e7e81d9-148a-3828-825e-9be3c024e47a | -2.80566 | -54.09232 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d75c80-421f-324f-8025-e8a3062fff41 | -2.80401 | -54.10273 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6abb9ae-d783-36a7-82d6-a73ca2293e1c | -2.8018 | -54.09527 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 787f51bc-f7ad-3de9-ba75-7570df1e9bb4 | -2.80162 | -53.94302 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eaaffec-8e3b-34dc-88ee-5b02995457cc | -2.79246 | -54.15427 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2164875d-96ec-3a0c-b826-88340ec9f6a1 | -2.79191 | -54.15775 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb9d6cf-6a07-3995-8a9c-371599246ffc | -2.78422 | -54.03228 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 317a3c0f-78c2-34c7-b7f0-19f9aaccb68a | -2.77852 | -53.96061 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b70bbc7-ef02-3d25-b96d-7d87a5a9570d | -2.77575 | -53.95667 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e1155c1-e7a4-3dcf-8eda-95996e79cb23 | -2.76988 | -54.03716 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f281b1-bf27-3ce1-ad41-1e1f06ab4093 | -2.76657 | -54.03664 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ce1d88c-7136-3f73-b5af-bb184ea43c5c | -2.76325 | -54.03613 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e148bfd-d491-3859-acce-97ea82245db0 | -2.75994 | -54.03561 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5479a757-c089-358a-bfd5-f10459511a5c | -2.75663 | -54.0351 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29e5ca28-07e4-3fd4-b755-04f933fa3145 | -2.75 | -54.03407 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 997abfd1-f07f-3ee9-a51d-7b02f11de514 | -2.74946 | -54.03753 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c0855ce-1eb8-33de-a6ff-6649f707a7ba | -2.73967 | -54.12124 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54f5babb-6649-3c71-937a-cbc11ec8e5e0 | -2.64459 | -54.29201 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 41d71abf-105b-3e86-bea4-de396befc075 | -2.64403 | -54.29551 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 05db7955-007d-31db-b2d4-f5b2a8215725 | -2.64107 | -54.29436 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f1cfc9f-c458-34f9-997f-6420e4180bb8 | -2.63665 | -54.30084 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 075ad91a-914c-3e7b-95a4-427264300399 | -2.6361 | -54.30434 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a330e2d-1e4c-3591-9f9c-7db9da539369 | -2.62122 | -54.00983 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22124ffa-7181-3575-a089-b027f6f2847d | -2.61791 | -54.00931 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7c5948b-87c1-3a1d-9a14-4f08b40435cd | -2.61183 | -54.00481 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ae286f9-d500-362e-8543-40e5741f43dc | -2.56904 | -54.01574 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9078a3f-6a8e-3638-85f2-263cfb9d79c1 | -2.5685 | -54.01921 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e9778a10-335c-34fc-bb24-dcabf11a3beb | -2.56832 | -54.17241 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49bf4090-45c2-3778-a4dd-0c3a2c5cbc48 | -2.56795 | -54.02267 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17f5c6cc-56d8-3285-88e0-c1711ffb0fa6 | -2.56741 | -54.02614 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a797bcb-3767-36ac-b671-01f9fd9d52ea | -2.56573 | -54.01523 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faecf594-fad1-35a0-9bc1-ce43c58338d5 | -2.56518 | -54.01869 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bd60430-3ed3-35cc-a564-523faa05d0ff | -2.56464 | -54.02216 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc477d0e-0b57-3ae4-883d-3ffd13deb0c5 | -2.5635 | -54.00778 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b98d7b0-6b00-3aa0-9661-d92b977dd962 | -2.56296 | -54.01125 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d3e1d69-0f10-3c3e-bd4f-5fe871f85ee0 | -2.56241 | -54.01471 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90556049-a560-3917-9f48-1f677f748dc1 | -2.56187 | -54.01818 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3036ea47-a0c5-36d1-91b3-24e4b370ac91 | -2.56132 | -54.02164 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ae416b8-0752-3aa7-ac63-dafbfebfc79c | -2.55964 | -54.01073 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d255bc9-4faa-3f38-b6e8-45c7db7be002 | -2.5591 | -54.01419 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b4b04c5-eafe-3ae3-81fa-44106897b5f2 | -2.55855 | -54.01767 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bebc2e36-4e99-3140-be4b-dd19a4207ea4 | -2.55801 | -54.02113 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06c42075-5cdc-3c0a-b534-7103cee9921b | -2.54416 | -54.00124 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efaa51d-af27-3f67-b68f-8012f5f2350c | -2.54085 | -54.00075 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 843b36b4-f915-34da-a5c6-442cc1cd96c6 | -2.94237 | -53.87309 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e204b10-7028-3c18-92b6-56f1977f80ce | -2.93707 | -54.35902 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a7b4f2-fd4f-378a-a456-a589409befbf | -2.93374 | -54.3585 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69fef125-7624-3a32-b039-370d72e689b9 | -2.93177 | -54.11205 | 2024-10-28 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5a65ef0-6b1f-3a95-832d-308612970203 | -2.88892 | -54.89637 | 2024-10-28 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce5a33c-0e89-30a6-8b7a-5e4cb66d817e | -2.87662 | -53.96511 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a818fad-6fda-3b66-9654-9ee9a3741267 | -2.87331 | -53.9646 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ba8bf56-1330-3f52-bf3f-9dfbfd806766 | -3.16753 | -53.91247 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b99252-14ff-36de-8609-874414938f86 | -3.16698 | -53.91592 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef2dfd5c-1231-307a-a071-52a362c75ea3 | -3.16644 | -53.91936 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42d88d09-64c9-3338-bec7-005784f39230 | -3.16422 | -53.91196 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f07e595f-3a6e-3f36-8020-a38a55526c90 | -3.16368 | -53.91541 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27e9a7a3-62a4-3755-8514-74392cceac0f | -3.16313 | -53.91885 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e93b252e-2ff0-3442-b0aa-a08438c8239d | -3.16091 | -53.91145 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e345460-6c8a-348a-b4bb-b3f972cdd9e7 | -3.16037 | -53.9149 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89ead422-e189-3991-838d-8d44189ccd35 | -3.15982 | -53.91834 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ddd2cd0-d671-3b5c-a159-2cdcd2beefae | -3.1588 | -54.9602 | 2024-10-28 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd3062df-f261-39ae-b0fb-3adc3e547ad4 | -3.15761 | -53.91094 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92a520e1-aae1-3d53-87c5-f8812d54282b | -3.15706 | -53.91439 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90e4b304-6eda-335c-a5cd-6f8d58c84248 | -3.15652 | -53.91784 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5c97bcf-2298-3e22-8d3b-67d3f23a3e56 | -3.1543 | -53.91043 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56405c24-9d7f-33a0-a236-0802771c401a | -3.15376 | -53.91388 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f7e59db2-056c-39e7-a91d-cde526f1e13f | -3.13945 | -54.28389 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 304b407a-59d5-3043-8905-7b213d4782a4 | -3.13891 | -54.28737 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f0cded-7b8f-340c-9da4-0859a06f8aa1 | -3.13835 | -54.29086 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8a5082b-e99d-3858-89be-5b8ea8209f99 | -3.13501 | -54.26896 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a54aedf-6c51-39be-95dd-17736efb4b01 | -3.09559 | -53.72137 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bd54c6b-4bc9-330c-95ad-394bda69eddd | -3.13446 | -54.27243 | 2024-10-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
