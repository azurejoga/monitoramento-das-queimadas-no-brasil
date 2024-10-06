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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f21fab0-7a83-32d1-815c-4f419e839207 | -11.92752 | -50.10893 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5d73837-7a35-3dd4-af6a-d2ffc7f18599 | -11.89633 | -50.11072 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af409bd0-c74e-3d3d-b318-c1f7d5fa1bde | -11.89126 | -50.11001 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcbd3fa9-631b-3b78-bc4a-0f653fdd0d88 | -11.89088 | -50.11302 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1f27523-c42c-3155-8f55-2421c7c65f7a | -11.8905 | -50.11604 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ce9c8a15-810c-3cba-b28e-d903e593a5a3 | -11.88732 | -50.10026 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93797a42-060e-3a49-8c37-e1ba1632f25d | -11.88694 | -50.10328 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 399bb930-41d2-3d4f-b8be-584d420e6588 | -11.88656 | -50.1063 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 884eb4b8-35d2-37a1-95cb-e0ee00763ed2 | -11.88225 | -50.09956 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6870627e-b475-3d0f-af0e-18a845315b3d | -11.88187 | -50.10257 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5e4d022-ca00-3fa5-839f-6e2ad69d695a | -11.88149 | -50.10558 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd825c2a-333b-313f-9be3-de183d19ed0b | -11.87642 | -50.10489 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23b279bc-4cbb-30dd-b6bd-f7c371b73fc5 | -11.87604 | -50.1079 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7668d35d-194b-3656-a3d3-be672e68a35f | -11.87567 | -50.11092 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ad7e8f-2249-31b9-8518-ccf42b3a9467 | -11.87529 | -50.11393 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d13f9ece-f849-3f79-96ef-f2f6a2294e80 | -11.8691 | -50.12224 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6afc6ff-14b8-368e-9828-8ff5c8b4a7ce | -11.86873 | -50.12525 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a25bd620-d286-3c91-96a1-c29b18fd52bb | -11.86835 | -50.12825 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03fe93d3-9e48-3c31-86ef-088fbcc9ab0a | -10.96704 | -50.15287 | 2024-10-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aae624c8-5329-31f6-ad48-75a197011730 | -10.96666 | -50.15576 | 2024-10-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8789354c-410d-31b6-a6c2-ecc4ab28e855 | -10.86209 | -50.13633 | 2024-10-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c575a590-4207-38da-a7ac-4ce02e4b86bc | -10.86171 | -50.13923 | 2024-10-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1f78e5b-2966-3487-84d1-b8c5afbf6a90 | -13.26478 | -50.62546 | 2024-10-06 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bd7d855-678e-3fad-b2f0-5f83370dfe7b | -13.10546 | -51.145 | 2024-10-06 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c056ef95-18f3-3b8b-bd72-9d449afda567 | -12.77742 | -50.52767 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86cdef2a-c0c5-3107-b101-17bf79ed0102 | -12.77707 | -50.53058 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07a31117-b027-330f-bc8f-95eee8505868 | -12.77671 | -50.53349 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c3cdf03-7756-30c0-862f-f94fc2a96f04 | -12.77635 | -50.5364 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 689cbc46-5ddb-3dac-8c59-1ced62d25192 | -12.77279 | -50.52407 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dbfc0cc3-b70f-32a4-84fc-341e09c651b7 | -12.77243 | -50.52699 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 40033cce-2026-3606-926e-b0c1598dfe5c | -12.77137 | -50.5357 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 2a045c6f-be23-37c8-a558-79a8511b4244 | -12.77083 | -50.54007 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b21e8bc7-4721-3fa7-ac6d-064cdb9df045 | -12.76815 | -50.52047 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5e62ed4c-bb49-3cc3-b7ca-3220c932720f | -12.7678 | -50.52337 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 27c2e391-f274-3ea2-b9a2-dce53aed2576 | -12.76744 | -50.52629 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f9d5dc98-8510-3bad-b9cc-2f05c1a7aa36 | -12.76709 | -50.5292 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 978e5d78-952e-3ece-b615-d3fcbdc77cb3 | -12.76673 | -50.5321 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| ec5f9d01-096b-35b7-ac39-759d18ffb7e4 | -12.76638 | -50.53502 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 97929d70-9f70-326c-bf75-febf14bccb32 | -12.76633 | -50.53183 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 142aad4d-1ecc-3207-9b62-cfa41dfb23da | -12.76585 | -50.53938 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5a8cc826-a6c9-339f-b9b9-7cfefce7e612 | -12.76557 | -50.53764 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 022a1dad-4b58-395a-bb3a-30b54c8bc020 | -12.76281 | -50.52268 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b66b19f-a822-3968-919e-aa2f0f439dd0 | -12.76245 | -50.5256 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dadab8be-ced6-376d-98d5-f4cf43b4c8fb | -12.7621 | -50.5285 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ad16ee0d-c9c5-348c-bda4-f18695f2018c | -12.76174 | -50.53142 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f90b9e33-a8f3-3437-bffe-079a1d8666aa | -12.76139 | -50.53433 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 484fa988-b960-3526-86de-67534c1a9229 | -12.76134 | -50.53115 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 74718302-077c-3c18-a069-11a0d87ae081 | -12.72038 | -50.61367 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 088fc949-8475-33a9-87af-dab7efd21d9e | -12.71965 | -50.6194 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7a5c2566-8c2f-3ae4-baae-b93461078bc0 | -9.38139 | -51.09158 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0c427a8-5431-35af-b684-96dea077c8e0 | -9.37936 | -51.07209 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc9a519-d940-3bf8-b0dc-e1c676941d88 | -9.37716 | -50.74756 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9437339-32ce-3dae-ace1-e242acc895aa | -9.37646 | -50.75263 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b065e4b9-0933-35cf-bd14-60b88e39e7bd | -9.37619 | -51.09562 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a775e6fc-eb61-34fc-ac08-d6fbfbe5d303 | -9.36957 | -51.07545 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10ae26ea-8704-368c-9eee-16f22cf0a160 | -9.36437 | -51.07944 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2b3408de-332d-3e14-b92e-1473e0fe5050 | -9.15301 | -50.56831 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e6acea2-b998-3e76-9b52-336908967d8e | -8.37437 | -51.651 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f772bb38-d3cd-38ec-b52f-61f5340d19f0 | -8.37125 | -51.64181 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf7a5b9b-6f31-3a02-a3c5-982f7d1b80b6 | -8.3706 | -51.64637 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5d2a620-403a-3dbe-bf73-5e98c17e02e0 | -9.3833 | -51.07743 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e30a0c-e80f-3812-861f-474957c8f6cd | -9.37873 | -51.07677 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fbd72f6-155d-3ce8-a4f4-00f59b56e01f | -9.37682 | -51.09089 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 676dd097-6cdf-3dab-9e53-468f6f7e1ba1 | -9.36563 | -51.07009 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d940d8fd-5917-3b0e-9577-c7c170e6d40c | -9.36375 | -51.08414 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 352b5945-0a8a-3e3b-bdf0-2042fddaa4d0 | -9.1537 | -50.5633 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af45d6de-0c9a-33a5-9bdb-a7cc13fa8bb5 | -8.38309 | -51.65184 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40efd20a-b708-3dba-be3c-10aed8e982fd | -8.37872 | -51.65152 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c204d475-bc46-3db2-a2ed-a62ad021cf79 | -8.37191 | -51.63713 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829e5f97-e6f2-304e-b7d9-bde03d3fc882 | -8.23522 | -51.01068 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc43cd80-b9af-3335-920a-56ad1a536a46 | -10.51251 | -50.96222 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6e871d03-7f76-33f2-8112-d6318dc52b97 | -10.45152 | -50.72266 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1dcc85d-da53-36b2-833f-1560a7f52f9b | -10.451 | -50.69038 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a511bc04-399d-3f38-8610-565a1e1f1047 | -10.4508 | -50.72796 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3ed6498-cee1-38f5-85f9-04fdeadec4ed | -10.4503 | -50.69563 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f70b1243-18b9-3381-8ea1-6435fa694f1a | -10.44959 | -50.7009 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 273c3469-a550-3360-9a8b-d46a20da1dfc | -10.44888 | -50.70617 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 59475825-bdfd-3020-8d53-f511ae5da774 | -10.44818 | -50.71141 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d2b5d1a9-5e0b-316e-ba6e-f5a974c5a81a | -10.44747 | -50.71666 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1c112ec6-9cf1-3f27-a89f-1063a2db4aaf | -10.44692 | -50.68454 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b923284c-9ba0-3e47-8772-2cff600168e1 | -10.44676 | -50.72192 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8016fd20-ef39-3d02-a5f3-13cf0723ca9b | -10.44622 | -50.68975 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b8d7d6b-257c-3486-84c5-f2fd363a1048 | -10.44606 | -50.72718 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 059cadeb-c3e2-347a-82b1-97d6193d35f0 | -10.44552 | -50.69498 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f86de02-2573-3da3-b65b-260f141bf3dc | -10.44411 | -50.70551 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 658fb54c-5f36-35df-a5b5-9f6b0eb50033 | -10.44341 | -50.71075 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 397fac38-781d-3dc1-b860-0378c524c22f | -10.4427 | -50.71599 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c1a3bff6-a3eb-3a42-9796-186a9eda44b7 | -10.44214 | -50.68391 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8aa494b-6cdc-3c6d-92a0-b3f7d41519c1 | -10.442 | -50.72123 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cd736eb-464e-3d28-be07-46d5a2959e52 | -10.44144 | -50.68911 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18ea1e5c-e28d-3ae1-9c73-c5e88295fe98 | -10.4413 | -50.72647 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51d0e852-dc92-3199-910f-855b6d78875b | -10.44075 | -50.69432 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 32b8bb67-bdf2-3c6e-a181-a4e7441148f6 | -10.4406 | -50.7317 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4a83d33-cef4-33b0-8ad7-a2212df0aa7f | -10.43864 | -50.71011 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5175541e-7fcf-3935-8a01-b4932087de6a | -10.43794 | -50.71534 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b332bee4-0909-3483-82a5-09377037097d | -10.43736 | -50.68328 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf720886-00bf-3c45-a93c-a93df98dc57d | -10.43724 | -50.72054 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bffcf18c-0e93-3e66-8ad9-f7548454d8b5 | -10.43666 | -50.68847 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02c3ed98-db46-3a4d-9850-fc5d5be32f8f | -10.43654 | -50.72575 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2276fd1a-208a-3a9e-8f1b-285488493a8b | -10.43597 | -50.69366 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README104.md)
