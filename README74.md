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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 347a056e-d1d6-3491-acea-cd68be9a992b | -8.08769 | -54.74319 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 907e2ce9-69a4-3d41-87a5-f43aeaf09bcb | -7.56002 | -42.6468 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 464d8f8c-ab4c-32aa-acc9-2406de9029b9 | -8.4344 | -55.62968 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6636232-117b-3472-bc76-92fe2a62cf6f | -10.1539 | -47.90451 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35dd816a-8c82-3c06-8746-dcf288982a8f | -3.76588 | -59.3557 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 054b3034-9576-3946-8d50-6297bf107529 | -7.57348 | -42.64323 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6033a20a-9dec-3725-bca8-89be4c122601 | -9.24411 | -51.25281 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5a47bd07-063b-3ec5-a4b1-bc234e576533 | -5.25321 | -45.57531 | 2025-09-13 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87b33163-d12e-381d-9d2e-c3fc6fff177c | -7.85747 | -61.17225 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b145b9d-efaf-3ab6-a277-cfedeb8a2c89 | -6.32802 | -43.44767 | 2025-09-13 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b8d9c2f-5de3-33e1-945f-4e211f794674 | -8.09597 | -54.75513 | 2025-09-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6559822-7530-38d6-a5c0-cf1d557e992f | -8.42618 | -47.24643 | 2025-09-13 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c31f4671-661c-3fac-a0b7-dbe82b84e0aa | -9.80451 | -48.89499 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31eb9651-8ce5-3ac4-a2b2-ed0b7664100f | -10.01648 | -50.40003 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa375f1a-6edb-38eb-b610-47046767f3f0 | -9.90654 | -51.89135 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c72d4547-1596-3b88-92e1-cc4e19277377 | -6.20284 | -43.45097 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c62f488e-d82f-379c-b310-1ee2e7e21b56 | -3.76943 | -59.36021 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d9306a3-1aca-3341-9f14-1fbbe0f08820 | -9.99394 | -51.73276 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b7713c8-0832-3d6e-97ad-136ae27013f6 | -7.25598 | -44.5943 | 2025-09-13 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f56e7bc-fe25-3f77-996f-163fe2b90120 | -6.4 | -45.6304 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9bba5c7-b526-3db5-9859-eb8d3ce6c5d7 | -9.01565 | -45.78083 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80cbe078-924c-31cf-8759-2c93ba257895 | -8.9251 | -46.14117 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1853acf5-99b4-3349-9e62-61f2b002b5d9 | -8.09375 | -50.19497 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d61ab49-f5d5-39db-a54f-d342c7b80d65 | -9.23518 | -51.22187 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c904446-4cb7-35df-bf8f-1dd13cda07cf | -3.32206 | -50.07693 | 2025-09-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac0702d6-08b9-307d-8ece-eeb2ba1ee87f | -6.56685 | -50.87497 | 2025-09-13 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5495bad5-de5f-3ca2-a024-df99b683ae39 | -4.61893 | -47.41618 | 2025-09-13 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec4591e7-c8ae-3a5e-8935-cad23a2163e3 | -10.24025 | -48.63929 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0492dc2-180a-37ff-b764-b00d87c955d9 | -9.24538 | -51.24394 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2fc50de2-d908-3e64-9126-80b4a198a3cc | -6.19084 | -45.28148 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c06fc4-ffb9-3db8-b006-0635ca251154 | -4.32618 | -56.10592 | 2025-09-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c05f0ef-54ae-3fa0-a70b-723579e6fde3 | -8.30304 | -44.88065 | 2025-09-13 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc2161ce-c010-3078-85a6-59561b61aaa5 | -10.34195 | -48.81325 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2807b3a8-0cb4-3017-94c1-4cd24639f27f | -9.02089 | -47.07314 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24778eca-f310-342e-81cf-b2c7f6ea0c0e | -5.25279 | -45.57825 | 2025-09-13 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bf2128a-07c6-37f4-a80b-77acd53c8894 | -9.91017 | -51.89176 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 796c0f7d-5fd5-35e2-97ad-e997921a820e | -7.86929 | -61.1562 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f131bcac-3b32-3450-9600-e18cd25e3e71 | -9.95568 | -51.68772 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b0fa46d-81ee-3a3f-955a-7a7b263310e8 | -9.23956 | -51.21794 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9fb410a-a2aa-3934-900d-4855a632dad8 | -6.8395 | -47.89415 | 2025-09-13 04:57:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4306a4a-4073-3cb4-a286-b6657f08fd08 | -6.83436 | -47.86588 | 2025-09-13 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5455ebe-fbfa-31af-8d87-31967bf6e081 | -6.91007 | -49.41021 | 2025-09-13 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5e344d1-17c1-3c7e-9137-0fd89894914a | -7.40442 | -44.33397 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfdef536-eb57-3175-a84c-986215cb3d1c | -6.80603 | -45.63513 | 2025-09-13 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad60f7b7-cb7d-31cd-ab11-df0999ad42eb | -10.01735 | -50.39875 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4636f9b3-a36c-3ebe-a966-4630610bc03b | -9.71595 | -47.53661 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ae4f10b6-da25-3dfd-9ce2-cc13a88bac67 | -5.3032 | -43.06125 | 2025-09-13 04:57:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ab2c24-cb3e-3967-a046-fda8ba6b229f | -9.98246 | -51.70909 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d454cb4-e06b-3244-bb75-727eb9f63e19 | -8.51053 | -55.31949 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac906956-fdee-384a-8885-1b412422316d | -10.01883 | -50.38852 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8339c48a-2e69-3766-8c40-f0bef2e557bd | -9.5139 | -54.65067 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcc380d7-f104-3885-9471-8b64179ccc35 | -3.81592 | -52.08415 | 2025-09-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 263c3471-a3cb-3737-8051-58c6e3231e3f | -8.10672 | -50.1934 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c5b601-fbba-3060-9a0d-d4ba4a4ce1dd | -10.22542 | -48.61498 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0665389-99da-34fd-bf63-6284d747d2dd | -9.96782 | -50.40717 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42bc5f73-1c44-3127-8032-368186d29e59 | -9.73993 | -46.89111 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c58644a4-98ea-3f28-8b56-3aff65030e93 | -8.10351 | -50.18797 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26acc9db-374e-3c6c-8449-586b800b344f | -10.07855 | -48.17934 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17c6e5fd-ea89-3c59-90f4-01f8f86c5288 | -4.92649 | -55.77523 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 764fff60-67ef-3cea-80f6-cbc0bdba147c | -7.89954 | -46.2482 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f595a5b3-a4c1-390c-9378-1772d55513b8 | -10.15151 | -47.90658 | 2025-09-13 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3da6234-761e-3ae2-83fc-86b59c9d0322 | -7.31855 | -46.58221 | 2025-09-13 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 28946934-bec7-3a61-b9c3-2c9976c39fdd | -9.24541 | -51.25529 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3f269940-d9f6-3fff-8aed-0f7dbbef3b78 | -8.09057 | -50.18959 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebe9e5cc-ce65-3dde-a605-4769afd90973 | -8.88188 | -49.93394 | 2025-09-13 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95f0934a-5c55-32eb-a045-8e0445848666 | -9.96723 | -50.2968 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b37b404-1cb2-3405-86e5-6ffac7c5c094 | -9.2509 | -51.25844 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a9b33e-1325-356d-8799-b184353d52fe | -7.54481 | -52.51521 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 157576d3-e1cf-382b-8e7a-d9a0bab50e9a | -9.00588 | -45.77287 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a69a5b53-0a7e-3d81-b320-92c72a401b49 | -9.24328 | -51.21846 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72977b4d-33cc-36d7-9713-6146b021e73f | -7.86189 | -61.17304 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6f74d6d-d6a5-3a5d-a4d6-d4931e032fd2 | -10.09272 | -47.20016 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5044f8a7-9762-33d8-9aed-491c62e43329 | -9.98852 | -51.71875 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5947a90e-3eb9-3419-80f3-e982cef20433 | -4.15253 | -43.88174 | 2025-09-13 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee5101dc-e83b-3568-8d30-8d036dce2c2e | -7.77339 | -52.11738 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6615dd2-1cc7-32f9-ae8b-6282c6cee3f8 | -9.06552 | -47.03731 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ec7ea21a-8837-3f48-9701-5d7545653aa9 | -8.92346 | -46.15363 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62120162-e6c1-3518-bee5-75917ccaed93 | -3.48543 | -48.43875 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2073b66b-d578-3811-aaa0-7192ba39088b | -5.20041 | -44.31069 | 2025-09-13 04:57:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 389c21e1-d908-30f1-bb8a-552fb9dfe08c | -9.06626 | -47.0319 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 678ba96f-7a63-3860-b84e-4c22022cf4a7 | -9.95508 | -51.69194 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e05ab735-31ac-3ca0-ad4a-56194693dc68 | -3.2408 | -46.7872 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 6772e911-951d-333c-a143-0280159902d6 | -6.80556 | -45.63846 | 2025-09-13 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c930659-a56b-36d4-98c7-b636690a862e | -7.43827 | -44.39907 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d954b79d-762e-36e4-b53c-5398b61a9414 | -9.02861 | -47.05265 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13dae447-4e7e-3d5a-a4e0-d392fd522235 | -9.24912 | -51.25587 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3d9c933-7ac2-30a4-a4c2-572e5060e432 | -5.34892 | -47.29035 | 2025-09-13 04:57:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 51e338b9-a6fe-31b8-bb35-1ffee7b9eef8 | -6.39876 | -45.63949 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5df6d0b-424d-3696-a222-fd44b74a2c70 | -3.22414 | -47.62507 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 57954581-ff11-3808-a3df-5264e9693e86 | -7.54136 | -52.51486 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23fe47b8-c985-3403-9a8f-255b9e4dc927 | -9.06135 | -47.03139 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0a54f029-17ad-3aa2-9fc8-68b70a1481f8 | -9.93983 | -50.31912 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44501e0f-83fd-32cc-a4e5-85827e2b76e6 | -5.43563 | -49.99622 | 2025-09-13 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62516c94-6474-304e-b2e0-e611bafc27a0 | -10.35972 | -45.39943 | 2025-09-13 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28444c6e-566b-3f93-a82e-3afa282a5985 | -6.11076 | -45.94799 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e54170f8-30e6-3ea8-97e0-d1e4e026e927 | -9.51991 | -54.6338 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d72f04d1-b63e-365f-b134-ff930d51da49 | -7.97199 | -55.30412 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f08b1831-ded4-3499-865f-3359ac825096 | -9.85528 | -43.14289 | 2025-09-13 04:57:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 854442a8-7fbd-3f00-acba-59e5c298d8b1 | -8.05392 | -61.76073 | 2025-09-13 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acb52b06-ee16-3534-8f04-1d8d9f3b285e | -7.40389 | -44.33787 | 2025-09-13 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README75.md)
