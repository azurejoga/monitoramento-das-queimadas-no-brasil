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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d07332de-809d-3382-bacc-ae2ffcaae9c3 | -17.28103 | -57.5068 | 2024-11-03 05:37:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e9c95b52-316a-39a4-a570-0d1a28d2bc6f | -17.28068 | -57.50993 | 2024-11-03 05:37:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5d33d488-954b-3405-b333-95f6e2c8d67d | -1.0441 | -47.9272 | 2024-11-03 05:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| bb4c3bdb-e59d-35c3-8e99-41ec7e788d26 | -1.0441 | -47.9055 | 2024-11-03 05:45:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b990a586-0f6d-3d5e-8f10-f2b2218ed446 | -1.0626 | -47.9269 | 2024-11-03 05:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 021dda5f-ef08-3832-837b-db0f0f769e08 | -1.0626 | -47.9053 | 2024-11-03 05:45:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e0274999-cf6b-3634-a749-b050051cc445 | -1.2755 | -53.4138 | 2024-11-03 05:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 30b9a46d-6db8-39f2-a891-7851a9c3bd87 | -1.2755 | -53.3936 | 2024-11-03 05:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ceb316c8-1909-389a-8bd5-c9154798461a | -2.5796 | -53.3927 | 2024-11-03 05:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ecdb6028-afc3-3dab-a209-3b8fca399563 | -2.5797 | -53.3724 | 2024-11-03 05:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 35a648dd-97f0-372f-833a-4ce83c9baab6 | -2.7419 | -54.4353 | 2024-11-03 05:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| ccf235c3-4403-3573-81b6-7c8cd39684a7 | -2.7419 | -54.4153 | 2024-11-03 05:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| b5596993-cf57-3f50-a9f4-cf31bbfdc480 | -2.7602 | -54.4349 | 2024-11-03 05:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 179d89b3-2095-302d-9fb1-2afd4a79b49f | -2.7603 | -54.4149 | 2024-11-03 05:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 1f4be678-26bc-3d61-acef-534cdaaf30ca | -3.1059 | -50.3105 | 2024-11-03 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 796f6be6-b756-31ab-874b-08add4b7c79b | -3.106 | -50.2896 | 2024-11-03 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 8dab9544-957a-39b1-b052-373a90f6b127 | -3.1061 | -50.2686 | 2024-11-03 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d9a13c78-a550-308c-af17-583ddd75862e | -3.1245 | -50.289 | 2024-11-03 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 200ffdfd-0999-3dc6-8fd4-99eef0fa81cc | -3.1501 | -48.5689 | 2024-11-03 05:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bc10fec6-6b89-3e6d-afb2-9fe34c7b0d25 | -3.2168 | -50.2861 | 2024-11-03 05:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 9bdc5abb-3014-339d-bfc8-b431570b385a | -3.055 | -54.1474 | 2024-11-03 05:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c976cfe2-5319-3a99-ae4e-0383bd1febbe | -3.0734 | -54.167 | 2024-11-03 05:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 266f813a-8364-3573-9cbf-1a074a942c12 | -3.0734 | -54.147 | 2024-11-03 05:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| db810f04-194b-3316-9fd4-00a667443ff0 | -3.9473 | -48.3666 | 2024-11-03 05:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7777e6cb-419f-391b-9ae1-a53eb0126b73 | -3.9474 | -48.3451 | 2024-11-03 05:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 37f77704-9ca6-3928-9eab-608b2acb9a8e | -6.5239 | -41.4929 | 2024-11-03 05:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 148.7 |
| f9a0093b-fe5b-3628-ab77-dd55f743e70f | -6.5241 | -41.4688 | 2024-11-03 05:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 1821639a-9f87-3c3f-afc1-69895fc8341e | -1.0441 | -47.9272 | 2024-11-03 05:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 7d6342e8-f92d-3c67-98c0-3a0eb81cb4f5 | -1.0441 | -47.9055 | 2024-11-03 05:55:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 002a1ab4-e3bf-32a7-af9c-0e7350a5585c | -1.0626 | -47.9269 | 2024-11-03 05:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 0def1ed0-7cd0-3cc3-b8fb-593efcfb4862 | -1.0626 | -47.9053 | 2024-11-03 05:55:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d8322378-8e18-3796-9cb2-6676fb2293cd | -1.2755 | -53.3936 | 2024-11-03 05:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4916fa68-54dd-3b0d-a17c-6e4ffde5f2d3 | -2.5796 | -53.3927 | 2024-11-03 05:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 4f92dd4a-c7b9-3186-b403-e0771726fd00 | -2.5797 | -53.3724 | 2024-11-03 05:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 3ed8a63b-1799-387d-ae66-8225b403080b | -2.7602 | -54.4349 | 2024-11-03 05:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 6e41399c-100b-38f0-b829-c8a92b27322d | -2.7603 | -54.4149 | 2024-11-03 05:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3e1b8acb-5742-35ba-9174-9eb273b4bf1c | -2.7876 | -51.6099 | 2024-11-03 05:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cdebd9d0-8b61-30f0-80c6-c5acbf065660 | -3.055 | -54.1474 | 2024-11-03 05:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 1869762d-befe-3445-9b6b-d196b94a52d4 | -3.0734 | -54.167 | 2024-11-03 05:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e51484d5-7ab2-33e3-b528-3736121ac560 | -3.0734 | -54.147 | 2024-11-03 05:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fdff5e54-7a4b-3711-9bb1-c1788de53426 | -3.1059 | -50.3105 | 2024-11-03 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 092aebde-5b46-3e31-b806-a87de4ead00a | -3.106 | -50.2896 | 2024-11-03 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 882d9599-1fef-3f45-8df4-f21d90c00fcb | -3.1061 | -50.2686 | 2024-11-03 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 96a46e43-d904-3ac2-8f8b-1f9be5f2c61b | -3.1245 | -50.289 | 2024-11-03 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 115be3c4-a5e9-3fa0-9b03-7f4e601a9ddc | -3.1501 | -48.5689 | 2024-11-03 05:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 726b8f15-f3f0-379f-952e-008d0673a8a8 | -3.2168 | -50.2861 | 2024-11-03 05:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 5d356442-c71e-3bd4-a781-2ec2dcf86342 | -3.4749 | -50.3826 | 2024-11-03 05:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| c93b63c9-ed95-375c-87d9-6f51b9d1c407 | -3.9473 | -48.3666 | 2024-11-03 05:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d96ebb9d-a154-3139-b7b1-b335b0473fca | -3.967 | -48.15 | 2024-11-03 05:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0c9d3293-53b9-35c3-b0b0-74026b89cb6b | -6.5239 | -41.4929 | 2024-11-03 05:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| bb8cd761-f36c-3ccc-ad0c-20f97903dd2c | -6.5241 | -41.4688 | 2024-11-03 05:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 323f1464-5d62-3f7c-8371-7725e2ac77ea | -1.0441 | -47.9272 | 2024-11-03 06:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| be56fd9e-bdbe-3634-bd18-c85fbd6c8d67 | -1.0441 | -47.9055 | 2024-11-03 06:05:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 655389af-38e7-371f-95df-bb3ce1dd4a4d | -1.0626 | -47.9269 | 2024-11-03 06:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4693a884-c757-3cb0-9963-ca0d56dec47b | -1.0626 | -47.9053 | 2024-11-03 06:05:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 929bc1a9-1734-3c8a-9c24-8499ddbc8c73 | -1.2755 | -53.3936 | 2024-11-03 06:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9d8fc69c-c87a-31e7-b747-36a75dc0c2e4 | -2.5796 | -53.3927 | 2024-11-03 06:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 996f964b-3a31-30ef-8b5a-3183710c97e1 | -2.5797 | -53.3724 | 2024-11-03 06:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| ffe267a7-c5d6-33e1-942d-27525c4e6bb6 | -2.7419 | -54.4353 | 2024-11-03 06:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 01b2c108-8ea9-3d27-ba0d-730beb13bfe4 | -2.7876 | -51.6099 | 2024-11-03 06:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 2ba55b18-8868-3205-829d-505a7ee429da | -3.0734 | -54.147 | 2024-11-03 06:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 124cc9a5-af8e-3e44-a9f9-2dd7d0981138 | -3.1059 | -50.3105 | 2024-11-03 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| dc45dd32-6c0c-3393-98a9-c4aa218138fc | -3.106 | -50.2896 | 2024-11-03 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6d3082a0-d050-3786-afbf-cd461579dd6d | -3.1061 | -50.2686 | 2024-11-03 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0f062de1-c4f2-3dda-a0a5-0fbcb5da03a1 | -3.1245 | -50.289 | 2024-11-03 06:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7ac04bdd-a2ec-317f-ad71-9eca50a25de9 | -3.1501 | -48.5689 | 2024-11-03 06:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e55f4657-0fc3-325d-92dc-ff8d44797399 | -3.4749 | -50.3826 | 2024-11-03 06:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e0fc47db-e7e0-3f48-ba1a-4e568f1cf880 | -3.9473 | -48.3666 | 2024-11-03 06:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 197043ec-f510-3689-b1e0-1f90b4dbcf20 | -3.9474 | -48.3451 | 2024-11-03 06:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 06340042-53be-37a7-91e9-03c2458db4f0 | -3.967 | -48.15 | 2024-11-03 06:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1a23ed89-5b89-326b-9b18-abc0f7365847 | -1.0441 | -47.9272 | 2024-11-03 06:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 02f1c179-0c8d-3d83-a914-a1b328711ed5 | -1.0441 | -47.9055 | 2024-11-03 06:15:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 0f7a9352-4bf3-3ddb-91b9-e5c9a4c571c6 | -1.0626 | -47.9269 | 2024-11-03 06:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 58208a73-c55a-35f7-9287-192139558ec3 | -1.0626 | -47.9053 | 2024-11-03 06:15:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d0c85c89-7a5b-323f-998c-7802a33cd01d | -1.2755 | -53.3936 | 2024-11-03 06:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| feda51e8-bbcd-3362-9214-8026e5894844 | -2.5796 | -53.3927 | 2024-11-03 06:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 584a1b9c-0eb5-3579-944c-ceda32ea5d4e | -2.5797 | -53.3724 | 2024-11-03 06:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 729e110a-ae18-3696-a14e-02d21cfb1901 | -3.055 | -54.1474 | 2024-11-03 06:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d00ea21b-af78-31bb-9f61-5ff256ec38fa | -3.0734 | -54.167 | 2024-11-03 06:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2a2f4713-d486-3be2-a666-dd6494b226d6 | -3.0734 | -54.147 | 2024-11-03 06:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4d956b6b-fa1b-354e-916d-54bc0402cb5d | -3.0875 | -50.2901 | 2024-11-03 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6d0c9576-9593-3de3-b327-24d3693327b3 | -3.1059 | -50.3105 | 2024-11-03 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b18df616-2b98-38a9-be15-2053f9afabb5 | -3.106 | -50.2896 | 2024-11-03 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| e71fb0c8-9d38-33a6-9461-272269c1c9b9 | -3.1061 | -50.2686 | 2024-11-03 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 32f3631b-5ae5-3ff6-8df1-02d19e731f38 | -3.1245 | -50.289 | 2024-11-03 06:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 45e47878-2be5-30d9-acec-0e2e21fc9851 | -3.1501 | -48.5689 | 2024-11-03 06:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5839de85-28d4-337f-815e-156cc8fd4c5a | -3.4749 | -50.3826 | 2024-11-03 06:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 76714abd-7e10-3c32-af2d-b9c91ab86708 | -3.9473 | -48.3666 | 2024-11-03 06:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 014225a7-2eb0-3e6e-bb8e-4063969513cf | -3.9474 | -48.3451 | 2024-11-03 06:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cc9ddc1e-8117-3f86-82c5-741bf6186cd1 | -3.967 | -48.15 | 2024-11-03 06:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 9da2f375-5b1c-3945-b5cb-39010396b83d | -1.0441 | -47.9272 | 2024-11-03 06:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 016e64f8-517b-3c70-8290-f2b275eade88 | -1.0441 | -47.9055 | 2024-11-03 06:25:12 | GOES-16 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 30d3062b-d1c2-3883-841f-f7e51abbd4b2 | -1.0626 | -47.9269 | 2024-11-03 06:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1c09317b-65b2-3321-ad68-078c90ff60e5 | -1.0626 | -47.9053 | 2024-11-03 06:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4ad5399f-0c03-3e38-b1ae-c4bad9ee167b | -1.2755 | -53.3936 | 2024-11-03 06:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fcd88a88-a54c-3cd9-bf34-f6d3025eebb4 | -2.1746 | -53.6834 | 2024-11-03 06:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 086c698e-fcff-357e-bc64-c1577b88f4f7 | -2.5796 | -53.3927 | 2024-11-03 06:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 01616a74-2080-3237-a844-0ac0f1e7230c | -2.5797 | -53.3724 | 2024-11-03 06:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 12010ee1-18f9-3c52-bfb9-887a034b3d52 | -2.7602 | -54.4349 | 2024-11-03 06:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 0ac05434-b2fa-33f4-ab8a-04469c70a4bb | -3.055 | -54.1474 | 2024-11-03 06:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |


[Clique aqui para ver as próximas entradas](README90.md)
