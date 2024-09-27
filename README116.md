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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 720d6353-0883-3e83-82e6-5e62ed0e81b9 | -11.20808 | -54.78502 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b9fd114-f5e8-3e20-be13-437dcf35136b | -11.20733 | -54.78867 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4668934f-9a62-340e-92cc-5995944e46ca | -11.20732 | -54.79073 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2655b2-d7b0-3dd3-b1f2-baf7640750ba | -11.20662 | -54.79436 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4446d9c-5655-388d-8187-f25dfcbd31f4 | -11.20652 | -54.75827 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19c765ae-3f5c-378f-b61d-55f8528efc92 | -11.20631 | -54.75602 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d87c4c1-4bc5-3b77-ab1c-5b905484124e | -11.20613 | -54.76125 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9601a060-eb73-3e75-a9e4-d94bf54a1df0 | -11.2052 | -54.76492 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b214dc5e-b18f-3672-82a2-384163d10f86 | -11.20483 | -54.76784 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dc912f0-fbdc-3792-91f2-1e1de6ca7348 | -11.20459 | -54.7729 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e24d5994-2711-3d40-8dd5-67be25f6fee8 | -11.20447 | -54.77075 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c98fb410-f25f-3e80-a2da-2122d1c8d8e9 | -11.20421 | -54.77576 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e539dfc-def5-371e-a12f-bee3fd35b7f1 | -11.20411 | -54.77364 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ecbc23-b92e-3846-a124-558bddd14a8e | -11.20375 | -54.77651 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 383e6b4f-104b-309c-a984-b08fe4edc969 | -11.20344 | -54.78152 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a20eb807-ec7e-3a08-a1a3-e4d9ac3b71a6 | -11.20339 | -54.7794 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af07125c-d4f3-3eef-8fb4-e49ae92ffa77 | -11.20267 | -54.78519 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6cd3339-141d-36ed-98b1-0049cf5a67d7 | -11.2023 | -54.79015 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3067af37-e901-3505-bf63-775c7010e9df | -11.20192 | -54.79299 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a95d2632-8d62-31ad-9218-0eeaec4b5059 | -11.20033 | -54.76645 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caf0c63e-d092-3fee-a9e6-58f2e4f56d5a | -11.19492 | -54.76873 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0c119f-089c-35af-8e36-53e2dfdb2825 | -11.1845 | -54.77033 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3a6fa0d-adcc-31b6-b1b0-339abac1bb96 | -11.18411 | -54.77326 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11cedb2d-694e-3853-8bb1-a87e1d8cc3d1 | -11.1791 | -54.77259 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb108da9-cd99-3b25-84aa-7881b0a4ea1c | -11.17871 | -54.77552 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 391c967a-e6e8-3e5d-8530-05421391ae45 | -11.23857 | -54.7837 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07bc14a-f0da-3a80-bb5a-e3c451ec1275 | -11.23354 | -54.78308 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6f4c584-c200-3b43-be72-ed51099966c6 | -11.23318 | -54.78597 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f2acf36-4132-3a44-8555-ccce9ab9b264 | -11.22924 | -54.77673 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 394ff6ba-6fa7-35d4-9ed1-9c004c6cfabb | -11.22888 | -54.77961 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42399134-88fb-3c48-8f2c-4eee5b5cbec9 | -11.22852 | -54.78248 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 172247fa-b700-31c8-9d81-ff760eb4f5e4 | -11.22421 | -54.77613 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b044c2d7-6f64-3146-bb38-3916d12243b3 | -11.2154 | -54.76839 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd3b8e30-fe6b-3d67-80ea-30cb887c82d2 | -11.21502 | -54.77129 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774b18ed-d6d6-3aa8-b79a-e124365e3f39 | -11.21463 | -54.77417 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a12eef-d785-3928-9e66-83952a796eaf | -11.21425 | -54.77705 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 970e27d6-c458-3510-8c83-1519f76eac3b | -11.21416 | -54.77494 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa6fcb1d-2c23-38fe-9f2c-a178afc18538 | -11.21348 | -54.78277 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9830109-9b48-376a-8df4-814ba016d03b | -11.21076 | -54.76485 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6a01303-29a4-3d45-a63a-4e613bbb5f62 | -11.21059 | -54.76267 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed86d37c-5776-3827-bfe5-d6e1dc009664 | -11.20986 | -54.76851 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6b2f1cc-3eb2-3af8-b69b-ef1d7b72d35a | -11.20949 | -54.77141 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae761304-c921-3438-ba7e-0b1e57518c19 | -11.20922 | -54.77641 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3636044-9835-3442-a54b-0a6074fbf4f6 | -11.20884 | -54.77928 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 798a41b7-dbc1-3d3b-bbe6-bcaba277ba0c | -11.20877 | -54.77717 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bbe3bab-18ff-39d3-9952-afa066bca863 | -11.20846 | -54.78215 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9af1bdf9-40c2-3f75-ab24-f93eda785182 | -11.20841 | -54.78005 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c4bb940-96bf-3f76-9ab0-36d3bc0f8e82 | -11.20805 | -54.78292 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abae4611-73e3-31e1-b1d7-6fb92bc3599b | -11.2077 | -54.78789 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb106dc6-341a-302d-b108-f675a18cb576 | -11.20769 | -54.7858 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e29c78c-3ad4-3165-913f-d8bd6660b141 | -11.20697 | -54.79152 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 939daaad-bc3f-3a7b-aa1d-0e6ca9ddd4f1 | -11.20694 | -54.79357 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 693b38a9-59b1-3644-8f1b-a165dded12d2 | -11.20594 | -54.75901 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 664a5ccf-089f-39a9-854f-3cdeb1b9350e | -11.20574 | -54.76419 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea598621-bf09-3824-b52a-39b22edcd15d | -11.20557 | -54.76199 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b469e491-4568-3b83-a296-fc3bb4601b0f | -11.20535 | -54.7671 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 696cba05-1f89-3999-8ca9-5618f7e6f861 | -11.20497 | -54.77001 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38274d73-8134-307f-802a-07e74b49ade3 | -11.20382 | -54.77863 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c8cc0ed-dccc-363b-b69f-1dc1c89035cf | -11.20306 | -54.78441 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4343e45-4fd0-3219-9187-6468f870c5c5 | -11.20303 | -54.7823 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 207aa6fe-4d45-32b8-89a1-808b350a40c8 | -11.20267 | -54.7873 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58e1594-6dd4-3d99-95fc-4566992a5f84 | -11.20231 | -54.78807 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f714aca0-5bf8-3732-bf3e-90aa5446f9de | -11.20195 | -54.79092 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f110c668-86c0-3713-b5b5-b0422d273788 | -11.2019 | -54.75459 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d163c7-2472-3f44-999f-f8645f685490 | -11.20151 | -54.75757 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 897a5791-9c55-308e-ad26-1ac367d90e6b | -11.20111 | -54.76055 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a13645aa-8679-3504-82b4-3e545a71caf7 | -11.20072 | -54.76351 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 460de0dd-ac07-33bd-9d9d-35b9bcee61ff | -11.19995 | -54.76937 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3960c0e9-afd6-36aa-a95d-0a8d00b371fe | -11.19956 | -54.77229 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de2c6f58-4b70-34f1-8956-41f35a47402d | -11.19918 | -54.77517 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 627f4371-487c-324d-a940-26d34724be59 | -11.19765 | -54.7867 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 837101be-7ebb-39ef-ab15-ce0103a1333b | -11.19649 | -54.75686 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad202bdb-a0e9-3e5a-8207-b4ce1f2ab60e | -11.19609 | -54.75984 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e517c3-ae5e-3ba5-b38b-cb4e36d6a21a | -11.1957 | -54.76282 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3379f6ce-e6d8-3e46-b970-529f0ecd7110 | -11.19531 | -54.76577 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61d922cc-f196-3ed4-8484-dd9aef3fe7d1 | -11.19108 | -54.75912 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e040d435-a0dd-3555-a5a4-748e87b2003f | -11.19069 | -54.76212 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfb7e9b3-80dd-3df7-bd67-c16eaf6f50d0 | -11.19029 | -54.76509 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49b4d676-3530-33e7-9723-b62f8a1d74a1 | -11.1899 | -54.76806 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b60a213-2ffe-3a76-9baa-2f8225d635c4 | -11.18489 | -54.76737 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8da241e0-f93b-360e-bc17-0658b00cadc1 | -11.67717 | -54.44551 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cabe1f51-198d-38fd-acd2-8e8847ef6568 | -11.67679 | -54.44859 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c417a4b-dc6c-3076-a415-e34f20ec23ee | -11.67238 | -54.44172 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a06de2e-e4b4-3601-9d74-55797a6f9089 | -11.67108 | -54.43938 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc0fcdc-1359-3943-9fc9-b8d62d2ec350 | -11.67027 | -54.44559 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10fe727b-387a-30a3-9971-23fe520dcfac | -11.32634 | -54.04469 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e0f050c-d911-3e1e-98d1-2153389cc575 | -11.32594 | -54.04794 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4896b06-5822-3b7f-a268-194a6ba60521 | -11.32188 | -54.03735 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df30b4b0-8158-303a-8e36-ad672afa50c2 | -11.32147 | -54.04064 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e70f4ed-92f1-3cca-8054-d4529110ac40 | -11.31619 | -54.03992 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0599d7b5-02d0-323a-9f6a-f376fbb81d1f | -11.31579 | -54.04319 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7df5add6-ef61-38a9-ba3a-a32c03906ce1 | -11.1959 | -53.89997 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d254cf8f-e6a7-32f0-968b-2af6587a7666 | -11.19546 | -53.90341 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 305cec2d-16a6-3554-8389-d66ee6d5afe6 | -11.19502 | -53.90684 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d32f08e6-1eba-347c-8a2a-f3bdf453a0eb | -11.19458 | -53.91027 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f960739a-0103-36d0-8048-006cced1817f | -11.19414 | -53.91367 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e0a969e-43b6-3866-9a26-0a10ac5c170c | -11.1937 | -53.91706 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b57d1568-6f08-39d5-9a1f-4eec64b2e3c8 | -11.19326 | -53.92044 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09f8c55b-e313-3b68-8849-862f7f6771d9 | -11.19014 | -53.90273 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5a63739-221c-336b-bcda-2b0dc9f7b14e | -11.1897 | -53.90615 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README117.md)
