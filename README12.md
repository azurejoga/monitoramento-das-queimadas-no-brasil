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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb035ab-c754-3155-b7dc-fc10fc210efb | -7.95928 | -43.9451 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8375cb72-5208-3034-bbdb-c55fdc9d4612 | -8.0166 | -43.675 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7151e2d6-f96d-3b15-a4a9-3caa17ab0cfe | -4.58225 | -47.27151 | 2025-07-19 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45fb9065-d6df-3cbd-bd83-a67a185bc237 | -6.02547 | -44.04951 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63f62061-a472-3259-94ed-2a6df1087cc7 | -7.35639 | -45.32054 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db58cde9-ecb2-3a67-8f6b-09883b7a5b7a | -7.49179 | -47.5081 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7855c9d8-46f9-3b76-9817-3420f0542794 | -10.47353 | -47.94878 | 2025-07-19 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 504e64e3-63df-3080-beb5-b9c2c953ec82 | -6.15833 | -47.76764 | 2025-07-19 04:08:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3933252-27d1-358d-a207-4a63b1c3c6b0 | -3.59164 | -47.52673 | 2025-07-19 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb1ff245-15b7-3cdd-b14a-8d93e47cfb2a | -6.87414 | -42.75084 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac575cd4-14fa-3ade-a635-e58a1ca9f5c7 | -8.01718 | -43.67134 | 2025-07-19 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 471009c0-6516-3d93-93d5-817da43dc434 | -9.62234 | -49.0975 | 2025-07-19 04:08:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9da0bde-245a-3f1b-955a-0ce631e103fc | -6.88859 | -42.76748 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 834b3e41-37b3-3161-bf4b-d3cb8217b530 | -2.9052 | -48.24277 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d9d7be9a-2bba-38ac-bfc4-44a7ac2590d5 | -8.07094 | -50.10975 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 66dc34e3-93b6-3c7c-b089-e5e1cebfec43 | -7.94782 | -43.95095 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1181b2a3-196b-3e22-8d1c-c53087e6edb1 | -5.73265 | -44.52179 | 2025-07-19 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c340fdc-a241-3f28-832f-da6adf357f33 | -3.83063 | -47.7431 | 2025-07-19 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0386e453-f378-3254-a943-c7162c189692 | -4.10241 | -48.20378 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc12cfa6-757d-373f-81a6-0e1d10976966 | -8.14665 | -43.4352 | 2025-07-19 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61405c40-f397-3ba1-b207-a3e8e689e153 | -3.13753 | -47.01093 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 88b54766-1296-3ac2-93b7-7380d3bdedac | -6.36664 | -44.59314 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c07ed65c-3f2a-3c88-bd64-70b7296e2211 | -7.05819 | -44.06503 | 2025-07-19 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8514d80d-4fec-3cca-9bea-80593e8fe019 | -3.13321 | -47.01026 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8224f12e-b9e1-3a3e-9758-f68d0d2952d4 | -7.70793 | -47.29063 | 2025-07-19 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bd93e81-8bc5-3a7b-bb32-f85426f3b4af | -5.18668 | -44.9577 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 427efe64-5e90-3d2a-ad3a-75223173a0f5 | -5.1079 | -43.15444 | 2025-07-19 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d4a852-c942-39c2-bfcd-45155e0ddf24 | -5.2135 | -44.11713 | 2025-07-19 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81af2c58-2bec-3593-bde6-d887b1bd40aa | -9.81841 | -47.74341 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65908c07-55ed-3be3-aaf1-f8f3737d02da | -10.51401 | -42.40376 | 2025-07-19 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2304646-234b-3c57-9c7b-3e910317df83 | -4.60576 | -37.88545 | 2025-07-19 04:08:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 71a078d8-bab0-3d76-ba79-4bcd995c0544 | -5.65092 | -43.71233 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc60ae12-4e13-37af-9233-a8ce37e1684f | -3.04018 | -49.42307 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3a4c7a9-91ab-31fb-95f4-e45757299faf | -6.44408 | -51.89045 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a1618fc-a5da-36c2-b3a9-c7c7fe6b7b4f | -9.03481 | -42.70576 | 2025-07-19 04:08:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f82808af-be09-3d51-b582-81eb7c97bdb0 | -5.65032 | -43.71613 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3bb01fa4-f31f-39b8-82e4-e9977f43e069 | -6.366 | -44.59716 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f35ab0e-fefa-30dd-ab1c-c8c557f5389d | -10.23125 | -48.24877 | 2025-07-19 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91b3f507-a998-3200-82a4-26d562cc26c2 | -9.66303 | -45.23059 | 2025-07-19 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7f64700-a2f5-3359-ad16-94eb661147f7 | -10.22616 | -48.24712 | 2025-07-19 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecf23808-08e1-3a25-8f2d-79f73abcbc1d | -6.13107 | -47.30373 | 2025-07-19 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c42cb13a-3904-3fde-b5d1-3fe1edc5f9b0 | -5.38309 | -43.25356 | 2025-07-19 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766af733-dc0b-3f78-952e-bacbc34145bc | -9.95342 | -48.1685 | 2025-07-19 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab5bfc20-5482-3d5e-903f-ac3bc17f5916 | -9.48364 | -40.38633 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 920c1bf1-b370-397a-92ff-7f84ee53bca0 | -9.38115 | -47.95316 | 2025-07-19 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2674ac3-fd71-30b8-b413-b239d412988a | -5.65698 | -43.71342 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4abb2517-5bd1-3eda-ada4-2bfead4011f4 | -9.5147 | -45.42997 | 2025-07-19 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 914cddc3-b748-353b-b132-6297e7264fa0 | -7.35274 | -45.31996 | 2025-07-19 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3c0c44-fd7f-3775-9768-a59a5233e0b6 | -8.0561 | -42.15739 | 2025-07-19 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d991fa0-d9cb-38e6-a119-74aa8402f3cf | -7.37965 | -44.63366 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dd17e34-ab4a-33d4-98c9-e8ac7ac73036 | -8.54633 | -47.85054 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89794076-f1b3-3110-8c09-5beeecc486ee | -3.80397 | -43.22548 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75de6511-d4e3-3a9f-8e4c-f6a89513bcc8 | -7.18345 | -44.09584 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a9aa38e-0d45-3e2c-a5d8-08d2487674e2 | -6.97766 | -42.80677 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 598a3d97-6d44-3c1d-b22f-013127c3d6e0 | -5.65783 | -43.71341 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d3c3c070-6cdc-312b-bc94-2f3a00071b7e | -5.64912 | -43.72374 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a24b924c-17b1-3579-aabc-645329166464 | -7.95184 | -43.94775 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b06f55-4071-351c-a6ac-65750ec5c445 | -10.85462 | -44.54926 | 2025-07-19 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8d545b3-39a1-31d6-8f31-74409e3ae4cf | -6.37816 | -43.75227 | 2025-07-19 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6c96ab1-e438-3057-bef1-68fa36d468e2 | -7.48615 | -43.93833 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2d09a0b-c5a0-3f85-bbe2-86eda708a734 | -8.0133 | -43.32951 | 2025-07-19 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce3256a6-9acd-3b92-a515-ef38aca7d88f | -4.47799 | -46.07429 | 2025-07-19 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a63100d-cb28-3fe3-a8db-a583cb1dbdae | -10.62986 | -44.76417 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4e5803a-a86e-3c0a-b57c-102babdc6d9f | -6.26717 | -44.06669 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abaac908-d8cc-31c4-a26c-01be1cd8e3a1 | -7.27941 | -50.33206 | 2025-07-19 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2e88167-c462-3928-87fe-c3a1c4df89ca | -8.88439 | -50.15387 | 2025-07-19 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0865b17-0d55-3469-aefe-416e6d88c102 | -6.13043 | -47.30763 | 2025-07-19 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fd61db8c-18dc-3948-825a-fdc2a173a38a | -7.48955 | -47.49606 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 005b2ba2-d763-3414-9ff7-b6b4c4324883 | -3.67856 | -49.57347 | 2025-07-19 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ca7752-04d5-3487-9b70-7ca972ad4db0 | -6.33882 | -44.04277 | 2025-07-19 04:08:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4625137-9262-3b3c-a39a-e8c04c58261e | -7.95466 | -43.95203 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b019b930-ee76-3468-b304-b9c077a782f4 | -8.3953 | -44.02955 | 2025-07-19 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aad53ae-ce75-3be4-9448-13fabca2efed | -2.91935 | -48.245 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 714f99c3-6864-3521-9c1b-f19068fa27eb | -9.76502 | -48.7469 | 2025-07-19 04:08:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d47b88de-5aaf-333a-9af1-fe7b5eaff680 | -6.91513 | -44.83158 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51d3c27d-3102-30e2-af4f-3a380111f32f | -6.67912 | -43.01352 | 2025-07-19 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f09af855-0517-36ef-84d0-6f68dedadd02 | -7.95023 | -43.93606 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d72a3f8b-2cfe-3673-91db-8b57fb65d12d | -6.13462 | -47.30836 | 2025-07-19 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7f446c3e-c591-355d-b4b8-993d094ea79e | -5.53076 | -43.88542 | 2025-07-19 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8615fb91-b234-3f49-a1fa-e050930ecdba | -3.9308 | -43.15674 | 2025-07-19 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eaf29be-fe96-3b8d-b6ef-dd916c8cb7d4 | -8.25695 | -46.06884 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26ab5d91-c150-361f-a7c7-94e1cb5a87b5 | -5.65318 | -43.72046 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7cbd8ed4-697f-3d80-b2e4-e7a753c5b954 | -9.8108 | -48.5616 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bc3718bf-d8dd-3352-835a-02f622819e79 | -5.64626 | -43.71939 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3348bec0-03c4-3c89-a0ee-d1be6f61b956 | -6.67794 | -43.76562 | 2025-07-19 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e95982b6-2903-3bc8-90e0-111d83a97d5e | -10.34332 | -46.49683 | 2025-07-19 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70b2a8d6-6a83-39fb-bd37-99499bffbee1 | -6.27128 | -44.06336 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f399c08-7784-3f76-a6d3-66768110a9d3 | -10.6258 | -44.76742 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c63c9db-c622-38a6-b3a7-a5e3056fad58 | -8.26524 | -46.0887 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47d4a49d-5875-3b78-aad3-f55c5c0e065e | -3.03968 | -49.42607 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cddbe32b-c9af-37c0-80cd-7716107a6377 | -4.78172 | -45.34749 | 2025-07-19 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f35f7d8-94e9-31a4-8ee1-078aadc343b2 | -5.65723 | -43.71719 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6f4aa3f5-f824-399f-b2f5-182a5bc8bbab | -4.13095 | -47.65254 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 664a1a81-6fc6-3693-99f1-8e218f36a17b | -6.16874 | -48.05619 | 2025-07-19 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aded5eb9-899a-3967-95a0-2d2593c1796b | -8.07353 | -50.07839 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0037cd6-666a-389f-b1db-ee023af0085c | -8.2562 | -46.07332 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2a95b49-1e21-3501-991a-b0d6e64bbd18 | -2.91382 | -48.24925 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 43ed2375-fab2-30b3-a338-63000175bc1d | -4.66524 | -41.95943 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 636fdb98-808a-35a5-bc6d-c556f0f74cb7 | -8.07073 | -50.08163 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81b192ff-071a-355e-b5d0-ce3897054eb5 | -9.60682 | -43.85884 | 2025-07-19 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README13.md)
