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
| d6936188-2d7e-3ff0-8998-84abb15e403c | -5.7754 | -45.1053 | 2026-09-24 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 5ebcaa33-cf10-3839-8850-05466bbf6bda | -8.5951 | -62.4988 | 2026-09-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c78b0fb3-f1c2-335c-8d85-4298b35ff7ab | -15.2517 | -43.2501 | 2026-09-24 00:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 95.5 |
| a90351a3-6727-3d3d-86cf-fd7503dbb14a | -13.2249 | -51.5679 | 2026-09-24 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a9386aaf-1580-3ad4-a004-5b1c6af30a5d | -10.9115 | -53.9429 | 2026-09-24 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d63b9f15-bdab-33a2-967a-1e87599086f4 | -6.4302 | -59.9724 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| da3c0f80-4142-36e2-b9e8-b5ba6a2dd658 | -6.4487 | -59.9526 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 131.5 |
| e5e24abe-7789-35fa-8e0a-7369bb04cbce | -5.7756 | -45.0826 | 2026-09-24 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 0b24a5fa-bc03-3dbd-bc90-280da4820ff5 | -6.5962 | -59.9279 | 2026-09-24 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6565c58f-eb46-3664-91e8-1133f5844102 | -3.4578 | -50.0679 | 2026-09-24 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 910c8b90-e342-3089-bc9d-8eed36eaa2e3 | -6.8221 | -38.5631 | 2026-09-24 00:10:00 | GOES-19 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 25fb00ee-5193-34bd-9d18-357f462be486 | -13.2057 | -51.5703 | 2026-09-24 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2890139e-93c3-36ee-b84a-fa3d827d94cf | -10.0924 | -46.0005 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 65af5587-5f8b-32c3-910e-69a47af009db | -10.2637 | -49.9626 | 2026-09-24 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 284d9180-12fe-397b-8265-a16cf8b86d1e | -10.111 | -46.0209 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| d2bbdbc1-4df9-35b1-ba74-3ba173498224 | -6.6331 | -59.9265 | 2026-09-24 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| fea60c9c-bec4-3196-8b23-d12c42e4325b | -10.0917 | -46.0458 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 88b771d1-1baa-3ea5-bc00-12d45679aa34 | -3.6764 | -60.5649 | 2026-09-24 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 83dccc0f-6b0c-32c7-a9b5-d0b1105298d9 | -8.595 | -62.5178 | 2026-09-24 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 38d8feed-4386-3173-a67b-17a0b7e0604f | -11.9583 | -50.7607 | 2026-09-24 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 562.4 |
| 85afae2a-6e1e-3f58-9d5d-9a05fe811f3e | -15.232 | -43.2541 | 2026-09-24 00:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 4f77182f-3ce6-328a-a5eb-034732c87073 | -10.0921 | -46.0232 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.7 |
| e574d1f9-a197-3ed3-a6f8-1298a7a1c6ab | -11.958 | -50.7821 | 2026-09-24 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 548480bc-fcbb-3eae-99b0-3ee28e741972 | -6.3502 | -57.7522 | 2026-09-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| a86fdd0b-adfc-3ede-a5f5-318d066fb172 | -6.789 | -48.6779 | 2026-09-24 00:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 25eb6857-6c25-349c-af45-0a43658602f9 | -9.8491 | -48.4927 | 2026-09-24 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 88056144-bbae-3e9a-a342-6e336b31e492 | -11.9392 | -50.7629 | 2026-09-24 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 6bd61deb-d571-3734-9a04-d10982707141 | -10.1107 | -46.0435 | 2026-09-24 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| d48955b2-1787-337a-98ec-ea3dd5569b09 | -5.1058 | -60.2639 | 2026-09-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| efbbeadf-144a-3b1c-aa19-124417d7960e | -3.6947 | -60.5455 | 2026-09-24 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d30d2dc2-7ced-3408-87dd-9bc10ec046d6 | -3.4392 | -50.0896 | 2026-09-24 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b1025042-0002-3ae1-99fe-b671817ef310 | -11.97 | -50.79 | 2026-09-24 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 276845d0-837b-3ba8-9a0e-5c8db91eeff6 | -11.94 | -50.78 | 2026-09-24 00:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03a25067-84be-38c1-adb9-9e006de59846 | -4.1367 | -56.312302 | 2026-09-24 00:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 093e5d9a-7504-319b-808a-a8eeaa13b9da | -11.9323 | -48.215698 | 2026-09-24 00:16:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da8acf34-2039-3319-845b-33dc2c4ef2f8 | -15.5516 | -42.3536 | 2026-09-24 00:16:00 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| daedbfd6-2f69-3748-8839-8f65ebf3794b | -8.2573 | -54.7514 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 790e06a2-dc85-3d08-acdb-fb9c65abf134 | -3.0637 | -49.569599 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 702f78be-4d77-3cac-bea0-8457e7060dc9 | -4.1196 | -51.081299 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0acbf26a-d6ed-3398-9bf8-13dd83d00d68 | -5.7899 | -49.184299 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c19953e3-1f74-3b3f-bd7f-4225128496bc | -1.1927 | -54.137001 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a644f99-d2fe-3635-ab4e-ee92e3023f98 | -9.5601 | -40.305599 | 2026-09-24 00:16:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 227d0932-1af3-3314-b6f9-d3cc9848eb90 | -10.7169 | -48.719398 | 2026-09-24 00:16:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd4a2a26-e23a-3bba-8a7f-0adba8b6a4b8 | -14.0126 | -42.899399 | 2026-09-24 00:16:00 | METOP-B | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b965ccb-356d-3320-95be-88edfd8bd10f | -8.2955 | -49.9039 | 2026-09-24 00:16:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4924a6e-68cb-398f-bab1-0397ad57ada8 | -8.8212 | -50.450001 | 2026-09-24 00:16:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a8c3ded-4051-3520-a5fd-9206878b2787 | -12.0513 | -50.290901 | 2026-09-24 00:16:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c760fb49-2827-3a48-8f8d-47bf8dfc2f8c | -2.5602 | -54.723202 | 2026-09-24 00:16:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4df14e0-a4e5-3629-af71-d6c40000c9d4 | -12.1685 | -47.363899 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb37a9d4-d21d-32e8-810d-c739f450ce7f | -6.6525 | -55.0592 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd09805-43ba-3687-ba16-61960d8e94b3 | -6.5707 | -51.483799 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5ad41ac-7c90-35d2-bd58-bbb8e380087b | -9.8577 | -48.482899 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92eee964-2226-35dc-a61b-c5571f08a383 | -3.0138 | -51.523701 | 2026-09-24 00:16:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9521b7e-1639-37b8-b932-6a4070e98b6f | -4.9798 | -45.5369 | 2026-09-24 00:16:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5ba256a-c85e-3d92-b7d0-3adfa94f0654 | -11.2689 | -51.360901 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 02fc0689-ad1e-3b95-b63e-82aa00380195 | -13.2136 | -51.559299 | 2026-09-24 00:16:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5801f17a-7fb2-3f09-9ea8-556e0ea39e31 | -9.0033 | -57.116299 | 2026-09-24 00:16:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd037af-11c6-3247-93b6-621dfd35494b | -8.2592 | -54.760399 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0708c3bc-97e7-3028-8e7b-955df4261334 | -8.1396 | -49.536701 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fb8cf4-5a5e-3958-819f-d7bbe96e32b8 | -3.1567 | -54.584099 | 2026-09-24 00:16:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6418d09d-11c1-31a3-b20d-76d6133f55a3 | -8.5867 | -54.615101 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a252721-9150-3e83-a374-dcb9f07876d5 | -5.5942 | -60.160301 | 2026-09-24 00:16:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f11511b-f680-32ef-8868-98a0eb38a06a | -2.7621 | -57.0079 | 2026-09-24 00:16:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84c7b3b6-dc32-35c2-a172-c5a768043654 | -9.142 | -49.953701 | 2026-09-24 00:16:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37be3552-fe99-3eb3-ae19-2e0f01229148 | -2.7644 | -57.018101 | 2026-09-24 00:16:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39838281-9c0e-3ed9-8ff0-24e6dbefb0ba | -1.2777 | -57.028 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b0cc3e-0e37-38eb-ae96-e30fb7bea2cb | -1.1911 | -54.129902 | 2026-09-24 00:16:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df2b84a-f95e-3a5e-a22c-224ff210f8ac | -11.2379 | -51.360401 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18f3dd26-b28e-3a4f-95e9-3af191204cdf | -10.2784 | -49.965 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 800effdd-c8ab-367b-870e-97d87d0ae15f | -3.4849 | -59.165699 | 2026-09-24 00:16:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0400e4a1-7fb0-3912-a19b-04eea67a1385 | -11.2364 | -51.353298 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b27d0cc-251e-348e-971b-416dfb2d4018 | -6.8606 | -52.180302 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b00a8b1-5805-349e-abb9-00c372abfccb | -7.4715 | -44.547901 | 2026-09-24 00:16:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a6eff2c9-cf20-360e-a6bc-d98dd9d40e68 | -11.9612 | -50.7672 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23bd73b3-0353-3e9a-836d-1fb8588fa699 | -11.2493 | -51.365299 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1495805f-da4c-35e5-a9e9-a8ad9ecc3e48 | -2.8916 | -54.089802 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 953e3aed-bfe7-3577-bdb2-90d94319712f | -5.2377 | -49.2943 | 2026-09-24 00:16:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3e4775-deef-32db-ab62-7f4376a2ce9c | -9.8612 | -48.497898 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11a03892-8e86-3fd1-bbcd-b416c5c4f6a4 | -2.8265 | -46.706902 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8cdfb9-3331-3ef2-bc48-55d030b6bd63 | -11.2544 | -51.341702 | 2026-09-24 00:16:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20bcf65f-0bd9-3209-a66e-4df64caa7cc3 | -3.551 | -43.456001 | 2026-09-24 00:16:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3ca4ffc-ae3e-3fa1-8c51-7b45b4419443 | -5.8521 | -49.770699 | 2026-09-24 00:16:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a7323a-62f8-3710-8d19-50a5315ec233 | -5.8098 | -47.755299 | 2026-09-24 00:16:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04040d00-64af-3db0-a099-b1d24d920a55 | -10.0984 | -46.032902 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d045d9a7-60ef-3959-b75a-2dfa0434b8fa | -4.5601 | -54.929401 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f28560a-b066-3335-8a3e-1b5bfa599bd4 | -9.8514 | -48.500198 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb108626-daff-376b-998e-d274064a58c3 | 1.6101 | -55.908199 | 2026-09-24 00:16:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63a0a1e3-8c32-3353-bcfa-c41d80eef417 | -10.2895 | -47.541599 | 2026-09-24 00:16:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28453180-2579-3aa0-bed1-14d0bcafd136 | -4.118 | -51.074402 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80c98653-31ba-39d7-bd71-279c5c98cbbf | -9.8399 | -48.494999 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6a6fce-ca3c-3e34-a6d1-8f04f7c1de52 | -11.5257 | -49.189899 | 2026-09-24 00:16:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48a1746a-92eb-3b25-921e-5478c16f75e5 | -3.1695 | -48.011101 | 2026-09-24 00:16:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a977178-d658-3ab5-b491-f1b1336b541b | -10.267 | -49.9603 | 2026-09-24 00:16:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6928716-8f99-3a08-bd19-a08c64f0337f | -11.9679 | -50.7509 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 473d5ea0-fc52-39fc-b6e0-3133a4c733b1 | -8.4483 | -45.909 | 2026-09-24 00:16:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 726d35ef-e1b8-357e-8ae2-63a8aa52dd6d | -12.0267 | -50.737598 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd89a9b1-227d-3064-8538-9fcadd1f05ae | -9.2282 | -47.373402 | 2026-09-24 00:16:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcef5fe1-1d3d-3672-856c-13d19e43aefb | -10.9118 | -53.940201 | 2026-09-24 00:16:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4a3a92-4252-3f48-afad-009e7b31a7a8 | -18.885799 | -47.165001 | 2026-09-24 00:16:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1bd5c2c-b7c5-301b-a7d9-de7b9095fc40 | -10.0913 | -46.003502 | 2026-09-24 00:16:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
