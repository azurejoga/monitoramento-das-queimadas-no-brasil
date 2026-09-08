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
| 73dde4f1-48c0-379d-9e7a-6fa06f87f803 | -6.1302 | -47.2444 | 2026-09-08 00:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4d5730d3-df80-35b5-a8ea-d4908ea800c1 | -6.7675 | -58.9583 | 2026-09-08 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| cd82b3bc-06a8-3c91-9cff-c5d55b1329a1 | -13.2289 | -61.7161 | 2026-09-08 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| dc115adb-bffa-372d-b49d-9449d8005a21 | -6.1118 | -47.2237 | 2026-09-08 00:10:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 521.1 |
| 824b83e7-6a8c-3840-94f1-d012c369a245 | -13.4458 | -43.8128 | 2026-09-08 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7a6324d8-52ea-329c-8f14-51c2ee7e7a0a | -21.9928 | -56.0491 | 2026-09-08 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 06181005-cfe0-3431-ba38-9a2e150fd442 | -3.5592 | -48.1666 | 2026-09-08 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 4644cbc3-0b85-37c4-8d73-0c753f2e2f7b | -11.3904 | -45.7412 | 2026-09-08 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 102d8f26-4ce6-303b-b979-6b1ad8bb6ce6 | -3.53 | -48.15 | 2026-09-08 00:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e085351b-c4a8-3e1e-844b-923580ee2454 | -3.53 | -48.2 | 2026-09-08 00:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6860a91c-37ca-3714-9481-fd0885f646b6 | -13.2287 | -61.7355 | 2026-09-08 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c874deb5-2f04-31cc-8b16-9e2207a8ecc4 | -3.5407 | -48.1673 | 2026-09-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 719dd708-5928-3fba-a713-f5512dc89bb9 | -3.5591 | -48.1882 | 2026-09-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 219.2 |
| fcda7085-a269-3e50-9c8c-581015bea130 | -6.6357 | -59.4459 | 2026-09-08 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| eeb3e67d-f56b-37dd-aefb-744e44b171f6 | -13.2099 | -61.7173 | 2026-09-08 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 27a70a9e-0fd9-3473-8dfe-4865923022ad | -13.2291 | -61.6966 | 2026-09-08 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 4490832f-5a3e-3401-917f-17626b1f5771 | -3.5406 | -48.1889 | 2026-09-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 284.5 |
| c70c712c-914a-331f-a15f-5d192723090b | -4.3587 | -47.7853 | 2026-09-08 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b19229f6-fef9-3c90-a832-a3968e3aa01e | -13.4458 | -43.8128 | 2026-09-08 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0ce82d3e-5f26-3e7b-a6d6-c5f83bab2512 | -6.7675 | -58.9583 | 2026-09-08 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| eb8de92d-aadf-3088-abf7-eaf9870794ae | -13.2289 | -61.7161 | 2026-09-08 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 5acc11f6-df79-3d8a-9d51-cd9088da4283 | -3.5592 | -48.1666 | 2026-09-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 509db012-6233-3fa2-84ba-f33431f63cd1 | -13.2479 | -61.7148 | 2026-09-08 00:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a51f5db9-097e-3a24-ad80-93a13d4aff6f | -13.2669 | -61.7135 | 2026-09-08 00:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9eb7b1e6-c4a3-393e-9a5f-d95ec74f2d6e | -9.7515 | -43.4378 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 14ddd7c9-d91e-306c-ab8e-d17ee6e38939 | -3.5406 | -48.1889 | 2026-09-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 332.4 |
| bac10ba8-c34a-3596-a156-47f9330ee48f | -9.7511 | -43.4614 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5eec3479-da7c-31ac-939d-2a3b9cda0a75 | -6.6357 | -59.4459 | 2026-09-08 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| be1d3430-be5f-3478-908f-f9ac8f801d81 | -9.7702 | -43.4589 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6752e912-381f-33e7-9f6a-55eb2442ebb5 | -3.5591 | -48.1882 | 2026-09-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 234.4 |
| 182a18a9-b18e-33b4-84e1-61f9c1e1ffd3 | -9.7131 | -43.4664 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5015d05e-6b12-39d8-843e-722a47fbec8c | -13.4264 | -43.8163 | 2026-09-08 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4f913762-68be-3f5b-9ec8-b34ec432e3c4 | -10.2187 | -36.3162 | 2026-09-08 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| a00d9d37-28e4-3feb-be0f-804fd71b2f1a | -21.9928 | -56.0491 | 2026-09-08 00:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c6e3b4b7-82a3-3d44-a87a-27c75239f7b6 | -20.609 | -57.9928 | 2026-09-08 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 776b6efe-0e3b-3fbd-8dd5-b84bada9dc6c | -3.5592 | -48.1666 | 2026-09-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| ae1b6140-5fb0-3a5e-9636-87b644a9deec | -9.7134 | -43.4428 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c176b399-ff13-321c-b554-336ce9d6058b | -3.5407 | -48.1673 | 2026-09-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 5e8fe632-f294-3017-bce2-97dd83c64906 | -21.9721 | -56.0525 | 2026-09-08 00:30:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 70b72ab6-cbd2-3788-b647-733e820a2d05 | -9.7705 | -43.4354 | 2026-09-08 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a73022d2-3b55-307e-a7bc-620f2e11adf3 | -8.5322 | -63.8604 | 2026-09-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 70ffae69-adff-3d4e-8945-379a08ba6eae | -4.3587 | -47.7853 | 2026-09-08 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2fed75d2-898a-3dba-af17-39e33bbd959e | -21.9721 | -56.0525 | 2026-09-08 00:40:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8a0731df-3a02-384a-9160-61814aa8a9ee | -3.5407 | -48.1673 | 2026-09-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 31078b40-00e6-38cf-9b70-2bc22b2e5ad4 | -20.609 | -57.9928 | 2026-09-08 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 1021e650-4b42-3f38-9718-abe61e86e61a | -3.5591 | -48.1882 | 2026-09-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 192.8 |
| b725f266-d9a4-3aba-8ca0-b395b975ccc4 | -21.9928 | -56.0491 | 2026-09-08 00:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 12b5911f-a960-3373-b84c-b258a301af83 | -3.6821 | -49.5315 | 2026-09-08 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| a6a1fd4e-dec5-35d2-afde-84692b990c17 | -6.6357 | -59.4459 | 2026-09-08 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 8af12dd3-0af0-346a-9cd4-7dd615d26cc1 | -3.7006 | -49.5308 | 2026-09-08 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 271.0 |
| 236c6c73-da7b-3578-999f-16bc188c7aad | -3.5592 | -48.1666 | 2026-09-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 0b04e05b-846b-3abe-aee3-6209577fa608 | -13.2479 | -61.7148 | 2026-09-08 00:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2d5200f1-d567-325d-b8b1-7ce3d5779411 | -9.7332 | -43.3932 | 2026-09-08 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 9ebbb5dd-bcf2-3d40-9e78-b4923bfdffcb | -13.2289 | -61.7161 | 2026-09-08 00:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 89fd835f-156c-39f2-be82-839dd215a484 | -8.5322 | -63.8604 | 2026-09-08 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 095c1ec5-fb9e-3670-a4b3-8e2f33ecb103 | -9.7138 | -43.4192 | 2026-09-08 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 3cbf001f-2c7d-3a12-a1d0-1f04969d6ce5 | -3.5406 | -48.1889 | 2026-09-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 93fd4f76-4c24-3050-a5aa-828af2978968 | -3.7005 | -49.552 | 2026-09-08 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 01f7dfba-1322-3170-a6ca-ddf9881594cd | -4.3575 | -47.769901 | 2026-09-08 00:46:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8651d2-47b4-3c1a-9ea8-7abe1d594eb3 | -8.5358 | -63.844002 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55c6b342-31e5-37bd-9930-b0d3ab00791c | -3.8859 | -55.810101 | 2026-09-08 00:46:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023bb60b-be09-3da0-b54e-6af6454bfd0c | -6.6298 | -59.435398 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8cd5a2-b456-3195-9dcc-a40bdb9214ae | -5.9903 | -57.702099 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdba6541-04e2-3c10-8a21-29d7a48cb09e | -20.6047 | -57.994202 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1cc8dcbc-5cf9-3db0-9847-200e31c9ae05 | -20.6161 | -58.0 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c17800cb-6d1b-3fdc-917c-a7fc9b5d5c31 | -6.6396 | -59.4333 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45fa25dd-e976-39d3-ad38-71f4edf427c0 | -6.0001 | -57.699799 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba57c932-22ab-3943-9311-590a26b0e6dd | -13.2795 | -61.763802 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e97e672-aedd-32eb-add6-839922f3eb69 | -6.1096 | -57.637501 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186c3da3-0b69-3a46-9258-906fa33c8dc1 | -3.1544 | -60.649899 | 2026-09-08 00:46:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 682f6b51-18df-374f-a3c4-f06c7e9d42ae | -5.9821 | -57.711399 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4b0792-7f61-3a2b-860e-416606815ae8 | -13.6175 | -59.469501 | 2026-09-08 00:46:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44836a82-ba63-3446-842f-f4e152e24c5c | -4.064 | -55.778599 | 2026-09-08 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d501c20-79d3-30da-af65-084e3de73b3b | -3.4143 | -59.2458 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd5dce5e-5b84-3390-946d-e7d924522245 | -3.688 | -49.537701 | 2026-09-08 00:46:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3baac300-bec4-3d07-bef5-ba42a10aaad9 | 4.1456 | -61.220001 | 2026-09-08 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cfc2484d-431a-30e3-8e5e-3d6a7c348750 | 4.1441 | -61.226898 | 2026-09-08 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 33e79a40-6d8e-3a47-9544-50c3b2078a03 | -6.0603 | -57.783199 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0599c888-8b79-3d41-8d7d-1ce20b217b6f | -6.7677 | -58.949501 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 724531ed-7778-38f8-a81a-55ea98671e71 | -8.8569 | -63.381901 | 2026-09-08 00:46:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c677ab8c-b0fc-3f48-be28-5bf812edf3c0 | -13.6158 | -59.461899 | 2026-09-08 00:46:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4514e7c-feed-3448-ad46-83c8040ebb96 | -1.188 | -55.7146 | 2026-09-08 00:46:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6c8c4c2-31f0-3f57-adbe-b9165f73babd | -6.442 | -58.146599 | 2026-09-08 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b3f3f2-9fb2-3bc6-8888-f9fba0ff2262 | -3.421 | -59.2299 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5512104b-5066-3c1b-92eb-e9d234c853d1 | -6.6381 | -59.426399 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e361f61c-6298-372c-936b-6cf27ec78b73 | 3.3217 | -61.308701 | 2026-09-08 00:46:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 607a648c-0fec-3000-9437-6ac146c5fe50 | -10.7707 | -60.7841 | 2026-09-08 00:46:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3bf1ed-c4fb-35d8-a6b1-76b61cd98cc7 | -4.2321 | -59.947102 | 2026-09-08 00:46:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88ba6be2-32df-3ec4-8822-eaae9ff25520 | -9.0769 | -58.961399 | 2026-09-08 00:46:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbffcea8-bc2e-325d-aa33-fc5433ea148c | 4.466 | -60.483799 | 2026-09-08 00:46:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 03d8d120-6805-3e30-af95-7cb4021c4c81 | -15.8404 | -56.601398 | 2026-09-08 00:46:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59605d7d-fc44-333d-b337-d486d461ac10 | -6.7988 | -58.949799 | 2026-09-08 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af58322d-07c7-38a9-a9a4-3f8b1866c906 | -13.2775 | -61.754101 | 2026-09-08 00:46:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e036d04-9bd8-3920-90f7-364b137bfd17 | -20.617701 | -58.008099 | 2026-09-08 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d67b592e-ccdc-36d6-9c29-1c33301d9468 | -2.8356 | -53.987701 | 2026-09-08 00:46:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ca6503-8b70-3a9d-a605-ca7f8a77846b | -5.3684 | -56.027699 | 2026-09-08 00:46:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adcf682a-261d-31f8-8512-058225f74e4a | -15.9948 | -56.4151 | 2026-09-08 00:46:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7b2e426-816d-3772-9cf3-0697b0b75b90 | -21.973301 | -56.044998 | 2026-09-08 00:46:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b1c01871-58ad-3809-a0ec-e02d6e44cb26 | -8.5162 | -63.848099 | 2026-09-08 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14539102-31bb-346c-9787-6f691c589961 | -2.5841 | -59.4021 | 2026-09-08 00:46:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
