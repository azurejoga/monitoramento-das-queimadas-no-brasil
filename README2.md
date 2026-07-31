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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81825225-f3b5-34ab-981a-aec7feab3ebf | -3.9671 | -48.1283 | 2026-07-31 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 016cf33b-bcc7-3c95-bf1a-75f3297d67f2 | -12.8543 | -44.386 | 2026-07-31 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 41039d7c-53a6-3fe9-b00b-572eea0c1d5c | -3.9486 | -48.1291 | 2026-07-31 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| afccb50a-4a19-3a8b-b6b3-53a1c2ff38ad | -18.0419 | -51.3097 | 2026-07-31 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f2e4f80d-1580-31c3-af58-7d59e7183278 | -12.8543 | -44.386 | 2026-07-31 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7caa0920-070f-320b-b9a4-63cb6c9261fb | -3.9671 | -48.1283 | 2026-07-31 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ca6b0b12-2d78-3bd4-be90-b4d7bbf04601 | -3.7113 | -51.1885 | 2026-07-31 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| c5c8d2a0-030b-33f9-8c6f-a6cd0472e919 | -3.7114 | -51.1677 | 2026-07-31 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| d4d40bb3-3c97-3e51-a589-05a103e0883c | -12.8543 | -44.386 | 2026-07-31 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b32c025f-4458-3ab9-adc0-8feb281a4c2a | -3.9671 | -48.1283 | 2026-07-31 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 211fa0b2-37fa-3cbb-8117-b4f4bc4ca3c7 | -3.7113 | -51.1885 | 2026-07-31 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| facf2a15-5f7d-3b2a-9899-083be08fa6b9 | -3.7114 | -51.1677 | 2026-07-31 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 027baee0-329b-31d9-9cbc-bbcaccda10b8 | -3.9671 | -48.1283 | 2026-07-31 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f4534872-df48-3050-b8b5-10354ca4bb8e | -12.8543 | -44.386 | 2026-07-31 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| db1f76db-42de-3368-ad31-fb1744da923a | -3.7113 | -51.1885 | 2026-07-31 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a0668e7d-cae9-31c2-8752-061f4be0629a | -3.7114 | -51.1677 | 2026-07-31 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b58c465c-b752-3c80-8bf0-592bc8201768 | -21.3828 | -56.8288 | 2026-07-31 01:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 127c5cdf-bcb7-3042-8d48-3e450542d006 | -12.8543 | -44.386 | 2026-07-31 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 5d9eb47f-76f5-32cd-9653-2dbea04bd955 | -14.386 | -48.0485 | 2026-07-31 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9946174a-b8da-3308-82c4-293c5eee1750 | -21.3828 | -56.8288 | 2026-07-31 01:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7de9a305-31d7-3141-8e84-6f3609beb2fd | -3.9671 | -48.1283 | 2026-07-31 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| f32beb95-1360-362d-9c1c-b2724f470b17 | -14.3855 | -48.071 | 2026-07-31 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 07dc5699-128d-31f2-adf2-e5d4b47cffd2 | -14.386 | -48.0485 | 2026-07-31 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7d91541d-2c74-348a-a612-4438f1768242 | -21.3828 | -56.8288 | 2026-07-31 01:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4da6717e-3af0-3170-aa5e-f841e8e5e9c9 | -11.3178 | -50.3847 | 2026-07-31 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 92120464-041d-35f6-8251-b3b591f1cba2 | -14.3855 | -48.071 | 2026-07-31 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 6c792c0b-e045-345a-aea8-81d2d8b532e9 | -11.3175 | -50.4061 | 2026-07-31 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| d774da3d-5f29-30e9-985a-eef0d58b9a7d | -3.9671 | -48.1283 | 2026-07-31 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3320d914-3ece-309d-8db0-77379e56d590 | -3.9671 | -48.1283 | 2026-07-31 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| fc7a254e-7d5b-3887-a005-be9705dfe68e | -14.386 | -48.0485 | 2026-07-31 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3a0e7504-125c-33b4-af69-3522c153a586 | -21.3828 | -56.8288 | 2026-07-31 02:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3b2d99bd-4641-3664-87d7-3c8d2ab37aa6 | -14.3855 | -48.071 | 2026-07-31 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7cfd9094-e0fc-395d-8714-5c59fd7d8ca7 | -3.9671 | -48.1283 | 2026-07-31 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 69c37a17-f0fc-3a29-abef-3b1754b0c6ab | -11.3178 | -50.3847 | 2026-07-31 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 92f649a2-da71-3bfc-9c5d-e0064c215510 | -11.3175 | -50.4061 | 2026-07-31 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2e781715-0fb4-3c10-ab6a-effd1552726d | -21.3828 | -56.8288 | 2026-07-31 02:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8abc4df9-410c-3b1e-a201-1056f17a83a8 | -11.3175 | -50.4061 | 2026-07-31 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c5ccdfa3-be73-3ad9-8ea1-b630463df5f1 | -3.9671 | -48.1283 | 2026-07-31 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 34eb4f39-743a-3d9e-93b6-fe189de030cf | -21.3828 | -56.8288 | 2026-07-31 02:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 80.1 |
| db66764b-85ef-33df-bdf7-4cf69415ab4f | -11.3178 | -50.3847 | 2026-07-31 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 1df22e61-e2c8-32b6-8ee1-6a9cb1afa084 | -11.3178 | -50.3847 | 2026-07-31 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3d4beb27-8580-39be-b719-ee9a5aed9268 | -3.9671 | -48.1283 | 2026-07-31 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ad5f6fb1-45c5-387f-87df-d2aadc79902f | -14.3855 | -48.071 | 2026-07-31 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4b6c84a7-a0f2-3bbd-95d6-9491bfcd486c | -21.3828 | -56.8288 | 2026-07-31 02:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7997a98d-8a04-3983-8290-5fa153879383 | -14.386 | -48.0485 | 2026-07-31 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3a7a4d68-613c-31d0-9b5d-20ddc5b1008f | -11.3175 | -50.4061 | 2026-07-31 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3dbcbb62-3c89-3cee-b1a5-bbf39de880ba | -21.3828 | -56.8288 | 2026-07-31 02:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c190eaa8-973c-3444-892e-1c0309fd4c5d | -3.9671 | -48.1283 | 2026-07-31 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 95212af9-7f2b-3676-afd0-28dfd699fd50 | -14.386 | -48.0485 | 2026-07-31 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f87797e8-6d16-3fac-9baf-db4ea20f9889 | -21.3828 | -56.8288 | 2026-07-31 02:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b3bc323f-cb2c-3c4c-a1b3-50f22ca6cf15 | -3.9671 | -48.1283 | 2026-07-31 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3a3178ed-0c0f-3966-a90b-41ac16a5689c | -8.90292 | -37.97337 | 2026-07-31 03:00:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 856ecfe7-d300-34ed-89a7-c6b71065c3ff | -13.65437 | -39.18402 | 2026-07-31 03:00:00 | NOAA-21 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1a7cded4-d7fe-319d-b5e4-353c4a021993 | -14.386 | -48.0485 | 2026-07-31 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| beb6f58a-9ccb-3dc8-967d-cfee946ae028 | -14.3855 | -48.071 | 2026-07-31 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f9f7404b-fc03-33bd-8c22-59e53fa4ce0d | -14.386 | -48.0485 | 2026-07-31 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 814562a0-42b1-39ea-b5d5-22345d5d2487 | -14.3855 | -48.071 | 2026-07-31 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9965864f-968c-3041-bb32-a5edd06ebaff | -2.91208 | -40.39621 | 2026-07-31 03:34:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b70a0ed0-6e25-3476-b643-d38cdb275007 | -4.90646 | -43.47087 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 888e04a8-2be5-318f-bf9e-49978c3cd1c1 | -3.6103 | -41.15613 | 2026-07-31 03:34:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 064bcbdd-43fb-3e01-abc4-2c57103a5460 | -7.54723 | -45.13265 | 2026-07-31 03:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d37b9a54-48c5-303f-8cfa-f07b160aa79d | -8.90146 | -37.97122 | 2026-07-31 03:34:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7cb8c8ac-b81c-3466-8d8e-d1522470f500 | -5.81026 | -43.63844 | 2026-07-31 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab7287ea-7f8b-3654-b870-0b26e4382b00 | -5.80917 | -43.64445 | 2026-07-31 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0307b745-3e83-38eb-81db-f90e6e968052 | -5.33037 | -37.32313 | 2026-07-31 03:34:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5df25754-b2ff-3c8f-b682-941282611c3d | -4.91449 | -43.46565 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 281aa843-8f8a-314c-a336-db7bb882ff03 | -4.91399 | -43.46351 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d8749b7-e1b3-34f9-ae8e-ba310c7ba443 | -4.91282 | -43.46989 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 300fd64c-2383-30cb-91b0-4b0d9d8062fb | -5.81033 | -43.6383 | 2026-07-31 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b6ad175-52e8-3909-9860-a431ff45a851 | -5.80914 | -43.64461 | 2026-07-31 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47127f40-e565-3190-991b-750114c9f03e | -4.91335 | -43.4721 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b033047-dd26-3204-8975-0fa672c86235 | -5.61145 | -37.53321 | 2026-07-31 03:34:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d1e179b-d369-39bb-9588-02bfbf5d8df9 | -3.61107 | -41.15506 | 2026-07-31 03:34:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b2b896e-6bdb-38e1-9359-81386c63986d | -4.90472 | -43.47523 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56a4a5d4-dbe5-3a2c-b8de-91bb25b6054d | -8.1632 | -34.97124 | 2026-07-31 03:34:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c67f45be-34ca-36c4-a052-4ee4f6d48384 | -5.60916 | -37.53065 | 2026-07-31 03:34:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96ea9274-1ede-364c-b630-8545883cf3d2 | -2.90619 | -40.3952 | 2026-07-31 03:34:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 45ba2d4c-7da5-33e4-9c66-3cc952531e25 | -8.90143 | -37.9693 | 2026-07-31 03:34:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1c62a7fa-1d5d-3afe-95df-762b17742421 | -4.90531 | -43.47738 | 2026-07-31 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f2d03e6-f5ed-31a0-8ee8-66125703e404 | -12.45489 | -43.53069 | 2026-07-31 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97debcf1-be87-330d-a2ec-82603de5ca17 | -11.82773 | -45.60648 | 2026-07-31 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ef68531-6ee2-3cb6-a0ba-23a1b8bcbc47 | -13.28891 | -43.10006 | 2026-07-31 03:36:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3fec1d81-a295-3638-8f08-cb479ba46230 | -12.62582 | -44.59904 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1145e765-3e63-34da-a4ad-ff126880878b | -14.20875 | -44.10758 | 2026-07-31 03:36:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a01da126-345e-3271-88fd-68b388a07b96 | -11.93516 | -43.44051 | 2026-07-31 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea035d4b-bb0a-3a98-ad7b-a91d6753833c | -12.61938 | -44.59747 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c81b38-2b38-336b-a64a-d3edbf188c27 | -11.25778 | -40.34495 | 2026-07-31 03:36:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49b583da-911e-3f36-a7f1-c573163b11f3 | -12.60345 | -44.64102 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffd6117b-984b-3bea-87b7-95c38ed0806d | -12.67726 | -43.0967 | 2026-07-31 03:36:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dd50bdb3-ecb9-3213-ab49-5968ddf35f89 | -12.58735 | -44.62876 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc43b9a9-ffd6-3a74-aebc-44a4e365f3a5 | -12.62647 | -44.62831 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00538ce7-491a-3cdc-a0fd-36fdedcd58c9 | -9.63535 | -40.60365 | 2026-07-31 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d40f9cc6-18eb-3494-acad-1e25c3da59eb | -12.59405 | -44.62123 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe84506e-5bcb-391d-9205-d3aa18d7a430 | -12.60292 | -44.6113 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d4d595-d2b9-3a69-830b-2f133ebb1c36 | -11.2522 | -40.34658 | 2026-07-31 03:36:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0e02794e-5594-3e5e-b0b4-0808d086435b | -11.25269 | -40.34394 | 2026-07-31 03:36:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bad06d96-8b91-3a8d-a0ca-d301604b5130 | -12.61231 | -44.63115 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 463b78d9-396d-3a90-b8d0-4f18da189107 | -12.5962 | -44.6186 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a2c8767-c1e0-3025-894d-9bbe1584b9ca | -12.61115 | -44.6367 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f14b9e94-6e9d-3d40-abbc-1f191fbe3c40 | -12.61176 | -44.60151 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
