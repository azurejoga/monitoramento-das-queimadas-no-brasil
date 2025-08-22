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
| 964a449f-3afe-3588-b2bb-1c7e4e95599d | -9.2095 | -59.4609 | 2025-08-22 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 44b64015-3b19-39f4-8659-e423a15ad6a4 | -14.7717 | -45.4055 | 2025-08-22 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 706668c7-a45a-3943-b618-f9f12c21bb54 | -12.9921 | -45.2252 | 2025-08-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 39844380-9048-3d5a-9ae4-f2a2955a2b7b | -8.8736 | -62.4115 | 2025-08-22 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| de470627-64c3-30be-aaa8-a883dd2be2f7 | -12.9925 | -45.202 | 2025-08-22 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| e4a0b774-ea43-32b8-b623-c04142daccce | -18.8805 | -45.0093 | 2025-08-22 00:40:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cd128aab-94ef-3036-9021-1f088be49df8 | -8.613 | -62.6118 | 2025-08-22 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 008aa323-d907-355a-8bab-560c7bfef003 | -8.6129 | -62.6308 | 2025-08-22 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1d706571-67d9-34b4-ae78-17f393b81eb8 | -9.5365 | -60.5451 | 2025-08-22 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 80de591e-6632-399f-855e-2dd8a5aaf0bb | -12.9921 | -45.2252 | 2025-08-22 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 73da1ce0-0c7a-308f-8a02-ea2dde2186c8 | -9.518 | -60.5268 | 2025-08-22 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0c29852f-3f48-3778-bd48-d911a685f61f | -9.5179 | -60.5461 | 2025-08-22 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6b983bfc-a4ba-3a67-877a-42117ef47523 | -13.0119 | -45.1988 | 2025-08-22 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| df43ba58-441b-3802-a168-2d88b2615304 | -20.2731 | -46.5778 | 2025-08-22 00:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e01fc719-8f8c-377e-98d5-0fadb97700eb | -8.5943 | -62.6315 | 2025-08-22 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 86049c1f-1249-3510-9f1b-c2e18eeaae4f | -12.9528 | -46.2647 | 2025-08-22 00:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 90b4c5fe-3b3b-3663-8f24-cfcc059d1fd6 | -9.2095 | -59.4609 | 2025-08-22 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 48eaf348-4fd2-3e3c-ad13-292e3a29ce9c | -13.0114 | -45.222 | 2025-08-22 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 94aa54b6-11c8-3084-bedc-00673b465b12 | -8.5944 | -62.6126 | 2025-08-22 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 481cf910-d72c-3a96-87c7-f36fc4f744a9 | -14.7717 | -45.4055 | 2025-08-22 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c1ef4258-753d-3366-884e-f36741bfce7e | -18.8805 | -45.0093 | 2025-08-22 00:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| adf3d5cc-ea7e-309e-97ca-436bfb20032c | -8.6129 | -62.6308 | 2025-08-22 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 86718f09-dff0-3503-bf3c-c804ecead500 | -12.9528 | -46.2647 | 2025-08-22 00:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| db3358f5-b067-3186-bf42-f0ac52965bed | -8.8921 | -62.4297 | 2025-08-22 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 391a7d5f-ab08-3f30-ab91-d7110876b29c | -9.6108 | -40.3171 | 2025-08-22 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.4 |
| f92cc3be-9729-3532-9edc-9deda41bd424 | -13.0114 | -45.222 | 2025-08-22 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 18bd64b1-2c88-303f-9cc0-a8f5204e5f47 | -8.5943 | -62.6315 | 2025-08-22 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2599cef4-e8f9-3504-8a07-bad6b5033b6c | -9.6104 | -40.342 | 2025-08-22 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 253.4 |
| cc06b0ab-ae22-3553-a696-a09e28decd2e | -8.613 | -62.6118 | 2025-08-22 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 18b82d29-d1ed-37b9-8bbd-30eced39b25b | -9.5179 | -60.5461 | 2025-08-22 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.2 |
| e41a4e8c-bc38-3e3c-9425-3a03942665a6 | -12.9921 | -45.2252 | 2025-08-22 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b2916254-bc38-303e-80d6-9f4debe1e253 | -9.5365 | -60.5451 | 2025-08-22 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f3dcd45b-4fcc-3a58-8e94-197423948138 | -11.1212 | -44.7217 | 2025-08-22 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 74bac175-8531-365f-95a8-d85229474344 | -8.5944 | -62.6126 | 2025-08-22 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 8e2fcaad-395d-384a-abd3-54744f41a6f3 | -8.8922 | -62.4107 | 2025-08-22 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ae0f7d65-2ce5-38d6-a4ba-8f2bf2429051 | -21.5032 | -47.2204 | 2025-08-22 01:00:00 | GOES-19 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| 195d3d15-e954-35d8-8a04-4e0ecd152086 | -12.9921 | -45.2252 | 2025-08-22 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 371ba982-e996-3bb0-9498-0c682eb2fc7e | -18.8805 | -45.0093 | 2025-08-22 01:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4c5572de-4c58-3420-8e8a-6c6286dc7c9b | -8.5944 | -62.6126 | 2025-08-22 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f824913b-8c2a-3d02-aa20-615ef8d8e31d | -8.613 | -62.6118 | 2025-08-22 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 646d3b87-6f3e-3577-bd2d-a46e4b9e0bed | -9.5365 | -60.5451 | 2025-08-22 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e8954d02-9484-3f0a-af4d-dbfd3f6d8890 | -8.9106 | -62.4289 | 2025-08-22 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 404bed14-64ef-3388-843c-95c4140e28b7 | -8.5943 | -62.6315 | 2025-08-22 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 8e4bccfe-c366-31ba-b6cf-1e21002dd63b | -8.8921 | -62.4297 | 2025-08-22 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 44bd1dfb-cd60-30f1-9a55-fd566473c17a | -8.8736 | -62.4115 | 2025-08-22 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ba44e4fe-bd5a-3a3b-8896-b100ac8471d8 | -13.0114 | -45.222 | 2025-08-22 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9fb49d71-964f-3189-a85c-ddd785937386 | -8.6129 | -62.6308 | 2025-08-22 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 07f63f2a-0de2-39b7-a9bb-5de35eadff37 | -9.5179 | -60.5461 | 2025-08-22 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 96e60e9a-6400-3bd9-ad79-5e37bcc2cab8 | -8.8735 | -62.4305 | 2025-08-22 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| cd129a99-64e7-3ca5-9e75-97a68f7dc161 | -18.8798 | -45.0334 | 2025-08-22 01:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a00b3d0a-3e86-306a-bffa-5efb445c5b81 | -20.23398 | -50.03227 | 2025-08-22 01:05:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.7 |
| 0a6c440a-c72b-3daf-9ede-df55407c7cad | -22.55521 | -49.77014 | 2025-08-22 01:05:00 | TERRA_M-M | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f503710f-d37b-33cf-827f-8b2b160503e0 | -21.18883 | -47.13733 | 2025-08-22 01:05:00 | TERRA_M-M | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 72db8839-2a8e-3d74-b027-36b54180231d | -21.49645 | -47.22572 | 2025-08-22 01:05:00 | TERRA_M-M | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 77833083-beab-3806-bdbe-a42706076d26 | -20.27229 | -46.57739 | 2025-08-22 01:05:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8a0b7504-1588-34cd-851a-dde9c829de2b | -21.59409 | -48.99267 | 2025-08-22 01:05:00 | TERRA_M-M | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 37.9 |
| cea27b4c-07e2-34fe-83ee-05a1bf6dc3eb | -23.90502 | -49.44462 | 2025-08-22 01:05:00 | TERRA_M-M | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 67b42cad-8406-36a2-b461-b38c48c8d685 | -24.54108 | -49.05764 | 2025-08-22 01:05:00 | TERRA_M-M | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| bae4c3b9-3811-322a-9dea-d636612b80b0 | -23.2963 | -47.47189 | 2025-08-22 01:05:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| c37561eb-b261-3176-aec7-cf941e132db3 | -23.29962 | -47.46561 | 2025-08-22 01:05:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 99e7bda0-959c-3e70-ab85-c906780f2787 | -23.89963 | -49.45195 | 2025-08-22 01:05:00 | TERRA_M-M | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 46df593b-6de0-3b3b-9258-080f6fdaf50f | -20.23164 | -50.01829 | 2025-08-22 01:05:00 | TERRA_M-M | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| d060b652-2538-3d33-a054-2ff49a93d964 | -20.08417 | -46.13371 | 2025-08-22 01:05:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 4f6e52da-8d84-3263-85af-2289d1625350 | -22.29197 | -48.21148 | 2025-08-22 01:05:00 | TERRA_M-M | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c51a5c66-2f81-32d3-8969-ea2a772a94a3 | -23.90733 | -49.45815 | 2025-08-22 01:05:00 | TERRA_M-M | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a65e834b-5cb6-3428-b02b-dfd600e835e4 | -23.91001 | -49.44983 | 2025-08-22 01:05:00 | TERRA_M-M | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 67fa4a38-259e-3ab4-a4b0-e43d96ff674d | -14.73691 | -56.03366 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1083ef3-b91c-3c04-a9b5-7524ca6577b0 | -15.66219 | -52.68653 | 2025-08-22 01:07:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d14ebd5-030a-3e39-961e-3de69bb8ab88 | -15.03354 | -54.85801 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65c08402-947a-34c8-8f3a-ed3143a93763 | -14.99791 | -54.86322 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d022cb1-e4dc-3c37-9204-78ed40923c0b | -14.76556 | -56.03236 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fa3b9ce5-7eca-3095-8bff-a7514e637b9c | -18.8745 | -45.0076 | 2025-08-22 01:07:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c825f50e-1160-3f3e-97e6-183f6abdf90d | -14.65056 | -54.88448 | 2025-08-22 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c0f3a3dd-3c93-3ccd-80d9-3dfc46711dca | -13.42928 | -57.17764 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 53de33aa-df61-3cf0-b723-518354e27c68 | -14.88805 | -47.96334 | 2025-08-22 01:07:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 97bcafaf-2e7f-3b5b-93d4-b323d6dc49bd | -14.74703 | -56.04147 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 747d999a-d492-3805-8e6a-e06a267b9993 | -14.79174 | -59.65551 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| cb03e07a-3b7f-3e5a-b293-b00e5c325ccd | -13.18693 | -54.96019 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9d8d320a-5fc7-3fc4-a6cc-ecb36a6579b6 | -14.64559 | -54.91357 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3e5e6558-ad80-3f89-bbac-2235eb68651a | -13.14441 | -54.9191 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e707cec7-eed2-3860-96b6-7fb441a8d96f | -14.64793 | -54.86599 | 2025-08-22 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 70a4dd2d-c165-38ef-ac00-97fec8b7abd3 | -13.01059 | -45.24747 | 2025-08-22 01:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ffc91b3d-bfc7-35de-b413-b312de1d0da4 | -14.73817 | -56.04278 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e81f4948-e5cb-3852-912a-d5d2220a1343 | -14.74828 | -56.05059 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7097f212-ca38-3ff4-8e31-7b618c5382d4 | -14.75795 | -56.0428 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b6565fdf-2412-3d9d-806e-e7e418eff06c | -14.66314 | -54.84474 | 2025-08-22 01:07:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| f961d3e5-1c81-3341-9bfb-65d9c2962770 | -13.64427 | -45.71889 | 2025-08-22 01:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3b3f2012-4e89-3667-a9e0-c9ede62e419d | -15.02463 | -54.85925 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4bd3a1fa-dd61-37b2-83a4-49d60aa4ef62 | -14.87885 | -47.94582 | 2025-08-22 01:07:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| dea19a61-2342-3c38-850e-42d14002dec6 | -14.33296 | -53.10864 | 2025-08-22 01:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a7caf066-06d1-3532-9970-0d309842c923 | -12.9554 | -46.29059 | 2025-08-22 01:07:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| ce732c2b-24ce-3300-a757-067e5b790a07 | -14.3313 | -53.09781 | 2025-08-22 01:07:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4245bfa4-2433-388d-8473-d645bf1fb206 | -13.64798 | -45.71111 | 2025-08-22 01:07:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 84a5d3f6-e082-344e-aa70-8b45d16ae3dc | -14.76432 | -56.02324 | 2025-08-22 01:07:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15a99f5a-3882-3219-a465-2f35c79d7513 | -12.96135 | -46.28238 | 2025-08-22 01:07:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 2b2caf76-69df-332c-9d45-b689bb0c6d76 | -13.32685 | -54.39845 | 2025-08-22 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d323f897-9931-3a37-a1aa-78e6d098d867 | -13.33596 | -54.39705 | 2025-08-22 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 431d65a9-7f00-3b66-9618-dbdbee8ffc03 | -17.67483 | -54.0584 | 2025-08-22 01:07:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4fe8830-49e5-36eb-8aeb-9e8fc6449df5 | -15.56032 | -51.69996 | 2025-08-22 01:07:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85b9008a-ccd6-3472-a9a7-a3dd4813d713 | -15.03484 | -54.86714 | 2025-08-22 01:07:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README3.md)
