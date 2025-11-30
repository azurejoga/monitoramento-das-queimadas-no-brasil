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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcf342ad-0635-3c0b-82b7-b931a2d24a79 | -8.17041 | -43.20977 | 2025-11-30 11:57:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 732ae509-27b3-312a-be4b-ae97d778ca05 | -5.75284 | -42.12316 | 2025-11-30 11:57:00 | TERRA_M-M | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c90a4f65-2f4f-37eb-8d8c-0bfffbe4f818 | -3.52241 | -41.96879 | 2025-11-30 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 134.7 |
| 2711e7fd-1b60-3b82-8326-33388769fc18 | -7.9125 | -37.19183 | 2025-11-30 11:57:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 27.4 |
| e1762302-77b5-3936-babd-3af43721736c | -5.64005 | -43.61848 | 2025-11-30 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| efd1cef4-9af7-3f8c-8b7d-c471485455c9 | -2.77955 | -44.11788 | 2025-11-30 11:57:00 | TERRA_M-M | AXIXÁ | MARANHÃO | Brasil | 2101103 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0cb1219f-e839-329b-b3b2-fa9daf1ad5f6 | -5.64134 | -43.60962 | 2025-11-30 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3ba8d528-a821-341b-867a-f25d4e01f863 | -4.38708 | -43.3461 | 2025-11-30 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 13778f3a-afcf-3921-abc5-8313dc519114 | -8.57262 | -40.27679 | 2025-11-30 11:57:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 58a3d949-0ea1-37ef-89a3-f8cd70b0f480 | -8.25469 | -36.53502 | 2025-11-30 11:57:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 1ba7bc3f-e38c-3d64-8299-c7add4f92ac2 | -5.82572 | -40.68614 | 2025-11-30 11:57:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 2e4764f1-6c8f-3be8-abf2-f6c78f2e4cf0 | -3.63283 | -42.7542 | 2025-11-30 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 5ebcd26e-a5c2-326d-bb54-a27e9ebc8b51 | -3.83419 | -42.0548 | 2025-11-30 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 1a609e33-81b9-3127-85aa-43063d6be1e0 | -5.51184 | -42.58545 | 2025-11-30 11:57:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e1ce4e9e-a9a3-3ed8-8cd5-5e5dab0c2aaa | -8.5504 | -40.21351 | 2025-11-30 11:57:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.2 |
| a48bf99e-8cb1-38d0-aa67-9cf42278520a | -6.30366 | -43.80984 | 2025-11-30 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5dff776a-daf4-34ad-9106-78f9aa19abd0 | -5.33277 | -40.32796 | 2025-11-30 11:57:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 05802d1f-2d00-37f6-ac55-8fbb72e23c18 | -8.24669 | -36.52761 | 2025-11-30 11:57:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 41.7 |
| e4279bd3-ecff-3363-9e78-9dca0a0c2786 | -8.88197 | -37.06443 | 2025-11-30 11:57:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 912511c6-d4b3-33d5-af81-a28bb88470dc | -8.25225 | -36.5549 | 2025-11-30 11:57:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 23.6 |
| bb4f1ec8-210b-3be9-9fdd-9f17b9ddb75a | -6.53211 | -41.69466 | 2025-11-30 11:57:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3aff40e3-ba76-3c33-bc12-9565ac3d5a1a | -2.79189 | -42.30745 | 2025-11-30 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dc1450b7-b001-3bb1-a19f-cefcd93c0502 | -2.88557 | -44.90416 | 2025-11-30 11:57:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 22778ffd-360c-3322-a816-3462254d4938 | -5.36552 | -43.02509 | 2025-11-30 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fb09b653-8c4e-31ae-b161-4feaad380f45 | -8.57101 | -40.28854 | 2025-11-30 11:57:00 | TERRA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 461a31e3-d3c2-32b8-a1ac-0f0fa2936035 | -3.83293 | -42.06363 | 2025-11-30 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 9acd2a61-7529-310e-ac3c-27e85e1c4df1 | -7.16892 | -41.35504 | 2025-11-30 11:57:00 | TERRA_M-M | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 9f5e0baa-ba14-3b5c-bef3-c3b3c69a2ce2 | -8.5524 | -40.49762 | 2025-11-30 11:57:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 41844a0a-4d41-3cb7-b00f-3fefd160c9e8 | -3.57676 | -42.04534 | 2025-11-30 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9fd3628c-0541-3107-8527-69763fb11eb8 | -6.05307 | -39.93956 | 2025-11-30 11:57:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| f83988b4-826c-3ae7-bbdc-38ab99784c9c | -6.05135 | -39.94509 | 2025-11-30 11:57:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5370e679-33ae-365d-8c6c-f14f948f031a | -4.16253 | -42.01034 | 2025-11-30 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 83727990-aaa9-3a0b-8821-314894ef8dc8 | -3.36229 | -42.19164 | 2025-11-30 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e53220d8-fe92-3e13-8f96-30c107e7df76 | -6.78812 | -41.71008 | 2025-11-30 11:57:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 5c5e397d-8f1d-39e4-ae50-1a9d1a5f1a6b | -7.38244 | -39.08255 | 2025-11-30 11:57:00 | TERRA_M-M | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 0bcf4a4f-34ee-3128-8d2a-4fce88f9994e | -2.79064 | -42.3162 | 2025-11-30 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d376fade-93a0-3a76-83e1-a444beefcac5 | -8.3533 | -39.18561 | 2025-11-30 11:57:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b4fff74e-a6f6-3654-b8a8-6bc4f1582c94 | -3.36103 | -42.20042 | 2025-11-30 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 68390d0c-746a-3823-a2fe-20a71aaa48ec | -8.24406 | -36.54793 | 2025-11-30 11:57:00 | TERRA_M-M | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 115e9dde-8ace-3808-9f08-8495d28db8f2 | -6.1748 | -38.40092 | 2025-11-30 11:57:00 | TERRA_M-M | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 16.7 |
| ab4af5ab-3b91-3718-b361-7d8308b306d1 | -6.17473 | -38.40736 | 2025-11-30 11:57:00 | TERRA_M-M | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 19.2 |
| a454e8ef-6d03-3e78-896d-9ad1463cbc71 | -8.29023 | -38.71622 | 2025-11-30 11:57:00 | TERRA_M-M | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 582be6dd-8354-3507-bca3-ccd2ad64db50 | -4.11573 | -42.02197 | 2025-11-30 11:57:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f8ba95b2-af61-3332-a27e-abce59f27a88 | -4.46087 | -41.47313 | 2025-11-30 11:57:00 | TERRA_M-M | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dd421bf6-605b-3443-94c3-5937ce7fe3a9 | -3.84177 | -42.06484 | 2025-11-30 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d14a860e-add3-3043-895d-fe25707879a4 | -8.69235 | -40.74507 | 2025-11-30 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cc2bae19-3a84-3b83-a507-30d3bb7793cc | -18.12544 | -47.15619 | 2025-11-30 11:59:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4774e8c8-7a7d-372f-964d-a9e0eced3dfa | -20.16822 | -44.80958 | 2025-11-30 11:59:00 | TERRA_M-M | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5bb4bda-52c1-3fd0-ba68-42726462b016 | -18.71943 | -39.86145 | 2025-11-30 11:59:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 1e363e36-2884-386d-a9da-5db6ebe4a015 | -20.60597 | -41.21133 | 2025-11-30 11:59:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5966e6a4-40c3-30dd-ba0c-f42e6794e5cb | -12.72804 | -46.805 | 2025-11-30 11:59:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 04b9157e-e1aa-3a85-be75-a9ac025767bf | -15.81121 | -42.22597 | 2025-11-30 11:59:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c2f07885-f1cd-39e5-b46d-62ede595ca79 | -19.08845 | -48.59063 | 2025-11-30 11:59:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8bbc1d93-5e2b-316b-9508-f9de3bd4d34b | -19.09798 | -48.59224 | 2025-11-30 11:59:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 81f033eb-4fc6-3cba-b84a-7c6539bcc7cb | -19.16177 | -44.49335 | 2025-11-30 11:59:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fc29598-32f8-3be7-83ee-b090517979ce | -14.81316 | -43.57397 | 2025-11-30 11:59:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| a0c8a346-a3c4-3fde-80f2-fd33592765ad | -18.41265 | -46.84168 | 2025-11-30 11:59:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eee7fdaa-5481-3670-a262-7fd61e629c27 | -12.72319 | -46.79768 | 2025-11-30 11:59:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| beba8a3b-adba-3dc5-9934-8db99d22bf08 | -14.70529 | -46.99709 | 2025-11-30 11:59:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3a9062bb-8b50-38f9-bb14-3e401d987e6f | -14.81185 | -43.58352 | 2025-11-30 11:59:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7082936e-fce5-39ae-bbb4-5ac4ae5cc05e | -12.72166 | -46.80793 | 2025-11-30 11:59:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0ab64475-531a-3ce3-8062-a62d91b6e378 | -19.88359 | -44.59884 | 2025-11-30 11:59:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6109da55-329c-388a-868f-79a7fd7e827c | -19.18288 | -44.74429 | 2025-11-30 11:59:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 09984552-fee3-3f33-9e1e-b0b99ecbd50e | -18.41123 | -46.85119 | 2025-11-30 11:59:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1ade3d01-d003-37d5-ab72-1c259e9f6d90 | -14.78835 | -39.27458 | 2025-11-30 11:59:00 | TERRA_M-M | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| cfaa0e11-53a2-3d2c-84a2-0323e8a5b3a8 | -15.31691 | -42.01863 | 2025-11-30 11:59:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 271ac098-85b9-363a-9c2a-57181df868dd | -18.72383 | -39.86776 | 2025-11-30 11:59:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 51515f75-5aa5-301f-80da-b2fb051b03ce | -17.4954 | -57.133 | 2025-11-30 12:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 614e26d3-0374-35fe-bed5-f67c34db6324 | -17.5148 | -57.1513 | 2025-11-30 12:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 21ec866d-e6b2-3a2c-a500-caa769d88af8 | -23.43392 | -46.36996 | 2025-11-30 12:01:00 | TERRA_M-T | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| a86646e2-1bcd-3167-a78c-5aee7498f9c9 | -23.19091 | -45.65908 | 2025-11-30 12:01:00 | TERRA_M-T | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| ff1e32c2-0be5-36dd-ae24-94123904a902 | -23.11888 | -46.11708 | 2025-11-30 12:01:00 | TERRA_M-T | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5e988e3a-36e7-33e8-8de0-f10509941e8c | -20.95454 | -43.80145 | 2025-11-30 12:01:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6346ccc3-0ab2-3f68-8ff1-7d41ada61ef3 | -23.20056 | -45.11016 | 2025-11-30 12:01:00 | TERRA_M-T | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 5755d103-a464-3dd0-bd97-59d97d2bf861 | -20.89322 | -42.34299 | 2025-11-30 12:01:00 | TERRA_M-T | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d44b3cfe-71ad-312d-b051-362779db9714 | -21.10954 | -44.02323 | 2025-11-30 12:01:00 | TERRA_M-T | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 711872e7-0bfe-3942-a868-f42ea5a4c9ef | -23.44279 | -46.37136 | 2025-11-30 12:01:00 | TERRA_M-T | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 73a1a14c-0e03-36e0-8c36-7c3dfc5abc21 | -23.56723 | -46.26928 | 2025-11-30 12:01:00 | TERRA_M-T | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 57dca5f8-d642-3c70-af45-66491eb8b8a1 | -22.94646 | -43.36283 | 2025-11-30 12:01:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b6f2fff9-68fa-336e-ab3e-0b402e19f0e7 | -23.19921 | -45.12029 | 2025-11-30 12:01:00 | TERRA_M-T | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 25e7ef49-df2d-346b-8e21-5a4964bf30d6 | -20.45086 | -45.30183 | 2025-11-30 12:01:00 | TERRA_M-T | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c5116259-6f53-3e16-9eee-147483d36dc8 | -23.55343 | -47.20653 | 2025-11-30 12:01:00 | TERRA_M-T | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 05760dc6-658d-342e-85f6-0fcfaab91f08 | -21.70549 | -43.43485 | 2025-11-30 12:01:00 | TERRA_M-T | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 39de20d8-2b1f-3057-b2f5-e4247780bea3 | -17.5148 | -57.1513 | 2025-11-30 12:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 160bf993-5d33-31d0-b528-6245ca080e6e | -17.4951 | -57.1537 | 2025-11-30 12:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 5eb3d69b-9d49-35d1-a636-fa663830a143 | -17.5148 | -57.1513 | 2025-11-30 12:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 0b4e1a47-1422-365e-aec1-9a13b3eb5f0c | -17.4954 | -57.133 | 2025-11-30 12:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 4e15417a-7b04-3df0-a2a8-cfe8852cf272 | -19.9339 | -57.4386 | 2025-11-30 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 1a56a956-bc37-3d95-8b63-0a929165c53b | -17.4951 | -57.1537 | 2025-11-30 12:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| e11467a1-a713-3a59-96d2-03d954e2a9d5 | -17.5148 | -57.1513 | 2025-11-30 12:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| efd2a0b3-91da-3276-952f-1b2738bc394f | -17.4951 | -57.1537 | 2025-11-30 12:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 06202412-4255-3d9a-a441-62743886dd0e | -17.4954 | -57.133 | 2025-11-30 12:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| ea03ec4f-7d95-3fde-ac34-5750961d5b7d | -19.8473 | -57.7835 | 2025-11-30 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 99e7cee7-6c3f-32f5-8f0e-c92595d1ad58 | -19.9339 | -57.4386 | 2025-11-30 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 4b8a914a-d215-3361-88a9-8b7949247964 | -17.4951 | -57.1537 | 2025-11-30 12:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| d085177a-b3df-38a8-bc27-e56c2b72259e | -19.9343 | -57.4177 | 2025-11-30 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 0e0655e1-897a-3440-976d-963b3309067b | -17.5148 | -57.1513 | 2025-11-30 12:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 3a93fbea-7164-3fd8-ba9c-487772985169 | -19.8473 | -57.7835 | 2025-11-30 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| c9986cc3-b629-36cc-aed0-e791c501e00d | -19.9339 | -57.4386 | 2025-11-30 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| aae40d74-cf3f-3f12-bfed-ff8b50875b04 | -17.4954 | -57.133 | 2025-11-30 12:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |


[Clique aqui para ver as próximas entradas](README23.md)
