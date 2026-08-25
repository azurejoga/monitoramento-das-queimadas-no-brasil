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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c5a8ac3-ef13-3aa7-8ab3-77c9029ac928 | -8.59193 | -54.71269 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 985c71fc-d61c-3e33-b6a9-f0a30af7459f | -9.97344 | -53.94579 | 2026-08-25 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b393f9b-393f-3fb7-b480-5be6034e5f5e | -5.94663 | -57.73581 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c292a402-607a-383d-a77d-c60ef918db3b | -8.57717 | -55.2812 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5346f4c0-de0c-3c47-b40c-59aba8b87497 | -10.80303 | -50.92372 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8999f424-1bfb-3821-bae8-56df49d686df | -12.84325 | -48.49714 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35b1d857-ade9-3871-88bf-c0c9ec68a72d | -6.94372 | -52.79507 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 529462ab-635c-3d8e-90a2-811afac106e5 | -7.00503 | -59.25399 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1a8aecc-f30f-3510-aa1d-eecc0819a913 | -9.53226 | -49.27215 | 2026-08-25 05:12:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d8a011f-c0af-3bd3-9fd6-a4bc90cc8a45 | -6.4405 | -54.97624 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c26a9ffb-04e3-3444-9767-02917b8fcc3d | -6.26359 | -55.42309 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f2d2a054-9c3e-32c9-9a9b-9477ff51e47d | -6.96607 | -59.07664 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ef8d04f-413d-358d-896c-19c856848e0c | -6.13824 | -57.76941 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efe2215a-a4f3-3c5e-8165-cee2e3acca88 | -6.89261 | -59.02824 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 11422f22-f8e2-3e76-b1a8-e2f2db0073dd | -10.77306 | -50.93009 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1534ea81-6410-3fcf-a511-3e28125cdcc8 | -10.36815 | -45.065 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 539d5b05-0208-3329-8882-7efb323d15b7 | -6.83604 | -52.50549 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68cbea23-070e-3973-9713-be5f901731ed | -7.21217 | -60.61044 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d788cf9-ea54-356b-830e-a3bfb00c0057 | -6.88052 | -58.93053 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91d87618-c027-3dfc-83a7-c0731d13672f | -6.54825 | -58.5172 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 344a9db6-242b-32d5-a35a-f02cf3accf7b | -8.17214 | -54.96611 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c3f0546-8e68-31cb-b447-132200ac5d03 | -6.79274 | -59.81199 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35d08743-d933-368d-a332-cfc243eceeb3 | -8.10123 | -47.49778 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c0c0be0-106e-3c2e-954a-c5af5c8cf30e | -6.88291 | -56.43599 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b40fc2c-e55a-318b-9289-4d7b7e085990 | -7.21507 | -60.61507 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 96d2a247-2f6e-3c1b-97be-6b6903261d69 | -6.35879 | -54.77504 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c949da8-f4b1-3d84-b1ef-2dc7802b5304 | -7.05187 | -56.61766 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f177aa-b6a2-3929-b9ff-6d2907f59f36 | -11.16147 | -54.00503 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 276bc40d-ed21-3400-bae9-6bf583dbffb0 | -8.81572 | -62.33982 | 2026-08-25 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d405b7b0-e425-327c-b524-46acddd80ca8 | -7.01577 | -59.25196 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93688796-7c1d-3fb4-8699-d8ad93014515 | -12.74868 | -46.46898 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c727a3a-c6bf-3c61-a314-1c3d758310cd | -6.12704 | -57.711 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83610609-b644-3c10-a3b1-517e79bd4295 | -9.41778 | -60.32135 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd7485e-10b1-39f7-86cc-7e28cfee62f7 | -6.96887 | -59.08079 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21939e52-6d4f-385b-8303-22d1dfded290 | -6.1452 | -57.70321 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e4c7452-7e6d-3634-a20c-01fd28a549a8 | -6.94445 | -52.79 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b46ad75-89ba-35fe-8eac-12a7a3df0133 | -6.83655 | -52.5019 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6feecc8e-146c-309a-a47d-aa24db10d4a0 | -6.39441 | -54.97319 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 502dbd36-585a-31a4-a7f4-607570115ed1 | -9.16984 | -59.61457 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75c82915-8a06-3777-8ab3-9b7865c27c9d | -6.10617 | -57.73607 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 978b13d6-9790-3b17-97ad-113b10c0f9fa | -6.7242 | -59.44703 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46ea21d2-cdec-3716-b9d7-20cc3d52f217 | -7.01519 | -59.25562 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 045ffcf4-470b-3b05-a3f8-bb504044da23 | -6.7974 | -59.80496 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d57299db-30b8-39f1-ae8f-d3c3f89d2513 | -6.26533 | -55.41175 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745071dc-bcc1-3951-a9ae-1e69a27b3afe | -8.10176 | -47.49367 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74572de0-2a62-3b6f-bf32-31480d99d250 | -10.93153 | -51.06557 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 343dc58d-ba0b-35ca-afc4-25d23ef5cc64 | -7.23243 | -60.64308 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a51debc2-fcd3-3f24-a4ab-3980c412a754 | -7.01974 | -59.24887 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3aa6d54-b901-3a79-adc1-970e01017881 | -6.86484 | -59.40433 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baf46012-9127-3396-9049-fcf719cad703 | -6.61383 | -58.37995 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90892c53-c369-3d7b-8ff6-e91566ffe6dc | -8.57469 | -54.8562 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe3ee071-a65c-3898-aa7a-e7369d2d19d6 | -6.56699 | -58.58895 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 632b6e37-a101-3d0a-9d36-dd3cb1af3a6d | -6.86171 | -59.02701 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5795a79f-66df-3363-8bfd-887f75eaca2c | -6.26189 | -55.41122 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c19813d-dd88-3f5a-afbf-035235f3bce2 | -11.49717 | -52.92018 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8f69e10-cfa3-34aa-a67f-8bce23c06c61 | -7.21083 | -60.61856 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0035f837-8079-3ae4-a808-384944de412b | -6.81717 | -59.59146 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9c1afd3-dccb-3140-8477-a0e4efffc837 | -5.94001 | -57.73478 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db820c91-a541-3b25-ac02-76b1905d857f | -6.01255 | -57.66112 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2ec64fe-c5ff-3957-8c39-c7d43106cec1 | -6.81661 | -58.64681 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29c9e205-f1e9-3535-81e7-4d47f1901d06 | -8.57054 | -63.02213 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00f4a5af-3e9b-369f-8719-48b519faa64a | -7.43699 | -59.77756 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fa2f67f5-35a8-3675-8352-d34f569a5d58 | -8.59131 | -54.71694 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1bbb2bf-cee1-30e5-8299-43e10b70328c | -6.79736 | -59.82001 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ecccdc7-4227-3c41-98b4-a08e6502c3b4 | -6.13012 | -57.82133 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8c5a23-bb3e-3e35-9a12-bd59438313fd | -9.67579 | -55.09346 | 2026-08-25 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e074093-80fb-3b3c-894e-e6ce372fc031 | -6.94124 | -52.78415 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a316a989-0627-3017-9709-1bd043f7b829 | -6.43528 | -54.96345 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c6f2b53-c746-3ad1-b545-4926beffe065 | -6.13831 | -57.858 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f10eba1-0de0-3933-a564-0b05aa3dde32 | -7.21095 | -60.62371 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c66cea61-e716-3f6f-a0ad-d1dfabd45842 | -9.98159 | -48.31872 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30455665-38ab-32a2-b6ef-079734e7b129 | -7.43356 | -59.777 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 99aa4509-17f1-3403-be7e-9441291c6d29 | -7.44103 | -59.77436 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ecccb89-f0fa-3ca2-9ca2-e6d904badc04 | -11.82217 | -47.64643 | 2026-08-25 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbe2105a-e12b-32ec-a7cb-731fc3cefd67 | -11.18973 | -54.00573 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa30a5cd-7e8e-3b84-be3c-37441fe576c6 | -7.53872 | -61.35608 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d39b93e3-adf2-3b73-a0b5-1d8d2eca3992 | -6.12242 | -57.82722 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d5f86bb-d884-33a7-88e0-044340b1b221 | -8.0723 | -44.65648 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 39b67ef9-2f6e-3665-b7b7-96e33f89eb4b | -10.8078 | -50.9244 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc8f723-eba9-30f1-8754-d65dd110e738 | -6.35818 | -54.77904 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c9790d-4031-356f-9008-0aafd9471138 | -6.43819 | -54.9679 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9526dfa1-e1f7-30f7-af16-15b2ce59c395 | -6.70549 | -56.3466 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b8d07ac-025f-31b9-866c-981cb4a44b6a | -6.72019 | -59.45021 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e32f06b8-c334-39cf-8a13-b6f5352db6ca | -10.93627 | -51.06624 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7088e5e-5e5a-3463-998b-a310e464281f | -6.14628 | -57.6963 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a4bb036-c3c2-343a-8925-9d6ab3de1d41 | -9.23185 | -60.38165 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f3d2d5-2393-3105-8c2f-13976c7f7432 | -8.57526 | -54.87744 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de35253c-cb15-3e53-a086-4c14dccc4065 | -8.59786 | -54.74825 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da0e2f10-1641-3e56-9f13-6a3c2c730dda | -7.38644 | -55.18451 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6a1bb7a-983d-3431-bc04-1537d4c06921 | -6.35345 | -54.78645 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dfa571a-886d-3beb-b677-bd6d21aa7d49 | -12.75829 | -46.44814 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3b5d7471-015b-3c88-babe-bd82cfb0b956 | -7.35889 | -55.66518 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49e57c0a-53c6-30ea-a6a7-e202d167eee5 | -6.35052 | -54.78198 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff3a4699-c992-3283-b70e-5c0f48aac05c | -6.25675 | -55.3989 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 582efa36-f4f1-3f04-a25e-d157c53169f8 | -7.00841 | -59.25454 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f72403c3-e1b5-3165-bafd-84d24b785061 | -7.41802 | -60.00774 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 554d68db-6726-389f-8c13-df08f03fb929 | -12.74819 | -46.47364 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f464491e-7343-3f85-b18d-df475a3739db | -6.81159 | -58.65689 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d48bfe3a-3d44-3cf8-9de6-487d92c6d655 | -8.56591 | -63.02498 | 2026-08-25 05:12:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 977ad2cb-6dff-35fd-a884-a80fa7868ebe | -8.59989 | -54.68346 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README48.md)
