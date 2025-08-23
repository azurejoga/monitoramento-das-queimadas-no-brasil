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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49561d02-b742-3588-8cad-f80d6b2faae7 | -14.9683 | -48.67049 | 2025-08-23 12:36:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca215d16-6051-33bc-b084-680b4f8a7d9e | -15.22207 | -53.85777 | 2025-08-23 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b3c4cfac-eafb-3519-8024-a3fd07280371 | -16.49591 | -47.60331 | 2025-08-23 12:36:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8ee72bd4-790c-3c7c-93f8-a91de11f6ea8 | -13.86888 | -47.38059 | 2025-08-23 12:36:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 50c1393b-115b-3410-aefb-ad96adc5e7c8 | -15.0707 | -48.50396 | 2025-08-23 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 281cfcc7-f24a-38d5-a742-4e58427944ce | -14.30232 | -58.5159 | 2025-08-23 12:36:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 3849c567-6517-326d-9929-2e1a17eaf20b | -15.01549 | -54.89735 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4ca0c7ca-ad8a-360d-b924-69c37ce0a24c | -21.53339 | -48.78075 | 2025-08-23 12:36:00 | TERRA_M-T | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ddd1a0f4-50a9-3b52-b41a-91ff17ade88b | -15.87687 | -52.22835 | 2025-08-23 12:36:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3285032b-4c15-3f4d-bfa5-945bfc51e260 | -14.02682 | -54.06214 | 2025-08-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 253581d5-baee-384a-904e-1721d8d96ec7 | -20.16487 | -47.85022 | 2025-08-23 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 4d65512f-6a2c-3a78-91fe-d3aec46b1972 | -21.64643 | -45.69741 | 2025-08-23 12:36:00 | TERRA_M-T | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 50b7adb8-4ef3-3cdc-8c1c-e26cd39044cd | -15.54756 | -51.69652 | 2025-08-23 12:36:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ae1d7dbf-f1cf-3edd-8889-6d90215b8d03 | -21.6511 | -45.70447 | 2025-08-23 12:36:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 5433e41d-17ff-33b7-a3cf-0fc8c07b36c4 | -13.87071 | -47.36598 | 2025-08-23 12:36:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0b6b5765-7d57-3a4b-bc00-f98ab3197dcd | -13.84328 | -55.95267 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ce3cc68b-6187-3be6-a1d6-44428c6e40d0 | -14.30243 | -58.5219 | 2025-08-23 12:36:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 178c212d-ce83-396d-aa48-21d62a126c72 | -14.46975 | -55.94255 | 2025-08-23 12:36:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 8eeb6e51-2818-3674-a5c4-34fe29fdcfb6 | -15.05361 | -56.39626 | 2025-08-23 12:36:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4fdd55a6-2d67-364d-b332-cdee38486f51 | -18.86299 | -49.46365 | 2025-08-23 12:36:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| e50728ce-0fbe-32d4-b05c-67f5e25049bf | -14.67256 | -54.91821 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 21f16b49-ff05-35de-ad02-7c7aaf324f65 | -14.81883 | -45.44465 | 2025-08-23 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 5a80ea0e-fc46-349f-bb7b-4363512ae052 | -14.03613 | -54.06363 | 2025-08-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 69c5879d-6d00-3978-acbd-b97c7b730e19 | -21.65346 | -45.67862 | 2025-08-23 12:36:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 8f248f43-99fb-36a6-bf90-ad92d5c1e95a | -20.15506 | -47.8318 | 2025-08-23 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 27b92211-a288-3ea3-bb9e-0c73e728b61a | -13.88165 | -47.36755 | 2025-08-23 12:36:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a748e237-2f87-3b8a-838b-a284ef3c4f45 | -20.38904 | -45.58305 | 2025-08-23 12:36:00 | TERRA_M-T | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4c26a48f-93ba-317c-be1e-1584ae91b264 | -20.15324 | -47.84873 | 2025-08-23 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 453633f9-86db-3267-8698-4d045ecbf6b0 | -19.8387 | -47.82109 | 2025-08-23 12:36:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9ba8cf0b-9cbe-3cc8-a82e-b611c2de6bf6 | -14.76153 | -55.98446 | 2025-08-23 12:36:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9bddb820-eadf-32ee-85d5-477c5765dd90 | -14.46146 | -55.92796 | 2025-08-23 12:36:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 28a220cd-1f38-31da-81f9-5f4e7b1fccf6 | -15.54627 | -51.70569 | 2025-08-23 12:36:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f67f37ce-25f8-39df-ae41-e4828fa25944 | -15.02518 | -54.89842 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| aba7266f-28e1-3e87-bb17-4f5bcb49b64b | -16.42458 | -53.15205 | 2025-08-23 12:36:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3b910c5-717a-3a5a-94ff-cbb1e8a41386 | -16.42322 | -53.16131 | 2025-08-23 12:36:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 37a7b535-b62a-30e2-9af6-cd347a6d2e9b | -14.34301 | -58.59049 | 2025-08-23 12:36:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a6d13af3-db68-3f9e-93e7-600a036f2724 | -14.61352 | -54.85235 | 2025-08-23 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 79dbc198-1d57-3cb0-972d-480e490b53c6 | -15.07229 | -48.49124 | 2025-08-23 12:36:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dda74fbc-db04-35ea-8c44-09f81fb62811 | -14.36275 | -52.04606 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c30ad638-f5db-3838-bed4-d2f58acf9e26 | -20.39433 | -45.59049 | 2025-08-23 12:36:00 | TERRA_M-T | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 2e4f5985-bf0d-359b-ba66-b860f3a637de | -14.4594 | -55.94066 | 2025-08-23 12:36:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f073633-5e52-3f05-921c-a48e3fb01ce0 | -14.47178 | -55.93003 | 2025-08-23 12:36:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 04f13a9c-d14b-3f6d-a180-5bd80788d00b | -17.1626 | -47.57225 | 2025-08-23 12:36:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| be8549a4-a5c5-30c1-a604-981a0c9ef04c | -13.53967 | -51.74845 | 2025-08-23 12:36:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fe7496cf-598b-314b-abcc-eeb2c66cf7d2 | -20.15531 | -47.85946 | 2025-08-23 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c7604d0b-d755-320c-8238-3f5799b7d579 | -14.78595 | -45.50381 | 2025-08-23 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 71b511d5-b72a-38bb-a4d5-fd136c0f6dc8 | -14.68563 | -54.89775 | 2025-08-23 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| a395f641-6373-3cf3-ae68-e355392077f0 | -14.03458 | -54.0738 | 2025-08-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ddf07844-9153-32ef-9da4-cfddee61693d | -13.42211 | -51.79897 | 2025-08-23 12:36:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5432fe8e-44dc-37d9-88b8-ababffc663b0 | -14.61179 | -54.8633 | 2025-08-23 12:36:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 80c4e7c9-8c26-36c6-b560-ec95ce53f7d4 | -14.02838 | -54.05199 | 2025-08-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 117666fb-9c83-372b-bf0c-80e40eb0ca4c | -15.01718 | -54.88647 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 76c628ac-10dd-3188-bf6e-0ea1f19d98c9 | -14.7871 | -45.4974 | 2025-08-23 12:36:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 66fd19a0-42d4-359d-9834-032ae1fb70b9 | -15.01377 | -54.90835 | 2025-08-23 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c8193e4d-5109-32e0-87e7-6883fa63e53c | -15.23074 | -53.85523 | 2025-08-23 12:36:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cd50c346-d57f-3ddb-894c-890374cd7cbc | -14.66436 | -56.58645 | 2025-08-23 12:36:00 | TERRA_M-T | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 30a46a6a-3395-31f2-a8dd-e3b449bb430f | -20.88182 | -55.0028 | 2025-08-23 12:38:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b1707400-5a27-3313-b402-3da6d969584d | -24.67638 | -49.44166 | 2025-08-23 12:38:00 | TERRA_M-T | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9135b3be-9b15-3a3f-9e7c-cbc5955c2e2d | -24.69344 | -49.71355 | 2025-08-23 12:38:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 6d0f706c-dbc0-3674-8c6c-849a1d5d3ae5 | -23.91456 | -47.53009 | 2025-08-23 12:38:00 | TERRA_M-T | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 6e56796a-4085-377d-9532-46bedf5e994d | -21.40709 | -50.45296 | 2025-08-23 12:38:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| 8926bc7e-9066-3216-8baf-a07d0a8532a8 | -24.69098 | -49.70687 | 2025-08-23 12:38:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| a81c2713-0a26-363b-a2f6-b7d7cb361bdb | -24.6653 | -49.4405 | 2025-08-23 12:38:00 | TERRA_M-T | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0eac227e-d8f4-3e8d-9b7e-27deee5493db | -22.53896 | -43.70872 | 2025-08-23 12:38:00 | TERRA_M-T | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| daac7e8a-3650-3a75-b334-a6a09d0d8ac6 | -23.11433 | -52.07717 | 2025-08-23 12:38:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9598c93f-f253-35c4-a502-b5bcb74444c8 | -24.75801 | -50.15147 | 2025-08-23 12:38:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f94682c7-e482-3a80-962d-e7ca72d0e95d | -25.17373 | -50.08622 | 2025-08-23 12:38:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| f650d53d-2f9c-3d17-8c91-29989193dbb6 | -25.16469 | -50.0708 | 2025-08-23 12:38:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| a42df586-3396-3fd6-a865-c481a3dd002c | -23.51335 | -47.6353 | 2025-08-23 12:38:00 | TERRA_M-T | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 44734ac5-12fd-3bbb-93c3-704761e98343 | -25.17536 | -50.07199 | 2025-08-23 12:38:00 | TERRA_M-T | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 9e89d69c-ddb7-38df-8279-161aef4708ef | -25.16006 | -50.54051 | 2025-08-23 12:38:00 | TERRA_M-T | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f237f944-79ae-399e-a251-004edf9935e4 | -21.4086 | -50.4411 | 2025-08-23 12:38:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.5 |
| 41b13ed2-392b-3c5c-83c5-ce7ac3810032 | -23.51536 | -47.61557 | 2025-08-23 12:38:00 | TERRA_M-T | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| d00b3400-5b2f-37bc-b0be-c41c850cc837 | -23.91359 | -47.52416 | 2025-08-23 12:38:00 | TERRA_M-T | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9245fb2d-7b1b-3f8b-a9fb-f17d50fa8bff | -22.66476 | -46.91187 | 2025-08-23 12:38:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 4055356a-cb89-3324-9fc9-74442c310014 | -25.13357 | -52.42824 | 2025-08-23 12:38:00 | TERRA_M-T | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| a02d5b4f-c622-32e2-b164-86d1765e73f6 | -21.40788 | -50.45899 | 2025-08-23 12:38:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 997e089b-a8b8-3dbe-97f7-4309d3fde68e | -21.92638 | -48.93107 | 2025-08-23 12:38:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 1f7a0479-0880-3a6b-81a6-402ea2e4328d | -25.15854 | -50.55384 | 2025-08-23 12:38:00 | TERRA_M-T | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| a4567875-ffa9-3c3a-95b2-5c895f01e548 | -25.73742 | -50.13914 | 2025-08-23 12:38:00 | TERRA_M-T | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1eeb2423-af99-368d-99be-e91c003c0683 | -24.14117 | -51.72732 | 2025-08-23 12:38:00 | TERRA_M-T | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c9bc678f-3009-3a76-b090-a7afd02b405b | -21.40932 | -50.44716 | 2025-08-23 12:38:00 | TERRA_M-T | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 4d65239c-0173-3dfb-88bd-b4b70243152f | -5.7615 | -57.5807 | 2025-08-23 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 698c2982-f991-3d99-a47b-b3e487d7a212 | -5.7429 | -57.6009 | 2025-08-23 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 30509e92-d368-35b7-a868-22108e714bda | -6.6044 | -44.5624 | 2025-08-23 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 790c6e68-d71c-3499-9867-0d655bb252d2 | -6.1229 | -43.9578 | 2025-08-23 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ebf1cb7f-0f7e-3c31-8363-38763b9e1e57 | -7.0164 | -44.6413 | 2025-08-23 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6a3771f0-b7ba-361c-adfc-14e33d7ca013 | -12.9921 | -45.2252 | 2025-08-23 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fb085511-b7c7-36f3-bad6-0e94dbc0a2ed | -5.7431 | -57.5814 | 2025-08-23 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 7dba6108-4be0-3a62-ae1b-b0c4cfad36be | -9.1533 | -59.5027 | 2025-08-23 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f058876b-de0a-335d-becf-df7e6f35ba85 | -6.1416 | -43.9563 | 2025-08-23 12:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0d23ada9-4da6-357e-a8b9-989f93ce5f3a | -14.6706 | -54.9142 | 2025-08-23 12:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f5c44f9f-28bf-3da5-95a2-ab15c0502cfc | -5.7614 | -57.6002 | 2025-08-23 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2a3bd416-06f3-39ae-b927-3a8e4e3d8d0f | -6.37 | -45.5356 | 2025-08-23 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 74b9ebdd-0bd6-35ab-9f36-25cd16a995d6 | -7.6296 | -45.2464 | 2025-08-23 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4734e1ad-db59-3aea-b9a1-ec67894b29af | -6.5856 | -44.564 | 2025-08-23 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| de7759f6-e05c-3d29-a366-9d0f66b2472a | -10.6201 | -50.1609 | 2025-08-23 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2989b8d2-b6b3-3ea5-8efe-392c27f33fe3 | -7.0352 | -44.6396 | 2025-08-23 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 382fbe81-e379-3928-afe1-318df8220507 | -6.1416 | -43.9563 | 2025-08-23 12:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 7f65f3c1-8e34-39af-b7e3-e42757d3ab2b | -14.6706 | -54.9142 | 2025-08-23 12:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 140.5 |


[Clique aqui para ver as próximas entradas](README88.md)
