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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07850ee7-6476-3c9d-970c-af5665ed9aed | -10.85368 | -68.26811 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d9fc2442-a0c3-3730-88b1-dbd59f151bbe | -10.80836 | -68.40919 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b15a2a4a-d4cf-3a19-bf22-75aa67ed0674 | -10.80711 | -68.40023 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 74a81392-b9d5-3794-9bb4-1cb023c1167a | -10.64448 | -68.55507 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8fe5983c-5633-32a1-a37f-f51ebcb2540d | -10.64042 | -69.59498 | 2024-10-18 02:19:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4249d7f-b505-3605-9846-967c6fcfeb77 | -10.61932 | -67.72301 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b3a784f3-7345-3cd5-9981-c937a3385d7a | -10.61579 | -67.82633 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e9bc46f-d07f-3cfb-99d1-a642b727d9b1 | -10.57988 | -67.7664 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 278cbef3-f090-3500-a4d2-e8328316f72a | -10.55813 | -67.81332 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1b476751-46bb-319a-ab65-b0308db88272 | -10.55005 | -68.5383 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7c4298a4-ec2e-3487-8244-5b3ae54c5524 | -10.54921 | -67.81464 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6f0869f-3e1a-3611-8f80-ba15aa11c111 | -10.54621 | -68.57536 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ae16976-d648-3d3f-ab5e-2573f39e9cf2 | -10.54496 | -68.56641 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d5f7eaf8-c47c-3f96-86d0-f6f488e97c2f | -10.48062 | -68.63679 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a7d986ba-809d-3a54-a019-f779e48b9b3f | -10.47937 | -68.62785 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b887ec58-e73f-39c3-84d6-0615f831543f | -10.42432 | -67.90425 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 24baa4a6-7f34-3c94-9b48-4e78819183df | -10.39654 | -69.16287 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a44f72f-091d-3fa3-82c9-ccdad81f8711 | -10.38959 | -67.9249 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 826353ea-7f9c-3f73-ab30-fcdd1c7ede76 | -10.38644 | -68.42842 | 2024-10-18 02:19:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a03dd052-8331-312a-9aa0-196bafb9e848 | -10.3555 | -68.06892 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bac38422-b01c-38fb-b827-c22e202f4697 | -10.3528 | -67.98606 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc071460-2cc6-32d5-a0f0-67b413c8ef45 | -10.29972 | -67.74231 | 2024-10-18 02:19:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1e586e1a-ca8c-3b8c-87b6-68295ac581fe | -10.29902 | -68.00007 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4d9781d8-f595-379d-80c0-d6818ac3c9aa | -10.24285 | -67.92487 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a2b8e72b-3007-3552-8d1d-d08ea7f42575 | -10.20265 | -69.09347 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8076e1b1-7def-3472-9432-be3236e71145 | -10.16116 | -67.99895 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0cb82721-fd98-3a3e-a164-1221d4aaf49a | -10.11253 | -68.04916 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0ec86f28-d385-3d9b-a31d-8588682b65fd | -10.02123 | -69.03445 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 39db2233-46c5-304b-bbcb-616d18b54ff7 | -7.78872 | -72.76106 | 2024-10-18 02:21:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a710c17-b626-3dc6-ab4b-e1c3d908d681 | -7.75202 | -72.48152 | 2024-10-18 02:21:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b33ab34b-f9e4-3905-9e0c-5edf6632359e | -7.70527 | -73.04401 | 2024-10-18 02:21:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0d2d28e2-8e3c-3033-b9f2-ade6f4c0b75d | -7.70315 | -73.05119 | 2024-10-18 02:21:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a2761eb9-f9a0-3aea-9d52-951485404c71 | -7.70157 | -73.03884 | 2024-10-18 02:21:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c385d1db-4ad6-3484-9754-14e32fef5bb0 | -7.38218 | -72.69646 | 2024-10-18 02:21:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2591d46-e3e2-32ba-b873-35ab3440d0f7 | -7.3815 | -72.69112 | 2024-10-18 02:21:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0e1df07a-bf6c-3a21-9529-833f5fb8a8cb | -7.38068 | -72.68484 | 2024-10-18 02:21:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9db2b165-b4b9-39aa-8697-a8a043031c70 | -7.38011 | -73.31129 | 2024-10-18 02:21:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 91a5d41d-3f17-360c-b332-e38ff65048ad | -6.68773 | -70.11539 | 2024-10-18 02:21:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 133903af-5e9e-323a-b848-038813ef34d4 | -6.68009 | -70.12557 | 2024-10-18 02:21:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 0fb7dc99-39bb-3353-a36f-909e695da1c8 | -6.67886 | -70.11665 | 2024-10-18 02:21:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b145b2c7-3aa4-39ec-b018-327078d7a308 | -6.67763 | -70.10773 | 2024-10-18 02:21:00 | TERRA_M-M | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3dda12bd-0355-3725-81b5-385835b42506 | -2.8795 | -51.6695 | 2024-10-18 02:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0fe21b6d-74d7-3ce9-a8a4-9266f0a7823f | -3.1566 | -51.4965 | 2024-10-18 02:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b8a40ebe-4b68-38d3-854d-b175047edda5 | -3.7009 | -45.9 | 2024-10-18 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 0c6412d0-57f9-3e93-b360-3fb4d1e76a83 | -3.908 | -42.402 | 2024-10-18 02:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 771b4f00-6ce2-3850-a441-7b23e4db7533 | -3.9265 | -42.4246 | 2024-10-18 02:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 6e1b1f88-1692-3155-90eb-45c2681b8250 | -3.9267 | -42.401 | 2024-10-18 02:25:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 61fba3ef-d897-3871-998e-754874614528 | -3.8733 | -52.0715 | 2024-10-18 02:25:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 19371985-52d6-3df1-b37c-dd68b3992b24 | -4.4258 | -45.9763 | 2024-10-18 02:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.9 |
| f5d56948-cb30-3b4e-9a1a-bb129440a140 | -4.426 | -45.954 | 2024-10-18 02:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 387cd3af-d03f-3c3d-9650-7d4d0a4088ba | -4.58 | -48.0132 | 2024-10-18 02:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b4910379-39f2-37c4-b591-8ebac95a8524 | -6.6886 | -70.1171 | 2024-10-18 02:25:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 27b7289e-0602-3e6a-8c70-9d3d2917e177 | -12.5048 | -55.1846 | 2024-10-18 02:26:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c661845b-b7cd-32f6-a500-3dc88cd1990e | -17.2177 | -57.3102 | 2024-10-18 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 7e8a9653-8126-304b-9df2-8a0871fd8e04 | -17.2373 | -57.3079 | 2024-10-18 02:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.5 |
| 1781fcf6-92a0-3116-93c5-269fa203cceb | -17.7855 | -57.4473 | 2024-10-18 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 6368c36c-28ca-33f7-a077-538d883a4987 | -17.7858 | -57.4267 | 2024-10-18 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 92da2669-51ce-35e5-92ec-6b6a50f9f3b8 | -17.8049 | -57.4655 | 2024-10-18 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 3e5fcec8-aeae-38f0-8de2-230b73aeb6ca | -17.8246 | -57.4631 | 2024-10-18 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 1bd35d09-9fe2-36b0-96c2-6b6bd05416e4 | -17.9234 | -57.451 | 2024-10-18 02:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| d15a41fa-f08e-3597-9adf-4a19f5663c9f | -18.2533 | -56.6446 | 2024-10-18 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 253.1 |
| c4d65bc0-a331-3dd5-9043-8bae9a4d8eb5 | -18.2537 | -56.6237 | 2024-10-18 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 357.4 |
| 63f39458-6f87-3724-b5c1-10cebc9c8dc2 | -18.254 | -56.6029 | 2024-10-18 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| f1a070db-2fd6-3e57-bc45-36ea988485de | -18.2731 | -56.642 | 2024-10-18 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 4650cea6-5604-3dd1-8fed-f3a253bdeb81 | -18.2735 | -56.6211 | 2024-10-18 02:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.8 |
| c5906cbd-3940-3cc2-bd84-f106ebc2d670 | -21.9662 | -49.7186 | 2024-10-18 02:27:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 460975bd-13ba-3a96-968d-691a9c93a7cb | -22.968 | -49.5286 | 2024-10-18 02:27:12 | GOES-16 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| d374c9b8-1488-3a04-bd1d-44cd9cd8109a | -10.4269 | -68.641197 | 2024-10-18 02:35:15 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5211292b-0224-3a9d-8945-a57f97da6791 | -9.5167 | -66.178802 | 2024-10-18 02:35:19 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07670795-d6ea-392f-a9ce-a3ba1c855db1 | -9.5214 | -66.197098 | 2024-10-18 02:35:19 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 937a8586-2b7c-33aa-bfdf-2ac8de3d1464 | -3.1566 | -51.4965 | 2024-10-18 02:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 186c2acf-1cdf-31e1-b12d-04047a3954ef | -9.6233 | -68.566399 | 2024-10-18 02:35:27 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab7a0bd-b4f9-3b26-b007-d2535e24d0a4 | -3.908 | -42.402 | 2024-10-18 02:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 43d90881-2658-3727-be0b-0a0224c3976e | -3.9265 | -42.4246 | 2024-10-18 02:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| a7af10b1-dc3c-34e2-9ea6-dff42fcdfc55 | -3.9267 | -42.401 | 2024-10-18 02:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 149.7 |
| ff9ce742-731a-3dcf-bcec-534674732fbd | -3.8733 | -52.0715 | 2024-10-18 02:35:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| aa7ea482-e7f3-3f33-a42b-e8dadb429912 | -4.4072 | -45.9773 | 2024-10-18 02:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 795708d7-2392-3da7-bda5-aa470735d118 | -4.4258 | -45.9763 | 2024-10-18 02:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| bc4f97d1-ff9d-356e-a44c-0b2d44581ed2 | -4.426 | -45.954 | 2024-10-18 02:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4ffa1b91-53cf-3f9b-8599-bd5f5094a9d9 | -4.5614 | -48.0141 | 2024-10-18 02:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8549a425-6c34-33b6-945f-49cd29ce25a5 | -4.5799 | -48.0349 | 2024-10-18 02:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1f1ef178-146b-3279-b573-d0cabd7ae648 | -4.58 | -48.0132 | 2024-10-18 02:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| df38431a-adf9-3d0c-abbb-afd4b9daa8c1 | -5.5716 | -44.8927 | 2024-10-18 02:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ff22a9b5-b09c-3b38-a824-c8df99904ccf | -9.084 | -68.807198 | 2024-10-18 02:35:37 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2c78c7-5e27-3f77-9c3a-af856af58a1b | -9.0871 | -68.819603 | 2024-10-18 02:35:37 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3b98a1-cf21-33c6-8af9-09e8d2156f59 | -8.5619 | -69.752296 | 2024-10-18 02:35:49 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd84aa9-2e5c-3b8d-b88b-05b603c0cb0b | -8.5073 | -69.994598 | 2024-10-18 02:35:51 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 89a58e78-a004-35b6-b5a1-ad90f88d5283 | -8.4582 | -70.260902 | 2024-10-18 02:35:53 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9318f73f-a352-34e7-b863-b3438724ed53 | -7.7023 | -72.503098 | 2024-10-18 02:36:14 | METOP-C | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 050a12cd-3967-3566-8aee-0bd8059e85ac | -7.7004 | -72.495201 | 2024-10-18 02:36:14 | METOP-C | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 35cef058-29da-3a80-b533-9ae7111da8fb | -12.5045 | -55.205 | 2024-10-18 02:36:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5fb79160-2287-38fa-a141-3ef68c04d9ee | -12.5048 | -55.1846 | 2024-10-18 02:36:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| edb86741-d27a-396e-b63b-af40fae4362c | -7.6463 | -73.056396 | 2024-10-18 02:36:17 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b015c721-c69f-34e7-800b-ea6c1e3966ee | -7.648 | -73.064003 | 2024-10-18 02:36:17 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f3b193a5-9421-3bc5-bc84-e3e78388fd4b | -7.3253 | -72.699699 | 2024-10-18 02:36:20 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eda81872-8fa0-302f-8b94-31b5a5e0e282 | -6.6229 | -70.138603 | 2024-10-18 02:36:22 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b234330-94b7-30f1-9888-017cb7528ff6 | -6.6202 | -70.127602 | 2024-10-18 02:36:22 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76bef68d-3fd9-3755-96f9-9f66009da767 | -6.6326 | -70.136299 | 2024-10-18 02:36:22 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 800ca742-5669-3fca-8be1-dd13f8de2ec4 | -6.63 | -70.125198 | 2024-10-18 02:36:22 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2443548a-ef87-3234-92eb-67fd9a53df0c | -6.6273 | -70.114098 | 2024-10-18 02:36:22 | METOP-C | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
