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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5669733-42b7-3c8f-b59e-1fd545b077cf | -11.573 | -47.62675 | 2025-03-19 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23eb042f-a773-3ac1-a59d-75bc2ecb6de4 | -11.85546 | -37.59719 | 2025-03-19 03:55:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 89f4352e-a019-3497-a349-7074b264a8bf | -9.14595 | -38.36152 | 2025-03-19 03:55:00 | NOAA-21 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d11c04dd-d895-3e9e-b099-4c912af9fccc | -9.2984 | -36.68009 | 2025-03-19 03:55:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d890bff8-9e0e-337e-b963-e1f4d72a7124 | -10.65085 | -44.39709 | 2025-03-19 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4008568-a0ae-3fcc-90ca-6b11fb31a331 | -12.08628 | -45.63134 | 2025-03-19 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9acabc3c-881c-382d-8d6c-4548b093df07 | -15.34292 | -46.95409 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e699690b-5e12-367d-a95e-c01e6a8d148e | -15.42664 | -40.58529 | 2025-03-19 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a36d59f7-926e-3c42-86a6-b79bbd8a6e5b | -15.70617 | -42.3352 | 2025-03-19 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7ebf009-e152-3bf0-a199-e68ffe7f0c4d | -18.11939 | -39.68489 | 2025-03-19 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| caa59cda-be22-3ff5-938b-c284f84580a4 | -17.59525 | -43.19863 | 2025-03-19 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56a8ecc0-9f6c-3620-92e6-2e69d27b27f8 | -16.08511 | -46.62275 | 2025-03-19 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 917c421c-5f90-35e0-a3e1-47fbdeda901e | -15.34126 | -46.96292 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 128fb827-8563-36f4-8fe0-83b364da2888 | -16.08661 | -40.88617 | 2025-03-19 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f531f97d-f20d-3823-9e99-543752c2c190 | -16.2949 | -45.0967 | 2025-03-19 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3f03ad1-6563-39f9-80bf-91d88c508d62 | -15.34998 | -46.96467 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 60bd9648-9adb-335b-b433-7277025eda4c | -15.34477 | -46.96838 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8d4c0bc5-6b3a-367b-9b7a-7854cc0853a1 | -16.0833 | -40.8856 | 2025-03-19 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 399b92b3-d9af-3486-8f2b-b0a54ee275c3 | -15.65514 | -40.66733 | 2025-03-19 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 795cd0b2-c51c-390d-91bb-a6a0edca7288 | -15.34371 | -46.94983 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6d6702a-f0f9-3f5e-9fd1-818c25975c93 | -14.85742 | -45.19518 | 2025-03-19 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a92ed08-01d7-35b8-a490-ad420e191217 | -13.63847 | -48.44835 | 2025-03-19 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f80b9dcd-88cb-3703-8bc1-416311cebade | -20.5642 | -42.12588 | 2025-03-19 03:57:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 841a1bde-a6f0-32de-8630-ffd3d3093caf | -15.42333 | -40.58475 | 2025-03-19 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81712601-c2df-377c-b69f-862f591eaae6 | -15.35242 | -46.95159 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afa5462b-e9d9-324e-bee1-fcfcb81650ad | -16.29873 | -45.09742 | 2025-03-19 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60793d0b-37e8-3968-b868-bfd65ba90e37 | -17.32667 | -39.57871 | 2025-03-19 03:57:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c8ed12cb-0030-3fb9-b3ed-d9d6c3fa3ade | -16.08585 | -46.61872 | 2025-03-19 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e7ff3f8-74e8-3eea-b9df-1bd8ab844e29 | -15.4272 | -40.58174 | 2025-03-19 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53713c55-5bc5-361a-a181-ce672abb9ceb | -15.34728 | -46.95496 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 56590603-c5d6-3738-9937-e7bc8e7b5784 | -15.34563 | -46.96376 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c2de2872-915c-3a85-bc5c-f0d59edbf5d3 | -18.81055 | -41.98474 | 2025-03-19 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c390cf6-bf54-386b-ae16-2508719dac5e | -15.42608 | -40.58886 | 2025-03-19 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db6bb867-f84e-386f-a4b3-6dabaf4fc42e | -15.34807 | -46.9507 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91f75f6a-dfc8-3ce4-bbd6-750b38bb5d67 | -15.25482 | -43.67205 | 2025-03-19 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28f3a47f-ef3a-3a73-90e6-573c87f3b2df | -18.81387 | -41.98532 | 2025-03-19 03:57:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7eced6c6-dd2a-3329-a671-1435e2b498a9 | -15.80125 | -42.03125 | 2025-03-19 03:57:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d843e30b-c995-3537-963c-e0ecdd24ad62 | -15.35517 | -46.96112 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 617089d4-40ba-3ce0-a9c1-0e183d35cfd4 | -16.61511 | -43.33033 | 2025-03-19 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb4b0ea4-25b2-3e36-962f-e0143e2e5336 | -16.07862 | -42.419 | 2025-03-19 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f17f1b03-cad3-3b1e-a881-2d0468d66d61 | -15.34646 | -46.9593 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| aac12f3e-b1dd-3536-9e09-08a69b5b09fd | -16.68042 | -43.88427 | 2025-03-19 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d61104c-b69c-3692-b3cf-787d663f689a | -15.34209 | -46.95848 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c14817d-919e-3968-a94d-8274de04c680 | -16.61443 | -43.33432 | 2025-03-19 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fb31620-f5ba-3fde-9c78-bfb4238e996d | -15.35598 | -46.95676 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0134341e-7108-3dc2-b0a6-ff7b80f84644 | -15.60784 | -39.11798 | 2025-03-19 03:57:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12d8d9de-1ef9-343d-8afd-c68292bdc6a5 | -19.84051 | -40.08207 | 2025-03-19 03:57:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e7db6576-c39a-3430-98d0-e6450db4579d | -15.35163 | -46.95587 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 44ee5711-da61-322b-aba1-1c49421459eb | -14.86017 | -45.19769 | 2025-03-19 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b772b46a-a23d-34f3-b513-d3544e11a3aa | -15.07979 | -48.94558 | 2025-03-19 03:57:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c343139-2075-32c3-8bfc-19d0eaf2a819 | -17.37871 | -42.48481 | 2025-03-19 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 036bce96-4a83-3f8c-94d2-7d70aefed0c2 | -15.35081 | -46.96022 | 2025-03-19 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| c1e6b2eb-67b5-3d87-a94f-df097f6a425f | -16.29678 | -45.09921 | 2025-03-19 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01b8c9c7-dbb9-33f6-8471-82c38453211b | -16.08605 | -40.88974 | 2025-03-19 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| db8af681-0071-3557-8912-87dcc7f5bd87 | -30.35566 | -54.29133 | 2025-03-19 04:02:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 93c4ab87-5a3e-32dd-98d3-44bf71f40315 | -29.36052 | -49.77761 | 2025-03-19 04:02:00 | NOAA-21 | TORRES | RIO GRANDE DO SUL | Brasil | 4321501 | 43 | 33 | nan | nan | nan | Pampa | 8.1 |
| 24ec655a-b600-39b8-aba0-a41e208932a3 | -27.33828 | -50.57833 | 2025-03-19 04:02:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc466d5f-a4f5-3880-83f3-156293ff7010 | -31.26776 | -52.87878 | 2025-03-19 04:02:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 303a88b3-7cfc-3913-8a05-78ee15d40bb5 | -27.33394 | -50.57719 | 2025-03-19 04:02:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8d40201-3bba-3587-9c92-7769b17d938e | -29.87281 | -51.15699 | 2025-03-19 04:02:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| e9cdc332-3d84-3cf1-80a8-11bd1b347aaa | -31.27137 | -52.87728 | 2025-03-19 04:02:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 99cc9f96-389a-3707-9e14-76eebbd1ce12 | -31.27235 | -52.88004 | 2025-03-19 04:02:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| c53c3622-53a5-337c-9627-7b2d1db3a1ea | -30.74437 | -52.66525 | 2025-03-19 04:02:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 49164981-ef1e-39f4-b3e7-ac730165b874 | -7.24587 | -44.77583 | 2025-03-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223f175f-e53e-3d43-b1ce-f79fe5116a75 | -7.24532 | -44.7793 | 2025-03-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb561a11-3224-3514-b597-d51990599dbd | -10.34855 | -38.48024 | 2025-03-19 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1114cd50-6361-354b-bd17-9d1431881bd6 | -7.24973 | -44.77288 | 2025-03-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec34a06f-6a38-3226-9a59-ca3fee9858ab | -6.83295 | -44.32292 | 2025-03-19 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af683c1a-c6ef-38b1-a358-6c5555b90121 | -10.82514 | -37.16684 | 2025-03-19 04:19:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5bd580f6-3366-3e95-8f07-32d1463771c6 | -7.05699 | -44.38288 | 2025-03-19 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 181b52f5-9bdb-3d74-b2e8-0ccd8d12ec0b | -5.7748 | -44.38349 | 2025-03-19 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff497a0b-217e-3f69-9b67-19bde2dfe65e | -6.82963 | -44.32239 | 2025-03-19 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96a70441-e8bc-3eea-98ab-dcb1c336d09a | -10.5031 | -42.42848 | 2025-03-19 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 077660eb-682d-38bc-8639-3134cab5fabe | -7.24919 | -44.77635 | 2025-03-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73e81543-22e1-3c4d-97b9-1d79a3cc39cf | -15.42379 | -40.58482 | 2025-03-19 04:21:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 85935045-5f7e-36d3-8ba6-9f6a23a0add9 | -15.34987 | -46.95883 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f8679662-2e54-34c8-b21c-b62dd4c4ff8d | -14.75739 | -40.31361 | 2025-03-19 04:21:00 | NPP-375D | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c180fd4d-7c8a-378d-92d7-867f6ebe5243 | -15.25265 | -43.66854 | 2025-03-19 04:21:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e66273d-b17d-3156-a263-83e2310d5338 | -12.09064 | -45.63852 | 2025-03-19 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fd6325a-38c4-36fd-be4a-5cadff2a21aa | -12.1472 | -40.29836 | 2025-03-19 04:21:00 | NPP-375D | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37c707a6-8372-30b8-82cb-44aa5a6df086 | -15.35433 | -46.95224 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a692871d-1313-3080-9bc5-8ccc8fb6c780 | -11.57611 | -47.62712 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19334970-b218-34f2-a55f-460d1beb3dc8 | -13.27453 | -54.34526 | 2025-03-19 04:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6d96bc71-defe-3330-a394-ff806e55bfbe | -12.0851 | -45.6304 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3d0eaf2-9468-3702-834c-c78280eb60c8 | -15.34047 | -46.95356 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41a2e9a8-962d-312a-813a-681cf30224c6 | -12.08897 | -45.62741 | 2025-03-19 04:21:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b322ec0-3fb3-3172-8af9-bf85726711a4 | -12.08787 | -45.63446 | 2025-03-19 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c557ba1c-4b4b-337b-887c-428d36362a7b | -15.34712 | -46.95469 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 735e21dd-52ed-3b12-8acf-3be5f9162ebb | -11.85102 | -37.59331 | 2025-03-19 04:21:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b9fc4b83-5c91-3093-a873-4486b8ca2a9d | -15.34598 | -46.96184 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 527d1716-708f-38c8-9d98-2151fba9be1e | -16.67897 | -43.88361 | 2025-03-19 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e033575a-871c-39e3-a8ea-c12e9182f089 | -13.31317 | -50.00937 | 2025-03-19 04:21:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15c6a8c7-ea5a-39a5-b5d3-567094074d8f | -15.34541 | -46.96543 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf5ad955-5aae-3b44-9e79-1fd982ce406c | -11.26296 | -44.49345 | 2025-03-19 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c28ed5de-5870-337e-8f44-3f2c3177e7de | -11.58355 | -47.62455 | 2025-03-19 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff8dbd6f-f93b-33c5-903f-0774b4f39a85 | -15.3399 | -46.95714 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b01db382-ddc8-3de8-b578-57085eb90120 | -14.19344 | -42.79607 | 2025-03-19 04:21:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6cad6ecb-b437-3a37-a736-bf0ea8fbb722 | -15.34104 | -46.94999 | 2025-03-19 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c026200-d286-38c0-8844-f02c65acd67d | -12.86189 | -38.36577 | 2025-03-19 04:21:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e526bc67-a24f-37ba-825f-4abb1f4c0306 | -15.80131 | -42.02924 | 2025-03-19 04:21:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
