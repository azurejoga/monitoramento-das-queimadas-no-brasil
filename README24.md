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
| 7344466f-f430-3213-9ff5-9082ea10b1fb | -19.42119 | -48.06415 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 70692993-fbf4-3297-99f5-e5ec79759b9a | -19.33216 | -43.04339 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a88a5b3b-9b35-3188-8a1a-7ca3732a8ced | -18.20382 | -44.33411 | 2025-10-29 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7646939-c6e4-3679-a87f-5c215df2f6d5 | -18.54908 | -41.57478 | 2025-10-29 03:57:00 | NOAA-21 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fe7aa67f-0a8f-349c-8869-ab5a051ef49c | -19.89665 | -44.62147 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5b3188e2-3bf9-37e6-a3c9-12451d3ebb84 | -19.24119 | -43.99652 | 2025-10-29 03:57:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cab97051-b642-3c64-bd27-d83c764b9551 | -17.40364 | -42.43779 | 2025-10-29 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 978aa112-8c45-3c4f-b19f-bffee304918d | -18.78242 | -44.33757 | 2025-10-29 03:57:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 740b3037-4de5-3028-809d-1a02a09545f3 | -19.69044 | -43.09195 | 2025-10-29 03:57:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 36d3348d-63d4-383c-9d22-e3fe4d93a8a1 | -17.68762 | -43.95298 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48c467b7-4bb7-3aca-9e58-89ae534ac36f | -17.4862 | -44.06833 | 2025-10-29 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 775eab48-5f7f-3c8a-8b3c-a108ab9b567e | -19.46317 | -43.58601 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ee431c5-2fd3-3ee7-ad2a-a14d2d1e8be2 | -19.33427 | -43.0518 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9ec11278-a1f2-3568-a023-0f387f6d24ad | -18.0879 | -44.24554 | 2025-10-29 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 443154ba-372a-3c1e-b46f-93a444893457 | -17.43785 | -44.36734 | 2025-10-29 03:57:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259c4b84-143c-34ff-adf5-e9c4ddce9988 | -19.80036 | -44.50601 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46edcb76-3a04-3f7f-ae2d-b256bf7ecabb | -19.33963 | -43.0405 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fa8ce61-ecf4-3cb6-bdba-87389ed1ca62 | -19.96503 | -47.20878 | 2025-10-29 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7610f64c-fbc6-3725-8609-c8737f07b5a0 | -19.81683 | -44.07417 | 2025-10-29 03:57:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea8a3a9a-ee98-3284-ae63-7f238ee83401 | -17.6269 | -43.99194 | 2025-10-29 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8539f159-c7c5-3015-955a-c774da522ff5 | -17.53703 | -44.61896 | 2025-10-29 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06d7a2b3-1950-3b9a-b80c-c0a53f38ccda | -17.20438 | -44.45366 | 2025-10-29 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 880f6b69-5530-33e1-8f21-687e4a0a76a4 | -17.99944 | -44.40442 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e338591f-e87c-3905-9b3c-51f3bac5464e | -18.29181 | -43.08049 | 2025-10-29 03:57:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d7ac1b2-14d8-3baf-a500-f78d1f29ecf4 | -18.58496 | -44.02562 | 2025-10-29 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aa80e3c-466c-35a4-8d31-02c005c06c20 | -17.69102 | -43.72415 | 2025-10-29 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13b1ed01-e932-3490-806d-f87df7513622 | -19.79373 | -44.52278 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ae5ce64-fc59-35b4-ba40-b88c14fb7fee | -19.79883 | -44.51476 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b08dd9c6-5a12-313a-a788-aedebbe88611 | -19.42558 | -48.06506 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 595489a1-0af8-3aa4-b8e0-4ca369d4df96 | -19.81753 | -44.07005 | 2025-10-29 03:57:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3f4ea981-35f0-36dc-8564-cb644e257c49 | -17.63377 | -42.9759 | 2025-10-29 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72d68f40-f984-31f4-88d7-90ddaacd8d49 | -18.2474 | -44.19006 | 2025-10-29 03:57:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e396d2-abf7-387c-9464-0f1febba4290 | -17.68688 | -43.95721 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 987638b6-ce53-3351-9b2c-4343f74836d7 | -19.8015 | -43.24734 | 2025-10-29 03:57:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23bc31f3-c3d6-337a-9873-31ad703e3bd4 | -19.67634 | -44.19445 | 2025-10-29 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03e173c-d6b4-3380-9f44-eb653d88d6eb | -19.45423 | -43.59694 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 260f76d7-d511-3822-abe3-c9cf9c3f1b10 | -19.6898 | -43.09578 | 2025-10-29 03:57:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9276e035-58fa-3313-9274-8e10e1a44815 | -17.20071 | -44.45292 | 2025-10-29 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd8fdf6a-c140-3248-aac9-627193dc7bf6 | -19.42504 | -48.07048 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6892f7e6-5d41-3c8c-9fcd-820e779d13e6 | -19.33767 | -43.05234 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 6258f426-1363-3996-9a34-0e9e56077038 | -18.89247 | -43.35787 | 2025-10-29 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 29c94db1-4590-36e3-90b6-8808a9217959 | -18.92837 | -45.02661 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bf097ca3-77d4-3124-9300-78c81141535e | -19.45767 | -43.59757 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a4901bd0-1077-359d-bfc8-1e66e4c0564d | -18.78949 | -42.49222 | 2025-10-29 03:57:00 | NOAA-21 | SARDOÁ | MINAS GERAIS | Brasil | 3165503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e71899d-d63f-3952-a302-f66095ae247d | -18.92383 | -45.03056 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4b48d8e1-1a7e-3376-ab41-34b29c1898f7 | -18.56956 | -42.93432 | 2025-10-29 03:57:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c069463a-27a8-3db3-9d82-e213ff5c0155 | -19.80425 | -43.25184 | 2025-10-29 03:57:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e7731cc-25fa-37a7-901b-701ba0a3c8fe | -19.79959 | -44.5104 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b9b2c9d-647e-35a9-a677-5b962c4ad823 | -19.7945 | -44.51841 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b4b27bc-542b-3c0e-8e08-d23b676bea85 | -19.98164 | -41.07415 | 2025-10-29 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 619b4d05-4b4a-31c6-bb10-5fc498de7fc4 | -19.79058 | -43.82872 | 2025-10-29 03:57:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c3c6322-2969-3f55-b50c-90bd44d9a3d9 | -17.90517 | -45.91215 | 2025-10-29 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58e1bb4f-b7d0-39b5-80fc-2cce4e96b921 | -18.50541 | -45.07773 | 2025-10-29 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 292c99d0-0a90-3d83-9d6d-3505c4ee2073 | -18.91931 | -45.03444 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2856e703-b07a-3cbe-af12-b480774171e3 | -18.92501 | -45.0453 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 9781671d-641f-3e28-8ad4-346dfbd09ef4 | -19.42594 | -48.06577 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 72dd52e7-0048-3988-8260-298bbd1be6e8 | -18.12457 | -42.58866 | 2025-10-29 03:57:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39e411b2-bd59-38dc-8cac-b58bc4b66f87 | -17.26335 | -45.28455 | 2025-10-29 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d977befe-42a6-3dc8-902f-f47aa38061b8 | -19.57674 | -43.18229 | 2025-10-29 03:57:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1c41448-f247-35ec-a4fd-19b12977025b | -19.42065 | -48.06953 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5de14ae0-d36a-3a81-acec-ef710fc1211c | -19.41846 | -48.07784 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1639c3d4-83bb-34dd-a286-d9e683af76f5 | -21.00038 | -42.80076 | 2025-10-29 03:57:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1ebaf8e-2690-34e5-b87c-a53094e1d76b | -19.33557 | -43.04394 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d54cbb28-41d3-3c3e-ac6b-3012cea7a672 | -19.7904 | -44.49979 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b44ddbbe-c13f-38c8-938d-f1d7ff26fe55 | -19.72012 | -43.93845 | 2025-10-29 03:57:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 793f0d7a-0dc5-333d-8baf-c82b860868de | -18.66309 | -43.7602 | 2025-10-29 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 153354ff-f9af-3c8e-80ed-68f6b40cfbfc | -17.64417 | -42.89351 | 2025-10-29 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2b6d941-401d-30ea-9fe2-f460e254ac3d | -19.33703 | -43.05621 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| cbcc4f3f-799b-3b27-ae61-703bf236c733 | -19.79749 | -43.83014 | 2025-10-29 03:57:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23156e63-11ba-32c5-a8f1-f2e8edb66527 | -20.99704 | -42.80014 | 2025-10-29 03:57:00 | NOAA-21 | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba7bce6f-1168-3046-bfa0-5c7e4c4df60a | -20.80398 | -42.75278 | 2025-10-29 03:57:00 | NOAA-21 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cbad17c6-195d-3d4e-9275-186818b6813c | -19.7973 | -44.52346 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3eb9cee-a517-3f69-9606-1953f5ae641b | -18.78722 | -43.33482 | 2025-10-29 03:57:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed90ea51-d026-332e-b893-5352c6a4cf85 | -20.10169 | -44.30183 | 2025-10-29 03:57:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa6817e1-0ff3-3efb-87a4-4e262b57eae5 | -19.33362 | -43.05566 | 2025-10-29 03:57:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| da2ef816-cf40-3ade-9d7f-fd1c261c044c | -16.90055 | -42.9207 | 2025-10-29 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f87064a-db32-318f-8e2b-82c0e2aad0c0 | -19.80315 | -44.51111 | 2025-10-29 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9ec9be4-b988-3ce2-9168-c355bb25983a | -18.92786 | -45.05076 | 2025-10-29 03:57:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7136e9da-0462-3a27-8ae3-7b63c8e97000 | -20.09888 | -44.29703 | 2025-10-29 03:57:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8a509a74-bc9b-3a47-b196-17d5c66359c3 | -19.28345 | -43.72937 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b81a5ef9-689a-39f5-82bd-d000539cea79 | -20.52127 | -42.95862 | 2025-10-29 03:57:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9fc3e093-b788-35af-b5f7-9321fb632579 | -17.53334 | -44.61825 | 2025-10-29 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37cd202a-a782-39b9-86c7-950ae1d8af9d | -19.45835 | -43.59354 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11aa98c9-d0af-3090-affb-57dec71aea0f | -18.54529 | -43.93904 | 2025-10-29 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 038f482d-f859-3153-86f6-310b330ea94b | -19.42155 | -48.06485 | 2025-10-29 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a869f5fe-2a58-3cd1-a1b3-019e49f53b30 | -17.56921 | -44.75232 | 2025-10-29 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f2cd64a-5f87-3e61-8939-d77fa020e7c8 | -17.13317 | -45.37814 | 2025-10-29 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 233f2dc0-928b-3dca-af1b-a1458c4d1db0 | -18.14307 | -50.96249 | 2025-10-29 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65d1199d-322d-3e3f-a653-d5e1c127b825 | -19.38453 | -43.63009 | 2025-10-29 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc03ca7d-3a61-385f-8e8d-44aa493a94ea | -19.96577 | -47.20491 | 2025-10-29 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 403bf222-3b46-301e-94ab-de5466987c2c | -17.69609 | -43.96775 | 2025-10-29 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b74769c-64d2-3b2c-881d-c1ad6baa2374 | -6.1249 | -41.8414 | 2025-10-29 04:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| d56f5655-664f-3978-ab4f-c9d1c1acf757 | -4.4804 | -43.447 | 2025-10-29 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 033d7a8c-7ec1-3a2d-9a81-cd58635c16dc | -7.8037 | -46.4458 | 2025-10-29 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 18e7bc84-40c1-331d-9dc9-39f14d0ec120 | -4.1972 | -50.0819 | 2025-10-29 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| d8eb8825-c105-34eb-836c-695c47324a1f | -4.2156 | -50.1022 | 2025-10-29 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 905120f6-c867-33e1-a441-61b5dc0a901c | -4.2157 | -50.0812 | 2025-10-29 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ab4bf2a4-ad7a-36fa-917b-b70c79c566dc | -12.0032 | -46.7892 | 2025-10-29 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| aa956599-3c5b-34b4-9821-0131fe8814d2 | -7.8035 | -46.4681 | 2025-10-29 04:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 65f98a19-6c6a-3af4-bc94-d367e2ebc1ac | -12.7021 | -46.303 | 2025-10-29 04:00:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |


[Clique aqui para ver as próximas entradas](README25.md)
