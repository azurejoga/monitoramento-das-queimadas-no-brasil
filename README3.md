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
| 91473de6-1c15-3b37-add1-8f8f08081b7b | 2.7816 | -60.3338 | 2026-03-05 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 264.8 |
| faac4846-d408-311a-8130-2f92247df9c9 | 1.5047 | -59.9116 | 2026-03-05 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a75d53f1-97b3-3f74-b072-be8b8ac9bfac | 2.7999 | -60.3335 | 2026-03-05 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a28ae43d-33c8-3633-8e2c-9453fbf24540 | 2.7633 | -60.334 | 2026-03-05 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 178afa59-1875-3273-96ff-e2064b1e4d6f | 0.0273 | -60.9799 | 2026-03-05 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e5cee6d6-c7d1-3840-b27b-6260e404ad8c | 4.5181 | -60.5842 | 2026-03-05 01:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9d4b92ae-554e-3e7b-8740-d4d3538dc593 | 0.0455 | -60.9799 | 2026-03-05 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 8a78180c-616c-342d-92d1-6bbda73e7033 | 4.5181 | -60.5652 | 2026-03-05 01:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e5c2b92f-e38d-30d1-bde4-25035cd3cc5f | 4.959 | -60.268 | 2026-03-05 01:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 75937a1a-c287-397f-af90-41d537bd0eb4 | 3.2738 | -60.7432 | 2026-03-05 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 5dc60e04-458d-321f-a15a-68d47f8998f5 | 0.0455 | -60.9988 | 2026-03-05 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 31fadc8e-20ca-3f19-9878-6ad05751e94a | 2.7816 | -60.3528 | 2026-03-05 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 163.5 |
| dbc8890f-8b8e-3750-b368-fa154f4c556b | 2.7998 | -60.3525 | 2026-03-05 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| de76a22e-1b9c-3f35-8b53-96d4bb45bcf2 | 2.7633 | -60.3531 | 2026-03-05 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 21f3192e-9abf-32cd-8830-a3ba38d38f87 | 2.7816 | -60.3338 | 2026-03-05 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 275.7 |
| 72fdb266-764a-35f7-970b-f291c3bffdbf | 1.5047 | -59.9116 | 2026-03-05 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5d587ec3-5c13-3ba9-a87e-4fe469312654 | 2.7998 | -60.3525 | 2026-03-05 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f281d6df-0265-37eb-8f48-acf26b5a08ab | 2.7999 | -60.3335 | 2026-03-05 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 8dd5ebe7-4d86-349a-b343-efb60cb9fef7 | 3.2738 | -60.7432 | 2026-03-05 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 00a3a2c1-1843-3f72-bc4f-629f72c7759a | 0.0273 | -60.9799 | 2026-03-05 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4ea8bfb6-c394-32fc-b46b-6525cf8689b7 | 4.5181 | -60.5842 | 2026-03-05 01:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 6ebacd8f-3e07-37ac-99c2-4ee8989e122b | 2.7816 | -60.3528 | 2026-03-05 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 73b4c1c8-6cd2-3863-a924-c39eb2042a7c | 4.9407 | -60.2685 | 2026-03-05 01:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 708609d1-a99b-3b1d-a7d5-40c87679ecaf | 4.959 | -60.268 | 2026-03-05 01:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 309512cf-e7cf-37b2-af40-d67dd204f3ae | 0.0455 | -60.9799 | 2026-03-05 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4794d3d4-7647-3be8-8c7b-e361298ec0ce | 0.6654 | -60.297 | 2026-03-05 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e64f0c59-6a24-3171-8f31-e7bdcc19130b | 4.5181 | -60.5842 | 2026-03-05 01:40:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 42.0 |
| f4670e64-4ef5-3d4a-8e52-61080ca95426 | 1.5047 | -59.9116 | 2026-03-05 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4ee11efb-4310-304b-8030-e8b1708c48b6 | 4.959 | -60.268 | 2026-03-05 01:40:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| e287344a-e46d-3c66-a668-f9f127618240 | 2.7816 | -60.3528 | 2026-03-05 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 148.0 |
| e5725628-1c25-3437-b03b-335cf3c216bf | 2.7633 | -60.334 | 2026-03-05 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d090ad75-083f-3ac1-96ea-b3e5a5572c7d | 2.7999 | -60.3335 | 2026-03-05 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d0daaec6-cfb0-375a-8e40-fb127aaaae8c | 0.0455 | -60.9799 | 2026-03-05 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 45e3ca0b-b6de-330c-9a21-6e54be2daaf0 | 2.7817 | -60.3148 | 2026-03-05 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ec3feac1-2688-35eb-b2f4-7e38ac362ab1 | 2.7816 | -60.3338 | 2026-03-05 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 255.0 |
| 6232e379-f146-3c77-bfe4-6dfd6a170d07 | 2.7816 | -60.3338 | 2026-03-05 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 243.9 |
| f30a2b7c-ce58-39ec-89d0-2af304185d33 | 2.7816 | -60.3528 | 2026-03-05 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 4463dc84-c26e-3054-95b8-4259c69e9579 | 4.959 | -60.268 | 2026-03-05 01:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 36.3 |
| e0ad5ff9-6cb2-3cf2-92e5-d6a44b349ab5 | 0.0455 | -60.9799 | 2026-03-05 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 59291639-8ca3-3638-a414-dd1251826a8f | 4.5181 | -60.5842 | 2026-03-05 01:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a3df4868-ee09-3fae-b723-fea929d7a991 | 2.7633 | -60.334 | 2026-03-05 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 86127e75-9687-3b5c-90df-10c565424798 | 1.5047 | -59.9116 | 2026-03-05 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b14f5d29-fb54-353a-893b-7498e39a0023 | 3.2738 | -60.7432 | 2026-03-05 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 66b6aa43-2f97-3290-825d-65ce43fdef1d | 4.5181 | -60.5652 | 2026-03-05 02:00:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 16b2d7fa-319a-3ecf-bea7-ecd3ec762c38 | 4.5181 | -60.5842 | 2026-03-05 02:00:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b66ca83f-c079-365b-8260-036a5ee50e36 | 0.0273 | -60.9799 | 2026-03-05 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 03ded1d6-505e-328e-8206-93eef5c62b0b | 1.5047 | -59.9116 | 2026-03-05 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b8b9b1ee-aa29-3b80-a671-1c3051619e7d | 2.7816 | -60.3338 | 2026-03-05 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 237.6 |
| 20c0ecd1-63f3-30f6-86c0-55e3135ab18d | 2.7999 | -60.3335 | 2026-03-05 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2726ebac-f41e-3cdf-aa1c-df8bcb4942a3 | 2.7816 | -60.3528 | 2026-03-05 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 1d87811a-07d8-32b0-bb99-7f024ba4f2ce | 0.0455 | -60.9799 | 2026-03-05 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 385ff339-d669-3c1c-9c23-140e89938ada | 2.7816 | -60.3528 | 2026-03-05 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 239ff992-6981-3937-8015-fae1f83d03e4 | 0.0455 | -60.9799 | 2026-03-05 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| e95d6c8d-3fe5-3d18-b39f-9fa1d561f679 | 2.7816 | -60.3338 | 2026-03-05 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 7362f8df-9705-32c4-b2cf-30780cd97235 | 3.2738 | -60.7432 | 2026-03-05 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e56fe3fa-ac7c-3311-9726-665bd7ce120d | 2.7817 | -60.3148 | 2026-03-05 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7042d687-bb97-3fca-821c-1f9eaa14322e | 0.0273 | -60.9799 | 2026-03-05 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2adce171-5ccf-388f-bcd8-fa795d2d6f07 | 0.0455 | -60.9988 | 2026-03-05 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ef048089-e3b8-3949-ba45-b7ebfd764062 | 2.7816 | -60.3528 | 2026-03-05 02:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 41bba03e-a34e-3828-a040-11805e2a4a53 | 0.0455 | -60.9799 | 2026-03-05 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5d60e5f7-8daa-3526-9297-696eef2bbbba | 0.0455 | -60.9988 | 2026-03-05 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 593abf31-a88a-34c5-8b5f-26227733f498 | 2.7816 | -60.3338 | 2026-03-05 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 22123a90-5c11-3588-bb01-3b235ea1f4d3 | 3.2738 | -60.7432 | 2026-03-05 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6d8a0363-3569-3dea-9505-4345a5a11895 | 2.7816 | -60.3338 | 2026-03-05 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 6b624b3a-8972-3532-9ba7-11d5c016ef22 | 4.5181 | -60.5842 | 2026-03-05 02:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2d53f543-cdbc-3b23-a913-b2b92758cca2 | 2.7816 | -60.3528 | 2026-03-05 02:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d1b40957-2974-3873-b63e-7cbf6c3dd3ea | 2.7817 | -60.3148 | 2026-03-05 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 83a20631-2553-3e16-bf3e-ef10789ccfb4 | 3.2738 | -60.7432 | 2026-03-05 02:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c3e74a0d-e0cd-30df-8316-ff7de87089a5 | 0.0455 | -60.9799 | 2026-03-05 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fe0638f5-3f77-33ec-b097-1b0bb2fb40f8 | 2.7999 | -60.3335 | 2026-03-05 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 55c4a391-0131-3f06-9e54-c6ecd52eea28 | 4.5181 | -60.5652 | 2026-03-05 02:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1fa424b3-86a5-3ea8-aeb6-93c087271ceb | 2.7816 | -60.3338 | 2026-03-05 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 247.1 |
| 97602b9e-225c-3ebf-81c6-f0591d4696b6 | 2.7999 | -60.3335 | 2026-03-05 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ae8862ea-d694-3eab-bc83-5d727070a90b | 0.0455 | -60.9799 | 2026-03-05 02:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 68c12fe2-7de7-3c7f-8df0-112187e849ac | 2.7816 | -60.3528 | 2026-03-05 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 9258e4cd-9b13-3e78-a4c6-da8e67db45ee | 2.7998 | -60.3525 | 2026-03-05 02:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5e1ef4c0-fc05-3af3-8ad4-625f9bd993b2 | 2.7998 | -60.3525 | 2026-03-05 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 270b89a5-b69f-397e-afdb-750046eaeb40 | 2.7816 | -60.3528 | 2026-03-05 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 171.4 |
| af0faa5b-5393-312b-ba68-3de8a6a327d6 | 0.0455 | -60.9799 | 2026-03-05 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 274bb229-4124-3ca4-a1f7-047e1d29e8b4 | 2.7816 | -60.3338 | 2026-03-05 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 227.9 |
| caf3c7db-6b23-3153-997e-ce52106c0561 | 2.7999 | -60.3335 | 2026-03-05 02:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8533c575-fefb-39fc-b9e0-e5037fae124f | 0.0455 | -60.9799 | 2026-03-05 03:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fdf7efe6-d166-33cc-8071-90c21022d308 | 2.7816 | -60.3338 | 2026-03-05 03:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 1760eebc-d665-3c30-8a80-9fbbe7ab1722 | 0.0455 | -60.9988 | 2026-03-05 03:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c6044667-2c80-32b8-aa94-3c8a9951f1f5 | 2.7816 | -60.3528 | 2026-03-05 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 0a800d7f-bd6c-3381-8895-61c13213b8df | -8.87357 | -35.19358 | 2026-03-05 03:04:00 | NPP-375D | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 19fd803e-06ae-354c-9a5c-703b02d3708d | 2.7816 | -60.3338 | 2026-03-05 03:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 182.3 |
| d003cabd-11dd-376e-bbe2-794d481bc458 | 0.0455 | -60.9988 | 2026-03-05 03:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 820b9f09-68db-3e4c-ac61-e87ee81d849e | 2.7816 | -60.3528 | 2026-03-05 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 1a75c7a6-607e-36c4-a321-d54361d4e8ef | -10.178 | -36.4313 | 2026-03-05 03:10:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 104.1 |
| 466167e4-d457-365a-8148-2160d61a5f89 | -10.1974 | -36.4278 | 2026-03-05 03:10:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 32543835-183b-3556-b554-c9b9f3807651 | 0.0455 | -60.9799 | 2026-03-05 03:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1949c207-ef81-30db-bcb5-f041e3772962 | 0.0273 | -60.9799 | 2026-03-05 03:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 7eec6462-eabb-3a9e-b224-5da1d094b917 | 0.0455 | -60.9988 | 2026-03-05 03:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| cdf510a3-109d-354e-9e39-429f3b2349df | 2.7816 | -60.3528 | 2026-03-05 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 9f8bf7bf-d216-39c1-9c09-7c5345343fd6 | 0.0455 | -60.9799 | 2026-03-05 03:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c0ea3b74-7664-38f3-a80e-86f42b09a715 | 0.0273 | -60.9988 | 2026-03-05 03:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 0fa15fc0-c376-39b3-ab43-0a8737f19407 | 2.7816 | -60.3338 | 2026-03-05 03:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 1b3a0da3-20b6-3789-a4cb-3ed3d8993170 | -3.51768 | -41.95852 | 2026-03-05 03:23:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c8b4e12d-0133-35d9-af3c-bc8132b39532 | -11.11866 | -38.60683 | 2026-03-05 03:25:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)
