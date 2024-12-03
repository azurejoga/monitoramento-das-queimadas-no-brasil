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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4a6b234-5964-33ca-8cea-32c24244332c | -3.2774 | -53.6383 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| be203f2d-9abf-3d10-9755-2c10805ad499 | -12.7147 | -58.2231 | 2024-12-03 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 33c5cba8-d25d-3d1d-8d94-3f0c2219c1b1 | -17.8181 | -40.1115 | 2024-12-03 00:10:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 144.5 |
| 42f7a7d5-27e1-3851-9667-fd3a1891bd1d | -3.2775 | -53.6181 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4aed1b4f-fadf-3a69-a298-de604a82c13c | -1.0919 | -53.4762 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 01621cae-70f4-3ea2-9f8d-4fc5377d74d6 | -1.7541 | -52.7993 | 2024-12-03 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| cd57412a-0d57-382f-99b0-c2c72fb5e854 | -2.8012 | -53.0633 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 78dd9b22-1c98-3b02-95b0-8545794412ec | -6.1229 | -43.9578 | 2024-12-03 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| edd0c1d5-6a20-33ae-8ef4-3dadd8f21ac9 | -2.8013 | -53.043 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f6038569-12d2-31a3-9820-1b2b6ac052ae | -2.6644 | -44.9743 | 2024-12-03 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 33d57090-05fd-38b2-84d6-cd22532c4a46 | -3.2406 | -53.6595 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4d474387-390e-362c-99ca-e9222df3a9c0 | -3.259 | -53.6388 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b6d5c416-78e9-3343-a584-9feced97f16d | -2.8196 | -53.0629 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ae147081-db80-3cf2-a090-a51728971ed8 | -2.4948 | -45.5873 | 2024-12-03 00:10:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d742c2f7-0444-37a8-9bac-8dc8ff3b49f9 | -3.2591 | -53.6186 | 2024-12-03 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e6cceeae-82e7-32ca-90dc-bb003b659d6b | -4.5402 | -42.93 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 04281d03-60ad-3b80-b42c-180938a5f68f | -1.0736 | -53.436 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9daef907-ec8d-3a51-9b31-b8c8c88fd360 | -4.1708 | -48.1842 | 2024-12-03 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b25c2ff5-7765-3fb0-94ab-7ab222dd203d | -2.8212 | -52.5741 | 2024-12-03 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 57f12eee-5629-3c27-a9fe-e0c13334429e | -5.1367 | -43.2185 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 3838d0e3-6fee-3f0f-8117-59c6815b6808 | -1.7361 | -52.6366 | 2024-12-03 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| b5fbd9e4-5d8c-3595-af82-b0b8746ebede | -5.1181 | -43.1964 | 2024-12-03 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 159.8 |
| ce66335b-ff4a-3bd0-8c0a-e58f0aa73b67 | -1.0735 | -53.4562 | 2024-12-03 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 285.9 |
| 6f4d0bbb-8161-3c1b-b4cc-f630648f6040 | -2.3459 | -45.7036 | 2024-12-03 00:10:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 172.7 |
| bc31d124-1444-3577-a125-2ea853736c80 | -4.1915 | -51.1706 | 2024-12-03 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5553ad1d-d869-388f-9b98-62ea63b2a5c0 | -3.076 | -53.3808 | 2024-12-03 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 0044b59e-2c96-3ec9-9db3-db9e1e918109 | -3.5019 | -41.5187 | 2024-12-03 00:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 51e5cd0c-c357-392e-864a-d5b22f51f84c | -2.2111 | -53.7835 | 2024-12-03 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c8dd0791-6a4c-3df6-99d4-5ddc7cc9add3 | -4.1914 | -51.1914 | 2024-12-03 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1810a64a-6d14-39ec-8d86-1bd32153f0bf | -10.61204 | -37.05021 | 2024-12-03 00:11:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| a2b23af4-4e1d-3ac7-a459-3aa68f3b8c2f | -9.87957 | -36.62963 | 2024-12-03 00:11:00 | TERRA_M-M | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 8b8f43fd-5417-3b8f-98a9-9de9e3c058b3 | -10.67845 | -36.99753 | 2024-12-03 00:11:00 | TERRA_M-M | CARMÓPOLIS | SERGIPE | Brasil | 2801504 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| b4a8ffc2-d8f9-3196-8123-04d4bb11227b | -10.43945 | -36.87508 | 2024-12-03 00:11:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 61ffb5c0-d6e0-36c2-8d99-e2111ad0040c | -10.61076 | -37.04118 | 2024-12-03 00:11:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5a59709b-2dbe-3299-8ad2-636350c8888b | -10.75857 | -37.17931 | 2024-12-03 00:11:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| d00d42ea-234e-34c1-ae9f-4562d08e8fa4 | -11.97969 | -38.28634 | 2024-12-03 00:11:00 | TERRA_M-M | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b651820c-3c59-3fae-87a2-9265a825ea2e | -10.39254 | -36.5445 | 2024-12-03 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 46f9bf61-5831-36ba-a3e7-2e626873c60b | -10.43816 | -36.866 | 2024-12-03 00:11:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| f7895109-0551-390e-b046-490a59849f23 | -10.75983 | -37.18832 | 2024-12-03 00:11:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a5eb6d26-d667-3161-8352-811162f4a747 | -12.71154 | -40.21206 | 2024-12-03 00:11:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 236fdcfd-9a24-35b7-8577-4c6f6955872a | -10.01075 | -36.19868 | 2024-12-03 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f8299610-5e08-390c-82dd-3de0b435376f | -9.90295 | -38.11213 | 2024-12-03 00:11:00 | TERRA_M-M | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| f1540157-ad8c-3d1f-91f2-2f86e1518f56 | -10.407 | -36.64615 | 2024-12-03 00:11:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ad1f1182-0e84-3181-8c68-22a1c6121b34 | -11.89289 | -40.98389 | 2024-12-03 00:11:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 98f56e2d-fc47-33ba-8213-6040849116b6 | -9.9017 | -38.10315 | 2024-12-03 00:11:00 | TERRA_M-M | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5cd7663a-81d5-3ea3-8cda-97143cf6c1c9 | -10.52137 | -37.06081 | 2024-12-03 00:11:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dfee3bd0-239e-3453-a793-b736e878d77c | -6.81399 | -46.76422 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c67024c1-0c16-334c-b42a-506bd38149a5 | -3.271 | -46.93366 | 2024-12-03 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 47cecc8b-42aa-3213-995b-c4eda5047ea7 | -6.19102 | -43.41171 | 2024-12-03 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 768eef15-34cd-3e53-a460-cf7ff7bb3695 | -9.16431 | -43.12141 | 2024-12-03 00:13:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 9099ea5d-202c-39b5-928c-cfe5bb9ff8c0 | -3.76731 | -44.05761 | 2024-12-03 00:13:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 680b0c49-2096-3ba8-8d80-b815276d7d82 | -3.60923 | -45.60901 | 2024-12-03 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2450e46e-68cd-3cef-8011-092804d76ef5 | -6.12409 | -43.95716 | 2024-12-03 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b1f8e1af-cc64-340d-8596-ba72592fc1fa | -5.80824 | -46.48423 | 2024-12-03 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| cb6dbe08-2a2c-3f24-b7bc-9a8c5de90d12 | -4.13604 | -45.82672 | 2024-12-03 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 25d3a3a8-fcf6-3c16-83be-d4e01dc954e3 | -6.12619 | -43.97342 | 2024-12-03 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 98a4ef82-7391-370e-bea3-cc9f252613bd | -3.34414 | -46.05309 | 2024-12-03 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6b988803-b5af-39ab-886d-f50356a2fc8a | -3.19816 | -45.46585 | 2024-12-03 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7571d18f-3737-3dc3-ad16-1fa9599467a2 | -3.83336 | -44.11165 | 2024-12-03 00:13:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d89df196-caec-3eb2-a292-9ce1f3ab2fa7 | -4.47539 | -46.10135 | 2024-12-03 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a2454c3b-0d4c-3236-a5f7-41613a98ba6a | -3.19832 | -45.47136 | 2024-12-03 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ce89e017-18a0-36cc-b949-bfeebbe71622 | -6.0354 | -39.36387 | 2024-12-03 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f7e57eab-0a1c-303c-a4ea-626a6e2cf5f9 | -5.99936 | -45.41035 | 2024-12-03 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d7fd148f-763e-3062-a9cf-dabce85e99ba | -3.8284 | -46.56759 | 2024-12-03 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 734a5719-0a77-39c5-9a43-1e7a9957efbb | -7.06997 | -35.22205 | 2024-12-03 00:13:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 68aa5a08-b92a-3b67-88ee-a9544e09eb04 | -3.35256 | -46.04576 | 2024-12-03 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 722c9621-54ee-3f43-a11c-6332e3639553 | -7.38353 | -35.05704 | 2024-12-03 00:13:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 44add731-6492-3e2f-b586-65c3eeee1e98 | -4.54519 | -42.93929 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 33d343d3-7a67-3ca1-aa9c-111c51fe1040 | -3.20302 | -45.30902 | 2024-12-03 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 213fdb52-f025-3195-b947-2b7b758c76cc | -6.0397 | -42.52751 | 2024-12-03 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 6ca36fa0-9e59-344c-aa86-032da55b6144 | -5.12122 | -43.20994 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 353.0 |
| 12ad691a-3644-33a9-aa86-66e1e186ca0a | -5.54634 | -43.89427 | 2024-12-03 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e42b579-ae1c-3d93-8c5a-aa100f7c1f7b | -4.80919 | -45.00377 | 2024-12-03 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 89f00d23-4b8b-3df9-9670-3d4955b1ac9c | -7.56398 | -45.7326 | 2024-12-03 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 86a14026-da39-318b-9967-f12151cfc7cf | -4.42798 | -45.78503 | 2024-12-03 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c275bd65-ab4c-3de4-817a-980f0aab5a52 | -6.02914 | -42.52897 | 2024-12-03 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ed86b2b6-c3a8-3222-905b-ca1180c728ec | -5.38527 | -42.96058 | 2024-12-03 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 6dff393e-58da-316e-a7c8-f2057a48e2c7 | -7.80815 | -38.7348 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8960c8c2-a021-340a-b7a8-df4eeeaf92f1 | -4.75127 | -38.47474 | 2024-12-03 00:13:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 96262f68-7aa5-3630-9b30-4d2ccfe90ea3 | -5.90673 | -39.2387 | 2024-12-03 00:13:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 55acd7cc-ce7d-3a5a-9bd3-698ee445e54b | -4.74548 | -45.11517 | 2024-12-03 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 0d912fae-d764-3213-b5fb-a945341f81c1 | -4.47277 | -45.71278 | 2024-12-03 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5ff41361-92cf-3d1c-a42c-44334d4b41d9 | -6.03798 | -42.51455 | 2024-12-03 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 89924e7d-b1d1-3799-8c9e-7d25fc92b644 | -4.345 | -43.75121 | 2024-12-03 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| becacb2c-0660-3d4c-b6f0-8aea3fee8418 | -3.46906 | -42.00569 | 2024-12-03 00:13:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| c92f2be6-b43f-35a3-8027-3002aaa020fb | -6.67715 | -46.39161 | 2024-12-03 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 04bb5bfa-dc75-362e-88b2-6412a7e28c78 | -3.47055 | -42.01665 | 2024-12-03 00:13:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 0bfe8fd7-d6ae-35ed-a227-78f493b60041 | -5.57772 | -44.89221 | 2024-12-03 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2f678344-0475-3908-a477-2dd047520aa5 | -5.45311 | -44.83689 | 2024-12-03 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f33f0cd1-d7fa-3e2d-a224-543defba220b | -4.86506 | -38.37113 | 2024-12-03 00:13:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b07f9916-ab26-387b-986d-12a9d7411ef5 | -6.42861 | -35.17327 | 2024-12-03 00:13:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 53.2 |
| 86d8f9c3-8dbc-3cd5-b375-59233f9c8a94 | -4.54344 | -42.92634 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| b116c46f-00f2-3524-be2b-398b84f70ae8 | -4.48756 | -46.3569 | 2024-12-03 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| faf94095-7249-3e4a-8c51-c161b54f86cb | -6.03417 | -39.35487 | 2024-12-03 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5fd69b42-44a8-30a8-a02d-db0c874b388a | -3.44576 | -45.85329 | 2024-12-03 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 43ce6f85-7e26-31e3-8919-09cc30d36715 | -6.4303 | -35.18491 | 2024-12-03 00:13:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ca05b098-7236-3d4f-90fc-46d9283abb35 | -5.12308 | -43.22393 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4d5b70e3-1ece-3038-83d5-fd14e9db2b47 | -3.61026 | -42.74075 | 2024-12-03 00:13:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b1c7bea-0191-39b7-9943-914ba9887b1c | -6.1122 | -43.95849 | 2024-12-03 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| f3a41e45-b29f-35ad-a7f1-edc82770e1b4 | -4.57483 | -45.1111 | 2024-12-03 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |


[Clique aqui para ver as próximas entradas](README3.md)
