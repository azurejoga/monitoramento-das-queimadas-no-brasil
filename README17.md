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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7df535b0-d14f-30e2-986e-4f31446fcc0a | -4.37116 | -41.71333 | 2024-11-05 04:08:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1fd0705d-84c8-3a88-81ea-ac8b67a29b12 | -2.17776 | -48.86105 | 2024-11-05 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c020835a-b570-38c4-8748-b2cffd639014 | -3.30149 | -50.1419 | 2024-11-05 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53f5ded7-9f9d-38d9-823b-348b5a0636bf | -8.32038 | -43.57291 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d585cc87-b973-3b07-815f-1df76f9be679 | -7.21585 | -42.535 | 2024-11-05 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 123712df-9fd7-38f9-94bc-3a81a741ee18 | -4.51367 | -44.07124 | 2024-11-05 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89fc6a8-b067-3087-bf7b-e259a14593d1 | -5.30036 | -46.24537 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8512ebf9-e376-3e32-b150-78a91e90a002 | -2.83962 | -48.46104 | 2024-11-05 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faeb3e76-5298-3fd3-92c6-1ac9fc803ac7 | -5.37526 | -46.45301 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b663cda3-89ad-334b-9b99-1dc5cfff2988 | -2.00812 | -47.73452 | 2024-11-05 04:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93dcca4c-91e9-3044-87ed-3cc33cd1432d | -5.46894 | -42.82049 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0970c8a1-9d82-3426-97d9-df60e0efd8bd | -6.30902 | -46.69609 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 965d2da0-84e4-3a63-985d-cf495505fac0 | -6.25309 | -43.56258 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 38f114a9-5474-335f-8277-a1aa6919e7f5 | -8.49633 | -42.09465 | 2024-11-05 04:08:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4675e8d9-67d7-3fda-9152-a5c44cb95a78 | -2.8061 | -51.49251 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ff52d1-973f-3a2c-a93e-3244ba51a73d | -5.1076 | -42.59142 | 2024-11-05 04:08:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 337cf84d-763b-3f14-ba1a-d57359c1fddf | -4.68618 | -45.81235 | 2024-11-05 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a97d756f-31e4-36fb-a13e-2bcdf5b602fc | -3.30596 | -46.0287 | 2024-11-05 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b895ed7-cbf9-3c04-8882-7d29eb07dbd4 | -4.40521 | -45.85914 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af71566-b073-3f91-a0b0-62aa8a0eaeee | -8.3474 | -43.57724 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40f8c371-ecd3-3f99-b1c1-5d7cb326937d | -4.14104 | -46.83823 | 2024-11-05 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a333df1-f2f3-302c-bd41-1ca9e5bd25ab | -6.01349 | -43.99091 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84e03ed6-d7f6-3e93-a9bf-33cbedeaa9e8 | -6.00741 | -42.70781 | 2024-11-05 04:08:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 330b5743-742d-3164-b948-200231ff5c7f | -5.60909 | -41.65059 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5be1013d-4ab2-32c2-affd-7b5f502c9037 | -5.3097 | -43.20234 | 2024-11-05 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7248e9c0-ae73-375e-871a-9bd83ca0c710 | -4.65101 | -45.33476 | 2024-11-05 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3098ae78-bea8-3f5f-b0ce-83fa92a56b36 | -4.23807 | -44.93728 | 2024-11-05 04:08:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 443a38a9-69d0-3597-b451-20d67a8801be | -5.61593 | -41.76139 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24b4a767-9dc1-3db1-9da2-ce7cd3b1c393 | -2.73093 | -46.67866 | 2024-11-05 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be6063d1-ba2d-3cd8-9f79-d718917bc86a | -3.54246 | -47.39061 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5fe0c11e-e614-33fb-a7af-8fe4e926d67a | -6.11548 | -43.96634 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 925c1789-7b04-300f-8658-841c2e4632e4 | -4.04548 | -46.20706 | 2024-11-05 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66de8c21-eac2-3b9b-9489-c16c395d0d09 | -5.56874 | -42.29859 | 2024-11-05 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65e73d6e-63a5-3edd-b7a1-efbb371c1c92 | -3.95282 | -41.49549 | 2024-11-05 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8908d2a4-92a5-3b74-90e2-68ce419e4014 | -6.30393 | -42.03673 | 2024-11-05 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7260791-fa32-391c-8c97-4751baa58af5 | -3.36141 | -44.26055 | 2024-11-05 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a8ea313-2458-3548-a08d-d0b67237c748 | -6.51799 | -45.93672 | 2024-11-05 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b8b2668-d307-361b-8dd7-3f3ec3ef2670 | -4.89047 | -46.71238 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45a773ca-066e-3e44-beab-995c4e1a5514 | -7.19813 | -38.82032 | 2024-11-05 04:08:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7ee1b9cd-6a8f-3bf9-bd40-f9814ed55838 | -4.41082 | -43.11212 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d9f47109-9fb6-380f-96d4-5accfe74c23f | -1.92874 | -46.45718 | 2024-11-05 04:08:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec34c525-5cc0-32fe-979a-99edf2fc75e4 | -5.47023 | -47.56627 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 689d54ea-8328-3cb3-930c-6ebcfbca505f | -5.29564 | -40.54026 | 2024-11-05 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e65a4ce-dcee-3592-9411-65ca20cbb7f6 | -3.31648 | -40.03365 | 2024-11-05 04:08:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a592d4a-2ec0-3e35-85d1-be7559e887b1 | -4.41446 | -43.11221 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd4c0e7b-096d-37cd-8104-ed0eb7a070ba | -4.3794 | -41.70399 | 2024-11-05 04:08:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3820b863-82aa-3802-ad45-64a5bcaff988 | -3.55725 | -47.38363 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| bddbad07-c9e5-3d75-8492-7a873e83f527 | -6.11075 | -43.97359 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fbf33d79-542d-3f8d-b254-f7cb4cc17856 | -6.51274 | -41.41866 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0729f428-452b-3f96-9a07-5ba7fbe35311 | -6.17869 | -43.96074 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7af0d095-ece4-3857-940b-f411e9a68e35 | -4.24516 | -48.04131 | 2024-11-05 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 79159185-29ae-37eb-99b2-8d497d62fa25 | -5.61071 | -41.64024 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 761cbcce-745e-385d-8a86-60aeaed39863 | -6.51381 | -41.41177 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8e66c925-b283-3f5e-bcda-5de88d9eb538 | -4.24519 | -50.36422 | 2024-11-05 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0abd47c7-9172-3f20-ad63-e12bdc57a7e1 | -6.47082 | -42.20924 | 2024-11-05 04:08:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b5d5486c-af67-385c-8943-6abef9caae05 | -4.38852 | -43.12008 | 2024-11-05 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c2c835d-f4fa-3e35-a887-cebd1667fcef | -4.28868 | -48.62017 | 2024-11-05 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2ffcefc-1d6b-3d73-ba9b-8d430243e21a | -3.55654 | -47.38799 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| 90ab70f1-ee1d-38cc-9d1e-660d28e1457c | -5.34934 | -41.61652 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5acac04-90f8-317b-b1d9-f0f61344cf48 | -7.55754 | -38.76648 | 2024-11-05 04:08:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d7ae89b-2ddf-3c78-b972-4e8c7d2e589a | -3.02634 | -53.26406 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 522d5d56-b865-3a72-a5e2-5600b1a08ab5 | -4.6033 | -46.87843 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 910c726a-4fd4-35c8-82ab-704d7782ffbe | -7.65241 | -46.0069 | 2024-11-05 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bd77f02-0c6c-3720-9cbf-80dd92f4eda9 | -6.98534 | -41.31285 | 2024-11-05 04:08:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60674922-b6b7-3207-86cd-e89a9f7e3601 | -8.39994 | -40.80051 | 2024-11-05 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 78be26a2-e3c0-3bca-a432-4fe48ad3d64f | -5.69155 | -45.84134 | 2024-11-05 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0982766-648b-3b39-85fe-8ccb9da67f29 | -5.37121 | -46.45241 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3834145e-3a66-381f-a096-abc4f93d0592 | -4.53742 | -46.41643 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b1533bb-5864-3c63-9abc-2470ff502d0f | -6.9449 | -39.80423 | 2024-11-05 04:08:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2fa05cc8-96b3-359c-84bc-ea60871577f1 | -3.07834 | -54.50888 | 2024-11-05 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 390af4d8-a9ad-36ba-9fb7-02ca4362a283 | -3.35492 | -41.66367 | 2024-11-05 04:08:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85808138-e4c5-3ff2-89bc-7b4197b61e8e | -6.24904 | -43.56588 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b6930ae-e7df-3dac-b129-b0d09733c214 | -5.07425 | -43.71507 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5ebca35-11b4-3a5d-ae1a-3ea9064fa526 | -4.3772 | -47.256 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ba9770-412b-37a4-a3cd-4db8d65093c8 | -8.18467 | -41.05347 | 2024-11-05 04:08:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2c880630-7e32-3da2-b1c1-33ff0de4659c | -2.64784 | -48.57563 | 2024-11-05 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d6bafe9-5782-375f-839b-c4029d49c775 | -5.83276 | -44.91766 | 2024-11-05 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d56822de-65a1-3e9c-a143-418a3d48e676 | -9.03198 | -37.67348 | 2024-11-05 04:08:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eba99ff2-6c6c-3ecb-87c7-ee7e14a523f3 | -5.9347 | -43.64455 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 571b672f-95b8-3c06-a6b9-20db7bac3f4f | -5.43116 | -46.52157 | 2024-11-05 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57fc3270-aaaf-3a43-926e-f4bc4ca18e0d | -2.81635 | -51.49269 | 2024-11-05 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 414e09e1-d660-394c-afdf-709a7f8fa0aa | -5.66284 | -45.20279 | 2024-11-05 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2725f075-6af3-3151-91e2-6102a0e64425 | -5.51176 | -41.66725 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c453f702-4856-3e8f-9157-32664a7166f0 | -4.05458 | -46.94178 | 2024-11-05 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 85a1bc14-b618-3fb4-8fe8-69869c2e4169 | -4.42959 | -45.85474 | 2024-11-05 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4158096a-232b-3d29-8f78-341065f1cae4 | -6.95916 | -45.19079 | 2024-11-05 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65ca7143-2230-36de-8657-99fcd8a542e7 | -4.6004 | -46.86981 | 2024-11-05 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a640b538-6e67-3512-9560-608df508c913 | -4.42916 | -46.28687 | 2024-11-05 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfe2fa7d-c80f-39ab-98e8-db1eac4d82cc | -5.06536 | -44.22886 | 2024-11-05 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0560d0a8-e922-3491-9f2d-82b584b6d2c8 | -5.93125 | -43.64401 | 2024-11-05 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98daffd6-d599-33e9-802d-632f34a91531 | -5.07528 | -43.71864 | 2024-11-05 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e557557-a6ef-314f-89f7-251c4f721c12 | -8.32097 | -43.56926 | 2024-11-05 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a871c392-4c6d-37f2-bf5d-92061aa60b9c | -5.86254 | -42.65913 | 2024-11-05 04:08:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bcebe63-d5c4-3150-8c17-a38d68cd1fbf | -6.4681 | -42.22659 | 2024-11-05 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6f812da2-a53d-3b49-b1fb-3e4b8bff19d4 | -4.11385 | -49.53535 | 2024-11-05 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0189e8e-014f-3af2-8984-41dfc904bcb9 | -4.50377 | -45.64638 | 2024-11-05 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eafcc7c9-203e-3e0a-8f6d-b9e8c64c331f | -5.61371 | -41.75399 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dac15e86-52c4-3f76-aef5-457e9ae662bd | -3.5432 | -47.38611 | 2024-11-05 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| be613c43-ec33-3dd2-9f82-bd635c266701 | -3.04516 | -53.27276 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e227b562-7d68-35c1-ad5b-ce5bf7ff9f0f | -3.03678 | -53.27332 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
