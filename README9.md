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
| 43fbcb2c-0626-38b7-aa87-4d4770b2ed7a | -12.81458 | -47.93711 | 2025-09-13 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ab1c9b88-8d1e-3fad-bd9a-e185ac9f14e5 | -15.59747 | -54.7729 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec8448fa-1f25-3f53-a9cc-c0bf22b75378 | -14.20076 | -46.24331 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 4cf68aa5-7604-3073-b946-8ed95d6a423b | -17.4132 | -49.24952 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5f4eb63c-c890-34a6-bd42-0c158bf35c0c | -15.46214 | -47.34064 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| f661a9c6-d6c9-32a3-b0b2-fbf9cffd656c | -11.49146 | -43.70935 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| e3817ece-b19d-3c3f-9c97-85faf3f89bac | -16.09599 | -49.95668 | 2025-09-13 00:50:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 64fa16d8-3a6d-3e0d-8cc8-7d4b125e74fe | -15.20524 | -56.69051 | 2025-09-13 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 82a140a0-1db3-3cf3-a378-73b08a2470db | -18.82607 | -49.57671 | 2025-09-13 00:50:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| dfa4c141-d940-325a-bb7a-644291d86ce7 | -11.37927 | -47.32594 | 2025-09-13 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a6903761-277c-3029-b869-eec92e685882 | -14.97836 | -49.56345 | 2025-09-13 00:50:00 | TERRA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 338a8758-3da5-3d62-bbe8-935feebab38a | -19.65953 | -45.88065 | 2025-09-13 00:50:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f3abb040-3d35-3bcc-a17f-7ca694ebb282 | -16.53104 | -51.73261 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e64d2fde-3ef4-3a0e-a4ae-9194abd403fc | -11.2303 | -54.9929 | 2025-09-13 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| df8723de-5628-349c-aeaf-bcfbbbad0449 | -18.04746 | -45.43022 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 209c66ee-0b4d-3fc8-af51-d6f6036f30c2 | -17.83007 | -50.40955 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 59b862d1-a781-36ed-906a-9cee5ccbf571 | -14.41471 | -46.40228 | 2025-09-13 00:50:00 | TERRA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e1d53d33-7593-37c6-9560-f34e7ecb98de | -11.14286 | -50.71851 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f87cbd32-8feb-3bda-9f7e-e80c53947c01 | -11.78114 | -47.39009 | 2025-09-13 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c28124de-5cf1-3910-a14e-25d49b51cfc1 | -14.20647 | -46.27753 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 1f17c4bd-499b-35b2-b789-708f3ccd0194 | -17.29946 | -48.7429 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6efd4d86-738f-3ebd-9b7b-e0300e0ecfc1 | -11.82116 | -50.56599 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1a7d60d4-ec58-371c-a1e0-6f2b833e4ba6 | -12.112 | -44.88879 | 2025-09-13 00:50:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 61efb3a5-63cb-326a-8c28-ace472126c55 | -14.49344 | -53.92734 | 2025-09-13 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 27b40d98-a1f8-375a-b32a-eefb633e59e4 | -11.07174 | -51.50925 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0997f155-af44-37a5-b791-b30d07f60d2a | -16.55167 | -49.22956 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bf1f8208-05b9-3ee6-a631-e85ec114ffe8 | -20.02259 | -47.64441 | 2025-09-13 00:50:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 19ad7e0e-08f3-3110-a66b-315fa413e4de | -19.98865 | -46.9054 | 2025-09-13 00:50:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5a6845be-f544-3dff-b548-6d1effa1e877 | -12.65629 | -44.25397 | 2025-09-13 00:50:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 81e41c3b-2a4a-3159-8b5d-6ac31ce46cb5 | -14.5954 | -52.52848 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a08af800-c236-38fe-ae1f-49fb7c4b3e53 | -11.17127 | -51.43187 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 5c791d47-083a-3167-86dd-01bc82d3688d | -14.45677 | -47.32981 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8b4ec101-140d-3008-a276-fa1ae0e7cd76 | -18.61241 | -48.20792 | 2025-09-13 00:50:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ac404091-7c87-3cde-b974-f16d2d5e14a1 | -16.86309 | -49.33618 | 2025-09-13 00:50:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 63959bad-007a-30a6-a166-8d370b9c90e6 | -16.25109 | -50.07295 | 2025-09-13 00:50:00 | TERRA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 70e75c4b-2029-328b-90b5-af99b937fa69 | -16.79295 | -51.36564 | 2025-09-13 00:50:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7f4d822-977e-3034-8b52-ac283bae462e | -11.72203 | -46.57992 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 336629ed-7884-395c-92cd-8e0dc40d38b3 | -17.42385 | -49.25803 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d8b3c6b7-7da3-3a72-9abc-01a300d7fc48 | -10.76544 | -50.52995 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 85beeb9d-1397-35f3-93c5-138a3ada20d9 | -16.5145 | -55.19279 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| 2bd43816-ceb2-38a4-be37-558a2fcaccc9 | -16.644 | -49.79248 | 2025-09-13 00:50:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f7feebec-668a-3068-b44e-324563aefd60 | -11.2157 | -54.99037 | 2025-09-13 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f3777ed1-abbb-3c96-9d36-6703a1725f50 | -10.45862 | -50.02419 | 2025-09-13 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a42276a9-8dd0-3989-82ab-c2d83dce03fe | -14.21131 | -46.2826 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a6446344-cfd2-3b32-960a-de0eeaf46a93 | -13.40632 | -46.80842 | 2025-09-13 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6751fb42-e327-38eb-96e5-dc1f2411c1db | -11.09071 | -51.45019 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9db766d-54a7-306d-a6f9-20a376e3acc5 | -14.43575 | -52.92094 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35edff20-d261-39a4-85b1-03baa3acd914 | -12.94054 | -54.74848 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3f639337-e99e-394d-9e59-e7fea70bbe7c | -17.44735 | -49.2374 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5846298e-31bc-351d-836e-543404fa6d1e | -11.15711 | -51.39639 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 76088f25-bbb0-3f6b-acce-d4d27f413e9e | -16.49504 | -55.11809 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| f6c5ca2b-0964-3207-9973-f9572b0faec8 | -10.75761 | -50.54129 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c29d168d-672c-3e4d-a70f-eec25c509286 | -11.08048 | -51.44233 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 20f8a34a-e282-38f1-967e-06e846947543 | -11.17257 | -51.44106 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 74ab490c-feef-3ee2-969c-717caa54ac83 | -11.15449 | -51.37796 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b95cb47-351e-3cc8-9a7d-398cf1c84bbb | -18.96906 | -48.607 | 2025-09-13 00:50:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 03f8bd79-c82d-3f68-98c1-c78c892ca9e7 | -12.00275 | -47.77561 | 2025-09-13 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 878b712e-c150-37ec-a14d-a9a27ff44d74 | -16.25873 | -50.06219 | 2025-09-13 00:50:00 | TERRA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 35f2017a-dad3-3e0a-822f-d8d93d9a7b82 | -17.4209 | -49.23792 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f689555d-c163-3b1b-9503-b951496e8f6b | -14.2124 | -46.24061 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 240e02ce-4174-3869-ba58-a0c5119aa54c | -16.33719 | -51.53054 | 2025-09-13 00:50:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 21c0630d-19a3-3ded-a306-14d0d38956fb | -9.97589 | -50.30606 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5e7f0f49-581e-304c-8d03-4c5e39bf3cc1 | -7.9114 | -55.26477 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0168ba3-1e4a-34c6-bf94-ac15b64aaaa5 | -8.94019 | -62.16645 | 2025-09-13 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 987d809c-c033-3e5e-a58f-95206cf5ac0d | -10.01766 | -50.39434 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 966363ba-2b6a-34c5-a1e4-c7979ee828bc | -9.2326 | -51.21991 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b63ecf7e-20b0-3132-a1bf-185fb369b852 | -8.07958 | -54.73777 | 2025-09-13 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74e2934b-568e-381f-a9b6-6d6fedd16553 | -10.10296 | -59.16925 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 7cf82f05-68d5-36fb-a126-28af2aa7bf97 | -3.24839 | -46.78901 | 2025-09-13 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6526c76a-04a3-380d-9130-7fc2fcf3eca7 | -10.70093 | -54.45401 | 2025-09-13 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 86f7021a-599b-3a3c-aa38-8e107ca649e9 | -9.57598 | -53.60826 | 2025-09-13 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 09fd8d9d-18c6-3857-9141-4bc90780ef93 | -3.21384 | -47.12222 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f149f077-175a-36da-9922-59e01c5e21ad | -3.22665 | -47.64259 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 8f9a8b40-79ed-367c-9c15-78ee0025d05f | -10.44616 | -50.62723 | 2025-09-13 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8858a545-4fa3-3c37-87bc-3996f733e233 | -9.88742 | -51.86662 | 2025-09-13 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6dbbe8e0-7977-38ec-8e56-e64e939d2693 | -10.33213 | -58.02051 | 2025-09-13 00:52:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fc720913-a5fe-3386-8776-5272de6c4d8c | -10.20008 | -51.67201 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 834d7f10-158c-3321-8ecb-192a586ebc1a | -4.28134 | -56.3317 | 2025-09-13 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 95b814c9-81f2-3fab-b63a-c638aa29ab2a | -10.69964 | -54.44418 | 2025-09-13 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9bf27d62-54d0-3fda-81be-d43fac3423e9 | -10.5271 | -51.50554 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0bd90b99-d57b-3bbd-866c-31cb748584e7 | -3.23063 | -47.14245 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b0cf2b61-a862-3f87-a063-4901571ed5b4 | -9.73352 | -46.89839 | 2025-09-13 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 322c0c82-a557-3a38-9986-d6cbb4755b45 | -9.7052 | -47.5314 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cc6f15eb-da4a-302c-865c-932c2809ed77 | -9.24002 | -51.21238 | 2025-09-13 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ad3d5526-bbd4-32bc-bb31-80f343252944 | -4.62297 | -47.41623 | 2025-09-13 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f61859bd-75cb-3bdd-94a4-66e862ea83b7 | -9.25126 | -57.06712 | 2025-09-13 00:52:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3895ecb6-0ab4-3a9d-80c5-016d90f9e143 | -9.48888 | -46.43495 | 2025-09-13 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3c3e6d0d-c5f0-370b-a229-4db5efd653e1 | -10.09012 | -59.17097 | 2025-09-13 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 099ab0d7-6294-320d-ae0f-922125add5ae | -10.5068 | -51.55539 | 2025-09-13 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f04d1e71-75c2-35ad-8db8-862dd10f5102 | -3.24395 | -46.80711 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 111b33b2-3e4b-3a2f-87e0-ee91e6bdb81d | -9.26197 | -57.06578 | 2025-09-13 00:52:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 938574f8-964b-3ab3-99a5-2bff58aae692 | -9.06053 | -47.03593 | 2025-09-13 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3dc79777-e00e-314b-b82b-a5892b4570c3 | -3.2192 | -47.12711 | 2025-09-13 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ca06d5f7-b62a-3f7e-8df7-8f0b5f0edd82 | -9.70876 | -47.53649 | 2025-09-13 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| bedc368c-7e3c-37a3-830b-6810130890e8 | -9.83844 | -54.53474 | 2025-09-13 00:52:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3fa9873e-908f-3adc-967d-6871537992ba | -9.74569 | -46.89653 | 2025-09-13 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 95cec59c-81c4-3227-955e-580186a114a1 | -10.27308 | -57.80447 | 2025-09-13 00:52:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 42794900-cfaa-37ab-8ef7-24e129e108e2 | -10.93526 | -56.21209 | 2025-09-13 00:52:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b4573b49-1904-3a04-aeca-2798fad6257a | -10.33419 | -54.32143 | 2025-09-13 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ce3daad7-d080-3c66-a83a-f85bc206d6e8 | -9.52894 | -54.63485 | 2025-09-13 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |


[Clique aqui para ver as próximas entradas](README10.md)
