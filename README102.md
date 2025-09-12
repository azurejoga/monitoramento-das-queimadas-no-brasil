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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27292a2b-5a02-3c0b-b33c-c2dc98d05f32 | -11.31874 | -50.78434 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afc266ab-5da6-3af2-b0eb-abcc90cf7d5a | -9.35264 | -65.45265 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2bd3528-31cc-392f-b339-ae8b3b6f69f2 | -10.19919 | -57.98492 | 2025-09-12 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 985f536e-4ae4-3e7c-a8d3-4eab856ef602 | -11.52745 | -50.59762 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc352699-a25b-3c92-bcbf-39bcc9395b93 | -6.67592 | -55.07438 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe89d7a4-a717-3f88-8d9c-3c26c82a53e4 | -10.43205 | -50.62499 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1197d966-64a4-36a4-9734-39b077b7b164 | -11.70121 | -50.60104 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc117b86-2d45-3e15-a961-67744cc43bda | -10.52071 | -51.52579 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41f9dc3d-1eff-30b1-b4b0-3b02a57e7dc3 | -9.03608 | -47.11037 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 77efc0b3-ad5e-34c5-b0f8-62ae97b1aef4 | -9.12026 | -65.48904 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b594e9-2365-3fd7-9adc-3107f571a3e4 | -9.04843 | -47.04519 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 02865d25-7a0d-3f46-a286-915dcf7030cb | -11.81089 | -50.57331 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50a3aa20-d54a-35e3-973e-5eb4a5e8d5d8 | -11.87716 | -58.82646 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8501bebc-81ba-336c-84f7-77181db2d87e | -11.96386 | -51.17555 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 79031f64-7d2f-35d8-a23c-35f3f633e471 | -11.87657 | -58.80763 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7763f615-edb5-3448-b171-a69d5a039ed8 | -11.94435 | -51.16874 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4087a087-2585-3224-a77a-0674e6339e3c | -9.95996 | -51.68447 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56d75a20-1c47-3716-bdd0-38e3e1ec5a11 | -10.68253 | -48.665 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9df19291-4e4b-31e1-97c1-982db63d9a9a | -10.09138 | -50.39663 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14c22119-8e4d-3ad3-a60f-17a678708ec2 | -7.40842 | -50.64318 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6ad3bbf-d78b-3571-9a14-2694f87035aa | -10.53099 | -57.08551 | 2025-09-12 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21bb7fcb-5e68-3b11-8ab2-cdd4df75f325 | -9.72373 | -64.94843 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c6d39d1-53ea-36e0-9bfb-45930e6e3e01 | -11.53858 | -50.41207 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2839a41e-a50d-3ef1-ab2f-1d0ecc65bffd | -9.04949 | -47.05705 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4392e0c-b136-306f-b72c-a6be556681d7 | -11.97773 | -51.15 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a92cab8-7ff6-314c-81e7-8caaa8ae4517 | -9.49113 | -55.97275 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bbe49a35-3731-33f1-9012-7fdf1dfcf6f3 | -7.78716 | -50.78086 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1650cdee-f6cc-3d3b-92d8-f3a44f3b9cd1 | -9.90838 | -57.06504 | 2025-09-12 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 904fc256-958f-3567-9040-5a9bfbd44d87 | -11.17769 | -55.05791 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 923dbe0f-b6f9-329d-bafe-c1522fac4eac | -12.90147 | -47.96567 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34ab5178-8e92-3770-a4f3-11ec8e3b04ba | -12.08463 | -47.59858 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9e9d48f6-80e0-3ceb-b666-b4f29b37b7a1 | -8.81204 | -64.07669 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7903ec41-e2a5-312e-95ab-8e220e2d8374 | -11.19585 | -55.07532 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31571570-2239-3bd4-b6f7-9423d4815ecf | -12.47145 | -53.83022 | 2025-09-12 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce08dc89-aaaf-3086-99fc-66e4798611e7 | -10.70515 | -48.6321 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba5f7438-62b3-3713-beac-741817739e33 | -9.07222 | -46.9586 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35317c5d-ea5b-3743-b9d7-8898997527bf | -11.97282 | -51.14585 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50713513-3994-32ab-941d-2843a11c3bae | -9.96777 | -51.70284 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ae7c4b2-353c-36f6-bcc8-db973f863343 | -9.68245 | -47.54829 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4fc3391c-7c87-3188-9e84-aff198bc4e0f | -8.89764 | -49.9324 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1465fb1-c218-3f26-b0c9-88fd4d76e623 | -11.53798 | -50.60275 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e23cfe4-a81d-36f6-9a9b-841f89b6bf77 | -11.31771 | -50.34093 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c46a222-0e83-301e-88ae-c43a1e1c0e49 | -10.52977 | -49.87164 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e02c98-0c1b-3804-907a-c9f071657a4c | -10.42175 | -60.47158 | 2025-09-12 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 943d0eb8-190a-3962-940f-7e970916c9e2 | -12.8264 | -52.96184 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1104abe4-f311-373e-952f-c73094ddf1fb | -9.95888 | -51.69297 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9ac9a4f-d219-302a-a248-ed9a28b966ef | -11.19182 | -55.07475 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ca1aa3-3ee9-364b-98ec-44669e5225c0 | -7.76789 | -61.3674 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca622be-fd4f-366d-8767-9637d4adb8a9 | -6.80928 | -52.80677 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00319aff-4d47-3a12-800f-cbb908a9a881 | -9.33526 | -65.45362 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa5847be-a7dc-3a1f-935a-793f226b2b9e | -10.67102 | -48.6056 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2c3eec2-252a-3d08-ab23-6064dbeffd85 | -9.33459 | -65.4575 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c0e6f4c-8ef3-357e-8c86-d6856967ac08 | -11.97855 | -51.14322 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ff512be-690d-3d1d-b1c1-3dae6bff99af | -9.91194 | -51.62074 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a6390b-f56a-30dd-877d-346bf3769a84 | -9.48918 | -55.98643 | 2025-09-12 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb205442-6f95-3f8f-b276-97cb291e3cf8 | -11.53481 | -50.39635 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e0a668d1-e500-3dda-ac7d-6575070f2f62 | -11.53842 | -50.59911 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b95fae5-6650-3dde-a0ff-80784c88ae93 | -11.50124 | -55.49663 | 2025-09-12 05:18:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1774ee14-09bd-3a18-aac4-fbd3842f6a80 | -9.83737 | -54.53503 | 2025-09-12 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c27d81b-b2b0-36e7-b0c2-d5224add6ff7 | -7.35948 | -59.82102 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e64132c3-b744-35fc-b2b7-7415e96afc41 | -10.52927 | -49.87555 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a2daeec-d01a-327d-abd8-742af650e4d4 | -7.23154 | -55.06314 | 2025-09-12 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86332c93-6747-38c9-98e8-175baf08b7df | -7.48739 | -61.40767 | 2025-09-12 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 073c14c2-1de5-3527-a74d-e4344a82ca71 | -9.72713 | -64.9527 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18056760-55bf-383a-9a83-241ff9907a95 | -9.71352 | -64.9357 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19fecdb6-e146-3316-9a63-ea1f3c89169a | -12.46966 | -53.83164 | 2025-09-12 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17786e22-8a73-3975-8ee6-40f752f5d642 | -9.04888 | -47.06194 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0eb6771-a9e1-383f-8d9c-d634ee55dca2 | -11.31681 | -50.34251 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f76ef41-d719-3583-830d-9bcfeb3e6996 | -8.88009 | -49.9374 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7321da47-5e51-30ae-bf0e-0d367c315ae2 | -9.78999 | -57.44473 | 2025-09-12 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f302ae-e045-34e4-a257-cd6a76d4dfc5 | -10.42155 | -60.79564 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2616d9d8-df95-389a-9ae9-86c0bdb23b03 | -10.08639 | -50.39229 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 265b9bbc-5490-3aae-99a9-459fee32616b | -11.18933 | -55.09253 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b74b01c7-5eed-380a-ab5b-30c85d1fb832 | -11.54458 | -50.40909 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a1e8fffc-c2da-3ab3-913a-5f01057ece79 | -11.87882 | -58.81553 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06818fb1-0dd8-3cf0-a71a-d409bdc4b930 | -10.68988 | -48.65561 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d740cc3-42f8-34bb-b575-3dc26504e0d7 | -12.93573 | -48.00634 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 660fb745-b4f5-3af5-9f28-02949bc45204 | -10.52991 | -51.50626 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0c20a90-fabb-3192-8f92-cf22162552b8 | -11.86926 | -58.81032 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62a3be8f-64b8-3e4e-a30f-13d8255bb99a | -12.93722 | -48.00474 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 254c1a34-cc72-3a9c-90c7-8110cebef97f | -7.72937 | -50.74242 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b254674-bcad-3482-912b-c671cc540d17 | -10.55513 | -51.53991 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 41b1b0d8-b1e7-3b87-b56b-91247ebfcc10 | -9.07305 | -46.95154 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6b00fb4-3613-395a-8314-e246e21992f1 | -9.03303 | -47.08077 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d0aaf969-7083-3e9f-953b-46afa0c6ffa4 | -10.85862 | -56.36459 | 2025-09-12 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f46653dc-0777-3d5b-8404-865931c030cb | -9.02945 | -47.10962 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab8e8223-6440-3b24-b01e-2191e3cf62af | -9.07984 | -46.95153 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 930c2160-c5de-3ebf-bad0-49dd766dab9a | -8.64743 | -55.24491 | 2025-09-12 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adce05fd-5d79-3d66-b9d6-8884fd7bd304 | -10.40124 | -50.0273 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26bf7774-c8c4-3be8-b64f-2c4dc4310ecd | -6.4032 | -58.21152 | 2025-09-12 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69bed15-7a8b-3594-ac3f-38538b28959a | -8.48616 | -47.2746 | 2025-09-12 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 48c7bf6d-4df7-3909-8288-c9b93ed537fe | -11.19436 | -55.08601 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce527b2-83d9-31f4-9114-50294210ae46 | -11.02822 | -51.51581 | 2025-09-12 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b323c82-bf35-31da-a78f-68aae572c19c | -7.35617 | -59.8205 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a68b983-d198-33ea-a2c1-ea5e683863fd | -9.04418 | -47.04546 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 76af5ad5-9195-36e6-a9d4-e4e2fc16da63 | -11.10417 | -51.95879 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 25abf7b8-fd5d-3d29-8067-5aeb53204c03 | -8.08217 | -50.18249 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ebaa604-6184-3c58-adb8-691412306353 | -9.14016 | -58.91862 | 2025-09-12 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85b427dd-a65d-351f-92e2-6f3bf0ecbc54 | -6.95299 | -62.93273 | 2025-09-12 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f9f4634-ec43-3dde-af76-86611e8343ac | -8.0863 | -50.1925 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README103.md)
