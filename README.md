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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b6e81ce-4622-37cb-9711-544124f618c0 | 3.0364 | -60.7473 | 2025-01-23 00:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 343f5758-e2e9-31da-96f3-f3dd1abc1463 | 1.3221 | -60.0463 | 2025-01-23 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 176.9 |
| e2aeaed5-3f71-30b2-86b1-879a6ffcc04f | 1.3403 | -60.0461 | 2025-01-23 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ea7a4a3c-bf20-37af-aa35-71ef152e20d8 | -21.194 | -49.3887 | 2025-01-23 00:00:00 | GOES-16 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| ccd77be6-df55-3b0a-8c79-47bfdce46e99 | 1.3221 | -60.0272 | 2025-01-23 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 0cb29c52-acfc-388f-9871-c19df7c172e2 | 1.3403 | -60.0271 | 2025-01-23 00:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 43b46e65-3c25-30c0-992e-9dcd44d00c8d | 1.3403 | -60.0271 | 2025-01-23 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e7bf81fd-ab5e-3383-bc30-b247d4912f4e | 1.3403 | -60.0461 | 2025-01-23 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 9409b0c4-9c8f-3adb-b943-0b6493ed3819 | 1.3221 | -60.0463 | 2025-01-23 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 23ebfcc3-fbf3-322e-98c5-1f758c654723 | 1.3221 | -60.0272 | 2025-01-23 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 93d91641-f84b-3733-9b08-e2118d72ee73 | 3.0364 | -60.7473 | 2025-01-23 00:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 41cbd9e5-8688-3868-a41a-ce0c5dc9a047 | 1.3403 | -60.0271 | 2025-01-23 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 357adf96-0157-37b8-9b81-72523a6614b3 | 1.3221 | -60.0463 | 2025-01-23 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 97793d48-41b9-3d07-b1f0-4a105871e577 | 1.3221 | -60.0272 | 2025-01-23 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 47cf46a1-537f-3e8c-8b03-975122ce6108 | 1.3403 | -60.0461 | 2025-01-23 00:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5b6a8e89-bc75-3d1b-b68b-a5c7bf49dae8 | 1.3403 | -60.0271 | 2025-01-23 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e9c5a30a-d51d-3ce2-acd4-7ac77542023f | 1.3403 | -60.0461 | 2025-01-23 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| da4b541f-43c6-3112-8153-dddbc8d90427 | 1.3221 | -60.0463 | 2025-01-23 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c74de48a-b1c9-3bb6-bec4-cdfd3d9b97d6 | 1.3221 | -60.0272 | 2025-01-23 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f0fe0c16-f47e-3542-af29-e8fb35a628b7 | 1.3221 | -60.0463 | 2025-01-23 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.4 |
| f50c0647-ec83-301a-88ce-d295ba0bb2aa | 1.3221 | -60.0272 | 2025-01-23 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 48908ef6-3bc8-3cf1-9856-9c90629ad500 | 1.3403 | -60.0461 | 2025-01-23 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3de3f8fb-d094-3971-a650-883a1af928e0 | 1.3221 | -60.0272 | 2025-01-23 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5385990f-7f5a-368f-9070-ec6dc2e1d0e9 | 1.3403 | -60.0271 | 2025-01-23 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f23016fb-7856-3330-8b95-adb7cad91267 | 1.3403 | -60.0461 | 2025-01-23 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.3 |
| bac1b9a4-0de8-32f4-8669-b0c0a6f1a2d7 | 1.3221 | -60.0463 | 2025-01-23 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dd697bba-9e71-36e4-905b-714b368f7a1d | 1.3221 | -60.0463 | 2025-01-23 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 665fbda8-bab4-39ab-8e11-fe6d9a71518b | 1.3403 | -60.0461 | 2025-01-23 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 351897b7-e9f0-3870-9b27-c5d3b31c0581 | 1.3221 | -60.0272 | 2025-01-23 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 0b0ac5c2-d550-3191-a905-814d4b4fa53c | 1.3221 | -60.0463 | 2025-01-23 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0085b6d4-8994-3e63-a4bd-e09220d89f85 | 1.3403 | -60.0461 | 2025-01-23 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9b008907-967e-395f-b714-7c239b73f51f | 1.3221 | -60.0272 | 2025-01-23 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fab24752-80fc-3838-9d03-59306aaacb16 | -30.02458 | -51.56785 | 2025-01-23 01:11:00 | TERRA_M-M | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| a28f0252-a43c-3ad2-9191-3679632e11bc | -27.56899 | -50.76221 | 2025-01-23 01:13:00 | TERRA_M-M | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e6486ce5-428d-3676-8406-0247b7fb85a7 | -27.56758 | -50.75228 | 2025-01-23 01:13:00 | TERRA_M-M | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 29ecac20-bfaa-34b7-a9d5-f56ce989614d | -19.81339 | -53.79153 | 2025-01-23 01:15:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 25bb9df2-497b-3be0-92f2-b92190147b85 | -19.81468 | -53.80109 | 2025-01-23 01:15:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 40068e68-5989-35a7-875c-81852e717a58 | -20.69308 | -55.42665 | 2025-01-23 01:15:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1350466e-06fd-3b9e-9063-a9cd22bb6ab6 | -19.72971 | -54.83103 | 2025-01-23 01:15:00 | TERRA_M-M | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15589797-808a-39b3-8920-221d308acbe2 | -16.43867 | -55.73857 | 2025-01-23 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 43f3893c-6fea-392c-90ae-ef9318463123 | -16.43999 | -55.74883 | 2025-01-23 01:17:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 2b73749e-0010-3c68-b658-779931830e3b | -18.95309 | -53.68876 | 2025-01-23 01:17:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a48f4afd-3cac-3c00-89e4-dcd4bbb1f04f | 1.3221 | -60.0272 | 2025-01-23 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 813feb09-902b-3ed8-a160-80de861a535a | 1.3403 | -60.0461 | 2025-01-23 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4807ac5b-7f1f-3935-a141-1325cbe5ed4f | 1.3221 | -60.0463 | 2025-01-23 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 481d34f0-a254-3698-b8ac-ff281fed6d8d | 4.35832 | -60.31147 | 2025-01-23 01:21:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| febbc05b-7eb5-37f0-93f5-e5c762b7cf4f | 1.05455 | -59.89833 | 2025-01-23 01:21:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1534f038-a3ae-3860-87b9-d727107f202c | 1.33537 | -60.03671 | 2025-01-23 01:21:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6832b102-7b26-3e93-b23c-fba5f28b3c28 | 0.69284 | -60.29849 | 2025-01-23 01:21:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2b477042-9939-36ae-9208-641f8a8fb401 | 1.33386 | -60.04729 | 2025-01-23 01:21:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| da708848-7ccb-3075-896d-1dacbc6d3c45 | 1.32426 | -60.04598 | 2025-01-23 01:21:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 8b15bcc9-12d3-3051-89bd-00af4159ccbc | 3.04339 | -60.7575 | 2025-01-23 01:21:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 37f5a8b1-08ce-3667-98f8-21b537408109 | 1.32577 | -60.03545 | 2025-01-23 01:21:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 28e42760-9591-3d06-afb6-929da7885373 | 1.05311 | -59.90871 | 2025-01-23 01:21:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e719b4f-255e-3eae-a8f8-d843fda73f1e | 1.01177 | -60.43596 | 2025-01-23 01:21:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 46fc3531-0cd1-3c29-a51b-6df271a8f330 | 1.3403 | -60.0271 | 2025-01-23 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 998f428d-ffb9-32dd-953f-0813c14eb5d6 | 1.3221 | -60.0272 | 2025-01-23 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 7ed3f3a8-0ba4-3fe5-90f6-03f531ece1d6 | 1.3221 | -60.0463 | 2025-01-23 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ba6eebb7-c417-3bcc-b207-cb4ab2aa1196 | 1.3403 | -60.0461 | 2025-01-23 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f5313e15-b958-3d4b-a391-25417ca3c03e | 1.3403 | -60.0461 | 2025-01-23 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 17d403c3-a3a7-3d98-a311-c3d93cb97254 | 1.3221 | -60.0463 | 2025-01-23 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.8 |
| fd9aa292-ae23-3111-be50-e985f62d4bcd | 1.3221 | -60.0272 | 2025-01-23 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9fb33f1d-ff97-35eb-9454-0b939b0841df | 1.3403 | -60.0271 | 2025-01-23 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c64cac35-10cc-3254-a4a0-a83dba016172 | 1.3403 | -60.0461 | 2025-01-23 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 84f4f62a-2a75-3643-b198-57f93bd15cbe | 1.3221 | -60.0272 | 2025-01-23 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 44d99b5f-c9c8-39fb-a744-580537a382b1 | 1.3403 | -60.0271 | 2025-01-23 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5ec2c81b-c5c9-31a3-a3a1-a88398bd45f3 | 1.3221 | -60.0463 | 2025-01-23 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f8d050a0-036f-3574-96bc-22198df6bf08 | 1.3403 | -60.0461 | 2025-01-23 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 7c50af6c-aa9a-3765-9ec5-823ed25bf57d | 1.3221 | -60.0463 | 2025-01-23 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 24c01e4d-bb2a-3c8a-a604-56668bb4f1af | 1.3403 | -60.0461 | 2025-01-23 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5b1deb65-9a3a-3e1a-8d54-3e6c89399252 | 1.3221 | -60.0463 | 2025-01-23 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e9f674d3-92ac-38d9-9f6d-849050ea01ed | -6.7885 | -35.1885 | 2025-01-23 02:20:00 | GOES-16 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| ff60405b-47aa-3daf-88bb-b2f91b4e6180 | 1.3221 | -60.0463 | 2025-01-23 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 57f82436-8054-39f4-b70c-b3654b9d7736 | 1.3221 | -60.0463 | 2025-01-23 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1f9d8dfa-5df5-36cf-8e29-d7e0e866da8e | 1.3403 | -60.0461 | 2025-01-23 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7a6d37c4-1288-37fb-8258-85e6eb9fa515 | 1.3221 | -60.0463 | 2025-01-23 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 99a0a885-f507-3c2f-bad8-7ed2e83990f4 | 1.3403 | -60.0461 | 2025-01-23 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 016d24c3-4f82-37cd-9081-cefa4b914a9e | -8.36403 | -35.30712 | 2025-01-23 02:47:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a649bc8a-ede9-3c8c-9957-d410af6a7fd8 | 1.3403 | -60.0461 | 2025-01-23 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ca0ffb36-ea82-3393-8ca4-3277c24cf529 | 1.3221 | -60.0463 | 2025-01-23 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 7301565f-bf06-30d6-ba01-1cd05d5c8151 | 1.3221 | -60.0463 | 2025-01-23 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 09f90777-954f-3710-a51c-565d5edcd49c | 1.3221 | -60.0463 | 2025-01-23 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 8ecc0907-d9d0-326d-a42c-bafb2d0a6ba8 | 1.3403 | -60.0461 | 2025-01-23 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5d6f4732-4cd1-3205-b160-81e3c185ccc5 | -6.07191 | -35.26045 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7543cbf8-4e74-300d-b8d9-795531361cfa | -6.07678 | -35.26156 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eebe240c-935c-3746-bc00-8afbc3f15682 | -6.07096 | -35.26586 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7bd3fdac-83d8-3264-96ae-f533770c0fb0 | -6.07372 | -35.2706 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 68e078ad-1b54-3103-ae2d-777ff610641c | -6.07486 | -35.27246 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 84be15e4-002b-388b-96b8-9a2c948ae760 | -6.07464 | -35.26515 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8eeab612-a750-3db5-af56-e4dfd65df94f | -6.06976 | -35.26403 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 17d5e850-50e4-33d2-ab3d-d5d7795d5655 | -6.07582 | -35.26702 | 2025-01-23 03:10:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 147247bf-79a2-3f61-996a-955615bf124e | -8.88383 | -35.40696 | 2025-01-23 03:12:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 9fb724e1-c44f-3e87-a3d8-e380cc07dac5 | -6.77887 | -35.17219 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ea653bdd-af9f-39a8-9970-730f531019ed | -6.80294 | -35.17681 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5890c335-ac3d-3d68-afe1-df4635ca62ff | -8.3668 | -35.30804 | 2025-01-23 03:12:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f53ca4e0-913c-3b06-9b37-7f1c5e8767db | -8.88293 | -35.41201 | 2025-01-23 03:12:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 31ca6821-188f-361e-9206-57c88aa50961 | -7.96736 | -35.23864 | 2025-01-23 03:12:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c8084cb-d143-3867-be17-b4f34dd22523 | -7.96263 | -35.2377 | 2025-01-23 03:12:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e104714-cb0e-3e4f-9d86-30edebf92eda | -10.35282 | -38.71447 | 2025-01-23 03:12:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 649f1ace-f5e4-3066-a23f-de442195f810 | -6.79723 | -35.18111 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |


[Clique aqui para ver as próximas entradas](README2.md)
