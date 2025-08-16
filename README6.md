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
| c114c714-78dd-3354-976e-cdc3109b6dba | -6.9303 | -59.5305 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| de3d6a45-6556-3f97-ba64-d7956bccf706 | -7.0404 | -59.6222 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5d10d430-1d1d-30d5-ba0b-fdd852ea1be7 | -9.4992 | -60.547 | 2025-08-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| babb3673-e4c6-3c65-a928-968f96b41bbd | -8.9706 | -61.7224 | 2025-08-16 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3a9e4639-4144-36f3-bfb9-857def7474c2 | -13.1077 | -57.131 | 2025-08-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 440db009-abb3-3540-a48c-1484989a1529 | -13.1265 | -57.1494 | 2025-08-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| cb085724-5ae7-3cee-af6b-242fe01acc27 | -6.6326 | -60.0224 | 2025-08-16 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d685df76-7efe-34d2-8cfb-52f5dfe9ab70 | -7.8247 | -61.3327 | 2025-08-16 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 5789c217-555a-3a74-8f37-1b8e7c40448e | -9.4991 | -60.5663 | 2025-08-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b417bb62-a65c-32c8-8cf7-6205b520143b | -8.9893 | -61.7024 | 2025-08-16 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 00723d65-aaeb-31e2-bcee-4a4d20385803 | -9.0531 | -67.4265 | 2025-08-16 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9096cdbe-0a3d-322d-8754-9335a19746ab | -11.2596 | -50.4767 | 2025-08-16 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| feea60e7-fdf5-3490-a72c-40c65f19c9c8 | -7.9334 | -61.7281 | 2025-08-16 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e19954c7-6218-3e61-9bc2-ec399c802774 | -7.9149 | -61.7288 | 2025-08-16 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 0fa20680-dbb9-3b6b-b712-0102a3756242 | -7.9333 | -61.7471 | 2025-08-16 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c4b8b140-bc76-3489-8dfa-c4e60c9a87c4 | -6.5638 | -43.0357 | 2025-08-16 00:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 189c1d5e-ba54-39cd-aa20-6c5f98e8805c | -13.1074 | -57.1511 | 2025-08-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 72a25ab9-c372-3ea5-b8bf-439dc26c8548 | -9.0346 | -67.427 | 2025-08-16 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0345e5dd-5fea-35cb-bebb-f4303c8d4904 | -9.1523 | -59.6384 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 35b7b241-7b32-3b64-b6e4-437a33ae8bfa | -13.4375 | -56.6775 | 2025-08-16 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 16737892-306a-3286-8a6f-3b72e715fb9b | -4.91495 | -43.26463 | 2025-08-16 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 43bd07ed-5a6c-3e2f-97c6-fd069dab0f92 | -4.07975 | -48.04092 | 2025-08-16 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f640944-c440-3a40-8ff9-f865e8dbd5c4 | -4.91296 | -43.25091 | 2025-08-16 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b4283e53-c5b5-3bdc-bd78-9d06fc04142b | -4.92383 | -43.24921 | 2025-08-16 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5816b958-cd5f-374e-8ac3-0360ff7d7bfb | -5.19981 | -46.10041 | 2025-08-16 00:30:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f4cbea9-3d8c-3638-b7b5-fc8caa4187f4 | -3.37723 | -52.71395 | 2025-08-16 00:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| d45217ad-9ddd-3676-8199-0f5ff80ec010 | -3.82543 | -47.74509 | 2025-08-16 00:30:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a58c2598-fd9a-33fe-87ec-44fed22a27ee | -4.22416 | -47.22015 | 2025-08-16 00:30:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee250142-43e6-35e9-93ed-8861a2f0d57c | -3.37923 | -52.72862 | 2025-08-16 00:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 73005deb-b425-3171-a61b-965a4c0f777c | -4.45814 | -44.14463 | 2025-08-16 00:30:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 87e38d35-cbe9-3b00-a782-d7af667caeeb | -3.43517 | -49.04971 | 2025-08-16 00:30:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0866aa4d-2ea8-380f-9f59-b99fe013101c | -5.44863 | -43.58159 | 2025-08-16 00:30:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f0a25459-c3c9-3db2-89b6-95dc15538f4c | -5.19848 | -46.09098 | 2025-08-16 00:30:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 7b9b71b3-09f6-32d1-a979-1ae828dc240e | -3.98474 | -47.88971 | 2025-08-16 00:30:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b69521bd-c904-369b-b19d-bd1e21cb9461 | -4.77951 | -45.33125 | 2025-08-16 00:30:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7f885272-ba99-3e76-8894-5347c2e58d73 | -3.98181 | -43.25031 | 2025-08-16 00:30:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 99c3ece7-28c0-3983-98db-f398b2c418b4 | -2.39056 | -47.62564 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdc875ec-3a24-3572-87f0-2209d0ea27d1 | -2.48061 | -47.2098 | 2025-08-16 00:30:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f6dcc77-7b6a-3954-b393-2195b8e8b638 | -4.29389 | -48.06157 | 2025-08-16 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 677a31ea-a86d-346f-8088-3aeebcaa6e9a | -2.37776 | -47.66352 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| befba118-6a6e-3daf-aa52-639e5194bcfb | -4.78385 | -45.32481 | 2025-08-16 00:30:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d16506df-044f-362a-b830-de2d73817cb7 | -4.60199 | -43.31534 | 2025-08-16 00:30:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f9907b8f-faa6-3e13-a571-6131af4e3ffb | -2.38785 | -47.67111 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| eba13bed-fa9f-356b-acd1-f19fe61a7576 | -5.7603 | -46.67926 | 2025-08-16 00:30:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 67dc7b38-1260-3deb-bab0-69ebba6f62d5 | -2.54261 | -47.71807 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd505370-4825-3816-a622-eec6128cd6c8 | -2.38662 | -47.66227 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6f588f3f-97a4-388b-8b18-da6888248622 | -4.14433 | -46.45753 | 2025-08-16 00:30:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2b73b0fd-468b-350b-8d42-689edaa12dcf | -4.92581 | -43.26297 | 2025-08-16 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f06b0485-9d3b-3d1c-a469-90d878a8bc67 | -3.97973 | -43.23599 | 2025-08-16 00:30:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0e31ba98-2b45-3a5a-ba78-6e49d26f8169 | -2.54384 | -47.72689 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6169225c-e450-3c43-9c11-827b77825ed5 | -3.82421 | -47.7363 | 2025-08-16 00:30:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 4d0c86e3-2ef2-34cc-99ff-758185238980 | -5.75904 | -46.67029 | 2025-08-16 00:30:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8d227073-1804-3a6a-b75e-4b96e3a17606 | -3.23739 | -50.80675 | 2025-08-16 00:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa314472-ac19-3f90-a8d1-4008c4522ecf | -2.77364 | -49.19406 | 2025-08-16 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d6a984a-8d9c-3584-bda7-eb6487a5aedd | -2.37899 | -47.67236 | 2025-08-16 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0c4b361b-6f64-34cb-b751-2319879daf59 | -5.2664 | -50.76307 | 2025-08-16 00:30:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2f8808be-889e-37e3-9480-0920f0b6f268 | -2.82174 | -49.00584 | 2025-08-16 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a67b023-16d5-33c4-a145-7da25abb3a08 | -9.0531 | -67.4265 | 2025-08-16 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e908ea30-6e8f-3296-afb7-899fb3f90246 | -9.1711 | -59.618 | 2025-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 07dcaf51-f07f-30ed-8226-ca350bfdf97d | -8.9893 | -61.7024 | 2025-08-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 05c9c387-5fce-3ee8-9940-7590de9c724a | -6.9303 | -59.5305 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6c82b572-1d8a-3e82-8a24-9c821c289830 | -11.2596 | -50.4767 | 2025-08-16 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 1d34a540-5fac-34f0-a27a-75fb1bd84131 | -9.1708 | -59.6568 | 2025-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 3de5ccb7-862b-34ec-bd8d-18f65f35c6d0 | -13.1074 | -57.1511 | 2025-08-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 18a60321-ff68-381f-aad9-a6781c54180d | -7.0404 | -59.6222 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1d2cb5a8-ac8a-31e6-8883-c9a7e7b849e3 | -14.9245 | -54.7189 | 2025-08-16 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4c52a30f-52be-332e-9612-af7412bbb7f1 | -11.3466 | -55.4326 | 2025-08-16 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| aea24907-8442-3d01-a524-1e83c40538c5 | -7.8247 | -61.3327 | 2025-08-16 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8743b23b-0649-3328-b6e8-937391635271 | -9.2082 | -59.6354 | 2025-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1bb7e4f3-98a1-35fb-9c2b-22d54b85cc29 | -6.5638 | -43.0357 | 2025-08-16 00:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a2fc86e1-3070-3080-8d9d-ec29e8cdcf23 | -13.1077 | -57.131 | 2025-08-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| d1f04d6a-8efc-3ec6-aea8-aa98119b5af6 | -13.1265 | -57.1494 | 2025-08-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f868714c-d84d-3d5f-bc02-24f829232715 | -9.518 | -60.5268 | 2025-08-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2f8ff60f-b8ab-3c66-8cfd-5ad80cb52d1b | -11.3468 | -55.4124 | 2025-08-16 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| adf6e315-b6a8-3c62-89f3-5b9421fb7924 | -6.49 | -62.9306 | 2025-08-16 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 447e8536-827f-3bdd-88a9-feeae934c435 | -9.4994 | -60.5278 | 2025-08-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 2da8f54f-2fa2-346b-ada6-96733ce1a72e | -14.6023 | -47.9018 | 2025-08-16 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9657a95d-3d3f-39dc-ba7b-bef79d1604a6 | -3.8209 | -47.7444 | 2025-08-16 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f5c6b179-90ae-3c8a-a74b-179d432f459f | -11.2786 | -50.4746 | 2025-08-16 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 70d90d66-0f9b-3624-b60c-a0692af98702 | -6.9487 | -59.5297 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 2d50aad8-0987-3725-9491-9fb714486944 | -9.5179 | -60.5461 | 2025-08-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| fb634b5c-a625-347e-968d-958e60c29c04 | -6.9486 | -59.549 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| ba1f622d-f5dd-3a69-b5a0-0b3d2533b8bf | -2.3763 | -47.6636 | 2025-08-16 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| a719f46a-5697-35bc-b51a-a5b2d4267133 | -13.1267 | -57.1293 | 2025-08-16 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| f03744bb-1dac-3354-824e-de2d69a6bce8 | -14.9441 | -54.6959 | 2025-08-16 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8f72cff5-1e5e-3a19-aad6-9a39a8fcd2bf | -8.9709 | -61.6842 | 2025-08-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 2a9dc856-5764-329f-8062-7afad609c3b3 | -14.5828 | -47.905 | 2025-08-16 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| e4413cfc-bf85-38f0-a8c9-a5d615c39a09 | -7.5292 | -61.3254 | 2025-08-16 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3420c916-cbee-3f2d-ac69-786e2d730ffb | -8.9523 | -61.685 | 2025-08-16 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| a92cbf4e-fa0f-3b16-b277-86f7b3cc9186 | -14.6018 | -47.9243 | 2025-08-16 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 081e3e72-d782-3cf5-a2da-106b4fc3c1f0 | -9.1523 | -59.6384 | 2025-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d447eb8b-952f-3fdf-b7e7-4115bb7bde38 | -9.4992 | -60.547 | 2025-08-16 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 74bf0b47-d407-3834-837b-f5cae818cc6b | -7.9149 | -61.7288 | 2025-08-16 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| cf53b2a3-9973-3d5d-98c5-cf94609c1a5c | -9.1709 | -59.6374 | 2025-08-16 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 93663e09-c5e7-36df-917e-98b05e0c72dc | -7.0797 | -59.2157 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 88eaf1f7-0657-38f6-99af-ab5ea5e84f78 | -18.0467 | -47.7253 | 2025-08-16 00:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 69d040a5-26a5-3e8a-b32b-d82b35e3bc64 | -7.1325 | -59.6569 | 2025-08-16 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 61afd222-266f-3df7-b48b-e3718284848d | -9.0346 | -67.427 | 2025-08-16 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a1986975-e893-3162-9982-f8af6e344fbb | -13.4294 | -43.6733 | 2025-08-16 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 87ddbb02-a7e2-3635-afae-dca7ba215579 | -14.9632 | -54.7143 | 2025-08-16 00:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |


[Clique aqui para ver as próximas entradas](README7.md)
