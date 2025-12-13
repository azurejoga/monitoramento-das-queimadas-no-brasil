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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0fe6876-8128-3698-a865-1bd1f5bda512 | -1.03269 | -53.73932 | 2025-12-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 739c3b5f-b559-34a4-bed7-96dbc74671d5 | -2.98933 | -52.87857 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3ecfc05-2739-333f-8c5d-fffe906703bb | -2.42803 | -51.92733 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c93c1648-d4b5-3f59-8b02-401137c71e98 | -1.32696 | -53.46454 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50563eef-f7af-3892-8f84-20dfd77c069f | -1.28254 | -53.16439 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bac9fe7d-b501-33b2-b899-f3c23dd047e1 | -2.7346 | -45.07929 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 863b6fd7-de7b-3bbb-8bc7-d820cd5c2d34 | 2.87743 | -60.25952 | 2025-12-13 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfe9d661-6927-3536-8189-68483e9de6bb | -3.69653 | -53.75489 | 2025-12-13 05:20:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb60bc7-2256-3c58-b7b4-dcf6280c36a1 | -3.51762 | -52.19016 | 2025-12-13 05:20:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38357ec7-c544-3648-84c0-9d51bcb99072 | -1.57878 | -54.12415 | 2025-12-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee5950f-37b7-3937-8d1b-2cd182ede649 | -1.66729 | -54.57459 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b45680db-f9bf-3e24-a936-1750cae029d7 | -2.45038 | -52.22619 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc01545e-d813-3157-a5dc-82d4524919c0 | -2.41926 | -51.92597 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0df1abb4-d53b-3fd8-876e-6a9e4e8898a3 | -3.51803 | -47.20706 | 2025-12-13 05:20:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50177a7a-abec-30fb-b1e4-e87700e34c9e | -3.07211 | -52.83802 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6bab5e-6b73-3948-bb22-ea56e1732e85 | -2.73647 | -45.06634 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f14f30de-a8bb-3a82-9ba7-5fdad3e2710e | -2.42365 | -51.92664 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7d72613-0119-37b9-b616-d4d7bbe4920e | -3.4487 | -44.73063 | 2025-12-13 05:20:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d9d76da-7164-3a07-82fe-d8e9f89a214a | -0.79678 | -52.36315 | 2025-12-13 05:20:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 199ef47c-89fb-311c-b05e-bda6708e3fec | -4.82915 | -49.53786 | 2025-12-13 05:20:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e5e4c9f-3a88-3cc0-afdc-44b8b6dd9e25 | -2.23052 | -55.93296 | 2025-12-13 05:20:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8abc3080-1e70-3e86-836b-8e31c179f158 | -1.20125 | -51.83221 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 403ed507-f766-31d6-86be-feaf66d13423 | -2.73752 | -45.06743 | 2025-12-13 05:20:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38c57330-4ce8-328c-b21d-1e360fe97dae | -3.2872 | -57.62974 | 2025-12-13 05:20:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfe3fccd-b230-3705-8bc3-69bbfc4f0b28 | -2.42431 | -51.92233 | 2025-12-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5be65c-4c52-3e97-b169-09e77d5486ab | -1.47342 | -54.20186 | 2025-12-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ee14b86-4cc0-337d-9c97-0a8497c00a88 | -2.4927 | -51.80176 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86a3c64f-d81f-30d6-988f-25f3bfe592c3 | -2.49635 | -51.80134 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b089a839-41e4-3e4c-9544-d4757dfb42e2 | -1.40089 | -55.3828 | 2025-12-13 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e80c6b3-e1e5-304e-92f0-d4dd5d467f13 | -2.48555 | -47.7728 | 2025-12-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b1f09026-d2b4-3692-84ca-131a6b081123 | -2.70355 | -51.88819 | 2025-12-13 05:20:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caa05d2a-c97e-31b5-8207-5637842e92d8 | -1.47316 | -55.5169 | 2025-12-13 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7cd2eb1-1e53-301a-93e2-20d8608bb3ab | -3.00359 | -57.81692 | 2025-12-13 05:20:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f349a25e-2482-3a7e-96dd-01aba12962ae | -3.23738 | -47.25179 | 2025-12-13 05:20:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08672dbc-d970-306f-b7c5-62ea94a44d12 | -2.9476 | -52.55312 | 2025-12-13 05:20:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a88d20b7-88ec-3436-baa3-970b2eabbd04 | -2.48617 | -47.76865 | 2025-12-13 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f1b2c6b-2ce8-38ef-9a9c-db2bad8b6a9d | -1.42925 | -53.47701 | 2025-12-13 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b92ee96-c3ce-3b6f-9f57-44a20dfc8c18 | -1.1112 | -53.68829 | 2025-12-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b9b61a2-e061-325b-862a-6711e58581b7 | -2.88716 | -53.0078 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f22041a8-b371-3609-a806-664eaf32dd92 | -2.49781 | -51.79811 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| febdbce3-a607-3c06-8cc4-a9e86bdd0751 | -2.43892 | -47.16021 | 2025-12-13 05:20:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d32cc0e-e2fa-3664-995b-32f997fa1016 | -2.93472 | -53.02646 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea393da6-904a-3bca-b059-df1a2019a109 | -3.80994 | -47.05021 | 2025-12-13 05:20:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b316984-8beb-3ed2-80c5-137124272529 | -2.50225 | -51.79877 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61429c26-d26e-3b6f-9080-0f81dedbca5f | -2.497 | -51.79701 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65e2ac4-cf32-3853-854a-3d91c6a67341 | -2.50144 | -51.79768 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f19d1e-d928-3141-8c4c-dc82457f96b6 | -3.22634 | -54.77477 | 2025-12-13 05:20:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee09c73b-05a3-3520-859d-d44815cf077a | -2.88659 | -53.01155 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 345c7353-f0d4-34db-b289-e6017fd9a27b | -3.22701 | -54.77035 | 2025-12-13 05:20:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b90d885-7810-3117-bbe0-2261b2236faf | -2.88249 | -53.01084 | 2025-12-13 05:20:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad863b62-ab0f-38ca-bc3e-96659213cdf4 | -2.52939 | -45.32952 | 2025-12-13 05:20:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86b28b45-0c6f-3e24-94cb-d51820455e8a | -3.51813 | -52.18842 | 2025-12-13 05:20:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b9198dd-385e-3b48-9f7d-4a1489865604 | 3.08135 | -60.37623 | 2025-12-13 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9edefff0-d309-39c9-9303-c6bea972a753 | -3.51848 | -47.2109 | 2025-12-13 05:20:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c6038ba-9faf-353a-9c79-4a8fe5e3a2a7 | -2.38581 | -56.0528 | 2025-12-13 05:20:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa4e1ded-1fd6-39d2-92b3-2f9e5ae131d1 | -1.90789 | -54.23735 | 2025-12-13 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9f53e10-129b-3730-aabd-b6860b6ece2b | -2.6591 | -51.64425 | 2025-12-13 05:20:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 994d38b1-57d7-3e31-bb55-264d799d8959 | -1.56219 | -60.31855 | 2025-12-13 05:20:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4325426-a771-3598-a170-76ee444df333 | -9.6564 | -56.86924 | 2025-12-13 05:22:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32db244a-a9c2-380f-90cf-a1a83663cc65 | -4.64783 | -56.20349 | 2025-12-13 05:22:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43d23682-8c21-3da6-b147-6a1d4de5eba5 | -5.02722 | -56.19474 | 2025-12-13 05:22:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65bc1638-78d4-39ef-8b87-fbd4c1daae1b | -14.8159 | -59.94932 | 2025-12-13 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31648865-3f8d-3f30-b581-a869c3ed0d7e | -12.27783 | -60.58532 | 2025-12-13 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf97e045-9da9-35db-97b3-bf10d06091cc | -14.81534 | -59.95296 | 2025-12-13 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a7c0f9-9949-3fc6-8c93-c718d4b758e0 | -11.81542 | -60.53898 | 2025-12-13 05:25:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75c3ced5-55e2-36cc-abcc-d1cd64186832 | -3.1278 | -45.2736 | 2025-12-13 05:30:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 0c7c280e-afee-3d30-a30c-21313413463c | -2.7383 | -45.0848 | 2025-12-13 05:30:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f8508228-23ac-3db1-943f-53859fd66c81 | -3.2009 | -41.844 | 2025-12-13 05:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e7f64305-1691-3002-a4a8-db029f02b348 | -3.2007 | -41.8678 | 2025-12-13 05:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e08a0996-2a1b-33a2-820b-885e2f32da87 | -3.2009 | -41.844 | 2025-12-13 05:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8addd4b6-d812-366b-893a-936ab13c25dd | -3.2007 | -41.8678 | 2025-12-13 05:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 840ba933-0a6f-3aff-9de4-fac343621a57 | -2.7383 | -45.0848 | 2025-12-13 05:40:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| dfd2cb5d-0536-3bad-bf55-4c8d67286618 | -1.42492 | -53.48 | 2025-12-13 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 948c9507-ac08-3929-9b03-c8d890dc06e5 | 3.08127 | -60.37815 | 2025-12-13 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddc38ccf-3b35-3104-ad95-f253ac5b617e | 2.87857 | -60.26236 | 2025-12-13 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a21c786-f1c9-3e6f-81ad-0fa8bd7e6182 | -1.4309 | -53.48085 | 2025-12-13 05:40:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eea24d7-bb35-3664-8df0-f680227c3b7c | -1.4279 | -53.47833 | 2025-12-13 05:40:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3a497bf-f79f-3f2b-94c3-304fd0f2243c | 1.12732 | -60.52641 | 2025-12-13 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef04a075-ed72-3a0b-b388-a12041254c32 | 2.50844 | -61.03169 | 2025-12-13 05:40:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7469ed86-f229-31c9-9fa7-1afa55a9e3c9 | -2.94692 | -52.55749 | 2025-12-13 05:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cafc7cc-f6bf-3611-9f7d-5a11b33ed818 | -2.38529 | -56.05564 | 2025-12-13 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92555f53-7422-331c-b502-c05872584bfc | -2.9944 | -52.87752 | 2025-12-13 05:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426360ad-2965-3a7f-acd7-33bdc76f528a | -2.99153 | -52.88055 | 2025-12-13 05:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a754d4c3-7932-3e70-9e7b-0d563a388a1f | -2.94803 | -52.55452 | 2025-12-13 05:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcf05635-36f9-3cf1-9038-c6ef4c71636d | -2.38993 | -56.05946 | 2025-12-13 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a45fd5-f6a0-3c97-a9af-de97620ccc68 | -2.95332 | -52.55881 | 2025-12-13 05:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82d4def-3b53-3498-8008-b65d9d8bab0f | -2.99365 | -52.88272 | 2025-12-13 05:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3d3bb1-7a96-3806-9e37-36ccceedee02 | -1.66332 | -54.57867 | 2025-12-13 05:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fd2400b-1ffe-35b0-b47d-29868921bfae | -2.42654 | -51.92488 | 2025-12-13 05:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efde43b5-a25f-3d2c-a4fe-dd1617a6f002 | -1.56421 | -60.32056 | 2025-12-13 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c68c1cef-f026-3053-9acf-6f9b39502ddc | -1.56456 | -60.31873 | 2025-12-13 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ea6397b-20bc-34a3-b98d-43439fb32fa2 | -12.28015 | -60.58632 | 2025-12-13 05:44:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4caf0fdc-aa95-315e-95da-59b8eba72c33 | -14.81397 | -59.95194 | 2025-12-13 05:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b46683d-0aaa-372d-a7ae-101a357ddef8 | -3.2009 | -41.844 | 2025-12-13 05:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 03590942-cc59-3540-9df4-d4805bb91444 | -3.2007 | -41.8678 | 2025-12-13 05:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c71d9644-3203-355b-bc18-be2788bbcf3b | -3.2007 | -41.8678 | 2025-12-13 06:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 21f3716d-dd31-35d2-ac01-7aefdba4b659 | -3.2009 | -41.844 | 2025-12-13 06:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6969fc05-57fa-3d3c-bd11-2d7fec43a7bf | -3.2007 | -41.8678 | 2025-12-13 06:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 91e1218e-e495-3554-8570-f6366c5ac5e4 | -3.2009 | -41.844 | 2025-12-13 06:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 32d4036e-a431-35e8-940d-bfdf8c031b79 | -2.66492 | -46.8909 | 2025-12-13 06:14:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README13.md)
