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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfe47971-e6db-3fe2-9a74-082f245dac60 | -6.93062 | -38.73505 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1b5afcac-a8c6-39fc-8069-e90e5f59beb4 | -7.88272 | -44.82768 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 88d2a0f0-66fd-3ca3-affb-74c8307f34df | -7.34897 | -44.45918 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9b38746f-41b4-355e-bbdc-956906977afd | -3.59608 | -45.34248 | 2026-09-21 16:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 50846a36-6f6c-3662-87cf-13dd91b8cf51 | -7.53776 | -45.20951 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1b86034-2feb-3532-a975-1ff268e008f1 | -3.47688 | -42.5258 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 683c3844-24e9-3028-a275-87fa26e27bb9 | -7.33613 | -44.46545 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5662b1e8-305e-3f54-b63b-cbc44f08f0a3 | -6.56066 | -45.53745 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4cb1bbbd-c856-31d8-b15c-189c93b22637 | -4.51513 | -43.54533 | 2026-09-21 16:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90048a58-30ed-3357-8186-fc742378fb14 | -6.5559 | -45.53819 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 183fe303-db62-34fb-bb7b-2ed294dfd8d2 | -7.45444 | -44.74085 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 154c65ad-b001-3449-bef6-3a7032e52c9b | -6.97669 | -45.82117 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| aa127d0c-4663-3e88-b608-dbeeb0f058f0 | -6.97746 | -45.82672 | 2026-09-21 16:03:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c8a977a5-88ea-34dd-8514-0716eb65129f | -5.77329 | -47.36589 | 2026-09-21 16:03:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f0ce788-e92a-3751-af7c-e981c62fdf0f | -4.5124 | -44.96467 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f170a3f2-3572-35a4-9e46-c66c0b86d5bd | -7.51633 | -46.21994 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b178ee86-b4bb-317a-983a-7d9ec0d483c3 | -6.24399 | -41.66126 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 50a8aec2-d469-3194-b167-17dc87029afd | -6.39333 | -45.18969 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4905b873-d5be-35e6-ad4d-4b012c318968 | -7.06428 | -43.67025 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a6e7c438-8a97-346b-83d5-20b19fcd07ab | -8.35387 | -45.67954 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d1d336e6-57c1-33d1-a4d4-55023b89a69a | -6.99533 | -44.71429 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fc7ae6d-bd78-3c59-86fd-4f04b6b7f190 | -3.33953 | -42.77458 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 23bc72be-f2a3-3088-a418-97e42b136e3c | -6.85037 | -43.71577 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 044ed23b-4333-30c9-8140-1086c04cc8a3 | -6.48823 | -44.76664 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c3daf8e2-94b8-3f48-a226-98b6aee9fa7e | -6.98595 | -44.70293 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 1e5c8d1d-9cdc-379a-9d5d-50e4684927d2 | -6.90866 | -42.91538 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| d77403e7-a35e-378f-9437-e0527888ac97 | -3.67253 | -38.83344 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8d4b4594-9c68-352c-95ae-0a1e4e29e34e | -7.00672 | -42.17657 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| aedaa76a-ab0f-3997-89ae-3115eb865dc2 | -8.80245 | -48.7374 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 54dca450-2824-3e68-a412-ce19c82c1c51 | -6.18351 | -47.60764 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c74dc6c6-8704-3a01-a80c-39c6f499f814 | -5.74932 | -43.6995 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 17b08b9c-6830-3748-baaf-641eb3647663 | -1.89776 | -48.26844 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d00c4bb4-8ac4-3ade-a596-896b89e4d813 | -3.16315 | -48.07446 | 2026-09-21 16:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bca02946-65d5-377d-9b86-a3dd6e02d74f | -1.4468 | -49.75012 | 2026-09-21 16:03:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1cdacfa6-d154-35aa-ade3-0c4b991af9e0 | -7.0919 | -43.93246 | 2026-09-21 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5fb1f680-3b8c-3233-bd51-2aae95fa4de0 | -7.5613 | -42.65601 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fb3b4e22-346d-38d2-9783-068fd0fe045d | -7.74193 | -43.88969 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 12c178da-3276-3fdb-a714-a0dec195421a | -6.16579 | -44.67511 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3483358e-7f02-3a76-a165-91b764ba0fb4 | -6.56681 | -39.32288 | 2026-09-21 16:03:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6385baa7-f29e-3c32-83bc-5090760d702e | -8.77942 | -49.9555 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 99cfb9f4-95b6-3be0-87a5-ae02bd5abbfb | -5.50413 | -45.54993 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 354678cd-6e00-30ef-baff-6cb54b5103c9 | -7.95542 | -44.07366 | 2026-09-21 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aff32cdf-88e4-33eb-aa89-17907616ddb3 | -6.83337 | -45.56303 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2efea1f9-7a6e-369b-bccf-5b2c40e39c3b | -3.41261 | -42.92855 | 2026-09-21 16:03:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e1ab283b-9639-3c84-ad5e-b3e73f0ba978 | -8.48578 | -47.02085 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 37396468-8efa-385f-a07c-c70c428b0b93 | -1.75018 | -48.18453 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 0bda933d-c548-3c4b-9dbe-28687672dd2c | -4.85003 | -43.55809 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e39c230-1205-3610-b048-3ace2f8afcfd | -2.47475 | -49.81533 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06b8662b-fa62-3da2-b991-5d0577695576 | -7.74011 | -46.78006 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 45c971a4-755e-3e09-bcb1-6f583bf4b5f6 | -3.57622 | -43.46826 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| edcb7503-7665-3c5b-aac1-704c91443383 | -6.55732 | -45.54815 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d4452835-0425-3b04-8434-5d7cbe8de2ec | -6.00889 | -44.11507 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fbc8276a-0611-3f5d-bb4e-1f1ab31ce783 | -6.92126 | -42.94587 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 6e197adc-cede-3e93-bd0a-a9933dc2a2de | -3.02378 | -43.88005 | 2026-09-21 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad7d097b-d94f-33a3-b44d-60a162b6abe1 | -8.42937 | -45.82431 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cffddfd5-3b10-3ef3-b837-49a658f2e0a5 | -3.39077 | -42.85974 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4a00f7b-a3f0-3b82-947f-e732e4d02e39 | -4.51752 | -44.96854 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2f336c8e-1305-3633-baa4-d81d2bbb1a0c | -5.6758 | -43.42614 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 579ddb38-ad48-37dc-9a6a-2d5e3a596579 | -6.55377 | -44.83759 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78929736-9831-38e6-80e6-1369c84e566a | -3.41394 | -43.26585 | 2026-09-21 16:03:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8f466117-efd4-3190-95f9-f95094052bf4 | -4.86331 | -43.56359 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b7f63336-5c4e-36ae-9cd3-a0f87e646e92 | -7.33296 | -44.47547 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8a65fbe4-d93e-354e-a5bd-e63e437cdbba | -3.55901 | -40.89569 | 2026-09-21 16:03:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 692cd917-9968-356b-b5a3-1f5fd2ec1323 | -4.20415 | -44.79461 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c73d911f-f7ed-3677-9f44-17324876b9c6 | -7.3662 | -44.71409 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61f24bf8-32ad-3b53-8dde-665f91e606c7 | -5.74067 | -43.72745 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 4b376900-b940-386f-86b9-0c3a68fb2409 | -3.18075 | -42.80102 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| bad688ad-8937-387c-bddc-ed2a65b348b5 | -4.83309 | -43.33294 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b44a2120-cd1a-3bf5-b0da-a9da5c8384a0 | -2.94906 | -51.04578 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 5e94a234-4645-3118-8f1f-e2632b64353b | -6.74348 | -46.62154 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 32062b3d-6094-35d6-af47-b5c46f3c3ae9 | -7.33231 | -44.47082 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 402d61ae-0248-3574-b560-d533294623de | -6.22846 | -45.44204 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5971c434-cc95-3bf4-9bc3-8ebbec052053 | -5.75876 | -43.70588 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06f52200-6309-3735-8912-82becc2a2c86 | -7.53765 | -48.69365 | 2026-09-21 16:03:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 24c3e08f-ec9c-3950-8997-759edeb8a8bb | -6.87738 | -43.07198 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 596892eb-e80a-34bd-8cbb-e96094d9e870 | -6.15117 | -43.84263 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| baadaffb-3923-368d-9e2c-8579e2f76d1b | -7.6363 | -45.43106 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bb4bd982-3009-39f3-ae72-1b75decaac0d | -3.27907 | -42.91645 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c0b50e13-3287-366d-b262-73b712083907 | -4.81523 | -43.63305 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdf393bc-2fd4-3d46-9271-d2c397960f8b | -5.7354 | -43.72047 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 15d86695-e334-34bd-b8d3-78c30dce5e5e | -2.94823 | -51.04025 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 116dfab5-aac5-3b78-ba18-e54c2b9d7838 | -6.55519 | -45.53319 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1863e369-e0c1-3ac8-9048-1a93e494219d | -7.42439 | -44.73016 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 71266f4a-35e7-3b29-9535-82c539227852 | -3.84063 | -41.70842 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 24d2c7d8-ca9c-38d4-82e1-40f089d64efa | -5.04125 | -43.03418 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6663298d-641d-3868-a969-d33c8659508b | -6.56138 | -45.54242 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3314dfdf-3cca-31f3-ae5b-a3fd9a224609 | -3.61288 | -42.76363 | 2026-09-21 16:03:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 910fb7e0-d931-3134-8f72-3fa2ed5775f8 | -6.59884 | -45.87386 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06557fa9-71ad-3ae3-abea-101e05c6d4d8 | -6.98899 | -47.48182 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 25dc369e-7230-36db-9862-2bec7874dfcc | -6.98401 | -47.48638 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bf3ffad0-6538-3e6c-add5-a7ccb7127c83 | -6.38541 | -45.20062 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e436119-1f40-3c8e-8c25-9f2f8330d46b | -5.55071 | -45.69541 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 353bf1b8-bb7c-3962-956e-b691f5565ed6 | -6.66995 | -47.78168 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7446513a-908e-3448-b994-225c837ef956 | -7.13072 | -42.06837 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d892ca1e-4958-3856-a85d-dfe79731f55d | -7.42172 | -49.84583 | 2026-09-21 16:03:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e5d70cd8-25ac-3554-a93a-6d52ee7d2071 | -7.74761 | -46.71555 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d26278d-c11e-3f35-938b-cc38cb9da952 | -5.41855 | -42.95255 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 37116b42-0fc9-3f02-a972-a4338a1c7223 | -7.51664 | -45.4491 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| df5cbdf6-a838-3e76-8a84-48b6f400fd9e | -7.74145 | -49.3845 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f097e0b-b785-3ec7-836c-de18471d0dd2 | -6.21667 | -45.36064 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README171.md)
