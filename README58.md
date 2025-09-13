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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d11bb19-522c-3c06-b524-3aec9a8fa49e | -10.65192 | -46.27737 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59243d8d-7ddf-3690-a56c-0513a74f4582 | -10.69999 | -48.65709 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cff260a-5fff-36ce-b101-2909cb18695b | -10.7893 | -50.54651 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b545c795-6d00-304e-874a-7ae2dc57cf19 | -14.44776 | -47.34426 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da58510-65a2-3951-9a64-e0e92fcb0b73 | -10.50868 | -51.55372 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 581cac8c-c221-3c7e-96f8-4a1be6ac237e | -9.98034 | -51.71696 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ef25e10-5f3b-3444-97b4-459d5f8071c1 | -11.61326 | -46.61224 | 2025-09-13 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a46b7c9-4c08-396a-8649-072af5a86833 | -14.4155 | -46.40356 | 2025-09-13 04:08:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e17b1c03-24b5-346e-8714-19e93204af31 | -12.94126 | -47.99908 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 56c2ec2b-5a12-380d-bab5-7821c8efd7d2 | -11.86555 | -50.58007 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| eca91b26-32d1-31e9-a550-fe1d39c97769 | -9.00996 | -45.76484 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbc3316e-1fc3-3590-91bb-823db6b933b6 | -11.73295 | -44.21789 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6454776-cb9c-3265-98fb-1c75f7076d5c | -10.64914 | -48.97498 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92ee0901-a068-3589-9be7-653e0a52d9eb | -11.73414 | -44.21056 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6008f8ea-0772-3acf-995c-ee85c7197afb | -8.74836 | -44.2304 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec8536cb-7bee-3645-b24b-47537275b849 | -13.91173 | -48.28046 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c81b483-7522-3b99-9d7a-f157da891c4f | -10.32937 | -48.81342 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a69ef964-e21c-3317-8eff-f034626b04f6 | -12.82955 | -47.92337 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66535929-6919-3962-8018-99e174fa6d76 | -14.12867 | -45.3749 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9016b85-bad1-3b5c-9111-5639c36aa705 | -10.45807 | -50.61119 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2428b38b-f737-3809-9e0b-c615037c375f | -10.36982 | -50.49947 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f03c440-17b2-3462-a883-213c2c9ba0ae | -11.73474 | -44.2069 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9b3e68c-83f4-3bd6-9250-337bfeda491d | -14.1883 | -46.28705 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf0ae8e0-2b92-3b02-8a7a-5cc1e7ae1513 | -12.08605 | -47.57302 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4f9babd-6db5-3798-9bb7-47db2928ce62 | -10.38312 | -50.49249 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8cf4814-99ec-3317-809e-e13277b7b8ba | -13.32037 | -44.63601 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6876359-d2c4-3865-8823-f5d652ad6900 | -10.15306 | -47.90451 | 2025-09-13 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d269b92-cbcd-36f7-b8c7-9a81acab2bdf | -14.1755 | -46.25486 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af2adf8a-e062-39cb-96bd-b8f3a31e0083 | -11.93441 | -51.1374 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c38313cf-6700-3ad9-ac68-8c6fc3460403 | -12.382 | -40.39649 | 2025-09-13 04:08:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7c16b54-f1d1-38c2-a6ee-5f3b70f7f3af | -11.56218 | -50.57605 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5ba453c-2953-34ed-aeb8-f72c756e84af | -14.46656 | -47.3473 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc16e8ca-57a5-3819-a008-54ab5c22bb4c | -8.50731 | -47.32313 | 2025-09-13 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 814296ae-fa9f-35ee-92f3-9c011b0b649e | -10.35309 | -50.50782 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a94dd2f-d6ad-37da-8446-cce9c0c73334 | -11.85893 | -50.56675 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 033af8a8-493f-38c8-ba20-fac712c9a19a | -10.45417 | -50.6045 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 453f49d5-a5da-35e8-83b0-262817463dee | -15.05173 | -42.24887 | 2025-09-13 04:08:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f98c9f43-d13a-3b09-bd32-b4197b4c6ab4 | -14.26711 | -45.07036 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ebb28dd-bdc5-3d9f-8294-644e7571d849 | -14.16282 | -46.2492 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d59dcf78-e546-3f10-8f15-ac3e49241c19 | -14.18904 | -46.28273 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e795262a-c78f-30f4-b498-d563297377e4 | -12.84849 | -47.93222 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db80b418-7b2a-35c0-a723-d28af566c381 | -9.9549 | -51.70477 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae2d0788-40b5-3c4f-a892-06dcaefae55f | -11.27908 | -51.13722 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44352bbd-f477-34d8-8943-b46fe665c55c | -10.69427 | -48.66437 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b555bd8-b12f-3a0d-b69b-0fbfa8c02b21 | -9.25641 | -51.24743 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c29e5b1-4bfa-3586-8a32-5a212bb60838 | -14.45907 | -47.3459 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 677d6a58-216c-3355-b240-f99e383b790c | -14.2224 | -46.28077 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a31f9980-6603-3fe5-9062-0141c88ac3d2 | -9.85015 | -43.14566 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ccc4aecf-e84f-3c25-8378-b2f6abdcc69b | -8.93907 | -46.72284 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76355a3c-d492-36e5-9df9-e7cd6968afcc | -8.09251 | -50.18732 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b72cf278-8a25-3a78-821a-fec6117586f7 | -11.18126 | -51.42282 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2058b403-eb79-3e41-89ce-220ae8d64599 | -9.97294 | -50.29799 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a7160f4c-db93-342d-adea-361987a882d1 | -10.32428 | -48.8166 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b8591742-8c36-3266-ad0f-9efdc71f8a5f | -12.11081 | -44.88531 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66720db8-3723-3308-a5c8-63573cde7dc8 | -12.09742 | -44.86412 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b4c56e2-8de5-3832-a4d7-b4672fb1b5a4 | -9.24608 | -51.24896 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b32b74b5-759f-3f20-a7b4-3bb384db6320 | -12.995 | -46.73883 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 379fb18b-736b-3d57-9c27-ab638652e0b2 | -13.00997 | -44.11522 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 840bd956-ee09-369e-ac08-ddd42bc25a54 | -9.5117 | -54.65424 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7e80b3a-2ad0-3ffc-ae31-782d430f7b46 | -9.50943 | -54.66575 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ae89a7-67d3-3e60-a76b-98ad80352ca3 | -11.71383 | -46.56405 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c54b860a-d331-3b1e-b210-aae09a86b836 | -10.36219 | -45.43005 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4939a363-95b9-3dc5-91ec-cc7838abbaf4 | -11.4505 | -43.571 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d74c597e-8dc9-3bca-b158-3f920669aade | -12.12596 | -44.83687 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 72d5cb51-52ad-3706-b19f-08db048ef2f4 | -11.40998 | -50.74547 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| deaabf34-5018-3835-bbde-3a3e523e6379 | -8.48652 | -45.14941 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 502cb5f8-8bbc-32fa-990c-cc31d95408fc | -10.70009 | -54.44265 | 2025-09-13 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4a1e415-29fd-39a7-80cc-5cf32d5dcf1e | -11.72909 | -46.61683 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a88d6bd-a858-3389-95a9-c1f6e5bb17cd | -12.9233 | -54.75253 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de7ba6fe-fd4a-3be7-94f9-b38fd5cb4c04 | -11.41342 | -43.65284 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d296c47-0b9c-3fe6-a55a-48c56b85a913 | -9.32556 | -48.94618 | 2025-09-13 04:08:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 182d9871-d9c5-3829-ad08-b0f99db9598b | -12.08146 | -44.89692 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1bd36ff5-10d6-394d-9e88-19261789c87f | -12.84758 | -47.9374 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 225d7cb7-3328-3cae-93ba-c648cf170628 | -14.19615 | -46.28411 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce7a76ed-1e43-3e5f-a49f-59b3094ba38a | -7.93979 | -46.90201 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e1e6df9-ec69-3b96-9ad7-1b86d31658d7 | -13.91436 | -48.21875 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f1e13ed-d459-3d83-862c-1fe984c24f75 | -9.80728 | -48.8981 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb6a73e4-b5d6-3d55-88d9-df6bff9bc506 | -10.5036 | -51.55173 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d84c8acf-bfe1-35c4-9751-e037dda5a680 | -11.13976 | -45.30954 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da804003-f79c-3074-9c4d-4612d36f3f6a | -14.44737 | -48.429 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1291e566-ac06-3057-a82c-8d65c7c7e87c | -10.69052 | -49.17471 | 2025-09-13 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef86f4b5-181f-3238-984d-6807f847c73c | -12.10273 | -47.58843 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cc8b91c-9da3-3160-96e6-f9547f7f88ab | -9.70391 | -47.53113 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25328c60-326d-34a5-96b8-8e249d8bb699 | -9.70358 | -47.52972 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aff7e420-03e9-33fc-9875-7b9f8931be32 | -10.78442 | -50.54556 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 53f04e59-d3db-3d0e-b1dd-ed9f228338af | -12.65656 | -44.23848 | 2025-09-13 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 494ea5b2-8113-330b-81c5-518cc9461c5d | -9.25766 | -51.2408 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80216a04-1bdd-31c9-b398-8263b2e4468e | -14.43216 | -47.32319 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbe9a94e-1974-39d3-b637-8f301257db09 | -12.92531 | -54.74282 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2a8e4e42-d539-35e9-91eb-10c71682ef09 | -10.76948 | -41.33444 | 2025-09-13 04:08:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2e25956-4a6d-3f48-9eb8-f7c784e4459f | -14.18833 | -46.24412 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89a19368-a2c9-3210-aae1-1983d641b957 | -14.14328 | -45.3933 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89cae514-8ed4-38eb-90af-1edb724130bc | -11.86177 | -50.57381 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 49a51c38-b363-35af-b7e9-0787156f89c0 | -13.47212 | -48.44843 | 2025-09-13 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32395809-dcd1-325b-bbfe-844ff49f1e98 | -8.09513 | -50.17265 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d939c97b-da55-356f-8f9e-d3295d9a0a5e | -12.95022 | -48.2554 | 2025-09-13 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15d262d8-89aa-3403-b1bd-15904963a076 | -11.48289 | -43.61952 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b8a1977-02f2-3054-9e29-a603ae1f01d9 | -10.78925 | -44.77509 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6b7520d-2801-3afd-b0be-4db4555e7d2c | -9.66761 | -47.54702 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c29316d-a095-36b9-9510-476d80fd61c1 | -8.08874 | -50.17952 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README59.md)
