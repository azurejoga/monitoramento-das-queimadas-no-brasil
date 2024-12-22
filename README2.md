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
| 6e182f30-aa20-3c18-b481-50817e815fb5 | -4.93033 | -41.32472 | 2024-12-22 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eb9d80fb-3337-30e3-8e09-721f74839c3a | -4.95332 | -44.00776 | 2024-12-22 03:34:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f8e3de9-dda4-35d9-a882-477a5a5ce792 | -11.56469 | -38.12827 | 2024-12-22 03:34:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 69f0c2b5-f855-3f88-899e-ab919f13e060 | -5.22322 | -44.33832 | 2024-12-22 03:34:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 243c4dbc-54ed-3d8e-8337-07f31bbc6853 | -7.51354 | -37.77952 | 2024-12-22 03:34:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c8beca3a-93e6-3a19-a69e-823e5744f0bb | -4.72542 | -43.25472 | 2024-12-22 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f2e92dc-10ff-3c7f-92aa-5dee6d222483 | -4.55718 | -43.30261 | 2024-12-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39e8ba3f-b460-3d7b-80ff-c738a5525e62 | -4.81799 | -44.41944 | 2024-12-22 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee89de9c-4b1a-30e8-b229-e2641471d069 | -5.86146 | -39.35717 | 2024-12-22 03:34:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7932704e-86b1-3e39-b990-3b1cd85239ad | -5.23004 | -44.33495 | 2024-12-22 03:34:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12fc1df4-d8fe-30c2-b3b3-00b91f30eb26 | -6.0009 | -45.4166 | 2024-12-22 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0476af3a-9e1d-3914-904a-96abaeea6914 | -5.96395 | -37.46301 | 2024-12-22 03:34:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a623540-46e9-3145-9fb1-818c4b7ab055 | -5.93278 | -39.73687 | 2024-12-22 03:34:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97b1233d-51e0-3964-b480-045a943861fd | -8.47779 | -41.82104 | 2024-12-22 03:34:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ace3bb9d-3edb-3dd3-93d6-745399b863e5 | -5.36922 | -43.08952 | 2024-12-22 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a32360-671f-3dc3-9b3b-b4bb1b5c9ecc | -10.18243 | -36.26581 | 2024-12-22 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 597cfb10-102e-3031-b94a-88ee847e91da | -11.54315 | -40.41456 | 2024-12-22 03:34:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c033c053-f3d4-3ce2-b5f9-449e386d7f65 | -4.81928 | -44.41185 | 2024-12-22 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23c7d301-3648-3e8a-9ae5-f1ccdf73b2cb | -4.72477 | -43.2586 | 2024-12-22 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2682a9d5-68c8-3ed0-a2aa-af3cb4c54d96 | -9.05488 | -35.5873 | 2024-12-22 03:34:00 | NOAA-20 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9cff26d-0100-3592-82a6-c6303a55469b | -6.44326 | -40.00369 | 2024-12-22 03:34:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4be8902a-6b70-3be3-8213-8bea9220c704 | -5.42772 | -36.73534 | 2024-12-22 03:34:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b2e7262-b3f9-37ec-a4fe-a2765f6a21cf | -4.9303 | -41.32582 | 2024-12-22 03:34:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef5a23dc-0c7d-39c6-bea0-ea3716531b8a | -8.34596 | -36.83298 | 2024-12-22 03:34:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 002bbf1c-25cd-3856-8c60-9e08ba6e85a0 | -4.00484 | -46.56207 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81eb296e-6c0b-3028-b5fa-ce26854418dd | -5.36985 | -43.08585 | 2024-12-22 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7186cbe2-8450-3850-a6a5-63527c63890e | -5.22401 | -44.33382 | 2024-12-22 03:34:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72d28b43-8c7b-39ae-a3f8-aba69b196f6a | -4.81279 | -44.41307 | 2024-12-22 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa7ec840-6ad1-316b-bf99-5c5df8e2bcb1 | -4.72749 | -43.25512 | 2024-12-22 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cecd8bc-3a20-3382-9379-8a2275bebd58 | -8.17001 | -37.68582 | 2024-12-22 03:34:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a968473-717e-382c-9a99-15912ad88859 | -4.55785 | -43.29868 | 2024-12-22 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b58b310e-21e3-3207-81d7-054e2c9fab19 | -8.0732 | -34.97599 | 2024-12-22 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 937ea41c-953b-3be5-b199-b92ed647f9f4 | -4.72681 | -43.259 | 2024-12-22 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24dbe017-92f8-3ac9-90fc-05b07fde7205 | -3.94346 | -46.41959 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2706da2-b2ce-3fcd-bb09-44c274bc841f | -3.95044 | -46.42083 | 2024-12-22 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26e3c0fa-3702-349e-9306-bf0bb72cf528 | -7.13114 | -38.7794 | 2024-12-22 03:34:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 45ed96a3-9ce0-3207-94b7-04e481cfddc7 | -4.81842 | -44.41664 | 2024-12-22 03:34:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23a2c11c-ed5e-340f-b686-90b20e80e332 | -6.26076 | -39.79987 | 2024-12-22 03:34:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a27c8f35-dd41-39e2-b56a-8f2aeba7f01e | -7.89761 | -35.25269 | 2024-12-22 03:34:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48ecd3e2-3c01-390a-9edc-6372d6e0d8dc | -12.33199 | -43.68007 | 2024-12-22 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e95d2742-aef4-3119-a2ce-41aa17e5ca29 | -12.33711 | -43.6811 | 2024-12-22 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1320a60-259d-354b-83cd-dc3375977d3a | -12.44635 | -41.43494 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5de490b1-d24c-3b94-8005-60c792528991 | -12.4389 | -41.42577 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a472fc6-91cd-3344-84d6-237df7a67216 | -13.39747 | -42.32399 | 2024-12-22 03:36:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3cd33613-98f7-3b70-bc82-057cc3ddd4fc | -12.43411 | -41.452 | 2024-12-22 03:36:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 159e5c0d-8a7b-317b-9ea5-4663aabbb57e | -12.44411 | -41.42223 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3dacbc9-222c-327b-82a5-c4d7d23da0aa | -12.33652 | -43.68417 | 2024-12-22 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b2a26c2-817c-322a-a93a-45bf84f7f7c9 | -17.73802 | -39.52703 | 2024-12-22 03:36:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c1c3c622-98c7-3729-a963-48c42d084f8a | -12.43503 | -41.44695 | 2024-12-22 03:36:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d6a8b251-1811-3287-921d-c2108c3d3757 | -12.43958 | -41.44705 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| faa5a78c-2cf9-31d0-8f7c-f84e43544f59 | -13.39838 | -42.31903 | 2024-12-22 03:36:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c80761a1-4ed1-3048-bc02-0fb6f559120c | -15.60391 | -39.61992 | 2024-12-22 03:36:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bb924f34-e861-3d9a-8c35-0d231b0532f3 | -12.44039 | -41.44258 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2b22e5ea-1654-3ff6-84b2-50cd977d1a8f | -12.44117 | -41.4383 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a202ce2b-39d5-30fc-9dc8-cf4c4b9e87cc | -15.31226 | -39.17998 | 2024-12-22 03:36:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61d09878-7db5-3008-8058-abb419986149 | -12.43589 | -41.44224 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 506c0f81-d391-3c16-bb7a-3ceb049281fd | -12.43869 | -41.45191 | 2024-12-22 03:36:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| cdf32479-6555-3f77-a3f9-642abdc3b6cb | -12.44559 | -41.43908 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d76b8642-31b0-3d80-afff-6eccb1c774be | -14.46772 | -43.35163 | 2024-12-22 03:36:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5dd8ad1-4a23-3d7e-9360-7f6b1c618850 | -12.4116 | -43.80215 | 2024-12-22 03:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44e2b2f5-7fe4-35da-9f2d-2ad745bc751c | -17.73439 | -39.52634 | 2024-12-22 03:36:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c09361c4-16e3-30c4-a5ee-425d4d9b8dfb | -13.40298 | -42.31998 | 2024-12-22 03:36:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 299d1cbb-e9fd-3d1f-89fe-ebeeaf0a379d | -13.40207 | -42.32491 | 2024-12-22 03:36:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24ff96e2-e36e-30dc-b198-8e5e3ca024e6 | -12.3377 | -43.67804 | 2024-12-22 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4be8de47-79ba-3589-94e5-ef9d7c8658f3 | -12.44191 | -41.4343 | 2024-12-22 03:36:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5016a9c-4bb5-3481-988e-373da6bad425 | -12.34282 | -43.6791 | 2024-12-22 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfe2546a-edbf-3464-81d3-f739aa0b6adb | -1.36571 | -53.69796 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80f0c7e0-8d0d-368f-b0eb-b5f5245f1904 | -2.90499 | -54.4982 | 2024-12-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77effe85-68e5-35a7-aeeb-5650cca3e0dd | -3.09612 | -46.56547 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f377eb1-ee67-3a71-8658-eaf114214157 | -2.8023 | -46.70557 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 480dbf61-598e-3123-bd1d-2eb95324e397 | 0.00157 | -51.19769 | 2024-12-22 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c147311-9a40-3a1c-afee-b73825fdd9be | -2.8253 | -52.86319 | 2024-12-22 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55ebecdb-64f0-3554-bc67-2d7a9c5e61a6 | -1.90968 | -45.6052 | 2024-12-22 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf9a06d1-a9cd-35bd-a0e6-b8b39212fb34 | -2.81328 | -45.9369 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55c29d6-6ecc-3ca4-9029-ad3caebbd3b6 | -3.76584 | -47.19646 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 350763a9-ecfc-3ad2-ba98-5344f091528e | -3.06792 | -47.77072 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 60331cdd-bcdc-39ae-b05f-bad638bef43a | -4.02931 | -46.79763 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2bcee5a-baa9-3fd1-ba81-b121ae0d25b8 | -2.50732 | -49.05704 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f11cb2-ab18-3587-932a-8dab9f159447 | -3.97085 | -46.60627 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb70794-287b-3122-8489-a0490145ce6b | -2.50234 | -51.82872 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f83419-0a62-30cf-99ad-4f8ad87b4b5d | -3.90958 | -46.65014 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c2d571e-76d6-366b-876d-b71991f4ef52 | -2.97592 | -48.08615 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b44aefa-e039-3404-8a2f-6474086b18eb | -4.05444 | -47.08924 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e573a06d-9559-3e63-a7b8-8e4253f8f2ea | -3.85543 | -46.67009 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261c2bd2-ba72-3297-b493-e05074fe2ea5 | -3.17545 | -45.97269 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df884fea-1736-3a5b-8cc9-0fb55b8582fa | -4.60721 | -45.44953 | 2024-12-22 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c25b601-fa03-3b94-9e5f-141f41d5d081 | -2.7294 | -46.19196 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79eb14ab-e07a-38a6-9763-af5203a02dfb | -3.99611 | -46.55339 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc2666b2-7968-3b18-b881-7fe20c533e23 | -3.79919 | -46.85445 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31f0f993-44e4-3ff3-a852-0ea0c49f7fc1 | -3.97584 | -46.61776 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2286c01f-da08-376b-b936-8bfd2ee1c586 | -3.98268 | -48.39672 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb526ab7-f252-30ca-99be-13006246fdab | -4.07091 | -50.34512 | 2024-12-22 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5f81a25-4349-3743-b867-5729fa6dc957 | -2.82952 | -46.68111 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c76efbba-e697-3d53-a62b-d603f1278916 | -1.36677 | -53.6915 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 904465a4-86f7-3415-afa1-640bfada746f | -4.04738 | -47.03025 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715a2a52-3e63-3d48-aaef-49bcdc5a0efc | -3.40981 | -44.11845 | 2024-12-22 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a20ac79-92d7-337f-a6bb-f7cb66381700 | -3.9193 | -46.89111 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19b6e8f4-fd5c-3014-96a8-96150991d577 | -4.93758 | -41.34454 | 2024-12-22 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f50fde99-cf39-3730-adbc-f6a82246e198 | -3.9182 | -46.8981 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 233c0760-6bf7-34e4-bc73-c93d0e1616e2 | -3.81124 | -46.71312 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README3.md)
