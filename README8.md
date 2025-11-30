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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d32ce74d-6813-39e9-b08d-75326e92896e | -5.51142 | -42.58905 | 2025-11-30 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50e293c8-e986-3757-8930-f900e5b0d93a | -4.19481 | -42.3714 | 2025-11-30 03:53:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1ba9c79-3686-351f-a752-526d35b87af8 | -6.11086 | -41.79979 | 2025-11-30 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6ef3f044-50f4-369a-8255-437479f8af27 | -6.43694 | -38.85941 | 2025-11-30 03:53:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0f0f02c7-00ef-32e5-9bf7-5602d3509638 | -5.73187 | -40.81479 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d990cdc0-8996-3532-96ae-baa512f6ace3 | -3.33376 | -42.49693 | 2025-11-30 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 433dfce6-1934-31c7-b3b8-67971a759671 | -3.59071 | -41.66742 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 804fb27c-1195-3d1d-9c20-5c605a3e156f | -2.59743 | -49.26355 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27582c67-5bcc-39ce-925f-e563223ca4ec | -3.03317 | -45.11873 | 2025-11-30 03:53:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1566fea6-9fe8-3f42-93b0-2747d0548535 | -2.60315 | -47.34298 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b741c8cc-7ac2-3c2a-94e0-76296333fa12 | -2.70149 | -47.39911 | 2025-11-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bf8ed30-0ce7-31f1-829f-9905f8281fb4 | -2.51389 | -49.10513 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51e91f66-82a0-37b1-906f-34039dc23a54 | -2.68423 | -47.36501 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13d897e1-adc1-38a0-aba8-ebf1e8851baf | -2.64623 | -48.54639 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f61680f7-ac9a-3a49-ab85-d6cefbd46444 | -4.52341 | -44.74794 | 2025-11-30 03:53:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e39b311b-c4e2-3c81-a261-ac9d19b6d834 | -4.99345 | -40.73518 | 2025-11-30 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2db03628-065c-324e-aed3-325437a97aa2 | -3.97895 | -42.51171 | 2025-11-30 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b0558a2-0fd6-3c5b-ba2c-7f264d1b54f2 | -3.44498 | -42.23008 | 2025-11-30 03:53:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 54050173-6c9a-3c4a-9d6f-12f899383c77 | -7.55812 | -37.58128 | 2025-11-30 03:53:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ecd2f47-727f-37fc-bd41-e80245befa34 | -5.37087 | -43.02586 | 2025-11-30 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 29817472-20dd-30bc-bc2e-4cff01129521 | -3.97813 | -42.51678 | 2025-11-30 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92c77693-4674-349c-87c7-8a4c020a9e89 | -6.72729 | -39.30335 | 2025-11-30 03:53:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 668f8952-2a74-3def-a9fe-5cff8905c290 | -3.59144 | -41.66283 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8e8c4c55-0efc-3086-9e49-a6280efedf72 | -2.47319 | -46.28298 | 2025-11-30 03:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6575223b-c50b-38ff-afbd-d5736d2d0d42 | -4.54848 | -43.22367 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645aa2bd-e384-36d9-a8dc-75921b233283 | -2.21311 | -47.99946 | 2025-11-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c15cc45-d78d-3f1b-b04d-ef3ac6643efc | -3.22971 | -45.53449 | 2025-11-30 03:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff5c5595-ad35-308d-963b-da5c7683864e | -4.52433 | -44.74723 | 2025-11-30 03:53:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ed787ba-9f56-3650-b260-88a70449b1e8 | -3.36618 | -40.61237 | 2025-11-30 03:53:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a04406f1-b898-31b6-a826-f0798780611a | -3.66062 | -40.90112 | 2025-11-30 03:53:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f2e721a-ba29-30b2-9948-485cb21af402 | -3.23552 | -45.52983 | 2025-11-30 03:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a201d52-db9f-3f8b-a8d8-9bcdafb88c81 | -6.31091 | -39.6576 | 2025-11-30 03:53:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 242e1890-c7af-34e7-9200-35ce4fe30086 | -5.73201 | -39.83239 | 2025-11-30 03:53:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bbbfc95a-e49e-3d18-81bd-067e5a51c3cb | -2.63415 | -48.54436 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05bdf2fc-9c9a-304b-9855-0ab5853a65f3 | -6.68917 | -39.69256 | 2025-11-30 03:53:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c39bce2-351d-3494-8d14-3418b1663ef7 | -3.59881 | -40.86267 | 2025-11-30 03:53:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41f0241f-652c-36d1-bac6-a69fb641b3ea | -7.83032 | -35.4696 | 2025-11-30 03:53:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f4c2a5ba-6f71-39dc-840e-b4a5e5a3e7e2 | -4.36616 | -43.15983 | 2025-11-30 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a1ccefa-8e1e-3e76-8bd4-ab0a300cff6e | -2.96203 | -49.21458 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfa92e94-964d-3bd2-a4a1-8be382706d49 | -7.83096 | -35.4654 | 2025-11-30 03:53:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3fb5a8b-8b8f-3405-be80-ec38b0584fca | -2.87335 | -46.70213 | 2025-11-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5982e21-77cc-3db5-8668-ab109f47c56e | -5.15489 | -37.68715 | 2025-11-30 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e961219-0c5a-3b65-a5a7-5b71be7d54ac | -2.60009 | -49.26575 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 544607b7-89d3-3b68-b88d-bea41dda10e1 | -5.3629 | -43.02446 | 2025-11-30 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8428107b-1e4a-3ead-b1b5-53162d11a155 | -4.42255 | -43.30525 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae5b3a38-2716-383e-94f4-f36fd50ca4dd | -2.68031 | -47.36302 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bab881-a17d-3567-a2e6-4041d155362a | -4.42607 | -43.3097 | 2025-11-30 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d0cb48b-8308-3225-896c-5423d1eb5f77 | -4.60691 | -45.20983 | 2025-11-30 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de0183e7-f4b1-33bc-9619-5f8d9412ebd0 | -2.4496 | -47.07676 | 2025-11-30 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb0750e9-2ca3-38cd-8b5b-620a10708fe5 | -5.74364 | -40.80888 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 205dd61f-c7ef-3b3d-8fc6-b346429baa0e | -5.15819 | -37.68766 | 2025-11-30 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05710eea-828c-3398-8bae-13d61d551837 | -2.9683 | -49.2156 | 2025-11-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7548995a-8d8f-3282-9a8c-e850f4aa7c60 | -6.72294 | -39.96739 | 2025-11-30 03:53:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e00a60cf-20e0-310d-982b-ea8c30129b4a | -3.58317 | -41.66621 | 2025-11-30 03:53:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bce81ab4-4f5d-3fe0-a3b5-cc48fa4a2f60 | -5.50912 | -42.57867 | 2025-11-30 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8d2fb824-788a-36c0-9efa-3c9d4dc6a7c0 | -2.17652 | -48.42022 | 2025-11-30 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87b77ad1-c14b-3893-9cad-337859c216b8 | -2.63492 | -48.53983 | 2025-11-30 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 295de05c-feb8-365b-a737-6f827d89b9e3 | -3.94656 | -41.77368 | 2025-11-30 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1144e66-b157-36b2-99b7-0636ece7c71b | -2.1396 | -48.52151 | 2025-11-30 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b18f217-a954-3960-bbb9-84c3b7cd1f3e | -7.83456 | -35.466 | 2025-11-30 03:53:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7d2eb2b-98ad-3487-b338-24e8557ae6fa | -6.58206 | -39.63878 | 2025-11-30 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed22b2f6-8621-325a-a043-1e4cb8e85cea | -5.74653 | -40.81327 | 2025-11-30 03:53:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2ce72ca-4519-3f2a-810f-a5a67473c07e | -12.82533 | -47.39261 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e94bb9-892c-3df2-82d5-fb8e83d8b390 | -1.47808 | -47.75422 | 2025-11-30 03:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30532e1b-62b6-3727-bfd4-6b03868dab2c | -7.47861 | -41.78882 | 2025-11-30 03:55:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05c397e2-6485-373a-8d6f-31eca98f05ec | -7.47567 | -41.78411 | 2025-11-30 03:55:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9b6e0fa8-25fd-37db-b63e-d5c4414f9635 | -8.048 | -43.1278 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 08139cc7-fb75-32fd-8626-692d29cc2a84 | -3.51032 | -39.09925 | 2025-11-30 03:55:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 78b0d548-0dc2-388a-b3c2-8629f3c15f6f | -12.45427 | -44.88783 | 2025-11-30 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b43f9de-6f0a-3f3e-9f28-896115327dec | -13.57517 | -43.06781 | 2025-11-30 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1037692-3f62-31ae-84bb-01a149ff42ba | -8.0489 | -43.13124 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3a5089b1-9202-3ff2-847f-a6f2ba6c2c11 | -7.74665 | -44.1909 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b80fb414-3bde-3cc2-930b-cac7af745b34 | -9.71709 | -36.66171 | 2025-11-30 03:55:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e50ad6d3-cfa4-376f-92e5-9a86188ca3db | -2.32061 | -45.64867 | 2025-11-30 03:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae63c8a-1c22-3485-80ec-a778ba8333e2 | -7.47928 | -41.78467 | 2025-11-30 03:55:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 65c2fc87-25b4-33f1-97d1-c6fd7e305deb | -7.83199 | -40.64604 | 2025-11-30 03:55:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3fbfb5d-484c-3635-8e6f-e6e25efb9603 | -7.739 | -44.1856 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adc2d504-dec5-3338-ae66-bfffb10f5c58 | -14.26356 | -44.38774 | 2025-11-30 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d320f634-9a1d-33f2-8ac3-1af1e7917697 | -6.91868 | -42.80544 | 2025-11-30 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdfcdab5-27e9-3e39-92e7-5d280b9f3c6d | -7.73964 | -44.1818 | 2025-11-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f87b2336-a33f-3b83-8a6d-5e5a22242fe6 | -9.3001 | -40.36624 | 2025-11-30 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3cad4b72-9d32-3a89-86f9-2841318ba949 | -12.65879 | -46.75477 | 2025-11-30 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46e1931e-5329-3a8d-ad03-89f03555fc57 | -7.45454 | -44.74453 | 2025-11-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f77cd675-21e4-3b01-b46b-bcd45f5af2ce | -8.04974 | -43.12637 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f0fdf5bd-37c5-38b3-b9d7-c45747d9dc01 | -1.47291 | -47.74912 | 2025-11-30 03:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 839315a4-1a97-3e27-ae0a-ab240c9c4214 | -8.0356 | -43.13073 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b1fea45d-decd-3a7b-8fd0-4da1eee553cc | -12.82627 | -47.38747 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b79af2-ff53-3604-914a-ef6a97ec3ea9 | -12.83097 | -47.38843 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5da94f6-0511-3ff3-88f5-88ed9dc62932 | -12.83003 | -47.39357 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c2c7db7-3d50-3f9f-938d-bb664d8e9e0b | -8.17158 | -43.2142 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 8ec8531c-4917-31d6-85fa-78038395cd01 | -8.16853 | -43.20865 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 8c356256-3713-369e-955f-1d5d6838f906 | -12.83663 | -47.3917 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6229308b-0b25-32f2-b779-ab32548b4bf6 | -0.96085 | -46.79832 | 2025-11-30 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 080266fe-dd66-38b3-94d4-126195c94b04 | -8.16382 | -43.21289 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 9424b8ad-8729-3449-a233-5c1201e0d54b | -12.83568 | -47.38937 | 2025-11-30 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83734ac9-9a85-3e9b-b5ce-a95b35f34aa0 | -8.17324 | -43.20441 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b3a80937-34c3-3ec2-9a57-21ebc5f10692 | -6.90852 | -42.8187 | 2025-11-30 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b0d01ad-5c53-33ff-9389-f1847fb466d3 | -8.0472 | -43.13268 | 2025-11-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e542a5ec-166e-3921-a13e-49482e5c7f1c | -0.96144 | -46.79467 | 2025-11-30 03:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26499a72-3909-341f-b830-f1574f7909c4 | -7.46348 | -39.9623 | 2025-11-30 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
