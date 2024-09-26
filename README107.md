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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc14dc68-4723-354b-828c-378a870afe9d | -2.6764 | -57.53122 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9bfb9cc-d94c-3ef0-96ad-a668cad18419 | -2.67414 | -57.52744 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9e41c153-8a60-31c9-a321-2f1dbbe84aa0 | -2.67335 | -57.52591 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f541185-17d2-31ae-9a92-717cb485e8ef | -2.67258 | -57.53062 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7e6a8d6-06c5-306d-a1f4-6513059fcf5f | -2.66575 | -57.53095 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 24bf695e-dc36-3953-ba05-e6535575adeb | -2.66501 | -57.53567 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ff8643b9-9b31-31ae-874b-887ca243522f | -2.66427 | -57.54039 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 87b3f662-d2f4-3f08-a957-1d6d4e79022f | -2.66352 | -57.54511 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad5445e8-e9d3-340e-88f6-571f3f238e4e | -2.66332 | -57.56306 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71599ae2-dae6-3453-bab0-bf2695272b3e | -2.66278 | -57.54984 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4db85810-2637-3493-9a5d-df614f2ceaf1 | -2.66203 | -57.55458 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 532179c4-bcd8-3dd7-8745-8503081527e8 | -2.66129 | -57.55932 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3c7e72a8-bc79-3d7c-9636-e0e1dec0f98c | -2.66054 | -57.56406 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 81eb9fe7-8454-34e5-b6f5-81d6bcadd942 | -2.66044 | -57.53979 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 13a4c1bd-90b6-3fd5-a6f7-54c86f7ddae4 | -2.59946 | -57.06725 | 2024-09-26 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a7db5d3-84c5-33e1-9d89-633975ccdb3d | -3.75046 | -57.20932 | 2024-09-26 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4d0d031-b7f5-3f8a-830e-5f1360ae2796 | -5.62403 | -57.43496 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f441e7-380d-3e55-830c-471c1e76fed0 | -5.62104 | -57.43022 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f56e343-82ac-3bd1-bb5d-db8cb96ccb38 | -6.84594 | -59.01851 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0759d9a2-a2ef-3d38-8440-deb1c018ec99 | -6.82586 | -59.04153 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53519e20-506d-3bb8-9d61-0842893c3f0a | -6.70515 | -58.92022 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6538b53c-338a-3658-9ce8-028fcd67c9be | -6.7043 | -58.92524 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d343a5ea-6c46-3350-9f48-969424506d07 | -7.47147 | -58.69423 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd1282c7-27e3-3e4b-adb8-05b06350e9c2 | -9.01195 | -58.98795 | 2024-09-26 04:57:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae4dca4e-6e22-3a7a-95f8-90a2a76b1f8d | -8.89123 | -58.365 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb25d98e-63a3-3e10-b595-2c4fb3ac51a7 | -8.88826 | -58.36009 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a859a01e-fc39-33d4-ac8f-fb89a90d35dc | -8.88456 | -58.35956 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64b2f54c-c3a0-3fd3-bcd7-aace49dc491a | -8.87642 | -58.36286 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de6e9a87-d2fc-356b-9327-41d638ce0f5d | -8.87568 | -58.36726 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd872e88-5887-3ae1-92d6-21c54c414af7 | -8.81444 | -58.21828 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd59e8c0-7487-3753-b288-99dc67abaa59 | -8.81374 | -58.22253 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f2c89e42-be06-3005-80d5-f675ab883b69 | -8.81303 | -58.22675 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 31204c71-b7fc-3362-b776-23050da72887 | -8.81078 | -58.21769 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ff635463-edd2-3238-9dbf-a6dda02e1b92 | -8.81007 | -58.22195 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| df84c77c-3a36-3aeb-a21d-a233aea4c941 | -8.80937 | -58.22616 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 865bdd91-d598-3188-8a28-a656c8591fa4 | -8.80712 | -58.21708 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3e2927e9-1cea-3e86-aff9-b9f427513f47 | -8.8064 | -58.22136 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c514b218-e3e9-30b2-a6c9-755009263004 | -8.8057 | -58.22557 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| adeb1803-b50a-38bc-9b3b-83335b01bae4 | -8.80499 | -58.22981 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a45401c9-a55e-3275-9564-828f4b9475d7 | -8.80427 | -58.23412 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a36488c7-0049-3530-893e-36da69ba4f97 | -8.80346 | -58.21647 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02e665a2-0c23-365b-b8a2-7f138531db16 | -8.80203 | -58.22498 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2868baf-c246-35c0-828d-96b6e0935571 | -8.79608 | -58.19318 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c02bbe15-7516-3d1d-8e3b-43ecddbfa818 | -8.79471 | -58.22375 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 965d46a6-37f0-312c-9e51-93c4a3830454 | -8.79314 | -58.18826 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a31425c-6d51-3035-a945-2009d3dbd12e | -8.79242 | -58.19258 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67086852-011e-3ff9-8357-06a38ff8a3f9 | -8.79105 | -58.22311 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd4b0126-2ef8-3191-93db-23cea6a508be | -8.7873 | -58.17835 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c646530-7250-38c0-9cdb-f26bfca8a85f | -8.78445 | -58.21759 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05858f8e-6eb4-3008-8787-e6e986bae66c | -8.78366 | -58.17767 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6367f1-981d-30c7-b8ef-1d8a651a908a | -8.7808 | -58.21693 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b30dbcc-8976-32cc-8e7b-f5b4a8fe136a | -8.78073 | -58.17276 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2bd77e6-3ea0-307b-86bf-1c8382b112fe | -8.78009 | -58.22117 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9c0ab28-4074-3407-9cfa-e2ab650c64a6 | -8.78001 | -58.17698 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40e21f51-2923-30fb-be65-4f7d98bbbb26 | -8.77786 | -58.21204 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d4b7423-a7fe-397d-8171-06fa7987244a | -8.77714 | -58.21628 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67ecb926-dffc-3dd8-9347-4511a3f5aa3e | -8.77708 | -58.1721 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51348998-a0a3-3442-adf4-41bcef7e027a | -8.77675 | -58.17361 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 63e5bb16-d96c-3524-a361-a629af859342 | -8.77421 | -58.21139 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43f810a6-4066-32eb-ae3d-271d4bc368e6 | -8.77344 | -58.17146 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c0252a8-bee4-3b7b-aa41-59c1227267de | -8.77311 | -58.17295 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b7f1013-a2fc-3899-a6a7-45c5d96f8f01 | -8.77273 | -58.17563 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b55f7f4c-f20e-32ff-b284-8fc03a6e5ebe | -8.77113 | -58.20807 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7963dc2-97d5-33cf-9bdd-49a7e4ae11ca | -8.77055 | -58.21073 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 23cca158-981a-3be4-a387-9c13ccc43b8d | -8.76983 | -58.21502 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f2e5263-e506-3754-a977-b4577cca118e | -8.76973 | -58.21667 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cc91910-3daf-32ee-9c15-96d828079cb7 | -8.76946 | -58.17232 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70e21945-6b35-32ce-be26-036ef36e3248 | -8.76908 | -58.175 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a10bef2-35d4-319d-869d-1fa6196ae6a8 | -8.76762 | -58.20581 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a23b86e-1cee-3d16-9438-69c77ea0354d | -8.76748 | -58.20743 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33051fdb-c8cb-3eba-af6b-074fa95f0c3b | -8.7669 | -58.21009 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5999ea3a-d45a-33c3-a0c1-63703013f3d9 | -8.76512 | -58.17589 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a182fdf8-093d-38ea-8557-6501b2dda9cd | -8.7623 | -58.19308 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd944cf3-6c58-3e37-8417-cf7026e4842d | -8.76159 | -58.19748 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b6d93d1-187a-3938-bcf3-f92bc1afe3bf | -8.76087 | -58.20182 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec9a516c-ced9-3dc4-b87f-83ec78471493 | -8.75865 | -58.19246 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d37e06fb-616d-39c2-818f-63989bcd6ff2 | -8.75711 | -58.17894 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c53798cc-c9f9-31ee-b97b-0ae73d2369b8 | -8.75641 | -58.18317 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 68d92e35-9868-3dcc-ab82-6a6fb9c5f0e0 | -8.75571 | -58.18744 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 877eae79-509b-3567-bf4f-cde06cb9c3eb | -8.75275 | -58.18258 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| adb9be76-457c-398b-874c-7d90c8a09348 | -8.74472 | -58.18572 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38bc6fa0-018e-307a-8705-f01ca24e8a42 | -8.74387 | -58.16811 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a89d2e0-81fc-3158-aea0-c745d4e86ff4 | -8.74115 | -58.20741 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38f1af16-e2ea-3049-a2be-835b44e02244 | -8.74091 | -58.1633 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d781056d-4df8-356f-a984-5aab237cea0c | -8.69715 | -58.20034 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 631294bf-d9e4-3432-8d51-f1055370c275 | -8.69349 | -58.19974 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ead9759-2efb-3d0f-8e89-50e6c0808216 | -8.69137 | -58.23492 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f762667d-c653-398d-b0a5-553a1b3b2299 | -8.6891 | -58.20347 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f3dc74b-3cec-31b6-8edd-bcb7f522dccf | -8.6877 | -58.2343 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d85d698-60c4-3d10-a7b8-3578a8f0b727 | -8.68698 | -58.23862 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcc6b7e6-42ff-3d0a-ac00-07d975130d0d | -8.6862 | -58.22079 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ba8fac0-eaca-3fec-abd1-0780744abc88 | -8.68403 | -58.23372 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a0ef005-0bbb-37d1-9629-b83e32fcc425 | -8.68253 | -58.2202 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55267748-3c74-3e42-a574-90c95a14cf88 | -8.68113 | -58.27353 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 061d0485-2e08-39f4-8553-769e02461ee7 | -8.67959 | -58.21526 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e2f917e-cf05-3602-b335-ad81dc0dfb68 | -8.67886 | -58.2196 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 408c9033-1eec-3667-bed0-08da074e46af | -8.67746 | -58.27286 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beec8e7e-d325-3d0d-bf4c-167873c8780d | -8.67592 | -58.21465 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe0f9cf6-beff-360c-857c-c8184baeb202 | -8.34331 | -58.1813 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bdfe5f3-7573-39af-9950-96ff9ca57d20 | -8.29813 | -58.77017 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README108.md)
