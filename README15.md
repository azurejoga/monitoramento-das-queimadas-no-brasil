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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f52f83c-22ec-3e3b-abba-c5791513e34c | -6.16238 | -48.05447 | 2025-05-27 04:49:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95c58e74-dfeb-3edf-ba67-c7a3f00cab57 | -7.6165 | -45.75987 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1943dad-8913-38c8-bc64-7befe8dbb67a | -7.19724 | -43.11112 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3d977e38-2362-35ec-b8d8-82513a8c0248 | -7.46677 | -47.05568 | 2025-05-27 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df2e1f25-8ca8-3382-8c81-29f5dcbe559a | -8.43164 | -46.64157 | 2025-05-27 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50f63a2a-75c6-3674-9f0a-61c9503fc518 | -7.56266 | -43.35898 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6544eda1-8bcf-3211-a9a9-8e293f4066d8 | -8.75426 | -49.75104 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 049cebbc-480f-3c2b-a7cf-c93cb5a18819 | -7.54982 | -43.37178 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7be2e0f1-609c-375c-a38f-8ac91ee0918e | -7.07786 | -43.55723 | 2025-05-27 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b6a0d29-ee56-34a1-86e2-0e17a46c3fed | -9.03289 | -47.74588 | 2025-05-27 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4744cb64-20d3-3c47-be85-1f0bf9c2ef00 | -10.63213 | -48.08601 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01a1498a-e110-37c1-9d42-78d63494753a | -6.22929 | -43.34965 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27be9710-b1b3-32f8-9090-75250e84cab9 | -7.62373 | -45.76746 | 2025-05-27 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6345d70-bac8-3d61-8439-43fc6d88df6c | -8.72333 | -49.38718 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cec99d97-e39d-3adb-99e4-4e7f1934241e | -7.22585 | -43.10794 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 53f87f1b-dd7c-3bd9-9105-80edd95f8594 | -8.75061 | -49.7505 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0cd04661-4f5f-3197-bd8e-30490408fb30 | -7.605 | -46.65004 | 2025-05-27 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 636fe331-5d62-3ace-b44f-ceabde54d2ae | -7.07614 | -43.55444 | 2025-05-27 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42ec0c2e-ed18-3f16-bf68-03ef2393bd97 | -10.23325 | -47.42739 | 2025-05-27 04:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad21b2b2-a839-37a1-90ef-98bbad9fda3e | -10.24797 | -47.60343 | 2025-05-27 04:49:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a57aff2e-adab-3d5e-badf-99b81e6767a8 | -7.58055 | -43.35025 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b72776a1-c4b8-3e14-b4d5-551b05b9376f | -7.56913 | -43.35228 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a9b066-caa6-321c-895e-01e493b7ba0d | -8.01675 | -49.68676 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48db25e1-bb1c-3c43-a0c4-49f4f6897739 | -10.3429 | -47.97762 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9407441-934c-3f08-b86d-4a75ae9ef4c3 | -6.21422 | -43.34018 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcd96b97-af45-38a3-b610-08b2ddefb399 | -6.22394 | -43.34883 | 2025-05-27 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b364c1d-9f3b-3a06-ad00-cecd4120d1c6 | -7.20728 | -43.12005 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 459e4e07-0a1a-3192-b30c-5ac02e9d32ab | -10.33875 | -47.97697 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98843f36-c086-3e7f-a424-416ae491c9f4 | -6.63771 | -43.21334 | 2025-05-27 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0ece47e-573b-3e35-83c6-7eb0703f17a9 | -10.36571 | -47.96579 | 2025-05-27 04:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7efe0986-ddde-3164-981d-0f0ec37f80b8 | -7.47762 | -43.36152 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3dca5dc-f235-3053-b743-82468bcb7e20 | -9.71828 | -48.32108 | 2025-05-27 04:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64360e60-58ca-37a5-9e97-1170a7fc9b32 | -10.52981 | -47.58695 | 2025-05-27 04:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d27d961-6773-3ee1-8727-d0a3f81821f0 | -9.15671 | -49.65446 | 2025-05-27 04:49:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 882f0be4-09ce-3f24-979c-a0ed33e7dd6c | -9.25191 | -56.32489 | 2025-05-27 04:49:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 189b4017-292f-3146-a296-0c68bb38efc9 | -7.23189 | -43.10508 | 2025-05-27 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d992888a-d903-3a8a-be6c-3d46b040d989 | -8.01611 | -49.69098 | 2025-05-27 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11cef796-7532-30b6-8a42-d86836cfafba | -7.54681 | -43.18404 | 2025-05-27 04:49:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 926a0b52-44ae-3b90-bd6e-cbee7235aeb9 | -8.38674 | -49.66194 | 2025-05-27 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0fa6e59-5b23-3af9-9ec5-32c575c783ee | -15.8757 | -43.4566 | 2025-05-27 04:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3800174a-7393-3038-8c62-a550915aaa53 | -18.8479 | -53.6251 | 2025-05-27 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 154.0 |
| de5cffb2-2bb1-31ba-a1b7-c7340b0d5ced | -18.8684 | -53.6003 | 2025-05-27 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cb5254ee-86bf-3ea2-94fd-6289150cdda1 | -18.8679 | -53.6218 | 2025-05-27 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5aafe969-c258-3e48-b063-274ee3eca033 | -15.8955 | -43.4523 | 2025-05-27 04:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 29e57087-26dd-338a-b3a2-6975def4c72e | -18.8484 | -53.6035 | 2025-05-27 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 115.4 |
| c38ddba8-c068-3b15-aa13-3924ad4adf86 | -11.56241 | -47.44307 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 788a0da6-8e01-3806-8b6d-ff60247616d9 | -13.09991 | -52.2898 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c96a287-4ab3-3d19-b5d2-678949078c67 | -11.57704 | -47.92833 | 2025-05-27 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b30a138-85fd-378e-befa-b17aa64a8fbc | -10.29334 | -57.1423 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ff888ab-41bf-352c-b6c3-d1a8b14c352c | -11.7546 | -54.23114 | 2025-05-27 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 166dbec3-f2b8-3f1b-a4bc-179e1b25aa40 | -15.89029 | -43.44753 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd8f6a4f-e6f5-3c19-b70f-a76c8c66d3ad | -11.81896 | -55.07951 | 2025-05-27 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd873c1-babc-3ae9-bfa1-134d8f443fad | -12.42398 | -49.97702 | 2025-05-27 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624290fe-2bf4-357d-8a31-f66bf22cabc3 | -15.88375 | -43.45136 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 83ee0bd4-6517-393e-80d8-025d63ef734e | -12.11685 | -54.665 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 974fcdd5-423f-369d-89ab-b46ab40ec5bd | -14.03352 | -55.12588 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97147b5-2af7-3406-8f15-c3599b063833 | -14.04567 | -55.13531 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa5c3c1-5936-30e9-99a8-4a5708eda575 | -12.64784 | -54.08121 | 2025-05-27 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e4c95ec-c029-323a-8bb8-fb5ec83bdd7a | -14.02021 | -55.12719 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503e3160-291f-3d9d-8288-17b2108d7eaf | -12.07158 | -47.35305 | 2025-05-27 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e95c09d3-9427-341b-b9f2-26306bd4e7b8 | -17.15236 | -54.00394 | 2025-05-27 04:51:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cb77b61-4fb7-3a3d-b836-6760ef7f9127 | -12.27002 | -44.5892 | 2025-05-27 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c714ab9-c839-3450-b364-ae0274db433f | -14.04281 | -56.05142 | 2025-05-27 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 097e25c2-53d3-3b60-8bc8-eaac7e9ad013 | -12.27333 | -44.58668 | 2025-05-27 04:51:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 593a80fd-5287-3d18-8701-b352c5e216fe | -14.1498 | -45.47341 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 296244e8-c96d-387f-9ebc-720c6cd6b046 | -14.14461 | -45.47274 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47dc94c3-7a6d-38e1-b587-b55c341b6c6c | -14.01791 | -55.14151 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a09b567a-3f33-3851-b6fb-4c823c271b80 | -14.02629 | -55.13188 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea975b3f-061a-3ee6-86d8-78c43d1d364e | -16.62855 | -52.13367 | 2025-05-27 04:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7cbcbd1-9385-3c2d-83a6-fdb1e062551a | -15.88931 | -43.45672 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 538006ae-265b-3ca8-bfb9-acbdb0fbb9f0 | -12.25035 | -51.44422 | 2025-05-27 04:51:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79f000fe-1cd6-3bd0-a19c-4841524bac2a | -11.5719 | -47.63041 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b82d1c4c-bfe3-3916-9b16-b35d0cb05f0e | -11.62407 | -54.93963 | 2025-05-27 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfeb9d2a-26ba-38f9-a0a1-c34d3fd1a5fa | -12.16734 | -54.26295 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bda5493-239d-3457-afc1-d3ba6f6cea6f | -17.8396 | -50.81279 | 2025-05-27 04:51:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3af1f58-5465-3bbc-abb3-6f5fc3e88f91 | -12.11742 | -54.66145 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9661cad6-8691-3daf-ab2d-1c06b341cb77 | -11.57336 | -47.92367 | 2025-05-27 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3865d716-fc29-3722-a26e-c302ccc33cb0 | -10.82054 | -54.01785 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae9c8cd1-2c00-33f9-890f-4ab9e8d57f5c | -11.57375 | -47.62917 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7efbd2-d4fe-3ec9-996b-691c0f308d5a | -10.81943 | -54.02488 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5bdf7f-3045-3678-bfc8-6b38737778bd | -11.13515 | -53.91803 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74ec93a2-e78b-3d8a-8b33-77d748ba5271 | -10.81667 | -54.02083 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 397c8146-4b91-3a49-a675-5f361ec61c9c | -10.83045 | -56.95715 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ee978358-c73e-38eb-9950-04ef07cea119 | -15.0788 | -48.94376 | 2025-05-27 04:51:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb26596-16ca-3ae6-8a7a-5c1e0b1dbd28 | -14.14903 | -45.47982 | 2025-05-27 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6712606d-f83b-3c7a-9d7f-3a688f23cf40 | -11.62742 | -54.94018 | 2025-05-27 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 898976e5-d3bb-38bc-aec0-02301e7e67b5 | -11.56181 | -47.44742 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7169760-9c13-39a2-ba9b-c5d120146a5b | -15.88425 | -43.44674 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bf6fb3f-a6e4-3e86-b213-a79735607e1b | -12.02892 | -57.10134 | 2025-05-27 04:51:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0869244e-c0ca-3e54-91b1-bff2313fbe83 | -15.88277 | -43.46058 | 2025-05-27 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9eb27045-771f-3e81-bf4f-285720b80a1b | -14.5929 | -48.35928 | 2025-05-27 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a30c126f-555e-3084-9304-423105f4c5ac | -10.81998 | -54.02137 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36b2ffe-a286-3a21-af70-d86a03d39e4f | -10.3361 | -57.48786 | 2025-05-27 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 949730bf-93fb-3646-9206-8a2e5375513e | -14.01906 | -55.13435 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24034627-201b-3bcf-8d76-4fd2b5d84eb6 | -11.57248 | -47.62622 | 2025-05-27 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62776f29-d744-3be9-b944-dec8e835579d | -11.86945 | -52.25582 | 2025-05-27 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8b313f9-93da-32be-93d0-0f2c28af6bbd | -14.04509 | -55.1389 | 2025-05-27 04:51:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9690bd02-aa03-3948-ba86-e24a91248694 | -10.8233 | -54.0219 | 2025-05-27 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 986fd6bc-7254-32af-9337-83b508958462 | -12.75659 | -48.34103 | 2025-05-27 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de235cf4-85ab-3d8d-9523-3182df735d65 | -12.11628 | -54.66856 | 2025-05-27 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
