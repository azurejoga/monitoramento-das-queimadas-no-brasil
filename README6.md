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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e2e8fd9-eb43-3fb5-adb2-3b4d166f376e | -22.03571 | -47.18885 | 2025-11-22 03:59:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c39d5c6-6a12-3536-b3d9-63dda8207617 | -22.56571 | -47.02067 | 2025-11-22 03:59:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e97d431d-0577-3032-83bd-7280073bfdfa | -30.52395 | -51.64465 | 2025-11-22 04:01:00 | NOAA-20 | SERTÃO SANTANA | RIO GRANDE DO SUL | Brasil | 4320552 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| eb855720-3ae9-30e8-bd1a-466787e35acb | -2.9109 | -48.2325 | 2025-11-22 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 73d166cc-32c5-3631-94e0-9728f9beb1a3 | -2.9295 | -48.2103 | 2025-11-22 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| cc3b9c4f-f950-32d5-93e8-ca2db855a24d | -3.8341 | -45.356 | 2025-11-22 04:40:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8c4505e8-111a-3beb-9294-230ff3275b27 | -2.9294 | -48.2319 | 2025-11-22 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 79880350-6fcb-3b7a-8f85-88c4e82b8f90 | -2.9479 | -48.2313 | 2025-11-22 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cfd3380d-fb04-34f5-811d-74f838d84e32 | -4.0382 | -42.5129 | 2025-11-22 04:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 437fb9b1-748c-35c4-8857-3125aa3dc93c | 3.26464 | -51.20061 | 2025-11-22 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b55e596e-7d10-3eca-951c-e1095103a5cf | 3.26812 | -51.20008 | 2025-11-22 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79a7204d-ba73-3722-ab10-a549007910f2 | 2.07549 | -50.83895 | 2025-11-22 04:42:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 89cdd95b-ad73-3712-8101-a02b3111785d | -4.04114 | -42.52342 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| e2fe3973-d583-3c93-8e8f-f51d4495e695 | -3.95019 | -48.08664 | 2025-11-22 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28eecf14-9d72-3a47-880a-a6414dba4caf | -2.92755 | -48.234 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| d89f3bb9-b802-314b-bbd4-76ff9c0dde68 | -1.30694 | -47.89133 | 2025-11-22 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae0524ee-5e34-3282-acdf-8c3f232eeeb0 | -4.73876 | -42.80223 | 2025-11-22 04:44:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb94ca6-30c6-335c-b129-9b2a470b6ee3 | -5.42938 | -40.66573 | 2025-11-22 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2fd5619-eb59-3002-80a2-d59d4eff136a | -3.83584 | -45.34629 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 941b4680-f61b-3cb6-bdef-667d488d4de3 | -4.11845 | -45.72667 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01316163-fe59-34e0-884a-08cd611b2284 | -3.12641 | -44.37538 | 2025-11-22 04:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e02cc3-5ad1-355a-a6c9-ec0e023a6807 | -2.63865 | -47.38242 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0537ca-449a-3b28-b3c4-7a2d9c04c4f3 | -2.92413 | -48.23347 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| f028b2c6-a959-374e-b539-2a02c42c2187 | -1.60039 | -47.02053 | 2025-11-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 949fa8eb-a434-36f9-a8d3-32e8721ae37f | -2.88961 | -48.02651 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 874d1cd7-bafe-392a-9f0e-4bfec1281d2e | -5.75669 | -49.38963 | 2025-11-22 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a258b4-21f2-3612-9252-596809ddac8e | -2.47112 | -47.82923 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09c8be6e-542e-35c2-8658-9d41a3d14f3f | -3.27283 | -42.21252 | 2025-11-22 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6303e7da-398e-39e8-8423-2468423a3fb0 | -2.91967 | -45.01307 | 2025-11-22 04:44:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbe4d7f4-f96b-35ef-9612-f031f8f6861d | -3.83878 | -45.35401 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 925f3553-276d-3351-a6f9-18f5e703bb24 | -0.96856 | -47.56246 | 2025-11-22 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02137e68-faa2-33c7-843f-dc487cfdf779 | -0.9982 | -53.74137 | 2025-11-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09879eba-8ebb-3445-a73f-c6cc492256ab | -2.88902 | -48.03026 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42f3ae28-b754-3e7d-9c5c-55778fb8ad1c | 0.25128 | -50.91868 | 2025-11-22 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66cbfe3c-4fd9-3e5b-92da-2b155371813e | -2.92812 | -48.23031 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| f5cd3b8d-4f08-3300-9c39-7d687cc4329d | -2.92186 | -48.22552 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cf793445-5fc1-34f9-b024-78865ea36c72 | -3.45564 | -47.63004 | 2025-11-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb232dce-53b7-343b-8a64-22709c42f92a | -1.59696 | -46.68536 | 2025-11-22 04:44:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d016043b-0478-3285-9397-47fa9e3f9c2c | -4.04195 | -42.51799 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| c775094d-9497-36b0-92aa-31012a9c8fd4 | -2.93211 | -48.22715 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7cdf9bf-d25d-3e78-9013-85f1c9a31df0 | -5.11116 | -40.73195 | 2025-11-22 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5433f1c-f137-399e-89b6-12f1b9efe4dd | -3.9372 | -47.56121 | 2025-11-22 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d90af4e-9bf6-34db-a938-102c8ce4417f | -4.57005 | -50.31205 | 2025-11-22 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85de3dd1-6048-3ab5-86f4-ca3ca6ff5d8e | -2.9156 | -45.01246 | 2025-11-22 04:44:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d964c642-18f2-35e0-8caa-20d47bccb2a2 | -0.95129 | -47.35365 | 2025-11-22 04:44:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ad5289-4aa8-3676-9f6d-dcc0121a824a | -4.12319 | -45.72615 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f95ab009-f014-324a-8ca3-ace4e96fd32a | -2.53233 | -45.96082 | 2025-11-22 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1eef981-29ec-3e36-b5b1-bb8de8f25513 | -2.69806 | -45.10583 | 2025-11-22 04:44:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9d015e46-80ed-34ea-bbaa-9bca45fe3bed | -3.82058 | -47.47057 | 2025-11-22 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdcc6c6f-ddcd-3ac5-bef5-5c41f9571457 | -4.66489 | -42.60658 | 2025-11-22 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cb70daff-9b2b-3b13-ae7e-0ca7004a2871 | -4.04404 | -42.51888 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 38347cae-21f3-3ccd-b7c8-411952049970 | -3.46311 | -52.23338 | 2025-11-22 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e370071-a8e2-362d-bcd1-d634f84004ff | -5.42993 | -40.66179 | 2025-11-22 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 884cccdc-e239-3ea2-a98b-433235ba1a1d | -3.26788 | -42.21171 | 2025-11-22 04:44:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a8397d8-2413-3fa7-8525-a7ad126a1cc7 | -1.60457 | -47.01704 | 2025-11-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94a9b781-cc52-30b0-8db3-0615f508e304 | -3.83421 | -45.35693 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ff52c688-87b2-3032-9808-2f2ab369a538 | -0.99444 | -53.7407 | 2025-11-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be2db29f-0c64-36cd-b76a-6ed046c9385c | -3.17448 | -48.61211 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 707beaf4-b19e-35e7-a4c7-a76d7a418792 | -3.83933 | -45.35044 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fcb324dc-8dee-3647-88ec-d9d9b9e035b9 | -3.62201 | -41.99612 | 2025-11-22 04:44:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6eb554c-bca1-314c-bb71-9c38f7d55083 | -4.11745 | -50.07532 | 2025-11-22 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cc3ca81-693b-3f2a-8803-55fb825a1e08 | -4.1224 | -45.72728 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0000ea2a-1432-367f-8793-91cdb64fb523 | -2.93097 | -48.23454 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 3b1cebd6-1c8d-32e9-bd23-e6c6e9503600 | -3.76879 | -48.03712 | 2025-11-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a67e250-15ed-3a33-96bc-4f541c001be7 | -3.4662 | -47.63169 | 2025-11-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f352bfc-3f58-3772-8bd5-08f0a2dbf75c | -2.9247 | -48.22977 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b746859e-81b8-34ae-b2e6-48675cd5df8d | -2.484 | -44.24368 | 2025-11-22 04:44:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7fb4817-25d5-32bd-aa84-a7ade4bdee13 | -4.11924 | -45.72557 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea129381-8547-3f84-9c96-5ae8d602cb42 | -4.03624 | -42.52267 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 1da94e74-328c-38c9-83b1-03b337d74777 | -4.02392 | -42.47014 | 2025-11-22 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00d8fee4-d443-3ebc-9519-3ad521bfdf6c | -2.54828 | -45.9585 | 2025-11-22 04:44:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06dbf534-e8f8-3f95-8e10-a00af740d2e2 | -2.69716 | -45.10289 | 2025-11-22 04:44:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6803013c-620e-379f-a03c-75c14cb65ee7 | -3.17392 | -48.61572 | 2025-11-22 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f62c3a7-4f30-3fb6-8ac3-db53ad908d16 | -3.45916 | -47.63057 | 2025-11-22 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e6a8bfe1-823d-3285-97d3-10c6d2004043 | -3.48725 | -54.0365 | 2025-11-22 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61ce0aec-6d94-3135-8d3d-6dcb805e7550 | -4.12076 | -50.07583 | 2025-11-22 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55a62d7b-6981-347f-8d3e-dadd80380f1e | -3.17664 | -46.59007 | 2025-11-22 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c780b244-d637-3f18-a861-18aaf69a763d | -3.24576 | -44.33097 | 2025-11-22 04:44:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca129a9c-e4ba-30f6-9202-08353a6c36ba | -2.92528 | -48.22607 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 25a69967-d2e3-3448-9d37-56f7b663ebf7 | -1.60393 | -47.0211 | 2025-11-22 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 280db267-e546-34a4-844f-c16733c85f57 | -0.9975 | -53.74582 | 2025-11-22 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62a5f173-77ac-3504-8c90-25ab018ca946 | -0.96798 | -47.56622 | 2025-11-22 04:44:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fffb15d-9d2a-3c85-b664-a95bd85fb161 | -5.42884 | -40.66968 | 2025-11-22 04:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 01585d8a-09c9-3ef3-acb1-c26fe42f2d9b | -3.83904 | -45.87749 | 2025-11-22 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7e04a19-5c8a-33b9-b482-dfd7209c18d4 | -3.74804 | -52.07479 | 2025-11-22 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c8720ad-d8eb-3523-aa6d-d2c622ec098b | -4.02803 | -42.47641 | 2025-11-22 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5efad748-fbf4-3158-991d-eaa291b28a1e | -2.48031 | -47.83844 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e36d5c0-16a3-394a-a247-f01f9e7f10df | -4.02883 | -42.47094 | 2025-11-22 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e693cae-6aaa-3297-aa91-0ce36fb0e6e2 | -3.84336 | -45.35106 | 2025-11-22 04:44:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e6c64e-1f74-31e3-a06e-d13d70ffcd9f | -4.12241 | -45.73121 | 2025-11-22 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 208110d3-93eb-3c4b-87df-3005bc453b44 | -2.91787 | -48.22869 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbffac5e-7ffb-36a0-a8af-67318b1abfdb | -1.19284 | -47.54222 | 2025-11-22 04:44:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d5fe036-4558-3b6d-aebf-bba12b61633f | -3.91202 | -46.13786 | 2025-11-22 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcb101f7-fe4e-31bf-bb61-4c50e7d10aac | -2.93439 | -48.23507 | 2025-11-22 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9cb99ce-b21d-33e3-a956-9a3dd019e769 | -4.03705 | -42.51722 | 2025-11-22 04:44:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 0eb5b145-8045-3780-8aaa-ce1452529243 | -5.75332 | -49.38911 | 2025-11-22 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7730660-d0d1-3c7f-8301-b79cb2c8f4bc | -0.42546 | -50.68306 | 2025-11-22 04:44:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b89777-389e-3ca9-84a0-bf8272e9e31d | -2.69662 | -45.1064 | 2025-11-22 04:44:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5f26a21f-01c5-30b6-b090-9b9b005a9359 | -3.62244 | -41.99313 | 2025-11-22 04:44:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fccc06ca-5062-39b0-a7a6-013cd9605444 | -2.48376 | -47.83898 | 2025-11-22 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
