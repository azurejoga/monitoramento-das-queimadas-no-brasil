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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4af0b81a-e5af-3b86-9cf8-38a4826b390a | -7.6851 | -48.7386 | 2025-09-03 05:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c1885097-99a9-3f27-a3fb-2cb57985e60e | -17.4431 | -47.2044 | 2025-09-03 05:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fb55e754-b584-3e73-8d27-1a8edbdc5a71 | -7.7036 | -48.7587 | 2025-09-03 05:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ba499ac8-eb50-372a-bbd5-88d4c9c14cf7 | -7.6849 | -48.7602 | 2025-09-03 05:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7a77333b-1421-37d3-b544-c0c8ff8701af | -7.7039 | -48.7371 | 2025-09-03 05:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 9b1b17bd-6db9-3913-bf5a-b9626ff04be3 | -23.66746 | -55.22219 | 2025-09-03 05:40:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8ffe0dcd-b77c-31bd-95de-2bd702fb9816 | -23.66701 | -55.22783 | 2025-09-03 05:40:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f9e5978d-0024-3b2c-a9a6-9836af5349fe | -23.66998 | -55.22063 | 2025-09-03 05:40:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d8f3531e-0579-36b1-a515-502d008c2332 | -23.66957 | -55.22624 | 2025-09-03 05:40:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a972519-3328-3771-a7d9-147417afb9ed | -7.7039 | -48.7371 | 2025-09-03 05:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 120.9 |
| b6f86b7d-4468-3e15-b1ca-d5fdfe856f8b | -17.4431 | -47.2044 | 2025-09-03 05:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 8c752994-690c-379a-a509-da418060a85f | -7.5477 | -61.3247 | 2025-09-03 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b9679ea4-02a4-3181-bc5a-375a897d3645 | -7.5476 | -61.3437 | 2025-09-03 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 57a7f273-6fc4-30cd-8d36-a301590ae21b | -7.7036 | -48.7587 | 2025-09-03 05:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 86.7 |
| fc23e09a-9f54-3425-ad93-9904faef908b | -7.5291 | -61.3444 | 2025-09-03 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 15a9803b-0fe3-3570-b9ee-7fdff962ceb9 | -7.7039 | -48.7371 | 2025-09-03 06:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 44a01510-c569-3306-a289-2f46d32e4cb7 | -11.8078 | -50.6499 | 2025-09-03 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| da65a30a-c8f1-3a9c-9325-d7e1390fa512 | -7.7036 | -48.7587 | 2025-09-03 06:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2ce47bef-2a40-3c1f-8515-d8fcebe8fcdc | -7.5291 | -61.3444 | 2025-09-03 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e73e71a9-b525-3611-b904-4af7e0c7d989 | -7.5477 | -61.3247 | 2025-09-03 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 32d41094-1c26-33df-9403-78f2e7c4a136 | -7.5476 | -61.3437 | 2025-09-03 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b7518cc2-bad1-3a06-a027-735bddad9bf5 | -17.4431 | -47.2044 | 2025-09-03 06:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 28799a43-7eb9-3ec7-9fc0-c445d48fd8c8 | -6.4648 | -49.5151 | 2025-09-03 06:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 2a186dfc-abca-333c-82d6-c394ca6343b2 | -7.5477 | -61.3247 | 2025-09-03 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 161a4843-8c3c-35e5-be78-9305d0477c14 | -7.6849 | -48.7602 | 2025-09-03 06:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 065666d4-9b06-3d10-a87c-713af442dfa3 | -7.5291 | -61.3444 | 2025-09-03 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8c62a164-c73d-3313-8c81-b892f081fb50 | -7.5476 | -61.3437 | 2025-09-03 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0738caac-dce7-3250-96a4-31fedf0396f6 | -7.7039 | -48.7371 | 2025-09-03 06:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 120.1 |
| c43cfb55-12e2-3091-81f6-2ed2d6e675b3 | -7.6851 | -48.7386 | 2025-09-03 06:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b47736a3-9b2a-304b-8e05-a5ce1c2340cb | -7.7036 | -48.7587 | 2025-09-03 06:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 100.7 |
| a0983deb-99cb-3f94-ac25-8e3be39f63ca | -17.4431 | -47.2044 | 2025-09-03 06:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c6cb50d6-8396-3336-b154-43359e9630c3 | -23.6978 | -51.7916 | 2025-09-03 06:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| df4fdc5b-2d2d-387c-853e-5cd354c85c64 | -7.7039 | -48.7371 | 2025-09-03 06:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 125.4 |
| e0dade5a-2d6d-31ac-a0f9-43e4d54b2ae5 | -7.5477 | -61.3247 | 2025-09-03 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3b8a5856-0682-3116-8e65-5936388b91d7 | -17.4431 | -47.2044 | 2025-09-03 06:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8bbb34cf-7e38-3222-b98e-91d9908e78f4 | -7.5291 | -61.3444 | 2025-09-03 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c4a62e44-0ddc-39f1-9ba3-ec1f8c8a1eba | -7.6851 | -48.7386 | 2025-09-03 06:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9ac840c5-999a-3749-b8f6-16cc8bdc707e | -7.7036 | -48.7587 | 2025-09-03 06:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e70acba0-a060-363a-9500-704ddbd532bc | -8.8845 | -45.7994 | 2025-09-03 06:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f906b298-3aa7-3705-8126-8dd166569855 | -7.6849 | -48.7602 | 2025-09-03 06:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 27056b30-fba7-3351-bac7-300a828efeea | -7.5476 | -61.3437 | 2025-09-03 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a9899669-a02e-3c02-88a5-0f232477f7ba | -16.1492 | -49.4738 | 2025-09-03 06:30:00 | GOES-19 | SANTA ROSA DE GOIÁS | GOIÁS | Brasil | 5219506 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 7b632366-27e2-342a-b378-76d33548c505 | -16.1487 | -49.496 | 2025-09-03 06:30:00 | GOES-19 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 6649794a-47db-3bed-91d6-83cb33e81048 | -16.1683 | -49.4927 | 2025-09-03 06:30:00 | GOES-19 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 745e4069-d300-3895-8513-4580e43f8ae6 | -7.5477 | -61.3247 | 2025-09-03 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 48de8412-b2db-3de2-a162-5e9c26ae821a | -15.1771 | -52.356 | 2025-09-03 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 12a57d46-7793-374e-b711-285bb6a6da8f | -7.5476 | -61.3437 | 2025-09-03 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8615cff8-3397-38c8-83ca-cb3c647e4664 | -7.7039 | -48.7371 | 2025-09-03 06:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 167.9 |
| f22fa722-22af-3784-9d5d-00960a53ba5d | -7.6849 | -48.7602 | 2025-09-03 06:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 69c5cbfd-cf72-3dfe-bb06-2ec8eb67d662 | -7.7226 | -48.7355 | 2025-09-03 06:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f8980c06-a4e5-3c7b-a254-f25f9caaf037 | -7.7036 | -48.7587 | 2025-09-03 06:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 6bc96f4c-e067-31ec-aabe-febabaaf0c65 | -15.1576 | -52.3586 | 2025-09-03 06:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d557f855-eff7-3ba9-9af3-dd5e2b1acbd8 | -7.6851 | -48.7386 | 2025-09-03 06:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 36773b0f-c973-3f5f-910a-da28691ede3c | -7.7039 | -48.7371 | 2025-09-03 06:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 130.6 |
| f19b7013-cb67-3f42-bee9-c97c77bb6c1b | -11.5779 | -52.115 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 204.5 |
| 2fcbe24c-98a6-39f9-b7b2-fe5b6355b251 | -11.5966 | -52.134 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 592.7 |
| 867c2edf-9c23-3379-9293-8d9071e233c3 | -17.4431 | -47.2044 | 2025-09-03 06:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 34218ac2-3bf9-3f48-adc5-eac8255123fc | -11.5774 | -52.157 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 7eface51-189a-3706-b1ab-4f9f8a582ae5 | -11.5776 | -52.136 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 356.3 |
| 03c225e3-526d-34b6-89d6-1911bbb64ee1 | -11.5963 | -52.155 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 827993a4-0aec-380f-874d-b154c21c94cb | -7.6851 | -48.7386 | 2025-09-03 06:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4cf0a9c4-3182-31fd-9b14-df142b4cd138 | -7.6849 | -48.7602 | 2025-09-03 06:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d96868d6-2728-3fba-a87c-8437050d6173 | -7.7036 | -48.7587 | 2025-09-03 06:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 9625f4f5-f7cf-334a-a6e1-2b606d8fabc9 | -11.5969 | -52.113 | 2025-09-03 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 298.8 |
| a2fe732e-a565-38b9-bc96-6f093af354cb | -11.5774 | -52.157 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 110282f2-712f-3f77-b6f1-09c9434f9fde | -11.5779 | -52.115 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 226.2 |
| ae28b3e1-b6af-3338-a74e-86b2aa6b4c9c | -11.5963 | -52.155 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 4aa8a1d5-3954-37aa-ac7c-c4efdfebd038 | -11.5966 | -52.134 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 717.5 |
| 1ad2908d-998d-3d2b-be7a-752c91264675 | -7.6849 | -48.7602 | 2025-09-03 06:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3dbc55ab-f988-3407-8151-5a4d0beff2b9 | -7.6851 | -48.7386 | 2025-09-03 06:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e9089d63-5a5f-38b5-8ba5-7806f86c9910 | -7.7036 | -48.7587 | 2025-09-03 06:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 91.4 |
| caead057-54de-3c2c-ae5c-7e4edbe053a6 | -11.5776 | -52.136 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 471.0 |
| 567600e4-b6e6-3f36-88dd-824cfc4083d3 | -7.7039 | -48.7371 | 2025-09-03 06:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 55381dbf-0720-3778-9644-03b22d869f91 | -11.5969 | -52.113 | 2025-09-03 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 294.9 |
| f0371273-1bd8-3fa1-8ca4-129d377d94d1 | -7.7226 | -48.7355 | 2025-09-03 06:50:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9983ce05-c7f6-3a5c-ae94-ef6d61b44aca | -5.92619 | -57.72505 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0c3e7985-0cf4-38c9-9ae2-56025bd29bd9 | -11.58489 | -52.15116 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 235.9 |
| 403dabd2-046a-367c-8d5c-000872e319fb | -5.90642 | -57.72209 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 98c64959-a672-3895-b871-48fe45cb79c1 | -11.58542 | -52.10534 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 461.2 |
| cb2fae13-b512-3e9d-b6d6-05796fcac1f2 | -5.8588 | -57.77314 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2fc3675c-6870-389b-830a-5a2d88074a96 | -5.91631 | -57.72354 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 89da2790-5473-39fa-9ef3-61b35a7f1be9 | -11.58903 | -52.11331 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 439.9 |
| 2ba99242-598d-3cd8-b88f-4bb8c0ee1cf4 | -11.6059 | -52.11512 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 57935808-b4ec-31b4-a7bc-87fc97a3062c | -5.91468 | -57.73479 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 9091f80c-6cac-3167-817d-a03eec356e61 | -5.8719 | -57.75176 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 5af12b64-6b7d-3b3a-9e44-85bd51e59ee6 | -5.91795 | -57.71223 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| fc8e42a3-d6e7-3b6b-8817-f970841bfbcc | -5.90806 | -57.71072 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 135d450f-55a2-39e0-8a90-cbcc0e050c0e | -11.58103 | -52.14319 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 433.0 |
| 467afc0e-9860-3ba0-8099-7fd12fd839cd | -5.92785 | -57.7137 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 9ff6a040-29af-3bde-aef6-4b6898306b62 | -5.89326 | -57.74337 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 33644736-fd08-39f4-b559-f853a9424156 | -11.60229 | -52.10719 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ef34aa30-878c-395c-ba02-0720fd876894 | -5.8703 | -57.76302 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 4a89f510-e478-3352-91ef-fb148f5e6637 | -5.8949 | -57.73198 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| af98b407-7ede-341f-9975-5ff57481a03d | -6.33133 | -58.17341 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b9d8cef-5e9f-3610-a405-bd2cbdd1ccf8 | -11.6068 | -52.06863 | 2025-09-03 06:52:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 4b69ddd4-2727-34a8-9bd4-b3736c71e2fb | -5.86202 | -57.75042 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a867e1ca-5f65-36ee-9afc-f9fdc49aabcc | -5.8687 | -57.77424 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 79698088-86e3-3825-861a-c23be6428fc6 | -5.90313 | -57.74485 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 514c4dc6-4cb2-3d98-ac72-cf1efd175983 | -7.33251 | -59.64702 | 2025-09-03 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5e57ccc6-f331-3e02-abb3-49971bb9d82d | -5.8604 | -57.76184 | 2025-09-03 06:52:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |


[Clique aqui para ver as próximas entradas](README108.md)
