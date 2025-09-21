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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d90d6bb-409c-3186-b64a-7069157d1d8d | -7.9256 | -44.0937 | 2025-09-21 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b37a3e66-1a61-3e9b-82fe-a3cb94e6ab0b | -10.3681 | -47.8875 | 2025-09-21 03:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 975dec2b-3ddc-35db-b5b4-f49d2974be27 | -10.3677 | -47.9096 | 2025-09-21 03:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6cad5a2a-6389-3220-876c-34d478b6a467 | -5.5243 | -43.8647 | 2025-09-21 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6e3d771b-6915-3b99-a30f-738b60e02923 | -12.7114 | -46.8454 | 2025-09-21 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0ca2f392-5857-39e5-8ecc-34e50f02dc36 | -5.6375 | -45.9481 | 2025-09-21 03:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 52709ba2-32fd-3ff8-a1af-d5a706cfbabf | -7.9253 | -44.1169 | 2025-09-21 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8bcb42cb-2788-391b-8e5b-8e159e55f8d5 | -13.541 | -42.9835 | 2025-09-21 03:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 6460b91a-d9df-3629-ae53-84ecdfa1e8c5 | -13.5405 | -43.0077 | 2025-09-21 03:30:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 140.3 |
| 7714a8a9-bc35-36f4-9875-d3ef94915452 | -11.6186 | -50.5861 | 2025-09-21 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0b6cc595-8797-3829-baaa-2ab05207d42c | -13.5405 | -43.0077 | 2025-09-21 03:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 103fa0b3-62b6-303b-98e2-258370c7d5d9 | -13.541 | -42.9835 | 2025-09-21 03:40:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 63a85545-782c-325b-ba82-e14ac35e05ea | -7.9253 | -44.1169 | 2025-09-21 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 333ee477-0efe-37da-81ff-ecf5f9f09474 | -11.6183 | -50.6075 | 2025-09-21 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f55a9119-9077-3487-997f-6653d0a530c6 | -12.7114 | -46.8454 | 2025-09-21 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 24fa7be8-afdb-3ca5-8ced-7aa3e082b7e5 | -11.3057 | -47.4197 | 2025-09-21 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| c4bb6215-e254-3cdc-b958-e922ed0de356 | -13.5405 | -43.0077 | 2025-09-21 03:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 7d2df169-e0c8-35a3-ac2f-6e579bf11a1e | -11.306 | -47.3974 | 2025-09-21 03:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| db4ecabe-6b99-3d4b-88e6-c9bbb8bc208e | -11.287 | -47.3998 | 2025-09-21 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f99ec919-09c2-3569-8ee0-b2a9b9c49dd0 | -12.7114 | -46.8454 | 2025-09-21 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c9ddcef8-0e97-3be2-b4ed-558346383425 | -12.711 | -46.868 | 2025-09-21 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3f8b11d7-0e5e-3386-abf8-0226850e745f | -11.2866 | -47.4221 | 2025-09-21 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c3e6019a-de4d-3b16-9e78-2567181a0a55 | -13.541 | -42.9835 | 2025-09-21 03:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| db87b7bc-5df7-3aac-86c2-796d8713ba3b | -15.978 | -59.4269 | 2025-09-21 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1f232e49-f973-35d2-86eb-a42959714b2e | -11.6183 | -50.6075 | 2025-09-21 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 502b4465-dade-3916-9f21-f0ea8590c9fc | -11.6186 | -50.5861 | 2025-09-21 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| da3eb793-cc7a-3e90-95fa-80b8a647e1a7 | -3.68497 | -43.52443 | 2025-09-21 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 641a3bf2-5b6e-35f1-814e-15a11a4ab042 | -3.86459 | -43.0998 | 2025-09-21 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60fd6da4-de2b-325d-a8c0-5199087014a7 | -4.77853 | -37.80433 | 2025-09-21 04:06:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08c8c706-d6ec-3f7c-97dd-c31dc0b4dd65 | -3.13458 | -41.88018 | 2025-09-21 04:06:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 695fe8e5-60b6-3cfe-a159-b05288ae3887 | -3.59365 | -43.91578 | 2025-09-21 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f51d611-3e19-3fc0-8906-f600b5d700a4 | -4.6161 | -38.68536 | 2025-09-21 04:06:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bf4b0419-61f3-3ed2-80dd-126e86702057 | -1.12573 | -54.14119 | 2025-09-21 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52291ea5-e4dc-31a7-b662-91cff0956fc0 | -2.62621 | -46.83921 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 707a3a8b-a3a1-3af9-a167-c36fe7324cb3 | -2.73798 | -49.55366 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb2be630-cdf4-3b0f-89fb-e37e30550b2e | -3.5943 | -43.91174 | 2025-09-21 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3e6840c-71c9-3c57-8044-59095bcb9fcf | -3.51377 | -40.74578 | 2025-09-21 04:06:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc80e82e-1181-3eae-a163-f3ef87ccae72 | -0.91012 | -47.54605 | 2025-09-21 04:06:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46aac706-61f5-3bab-82bb-c9770b452d32 | -3.51972 | -47.21245 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6862d5d7-025f-3cb1-b71c-d883da61addd | -4.61669 | -38.68146 | 2025-09-21 04:06:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2af1727c-56a0-3e9d-9098-3f7ae9d5f879 | -1.25976 | -47.11568 | 2025-09-21 04:06:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1891c3b9-4d2c-30c1-a794-370a2a115819 | -1.79577 | -48.07129 | 2025-09-21 04:06:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47ea3509-e1df-3b4e-84eb-97eb9976c107 | -1.79143 | -48.07277 | 2025-09-21 04:06:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7890ff9f-9943-3863-a05b-4be6734ebea4 | -0.95301 | -47.35904 | 2025-09-21 04:06:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2ad427a-35d8-327a-8721-cbd2520d594d | -3.84124 | -40.34546 | 2025-09-21 04:06:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ced34f0d-677d-3818-955c-d5383488adb5 | -2.91881 | -48.30204 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da1f7313-9a40-3d2b-be98-4fb5548c7345 | -2.26194 | -47.19404 | 2025-09-21 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 779c13c4-dc3c-333d-8af5-5f4c4505e7bc | -3.86176 | -43.09553 | 2025-09-21 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef2c6627-ebdf-3212-84e4-35ae97760f12 | -2.74423 | -49.54824 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7efc0e12-1c81-38c1-af45-9150f53f2901 | -2.7437 | -49.55137 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a270ffcc-43d2-364d-9fe3-f1f9c786e23a | -1.7962 | -48.0735 | 2025-09-21 04:06:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb2bf2ea-1f38-30b0-96b3-565e053868cd | -3.6821 | -43.51997 | 2025-09-21 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22cedae1-e4d4-3188-8886-338c39f57383 | -4.02099 | -42.77773 | 2025-09-21 04:06:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 93a064a6-165c-38d4-aaf5-b2c257910ef0 | -2.73687 | -49.5526 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffba7829-1087-340e-9f7b-690fa06858f8 | -2.91963 | -48.29699 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8eb30b3f-30b9-3f6f-a31c-0f8e1b267cc9 | -3.86802 | -43.10033 | 2025-09-21 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c21479e-a7a3-30ee-b5b5-aa3a75f58fb6 | -2.60661 | -48.13597 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e0c3f298-0bd8-322f-b860-7fb6aa6c72b0 | -2.61491 | -46.85453 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38684a38-74e6-3d86-beba-510f52a78c24 | -2.61927 | -46.855 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa504d3e-c479-39dc-91c5-fe7f062e28db | -2.73737 | -49.54948 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1899857-9268-37ef-9f26-f3663460f3af | -2.30386 | -48.39434 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 614d461c-687f-3d4f-80d9-a17f64a2ade9 | -3.51236 | -47.20273 | 2025-09-21 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 550e0322-ffcc-321c-b1ca-d018f5fde79f | -3.35085 | -48.3964 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d967027e-81b3-3e47-aa90-c332e0092d50 | -3.14002 | -44.42573 | 2025-09-21 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd12ffb0-b0f3-34a3-8399-b3f8a369cd01 | -3.51605 | -47.20754 | 2025-09-21 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f867ee86-c913-36fc-aefd-7cc30d920ce5 | -3.79902 | -44.08416 | 2025-09-21 04:06:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59f6757f-ebb6-3018-81e0-c9684998cd03 | -3.91767 | -40.74918 | 2025-09-21 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7eb68ac9-2f77-3ba3-a0ee-ec3b7b6d645f | -3.45686 | -47.62674 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11381b5d-47e8-3e89-b554-f83920441fc0 | -2.61859 | -46.85925 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 658e908f-70f9-3174-a842-1c02bb0e1924 | -3.87263 | -43.09341 | 2025-09-21 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a99158cf-ae3d-3809-8642-f9325ab500e8 | -3.13931 | -44.43005 | 2025-09-21 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3822d03-e037-3c62-9209-09ef3f9b6e4c | -4.66547 | -37.63366 | 2025-09-21 04:06:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c35e5dbc-5c58-38eb-b4f0-51c81fbfec54 | -1.12459 | -54.14822 | 2025-09-21 04:06:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e294c17-d699-3ac3-97b8-e925787c9cb2 | -3.86497 | -40.34557 | 2025-09-21 04:06:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15ce7f2d-f207-3b4a-8d4f-cafc11afc0f3 | -3.52041 | -47.20819 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a31c6651-37a9-3a83-b460-042e95977fc5 | -3.49828 | -42.33458 | 2025-09-21 04:06:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71009b33-e439-32ee-b211-974e9139c7d6 | -2.74206 | -49.55342 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1698c113-9a9a-34cd-85bb-10218daf908d | -3.59009 | -43.91521 | 2025-09-21 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b651340-f93b-3ae9-b8e2-1a052e411587 | -3.39102 | -44.76024 | 2025-09-21 04:06:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6289314-0bb6-35ae-9c94-26816f85b61e | -2.26409 | -47.84328 | 2025-09-21 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5af03f6c-ac1b-34b5-beaf-c75e9abc7b46 | -2.74257 | -49.5503 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b27e8a8-9ddc-351f-9b69-8faa4481941d | -2.26285 | -47.19556 | 2025-09-21 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc9abfb2-a477-3306-93b1-566977c4641f | -2.92356 | -48.30276 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5811a33e-366d-3983-b2a8-6ba8c7364681 | -3.86058 | -40.35198 | 2025-09-21 04:06:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31ad7377-993b-3dc3-8336-80cd5c92c7cc | -2.26244 | -47.84515 | 2025-09-21 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f88159f6-6ee9-3c44-8527-5d22837a65f9 | -2.73637 | -49.55573 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba8360cf-d865-3687-a9db-ded56e04b459 | -3.51653 | -40.74973 | 2025-09-21 04:06:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eca7207a-a780-32a8-9e70-4d6c0f815aef | -3.35167 | -48.39136 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d427afcd-b47b-3299-bb5d-a3737fef2e78 | -3.51673 | -47.20333 | 2025-09-21 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81306f40-4715-3f43-bef4-2d69ae0151f9 | -1.86412 | -47.98527 | 2025-09-21 04:06:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba0405a-1c98-36fd-90ef-1bc150cc5d1d | -3.69675 | -38.71626 | 2025-09-21 04:06:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2039966-be35-3a6f-8720-f1118fc54fcf | -3.14027 | -44.42729 | 2025-09-21 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6c25f9b-f527-364d-af0f-b47f503a9bea | -2.62189 | -46.83852 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90b571c8-d810-3e72-81f5-327a339b780c | -3.59106 | -43.09636 | 2025-09-21 04:06:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 580b2489-1576-391e-bf9b-6ea5cdeceb98 | -3.34693 | -48.39059 | 2025-09-21 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 744cf2b3-7a04-3436-ad87-763a7f94b13b | -4.31607 | -41.46655 | 2025-09-21 04:06:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9dc94c50-27b1-3d71-b081-09308e445fa0 | -2.74307 | -49.54717 | 2025-09-21 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc4de288-47ec-3e30-bae3-2d25885b6a17 | -2.30465 | -48.14775 | 2025-09-21 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 42a7e188-a1a3-37ac-abbf-85a9792d45af | -6.2593 | -44.08993 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724ceff2-bf9d-3925-90f8-26ebbb517989 | -6.8478 | -44.15086 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README7.md)
