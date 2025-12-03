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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6688a3d1-6100-33f5-b0b4-c7e4e19ef0b8 | -2.20786 | -48.00731 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0c0a3d2b-511c-3a09-ab95-799930bc37d6 | -2.92423 | -45.46437 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37a1aecc-0c9f-3162-9e41-905f45f76501 | -5.67976 | -47.51793 | 2025-12-03 03:46:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36755df3-f352-30ca-8cd0-2606f8e36e46 | -2.99808 | -41.78459 | 2025-12-03 03:46:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 720df75f-037e-32ca-83fb-e60f0975cb96 | -4.44333 | -37.85407 | 2025-12-03 03:46:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ccd307d-15ae-38b6-9611-84bab4a93067 | -3.85952 | -47.05534 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eddde8cc-abcf-3c19-a636-57c7e1be3df2 | -2.37914 | -49.39515 | 2025-12-03 03:46:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 529b964c-1509-3132-8e76-f817c238b67d | -3.31875 | -42.4984 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55fa60e8-22fe-397b-ae05-4541d5f72f45 | -7.36372 | -38.52244 | 2025-12-03 03:46:00 | NOAA-20 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e171cb5b-d1b4-3b7c-9181-ddd89af3be2d | -2.92294 | -48.23592 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28d97bf9-9b1c-33c9-83da-54598c8576db | -3.31946 | -42.49413 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c425e3c-b934-3198-b5b1-ec70d475356e | -5.85045 | -39.07684 | 2025-12-03 03:46:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bee5cd19-7dc2-3ca3-b0b9-033bcca6b92f | -2.70405 | -49.31816 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2444c36a-fc02-3d21-937b-3640420696f7 | -3.18968 | -41.85857 | 2025-12-03 03:46:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d835f90f-7c2d-3618-aa3d-e568f19bf83c | -5.02915 | -41.01085 | 2025-12-03 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5dc8d00f-426e-3a3e-8896-787dd9547886 | -3.31805 | -42.50268 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df200b7f-f3a2-36db-9ace-4483a0595390 | -2.61835 | -45.14621 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad0fd564-9683-39e5-9f02-1b74ceaa8182 | -5.85312 | -39.94427 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5c7e2a7-cfe9-3092-b6b5-c20993734b55 | -4.45387 | -38.38338 | 2025-12-03 03:46:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6958b75-6dcf-370e-9705-cd121c25c3c6 | -3.84536 | -47.0667 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 934ba934-2d02-352a-bb07-d594e61600c5 | -3.31294 | -42.50628 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea7a552d-b433-3038-a66a-d274e14a0bbe | -4.49788 | -38.45845 | 2025-12-03 03:46:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dced0efd-d658-3745-8d92-2d7819ef7f32 | -2.62265 | -45.14002 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd0383c1-5004-349d-a662-036a4dde90e8 | -3.69817 | -42.14099 | 2025-12-03 03:46:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19827fbf-64e7-3701-9429-39fc8bb51c10 | -5.80167 | -38.13428 | 2025-12-03 03:46:00 | NOAA-20 | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 310cb976-5849-3e0e-ac08-15af76bb4026 | -2.92966 | -45.46528 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d7ef0d-cfac-34a4-8653-e5dad13b2a1e | -3.30781 | -42.50993 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a447b6af-5b5f-30a6-92e4-6644e88a4895 | -3.05036 | -48.42562 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 75e97f6d-f246-3606-9f2b-3d40ea82525a | -5.38226 | -43.11272 | 2025-12-03 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b99f26d-c551-3d7b-8bcd-77a2b682a0be | -3.87199 | -41.58957 | 2025-12-03 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a00f83d6-be58-3b1b-8fa8-951669bdc9fc | -2.57078 | -46.89 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4170a8b-7875-34ba-b9db-6a2530e513a8 | -2.63612 | -48.03761 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d95c4a1a-a73d-388f-aa08-fbdf1516692b | -2.96316 | -48.58748 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d25cbcc-a8c0-3abb-97fb-0ca01811541f | -3.24147 | -50.16102 | 2025-12-03 03:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e2a539a-538c-3c97-bc61-de776bc94b24 | -4.13101 | -42.93524 | 2025-12-03 03:46:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83a2404c-435e-3f95-a46b-4888b94bdeea | -3.44361 | -45.39486 | 2025-12-03 03:46:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e6b26e6-38d7-3262-ac0b-43842d75067a | -2.99873 | -47.90275 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77c9e4fd-8847-38dc-84cf-646b2dcba68f | -2.17209 | -48.37329 | 2025-12-03 03:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53dbb4b8-4d4f-370b-b3f6-a703bab6406f | -4.26781 | -39.54773 | 2025-12-03 03:46:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e15dd048-c020-34a7-997e-1466b8d5958a | -5.91399 | -39.98058 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 92f52747-c9a5-3f1f-b5d7-383cd55d0748 | -2.63521 | -48.04303 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b414eb8e-77dd-3fb4-bbed-f1dd9a17f2f1 | -3.77369 | -50.13767 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2e0b9da-eb8d-3c8d-adca-1fe55ef5bb55 | -3.62817 | -48.90026 | 2025-12-03 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76a3816f-20cc-3a95-8f82-f2d9f7b54ea9 | -3.19033 | -41.85461 | 2025-12-03 03:46:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0cd92237-dab5-3331-98c5-5875629ab928 | -2.84805 | -46.73371 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7d6b6371-bb58-3842-8909-edd48d36fd9d | -3.04411 | -48.42779 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 15d3c3b8-13a6-3dc4-967d-c24a95cf6d75 | -2.85323 | -46.73905 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7194056a-7245-3ca3-9c76-153898c2e093 | -5.89949 | -39.88801 | 2025-12-03 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c14856e4-34ca-3c63-bdb5-b182a90aba23 | -2.82568 | -48.45166 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7714569d-6946-3650-894d-88647884a871 | -4.28368 | -43.76717 | 2025-12-03 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5dbcec66-651c-3be2-9602-d6a4a5e83ad1 | -3.11452 | -40.99508 | 2025-12-03 03:46:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 016752b1-be81-3a00-bb14-0172e4f419a1 | -7.48428 | -34.90123 | 2025-12-03 03:46:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d99d8fc-cc42-3a7b-ac3c-d8f1aa81c26c | -2.62422 | -45.14383 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3afaac7-36cc-38f3-a290-3c98775fb325 | -6.90127 | -39.55075 | 2025-12-03 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8ec0a9eb-a635-321d-8b13-69c157c3b16e | -2.91646 | -48.23485 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 607a70d8-a738-3513-889e-d9e827608d27 | -2.69715 | -49.31688 | 2025-12-03 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8742aac9-edaf-3e17-b91f-90a415dcf9f4 | -2.62153 | -45.14665 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b384645e-2b06-398f-ae7b-aee1855746ce | -2.61889 | -45.14288 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1b037a23-9d29-3899-8968-abecc03f7c6f | -7.33252 | -35.06775 | 2025-12-03 03:46:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ca44e42c-b592-3667-bc26-4ebd2b905412 | -3.21197 | -48.61728 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08c9ba99-77c5-30db-8c3d-5c5767e2ad55 | -3.33885 | -44.33764 | 2025-12-03 03:46:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dd76c975-c792-34d6-99b8-a402f7b67726 | -3.6315 | -49.48841 | 2025-12-03 03:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9361ed21-d0a1-33dd-9be1-19b7e7fdd2bb | -3.23502 | -45.56838 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e4b05d76-8431-3acb-a942-b3d03974b8e2 | -3.2173 | -48.61493 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 415e96f8-706c-351b-9c75-076058f5ab7a | -5.68642 | -47.51489 | 2025-12-03 03:46:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 858fd62b-7db3-3b12-ab8e-1bf5bbe0c9dd | -2.78626 | -47.43886 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52377065-e946-31b7-9f91-ed2d484e9801 | -4.13027 | -42.93969 | 2025-12-03 03:46:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 294595c9-a509-3d33-aa09-ac0cf3caf93a | -2.78847 | -47.43116 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4e64e17-b9c4-34fa-a6ed-9990f98ec8c7 | -3.02363 | -44.80744 | 2025-12-03 03:46:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67b19ee2-e990-3162-849f-30b88175d986 | -2.16777 | -48.36998 | 2025-12-03 03:46:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a85007b-a711-3b34-8c86-fd3215617bb5 | -3.24046 | -45.56926 | 2025-12-03 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 925b877d-64fe-30ec-8a34-10ac41788699 | -3.23443 | -45.57188 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 789330ef-59e8-3a2a-8322-b86de57ba433 | -3.85208 | -47.06317 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7360aaaa-b980-3ab9-894b-2c1ba2504c91 | -4.40315 | -41.45417 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e9ea845-a571-3f72-b22e-5ff29c911f24 | -3.23928 | -45.57629 | 2025-12-03 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b5006a35-6042-344e-9624-1bae57c2d7be | -3.85281 | -47.05888 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b85022f4-a528-34b8-ae61-2f0c9739717b | -2.78389 | -47.42036 | 2025-12-03 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f346952-e42a-3732-b33f-feccd838049c | -5.86288 | -39.11038 | 2025-12-03 03:46:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba3449ca-acb0-3ff6-a80a-6e1b667370ba | -3.21806 | -45.53648 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc6b37eb-73a8-3e94-8a2c-9de8e2257aa5 | -2.85252 | -46.7433 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 08c624b6-2147-30f4-81ff-57eaf43217ec | -3.7695 | -50.13839 | 2025-12-03 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ff24ac-6dac-37a1-8807-4d59b1b9d9bc | -3.2356 | -45.56489 | 2025-12-03 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d643d056-c48a-3140-8ac0-ac50cdb4209e | -5.02951 | -41.01306 | 2025-12-03 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 99579cb0-5a8c-3b88-a104-61f958fc82ff | -2.61676 | -45.1424 | 2025-12-03 03:46:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7dc48c3b-3b1c-3d54-9813-611f4ff58014 | -3.31734 | -42.50698 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a55a8ef-d4f1-32f8-b6e8-d80412a37099 | -2.57234 | -46.88075 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f027cb4-d037-3697-b5fe-44f82f1b375a | -3.30853 | -42.50558 | 2025-12-03 03:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bbd0d8a-cb60-3f13-98c4-f2789b28b301 | -3.43825 | -45.39392 | 2025-12-03 03:46:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18820803-86c2-3afb-b808-6ecac9c2a33d | -3.0231 | -44.81056 | 2025-12-03 03:46:00 | NOAA-20 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38eadc21-e75b-351b-aee5-7bb4f102106d | -3.21856 | -48.61844 | 2025-12-03 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26f24d8c-727a-3406-87a2-dc56e0217b39 | -3.21747 | -45.53998 | 2025-12-03 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fff747c5-a2a5-364c-a419-4714efed8822 | -5.7983 | -38.13374 | 2025-12-03 03:46:00 | NOAA-20 | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef69f1b2-aa6b-397c-8a62-1dd7cf5bb239 | -3.05063 | -48.42905 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a2d6e261-2d88-3e4a-bb37-95844b8a5010 | -7.48024 | -34.90451 | 2025-12-03 03:46:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2a6b885e-c269-3701-8f58-06ce92792be9 | -3.22265 | -46.87478 | 2025-12-03 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf3999d5-5d29-3e64-a331-5eafa3b6cd6e | -7.22668 | -37.22837 | 2025-12-03 03:46:00 | NOAA-20 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d5bf782d-3125-33b5-8ad8-99fd7418134f | -3.86259 | -40.64597 | 2025-12-03 03:46:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a9688c2b-c63f-388e-8b40-e28363b573b2 | -5.03222 | -41.01659 | 2025-12-03 03:46:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8d8d3ef1-c8ff-32fd-9979-bad119c82160 | -3.84685 | -47.05802 | 2025-12-03 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 282d787f-590f-30d6-8789-73e66416d343 | -2.20878 | -48.00182 | 2025-12-03 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README7.md)
