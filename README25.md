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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c526899-7e68-36e5-b38a-017ab1b4a775 | -3.17726 | -52.87444 | 2025-07-19 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae21889f-32f5-3896-a6ce-0fe413392926 | -6.1639 | -48.05474 | 2025-07-19 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 568bd103-57cb-3529-98e6-93d986c9e5dc | -3.60991 | -43.54168 | 2025-07-19 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c35f9cf-0703-3644-addc-43d422f84507 | -3.36473 | -49.16529 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 461981e7-376a-3be2-b37b-3d1e8665b775 | -5.64868 | -43.71574 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 53e4991c-2744-3ae3-876a-147e0498fc5b | -3.1414 | -47.01405 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 001e76cb-d214-3dd7-aa83-1e0be73a095a | -2.91565 | -48.2491 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 225ae9d2-7caa-3ecc-84ee-ac1cb758b565 | -3.76333 | -47.50716 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18a52962-b934-369e-b65f-fda6e76d1c20 | -5.64928 | -43.71534 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 121158e2-fafd-30f2-969e-93d2be3b37f7 | -4.10374 | -48.20441 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05f55437-ecb6-3709-aebb-6eb259ceeada | -3.50975 | -47.21998 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a549fa7b-1846-3e62-929e-a3726db36e6f | -4.8197 | -47.31665 | 2025-07-19 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e64c89de-1b56-37fe-9c56-f2af0727ea34 | -2.90856 | -48.2405 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| cd476214-13e9-3301-bdfd-cfad3f3b3bb2 | -2.44838 | -47.32848 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 038e602c-00ca-38c9-80fc-7aba7c06bf7e | -5.79787 | -43.63021 | 2025-07-19 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdc86362-7628-3de0-a33e-fadb49e9095e | -6.78947 | -42.99799 | 2025-07-19 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 00a6f1db-7eac-3d7d-9e0f-24dafeaef031 | -3.39397 | -47.48289 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ea94cc5-6d7f-38a2-aa69-adc920b4af66 | -6.83683 | -42.74382 | 2025-07-19 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4437946f-6f1b-39e7-a3b9-b989501e62ce | -3.46583 | -50.25562 | 2025-07-19 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8dc5ef-6204-300c-836c-5c5e4191aa90 | -2.91677 | -48.24177 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 267ed22c-172e-3613-8b81-c17e730bfa5e | -3.3562 | -51.59689 | 2025-07-19 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e55e9f12-5eaf-349f-8f0f-39cea34e5e0f | -5.65569 | -43.71209 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5f41c745-5cff-3ba1-830a-de67500f66e3 | -0.7488 | -47.75402 | 2025-07-19 04:55:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b9e3108-7362-3472-913e-0213efa08516 | -3.1376 | -47.00892 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 41768208-714a-3ab4-824c-16f26bd36c42 | -2.91323 | -48.23749 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8f28583-7faa-32d5-953d-c4a1ca9739d1 | -4.02985 | -48.0629 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ee61721-b59d-3175-aef3-502632b1d600 | -4.30859 | -48.10697 | 2025-07-19 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 00dbc87a-15fc-33bd-b262-3fd2785a7bba | -3.06124 | -40.0499 | 2025-07-19 04:55:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f291a4c-6ba5-3273-bd07-8e883c4f44e4 | -5.7466 | -46.18884 | 2025-07-19 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3095b115-8543-3ccb-b626-f7b4941ae331 | -3.58895 | -47.52715 | 2025-07-19 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4fc949e-9a85-3d0a-85f8-aa4f4360f7a9 | -5.64758 | -43.72386 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c7dfb1a9-a419-3a43-ae0b-f8cbe330658a | -4.10793 | -48.20504 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec9e6194-7438-3c57-a7cf-7c7971b63d47 | -3.11452 | -47.00999 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd4a466-0dab-327a-8d64-edeb3eb177e8 | -3.29517 | -50.7529 | 2025-07-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 180825cd-7957-3c20-9a90-c999fbe4dd0e | -4.12914 | -47.65074 | 2025-07-19 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 081a88d4-65f9-3e7b-a33b-79612af4f395 | -5.52978 | -43.88503 | 2025-07-19 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 419c4d05-2049-3c32-b3e5-81b5817ceacb | -2.44966 | -47.33101 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c24ffe-b63a-3381-9f45-fc92a9aec592 | -3.13244 | -47.01268 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 96e1c42b-cb79-3df1-bf6b-748d9f78e22d | -5.64813 | -43.71982 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 685a1f5f-bbe3-3039-bce8-5a5cde3f771a | -3.11383 | -47.01448 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4274f8a0-ba38-39db-8000-0ee5b237a68e | -2.908 | -48.24418 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3bb620de-8b6b-3307-9a86-6dbcaa370b9e | -3.38899 | -47.48647 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3caf691d-cfd9-37f2-9177-4cd7d95dd0f1 | -5.6551 | -43.71627 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 69706507-b0fc-3089-8dc3-d77a3d929599 | -4.56043 | -48.01217 | 2025-07-19 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20669e82-e41f-3987-88e8-b99cd9418ea1 | -3.119 | -47.01066 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4dee34b6-8857-35f6-a736-d20c6c625dba | -5.18512 | -44.95771 | 2025-07-19 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9236c442-0a30-38b0-ac1d-d89547f4e437 | -6.78328 | -42.99707 | 2025-07-19 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 6ee5522f-d5a0-3ace-8fa1-736623135a50 | -2.4416 | -47.32552 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93eb309e-64f0-34e5-8daa-9f97b40b8906 | -3.03571 | -49.4276 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 946072f5-33bc-358a-a5ed-e866ac59eae8 | -2.44532 | -47.33035 | 2025-07-19 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bf13d7d-78b2-3baa-a6b5-129ce3fe0bdb | -3.36441 | -49.16321 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2969c0c9-f33f-3f13-8586-45ff921a7070 | -3.54945 | -53.01417 | 2025-07-19 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7072fa95-3e71-33e4-986e-e5c99b249784 | -5.65506 | -43.71254 | 2025-07-19 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 206acdf2-b836-3879-aa4e-60927e0941f9 | -2.91734 | -48.23811 | 2025-07-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47f28658-8f7f-3999-a58a-0ccaada99c6c | -6.15609 | -47.76314 | 2025-07-19 04:55:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35f974a5-05e0-3eb7-a119-876a929f2d69 | -5.53157 | -43.88099 | 2025-07-19 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c188dad5-d0f0-3080-a9e4-fbc82021bee2 | -5.53104 | -43.88487 | 2025-07-19 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8254cb0-1097-3638-a714-6272da85c37f | -3.04406 | -49.42408 | 2025-07-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6539e021-8442-3a73-8f0a-6e140b9a9d81 | -6.78881 | -43.00281 | 2025-07-19 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| f8606346-84b8-3783-b6b3-b320e46c6464 | -3.38845 | -47.48359 | 2025-07-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39619ffd-0959-3c27-9e06-832ac3a78924 | -8.53957 | -47.84375 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61d70e0b-ec45-3f4c-a1fd-967ef3eefd00 | -12.03605 | -48.76268 | 2025-07-19 04:57:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7abba3ce-b41c-3b7c-a71f-39965521719b | -11.96354 | -45.46584 | 2025-07-19 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff5dab6-a817-3cbc-ad75-3765e6955772 | -12.03151 | -48.76202 | 2025-07-19 04:57:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b700842e-3ecd-3e7b-9c1c-082ec7bb2ca5 | -14.20142 | -45.33548 | 2025-07-19 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2109aba9-5ace-3d81-a9ff-fed0ef556ad5 | -10.68153 | -49.67812 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 692645d8-3751-3e8a-a244-b47261d11002 | -12.36599 | -50.33311 | 2025-07-19 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4288d7d3-d638-3067-b704-78f356a7d489 | -9.81199 | -47.74119 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7188cc9c-c279-362d-b387-8c71abfd184f | -11.35859 | -48.73041 | 2025-07-19 04:57:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 141c6997-faf9-31c8-8849-22497bc75fd5 | -10.63099 | -44.76873 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e38f102-aa0b-302b-85c7-c34780f41938 | -12.57802 | -56.97178 | 2025-07-19 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 189039e8-fda4-340b-bd10-95181b4883fc | -11.46293 | -48.16503 | 2025-07-19 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b5f43e0-ed2f-3fea-8103-2d73e49b0981 | -11.73797 | -48.19341 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c3fc33e4-9fff-3033-8645-ea033faabaa3 | -8.41525 | -46.86918 | 2025-07-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ceca108-b9b6-3614-b9dd-c6e1b972ecd1 | -9.80256 | -47.73992 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb042c07-ea6c-3caa-a385-ac9ed79e0930 | -11.48825 | -47.3307 | 2025-07-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bd64b19-265e-311f-bcde-d9964dbb2357 | -12.09199 | -44.74075 | 2025-07-19 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 887ef213-c7ca-3713-835d-29babafc17ce | -12.98822 | -46.94151 | 2025-07-19 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 513e8227-8678-3ac8-896b-669064a8086d | -10.63172 | -44.76636 | 2025-07-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 305fa2cb-95bf-3db2-ae38-986a202fe55c | -7.18347 | -44.09574 | 2025-07-19 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be57c7ca-c430-3d23-8e28-c3db28ea3c18 | -8.07263 | -50.11149 | 2025-07-19 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7884a65c-4c94-3a69-b587-e6d25e7051f3 | -8.30871 | -55.11123 | 2025-07-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7db7ecc5-7743-331e-b922-a5fc4f45b5ea | -10.66792 | -49.68402 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63e90bb1-e145-3b27-933e-778673f14f77 | -10.66846 | -49.68015 | 2025-07-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7ba20d5-2251-314c-b41d-6101d2657cc3 | -7.48968 | -47.49961 | 2025-07-19 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6d793709-4c97-3914-a009-a9b00b486dad | -8.97592 | -61.51114 | 2025-07-19 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c9ee56a-1c6c-3719-bec0-e5a9777a8d6c | -10.2311 | -56.7687 | 2025-07-19 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94972ca4-a1d7-3580-82be-af5c0cec76e1 | -9.76437 | -48.75051 | 2025-07-19 04:57:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1e3228b-995b-373b-b4f1-350770bcdedb | -10.09595 | -47.23927 | 2025-07-19 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5ddd052-3a39-3eee-9eac-22076fb49ce7 | -11.82369 | -48.213 | 2025-07-19 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5732e9ff-33c6-3ecd-a7a4-1d82a968d922 | -10.42 | -48.61556 | 2025-07-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 167a9923-a3ee-39ba-b525-29d02441f91a | -10.29621 | -60.54713 | 2025-07-19 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1210e646-8fc2-3f19-99fe-98b70c91d973 | -9.8167 | -47.74186 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4753e9cd-6c13-3e8d-b218-091912861f60 | -8.53498 | -47.84306 | 2025-07-19 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2692ab9-18f7-3222-8314-a22eb8340617 | -9.62056 | -49.09903 | 2025-07-19 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6413ea-0ae2-3280-9c54-ee27d5f36351 | -9.81415 | -47.73674 | 2025-07-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 78e7c624-db4a-38ee-9f5f-4725324f22d0 | -12.42255 | -45.37696 | 2025-07-19 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f01a610e-e498-3f9d-9f29-9d9cadb50633 | -7.79062 | -56.6916 | 2025-07-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 737f954e-cc80-3f3d-bbb6-2be197c17ace | -9.83536 | -48.37537 | 2025-07-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfb975f2-0f72-3272-a842-7ed251382541 | -8.0534 | -48.40785 | 2025-07-19 04:57:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README26.md)
