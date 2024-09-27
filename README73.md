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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6d125f3-5afa-3780-9dbe-66005754aac8 | -2.35702 | -47.60926 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 731d5ccb-8f01-3e75-9d95-13bbeb83cfda | -2.35478 | -47.6018 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c826bcc1-79ae-3962-a55d-837e0a623105 | -2.35424 | -47.60528 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d500031c-64e6-39a9-8cda-87e6fd270319 | -2.3537 | -47.60875 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 049a9a62-4daa-32d0-ba36-d04f782fa198 | -2.35092 | -47.60476 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3bf94816-5ca7-3a7f-9d19-1d25fae8b48d | -2.35038 | -47.60823 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9883fbe5-2883-3b50-a793-af73adedd261 | -2.34065 | -47.97518 | 2024-09-27 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7618194-2425-3425-9db3-de3322ba4bf2 | -2.22445 | -48.23787 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f23b70ce-e71b-32d5-a870-70b91b9690e3 | -2.22391 | -48.2413 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81b6ad23-848f-30cc-816e-17913dd0c14f | -2.20659 | -48.15785 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ee25800-94f6-3a9d-90d1-7271ec431070 | -2.20605 | -48.16129 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dbc0e5f-17a6-384a-a29a-8b7a75f04b63 | -2.20329 | -48.15734 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d33cb87-72f7-35cf-887f-44a3bf04fb87 | -2.20276 | -48.16077 | 2024-09-27 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6f30c56-b184-32d7-b3c9-fe497eff6dd6 | -2.89975 | -47.88195 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d338b7fe-a52b-30a3-97a4-75df0c7baf7b | -2.89921 | -47.88542 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 709cf839-9d01-3250-ac2e-fc71f71e2f0d | -2.89643 | -47.88144 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb6b1fa-7572-3014-838c-c78688761612 | -2.89589 | -47.88491 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47537264-d41c-31fa-ba04-54bd8b8fb71d | -2.88595 | -47.88338 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13214a3e-00fc-3a3d-9c84-c6103abd8f5e | -3.46327 | -48.82291 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfbd1c62-e13c-3775-8d27-18a76ea6b130 | -3.45997 | -48.8224 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c071a37-0429-3ccc-8699-a8e6792bc74e | -3.25342 | -48.47062 | 2024-09-27 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a95da7ea-1ccd-3019-928b-259791ce8fe3 | -3.1356 | -48.61325 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07c2de5a-457d-3117-a596-0b1afe162731 | -3.09793 | -48.68112 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46305e94-8577-3b9b-855d-5e9adb6a3895 | -2.94964 | -48.73871 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec484c3e-b9c7-3dd2-8dc7-e0e59959a7ed | -2.93749 | -48.90194 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21370b7-a746-3418-8d77-d1aabbe5795c | -2.92261 | -48.88908 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d50a286-462d-38eb-a1c5-5730cef62fb0 | -2.91931 | -48.88857 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ea49889-7735-3327-acac-d5a4f0f17ba5 | -2.83173 | -48.59683 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa1278e-d2ae-3323-9709-1cbcfb5e9511 | -2.8312 | -48.60026 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b6454f6-e15f-3758-9210-d8c6bb0b4971 | -2.79486 | -48.57358 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa9b0b48-f42b-328d-ba6d-6e1cb1b52036 | -2.79157 | -48.57307 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 463638d8-182a-3eac-be8f-556b0c6fc1df | -2.78881 | -48.56913 | 2024-09-27 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 976ebab8-aa5f-37ad-ace6-5cc3094d9c24 | -4.86944 | -48.38594 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b707e55-0c2d-3ed8-b7df-fc476a323767 | -4.8656 | -48.38887 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68bf81c0-e2d6-3555-ba80-dbee19ee5427 | -4.80099 | -48.43141 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a00660b-486a-3f32-9784-63855e448608 | -4.77002 | -48.89297 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e3e565a-e3b5-3f34-b06e-19b69e902ceb | -4.76672 | -48.89246 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 534335bf-edb8-3588-9186-c8f17b5e2d49 | -4.76288 | -48.89538 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08033989-c224-352b-b048-19b74b4effe3 | -4.75514 | -48.89699 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a16e1c0-2187-399c-9e43-c028c44fee6a | -4.75131 | -48.89991 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bf987490-d26b-30dd-b413-7b2300ffe38f | -3.90081 | -48.35769 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c5a6ef-ade3-3aec-bbfc-4c39a44b555b | -3.89912 | -48.34686 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb72a203-0f34-3057-9826-ef8ba2ee04f3 | -3.89858 | -48.3503 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc84b4e1-5503-3374-9c4a-a8620f3b9256 | -3.89751 | -48.35718 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 354ca962-89de-3b58-baaa-c7387d0afda4 | -3.89582 | -48.34634 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fae5e8b5-f76a-36d6-84c1-a31b543beb63 | -3.8942 | -48.35667 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02419ea7-1792-3499-8720-1b2b35924cc9 | -3.89305 | -48.34238 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af3da885-febc-37bd-8fe2-8a2a817899c8 | -3.8909 | -48.35616 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c547fcab-2b28-3e28-94b7-837e7dd761e4 | -3.8876 | -48.35564 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bbbb572-5ac3-331b-af3c-e9689a939f64 | -3.88644 | -48.34136 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e42bd8a-50ac-393e-93dd-331dc0852d23 | -3.88598 | -48.36597 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e2265e7-784f-302f-86f1-817ff677f5e3 | -3.88314 | -48.34084 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2340706d-b6f4-3e38-b7f4-01f9fc2b7ea7 | -3.88268 | -48.36546 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70bf96dd-dd01-3eee-aff5-eb3eca3c3e29 | -3.88214 | -48.3689 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 388b022c-d9cb-3fe8-bec2-38b7a0b0fe3a | -3.87938 | -48.36495 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9906e93b-c9f5-36bd-a8c7-c267190ca6d6 | -3.87884 | -48.36839 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54e81bfb-6c0c-3b0d-af52-bb88ea1a5875 | -3.86112 | -48.97762 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a4a949-2868-35bb-8143-1a23110caee4 | -3.84793 | -48.97557 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554e8309-2f2f-3284-830a-f72d31fc4bbe | -3.84463 | -48.97506 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d826e0f-7013-34e6-b46c-4853015561c9 | -3.80763 | -48.90956 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95b365b4-faf3-3539-a681-7708bbd48ddc | -3.79282 | -48.91781 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d56f5e2-1ae8-3dcf-916c-a3e198fd9b62 | -3.72873 | -48.86859 | 2024-09-27 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c91441f-c30f-353f-a50e-0b4d1b964bdb | -4.94892 | -49.24837 | 2024-09-27 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bc3dcec-6e7c-344e-b49a-90ece1d24974 | -4.94563 | -49.24785 | 2024-09-27 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e024ce-07fe-3321-96c2-3a8d70fb4d59 | -4.63168 | -48.53604 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9097e408-ab91-36f9-be10-139ff730fcfd | -4.63114 | -48.53948 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b681a39b-b2ac-3dd9-a08e-af3592250d47 | -4.56173 | -48.00215 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3c06742f-ac1b-382b-8f8c-5b1d89049d36 | -4.56119 | -48.00565 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bceb29b4-ea0d-3558-8b7b-15a6788be0e0 | -4.41747 | -48.64318 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec93b935-4495-3363-962b-811031547842 | -4.41195 | -48.63527 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbdd1317-1684-3b6c-9fdd-b91f998a747a | -4.40865 | -48.63476 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89ae006a-94ff-3822-b553-c18e080f51fd | -4.40811 | -48.6382 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab314392-796a-3bd6-9c97-7373da6b4caf | -4.37473 | -48.67881 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39d7ff93-42f8-3653-999f-bae7e83ed7a2 | -4.37419 | -48.68224 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9588024e-8768-3363-8fa0-ead7f8e6667a | -4.37143 | -48.6783 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cbbaf70-8192-317b-ac22-9be6a4754732 | -4.3709 | -48.68172 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80b20756-2fa2-3d4a-b30a-7c09800eab01 | -4.36261 | -48.66988 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6851a264-067e-32b9-9f58-78f56c3e1c09 | -4.29045 | -48.65152 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a61e8f-deb2-35b0-83bf-0859cdc86b7a | -4.25283 | -48.15081 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 762a6683-79f8-3189-b811-eae70f3aa93b | -4.25059 | -48.14339 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f39d19a-d51b-32f4-acf5-cc29e09d2d49 | -4.25005 | -48.14685 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3818f0b-075b-3cac-bd30-e90758f9f0a7 | -4.22316 | -48.18889 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa0f3fda-a3b0-3cda-bf2a-e59153fe5d15 | -4.22 | -47.85918 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dec925aa-beaf-3c95-9506-91098ee2e86f | -4.21985 | -48.18837 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 720f0d86-0798-3c8a-992d-5795881bf5bb | -4.21931 | -48.19184 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ce63b0b-289e-3300-9176-4077a995b8b5 | -4.21666 | -47.85869 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abb354a5-f21d-3480-8bfe-08e8f88109e2 | -4.2038 | -48.61694 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af42c948-e854-32a8-b458-3652de5e0264 | -4.20326 | -48.62037 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2c659e9-7daf-3f91-9454-ffd0bc368d1e | -4.20272 | -48.62381 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20f0aac8-2f0d-35b2-b8d7-5f0ebdc74254 | -4.2005 | -48.61643 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 675c5096-5aec-3af4-9dcd-bfaee2a47171 | -4.19996 | -48.61987 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf552e14-4957-3c88-b1a2-44ebb237e445 | -4.19888 | -48.62674 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| daeb6500-6a9c-3eaa-b435-9f9d1748d9f5 | -4.19835 | -48.63017 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddce7f16-759c-3641-87a3-5299620aca60 | -4.19666 | -48.61936 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8660032-13b1-3921-887a-53e052331376 | -4.19612 | -48.6228 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d0b337-c862-33b2-a9dd-bea9c8b9bca9 | -4.19559 | -48.62623 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c93f6064-beb4-3ad9-8186-b1fefe867a16 | -4.19505 | -48.62966 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 73373b03-099e-3e00-aeff-86cd30429d25 | -4.19336 | -48.61885 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eeddbee-2469-3ea5-8f74-af908daf8c26 | -4.19282 | -48.62229 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33511253-14af-354a-a047-4a366e7e457e | -4.19229 | -48.62572 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README74.md)
