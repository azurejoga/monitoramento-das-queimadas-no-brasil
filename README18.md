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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ecc6b53-4fe8-3c26-b19c-dc5950f1efac | -19.14938 | -57.34981 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1eb6b056-9c03-30b9-b9a3-d34e73552af3 | -20.7402 | -47.14577 | 2026-09-05 04:23:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4e7171a-5157-350a-b7a5-4bcb5211234f | -20.60188 | -46.36893 | 2026-09-05 04:23:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c547a3ca-c277-3292-bee2-dcd6b0b9102d | -20.78757 | -57.75983 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 971ae419-6edb-3884-b59e-324b85652ff7 | -19.25579 | -46.86847 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c979d01-eb8d-35c5-8f8c-c014d853a90a | -20.25749 | -46.3356 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9d5cc9e-0ac2-30bc-8ffe-89e709f9677f | -20.14827 | -46.31709 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f16ed241-65e4-3a49-ab8b-b9e19632f2a9 | -20.6052 | -46.36951 | 2026-09-05 04:23:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9b0c851-5360-3b1a-851f-0fe3cf157aaa | -20.3413 | -47.59433 | 2026-09-05 04:23:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c817c58-e0d6-32ae-bdbd-e0a3aee07f33 | -21.23957 | -46.84782 | 2026-09-05 04:23:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6de3ffd6-8fc4-3591-903e-27ec02d3b753 | -18.58795 | -48.23745 | 2026-09-05 04:23:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d006a8d7-646d-31de-a7b6-d5e619e6718c | -20.17393 | -47.39167 | 2026-09-05 04:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeb4b1c3-2905-3a45-8bc1-6e60d43b53bb | -20.25418 | -46.33501 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 978a759d-d33b-39ce-9082-5093388a9f5d | -20.1706 | -47.39108 | 2026-09-05 04:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17138e0b-582b-3a3c-92b0-7faa81e44b67 | -21.45762 | -45.7693 | 2026-09-05 04:23:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e04c6493-2438-36a2-b959-91fe653bb851 | -19.74617 | -46.6908 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb39f07c-a6d6-3bc9-b272-a3b9dcc9b783 | -20.76017 | -45.05758 | 2026-09-05 04:23:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d05f78d-9189-3cfb-a6da-1985caebc841 | -20.41668 | -46.57451 | 2026-09-05 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cc246bf-d198-3dcf-9464-ac7cdfe91634 | -20.98778 | -45.80258 | 2026-09-05 04:23:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 114c560d-5b70-38e1-9c72-22796667d1be | -19.23386 | -46.72903 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdeff113-be53-3cd2-a3ad-ffd86e5e6390 | -19.25969 | -46.86541 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e51c76dc-9969-36ab-8aab-ee51afb96713 | -18.4438 | -49.18818 | 2026-09-05 04:23:00 | NOAA-20 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4091504-47d1-3d01-9ac2-499025418aff | -19.83476 | -42.70516 | 2026-09-05 04:23:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 664eb335-2677-3097-92ea-641fcf3e28b0 | -23.0539 | -55.50536 | 2026-09-05 04:23:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be9eb290-1cfc-31b0-8eba-9ce1415195b1 | -21.51674 | -50.03595 | 2026-09-05 04:23:00 | NOAA-20 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 213fb7cb-9211-3504-9512-dc2a4c3f6293 | -21.37855 | -45.34295 | 2026-09-05 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a9407d7a-87f7-3db1-8e0f-c48418918e58 | -21.4608 | -48.67709 | 2026-09-05 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9965bdf1-3079-3abc-be8b-e3aad4051059 | -20.4091 | -46.58086 | 2026-09-05 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 298ea0e3-c9ca-361b-904d-55e0f07a0083 | -19.1551 | -57.35125 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d6d3c616-471c-35fa-b27a-29c7879f2f3a | -20.66034 | -43.52983 | 2026-09-05 04:23:00 | NOAA-20 | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c13c14b7-78bf-3fb3-8acb-0fd6ce49e919 | -20.25692 | -46.33926 | 2026-09-05 04:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72677eed-782a-337c-a1c2-a549fd7ef183 | -21.50923 | -49.95372 | 2026-09-05 04:23:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0d4bbc0d-befc-3775-908f-333f6aabf03f | -21.38883 | -45.50566 | 2026-09-05 04:23:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 461fe698-c480-3188-b840-af97c06613d1 | -19.1627 | -57.34422 | 2026-09-05 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| abe6bc66-c66b-377e-accd-b02624ef4c20 | -20.98721 | -45.80633 | 2026-09-05 04:23:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ee369a6-f3ac-3298-b7bd-7d8c7ba2a8ae | -18.89667 | -47.05107 | 2026-09-05 04:23:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1379a7-ef17-39ff-9803-469a157cd9e2 | -17.1117 | -56.83871 | 2026-09-05 04:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 05cf1fff-7b80-3ad0-8659-eb420e9f93e5 | -19.25638 | -46.86481 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 107532e6-9664-3492-8b93-6ef999f83a5c | -21.55262 | -44.056 | 2026-09-05 04:23:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 138dbadb-da36-30fa-9104-3a6388c4ce58 | -19.32577 | -46.36647 | 2026-09-05 04:23:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf58469c-2d00-35d1-aa4f-11df4660d006 | -19.75124 | -46.68039 | 2026-09-05 04:23:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73625c58-b09e-3e39-944c-816c93d0d3d8 | -21.51752 | -50.03157 | 2026-09-05 04:23:00 | NOAA-20 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9e84c8ee-fb8f-30cf-93a7-bd9c9af96b1e | -19.23659 | -46.73328 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1907fd53-9522-3a0f-9a5b-e725a3382808 | -21.57706 | -48.65361 | 2026-09-05 04:23:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| beb8b6ce-a3b9-346e-9873-2b1ad37d25e3 | -21.46146 | -48.67318 | 2026-09-05 04:23:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8bbea3e-bdbe-3516-b000-fdf8969ce069 | -21.51126 | -49.96304 | 2026-09-05 04:23:00 | NOAA-20 | AVANHANDAVA | SÃO PAULO | Brasil | 3504404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ea6caf36-bcf5-3bbc-8c84-e261a1d07548 | -20.67552 | -44.41696 | 2026-09-05 04:23:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 563b220e-b676-357b-923d-4b69600c4a7f | -21.34512 | -48.23987 | 2026-09-05 04:23:00 | NOAA-20 | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ba452ce-e62f-3cba-ba50-f4f2e88c0cdd | -21.45427 | -45.76871 | 2026-09-05 04:23:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b17d3ba-f69b-3bd0-b112-b11031863d5c | -20.34068 | -47.59808 | 2026-09-05 04:23:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a385110b-b24e-3305-aec5-4b8f53e3ab6c | -19.25911 | -46.86907 | 2026-09-05 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a21b31cb-6f67-37ed-9cce-f560341092f7 | -28.18851 | -50.43182 | 2026-09-05 04:25:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57285c2e-c5ee-3708-a427-337626f931ad | -6.6699 | -59.9251 | 2026-09-05 04:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b126fc22-3c38-3886-a2cd-d135290a1b2b | -6.6698 | -59.9443 | 2026-09-05 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 6d867031-1f88-35b2-b8d2-18effc27e03e | -6.6514 | -59.945 | 2026-09-05 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 193.6 |
| acdd61fd-c6b3-3cc5-8999-01572d4e522d | -6.6697 | -59.9635 | 2026-09-05 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d922e8de-0cda-318d-aac8-3954e7132c11 | -6.6515 | -59.9258 | 2026-09-05 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 613e4700-bae6-3627-ae67-a43792ee791a | -5.3462 | -56.0256 | 2026-09-05 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| cc862c77-4947-3367-b3c4-2525f7b36f6d | -6.6513 | -59.9642 | 2026-09-05 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 8ae4a652-a45a-374a-83fa-c0836f3c3838 | -6.6697 | -59.9635 | 2026-09-05 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 8514e624-40fe-32f0-97ba-48808218742c | -6.6513 | -59.9642 | 2026-09-05 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f23e8d55-e2ba-31b8-9708-003258006640 | -6.6699 | -59.9251 | 2026-09-05 04:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| cae73e7e-3010-32bc-8e93-45d553aeb17f | -6.6698 | -59.9443 | 2026-09-05 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 218.7 |
| bba695ef-44ba-3157-9b53-d24f9f12b9b2 | -6.6515 | -59.9258 | 2026-09-05 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 014dca8d-fd2b-3f4a-8577-40673437e66a | -5.3462 | -56.0256 | 2026-09-05 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f0e3a94e-bd65-338f-adf8-7263973f8c4b | -6.6514 | -59.945 | 2026-09-05 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 95d71426-08cb-3db6-8a34-23d7598ace9c | -6.5963 | -59.9087 | 2026-09-05 04:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| bcbac058-cc6c-3924-a16e-11e989351bc6 | -6.6513 | -59.9642 | 2026-09-05 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 2f09cacd-6530-385f-a635-93fa43d8d714 | -5.346 | -56.0454 | 2026-09-05 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 17456afc-bdb1-381c-b7c8-04f7697c6e62 | -6.6697 | -59.9635 | 2026-09-05 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 73cff030-8273-3329-9adf-593f25ddd5fc | -6.6698 | -59.9443 | 2026-09-05 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 763b6534-ebfe-3ba8-9c93-a9a41006ed55 | -5.3462 | -56.0256 | 2026-09-05 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| cd09cd6d-69b7-3245-abf5-e11a5f1aeb21 | -6.6699 | -59.9251 | 2026-09-05 04:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8b12fc5b-9ef2-3949-8b1b-896351d5efff | -6.6515 | -59.9258 | 2026-09-05 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6b6cc088-9b35-3e3a-9e18-dbf77afde66d | -6.6514 | -59.945 | 2026-09-05 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 256.3 |
| 7147a7e1-8a80-3511-b623-53572cae12de | -5.346 | -56.0454 | 2026-09-05 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| add4657e-427c-3089-87f7-8ee2c8b806d1 | -5.3462 | -56.0256 | 2026-09-05 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 943d54a3-7c47-3f76-8587-b4c6cb879ca8 | -5.3277 | -56.0263 | 2026-09-05 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0e000051-c87d-321b-8510-7eea2a3df2f8 | 4.35857 | -59.73908 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e7f199f-0435-3833-b3c0-11e37d9fe233 | 2.36872 | -50.76944 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c0911f04-3122-30e8-97cd-87a682913dc5 | 4.27386 | -60.04628 | 2026-09-05 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 961847c7-67df-3324-98e5-54daf475a81b | 4.8884 | -60.29815 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e619ab01-1f93-3a35-8051-7dc5be57ff74 | 2.37889 | -50.76357 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 400f063e-883c-3d85-87fd-404d737ff485 | 2.37822 | -50.7594 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af24fc69-4962-313f-b0ff-2c2a2b9eb2fd | 0.20924 | -51.50963 | 2026-09-05 05:01:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a18d5d-61f0-34ff-8b61-002ae4a21e0d | 2.36644 | -50.77832 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a4a389b-3119-37a0-a453-bd5b09d53c5b | 4.35421 | -59.73977 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c4331c3-6390-3025-aad8-78acd83d68f3 | 2.37233 | -50.76886 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6344e04b-d5bf-3c4b-926a-88fcd318c364 | 4.35798 | -59.73515 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93b7fdd8-a0dc-32da-b7f9-c4a792cbc2fd | 4.15213 | -60.01441 | 2026-09-05 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d33e1ff-55d1-3057-b56c-a44203dff90c | 4.27451 | -60.0506 | 2026-09-05 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c65348ef-49bb-38d0-ad36-7864e21f3180 | 0.20988 | -51.51369 | 2026-09-05 05:01:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d37a9d2-24ea-30a4-a13c-4acc37f96be7 | 3.85998 | -61.44907 | 2026-09-05 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aca2cd5-8d04-34b1-ae19-c16228e22842 | 0.2086 | -51.50558 | 2026-09-05 05:01:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2314d7fc-2dba-352f-acde-713428b4d0f2 | 4.88845 | -60.2956 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36bf18f4-7cbc-3ed0-b7dc-2074812fa895 | 2.45032 | -60.75792 | 2026-09-05 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ddfde1c-841e-3e25-ab2d-f222b8f74196 | 4.39429 | -59.7328 | 2026-09-05 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ef4732e-d96d-3e49-bfbd-f26658676f33 | 2.37167 | -50.76472 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d9da0005-d386-3aaa-bc1a-899442f3a7bb | 0.21408 | -51.51719 | 2026-09-05 05:01:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ed704e0-1d1e-3473-b541-4201d24e9cff | 2.36938 | -50.77359 | 2026-09-05 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
