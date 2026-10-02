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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a0cd94-dbcd-3491-a140-36ae444e521f | -4.2812 | -50.77464 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9863b56d-e120-3f6f-9008-38a4b42e3f87 | -4.27933 | -50.78555 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b5ba1a6-72f5-353e-8f7c-ba2868974afc | -6.00693 | -45.78097 | 2026-10-02 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e1cbbf4-f349-3bea-944c-6d0555d9d122 | -8.56359 | -44.13266 | 2026-10-02 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42b94122-0cfb-3847-8669-5e015183cfb3 | -8.61461 | -49.46825 | 2026-10-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 868e63bd-343d-3cba-9f2e-ea0564285a3c | -9.51956 | -45.32853 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a912971-4054-3df5-a1a2-27f9ed682830 | -9.81942 | -44.81533 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 749c408e-4ada-3b36-9dea-2be571f07f47 | -6.00599 | -53.54762 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 358276b8-ec30-3a91-8741-b1997325c6f1 | -3.28236 | -53.86044 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7701e86e-41ab-3994-962d-2164ca2f2cce | -4.25812 | -50.74525 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 852d5535-a514-3a00-8657-356cc4aaa2d5 | -8.32809 | -44.15666 | 2026-10-02 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61d210b0-950c-32e9-8afb-98f43057545c | -6.44228 | -51.70383 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 569670d3-9c67-33f0-bc8d-741d322891f1 | -7.4602 | -54.99 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e3dd281-a32e-36a1-8a9f-9e5d5e60b430 | -5.75156 | -45.14401 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ca5fc1f-1d33-3a06-9b72-3f885961eaf4 | -6.1292 | -43.7231 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 457aefa1-c151-3896-931e-067987796ca2 | -4.38311 | -54.83526 | 2026-10-02 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16911d0c-dbb9-34b0-a3e1-f4dea34b2ec8 | -7.83112 | -55.13113 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb80f654-4857-3063-8a9d-d9107277c865 | -4.25863 | -50.7748 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b00dde33-80d2-37c6-866a-25de49c4b50b | -8.78089 | -41.07951 | 2026-10-02 04:14:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7cc3fbe2-0389-3b17-90b8-e438c4559bd6 | -3.00248 | -53.88652 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| edc87d61-37b8-3037-87a0-4bba29d7e988 | -7.8756 | -44.17701 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc035aef-3b58-3765-869a-6933a9e742ea | -5.73991 | -43.28892 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c93f105-156e-3904-9e96-aaad7b8e3736 | -4.27267 | -50.75875 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2645dce4-4f8d-3ce4-95a2-46f513df46ab | -9.77998 | -44.80531 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc78ae2c-1d4b-3f8f-a485-90553c602fb3 | -3.01601 | -53.88898 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1554a042-94da-347a-a120-8e112e4c4044 | -5.5531 | -45.2609 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed8b69e2-06d6-315f-bf22-345db1a624bc | -7.58416 | -40.39049 | 2026-10-02 04:14:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c3befe3-6cba-3270-b739-05169f07afe6 | -6.20634 | -43.2879 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06f01c2b-bf8a-3ce1-ba84-39f00b5203e9 | -2.60615 | -48.25586 | 2026-10-02 04:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 838885c4-e7d0-3407-a820-381493fc636c | -9.809 | -44.81365 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dafb9c5a-3d75-3b70-b560-e663e93c7f35 | -3.27175 | -50.09184 | 2026-10-02 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 366d553c-b42f-399a-a2b7-a8040a784da5 | -5.7439 | -43.28582 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92f1ce09-d35c-3acc-9b2e-4ac8bf49cccd | -5.6755 | -50.0991 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95188fb9-bfda-32f1-8ca6-56479c86ca6d | -9.84552 | -44.85162 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9995b07c-1585-344f-a15b-14b744252217 | -4.26114 | -50.76031 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3edf3d9-0741-3e51-a943-cba4a4291b59 | -7.45847 | -54.98944 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26984f1a-8b74-36d5-8fcb-35c363812c90 | -5.58199 | -42.72728 | 2026-10-02 04:14:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 652ce1b6-bc9e-3cd4-9697-9b55b640ed81 | -4.28969 | -50.79093 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ca94cbc-f5ab-3989-920b-0cad571d2507 | -5.27398 | -42.63488 | 2026-10-02 04:14:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 192ba6ca-3ea2-3150-a459-418e01df3633 | -6.09485 | -47.67192 | 2026-10-02 04:14:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60317858-37c5-349c-8c90-9cab7d3e4727 | -9.83484 | -44.8299 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4bb0d81-0951-319a-9c84-47b138e2f5e3 | -7.1749 | -44.75826 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08bb8b76-7651-3336-b00e-470bda5228dd | -8.36453 | -45.50355 | 2026-10-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e06e3ca-f84b-3ac7-8b44-8446439b6613 | -6.92004 | -44.56466 | 2026-10-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9e18671-13f3-3890-acc6-973490c3c6d0 | -8.04063 | -50.11648 | 2026-10-02 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93cc1294-d47e-39ba-b179-bac1c81fb6a7 | -9.52461 | -45.34204 | 2026-10-02 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35af4751-9e1b-3e60-8bad-0ceee72ae428 | -8.97994 | -48.94215 | 2026-10-02 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0727b442-82a6-397c-a752-ad5be9a399c8 | -7.34683 | -55.58767 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3ce4d2a-3f25-3cd9-833c-0cc1fa467f75 | -5.88701 | -45.54369 | 2026-10-02 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9a31a4d-25e9-3f0d-ab40-967fdb7f6d4e | -6.33124 | -43.36005 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 07e28681-dc14-3158-a74a-01255e764392 | -4.25689 | -50.75233 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| afb43d6a-d089-3b70-94c7-c12da3b1e3dc | -3.29215 | -53.84352 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 371ab96c-54a1-3679-bb7f-2729bb5fd4c5 | -7.72209 | -54.75796 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cc20355-7354-3fa8-9393-95d090244bd5 | -5.87275 | -43.59403 | 2026-10-02 04:14:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad1242a8-99c9-3967-91ed-882cf443e9b2 | -3.28083 | -53.84371 | 2026-10-02 04:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| de36b9ac-a3b6-37fa-8b27-1c0a126bea6a | -2.92773 | -48.7524 | 2026-10-02 04:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adb32b7b-53fa-3b49-9912-136f81a37c90 | -5.97727 | -43.74918 | 2026-10-02 04:14:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a519ac96-b8df-3715-b971-16790d3d31fb | -4.27208 | -50.76219 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 577e4774-d5dc-3d50-8d03-2273339266c2 | -6.23378 | -53.13727 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16d3f7c4-bf25-3856-bead-3c7ca017b4fe | -5.72175 | -47.41826 | 2026-10-02 04:14:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7d56236-d05a-3009-9ff1-6b045c8d56c5 | -8.00565 | -42.91648 | 2026-10-02 04:14:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 248ff6d6-e65a-36a5-aca2-6dde5a49b7b5 | -4.26964 | -50.77635 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a711dd8-2bd3-3415-9222-6f39458b7955 | -7.83567 | -47.92289 | 2026-10-02 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58bd781a-9d8d-38a8-a1ee-9dc2d7ef368e | -4.92381 | -47.54555 | 2026-10-02 04:14:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e92643-032d-3eac-96c8-e4b489a36c77 | -3.74726 | -47.15195 | 2026-10-02 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564617e4-9b6f-38db-9180-41c1c7b8b029 | -8.04622 | -43.99262 | 2026-10-02 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba82ec03-5bf2-381f-b884-58e21cc90c54 | -5.14057 | -49.87167 | 2026-10-02 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df263da1-1502-3552-b1dc-efc4d90a1cda | -7.86588 | -44.17152 | 2026-10-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8dcdc1f6-fe82-3078-b4fb-c9454b08f3de | -6.20598 | -43.61575 | 2026-10-02 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1d469f9-8883-31e8-917f-79ee498e005f | -8.1585 | -54.80705 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 682fc31f-c58b-36ac-9c7b-fa000e8baf7c | -4.01757 | -48.94771 | 2026-10-02 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 415f595b-311d-350e-8225-d7639bc9c839 | -4.0629 | -51.0964 | 2026-10-02 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00758971-1c47-3fb9-ad29-e94140d91fdd | -6.24447 | -53.14859 | 2026-10-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 30160f4c-23cb-3047-ba72-d15df7b184ab | -3.33034 | -46.54852 | 2026-10-02 04:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b0e9e49-fb2c-3cbc-920a-7c3b10c0fd4e | -4.28543 | -50.78285 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bdd6087-536a-32a4-b229-23fd565669b7 | -6.71488 | -38.9971 | 2026-10-02 04:14:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c0c21a2e-eb8f-37c0-93af-43be71f2d3d5 | -6.31602 | -43.34636 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| caaf6909-e0ce-3a6a-825a-7fc91324cdc9 | -3.95156 | -47.63988 | 2026-10-02 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f0c5f80-eeee-3da9-b85a-c6a259ff10dd | -6.33649 | -43.37594 | 2026-10-02 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b97d9d2a-a3c2-35b8-a222-5f1146c03a75 | -6.92424 | -44.56127 | 2026-10-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25b901f3-e77b-3a3c-a6a2-183e92ccfc34 | -7.28021 | -55.59473 | 2026-10-02 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 20eb5da7-2fa1-3ddb-9144-85e44da9c9dd | -5.7377 | -43.28106 | 2026-10-02 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6cadeeb-95b3-3a48-b55b-206ca55c36be | -6.0032 | -53.55157 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c605b36d-77ad-3653-aa40-8d828b7f0731 | -5.86991 | -50.16183 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 69936b43-eb87-3314-b321-3c07c3cfc903 | -5.55699 | -43.96662 | 2026-10-02 04:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b20e878-da4f-317c-8886-fae9f73b205b | -3.06815 | -49.37081 | 2026-10-02 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b438ace-129b-36dc-84f2-82f3e2b96530 | -4.28481 | -50.78648 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acc3f081-b665-3e5c-9897-101c9531c816 | -9.78345 | -44.80589 | 2026-10-02 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24208309-c4b0-317e-a49b-1465ffd552e0 | -4.29152 | -50.78023 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6fd00ad-f33c-3492-a2ed-c95c058190ac | -4.26051 | -50.76393 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ea75586-6902-399b-836c-875ccf8894db | -7.73101 | -54.80279 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f40301ed-5484-325c-a518-19ff55423fe9 | -3.97808 | -41.51656 | 2026-10-02 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cf3ecae4-04bf-3c22-9e37-42c4cfab69c3 | -5.99214 | -53.55162 | 2026-10-02 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b14fb31-fd2a-3191-a01f-9c674acc616a | -5.76782 | -45.16032 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfbe4b3d-c294-3a43-b7c5-c89a75ede13a | -2.57721 | -50.00069 | 2026-10-02 04:14:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 592806cf-6d39-34c6-9f2f-b61ca944d77f | -2.87872 | -44.24654 | 2026-10-02 04:14:00 | NOAA-20 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c39fa87c-cdec-3d0f-8915-8941029a542e | -5.76414 | -45.15965 | 2026-10-02 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e53c360-e429-3575-a60d-14e2960674db | -4.27512 | -50.77726 | 2026-10-02 04:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53797a19-9979-39a1-8c0e-735a7c0d0611 | -5.86477 | -50.16106 | 2026-10-02 04:14:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a12e206-d326-34f5-b882-562bf2e1714d | -6.7425 | -44.14027 | 2026-10-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README41.md)
