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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46bc2f4a-1132-3ab5-9190-148ae504fc9f | -17.72 | -57.6 | 2024-11-15 12:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92d0121f-3505-3bd9-a092-43b0f385361d | -3.48915 | -39.42837 | 2024-11-15 12:04:00 | TERRA_M-T | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e9619f41-c588-3036-943f-1cb09462b9f5 | -3.55723 | -40.54547 | 2024-11-15 12:04:00 | TERRA_M-T | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 51aa1677-af12-318b-8e4f-1eb972ac4b8c | -3.47796 | -41.49439 | 2024-11-15 12:04:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 8b8e63ce-19ce-38bd-8969-e7c50e013542 | -3.35028 | -42.02847 | 2024-11-15 12:04:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f5085bc4-099b-3656-b7af-811db1f0036a | -3.46307 | -42.97436 | 2024-11-15 12:04:00 | TERRA_M-T | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 88cc6c09-3c0d-3141-9926-f15de9bc1d4d | -3.56535 | -39.79561 | 2024-11-15 12:04:00 | TERRA_M-T | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2181737b-d794-3371-a335-8ab0ef411b08 | -3.3764 | -40.52145 | 2024-11-15 12:04:00 | TERRA_M-T | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 25.1 |
| aad74f23-9fed-30fe-955e-cd9609394934 | -3.35234 | -42.01447 | 2024-11-15 12:04:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| e0c6c217-9155-321b-8572-2a024accc6b5 | -3.09443 | -42.58559 | 2024-11-15 12:04:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 87cd80ae-1616-3e90-b84c-de1a11878f90 | -3.5474 | -40.54426 | 2024-11-15 12:04:00 | TERRA_M-T | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 727ad2b2-3861-333f-b2a8-f678b5d005f2 | -5.96646 | -39.08843 | 2024-11-15 12:06:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 613d722f-6d52-3879-a6d3-47f1531ce504 | -5.7721 | -38.07404 | 2024-11-15 12:06:00 | TERRA_M-T | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 490f8b40-5bb9-349f-8487-768da52b8b3b | -5.40613 | -38.17735 | 2024-11-15 12:06:00 | TERRA_M-T | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f9aceab4-18a2-3d35-9044-270e7134dc80 | -6.83182 | -39.2933 | 2024-11-15 12:06:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 219e2d6a-e9e3-334e-81b9-2a4ff2bb7d66 | -6.33478 | -38.01068 | 2024-11-15 12:06:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f9205240-6a8a-39b6-b018-55c2fb1395f3 | -5.64773 | -37.72019 | 2024-11-15 12:06:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ab363ef9-7a57-301d-ab0e-7d515c49bb9a | -4.39457 | -43.69839 | 2024-11-15 12:06:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1ea872b7-233c-38d0-b974-5769b7e4088f | -7.36932 | -38.57423 | 2024-11-15 12:06:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| c507e4cd-c7fd-344b-838a-139f9bbb3bee | -8.12062 | -38.04328 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c48c2061-69f3-3f61-919e-314e87d9b766 | -5.00466 | -38.66244 | 2024-11-15 12:06:00 | TERRA_M-T | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 5ee9fb1c-41ce-3bfa-ac19-6cb98b3a2481 | -5.24154 | -39.56279 | 2024-11-15 12:06:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d7050c1e-72b2-357f-8769-cbb09ac28e4d | -6.55809 | -38.0066 | 2024-11-15 12:06:00 | TERRA_M-T | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 19b75499-f795-3af8-bb9a-d038787d6ddc | -6.6015 | -38.40649 | 2024-11-15 12:06:00 | TERRA_M-T | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 841e81dc-2c79-3b75-9632-309996d6cf3c | -6.83316 | -39.28424 | 2024-11-15 12:06:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 02094b75-5372-3a06-8556-47deb8baec85 | -8.00903 | -38.49201 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 180373ee-069d-3813-88f6-5c90062510f8 | -8.63331 | -39.27552 | 2024-11-15 12:06:00 | TERRA_M-T | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| fe4c4358-e0f3-3898-94f7-bd97e2aeac35 | -8.00776 | -38.50086 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2da36ad5-2d5e-30e8-b03c-176251bcba84 | -7.31884 | -37.26161 | 2024-11-15 12:06:00 | TERRA_M-T | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 50.6 |
| caeba9cf-2f48-3f84-a68b-699a0e80dfe9 | -7.32013 | -37.25241 | 2024-11-15 12:06:00 | TERRA_M-T | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 2cc881e8-bc29-37fb-8e59-d2450637e3bb | -7.72424 | -37.52525 | 2024-11-15 12:06:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 9089eb0d-0526-34e7-b426-99fda163f075 | -7.63775 | -39.0181 | 2024-11-15 12:06:00 | TERRA_M-T | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 45767d60-7342-3601-9495-e6598b963246 | -7.71915 | -38.33302 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 45d0fe02-b6cf-37e9-ae54-9a148b979406 | -7.28448 | -38.08655 | 2024-11-15 12:06:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2d8e82a9-aa75-3e64-a98a-6731343e3395 | -4.36158 | -38.19546 | 2024-11-15 12:06:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1c1755bb-75d6-36bc-95e2-482a834b11ca | -6.52445 | -37.59752 | 2024-11-15 12:06:00 | TERRA_M-T | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ce4756f3-80a2-3dee-90b9-16ba9cc07278 | -6.54998 | -39.07106 | 2024-11-15 12:06:00 | TERRA_M-T | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 054405f4-3702-36fd-8f8f-3efe14775706 | -7.85965 | -38.06041 | 2024-11-15 12:06:00 | TERRA_M-T | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 33.5 |
| dca6f8b8-a604-3b21-8027-3c7191c93b9a | -3.70981 | -41.93741 | 2024-11-15 12:06:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 8c52651a-3599-3e1b-a771-76fbf5b03799 | -4.73828 | -44.09879 | 2024-11-15 12:06:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0c5c9fba-549c-381a-98e3-41af306ea984 | -5.46027 | -39.52015 | 2024-11-15 12:06:00 | TERRA_M-T | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 6cd5c7d8-aec3-30da-8bd6-ef61270309ab | -7.63906 | -39.00918 | 2024-11-15 12:06:00 | TERRA_M-T | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 31.2 |
| f6982a44-4ea9-31ff-a8cb-6f60fb5ca078 | -7.94809 | -38.66404 | 2024-11-15 12:06:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6f76ee95-6450-30a3-a738-726fe3bc774f | -6.52318 | -37.60644 | 2024-11-15 12:06:00 | TERRA_M-T | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 30e93265-7d47-3894-84da-b4b432832686 | -4.4686 | -38.60397 | 2024-11-15 12:06:00 | TERRA_M-T | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| f4203655-28a3-3f41-b4e3-eb47cdaeba16 | -10.99444 | -39.22279 | 2024-11-15 12:06:00 | TERRA_M-T | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| f9f32d37-8b6d-3183-8fdd-22c9a1b26964 | -8.1219 | -38.03439 | 2024-11-15 12:06:00 | TERRA_M-T | CALUMBI | PERNAMBUCO | Brasil | 2603405 | 26 | 33 | nan | nan | nan | Caatinga | 31.1 |
| b4b25de8-2604-3d84-9431-307bea0ab8e8 | -8.01441 | -37.62158 | 2024-11-15 12:06:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a0cf954d-9ba2-35c3-a012-212b484da028 | -8.05907 | -38.01898 | 2024-11-15 12:06:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| be686045-2977-3f09-b201-73273137c981 | -7.9468 | -38.67289 | 2024-11-15 12:06:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 20.6 |
| eb41ec60-2859-32c8-82fa-9ea97175404e | -8.25949 | -36.66744 | 2024-11-15 12:06:00 | TERRA_M-T | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 2824e6bc-5159-305d-84f9-16b45f4b5090 | -7.77193 | -37.18606 | 2024-11-15 12:06:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 43.0 |
| ed6f0fd6-0bc0-33e4-89c1-651b10a7fb1d | -5.1994 | -36.86333 | 2024-11-15 12:06:00 | TERRA_M-T | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 67f1f7d7-49da-3282-addc-869d3ca80e14 | -7.5412 | -37.6441 | 2024-11-15 12:06:00 | TERRA_M-T | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ee681872-7e87-3c52-afda-27b026afd783 | -8.04292 | -38.5213 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 35118dc4-402f-37c7-bf1f-dfd8ff460838 | -8.85442 | -40.71054 | 2024-11-15 12:06:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8d9e1245-d97e-3cf6-9010-8543291c6148 | -7.97743 | -38.52365 | 2024-11-15 12:06:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 77dea9f4-07d1-3f61-87e4-d4b63086daa1 | -9.14559 | -36.84991 | 2024-11-15 12:06:00 | TERRA_M-T | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 84ea38f4-f899-3934-96cc-973260308a63 | -4.76859 | -38.82742 | 2024-11-15 12:06:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 79de6c37-2d65-39f1-bf53-c4330b7e7c0a | -11.04255 | -40.27604 | 2024-11-15 12:06:00 | TERRA_M-T | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 587336a6-a962-3ddb-a853-a0260022ed78 | -5.8267 | -39.84632 | 2024-11-15 12:06:00 | TERRA_M-T | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| cf00f7a6-b6dd-32ac-b379-1ca94f75028d | -4.40112 | -43.71194 | 2024-11-15 12:06:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 06622e09-3645-3f1a-a72b-cc903d436e55 | -12.93565 | -40.70135 | 2024-11-15 12:08:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dce2a310-7084-3a1b-82c8-16b61ef2fc78 | -17.7048 | -57.5597 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 408.7 |
| 46c6cca8-f1c5-36da-b46b-58078b23a535 | -17.646 | -57.5463 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| a6d7d369-154c-37d0-872b-6d4c9f0b3496 | -17.7052 | -57.5392 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| d6ca1a7b-fe4c-31a9-bca6-416dc886f7fa | -17.2543 | -57.4698 | 2024-11-15 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| c5f297a3-36ca-3ec5-99da-566f80bcc137 | -17.6477 | -57.4434 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 214e5ca7-7bf5-3aa2-bfae-ebc46c600d25 | -17.5885 | -57.4506 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| bf8c0e69-2370-309c-84af-e3556746f4c0 | -17.5865 | -57.5739 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.5 |
| 5397b1c9-9127-3058-9d84-8a06a4ba65ba | -19.5426 | -56.908 | 2024-11-15 12:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 85b04ed6-7982-3dd2-b973-953cf44fb9ca | -17.2547 | -57.4493 | 2024-11-15 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 90331a65-7840-35b1-81cc-ed61b0646db2 | -17.5672 | -57.5557 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 9d9e85bc-37f5-30ce-bfd6-84ed33951b52 | -17.5882 | -57.4711 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.4 |
| 0dd7fa11-68c9-3596-845e-f0527b1fa45a | -17.6263 | -57.5486 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| cb5202fb-b7ec-3b9b-9e97-fc29566e871e | -17.5869 | -57.5533 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| dba1d2eb-be63-3db6-a517-1ef6f443db9c | -17.6473 | -57.464 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 558a5e58-ac33-3dbc-a438-b6244c7ef225 | -17.5675 | -57.5351 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.5 |
| caf6b5dd-2b0f-31d7-a464-543cb9094894 | -17.274 | -57.4675 | 2024-11-15 12:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 94f6294b-5a2b-3a29-bc3c-d9dd11087709 | -17.5879 | -57.4917 | 2024-11-15 12:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| a5f6933d-7fa4-3fcc-b6c6-1bcc1ed586fe | -17.5885 | -57.4506 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| bf49c1dd-55df-3a93-83ed-338fa4739562 | -19.5426 | -56.908 | 2024-11-15 12:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 0d76c2a5-2866-3b53-bbff-9467c90e45b3 | -17.5672 | -57.5557 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| f3531964-c50f-3c58-beaa-dc2373924b23 | -17.5865 | -57.5739 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 8a606209-c06a-3fe6-94f4-20bb869b6b67 | -17.7246 | -57.5574 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 54096db3-6eb3-39c6-9a7d-9889597a42f5 | -17.5872 | -57.5328 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 73a6544e-df77-3bc6-9518-26d7652d630d | -17.6079 | -57.4688 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| b299cdb4-daa5-3e64-966d-f777dc961138 | -17.6263 | -57.5486 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 69936019-a514-378f-9531-78ef84933b62 | -17.2547 | -57.4493 | 2024-11-15 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| da74d786-2c31-3d36-aad7-c7b2e8bd6ec7 | -17.5869 | -57.5533 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| 20fd19b3-b468-3b83-b541-adadb15e8940 | -17.7048 | -57.5597 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 213.9 |
| 0d50cb51-8cc2-3513-883c-098fb0ffcb91 | -17.646 | -57.5463 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 1d7e90fd-5b52-39e5-b2c0-44ae20c044a4 | -17.5688 | -57.4529 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| beed7e0e-0434-347a-8f7f-d009addd67b4 | -17.7052 | -57.5392 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 44319ab3-76ad-3916-bf2c-35b994440ee2 | -17.2543 | -57.4698 | 2024-11-15 12:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.7 |
| 6813180a-d72e-30c6-bc65-940476112067 | -17.5879 | -57.4917 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| fcdec6d9-81db-3988-8d33-760dbef962fa | -17.6477 | -57.4434 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 24745819-82e5-30a3-b28a-b0b442f94099 | -17.5678 | -57.5146 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 8a2b73b2-a63d-3f15-bf64-4ee5b9854b27 | -17.5675 | -57.5351 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 16ef1b19-7292-3a0e-86d5-d799b5693559 | -17.5882 | -57.4711 | 2024-11-15 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |


[Clique aqui para ver as próximas entradas](README36.md)
