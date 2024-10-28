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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8305b407-d9b7-3c0e-9e1e-59162acfc83a | -12.89023 | -44.61174 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83699963-a84c-3d0d-b5f2-1bcec256e876 | -12.8871 | -44.60741 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b93f1a89-edd3-3aa8-8a7a-68c4f73968aa | -12.88312 | -44.61024 | 2024-10-28 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beecc758-e65e-37c3-9cda-86df707cd1fc | -11.38981 | -37.67578 | 2024-10-28 03:19:00 | NOAA-21 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d0edf5f-30b2-32b5-be6f-d5976f980495 | -11.29176 | -41.8607 | 2024-10-28 03:19:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0a580056-a939-3878-86e0-e37001db54c4 | -11.29073 | -41.86588 | 2024-10-28 03:19:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4c1a5e9c-2f73-3bd4-b81d-45c8ad387d8a | -11.28868 | -41.86282 | 2024-10-28 03:19:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 379d8bd1-d7c9-3f07-8d94-520e6006313c | -11.14115 | -42.17574 | 2024-10-28 03:19:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d48d424-6aa4-31d0-b6fe-6feaef6a8609 | -11.13655 | -42.17376 | 2024-10-28 03:19:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c2225a1-00dc-3415-8b0e-3656a9ed4189 | -1.1836 | -53.4956 | 2024-10-28 03:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 891d4b1d-eadf-33d0-ae80-73a75383c3e1 | -1.9763 | -52.0804 | 2024-10-28 03:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| eb326e5f-c519-336f-a353-a0564e088b5d | -2.2662 | -53.7825 | 2024-10-28 03:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 84e63e1a-f473-3112-9b24-2c22ac9d7190 | -2.2846 | -53.7822 | 2024-10-28 03:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 789c817e-8673-3e83-9aac-e81bfdbb2cb7 | -2.2662 | -53.8027 | 2024-10-28 03:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 26b7b32f-9f21-3756-95e7-82bb53da8e13 | -2.5127 | -51.1821 | 2024-10-28 03:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 6bf3f16c-629c-3a48-b8da-873e03fa7f34 | -2.5311 | -51.1816 | 2024-10-28 03:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 12f3ba1b-0043-33be-9d5a-a16b8a587bc1 | -2.833 | -49.2413 | 2024-10-28 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c59ae6c3-9e65-3c26-b38d-86d27d0f21a0 | -2.8515 | -49.2408 | 2024-10-28 03:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7a922c5b-5e43-3495-8bfd-230952efa996 | -2.8556 | -53.3256 | 2024-10-28 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3ce17122-47c3-35ae-9760-eb1e7b644367 | -2.8699 | -49.2615 | 2024-10-28 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4f192112-54bb-3500-87a3-5a96e90baac0 | -2.87 | -49.2402 | 2024-10-28 03:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9451dacf-511a-343b-8c78-3c804037d76e | -2.9761 | -50.4821 | 2024-10-28 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2f80bc9a-255a-3a30-a78a-35455852c8ba | -2.9945 | -50.4816 | 2024-10-28 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 3455abce-3c2f-3365-939f-bd09e578b766 | -3.0501 | -50.4171 | 2024-10-28 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9c019943-9178-32f8-a830-4ba94db77365 | -3.0317 | -50.4176 | 2024-10-28 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 507468d3-a4c8-327a-b824-286291a461ad | -3.0317 | -50.3967 | 2024-10-28 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8183e746-1a68-39df-8071-a37f24e020e0 | -4.12 | -47.3388 | 2024-10-28 03:25:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| a4f12121-1eeb-395c-889a-6383c4781e8f | -4.1201 | -47.3169 | 2024-10-28 03:25:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| c93c5b45-8d56-3ae5-a476-30d37f9ad477 | -4.2797 | -45.5362 | 2024-10-28 03:25:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| bda304d9-cd2d-37e0-bc03-33b5f9055275 | -4.428 | -45.6406 | 2024-10-28 03:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 999a283b-f097-3125-b7bf-b2c7ae23f64c | -4.7766 | -46.4022 | 2024-10-28 03:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 150d472f-054a-31bf-923c-1741d92b99e3 | -4.7768 | -46.3801 | 2024-10-28 03:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7ebb063e-9fbf-3fdc-9c08-698c177b15c4 | -15.3686 | -40.1745 | 2024-10-28 03:26:30 | GOES-16 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 75f7a150-c759-3a34-bb11-d8782f0c12ca | -1.1836 | -53.4956 | 2024-10-28 03:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 9f66b505-1a5f-3f70-adf0-34f1490cc4d6 | -1.1836 | -53.5158 | 2024-10-28 03:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 68095ada-9e01-3bec-83fc-14de84ddca57 | -2.2662 | -53.8027 | 2024-10-28 03:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| cb6b60e3-5745-318e-9fea-0a711fdce2a1 | -2.2662 | -53.7825 | 2024-10-28 03:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| a01bebb0-0af1-3f3f-82fb-989b1b87a91b | -2.2846 | -53.7822 | 2024-10-28 03:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0e137f46-de8a-3fe9-b3d8-73c165053e18 | -2.4104 | -48.5479 | 2024-10-28 03:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| df6a85a8-2fb1-3eb0-bf3d-59d3cef14aa8 | -2.5127 | -51.1821 | 2024-10-28 03:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| c821eea3-806e-383b-a518-c6dd08ce8e16 | -2.5311 | -51.1816 | 2024-10-28 03:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 3a840eaa-f6ca-3706-abb8-604f476d8512 | -2.833 | -49.2413 | 2024-10-28 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 315efdec-dabf-3c31-970b-7382ef7d6617 | -2.8555 | -53.3459 | 2024-10-28 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 4fb28209-2b1e-3ca0-b192-b47e915a90d3 | -2.8556 | -53.3256 | 2024-10-28 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 19bac797-1d2e-369c-9045-183043ba78cd | -2.8699 | -49.2615 | 2024-10-28 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 57476c8d-3b65-3208-a68c-19ecc2f024e6 | -2.87 | -49.2402 | 2024-10-28 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 39f1574b-483d-36e0-9921-cb06fca5ca22 | -2.9761 | -50.4821 | 2024-10-28 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e6b8d358-7a3d-375a-8487-6902567469e0 | -2.9945 | -50.4816 | 2024-10-28 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ed1694c8-cb0c-3878-8e5d-44750e3479e1 | -3.0317 | -50.3967 | 2024-10-28 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 483a0cb2-be4d-3a62-8dce-1df3aa494047 | -3.0501 | -50.4171 | 2024-10-28 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0ea257ac-4b61-3950-825c-3296e278c74b | -3.0317 | -50.4176 | 2024-10-28 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e18619bf-ce99-3104-b1ec-638c09c6676d | -4.1387 | -47.3161 | 2024-10-28 03:35:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8f4d99ce-1801-32d5-a983-1cc974d4e101 | -4.7766 | -46.4022 | 2024-10-28 03:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3c8f8aeb-a4e6-33ff-96aa-08a0230a80ca | -4.758 | -46.4033 | 2024-10-28 03:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a485b85b-db29-3a55-8547-915e65a6217e | -5.55322 | -43.22129 | 2024-10-28 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6432fce-44f6-3039-a2eb-24ce5c3f39dd | -6.60686 | -37.27881 | 2024-10-28 03:40:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ffddb59-3684-3828-9870-45d91cba8789 | -6.6034 | -37.27824 | 2024-10-28 03:40:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be23350b-8d77-355c-8901-7dc586355eaa | -6.38339 | -39.84916 | 2024-10-28 03:40:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ae6e6240-9680-32fc-be62-f42c2c9103b1 | -3.56342 | -41.40114 | 2024-10-28 03:40:00 | NPP-375D | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fd57d056-b2b7-3ec4-8650-c5b99dab20f8 | -3.55882 | -41.4003 | 2024-10-28 03:40:00 | NPP-375D | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a59141db-5c43-3da7-848d-5b5bac462d8d | -5.26602 | -41.23252 | 2024-10-28 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce64e7b0-6009-38be-9b6a-b7f657803977 | -5.26253 | -41.23387 | 2024-10-28 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 41787f3c-a457-3b09-ac2b-b74d42134d6c | -5.26157 | -41.23185 | 2024-10-28 03:40:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 66f83e0d-681f-3c60-9a80-c19d0d26bfa9 | -3.3893 | -41.62633 | 2024-10-28 03:40:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fb9861ef-15b1-3281-ac80-d3ce9c81cb96 | -5.0483 | -42.46523 | 2024-10-28 03:40:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05743f17-ebb1-3311-8fe7-ceb8bc578322 | -4.95729 | -43.19684 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b33083ec-51db-3fa5-b6f5-71e69425ec81 | -4.95677 | -43.19986 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d95182ee-ec7a-3478-a4f4-16bd3f23bfee | -4.95625 | -43.20288 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 249f2414-6db6-3885-8338-0f41bcaa13b5 | -4.95219 | -43.19599 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e6d117-42cd-30e5-a38b-34474df66a2a | -4.95167 | -43.19902 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33135404-7343-329a-ad4d-0b3d5e6b7c80 | -4.95114 | -43.20206 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b77f7b87-5d3f-3e32-92b1-66846fd749a7 | -4.94761 | -43.19212 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 589c044c-8454-3cab-ac85-feaeae99d55e | -4.73326 | -42.83111 | 2024-10-28 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c888697-e1d9-3976-8ac2-499e6c2fb2ad | -4.72826 | -42.83031 | 2024-10-28 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abb10431-fc9d-3b12-a8c2-9810665514eb | -4.69853 | -42.91436 | 2024-10-28 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93c5a748-5ff5-307b-bc8e-07cdc8b2b566 | -4.63324 | -43.11256 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b6c4f8c2-9761-304a-a8ea-03e02c1afa97 | -4.63106 | -43.11189 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef6c2b80-bd6b-3d90-a443-dd0f05e1ea5e | -4.62815 | -43.11166 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 134db3ae-4ad7-35af-bad6-3a1b37f464fd | -4.62596 | -43.11099 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8937a930-6d95-3689-a93f-48d43a6fcf2f | -4.62305 | -43.11079 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e46afa61-a638-350b-b160-acd4efe33922 | -4.54522 | -42.9802 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7dcccf5b-8bb9-3d3d-ba0f-812b61ef0d7a | -4.54474 | -42.98314 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98927ba0-ac4c-3b5b-bd6f-9c5c9690290b | -4.54343 | -42.98106 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0dc2b429-4121-3d5a-aa07-810eda147a6a | -4.54292 | -42.98402 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c8599f29-f21c-3f6b-8751-6b509e41c0f0 | -4.54017 | -42.97931 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31ab2cc7-3379-3b76-ae46-ec0587b83bf8 | -4.53967 | -42.9823 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f2e924d-924e-3efe-8082-157905a10c69 | -4.53837 | -42.98021 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad012b19-a629-3e74-a5c9-30f12e27afba | -4.48913 | -42.88128 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46cd2891-9332-3d9f-8531-5570f1fcd505 | -4.48864 | -42.88417 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5febd8b8-2f88-31e2-b5dc-07055b7634c9 | -4.48815 | -42.88703 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58a57af0-bfda-3cd4-9b05-f909bb2147d8 | -4.48262 | -42.88908 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b95e637-49dd-3c87-a3df-06c10a5be67d | -4.48213 | -42.89196 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b25fec6-977e-3a47-9d8e-3d72d3ca68b1 | -5.96717 | -42.12957 | 2024-10-28 03:40:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3567b94f-86e3-3eff-9888-0360e464e16e | -5.83266 | -42.78204 | 2024-10-28 03:40:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dade2d49-29a9-3a41-a797-481a05595ce3 | -5.67964 | -43.20312 | 2024-10-28 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec8c4f78-bdb7-3fbc-afc0-927cd6c104a3 | -5.67511 | -43.19917 | 2024-10-28 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e558210-1978-3df2-b14f-73acedfee942 | -4.96136 | -43.2037 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43023811-0397-35d5-bfb8-5939fffce08a | -5.9692 | -42.13215 | 2024-10-28 03:40:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 81cc7ee3-5a01-38e4-8661-96d95d998a87 | -5.87562 | -42.5874 | 2024-10-28 03:40:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b8e25177-1704-3756-9a67-7dd7deb6a2c0 | -5.55271 | -43.22426 | 2024-10-28 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
