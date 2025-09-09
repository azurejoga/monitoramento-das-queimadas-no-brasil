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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e6ccc47-90bf-3939-862a-dea13a7d1f26 | -6.20891 | -43.3939 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efa51a19-becd-33cc-b062-1fd0986a2766 | -6.43888 | -44.05749 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce2c45c5-f162-362f-8830-a587852844c7 | -5.36241 | -45.94779 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72dfb41-3098-382a-824f-f1a8d9dadf26 | -5.17312 | -45.16973 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602a1488-6d4d-3783-9b2d-7733827e83f0 | -5.76684 | -45.52873 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ccd4b6-ab37-3cea-99d6-a68c7d443a09 | -4.88276 | -44.95928 | 2025-09-09 04:32:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f86d5c4-bb10-3c22-9d41-a310401ce7f8 | -4.70032 | -42.8214 | 2025-09-09 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7ee82a1-62e3-3486-bbe2-44ed5318292c | -5.92461 | -45.94162 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 426c2d7a-50f8-3620-a753-4b871d55f5c7 | -4.60165 | -43.31853 | 2025-09-09 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2595485-6da8-398f-be30-0882459a6f3f | -6.30404 | -43.81716 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d5fd65b-e467-3d43-87fa-2562bd5f7f9b | -6.39774 | -44.47692 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9a9cc1-ee57-361a-a5dc-8e6d1d4533af | -5.36048 | -44.79725 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd372f3b-d636-3ce6-bbb6-0f1f130c9830 | -4.17495 | -42.02842 | 2025-09-09 04:32:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 617dd78e-b9b9-34b9-9046-62124a5a924c | -5.83626 | -44.1017 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fea52553-1db7-35fd-a726-bb0bb7d3504d | -5.68406 | -43.89843 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a303a5e3-a8db-3977-8c43-f7b62f39952f | -6.24594 | -44.79842 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f99615bd-6c5b-359e-b239-f0dfc890d002 | -6.34838 | -43.78088 | 2025-09-09 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a0d24ea1-4518-31e0-a620-efc892b4b24d | -5.93487 | -45.9432 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8538947e-6a56-38eb-bf6e-33baaa563e44 | -4.97644 | -48.9452 | 2025-09-09 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65f4dee1-e77a-3f6e-9641-1fe503251649 | -6.80583 | -43.56476 | 2025-09-09 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a945032-adc8-3a6b-bdd7-f0621fed061f | -5.80104 | -45.66933 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a925f2-c7c9-3948-850e-c1960a9e3be5 | -6.17709 | -42.65425 | 2025-09-09 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e75bb4df-6ed2-3f57-86b1-c72e682a9b7c | -6.258 | -43.49911 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 152acd2b-cdd7-32d7-be1f-fc6697fc32da | -5.88382 | -46.09398 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75cfcfe1-6ec9-3ce5-85f2-5dcbdbeaa0e7 | -5.66894 | -45.31707 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7803ad5a-bfcf-3519-8c4c-3a381eb6d746 | -5.43967 | -42.7955 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93b8af54-18de-398b-a9d1-43f3031933a7 | -5.73799 | -45.41415 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd9f93ff-b38f-3a3c-a243-ed539a487c19 | -5.69021 | -43.9087 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc3d38a0-f88b-3bb0-8332-a8faa8bd96ca | -7.18662 | -44.90789 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31d69fab-f1c4-3274-9e89-87b10e915bad | -7.17575 | -44.90628 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d0cf40d-4fe3-3b39-b5ad-8937f6a65d94 | -6.14656 | -43.30102 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ae29c1a-b0fb-314d-9252-081f6cdc86b4 | -5.39393 | -43.2373 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1985621-f376-3fa2-b069-76d565bea7a4 | -5.83694 | -44.09716 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17b38357-b6a7-34a2-81c6-109ab9367e52 | -6.27978 | -45.61198 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea5c5008-5c06-3faa-bb63-b53605d88adf | -6.21652 | -45.57108 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c7383c5-2ad3-375a-9d94-d86812ed209c | -3.97 | -47.16641 | 2025-09-09 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| debdd34c-d0ef-3b6f-8e6e-c6d4349bad36 | -3.3278 | -54.90573 | 2025-09-09 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a0ffac-0656-308a-865f-3d358619643d | -2.33876 | -47.58938 | 2025-09-09 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0962bee-d3b6-350d-9ab1-e1b9a4c5e089 | -6.24243 | -44.61523 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 577e2ab3-3286-33a8-a811-4d720f572f19 | -5.72522 | -45.40421 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcf9792b-3328-3b33-971a-24c2e508dbf6 | -4.99944 | -56.25166 | 2025-09-09 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2098bedb-524f-3284-887d-04a63fd1599d | -5.93923 | -46.16963 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf414ab1-b8a5-33bf-a334-432c2b81d91f | -3.81996 | -52.30576 | 2025-09-09 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3290600c-f9ef-3da2-9cbc-314051451589 | -5.99298 | -46.20406 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e2ce5cc-8b11-38f4-a71f-2c1963d98500 | -6.43652 | -44.04755 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a8afaa8-257f-3d6a-b6cb-23bbe767d4bb | -3.39144 | -52.83581 | 2025-09-09 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6054c44e-dabb-3c70-8b0e-907d246baed6 | -5.8889 | -43.95365 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05761f26-1c64-3258-8b10-a75f1ecb5409 | -5.73629 | -45.28245 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b37cfb7d-ae55-3cd1-ba50-173d95e72506 | -6.2205 | -43.50215 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 075735ec-8390-3539-8df4-7fe2320a8005 | -5.30739 | -44.50775 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 433678ad-3964-32b1-9491-2ea920174fa3 | -5.82061 | -43.96769 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4b835e9-7d88-3799-8599-cec8c1d73114 | -6.96489 | -44.79045 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5230dc6c-3318-3193-a330-10a57f3ba639 | -6.06401 | -43.1226 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b8f44056-3f62-372d-86d1-17a386673aec | -6.60444 | -43.96012 | 2025-09-09 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a94b21c-fe9b-37b0-973b-186b6e313edc | -5.75365 | -45.42841 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ce78ee3-98bc-3639-a8a1-c7f18b1b423e | -4.42392 | -47.96009 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e91baca-e5e1-33c2-844c-cb674cc66f13 | -5.79255 | -45.43034 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a997b7b3-4040-376e-b2e0-0298d6686672 | -4.19219 | -47.57463 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e47cc812-dafb-3f76-bd28-f8900d794ab0 | -2.77234 | -48.59577 | 2025-09-09 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13bc69b5-0b04-3f71-a6fb-0db3fb2ec363 | -5.26196 | -44.44075 | 2025-09-09 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2939efe5-838e-3a81-937c-e2372782bc8b | -7.24288 | -44.04045 | 2025-09-09 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a361d45f-a136-3811-b0bd-c07ba4ab44e9 | -5.16963 | -45.16918 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d18787d6-89e2-34a6-a646-6b2c07508626 | -5.36638 | -45.94462 | 2025-09-09 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8623097e-8387-3a9f-908f-c4be3e9d454a | -5.85658 | -43.85957 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c57f28e1-7a05-3375-bbd7-2706c2f4d84c | -5.57871 | -42.90484 | 2025-09-09 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 13893951-7a49-3a71-8fb2-ce2d643a724b | -4.51005 | -47.82536 | 2025-09-09 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20e01ab-6753-3f06-9b3b-2adfe5692f21 | -5.95032 | -44.16703 | 2025-09-09 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99f4de22-7918-30db-b1aa-98f77da75876 | -6.41542 | -44.48438 | 2025-09-09 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1052a6f8-b31c-31bd-8403-857993e698f9 | -5.83896 | -44.21131 | 2025-09-09 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9127dc43-a9f5-3d64-a086-1b0d48deb4cb | -5.57558 | -45.0493 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6f81b04-88d0-3ae1-8542-e42a3087b8f2 | -5.83907 | -45.39278 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35bbf9e4-dc01-35af-b48e-167deedc6daa | -5.49406 | -42.65856 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a4137d84-8bfb-38d4-8c95-16619df19204 | -7.20006 | -44.89253 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3b743e2-777e-3e50-b4aa-59c1f7c69407 | -5.82682 | -44.11409 | 2025-09-09 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c91840b-ce4e-350f-9fa9-be8aa456d0b4 | -5.35628 | -44.80078 | 2025-09-09 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ac937db-5c8b-306c-93c0-a3a119490f72 | -5.3808 | -43.24541 | 2025-09-09 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d922dc-a377-3c9c-8c11-9773092480ad | -5.94636 | -45.79973 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc0d98fc-619a-347d-9fd6-66c4276296e9 | -5.89143 | -52.09928 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac094c17-7a15-35ea-bf49-ed1b76ceffe7 | -7.08111 | -44.86254 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58a37afd-f7ae-31d1-a653-ab8edf85f776 | -6.08597 | -43.35808 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb58b22-abf2-3538-a8f4-461483b8699e | -5.08775 | -42.4181 | 2025-09-09 04:32:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab51437d-d4bf-3b90-9792-256c782b69a2 | -6.23001 | -45.58857 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29c03aa8-4738-3863-b662-a265f516073e | -5.64507 | -43.64375 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9072f44e-d824-3371-af67-1793cb113b30 | -2.62918 | -46.84009 | 2025-09-09 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 52b4dd40-5a9a-3fcb-9290-2762fea1fc49 | -5.4571 | -43.42644 | 2025-09-09 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e65bf2f3-a6d6-32f2-8f9d-5e93bf902d5a | -6.22805 | -45.5886 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c5186e7-4cfb-32bf-a7eb-d5552d0d9eb8 | -6.205 | -43.39335 | 2025-09-09 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de641151-08ab-376d-b192-25d0f1ec75dd | -5.68681 | -45.38737 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5223c6a2-bdee-3f07-b35f-dd16c2019ebe | -6.03237 | -45.02074 | 2025-09-09 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca06264b-c385-393c-8c39-7ddd7173eddf | -5.92519 | -45.96063 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53fe2570-c4f2-3fde-8c67-ff1ae0cc93b6 | -5.82355 | -43.98019 | 2025-09-09 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5ff9c15-c9a1-343e-9e74-44114d2ddf7e | -5.54952 | -45.175 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 64c76969-d7a0-3098-ad1d-714bc9cea3c7 | -6.8363 | -44.89884 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09c28f6f-e55f-39d5-8a0d-42cf34d0fa45 | -5.77739 | -45.4596 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf89103c-fac5-3786-b491-27a3ed5fa26a | -5.66866 | -45.45951 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a79f84c-ff6a-38c7-8e3f-855a2b75539b | -5.94472 | -45.67191 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cd701b0-0288-3e06-8285-16177367f8fa | -5.78565 | -45.40549 | 2025-09-09 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d8a63e9-5c0b-3ccf-b8f1-94fbf73185e1 | -5.9975 | -46.19727 | 2025-09-09 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60475bdc-0bcf-3ca2-bbaf-7b4084ad9052 | -6.06327 | -43.12772 | 2025-09-09 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0622de0-80fd-3ec8-ad95-9ea20a5c16d2 | -5.45569 | -42.79815 | 2025-09-09 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README25.md)
