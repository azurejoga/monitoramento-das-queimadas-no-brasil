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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34607f52-3a7d-3689-98b4-bc96d5b1c08c | -3.38064 | -44.44793 | 2024-11-22 04:36:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a83e828-ec8f-31aa-9aff-ab12ef943941 | -3.20782 | -54.24491 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 045a124d-fa68-31c1-a571-e2a6cf876467 | -0.80936 | -51.79515 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2a751e1d-87a0-3fee-b253-57f7fcbb5c69 | -4.13693 | -46.7077 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2af1c697-5829-3357-811f-e7e294621321 | -2.61994 | -54.05555 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30019530-b22e-36b4-9cdf-fe68c9dfcc4c | -2.83465 | -51.82351 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb82184-a82c-38da-a61e-58e284891070 | -0.9363 | -51.65734 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cc8e1b4-2eb4-3e92-b34f-813797ce6da7 | -4.1372 | -54.6591 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 738bebf8-21c2-3b8a-82cb-bad7f70b4ccf | -4.00804 | -49.92542 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aff11639-e5b0-36fa-858e-748980b07cc7 | 0.29762 | -50.8415 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c62a8c3-7255-3723-800f-58c7feaba9d2 | -3.57415 | -54.68721 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36f28f65-fae3-3a36-9812-22adc1f123b4 | -1.18664 | -51.94865 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30103ff4-f5ac-3089-b7d9-ad7bce810ea0 | -2.80526 | -54.02677 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1c6f495-521b-32ce-ac0d-5fafae5374fb | -1.66564 | -46.93534 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a5cf44-7d84-3603-bf1c-a6ab851413a6 | -4.73496 | -46.67197 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d9fe30-7647-37a3-bc2e-3e37ded2067f | -2.00522 | -54.52443 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30812992-2399-36aa-92d0-46dd19318176 | -1.77245 | -53.60456 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c028789-72e6-385a-944b-bea163f95b0d | -3.76139 | -49.93693 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e7682c-4bdf-38f0-a63e-8e5fec98d53e | -1.50973 | -53.13593 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d3ab055-f5bc-3fb8-8381-131e3b31279d | -2.41127 | -47.83076 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aff8da52-ccda-36d9-9a0d-3c99f198eef2 | -2.56262 | -48.16511 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f47de00-f5ba-316f-9d51-ab62288d883b | -1.56403 | -51.17908 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e57da97-245b-3dc8-a711-89c9497f9405 | -3.87497 | -52.36441 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0cccaec-6851-3ecc-ac23-4b7294a0674a | -3.80304 | -51.26501 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20546eb3-03c2-33f0-932b-9b20f137ce77 | -2.71694 | -53.17186 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 351a2d09-92e6-396e-8cfc-b34e03e344a8 | -3.24448 | -54.23882 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e6c024bb-3238-3820-80a0-38f9ee040c8b | -3.52391 | -53.80619 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 682fd1c4-161f-355a-88b4-dc2d2208e9ac | -3.14816 | -51.12577 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee654855-97dc-33ed-b641-30b36ca2e9c4 | -3.25092 | -54.2517 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 05194c48-72ba-3956-93a1-56eb7ef3ae6d | -1.21957 | -51.73869 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8815b2bd-d133-3bf8-9e51-0105dce91cb1 | -1.64048 | -52.69768 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2d51efe-59bd-3184-8d08-16455e427ef7 | -6.26804 | -44.54523 | 2024-11-22 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 174ed4bf-305d-383f-8803-4af10f0d8280 | -0.94502 | -51.6499 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 936a0bc7-16a9-33cb-be8a-3f568285e1b7 | -6.27202 | -44.54578 | 2024-11-22 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e1485c7-4938-3151-900e-cf7d1268a813 | -2.37201 | -50.42704 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aacfcf2f-d5fd-30d4-9c48-4da2afd355cc | -2.36005 | -53.68239 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96726872-ffad-359b-a155-af3d4b85dc98 | -2.95712 | -51.41478 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c257db4b-1288-3a5c-b115-5a53b054ce1b | -4.9621 | -49.84218 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f9bbb1d-f15b-35c5-9386-7e8c56fc32bf | -2.40736 | -48.33136 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8007b98-6413-3ed2-a668-bbe81a031720 | -3.63881 | -51.45567 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 171bad6e-1b3e-304d-874f-728426c4776a | -2.09085 | -50.49855 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db1d2b6e-45af-3bfa-84f9-b268b964f17f | -2.40435 | -50.31136 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1498e47f-5ae0-305a-87b0-ba8da1fb0490 | -2.46217 | -48.80389 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3034b30-0568-3262-8275-d2a42126fd07 | -1.80778 | -52.16295 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a54894e-a6ae-3bd2-a128-ef8f3df002dc | -2.80646 | -54.01929 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5e2372-21ae-3d7a-9dff-8af4d0c96d12 | -3.09911 | -53.16999 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674c6fcd-f5e6-3d0c-8242-64ccd152b6ba | -4.40347 | -44.1193 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17945bf-e10c-3a7c-a0b2-f58599aa50d9 | -1.94086 | -49.52251 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 847d3ad1-3db5-389b-8178-e161e5c19e24 | -2.69004 | -46.18721 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eab6615-08dd-3b1c-8269-93b5ddd38d5a | -3.29164 | -53.85206 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ba157a-0539-38e6-aa91-ff9f9e7df0ee | -2.79157 | -45.94837 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b71c7677-7ce7-3b55-a3c9-76de8e5f687c | -4.19735 | -53.77636 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae35f59e-1989-3f66-a698-9dd3362f9f80 | -4.1864 | -53.57689 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 009141c3-0218-3795-875b-4e8196199dd9 | -0.81047 | -51.79757 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 06979dca-4a00-3519-a2ee-bb48866dc00f | -0.93768 | -51.64876 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e86ffe72-f5bc-325f-b0c2-1d38c1308428 | -2.65835 | -46.15167 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2deea5ff-7a12-308c-a0f8-d8d89240745f | -2.38382 | -50.33069 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c562c767-31d3-3004-9f77-a26084ca8380 | -3.20656 | -54.25275 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37f37396-5448-347d-bf46-387ca778e6a1 | -2.70892 | -54.14011 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5522e4f-62da-30fe-88b9-5b540733ef92 | -2.74126 | -54.13256 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4af22d73-56ef-3aed-808c-f71d788bf16a | -0.06177 | -51.24708 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12c7f856-d9e5-39aa-8ce9-5066b4f330f8 | -2.78431 | -51.7217 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e5ea5ee-ea60-31a7-b366-fc0759461fc7 | -2.66723 | -48.66741 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62eb9cc3-c43a-3497-9ae8-f328e01a679a | -4.44636 | -48.19704 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4ef95fa-5c7d-31c1-8ee5-382582bc0e2b | -1.74717 | -56.18236 | 2024-11-22 04:36:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdb0e6f9-6f77-3e14-bb46-4fdaf963a541 | -3.23639 | -54.25377 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ad28274b-8e77-3fe7-be4c-8e4a92433bbc | -3.95922 | -51.13519 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f5deb22-c033-39fe-bb97-7deffe8182b0 | -2.64237 | -48.82541 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e440731-46cc-3e91-afde-dd2dfa5c7e43 | -2.65434 | -46.24506 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a7eea9-86dc-3b8a-b578-25854b77ab00 | -2.94656 | -48.33845 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227372ec-9e47-38e3-a7dd-178d6aca3ae7 | -3.75984 | -46.12337 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0932b49-4354-3692-b931-c8e974068cbf | -3.68085 | -54.58946 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aabadd1d-25f1-37e3-bdb9-073235640f28 | -2.50708 | -46.21897 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f98239f-9f92-30d0-9078-41f61599d626 | -3.27531 | -53.82398 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 68b416de-6922-3c6e-82e8-6bff74a8fbd3 | -2.19826 | -50.67975 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff8dd0ab-70ea-381c-90cd-0251f01e999a | -1.59889 | -52.25883 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e604c75e-f2a4-3c63-8347-c8136d49938a | -2.80045 | -53.00534 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5f35b1b-f6af-3e5c-a95d-9db9c9470b52 | -2.26977 | -51.1377 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b1dfe2e-b8d8-3bfe-b78d-19489cfbf59f | -2.63415 | -46.57239 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a04e558c-688f-3645-b798-c0b40a88f768 | -2.69621 | -46.26245 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddd37206-fe30-350c-899c-ab7be149f424 | -4.40399 | -44.11583 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05597944-db07-34d4-bfaf-6ed19205ac35 | -1.63278 | -52.41317 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b06baaf-2d55-3ae0-8c84-f2ec8fb55597 | 0.46665 | -51.34622 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89252b50-e8c4-3ccb-94ca-6ec003040697 | -3.00317 | -51.30818 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c657c5d9-1778-3b34-841d-e97ce3b9f6bd | -2.19811 | -48.56236 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f06ff68-c44f-3e00-a412-9ab8769c4766 | -3.84338 | -51.14504 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bc4b955-9ef7-3d4f-a802-895e131f6762 | -2.1738 | -46.69478 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4b7f453-ae1a-3e72-9988-3c1b01a0aa8d | -3.56232 | -54.22033 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 637f5ade-4407-36bb-bb37-f171fc6d700f | -3.18223 | -54.32387 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5aa5869a-d286-338e-96fe-7599313b5ebe | -1.63141 | -52.62039 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73baf717-64ca-39a6-a638-320885334ceb | -2.70518 | -48.66277 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f9321d-2c1d-33e1-b17c-f10e2cb1329c | -3.6106 | -54.75069 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dc90df7-9327-3654-89da-83082294ad44 | -1.06017 | -51.7508 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82294dad-a6b6-39ac-bc24-117e29401440 | -4.88128 | -50.94332 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2617f4a5-9e69-3398-8e15-b841aa3ce06f | -3.83368 | -51.71031 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a51d04da-8762-3889-a080-9806b425d52a | -1.39218 | -52.34135 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 198b3f0d-6dea-37d7-a8fb-dfc9de631bdf | -1.19944 | -51.96433 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2fbeb1fa-2809-31a0-8475-2bbcf10b58cf | -4.48669 | -46.71277 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9366f321-6903-30ec-9e79-69a98464536a | -2.63114 | -46.25712 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 752c030e-b9c1-35ad-8392-75e31f55ad36 | -3.45348 | -45.90496 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README43.md)
