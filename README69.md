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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6f38d1a-168c-393d-ad4f-287ad6c58967 | -11.77991 | -45.58869 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3080985c-3490-339d-b3f8-ae19e305f9a4 | -11.99676 | -43.46458 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa323433-25b4-328c-8811-420f50a59832 | -9.91249 | -44.79128 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cec09305-1ecb-349a-ab7c-83ef49a192b1 | -8.90103 | -45.22475 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3d59379e-a8e0-3256-986d-29365bb9b106 | -11.00859 | -45.42157 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3d4f5899-771c-3309-b4ba-bf00cbe8139f | -10.91011 | -45.52582 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e78bd2b2-9f9e-3ade-88f7-e2aff6da4661 | -6.96424 | -45.25631 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10fba496-e8a4-313d-bd20-6018ef094367 | -10.57398 | -46.2925 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56329bbd-bda8-3f74-ae84-9e70064aea8b | -7.50214 | -45.76573 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45b01637-2f8b-3a64-92ac-17e4cf1cad08 | -13.16112 | -43.28325 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| cb56792f-eedb-3476-8129-89701233b36d | -8.96387 | -45.1515 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8b78926-8918-3d71-a1d2-e76d3263318c | -12.00837 | -43.45791 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c054ecc9-2754-30d9-b495-5222b32741b7 | -11.23802 | -44.87709 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 908c8dd9-0cfb-3239-bd21-5deea7661f8f | -11.64184 | -43.70695 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| deb3ce00-57d8-3b2d-a858-77ed9f2e1cca | -11.75735 | -44.95533 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef26592b-d10c-3735-ad6b-bb82946a9ba3 | -10.90433 | -45.52451 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57f98fe5-9946-3824-8729-ad729f61cbc0 | -11.06273 | -44.08277 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcd75efe-4f8b-3e1e-a2f7-684a334e69ac | -11.41752 | -47.58386 | 2026-10-09 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 728895c8-7ac7-30a3-b31f-bc38465dc755 | -11.24545 | -46.2937 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6996f1ec-7245-3704-851f-663b5bad4057 | -8.95874 | -45.17861 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4b28179-f4ea-39b3-961b-0597c796c10c | -11.20835 | -45.25909 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4c71c71-53cd-3b96-845f-d2ece4f39bdc | -9.3478 | -46.57991 | 2026-10-09 03:45:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19f5dab9-725c-375b-abe0-31e81a2d14f2 | -13.81892 | -39.90413 | 2026-10-09 03:45:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 979dd423-5330-3cb8-8718-44d8f8ad825b | -11.21478 | -45.2564 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc242477-6b79-355c-9687-21316ff9e51f | -11.83859 | -43.59005 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2bc044b-cd8c-3ca5-8eb9-1a5a920a7b35 | -11.75024 | -44.93261 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c73a0ea-b0d0-3a99-b5d7-e8de613359e2 | -12.00399 | -43.45365 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff2b2a3-970e-3012-b208-68a1ad4188a5 | -11.25244 | -45.25475 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da3bafd4-882b-3ded-9b97-3fee1afc88f4 | -7.40327 | -44.76403 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8aa00923-b485-34e6-b6ac-1df88ae5944a | -15.3864 | -41.8941 | 2026-10-09 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d3166e85-0a38-3e98-b933-e306414038f4 | -15.24976 | -42.36847 | 2026-10-09 03:47:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ed59ba99-05db-3e8e-b3fa-7c3385cd20ce | -15.44276 | -45.44412 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a595b21f-128a-3fe5-ab1f-460f7262672b | -17.7157 | -39.74891 | 2026-10-09 03:47:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 124fdc5c-3c86-3ea5-af4a-90220a945e2e | -15.49366 | -44.41354 | 2026-10-09 03:47:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 76aaa006-44f0-3ae8-bbcc-082a71fc8012 | -16.58634 | -46.76221 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d804b493-1332-3b81-a8f3-f0cd88475de7 | -15.78138 | -44.68606 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2231c43-2b68-3aea-be96-013b199ba6ed | -18.47645 | -42.24861 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b79c38f9-51f7-331d-a958-609a19e018f4 | -15.42954 | -43.24479 | 2026-10-09 03:47:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bdcd6280-64d5-3e82-b137-31c92f087f43 | -19.32266 | -44.02065 | 2026-10-09 03:47:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f291514-0a63-3fb6-89af-50610f1a8d3b | -15.56121 | -44.51616 | 2026-10-09 03:47:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b444e5bb-428a-30c3-81fb-18d591953c8a | -16.12309 | -43.75564 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e69cfc4-dfef-33df-8e31-0fe99dcac2c5 | -16.12273 | -43.75272 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a2ac050-b926-3c8e-aa3d-10e9e99d4b03 | -15.10304 | -43.63443 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| adbb73f3-d613-3c42-b6e4-933bdea5f5ce | -18.78604 | -46.4724 | 2026-10-09 03:47:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1029c517-5410-3e3b-a15a-368fe8c018f5 | -19.99342 | -49.0927 | 2026-10-09 03:47:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d2b7338-c928-3e0e-877e-9bffbc487cc4 | -15.95085 | -41.08558 | 2026-10-09 03:47:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7db60070-abe7-3d2e-a7eb-21c69713fd1b | -15.44878 | -45.4419 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 617c8746-255c-3136-af45-4fd431d5c3bc | -18.08346 | -42.26811 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| cf70bb14-98a7-3571-b45f-0805cd8d7d30 | -14.93921 | -48.10321 | 2026-10-09 03:47:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c019712-bd84-3264-840d-b98f1751a282 | -17.15411 | -46.12626 | 2026-10-09 03:47:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ed15131-d2d9-32a0-b620-dfcf388e9461 | -14.73645 | -48.22707 | 2026-10-09 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fc23b15-bea5-362d-a9e2-7a6940cdde70 | -18.05077 | -44.5633 | 2026-10-09 03:47:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9867f741-b489-3b70-8dbd-328d44ee9440 | -15.78582 | -44.69019 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf8511d4-a653-3585-a619-d500b73e1978 | -19.32243 | -44.0179 | 2026-10-09 03:47:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bc5bb46-0a10-3926-abb2-45ed5f5d4b21 | -15.38576 | -41.89315 | 2026-10-09 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 00bc6271-795e-3937-a901-e6a67bd7c057 | -17.97045 | -44.34904 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2053437f-0cc2-32b3-b8ec-66e52877b8d2 | -15.63522 | -39.18436 | 2026-10-09 03:47:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e43d9574-5d5e-38aa-b40c-7faed49b6a08 | -14.87495 | -50.2993 | 2026-10-09 03:47:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c358508d-24cf-33d3-b946-6771bf42b4ff | -15.93801 | -40.72845 | 2026-10-09 03:47:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1e7c1469-aaf5-3df5-98a2-9a8cfd9b3ace | -18.63867 | -41.35055 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4d3615b2-817e-38ae-8b37-15ac02752c47 | -18.63574 | -41.34293 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 160247e5-485b-3b31-86c6-8d2f61aacd6a | -18.32808 | -42.37841 | 2026-10-09 03:47:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| fb9aea3b-e737-38e3-964e-470bf233122f | -14.99433 | -44.06062 | 2026-10-09 03:47:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 83c50579-a5a2-3118-b0ce-04ec530db711 | -18.63963 | -41.3454 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2b05eaac-7808-3605-a9a3-8f57dde68df4 | -16.58065 | -46.76109 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dec43b5-ae0f-3bed-bb1e-b4382552d66e | -15.98635 | -44.85439 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ed81ca5-b08c-3989-9fd4-2b93d64a6587 | -15.255 | -42.36476 | 2026-10-09 03:47:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| dee66d3e-5091-3868-ba6f-acecce79263e | -16.88039 | -40.71489 | 2026-10-09 03:47:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 81d36ac1-8cf4-38ee-a0c3-a707a9722a72 | -18.08763 | -42.2688 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4328f9c5-6eb0-32ca-8141-ee98fbe822f4 | -15.95487 | -41.0862 | 2026-10-09 03:47:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6b44eee9-8ed3-3d15-87aa-d58176960bcc | -15.44592 | -45.44165 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb94353d-e946-3b58-a2c9-647d296a1091 | -17.93594 | -43.95559 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2090ebca-1a78-3306-9861-bab6f466c9ff | -15.93408 | -40.72786 | 2026-10-09 03:47:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 202c5a9a-43b1-3ce6-88ca-b1b58f50a389 | -17.36258 | -48.17917 | 2026-10-09 03:47:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d6f46a9-c62d-3e8f-a656-aa450df709fd | -18.63386 | -41.35331 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 2757469a-9782-3c74-803b-da50004bba9f | -15.10201 | -43.63977 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6e2bc719-a2f2-3b80-bee5-72f2f46d10d7 | -18.63091 | -41.34735 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 26162cb4-8c3f-331c-8885-da0928da8e80 | -15.63956 | -39.18074 | 2026-10-09 03:47:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ee78374-b8d3-3b6e-886f-fcaed2d6b342 | -17.51334 | -43.67651 | 2026-10-09 03:47:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf6beb03-9ada-34b1-bbec-17af5e661bd9 | -14.73 | -48.226 | 2026-10-09 03:47:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f63fda9-0559-3cba-ac04-1c5fc9f92d11 | -19.42163 | -44.47294 | 2026-10-09 03:47:00 | NOAA-20 | INHAÚMA | MINAS GERAIS | Brasil | 3131000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a882e6bd-26d5-3b60-a33d-fe709112eeaa | -16.12439 | -43.7491 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc54f50-c7c3-3cc7-8f84-ff1f2abb97e1 | -16.88129 | -40.70982 | 2026-10-09 03:47:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9abdb9c8-6502-3f9b-a281-d38ae082ceef | -18.05734 | -44.60498 | 2026-10-09 03:47:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| beab622c-5603-32b9-a9cf-35ac7f9044dd | -17.51427 | -43.67175 | 2026-10-09 03:47:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79ff6dca-93c6-3bbb-97c7-56780fc9fd10 | -15.63595 | -39.1801 | 2026-10-09 03:47:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2545b03-7fd5-3ca7-bbb5-572f35410edf | -17.93697 | -43.95982 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92b6a61-2a17-39d4-bacb-ae7d130c504d | -17.20573 | -40.81262 | 2026-10-09 03:47:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b323796f-5fb9-307b-aaf4-a07fc5c089e6 | -15.38716 | -41.88989 | 2026-10-09 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b637b474-5935-35de-b49a-5e3d750b54fb | -16.58267 | -46.76126 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd7f9ca-bfe8-3e31-b06c-a6af33cbdcde | -14.87325 | -50.30672 | 2026-10-09 03:47:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09112f1c-3fb6-3e10-b691-eab39b558bb0 | -15.44346 | -45.44072 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 494fd3fc-4f48-3c07-b95e-61c4a37ec72b | -17.15246 | -46.12532 | 2026-10-09 03:47:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07837e07-4e1b-3b31-bc04-d5ab9f5e07d3 | -15.42493 | -43.24382 | 2026-10-09 03:47:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dc262aae-dd31-3a0e-9007-3590a2ce91e7 | -17.97021 | -44.34816 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e096cad-cc5c-39cb-880c-e48f0857a3a1 | -16.93208 | -42.10715 | 2026-10-09 03:47:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ef5de766-5fe3-3101-b21b-86b1d1054524 | -15.44525 | -45.44503 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c778c915-655f-3f39-9132-322f8300cb40 | -15.25417 | -42.36916 | 2026-10-09 03:47:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a1dc8d85-6e6b-3de6-87c2-3811d670c3a0 | -18.64252 | -41.35149 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b0a59a4-5294-3561-a3bb-690a0be68a23 | -16.99099 | -41.17492 | 2026-10-09 03:47:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |


[Clique aqui para ver as próximas entradas](README70.md)
