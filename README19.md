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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77fdeceb-d88e-35d0-8d18-5264b26129b3 | -3.2174 | -50.139 | 2025-12-01 05:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 81ca6a6c-4588-363c-bf12-6d3ef0207185 | -4.3877 | -43.3362 | 2025-12-01 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| ee6778cd-b49d-3550-a4cd-c64b41a54427 | -4.3879 | -43.3129 | 2025-12-01 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2321120e-ea9c-358c-8927-f554fdbbc25d | -5.3398 | -43.5535 | 2025-12-01 05:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f7ec84a7-4154-3f13-9d3d-2380a5216da6 | -4.389 | -43.1497 | 2025-12-01 05:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 821e08e3-6b4e-3850-9e3d-79c7a068a1b4 | -20.19028 | -50.69892 | 2025-12-01 05:20:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| cb4b9cb7-1972-38f4-a739-3edda3ea494f | -20.02623 | -57.45552 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 10f82785-1eb1-3918-8b99-3a637cc791e2 | -19.97166 | -57.38269 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2ca3f0f3-9cb5-3eb6-9747-9c3a13842e3b | -20.0328 | -57.43542 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| de63365c-08c7-3ef3-bc1a-10df3b75df70 | -19.97488 | -57.38846 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5d3b7aec-ea32-3a2d-bc7e-57709210b354 | -20.19422 | -50.69462 | 2025-12-01 05:20:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 5099ed32-fdea-3ba0-aaff-d2cfe996110c | -19.96775 | -57.38211 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e903e85b-b4a1-3731-8ded-6368d4f0d964 | -20.02891 | -57.43484 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cf2d7d51-7aff-32e5-9559-05ebf771a09f | -19.96722 | -57.45201 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5d240e66-1037-34e6-852c-c8c89a6c69c2 | -15.27537 | -60.41038 | 2025-12-01 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9e77cf9-2747-39b6-bc57-9da2fcbc53e2 | -20.02757 | -57.44519 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 365f22c2-170c-349e-8abc-93d0fade30dd | -20.03213 | -57.44059 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 98036a36-22ff-308f-ac6a-de67ad7ee732 | -19.97878 | -57.38905 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| be918880-f6c2-31c8-b8af-7bc2821db1b8 | -19.97893 | -57.39038 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0cbf1140-7998-3a18-b0ac-d324281dcb8e | -19.98291 | -57.44771 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 44076bdf-411c-3c4d-b3a2-197c1ea77360 | -20.19378 | -50.69921 | 2025-12-01 05:20:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 92c19ece-a758-3502-a57f-9cd9a9b5ea34 | -20.02568 | -57.42909 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c5eff1d7-7e39-37b4-8072-b81d19005c48 | -19.9462 | -57.39482 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8bdadf19-baf2-3403-b045-9fd7ab8f8b54 | -19.98343 | -57.44916 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0c7e1f48-7009-3c8f-9954-5464a6ee6d2f | -15.42371 | -52.19324 | 2025-12-01 05:20:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be34bb58-1bcf-35ad-8e71-5b96ef6e8e43 | -20.19068 | -50.69429 | 2025-12-01 05:20:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 40595e22-dfeb-303d-bcc5-5e70e84a77d8 | -20.02111 | -57.43368 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 8fddf94b-a8da-37a8-98aa-561c851f2564 | -20.01788 | -57.42792 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d5694d1d-68d0-358a-b94f-6be54232fbdd | -20.02178 | -57.4285 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| e8874e7b-c143-326a-96c9-94fc341596ef | -19.9423 | -57.39425 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4d885d10-95d2-3517-bc65-e0afe84edbd1 | -18.13752 | -48.53733 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 65ea9bea-c0c8-3886-ad20-04589da6e4fd | -19.97029 | -57.39309 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7e5502cb-225e-3dc2-a894-fae0bdc33d99 | -15.42409 | -52.19007 | 2025-12-01 05:20:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa7ab9be-ac62-3c66-96c3-225ec80d2dd1 | -19.97568 | -57.38459 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b40df04-b2bf-3b82-bcb1-53c141e7642e | -18.13083 | -48.53678 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 28cd4bc3-4202-3b88-9a9c-830690eca8e1 | -19.93638 | -57.40921 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 452a7853-ab98-31ee-9102-f092d0833093 | -20.03146 | -57.44577 | 2025-12-01 05:20:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| e18a8bde-2160-3730-9e4e-db866c4d7645 | -21.19823 | -56.93354 | 2025-12-01 05:22:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9799cda-5d0a-3ce7-b0a6-e8c85e925c18 | -2.7377 | -45.2201 | 2025-12-01 05:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7ab0d237-cf33-33d5-970e-3a0c8c1fe1b0 | -4.3703 | -43.1508 | 2025-12-01 05:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| bac49719-94d8-3b2f-8c03-07af36db3bad | -4.4064 | -43.3351 | 2025-12-01 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a786a0de-7a03-34f4-899b-43050b91e40f | -5.3396 | -43.5768 | 2025-12-01 05:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| cc48d511-5c2e-3614-b3a4-2c793ec3083e | -4.3877 | -43.3362 | 2025-12-01 05:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e51dd350-fec9-34c2-b867-2d0933759ab9 | -5.3398 | -43.5535 | 2025-12-01 05:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 36479322-fed8-3d0b-9203-d45b4b1043b6 | -4.389 | -43.1497 | 2025-12-01 05:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a1967eed-b30d-3d84-9a5b-54430b76e384 | -4.3703 | -43.1508 | 2025-12-01 05:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 64c10a0c-b4eb-3494-9d3d-23a50f88aff8 | -2.7378 | -45.1976 | 2025-12-01 05:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ce3d6f21-cd20-3ebe-b554-7955e6c17a96 | -4.389 | -43.1497 | 2025-12-01 05:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 94a32d80-b413-31c7-be48-e986e660ad86 | -4.3877 | -43.3362 | 2025-12-01 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5cdc238b-90e0-38d0-9bb1-8c90e1b3bebd | -4.3879 | -43.3129 | 2025-12-01 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b8b1d59d-f249-3d1d-973e-f080160acd82 | -2.7377 | -45.2201 | 2025-12-01 05:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 7ac58fd5-b7ff-34c4-b12f-d93b02797351 | -4.4064 | -43.3351 | 2025-12-01 05:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0d4dbff0-d3bb-3cc6-9ae3-72afdfa4bea4 | -2.04498 | -52.10624 | 2025-12-01 05:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 786343f8-b3e0-37dc-9e46-fd9d1a89216d | -2.936 | -53.27462 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 295a87e8-0e78-33c0-9110-e1605aeff630 | -2.93404 | -53.28777 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bfcf66-518e-3a1b-8a2c-50f922c4143a | -3.47701 | -51.37047 | 2025-12-01 05:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fff190eb-e2b8-3197-b848-69419119a7f6 | -2.94089 | -53.28411 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b194a86-cd2a-38bd-a4ec-3a6c4218f9af | -3.47796 | -51.36376 | 2025-12-01 05:46:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39abcfbd-8309-36e7-b181-a11882199192 | -2.93468 | -53.28342 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36291b20-b98c-3672-a39b-0704657005ae | -2.94022 | -53.28859 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f1eaf44-ed73-3737-9a49-ed802adc18e8 | -2.93533 | -53.27909 | 2025-12-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e28c973-10dd-32ad-8119-d6084cd2aac8 | -4.3877 | -43.3362 | 2025-12-01 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c0457923-066d-37ae-b0b5-e4306b7dc09b | -2.7377 | -45.2201 | 2025-12-01 05:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 25afac56-33c6-3155-80f3-a0179b52083a | -4.389 | -43.1497 | 2025-12-01 05:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a99f2645-9e7a-30bc-afda-42daf6480d79 | -4.3879 | -43.3129 | 2025-12-01 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3d83e1bf-c3f1-3848-bb48-e77bb3f359f7 | -4.4064 | -43.3351 | 2025-12-01 05:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fa945ac1-6153-3e87-a7d0-3da39fa4f204 | -4.3703 | -43.1508 | 2025-12-01 05:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ea7111e6-1ce0-38ad-8895-0775205ef355 | -20.03178 | -57.43653 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b9f9777b-86f9-33e5-9057-f8bffbe22e25 | -20.02794 | -57.43142 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ee25c7d-f033-3d9c-989f-e8e4a8ed032a | -20.03219 | -57.43208 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fd72529b-a21a-3253-8dea-a02735f80c35 | -19.9676 | -57.3751 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c5b2dc83-4052-33f1-b41b-534a86cc5afc | -20.02661 | -57.44474 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f1eb438f-372e-3a06-9398-081c466f0574 | -20.03137 | -57.44099 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff4c323a-8695-3d85-b58d-f4385c142cf8 | -20.02749 | -57.43585 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4d2d34d0-57d2-38bb-9253-1863bdbf6493 | -20.03296 | -57.44094 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7d8761d9-fb5c-33de-b61b-1a19d09730ff | -20.02246 | -57.42633 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 93d8ffd4-0189-3289-a8c2-e48ac8bbbc19 | -20.03096 | -57.44545 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dfb7f7ec-e4ce-30c0-8d2c-83c35df66d5b | -20.02546 | -57.44034 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 079ae048-ccbd-3fa2-bf8c-70dc717a774d | -20.02078 | -57.42632 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 212362a0-f803-386e-a9b1-68ec14f677ee | -20.02202 | -57.43076 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d351bc13-a7c5-3c91-8b38-17a1c4e76272 | -20.02705 | -57.44031 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 880cd7d5-094b-3e2a-adad-95643d01683c | -20.0334 | -57.4365 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1a8c30fa-bbe6-306a-ab53-40474a0f6f1a | -19.97267 | -57.38472 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b0af73cd-de5e-30dd-89da-e8103ea22ddd | -20.03251 | -57.44538 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c56b31db-559b-3b77-9053-fe9b3964ec52 | -20.02423 | -57.45367 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7eef9ad7-00cd-3bcf-858b-eedd3822f871 | -20.02573 | -57.45361 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e6606d57-d95a-328f-89a1-563ca46faa05 | -19.9731 | -57.38024 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 44ea22b2-2350-37ba-867c-b0e0c49dbf1c | -20.02037 | -57.43076 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 63db863b-e481-3f39-9f82-c75d6207a05f | -19.96717 | -57.37959 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e930aa38-0eea-3b6f-9fb2-018e44410b29 | -20.02505 | -57.44479 | 2025-12-01 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8c6359de-17d5-354a-8f9b-5168d2c5d7f1 | -4.3877 | -43.3362 | 2025-12-01 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d226aec2-5e5e-375b-9221-bb27933aca4c | -4.3879 | -43.3129 | 2025-12-01 06:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8d7c3e16-bacf-3796-8de8-945d731fd227 | -2.7377 | -45.2201 | 2025-12-01 06:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 96318ff7-170c-358c-ba31-a8eff361dbe7 | -4.3703 | -43.1508 | 2025-12-01 06:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0af676fd-3eb4-38ca-ab70-67caf56de994 | -4.389 | -43.1497 | 2025-12-01 06:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c8f0fc40-8c6e-38a1-943f-cffd8834d64b | -4.3703 | -43.1508 | 2025-12-01 06:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c31407b5-afa3-33de-b2b9-890d552e2997 | -4.3877 | -43.3362 | 2025-12-01 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 81386296-a752-3df1-8e5d-fdb200eb096f | -4.3879 | -43.3129 | 2025-12-01 06:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8ec64029-1137-37e0-ac12-873ce42f4b36 | -4.389 | -43.1497 | 2025-12-01 06:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 21d661ea-e092-3dd3-b347-08381299b26b | -4.3877 | -43.3362 | 2025-12-01 06:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |


[Clique aqui para ver as próximas entradas](README20.md)
