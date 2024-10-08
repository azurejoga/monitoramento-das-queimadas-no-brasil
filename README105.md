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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 706caa65-6c2e-3593-ab68-8281f33682f5 | -16.70356 | -57.46613 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 228d46e4-4205-3d38-9cc9-e76e69d5877a | -16.7008 | -57.46187 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8de0d5d3-4f01-35c4-a93c-bc29788ec4cf | -16.7002 | -57.46555 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c40fd667-c805-357b-9d16-1fdd1e0c8a1a | -16.69804 | -57.4576 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d922ad0b-203d-33fd-8442-5c15db60b2ec | -16.69706 | -57.44231 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| da619300-6f33-3231-bfd1-beaf5dc4f7d4 | -16.69528 | -57.45334 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4e34eb5d-1938-34bd-88d8-fa636f1ec8a3 | -16.69468 | -57.45701 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 476cbb15-d3a6-38a1-8087-a795c65703d2 | -16.6937 | -57.44173 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 695c7dab-ce15-3c61-b3f3-55c0abb6af7f | -16.69311 | -57.4454 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7b2df9d3-1a2e-361a-a0b9-11686c8d7dd4 | -16.69192 | -57.45275 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d8b99d4e-fa8b-32c5-827b-eb2b859fe639 | -16.69133 | -57.45642 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 802d9c70-602c-3423-8612-54f22bfaeb2c | -16.69035 | -57.44115 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 39d8d0aa-4913-365e-b5d5-ff5137a424c3 | -16.68976 | -57.44481 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2783fd65-6d44-32d8-b4c4-d5e9dc0d66d8 | -16.68916 | -57.44849 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4dff0db8-88a6-3470-9907-6aba81803cc1 | -16.68857 | -57.45216 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3ec20229-2503-30cd-ae98-d56d629d348f | -16.68521 | -57.45158 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c6c6f1a6-0f6a-3d20-a3f6-c8df8294dffd | -16.93651 | -57.47935 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8db4142e-3623-3738-b62e-3440bc8afea3 | -16.93591 | -57.48302 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 27293faa-4d33-35ee-8e2e-768d72af55a9 | -16.93532 | -57.4867 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4507a635-fe02-3330-a01f-cee87edd442e | -16.93376 | -57.47509 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 62d00ff9-ba2d-31ba-b376-f65b25fdc0be | -16.93316 | -57.47876 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 72cf40b7-822a-3347-87cb-02bf81957e28 | -16.93256 | -57.48243 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| c7dd1b08-0042-3334-a3e5-091dc7e50004 | -16.93196 | -57.48611 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| e751285c-f06b-3555-88e4-f5758a4b2dd7 | -16.93136 | -57.48978 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a6d44040-d717-3e33-b972-e07492da82cc | -16.93041 | -57.4745 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 7cf90806-f621-3513-935e-6b7a7aaef7b2 | -16.92981 | -57.47817 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 51c2b0f7-0284-3c06-a308-de141a4fa2e2 | -16.92969 | -57.4713 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f266183b-4434-3eb3-8e9d-91519069bc7c | -16.92921 | -57.48185 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| c0cc904a-7a24-3f16-a0aa-438dffacf3eb | -16.92909 | -57.47498 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 1c68cb76-e2fa-3489-b93e-8decf36a595a | -16.92861 | -57.48552 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| b3099eeb-38c7-3bee-9b65-b6e6dc5e6a54 | -16.9285 | -57.47865 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| be4c1d09-00fd-336d-8b99-7e002f5b7292 | -16.92801 | -57.4892 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a3c9ee76-1c46-34e0-a452-396c655da273 | -16.92791 | -57.48233 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 6d670608-c2fa-3ba4-ada0-347330789d24 | -16.92741 | -57.49287 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ae0956ae-045d-34b1-991e-024e7c73dc94 | -16.92731 | -57.486 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| c2889f71-9e09-3d08-87c7-2b8e0286a84f | -16.92672 | -57.48967 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 669ab437-c878-35b0-b1d9-0d906680ed6d | -16.92574 | -57.47438 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a028459a-d102-3d3e-abb3-1f1f93aa9e66 | -16.92515 | -57.47806 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| deb84f37-9a57-3562-979b-621af940beb4 | -16.92455 | -57.48173 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 16e26029-246c-3bf7-a32d-ddcdaccd5a8c | -16.92396 | -57.48541 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.7 |
| e2d9adbe-bc4c-3df4-a23f-fadd1b698380 | -16.92337 | -57.48908 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c9ffc9f4-bdd7-3f07-907f-c544a7b6e2dc | -16.92179 | -57.47747 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| de524079-7125-37c4-ac92-8a7a7f42eedb | -16.9212 | -57.48114 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f2337afe-b18c-3f1b-a38c-6a9793b7f587 | -16.92061 | -57.48482 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b44f47c0-9341-3182-989e-4cf3b4386b3c | -16.92002 | -57.48849 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 904ab507-882a-33eb-b185-6cb30c2f73dc | -16.91785 | -57.48055 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 95419595-a51e-3c31-b5a2-72d042a26e5e | -16.88895 | -57.68044 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 26656998-b234-3154-ab69-85dc950eacab | -16.87212 | -57.67747 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 5a9a328e-cf10-3695-bb63-8dcc1283aeef | -16.86876 | -57.67688 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a6c7b11d-e151-328f-a602-d48b9c3c4587 | -16.83975 | -57.45177 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f0dab5b1-6063-3033-9aff-3aa66561b7f6 | -16.83699 | -57.44752 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0cbcb9ea-f171-36e0-a6e0-39e96275f642 | -16.83639 | -57.45119 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6e643510-fe54-333c-bfba-dba7aa69225c | -16.83484 | -57.43959 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a833c86c-2873-3eb5-9d92-d4b0aef8272a | -16.83424 | -57.44326 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fe48954a-6ee7-37c8-8998-ae211880aa84 | -16.83364 | -57.44693 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7a8eb8b0-cb82-38ff-9975-8a3241eb4048 | -16.83208 | -57.43535 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aefaf2ab-8438-3615-90df-5006b92c1c71 | -16.83148 | -57.43901 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c4c7d874-cfc2-35ce-bbe0-bc5b1ef00ca6 | -16.83088 | -57.44268 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 40ba9ae2-5d0a-301f-b81c-4da9f11489a4 | -16.82753 | -57.44209 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fd6bbd6a-9d0a-3a74-8f40-2184870530c6 | -16.82585 | -57.44224 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a837186-35da-38f3-bebb-c11bb6b8c11c | -16.82033 | -57.43372 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a1c4b479-8709-3547-b197-2560a71d3fd4 | -16.81974 | -57.4374 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9d1bdcf3-5ed9-3f63-aaa9-57eb04aef14d | -16.81915 | -57.44106 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4fa360ce-29bb-372a-9d75-99e5f8309dd1 | -16.81854 | -57.49719 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 957383e2-2b84-388b-bd30-ac5b5dd0ffb4 | -16.81755 | -57.49369 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e15170af-7bac-3e53-bf8a-5ffbc0818f08 | -16.81696 | -57.49737 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff2d8a89-5371-3d20-9794-2bb2abd35455 | -17.74143 | -57.09188 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d6651c6-38a2-3396-98ca-aee2beaabfb8 | -17.74085 | -57.09552 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9e3de75b-f974-3180-bf92-3138af0f92f9 | -17.74027 | -57.09916 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 52c65e4e-5afe-30bc-a379-b9831c8669e0 | -17.73809 | -57.0913 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8ecb6632-acdb-3640-b493-8536da1e228d | -17.73432 | -57.07197 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0d20a01a-4ecb-3740-9491-658c48ee72fb | -17.73418 | -57.09436 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dceaaad5-539e-3f8d-8f99-07481a3f9766 | -17.73157 | -57.06776 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 91f790e4-f703-3192-b7b4-5b3af0f4106d | -17.73099 | -57.07139 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2682a302-6938-38a3-8ca2-6293a73bf47a | -17.73085 | -57.09378 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5852db70-029c-31ef-8cb6-90eb8b3abec4 | -17.73041 | -57.07503 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9359a61d-0641-3715-ac41-da1e07a2f0b8 | -17.00228 | -56.6954 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d9f52334-0090-35c1-a63c-fee05fbeef42 | -17.00113 | -56.70263 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1273dc63-43c3-3355-87c4-32bf5ba18f5c | -16.99115 | -56.70092 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9b48bcd5-4d26-379d-8c64-9d8a677e268e | -16.98725 | -56.70397 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d8d67919-ea8d-336f-aa44-0e57386d16df | -16.98668 | -56.70758 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6dc0a35d-92bc-3719-838c-a0209f60c8a3 | -16.98449 | -56.69978 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 294e7923-8c6a-346b-bec8-4bfa7e1c9536 | -16.98392 | -56.7034 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 424f07ff-190d-3149-8129-6eb7957aa263 | -16.98335 | -56.70701 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| bae09de5-b5e3-343c-b286-95a7be1ad779 | -16.87312 | -56.71819 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 88ba06bd-11b6-393d-a98b-42c8e5852558 | -16.87254 | -56.72181 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d9ca11d1-05ce-314f-9eab-5247b6875df3 | -16.86979 | -56.71762 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 589b35ff-0f30-3340-ae04-da9e2cb7e747 | -16.86922 | -56.72123 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1d47cc8a-c2fc-30cc-bde9-f53256d309f4 | -16.8691 | -56.74349 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d77d1a4d-336c-3dff-a30d-dcd44a688d31 | -16.86703 | -56.71344 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e50f9c1d-d93b-3655-abaf-4a42da0ebaa3 | -16.86635 | -56.7393 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| df8795eb-976a-37f1-a842-d276ab5d63dc | -16.86588 | -56.72067 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eef61cbb-6439-3722-add9-6243cbeb88ed | -16.86577 | -56.74292 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db594206-cd5c-32ee-ac87-e0a9f77a8173 | -16.8637 | -56.71287 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0f1bddc6-6776-3129-9a92-34b1209300d7 | -16.86302 | -56.73873 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3913bc7c-803d-320e-9155-7c5b2da79993 | -16.86244 | -56.74235 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ce60a46a-afba-325d-af66-aa9408debba2 | -16.85912 | -56.74178 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3bd72d45-108b-3444-9ee3-a9c3f1870ffa | -16.85693 | -56.73398 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 658f1f27-bcd5-31a9-acf3-0bb760060062 | -16.85579 | -56.74121 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4b26e82a-cc03-3291-891d-fcdc9bda9a21 | -16.85521 | -56.74482 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README106.md)
