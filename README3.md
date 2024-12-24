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
| 11efbb88-1801-3116-bb27-7dcc644f293b | -2.9337 | -49.43825 | 2024-12-24 01:04:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a66ecea2-425d-300a-af04-c88a61c6fbe1 | -3.06272 | -53.80116 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a500b712-1e31-3940-8727-3d7c835b9f56 | -4.21664 | -48.4691 | 2024-12-24 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 70b0111a-dd28-3d61-8c9e-c380d144a720 | -3.41854 | -52.85004 | 2024-12-24 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 56249586-5a17-30b8-9dfa-75d5084dd396 | -3.02873 | -53.89167 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b46b9fb5-43fa-3161-b3ef-a40d1ae1d5ae | -2.35032 | -45.5954 | 2024-12-24 01:04:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e2ddd6c1-4e02-3648-ac6e-20adb365dd07 | -2.58391 | -51.81255 | 2024-12-24 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14bf7191-2f6f-3b12-aac3-a4b72ae5a1dd | -3.03002 | -53.90108 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 99409097-93c7-3298-a0a5-14b2e5d370ac | -3.06142 | -53.79179 | 2024-12-24 01:04:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 8beb15b3-d98e-3d9c-85ba-a878a0242982 | -2.76622 | -52.65356 | 2024-12-24 01:04:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88c03787-8b36-35c9-9abd-2a8e6417e0d0 | -3.80973 | -51.02893 | 2024-12-24 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 426dd588-7036-3026-b2e9-41fc36e02d83 | -4.15421 | -49.02795 | 2024-12-24 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aabfc8c3-3bb4-3a80-85fb-a4a1b257222d | -2.9413 | -53.05682 | 2024-12-24 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1480d4bf-b942-3ccf-b117-a2a4e1658eb3 | -2.79849 | -51.76995 | 2024-12-24 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e5f77ae1-d70a-3152-ad2c-1dfdd34ba641 | -2.617 | -51.78971 | 2024-12-24 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6416ecd-11e4-3000-8708-e4adcccf3bff | -3.06872 | -54.64813 | 2024-12-24 01:04:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 91317d60-76e8-37be-b1f9-9999bbaf21a6 | -3.10331 | -54.55044 | 2024-12-24 01:04:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bd970e26-a539-31c7-819d-a15a8286d95e | -3.97878 | -46.35207 | 2024-12-24 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c92423ec-d46b-3d1f-98f6-128d2bbc8a6e | -3.35687 | -52.73202 | 2024-12-24 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6613c44-fb87-347e-a5fe-0310d989735a | -2.76231 | -45.08986 | 2024-12-24 01:04:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1835c95d-aaed-3d28-817d-4769a9c5f4dc | -1.4969 | -55.47765 | 2024-12-24 01:06:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 333d225d-0615-391e-a400-75b80f8c3021 | -1.36078 | -53.68083 | 2024-12-24 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37647673-de04-38dd-a4e2-65dcab4b6da8 | -1.71256 | -54.48426 | 2024-12-24 01:06:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 52ee63ee-a827-3e48-8a05-10a714f6e0ae | -1.75543 | -52.81513 | 2024-12-24 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd55f96f-0b93-3e63-af17-ddb653e4bb77 | -1.58813 | -53.39261 | 2024-12-24 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b444ddd-369f-3432-a24e-5b1bb5e66165 | -1.58071 | -53.33904 | 2024-12-24 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47ddfe53-0b0d-34e8-828f-fb462067d0c8 | -1.71392 | -54.49393 | 2024-12-24 01:06:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63ac17c5-7762-33ec-947d-6c2c138a9d34 | -1.57132 | -47.3562 | 2024-12-24 01:06:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af05fc29-f206-3027-a9fa-c5aa95dbedb5 | -2.22882 | -53.83042 | 2024-12-24 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e0e356c-f42e-3690-8a13-7eb7d156ce7d | -1.58962 | -53.33779 | 2024-12-24 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ad03f44-2deb-3810-9a18-e5c707aa36ea | -1.3556 | -53.7094 | 2024-12-24 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1e0b1d16-dd33-3b49-992d-52de028cff81 | -0.32268 | -48.4311 | 2024-12-24 01:06:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 553c612a-3501-3b9e-84a8-12d1d047f2da | -1.98732 | -54.2164 | 2024-12-24 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5db3960-65f8-3bfe-bfb3-e6e66ab1906e | -9.2158 | -60.336899 | 2024-12-24 01:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1be8933-85c6-3bf8-b80e-b9857148500b | -7.75266 | -34.94109 | 2024-12-24 02:55:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fd257d7a-a5a9-3c69-960d-f3cf20f82aaa | -7.23558 | -37.43172 | 2024-12-24 02:55:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6d2d92dd-2946-3e46-a205-dc12fffc85ca | -7.24114 | -37.43963 | 2024-12-24 02:55:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c0bdbb5b-95fc-31b4-87c2-7b2ed792abe7 | -7.23421 | -37.43533 | 2024-12-24 02:55:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 67fa0183-d832-3a63-9c66-ca82031f35c3 | -9.42862 | -35.51468 | 2024-12-24 02:55:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9f07534-92fb-30b2-abd3-bb56b5966265 | -5.8404 | -35.48491 | 2024-12-24 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8bf77fa8-8629-320f-a2fa-1ffc014c35eb | -7.23448 | -37.43741 | 2024-12-24 02:55:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 903760f1-c7d2-3892-a99e-04ef4d89913d | -9.42785 | -35.51882 | 2024-12-24 02:55:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 49f54edc-76e2-3b4d-81fb-671f0fcf01b0 | -5.84128 | -35.47997 | 2024-12-24 02:55:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 31117337-ad4b-38ab-ad66-8311036e635d | -10.09451 | -36.14858 | 2024-12-24 02:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| c31ff8d9-3d48-3a4a-aa2b-c5bf4773cffd | -7.24089 | -37.43749 | 2024-12-24 02:55:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 70330b3b-c256-33ff-b058-82b5e9242c48 | -10.09876 | -36.159 | 2024-12-24 02:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| aa27beab-522c-33fa-ba1c-907ef34f9797 | -10.09362 | -36.15313 | 2024-12-24 02:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| dea594b2-efa6-320e-b4cf-5fb1cbe8a6d4 | -10.09273 | -36.15769 | 2024-12-24 02:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| fb1e6176-7cf9-35f8-bded-14e5139846bf | -7.74684 | -34.93996 | 2024-12-24 02:55:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bfedd044-dc67-3f93-aaf1-c361255fa716 | -10.49824 | -36.99448 | 2024-12-24 02:57:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9471d6f5-7a7b-3d49-8a43-1b20fcb9b23d | -2.77125 | -45.09867 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9a00ee15-e9c1-3330-af83-fe5565ddb2cb | -3.83899 | -41.55764 | 2024-12-24 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91e29640-8a35-3a5d-9b9c-05f9a8f151ff | -2.77179 | -45.09538 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 74e1d08d-4ca0-35f7-a0a0-7feb2049d111 | -2.34603 | -45.58611 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| af151823-8da5-3cde-acd1-4e49e3cc0c0c | -3.5288 | -38.98725 | 2024-12-24 03:46:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3d09e9e-9b4a-3150-b98b-1da2b169dbbc | -2.99727 | -40.39585 | 2024-12-24 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7722184d-400c-3034-84cd-6d3920bc3318 | -2.21122 | -45.4451 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c4bd414-b424-33a7-8bb1-a7476c50f373 | -2.09368 | -45.35968 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e55d1b24-1788-3edf-acdd-a6aec695705d | -0.93282 | -46.89318 | 2024-12-24 03:46:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f1b82a3-501e-3363-9adf-ac13cc7e706c | -2.9627 | -40.29434 | 2024-12-24 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 747930bf-e512-36a3-830d-6739d2b955db | -2.89278 | -39.95006 | 2024-12-24 03:46:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e0a92fca-af68-3688-aebc-450b86671fdd | -2.09256 | -45.36664 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6bdbe2d3-2125-3ed1-b9e9-d21522967d6a | -3.63937 | -40.48244 | 2024-12-24 03:46:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2dcc794-1ce8-3391-8bea-2cd05b166c07 | -0.93358 | -46.88854 | 2024-12-24 03:46:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51ccf34a-52dc-33ee-9922-2c8bf108bc3d | -2.77071 | -45.10197 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9da4c27c-3af7-372b-bca8-14886224137a | -2.11286 | -45.49037 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05f9ccbe-7f8b-36b9-b228-4e793ad422c3 | -4.31285 | -38.16254 | 2024-12-24 03:46:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 129fdc96-bd52-3b81-aa68-bab8b1efe8cf | -2.77017 | -45.10526 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e436c7ed-fe78-36ca-a519-bc78664ca01e | -3.52942 | -38.98331 | 2024-12-24 03:46:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e4c28e12-b22b-3acb-a9a4-c436351151f8 | -2.76544 | -45.1011 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb6139ca-1976-3112-8ca8-e594187e2797 | -2.34544 | -45.58969 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ac95e788-6c79-33e3-b344-38ff0736f1eb | -2.08768 | -45.36235 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 19b374f7-5e59-3a48-af9e-9ceb287a3ed5 | -2.77232 | -45.0921 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 84fed94f-212b-3943-bdd9-a01afd717b1e | -2.76652 | -45.09452 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 266c7251-f1a6-35c2-b5ec-ef56eef32b94 | -2.29047 | -44.87455 | 2024-12-24 03:46:00 | NOAA-21 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa2f2794-b91d-3c48-aa0d-a70968a757a2 | -2.85287 | -46.74372 | 2024-12-24 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17bfa501-889d-32b9-bcb7-83e5d8077a7d | -2.35092 | -45.5906 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 316dae4a-8c60-37dc-b1f6-514c36a26b8c | -2.09311 | -45.36317 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1477b11d-c54e-3f19-a483-96d366f4b39f | -2.08712 | -45.36581 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 004de97f-dba5-3e2f-a45e-f9d21611c95a | -2.35209 | -45.58345 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 41933c1e-f25c-3619-8f9f-668166491703 | -3.00182 | -40.00525 | 2024-12-24 03:46:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52c84514-a388-3aa4-b138-dd0efdc31eb3 | -2.20939 | -45.44786 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a59dcb8b-38f9-3586-807b-aa8556c98ca8 | -2.89382 | -39.95299 | 2024-12-24 03:46:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ed747c6b-12fa-3eee-8ebb-af8fdf910a66 | -3.8384 | -41.56122 | 2024-12-24 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4596c360-22ff-3dff-98ec-eb4af4b356dc | -2.11775 | -45.49473 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ae132b4-14ae-369f-8ae1-2c01afb79e21 | -0.96214 | -46.78961 | 2024-12-24 03:46:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4847cd3-60bc-3f66-a3f8-5a6ac16e6afc | -2.85875 | -46.74462 | 2024-12-24 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8292f2be-9558-3c9a-b294-95ece8e5128a | -3.64011 | -40.4778 | 2024-12-24 03:46:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0068765b-5190-3b01-9871-a4d39a08bc2f | -2.76598 | -45.0978 | 2024-12-24 03:46:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d3bbe711-cc28-323f-86ba-a73222e1463d | -2.35151 | -45.58703 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b30229c9-68c8-37e3-9e85-f0de32126e3d | -2.08656 | -45.36928 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bcea1ffa-ec3b-3ed0-9e84-3c28e042ce7a | -2.99344 | -40.39528 | 2024-12-24 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 666df97b-d1a2-3dd5-b1b2-8543c0aa0fa8 | -2.89137 | -40.28004 | 2024-12-24 03:46:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d132a90-2001-32c6-ac97-ae14f65d174e | -2.08825 | -45.35884 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6e6c339e-4a46-3a73-9436-26d9714ba959 | -2.34662 | -45.58255 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9deb1278-6c34-3619-b26a-4bd90e597b41 | -0.96288 | -46.78506 | 2024-12-24 03:46:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b23ce436-9216-38c4-838b-498a35e5730f | -2.21064 | -45.44857 | 2024-12-24 03:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7667312a-7f04-35b5-9e6f-e1eb23e8b23c | -2.99419 | -40.39056 | 2024-12-24 03:46:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b4635463-a242-31b0-a4fc-7ec06a292158 | -2.60952 | -45.90976 | 2024-12-24 03:46:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7987c0c2-037d-37ae-be19-ce40958d359a | -3.8378 | -41.56483 | 2024-12-24 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
