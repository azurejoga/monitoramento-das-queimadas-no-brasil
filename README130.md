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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ff0622b-1f1e-3dce-99ee-59ccbcf9308d | -10.40199 | -52.92179 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dadbe59-9d87-316c-996d-291fa15e0971 | -10.39865 | -52.92126 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 759afe9f-c058-3770-95a1-46bd3bddc95f | -10.39532 | -52.92073 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4ff39c-2b70-3d69-a583-c75d8afb6478 | -10.39144 | -52.92373 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb37975-5673-3f78-b0cc-c1bc5f9bcbcd | -10.38811 | -52.9232 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0fe8a74-62aa-31da-80e8-9f89bd825af5 | -10.38756 | -52.92672 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e5399d0-3017-3d39-994d-96de89a62cc6 | -10.38701 | -52.93025 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40448013-53aa-37e9-a567-caf9dd83a471 | -10.27775 | -53.32328 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727b32ae-cc4e-349f-a77e-b562b4c8a37c | -10.22902 | -52.72403 | 2024-10-03 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8200996b-4fc1-320f-9acb-a2b552506824 | -10.22569 | -52.7235 | 2024-10-03 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25e864d-7249-3ebe-b116-96171651d560 | -10.22327 | -52.70158 | 2024-10-03 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5aaf7ca-71d2-36ec-93ea-0a0cc7687180 | -10.22272 | -52.70511 | 2024-10-03 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef96d48d-e190-37cd-8e42-0d1f0b109264 | -10.21993 | -52.70105 | 2024-10-03 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f830cca-76f7-3063-a788-d67a0ee206f1 | -10.04562 | -53.48709 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6087dce2-0b38-351a-988a-1e15fe33d126 | -10.02341 | -53.41167 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a03c52e-af77-3107-9483-5161bd9c436b | -10.02286 | -53.41517 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21cf1ca2-7fa7-3ae2-8de6-41e866013407 | -10.02009 | -53.41114 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 810c2c51-7528-3fd1-8fd1-2fb3ac1af920 | -10.01954 | -53.41464 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b15e509f-7af1-341b-8f8c-f2f698146ee5 | -9.76105 | -53.16862 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 427c434c-b69d-3c26-b511-fedf312b6034 | -9.75828 | -53.16459 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce0ea21c-cad7-32b9-84a4-b0a202da0445 | -9.75773 | -53.16809 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ad1588-fd19-387b-b47e-e99c01c51310 | -9.73613 | -53.17541 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e7679dd-9d18-3cb3-a3d7-7f8be615a434 | -9.68687 | -53.18917 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5187641-2a2a-35ab-b373-129463d59e33 | -9.68132 | -53.18111 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67cbc748-a6c3-39e3-bf56-4140c2219d8d | -9.67964 | -53.17007 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60529f4c-6f68-335e-872f-b0bb6f41cdcf | -9.67909 | -53.17357 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b5ba64-2a2f-3502-9e77-4a7326338c66 | -9.67854 | -53.17707 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e085243c-915e-3625-933d-b7fb531de805 | -9.67412 | -53.18354 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bc14563-22fd-31be-8711-44d906677ca5 | -9.62979 | -53.18364 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c4ee26e-93d1-3d26-b84b-2b5e13e9ecdf | -9.62591 | -53.18661 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31bf9d80-3b78-334b-9056-7e75f9e2541b | -9.62259 | -53.18608 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 897d065d-b6f7-37d7-a2af-6ffd00dfcd4f | -9.61319 | -53.20251 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7174d3-3760-3712-8032-8bcc9a0655b9 | -9.61209 | -53.20951 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbd5ff0a-995c-3fa1-aa3f-ef214fc52501 | -9.59996 | -53.26497 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a96efa1-f09a-3e2d-8257-1af22105d281 | -9.59941 | -53.26846 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c719d39-bd29-3218-8089-0f1fc9ddd5f2 | -9.58325 | -53.26982 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 186e3a78-cc09-3ada-8f31-81a44bc78d7c | -9.5827 | -53.27332 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385ea231-1900-3354-9e1a-3a859ff77b60 | -9.5816 | -53.28032 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7112809-6422-3697-9652-62a8cf5b94b3 | -9.57937 | -53.27279 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d9e571f-4d28-34ed-8281-3b07e18c624c | -9.57827 | -53.27978 | 2024-10-03 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc03fab-ca8d-3d4e-848b-e8c6c4065283 | -10.66696 | -53.70884 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ab6730-c026-3886-a02f-771292d0ebcf | -10.6653 | -53.69776 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab4f3d8d-74cf-39ae-85e1-1e84d52b3ab4 | -10.66475 | -53.70127 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75026978-d153-3e82-92c1-4f79d1650692 | -10.66364 | -53.70829 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93e2050-a96b-3577-bbc4-0c84cd75b95a | -10.66308 | -53.71181 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 566927fe-0e31-3a05-bc15-8b4b5b5fea6c | -10.66253 | -53.69371 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384ff2dd-e7ab-3f27-8e81-d2d562093346 | -10.66198 | -53.69722 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08226b5e-ea4e-3688-a9e4-c0c7f09c7ee0 | -10.66142 | -53.70073 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111a9c9c-f5bf-3720-b3ec-44b2e76b7c63 | -10.65976 | -53.68966 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 777ad64e-ad07-32f0-8f61-58cd3de1104b | -10.65921 | -53.69317 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc08366-3b0f-3458-95ac-f6aafe7f9f54 | -10.65865 | -53.69668 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| decd1210-74d1-3622-a668-619a40175e8b | -10.6581 | -53.7002 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96878d5a-f5cf-309a-be7c-cbbb22ffe616 | -10.65755 | -53.70371 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 359f9fcd-90b8-347a-8b29-a85ae09851da | -10.65699 | -53.70722 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce64b4ef-6ba4-3d49-9411-87ce67c9b026 | -10.65588 | -53.69263 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a16ec71b-aa9e-3129-a1b9-491eef15e487 | -10.65533 | -53.69615 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988058de-84af-3022-90e4-66e96b58425b | -10.65478 | -53.69966 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d816b2f-e378-327a-8a96-9daba5dd8590 | -10.65422 | -53.70317 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea43e7f-7af2-35d3-aa4b-547325515706 | -10.65366 | -53.70668 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be21101b-0c71-37d2-9b89-78d47203091b | -10.65311 | -53.7102 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 335530bb-8e5a-3de7-9668-007df6c6d80d | -10.65256 | -53.6921 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ca642e-652c-3bfa-880a-bbff5e94f84e | -10.65255 | -53.71371 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b3fb35-b5cf-32b9-a410-c17d044b65e1 | -10.65201 | -53.6956 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af7c41cf-7aa3-3bd4-890b-1ca66fbe9268 | -10.652 | -53.71723 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2393686-1876-34c6-845b-3b383c1ffaec | -10.65145 | -53.69912 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b511c17a-8b8b-337e-8dfc-af5f72f4075e | -10.65089 | -53.70263 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e26ae222-f1f1-398e-b9eb-d1f8f56261a4 | -10.65034 | -53.70615 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19547d66-f9d5-32f1-bab4-41837b7c0c4f | -10.64978 | -53.70966 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c620b7d0-2521-36a0-ba35-c90d8ede236f | -10.64924 | -53.69156 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f81c1c64-97d3-3468-9e53-0845c1695388 | -10.64868 | -53.69507 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd6cc0c-534c-3b5f-845e-b92c0be6bebf | -10.64812 | -53.69858 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609fb0e5-9584-32b6-8900-f7e6d53e9e12 | -10.64757 | -53.7021 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd265c42-b13b-350d-92a9-fd384e5919d1 | -10.64591 | -53.69102 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc018655-f7a5-3e18-a3d0-017841952925 | -10.64536 | -53.69453 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4d257f-73b9-319f-812b-16fe49b065cb | -10.6448 | -53.69804 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e81a53fa-81c2-37aa-a4a8-b69ed21b056b | -10.64425 | -53.70156 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb0061c8-99d3-35bd-8bef-e3b6750e574d | -10.64369 | -53.70507 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a358f17c-eef5-3975-a4a2-53870d9a6342 | -10.64259 | -53.69048 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10d644bd-54b1-3062-bfb6-a96059efb843 | -10.64203 | -53.694 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b4d1b1-a387-3b2d-b0a7-a4a82b04851b | -10.64148 | -53.69751 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eacaf81-ee59-3875-b1bc-158be808c17e | -10.64092 | -53.70102 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a3b015-6f0f-3200-aa7f-d0c06fc658b3 | -10.64036 | -53.70453 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73095aa9-e943-355c-94a9-65135447f7c0 | -10.63926 | -53.68995 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7e777c3-f266-37e8-94ed-03d4385160bf | -10.63871 | -53.69345 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed03f0b4-57c9-3dcb-89db-0a507f55e410 | -10.63815 | -53.69697 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b9be139-0bc7-3784-9b47-9a00b1e2b262 | -10.63759 | -53.70049 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d79f4d-0692-32ef-a9fa-4358cbd7dc2b | -10.63594 | -53.68941 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 381e3e8c-782c-3a56-9c7d-5243710659b5 | -10.63538 | -53.69292 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e95752d7-8433-3317-a61e-7aa9ed57afa4 | -10.63483 | -53.69643 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c6089cf9-2957-3ec6-b351-e72d7fa8deb0 | -10.63427 | -53.69995 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 348e344c-5698-32f3-bdd8-b5591e3d0672 | -10.63206 | -53.69238 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5f96184-7339-3a7b-be29-0ea06062cefe | -10.6315 | -53.6959 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d284898d-4814-36ec-8864-8cc6756e7260 | -10.63095 | -53.69941 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 89bf4595-8470-387b-b350-b2c3520d847f | -10.62818 | -53.69536 | 2024-10-03 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 631bb773-3ed0-34b7-a323-32236fd00544 | -10.43259 | -53.69291 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2d0d58b-1da2-3ba6-ad1d-0389ca1b284f | -10.42261 | -53.6913 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0350266e-fee5-3217-a515-bf5f1b269089 | -10.41929 | -53.69077 | 2024-10-03 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9218ea8f-d03a-3fc4-8d9f-989be4bf4b4f | -11.08553 | -52.52215 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea33c387-584b-3dd3-af9d-baf18aa53532 | -11.08498 | -52.52575 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ab61bc5-2a48-3260-8168-a4c3b84ffc05 | -11.08442 | -52.52935 | 2024-10-03 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README131.md)
