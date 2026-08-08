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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beb9b590-1444-32a3-81ae-b4b344b424e3 | -14.3422 | -54.9929 | 2026-08-08 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| bdd19227-327b-35b0-bc6c-6d9463378012 | -11.1838 | -54.838 | 2026-08-08 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1995a7af-9ff2-3a3a-b100-fd2a31ea7c30 | -0.9797 | -55.3962 | 2026-08-08 14:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 22613aee-ebe4-3d71-af0b-41eae01ffbed | -6.8784 | -58.9343 | 2026-08-08 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| b934ab79-5944-30d9-8631-6506790c295a | -11.1583 | -45.9323 | 2026-08-08 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4fc7099b-913d-316c-92f9-b6411767d9c3 | -8.569 | -45.4024 | 2026-08-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 8c7b8912-09f2-3284-963d-5f2b42d845db | -11.3099 | -44.8569 | 2026-08-08 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| c7893c66-a1eb-3761-8a49-bd50ab2eb740 | -11.2026 | -54.8363 | 2026-08-08 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| c6c10a65-cde0-3337-8eb9-fc99c60a50f0 | -15.4039 | -53.8047 | 2026-08-08 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 59da07ec-514b-3cbf-9753-4881d572388c | -7.3562 | -42.8666 | 2026-08-08 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| cb774a6e-1a20-373d-ad21-be22c8275fc6 | -17.8805 | -40.0424 | 2026-08-08 14:30:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 585.0 |
| ad3c301b-b96f-356c-b846-573e9e17cc91 | -15.6968 | -54.8534 | 2026-08-08 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| dc79145a-fc70-330f-a8fc-9c6d4e6d176c | -7.223 | -42.974 | 2026-08-08 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| c32ac3df-effe-3cbe-9f89-997036f812f8 | -12.342 | -53.1625 | 2026-08-08 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 7d480078-02f0-3d7a-819a-d1ad4bd08feb | -7.3751 | -42.8647 | 2026-08-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 7698bf53-55e3-35eb-9359-7d5ee64a6c80 | -14.3422 | -54.9929 | 2026-08-08 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ee21fe09-6fa2-3231-b90a-21713022b93b | -8.5501 | -45.4044 | 2026-08-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 228f7d9e-3ece-3dd9-bd2d-9432f6cdebe8 | -15.1124 | -52.7257 | 2026-08-08 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fba1a0e5-7b43-3c0a-a2cc-41edfbc0434f | -6.8599 | -58.9351 | 2026-08-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6b0210ba-8c44-34ff-a2a5-29404e7e109b | -7.2233 | -42.9505 | 2026-08-08 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 836c0da8-0419-3ce8-909b-25fe457d3917 | -15.6972 | -54.8326 | 2026-08-08 14:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 437e1c93-3cfa-3176-b6bb-c72d32659235 | -11.3099 | -44.8569 | 2026-08-08 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| a06f0af7-4aec-3d3d-ba4b-6c653e99d76e | -15.4039 | -53.8047 | 2026-08-08 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b87ba0af-d7be-3397-b14f-82c9829a0b19 | -12.3423 | -53.1416 | 2026-08-08 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| cbea690a-44d9-3d0e-8a23-a1d59cc70aa4 | -7.3562 | -42.8666 | 2026-08-08 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 3c7db56f-5c70-33b8-8091-9496feee8971 | -6.8784 | -58.9343 | 2026-08-08 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 4f109eda-ee9a-32b1-bd25-5e8603e72270 | -15.112 | -52.7469 | 2026-08-08 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4563f07d-6ec8-3287-8a52-868bba91e2c5 | -11.7012 | -50.1479 | 2026-08-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 3c93945e-1cd8-3cc4-b259-576f8f6a7cca | -15.093 | -52.7283 | 2026-08-08 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 883af822-57fd-38c7-a6b1-cfbba0dc5027 | -17.9007 | -40.0367 | 2026-08-08 14:40:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 51a8257f-ec6d-360f-8ece-e82626cb1070 | -14.9254 | -48.2523 | 2026-08-08 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 157.2 |
| f604ccd6-8694-38ad-8b12-ba4f0028ba93 | -17.8805 | -40.0424 | 2026-08-08 14:40:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 468.0 |
| 6ae87a58-37bf-3a17-a5c8-f2ebe6dcb254 | -17.8797 | -40.0685 | 2026-08-08 14:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 178.8 |
| 88db89b4-dde7-3a7b-a003-67ce86670496 | -15.6968 | -54.8534 | 2026-08-08 14:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3f8da13e-fe50-3dd2-85f2-98dff4d78543 | -8.569 | -45.4024 | 2026-08-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| c6c08da3-af8d-31af-99d0-cc628b48d777 | -11.7015 | -50.1264 | 2026-08-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4f519428-9754-3c17-a8e1-bc38efac5fe6 | -15.0926 | -52.7495 | 2026-08-08 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 0c025cac-01b7-35ed-ab4d-678b46628d26 | -14.925 | -48.2747 | 2026-08-08 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 696dded7-9942-37aa-9f3b-f2d3e732eff1 | -15.3848 | -53.7862 | 2026-08-08 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 89b3f0ea-9923-3613-a260-e015c8851dcd | -10.9213 | -50.2785 | 2026-08-08 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d4ae4a4a-0a81-3b2a-a5ef-d31b3a8d2082 | -11.2026 | -54.8363 | 2026-08-08 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 23073b2c-abff-395f-ab18-21e57f6bcc37 | -8.6573 | -45.8686 | 2026-08-08 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9a6477d6-fc2a-3e95-904c-a9a361e3dba2 | -0.9797 | -55.3962 | 2026-08-08 14:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b3ecc2f4-7eb0-326d-a7bd-4a90b44eeb91 | -7.223 | -42.974 | 2026-08-08 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| d0c53a1b-7514-3701-adc3-396a84bffcb6 | -12.342 | -53.1625 | 2026-08-08 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| e10eff14-1759-37ad-89bb-89ea2ce62cec | -7.2042 | -42.9759 | 2026-08-08 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 163e51fe-a08a-3237-a38e-2cb38569b6d7 | -7.3751 | -42.8647 | 2026-08-08 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| d3a6470d-8073-33dd-982a-f288731da543 | -11.6824 | -50.1286 | 2026-08-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 9bbf8e0f-7461-3a77-9d18-f98a53d16e1a | -11.3103 | -44.8337 | 2026-08-08 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |


