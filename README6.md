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
| 9136afc7-860c-35b9-8066-508fab5a9943 | -8.9851 | -65.9232 | 2025-10-21 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6f2d5306-9e18-36a4-be8e-4c467cc86bb3 | -17.4135 | -55.0468 | 2025-10-21 02:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 412203ce-ff4c-3ebd-a316-6a7a44e8c7a9 | -3.5153 | -45.8411 | 2025-10-21 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| b4360621-61de-3e3d-acfd-7af2941f40ed | -3.4783 | -45.8203 | 2025-10-21 02:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 01a86dc0-8224-3d10-b0d9-bfce959b4e7f | -9.0036 | -65.9412 | 2025-10-21 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3d222ab2-0abc-3892-88d5-b9cf9a112b87 | -9.0036 | -65.9226 | 2025-10-21 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 4d380204-b2d5-3f08-95e9-761f4e1b333a | -17.4332 | -55.0441 | 2025-10-21 02:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| df9fd995-d9ea-3eeb-9868-fd3af5dd975d | -3.5153 | -45.8411 | 2025-10-21 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 116.6 |
| d8035039-6b92-3fda-a6ab-738f313ba0eb | 1.7119 | -55.7051 | 2025-10-21 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 22baa31c-e397-39ef-a610-03945c5adbe6 | -17.4135 | -55.0468 | 2025-10-21 02:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| e46858d0-88ff-3d6c-82ff-2056d258dd15 | -8.9851 | -65.9232 | 2025-10-21 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| cc946b81-8a22-358b-a484-7602d1cc4c50 | -3.5154 | -45.8187 | 2025-10-21 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 04ec872f-0562-3395-a488-3e3717055d17 | 1.7486 | -55.6651 | 2025-10-21 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 12b69aef-3c95-3bc0-ab58-5a0870182ea8 | -3.4967 | -45.8418 | 2025-10-21 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 4f8d8a23-c421-3f40-9eb2-b091b54765e8 | -3.4968 | -45.8195 | 2025-10-21 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 240.0 |
| 75dd1277-58bc-3bc3-b522-53100655a08e | -17.4131 | -55.0678 | 2025-10-21 02:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| fb47d123-7750-3905-9f3b-4e7e14eace18 | 1.7486 | -55.6849 | 2025-10-21 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5a4150e3-f780-3dab-8349-3fdc142eb5af | -9.0036 | -65.9226 | 2025-10-21 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| d9f38123-0fc1-3d06-9a7b-7431da99080c | -9.0036 | -65.9412 | 2025-10-21 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bbf10669-c9f7-315a-abec-f481c291fdcd | -3.4968 | -45.8195 | 2025-10-21 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 248.0 |
| 58097881-6943-308c-b593-034bb2413c28 | -3.4967 | -45.8418 | 2025-10-21 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 24f8ff3a-6cda-35d9-b4ac-ce026078381e | -9.0222 | -65.922 | 2025-10-21 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 547aa0e9-43f8-3f40-aacc-aeedd939be3e | -8.9851 | -65.9232 | 2025-10-21 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bfd8855a-01f4-368a-a9a0-6b09d1665f4b | -3.5153 | -45.8411 | 2025-10-21 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 0ad9251d-af98-3913-bb8f-6e85b94ecfcc | -17.4332 | -55.0441 | 2025-10-21 03:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 14df7dd4-4694-3437-8f79-37df1dd45bbb | -17.4131 | -55.0678 | 2025-10-21 03:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| bf48806a-e7f2-3dd9-b404-89563d6793b2 | -17.4135 | -55.0468 | 2025-10-21 03:00:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 137.6 |
| b878a213-b0ae-3f75-9e0d-68ca8c8a81f7 | -3.5154 | -45.8187 | 2025-10-21 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 5afed400-562c-3de2-bc99-8387c819c722 | -6.25814 | -35.19449 | 2025-10-21 03:04:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 251e6b07-12a6-3459-87a3-af989b3c8453 | -6.9409 | -35.06176 | 2025-10-21 03:04:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b83057ef-2639-3a5c-bd36-622b83b06847 | -6.94029 | -35.0652 | 2025-10-21 03:04:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3172e231-e726-3d3b-8524-84f95c60d1dc | 1.7486 | -55.6849 | 2025-10-21 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 378a68c4-5e7b-3762-83b4-72e5612a8e21 | -17.4332 | -55.0441 | 2025-10-21 03:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| b5b6a23f-78f6-3aed-8f6c-1664f2eb004f | -9.0036 | -65.9412 | 2025-10-21 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 90826919-f585-32e5-81e4-deb39d07180b | -17.4135 | -55.0468 | 2025-10-21 03:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 133.7 |
| c8908281-5a3b-3305-96c9-93b9b4c2d597 | -3.4967 | -45.8418 | 2025-10-21 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 495077e3-955a-37af-944a-bd0ead083fa4 | -3.4968 | -45.8195 | 2025-10-21 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 222.9 |
| ef4b8467-b007-39fe-8417-322e49168dcb | -9.0036 | -65.9226 | 2025-10-21 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 22c9f186-8028-3dbf-b843-bb2c7931750e | -3.5153 | -45.8411 | 2025-10-21 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 876d316b-733d-3c63-89bc-cda3c063d654 | 1.7486 | -55.6651 | 2025-10-21 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9dee9caa-10e5-3a06-adcc-1d98c99b909d | -17.4131 | -55.0678 | 2025-10-21 03:10:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 272c5cf0-08d9-3563-909b-0c3e63809d7c | -9.0222 | -65.922 | 2025-10-21 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3f8b92f1-0900-34c2-973f-cd477844fa3d | -3.5154 | -45.8187 | 2025-10-21 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 181.6 |
| fa8b6db5-68b9-3eb8-b63a-ee57fcf71f24 | -9.0036 | -65.9226 | 2025-10-21 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6b4d6882-d1be-38bf-b166-6e2f13d68293 | -19.0918 | -57.5304 | 2025-10-21 03:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 2928bdf1-1ef9-36da-a439-d3b09f4f5f3d | -19.0915 | -57.5512 | 2025-10-21 03:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| acf14cc7-3967-3c8e-bd7e-eab8982e3a19 | -17.4332 | -55.0441 | 2025-10-21 03:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 8c6be5e8-51ae-31b7-af91-7db255235a38 | -17.4131 | -55.0678 | 2025-10-21 03:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| eedc8844-af16-35b3-9f48-775cda93984d | -3.5153 | -45.8411 | 2025-10-21 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 29fa8b9b-3a25-3e01-aeca-4ce7e1ce0049 | -3.4968 | -45.8195 | 2025-10-21 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 883e004b-d786-34dc-a060-43367c298bcc | -9.0036 | -65.9412 | 2025-10-21 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 4c079648-c55f-3dc7-adf3-9caecee472f6 | -3.4967 | -45.8418 | 2025-10-21 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 963448e6-3a8a-3fb9-b2ec-2ef0c85e33b8 | -3.5154 | -45.8187 | 2025-10-21 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 40189517-e8e5-303a-9235-643ecd51130c | -17.4135 | -55.0468 | 2025-10-21 03:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 141.7 |
| 095fd1c5-8c6e-37f9-8194-c7e1b4b60b2f | -3.497 | -45.7971 | 2025-10-21 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c5ddcfd0-cfa7-3a29-84e0-2bb2bc60bf4e | -3.5154 | -45.8187 | 2025-10-21 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.5 |
| aa5087e6-ef82-3eb0-ba02-be6170bff8b3 | 1.712 | -55.6854 | 2025-10-21 03:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 507bb21a-441e-3b4a-94d5-82fa1e5e8f37 | -9.0036 | -65.9412 | 2025-10-21 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 619ba0f2-7d26-34a0-ad02-73c64fc2dad3 | -9.0036 | -65.9226 | 2025-10-21 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 4b0ee80e-bb3a-3822-8906-b77e6fd03499 | 1.7119 | -55.7051 | 2025-10-21 03:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6f372ebd-4c13-380f-9b5a-9a052fd2525a | -8.9851 | -65.9232 | 2025-10-21 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 505707db-6b0d-3dcf-b570-2b5024f23483 | -19.0915 | -57.5512 | 2025-10-21 03:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 122.2 |
| c113ef7e-6bdf-3bd7-a795-aa0fd12c1aec | -19.0918 | -57.5304 | 2025-10-21 03:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 9e8dc84f-38d1-33c7-9d55-e4638e5cbb26 | -3.4967 | -45.8418 | 2025-10-21 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 65b7342b-701b-3242-941a-63fde0f59a5c | -3.4968 | -45.8195 | 2025-10-21 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 172.8 |
| a48307cd-2c4a-379e-ba2b-7314c13a34c5 | -17.4332 | -55.0441 | 2025-10-21 03:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| d9d8f983-5ff5-3e53-9349-33e1e72d5847 | -17.4135 | -55.0468 | 2025-10-21 03:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 165.5 |
| acd8126f-46a7-324a-a174-2167a5c93222 | -3.5153 | -45.8411 | 2025-10-21 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b77fc2d6-6b25-3695-84ad-c786f9f44571 | -17.4131 | -55.0678 | 2025-10-21 03:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 157.0 |
| dba5af01-6424-375a-8a97-4c387636f651 | -3.59101 | -43.04927 | 2025-10-21 03:32:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f919b9d4-49a2-3ca1-bf54-4ce0c20375ab | -2.98624 | -39.96693 | 2025-10-21 03:32:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de6a9340-0f6f-3614-9dac-45955d68aefe | -6.32218 | -35.05875 | 2025-10-21 03:32:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bab7474a-bad4-319c-8282-25bdc6d3422b | -4.39671 | -43.31679 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e96d9f3-214a-3c96-8996-b78c40bb777d | -5.89903 | -37.82341 | 2025-10-21 03:32:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f976d81-cb8d-37a1-9bea-bc33fc616e62 | -3.59186 | -43.0443 | 2025-10-21 03:32:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d1580e1-166e-3f82-8237-9f0572c5845e | -4.38862 | -43.32589 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c8c17a8-ccd1-3e81-90b6-c38a10908bcf | -4.00611 | -43.27769 | 2025-10-21 03:32:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49961fdf-5c87-3121-b450-6031b14aea4b | -4.3904 | -43.31572 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eeedf1f-dbe7-3dde-bfcb-f495f4a66e74 | -2.98677 | -39.96383 | 2025-10-21 03:32:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56f7387a-7298-3edc-93fa-59faeb281760 | -4.38951 | -43.3208 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea08388c-4e45-3cb6-ba12-be8dc18acd1f | -3.99887 | -43.28165 | 2025-10-21 03:32:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b77eb909-b315-3c2c-b037-845c5dfa4231 | -6.32577 | -35.05937 | 2025-10-21 03:32:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c8e31ae5-a9b4-3158-9e6e-aef2176121fa | -4.39583 | -43.32189 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bf141de-6835-3035-a623-2369edef71a3 | -4.90688 | -38.93632 | 2025-10-21 03:32:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df7cf758-be36-3b5a-8c66-14f8d1e9aa09 | -4.3976 | -43.31169 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07280f9c-e249-3d3e-850e-edea5739a998 | -5.8997 | -37.81937 | 2025-10-21 03:32:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a752a9b3-6896-3fa9-8f88-9afa1f0b9352 | -5.84971 | -40.83213 | 2025-10-21 03:32:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 343a20cb-469d-361a-892d-b40c062716bf | -4.39495 | -43.32694 | 2025-10-21 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d7e0fcb-669c-335b-bc01-fa193615e54e | -6.64898 | -43.42941 | 2025-10-21 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79552389-b7cc-3ec6-91f0-a9cdb12d9961 | -6.92534 | -43.5952 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9409e017-a973-3682-b187-444b79bbc0f3 | -6.90214 | -43.58891 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a62a00e4-3d71-3b78-b847-79aee3d316c9 | -6.92623 | -43.59053 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 279573a4-3293-3caf-98d4-5ffc8c73368b | -6.88977 | -43.6216 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ebf3db7-be1a-3518-8e12-1b5e5140d095 | -8.44218 | -36.26355 | 2025-10-21 03:34:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a94effb0-6d51-3325-8da3-e774a925b3fd | -7.45068 | -37.33281 | 2025-10-21 03:34:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9887599-48c0-35c7-8aba-d869b8a03bd2 | -6.89425 | -43.59718 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96c16a88-48b4-3daf-87e3-4731b9204918 | -6.64813 | -43.43417 | 2025-10-21 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b500494c-0290-30bd-8f67-772d6f925364 | -6.88885 | -43.62663 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d7af61f-0aa7-313e-bd5e-f3d0ce82fb61 | -6.89592 | -43.6229 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86112a5-70fc-355b-82aa-8835f44416f1 | -6.90745 | -43.59475 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README7.md)
