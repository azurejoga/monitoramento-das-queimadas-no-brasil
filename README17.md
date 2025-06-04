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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e59878a4-9c65-3353-8869-3e940fc8b555 | -10.29702 | -57.13925 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b301463e-3a27-34da-899b-697953ff382f | -11.5604 | -56.42178 | 2025-06-04 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8fe87fa-9f3e-317c-ae97-1a4388d7cd54 | -11.55476 | -56.42113 | 2025-06-04 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c3d1ceb-df77-321e-9a59-0044a61c757c | -9.371 | -64.4558 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac686c07-8706-3380-b281-8f4d78253f66 | -9.5999 | -63.25558 | 2025-06-04 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5639759e-419d-3460-8ce4-0f845b1b6c04 | -11.90047 | -54.79445 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 658c0a2e-456c-35a1-b1c6-2f4e997bc4f8 | -12.17288 | -64.19927 | 2025-06-04 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe4052f-fe1d-39c6-9da9-1f05d6583cde | -9.6557 | -65.74993 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aea25681-d882-36ad-b16d-5b547990c93c | -11.9163 | -54.8215 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68dc7ff3-45a8-31ea-90e6-87b207ef5739 | -9.96412 | -64.96796 | 2025-06-04 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b498e45-4de8-3416-8ea5-28e6f2294060 | -11.9175 | -54.81157 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b326b953-650b-34ef-b478-28eb76c3c2c1 | -11.9169 | -54.81654 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 848ad48e-fdd6-344a-8f3a-1297a1d2d28b | -11.90502 | -54.78657 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72b11e10-36e0-3eef-b10d-8d53962faadf | -11.80702 | -57.3558 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e392dc9-11d3-3619-8bf1-8a2d25b3c16f | -13.14659 | -56.80987 | 2025-06-04 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74df6c53-f5dc-3e8f-9fa3-7c4c0d8f2708 | -9.61781 | -67.29449 | 2025-06-04 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bed082e9-660f-343c-ae06-e9dc081b8188 | -11.64393 | -58.01587 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 952f4e09-49a9-3a53-b066-332d74c1321c | -12.51518 | -57.18062 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b09f4f7-aeeb-3336-9e12-372117126e3c | -12.17199 | -64.19604 | 2025-06-04 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa8cf759-7a8d-3001-9a71-3bf527a6dd0a | -11.80659 | -57.35916 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b44c284-5466-34f1-838f-ad43c5174768 | -9.79633 | -67.71586 | 2025-06-04 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4df21a22-f444-31a0-a380-1cbbe7153100 | -12.51561 | -57.17704 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 293d873d-95e4-3390-932a-104852c2d478 | -11.55524 | -56.41721 | 2025-06-04 05:42:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a8fe952-29da-3d02-b581-8c44586464cf | -9.24114 | -63.28706 | 2025-06-04 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebac7437-8542-3404-884a-2338c6eee80f | -10.30187 | -57.14321 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 081f6638-ae42-335f-8bef-d73177b72101 | -12.51474 | -57.18423 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa0d199-e153-3abe-969b-1e38290e3f52 | -10.49851 | -53.65717 | 2025-06-04 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9868ec3a-94fb-3482-bfc0-23c1ae751475 | -13.96233 | -56.77919 | 2025-06-04 05:42:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84acd32a-d9be-3492-b7f3-7fc3077f5c40 | -12.64609 | -54.11902 | 2025-06-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb23b0b-7215-3641-ba57-9a8d626edaed | -12.1714 | -64.19996 | 2025-06-04 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89f251c4-6ea8-3e09-9c64-f42a09d44b63 | -9.59635 | -63.2558 | 2025-06-04 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf4803d6-1c52-3ce1-a932-8566ac748ab8 | -8.67456 | -64.26836 | 2025-06-04 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4e07356-b5cb-3735-81e5-e92ee25ec285 | -9.62306 | -62.8102 | 2025-06-04 05:42:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f1f6ea9-e480-3f94-8f7e-c0e4b5a6b025 | -11.82263 | -57.81702 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 395f8afd-2831-3344-b6e3-a75006e5c289 | -10.29659 | -57.14254 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d10d471-d8fe-32d1-8d3b-c08ab600cd11 | -11.90794 | -54.78517 | 2025-06-04 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3016dac7-b642-32ef-8782-1272a278b2c7 | -11.80171 | -57.3551 | 2025-06-04 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9697d915-1342-3dc1-a1cf-a7c6489a2e68 | -10.69504 | -57.64628 | 2025-06-04 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9dd460b-7089-35a5-ad31-9b4a2c577ab8 | -16.39677 | -58.17607 | 2025-06-04 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8b0a2488-463a-3c89-80dc-6f5f76621b12 | -16.39637 | -58.17957 | 2025-06-04 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6ad29093-714a-3360-bc9d-5ba2845a1bc8 | -6.9602 | -42.9052 | 2025-06-04 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| ace389dc-cd97-3868-a59c-888e7df2de9e | -7.0169 | -44.5954 | 2025-06-04 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bdef7e35-77e2-3194-907a-4b8ddd611f60 | -6.9791 | -42.9034 | 2025-06-04 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 4a61a5c2-eefe-3040-8384-97acb7dbfbbf | -6.9602 | -42.9052 | 2025-06-04 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| f6d8a3fc-8a28-3f7f-8c19-404ac25ec294 | -7.0169 | -44.5954 | 2025-06-04 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 495c4481-3c82-38fa-b678-acb611cd3b24 | -6.9602 | -42.9052 | 2025-06-04 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 66c81852-1e43-3a09-aede-66fa6cc1964e | -6.9791 | -42.9034 | 2025-06-04 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 70a1633e-b75e-332f-bb3e-070a0373a9cb | -7.0169 | -44.5954 | 2025-06-04 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 837e89d5-e565-3b59-9355-bb548db4a73d | -6.9602 | -42.9052 | 2025-06-04 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 276f5b9a-79b7-3f9a-8463-a5b093fb692a | -6.9602 | -42.9052 | 2025-06-04 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 9085cbc5-5427-3c17-9714-c0c5be0285bc | -7.0169 | -44.5954 | 2025-06-04 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 02708d14-0248-3da7-a833-39194750726d | -6.9602 | -42.9052 | 2025-06-04 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 5b285266-12d7-3dbf-820d-99c3608fdf30 | -7.0169 | -44.5954 | 2025-06-04 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3ad66d1f-025e-3101-85a3-dd644404dae4 | -6.9791 | -42.9034 | 2025-06-04 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 8a765461-9074-3155-bba0-378ffc45e451 | -6.9602 | -42.9052 | 2025-06-04 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 031dbf0a-6a6d-3e02-8bf7-717734a1840c | -6.9602 | -42.9052 | 2025-06-04 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| b7aa9e24-24cb-39b5-940a-94abfb470a57 | -6.9791 | -42.9034 | 2025-06-04 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 17c080c4-76ee-3f8a-ab6d-93492ce9daa8 | -7.0169 | -44.5954 | 2025-06-04 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 61f653fc-33a1-3c89-8ed5-6c701b4d25c2 | -6.9791 | -42.9034 | 2025-06-04 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| bfcfac35-421f-3bb5-ab7b-17a469bceb06 | -6.9602 | -42.9052 | 2025-06-04 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 98441b3b-b478-3ca8-b5b6-7c0e65e31059 | -7.0169 | -44.5954 | 2025-06-04 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| be63d0da-b208-378f-9876-93c2341e710c | -6.9602 | -42.9052 | 2025-06-04 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| b043a2ab-b532-3073-9a2e-4501e34f54a2 | -6.9791 | -42.9034 | 2025-06-04 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 28e5ba51-80d5-37d2-8c75-7d7a456b14dd | -7.0169 | -44.5954 | 2025-06-04 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4574af5e-3c94-315d-b1a5-d8224b6f5ffc | -6.9791 | -42.9034 | 2025-06-04 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 2b42bad8-627c-369a-af51-ba69ad9c8d28 | -7.0169 | -44.5954 | 2025-06-04 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d74ef57e-f3ed-3500-a846-21926346cf0e | -6.9602 | -42.9052 | 2025-06-04 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| fd57d3da-b24b-384a-9190-08fb04366281 | -7.0169 | -44.5954 | 2025-06-04 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e09ea48f-4194-3729-8c9a-159da412a188 | -6.9791 | -42.9034 | 2025-06-04 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 2463b8d6-1298-3ede-be45-ac210d34b563 | -6.9602 | -42.9052 | 2025-06-04 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| df7daa86-3714-3736-a8c1-b1065b18f106 | -7.0169 | -44.5954 | 2025-06-04 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4dd32337-b53f-3f57-aeb9-b2f95364cda1 | -6.9602 | -42.9052 | 2025-06-04 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| cb8ac8ca-7c5c-3a06-bc41-c9fec16a59cc | -6.9791 | -42.9034 | 2025-06-04 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| a200ad3f-aac3-3901-bce6-c0cfe7a29084 | -6.9791 | -42.9034 | 2025-06-04 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| c5948514-fb97-3d6e-92f1-c8123843b7e9 | -6.9602 | -42.9052 | 2025-06-04 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| f93c87c7-b39c-32db-96c1-498bf6f60831 | -7.0169 | -44.5954 | 2025-06-04 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 13edc824-d14d-3262-ac6c-c98456215028 | -7.0169 | -44.5954 | 2025-06-04 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 25dbea10-1ff9-3f6c-ada9-28ab1fc279ec | -6.9602 | -42.9052 | 2025-06-04 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| bfd98bad-88fb-393d-9610-7129fff5aef3 | -6.9791 | -42.9034 | 2025-06-04 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 3dbba35e-6458-3a70-85b0-6b67af32eb72 | -7.0169 | -44.5954 | 2025-06-04 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 1ccde2e3-fe64-36df-82ed-24ca15a2565f | -19.444 | -54.7708 | 2025-06-04 09:20:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 45.1 |
| e8f54673-89e3-3a21-9576-4cff30dc4f78 | -5.78219 | -43.61915 | 2025-06-04 12:21:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| c212640f-0ca6-3294-8d1d-3897b1c4b793 | -5.78362 | -43.609 | 2025-06-04 12:21:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a2860616-e0ff-3588-8808-9d5b0df09694 | -6.24863 | -43.36579 | 2025-06-04 12:21:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ac4586e2-704a-33cb-8588-0bb522c579a2 | -5.77229 | -43.48275 | 2025-06-04 12:21:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3f6391b1-8a66-362c-8a50-10414e106b32 | -6.22772 | -44.51005 | 2025-06-04 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 568115b9-9145-3c19-9c2d-931aa0dbd1f2 | -6.22905 | -44.50072 | 2025-06-04 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e512a32c-5a60-379e-967c-15a249bba484 | -6.21018 | -43.33306 | 2025-06-04 12:21:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45e6ea46-02ec-30e3-9097-29ccda6d80e3 | -3.9399 | -41.50854 | 2025-06-04 12:21:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9d6e7af0-dde8-368d-bcad-a8c2eb8e6381 | -6.35733 | -43.38675 | 2025-06-04 12:21:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1c0d6c25-2fff-36f5-b15a-2d5ca3ed5f42 | -7.26186 | -47.13434 | 2025-06-04 12:23:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9f06b18-e8ed-3638-939d-4e80f7996796 | -11.91164 | -47.44484 | 2025-06-04 12:23:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 640e33cf-ce41-3602-8cbf-ba63eb128a8a | -10.00408 | -48.48699 | 2025-06-04 12:23:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bbc4d15c-2611-3e5c-81c2-6d9df6d3b97d | -10.61261 | -44.76642 | 2025-06-04 12:23:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7d5f9cb-72f5-3c4d-bf4b-cc38942f9e19 | -6.26756 | -45.72332 | 2025-06-04 12:23:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 76c184ec-5884-37cc-bdcd-8912f3a26f8a | -9.0283 | -49.96803 | 2025-06-04 12:23:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7f0ff28d-c2cb-347f-ad75-8bed8275a162 | -12.09817 | -49.47159 | 2025-06-04 12:23:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8a6ab5e9-3759-304e-9717-1f4ddc4810b7 | -7.01684 | -44.59749 | 2025-06-04 12:23:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8eb21ff4-5859-3f91-a303-51510b950d12 | -9.12422 | -48.64283 | 2025-06-04 12:23:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e3b59247-7b4d-3dab-9010-adcb64017fea | -9.56765 | -46.93728 | 2025-06-04 12:23:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README18.md)
