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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bff3c7a7-e29a-37a4-bf7f-c776da652f19 | -6.94421 | -63.10339 | 2025-10-04 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e52bdfbd-dd86-3f11-90b2-7df660eab73d | -7.2986 | -55.3219 | 2025-10-04 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b19be836-ae52-372d-859d-3bcb9d9fd8c6 | -6.86952 | -63.13446 | 2025-10-04 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fd400ff-90f9-350b-8c6d-29e87498bbaf | -21.6888 | -50.0559 | 2025-10-04 07:00:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| dd90a56c-c2f9-3976-85cf-3a287a550bb5 | -9.71183 | -67.46297 | 2025-10-04 07:14:00 | AQUA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 73807951-ae4b-350d-8d6b-ae93ac8649ba | -21.6888 | -50.0559 | 2025-10-04 07:40:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| c9481e9b-289f-3385-adf1-a860f8aca7a1 | -13.9387 | -48.1629 | 2025-10-04 07:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6d50f433-4e7f-3700-8ed6-6245577ac028 | -13.9383 | -48.1852 | 2025-10-04 07:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 8300a349-debf-3ffa-b4e6-a7ceab72eabc | -13.9383 | -48.1852 | 2025-10-04 08:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 88614ac7-4644-37c1-a9f7-32151d75c013 | -13.1585 | -50.9359 | 2025-10-04 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5dae243a-868a-3603-ad67-9722e5643376 | -13.1777 | -50.9335 | 2025-10-04 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 351.2 |
| 8971de8b-29ea-39fe-8fa3-90e7bbb328fc | -13.1774 | -50.9549 | 2025-10-04 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 8f8ac660-804c-38b6-9c9b-b5bba717a29b | -13.1333 | -47.949 | 2025-10-04 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e7adb6f1-cd8f-3d43-99b1-2af59f785e76 | -13.1582 | -50.9574 | 2025-10-04 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 749ed92f-cee4-366a-8c2e-3cf1d1c14aab | -13.1774 | -50.9549 | 2025-10-04 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 3f8a5076-6b6f-3291-880b-7d28e7a03725 | -13.1777 | -50.9335 | 2025-10-04 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 269bad62-73c4-3db3-a0f2-29d11d6bd96a | -13.1585 | -50.9359 | 2025-10-04 08:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 94747205-8d69-33a8-9702-fa8c694d3d26 | -13.1585 | -50.9359 | 2025-10-04 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 070358c8-709a-3387-867c-e4a60934f3fd | -13.1774 | -50.9549 | 2025-10-04 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 2405cde3-f0ce-3096-8eb9-91983ffc7e49 | -13.1777 | -50.9335 | 2025-10-04 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 5b4415e7-92fd-3e27-912e-ebae49613749 | -13.1582 | -50.9574 | 2025-10-04 08:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 42765220-1993-3ffd-92a0-731e75b16b38 | -13.1777 | -50.9335 | 2025-10-04 09:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 66f92242-8bf3-3588-8aed-8e3a96bf55f7 | -13.1774 | -50.9549 | 2025-10-04 09:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 260.8 |
| ddd41977-0025-3283-a51b-921d5fe3cb78 | -13.1333 | -47.949 | 2025-10-04 09:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| bd28b001-ae69-353a-bde8-d7b6f6e88fca | -13.1774 | -50.9549 | 2025-10-04 09:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 1e191f95-c5e2-3de9-9441-3ec3fd5a4794 | -18.0809 | -49.5982 | 2025-10-04 09:20:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 174.6 |
| ec070319-61b0-3851-a663-80e9625b42a4 | -18.0609 | -49.602 | 2025-10-04 09:40:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 267.7 |
| 209a68ef-e6e3-30c4-b290-5b1ccbc8f8b5 | -13.1774 | -50.9549 | 2025-10-04 09:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 0ac15dd6-39b1-3811-8cad-ea65e54b76d8 | -18.0804 | -49.6207 | 2025-10-04 09:40:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 210d914b-e19f-3bba-a870-49e950c8931a | -18.0809 | -49.5982 | 2025-10-04 09:40:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 491.4 |
| 6315a471-3cbb-30cf-9e5c-f34f6fee4533 | -13.1582 | -50.9574 | 2025-10-04 09:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 5bced602-7546-3885-9436-4c71273f5fa4 | -13.1582 | -50.9574 | 2025-10-04 09:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 00fd60ad-c807-359e-be0e-c23925d233b8 | -13.1774 | -50.9549 | 2025-10-04 09:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 340.0 |
| c2e6476a-924d-3f3d-86b9-088d379e6be2 | -13.1578 | -50.9788 | 2025-10-04 09:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2b79bffb-c1d3-37a4-81fc-41376f73bb5c | -12.535 | -45.9864 | 2025-10-04 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 00e598fe-83df-3d61-b145-6fb32e71fc5a | -13.177 | -50.9764 | 2025-10-04 09:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| c61b60b5-1057-3d0c-91c3-8a38548ee48f | -12.535 | -45.9864 | 2025-10-04 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 5f77cc75-5668-3c9d-9189-611b6ece35f2 | -13.1582 | -50.9574 | 2025-10-04 10:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 92a56277-3826-36f7-b53d-c8d160686f10 | -12.5355 | -45.9635 | 2025-10-04 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ce48270c-3fe3-38a8-8904-218e97daaca5 | -13.177 | -50.9764 | 2025-10-04 10:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| eed54831-1f79-3f48-9e07-f04090e52986 | -13.1774 | -50.9549 | 2025-10-04 10:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 249.4 |
| f94e7104-295e-3062-a0cd-54c56983b673 | -13.1333 | -47.949 | 2025-10-04 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 450b18f2-c483-3d7d-8b37-b209d1157a52 | -13.1333 | -47.949 | 2025-10-04 10:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 11d0dbe7-c82c-35ed-80e5-d59001f60500 | -13.1774 | -50.9549 | 2025-10-04 10:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 5e3877a0-1c76-3a7c-845d-64b96efaa149 | -12.535 | -45.9864 | 2025-10-04 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4327da16-6d0d-36aa-8f03-294e6f89f15f | -12.535 | -45.9864 | 2025-10-04 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ae9eb9b1-9993-3c43-94f3-95f67f3f7303 | -13.177 | -50.9764 | 2025-10-04 10:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| afaf71ed-83b6-3af8-8f15-e37462909ad0 | -13.1333 | -47.949 | 2025-10-04 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 933c3eda-047f-3fdb-930b-363901a62614 | -13.1774 | -50.9549 | 2025-10-04 10:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8696f178-5964-32da-a190-16e5358a49e6 | -13.177 | -50.9764 | 2025-10-04 10:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 227.5 |
| b9e716ce-8682-3162-8c27-4d6aa8124a3d | -14.2131 | -46.0596 | 2025-10-04 10:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 24e24d3f-96d1-3bb8-8d53-b96942956a33 | -13.1774 | -50.9549 | 2025-10-04 10:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 374.0 |
| fb601f65-fd48-3a86-85ae-42b8391455f4 | -13.1578 | -50.9788 | 2025-10-04 10:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e36a0a40-50f5-3bcf-a186-ff04115c4179 | -13.1966 | -50.9525 | 2025-10-04 10:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 6828ffb9-90b4-35e0-a09b-6ce55ed22d44 | -13.1582 | -50.9574 | 2025-10-04 10:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 8d0848a8-fee8-3f1a-80e8-d6dba96fa1a2 | -17.9763 | -49.8187 | 2025-10-04 10:40:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 141.8 |
| d26ed048-1baf-394d-9b6e-5fe64da2d25b | -13.1774 | -50.9549 | 2025-10-04 10:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 3b778ef8-b9ed-3ea9-9070-f07bad8bf413 | -17.9768 | -49.7963 | 2025-10-04 10:40:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 134.4 |
| a7d6d0e2-1d86-3035-bdff-4744081c88b8 | -13.114 | -47.9518 | 2025-10-04 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 2dc06643-0137-33f8-abc3-81bebaa14af1 | -13.1578 | -50.9788 | 2025-10-04 10:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| cecd837e-f21c-35c8-9f85-2ea58eaf2d47 | -12.535 | -45.9864 | 2025-10-04 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 390a7fa2-d92e-33d7-a84a-ed05c469f73d | -13.1582 | -50.9574 | 2025-10-04 10:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 78556314-5433-366c-8a80-b1be817d04fe | -14.2131 | -46.0596 | 2025-10-04 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 31f43de1-195c-35d1-b1b7-dbdbe36b08fa | -13.177 | -50.9764 | 2025-10-04 10:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 7a5d5c0d-6438-3529-b5fd-7eba021858a6 | -12.031 | -45.2132 | 2025-10-04 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 7226386d-e7f5-3886-b045-6d86ace477cb | -13.1578 | -50.9788 | 2025-10-04 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| f29ce094-9617-3c3d-b972-e76d81cb7a4e | -12.535 | -45.9864 | 2025-10-04 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a403c3f5-81c3-3940-b707-090ef6573e84 | -13.177 | -50.9764 | 2025-10-04 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 70f94e3c-3d1e-3b35-afe4-654adfdd02a8 | -13.1144 | -47.9295 | 2025-10-04 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 157ee6d5-5841-35a5-b674-c6e588c2e4a3 | -13.114 | -47.9518 | 2025-10-04 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 07e4f4c6-3e36-3c14-8e0c-35f87ab74627 | -13.1774 | -50.9549 | 2025-10-04 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 214.0 |
| dc59f91d-e4ca-3d30-9bb3-9275bd27ee6a | -14.2131 | -46.0596 | 2025-10-04 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a36c6710-fc14-365b-91be-b4ee83736157 | -12.0314 | -45.1901 | 2025-10-04 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| e9133f3a-ca30-32dd-9e40-3a0de5db75f3 | -13.1582 | -50.9574 | 2025-10-04 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| f894bdb0-da95-30e2-b0e5-469770f28853 | -14.2131 | -46.0596 | 2025-10-04 11:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d59d99e2-d7e1-3f5f-8711-59f3db2fc9cc | -12.6516 | -46.9669 | 2025-10-04 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 366cdb8a-0023-3a36-b9d9-beb2bc6158c1 | -17.9768 | -49.7963 | 2025-10-04 11:00:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 54e62f1a-0dfe-3fea-b65c-5e904ff811b3 | -13.1774 | -50.9549 | 2025-10-04 11:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.7 |
| d3faaa50-c25e-3482-ad6e-2bd373e8fac9 | -13.1144 | -47.9295 | 2025-10-04 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 4cc74251-4e29-3535-8fcf-1b206b80635a | -13.1333 | -47.949 | 2025-10-04 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 36edff01-1a75-3f47-aab1-7e0ca7a8997e | -12.5355 | -45.9635 | 2025-10-04 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5fa74e20-e792-356b-9df8-85d626bdb9d7 | -12.6512 | -46.9894 | 2025-10-04 11:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f525e7bd-009e-3c47-95f2-e2f15e4d035c | -13.114 | -47.9518 | 2025-10-04 11:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| e1b489ba-1dcd-33d8-8455-dad1f79e4186 | -12.535 | -45.9864 | 2025-10-04 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| aaee6a50-f34b-3b2a-9b8d-6fa0701d78cc | -12.535 | -45.9864 | 2025-10-04 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 367.5 |
| 3bebcb13-72e6-33fc-b1a7-9d69b638a07d | -14.2131 | -46.0596 | 2025-10-04 11:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 1f72677a-76f4-3e77-903e-999a619dde94 | -13.1144 | -47.9295 | 2025-10-04 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 89587f12-f022-3501-98fb-00fe319a462f | -17.9768 | -49.7963 | 2025-10-04 11:10:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 239.4 |
| fd4b2d4d-626c-32ba-bda5-538e56952909 | -12.5158 | -45.9893 | 2025-10-04 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e841027d-7f8a-3cf9-9a52-d1297635babc | -12.6512 | -46.9894 | 2025-10-04 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7932d900-6d40-3c2f-b8ef-0421381970da | -13.1966 | -50.9525 | 2025-10-04 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6a08f6ca-ab03-3b8a-92d1-f4489bf29a30 | -13.1962 | -50.9739 | 2025-10-04 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9f467264-c7d3-3f1d-8a6c-60b860091afa | -12.6516 | -46.9669 | 2025-10-04 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eb88d041-f2ed-3828-a203-a25bfecc61f0 | -12.5355 | -45.9635 | 2025-10-04 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b5514885-75f5-304c-992a-02c1b3428eb2 | -13.114 | -47.9518 | 2025-10-04 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 4febc6ba-3524-3e81-9a93-338a8fe872f2 | -13.1774 | -50.9549 | 2025-10-04 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 0916be78-65e7-3762-9df1-9fd3f231fd98 | -12.8761 | -47.2937 | 2025-10-04 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 0a202e4b-5f2d-3943-9136-2d8cba36c561 | -12.5355 | -45.9635 | 2025-10-04 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 297.2 |
| b2db62d0-657e-39bf-bc77-3d62ad5cd2b4 | -12.031 | -45.2132 | 2025-10-04 11:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 377906b5-1e4f-3e08-af40-846a3f885c63 | -12.5158 | -45.9893 | 2025-10-04 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 466.3 |


[Clique aqui para ver as próximas entradas](README135.md)
