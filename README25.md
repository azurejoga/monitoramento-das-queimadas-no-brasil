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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a497818d-cf95-3eb4-aa8d-b99078065075 | -10.3153 | -56.772999 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3681b1-f08f-3a42-8ba3-9b4a43d4ca9d | -10.3173 | -56.7822 | 2024-09-26 00:56:17 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 619033dc-a6c5-3179-8c3c-0ccc49c28184 | -9.5683 | -53.3811 | 2024-09-26 00:56:18 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08a8ef5a-6601-3850-80f3-6380f1736d9d | -10.3055 | -56.775101 | 2024-09-26 00:56:18 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba00da0-c0b3-3f4d-9eb7-f40b0516ddc7 | -9.138 | -51.520599 | 2024-09-26 00:56:18 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 434d9a15-1375-3a7c-b504-fee06af6c5e3 | -9.1397 | -51.527802 | 2024-09-26 00:56:18 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9c4336-9e5e-397f-a465-7e0bf0195af2 | -9.56 | -53.390301 | 2024-09-26 00:56:18 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e5a3d5-ae51-32d6-9efc-90ee4c9da03f | -9.5616 | -53.397202 | 2024-09-26 00:56:18 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe7b9fe-78e3-3fff-a66d-59129a171c43 | -9.1266 | -51.515499 | 2024-09-26 00:56:18 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723c6c23-3f06-33fb-84d3-b025f82c9bb9 | -9.1282 | -51.5228 | 2024-09-26 00:56:18 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 858adf50-3bb7-3d1c-a988-d405ed8bf2b6 | -9.1299 | -51.529999 | 2024-09-26 00:56:18 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16d19267-7f44-379c-a4ce-0aa6649ddbff | -12.822 | -62.7078 | 2024-09-26 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 557238dd-4378-3328-a28e-f66a03c27d23 | -12.8222 | -62.6886 | 2024-09-26 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b22cd9d3-f8b2-334e-900d-ef8fc3dacdb4 | -12.841 | -62.7067 | 2024-09-26 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 08e2a4f6-3e6b-33e1-9888-ce68f6b31bf5 | -12.8411 | -62.6874 | 2024-09-26 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4148f610-e1c0-3838-8fa0-890641273698 | -10.3288 | -57.273499 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da8bd910-2873-36ac-8471-7edb0adcc042 | -10.3308 | -57.283298 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd282d4-fa13-381d-ae33-eae1f25b59d1 | -9.665 | -54.235699 | 2024-09-26 00:56:19 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea749811-2f0d-3cc3-8586-307db0fd42b2 | -9.6666 | -54.242802 | 2024-09-26 00:56:19 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3774da5-bdc7-3123-b050-9bdcdf4d6bef | -10.3128 | -57.246399 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f343efc9-bf95-3112-8ddd-0daf434e210a | -10.301 | -57.238701 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e731d50c-de83-3890-aff8-0652b2fb4b4e | -10.303 | -57.248402 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3da33730-12f1-3dae-a89e-74dd1d4a2548 | -10.3051 | -57.258099 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd1f129-9b2d-3df6-9493-47821134dec4 | -10.2932 | -57.2505 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4abb6b99-a6c2-3a25-aa96-45d92166275a | -10.2953 | -57.260201 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 772bc8b7-0640-33f3-a26e-81250aad35fc | -10.2973 | -57.27 | 2024-09-26 00:56:19 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22719c9a-3d9f-3095-b2b6-351da87cff66 | -13.0295 | -57.2985 | 2024-09-26 00:56:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 238507d9-1e8c-3d2c-bbe9-620b0cf1babc | -13.1963 | -45.6308 | 2024-09-26 00:56:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c687acdb-d13e-3e0e-837e-1cf58bc3187e | -9.4666 | -53.571602 | 2024-09-26 00:56:20 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 099ecbd9-cebb-3231-b57a-7cb7fbdec4d6 | -9.5849 | -54.245998 | 2024-09-26 00:56:20 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1104059-580d-336f-b94b-2398c8a6583d | -9.6811 | -55.155102 | 2024-09-26 00:56:22 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c173d4a7-aae0-378e-9596-f4ab00299a66 | -9.6828 | -55.162701 | 2024-09-26 00:56:22 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95a6d2cc-9d1a-3a81-a2bf-8be558d19217 | -9.4865 | -54.546501 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac03dd80-77b1-3c71-89c4-8e318196c7a4 | -9.4881 | -54.553799 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb31b2d-c9c6-38da-9cd1-73d40178b2df | -9.6958 | -55.506599 | 2024-09-26 00:56:23 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f52f2910-22f9-39f9-9eda-ff2673a51e57 | -10.4554 | -59.1152 | 2024-09-26 00:56:23 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9117b108-e733-32e0-88e0-709c5c361569 | -9.4767 | -54.548599 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a14aece-fd4b-3caa-9c19-83f9bead470d | -9.4654 | -54.543598 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62721202-1252-32ee-8004-eaac5a6673a8 | -9.4669 | -54.5508 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cba700d5-f17e-33d5-ac50-efbeb8d956ed | -9.4685 | -54.558102 | 2024-09-26 00:56:23 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec67386a-bae9-3c9f-827c-fdec4ad182b7 | -10.3843 | -58.867901 | 2024-09-26 00:56:23 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9deda8a1-0f6a-30ed-916a-0aa23c0e7542 | -10.3869 | -58.880199 | 2024-09-26 00:56:23 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90b0b380-c14e-3d78-97e9-4ac99582ab72 | -13.7513 | -51.0736 | 2024-09-26 00:56:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8555d9d5-f301-332b-9888-2de54055bb74 | -9.4587 | -54.560299 | 2024-09-26 00:56:24 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ddda6c-7acd-324b-98ff-0ca7798a08d8 | -10.3772 | -58.882198 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf28275c-fe48-32fc-8ac1-f370ee6e8e38 | -10.3797 | -58.8946 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38dc67f8-7055-3bc9-be72-6367ff9a18a8 | -10.3648 | -58.872002 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a96a8cb-6759-3c75-93e3-aaef357f60bb | -10.3674 | -58.8843 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 080fd71c-5077-366a-a57f-f73594cfefd3 | -10.3699 | -58.896702 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e60add4-2720-323c-b274-a18677840281 | -10.355 | -58.874001 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 873583a5-c9e8-3c6e-82be-44f4a9646a38 | -10.3576 | -58.886299 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 280a3eac-b006-39d3-b452-2005e3e103ac | -10.3601 | -58.898701 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 599354a3-0da0-32e0-896c-08bd2d1e398d | -10.3504 | -58.9007 | 2024-09-26 00:56:24 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76056551-5f55-389f-ae16-26501aec3c23 | -10.72 | -60.728901 | 2024-09-26 00:56:24 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d06e293a-227c-3613-af0c-0221558bf1e4 | -10.707 | -60.714199 | 2024-09-26 00:56:24 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d082d17a-f305-3060-bab7-931dc26502cd | -9.1149 | -53.2869 | 2024-09-26 00:56:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45eb8a78-ddbe-315a-96b7-811ecadc1b6d | -9.1164 | -53.2938 | 2024-09-26 00:56:25 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d90af01c-4932-3a62-989f-90257ce5489f | -10.6875 | -60.717999 | 2024-09-26 00:56:25 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12931381-0ef9-311f-b588-bb6a731ca0e1 | -10.6777 | -60.720001 | 2024-09-26 00:56:25 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b728e8ab-4b28-3aee-b745-dd74d8d69426 | -9.9001 | -57.0354 | 2024-09-26 00:56:25 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c487d9dc-612b-394d-97f2-74f0e460f640 | -9.9021 | -57.044701 | 2024-09-26 00:56:25 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acb14bb4-eb42-3d27-a388-03d477b6e557 | -9.904 | -57.0541 | 2024-09-26 00:56:25 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0d5844-5756-32cb-99bd-16b2f0e4873f | -8.914 | -52.7589 | 2024-09-26 00:56:26 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0e3eec-2d43-3e2a-824a-daadeb7fa58e | -14.4444 | -45.2321 | 2024-09-26 00:56:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 46646277-a921-3f60-a7af-788a2aedfcfc | -14.4449 | -45.2088 | 2024-09-26 00:56:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e32c4634-df4c-3173-821b-101134a5bb3b | -14.4634 | -45.252 | 2024-09-26 00:56:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2059ce96-1ff9-3a9e-b99d-341999f2fa00 | -14.4639 | -45.2286 | 2024-09-26 00:56:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 56dda8d7-c17a-39ba-9a5b-ba8c6d4cba46 | -14.4644 | -45.2052 | 2024-09-26 00:56:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 87e0fd60-5d99-3fbe-8e3b-53c27c5e85e0 | -8.8884 | -53.0117 | 2024-09-26 00:56:27 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5a3767-2dc2-3874-9136-4a884e9472f7 | -8.8899 | -53.0186 | 2024-09-26 00:56:27 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841c52ce-330a-3f65-9213-a8fcc8af67cb | -8.8915 | -53.025501 | 2024-09-26 00:56:27 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b22ee7f-290c-30a5-8c2f-31b65b34ae11 | -9.1725 | -54.6614 | 2024-09-26 00:56:29 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f710326-5db8-3313-b411-eea7fdb6ca80 | -9.1741 | -54.668701 | 2024-09-26 00:56:29 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ecaa4e-6add-32bf-acce-745b3508d3b3 | -9.6208 | -56.7327 | 2024-09-26 00:56:29 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a67ac04-5ba1-33f0-8dcd-b03f59e7b60f | -9.6454 | -56.944698 | 2024-09-26 00:56:29 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7b7768-5f06-301a-987b-df1374bbb992 | -9.6947 | -57.1772 | 2024-09-26 00:56:29 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b048a633-3c5a-33ae-b4cc-f86d5fa81532 | -9.6968 | -57.186699 | 2024-09-26 00:56:29 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6656f6-052b-3233-94e2-fd828a0286eb | -9.6988 | -57.196201 | 2024-09-26 00:56:29 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b221c8b-d317-31a1-a7ec-2f7bb5b48ec3 | -9.689 | -57.198299 | 2024-09-26 00:56:29 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7d72dc-de75-3d1c-b54b-397464d2df4b | -9.1007 | -54.662102 | 2024-09-26 00:56:30 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dedb23f-754e-3a18-83bd-98ec39b14da4 | -9.7585 | -57.770302 | 2024-09-26 00:56:30 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61d67903-cd75-3900-9484-fcfaca31043a | -8.6629 | -53.062599 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c994ccdb-492e-303f-8880-31ce25970fa0 | -8.6644 | -53.0695 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62409263-973a-32fc-9a7a-72ccf3d44ef4 | -7.0899 | -46.423401 | 2024-09-26 00:56:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 088fdc26-faf5-3bf5-922c-5e78ffda199e | -7.0934 | -46.437901 | 2024-09-26 00:56:31 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6936bec9-9c27-3224-aed8-5ba31c93d464 | -8.0401 | -50.425999 | 2024-09-26 00:56:31 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037d20c8-0e60-3b21-be3f-b8ef8a443954 | -8.6495 | -53.094501 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d413b24f-bfe4-32dd-a8df-e8d6bf81669c | -8.651 | -53.101398 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcb9136-ea11-3461-8499-b1e78087f001 | -8.6526 | -53.108299 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66b906ff-4a72-35f2-8261-b26e49e62e63 | -8.6681 | -53.177299 | 2024-09-26 00:56:31 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35e11ffb-228a-3bfe-bdb1-9626c7e9c0b7 | -8.6567 | -53.1726 | 2024-09-26 00:56:32 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d68cae-018b-3289-962b-14c05a3bc4f0 | -8.6583 | -53.179501 | 2024-09-26 00:56:32 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff7dbf75-95bb-3c15-b51e-4536a9bcd07e | -8.6485 | -53.181702 | 2024-09-26 00:56:32 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0618e7b-b0ed-3fca-8556-46b13a108abf | -9.6206 | -57.745998 | 2024-09-26 00:56:32 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa7e3cca-bad6-3ea5-87d4-663f7cd8dd71 | -9.6108 | -57.7481 | 2024-09-26 00:56:32 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b647d7d3-91d8-3066-ac48-9afdedd12584 | -9.6129 | -57.758301 | 2024-09-26 00:56:32 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97970e29-5f8f-3d4f-8ade-4ad66fbb42d2 | -9.3991 | -56.845699 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d368b9c-c8af-3951-8f2c-cdafc1c7f351 | -9.401 | -56.854698 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 925ba734-951c-3c02-abff-359b91dfee2f | -9.4029 | -56.863701 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64edf29e-682e-3ab4-91ff-6abe48a904fb | -8.9207 | -54.732101 | 2024-09-26 00:56:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README26.md)
