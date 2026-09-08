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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1aa9dff9-9335-3302-947f-80e05dbfd666 | -4.36169 | -47.77306 | 2026-09-08 00:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b0e6419d-a7d1-353a-945f-e7aa26657882 | -6.62053 | -44.71175 | 2026-09-08 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d1ad39f3-5f77-3458-ab23-3e705d09fafa | -4.57592 | -47.18742 | 2026-09-08 00:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 03e7908b-2bce-3f17-b815-c185f65f2e63 | -4.03918 | -50.88463 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2a0046ef-da70-30f5-b1e5-f8958191b924 | -4.72447 | -48.8439 | 2026-09-08 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8916d318-c82a-3ef1-9f90-dccc6ca50c09 | -3.92368 | -49.05144 | 2026-09-08 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 03f31170-0fbe-3c02-a94b-20b63104f366 | -4.98403 | -50.64038 | 2026-09-08 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e34aa03e-fcbc-36a7-8502-7cf8817f9fdd | -3.54012 | -48.17708 | 2026-09-08 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 4f30e389-42fb-36dc-af4d-bc1d52c5d1c6 | -3.54163 | -48.18768 | 2026-09-08 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 139e1fc1-368d-3309-acaf-6dce78d9e597 | -6.62319 | -44.72897 | 2026-09-08 00:05:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| df9a890e-69be-3390-9bd5-9348fee475e8 | -5.62733 | -44.25316 | 2026-09-08 00:05:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6ee2f9bf-7594-3ab6-b796-baf6fdf9d8b1 | -4.56914 | -47.21263 | 2026-09-08 00:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 93675d29-e38a-3992-beb3-b574818dedf4 | -5.9974 | -57.72402 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a475053c-fb29-3e99-bb38-3b61fa498efc | -3.54975 | -48.17578 | 2026-09-08 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 392.1 |
| d7b6d9cd-c18a-3e5f-9121-3d9dfcaee000 | -6.65138 | -51.17955 | 2026-09-08 00:05:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b898da9-566b-30a0-8be8-7c56a140288c | -4.16967 | -50.0865 | 2026-09-08 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3634067e-726e-3c09-9241-ef4fb13bd50a | -4.04796 | -50.8834 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 83ce558e-f756-3c92-a39b-94afbbb06f5c | -7.3724 | -47.75551 | 2026-09-08 00:05:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ca22eb2-c465-3084-9b8e-5b885c20b3a5 | -5.76821 | -49.12413 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 92901db8-0e1d-3f0a-8dff-fb1f7e3b71da | -6.96174 | -50.42282 | 2026-09-08 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| babe39fa-b82b-3fa3-929a-ff160cfea1fc | -5.98358 | -57.72596 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 1380fe77-bfa6-3196-90ea-505d064dfc24 | -6.77628 | -58.97242 | 2026-09-08 00:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 24d5d47c-0018-350b-91a4-e0178a56ef5d | -4.36325 | -47.78409 | 2026-09-08 00:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| da9e68d8-fd7c-39a1-8791-ed2de9a8428d | -5.49626 | -48.17905 | 2026-09-08 00:05:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c6071330-9913-37b9-abdd-fc368554069b | -3.69626 | -49.541 | 2026-09-08 00:05:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 6c9a6d9f-3b69-3b85-8a74-71d6d40aff2c | -5.75794 | -49.11621 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| a0e68dc3-c2aa-38c3-af7a-2d5819e3b804 | -4.57424 | -47.17549 | 2026-09-08 00:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 135.9 |
| eb1fb7a9-ff43-3b85-a586-95dd4616470d | -5.75666 | -49.10699 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a9670c53-d1aa-39db-9d6c-731d44a3097a | -3.32952 | -44.59437 | 2026-09-08 00:05:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 312c8323-205f-394f-b877-3ba2bada8274 | -4.98523 | -50.64915 | 2026-09-08 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5cdf9a2f-ed79-34c7-a7b5-ac37da5fefae | -5.76693 | -49.11491 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 75017246-c1e6-3df6-8887-b23949c0481a | -4.1094 | -49.06129 | 2026-09-08 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 88f60af2-e23a-3856-bb19-181210f8c14c | -4.11071 | -49.07079 | 2026-09-08 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 314d0a78-88a5-33e6-94f8-2099fb83de65 | -5.75922 | -49.12542 | 2026-09-08 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 52b140ac-a5ab-3890-bbd6-bee465a582bd | -4.05675 | -50.88217 | 2026-09-08 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e5df9769-be4a-3373-a7ef-182e1ce6d13d | -6.69753 | -47.41653 | 2026-09-08 00:05:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e89f8f06-d462-3945-98ad-afddcc39851d | -5.98956 | -57.71965 | 2026-09-08 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a3a15bc1-de7d-3b62-b302-5ac283907ba1 | -7.37386 | -47.76567 | 2026-09-08 00:05:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e5b8d33a-54ee-3cf8-9617-ee859532c27c | -6.91346 | -44.95554 | 2026-09-08 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 740941f7-cd8f-3985-b2f2-5f2d7f834278 | -4.70291 | -49.15477 | 2026-09-08 00:05:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f73458b4-99d3-3d3e-98f9-ab7bbf6b1516 | -6.64727 | -51.49207 | 2026-09-08 00:05:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4bf115ac-2a18-39d0-a28c-100b4cb780b7 | -2.75658 | -49.47947 | 2026-09-08 00:07:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2f41e711-e787-3a4c-977b-2c51925789d4 | -3.05414 | -59.28027 | 2026-09-08 00:07:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 959c575b-ed4c-30af-a67e-57c1da64b571 | -1.19762 | -55.71014 | 2026-09-08 00:07:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ca2b1b04-9917-3b0e-9425-48858baca266 | -2.73336 | -51.3812 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4c8692e8-a764-330e-a1f8-4aaf3ce03ecf | -2.425 | -48.94482 | 2026-09-08 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 5f7ee6b3-3de7-3980-8f8b-2f465e3b1b83 | -4.06696 | -55.78146 | 2026-09-08 00:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cfbf54d9-4afa-30aa-a0b3-4f24c5a4f233 | -3.36238 | -50.39627 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eba31919-ad4a-3527-bd86-60cdacd16743 | -2.97062 | -49.56061 | 2026-09-08 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f698352e-edb3-3bb2-b33e-88afa3c2c1fc | -3.68599 | -49.53306 | 2026-09-08 00:07:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 384b0ee7-e6a5-34e0-9b77-935c804cca8a | -3.70376 | -55.4762 | 2026-09-08 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d50b399e-c07b-3481-a17a-30133978ae9f | -3.49226 | -50.60513 | 2026-09-08 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba078194-da9d-3516-a420-ec8462c6b231 | -2.97575 | -49.26637 | 2026-09-08 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27020f9e-304f-36a7-adef-ffe8710979f5 | -3.44144 | -53.05008 | 2026-09-08 00:07:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0d4e131f-3934-346b-8d4b-92f8bc472aee | -3.24397 | -47.25632 | 2026-09-08 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 73257c2d-96d5-3f31-a31e-e1e67a33dca9 | 2.51127 | -50.8582 | 2026-09-08 00:07:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea1ed609-e01a-374e-87d1-689592626034 | -3.71468 | -51.14188 | 2026-09-08 00:07:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a82110fd-28d4-380e-a088-6d25ccf77005 | -2.55184 | -48.42831 | 2026-09-08 00:07:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ba3bacc5-4396-3255-a18b-6af2bcea27c9 | -3.06678 | -49.52182 | 2026-09-08 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 487b0517-2e10-36c6-93a2-5979cf57303a | 2.06201 | -50.83992 | 2026-09-08 00:07:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62de96b8-c154-3bbe-98a7-57781fb07581 | -1.20142 | -55.73789 | 2026-09-08 00:07:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a0e0d73d-23df-389c-a9f6-882b4661eae3 | -1.47804 | -54.84263 | 2026-09-08 00:07:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 1498be7c-1930-3d6f-8185-f71f2a897a7f | -3.81833 | -55.89507 | 2026-09-08 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bea2b8f8-4884-3496-8a4f-3f4854f28799 | -1.87347 | -47.98465 | 2026-09-08 00:07:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4789a604-66e1-33b0-96f8-ab12bebb8d3b | -3.3712 | -50.39502 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7dcd076c-a792-3a05-9c2d-44baa29029c8 | -1.70836 | -55.17528 | 2026-09-08 00:07:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 84ac8de6-d690-3e0a-9b74-3f0ea264eda2 | -3.26659 | -50.02949 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 118df7ae-e7b1-3f41-9382-c73f718d0759 | -2.63351 | -46.77534 | 2026-09-08 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a04b1971-0fbe-3ac1-9fec-5ddba8d8f8dc | -3.34063 | -53.41 | 2026-09-08 00:07:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5e926ddf-7109-391d-a30c-7831e0a6e63f | -1.2033 | -55.75164 | 2026-09-08 00:07:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fc8e60cd-2ba9-353f-85b1-60813ae594f3 | -2.96891 | -47.33881 | 2026-09-08 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 36f1da4b-c7f8-3b16-9165-9febef37064c | -2.84298 | -53.98669 | 2026-09-08 00:07:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23cc3313-f403-322a-b0a3-c517f7a33609 | -3.24221 | -47.24405 | 2026-09-08 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| a08580db-da53-3c42-91bb-55e8dc0543fd | -1.09532 | -48.05595 | 2026-09-08 00:07:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c7ef3997-e58b-3b21-bd00-4cf378b7b64c | -3.88791 | -55.81679 | 2026-09-08 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8a5fb9c9-35f2-39c2-a9e7-6f1ca1b18d5e | -2.72957 | -51.82839 | 2026-09-08 00:07:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 16439542-a1ba-3c7d-b78b-63e26effa855 | -3.68727 | -49.54227 | 2026-09-08 00:07:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f68685c3-458a-31b2-ba56-a2f204cdf645 | -2.88286 | -50.45824 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8cfc88fd-25e5-3eba-a486-4d217bca1791 | -1.19952 | -55.72404 | 2026-09-08 00:07:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 49efcd56-04bb-3d16-af59-00969181fa85 | -4.06774 | -56.29407 | 2026-09-08 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0372de29-d92e-3997-89ac-7de710800ee3 | -3.88996 | -55.83208 | 2026-09-08 00:07:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 6193e1d8-326d-37f2-b293-147dafc3ab62 | -2.60963 | -51.21744 | 2026-09-08 00:07:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8eef34b-b2db-3780-9303-3b22211714d0 | -2.97708 | -49.27588 | 2026-09-08 00:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7cac21b-50c1-3171-8076-0c3466ddbd54 | -1.97202 | -56.49714 | 2026-09-08 00:07:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 69eb6fe9-5972-35b9-bd96-49156c6c114e | -0.9323 | -47.18967 | 2026-09-08 00:07:00 | TERRA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e7eccd96-e0ec-3f78-99b5-efc8a1af2682 | -1.4797 | -54.85458 | 2026-09-08 00:07:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce1ceabd-8725-3918-930a-ace72bdf236b | -2.30631 | -48.57766 | 2026-09-08 00:07:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5cd688f6-2c49-3bea-ad7d-4c97104fab7b | -2.75788 | -49.48884 | 2026-09-08 00:07:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb267a59-c1b0-3b15-bd08-ea176da34985 | -2.9792 | -47.33746 | 2026-09-08 00:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0d36568e-1efe-3c86-b307-3d3b55cd421e | 3.32256 | -61.31914 | 2026-09-08 00:09:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 08f78f86-e4cf-34bf-9fcf-5ed1bed07cb1 | -3.5406 | -48.1889 | 2026-09-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 216.1 |
| 127f5156-24ee-35d2-bc1b-eb637b8e4189 | -3.5591 | -48.1882 | 2026-09-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 321.4 |
| f8782299-dd61-3372-973b-03c33f3535fc | -3.5407 | -48.1673 | 2026-09-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 1456ee81-b4b5-3987-92dd-1449ee6f18ef | -20.4984 | -57.4227 | 2026-09-08 00:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 181bae79-4b24-3b7b-80a9-460a85149368 | -6.1304 | -47.2224 | 2026-09-08 00:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 30ca1d9f-983c-3c7e-ac52-8a1c26405f03 | -21.9721 | -56.0525 | 2026-09-08 00:10:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e3817769-8993-3b35-bdbe-15c1d72dce99 | -13.2859 | -61.7123 | 2026-09-08 00:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2382b0c3-451a-35e4-b7d5-8272ff5f8319 | -6.6357 | -59.4459 | 2026-09-08 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 505c16db-a5eb-3c74-b92d-078dfc8e831c | -6.1116 | -47.2457 | 2026-09-08 00:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 68986786-168b-3937-846e-16facb73f52e | -13.2479 | -61.7148 | 2026-09-08 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |


[Clique aqui para ver as próximas entradas](README3.md)
