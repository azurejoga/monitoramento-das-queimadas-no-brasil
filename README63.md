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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83b8a599-1cf2-3db6-b5b8-9466a01e57cf | -13.04519 | -42.14366 | 2025-10-19 12:19:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 52.4 |
| fc0a7a62-6d46-39c1-8a6d-5d0a58cd9ed8 | -8.58317 | -39.59696 | 2025-10-19 12:19:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 42.8 |
| c1d179ec-2fb7-3559-af61-ca5f5afc31c7 | -14.64328 | -43.18492 | 2025-10-19 12:19:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 901f2429-9b8e-3057-b88a-38ac64599b67 | -16.45034 | -49.06522 | 2025-10-19 12:19:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 36a02461-8796-3593-9b78-999c407dae0a | -8.25475 | -43.31218 | 2025-10-19 12:19:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| e3ac939b-09c4-36e4-be26-dc63c6db51f9 | -13.90443 | -42.13066 | 2025-10-19 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| c57b3b3d-81b5-3126-aaf9-522a32d4afd9 | -8.23463 | -43.29521 | 2025-10-19 12:19:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 5aed5b60-fed4-36f8-b59c-128c390c65e8 | -10.55971 | -43.39782 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 83e096c1-03ac-3f07-9662-acfebea9cd2f | -12.9613 | -47.25938 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0f2de80c-7693-3617-a6c8-8124ae1b505f | -12.95352 | -47.24847 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0a862a37-e6bb-373a-aa03-ce4e0ec6944c | -12.01751 | -41.46493 | 2025-10-19 12:19:00 | TERRA_M-T | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 161.3 |
| 628d562a-3433-3fb9-b33d-bc9cce5adf2b | -13.87909 | -45.52307 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 317707ff-7618-33ee-9f4b-26b75db4be13 | -10.54954 | -43.3907 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fba5eac1-03dd-3049-915e-710053463ac8 | -8.94377 | -42.68989 | 2025-10-19 12:19:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| df8e926d-9c21-38a7-a28e-e7b05ed227e4 | -14.49184 | -45.60378 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6b4b2a68-3826-383f-b1c7-d99f4d33ce2e | -12.95997 | -47.26897 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 58159c1c-a5eb-3984-b8a2-f9d9aaaa458d | -8.565 | -44.56514 | 2025-10-19 12:19:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 39693d4e-b649-3b0c-bd5b-1aa55914a234 | -14.48167 | -45.6024 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| add231c1-6fdf-35f4-b5c3-fc118fd94e09 | -11.13828 | -42.17098 | 2025-10-19 12:19:00 | TERRA_M-T | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 1ac72a8f-18a8-386d-9f17-36e7abb5970d | -12.99493 | -47.27997 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 79b318ce-0ea7-3053-ba86-286a5df4e1c6 | -15.22919 | -47.2266 | 2025-10-19 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5bafc7f8-fb21-3897-99d1-2e8025001913 | -14.02703 | -42.66415 | 2025-10-19 12:19:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| a17be341-6d35-3f4c-87d4-740a84a5c4df | -10.22308 | -44.06092 | 2025-10-19 12:19:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c847a10a-bd64-3593-a309-43357d0da31d | -13.92887 | -45.61571 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c49a7c1f-efbb-3a1e-88d5-8060f94a5054 | -8.44515 | -44.157 | 2025-10-19 12:19:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 7c257cbe-05fb-38d0-8d14-085139e271ed | -8.94169 | -42.70607 | 2025-10-19 12:19:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 589407e0-a83e-3376-abeb-411f031e289b | -8.56346 | -44.57692 | 2025-10-19 12:19:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4bc4466e-d97c-336d-b069-f278f80e29c1 | -16.15607 | -41.14859 | 2025-10-19 12:19:00 | TERRA_M-T | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| 190eeb1c-9a16-389a-9802-35c046ed331a | -7.71319 | -47.85952 | 2025-10-19 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7dfc7f05-6e8a-3df0-80c1-e7bd4cd691e3 | -14.22972 | -51.84736 | 2025-10-19 12:19:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| be2ce5ff-4c8e-370c-92b7-eed4dc63b04c | -14.47308 | -45.58878 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 4e24f6ea-028f-3467-aa9e-28e44af8b1fb | -10.85742 | -43.94861 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f22ddef4-6618-3a28-b191-2943a153d24e | -7.93692 | -47.20791 | 2025-10-19 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 228c1c92-7b69-3952-a90e-f40960760758 | -13.90811 | -42.1242 | 2025-10-19 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 6c4f9488-4b73-3b67-9828-280ecc9c21dd | -8.43482 | -44.15556 | 2025-10-19 12:19:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 9ba7882f-1e82-30b5-b5b3-2389b7b6b2af | -13.93926 | -45.61079 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 74997be6-3c50-3765-8ce7-be20553dc12b | -8.43831 | -44.1499 | 2025-10-19 12:19:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 8770aa7e-fdaa-3509-88bf-b35292379782 | -8.56432 | -44.57108 | 2025-10-19 12:19:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| d9c235e4-6579-3b60-b444-3868d0f57e2f | -8.25288 | -43.3261 | 2025-10-19 12:19:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 52ff48db-508d-32fd-bbd0-9a3ce7a15b2e | -12.97818 | -47.27155 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| bb10ad8b-1493-31db-9948-8d29b3f69385 | -13.0444 | -47.25779 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b2d64ad3-c8a6-3be5-b2d2-c889261d6bc7 | -10.55148 | -43.37584 | 2025-10-19 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ff56fe4c-b3c4-3acc-8232-b12da8c2720c | -7.70564 | -47.84943 | 2025-10-19 12:19:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| da01ae6a-5c61-3e4a-8d2b-fe32ddb2d31a | -10.56283 | -43.37723 | 2025-10-19 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e414e9a6-729c-3fcb-8409-36d33e7cbc86 | -12.96775 | -47.27985 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 767f658f-5d93-329b-91c9-433691f58f12 | -14.71489 | -43.14365 | 2025-10-19 12:19:00 | TERRA_M-T | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 21.9 |
| f1bf6b85-70dc-3d06-bdf5-1a75e34f41de | -10.55021 | -43.38152 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 04106fb3-f822-32c0-95a0-4d54299e11ec | -8.49869 | -44.15005 | 2025-10-19 12:19:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6e37998a-17de-3fca-a3ea-b98ce1329fcf | -14.02686 | -42.65764 | 2025-10-19 12:19:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 5ace5c1d-4ef3-3d8a-b4b3-0606405d9eac | -8.58241 | -40.9925 | 2025-10-19 12:19:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 081b1a30-c892-3f99-b763-c01b4b798f7f | -14.71155 | -43.13662 | 2025-10-19 12:19:00 | TERRA_M-T | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 7d44a720-3dc5-324c-b4e3-bf037bd2a830 | -8.75328 | -40.79206 | 2025-10-19 12:19:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 7ab3073f-0505-31b8-ac17-6899ce3f1e7c | -14.49132 | -45.59718 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d8f87132-f84d-3dec-ba5c-7bb25a693644 | -10.3072 | -44.0366 | 2025-10-19 12:19:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 712218c0-2990-33d6-8570-0393008a9e27 | -13.90554 | -42.14587 | 2025-10-19 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 33.9 |
| c452a148-fa8e-37a5-bf02-ec0762d04ca4 | -10.12272 | -45.52291 | 2025-10-19 12:19:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f1456ec2-8617-3ef4-ad95-2e102662acf6 | -8.58403 | -41.0078 | 2025-10-19 12:19:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 126.2 |
| b25ccb96-e435-33c5-ab7f-6a5dee8506c1 | -10.55216 | -43.36571 | 2025-10-19 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 79164ab6-c523-3d6b-afd1-c9f3f4caf10b | -13.0523 | -42.08309 | 2025-10-19 12:19:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 41123e8a-88a0-30ec-aace-8f2b8a54e334 | -10.87009 | -43.93605 | 2025-10-19 12:19:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 66974f69-6e4c-3005-81ab-29d88c0ec986 | -14.22805 | -51.85824 | 2025-10-19 12:19:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ed0a1839-6f70-3fa2-a71e-fb239ad64ddd | -10.57102 | -43.39942 | 2025-10-19 12:19:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c02bda74-e7ce-3e93-ba17-bfeaf0688972 | -12.97041 | -47.26066 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ff165f66-65e0-37bc-bbfb-1db29b50b621 | -14.02918 | -42.64505 | 2025-10-19 12:19:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 3d1d666e-8d90-3e91-9c78-748414d08046 | -13.21117 | -43.15112 | 2025-10-19 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 1ffa864e-698c-31fb-8b39-138e28e641d3 | -12.96263 | -47.24976 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| df06e2ee-436f-3c3e-83e3-44ec8659dcdc | -13.93775 | -45.62273 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 863f9cb2-a298-3c03-99d3-9c4064324847 | -12.97685 | -47.28112 | 2025-10-19 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 4429c7f4-ca3b-303d-ae54-cbc8e87b90df | -13.0547 | -42.06265 | 2025-10-19 12:19:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 48f07f0a-a2c9-3cb2-8c15-958d598444f2 | -13.89078 | -45.51239 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a5cb4591-ec11-3bd4-a3e8-d3ace4d35244 | -13.93896 | -45.6171 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 687e9d32-d049-3d59-aecc-bfe30435da07 | -14.49025 | -45.6159 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 012b5f68-00de-340f-bee6-cef1a7cfb747 | -14.21984 | -42.45212 | 2025-10-19 12:19:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 41cddbd5-7d14-3b45-9346-a3f0bc5d9699 | -14.48325 | -45.59025 | 2025-10-19 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 94cb9df2-56ee-32d5-a21b-b400070ffd9d | -8.12629 | -42.25943 | 2025-10-19 12:19:00 | TERRA_M-T | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 3115d1bd-8289-3014-a284-c1d30d56be5f | -14.52446 | -43.52784 | 2025-10-19 12:19:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ff85bdef-a6ba-3aab-8042-65c87e8fb8ef | -16.61347 | -41.66383 | 2025-10-19 12:19:00 | TERRA_M-T | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| f2cef354-4150-3c55-91b4-96cc37a3143c | -8.57069 | -41.00621 | 2025-10-19 12:19:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 125.9 |
| b53bdd98-39f5-3444-8db1-9c1a9b13aaac | -15.26151 | -43.57756 | 2025-10-19 12:19:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| db6cd89c-783a-347b-8da7-14b7cfc3ff35 | -10.16497 | -42.21367 | 2025-10-19 12:19:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 3ed1f2ae-43a1-30be-b443-697df3df5a7e | -13.92036 | -45.60234 | 2025-10-19 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e4b6cd78-7d07-3639-8707-3c76a01e6470 | -14.4949 | -45.5949 | 2025-10-19 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 70ac1efe-8bbe-3cf8-9e47-690a70af0cfa | -13.9317 | -45.6007 | 2025-10-19 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 543f1693-a3c2-3b20-917e-9b7e67112485 | -13.8947 | -45.5145 | 2025-10-19 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 081477b7-f295-3cbb-bfce-9afd09c712d1 | -14.4754 | -45.5984 | 2025-10-19 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 781953a9-d3fe-3af1-be6d-6e3232fdf7d7 | -14.4954 | -45.5716 | 2025-10-19 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 22221189-b148-3ed8-b7c7-016e6fdbfefe | -26.78698 | -50.95698 | 2025-10-19 12:23:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 88094be6-1570-3db1-a2dd-9bac5f42f737 | -31.57072 | -51.27939 | 2025-10-19 12:23:00 | TERRA_M-T | SÃO JOSÉ DO NORTE | RIO GRANDE DO SUL | Brasil | 4318507 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 7f4b64a9-c873-316f-b9db-d9b317a34817 | -14.4949 | -45.5949 | 2025-10-19 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 199.4 |
| b57ad77a-5546-37d8-83c0-c6f39627824d | -14.4954 | -45.5716 | 2025-10-19 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 7e633f09-7a88-356f-b721-c3d31cb9828b | -14.4754 | -45.5984 | 2025-10-19 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 28c9fb76-8297-3879-a718-e3755836f5c5 | -13.9317 | -45.6007 | 2025-10-19 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 623b155a-2b59-3e5c-b8da-e73a0d2c9258 | -14.4759 | -45.5751 | 2025-10-19 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 70edd5bd-8b2c-37bb-9516-488d319b3cce | -14.4759 | -45.5751 | 2025-10-19 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 86ec437f-4311-3ff6-864b-bca0d6643e0a | -14.4949 | -45.5949 | 2025-10-19 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 226.8 |
| e935f8a6-9c9e-3489-8040-68d8b826757b | -11.358 | -44.2926 | 2025-10-19 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d2625ccf-dcde-3feb-8000-7109731f86ab | -13.9317 | -45.6007 | 2025-10-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8e1aea90-4998-32dd-a4bb-bf363388658b | -13.8947 | -45.5145 | 2025-10-19 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| c42e2b2c-5533-30c8-b99f-c3bdc53ef733 | -14.4954 | -45.5716 | 2025-10-19 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| f0eb3d11-89c5-32c0-ad5c-aae1971bc337 | -14.4754 | -45.5984 | 2025-10-19 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |


[Clique aqui para ver as próximas entradas](README64.md)
