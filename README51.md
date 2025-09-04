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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a1435d0-6183-3f87-bbe4-1da3a8812ec0 | -16.07849 | -43.62472 | 2025-09-04 04:29:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7dc5100-0994-30ae-9998-31a3721a9e84 | -17.72495 | -49.79771 | 2025-09-04 04:29:00 | NOAA-21 | VICENTINÓPOLIS | GOIÁS | Brasil | 5222054 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d44bf0-37ed-3dd9-bc5d-04851ee7d47c | -17.16089 | -46.25123 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a47f53f7-637d-3d57-b50a-57de37d15605 | -20.08809 | -44.14021 | 2025-09-04 04:29:00 | NOAA-21 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9d1100b-52f7-3a5e-bee4-fb1ec42d6cea | -15.46168 | -53.00479 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7609b17-f3eb-3f1f-bab0-d88127fc1f0a | -16.46736 | -49.5106 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f1548b1-5fca-3136-8229-572029cb9fdb | -20.92908 | -46.98181 | 2025-09-04 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc07ed7a-97d3-34ca-847a-601ed3d30659 | -19.23643 | -48.67941 | 2025-09-04 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b57ef271-7d14-3433-9612-1fe66218e6d6 | -17.17198 | -46.22373 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16935309-a904-3d1f-ba48-861bd79d0593 | -16.31864 | -52.95965 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9069622-b5da-3f49-aaf7-c2fe1d91c3f9 | -16.53434 | -55.08585 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 822afd4d-461b-35c5-a875-92166e909780 | -19.69338 | -49.35268 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b8ae60d-5ee9-30b1-a12d-0b6e8c679e32 | -17.16498 | -46.2477 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68b008a2-4284-31f0-9c05-948f0e9f3a0d | -20.07808 | -48.27952 | 2025-09-04 04:29:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a5084d5-0787-3cb7-a62b-2f851744128e | -20.3531 | -50.70724 | 2025-09-04 04:29:00 | NOAA-21 | SÃO FRANCISCO | SÃO PAULO | Brasil | 3549003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b150234d-989c-3761-ba7c-4cbadf32e39a | -17.05356 | -46.44253 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20a1047b-06da-3649-aa05-1ef02d5d1deb | -15.24389 | -53.80576 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0006ac09-c711-3b3d-b7bd-112a389f876f | -15.17267 | -52.35881 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0539de07-e0bd-3369-9a6a-28486fd00b81 | -15.73562 | -53.642 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82f9d077-e75b-3dba-846b-3f68794d3db3 | -20.33794 | -54.0695 | 2025-09-04 04:29:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 315c3518-68c8-3a00-891a-57afb4fd3c7e | -15.18345 | -52.34977 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8dcb5a2-0e0a-332d-8fd1-c4042395e822 | -15.55112 | -48.39696 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b700806-7aef-3b6e-bd64-b7abd46338b4 | -20.4739 | -54.40057 | 2025-09-04 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5306021d-3cde-344e-b678-031afe6e79db | -19.56828 | -49.43615 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcf415dc-2f4e-3174-a124-81b023e3fe96 | -20.29196 | -46.71071 | 2025-09-04 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 62fb11e5-31d3-3be7-b4f0-b23948496c76 | -15.30548 | -52.76346 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 114c959f-4e60-3e57-b5c5-cc9e3768e622 | -18.72106 | -46.88683 | 2025-09-04 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c18ab71d-c230-3cd3-9140-4e23bc9148bc | -16.30372 | -45.69951 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e6f76df-d8db-3763-834b-47325a1d8dae | -15.55221 | -48.41175 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1eb5bb76-4bb9-3491-9f14-cc5798840b00 | -19.23919 | -48.68364 | 2025-09-04 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 879556d7-ffa3-3d2e-a2ed-2f777a84f7a2 | -16.29422 | -45.68947 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 37078943-1799-3f83-a4ba-27b63ce46fba | -15.54568 | -48.32299 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8b68bc8-500e-3507-a3f6-fc9b8f37718d | -20.09167 | -44.14473 | 2025-09-04 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69aaa3c6-a53e-326e-944b-246766f1b6bd | -15.54844 | -48.32711 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f87b8de0-cea4-3b2d-ad5b-bda05ac2f28c | -15.60679 | -52.88871 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dbede98-4e3b-3ab0-bad9-0a8104a7a4d9 | -15.179 | -52.35328 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a0827d2d-756c-389a-be23-24b7d920e53b | -20.28836 | -46.71049 | 2025-09-04 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abdbeb2c-c107-3670-992d-196c3e84fcf0 | -16.31019 | -52.96318 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dc4a601-1502-30c0-8fb0-28185207b077 | -20.02828 | -49.75582 | 2025-09-04 04:29:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1e761b6-76a1-3b7d-8b36-e8b05f0ca78c | -16.41183 | -45.65042 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72876df9-fac5-31fa-8a43-67bd9aca40f9 | -20.09678 | -50.01195 | 2025-09-04 04:29:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 9d76042c-1fa0-3c64-b411-be373aad254e | -18.06381 | -45.99215 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8380a3ab-48d7-30d2-9eb5-8836a95623c8 | -18.14083 | -51.78836 | 2025-09-04 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 177d32a5-7069-3f80-822a-29218fb10656 | -16.00386 | -49.27975 | 2025-09-04 04:29:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57867598-bb4b-367e-a2e2-e5157bf4787e | -15.57615 | -50.32288 | 2025-09-04 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d6c0c8-a237-3a73-9370-9e9fcab1b819 | -15.30419 | -52.7483 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8742a1b2-ffbe-3f4a-92e2-9d1d77cdef7a | -18.68967 | -48.18126 | 2025-09-04 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f496ba9-1204-3712-93dc-ee30cd58c96d | -15.5352 | -48.34682 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d2c9621-797f-3dbb-9a92-5f9e54987d99 | -16.96665 | -49.30295 | 2025-09-04 04:29:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cbae252-c639-3127-820f-aa6e0bb7c326 | -15.4685 | -53.01117 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfed1d5f-51d5-3cf0-b2bd-056c8746aee7 | -16.46678 | -49.51421 | 2025-09-04 04:29:00 | NOAA-21 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 169bd9ac-caca-38a9-9ee1-8140e9ee8fb7 | -15.59451 | -52.89148 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c44b64d-1831-3abf-a6b3-e296da06e978 | -19.24251 | -48.6842 | 2025-09-04 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c629d173-2104-3fa6-9e6a-de428000c654 | -15.9851 | -55.97638 | 2025-09-04 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 33a95dad-062a-3484-a8a7-9c783aac940b | -15.30287 | -52.73338 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c90f9cb-720c-3a6a-a81b-c67d71a44ab3 | -19.56771 | -49.4398 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a50d3f6-cd74-3e42-acee-5959f5730c6e | -20.16341 | -46.59658 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9d9fc5c-78c8-39c8-9117-ed066f5e3f5d | -15.53576 | -48.34326 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af15ad3b-35b4-34b9-a32b-f079a1f65744 | -15.59831 | -52.8922 | 2025-09-04 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 904a738f-769e-32df-935e-1b27c903953b | -16.30492 | -45.69115 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18495a33-08fc-3610-bc50-b673557873f2 | -16.61818 | -49.43977 | 2025-09-04 04:29:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b4abfcf-1137-376e-baf2-47d3eb110a00 | -15.15373 | -52.37973 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d02e7b2-f7c0-3141-9379-bb969ca45dd6 | -17.04204 | -47.14536 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| afcd99f1-ad99-38b9-9ebf-d8c0385f600f | -15.55387 | -48.40107 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 584eaa1e-1777-3883-8c9e-b97a28f1f2af | -15.55165 | -48.4153 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7c6a2b3-790c-3d49-afb6-f0e131ba6aee | -15.30716 | -52.75379 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5b377cd-1854-37e8-9d0c-2de585adb6b1 | -17.15792 | -46.22153 | 2025-09-04 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f4e5d21-9d91-3f47-918d-badd9ef29cd3 | -15.16968 | -52.35386 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 735e78ae-1743-32b8-94fa-d3eb5a1aa40f | -17.97699 | -47.1196 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32f54102-a238-3990-a738-1dc57ce750ec | -15.16773 | -52.35183 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db9734a2-a62a-37ed-b1a6-5d8db99b2641 | -19.5009 | -49.56291 | 2025-09-04 04:29:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c138cb2-96a9-3b51-a473-0dd8ae80349b | -17.05646 | -46.44707 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8494d41-4793-3fdc-b9b1-bbac8f8c018f | -15.73625 | -53.63855 | 2025-09-04 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bef0e97-e319-375d-801d-e7787eb7e0ab | -15.58536 | -54.31978 | 2025-09-04 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35b6d750-1c43-3694-af8a-8a46c836363d | -20.29497 | -46.71511 | 2025-09-04 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4214c5fd-784a-365b-919e-4f5a59d41191 | -19.68894 | -49.35941 | 2025-09-04 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1a566a8-f3c2-3985-b184-10e801a1dd2d | -17.97297 | -46.90812 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a830dcd5-1e7d-3cb0-8099-d13cf03bb334 | -15.56764 | -48.39969 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a77be135-875b-3b41-90ce-d522bc87e70a | -15.15454 | -52.375 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5d87d23-a1e1-3a3f-9ffd-bb8fb12f0ac4 | -19.51375 | -46.90039 | 2025-09-04 04:29:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dce55455-890c-3c29-aaf1-3c717ff27c2b | -16.30729 | -45.70007 | 2025-09-04 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 831aef5a-4a1b-31b0-aa6d-e91db5d940f5 | -15.55057 | -48.40052 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ebdaf5f-e862-3f8e-b23b-e8ba2ec02203 | -15.54726 | -48.39996 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5137dc7a-4ebc-30e1-8768-aa5b52df73bf | -17.04316 | -46.4899 | 2025-09-04 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bb54c53-fcd1-3297-ae54-88103a63ee66 | -15.86219 | -52.30029 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bbcccf09-0afb-3bb9-8e43-a1a950de0b15 | -17.973 | -47.12297 | 2025-09-04 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 825ca997-5ba3-36df-ab37-0e8c10cd8525 | -16.47011 | -46.86625 | 2025-09-04 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c05927e4-0099-3888-9bc6-45bee13a344f | -16.71031 | -49.39587 | 2025-09-04 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe05ee7-a639-3dd6-8f1b-56de148220f7 | -18.57242 | -44.03537 | 2025-09-04 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f6d948b-8996-3797-acb1-113c97701369 | -15.24493 | -53.80183 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 399a9b58-b9d7-3da1-9bce-e34655553e09 | -21.70043 | -45.42722 | 2025-09-04 04:29:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4f0a9b5-927b-34ac-9ef3-3698a931f4dc | -16.31025 | -45.70481 | 2025-09-04 04:29:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31adf98e-168e-3b97-a907-56517640a344 | -18.26203 | -45.36106 | 2025-09-04 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49fb5e41-79c9-3b5f-91d7-1a42031a58c2 | -15.2456 | -53.79815 | 2025-09-04 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001b8750-842e-3229-8866-412b22f1ee80 | -15.54893 | -48.38929 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2853439b-50e3-3816-a922-b33cd0b783ad | -16.31486 | -52.95892 | 2025-09-04 04:29:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ad230c6-9200-3ae0-8243-8a612d7f8a1f | -18.34714 | -47.02857 | 2025-09-04 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21fd6867-c91e-35cd-921a-ddd365faa42e | -18.33 | -50.97841 | 2025-09-04 04:29:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba550b99-f06c-3771-86d8-0b9fc3771226 | -15.54513 | -48.32656 | 2025-09-04 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffc96edb-b5b3-354a-99ad-9876993d0472 | -15.17448 | -52.3571 | 2025-09-04 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README52.md)
