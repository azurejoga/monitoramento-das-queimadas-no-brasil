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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 380665d2-b7c0-31a6-914a-986a27df58db | -9.3045 | -45.4809 | 2026-06-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 49c43201-f8f7-3e65-804c-d6410df2522b | -7.1092 | -46.5065 | 2026-06-10 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 8cd6f358-50da-36b3-b549-bd5ba11bd350 | -9.3234 | -45.4787 | 2026-06-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| da45d690-a343-3a1a-a520-3fb0724d81da | -9.3045 | -45.4809 | 2026-06-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 31dc1a39-9704-3b9d-b894-f38214b9b14b | -9.3231 | -45.5015 | 2026-06-10 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 431f71c3-da68-3869-a127-501728c4923c | -7.0905 | -46.508 | 2026-06-10 00:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 48e25e7f-ce54-348a-aac3-37a83ebd9ab2 | -7.1092 | -46.5065 | 2026-06-10 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f9470a54-3b18-38e3-bbf3-9c50aa4d5271 | -9.3045 | -45.4809 | 2026-06-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| fc0dba01-8383-3138-892d-0244d98b8ea1 | -9.3048 | -45.4581 | 2026-06-10 00:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 248c3389-7ca1-3f40-ab4f-54f588d9b88c | -7.109 | -46.5287 | 2026-06-10 00:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1758c340-2c99-3dcf-a659-a91e3c926eb3 | -9.3234 | -45.4787 | 2026-06-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 715e70ac-effc-3b7c-89b3-a13367ce4901 | -9.3045 | -45.4809 | 2026-06-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c104b1f1-9bca-3d43-b3f1-d8cf9e17a48d | -9.3234 | -45.4787 | 2026-06-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3bae338e-afb1-3441-853f-39ba69cf9f6a | -7.1092 | -46.5065 | 2026-06-10 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| df2d2490-8c4e-33b1-9a82-403166e7e15d | -7.0905 | -46.508 | 2026-06-10 01:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 69046d73-1ca7-34da-9a84-b2993993c16b | -9.3045 | -45.4809 | 2026-06-10 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 995a2826-55d9-3eb9-b005-92af0cb662e1 | -9.3048 | -45.4581 | 2026-06-10 01:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| cc573ef2-a409-337a-beb3-28176bdebd91 | -7.1092 | -46.5065 | 2026-06-10 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 587238ce-c7ea-343a-8695-0465edeb71f6 | -9.3234 | -45.4787 | 2026-06-10 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 72ff2e81-ae2e-370d-8206-b110418c77e7 | -9.3045 | -45.4809 | 2026-06-10 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 255b6229-4d03-3ef2-b703-7571b12f406b | -9.3234 | -45.4787 | 2026-06-10 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| d6fe2380-68c7-326f-b070-28ce7f796991 | -9.3048 | -45.4581 | 2026-06-10 01:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 72a17e88-08f2-36ad-b4ff-c6083a063950 | -7.1092 | -46.5065 | 2026-06-10 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 906d6af9-6721-35a4-99ca-afdf19ecd81f | -9.3045 | -45.4809 | 2026-06-10 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 49c91454-14b8-35c2-bbfa-861a3d913674 | -7.1092 | -46.5065 | 2026-06-10 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0825db0e-2233-3021-8c40-df8afb3d6a13 | -9.3048 | -45.4581 | 2026-06-10 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f214fced-7789-37b9-a78c-ff3284e293c6 | -9.3234 | -45.4787 | 2026-06-10 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d11802b3-da8b-344c-b3bb-597a5836c57b | -9.3048 | -45.4581 | 2026-06-10 01:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4a951270-52ff-3a38-88c6-5de0b84c394f | -9.3234 | -45.4787 | 2026-06-10 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| bd93f6ef-3cf1-3583-a44b-67cdfcec62c7 | -7.1092 | -46.5065 | 2026-06-10 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0539457a-cd3f-3724-aab1-417e7e78265d | -9.3045 | -45.4809 | 2026-06-10 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d73d6c3c-b3ca-3a99-a282-7f3f1d92edbb | -7.1092 | -46.5065 | 2026-06-10 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6a2b6dad-f4ba-3b1b-a28b-1e172ab4a517 | -7.1092 | -46.5065 | 2026-06-10 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 577027d7-5774-3b9f-8a82-a931c6dfcf4e | -9.3045 | -45.4809 | 2026-06-10 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3e5a387a-7f87-3b76-942b-6e0c246dee49 | -9.3234 | -45.4787 | 2026-06-10 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4b2b5f06-25bc-3951-9f35-4acf3e57e712 | -9.3048 | -45.4581 | 2026-06-10 02:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| cca149df-27fc-3759-8d32-d349d6764917 | -9.3045 | -45.4809 | 2026-06-10 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e56ef88c-115d-34a9-8165-dc0c5f260d28 | -9.3234 | -45.4787 | 2026-06-10 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5229f253-0c91-32d6-bd8c-15ffcf3f7855 | -9.3048 | -45.4581 | 2026-06-10 02:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ad2a99ae-9125-3bec-aa7b-5ba19b6f40e7 | -7.1092 | -46.5065 | 2026-06-10 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5478ed18-8095-3c0d-841b-f068e8b1bae6 | -9.3234 | -45.4787 | 2026-06-10 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 055a1e0e-a1f8-3015-8bb8-d8254c088af3 | -12.8548 | -44.3625 | 2026-06-10 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| fbc1f717-8edd-30f2-ac79-b5e7a4f4524c | -9.3045 | -45.4809 | 2026-06-10 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d6cc58c6-ec93-3d50-ae77-efe5cb477116 | -9.3048 | -45.4581 | 2026-06-10 02:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d75a3ee4-7405-3cbf-98fb-7e1509ef04aa | -9.3045 | -45.4809 | 2026-06-10 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| faef0359-dc76-316f-ba5f-b48d87a184b5 | -7.1092 | -46.5065 | 2026-06-10 02:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f21895c8-8b84-3ab9-98dc-fdb971215a3d | -9.3045 | -45.4809 | 2026-06-10 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 34484cda-6f7b-35c8-8160-acd80c0f71b2 | -9.3045 | -45.4809 | 2026-06-10 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 424137df-238f-3ca0-b50f-346d617281c0 | -7.1092 | -46.5065 | 2026-06-10 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 95440a1d-5513-3d18-b2d9-2e14c0b7c46f | -9.3045 | -45.4809 | 2026-06-10 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c023e88a-f72f-3666-a152-d6c8dd3ffe02 | -12.8548 | -44.3625 | 2026-06-10 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| ba42cf8c-c3d2-3c02-b3e3-0322277572e0 | -9.3045 | -45.4809 | 2026-06-10 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| cc1075c4-450c-3799-b7d6-b50d71311151 | -9.3048 | -45.4581 | 2026-06-10 03:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6ac0b824-2189-3972-b0a7-442b21e751ba | -9.3045 | -45.4809 | 2026-06-10 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 498d5e36-7dba-3a6d-bd78-6d513af184b2 | -9.3048 | -45.4581 | 2026-06-10 03:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 620d52c1-08ec-3e61-85b4-5fa0677f779a | -9.3045 | -45.4809 | 2026-06-10 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ad45cd73-dd51-3332-b370-5008ec83bced | -9.3048 | -45.4581 | 2026-06-10 03:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| bf6140aa-5b12-38fc-a93c-6781fde5f550 | -9.3234 | -45.4787 | 2026-06-10 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 07022bb7-aa3f-393b-959a-cce84a553135 | -9.3045 | -45.4809 | 2026-06-10 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 1b0c0504-2a8f-3cb8-8fcd-c2568aa188df | -9.3048 | -45.4581 | 2026-06-10 03:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4dfe40fb-378c-3922-bf10-a3eb0b5d7de8 | -9.3234 | -45.4787 | 2026-06-10 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8082c07a-6907-3338-b557-7c9f43b3675e | -9.3045 | -45.4809 | 2026-06-10 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| aaa2560a-7fb0-3f33-8408-ecde98d808a8 | -5.04346 | -43.26357 | 2026-06-10 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 416fa0e8-3bdc-3b92-9a6d-7e733a623d23 | -3.50491 | -48.03348 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c387ced-35e5-376b-b8d0-9d15f95aa1f6 | -3.80603 | -49.18105 | 2026-06-10 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb1a136c-22f4-3327-8e32-e448d72dd215 | -4.95617 | -37.5375 | 2026-06-10 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0520db6-929b-30a3-a81e-3bfafd93a02e | -3.4984 | -48.03676 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d310255a-8c61-35b2-838a-fcf7249b281d | -3.50392 | -48.04031 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0d9846d4-6697-3b50-ae67-7b88f3e2184d | -4.42993 | -47.73351 | 2026-06-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a54b848-be7c-3025-980c-c9834b761283 | -4.95947 | -37.53801 | 2026-06-10 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a431739b-78fc-384d-82a4-3fb898f752d7 | -3.50425 | -48.03751 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 41eeca40-7d09-3dc3-aae7-7eda1cd1ff18 | -3.49768 | -48.04117 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b270e119-c49c-3e26-b85a-19a0773f8e85 | -3.49253 | -48.03618 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f233b1-98e7-36e9-a6ff-b4e8b6fd2f81 | -3.50467 | -48.03597 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa4dcb78-f765-33af-9472-71af68002e57 | -5.49541 | -37.24293 | 2026-06-10 03:53:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 465f176b-052c-3b4c-b60b-f8d0b09df1f6 | -3.50535 | -48.03201 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8ef95b09-efb1-312b-ba0b-ba431d614540 | -3.49809 | -48.0395 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 156522b4-e570-356e-b5d9-a27b249fb71b | -4.43056 | -47.72987 | 2026-06-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058c112d-a9a4-3fc1-90cc-7ed5b750fddd | -5.52231 | -37.48503 | 2026-06-10 03:53:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0747796b-d12f-3df9-81ae-0c603cc97924 | -3.80521 | -49.18587 | 2026-06-10 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee0a8f2b-4603-35e3-87c1-ce7934e51140 | -3.51075 | -48.03421 | 2026-06-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e144190-dc9a-383e-b9e2-dfb942011534 | -9.7484 | -47.88039 | 2026-06-10 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ece368a2-8a62-3c62-aca2-c22620c914fb | -7.10248 | -46.51517 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a2c61da-5963-35b4-ab65-abea1c0a27f4 | -6.01226 | -47.0782 | 2026-06-10 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35a6ab37-9783-38bb-832c-753ae41e1dcb | -9.7744 | -49.74678 | 2026-06-10 03:55:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de14593a-e377-364a-8c2e-8c094704e5f3 | -7.99017 | -46.04934 | 2026-06-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a573730-7ec4-34a7-b5db-cbf0a8bc9d9d | -9.31516 | -45.48869 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73216aa4-479d-31ee-bdc9-7ca88f2a14fe | -7.7167 | -44.56923 | 2026-06-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21598d20-8931-3534-9338-ba839a74fb1d | -5.82934 | -43.59069 | 2026-06-10 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0eef31be-fc29-3725-b5fa-74b89d0d1515 | -5.805 | -43.79065 | 2026-06-10 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48997306-58f5-30ba-9515-b61a88318a2d | -12.02957 | -47.8068 | 2026-06-10 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e26ffbd6-7334-3af6-95ff-94cef3796b75 | -7.15846 | -44.06574 | 2026-06-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46f2382e-04a8-36e2-851d-0a0dd9d8f582 | -9.30417 | -45.47299 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c58473ff-1b44-3a2e-acda-be5e684d4d24 | -6.19507 | -45.16467 | 2026-06-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2becc47f-3ade-3b17-80df-7b765b0b9afb | -7.09845 | -46.51637 | 2026-06-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb076ce3-5f53-3107-8c46-928f638ab330 | -10.77544 | -44.84918 | 2026-06-10 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6dc3665b-bd34-388e-bc8b-825ab0f61716 | -9.77514 | -49.74788 | 2026-06-10 03:55:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6490f94d-20bd-3f21-80a4-16085f7ea908 | -9.31592 | -45.48427 | 2026-06-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b62964db-411c-3206-a924-dcaa659256b9 | -8.49986 | -47.0193 | 2026-06-10 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e4be568-12dd-3be1-8cca-fd8fb975b521 | -11.16502 | -44.68481 | 2026-06-10 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
