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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5ebd3b-d05d-3609-bfda-f0bff5653efe | -11.9512 | -41.3251 | 2026-03-14 00:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 028eb277-998c-3d27-815e-4c86226784d5 | -11.9512 | -41.3251 | 2026-03-14 00:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| ad9f095f-67d8-3e39-95fd-d5840cc22af2 | -11.947 | -41.313599 | 2026-03-14 00:19:00 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e80999f8-8216-3edf-b58e-3a77822f466c | -11.9373 | -41.3162 | 2026-03-14 00:19:00 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1f14b4b6-0bd3-3fff-8bdf-87647b5134b2 | 0.9103 | -60.2714 | 2026-03-14 00:19:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 31f1d5e0-8552-383e-8d9a-a2bf2ee340d0 | -20.2432 | -40.2192 | 2026-03-14 00:19:00 | METOP-B | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31a0dad2-9f73-303c-9e12-44815256233f | 0.92 | -60.273602 | 2026-03-14 00:19:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce3d1e6-b479-3c31-a67a-9acbc69dac48 | -11.9326 | -41.2981 | 2026-03-14 00:19:00 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 57056d9a-e909-3de1-b05b-2ff33254548b | -11.9423 | -41.295502 | 2026-03-14 00:19:00 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c4e8327-a7cb-338d-a08f-546adbacbfde | -11.9512 | -41.3251 | 2026-03-14 00:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 29e891b4-f9c2-3607-9f7f-a58a3264aae1 | -11.9318 | -41.3285 | 2026-03-14 00:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| e5920b54-5c1e-39ef-8d13-d43b028b3d05 | -23.5556 | -52.50623 | 2026-03-14 00:20:00 | TERRA_M-M | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 0f9d8391-c0a4-394c-80a5-28e4bd5e5cca | -17.2093 | -55.18998 | 2026-03-14 00:22:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 51f0d22b-6f2d-3c23-9245-7d1d1ce453c0 | -11.7814 | -47.09002 | 2026-03-14 00:22:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0b792221-129c-33be-8bdf-de6bd5fc9f6d | -11.939 | -41.32816 | 2026-03-14 00:22:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 151.9 |
| 5b55246e-f352-3fae-99bb-c28bc2471ec3 | -11.78289 | -47.10035 | 2026-03-14 00:22:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 97e6518d-7341-3b94-8ffc-820d7df78992 | -11.94359 | -41.35528 | 2026-03-14 00:22:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| c66c5390-ea02-373d-b8c4-66102e3d7ab7 | -11.78703 | -47.09386 | 2026-03-14 00:22:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca94b589-e0db-3247-b9ac-7a6eefeeca6b | 0.90911 | -60.2836 | 2026-03-14 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5770e543-b29f-3c5a-a04a-afb02b84d46a | 0.90527 | -60.3059 | 2026-03-14 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 7325a17f-8bbd-393b-83e1-d76fdcfdc35c | 0.90505 | -60.31103 | 2026-03-14 00:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 663fea24-1897-36bd-9692-662431bf6830 | -11.9512 | -41.3251 | 2026-03-14 00:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 234bd56d-47e2-3d54-8fd0-2dc476567127 | -11.9318 | -41.3285 | 2026-03-14 00:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 58.3 |
| fce4a275-5c61-3cbb-835e-31a182bf5f00 | -11.9512 | -41.3251 | 2026-03-14 00:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 103.6 |
| d4840f63-76ec-311e-9b94-4cf3668a518c | -11.9512 | -41.3251 | 2026-03-14 00:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 79.0 |
| aabbdcc1-11bb-3699-985a-35184e74652f | -11.9318 | -41.3285 | 2026-03-14 00:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 249bf2b7-00bf-3e2f-98e9-1a4cf6c0fd9e | 1.7699 | -60.395302 | 2026-03-14 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 096198f9-a352-377a-853f-63b06e29c88e | -11.9538 | -41.335899 | 2026-03-14 00:54:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 49afc7e2-d388-3bd2-8d78-8b841940a942 | 1.773 | -60.382 | 2026-03-14 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8a3b61-e759-3b61-b32f-f7b13809175a | -11.9431 | -41.2953 | 2026-03-14 00:54:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0326e693-7b8d-3021-b1c2-d34109694dd9 | -11.9485 | -41.315601 | 2026-03-14 00:54:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c06a2594-8c3d-39b1-8e43-9bc88442c922 | 2.3216 | -60.232399 | 2026-03-14 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cb3d4d62-247b-3d7b-a354-3a1306dec6b3 | 2.3119 | -60.230099 | 2026-03-14 00:54:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1dffb515-cc21-3232-a65c-2a58d312ecd2 | -11.9389 | -41.318298 | 2026-03-14 00:54:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fcefcc70-ddfa-34b3-9039-c1bb010f32c6 | -11.7887 | -47.093102 | 2026-03-14 00:54:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a600637e-f318-32f8-a7bd-3c2e38b3fa0e | -11.9318 | -41.3285 | 2026-03-14 01:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 9078a299-bcff-3cc0-8eab-70b85a965a46 | -11.9512 | -41.3251 | 2026-03-14 01:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 70e98787-91b5-3f87-ab63-08764fc731b0 | -6.5631 | -51.1126 | 2026-03-14 01:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4baf2444-0538-38ec-ab43-79af246d466f | -11.9512 | -41.3251 | 2026-03-14 01:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 79f676fc-a5de-3c22-85fc-684e877f7c04 | -11.9512 | -41.3251 | 2026-03-14 01:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 8a5417f5-21a6-3bc2-844a-6063f3f14114 | -11.9512 | -41.3251 | 2026-03-14 01:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| eb34503f-57eb-3240-84a2-3c0129d51a62 | -11.9318 | -41.3285 | 2026-03-14 01:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 8d390c91-1188-34a3-b1d5-09789b675e8b | -11.9512 | -41.3251 | 2026-03-14 01:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 10160b4a-47d1-3cf0-a042-8ba8f8d7f788 | -11.9512 | -41.3251 | 2026-03-14 01:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 58.0 |
| d9f11e67-11b3-32ff-a06c-abc720032ac3 | -11.9512 | -41.3251 | 2026-03-14 02:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 74345d09-effe-3975-a5b9-cdefd0bacf64 | -11.9512 | -41.3251 | 2026-03-14 02:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 9e708149-1610-39ce-8ce3-76ff27eb1170 | -11.9512 | -41.3251 | 2026-03-14 02:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 038ad9ed-365b-3eb8-9dde-1afbc9c1565c | -11.9512 | -41.3251 | 2026-03-14 02:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| d6f3cc84-9acc-31fd-a57d-807ac9bc29ba | -11.9512 | -41.3251 | 2026-03-14 02:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 05f3b608-1646-3e63-9a6d-4b259d86f4db | -11.9512 | -41.3251 | 2026-03-14 02:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 61.3 |
| d766cd53-25b8-3f5f-956f-84998cb1da33 | -11.80106 | -38.22205 | 2026-03-14 03:08:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 891af91b-2f71-3ff2-9cbc-c38cb35f668e | -11.96256 | -37.95436 | 2026-03-14 03:08:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d552c94a-9453-3cc4-956d-bcfd7e2e5fb7 | -11.9512 | -41.3251 | 2026-03-14 03:10:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 20b2b7b1-e2ff-360a-a01a-f95f8f372faf | -11.9512 | -41.3251 | 2026-03-14 03:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 54.5 |
| b4be6774-eaf2-3795-9f77-4d1353a98a34 | -5.69651 | -44.12577 | 2026-03-14 03:36:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 578beecf-6535-3105-b6d5-91f153918355 | -10.23208 | -36.49178 | 2026-03-14 03:36:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf17cc4e-83c6-380f-a1fa-9eff6e169587 | -8.88004 | -44.78489 | 2026-03-14 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0312300-7c2a-357c-b374-84d999ed39ac | -8.88109 | -44.77938 | 2026-03-14 03:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49a0b776-6bf6-33c9-b90d-e5e0bdb69a42 | -5.52851 | -35.52205 | 2026-03-14 03:36:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 80843714-42e8-35d7-bf4f-8689f18ea1fb | -5.52924 | -35.51757 | 2026-03-14 03:36:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 54248dbf-6f4a-3197-8662-3ee7e9ee8264 | -11.96404 | -37.95253 | 2026-03-14 03:38:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2e4a5c1-b076-3c60-b6ea-c1425833690a | -11.80051 | -38.22256 | 2026-03-14 03:38:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3a2ba964-5142-360a-8bb6-46103b5785dd | -11.80452 | -38.22329 | 2026-03-14 03:38:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 81f40679-da70-3e91-a365-5047a9071ec8 | -11.96625 | -37.95441 | 2026-03-14 03:38:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3dd26ca-442b-3a3e-a63f-65d7ce2bf7b8 | -17.57895 | -39.49935 | 2026-03-14 03:38:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a4a90634-a978-336c-a052-45fdcf7de0d8 | -10.66639 | -40.30453 | 2026-03-14 03:38:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea84e987-1089-3b05-bfb4-034752a95d7b | -11.93982 | -41.33118 | 2026-03-14 03:38:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 33.6 |
| c625c6d0-4e51-3bb1-90d3-4e98e1a20cfe | -11.94472 | -41.33213 | 2026-03-14 03:38:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 33.6 |
| f7715a9b-ca60-3dd0-a59c-61c0f2d347b6 | -11.94087 | -41.32563 | 2026-03-14 03:38:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 88b05d15-fa22-3b85-a38d-461b2aae876f | -11.94577 | -41.32658 | 2026-03-14 03:38:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e817927f-e2b3-3064-9f2e-520aca8c90ea | -25.23511 | -52.13671 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d303a64a-be21-3332-ac97-c6fac4ef7e02 | -25.2391 | -52.1224 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| efd84fee-91dc-3d50-bc26-58409567b624 | -25.24336 | -52.12516 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2d7d0871-f318-3584-8fc0-1076fa660559 | -25.23246 | -52.13716 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 93ee9aea-ebfd-3bac-9d45-9606e51075b7 | -25.23437 | -52.13015 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 81aeeb83-b100-3183-a96a-62d0a64ab131 | -27.68549 | -48.75055 | 2026-03-14 03:42:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dede9913-8d5a-3c84-bec8-8281afc77e7b | -27.68592 | -48.7534 | 2026-03-14 03:42:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6329d928-592e-39ff-b9e4-6d627c224510 | -27.68443 | -48.75491 | 2026-03-14 03:42:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a51e95c7-e0f4-3e70-8094-a72bebc9e90a | -25.23704 | -52.12979 | 2026-03-14 03:42:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ce543cda-78c8-3f9c-9f22-fc605d75b3d1 | -5.53022 | -35.51606 | 2026-03-14 03:55:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d525e8e-2f56-3f5d-89fc-c2c7c2f06a64 | -5.61078 | -37.53034 | 2026-03-14 03:55:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20a6b105-dd94-3975-b3af-b8db1b726628 | -4.91475 | -37.48539 | 2026-03-14 03:55:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4c707a2-5ded-3f03-9c1f-0bd4e74e41d7 | -5.5296 | -35.52004 | 2026-03-14 03:55:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7f230988-6110-3ec6-a4ce-6a85c4e3103d | -10.23043 | -36.49031 | 2026-03-14 03:57:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36e4943d-f073-3763-a345-ea24ec7e0c23 | -11.80394 | -38.22163 | 2026-03-14 03:57:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f044bd6d-0df6-3f8f-b804-87dbd00ea509 | -11.96394 | -37.951 | 2026-03-14 03:57:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b25ea6c-1dc8-35a0-b7c0-d88d299ec247 | -11.78355 | -47.09541 | 2026-03-14 03:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e49e449-bc08-3ffd-8758-bbb1fbcd4f0e | -12.05663 | -40.68038 | 2026-03-14 03:57:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 334f6c53-c24e-32fb-9605-059aca9b31a7 | -11.7789 | -47.09446 | 2026-03-14 03:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e317478-d551-3073-832d-8552858a5c5e | -10.43017 | -40.35377 | 2026-03-14 03:57:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 37bf2e70-6272-362d-915e-b7053eaf60d5 | -11.78263 | -47.10046 | 2026-03-14 03:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09192f61-9bbf-3a89-9390-be1532b67fdc | -8.30113 | -35.96012 | 2026-03-14 03:57:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef688c89-0e66-38bf-b071-997fdde0e167 | -12.32546 | -43.65395 | 2026-03-14 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c4df75c-92d6-35fe-82ad-46e5122e0df3 | -12.09257 | -38.88772 | 2026-03-14 03:57:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e0b1d081-cabf-3222-8bbb-6c197181b65f | -8.8805 | -44.77874 | 2026-03-14 03:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 44c54340-97aa-3469-8cc7-d5dbe88efde9 | -11.9408 | -41.32505 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 768fc621-0166-3299-9b99-c1b22789d143 | -13.18475 | -43.55152 | 2026-03-14 03:57:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaab5c95-1f90-3e4f-afe0-a91b391430fb | -11.93896 | -41.32898 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b4353df0-9a21-3efa-8ccc-a58c4f528f74 | -11.80056 | -38.22109 | 2026-03-14 03:57:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f3454ca4-9747-3f48-afad-b0208b32dad9 | -12.32917 | -43.65461 | 2026-03-14 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
