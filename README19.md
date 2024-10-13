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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2e5e851-f4b1-37eb-bc66-2e9cf93160ba | -3.0079 | -54.0378 | 2024-10-13 01:00:18 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8aa2b47-b044-347e-adf7-e2b2f00fc637 | -2.0595 | -50.707401 | 2024-10-13 01:00:21 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fa290b-bc8a-3ae5-9577-bd7c39c1fefe | -2.6641 | -53.342602 | 2024-10-13 01:00:21 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22295e11-f39b-3e4a-ac0b-bd1eea6ecd9d | -2.7325 | -54.3209 | 2024-10-13 01:00:24 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfcb7af-2da0-31f9-9cf1-f4dc2bb75445 | -2.2603 | -53.469501 | 2024-10-13 01:00:28 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab403708-0d3c-3907-aac7-ffb74622d0d8 | -2.2619 | -53.476601 | 2024-10-13 01:00:28 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c899cab7-715b-36ea-8fb6-96ddf461e1e7 | -2.2521 | -53.478802 | 2024-10-13 01:00:28 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eefdbd70-811a-3256-af92-e543047026d7 | -2.3628 | -54.3708 | 2024-10-13 01:00:30 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbb60cf-35b4-3f83-84d9-6696965aac9e | -1.6632 | -52.123199 | 2024-10-13 01:00:33 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15471462-d33b-339b-93a7-df144b189fdc | -1.6647 | -52.130001 | 2024-10-13 01:00:33 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8a63f75-789c-35ab-b34d-47d62a9bcf86 | -1.6663 | -52.136799 | 2024-10-13 01:00:33 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbc3576-68f2-394d-b7e5-5fba12ab84f9 | -1.6549 | -52.132198 | 2024-10-13 01:00:33 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19474b09-2b37-3b78-be58-fc01139c148e | -1.6565 | -52.139 | 2024-10-13 01:00:33 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84de76c1-f27e-368d-b327-cb1ad593c1b3 | -2.1204 | -54.617699 | 2024-10-13 01:00:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8087c4dc-3fd0-3948-bbd0-555552a17f4c | -2.1222 | -54.6255 | 2024-10-13 01:00:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b697fc09-0ac1-3211-adf4-576918c3e61b | -2.124 | -54.633202 | 2024-10-13 01:00:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900fd6b1-90a2-3581-878a-18f1dddbc7fd | -2.1052 | -54.686401 | 2024-10-13 01:00:35 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f365c17-85bb-38ea-ad11-c7f9a0c203dc | -1.4407 | -52.861301 | 2024-10-13 01:00:39 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3fe799-daab-33ce-bcb0-6d618e314dee | -1.4293 | -52.856602 | 2024-10-13 01:00:39 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1472a6f6-8158-3dbc-98d1-4e27d985e4bb | -1.4309 | -52.8634 | 2024-10-13 01:00:39 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc8323be-11dc-3c5b-8326-514dc0ff3d42 | -1.7305 | -54.172501 | 2024-10-13 01:00:39 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0300ef-36ae-3043-b6d9-859e397f9925 | -1.7322 | -54.179901 | 2024-10-13 01:00:39 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96c41df3-1e90-3ae2-8912-155718cc07a1 | -1.9503 | -56.446899 | 2024-10-13 01:00:44 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503bdd66-845b-3b3a-a97e-7d565f75c1ef | -1.9524 | -56.456501 | 2024-10-13 01:00:44 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1783cb-e1c3-3fb7-ae78-27b93b84e4fc | -1.9405 | -56.4491 | 2024-10-13 01:00:44 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1bf2aa9-795f-311b-a090-4da91e22e30a | -1.9427 | -56.458698 | 2024-10-13 01:00:44 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615be285-1c97-3990-afd8-ad4868200776 | -1.1459 | -54.094501 | 2024-10-13 01:00:48 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e133160-de24-3acc-9a19-5d546f802203 | -0.4388 | -52.045799 | 2024-10-13 01:00:52 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6e9202-db2b-3721-80aa-6b6f5543ee20 | -0.4404 | -52.0527 | 2024-10-13 01:00:52 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8f9980-2701-3e42-9be0-6aeda4af841f | -0.4114 | -52.016102 | 2024-10-13 01:00:53 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| adf3471a-be8a-3ab8-b6d4-9a71e10487a4 | -0.1076 | -51.6366 | 2024-10-13 01:00:56 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 507acd8a-8937-3a9b-b578-cba409489855 | -0.1092 | -51.643501 | 2024-10-13 01:00:56 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 95a10a70-1842-39bd-bd78-038f9983dbab | -0.1026 | -51.6595 | 2024-10-13 01:00:56 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 94cf7e11-e1a4-377f-9e58-4715fd5953f6 | 0.7505 | -50.8615 | 2024-10-13 01:01:07 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 403aea55-92d1-303f-a437-28127da44605 | 0.7488 | -50.868801 | 2024-10-13 01:01:07 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 234c88c4-d089-323a-ab52-5a79dd51855d | 1.2393 | -50.7076 | 2024-10-13 01:01:14 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b69ed08a-b6c6-3cb2-a3cd-774c0496f5d8 | 1.1334 | -59.516899 | 2024-10-13 01:01:46 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed2c624-3607-3120-83ca-819d8d1c32b9 | 2.5856 | -60.672298 | 2024-10-13 01:02:14 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e0b147cf-482f-3903-9eee-81469042f44b | -17.87 | -57.41 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7e0b8f-c200-35ce-9ba8-0b0fecbb55db | -17.87 | -57.34 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| be5a6cdd-2133-3a78-aaef-7d02654d61bb | -17.91 | -57.43 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8da1622-fe67-34f4-9365-5cfcbf490dd0 | -17.9 | -57.36 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 77de110b-f425-389f-a6ba-f3a0892c2458 | -17.9 | -57.28 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79558c9b-561b-37aa-bc30-013cf6ae4ed8 | -17.93 | -57.38 | 2024-10-13 01:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 02aca780-0b94-3937-8ede-26d01c6ebca6 | -1.4416 | -52.8646 | 2024-10-13 01:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1fac3a5d-fabe-3f19-b983-ef18cd94aeed | -1.9486 | -56.4496 | 2024-10-13 01:05:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 42a8a25d-e044-3bdd-8190-307d1deacca5 | -2.1508 | -48.8112 | 2024-10-13 01:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| af9d4467-bd90-3867-bd5f-c7a6dfd45fcf | -2.1693 | -48.8108 | 2024-10-13 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e904d136-989a-387c-a443-26dbdd19fcf9 | -3.0731 | -54.2473 | 2024-10-13 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| f6c3312c-06be-3989-b259-067eedc7f297 | -3.0773 | -53.036 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3e0674e7-463c-3f87-ae70-1a5576ffc44b | -3.0915 | -54.2469 | 2024-10-13 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8fe3778c-ff26-3291-ada0-898e91b741e7 | -3.0956 | -53.0559 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 00b9604d-a7e9-38d4-ac99-a16ed2830167 | -3.0957 | -53.0355 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 206.8 |
| 77d91675-5af5-36f2-a244-5698a3acc099 | -3.0957 | -53.0152 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1b5e6b5a-9ad2-3cb3-a8de-b640db23c04d | -3.114 | -53.0554 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e97e129e-fdc7-3946-9122-8584975ac488 | -3.1141 | -53.0351 | 2024-10-13 01:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| fb4c07d7-a101-3b04-90ba-b7b55f11ffba | -3.1791 | -50.476 | 2024-10-13 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 60215880-4bc2-301d-bdda-8826775176ba | -3.1792 | -50.4551 | 2024-10-13 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 8285ea86-ff20-3968-a85b-16ffad40cba7 | -3.2225 | -48.9306 | 2024-10-13 01:05:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 95f09ca1-ee06-30b9-b44e-889e98a2b98f | -3.7128 | -40.7102 | 2024-10-13 01:05:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 6efdaac4-c2dd-34e2-96af-9d4900b6de72 | -4.1148 | -48.2515 | 2024-10-13 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 70e41ec0-e044-33ce-9ddf-42b33bdd7ad1 | -4.1149 | -48.2299 | 2024-10-13 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 743b9625-4067-33dc-9ad2-81958a0e733e | -4.4026 | -49.7563 | 2024-10-13 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8e6b257f-a133-3a38-a4cb-58d967795c30 | -4.8037 | -42.7254 | 2024-10-13 01:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 167baf18-4793-3e07-9835-164a6d2cebf5 | -4.8039 | -42.7019 | 2024-10-13 01:05:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a0fe2743-3b72-3c60-aba1-01377aec37e8 | -5.0713 | -46.8499 | 2024-10-13 01:05:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f8ba2e6a-28f0-35f2-a850-0da04c47ce17 | -6.1299 | -47.2884 | 2024-10-13 01:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 9b1091a9-3ed6-3624-bd71-903333b30a55 | -6.1301 | -47.2664 | 2024-10-13 01:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| c03969cd-38dc-31d7-86d3-a4b002e0e1ba | -6.1487 | -47.2651 | 2024-10-13 01:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| c77fde60-08f0-3305-a2c1-8753069ff61d | -7.3823 | -47.2586 | 2024-10-13 01:05:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 91c1e4c9-52b3-328b-a3dd-b089c875e294 | -7.3657 | -64.6656 | 2024-10-13 01:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| ee6ad21b-02c5-3945-9e64-4f5ea02ea594 | -7.3841 | -64.665 | 2024-10-13 01:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| bba723d3-2720-31e7-bd2f-649af7b55ac6 | -7.6627 | -47.3229 | 2024-10-13 01:05:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0ca5505d-5903-3a32-8143-11b1f0b32c86 | -7.6629 | -47.3009 | 2024-10-13 01:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 62afeef1-75e9-3448-92a9-16a972ae4bd4 | -7.6815 | -47.3213 | 2024-10-13 01:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 3e730847-fa87-34ae-8dec-6af08cecca76 | -7.6817 | -47.2992 | 2024-10-13 01:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 39365dec-cecc-3b13-8a2b-1623605fe5af | -8.0275 | -71.3985 | 2024-10-13 01:05:53 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 45b3fb6e-527c-35fd-929c-a6eb86012345 | -8.7045 | -46.6042 | 2024-10-13 01:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 45c20e9d-65fb-3f35-9dc5-7ee3f752d41e | -9.7359 | -64.2295 | 2024-10-13 01:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 190b44f5-711f-31c9-95ad-943deca335ec | -10.8987 | -44.3352 | 2024-10-13 01:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 456dca4d-fc40-3a04-84d4-244002652ec2 | -10.9311 | -44.6789 | 2024-10-13 01:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 62546b0f-b3bb-3247-b8d5-89e64867724d | -10.9502 | -44.6762 | 2024-10-13 01:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 44e3fe9f-0559-3a3e-a622-16de7ecbd295 | -11.2535 | -50.9036 | 2024-10-13 01:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2869013b-1d47-3018-9e9d-f55025e1436b | -11.6143 | -48.376 | 2024-10-13 01:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9bcc706d-e2bc-324b-8dda-4076f9bc1bb6 | -11.633 | -48.3956 | 2024-10-13 01:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 0c87f64f-e15a-3acf-9966-58cb643dc91c | -11.6334 | -48.3736 | 2024-10-13 01:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 36717d53-c4b3-32dd-b653-5c4a8f7b0a41 | -11.712 | -64.9777 | 2024-10-13 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7a1a1085-f2d4-333f-9529-94dd3b8a0374 | -11.7308 | -64.9769 | 2024-10-13 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 71702147-f35d-3ccf-b55f-64d29db4d111 | -12.2754 | -47.6473 | 2024-10-13 01:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 7bf0c1d0-ca8b-3ba5-871b-2dbbc21f387f | -12.3793 | -63.7294 | 2024-10-13 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| aaffe04a-346b-37f3-a051-f8f7736c4b23 | -12.398 | -63.7475 | 2024-10-13 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 582838d8-e627-3bee-97c9-ac33e9c4df06 | -12.3982 | -63.7284 | 2024-10-13 01:06:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 54c2a80c-b991-3edc-bea0-b557f0094fd1 | -12.9372 | -62.5275 | 2024-10-13 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 35fcd377-b446-3621-91ae-1c0ca3d3f967 | -13.1475 | -62.3215 | 2024-10-13 01:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 212497e7-4682-3be2-a4cd-5f72eb1cb2e1 | -13.7346 | -60.6079 | 2024-10-13 01:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| ef66b196-adb3-3d85-bcd6-c121be636eb3 | -13.7348 | -60.5883 | 2024-10-13 01:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| f062282e-d243-3864-badb-f5cc4a0b433b | -14.7638 | -57.799 | 2024-10-13 01:06:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| f48fb43d-49d0-370b-8d2b-3ed632cc1bd8 | -15.3244 | -41.8911 | 2024-10-13 01:06:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 477bf159-2248-368b-b479-408a49b7ba0d | -15.6419 | -59.9767 | 2024-10-13 01:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 76e7fb9b-5a1d-3480-9b14-92b423639c42 | -15.9435 | -59.1098 | 2024-10-13 01:06:36 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |


[Clique aqui para ver as próximas entradas](README20.md)
