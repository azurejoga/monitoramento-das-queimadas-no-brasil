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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9cfbcd4-a6d3-32a1-a610-72c3a6fd9144 | -9.47594 | -50.81964 | 2024-10-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9eb600a-15b6-3021-ab97-e70c39c99f23 | -3.60489 | -51.47225 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05cc035b-9532-311c-9894-9f8984a41d08 | -3.58768 | -51.2107 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5da30fe7-21ac-3082-9bac-bd290f29d91b | -3.58651 | -51.21746 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e3807806-fa0f-3212-9da9-95caa00970cf | -3.58619 | -51.21054 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 1e23ba41-532b-3409-afd0-1a2546fa5dda | -3.58497 | -51.2173 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| b30b2c4b-0cce-31a0-819a-cc7502177ec7 | -3.58067 | -51.20959 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 076fe263-75de-36f4-9932-4b70b9877705 | -3.57948 | -51.21641 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 42bf9666-85c1-31e4-98e7-5cc909404e59 | -3.51459 | -51.01529 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53552a44-8032-3d5f-a37c-9c8af8b099a2 | -3.51416 | -51.02118 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 652d6671-cb4b-322a-819e-bf01cd524dc2 | -3.51343 | -51.0218 | 2024-10-26 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9da86cf7-dfea-3d9e-8723-6ac3af512625 | -3.3354 | -50.82172 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f685bc1-edb7-32d6-967f-23abb5d91b85 | -3.12456 | -50.60437 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6d422183-59e3-3e79-b0aa-ba85c35fc54b | -3.11772 | -50.60345 | 2024-10-26 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74ccefcf-34f2-3841-b69a-f55114f3a4a9 | -3.09607 | -51.341 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28f1a0e9-93d2-3de0-a457-ec2efc9ed107 | -3.0948 | -51.34828 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35a0c816-a041-31e6-8524-19ec6d35879d | -4.66836 | -50.9657 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d030528-5da4-3762-a2f3-d0a00942c4fa | -4.66722 | -50.9721 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c9b6546-81d2-3f8f-967c-220030b5115b | -4.54025 | -50.96893 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 859297f5-0544-3e4b-9cbf-542d616028e5 | -4.53344 | -50.96778 | 2024-10-26 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd24987b-508e-32cc-9b87-0d1cc1cbaa8d | -2.9501 | -52.5708 | 2024-10-26 03:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a040fb14-9f66-35cf-a6d9-1cfd4c0acf6c | -2.9945 | -50.4816 | 2024-10-26 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b5fa27af-9a15-3f8f-b835-5c5836912cd3 | -3.013 | -50.481 | 2024-10-26 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 3ea0b480-f0d1-3b4d-8c56-e53e4fb7a2e8 | -3.4729 | -43.3377 | 2024-10-26 03:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f8497ade-8510-38e8-9552-f688408df1d9 | -3.473 | -43.3144 | 2024-10-26 03:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| dff94828-30aa-39c5-9426-3863f51500c7 | -3.6084 | -45.8147 | 2024-10-26 03:55:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| c0ffc673-18e3-3779-861f-8116748e5e1a | -4.5613 | -48.0358 | 2024-10-26 03:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6a90238f-0d22-3a0a-85fb-006bf6614a61 | -4.5799 | -48.0349 | 2024-10-26 03:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 231.7 |
| 5a223c2e-669d-3791-8f0a-cbd5624958d3 | -4.58 | -48.0132 | 2024-10-26 03:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| d05cab07-2821-3cb5-a88d-1fbddd5b0405 | -7.6474 | -63.4584 | 2024-10-26 03:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 838cc167-97da-3a00-b15a-44d6e5c6bf47 | -7.6475 | -63.4396 | 2024-10-26 03:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 025a5901-2916-34a9-bd36-3a0d4d5ee26b | -16.9012 | -57.5108 | 2024-10-26 03:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 53a8db4f-48df-3b53-b3c3-7beac0c3d276 | -17.0499 | -53.452 | 2024-10-26 03:56:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 171f63d1-60cc-3f89-b5fa-03331b7101c4 | -17.6667 | -57.4822 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| a3019a9c-ba1b-300d-be57-0fa0d872da97 | -17.6861 | -57.5004 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 325c0961-5985-3bfe-9e40-963690be27ca | -17.6865 | -57.4798 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| fdc7f0af-989f-33a4-90ec-35d1859c8a0d | -17.7246 | -57.5574 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 25a70a1d-2141-3a36-b88f-ee4c2c132c68 | -17.7443 | -57.555 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 9898f257-ad9f-3368-b75c-17d815c7edb8 | -17.7446 | -57.5344 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| affa50fd-e4a3-3b49-ab1c-aa21e72c3853 | -17.7868 | -57.3649 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| fab57d54-c85f-3140-b241-fadb000062c1 | -17.7872 | -57.3443 | 2024-10-26 03:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| 2c1310bd-bb85-3309-9775-78f69fbb65cb | -17.843 | -57.5431 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| b45cef51-fcc5-34c2-a518-c2762b1c17ca | -17.8628 | -57.5407 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 791c93c8-2d66-3c0b-98e5-bb34fb14c9ca | -17.8631 | -57.5201 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 193.0 |
| e9cded3f-9100-3b7f-8a47-8da7846f4e3a | -17.8634 | -57.4995 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| e335405d-f1bf-3590-b39a-bb4fe8e8735f | -17.8825 | -57.5383 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 7ba23945-f01d-32c9-b82f-00093f53d2a3 | -17.8828 | -57.5177 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.4 |
| 18f3da3f-6e2d-3c90-9655-0d441c9461e1 | -17.9217 | -57.554 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| e31f3b2a-db13-3f82-b503-d31bcf46423d | -17.922 | -57.5334 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 3d200b05-a24c-3aea-8d40-c95c8aff9347 | -17.9415 | -57.5516 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 5537f756-48b2-31d9-8dcd-aa3f3c6a8716 | -17.9418 | -57.531 | 2024-10-26 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| aa41042c-dcdb-3f2f-a3c3-bbcf0f88222b | -18.0629 | -57.3721 | 2024-10-26 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 238fcd31-ba1d-3cca-a08d-30e4b0682430 | -18.0827 | -57.3696 | 2024-10-26 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| e3e38d66-de07-3b40-b896-1693f99b8dfa | -18.2649 | -55.9975 | 2024-10-26 03:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 03e8b3f5-5758-3d1a-bc76-574a55211845 | -15.07852 | -41.95357 | 2024-10-26 03:57:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b5c93d16-ae5d-3943-956a-bde869ba7300 | -12.86215 | -38.44269 | 2024-10-26 03:57:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 02ae60dc-4445-387d-ad51-03151ea9705a | -13.95055 | -38.94751 | 2024-10-26 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1858bb95-a059-3bd8-8283-c9ae79c0e969 | -13.95 | -38.95113 | 2024-10-26 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c89e0b5-cab2-31f1-ab6c-8f3a29a3d004 | -13.94721 | -38.94697 | 2024-10-26 03:57:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1035fb78-8e83-3c00-bbbe-f9a3001cb353 | -19.24256 | -40.02378 | 2024-10-26 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 596feda1-4604-3660-b641-e70a0ce51d6d | -19.23921 | -40.02322 | 2024-10-26 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79ae2c7b-f557-3bf1-82d0-e9f795f5400d | -19.17209 | -40.13493 | 2024-10-26 03:57:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7872de82-e80e-3004-97a3-eb71e194f2dc | -18.04166 | -39.92447 | 2024-10-26 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 18478d84-7fad-3403-b343-15a1de2dfb6c | -19.839 | -40.08163 | 2024-10-26 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c7b42d7b-5e60-3430-b3c4-e63d69d9dc10 | -15.61349 | -40.78682 | 2024-10-26 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 43003ae4-68f0-3e24-863b-27489bb807ec | -15.5849 | -40.44957 | 2024-10-26 03:57:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0fb07d3b-9707-37a6-9762-1cbd88b5b7e8 | -17.80832 | -41.06372 | 2024-10-26 03:57:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 50392987-d60a-3ed0-9878-787c0703ed48 | -17.80775 | -41.06733 | 2024-10-26 03:57:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d560fc6-cd51-3630-8e36-f2bae6a6a0cf | -17.21442 | -41.16185 | 2024-10-26 03:57:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c656a519-045f-354b-9af6-7a3bc5b92d3e | -17.03036 | -40.14162 | 2024-10-26 03:57:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b57c29c2-3dfe-3700-8d86-b84239a166f6 | -19.09152 | -40.9925 | 2024-10-26 03:57:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 561a7c7b-ee44-3f49-8964-dac2fb20ed62 | -19.09096 | -40.99614 | 2024-10-26 03:57:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2be64efa-e89d-3987-ab60-346bde8bc75a | -18.54228 | -41.34904 | 2024-10-26 03:57:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a430bfce-1beb-39c6-9c33-498fd552fb42 | -18.3477 | -40.01196 | 2024-10-26 03:57:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 964dd904-86e7-3b38-a2b6-7e87714cc8a5 | -20.08642 | -41.21892 | 2024-10-26 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5b976507-b3bb-30e1-a6b6-7f98fccadfbd | -19.76995 | -41.54657 | 2024-10-26 03:57:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a3659b12-6cdb-30d6-857b-1eaf972eab65 | -12.94398 | -40.64349 | 2024-10-26 03:57:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e630bd39-4360-3fad-aff4-fcd6486425a4 | -12.94065 | -40.64296 | 2024-10-26 03:57:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 190908c2-39ed-38a3-850e-19e4793053ed | -12.9379 | -40.63887 | 2024-10-26 03:57:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe00476c-4299-383f-9ac6-04bfa881aff7 | -12.53311 | -40.74392 | 2024-10-26 03:57:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a93709a-8d17-342e-9203-816a8f01e16e | -14.7686 | -41.61531 | 2024-10-26 03:57:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cd540dd-26d3-3d5f-88f4-5e328772899d | -13.92657 | -41.45386 | 2024-10-26 03:57:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aeec8f5a-454b-3c97-9dd6-2633cc9f20f3 | -16.0258 | -41.18824 | 2024-10-26 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 981d089d-2669-36ef-95b2-4b2b2947b1d8 | -16.02248 | -41.18771 | 2024-10-26 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 676ad15c-55cf-307e-85b7-a6adb92ebfd0 | -16.0219 | -41.19133 | 2024-10-26 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9dd29fa3-6fc3-3ee6-8d5a-6147bdcbcc8d | -16.01974 | -41.18355 | 2024-10-26 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6a307fae-1932-38dd-b23b-c9b9604e8418 | -15.76795 | -42.16789 | 2024-10-26 03:57:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2a8f757-f8c2-384d-9f65-9c1772fb93e8 | -15.46455 | -42.04609 | 2024-10-26 03:57:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7a8d15f7-004d-3e8c-94da-a3383d04bd2e | -15.31968 | -41.74693 | 2024-10-26 03:57:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 41c77bda-2d79-307e-9d51-a1b5c75b6a7d | -16.54049 | -41.62982 | 2024-10-26 03:57:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 09b8e53a-973b-3587-ae7c-b85f4c5cf9f8 | -17.77245 | -42.25863 | 2024-10-26 03:57:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 240dabe3-fe46-30e7-a0bd-6521e44f3b94 | -17.68712 | -42.11434 | 2024-10-26 03:57:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d68e89a5-24da-319d-ad56-d29a7f5dafc4 | -17.68378 | -42.11377 | 2024-10-26 03:57:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ee852107-2d01-3b94-9ee6-5cc070138ebd | -17.67171 | -42.62794 | 2024-10-26 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08c1e96a-6e8d-39c5-8a4b-74bc8fc60483 | -17.64703 | -42.09269 | 2024-10-26 03:57:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4561e269-ef0b-3f14-a938-9cceccf70024 | -17.38303 | -41.76738 | 2024-10-26 03:57:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 470ba335-40bb-32f4-bb31-2dbf6895db36 | -16.70033 | -41.92505 | 2024-10-26 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c9b5237-77e5-37a5-9646-88788c9dddfb | -18.16438 | -42.45153 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ba97434a-a09e-346b-a92e-2b7d463a9fdf | -18.16163 | -42.4472 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d30ce79b-1749-3c0e-a8c8-d8730fffe964 | -18.16102 | -42.45093 | 2024-10-26 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README35.md)
