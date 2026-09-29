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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded3fbef-d825-3b44-a553-22bc147aef85 | -11.42119 | -43.47447 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 70e30957-3e44-3953-ae50-1e1fb54c3f7e | -11.42433 | -43.45173 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 335f8081-2bdc-3c34-955e-962567b26595 | -15.15172 | -43.61586 | 2026-09-29 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 888fd519-aec1-381f-b673-9b35bfb1c836 | -11.43243 | -43.44342 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4ed63b15-fe14-331f-9a0b-5bb5be990093 | -11.1693 | -44.78889 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52860a07-1660-3c0d-ac62-3e05b5c1d9fd | -15.64882 | -41.35345 | 2026-09-29 03:32:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 194629b0-abe8-349d-866e-54ebbd9a860d | -11.40945 | -43.43656 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a0a5b7e-ec31-3671-8d51-0958b33e68a6 | -11.43349 | -43.47719 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec1d368b-7917-3aad-a595-f52f34a7fd09 | -15.24739 | -43.27422 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 6f0bbca0-2779-3473-8a57-a7a887aad602 | -15.65377 | -41.35473 | 2026-09-29 03:32:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1afeaba9-350d-34ba-a6a6-90e3fbe34baa | -14.08018 | -46.31982 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a56fd7c-5650-3644-ac8a-e0fa34b382ad | -11.41305 | -43.44419 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41628331-cc3c-3695-ba4b-387b34fdc120 | -11.41135 | -43.42696 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bebebae9-b4f2-330d-aa71-2211e5a29d28 | -16.34649 | -42.57577 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8227832-8208-3bd9-a463-76a406dd39e8 | -15.45671 | -46.14695 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4aa1ad6e-e05b-3a96-9e74-57a0a0fdb562 | -15.45489 | -46.14383 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15643141-a6a9-3297-988f-bc3045bb8608 | -15.45655 | -46.13633 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eed070ee-d3bb-3a6e-8bde-c57308a1b471 | -11.42138 | -43.46619 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e00b12c-45d7-3fac-855a-c7b2e402ba0b | -12.77563 | -44.15644 | 2026-09-29 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea33203b-c10f-3326-899b-0d552c1a1a5f | -16.34964 | -42.58772 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84f2e731-8ad4-309a-9ffa-ed0254737ef8 | -12.13954 | -45.00832 | 2026-09-29 03:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ceb22440-1129-3f06-ab38-ba824c119802 | -15.45335 | -46.15077 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e994f8e4-73f6-3b54-bb9f-4cc556ccf46b | -11.41653 | -43.43312 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bdbe1b8-7e57-33f5-b1d5-c0394e063f5f | -11.42655 | -43.47233 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c96b89da-2e4c-3fb0-a09f-9968eda077a7 | -15.46167 | -46.14495 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cf3b9555-8b7d-392d-ba30-bb0c23d5f1db | -11.41696 | -43.4634 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| db38dcb7-f6fa-352c-bd09-71a4c4312c1a | -12.2081 | -38.9849 | 2026-09-29 03:32:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 91dde807-3737-3033-ba3e-33febe756ddb | -11.43982 | -43.47017 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 032ccb5f-9f6e-3eab-8b90-512ef3bd5d57 | -11.42335 | -43.45655 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9f1a8fcc-be17-3a46-99ca-39979fd07fb1 | -14.11508 | -46.29328 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 727c4606-dad2-36f0-8511-db2af4628822 | -11.41207 | -43.44898 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcf9c903-a52b-32ec-a534-0c8bce3d9ad7 | -11.43019 | -43.46133 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a923bae4-8856-35b6-833e-7ca58038a079 | -12.77671 | -44.1513 | 2026-09-29 03:32:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 409f33cd-06ea-3b75-99bc-645229d6189e | -11.40471 | -43.42237 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d411a166-48f0-3b24-944a-b04fcb5d7cc7 | -10.27775 | -44.631 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4f9dab1e-d806-3917-a5d6-793e7792f68b | -15.83119 | -42.56092 | 2026-09-29 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8739fe9f-bad3-3a2a-9168-68ae3b774633 | -11.30523 | -43.54918 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc001516-8c59-3f14-a2be-559599e10647 | -11.41791 | -43.45858 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f8916a8c-6e0a-38f6-91ba-94f986668ce3 | -11.40594 | -43.44758 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f84c5bb-83d9-3ec2-ad00-e1d39145ff56 | -15.22171 | -46.19093 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76c1594-a31f-3245-a6ea-da2175f6c28c | -15.15082 | -43.6202 | 2026-09-29 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83ae3cbd-0fde-3a92-8317-906cddfc5d15 | -14.10827 | -46.29129 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a411bb88-056f-37f2-a07a-d66354803ddd | -11.44695 | -43.46667 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa501696-d552-3561-a074-23a13b5d2962 | -11.43047 | -43.45305 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d0fcfef-7285-390f-b719-49482a10270a | -11.43661 | -43.45437 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 93b24668-75e0-32d9-acd2-a5938bf78978 | -11.38546 | -43.39635 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a33bd23-5f68-3b3b-af80-7a54194d2dbb | -11.39623 | -43.43862 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb700cba-034d-3d74-b75c-7fd60f294ccc | -15.24825 | -43.27018 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 4c6a4533-0ae3-329b-a636-df5942ce97fe | -11.444 | -43.48125 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 25fe0e56-fab2-309f-8ec8-43d5f8bb96a0 | -11.42728 | -43.43726 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a486060-ede0-33fc-8b32-e681174dec24 | -11.3998 | -43.44625 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d041cacc-b4ba-30f5-ae36-e2246bf5e1a4 | -12.87417 | -44.80318 | 2026-09-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f1ab933-92ba-3c8d-8d14-a2078ed7ad1d | -15.23935 | -43.27703 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 5b0fd6e3-1af1-3ada-9afa-6b801520f751 | -11.4288 | -43.43579 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 19b0f77b-648a-3644-9942-75a3fa44526f | -11.43728 | -43.45781 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d1424356-71a5-3fb8-805d-0a602d71d284 | -11.43145 | -43.44823 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 722a2521-d7f5-3b8c-8e49-b8506e3db671 | -11.4231 | -43.4648 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8446cfda-1821-3d71-a84b-4c070afd502d | -11.42405 | -43.45996 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9b22790d-83d0-34d8-81d4-f1edbdb6bc37 | -11.4327 | -43.47367 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cbcf30a3-0d5d-32b4-8ee9-7504063440a6 | -11.18189 | -45.1421 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd989891-b474-328e-beb1-6e4c87cc59d2 | -11.41981 | -43.44894 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0191786f-0d46-3099-a942-72a32bf872c2 | -14.48467 | -43.26336 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d2b339d6-5764-33bb-8cdf-34eb1e14714f | -14.44664 | -40.75385 | 2026-09-29 03:32:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 11abdaaf-a205-397d-9807-b1327e51dc0d | -16.35039 | -42.58403 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31cbbf74-6858-3dd2-899b-fad4f30b6fd2 | -12.31266 | -46.40652 | 2026-09-29 03:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6d9684b7-4c2e-3e33-908e-aba968b8ddfb | -14.49041 | -43.26472 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7890d41f-cf05-31ea-8bbc-946f4266f32a | -11.43368 | -43.46883 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0e45dea3-79c0-34b5-9f60-7fdcafbe1e0f | -11.43304 | -43.44681 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cc299234-1fc5-32ca-8442-f64980c601c6 | -10.27528 | -44.64322 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57b85c2c-1be5-3cd0-adaa-297e77fe02c7 | -12.31101 | -46.41406 | 2026-09-29 03:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cee8bf2a-b06e-3f6d-82db-3f151256a52f | -13.43561 | -43.83005 | 2026-09-29 03:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52236834-33ca-3918-b3da-116e3299ff5b | -15.24018 | -43.27295 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 6e34b7ab-3cda-3ca1-9576-fbec74a0a4f1 | -11.425 | -43.45514 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7bf541f9-2405-30e6-ae20-59c31b6a1b70 | -11.40078 | -43.44147 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 820ef0b8-a7a3-320a-bd45-1a66143dd6ae | -14.48552 | -43.2592 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0569f932-3ed2-32f9-9e8f-da267db8b744 | -15.16704 | -46.14315 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 918b4533-23e8-338b-8707-15749ff8a32a | -15.65316 | -41.35778 | 2026-09-29 03:32:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f73316a7-3e7a-3d01-86f3-a4b5ad3be9fb | -14.44381 | -40.74918 | 2026-09-29 03:32:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e748a281-a416-36be-be9f-1375e40540a9 | -15.93773 | -42.34077 | 2026-09-29 03:32:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 89435aad-341a-3997-aee4-a279c8e0e5d3 | -11.40495 | -43.45238 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2dd871c-2e09-3de4-9583-3f081573fb24 | -11.30371 | -43.54679 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28866c85-7a47-3ab5-84d2-77a7d2b446e5 | -10.26183 | -44.64044 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 26682e34-0290-3a40-b707-4a762f2937ec | -11.37836 | -43.39986 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77be7a71-6257-3580-a4d2-4e9af18ad1ab | -11.3862 | -43.45682 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d968298-e8a5-358a-b3a1-afafc821ebb8 | -11.43884 | -43.47502 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8edd3a2b-46dc-3911-9f0c-87206a622790 | -11.3965 | -45.41529 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3fbfe05-dfda-3b80-a000-08c8664dc55b | -15.24086 | -43.277 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 79a958ec-0b89-3956-bc2a-ba02b6000b32 | -11.41558 | -43.43793 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdfbf125-b06f-3d95-8543-f46fec2ebd56 | -11.17601 | -44.79014 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 70090087-0b94-3ad2-b612-852524914609 | -11.18052 | -45.1486 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 539bba90-0837-3c57-85f6-d9af9ef9601d | -12.00376 | -44.92795 | 2026-09-29 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb6cf525-f57b-31d5-8d76-0c71d6805ac4 | -10.7132 | -44.42962 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| babfb246-d3ad-3d30-b9bd-8320386e8399 | -11.67726 | -44.54485 | 2026-09-29 03:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e792a640-1030-3d59-9b69-ce2f291c2125 | -11.4085 | -43.44133 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eff9ef1c-b5d0-390c-8ad2-7db81601db1f | -15.2118 | -46.17184 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5f92565-21a8-3e85-adb7-a9f9e379631a | -11.41918 | -43.44555 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| faedb620-cf44-36c0-9c01-a8118544ff66 | -11.43114 | -43.45648 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a8ed3f5-3a74-3ec4-9df0-240c9222c96d | -11.41748 | -43.42829 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1264897-9ac4-3f3e-800d-20599a63e835 | -11.42735 | -43.47581 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fd45d874-840f-3d07-b6c4-31d84be2ff00 | -15.45849 | -46.13915 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README12.md)
