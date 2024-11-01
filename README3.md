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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba54a917-8d4d-3239-8bad-cb4d06f1c7d0 | -3.50731 | -40.75885 | 2024-11-01 00:13:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 71d85b6a-8c23-30a4-820e-5a290039cab8 | -3.50147 | -40.75556 | 2024-11-01 00:13:00 | TERRA_M-M | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 04cfaae9-0264-3960-ae4d-d0b6ae54c9e1 | -3.40107 | -41.64459 | 2024-11-01 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b54d8624-50d9-3d8d-b201-9175b7cd4803 | -3.39111 | -41.64601 | 2024-11-01 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| da5bae84-80ca-34b8-92d0-059ce48187af | -3.03724 | -40.07103 | 2024-11-01 00:13:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e90722f6-875c-3b83-b308-f105fe8225a9 | -2.9597 | -40.24184 | 2024-11-01 00:13:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 1680e6ec-d4f1-361c-b986-59d5d7953214 | -2.88554 | -39.90855 | 2024-11-01 00:13:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c5c3c5c0-691e-3d84-89ac-18b717daa082 | -6.04943 | -45.81034 | 2024-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 75fd2254-72a5-3dbd-9b2d-79f9c0174460 | -5.33483 | -45.11256 | 2024-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| c3bef0dd-abae-3b32-95f9-5de5d0d8aa65 | -0.6896 | -51.6847 | 2024-11-01 00:15:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ad1c19d0-6710-3b4e-995e-084c21f28db7 | -0.7915 | -63.0797 | 2024-11-01 00:15:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| b7970c59-2673-344c-a47f-a97f66ce494a | -1.2292 | -47.7516 | 2024-11-01 00:15:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| dd2de57b-2187-354b-b5df-8a94b38a2c96 | -1.2292 | -47.7299 | 2024-11-01 00:15:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f21c7a45-d6d4-3641-a226-7670aea1dd4b | -1.2477 | -47.7297 | 2024-11-01 00:15:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0eed31d6-49fb-3496-8454-7b851f2fb62c | -1.4244 | -52.2118 | 2024-11-01 00:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7586b241-36ff-32e9-8769-3f6ad3027663 | -1.847 | -52.3285 | 2024-11-01 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2e13ff38-61ba-3837-a1de-85e458cd8f10 | -1.8471 | -52.308 | 2024-11-01 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 4cf2ebf6-43e8-34ee-8fa7-f226a87cdaf6 | -1.8654 | -52.3282 | 2024-11-01 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8fcee09c-5c29-3402-a6d5-c7f713559ab4 | -1.8654 | -52.3077 | 2024-11-01 00:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c028c447-e5f8-33ce-b744-6a862ec51956 | -2.1695 | -48.7252 | 2024-11-01 00:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b9855903-b59b-35b5-936d-8a80900a0bf2 | -2.3545 | -48.678 | 2024-11-01 00:15:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 62683676-f351-3a7c-b9e2-350b2d912be6 | -3.0891 | -45.5896 | 2024-11-01 00:15:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8913a006-3d8f-3e9c-acfe-b4366f88c39c | -3.0893 | -45.5672 | 2024-11-01 00:15:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 418.5 |
| b9132faf-167f-3100-9184-dff8ca2a1a57 | -3.0894 | -45.5448 | 2024-11-01 00:15:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| e6643ee5-f227-33d7-822f-d6c8560adb08 | -3.0734 | -54.167 | 2024-11-01 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1801de51-c729-3583-a6ba-27129d0c9353 | -3.1078 | -45.5665 | 2024-11-01 00:15:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 240.0 |
| 81a69aad-d8c4-3a93-bd59-f086f2b7f4da | -3.1079 | -45.544 | 2024-11-01 00:15:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4a7f8f73-183e-3021-9790-22dfb1e5f464 | -3.132 | -44.3891 | 2024-11-01 00:15:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 96a7dd26-0801-37bc-96d0-b35514f0390e | -3.1281 | -54.266 | 2024-11-01 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 685842cc-9305-3198-9000-cddf8491de5b | -3.2535 | -50.3479 | 2024-11-01 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e37a8883-bcbc-3384-b570-c9e4e27a2738 | -3.5297 | -50.5274 | 2024-11-01 00:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f50ead4e-fcb0-35c8-9bf2-5906daf67f8d | -3.5631 | -47.3847 | 2024-11-01 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 4f972870-3507-3108-8dd0-e3be908a580f | -3.5632 | -47.3629 | 2024-11-01 00:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 95228e95-461e-3005-8673-7088b0f0d36b | -3.7703 | -43.5323 | 2024-11-01 00:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3ac4bba7-32a0-379f-9fb3-5d3c3c1a13a7 | -4.2977 | -45.6475 | 2024-11-01 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 18a589ff-c9ea-3060-9640-ccdc1ddff631 | -4.2978 | -45.6251 | 2024-11-01 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 124.6 |
| d452268b-78ae-3348-aa0c-f08e4bf966b4 | -4.3163 | -45.6466 | 2024-11-01 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 7349f219-1596-378d-8a59-10fbac7faaeb | -4.3164 | -45.6241 | 2024-11-01 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 0ad11c3a-6c40-3ff0-953e-5c1a16609382 | -4.3166 | -45.6017 | 2024-11-01 00:15:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 705ac019-6922-3f94-8fb6-cd6986015f5c | -4.3867 | -43.4757 | 2024-11-01 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 410.8 |
| 5b3bbe3a-b311-3d61-b704-a3a9f41230e9 | -4.3869 | -43.4525 | 2024-11-01 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 935e8d96-492b-3326-b547-80500afc7e37 | -4.4054 | -43.4746 | 2024-11-01 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| a33e9ab1-7d13-3a8a-b7ac-5297ba0ef830 | -4.4056 | -43.4514 | 2024-11-01 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 900d68e3-a360-3057-8d0f-686a654ebc0b | -5.097 | -48.4617 | 2024-11-01 00:15:35 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 00c2d2b9-fc37-3c3f-87c1-24f89aeb3048 | -5.0971 | -48.4401 | 2024-11-01 00:15:35 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| dd72b085-7a45-3946-97bf-ca10505a7faa | -6.1231 | -43.9347 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f1149143-cd6d-3971-872e-691ad182619d | -6.1039 | -43.9824 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a6201b5f-e279-394b-9457-2ecdace11b10 | -6.1041 | -43.9593 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| ba574c31-7731-3830-9021-c9d6a5f1850b | -6.1043 | -43.9362 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7f678de0-901f-37a3-8b1e-ee2be7e513da | -6.1226 | -43.9809 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6e1977ae-ee78-3dc8-abf8-c9c8e186bbd7 | -6.1229 | -43.9578 | 2024-11-01 00:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 2ab55dc6-8ed8-3829-8ad1-411aebf9a02a | -6.0496 | -45.8072 | 2024-11-01 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f0ab2f11-f5fe-3f10-bad5-3b0d3b38d116 | -6.0498 | -45.7847 | 2024-11-01 00:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4cbaf51b-66a0-34bc-9aa1-e57555d6b526 | -1.23064 | -47.73934 | 2024-11-01 00:16:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 73087f19-cb5f-35df-a137-03bba818adbe | -1.23551 | -47.74392 | 2024-11-01 00:16:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| c6653974-2d75-3747-99dc-61c481d69a30 | -1.24623 | -47.73711 | 2024-11-01 00:16:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d460f73a-8f22-3247-b2e2-5f2a7276a169 | -10.6819 | -65.002 | 2024-11-01 00:16:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1e50bdcf-907b-3bf6-a7eb-33336a6ee61d | -10.682 | -64.9831 | 2024-11-01 00:16:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ab90c479-1646-38ac-a5ab-fd8b7d872ad6 | -10.9811 | -45.1104 | 2024-11-01 00:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6b1acc40-75a9-38ed-94d4-25b80005ff8e | -12.4593 | -63.1512 | 2024-11-01 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 680b57b2-4a72-3b5b-b238-364e064970dd | -12.4594 | -63.132 | 2024-11-01 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| be45b63a-d20a-3bc0-a8e8-faf2ba31f38d | -16.9008 | -57.5313 | 2024-11-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| e2b7e95d-6ebe-3991-9aec-1017df989b5a | -16.9012 | -57.5108 | 2024-11-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 67f27a25-92ab-332a-9ebe-fc69cba50102 | -16.9204 | -57.5291 | 2024-11-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| f486b110-ec98-3327-aa9a-3a7573a53296 | -16.9207 | -57.5086 | 2024-11-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| aa093f8d-b1de-3c81-ab06-f447f1be2402 | -17.6664 | -57.5028 | 2024-11-01 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| f848dc0d-e142-3520-a0e0-9f06d57e9ee4 | -17.6667 | -57.4822 | 2024-11-01 00:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| b956874e-c1ca-3d23-8163-e7cc339871e8 | -17.7249 | -57.5368 | 2024-11-01 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 57a62198-0be5-3bd2-ac89-c6966c62d1fa | -1.2292 | -47.7299 | 2024-11-01 00:25:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 324bee9b-8302-3bd7-8a06-2e3a79ff1ec7 | -1.2477 | -47.7514 | 2024-11-01 00:25:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6d71af27-5029-3c72-ab45-d06a4783ed0c | -1.2477 | -47.7297 | 2024-11-01 00:25:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8ce49d9a-bb39-3a79-b923-62801514edf1 | -1.8471 | -52.308 | 2024-11-01 00:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8a1a91f4-087a-3206-9798-c0837563c956 | -1.8654 | -52.3282 | 2024-11-01 00:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bdebe75c-ccb6-3cfb-bfaf-2c00678f7f2a | -1.8654 | -52.3077 | 2024-11-01 00:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e8151b0b-0112-38fc-b630-70f9f9ced670 | -2.1695 | -48.7252 | 2024-11-01 00:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ebba603b-db22-3732-98f3-ec673006abf7 | -2.3545 | -48.678 | 2024-11-01 00:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7145fb85-4f7a-35cb-a637-5313ab1d97dd | -2.6062 | -45.5839 | 2024-11-01 00:25:21 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fabce8cb-ab12-319f-a38a-0251efbb0de4 | -3.055 | -54.1675 | 2024-11-01 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 87c32e55-aa4b-3e92-b235-fb0c8b950393 | -3.0893 | -45.5672 | 2024-11-01 00:25:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 9ca201fd-a0fa-3c03-835b-33d5ec587fa3 | -3.0734 | -54.167 | 2024-11-01 00:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e02bf15e-a759-35e0-bf08-cefc3bb00e25 | -3.1078 | -45.5665 | 2024-11-01 00:25:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |
| cd8749cb-69db-3709-8682-1b6a4a691207 | -3.1281 | -54.266 | 2024-11-01 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8346a149-d723-3644-b659-6d79c32afc91 | -3.3572 | -44.0591 | 2024-11-01 00:25:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 03ecee66-72ee-3ae0-9933-5c312383cf19 | -3.5631 | -47.3847 | 2024-11-01 00:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 90ec417e-b373-34dc-8269-ec684f7f8b68 | -3.7703 | -43.5323 | 2024-11-01 00:25:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bceeb8c1-034c-3439-923e-a4130e1d6b98 | -3.8143 | -48.9943 | 2024-11-01 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f7086a07-a08c-3cf5-9200-f41f0b936d3e | -3.8144 | -48.9729 | 2024-11-01 00:25:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 0c6b48a3-38fe-3cf3-b500-12f372e8c991 | -4.2978 | -45.6251 | 2024-11-01 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b0f90af9-1109-30b2-b641-9d89c0bea2e1 | -4.3163 | -45.6466 | 2024-11-01 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1857cfc8-228e-3403-b042-c038d3a58f6c | -4.3164 | -45.6241 | 2024-11-01 00:25:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 9c5a5d7d-d8d0-3a45-8caa-dbbb60c964ca | -4.3867 | -43.4757 | 2024-11-01 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.0 |
| ddddc8d5-f608-364b-b002-da27ed96d6bf | -4.3869 | -43.4525 | 2024-11-01 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 7b3676f7-dfd1-3130-bcad-48aaa09ea017 | -4.4053 | -43.4978 | 2024-11-01 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 77255331-55ec-33f8-b4bb-a20b990fa561 | -4.4054 | -43.4746 | 2024-11-01 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 286.3 |
| 419ef51e-e498-3530-bb89-96cd8580a826 | -4.4056 | -43.4514 | 2024-11-01 00:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| a79e5503-3926-35d9-9d06-0c74d614c2f0 | -6.0496 | -45.8072 | 2024-11-01 00:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 64b41bc8-8777-366c-917e-1e7145bdbf78 | -10.682 | -64.9831 | 2024-11-01 00:26:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1d1aeb4c-02ec-3118-be95-bc9bcece83fb | -10.6819 | -65.002 | 2024-11-01 00:26:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0baea6b5-eff9-3209-86fd-b0dbcd910f7c | -10.9811 | -45.1104 | 2024-11-01 00:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| badbc8b6-6226-327d-b337-71f7a1946c62 | -12.4593 | -63.1512 | 2024-11-01 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |


[Clique aqui para ver as próximas entradas](README4.md)
