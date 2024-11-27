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
| 377122fe-d95f-306e-adc9-4482a05cab1e | -3.5879 | -53.2495 | 2024-11-27 00:59:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6aa576-be09-3405-9baf-3e8b50a75547 | -12.025 | -49.5368 | 2024-11-27 00:59:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05fc1d9a-04e5-31e3-89a0-1d4547d68900 | -22.1238 | -49.601002 | 2024-11-27 00:59:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12c7799e-f452-3a59-a518-33af3e3e8f89 | -4.2196 | -50.9011 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed1b9d95-fc12-3557-99b0-ac4938bff048 | -4.2064 | -50.888599 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3012f133-df57-3394-9fa4-79f8d95df180 | -22.1141 | -49.603802 | 2024-11-27 00:59:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 836562aa-ec23-32da-9ca3-0507a94193c5 | -3.1551 | -48.408798 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc92247-0e2f-304b-81e6-fafe31e40deb | -3.5246 | -52.139198 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37dc818e-3faa-388a-85a2-b096e175c0e0 | -18.0217 | -54.005299 | 2024-11-27 00:59:00 | METOP-B | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 335d9c6b-8223-3540-b89e-3023be46ec5f | -4.7212 | -46.5854 | 2024-11-27 00:59:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4434bc3e-561a-31e8-88da-218e02bf1e2c | -3.5373 | -52.149399 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aed24ee-61f2-3b80-8a64-2196f883c30d | -18.0201 | -53.998001 | 2024-11-27 00:59:00 | METOP-B | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 34524e7e-8c0c-3fe5-89bb-42fe0ec301e7 | -3.0512 | -48.529701 | 2024-11-27 00:59:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 253204dd-26bf-3cdf-8391-0554866bfafe | -3.4515 | -50.299999 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 701dee5c-3daf-3df7-b4a1-4718153fa349 | -3.6769 | -53.544701 | 2024-11-27 00:59:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be1e37ab-6157-33ca-b7e4-56e68a5d27e8 | -3.9384 | -47.973301 | 2024-11-27 00:59:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a1f01c-bb61-30da-b45e-94e329c277aa | -3.5974 | -50.3536 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d7ba41-175d-3c6e-8fc1-ff2b0df1e18d | -20.9778 | -47.206299 | 2024-11-27 00:59:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4d2b4c51-bd1a-3229-a727-fcd8ae041c9b | -2.8364 | -46.8269 | 2024-11-27 00:59:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd6c423b-d0ca-3384-8d72-0f32e029d02f | -3.1647 | -48.406502 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1de6932a-663c-3694-987f-350edd11d6bd | -17.2908 | -46.2771 | 2024-11-27 00:59:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e6b7d7bf-2c55-3591-b46d-0ec89721a2f1 | -3.9671 | -48.091702 | 2024-11-27 00:59:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 413c3473-68db-35fc-bfbc-e3d5143121ba | -3.7784 | -52.389599 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903a6197-cf7f-3fbb-bb3a-e1c178fafc60 | -11.9915 | -57.1908 | 2024-11-27 00:59:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d35bd0b-c416-3ae1-9b72-337dc3113cc0 | -3.5305 | -52.164101 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9290719-1bf8-3d5c-b79d-eda7030274af | -3.7121 | -51.798698 | 2024-11-27 00:59:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c4b3fb-7323-38b9-aaf0-2812eb571629 | -17.2812 | -46.2799 | 2024-11-27 00:59:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0e353a4f-3bed-3a9a-a943-0806e0e7bfeb | -3.4983 | -50.497898 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 133d5eba-0c63-3192-90d4-021726fe2a79 | -3.1702 | -48.429401 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a58da4-e765-3c6a-8e31-367416f85bc6 | -3.166 | -48.454498 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8da14bf-237a-3ed7-81a6-f5af4e3447a0 | -11.7802 | -54.689201 | 2024-11-27 00:59:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 383bc171-c66d-3d2d-8fa7-bd4ad1e51cbd | -3.7561 | -51.5919 | 2024-11-27 00:59:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b257e4a-491e-34af-a155-a9d1fb19130d | -17.2293 | -54.427101 | 2024-11-27 00:59:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6cff9a9-c1a0-339a-b4ff-0a844fa04cc4 | -4.714 | -46.5564 | 2024-11-27 00:59:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63d6a53d-c362-3b72-9438-fa4d7dfb84ea | -20.381599 | -47.473301 | 2024-11-27 00:59:00 | METOP-B | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0c27c4f2-1793-3ae7-8064-216acd9791cb | -3.0979 | -50.365002 | 2024-11-27 00:59:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12cf3158-116e-30b2-aa6b-9b2b24a5f1c9 | -4.2161 | -50.886299 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44ff96c4-57cd-3904-886d-353faeca7323 | -3.2511 | -50.623901 | 2024-11-27 00:59:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991a0388-efaf-31c9-8785-5bf627113e6f | -11.7819 | -54.696499 | 2024-11-27 00:59:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3974e87c-b385-31b6-a76c-919abe82bf05 | -3.2473 | -50.6078 | 2024-11-27 00:59:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d58899d-ed19-305e-aeac-a6f962de955e | -22.9883 | -50.390701 | 2024-11-27 00:59:00 | METOP-B | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5284f6a1-3f54-3438-959b-e21619afec3a | -17.7087 | -54.0816 | 2024-11-27 00:59:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 18bd9379-702d-3323-8b07-a67c174b8e9e | -4.2126 | -50.871399 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc6d19c-8bab-39a1-883b-9f856162be63 | -3.5877 | -50.3559 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eaa74c7-ba90-39bd-ac4a-602248cbb803 | -3.9614 | -48.068199 | 2024-11-27 00:59:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17bec9c7-aa33-3610-a4ab-c2b032c7e434 | -20.378 | -47.4594 | 2024-11-27 00:59:00 | METOP-B | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 50f3f046-6437-39cf-9b96-fa2957dbcd9b | -17.2309 | -54.434399 | 2024-11-27 00:59:00 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5982a740-8bd4-3268-bfcc-6a47dc4e755e | -3.7687 | -52.391899 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7245773e-2885-3f5e-9d62-af747d35b9d0 | -16.672001 | -47.229301 | 2024-11-27 00:59:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3b88fb2-9b34-35ca-b512-55fa74d10333 | -20.9741 | -47.192101 | 2024-11-27 00:59:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c3415c4e-47df-3b0e-bcf8-8e6474a0871c | -2.846 | -46.824501 | 2024-11-27 00:59:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd95a64d-fbe6-3478-85ff-195054ee669a | -2.8436 | -46.856701 | 2024-11-27 00:59:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f2ab92-aac7-3293-bfb1-c773be993217 | -22.9904 | -50.3997 | 2024-11-27 00:59:00 | METOP-B | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3906e15a-b8e1-368a-bf7f-0dc2447b7fde | -15.3 | -56.514999 | 2024-11-27 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69ffb468-7482-3d70-9ab0-a409801cbd85 | -3.5137 | -50.303001 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d57f5e28-34c4-3dc9-a9f8-1069c18e8066 | -3.0362 | -48.5093 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17ea4435-c0be-3d46-acce-ca06e775a1d4 | -4.1417 | -43.8135 | 2024-11-27 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| f279cd4b-4b97-3827-8349-b2de31889958 | -1.6629 | -52.454 | 2024-11-27 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c6332ff1-aedb-308c-b7c2-29b0f1b0180f | -1.6813 | -52.4537 | 2024-11-27 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f6848eaa-9e28-3fae-9fc7-63700956857d | -3.0392 | -48.5297 | 2024-11-27 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 7f9680ae-c7a1-3aba-9f68-761639f6d4f9 | -2.8611 | -46.8186 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 639fc0a6-21b5-3c66-b5e2-71e1289f21dc | -2.8425 | -46.8193 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 887a7a99-52a7-3e0f-ab43-39068709491f | -1.9561 | -45.7361 | 2024-11-27 01:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 8f56ee0e-059c-36db-a39b-617f603cc6df | -1.6444 | -52.4951 | 2024-11-27 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ba03d448-db19-3db4-a14d-06d2ee765d75 | -2.6988 | -45.6481 | 2024-11-27 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2c9dd068-98c9-3b59-ab93-a07e536799b2 | -3.541 | -52.1647 | 2024-11-27 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a9ef5be9-78bd-3ac6-91f0-c5a543021b06 | -2.5963 | -53.9771 | 2024-11-27 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 99114a36-a2e5-3c74-998d-43a3b2398a10 | -2.8424 | -46.8413 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 7bb454a5-8fc1-3d33-be57-8446d5ec3ad9 | -3.5411 | -52.1442 | 2024-11-27 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| fbdc63ed-f6cc-349d-b609-07beebead523 | -3.1691 | -48.4394 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 390.9 |
| f9da1373-68d4-36e1-8dc9-70aa85a1f01a | -2.9967 | -45.4809 | 2024-11-27 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| af8d8083-55ee-31d4-b521-a872a31fecd3 | -1.9376 | -45.7141 | 2024-11-27 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b6720bdf-5d5f-33f3-b9be-01b3dfddade5 | -2.9968 | -45.4584 | 2024-11-27 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 5a1dedbe-3262-30ac-bb64-6aa53ddba1bd | -3.9675 | -48.0634 | 2024-11-27 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| e5fde682-2d3f-3154-b5f7-9772156cf100 | -3.0393 | -48.5082 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 702f1fc2-5ae7-37a7-b289-8adb580cff6d | -1.9376 | -45.7365 | 2024-11-27 01:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4d60e458-d7fa-3882-93d2-9ecb0d37ad2b | -4.2114 | -50.899 | 2024-11-27 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 2028b6a4-824e-34fc-b28e-2258c18c84b4 | -5.9788 | -45.3621 | 2024-11-27 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 94d0f572-423e-31b1-ad96-165a1287a1e4 | -1.6629 | -52.4336 | 2024-11-27 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0c1e9393-40d1-3e7c-9122-ea3829923f95 | -4.1419 | -43.7905 | 2024-11-27 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0d4840d0-ebb7-35e3-876b-364c955e79cf | -4.7195 | -46.5827 | 2024-11-27 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b7fd1b47-caef-39d5-8323-c2d6d9b87ef2 | -3.5226 | -52.1448 | 2024-11-27 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| f56038f6-6864-3188-9639-810ca1a172eb | -11.7715 | -54.6828 | 2024-11-27 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1ec10b5a-f6d8-3360-933b-a8f3149293b6 | -4.2237 | -48.6557 | 2024-11-27 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b2914c21-673e-3e03-bd0d-3d4afaf052fa | -4.7383 | -46.5595 | 2024-11-27 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 11f6de88-9f8b-3f07-8533-9d08534e4f4d | -3.1876 | -48.4387 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 212.3 |
| 5ceea164-aa72-387f-89ef-f84ccc39cf59 | -3.5226 | -52.1653 | 2024-11-27 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| bc61f7e4-9ecb-38e3-a110-592ccb405b94 | -4.7381 | -46.5816 | 2024-11-27 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 7e0a618d-bea4-3156-a881-326b9859e728 | -2.824 | -46.8199 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 39852f90-83c2-369b-9783-b3eae6695511 | -3.169 | -48.4609 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8e3e1875-e5f0-3acb-bd88-f603ded75fea | -1.9562 | -45.7137 | 2024-11-27 01:00:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| d60c9128-179f-3e61-a3e7-908ed147cc54 | -2.8347 | -54.1125 | 2024-11-27 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| d47d0bee-cf43-31a6-add0-cc41c2306015 | -11.7713 | -54.7033 | 2024-11-27 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c2a4dae4-720e-3694-94a5-ba55e9615c6c | -4.2115 | -50.8782 | 2024-11-27 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 335b22e8-c209-3737-96b2-6ff7a5b9bebf | -3.9674 | -48.0851 | 2024-11-27 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| c56143a8-720e-3611-9579-9d31e7e4ac68 | -1.6813 | -52.4333 | 2024-11-27 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8fadf367-b6a1-350d-b595-5ae867ea89ef | -4.7197 | -46.5605 | 2024-11-27 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8843b574-f87c-313e-8273-f534dc20fc4e | -2.8239 | -46.8419 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1b04a32b-08d4-362c-a969-d10e84ff16be | -2.1928 | -53.7839 | 2024-11-27 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 71b13e67-3d71-377a-bae1-231b9740e76b | -2.6987 | -45.6705 | 2024-11-27 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |


[Clique aqui para ver as próximas entradas](README10.md)
