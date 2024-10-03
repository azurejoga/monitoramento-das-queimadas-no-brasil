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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e36d31e-9566-3695-b9e0-f52dbe5dabe9 | -5.314 | -42.959 | 2024-10-03 00:11:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f97b0f6b-25b9-3d9f-b3b5-e6179ec17cff | -5.3155 | -42.965801 | 2024-10-03 00:11:47 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 61b6cabf-71c0-393c-8fb9-d1f79dfb9188 | -5.9667 | -46.276699 | 2024-10-03 00:11:48 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87f03ad6-01bd-3c7e-bb57-f01a3b35b000 | -5.9686 | -46.285599 | 2024-10-03 00:11:48 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bcc2ed0-6979-349f-8895-aa39fb3e1a9c | -6.1271 | -47.2505 | 2024-10-03 00:11:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d6e697-646a-3c91-b82f-661ac3f5a74d | -6.1293 | -47.2607 | 2024-10-03 00:11:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8004d4e-d8ce-32e8-aa09-fc95890d31d0 | -6.1173 | -47.252602 | 2024-10-03 00:11:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9a2607a-a4ed-3766-9768-7249ffe76214 | -6.1195 | -47.262798 | 2024-10-03 00:11:49 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7eab5317-9c46-384d-9960-b027f35d4d75 | -5.4954 | -44.602402 | 2024-10-03 00:11:50 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7ff0d37-4495-3cb6-846d-ae46002a21fb | -5.4971 | -44.609798 | 2024-10-03 00:11:50 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abc00762-626f-3589-8c6f-fd0a5e8ff266 | -5.8414 | -46.220001 | 2024-10-03 00:11:50 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 361f5b99-92a0-3d1b-96ab-93ab224f1537 | -5.8433 | -46.228901 | 2024-10-03 00:11:50 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c897490-e7de-33ff-8d36-eba09dc559da | -5.2424 | -43.788898 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea9160ba-dcf7-354d-8935-616af8a7eed6 | -5.2439 | -43.795898 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf7ba291-2532-3ae2-a9fe-2fd61dc37332 | -5.2455 | -43.802898 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76f88164-fe76-3a21-8116-f300eee30b3a | -5.2326 | -43.7911 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb93608f-e756-35d5-840d-e9fe23f66335 | -5.2341 | -43.7981 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f21677e-8dff-3dca-8c85-815ca949279c | -5.2357 | -43.805099 | 2024-10-03 00:11:51 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 354de46f-3c1c-381a-930c-b137addf3b23 | -5.1056 | -43.315498 | 2024-10-03 00:11:52 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94e7fb2f-4dc8-36d0-b7aa-235d142bda02 | -5.1071 | -43.322399 | 2024-10-03 00:11:52 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76e387ab-e2a2-3261-9c21-464a788f6b2e | -5.7963 | -46.435902 | 2024-10-03 00:11:52 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fad1b4d2-1e6d-32d4-983b-e30ee84b5144 | -5.1995 | -44.520199 | 2024-10-03 00:11:54 | METOP-B | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 063fc85e-e6b7-3d6b-b5f9-44721206717f | -4.8392 | -42.863201 | 2024-10-03 00:11:54 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7c3c572a-2beb-3571-b59f-70bdc1cb149a | -4.8407 | -42.870098 | 2024-10-03 00:11:54 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8cb511-a6f5-3554-b725-288772d3a5f0 | -4.8423 | -42.8769 | 2024-10-03 00:11:54 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b74b2e39-6182-3d52-85b0-abc45818d0c3 | -5.5944 | -46.356998 | 2024-10-03 00:11:55 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bea79cc-6058-3a8d-8c59-4f1a9fe42501 | -5.5963 | -46.366001 | 2024-10-03 00:11:55 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e09ef115-8295-38e0-adb5-34266006e0b2 | -4.9384 | -43.672501 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 935dbb21-4284-39d2-92f2-24f2e090a42e | -4.9277 | -43.762699 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 963d48b5-cbb0-3adb-85cb-f08950d0dc83 | -4.9293 | -43.769699 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aab44d44-20b3-30b9-90f5-1243be21ccab | -4.9308 | -43.776699 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b11520a4-ce59-370b-8259-868cc894a96b | -4.9179 | -43.7649 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40a22b0f-8122-38a3-895f-7aeb4fdd0280 | -4.9195 | -43.7719 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d4c4c4-a3a8-364e-82ad-e3c0655c3cf0 | -4.921 | -43.7789 | 2024-10-03 00:11:56 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf9cdfc6-4d87-3042-8da8-a56b92985acc | -4.6888 | -42.652802 | 2024-10-03 00:11:56 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 32aa65b4-db2c-3f88-8f80-2244fdf4f627 | -4.6903 | -42.659599 | 2024-10-03 00:11:56 | METOP-B | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e73ba81-d69f-388e-8695-8f3a52d129a7 | -6.4757 | -51.476398 | 2024-10-03 00:11:58 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f194ed-9dfe-3e3a-b6e5-90d161756711 | -5.4628 | -47.068802 | 2024-10-03 00:11:59 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44006e1f-46b5-3cde-8596-7e04e1b41f5c | -5.4649 | -47.078499 | 2024-10-03 00:11:59 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af82ca61-92c9-3e55-8e1d-348e486434c1 | -5.4551 | -47.080601 | 2024-10-03 00:11:59 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf322d3-80f1-3579-aebb-4077b0661a31 | -4.657 | -43.749298 | 2024-10-03 00:12:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fea6532b-ea32-3f55-bf02-9aa603084a57 | -4.6586 | -43.756199 | 2024-10-03 00:12:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eff9360-336f-3f80-88a9-8ed7f43176c8 | -5.3524 | -46.704399 | 2024-10-03 00:12:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2c10cb-2c04-340a-90b8-9c909a28f46c | -5.3545 | -46.713699 | 2024-10-03 00:12:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 531de10c-48c9-3ad0-9dcb-523c79077ba1 | -5.3447 | -46.715801 | 2024-10-03 00:12:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f390dcf-d2a1-3dd2-83d1-ee20400596f3 | -5.4257 | -47.086899 | 2024-10-03 00:12:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b480eb73-7494-33db-8130-a76f2440bcd3 | -5.3393 | -46.785198 | 2024-10-03 00:12:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2094e693-017b-3ac7-a6ee-26a0350a242f | -5.3414 | -46.794601 | 2024-10-03 00:12:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee5091a5-eb3f-3450-a4fd-ebe3d35b8134 | -4.4706 | -42.873402 | 2024-10-03 00:12:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 402273e2-5c41-34c8-b897-2773012dda9d | -4.4722 | -42.880299 | 2024-10-03 00:12:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6480e4d8-8f8e-3612-af47-9b1c46005060 | -4.4593 | -42.868801 | 2024-10-03 00:12:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2aee0631-ecd6-3a7c-82bf-2e1d7bcf02df | -4.4608 | -42.875599 | 2024-10-03 00:12:00 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a82bf1d-6b36-3b8a-8fd3-fb98c7205882 | -4.4624 | -42.8825 | 2024-10-03 00:12:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6778950f-39a3-30aa-add3-2e0c2570dfe8 | -4.4639 | -42.889301 | 2024-10-03 00:12:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5275f436-a431-3703-9547-ca1d1870781c | -4.4221 | -42.841202 | 2024-10-03 00:12:01 | METOP-B | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e38b805-09a6-3812-af5a-68a9f08739cd | -4.4344 | -42.895802 | 2024-10-03 00:12:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfee39fb-1e28-3cd7-82f6-7fdc06c6768e | -4.436 | -42.902699 | 2024-10-03 00:12:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 437d261e-7641-3429-b7de-c815ba76a31c | -4.4246 | -42.897999 | 2024-10-03 00:12:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e29b33b2-cf12-38d0-a53f-9329f5896ac7 | -4.4262 | -42.9048 | 2024-10-03 00:12:01 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0f26f37-0301-3a6a-980a-014a05cd381f | -4.5335 | -43.2906 | 2024-10-03 00:12:01 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9b0020-503f-39d0-b24f-d1d9c8a8dd85 | -4.5351 | -43.297401 | 2024-10-03 00:12:01 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5ae91f1-9234-3c37-8e7f-60433659e097 | -4.5366 | -43.304298 | 2024-10-03 00:12:01 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bbc97a6-bda0-3806-b19e-5b15969428a3 | -4.5382 | -43.311199 | 2024-10-03 00:12:01 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5082e28a-8ebc-3383-9d98-3a571beea0b4 | -5.0398 | -45.795799 | 2024-10-03 00:12:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 348befc7-276e-3ae1-a99f-a1593fa2202a | -5.0417 | -45.804001 | 2024-10-03 00:12:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c28851a-d610-3a0e-a0d9-ffd5f522f585 | -5.2409 | -46.7575 | 2024-10-03 00:12:02 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93cf10ec-26be-3585-8c9c-58d7c6fdf290 | -5.0867 | -46.101501 | 2024-10-03 00:12:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f75a47a-fc8c-3d76-8418-7bc78c1db0c1 | -5.0886 | -46.110001 | 2024-10-03 00:12:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9190bb-d96f-3f65-81a4-d0d2fc0b6db7 | -5.2312 | -46.759602 | 2024-10-03 00:12:02 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2f0bb09-ba21-3603-89fb-fc431c35288a | -5.0788 | -46.112099 | 2024-10-03 00:12:02 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d7468a2-70a9-3452-ad26-cb99c7c44112 | -3.8495 | -40.771 | 2024-10-03 00:12:03 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e9749e0c-534f-3a24-acb7-cb178c40b62b | -3.8512 | -40.7785 | 2024-10-03 00:12:03 | METOP-B | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 131ae954-dce2-3177-b3ea-6746215e596a | -4.7508 | -45.371498 | 2024-10-03 00:12:05 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f891dbc-d114-3f82-bcfe-894bee89bbee | -4.7526 | -45.379398 | 2024-10-03 00:12:05 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae301172-4eee-3ed0-91ed-d201bd180c95 | -4.7543 | -45.387199 | 2024-10-03 00:12:05 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e04ebc3e-5156-3e41-a4ac-ba6e44dc8586 | -5.2204 | -47.9314 | 2024-10-03 00:12:06 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee3d4fd-f445-30b5-b73c-da00a8d69050 | -5.2227 | -47.942402 | 2024-10-03 00:12:06 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eee02953-3d68-34f2-9243-9d51a5460ad5 | -4.7739 | -45.940201 | 2024-10-03 00:12:06 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d67a9c99-83a6-3cd2-8c29-0c475eed1cf6 | -5.2106 | -47.933498 | 2024-10-03 00:12:06 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf4dd568-9f5c-3e5c-84be-20b27cdcbe27 | -5.2129 | -47.9445 | 2024-10-03 00:12:06 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32a8624c-b376-3770-a934-08be07f01358 | -4.6772 | -45.874599 | 2024-10-03 00:12:08 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52f5eaee-c62c-38f5-8170-3b59047f562f | -4.679 | -45.882801 | 2024-10-03 00:12:08 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 970c2e22-0496-3d8a-888a-2351f6f51766 | -4.9193 | -47.114601 | 2024-10-03 00:12:08 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcbdadfb-d7b7-33f3-9ea9-4408cd33fd51 | -4.9214 | -47.124298 | 2024-10-03 00:12:08 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11534746-15dc-3f8b-a9bc-d339f5b13658 | -4.9235 | -47.133999 | 2024-10-03 00:12:08 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7357bb-8bf0-3698-9829-e8a9ebee5323 | -4.0143 | -43.225899 | 2024-10-03 00:12:09 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ee06d3c-825d-3b8d-ac26-06f25c9cdf37 | -4.0159 | -43.2328 | 2024-10-03 00:12:09 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26ee73db-6ea1-3684-aab6-1d435b8aa99e | -4.6901 | -46.818298 | 2024-10-03 00:12:11 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32ef2d76-b422-398d-8b9e-b9d54298af1e | -4.6803 | -46.8204 | 2024-10-03 00:12:11 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 921401a2-74c7-3abe-92d4-0880a3f75077 | -4.4714 | -45.919399 | 2024-10-03 00:12:11 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60810299-8aa3-340d-bca3-5a77d021c0e7 | -4.0946 | -44.5947 | 2024-10-03 00:12:13 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab513b0d-e7f6-338d-a7c5-7aa32f9222a1 | -4.0962 | -44.602001 | 2024-10-03 00:12:13 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a014a58-1850-301d-baae-0aa1e875d71f | -4.488 | -46.366501 | 2024-10-03 00:12:13 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d36406f2-7926-3e42-839c-d87cd5581d89 | -4.4918 | -46.383801 | 2024-10-03 00:12:13 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb3298b-91a4-3ee4-a5e5-8df7b170297b | -4.6478 | -47.4198 | 2024-10-03 00:12:14 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3baca8a-ebc8-32f3-832b-14239202c216 | -4.65 | -47.429798 | 2024-10-03 00:12:14 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d93c52d9-5362-38e8-b25c-789c69218237 | -4.1119 | -45.3647 | 2024-10-03 00:12:15 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa4ca60-fc0b-3237-a4d3-726b1fbcf1f3 | -5.0541 | -49.759602 | 2024-10-03 00:12:15 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b9b47c-242b-322e-9c66-a170b0afc025 | -5.0573 | -49.774101 | 2024-10-03 00:12:15 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08aa980a-479c-3cdc-970a-4dbf8fbe1444 | -3.3952 | -42.263802 | 2024-10-03 00:12:15 | METOP-B | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
