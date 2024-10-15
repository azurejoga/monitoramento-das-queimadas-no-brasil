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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3180bbf-da21-3d47-9886-1c142f50bc45 | -3.20032 | -51.03666 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be14d3df-1767-39a5-ab30-fccc20ab8810 | -3.19828 | -51.02895 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e99edcea-7e9b-385f-8699-356025cbb435 | -3.19774 | -51.03243 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 931e2a6b-9419-31e0-b4fa-b34976f2747a | -3.19719 | -51.0359 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d8755a-87c8-3a98-a317-007fbb803d4f | -3.19664 | -51.03938 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d40667db-e7aa-310f-8fc5-dd13060dbff6 | -3.19387 | -51.03539 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f854adfe-964b-30a1-8e9e-f10374da8153 | -3.19332 | -51.03886 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29cb02c7-7281-3f35-9a44-beeee0e79abb | -3.19054 | -51.03488 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 211f6db2-4f29-34de-8986-d51abf945deb | -3.10898 | -51.3382 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 434daad1-c56d-3ff8-ae35-86d4a8a24b3c | -3.10662 | -51.28834 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5f4ef0b-3f0d-3ea3-b785-e02c1c86fd5d | -3.10439 | -51.28091 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e03c17-081d-3757-b1f9-3edeeb2a0703 | -3.10385 | -51.28437 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89560a00-83ca-3167-aa3b-824e52037098 | -3.10331 | -51.28783 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0ba01fd-7e69-344f-babd-3c914595c361 | -3.0776 | -51.19173 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1719ad7-eb1b-30f3-8ac8-ffd5e6dabdc8 | -3.07429 | -51.19121 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a710df4-772f-3a07-bdb8-fc2153df9285 | -3.07259 | -51.1803 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d90e0e-fd83-38f7-b99a-adba2edf5829 | -3.07205 | -51.18377 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a5b3e74-3cac-3163-8094-97889f24f37a | -3.07151 | -51.18723 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 206402e2-cd3c-32f6-ad67-6f0886424b36 | -3.06874 | -51.18325 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c3115a5-8d58-3521-889e-4dd8d6d01cd8 | -3.0682 | -51.18672 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f03c41a6-9311-31a9-95c3-9ef43304415d | -3.06241 | -51.26732 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1af434f-acf0-35b1-a657-19dc7eb46dc8 | -3.0191 | -51.21867 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3534619c-68ef-3a47-a836-94f7ef1699d5 | -3.01849 | -51.20087 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b76e2bf-1274-3719-a716-aca82c7b425d | -3.01795 | -51.20433 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d43b25b9-3e0b-3af2-acae-b18bf0151ce6 | -3.01579 | -51.21816 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 789d4bee-d02a-38fb-8c9b-d4080101c801 | -2.97597 | -51.36407 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c0d14a4-3f3c-34b2-9b35-dfffb2306a1b | -2.79048 | -51.65896 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4528296-7155-3f1f-a439-2667bba4c833 | -3.4711 | -52.10678 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2769b469-512b-337c-8a41-5fabd1359b79 | -3.45809 | -51.77705 | 2024-10-15 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed80675-77dd-36f1-a78f-c6781a0aaa1b | -3.37179 | -52.17532 | 2024-10-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2be524d-1897-3aad-a2db-cfe6821b3fb8 | -4.27531 | -50.9619 | 2024-10-15 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5beaf334-9af4-37bf-b7ed-8a0f985a19fe | -4.26583 | -50.95681 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfd83eca-fc75-33a1-98c6-61d91f031f10 | -4.26528 | -50.96035 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803aa2a9-f5df-33e5-9c37-2494ad7efe76 | -4.26249 | -50.9563 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19bb064c-3417-331b-8466-fb842b428487 | -4.26194 | -50.95983 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2618c875-ed38-36cc-b660-a88c233b1401 | -4.12618 | -51.11197 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cb8b3b2-c6b8-3420-b4fc-d9158f2ba8b4 | -4.12286 | -51.11142 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea041d90-ded4-3f93-9e9a-2c517f2ba263 | -4.12231 | -51.11491 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b8eec20-6004-3d38-9743-a7e9ac6bfa45 | -4.11172 | -51.09533 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 418719b3-78f4-3483-a29a-41d1deda6ad7 | -4.07724 | -51.07562 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1188a4-1962-3aed-946c-2c0680a7a091 | -4.0767 | -51.07912 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d55d2e50-f12a-39ca-b312-17cc838f4800 | -4.07391 | -51.0751 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a37e63-3687-37f0-9b36-f84ae500340d | -4.07336 | -51.07861 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cbe4231-5000-38e4-aa73-c8d67d556c3f | -4.07282 | -51.08211 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3ca340a-5c3c-3d88-8286-4b3653f2b252 | -4.07057 | -51.07458 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e511dcf1-d2ed-38e3-b453-c67485b60ab5 | -4.07003 | -51.07809 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 930c4ac3-78be-3b2e-b1c8-7537c930096a | -4.06949 | -51.0816 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82a932e0-d2bb-3be4-9178-2f882dea3b0d | -4.06738 | -51.11718 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 941a625e-955d-36b1-a232-73b798c6c081 | -4.06724 | -51.07407 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2061f349-b804-3df0-8e42-47781a419922 | -4.0667 | -51.07757 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09d982c-ee10-3d5a-8879-97a46497e356 | -4.06459 | -51.11316 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 090c9d2d-759b-35ca-8f76-384dca2806f9 | -4.03992 | -51.0989 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fabde6cb-1252-3e36-9e6a-8f2124bc2b42 | -4.03659 | -51.09839 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c16e2064-82d3-3183-a97b-aef0eb398f73 | -3.92088 | -51.23068 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b02d02-c8b0-3110-a7a7-e82f89ca342d | -3.8743 | -51.20209 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 945ffcf3-a20b-346e-a459-69420607158c | -3.85368 | -51.33417 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd2df21-7b57-300f-9636-5ed6c83027b0 | -3.85314 | -51.33764 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad65ab49-f517-33e1-821c-e087b0172bb3 | -3.85204 | -51.01942 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eaafff1-c103-3863-bd69-65a4be829ed6 | -3.85149 | -51.02291 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd3b425-e85b-3cc7-87e4-fbeae5504300 | -3.8509 | -51.33018 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af9d71ec-c9fe-34f0-b061-a954cb5f40ba | -3.85036 | -51.33366 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cd92a36-5e53-35fb-b537-d009ca14387a | -3.84271 | -51.36089 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89266749-d470-387c-bde8-f217b9864f03 | -3.84095 | -51.32866 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff795e01-9005-3c79-83ad-85fb84d87038 | -3.84041 | -51.33213 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51ac7f9f-bbf5-3f19-aa2c-e33874584979 | -3.83236 | -51.4054 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c372510-529f-31ad-9765-e9ae03dba259 | -3.83182 | -51.40886 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a91c731-ef47-382a-9de1-0c29649fcd0c | -3.82905 | -51.40489 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6066aeed-4b4f-3b54-9150-98001c38073a | -3.82851 | -51.40835 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66e0e432-3ecb-34df-bfe0-e203ad225be8 | -3.82797 | -51.41181 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b02998c1-1308-3222-8e6c-59fa07512efd | -3.82743 | -51.41527 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db3bc4d-7069-3ff7-b99a-3eafbbbfcbc4 | -3.82519 | -51.40784 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7caf903-d8e3-312c-bd07-d5502426ad29 | -3.82122 | -51.54174 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109ea458-8248-39bc-8744-ec7c80e19895 | -3.80414 | -51.19449 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44913dcf-ed91-3e09-8b02-1c45bd6c1f26 | -3.80359 | -51.19796 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec4580e2-e6e8-3cc8-9aa8-5b412219b727 | -3.80084 | -51.3899 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ea1f49f-8d39-3b13-acff-2903175f4c75 | -3.79613 | -51.09329 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d735ef28-a091-3b8f-87f2-b6b59949c3c8 | -3.71833 | -51.04892 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3508f2d-3afb-39a8-9be0-2994fe625a57 | -3.7108 | -51.2477 | 2024-10-15 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a2c36c0-c53f-36fd-abbe-415f96223070 | -3.68204 | -51.17194 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c030f8-a16d-34ab-9bc4-a468e834b42e | -3.68149 | -51.17542 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94291e49-532b-39e0-b5c6-207a93b706a2 | -3.67871 | -51.17142 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ced66059-b83a-3547-9bb2-87d06c910d52 | -3.87399 | -52.13493 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee9ab194-55ad-366a-8493-9d2c78efa81b | -3.86943 | -52.27154 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52eef597-9d96-3e24-b06d-149e5144af50 | -3.84554 | -51.75374 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57d8b9e7-184a-386e-b719-ec40c9afbdfe | -3.83029 | -51.87465 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81fb4bb5-945e-32f8-8944-0637867ad056 | -3.8222 | -51.85928 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81553db4-ef4f-32e7-92f9-32535698c240 | -3.82166 | -51.86272 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be98bfa5-4349-3050-b283-59eaebaee9f2 | -3.82112 | -51.86616 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f9f7589-0647-380f-bf29-892471f5f24a | -3.8189 | -51.85877 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcab2389-0d1e-3d26-893d-aa6806d49101 | -3.81836 | -51.86221 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba4b6b94-795b-3f15-aae1-d9e0dd5b59d1 | -3.81782 | -51.86565 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 999ff5f1-8e53-3ea6-9a9f-e3e2bd0e09eb | -3.81747 | -51.93248 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ae3709-8b4f-3400-9067-a155073b4158 | -3.81687 | -51.91478 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| facad3c5-e3a5-3350-a209-f814361b2dde | -3.81633 | -51.91822 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3305801-ae60-36e4-a6cf-a11dccfde4a3 | -3.81505 | -51.86169 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 685ac29f-507b-3000-9c00-14231544d6fc | -3.81471 | -51.92853 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dae48c80-c5ab-3b7a-948c-b7ac4bee94ef | -3.81451 | -51.86514 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 289ee42d-1797-3d56-8cb0-b8197015e90e | -3.81417 | -51.93196 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 584229b1-b6c3-3fa3-bb44-e01b7540130e | -3.81302 | -51.91771 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26dd3a2d-781f-3e06-b5c8-7df1e2b60cab | -3.81175 | -51.86118 | 2024-10-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README63.md)
