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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71a1f704-e78a-3d5a-80a2-e90f391819e7 | -8.45978 | -44.19363 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 491c5ba4-9cde-3a5d-81a5-eda81a19a7cd | -9.32556 | -46.95808 | 2025-10-15 04:06:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5de82065-12ae-37ec-a109-97be4a94197e | -4.6535 | -43.12288 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86944011-c764-3f16-8d37-637399b5e954 | -5.98335 | -42.88148 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d23e0f62-16e8-3843-8ad1-493330f87af0 | -6.43338 | -41.70531 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b67f446e-e12c-3b47-84fc-0075938dd885 | -3.42564 | -50.25206 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a41e441-9eaf-38f0-a970-a7cb39c5b6fb | -6.17295 | -42.61497 | 2025-10-15 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 901ccd09-71c5-34fb-bcfa-bf1093315b3e | -8.18468 | -44.03515 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 353b863b-3f07-372b-af11-9368fc7c856c | -8.18532 | -44.03129 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ed00f9-a4cd-380e-b8f5-f6e20c4e1eb6 | -4.90394 | -41.55835 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c08ab75f-ba5c-3375-af41-fdb5e4235c6f | -6.56057 | -43.92345 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 263eb963-9191-33c4-9f9d-ea645c0a0f2f | -4.83606 | -42.77242 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0450f867-0ba0-311d-85b9-c773e6d2e981 | -8.21392 | -43.31857 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 572ab52d-050b-3fe9-8e6d-f3f5907b9002 | -7.94392 | -44.13225 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08f8de9c-c680-32c9-a024-8537a3d74f7e | -5.82777 | -42.32613 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8880c48-277f-3900-9514-8247567b5c94 | -5.2639 | -43.22927 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e189e94-ffc9-3d6e-8fc9-14bbe831db92 | -5.02849 | -45.01489 | 2025-10-15 04:06:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfacef60-bd5d-309a-b55f-9190ba0ce67f | -6.02188 | -43.40141 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e209d38-2f87-3e13-9529-1e9fe4a60601 | -2.92136 | -48.30161 | 2025-10-15 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 410a9b3f-e692-34a8-af20-2bc67ff43feb | -5.41302 | -44.21983 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f715e70d-2ad8-3bed-8004-90b5c3037dc4 | -3.08403 | -47.72869 | 2025-10-15 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 54bfb286-f4ff-3d5e-8bfd-420a94026ab9 | -4.91609 | -41.54604 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e19887b-8ca0-3ee4-9ab0-fd72a7334e14 | -7.17168 | -42.19083 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81aa5826-578c-3bbe-aa55-23302c71f9d6 | -6.45615 | -46.21162 | 2025-10-15 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3caa6bf-3f38-3faa-b9f0-4319bed6cd94 | -6.92313 | -41.37959 | 2025-10-15 04:06:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b04fb886-2747-371b-a578-f6aeaae2d1e9 | -8.21623 | -43.39024 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0249548f-8864-31bf-b099-bb1ebbf9bac3 | -5.40368 | -40.89123 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93a1874f-61cc-3ac3-ae89-51c13844e156 | -8.25041 | -43.35083 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 72a61850-df80-3eb3-851a-ef3ade5c1609 | -6.45823 | -44.58665 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f636632b-59ea-32cc-880e-5edfbc1ee103 | -4.92105 | -41.53615 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4d79ba8-8d77-3eee-b646-1c7a3f298407 | -14.12067 | -42.64899 | 2025-10-15 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1bd01683-36a5-3284-a835-8c276b45a273 | -10.49047 | -44.41691 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1019f4c8-621e-3d0b-a02f-3706d3d8c97b | -10.34341 | -46.51527 | 2025-10-15 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0cb4834-0acc-3785-9df9-6694de16b6e7 | -10.05473 | -48.18173 | 2025-10-15 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 392cd33f-ad21-304a-82fe-c790e1f49af3 | -13.38835 | -42.70754 | 2025-10-15 04:08:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 87474f2c-d8de-37d2-bf2f-9c6c5b8a7fd6 | -11.77673 | -43.73848 | 2025-10-15 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a96b886-7681-375f-b0cc-e7746ffb12d2 | -10.34422 | -46.51044 | 2025-10-15 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f3ebbbb9-fa09-3af8-80e1-335c49db5bb0 | -13.21075 | -40.46316 | 2025-10-15 04:08:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 680b10d7-4ec0-3b78-83da-66a33242853c | -13.79666 | -42.7012 | 2025-10-15 04:08:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06a757ff-2267-3e04-89f6-6610cb1b6e7e | -10.13585 | -44.55427 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e982307-bad7-3e9c-8591-5aa1618e2a39 | -10.14061 | -44.54699 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be5f887a-f837-30dd-b0fd-d047c5ce05c3 | -11.23156 | -39.23742 | 2025-10-15 04:08:00 | NOAA-20 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42c5c5b8-dcc7-3bfa-afb4-68519f394c05 | -12.24502 | -50.39343 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 084419b5-da66-3d06-b4b3-d0c204099da4 | -14.54376 | -41.54182 | 2025-10-15 04:08:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 270c3dd6-e18f-32b7-89af-aacdccdf4159 | -10.04378 | -43.82808 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19e38e47-5d94-3608-984d-e219aa9cdcfc | -13.4791 | -43.69669 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a44b9933-6b79-39fe-a780-481e05225938 | -13.38987 | -43.65956 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5692482-d02f-3908-9e36-36e80442ac6d | -12.63664 | -42.39035 | 2025-10-15 04:08:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4addddfc-038f-3e75-8464-f06f74bf4a77 | -10.51807 | -43.36499 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15aa6d57-ab3a-30e2-a3cd-294b4ed91c35 | -14.64872 | -42.76747 | 2025-10-15 04:08:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aea23d50-b7f7-3da3-b5a7-14efdbee8188 | -9.88429 | -49.31399 | 2025-10-15 04:08:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 751928e7-1257-3f08-8783-ec44df9ada9f | -10.04656 | -43.83235 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b058829b-2d31-32d4-8b11-6366cbdfb0d0 | -12.24882 | -50.39967 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa7fe992-4fee-3499-bd9a-a8ca82a4b575 | -10.04243 | -43.83215 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552ab1ba-b7c3-3147-beec-ddc256d0125c | -14.38097 | -42.30614 | 2025-10-15 04:08:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45610f1f-3ed1-3556-b764-e113467c878d | -17.20249 | -46.93055 | 2025-10-15 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f03bbea4-f721-30d2-bc47-8cdfa716b4c6 | -12.25164 | -50.41122 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80e3be20-bcf3-32bb-916e-8e744196bdcd | -12.03622 | -44.02292 | 2025-10-15 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6aa402b-5fb0-3d01-984a-1b6b55d74fd5 | -13.34222 | -43.74332 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a2ae8bf-a8d1-3cf3-ade2-0eaf94cbe3e2 | -11.78066 | -43.73542 | 2025-10-15 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af82d2d8-4057-3ea6-b803-75e263b3070c | -10.56302 | -43.71704 | 2025-10-15 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66cae212-9b74-3327-afcc-f77b0d6c5d13 | -12.19729 | -50.38403 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b3d183a-22b4-34af-8f44-1a7a9cb3ec19 | -13.92816 | -42.55564 | 2025-10-15 04:08:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f6832ef9-8885-34bb-940d-71e2f4d73df1 | -10.04317 | -43.83179 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 967dbb0a-7e5f-3298-8b05-8d20ea49dc27 | -13.41188 | -43.69258 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 225c6b3d-5c6a-3768-9493-80a668b1d6f8 | -10.04362 | -43.82474 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ccbac4-5d7b-3974-9122-d662c77586d6 | -12.22775 | -50.4065 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f2605e-54bd-3441-9904-9cdf6d79ba06 | -10.04303 | -43.82844 | 2025-10-15 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64012214-1e2f-3c87-997c-85785fd8f527 | -14.83557 | -40.98584 | 2025-10-15 04:08:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 73c8fa67-8c0b-3d57-9bde-b8dc1957e478 | -12.221 | -50.41617 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ed31a36-6bfd-348a-bd37-01b56a0688aa | -13.87924 | -45.53566 | 2025-10-15 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2425f11-67b1-3751-a508-e909e2abe927 | -9.81413 | -47.63887 | 2025-10-15 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9af13aab-4e89-3642-8371-9917a6093ec9 | -13.92712 | -42.38761 | 2025-10-15 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5430eba6-c2e9-3887-9ae0-917e7a55ce93 | -12.23352 | -50.40213 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf5ff22a-bd41-3943-95a4-69926a1c9875 | -10.13997 | -44.55093 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4f41832-e911-3829-a4e5-7a330bdef820 | -14.41803 | -43.98606 | 2025-10-15 04:08:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c19abfb-98c3-3dbd-8ed8-4c2cf380a664 | -12.24491 | -50.42088 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09976347-f8f3-3721-ae8d-dc38adabebc7 | -13.16477 | -42.50825 | 2025-10-15 04:08:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd5c1bf5-52e1-3095-a6e9-5f1cc67f0934 | -10.51358 | -43.37154 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 936ba349-3042-3145-b7d9-94cf65b1586a | -13.47072 | -43.70629 | 2025-10-15 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f98c87f-5ec7-3159-b626-c0bf1cd6c54d | -11.05867 | -47.59281 | 2025-10-15 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ba150a1-d12a-3790-ba91-65da5803a302 | -11.8563 | -47.1371 | 2025-10-15 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eeb7fb3-5aa7-31ef-a239-42e62124f634 | -11.84615 | -47.91994 | 2025-10-15 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbd05f76-cbd6-329a-ac12-986a3c3cd3e1 | -10.34038 | -46.50981 | 2025-10-15 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10242869-8703-3e9c-929b-016d0c185553 | -12.23731 | -50.40838 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 61b79124-b332-338a-b593-ef60672697a7 | -12.17401 | -45.0626 | 2025-10-15 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e7ec29c-6543-341b-9df5-fb628840f305 | -11.88338 | -44.78257 | 2025-10-15 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ec5560f-b00c-32ca-9a81-161861f7af20 | -12.25545 | -50.41747 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee6e027a-75b7-39a7-bd8c-deeec3402240 | -10.75122 | -42.73545 | 2025-10-15 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ea12299-160f-3eb7-aaef-5ba7bce5ae4e | -12.24013 | -50.41994 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46a6b66e-6d45-3fac-8a9b-8f6fb510eb8b | -10.19124 | -42.43304 | 2025-10-15 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 621103f3-b55a-3822-b9e4-97ceac91dfed | -12.24025 | -50.39249 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 729eee93-bc91-34bb-bebe-d9d451874b4a | -14.11681 | -42.652 | 2025-10-15 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5a572b83-b0ca-3d0c-95e5-a60dd46ce541 | -12.20188 | -50.41239 | 2025-10-15 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b27738b3-7e25-3d57-9f8f-01a88c89dc0a | -13.66015 | -40.35351 | 2025-10-15 04:08:00 | NOAA-20 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| df9f4c96-2a04-3849-9a42-ee203ea6c766 | -13.93542 | -42.35604 | 2025-10-15 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90926b0c-2275-3b5f-973c-ec8226f53fac | -11.88757 | -44.62968 | 2025-10-15 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35dccc6e-8b5f-37d7-8ff0-9a7f255c625e | -10.14982 | -44.54369 | 2025-10-15 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b0bb1f6-2d0b-3b88-92df-6d07bcfcfaa8 | -12.04246 | -44.24702 | 2025-10-15 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba11e87b-4314-3dc2-9da3-8ee0e3302ed1 | -11.78124 | -43.73181 | 2025-10-15 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
