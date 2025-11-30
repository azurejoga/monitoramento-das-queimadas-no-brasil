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
| f181034e-1e1d-320b-af86-87654dc11227 | -17.4951 | -57.1537 | 2025-11-30 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| b026f0c1-e5a2-39a9-a9ec-5bbf227b58f1 | -8.0321 | -43.1257 | 2025-11-30 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| cbc4ff10-1389-3fd8-a203-bbf0a6b2159c | -8.051 | -43.1237 | 2025-11-30 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 0a623076-b41c-33cb-b357-a25ff9465125 | -12.0195 | -49.2659 | 2025-11-30 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 68ce87de-d09d-3946-8737-7477b3ee9494 | -19.8473 | -57.7835 | 2025-11-30 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 051fa099-a284-3ab6-a47d-55b653f12569 | -8.1633 | -43.2055 | 2025-11-30 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| d231f80b-907b-3b8b-8b85-c04bfb587267 | -8.163 | -43.229 | 2025-11-30 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 73b6fd8b-15ac-3d60-8b06-54850d12863d | -17.5148 | -57.1513 | 2025-11-30 02:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 59d53a5c-3392-3762-a72c-9ed149ccfc3d | -17.4951 | -57.1537 | 2025-11-30 02:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 56cc0c48-2e43-3fec-8f36-6f2b76d73c8e | -12.0004 | -49.2683 | 2025-11-30 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| aa20e0ee-b465-3c8f-af70-9e6b15ca1f94 | -19.8675 | -57.7808 | 2025-11-30 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 62ae5ed1-af62-38be-999d-cf1c5888224b | -12.0195 | -49.2659 | 2025-11-30 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b4c69d62-79c4-3d79-af5d-51d5b2b49d61 | -19.8473 | -57.7835 | 2025-11-30 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.1 |
| 48757508-5bc2-3bce-bf90-1435efa9aa8d | -8.1822 | -43.2034 | 2025-11-30 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 53ec0e7f-b465-35a1-bb8f-dec8c6775901 | -8.0321 | -43.1257 | 2025-11-30 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| f13e44f2-634f-3560-adcc-3992336d1db1 | -17.5148 | -57.1513 | 2025-11-30 03:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 88eb3a10-ae57-31ff-a284-ae1a79775696 | -12.0004 | -49.2683 | 2025-11-30 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5c5c0478-3bcb-3690-bf0c-1b8f32e40e67 | -8.1633 | -43.2055 | 2025-11-30 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 60fc3816-aaa2-3b9c-be55-3166c4c6b48d | -8.051 | -43.1237 | 2025-11-30 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 0e4d8e52-0097-3b76-b682-78c0551800d3 | -19.8675 | -57.7808 | 2025-11-30 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 274e48e2-e367-37dc-b01e-8aeff5fc1e7b | -7.46002 | -39.96627 | 2025-11-30 03:04:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8a2e93b3-7c0a-3e90-abb1-fe947aef83b4 | -7.49405 | -37.43868 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| b2a192ab-acc8-36f9-b7a3-df66ff6c6763 | -7.82864 | -35.46872 | 2025-11-30 03:04:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19191535-9985-3005-b14c-b2990a56589e | -7.49573 | -37.42954 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 23519857-1df8-38c4-bc5d-b113b098852c | -7.4949 | -37.43407 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 4c5697fd-59e8-30af-a2c5-da869e241921 | -7.32769 | -38.76735 | 2025-11-30 03:04:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 63ca705e-b1a3-3054-926e-7171bd207768 | -7.83408 | -35.46939 | 2025-11-30 03:04:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7e14e865-30ed-336a-bc4f-3078f58cc55e | -7.82802 | -35.47216 | 2025-11-30 03:04:00 | NOAA-20 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 837f9d76-e12d-3622-a3ac-0aa90f1f457b | -7.49524 | -37.42897 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 86669313-041f-3ee9-a27b-10beabdaae48 | -7.49438 | -37.43348 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 3c4ba718-35c8-3fde-affd-7c16934a1356 | -7.48876 | -37.43292 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 8ad1111f-116e-33ce-b629-7d24b7aeea5c | -7.49351 | -37.43805 | 2025-11-30 03:04:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 17.3 |
| d2ce96cd-f43f-3c89-bd0e-d7ef8cc0141f | -17.5148 | -57.1513 | 2025-11-30 03:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 173d0af8-59a6-3306-9cf6-70043b02e07a | -19.8473 | -57.7835 | 2025-11-30 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.2 |
| 2baea9ad-1e4b-3a6c-b03c-f4dbaec7fe1e | -12.0004 | -49.2683 | 2025-11-30 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5804886d-fa01-3757-bd52-3bebb1595943 | -17.4951 | -57.1537 | 2025-11-30 03:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 6590b639-51ff-302b-bed1-3e6c2fbbec7f | -19.8675 | -57.7808 | 2025-11-30 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 77410e80-e43c-3191-871f-28804ad0e2c3 | -8.163 | -43.229 | 2025-11-30 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| ebd3a1eb-18b5-3a42-9d27-0baafa6bcd72 | -8.1633 | -43.2055 | 2025-11-30 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| b111e82d-dffd-3f0b-a293-5f3beaa668c5 | -12.0195 | -49.2659 | 2025-11-30 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 655ac20d-ec8e-3a52-958c-041384e2ea3c | -12.0004 | -49.2683 | 2025-11-30 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b8f027b7-239b-3ef8-9875-aeae59ee5cc9 | -12.0195 | -49.2659 | 2025-11-30 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 59721be4-3cc8-3e1c-8ce1-3c0df3f192aa | -17.4951 | -57.1537 | 2025-11-30 03:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 2ab99dba-35bf-3b85-95b8-046896133d2d | -8.1822 | -43.2034 | 2025-11-30 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 22d067ab-2d7d-30ff-b957-522192af68d6 | -19.8675 | -57.7808 | 2025-11-30 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 92467145-d7f5-3048-84fb-2bb520e5ace9 | -8.1633 | -43.2055 | 2025-11-30 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 55f578de-4ed5-3081-a718-bc5f2930f60c | -8.051 | -43.1237 | 2025-11-30 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 26a80fdd-4c00-3c60-817d-eda28d54c20b | -17.5148 | -57.1513 | 2025-11-30 03:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| f8cf03d8-7726-3872-8bc7-985457da4375 | -19.8473 | -57.7835 | 2025-11-30 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| adf87a56-6872-35c5-9311-4c4e4f05d835 | -17.4951 | -57.1537 | 2025-11-30 03:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| f4b83810-8ed2-3c48-a6ce-431eab97891a | -8.163 | -43.229 | 2025-11-30 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 5ec0c51a-6499-3063-b675-144073807584 | -17.5148 | -57.1513 | 2025-11-30 03:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 192bebee-8225-3956-a9be-afcba56496a7 | -8.1633 | -43.2055 | 2025-11-30 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| b918ca61-e61f-3505-a85c-5fa7ab2c99a5 | -19.8675 | -57.7808 | 2025-11-30 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 92873551-39c6-3ee5-b882-78dd7c6abd01 | -12.0195 | -49.2659 | 2025-11-30 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e1cba25e-33d0-3e34-a0ca-80c76ff67086 | -12.0004 | -49.2683 | 2025-11-30 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 856c2c1f-db9b-3703-a1f0-50f133b39f51 | -19.8473 | -57.7835 | 2025-11-30 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 55553eb3-e261-3ca2-b19c-1fb05c6de630 | -8.1822 | -43.2034 | 2025-11-30 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 6085b5a2-6b26-3416-9293-fd3f099ad7d3 | -12.0195 | -49.2659 | 2025-11-30 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 27d19a2f-3ff7-3ca5-b0cc-9a2b211b9bf8 | -8.1633 | -43.2055 | 2025-11-30 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 0a6bd454-eedf-349f-8c57-9df30855614d | -19.8473 | -57.7835 | 2025-11-30 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| fda1e2d0-d555-3454-a7be-9eb4c3b61590 | -8.051 | -43.1237 | 2025-11-30 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 5dbcd393-53b5-3752-8090-02efa4fe1675 | -8.1822 | -43.2034 | 2025-11-30 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| c9b5a4ba-5972-3e29-8527-c921f5093694 | -19.8675 | -57.7808 | 2025-11-30 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 5ee0615a-9e4a-398c-98d7-365fae01a32b | -17.5148 | -57.1513 | 2025-11-30 03:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| b20d28bb-3b54-3838-a7f1-26a85df6b8b5 | -8.1822 | -43.2034 | 2025-11-30 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 6ea22187-5018-3ac9-b6b5-9cccf59ac18a | -8.1633 | -43.2055 | 2025-11-30 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| aef30d44-3e4e-36e2-aeda-5fa4528c1440 | -8.051 | -43.1237 | 2025-11-30 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| e468e5af-27b2-30ab-ae24-ec251ed59dc5 | -2.50847 | -49.09913 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b6057c8-d66d-3864-8b36-48185edaab4a | -2.63601 | -45.91808 | 2025-11-30 03:53:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b451db57-54bf-306f-adc4-3a10094a49fe | -2.64548 | -48.55086 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8f5116ef-076f-371e-b892-ba41759b8514 | -2.51133 | -49.09713 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0ee64f5-1782-3c87-bdeb-ac24a202a1c0 | -4.61164 | -45.21041 | 2025-11-30 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a542babf-928a-3220-97a2-d41f863ffbf3 | -4.60607 | -45.21487 | 2025-11-30 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39f3123-aeba-3f7b-a4cb-b6a515186b7e | -3.62607 | -42.75584 | 2025-11-30 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ca2a1c9-482f-312c-b409-20c6a7eab456 | -6.10331 | -40.36863 | 2025-11-30 03:53:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15ed4012-0a6f-3180-9460-05ab60cc0d4a | -6.29287 | -35.19637 | 2025-11-30 03:53:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 16a0570f-7fb7-3f46-aea0-20afd4e14711 | -3.43013 | -41.00456 | 2025-11-30 03:53:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7157193-2835-3738-b568-575d7f2f0eff | -6.87668 | -39.56554 | 2025-11-30 03:53:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4894aad0-6484-3315-9683-c3e5de07d4a0 | -2.21241 | -48.00375 | 2025-11-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4062ed21-70da-3f97-9906-c16072a2c4f4 | -2.44901 | -47.08028 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1cb5879c-fee7-3e62-82d0-818c68c9e72c | -2.90117 | -45.26781 | 2025-11-30 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce98ca57-5047-3c92-a8bc-21dec2decc2a | -3.54797 | -43.61569 | 2025-11-30 03:53:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 22099146-f095-3122-87fc-2c0fea7e09b6 | -4.80327 | -40.06455 | 2025-11-30 03:53:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ca9e139d-5ebe-3088-88ab-e661f9cb0ba1 | -2.70212 | -47.39538 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 945cfa49-b18d-39ad-a301-2872be6fb9eb | -7.16361 | -37.64949 | 2025-11-30 03:53:00 | NOAA-21 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3946551b-383e-34e7-b67a-5f24673bd825 | -7.33004 | -38.76057 | 2025-11-30 03:53:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 106e2eee-1594-38ac-81f2-8bb70c3ff3ad | -4.27118 | -40.67064 | 2025-11-30 03:53:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db07ff02-9bac-3b49-a29f-a2b1fdf756b7 | -4.27182 | -40.66665 | 2025-11-30 03:53:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c855192-297e-3068-9585-eda648c24a17 | -3.62664 | -42.75233 | 2025-11-30 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e3c3941-c832-3009-9c56-f26dabebe57f | -3.71333 | -39.54268 | 2025-11-30 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 276b1348-235c-347b-885f-2541ff49b30d | -3.21514 | -41.56697 | 2025-11-30 03:53:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 850a3f1b-ad3f-37e9-a713-a06122e4a4f9 | -2.51052 | -49.10208 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3775de59-9e2a-397e-b59b-bb8ab2132007 | -2.63264 | -48.55334 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86311343-377c-3fd0-ac4c-5926e5b04861 | -5.60402 | -40.82008 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 943cdcd6-780d-3131-bff9-02fa3993c7a3 | -5.97805 | -39.48023 | 2025-11-30 03:53:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 110582ed-0ee0-3e76-9701-330a2aa84812 | -3.89958 | -40.70136 | 2025-11-30 03:53:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 65c7cd39-a394-3fb7-bde2-c588c5b4470b | -2.60938 | -47.34011 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab126d30-470c-38b2-abfc-588d9c74452c | -3.84582 | -43.33356 | 2025-11-30 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ec61f3a-1ca5-38aa-8641-ef59394cd8d5 | -4.52266 | -44.75256 | 2025-11-30 03:53:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README7.md)
