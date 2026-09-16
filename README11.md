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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b834b8ee-d39d-306f-b098-67432c505a5b | -5.144 | -55.9345 | 2026-09-16 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 993544c2-873e-3474-9654-518701cfa89a | -11.9033 | -43.8112 | 2026-09-16 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| e9771207-150f-3bad-8111-03bce4784c33 | -9.112 | -45.7294 | 2026-09-16 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 2d0ed397-3df6-3c89-9872-be44a570471a | -5.1215 | -47.6146 | 2026-09-16 02:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 66316002-0b20-3522-8d25-f5dc569b0395 | -9.0931 | -45.7314 | 2026-09-16 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e0cf1237-9030-3222-9820-934cdc5745b9 | -7.6511 | -67.164 | 2026-09-16 02:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0b5daccf-49ed-3da4-ad26-dd1871681c88 | -11.1401 | -40.4748 | 2026-09-16 02:40:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 81.1 |
| f08c453b-3b97-31ab-ae8b-b4c5b2c966ad | -9.4943 | -45.4362 | 2026-09-16 02:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 671abaaa-d0dd-3b54-9652-1035199b3c9c | -9.4102 | -62.7113 | 2026-09-16 02:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3118403e-72ad-3972-93b6-44197e1b5ec2 | -10.7729 | -46.2096 | 2026-09-16 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 34a0e3e5-a72b-37b0-ab33-54f2bd20277d | -15.2329 | -49.4021 | 2026-09-16 02:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b97b6564-72eb-37dc-9f7e-3394c4c23997 | -5.1624 | -55.9338 | 2026-09-16 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 2528f04c-497d-372c-b3d3-5a8a4639d8e3 | -12.12 | -57.1967 | 2026-09-16 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dd609cb1-d758-32fc-aca9-6a271d23dd98 | -15.2529 | -49.3769 | 2026-09-16 02:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 804d9903-ae91-3aff-882c-edfb13e75452 | -15.2334 | -49.38 | 2026-09-16 02:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 184.7 |
| b4460444-94c3-3148-adc8-312747af7f88 | -15.2329 | -49.4021 | 2026-09-16 02:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 798adb53-f3e3-3b5e-aa57-2c4ee15b1b0c | -9.457 | -40.3889 | 2026-09-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 0b2e91e5-1420-3ffc-a088-4279959df365 | -9.1117 | -45.752 | 2026-09-16 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 4d0d8dbb-1b1d-356f-a11a-f8bc58cedaee | -9.4102 | -62.7113 | 2026-09-16 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a373c938-af62-39df-8163-1ebcf65a0d5a | -2.6966 | -57.6084 | 2026-09-16 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c8009316-6352-3933-8a0c-cf6d33363706 | -5.1215 | -47.6146 | 2026-09-16 02:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 653ee892-41a0-3f3a-896f-19f7a445b61b | -5.144 | -55.9345 | 2026-09-16 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 5fc9c0d1-05cc-3a7c-98f2-e76d1de064ce | -9.4574 | -40.3641 | 2026-09-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 2691f2cd-a9d3-3e49-a66b-e9ce36c83d47 | -11.9033 | -43.8112 | 2026-09-16 02:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5dfabf15-2c70-3556-8a65-d9407c2d6ed8 | -7.6511 | -67.164 | 2026-09-16 02:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c36a1b86-5562-39db-af4a-a5e77548346b | -11.1401 | -40.4748 | 2026-09-16 02:50:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 9014238e-6597-3f0f-a3f6-8531387f3851 | -9.4943 | -45.4362 | 2026-09-16 02:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d667f0b7-4798-38b4-a5d0-234f65a37c9e | -9.112 | -45.7294 | 2026-09-16 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 394ef922-bd22-3d56-9323-0f7e98fcf001 | -12.12 | -57.1967 | 2026-09-16 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 345761e3-6ab3-3468-a795-b7ff5632c767 | -9.0931 | -45.7314 | 2026-09-16 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 81203dd6-09f8-36cb-9d5b-a81a1351f250 | -5.1624 | -55.9338 | 2026-09-16 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ca710fce-c999-3ac0-b2dd-2e4a9e2be029 | -2.6965 | -57.6278 | 2026-09-16 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| a95f2dd5-4e0d-3ad8-95cd-30d95bb5e62c | -9.457 | -40.3889 | 2026-09-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.3 |
| 3ed26cda-0343-3d99-b851-d59336fffe43 | -5.1215 | -47.6146 | 2026-09-16 03:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f83d5b86-d610-3432-8ad5-eb209ee34cb2 | -5.144 | -55.9345 | 2026-09-16 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| c79bc2a8-4a74-3ae4-852f-590988625b38 | -9.0931 | -45.7314 | 2026-09-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 87e3f971-59fc-3ab7-9a62-c6b52b131361 | -7.6511 | -67.164 | 2026-09-16 03:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| dbee490f-0568-338c-88a5-577e64f9ac56 | -9.762 | -46.5796 | 2026-09-16 03:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 9ff0b8e5-1a59-37ec-8203-a379fd772e9e | -9.4574 | -40.3641 | 2026-09-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 1b876031-c723-30a0-8689-7edeee4c5611 | -11.1401 | -40.4748 | 2026-09-16 03:00:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 3b42c156-04de-3b64-9e45-dda01e93b337 | -5.1624 | -55.9338 | 2026-09-16 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cf320048-3b41-3506-bafe-daf414396b6e | -9.4102 | -62.7113 | 2026-09-16 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 911db30a-48e1-3e46-81aa-d545e496d551 | -9.112 | -45.7294 | 2026-09-16 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 2cb05aa1-8b7b-3a71-ba6d-9cba7a89fa77 | -2.6966 | -57.6084 | 2026-09-16 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 60f3631f-0413-3fb2-b42a-6a669c1d4553 | -2.6966 | -57.6084 | 2026-09-16 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 6c777629-5211-3ff2-bb5c-623919399217 | -9.762 | -46.5796 | 2026-09-16 03:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6c044a09-4ee7-39ce-ad11-e194e5277901 | -9.0931 | -45.7314 | 2026-09-16 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 478f7230-b2ca-3bf3-bc6c-fe278b82dade | -9.4574 | -40.3641 | 2026-09-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 5559ba49-2369-3186-bcb9-cddc5bcfcedb | -5.144 | -55.9345 | 2026-09-16 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| c952b308-ad27-34da-a772-1e3cbfacdb7a | -9.4102 | -62.7113 | 2026-09-16 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 50c2a24a-6c06-3613-a608-643bf960800e | -9.457 | -40.3889 | 2026-09-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 8288f9ce-85ed-366f-ac15-95a19cfee7fe | -5.1624 | -55.9338 | 2026-09-16 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 5eb2ed8c-1388-3a1c-932c-009128d1accd | -5.1215 | -47.6146 | 2026-09-16 03:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2c57815c-1b5a-3754-b4f0-028b0065ab1c | -11.1401 | -40.4748 | 2026-09-16 03:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 120ee7fe-f91c-3416-a66a-60dd650ee4ff | -9.112 | -45.7294 | 2026-09-16 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 22514423-3dc6-3d1b-b5e8-c4c76abb6da7 | -17.0431 | -41.2862 | 2026-09-16 03:10:00 | GOES-19 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.6 |
| a16ca235-2941-3a9c-a30d-51882e978947 | -7.6511 | -67.164 | 2026-09-16 03:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 50cc1df2-b018-3806-952e-d21410b5f9df | -9.5284 | -42.9646 | 2026-09-16 03:17:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f26e1a60-63ba-354a-a3f2-51e4e75369b2 | -9.45805 | -40.38056 | 2026-09-16 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 5c5ef22e-44aa-37be-9d6c-4ea899042bb8 | -10.58529 | -36.99026 | 2026-09-16 03:17:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe29aed6-9dd2-37aa-959e-024c23f08d98 | -5.87754 | -35.35148 | 2026-09-16 03:17:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c646259-e439-368d-912f-e92316b6a131 | -7.03684 | -42.04409 | 2026-09-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 071ea0cb-3ede-3c3e-a061-66620c8c4f40 | -7.09379 | -40.65091 | 2026-09-16 03:17:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ec4a592b-5326-309d-a9e4-d54220699844 | -10.10035 | -36.18909 | 2026-09-16 03:17:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9189dd96-de7f-388d-96b9-7bdc830ad708 | -7.18417 | -41.80996 | 2026-09-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b6282c7a-6d76-3ffb-bbe2-71e07ca89b47 | -8.48021 | -38.12586 | 2026-09-16 03:17:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b88a705a-13a3-3ba9-a820-3c1af74e9e15 | -9.45725 | -40.38476 | 2026-09-16 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.6 |
| e2a2b1df-b33d-3c4b-a26c-5b0a9e9c2e51 | -4.6752 | -42.09633 | 2026-09-16 03:17:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 12a5a3f0-8216-3200-89be-dd2d92ae76cb | -9.45645 | -40.38897 | 2026-09-16 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 6171f94f-bc86-35d4-b956-32704ddeb084 | -7.09352 | -40.65595 | 2026-09-16 03:17:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 167fcebb-3f67-3280-8900-d46aef41d413 | -4.6764 | -42.08956 | 2026-09-16 03:17:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 818c08d4-60ad-3d08-9d58-edb894c7624f | -5.8788 | -35.34855 | 2026-09-16 03:17:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 348aafdf-5744-34ca-9249-58b12d4319ef | -5.63116 | -40.8525 | 2026-09-16 03:17:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c3dd121c-d320-3b70-bd77-bb0d8403726b | -5.63033 | -40.85717 | 2026-09-16 03:17:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d9f4ac06-eefa-3d78-a1a3-0791bf094268 | -7.09289 | -40.65572 | 2026-09-16 03:17:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7c184975-5a36-39aa-8c39-f786789c690a | -4.67389 | -42.09701 | 2026-09-16 03:17:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2ee20c13-d6a3-3831-8474-1bb298821c5e | -10.5847 | -36.99244 | 2026-09-16 03:17:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2f09608c-8b3b-3a30-9867-e06314eb02b1 | -7.09439 | -40.65113 | 2026-09-16 03:17:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 35dedfd3-f077-30d2-ac3d-b03093bb69cb | -4.67513 | -42.09025 | 2026-09-16 03:17:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4af35a4e-e047-3561-9245-f741f7f03522 | -11.88846 | -43.81979 | 2026-09-16 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 3657f080-ed87-37de-a03c-d97621165f97 | -11.13717 | -40.48672 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 302fe4d5-3ec9-36ec-8e49-faba8ddaa6f9 | -18.23129 | -41.24424 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 883725d4-6dc9-33c6-a58d-df10e9aaa7b3 | -15.28459 | -42.81528 | 2026-09-16 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66d9b425-39a0-3b0f-a7ee-21a3e4543a2c | -12.47334 | -41.41687 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 765ac424-d15f-3597-bcb6-1edeb2aaa294 | -11.16677 | -42.79402 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 459b1674-1e00-3370-94ca-d4ed8946b1e7 | -15.36518 | -42.196 | 2026-09-16 03:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4d2bb151-e333-37bf-9bf0-7400701ec965 | -17.04095 | -41.29156 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| bad63006-5c94-30b1-a225-ff5105f454ed | -13.56131 | -43.52737 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 149301d2-e921-36ff-87b2-5b89a3cccc68 | -18.23191 | -41.24121 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d588bb72-6e33-32e6-9396-83d29465a519 | -17.03863 | -41.27542 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9fec22c9-f62b-3289-b031-99ae239f5b5c | -11.24295 | -43.44225 | 2026-09-16 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55c5d719-0e62-36e1-b9dc-fe7e5f58942a | -11.20141 | -42.82486 | 2026-09-16 03:19:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b72f5f96-8635-3b81-ac96-e1bea06cb229 | -18.22984 | -41.25131 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cafc9dbe-2df0-386e-8bdd-8081e372fb59 | -18.22663 | -41.24027 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 6bf67cdf-9f00-315d-88d5-7066c539a639 | -13.55038 | -43.50825 | 2026-09-16 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ca0802-4d44-327b-9453-4e5413bb9f4d | -12.47125 | -41.39699 | 2026-09-16 03:19:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ed7317f5-3f11-316c-a028-7ca9c85d2f14 | -15.88581 | -39.94111 | 2026-09-16 03:19:00 | NOAA-21 | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c19f229a-c84b-3f3b-8ce8-e1080e6630b1 | -18.22597 | -41.2435 | 2026-09-16 03:19:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 57c54090-b062-3d2d-a052-c75d54188b21 | -11.13306 | -40.47762 | 2026-09-16 03:19:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2407be08-b8a8-33ec-8362-f816d67305f4 | -17.03716 | -41.28261 | 2026-09-16 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |


[Clique aqui para ver as próximas entradas](README12.md)
