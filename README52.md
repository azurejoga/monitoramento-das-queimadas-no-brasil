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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fd54897-f0e9-3cf0-84fa-4516cf57f5e8 | -11.82485 | -51.78764 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f3707404-8d44-31cd-9724-5b761b2eb8f1 | -11.81422 | -51.78769 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da04b557-8a1f-38bb-ad5c-1f88a3d37239 | -11.35339 | -44.95858 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3660652-42be-349e-ac97-543e727c5307 | -9.46058 | -45.49345 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7a6e2f7-069a-30c8-929d-2d3e10ccbecf | -11.95576 | -48.04588 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64f782e6-bdff-3ca0-b0ae-7c3ab3fcb1ca | -11.44817 | -51.49365 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b4ccb29-cbbc-3fcb-8fbe-131b043536c1 | -14.28517 | -49.39589 | 2025-09-29 04:08:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 464928d4-3c36-3411-99dc-92c4c8ab5503 | -13.25127 | -48.44936 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc5bd502-9210-33ea-b1f1-abd729d81788 | -12.88309 | -46.98737 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 586593e6-4064-303c-b898-5761444e14b9 | -15.46806 | -47.93658 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4f3946e-217e-3c73-94e7-c0345c538486 | -11.44638 | -47.28482 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41348542-6ab3-3960-9e0c-87d975fd6e8c | -11.92796 | -48.06033 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cc3c91f-6e37-3784-bc8e-5efc3768d6dc | -11.72835 | -45.23413 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c401daf-b750-3c4a-ac6b-00fe1af420df | -11.97714 | -46.58331 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1061ba8-63b2-3229-81b2-37122f029c24 | -14.5336 | -48.4268 | 2025-09-29 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d925c4d3-96f6-3855-9e00-6198d24e76d7 | -14.5331 | -48.4491 | 2025-09-29 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 847f796b-b0d4-3db4-b0c1-3a518c78c80c | -17.9009 | -57.6182 | 2025-09-29 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.0 |
| a1129d1d-560b-348b-af01-3b953dd2cc89 | -11.925 | -48.0273 | 2025-09-29 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 30563f9f-2448-3893-b134-6abddfdf7cbf | -8.2851 | -45.4999 | 2025-09-29 04:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| f98e7c68-e944-3c90-b5a4-6b74fb0cfc3a | -9.4007 | -54.6984 | 2025-09-29 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 54a2e67a-eab7-384c-96b7-ae285448d766 | -15.2893 | -49.5035 | 2025-09-29 04:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3d0db24a-df3c-3df5-907b-76f120e69209 | -20.0491 | -41.3251 | 2025-09-29 04:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 079df709-4579-3bcc-b19b-791ce5ee7aba | -20.05095 | -41.3332 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b8811a45-677a-39af-8a95-aff804170cc3 | -20.54143 | -45.10526 | 2025-09-29 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb570f08-68c7-3802-af4f-1ea78b19d08b | -16.10438 | -46.66934 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ce13bce-aa87-3919-953b-83fc6c73514e | -22.08842 | -46.84168 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c697325-3aed-3d02-884c-4dcc4744eb65 | -20.54475 | -45.10585 | 2025-09-29 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c66d2bc-853f-3ae1-ad0e-5c4c86eeeb1a | -23.41804 | -49.46058 | 2025-09-29 04:10:00 | NOAA-20 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| cc4c8034-69be-33c3-91ed-b7dabb68af0b | -21.13568 | -45.10823 | 2025-09-29 04:10:00 | NOAA-20 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 50b7f6aa-5b0a-3b8f-9b2d-a66b98c90a06 | -17.50024 | -43.48243 | 2025-09-29 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5b04cd-47eb-3b67-a510-c75127bf63e5 | -17.28492 | -42.69747 | 2025-09-29 04:10:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bf43f5b-0bc2-35eb-91b0-8531d4601be5 | -16.53869 | -45.30989 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c453062c-b9c0-3dca-9d5e-7470b643148b | -17.4737 | -44.04102 | 2025-09-29 04:10:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 819f4adf-e729-367d-ac32-488e4058f2cb | -16.85058 | -45.80061 | 2025-09-29 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29665720-f40f-36e5-be23-e77ba6c8fcf7 | -16.54605 | -45.30735 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 55c58552-b996-31ec-bfba-a4b4a1e2cae0 | -20.05754 | -41.33881 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| dfa434b2-bf6b-3e30-805d-9aec92997608 | -18.9264 | -41.08546 | 2025-09-29 04:10:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 09948689-0220-31f9-b942-fc465027899f | -17.08494 | -48.56584 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45479b38-a865-3c2c-b992-cca7776a2863 | -17.71846 | -46.71595 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa3df99-86fc-3b0b-b387-286b48fea4ed | -19.9283 | -41.62017 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba173519-7e00-3ca8-ad5b-60f1a1adee13 | -22.97615 | -48.36138 | 2025-09-29 04:10:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7c05f15-943e-3236-9b84-b0d254f76273 | -17.49693 | -43.48186 | 2025-09-29 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79f6ac91-00a6-3134-ae24-c48a499a52c0 | -17.7511 | -48.76597 | 2025-09-29 04:10:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1101ac5c-2e8c-368a-ac34-d0cb49bf6aff | -19.51652 | -44.24285 | 2025-09-29 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eecb584-715d-31ce-8b06-86b6e0f13a1f | -16.52591 | -46.9547 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2cd893-510e-3d70-89fe-f42ffd255d0c | -19.32585 | -43.80837 | 2025-09-29 04:10:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 621b2846-e7c8-3113-b680-daa1accfbced | -19.94442 | -43.66911 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 16d501f6-e3e0-3449-8c6b-cb38a4572473 | -16.59829 | -45.12434 | 2025-09-29 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cda754e-9035-3d79-b6ff-8a79eb902095 | -17.28156 | -42.69693 | 2025-09-29 04:10:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8beacf96-d230-35df-8c2a-2fec01b93253 | -20.40549 | -42.34953 | 2025-09-29 04:10:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dba949c3-2a84-3947-871b-aa7c098eca36 | -16.40362 | -47.03137 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d7ac22d-b05d-33f2-bac8-7eafd0e86fde | -17.08602 | -48.56265 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2397fd2a-5754-35f3-9b44-14cfdd586819 | -16.99407 | -43.50614 | 2025-09-29 04:10:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5217cb0-7e84-3ef0-ab90-23a9e98e7e81 | -17.72679 | -46.68816 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d182844b-3a30-3377-816f-28a0dae84509 | -18.96782 | -43.19581 | 2025-09-29 04:10:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 236a504c-a349-379f-a688-f0b5e1a39831 | -23.54783 | -47.53873 | 2025-09-29 04:10:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9a17f182-cc93-3b7e-8d34-e5ac77dec511 | -17.39916 | -47.11495 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4961c407-f3ed-360e-98a0-6b9828e916e1 | -23.14379 | -50.21636 | 2025-09-29 04:10:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8ecd90ad-3268-3e10-9cd3-adae385fb6c0 | -19.99107 | -43.96191 | 2025-09-29 04:10:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7a71790-85b1-3d9c-9bc1-e69556672d54 | -17.2356 | -44.10768 | 2025-09-29 04:10:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee922adf-d748-3add-9198-a5b87a7d7f4e | -17.71776 | -46.72002 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 894b3909-1176-3faf-bd16-561bc21b458f | -16.84498 | -53.20156 | 2025-09-29 04:10:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c87399f7-05ca-32cf-a919-23b5a13da03b | -19.86352 | -43.79599 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a6532627-4c0e-3ec4-94ce-3a365d20d4b7 | -20.56768 | -41.93949 | 2025-09-29 04:10:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f7c0835f-59a9-3412-b6aa-ca76021ba84d | -16.41236 | -47.02399 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f45a7edb-288c-3cb4-a84a-00d9cea7d4f1 | -19.86348 | -43.53382 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4221ea8-7f6a-3ccd-aff4-03344a62ad43 | -18.56715 | -44.01805 | 2025-09-29 04:10:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf409394-c303-3431-92c0-1c9d568c267b | -19.6779 | -43.76907 | 2025-09-29 04:10:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f0c1c2e-65b3-3f6f-9f90-5a03d55ee1ef | -16.50605 | -46.03304 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edab3b3c-a8cb-352f-b5c4-f394a2eeca96 | -20.05397 | -41.33801 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 1c7df66c-a18c-3855-90fc-c92b59720d83 | -16.49158 | -46.03441 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 116fa2d7-1d1a-3d1b-9a24-3449e6dd0a37 | -18.10588 | -42.19339 | 2025-09-29 04:10:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd9da0a4-e6be-3dbc-ae0c-1da5cb946cee | -19.31864 | -50.06002 | 2025-09-29 04:10:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 503f9a8c-0a25-3a09-9845-b152764bc937 | -19.30509 | -48.91936 | 2025-09-29 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a609b245-a560-3ab2-9e8e-1014d64f009b | -20.63375 | -46.16948 | 2025-09-29 04:10:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ecd95ac-6714-3017-bdde-4d583b093257 | -20.44079 | -43.23272 | 2025-09-29 04:10:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5fea7d11-7702-3928-b4bf-a906b79a8b1a | -22.08974 | -46.8339 | 2025-09-29 04:10:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38a59447-7f26-37e5-aefe-62eb2566eeae | -22.02664 | -46.49145 | 2025-09-29 04:10:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1ca3fd7e-4a83-31e5-8cd6-94d56ec85ee6 | -17.08509 | -48.5677 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 05d11a33-da98-324e-bb87-b80f502f9103 | -18.11327 | -42.19078 | 2025-09-29 04:10:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd4d2071-828d-377a-be60-8a68997e0cc1 | -18.33808 | -41.7965 | 2025-09-29 04:10:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a4fd3f1b-5683-3ec2-a4c0-db17f07e03e4 | -16.34171 | -49.94806 | 2025-09-29 04:10:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b002d39a-5470-301f-958a-1d0f1384077e | -17.52216 | -44.88269 | 2025-09-29 04:10:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 385860bf-0775-3786-a470-69f26b921cab | -23.22649 | -49.39827 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b43db602-20ab-362c-b580-eb6308a3b1d3 | -16.85123 | -45.79675 | 2025-09-29 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a7fe9f-0479-3c13-92cf-c5d7adafe5b9 | -19.94386 | -43.67283 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b183e301-afb8-3c47-945f-3a9ce6936a76 | -21.0488 | -44.73254 | 2025-09-29 04:10:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 82927e87-8906-39fe-a5ef-653f45de4ae7 | -17.74816 | -48.76011 | 2025-09-29 04:10:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b347db1d-0dcc-3b65-8907-0d071cedbd2a | -16.4116 | -47.0283 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3be4cea8-879b-31c6-87e5-740aa65f0009 | -17.08801 | -48.57362 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e6995ae9-9c5f-37bf-8188-35d8f410ec48 | -20.40896 | -42.3501 | 2025-09-29 04:10:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48295318-28fe-3e94-a164-dc6bf8869183 | -19.20329 | -43.98654 | 2025-09-29 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17e6a106-71bf-386c-890a-9d71e6fa30f1 | -17.755 | -48.76668 | 2025-09-29 04:10:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a3ad2f0-ecf7-364a-a324-7deeff0de011 | -19.98807 | -44.15759 | 2025-09-29 04:10:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6171aef2-03fe-3c3d-8c71-4063243eb617 | -16.53024 | -46.95114 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cfa38d6-5841-340c-bb3c-9be2c6bde8d3 | -16.40799 | -47.02769 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d37f92b-90a7-3c1f-85b6-2f4218365ed1 | -18.70586 | -43.6712 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0898212e-cc2f-3525-8fc9-910036eea06f | -18.90533 | -41.13041 | 2025-09-29 04:10:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0162783c-e196-3960-9371-5eddcbe5dbec | -17.39696 | -47.12762 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc67ca5f-9792-32dc-9dd3-86605571ea2e | -16.49225 | -46.03046 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README53.md)
