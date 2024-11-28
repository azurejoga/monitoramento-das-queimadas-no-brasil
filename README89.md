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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0c9035b-e038-3952-aed9-87c920ab5610 | -2.94283 | -51.59112 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eca1e320-4a2a-3d88-b93d-888b1feb03a2 | -3.33524 | -53.72351 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49132986-9a9c-3837-9e36-8b66cc787dd6 | -3.05471 | -54.03313 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0854265f-651a-3ebd-bc42-9237fd38cc96 | -4.48137 | -48.11512 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f8f9d5e-43ad-37cd-a208-e30940bc5e04 | -2.52375 | -54.13647 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f79178a4-c61b-356e-a203-aed1869cd2ea | -3.78668 | -50.13322 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b50a2ada-caf5-3738-9e2e-63726a0e1011 | -3.10362 | -50.36125 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2e11d1f-5d58-3cb3-8eea-1195de0f52a5 | -3.48452 | -54.66948 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9dba4f5-37b5-3c4f-b27c-ac66bb9d1ed6 | -4.09006 | -54.76662 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a13edfa-762f-361e-aeb5-bac337b4e02a | -2.60664 | -54.27589 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae5c79f4-7635-35c7-bad2-6a53f257d433 | -3.1619 | -50.58092 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ee056b4-d4a2-365f-b499-241eaf80c9fc | -3.71804 | -50.54069 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e55ced4d-1bc9-3157-83e0-df4114874967 | -3.62734 | -51.49964 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da2e5663-6f0f-327a-9b9f-88ee35c57ce8 | -3.43577 | -51.43206 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61538196-2866-3bdf-8aa9-a6859d5587be | -3.08209 | -49.21449 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92fcc5a7-cc25-3007-83d2-45652570f13b | -3.65174 | -51.39924 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07127a31-7c0f-3977-837b-f6aa563fb841 | -6.54442 | -55.08088 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f417435c-1b1d-3c41-8f64-001af59fb7f2 | -2.18383 | -53.68844 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a8531ef-4328-3c5c-a058-5847ee8b2db1 | -3.24022 | -50.7668 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8425c904-d636-3a6a-a9a8-457c151b41a7 | -3.24709 | -48.47834 | 2024-11-28 05:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 426923cf-3144-3b3e-8203-cdb09dc4fbee | -3.32847 | -50.22244 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 728b34d4-086d-336e-b3d8-4c9b4aeefb73 | -2.5903 | -53.97396 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bbaf7ad-fd4c-3f14-bc84-410ec96c27a4 | -3.12653 | -51.04503 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da04c5bd-b5e6-3c08-9379-162b84b664be | -2.87062 | -53.9833 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 596a18f3-5643-3e50-947b-dff9bf97e0e8 | -3.60012 | -50.36251 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3520887a-d90e-3943-b93a-8aa679c86c77 | -3.14969 | -53.24823 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a793307-9978-3c86-b6c0-4e09a5819b68 | -3.6222 | -53.51534 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae5e302-3adb-39c1-8b9a-9cba46f95d1e | -2.85812 | -54.0292 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b05fe5f8-52a0-3abe-a18d-e834602583fc | -3.22691 | -54.09286 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2bdf6bb-4157-3e98-adc1-1e6797339dbc | -2.31199 | -51.95995 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53a3f959-8762-3167-acc0-69f0b1869909 | -3.69699 | -50.22637 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a2b1e90-b2b6-36f3-8d4e-68271b14812d | -6.67347 | -47.87594 | 2024-11-28 05:18:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c595de57-4afe-39f6-8111-cd99083975b1 | -6.66729 | -47.87513 | 2024-11-28 05:18:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d88ccfab-93d8-3b1d-84fc-a73eb4f76d27 | -3.27459 | -50.61526 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f1c37d2-271b-318f-ae9e-f68ee4dd274f | -5.98743 | -45.35702 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 95121ad7-f350-3c33-bb18-c6f59b855970 | -2.80529 | -53.04358 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5592320-11ee-3ffb-9e78-7a68ea093585 | -3.17394 | -48.58384 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28366fe7-06ac-3af2-929e-41a8d53ebb04 | -3.03219 | -54.02481 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8cb8ec4-b55e-3bef-9daa-8b4808ddf846 | -3.17801 | -48.43605 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8526914-aaa4-3431-98dc-9fe09a72505a | -3.84009 | -51.70971 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109acd89-be58-3dd1-9183-527bd7963ff2 | -3.31019 | -50.27997 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a8fdccd-256f-33eb-9e18-36659115e605 | -2.20456 | -54.52132 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff47b1c0-46ef-374d-a90e-01bd95f7b13e | -3.28654 | -54.7441 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3238f456-4fc2-339d-b3d8-3e095ce3a81e | -6.09405 | -48.03888 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fcc0afdd-dbf2-32ce-b572-daac62760bfc | -2.17305 | -52.13865 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d7598b2-2adb-3fb5-a563-404fc1a9e5f3 | -5.5145 | -46.26593 | 2024-11-28 05:18:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9085f7c-429f-379e-8e62-83ac04055c15 | -3.78114 | -50.13545 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df2ac320-7190-313c-826e-9e400015309b | -3.06003 | -53.29047 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b18998-b344-3c9a-b10e-5cab2b10d2b2 | -3.10328 | -53.82081 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e223fac4-a307-3e04-97c9-a6316ea44ac4 | -2.96076 | -53.88683 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da116212-031d-3ab2-a0b2-5523a2e02391 | -2.58764 | -54.09512 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84333f15-3c89-33a4-8d95-51bd8d719d41 | -3.11678 | -53.75968 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92f4f38e-6f19-3f3b-b4a1-f8744b1c64aa | -2.2608 | -53.47385 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ce0824b9-4a3e-3983-85a4-a6255f55fb1f | -2.72696 | -48.9003 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 76669f92-be5e-3afc-b491-dad080132258 | -5.09151 | -45.84141 | 2024-11-28 05:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e50a6837-91d5-3dae-bf24-a5ed8dc846c9 | -2.87345 | -54.00692 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad15e8e1-5e47-3665-a9fe-53c9c19504f5 | -3.38604 | -50.11064 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| deaeedc4-6f45-3e90-8542-dd294539670f | -2.18078 | -55.14112 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55185c6a-ac2b-3d3c-848e-e550fb96f557 | -3.63547 | -54.44086 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c1cbc59-fe6d-3c06-a5a5-977c7844ec1f | -2.85649 | -54.01414 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c77e6363-724f-365c-aa3f-b392661ed63f | -3.06199 | -51.28977 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d08003-ae59-3a76-8a93-913dea4f3120 | -3.28106 | -53.84018 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54906ee2-c55b-3b87-8edc-5de57d555c4d | -3.97032 | -48.08441 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a27dcff6-4b42-39b2-91a6-91823b610545 | -3.24383 | -50.20745 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ae8610b-47da-36b0-b36f-93a733e3ac60 | -3.33955 | -53.28739 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b73e822-22a8-3454-b222-59c26c342f7b | -3.60912 | -51.15662 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e411c16b-00e6-3930-9c64-c9e91f356b70 | -3.20187 | -46.59677 | 2024-11-28 05:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| de38b4ff-60f9-33a4-a3b1-9b7d82787755 | -3.46171 | -54.48793 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6b6a77f-e182-3416-98f6-5c9aff4b3d4f | -2.65829 | -49.50413 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d8276d5-0181-3cd5-a716-7d3c42535811 | -2.83888 | -51.84189 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a57363be-7ec6-3ba8-bbbe-ca269b17fc90 | -3.28652 | -53.83077 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a98b079-1a61-3bd5-8d59-2be24b0ef113 | -4.19317 | -50.68493 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 541838b1-31a8-3fb3-9e96-11498d985c62 | -3.96391 | -48.0874 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b8332f93-fe72-3a48-a376-7b2ee710faa4 | -3.24189 | -50.76483 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d51eb724-3b63-3d9b-b312-8bed3c4edad0 | -3.15951 | -53.2385 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fce19baf-079f-307b-9040-11abc5a758f0 | -3.08383 | -50.25109 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0733e855-f44b-35b8-b913-b1e0aeab804c | -4.0533 | -50.87084 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ed4389-6335-3a38-ba3f-33beac331abb | -3.11138 | -53.25338 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cb129f4-ed47-3575-bb6a-e5cbbb91be60 | -2.98805 | -51.44464 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f9097345-15cf-3816-86d3-c35138984e99 | -3.28575 | -53.83579 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 347eddca-cc4d-3fd8-ac88-c331ce903650 | -2.84372 | -54.07126 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3c941d0-46bf-3abc-84bc-0990e7ddf7ab | -2.60653 | -51.94847 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04cfc98f-c738-37a6-afe5-c4ab1fab2972 | -3.61707 | -51.53709 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a9e6af8-80f8-3d99-9034-465ebf7539e3 | -3.27253 | -50.61145 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0186172c-e020-3e0a-8811-4e5e7df3cafd | -3.4969 | -53.81955 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38f243d5-bee1-3518-8a5c-15f507b5ab3f | -3.0706 | -54.41012 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46d5b0f8-abb6-32b2-9d15-a9871dbdf569 | -3.0442 | -48.51775 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b627fcf5-9da7-37dc-8ead-44a1f5e422ba | -2.74509 | -48.66405 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f131f152-c2ac-32de-99ab-436ce5f375c6 | -2.81175 | -54.02214 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 693cc345-ab6e-3ed7-8e06-c8bac2c58269 | -4.22707 | -50.88215 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83c68e7e-2916-3ae7-b390-334ea0c997a1 | -3.06745 | -49.20174 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9c5e429-f24f-35db-8252-961a9f71babd | -2.23992 | -55.88527 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 642514d3-1e99-355b-9ee3-2943cfb1fb1d | -3.64708 | -51.39848 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11cdf2a4-ac79-3fa9-bd66-cdb333cbb417 | -3.59593 | -50.35624 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc5179b9-6a11-3d15-83c2-42bc6f2a6837 | -3.38737 | -50.10154 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 551d9915-bb8e-3dcb-bec3-2db05705dedf | -2.8232 | -51.79408 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3aba119-40da-3654-aa45-0f42a9559239 | -2.84019 | -54.11954 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4e98947a-3187-343c-b1df-ad2ba2c3b590 | -2.7288 | -54.1385 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1b51476-911f-379b-b68e-a6c0697375e7 | -3.6163 | -49.89655 | 2024-11-28 05:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbddcc5c-64c9-3b17-b66b-4c4681ece4f2 | -3.11599 | -53.76177 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README90.md)
