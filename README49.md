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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04a1cc85-2a35-3c09-8c31-579d6ea2806f | -5.04705 | -49.2331 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a151aa1-fb47-3f5c-bfb8-d4d5dbdb4ab4 | -6.6078 | -43.74689 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2e619e23-bd18-3140-b379-d94e049c197a | -1.92028 | -58.25858 | 2026-09-23 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3fbefee5-5ec6-3cee-803b-db4cfafdbf9a | -6.95554 | -45.30811 | 2026-09-23 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7737795-46f6-38a5-817f-11d64f99a427 | -3.86655 | -51.18667 | 2026-09-23 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 677d2583-478c-3ed5-a3cb-5d1a006d61af | -7.0323 | -44.64978 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9b654d70-ef3f-3541-b886-2aa078c0cc39 | -6.6096 | -43.73492 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 43e8d18d-3f39-378c-963f-fa53564d9b9d | -5.83335 | -50.21381 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac5a9b9-e695-3874-a731-2938bc23620d | -6.0006 | -44.26323 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d9343e1-9e93-300f-a688-38627b657336 | -5.57389 | -52.0229 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19ca089b-50f9-3e6a-afbc-e68f5a8abc94 | -5.18469 | -56.18129 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2062198-6c78-37bd-87b8-530916d6c019 | -5.41944 | -49.26835 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68736961-b316-3f79-9fa0-904bc32a7e2e | -4.22524 | -48.61514 | 2026-09-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b80d2e5-66a6-3af9-8be2-9ed6a37fc127 | -2.97014 | -50.3986 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6ff633f-573c-3ebe-a41b-de9c92863fd8 | -6.62375 | -43.73702 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07fbc42c-273f-35ff-947e-18df3fe602b0 | -3.81825 | -59.01357 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 927220d0-3249-3a17-8e7f-10be590eb10d | -3.25231 | -53.96059 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a490ba49-98a0-3d32-b894-3bb0b2f8b482 | -2.16855 | -48.31832 | 2026-09-23 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f2fadd4-e558-37ec-8f32-c01c1dbfc71a | -5.99802 | -45.23355 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 082b3f18-29c9-31e9-89d3-16fdc944955f | -2.73917 | -51.54428 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5287dc0-3c27-3fc3-9467-03b605958d14 | -5.19036 | -49.33937 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd1e84c-3450-33ee-b640-9ac58925b0b2 | -6.12961 | -43.72651 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a883b53-bae7-3351-801b-8c26714c0948 | -5.41652 | -49.26368 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 706955eb-6d48-3745-8e33-735a3ba86a10 | -3.86031 | -58.81749 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 31d50744-3faf-3ceb-9a9a-1f023d108c07 | -2.32567 | -47.19764 | 2026-09-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7af0ad5a-bf29-3e3f-924d-9e3984cb219e | -4.01363 | -48.96046 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 294057d2-e9b6-32c0-b01e-5ffe2db88d5b | -7.02433 | -44.6562 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66da5cc9-19be-3d51-b376-f4a0b641eeae | -5.63645 | -40.87672 | 2026-09-23 04:25:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0429909-2c1f-3ff6-b253-6735bcd4bb6a | -5.92279 | -51.71987 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea1010c-72f5-3250-98d3-12b18453ade9 | -6.61961 | -43.7405 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f463a1e2-d54a-3e59-86e9-0f3d40f45f63 | -5.81885 | -52.06429 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16b9c45b-496c-378c-ba94-e7acd95ec27c | -6.60487 | -43.74238 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 96acf676-f8b9-3b33-8271-caef0029ca06 | -3.951 | -47.62049 | 2026-09-23 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37250a6c-a637-33aa-a52c-f40b6367d2a4 | -6.4352 | -48.45413 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980f07df-b1b3-3d19-85c0-ae31a76d65ae | -5.81159 | -49.15384 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93132d79-2ef1-36ed-9939-c96015ffecea | -2.76338 | -57.03022 | 2026-09-23 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75f82d6c-9025-3255-9d69-2fe0bc939c93 | -3.02049 | -57.93434 | 2026-09-23 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c2fd604-15d1-30fd-b011-7377bc74410f | -6.91162 | -41.69179 | 2026-09-23 04:25:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 289bee36-5dad-3123-9f6f-22ce1563b1c4 | -6.57815 | -44.66173 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6bea46d-7a46-33b2-9222-63290ee26b8a | -3.4886 | -43.34897 | 2026-09-23 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f583af63-23b8-3400-8cd0-ba8176f881bd | -4.83538 | -55.76593 | 2026-09-23 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d13bd7f-16d6-327c-872e-25cdb34eabca | -5.7458 | -43.05397 | 2026-09-23 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 956eb5dc-f66f-3d2c-8a27-7320dc519116 | -7.12899 | -43.08808 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfc9e4c2-b52c-3fdf-85fa-210b36ea8d89 | -6.11684 | -43.40111 | 2026-09-23 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1eea2b6-79b3-3318-b768-d1703aa61c43 | -3.16139 | -57.69538 | 2026-09-23 04:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a0c2904-fd21-3d17-8802-1b73b18f20d5 | -6.47987 | -48.43868 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfc67bde-2116-37ec-a6e1-c431f1be73cf | -3.91105 | -55.83671 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acc7e3c7-b00d-391b-a979-4230d8b504e3 | -2.16791 | -48.32232 | 2026-09-23 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32956cb0-9dfc-3afb-b442-11d97546022e | -7.13513 | -42.0594 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 00ebf8e7-1a94-3985-ad91-74f60346298b | -5.82543 | -52.02495 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3714615e-f216-33e6-b6a6-060d4aad2deb | -2.50768 | -47.04165 | 2026-09-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fc7b712-87b1-3770-8f11-43c14192036e | -5.79944 | -46.09747 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d7e47df1-9f2e-3876-832a-58ec196047a8 | -5.77836 | -43.76915 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7db1056-41fa-3bf0-9bbd-9c19f2aa13cc | -2.45582 | -49.21948 | 2026-09-23 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9face52d-6cb2-3027-9fe8-ce3967b05b46 | -6.98519 | -42.59064 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6f419530-9365-3c1d-929a-05cff8ab6d67 | -2.9451 | -54.08158 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 590ae71b-9d00-3c43-976c-e4fe0440445b | -3.22453 | -46.942 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| f108673f-6181-3290-a577-dd486c0a0c5d | -6.47225 | -48.46389 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afe8707c-74f6-312b-9485-c3ac974f3eae | -7.1346 | -43.07554 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d322531c-66f1-3c31-a216-ed1c18574fa3 | -5.12131 | -48.79973 | 2026-09-23 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a3b8b2d-8ccc-3a31-8651-418184ef47d0 | -7.18375 | -39.32851 | 2026-09-23 04:25:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15adaede-2645-3c4f-9e61-3e9571d0ebae | -1.41682 | -49.3035 | 2026-09-23 04:25:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ea087b32-99dd-3c38-bb72-6858af3041f1 | -5.61638 | -43.36016 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98ec277-b504-37f3-b196-b1063e48ad7c | -2.97174 | -50.38855 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9c7272c8-d989-3ea1-b147-58241c45db04 | -2.74141 | -51.36993 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff5b7fd4-b42f-36c3-a528-8499b64a80eb | 1.44411 | -50.81258 | 2026-09-23 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a642eea6-3c7b-39e1-9740-de4e1de40561 | -6.32991 | -43.93596 | 2026-09-23 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a549c19d-1dbe-3120-9ddf-dbd1a45ae97b | -5.81223 | -49.14984 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 79862bc1-53f3-366b-ac9a-7dc01fd63c03 | -5.89188 | -52.04433 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3914dd48-ea8c-3392-a700-952855dcf6f4 | -1.2723 | -57.03309 | 2026-09-23 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29ed1133-059b-3724-b7cc-9dee3749910d | -6.92726 | -42.88194 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3ff54654-f42a-3b95-8b57-74d43603ea9a | -3.23777 | -53.95534 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28374c6f-b240-3ec5-af95-6e055c2109d6 | -2.50431 | -47.04113 | 2026-09-23 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0426cb9-7ee5-30ac-82f5-d3f38a23032d | -3.83915 | -55.86436 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58f75bfc-3521-363a-a1e2-56101c6a31cb | -5.76231 | -45.10706 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 748f9dca-13f2-32b0-88d9-0765a5b75def | -7.13092 | -43.075 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0aa4dfb1-da64-34b5-a0e2-9dd8fb5be6a3 | -6.31043 | -47.41724 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 711f1f81-d56f-383a-95f2-44623e2b7f02 | -4.33895 | -55.65174 | 2026-09-23 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a5e2319-e8ef-39e6-a4a8-7f6f9383b309 | -4.41432 | -55.47315 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a8eb879-9466-3815-8287-b2aebad24fde | -6.00923 | -44.11384 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49b26692-6257-3153-b4fe-734d75e15e1d | -5.18743 | -49.33466 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d89fffaf-8921-34a6-bd59-9186b14f859a | -1.91592 | -58.26137 | 2026-09-23 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae4de994-e189-325a-b585-a737554111a3 | -2.9428 | -50.49357 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c87e4488-3517-3d49-b158-944237e4db6e | -5.5988 | -45.37338 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 051709b8-d697-3e30-8a3a-7114697d0beb | -0.83072 | -48.52169 | 2026-09-23 04:25:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62e4b90c-4e35-3d16-933f-af4636f9613f | -2.82409 | -49.24111 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bff33786-bd65-3f42-9b45-13393d2c71a3 | -7.02774 | -44.65672 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 150c82ba-01fb-3d2d-9eb5-14cd4a00a077 | -3.93931 | -49.99027 | 2026-09-23 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa21747-fd0d-3853-8a5a-536095de77e6 | -5.75629 | -44.04488 | 2026-09-23 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3e6fb863-0b59-3ecb-b04b-af4943df3b69 | -5.61994 | -43.36071 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2d00d80-4bc2-3285-b060-178be2746764 | -5.76456 | -45.11465 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 938fd510-919f-3258-b277-73c60d721b37 | -6.18564 | -45.31696 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a77f59e9-f597-32d4-80ef-82738f71faec | -3.2487 | -53.95136 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9b89bfa-2411-37b7-8c35-a9dac39d7ac0 | -4.05102 | -56.31622 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23a2bf58-4c15-38b8-a68d-49cbbc0fa6ac | -2.97882 | -50.39487 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6c4a0f57-3f05-3c3a-864d-a98383673542 | -5.86992 | -52.06918 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0c4acea-1dcc-31b7-ac18-7447aeb853eb | -6.4077 | -43.20565 | 2026-09-23 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4feaed00-c784-33e5-8762-791b4bf38831 | -4.46163 | -47.92163 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d95d8367-b843-3d78-b9ea-0d7dcf9194bd | -4.29979 | -49.13069 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 159a2837-de39-354e-a3a2-9688295ba376 | -4.0575 | -56.31302 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
