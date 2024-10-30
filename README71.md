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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e370d6ab-3b4c-3669-967b-9b67d4054f2c | -3.42085 | -44.457 | 2024-10-30 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b103981f-777b-38c2-b69b-361be6a169db | -3.53749 | -43.61624 | 2024-10-30 04:44:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12d72e08-646d-36ad-873f-c3ae5d3ee376 | -3.53683 | -43.62072 | 2024-10-30 04:44:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8e0ab53-d4f4-314c-a507-87422f1f7536 | -3.53296 | -43.61555 | 2024-10-30 04:44:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82579b4f-16f4-3ae3-805e-c6ed61a80553 | -3.5323 | -43.62003 | 2024-10-30 04:44:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba863b68-109d-334d-bf0d-09dce5d24382 | -4.35375 | -43.78032 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bcb0c99-7b43-38b7-ac60-a73ac8abbb73 | -4.34921 | -43.77966 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22f78033-d5a3-3e8c-8e04-542014eedcc7 | -4.34858 | -43.77628 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a91c7311-b6e6-334e-88dc-80e99ea73848 | -4.34856 | -43.78414 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39d48964-1f35-3d53-b5ac-2f109bbaff4f | -4.34789 | -43.78079 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e98555a9-a402-33d5-8075-5aa8203d9ddb | -4.34721 | -43.78528 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7556583f-2a35-3820-8c32-078d9e801ca4 | -4.34599 | -43.76985 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17da82bd-f775-36cd-a42d-b03734350734 | -4.34468 | -43.77894 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6417f14e-fcc4-307e-aba4-1252392f481f | -4.34337 | -43.78006 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b22f6bc8-592f-3b15-9090-6a30bb3caa2e | -4.3395 | -43.78273 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2494e9ab-211e-300c-88ba-8e16b3e56ee0 | -4.33814 | -43.78391 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b7fdc22-3779-3d6b-a6d5-602344d82cd1 | -4.33497 | -43.78199 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92dc190b-5858-386b-b8e1-ebbc461fc1aa | -4.33362 | -43.78316 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ede345f4-ce51-39a7-ba84-9bb12d04261b | -4.32849 | -43.63187 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e4aa0ab-0666-3c9b-bd44-c79e0b33035f | -4.32391 | -43.63123 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cb67b3d-b045-39f6-8e4f-bf95164d4896 | -4.27113 | -43.4448 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c1087a0-31a4-3be3-ac99-808ed856d717 | -4.27047 | -43.44944 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf6b5811-5215-3067-87b4-0f684997c347 | -4.26941 | -43.43793 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae6cbc7b-571d-3927-9e84-f4ce213fbbf8 | -4.26868 | -43.4427 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 595ef2ac-cac7-3f58-a599-498a6dde951b | -4.26798 | -43.44739 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 19683cc1-ea00-32cc-9d24-12bd01b47a23 | -4.26405 | -43.442 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| abce3b35-7549-3afa-96d0-9b0e0d4835d8 | -4.26334 | -43.4467 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ef25dc18-9467-31b9-abaf-14f58034e986 | -4.25942 | -43.44125 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4f67109d-d57c-326c-8efc-d27e5921a45a | -4.25871 | -43.44601 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 403add6d-9b13-3f1e-bb3d-a47cafbacaaf | -4.258 | -43.45072 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c5c4e04-106f-3381-a8a9-14a4760749c8 | -5.12787 | -43.44785 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 719c0c62-85c9-3b65-ab22-73ba5f7582ee | -5.08118 | -43.36392 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72833a98-1292-345f-a872-0b2ed9a1e532 | -5.07646 | -43.36322 | 2024-10-30 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf5df78c-0c9f-3c19-94c4-4bb098699b63 | -5.06971 | -43.67076 | 2024-10-30 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2218cca5-e11d-3e8e-b871-13598f7f5112 | -5.06901 | -43.67551 | 2024-10-30 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 993a1c6e-1cdc-3221-ad76-5050a0d8be2d | -4.66058 | -43.81765 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d662dcc2-2193-3d8b-a5ae-1167e6496a50 | -4.65603 | -43.81698 | 2024-10-30 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6cb7917-3ec9-3ec0-9112-d4f08bfe1f16 | -5.00736 | -44.36406 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13531239-f609-3656-bc23-d0912c4ea961 | -5.00688 | -44.36193 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf1ab060-3aff-3021-b04c-90dc4118a2c5 | -5.00296 | -44.36343 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 059d834a-a3c5-3ba8-bb2c-86139875e55d | -5.00248 | -44.36129 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daba1198-c180-36d9-9d96-1217eed2e321 | -5.00232 | -44.36764 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 827e748e-2fc5-379f-9693-f2dfa25d8a1f | -5.00187 | -44.36553 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02ae61f2-a6fb-3ba7-b146-aca4824e2377 | -5.00168 | -44.37186 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 630ac471-5e6c-3a92-9497-d58036db6357 | -5.00126 | -44.36974 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 117f8a94-fbcc-3286-a674-563ff64fa9f2 | -4.99856 | -44.36275 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d6e102b-0262-3066-ac4b-745726d64564 | -4.99793 | -44.36695 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faa50366-88d8-3a71-9029-f99930e47526 | -4.99747 | -44.36485 | 2024-10-30 04:44:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48c0f4fc-aa4a-3e68-a042-d01f0d7f661e | -4.60433 | -44.30001 | 2024-10-30 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ad2eff0-9f2c-3e42-9816-4d2f383c1f66 | -4.60372 | -44.30416 | 2024-10-30 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c263f36-8732-30c1-a9d1-a58f74c2dd46 | -4.59995 | -44.2993 | 2024-10-30 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 754b700b-a8c3-3f62-839c-9b300750a64a | -4.59934 | -44.30346 | 2024-10-30 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f18eb6f2-f816-3381-be18-51875bd252fd | -4.59626 | -44.32463 | 2024-10-30 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 298373b8-3f23-3128-aabd-938aee7cbef0 | -5.06359 | -44.22017 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 465f1891-fab2-37ce-b4df-8b8174d61023 | -5.05849 | -44.22396 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4665e6a9-9857-3c4e-98db-87346ec6de79 | -5.05403 | -44.22338 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83236c8d-a635-3585-addf-5d509c61332d | -6.14002 | -43.51748 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9191a37e-a22b-3a87-a38a-cee8ce985430 | -6.09172 | -43.55111 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 110a4aeb-03ce-3d86-ae0a-d0f416019065 | -6.09083 | -43.54957 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb280da1-2299-39c8-9754-7eab2b2443ad | -6.08769 | -43.54543 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b090b8b0-518a-3576-85c5-43a338855707 | -6.08698 | -43.5505 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d97a031-1c4a-3704-9bb1-dfe9d0751ef7 | -6.08609 | -43.54891 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c86da1d-6a99-337d-b791-0f83451c8058 | -6.06101 | -43.62119 | 2024-10-30 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adec3baa-15ea-3bc0-93c9-a8d5c6ed1c5d | -5.94037 | -43.6825 | 2024-10-30 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f88b48a6-2a01-3a46-b275-51ea7d16cd67 | -5.93569 | -43.6818 | 2024-10-30 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ef7c743-ecc3-35db-bc9f-524151759ebf | -5.93102 | -43.68106 | 2024-10-30 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48eaa6a8-7801-3e3b-8c32-d98dfc3615ed | -5.92635 | -43.68032 | 2024-10-30 04:44:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889251c4-9a36-34b3-9f64-1a6feef6fd27 | -5.83275 | -43.65012 | 2024-10-30 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dda18a46-dbca-3e3c-b3aa-ec311964dd79 | -5.70124 | -43.68784 | 2024-10-30 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97271fc9-eec0-3dc1-b2c8-094fe7bd99ad | -5.69656 | -43.68725 | 2024-10-30 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82925e6f-d39f-3331-818c-c71ab3efa5c1 | -5.57136 | -43.71087 | 2024-10-30 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fadf9c4-39f0-3820-beb1-f0c4c9eca7ac | -5.28151 | -43.90961 | 2024-10-30 04:44:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1403c318-e3b5-3ad7-99e1-833d7ecc90d1 | -6.41496 | -44.13319 | 2024-10-30 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c317421-9770-3f48-be95-25f03639bc3e | -6.30898 | -44.88316 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 613afa34-a68a-360c-b938-9bb7da41d29a | -6.30466 | -44.88247 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4974e6e-0352-3bb2-b449-d205b88f91cb | -6.27318 | -44.4796 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 898753a4-5075-3dd2-a86f-c83c6d75e05f | -6.19714 | -44.09157 | 2024-10-30 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b70b2a33-4804-3c7e-8e97-514a2c525c97 | -6.19008 | -44.20302 | 2024-10-30 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5beb2ee2-c3b4-3e83-8986-f23d10adc297 | -6.18948 | -44.20711 | 2024-10-30 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afb444ff-6e8e-30ca-a49c-9a603d54fa39 | -6.06967 | -44.62378 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73f1931e-1812-3033-a682-7b13d457b92e | -6.0412 | -44.79067 | 2024-10-30 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43256746-e696-3a12-90da-ee6b5f0ea377 | -6.03686 | -44.79004 | 2024-10-30 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9360bf14-0b01-3b91-818e-d94b6d2d4d6c | -5.92415 | -44.51918 | 2024-10-30 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95793d6c-663d-3ebd-86b2-0725b1c84eb9 | -5.92285 | -44.52796 | 2024-10-30 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5917ef-d638-3ed3-83c4-5f6d5c421fcc | -5.86959 | -44.31844 | 2024-10-30 04:44:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a55485d-73a1-3f8f-8522-84f51cc78afe | -5.6096 | -44.89507 | 2024-10-30 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9228d662-2796-3770-b22c-018b4b973c28 | -5.60902 | -44.89903 | 2024-10-30 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8a4fafe-a8a9-3e90-bf1e-539b35c623da | -5.60474 | -44.89844 | 2024-10-30 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c56eb3ac-caad-3e0e-94c6-77fe24a9d7d0 | -5.33815 | -44.18604 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7abd5d2-d485-3126-8c70-3bf9523c42d4 | -5.33748 | -44.19048 | 2024-10-30 04:44:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e1ebd24-bb11-3d92-9af7-8b0d20211717 | -7.24494 | -44.19803 | 2024-10-30 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 465067e1-7c70-3403-adf6-244c8b283f5f | -7.25793 | -44.91797 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cc2071c-ae03-3e36-9518-2296a1bac6ff | -6.97513 | -44.32476 | 2024-10-30 04:44:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ec17f58-6ca1-32ce-8f72-2d4133c0ae70 | -6.96937 | -44.71552 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eccc9e6-eb47-3ec6-acd0-6505ee64ec23 | -6.92694 | -45.06605 | 2024-10-30 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5bfd0dd-6ad9-375b-b09a-e1783387b0d8 | -6.89286 | -44.56853 | 2024-10-30 04:44:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d7cf954-cf72-3b74-9233-6a6d5e5b0104 | -6.66792 | -44.69926 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d790464a-1969-361d-9ff3-31e9b366f0e7 | -6.66722 | -44.69693 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58559d97-65da-35ca-815b-6a7401bbdd80 | -6.66662 | -44.70125 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbc9ff01-3827-3c5b-81e5-5ad58ed12282 | -6.6635 | -44.69866 | 2024-10-30 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README72.md)
