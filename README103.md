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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc69bd4c-fdae-3b4d-a2ee-c2ef15117dcd | -17.21711 | -57.23183 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 9b66ec0a-4d43-33ef-85c3-3f02889cf65a | -17.04306 | -57.43488 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8d911523-0600-38a0-9b3e-4842824fb5a7 | -16.87968 | -57.67087 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cd1f1d28-68b2-3b1d-aa42-af88641cc6a6 | -17.21854 | -57.22143 | 2024-10-26 06:08:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| f55e6e90-5750-3517-96c2-bbbf40d5a4cd | -17.2467 | -57.49812 | 2024-10-26 06:08:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 927ae952-9f66-32fc-9aa5-cb5fc26935a3 | -15.66886 | -59.76288 | 2024-10-26 06:08:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5de28423-f7dc-370b-bd57-70d6db73463f | -16.09467 | -60.11994 | 2024-10-26 06:08:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2253e11d-1776-3579-b066-c4fbb896c45c | -17.0148 | -55.99746 | 2024-10-26 06:08:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 16c24632-3a04-393a-8784-29ef0680e8c5 | 4.33905 | -60.22424 | 2024-10-26 06:22:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d961a8c1-3063-3735-bb75-77b1626f5cdb | 4.33798 | -60.21816 | 2024-10-26 06:22:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a933e689-e555-3001-97d8-3cf6bb43ae75 | 4.33568 | -60.22235 | 2024-10-26 06:22:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06511169-13aa-302e-b068-84e056930d37 | 4.33456 | -60.21621 | 2024-10-26 06:22:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b35e655-28dd-3dc5-9855-b4ec78f3f4c5 | -9.44859 | -70.60359 | 2024-10-26 06:25:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b46f5e8-a2a9-380e-9711-10ebfc47f6c5 | -8.28094 | -72.67245 | 2024-10-26 06:25:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23e90322-26d6-3d4a-b34e-3d0a46df075b | -7.82402 | -72.78107 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c91cf1b-fc66-3337-bd97-7622a61b157d | -7.82334 | -72.78565 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 04547f9e-7816-3f32-aa8d-b2d28146b675 | -7.82025 | -72.78054 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da02852b-9cc2-3910-8f5f-995b85a3ffc6 | -7.81957 | -72.78511 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| be1da7f0-5020-3a04-ad50-a9c4c58d3e10 | -7.74916 | -72.79322 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac157dc6-aa88-3376-ae48-b7964bd53abf | -7.74831 | -72.79532 | 2024-10-26 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9008db70-76ee-3c77-939a-b1c7f8a9c842 | -7.39423 | -72.65518 | 2024-10-26 06:25:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a6f0ce6-556f-340b-8efd-63e0926d01f7 | -7.39046 | -72.6546 | 2024-10-26 06:25:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b3f2c2-8e83-3152-a7d4-2560cd6dcc82 | -7.36455 | -72.85493 | 2024-10-26 06:25:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee0b9c7e-9b42-3a21-8cd0-8740b3da8eb4 | -7.33825 | -72.80046 | 2024-10-26 06:25:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30fccdb2-eced-3794-b932-08633c68b76b | -17.7446 | -57.5344 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| e55f2fe1-28af-3ddf-a2df-4168ddd45cf3 | -17.745 | -57.5138 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 9232500a-8852-316d-b08e-1219f9b4047a | -17.7868 | -57.3649 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| cce221cf-f928-315c-845a-ee0ecd3866b7 | -17.7872 | -57.3443 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 7754fa0e-015b-34f7-a253-7c9c0484ca6f | -17.7875 | -57.3237 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| d1b31d01-0e7d-3bf1-a6ef-93a1c55f7377 | -17.7443 | -57.555 | 2024-10-26 07:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 612aec3b-acde-364c-92cc-ae9f0d76d1cd | -18.0827 | -57.3696 | 2024-10-26 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 572d38cb-1c5f-38f3-9b7f-fe8e34403516 | -18.0629 | -57.3721 | 2024-10-26 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| a898607b-b541-3b31-ba84-37c260f667aa | -17.7443 | -57.555 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 4847ee90-41ee-3402-8a61-cc07cccc860d | -17.7446 | -57.5344 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| f5e78cf0-ab6d-3030-a96b-c0270d99e1cd | -17.745 | -57.5138 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| d42b67dd-baec-3ccf-a0ec-8679d138288b | -17.7674 | -57.3467 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| f7820e40-1cf4-3821-b122-ea9014dc2243 | -17.7872 | -57.3443 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| bc978c8a-96f7-3f65-ab70-bea2ac504392 | -17.7875 | -57.3237 | 2024-10-26 07:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| e9ddf716-0224-3e7e-981a-9c6e02aab25a | -17.9418 | -57.531 | 2024-10-26 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 1ad7ed5d-9b0a-32de-80da-bc832f45b5f7 | -17.9415 | -57.5516 | 2024-10-26 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 36f2d349-b7f1-3645-8c23-14af121cb33f | -17.922 | -57.5334 | 2024-10-26 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 455a9d8b-3fe6-3229-983c-66300c96292f | -17.9217 | -57.554 | 2024-10-26 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 025e5274-b902-34ff-90c7-637f91a7ad57 | -18.0629 | -57.3721 | 2024-10-26 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| c0db2ec3-cfe7-3270-b6c3-0eacd34e8706 | -18.0827 | -57.3696 | 2024-10-26 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.4 |
| adc0b31d-1e2f-3929-8693-981d13111aa1 | -16.9792 | -57.5223 | 2024-10-26 07:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 0d6818ff-db22-3f93-8824-3358e2cdfcb6 | -17.7875 | -57.3237 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 221050f7-2dbd-3ac9-8c58-a2124de90d1b | -17.7872 | -57.3443 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 6d333924-cd56-3764-86ad-24e8bbb52f70 | -17.7868 | -57.3649 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 90c722c5-1ff2-320f-863c-e64e46ef8c57 | -17.7674 | -57.3467 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 262268a8-9d0b-3bf2-b88b-02815794759e | -17.745 | -57.5138 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| a7a242e0-51c4-30b1-8312-49ded65e0626 | -17.7443 | -57.555 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 02ab7ff0-692b-3d6b-85da-2a73b53e0726 | -17.7446 | -57.5344 | 2024-10-26 07:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 2a700b38-9b85-3bb7-bf6c-8614f97521a7 | -17.9418 | -57.531 | 2024-10-26 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| c99f7c3f-90f5-36f7-be2f-52d9408ae027 | -17.9415 | -57.5516 | 2024-10-26 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| fd3f553b-10ff-3bd7-aca2-8c196bae4b8c | -18.0827 | -57.3696 | 2024-10-26 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| a95535ea-c3ab-37e6-bbc2-8ca10ee5c890 | -18.0629 | -57.3721 | 2024-10-26 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.3 |
| ccf8e4e4-af93-300f-8e4e-9d41a2155693 | -16.9792 | -57.5223 | 2024-10-26 07:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| fd899d10-b8da-3827-b010-aae8d268b8c9 | -17.7875 | -57.3237 | 2024-10-26 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 366537b7-96a7-39df-896b-1a3fcc768ffc | -17.7872 | -57.3443 | 2024-10-26 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 9ba7b2b2-b86c-3d2b-8813-73e0e2875f7d | -17.745 | -57.5138 | 2024-10-26 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| d9fcb968-e849-3689-8b1f-0986fef5ff17 | -17.7446 | -57.5344 | 2024-10-26 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| ffbe91d4-ff8c-30d6-a3b7-340a7e526614 | -17.7443 | -57.555 | 2024-10-26 07:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 6986d374-1928-3021-9b70-e0ea62436cdf | -18.083 | -57.3489 | 2024-10-26 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 186c3416-f0de-38c6-8f15-c70bd5446ba9 | -18.0827 | -57.3696 | 2024-10-26 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.8 |
| f95b3671-221c-3f78-9092-b5593d8a1350 | -18.0629 | -57.3721 | 2024-10-26 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 165579ee-410f-3b5e-ac0a-8f225aad4956 | -16.9792 | -57.5223 | 2024-10-26 07:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 79211820-720b-3025-a1c3-4e54573141cf | -18.0629 | -57.3721 | 2024-10-26 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 8f4efd17-925d-3189-8055-30571aee1040 | -18.0827 | -57.3696 | 2024-10-26 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| de904f5c-de7d-3872-ba6a-dba39134cb74 | -18.083 | -57.3489 | 2024-10-26 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 886d1cb0-7f34-34c5-a901-4ce13028eaa5 | -18.1025 | -57.3671 | 2024-10-26 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| ba0d84c5-8396-3b3f-87b9-d3f6ad1dbd2a | -16.9792 | -57.5223 | 2024-10-26 08:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 0c566495-63f1-3ef0-bb5d-6afa69dc085a | -17.843 | -57.5431 | 2024-10-26 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| abc374f6-42c0-3961-8247-5740888d9c08 | -18.0827 | -57.3696 | 2024-10-26 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 2e63b06a-dffd-3aad-af98-fce43524b3d0 | -5.33666 | -35.67155 | 2024-10-26 11:51:00 | TERRA_M-M | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c071fe3e-9b71-386d-9ae0-11f21edf5489 | -3.66917 | -42.38581 | 2024-10-26 11:51:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 494a5289-6800-380d-8250-38a81df57f8b | -3.66749 | -42.40822 | 2024-10-26 11:51:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 5e531e04-769b-3503-9abf-7ddedcf46fce | -3.66461 | -42.41497 | 2024-10-26 11:51:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 32cd59be-64a6-321b-8b76-5e06e6793620 | -3.48252 | -43.31411 | 2024-10-26 11:51:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 9dbbffe4-92bb-34d0-9684-d43633698eda | -3.47722 | -43.34864 | 2024-10-26 11:51:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 13e18b67-089b-376b-9393-7e705e7a3fc5 | -8.9585 | -40.73827 | 2024-10-26 11:53:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 52bcc4b9-22d8-3098-9a23-256959ebb00b | -8.68101 | -41.13533 | 2024-10-26 11:53:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 27.5 |
| d0002b2b-c862-3a2f-8893-2eb9031bf8a2 | -8.67148 | -41.11485 | 2024-10-26 11:53:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 45.4 |
| d1445327-9576-3154-95ca-ed6e7abe1f79 | -8.66851 | -41.1334 | 2024-10-26 11:53:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 79c554d0-534f-37d6-a4a5-3cd77d641058 | -8.35507 | -36.84721 | 2024-10-26 11:53:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1ef8da3f-e641-3616-897b-2562c47ee18d | -8.19765 | -38.71364 | 2024-10-26 11:53:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| cd1596d7-7252-349b-a4d2-7a787e2836be | -8.04957 | -38.7562 | 2024-10-26 11:53:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| de5e3920-6eb0-3a67-a0a5-152806d8eb8a | -8.03909 | -38.75456 | 2024-10-26 11:53:00 | TERRA_M-M | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 27.8 |
| dc1d1d4b-89fa-3018-900f-2587e3805039 | -7.98512 | -37.63194 | 2024-10-26 11:53:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 56f96fa8-a0c6-3bae-8d07-33504f75f298 | -7.96702 | -37.601 | 2024-10-26 11:53:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 25.6 |
| beb51e4b-78f4-3df1-97ec-9c801c62c66d | -7.96458 | -38.4321 | 2024-10-26 11:53:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 4d0b3dd9-d5c8-3cc4-be1c-afbb24859c71 | -7.94453 | -37.89681 | 2024-10-26 11:53:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 3b6c6eca-30d7-35f5-bf50-26fbf2af3968 | -7.78634 | -37.24762 | 2024-10-26 11:53:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 56ce13f3-f2f9-373a-a29b-f389398aa952 | -7.74306 | -38.0741 | 2024-10-26 11:53:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 60c7ad0b-41ba-3690-af5e-df86abcd9367 | -7.6778 | -37.96429 | 2024-10-26 11:53:00 | TERRA_M-M | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 56b9c6de-2b79-3dff-ba17-28e12bb488dd | -7.46201 | -39.51448 | 2024-10-26 11:53:00 | TERRA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 77acb3e7-b4bb-3d2b-98c2-48fb64a71d92 | -7.1289 | -42.52657 | 2024-10-26 11:53:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 5a0447a1-9c45-3d3c-b9e0-ff72e9168163 | -7.12692 | -42.51913 | 2024-10-26 11:53:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 179.2 |
| 8d682014-20a9-3341-b322-ba9f4ea40e9d | -6.12295 | -42.50983 | 2024-10-26 11:53:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 233.5 |
| c58bed22-f4d2-3972-8830-2b3dc4a2a9ef | -6.11776 | -42.53111 | 2024-10-26 11:53:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 26af92c4-67c7-3e32-91c6-58fc5438ccbf | -7.30776 | -44.97413 | 2024-10-26 11:53:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |


[Clique aqui para ver as próximas entradas](README104.md)
