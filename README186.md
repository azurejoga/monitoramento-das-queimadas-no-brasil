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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf247524-b694-3f21-836e-fcfb6b0470b6 | -3.46657 | -64.9592 | 2024-10-25 16:54:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d9422eca-56db-3450-9332-a563bbde82df | -3.45326 | -64.96793 | 2024-10-25 16:54:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 13224d38-3ffd-35c5-b587-f2cd84c6d708 | -2.42382 | -65.05849 | 2024-10-25 16:54:00 | NOAA-21 | MARAÃ | AMAZONAS | Brasil | 1302801 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e154a328-1009-36cc-9d0d-1daec279788d | -1.50822 | -46.5512 | 2024-10-25 16:54:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 606527ff-5319-3f58-85aa-f78d13ab49de | -1.50418 | -46.55183 | 2024-10-25 16:54:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d9bc3a55-134f-3024-913d-a9841307869b | -1.46061 | -47.06178 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e573fa7b-fc4f-3636-8c39-907e87c5da6a | -1.46055 | -47.06458 | 2024-10-25 16:54:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 78895eab-7274-3111-a77b-564c1e64dc19 | -1.34611 | -46.74283 | 2024-10-25 16:54:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a6cfcd14-c8b8-369a-9322-19448d5d1356 | -1.07989 | -47.01849 | 2024-10-25 16:54:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e01c5bc6-eabf-39a4-be14-5208110feae3 | -0.964 | -46.97086 | 2024-10-25 16:54:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b9a4ae8d-1dc4-3326-9c1b-c8767a5e7a6e | -0.90496 | -46.8796 | 2024-10-25 16:54:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 113dee82-762b-3648-b3ed-177607829538 | 2.32538 | -59.82718 | 2024-10-25 16:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ff183827-a0b1-3285-b6ff-12912817b0e9 | 0.59499 | -59.22444 | 2024-10-25 16:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9afeb24e-84c8-31a4-8ae8-89612a1c0514 | -1.89231 | -60.00477 | 2024-10-25 16:54:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69d849a4-e16c-3989-a571-571884e4add7 | -1.65179 | -59.97674 | 2024-10-25 16:54:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 44f62c45-286d-3090-a6a8-016fa800c1bc | -1.19252 | -60.31903 | 2024-10-25 16:54:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e9b96c9b-f9b7-345c-a5c3-d55d03a82b85 | -3.519 | -60.3843 | 2024-10-25 16:54:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 40784bdf-a37a-3483-b1d5-4d33e36f806d | -3.46131 | -60.38725 | 2024-10-25 16:54:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0d935de1-280b-3458-94a4-47c148a8b4c4 | -3.46081 | -60.38389 | 2024-10-25 16:54:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 05bea3a0-2138-37c5-aa3b-2cd7033efc4d | -3.41046 | -60.37698 | 2024-10-25 16:54:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e3906cfb-5a78-3cb8-9470-0912a8e9fb4c | -3.40731 | -60.20767 | 2024-10-25 16:54:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| f1ea53f5-f51d-3738-981a-57c7d54f6949 | -3.36278 | -60.74492 | 2024-10-25 16:54:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 90260e3b-bef2-3414-9edd-f372fecd2766 | -3.35727 | -60.74563 | 2024-10-25 16:54:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 14302836-86b0-3ae2-8070-135b52468fed | -3.32938 | -61.24778 | 2024-10-25 16:54:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9ae89098-7aea-3c6a-b0ca-2259dccca5b4 | -3.27102 | -60.96643 | 2024-10-25 16:54:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7c812e33-877c-377c-80ff-dfd84502cccb | -3.26694 | -60.89967 | 2024-10-25 16:54:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af4bfa20-0a5b-35f4-9936-67074af7837f | -3.21304 | -59.98807 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d92c01-2618-3ee2-a19e-a4236e476414 | -3.12854 | -60.87844 | 2024-10-25 16:54:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a6337457-93b8-34c6-a959-64a511125f64 | -2.93363 | -60.16467 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8d5036d5-9d58-3e7a-80b6-07bb14556627 | -2.64294 | -59.91611 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a724dd37-4efe-3eae-baa5-3dc1f80b0a7d | -2.52865 | -60.75735 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db722dd6-eb9a-385e-9608-f4f12346ad7d | -3.52839 | -62.35313 | 2024-10-25 16:54:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6bf1ea25-c0ee-3d44-9611-4b3a6684675d | -3.29137 | -62.95429 | 2024-10-25 16:54:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 6de3924d-8571-3066-a0bc-dae8d20e79a8 | -3.29062 | -62.94926 | 2024-10-25 16:54:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 1de3fbb5-6396-37a1-8904-7bb27f33b0f2 | -3.27264 | -61.50949 | 2024-10-25 16:54:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 49af179d-0942-31ba-a15f-6367da47267e | -3.72455 | -62.00965 | 2024-10-25 16:54:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a510280-41f7-3413-b4a3-b3bdd0c3c4b8 | -3.95943 | -63.20006 | 2024-10-25 16:54:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8400cb89-ca2a-31e1-9fc5-190bfd18e18c | -3.95864 | -63.19464 | 2024-10-25 16:54:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 4c1d2721-38fa-3b01-b026-87f4a8be22a2 | -3.95296 | -63.20108 | 2024-10-25 16:54:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bf360d6f-3a45-31fc-a0de-d69ff6ad104e | -3.90231 | -63.72762 | 2024-10-25 16:54:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6bee72aa-e531-3733-ba3a-3968a48425b8 | -3.90148 | -63.72179 | 2024-10-25 16:54:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 723e36d5-3228-3924-9d0c-853f5343e0a9 | -3.84477 | -64.16219 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 82a6b4bc-47cc-3377-a618-5a26a9a4df72 | -3.83278 | -64.17624 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1c031798-a46e-39e9-9534-c4fd00c08971 | -3.83232 | -64.17991 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 58de08d1-f941-3f66-98ed-534bc2b28d0e | -3.83142 | -64.17385 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9a67d70c-409d-3002-be70-4dd290cadeee | -3.7 | -64.18396 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c8da3588-e93f-3bb1-9f7a-c7460aa1bd39 | -3.69943 | -64.18655 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 49f7e566-8a9f-326f-b62d-bf516c734baa | -3.69851 | -64.18027 | 2024-10-25 16:54:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ae9314dc-130d-3cfe-a1e1-6704946d0a75 | 1.58101 | -55.65479 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d85e2b20-4b92-3535-9daf-950bf745219c | 1.57804 | -55.65002 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 94572e1e-30ee-3d0c-9bfa-03f3a106095d | 1.57441 | -55.64947 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4645bf7c-819d-3f2f-acc9-8c024c4125fb | 1.57411 | -55.64643 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c85536d-8d7f-3d84-a841-74b43bb407f8 | 1.57346 | -55.65064 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6955a831-14a2-30e6-a018-8c7e0451a5d9 | 1.57047 | -55.64588 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e22d171-c893-36ff-9cee-94e7302dd97f | 1.56983 | -55.65009 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a685c3f0-0932-3227-a9f8-992aa8bdd831 | 1.5678 | -55.64415 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5d48b3cc-8046-38d0-9190-8b09a5d36e09 | 1.56713 | -55.64836 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bf403317-6c67-34c7-9fa0-df22e3ec86d9 | 1.55955 | -55.64422 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c868a3df-b56a-3b35-9d19-2dfa1dc6508f | 1.55891 | -55.64844 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1afe62fa-4e75-3917-a358-7726ec713fdd | 1.55826 | -55.65265 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e911eea1-5aa8-3d27-b8ab-cac7b973b6bf | 1.55526 | -55.6479 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 587dc5a6-55cf-36b4-8b03-712c76ce4ed9 | 1.55462 | -55.65211 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bb4cae32-fa55-3842-94ff-deab34a78aaa | 1.55098 | -55.65157 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fcf3884a-cd7c-3fdc-8f94-15c6a141daf0 | 0.86924 | -54.64645 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 1255f402-cd11-3737-9a8d-14081da7685d | 0.85756 | -54.65259 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 880809ad-0f20-34a9-aa44-fc44cd215ffb | 0.85605 | -54.65224 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b0b2af70-560d-3219-9fa6-02c589e3df26 | -1.20638 | -55.73103 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d98b7861-f090-339b-8a3c-9faee0b5fa6c | -1.20258 | -55.73156 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b492b9c2-f601-388f-b19b-343998d1eaa8 | -1.20187 | -56.0649 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1279cf8e-30b6-3bb2-8598-96ce9948d858 | -1.20003 | -56.06332 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 089327cb-ad06-342a-9b11-282886014243 | -1.19305 | -56.06934 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d1d9d3cd-32d0-3a7c-a22b-79e0ce3e6ea0 | -1.19228 | -56.0644 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6fa79a81-0315-3acd-b2d9-2a38e16eb46e | -1.18191 | -55.84687 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| f29ea8fd-425e-37da-aea3-9b4b665542bd | -1.17885 | -55.85222 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 9c5e993a-cb48-3529-a1fb-010f2d42ffe7 | -1.17811 | -55.84752 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 9d5dd52b-4f0f-39e5-a878-571a37a7f6bb | -1.17754 | -55.84917 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 356.5 |
| 082a23e6-0b4b-334b-899d-32282704c711 | -1.08817 | -56.04264 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d1ce12a8-6c97-3451-bda5-2dcc6dbe9e9f | -1.60285 | -55.40826 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5a8fe84-8d60-3a00-83a2-962caa9314aa | -1.52885 | -55.40885 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e3aa1baa-a974-3458-9f71-41c9f36b5dbe | -1.52817 | -55.4044 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bf6e2533-60b4-3ed4-9ce1-659080784972 | -1.5257 | -55.36386 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a1d0f5de-69a8-3dad-af4b-b266b520d6f9 | -1.52512 | -55.40943 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 50d30bec-9a76-3360-90c9-59d0c8c50d91 | -1.52443 | -55.40496 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bfed7767-a8ca-3b0a-a34d-30a6ab7df80c | -1.52266 | -55.36883 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 101b1107-47ad-36ed-917a-71e520bf909f | -1.48171 | -55.12859 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 56a68507-dd72-3fb0-b5a3-b66d3dea7387 | -1.47589 | -55.41218 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7c1b2b3f-9659-348e-b4a4-07f825c02923 | -1.47491 | -55.3306 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ebd7da79-6a84-35d0-bec9-34d1b16e775e | -1.44068 | -55.38103 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4e37813f-8d6d-3c01-b66d-87a9ef6c3a6c | -1.42748 | -55.50554 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85eb10da-7c9f-3c7d-9966-6f3ae35b42ab | -1.42189 | -55.23051 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1651dd4f-0482-3842-becb-fd3672d8233d | -1.42153 | -55.31963 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 48b22069-494a-3442-8c7e-06a8d748ac80 | -1.42024 | -55.32066 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d4357d86-672a-3620-9deb-867dad24498d | -1.3875 | -55.41978 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 605faeb1-2864-3178-a961-b194ff7b677d | -1.38477 | -55.40189 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 552ddc92-f7f1-3977-905d-555f2b23e90c | -1.35281 | -55.49356 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 31a9844d-0f3d-3e73-ae4c-4140fa461281 | -1.35213 | -55.48906 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 54756081-e670-3f07-8267-7c9509f8dc8a | -1.34906 | -55.49411 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 275ec267-5b26-3aed-9032-d2a1e7f1011f | -1.34838 | -55.48959 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 093e073a-f1a5-3d52-a2c9-1fca0fbb0ef7 | -1.34648 | -55.37545 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ad95ebf-2bee-3206-931f-19962eb17473 | -1.34567 | -55.47151 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README187.md)
