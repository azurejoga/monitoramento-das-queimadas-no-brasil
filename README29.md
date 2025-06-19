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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7f6ee1a-f403-33ec-b7ba-3b4383bba52c | -19.13265 | -52.71098 | 2025-06-19 12:29:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e9c14335-b6cd-3f39-971d-788a2d5322ee | -16.33224 | -53.94313 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 775e6d7a-947b-3178-b1de-7d36d1196d2b | -15.10393 | -54.65211 | 2025-06-19 12:29:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6ecf09ce-080e-3b00-a88b-2095839e7471 | -16.31857 | -53.81052 | 2025-06-19 12:29:00 | TERRA_M-T | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 163.7 |
| dae1fa03-2480-3523-bee1-980448e437e1 | -13.99348 | -58.11561 | 2025-06-19 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 6cb75b3a-2707-3f46-8006-69a0d6cbd57d | -16.3185 | -53.8094 | 2025-06-19 12:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| d0203bc6-98c7-32cb-865a-13dc8f1de32b | -11.4602 | -47.2883 | 2025-06-19 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9c9d3d3e-de8a-3a7d-afd3-58c16f9b82ac | -8.5911 | -51.5537 | 2025-06-19 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a567ae82-9fd6-3e1c-8662-9dd7ab8c5e12 | -16.3189 | -53.7883 | 2025-06-19 12:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 90df2a5f-40af-3977-ad75-66fef97a1cb3 | -4.8375 | -43.1919 | 2025-06-19 12:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 7cca473c-a8e7-30c4-b9cf-02a9014e1542 | -11.4793 | -47.2858 | 2025-06-19 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 65b93872-fa33-3859-8104-2dafcadf0814 | -4.8375 | -43.1919 | 2025-06-19 12:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| cd9123da-98e2-3e2f-81c8-c09ef6b48850 | -16.3189 | -53.7883 | 2025-06-19 12:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 0511ed69-2bf3-3caa-8517-674e636ff8b8 | -11.5366 | -56.9847 | 2025-06-19 12:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1e0874a1-c2d8-30c7-b429-9df2a6600cc1 | -11.4602 | -47.2883 | 2025-06-19 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 55984a76-5dfc-30e7-811a-937a75ae8d69 | -8.5911 | -51.5537 | 2025-06-19 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0bc21f5f-c48e-35e2-a197-bf809720f2c0 | -11.4793 | -47.2858 | 2025-06-19 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 339ceaa9-4a64-3256-9aef-a1ff6125065a | -16.3185 | -53.8094 | 2025-06-19 12:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7bb76ed6-6b15-3b81-b017-5453ffb9616d | -16.3185 | -53.8094 | 2025-06-19 12:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 8fd4951f-101e-3d66-afa1-5c28298597af | -8.5911 | -51.5537 | 2025-06-19 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| cc1578dc-882c-348f-bc4f-a8a20178eea1 | -4.8375 | -43.1919 | 2025-06-19 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 8dfebace-922f-3821-adac-da58cc862242 | -16.3189 | -53.7883 | 2025-06-19 12:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e167eef6-dd82-3f2a-9ffd-9421aee4e984 | -11.4602 | -47.2883 | 2025-06-19 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f1cfc1b6-1d6e-358a-8605-a15ea04f4d9c | -10.8353 | -54.0112 | 2025-06-19 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f6b1e166-87af-36ce-a269-ec0670456f48 | -11.4793 | -47.2858 | 2025-06-19 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b79d29d9-659d-3e4c-b790-faba8de36372 | -11.5366 | -56.9847 | 2025-06-19 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0703bfac-624d-3629-8594-ca362e63288b | -16.3189 | -53.7883 | 2025-06-19 13:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c47d0ec4-e8a7-3554-9c6b-6f35c7ecde72 | -11.5366 | -56.9847 | 2025-06-19 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6da0e833-b258-3206-ac3a-edbbc2d5ebb6 | -8.5911 | -51.5537 | 2025-06-19 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 60454fd3-0e4c-3ff9-a4ad-f505591535b0 | -11.7754 | -54.3756 | 2025-06-19 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2fda46ea-a095-3338-9eb2-d865c27fafff | -11.4793 | -47.2858 | 2025-06-19 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 5b95917e-29fc-3a18-926a-deb472e2f76d | -16.3185 | -53.8094 | 2025-06-19 13:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 05cdbd12-4ac7-355e-8006-d4951241c2dd | -4.8375 | -43.1919 | 2025-06-19 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| f91119c7-a8eb-318a-aa05-dda94f653be9 | -16.3381 | -53.8067 | 2025-06-19 13:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 864e62fa-d085-33ed-a708-891f3f7c4c56 | -11.4602 | -47.2883 | 2025-06-19 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| bf51bac0-ac88-35b4-bd73-859cc3ca218e | -10.8353 | -54.0112 | 2025-06-19 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 61385137-b023-3d5e-8ea7-51c81537e54f | -4.8562 | -43.1907 | 2025-06-19 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 693a844a-4d07-3511-aa10-233e7703bf5a | -11.5366 | -56.9847 | 2025-06-19 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| e08ec773-a3fa-30d0-b2f6-a45d3058d9e3 | -8.5911 | -51.5537 | 2025-06-19 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ece38f88-0ae5-30f8-8081-622eead3667d | -16.3185 | -53.8094 | 2025-06-19 13:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 8583e678-710e-306e-ad31-50a37b5aabaf | -16.3189 | -53.7883 | 2025-06-19 13:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 59f65736-cfa2-3b86-82bc-20ddbe7cb6ac | -11.4602 | -47.2883 | 2025-06-19 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 212.1 |
| aa3cfcfd-d47b-3a91-b045-ee3c88b319f6 | -11.4793 | -47.2858 | 2025-06-19 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 21d0ff8a-5e3f-3a21-b22e-bf20237925e5 | -11.7754 | -54.3756 | 2025-06-19 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c33b902f-1731-32ac-bea4-ddc55e29c299 | -4.8375 | -43.1919 | 2025-06-19 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 7cae2529-f305-3fef-a9bd-2b2b979d7a11 | -4.8562 | -43.1907 | 2025-06-19 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 37657ffa-98d7-3462-a359-0e2a6a517307 | -16.3189 | -53.7883 | 2025-06-19 13:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 16c27180-7d6d-39b7-b00a-d7da6b89006b | -11.4602 | -47.2883 | 2025-06-19 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 232.3 |
| e74f7afe-9b41-356f-9289-efaa5280b701 | -11.7754 | -54.3756 | 2025-06-19 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c8ab4555-a001-3d15-9ea6-b82b3c145ebe | -16.3185 | -53.8094 | 2025-06-19 13:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 206.9 |
| add7d69c-b6b7-34dd-afef-f020e8375a8b | -10.8353 | -54.0112 | 2025-06-19 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0b8d7646-c595-3d21-8fd4-735007b08f49 | -4.8375 | -43.1919 | 2025-06-19 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| b78cc410-1913-3e63-b921-cc7f56ac199e | -11.5366 | -56.9847 | 2025-06-19 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| c068cc21-13d2-3eaf-9d6d-445c797eec72 | -11.4793 | -47.2858 | 2025-06-19 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| b6d400c7-c92a-3b6d-8e9c-be49124489db | -11.7754 | -54.3756 | 2025-06-19 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0366e59a-6c65-3cf4-842e-9aa1ef6d8459 | -11.5366 | -56.9847 | 2025-06-19 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 038f2ce1-a32f-3987-9f05-50535738a624 | -4.8375 | -43.1919 | 2025-06-19 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 8c252723-263c-30d1-9791-b8950cdc177b | -11.4602 | -47.2883 | 2025-06-19 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ba941039-7395-3f91-9d81-acc9b7ecc80f | -11.4793 | -47.2858 | 2025-06-19 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 263.8 |
| bf8ade1e-acdc-3c0b-a703-7b5dfb03ea01 | -11.5177 | -56.9862 | 2025-06-19 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| afe3b182-7ee3-34c8-9d5b-8491d4d7e436 | -16.3189 | -53.7883 | 2025-06-19 13:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| e181eb43-5b56-31c2-9645-8692fdedc0d8 | -16.3185 | -53.8094 | 2025-06-19 13:30:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 90302ed1-8197-3125-99a8-ca30fd8e5e5b | -10.8353 | -54.0112 | 2025-06-19 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| a0016cbe-e869-3494-9f7b-0f812d43623b | -4.8562 | -43.1907 | 2025-06-19 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4b679447-f6fc-3776-8721-5ee420864142 | -6.6935 | -43.2117 | 2025-06-19 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 895f72e2-1063-3c08-a557-86aae8e9bd23 | -4.8375 | -43.1919 | 2025-06-19 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 302.4 |
| af93ee56-5274-32db-9261-11b9e0761cf8 | -9.4994 | -56.0788 | 2025-06-19 13:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 01819f77-0dd8-3c9e-bb37-6cc9cfd2287f | -16.3381 | -53.8067 | 2025-06-19 13:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 69a24342-9131-3235-9f6d-09822fcab361 | -16.3189 | -53.7883 | 2025-06-19 13:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 2a88ec55-c47b-38e0-bcea-82f3ecf22199 | -11.4793 | -47.2858 | 2025-06-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 473ba0d4-2cd8-35ac-bc5d-6032742cde17 | -16.3185 | -53.8094 | 2025-06-19 13:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 1d03f23a-1e16-39d7-aab9-928cf8b0a447 | -16.3385 | -53.7856 | 2025-06-19 13:40:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 13c2336d-78a1-398a-aa9a-239ceddc3d8c | -11.5366 | -56.9847 | 2025-06-19 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| da2f5ad0-1833-3f3f-83ad-770afaeede60 | -11.4602 | -47.2883 | 2025-06-19 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| b2539db0-1198-30a3-8d24-c3f0f7a7df66 | -9.0021 | -46.9079 | 2025-06-19 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 794cda20-85b9-30e4-8b00-56c1e8acdd22 | -10.8353 | -54.0112 | 2025-06-19 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 779df6c2-7e39-362d-a0f5-e908104c99b2 | -12.2412 | -44.2277 | 2025-06-19 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7e2e912a-952f-3c1a-9fd3-1e61d1a91e13 | -20.274 | -55.4927 | 2025-06-19 13:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1b86ab11-2a0f-3652-a487-ddf2d60ea5d6 | -9.4994 | -56.0788 | 2025-06-19 13:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9bad2144-a83d-3d61-9abf-1baa8b2adf30 | -7.3162 | -44.7056 | 2025-06-19 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 5518becc-3fa8-3a7a-81b0-dd4782c05947 | -6.6747 | -43.2133 | 2025-06-19 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 9fce1e89-bbc1-325b-8f18-2cf31bde077d | -9.0021 | -46.9079 | 2025-06-19 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 668aa2ad-2c92-3c92-b08d-19e1f0f69bb3 | -4.8375 | -43.1919 | 2025-06-19 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 307.4 |
| b91c2579-40fe-363e-8148-0f6f23881995 | -7.8626 | -47.898 | 2025-06-19 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9dc499af-80a2-38c8-a297-4c7748a50629 | -4.0148 | -43.2408 | 2025-06-19 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9a5cd753-3917-3181-834d-c1de28e00e08 | -11.4793 | -47.2858 | 2025-06-19 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 4689c292-8447-3087-aecf-a7334d76148f | -10.8353 | -54.0112 | 2025-06-19 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ca0d3340-e8b9-3a7c-a21c-d41ceb25ac2d | -16.3185 | -53.8094 | 2025-06-19 13:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 197.4 |
| f03e512e-6e6b-3176-a823-57eacc7715cf | -11.5366 | -56.9847 | 2025-06-19 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 56d9cb55-552a-3fde-800a-08fe5f038d26 | -16.3189 | -53.7883 | 2025-06-19 13:50:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 163.0 |
| e62516de-773a-3e0b-9f0c-704166912ae0 | -11.1419 | -55.1869 | 2025-06-19 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 99b8a8aa-4c57-3bd6-b10e-f27254ba6e3f | -11.7754 | -54.3756 | 2025-06-19 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f13935e5-1b41-301e-b902-8fd75ff928e9 | -11.4602 | -47.2883 | 2025-06-19 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| c0ae87b8-0031-322f-b126-96d4f2773707 | -9.4994 | -56.0788 | 2025-06-19 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 01aef5be-85ed-318d-9604-c385960b7763 | -11.5366 | -56.9847 | 2025-06-19 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 1519778c-6a8f-34f2-870d-6f1c119ce82a | -4.8375 | -43.1919 | 2025-06-19 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 334.7 |
| cda3d72c-641c-3fa3-82c0-af4c1e512c83 | -10.8353 | -54.0112 | 2025-06-19 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 73aa6bee-0eca-3066-ab0d-e8f14cd864c3 | -11.4602 | -47.2883 | 2025-06-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 08e3313f-0236-399e-a542-bf9e5b069298 | -7.3162 | -44.7056 | 2025-06-19 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2dab6a72-2730-386c-a9fc-624367c9440a | -3.9961 | -43.2418 | 2025-06-19 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |


[Clique aqui para ver as próximas entradas](README30.md)
