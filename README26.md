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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 331820db-b910-3623-a8e8-54500886a4ab | -15.1124 | -52.7257 | 2026-08-08 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4dd0f36c-d305-392b-9175-4453f0264bd6 | -7.3562 | -42.8666 | 2026-08-08 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 63780de6-6f50-336b-a85c-8e4dcfe0afb4 | -15.4039 | -53.8047 | 2026-08-08 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6ef7a6e5-9342-392d-b67d-b63902b3f8cb | -6.9763 | -41.4971 | 2026-08-08 14:00:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 49e9ddbb-1f28-342f-979f-0c6f2b9584ce | -10.2662 | -45.7979 | 2026-08-08 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 42b0aa37-38b8-3164-aea1-827b5567249e | -0.9797 | -55.3962 | 2026-08-08 14:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b5bb3d48-943a-3760-b638-99c47da3af9a | -11.3099 | -44.8569 | 2026-08-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 420.0 |
| 87f7a983-06e3-37e0-b09a-8d198b61d250 | -11.2908 | -44.8596 | 2026-08-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 032705c4-1e33-3007-af00-60af90cd5275 | -17.8797 | -40.0685 | 2026-08-08 14:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 200.9 |
| 30a3597f-f691-3f10-b3e2-e56fc21b0235 | -7.3751 | -42.8647 | 2026-08-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| b4cc7936-f769-34a4-a4a3-56838d604320 | -5.89 | -57.6538 | 2026-08-08 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 102f89b2-fca7-31b1-a2a8-aad3538132b9 | -14.9254 | -48.2523 | 2026-08-08 14:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 3d610cd4-6c1b-3a92-9cfc-21aeaff78374 | -6.9979 | -42.9016 | 2026-08-08 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| a805c24d-6a55-317f-8882-6ab82f30f986 | -8.5501 | -45.4044 | 2026-08-08 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e1ffd019-da50-3451-8ff3-37372d8d0e90 | -6.9765 | -41.473 | 2026-08-08 14:00:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| e417df91-a4c5-333f-bcdc-758b59971cce | -11.2503 | -54.0146 | 2026-08-08 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 674794ba-95f0-3c84-a7af-b6668be2254f | -11.3103 | -44.8337 | 2026-08-08 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ff801ecc-3a14-388f-ad18-3cf16abb5f88 | -10.2659 | -45.8206 | 2026-08-08 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bda4796c-f70d-3c89-b12c-871dc5bf0a76 | -11.2314 | -54.0164 | 2026-08-08 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 0f20c76e-b255-346b-a9d0-6ba68a94b3e7 | -6.9765 | -41.473 | 2026-08-08 14:10:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 216a7328-2c26-3fc3-8677-6ef07be732d4 | -11.2501 | -54.0352 | 2026-08-08 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 48e29c6a-558e-36bd-91f8-ad2ed4d85fdc | -6.9763 | -41.4971 | 2026-08-08 14:10:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 144.4 |
| a8463acf-9643-3ac4-8a60-09bf8623f9c2 | -11.6601 | -51.6644 | 2026-08-08 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 3eb1f344-d741-3da6-a10a-d231a307b986 | -15.4039 | -53.8047 | 2026-08-08 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 030d8be3-2f64-305a-abd0-1d4ed618c6b9 | -7.3751 | -42.8647 | 2026-08-08 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 60da9b08-7242-3021-8357-15243e1b4807 | -10.5001 | -46.6491 | 2026-08-08 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5e79358b-7188-3477-a98b-ad3809f584ac | -12.3423 | -53.1416 | 2026-08-08 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 4fbb55f3-5b28-3a0c-afdf-866f4181410e | -20.8826 | -42.7819 | 2026-08-08 14:10:00 | GOES-19 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.2 |
| 571794dd-e378-3a64-9327-cb19dd0afb62 | -11.2503 | -54.0146 | 2026-08-08 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 64905b63-9306-366e-ac15-35434d86c9a4 | -11.3099 | -44.8569 | 2026-08-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.0 |
| 667e3029-475d-3372-ac3b-e3ab512f99ef | -11.2312 | -54.0369 | 2026-08-08 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| efe451a7-2381-3f0d-9195-3835771e2680 | -17.8805 | -40.0424 | 2026-08-08 14:10:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 477.4 |
| 585095bd-a01f-37c4-96be-97f38a92c0af | -12.342 | -53.1625 | 2026-08-08 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| f392edae-bdc7-31b3-9dc0-7aa60224a398 | -15.6968 | -54.8534 | 2026-08-08 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| ed0fe871-2a39-3e84-8ac1-e819109e03bf | -15.1703 | -52.7392 | 2026-08-08 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8bbc21d5-7475-336a-aa97-ca9fcfd31cc7 | -11.3103 | -44.8337 | 2026-08-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 06f6ea87-e3c7-363f-a526-4e69c7661612 | -11.2908 | -44.8596 | 2026-08-08 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1c9532dd-e7a1-32a8-8538-c85277fefac1 | -6.9979 | -42.9016 | 2026-08-08 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| ef4a18d9-2d25-3912-a8b0-387cf9354e07 | -12.3229 | -53.1645 | 2026-08-08 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bb80d45f-ffd9-3983-b986-8f9b929e9ed5 | -15.1124 | -52.7257 | 2026-08-08 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fa35096f-d3df-3553-866c-6270547e4f4a | -14.3422 | -54.9929 | 2026-08-08 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2a7b005d-d5fe-3ea3-ba45-f0c8aff6e2fd | -10.4811 | -46.6515 | 2026-08-08 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d172fdbc-04a2-38d9-b8e1-2bb288ea4de1 | -0.9797 | -55.3962 | 2026-08-08 14:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| fb3598e1-571a-3055-9918-91a7cd05b586 | -14.014 | -53.8292 | 2026-08-08 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 96f6517d-aafc-356b-916e-4af2fbb5e43e | -11.2026 | -54.8363 | 2026-08-08 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 70f185e0-9376-35a4-9584-2274e22d364b | -7.3562 | -42.8666 | 2026-08-08 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 422b3ee1-f82e-37a5-bbb3-68f943ad3142 | -8.569 | -45.4024 | 2026-08-08 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dd012d64-6b3c-3d90-a0fa-0ef4204ed307 | -14.9254 | -48.2523 | 2026-08-08 14:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 88169241-a40c-3925-a4ea-884ef8283790 | -17.8797 | -40.0685 | 2026-08-08 14:10:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 184.6 |
| d86187de-fda2-35ee-b557-aefe2a8d6e90 | -14.3238 | -54.9331 | 2026-08-08 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 852dbe8f-bf81-3ab2-855e-07aefce7ae2a | -14.3235 | -54.9537 | 2026-08-08 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d9d009ed-a664-353c-808e-f10f3f3d0332 | -17.89 | -40.06 | 2026-08-08 14:15:00 | MSG-03 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bc168c4-7e0e-3fc3-a710-46fd9193e3aa | -6.9278 | -42.4354 | 2026-08-08 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 1322abe2-db38-365c-a744-4030e0f8c90e | -7.3562 | -42.8666 | 2026-08-08 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| e73280e2-3639-34b6-b904-802929191a8d | -7.3751 | -42.8647 | 2026-08-08 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 606619fb-2e97-3070-965a-cd88f6882643 | -15.6968 | -54.8534 | 2026-08-08 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 83a2271e-b8e1-38e4-ba2c-74299b9fa246 | -8.5501 | -45.4044 | 2026-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 452676fa-99d6-3e60-88c1-43b54df5d7a0 | -15.0926 | -52.7495 | 2026-08-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ba8acb0b-6d2d-349a-8d23-c902eab3facc | -17.8805 | -40.0424 | 2026-08-08 14:20:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 433.5 |
| 13c201a2-a75f-3ed8-9410-6b78778adb9d | -8.5687 | -45.4252 | 2026-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c76dbd6b-31e3-3a46-bcd9-8d9975385f21 | -11.2501 | -54.0352 | 2026-08-08 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6cc605c9-79b0-328a-b04e-d73abac60726 | -11.2026 | -54.8363 | 2026-08-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| cd3c9187-66d6-3120-9aee-90f54d1fd91a | -11.6601 | -51.6644 | 2026-08-08 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 231de827-f650-3a3d-ad8e-152b6554089c | -6.8599 | -58.9351 | 2026-08-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5459db6e-10d1-3d4d-b627-e19345c8c812 | -12.3423 | -53.1416 | 2026-08-08 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 644135ba-0dd7-3a68-8848-9715b175c5df | -15.093 | -52.7283 | 2026-08-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 41914e22-6380-3cbd-a48c-2e84135e0f88 | -15.4039 | -53.8047 | 2026-08-08 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 74cbb7ad-3dbc-302b-8917-1654ea958058 | -12.342 | -53.1625 | 2026-08-08 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| d59c1099-be37-3849-a97c-e57891f5d1db | -15.7163 | -54.851 | 2026-08-08 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bbb1b6a3-4c86-3098-baeb-69d1f0008539 | -0.9797 | -55.3962 | 2026-08-08 14:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f5dd8fcb-8817-31da-8c55-1baf16e61fdf | -15.3848 | -53.7862 | 2026-08-08 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4d07d31f-7483-307e-8715-35d4be1147f6 | -14.3422 | -54.9929 | 2026-08-08 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 769cc89e-ba61-3e8e-8de9-6802000b01ad | -8.569 | -45.4024 | 2026-08-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| d62bb730-ec41-3c24-adf2-0831a4308651 | -6.9763 | -41.4971 | 2026-08-08 14:20:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| ba492a44-cfa7-3423-a070-2deb19adb4e4 | -14.9254 | -48.2523 | 2026-08-08 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 461a34c8-e407-306b-9c2b-6b02b3391483 | -11.2503 | -54.0146 | 2026-08-08 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ceca7c08-0f8b-3451-ac47-d3ab8c1aabfd | -17.8797 | -40.0685 | 2026-08-08 14:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 185.1 |
| f1e0824b-1348-3372-aae7-1f47aacc9947 | -6.9146 | -41.936 | 2026-08-08 14:20:00 | GOES-19 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| d8a8061a-01cc-3367-b17f-6be9434851ec | -10.4811 | -46.6515 | 2026-08-08 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d02f536c-5a28-34c2-95d3-567e9a80d1e3 | -11.3099 | -44.8569 | 2026-08-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 246.4 |
| eebf4d49-c006-3147-be95-bf36dccbf022 | -15.3845 | -53.8072 | 2026-08-08 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a7c14d97-16a5-35ad-a479-f5145d7901e8 | -8.6573 | -45.8686 | 2026-08-08 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5334e6aa-bb70-3adb-bc8b-8217e9ed9719 | -11.1838 | -54.838 | 2026-08-08 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e1c10ce1-0816-3e8a-89b4-a63f2e1bc5e4 | -6.8784 | -58.9343 | 2026-08-08 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ce63be1c-6ef2-388c-af45-5cbe35d5b8f7 | -15.1124 | -52.7257 | 2026-08-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 69e5c626-7947-3553-b278-9ede47dee47c | -11.3103 | -44.8337 | 2026-08-08 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| aadb1d52-878c-3773-bfc8-7f39bc9e59a0 | -15.112 | -52.7469 | 2026-08-08 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| fdf322c9-c844-33ec-82a0-c7220d374e43 | -15.6972 | -54.8326 | 2026-08-08 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b0c619c9-757b-3d48-bbef-675817d672d3 | -11.6598 | -51.6855 | 2026-08-08 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| d65371f3-7f59-316b-b55d-48725c437082 | -6.8599 | -58.9351 | 2026-08-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b85a270f-9888-349b-9666-0f6de1952958 | -6.9763 | -41.4971 | 2026-08-08 14:30:00 | GOES-19 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 29e9eefd-2d9e-3c7c-a69f-88485c6e481a | -8.5501 | -45.4044 | 2026-08-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 534d2163-2e56-3633-b3bd-bf6fc32ff538 | -14.9254 | -48.2523 | 2026-08-08 14:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 37b268c2-f263-3e2c-8955-cfa938da6cb5 | -8.6573 | -45.8686 | 2026-08-08 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 73e9c1c5-4cbb-39b2-8dd3-fadc09c0af59 | -11.6601 | -51.6644 | 2026-08-08 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 271.7 |
| 0322e453-5280-34a9-885a-398ea1287372 | -10.5004 | -46.6266 | 2026-08-08 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 68ab3a7d-06a9-3bf5-8e8f-cfdc62fe6f31 | -7.2042 | -42.9759 | 2026-08-08 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 7e580902-1ef2-3094-91d7-8c236a36b352 | -12.3423 | -53.1416 | 2026-08-08 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 08905453-52e8-3856-a1b1-d86f82f30306 | -8.5687 | -45.4252 | 2026-08-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 112f7ded-cc28-3a7e-a2c9-a3e169ca8504 | -17.8797 | -40.0685 | 2026-08-08 14:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 219.6 |


[Clique aqui para ver as próximas entradas](README27.md)
