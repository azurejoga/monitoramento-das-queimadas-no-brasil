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
| d79a2120-f2f4-336b-9694-1c2a7e6a25f0 | -7.08122 | -44.9573 | 2025-10-28 00:54:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c7b6e977-4a45-3d97-97ec-bd2168b265d3 | -8.70056 | -50.80663 | 2025-10-28 00:54:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f2a5e068-df58-30ed-88b9-380133e8eb1c | -2.75303 | -45.40491 | 2025-10-28 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 3fabbe67-4111-308c-9c48-487feb36475e | -7.98544 | -46.74254 | 2025-10-28 00:54:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| dd3d2264-b68b-33b8-839d-1c1015f01367 | 0.98008 | -51.11888 | 2025-10-28 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7c933428-fe2b-383a-aed1-9eb8ddb5c1e6 | -2.8241 | -49.39404 | 2025-10-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 463a3b67-b832-39b1-bf6b-8a53ffae38bd | -1.66983 | -51.9954 | 2025-10-28 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3d77cb27-4ab5-33e5-9755-8973e8ca32bb | -1.33184 | -53.60112 | 2025-10-28 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ecf53be-331d-3492-b4a2-709ce78f5ddd | -5.70965 | -49.19561 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 90786411-3c42-37b9-9203-baff924a0ee8 | -7.07023 | -44.92937 | 2025-10-28 00:54:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 1bdb6de8-e2e9-38ae-b755-6afd3cfe6c41 | -5.58513 | -45.34921 | 2025-10-28 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 38d73a52-7800-3b69-ae9f-bd8226835111 | -7.00218 | -46.99573 | 2025-10-28 00:54:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| bbfb6967-6765-3003-8c75-41b6df4a837b | -3.71035 | -47.6669 | 2025-10-28 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 768daf0e-0bc6-36ca-99d5-82b07408aaa0 | -4.38454 | -56.27944 | 2025-10-28 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e9c1bfa-0dfb-3b99-8110-c7fe0413e474 | 0.40645 | -50.85168 | 2025-10-28 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1cc1ac5b-8dde-368c-bef6-277e25ee1d12 | -5.61103 | -47.10791 | 2025-10-28 00:54:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 2f1db65e-03bb-3ab5-8a3c-bc5bac420462 | -1.54855 | -55.42045 | 2025-10-28 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 20e92cb9-5959-345c-81bd-38b0c37e7387 | -3.9322 | -56.06491 | 2025-10-28 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 567a709a-44b8-366a-87ba-57c9bd12091a | -3.23984 | -50.66064 | 2025-10-28 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d22b20a4-0c3a-36bd-a79c-eb4350c8a97e | -1.4922 | -53.12458 | 2025-10-28 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e0da33a5-b5a0-371d-a4d5-7347c370e0de | -1.49373 | -53.13526 | 2025-10-28 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 147369ec-22b0-316a-a6be-bb8b3eac9ecd | 0.40744 | -50.79535 | 2025-10-28 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 649c4e7a-3e6b-34ec-87bb-7150a34963a7 | -2.73775 | -45.39998 | 2025-10-28 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 2fa203d0-df91-3a5e-b5b7-e3d1d3e13751 | -7.44572 | -49.40033 | 2025-10-28 00:54:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| abe7a4c8-9a7a-392c-94a1-8a1bd17d50cf | -5.84202 | -46.43117 | 2025-10-28 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1ce965ed-cc3c-3970-a2e6-f7409693099a | -6.09048 | -53.50121 | 2025-10-28 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfa806d2-1657-3a57-81d0-f1f8edcc3f5a | -1.61502 | -54.51065 | 2025-10-28 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 698f7da2-8f10-3d26-9683-3a09df38c5ac | -3.27552 | -52.57104 | 2025-10-28 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 652bb5d7-7371-3483-b2ef-268e881466d1 | -1.50188 | -53.12317 | 2025-10-28 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 508e9adb-405e-3a9c-ab94-d74de9956fa6 | -2.19596 | -56.97777 | 2025-10-28 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 57202cb0-89c0-32a7-bf79-8203a82456cb | -7.92203 | -49.73553 | 2025-10-28 00:54:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e0645187-7308-30ed-bfd8-66c6f87e0a06 | -1.69479 | -53.69868 | 2025-10-28 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd6982c6-2bd2-38cc-a5dd-4a9298791485 | -6.1019 | -44.68198 | 2025-10-28 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c6bfbbe5-e92f-3d09-b2a5-be3a73b40642 | -4.35568 | -50.50819 | 2025-10-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2e1039ed-d90f-3ac8-9ffc-8d90611f7d77 | -3.71305 | -47.66069 | 2025-10-28 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d2a5fa7f-d7bc-301d-8674-e70387e69b26 | -2.05267 | -56.54328 | 2025-10-28 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b158c475-6b16-3a19-9364-fe8773be9238 | -3.53118 | -53.31525 | 2025-10-28 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 47ee1839-2322-3e8b-82fa-f0c606edf2d7 | -6.16165 | -48.12137 | 2025-10-28 00:54:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 010b9448-0350-3601-811c-f56585b8dedd | -3.75217 | -50.95317 | 2025-10-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d6f0e881-fed5-3058-a5bc-3d3c1bd819ce | -2.76111 | -45.43691 | 2025-10-28 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| afe68533-dda6-3400-bfa3-9cd0ed3fe112 | -2.75885 | -45.44436 | 2025-10-28 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 40146a0d-aab0-39bd-a7f0-7c42699ccb5f | -3.70916 | -47.63564 | 2025-10-28 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| f113059a-88c6-342c-a13d-176379c5bb7b | -7.25931 | -46.81515 | 2025-10-28 00:54:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 9a5ae9d9-8b82-39e0-9c2c-76157513269a | -7.44813 | -49.41624 | 2025-10-28 00:54:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ba8aae1e-89e8-3dff-94f7-9519c436bbdc | -1.56622 | -55.41795 | 2025-10-28 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4c108140-3995-3cf8-a9d4-b65f570967cf | 0.98743 | -51.12654 | 2025-10-28 00:54:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 60f1d7b2-5e82-38d3-b30c-4114a4147147 | -7.29684 | -45.05454 | 2025-10-28 00:54:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| ce2e5b64-8e67-389a-91f6-272dbf719040 | -7.4573 | -49.39843 | 2025-10-28 00:54:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 61e9f162-f193-3f3c-8853-b5cbbb83a85c | -0.99622 | -47.65116 | 2025-10-28 00:54:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| be775fbb-9aa4-3015-8894-d2e8de3bb60d | -2.73578 | -45.40751 | 2025-10-28 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b17c4f64-5f32-300f-be80-fea81dd471a4 | -3.44046 | -50.21841 | 2025-10-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4f273cc2-1e6c-311d-9acf-84003ec25359 | -2.83952 | -49.41134 | 2025-10-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6378349f-faff-3284-8184-fae7898dc9e9 | -3.5479 | -54.69731 | 2025-10-28 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3434a0e5-717b-304b-87ce-16c871c8ecb8 | -7.2908 | -45.0624 | 2025-10-28 00:54:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 219fcd71-0579-3b0d-8519-1c6671a26f88 | -5.82568 | -53.45236 | 2025-10-28 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1319a85e-1ea8-301f-9eed-b09bf9e29527 | -2.83672 | -49.39221 | 2025-10-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3fd8d1eb-9dd3-3943-9556-3cdbe8cc2163 | -5.64405 | -47.64084 | 2025-10-28 00:54:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| c0aa92e6-3c9c-3cfb-994d-c2e612bbf130 | 1.88708 | -50.84353 | 2025-10-28 00:54:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 76b95cad-c8cc-3988-adf8-de39e35d0156 | -5.84637 | -46.45977 | 2025-10-28 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| e3a1a2ce-bf04-310e-8532-2dc825a9c684 | -3.79811 | -51.09491 | 2025-10-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8cfc72d7-7e0f-3666-96de-217221420793 | -2.94804 | -49.3508 | 2025-10-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e6cb1527-088a-3f2e-a7e0-3aee361a6cee | -2.06011 | -56.59685 | 2025-10-28 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5f0d4563-25ba-32e0-874f-2abb5f4bc03a | -7.07582 | -44.96465 | 2025-10-28 00:54:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 57f8c9fe-2aba-38ea-ae04-248e12d7f644 | -6.10382 | -44.67461 | 2025-10-28 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| cb4aa793-4218-31f7-b9cc-901f21b430e8 | -7.81588 | -46.46424 | 2025-10-28 00:54:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| fabce01d-11c7-3e2d-8f58-bda8744755bf | -5.70327 | -49.18504 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 32cd3261-d13e-372d-b8b9-0401b42ef26a | -7.98229 | -46.74872 | 2025-10-28 00:54:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 319e7e00-89b3-358e-8507-72b217b2d653 | -4.71488 | -46.43893 | 2025-10-28 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 250a09f9-d0cf-3030-bfce-2c389879c2ff | -5.70586 | -49.20271 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7738c479-99be-3b3c-8a5f-1a32758435e3 | -1.98154 | -56.5532 | 2025-10-28 00:54:00 | TERRA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd7174b4-3585-3434-a920-9067bcfb4cf3 | -1.86491 | -54.5192 | 2025-10-28 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d02e55e9-c1bd-3af9-9b67-592ea2e212c3 | -1.67105 | -55.37897 | 2025-10-28 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| faae7a7c-7122-3c87-b619-e7c76a2b3b5d | -2.19469 | -56.96861 | 2025-10-28 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fcdca27e-2593-3b66-935b-2a270927c42e | -5.46632 | -50.16206 | 2025-10-28 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3b858cee-dd1f-3fc2-aed9-8cd0853626cc | -2.7439 | -45.4395 | 2025-10-28 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8aef69a4-2ccc-3a26-9fa6-e97c8b53cbea | 1.6306 | -55.69079 | 2025-10-28 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eebf853c-cd41-3e61-9819-c0a2fda19fb4 | 3.13857 | -61.00811 | 2025-10-28 00:56:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 517622d7-dad7-342c-afed-976a2b910eb8 | 1.60912 | -55.71508 | 2025-10-28 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f0aadad-709a-3368-89bd-f83fba897c59 | 1.60788 | -55.72402 | 2025-10-28 00:56:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c0ceaf6-e2dc-3093-912d-f106225f2920 | -7.4539 | -49.4232 | 2025-10-28 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c76f9112-d87a-39bf-9dcc-a54b4d731fad | -4.4602 | -43.6569 | 2025-10-28 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 8d4e9a2b-e7cc-3f84-bb4e-f9a090652262 | -11.2798 | -45.5052 | 2025-10-28 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 527fb668-6600-3a06-825c-cbdc22b115c0 | -7.4541 | -49.4018 | 2025-10-28 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d446b43c-c796-3be2-9a5f-a43dd379545d | -7.9644 | -45.5543 | 2025-10-28 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 94614de0-e67a-3ecb-9a41-1a5d2498cf54 | -7.9647 | -45.5317 | 2025-10-28 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 19eb9472-1a4c-3c9e-9c42-be050db9c52c | -3.5831 | -43.634 | 2025-10-28 01:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d57a5f04-2d39-3064-984c-02c75041472e | -2.7556 | -45.3995 | 2025-10-28 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 008adac4-5f9c-33bd-8a5a-77710fb49176 | -7.9461 | -45.5108 | 2025-10-28 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b8b50b03-9fb2-3426-9b52-df8138b9ba85 | -3.5833 | -43.6108 | 2025-10-28 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 92751c55-e87e-3d57-8806-d87a2d1d50b8 | -2.7555 | -45.422 | 2025-10-28 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| dee02493-8744-31f9-9c95-aa61f9e94faa | -9.1371 | -51.299 | 2025-10-28 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| acd0eac1-c70c-3532-bcf1-54a6433ce153 | -12.6097 | -45.0779 | 2025-10-28 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e189be09-3459-34bc-97de-cd6141f99a02 | -10.5683 | -49.8018 | 2025-10-28 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7c0ea152-9ecc-3d09-9681-7cdde7d443a3 | -4.2206 | -43.1828 | 2025-10-28 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e12026e8-7753-3698-b64d-435d3718d8d5 | -4.2204 | -43.2061 | 2025-10-28 01:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 000e81f5-8b55-346f-9f87-5e2e978a0f9e | -10.9402 | -50.2764 | 2025-10-28 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| a08dea5f-e2f5-3f29-8e12-69d3a6eea6c0 | -8.5676 | -47.0184 | 2025-10-28 01:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 0d45b5cf-6378-37a6-9d81-5aace5b94e09 | -6.7061 | -42.0517 | 2025-10-28 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| c2582833-8667-3810-9f4f-b806adb6e35a | -8.5673 | -47.0406 | 2025-10-28 01:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 200fad0e-9012-353c-a88a-a4649871ca27 | -4.3625 | -44.2842 | 2025-10-28 01:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |


[Clique aqui para ver as próximas entradas](README6.md)
