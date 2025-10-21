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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d844629-2b0d-3abb-8bea-3bff32f7d266 | -18.18421 | -52.96864 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f88c921b-0a4f-35cd-bfd4-05682644b896 | -18.17799 | -52.96909 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5e9e130-abdf-305d-84d5-452b991abfa2 | -18.19588 | -52.97632 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18693115-eb66-347d-9cb7-199f4e127395 | -18.17899 | -52.97289 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd608ee1-d387-3524-bdfd-929a53950034 | -20.48659 | -54.67889 | 2025-10-21 05:18:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f23bfdce-b6cc-350d-8982-8a4f0779d046 | -18.79537 | -47.0142 | 2025-10-21 05:18:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e556ecf-fb3a-3ba3-aaeb-3f94f74220b8 | -18.17743 | -52.97394 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03432862-75f5-3f5f-bef1-87c2b8f5d17a | -18.19127 | -52.97572 | 2025-10-21 05:18:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9de532f-8127-3a47-916d-16a175b9d329 | -18.59237 | -51.71815 | 2025-10-21 05:18:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47bf4757-bbef-3eca-8418-b59e42a16d95 | -19.08943 | -57.53801 | 2025-10-21 05:18:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ddd9c707-8380-3729-853f-d6508982ef79 | -3.4968 | -45.8195 | 2025-10-21 05:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 110.4 |
| b3813a57-d94f-3f7b-aac8-59fbc15d02e6 | -33.05553 | -53.16116 | 2025-10-21 05:23:00 | NPP-375D | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| dca1cccb-6a63-33b8-9d07-5f20d0b58783 | 1.712 | -55.6854 | 2025-10-21 05:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f5cbba9b-996d-3481-a9d1-b5f0768c2f9d | 1.69153 | -55.72668 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2579cd1-3aae-3721-a940-944d4476149e | 3.99236 | -59.71765 | 2025-10-21 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98184120-d4c9-38b5-a8b7-7ce2979b7177 | 1.72633 | -55.69601 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74a2e67c-f28d-3a78-bb74-568ea67ef26a | 1.72374 | -55.67965 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f853607c-7436-3920-ba96-b75a5213cc0f | 1.72161 | -55.7219 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20a33b34-383a-328b-9497-96ed2a708df6 | -1.20119 | -49.07873 | 2025-10-21 05:31:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7603455-e99f-33ff-ac85-97d9567fc4d2 | 3.98899 | -59.7181 | 2025-10-21 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57d97182-6912-3b1f-ac43-ab4fda37445b | 1.71643 | -55.68922 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 34814442-3919-3bb0-aa90-0bcfc8542c3a | 1.70314 | -55.71661 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 931cae2d-c1e1-3367-8db2-8040df416499 | 1.71172 | -55.71514 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 598c5b18-06e3-3f5d-86f0-32d4bcbfc007 | 1.76757 | -55.69016 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4557b1d3-1faa-3040-b52f-dfa49e3b9b43 | 1.76059 | -55.67447 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cef7edd-0555-3730-9c53-43d3c1b21331 | 1.72439 | -55.68375 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3db54151-e53b-33d4-acef-a6e2512a4211 | 1.69583 | -55.72601 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 170b4b3b-76e0-3b2d-b1e5-bf34307ad882 | 1.72504 | -55.68783 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ab7f6d9-aa61-39dd-8a1a-40ed2dfcbbb6 | 1.72032 | -55.71376 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f993a0a6-7a0c-3d82-a545-68d75fd6f55c | 1.83707 | -55.64285 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cb59c59-49d7-3682-81c7-5d7d08179dab | 1.71237 | -55.7192 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 942debc7-106d-3525-bfc5-3be5cd193613 | 1.69648 | -55.73006 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93aba9aa-90ad-349e-bd32-3a2390e470f5 | 1.70378 | -55.72065 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddfded61-c6af-377d-a981-3a6037dd8285 | 1.72073 | -55.68852 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48c75a5-eba8-3bee-9fe3-604507af6a7b | 1.7626 | -55.68678 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca3539e-5187-3cb7-8c4a-bdf6d6256333 | 3.30256 | -61.43873 | 2025-10-21 05:31:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a4d6e69-65cc-3c2a-b09e-23f41c6f74d5 | 1.83492 | -55.64183 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b3cf4a3-0dd2-3b7d-b73d-6f79634b718a | 1.71277 | -55.69399 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f4ccc5d-6845-341e-8d1b-ec1af7ac1ddb | 1.71578 | -55.68512 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c530a1be-1b76-3154-8935-66e433a3ca54 | 1.73879 | -55.70305 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf2c5305-1e25-3fcd-81e9-b6abcfbef387 | 1.72697 | -55.70009 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62552e04-a873-34cb-a520-d7a44e764315 | 1.67266 | -55.74622 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a26381-ffa2-33da-b962-aa03ca613264 | 1.70808 | -55.71994 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d823a73a-ae4a-3c4f-9302-ff1c6d54ced6 | 1.71212 | -55.68991 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 24efbcbc-21ec-3280-82ed-05c9f6dfcd9c | 1.69218 | -55.73073 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 771fb05d-9d72-3f3a-b41d-d5cedb463ed8 | 1.72224 | -55.72591 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1382d1b5-79a6-3e35-9ab6-bb66e58033ab | 1.75697 | -55.67932 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 097a3c22-a79e-3cce-9782-0bd2b06ee554 | 1.75629 | -55.67521 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 620bebbc-3730-3580-b2ee-6282054ad093 | 1.76127 | -55.6786 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a36ac6a1-30a3-31e4-b66b-f9101a3b2c50 | 1.73127 | -55.69939 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a94f5f18-cbad-354a-b5e9-476b5deed745 | 1.76194 | -55.68269 | 2025-10-21 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e2ddc4bc-6421-3908-a9c2-902fd0001462 | -3.33109 | -53.24814 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5dd36e-74db-3a6d-ba4d-642459c018e8 | -2.85741 | -50.74125 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3eaa9ad-2f31-351e-accd-f8d6f821610c | -3.58316 | -55.45053 | 2025-10-21 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a09f9306-0809-32d8-8ab5-6b26a7c2c4c0 | -3.58394 | -55.44541 | 2025-10-21 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3532c9cb-a283-3d72-97cb-347281360c08 | -2.40612 | -57.65955 | 2025-10-21 05:33:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4deed366-c9bc-36d5-aaec-164d9374307f | -3.23501 | -54.77908 | 2025-10-21 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 886018f5-86a5-33f9-8705-323000e14361 | -2.81327 | -54.38343 | 2025-10-21 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c23f17-0990-3ce3-b76c-a82266edf279 | -3.54416 | -55.41833 | 2025-10-21 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06035a2d-a547-3c8f-8391-23d472e00bc2 | -2.25406 | -51.91486 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0309eb00-4481-3151-a5f7-b78b1e4b2189 | -2.8137 | -54.38052 | 2025-10-21 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be17ed73-4ebb-329e-8bc4-dce38efb5958 | -2.20663 | -56.89077 | 2025-10-21 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6157e5c8-efb9-338d-bfc6-f3d4c72bcc6c | -2.16466 | -53.48988 | 2025-10-21 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6d8c5f9-c276-319b-890f-d7417bfb8ac4 | -3.6627 | -52.1206 | 2025-10-21 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5eecdac4-62c5-3c03-9ba3-eef194245a6e | -2.17051 | -53.48737 | 2025-10-21 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807f0823-d733-3f64-ae62-33ea158d87dc | -2.05966 | -56.8337 | 2025-10-21 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32f5afc6-765e-3ee5-9a4c-ceb44e43a195 | -2.8582 | -50.73592 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2276c230-ccc4-3ecb-bdf3-0a364f97e939 | -3.58402 | -55.44727 | 2025-10-21 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0265187a-67f8-33f8-a5c0-781eced3aee4 | -3.11405 | -51.20399 | 2025-10-21 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a26982d-074a-3155-8d13-4e85cf742dcd | -2.16999 | -53.49073 | 2025-10-21 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94ad5840-eae7-3acc-8fdc-59ea77b80e0d | -2.34393 | -57.11899 | 2025-10-21 05:33:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24c561f2-77da-3e4a-b55c-2bf7219835c3 | -3.11331 | -51.20894 | 2025-10-21 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38c8ca84-016c-3854-957f-3d8f8593d861 | -3.65672 | -52.11983 | 2025-10-21 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f6bac0c-f8a5-377f-9ba0-785cd444229f | -2.87348 | -50.72187 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19316a4a-5ec5-3448-9b94-1a129cc3c12a | -3.13114 | -52.99973 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdc6eaf-1c05-3bcd-b9bb-838a02bfc199 | -4.66512 | -49.68301 | 2025-10-21 05:33:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46b7ceb1-a8b0-3235-abaf-a9335361a38a | -2.86464 | -50.7369 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ed4bced-2de4-340e-a6db-e8b094c159eb | -2.24814 | -51.91394 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b25a8a3-342a-3297-9625-d7a61017b1ce | -2.86384 | -50.74223 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdbc5f9e-a4b2-358b-9745-3515478af428 | -3.59649 | -55.26662 | 2025-10-21 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bc6fe2a-983c-34da-a4d0-ec1ef5e12146 | -3.3207 | -53.35554 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cb3943d6-028c-37af-a59c-8dc560da2f62 | -3.33163 | -53.24456 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 386ff64d-34c0-3507-ae99-46d032642a2b | -3.13057 | -53.00354 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5a75368-d199-3aaa-82aa-2fa19a6fa01f | -3.32018 | -53.359 | 2025-10-21 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7901326-6469-3050-9c9e-140de74c17de | -2.70523 | -59.68755 | 2025-10-21 05:33:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d0b19be-a67e-3e05-ace3-886c3a4e9fd0 | -2.16855 | -53.48728 | 2025-10-21 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c6facbf-0e6b-3798-91a4-08d117c21805 | -2.25341 | -51.91914 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c6eed53-e11c-3236-a635-25dcbe68b81c | -2.24749 | -51.91825 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46c588d8-6639-3ddf-95c5-cb309da61e9c | -2.87427 | -50.71658 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b2dcb95-a7ce-3bcd-b346-82fac3bc9617 | -3.77852 | -64.1693 | 2025-10-21 05:33:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27ade391-1868-394f-bae3-f9de38150583 | -2.85661 | -50.74657 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20860b71-7016-3aa9-a438-3eb20d172b32 | -2.16805 | -53.49065 | 2025-10-21 05:33:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dc04ff6-2d8c-3ee3-8ccc-c33f41ff0893 | -2.86304 | -50.74751 | 2025-10-21 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df563bcc-d707-3b93-a375-bb9b3ce3d19a | -9.00764 | -65.91953 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 85c6db69-ac73-38d2-badf-a71388c71729 | -9.78111 | -63.81299 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2254fe7f-167e-3f89-919e-1a66c7b84383 | -9.64145 | -64.74168 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfb5cc1-1b1b-3f4f-93cb-4dd3a9f4c8f6 | -9.11775 | -65.36324 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a527bacc-4ee2-3793-974e-2b541354f937 | -9.62378 | -64.746 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d717311-2386-33a2-9350-97d928fb6c90 | -9.03919 | -65.70232 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83bc6d72-16fd-36df-b363-4b9f1843ecbb | -8.99859 | -62.10186 | 2025-10-21 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
