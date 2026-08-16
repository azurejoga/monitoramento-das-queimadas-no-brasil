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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6a6fc95-4895-3150-aefc-e6d2ec226db0 | -11.87335 | -51.95257 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e795b59-6163-3d52-86f8-30dc2eb14aa1 | -8.62333 | -63.72589 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f646fb1-a12d-37cc-8f76-04c26e4e8ff7 | -9.14487 | -59.64985 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8b8fb01-db3e-30e1-b8a5-7caf160b5633 | -7.55163 | -61.17664 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844c8a64-4b06-3f7b-8e4b-4a1b76b98966 | -6.73399 | -58.58582 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8ea48e2-f1be-3e3b-bee8-8c3b0f3a0ee7 | -9.47679 | -51.62007 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa08a7cb-3d74-38f1-94e3-e980f99be264 | -9.37032 | -57.36409 | 2026-08-16 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9448c78-099f-358e-92dd-a53907118330 | -9.54106 | -56.80206 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96bd77d4-e9d2-372a-ba59-4d2bf8a384ef | -6.83036 | -56.41688 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b6e7d86-5673-36a5-9f60-dd81effa9582 | -11.04461 | -47.24817 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad727eb8-ff91-30c5-b6ff-cc791f5f8edd | -6.56928 | -56.54615 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c554f07-1d30-3086-a6fd-6dafa00f73ff | -8.95936 | -60.51125 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f194b63a-4917-368e-880d-eaa13419d703 | -8.95737 | -60.59238 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1047e6-2e88-348b-a944-4b7d4a322a82 | -8.98352 | -60.5297 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9d7d1991-7bb4-3055-85e9-5bd7f68b3e07 | -6.63637 | -56.40329 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16bb169a-9561-34ed-97a3-55556936e44f | -11.07781 | -47.25336 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a84db28-74a6-3863-9b0c-6c9d39272d71 | -7.36519 | -46.84324 | 2026-08-16 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84da86e9-7838-3840-8cd4-0b711942a153 | -7.68921 | -55.15764 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a36ceb9-7e13-3fef-b54b-6c089204fc9b | -6.84808 | -56.43394 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f5e0abc-40ad-36a4-9e78-d7083147a865 | -6.71948 | -58.9378 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03a38baa-f5c8-3579-9cf9-039e3a5f76f6 | -8.25916 | -57.3443 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986ae9c5-537c-3854-9ce3-5b2cd6910124 | -6.59538 | -59.12221 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2caf21da-0631-312b-9e7c-63869ba95ad8 | -6.72508 | -58.92612 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e11e2c7f-1f6e-339f-9e99-829fb1c74a45 | -6.82648 | -56.4626 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d74b761-a5dc-3440-8fba-cee7cd8ec444 | -6.83922 | -56.4468 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56997299-7092-3f32-a1fa-d9228c394452 | -11.21019 | -54.81753 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b5c98a9-1994-385d-9323-2c1b0325ad58 | -8.43288 | -62.68351 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 7fbd527c-cdf2-38f1-902d-9a33dd64c167 | -6.82482 | -56.45164 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb312b0e-7ea3-3e7d-ac56-3266540c19ac | -8.43078 | -62.66995 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 916c8136-58db-36f1-83a1-a20f4252b46f | -6.85859 | -56.43206 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb0c1417-a586-3d34-9fdf-87c200ccddf8 | -9.20825 | -59.67655 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 483ab0f8-8eaa-3a71-9b7b-8489b4d11fc7 | -6.61584 | -58.99767 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85818474-de3c-3c70-be3d-03293e6969f7 | -8.60603 | -54.69464 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bec63f6-9783-39ba-a4f6-c3c41ed1fb7a | -9.27521 | -56.90244 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d375beb9-fe08-3f25-985e-59b63e84e985 | -8.10455 | -51.65852 | 2026-08-16 05:16:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 19fcbb96-e932-3ed6-b280-00a1bf64e523 | -11.07182 | -47.25608 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5aa2efda-1016-3a9d-81be-60e659f2492a | -6.79308 | -43.0252 | 2026-08-16 05:16:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4afba69b-2c99-3cc0-8056-5763e44e3879 | -6.70828 | -58.96109 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4431483a-c693-3fe7-a24c-02436f9b47a0 | -10.48239 | -50.37914 | 2026-08-16 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdd4f062-7231-344c-bcc4-8f3a7fe94b89 | -11.45933 | -46.61383 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b4265f1-34e3-311b-8d7e-c52391df198e | -7.57896 | -61.23598 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2690c40a-7bc2-379c-826a-ff06d150b551 | -7.34558 | -59.5972 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2af2ecee-0b12-34a8-bf44-7506705846d1 | -7.25656 | -44.6991 | 2026-08-16 05:16:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b72a53d-90cc-3e88-977b-cd859689d8a5 | -6.86154 | -58.97726 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e73d59ce-eb91-34fa-81a5-ddac3d38565e | -11.88254 | -51.94629 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb03cd13-93e1-3eae-a4e2-7467a48e92c9 | -9.69514 | -57.88839 | 2026-08-16 05:16:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 029b6ead-e552-398d-8fcb-d3de05a7ec81 | -6.62591 | -59.07173 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c07905b-d5f5-3c49-b8f5-2870fb5c3743 | -10.52304 | -44.8488 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 448b78b7-478c-3012-b21f-bab6ac642f91 | -12.01026 | -46.43829 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f489c92-9485-3f8a-ac5a-6e6948067d9f | -8.90355 | -60.56396 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c18bb13-7fc4-3f95-aecf-89deea14f2f9 | -6.6347 | -56.39235 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52327854-beb4-3b27-ac6b-50110c908c91 | -8.89975 | -60.56333 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a2b6a5a-5737-3c10-8e60-25cf1b45ef49 | -11.21713 | -54.81861 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc00bc82-c334-3975-8bdc-ec565bfda709 | -8.81277 | -66.76472 | 2026-08-16 05:16:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c895e438-928a-3c43-8af3-81df8b4ced77 | -6.63798 | -56.26473 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b725782-1ff0-3cc5-af7e-dee236f47516 | -6.7826 | -55.84392 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d51645-cf39-3759-9b4b-b92ecd914d8d | -6.86413 | -56.4187 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ca76997-7540-3886-9180-3250c8f44fcd | -11.47411 | -46.59022 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9f07c87-be9a-3f1c-8efc-53807dee2155 | -6.86513 | -58.97782 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74e1af58-8a20-3809-808c-b44edf5a180f | -5.23578 | -49.33388 | 2026-08-16 05:16:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e182d23-598f-3b0e-bfb0-807996156296 | -12.45343 | -46.6478 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6532d7a-289d-37e7-82cb-546abbed9c02 | -7.69256 | -55.15817 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc77b9f-d4e7-38e3-ad64-62e5f8b88611 | -6.86088 | -58.98134 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 213ce6cb-3df3-3e71-8333-4c367e590e6b | -6.70043 | -58.96399 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f7fa9a9-8f6b-3b5f-b277-59247af4aeed | -6.69122 | -59.06422 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5ed808d-b2ef-33be-9063-bb4064745d33 | -11.48478 | -46.59949 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b82c8908-aa7f-3f8f-83a6-726f241ca0b1 | -6.11445 | -57.70318 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 890e20d7-9595-300c-a54a-a4dfdeea2636 | -9.3059 | -56.91791 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e532227-c634-3b51-b846-eae643d39375 | -6.63313 | -59.07293 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b2dbf778-02a8-317e-bf44-e43ae81de99a | -9.93969 | -57.48978 | 2026-08-16 05:16:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca896ea9-bbdc-3123-8b45-cc78a697b6b5 | -8.97516 | -60.53306 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e782c26-ff70-367c-b281-36c6d539a13c | -6.31458 | -43.61255 | 2026-08-16 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f1e1258-3a18-398c-9eaa-ffcbcb1e1e9a | -9.13922 | -68.20507 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1f4e642-cc9e-3edd-b748-58b580e64435 | -11.20444 | -54.80867 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fdc70cb-4dbf-330b-9f60-5f266a843fd4 | -6.85705 | -58.9597 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3edd82d-f437-37eb-b2f1-b32f68a1ac5b | -6.13118 | -55.81135 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ea04b73-3dd3-3dd7-8069-e9a5f12283d4 | -6.84143 | -56.43289 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58660e67-b2fe-3128-add6-3b17f8213c43 | -8.89846 | -60.55554 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d2563e2-7778-36a7-8e66-0bcf0972b014 | -9.47509 | -60.55142 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07809899-2c5b-3bf0-8a2c-b9182ee34577 | -6.84088 | -56.43637 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 940d4e0f-1982-3ffe-b865-77e016488d0c | -8.42851 | -62.68273 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 341fdfc2-bba1-3668-9ebd-9773bc320177 | -10.9437 | -57.13706 | 2026-08-16 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75a304cf-b184-35a9-8d25-08df8c413d9b | -11.80496 | -51.78855 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447eaa97-1cc0-3303-920a-3ee1b680aeb3 | -6.6149 | -59.0485 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b90c08e5-2680-3d9c-835b-d1cb899b1cbd | -9.47759 | -60.51413 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61b37b8f-2049-34ee-8b6d-0f2396821e8e | -8.89954 | -60.58728 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab796799-7fad-304f-a408-44bfbb2543ba | -7.46418 | -45.09545 | 2026-08-16 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d97db336-71c2-31f2-9eec-9c6b7df3545e | -6.77928 | -55.8434 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cbd4c5c-6305-3606-8023-65265b818574 | -6.60797 | -59.00062 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b348a225-a8da-301b-8ae6-b4a78e6a0c3c | -8.97594 | -60.52841 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 57dc93f7-f6f1-399b-8489-832f7cf134d3 | -8.65966 | -54.73279 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a711039-c293-3e8d-862d-9f05f42c69e8 | -8.64412 | -54.69688 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3a3c18-6d6d-3fbf-97e0-9d78ab1cb804 | -6.40088 | -45.69427 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99b4b8e6-d002-36fe-8c45-df6e0ca34f51 | -8.9638 | -60.53108 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5cc9f9c5-ae06-3033-a228-6590298ed55e | -8.96537 | -60.5218 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cf0ebbb6-b68b-3fb8-a3fd-8eefd6e45123 | -7.36404 | -46.81126 | 2026-08-16 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c41d6f2c-88d8-377e-ae99-e728dbd84786 | -10.53996 | -44.86671 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a584cdd2-fe7f-3440-96b8-1d18682c9794 | -6.59314 | -59.11327 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2438a2d-da8a-330f-bdd8-d69feffe5476 | -6.87969 | -56.51029 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd3f61e-9c4f-38ab-89fd-b7abf8d8acdb | -9.29937 | -56.80936 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README40.md)
