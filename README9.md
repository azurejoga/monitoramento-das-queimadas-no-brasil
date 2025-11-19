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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 310206e7-5872-376c-8afb-ea16fdc7fd2b | -10.94265 | -48.70869 | 2025-11-19 04:01:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b4ac31-877a-390f-84e0-fc2816767d89 | -10.50476 | -44.03054 | 2025-11-19 04:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10d24a65-9fee-3164-9132-cf9fdab321c3 | -7.94209 | -38.37012 | 2025-11-19 04:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6eb84f89-8e3f-389a-abfb-d43b5a32509d | -10.35453 | -48.92953 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2aa70d44-4826-3d90-81c5-54642dd04a0f | -7.83126 | -42.16426 | 2025-11-19 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bfafffd7-cffe-39f7-8ae1-6da51094054b | -12.59784 | -41.33638 | 2025-11-19 04:01:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c68f5316-a340-3aff-a4b6-a68f4b338e50 | -7.91337 | -42.75868 | 2025-11-19 04:01:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb42a3cb-4c84-3c69-b7ec-8a0f218584e6 | -9.66233 | -43.89465 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26189bc0-e426-3697-8dfd-650b18113b82 | -7.63393 | -42.57873 | 2025-11-19 04:01:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 31f68053-b4ce-3961-a691-40c1c5b5eb8c | -10.11672 | -36.39477 | 2025-11-19 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fa0a678a-bd4b-3380-b7fc-0f95c4fee6b8 | -13.90882 | -45.28911 | 2025-11-19 04:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 00aaef2c-6d38-3ce8-9143-4da18e3a0390 | -7.83468 | -42.16479 | 2025-11-19 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 42a8e887-75c7-3cd2-96c7-5033f2ef014f | -10.1174 | -36.39 | 2025-11-19 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 514940bf-ca23-3c3a-9f14-462801e77f98 | -7.83246 | -42.15677 | 2025-11-19 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4514090d-7746-3a04-a401-b82c00f83473 | -10.74938 | -44.91668 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce22653c-bc99-3850-9485-acbba1d58c85 | -10.03439 | -36.35142 | 2025-11-19 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 94a78a78-3f77-37a7-b3f1-fd8ff6832737 | -10.661 | -49.37195 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9576f32c-3ba7-31bc-8f87-946c39a9a279 | -10.3477 | -48.91118 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e110baf7-49b0-3a1f-b2cc-6205201af55b | -12.59994 | -48.87893 | 2025-11-19 04:01:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27ed5683-004a-3887-8fa4-5d2cfc4a759e | -9.66715 | -43.8941 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9362722-6bc9-3db4-8eb8-feefffecb548 | -9.36924 | -48.40941 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7bbdf878-bf11-3bd9-b086-ed66c76c0b11 | -7.83186 | -42.16052 | 2025-11-19 04:01:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 944d0dcf-3aef-3cc9-9c86-dafc5a9fa8ce | -7.44172 | -45.19769 | 2025-11-19 04:01:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c17a784-59e7-349b-b09b-33cd3ead0edd | -9.38576 | -48.42899 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb00d698-c467-35fa-b7a0-9a6174e4fffe | -7.28075 | -47.90434 | 2025-11-19 04:01:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33693256-d48b-38c4-b2ce-91d17951529f | -12.60087 | -48.87381 | 2025-11-19 04:01:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdf1e676-5128-3b69-b624-ad8ae1c4818d | -10.35366 | -48.90651 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aaa66eca-68f7-3fb6-a54e-3ea020299c73 | -11.78519 | -44.63369 | 2025-11-19 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1700c3a6-a351-31e4-b1a8-4f4bae6a24f3 | -11.27918 | -48.86834 | 2025-11-19 04:01:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c749dd-cf0d-3556-a323-405476028236 | -10.35161 | -48.91766 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5c42565-5ea6-3f0e-8d59-b954ff2d72aa | -8.87783 | -47.32626 | 2025-11-19 04:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3533b161-a3ed-3d89-aa56-dca5839c5bd6 | -13.38159 | -43.61785 | 2025-11-19 04:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c0202a3-9bba-32c4-b725-0b6038067fed | -10.71099 | -45.05053 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7281069-361a-3ef8-bf39-8d1c6514ad40 | -10.61469 | -44.95399 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba9868bb-40f5-38f2-958a-4e82dc99472e | -9.37313 | -48.41561 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54b4a228-53f6-3321-a0b8-0bd15ab33f28 | -8.37105 | -36.05301 | 2025-11-19 04:01:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 444112c5-16d7-3847-8987-e2223a4659ef | -10.65956 | -49.37291 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 28984908-e070-37f5-b796-e92fb1b37d21 | -11.78888 | -44.61178 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 024f86fb-506c-3613-8c23-e09ab963f92d | -10.35263 | -48.91209 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7014f863-7cd5-3344-ae31-875308c30965 | -11.67259 | -47.97463 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 144520bd-1f8d-3e59-836f-6464420ffcc6 | -10.34956 | -48.92881 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8444a5e9-8988-3416-b11f-cb967946f9f4 | -10.91052 | -44.83661 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1566806d-be41-34dc-80f8-2ca6182bcb48 | -10.68343 | -40.3552 | 2025-11-19 04:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| df7d6dcc-2d4c-3d2d-a150-077b9fb8878a | -9.39645 | -48.45341 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b218756-7406-31fe-922f-e4e3135a62ff | -10.66155 | -49.36892 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 367e1d23-d0d0-3162-9266-38a6500f47db | -11.61958 | -43.90891 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e469722-a1b4-38b8-a6b6-57b7430247b4 | -11.78593 | -44.6293 | 2025-11-19 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66833a93-9891-3540-b7ef-c762165eba27 | -10.00911 | -39.18893 | 2025-11-19 04:01:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32916141-b093-3bd6-979f-34d8f599d80e | -10.47283 | -49.18516 | 2025-11-19 04:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b157af89-c89f-3231-a5cb-859587f9a3e0 | -10.77685 | -48.11938 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3759b8f6-0a3f-3b34-a0e3-4c730a78cf49 | -7.73362 | -47.25602 | 2025-11-19 04:01:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460c4554-3d88-38d0-9cb7-b13b1d94b540 | -12.45856 | -54.44824 | 2025-11-19 04:01:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bf584a0-486d-3247-ab87-fdd423ba26f0 | -10.44718 | -49.35607 | 2025-11-19 04:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b24fa62-58d0-3bc0-9f0f-e503b7b23986 | -11.50241 | -48.2326 | 2025-11-19 04:01:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e88cac1-e533-3e6e-8a02-0c28f8532523 | -10.06288 | -47.90688 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bde83a37-451a-39cc-8f32-6d72ed5c3504 | -8.75607 | -44.1717 | 2025-11-19 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 366530de-71ec-3031-89f2-4ac35cb875d1 | -11.78522 | -44.61115 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7ddb028-3f12-348c-a341-b44bc8eb712c | -9.40229 | -48.44876 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e474feea-969b-36c5-985a-1601f1daca9b | -8.39259 | -44.06101 | 2025-11-19 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95193670-632a-33a7-be79-e0df4a80b86c | -9.37702 | -48.42189 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf6cc710-8005-3ddf-8d5a-126736c6828a | -9.66301 | -43.89046 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c45e690a-f691-3d40-bbda-4dc7cadcadec | -10.88006 | -44.07341 | 2025-11-19 04:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d7e0576-7e8a-3de3-889e-e5b4fa210cc0 | -10.66045 | -49.37499 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02645697-da8d-34f1-b154-26cb7397f9b4 | -13.93812 | -47.5089 | 2025-11-19 04:01:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02b665d0-c6c6-36fa-b027-3d9742251738 | -10.74558 | -44.51944 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcfb0e78-3453-3e4b-9163-da02bc557baf | -10.01248 | -39.18946 | 2025-11-19 04:01:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce86870d-4442-3b38-b661-69e3dc29a5cb | -10.7667 | -44.81442 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c755bbb-6f34-3d83-b96f-975b8c61f948 | -9.08464 | -42.71374 | 2025-11-19 04:01:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e027d134-98c3-3cba-9c49-0a3dc7d84ea0 | -8.8124 | -37.34046 | 2025-11-19 04:01:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 752bd8e0-6ee1-35ac-b619-997248e7a443 | -10.50326 | -44.03164 | 2025-11-19 04:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa30a59b-afeb-3f24-af9a-c8ebfc2b524a | -10.34976 | -48.90001 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46695585-26d3-35a4-b3b3-3b57c618a3e8 | -11.79767 | -44.60431 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a12fa54-0c9b-3317-b768-d639d510c8c1 | -10.06006 | -47.90278 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 415405ec-5a6b-31a1-9ae3-3f3ea9ceeb2d | -10.64407 | -44.78162 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaa83114-6788-3893-98e7-9133fbb9f8ee | -11.92938 | -44.22532 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a125cb11-e6a8-3a39-9ba5-90b3b237611f | -11.49406 | -40.60686 | 2025-11-19 04:01:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bc94ef37-becb-36a2-bdbf-81ecc1ddb6ed | -7.84509 | -42.84062 | 2025-11-19 04:01:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0179ebd-de29-361b-bcb1-3afcb455f759 | -11.81378 | -44.6206 | 2025-11-19 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a59a5a05-3693-3782-bf4a-a9f91b1eca90 | -12.53038 | -48.75438 | 2025-11-19 04:01:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f04beacf-b6a9-3af1-88d1-5c88a34b8c81 | -10.78879 | -44.01223 | 2025-11-19 04:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0956f4f6-54e3-3ee7-89dd-af36309835fa | -7.63329 | -42.58266 | 2025-11-19 04:01:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4def12a4-9f8b-3d5f-9fe6-0fea3fca74d9 | -10.61389 | -44.95868 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88e7a405-8621-3293-a54b-60512f13c24c | -12.16278 | -43.98263 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c134b4-1544-3e20-ae55-081d283f467c | -11.35005 | -37.42793 | 2025-11-19 04:01:00 | NOAA-21 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c6818121-f4a9-38ec-8abd-528d38e3a612 | -11.81745 | -44.62123 | 2025-11-19 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e326b46f-1aee-3aa0-bf5a-41791f96a228 | -8.88154 | -47.33176 | 2025-11-19 04:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06d9810f-f07f-3fc4-8b9c-9064d7f2ce0e | -11.66674 | -47.97443 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7e978b5-1e43-36e4-9eba-23488ac40c57 | -8.38441 | -44.06426 | 2025-11-19 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54471729-c01d-3c69-8bdc-bdb7347eb283 | -8.23567 | -39.97985 | 2025-11-19 04:01:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 471a6a9f-7d07-3163-8fee-da718a1ccb05 | -10.91145 | -44.83568 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a132d77e-f4d8-37e8-a2fc-b92fb560d67d | -10.35468 | -48.90093 | 2025-11-19 04:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 09cf9cf6-bdd8-32fd-99db-1230ac68c833 | -11.62014 | -43.90371 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| daf3c8bc-e66f-3d8e-8883-d0ab101759b9 | -10.69662 | -44.79054 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c411af7c-ed62-3914-a4e4-bf0168a523ef | -10.74482 | -44.92064 | 2025-11-19 04:01:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2b13785-918e-316c-8b23-e2a6ea7949f2 | -7.68515 | -42.69043 | 2025-11-19 04:01:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 321bdb1c-ea90-3366-86db-a4f8ebd591b5 | -11.7896 | -44.62993 | 2025-11-19 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a195eae-0bec-3ec4-80be-599246d52e8a | -8.3014 | -42.25473 | 2025-11-19 04:01:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9b4994a-f867-3dac-91ef-5556d84d2ef3 | -8.0379 | -40.95569 | 2025-11-19 04:01:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44e13345-a173-34a4-8bbe-c1847f8ad0f4 | -10.54905 | -44.12094 | 2025-11-19 04:01:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa1e907c-3fe5-35d2-bf9c-610f31c8f98d | -7.42992 | -42.76001 | 2025-11-19 04:01:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
