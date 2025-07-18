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
| c5b3a001-437f-3434-a07a-2dd5efe0be09 | -22.27485 | -54.1706 | 2025-07-18 04:32:00 | NOAA-21 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aacd4282-cf2a-30ca-9602-ba3178e109c0 | -23.39008 | -46.69968 | 2025-07-18 04:32:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2aa30eed-0509-36dc-b3e3-c50a85fcc411 | -24.57591 | -53.00443 | 2025-07-18 04:32:00 | NOAA-21 | UBIRATÃ | PARANÁ | Brasil | 4128005 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ff32088-6b5f-30e9-a873-e253528a0e87 | -21.86474 | -56.73961 | 2025-07-18 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16866b15-868a-3294-8970-9f8c8517e460 | -25.1233 | -49.76307 | 2025-07-18 04:32:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 052ecca9-2fe2-369e-836c-26d335b01779 | -21.86387 | -56.74399 | 2025-07-18 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ad8d6cb-815d-3a87-8f99-85976d301abc | -21.04523 | -55.98856 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 690d8306-5a7b-3cab-80c8-e972a16c5019 | -21.63432 | -49.84013 | 2025-07-18 04:32:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 56acedaf-f485-3725-b2a9-38647c5e097d | -23.47626 | -47.1732 | 2025-07-18 04:32:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e40faef3-8988-33af-b308-c91e95e8686b | -23.96 | -48.11821 | 2025-07-18 04:32:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f431c939-f56a-3303-8a48-c4d559c00b42 | -23.41792 | -46.99559 | 2025-07-18 04:32:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 227dd41f-fe2e-3fd1-bd92-dbafc5b492f4 | -22.4213 | -48.15123 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 766b430f-77fd-341f-8497-44ad61cbfb7c | -22.41843 | -48.14668 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 052cb834-92fa-3596-9631-21867122f2cd | -23.56184 | -46.1706 | 2025-07-18 04:32:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8f597acd-e412-3ae5-8347-3b2477187876 | -23.15033 | -46.25645 | 2025-07-18 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 864c70fb-ae37-3754-aab0-b181399460bc | -25.67364 | -50.39484 | 2025-07-18 04:32:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c849b04-f5c7-3b01-a0c2-863382e8f55d | -22.65642 | -53.3763 | 2025-07-18 04:32:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1448a904-d029-3f3b-b675-13f5b191e49a | -22.96123 | -49.10755 | 2025-07-18 04:32:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94d54dd-c3a9-3c9e-a7b7-642e00969d04 | -22.70372 | -44.17867 | 2025-07-18 04:32:00 | NOAA-21 | BANANAL | SÃO PAULO | Brasil | 3504909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1332fe4b-025d-3e62-8b19-c437abf31a83 | -23.15533 | -46.24738 | 2025-07-18 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6d9d2c67-bd72-3b71-91e9-3e7639ac7a05 | -22.42073 | -48.15521 | 2025-07-18 04:32:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 74b2805b-d2c5-37f8-afab-95e558156484 | -25.41879 | -49.10013 | 2025-07-18 04:32:00 | NOAA-21 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a4384a45-55e7-374d-976d-8deaf57dd1a1 | -20.20773 | -56.61476 | 2025-07-18 04:32:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7dd83b67-adad-3c4a-9d20-bb55deba6809 | -22.92182 | -47.19331 | 2025-07-18 04:32:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ebd05fc-1923-39cb-9088-b35f0ac10feb | -22.35875 | -47.56133 | 2025-07-18 04:32:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ebc7b8d-d7d9-3b0e-8054-1829831e7d3a | -22.88367 | -44.77205 | 2025-07-18 04:32:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1299df46-6e42-398b-8b42-cec8182f9233 | -24.44395 | -50.87614 | 2025-07-18 04:32:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6b393c78-06f9-3a80-8ea8-c10e1e92241c | -22.2473 | -49.921 | 2025-07-18 04:32:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d1a21cf0-205e-3e9b-8e69-d86df5c111a0 | -23.00737 | -48.6259 | 2025-07-18 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd2b1269-9eaf-3e62-a63f-42d2c6f8418e | -25.4191 | -49.09899 | 2025-07-18 04:32:00 | NOAA-21 | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ba1f0039-b1ee-3551-af55-7f5f68edf550 | -22.6827 | -47.6438 | 2025-07-18 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c706b30f-0c77-3d41-938a-97e4c1eb7d5d | -22.643 | -47.51697 | 2025-07-18 04:32:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e5694913-5e54-3abd-b4b5-7995f2c36c28 | -20.94066 | -56.59595 | 2025-07-18 04:32:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7fe137e-f9cd-31bb-bf5b-84a385376671 | -21.04103 | -55.98767 | 2025-07-18 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6ac6349-8057-3358-a9cf-f21e7e611837 | -3.3957 | -47.5003 | 2025-07-18 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a13d182e-4335-35ca-a94a-1ac1c8fb8dd1 | -5.6379 | -43.7175 | 2025-07-18 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 771d3d01-d8d4-37fa-bca8-0fb20c5226ea | -11.7508 | -48.1825 | 2025-07-18 04:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9079e939-5dcf-3474-b6ae-930c89d33bf9 | -3.3958 | -47.4785 | 2025-07-18 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 0cab03aa-8d84-30c8-84be-2398839ff1a8 | -11.7317 | -48.1849 | 2025-07-18 04:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 136c2b9a-f58d-322d-846a-07fd9cfae3a8 | -5.6567 | -43.7161 | 2025-07-18 04:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| e7e8e199-9657-3c47-9136-020475426731 | -3.3958 | -47.4785 | 2025-07-18 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 25ee1ade-b09f-3a22-a364-81fb12505210 | -5.6567 | -43.7161 | 2025-07-18 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 3b2b181a-8011-3b67-814b-e9d56369d055 | -11.7508 | -48.1825 | 2025-07-18 04:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| fbe37dbd-c658-31ec-aa45-f04aa89e4be6 | -11.7317 | -48.1849 | 2025-07-18 04:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 06a2d4da-e46d-3f22-b8f8-36523ba8ba14 | -3.3957 | -47.5003 | 2025-07-18 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2f957e1a-a444-3840-8d61-cedf84139fbf | -5.6379 | -43.7175 | 2025-07-18 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 38c45d3b-b864-3e37-80f9-3fed529428c9 | -4.64403 | -43.12197 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38be63f9-4170-3ddd-b511-626a1d3b8e89 | -3.04581 | -49.42764 | 2025-07-18 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1e92ba-0f75-397e-a094-e9220881f5a9 | -5.77925 | -45.07357 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0253cfc-7c96-3119-93db-4d24d1ee95d0 | -5.73801 | -46.25626 | 2025-07-18 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fff69de-8bb1-3c3c-89ec-aa205937e381 | -5.73333 | -44.5015 | 2025-07-18 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a1aec0-a470-3935-8812-7915effe8a41 | -5.65085 | -43.71761 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 09d64425-ca32-3679-96d0-434ed4974ea4 | -3.03765 | -47.86332 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f564329d-4c43-3ffd-b6cf-bae6c036f665 | -5.85739 | -44.96574 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e84dbf4-2c63-3727-bae9-3d349509c048 | -3.11571 | -47.01573 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 678f678e-3a76-3b24-9882-ff1f263f1787 | -5.78946 | -45.07006 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33a01f0d-4513-38b3-b199-bac97c073eb9 | -5.79152 | -43.63146 | 2025-07-18 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13f3e682-338c-34a8-b8a2-ce35a387acdf | -4.79862 | -43.2264 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e8e8cde3-8f9e-3fb3-9120-dad5bfc18265 | -3.61032 | -43.54007 | 2025-07-18 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 251cd0b8-071d-3841-a3d1-615faa0b9122 | -4.64453 | -43.11863 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7642e1-d355-30c8-a008-eab485005761 | -3.86022 | -50.08192 | 2025-07-18 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bfde8f-4b80-39f4-92ff-a2f0b6ea842c | -3.72936 | -53.99171 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76a6eac3-5616-322d-8db5-8de273ee08b8 | -4.11068 | -47.93155 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afea6aab-04b3-30d4-9186-fe285ccac404 | -3.7146 | -49.07082 | 2025-07-18 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04a55029-6c91-3f5a-b892-ab68ca41d62c | -3.84696 | -47.7556 | 2025-07-18 04:51:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cda44cc0-173e-3157-90eb-6942f3078dd1 | -6.69063 | -43.18311 | 2025-07-18 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9dcf0d89-bb13-356f-90c4-8e0bc49636c1 | -4.64987 | -43.11942 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4795b4fb-886b-3f6d-8f29-8dc1c449b675 | -4.11035 | -48.20732 | 2025-07-18 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d74aff31-49e9-300d-b2da-a9b966a352a2 | -4.30709 | -48.1088 | 2025-07-18 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 51db70e8-5199-321a-8d93-16f3a0ff3198 | -3.39686 | -47.50425 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71130187-4e0a-3f97-87cb-c4fa2718b6f7 | -2.94308 | -48.05265 | 2025-07-18 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2c8110b-d37a-3e51-b843-861cefeb3400 | -3.39669 | -47.47935 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 1a7ed5e3-10dd-3ba8-ab91-a9ad2a6524da | -2.44182 | -47.32442 | 2025-07-18 04:51:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e7638ca-e243-3a87-ac19-d40c0639c00e | -3.4015 | -47.49995 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2546379e-4051-3f50-b02a-598d506c7e7b | -3.3913 | -47.48851 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e0deae07-2c79-3f62-9130-bb0b109be90a | -3.52207 | -53.20536 | 2025-07-18 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee68e4f-e536-3d79-a920-a515e0cbcb28 | -6.47094 | -45.17119 | 2025-07-18 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28cfdf06-86ad-3e0b-ae78-e751bf3ae1f7 | -5.66691 | -43.71688 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12619009-14a7-3d2d-b053-174d5ff367bd | -3.12449 | -47.01176 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17ed715a-b3bb-3bdb-a4cd-91bd399197f2 | -4.3078 | -48.10419 | 2025-07-18 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c776e3db-9d13-3ccb-8047-21776e8afa43 | -3.58962 | -48.94052 | 2025-07-18 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5c26f4-e806-30a2-9059-538804468896 | -4.79957 | -43.21987 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba215fc5-0286-319f-8924-652e8cff3a52 | -5.44206 | -46.28957 | 2025-07-18 04:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d9ef2ad-ef9e-3158-8d6f-780a358c81d2 | -5.85209 | -44.97449 | 2025-07-18 04:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e83c780-88bc-393f-abde-01451643ca86 | -5.6461 | -43.71365 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e15d89b1-1e87-3f8a-bdd4-70eada3346df | -3.73281 | -53.99227 | 2025-07-18 04:51:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79b57ef1-78f6-3397-a340-0adefcdd59d8 | -5.78801 | -45.08018 | 2025-07-18 04:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2232a41-6176-3cbe-a4b7-4b030bcc2ea7 | -6.68465 | -43.18597 | 2025-07-18 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f92f9bfd-a63c-32f8-be0c-7815fec9ca5c | -6.72417 | -44.33199 | 2025-07-18 04:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52d94fbc-df1d-34a1-b80c-caba7c2fdafe | -6.3381 | -44.753 | 2025-07-18 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0d9dff8-ee77-354e-9777-a7962f52b58b | -6.9345 | -43.80875 | 2025-07-18 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1163f66-1395-3ade-9728-d41f638ba853 | -4.64696 | -43.12014 | 2025-07-18 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f731cb12-4475-3c48-b9ad-54e2f0426953 | -7.05965 | -42.98219 | 2025-07-18 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3ab2a31-1a52-3f9d-b4b6-5a4e1eccf9bf | -3.93687 | -50.44284 | 2025-07-18 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82e8ff8c-8707-302a-ade0-2a8bdefbaa5a | -5.84149 | -44.10059 | 2025-07-18 04:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b96049ec-b258-3257-aa3f-1da53ec9c957 | -5.76119 | -43.39776 | 2025-07-18 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fccace49-aa46-35c1-9462-58f0502e1155 | -2.91862 | -48.23877 | 2025-07-18 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f48b9e00-19ec-326c-930b-a0bdcf093530 | -5.65129 | -43.7145 | 2025-07-18 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 888e63f7-afdd-344b-b742-659c3cb98d4b | -6.69013 | -43.18673 | 2025-07-18 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 291ab935-e6e1-35dd-8ce0-14433a98a6dd | -3.3874 | -47.48794 | 2025-07-18 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |


[Clique aqui para ver as próximas entradas](README20.md)
