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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2860d363-7ae0-3c95-9ad4-75fb115f2eb1 | -18.7549 | -47.1133 | 2024-10-03 00:08:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ce8c166a-17b5-34c8-8300-6a13aee0bba2 | -18.7577 | -47.128899 | 2024-10-03 00:08:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b42d7c2a-c16f-362d-a908-84c3dbdc7558 | -18.7451 | -47.115101 | 2024-10-03 00:08:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40475337-0f9d-3f1b-b64b-179a8397392d | -18.7479 | -47.130699 | 2024-10-03 00:08:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 508c4a6e-b4f1-31c0-9a9d-a0ffdd9572ef | -17.8552 | -42.877998 | 2024-10-03 00:08:23 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9c6b6ad7-b4d1-3a3f-840f-3c56bc625d34 | -17.424299 | -41.053799 | 2024-10-03 00:08:24 | METOP-B | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d12ba58-173d-3b4c-8c93-bd8cc0cff481 | -17.402901 | -41.582401 | 2024-10-03 00:08:26 | METOP-B | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5dd02839-d521-3fa7-b3ed-3149c49d13cf | -17.404499 | -41.59 | 2024-10-03 00:08:26 | METOP-B | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24a77924-f12f-3d29-85cf-732efc40c606 | -17.325899 | -42.4911 | 2024-10-03 00:08:30 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3064aea7-450d-3a38-8334-3c2b73c74208 | -17.3276 | -42.499199 | 2024-10-03 00:08:30 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cfc8a9ef-74fd-3f6a-aaeb-baa2689ec484 | -17.329201 | -42.507301 | 2024-10-03 00:08:30 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 808f2718-aa1b-30f6-b3cf-226a6ef692d7 | -17.254999 | -41.9524 | 2024-10-03 00:08:30 | METOP-B | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e538b71d-2235-3b23-bd32-927c4af9b269 | -17.2521 | -43.180099 | 2024-10-03 00:08:34 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7e0bf68-ec51-3988-9f4d-95f1ae72eb01 | -17.594801 | -46.948299 | 2024-10-03 00:08:40 | METOP-B | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0e2dd70-8583-34de-b4a1-9d9c5a478a47 | -16.9072 | -45.293999 | 2024-10-03 00:08:46 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d04680f-e7a3-3ff4-ae4c-fe912493576f | -15.6722 | -39.214802 | 2024-10-03 00:08:46 | METOP-B | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e814e297-5808-3b59-b6db-8e0c4006637d | -16.329399 | -42.281101 | 2024-10-03 00:08:46 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb1e4b5f-b7b8-3b53-b3f9-ca5a20beb372 | -16.3311 | -42.288898 | 2024-10-03 00:08:46 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1758ef70-4e33-3dde-ada2-0d95f521ba19 | -16.332701 | -42.2967 | 2024-10-03 00:08:46 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85b6195e-0793-3ad6-9b79-17424ffbfdd1 | -17.110901 | -47.118999 | 2024-10-03 00:08:49 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec146755-6ed3-30cf-a09e-46c9c8a07ba6 | -15.8072 | -42.478802 | 2024-10-03 00:08:55 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa1977c-48d7-3240-8aa4-5da58591663b | -15.8088 | -42.486599 | 2024-10-03 00:08:55 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8102a64a-0041-38aa-9b95-eef026ed1f05 | -15.4383 | -41.135899 | 2024-10-03 00:08:56 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8928872b-302c-3def-89cb-c58057583a56 | -15.7684 | -43.5742 | 2024-10-03 00:08:59 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 107ce05f-0b2a-328e-8f51-26b3664d91b0 | -15.0747 | -41.927799 | 2024-10-03 00:09:05 | METOP-B | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c6e1c49-7436-3e7f-8db3-5777ae2e796c | -15.0763 | -41.9352 | 2024-10-03 00:09:05 | METOP-B | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10594c91-12a0-30af-a9bd-98a758dfabc6 | -14.9966 | -42.234501 | 2024-10-03 00:09:07 | METOP-B | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0652db6c-75b3-3ece-bcc2-7ad04781324e | -15.2348 | -43.3186 | 2024-10-03 00:09:07 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1b61504a-135a-3690-8485-9e35cc66e3e6 | -15.2365 | -43.3269 | 2024-10-03 00:09:07 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3da28757-8c1a-3baa-8bf9-0e01dc6a352a | -15.2382 | -43.335201 | 2024-10-03 00:09:07 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3537b6a6-7818-3767-a47c-877df75f45d8 | -15.7765 | -47.659599 | 2024-10-03 00:09:12 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| e7e89221-06a2-36f7-8cfc-999376827466 | -14.7578 | -42.414299 | 2024-10-03 00:09:12 | METOP-B | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0a2cab84-adb2-34c8-b5ba-56d8eec27cd4 | -14.6107 | -42.494801 | 2024-10-03 00:09:15 | METOP-B | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3970f77c-8809-30a1-975c-4c5c12449362 | -15.2482 | -47.4855 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee653b93-cb36-3b28-937d-35482629d2c5 | -15.2509 | -47.500099 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a101948-dd53-3ed2-b29c-9b3a5cb1215c | -15.2384 | -47.4874 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1980996a-5696-3be1-aa0b-cb3f700fb0e6 | -15.2411 | -47.501999 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5debb4f-0f72-3f85-afce-b8d3411b7882 | -15.2287 | -47.489399 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7746a049-536b-35cd-a2b5-0ca041175ef0 | -15.2314 | -47.504002 | 2024-10-03 00:09:21 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 60283cdf-cf8a-37f0-9f6b-b9357e1004fe | -15.1437 | -48.056999 | 2024-10-03 00:09:24 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3d6b48b2-56f5-31f4-8676-436a9fd4c496 | -15.1467 | -48.0728 | 2024-10-03 00:09:24 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ffd207b5-c119-3f6a-9a93-b7c1f196c3a8 | -14.5191 | -45.2141 | 2024-10-03 00:09:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b05bc9c-4ec1-3fdf-b96a-5b928cc2d158 | -14.5211 | -45.2243 | 2024-10-03 00:09:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad830354-a85c-3680-8783-1d274b58d2af | -14.5114 | -45.226299 | 2024-10-03 00:09:25 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f88f16f-f0c4-3024-a40f-ce2bac6e02a5 | -13.752 | -42.6064 | 2024-10-03 00:09:29 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e80b6f4e-1731-3895-89db-a9d0bb695ff7 | -13.9889 | -44.0215 | 2024-10-03 00:09:30 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37bf15e7-d56c-3669-8954-75eee01f213a | -14.0342 | -45.086498 | 2024-10-03 00:09:33 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eaa87150-633a-3a8d-8813-d9b9458161f7 | -13.3064 | -43.695301 | 2024-10-03 00:09:40 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90e9f3d1-b7eb-3548-83e0-1c632d2e72ba | -13.3081 | -43.703499 | 2024-10-03 00:09:40 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 095f42ab-ea86-31c9-8ade-47db0f2f085f | -13.3098 | -43.7117 | 2024-10-03 00:09:40 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfb8b928-cc50-3d80-82ad-f6f7cf17ea42 | -13.2983 | -43.7057 | 2024-10-03 00:09:40 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 674dfd50-9889-3570-b2c7-5df4af7d96ff | -13.9508 | -52.536201 | 2024-10-03 00:09:57 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0cded5-8ea9-36ad-ad1b-6bb9d54b98cb | -13.193 | -48.588501 | 2024-10-03 00:09:58 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4e4d114-877b-3169-b4a4-f888d07296c1 | -13.1961 | -48.6045 | 2024-10-03 00:09:58 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 563d3a76-9002-37d4-8166-587a71ac3889 | -13.5605 | -51.191799 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 725dce05-186f-346a-b7c1-41fb70cfcee6 | -13.5463 | -51.169102 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0b4b266-9b62-34b5-acd7-449feb16c578 | -13.5508 | -51.1936 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2f49bb0-91f0-399c-b256-72ecaa601a2c | -13.5553 | -51.218102 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3171be3-62ce-3d9c-9159-3b33ec9ff04a | -13.5411 | -51.1954 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc7bca9-a35e-3070-b57b-6c55d4c31a1c | -13.5456 | -51.219898 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b386bd6-5e32-39e6-bbcc-54bdac6f983e | -13.5501 | -51.244598 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 455e8a78-461b-34c7-bccb-c7d6fd4fb616 | -13.5136 | -51.099701 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 857732a7-d7ee-3683-a1cb-bb2f45e7d0f4 | -13.5314 | -51.197102 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc6b030-8bc5-3dd9-8f0e-7cb230e8672e | -13.5359 | -51.221699 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32f56a74-0b86-313b-a8b4-dd64909f2a63 | -13.5404 | -51.246399 | 2024-10-03 00:10:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f639fc0a-87c4-3ada-813a-47a5b73a6c41 | -13.5039 | -51.101601 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe069c5d-65c9-34c5-9b46-b2006d6ea3d2 | -13.5084 | -51.125801 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98d9f7c0-0969-3963-80e9-65480d6fba93 | -13.5217 | -51.199001 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bad779b-79c8-3577-95b7-147e319e5ec5 | -13.5262 | -51.223598 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e96b9747-0929-38a5-a73e-81970802be3f | -13.5307 | -51.248299 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d132ee13-b0ee-36c1-9ed0-54d8dda86d4f | -13.5121 | -51.200802 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8db2be66-310b-356b-9883-45df2764c8be | -13.5166 | -51.225399 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dac80446-5ab8-3deb-89ee-c3b644fb12db | -13.5211 | -51.250099 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6660b6af-5b6c-3e22-a943-baab6f74f701 | -13.5024 | -51.202599 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c84250c9-a779-3316-ba1b-9cb61597270c | -13.5069 | -51.2272 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b081c20b-faa6-367c-b5fe-cef18c3ff3d7 | -13.5114 | -51.2519 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8191ef7-c241-3584-b0ee-79e8440ef05c | -13.4972 | -51.229 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cac1b4d3-c24f-3c23-8668-80d2e79fc6f7 | -13.5017 | -51.253601 | 2024-10-03 00:10:01 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a986469-1525-3961-8832-e1b82390f8f7 | -11.5616 | -42.171001 | 2024-10-03 00:10:03 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8107a5cc-644a-3546-8ba0-ea8ef5e0591d | -11.5631 | -42.178101 | 2024-10-03 00:10:03 | METOP-B | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dda970af-920c-3fdc-9781-b89a7646f8d8 | -11.8349 | -43.812901 | 2024-10-03 00:10:04 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca2de8a-bdf5-3ccf-9e70-1c420975c1ba | -11.8366 | -43.8209 | 2024-10-03 00:10:04 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3eab0f93-2643-3e3c-9ec6-dfa9a8aeec87 | -11.8383 | -43.8288 | 2024-10-03 00:10:04 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce69d3c7-0a57-32a1-be2e-0d2f22da57c2 | -12.2723 | -45.9529 | 2024-10-03 00:10:04 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd3b338-3852-3ce5-8e97-96441b9ed865 | -12.2744 | -45.963299 | 2024-10-03 00:10:04 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5ac2bf7-104e-32a2-8b25-779702793298 | -11.9386 | -44.5439 | 2024-10-03 00:10:05 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5b60b5b-be06-326b-aed6-4500b8545456 | -11.9404 | -44.552502 | 2024-10-03 00:10:05 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9e7fa7-f112-31b5-bc07-fe8f10b5fbd7 | -11.9288 | -44.546001 | 2024-10-03 00:10:05 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24d6f346-6c39-3d3e-b03c-14d47371b658 | -11.9306 | -44.5546 | 2024-10-03 00:10:05 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7593410f-efc8-3a6b-9472-a79b3ab75f89 | -12.2604 | -45.9445 | 2024-10-03 00:10:05 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4414163-8831-3bcd-af0a-50255733b55e | -12.2625 | -45.954899 | 2024-10-03 00:10:05 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4fc29a6-789e-32f3-8ac8-2d3a6a566790 | -12.2646 | -45.965302 | 2024-10-03 00:10:05 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a54436a-de0d-3e0b-a5ae-765a50293d9f | -11.2108 | -41.053699 | 2024-10-03 00:10:05 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bb0439c4-4214-3208-a4e8-1e05a4af0eee | -11.2124 | -41.0606 | 2024-10-03 00:10:05 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f1629cb2-9059-3d18-9626-4ea5fe1a9ea4 | -12.1978 | -46.738098 | 2024-10-03 00:10:08 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0aeb9d95-bb34-348a-95ac-cced337bcb7f | -12.1881 | -46.7402 | 2024-10-03 00:10:08 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ded08921-f1cd-3f88-8267-d73f95ab2f02 | -12.1904 | -46.751801 | 2024-10-03 00:10:08 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b28b7de-c18d-3f40-8dd2-9f2cfb975d08 | -13.0354 | -51.1147 | 2024-10-03 00:10:08 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a728b74e-62d4-3cfa-a542-d400d2cd8572 | -11.2707 | -43.383598 | 2024-10-03 00:10:12 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbed2f92-1e69-39a0-994a-f57ed04a5de8 | -11.2723 | -43.391201 | 2024-10-03 00:10:12 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
