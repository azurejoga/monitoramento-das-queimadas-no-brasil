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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4fe01d1-33a2-38d2-8595-15d774786dc4 | -14.1824 | -52.9089 | 2026-08-18 08:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 050eea99-ec16-3494-868e-20d316692e0c | -14.1828 | -52.8878 | 2026-08-18 08:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 313cd105-332c-35b7-b6c9-d04cc36baa88 | -14.1824 | -52.9089 | 2026-08-18 09:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| dd528ec4-aa8e-3dc1-b674-1e835caf1c2c | -14.1828 | -52.8878 | 2026-08-18 09:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ddd12d80-800f-3289-abff-8069e843cdf1 | -6.7478 | -59.1716 | 2026-08-18 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 750f40bf-2e28-3973-bc91-114fe271b2e5 | -6.7478 | -59.1716 | 2026-08-18 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ecc9b9c5-134b-3b8a-8592-3b91fedf5f54 | -6.7478 | -59.1716 | 2026-08-18 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e26e765e-1708-3af2-97cd-daa812863ab4 | -8.5787 | -54.7364 | 2026-08-18 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.6 |
| e5e4dc2c-fb49-38d1-88e2-366922f70596 | -8.5788 | -54.7162 | 2026-08-18 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 3849ec88-acb8-3313-b81b-1c819cddd40d | -8.5788 | -54.7162 | 2026-08-18 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 4af8f76a-5368-3fd6-bb2d-d1fb3934d300 | -8.5787 | -54.7364 | 2026-08-18 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 208.5 |
| afdcfb96-2693-3cdb-8440-05f39897848b | -8.5787 | -54.7364 | 2026-08-18 10:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 1184eeff-3785-3653-9231-dec489f6f19f | -8.5788 | -54.7162 | 2026-08-18 10:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| b0753a27-1799-3d03-9089-64df0387cb7d | -8.5787 | -54.7364 | 2026-08-18 10:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 1f3dad24-fd1e-368f-940c-0d35c5350658 | -8.5788 | -54.7162 | 2026-08-18 10:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 109f33f6-5c94-3dc1-aaac-525a4739f2d8 | -8.5788 | -54.7162 | 2026-08-18 10:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 40288d20-3f3c-3fa4-ac1f-b2464d4c76e7 | -8.5787 | -54.7364 | 2026-08-18 10:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 4bc065b1-f6b7-33a3-a67b-beb2b1b77ec6 | -8.5788 | -54.7162 | 2026-08-18 10:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 204d1aa8-625b-3686-8131-2430b23357a5 | -8.5787 | -54.7364 | 2026-08-18 10:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 176f676c-4584-3bb5-88e1-e64213904625 | -14.1628 | -52.9323 | 2026-08-18 10:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d542a85d-23cd-3834-90fc-6513ebd6ad32 | -8.5787 | -54.7364 | 2026-08-18 10:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 7d934947-69f0-339e-a319-fc0c090b308b | -8.5788 | -54.7162 | 2026-08-18 10:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 1bfae169-476d-3fbc-a072-4e3128ef0c68 | -14.1824 | -52.9089 | 2026-08-18 11:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 797a621a-460f-339c-a8b6-2a0fb4911217 | -8.5787 | -54.7364 | 2026-08-18 11:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| ad9a8f7f-3db3-30c1-9036-b09be51dd88d | -8.5788 | -54.7162 | 2026-08-18 11:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 1aaa65fe-816c-398c-b6fc-4069e6dd9c6c | -14.1631 | -52.9113 | 2026-08-18 11:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d5bc8fcc-3f9e-3245-8f4f-790bd23a46ad | -8.5973 | -54.7352 | 2026-08-18 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 40788a83-bd2b-3851-a305-94196eed905d | -8.5787 | -54.7364 | 2026-08-18 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.9 |
| b4e09de9-99ba-3d03-8324-2898e365ea79 | -8.5788 | -54.7162 | 2026-08-18 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| b93ba9b5-84b2-3180-9622-7de39073f10d | -14.1824 | -52.9089 | 2026-08-18 11:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 367f127c-1d9e-3861-981b-57551fa06e12 | -14.1824 | -52.9089 | 2026-08-18 11:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4b9edebc-d613-33c7-9057-648f741c41bc | -8.5788 | -54.7162 | 2026-08-18 11:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 0424bcd7-249d-304d-a0c7-a8b0605ea7a7 | -14.1821 | -52.93 | 2026-08-18 11:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 34dbb34f-618e-3b61-9ca7-037d6f7f44ea | -12.7793 | -48.4205 | 2026-08-18 11:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 891ab8a1-37da-37cd-a50a-84b0315a8c2c | -8.5787 | -54.7364 | 2026-08-18 11:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.0 |
| acbcfb11-f6dc-3ad6-94d1-3eeb7724726d | -14.8233 | -46.619 | 2026-08-18 11:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5a0aa4a5-86ae-308e-ad3e-d6e71ba6ef5b | -8.5787 | -54.7364 | 2026-08-18 11:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 836154e1-4c3a-36b4-b112-9d06fc956a2e | -14.1628 | -52.9323 | 2026-08-18 11:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 925bee79-f516-3345-a193-317bb43d486a | -8.5788 | -54.7162 | 2026-08-18 11:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 1f376ae3-5948-39fe-9e27-e354066c6aec | -12.7793 | -48.4205 | 2026-08-18 11:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e70782aa-5bc8-35e0-afe6-277e70513fab | -14.1824 | -52.9089 | 2026-08-18 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 85bc8771-a52e-3ce8-b9dc-63a1acb9ebe7 | -14.1628 | -52.9323 | 2026-08-18 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e5dd3b42-1edc-399c-ac64-0e0487f9d2b8 | -8.5788 | -54.7162 | 2026-08-18 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| e7b1db8b-4f85-368a-ae52-e3331e4331ba | -12.7793 | -48.4205 | 2026-08-18 11:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| fc48525b-5daf-3475-9813-77d5c5114845 | -14.1631 | -52.9113 | 2026-08-18 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a927cab8-92f0-3912-90ae-f27a0b0ecdf2 | -12.7597 | -48.4453 | 2026-08-18 11:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 216f7918-cf53-3e7a-ab8a-3b1dd4658f91 | -8.5787 | -54.7364 | 2026-08-18 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| ca431636-0fac-39bd-a989-e758f6623a63 | -14.1821 | -52.93 | 2026-08-18 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ce33c279-d0a8-3e89-bf6e-ebeeb8a8e48d | -14.1628 | -52.9323 | 2026-08-18 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 120aa7f8-e020-346c-91f8-df085e62a818 | -8.5788 | -54.7162 | 2026-08-18 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 1588a596-75ba-3201-b099-f21b8d3dcd2c | -14.1821 | -52.93 | 2026-08-18 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1708c7e4-4bc3-3294-af92-0f187e9a9df8 | -12.7597 | -48.4453 | 2026-08-18 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1e133db1-c52a-3c43-9652-8c71649535b6 | -8.5602 | -54.7175 | 2026-08-18 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 2eb4e39d-ebc2-343d-8441-8125b00b2439 | -14.1631 | -52.9113 | 2026-08-18 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c7a16d4d-c308-3a9d-bbcd-2f9d35ec7ae4 | -8.5975 | -54.715 | 2026-08-18 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 56f509b1-fb68-321b-ae61-fdf080fa9a85 | -14.1824 | -52.9089 | 2026-08-18 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2f2305e9-1454-365c-ac98-e3859e7465d4 | -12.7793 | -48.4205 | 2026-08-18 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3fd7990c-c055-3e94-87b3-421f858fadad | -7.23978 | -49.88779 | 2026-08-18 11:53:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2f0d63b9-9299-3152-974f-50cd78871a16 | -7.1343 | -47.51898 | 2026-08-18 11:53:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 14ae1711-80ff-37e4-a684-780dc11de2f4 | -6.40552 | -54.9351 | 2026-08-18 11:53:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 552f3267-e738-3cf3-864a-d0face1bd15f | -5.37095 | -49.02418 | 2026-08-18 11:53:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4b15e1e7-691e-3c16-a699-26e3f4430c33 | -2.79986 | -48.94368 | 2026-08-18 11:53:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| aa94672c-15de-3706-86e9-7edd298c351b | -7.34705 | -45.84006 | 2026-08-18 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9d27339f-b9df-3405-9cf7-ad1f3e455b1b | -7.20395 | -43.27835 | 2026-08-18 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| d9b77ecd-3ac4-31a5-ba68-e6eaf4342943 | -7.18215 | -43.12456 | 2026-08-18 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| b737d1e9-2481-38fb-996c-af3256caf95e | -6.17997 | -47.81492 | 2026-08-18 11:53:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 257fea73-d303-3acf-89b2-3aeaa8994a55 | -3.51241 | -48.03498 | 2026-08-18 11:53:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 28fd4972-ed4f-326b-b9e8-0847b4d0db6f | -6.95704 | -44.12619 | 2026-08-18 11:53:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dad17d03-ea35-301b-a5c5-db171a68a28a | -7.6361 | -45.74295 | 2026-08-18 11:53:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 11f9840a-44d8-3d39-907d-a7bf6e4e0469 | -3.86757 | -42.96465 | 2026-08-18 11:53:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 185a4ef5-b9e2-3983-87b5-3bd6b92a8cc4 | -6.16849 | -47.76714 | 2026-08-18 11:53:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a04621aa-0f0f-3b59-bc2e-2152165ee00a | -6.41794 | -54.93704 | 2026-08-18 11:53:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7607ca2c-0e73-38d5-a610-2912a97bd158 | -7.45839 | -46.1539 | 2026-08-18 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e5623b9c-a62b-33fe-aa23-7e6dbabdebf7 | -7.23846 | -49.89693 | 2026-08-18 11:53:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3e22c64a-c6ab-36d0-9677-e0ed8c8bd514 | -2.4907 | -48.02192 | 2026-08-18 11:53:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 98216702-972b-35d6-aeae-a8beaa45e5a7 | -3.68768 | -47.64225 | 2026-08-18 11:53:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bad76b7a-9427-3600-bd8e-3714b347fdfc | -3.68642 | -47.65111 | 2026-08-18 11:53:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ed9143f6-d290-3ce1-8091-8f0467b410d7 | -4.01472 | -48.91 | 2026-08-18 11:53:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b525cbe-9bf3-3297-8661-68fa278e332e | -7.40005 | -45.08442 | 2026-08-18 11:53:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 58a4664c-233b-39ee-a781-c0fc784d8169 | -7.82263 | -44.5984 | 2026-08-18 11:53:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 17cada5b-459f-379f-bb56-2202074386ce | -4.016 | -48.90117 | 2026-08-18 11:53:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3a25fa0e-8c71-3801-9b4b-b8b4f5443856 | -6.16977 | -47.75805 | 2026-08-18 11:53:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 363ceed4-0fa3-36b5-a1e1-b397722db44e | -6.75444 | -45.02234 | 2026-08-18 11:53:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7d08baf0-bac0-3358-9b3c-718773c637fc | -7.8236 | -44.60501 | 2026-08-18 11:53:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5d69d8bc-80b3-37ac-a954-9efcf83db261 | -7.38859 | -46.81169 | 2026-08-18 11:53:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46ef0380-89f9-321e-bec1-fa0c9d4390fb | -4.94775 | -45.15213 | 2026-08-18 11:53:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ae47cdd2-3190-3165-87c6-544279aa284c | -6.9061 | -42.84566 | 2026-08-18 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 1bdbac0c-d784-3bc2-b27a-17144b2ba7a7 | -6.8116 | -45.33496 | 2026-08-18 11:53:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c2a4cfcd-36bd-313d-90c6-17f39e31a3e4 | -2.49195 | -48.01315 | 2026-08-18 11:53:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdcf60bd-c86b-31dc-a93b-18607c3cc2e3 | -2.48314 | -48.01194 | 2026-08-18 11:53:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5209a9f-5c40-3b0b-8221-7bfeb6a54a53 | -7.20622 | -43.26058 | 2026-08-18 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 47d6a89e-b6aa-34e0-9ae6-8fea856b9688 | -6.53089 | -43.10824 | 2026-08-18 11:53:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4b4bb499-017d-3ce2-ade5-b06b85a1fc2c | -7.15382 | -47.51204 | 2026-08-18 11:53:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cc143047-b396-31b7-aba2-16661fd935bb | -3.02516 | -49.04871 | 2026-08-18 11:53:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4d674f0b-becd-3bf1-8f6d-634e6b19b460 | -6.813 | -45.34132 | 2026-08-18 11:53:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1793f924-e291-39d5-9b09-a7365612d7ac | -10.28119 | -50.4169 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 488104f6-8bcc-39d4-a031-63d68fee2407 | -11.10027 | -49.91638 | 2026-08-18 11:55:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1d158684-b40a-31ce-a91a-db8eef6c0965 | -10.76837 | -50.3623 | 2026-08-18 11:55:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4bbf9dee-9a5f-371c-9340-0bb859e43546 | -9.72243 | -46.09956 | 2026-08-18 11:55:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3bd0b59b-e0d8-39a3-a748-5d0cfbc4a43c | -11.13546 | -47.28397 | 2026-08-18 11:55:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README64.md)
