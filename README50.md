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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a780cb2-3075-314d-971e-909cf89c483e | -4.63511 | -50.61665 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13ac5696-87d6-3d49-bff0-a9ef5ddf1ab2 | -4.27289 | -50.76208 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a41f7517-2c24-32ae-a9f7-c86f1a02a599 | -4.15533 | -48.89187 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dbd602e-8b02-3a5c-b277-a2dcff5bce30 | -4.31002 | -50.78395 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a6457bc1-ada0-31d8-9c58-4941a4c4fd22 | -2.96944 | -51.02366 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2348e3a-a217-3a15-b886-ed537e509e0b | -4.16114 | -48.90116 | 2026-10-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc607b78-9a20-3566-afde-a72a7a2eae2b | -3.56684 | -51.47786 | 2026-10-01 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0ad5104d-e1d7-3fad-a5ff-c28691a0c976 | -3.16487 | -54.08156 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f08eefa9-8064-35f4-a8a9-2a125518b1db | -4.26596 | -50.7644 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4e2ae814-0a56-31de-bc38-13f08797eb96 | -3.49053 | -54.72868 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52fb4b9f-dff7-3528-9809-b6aec040198a | -5.74106 | -45.16192 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f3b730f-424f-31c4-842b-ef37b2437053 | -5.58289 | -42.73002 | 2026-10-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b7f1f29d-201e-3013-ba66-a17a6dd5514b | -7.02993 | -45.27734 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3b51042-656b-3515-9c18-c045aba82ea6 | -5.74368 | -45.05682 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52036b04-6e68-3643-9e20-7aecb0226710 | -5.22218 | -48.41683 | 2026-10-01 04:32:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91c5176b-0fd4-38c9-a82e-8f02dc0070d2 | -2.85939 | -54.12785 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a363814d-abb5-38ff-b8c2-eb4962868599 | -3.11765 | -50.28624 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c48ef89f-06df-3476-944f-1725ed764902 | -5.1159 | -56.01165 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32ad0df4-8309-37d1-99e7-e986d0a24b71 | -3.09737 | -50.26261 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2728a62-b6dc-3660-8cdc-dea7f5660c88 | -4.30403 | -50.74619 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf31694f-2b1e-354c-95fb-0e1377970e41 | -5.76617 | -45.15488 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c886b025-ad8f-37b2-9bd3-814fdafb531c | -3.16347 | -54.09768 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88f62ce9-cea2-38c3-b328-a23bc7352aa7 | -6.92279 | -44.56455 | 2026-10-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1874d6f0-b3f8-3ea4-b14b-e6b255e016f6 | -5.75166 | -45.15993 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d89374ef-e1df-3ae3-9cf5-9ddc1b1ef15a | -2.99294 | -51.03505 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02cb3413-950b-33c4-999a-b8be6a83fb55 | -4.61691 | -46.47489 | 2026-10-01 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38c7306f-d01f-3e6a-a3d7-c0bb15e7839d | -4.34528 | -47.76677 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15435832-e7b8-3214-9184-ff7cc0f9ce24 | -3.21977 | -54.31623 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34c5c296-c3c5-38a2-95e5-55b23c71f197 | -4.26281 | -50.75864 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| deb6e954-77bb-3546-a18d-4477204df717 | -5.25456 | -43.57812 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91dbe181-0856-3aa2-9394-737c5c0caab5 | -3.11141 | -50.2751 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20bfce49-a1ae-32e7-9d5c-4f40889295f9 | -3.12315 | -50.27695 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e98fec35-e24e-3ac0-9e42-3720446fb96c | -5.12689 | -48.8021 | 2026-10-01 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 861a4e23-b84d-3f7e-a6de-6890983855f0 | -3.07563 | -54.37589 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af849ce7-5caa-3e3d-aa27-3f10541315c4 | -7.02268 | -45.30193 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3f2e983-5ba3-32ee-ac2a-c5875ea12800 | -4.24692 | -50.75617 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd0132eb-24d8-3295-bd76-5a4c27e400b8 | -5.28513 | -45.83855 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0105c5b-c61f-3ee4-be1c-8c0193cd3f10 | -3.16237 | -54.09618 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d988837b-1e37-37d0-a701-d63ecb3d73e3 | -1.83005 | -54.99408 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29c0eeac-4643-3fda-a9fc-329a5f2e6b4f | -2.90693 | -51.32732 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2c6a012-9428-3ed4-8433-e5d568f18d20 | -3.16394 | -54.09476 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d0cf874-dc32-3373-99fd-eb370471ea57 | -3.01403 | -53.88137 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5e80b99-048c-31d7-90cd-a99d921fd750 | -4.28919 | -48.55754 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3166e1e7-9e6a-3df4-bc6a-b63e4756586a | -4.4573 | -47.92059 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5101beac-dd56-395a-8234-f7d4030b97ca | -4.63202 | -50.6111 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba8e550f-6dfc-3beb-b11f-60dc9f6a1fe3 | -4.41083 | -42.13976 | 2026-10-01 04:32:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92c1edfd-17c7-301d-8eb3-80cd1b36f0ce | -3.37856 | -50.94351 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 124c189d-ab40-3323-b46a-962d4c368526 | -4.27998 | -50.76845 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 00f491c6-a7fb-36b5-a3bd-fdeadc31c88b | -6.75514 | -44.74408 | 2026-10-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8485bf8-f0ba-3a6e-8e1b-ef731793dd0c | -1.0848 | -54.11001 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 080dd31e-1378-3527-8f68-0ff9fb8cc6cd | -1.32643 | -49.12982 | 2026-10-01 04:32:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb53b155-70b9-3628-9d21-d16a1651bcf7 | -3.49072 | -54.72917 | 2026-10-01 04:32:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee51d8b-de94-3c90-9c33-0b8f780d213c | -1.90589 | -45.80873 | 2026-10-01 04:32:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b9409f3-0425-3e30-b2bc-4992d5c6ecc2 | -1.67739 | -55.31185 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd37c25-617f-3431-b671-8e2d9132d929 | -4.25391 | -50.75381 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b66ae161-cbc1-398e-bd08-f731e889daad | -4.29829 | -54.79446 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 336374b9-958c-3118-bb55-ea71fd1fca65 | -4.06156 | -51.10223 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3287a750-f880-3025-b152-1df5003073d2 | -1.68074 | -55.31237 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cda4b0a-a375-3860-8e28-1c42a9451cd2 | -2.9853 | -51.03003 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34e1ccca-0efb-3fab-a3bb-52c31ed2c659 | -4.2845 | -50.79029 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 77f76919-be9a-3945-bd77-b1f81811204a | -4.30349 | -50.89845 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec8572b-3f66-3916-ba8a-70ac77b87305 | -5.75056 | -45.167 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c1d9845-40c2-385d-951c-011bc9210d1b | -5.53312 | -50.0429 | 2026-10-01 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f149ce5b-83e9-3327-83b9-d01afd261e53 | -3.59009 | -54.55341 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4fd75e5-6dc6-355c-befd-75094ef17544 | 1.84549 | -55.56623 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30b68ccc-23be-3061-928b-d03ad7bf8781 | -4.28422 | -50.74299 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cab5ba9f-2919-3d7f-83e1-5030566db3e7 | -2.98238 | -51.022 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e68ef08a-aa4d-30b6-95c9-ee74fcacda15 | -4.25788 | -50.75442 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 040d8bdf-9d63-37d2-9b7c-6194c3590db2 | -4.24858 | -50.74594 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93f4032a-ba9b-33a1-bf60-9a0d523f732c | -2.97346 | -51.05087 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a56b63a-3136-3da6-a7f1-38530826c71c | -4.26151 | -50.78136 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 636a5ad3-3fe1-3ba6-bd5d-c8440aeebe57 | 1.87539 | -55.63998 | 2026-10-01 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 230d97ac-2501-3858-9298-40737b86fc23 | -5.12623 | -56.00902 | 2026-10-01 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ccda4409-f12f-3e93-a939-6cf9ba294fab | -5.76005 | -45.17207 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cc7a996-84f7-3c69-b128-3c3a3ea1fc92 | -4.27517 | -50.77283 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| c6c97cab-4425-363a-8531-e52372213650 | -5.75836 | -45.16095 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1851bf1f-647a-3f3d-839f-85e2dc4b45fb | -3.79675 | -50.60661 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| de7a607f-c9d2-3088-9c82-d9d4e24327e0 | -7.02358 | -44.63713 | 2026-10-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c77ade7a-12db-3368-9d3f-c867cbb1b184 | -1.63756 | -55.13276 | 2026-10-01 04:32:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37592d68-8c2f-3a5c-a557-e55cffd93a8d | -4.29948 | -50.89782 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24bb3c9d-af60-3784-ac32-1a6c42f7e3ad | -3.55342 | -48.17865 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0450c007-9b92-37e3-ac45-ecb205b8556b | -4.265 | -50.7958 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51768cdd-d224-3b57-8523-fb14f8a05e2f | -6.7095 | -45.98162 | 2026-10-01 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c41dbaf-48f4-34c3-bf60-b53b8a09ffb2 | -3.16127 | -54.07932 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f402f02e-a341-394b-bf0e-f8cd4edd2544 | -3.10128 | -50.26326 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 680b1218-a4b5-308e-a378-98ef10bf7c6f | -2.90675 | -54.12646 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c39d8e-2723-3fd3-9809-8a66d7f00053 | -7.02937 | -45.28093 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f932352-bfd4-3923-b6db-cc5a8e35fa24 | -4.26129 | -50.74277 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6503bfb7-b0c5-3854-ae46-3eee14484f8f | -5.41393 | -45.9052 | 2026-10-01 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca39f179-40e3-3e6e-8b3a-a3db16f651f9 | -3.10047 | -50.26823 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da8e9ed9-a906-360d-b939-51044639e98a | -2.97055 | -51.04277 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b773817-8f31-3d61-b6bf-98b9e01194de | -7.07275 | -42.85602 | 2026-10-01 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dae289d6-e9ec-3737-afb2-ce6faf936e4b | -3.10981 | -50.28499 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a11bf8cf-fa3b-34ae-b416-150a898317d9 | -2.98351 | -51.04108 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a23059b-0f60-341c-b73e-6c0900b9f1a3 | -4.29667 | -50.76608 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b58d9eeb-0085-364b-b115-e14027374419 | -4.26116 | -50.76896 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 698436d5-3a53-3c2e-bcdd-1401e51e8733 | -0.93998 | -47.55318 | 2026-10-01 04:32:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 322a9cf7-b5ca-3488-a932-d1baab2af23a | -5.32501 | -47.47006 | 2026-10-01 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030406d5-9fd5-3b85-aef8-00a23993b8cb | -3.93137 | -45.42018 | 2026-10-01 04:32:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c4d45e7-4f50-3776-aa98-34c062b3f748 | -4.31254 | -50.76865 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README51.md)
