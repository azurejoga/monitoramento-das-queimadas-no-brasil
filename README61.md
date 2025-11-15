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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a24dda2-1545-312e-8679-d7f1a900f01d | -4.3621 | -44.353 | 2025-11-15 12:50:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5207eb46-6e7b-378c-9b4c-c637f0a376bd | -3.9895 | -44.2813 | 2025-11-15 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 571f7a56-5091-303b-bb95-577dba991087 | -4.0524 | -40.3975 | 2025-11-15 13:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 84.1 |
| ef3bc65d-10e9-38da-93af-9c5ca552f4c4 | -3.8196 | -44.655 | 2025-11-15 13:00:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 6f84f8fb-f77a-336c-8037-0deab36bb487 | -6.1233 | -48.0532 | 2025-11-15 13:00:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 283.0 |
| 52d43abe-4a34-31ed-be81-2a06ac3eaaf8 | -7.1129 | -42.7254 | 2025-11-15 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 7b9ad71b-e7aa-30be-a600-ac126aa64df9 | -7.4917 | -42.5689 | 2025-11-15 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 6f3571a8-08db-3850-8de4-81f008e5fc7d | -6.1608 | -48.0289 | 2025-11-15 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| e69f7851-9307-3d01-bdd8-a0a23e86427b | -6.7339 | -42.9498 | 2025-11-15 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| efb4f5b5-a1e5-3b6d-a985-569219dbdb60 | -7.1126 | -42.749 | 2025-11-15 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 0ba61a4c-312c-31d9-a581-a0cc307e44ff | -3.2756 | -45.4702 | 2025-11-15 13:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8c12143d-ca19-3d3e-ac31-57ba7e676a00 | -7.492 | -42.5452 | 2025-11-15 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| c4161102-d465-321f-83ce-0bbd61cc2f45 | -3.9895 | -44.2813 | 2025-11-15 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5fc94f12-d23f-386e-bfd5-00b387b55015 | -7.9792 | -38.6285 | 2025-11-15 13:00:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 150.8 |
| e7033c6e-0bd1-3e15-8907-f42342c9d7fc | -6.1421 | -48.0302 | 2025-11-15 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 311.7 |
| 4fc1d7d9-2701-3022-9f63-303bce39ffa1 | -3.9897 | -44.2584 | 2025-11-15 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 87acc728-c22e-36ef-9ec1-2c7abcdc922c | -5.5127 | -40.9765 | 2025-11-15 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| dff27d20-02fd-346c-89bc-e74f6448130c | -4.0083 | -44.2575 | 2025-11-15 13:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 685588ed-72d4-313c-8bbd-05dbcc66df1d | -2.7121 | -46.9772 | 2025-11-15 13:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4eb67ce3-594a-39d8-88d9-06a75e048288 | -3.9897 | -44.2584 | 2025-11-15 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| d22462e0-09fb-380f-9f38-c1f5808eff07 | -5.5127 | -40.9765 | 2025-11-15 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 9bde7a9a-21ee-3342-8eeb-c9317db19d4e | -5.5316 | -40.975 | 2025-11-15 13:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| dec4bfb2-f035-3738-b5aa-5f643560eafe | -3.59 | -42.4421 | 2025-11-15 13:10:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 190.6 |
| 5899b37f-929d-354f-9f6a-584dce27e572 | -7.4328 | -42.7644 | 2025-11-15 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| e3ba85c1-ae2e-3a2f-b041-2b6a8d189c19 | -7.492 | -42.5452 | 2025-11-15 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 7ed33b3a-9dc6-3a40-a5ee-4c384e653953 | -3.9895 | -44.2813 | 2025-11-15 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 71e017fd-6769-305a-91f5-6316e48b6fa4 | -7.4517 | -42.7624 | 2025-11-15 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 04d2d82c-ffaa-31c8-9465-c12ab6071496 | -6.1233 | -48.0532 | 2025-11-15 13:10:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 485.9 |
| 372dd5c0-aa7f-3556-8b16-a1441722f40e | -7.9792 | -38.6285 | 2025-11-15 13:10:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 162.7 |
| f8a1f8c4-dc02-3144-9421-0865f16f546e | -6.1421 | -48.0302 | 2025-11-15 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 400.9 |
| d4101b6a-edc7-30cf-bc32-9cb269a49fcc | -7.1129 | -42.7254 | 2025-11-15 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 58b32dd1-6493-359f-8fc8-8f8f3711d3d3 | -4.0083 | -44.2575 | 2025-11-15 13:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| ce23374f-3d02-3155-8e84-c42bfe7006e2 | -7.4917 | -42.5689 | 2025-11-15 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| b398c24d-a73e-3510-a093-70faa6d70b49 | -6.7339 | -42.9498 | 2025-11-15 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 63a3ed6b-30ef-3ef7-a00c-13d50384b8df | -7.442 | -45.2184 | 2025-11-15 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 931d670b-6c88-3321-aea6-af524c7890a9 | -7.9789 | -38.6541 | 2025-11-15 13:10:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 121.2 |
| ae96ea95-49d4-3f2a-b1cc-c1a3cb96fcc5 | -6.1608 | -48.0289 | 2025-11-15 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6164a026-5d52-3003-8333-8f2d3ae28bfe | -7.4417 | -45.2411 | 2025-11-15 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b45a8fc3-50cc-3235-a876-2307b90a4a20 | -7.4328 | -42.7644 | 2025-11-15 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| bf186a07-b90c-33e5-83de-9a32848505d5 | -3.8196 | -44.655 | 2025-11-15 13:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4b4413ec-5faa-32e8-953f-48e170b39da2 | -3.59 | -42.4421 | 2025-11-15 13:20:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| c98df6e4-cb47-3cf5-9248-eee7f8eb75d5 | -6.0496 | -45.8072 | 2025-11-15 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 686a1db9-6970-3e61-8657-888644b75eda | -7.4917 | -42.5689 | 2025-11-15 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| f4f69dd8-ec03-3963-8453-f8c36b7073e8 | -3.9897 | -44.2584 | 2025-11-15 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 46397b2b-ffb5-37fa-9ecd-66b58d786432 | -7.442 | -45.2184 | 2025-11-15 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 6626b69a-7806-3f9d-965c-0e423ea0f528 | -5.5127 | -40.9765 | 2025-11-15 13:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 322ccc07-e254-32f1-8abe-bb27a455e810 | -8.1781 | -45.0103 | 2025-11-15 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| a6112c39-03a6-308c-99ab-f6df46ec9c64 | -7.6149 | -46.552 | 2025-11-15 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| c17f23cb-06ae-3825-964c-3eb824010e18 | -4.0083 | -44.2575 | 2025-11-15 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 27f55572-fc9a-3c33-870a-2cb40f4b8897 | -6.1233 | -48.0532 | 2025-11-15 13:20:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 432.2 |
| 5294e28f-3c94-37ab-83a6-0e5259d9b024 | -7.492 | -42.5452 | 2025-11-15 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| dfc334c2-934d-3b70-bd14-f3a503d8df19 | -4.105 | -50.0436 | 2025-11-15 13:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 73ad2d32-8e23-3526-a621-71c7f73115fa | -8.1778 | -45.0332 | 2025-11-15 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 337.4 |
| d5f9e3cb-259b-32c8-9ae1-bada7ae7cde1 | -6.7339 | -42.9498 | 2025-11-15 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| b4f24d4a-357a-3011-ae0d-e5544a341545 | -6.1421 | -48.0302 | 2025-11-15 13:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 236.2 |
| e80af0c9-c468-3cf2-af28-9fb70849bb06 | -7.1129 | -42.7254 | 2025-11-15 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| d55083d5-5f09-38f2-ac5b-bf7ed2a4cfe0 | -3.5088 | -40.3549 | 2025-11-15 13:20:00 | GOES-19 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 142.4 |
| 33e3c2f9-6d22-3211-841a-f0ce9988ee12 | -4.1235 | -50.0428 | 2025-11-15 13:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b7fe72a7-33da-38f3-b58a-48802e723667 | -8.1967 | -45.0312 | 2025-11-15 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 88ed8719-2f98-3afa-b761-b0caab12bdf4 | -7.4417 | -45.2411 | 2025-11-15 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8ea9f10b-b02f-35b3-bcde-f8b0e3c7d8a9 | -4.2641 | -42.2871 | 2025-11-15 13:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 5c5a6d2a-76d7-35ae-bb99-23f2b849d8f6 | -7.9792 | -38.6285 | 2025-11-15 13:20:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 164.0 |
| 8534ea38-8eb8-33b2-8f2f-94d486ff45ba | -8.159 | -45.0351 | 2025-11-15 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 1916b212-311f-31d2-a45a-d75d9b04104a | -7.4517 | -42.7624 | 2025-11-15 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 139.0 |
| 74add22b-84a3-3ed3-8c58-f4d272a14fc5 | -4.1739 | -39.1754 | 2025-11-15 13:20:00 | GOES-19 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 81031c92-5c7c-3fdf-92ba-23fedddf1a56 | -3.9895 | -44.2813 | 2025-11-15 13:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 5987c0e9-4101-3269-9846-63ed7612f441 | -7.9789 | -38.6541 | 2025-11-15 13:20:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 114.0 |
| f516b9e1-b695-39f7-8c09-ca06c80bf3c1 | -8.6623 | -45.4834 | 2025-11-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 69e2f1ed-725d-3966-bc43-7c4f6aab373a | -7.9792 | -38.6285 | 2025-11-15 13:30:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 221.9 |
| 3dafe342-014c-39f3-a8b2-1f5feeecf6ae | -7.6149 | -46.552 | 2025-11-15 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c50e48ce-8908-3de4-b968-b47f14c6112d | -4.4246 | -43.4038 | 2025-11-15 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0d92f8f9-5658-3d9e-ad83-e00da6e48477 | -8.662 | -45.5061 | 2025-11-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 1da8e9c3-12a4-3983-824d-9b802db3e8a3 | -7.442 | -45.2184 | 2025-11-15 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| e62bf59b-fe54-3b0e-8286-a28fca2c20f9 | -8.1967 | -45.0312 | 2025-11-15 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 533fa737-db27-3e8b-881b-41edbb9c978a | -3.9897 | -44.2584 | 2025-11-15 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| a2aed5f4-2113-39f2-84f8-13370fae60d1 | -4.552 | -38.9481 | 2025-11-15 13:30:00 | GOES-19 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 115.0 |
| f54e78cd-a0cd-3c13-98a5-bf74ca89b191 | -8.7543 | -45.655 | 2025-11-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cea2e9d7-6164-3a16-a040-c15e5cf70f32 | -8.159 | -45.0351 | 2025-11-15 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 197.3 |
| d5d41c4f-7a30-355c-99f2-a4209699f5d3 | -6.411 | -41.4793 | 2025-11-15 13:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 9db6f32b-b32f-3ff5-a1c9-9e8fdee29cda | -7.4517 | -42.7624 | 2025-11-15 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 7d76409f-c46f-3023-a865-a6f8242333e7 | -8.6808 | -45.5041 | 2025-11-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 3c63dec2-49e1-34b2-ab5b-292f4670ef46 | -6.1421 | -48.0302 | 2025-11-15 13:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 253.7 |
| b09a087f-b0dd-3c41-b077-743f7ee9c066 | -3.6696 | -44.8212 | 2025-11-15 13:30:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| eb307371-0e4d-3fb5-a5d2-1e5c680d22eb | -6.7339 | -42.9498 | 2025-11-15 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 1c30232d-49eb-3466-b1fb-f65f46c0e197 | -3.59 | -42.4421 | 2025-11-15 13:30:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 159.9 |
| 63383c78-7fdd-31b3-bb57-2c86e0ec228d | -7.4417 | -45.2411 | 2025-11-15 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 07f6096d-ffb4-37ae-9424-925398b64382 | -8.7355 | -45.657 | 2025-11-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 86166fb4-3e0f-3b3c-80ad-57dbd9f4831c | -8.1778 | -45.0332 | 2025-11-15 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 288.0 |
| 83977b7d-f744-3c11-9d8b-c3879e92cf1d | -7.492 | -42.5452 | 2025-11-15 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 9ed855a9-5954-39f5-b7a7-6a4677214b36 | -7.4328 | -42.7644 | 2025-11-15 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 243.6 |
| 8eda681a-0088-32c2-a127-c6a128c61d44 | -7.3868 | -48.6545 | 2025-11-15 13:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 8ac57360-5ba8-306d-b074-063884c0791b | -8.5795 | -46.0568 | 2025-11-15 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 8166f92a-b2ad-35af-a9c1-fc7811415a62 | -6.1233 | -48.0532 | 2025-11-15 13:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 783.6 |
| 14d78223-547e-349d-ac2d-1ec7c72c75b3 | -7.9789 | -38.6541 | 2025-11-15 13:30:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 5d31313e-56d2-32f8-b76d-72bdc6731b3f | -7.4517 | -42.7624 | 2025-11-15 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 171.7 |
| 765f5af6-3da5-3ad5-886e-7fd2e1f31d85 | -4.552 | -38.9481 | 2025-11-15 13:40:00 | GOES-19 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 17cab545-188d-36fc-adb2-916fe901b4ec | -5.5127 | -40.9765 | 2025-11-15 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 89c80a2a-e44c-3da3-a83a-473de179fb9c | -8.159 | -45.0351 | 2025-11-15 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 88823e84-4e99-3a92-8b95-c65d498a10ba | -8.6808 | -45.5041 | 2025-11-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 34495e5c-9153-3761-95a0-4ac7b2a733d3 | -7.387 | -48.6328 | 2025-11-15 13:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 61.6 |


[Clique aqui para ver as próximas entradas](README62.md)
