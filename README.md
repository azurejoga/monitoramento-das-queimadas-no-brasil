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
| d7bb20a7-aed7-3f2e-bd04-7f5dd3813d93 | -6.12 | -43.95 | 2024-11-01 00:04:52 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50870d31-e1da-3127-b002-c45cf35a9578 | -4.39 | -43.49 | 2024-11-01 00:05:03 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c6aed9d-606e-3423-81e0-d83f86446bec | -4.39 | -43.44 | 2024-11-01 00:05:03 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f35f66e0-2c14-3190-a3ba-b21eb0d58975 | -4.32 | -45.63 | 2024-11-01 00:05:03 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d389396a-52c9-302e-a3cc-ae7a91c4ca74 | -4.29 | -45.63 | 2024-11-01 00:05:03 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 436270e3-a7a4-37fb-a883-e86d1d2707e5 | -0.7915 | -63.0797 | 2024-11-01 00:05:10 | GOES-16 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c2af347f-44b2-3977-b39a-382cead987fb | -3.08 | -45.53 | 2024-11-01 00:05:11 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6097c7d3-e5dd-3fec-a786-69bc4a9e2fa7 | -3.11 | -45.58 | 2024-11-01 00:05:11 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a11ac7c7-5b37-3107-b4a6-f06c32220e7e | -3.11 | -45.53 | 2024-11-01 00:05:11 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60c84858-0c4c-3a5a-9bdc-d1118895744d | -3.08 | -45.58 | 2024-11-01 00:05:11 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ecf22ab-0fcb-3be4-ae84-80bb983a17b1 | -3.05 | -49.5 | 2024-11-01 00:05:11 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6cf5496-8246-387a-82b7-47fb064e8c3b | -3.02 | -49.5 | 2024-11-01 00:05:11 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57bc580b-8f9e-3778-a5f3-1b1e4cd2b11d | -3.02 | -49.45 | 2024-11-01 00:05:11 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec8b70ff-cc71-3624-b7d3-d3aaf05f90e5 | -3.05 | -49.45 | 2024-11-01 00:05:11 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e774ab4-5be1-3790-9cf0-b86a494026f5 | -1.2292 | -47.7516 | 2024-11-01 00:05:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 646dc03b-fbf2-387e-96ad-0cda72a76380 | -1.2292 | -47.7299 | 2024-11-01 00:05:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| a7386b08-ca78-3a94-8513-0a2bf071f09a | -1.2477 | -47.7297 | 2024-11-01 00:05:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8f6837bb-20f6-3314-8a60-5edaf04544a8 | -1.4244 | -52.2118 | 2024-11-01 00:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 80f9cb51-bf32-3c37-ad42-1af27af2bd11 | -1.8471 | -52.308 | 2024-11-01 00:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6f1353ee-e97b-33b7-846d-f9fb9dc783bc | -1.8654 | -52.3077 | 2024-11-01 00:05:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 96d7b478-3bd3-3af6-9a2d-35727972e980 | -2.1695 | -48.7252 | 2024-11-01 00:05:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 07e5754e-440d-3dc7-a6b6-72e97c8e3504 | -2.466 | -48.5035 | 2024-11-01 00:05:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7784d134-7f78-35d4-9aaf-4f6a1ce11e0d | -3.0891 | -45.5896 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a0b690de-1699-3338-bd1a-f82ec3d65386 | -3.0893 | -45.5672 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 396.3 |
| 71b06e0b-2a1f-325c-b218-9b381b6d08b9 | -3.0894 | -45.5448 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 4fb77856-5c14-3ccf-a990-e6d4d1d63b1e | -3.1077 | -45.5889 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| edf54339-597c-3156-8b7c-66560d18c6aa | -3.1078 | -45.5665 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 347.1 |
| 5bc59354-aca2-3523-b7c9-960cfc253398 | -3.1079 | -45.544 | 2024-11-01 00:05:23 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cc64cafe-21d8-3c8d-b3dd-c7a98a31de94 | -3.1281 | -54.266 | 2024-11-01 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7c268cd8-f7c4-3f48-ab61-79c1261ca899 | -3.2719 | -50.3473 | 2024-11-01 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d33f3d61-eb7a-3920-b4ca-f472eb3d27c8 | -3.5631 | -47.3847 | 2024-11-01 00:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 79f938a7-0f34-3d6e-81b0-b393ffcad9d7 | -3.7703 | -43.5323 | 2024-11-01 00:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| b6282e3a-fe17-379b-8535-175a043367e2 | -4.2977 | -45.6475 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 79c55b78-df96-3a38-85cd-132445faecee | -4.2978 | -45.6251 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 49a5dede-3eec-34bc-a878-d149693e64c5 | -4.2979 | -45.6026 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 462e8818-0caf-3e5a-a1ff-74f176a907d1 | -4.3163 | -45.6466 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 326.9 |
| bbe7ffe0-9b99-3ac6-bc65-a034451a2b07 | -4.3164 | -45.6241 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 494.7 |
| b3659535-101b-3889-920a-30888f3381bb | -4.3166 | -45.6017 | 2024-11-01 00:05:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2e394beb-884f-3b86-a29b-f2297ddf7d43 | -4.3867 | -43.4757 | 2024-11-01 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 477.4 |
| 440e8a6b-dc44-3ab1-b3f8-e37335a1a6da | -4.3869 | -43.4525 | 2024-11-01 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 685f8dd3-b4ba-3f50-a54e-ad70a902d941 | -4.4054 | -43.4746 | 2024-11-01 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 4057a3e9-71a4-3d4b-ba3c-747249a041a4 | -4.4056 | -43.4514 | 2024-11-01 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| d088684c-ef28-359a-9a1c-3ef13464e568 | -4.8398 | -42.8875 | 2024-11-01 00:05:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 99feaf64-f4e6-3af8-8f37-0336bcacf735 | -4.8584 | -42.9097 | 2024-11-01 00:05:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 8baa8551-06d6-342a-951b-cdfe5736a13e | -4.8586 | -42.8863 | 2024-11-01 00:05:33 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 99cd04c8-9c56-31d9-9207-7d2b716c2352 | -4.8397 | -42.911 | 2024-11-01 00:05:33 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1408778f-1b78-3005-90eb-b2cae67f50f9 | -5.097 | -48.4617 | 2024-11-01 00:05:35 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ca706d06-b2a4-331f-906d-7116f651d466 | -5.0971 | -48.4401 | 2024-11-01 00:05:35 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 43c1c676-205b-3e92-8ac4-9b5b1f40ecae | -6.1041 | -43.9593 | 2024-11-01 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f406631f-6399-31b3-bc3a-b13e0bc1fa6a | -6.1229 | -43.9578 | 2024-11-01 00:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| fc407413-8f7a-36bf-8518-4d815c458293 | -10.1071 | -68.3823 | 2024-11-01 00:06:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 868c93be-9c77-3f79-ac51-9e3864b1892f | -10.6819 | -65.002 | 2024-11-01 00:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5e8b7655-f5dc-31fa-9cd6-d82d3a3e5a94 | -10.682 | -64.9831 | 2024-11-01 00:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3f2caae7-c256-3c05-bf17-8716771bae7c | -12.4404 | -63.1522 | 2024-11-01 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6efc82d0-8262-3495-8006-73249e485d91 | -12.4405 | -63.1331 | 2024-11-01 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4aaf012d-1a7f-3976-8321-b9fd17e00780 | -12.4593 | -63.1512 | 2024-11-01 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| f22c5add-c790-38df-98f3-e3c30eeb0ab1 | -12.4594 | -63.132 | 2024-11-01 00:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d5e3c2a0-c694-3667-b97d-8fe34e59e550 | -16.9008 | -57.5313 | 2024-11-01 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| a9df7af3-789f-3674-ae9a-e88e8a2e0555 | -16.9012 | -57.5108 | 2024-11-01 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 8a8d48b1-6da0-3d3e-be3f-677358e0fa68 | -16.9204 | -57.5291 | 2024-11-01 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 28444ae9-0388-3473-b876-b08dd06c43e3 | -16.9207 | -57.5086 | 2024-11-01 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 01c6af1c-1118-3bff-9cf2-f469e5b3a48e | -17.7249 | -57.5368 | 2024-11-01 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| bdc678c1-1a80-34c6-a082-a36aff38858c | -9.59599 | -36.15667 | 2024-11-01 00:11:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8666ccb8-f694-3068-bb1a-7cdfdea6ae4e | -9.39302 | -35.96362 | 2024-11-01 00:11:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 90cfb991-511e-39a2-ac00-e53ce7888323 | -8.89858 | -35.73197 | 2024-11-01 00:11:00 | TERRA_M-M | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 8ce927aa-411a-3ab4-9bc7-97fa21a13f69 | -8.8126 | -40.18047 | 2024-11-01 00:11:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d24694a7-283f-3cec-87a7-59d5b7a4e211 | -8.81114 | -40.16952 | 2024-11-01 00:11:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 46aba030-5802-3552-b0f1-70bad0300529 | -8.40299 | -35.29976 | 2024-11-01 00:11:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a8b61dd1-7bb0-31fe-bd87-9b5bd6ca8018 | -8.39625 | -41.4493 | 2024-11-01 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8f2a5075-420b-319b-801d-a81c408198ae | -8.38723 | -35.32253 | 2024-11-01 00:11:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 06b60410-869f-3d65-b96d-79c0098d8915 | -8.13596 | -39.86138 | 2024-11-01 00:11:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 35c58aa8-e24e-315f-ac16-6d32a045c2f6 | -7.76079 | -37.59781 | 2024-11-01 00:11:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0f28b8c3-bd2e-3f56-b997-8129e9cae5aa | -7.60396 | -38.85893 | 2024-11-01 00:11:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 313305e5-a8e6-32d6-a8c3-bd88fba99654 | -7.09305 | -35.09942 | 2024-11-01 00:11:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| acbfb107-691f-35a5-b007-119d48615b0e | -13.33737 | -41.32098 | 2024-11-01 00:11:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 06706e97-81db-355c-8108-4d00c970b160 | -10.75243 | -37.10415 | 2024-11-01 00:11:00 | TERRA_M-M | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| c0d6c9c8-d619-3bf0-b522-14f73408398c | -10.41029 | -36.90456 | 2024-11-01 00:11:00 | TERRA_M-M | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fcb23691-253b-3f6c-9daa-8eab2e99a3b3 | -10.14954 | -36.35961 | 2024-11-01 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 5201ff33-4662-3f23-80c4-933fd2e68004 | -10.14827 | -36.35057 | 2024-11-01 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 31.3 |
| 310f1bac-84ad-347c-ab51-4a26dba31ae6 | -10.12536 | -36.31702 | 2024-11-01 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 000162e2-e9b5-3c53-a929-5beccdfa1b39 | -5.09621 | -48.4613 | 2024-11-01 00:13:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 62de7a79-1b13-3353-859b-046b05fc501b | -1.73381 | -46.72726 | 2024-11-01 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0fb9afe0-f8cb-30b2-8007-879500b61fcb | -1.74305 | -46.70598 | 2024-11-01 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 176811d4-8d9b-3bb4-a5f3-e2a8e913edf4 | -1.74674 | -46.73213 | 2024-11-01 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 9a25117a-4ca5-39f6-b587-29ad1fe44a9c | -1.90259 | -46.33711 | 2024-11-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5f22105e-3e00-3cb7-a3a0-e0f035fc96fb | -1.90664 | -46.33003 | 2024-11-01 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 39b9143e-fdb1-3e32-aff5-739898b6110b | -2.25401 | -46.65299 | 2024-11-01 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 09a3b52b-5bb4-3c69-b754-fed365d4e669 | -2.35078 | -48.68541 | 2024-11-01 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bd1fdf53-3a8d-32bb-aef2-c9c88d01ee20 | -2.35384 | -48.6784 | 2024-11-01 00:13:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9dbd5dfa-aa90-3a38-b212-ed26af84ab49 | -5.09529 | -48.46868 | 2024-11-01 00:13:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2105730c-1773-38f2-8433-ccd36ffb8d26 | -4.73709 | -45.75517 | 2024-11-01 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 1cf5681a-a5bd-3c35-bb6d-4ac7032db86b | -4.73289 | -45.7622 | 2024-11-01 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1c14cad4-bf1c-30e7-9083-a0ede21473c2 | -4.72964 | -45.73815 | 2024-11-01 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3cd2ce8a-1d63-33cb-8b1c-aed101669052 | -4.32324 | -45.64508 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 93f2f418-e06b-3443-814f-fdde957dbe1b | -4.32014 | -45.622 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6b1a1c55-381e-374d-b198-076431c380bc | -4.30934 | -45.64704 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 3d3e5cbe-bda1-3ea8-9cdc-3c3d1ceb1c8f | -4.30624 | -45.6237 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f0be64a5-65fb-3bc1-95b9-c563ee7af581 | -4.26607 | -45.75094 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a5f2e118-58be-3a41-b075-fc51b64850d8 | -4.2613 | -45.757 | 2024-11-01 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2822df80-88a4-3be4-8606-29903ff00770 | -4.12636 | -44.18561 | 2024-11-01 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README2.md)
