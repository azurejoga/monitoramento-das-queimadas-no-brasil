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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2a25833-e1d8-33d3-ac9e-83fd624b2af0 | -10.79422 | -50.11552 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85d47390-cf9b-357d-92f5-700456f016b0 | -10.78972 | -50.11849 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d041ca8-f7b9-3e6d-b6e9-77ea9b4a61fe | -15.0274 | -51.35304 | 2024-09-26 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93a8d4ad-9a33-33c9-8b09-a97911279bd2 | -10.78923 | -50.12204 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5a5b0fc-628f-31cb-aca8-62be898b7762 | -10.76243 | -49.86378 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c969d40-7650-32c9-a77e-877671e2ca0d | -10.64766 | -49.91134 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd2a12c-4ef7-3207-a512-31b4e510c063 | -10.64462 | -49.90348 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 611d9b02-c1e6-3fc5-a460-7b414b38c95c | -10.64411 | -49.90711 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1befda85-e18f-3b86-b9a0-95f5f9422961 | -10.6436 | -49.91075 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5ab3cf0-3536-3ec9-9f12-23542cc9045e | -10.64056 | -49.90287 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 334bb10d-6eb5-373c-ab7a-b1d24c72f8b9 | -10.64005 | -49.90651 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 080a2018-6470-338c-a27d-da8db72d9395 | -10.63954 | -49.91015 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6dad025-b5dd-3017-a1ce-31f98aa1d89d | -10.51213 | -49.78019 | 2024-09-26 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea90510d-2402-3e2f-a534-7dc7bb60f488 | -12.18122 | -50.14764 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8cf9655-3995-3936-a568-7ed7624eedbc | -12.18073 | -50.15135 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc00dbf4-6048-359b-8f0d-e1d03fe1feca | -12.18023 | -50.15505 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa51d9d7-624e-3f94-b69e-58ce5aa67d9f | -11.85463 | -49.61699 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7defe0d-3886-3326-8f5b-8061e396acf6 | -11.8541 | -49.62094 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9283ba96-f424-3d64-b321-111a65c25f5d | -11.85357 | -49.62489 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bd33d716-f4d8-316a-83c6-066ee4861ae9 | -11.85038 | -49.64857 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e2fbf801-b786-3d88-b70e-1d72e042ca5e | -11.84989 | -49.62033 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5921458-04fd-396d-85f8-b9e899e01f86 | -11.84984 | -49.65252 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b80741f-524c-3efc-b696-f7a5d5f615ba | -11.84936 | -49.62428 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06cfddba-7454-35ca-99ea-37791a432215 | -11.84931 | -49.65645 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c1ef654-79af-3b9b-9a06-faff5b2ae5ac | -11.84882 | -49.62823 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00d4e066-8c52-3d6a-ab98-7814b4651a1f | -11.84879 | -49.66038 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9da1192b-56a6-3c46-b28d-eecbc235a036 | -11.8483 | -49.63218 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c5326e1e-945f-3fb3-881f-afd4ca2c3a54 | -11.84826 | -49.6643 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d4d7036-d075-343e-aa34-e9d024e3fdde | -11.84776 | -49.63613 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 38925faf-ed90-33fb-9eb3-d8304d14f490 | -15.02417 | -51.3473 | 2024-09-26 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f3b7e3e-41c1-38f3-a026-b3d96c0bf768 | -11.84723 | -49.64008 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cdf3f13e-5dd0-304b-97dc-7958d0236e1f | -11.84564 | -49.6519 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166815cc-e238-3f59-8a41-66951f3d123e | -11.74294 | -49.89334 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 958a0693-3caf-3d18-b7fa-526eb7f94c3e | -11.73881 | -49.89276 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a8631e-72d8-3936-ba74-1ff9d711e1c0 | -11.73829 | -49.89655 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57335c0f-2daa-301d-a8f3-705c646069d5 | -11.73468 | -49.89214 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5c1cdd2-7d58-370d-b90d-4afbe305b7a1 | -11.73416 | -49.89594 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0865442-07fb-338f-96a9-7bfd1d4f1267 | -11.72281 | -49.91734 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eee1b49-723b-3ade-a586-2ffb30bda53e | -11.65374 | -49.99978 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f1d41d-0f52-3af7-918d-6530805b1e67 | -11.65314 | -49.99877 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20243aac-ac04-3619-a9bb-72f610b6c1ac | -11.60136 | -49.67438 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9740fee6-6226-3c16-9831-563d7ccb1fdb | -11.60084 | -49.67827 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97adc7e1-da9e-39d8-b7c6-6bd947e8f330 | -11.59718 | -49.67377 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 793c3d18-4687-3474-8257-798a4c58b5f1 | -11.59404 | -49.66537 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d255da6d-b283-3983-8c4f-700e2483908b | -11.59243 | -49.66674 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e6d0b3d-202b-38d6-9212-76aa4bf50d52 | -11.22 | -50.2809 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65abf847-f48a-357c-b843-e29539009ed7 | -11.17401 | -50.21697 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49cf8580-9257-3570-8aea-5b54d139e411 | -11.15533 | -49.73224 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1cc0d49-b9c9-3dde-a5fb-6e6d756dad90 | -11.15423 | -49.72774 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d42f52c6-c4e0-345c-8907-017d13940399 | -11.15372 | -49.73153 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd411362-5b74-3830-a5be-6b6ac4340931 | -11.15172 | -49.72787 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f24197c-5dc8-3faf-b94b-ff9a3a2bc066 | -11.15119 | -49.73164 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0884d8c9-4976-3294-95b6-41475a48c668 | -11.15009 | -49.72715 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb23bb50-fbdf-34cc-a2ab-08cf41db263f | -11.14958 | -49.73094 | 2024-09-26 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6be280a-da34-3283-9351-c887b79b4ef4 | -11.02744 | -49.63314 | 2024-09-26 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c384ca8-84aa-3b79-8e23-9dda3554b619 | -11.02329 | -49.63255 | 2024-09-26 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56eb1a30-6f64-3873-b08b-509b88c15e7a | -11.01913 | -49.63195 | 2024-09-26 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97ac5007-e225-33d7-b893-85e188f0053b | -11.01544 | -50.19726 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a747895-1f56-390a-bab7-3dc662df4b71 | -11.01535 | -50.16832 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e517fc-a739-3639-a879-862bd9c29f4c | -11.01486 | -50.17187 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 730ce16e-565c-38a1-9622-7a2130753b69 | -11.01035 | -50.17483 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cae7a3eb-1181-3c91-bc90-fea193a279e9 | -11.00938 | -50.18192 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab665cbb-5a6d-383e-a3d8-ac27dd2bcca3 | -11.00537 | -50.18132 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 600fe94a-efc9-3215-bea3-46153204f5b7 | -11.00136 | -50.18073 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 080f8833-70c0-32bc-b191-37cb71290715 | -10.99735 | -50.18015 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce86bf7-505b-3b63-9908-7a7aa9b96790 | -10.99043 | -50.20078 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e393ed85-93e2-3145-9701-b33d53f2c4ad | -10.9385 | -50.15044 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdc5c61e-8281-36c8-996e-d944530cc77e | -10.938 | -50.15398 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbd95f88-99af-3b2d-b4f6-47e075e7fbad | -10.93403 | -50.18229 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85b68684-92c9-33a3-9cd8-067ff509fe8b | -10.93354 | -50.18582 | 2024-09-26 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1960637d-a9a3-3cde-96d6-b143e9f04175 | -12.21681 | -50.71452 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 326fc72f-eea4-3004-a6f4-a6eef5c77058 | -12.19829 | -50.82108 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a00945bb-99ee-304b-ab60-4baffdef2c21 | -12.49494 | -50.43724 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899bf998-5c3a-3fce-b1c9-7360024326ae | -12.49287 | -50.42225 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 845f5dda-1766-35a1-8ad4-67dae97b2f59 | -12.49238 | -50.42585 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eddadb8-bc11-3963-84d6-91d9da4597a3 | -12.49189 | -50.42945 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1843718-d039-340c-9d40-b513ef29de2f | -12.4914 | -50.43306 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1550ffee-e23c-3461-a82d-22f0d74014a8 | -12.4903 | -50.41086 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a147ce-6558-3c3c-8bc4-a44a20e56302 | -12.48932 | -50.41806 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be5fddee-e5d7-30b5-b782-9dad2d901c02 | -12.33439 | -50.50902 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c04b9ab2-db6d-305d-926c-4ab0cc9615fb | -12.32989 | -50.51197 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1632ac3-dfae-3cc2-8e19-01f0abe2dbbf | -12.30941 | -50.51258 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c775b633-f94b-370c-aa3a-26937991079e | -12.29693 | -50.51435 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49defe1f-b03b-376c-8208-c842622005bd | -12.29595 | -50.5214 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cc33761-f61d-346b-97dd-e7b3db4d8107 | -12.29245 | -50.51729 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef0ee139-19ba-3cd9-bfa9-eae629d8b7de | -15.02701 | -51.35403 | 2024-09-26 04:59:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d76a6f6-5a1f-3c94-af2e-b9fbb22093f7 | -12.29196 | -50.52081 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0be74c1a-f021-3e01-94c5-eeef8987518f | -12.28797 | -50.52023 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b99c068c-b50d-3339-8817-b8a514b85303 | -12.28651 | -50.53079 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd2976ec-24a3-32ce-a8e6-b114497bf23d | -12.28602 | -50.53432 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3995679d-31f4-3d64-87ed-bcde392b9882 | -12.27164 | -50.63825 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa7e504d-8fa5-3f12-aacf-861bad1d8f99 | -12.26768 | -50.63766 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab1264a7-7906-3564-bc8d-a8a0c1a8ea8d | -12.25293 | -50.65668 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 410b29a7-4f21-3b43-9c16-0598467eb6ac | -12.2149 | -50.78729 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74960418-6c27-351e-988f-53660f8609d1 | -12.2142 | -50.79238 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 542701f2-76df-3b10-a990-5aa37998857f | -12.21097 | -50.78671 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91a80b4d-71c5-395f-9e1c-067b7d61bd07 | -12.20958 | -50.79688 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2a9755d-c660-3eef-ad48-52ad62ed3995 | -12.20726 | -50.84305 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad369042-4eaf-348d-b03a-e1e8dd72f2c0 | -12.20681 | -50.81718 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efa1ba61-60b8-3ca4-b5cf-810144d1d562 | -12.20289 | -50.8166 | 2024-09-26 04:59:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README116.md)
