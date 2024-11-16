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
| 463b6864-fc86-3f1e-8dbe-7064af7bfcd2 | -3.91972 | -46.51963 | 2024-11-16 12:44:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3f898193-2e4e-310d-870c-e03d718e42c4 | -0.25521 | -48.51137 | 2024-11-16 12:44:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a2d16a09-872b-3ed5-a2ee-fb183ae841c2 | -1.33881 | -46.1842 | 2024-11-16 12:44:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3f30a6ac-7422-3795-8fc0-9cbb88d9fbfb | -3.47969 | -42.31214 | 2024-11-16 12:44:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1339f93c-ce5b-39e7-beb2-24d982e1279c | -3.83841 | -42.14285 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 507.3 |
| a92e379b-2b7c-3e2d-827d-03c4fb64a75e | -3.6508 | -42.25848 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| ef9f2453-0c97-360c-81d8-439779f79086 | -3.20693 | -45.44867 | 2024-11-16 12:44:00 | TERRA_M-T | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6e9021d4-dde3-383f-959d-58fd0b8dff70 | -1.00926 | -47.76163 | 2024-11-16 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 917f39b4-9e54-3cbe-91ed-e3b0820f1a00 | -2.35636 | -48.59109 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| ddc05374-ea9a-3ba1-b390-70739200d69a | -1.23427 | -47.54418 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fa2233ba-1924-370e-a370-e0aabb9bb0f5 | -3.65307 | -44.33618 | 2024-11-16 12:44:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8c7b2bd2-f91f-335d-9c18-f89e2a99ae68 | -2.03993 | -46.37737 | 2024-11-16 12:44:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71537d40-d852-3d65-9ff6-d77792940a47 | -2.82017 | -46.661 | 2024-11-16 12:44:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ee7e6710-186c-360b-b699-6d7a7b93f044 | -2.28171 | -48.40727 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| afe61596-f877-318b-8986-f7134b9249d4 | -3.78508 | -43.91291 | 2024-11-16 12:44:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| bfcbb025-ac43-313f-b6c9-708f09b4651e | -3.76371 | -42.19503 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| ebe64714-837d-325a-89ba-e71eb67290c3 | -1.01054 | -47.75277 | 2024-11-16 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 64494ae2-f775-3c11-b344-5df94a9b9154 | -2.52545 | -48.12494 | 2024-11-16 12:44:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 2708d998-36af-3d00-8a5c-0112e5dfb06a | -2.82451 | -45.07286 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e4cf3114-9916-37fc-9287-4359813a10cd | -3.47479 | -42.28916 | 2024-11-16 12:44:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 3fce98e9-81cc-3698-9ecc-3381cdfbe690 | -3.92588 | -42.4038 | 2024-11-16 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 0e2fc1c1-5731-3948-b329-014bf71827af | -3.29247 | -42.34034 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e7cd9e09-6fe0-3020-a50c-be6a440b1ccc | -2.35449 | -49.10997 | 2024-11-16 12:44:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 202bc006-bdf5-31d6-bb5e-cb6771c68f91 | -1.65991 | -46.3271 | 2024-11-16 12:44:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6321108b-4168-399b-89dd-89aaee2d7e41 | -4.18817 | -45.85866 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 35468e99-fa65-3763-bcd9-13b15f137746 | -4.28066 | -43.73812 | 2024-11-16 12:44:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4c7f44f1-8662-3e7b-85bf-c7af1bc9345d | -2.91774 | -45.4706 | 2024-11-16 12:44:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c767f72-cbf2-39cb-b917-98d2f74403c4 | -3.5126 | -42.02237 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 67676967-39b7-332b-b3df-2cb3152077f9 | -3.50297 | -42.09039 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| dc1c5630-b228-3781-93f2-efa6c564dfd9 | -3.76121 | -42.03846 | 2024-11-16 12:44:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| e48a5fac-3218-3954-abb1-c03cbb2fbb17 | -3.80651 | -42.45747 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 16f12890-876c-3a7f-8a79-411258a30afe | -3.42132 | -41.93303 | 2024-11-16 12:44:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 7f49acb1-8cc5-34b0-bae0-c94cf2cbcf9b | -3.66264 | -42.26007 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 368.7 |
| d981afaa-77d6-3fc2-9736-7128e3758644 | -3.73163 | -42.50553 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| faef376c-2570-3b10-a64d-f8e2b22db846 | -3.61885 | -47.52009 | 2024-11-16 12:44:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 59d68318-cad3-372c-85af-c011247104b5 | -3.65782 | -45.17976 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e8456f56-9384-389b-a1af-1d9a78d2f2d7 | -2.61277 | -46.17937 | 2024-11-16 12:44:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eedb0cd0-ddb9-3a58-a19f-106d7fe66043 | -3.11613 | -40.92429 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 253.7 |
| b835fbef-084a-3242-828e-b97f50c63e2d | -3.95964 | -42.91962 | 2024-11-16 12:44:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d034a3c8-69b2-36c2-b1a6-a57948436d1b | -3.36904 | -42.21874 | 2024-11-16 12:44:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ddc3eb7b-9230-3de8-b02f-f2a54a503638 | -0.79049 | -49.47781 | 2024-11-16 12:44:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 961df667-44cc-3a71-a65a-46e328e17888 | -3.65955 | -42.24847 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 2cd8b7f8-5773-3aba-9a34-be4a40653f2a | -3.65147 | -44.34782 | 2024-11-16 12:44:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 21753ca6-d409-3322-ad8d-207a4cd40191 | -2.14369 | -46.55955 | 2024-11-16 12:44:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5568f269-7baf-3818-b6bb-5a8617ebfe6b | -2.28039 | -48.41631 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 923f74e5-4a4f-337d-a511-2162d1cf3764 | -2.14496 | -46.55062 | 2024-11-16 12:44:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 09957f3f-843f-39f8-a45a-abab74ef00e1 | -1.99821 | -48.51575 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aaea92d1-de02-3d38-80d1-5d86004f55b4 | -3.11574 | -40.93971 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 52878760-2878-3ad0-8191-1d49b191d92c | -1.28373 | -47.40477 | 2024-11-16 12:44:00 | TERRA_M-T | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 80bd9a9c-37b8-37a1-883e-bd7512498e9d | -3.98558 | -43.71938 | 2024-11-16 12:44:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cb8fdd79-5eb5-37c3-9ff8-ce3f68695ae8 | -2.90541 | -48.30964 | 2024-11-16 12:44:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1ba63aaa-cfe7-37b1-89f5-9a62bbd7329c | -3.72792 | -42.51165 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 40.6 |
| f4d0cca1-369e-3e6e-aa89-ce11df0d20b3 | -2.43608 | -46.18908 | 2024-11-16 12:44:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0ac2be5e-9b3f-3095-aff7-52ec2a33958b | -4.18518 | -43.80422 | 2024-11-16 12:44:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4df59dc3-7cc9-3f87-b920-b295b8c2d1c2 | -0.66103 | -49.40104 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| af87f350-a522-36a7-acd1-f0798dbb2632 | -2.79436 | -48.56303 | 2024-11-16 12:44:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1b1fb68d-16ea-3ec0-ae83-33fb749548e0 | -3.51502 | -42.00526 | 2024-11-16 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 686038f9-844f-375c-8120-37e3e67c5ab4 | -0.65156 | -49.39971 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5d7b9c60-7591-3fd9-adc1-17368f21dc67 | -3.73919 | -45.65973 | 2024-11-16 12:44:00 | TERRA_M-T | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7fdde0a4-435b-33fa-a905-c9b9f466d641 | -3.93764 | -42.40534 | 2024-11-16 12:44:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f7764ee2-da41-3ae5-8cf5-a286c90ac83b | -3.01686 | -45.28796 | 2024-11-16 12:44:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e6d3b03e-1b08-3fd3-841f-fb109cdc0441 | -2.2527 | -48.15897 | 2024-11-16 12:44:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e85b414-1e75-34ed-9da6-b84845711972 | -1.48688 | -47.40084 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e4435140-1e3e-32e7-bc52-bbdedda3cb3c | -1.33561 | -47.23309 | 2024-11-16 12:44:00 | TERRA_M-T | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 38d17c54-82f2-3f42-99de-f7edd56144d1 | -1.21717 | -46.90014 | 2024-11-16 12:44:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6b03f25b-a801-3f04-bf08-3c9ab0ae423e | -3.25181 | -40.99123 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 61.0 |
| b4da5c49-808b-3f6b-bfbf-3c1c19429357 | -3.36075 | -41.3424 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 9fa93f8b-82eb-3362-a7fe-e59d8c7f198d | -3.24898 | -41.01176 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 55701f99-68fe-3dcc-96c2-bf8155f063c1 | -2.34603 | -48.59895 | 2024-11-16 12:44:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 1648e0b0-2af2-3ed9-9099-ccd8dc9844a2 | -3.75976 | -42.18395 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| d14a4fe0-6d22-3692-b7b7-bb6ca097bb4d | -2.4751 | -46.36788 | 2024-11-16 12:44:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 506878cf-019c-3941-a74f-cc29633ab043 | -2.77377 | -48.57863 | 2024-11-16 12:44:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 38b599fe-57b3-3f25-b1b4-490aa566b7df | -3.79485 | -42.45584 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 40a7959e-4d73-363e-80ee-787d425fc28f | -3.82642 | -42.1413 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 40.1 |
| 0f2fd605-88af-3825-aa52-816dba9c4b11 | -3.72936 | -42.52145 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 01f8a4ad-be09-334d-a294-2ab08dd6d22a | -1.01941 | -47.754 | 2024-11-16 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 29186c5d-2b54-3a43-9dd1-bdd0fd1dbea5 | -1.02885 | -47.88821 | 2024-11-16 12:44:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 713bd3db-67e9-34bc-a492-c2650d8a9402 | -1.6236 | -47.91807 | 2024-11-16 12:44:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9548496e-59ca-3aef-987e-e9414276e4e2 | -3.7636 | -42.02127 | 2024-11-16 12:44:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 6abaae0c-2b98-36b7-94e7-cd227629c872 | -3.62214 | -42.20388 | 2024-11-16 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 41.6 |
| f923ab0c-2ab5-3794-b7f2-9cc44c14a8b8 | -4.19066 | -43.79913 | 2024-11-16 12:44:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 546d810c-d9e1-360d-8265-942fc59fe20e | -3.65638 | -42.62254 | 2024-11-16 12:44:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 55dee40a-d298-3b10-ad01-c693a18d1b16 | -3.4166 | -41.60562 | 2024-11-16 12:44:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| bba6254c-6070-3bd7-a86d-e48ef3d01b38 | -3.11868 | -40.91901 | 2024-11-16 12:44:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 268.1 |
| 4f072464-e857-3bc8-8a42-22723e5be6fc | -3.07709 | -48.01372 | 2024-11-16 12:44:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fdc4a6c6-9763-3b12-9720-5377e4794e9d | -0.73272 | -47.88567 | 2024-11-16 12:44:00 | TERRA_M-T | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3b96f1d3-31eb-3b35-ab74-f7e4fed96dd3 | -3.11202 | -42.57517 | 2024-11-16 12:44:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4c5c8323-b1d4-33b9-8b23-bb1fd030aa05 | -4.18954 | -45.84893 | 2024-11-16 12:44:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e1f35aed-aa74-3ccb-9143-4a30aeedc971 | -0.86267 | -47.76189 | 2024-11-16 12:44:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 982018c6-bee0-35e3-9351-d09602a97068 | -2.17639 | -48.75032 | 2024-11-16 12:44:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0bb29a5b-c95f-3f3f-bf5d-997211aa592b | -3.82408 | -42.15829 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 6ad67094-b26b-32f9-99fd-54179ae9392a | -2.03359 | -48.97198 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd2ed8a4-7676-3976-afb0-40595e6cc9e8 | -2.82307 | -45.0831 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ec93cdc0-569e-3f86-8440-b8f8751157d8 | -3.71564 | -42.10243 | 2024-11-16 12:44:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 595d27e8-16a8-32cf-8704-d207661ed360 | -3.7686 | -42.38678 | 2024-11-16 12:44:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 2d88fffe-ea79-3f48-9e80-385777be86de | -3.15108 | -41.8963 | 2024-11-16 12:44:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 48078878-6d74-3425-b646-fe8b0049352d | -0.78903 | -49.48807 | 2024-11-16 12:44:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 9de573d4-5dad-3895-b391-67a18ac1551f | -3.21421 | -46.67659 | 2024-11-16 12:44:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| c17e7330-422b-33ac-80cb-c933503a65bd | -2.64878 | -48.48385 | 2024-11-16 12:44:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 46ff095b-6ab6-31bc-8521-d836e9594d9d | -3.65636 | -45.19013 | 2024-11-16 12:44:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 20.6 |


[Clique aqui para ver as próximas entradas](README64.md)
