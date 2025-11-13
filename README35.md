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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f50012-f7be-3a9f-afee-985a4957ebc5 | -1.81062 | -53.81863 | 2025-11-13 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb1e07b1-03d0-38a6-94d4-c0d5e1c03f64 | -4.25279 | -43.78775 | 2025-11-13 05:01:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe7404dc-6333-3be9-a59e-32bf61b5ff8d | -3.34457 | -48.38728 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4276f41e-05b4-3d8b-811a-701f3b0149e5 | -3.09138 | -49.27909 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b79f1ed5-f4ce-3bc2-aec6-630afaa14c40 | -3.12405 | -46.04339 | 2025-11-13 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 084f0f81-bfcb-371d-b522-fe41a73c968e | -3.3831 | -50.13521 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 387b3ead-056e-373f-9a1d-8841b1e15767 | -3.09334 | -49.26829 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a0b71d-6ead-3723-90c4-96df9c719b2e | -3.29176 | -50.07821 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2c254fc-8bd3-38af-a675-c736fe74053d | -3.34695 | -48.39042 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 275552b0-69fc-3db0-adc8-db73adf792d1 | -1.96959 | -54.08177 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5252d37-71bd-33e4-9f1a-dd14ea1cc643 | -3.3439 | -48.39181 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7aaa6c36-c17d-38f8-92d7-84e8ef3fc423 | -2.87091 | -51.47376 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cf662a81-300d-3903-810a-47b0fd2d5cf0 | -3.27595 | -50.79891 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0bab171-2fab-32a8-bb33-0adcccea0988 | -2.85616 | -51.28136 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91619a95-0983-39b4-8ac5-6a42fc369793 | -2.00273 | -54.45469 | 2025-11-13 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4e3b3c7-d98d-3f76-a33a-3fd4ec7a4b32 | -3.09196 | -49.27515 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04ea3021-dde3-3ba9-9c39-0725cd9be7d9 | -3.08849 | -49.2716 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd3b0626-0836-338b-8fe2-5473c7c20b3a | -3.34525 | -48.38267 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e33c96f3-15fe-31d2-a0b2-2b16d9ecca26 | -2.63376 | -52.08348 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f13f17f5-418d-395a-908e-8ff47183d5b6 | -2.82552 | -52.87128 | 2025-11-13 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee4e3f41-9f50-36cf-902e-97894b75fea9 | -1.3711 | -55.39796 | 2025-11-13 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3684b88e-7d7a-3734-9177-a57102d6fee4 | -2.45734 | -49.27102 | 2025-11-13 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d942f10-eff5-328d-b9a4-5d2f115a09f4 | -3.00633 | -51.39469 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d621bb5-ef74-37cd-881e-e15e989ea1e0 | -3.08727 | -49.27945 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05ebe481-42a9-367a-84f6-0259a8dc7340 | 1.46024 | -55.85769 | 2025-11-13 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d2e47cc-1c5c-3e51-b965-d67bb79c8261 | -3.4416 | -45.58559 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a052f66-c641-32d9-9fba-f1968156a52f | -3.09619 | -49.27579 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d29dd8a8-db12-3c66-8620-6f0d82a7284d | 3.30094 | -60.12561 | 2025-11-13 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7dde890-4ad7-3e9e-b203-0361ca049983 | -2.86952 | -52.79338 | 2025-11-13 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2539f54b-17f8-3fd2-bb22-db9d88ede470 | -2.63361 | -47.30027 | 2025-11-13 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f555b6a-c230-302e-a04b-a79a7686e448 | -3.43572 | -45.585 | 2025-11-13 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de1cfd08-54cd-3403-8b97-70442a492e10 | -3.33863 | -48.38446 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9e53499-48c8-385a-aee7-536b57dc57e4 | -2.16987 | -48.36917 | 2025-11-13 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3be649d-b28f-312e-b02d-9ef850a009e7 | 3.30161 | -60.1301 | 2025-11-13 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b36f53da-f2bf-307e-9aab-715a7f962a74 | -2.55406 | -49.11833 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b03ca4d6-95f5-363e-9142-d57cff9f07b1 | -2.82493 | -52.87503 | 2025-11-13 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53251175-5554-3ce9-afc1-bac9f7ddea67 | -2.86355 | -51.47263 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 320b06db-e78a-342f-8235-47caae7d70d9 | -3.13982 | -50.28029 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44653469-dbe6-3d43-ae00-6be6fcad972b | -2.87025 | -51.4781 | 2025-11-13 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0b5e05c-e853-319e-872d-b26e907e2290 | -2.52546 | -51.04443 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba937e93-d561-3111-9889-301e5d677c6b | -3.09573 | -49.28073 | 2025-11-13 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33d8dabc-8a5d-3c50-89c2-0ab9a9caea5f | -3.1524 | -50.26839 | 2025-11-13 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cbd00b5d-e725-3cf2-bc0d-a1413d21d385 | -3.34073 | -48.38197 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5bd0fda-ee9e-34c4-993a-2caad06e794c | -1.9369 | -52.09602 | 2025-11-13 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78866b71-5e9b-3217-a44d-cfc798311feb | -3.39872 | -50.17692 | 2025-11-13 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09790b9e-9d5a-384d-86ed-28549a05e577 | -3.34315 | -48.38518 | 2025-11-13 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7387e25e-3154-373d-88ca-e0b0fa2f8913 | -1.65657 | -53.19701 | 2025-11-13 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cf94bcf-ac14-32ff-b8db-c2eaf153613f | -5.84222 | -38.34634 | 2025-11-13 05:03:00 | AQUA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 9a1d05b4-4c74-344c-8e64-722bd111ee85 | -3.45772 | -53.04258 | 2025-11-13 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4998604-91bf-3282-866e-005b2426e0cc | -5.44276 | -44.65605 | 2025-11-13 05:03:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be06bec1-b7f6-3fce-82b1-24f852d39129 | -10.37362 | -45.05821 | 2025-11-13 05:03:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5acf247-0949-3069-83ba-da65fc806a1e | -4.82793 | -50.62325 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad30eeb4-06e4-32a0-a865-589d6096784a | -5.85196 | -46.44697 | 2025-11-13 05:03:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac254800-12a8-3048-8230-2f83cc4668f2 | -6.14088 | -48.0592 | 2025-11-13 05:03:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51855b89-d0b5-301a-b37b-2ddf71dfbb3c | -5.38287 | -46.76381 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc6fd9ad-7384-3d95-a43a-daf78721effd | -8.72825 | -49.59665 | 2025-11-13 05:03:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25118ef0-a803-3f1c-9b59-bff41a596067 | -9.01471 | -45.43667 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bf847bf-d0f6-3303-8b3b-62ef3d89fc10 | -3.86367 | -49.80089 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b65e6223-b4f5-32e4-ae93-353f90d5f1ff | -7.14289 | -49.12933 | 2025-11-13 05:03:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed3bd99-3c66-370b-be88-8f431dc80084 | -7.22557 | -47.98608 | 2025-11-13 05:03:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb32831-591c-3709-9815-e6a752efd135 | -3.70347 | -49.03052 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0511a5f-7b11-306d-ab2c-7269a0374170 | -8.86306 | -49.94359 | 2025-11-13 05:03:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9b573fd-a2a9-38c2-b3a6-44e25ff04bab | -4.743 | -50.72995 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d852a2f-c780-3358-9042-c1d64f901aa0 | -4.24244 | -49.67671 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b780a3b0-c8f4-3695-840a-ea8fd7b81d5a | -4.21249 | -48.56996 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a2280905-a2e2-38c8-b0c3-1e639e871710 | -5.68335 | -46.01301 | 2025-11-13 05:03:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ba114b9-f25f-3c63-a81a-302322ac0da8 | -3.63812 | -49.83262 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4b81bb-3390-369d-91e2-69e6fa6ffe30 | -5.57409 | -47.10294 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2debdfe4-34ae-3f66-9253-8e966e1fdd4d | -4.60999 | -49.28842 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b95e0be5-bb29-308a-84fe-a5c90b29da3a | -7.26023 | -45.37405 | 2025-11-13 05:03:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a76b0fef-1062-3350-adfc-91f9dffce323 | -4.2096 | -50.09515 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9161a4e9-158a-3512-921f-64add4392c6f | -6.6897 | -47.802 | 2025-11-13 05:03:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c2461e1-dbae-3462-abfe-8ff76c282202 | -3.29185 | -52.11196 | 2025-11-13 05:03:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e24faf9-0d32-3508-911e-4c195853ac29 | -3.68235 | -54.55519 | 2025-11-13 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59e5195d-ad11-3c16-a192-02f57393808c | -4.0974 | -48.02018 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e22f253-ffa9-31ce-af32-2c30acc39855 | -9.63493 | -44.55149 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3794b816-425f-38ba-a6c4-c787ed038bea | -3.70285 | -49.03469 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a7a7247-8071-3203-b679-6609dffd0b09 | -4.01143 | -48.80723 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94ebc391-4131-3b1f-bdfc-b29d3bd5b7f5 | -4.45269 | -46.55868 | 2025-11-13 05:03:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3887e02-7454-30e9-a22b-f46086d34014 | -9.64129 | -44.55256 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce05d94-2756-3c9d-b68a-9769237b4df4 | -5.57121 | -47.106 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1bdd32b-97b0-31c5-b663-32110eeaecee | -9.32674 | -47.84059 | 2025-11-13 05:03:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 036e4afd-b9f7-34c0-bab3-2b41d1cfef2e | -4.1464 | -47.65759 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c481444-d416-38c7-b57f-89b6d9df6c0e | -4.10209 | -48.02087 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c7f1a35-e159-3108-a6ee-a2e0cecbfc78 | -4.88995 | -48.96975 | 2025-11-13 05:03:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94022b49-cf30-3d8c-a37f-d2d736aa0f69 | -7.22066 | -47.98528 | 2025-11-13 05:03:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85851da7-4aaa-3fab-9e02-d36cdd49da81 | -4.20607 | -50.09089 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0653de94-ddab-3708-a7d1-541bed3c7f81 | -8.40653 | -48.05477 | 2025-11-13 05:03:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fcec9fe-4a0d-343a-87c8-ec43686ba50b | -4.71846 | -49.24514 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d155b811-d77c-3998-a184-7ec4cc27c6d9 | -5.5716 | -47.1032 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e84a351-3e8b-3c56-b46c-f730b4022eb3 | -8.94315 | -49.82499 | 2025-11-13 05:03:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb0e4aca-651e-380a-9663-05dc4037dab3 | -8.20518 | -47.88586 | 2025-11-13 05:03:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f33619a-f74a-3f9f-b072-40984928cb7d | -3.75266 | -52.14301 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e06284c-c16a-3890-92da-2d0cea986c08 | -3.78242 | -52.1643 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23648ede-62e4-3553-88b9-d406b224791e | -4.71029 | -46.45048 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c924702-7fa0-3df0-bc44-f57e2e914e79 | -3.88049 | -53.63649 | 2025-11-13 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 431847f7-8ba9-3a5a-97f3-b0548f3f703d | -3.08017 | -53.10424 | 2025-11-13 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69927f3a-7a56-38d3-9e62-156101f64255 | -9.3522 | -46.59587 | 2025-11-13 05:03:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 221bb674-b8a0-38ea-aaa8-de60d13d6437 | -5.38766 | -46.76753 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d517d894-cb2a-3f6c-bbff-68eec94a8d0f | -9.63006 | -44.55568 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README36.md)
