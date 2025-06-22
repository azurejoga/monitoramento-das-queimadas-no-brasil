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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67447539-06cd-3c8c-8684-6a17a4d65526 | -10.9815 | -45.0874 | 2025-06-22 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b777c80d-3710-33eb-a84d-753628f688ce | -8.6097 | -51.5731 | 2025-06-22 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a00f1aa9-b6ba-365a-8b7c-b08788c1292f | -9.553 | -40.3503 | 2025-06-22 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| a749e782-8299-31de-8d2c-8a73a83c4a6f | -12.4767 | -54.4302 | 2025-06-22 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| ab211ff4-1b01-3b82-967f-0b609f60e50f | -9.4622 | -56.0614 | 2025-06-22 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4f9cd4c4-1711-32ea-bee4-f6329cb8a1dd | -9.16757 | -61.40022 | 2025-06-22 02:00:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e72312ae-9894-3b79-a882-f395509058b4 | -9.1791 | -61.41568 | 2025-06-22 02:00:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 753cded7-f068-39f0-a4d5-31c1aff99e91 | -8.5907 | -51.5955 | 2025-06-22 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e1320566-d351-3031-8ed1-48396d378759 | -12.4767 | -54.4302 | 2025-06-22 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2651b9bf-7c5b-39d4-b73d-ea8ee6c7a98a | -12.477 | -54.4096 | 2025-06-22 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2535d091-51ea-3453-94f6-39034611f20b | -10.9324 | -57.1312 | 2025-06-22 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ace7c8d7-eb8d-3434-93ff-9630042c0526 | -8.5909 | -51.5746 | 2025-06-22 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| ea466921-2f75-3784-ab08-13eeed11a2cc | -12.4767 | -54.4302 | 2025-06-22 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 87f8a4f5-ac06-3373-a6e1-ad2d4489b322 | -9.4622 | -56.0614 | 2025-06-22 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f3d7aa91-208c-39a6-87c6-708b970067ac | -12.477 | -54.4096 | 2025-06-22 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| f05fa13d-1170-3a6b-94ab-04ed5730663d | -8.5907 | -51.5955 | 2025-06-22 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1ef95d34-2dcb-3cd3-94d4-41ac9e292997 | -10.9324 | -57.1312 | 2025-06-22 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0ed9148c-70f1-3628-8cea-3e4a53e56aed | -8.5909 | -51.5746 | 2025-06-22 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4fe7740a-ea83-3d38-b3d3-9e1af8ae6d67 | -11.0006 | -45.0847 | 2025-06-22 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 78d87055-5099-34fa-9c8b-9f8b4acc25b3 | -12.4767 | -54.4302 | 2025-06-22 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a341844d-a910-34fb-8377-2d0634197c32 | -11.617 | -58.289 | 2025-06-22 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| cb754474-a82f-37d4-8142-485c4b28991a | -9.4622 | -56.0614 | 2025-06-22 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 18f1ee27-86d7-3689-978b-0f15096b8c9b | -10.9324 | -57.1312 | 2025-06-22 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 27c4b9ab-ab73-337b-a484-dc2dc3f60923 | -9.4622 | -56.0614 | 2025-06-22 02:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ae61417b-f308-32b9-aff0-0baa1a47a3bf | -8.5907 | -51.5955 | 2025-06-22 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1e46413f-c32c-32e9-9379-ce545d8a0f56 | -12.4767 | -54.4302 | 2025-06-22 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5e611fcb-b6c0-379c-9e97-2641c78b1297 | -8.5909 | -51.5746 | 2025-06-22 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ca9b9d3b-354b-38e5-9729-fd9d86a1d19e | -8.5909 | -51.5746 | 2025-06-22 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9e6e10ad-22d2-3c60-baef-35f6f4c714d7 | -9.4622 | -56.0614 | 2025-06-22 02:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 8a93f4e2-89d9-325f-8d32-d88b3759619d | -8.6097 | -51.5731 | 2025-06-22 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 26b8a656-cbdc-3249-86dc-7b6d8827e2ca | -12.4767 | -54.4302 | 2025-06-22 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d3e7065c-ac65-32d7-a19b-cde392538f98 | -10.9815 | -45.0874 | 2025-06-22 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| bdeee2f8-7417-3bfe-9efd-cd44d690661a | -12.4767 | -54.4302 | 2025-06-22 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0a031030-b62d-3f0a-9785-1e54fdf3e630 | -10.9815 | -45.0874 | 2025-06-22 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7bc337e9-8514-3497-b6f6-6c2d7d7e25e9 | -8.6094 | -51.594 | 2025-06-22 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1d50e466-12f2-304e-ab91-2dd808af09d4 | -20.7299 | -41.91195 | 2025-06-22 03:04:00 | NPP-375D | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2938c79a-253e-33f6-a95a-a2f77e46824b | -20.73145 | -41.9057 | 2025-06-22 03:04:00 | NPP-375D | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ba4d6443-785e-3aab-9b3e-5428fcd64dcc | -12.4767 | -54.4302 | 2025-06-22 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3f69b868-a685-3ea0-8fff-6a9db2e6257c | -12.4767 | -54.4302 | 2025-06-22 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ccae4aea-90e6-32a8-bceb-4755d0147f59 | -8.80738 | -38.39016 | 2025-06-22 03:21:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71342790-9cf1-3762-af53-1f8fce978d9f | -8.10836 | -43.14873 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b8140999-89f7-3e78-8b83-6817238ed626 | -8.1019 | -43.14748 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5cf22e6f-8aee-3c38-a3bd-8431c6cb1d9c | -8.10863 | -43.14769 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9d0e524f-fb2f-39fb-a6d9-c831d00a3e75 | -7.37755 | -34.8876 | 2025-06-22 03:21:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| baf1d86d-661c-3676-83e4-5556f971dee2 | -8.11611 | -43.14349 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 50944c95-ab17-3f3a-aa58-14ab629bdef0 | -8.11482 | -43.14999 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e5f85d70-6848-397c-a169-7320717647c1 | -8.10083 | -43.15295 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 1ec958f7-b4d7-36d3-8dfe-83f5f7fa31c3 | -8.10942 | -43.14328 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ec83cf7b-2383-3b7b-a33f-8603a1420d46 | -8.08071 | -43.15364 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ffcd0d20-d9c3-3637-ba7a-efabdc0de175 | -8.81208 | -38.39099 | 2025-06-22 03:21:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 868d47dd-17ab-324d-b411-ece3183af2b5 | -8.09469 | -43.1506 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e361234b-999a-36a1-92f6-9ab0da6e2af3 | -8.11588 | -43.14453 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3f6e1f16-38b5-31d3-90f0-9ebbb546671e | -8.11509 | -43.14897 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 1833bc29-e467-309b-a81a-c899f2e57f92 | -8.08823 | -43.14932 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| af339c69-db8e-3776-9d60-5c90f294d020 | -8.06966 | -43.10611 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8b9b3833-f20f-3b64-996b-5b1f89f4c130 | -8.07422 | -43.15251 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1a793d41-21fe-3a60-a7d3-e6781db391b2 | -8.10114 | -43.15189 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f38e183a-73ef-336b-a97d-29bc8d34be1d | -8.10218 | -43.14641 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a888e9ba-a25f-3150-8e87-dd762ecce213 | -8.06863 | -43.11152 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 082ce1e7-501f-37fb-bd7a-a475bebe7f98 | -8.08719 | -43.15483 | 2025-06-22 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f57b4189-49f1-3257-8d5d-b2bc3d40e5bb | -12.42113 | -43.81845 | 2025-06-22 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 295d7188-21d9-3d32-b3b6-d1b61133396f | -12.4149 | -43.81699 | 2025-06-22 03:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01dd6bf6-9445-37b6-b62a-704f93b94c65 | -21.62375 | -43.46453 | 2025-06-22 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7914e03c-ae3b-3633-9437-6c15d4b9113e | -20.48789 | -42.38013 | 2025-06-22 03:25:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3636e8f1-792c-34a4-8939-ee3f9c301446 | -20.73367 | -41.90959 | 2025-06-22 03:25:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7c8103ef-f57e-3f67-a49a-b7004b75d4c6 | -22.73796 | -42.95836 | 2025-06-22 03:25:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2257443f-4d4b-32dd-9f81-ede354d5a2e2 | -22.95545 | -42.68678 | 2025-06-22 03:25:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 537d9f94-8bc8-3fdc-85fc-4cf7fe0f1841 | -22.95414 | -42.68764 | 2025-06-22 03:25:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5e4a562-509b-35ef-8c53-b4056944a7db | -19.62146 | -43.82177 | 2025-06-22 03:25:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24e96f06-2bca-374f-a6db-abe5371bd0be | -22.95532 | -42.68217 | 2025-06-22 03:25:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a4bda5b8-e33b-38b7-9fe2-158f2eb62bcc | -18.05556 | -44.49209 | 2025-06-22 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e750532a-792e-3ff8-bd65-c12d2ae30b42 | -20.72893 | -41.90845 | 2025-06-22 03:25:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6397482e-4c6c-34b3-86c5-4c1da0e6137f | -21.62302 | -43.46786 | 2025-06-22 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e7553e7-4c38-31d5-9b69-e4f1eae80056 | -19.62223 | -43.81822 | 2025-06-22 03:25:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f568582a-f4ec-3a4f-a0e3-1b99af31fd97 | -20.72936 | -41.90435 | 2025-06-22 03:25:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4ef355ed-ce05-3628-b1c9-c8daff0bee53 | -18.01883 | -43.06537 | 2025-06-22 03:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c22b5d64-927a-3173-8c9a-19902d78dec1 | -29.86028 | -51.16812 | 2025-06-22 03:28:00 | NOAA-20 | ESTEIO | RIO GRANDE DO SUL | Brasil | 4307708 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 6d655a91-dfe9-318a-a700-4b4b6fe160e3 | -12.4767 | -54.4302 | 2025-06-22 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 08855cda-69da-3823-b739-4f0d0a0fc3f1 | -8.80888 | -38.39249 | 2025-06-22 04:14:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50d716de-2017-3338-9852-97ad13186e50 | -9.33115 | -47.82552 | 2025-06-22 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eb738fc-21ff-3bbb-8863-61a2d0ac1d39 | -8.09039 | -43.14967 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5f79eb3d-ad9d-340f-a53b-614b589d854d | -9.15215 | -47.15276 | 2025-06-22 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a7658a1-72e0-352c-8264-fd4475e83784 | -10.65319 | -44.49591 | 2025-06-22 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b1a4b01-db3f-3572-b2f3-a05bf8a8819a | -7.98313 | -46.2066 | 2025-06-22 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67620397-b34f-36c1-9696-b87007651ce1 | -7.97549 | -46.20928 | 2025-06-22 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20dc06a6-363a-3bb5-b601-456f90801145 | -4.42382 | -48.14461 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28180d81-3b62-3f54-b080-5834bade22b1 | -7.22954 | -44.66532 | 2025-06-22 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2d651bd-8f01-3ae0-a649-138315ba35fa | -9.39064 | -47.49921 | 2025-06-22 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 483da591-283a-3455-a170-f2bce25a0c5a | -5.57202 | -45.21738 | 2025-06-22 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 214c80e1-0c21-3f38-abb4-1481fd2a5582 | -6.85682 | -43.16354 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| f6b82784-3165-3dcd-987b-2220c7d6e9cc | -8.02677 | -47.64548 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16b9cbfa-ad34-3aff-b1d9-4b2970581e05 | -7.87761 | -47.88912 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b309fc55-6f6d-31f0-878b-4cceb5d3e9d4 | -4.53801 | -48.00954 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ebf1779-0f77-3087-b597-2be66ec84d68 | -7.10762 | -43.71264 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c14c53-059e-3ec7-9125-a4131e37fc37 | -7.10378 | -43.71558 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 534d4d31-e6bb-397d-b14c-abc75a57d84a | -7.3167 | -43.18015 | 2025-06-22 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2063b089-00aa-3a45-bd1c-cbf75166f51d | -8.11129 | -43.14583 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| f0e8fa25-38ff-3e84-b25b-a23046f67c21 | -7.07078 | -47.85017 | 2025-06-22 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5926006-3e73-36f8-ab15-f6f9b2cb1181 | -5.46979 | -44.68893 | 2025-06-22 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbdd9e68-3f9f-3f32-85bc-959276602c39 | -5.1564 | -46.09217 | 2025-06-22 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)
