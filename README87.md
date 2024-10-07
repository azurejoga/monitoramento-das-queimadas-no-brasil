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
| dff0f1f3-fb45-3d4d-999c-0f786e343f8c | -19.8933 | -42.64408 | 2024-10-07 04:55:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7151b577-369b-35c9-a026-e5eb54875a62 | -19.89281 | -42.65009 | 2024-10-07 04:55:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| eadefec0-094a-398e-901f-25fb8451b3ab | -19.8923 | -42.65625 | 2024-10-07 04:55:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9dbc178a-df48-32db-b918-8d4a196bad25 | -19.84423 | -42.37711 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 38d1edb7-9b8d-35c8-8d72-1ec733a39781 | -19.84385 | -42.38171 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 5540b363-c9b9-3515-9731-79d40b6ec896 | -19.84348 | -42.38618 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 5becb973-0c80-3b9a-87aa-cf8149187ca9 | -19.83717 | -42.38049 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c34913db-7471-39c2-8173-fba8ab4ef5c1 | -19.83116 | -42.37121 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 636412e3-fa78-30d7-923f-6829839b332f | -19.83075 | -42.37614 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3dee4ce8-6f25-33f2-bb2e-012f24f2e364 | -19.83037 | -42.38071 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c85b8595-6de0-3fdc-9c5e-67445d2010ad | -19.82495 | -42.36417 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 829310f6-b824-3c5f-9a15-e615e2e23b66 | -19.82454 | -42.36911 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| eb1863f4-c032-3bd1-9368-11caf7b64c9e | -19.82412 | -42.37428 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 105bf284-6811-32ec-9f56-996dc03b0533 | -19.82368 | -42.37958 | 2024-10-07 04:55:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cb20e56e-4563-3fb0-8a18-a9c010a316a7 | -19.77597 | -42.65633 | 2024-10-07 04:55:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 27c20ff4-e284-3fe8-915c-3c5f9033bfd8 | -19.77443 | -42.65409 | 2024-10-07 04:55:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 57531bbd-48a5-37d0-a2f5-893472569992 | -19.76938 | -42.65538 | 2024-10-07 04:55:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0811974-9555-3800-b01f-171fc4b087bd | -19.56415 | -42.74012 | 2024-10-07 04:55:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 50ddf0ab-62d1-30ca-b526-20550336ebda | -19.56359 | -42.74692 | 2024-10-07 04:55:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f7973a60-801d-334f-8b30-6344da33e5ef | -17.5756 | -43.70888 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0b709fa-f6a4-3b66-8f00-0f285908fa5e | -17.54846 | -43.73632 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27d5cf5e-c7d5-38ad-a1bc-24c073a9e3d3 | -17.54803 | -43.7409 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bce7cd1-5026-333e-a577-70b9c2db6873 | -17.54666 | -43.75521 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd1278a0-ad87-3e7f-86c3-9dce5a387134 | -17.54654 | -43.73849 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 951a3a1d-f7bf-33be-a0aa-d79b29f27df1 | -17.5446 | -43.7575 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a92c674-4b36-376a-ae95-9e0b0df2c95c | -17.54063 | -43.75431 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0736f489-a0d3-3e66-b634-a53e0fd6e27c | -17.54016 | -43.75925 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d267814d-80c7-3d7e-923b-84c76c87a3c3 | -17.53908 | -43.75166 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3232a9ad-c3eb-3c26-91bc-4f6524ea40b7 | -17.53858 | -43.75658 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba9baa80-a4ec-3ed5-a376-c3e63ec0c533 | -17.53807 | -43.76153 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb736d5-51c6-34f1-925e-c380ee5e63da | -17.53459 | -43.75352 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5ee5f2a-65f3-37c2-bfab-506c24915900 | -17.53412 | -43.75848 | 2024-10-07 04:55:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72d7d7ce-bb14-3315-90b8-bf2fa93d0a3d | -20.3429 | -44.68459 | 2024-10-07 04:55:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b71679c1-22d6-3b47-a869-4b3a45e8dd25 | -20.34249 | -44.68903 | 2024-10-07 04:55:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f60b4f2c-0063-30ad-8eb3-8ea5a565034d | -19.90113 | -44.95145 | 2024-10-07 04:55:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e52099-0c9f-31df-b133-61317f976a6a | -19.82702 | -43.79206 | 2024-10-07 04:55:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f35c7db0-67d7-340f-a28b-49fce4563a50 | -19.82088 | -43.79083 | 2024-10-07 04:55:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d19547f9-d6d0-34e3-a608-423aac860164 | -19.82051 | -43.79495 | 2024-10-07 04:55:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ec465f-74a1-3df7-9dde-bb0913d600fa | -19.94343 | -44.08851 | 2024-10-07 04:55:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 53ec4dfc-3536-307c-97ab-782b7719c194 | -20.41873 | -43.74984 | 2024-10-07 04:55:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 718fb0c0-2ef1-3f3b-8350-b38fcfb94811 | -20.13703 | -43.86293 | 2024-10-07 04:55:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e58b5fd9-9c39-3498-93e8-14cc8b95380d | -20.1366 | -43.86772 | 2024-10-07 04:55:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7b0d02ec-7d09-3251-8270-a84437d87ae1 | -21.95068 | -45.35677 | 2024-10-07 04:55:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b3f808e-bfbf-382d-9154-8dfa0eed5523 | -21.67292 | -44.00439 | 2024-10-07 04:55:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 53ad2a82-09b7-3c0c-aeb5-8019e5d40d7c | -21.6667 | -44.00366 | 2024-10-07 04:55:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| fedc08ad-ef8f-3458-af5c-640883845ceb | -21.66629 | -44.00871 | 2024-10-07 04:55:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| dbb731ef-5d19-308c-84ba-48da92d8c6b0 | -21.66587 | -44.01383 | 2024-10-07 04:55:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| db94b142-ec9e-3ce9-b376-49c6c811cb34 | -21.40395 | -45.34584 | 2024-10-07 04:55:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a38aff6-9cd8-3958-ae7f-378162f8802b | -21.4 | -45.3457 | 2024-10-07 04:55:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c11e0778-5002-3aee-b17d-30a4d53834c4 | -21.19515 | -44.93726 | 2024-10-07 04:55:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9721ec58-2e1b-308d-9a39-024bf59e3870 | -17.31374 | -44.92841 | 2024-10-07 04:55:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53cf6635-6005-3c4d-b62b-059bdaa07c33 | -18.09805 | -45.6265 | 2024-10-07 04:55:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52c01167-aa78-38d7-b465-1db7c1aaf349 | -19.01884 | -45.52917 | 2024-10-07 04:55:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d5189c9-67c6-3c56-b9ce-4010d29dbf4e | -20.6027 | -46.00459 | 2024-10-07 04:55:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e00b5fb-8cde-305b-8f96-022fec3f1bb6 | -20.59886 | -46.0024 | 2024-10-07 04:55:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80ba2919-5fab-3191-b79f-b8d115d7712e | -20.59851 | -46.00607 | 2024-10-07 04:55:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec6a1fec-cf24-37d7-9ce6-ef549f0f4d27 | -20.59725 | -46.00404 | 2024-10-07 04:55:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b54721a-d6b7-3800-be7d-9ee04be6645c | -19.75484 | -45.31568 | 2024-10-07 04:55:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 125809c7-92ff-3556-8f71-40615014563e | -21.84265 | -46.93537 | 2024-10-07 04:55:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b58c1952-8f90-3514-bf15-a30ba1cf6e05 | -21.84232 | -46.93869 | 2024-10-07 04:55:00 | NOAA-21 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43e15925-590d-3d54-9e8c-1c0119e598f8 | -22.22355 | -46.57741 | 2024-10-07 04:55:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 549cbf2b-2c5e-30da-8b8d-3d18bf9e9ddd | -21.79231 | -46.42046 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 61dd8f2d-3cad-3c5b-8970-e9a6789c0407 | -21.78697 | -46.41952 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2c849454-0aff-3f75-9715-53a0ba8af22b | -21.40357 | -45.3499 | 2024-10-07 04:55:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d93f1969-f2c1-329d-b36f-b36cbf2b0580 | -21.39964 | -45.34986 | 2024-10-07 04:55:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3d479158-469b-37d1-822d-77a9a7bc22d7 | -21.14565 | -45.82717 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c4e6890a-220c-37e6-a9ce-328a6e027edc | -21.14541 | -45.82636 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 278b585f-2940-3754-85c6-f2906497ee92 | -21.14527 | -45.83105 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2347c975-20f5-3e45-b5b9-52e5381c1c16 | -21.14506 | -45.83024 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 90e89af5-6fae-3c49-be4d-a7bbf9772a82 | -21.1293 | -46.62386 | 2024-10-07 04:55:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfef803d-0309-3444-ba0e-1051686bf9d1 | -21.12439 | -46.61969 | 2024-10-07 04:55:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6d0a43a9-1a8e-3bd2-8215-81f26287f2e6 | -20.99662 | -46.09404 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d0465f47-1f94-3174-855f-a2917c0afdb4 | -20.99622 | -46.09811 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d3cb1630-93d5-3e89-a75c-a17055941fbe | -20.99158 | -46.08945 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6ff2b76-398b-3dd7-bae2-7e9d98ee2e74 | -20.99082 | -46.09706 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 45be40b4-ce9a-32ea-8991-99559c6e922f | -20.98619 | -46.08832 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 95e186cb-fc81-3573-8d53-0e518fe0957d | -20.98583 | -46.09187 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cf1078d6-14ef-35f1-9cc7-95d144ce0d29 | -20.98549 | -46.0954 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be96169b-4426-398d-8633-0c414a7432bd | -20.98511 | -46.09925 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9af051bf-075f-33ac-aec4-456c77773ffd | -20.9813 | -46.08197 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7baf700d-0bd1-364d-81c3-20723471242b | -20.98092 | -46.08594 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5a1e6195-2c31-34ee-ac70-1fa92321640c | -20.98054 | -46.08974 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 39e21776-ddc9-3031-9f4f-102dd4ec49ce | -20.98018 | -46.09341 | 2024-10-07 04:55:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f41478ec-1eb2-3e6f-ba9a-856366bcf66a | -22.73694 | -47.03623 | 2024-10-07 04:55:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6eeed3bc-16c2-381b-a9a5-ba87d7a3a21e | -22.73663 | -47.0396 | 2024-10-07 04:55:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 39829690-0a15-3b52-bd3d-2ed3c1bc5705 | -22.73615 | -47.03771 | 2024-10-07 04:55:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 59e49d54-d845-3c70-926b-18b1a5b26398 | -17.77561 | -53.79305 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9b42850-a335-34c0-948a-2befa95dbe76 | -18.69663 | -57.26129 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cc9d6707-24f9-3e1e-b76c-81cfbac4f4d3 | -18.69389 | -57.25684 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 25f72f10-86f4-38a7-830c-4a079c5311fe | -18.69324 | -57.26067 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc9cf39e-8161-3f74-acb3-03e9df51660b | -18.6905 | -57.25622 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| adcff5f2-0cc0-38e5-a9d3-d4d2dc22f002 | -18.68711 | -57.2556 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e6921f19-4764-3aad-bba2-aa46769c5ca1 | -18.67897 | -57.258 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 156e738d-8507-3406-b260-19cbbf92c30e | -18.67622 | -57.25355 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4b44bc4d-32fa-31ca-bef3-7fab523de212 | -18.67558 | -57.25739 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b8aec7fb-4489-39bc-babb-56326f0febc6 | -18.67283 | -57.25293 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 58034fdd-f456-364c-ab27-b35593278a66 | -18.66944 | -57.25231 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 98f11173-519d-366f-bd70-355dfad7a897 | -18.66605 | -57.25169 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| efdc7754-d97f-3ba5-8981-ad0ec8978ba7 | -18.66266 | -57.25107 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3be64b49-12c7-3df1-8efe-e63ff05b05e8 | -18.6599 | -57.24662 | 2024-10-07 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |


[Clique aqui para ver as próximas entradas](README88.md)
