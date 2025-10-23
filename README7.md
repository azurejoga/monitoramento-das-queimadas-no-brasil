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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e6f84ac-fd2b-3c39-b095-afd64d5e59b9 | -3.12166 | -49.10193 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c2ab3a-162f-3163-9dec-5fc4cece891f | -3.81198 | -50.77052 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac3f0ddf-232e-3e47-b059-99ff4701a1ad | -3.14935 | -50.16183 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4846981e-1313-3312-b3d8-d90f3ca0fc02 | -5.62116 | -41.11125 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 664e9b71-5af6-3cd3-a6ac-fbccdf30cc9b | -5.68611 | -38.59488 | 2025-10-23 04:06:00 | NOAA-21 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c8b976f7-ccdb-38cb-9a1b-a26c1e0ebbdb | -2.56804 | -49.49986 | 2025-10-23 04:06:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 660b9636-89fd-3842-ba6d-0c0809ffd6a9 | -2.91105 | -48.98151 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fbdb7fa1-f2d2-395f-a0ed-f72508c13027 | -3.24512 | -48.76311 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 122b1dcd-925a-358d-bb29-23f64ddeea75 | -4.18556 | -46.23045 | 2025-10-23 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d97acc34-31f7-37b9-874c-8035a7d367f2 | -3.14935 | -50.16184 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42b2d2b4-0ea1-302c-a356-a42437dc2cf1 | -6.32315 | -43.62814 | 2025-10-23 04:06:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f84d7491-3cee-39ce-8828-f4dcbeb11a18 | -5.69097 | -45.96657 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 27ba3655-e9ee-3cf1-96b0-1dbce5a8aea9 | -2.89879 | -49.17286 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d17d5ede-f71f-37d7-abaf-4c1a74359eb9 | -4.41369 | -42.14069 | 2025-10-23 04:06:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| afc0c746-208c-320b-b6dd-14be6ad2389e | -5.72707 | -38.98263 | 2025-10-23 04:06:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 13d9999d-d745-3669-829a-cd994d93c33a | -5.61901 | -41.12498 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4310fd98-901e-38f2-97e0-6a4a0808406e | -5.32398 | -48.17921 | 2025-10-23 04:06:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 46565083-bf51-32b4-9c86-b21b60b43fc7 | -3.96645 | -43.18908 | 2025-10-23 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdef824c-d44c-3f2f-aee6-5bd521dca0db | -3.02378 | -49.45013 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ca229945-d6d7-337a-86c7-0acf94bb1eba | -5.61955 | -41.12155 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ca6a5d2-1ba0-3908-ad39-5305857594de | -4.33199 | -46.79278 | 2025-10-23 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bbd5def-aace-3435-bdcc-348468988217 | -6.20499 | -43.70692 | 2025-10-23 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ed1e11d-b5f7-35ff-b499-64f201020315 | -5.42802 | -40.88322 | 2025-10-23 04:06:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7927c547-f871-3d6e-b142-f0f520b4e042 | -5.45985 | -40.67958 | 2025-10-23 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a06e43b7-d0b4-3ec3-bf0e-12c36d34efdb | -2.92783 | -48.29999 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a71fa93-ec73-3247-aae0-ffc8a7813592 | -6.32254 | -43.63192 | 2025-10-23 04:06:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b11bec6-d774-3119-a997-64ddc95ea01d | -3.11548 | -45.23632 | 2025-10-23 04:06:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b83477d-62de-303f-886c-87536b89a34c | -3.98823 | -47.88093 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63ff98f5-2241-3374-b00e-7f8946898513 | -5.53877 | -41.3517 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32ac0ee5-0933-332b-b5ad-db1fa526f97c | -3.6995 | -49.56843 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec688986-c4ea-3960-b642-149790aa456d | -3.01908 | -49.47858 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| afcb9c93-f031-3120-b0f7-9a9ef23412d5 | -2.73264 | -48.29049 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 230e157a-b096-325d-a167-28beaafd52a4 | -2.80346 | -51.35171 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18b92e39-b0a3-3c9e-bad0-59c40642847a | -4.68178 | -42.72917 | 2025-10-23 04:06:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab26c94e-3d22-3014-bb3e-1b31393ca056 | -4.91778 | -47.32647 | 2025-10-23 04:06:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bb6bb5-a6fc-3259-989b-4884367ed542 | -2.56804 | -49.49987 | 2025-10-23 04:06:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7743e100-0919-3236-bbec-384f921fb6fe | -3.69663 | -49.56421 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9968c469-bc97-3b8a-b6ad-005a284a8de8 | -2.72456 | -49.56536 | 2025-10-23 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b350ad0-4877-3dbe-b686-1d0345de4b32 | -4.0004 | -43.27997 | 2025-10-23 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3880fdc9-ef5d-377c-9673-45ce9f86f3b8 | -2.81307 | -49.13361 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30321e82-560c-3bba-a060-34cbc5dc9177 | -3.99693 | -43.27943 | 2025-10-23 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b27030bb-86ce-39bd-8ee6-57dba9f04bac | -5.58999 | -40.61161 | 2025-10-23 04:06:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b64e26b4-f276-3da6-aa4b-1270c3078529 | -5.59983 | -47.49765 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88c31026-884d-3b53-8c7b-522850d4cf5a | -2.9271 | -48.30709 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 85640d13-8247-3aed-a78b-1d04a5d7d9ea | -4.28382 | -48.2548 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69dfd381-8684-30d0-bf09-f6cd2fe6ba5c | -2.87273 | -50.71315 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cdc4eb6-b242-31f7-bab7-8f64a8529c63 | -3.22255 | -49.36133 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8033e143-a99e-3848-a38e-e6a0f7fcb236 | -2.85936 | -50.73993 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e92028-3a33-3eb6-94c9-db55dd29e844 | -6.01234 | -45.87281 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b432215d-1f6b-3b2e-a7cb-ebe468b79552 | -2.73288 | -48.29387 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7390137-a20c-3552-91a5-d44a7f549d13 | -4.91343 | -47.32575 | 2025-10-23 04:06:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc8328f-c049-363d-84c7-201fb7c4a448 | -5.79302 | -35.59866 | 2025-10-23 04:06:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8cde8dbb-fde7-345f-8930-82bc3317b929 | -2.8587 | -50.74382 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3c79a5f-3d1f-337d-891c-5a33cc92c4bd | -2.86966 | -50.71372 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f840829d-980f-373c-b685-05775e8dd5b8 | -2.7396 | -48.42849 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aee53d9-c658-311b-9cef-7200ac5161fb | -3.35312 | -40.42328 | 2025-10-23 04:06:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c1a8ce2d-91c4-3069-b61b-97ebf26767a4 | -3.94686 | -46.96729 | 2025-10-23 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97b6daa-868b-3de4-87b6-8b1cbb5f920c | -4.08026 | -38.50559 | 2025-10-23 04:06:00 | NOAA-21 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49bd40bd-1c0e-3e8d-a7c6-8fda58e203b2 | -2.87532 | -50.71461 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff3c102-deca-30c0-a954-e2b24f53797b | -7.20437 | -38.32266 | 2025-10-23 04:06:00 | NOAA-21 | SÃO JOSÉ DE CAIANA | PARAÍBA | Brasil | 2514305 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4042eec-f1aa-31b5-bde9-54db50797a51 | -2.73352 | -48.28523 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8977e0d1-8398-3a63-83f7-a875b7948379 | -3.85193 | -40.73741 | 2025-10-23 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cc88585-4b41-3fab-9430-cd3faa3ed1ca | -3.02429 | -49.47941 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| a5ca3783-404c-3641-beaf-f8a81a9b7fcd | -5.32476 | -48.17446 | 2025-10-23 04:06:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d543812c-edd9-3c86-9687-f14b97e96621 | -5.88715 | -46.28543 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7abce14c-7540-3756-a299-d3484b93453c | -4.64368 | -42.51223 | 2025-10-23 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 32e72522-d8a3-3eff-b64b-25d9da9483aa | -2.24758 | -51.92558 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce9ce6a0-8d56-31ce-bffc-3161d5c6e7e1 | -5.61733 | -41.11417 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58eb8840-398b-35f9-b7bc-ccb71b5faa2d | -3.37045 | -44.39353 | 2025-10-23 04:06:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2abffb34-43e7-30e1-b01d-466e0cb356e3 | -2.85697 | -50.7385 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3ad9bbf-f2b3-323d-bb8c-ba49ecaae40d | -6.32376 | -43.62436 | 2025-10-23 04:06:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2436e6f6-0f6d-39db-b737-aec519a073b2 | -5.31939 | -48.17846 | 2025-10-23 04:06:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1071c660-7204-3f02-a148-3b1fe0344d24 | -3.22769 | -49.36218 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4aabbb-2379-3ea9-a1e4-ea5dfd12b796 | -2.83568 | -48.56308 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c2b5706-bded-3ccf-8edf-8599c285e659 | -5.30099 | -41.15565 | 2025-10-23 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2cd9aebb-b500-3e75-8b77-60011a6c2b5a | -3.01908 | -49.47859 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bb0f9bd1-9088-3000-939e-d889c72b7171 | -5.37083 | -46.86929 | 2025-10-23 04:06:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0448ed94-ae62-3fe9-8a64-b5e2e2f6d1c9 | -3.98718 | -47.88687 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5c4c840-398b-3dfd-987c-0042f81078f2 | -4.93916 | -38.52794 | 2025-10-23 04:06:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6150cd2c-92aa-38b2-95ec-fa9d512f1863 | -5.88957 | -43.20034 | 2025-10-23 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08f9f483-0204-3982-ae9b-ff96953b2c1e | -2.87273 | -50.71314 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eea7a2b-240a-35d1-942f-936c2e542d9c | -2.25428 | -51.91913 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1de0919-61ef-32b4-aeb3-d42f001154ec | -3.66946 | -39.48437 | 2025-10-23 04:06:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 40f48b92-db6c-30ef-8fd0-429e57c51dcb | -3.02898 | -49.48338 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 454a3a19-e038-3d5e-9f93-a39b8035d629 | -2.85633 | -50.74238 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 009b4061-1b45-335b-8504-53d375467bf6 | -3.41598 | -51.43387 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ca5034b-2b66-31b8-a9a2-7b5a5a644633 | -3.81332 | -50.77324 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59f52838-e822-376f-9474-1e54325cba84 | -5.72946 | -38.98281 | 2025-10-23 04:06:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2bb1a595-8ba9-3e6b-b425-81a5d6eeea4e | -6.01393 | -43.32233 | 2025-10-23 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 98c4aba6-b2e7-3790-b677-a82b431bed5e | -6.89741 | -38.27191 | 2025-10-23 04:06:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 09cb19b3-9b3d-3e50-a029-be2ce42f525d | -6.40903 | -39.93317 | 2025-10-23 04:06:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cedd8d69-f71f-3096-8f3c-4cf5e934c856 | -5.20119 | -42.6482 | 2025-10-23 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98b692d5-b44d-3458-ad54-cd279563144b | -5.84974 | -43.64848 | 2025-10-23 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ce44695-3828-3187-861f-5b9e1941b6cd | -2.43272 | -49.26992 | 2025-10-23 04:06:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0826bb07-a58a-3c03-859b-d28cafc23d15 | -4.37722 | -50.35471 | 2025-10-23 04:06:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9d28221-3da3-359c-b19a-0319d75e3e30 | -2.89931 | -49.16982 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cedf7216-8257-38f0-9923-905381e29d0b | -3.25789 | -49.11955 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c914077d-dea6-313f-8446-cd5c83d95d62 | -2.51674 | -44.1782 | 2025-10-23 04:06:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb1f1f0-2f1b-3c8c-86a2-0ff8f3aeb72e | -5.69408 | -45.97225 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c988152-0b8c-3241-b708-52e0065b8ca4 | -2.81819 | -49.13437 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
