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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 606c17f8-16b5-38ea-b25c-301c33090fed | -20.362101 | -48.723099 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 572a7c49-9e24-3fa2-82e3-4b1aa1da3e06 | -20.3643 | -48.734299 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6d451dae-d7f6-32d1-ab33-9367b489e892 | -20.348101 | -48.7029 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 458693ec-f2f3-308f-9ad3-0dcc03a82fdf | -20.350201 | -48.714001 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 70f0c1e7-e3de-334f-b99e-50a1977053cb | -20.352301 | -48.725101 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aa2b2c05-d5cd-3026-a80c-a4d459b7c050 | -20.3545 | -48.736301 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 318e00fb-1f53-3bca-b9e4-744d5c70755d | -20.400801 | -48.819901 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3887e032-4d27-3e31-bda9-6fc4a751bf53 | -20.403 | -48.8312 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 56058cab-90ee-3fa2-a321-279c159395c1 | -20.4051 | -48.842602 | 2024-10-09 00:37:44 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7248be28-c7e5-36dc-90e3-02d0c1ecea23 | -20.3608 | -48.769798 | 2024-10-09 00:37:44 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 009f99d5-c11a-3b59-9a6b-91e35b0c93f2 | -20.5578 | -50.098099 | 2024-10-09 00:37:45 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8144a59-c39b-3e87-afb9-e3a58d06bb23 | -20.560301 | -50.111801 | 2024-10-09 00:37:45 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 815d07d9-3db6-3988-9596-190cc0de81ab | -20.5506 | -50.113701 | 2024-10-09 00:37:45 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| affb009b-9018-3c22-b017-1418381ad1ad | -20.338301 | -48.704899 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 433f0ac8-a369-3277-a39f-55e03dfe143f | -20.340401 | -48.716 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6d788bd7-c563-3c1f-8ff7-902da279a0cb | -20.342501 | -48.7271 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 435e3962-14d4-3aaf-b25c-a00be9b02cef | -20.3286 | -48.707001 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae89d68b-366c-33a0-9bdb-68be9f7c8c7f | -20.3307 | -48.718102 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 55079b56-fc81-3673-95ea-a8f323189eec | -20.3328 | -48.729198 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61beaf12-b513-3be6-b397-18ed937511d3 | -20.3489 | -48.760601 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 140bb1c8-a55b-3888-b436-f66a813f2166 | -20.351 | -48.771801 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6ae1b19c-d313-3b85-95da-2cc2440da5ec | -20.353201 | -48.783001 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 18034e31-bdec-3a8b-ade9-3f57d8b2b7cc | -20.3346 | -48.845501 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 15b45736-f67c-3c21-89c2-a0c8905d901f | -20.3368 | -48.8568 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b6626907-04ce-31fd-8d5e-f66e95659ce2 | -20.3389 | -48.868099 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21d042b9-35ff-38ae-934d-450c055dcf7f | -20.327 | -48.858799 | 2024-10-09 00:37:45 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9940ea-5252-38c8-86f6-3b928fb452ed | -20.5481 | -50.100101 | 2024-10-09 00:37:45 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 45bf1c75-e03e-3a96-86cc-a872ca58138d | -20.5408 | -50.115601 | 2024-10-09 00:37:46 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2cc56344-3f62-3dd2-abc9-c555e657246e | -18.6299 | -41.121601 | 2024-10-09 00:37:46 | METOP-C | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1c339b0-9f0c-3c1f-8af2-0968cd94bd1a | -18.631901 | -41.129799 | 2024-10-09 00:37:46 | METOP-C | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f365f6f8-d0d3-3978-9cf8-494ba8df5059 | -19.0574 | -43.0541 | 2024-10-09 00:37:46 | METOP-C | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ef726a7-f1ac-3dea-8ac0-01dac8c893bb | -20.5383 | -50.102001 | 2024-10-09 00:37:46 | METOP-C | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f512e3b4-1044-30c8-a742-959e55d03a69 | -19.010401 | -43.211601 | 2024-10-09 00:37:48 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1960ba0-d95a-36fe-ab6d-cdee94386b9b | -20.010599 | -48.218399 | 2024-10-09 00:37:48 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 04488995-0f39-35f6-afa3-705064216109 | -20.0126 | -48.228699 | 2024-10-09 00:37:48 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3eca24cf-a4a7-337b-95af-453e0b53b910 | -19.262699 | -44.349201 | 2024-10-09 00:37:48 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e1661e15-e59c-3275-8e8f-96966873ebc9 | -19.251301 | -44.3442 | 2024-10-09 00:37:48 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 74d876b0-c6db-3e55-8437-76862a98d05e | -19.252899 | -44.351501 | 2024-10-09 00:37:48 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d36223d1-df12-3d77-9b42-18d7758cfb65 | -19.254499 | -44.358799 | 2024-10-09 00:37:48 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e4e4f36b-bed4-3941-8fc0-a25c0f958e72 | -19.2561 | -44.3661 | 2024-10-09 00:37:48 | METOP-C | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3d249c0-06e2-329a-b713-1dd0fc7d4931 | -19.6602 | -46.2192 | 2024-10-09 00:37:48 | METOP-C | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9190e093-a5a9-31e7-b115-33e6282287b8 | -19.6619 | -46.227299 | 2024-10-09 00:37:48 | METOP-C | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf92ed83-8d84-38bc-a42f-342cc1981de4 | -19.663601 | -46.2355 | 2024-10-09 00:37:48 | METOP-C | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 35d767c8-3618-30b3-ba45-dcf36cae8889 | -18.933701 | -43.146099 | 2024-10-09 00:37:49 | METOP-C | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 325b413b-b0dc-32a4-8ebf-01916e29ac88 | -18.923901 | -43.148499 | 2024-10-09 00:37:49 | METOP-C | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46d1cf08-8e2a-36c4-81dd-cad0a0181ddd | -18.9256 | -43.1558 | 2024-10-09 00:37:49 | METOP-C | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df0cf225-3ad3-3db3-ab91-cb070b06e146 | -20.116699 | -48.820702 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5b76b483-2ec5-3c82-82e1-c3996964d98e | -20.118799 | -48.831902 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2facc74d-f102-3a26-891b-0e60881fc5ce | -20.120899 | -48.843102 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9c222f35-21fd-3e7e-9e5f-84e18ca1dbd7 | -20.102699 | -48.8004 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40ed67ca-7ee9-34b9-a1eb-a7e27e1e54c8 | -20.104799 | -48.811501 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f431111-e3cc-3468-8cb4-ea652f2751a5 | -20.106899 | -48.822701 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ccdac628-393c-3308-9ac6-58c1d2a2a68f | -20.1091 | -48.8339 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88f996ab-7d05-3b62-8129-098ba602d25f | -20.1112 | -48.8451 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a2ab31e1-4df1-387e-bca7-5666889a6e4f | -20.092899 | -48.802502 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4085ea-e8c5-33d9-8869-b7f384317261 | -20.094999 | -48.813599 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b9f899eb-6c4c-3886-ab04-dbb4dd223bd7 | -20.097099 | -48.824799 | 2024-10-09 00:37:49 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3f68f9b7-72ea-3c98-844d-3f708b4702c2 | -18.5935 | -42.333801 | 2024-10-09 00:37:51 | METOP-C | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1060b880-090b-332a-aca0-1f7e9b22a978 | -18.5952 | -42.341301 | 2024-10-09 00:37:51 | METOP-C | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b81246ca-3a79-3bf1-8465-f47e6b4e546e | -18.596901 | -42.348801 | 2024-10-09 00:37:51 | METOP-C | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96ec6ca5-14fe-3db1-b368-fbce661122fc | -18.8403 | -43.787102 | 2024-10-09 00:37:52 | METOP-C | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 46d40d89-5306-3668-ac11-f382beb018a2 | -18.828899 | -43.782299 | 2024-10-09 00:37:53 | METOP-C | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 381749b4-a967-36b3-95d2-956f51d28d32 | -18.8305 | -43.789501 | 2024-10-09 00:37:53 | METOP-C | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bc3203fe-107d-3d4d-9069-734606031de4 | -18.8321 | -43.7967 | 2024-10-09 00:37:53 | METOP-C | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bbf07961-8a01-377d-917c-e7850c5c5142 | -18.410601 | -42.616501 | 2024-10-09 00:37:55 | METOP-C | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed43cc34-38a6-3f55-a1dc-e116cc1f96cc | -17.894501 | -41.423401 | 2024-10-09 00:37:59 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21c819e6-e0aa-33f9-aeba-8371430034e5 | -17.8965 | -41.431499 | 2024-10-09 00:37:59 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7dea1627-9f87-377f-9e96-3a7195df20e1 | -18.183399 | -42.5709 | 2024-10-09 00:37:59 | METOP-C | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 951894d9-0d7a-39ef-a663-1000b6fe1938 | -18.185101 | -42.5784 | 2024-10-09 00:37:59 | METOP-C | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c10bae6a-9cfe-3d3c-a7ab-6479cb39826d | -18.1868 | -42.5858 | 2024-10-09 00:37:59 | METOP-C | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1bf1ac70-0a93-395f-8754-a5c76da7129f | -18.237 | -42.940102 | 2024-10-09 00:37:59 | METOP-C | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10c65f98-4098-376b-878e-7119a206aaec | -18.238701 | -42.947399 | 2024-10-09 00:37:59 | METOP-C | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac54d605-ed79-3a60-827a-0e89ab35be97 | -18.2404 | -42.9547 | 2024-10-09 00:37:59 | METOP-C | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37e857f5-0494-3b94-ad2b-706e0d953e5b | -20.200001 | -52.9333 | 2024-10-09 00:37:59 | METOP-C | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 975ae376-3d06-3914-ac4c-49e62580afcb | -20.203501 | -52.953999 | 2024-10-09 00:37:59 | METOP-C | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58051a20-e983-3388-a89b-55fda3548d48 | -20.1903 | -52.935101 | 2024-10-09 00:38:00 | METOP-C | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 24a44d2f-699a-3d66-8d97-e4f279d39a6c | -20.1938 | -52.9557 | 2024-10-09 00:38:00 | METOP-C | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad51fcf-e47c-3ed1-8552-14b999e03955 | -18.053101 | -42.767899 | 2024-10-09 00:38:01 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 800ea79f-8f10-3308-be1b-a83cd5ee5561 | -18.0548 | -42.775299 | 2024-10-09 00:38:01 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57d1ddaf-77d1-3041-9356-640b80ef4a7a | -17.758699 | -42.076599 | 2024-10-09 00:38:04 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fd710a2-8314-3cb1-b9ea-03eafe270e82 | -17.8813 | -43.281399 | 2024-10-09 00:38:06 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba86a93-a753-3042-a4cc-70af4af4685d | -17.882999 | -43.2887 | 2024-10-09 00:38:06 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9e89e8-3f17-39e3-9a06-c7888dcdaa90 | -17.8699 | -43.276501 | 2024-10-09 00:38:06 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf2f439b-fb6b-3895-a561-d755781b8ef4 | -17.8715 | -43.283798 | 2024-10-09 00:38:06 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe5f0cc1-3173-3e6a-a7a4-2c27911b177b | -17.873199 | -43.291 | 2024-10-09 00:38:06 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3e12d968-c3ed-3559-8bd6-7b35414fde52 | -17.974199 | -43.7383 | 2024-10-09 00:38:06 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84030df0-69ff-321e-98e8-6a3994c539e3 | -17.9758 | -43.745499 | 2024-10-09 00:38:06 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e0c5074-026b-3a51-9913-bb8e776a4bf8 | -17.964399 | -43.7407 | 2024-10-09 00:38:06 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b80230f2-742b-3fec-81d9-4fd2ec1c97c0 | -17.966 | -43.747898 | 2024-10-09 00:38:06 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7b43528-3f3a-393c-b128-84c070a58313 | -17.9676 | -43.7551 | 2024-10-09 00:38:06 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6dfb6dce-a9fb-3d7c-99f1-6ad94db2351f | -17.993401 | -44.566601 | 2024-10-09 00:38:09 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5846aa48-d617-3be4-844e-bd11fb39f613 | -17.9949 | -44.573799 | 2024-10-09 00:38:09 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| beeb1ad4-2876-3b0d-827d-d595f39c4f55 | -17.928301 | -44.551601 | 2024-10-09 00:38:10 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f4e4df21-ff27-3372-82c8-6193cabd4ca1 | -17.929899 | -44.5588 | 2024-10-09 00:38:10 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c16ed519-12ac-3be3-b37c-84831c7872ae | -17.931499 | -44.566002 | 2024-10-09 00:38:10 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 85de1046-3487-3223-ae39-d7e4710bb0da | -18.0413 | -45.401001 | 2024-10-09 00:38:11 | METOP-C | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 202aba4f-a9fe-38d3-a20f-e55ab19b1cb4 | -18.0429 | -45.408401 | 2024-10-09 00:38:11 | METOP-C | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb46c2e7-dd72-3a5e-974e-b7e89e887ceb | -18.239401 | -46.8223 | 2024-10-09 00:38:13 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66ce433f-1bf0-37f5-9852-b901cd38ea2b | -18.2411 | -46.830601 | 2024-10-09 00:38:13 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3223e499-f377-36c0-b292-0384c3a78082 | -17.0056 | -41.994701 | 2024-10-09 00:38:15 | METOP-C | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README11.md)
