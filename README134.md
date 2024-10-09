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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b920a2e-937a-30ac-b8ee-184f55291828 | -17.09925 | -57.45114 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7b9cb6ce-b2eb-31d1-b122-fbb79a160472 | -17.09873 | -56.85986 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9601c87d-1c74-3403-ad9b-c3c2d1843a46 | -17.09854 | -57.45505 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 57392289-f9ac-3405-8ff9-246dfaa2a9eb | -17.09835 | -56.85849 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b43b5217-52d0-3c53-b23b-9e6d7c951343 | -17.09796 | -57.43468 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 35530df8-c958-3101-bd05-f746b50b4ff2 | -17.09782 | -57.45895 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bc342eee-8f39-3534-b0c7-5d0e993adc0d | -17.09773 | -56.86525 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ae2212b4-68d7-3228-81bf-62792785bbde | -17.09738 | -56.86389 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46cc263c-6cd8-3554-9ad3-b83750436ff5 | -17.09725 | -57.43859 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ec868c76-8c5a-3b7b-afe5-d34b09bf3855 | -17.09657 | -56.8684 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f59631bc-a8d7-378e-bc90-f52c3394e578 | -17.09653 | -57.44249 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f15723f1-b731-3c71-b5f1-f8349f4cdc85 | -17.09582 | -57.44639 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8401629f-d5ff-3d9c-a145-4a6d0543042a | -17.09574 | -57.33001 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c11369bf-5672-3821-a14d-376d40809fc9 | -17.0951 | -57.45029 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4ac09ca8-6610-3c8c-b980-4e602c593fa3 | -17.09503 | -57.33384 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 60990a34-1d72-3f5a-85e2-24ef9db2bc85 | -17.09474 | -56.85906 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a3a11029-dfaf-3e94-bc59-d5f6dc9c5e53 | -17.09439 | -57.4542 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 284873ea-8486-3704-8063-6adaf8c9c7f9 | -17.09435 | -56.85769 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eec75991-9954-3cc5-8546-160dd973ec38 | -17.09432 | -57.3377 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2ba66264-4b39-3e10-88f5-b3c80592d7b0 | -17.09382 | -57.43384 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8c37ac9a-0d97-337e-b627-6c9ebe84db50 | -17.09373 | -56.86444 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 558ec694-6a51-3c75-8ba7-0405f1683c84 | -17.09338 | -56.86309 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 46ffa476-7cf7-34e0-b2d3-4185f7b30904 | -17.09311 | -57.43773 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d66f6226-b7bf-361f-9941-6773cdaf621c | -17.09239 | -57.44163 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 600b440a-a24d-3f85-8edf-076a216c9917 | -17.09168 | -57.44554 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 806459d7-03b1-3734-bfb1-1e5852402788 | -17.09133 | -56.85149 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2aa42b43-8e98-3e27-9a51-dfafe7539313 | -17.09096 | -57.44945 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 38158f84-3ca6-3e61-8c93-22afb89a403e | -17.09036 | -56.85688 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a3b904df-e766-3da8-bf7b-199bb2137383 | -17.09025 | -57.45335 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62e76df1-5de3-351a-a000-2e820a0b42ca | -17.09021 | -57.33686 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7699036b-1cc3-3a85-adcd-bce10b734f0d | -17.08939 | -56.86229 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 131b1b74-30a0-359d-a218-d27068198b0a | -17.08897 | -57.43689 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6023d5a0-f8d7-390b-b7ca-7a7a1f6b1a34 | -17.08831 | -56.84529 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a0b83d4e-e434-3458-8377-0f34e409acb6 | -17.08734 | -56.85069 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bf918465-4942-3c70-b6b6-3e8eaff62b88 | -17.08636 | -56.85608 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 189b9312-6e60-3622-88e4-6395713c4835 | -17.08539 | -56.86149 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2b3e6ed6-becc-3bc3-b664-3b299a0f09d4 | -17.08468 | -57.3437 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5ffc2e94-fddd-3b1d-816f-c3b946d91662 | -17.08458 | -56.866 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 533c17cb-458b-3b3b-bdb1-14b0b6c0a1b4 | -17.08432 | -56.8445 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1997ebc3-ea7c-3636-b152-524d1be0a7d2 | -17.08397 | -57.34755 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 37f10bf3-25e0-3f57-b17e-a36a51b71530 | -17.08392 | -56.86961 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 318cec82-e829-3c47-a193-12b1b929a375 | -17.08335 | -56.8499 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f53147a1-119f-38bc-bbfe-0e1f9accaee9 | -17.08327 | -57.35139 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ee036857-c231-3f82-8d39-a1eb58f92917 | -17.08237 | -56.8553 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3cf8b351-7135-371c-a54e-8cf65305df11 | -17.08139 | -56.8607 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a68c0aa5-d32f-3098-98bc-493a3a1635bd | -17.08058 | -56.8652 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e4dc2a3f-c9b9-3cdb-95c6-4d95b7b61fee | -17.08033 | -56.84371 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| af3d179f-cf58-306d-885c-e1b1d98a1c07 | -10.19728 | -58.79364 | 2024-10-09 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96b14332-ea5e-303f-9c9a-2f0c4c5a83d3 | -10.19672 | -58.79671 | 2024-10-09 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba6e0010-6256-3719-b4a5-89996c4353fa | -10.19613 | -58.79986 | 2024-10-09 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f98b8fc0-b9a3-36cd-bd3f-058a9af4cd69 | -10.19555 | -58.80303 | 2024-10-09 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3146642e-54fb-355d-b585-2aa1c0d319a0 | -10.14147 | -62.11129 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26eb02c2-16d8-39f4-b4e7-29dc78012696 | -10.14052 | -62.11618 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54561a56-cdd3-320e-a2ff-ab18d6122639 | -10.13765 | -62.10948 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a37b1f4-64af-3e31-9a95-22dabeb1b56c | -10.13667 | -62.11436 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5acca114-af26-3b87-85ed-ad54567b0588 | -10.13517 | -62.10998 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 617d9dbb-a6c7-3eec-b470-ae6f42774204 | -10.1342 | -62.11494 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a081881-6d8e-3fc8-9f15-5c8bc340fd6e | -10.12895 | -56.76342 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ab4ac5c-0325-367f-8fcb-5f70798191f4 | -10.12815 | -56.76792 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ea0b45-3fd9-3335-b3e2-126b67689158 | -10.12655 | -56.77686 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11a66cb9-d82f-37c1-a131-bf161e9f2cb5 | -10.12288 | -56.77159 | 2024-10-09 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e2f56af-0e28-33dc-bd6b-96ff51139929 | -10.08992 | -62.51452 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c338a60c-7436-36b9-9a26-cce954eec9e6 | -10.08981 | -62.51294 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 231b217c-1a39-3a4d-adfd-b48761acacf5 | -10.08888 | -62.51988 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bbb9034-3eb3-3cc6-a137-f0dbc9a5cedc | -10.08873 | -62.51831 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2375a04-5205-3a3e-b5ab-f53b55707de0 | -10.08346 | -62.51313 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc4ee384-2864-3b3a-a678-d7f131e5a4d6 | -10.08242 | -62.5185 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02d96c93-37b8-3b42-adaa-b5f1014f5eb8 | -10.08227 | -62.51695 | 2024-10-09 04:40:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2d6c3b2-7d32-3c78-84c4-6f563261094d | -10.06261 | -61.11677 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8a62c16-d003-3f9c-8bd9-600c741300f5 | -10.06183 | -61.1208 | 2024-10-09 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efc20cfc-e104-3495-8b70-52e714799d82 | -10.03013 | -63.47612 | 2024-10-09 04:40:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be595f46-08c1-3d34-bb85-0219075471f1 | -10.02885 | -63.48246 | 2024-10-09 04:40:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8996555c-d978-3f7d-84a7-cfa92402deed | -17.07992 | -56.86881 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2c90f4dc-4559-325d-9b58-f20a632271c9 | -17.07935 | -56.84911 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| da314697-8d52-3b0e-bc24-0f345ad0d76f | -17.07837 | -56.85452 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1b7b8959-4148-3d8c-af71-0eb633a56a60 | -17.07701 | -57.36212 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 4c5712d9-3ffc-3a16-96c3-97e38a273832 | -17.07658 | -56.86441 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b369ec0e-0075-3d3d-a803-60dbab1088bf | -17.0763 | -57.36597 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0f8e644a-cf3c-364f-bdc4-f34dbc3b03e3 | -17.07559 | -57.36983 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c27ec06a-0bbe-3b9d-8063-b48e00b777e0 | -17.07488 | -57.37368 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 04d05672-5b0f-3a23-a968-34c3d58a931e | -17.07416 | -57.37755 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c0fe691b-ab32-32ac-a446-ff36c2a2560b | -17.07289 | -57.36128 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 97927aa4-dce2-37d8-a52f-92a9036fea27 | -17.07218 | -57.36514 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 65c6c02d-d17e-3045-902d-3bb128bc8064 | -17.07146 | -57.369 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bc62cb88-4db2-3154-9f85-c9a128daef1c | -17.07075 | -57.37286 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 18d9a8dc-4132-3493-b8bb-03f527aae2ed | -17.06436 | -56.84052 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2c999b66-c5bb-3f8a-b84d-11534d24dfea | -17.06337 | -56.84591 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2ed2a650-b5f5-3231-a8db-4b6e48413d68 | -17.06239 | -56.85131 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 46caa110-383f-35be-a347-b81c267966a7 | -17.06036 | -56.83972 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 73874420-b332-3969-a0cb-790752911346 | -17.05939 | -56.02306 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 28ad3351-8c6e-382a-84f3-96f2f9f53f27 | -17.05938 | -56.84511 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 733f2495-c112-3f1c-9402-35fc549b65be | -17.05852 | -56.02791 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 65ba76a7-3d3e-3604-bab3-0d4f092b51c4 | -17.05559 | -56.02231 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 57b04367-fdb0-3fda-b322-ea38f8747342 | -17.05471 | -56.02717 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 810730a1-d187-325c-883b-37836e5e0f69 | -17.0509 | -56.02643 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b84cbffd-7010-3e67-a5e2-d628022e39d5 | -17.04825 | -56.04102 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0d390d62-283d-3463-af3f-7f9a49709524 | -17.04068 | -56.05204 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 46709914-2b77-3f4c-89c7-58dcd59deb01 | -17.03886 | -56.04927 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5c359070-ba34-3728-95a0-055d8789fdaa | -17.03798 | -56.05414 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 676d7f4e-fe04-34d4-8052-aa09300a83f5 | -17.03772 | -56.04641 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README135.md)
