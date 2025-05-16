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
| a3eb838b-5564-387b-be33-5b15188ec11f | -14.0136 | -55.1321 | 2025-05-16 00:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| ee4afd28-d465-3532-8b72-f69f96c2774c | -11.756 | -38.5168 | 2025-05-16 00:05:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c07cc5de-f1db-3d9f-a049-828d06fe3fb7 | -6.1686 | -48.053501 | 2025-05-16 00:05:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 616e7047-a98c-37c3-96dc-530e89a94cd3 | -11.7899 | -47.378899 | 2025-05-16 00:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 164fb284-c2dc-3722-bb9f-053fcbcd77a0 | -5.7742 | -43.6134 | 2025-05-16 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abe7e306-1393-364a-b500-dbd9a3fc6e45 | -6.6568 | -43.1982 | 2025-05-16 00:05:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8739e4c5-5b13-3ab5-9588-c5293bdb4dd0 | -11.7857 | -47.357101 | 2025-05-16 00:05:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90fe36b4-66b4-3f80-8419-a085e6f86e06 | -14.1774 | -45.489399 | 2025-05-16 00:05:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc351ea3-22ae-3ed4-a405-fe3775657877 | -6.6547 | -43.188599 | 2025-05-16 00:05:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| c18d35f7-94ef-3d93-af19-bc6194cfa613 | -5.784 | -43.611301 | 2025-05-16 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e8635f7-ed68-33a8-942b-5801e8693a12 | -11.7462 | -38.519001 | 2025-05-16 00:05:00 | METOP-C | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 908df462-c9de-3963-a8e5-6fbea0adba6b | -6.1589 | -48.0555 | 2025-05-16 00:05:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f48feb9-cd5e-378c-8a39-a4686a6a7acc | -7.0721 | -44.395 | 2025-05-16 00:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5c547f-7813-3e1c-952d-9d13c97e5e58 | -14.1643 | -45.473701 | 2025-05-16 00:05:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 594479ed-8bca-3c91-99c4-979ae93e4983 | -14.1741 | -45.471699 | 2025-05-16 00:05:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d3e323e-5939-383f-b6b4-df28f0582a1e | -11.7991 | -44.2756 | 2025-05-16 00:05:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 155bb121-66d4-37c1-82ba-d32819411c5c | -11.7964 | -44.262199 | 2025-05-16 00:05:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 255a480e-1750-3978-a696-07b9652a85b2 | -11.5723 | -47.605499 | 2025-05-16 00:05:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14826aa3-d9a6-3057-8a05-2d6b550502ce | -11.7576 | -38.523899 | 2025-05-16 00:05:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ff27a804-6c2b-3f38-8a25-547f37458bf4 | -11.7478 | -38.5261 | 2025-05-16 00:05:00 | METOP-C | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 98c13636-26bd-3f78-a7d7-e87e9c928537 | -14.0136 | -55.1321 | 2025-05-16 00:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ea5447cc-7986-38b6-b788-2a0cabf6ad54 | -14.0328 | -55.13 | 2025-05-16 00:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| b53248cb-ae91-3fb2-9a57-33d01a02c17a | -14.0136 | -55.1321 | 2025-05-16 00:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 21b60d58-3f7e-3bce-90ca-ad6122459108 | -14.0136 | -55.1321 | 2025-05-16 00:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b67bab42-35c9-305d-ac89-a3bb877cc64f | -19.53405 | -43.92275 | 2025-05-16 00:33:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8c71c4f1-de7f-3144-a637-68751d87e835 | -21.23424 | -44.16556 | 2025-05-16 00:33:00 | TERRA_M-M | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9431acf8-53a7-3859-9084-a2247dee84b3 | -17.88523 | -43.9902 | 2025-05-16 00:33:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06b1433e-f603-31fa-a925-439a21995a2a | -17.05454 | -45.91704 | 2025-05-16 00:33:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 985f758e-118d-3eef-a38f-29f66843e490 | -17.05582 | -45.92657 | 2025-05-16 00:33:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 28e14e52-8415-3154-b99e-6d5bab8df2aa | -23.07343 | -50.356 | 2025-05-16 00:33:00 | TERRA_M-M | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| a2628846-add5-3104-b931-55241f47f33c | -19.06017 | -53.45008 | 2025-05-16 00:33:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 56.6 |
| c5f67309-edcf-3147-bdc0-6a6d0a72e101 | -16.58583 | -45.77882 | 2025-05-16 00:35:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30656c57-6edb-33a8-9b52-a3722ed5e192 | -14.16986 | -45.48004 | 2025-05-16 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dc7df46d-6f20-36bf-a76a-84a5e2cb449b | -7.55094 | -45.86996 | 2025-05-16 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d689ef9-0951-3e12-8318-1e67476f3360 | -10.34374 | -47.68019 | 2025-05-16 00:35:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38109fd4-b158-33f5-8839-09f1a2345f0a | -14.17868 | -45.47873 | 2025-05-16 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 96f6efee-990a-30bf-b3c5-9c244b358d67 | -11.42414 | -54.32479 | 2025-05-16 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 7b6e2a3a-ed91-3401-bbd0-6c27e49b379c | -10.50823 | -46.185 | 2025-05-16 00:35:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a033f55-7d8c-329c-9c9c-9c4734f3a623 | -12.07199 | -47.32242 | 2025-05-16 00:35:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a174bdf-28e1-3940-a653-a013b84abcc3 | -6.65804 | -43.20389 | 2025-05-16 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1709dce7-481b-3c62-b6b4-3b1927eb49f9 | -12.31755 | -44.50451 | 2025-05-16 00:35:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b1e02c00-3699-3c33-8996-0ffdcb318044 | -6.62185 | -48.00713 | 2025-05-16 00:35:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bbb7a7d-6628-3b13-9438-94e9682e4ce7 | -14.17743 | -45.46968 | 2025-05-16 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1acf7428-ef88-308e-a867-b03cf2dc12bf | -11.58416 | -47.87223 | 2025-05-16 00:35:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e942ed06-9ff1-3c9b-9c1d-bf5b41e26ecc | -16.03582 | -43.68868 | 2025-05-16 00:35:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d61ec26a-5019-352b-9914-45acd33e367a | -12.31889 | -44.51388 | 2025-05-16 00:35:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9074558c-a482-30e7-b6a3-5dd2c1ee84d1 | -11.79438 | -47.37949 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d4229412-e480-3b17-953c-c6a14f910e55 | -11.78275 | -47.36172 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fd5a755d-a34a-3441-ac8a-e062c883585b | -11.75057 | -38.52403 | 2025-05-16 00:35:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| cb6f3805-ec1d-3074-9024-94a429ab7e78 | -14.86775 | -51.98256 | 2025-05-16 00:35:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9015b785-bb19-3a9c-99e1-0820119f13b6 | -12.16567 | -48.79987 | 2025-05-16 00:35:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c73b9a4-16bc-3a1b-9373-de5cbe38863c | -11.15732 | -48.66881 | 2025-05-16 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 503875ff-2e84-3e50-b407-ce0cd564d6dc | -11.57764 | -47.61379 | 2025-05-16 00:35:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 912386a0-fb77-39c9-9986-eb38eb3bb795 | -12.26167 | -49.31583 | 2025-05-16 00:35:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6397ffc5-110a-39f1-8249-7a109eb96393 | -15.26461 | -51.47238 | 2025-05-16 00:35:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 41.6 |
| be510f3a-937f-36e1-991a-cd8a6dcc0879 | -12.07327 | -47.33195 | 2025-05-16 00:35:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 449a326c-e4ef-3ce3-99ab-3ed11b20385b | -10.34673 | -47.98272 | 2025-05-16 00:35:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cdb0aa1e-aafc-3f0f-9395-27d1343e20c9 | -11.79311 | -47.36998 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d758e915-bff9-372e-900b-264e0023fba8 | -7.07508 | -44.39045 | 2025-05-16 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ad90d3da-73f2-3a0b-93a4-6ecc4c1b83be | -11.10931 | -45.08385 | 2025-05-16 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 33f92c1a-9d4f-356f-a32a-a44ebaafba85 | -9.42006 | -49.3412 | 2025-05-16 00:35:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2473fa8c-86e7-3f9b-8fc9-b0f775a28735 | -6.31912 | -43.75216 | 2025-05-16 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b9fb4516-c004-316d-8215-5a9291a580b0 | -7.7458 | -46.33218 | 2025-05-16 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f28a75b-c5aa-3c8e-bbf4-9b7a31d2f68e | -6.65619 | -43.19141 | 2025-05-16 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 971f80e4-6a9b-32be-925d-e4275ae0ebc3 | -14.17993 | -45.48778 | 2025-05-16 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4109aa91-a935-3ccf-9b27-4522562c75ae | -8.43416 | -46.64258 | 2025-05-16 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e4d5c50-12bd-3c11-92be-5f24b970189a | -15.26557 | -51.46676 | 2025-05-16 00:35:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 42a6e33d-51d6-3a14-bf79-0781e9dfab3e | -11.79566 | -47.38902 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4745a8a6-29c0-3838-ba37-3305c2a82ee2 | -10.02912 | -48.70153 | 2025-05-16 00:35:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da50b168-a71b-33e6-b077-bbe30d5d3880 | -9.30201 | -44.8238 | 2025-05-16 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b371fc7-8a13-3784-adf8-6d0aca99c36d | -13.38602 | -48.44673 | 2025-05-16 00:35:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 02570897-dd01-37de-b536-8fd61427b2bb | -12.34645 | -49.96 | 2025-05-16 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab3f3096-835a-341a-a391-d3b1d8ff8ad4 | -11.58612 | -47.61627 | 2025-05-16 00:35:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f5ac3650-caec-3eb6-80c4-b7544d417987 | -11.63339 | -48.02821 | 2025-05-16 00:35:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 682ba012-521e-3284-b99e-6633a874e8fd | -11.15875 | -48.67955 | 2025-05-16 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9c0f4794-7d05-390d-bf64-d66a988a3b20 | -9.66488 | -47.56052 | 2025-05-16 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 084fc55a-ed36-3a02-b8c7-dee3631abe6e | -16.03444 | -43.67918 | 2025-05-16 00:35:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec3711c6-4fae-3974-9607-ad7b5fb44fa9 | -11.57894 | -47.62346 | 2025-05-16 00:35:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f8db3f5-05b8-3959-bd2d-193d8bfba982 | -11.1106 | -45.09299 | 2025-05-16 00:35:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 53e472dc-b3aa-3710-9d83-b8d776e23132 | -11.42472 | -54.32998 | 2025-05-16 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 5f86f535-986a-34b2-ba28-aafe7df57f3a | -14.02085 | -55.13681 | 2025-05-16 00:35:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| ee61a477-a40e-3abc-9880-be1e3e04cc9c | -14.16861 | -45.47099 | 2025-05-16 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3e48f540-7436-3047-972c-498ee455591d | -12.16714 | -48.81115 | 2025-05-16 00:35:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5b931295-bb57-35e8-baec-54a906194c09 | -14.01091 | -55.1331 | 2025-05-16 00:35:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 0da0b343-db8b-3995-b82f-4de4f5ac0395 | -11.79055 | -47.35096 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 300732c9-d792-38f9-9116-399adb6b6c7e | -9.30337 | -44.8333 | 2025-05-16 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37ddbaed-1e05-3583-943c-51cd7ab26faa | -11.16836 | -48.67822 | 2025-05-16 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| b081265b-6964-3ff2-bdf7-c7b6d1bf815b | -7.5433 | -45.88028 | 2025-05-16 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea718282-dd95-333a-81d0-925e02732e48 | -11.78147 | -47.3522 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a64afcbc-928e-38df-85e5-08916b3985c9 | -11.7957 | -44.27552 | 2025-05-16 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5e3e9aa-9b9c-3c8f-8753-1b6b348be825 | -11.79183 | -47.36047 | 2025-05-16 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9ad5796-08bf-356f-9ef0-187c1177e8f3 | -11.57633 | -47.6041 | 2025-05-16 00:35:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 81cb4e06-2560-303b-9d8b-4246bedd6ed5 | -7.08038 | -44.39387 | 2025-05-16 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cba5b3a3-5582-38cd-88cc-7b64e76012d0 | -9.31246 | -44.83194 | 2025-05-16 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b15a6d8d-1c8d-36f0-b027-f865544877e2 | -12.26231 | -49.30918 | 2025-05-16 00:35:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54779c7c-3b76-3070-ae1f-7000a99a65db | -7.54203 | -45.87124 | 2025-05-16 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e95cda46-e84a-3a10-9ab0-c1b840a028a5 | -5.77731 | -43.62191 | 2025-05-16 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 974706d1-3ef9-3f1c-a5ad-08fae6dbcb86 | -6.17026 | -48.0728 | 2025-05-16 00:37:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bbf889ec-6232-3546-90f6-d28b9b536a72 | -6.16778 | -48.05468 | 2025-05-16 00:37:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b0df361-b58a-34ad-b9ad-923264a39096 | -5.7875 | -43.62041 | 2025-05-16 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README2.md)
