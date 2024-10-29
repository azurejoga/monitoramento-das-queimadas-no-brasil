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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0388ab28-b5f0-3e97-a0d1-6a2b5fc1cd36 | -11.3504 | -54.48361 | 2024-10-29 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49ff62e4-f2f3-365c-8cb0-059f46719de0 | -11.34982 | -54.48752 | 2024-10-29 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f139e2d4-f396-37db-ba7e-937bebc4e7a7 | -11.3305 | -55.21738 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19680f76-b8f5-313f-b0b6-f9c94485e1cb | -11.3271 | -55.21685 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c03b99f1-0a8e-3907-88e9-f61be40a740c | -11.32425 | -55.21263 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c34e4b25-ced4-3eed-942f-f45da643122b | -11.32141 | -55.2084 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9a5d80c-131f-3f30-b0a5-939c258cf194 | -11.32085 | -55.2121 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9243f8b6-ebe8-30be-bcc5-6b4579f6224f | -11.31517 | -55.20361 | 2024-10-29 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d47270db-49bc-37a2-9129-f7013e4833c9 | -6.38854 | -55.37061 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aae67618-0f2c-31a1-9b28-0f0b2903a82d | -6.38799 | -55.37408 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20b42ece-5a76-35b2-8985-a2b2a9bad2b9 | -6.35357 | -55.54989 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 313edec6-c7fa-3589-ae08-097000f8bc51 | -6.23725 | -55.5565 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b0b921-6167-3913-8b89-754f20c7091d | -6.55508 | -54.95395 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 387d6666-afdd-3c7e-9e16-c1a832545f7a | -6.55453 | -54.95746 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cb171b4-18aa-311c-b7ef-db3568156361 | -9.31648 | -55.94235 | 2024-10-29 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9d86a27-4b2e-363e-9124-ea814540adef | -8.36999 | -55.15912 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12b7cd68-bce0-387e-bb85-ec656b2f7b9c | -8.36664 | -55.1586 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e2ae803-da19-38f3-bbde-896027e0cf10 | -8.32468 | -55.1193 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92d6e083-96ff-3511-b8d7-35daaeceb948 | -8.30567 | -55.10903 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 352c82a6-905a-30df-abc6-80fbb0f2c441 | -8.16664 | -55.19649 | 2024-10-29 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea3bc0b6-3483-3d7d-9855-fa5dee764e29 | -9.75349 | -55.34053 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c6367d-8c2e-3a17-9cae-da0180750875 | -9.75294 | -55.34412 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90a58cd5-f007-3631-9503-3f44f1439da7 | -9.74958 | -55.3436 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbfc820c-5746-31df-9e6c-e27db076d541 | -10.12617 | -56.27866 | 2024-10-29 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da9b9853-085d-31eb-81e3-b71ae3880fb6 | -10.09204 | -55.40332 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3fcb64a-36c9-3ce8-b24e-b55cddff90d1 | -10.089 | -55.19271 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fca4669a-f800-3095-8554-7bf005f87a78 | -10.08868 | -55.4028 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3708a5fd-6f8c-3469-886c-d7edefdfac93 | -10.08562 | -55.19218 | 2024-10-29 05:04:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e18c770-3efe-336e-861e-8e68dc56d662 | -12.0963 | -56.82853 | 2024-10-29 05:04:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ab0164-c194-39f5-8615-51f6b72f4caa | -12.09574 | -56.83206 | 2024-10-29 05:04:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6691ae5-99a1-3b93-9262-4ba431b08dad | -11.86912 | -56.87476 | 2024-10-29 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa229204-d9b7-3f0d-a3ac-5f3fecf78c47 | -11.86746 | -56.88534 | 2024-10-29 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d1df6d-2785-3fcb-b43e-e39e530e8b8e | -11.86413 | -56.8848 | 2024-10-29 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 899ed98a-2172-39c3-9df8-65ed12547d90 | -11.17239 | -56.29051 | 2024-10-29 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4141baae-6334-38f2-8900-661e45260a3e | -11.16907 | -56.28997 | 2024-10-29 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a8e2120-fc7d-3d3a-8302-7f2641b0d999 | -11.16574 | -56.28944 | 2024-10-29 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ede4691-f2c2-33a7-a59d-35c51bb8db93 | -11.16519 | -56.29297 | 2024-10-29 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2f0a56-a7f8-3aeb-98c9-cc8188f33e5a | -11.13975 | -55.53173 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a649bf-5f04-3a6c-a897-9e64dfc2c003 | -11.1392 | -55.53535 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a6ca44f7-e2c1-3edc-bf6b-4851a7264695 | -11.13865 | -55.53896 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 07464b35-bac3-3e0e-8b26-9d2dec47922a | -11.1381 | -55.54256 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 759c52cb-e1ae-325f-831a-af00af98a8c0 | -11.13755 | -55.54618 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 11d84444-f1c2-360f-9221-7aa21ac49374 | -11.13748 | -55.52397 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b4659d6-cf00-326a-9b86-a4d17fc43bd7 | -11.13693 | -55.52758 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3026b2ea-2559-3faa-9aeb-b9af89edfd67 | -11.13638 | -55.5312 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| de1b3aea-b6d5-3fb6-88be-06fd4296fc40 | -11.13583 | -55.53481 | 2024-10-29 05:04:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad23112e-12c9-3cac-9c2b-1279ece66aa2 | -11.12748 | -56.29418 | 2024-10-29 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7093d2e0-985a-3b13-bf80-ae6d91cf20dc | -12.33345 | -56.86628 | 2024-10-29 05:04:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f639956-12d5-36b4-aeb4-7c75967e34f9 | -5.07931 | -56.2431 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71c61b3c-53dd-3fa6-9e54-aa09c49422f8 | -5.0091 | -56.17452 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 705fc5b0-1fc6-3450-9bea-efe3171eeaa0 | -4.9619 | -56.93317 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e16f3b77-880f-3209-bb32-75b8deb2eaa1 | -4.93018 | -56.93217 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c62d08c8-ffb8-3147-816c-8a5161a8ba75 | -5.30769 | -55.82871 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 239f5f16-bb28-3e84-8610-a15d7819428f | -5.30714 | -55.83218 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab905c43-6dbc-3c9a-a1b6-a0f980a9c784 | -5.30659 | -55.83565 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c08dd063-3b8f-308c-bfa6-3ac47cfdf729 | -5.30605 | -55.83913 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e58faf1-a414-3be2-8f2b-de21ef023699 | -5.30491 | -55.82472 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b77bdd43-f6d2-38d5-b2ab-9b31bfee1d92 | -5.30436 | -55.82819 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56304702-822e-3a06-b39b-4d104bd6d238 | -5.30159 | -55.8242 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 947101da-55f1-39e1-ae82-c10d6619d2b7 | -5.30104 | -55.82766 | 2024-10-29 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c566519d-b443-3a7f-a482-9048396bac89 | -6.47662 | -56.01372 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 738c79da-6d87-30a2-9423-8e17711208f9 | -6.33763 | -56.05589 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14a1a551-3e28-3ffd-9ec8-1426c25ae825 | -6.33376 | -56.05884 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc5d76c4-6ada-3a5b-b1b9-78341a6ad575 | -6.26624 | -56.52783 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e46c19c9-b603-3eac-a91d-0128214fed76 | -6.26568 | -56.53135 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c5c576-6284-33ec-a147-af567653f214 | -6.26512 | -56.53487 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8111c436-f309-3539-b74d-7cbd53a2d030 | -6.26401 | -56.52026 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a30a6369-c605-3c85-86bd-21e189c93b50 | -6.26345 | -56.52379 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc89be6e-27c6-3d7d-bdfa-8d091852371e | -6.26289 | -56.52733 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1820bffc-b3c3-3a4a-a169-96472558e1f9 | -6.25551 | -56.68169 | 2024-10-29 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20f27e6-ea3c-3c81-a087-431ad919e859 | -9.36853 | -56.83563 | 2024-10-29 05:04:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9660dd30-49ac-336e-a738-209cfb504311 | -9.74133 | -56.97851 | 2024-10-29 05:04:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4facc78-c5e1-373f-888b-bf9dbd548a5b | -10.85041 | -56.91957 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bae38130-c414-3eb8-9387-7ae9073b41b3 | -10.84764 | -56.91552 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f18c36c-a08c-3470-8df1-03f23f4a1a3c | -10.84709 | -56.91903 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14a7dc35-f2fa-3a3e-9500-caf0f1ccf804 | -10.59545 | -57.79416 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a0822a-6556-3033-82d1-274e51cd2a63 | -10.59487 | -57.79776 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c88c65b5-c6ed-3a61-afb3-caa95de7784e | -10.59429 | -57.80135 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72efaa08-28ea-3381-b86b-5032747c02b9 | -10.26014 | -56.75997 | 2024-10-29 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e19e944-68e5-3ed3-b788-682287cb2c55 | -12.20596 | -57.22565 | 2024-10-29 05:04:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1b08855-60ed-3b7b-8c1b-469fe2ee0197 | -12.20264 | -57.22511 | 2024-10-29 05:04:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce63a361-3496-3862-b404-773a5611e9ec | -12.11935 | -57.83385 | 2024-10-29 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 162fa704-3b42-3b46-946a-ed82eddbdf3f | -11.80892 | -57.36398 | 2024-10-29 05:04:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e765eb-25fa-3be1-94dc-39c17d26815e | -11.51528 | -58.41574 | 2024-10-29 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 748001a5-4ee3-3a0f-bc77-b77352acd825 | -11.40774 | -57.43693 | 2024-10-29 05:04:00 | NPP-375D | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6519a9fa-f700-392d-afcb-d4c7b829e5b7 | -10.53359 | -59.4252 | 2024-10-29 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dacb34a8-737a-3263-9e50-531435106a96 | -10.25518 | -59.21225 | 2024-10-29 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09e009ec-743a-3a71-9cc8-b2a4be0def46 | -11.48805 | -59.07245 | 2024-10-29 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cbc6ea6-1973-3990-a63d-17a23fcdc123 | -11.48423 | -59.09563 | 2024-10-29 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b669cb62-931b-33a0-ac3d-a42a54628f5f | -7.92695 | -61.55626 | 2024-10-29 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01d8786d-25bf-3cc7-bb00-2b1fbec4d5db | -7.6585 | -63.45304 | 2024-10-29 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91269379-8590-3112-8667-dc8f8d089ee1 | -7.658 | -63.4543 | 2024-10-29 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf24bf5-de11-348e-8367-efd10f0c8e73 | -7.65762 | -63.45818 | 2024-10-29 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6e5f27-e359-3cbc-b6e5-c428354c5839 | -7.65709 | -63.4594 | 2024-10-29 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74136eef-9237-3a1f-b726-cc96c2c22231 | -2.6666 | -49.2673 | 2024-10-29 05:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8b6f14f4-3358-357e-91e3-eec8b08dc3e9 | -2.6667 | -49.246 | 2024-10-29 05:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b0e9cffe-adae-3bc9-a62f-0789c222eef7 | -2.8145 | -49.2418 | 2024-10-29 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a8ea5f4f-71fe-3ad8-badc-3323c0f70de6 | -2.8146 | -49.2206 | 2024-10-29 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3592d40b-3a75-319f-9b1d-e81e99785fb7 | -2.833 | -49.2413 | 2024-10-29 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 3ecfcd94-dfb5-3ea1-a6c5-cb54f746a820 | -2.8331 | -49.22 | 2024-10-29 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |


[Clique aqui para ver as próximas entradas](README94.md)
