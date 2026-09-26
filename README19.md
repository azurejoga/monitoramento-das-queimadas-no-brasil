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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2401fcc1-765b-308f-9fbe-bc58145f92f1 | -10.75779 | -50.83976 | 2026-09-26 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 010d49f1-9191-37f4-8614-0662e92fcc2e | -13.42578 | -41.33104 | 2026-09-26 04:27:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11fc1bee-a6b5-3580-804f-9a890b3b2951 | -13.71318 | -48.80667 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7510f73-6695-3413-865b-588f8f1dc54d | -11.028 | -54.05112 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd5ea091-99ff-36c4-a1f7-4fe09c9fb1ee | -12.17626 | -50.32936 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4282b92c-86d9-3655-ba84-20be1e3855a9 | -12.17329 | -50.32397 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4fbde2b8-8821-3c68-81f8-a8193631d6a5 | -11.93895 | -50.69642 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9b9d79c-b8c7-3494-a52f-3f26438c69d7 | -12.25765 | -50.74024 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d8b6aa5-370a-30eb-9509-8f9a98aa5891 | -11.92031 | -50.59621 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cde8de89-a218-37ed-a52d-cc8d5efb1f41 | -9.46221 | -40.33593 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bbecaa0c-23d1-367e-9704-6e3a516ec7f9 | -9.46783 | -40.32558 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 14b504dc-b59b-3e57-93ea-0c203d13b9d6 | -10.7584 | -50.83625 | 2026-09-26 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 41b0ee98-8564-3818-8bf0-b70a27fc6569 | -11.02312 | -54.05006 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e01942c0-3bd4-370a-850c-c6598a6854fe | -11.79297 | -50.65765 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bbf3d15-c807-3ae6-b6ce-a8d8846252a3 | -11.94103 | -50.6891 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c4bfc24-fc63-3f54-b40f-b42d10267623 | -14.90708 | -43.41096 | 2026-09-26 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69910ac0-26d9-3efb-b17d-1505b0367ff6 | -13.85802 | -46.37476 | 2026-09-26 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b4fe26a-7e1e-36be-9ae5-9ae64173f7fe | -13.42241 | -43.67185 | 2026-09-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ece84a-af53-388a-a116-a7a0894a05dd | -11.02669 | -54.04965 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 222d5a70-b47e-3746-b403-e682301e8f6d | -11.85122 | -50.55133 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9186e116-ecd2-3866-8f29-6b4d41b5991e | -12.21916 | -50.3496 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97a294f6-bcca-33cf-b9f9-97b84bdf94ed | -10.4069 | -53.81241 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96d0830b-9172-378a-b760-26559b960a12 | -11.95484 | -50.6737 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cf1ddb1-b2e7-3c82-95f2-d545c354ac52 | -12.26152 | -50.74095 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7597c5-7a5f-3be8-9cf6-a361387f2bf3 | -14.87554 | -47.13273 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9ec8e729-fbfc-3756-8a7e-23aaa738051e | -12.6614 | -54.64351 | 2026-09-26 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb91e7b6-514f-3876-bf7f-9a24fddb6d22 | -8.19289 | -54.82729 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2efae47-210e-30b5-b714-b86b538209a1 | -14.87885 | -47.13329 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a6d5956-879b-388e-8525-f6ed52ef3bab | -11.03394 | -54.04661 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 032b6e9d-5f60-3126-8184-b837204b7038 | -11.93748 | -38.29747 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 9c6a2923-4ae2-3fc3-b860-d0f9795f9311 | -12.6675 | -54.63855 | 2026-09-26 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de28821e-23b4-35ec-a7b8-6e58a6ab89d2 | -14.8816 | -47.13741 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c697e6b-388d-3dc3-92e2-99e119beaf13 | -14.86839 | -48.21048 | 2026-09-26 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0da8b80-f1dc-368c-af9c-599868a74a01 | -12.28695 | -50.73735 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cf70e03-e0d2-3fc8-8138-97c1a109b0f7 | -13.42531 | -41.33451 | 2026-09-26 04:27:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5d1cf2a-6b6e-3c28-8c11-1e07843031cd | -11.75767 | -50.63079 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62f1c738-4d17-39d9-8dbc-aaa2f1e89334 | -11.27528 | -54.43588 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d63ab347-7934-3242-9fd7-1f7a4f16e424 | -13.7098 | -43.68406 | 2026-09-26 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d43d41a-7904-3bfd-8f23-a11478f1d627 | -13.68896 | -48.80265 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 968745d7-edea-389d-b59c-abf4038d9295 | -12.22007 | -50.34702 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 763cbbbc-8f7d-31df-a072-31249cba6969 | -11.0159 | -54.05317 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc72850e-533c-39c0-9d2c-68286f632a3a | -12.15897 | -50.31654 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4274ed27-edd9-3721-9a2c-38d269cae798 | -15.24381 | -43.27043 | 2026-09-26 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 763a2934-e6db-317e-8d36-13bdf76fe3ba | -15.42281 | -41.51683 | 2026-09-26 04:27:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb6fce69-4f00-38b4-b33a-18b0d4cc2d53 | -8.18811 | -54.82276 | 2026-09-26 04:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d74599d-0787-31dc-b346-2602bf20c871 | -14.86504 | -48.2098 | 2026-09-26 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9db12f47-13b8-3199-a26a-ee8710561a81 | -15.19747 | -49.29625 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af9b3a47-6e69-3bab-b770-824a5d3f9a24 | -12.25898 | -50.73736 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 629e6729-2e2a-330c-9e05-f74778cb8771 | -9.54116 | -56.16477 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 468991c6-a1a1-3dae-b8f5-46f5af55d252 | -12.12808 | -50.29502 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0613b218-6c0e-3111-97c4-636d26da3559 | -15.89349 | -43.47464 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46694b65-871f-31e0-aab8-c40ac81cd9f0 | -12.02716 | -50.65374 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9d213dc-abad-3c12-8313-5117f10458ca | -12.23613 | -50.72608 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d2de3c6-92c2-3470-b5ca-d02704194604 | -13.80105 | -43.75094 | 2026-09-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18f849c0-d0bc-3634-8f2b-63e1d5427305 | -12.24862 | -50.35979 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e49b794b-6edf-33bf-8e5b-957d0605654d | -11.93274 | -50.59341 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a26fde6e-734c-32fe-a217-0b2c2ddf94df | -14.87497 | -47.13629 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a821967c-2bb5-3353-8372-85e4f7e45bb4 | -13.00239 | -48.67235 | 2026-09-26 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7647590-feff-351a-8d50-3ab3fa060473 | -12.26105 | -50.72044 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7db3d0a6-f557-3940-a6b0-4decc09efb1c | -11.77832 | -50.64987 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e44bdf-0d77-37c1-b820-8322cbacbebe | -11.7822 | -50.65057 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b1846db-96b2-3770-895a-51bb6f2628fd | -11.1727 | -50.04363 | 2026-09-26 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62de2088-41ef-3ef6-baee-18102c60a77e | -12.24483 | -50.3591 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4792af15-a8ba-3cc3-b953-08fc598fcfc2 | -11.13688 | -42.82609 | 2026-09-26 04:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be5324e0-3ce9-393d-80c2-0cccdcc34172 | -11.94794 | -38.29313 | 2026-09-26 04:27:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bed08826-a36b-356c-8c01-e3e341731e50 | -11.7918 | -51.00528 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2abee415-ff35-3d89-b603-d72189f1b1db | -9.53694 | -56.15561 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98f4c45-40f2-374c-987e-ba5f6177c5af | -12.60018 | -51.95261 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915bee3b-de86-337b-9de5-83d0ac1781ef | -12.2655 | -50.72325 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fc8cb1ba-8108-3d30-b2c5-c7fb512a409f | -12.12728 | -50.29972 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 147c6fff-b4f8-31a7-9c72-d09897851772 | -13.69522 | -48.80769 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63c35e43-ea49-3b0d-9286-b00fadeb50fe | -11.90659 | -50.5836 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f544b6d8-94b5-3701-af63-1240ff8c7c38 | -12.60364 | -51.95718 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac375c0-3ff0-36b1-9df2-10f5ce8f8b48 | -15.88918 | -43.47853 | 2026-09-26 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89146d35-f896-3ddb-afe6-88f06839f8cb | -12.26672 | -50.73877 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76410043-43e2-339a-ba9c-60cc6ea90cbd | -11.27561 | -54.4372 | 2026-09-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 052a0779-40db-30b9-95b2-a22eb8ba1065 | -9.53617 | -56.15959 | 2026-09-26 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 471474c4-76d3-3650-82fe-396ed717194c | -11.79383 | -51.00394 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6ba80c-9b86-3c1d-bf58-a2691053201d | -12.59102 | -51.94725 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64e6a551-d20f-308c-b49c-26b3314f5335 | -11.93189 | -50.59831 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbfdad41-281c-3421-a5d6-e77ea9131cb2 | -12.2585 | -50.73529 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ab17e32-1dce-3280-8f62-0d3638b674ca | -12.24171 | -50.7169 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da78d817-f9f3-35c8-96d8-30a86baa7c61 | -15.57876 | -48.84329 | 2026-09-26 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 102d02df-8bce-3df8-9c56-5c438fa883b0 | -9.4714 | -40.32984 | 2026-09-26 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 8029d514-46fe-3b0c-aa29-ecc7844b9a61 | -11.7318 | -50.61335 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62775359-e7c9-3acf-b9ce-704228878031 | -15.19534 | -49.28767 | 2026-09-26 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac74e3a4-7a9e-3fdd-a838-1a70ff681cc1 | -11.85944 | -50.85312 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e9928dd-a2fb-31c9-822f-b4874373badd | -11.95871 | -50.67441 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb6a3f4-6a7a-3eae-9732-fd413b95875d | -11.78996 | -50.65198 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff560d99-7818-3df0-be08-5911fc52bfad | -12.29597 | -50.33439 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dafd40f8-0323-3ebd-9f14-7f1d32ffc04f | -12.26539 | -50.74166 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d1622f-8d80-36ab-a837-4def6275e310 | -14.87223 | -47.13218 | 2026-09-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8185f6a1-8d96-3262-8cce-0d9a75dbe258 | -12.17707 | -50.32466 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c43de788-7a51-350b-9e47-4392e10fd18c | -12.68223 | -47.29029 | 2026-09-26 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a42c5d-ee05-3bb9-8bfc-bae5c300b63e | -12.60087 | -51.94882 | 2026-09-26 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b513e7c-01e6-32db-b43f-6462381510ba | -13.69176 | -48.80714 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f53d032a-8da3-3afc-bffc-459e4c80b025 | -12.24558 | -50.71761 | 2026-09-26 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdaf5ca6-e22b-3516-94dc-810febbf6c51 | -10.41768 | -53.80883 | 2026-09-26 04:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1882dec-a4c8-3bb6-b19c-3558f1bf802b | -11.79115 | -51.01958 | 2026-09-26 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bbc79d1-b452-3023-a24d-c233fb189808 | -11.87746 | -50.56821 | 2026-09-26 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README20.md)
