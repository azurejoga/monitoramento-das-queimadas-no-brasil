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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58dc88fc-e2cf-3670-9e7a-a511fbae99ef | -9.4712 | -51.93783 | 2025-08-28 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 2512f517-3d68-386b-9594-1caac6c0f877 | -11.33103 | -43.55589 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a08aace-4727-3c5c-8c1e-1e8c4560674e | -9.66238 | -48.31139 | 2025-08-28 00:09:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0b2bcc77-bfb0-323d-b382-d745b3033733 | -16.80606 | -41.22504 | 2025-08-28 00:09:00 | TERRA_M-M | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 971f766b-42c7-394e-a1f8-60f52e148d29 | -13.62861 | -48.25035 | 2025-08-28 00:09:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 2f16430d-f876-3a49-bf99-3f46ba9daa65 | -13.74718 | -51.89318 | 2025-08-28 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| bd45f796-cf9a-3778-b93a-60352311fe92 | -12.88509 | -48.11382 | 2025-08-28 00:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| d9078f48-ef81-3345-8141-3b19e507fa6c | -11.28901 | -43.3088 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bc481e15-983d-3555-9408-886a746eeb71 | -12.44068 | -45.95984 | 2025-08-28 00:09:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3f5288ae-3323-3949-a4a7-9fb3fd5f7051 | -17.81401 | -44.51722 | 2025-08-28 00:09:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 3b79b9e3-5ae5-33ad-91e9-10d3caeef51f | -17.5495 | -46.62608 | 2025-08-28 00:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 69baa739-f6ad-39e4-9c0c-6b96099d5a03 | -11.34677 | -43.53411 | 2025-08-28 00:09:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d6412f68-039e-37f6-84bd-5342b86be7fe | -6.9129 | -62.9366 | 2025-08-28 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 04c4bef8-4192-32f7-aca6-d69778bee10f | -9.1363 | -65.2835 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 30b9f197-4650-370c-aff2-ddd9aca285b8 | -9.0786 | -65.7338 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e65fad12-0eb3-379c-9a3e-6d464c524ec7 | -11.3329 | -43.5452 | 2025-08-28 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| fafa6be9-f44a-35a3-aacd-7c4a67b66e30 | -11.2191 | -55.0382 | 2025-08-28 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| df45a21b-27b5-35c4-a40b-cf0eeb8db95e | -4.8079 | -47.2604 | 2025-08-28 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 2ccdda72-c31d-30f8-862f-fffd549cde26 | -9.134 | -65.7694 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 313.5 |
| 7b71e38d-b3a1-3d0b-b530-086ccf4b0cba | -7.3541 | -59.6669 | 2025-08-28 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3a65e5c7-2218-3567-b97c-feaae4c3af00 | -9.181 | -60.8131 | 2025-08-28 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 54c97dea-887d-3c3a-b1d2-40a75a565b1c | -10.4736 | -57.9563 | 2025-08-28 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8a9ac138-07d5-3279-ac12-ef01794d8b39 | -13.1837 | -45.2865 | 2025-08-28 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1cd94e99-2b6d-39b6-b348-d676198478ee | -9.4864 | -51.9387 | 2025-08-28 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| f63fed18-07b5-3b98-ab42-d1a0b364ed4c | -5.3285 | -55.8878 | 2025-08-28 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 10ab2256-bfd2-3bb3-9c89-2831152ecbcb | -7.3542 | -59.6476 | 2025-08-28 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| fd5aca1d-4bae-38ac-af67-c050b7329831 | -9.3169 | -57.6967 | 2025-08-28 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 66025ec7-6e03-3106-ab7c-3a619790c0d9 | -11.2189 | -55.0585 | 2025-08-28 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| b3bd6c26-b651-3e9c-9b1c-de3dc3793294 | -7.3356 | -59.6676 | 2025-08-28 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c7740e66-ef84-387a-8708-6fb1788eebdc | -8.948 | -65.9429 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 2d4b58df-e36d-368b-84e4-0e16a875e4e2 | -9.1154 | -65.7886 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 448.5 |
| d7de1ffc-1007-33c7-b8ca-f92f3b7f600f | -3.2485 | -43.4406 | 2025-08-28 00:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 07a865be-2539-3b81-958c-8ad4c39f24d9 | -13.4234 | -46.8503 | 2025-08-28 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 68a9a22a-6c0d-3b27-8e1d-ebddaa8d52d7 | -6.8772 | -43.6152 | 2025-08-28 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| cfc7967b-3b2d-349d-9764-7dd28c0cf18f | -10.5375 | -46.6894 | 2025-08-28 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b3c48611-4a07-3ce7-bbf2-94ee172c15e3 | -9.1339 | -65.788 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 522.8 |
| e685e890-207e-3348-8a6e-38ae186101f7 | -3.2299 | -43.4414 | 2025-08-28 00:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 38ae3034-0470-353a-94a9-79b23021ecf6 | -9.1338 | -65.8067 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c5685171-b244-31d0-9092-6ba5c5b296f0 | -11.2378 | -55.0569 | 2025-08-28 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1ae8dbf6-045f-39df-a2df-7c8eafe9c261 | -9.406 | -60.5711 | 2025-08-28 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 6bfb086a-cb28-32e1-a8ed-19000bf6d4ce | -9.5423 | -62.4014 | 2025-08-28 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| beed032c-b17d-3153-b4c4-462b6ebe162e | -4.7893 | -47.2614 | 2025-08-28 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 987633c6-ebad-33fe-8795-4175563658a2 | -7.6242 | -60.8448 | 2025-08-28 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 50c09102-a99d-3d73-8fb7-5b3749d4398d | -7.3357 | -59.6484 | 2025-08-28 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9e01ec8f-a632-3b58-99c8-f91a91cdc9bb | -12.8032 | -48.1516 | 2025-08-28 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 34ea7730-bb15-3412-b0ff-a9d58d17fb9a | -9.0969 | -65.7892 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4852ba67-161b-3eba-8559-fbaae3f6a634 | -8.9665 | -65.9424 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 363cce92-4de1-384f-a0b1-9f1ea1050dbb | -8.9664 | -65.961 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 37b63882-1425-34f2-bd79-f99b6dd7878c | -8.9479 | -65.9616 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 157.9 |
| f10811f9-72d3-3bf0-8a1c-b9deba898744 | -9.1155 | -65.7699 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 254.8 |
| 60e86390-8ac3-36e4-80e1-64f98cdc9a08 | -10.5565 | -46.6871 | 2025-08-28 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a22f3026-b293-393d-8018-bb2ef4002d2a | -11.3526 | -43.5187 | 2025-08-28 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7eddc08a-6108-3f56-9c20-6503af7149ee | -13.7566 | -51.9053 | 2025-08-28 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| adfd3a34-5bfd-3226-b819-809cd0f2ce12 | -10.4738 | -57.9366 | 2025-08-28 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 1b2dd6a3-92d9-323d-b1b2-f21e882fd7bd | -8.9478 | -65.9802 | 2025-08-28 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 9b2bc5c2-cc51-3939-ae9d-a0f5eee602f9 | -11.3334 | -43.5216 | 2025-08-28 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.8 |
| cfc99800-ad08-3d9c-b0d6-87f2b728a7af | -13.1644 | -45.2897 | 2025-08-28 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e273af38-74e0-3033-809e-7756ba87ccf9 | -7.4283 | -40.079 | 2025-08-28 00:10:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 0da4ba99-29d0-3ec6-99d2-fe87e95a0f09 | -4.87465 | -44.95799 | 2025-08-28 00:11:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa15295b-18e1-3dd4-8e0e-cbb5b4b26830 | -7.28808 | -49.26978 | 2025-08-28 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2dca590d-3c9b-38bf-83b7-1cf628b82e60 | -4.79648 | -47.27476 | 2025-08-28 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c187837d-c2be-3e14-8ece-27caee2c5a8e | -7.63826 | -42.67069 | 2025-08-28 00:11:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 09487823-dbc8-3bfa-997f-cc6431cc0a47 | -3.23665 | -43.43163 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| acc2a79d-9c1a-3e39-bdc3-a5b09a340ed0 | -4.15473 | -43.87483 | 2025-08-28 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e935098d-a808-3859-9204-801af8ba51a0 | -6.87475 | -43.61898 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 44a327f9-0342-350f-80b0-514ada056d6e | -5.03592 | -43.58212 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b342f9e8-216a-3b7e-b04e-9d941fc443d5 | -3.22905 | -43.44166 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 260fe817-e036-3a2d-b5e4-f93b8c844b9c | -5.20325 | -46.06293 | 2025-08-28 00:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5a37391f-d0e1-3e7f-9549-aa58c3b07d9b | -6.22398 | -43.3655 | 2025-08-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3f44badb-42c7-33d8-8865-cbbd1141af97 | -6.26787 | -43.82925 | 2025-08-28 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f56dd1f0-579f-33ba-80d6-9a89f3144c59 | -6.86463 | -43.61126 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1db6064a-7a35-32ce-b67e-92d0d9484625 | -4.08444 | -48.03549 | 2025-08-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7b39b10f-187b-31a7-ba5f-b7071b28b824 | -3.73597 | -40.27871 | 2025-08-28 00:11:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 448814aa-13fd-37a0-8083-32833d49901c | -6.18289 | -44.01288 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7edc9ad6-2cba-3472-96ab-d7f1c37a9894 | -6.18616 | -44.17037 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f43a78e-063b-3624-a2dc-5dcf208b8c02 | -7.25619 | -45.35421 | 2025-08-28 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 36ee8684-b946-3935-bc5b-f746dfaac22d | -2.44551 | -47.12346 | 2025-08-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 886a9555-ea25-3aaf-8cea-ad3a720a4994 | -5.67201 | -44.2508 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 35617080-7e37-3c77-a183-83fd5c2ff7e5 | -5.48085 | -41.41375 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d56fd0cc-253c-31b2-b0e4-96acacb90667 | -2.4439 | -47.11166 | 2025-08-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| cd0de787-b734-3506-94b9-7ad68339d73a | -6.1939 | -44.16002 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f46814d4-2089-3a10-81a7-9a8e96a48d40 | -6.86586 | -43.62025 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 00c78409-5766-3d5a-a57d-bba52837b1da | -6.44031 | -37.14361 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 87e6bee6-96f3-3feb-947e-ec2c4b073bcd | -3.23787 | -43.44041 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 905dfd49-75d3-371e-88a5-cdae99f14b72 | -6.81254 | -44.9999 | 2025-08-28 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b77b561d-a2f4-31eb-8ce3-7027fffeccf9 | -6.5777 | -47.37476 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1d919be3-d807-3c0f-831e-0d579ebef06b | -6.56674 | -47.37619 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| eed77e8e-6e51-3462-ae23-93c32707ba18 | -6.12809 | -44.42054 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ae956cba-7f53-3f21-ad73-43509d5a12a6 | -5.17726 | -43.27158 | 2025-08-28 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0f438bf6-4c12-31ac-87e6-2503cfbf955d | -6.86833 | -43.63823 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d39edae5-4f66-3671-9c2c-376ddeb1d04e | -7.42411 | -42.05557 | 2025-08-28 00:11:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 80a1ce55-8dc7-3bc3-b7f8-1b844babbe67 | -6.17394 | -44.01414 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c3d30c7-e205-3882-9574-8e62974a6768 | -4.7859 | -47.27606 | 2025-08-28 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b32a1336-db45-3aca-8b15-4e0f5b086138 | -6.39975 | -44.66262 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43705e10-cbd9-3c9f-9b38-12b003007504 | -7.1216 | -38.51786 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 66965ba7-ca03-3e45-a1fd-495604d59bc4 | -6.18662 | -44.04009 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94a87cda-4b4f-3961-ada1-2bdb5dad1f8f | -5.19351 | -46.0643 | 2025-08-28 00:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 170c9bf4-f4c4-3651-9e3c-982b1c830e20 | -6.4352 | -44.57978 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 08af6033-4869-3977-b84b-073cc284b587 | -4.78757 | -45.32765 | 2025-08-28 00:11:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7cdec97-52df-3954-93e4-817370248c09 | -6.88956 | -44.39986 | 2025-08-28 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README4.md)
