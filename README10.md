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
| 43856ded-c7d0-3926-a866-83296e9bce2c | -15.66746 | -59.75707 | 2024-10-22 01:41:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 24d62c50-9984-303a-8b45-9b7291d27dfe | -14.32269 | -59.34743 | 2024-10-22 01:41:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 24fc9c98-461d-3f73-b09a-4f80ce9e756a | -14.31131 | -59.33051 | 2024-10-22 01:41:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f10466a-c347-344a-b4ff-dbd2c13e3ce5 | -14.27286 | -60.12799 | 2024-10-22 01:41:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b6cdeb88-3a75-33c6-9711-2498911bd180 | -9.7412 | -59.31996 | 2024-10-22 01:43:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 691cc129-bef8-352f-a90b-a695ce77e921 | -9.64614 | -61.92202 | 2024-10-22 01:43:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0834814e-8a8c-32bd-806f-622766848f9a | -9.64482 | -61.91206 | 2024-10-22 01:43:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b556e5e1-eae2-3953-896f-cda2800dc5c3 | -7.82422 | -61.37817 | 2024-10-22 01:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 0e2c9b48-1d99-3ae3-812e-cb878131349e | -7.82297 | -61.36898 | 2024-10-22 01:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b84624cd-3063-30ec-bc0d-85a19743049c | -7.81524 | -61.37944 | 2024-10-22 01:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 86c0edbe-67a0-305f-bcf3-e77860812d70 | -7.81399 | -61.37026 | 2024-10-22 01:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25db4ef7-0310-3054-b19e-5340625f35ee | -7.80383 | -61.56585 | 2024-10-22 01:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 33376024-87d4-34bc-b44c-5a28c57e210a | -11.64057 | -58.61421 | 2024-10-22 01:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 606bf930-cc32-333f-a86d-d4ed53043612 | -11.63928 | -58.60507 | 2024-10-22 01:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b844f0d-1b24-30dc-b0dd-d76fc5c30f4f | -10.83941 | -58.61477 | 2024-10-22 01:43:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1e17617d-78a7-380b-b6b8-3f7b6b14846e | -10.8381 | -58.60561 | 2024-10-22 01:43:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7f019180-4433-336b-b3ab-33000e9bd3ed | -10.43605 | -58.82717 | 2024-10-22 01:43:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d5e43902-5de3-326b-9984-c217b649278a | -2.08725 | -53.24135 | 2024-10-22 01:45:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7d8f7145-7b6a-3871-8c47-773cad9d0cd3 | -2.4824 | -49.1233 | 2024-10-22 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 07faf483-f4dd-37f6-bb5a-c90436db89e0 | -2.4824 | -49.102 | 2024-10-22 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 60cb31b2-835c-33a8-871a-06b7081e64d6 | -2.8482 | -45.4637 | 2024-10-22 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 218332a6-aa08-3c86-84a6-51ec7b83c047 | -2.8668 | -45.4631 | 2024-10-22 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 308a4b1f-6fa4-3723-985f-d6ee766a26b4 | -3.0837 | -51.2708 | 2024-10-22 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 78a208a4-e981-39a6-9c57-c3d1b62e644f | -3.0838 | -51.25 | 2024-10-22 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ae019b41-394f-365f-af7e-4ce737f12ea3 | -3.0917 | -54.1666 | 2024-10-22 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 87871993-7b40-3b2b-9687-42a417095e3d | -3.1101 | -54.1661 | 2024-10-22 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 7be8ad74-19be-3025-91d3-15427d413b09 | -3.9977 | -46.0202 | 2024-10-22 01:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 971ca78b-64c0-37fa-9dc2-809e1b2803db | -4.0163 | -46.0193 | 2024-10-22 01:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3d5f40ca-8f0e-333a-8e57-17e8b8c39cf6 | -5.2305 | -43.1886 | 2024-10-22 01:45:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b0fc9f44-5a41-3e8c-948d-2482fc58e10f | -5.5718 | -44.87 | 2024-10-22 01:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| fbf7d4f7-cae1-3cb4-8084-31f5a6dfabac | -5.5905 | -44.8687 | 2024-10-22 01:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3d3565eb-bcf3-351d-a2ea-ab0bbb6bde8a | -7.8245 | -61.3709 | 2024-10-22 01:45:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d1bed111-82d8-3567-b2e7-0abe4872efbf | -17.0213 | -57.3333 | 2024-10-22 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| b9e79ade-9cad-30bc-9f83-272d90deef00 | -16.945299 | -57.315399 | 2024-10-22 01:54:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b062b069-5632-3ba8-abf8-1680eccdc95d | -16.951 | -57.3363 | 2024-10-22 01:54:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35a275ac-2de0-3d62-89d6-9cf434c3aae3 | -16.956699 | -57.357201 | 2024-10-22 01:54:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d80d38a-06b7-390f-8963-ff76aedb8b61 | -16.947701 | -57.515202 | 2024-10-22 01:54:28 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53996b09-307b-364a-80c8-9c974f2aa9a3 | -16.938101 | -57.518101 | 2024-10-22 01:54:28 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea92c1cd-714e-3583-891a-afef11fec1cf | -16.880501 | -57.535 | 2024-10-22 01:54:29 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ceaedb6-5ab1-3a7f-a9be-f44464c3f9d9 | -16.231899 | -59.1502 | 2024-10-22 01:54:47 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50c6cbc8-8acb-3b1c-aee2-aa73680c2fe7 | -16.0235 | -60.106899 | 2024-10-22 01:54:54 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0faa1af8-0e6e-34fe-b2d7-2e4c583f5a77 | -16.027201 | -60.121101 | 2024-10-22 01:54:54 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fdd70b7-6451-3a4b-a8a6-08d5d8b80cb9 | -16.0308 | -60.1353 | 2024-10-22 01:54:54 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba7d024b-42aa-3633-9525-24a8ba2b2d0b | -16.0175 | -60.123798 | 2024-10-22 01:54:54 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83a80041-38ec-30ae-ba90-58026389eb9f | -1.1834 | -53.6569 | 2024-10-22 01:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7dcf80a1-b618-344c-a6bc-8935db5575cb | -14.2618 | -59.3405 | 2024-10-22 01:55:19 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff85f313-6cb4-3e71-905a-33295e2dcf10 | -2.4824 | -49.102 | 2024-10-22 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 9a6cb916-8172-34ca-848b-1dedfece1729 | -2.4824 | -49.1233 | 2024-10-22 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 7705b94b-f2b8-33e9-a8e2-2a71fedba903 | -2.8668 | -45.4631 | 2024-10-22 01:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b3b1442d-6568-3ea5-990f-029612c5c6eb | -2.8482 | -45.4637 | 2024-10-22 01:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2de4b9fd-7017-333a-9d18-5c981f1d7f7b | -2.9574 | -50.5245 | 2024-10-22 01:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 37d175c2-13ea-3230-92ba-ef0d1d563bbd | -3.1102 | -54.146 | 2024-10-22 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 01cfbdd3-8047-317a-af80-de12ad0ef50e | -3.1101 | -54.1661 | 2024-10-22 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f5b5665d-e2bd-38f1-ad58-8a65067fd3fc | -3.0918 | -54.1465 | 2024-10-22 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ca2dd6ce-b25f-32da-a6fb-f8ce239dfa73 | -3.0917 | -54.1666 | 2024-10-22 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d539e349-ea57-3616-83e6-ff6658f0ab51 | -3.0838 | -51.25 | 2024-10-22 01:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0bfaf75d-3ec8-35c9-9f2f-f7eb9033c9cb | -3.0837 | -51.2708 | 2024-10-22 01:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d67363cc-f18d-3b26-9522-cc93aa9928fa | -4.0163 | -46.0193 | 2024-10-22 01:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 934d8add-fa5c-3e23-8ab0-f5abbafc8942 | -3.9977 | -46.0202 | 2024-10-22 01:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| acbb7ba4-2112-3bde-87bd-f9841bb0a7ad | -5.2305 | -43.1886 | 2024-10-22 01:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b0a44273-505c-354d-835e-b4aba53be8b3 | -5.5905 | -44.8687 | 2024-10-22 01:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 88f9abe8-25cd-3e57-b888-412706f2e475 | -6.2524 | -44.132 | 2024-10-22 01:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| cb792dfe-ec29-388c-91d9-c2339479c551 | -6.2522 | -44.155 | 2024-10-22 01:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 19ed5ede-0c92-341c-a5c6-2aa69db54116 | -6.2336 | -44.1335 | 2024-10-22 01:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| fc3a0458-7555-3760-a94f-801c1764593b | -6.2334 | -44.1565 | 2024-10-22 01:55:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| aea5eeb1-9d70-3858-81a4-0b90b488b8d0 | -7.2028 | -44.7618 | 2024-10-22 01:55:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 39993f81-8a9f-3304-aedd-1a950004a722 | -17.0213 | -57.3333 | 2024-10-22 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 5ea87634-e722-3d9e-aca8-75f2d386589a | -10.1203 | -67.468399 | 2024-10-22 01:57:00 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6f37c842-45c7-3f9c-b2b1-43b2ef438bbc | -10.1219 | -67.475502 | 2024-10-22 01:57:00 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 637d586e-849f-39d5-866d-a0794e544297 | -10.1169 | -68.1838 | 2024-10-22 01:57:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5b3245-f3da-3584-9804-d9259085d34e | -10.1185 | -68.190697 | 2024-10-22 01:57:03 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca1c5b0-561c-3bda-8737-25d4afd2ad39 | -8.899 | -65.9254 | 2024-10-22 01:57:14 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58c0c1b5-5214-3ce7-9b62-91651d6ab6b6 | -8.9009 | -65.933502 | 2024-10-22 01:57:14 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aae35d20-ce69-3fc6-9ec2-859dd73cd2a3 | -7.758 | -61.3689 | 2024-10-22 01:57:15 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 640722bd-d9bf-3efe-aedc-6b22c3df066e | -7.7483 | -61.3713 | 2024-10-22 01:57:15 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d694828-dac5-3a54-afb5-e74abb053be3 | -1.1834 | -53.6569 | 2024-10-22 02:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6dd3bce2-64fb-31f8-a9e7-20b764332e5b | -2.4639 | -49.1237 | 2024-10-22 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d10d8cff-75cd-374d-9f0c-8b459486a6a6 | -2.4824 | -49.1233 | 2024-10-22 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ecf9cc7b-64a1-3850-86fc-173b6b8168f7 | -2.4824 | -49.102 | 2024-10-22 02:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 033112fd-b9c2-3352-beb6-51377bdaee3c | -2.8668 | -45.4631 | 2024-10-22 02:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d1f9c534-59eb-3903-a040-027774862942 | -2.8482 | -45.4637 | 2024-10-22 02:05:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6fc3beb6-47b2-3808-b187-4838aa618d72 | -3.1101 | -54.1661 | 2024-10-22 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 162202cf-12dd-3eaa-b87d-42d2362d8318 | -3.0917 | -54.1666 | 2024-10-22 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ab0afbf6-e14d-3460-ba7a-e8c55c188360 | -3.0838 | -51.25 | 2024-10-22 02:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 09ef7e18-b41a-3cc3-a44c-9de404c86ecc | -3.0837 | -51.2708 | 2024-10-22 02:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7fb2e977-7426-3947-8f2c-522e0c22f227 | -3.0765 | -53.239 | 2024-10-22 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e7b40115-fd64-3aaa-8f57-22747e25c96f | -4.0163 | -46.0193 | 2024-10-22 02:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 743de82a-7981-33ec-a107-07109f3dbe01 | -3.9977 | -46.0202 | 2024-10-22 02:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 97882f38-cbf9-3cbd-9cba-e7996fcdec83 | -4.5574 | -45.7905 | 2024-10-22 02:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 57f9129e-49e3-3ab3-b6cc-5734c2851642 | -4.5572 | -45.8128 | 2024-10-22 02:05:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3232b138-e7cc-3218-a365-6fca2a39a9ad | -5.5905 | -44.8687 | 2024-10-22 02:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 4cf2e8fc-e40d-3c00-8962-f10caa02bca0 | -6.2336 | -44.1335 | 2024-10-22 02:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9f549edb-e1d8-3c59-92c8-61ba059f14a9 | -6.2524 | -44.132 | 2024-10-22 02:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3167c2d9-722f-306a-865c-0208062a06c4 | -1.1834 | -53.6569 | 2024-10-22 02:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7af07d85-af20-3227-b839-962b8faf6053 | -2.4824 | -49.102 | 2024-10-22 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1f3f114c-01d9-32fc-a974-cfd2c9c3616c | -2.4824 | -49.1233 | 2024-10-22 02:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| d4b7fa7d-7d40-3d3c-a24e-6c08b99c25bc | -2.8668 | -45.4631 | 2024-10-22 02:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c10be47-e68f-3697-9300-c7f54f84bb2e | -2.8482 | -45.4637 | 2024-10-22 02:15:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0f5a8b19-8d89-3e2d-a839-54cbc66d7396 | -3.0917 | -54.1666 | 2024-10-22 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 2b1102f9-93f1-3d94-a340-a1d59d0eb5ed | -3.0838 | -51.25 | 2024-10-22 02:15:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |


[Clique aqui para ver as próximas entradas](README11.md)
