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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 435c921f-3624-35b6-9c5f-075458c4c678 | -8.23172 | -45.4413 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7f9da87-08fe-36a0-8987-4653c6558e14 | -11.68443 | -44.53436 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62144dc6-9f83-34c0-88c5-e20e5654e628 | -11.70007 | -50.66146 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d344e0-9304-3ad9-9d0c-250357f2198a | -11.44563 | -44.93156 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea1de690-bd97-3fdf-95fb-f708d2543637 | -11.71002 | -50.59974 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c085884-9eaf-3c14-8b82-40622d380e6e | -12.16467 | -50.39724 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5261142e-3f5d-3c73-a7b5-1611ae688c38 | -8.22873 | -45.43679 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ebc6728-4a97-376f-ac22-d9494c7e9fe1 | -7.38286 | -47.01541 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e83f2b1-ae3e-35f2-b402-98d2ee118be3 | -11.4439 | -44.92444 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 167e021e-2bb2-3e43-b1d2-48d82c6143c3 | -8.97082 | -44.14571 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2827c5a-b60d-3a52-abb2-84f249560a68 | -6.6732 | -45.62169 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3498eaa5-2911-3cd2-be49-cb570d61b891 | -6.6563 | -55.10434 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1257845-a2ae-3736-a5d6-bd94db1a1153 | -6.602 | -47.16302 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8467d05a-1126-3823-af32-6b3de04e3290 | -12.63433 | -47.26953 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5fd4e21-c4ac-30f1-9d57-b9820f105cc2 | -11.07308 | -51.40635 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 650374b5-00f3-3d6c-9f20-081cf5ae8ab1 | -12.59177 | -51.9589 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b3a79d3-c61f-302f-a62b-d29cc821893d | -8.33515 | -45.4105 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2ff064b-cfbf-36c5-95d0-5ce6957c5291 | -11.1916 | -44.81928 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b8fe45cd-19fd-3264-baa1-bad6275a64f8 | -10.60051 | -49.98325 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff6a7e7c-0516-3a90-9db4-c722dd62b5c5 | -7.51797 | -46.61473 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ccb5f38-334b-3c5f-8c70-b154b361d5fb | -8.14179 | -44.45256 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04d38c00-ccad-330c-b5a5-316afedd754c | -6.71452 | -45.59505 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1575fe36-bf7b-3830-81bf-a7e208618655 | -6.6994 | -45.64832 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c3195bf-42c8-3009-a799-72d15bafbf62 | -9.99495 | -50.13383 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f679c8c-0266-3d09-bdba-c226b00c159c | -13.33375 | -46.80806 | 2026-09-28 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2cb1130-0a78-374d-88ff-8c7ea242298e | -6.68893 | -45.64676 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8ec4050-5e93-3878-b2a4-36d66f8342f5 | -11.41432 | -47.42083 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad5032bd-57af-3aba-a61c-06356b7129d3 | -10.89857 | -45.11357 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9822b241-5030-3f6a-a09e-bc53de7b80e9 | -6.69242 | -45.64731 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d25a928-35c3-3b82-a351-c7946faabb9c | -6.70028 | -59.96048 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 185da953-a085-3b38-932c-c0f06f1607a3 | -7.86308 | -61.19264 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3906c746-e03a-3f07-b1bd-825b0b0b32d1 | -12.59241 | -51.95498 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51a11b41-82b8-325b-b090-1a39161b31f5 | -10.89872 | -50.68699 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1ce5301-4e6e-3495-bb34-c28a0ee54fb4 | -6.59565 | -48.60219 | 2026-09-28 04:34:00 | NOAA-21 | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d03dc56-e0f3-3cf0-b099-4b2163daf546 | -11.01118 | -54.14153 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba3920b3-349d-3d96-aa2d-c4be0f431793 | -9.97697 | -50.16043 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a41331fe-4af3-3df5-9f6a-79f1d22d1729 | -6.65926 | -55.11478 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2303989-f505-3c59-b6f1-0f383645feaa | -11.0737 | -51.40249 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f227be-bc8c-31f9-a8bd-d5296f8a45b3 | -7.68923 | -44.87773 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d542abe-6343-306b-a319-e4c9266cbce6 | -11.71032 | -44.51867 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eccb4a9b-491b-31f0-a1f0-8c37b796c953 | -11.7101 | -44.5499 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e744b426-b86e-31a7-b350-e87927d2dbc6 | -8.1 | -44.00376 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 195d79c6-286c-3469-b80f-e19a658cb9ee | -11.70191 | -44.55251 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da956abd-27c6-3e8f-8765-97fcc6013a66 | -12.09951 | -50.29491 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7c3e5b13-7956-37d9-a507-ef000c77e7b1 | -12.62575 | -47.28001 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b913e677-e02f-386a-a6c9-2dff1099d3a5 | -8.73066 | -47.97903 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e02a773-9d4e-39cb-b2fe-2334e519c360 | -9.17359 | -45.77705 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6692ce9b-8665-3d7e-bd2c-e0e7473d3b10 | -9.1754 | -45.78945 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0490571-183c-3235-9b1d-89576da2f246 | -13.46389 | -48.58932 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f31d0af-de15-37f5-bd8f-125b5bd4372c | -15.5771 | -47.90305 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7063b450-9a28-3588-b1d3-fcf829fbd8f4 | -14.80344 | -45.96214 | 2026-09-28 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cf4aadec-02e3-3a12-9a3b-03aeff6bba3d | -14.49095 | -48.3337 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9271e6b3-87d8-3131-ac67-1d6a20237d09 | -18.54707 | -43.58829 | 2026-09-28 04:36:00 | NOAA-21 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f2a17a78-9584-3ff3-a44c-c808d9e3f918 | -15.28342 | -47.68278 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65090124-d0cc-3119-824c-3d28b18ea5f6 | -14.73289 | -45.57342 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6939571-6617-3d26-9ef6-26bd919b6f7e | -14.78969 | -45.95051 | 2026-09-28 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a1aa170-c2a4-3397-88db-ea01034a5ea3 | -18.12278 | -44.37923 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91044041-c977-3266-90b8-81b8fc56c606 | -15.56161 | -47.91258 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c739e57a-3f99-3dd5-a853-007ad6626062 | -13.85749 | -46.3751 | 2026-09-28 04:36:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f2c023e-74c0-313e-8238-528f36086768 | -15.94255 | -42.3378 | 2026-09-28 04:36:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1dac4763-9a7a-3ce9-95d0-d6726f693f49 | -14.50274 | -48.32425 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3091e6a-dcca-3591-bfcb-c7046813449b | -14.51792 | -48.31526 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4a47d4e-6f6a-3e13-93b6-d648e4235970 | -13.37551 | -51.31644 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 251dbfd5-fdc8-3207-a273-afa689cf7e7a | -17.82912 | -44.39521 | 2026-09-28 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a02511b1-a864-3354-9c51-0fce3b3eac7d | -15.17101 | -46.15837 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5cba5c80-7edf-3ec8-8b41-4be0992db022 | -14.52296 | -48.30475 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c0626f2-2e54-3ed6-828e-ea56f32e1f5a | -16.46631 | -55.07563 | 2026-09-28 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4a39b2fd-a5c4-3b10-8e4e-551a44d33091 | -18.09614 | -44.38076 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e9b3f17-6943-3971-a25d-19ddc70fc7f1 | -18.67927 | -41.46203 | 2026-09-28 04:36:00 | NOAA-21 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dd9a6678-f0f8-3a2c-a756-802640f17250 | -13.38167 | -51.3213 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32347b39-af1e-3c95-8584-11e5c22f5a27 | -18.67895 | -41.46512 | 2026-09-28 04:36:00 | NOAA-21 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ef9e6c43-604a-3d4f-b297-1de9670e32c7 | -15.13081 | -43.61679 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03d54472-ffec-368d-8186-0cd13a1f786e | -15.40782 | -47.91433 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8d89bf47-e4fa-3670-8f95-ad39a621be66 | -15.93251 | -56.25869 | 2026-09-28 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 02505885-c632-3ce1-b25f-aad1461c2182 | -18.68492 | -44.60741 | 2026-09-28 04:36:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 382f217d-e3c3-3251-b575-385690b9b44e | -15.15934 | -43.60306 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d2f9b980-2940-362a-b1d8-8b217da84a1e | -14.52678 | -48.31222 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe08d0eb-a026-371f-a120-a1077f578152 | -13.7251 | -48.81446 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b20fca3f-dda8-375e-997d-442864152374 | -15.10701 | -53.86917 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7345cee-679a-34a3-9f9f-148052ff9b5b | -12.90012 | -52.05021 | 2026-09-28 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76c39e2-2cc9-3d2f-b0bd-d0ed4802cdcb | -17.83594 | -46.54914 | 2026-09-28 04:36:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2065ba3b-c41a-3bcb-80ad-8aef1b592310 | -13.46334 | -48.59293 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfdd6fa8-24c6-39fe-8511-d048530d2230 | -15.11577 | -53.88482 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ef9592d-6cab-3d49-99c3-b42e11901f5f | -12.76403 | -54.0411 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1357d1b-8c9d-3cf9-99b5-d659e70332cd | -14.72074 | -45.57635 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 321d3c81-e2d0-3927-852e-399504fab506 | -14.12197 | -46.29991 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4f06c604-ff00-39af-adba-443d9d2ce656 | -13.46055 | -48.58878 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 497632a0-dfbf-324c-8be2-b01f1cbfdad2 | -15.12025 | -53.88095 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24a37c6f-c061-3efd-a24c-a23b5079a23c | -16.13444 | -49.50621 | 2026-09-28 04:36:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d100bc1-00c6-3a93-a095-671375f5e628 | -14.71691 | -45.57572 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e0e101c-4abb-3e0d-b37a-b89932e36182 | -18.51552 | -42.41806 | 2026-09-28 04:36:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6f474559-8f57-331a-bfd3-c86511ae2336 | -15.18923 | -48.42603 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f01b099-9b76-3859-b6aa-606716535899 | -16.38797 | -42.56168 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed843735-66b0-319a-83a3-fcb821798aec | -15.41013 | -47.92264 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f95d1b39-0dcf-343d-acfd-17dbe8752ebd | -14.52241 | -48.30844 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4ddc44d-cdd1-34e2-844a-858110d8071e | -15.17848 | -46.15946 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 20fa6b73-13d8-3927-bb66-605bd44fb990 | -15.1698 | -46.16724 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04609010-4b9a-3bcd-b9bb-916e7072740d | -15.82843 | -42.56357 | 2026-09-28 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| abb37e88-840a-34f6-aa7e-f97b0f59e831 | -16.0659 | -47.91498 | 2026-09-28 04:36:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 631ba013-0997-36d2-89ff-9dd3e096cb8e | -13.69074 | -48.81627 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README41.md)
