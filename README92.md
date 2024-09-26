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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2252a750-831b-3da5-bead-82e9e570792c | -9.33942 | -51.07663 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 722edd5f-57b6-3b21-bf56-e13252a4f152 | -9.33795 | -51.07493 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 307df08f-7c63-335c-aefc-65cfb15fc824 | -9.33731 | -51.07942 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6f01845-d49f-3bad-90fa-0fc5f433f40e | -9.33571 | -51.07607 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 851930d4-7202-3394-ae39-fe43a421e86e | -9.33504 | -51.08052 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 56c147db-a71e-31e8-bb92-8036ff87339c | -9.3336 | -51.07883 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f5a9cbb-0c3f-3c08-affe-8d7cdfb20494 | -9.33297 | -51.08323 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffde803d-f9b4-34a6-83a9-fa00c77972ad | -9.33214 | -50.73499 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 973a3418-8851-3ac0-b211-036f5a4e10db | -9.33142 | -50.74 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39727165-c8f2-3604-9a83-25b426b93296 | -9.3307 | -50.74504 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c7031a6-956b-3793-8b44-a17ea6beefd6 | -9.33003 | -50.74963 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2fa6a992-e883-3246-b3f4-c60ac43c0e2c | -9.32833 | -50.73465 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c433a61-abcf-3044-be3e-83838cd0b7f6 | -9.32596 | -50.72421 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c737a03f-7790-36d9-b2a8-db56e190cfb7 | -9.32556 | -50.75385 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08767718-7857-3d3f-9f71-1eee8a0098c0 | -9.32525 | -50.72916 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1f762bb-6993-3911-885a-bb1a7e541d84 | -9.32493 | -50.75813 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d83c0e0f-9b01-34c5-99a8-8ba65f6a4193 | -9.32453 | -50.73414 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 298aef77-d2cd-35d5-9187-097303221806 | -9.32216 | -50.7237 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 875d75e7-6bd0-37ad-82de-67b518e905fd | -9.32145 | -50.72867 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e400618-37ab-38d6-bfa8-e767ff2f00b5 | -9.32111 | -50.7579 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d013d66e-e447-39f8-ae13-4e76069139a6 | -9.3205 | -50.76206 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 60393243-9f86-3bdb-9e8f-e03282ac448d | -9.31601 | -51.13213 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c65841ec-c63f-359b-a552-41cbccf1496b | -9.31409 | -50.93846 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d5891a4-1ea2-3d4c-a153-25f7e33db0a8 | -9.31285 | -50.76162 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5e6a281-b8b9-35da-8744-4c15d37c472a | -9.31231 | -51.13154 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654188ad-7e66-3f06-9810-6f1daa3689b0 | -9.31101 | -50.93338 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99abef07-473b-3636-90fc-663551726aad | -9.31035 | -50.93793 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4285f48-ba22-3ec2-8757-86bbfc7a9138 | -9.30908 | -51.07652 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7137370c-7d2b-393a-85d0-349ad2b12683 | -9.30908 | -50.76103 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86a86e50-8a16-3508-9f15-46554b1de333 | -9.30903 | -50.94698 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 869d29a8-d888-3841-bd16-5060427e69ac | -9.3066 | -50.9374 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4176aa64-d187-3e38-91dd-3ad7c9394801 | -9.30531 | -50.76035 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 90bcecff-9f1c-327b-8730-4ca9c3ff50e8 | -9.30466 | -50.76487 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 91117437-09bb-3f4a-8de4-a315d43811ea | -9.30154 | -50.7597 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e8f748a1-b57a-3c89-9669-d429d8f84dd8 | -9.30089 | -50.76427 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f73bd88a-557c-3805-8a2a-1e06262b5298 | -9.29556 | -51.14256 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d92fbad9-6c68-3c95-b911-ca395d79c738 | -9.29052 | -51.07371 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d44f24c-c347-3d5d-90af-f99018420ab9 | -9.28681 | -51.07315 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdfab7d5-fb98-3a57-9eef-a867c3a872af | -9.27372 | -51.08496 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f7d1a19-fd6c-34d8-a372-e958a1972a0f | -9.13742 | -51.52747 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14553a41-6386-327a-8abb-6f3c2797e534 | -9.13679 | -51.53171 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbea2994-e7b9-3473-a864-7082d5866366 | -9.13381 | -51.5269 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6456288d-e45b-3b6d-b4da-6c041ee6904c | -9.13317 | -51.53114 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9268e3da-6713-357c-98f5-a3c235b3e128 | -9.13019 | -51.52634 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75883e82-149f-38e7-b8b4-8a74afcd62e1 | -9.12956 | -51.53058 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5917718c-2d78-3d02-94e4-bdb461343014 | -8.93114 | -50.67109 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95e1b29e-d81e-30e2-8520-eba8869a07a0 | -8.93086 | -50.69928 | 2024-09-26 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d343ae9b-9494-37cb-9645-98640b2f004d | -8.93048 | -50.67558 | 2024-09-26 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8778adb5-0a12-3935-8e5d-002576311a63 | -8.69707 | -51.01036 | 2024-09-26 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76ee5de0-4e1f-371f-955c-aa1e4a1ec008 | -8.6949 | -51.00758 | 2024-09-26 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fbbb888-6ebe-305c-b948-0bf63e561921 | -8.60683 | -51.44636 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8435d45e-3c05-3042-9144-92663ce1ccc6 | -8.60322 | -51.4458 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 552bb8a7-7507-389c-be3c-7175af7085b5 | -8.6026 | -51.44999 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5b8e7a0f-4804-3dca-bd87-6c5d0cf9fe9c | -8.60197 | -51.45417 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9b12a46-0294-3b71-822a-9a1c12e2a658 | -8.599 | -51.44942 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb244a30-7bb4-327e-a707-183d6e14e23e | -8.59837 | -51.45361 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ec9e391-ac8e-39a2-9dcb-0bd7dee73444 | -8.59664 | -51.44045 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74bdbd18-03ba-341a-8e77-79198392cd00 | -8.59303 | -51.43991 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cc62c5e-e3e6-386f-ac15-b8e367700c00 | -8.59241 | -51.44409 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f17b0c0d-3d0c-3911-b28e-0bc9daaf8d3c | -8.59116 | -51.45247 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ad7603d-6f0e-34b9-a5e0-f44f7ab892b1 | -8.5888 | -51.44354 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19f6489d-1760-33a4-a67f-a4cd861a0feb | -8.58159 | -51.44246 | 2024-09-26 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7bce3e5-aa16-3988-837e-a4d113b1a72b | -9.70929 | -51.35551 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51ea06db-8bc3-3bcf-bbf5-ab4aac479aa2 | -9.44962 | -51.51801 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e3bfb04-5dd4-31ff-a4f8-f548efae6af3 | -9.449 | -51.52225 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b554fd-483f-3a03-9c80-f8b4d28cbd4c | -9.44837 | -51.52648 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67ff6e6-a7c8-30fe-9c5a-87a17f305042 | -9.44663 | -51.51319 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45c42925-2dcc-32cb-b8b4-f75e771b3a85 | -9.44538 | -51.52166 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c2dda85-0de0-3836-ab91-e1a9632737d4 | -9.44425 | -51.50413 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04730315-8ce7-3005-966c-bb94fb11a1c6 | -9.44361 | -51.50843 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbb5bcc-834d-3baa-a5c6-1f19390884f7 | -9.44298 | -51.51273 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5322c5f-9bf1-34ea-af90-84077eb429aa | -9.43997 | -51.50796 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e113510-e19c-3eab-8209-9e1094f92a15 | -9.43709 | -51.477 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 612a029b-7a12-3d4a-8e46-5e6567056aad | -9.43646 | -51.4813 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe66ee3-e7c2-3fce-b5a9-89fe259741de | -9.43633 | -51.50746 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1252966-f35e-35a0-b7d1-b517d17b5aee | -9.43583 | -51.48558 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c229283-47d2-3102-bf87-2f7b9ed1b091 | -9.4357 | -51.5118 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fd20f51-3fdc-354b-84bd-add63456559a | -9.43345 | -51.47646 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ffca024-a46e-3e75-81f6-812ed532ff62 | -9.43282 | -51.48077 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88722f6b-0983-3167-b674-ab425ec8dc00 | -9.43219 | -51.48509 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8e1bd87-4c7b-3fcf-b11b-8351f9092386 | -9.43207 | -51.51126 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f02b3b-3915-3ec6-87a4-58288ccd317e | -9.42843 | -51.51073 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a3949e-7f87-31aa-b58a-a94890b524ff | -9.42586 | -51.55353 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7365a7f-7d11-3074-9a21-ce86c8a4c8f9 | -9.42524 | -51.55776 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f7b36a4-d2b5-30a2-af46-c5a5c9785464 | -9.42491 | -51.48403 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7730ef5-2be0-334b-a6f2-013de43f83cb | -9.4248 | -51.5102 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e6c100-aa8b-37a1-881b-45e1f4ab9c97 | -9.42285 | -51.54884 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9acf19e1-baac-3071-8c98-517ccaca9b1c | -9.42128 | -51.48349 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 905a13c8-54ea-33d0-bb7f-46bf5be7b91d | -9.42099 | -51.56151 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 876f236d-7e8e-39a1-ba63-ffbda5153e71 | -9.41985 | -51.54404 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98745123-d119-370d-8411-61d81e4b3279 | -9.41825 | -51.47874 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 746efff6-d03e-3a56-bf17-29602afb2b98 | -9.41806 | -51.53093 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d713585-f44e-33cf-8597-73854ce004fa | -9.41764 | -51.48295 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c843c38-2bfa-365b-89d2-110af5e8b83c | -9.41677 | -51.56508 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20a573c0-d965-3bf2-833e-3b5d355acace | -9.41624 | -51.54337 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a437f332-4aa2-3e9b-85e8-af70d27cdd09 | -9.41444 | -51.53035 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa81313b-4cf2-3fab-a244-0490fa93f412 | -9.414 | -51.48242 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e339c6b-d5c0-3759-9e8b-e75bf305c97a | -9.41385 | -51.53442 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e713042-0a33-3f96-94ab-419a0ca67a47 | -9.41327 | -51.51297 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b19faac-bf96-3486-9dd5-60567cb79ee7 | -9.41284 | -51.46483 | 2024-09-26 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README93.md)
