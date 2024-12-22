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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2b4c1d8-3619-3692-b897-85cc2442eee0 | -1.8341 | -47.10984 | 2024-12-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e893d152-5053-3107-bc16-2a352364ecf2 | -4.0119 | -38.81133 | 2024-12-22 04:25:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ef04a70-13e1-3c5c-9c40-2919d1860eeb | -2.50104 | -48.0657 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08aa492c-c2c7-3ced-8001-067a406d29a3 | -3.80696 | -46.84847 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7f2b0c-c01f-3cf4-9262-5e0df6f54be5 | -3.75969 | -47.19185 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df996ff1-a67b-32e6-9812-3228d4d16d48 | -3.98329 | -48.39288 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc158184-69a9-39d3-9839-7d6a155c8d21 | -2.71049 | -46.13957 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de976e24-39b3-3aa8-bb59-a67d76f1367b | -2.39585 | -48.10979 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d14f1810-2e06-33f5-a31a-e607e5eb1bd9 | -3.91971 | -46.368 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 838c6099-157a-3297-8a74-6ae1d9c56d1a | -3.97764 | -46.67135 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 221c0d38-f76d-3cde-b07b-2db0f48a7bc4 | -2.45212 | -49.02649 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc2b1fcc-e60c-30b1-abaf-6e22af54a52d | -2.69628 | -46.59948 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25647f51-fd0c-39e7-b27a-0ca4b48a2bb4 | -3.49892 | -51.17844 | 2024-12-22 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c51dfe9-1221-320c-9fcd-22c8289ea82e | -1.41481 | -46.4858 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4f33d63-d199-3691-9126-03d59da481e7 | -2.614 | -47.46582 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 552cc09c-e5ee-3851-9cdf-d718f832b23a | -1.36338 | -53.68637 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35a3770c-49b8-3b0a-9050-0d45bd143b4d | -3.01476 | -46.99566 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7dd8757-7e12-36d8-bc36-4110575a401a | -2.57292 | -49.47663 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ec1cf9-921b-337a-871c-981571e47e53 | -3.9199 | -46.93071 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c68915-14cb-3e9b-879c-dd2029ab0803 | -2.71833 | -46.17611 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac1c007-3a98-3b64-9126-ebeb767d41f5 | -3.91385 | -46.99096 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 510d5587-b348-3c6d-a9f9-e0a4f14607e0 | -1.18962 | -52.54318 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0ca8588-6b25-334f-a04b-672fcd3f9c3a | -4.9571 | -44.0057 | 2024-12-22 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2af84f0e-93f6-333d-ad03-2dc52e3f59ce | -3.80724 | -45.71593 | 2024-12-22 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475c013d-e83b-37fb-bdfc-2446d0eb053a | -3.90551 | -47.00046 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f627f52-2dba-36d6-91cb-026170db6ece | -3.91472 | -46.35664 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7446981f-a188-3d5d-997e-4b1d5902b05f | -3.17822 | -45.97663 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14c87427-d71f-3b83-9891-7020d4656d68 | -1.37532 | -53.70269 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 21876273-ac7e-3e6d-a149-b3a2585602b1 | -3.09334 | -46.56148 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772ece92-ae4e-3cdc-b1ae-6e51f841e2c1 | -2.62862 | -46.11919 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 436d3bc7-9871-3339-a1a6-18ddf0667ac4 | -3.91235 | -46.65412 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd4bf464-7983-3b03-8b0d-aa89d0cfb38e | -3.30521 | -46.29624 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5a74abeb-db8c-33d5-871a-4a8d4379c27c | -2.87447 | -45.93938 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec780561-1dad-3348-8502-e2276329524d | -2.80452 | -46.70958 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 903a978f-3292-31af-abc5-010831e0d0e6 | -3.16332 | -45.96378 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86013aaf-9292-3a52-8029-85bc9d6acad7 | -4.05611 | -47.10033 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5997e963-0b30-30cc-9341-bdb655f10f01 | -3.83168 | -46.69131 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48366e2-f468-365c-8eba-c2f502f259f7 | -1.72929 | -45.8862 | 2024-12-22 04:25:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0afc718a-2fa4-3d35-8566-e27f07d38143 | -3.88713 | -47.03024 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6102685c-2584-34cd-af16-bfadc0bfe437 | -2.14885 | -53.46103 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d8b7772-aaea-3354-8fc5-95f9d609b046 | -3.91718 | -46.9915 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1246b6a6-3a6a-338f-96a0-23b1e9eef596 | -1.70243 | -52.41967 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 769422ea-5950-3730-8533-48eb19b03203 | -4.1039 | -46.82007 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9594f99a-ec34-3097-b437-c5c21c759c96 | -1.37184 | -53.69224 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f09b43f5-a4db-368c-95ac-281e81e1442d | -3.11182 | -48.28498 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c219bd0-473d-3b6f-a5b6-a0fe476b749e | -4.10935 | -46.72096 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b7e496-0b15-3afc-80fa-8a879da5b7af | -3.60326 | -44.79725 | 2024-12-22 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1dcdaf2-85af-3cea-9b8f-699aa9664d12 | -2.81535 | -54.38852 | 2024-12-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2ea3a54-6760-31b2-ab9a-7fd04cb1f5e7 | -3.75019 | -47.18671 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06ded2e2-7b5f-3547-a6f7-e8a56082b431 | -2.69007 | -54.84789 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02bb286a-be89-3a95-a131-a989c3d970f3 | -3.93373 | -46.88613 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8f19332-5afa-3e7f-bddf-1ea859062800 | -4.48173 | -47.14168 | 2024-12-22 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41db10e1-cebf-39dc-8abc-028a3749d216 | -3.92268 | -46.93477 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa3d5ec-fbae-3af4-8ff0-a5808a0c08b7 | -3.94871 | -46.87767 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68dbc073-c898-320a-aa28-71d0391705c5 | -2.84543 | -48.10997 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91d3aba0-12e4-32b5-b42b-e951790e0ec4 | -1.36623 | -53.69482 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 929eaad3-d4dd-3bff-8943-3d67c57087d6 | -3.80901 | -46.70565 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49445c66-0bc6-3106-aa5a-f74865375335 | -3.90996 | -46.99395 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ce18734-f1b4-3fa3-beaa-c8ea46bb6c6c | -3.92387 | -47.01424 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed11e72d-70b5-30ca-855a-5cdc80135cf8 | -2.57433 | -49.46761 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b255ea0-63fc-39e0-9314-bfabf146f2a1 | -3.13927 | -46.35529 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2e16fbd-283c-306d-ad3c-f344d3f1b9a6 | -4.06905 | -50.34661 | 2024-12-22 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3550bd4-c6b3-3e74-ae5d-4c27e5ceb44a | -3.82504 | -46.69028 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20a5da7e-3351-3aa7-be18-9898f006463b | -3.75468 | -47.13651 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31c57640-7029-3fcc-a843-5e8bafdc066e | -4.10445 | -46.81659 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 395083ec-0734-334d-9a5e-22aa4333fc20 | -2.5023 | -49.06505 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef3d7baf-2a6f-3c6d-b350-ae2944f56dd0 | -1.36693 | -53.69684 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b99073ad-47dd-32d7-93d5-337e51d8f96f | -2.69064 | -54.84448 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edbaf888-20db-367a-91c8-82c1f8a711d3 | -4.55888 | -43.29955 | 2024-12-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7f377701-2988-3706-82a1-1fdd8c03e896 | -2.65556 | -46.09858 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74820f55-9768-36bd-8247-b68c6d3d3612 | -3.92985 | -46.88913 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b37bde4-c0c4-3b44-947c-be2e6f279d0f | -4.93338 | -41.32687 | 2024-12-22 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8e94b134-d961-3ac2-b583-0503adb8b04d | -2.50453 | -48.06624 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c06fcf30-a53e-3ac7-b90f-6221ac53495d | -4.01561 | -38.8084 | 2024-12-22 04:25:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd1a03da-0c52-3c9c-bb0c-9207b77a9a15 | -4.52571 | -42.07101 | 2024-12-22 04:25:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14325484-3d4d-3653-8790-d5d069fcd72e | -3.9131 | -46.36699 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1539ca1-7514-35bd-9b4b-f4ca0a2b544a | -2.58208 | -51.92355 | 2024-12-22 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf6aa766-55db-3d5e-82ec-fbc785310f18 | -2.14401 | -53.59352 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a5a539f-95cb-3cc9-b218-16495a1cac91 | -1.29216 | -53.10305 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c722cd91-6af5-3a79-bf3d-1a0e9b63cf9b | -3.44047 | -45.64812 | 2024-12-22 04:25:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e35ee0-7507-3b96-a3c3-633aa820d32b | -4.08334 | -46.1255 | 2024-12-22 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 339718ce-3e58-3694-982b-66e947f939af | -0.35706 | -50.07083 | 2024-12-22 04:25:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be01d3f-ca64-35e6-962d-66afccbc67c8 | -4.09447 | -46.81504 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03b0d08-32f4-30c0-9d1a-bfc87933ccc5 | -2.72576 | -45.93398 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff7a7cb-e08e-3f50-baf5-a893682bacdd | -3.14421 | -46.34543 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04713d7b-5ad2-31e3-b7f9-60fab7c8e5d5 | -3.50348 | -47.19551 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17c1fbd6-033d-3815-b707-831f3eec9320 | -2.58405 | -47.5444 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b33dad7-3052-3d2e-b8d4-f083ffeb4b38 | -4.05723 | -47.09327 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37906b2e-fb78-3482-93e9-3f2cf7a0d4f1 | -2.39294 | -47.08181 | 2024-12-22 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3d2e49-c204-3766-a96f-36f9a43bf4c7 | -4.05555 | -47.10387 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80a9baa1-624b-3ad8-80b6-499ff434f82c | -4.0656 | -47.08371 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bd1545e-9a93-3e85-8fce-25a24b4675e9 | -4.06635 | -43.41396 | 2024-12-22 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0487c5f-6215-3180-8724-29c605f17550 | -3.08947 | -46.56445 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c010a3e-495e-322e-999e-f93412ce1828 | -3.77647 | -47.15081 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b4f3ee53-08c3-3de3-b7d1-63b836b0cb27 | -3.76193 | -47.19949 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19d6b495-770a-3dfd-9b61-6a1b5367d40d | -3.24885 | -50.96591 | 2024-12-22 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 336bf9bc-2ee4-3d48-b7fc-b0f9bf7dc5d5 | -2.14555 | -53.46233 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65ed4f4b-eadc-3194-bbb4-f92ffafff684 | -2.71103 | -46.13612 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70faaac2-9005-3ee5-80c1-5e2836c81acd | -4.00605 | -46.55494 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dc84882-a3df-3ed7-bff5-1ae431b4f3ff | -3.83718 | -46.67796 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
