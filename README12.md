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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a27ad72b-3b90-3781-b182-81bbcf896ee4 | -5.43095 | -40.66555 | 2025-11-15 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb8d9e5b-a848-3eb9-ada9-f62adf195751 | -3.37246 | -41.16984 | 2025-11-15 03:34:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bcf374de-4940-3960-99db-9d3d87761b7d | -2.73295 | -45.307 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5f1906e-6977-34c4-9b99-d2abe5ed356d | -4.59116 | -44.32202 | 2025-11-15 03:34:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7fc62ca8-1e3c-366f-8b34-11a34f0b1161 | -3.28055 | -45.46483 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6742e4ff-68e2-3f5d-a319-380a164afd97 | -4.05233 | -46.42292 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc5c90bf-a9a0-3029-8598-3188db57d9d3 | -3.284 | -45.46671 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 379720c3-3b02-3b02-84bc-352a17b77827 | -4.53931 | -43.22125 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 45f39e9c-8ee3-3507-94e9-7a51eac16524 | -5.51049 | -40.54753 | 2025-11-15 03:34:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ff371503-a2cc-3c5e-8869-63051290fb38 | -2.73494 | -45.29542 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b1704d4-654e-3a44-acfb-dff02077b533 | -4.70527 | -40.12433 | 2025-11-15 03:34:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8b33630f-c3cd-3d0a-a743-fd086df2d511 | -3.90741 | -45.79816 | 2025-11-15 03:34:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63b232c7-465c-397b-a63f-129ef4951e1f | -3.4613 | -40.5049 | 2025-11-15 03:34:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c00564c0-8d13-3627-80b5-5c1ec87eae61 | -3.99211 | -44.28396 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c40ce43f-2ae4-3fba-8f62-329e8a645d55 | -4.91527 | -44.78325 | 2025-11-15 03:34:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71079d07-ec6b-385f-a217-99ca4744d0c6 | -4.26218 | -46.83363 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef53b23-8bdc-3c5f-af29-53b3ec028016 | -4.35214 | -46.49459 | 2025-11-15 03:34:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6909f392-f577-3b38-88c2-dd99a1b60b5f | -5.03576 | -43.60475 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 65d88f0a-10c5-3e1d-8c52-312f6caf72ec | -3.47187 | -45.6494 | 2025-11-15 03:34:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86b4f9c9-e709-3a7b-9247-ee591168e15f | -4.5463 | -43.21455 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| da1adeb5-d595-3ffd-befb-d745f99a727d | -4.27138 | -46.84282 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1c4040a1-68be-30a8-a145-9a35c3458fc9 | -4.54072 | -43.22525 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ff74c215-181d-3373-a5b4-5d1ff132a8f6 | -5.04155 | -43.60573 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a756af5c-5235-3859-b332-285e849c324e | -3.22528 | -45.48508 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb8fdf59-5fd3-3faf-927d-107f7f797865 | -4.26553 | -46.83431 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96d4550b-6ddb-3330-a7c7-af4286f20969 | -4.54709 | -43.22236 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 266699a3-bbf2-3099-b7be-4558385d4735 | -4.58088 | -43.39972 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ae4bbbf-0e8d-3a54-8f62-0f925d6a7d74 | -3.22626 | -45.47921 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f302af5-0d9d-350f-98a5-1aa3c898b13a | -3.99544 | -44.26474 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8416a689-9db0-362d-a620-453f9dd5ce4d | -3.47519 | -45.65443 | 2025-11-15 03:34:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c68792da-d800-377e-aee8-bc257f9cafba | -4.85884 | -43.25495 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c61220e8-a303-32bb-a53a-f3181c0d1d04 | -5.48267 | -40.97266 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bd0809ff-7577-3d89-8e09-123b832294f5 | -4.53496 | -43.21242 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716bfade-8499-30e2-954b-efff0cf07f8b | -4.90489 | -44.04512 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cc7432c-72e2-3920-afa5-ccd8420efc0e | -4.58013 | -38.36116 | 2025-11-15 03:34:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93250b22-f09f-32c4-9a9a-145da26f88d1 | -3.28154 | -45.45903 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 04d58423-d0b8-3720-b57a-ed3041a11917 | -5.42623 | -40.66475 | 2025-11-15 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 81565322-f932-3289-9d6c-98a60abc1498 | -5.42717 | -40.66722 | 2025-11-15 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca1bae59-b7e7-333d-867a-ca84fe1de42c | -4.42857 | -43.65953 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 984153a0-aea7-3000-87b6-87bc8ff2eb9d | -4.26796 | -46.84224 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5cdd5802-bec1-33e7-858c-1e9a157c360e | -5.03502 | -43.60895 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| be1ac1d7-edb7-3d75-9d8a-2f2853d6e8ba | -4.59244 | -44.3175 | 2025-11-15 03:34:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bbbf98e9-7ac1-3b21-bca3-20338a444d8d | -5.7364 | -35.30566 | 2025-11-15 03:34:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0fbaedda-1b89-3e1f-888c-d7ca8a1af3f4 | -4.81051 | -41.61378 | 2025-11-15 03:34:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 704ac3bd-2973-3ab8-be0c-d537da11d84e | -4.39524 | -44.07772 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 521eda1b-7da4-31ff-9e31-02f36df4d825 | -4.59162 | -44.32215 | 2025-11-15 03:34:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 89205e34-1d49-317e-8cf6-8bcc5e0a846e | -4.5421 | -43.21745 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 800c3f85-ddd5-358b-8ad5-5c024c85d2af | -4.59806 | -44.31834 | 2025-11-15 03:34:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73268f3c-f3e4-30eb-97ee-2047c2a2a46e | -4.54432 | -43.22625 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2e11b79c-2e74-3659-b9d0-4b8d3847d8d7 | -5.04046 | -43.60908 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 81a93638-98dc-348a-882c-b5ebcd0680b4 | -4.91978 | -44.78153 | 2025-11-15 03:34:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 825c04a0-a119-338b-90df-916280be4bd1 | -4.53997 | -43.21736 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b48344fc-1902-3d29-8731-6d0d68cfabc9 | -5.65804 | -35.44302 | 2025-11-15 03:34:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e261488f-31ea-3be7-bdd0-6e1999b43542 | -4.54063 | -43.21348 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dfa0154a-ecdf-3275-a036-d70eabb84cc4 | -4.81101 | -41.61082 | 2025-11-15 03:34:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f8f9d0a-7829-3cea-8b36-c5ce81bd0ae7 | -4.86124 | -43.25971 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e705d5f-418f-3644-9ad5-a2614bb0f673 | -4.47767 | -46.63005 | 2025-11-15 03:34:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df55beb9-0f7f-3e34-8a54-a059284c89e4 | -4.5343 | -43.21632 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7736f183-020c-38ee-b213-30c2fb00a42d | -4.86189 | -43.25586 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7f8ec8f1-e9b6-3479-b095-d7c026a799f1 | -5.51717 | -40.97376 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 88ea75c9-fd76-353b-9533-e5ca4953e8dd | -4.54498 | -43.22234 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c868c9de-a52f-3a31-9c0a-fadb4948a648 | -5.79736 | -35.56218 | 2025-11-15 03:34:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 70edc43d-f90f-332b-aee7-25f850368f95 | -3.66601 | -44.8157 | 2025-11-15 03:34:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8492b95d-b504-32fd-8687-31dde673fbac | -4.06625 | -46.42538 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 753aa088-96cb-353b-8af7-09ee211f3a92 | -3.21957 | -45.47813 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06549def-26c0-39c3-bf17-363ddf47ae51 | -3.22309 | -45.47939 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fd3a959c-b721-32b3-bfeb-fda396ad5584 | -4.54778 | -43.21846 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 76ca1729-28c4-3f2d-86ed-f903d9ac2d73 | -2.73395 | -45.30116 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fd3d586-a842-396f-beee-102fe6c5570f | -5.51534 | -40.98445 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3a50d36-8ee3-36a2-a3d5-aca709c2f85b | -3.37174 | -41.17424 | 2025-11-15 03:34:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d5e1153-965e-376b-b2d8-900ce226c547 | -4.27506 | -46.84356 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35754a61-07cf-3a1b-bd75-ae2ced5d966f | -5.47784 | -40.97196 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f71d24e7-294f-3607-989f-11068f97911f | -3.28503 | -45.46091 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3839634c-889e-352c-b88e-b53a74be885a | -5.47893 | -40.96886 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c6444874-e39c-313f-b7ea-42a614ba0caa | -4.54564 | -43.21843 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 054a798c-df09-3304-bbca-61b7256f8516 | -4.91442 | -44.7881 | 2025-11-15 03:34:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd4987a1-3946-35fa-8f92-f62f2c8f5444 | -3.99941 | -44.1692 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf8d633-3981-3174-bce3-d4aa5d9d88c8 | -5.47878 | -40.96655 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2b33f31-b342-3c40-8402-1a20cfa2fe59 | -2.73192 | -45.313 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65bae72c-d080-3d74-802c-5e6302c65005 | -3.21861 | -45.48391 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82948de5-5be3-3dce-94db-e0fed9ce5abb | -4.54279 | -43.21357 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f69d1008-b840-32e0-8d1b-fed1befac05a | -5.10035 | -37.78545 | 2025-11-15 03:34:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 4466dcab-d42e-32d2-aa37-d309f67698c8 | -4.85555 | -43.25883 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 902b61f2-0b92-348d-a80e-9176494fe942 | -4.54141 | -43.22133 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| bef850aa-6514-3206-bd61-4f3e85342591 | -4.4703 | -45.65168 | 2025-11-15 03:34:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ee72d68-9537-3396-9a91-1eed99c634f6 | -4.91891 | -44.78635 | 2025-11-15 03:34:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab1d6d1-d6be-3212-91b5-e5aa82128f6a | -4.40049 | -44.08311 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39666b69-9f8e-356a-b5b6-5e0acb1c2ee1 | -4.95083 | -37.39245 | 2025-11-15 03:34:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bcb1bfe-03a4-321d-a45a-e93539a68179 | -4.43443 | -43.66057 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0af96cd4-765a-3354-be42-3ab2b6568c2c | -5.03466 | -43.60812 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b65cbb01-1570-3030-96dc-368bd4b4a25f | -5.09644 | -37.78482 | 2025-11-15 03:34:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| f1bb8b8e-1b3f-3a3b-b0f1-5dec547fcdb2 | -4.81001 | -41.61677 | 2025-11-15 03:34:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fe5d09d-c3f4-3784-bbce-3a5b48be901f | -4.40128 | -44.07865 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 591744ea-64ff-31fa-8e0e-b49b2314c246 | -5.48377 | -40.96957 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2ad2ad17-90d2-3a6a-a43f-939f5512badb | -5.48726 | -36.74441 | 2025-11-15 03:34:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8caf99bf-20c1-38e8-b3c9-a328887fae7b | -4.0593 | -46.42413 | 2025-11-15 03:34:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0ac0bf7-934b-3d6a-81ff-eeabd81a5130 | -4.39445 | -44.08217 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed73abc4-be89-3350-8305-80655c152fec | -4.98092 | -43.88783 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e1b7457-438f-3403-b4ab-98904133d4e0 | -4.91163 | -44.04171 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c79dc362-40af-382e-b431-4d176770b1b8 | -3.99294 | -44.27916 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README13.md)
