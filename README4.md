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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 820935e7-09eb-33c4-b2b3-cf5a738d9470 | -9.1985 | -68.2004 | 2026-09-11 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 96a6dc3c-1793-3701-98da-5cde24445aef | -9.043 | -65.4175 | 2026-09-11 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| dcf0b2db-2323-321d-9c88-155f29f7013a | -9.18 | -68.2009 | 2026-09-11 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 82c6cc6a-81af-3ddc-82bc-5c0fd8e3fc32 | -4.2953 | -49.1021 | 2026-09-11 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8bde393f-69d4-3222-b568-ec6f11735a51 | -10.2243 | -68.077301 | 2026-09-11 01:25:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8ce814-4ac3-3994-8ea3-e0e6f9e5df85 | -9.0366 | -65.397102 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8242429e-6b12-3704-9a47-1f24e2887330 | -10.2914 | -67.2743 | 2026-09-11 01:25:00 | METOP-B | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 83ded055-057c-3fce-9d3b-9627dbf4df2a | -13.3133 | -61.673599 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb6c7881-783b-371a-8512-201dbf740b8f | -9.0323 | -65.422997 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5d44a21-e387-32f7-bb55-83db0507a074 | -9.7558 | -64.940697 | 2026-09-11 01:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb356142-2bf9-3f63-8774-0520a837a5fc | -8.8323 | -62.484402 | 2026-09-11 01:25:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c87d7602-13f5-3e27-99f4-3218a65df02f | -13.3106 | -61.662498 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| baa3efbf-4fa3-3dfb-be1a-d1df2a3352b4 | -8.6311 | -66.500801 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba02bcae-9334-34ff-94e1-7f36d11a8b3a | -9.468 | -68.2407 | 2026-09-11 01:25:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5506b76b-7b7c-3357-8dc2-8db29a8651b4 | -13.323 | -61.671101 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7fde190-0dec-3648-a9c5-9cea4cd7f604 | -9.4202 | -65.8508 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f29db8a9-2ff3-3e98-b466-fdf85cfccd02 | -12.1471 | -64.132004 | 2026-09-11 01:25:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd58ca83-2870-3e83-9d81-37ed1faa4e16 | -9.4006 | -65.8554 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf0d2b6-d9a9-3d44-9adb-21e32832cd38 | -9.106 | -67.683098 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73b2ff7e-87c4-33fb-9124-5da3eb776769 | -13.3203 | -61.66 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c54c1f78-9144-3f9a-b767-d38c0b4eb8d3 | -9.0762 | -65.478798 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 926234b2-f311-37d9-963c-2374442a479e | -9.1583 | -64.416702 | 2026-09-11 01:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae565f4d-2382-363a-9d5e-49b266075da5 | -9.1931 | -68.208199 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea155bf1-1863-3d8b-b2ef-207a4cae7ee1 | -9.1833 | -68.210403 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adcb6e73-9731-3b96-8758-ec1ab60e7a3b | -8.9369 | -66.846199 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b533f881-9e45-31f4-9b72-844d79a7d14e | -9.009 | -65.411797 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0e14819-6ae5-3963-9ae8-09c5fbf11087 | -9.017 | -65.401604 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c37d655-cb86-3c86-a1b9-815628c442b9 | -8.9877 | -65.408501 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 203f67a2-f609-3e14-bb0c-bcf9cb8caf59 | -9.4664 | -68.233803 | 2026-09-11 01:25:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e3b3f745-8d84-3709-9596-971b407f7ec1 | -9.1402 | -67.835297 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e34e7213-f80a-3991-b67d-8df9069e48f4 | -8.9895 | -65.416397 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d83c8fc6-5749-36d1-8733-40272ce5d1d0 | -8.9841 | -65.3927 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa57a10c-a0eb-3b65-855b-64db0fabbddf | -9.5016 | -66.7911 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1df4701-d1cb-3d03-a9a3-fc59154a8889 | -9.4023 | -65.8629 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc4e1889-f6e5-3eb0-a325-c86c9e05f25e | -9.1438 | -67.805397 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca0e67c7-4d3c-3ac7-9938-401ce9cfb8b6 | -9.1802 | -68.196503 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a580231-e8a2-3b98-93e1-5023e2aee5b1 | -10.2599 | -69.073997 | 2026-09-11 01:25:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f6de5d05-58e2-39f9-bd87-623c333cfce6 | -9.483 | -68.492401 | 2026-09-11 01:25:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3421ff-a933-346f-aab1-d456ec0bc2bb | -10.2259 | -68.084297 | 2026-09-11 01:25:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e29ada79-2a63-3dad-91e8-7865b810a410 | -9.1915 | -68.201302 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc26afe2-a24b-3153-9a9d-1477f94a03a8 | -8.6469 | -69.779999 | 2026-09-11 01:25:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d16f1259-2427-3077-9ede-c26b9ea81d24 | -9.0661 | -61.030701 | 2026-09-11 01:25:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb3419ec-2654-35b5-a070-224e5b330c59 | -9.2224 | -65.5756 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46f9f3b9-5353-312c-b8d4-95fdb0963f23 | -8.6028 | -67.190201 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e29e15c-3d0a-32df-8c6c-d31b3aef0e70 | -9.0384 | -65.404999 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2cddb2-1cf1-30f5-a4de-a6299e8de090 | -8.6344 | -66.515297 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa465f89-9d8c-3836-add4-97b334d9b926 | -13.337 | -61.643902 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4146c0e-5b79-3dfc-8a8a-05b04bed5f30 | -8.9822 | -65.384804 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39e99916-0739-3706-a2fd-ae6c42905253 | -8.9336 | -66.831902 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94dcd27e-d8a9-3309-9001-e5ebad746116 | -8.8295 | -62.473 | 2026-09-11 01:25:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbe6b71-665e-30a6-b6ff-0eab77b96bb9 | -9.5 | -66.783997 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 134a81b8-0d0a-370a-a555-9856b2b18bbb | -9.2322 | -65.573303 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7dfffdf-93f9-38c5-8ab2-1f2a05ea07cc | -8.5351 | -66.983101 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98028501-37ac-3088-890e-518ae76bfb4c | -12.1569 | -64.129601 | 2026-09-11 01:25:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9ed596-e0fb-3ec6-9e88-618f993a5d84 | -9.3488 | -65.675697 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7866e033-12dc-33a2-9c99-ee32c9336a67 | -13.33 | -61.657501 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa2fc28a-e73d-3b1a-875b-e3b258861f8f | -9.1817 | -68.203499 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a25f7e1-0cbf-3b2a-b4d6-cc3aa6377128 | -9.0305 | -65.4151 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7344613a-7b21-38c3-9d70-340587d7e7a4 | -9.4944 | -68.4972 | 2026-09-11 01:25:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cd29e109-55a9-3696-813c-34fa8e81e679 | -9.0878 | -65.484299 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d749cb9-8dd6-3c69-be0f-b9bb8b08b33e | -9.0781 | -65.486603 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4330f67-4696-3380-a9a2-71a14735b0fe | -9.1387 | -67.8284 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb5fbb9b-e9a7-3ddb-a9b8-6f72e3803d5a | -9.4219 | -65.858299 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8aae612-f6df-3a39-87c8-665a89ad29dc | -9.0403 | -65.412804 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3adcac5a-803c-3ef2-ba5a-c5631b77abff | -13.3565 | -61.136101 | 2026-09-11 01:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| baf9e49e-ce97-359e-8c04-b304ef46d038 | -9.2242 | -65.583298 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac26ef4b-956c-3f9f-a3f6-eb3b051edee6 | -13.3327 | -61.668598 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc333e2c-25a7-3f2c-a4bc-a36c598ea2df | -9.2305 | -65.565598 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f425ab7-8adc-3ca5-92a8-98be7a1a7522 | -8.6583 | -69.785103 | 2026-09-11 01:25:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b0985eb0-47d3-3b8d-a12e-231b9f857d35 | -9.1563 | -64.407898 | 2026-09-11 01:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 990beb52-ff73-353e-9f9a-35f4e8b09afa | -8.6327 | -66.508102 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7b4d2a-ffca-3b09-8411-f7f718b183e5 | -12.1588 | -64.138 | 2026-09-11 01:25:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c91a7bc-80c3-3382-b8f2-820a315357c3 | -10.2898 | -67.267403 | 2026-09-11 01:25:00 | METOP-B | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 83600315-22eb-3249-ab4f-ba18e41ea4f2 | -13.3035 | -61.676102 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5223b764-3030-32c1-bfc3-61f125890d64 | -9.4401 | -68.254204 | 2026-09-11 01:25:00 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 912d928a-5a61-3862-81ea-98335790f403 | -13.3439 | -61.126701 | 2026-09-11 01:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4f04f89-6fdc-351e-bd17-b753d1ff29f2 | -9.4104 | -65.853104 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb82148-fbe6-333a-b37e-90847ce3d242 | -9.0664 | -65.481102 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df41856a-b6ec-3ed8-a7c8-c9b3884ca668 | -13.3398 | -61.654999 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49e2dd9b-b1ac-367f-8043-f044dca5fd09 | -8.9353 | -66.838997 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6be850df-959f-3ea3-a43c-779bad25fe82 | -7.7548 | -66.906898 | 2026-09-11 01:25:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7527bf48-fb9e-3b3c-b1e2-471677838c0d | -13.3468 | -61.138599 | 2026-09-11 01:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6c244f-ab1f-3377-a501-7fdacf612587 | -13.3272 | -61.646301 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4d78b09-ab49-3705-9ac0-af11fe21daaf | -13.2121 | -61.6404 | 2026-09-11 01:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ca8c581-8064-345d-818a-b69e9fc97672 | -9.0286 | -65.407303 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab90b2a5-9354-3d3b-97a5-ed57def25651 | -9.19 | -68.194298 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87dc3070-e4d3-3adb-a119-874bcd02ac4b | -9.0188 | -65.4095 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1862b7f2-3530-3e96-9288-dc1cb57043ee | -7.3997 | -64.571297 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efc4892e-85da-34df-90b5-a498333b3f92 | -9.1422 | -67.7985 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b29fe932-df10-3d68-91ff-b3c193d8be21 | -8.6485 | -69.7873 | 2026-09-11 01:25:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8696a7ca-70e7-361d-8675-aa6d10f77b9c | -13.3008 | -61.665001 | 2026-09-11 01:25:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80340b3d-ec08-3f03-bee2-c46e9f8dc5ad | -9.4058 | -65.877899 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6d479a-1592-3eaa-a4af-95060a98eeca | -8.6425 | -66.505798 | 2026-09-11 01:25:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6b3415-7a7c-36d0-ad07-acb0064dc463 | -9.1075 | -67.690102 | 2026-09-11 01:25:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4be99fc-6494-32a0-ba82-f1c012e96e8e | -9.4928 | -68.490196 | 2026-09-11 01:25:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 57a1dae5-2e38-3cf1-82e8-3629cac26b76 | -9.0866 | -61.0287 | 2026-09-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ec476279-4bbf-3747-81f9-1627018ff908 | -13.3433 | -61.6696 | 2026-09-11 01:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 157.0 |
| ff671c1a-b766-3ca2-962e-831d30708a1f | -13.2488 | -61.6177 | 2026-09-11 01:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e8dce02e-c715-3a75-9cc7-9484672a9253 | -9.5913 | -40.3448 | 2026-09-11 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 7e683348-4297-3037-94b9-f7f62fef5c9d | -10.7959 | -45.9575 | 2026-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |


[Clique aqui para ver as próximas entradas](README5.md)
