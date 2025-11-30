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
| 1ba3bc4b-4960-35ad-9592-32cd84695f47 | -19.8675 | -57.7808 | 2025-11-30 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 13f4fcfe-f0ab-303d-ae7b-1feeacb5bce1 | -2.3464 | -45.5469 | 2025-11-30 01:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 106.7 |
| e148179c-425f-3ff5-b3bb-b1cdf9a90147 | -8.0321 | -43.1257 | 2025-11-30 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| d529fa95-ff5b-3ce8-ac5b-1df02de3303a | -19.8473 | -57.7835 | 2025-11-30 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 1338e083-ed78-3f99-96ab-80474b959ce0 | -12.0195 | -49.2659 | 2025-11-30 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2986d181-5f61-3c0d-b4b6-b24ff2d3521d | -2.6507 | -48.5414 | 2025-11-30 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 1c357443-7ba6-3621-a914-ffc1fb36865d | -8.051 | -43.1237 | 2025-11-30 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 0701447e-e511-32d9-93bb-4f9c54191fd3 | -8.1822 | -43.2034 | 2025-11-30 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 5fd4ad86-afe5-31d9-9b2f-b436ce89cd40 | -8.1822 | -43.2034 | 2025-11-30 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| b0d85f3c-a74f-3b65-8c4e-f5ec57069aea | -2.6507 | -48.5629 | 2025-11-30 01:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d189d6a4-6d2c-3056-9cf1-8ff8f1470209 | -5.7309 | -39.8286 | 2025-11-30 01:40:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 98f0e398-31a9-34fd-81a8-1f847ac14d78 | -2.3464 | -45.5469 | 2025-11-30 01:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| c129af02-65d8-300b-9a6f-38251aa35ecc | -12.0195 | -49.2659 | 2025-11-30 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c9b239c0-d953-3ea5-98e8-221fa58aba4f | -19.8473 | -57.7835 | 2025-11-30 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 01de71ff-b190-34c5-9b84-8ad1383551e2 | -8.1633 | -43.2055 | 2025-11-30 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 64dcd742-580a-36f2-a013-7724b3e4157e | -7.5014 | -37.4242 | 2025-11-30 01:40:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 62.0 |
| bf2b9f26-297f-3564-ad19-7f3b7fea75cf | -8.0321 | -43.1257 | 2025-11-30 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 92dc5cef-ea65-363e-b0de-0a661b563f60 | -12.0004 | -49.2683 | 2025-11-30 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 710156ef-ffec-3f61-9725-8ebbb4ee9cbd | -8.051 | -43.1237 | 2025-11-30 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 2e5ea5c6-cf94-3fdf-87c6-83410a5059c2 | -19.856001 | -57.7696 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ed2c9cf-e81b-3256-ae70-c4be1e04888c | -19.8634 | -57.757401 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b1970c08-8051-3bdb-889d-915802169759 | -19.868099 | -57.776501 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ee3df423-2475-3c14-99a6-84e97df41a8d | -19.8416 | -57.753101 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8eb62689-8c44-3381-8f0f-2848be035765 | -20.925699 | -56.354301 | 2025-11-30 01:44:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ad9062c4-aea8-38ac-be22-ef6194b76e18 | -19.843901 | -57.762699 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1cd2a427-e408-399c-8056-0a5fc57cb3c5 | -17.5098 | -57.140202 | 2025-11-30 01:44:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccf76b95-6c90-3d34-9c02-536c6e6a65ff | -19.8486 | -57.7817 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 886cc985-95e5-3000-8896-2b00a4ae114e | -20.928499 | -56.365299 | 2025-11-30 01:44:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7137cd0b-2ca0-3da2-bbd9-6678cf3b2ce9 | -19.865801 | -57.766998 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fca71bfb-b568-32bd-a578-71c46497d96d | -19.8536 | -57.759998 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8b3f1686-f417-3cb6-af4a-fc81ca12cfc8 | -17.507 | -57.1292 | 2025-11-30 01:44:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ede2bf7-c848-3359-83ce-f1090667061f | -19.858299 | -57.779099 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec24ac5a-6565-36e0-b772-a146f80102ea | -17.4918 | -57.1096 | 2025-11-30 01:44:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53b6f35b-30f1-3897-a76d-f4a384d36a76 | -17.4821 | -57.112301 | 2025-11-30 01:44:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 315af980-5854-359b-ac60-10e9a2e954e4 | -17.4848 | -57.123402 | 2025-11-30 01:44:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74012c3b-12eb-3798-8497-c5c44b3d2cdf | -19.8463 | -57.772202 | 2025-11-30 01:44:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0dd96d1c-0b0e-3ad5-8ac9-1fde3c55a28c | -19.8473 | -57.7835 | 2025-11-30 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 236.1 |
| c58ca7ea-d46c-3f15-a2ef-7f7d222bf79e | -7.5014 | -37.4242 | 2025-11-30 01:50:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 60.5 |
| d5718027-8d52-3867-8049-e3c864e1e190 | -8.1633 | -43.2055 | 2025-11-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| ef33422f-8a62-3b3c-86df-63171b4c9a62 | -12.0004 | -49.2683 | 2025-11-30 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 58c99485-53ca-313b-9b1c-ec3511a15c94 | -8.0321 | -43.1257 | 2025-11-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 6b1a31ec-0ad6-3111-9169-5904bf000df0 | -8.051 | -43.1237 | 2025-11-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| cbb89e0a-6df2-3de5-a81c-35e0d2c931b8 | -19.8477 | -57.7627 | 2025-11-30 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 03bacb88-fa28-3c90-b658-30b4f79cdcfc | -19.8675 | -57.7808 | 2025-11-30 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.5 |
| 9fb03850-0a90-36de-87f2-f169f8e16aa1 | -12.0195 | -49.2659 | 2025-11-30 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 63ee0ca1-5811-3eb4-9ccd-07508f3dbd63 | -4.3702 | -43.1741 | 2025-11-30 01:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c177f670-170c-3c39-be16-ebde84093c74 | -8.1822 | -43.2034 | 2025-11-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 1609bf6b-b8c1-3662-b272-3399ebe443b4 | -8.163 | -43.229 | 2025-11-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| cfcbf306-d6ec-3756-9d4f-cb63174581ed | -12.0004 | -49.2683 | 2025-11-30 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a7ba1ff3-141d-34b2-9772-b27712afa7c6 | -8.1633 | -43.2055 | 2025-11-30 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 81e69766-ce27-3dc8-b79a-14806d7713de | -19.8477 | -57.7627 | 2025-11-30 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 9a60f723-4098-369b-9c49-68fb16d9c8cd | -7.5014 | -37.4242 | 2025-11-30 02:00:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 8038a53a-d88a-3476-b032-c55add7a6c21 | -8.051 | -43.1237 | 2025-11-30 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 9c9ce4fb-54fc-33e7-ba3b-5472c89b15a8 | -12.0195 | -49.2659 | 2025-11-30 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 372ca849-b8be-384c-b1ab-aa453aeea070 | -19.8473 | -57.7835 | 2025-11-30 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 3599f31b-db21-396a-b127-d44d11d9f096 | -8.0321 | -43.1257 | 2025-11-30 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| aac335cc-b4cb-3689-b266-5eb20d9c3b61 | -8.163 | -43.229 | 2025-11-30 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| ed322f08-4275-34d1-b96a-dc25bc1b7461 | -19.8675 | -57.7808 | 2025-11-30 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.2 |
| 40d1c79c-2bdc-3321-8360-a6e8c588b7c7 | -7.5014 | -37.4242 | 2025-11-30 02:10:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 79.6 |
| e39382a6-2897-3188-a4b8-5b3801bf6f1f | -8.051 | -43.1237 | 2025-11-30 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| c12c9f47-0609-34ed-a033-f7d167b247f6 | -19.8473 | -57.7835 | 2025-11-30 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 3d273470-f2c4-3067-b276-edb10912ee4d | -19.8675 | -57.7808 | 2025-11-30 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| c5342532-65a4-3ac6-84ed-916e4e49bf87 | -8.1633 | -43.2055 | 2025-11-30 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| ca574408-cb84-3f06-a688-a00e275746b8 | -8.0321 | -43.1257 | 2025-11-30 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| fa68ccf2-529d-30da-92cc-7c40401e8e33 | -19.8477 | -57.7627 | 2025-11-30 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| f503caa5-7729-391a-89af-564599b4c078 | -8.163 | -43.229 | 2025-11-30 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 42a19339-bf4b-3bec-8f39-8e506a70bb5d | -12.0004 | -49.2683 | 2025-11-30 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0da08c58-76a5-37c9-8f9c-d04f43b95e72 | -12.0195 | -49.2659 | 2025-11-30 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8593f23a-f56e-3f04-98ab-6349e7816698 | -19.8477 | -57.7627 | 2025-11-30 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 6eab8424-8b1a-3774-800b-5bce0aba7388 | -8.051 | -43.1237 | 2025-11-30 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 84332f56-c71d-3e71-8a71-fef27fb87af8 | -12.0195 | -49.2659 | 2025-11-30 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d7d4c336-6638-3f90-be4a-6590c35a3c7e | -8.1822 | -43.2034 | 2025-11-30 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 9a70e9cb-a1f1-398b-9471-d4999a796e16 | -12.0004 | -49.2683 | 2025-11-30 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 901255ee-abfc-311b-9c15-538854c00c56 | -7.5014 | -37.4242 | 2025-11-30 02:20:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 103.5 |
| fca4694e-255e-3760-8cde-1e9adb0e3452 | -19.8473 | -57.7835 | 2025-11-30 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| f4b93e0e-7d50-3b7a-a619-0798509c162a | -3.0356 | -45.1193 | 2025-11-30 02:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d19ae03b-32d5-3ccc-bb54-843bc71b406c | -8.1633 | -43.2055 | 2025-11-30 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| f64bfbb1-45a3-3c64-aab8-111d5f64d4fb | -17.4951 | -57.1537 | 2025-11-30 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| c2939379-3d4e-3147-84ad-9bfde88325cb | -8.0321 | -43.1257 | 2025-11-30 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 98518189-c13a-367d-83a4-d11c3b1e0222 | -8.163 | -43.229 | 2025-11-30 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 6341122f-ba00-35c6-9705-4f76ac0e5c89 | -8.1633 | -43.2055 | 2025-11-30 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 385c5039-2a39-38e3-9f30-30e1a0266579 | -12.0004 | -49.2683 | 2025-11-30 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| b49573c2-9956-32bd-adb1-bd9d52859628 | -8.051 | -43.1237 | 2025-11-30 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 4e09b4e1-bfac-3217-aa65-13a39c8d6f37 | -8.1822 | -43.2034 | 2025-11-30 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 6cbf34f6-64c4-38ee-8a59-5fea70b9241b | -3.0356 | -45.1193 | 2025-11-30 02:30:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 214b1149-89df-3eb8-a60a-b606ab9598b7 | -19.8473 | -57.7835 | 2025-11-30 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 0bc12d15-a861-3654-8f3f-35aaeb449317 | -17.4954 | -57.133 | 2025-11-30 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| b23ff983-b1bd-3b7f-a3a4-444b922dacfb | -7.5014 | -37.4242 | 2025-11-30 02:30:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 233b4c7a-ff8a-3d1b-a135-f964e1e3f103 | -17.4951 | -57.1537 | 2025-11-30 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 099de794-512e-3ec0-b5ef-76bb24115c6c | -17.5148 | -57.1513 | 2025-11-30 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 3f9cc7ab-1417-3ffc-beb8-a85f07dd1f67 | -12.0195 | -49.2659 | 2025-11-30 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ffe9d3be-9669-3020-9ff9-89456a6c3f8c | -7.4824 | -37.4266 | 2025-11-30 02:30:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 8bf2429b-50d3-3b46-aca2-0e39a0f3c811 | -3.0356 | -45.1193 | 2025-11-30 02:40:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6934dbba-4f2f-3dfa-92c7-0f8ad6070a09 | -17.5148 | -57.1513 | 2025-11-30 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 8009c0ad-2355-3497-805f-2cffbf77ca59 | -7.5014 | -37.4242 | 2025-11-30 02:40:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 83.6 |
| a5270df4-022f-3434-99aa-8db631308bda | -19.8473 | -57.7835 | 2025-11-30 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 0cce1fa5-c6d8-3932-b574-a92bed317c38 | -8.1822 | -43.2034 | 2025-11-30 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| c9c7ed44-fe95-36bc-af81-7869e97aa44e | -12.0195 | -49.2659 | 2025-11-30 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7e105fde-ff63-3a74-8a44-82622910e26a | -19.8675 | -57.7808 | 2025-11-30 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 4bc4523b-7fa7-3162-b080-4e5df487b0fe | -8.1633 | -43.2055 | 2025-11-30 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |


[Clique aqui para ver as próximas entradas](README6.md)
