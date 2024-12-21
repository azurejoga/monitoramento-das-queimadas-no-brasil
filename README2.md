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
| cb45aacd-2e71-361b-bb0c-dba4c3d3ad9b | -4.30144 | -43.7699 | 2024-12-21 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5461fe35-34fe-3d64-a12f-522edf351c4d | -1.88128 | -45.55941 | 2024-12-21 00:43:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3f63c124-a321-34ca-84f1-abba34786351 | -5.46868 | -39.31284 | 2024-12-21 00:43:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 9fdbee86-c80e-38f4-92cf-776bc5ef225b | -3.91608 | -46.67332 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b999694b-8def-3fde-91fc-af3ca33c8520 | -5.60741 | -42.81903 | 2024-12-21 00:43:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8f5a976a-47f1-358f-9899-8dc85fc9c980 | -4.53936 | -44.05726 | 2024-12-21 00:43:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8de0d6c2-c99a-3ef3-ac27-36b887c0f70f | -2.79036 | -45.87144 | 2024-12-21 00:43:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 64b7dbe4-3a64-3988-8366-6aac86c14644 | -6.1724 | -44.3862 | 2024-12-21 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d969ed2e-dcaa-34c9-b101-3fb004d6249c | -5.55592 | -46.3488 | 2024-12-21 00:43:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c2e0ad13-737c-3889-b38c-b82b4f5f75f2 | -3.28737 | -42.52467 | 2024-12-21 00:43:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f747746f-89fb-32c4-9f91-30a9ac938799 | -3.0901 | -46.56628 | 2024-12-21 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 387e0fd8-ae4e-3484-b056-1692a88e88df | -4.93167 | -41.34126 | 2024-12-21 00:43:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4d8deb6d-a306-37b3-8170-69a3e3cf58c0 | -1.36631 | -46.03091 | 2024-12-21 00:43:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2cc77295-4cad-3d65-a6f5-3ea070ba55f6 | -1.5626 | -46.77746 | 2024-12-21 00:43:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5f0ebb06-7f73-3993-a810-f8597bba1e76 | -3.95332 | -46.41006 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 842d6048-f7c1-3120-b3d6-19a80428b009 | -4.00088 | -46.55652 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c248bb4-ae04-3b5a-a233-509bd3e00cb4 | -2.64841 | -46.10754 | 2024-12-21 00:43:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea90f43e-d031-3f24-b42d-a37447635989 | -2.67828 | -46.91576 | 2024-12-21 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 201af68b-166e-32a5-b5bd-6b4b25165d3f | -3.99007 | -46.73796 | 2024-12-21 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe119caf-8eb8-31d1-8c38-1f80e316659a | -5.21481 | -44.90716 | 2024-12-21 00:43:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8f828c37-a7b3-37da-925c-00b3ae9963bb | -1.87211 | -45.5607 | 2024-12-21 00:43:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e94ebfbc-2dd3-3875-9e80-05d5a04f09bc | -3.70567 | -50.20797 | 2024-12-21 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f9a3e77-4475-3621-910f-6f257e58aea6 | -3.17379 | -45.97763 | 2024-12-21 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7cf13db6-0ce6-3086-b805-539acbc07a46 | -2.05685 | -52.06702 | 2024-12-21 00:45:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d978069d-aba4-3088-8280-41bad9137e45 | -1.34164 | -53.84708 | 2024-12-21 00:45:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f99cb72f-6ce1-3d7b-b2a5-c4c17c8111cf | -1.03806 | -47.23891 | 2024-12-21 00:45:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20be9a4d-e973-3b70-8e20-5501ba3a8324 | -1.2938 | -53.11441 | 2024-12-21 00:45:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 187fc59a-2680-3465-82f2-675a57104806 | -1.29623 | -53.13226 | 2024-12-21 00:45:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 4049d632-62b0-3f02-8ac2-93bbaf1c7d43 | -2.07756 | -52.04875 | 2024-12-21 00:45:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 1681ce8b-e544-3a88-8af1-1d57e5ed67e1 | -1.29029 | -53.12144 | 2024-12-21 00:45:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 7c427814-a94f-3807-9d2d-760ecd097fb2 | -1.01511 | -48.07324 | 2024-12-21 00:45:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0b280f2-27f7-3512-be78-a18ad09e85d4 | -0.85708 | -47.13296 | 2024-12-21 00:45:00 | TERRA_M-M | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 991c6aa7-9d3a-3887-addc-f3adcb01227c | -0.35567 | -50.07987 | 2024-12-21 00:45:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a831951b-5b81-3538-bbd6-18eefaf090d1 | -1.30308 | -47.75497 | 2024-12-21 00:45:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 89f9bd9b-0930-3969-8ec6-00c20aab4c0e | -1.33342 | -46.65 | 2024-12-21 00:45:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5be5acb0-6c2d-3936-916b-54f4a7610907 | -0.99854 | -48.88053 | 2024-12-21 00:45:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8d751d2-5423-300a-8ef7-ef6fca240787 | -1.30186 | -47.74614 | 2024-12-21 00:45:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fbd1924-c850-3e5e-9c35-8087a0b2ecef | -2.05656 | -52.05808 | 2024-12-21 00:45:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bb0356ab-34ba-353a-8269-6579578ddec8 | -2.05483 | -52.05192 | 2024-12-21 00:45:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b093076f-6825-3e6e-b805-78cadfb6fa25 | -1.2943 | -53.1303 | 2024-12-21 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 792da4b0-6cfe-3dc4-8099-a317a43f750f | -2.6991 | -45.5809 | 2024-12-21 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| c40ae3ba-4fdd-3239-984c-6581a0fbd2cf | -2.6992 | -45.5585 | 2024-12-21 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2386f8d2-4626-3097-95dd-de30534e8c3a | -9.2215 | -60.3495 | 2024-12-21 00:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 11ee910d-c821-3d03-8ae9-0da054b595e3 | -9.2216 | -60.3302 | 2024-12-21 00:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 77b49509-0ab3-3005-8ce4-4c37abd06378 | -2.7178 | -45.5579 | 2024-12-21 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 80f0f409-fdf3-3a28-ac59-a9999c5ebf64 | -9.2403 | -60.3292 | 2024-12-21 01:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 30ab49d0-dbf7-3a31-b878-501fefdb06ff | -9.2216 | -60.3302 | 2024-12-21 01:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 5cfe45df-6bee-3a99-ab5f-5548c0125760 | -2.6992 | -45.5585 | 2024-12-21 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d5eaf8e3-7abf-33a8-909e-d0a8d60bfe1a | -1.2943 | -53.1303 | 2024-12-21 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bff1ef1c-d293-3f73-8b15-8ea25d234149 | -2.7177 | -45.5803 | 2024-12-21 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 776fada1-7f06-3fcd-bc74-bc9f54a1c2ad | -2.6991 | -45.5809 | 2024-12-21 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 4bd84380-6c24-3c76-972f-aae85862652f | -9.2215 | -60.3495 | 2024-12-21 01:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 30e5ef9a-c27c-343b-9023-90d1257fc093 | -2.6992 | -45.5585 | 2024-12-21 01:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 87cbeb45-8afe-33ea-844e-fb79a7f401cb | -2.6991 | -45.5809 | 2024-12-21 01:10:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9fbe5617-9e3c-3dc9-af42-0375c3d05b74 | -9.2401 | -60.3485 | 2024-12-21 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c8b74bbe-8cb2-32e8-b7ac-596addcefe5c | -9.2215 | -60.3495 | 2024-12-21 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c800e6db-d30a-3420-b5ff-f2f4c0fccbd2 | -9.2216 | -60.3302 | 2024-12-21 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 586ef7f0-4228-3e03-b2c2-281d8b6cba31 | -12.3706 | -52.4911 | 2024-12-21 01:10:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 83d1c6e4-4a1c-3b57-8992-af93ad94a829 | -9.2403 | -60.3292 | 2024-12-21 01:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c9dbb4e8-2ce6-3b45-9bf5-6a312caafe08 | -1.2943 | -53.11 | 2024-12-21 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f9b836ce-45ce-37ed-8b25-b0b87122ea01 | -1.2943 | -53.1303 | 2024-12-21 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 96454d73-a2c5-3f70-aab4-71ae46d0ecc7 | -12.3709 | -52.4701 | 2024-12-21 01:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2c4b91f0-0f91-3fac-bab0-a908d8d125f7 | -9.2215 | -60.3495 | 2024-12-21 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1edaf3b4-9b69-3193-b4e7-fddcc28ca914 | -12.3706 | -52.4911 | 2024-12-21 01:20:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 45b13e45-22c6-3701-93bf-443a23cc4784 | -9.2401 | -60.3485 | 2024-12-21 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9a8c7ee6-00e4-3cea-ba3b-0e3be2095213 | -9.2403 | -60.3292 | 2024-12-21 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 2ff07cb2-8981-3812-8129-4a65e544b365 | -9.2216 | -60.3302 | 2024-12-21 01:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 2d08796c-1658-3422-9f1d-a5c073b59d03 | -9.2215 | -60.3495 | 2024-12-21 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4e12ffcb-9dea-35c0-8ca2-dabbd80f48c2 | -9.2403 | -60.3292 | 2024-12-21 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 97e930f0-2f31-3e69-81ce-8b62cfde9a11 | -12.3706 | -52.4911 | 2024-12-21 01:30:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 8929d9a9-57e6-3f1f-a5a2-13b616b36484 | -9.2216 | -60.3302 | 2024-12-21 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 812f79cc-0e0b-33c4-a7fb-a0b6fb0a77fe | -1.2943 | -53.1303 | 2024-12-21 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8eae439a-ed01-3091-a27b-69c3b7bce54f | -9.2401 | -60.3485 | 2024-12-21 01:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 05e569b7-4b99-333a-96b9-1e5e60d23704 | -12.3709 | -52.4701 | 2024-12-21 01:30:00 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1744eb5d-62c1-3a2a-8e77-bcd658fffcd3 | -9.22905 | -60.33447 | 2024-12-21 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 81e7fc99-4443-39d6-ad32-a79a2686d495 | -9.22506 | -60.34045 | 2024-12-21 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 699697b9-a056-36e2-8bd0-38dd25ed97c5 | -7.6868 | -35.26116 | 2024-12-21 03:06:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 76a57b11-6f3e-34bb-ae50-41479a73277d | -5.82408 | -39.21567 | 2024-12-21 03:06:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a589b17e-04f3-3509-8d25-d598b6af58b7 | -5.82428 | -39.21925 | 2024-12-21 03:06:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9cd174c-c937-3a01-9fc5-d75130cd59a0 | -5.17943 | -37.58751 | 2024-12-21 03:06:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5fb3061d-8aa5-3116-b0fc-70190d7d9253 | -7.68623 | -35.26438 | 2024-12-21 03:06:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7c1ba63f-3d70-326c-8b14-0b9851de0369 | -5.82548 | -39.21259 | 2024-12-21 03:06:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 29275e48-2884-3bff-ade0-50a7da84f800 | -5.61433 | -35.35597 | 2024-12-21 03:06:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2b32817d-8282-3237-aa49-8008c3d53b3b | -5.1785 | -37.59274 | 2024-12-21 03:06:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c4868b0f-f052-3a33-b659-0c0d7074987e | -17.75293 | -39.595 | 2024-12-21 03:08:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5cec8b3f-a18c-35fd-9b97-e6472e240018 | -12.92297 | -40.58649 | 2024-12-21 03:08:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e569e887-65ab-32b3-8839-cb6bb40bf807 | -15.38917 | -39.38925 | 2024-12-21 03:08:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 697e7e56-f1ac-3777-a0a7-fb95336b8bb5 | -5.17683 | -37.5879 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3cab3fc2-6c95-3234-a1e4-d62f21637287 | -4.58613 | -38.60718 | 2024-12-21 03:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9b36a3f1-bf07-3254-bca7-63521b0b6da0 | -4.58155 | -38.60631 | 2024-12-21 03:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2c558d40-d6a4-3a33-9fc0-b72a74d4cf6a | -3.83461 | -41.56702 | 2024-12-21 03:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 479880d3-f359-3149-9b8a-9bb200e410fa | -5.1775 | -37.58396 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e0f3b48f-0166-3cf6-9151-4c0f3b488753 | -5.17739 | -37.59352 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c421ddfe-b5ed-38bd-be42-b71ca22b71aa | -5.17803 | -37.58955 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ffe71e13-4adf-3885-ac90-51aa04167621 | -3.28936 | -42.52954 | 2024-12-21 03:27:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ad5b42e-9f7e-3c5e-83be-d54f89d92861 | -3.29012 | -42.52492 | 2024-12-21 03:27:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad49021-af36-3d86-9344-9e89ec0b9a8e | -5.17616 | -37.59185 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 53842544-e115-3774-bbc1-aa9aac1e9a67 | -4.5854 | -38.60404 | 2024-12-21 03:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7e7de4a2-715a-30c5-9249-7b835cb3fac9 | -5.17443 | -37.58488 | 2024-12-21 03:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3186f7d4-f939-3dd8-8482-ad39e2782f1b | -5.36965 | -36.71791 | 2024-12-21 03:27:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
