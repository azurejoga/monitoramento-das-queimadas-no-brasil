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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abfb6fc9-b150-35a1-aac5-576fb1b67c10 | -18.4279 | -54.7129 | 2025-04-03 00:00:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0c8e5f5f-da5e-3b95-b25c-71ad4e48da12 | -18.4283 | -54.6916 | 2025-04-03 00:00:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a8474715-e27b-3644-b456-3d445dbef388 | -20.23728 | -40.67947 | 2025-04-03 00:03:00 | TERRA_M-M | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 95817520-372b-3b92-8265-291bc6504fed | -15.54602 | -42.66554 | 2025-04-03 00:05:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.3 |
| 1d529c3b-cb18-3f33-ace2-b6a20d2106ca | -17.78928 | -42.35364 | 2025-04-03 00:05:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 94a9f4d0-1fbd-3762-b2de-7015056aba91 | -15.54809 | -42.68389 | 2025-04-03 00:05:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| a69f2aa9-68ac-3e43-a4c2-11fed9762cff | -17.01128 | -40.74616 | 2025-04-03 00:05:00 | TERRA_M-M | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 17ad6c11-5340-3f83-b425-be9f3a6819f0 | -9.32712 | -37.01394 | 2025-04-03 00:05:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 75506938-237e-32aa-b779-3fc220c26ccd | -9.82601 | -40.57956 | 2025-04-03 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 95e3d4d9-fee7-356e-b772-f32ea43767ec | -9.82463 | -40.56914 | 2025-04-03 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 98989464-443b-3d24-8903-075dbccc7721 | -13.03699 | -45.08057 | 2025-04-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d6ca8445-c403-3ac8-8a26-988bfafb59e3 | -12.26015 | -42.09947 | 2025-04-03 00:05:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 335e8354-f697-3273-ae7a-cf505ffdb174 | -13.03983 | -45.10552 | 2025-04-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c7f2ccf5-d129-385f-b28d-1517006527ba | -11.27694 | -40.98244 | 2025-04-03 00:05:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 3ba701e1-a3eb-3fd1-9656-39f7123b4f72 | -12.25852 | -42.10576 | 2025-04-03 00:05:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b98aeb52-dd92-3ea1-94e2-521811ca8142 | -6.96847 | -43.01918 | 2025-04-03 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 593ea00d-e88e-3a1e-896a-ed934d1653f4 | -18.4283 | -54.6916 | 2025-04-03 00:10:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6956d827-a058-3a5e-9460-13eee0fdfe3e | -18.4279 | -54.7129 | 2025-04-03 00:10:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2e7a22ca-b452-3fc6-ac7b-d606a0195cf1 | -18.4283 | -54.6916 | 2025-04-03 00:30:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1d2e77d5-05e1-3c0b-a213-6db273719643 | -18.4279 | -54.7129 | 2025-04-03 00:30:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d3e57a9c-58ad-3975-9b8c-ddbfd3b0b42e | -18.4279 | -54.7129 | 2025-04-03 00:50:00 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7db0e46d-3de0-386c-9667-8ab115b4dfa0 | -6.235 | -48.0674 | 2025-04-03 01:00:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 84210be1-c8c7-3545-ba93-afd8f458a8b0 | -6.2352 | -48.0456 | 2025-04-03 01:00:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| df17a9d8-6f88-3bf6-8cf5-6923008e7e12 | -6.2352 | -48.0456 | 2025-04-03 01:10:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 9a06eb6e-32e6-3a5d-807c-46e14dc7d77c | -6.235 | -48.0674 | 2025-04-03 01:10:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2bb11403-8819-3b37-aef5-c235cf2148eb | -6.235 | -48.0674 | 2025-04-03 01:20:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e0293edf-6a3e-38f6-87ed-069fb8247c79 | -6.2352 | -48.0456 | 2025-04-03 01:20:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f986becf-46dc-31db-9b4d-33e9e1892a94 | -6.2352 | -48.0456 | 2025-04-03 01:30:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d7c27029-3d88-33e5-9ff4-01406669beac | -6.235 | -48.0674 | 2025-04-03 01:30:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 02e8611e-0b04-3177-9af7-e8dc43a7ac00 | -6.2352 | -48.0456 | 2025-04-03 01:40:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e016363d-764b-3365-9cc0-c4ff416f9a91 | -6.235 | -48.0674 | 2025-04-03 01:40:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 49df60dd-a6c6-3c04-9358-4ee161ec79dc | -18.43472 | -54.71049 | 2025-04-03 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 39.6 |
| dcf4a938-de20-3a5b-91bd-a3fa32adb918 | -18.43733 | -54.70406 | 2025-04-03 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 93985e85-aca6-3262-a567-b696ff388ef1 | -18.4251 | -54.70642 | 2025-04-03 01:41:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 48ebbf9f-4051-35cf-95c0-b8226bce3508 | -12.27946 | -63.80159 | 2025-04-03 01:43:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df3e7f75-6504-3299-a1a5-70b53bb86bfa | -6.2352 | -48.0456 | 2025-04-03 01:50:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1f2bf148-e10a-368e-9336-493be7c4803f | -6.235 | -48.0674 | 2025-04-03 01:50:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e8c61f76-c40f-3c97-86c9-c3966b32fd14 | -6.2352 | -48.0456 | 2025-04-03 02:00:00 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| be0705fc-ce79-364a-a909-33a377c1af5e | -8.86584 | -37.28798 | 2025-04-03 02:58:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.2 |
| c489e82d-85f3-3715-80a1-c3be8f948554 | -9.37352 | -37.17896 | 2025-04-03 02:58:00 | NPP-375D | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b6fa696e-b84e-3609-ad08-863a966a65f8 | -7.23019 | -35.59539 | 2025-04-03 02:58:00 | NPP-375D | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13232035-0c9d-3285-87d2-cc6cf681dfa0 | -10.7513 | -38.01566 | 2025-04-03 03:00:00 | NPP-375D | POÇO VERDE | SERGIPE | Brasil | 2805505 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ce8cf37-f10e-3b9d-a172-e1ca508ba99b | -12.45959 | -39.7703 | 2025-04-03 03:00:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d1e5a4f-bef4-3839-ae24-a6302846d221 | -14.10431 | -40.38516 | 2025-04-03 03:00:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d00a62ff-5cb4-35a3-a02c-39e9ad6cd544 | -9.8063 | -38.99697 | 2025-04-03 03:00:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df22aac1-0ea0-3467-9053-2c8e7d382f2f | -11.44493 | -38.34979 | 2025-04-03 03:00:00 | NPP-375D | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b19b4212-d217-3d01-b193-d6e246713694 | -16.27096 | -39.13787 | 2025-04-03 03:02:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 845d70b7-47ff-3f18-926b-7dffae8ad082 | -17.61522 | -41.17682 | 2025-04-03 03:02:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65455255-0654-3625-a845-77b2f4dce59d | -21.13375 | -41.45515 | 2025-04-03 03:02:00 | NPP-375D | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fd8b28f3-f210-3b91-8291-148a995d4095 | -17.63961 | -39.34366 | 2025-04-03 03:02:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4fdf36d1-3ed7-3035-8a17-3db57cc202a4 | -17.82235 | -39.4302 | 2025-04-03 03:02:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8647ff10-41ef-3c49-aad3-d93e3650d8a8 | -7.47425 | -34.84276 | 2025-04-03 03:19:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b26d5ab7-99e8-3940-824a-d82380137bf2 | -7.47534 | -34.84417 | 2025-04-03 03:19:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5fcf5849-f4fe-3aca-8f25-707eb8a3d76c | -7.22513 | -35.79053 | 2025-04-03 03:19:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4bfe850f-314d-327c-824a-0c04d051adc5 | -8.07182 | -34.97723 | 2025-04-03 03:19:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6f61bcf3-ffbc-3852-8d65-a008756da3f0 | -7.2298 | -35.59283 | 2025-04-03 03:19:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58b9bdc7-8960-3262-8656-d9937a82077a | -13.03234 | -45.09461 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21c0799b-e8ad-31f5-b777-3f803803478d | -9.16472 | -40.97205 | 2025-04-03 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1946e560-61c1-33bd-977d-8e7a42bd4c31 | -9.9154 | -37.08749 | 2025-04-03 03:21:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 72377aa6-6ec5-3146-ba22-012789e6f9a4 | -13.03302 | -45.10035 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c947c44-8684-3db5-8304-8430fc58a841 | -13.03103 | -45.10088 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aba0b44d-043b-3507-8314-4e4c76bcde5e | -9.82317 | -40.57492 | 2025-04-03 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db9aa91a-661a-38f8-9852-44cf6506057b | -10.75059 | -38.01535 | 2025-04-03 03:21:00 | NOAA-20 | POÇO VERDE | SERGIPE | Brasil | 2805505 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1749a665-9337-3fe9-8a37-18cadc876a4d | -13.03571 | -45.08786 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bee42eab-eb38-357e-84cd-46e52fc7baed | -11.78744 | -40.9314 | 2025-04-03 03:21:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7cd2c614-de53-3e91-91a1-7d99ae5cd0c0 | -10.69407 | -37.05016 | 2025-04-03 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d5b76f9-cb71-3fdf-8934-adccf2cffb38 | -10.65699 | -37.40533 | 2025-04-03 03:21:00 | NOAA-20 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 18a3c460-ca65-3119-b1b6-757fc7fac428 | -13.03437 | -45.09409 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52497f64-bb36-31f6-8798-80a282612f65 | -13.03365 | -45.08835 | 2025-04-03 03:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5dc88f8f-d31c-3f13-8912-e2018b13142c | -9.9178 | -37.08645 | 2025-04-03 03:21:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0e8a000f-d93f-31eb-bb7a-43e77dcd0b71 | -19.7176 | -40.35342 | 2025-04-03 03:23:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d568fc55-bcb0-3c02-9096-edf28ff945c3 | -15.8059 | -43.57298 | 2025-04-03 03:23:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f163bb56-0ced-3f4d-b20b-15680c6ecd01 | -20.16035 | -47.32274 | 2025-04-03 03:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82379370-daa6-3676-9be7-fab1426496d8 | -20.15556 | -47.32164 | 2025-04-03 03:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6cab027-e6c5-3d31-9722-103bad260c0d | -20.16226 | -47.32328 | 2025-04-03 03:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14a7db0f-c08d-382d-a685-44eab1267f82 | -17.74664 | -42.89412 | 2025-04-03 03:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cfda662-c4eb-3235-b800-6cdfe98e47ab | -15.80683 | -43.56856 | 2025-04-03 03:23:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6c2805fa-9110-38fd-8ffc-46327235ae78 | -18.03824 | -39.92608 | 2025-04-03 03:23:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27c0875e-2700-3563-8af1-e80c260a550b | -20.15879 | -47.32926 | 2025-04-03 03:23:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83b06910-0592-3572-9eab-3063e3831c1d | -17.75211 | -42.89516 | 2025-04-03 03:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86513062-8cff-3d17-82ce-b3b9b573bf22 | -17.47058 | -39.26749 | 2025-04-03 03:23:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b16e586b-436e-3c2a-a267-825684c0e71e | -22.89962 | -43.75106 | 2025-04-03 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 36de52f2-5e5a-3db4-a977-a8453120c6ad | -21.62397 | -43.46544 | 2025-04-03 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6261132b-19d6-34c0-a32f-72a6acbd1fd7 | -22.96069 | -43.59706 | 2025-04-03 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60ec6785-0bd3-3595-9fbc-b9feb9b4e5be | -3.95482 | -41.48727 | 2025-04-03 04:12:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0fe15c14-fabd-3de2-97e8-7cbcbe32bfb7 | -6.97105 | -43.01641 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a5c108c-a5f4-3779-9c82-0e9274bac4a0 | -7.2247 | -35.79206 | 2025-04-03 04:14:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2166b491-cf40-3b42-b5e4-7dbb9f657368 | -8.90307 | -50.04464 | 2025-04-03 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d9e1356-d811-30a3-9a43-d066e913ef88 | -6.9579 | -43.03557 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4b9239bc-961c-36d8-a925-5757fd12775d | -10.66803 | -44.40527 | 2025-04-03 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 367b6da4-6df5-34db-8ea8-1ad9490d262a | -11.02085 | -45.2461 | 2025-04-03 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a4d8769-b0a7-3baf-b479-badf3be1f612 | -6.31886 | -43.8362 | 2025-04-03 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8e20265-62ca-3e39-ad54-1fc2c4b3754b | -8.17256 | -42.92137 | 2025-04-03 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3de34a1-a7be-30b6-bfb7-40bf332ad7be | -6.01391 | -43.87038 | 2025-04-03 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5e0b663a-98e1-3188-a430-269fa04c08d3 | -10.35136 | -44.83718 | 2025-04-03 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f33f6461-4f58-3a99-9262-9d68c5099998 | -8.72806 | -44.02465 | 2025-04-03 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb3d326e-ebdd-3363-9256-4922e4c8fec0 | -11.29306 | -41.86081 | 2025-04-03 04:14:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0bfd57d-b263-33e6-abf9-269c5953a04f | -6.23215 | -48.05238 | 2025-04-03 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| beaa776d-6103-3eb1-a09d-c8c4b3a361c6 | -6.95128 | -43.03458 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9677fa00-a9d6-36b4-8c61-7f899bb50373 | -9.16487 | -40.9696 | 2025-04-03 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README2.md)
