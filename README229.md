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

## Dados Diários - Página 229

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5440447f-0d40-3ad7-a215-c59b73d45dd5 | -12.02958 | -43.44431 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 375bbbfc-4d1d-383b-872f-29f35af2560e | -14.26629 | -40.70269 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 90cf345d-f957-3834-8dbf-7921845cf6cc | -18.05277 | -44.57253 | 2026-10-08 15:39:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9cefc091-bbb2-3006-bea4-10175d3e488c | -11.61173 | -43.6536 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3cdf6af1-a2fd-3cf5-95a0-b76085b78cda | -11.83825 | -43.56886 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 035cbb6b-65f0-3d08-8832-359262450b2c | -14.39312 | -41.64223 | 2026-10-08 15:39:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e44610ef-d712-3969-bf1f-975865bb11ad | -14.03497 | -40.55706 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| fa07383c-7234-354d-89c0-7b8dba9fdb9f | -10.76503 | -38.72699 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 68841e07-a3cf-36b4-85fb-022839e4178e | -11.76633 | -45.58799 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 140f5844-acb8-3268-95c3-5f2a2ea9970f | -18.25948 | -42.17505 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6850b99a-3469-3739-93e0-588e6ad7d2a4 | -14.53666 | -41.27211 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5edc0f74-dafe-3b8b-8158-bb3b536fca60 | -11.06032 | -39.50374 | 2026-10-08 15:39:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 893905f8-7d3e-3b7a-bff9-d8ccbcff0f56 | -12.13963 | -43.31548 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6163dac0-b7e3-3600-beb3-e32d73e93f56 | -14.2658 | -40.70417 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 906e0596-92fc-3f8b-9969-09c4a0d3a896 | -12.61914 | -44.54083 | 2026-10-08 15:39:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 9171e281-5824-3e19-8287-520752beef56 | -17.109 | -41.35476 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 982529b4-4322-3fd6-bf68-31807ab04471 | -12.03548 | -43.43958 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0373e2a9-7e77-34c9-a4f5-8e70a72bfba6 | -15.56662 | -39.41317 | 2026-10-08 15:39:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| baf48c7c-70a1-38a1-9173-a16c51b1abaf | -11.6205 | -43.68186 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d0f608be-5ced-3acc-a520-19441a25b3e7 | -11.76667 | -44.68728 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9c208ab6-6e37-3d73-892e-b5ffdc050164 | -16.45906 | -41.25991 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| f735c7bc-ee19-3bb3-b694-25af3d906ec3 | -16.4569 | -41.27118 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9a516f7e-3c12-3a97-937e-e45116eca4c0 | -11.64105 | -43.69658 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e30231a3-1459-34ce-a6bd-ab689f1d7393 | -12.51061 | -38.69569 | 2026-10-08 15:39:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 502226e8-56b8-38ed-a98d-6d95e122febc | -11.99596 | -38.03955 | 2026-10-08 15:39:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| d045b15c-599f-3c99-8d51-35216514714e | -14.66903 | -40.49899 | 2026-10-08 15:39:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e213582a-06dc-3941-8fc0-69b298937a47 | -14.17187 | -43.66869 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 98241555-1b93-3efd-8526-d1f37fa20079 | -16.23455 | -40.15085 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6ab7045d-efec-3501-91a4-b86faf1d9b96 | -11.61058 | -43.64398 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5931f7d4-1771-379a-ba1d-373ea608f81c | -13.40523 | -40.78036 | 2026-10-08 15:39:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 80f32951-9e8f-3116-8c16-8f92365f7a04 | -13.60533 | -40.6692 | 2026-10-08 15:39:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e9874d0a-0d42-3efd-9057-860a4c93821d | -11.61084 | -43.65173 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 5a8b4a3e-f760-3112-8e64-a699be8c3e23 | -12.03519 | -43.38728 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b55c39c3-461f-3f6d-81f2-60785278f64f | -17.95814 | -42.77718 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 532f50ee-653a-3ac5-bbf1-a805c998af50 | -11.76166 | -44.93416 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 696a0671-e419-326c-bae3-d3a2de5c22dd | -11.6422 | -43.70674 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| b594f65f-b5d8-378f-83cb-e59eda642bf9 | -11.76282 | -45.49675 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 251a0046-1ce1-38ed-bd1b-9379132d4524 | -13.36493 | -43.87774 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 771fbbdf-be5f-3230-9d95-9c4c45a3c0b9 | -13.95753 | -44.85258 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0b601a57-382e-393a-bc25-190699bd3a58 | -11.61595 | -43.6414 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f945b0c8-fa9a-323c-8f14-801eb2974002 | -15.51685 | -42.65408 | 2026-10-08 15:39:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| dfc57e41-f116-3251-a15c-905cfb9a466f | -11.79542 | -43.52089 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e068a57a-970a-38cf-b696-07b88d95ed35 | -14.97597 | -40.6609 | 2026-10-08 15:39:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 20617c72-a22d-3e07-b404-a1f5f40dff58 | -11.30758 | -44.8308 | 2026-10-08 15:39:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b486c063-fc9f-372a-8ae6-cd8ce5b028c4 | -14.30109 | -39.21206 | 2026-10-08 15:39:00 | NOAA-21 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 513f0d7f-d53d-3e67-97b3-0bc8dc2cd7cf | -11.63727 | -43.70922 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 69099411-c530-3d51-b2c1-4f0f76758508 | -15.06114 | -41.35278 | 2026-10-08 15:39:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 909999cd-894d-3167-90ad-e84fb57bcaf0 | -11.30092 | -44.83132 | 2026-10-08 15:39:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| f984f6fb-911c-3bf4-956e-832f7a6b1b6e | -14.05864 | -43.8261 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 3a1066ea-0177-3fcb-98d3-e14b09bde725 | -14.57093 | -41.66787 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 541010a5-b7df-3cbb-a26f-1ff49ff04002 | -11.63652 | -43.71225 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 3c637d61-d333-3079-8303-21b28b77a7ee | -14.47624 | -40.71822 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0314a929-2584-3b76-bb88-2678fcd6bc97 | -11.60554 | -43.65432 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e8576df7-3092-3940-a8c0-c2f1fc85f48e | -11.77996 | -45.59127 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| ca5a5f39-511b-332b-8a69-7966974a1c8c | -12.19056 | -44.81964 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 927c1836-ebb6-3a6a-9ce9-96485a1b003e | -12.71622 | -45.82259 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| a3a84359-6ed9-3446-9192-b9713c37ff01 | -12.20047 | -44.7881 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 015234aa-05a2-33a9-b2e3-a552b33ca6f6 | -11.62413 | -43.70479 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bc99cbef-885d-30cb-ac18-143a9d59c4ad | -14.48627 | -41.80507 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f59bf78b-4254-37f1-8a97-bd20602c6a16 | -16.95421 | -40.05821 | 2026-10-08 15:39:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ea2fcb9b-c351-32f1-9d7b-a42069ae920f | -14.49427 | -40.82358 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7b55b491-6ad6-3376-9b44-aaa3238d0ead | -13.9692 | -44.84394 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3cf747d1-89e7-39e8-b074-3a70c3d9acbe | -12.32742 | -38.93705 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c377e4fc-cb36-320d-a50b-609b198d9342 | -11.76799 | -45.54143 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| b073c877-9e38-3bd8-8808-f0fc027adc25 | -13.73822 | -42.66335 | 2026-10-08 15:39:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8673b43d-02fd-3576-8bbe-13365949e940 | -14.4332 | -40.8118 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e0ed75a3-de13-3404-a84e-447a482d4c37 | -13.35657 | -43.87739 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 339f2fdc-fca0-377d-a12d-951c0117354d | -18.26702 | -42.18056 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| e6226716-2827-3327-9a35-3ae8ffe79883 | -14.43191 | -41.13754 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3ad84b41-7b59-3e6f-be39-e3119b3c5b2a | -14.48162 | -40.71805 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 312d5639-f78f-30f3-82d0-a88b23c2011c | -15.11176 | -43.62406 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 13.4 |
| c8d0ce9f-c48d-388e-9a12-18f23660c519 | -13.97678 | -44.8376 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 6cb34b49-6319-3b2b-b4e4-b17a3ea35da3 | -14.85217 | -42.06504 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 7c3647cb-1ea8-3c88-a70a-311d5c8566d8 | -17.92284 | -42.28603 | 2026-10-08 15:39:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| b11b0798-7edb-3bac-bfec-a725e91583ab | -12.22835 | -43.93307 | 2026-10-08 15:39:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19ab694c-76df-3720-a761-811f1e23bc31 | -15.76345 | -41.77508 | 2026-10-08 15:39:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 97dad8b5-8537-3816-96d8-c4b30366f849 | -14.35414 | -41.49535 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7d75b682-9ec4-3afb-9414-801f95851f28 | -15.34326 | -41.69736 | 2026-10-08 15:39:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ee6b43ea-c3bc-393f-a256-d9e86d2968c5 | -11.85272 | -43.5311 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9f4a2db7-dece-3704-8982-5337be5e26a2 | -11.62788 | -43.68358 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| eb4d10bf-742e-387d-9b78-c8837525810f | -11.74217 | -44.94202 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3f29e905-d64c-3350-8143-c3484661c6f8 | -11.6123 | -43.65834 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a91e241f-357a-3b6e-8792-f5e85f6afa39 | -15.11285 | -43.63501 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 352e02d2-eeaf-3b00-af91-fa4099746287 | -11.6429 | -43.70367 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 2736cefa-c40b-39a0-abcb-3bb480a2f52d | -11.63635 | -43.59755 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 9e44d568-217f-3c8b-9985-baeb932fae39 | -11.2357 | -44.02261 | 2026-10-08 15:39:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f5c3a88a-1b7b-38a2-88bd-e76cfb2bdc28 | -12.24629 | -44.73792 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 04657fda-69f6-3fc3-a2ac-811d671b5e97 | -11.74073 | -43.64376 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6e906939-27d1-35ae-94f1-220e42aa970b | -14.44398 | -43.92501 | 2026-10-08 15:39:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 7b9bba53-383e-3f73-aee3-54e3a20416ec | -12.28473 | -38.9667 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 77d1bfab-80b0-3cc0-a1f3-7256e5e9b94d | -11.64609 | -43.68554 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1d3b0901-e16f-3076-b8f3-ad543b255c54 | -14.60033 | -40.01917 | 2026-10-08 15:39:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 49614913-f512-3494-9992-b8a9a0e7566d | -15.00375 | -44.05585 | 2026-10-08 15:39:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 677cb095-5efb-3c69-b448-51ce5ee2370b | -12.1328 | -43.31567 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7a18745e-1822-3786-b166-50cd4ae0cf5b | -11.61323 | -43.61723 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 20d9fcc9-e2b3-3b8f-95bb-c71177c5f8db | -14.23706 | -40.91205 | 2026-10-08 15:39:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 19371d28-668a-3ce3-845c-ef3388a8ad6f | -17.40492 | -42.90299 | 2026-10-08 15:39:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 9c7042ce-8965-3b45-9f52-edc8ea6b686c | -17.96079 | -42.7708 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a0dabc9e-d03f-3ab1-8efb-29d7cd0fe9ba | -16.23488 | -40.15385 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 485f38ad-8d13-38c4-a68c-89c7a8d51d5d | -12.54214 | -42.0469 | 2026-10-08 15:39:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README230.md)
