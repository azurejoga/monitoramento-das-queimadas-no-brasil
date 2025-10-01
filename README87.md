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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22bc9e4d-bb18-3dc1-857a-6d4866243902 | -3.67499 | -52.13284 | 2025-10-01 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa95ed0-94ea-3011-b10b-96db6a2f7e8a | -7.02878 | -44.78951 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89eb34e0-9954-32af-a1f8-3e901686d74c | -8.58356 | -44.73448 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8753b48-a7d1-3e7d-8661-b367a4d17ea8 | -7.39463 | -44.60895 | 2025-10-01 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e1a62cc-6deb-3286-94c6-8b24c35bcb0d | -6.23239 | -45.33516 | 2025-10-01 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7656eef-8ccd-3257-a40e-4e30e08d3c86 | -3.09075 | -47.009 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5503a414-a431-3f94-ba39-93f5591075ba | -7.79363 | -42.50599 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 74643679-a1d6-36e2-bba2-b3fe9b8e0427 | -5.50018 | -42.76062 | 2025-10-01 04:49:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 64098ee9-890d-3c05-8b14-1d81955f34f8 | -8.55439 | -44.64627 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 863a0d5c-cf2a-34a9-8b8a-1764b688b117 | -6.95628 | -52.55567 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da2d0c89-5043-3453-a035-c86528cfd30b | -6.23056 | -44.14964 | 2025-10-01 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3839bae-0a6f-3247-8544-a230607b06d5 | -6.89559 | -48.00766 | 2025-10-01 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 711510f5-7465-36ae-a814-ea21b531f658 | -3.88079 | -42.51589 | 2025-10-01 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54d1ebde-dc05-3477-b3b1-ab0cba0bec5f | -3.0944 | -47.00961 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e6627f1a-6a27-3866-acee-3fd75dc44bf5 | -2.65179 | -48.50897 | 2025-10-01 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abdb1a30-fc4b-3a4c-8e92-155520485592 | -6.0483 | -42.44405 | 2025-10-01 04:49:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f9a6568-2533-3c3f-bf4d-e50b63a1fd36 | -3.10042 | -47.01926 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba18e570-17dd-3ba4-8f3f-680d0c010225 | -6.21551 | -44.22258 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4e370de4-fd66-38f5-9b9e-2c9ddef8b7d3 | -6.81818 | -47.32249 | 2025-10-01 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 195eba81-db65-38d7-852b-8be89e4e6880 | -7.13187 | -47.33977 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7993cc46-5fa6-3c68-beda-84acc46069ca | -7.11172 | -45.08056 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59db8f10-920d-3950-af5e-9c5fe793cc18 | -7.87723 | -47.27256 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d43e7663-a613-3380-ae8a-3704e38f4734 | -8.55632 | -44.66594 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4046fac1-1368-3640-8d30-2e7e4fc6f4c3 | -7.16327 | -41.71121 | 2025-10-01 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c13663e-2555-3db6-bbdc-d7d43eba1f15 | -2.54011 | -48.24331 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81e23194-6524-32fd-a301-876db8c13eca | -6.81358 | -44.47367 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67d5f7d8-c30b-32dc-9048-c8806663be54 | -6.2758 | -43.65508 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 395ae0f3-e4e1-36da-9633-e47dd8be9e04 | -4.40403 | -50.84157 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819a1197-9744-30c1-9d35-90179368d380 | -8.55172 | -44.73182 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1913bbaa-6baf-3c07-8997-69c7c7aea8e5 | -5.76583 | -42.85996 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2c29d6e1-0d96-39c6-835d-00591a3a3909 | -5.73167 | -42.8147 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 49dca96e-3446-3eae-9c74-9e312063a9b3 | -8.75044 | -45.92796 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5bae95c-a727-3f48-a69f-2ca1aab5278c | -5.80283 | -42.78052 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7931aa28-bba2-3f30-aebe-01164e0e5542 | -8.14998 | -46.27203 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5956a436-1e3f-3bbe-982f-5fed0928ee7f | -7.74156 | -46.20157 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba3c9b0d-9efc-3727-8c93-db27223ba45e | -3.08767 | -47.01034 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce61bda-91b3-325b-85df-2a6df7765346 | -3.93017 | -41.57967 | 2025-10-01 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe08d100-489a-3272-8acd-1070d04b60ee | -6.57872 | -51.67705 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfe4618-f378-3781-ad29-9416cfa636c2 | -8.15977 | -46.26243 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba971ab1-bc48-3067-92c2-3eb6bd5d220e | -8.58877 | -44.73045 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab95f9c6-9c21-3cef-822b-d07b67078b10 | -7.87201 | -47.28134 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6fcdb94-e5b4-3a3f-9a8f-a809e60823c5 | -7.51258 | -45.43063 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c83c38b-db24-3d7c-80cc-7dd419c60d3b | -7.82872 | -47.06376 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30fe0646-7ce7-393d-9d16-b906e331813a | -8.58169 | -44.74831 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b07abe1-b8d5-363d-bc61-2de9d504b3b2 | -5.91227 | -43.90883 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02ec1a21-b707-39e3-8c20-ef97e01083fd | -2.79056 | -49.61976 | 2025-10-01 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4621c553-cfce-31dc-9d50-6c7a9f31c210 | -7.82956 | -47.06073 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fdf4e6b4-b524-38ae-8508-b5e4e60b1ce5 | -7.0564 | -46.42168 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78100902-630c-32e6-9546-f93c8417d4ae | -7.72156 | -47.22831 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f3f82b5-6817-3967-a89c-07cfe061dd6a | -6.43258 | -43.07553 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e356b92-7c13-3dfe-b9e9-a96387d72106 | -4.25626 | -48.55306 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baf4ba80-ac71-3b8c-a95a-109e689583a6 | -5.68104 | -42.62937 | 2025-10-01 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95d1a601-2dd9-345f-82ef-80bf3fa463cc | -5.49932 | -42.73108 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5e44c8c-b501-3177-aaf2-64bcc3b0dbf3 | -8.75413 | -45.93245 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3a49fd4-83c7-3de7-827c-09b1dd0470b6 | -5.85911 | -43.40768 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e850be3-fd0b-31dc-9b11-0b9c59ee0ee2 | -3.94462 | -41.59193 | 2025-10-01 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34da5fbb-f737-369f-990c-137b80f41771 | -4.68471 | -50.47762 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb8adcee-c88a-3161-9e67-e15fc34b6a93 | -8.90672 | -47.62098 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5334b1-20ca-36d0-80b7-427010e0d0de | -7.47288 | -46.45592 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a7da97-ef8b-3568-88f2-b1fb89464f20 | -7.79848 | -42.50978 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7175306-1be9-333a-9036-66bad3352b90 | -5.91006 | -43.92374 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ade08a8e-6f2c-3c58-8448-91df9c5d2653 | -6.40352 | -42.80957 | 2025-10-01 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4c2a264-8d22-3b28-bf70-32255c93db07 | -7.72087 | -47.23301 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97fc8fad-5cc3-3f64-b494-91d1c52e4069 | -6.2608 | -43.65801 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1b149e9f-3f63-3f2d-9b6b-fdbfe7db2a9f | -8.29472 | -50.76522 | 2025-10-01 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d2f6ee3-8ff3-3ad6-b06b-3b719521c740 | -3.45942 | -50.09723 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8e237cf-2dd3-3730-b46c-d34060dfb3d7 | -3.892 | -52.28246 | 2025-10-01 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1a66655-b650-3dcd-a286-d0768190d872 | -6.66443 | -41.39632 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f4f9fa38-958f-36cd-b1f8-2aaabd6a1384 | -5.79862 | -42.77408 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9deaf119-c80d-3031-9030-a69e9426dfc0 | -8.38134 | -48.64803 | 2025-10-01 04:49:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3131fdf-e63c-3522-babd-ee14062fccae | -8.16432 | -46.2474 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb3e1831-f68f-308b-bd03-9a0bd3d1d8ab | -6.0671 | -42.67932 | 2025-10-01 04:49:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 280f78ad-c60f-3372-a08f-1acdbaf33942 | -3.92277 | -42.26913 | 2025-10-01 04:49:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2149af63-64fb-3892-bcb4-5bf45fbeb835 | -4.40293 | -50.84849 | 2025-10-01 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9b7ff8c8-1d7b-31e5-ae47-d06aa2d137ea | -7.62611 | -45.4517 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26ac8497-5170-3903-b71b-3b89ea07fd12 | -7.07836 | -49.6125 | 2025-10-01 04:49:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eab606cc-f023-368f-9ac8-b47391383f4c | -7.63331 | -45.44631 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70922d5b-af55-3b33-9d62-8dff33c7454f | -8.55891 | -44.71391 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1093f77-6982-3d1b-8d5a-fc1e6ffba3f0 | -6.79777 | -45.98248 | 2025-10-01 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05333fc8-baa4-3498-8505-28c54d283798 | -6.1376 | -44.7372 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5f8f8dc-1ae9-3b21-9e04-4c880407b962 | -7.39527 | -44.60454 | 2025-10-01 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f31d6eb6-9a4d-3005-8faa-309e228f08bd | -8.58046 | -44.75737 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e924851-4dcc-3a04-999f-824e5107f0d5 | -7.4171 | -45.40985 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad8dc1fb-15cf-3e80-b3f2-30d2d5d44a62 | -3.87999 | -42.52144 | 2025-10-01 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d13c07c-c08a-3a6c-8e1e-5b82308897dd | -6.73733 | -50.9289 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af5c815f-b21c-3b3c-a147-577d2daa61db | -8.5576 | -44.75617 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 581e84cb-7105-3123-ba01-433226755857 | -3.45997 | -50.09376 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41943cda-8def-395f-9ee0-cf235e54ce0a | -7.02324 | -44.46725 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fbe96de-8b83-3032-97f1-ac75c9f781d0 | -3.28251 | -50.03411 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7dbb944-14e4-317b-b5c6-99e83f68f715 | -6.7381 | -43.75929 | 2025-10-01 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dce84daf-a454-35e4-9300-58b914db861d | -7.41882 | -45.4125 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1ae9cb5-e69d-378a-a90d-676161749ac2 | -5.8897 | -43.83566 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8da2829-ea34-3523-a322-7ee2c841a977 | -5.41461 | -41.323 | 2025-10-01 04:49:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fd3dcc2d-1634-3640-b000-ec9cd73d83cc | -6.27659 | -43.65304 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 041efcab-042c-3477-8370-f940ae3cc6f1 | -3.93402 | -41.59042 | 2025-10-01 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b84d6832-74ce-3c35-bd51-ef56958b67fc | -7.6298 | -45.45638 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d4b86d8-5e2b-3db5-a6ea-97adf7894a8b | -3.41776 | -51.23181 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40a762fa-65f6-3ea8-89bb-aa49ea71a7a3 | -8.22441 | -45.78864 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d838ab7d-017a-3200-9cac-11ffbbb9a713 | -6.89922 | -48.00821 | 2025-10-01 04:49:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcc966aa-3ef7-3756-8699-05466b2fa014 | -8.90812 | -47.6116 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README88.md)
