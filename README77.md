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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 132d42b3-bb79-3990-8f2b-b0a51a5cd6f2 | -6.70985 | -49.46953 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15ac3278-da09-3246-a0ef-7f7812840126 | -6.7089 | -49.45511 | 2025-08-29 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47957c0b-df6c-3fbb-9107-8523b999da5d | -6.96981 | -59.33043 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 33c230d8-e38e-3bc3-b52a-0415939b550b | -3.53102 | -52.98932 | 2025-08-29 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06f158f2-64e9-3807-9973-c8c1d931f86b | -3.76371 | -54.81229 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3cce2c7a-d7a7-3dc9-b51b-c1845ea70831 | -3.42356 | -49.05149 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f9c2a2c5-4b13-32de-808e-6b1a37fc4c72 | -6.97758 | -59.32745 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6c1bb41-2aac-37fb-a683-33a7e99bb9fc | -5.14785 | -60.37218 | 2025-08-29 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbe9717f-f496-3e42-8d25-72510a1632b9 | -3.66486 | -50.95377 | 2025-08-29 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e1cccb9-7c93-3664-b0c6-442b3440727d | -8.56388 | -51.31814 | 2025-08-29 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87325668-c665-3f22-b269-a62eb8db41ad | -6.80092 | -58.9887 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c91814fd-a0a6-339a-9591-bb714dd15493 | -7.7267 | -50.28868 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54fe44ec-a099-30a2-901d-8353caacacee | -6.0006 | -57.85315 | 2025-08-29 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04afb1d8-a6b7-34df-84f1-a5464b0bf144 | -6.39353 | -62.91068 | 2025-08-29 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5e686961-d700-3317-8fc4-4cd54f3b9058 | -3.75851 | -54.81597 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 732a38ce-f774-3c0c-8d49-64206cc4ac91 | -3.41777 | -49.04488 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 07dd7e12-5fbe-32b1-aa1d-4a804866e80d | -6.70311 | -49.46864 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 429b8f60-74ae-3de6-be9c-2c5751289738 | -6.9835 | -59.3367 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d39dc583-3037-3f6b-b03c-43ece5853f63 | -6.39409 | -62.90719 | 2025-08-29 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0042c86-8b56-3850-89aa-51d4f0e104e2 | -3.76237 | -54.82114 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| ea5b4f69-961d-3d2b-8b34-e578838aa293 | -3.75716 | -54.82494 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfb16396-7aae-3923-8610-5ca3b58f1ce6 | -6.97992 | -59.33616 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98f6fd31-ba44-3c4e-aaa2-df6d3afdb1b8 | -6.70233 | -49.47466 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9ebd5e3-7ee6-30e8-9a98-818381c0fdf1 | -7.72149 | -50.27807 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba228710-c88d-33f7-b03c-8c40c184f18e | -7.72741 | -50.28331 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 149fa38a-f899-324d-b2de-612bb976fa80 | -6.70389 | -49.46266 | 2025-08-29 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69dea488-26cd-3a6b-87ad-7139007b89ff | -1.7453 | -54.51641 | 2025-08-29 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08733fe3-761e-3941-8e95-90fde1171a50 | -8.70055 | -50.36899 | 2025-08-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d579054e-6522-3725-a56e-211eaa530d8f | -3.41694 | -49.05054 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 589d0cbb-ce16-300e-a4cb-c16a9f6537f9 | -5.27136 | -60.40943 | 2025-08-29 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6888d56-dabb-3fdb-9af3-2f2dcb6cd7f1 | -6.21032 | -55.66857 | 2025-08-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566920a2-c1ec-3b13-9446-41e95b0b1390 | -3.76169 | -54.82567 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 9d9e9163-1e2f-3ca5-9443-006a2bc52caf | -6.70643 | -49.47313 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7a086a9-e611-3ef0-983f-a314cd8b8955 | -4.22725 | -56.00502 | 2025-08-29 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb837b2-06b9-3c64-b9b9-5dac774172ef | -6.00827 | -57.85432 | 2025-08-29 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56221013-fe55-32cf-9811-08fc7245a6bc | -6.39076 | -62.90666 | 2025-08-29 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e00a7d7-f888-3eec-ac52-18d35e8de1b5 | -7.7208 | -50.28334 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07e09aac-b257-30dc-8a36-59ddcd07aff5 | -6.71064 | -49.46351 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 867fed28-0815-34f5-a2b8-6298c76a8434 | -6.77508 | -55.48764 | 2025-08-29 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64f4f56b-6165-3ac0-b2de-29920422b0a8 | -6.9793 | -59.34027 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45de7776-8b32-3f2b-acbd-f7242a7303e4 | -8.55814 | -51.31157 | 2025-08-29 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f227aac-8eb9-324b-8cc2-d842175832b8 | -6.97867 | -59.34438 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88473b29-9428-36ca-8913-b1548ad7b452 | -8.70071 | -50.37223 | 2025-08-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5e999f83-2f85-3dbb-ad37-98b8c2714afd | -3.79217 | -49.43351 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 686188df-6d9d-396b-9d10-705e9d6a5a00 | -6.97339 | -59.33099 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35aa5ee1-00c1-3153-9af3-b14ac99b6356 | -8.55761 | -51.3158 | 2025-08-29 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f13ed1ec-0b34-35b8-9b50-ddc365d1d245 | -7.74152 | -50.27469 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eee5f1c7-6cbd-3143-b290-43f85d5aa164 | -6.98288 | -59.34081 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9673109-437a-37cc-9ea6-7bbb050f2b15 | -6.97696 | -59.33153 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 063e7f8c-65c6-3024-a3b2-1f5703c1c8a0 | -6.70467 | -49.45661 | 2025-08-29 05:27:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9ec680d-f980-37e0-96f0-d6662aaef2ee | -6.70906 | -49.47556 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4847acb8-7097-3aa5-a09b-87c37c421d9e | -6.70725 | -49.46713 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46b13bc1-f905-3463-9aef-3a6dc5683e12 | -3.75784 | -54.8204 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9790a606-9c95-360f-a229-d22232aacb01 | -6.97634 | -59.33563 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a9e673c-8ca1-30b1-aecd-1980f4f70aa6 | -3.42439 | -49.04587 | 2025-08-29 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cad3fa17-9b22-3583-bcdc-2c3262d591d8 | -6.98225 | -59.34492 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afbc931e-50d8-3fc7-804c-d626b222dd82 | -3.98221 | -47.88521 | 2025-08-29 05:27:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62a579fe-694f-3e2c-9ca1-d6b4f997290a | -5.99677 | -57.85255 | 2025-08-29 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42b7c392-9f07-3bb7-bf93-e08523ca1409 | -6.70807 | -49.46113 | 2025-08-29 05:27:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 642e5d9c-7ce6-35bf-891e-a52367c5de31 | -3.09822 | -54.59511 | 2025-08-29 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4547b6-1151-3bc7-b3c7-4dbbeffdc22d | -7.7349 | -50.27475 | 2025-08-29 05:27:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63c543af-19a7-3f05-8828-ec60dbade169 | -3.98566 | -47.88689 | 2025-08-29 05:27:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cf76154-0c6d-38c5-8638-97f05846b4b2 | -6.98645 | -59.34135 | 2025-08-29 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 305bb4f8-5ff0-3a12-ba88-2609b8acb6c2 | -3.75917 | -54.81154 | 2025-08-29 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e712b8-cb58-3c99-97eb-7d5e1a71ecef | -8.70643 | -50.37527 | 2025-08-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd522e4a-8c0d-398e-bd1e-80f2672731e0 | -8.55825 | -51.31333 | 2025-08-29 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02d684a3-b8c8-31bc-8052-2acf5b50b009 | -8.7071 | -50.36982 | 2025-08-29 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a6728e2-c9b8-30c3-bde5-886a0bb46710 | -8.55217 | -51.3119 | 2025-08-29 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef2d29cd-7c73-3d3c-8aa1-9881cd460c8d | -3.46554 | -59.31128 | 2025-08-29 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 421674b2-c90a-3087-aa81-5f88d364d2e4 | -3.53052 | -52.99257 | 2025-08-29 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a39fde4-98c5-3d9e-9292-7be8a608608a | -9.16337 | -59.55557 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ce28a7c-143f-3acb-a46e-cd19efcc4e1f | -11.22794 | -55.07041 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4ca652a-1b8d-347e-916a-ba1c7509f7c2 | -8.69513 | -62.46881 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9e91a41-c190-3b30-bcb4-870f3c75aae2 | -10.14848 | -64.24817 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8366b4a-017b-3a4e-a4d6-a300237ac0a9 | -9.10703 | -65.79668 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3723bc8a-1ae8-3772-b38f-25e86b56b937 | -9.22275 | -60.80766 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6beae001-4234-3c8d-91e7-46936cc9d834 | -10.52953 | -64.3689 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba86b7ed-d8b6-36cc-a8c1-db5082e169a2 | -9.13273 | -65.79676 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5a61521-cc1f-3e5b-b89f-6d0b8bb1413a | -8.09302 | -71.24857 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e686c983-a399-3533-a799-322095bbfc8c | -9.05099 | -65.73653 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a90856ce-d742-36bc-8993-cce281eecaf7 | -7.65886 | -69.93346 | 2025-08-29 05:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a49d6d7-ee0c-3557-b31d-90846ae23f99 | -9.79241 | -64.24178 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a99d4d3-0fe6-3804-94ff-81fe1bf15c70 | -14.33855 | -53.32746 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 647c6577-5127-3c18-802a-e58cc71d5809 | -14.34919 | -53.23387 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df86442f-46f8-3efb-bf22-95279aed2769 | -9.6676 | -65.03225 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6828ee50-4990-32c3-a439-287b1b593809 | -9.17526 | -59.44838 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17c61cb0-ed61-3b2b-931f-4c8c88024fa8 | -10.3802 | -57.83243 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e761c92d-f0d3-3b75-9d07-977dbc6f9a7f | -9.46446 | -60.30286 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c39ba39d-5969-3482-95ce-dfb788342095 | -9.72686 | -64.90628 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b85e59be-7f52-3d3c-b846-57cc26210e2d | -8.18134 | -61.36543 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b20822c-8199-3a1c-b678-140105460d5f | -9.10618 | -65.77962 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2049b0dc-d1b0-317e-b330-1e6aa1efadd5 | -8.24915 | -61.49666 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d6ce59c-f28d-3ad4-8b7a-cc70dd5e5c5e | -9.11418 | -65.79787 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 551b770b-61b2-3591-8038-e9c2f429a774 | -9.15845 | -59.58929 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1edb4363-4e57-3266-b4af-9e2673ca16a9 | -12.93241 | -56.97602 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ea5fded-f120-326a-ad09-644cde0c7e3a | -13.00241 | -56.91256 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf44880e-14aa-3c49-96a5-6f142f47d990 | -9.088 | -65.73447 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdda08f3-2e61-379e-ae11-26ee14bf296a | -11.22868 | -55.06467 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8588d3d8-092d-3a20-8f5f-114c5f9ec804 | -9.133 | -65.29015 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0689a456-f5ff-3deb-9db0-08e93067baf5 | -9.19668 | -61.02557 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README78.md)
