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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448f2699-1db9-3d71-940a-7a784ac628f2 | -7.96839 | -44.50983 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2eb0c6c4-c095-31b9-843e-a1e96538f6a2 | -7.96787 | -44.51354 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c6fdf97-f747-331a-a2ef-5365c5a29d08 | -7.90269 | -44.62047 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 439ddba2-8e10-39bd-adba-81035336694e | -7.8997 | -44.61259 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d126d74-d533-39ea-8767-c0dccfbc9c27 | -7.89916 | -44.61625 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 234852ac-a862-37f3-8781-b1981ca4e459 | -7.89864 | -44.61988 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63308ad6-0fc7-3f99-8800-6e1924485098 | -7.89811 | -44.62351 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46f0e11a-e937-338f-8fa1-0c9b30485680 | -7.89564 | -44.61201 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da6412b0-05bf-3c93-b8b0-9685e5d8f578 | -7.89511 | -44.61566 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f81ddcb6-e96c-3647-acfb-61d1a165b5ee | -7.89458 | -44.61929 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2917c4ea-0169-3197-a744-a1b20be9f23e | -7.89406 | -44.62291 | 2024-10-13 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82731860-e0bf-3627-931d-d28882e7667d | -5.80028 | -43.22348 | 2024-10-13 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73006a76-303a-3a19-8cb3-798d1ad7341d | -5.66715 | -43.30643 | 2024-10-13 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54b41859-da0d-3529-b2a6-9f2262500021 | -5.94581 | -43.97014 | 2024-10-13 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2d0a66c-a6a7-35d8-98bc-e03c1f1d6637 | -5.94414 | -43.48255 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a50cf12e-fe23-3bfc-87d6-e12de9c2725c | -5.80815 | -43.97105 | 2024-10-13 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37510ce1-e7f2-3dbd-bab6-968da692b9b3 | -5.57614 | -43.93425 | 2024-10-13 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f4c044-b53f-3e02-8d09-1f5d26902f47 | -5.57203 | -43.93365 | 2024-10-13 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bd353a2-6981-3e07-b1e7-fc58b997fa50 | -5.38208 | -43.51001 | 2024-10-13 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c23815-4992-3235-803d-bde527d0f95c | -5.37788 | -43.5093 | 2024-10-13 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7e19111-15a7-3a86-9d35-82db6f809cd9 | -5.3773 | -43.51318 | 2024-10-13 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ba5e2f-a2b6-3193-bb85-0d4c2c88d433 | -5.3731 | -43.51252 | 2024-10-13 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eccaf82b-a263-35c0-9d9f-a08646d1d3cd | -5.22089 | -43.88964 | 2024-10-13 04:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1acc13aa-323d-3910-95b6-bc95ca09db1f | -9.82642 | -45.04543 | 2024-10-13 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac8fb712-1bd5-3de9-a120-3a7ef814d27b | -9.65965 | -45.21894 | 2024-10-13 04:40:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 148bd22e-e750-3509-9a55-5e3e43126302 | -9.65915 | -45.2224 | 2024-10-13 04:40:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e5be4dd-4bac-34ab-99ae-36b540cf9400 | -9.44489 | -44.14383 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75f01ae2-a9dd-3daa-a842-3e382732f804 | -9.44433 | -44.14794 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9046f0e8-2bed-3356-8223-8d248b40c1a5 | -9.43149 | -44.14609 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 749c59b3-519d-39d0-9101-19fa1f08871a | -9.43093 | -44.15018 | 2024-10-13 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f82a6a2d-fb11-3cb7-86e7-f0a5c3e62c1c | -9.57522 | -44.38551 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d71f117e-9d83-3496-9e2c-d9bb01b2ceb8 | -9.57466 | -44.38941 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 544118f3-955c-3690-8ec6-b59566b9c67b | -9.56299 | -44.47124 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68425913-a22e-376b-82ff-64af79d8f339 | -9.56242 | -44.47523 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 925f753e-e9d8-3f10-b943-e8bb9fadf139 | -9.55767 | -44.4786 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77d54d38-8ac2-32e3-b21e-d96ce491673e | -9.44501 | -45.51408 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff2fa2d9-c4fe-3d9d-8a89-c619b3c89fe7 | -9.44177 | -45.50879 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 7bffed97-28b0-3163-aabc-6674e0bcf77a | -9.44108 | -45.51363 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0e854ae7-9d08-3f8d-9d47-4eab484303c5 | -12.29579 | -44.34991 | 2024-10-13 04:40:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac7d3bef-bb53-3c22-bfe9-4f1c577b3a77 | -12.29537 | -44.35223 | 2024-10-13 04:40:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51452f30-2fd3-385d-a6df-6c532f5a1318 | -12.29523 | -44.35425 | 2024-10-13 04:40:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6f79161-d6e8-3668-abae-6cd1de30ee57 | -10.93102 | -43.09438 | 2024-10-13 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cff5e2dc-b292-3f65-a77b-60d1612c387e | -10.34294 | -44.36493 | 2024-10-13 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49ba7e5a-61d2-327d-9bcd-ac41dc9743d0 | -10.29693 | -43.42403 | 2024-10-13 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cef78c52-58da-39eb-b94c-6e034b615ca6 | -10.06128 | -44.17647 | 2024-10-13 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 324dcb16-ac4a-3105-92e2-f85e524fa98f | -10.88722 | -44.34998 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ca4b029-da48-3903-b2c2-0ba9855b5d19 | -10.86154 | -43.64084 | 2024-10-13 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 987890c2-4e53-320b-8dda-a311cfe770cd | -10.78916 | -44.30882 | 2024-10-13 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0040c56d-1f08-35be-8c77-c74d1def33b9 | -12.57202 | -45.80432 | 2024-10-13 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30023871-bb8e-3f2e-900b-f930ee2aad16 | -11.93404 | -45.78843 | 2024-10-13 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f38da98-6757-37d5-ab21-0dbdf82b3bde | -11.93355 | -45.79192 | 2024-10-13 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9137258b-6d85-31ea-b0da-5f9b7be8ad8c | -11.92897 | -45.79571 | 2024-10-13 04:40:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71752bc4-9c81-3682-b589-3e7277a873d6 | -11.10355 | -45.91055 | 2024-10-13 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14dcf65b-7673-3bd2-b151-2155f68cc2b0 | -7.88859 | -39.15208 | 2024-10-13 04:40:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9b09cf3-8a35-3654-b1b2-499e9f64ea76 | -12.71677 | -40.21677 | 2024-10-13 04:40:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 859bc383-aba3-3693-a976-f5400a09d476 | -12.71629 | -40.22105 | 2024-10-13 04:40:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6d27e229-e605-3c70-8ab3-65ea08ba255e | -7.3868 | -39.14081 | 2024-10-13 04:40:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a800f506-d88e-32be-995e-694315a03d13 | -7.38678 | -39.13755 | 2024-10-13 04:40:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25fb09f6-194b-30f3-9d4c-299aaec2563c | -7.38622 | -39.14189 | 2024-10-13 04:40:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 40f19f4d-d5a2-3a07-951c-db734cac7953 | -8.66688 | -40.40993 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6439c082-7de0-3166-958c-f9fd90613e07 | -6.39043 | -41.59722 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 527ebbe3-7e2d-3b87-a9e9-b615d0f28f82 | -6.38966 | -41.60261 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 1fd15b3c-0cb2-3399-a787-d206cc5e3ee7 | -6.38633 | -41.59111 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 80d19374-9be5-3fa3-b114-641e32f7427e | -6.38556 | -41.59652 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f92a2cd6-f077-3414-a112-274e73bf6f46 | -6.38479 | -41.60191 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5b0dc9da-c321-36b0-8d29-e108f9a18b51 | -6.02186 | -40.44769 | 2024-10-13 04:40:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b246e8ef-8771-3355-a1c9-bba570b9c98b | -7.34387 | -41.1187 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 489ad4d4-bd41-3d9d-bcc6-cab20d9e892c | -7.34171 | -41.1183 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 02c6e3a9-37d9-349f-810f-914695702e7c | -7.33916 | -41.18884 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7475e99e-1b92-3777-90d1-57cb8c539ce8 | -7.33875 | -41.19176 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92333280-53ed-360f-aae8-fbd7249b8df9 | -7.33875 | -41.11806 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5147e680-f23e-3548-a2e6-fec744d4e913 | -7.33753 | -41.18865 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57e12fb0-34be-3550-a5ef-612ef365cc96 | -7.33714 | -41.19154 | 2024-10-13 04:40:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1deed48a-3a50-3301-a5aa-d195dbd1d16d | -6.74127 | -41.10532 | 2024-10-13 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dabfcb0-a9cf-3dcb-a92b-6ae9c9934764 | -10.51058 | -42.50716 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 72d595ee-15f7-3712-b91f-0c1832e16ee4 | -10.50988 | -42.51257 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| ffbc098e-8c00-33ff-9b3c-044909c2127f | -10.50572 | -42.50642 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| aa44bfa2-86d2-3a2b-aafa-2c4b954e2d6b | -10.50502 | -42.51183 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| f57e458b-ed57-30be-ac67-2b7f60bf2b8d | -10.50433 | -42.51726 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 8d9512de-a287-3be5-b49d-b8701704b314 | -10.50156 | -42.50027 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ff59803f-051a-344b-a94a-58b9e488ebeb | -10.50088 | -42.51628 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d3660bb8-05b3-3595-933a-e61f1c0e3be3 | -10.50017 | -42.51111 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ca6f3f1f-cad9-3386-a06c-6146d40e02e1 | -10.49824 | -42.49934 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| be9358df-88a5-3248-aed3-af84b75821ef | -10.49677 | -42.51016 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 9ba6f319-566d-3e7f-88a8-f9577ada1f87 | -10.49531 | -42.51039 | 2024-10-13 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d68f500d-9fcb-319b-96c5-91c97e0ac1bf | -10.2115 | -42.44494 | 2024-10-13 04:40:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cf93e4c2-64f3-3aac-8d6f-b09adf045bde | -12.12176 | -43.1846 | 2024-10-13 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 819dd2c7-ef02-329d-b9e9-70985693e744 | -12.11698 | -43.18418 | 2024-10-13 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9a0f341-a4c8-3118-9250-3e0e3c031122 | -12.11636 | -43.18916 | 2024-10-13 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69689824-7d7d-3666-ba0d-46d2a7c4dbc2 | -11.65242 | -41.73569 | 2024-10-13 04:40:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0c6a6e1-21b0-34b3-b8a4-a261808acdf7 | -11.04314 | -42.01677 | 2024-10-13 04:40:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c259e20c-1a6e-369a-8ae7-d36a1507b710 | -11.04275 | -42.01978 | 2024-10-13 04:40:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04547cb1-6311-3388-99c5-a7e1da0f3f3b | -13.14216 | -41.96198 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 536c5b53-a929-3d4f-9dad-8d591932de1e | -13.14177 | -41.96527 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6576b6ca-0d44-3a21-bf5b-3bdf162c6bcf | -13.1406 | -41.97509 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bf7e7893-e263-3033-a2f4-a166444dfd79 | -13.14023 | -41.97829 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbfdf95f-c61a-3024-bd2b-8d262e6e99dc | -13.13985 | -41.98148 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7ed67444-8b78-3dc7-b6d6-6ceb84db8938 | -13.13613 | -41.96799 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 50b86b22-5496-3d36-924a-7ab311715ffc | -13.13574 | -41.97128 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e09b3adc-be2f-302b-a324-f773ad1be17b | -13.13542 | -41.96904 | 2024-10-13 04:40:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README59.md)
