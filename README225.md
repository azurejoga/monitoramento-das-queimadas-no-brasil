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

## Dados Diários - Página 225

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e7760a-d730-3e93-9a53-f6cb314548eb | -10.01025 | -68.4443 | 2024-10-09 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d22d5841-6c3f-3528-b9d1-3abe6167b2eb | -10.8755 | -63.8979 | 2024-10-09 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dd2fa52d-b8e4-37f0-a818-1601356ff8fd | -10.8754 | -63.9169 | 2024-10-09 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f6b8a1ea-9b3e-33d7-8102-89ebd6fe9aaa | -11.6806 | -64.0312 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 5eb1076a-dab1-3382-9e25-d3800533c8f1 | -11.6808 | -64.0121 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 43acc48b-7f6c-32fe-bad4-f7a1d0c7ecad | -11.6994 | -64.0302 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5aae8195-45ad-3f80-b285-d7a8aa00a1ec | -11.7117 | -65.0155 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 27db4624-041c-375e-a40f-f22814b2d34a | -11.7119 | -64.9966 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d9d1ac25-5a89-3c1b-ae87-9df02b52d494 | -11.6619 | -64.0321 | 2024-10-09 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0bc10183-d07c-3557-9ec6-5df982ef57cb | -13.417 | -61.9169 | 2024-10-09 06:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6af51005-7d4d-38be-9dff-81c27af3365f | -13.398 | -61.9182 | 2024-10-09 06:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ba29686b-b44c-3402-b172-2fdc1a220717 | -13.3978 | -61.9376 | 2024-10-09 06:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 19a8b2ca-5c80-3aad-a939-6051e2c6476a | -18.5993 | -57.2629 | 2024-10-09 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 1aea1df2-d589-3e23-ae53-a436fd9aab7e | -18.5996 | -57.2422 | 2024-10-09 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.0 |
| 8a12638a-31c8-3f92-a88d-9bb7e49ca8e5 | -18.6 | -57.2214 | 2024-10-09 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 5c0060b8-0ef0-398c-a1ee-1aebce2127c8 | -18.6195 | -57.2396 | 2024-10-09 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.8 |
| 51372bbb-7557-33f7-9cc8-1df85ad49bcb | -10.8754 | -63.9169 | 2024-10-09 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c202766f-7c7d-3469-8cfa-89371eb3f868 | -10.8755 | -63.8979 | 2024-10-09 06:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 539afff8-1905-3511-97fc-83e7fe18a324 | -11.5233 | -65.137 | 2024-10-09 06:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| dcef3adc-c66e-3697-8244-b90bf341e88a | -11.6619 | -64.0321 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c547c8bb-4f9d-3ac9-8f0c-9c180204713d | -11.6806 | -64.0312 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 109.5 |
| cf4f75b4-0c83-37c3-bbaa-b8ccdb4ed796 | -11.6808 | -64.0121 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bfeafb24-ae68-354f-a31d-c74aea977ddd | -11.6994 | -64.0302 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a5395844-eb55-307d-80ed-f1618edebb9c | -11.7117 | -65.0155 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 628cb2a6-177b-3b0e-b8a2-712943657d61 | -11.7119 | -64.9966 | 2024-10-09 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5ec7c3b9-f5e1-3e94-8692-3fa58f43e2e3 | -13.398 | -61.9182 | 2024-10-09 06:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 42eb4514-9e0b-3bd0-90b8-e982630f75f8 | -13.417 | -61.9169 | 2024-10-09 06:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4ddcd1af-04fd-3e06-b2b9-ba3dcbbb5204 | -13.3978 | -61.9376 | 2024-10-09 06:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 017b8e59-faf7-3f1d-b434-87ddfb4df7ab | -15.6877 | -59.4145 | 2024-10-09 06:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c7c35be7-f090-3100-b271-d5a534914d0d | -15.688 | -59.3945 | 2024-10-09 06:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 6d8d3b83-c6f6-31dd-a7f5-e45aa737ad67 | -16.9403 | -57.5063 | 2024-10-09 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.1 |
| ed6f87a1-4c46-33c9-9195-ae6b254de98a | -16.9599 | -57.5041 | 2024-10-09 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| c623152b-5b31-3926-9c43-e2b11f7d8a82 | -16.9799 | -57.4813 | 2024-10-09 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 265.1 |
| 964f50cb-eba7-308b-a992-88c82a1f5a20 | -16.9995 | -57.4791 | 2024-10-09 06:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 2de7b6f5-8f28-36ab-8679-70ada4e779a3 | -17.1188 | -57.3628 | 2024-10-09 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 13829e98-2f11-3f8d-a16d-5b7ea93810d9 | -17.1467 | -56.8463 | 2024-10-09 06:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 74f57ef4-332a-3ec6-a746-5c338519055d | -18.1193 | -56.3921 | 2024-10-09 06:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 9856d50b-1959-31f6-b8ac-44a19db91c0e | -18.5996 | -57.2422 | 2024-10-09 06:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| ee43b9fe-0c56-3c75-a435-4ac878500092 | -9.4435 | -67.1008 | 2024-10-09 06:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 105e9b9d-4ae3-3cb7-b6e0-4d70701691fc | -10.8754 | -63.9169 | 2024-10-09 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 43e720f9-7171-3d5f-ab37-a0468edeb285 | -10.8755 | -63.8979 | 2024-10-09 06:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1e5aa2b6-6453-389f-8396-e15126e77f81 | -11.5233 | -65.137 | 2024-10-09 06:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a8c16a36-f958-3aac-b1f8-0292d61dd0a4 | -11.6619 | -64.0321 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 305f50b9-5995-3385-ae3d-e2a6de5ae5f7 | -11.6806 | -64.0312 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 33646b59-211e-375d-b9c3-b3f4ac41a033 | -11.6808 | -64.0121 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 47480b9c-8e9b-3d02-8092-e5597a07f69a | -11.6994 | -64.0302 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 5ca74326-6032-30bd-ac33-7fdea2a7e22e | -11.7117 | -65.0155 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| fefa589c-3eb4-35c2-8d6c-e080941b52c7 | -11.7119 | -64.9966 | 2024-10-09 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a52421f7-e1e1-323a-b16f-97f844e586b7 | -13.3978 | -61.9376 | 2024-10-09 06:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 01a10c14-4663-36da-ba79-c0ba36eaaf7e | -13.398 | -61.9182 | 2024-10-09 06:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 46ca9dd5-3380-37f0-a453-ee87c5f49cc9 | -15.6877 | -59.4145 | 2024-10-09 06:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d1e254fd-2595-38b7-8133-bc3e491a6c32 | -15.688 | -59.3945 | 2024-10-09 06:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| eb86cc82-db23-3db7-a5e8-d4d6058db336 | -16.7067 | -57.4514 | 2024-10-09 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 0f32df0e-01ff-379c-bfd5-ff168acc6d48 | -16.8576 | -57.8014 | 2024-10-09 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 860c2d41-7eb8-3c96-a168-98587c347121 | -16.8898 | -55.8039 | 2024-10-09 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| a848f992-c534-3c0e-85ca-8910fda5c862 | -16.8901 | -55.7831 | 2024-10-09 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| e0211ce7-88e9-3754-9460-12bf1b53abac | -16.9091 | -55.8222 | 2024-10-09 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 314f8934-36f7-3ead-a9ca-f569e4b9f4a4 | -16.9094 | -55.8014 | 2024-10-09 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| 364cfdf1-e13e-3c96-b3f2-41014d8cfac6 | -16.9098 | -55.7806 | 2024-10-09 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| eed139aa-04da-3c4a-a729-a9572f1bde13 | -17.0623 | -56.0308 | 2024-10-09 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| d241725e-5e6f-3844-99ca-9f95a36617c6 | -17.0626 | -56.01 | 2024-10-09 06:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 388bdeff-1a5c-31ee-876f-24fc5d664181 | -17.0795 | -57.3674 | 2024-10-09 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| c132ba61-a0d3-3d33-8caa-0f4bb81c5afc | -17.0799 | -57.3469 | 2024-10-09 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 4b50af03-d464-3a15-b7b2-45f8b2fa039f | -17.1188 | -57.3628 | 2024-10-09 06:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| c4f33d31-57b5-36a9-b79f-3b0547501b91 | -18.1193 | -56.3921 | 2024-10-09 06:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| e045951b-4e36-3376-80d6-b5a4e1808ed3 | -9.4435 | -67.1008 | 2024-10-09 06:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d5f74b92-118f-3762-a4d8-650bb8b1d84f | -10.8754 | -63.9169 | 2024-10-09 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a99e26b7-e269-3689-a838-bc51afc8f8f1 | -10.8755 | -63.8979 | 2024-10-09 06:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 950bbea4-bb0b-339b-8612-0fe2a951dfc4 | -11.5233 | -65.137 | 2024-10-09 06:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 79a2dfdf-2ec8-3330-96f7-c80cda9a0983 | -11.6619 | -64.0321 | 2024-10-09 06:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b357967f-ea67-3107-b147-231d53a16ddc | -11.6806 | -64.0312 | 2024-10-09 06:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c5b7f711-cd5b-366f-8fc2-f2c5a88ad2d9 | -11.6808 | -64.0121 | 2024-10-09 06:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| df9d4a1a-d45f-3103-8c0c-3c22ed84219c | -12.878 | -62.8007 | 2024-10-09 06:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4b9acf39-1272-30ba-840f-b66d9cf315a3 | -13.3978 | -61.9376 | 2024-10-09 06:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9324b8d5-49cd-310a-8daf-151a17d6f00f | -13.398 | -61.9182 | 2024-10-09 06:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 3cffedc0-8a20-3168-aab0-c108a2265d4e | -13.417 | -61.9169 | 2024-10-09 06:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 099abcf4-4b6c-3cc8-bb43-22fd7b6ce627 | -16.8898 | -55.8039 | 2024-10-09 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 1cd2a497-a7e7-3976-a4ea-f769c7274db9 | -16.9094 | -55.8014 | 2024-10-09 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 0ec818a3-a765-3ea3-a4a9-1e234accbca9 | -16.9098 | -55.7806 | 2024-10-09 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 07e52e8f-1a1c-37fd-8591-e46ac1a9d37c | -17.0207 | -55.0371 | 2024-10-09 06:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4e4c8a3d-e5be-3f3f-8dd6-8e44973301c6 | -17.0426 | -56.0333 | 2024-10-09 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 291213e7-8f7e-3ff8-886f-01ed4f7f7269 | -17.0623 | -56.0308 | 2024-10-09 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.4 |
| 09fe65b0-ebb0-3a36-ad6d-fba1375221ea | -17.0626 | -56.01 | 2024-10-09 06:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 44a1b10e-41a6-3cdf-a154-f029b4903962 | -17.0599 | -57.3697 | 2024-10-09 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| f0961691-cf1b-30c8-8e5d-6bfbca03415a | -17.0795 | -57.3674 | 2024-10-09 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| f67d8542-9c75-339a-8380-9938429b70b7 | -17.0799 | -57.3469 | 2024-10-09 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| c74d5af7-0ec4-393f-b62d-b0af44c16a88 | -17.1188 | -57.3628 | 2024-10-09 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| a9be7608-8cd3-3706-827b-1285d2d8d8f3 | -17.1467 | -56.8463 | 2024-10-09 06:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 34d66a1a-7950-34bb-9fea-35ed23876adf | -17.1588 | -56.1222 | 2024-10-09 06:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 25b7b50b-4546-3763-8103-2d33ae4b8c18 | -18.1193 | -56.3921 | 2024-10-09 06:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| ee6c7911-7cb3-309e-bbda-d094ff9a8ffc | -18.5993 | -57.2629 | 2024-10-09 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 228f6ba1-0ff9-3d30-9fc2-c3ec51f16c17 | -9.4435 | -67.1008 | 2024-10-09 07:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| d9f69285-2c06-31e8-a652-5e5aad22a805 | -10.3843 | -64.8255 | 2024-10-09 07:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| edbe5bb2-caf0-3ba8-bb67-455f56d89e2a | -10.8754 | -63.9169 | 2024-10-09 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3c17e9f0-3967-3bf8-aa1d-4379c1434013 | -10.8755 | -63.8979 | 2024-10-09 07:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| ec95f666-fcc2-3e9d-a216-335dc904180b | -11.6806 | -64.0312 | 2024-10-09 07:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 994a3ed2-93be-392c-af22-f7acd33c710d | -11.6808 | -64.0121 | 2024-10-09 07:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b0c739c8-591f-3f85-980a-2ec1592fc735 | -13.3978 | -61.9376 | 2024-10-09 07:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 6f1eb1da-6c6a-3872-90db-baabe8751c8d | -13.398 | -61.9182 | 2024-10-09 07:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 42828daf-b41e-3f76-98b7-a250b79ed355 | -13.417 | -61.9169 | 2024-10-09 07:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |


[Clique aqui para ver as próximas entradas](README226.md)
