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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc1f8d82-fcf9-3fdc-a6d5-ded044f07295 | -2.91464 | -48.24723 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70a16bdf-108f-359a-859f-6d83e50e6936 | -2.58607 | -51.92223 | 2025-08-23 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96290258-f108-395a-96e5-da656295f8ef | -1.55596 | -54.54303 | 2025-08-23 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15b4093e-19b9-3bbf-8336-865e02208793 | -2.55057 | -47.71406 | 2025-08-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 568a7b81-d897-39a5-b1a7-0e1cf003a111 | -2.38423 | -47.66456 | 2025-08-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ceab7d2-82e4-3938-9e37-4856bf4922d0 | -3.55441 | -41.62225 | 2025-08-23 04:49:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1220d7e2-0b47-3cf3-9ad6-0caa1165f02b | -1.09341 | -45.84978 | 2025-08-23 04:49:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25380829-5533-3c84-bde5-84a716de5aad | -2.64765 | -48.81044 | 2025-08-23 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1a8d456-aa06-35ba-8a1a-f63e5c27ee44 | -0.75828 | -50.55865 | 2025-08-23 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 602c0938-93be-3070-9d2c-5b8fa2419145 | 1.21303 | -52.57747 | 2025-08-23 04:49:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ad97b68-21c5-36d8-a272-ea67705cc613 | -2.25861 | -47.84986 | 2025-08-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 809bee92-ceb3-30d8-bc35-619b42a9a6b1 | -2.62478 | -46.84614 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 178ea5c4-78b8-3006-bb63-71e18ab38757 | -2.25792 | -47.85447 | 2025-08-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1bc4fdbc-27a5-3fd1-a717-d6026ba40f77 | -2.29878 | -47.99121 | 2025-08-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb445893-cd4c-3a11-b16b-f0ac5bd2c864 | -2.79366 | -49.59874 | 2025-08-23 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87e10b6f-c8f0-36a1-8e58-863c6dbf8aaf | -2.55511 | -47.70994 | 2025-08-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c4c6e40d-b62a-37a3-843e-d8fc3b91ebef | -2.64886 | -48.8133 | 2025-08-23 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b912d598-a05b-367a-b569-c264a0c4d07e | -3.97899 | -43.24347 | 2025-08-23 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68d34e5f-11db-3c87-a533-78038a6b6b6a | -2.70319 | -48.21028 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c113337-701c-33bd-9107-03c73e56d0c0 | -2.4721 | -47.77198 | 2025-08-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bbd6584-7e50-302f-82b0-3ccd9b20b25f | -2.70691 | -48.21087 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb62e47-a532-3938-9948-986728df4d71 | -1.46301 | -54.11961 | 2025-08-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23c68992-de53-3f47-b0ac-cbc7fcfbe5e9 | -2.90723 | -47.76587 | 2025-08-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d8da59f-d105-38b5-b26c-0b4fa6f76523 | -2.77224 | -49.19603 | 2025-08-23 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c411d9-c05e-3bd5-9ba6-e0914ec61722 | -2.44771 | -47.33387 | 2025-08-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e13c107-8a33-3bad-bf2d-9262e7ef7c6a | -2.55439 | -47.71463 | 2025-08-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 073f382d-d24d-35dd-982a-95c5d475b6b6 | -1.70032 | -55.18789 | 2025-08-23 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d80644b1-bfc5-39fb-80da-62fbe02e16ec | -2.44457 | -47.32833 | 2025-08-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fd24798-c344-354f-b806-3f3504d0e2ec | 1.12365 | -52.59104 | 2025-08-23 04:49:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f8dc834-0fd0-393d-baae-6625bf90f20c | -2.29503 | -47.99065 | 2025-08-23 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0a49004-e247-35a4-86e9-e4a1b08fc21f | -2.30517 | -48.14746 | 2025-08-23 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c4f9b5-2c08-3bc7-a0a2-ca14fd5bf29d | -1.56014 | -54.53962 | 2025-08-23 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63dd14c8-e533-3c9a-83b9-3c60b15def75 | -6.3698 | -45.5582 | 2025-08-23 04:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 75d457bb-fab7-3440-80e7-97042123d661 | -6.3887 | -45.5342 | 2025-08-23 04:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 03e0ddfd-3d1a-38cb-bd4f-08e9874428b4 | -7.0164 | -44.6413 | 2025-08-23 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1a829834-996f-3062-ab77-f49c465b2d93 | -6.37 | -45.5356 | 2025-08-23 04:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| fc7b0fdd-0d6f-34a9-b417-d59a48431143 | -9.968 | -60.1937 | 2025-08-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 185.9 |
| ac641f4f-3950-3847-9be7-d41723f056df | -6.6044 | -44.5624 | 2025-08-23 04:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c346aafc-1c4f-3696-9cd5-c7782514310f | -15.2288 | -53.8481 | 2025-08-23 04:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6f0baa51-9a9e-395b-a647-baeb63c2d95b | -14.6706 | -54.9142 | 2025-08-23 04:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2020af84-1602-3115-8a1b-b91fcd300c89 | -9.9681 | -60.1743 | 2025-08-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 05dd9313-82bf-3502-b8cb-aa4b4f2e21c3 | -17.5985 | -46.5481 | 2025-08-23 04:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c53a437e-0902-381c-8938-4333d4d86ed0 | -9.9493 | -60.1947 | 2025-08-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 400.1 |
| 0b4d1835-94a5-382a-bd2c-3763e92a41bb | -12.9921 | -45.2252 | 2025-08-23 04:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| fa46ddc6-87c9-3cbd-9b61-650488ed232c | -9.9495 | -60.1754 | 2025-08-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 205.0 |
| b0523dbe-2330-3f6f-a9c0-6e05a8c47cff | -9.9492 | -60.2141 | 2025-08-23 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ac327200-1665-342a-a2f9-bebd3681f11c | -7.29588 | -59.63884 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f834b73-0383-32de-b616-832cc041f1f6 | -7.07163 | -44.61102 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 837a962e-9030-3c49-b7dd-8a6786958ff9 | -6.74209 | -50.95079 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f81c67a2-68d5-30b3-a014-55c44940acc7 | -7.78996 | -61.57947 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1793aeb8-9d1c-3653-971c-83185eced378 | -6.25705 | -53.67572 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab71c97-b803-3fc5-8354-f895d7dc19ac | -10.75273 | -48.25196 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e17dc029-cf86-37bc-a733-5228702ca959 | -5.80447 | -46.55065 | 2025-08-23 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9fd9981-5b90-339b-96a8-368a330daac3 | -9.17063 | -59.59919 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 863605b6-9d56-372a-bffa-44cf25eed397 | -9.22096 | -59.75509 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2cfaedd-002f-3b6d-b775-fe957966a8d1 | -3.50604 | -49.03559 | 2025-08-23 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4d00af2-6dbc-3e41-83a5-e8f93ff90abd | -6.41473 | -45.4812 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4fc09a8e-c19f-3c55-a505-fabe2e3bafda | -5.90462 | -43.46946 | 2025-08-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd8041d1-1288-358d-b965-37067dd8b998 | -4.95321 | -55.79143 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59b84c95-f86f-3fc9-906e-6d1cac654e04 | -6.06225 | -53.85409 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77ca8b73-0fd1-3b4e-b975-88e12b1eb2be | -6.56924 | -60.05714 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 680c3bc4-f75e-3160-905f-9661b2b400ed | -8.58017 | -55.28487 | 2025-08-23 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6869869e-5936-384e-aa08-18c909a21d4a | -9.02782 | -59.01156 | 2025-08-23 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18243d4b-cc5c-3518-a783-30f272d96c96 | -7.44201 | -60.62496 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f9aba7-a7dd-3633-885f-1f2004bdd11a | -8.30198 | -47.26322 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 782f1f5a-ab4c-369f-bf31-1e5dc9715e81 | -5.10759 | -43.21865 | 2025-08-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff176f4e-b3d4-3934-b66d-45669afbea4d | -7.0386 | -44.66657 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07e636fd-4bbe-3317-b99d-8072a0879aa7 | -4.09086 | -46.92744 | 2025-08-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1d4738-b47c-3f00-8c5e-891fad511960 | -7.02243 | -44.59905 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8a98185-89c5-3aa9-8944-752e691b90b8 | -5.99712 | -53.298 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 652e50d2-e00e-38c2-91f8-85094706dd2c | -6.77097 | -44.31937 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8652a89-eae4-3eb6-8c42-25708cd85e24 | -6.31568 | -43.74762 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee4a7557-436a-33df-b46f-cf68b8e9513c | -7.72821 | -67.06715 | 2025-08-23 04:51:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc1dae06-ea91-3d8e-bb5a-19e80fb33015 | -3.65062 | -48.32787 | 2025-08-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e94a2b5-9c3d-37b3-8b73-64b810967624 | -7.63027 | -45.24269 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba6e9529-b18b-3c18-90ab-30f4284283d2 | -11.13012 | -44.76918 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db5110ec-7fcb-3961-bde3-b37998595eae | -5.74157 | -57.60234 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd4ddc14-6fa3-3962-89d0-06b3ac7f5199 | -5.43388 | -60.16264 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d8e647e-2b66-3226-a2c0-8c67db233596 | -8.30093 | -47.26124 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe900979-b7a7-3641-8fa1-04e49d54696f | -7.18448 | -48.43313 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 539e5fbc-fda6-30dc-867b-e89bd0fc6f20 | -8.65954 | -51.27438 | 2025-08-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 458b471a-3fe5-3562-9a00-dea3863cbfbc | -9.19536 | -59.62033 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba85bee6-acd8-38cd-9a14-c9fe2d9b4613 | -7.78036 | -61.57476 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e2d4a8c-45c8-3fb3-a99f-db73adb87589 | -7.86995 | -46.29251 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da6b9e8b-2481-3ea7-9a73-08ab8da76b73 | -9.58035 | -55.35691 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aa2b993-7727-38b1-9a8e-d9b0bfc7e55e | -4.23334 | -54.92767 | 2025-08-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adff9713-6adb-3b6f-beb8-aeeef1b19845 | -6.37156 | -45.55123 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5d435a42-359a-3b73-b4ab-49c55b434494 | -6.98427 | -44.17953 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94b55ba7-03b9-3911-85d6-d3bf9735277f | -3.2655 | -50.02026 | 2025-08-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b856910-f43b-3508-a49b-03741d80b18e | -9.20886 | -59.45302 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5fab399-2f33-38c5-a2df-4888d25f9998 | -9.20609 | -59.4693 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d2f4259-4579-37a6-830a-5d83d9511cf2 | -5.87715 | -53.62616 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b08442d-9407-39a0-b089-fd5de3cff41a | -7.5456 | -63.8527 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cc713ee-1b24-3570-97c7-6acfdda463b4 | -6.46069 | -53.3999 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4abffbf-f4cd-36b3-83ca-36b5efff908d | -10.75491 | -48.25139 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c80ec54d-5069-3caa-a6e1-0a50a8ec8b00 | -7.57242 | -63.44093 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05fe1589-a211-349e-92b2-10d20cf0b275 | -7.79503 | -61.58031 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0e08784-ad71-34a2-b4a9-501220334b98 | -5.87663 | -57.76636 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ceea99bf-bf3a-3a1a-84f2-2a13fa5dbae0 | -6.72634 | -51.98212 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14893a8f-68bf-331f-8d27-65d8d182c775 | -9.15115 | -59.50615 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |


[Clique aqui para ver as próximas entradas](README37.md)
