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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7f5bd74-3a1f-3007-8adf-ec04ae428a21 | -11.05841 | -45.35638 | 2025-04-09 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c93d5307-66a8-3c5d-bf37-970d8b71a91f | -9.56369 | -35.69106 | 2025-04-09 04:02:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f6a3e00-c2af-312e-a09c-273703b28052 | -8.85995 | -49.88788 | 2025-04-09 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eceef9a8-fd71-3dd1-ab00-035c9273deed | -19.77162 | -43.8283 | 2025-04-09 04:04:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 82b26049-effc-38b8-8cf1-42edaaf167ce | -14.67364 | -45.81074 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31653002-7980-3f9a-9bf8-8195743914b3 | -17.86645 | -44.56203 | 2025-04-09 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06bf0b77-17e3-387e-8ece-c311e84cae10 | -20.41787 | -43.55176 | 2025-04-09 04:04:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 93117eb8-b229-301e-88b8-5347f62a8cfc | -21.9132 | -42.26207 | 2025-04-09 04:04:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f00ddbbd-81f3-3e7a-bf5e-9e26f39e47b5 | -14.67281 | -45.81545 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c2f7c83-1fe8-3475-8f28-16fd985634f1 | -19.16143 | -47.81747 | 2025-04-09 04:04:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 384b3978-8ed0-342c-b349-d7257a8bd4d2 | -17.86516 | -44.56977 | 2025-04-09 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcca060f-63bf-3617-ab0d-d7fc7b4c3196 | -20.34965 | -40.36044 | 2025-04-09 04:04:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fbc22bfd-9ebf-383e-9430-eb3615f407d3 | -17.37917 | -42.48354 | 2025-04-09 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba0e556c-0da0-34a0-86c1-edb2236ab8e4 | -14.67168 | -45.81752 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047fcf9f-ca04-3256-8f5f-c64a9caaffc0 | -17.45394 | -48.17231 | 2025-04-09 04:04:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d79c23b6-9c74-31ee-b358-b5b4e41110f6 | -16.35089 | -43.69541 | 2025-04-09 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb1e1926-cc1c-3bfc-8179-f6147b847cda | -19.85042 | -43.84563 | 2025-04-09 04:04:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 82f2a16a-d0a6-317a-ac9c-f589a546faf9 | -20.985 | -43.03508 | 2025-04-09 04:04:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 071e6f40-ade1-3346-926c-e2452d38e5e1 | -14.66873 | -45.81216 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c137590f-5f45-3cba-8f75-dea7c83bf54f | -17.48366 | -48.98123 | 2025-04-09 04:04:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 722b37f8-1ebc-3217-8329-8791de326f0e | -14.66905 | -45.81482 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d823521c-45c3-341a-9de0-f26b93765db1 | -17.8658 | -44.5659 | 2025-04-09 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77f62fd9-56bf-3a2f-923b-dc584352377e | -14.67248 | -45.8128 | 2025-04-09 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93fdd816-51ae-396c-bdfd-9cabb08c4b3f | -17.94279 | -44.41951 | 2025-04-09 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db04a548-3f6b-35bf-9691-ec38a63f6ee1 | -17.09558 | -43.80527 | 2025-04-09 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 278788f4-455a-343c-9f12-97ab127047aa | -19.51433 | -44.27612 | 2025-04-09 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff0dbee-07c5-306d-b3c3-0f39c3199c52 | -17.38592 | -42.65808 | 2025-04-09 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1690997c-fbd3-381e-a299-248132d19b8f | -18.00872 | -49.39658 | 2025-04-09 04:04:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e812cb4-3421-33e4-bd94-9aff6d1cc866 | -26.66795 | -48.88186 | 2025-04-09 04:06:00 | NOAA-21 | LUIZ ALVES | SANTA CATARINA | Brasil | 4210001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| 60d275d0-8a30-365e-af53-0389494c7168 | -23.15382 | -49.1482 | 2025-04-09 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47ed2a72-67cf-31af-b507-4a42a3ce23dd | -23.15778 | -49.14911 | 2025-04-09 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 68421e21-22a1-34e6-9c1f-7fe7fdc661fa | -22.84559 | -43.79187 | 2025-04-09 04:06:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e7462db9-2a74-3101-ac76-0e9a975ee348 | -23.36692 | -46.28019 | 2025-04-09 04:06:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 879fd898-4594-3806-b059-99d2d9cea231 | -23.33966 | -46.77276 | 2025-04-09 04:06:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9823f99d-8607-3fe5-8cd0-d44c4d638579 | -26.67253 | -48.87789 | 2025-04-09 04:06:00 | NOAA-21 | LUIZ ALVES | SANTA CATARINA | Brasil | 4210001 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| cc625a13-2684-363d-8633-5e9223a47fa3 | -23.15454 | -49.14446 | 2025-04-09 04:06:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ad8e5f2-ea3c-330a-9146-722cec430cb2 | -23.33991 | -46.77135 | 2025-04-09 04:06:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e761b8d-6526-3c15-b9d4-9acaf2ee0b39 | -7.06948 | -44.3721 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1295635f-a9ec-3b26-8d58-8d63a7418a2f | -7.07177 | -44.38021 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22006c9c-07bb-3966-b9be-d2e378c78bcb | -6.59063 | -44.78617 | 2025-04-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4401ecf8-e6ce-3974-bcfb-0a8c5ed2fcd3 | -6.68385 | -43.57003 | 2025-04-09 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb71955-ae99-32a2-b455-53dc7cfaabe7 | -6.49607 | -47.49076 | 2025-04-09 04:25:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eea1be60-688c-333a-8ad3-0470a019c628 | -6.59346 | -44.79028 | 2025-04-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c78eb6-728a-3784-b8d7-2a7712b6429c | -7.56774 | -45.8463 | 2025-04-09 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcc4301a-5c7f-37da-94ca-d7f881cbb764 | -4.60776 | -43.31652 | 2025-04-09 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f73670f6-504d-3f35-8a54-60c845719f89 | -6.59118 | -44.78257 | 2025-04-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28a6bf47-a52f-3b5e-aac5-be44bdd8eb79 | -6.71823 | -47.60686 | 2025-04-09 04:25:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84589ebe-552d-34fa-b158-c3a965d65bd8 | -6.01303 | -43.8527 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ac5f175-adc9-36ae-83b0-ad804989598d | -6.01362 | -43.84888 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33ef06a2-6b18-39fa-b65c-1c6f1d5ac664 | -6.0165 | -43.85324 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 33d25d9f-6736-32f5-a9d7-2b6edf41bda5 | -6.01421 | -43.84506 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ec96675-6b9d-38d6-87bc-1731b2452983 | -8.11423 | -43.12343 | 2025-04-09 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 015a805a-68dd-39ad-93c8-600659ccdbf8 | -8.11055 | -43.12286 | 2025-04-09 04:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c8c1923a-9d7c-31e2-84d8-460116e33140 | -7.07695 | -44.3694 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feaef1a9-8aaa-3e7b-a29e-ce1c0fc79f2b | -7.57107 | -45.84683 | 2025-04-09 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f503b5e8-eeab-3c4a-90e3-f726a6c35fb1 | -6.0171 | -43.84942 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f3c3594-35bc-3a40-a994-d73ac96d71dc | -4.87417 | -47.40893 | 2025-04-09 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6bed34e-217d-30bb-8f65-e9bc917a781a | -7.07293 | -44.37264 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98e5e848-3a9d-38a0-a265-1af37b5fb033 | -7.07235 | -44.37643 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ffcc60d-dd86-3938-af06-0c885536a987 | -4.59572 | -43.18318 | 2025-04-09 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c2e9fca-e66b-357c-b794-2280614da174 | -4.79516 | -43.78184 | 2025-04-09 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2f4cd6c-5b90-38f0-ae12-218bc1d83c7c | -7.0689 | -44.3759 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6aa6b2d-6626-3b10-95ec-e6131bead298 | -7.07521 | -44.38073 | 2025-04-09 04:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d8448b2-c8a5-3043-b519-36cb160b6441 | -6.01769 | -43.8456 | 2025-04-09 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 435d01bd-8d4d-30a4-836c-63ea37e96fc5 | -11.87996 | -43.93726 | 2025-04-09 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52cc9a40-0cc6-331c-8a8d-e3a1175c188e | -9.02537 | -40.58569 | 2025-04-09 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 311fe1a0-afd9-3072-93c3-647f9039c722 | -10.54225 | -44.67225 | 2025-04-09 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ee8dda-400c-3185-96d5-9d5c976a5db0 | -11.05835 | -45.35448 | 2025-04-09 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1134ec55-7989-318f-83a7-53c26e678151 | -13.68126 | -47.75911 | 2025-04-09 04:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79696497-83bc-3ba4-8139-f9df76c305eb | -10.72302 | -42.3191 | 2025-04-09 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| eb98c76e-f30b-30ad-8e8a-d6d7b0775357 | -13.68458 | -47.75965 | 2025-04-09 04:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67a17b05-3692-348c-a0f7-8ca253dfd85e | -13.28874 | -43.19241 | 2025-04-09 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af840ae2-5951-310b-a75b-e709b5917a3d | -11.92624 | -41.86131 | 2025-04-09 04:27:00 | NPP-375D | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18a89945-190f-3a19-bae3-0b622e42b817 | -9.81485 | -48.04129 | 2025-04-09 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2ecb265-f086-36c7-b020-c297431d4ee9 | -12.10582 | -45.61933 | 2025-04-09 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3912127-347a-316b-8fe5-490729d239fd | -8.85958 | -49.88725 | 2025-04-09 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ad4a6165-49f3-3991-a640-67254e72672f | -13.01602 | -45.07172 | 2025-04-09 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc61eafd-4e2a-3cfb-aee3-8d341a154631 | -13.28482 | -43.19184 | 2025-04-09 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a8d5faa-d36a-3820-9151-d44484f568b7 | -12.10524 | -45.62312 | 2025-04-09 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2c3a418-bbd4-394a-a586-0f0a4808e1e0 | -13.67683 | -47.76565 | 2025-04-09 04:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f4a816f-da11-3a1e-b229-206edc4b9fac | -13.01661 | -45.06768 | 2025-04-09 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8caf242b-a51d-3cf5-8317-c0ea52387e5b | -10.73101 | -42.32026 | 2025-04-09 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eab05b0b-5203-32e9-8809-396dfaa16bb6 | -10.53859 | -44.67219 | 2025-04-09 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3abc2ae-9e57-388a-a0ed-bf196137ded3 | -12.0961 | -45.61395 | 2025-04-09 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 772d678a-519f-3b1e-9779-5e29e67c0135 | -10.53919 | -44.66824 | 2025-04-09 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed681be-73eb-3335-a7e9-acad7010d2e8 | -12.10181 | -45.62259 | 2025-04-09 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46509480-7ffd-3415-bac8-8ec8ff670b77 | -12.41578 | -46.80809 | 2025-04-09 04:27:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f9911c1-14fe-3bc7-b03b-13f4d64ae34f | -10.5421 | -44.67273 | 2025-04-09 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1f4719-0010-33c8-9bb6-3a6c6bb88b5b | -13.67794 | -47.75856 | 2025-04-09 04:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a609d27-6534-389e-b674-95766e211db5 | -10.72702 | -42.31968 | 2025-04-09 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c2082f3-de82-323b-9766-92678cf3dabd | -10.6967 | -46.53336 | 2025-04-09 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a9d6bb0-c035-37e3-a908-92c3e4a5835c | -8.93501 | -44.23106 | 2025-04-09 04:27:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 982d1a7b-236d-39b0-86a1-c83547a1d513 | -9.81763 | -48.0454 | 2025-04-09 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfd4bbd5-0539-3b2d-b20d-473b5f149a9b | -10.71902 | -42.31852 | 2025-04-09 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f1e67fce-94c9-3b46-b558-8281522d4090 | -10.72776 | -42.31446 | 2025-04-09 04:27:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7af9f16d-46ab-3794-94cd-d987a992d525 | -13.01955 | -45.07225 | 2025-04-09 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527df70e-e077-3922-b42c-fea181775082 | -13.02014 | -45.06822 | 2025-04-09 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0083ce6f-58b2-303e-8ab0-b723008a1181 | -10.6279 | -46.41332 | 2025-04-09 04:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d432978-512b-3052-83da-7bfb54ad5cf6 | -13.67738 | -47.7621 | 2025-04-09 04:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb97a9b7-493d-3d4d-a7ea-801dd8170533 | -10.5427 | -44.66879 | 2025-04-09 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
