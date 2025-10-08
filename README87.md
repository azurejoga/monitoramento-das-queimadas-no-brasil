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
| 601055b2-158b-330e-b681-693ee2e4f116 | -17.82776 | -57.62314 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 229c81f8-9d4a-3397-a2d5-528eba50655d | -20.63211 | -54.74883 | 2025-10-08 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5feda87b-2b56-3e5f-b17b-64eaaf2f9d42 | -22.38135 | -49.97639 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7e86600-0d5b-382c-83bf-e2b63635ffd9 | -17.83011 | -57.64517 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a40888da-c2c4-3665-81e5-26e1e9a89aaa | -22.38792 | -49.98165 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b9ce15b-f9ed-3098-bd57-6e010ccd2f9c | -21.52908 | -45.43336 | 2025-10-08 04:42:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a1980a7-e562-35c7-8eea-dbf7940d29cf | -22.18456 | -45.91671 | 2025-10-08 04:42:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a01f028-75cc-3e99-b084-ee47d2abf358 | -18.05214 | -57.541 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 64b1b162-df4a-307f-8151-5a54c645be98 | -21.2554 | -48.8065 | 2025-10-08 04:42:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 57770643-bda7-3b48-b099-d344bd3bbe65 | -17.86413 | -57.64626 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 91df9816-ac85-3de0-beee-a1bc3adf030c | -17.97974 | -57.49822 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 764ad8b2-2123-3bb4-898c-cf190890454e | -17.86748 | -57.65121 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 562276fb-5dda-30ec-93c6-1f476aa751b1 | -17.9623 | -57.50685 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7cf4307e-ad8f-3408-910f-bb91d9e6988a | -18.04493 | -57.55725 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| eab88673-dbdf-3a4d-aad2-0944a665850f | -17.98866 | -57.4958 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3b4a9eab-df6d-3dce-b357-fabb0f245b6b | -22.36354 | -50.0265 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31f228b8-8f15-346a-b9e1-c173ae296476 | -17.92642 | -57.51773 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 82804bb7-383b-3e9d-b81b-9d5836e74371 | -17.85462 | -57.58358 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a3ab0b42-04cf-3bfd-95ba-ac6fc0755bac | -20.09096 | -44.20643 | 2025-10-08 04:42:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8400ec84-2fc0-3b56-bc5b-3dfa5bf9c7c1 | -22.31413 | -49.9179 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5ea17d7-1e14-3a16-9249-8fc167fb026b | -17.97021 | -57.5039 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8c49f860-bdac-390c-a195-712ad96afa95 | -20.30057 | -48.51514 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7793a0c9-49d0-3a92-b7e3-38412cceca5d | -17.86901 | -57.64305 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 573aefb9-7c48-3357-9afa-44e7eb94f178 | -20.19469 | -43.95047 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02473777-7681-332c-9ee6-b9b09e587f6f | -18.05746 | -57.53511 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 40a48bdd-caeb-3495-a335-ed754f6b1dbf | -18.0515 | -57.54448 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 848910da-170e-3906-86eb-cb4d2e964821 | -18.01405 | -57.56375 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 50292daf-daa6-3d36-991d-9167b5d8d598 | -17.93717 | -57.52839 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ab451a6b-fe01-37df-91b9-ac311e771337 | -17.8553 | -57.57998 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 92709363-3c95-3b8f-9a58-187c4a599bb2 | -17.826 | -57.64425 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 5e64176d-60e2-34c3-8fd0-7d5b44766d1f | -22.2986 | -49.92449 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 600fbc90-1c04-3e75-9940-7dc488279029 | -20.29682 | -48.51456 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02e6bfc5-4d17-337d-a5e2-a2c5800d3c15 | -17.93237 | -57.50854 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 25b0282e-827e-328d-97e0-bb4063ae353f | -17.8266 | -57.61869 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1e30e3c6-f613-3942-a1c8-39ef1d0087a9 | -22.96162 | -48.35366 | 2025-10-08 04:42:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f38b8e3-32ce-3d23-86bd-d40d5f79f1cc | -20.20158 | -48.70503 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f10b473-5fb3-3053-800e-ea0c8fe69f06 | -19.42747 | -49.5836 | 2025-10-08 04:42:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aac96df4-7b87-3b60-950a-4df5ca743dfe | -19.83048 | -46.167 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d92df2f-0392-320a-b1bb-d4999469dcff | -17.83149 | -57.63793 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 2f03ee54-ab43-36ae-843e-2cd25ad4be62 | -17.95411 | -57.50537 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9e63b826-2800-3d5f-b7e4-950eae11a31b | -17.9405 | -57.53333 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad534ab7-a39b-3a44-8b36-2f5722768109 | -17.86493 | -57.64199 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a3866b0-5bd5-3cd1-8a1a-593a1ee9fe1a | -19.85243 | -46.16612 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9051c45e-04b9-39a7-a8bc-ebe9e6f8b63e | -22.30218 | -49.92507 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8ea9eb92-007e-3bad-bcbf-1aba8803cae2 | -17.98455 | -57.49518 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 502826c6-c9d6-3061-b03d-3f2cf354e735 | -19.82834 | -46.16356 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c93c4a11-b517-370a-be46-c7d76cf4387b | -22.18334 | -51.36949 | 2025-10-08 04:42:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11dff0f8-4a4c-336a-9e52-5efd0496ca40 | -17.92766 | -57.51112 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 38bc6cb7-2164-31a9-948a-8ee89d58205a | -20.97625 | -48.99886 | 2025-10-08 04:42:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b16791b2-3751-30d2-9528-5d01a87e8052 | -19.83526 | -46.16358 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4dffc047-2546-361e-9db2-847b84ab8848 | -20.85098 | -49.48072 | 2025-10-08 04:42:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b11f0b69-70a2-3dba-bda7-80d83b01ed60 | -22.39084 | -50.01331 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8fc65ca2-ac4a-30e2-9661-20e4e7841a84 | -20.39124 | -43.06959 | 2025-10-08 04:42:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c3f659fa-513b-32a5-b1da-baf632ba4385 | -19.83261 | -46.16432 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 68cf4eb9-189f-36da-977f-6a449215ee8d | -18.02189 | -57.52165 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 48a85a29-3f13-34a4-a79d-2ffeaab0bc52 | -20.20454 | -43.95218 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| df885cf6-a3d4-331a-b07b-4f245ba8d75b | -17.90042 | -57.65802 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 22425724-59d1-338a-8fef-2796c9514144 | -17.82387 | -57.64415 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8275bf60-ed23-317a-94da-1e16d6b0d3e1 | -20.16843 | -42.20851 | 2025-10-08 04:42:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 22afe0a1-e238-3af1-a266-473054a34592 | -17.82932 | -57.62684 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0279d0e4-04ad-3afd-ba67-f32150f7d0a3 | -22.38728 | -50.01271 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f431b0a3-e586-3666-bdee-9151b0f6a244 | -22.39207 | -49.97802 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bf633ddc-5967-3359-856f-a2cb999c077b | -17.87571 | -57.65294 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e8e612e7-3aec-3814-b8ad-744ef2548b8a | -20.12493 | -44.42038 | 2025-10-08 04:42:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d0b95538-8151-333a-9c2b-999201e139e6 | -17.85111 | -57.64725 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f9e33552-8b5e-3a12-b1ba-df2498eae32f | -17.82451 | -57.6407 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 17140e8d-39fc-3afe-a537-7794fef9649a | -18.24248 | -55.38443 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9590f1f0-ccd0-3e51-89e8-feb1b826033f | -20.186 | -43.93683 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d0ffa21f-e9a9-31b0-8e32-8d8a404da6e1 | -18.03634 | -57.53492 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 94b2f223-18e1-30d0-b965-42cb8a3e26d6 | -17.89292 | -57.6524 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f7f555b1-cb99-32e4-8387-054fba70fd5b | -22.30575 | -49.92563 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e296103-18ff-316b-a125-f409ab46e0fe | -17.83215 | -57.63446 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 67fe75a3-5ec4-3323-b619-4d33e4f9326c | -17.96543 | -57.50675 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e0f7c37-f567-3283-b7d1-6d4f6f26748c | -17.84902 | -57.59064 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 72437efb-e4d1-329a-b99a-dd8e1ac7bd6a | -21.90178 | -44.89349 | 2025-10-08 04:42:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb175664-8129-3e55-8900-b78657fdca60 | -17.94056 | -57.51004 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ca44218a-57b0-3614-aa32-e1180e27b8c7 | -17.89218 | -57.65634 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 39a9b851-0b34-3225-830c-876f993b233a | -17.92983 | -57.52219 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a813caf1-784a-3685-8308-0ae5894adbb6 | -20.12627 | -44.42104 | 2025-10-08 04:42:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 302ea4f3-422a-3c1d-a2e7-f7049c67e222 | -20.50374 | -45.94461 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe10711-c476-38d0-8fde-c361cde977c3 | -17.8716 | -57.65206 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0dd1bd88-6f91-3527-aaf6-18e2469d5ef3 | -17.85393 | -57.58722 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1141826b-5ea3-38c5-8774-12d2384d7b6b | -17.85518 | -57.64836 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4579857f-96c2-37ca-9f83-9ea0d28b77f7 | -17.85176 | -57.59868 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 484b5c83-fba6-33b0-816d-1bd4bc22b47b | -20.09583 | -44.20733 | 2025-10-08 04:42:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e0b8378c-401e-3634-9f6b-0a954d3238a3 | -21.90943 | -45.00175 | 2025-10-08 04:42:00 | NOAA-20 | CAXAMBU | MINAS GERAIS | Brasil | 3115508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 174bca86-b229-354c-958e-00a5c14d0d69 | -19.12194 | -43.51897 | 2025-10-08 04:55:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0f729341-a0ef-34ed-aa0f-d93ac402f5c1 | -19.12144 | -43.51211 | 2025-10-08 04:55:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 4e7a081f-daec-3af5-a961-140a1b633c74 | 2.13524 | -50.87043 | 2025-10-08 05:25:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9314b27-c455-3fd6-812a-c64964b4d0e1 | -3.09644 | -50.57558 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ec99034-e7bf-347c-8efd-1f587282d639 | -3.38389 | -50.14369 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 616d5469-b875-328a-bebb-2a1fbdc1404b | -3.19968 | -51.01508 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33fb4db1-3057-3816-84b0-7b09aefbbceb | -3.5825 | -49.43869 | 2025-10-08 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8d26ed-6124-3197-a064-ab7f8309a323 | -0.90109 | -47.54724 | 2025-10-08 05:27:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a718b9e-5507-37bc-a0b8-24bef0debdcc | -3.39018 | -50.1427 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c292f6b9-93cb-3b50-93ed-e82dbdee2998 | -3.38335 | -50.14653 | 2025-10-08 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de08335e-823b-3f2c-af99-4f7a9f9eb06b | -3.0933 | -50.57455 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aef23e4-d5b6-30c4-9c4d-2cd777cbbecb | -0.90802 | -47.54854 | 2025-10-08 05:27:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71fbda21-f961-31d6-909c-3c2e1c95277b | -3.79058 | -49.42844 | 2025-10-08 05:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b73ce8e-fdd1-3b5a-a955-afb15b4a4aa9 | -2.88432 | -50.73312 | 2025-10-08 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README88.md)
