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
| 7b21e1f0-d1bd-3f41-86e0-90b487de294c | -7.11769 | -42.75827 | 2026-08-31 03:17:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6811cb5f-2d20-3a27-84e9-2aba789c7671 | -9.00578 | -39.88544 | 2026-08-31 03:17:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 24482232-97ad-39e2-a119-78c6ed38582d | -11.20109 | -43.37764 | 2026-08-31 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a140b8a7-4584-328e-8b62-fdddda0a9886 | -17.79171 | -39.70339 | 2026-08-31 03:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c887a04d-6090-3520-9299-d3a0be0e4254 | -11.20784 | -43.37914 | 2026-08-31 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 44dbe2a0-566e-34a4-a24c-e659d9942fb0 | -17.79063 | -39.70889 | 2026-08-31 03:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 76575294-2848-3aa8-a1ee-affb253a606d | -15.70106 | -39.89539 | 2026-08-31 03:19:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8b6ebe9e-5752-3afa-a87e-c089e340e3b8 | -17.52833 | -40.24374 | 2026-08-31 03:19:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f7951960-d9ab-30c1-a628-666fec11d630 | -15.90639 | -42.39923 | 2026-08-31 03:19:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae2a0dce-3955-351e-bb66-8fced4fbf169 | -13.38798 | -41.32631 | 2026-08-31 03:19:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 3364c706-2269-310e-8c9d-648208a74fc8 | -17.52459 | -40.23652 | 2026-08-31 03:19:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 56a00f70-8ad1-3639-afd1-a2e577ea577e | -17.79543 | -39.70993 | 2026-08-31 03:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| caee498b-b3f5-30ae-bd84-7c89a50e66d9 | -13.38719 | -41.33016 | 2026-08-31 03:19:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| a22cec98-1f94-36cc-8a0a-ce528a74b398 | -15.90059 | -42.39757 | 2026-08-31 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2efbc043-9d47-36a7-81a3-3ec9bd00c896 | -13.19348 | -44.06647 | 2026-08-31 03:19:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d077a1a-f299-3193-8533-5f7a662fbca7 | -17.52398 | -40.23953 | 2026-08-31 03:19:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 12ffde93-425d-370c-942e-d51e06d90f23 | -13.48167 | -42.4764 | 2026-08-31 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 17a4ccec-f9ad-348f-aa39-ef7c08b9fbda | -15.70616 | -39.89622 | 2026-08-31 03:19:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5a372c0-ae6e-3342-82ae-b2ccabcde0a1 | -16.28273 | -42.58329 | 2026-08-31 03:19:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b88a42e1-284d-3277-98be-271fb44a6f98 | -13.38636 | -41.33424 | 2026-08-31 03:19:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 065b5105-777b-3568-b4a0-7453e1a24ede | -14.20089 | -44.58591 | 2026-08-31 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0309e5a1-2997-3aac-b616-7d94207a9452 | -17.79651 | -39.70444 | 2026-08-31 03:19:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7fb267fb-ccd3-317d-be62-a5a574869877 | -16.28982 | -42.57909 | 2026-08-31 03:19:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58efd9a0-267d-3d3a-99ad-486f931a7832 | -17.28932 | -46.00455 | 2026-08-31 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2a75dd71-000b-34f9-b319-ef828e56848f | -11.20655 | -43.38546 | 2026-08-31 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78e7b408-4b94-3623-b57e-a95a4ba31255 | -13.48063 | -42.48139 | 2026-08-31 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f7de4409-f2f5-3023-bd23-3bfe29ab7139 | -15.11737 | -40.04683 | 2026-08-31 03:19:00 | NOAA-21 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c377465-5b25-387e-8141-59b9b6ecb0cb | -15.11223 | -40.04566 | 2026-08-31 03:19:00 | NOAA-21 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b87d9ff2-5888-3545-8350-0d690ca821cc | -16.2767 | -42.58257 | 2026-08-31 03:19:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d94c38c-30fd-3291-a661-ffca0865b0c3 | -6.1111 | -57.6645 | 2026-08-31 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a487974c-4b1f-35f9-b703-42f74fe16d56 | -6.6036 | -58.5972 | 2026-08-31 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 56c8a7c8-554a-33ae-84fa-6b50ca82ea47 | -5.2362 | -55.9112 | 2026-08-31 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0cf8aca4-3efa-345d-b01d-9dd864840583 | -7.9239 | -44.2327 | 2026-08-31 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c5e74bf8-a263-3775-afbb-4805efb8c9ca | -18.2904 | -52.6818 | 2026-08-31 03:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 29636631-e2c5-3866-9eb4-719103b7c5e7 | -5.2363 | -55.8914 | 2026-08-31 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 088c8169-e63f-3f44-9a9b-e20948d20e2c | -10.746 | -50.6386 | 2026-08-31 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 2fafed89-5313-3ef4-a18e-af939459bda8 | -10.8025 | -50.6539 | 2026-08-31 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 30c5bbc8-01cd-39e2-b4a4-10d991fcccc0 | -5.2547 | -55.9105 | 2026-08-31 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 233.5 |
| e29ef842-f46d-3750-809d-dd7285740884 | -6.1295 | -57.6637 | 2026-08-31 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ab45af23-50a8-3209-8554-61c7dc6fd178 | -6.77 | -55.6445 | 2026-08-31 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| c4570ffc-1f28-3c36-85a5-003d9a7fedc7 | -10.7457 | -50.6599 | 2026-08-31 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 71d648bb-aa97-3648-8957-795642aa419c | -1.5859 | -54.3953 | 2026-08-31 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 770b5880-1bbb-3bf6-9af9-c3c08347ae7f | -6.622 | -58.5965 | 2026-08-31 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bd2fbda3-9c91-3b83-aa89-2db3f167b1b4 | -7.9236 | -44.2558 | 2026-08-31 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5e7b54df-02d5-345f-b004-868fccc69f37 | -5.2548 | -55.8907 | 2026-08-31 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| a031336a-3435-3bc7-ade0-eb7da2423415 | -6.1294 | -57.6833 | 2026-08-31 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 1c3734af-3ade-397b-ae1e-d5a9df948d3c | -1.5859 | -54.4153 | 2026-08-31 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| bf62d5e7-baf0-3b23-acd1-d68f7777a35f | -6.6035 | -58.6166 | 2026-08-31 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5ebf1a2b-7e97-33b8-ae6d-f02f5cc8c265 | -6.1109 | -57.684 | 2026-08-31 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7a098ea7-2ad4-32f4-9373-b9d3c5df27a0 | -10.8022 | -50.6752 | 2026-08-31 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0aa1f967-dc2a-3a67-8d9a-d462c8292ddd | -20.46823 | -44.41523 | 2026-08-31 03:21:00 | NOAA-21 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2c9bc5d9-bce6-3c5b-8613-64d68665e799 | -17.98956 | -44.31363 | 2026-08-31 03:21:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0260d255-b4d3-33b4-a4ad-efcd64dd1694 | -6.1295 | -57.6637 | 2026-08-31 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| df5bf156-76fa-3e50-9449-4279f97e2798 | -6.1109 | -57.684 | 2026-08-31 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6e3df247-04f1-3b2b-8a5b-6bb0d7553989 | -5.2363 | -55.8914 | 2026-08-31 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 093f5f4e-17e3-3a5b-b6cd-76c1ae8d5aa4 | -6.6036 | -58.5972 | 2026-08-31 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 81d40186-4f06-3999-a3ff-2c599a27eb6c | -7.3118 | -60.5897 | 2026-08-31 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 40e4b11f-5ad3-3a3b-86da-8d4b49113e3f | -10.8025 | -50.6539 | 2026-08-31 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| e343087d-5baf-3a8b-a871-3f4c46ec5a73 | -6.1294 | -57.6833 | 2026-08-31 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d3716b8c-5af3-3f89-94a8-5cca49d25e66 | -10.8215 | -50.6519 | 2026-08-31 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 269c4075-6903-3a6a-8624-c209828d03ac | -5.2362 | -55.9112 | 2026-08-31 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d7edc74d-60ac-3edf-9942-e743bbe9e79b | -10.8022 | -50.6752 | 2026-08-31 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 1e668942-e839-38f0-ab4a-c76977aa7038 | -5.2547 | -55.9105 | 2026-08-31 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 233.4 |
| 9442e956-4a2f-36fe-b420-3329873921ed | -7.9239 | -44.2327 | 2026-08-31 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e4f303f5-22ba-399f-a738-fe1ae0c07fb7 | -5.2548 | -55.8907 | 2026-08-31 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 2db05f87-be5d-36de-882a-7d0e56e467a6 | -6.1111 | -57.6645 | 2026-08-31 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2dedbf08-8fa6-3d76-96d4-47fe7e7b0ee8 | -6.77 | -55.6445 | 2026-08-31 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 7c1ce1c6-5c3c-36e2-8ab4-769b5b02bbdd | -18.2904 | -52.6818 | 2026-08-31 03:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 894fcd07-e5a3-3a98-b7b5-cdee5e0b37c8 | -6.6035 | -58.6166 | 2026-08-31 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 93d2d168-fc4b-3bc3-9cfa-2476a3e50b01 | -7.9236 | -44.2558 | 2026-08-31 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 69ea45a4-5af9-34ff-823e-6eab9b6ca0f1 | -5.2548 | -55.8907 | 2026-08-31 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| bfcc4452-5a26-3b23-9a4b-fef33550a7ac | -5.2362 | -55.9112 | 2026-08-31 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 7fc89d2f-b9d3-3460-8ea8-3df110faeb34 | -15.0244 | -48.1689 | 2026-08-31 03:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c4deeb53-e28b-336c-9f3c-07ea102fe32a | -5.2363 | -55.8914 | 2026-08-31 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 03004392-6e8f-3151-a17c-e86fe87e7313 | -6.1294 | -57.6833 | 2026-08-31 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b7acdd59-44a0-3019-8300-8292cb4fc5e2 | -10.7407 | -54.0401 | 2026-08-31 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 8ad6135c-aa98-3477-824a-e9a89744c904 | -6.6035 | -58.6166 | 2026-08-31 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 33f492b4-96a4-33ab-a025-6d088d123da0 | -6.1295 | -57.6637 | 2026-08-31 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ed4f72df-c446-3fef-8afa-85b61f0adeb3 | -14.6061 | -54.113 | 2026-08-31 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 630eaa51-862a-3bea-be98-88d35ced1c58 | -6.6036 | -58.5972 | 2026-08-31 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| f2d9476c-82ea-3b48-8d11-7e1ab6013b14 | -18.2904 | -52.6818 | 2026-08-31 03:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 8ed4f139-1d1b-3822-a130-8343b5860c66 | -5.2547 | -55.9105 | 2026-08-31 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 7d716b90-e431-3920-abbe-ebdce530e6bd | -5.2363 | -55.8914 | 2026-08-31 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 241a77fa-0dd7-3dc7-b1ff-1ba786c05345 | -5.2547 | -55.9105 | 2026-08-31 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 182.7 |
| b9da0828-397a-3fa8-b371-6865b0c2cde7 | -7.3118 | -60.5897 | 2026-08-31 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c3657ea6-a554-3d43-8878-b679ee9040c6 | -5.2548 | -55.8907 | 2026-08-31 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| dc7ef371-e1d7-332a-9067-ba73afaec7ed | -6.1295 | -57.6637 | 2026-08-31 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9b4e30d6-0d30-3359-a970-f5c75414cfae | -6.6035 | -58.6166 | 2026-08-31 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 30f22270-70c1-337e-8b42-51513fd8d9ce | -5.2362 | -55.9112 | 2026-08-31 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e472021d-0e14-3167-90a8-dc883300e97e | -6.1294 | -57.6833 | 2026-08-31 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a34c7e4a-53a3-3e98-b755-ef07af515d05 | -6.6036 | -58.5972 | 2026-08-31 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 2a42f873-570c-3516-b52e-16361978f910 | -3.40075 | -43.27298 | 2026-08-31 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ead20f4-af21-3f31-8fc4-1d0bcd475227 | -8.37601 | -45.76545 | 2026-08-31 03:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc6f402-f745-31a9-91a6-b4173db91499 | -6.86792 | -44.43715 | 2026-08-31 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86abd1ce-acee-30ab-908f-cecaf3021a2f | -7.78752 | -43.95642 | 2026-08-31 03:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2510eed-2823-3e02-b431-c26bf4d21575 | -8.07775 | -45.47486 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eee7509-8bda-378b-a5d1-d6d70ca0cd1f | -7.14557 | -46.17085 | 2026-08-31 03:53:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73f272e3-4187-3016-8626-fb803565a1c4 | -7.41977 | -44.26358 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9134cef-8c93-3e3f-be46-b7cee347aad9 | -8.74991 | -46.45279 | 2026-08-31 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4932af3-11c0-3509-bb58-a8c8246bcd78 | -9.00387 | -39.88722 | 2026-08-31 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README18.md)
