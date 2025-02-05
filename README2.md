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
| 103cde79-90cc-31e6-801e-d393551fd56d | -7.05321 | -44.37978 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45a8d6a8-63d5-32f9-94b5-5f06f25e03e6 | -7.04281 | -44.40806 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e7a1aed-8f94-3301-a7d2-9a0851d30b97 | -7.05793 | -44.38396 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b2f1231-5171-35af-9eed-08a80cd7a5fe | -7.05037 | -44.39603 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ac186bd-67d4-32cd-aab7-de0c15236314 | -9.47734 | -35.92887 | 2025-02-05 03:42:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b89e354b-adc5-35c3-a003-12ff5862c8ee | -7.65803 | -37.28585 | 2025-02-05 03:42:00 | NOAA-21 | TUPARETAMA | PERNAMBUCO | Brasil | 2615904 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9420a69-7ece-393a-9fcb-8938894f5a6f | -10.31181 | -36.61441 | 2025-02-05 03:42:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f499ca50-8967-3739-88d3-fbd04146fc84 | -6.41699 | -35.64959 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0fd640bf-1ee0-3d67-affb-28ccf5458b93 | -9.8524 | -37.2763 | 2025-02-05 03:42:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 071cec83-ceb9-35d3-adfa-edfdff9dcdcd | -5.48168 | -35.81831 | 2025-02-05 03:42:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90a9f9f5-0024-382c-8e8d-a7465e08f2ab | -6.23351 | -42.79484 | 2025-02-05 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 192e55ed-f01b-396e-90be-a47efd3efdab | -7.05849 | -44.38076 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50a4e929-6f22-30cc-9e83-cbba33cbc7f6 | -6.97677 | -42.99313 | 2025-02-05 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ed2e1b8a-ecce-31d8-8864-f1bbd2efdc4e | -5.95065 | -43.36419 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9bffd364-bdf4-334e-803e-71b970138d96 | -7.04397 | -44.40141 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a562f8a3-e4c5-3ffa-82e0-e0b8141b25b3 | -5.48112 | -35.82181 | 2025-02-05 03:42:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6bee23a0-43ef-33b4-9411-de46a8f1304e | -8.11469 | -38.95414 | 2025-02-05 03:42:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a45afa7-3785-3906-bc86-4f410b471e08 | -9.4768 | -35.93235 | 2025-02-05 03:42:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c10a524-423e-35bb-9a33-1ccf1e14be17 | -6.38223 | -43.67102 | 2025-02-05 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7484cabd-3857-300a-ac39-669e77ff8e54 | -6.41368 | -35.64907 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c4726faa-00af-3bd4-930b-721967c58e94 | -7.04455 | -44.39811 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbdb393e-1748-334b-b4a0-c1f51e18328a | -7.05787 | -44.37812 | 2025-02-05 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18e3ece5-de14-3cb4-bf39-2d8894a901d7 | -6.41092 | -35.6451 | 2025-02-05 03:42:00 | NOAA-21 | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d6697893-03a1-3b45-9d48-10721c330fa5 | -8.84987 | -36.51781 | 2025-02-05 03:42:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43cf4cae-fe4c-3b94-9d9c-3896816d4d44 | -11.46955 | -44.95809 | 2025-02-05 03:44:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5bebdee-131d-32e6-ab30-7abe1e84115e | -15.75489 | -42.64845 | 2025-02-05 03:44:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 50f057c6-cd12-312d-a9bd-1e7a72e75072 | -11.95848 | -40.61134 | 2025-02-05 03:44:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a5d6e26-b83f-3bbd-b13f-494f9e3dbf90 | -16.48776 | -39.06951 | 2025-02-05 03:44:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b1cc4cac-5fb8-34e2-bdad-2072ae8b1237 | -16.03836 | -42.1396 | 2025-02-05 03:44:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f5d9a76-720d-3eb6-9c62-75f52e777a10 | -15.64795 | -39.18967 | 2025-02-05 03:44:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9c7d4238-4655-3283-844b-5ea9669d0f5d | -12.87803 | -43.47713 | 2025-02-05 03:44:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1af0316-b04c-320f-b4c6-75436bf276d4 | -11.11953 | -43.3647 | 2025-02-05 03:44:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ea5996a4-b88e-3c00-a573-87b7e8874aaf | -12.65427 | -43.81425 | 2025-02-05 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fc1f258-a8d1-3586-9c72-66d049f24e22 | -10.95051 | -40.73438 | 2025-02-05 03:44:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 51d84233-97c8-31fb-81ee-24ff4e254da4 | -16.68147 | -43.88403 | 2025-02-05 03:44:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a34601a7-65d3-3367-bca4-cbe6bf319ab0 | -12.64965 | -43.8134 | 2025-02-05 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 169ed4c1-04fb-3e5c-a49c-5702b63d6843 | -12.48799 | -43.78941 | 2025-02-05 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f3955b5-3ca9-3322-b33c-a5e364d6fe34 | -16.87318 | -40.69823 | 2025-02-05 03:44:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d5018ef2-b7f4-33ee-8054-ec7eed444c50 | -16.53101 | -39.44406 | 2025-02-05 03:44:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cc3f4d63-f9fe-3644-b6ce-07db29135a5b | -17.38113 | -41.2375 | 2025-02-05 03:44:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b55f673-7c1c-30b1-8709-2ce829956f7f | -12.88041 | -43.47966 | 2025-02-05 03:44:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae738b42-6a40-3cd5-9429-7f14f2fee28c | -10.33914 | -38.02829 | 2025-02-05 03:44:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9d79942-1de6-32e1-a8a9-ad27a8bac78a | -17.14879 | -41.40592 | 2025-02-05 03:44:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b560e664-455b-3846-bffe-baec41627361 | -17.20604 | -40.3283 | 2025-02-05 03:44:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb263c03-a1ba-37fa-a0ec-93dd8b4aa761 | -12.07996 | -37.78242 | 2025-02-05 03:44:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d301614-143f-3002-b94c-06e58d41f73c | -12.64875 | -43.81831 | 2025-02-05 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4df3a68a-2c45-3a73-8c90-a759ebcf34d1 | -12.86092 | -38.36584 | 2025-02-05 03:44:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4bc0c047-0eac-3eac-8dd8-a48070976e23 | -11.12037 | -43.36001 | 2025-02-05 03:44:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 757eda80-a0e9-3bc2-bbc7-cb20a817ddbd | -12.48959 | -43.78738 | 2025-02-05 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06c9b281-1c02-3589-b843-5f7b44a586d0 | -16.86962 | -40.69751 | 2025-02-05 03:44:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cf8abd6a-1d53-3bc5-be11-94944624a71c | -16.3489 | -43.69805 | 2025-02-05 03:44:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5257b12-cf30-3011-a7c8-be0bd6811f8d | -21.88533 | -41.08956 | 2025-02-05 03:46:00 | NOAA-21 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a3f8a01d-6b9b-3e16-b99e-0fff360f5468 | -18.00935 | -41.94518 | 2025-02-05 03:46:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f345fce-98bb-399c-a12d-4cd9f509f59c | -22.90195 | -43.75236 | 2025-02-05 03:46:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a47ff123-6c4d-3d9a-bf57-dce73d1945a4 | -17.71373 | -43.45401 | 2025-02-05 03:46:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b38357da-58ad-35f6-b52c-11835fd74711 | -22.78749 | -43.75793 | 2025-02-05 03:46:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dea16178-8f1c-3cc5-b7d4-7bc79c743985 | -17.96792 | -40.44553 | 2025-02-05 03:46:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ede5b79-60d0-33e8-89ad-060a8c6c2787 | -18.04117 | -39.92426 | 2025-02-05 03:46:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8f71f7d-fd1b-336e-9300-24510626a34e | -19.12549 | -39.73098 | 2025-02-05 03:46:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 922bad80-dcf9-31cc-a697-5a3980f95d8a | -22.67597 | -42.85669 | 2025-02-05 03:46:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 32cc3091-abca-395a-8826-a9f2c3bba827 | -17.82096 | -45.31747 | 2025-02-05 03:46:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7218a9ea-a276-3354-b886-204fdf797f23 | -21.88464 | -41.09362 | 2025-02-05 03:46:00 | NOAA-21 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b19fa0f5-3e9d-3000-abad-ff13f9d209e2 | -27.96796 | -51.63826 | 2025-02-05 03:49:00 | NOAA-21 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3ba33c51-3ea0-31e6-9636-209379740795 | -29.89047 | -51.23238 | 2025-02-05 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 1ea16d6e-8fe0-37d6-b83d-64c80848cb89 | -29.8896 | -51.23599 | 2025-02-05 03:51:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 0b106484-9822-37a8-ae94-b2d15eddd6f2 | -2.8488 | -41.75873 | 2025-02-05 04:06:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96adc2e9-b0e9-34a8-9ee9-eb6946a38848 | -2.85215 | -41.75925 | 2025-02-05 04:06:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d4edfc-5f2c-3087-a6c3-7bc509070f04 | -5.95302 | -43.36314 | 2025-02-05 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f1024f3-fc9f-385f-8037-b7bc89bc72df | -6.38164 | -43.67029 | 2025-02-05 04:08:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d5cf9b1-45db-32d4-8986-3226ce51e6e0 | -7.66789 | -46.09951 | 2025-02-05 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe75a7c9-f83d-375e-a92f-a93a3ca8611e | -5.89547 | -42.21615 | 2025-02-05 04:08:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de7ea1c5-97f5-3311-9edd-441455f0fa30 | -9.47016 | -35.93258 | 2025-02-05 04:08:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 044ec62f-82ec-35d5-91cc-965d6209a8ae | -7.05602 | -44.37838 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6924c6e3-f6ac-3698-acfb-94cc054a1238 | -4.83284 | -38.40734 | 2025-02-05 04:08:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c986564a-9b02-36fe-823b-1e09d630b467 | -5.48211 | -35.82185 | 2025-02-05 04:08:00 | NPP-375D | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 236c91cc-cefa-3b2f-a551-9af1a9557e54 | -7.04994 | -44.39342 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3beda5bd-6d0c-3ecd-a6a2-4e5da6c28c0c | -8.11502 | -38.95412 | 2025-02-05 04:08:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5def73ad-86a1-37f9-93aa-e367e9b58562 | -3.23046 | -40.02251 | 2025-02-05 04:08:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3bea7e3a-08b2-3f28-8e8c-3dacdb4d850e | -9.85204 | -37.27581 | 2025-02-05 04:08:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a803c600-b699-37ba-b9f5-24b842d40c2f | -7.1008 | -44.36983 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed9e2e0-5717-38e5-ad02-706a1805be1c | -5.5868 | -42.92382 | 2025-02-05 04:08:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 60881bb0-5647-3eb5-917f-0a97cbdbd686 | -5.25623 | -45.23937 | 2025-02-05 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0c4948b-d0be-381a-888f-a9d618c4ac8c | -10.69495 | -37.04854 | 2025-02-05 04:08:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ecf27c51-a6b5-3455-86f5-3ebffa02482e | -7.92638 | -41.76034 | 2025-02-05 04:08:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9d988e3-a7ce-3656-981e-c6e77472c007 | -7.04448 | -44.40463 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7047b41-0acb-31b8-9fa6-4940ca7de37d | -7.04383 | -44.40859 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5df913a4-4ea0-3ee3-b659-8f0eb501197e | -7.05539 | -44.38227 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c00292a5-aca0-3c82-af6a-58c5f96e7ac9 | -7.04578 | -44.39674 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79aac08f-f849-30dc-9009-e2a5db191b63 | -8.35758 | -45.18087 | 2025-02-05 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5c5b67d-e851-363b-adef-bcfb7065a8cc | -8.70909 | -36.16044 | 2025-02-05 04:08:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d01c4b4-21c7-3af6-b62c-9a07698c74ab | -8.7085 | -36.16449 | 2025-02-05 04:08:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5749998-48fe-3d6a-b48d-a38b7f18f394 | -7.67171 | -46.10018 | 2025-02-05 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 456c08f2-e49e-3339-b8f4-e9c16cf1ceaa | -6.38225 | -43.66656 | 2025-02-05 04:08:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa80bd23-9426-34a6-b08c-7b414f9c7bb6 | -7.04161 | -44.40005 | 2025-02-05 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05494aa8-8e86-36e9-8573-082a18bf2085 | -4.83643 | -38.40788 | 2025-02-05 04:08:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5919ae0b-5e73-3d74-af4f-fc266683d5c9 | -6.03192 | -46.25846 | 2025-02-05 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df496f6a-0b06-3e9f-a58d-d00406b63a7e | -9.47461 | -35.9332 | 2025-02-05 04:08:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8646d80-758f-3845-9a77-2cc94bb290a9 | -5.62472 | -43.63047 | 2025-02-05 04:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1105586-ab15-3f57-9ea7-257e7f6f546a | -6.97664 | -42.99284 | 2025-02-05 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2db98a4-e3f9-3fea-b153-82f1100d23f8 | -6.98001 | -42.99338 | 2025-02-05 04:08:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
