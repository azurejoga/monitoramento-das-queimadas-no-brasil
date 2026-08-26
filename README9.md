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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e9701bb-7359-3f1f-b880-c934639b5135 | -6.85525 | -38.3526 | 2026-08-26 03:13:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 522aaa69-034e-3bba-bb76-ea2f5ce962b4 | -8.08014 | -37.68765 | 2026-08-26 03:13:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa348eb2-d91e-35d4-997b-dd01a8ade41e | -17.69095 | -40.17891 | 2026-08-26 03:15:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3b49c70-9c73-3c6f-8a01-4dc92a26e4c1 | -12.80885 | -42.72929 | 2026-08-26 03:15:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| dbf30001-5024-35d1-bba2-02e8c1a7c4db | -17.69014 | -40.18276 | 2026-08-26 03:15:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b427ed2e-7331-3b94-ae6d-b3759097f71a | -14.7977 | -48.8074 | 2026-08-26 03:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8631b882-001f-3106-aa16-2bd7e35ed85e | -10.7784 | -54.0368 | 2026-08-26 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 49b42a26-9014-3f52-9209-768720d35017 | -6.6595 | -58.498 | 2026-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 383c9a0c-d380-316b-82b5-1138866ad1df | -13.2842 | -51.4541 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cc13f8e6-b879-3b46-a7bb-6c8a7c8646b3 | -7.5288 | -61.4015 | 2026-08-26 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| f5a52e03-1a75-3336-b9f8-12a1e119188a | -7.0613 | -59.2165 | 2026-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| e7984473-3d83-36e1-8e49-326323e132bd | -7.0797 | -59.2157 | 2026-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3d3ec5b7-2295-3c75-8e3f-834f0e44cb58 | -13.19 | -51.3593 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8f32d1cb-82d5-3451-9486-2ad9a1ee8ee5 | -7.0243 | -59.2181 | 2026-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2fed2c6b-3627-3bf8-ab44-bdf45c58cd5f | -6.2677 | -53.3565 | 2026-08-26 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ac7fbb42-b780-35d3-8d50-c11f6a51eab6 | -13.228 | -51.3759 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| ed6816a1-fbf8-3261-8cb7-0f3132580beb | -13.2472 | -51.3735 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2440d723-55a7-315e-a04b-087214c9e043 | -13.2277 | -51.3973 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c7df25ea-164a-3433-9de1-e7db6cefd550 | -7.0242 | -59.2374 | 2026-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3fce3460-4658-3cf0-a4aa-e6ff4ee138c3 | -9.6024 | -55.1078 | 2026-08-26 03:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f64edd19-a4c4-3743-9bf1-eca3e3dd205d | -10.7598 | -54.0179 | 2026-08-26 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| f485fd61-225a-3384-b9ec-7aa2529a53b1 | -13.2469 | -51.3949 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 036ddaf4-646e-36d5-bd2a-e3e662dc1090 | -7.5289 | -61.3825 | 2026-08-26 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 3033e5a5-2f52-37d7-b210-c9665c101e49 | -14.7981 | -48.7851 | 2026-08-26 03:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c3c43e76-9fba-3fff-8b85-ec32a470baf8 | -7.5104 | -61.3832 | 2026-08-26 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| d84289ce-3add-3395-9529-c85596c9701e | -6.6409 | -58.5181 | 2026-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| be6670a1-5729-3c7f-9537-b2ef0b01323a | -7.0612 | -59.2358 | 2026-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c6e1d0ae-ce31-3dbf-8853-54721941cd0b | -10.3727 | -45.0537 | 2026-08-26 03:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 71be2d95-c2d5-3fa6-805c-344ccd7b1fe4 | -10.7596 | -54.0384 | 2026-08-26 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 4658c9a8-8b0e-3d6b-92b3-896b53310aa7 | -6.641 | -58.4987 | 2026-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 127.4 |
| a62dfd00-14ab-3120-b2c0-12aa174b22ac | -6.6226 | -58.4995 | 2026-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5184dffc-5970-3517-987f-85c27cdffca7 | -6.2676 | -53.3768 | 2026-08-26 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 2c4378a3-fa6d-33fa-90b9-86610cc7fa61 | -13.3031 | -51.4731 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 111ad2cd-ef7e-37f2-82ae-34ac50b358b7 | -13.2839 | -51.4755 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 26c9d819-673b-38bd-b210-89aa4bd282c6 | -13.1903 | -51.338 | 2026-08-26 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| a21ac7ae-f407-319c-bb84-9302c24c110d | -10.7787 | -54.0163 | 2026-08-26 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| eadd0c79-5bda-31f2-aee5-f2abe9be0a59 | -7.0613 | -59.2165 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 29d2a18e-9c8b-3b37-8474-190788e317c7 | -6.6226 | -58.4995 | 2026-08-26 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 09faa495-ad31-39f4-8e8f-d7ee1e455bb9 | -7.0612 | -59.2358 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2127acb9-7326-3749-9209-b093be20f4d1 | -13.3034 | -51.4517 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 20f9ebbc-4c59-3a49-975e-7876076f7d5f | -10.7598 | -54.0179 | 2026-08-26 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| c55aaf5c-0239-30b0-857d-436e4dd8e2f8 | -7.5104 | -61.3832 | 2026-08-26 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 148.7 |
| d14a8947-a0cf-385a-9b97-6efa36bd5c2d | -7.0796 | -59.2351 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 20df5906-7fde-3116-895b-3c7987e67ee1 | -13.6614 | -51.8535 | 2026-08-26 03:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 32b928c8-4c7a-33b3-9e32-47af780e679e | -6.2676 | -53.3768 | 2026-08-26 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a292118b-ae86-3cf7-b2cd-4fa182937ff2 | -7.0243 | -59.2181 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ea29a4e2-4606-3837-8932-a9e5715bb6c9 | -7.0797 | -59.2157 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 48e20a96-82ab-3200-9287-8c6010485efd | 1.4734 | -55.9642 | 2026-08-26 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 39b8f0e2-b2b3-3c2e-ac98-21fe68d4ddd3 | -10.3723 | -45.0767 | 2026-08-26 03:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ae51ef12-6553-3e1d-9535-9dfdc27e9703 | -13.3031 | -51.4731 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 54828084-c5b1-35e3-8e37-6047fa0b7fd0 | -14.7977 | -48.8074 | 2026-08-26 03:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| cfab685a-8df2-3a73-b348-ad0af80281c0 | -13.1903 | -51.338 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0f05c3cc-c964-33ac-bf9b-21c08279b1dd | -13.2839 | -51.4755 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 8395e4e4-9e56-345d-8c16-3801eb0df702 | -13.2842 | -51.4541 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b9563bce-ebf2-3115-a7ea-d06d16bdcea5 | -7.0242 | -59.2374 | 2026-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5bfcc86f-1c2c-363b-b940-20559ed20ac3 | -9.6024 | -55.1078 | 2026-08-26 03:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 14b1bcf6-34e9-3bf9-8280-2c0b32284c60 | -6.6595 | -58.498 | 2026-08-26 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 165ae1b5-b4ae-3b09-8732-14e842bf653f | -10.7784 | -54.0368 | 2026-08-26 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e5edfb6c-f6da-3689-8e68-8898749cc9c5 | -13.228 | -51.3759 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a7328a45-d944-37c1-acc7-51e356b4b726 | -6.6409 | -58.5181 | 2026-08-26 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 69484967-b3d5-329f-8707-be4daa4a097a | -13.2469 | -51.3949 | 2026-08-26 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9185cbee-1b1b-3ab4-ac88-f0852ed7c362 | -6.641 | -58.4987 | 2026-08-26 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 60c71770-192f-3097-9042-66b35f376ff4 | -14.7981 | -48.7851 | 2026-08-26 03:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0db68d76-52b1-3142-9258-f4642369fcaf | -10.7596 | -54.0384 | 2026-08-26 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 197acc8f-9a31-3ade-8b53-8140175a1b74 | -10.3727 | -45.0537 | 2026-08-26 03:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ef2b7fe4-cf06-3dfe-bdf7-e933b01dc2c6 | -7.5289 | -61.3825 | 2026-08-26 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 159.3 |
| fbf6adab-fea0-3956-a692-c0aac8856a45 | -7.0242 | -59.2374 | 2026-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6178bf95-6fbe-3ddc-989f-76972007be7d | -7.0612 | -59.2358 | 2026-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 86e17797-a488-3064-881e-84c62c50736e | -6.2676 | -53.3768 | 2026-08-26 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f7e83b83-f4a9-3755-b032-fc5016ec27a2 | -13.2469 | -51.3949 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c16d5a1e-a3c7-3e69-940c-401625d7c6b9 | -6.6226 | -58.4995 | 2026-08-26 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ccaa1314-46d3-3ac2-8e61-f24208351639 | -7.0243 | -59.2181 | 2026-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e16a9483-321e-3ce9-b2ed-6081cf2b9f3d | -13.228 | -51.3759 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d64fba88-64a6-31f3-8c40-010d15f5a58f | 1.4734 | -55.9642 | 2026-08-26 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d13d6c41-6b3c-35e5-98db-8bfc7d3d6ed6 | -13.2842 | -51.4541 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f4715976-39e4-368a-9880-2314311957ca | -10.3723 | -45.0767 | 2026-08-26 03:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b08d106e-d25c-3492-b5b1-47e3bc95fa15 | -6.641 | -58.4987 | 2026-08-26 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 56dcf617-de56-3963-b6f4-7dfa8891716d | -6.6409 | -58.5181 | 2026-08-26 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a338f85c-5f07-3b85-83d7-4a5bddca254a | -7.5103 | -61.4022 | 2026-08-26 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0843e0e5-7432-3b2a-baff-f1d70c843142 | -13.2839 | -51.4755 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 284a90f8-a3f3-3286-8d77-8702233caded | -13.3031 | -51.4731 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 749b75a0-4b5a-33f3-afa7-5290e0104d00 | -7.5288 | -61.4015 | 2026-08-26 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e15d1e51-b407-355b-b34a-4d379df44d90 | -7.0797 | -59.2157 | 2026-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 21f75258-e4e7-395a-ae0b-baf5945eccb9 | -9.6024 | -55.1078 | 2026-08-26 03:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b11d4bcb-b1ff-36a6-96b5-519bfa63173e | -13.3034 | -51.4517 | 2026-08-26 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9223422d-5fce-3e24-818c-abf27a5f04d5 | -7.5104 | -61.3832 | 2026-08-26 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| d4de38d2-8227-38fc-abf5-d9c1973d71c3 | -10.3727 | -45.0537 | 2026-08-26 03:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0b75b36b-19f1-3c1d-9e56-c106f87b872c | -7.0613 | -59.2165 | 2026-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| fd7d6a86-4761-30da-b34d-ea82d05f61e1 | -7.5289 | -61.3825 | 2026-08-26 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| ad97572f-4d10-3e47-b123-7eb8cc76ac93 | -10.02203 | -46.42487 | 2026-08-26 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12300bf5-a10b-3ed7-bed7-cde9cef13bab | -7.756 | -44.76913 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dca8827-cd31-3155-9e07-9a9ad7b6db53 | -8.07832 | -47.50472 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c0916c-1f70-3b00-8ec9-1f00d499c0c8 | -7.31717 | -42.98889 | 2026-08-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31f07630-8b0e-3b6b-abd4-6cb594df499f | -8.13623 | -47.50217 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 53f45abd-7137-3792-8248-2fc6c0ab50f4 | -7.75771 | -44.75969 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e28790fa-6c3f-3a1d-9477-c3f8c0648723 | -8.07891 | -45.90194 | 2026-08-26 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc1deefd-246d-3740-a90d-afdbdbb2a8c5 | -7.76441 | -44.75639 | 2026-08-26 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc42bbd1-64e2-3e2c-b849-a05b507f211c | -7.1394 | -42.77528 | 2026-08-26 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b082dde5-f31a-3703-a7ad-f485a2f5a80f | -7.27432 | -44.07514 | 2026-08-26 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dc5e7c5-f451-32e9-a228-6ad4a34c18d6 | -8.13497 | -47.50863 | 2026-08-26 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README10.md)
