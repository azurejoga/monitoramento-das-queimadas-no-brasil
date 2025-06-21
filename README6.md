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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6486858a-4551-3c88-a03c-32dd4249136d | -4.5244 | -47.9943 | 2025-06-21 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d8d41be5-cfe9-3d86-a274-62997a077836 | -11.798 | -57.243 | 2025-06-21 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 766ea182-ac4c-347f-b94a-08c727a7874f | -11.8855 | -54.6517 | 2025-06-21 02:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| cf549058-d750-350c-9b3b-d76e08d37a08 | -12.4577 | -54.4321 | 2025-06-21 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| eb13a111-02e5-36c9-a376-d611321d79d5 | -10.4564 | -47.0347 | 2025-06-21 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 0ecb29dc-4f7d-3e81-98b0-c7e0379f6d33 | -12.477 | -54.4096 | 2025-06-21 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b501bae2-df24-3a60-b335-a98fba22705b | -11.7791 | -57.2445 | 2025-06-21 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1f3afa21-ad42-3dd1-950c-72d2f8fa8d1c | -11.8853 | -54.6722 | 2025-06-21 02:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 204.7 |
| f6e5b72b-9e79-3fac-b266-1ae1e88d465e | -12.4767 | -54.4302 | 2025-06-21 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| fba95849-5c0d-3862-8eec-c2916e561654 | -11.798 | -57.243 | 2025-06-21 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| ba5b7570-99c4-37f3-b155-2e30a126d95c | -12.477 | -54.4096 | 2025-06-21 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 80dcd78b-1f22-35b1-bd56-94ca3dabe431 | -4.5243 | -48.016 | 2025-06-21 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6443e086-85e5-32e6-a545-74cde17fd084 | -4.5427 | -48.0367 | 2025-06-21 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3534a744-726a-3d4d-b4bd-c6e3b72473ec | -4.5429 | -48.0151 | 2025-06-21 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 339.1 |
| 8b69d1cb-4f9c-3116-95de-0a90adecbc08 | -12.4767 | -54.4302 | 2025-06-21 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 178.7 |
| cc734f7d-d18d-3ca7-b84d-6fa6964bb576 | -9.4648 | -57.8449 | 2025-06-21 02:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4fec7204-37ad-391c-8e24-63963b20e709 | -11.7794 | -57.2246 | 2025-06-21 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2e1437b3-56f9-35ba-a00c-77d08be20920 | -11.8663 | -54.6739 | 2025-06-21 02:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c7217f4f-ea6c-3169-a36b-410b3cbe8b1c | -4.543 | -47.9934 | 2025-06-21 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 77a3cdad-d150-3817-9283-b3a4855457bc | -10.4564 | -47.0347 | 2025-06-21 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 42513e2a-a987-33ab-9bdb-d49a3ad4212a | -7.2219 | -43.0682 | 2025-06-21 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 9878d923-e8ef-3e86-a51a-9cb3502e9dd5 | -9.2624 | -57.5228 | 2025-06-21 02:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4c096cfb-3ea3-3e34-8e17-33806032f7a5 | -10.456 | -47.0571 | 2025-06-21 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 476bb395-97ef-3b74-bb1c-9cc103e7dca0 | -11.7791 | -57.2445 | 2025-06-21 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6f34daf1-29b0-317b-824f-982adcf658cf | -11.885 | -54.6926 | 2025-06-21 02:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f2c21cac-e78e-3bce-9df5-ecfd3ad8c114 | -11.7983 | -57.2231 | 2025-06-21 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6b1c1b22-3b7e-362a-8b6f-ede8584d262e | -11.8855 | -54.6517 | 2025-06-21 02:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 4982e087-89a9-30bb-869c-ed7c7b7143f8 | -11.8853 | -54.6722 | 2025-06-21 02:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 213.3 |
| 64812bdb-ab7e-30f7-aae2-51757df0fd00 | -10.456 | -47.0571 | 2025-06-21 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b935b351-a085-3362-9eef-ca1fe4bffdfd | -3.9671 | -48.1283 | 2025-06-21 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9cfcb516-47c9-33ca-b7d8-3aa4f99766d4 | -4.543 | -47.9934 | 2025-06-21 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 9f8e2ac6-e46b-3fb4-8b9b-15deb5cb636e | -11.798 | -57.243 | 2025-06-21 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 165b166d-0ed9-3479-a562-d9095494f14b | -9.4648 | -57.8449 | 2025-06-21 02:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8115f99b-c597-3a33-bd09-0683452644eb | -11.8853 | -54.6722 | 2025-06-21 02:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 67cbfdc0-98fa-38bd-bfad-c6b0474a4e10 | -4.5243 | -48.016 | 2025-06-21 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| acfb2ec5-794e-3017-8b0e-caf771371998 | -10.4754 | -47.0325 | 2025-06-21 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| dbbb4032-a801-3e62-8390-81906fd8bfe2 | -4.5614 | -48.0141 | 2025-06-21 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b1fb2648-361d-3330-bfed-d02f663496dc | -11.7791 | -57.2445 | 2025-06-21 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c21c195d-8985-34f1-8d30-07a05df875c3 | -10.4564 | -47.0347 | 2025-06-21 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 206.0 |
| f10f8940-c603-3a31-886c-535017498f4a | -12.477 | -54.4096 | 2025-06-21 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| aa6bd2ad-e192-3b4d-a065-0cd1416859d6 | -11.8663 | -54.6739 | 2025-06-21 02:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| b8161ad5-ffad-3c00-b3c8-e593dab66f8b | -4.5427 | -48.0367 | 2025-06-21 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| cc3e983a-df30-3749-8a02-88009d6b17a4 | -12.4767 | -54.4302 | 2025-06-21 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 146.0 |
| f5b2e02a-310f-37a3-abd2-9e8fe6b7208f | -11.8666 | -54.6535 | 2025-06-21 02:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 1d963745-c0df-3be0-8e97-9b517f26c75e | -4.5429 | -48.0151 | 2025-06-21 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 299.1 |
| b65896e3-44c7-3653-b1a1-79c8895753ea | -7.2219 | -43.0682 | 2025-06-21 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| c42a8973-0568-33b7-be6f-47ed45c7f759 | -11.8855 | -54.6517 | 2025-06-21 02:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cd43cf0a-8422-3ead-996e-d7f7bccd612a | -7.2219 | -43.0682 | 2025-06-21 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| c7c46002-9df7-3a5a-ac3a-19b0e90fe3a0 | -4.5244 | -47.9943 | 2025-06-21 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1c240a9e-c297-3283-9559-20074185aa95 | -4.5614 | -48.0141 | 2025-06-21 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| aa8a8736-ebaa-36fb-898e-1f64d963cb4a | -10.4754 | -47.0325 | 2025-06-21 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e41e16f1-ec0d-3842-904f-c7d3241144b1 | -10.456 | -47.0571 | 2025-06-21 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2a215aaf-aa8e-34fc-aecf-09d6ecff9ff4 | -11.8663 | -54.6739 | 2025-06-21 02:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 2b02fcd3-0576-30bf-9f8b-2865bc473328 | -11.798 | -57.243 | 2025-06-21 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 67bd03e3-a4be-371c-b1f9-bfe6c9abf838 | -10.4567 | -47.0124 | 2025-06-21 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| f93e3e60-8698-331c-9b23-788af549b254 | -4.5243 | -48.016 | 2025-06-21 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 8a63ad1d-13ba-37b2-a975-073e38576318 | -11.7791 | -57.2445 | 2025-06-21 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| fcc4a03f-b26b-3f15-9044-facddafe1254 | -11.8855 | -54.6517 | 2025-06-21 02:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8eeb929b-cffc-3db7-a36c-9f3e187d0455 | -4.5429 | -48.0151 | 2025-06-21 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 283.6 |
| 06c54553-23e6-3a47-8ce4-19ea3d2a14cf | -11.8853 | -54.6722 | 2025-06-21 02:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 3d07c557-cc7b-3bfa-aacb-ffdc03cd74d7 | -10.4374 | -47.037 | 2025-06-21 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 8f0bd109-5cf3-3b78-8b7a-3e3a5468a496 | -12.477 | -54.4096 | 2025-06-21 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0f055bc9-2156-301f-969e-3db9d644e9e2 | -11.7983 | -57.2231 | 2025-06-21 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6418e012-cab1-37a0-b7d5-804813132145 | -3.9671 | -48.1283 | 2025-06-21 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1de16562-ee5f-32f4-94a5-573e5224dbaa | -10.4564 | -47.0347 | 2025-06-21 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 84c6bb14-d84f-33ec-900c-56e3d148e4e2 | -12.4767 | -54.4302 | 2025-06-21 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 242a3878-b60d-3dfd-8ff8-8c01cf4daed0 | -4.543 | -47.9934 | 2025-06-21 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| c3589ee5-584d-3dee-a9e0-a443d4fd4982 | -10.4374 | -47.037 | 2025-06-21 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3d6d0906-eb3b-3067-97a0-090d0e59f2b3 | -11.8666 | -54.6535 | 2025-06-21 03:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 44d53d14-99db-397a-8a3a-0004b21932c8 | -4.5244 | -47.9943 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b84812b2-fb49-3fce-9735-cda5db411221 | -10.4564 | -47.0347 | 2025-06-21 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 1d1b2263-9a61-3aec-86b1-373c6e712bfb | -11.7791 | -57.2445 | 2025-06-21 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 540a1126-e7ea-3ac0-a495-17b52737f9d9 | -11.8663 | -54.6739 | 2025-06-21 03:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| c24c09d0-7efa-34b5-a003-325adb725e81 | -11.8853 | -54.6722 | 2025-06-21 03:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 148eeb85-cf74-33e5-9769-397bbf82578e | -3.9671 | -48.1283 | 2025-06-21 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1ab4cfc1-18e4-361c-9aa9-f0a2aba820b8 | -4.5243 | -48.016 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 68bc5d09-05e1-337b-8099-66ac3fa5262d | -7.2219 | -43.0682 | 2025-06-21 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| aee72927-70d1-376b-94f3-ee02771ca79c | -4.543 | -47.9934 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| c888921a-c9b3-32c2-88a5-adce8fd41501 | -4.5614 | -48.0141 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4321550d-bdd7-38d5-bbba-1298600c675f | -4.5427 | -48.0367 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d862e7a3-1a4c-33f2-a47c-a2b5e0ff3fde | -11.8855 | -54.6517 | 2025-06-21 03:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 116fd88c-b0a1-3cba-8804-22c0f2ff5e02 | -4.5429 | -48.0151 | 2025-06-21 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 236.5 |
| 88419811-73e7-3220-bf90-80a7524d2376 | -10.456 | -47.0571 | 2025-06-21 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ca28409a-426b-3889-abd8-62fc95649a3f | -11.798 | -57.243 | 2025-06-21 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| f0bf08aa-8f9e-3aaf-9c8d-8c28abf4c9a8 | -12.4767 | -54.4302 | 2025-06-21 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4ed2fdc4-4d9c-33e0-aca3-054969a894ac | -10.4374 | -47.037 | 2025-06-21 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8fd853e7-33fe-3f29-a71e-5dcc6b190864 | -11.798 | -57.243 | 2025-06-21 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 88ab79fb-2995-3283-8f71-ea9d1feb0a5e | -7.2219 | -43.0682 | 2025-06-21 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 3815f18a-2e55-3cca-85ea-c8a4ec28c679 | -11.7791 | -57.2445 | 2025-06-21 03:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| fde455ba-dd9f-34af-8fee-09f3a84fa5c5 | -4.5429 | -48.0151 | 2025-06-21 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 320.7 |
| bce8533f-ec1b-3f9e-8b17-9d1e5f0d28e8 | -9.4648 | -57.8449 | 2025-06-21 03:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 38c0d611-1ed1-3fb8-ad93-e561e02c67cf | -10.4564 | -47.0347 | 2025-06-21 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 93457b8b-7fa6-3d8a-a8e9-1a8b62bc821e | -12.477 | -54.4096 | 2025-06-21 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a541d5c0-0fe0-39d6-87ba-31869965eb28 | -3.9671 | -48.1283 | 2025-06-21 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 791a6265-e688-3b49-a70d-2b7bbcfbdbe9 | -4.543 | -47.9934 | 2025-06-21 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| ff9702a8-e013-35aa-b0a4-79e8efd65be9 | -4.5243 | -48.016 | 2025-06-21 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| f3430a07-abce-34ab-9ff9-6353bd82e8c3 | -11.8853 | -54.6722 | 2025-06-21 03:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| e0a8e29c-0c55-34c0-a73a-f8868dacf8ac | -11.8855 | -54.6517 | 2025-06-21 03:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9e12fe68-448d-329d-a6cd-425987b60997 | -10.4567 | -47.0124 | 2025-06-21 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 17a76e63-36f5-3d18-9367-8a64e8bf6e09 | -11.8663 | -54.6739 | 2025-06-21 03:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |


[Clique aqui para ver as próximas entradas](README7.md)
