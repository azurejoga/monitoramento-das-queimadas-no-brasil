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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c023af5-43cb-335d-ad93-7d85478c9cc1 | -4.03099 | -42.19635 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6266412e-e1f1-312d-932b-6296cf966b83 | -5.15553 | -45.38672 | 2024-11-23 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77216827-a524-31b9-9537-53eaae8cd101 | -4.48006 | -45.65954 | 2024-11-23 04:18:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc16ad7-7803-32e7-a4a9-a17d0a713c90 | -4.65916 | -45.67241 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c9fd9bb-38a0-3b4c-b7c1-8e1221e6948b | -4.41941 | -49.69552 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fce4ac0f-9693-3811-aced-d6431fa39b4a | -6.25364 | -43.56731 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c255538d-6b9e-3b18-827f-c5cc484c7c2d | -3.24955 | -54.22044 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf3aa080-ea35-3f08-9a39-01ea4cf3ad6f | -4.06557 | -48.92684 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd410452-9205-3122-bb0f-cde1dce0a8df | -4.54357 | -45.87634 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0d165b4a-e79a-3153-9b6b-59c9acf32517 | -7.01625 | -39.22523 | 2024-11-23 04:18:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d92abf31-69ed-31ae-852c-6bfc58d4ac69 | -3.19001 | -54.32809 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0111d1f5-3626-337f-be8d-6fe33fe06b31 | -4.08846 | -47.03584 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8006476-18d3-39f4-83ea-3686ec8b9248 | -4.66533 | -45.67705 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00849731-3e03-39cc-9fba-1b73419d47ee | -5.56427 | -46.29101 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d6142c-4be8-3e2f-8e28-cb59606687af | -3.47208 | -47.68558 | 2024-11-23 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4cce5ff-e6a8-3a6a-9990-80060401a482 | -4.39695 | -44.2117 | 2024-11-23 04:18:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d9e36d6-2bdf-3c30-bf96-886b88502cb3 | -4.06362 | -45.20454 | 2024-11-23 04:18:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ea205e4-38ca-312c-9d84-e70df6ec1fcd | -3.88571 | -46.67369 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566b7c86-ef55-3eb8-bdd3-b5dd48af5df2 | -3.67258 | -47.13672 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0142d6f4-05fd-3273-82f6-0661b2061dca | -4.54239 | -45.88369 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b2dd4b1-4225-3be5-a7b5-30124ad1d6fc | -7.07436 | -49.21329 | 2024-11-23 04:18:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2093983e-3c7a-3743-87dd-e7d96ad63187 | -4.55407 | -45.81097 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddf19770-f84c-33ab-a318-ba4816aa3643 | -3.11965 | -53.10447 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0fe7dc02-5365-3378-80ed-8dd89544bb5f | -5.20314 | -46.81572 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8b8788ef-041a-3fa5-9482-75546f5f445e | -3.86683 | -51.25499 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8be4dbd5-b84a-30b6-987d-fdf2898a45df | -6.2497 | -43.54865 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7956311-8932-30ed-abd8-41bce8e1b44c | -3.24632 | -54.24477 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 68b42ef3-b49a-3778-bf8d-de24ab781a1c | -4.95378 | -45.43837 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb878691-05fb-3074-bb8f-0dd4f37efea9 | -7.19216 | -46.2493 | 2024-11-23 04:18:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1fe14d9e-56b6-303e-85ba-5f93e5f20bbf | -6.03183 | -42.23526 | 2024-11-23 04:18:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64dc2369-a5bc-3ca9-b4ea-b5b0afa8de63 | -3.97957 | -49.01522 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef357ef7-8931-339f-bebe-648bb9dba233 | -5.66741 | -42.96611 | 2024-11-23 04:18:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b86f399d-e16d-3d24-86f9-158038ee1beb | -4.11074 | -42.47494 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 90d1e064-873c-3eea-b0fb-7f1e67e6e671 | -4.12494 | -49.40382 | 2024-11-23 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 066b1acc-21de-3b90-a852-a83f560c0ef5 | -5.93102 | -43.78672 | 2024-11-23 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67da58f7-16ff-3a39-b2b9-886ffbe243d7 | -4.43992 | -49.83897 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cfdd3e9-1a29-3c1c-b00e-b14d8c6aa21e | -6.35183 | -39.79331 | 2024-11-23 04:18:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 83880f1d-2d28-319e-abe7-d9f579379b49 | -2.89474 | -53.04572 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdbdaf35-c448-356d-9fb6-b61fac71161f | -3.05943 | -53.2844 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 54b6aade-0e33-350a-8cf2-633893dcbcdc | -4.10396 | -42.4739 | 2024-11-23 04:18:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ea28bfc9-da93-32de-8d23-c72c1587ee78 | -3.23399 | -54.2429 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74aad41f-afdb-3ed9-8a18-1e0f6b80c399 | -3.93467 | -47.02028 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf772b9e-bb51-3877-904c-286d1ea978ca | -3.92294 | -45.3639 | 2024-11-23 04:18:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76871960-4e66-36fd-8337-03737a718e0c | -5.32629 | -44.78206 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c80af6c-0e20-31eb-96dd-1e4d76ceecce | -5.92992 | -44.72549 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48bc8720-e153-36c3-9d70-5ba9d27f0e1b | -3.24888 | -54.22447 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2062c08e-4bbb-33ea-bf98-7461f91986b5 | -4.41263 | -44.11194 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ea3845-953b-34e0-a33e-0767c657118f | -4.44053 | -49.73319 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8831e57b-1b1c-37d5-a26a-8527c83a5b97 | -3.3105 | -46.66778 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5f28175-ce30-37ea-a0da-5e2bc4aa2fa9 | -3.79728 | -51.75965 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1f0c3d2-2ce2-3809-b865-01ecd1b545da | -4.52952 | -42.91018 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e783d9d6-9e6b-399c-a11e-ae17dad973b4 | -4.52896 | -42.91375 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 51812fb8-151f-36f3-803d-3567f949299c | -6.49939 | -47.04393 | 2024-11-23 04:18:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3d67de5d-082f-3a80-b119-609c770653ce | -4.40851 | -46.14949 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10a59a02-4798-3c68-94e2-2cd02e3f58e1 | -4.1611 | -46.80831 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7f8ade5-1cd8-3958-bc5b-fc7f2464559e | -3.24776 | -54.23642 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68803469-1ebc-34c7-9eff-bb7973548c58 | -6.29821 | -35.05943 | 2024-11-23 04:18:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eb413e58-8c6c-3186-bcfc-bc1dbb9a3409 | -5.33118 | -43.49657 | 2024-11-23 04:18:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65c818c-dfe1-3e0f-b681-e7a59e15ba43 | -4.03679 | -46.19521 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b2e32d5-3b7a-3d6d-a1c1-527c46059e4d | -5.32736 | -42.71445 | 2024-11-23 04:18:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 66fbdbfb-d55f-3294-9d3a-0b5ecbc932a9 | -7.30268 | -39.62477 | 2024-11-23 04:18:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 269593ed-ea51-3d0e-bfe5-16af898e8543 | -5.27604 | -45.18672 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c73d81de-3dbe-3678-83b6-fdb374d9d1a6 | -4.69731 | -45.85598 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4f4db010-8112-3ed2-b0b0-0b5480b59d19 | -4.26966 | -46.29242 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cb2a66-e339-3385-aa7f-49cc766cc75b | -4.70467 | -45.85337 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e063ac90-a8f3-3541-9d6e-f55b608062ee | -4.04774 | -48.32644 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4045530-9852-3405-af23-3374cc886b7b | -3.67234 | -51.74166 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a0968f2-312d-39bf-89a2-6d0cedcf5e75 | -5.23004 | -45.1116 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aeaa98e-7ac8-3a09-a792-0f33eb6f48f9 | -3.23027 | -54.22964 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5357ee35-6c46-36f9-9c1a-ae0a76a2c4f9 | -6.46062 | -46.30059 | 2024-11-23 04:18:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d17c8ff7-56d7-3f89-855f-783e4052b148 | -5.22223 | -46.76344 | 2024-11-23 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc20dbec-152b-3256-a1cb-9264eca79d19 | -3.70763 | -47.61637 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 341eee4a-93f0-39d8-9817-af44929b05a4 | -4.5256 | -42.91323 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 150b89eb-30d5-3fa0-a517-26110a63d094 | -3.23203 | -53.94035 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647bb4cb-e6ad-3af9-b3a9-24fa49a5e662 | -3.30004 | -52.57562 | 2024-11-23 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de2e2883-2c7c-35ad-811b-241d46c3dfca | -3.24822 | -54.22849 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cbdad43-e045-3742-ad52-b46d09d0f8dc | -3.22034 | -54.25364 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0fb25fd-1075-3da6-a993-e3a04fb28b56 | -3.96557 | -46.6467 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 157644e8-b555-362e-bcd6-fc324713a46f | -3.12784 | -49.40501 | 2024-11-23 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8703fbb4-486d-3498-a8bb-1b0257d66eeb | -3.24524 | -50.12027 | 2024-11-23 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 41dd99e4-b2db-395a-bdc7-6a32754057bc | -4.5284 | -42.91732 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a88c8ce-6527-3d3e-b90b-88112b021b7b | -3.96366 | -46.7296 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca27ff20-cf15-390d-ade1-f7dd67f0c5fa | -3.79874 | -46.6052 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26726b83-452c-320b-b6cf-ba27a1208f0b | -4.25372 | -48.71163 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03b65d00-26ae-300b-9b8c-e9c918efb99d | -4.34528 | -45.88671 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35bda5e0-8d61-3031-a995-91e15cd8ab02 | -4.66647 | -45.66983 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89ce890e-2b85-3346-98da-35d53056bb94 | -9.72549 | -37.0284 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a876a55d-32b0-3ed5-abb7-eb8d04bb23ce | -3.70256 | -47.61772 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0819df71-fb59-338f-b0e6-c9a374d59e01 | -3.99879 | -46.93927 | 2024-11-23 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e373b2c2-001b-3a73-9cbd-39d70abc9cf6 | -6.42022 | -39.57785 | 2024-11-23 04:18:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 763478ee-864d-3cc0-83a9-bebda808fbbd | -3.81121 | -51.99704 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1eb2d63a-7ac5-3e6b-b309-812f83f9c25d | -3.91126 | -46.4708 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2f2da41-6955-3fa2-8ed3-93d12c8b33a8 | -5.65757 | -45.20115 | 2024-11-23 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa4b535b-65ce-3d9e-b82c-e07274a76d88 | -3.96998 | -46.64643 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 149a231d-53d6-3616-943b-b2c38aacae39 | -5.56767 | -46.29159 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10f6695f-61de-31a1-a969-892296e89182 | -4.69249 | -44.40684 | 2024-11-23 04:18:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c352eb8-6542-3a8c-a62e-75b689350961 | -3.80226 | -46.60567 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35bc69b1-20db-38ba-b948-a95a27618c88 | -4.15175 | -50.08993 | 2024-11-23 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 348d43ff-9def-3ea1-8e0a-fbe72b579cc2 | -3.25212 | -54.24549 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff43a3b7-67d1-32e8-9f79-8caf3ceca877 | -5.96843 | -46.30623 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
