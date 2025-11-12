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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e845ed5-f8ea-38c9-9b35-ba64aaab68ad | -4.9643 | -43.7182 | 2025-11-12 04:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| e0f8e7f8-e4ea-37b2-81b4-46ac0161c5db | -4.9456 | -43.7194 | 2025-11-12 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 60fd2052-0e18-3b61-9561-fd64c8c0fe94 | -4.9641 | -43.7413 | 2025-11-12 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| ccea92e6-a628-3e75-bfed-9c2c79c2faf3 | -19.8034 | -57.997 | 2025-11-12 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 6a6cbbd3-42f7-3556-9b96-892f86a6ed4e | -4.9643 | -43.7182 | 2025-11-12 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| b491fbc5-8350-33a8-a9e3-529564bf8068 | -4.0976 | -48.0144 | 2025-11-12 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f2a286b4-2a36-35ed-8849-add86ca5219d | -4.1161 | -48.0136 | 2025-11-12 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9f0c3e11-7005-3848-9b50-9c388382aa54 | -4.9454 | -43.7425 | 2025-11-12 04:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 0b7fcef6-bc85-3b69-a129-bbceaca0958b | -4.0974 | -48.0361 | 2025-11-12 04:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 51a21711-468a-3c60-9e5d-b30c91376255 | -4.9643 | -43.7182 | 2025-11-12 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 55b2960c-6dc0-37ec-be8e-f48acc2bfecb | -4.9456 | -43.7194 | 2025-11-12 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a7fc1fd7-9a4c-361b-a5bd-ea2fdfef0d11 | -4.0976 | -48.0144 | 2025-11-12 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| dd7e639e-1924-3ffc-87af-e925f10fe614 | -4.1161 | -48.0136 | 2025-11-12 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| db664c7f-df9e-326f-9446-c0b6cd667002 | -4.0974 | -48.0361 | 2025-11-12 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 037289d7-636d-3224-83a3-c1d4522a60f8 | -0.42766 | -50.68157 | 2025-11-12 04:29:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e663f4b-4892-3ce7-bd95-8c5a45f56d9a | -1.61345 | -47.46896 | 2025-11-12 04:29:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1601a65-6739-3b74-9170-6b901a364761 | -0.3543 | -51.71338 | 2025-11-12 04:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca8c6772-400b-35cd-b1f5-07fde2f4609e | -3.02409 | -41.12383 | 2025-11-12 04:29:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 546ab3c0-2afa-3749-ab47-eebeb63245c2 | -3.26293 | -41.40469 | 2025-11-12 04:29:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| caffce5f-02d8-3c0d-8650-32f7c907f870 | -2.82873 | -40.30057 | 2025-11-12 04:29:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 44cde8b4-971c-3e9d-8144-e77d8057b242 | -2.83082 | -40.29925 | 2025-11-12 04:29:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 385ccaec-7ee6-30e0-a960-474e6f021ad1 | -0.62446 | -51.77034 | 2025-11-12 04:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8a33f0d-48db-3f75-9aa5-fe019a856d51 | -1.61399 | -47.46548 | 2025-11-12 04:29:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa9866e9-161d-3a18-9be6-5dc9dc017357 | -1.68966 | -46.57175 | 2025-11-12 04:29:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0da2c2a2-8105-32b2-95e4-5ee293c00a6d | -1.11362 | -52.59306 | 2025-11-12 04:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5bbb496-eb1a-3d72-87e2-30327649f1dc | -1.07933 | -46.57742 | 2025-11-12 04:29:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87414002-6994-3d8e-9592-3fa7ae74f6da | -3.45062 | -39.35918 | 2025-11-12 04:29:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f04ccacb-80bd-379c-b1ec-f6985b81814d | -1.10996 | -52.58824 | 2025-11-12 04:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 533ea6d2-d2cf-3502-9bbd-229d5ed035af | -3.05419 | -40.81252 | 2025-11-12 04:29:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 14799100-1542-3a03-b3c2-a5209349ba2c | -1.08263 | -46.57793 | 2025-11-12 04:29:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c098da-bf85-33d3-b2fb-6ffc95a5ae15 | -1.76768 | -45.28486 | 2025-11-12 04:29:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbcca73e-9420-357a-9059-da30f09ada9a | 0.36731 | -51.13231 | 2025-11-12 04:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 597c25f8-892b-3ffa-96c7-856c7728009d | -0.97771 | -47.63799 | 2025-11-12 04:29:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9bffab7-49bb-3338-a8b3-d07f2abb67e9 | -0.7681 | -52.3337 | 2025-11-12 04:29:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad0724c-144e-3c84-8c64-fc59210963f1 | -1.95614 | -47.06323 | 2025-11-12 04:29:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96673dc6-e6b1-3134-8631-c99d3620e16f | -1.10931 | -52.59235 | 2025-11-12 04:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e1a8475-cec6-3cc8-aa24-e95eb03614a9 | 0.36331 | -51.13294 | 2025-11-12 04:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43c0ad82-dcf0-3175-9b6a-da5c9a5c3434 | -3.2016 | -41.94763 | 2025-11-12 04:29:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8f32ba7-d5d1-347b-a32c-76f0a187176b | -1.25427 | -47.89106 | 2025-11-12 04:29:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fec3baa-5242-37f1-96a5-5ebed7b4fe68 | -4.0976 | -48.0144 | 2025-11-12 04:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 52452e81-63b3-3ed9-b0ef-17a9071b72c5 | -5.65166 | -45.98879 | 2025-11-12 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab70b92f-aaf0-3010-8287-71818b4ff99e | -6.47326 | -43.53615 | 2025-11-12 04:31:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21612e35-0378-39a7-9488-044a3e7f9bd5 | -4.7603 | -44.46301 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6b5c438-145a-3971-b870-05a999661b1f | -2.61831 | -49.21508 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e33994aa-d263-3a51-bb28-80837ab8dbca | -7.184 | -41.73138 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 94d732e1-bce8-30a0-b463-5e830a1207de | -3.9821 | -47.29451 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 0f8d1f6e-6f76-3106-aea7-8d3c465abf63 | -3.93324 | -43.47608 | 2025-11-12 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31272db6-c1a9-3bc6-930c-a2e39f7e211b | -3.23556 | -50.03534 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 838434f5-ea8e-3c7c-8fba-ce1e9c8654b6 | -2.52702 | -47.80521 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ce45670-6dcb-32d8-aca3-0c92ab3ad077 | -3.36383 | -49.50904 | 2025-11-12 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb5a6014-34d6-3e51-a9d2-4189821a203e | -4.10426 | -48.01073 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffac2d0f-dab4-3242-bf94-25fb725e7e7a | -4.10372 | -48.01421 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11934f46-4f11-3f7d-8ea0-7cbd5dd199f8 | -7.40441 | -43.33469 | 2025-11-12 04:31:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1e068a6-e429-3604-8bd4-d9c7d129d006 | -5.21153 | -49.13961 | 2025-11-12 04:31:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f630248-9bdf-3f89-9d19-1c9f84cabdff | -9.5242 | -42.9353 | 2025-11-12 04:31:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f869044c-0536-3d44-ab02-080a99db3818 | -7.36897 | -41.1447 | 2025-11-12 04:31:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 767bb6b7-8b5c-32c0-896d-788342d48ade | -4.1148 | -48.03025 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d534eb0-0759-3a1e-a4b7-9bba87dd7407 | -7.28159 | -41.58037 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 63b8b4dc-4477-3c08-b944-5fece262642f | -3.48924 | -49.96958 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7abc4ef9-262d-3140-8496-5eefe0b83a28 | -6.9997 | -41.28939 | 2025-11-12 04:31:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 349e5915-0f69-3207-9bcb-0f1619a0cb34 | -2.98953 | -52.51805 | 2025-11-12 04:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 636a37aa-bb52-3b07-b8ae-324c266d767c | -3.88807 | -47.17788 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 925a8742-e0b0-3d2b-901c-6757723c3ed9 | -6.90241 | -42.07444 | 2025-11-12 04:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fab521df-3c88-3033-b88d-1b9bc95d696e | -5.00115 | -46.86982 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4516970d-a232-3ede-8725-9f969db7e389 | -5.35705 | -48.24502 | 2025-11-12 04:31:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c292d2-c20a-3fd3-80fa-661112764e23 | -3.96611 | -43.77626 | 2025-11-12 04:31:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97fcfa30-3107-3244-9e3f-0393592a0a07 | -5.06853 | -47.54702 | 2025-11-12 04:31:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b1d2ada-1c4b-31fa-b0fe-a331157c2ad7 | -6.10572 | -41.53642 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 468656de-823e-3281-af0a-0d732eef992c | -5.09111 | -43.73944 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d96da54-6ff4-38e1-aec8-90d644786729 | -5.3383 | -48.53629 | 2025-11-12 04:31:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e03ec55-99e7-36da-b9c9-8b93947d32c3 | -4.22119 | -42.52813 | 2025-11-12 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f2d65443-b4c4-3b7d-9108-4c8866f4fb45 | -3.84745 | -50.06401 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e61fbf8-035c-38dc-83bb-9963ffd5fca1 | -6.22534 | -47.33131 | 2025-11-12 04:31:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 623a222a-5bb4-39ce-b948-0cc462b2d44b | -3.09377 | -49.26754 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e7d8152-7ac8-321d-8ea3-408365210d56 | -4.93841 | -44.297 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c750ef5b-2d9a-36e1-85d6-7a38e2395a52 | -2.46336 | -52.17553 | 2025-11-12 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f960f987-1da7-3209-9f8f-eba1aac1bf1f | -2.63459 | -49.20197 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 187e29c2-a5f5-3b53-b211-1b5bd849c0ed | -4.0993 | -48.02065 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf128d7b-72a6-3844-9472-f502dd4f5201 | -4.77833 | -46.44345 | 2025-11-12 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8eef9e8-3c94-3946-a01d-04259fb44a1f | -4.26112 | -44.60255 | 2025-11-12 04:31:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d10499f5-1fba-3fac-a992-6d8fe552d632 | -6.4764 | -43.54144 | 2025-11-12 04:31:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bdbe633-f9b1-3ebd-a6a8-21d874125d3c | -2.63974 | -49.2145 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec5f9e40-94e1-347e-b9ce-a34d78fcdf51 | -3.48987 | -49.96555 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e819834-15b5-3e1c-ba49-c36077b6a0a2 | -3.26257 | -50.02696 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 885835ae-ddda-32f8-a593-74a862dc2032 | -5.25151 | -38.43012 | 2025-11-12 04:31:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 151e72da-1c5e-3ad0-a908-6833239ff30e | -6.29143 | -47.34159 | 2025-11-12 04:31:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777a255c-049b-33cd-a6fe-1902bd0d10a9 | -4.54721 | -50.26825 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e13bfeec-86c6-3855-bb87-67f647acf300 | -1.50717 | -54.24723 | 2025-11-12 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48af056b-eb4f-3da7-a92d-4a0025b8ec94 | -3.48631 | -49.96499 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c535e31-578a-3e2f-8300-f4156c0c7493 | -4.93748 | -44.29177 | 2025-11-12 04:31:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98ece2b6-570b-3c64-9d30-81885524d718 | -4.32765 | -44.54422 | 2025-11-12 04:31:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| df0acb9f-e4af-3c96-b09c-e1317a26f1e2 | -2.31042 | -50.47733 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3efe2522-819e-3197-8002-d0e3ea6c6726 | -3.87107 | -40.98626 | 2025-11-12 04:31:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7c5861f-244a-3949-99a2-f0042cca6f20 | -4.73647 | -40.17956 | 2025-11-12 04:31:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 84e44336-6fb7-3722-933a-56e849ec4682 | -10.49894 | -44.94687 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4a08d1c8-7031-3568-8d11-46c3071a925c | -9.32641 | -47.83841 | 2025-11-12 04:31:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fcd6de9f-f9b8-3877-b1f5-afd60babef49 | -5.89678 | -42.25602 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5ee23c3b-ca02-375b-96a8-3b533f725dfc | -5.47182 | -48.85134 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30ef1221-3059-33c8-9e3a-84ac762dd057 | -5.25104 | -38.43338 | 2025-11-12 04:31:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa45f44e-3db8-3fa1-97d8-8d1f30003b9e | -6.44253 | -43.48611 | 2025-11-12 04:31:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README11.md)
