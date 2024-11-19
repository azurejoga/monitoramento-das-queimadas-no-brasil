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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29441166-2241-3109-bbfe-ed11757408df | -9.3015 | -46.1777 | 2024-11-19 00:28:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a93d294-d0cf-31ff-a148-28a5c2c7c547 | -2.4393 | -49.139 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdb5f520-9433-344e-850d-9b0ba40570e2 | -7.5613 | -46.4603 | 2024-11-19 00:28:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12a75daf-35ee-3842-aaaa-22864443356e | -3.2904 | -45.3298 | 2024-11-19 00:28:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 818f6902-b9ae-329d-a6fc-9ec0de6a9571 | -6.0415 | -44.053699 | 2024-11-19 00:28:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85b37d00-e2ad-3d43-98dd-ea66fb144869 | -2.5846 | -51.706699 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e899ca-a50f-33a0-bd2d-f92904c44018 | -2.6779 | -51.800999 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89dcebeb-0f05-38a9-8a1a-1d082331a140 | -5.574 | -46.339699 | 2024-11-19 00:28:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62b97b5a-847a-3fed-a181-3f91c6eb9c63 | -3.4658 | -48.255901 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 071f6141-3334-399d-acf6-74111b49d120 | -1.618 | -52.5839 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e78c146-5b29-35fa-a56e-c400ab5cb393 | -2.5765 | -51.716202 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 978dd5ea-c2c4-32d2-8099-6f3f20d52fcf | -2.8246 | -46.664001 | 2024-11-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b485e01-3f07-33b0-bcf8-914bc00b27b3 | -5.932 | -39.668499 | 2024-11-19 00:28:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2bb9cfce-e789-38de-8176-5475bdcf397d | -0.2383 | -48.520599 | 2024-11-19 00:28:00 | METOP-B | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04085e72-d706-3bdc-afcc-aa0b4c0fdd13 | -2.1472 | -50.905399 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c821af5e-9acc-3dea-92de-92f5deeaf330 | -8.6694 | -47.973701 | 2024-11-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad02c62-155e-342d-be39-5c9e7c45a01e | -2.6462 | -48.5508 | 2024-11-19 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a193abd1-bf14-3c33-b6f4-1a877114f7c2 | -1.6222 | -53.290699 | 2024-11-19 00:28:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b8fefc-7369-33d2-9006-08dac162a12a | -6.0488 | -44.040798 | 2024-11-19 00:28:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b061585-b680-3c2e-bcc4-d562f677f2d3 | -4.1051 | -51.047798 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb7a1d26-08ba-3a84-afe8-23ac3821f409 | -3.134 | -52.9683 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2885059-4a46-35d5-b550-92dd07caf9fa | -5.9636 | -45.350399 | 2024-11-19 00:28:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f2b08f1-2539-3a77-83b7-b52a90faa159 | -3.167 | -44.307201 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cccca057-eda6-366c-94b5-c8cfd5a5a4c5 | -4.8145 | -43.696701 | 2024-11-19 00:28:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d61a5415-2b43-3624-9a20-cd7e3b59a6a9 | -2.5928 | -51.789001 | 2024-11-19 00:28:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5c30bf-6c18-3ddd-89ba-a175f0704fcb | -2.9395 | -48.071701 | 2024-11-19 00:28:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67f01b0d-251e-30f1-9f12-a229c4b363d7 | -3.0565 | -53.266899 | 2024-11-19 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c53eca-1c5e-3993-bfdc-06fe64879893 | -8.9445 | -47.640301 | 2024-11-19 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77427cca-b20b-3cb5-8b1c-5b2f89ceaf48 | -1.6936 | -52.141102 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9703bdd7-0471-30ec-89ec-1e9403741f5d | -3.5429 | -51.5266 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e473399-f989-307d-830b-3e7c1d3fd0e1 | -20.101101 | -47.465302 | 2024-11-19 00:28:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6e826255-67e2-3410-b27d-7a94e681cf5c | -2.4738 | -49.1096 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 779de7f0-a645-3210-820a-2f5a7132428b | -3.7161 | -52.442501 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ddc0611-6cef-3399-bb95-373bee80a046 | -7.5577 | -46.445099 | 2024-11-19 00:28:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71432af9-4227-3bb9-8f89-24e96b22616c | 0.3887 | -50.8549 | 2024-11-19 00:28:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9f1e02-a3aa-3e11-ae55-a27609c6d652 | -8.9429 | -47.633301 | 2024-11-19 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8614f09-e674-3135-9056-8700e08f2241 | -3.5413 | -51.519299 | 2024-11-19 00:28:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec98e7c-68d1-3440-b2f0-006f7ac5edd0 | -3.5644 | -50.152 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e77715-f301-3f55-b7a2-aaa629db2c90 | -10.9602 | -44.523201 | 2024-11-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c48031b-9ac0-36b3-83cc-e6576c6caa56 | -8.2621 | -44.026402 | 2024-11-19 00:28:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3dbca01-8a9d-3c50-9585-958ccb182be3 | -4.158 | -48.763199 | 2024-11-19 00:28:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b01ff7d5-4704-32ef-9e7a-e1e0f5da3ef2 | -3.7144 | -52.434601 | 2024-11-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a6cfda-3ebd-3358-bf2c-7811f8a0cf94 | -6.3851 | -44.726799 | 2024-11-19 00:28:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb2017db-f319-3d0e-b913-878934f098bd | -3.3545 | -54.1008 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f65902-ef1c-3bc7-8ecc-38901b5d76ab | -11.1321 | -45.3465 | 2024-11-19 00:28:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8293364a-39df-30a7-89c9-a9b4ed4d6279 | -1.692 | -52.133701 | 2024-11-19 00:28:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef3c45a-a3a1-30af-bf78-fc28928e60e2 | -3.4114 | -50.2505 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a10e24fa-ecf3-337a-99c3-e4bc0acdbbdd | -3.6042 | -54.209 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26b569eb-c40e-3d44-abc9-2b46276de447 | -2.9177 | -49.112202 | 2024-11-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9ca7c5-b40a-3da5-814a-1ab6b7dce970 | -2.9345 | -48.322201 | 2024-11-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1810a5a2-2965-3697-9682-199ad33488c9 | -0.1098 | -51.421001 | 2024-11-19 00:28:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 63932095-7ac1-35aa-a07e-54154c955324 | -8.671 | -47.980598 | 2024-11-19 00:28:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39738b2b-eadf-3271-a585-d4baeecb9b12 | -8.2523 | -44.028702 | 2024-11-19 00:28:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0e3390-aceb-38ee-b400-1bfb4604dc32 | -3.5383 | -50.402699 | 2024-11-19 00:28:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd8b038d-ec1e-382d-8895-3381336bf828 | -6.4796 | -47.501499 | 2024-11-19 00:28:00 | METOP-B | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9b2f278-e86b-32fd-9a3b-82dd99fe2226 | -2.8481 | -53.993301 | 2024-11-19 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c56e495d-46cf-31aa-a455-09585831b05b | -3.3524 | -54.091202 | 2024-11-19 00:28:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef46f829-df75-3e80-8262-4d1546f968d0 | -7.3952 | -42.7691 | 2024-11-19 00:28:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20895e36-72fe-3664-bc6a-718b5f4e478d | -22.304701 | -49.7672 | 2024-11-19 00:28:00 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8fff0725-34d2-3f58-9338-76d4ddaec5be | -2.8577 | -51.776901 | 2024-11-19 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9f7f04-7a57-30f7-8858-428002829072 | -3.3104 | -52.6987 | 2024-11-19 00:28:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d6c393e-496a-3800-a37f-dbea9ae2f1fe | -3.5125 | -50.2343 | 2024-11-19 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 44fcd4f2-3f1f-3307-9603-06f32d032ecf | -13.2643 | -56.7947 | 2024-11-19 00:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 32f7e393-a6e9-3fdd-ac15-500ae9c6e5a4 | -2.9982 | -45.1658 | 2024-11-19 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5408e8a7-7134-31be-b44d-a6f1ce8c2718 | -2.5011 | -49.0375 | 2024-11-19 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a817d77b-db43-377a-a860-d69f17436c1b | -4.1182 | -51.0486 | 2024-11-19 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3951df85-00d8-3e16-b5a0-c883c45c0b64 | -13.264 | -56.8149 | 2024-11-19 00:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ea52eacb-5d5f-306a-991c-09570916d689 | -9.2546 | -44.9845 | 2024-11-19 00:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 301d4106-68e9-3aee-8482-b00526e5adf2 | -5.9975 | -45.3607 | 2024-11-19 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| de00ccbf-d6c7-3eb9-b8d5-ce2737327e81 | -2.7844 | -52.5954 | 2024-11-19 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| d26b1dc8-2c1e-31a9-8645-42dfc23ca67f | -3.5126 | -50.2133 | 2024-11-19 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6441d280-4351-3f11-b3fd-cbad738fc2c0 | -2.766 | -52.5959 | 2024-11-19 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| e33995e5-6596-347d-a24a-cae97a7b065d | -9.2543 | -45.0074 | 2024-11-19 00:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b82fa6f0-e62e-3cdb-b28d-17a4a278ae7f | -22.3365 | -52.0415 | 2024-11-19 00:30:00 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 747aefe2-6b63-3ad2-a1de-a7c8ecdf9b06 | -13.245 | -56.8167 | 2024-11-19 00:30:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c213d850-5b7b-3795-b82a-0e183bb4ce27 | -2.9983 | -45.1433 | 2024-11-19 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| bc69b814-44ec-3353-b364-11ebf81c1811 | -5.979 | -45.3395 | 2024-11-19 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d991f405-4ff2-3fc1-b0b6-5cede8c788a1 | -5.9788 | -45.3621 | 2024-11-19 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 3d7c5b28-4a69-382e-96fa-8534654c20d1 | -3.3677 | -54.0991 | 2024-11-19 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7e987b0e-e853-306b-a0f7-5c08196576e8 | -2.4827 | -49.038 | 2024-11-19 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e539ab93-9fcf-3105-adc3-ac2830b689c4 | -6.0659 | -44.0316 | 2024-11-19 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d5119f7c-1806-3887-89c5-5b29c4757665 | -6.0657 | -44.0547 | 2024-11-19 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 44e727d5-e3b4-3863-9d73-9295392e6622 | -2.7659 | -52.6163 | 2024-11-19 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e290c836-495a-32e2-8295-9463e05b68ae | -8.6876 | -47.976 | 2024-11-19 00:30:00 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0e66a4aa-628b-3e73-83ac-c46ac92f17e9 | -3.0354 | -49.4688 | 2024-11-19 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| af060f1e-e91e-3171-ae56-0a0702649444 | -2.7843 | -52.6158 | 2024-11-19 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 57881750-2625-3228-b255-f12d000f10b4 | -9.2733 | -45.0052 | 2024-11-19 00:30:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2f5ef87f-1125-3633-a861-296e8c33d15e | -2.4827 | -49.0167 | 2024-11-19 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 37e3f390-e36f-35b2-8866-60a7ab814423 | -2.5012 | -49.0162 | 2024-11-19 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c66df795-3267-35b8-a26c-91f7772bf803 | -8.2662 | -44.0115 | 2024-11-19 00:30:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9cf71ce6-7ea4-3eee-902f-d4d34c5623f8 | -22.30955 | -49.75763 | 2024-11-19 00:39:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.7 |
| ac210ca1-75e7-35bb-b60f-dd10eed2cf04 | -22.31179 | -49.78094 | 2024-11-19 00:39:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.4 |
| c29c0182-0069-3fd7-baee-e164ff20a1ea | -5.9788 | -45.3621 | 2024-11-19 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 180918a1-cad6-32e0-9308-4504a5bc27d6 | -6.0659 | -44.0316 | 2024-11-19 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 434fd346-c062-3482-a840-8f259b71f226 | -0.1196 | -51.4186 | 2024-11-19 00:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7e52dcd4-2670-3e76-8456-9aa5acf20698 | -2.7844 | -52.5954 | 2024-11-19 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4a460008-4099-3e2f-8bc7-5392b9eaca7e | -2.5011 | -49.0375 | 2024-11-19 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b8c42337-cfe1-364c-9c84-c1448648118a | -4.1182 | -51.0486 | 2024-11-19 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5970ed54-87f6-32a8-9700-4013298fc4ef | -2.766 | -52.5959 | 2024-11-19 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 8a320c91-56f7-3cde-b2c4-cc2e767f89cc | -2.678 | -46.2281 | 2024-11-19 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 38.6 |


[Clique aqui para ver as próximas entradas](README6.md)
