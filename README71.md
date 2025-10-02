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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f7f4bf8-eb39-3fa3-9d75-478c24b65d2a | -12.27474 | -44.12394 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d0b91f4e-4c28-38bb-b146-5456a4e098a1 | -10.21968 | -50.34487 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 749f60e6-875d-37bc-a9db-fa1a864b9ab7 | -11.87345 | -45.027 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 465d77e7-d4c2-376e-8cfa-6477884f0898 | -11.4823 | -44.99585 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a00adfaf-fa7c-366e-94bc-a2dcab977b2b | -10.60704 | -47.84429 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5841b80-d709-33a6-8d57-1788db79cba4 | -9.80404 | -47.82616 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93a7a99d-b223-336a-83de-a6fbb827e249 | -12.11092 | -43.42728 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69c72ade-18ff-3c66-b612-1228857311fa | -10.66642 | -48.5653 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab8a3735-25ef-3cf8-9a5d-8a4ac62070de | -11.67856 | -44.28086 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65bb639e-0245-363a-946b-c7cdef4625ca | -6.77666 | -45.57915 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 838e22cb-ccca-32bf-86ce-cf64a3b077aa | -8.50945 | -47.79607 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91f8ae7d-d7f8-3263-9f0a-9771bacf04f4 | -10.8279 | -46.62984 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f1dab8a-cdec-345d-a402-e97865a317ca | -6.72957 | -44.14523 | 2025-10-02 04:29:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5983e09d-1a9c-3208-ba5f-3dca2037868c | -6.28244 | -44.05645 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec3a6c99-cafe-3c7b-9a18-1addf45003fd | -11.7866 | -47.5684 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e8b57ae-6420-3dd5-a4a5-6ca7c6e031db | -8.90272 | -46.66363 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01d8c100-0195-39bb-875a-2d9e1184219a | -11.46711 | -45.00135 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bab1b6b-e733-3b26-a6bb-ee53e5606440 | -11.4765 | -44.98669 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc478f11-9b6e-35d2-92ed-6cd3cffe344a | -6.78775 | -44.89681 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c566aa3-1797-308a-9179-44f192be2abb | -10.47278 | -49.10936 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e159f343-b1eb-3464-8e0c-451024b01d36 | -11.03437 | -47.81567 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3b1eaeb-c26a-3295-91f6-7def274ae726 | -10.22759 | -50.32027 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ef66c86b-2d31-3000-9b9e-d72d88789459 | -11.59449 | -47.21938 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d576951-5604-3c10-9b3a-3130ae9a024f | -7.02605 | -38.82872 | 2025-10-02 04:29:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3eec1fd4-5d86-3eb0-a117-98e1bc32829f | -6.69726 | -42.81977 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ffc37d30-5efa-37d0-b776-d3ffd80ee833 | -8.89656 | -46.61608 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a0e4275-1ba1-35b7-b857-65d1bac3948d | -11.77948 | -47.3972 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ba95143-2b53-36e6-ae16-55316743ad8a | -9.94629 | -43.6806 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3654810c-95db-3c19-be88-d7bccf3c6bd7 | -6.32537 | -43.04229 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd92b47-098f-3fd5-95de-2d00c97f4178 | -10.19357 | -50.27731 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a58276d-56b3-349c-bf24-def0862ce96e | -10.24999 | -50.31979 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ebf5095-678a-32aa-9bd5-54ba55112165 | -11.9477 | -43.91634 | 2025-10-02 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 806223c5-482b-3ed2-98f1-2e86c7fbef56 | -11.81766 | -45.01463 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51bf1ebf-7011-3dd9-b7fa-c2867a324585 | -10.21707 | -50.33751 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08d21fbd-9008-3985-b225-c568c5bb6eed | -8.21101 | -45.52785 | 2025-10-02 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b35ffeed-d5a3-38fc-9316-6d764cdd0daa | -6.9602 | -45.31411 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd2cb2f-08b8-3efd-b88d-c8eb50310044 | -11.80631 | -44.99369 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6d5ceee-2725-3be5-ab78-c6d77d9d2993 | -11.79049 | -47.56542 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 425dc93b-53ca-34e6-b933-5c756613ce44 | -10.83918 | -45.39408 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78246801-330f-3f02-b455-46a96183080e | -11.48373 | -45.10731 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f090b21-1348-39cb-9b24-36930c2cf6e6 | -9.71241 | -48.95196 | 2025-10-02 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43f3f327-2fe5-344b-a7a1-51a83871c058 | -11.19623 | -47.19528 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3e00ff3-5157-3c2c-983d-3fa4f0c93434 | -11.76595 | -46.8583 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 087304bb-cca6-3faf-9f43-909a18249049 | -8.44569 | -45.58662 | 2025-10-02 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a2d978c-1c8f-3fba-80cd-1dc3d5e3401d | -10.76258 | -44.97425 | 2025-10-02 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09426c03-2986-30b7-aac6-6510ba2acee0 | -6.49358 | -44.29677 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1cd2c98-3b83-3c3d-b96b-e431a3d3435c | -8.57084 | -49.88927 | 2025-10-02 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a5897c1-80e0-3251-bba3-e41799ab4ea4 | -7.77873 | -42.50946 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8f12d661-b201-33e5-a78d-48f0a2eca9fa | -5.83351 | -45.77552 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12d83116-55d0-3d64-8a5c-e6b5811d441f | -11.42805 | -43.49558 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0061a570-96fd-3231-a05f-1a1639e132e0 | -6.78055 | -45.57613 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb7710b2-02e5-32cc-a3ca-5f28aaae575e | -10.22616 | -50.32867 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c7a170bc-6e37-321b-a16f-bab581a8741c | -11.81622 | -45.02354 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55ed9a58-0d44-3a12-8554-320eb21c22d7 | -11.49872 | -43.50873 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d57c20d1-2c48-3c0f-9efe-da71dc6f2450 | -11.194 | -47.76521 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eef331cc-2bf1-3a2a-bd02-6a5e5bf89bfe | -7.78813 | -42.52539 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d7c66061-941e-33a2-826d-e6b94a8d9d85 | -11.44439 | -44.96099 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31c4563e-152c-32f7-a617-c0ef45ed1ac0 | -6.5964 | -50.03818 | 2025-10-02 04:29:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| beb2ab81-d973-3fd1-81f1-e91140d6df78 | -5.99513 | -45.79772 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86d130a1-8965-3464-bb08-7ff43d91838f | -6.64285 | -42.08694 | 2025-10-02 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ee9e375-c1be-3600-8c8c-69280c2e2e7f | -6.79115 | -44.89735 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1015a695-10eb-3018-9f61-b8eb43e74d26 | -6.78505 | -45.59127 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76c70bf4-89de-3ea1-b4b0-42d6bd58ed6a | -10.35153 | -48.20385 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 566326b7-771c-35b5-ac20-90c0d4816527 | -7.30394 | -42.88662 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f06604f7-85ea-34ef-a270-9d86c3e6e093 | -11.00767 | -46.58906 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71166f6f-d58f-3c48-97e8-0b5dde9d624b | -7.55541 | -42.6432 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b47a52f8-9d02-3025-bdfa-9674a98feca8 | -10.82287 | -46.61812 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 205ff0b4-498f-336e-9ab2-71de2599566c | -10.22658 | -48.21266 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e48eece7-e3b3-3918-9ffe-a4c581de8bad | -7.78255 | -42.51008 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5a140280-baab-3721-a6e5-7d6ebcb5e296 | -7.30896 | -42.87837 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3530053-4aaf-3590-8ccd-31d218880d42 | -12.21749 | -43.75494 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 012ab2b4-ba5b-3a51-bce0-223ccdd2bd31 | -6.32966 | -43.03859 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0b32798-2f78-3b0b-bf5d-ee53d9272f92 | -10.84262 | -45.39461 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5ffe7700-3b77-3281-93a3-ec7cff91591d | -6.80854 | -44.73903 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d7f33c6-902e-3b64-8bfa-85ccb7ef5506 | -7.19247 | -41.69475 | 2025-10-02 04:29:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 156794c9-9ac2-324f-a2c6-4d03445f9f57 | -10.11055 | -45.67098 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f63668f5-ecab-337b-a3fd-48dd388249f6 | -6.36347 | -44.64263 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aaa28f8-472b-3c60-acf9-de7b5e292759 | -10.13033 | -45.67807 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ed5cf7b-dfb2-3828-ae1b-54aa2f9f83aa | -11.57458 | -47.02805 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94cae1a6-84ad-3962-a8f5-d70ce23263c4 | -7.51983 | -44.27996 | 2025-10-02 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce4c385c-743f-3cb7-b334-4b2043be867e | -9.79678 | -45.94287 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cc4fd1a-26b6-34ea-ab13-d6ce6f4bf55e | -6.96586 | -45.34414 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e504f41d-5b50-3329-8d0a-b12557ad4776 | -9.82826 | -48.28474 | 2025-10-02 04:29:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17bd1de2-8c9e-3fcc-a285-4208ec9301f8 | -10.83293 | -46.64155 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f45e408-0092-38da-b796-ca371c3b7678 | -11.47062 | -45.00187 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6cf63cb-490b-378d-8e21-1d40208719ae | -6.95627 | -45.31721 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fbbd090b-3f7d-3a8a-9834-64a303c2b390 | -10.89958 | -46.47728 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0275ea4-3017-3d89-b25b-1c71bf10b81b | -11.48107 | -43.50338 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2b59dc7-4185-37fa-80b4-438c76322109 | -8.85989 | -46.57464 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f06d0d78-6048-3653-8045-f08016b74f4e | -6.184 | -44.06569 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c645d626-18ca-39d1-a985-5789319f8be9 | -11.21596 | -48.21661 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e0ab4b0-801a-35f1-8671-6dd3ba5101bb | -9.93771 | -43.76304 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f9f5e0d0-f871-3219-a453-66d37d214d5f | -9.91442 | -47.70688 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f5c8a29-b609-31d4-95b3-9262e0ddbd46 | -10.68446 | -48.5609 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52ef55dc-374a-3999-ab4a-84a25d211c54 | -11.76646 | -46.83298 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77d8830d-525a-34dd-abfe-cee8ba317757 | -11.04104 | -47.81678 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec352776-4871-37ff-9096-bc28b72c48db | -10.96427 | -46.6477 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f5e7901-0227-31ec-948c-3823194ecc61 | -9.93295 | -43.74472 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 14ef4371-1420-30f4-aa91-e54f6f6beab7 | -11.48054 | -45.00755 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0135f04c-bc09-3f03-9f1e-06cdd9b62e92 | -11.16463 | -47.26599 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README72.md)
