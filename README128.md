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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a975f40-ff11-3564-a744-fb6ad03a83a9 | -4.48021 | -42.89336 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 88c8d08e-fc7f-3134-bda7-c6dce2aafc28 | -4.47708 | -42.8708 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45903924-223b-3d76-8994-b7bd190dbfbc | -4.44566 | -42.91107 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7c515cf2-efe1-3fcf-a79e-d0ca22114b08 | -4.44501 | -42.9066 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7eb3f457-97ae-3396-8cf2-6cf8b408febf | -4.44437 | -42.90211 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f372578-62eb-3cdd-b32a-2ffad76ad0f7 | -4.44372 | -42.89758 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dcba65e9-106e-386e-9cfc-33d3a84fb0eb | -4.44307 | -42.89307 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a514c64-de14-3717-bab2-9985c48c294b | -4.43827 | -42.90297 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 132f63c5-59e6-3518-afed-02e62244006d | -4.43763 | -42.89845 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d454806-e9a3-3221-968a-56d46f29e6af | -4.43698 | -42.8939 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 060a1a77-e387-35df-865d-f20b27a82da5 | -4.43218 | -42.90384 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 00611094-69a1-3398-a26f-1aa21554de8e | -4.43154 | -42.89932 | 2024-10-25 15:35:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 605c8bb4-c15a-30bc-8d70-8e7765e77586 | -4.07476 | -42.89149 | 2024-10-25 15:35:00 | NPP-375 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 189e6ad1-ee9d-33e0-9639-ef0d0fc20444 | -0.524 | -51.8503 | 2024-10-25 15:35:08 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8a788fd4-3b14-30e1-9188-d5f654b81056 | -1.5292 | -55.4108 | 2024-10-25 15:35:14 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2761f208-bb49-3ded-a7b5-55497d1d3223 | -1.7864 | -55.0704 | 2024-10-25 15:35:16 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| afe853d1-6146-3f69-9883-67d18344c950 | -2.1727 | -54.4865 | 2024-10-25 15:35:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3877bc80-38eb-3ae0-b38c-6c5e199a4dc0 | -3.0932 | -53.7239 | 2024-10-25 15:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8cc2dc4a-a263-36f0-ad70-2cef8f06d5eb | -6.5266 | -62.9483 | 2024-10-25 15:35:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2a63518f-6f78-3b34-ab01-102f3b2ff7ac | -6.4967 | -61.4195 | 2024-10-25 15:35:43 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fe771899-716c-32c0-b414-5b30987734ce | -9.2322 | -45.2386 | 2024-10-25 15:35:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 29e8e782-3d0d-3303-a4a4-649a013564a3 | -9.2508 | -45.2592 | 2024-10-25 15:35:58 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 155a3b03-de81-3765-b782-042050642716 | -16.9018 | -57.4699 | 2024-10-25 15:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| ea5dc620-7ce8-304b-8363-be73ed0e8b65 | -17.2177 | -57.3102 | 2024-10-25 15:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 534d7eb4-d767-3619-8280-c0f9f48e7964 | -19.5071 | -56.6619 | 2024-10-25 15:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 5f6122b2-c449-3351-a81f-0d6d1d8833a7 | -19.528 | -56.6171 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| d8c8c2b6-4ead-3220-b29c-6f79768dffb8 | -19.5685 | -56.5904 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.5 |
| 0b527210-68cc-3d73-a8e3-fcd26e21288e | -19.548 | -56.6143 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 85951d4f-e9bb-3f7d-a2e8-51670cdfae6c | -19.6241 | -56.8339 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 2eebb0ad-9e2e-37c1-a1b8-01400937530a | -19.5484 | -56.5932 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| c9ee692d-1ea0-34ad-8c02-0c29a0239d80 | -19.5276 | -56.6381 | 2024-10-25 15:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 9bfbd0af-5569-3943-9bbe-f6c8ab08e4cd | 1.8144 | -50.4673 | 2024-10-25 15:44:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0764f99c-8b87-3f4c-964b-5fc5e470f4a3 | -1.1987 | -56.0653 | 2024-10-25 15:45:12 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9f221ec6-f311-3c9d-9c20-1cfb67ab4eae | -1.5352 | -51.9231 | 2024-10-25 15:45:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 388349a5-cfba-3eb0-9be9-8041c25ecd79 | -1.8973 | -54.6108 | 2024-10-25 15:45:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 367747de-0e3e-3a55-a3ca-8d4ac69992a7 | -1.8972 | -54.6307 | 2024-10-25 15:45:16 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7c72e5b2-fcba-3d96-b03d-243292eaf36a | -9.2322 | -45.2386 | 2024-10-25 15:45:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3f76b0db-bc5d-3c0c-97ca-736856d1d23f | -19.526 | -56.7221 | 2024-10-25 15:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| a6fb46c5-a67e-3601-a089-088ed1512f99 | -1.5352 | -51.9436 | 2024-10-25 15:55:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4707f966-9b68-303d-9c8f-3d01b3eaf51b | -2.1727 | -54.4865 | 2024-10-25 15:55:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 37da7bc2-04df-311a-b4c5-504e3b8795b5 | -2.5699 | -57.0071 | 2024-10-25 15:55:20 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 627bfaaf-e053-32d2-aa48-741ae42c18c0 | -7.62988 | -34.92141 | 2024-10-25 16:03:00 | AQUA_M-T | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 182.4 |
| d120f57c-a96f-3f43-a9e5-fa7f93fbccb8 | -1.2393 | -53.0497 | 2024-10-25 16:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 22237fa1-a131-3649-ba34-402e0f972d4b | -1.7864 | -55.0704 | 2024-10-25 16:05:16 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a84d22b9-4b0a-3fc0-8c5c-95c16c3f0b5d | -2.1727 | -54.4865 | 2024-10-25 16:05:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5d22490a-f298-3fca-bf95-ca5545903fd2 | -6.5266 | -62.9483 | 2024-10-25 16:05:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8e2bd928-de32-38ca-8a9c-c43b8c7a2408 | -2.1727 | -54.4865 | 2024-10-25 16:15:18 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fbd4b6d8-a41f-3188-8f09-bb6b5cd39bcd | -5.2897 | -60.1441 | 2024-10-25 16:15:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9ea34e54-eaf2-3291-aa91-5721d700af3d | -6.5266 | -62.9483 | 2024-10-25 16:15:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 420352c8-cb9f-3755-bd87-1db70768b22c | -3.0343 | -61.673 | 2024-10-25 16:25:23 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e1826660-5c08-30c3-8da0-9e91713936ae | -5.2897 | -60.1441 | 2024-10-25 16:25:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9214de61-b51a-3b2c-9107-607e82344651 | -19.5669 | -56.6744 | 2024-10-25 16:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.7 |
| cee82194-3b9b-339c-9b54-67d918c0c3e4 | -6.4967 | -61.4195 | 2024-10-25 16:35:43 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 41e6dab5-bc64-3e79-94ed-b88d5b4ba6e9 | -19.641 | -56.9988 | 2024-10-25 16:36:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| a8c79607-f7bf-304a-b888-18e1464899b8 | -19.6407 | -57.0197 | 2024-10-25 16:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.8 |
| d436d2f1-e2f6-3a5e-bb1d-773ddd6e8427 | -19.5669 | -56.6744 | 2024-10-25 16:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 6c92619e-e54b-3b46-a081-591a5d7018c7 | -25.40858 | -51.50392 | 2024-10-25 16:45:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b4920c6b-189e-3dba-a502-54edbc4c3eef | -27.04106 | -51.44723 | 2024-10-25 16:45:00 | NOAA-21 | IBICARÉ | SANTA CATARINA | Brasil | 4206801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dd45cdb7-bfe9-3c49-9c53-1f0aec86426b | -26.60783 | -53.13522 | 2024-10-25 16:45:00 | NOAA-21 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bc6db3aa-4009-34d3-87e8-6be93ed6f176 | -23.66498 | -46.58243 | 2024-10-25 16:45:00 | NOAA-21 | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 61e1f662-6db1-360a-a905-0c4be9deaf86 | -23.66224 | -46.58678 | 2024-10-25 16:45:00 | NOAA-21 | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 98c4d3c4-14ed-356b-9284-5d33338e0dce | -27.9297 | -49.32449 | 2024-10-25 16:45:00 | NOAA-21 | URUBICI | SANTA CATARINA | Brasil | 4218905 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a9e79494-c038-3e16-9443-6d69377e3332 | -27.09179 | -48.91086 | 2024-10-25 16:45:00 | NOAA-21 | BRUSQUE | SANTA CATARINA | Brasil | 4202909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 969039f9-44c4-3392-8728-9ad642c4c7f3 | -26.90505 | -48.82607 | 2024-10-25 16:45:00 | NOAA-21 | ILHOTA | SANTA CATARINA | Brasil | 4207106 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a6225e6f-4607-3569-a386-c82cdc0ed5b4 | -26.86213 | -49.09125 | 2024-10-25 16:45:00 | NOAA-21 | BLUMENAU | SANTA CATARINA | Brasil | 4202404 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 627c024d-a74c-3be7-b3be-30a5bcf4f097 | -29.06893 | -49.73252 | 2024-10-25 16:45:00 | NOAA-21 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 14316f38-2ec9-3fd3-b67f-19e0d92c3ca7 | -28.93013 | -49.7995 | 2024-10-25 16:45:00 | NOAA-21 | JACINTO MACHADO | SANTA CATARINA | Brasil | 4208708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8f9785ce-34d8-30d8-8c30-c7b66ed916e1 | -28.92628 | -49.80008 | 2024-10-25 16:45:00 | NOAA-21 | JACINTO MACHADO | SANTA CATARINA | Brasil | 4208708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| a1899361-e199-35b7-9c10-45e12e1b9734 | -28.76329 | -49.74725 | 2024-10-25 16:45:00 | NOAA-21 | MORRO GRANDE | SANTA CATARINA | Brasil | 4211256 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 075d8ca5-3d88-3a2c-8864-6a601fc1e666 | -28.76216 | -49.75029 | 2024-10-25 16:45:00 | NOAA-21 | MORRO GRANDE | SANTA CATARINA | Brasil | 4211256 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 507cad8f-0235-3c46-8fdf-b9f7dba2895a | -28.75409 | -49.64064 | 2024-10-25 16:45:00 | NOAA-21 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 64179072-da1b-3083-860c-d3a261d43dab | -28.75357 | -49.64342 | 2024-10-25 16:45:00 | NOAA-21 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 2a7d9ccf-f660-31c4-bd0c-5086723caeb4 | -28.55021 | -49.14351 | 2024-10-25 16:45:00 | NOAA-21 | TREZE DE MAIO | SANTA CATARINA | Brasil | 4218400 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5348f87c-3239-355a-a47b-7e08a62b8025 | -28.26103 | -49.1475 | 2024-10-25 16:45:00 | NOAA-21 | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0fa59b2c-b128-3f5e-a3ea-7f41fcd62dc3 | -28.48847 | -50.95593 | 2024-10-25 16:45:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 761db9ea-b33d-3887-92e5-b3f710ad0458 | -19.641 | -56.9988 | 2024-10-25 16:46:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 8b85cdd4-3ebf-346f-95b1-f8028fdef6b7 | -19.6407 | -57.0197 | 2024-10-25 16:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| f0f6a50b-1589-3d20-a194-c9448e85ce77 | -19.5669 | -56.6744 | 2024-10-25 16:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 4ff4cd4a-a403-31b4-91be-4d5edaf8e34c | -24.05232 | -53.71493 | 2024-10-25 16:48:00 | NOAA-21 | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 723d980e-a452-36e0-8d28-3426323042b8 | -19.12141 | -50.69003 | 2024-10-25 16:48:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| a115ff76-9744-34ac-b9b4-cf99141f142b | -23.37278 | -51.90673 | 2024-10-25 16:48:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c9aaee8c-a3f7-3ad7-92e3-1bba9baa1c25 | -22.5105 | -53.45755 | 2024-10-25 16:48:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d663c473-5935-309e-aff7-a686533dc3c2 | -20.84678 | -55.86275 | 2024-10-25 16:48:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f733bfe-6ee3-3978-b4bc-d53f087485f6 | -23.85038 | -55.32938 | 2024-10-25 16:48:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| e49f47b6-dd78-3b9f-a39d-809d90de33a4 | -23.82322 | -55.31277 | 2024-10-25 16:48:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a677ed1b-70fd-371e-9969-64ddd845661a | -23.82142 | -55.29398 | 2024-10-25 16:48:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4ea923b5-20ae-3a9e-a4f6-e70f3e01f6f2 | -19.66502 | -56.97926 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 4206984f-f3f5-3d32-8045-2c2369cf67f4 | -19.66465 | -56.97574 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.8 |
| eea7238b-37bc-3b1a-a0fe-e7284c232a4d | -19.62328 | -56.99432 | 2024-10-25 16:48:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 8140a470-1357-3953-b259-8eeb4a642888 | -19.66075 | -56.99035 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.0 |
| c5e7cb8d-c9aa-39b2-a806-48eadb24588f | -19.61987 | -56.99439 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 5602394b-4757-3fd3-a390-676da5dddcaf | -19.65531 | -56.6818 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 161f018a-48a7-3903-a0d2-f706baa49fda | -19.65042 | -56.68572 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 739d6ede-7e99-3029-902d-69b5e3df6b4a | -19.65006 | -56.68237 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 34c51df4-1a91-3ab1-b7fb-94871a374c5c | -19.64517 | -56.68629 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| be58df8c-68fa-3d6d-bd06-b9841a95dd62 | -19.64482 | -56.68294 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| eee59c47-011f-355b-921f-6b69e54f76c3 | -19.62908 | -56.68462 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| b0fa7de0-0b29-3f2d-a744-3d89126b5408 | -19.62383 | -56.68518 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 7ad5da0d-22c3-3375-830d-e92351711f63 | -19.62348 | -56.68182 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| f2877711-c450-3483-be50-fffc132a2aa1 | -19.61859 | -56.68575 | 2024-10-25 16:48:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |


[Clique aqui para ver as próximas entradas](README129.md)
