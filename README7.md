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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3be283ef-96ec-3674-b4de-bd0d5394372a | -21.9049 | -55.3755 | 2026-08-14 02:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c0b9a692-1d26-36d5-8eb3-1be948430404 | -13.3794 | -42.3854 | 2026-08-14 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 22da3fc2-f08a-38bd-81a6-f9f4536a34f4 | -16.9191 | -54.1481 | 2026-08-14 02:40:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| d2d06513-b023-3471-b7a7-c81d0d44ed26 | -4.5055 | -42.5561 | 2026-08-14 02:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 2b9ceedf-4df6-3d14-8f5c-4823be77e88a | -12.516 | -55.7935 | 2026-08-14 02:40:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 31e6a659-eb27-3c2e-8a90-cf572997b57c | -4.5057 | -42.5325 | 2026-08-14 02:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| baf595b2-618a-3167-a30d-2912652a0918 | -11.4885 | -54.6273 | 2026-08-14 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 851b87de-bb19-38d0-a543-871ac190ba49 | -22.619 | -47.9773 | 2026-08-14 02:40:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 0ca5cc9f-1b88-3785-97d8-7ab87b7b0247 | -6.6195 | -59.0416 | 2026-08-14 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e2a42556-1adc-3398-890f-da0f2d6d6490 | -22.598 | -47.9827 | 2026-08-14 02:40:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 609eb04c-1b94-3174-b7b2-63a99d1fdd06 | -13.2415 | -54.2476 | 2026-08-14 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0375744a-9a66-3d30-81fc-12039035419f | -6.4164 | -39.2641 | 2026-08-14 02:50:00 | GOES-19 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 6635cfb2-8109-37b5-9c91-8fcaa5a9e261 | -13.2413 | -54.2683 | 2026-08-14 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e8a4c864-625c-36b4-9d4d-202534256d9a | -16.9191 | -54.1481 | 2026-08-14 02:50:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e3a7f986-cd50-3ce5-9e42-374cdb4c0a9f | -13.2415 | -54.2476 | 2026-08-14 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 93dd7240-fd5f-3f0e-858e-47117ae0002f | -21.9049 | -55.3755 | 2026-08-14 02:50:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fa29ea68-f2c3-304b-b4ee-186f549bde01 | -4.5055 | -42.5561 | 2026-08-14 02:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| d5cba80b-ac21-3541-afb2-9de82810a65b | -6.9145 | -43.6351 | 2026-08-14 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7d81caf4-5b92-3e67-8310-25391d23ecb4 | -11.4885 | -54.6273 | 2026-08-14 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5e0ae6dc-9f87-3382-8545-19ece5d5c013 | -6.6195 | -59.0416 | 2026-08-14 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 69ae53a3-8bf0-3ff5-b794-78aee6499dde | -4.5057 | -42.5325 | 2026-08-14 02:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 0360dd95-9213-367a-ad3b-08038e353078 | -13.3794 | -42.3854 | 2026-08-14 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 5d26e268-bec5-3fb4-b744-314f91f514ff | -13.3988 | -42.3817 | 2026-08-14 02:50:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 6ba1393d-2688-3d92-9840-ed61674df714 | -20.9552 | -49.1439 | 2026-08-14 02:50:00 | GOES-19 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| ab737869-6df9-3412-a0ca-d3bcfaebc5bc | -13.3988 | -42.3817 | 2026-08-14 03:00:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| a3b81806-a1c4-37d0-b555-2880d61adabd | -13.2801 | -54.2228 | 2026-08-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 9772cd60-c12f-3536-99bd-3ae66769ca52 | -11.4885 | -54.6273 | 2026-08-14 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| bdf6ac4d-2809-3875-befb-3bf01145d1cd | -13.2224 | -54.2497 | 2026-08-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 27bf8911-e35a-3c34-9e0c-390d5ef47018 | -14.4507 | -51.8576 | 2026-08-14 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4584282a-8c91-3a7a-830d-f8896f3c659e | -4.5057 | -42.5325 | 2026-08-14 03:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 71a79b24-a20b-3845-9c79-a8abb7cc8863 | -6.1855 | -47.3284 | 2026-08-14 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 8d3614f8-d89b-33b2-9d17-3a78b344d0ed | -13.2415 | -54.2476 | 2026-08-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| dd920c28-e288-3867-a358-b04ddbc8cf1f | -16.9191 | -54.1481 | 2026-08-14 03:00:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 77279744-0047-36d4-bdd9-3d73c8c792f3 | -13.2221 | -54.2704 | 2026-08-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| d34ea244-f870-34c0-9596-152f5c97f4d9 | -4.5055 | -42.5561 | 2026-08-14 03:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 9f538140-d516-32d0-90b0-332047c73c0b | -13.2413 | -54.2683 | 2026-08-14 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 3102645a-6dd3-3be1-9045-fd7a80477c67 | -6.6195 | -59.0416 | 2026-08-14 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4d6515cd-5f18-3747-8af3-c15b0d420fc6 | -21.9049 | -55.3755 | 2026-08-14 03:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 297b5b6d-88e8-39ef-9e49-058d789a9cac | -13.2415 | -54.2476 | 2026-08-14 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 235.8 |
| 3dd2e64b-a542-31c0-a687-e4aa38255e58 | -4.5055 | -42.5561 | 2026-08-14 03:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 36119e88-346b-3b52-ba6d-b28ed67ae45e | -13.2413 | -54.2683 | 2026-08-14 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 269.6 |
| d3c93022-111c-3018-83ff-b85b4ceed0d6 | -21.9049 | -55.3755 | 2026-08-14 03:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a7426f99-1073-3ea2-bee5-c166d6b07b40 | -14.9401 | -46.6214 | 2026-08-14 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5a64d4fb-f831-3f28-81d8-94fe02ed1b11 | -13.2221 | -54.2704 | 2026-08-14 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| d381231f-d42c-3505-bf92-fda257f00a2e | -13.2224 | -54.2497 | 2026-08-14 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 82d6d5ae-7da0-3369-afa4-78c864d98f87 | -13.3988 | -42.3817 | 2026-08-14 03:10:00 | GOES-19 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 69.9 |
| f49773ee-86ad-31c4-afed-d7d6ef2ec441 | -4.5057 | -42.5325 | 2026-08-14 03:10:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| fbe6638d-e6e6-32a0-9fb0-1584b93ef13c | -11.4885 | -54.6273 | 2026-08-14 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3aabbe38-0c26-3451-a2f0-2f329364c9e8 | -6.6195 | -59.0416 | 2026-08-14 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4285245a-7dfd-3453-8825-9e96d2e342b7 | -13.23 | -54.24 | 2026-08-14 03:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 533d4fd5-9124-3040-9456-f1636f57e961 | -13.23 | -54.31 | 2026-08-14 03:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baa3e8d2-0de0-3771-92aa-8f18f359d02e | -13.26 | -54.26 | 2026-08-14 03:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12875e60-e6d5-39a3-9268-1fcae0c8d43c | -11.4885 | -54.6273 | 2026-08-14 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b6654cb2-468c-3841-a620-d5710917f2da | -6.6195 | -59.0416 | 2026-08-14 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0c10d8d2-b474-366e-b33a-fd70be1915b2 | -6.1855 | -47.3284 | 2026-08-14 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 0accbf7e-fb4b-3a4f-b64d-f5631c6e5899 | -13.2413 | -54.2683 | 2026-08-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 2b9ee95c-dc93-33c5-8a54-3a211684e8b7 | -14.9401 | -46.6214 | 2026-08-14 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 16cc43cd-3d07-3290-8453-27137ed8e2d6 | -13.2801 | -54.2228 | 2026-08-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 657ae491-7441-34cc-a546-b26ca2116ee3 | -13.2415 | -54.2476 | 2026-08-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f5312cf0-2792-37f2-96bf-f0c421bb0891 | -13.2221 | -54.2704 | 2026-08-14 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e884eb58-74cc-3c64-9585-1ee7976b00b6 | -6.6195 | -59.0416 | 2026-08-14 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3acd3642-4635-366c-9c35-eaf9c1e5ddb8 | -11.4885 | -54.6273 | 2026-08-14 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 629217aa-0366-369d-8ad7-28daefb62077 | -6.42092 | -39.26053 | 2026-08-14 03:36:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 97f48da8-a293-3359-ab01-2bd37fa589ed | -4.49428 | -42.54637 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c5c18974-c6ff-35f6-b53d-5d0490ff172e | -5.55354 | -44.11514 | 2026-08-14 03:36:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18899356-02c2-3ee4-80db-7a02b09e179a | -4.49313 | -42.55321 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 138145c3-5be0-36d8-b7f0-0c4998746900 | -4.50506 | -42.54808 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 96055e10-8cc5-3c37-a618-ed320b8aebf6 | -6.91389 | -43.64244 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eee208a5-1dd0-3589-96af-6a1aafce44e7 | -4.49543 | -42.53954 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| f2e20327-72d3-35d8-a705-ef661af6b590 | -4.49967 | -42.54721 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7e593ca8-3ab0-3ca1-b6c0-eb2520b5a5e8 | -6.92056 | -43.64364 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b1d06eb0-7222-38fa-8dba-885a0507412c | -6.91634 | -43.63503 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 684d7f47-aa2b-3f0e-a94a-71d14a536fb3 | -6.84268 | -42.9055 | 2026-08-14 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2ebe225-fa2a-3d3f-b2a7-c18a0330f134 | -4.50025 | -42.54379 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8ed0478d-08ad-352c-8ee8-9135a15210a0 | -6.83673 | -42.90817 | 2026-08-14 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6cbb6a99-618d-3fe0-b7cd-f654af16f178 | -6.91496 | -45.73008 | 2026-08-14 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b36baf-33b7-3b5a-9ff1-03ace9d42f61 | -6.11147 | -44.03024 | 2026-08-14 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9311b681-e1e3-3952-a759-744fbb20ca6f | -6.9219 | -43.63594 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a7f0b02-d9cf-3f8d-a685-3b1b2463b081 | -6.97593 | -41.46759 | 2026-08-14 03:36:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ebcbcd3-cade-3be1-840d-04554ce5a43d | -6.97527 | -41.46937 | 2026-08-14 03:36:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65c0fa84-524e-3b87-94a2-aae860af07a4 | -6.40771 | -39.26255 | 2026-08-14 03:36:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa5cad37-c9eb-303b-a99d-f5a9f086c7c5 | -6.90833 | -43.64149 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c65ccc78-752b-3ef1-8b3a-919ba11d81bc | -5.87601 | -35.65397 | 2026-08-14 03:36:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d8837f23-c1d8-345f-956c-ac45353eaf48 | -6.92084 | -43.63574 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a10787d4-1863-3986-bda1-33f26a7f2760 | -6.92762 | -41.99677 | 2026-08-14 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3dae9a66-020c-3ada-bc39-ae4a3170ca1a | -6.92123 | -43.63979 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df619239-9755-3d97-9edc-36b735175ed1 | -4.4991 | -42.55063 | 2026-08-14 03:36:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89aa9840-960d-3baf-96a4-e0262c098d33 | -6.41673 | -39.25995 | 2026-08-14 03:36:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6dc50c3-0926-3d93-8300-05ec2a193169 | -6.91458 | -43.63866 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7b0bbf9-07ad-3c38-8184-61184c63cf50 | -7.99441 | -38.32927 | 2026-08-14 03:36:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5f9accf7-e954-3db7-a0a0-f63b324cbd03 | -5.55844 | -44.11504 | 2026-08-14 03:36:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcfd5fcb-021f-3d24-a63c-ceadd7f11aba | -6.41254 | -39.25937 | 2026-08-14 03:36:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60128b7a-6911-391f-b62b-0ad7a8261d68 | -6.90944 | -43.6417 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 549bbb9c-4460-3152-8417-3365bd0304b3 | -6.92132 | -45.7311 | 2026-08-14 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d9b52e1-1d5a-36b2-b216-227de886b009 | -4.52616 | -38.54942 | 2026-08-14 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3803a841-d914-3565-8360-f2a7ff4ae12a | -6.98077 | -41.46819 | 2026-08-14 03:36:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fdff7200-631d-3851-99c4-a5242a0f1f90 | -7.86251 | -35.15242 | 2026-08-14 03:36:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62bfcfe2-f372-3aae-ae16-bede9caabbe4 | -6.11178 | -44.03122 | 2026-08-14 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 71c6d7a9-f545-3030-b397-1108c2d70258 | -6.92015 | -43.63957 | 2026-08-14 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f6a0c03-d860-397a-87d8-74bd017f17ee | -6.83811 | -42.90781 | 2026-08-14 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README8.md)
