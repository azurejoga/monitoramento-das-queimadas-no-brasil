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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e97571f-130e-31b7-8ac5-bc9bc8a0606d | -12.6723 | -54.0395 | 2024-10-04 08:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cc31bffd-a276-3a3b-b32c-ad8f11ee7721 | -16.5726 | -57.2829 | 2024-10-04 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 26fe1945-f83a-3bdc-957e-6b2507d3f58c | -16.6871 | -57.4536 | 2024-10-04 08:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.2 |
| cebd9935-a165-39d6-8519-b2c84563faff | -16.6133 | -57.176 | 2024-10-04 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 71aa0eff-59b5-36af-9755-7dc6962bf901 | -16.613 | -57.1965 | 2024-10-04 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| ec2b02de-0eac-371e-8059-9b797434ec0f | -16.5938 | -57.1783 | 2024-10-04 08:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 910a9ffc-176d-39b6-bd81-cda85cbb735b | -17.011 | -56.7598 | 2024-10-04 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 446bfaae-7d0f-31a2-9876-f76e851c3bc0 | -17.0113 | -56.7392 | 2024-10-04 08:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 99a1fc6a-2661-30e4-a5ba-1e09671c8f4e | -17.1577 | -57.3787 | 2024-10-04 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 3731f889-67e8-376d-bdb7-17d2c559da54 | -17.1574 | -57.3993 | 2024-10-04 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| 728e809c-0475-361c-b7dd-610de7512a2c | -17.1378 | -57.4016 | 2024-10-04 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| edd9bfa5-1f65-32df-90e6-a182f07e8cd8 | -20.5207 | -48.6203 | 2024-10-04 08:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8908d044-8aae-372a-9786-2e28f9e67c0d | -20.5412 | -48.6157 | 2024-10-04 08:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 241f7656-6968-38d1-9e58-e4da2285c7a7 | -12.5898 | -53.1359 | 2024-10-04 08:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 15659712-0880-3cd4-b991-bc71a70d8dfc | -12.5901 | -53.115 | 2024-10-04 08:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| e96c821b-7d48-34e5-8f0b-1292af7805dc | -12.6532 | -54.0415 | 2024-10-04 08:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e1bbd17e-5f30-3451-8e88-d33bf1e1094d | -13.0786 | -51.1385 | 2024-10-04 08:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 41ec7d4f-dd4d-318f-afa7-7b3ad4fd9917 | -13.079 | -51.1171 | 2024-10-04 08:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 40ef67df-5a1a-3ad6-8487-8933848fb693 | -16.5531 | -57.2851 | 2024-10-04 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| ab38c16c-d2ad-3abe-b14f-3ea6a004e200 | -16.5938 | -57.1783 | 2024-10-04 08:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| 7612dfcb-7b93-3471-81fa-30b2ac500306 | -16.5726 | -57.2829 | 2024-10-04 08:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.1 |
| e147c53e-c3bc-3603-a122-47d9294877e9 | -17.0113 | -56.7392 | 2024-10-04 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.8 |
| 42bf3813-8cb7-3868-ab9c-140d9a9e916c | -17.1577 | -57.3787 | 2024-10-04 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 36555184-e0aa-3035-a213-55697fbad53c | -17.1574 | -57.3993 | 2024-10-04 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 4fdfba76-5811-3099-a95f-c6ecc2574a70 | -17.1378 | -57.4016 | 2024-10-04 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| 849fae30-5dbb-3c30-abcb-f4c8771f75da | -11.8242 | -56.6009 | 2024-10-04 08:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e3f91bc4-85bb-3171-aa8b-7d92fc2de528 | -12.5901 | -53.115 | 2024-10-04 08:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 6c53b774-0166-3923-95ff-789a285b118f | -12.6532 | -54.0415 | 2024-10-04 08:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 982c8be1-225e-362a-af3d-c26e42a8d969 | -12.6723 | -54.0395 | 2024-10-04 08:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a117a1c7-5674-358e-a6cf-d1431f1c257a | -16.5531 | -57.2851 | 2024-10-04 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 6f88cef7-a14d-3230-82bf-6607f76384b6 | -16.5726 | -57.2829 | 2024-10-04 08:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| ea2543c5-c66a-368e-9fa0-0c09cd685d87 | -16.5935 | -57.1988 | 2024-10-04 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.5 |
| f8f6df43-759f-32fe-ba17-c81c25e43500 | -16.5938 | -57.1783 | 2024-10-04 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| b7a5a87b-a147-39b6-a17d-fb69854d13e5 | -16.613 | -57.1965 | 2024-10-04 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| bc0b363b-739f-37c2-a618-fca772da90c6 | -16.6133 | -57.176 | 2024-10-04 08:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| fce0d25c-589d-3b55-b3fc-b5bfb93b6696 | -17.1085 | -56.7892 | 2024-10-04 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| fd10a453-c6ac-3130-898f-74f27bca2f05 | -17.1574 | -57.3993 | 2024-10-04 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| ee99070c-2e1e-38d5-a424-adc08211c39f | -17.1577 | -57.3787 | 2024-10-04 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| ebe9c6ab-a037-32c9-b7da-d1f072126263 | -12.6532 | -54.0415 | 2024-10-04 08:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 33fb7ff6-e36a-3745-893d-a679d5644819 | -16.5935 | -57.1988 | 2024-10-04 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 9f3a499c-80eb-37ac-bacc-853fc5375768 | -16.5938 | -57.1783 | 2024-10-04 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| b998d347-3b87-33e8-9f93-d1dfcd0c66c5 | -16.613 | -57.1965 | 2024-10-04 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.0 |
| f8be63f0-cf71-33bd-a48c-60274a98631d | -16.6133 | -57.176 | 2024-10-04 08:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 7ff869df-685e-3263-90c4-0e17c15d51f6 | -17.0113 | -56.7392 | 2024-10-04 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.7 |
| dfe391a0-3989-3d97-a79d-160ea6974f9d | -17.1378 | -57.4016 | 2024-10-04 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 4f65a36f-4ea2-30b0-bd75-70b1159ea8b1 | -17.1574 | -57.3993 | 2024-10-04 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| b2efef51-4f30-3f89-95be-64d41bda83db | -17.1577 | -57.3787 | 2024-10-04 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 58d98251-2f80-3af2-b8c6-acca17c652d6 | -16.5935 | -57.1988 | 2024-10-04 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| e99b0ed0-6d14-3d5b-ac3a-a03c7ea8ab3e | -16.5938 | -57.1783 | 2024-10-04 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| ea76e354-5486-326d-b880-338360e46e6f | -16.613 | -57.1965 | 2024-10-04 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 076fc42b-fe97-35c4-bcc8-9446815ffd33 | -16.6133 | -57.176 | 2024-10-04 08:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 6b110dea-100e-3f1e-a033-324a0b39ec44 | -16.843 | -57.4767 | 2024-10-04 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 761b6d87-c59d-3d5d-bdd4-a1a83245d576 | -16.8433 | -57.4562 | 2024-10-04 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 70b631e5-c86f-3634-957c-a150fc72411e | -17.1574 | -57.3993 | 2024-10-04 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 50701c01-e86a-37b7-a1a2-7a2c90a43e5f | -10.4235 | -50.7355 | 2024-10-04 09:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 47fc9b61-35e7-3c57-b3a2-9876e738f870 | -10.4424 | -50.7336 | 2024-10-04 09:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 526.0 |
| 3801de47-7c93-3eb3-abd4-c354b8b1d837 | -10.4616 | -50.7104 | 2024-10-04 09:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 2f71482e-137e-35cb-9aeb-329ef64dd385 | -10.4427 | -50.7123 | 2024-10-04 09:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 416.6 |
| 12446487-bd6f-33f1-8ca5-5b089873b453 | -10.4613 | -50.7317 | 2024-10-04 09:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 490f11ba-dd51-34e2-84a5-1b4f9f72b807 | -13.1443 | -46.3261 | 2024-10-04 09:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 5061cad6-c78b-35c9-9e8e-02f70c0316e0 | -10.4616 | -50.7104 | 2024-10-04 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 220.1 |
| df929484-8d22-372c-9750-bb74bf8b5767 | -10.4424 | -50.7336 | 2024-10-04 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 434.0 |
| 35f8b554-a663-3ecc-946b-302386aedc51 | -10.4427 | -50.7123 | 2024-10-04 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 361.9 |
| 36c93779-9216-3d71-affa-66df5171c959 | -10.4613 | -50.7317 | 2024-10-04 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 393bc43a-afdf-389b-a270-d51fa978a902 | -13.1443 | -46.3261 | 2024-10-04 09:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 116.6 |
| fbb1803f-a09c-3848-803a-01442dc9d285 | -13.1636 | -46.3231 | 2024-10-04 09:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 5ef29e31-5dfb-3369-9a12-6bb0ede4daea | -10.4427 | -50.7123 | 2024-10-04 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 2a7b5bbf-da55-36e4-a8a5-3cffc496f88c | -10.4424 | -50.7336 | 2024-10-04 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 398.9 |
| 153709fb-63b1-339d-8816-5ae42c5c5d76 | -12.5901 | -53.115 | 2024-10-04 09:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 745b1b5f-586f-317b-9981-36c3b9ba4500 | -21.7988 | -48.3691 | 2024-10-04 09:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 225.5 |
| a41dfcec-b813-3015-8dc9-9cd71287550d | -21.778 | -48.3741 | 2024-10-04 09:37:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f9593bfc-5753-39fa-80ab-1901783ee1fe | -12.5901 | -53.115 | 2024-10-04 09:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c2c7a17f-2e57-3dce-a2aa-a3fd82a10005 | -21.778 | -48.3741 | 2024-10-04 09:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 294.7 |
| 80e2ac7a-679a-3e53-a07d-7df8dc283724 | -21.7988 | -48.3691 | 2024-10-04 09:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 338.1 |
| 1e29b737-4f4f-3ed8-bfee-679919c5d912 | -11.0532 | -46.5344 | 2024-10-04 09:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 98c6b9ac-13fc-3233-825c-178d4f3b0347 | -13.1443 | -46.3261 | 2024-10-04 09:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 30264daf-7b09-3653-971a-f59058acef09 | -21.7988 | -48.3691 | 2024-10-04 09:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 444.3 |
| 013619b0-0c51-33d5-9108-01531264f9e1 | -12.5901 | -53.115 | 2024-10-04 10:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 416a2ac6-dda3-3c64-b41e-74283b806601 | -12.6092 | -53.1129 | 2024-10-04 10:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 1972a054-cc6d-324b-8b7b-af641ca78faa | -13.1443 | -46.3261 | 2024-10-04 10:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 9ddb4bb6-102a-3473-9444-c72d2846a0f2 | -13.1447 | -46.3033 | 2024-10-04 10:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f057b97a-96d8-3202-8891-3f30df55623b | -11.9105 | -50.1447 | 2024-10-04 10:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 04c435c7-eb42-35b4-bae9-0d035640bdfc | -12.5901 | -53.115 | 2024-10-04 10:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 2b885ab3-d441-3467-92aa-f86d1ede5f1f | -13.1443 | -46.3261 | 2024-10-04 10:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| e96caa84-ef1e-3501-b789-00ab3af83e1e | -13.1447 | -46.3033 | 2024-10-04 10:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 54babfef-6f2c-37ff-a105-d042237affc7 | -12.5901 | -53.115 | 2024-10-04 10:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 7327d983-ec50-3e5e-82f3-ff527e1ee076 | -13.1447 | -46.3033 | 2024-10-04 10:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 318554bd-ae06-30a6-a057-f77228f0d721 | -13.1443 | -46.3261 | 2024-10-04 10:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3db7930c-6110-3f1d-a309-ed38c859f43d | -10.4613 | -50.7317 | 2024-10-04 10:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| b0a21d52-05aa-311b-87a4-6b1f3ff7a952 | -13.1443 | -46.3261 | 2024-10-04 10:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 161.2 |
| c489b79a-40fb-342f-9076-6d370850107b | -13.1447 | -46.3033 | 2024-10-04 10:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e7d70838-b7b4-3798-bfae-06af64ae9c40 | -13.1636 | -46.3231 | 2024-10-04 10:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9304b5ed-6ca2-355f-a3c2-c13085bb2029 | -16.5938 | -57.1783 | 2024-10-04 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| dc0f19fb-3d02-3010-872c-ec39dd7f2d9e | -10.2378 | -47.726 | 2024-10-04 10:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3ed63e63-a52f-3ed9-af89-de5a1c7e9100 | -10.4424 | -50.7336 | 2024-10-04 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 266.8 |
| a9001eba-4910-3618-93a1-addeb274c011 | -10.4613 | -50.7317 | 2024-10-04 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| e39c56f5-70dd-34db-9148-171dc9b225bf | -10.4427 | -50.7123 | 2024-10-04 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 60cb5f1b-7188-342f-81dd-48443c05d364 | -10.4616 | -50.7104 | 2024-10-04 10:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4c62b0be-54d3-3dea-ba76-0cd0e51a18f9 | -11.2178 | -46.9622 | 2024-10-04 10:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 78e9c1ee-7bb1-3735-aadd-f711533339cf | -11.2369 | -46.9597 | 2024-10-04 10:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |


[Clique aqui para ver as próximas entradas](README185.md)
