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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad6b1ee0-3262-3e0d-a5f3-1fcb40427419 | -6.6249 | -42.11995 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 05a671fd-4e0c-3289-9276-3743301c4d1f | -6.62431 | -42.12389 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 581d18de-f5d7-3c59-a337-2e9a93baeebe | -6.62371 | -42.12785 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9b4a60c1-174c-35b3-a814-77616aa650cb | -6.62312 | -42.13176 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 77667cf9-9143-3e42-8018-74405246ce61 | -6.62081 | -42.12329 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a99b6fe7-afc3-34a1-9c3a-cf3cdd424490 | -6.62021 | -42.12728 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e30c930d-c30a-3479-9e59-a781ee2af024 | -6.61962 | -42.13121 | 2024-10-06 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c3f95aea-14fe-3a38-8105-11b022804c6b | -7.30036 | -42.26501 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e910c60-9c58-37e6-af46-eb6fb17b21b3 | -7.29925 | -42.24876 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3a62b385-37b5-3e4b-9d05-9318315352b3 | -7.14061 | -42.62357 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a1bd97a-72c6-3062-beb6-2cb94b1f9820 | -7.14003 | -42.62734 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a0b1789-218a-3777-b033-4451c62441bf | -7.13774 | -42.61927 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2013a8d3-4a2e-30c5-aaed-e209714e460c | -7.13716 | -42.62305 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5e898ee-2f65-3795-9bbc-059a8b6a7733 | -7.13659 | -42.62682 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9075839a-0d47-3116-b45c-697b8659cb0d | -7.13314 | -42.6263 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c321fdb2-2427-3659-a295-efbfef3a3e84 | -7.13201 | -42.61063 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1848dd4-f498-3243-a3be-126913d8eed9 | -7.12914 | -42.6063 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b396ffa9-9638-3fc1-8c5b-a17ffe5ae330 | -7.12569 | -42.60575 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 78253602-0b58-37b3-97bd-97950c0dc499 | -7.12566 | -42.62904 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 894aa73c-a038-35d3-a21f-f362129f648a | -7.12336 | -42.62095 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e01f1f67-2808-357d-9e17-a33372b412a4 | -7.12279 | -42.62474 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9d42ea9-990c-3daa-a41f-e9b6df572246 | -7.12224 | -42.60521 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b796e1ca-9632-3441-8c28-1c888b99d7ea | -7.12221 | -42.62853 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f94c710e-62a3-3ecd-a884-8f276b2b3aef | -7.12166 | -42.609 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7ecd3d3d-d628-3e7a-824d-69aa7d73f5dc | -7.1205 | -42.6166 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 756acf45-82c8-3428-9147-57330bdb316d | -7.11992 | -42.62041 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5530802d-1238-32a4-b4af-db4b387e8f17 | -7.11821 | -42.60846 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 508b21d0-a818-3101-8fb6-417e769d4d5f | -7.11705 | -42.61606 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e0d09972-d8fb-37f9-ba1b-96cf95086cba | -7.11647 | -42.61988 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d3b44f27-a378-3276-9c3c-e299912a3b86 | -7.1136 | -42.61553 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e3e6f89-4a04-3b08-b5dc-5d26b8ac861a | -7.11302 | -42.61935 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00df4b8d-09d0-3ff9-886c-e5ced1f8247a | -6.831 | -42.81548 | 2024-10-06 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 449cbedc-a5d2-37cd-8e1a-4275efaf7825 | -6.82815 | -42.81122 | 2024-10-06 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 675546bc-5166-3859-a7b6-89818e67940e | -6.82758 | -42.81495 | 2024-10-06 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2fd4a471-77b2-3a20-ac61-431a5a0e5250 | -6.82473 | -42.81069 | 2024-10-06 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7c2cfdc0-e093-3dd6-a19e-a3339fa45488 | -9.25488 | -43.51931 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 242ca917-8e9a-3b2e-8714-832b45ce565f | -9.24636 | -43.50665 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9230717-5e7e-33dd-9101-308551ffab8c | -9.24525 | -43.514 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ae39f12a-d764-3179-85cb-b7e5180b6237 | -9.2413 | -43.51711 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ee62c570-67aa-313c-9523-b6b763fafb54 | -9.24074 | -43.52078 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 77ded8ee-a754-3d52-b88f-0d1c9bc90395 | -9.23791 | -43.51653 | 2024-10-06 04:17:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b856bda8-02f9-3286-a49b-312d6b9c14bb | -8.19804 | -43.70453 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f819540-c8da-3c1b-ab92-b8cfadbda5c5 | -8.19749 | -43.70814 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9dcee13-9ab8-3e99-a764-41b78fae9e7a | -8.19694 | -43.71174 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0143be8-72bc-3b02-a108-4021d3723fc7 | -8.19365 | -43.73327 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ced6c413-0a1e-3a20-b1e5-6ed8cf7e9f75 | -8.19358 | -43.71124 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd5e5c46-4686-34f4-834b-442807b8b786 | -8.19084 | -43.72918 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0448bc8c-c4d4-333f-94c3-af11ee131cd8 | -8.18879 | -43.72881 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d846160-50a6-351d-bbc4-5e1a14b7c8d9 | -8.18598 | -43.72471 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91405add-45e7-39e0-918f-128fc2147464 | -8.18318 | -43.72062 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6cc19828-ab37-334a-8218-d179b48e705f | -8.18263 | -43.7242 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b1e848b-0346-3338-8d5e-f0df618bfb54 | -8.11458 | -43.78671 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbe8be5b-6008-357c-9981-3fb747bb8359 | -8.11404 | -43.79026 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1e93a46e-898f-346c-a4c3-380b0eda94a1 | -8.11068 | -43.78975 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d009f077-2fb5-395a-bc5d-1ea11597720f | -8.10733 | -43.78922 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b7b9435-8fe8-3f00-88fa-67532d14ed70 | -8.10398 | -43.7887 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a144cf6-ac51-3d6c-8555-03df2dd7d66e | -8.36493 | -43.66017 | 2024-10-06 04:17:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5172020-c897-3719-9ad8-8d28438e1f6c | -8.20133 | -43.68294 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9daa2b0b-e28a-38b8-8b64-b046e22d862c | -8.19796 | -43.68244 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36866706-7bc8-381f-92c6-b48e9f243aca | -8.19603 | -43.68211 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42dbf2f7-3576-389c-99fd-0d342f0b0267 | -8.19267 | -43.68161 | 2024-10-06 04:17:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f78b23e6-42ed-3464-b0b6-6d13e5474f4f | -8.29602 | -42.8282 | 2024-10-06 04:17:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 91b315e3-84be-3a4c-b44c-00483604e62c | -9.42068 | -44.12364 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f48c1a3b-f82e-3a0b-8b7d-5c8cc5658f51 | -9.42013 | -44.12725 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1b4f3d7-119d-3863-96da-24b3985ae273 | -9.41734 | -44.12308 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fd3d473-4bd7-3b41-b532-d0937ed1d127 | -9.41679 | -44.12669 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba04b3a2-5d6d-32e3-a95e-f0c98ca5ad36 | -6.51043 | -43.77826 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39a497f4-6755-37af-90a9-4bc083fa9b54 | -6.42401 | -43.6567 | 2024-10-06 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01795149-2f88-3d1e-b681-b7f60392f942 | -5.88849 | -43.97742 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5e68c3d-1c2e-371b-9122-54e7d0c0580b | -5.88517 | -43.9769 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c19e95-c9d0-3174-8a0f-6452e54f0327 | -5.72383 | -43.79186 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a830169-cd5e-3ef8-8dbb-6f7128f642b0 | -5.72329 | -43.79534 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd0f1895-b9c4-3f4d-bb2b-fdf56d60a247 | -5.72051 | -43.79135 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 369c12fb-7196-3341-9d82-d215ee227165 | -5.71997 | -43.79483 | 2024-10-06 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1704e3f3-e337-322a-999f-a959f29ff4c0 | -5.69501 | -43.4327 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49abcca4-d1cb-33cb-baac-b87378e67739 | -6.54013 | -44.00102 | 2024-10-06 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6a9108c-b513-3e93-8a36-f918a94da9c7 | -6.50673 | -44.25899 | 2024-10-06 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bb3a603-c812-3ee9-86cc-557f160bab65 | -6.26397 | -44.48605 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0c6269e-a285-33be-ab3b-9159e6f4cc01 | -6.23718 | -44.80722 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce026100-66cf-3b29-b6f1-08c88d3c6347 | -6.21045 | -44.13429 | 2024-10-06 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 315571f1-a4c9-3c9b-87ef-7d0112aac473 | -6.20603 | -44.31423 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8c44534-c908-3e89-8582-407e77c17877 | -6.16666 | -44.15246 | 2024-10-06 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87bfe039-2958-37d7-a4b1-f05cc595b608 | -6.15727 | -44.14748 | 2024-10-06 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc17bd33-80df-3739-bcf0-e3c6fd7a338e | -6.08047 | -44.70144 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03459e58-90c9-3ce9-8c36-49fd96545acf | -5.89572 | -44.6688 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b5278ce-7d2b-35b3-aed7-834039b5105a | -5.88932 | -44.77388 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dcba3c3-6ab3-362e-8f79-22881d28ff41 | -5.86305 | -44.8973 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3761fac-e4f6-39cf-bae3-49b346514867 | -5.82327 | -44.13383 | 2024-10-06 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6b4e4072-e459-3081-9956-193cd147d0d5 | -5.82051 | -44.12986 | 2024-10-06 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 644f0429-a320-316c-8366-e6c850cd2c3a | -5.81996 | -44.13332 | 2024-10-06 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e2833080-b02e-3e95-bc9c-4bade4351854 | -5.81942 | -44.13677 | 2024-10-06 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cb40b3b-1369-3a4e-af1e-5db8d0d9c2c7 | -5.8172 | -44.12934 | 2024-10-06 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f784164-bbfe-34cd-ad61-727f3818116f | -5.81666 | -44.1328 | 2024-10-06 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb88cc66-795e-3bab-9701-24e13f4a31b4 | -5.81612 | -44.13625 | 2024-10-06 04:17:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1e7d416-937d-36d2-934c-62eadb53ef2a | -5.81281 | -44.13573 | 2024-10-06 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7fe8e0a5-5dd3-3db1-b525-d5e68f90b2f2 | -5.81227 | -44.13919 | 2024-10-06 04:17:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca3f92ce-43f8-3fd0-a83c-e633db70af8d | -5.58011 | -44.88087 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2b012ce5-dc65-3539-9d79-47c53142cb6b | -5.57956 | -44.88434 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ded598c4-b709-3246-9793-23708d3b4e99 | -5.57735 | -44.87689 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 81ef1d12-5617-3475-a53a-02e5a1f3d0bf | -5.5768 | -44.88035 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |


[Clique aqui para ver as próximas entradas](README65.md)
