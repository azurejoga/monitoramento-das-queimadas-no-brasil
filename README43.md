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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080b41c7-bac3-376a-929c-051b4feb0fbb | -12.8843 | -45.8183 | 2026-09-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3d1d7485-6e74-312d-ad99-a144ef425996 | -5.6168 | -43.9965 | 2026-09-04 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ccb14082-a1e7-36c1-b694-8832c14915a1 | -12.9032 | -45.8382 | 2026-09-04 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a0aa26e5-e0a5-3b8b-a91d-58d292450445 | -5.5982 | -43.9748 | 2026-09-04 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 640a89f7-acdc-32bd-978e-09fc664573fb | -3.7828 | -61.7545 | 2026-09-04 13:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 32d9509b-fcc9-33cb-a0af-33baeba1e0d4 | -5.598 | -43.9978 | 2026-09-04 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 62f8a71c-1082-38cc-a192-97c0b7c3a0b3 | -17.1074 | -56.851 | 2026-09-04 14:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 74c3393f-be2b-3d64-a81a-5e6117868dc7 | -7.2513 | -43.7896 | 2026-09-04 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6a1a0cfe-c699-3b84-943c-983be6b4e4d5 | -3.7645 | -61.7548 | 2026-09-04 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| fcdb597b-b79b-3b26-9630-6664e76851a9 | -3.3 | -57.8875 | 2026-09-04 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c9ea6275-4c7e-39d0-83d6-b6a1e78a6245 | -3.7828 | -61.7545 | 2026-09-04 14:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 059b7d64-216c-3b71-a6d0-729816ba2305 | -3.3685 | -59.5036 | 2026-09-04 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 75d7fe54-d0d4-3423-aa5f-24b46bb8d94e | -10.9661 | -51.1463 | 2026-09-04 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ed6b9ff3-a47c-3d8f-a177-4a749b69d173 | -11.3524 | -50.6159 | 2026-09-04 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 57af0301-a321-3a89-b0c3-f16b114a8a98 | -6.6881 | -59.982 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 254.6 |
| 66acfa0b-d51e-3ba3-8733-13583bd2a06a | -12.9032 | -45.8382 | 2026-09-04 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2b3ad480-be4a-3906-bc24-147976eb5a4a | -10.5103 | -51.3194 | 2026-09-04 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 582fc29c-8283-37b1-a4d1-fd16088f4093 | -6.688 | -60.0012 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 51aed099-e467-36c5-9c37-2e77094be81b | -6.6696 | -59.9827 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 8992c416-2ef8-3723-86ff-de8a0b6b76cf | -5.5793 | -43.9992 | 2026-09-04 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c4199a0c-780e-3a9c-b8f7-4262e4f52260 | -6.6698 | -59.9443 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 46098dd5-905a-3bff-9ad9-a57b009bfecf | -3.6215 | -60.566 | 2026-09-04 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5da4cfb8-1ea4-3782-bd38-17b6ea16f094 | -6.6697 | -59.9635 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 360a23d7-3b31-3671-b97b-39c7c3a392a3 | -5.5978 | -44.0209 | 2026-09-04 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1a6cfa57-99aa-3441-b41c-baf3d830b67f | -11.1123 | -51.5325 | 2026-09-04 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e5b8a330-712d-35c0-8c8e-720efdd8d613 | -5.5982 | -43.9748 | 2026-09-04 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 55583f21-c8d9-315d-8130-c862cbc8b252 | -4.1307 | -56.3434 | 2026-09-04 14:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 73d8be90-2753-37e2-90ec-31ff8e7fa2a8 | -6.6882 | -59.9628 | 2026-09-04 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 4dd6c930-9390-3012-a934-b4fab91d4076 | -5.5978 | -44.0209 | 2026-09-04 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 03ea8e4b-19b5-3d3c-9c25-48888507e654 | -11.1123 | -51.5325 | 2026-09-04 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8a414c6f-945d-38d3-b93f-537708ea02b7 | -3.3 | -57.8875 | 2026-09-04 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| de8721ed-8c8d-3389-9880-1e7783e5dade | -9.4538 | -45.6228 | 2026-09-04 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 16f3f53c-9089-3ec3-9b07-e4a6650f99b3 | -4.1307 | -56.3434 | 2026-09-04 14:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 13d8368a-c162-394c-94fa-9739eaf072eb | -17.1074 | -56.851 | 2026-09-04 14:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| 4034d269-5b17-38f0-a921-22433b24c8ba | -5.598 | -43.9978 | 2026-09-04 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 71a4e226-79a5-3726-9902-d75cc217c2dc | -10.5103 | -51.3194 | 2026-09-04 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| ca348f07-a017-303c-941f-790578370625 | -13.7014 | -52.9464 | 2026-09-04 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c42cb96d-8fb6-3659-8406-f20adb566612 | -4.6297 | -55.7353 | 2026-09-04 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 7aa27169-c4e4-3303-a2b7-d62555b0758b | -3.7828 | -61.7545 | 2026-09-04 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4880a149-0c58-356b-87dc-0644b7feecf0 | -5.5793 | -43.9992 | 2026-09-04 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6326c8b7-012f-353c-b360-77a41a2fe1b2 | -5.6168 | -43.9965 | 2026-09-04 14:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d95d6bef-11c7-3f84-a769-9b932f65eca9 | -3.3685 | -59.5036 | 2026-09-04 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 74e1585b-248a-39f4-a8c2-7188a9334b57 | -3.7645 | -61.7737 | 2026-09-04 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e5d4b36-82ce-3e61-9238-36cc21e9d5ac | -3.6215 | -60.566 | 2026-09-04 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 514d4129-2489-303a-a624-adf61459f685 | -6.1543 | -59.944 | 2026-09-04 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9e956741-b203-37d5-abb2-6c3d80dad438 | -11.8248 | -46.0448 | 2026-09-04 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 37f47746-ddf3-3ada-a725-eda2aeee6dbb | -13.4191 | -51.4159 | 2026-09-04 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 57c11817-7e6f-3af4-abc8-f7258278620a | -3.7645 | -61.7548 | 2026-09-04 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 2ffd1660-e10f-358c-aba9-1e69b3bd9b30 | -17.0878 | -56.8534 | 2026-09-04 14:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 412c949f-93f8-3095-a26a-bf9b2e9cf253 | -4.6297 | -55.7353 | 2026-09-04 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| db501cdb-0e11-32a8-98f1-88b8041341fb | -13.4096 | -41.892 | 2026-09-04 14:20:00 | GOES-19 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 97.1 |
| d9b00ca6-09be-3e8c-a993-7bbe2c8d4dc6 | -6.6698 | -59.9443 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| dae3f208-0748-3609-a6c2-fbba5c63c8e8 | -5.5793 | -43.9992 | 2026-09-04 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d7fe9db5-215f-3e5b-8a00-51747d023329 | -3.6215 | -60.566 | 2026-09-04 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0d2c2d4e-a6db-33eb-8a4b-61ea36d0869c | -6.6697 | -59.9635 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| fc9b9e14-b821-312d-a389-2f751cc10eb1 | -3.7462 | -61.7552 | 2026-09-04 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 13645fff-88a7-35b9-9080-6e0a2aa091ab | -17.0878 | -56.8534 | 2026-09-04 14:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 817dff53-fc2c-3664-9797-fca770ab8077 | -5.598 | -43.9978 | 2026-09-04 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |
| f868b7c2-aa52-3993-b101-50dda001cc7a | -6.6882 | -59.9628 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 4e948aaa-dc6c-3011-87da-9d34b26f1062 | -17.123 | -55.9194 | 2026-09-04 14:20:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| c6b940ba-5ab5-3b49-b042-80908ba3f8da | -3.7645 | -61.7548 | 2026-09-04 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| cb85fa48-e128-397b-85c3-57e69231e2fa | -6.688 | -60.0012 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 3f69bcab-4838-37f5-801e-3eb99ebccc3e | -10.6166 | -50.4177 | 2026-09-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2ba4bd50-0cab-3c05-a61b-e45f025b6ef8 | -13.7014 | -52.9464 | 2026-09-04 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 770197f3-bab1-388c-8d74-84c3b2647fd2 | -3.3 | -57.8875 | 2026-09-04 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7ee8c18d-66a3-39eb-a7fd-60ad3775a2d8 | -9.8433 | -64.9965 | 2026-09-04 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 11c0dbb8-730a-31b8-890e-6f0e597d8319 | -5.5978 | -44.0209 | 2026-09-04 14:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 8a63a528-172f-31d3-b822-7b7175daf552 | -17.1074 | -56.851 | 2026-09-04 14:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 7ead68f7-806f-3d9b-8993-e69bf3b82082 | -6.6696 | -59.9827 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| bb26d3e6-715f-3e57-b3ff-5ad676d03761 | -10.6169 | -50.3963 | 2026-09-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 4d610fc0-9591-39c5-a573-b7b6c20a49c0 | -6.1543 | -59.944 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d26378ba-fcda-3f83-8dfc-e5b97b7d6104 | -10.4914 | -51.3212 | 2026-09-04 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| db1fa470-8f73-35e5-aa0c-a19e6dd899bc | -6.6883 | -59.9436 | 2026-09-04 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 76e79f4d-ae12-3c63-bbb7-a1da4adf48fb | -3.7828 | -61.7545 | 2026-09-04 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 89727506-269b-3bd2-92a9-94a34ef50940 | -6.688 | -60.0012 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 59871785-50f5-39c4-a257-94d66595cf9d | -3.7645 | -61.7737 | 2026-09-04 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 68f3133b-3f2b-3521-8f20-c2b760bde9e1 | -5.598 | -43.9978 | 2026-09-04 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 37f6d867-7518-385c-8144-d4b4db64a6fa | -17.1427 | -55.9169 | 2026-09-04 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| f7485843-8460-3d11-8b30-da4615b73d14 | -3.6215 | -60.566 | 2026-09-04 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d2ea2404-43f5-39bc-a30a-46b8dc87a83c | -5.5793 | -43.9992 | 2026-09-04 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c606f7df-a772-3564-80b2-174f58c059f4 | -6.6698 | -59.9443 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| beb8c1fd-3355-34ef-9b81-7f6495755655 | -14.098 | -58.8611 | 2026-09-04 14:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 11e60ce1-eb72-3bcf-8060-04fc61bfa093 | -3.7645 | -61.7548 | 2026-09-04 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 4bb8af09-2763-33bd-b6dc-3794c90bfdb1 | -17.0878 | -56.8534 | 2026-09-04 14:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| cdb15387-7dd7-3736-8e5f-d0318caa67ad | -14.5634 | -52.0344 | 2026-09-04 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a7f26183-38d8-36d7-97a7-4d69361388a4 | -6.6882 | -59.9628 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 42ea6abe-7b63-36b5-ae0f-b183421b290e | -5.5978 | -44.0209 | 2026-09-04 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 32dac094-4041-3dc7-93b9-249b2c45f090 | -6.6696 | -59.9827 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 30ef9d11-8db8-3c03-95f2-c75156feb585 | -3.3 | -57.8875 | 2026-09-04 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 728a8cec-3907-38f9-aeaa-f830bb942f5a | -3.7828 | -61.7545 | 2026-09-04 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c775e947-ce25-31ce-a13b-9d88e62eafca | -5.6168 | -43.9965 | 2026-09-04 14:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 311f3a40-3ada-374d-ba64-05dd1bd02fa7 | -6.1543 | -59.944 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 42a57ea7-bd5d-34b8-b554-c6a22e40923e | -4.6297 | -55.7353 | 2026-09-04 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 443617c0-d8e4-30dd-8035-1d462bb7f76b | -4.6669 | -55.635 | 2026-09-04 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| d7dc38f1-b4b5-35f3-bbf3-871a30edbfa1 | -6.6697 | -59.9635 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 5b390f61-72e0-381d-935c-76e6f6fb2f35 | -17.1074 | -56.851 | 2026-09-04 14:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 44d1e64e-a4cb-3d5a-b155-48222bd2e5d1 | -3.3685 | -59.5036 | 2026-09-04 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cb8b84b0-a445-31d7-801e-337156c03bc2 | -3.7462 | -61.7552 | 2026-09-04 14:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0c79aa05-9548-37f5-ad19-80be405d5536 | -13.4005 | -51.3756 | 2026-09-04 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 17993824-7abc-3d55-bd2c-fc4655779a9e | -6.6883 | -59.9436 | 2026-09-04 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |


[Clique aqui para ver as próximas entradas](README44.md)
