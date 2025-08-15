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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cf186e3-188b-3645-b20a-1b472d4236c2 | -29.80424 | -52.12545 | 2025-08-15 04:57:00 | NOAA-20 | VALE VERDE | RIO GRANDE DO SUL | Brasil | 4322525 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 335a56ef-4d1a-3cae-b740-4db8e68a0c0d | -9.1706 | -59.6762 | 2025-08-15 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cd9666d6-fb38-3580-a60e-975423ce7ce9 | -9.1894 | -59.6558 | 2025-08-15 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 84e3b880-8b3a-3bca-8c39-826e1d29ddc7 | -11.3468 | -55.4124 | 2025-08-15 05:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 71166194-dc5b-332e-a4a2-d416f6e9ee27 | -6.9303 | -59.5305 | 2025-08-15 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 7dd04a09-fdf0-3fe3-88c0-12c6f6ff9602 | -9.1892 | -59.6752 | 2025-08-15 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 871a2674-bfa3-3b18-b8f4-aee8ed385f51 | -9.518 | -60.5268 | 2025-08-15 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 590b2841-cdd7-3097-8dfd-e3c541a87144 | -9.1708 | -59.6568 | 2025-08-15 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8f00f50f-b8d7-3731-9c5d-7ec4cd7a409e | -6.0807 | -59.9465 | 2025-08-15 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e6fdea6f-d893-3154-8ec5-7fe249d5e4e6 | -6.9302 | -59.5497 | 2025-08-15 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cb15f64e-5961-39a8-b686-daac56389d94 | -9.4994 | -60.5278 | 2025-08-15 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 375432e9-e016-3a14-b38c-31f4d7fc444c | -6.6945 | -58.8259 | 2025-08-15 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 59afcaf7-c465-3e25-87c3-b387035198bf | -5.455 | -60.1391 | 2025-08-15 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ab054326-4b9b-3d54-9db2-a6bb86cca334 | -9.4992 | -60.547 | 2025-08-15 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e75f06eb-2490-3159-a218-c2ff373ab283 | -7.3116 | -60.628 | 2025-08-15 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 255fb15e-722f-374b-a7ae-1d7c26fb469d | -9.1706 | -59.6762 | 2025-08-15 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| eb9f0662-2542-3862-9213-b6167f8d2f61 | -6.9302 | -59.5497 | 2025-08-15 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b56c1b94-c266-3ed3-8643-21f2bb225ff7 | -9.1708 | -59.6568 | 2025-08-15 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 380e36e6-afff-3d1f-a524-9dc9ccfe234b | -9.4992 | -60.547 | 2025-08-15 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 810aee10-5172-3ac8-bb8f-891d15f7d6e5 | -9.4994 | -60.5278 | 2025-08-15 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 81b00db0-e437-3eb4-9b22-fa983422c23a | -5.455 | -60.1391 | 2025-08-15 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7b2736b5-abce-3729-bbf0-95f220de8bb4 | -6.9303 | -59.5305 | 2025-08-15 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 56d4f99f-61fd-3359-8d8e-53e784fdf92e | -9.518 | -60.5268 | 2025-08-15 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d2a4519a-c51e-3fdb-8c4d-9ad53e4a1176 | -6.9302 | -59.5497 | 2025-08-15 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 088b087a-6df7-3194-9904-41f384ea0106 | -7.3116 | -60.628 | 2025-08-15 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 257b3434-a3fd-3a24-9f36-959934a53005 | -9.1708 | -59.6568 | 2025-08-15 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8e2a1888-f411-32eb-8251-fb201d69944b | -9.4994 | -60.5278 | 2025-08-15 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 96dfde0f-d9fb-39b4-b3ce-c25d19fa1d95 | -9.1892 | -59.6752 | 2025-08-15 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 03c83e22-743a-3421-afe4-7ec0b368e411 | -11.3468 | -55.4124 | 2025-08-15 05:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8502402d-be72-3c85-bd07-9c55abfe60af | -9.1706 | -59.6762 | 2025-08-15 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a2ff17a0-4289-305b-a48d-9c0f45238749 | -5.455 | -60.1391 | 2025-08-15 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 416b64f4-bd75-3c9b-b4c7-b39bdfc68f9b | -9.1894 | -59.6558 | 2025-08-15 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 27a8bfc1-7324-3719-b930-a0856e28c9f2 | -6.9303 | -59.5305 | 2025-08-15 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| b399b957-337f-3660-b09e-a8f72e0369fa | -9.518 | -60.5268 | 2025-08-15 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e1ae986c-385f-37d2-8a76-690b2da73d4d | -6.9303 | -59.5305 | 2025-08-15 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| dc57a5d6-0a24-34f0-8b3f-89d01492cbb6 | -9.4994 | -60.5278 | 2025-08-15 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e660fdc3-ca08-3086-b101-4f5b883ac84f | -9.1706 | -59.6762 | 2025-08-15 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9e125280-49c7-3826-a660-711b2dab22fe | -9.1708 | -59.6568 | 2025-08-15 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b37b7c04-d65f-3e10-8599-f0196d2c5c0e | -7.5291 | -61.3444 | 2025-08-15 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 67a746f7-2e64-35d7-8590-0b8555480cdf | -5.455 | -60.1391 | 2025-08-15 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 10d4c5f4-8001-3cbb-962d-c26aa9d86c41 | -9.1894 | -59.6558 | 2025-08-15 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b3ceef48-a512-3d56-a774-4148d6bdb581 | -6.9302 | -59.5497 | 2025-08-15 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 9bf16f91-c3ee-3f9c-9513-e6e235dbfd67 | -13.4759 | -56.6537 | 2025-08-15 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a301828d-75fd-3bb1-af31-8891363ef413 | -13.4757 | -56.6739 | 2025-08-15 05:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 7837594a-819a-39cf-bc24-897f0378cd7e | -7.3116 | -60.628 | 2025-08-15 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 8c9694cb-18f5-3079-aa70-6cddce6fb352 | -6.9302 | -59.5497 | 2025-08-15 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 59431922-1a3e-3190-a7bb-c630ebd59bba | -5.455 | -60.1391 | 2025-08-15 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f02a73d6-f689-3db2-99d8-e74f644e511f | -6.9487 | -59.5297 | 2025-08-15 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a09c9a5d-1d1d-33c4-b7a7-b99e866943d7 | -9.1706 | -59.6762 | 2025-08-15 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| afc68dbf-1f24-3939-8c8a-54c7e71d1ceb | -9.4992 | -60.547 | 2025-08-15 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7b9c72da-ef73-350a-8f7b-f8cc58358ed7 | -6.0807 | -59.9465 | 2025-08-15 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ba7f869e-6515-3fef-8f93-b2fafde3f731 | -9.1708 | -59.6568 | 2025-08-15 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a4cc9d6c-3690-3b9e-b906-5d6b202c84bf | -9.4994 | -60.5278 | 2025-08-15 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3e9a0ea5-603f-37f9-87c0-3b3c83b76b3e | -6.9303 | -59.5305 | 2025-08-15 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7174c637-bbd4-3bba-8641-a57e9fc62442 | -6.92981 | -59.53188 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7db50d5d-2990-3674-9489-b783c1d9e89c | -6.63048 | -59.99813 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c261dff5-3d7b-3277-8c93-83d13f4be65e | -7.23948 | -57.66663 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c40b1bf4-3581-3b99-b91f-929d50684f88 | -6.95138 | -60.13949 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a28087-75b3-3214-8f80-12b022398a7b | -7.31802 | -60.62769 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 403315d6-7ad8-3872-84eb-830a1df46ab6 | -7.43889 | -60.02133 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce4a3c4a-a311-30c9-a1b2-0b7b5892f39d | -7.42518 | -60.0271 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39c38f1e-15d4-3035-83ac-e5b183f2f0ad | -6.70588 | -58.82456 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 76412a00-3686-366a-8209-1870f51d4315 | -7.29834 | -60.62123 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f38772d-26f5-3570-ad46-d7dbc88202ea | -7.42828 | -60.03543 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328ce2f9-35f3-30c8-99df-c4ea77f8963f | -7.32761 | -60.61837 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 927588d1-0cd7-364a-a246-423d41891437 | -5.45603 | -60.12708 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3104f9e4-7db1-3116-9533-aea2ed0768fa | -6.70205 | -58.8518 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8160802b-9ba8-383b-9215-8085a64bb869 | -6.66269 | -58.8246 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2fffcace-5c8b-3603-8f7d-160f7f19f2e4 | -6.7246 | -58.82259 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 240d5402-34f9-3b71-8925-a4aa03e69131 | -6.66524 | -58.81856 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b86b4288-e11f-34c8-91ee-27f76b3efd48 | -6.93961 | -59.52495 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 070bae9b-a852-3705-9003-fed1e36081cd | -7.32256 | -60.62481 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b206c5f1-cd9c-3e7b-aa0b-ea806beee67c | -7.42152 | -60.02271 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56762f1f-0340-3232-8370-038bce17fe8d | -6.69881 | -58.84213 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2fc00a8-e591-39e2-9a58-3b5bbebae64a | -7.06835 | -59.2179 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 549611f5-cb12-308b-98ad-610b55757738 | -7.07902 | -59.20617 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26de0343-ebf2-3b8a-b89d-b3bdb1a63262 | -7.26705 | -60.63147 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5baabe56-4852-3ef3-90dc-4bc9a21b9e40 | -7.31095 | -60.61949 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26acdf6e-ba19-3583-9bef-84341a6f913b | -6.9407 | -59.9962 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be8147ce-efa7-33f4-9255-b18a4a81e974 | -7.15607 | -59.64468 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f90f4f70-0526-3d41-83ad-34849cbe00f3 | -7.03607 | -59.81827 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f56ee0d4-adcd-3b44-b93e-6b26fb08b61e | -7.08283 | -59.21116 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b17c2b96-28a4-3775-ace3-d4c7c9983a23 | -7.31852 | -60.62421 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84c24418-2b74-3334-9162-f488f9ca5a73 | -6.90439 | -59.13912 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d47efd1c-51e4-39b1-967b-3fadccad5096 | -6.90562 | -59.13046 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9db289-8790-3aa9-bff0-94abe47018e6 | -6.87975 | -59.15346 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ad9670-4f45-37f0-b5e4-71f0f479e622 | -5.44934 | -60.14439 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad262b9b-1eb2-3d0a-a49f-c1ed904c7a7e | -5.93729 | -59.93958 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec82b94a-5652-3947-b5bc-6512d484f9c8 | -6.72394 | -58.82722 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c28d0c8c-09f9-3d15-a3a2-0b0e116e1f19 | -6.91515 | -59.54214 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc68f56-3d44-3e86-96fa-6b7a8e630305 | -7.24326 | -59.99838 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5fb5cee-f164-35da-9957-f43ccbb0b2fb | -7.14824 | -60.1252 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4f812a5-eed9-342d-a2ea-9487cc703d8d | -7.08222 | -59.21554 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1292e9f3-5ac9-3f16-b74b-0906f013103c | -6.94207 | -59.99513 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67985538-4ab5-39f9-af4a-bfb6ee4693a0 | -5.73817 | -59.88017 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2989da4-25ca-3883-b959-32e4a72dade1 | -6.67306 | -58.81674 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dea7cf89-2491-3337-82c9-9c1e6c8f5da5 | -7.46246 | -59.88777 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b3d8c2-65f2-3a4a-9ab8-451af3b48c31 | -6.94054 | -60.1264 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa681d1a-b2a2-3d89-b464-cb71bb22deb7 | -5.93066 | -59.92712 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56a837fc-2c6f-39b7-adbe-8cc443540233 | -6.90739 | -59.62838 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
