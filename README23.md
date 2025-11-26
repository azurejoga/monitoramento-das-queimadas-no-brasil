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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b075d3b-8b72-3d2a-87e1-0b9eb1e24d04 | -6.05962 | -43.25255 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 565fd7d0-21a0-38b2-bac5-2cee9b1044ce | -6.3062 | -43.78538 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c3ff3ac2-38f6-3540-9f06-5ddf3a7f1379 | -4.26722 | -45.12463 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2676be98-fb1f-3ab1-a890-91f26755d819 | -2.74678 | -47.1322 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5442a8c-b8cb-33f5-9417-ce556457dc2c | -4.16725 | -43.73632 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b22e6a0-4d0e-30e8-bb3f-5602fcef4ef4 | -6.1089 | -42.9556 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da8c2bf2-2ef6-3fc2-8e9b-9c0c847e5f02 | -6.56632 | -44.03382 | 2025-11-26 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d3acc42-a124-327f-b8e4-41d391750487 | -8.05927 | -43.11669 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| dd1894a5-dd3d-3664-8fa7-990cac8bbac0 | -7.74734 | -44.18987 | 2025-11-26 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24847259-3d02-3c72-be8e-c55d36727b19 | -4.30035 | -48.59917 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e76bed46-5e51-3253-a808-d74490496237 | -2.48727 | -47.8314 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4326380-ff8c-3f04-95ef-2e3e6a32d710 | -8.04613 | -43.11082 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a9a7556c-57d2-3238-965e-05ebd041fee6 | -2.92634 | -48.23668 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3439bba-498a-36a1-8a2a-4c413d36bbc5 | -4.05333 | -48.8252 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07c1e13f-7ca8-3a39-875b-913b949673df | -3.36726 | -49.25896 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32ec9eda-2d6f-359e-b70d-2b8cb7f8f0fa | -2.72055 | -49.79078 | 2025-11-26 04:21:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff30e3c1-528b-36ad-9c26-c5104b368eaf | -2.43522 | -50.26242 | 2025-11-26 04:21:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ca256d0-64f0-3b81-9976-f1ba5ef13837 | -4.16612 | -43.72198 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45cea6d7-33b3-3565-b9cf-d03f0dc36fea | -2.74812 | -47.7524 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90f10b66-f2a4-316d-9670-0dfeb55f3136 | -4.16888 | -43.72595 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1f8a157-2572-361a-a135-07a175750ee6 | -3.47831 | -43.42988 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f10551e-e92f-34db-a23d-290c0137b1f5 | -2.42316 | -48.59578 | 2025-11-26 04:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1a3740f-87fc-3c52-9ff3-f5a1e016bdea | -2.93171 | -48.22773 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d9331d24-746e-3d2a-90c6-f9c5a379706f | -3.24299 | -50.15006 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37eda80-5b48-3912-91a7-87a521a046a8 | -4.372 | -49.76866 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc027b63-a5d4-3c7b-a415-d1e06aa14dde | -4.56942 | -43.29596 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 96f43a2a-829c-3b7a-b7ae-73f73650d132 | -3.21289 | -50.17064 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 069b9ff1-9dd4-3003-8d72-57de77dc8053 | -3.39659 | -49.52088 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9161fb8d-1b16-3cdd-aa9f-62e10679ce0a | -4.45181 | -44.30358 | 2025-11-26 04:21:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0db45ae1-87e2-371a-beab-8d22a0f5b88a | -2.93837 | -49.3588 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e42e86fa-4ee3-3117-84f7-4e9eef34e925 | -10.21484 | -36.36075 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d83307d4-ffa4-3f73-81a5-7e29939b8eeb | -4.70754 | -43.9947 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed331d9f-39a0-3d6a-9735-fc98fb6a4433 | -2.49178 | -47.82743 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32ff318b-4d79-36f8-943e-7dd1daedc8bc | -5.57246 | -46.28799 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e81b636-ec9e-3cbf-a696-097937964040 | -3.92059 | -49.2171 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1e885c73-10ba-3c6c-b1fd-002d8d8d5235 | -8.04898 | -43.13809 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 464d12a6-93f3-3605-b40e-e01fd02bf24b | -8.0387 | -43.11352 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00e0c9ee-9ea1-3a08-b953-81c1b5afb936 | -3.95843 | -49.03644 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2528c70c-3aef-3852-a18b-227a3655a0de | -5.50227 | -42.37086 | 2025-11-26 04:21:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50f2ce8b-b8c6-3d75-a9c7-43641f54b3ec | -2.46765 | -47.833 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40568163-5a30-3d19-adb2-a65f643ccfb6 | -3.48779 | -44.51124 | 2025-11-26 04:21:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1097e324-cb3f-3d21-b6d4-ea60afc480b7 | -3.13011 | -49.40863 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 775eeb6b-f910-3284-a407-05a686abe032 | -4.0964 | -43.64733 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39504103-18b2-3e7c-a2f1-f74adbbc3b54 | -5.37542 | -43.72292 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d2c838-840c-30e2-8b8f-30962b32a512 | -3.92754 | -47.7534 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b21314e7-553b-3ad5-8738-8464a2eb5493 | -8.05985 | -43.11294 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| c3e6cc9b-a199-3c88-9b8a-435deb3282b8 | -3.80834 | -44.28992 | 2025-11-26 04:21:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 594d35c0-069c-355b-8211-93cf0195adb8 | -8.06042 | -43.10918 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe8118fe-2983-3356-8056-e845225db983 | -3.23016 | -51.18034 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de034121-078f-3462-a4b1-bc1840f80f3b | -6.72877 | -39.03131 | 2025-11-26 04:21:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11f98249-91a6-3034-83a4-390d6bbf83c8 | -6.6877 | -42.47572 | 2025-11-26 04:21:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d59afc95-6476-32e7-8c50-df616204ad08 | -6.88995 | -46.14875 | 2025-11-26 04:21:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58e5a2ac-e480-3385-91a8-eb92d4d81731 | -2.48573 | -47.81715 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b975a53c-ca20-3d16-827f-5326ce7e5106 | -5.21441 | -42.98735 | 2025-11-26 04:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62275b31-9952-31cf-aff8-172b72ebfecc | -5.3397 | -49.51622 | 2025-11-26 04:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bdc3a2e-dce6-33e1-a582-06722c304bf8 | -3.48108 | -43.43386 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 409863b0-38f2-336b-9a8a-6fd180ab8e6c | -20.39339 | -57.96362 | 2025-11-26 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 760540ba-85a8-3273-8e64-1ea5abff6276 | -12.78068 | -48.82924 | 2025-11-26 04:23:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d01da9-e4ee-3c1d-b162-5ae34e70bfac | -22.47347 | -49.12965 | 2025-11-26 04:23:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f69a4e08-0496-339e-8ff9-39f57e3da91e | -20.5733 | -45.88121 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c49ce58-ba34-387b-944f-86984eede535 | -19.79509 | -56.10301 | 2025-11-26 04:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2a1718ee-29ad-3bc1-b8bb-a40bef9ad48e | -22.97871 | -48.66727 | 2025-11-26 04:23:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3eeb7dbb-0d3b-3c25-9f5d-c910b245883e | -11.88299 | -40.94796 | 2025-11-26 04:23:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c6d5cc7-42c0-37cc-b9c4-8e8573275da8 | -20.65047 | -50.38507 | 2025-11-26 04:23:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4a680898-bfb0-3b16-b1b3-fc0435e6d2ff | -20.00892 | -50.57315 | 2025-11-26 04:23:00 | NOAA-20 | MESÓPOLIS | SÃO PAULO | Brasil | 3529658 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b373f78-c371-3d93-8518-5bb27b22fca2 | -16.31823 | -51.60547 | 2025-11-26 04:23:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 303dd3c3-0561-384e-9bc2-7b7928b20b4c | -20.57507 | -45.86911 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d062e4ea-62d9-3dda-80de-aab6f383c946 | -20.7012 | -49.11251 | 2025-11-26 04:23:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebd9f587-e2a8-3681-8c69-d209a2900ce8 | -12.71374 | -46.79759 | 2025-11-26 04:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2f22bea-eab4-3810-8ddf-eee2df0dbb96 | -12.05899 | -48.23547 | 2025-11-26 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0009940a-7e15-38c7-bdb2-891367920c28 | -11.88249 | -40.95148 | 2025-11-26 04:23:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 576782b5-a416-397f-8c79-794086686631 | -12.53501 | -48.71146 | 2025-11-26 04:23:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 140de173-0b83-31a2-ae9c-8efa696eceac | -20.5757 | -45.86479 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781dad6e-a2e1-3b59-9b15-ee0b35a56d0c | -20.24445 | -50.68063 | 2025-11-26 04:23:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aba15e5a-33ac-310e-b523-22d2f75281e5 | -20.65195 | -50.38836 | 2025-11-26 04:23:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 54a029d3-b325-3d10-a973-8e6ea4f54db9 | -11.87847 | -40.95092 | 2025-11-26 04:23:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 324c3ec8-814c-39dc-8120-d2ddf520bd7e | -10.82122 | -44.01437 | 2025-11-26 04:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 970a2b11-18b7-3a30-9fec-cb5e2c0cfc51 | -22.47679 | -49.13026 | 2025-11-26 04:23:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6891f2b-483b-3669-b315-47e756b42acb | -20.39871 | -57.96495 | 2025-11-26 04:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| aece6f86-ef7d-3633-a689-4c6c851ca2fa | -20.56987 | -45.88055 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e58ed72-d3e6-3978-988e-236f86c7202f | -11.25887 | -49.47829 | 2025-11-26 04:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74104ca2-7db8-3d05-9640-59339175dd97 | -21.29643 | -48.69131 | 2025-11-26 04:23:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5ceed9e2-e025-34c6-9ca1-6a53d66ca651 | -22.47286 | -49.1334 | 2025-11-26 04:23:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd3c2953-c95b-3312-a23d-37c5bc173504 | -22.47704 | -50.79927 | 2025-11-26 04:23:00 | NOAA-20 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b26a895-a31e-377c-b452-c28e119346fe | -11.25963 | -49.47386 | 2025-11-26 04:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74956605-2543-3fda-a718-4c853bddd2f6 | -19.79029 | -56.10188 | 2025-11-26 04:23:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 66c9edc3-ba99-3b1a-8b8e-0b475251ab6f | -23.24859 | -47.23136 | 2025-11-26 04:23:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ba0514f-786a-3f89-88da-fdda91dc969f | -20.57673 | -45.88184 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffdeccb7-774c-326a-90e9-c25f79fa7a61 | -20.61666 | -45.65623 | 2025-11-26 04:23:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f20e05ae-1466-35c6-aeab-78a0e69d8813 | -12.05962 | -48.23164 | 2025-11-26 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cee104d-2441-379d-87ea-82d58a8df966 | -11.2567 | -49.4688 | 2025-11-26 04:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 909c4461-9004-3567-b07c-a4f044e58dad | -20.95486 | -43.29701 | 2025-11-26 04:23:00 | NOAA-20 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8e3ac2f5-83fd-3986-ae5e-66664cfc21fd | -20.58017 | -45.88244 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b449783f-2cfd-3435-b188-998cf1e044f2 | -14.62648 | -50.04567 | 2025-11-26 04:23:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09a3f7d3-2f70-364f-a9a0-1eca08f73610 | -19.78822 | -55.34912 | 2025-11-26 04:23:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c9ba8b-2b27-38f2-b9d3-d13ab91f3621 | -20.56704 | -45.8758 | 2025-11-26 04:23:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 485ee9f5-334b-399e-b0ec-9d8b946102a0 | -18.94561 | -49.30281 | 2025-11-26 04:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 075f7076-0636-306e-90cf-b3fa4c89062f | -16.54505 | -54.2492 | 2025-11-26 04:25:00 | NOAA-20 | SÃO JOSÉ DO POVO | MATO GROSSO | Brasil | 5107297 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79923332-3927-37ee-aefe-4e86d19a74d5 | -25.19054 | -52.97652 | 2025-11-26 04:25:00 | NOAA-20 | IBEMA | PARANÁ | Brasil | 4109757 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f78b3cc4-36ad-3864-98a4-fcaea47e7c73 | -16.76443 | -51.35753 | 2025-11-26 04:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
