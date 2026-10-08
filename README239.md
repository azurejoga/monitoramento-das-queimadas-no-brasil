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

## Dados Diários - Página 239

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b57003cc-0f16-372e-ac37-9022526b7d5d | -6.49527 | -41.82511 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d11b0eb3-fd7f-395e-8f7f-fb508a8e7b96 | -7.08881 | -43.08521 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5ef9446a-4690-33d8-a092-d2b02053a41b | -6.79021 | -45.05117 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 0dd95ca8-3d77-362a-a53c-680b805556f5 | -11.09168 | -43.99989 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7539af03-1fd6-3860-aa50-640bdc3d167a | -5.48294 | -41.21919 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 881b68dc-cb0f-3d77-ad80-f7683e79e70c | -5.94853 | -45.69313 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5cc02728-efc4-30ba-890e-d274b2374c0b | -7.19142 | -44.3133 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 04f01c68-da58-3339-908a-a02598c8032e | -9.74436 | -42.24164 | 2026-10-08 15:41:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3aa78e6d-6a6a-34d4-81d6-ef0a6faff99c | -5.96778 | -40.91154 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| fd87f6f3-792a-315a-92d5-bf6d21ac564d | -5.75352 | -42.07712 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b8903dc0-f382-3b7a-9edb-dfe28d43615d | -9.55417 | -45.23351 | 2026-10-08 15:41:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4d126dd7-a5fc-3ea6-bc1e-17ba6b3b3ee9 | -10.64681 | -41.20515 | 2026-10-08 15:41:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 61.5 |
| a123c17d-e7a2-39eb-976c-3a53b68a0ef6 | -11.08659 | -44.01075 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0e617d46-909c-3a71-8a01-76c6f7834389 | -7.54038 | -42.08508 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 6f6873ab-d036-36ab-8715-bd88c8c29982 | -10.0756 | -46.00669 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d2e760b9-9b07-3ebf-a7f0-12169d6497d0 | -10.0421 | -45.59784 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b49fa9e2-2fa2-3925-a076-201cbca316b3 | -9.94241 | -43.57217 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f3d1825b-7e0b-3219-9b23-af1346089ddc | -9.8852 | -44.86017 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 87cece04-52ed-3b07-89b0-d6b61e92c6f0 | -7.39503 | -44.47863 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c2786e7f-68bf-32e9-9e49-5e8ab1c95623 | -11.26616 | -45.20514 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 13892494-c87e-3db5-94ac-cbaa59fe354c | -9.89138 | -44.80255 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 307408f9-ad6d-3f83-a12a-bd54524b5774 | -6.82194 | -41.89319 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| ed77c7cb-d5f2-37de-9a38-34ac4875bf3e | -10.25152 | -39.96378 | 2026-10-08 15:41:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3e8000a3-83cb-3821-99c4-0ef430c04dce | -6.05277 | -35.18981 | 2026-10-08 15:41:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3c406902-d479-3c87-b6e7-b58a9af28567 | -6.25784 | -45.33023 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ddb27c0d-f787-39f0-85a7-2c303bc72aad | -6.49332 | -41.82731 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3022cdab-fa38-32ca-9ed2-a1ed194ce13d | -5.87363 | -45.9634 | 2026-10-08 15:41:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 216958e6-00cb-3f76-b11a-81bea00b46df | -6.3381 | -35.12825 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 4c334b52-5657-3eaa-97be-a88afb50804d | -6.79091 | -45.05642 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| e8bd048d-412c-3dce-8d72-79bf4541be1b | -6.66706 | -45.36625 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 5a486e74-7735-3172-a5d3-17b705b86b17 | -6.68173 | -45.08334 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 316d6be5-a5a5-3258-a3e5-e42b8b62946e | -7.40391 | -44.45507 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b5cdf9d7-dea6-32db-a527-0d6375b67576 | -7.84506 | -45.5089 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b329c70a-4840-3e19-bdab-24ee8bab9ae3 | -6.15482 | -39.4456 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a2af85e2-53c9-3bc6-96d2-fd28fef0a615 | -6.32392 | -35.12658 | 2026-10-08 15:41:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 5cd62c81-127a-367a-87ab-3066abbf95df | -6.8558 | -41.74369 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 4d710ef1-01b3-34b5-9011-222f61048c5f | -8.20426 | -46.37626 | 2026-10-08 15:41:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 53e1a2b2-3431-3fb0-922c-29a276245061 | -6.01067 | -42.26285 | 2026-10-08 15:41:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f2b7f0cb-48d4-382c-9263-a2e2a8fd0b7c | -7.27602 | -44.1941 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66856769-412b-316c-8004-f1a96d8a6ff9 | -7.26671 | -44.21727 | 2026-10-08 15:41:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6197d084-d412-326e-8481-1e0632178313 | -10.15956 | -44.67225 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 51c9fcbb-3b74-3650-9b35-8a32b9565072 | -6.53103 | -45.39382 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0b2adff7-3e2a-3f7b-8add-d4b936443c31 | -5.38289 | -44.1961 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| c1f9ef2d-bc1f-3eed-a53f-1680c2c4f48f | -4.98137 | -36.88209 | 2026-10-08 15:41:00 | NOAA-21 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 55e8e7d5-ec25-316a-866f-cfed4e38b2a2 | -10.22166 | -39.34959 | 2026-10-08 15:41:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2fb9c865-3951-302a-8159-fdd66ed639d0 | -7.24461 | -43.51031 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5ae401c4-6f80-3807-a084-c96ebbc63eb6 | -7.3089 | -44.00631 | 2026-10-08 15:41:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b3e1e02c-1fcc-33df-91ac-53310e38c11d | -5.72211 | -41.71756 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d1aeccfa-913b-3525-935c-e0ce1217d8a3 | -6.9989 | -44.05315 | 2026-10-08 15:41:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7ebe178-d01c-35b2-848f-50e8b55937ae | -5.85184 | -42.62907 | 2026-10-08 15:41:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bad355a4-2d60-3e35-a144-c17ac7e514bd | -6.50217 | -44.20847 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b41b0977-da7a-3b3a-8d9a-b23ff70d6e23 | -5.77283 | -42.06516 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6d907311-f507-352e-8253-4af7800e81ed | -7.1339 | -41.80787 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f53a5fdc-c131-390b-ba1d-302ea8da93fe | -8.257 | -35.67376 | 2026-10-08 15:41:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5ea52754-f5c6-3740-b25f-35d1e846c217 | -5.71898 | -41.65825 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 807a8f0a-cce0-353e-a17d-81e4c7241d79 | -6.92447 | -43.06879 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01586061-9ac1-3040-86a3-59c52e1260a2 | -5.37269 | -38.2813 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e6e508c3-c6e3-3531-b801-8a6c85e5eae0 | -7.05524 | -44.32155 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 09f1150a-0ae8-3e3b-8c68-4bfbb40a711a | -7.53552 | -42.08905 | 2026-10-08 15:41:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 2e245e1f-2d92-33f0-b5f1-5170d9fe6f6c | -6.53678 | -45.3877 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 19cffee9-0f91-3136-b81f-65611a534d11 | -6.92534 | -45.26844 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 44ce946b-32cd-3a8e-be93-19863adfc6c4 | -7.48255 | -42.82975 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ec5653a3-2289-33cf-9cd8-e93038a3e087 | -7.46554 | -42.82529 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ac1b7aa4-6aaf-326f-a41a-087996f8ae87 | -11.09798 | -43.99924 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b2865e3d-bb8d-3ad3-827d-da2977c7377d | -7.39393 | -44.47507 | 2026-10-08 15:41:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d3924327-577a-3ce8-b74b-0fb4f5a9fe1f | -5.53108 | -39.85595 | 2026-10-08 15:41:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 46fbefbb-2fa3-394f-9dce-c20bbd4616e1 | -6.15704 | -39.44629 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 95652e12-2408-3844-8049-96a5761c6fb6 | -6.22932 | -44.97445 | 2026-10-08 15:41:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcd9fdc0-ef3c-3a55-bef3-eaa74dc67a08 | -10.96499 | -45.39408 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5be9c704-dde2-3874-bc41-b98bcf98de63 | -5.76767 | -42.06579 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8fbc5adc-1d7d-3ea6-8814-8d22ab624c13 | -7.18946 | -46.51827 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f9f741f5-f171-32f7-a65c-be1221aa8432 | -5.71071 | -41.67167 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fc3f4c70-1be7-3d2f-ae5b-d13fb05509b9 | -6.60404 | -37.89736 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 20.9 |
| dcbb3608-92c3-3f24-be61-0a1e128aca47 | -8.93587 | -45.15594 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 395705f8-665c-35e8-b74e-52b3f307b8ff | -5.73088 | -41.77547 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 38dfb14a-2df1-3884-9e5c-fbd9b88540bf | -6.15865 | -42.58689 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 6f82f957-4220-3cd8-a202-463040b1ab5d | -5.74748 | -42.07167 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 19fe104a-9e0b-36ac-917f-b723216f6d8c | -7.05644 | -44.33069 | 2026-10-08 15:41:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c8c69ddb-2526-3a24-ac51-6beec464e29a | -5.70316 | -41.6902 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ff53d31-101c-3a15-829f-c703f336f353 | -10.38239 | -46.30662 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 42662b5f-2d94-3283-b243-555bc553cae7 | -6.82426 | -39.55967 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| aff8501d-87d4-30ad-8082-6fff8a1c9695 | -8.93748 | -45.15925 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| dc1cbccb-f579-3075-862e-f7dfe3851c56 | -7.39799 | -45.6368 | 2026-10-08 15:41:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| a3ad221a-c6ea-3bc8-be12-bce922fe5247 | -6.56251 | -44.38449 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fec3dc5c-7ed2-3831-9ffb-4347467115a5 | -8.9529 | -45.17546 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1fa30a63-5524-3cf8-918a-c8837cc8e25b | -11.10428 | -43.9986 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d98212da-375b-30a0-a990-6b1141c58b18 | -11.25122 | -45.25432 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9396f191-1696-3572-bbfa-2ca448afabed | -5.30198 | -45.71702 | 2026-10-08 15:41:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 5ff510c6-4c09-3ecd-a0ce-ef6aea438202 | -5.76426 | -42.06396 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 35fc2cf6-fbe9-37cb-b5d3-1ef7e0027724 | -6.848 | -41.76289 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a403fb86-4271-3021-8fe8-90c9225b45d5 | -6.32772 | -43.83046 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 45c54b23-0147-3098-a379-d3a4662d9e76 | -6.15531 | -39.43383 | 2026-10-08 15:41:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| f3e38a57-43b9-30d4-a81b-f44af3727676 | -6.96962 | -43.89755 | 2026-10-08 15:41:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef0aea03-382b-316b-9036-7ed269a24a62 | -9.88588 | -44.86558 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 29001840-28be-3c89-b7b4-ede303daa979 | -6.66447 | -45.35215 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8d014be2-5dca-310c-8dba-5dd4ee392126 | -8.59724 | -44.86895 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 978ce015-0df1-3279-ad59-f8d4e1b440a4 | -4.58217 | -40.65285 | 2026-10-08 15:41:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 732469fe-1d58-3b32-8326-1fea03e1e6cb | -9.93637 | -43.57283 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 5820bf86-1ab3-3e55-a35c-5b37c233076e | -10.90416 | -45.53006 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 436ae343-8e1d-3742-b22e-f83fa3222e1e | -6.24168 | -38.47905 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README240.md)
