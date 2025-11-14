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
| d5d5d4d9-0a38-3067-9646-990c81ea4a77 | -3.98616 | -47.99575 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 97908a53-a265-3ac2-90f2-ef58539453cd | -5.39913 | -48.3157 | 2025-11-14 00:34:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b1ca25c4-8960-31fe-bc05-d015fa63b2c9 | -2.12241 | -45.37435 | 2025-11-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 249c6056-3f9e-3db3-8b35-447d7ea0a42e | -3.47875 | -45.64542 | 2025-11-14 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 7b5ea526-09a5-3e60-88ef-b08b80141c69 | -2.65427 | -47.00115 | 2025-11-14 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d15399f8-1510-3197-aae8-0070db1f4ff5 | -3.30675 | -49.16079 | 2025-11-14 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 383df18d-04a2-3d50-9dde-4ef9a446a856 | -3.29144 | -52.10967 | 2025-11-14 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 65dafefc-c01d-30d8-aaf4-8c7c77c4952c | -3.76617 | -47.75042 | 2025-11-14 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 1c466368-ad30-3f59-a79c-b23bc3da98a2 | -6.85498 | -46.7552 | 2025-11-14 00:34:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9297f74c-1f0d-3248-90b8-42d14f97f59d | -6.42216 | -47.29697 | 2025-11-14 00:34:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f4cf83e2-5921-391b-b2a6-218c074ddabe | -4.21351 | -49.12492 | 2025-11-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd1955ca-b7a9-33c1-a06a-41695ff80249 | -1.66353 | -54.27591 | 2025-11-14 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| aa300d8b-4ad4-32bc-b9cb-3fbc21b5380a | -5.84237 | -47.6797 | 2025-11-14 00:34:00 | TERRA_M-M | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6f814cfb-156e-303a-aec4-432de179489a | -6.16288 | -48.05798 | 2025-11-14 00:34:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d8f61418-99d1-3447-8eb1-a9761aa2e88b | -2.79167 | -52.96353 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b30e5dd6-df90-3002-9b50-91fe1660c92c | -3.75767 | -45.74582 | 2025-11-14 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f4293dd6-efff-3995-92d2-610e37a6cf18 | -7.85422 | -44.29339 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 323.7 |
| ad8e7b2d-2d0b-386d-9f44-546256cf87ea | -2.10774 | -45.35853 | 2025-11-14 00:34:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 798980e6-0c57-3cc6-b81a-f3b5477b54e5 | -4.10443 | -50.05574 | 2025-11-14 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fb5169db-f78e-3b20-9298-bb33850bb9bc | -5.59303 | -45.18244 | 2025-11-14 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fb628419-3e03-349d-a324-3750cbdd04ec | -4.10254 | -48.02782 | 2025-11-14 00:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7e56f056-80d8-36b5-82c4-b1023703e03a | -3.51367 | -45.55835 | 2025-11-14 00:34:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 60cf9f16-e811-3089-9303-c64652335cac | -2.98519 | -52.63309 | 2025-11-14 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11d1cf60-616c-37a2-839c-7bc5f27a7477 | -3.41422 | -52.73505 | 2025-11-14 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| fb2de6da-6e44-30eb-b82d-eceb356adc45 | -1.50254 | -47.8065 | 2025-11-14 00:34:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a24cfd3b-5553-3412-ade9-4805d469890b | -5.3657 | -46.28637 | 2025-11-14 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 03731a2e-0344-3239-81cd-2f6fcfee7356 | -3.4709 | -45.65294 | 2025-11-14 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e9f60d10-cc00-3248-bd57-e74d136aeb20 | -4.11456 | -50.06341 | 2025-11-14 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e8fae852-a3e8-38c0-a99e-4d7e2297702f | -2.28436 | -53.64655 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da965c3d-7c7b-319c-b7d2-7b806de09762 | -3.77546 | -50.14482 | 2025-11-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| afd4fba7-3199-33df-a0b7-6eef27cf321d | -2.79994 | -45.4888 | 2025-11-14 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| aae2a578-4023-3452-a74e-5d5ed84cc457 | -4.04439 | -46.13168 | 2025-11-14 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0eb1a6a9-b83b-3344-af4e-3bd31bd85a14 | -4.22263 | -49.12363 | 2025-11-14 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 22dd9171-f567-3c90-82b7-fda16b85a1e0 | -2.92969 | -51.76004 | 2025-11-14 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66bc6e11-75bf-3087-82da-fedd79b3b7be | -2.87134 | -51.46898 | 2025-11-14 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53fe0322-9225-3521-b3e9-b34b5dc9b6f7 | -2.87582 | -45.29742 | 2025-11-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| caf34299-00d9-3b50-a22d-e12282d4dfec | -5.01519 | -47.69212 | 2025-11-14 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 253a5ed8-7840-3cb9-87be-eec9b4b3c895 | -2.83808 | -45.50021 | 2025-11-14 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c7e700b4-ef74-3657-ba4a-0fde1a0ad138 | -2.62616 | -47.29474 | 2025-11-14 00:34:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0fe39d56-c61a-3111-ab90-34e509b78c34 | -3.30026 | -50.10627 | 2025-11-14 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 98c9fd99-2507-327b-8e18-07c86d6241a7 | -3.82064 | -44.24437 | 2025-11-14 00:34:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b332176b-7180-3d7a-a587-5629bb046da6 | -1.84104 | -53.79796 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e474643e-a598-32e8-97a4-c8b956671e18 | -2.27972 | -53.64241 | 2025-11-14 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 447c1e2e-84c4-3707-af4a-afa9811ab224 | -2.38132 | -48.67334 | 2025-11-14 00:34:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cd228cfc-b043-3191-8631-715ec6470b2f | -3.9117 | -44.32721 | 2025-11-14 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 6d117e88-eb44-3bc8-9b24-49313200a5c1 | -7.84481 | -44.31234 | 2025-11-14 00:34:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6bf10d62-ccc0-3b4a-afc8-86c42f84cbf8 | 3.13234 | -60.70923 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0594d2ae-e789-385c-a0f9-6b29b7be5977 | 3.53332 | -51.45531 | 2025-11-14 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ffea3e2-ec94-38cf-8575-e9b88807ec7f | 3.1085 | -60.7656 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 287.3 |
| 0cb80d06-9df8-322a-bbe9-bc88a109dc29 | 1.3291 | -50.67233 | 2025-11-14 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2adcc54f-835c-3ad4-b4cc-466d08b2d13b | 3.14494 | -60.71635 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e0520705-9c2d-3e20-afc3-b45f7e9432fb | 3.11006 | -60.74116 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 50b45708-4458-3b41-b16f-fc39e57dbb63 | 1.32784 | -50.68145 | 2025-11-14 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9b08a550-c517-32b4-89bd-6ad6bb76dc1a | 2.33761 | -51.64954 | 2025-11-14 00:37:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39c0caf5-aec4-3776-8cfe-349587348bb4 | 2.75643 | -60.36144 | 2025-11-14 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 7ede3ce6-3c9f-3dc0-8d9d-36af36ca31a2 | 3.10413 | -60.79507 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.6 |
| baf80c8c-a57b-3edc-89e1-4c738c0facf1 | 2.75593 | -60.368 | 2025-11-14 00:37:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a28ef72f-f27b-387a-b677-b2c0a05fb756 | 3.08887 | -60.79275 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8644d198-658b-3947-92de-bfc2ca798bf7 | 3.12977 | -60.71418 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 16ca5370-1236-332a-9e89-6ce15553e7d5 | 3.10549 | -60.77048 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 375.6 |
| d604db69-1e41-3515-9500-f8b8c8008a6a | 3.09326 | -60.76333 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 246.2 |
| 72b6bab6-e23b-3ada-a400-a4c235433354 | 3.53456 | -51.44635 | 2025-11-14 00:37:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3ed84201-4c53-3f51-82ce-255f373278b0 | 3.12804 | -60.73849 | 2025-11-14 00:37:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 44841969-5091-3861-837a-751e022b9be3 | -7.8606 | -44.300598 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c06c80e-3579-391d-84ec-877a0e4aa0e2 | -3.8141 | -44.2477 | 2025-11-14 00:38:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9b8253-46c6-3f24-9bff-ca9487f27f03 | -9.6284 | -40.336899 | 2025-11-14 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 437d8ffe-548c-39e8-9652-b2cebd6ee69f | -6.6103 | -47.632599 | 2025-11-14 00:38:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e962bf4-09c0-322a-b101-076a70e9b70f | -9.6774 | -47.890202 | 2025-11-14 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03f402f6-b42e-3b11-94a8-183a879224e5 | -15.3853 | -48.971199 | 2025-11-14 00:38:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1e031fe-b499-3f81-8bf0-f946b13fb4b7 | -7.7251 | -47.186501 | 2025-11-14 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d80d9a0d-6eea-3fd2-86c5-4b4850db5c41 | -6.8839 | -42.839699 | 2025-11-14 00:38:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f283eae-9246-3864-9ea1-adfe6f430821 | -7.4602 | -42.574699 | 2025-11-14 00:38:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72898169-5339-3757-bb7b-3c1f9522f280 | -13.4984 | -43.6334 | 2025-11-14 00:38:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bab75ef1-385c-3fff-aa24-c243f422efab | -5.7472 | -45.102699 | 2025-11-14 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02de8021-224e-3785-8d3b-6f60f9f5879e | -2.7953 | -45.493198 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 472337e1-bd54-31f7-8603-cb8a8a66473f | -20.758499 | -43.2215 | 2025-11-14 00:38:00 | METOP-C | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc3a0b3d-4673-36fd-bb79-1f1ac0156835 | -12.6967 | -45.429699 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4ee0d25-c453-3870-a3de-e09621c605a8 | -10.7273 | -44.0196 | 2025-11-14 00:38:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91769755-15ae-3699-87c2-8ddb75e05547 | -11.8541 | -49.2309 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b69d2ad-1bce-3f97-b14a-b0ccbcf15e39 | -2.9416 | -49.354801 | 2025-11-14 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9065d71-4a5c-3767-b44b-6715311d52b6 | -20.7551 | -43.206699 | 2025-11-14 00:38:00 | METOP-C | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 982811dd-eb25-3a4c-b6ff-85eb5e4b5055 | -3.0128 | -49.4412 | 2025-11-14 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88211fca-48cc-3a5b-ac38-c25f36265377 | -6.148 | -48.0462 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1733c2b8-0e9f-36cf-8469-4e07536cae54 | -4.7051 | -46.434101 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d6f8f33-c508-3741-9320-49768f9bbd65 | -12.667 | -46.756001 | 2025-11-14 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 490e0537-7aba-3b90-b3a0-4dae72abd50e | -12.4869 | -47.287701 | 2025-11-14 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4605bd9a-da1b-3b68-8876-13d6dfd804a5 | -5.9775 | -42.586399 | 2025-11-14 00:38:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33559ffb-45cc-3856-8e84-cd25d78347fc | -2.8033 | -45.482899 | 2025-11-14 00:38:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87cd3f49-710f-3d7b-96e0-a431e21cfad1 | -6.206 | -47.262501 | 2025-11-14 00:38:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9ab578-f31a-37c4-9a2a-eed5b5f15366 | -3.1032 | -45.3979 | 2025-11-14 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d378927-0650-3ba4-971e-414db4181017 | -5.8384 | -47.683899 | 2025-11-14 00:38:00 | METOP-C | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab0526f8-37cd-36f9-aaae-75079a968f7b | -5.3064 | -45.071098 | 2025-11-14 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd2c155-ca4e-3b47-b918-2da731658b03 | -12.6786 | -44.146801 | 2025-11-14 00:38:00 | METOP-C | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6791cfc-d860-37c0-a3cb-4766287dacfd | -12.0116 | -46.7729 | 2025-11-14 00:38:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38737b02-ba2b-3a9e-9f87-2cb58cc3567c | -2.1139 | -45.355499 | 2025-11-14 00:38:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9ec6204-070e-3092-8148-674db9cc8a38 | -11.9372 | -43.9366 | 2025-11-14 00:38:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ffed9343-8aea-32be-b7f7-6391f1451e19 | -12.6837 | -45.417801 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5ff1408-a27a-3d84-a4e0-08a9c4586ea1 | -4.1003 | -50.055 | 2025-11-14 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaba17b6-0839-370f-b8da-129e3c76acdb | -20.1008 | -41.6786 | 2025-11-14 00:38:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe8bf74a-1c17-390f-a1f6-56e0ebaeb955 | -12.7033 | -45.4132 | 2025-11-14 00:38:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
