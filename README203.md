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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 053c3464-36b2-3662-97dc-d754f966e2da | -5.74536 | -43.27614 | 2026-10-07 16:37:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4199acc7-ab86-3bda-91e4-b063abedce4e | -9.78403 | -47.81003 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e45ad6f6-e042-3da1-b77b-28160973c7cb | -7.18296 | -44.30751 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c2498ca8-8c0a-330a-bf4e-ac118e1675b9 | -11.11073 | -45.68887 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3f2acefe-214b-3d7e-a746-894bed724adc | -6.56289 | -46.03817 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 54c81f2c-8862-3e01-8688-f173f3403d05 | -9.37477 | -46.26202 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d9f6b62-ef5c-3b77-9775-3da35602c0fe | -6.22203 | -52.84882 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 15fef04b-c9d3-3253-ac6a-5c01672e10fd | -9.03683 | -46.90649 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49766df5-e52b-387e-b459-595a5122db60 | -5.89065 | -57.75488 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c9ef0a6-6a48-37c5-8776-277476d6052a | -5.21425 | -48.33977 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ec7050df-818c-3d16-b480-01f404e293a5 | -9.93557 | -46.80574 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0472f848-b8cd-3450-bc46-a879e83df348 | -17.02517 | -45.92029 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ded9a267-342e-3c36-a13a-235cbc1beb31 | -11.38068 | -46.66795 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0677264-70ef-3560-9e9e-547f7befeaac | -3.7715 | -41.7878 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 948b2559-4abe-3dcc-95ee-ebf70fcb8634 | -4.05553 | -42.21503 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 4bb2943f-d40e-3a97-8807-b92869915b54 | -6.22464 | -52.8294 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| aa4260a0-be97-311a-b62c-3337e2bca1b4 | -5.27476 | -45.72686 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3948a737-4f54-3aa9-8fa5-c86698fb2603 | -4.07676 | -47.30093 | 2026-10-07 16:37:00 | NPP-375 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a57d7e17-2f89-31e8-b5e9-cc9ed9c28207 | -6.82811 | -39.54438 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 62ce1a87-4f64-3580-987a-13f76bfe7a11 | -8.54127 | -54.5878 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1f1c7fc2-49c2-3bed-b96d-33e3b5a4c56b | -3.89707 | -44.11154 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73fc9fab-ccf2-31b0-8b59-b4f0bb9f0950 | -8.19173 | -46.33928 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1dbc54f5-80b6-3cfd-bfd9-b319ee2458d7 | -5.74255 | -41.70396 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 13fe394b-20b3-3a8b-890a-3db8a7aa9613 | -8.82545 | -47.55093 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 7f597dd7-f846-3d50-aa49-359bac172a19 | -6.02785 | -44.11689 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 5782a938-cef4-3a36-940e-fc727e47a253 | -7.20974 | -55.10314 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| a4b527cc-8242-373a-a8ad-574ea94b81e0 | -6.60928 | -35.11081 | 2026-10-07 16:37:00 | NPP-375 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7f43dabd-910c-3074-a83a-7d4323714c1b | -5.78235 | -52.36458 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4311929b-e7f9-39d4-a880-7621d788ec7a | -9.51758 | -46.84357 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b66103b-1c52-3615-a562-8daeb3fb07f4 | -5.79304 | -43.75336 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3d99896-94a1-3439-a691-4099c6cd5c55 | -6.65027 | -43.7874 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3b2193be-7aa0-3daa-aec3-f0aa72ba860b | -7.77263 | -48.24275 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e4df1517-4aad-337e-b786-bf19f7aedc76 | -3.67841 | -40.39132 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| a96ccec2-a163-352f-b15f-86fddd9862ac | -8.45905 | -36.82741 | 2026-10-07 16:37:00 | NPP-375 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 33857b48-30a6-3040-9007-516ff643d74d | -4.78746 | -43.3342 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| da0828f5-29eb-3ac5-83b1-3bb4d437a03c | -6.8618 | -41.80219 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2055e2fe-61d7-3cba-beb1-02d97153fae4 | -15.11427 | -39.92435 | 2026-10-07 16:37:00 | NPP-375 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0f1f0a46-e5be-3b73-8f88-35d4a88db715 | -17.01536 | -45.91906 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 309f9dcd-b5dc-3ec0-b867-7e73e1f9627f | -5.74049 | -41.73633 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 906b1607-a8ed-3a6d-ac10-c56d295515c6 | -16.02857 | -48.24423 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dad76711-16d5-3478-8026-856315550e46 | -6.08617 | -53.73114 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 43c8fe7c-dffd-3cda-af6b-7b4ee1ab1281 | -4.10545 | -39.16261 | 2026-10-07 16:37:00 | NPP-375 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d3b5f4ba-2117-3f7f-a718-68832c33b30c | -8.26035 | -54.71791 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 48afa310-e267-368e-af75-e4c195876c44 | -6.68449 | -52.95195 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39679cec-e06e-346a-9425-dbe453c6895b | -3.77222 | -41.87425 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 8b34f6a4-6ce9-3bd9-a2a7-b3d5d063c398 | -3.77817 | -41.64481 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 96219870-7cdd-3cce-aaf5-9e742cedbd1c | -3.76099 | -40.83247 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 43e65207-f2d1-3f66-948e-0553d5a53a25 | -6.15244 | -47.12452 | 2026-10-07 16:37:00 | NPP-375 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03a6faca-acb3-38bf-91ba-6520b346834b | -6.67563 | -41.76862 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c6ee65fe-60b8-3a09-976b-af5281a1b206 | -7.47563 | -42.82589 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 43f96505-93ee-37c1-adc8-3cf9a97d1289 | -6.12228 | -53.05639 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 234b10d8-441e-3aaf-8cd1-74d2acb7ba3f | -7.76295 | -43.79385 | 2026-10-07 16:37:00 | NPP-375 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a17cf372-2e86-3526-8ced-d510d3c411d0 | -3.69943 | -40.83526 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 20b40377-d202-35e8-9bc6-8e964e6f69ba | -5.40814 | -45.64098 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4db19122-8460-3e5b-99a4-b784ad81ab0b | -3.53192 | -44.84159 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| adbc419c-57c7-335e-bd88-5e8bdc33ea9d | -7.77322 | -44.90604 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39c2f015-f885-3e6c-85b4-ca5e2d87f0c7 | -6.04678 | -53.49306 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d687f9e5-c118-3413-adcc-922cd4383aae | -5.49902 | -42.84071 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 9cce3818-0d10-31d1-95d6-5689046c4948 | -5.37521 | -44.16049 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4382f4a-5814-384b-bc04-c51068295bd6 | -11.01349 | -47.97642 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| be2f09e2-df48-3ca5-b00e-50c8918b66ed | -8.21054 | -50.18624 | 2026-10-07 16:37:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| de2e3089-776f-31b9-8df3-c624faaa2d24 | -10.17882 | -42.51143 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| f83e090e-ffa7-3c85-a97d-619252f4b523 | -16.1595 | -43.63016 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01f4d390-2d81-34ff-83d6-a6a3da28ddf6 | -5.43122 | -45.6339 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f1bcae34-aade-3ad1-aae8-daf456774879 | -9.94101 | -43.55684 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9808197-ed5d-3561-8c25-b121e4e2cef3 | -6.27437 | -52.84317 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 365942ad-0a04-3d1c-8957-dd5cda0f6728 | -7.00521 | -44.05383 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5dc75fe1-e308-3285-9ddb-3a5ed1981512 | -9.12077 | -45.10557 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 692e477b-b2f3-3503-9941-735ea563ce66 | -5.04412 | -49.76738 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 33d48e87-f7a9-3c10-9b04-eb57a897320b | -4.07851 | -43.24907 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af520003-1a58-39c6-9e86-68d81e3cbc1a | -6.12757 | -53.05571 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d0d2b5c9-37a9-3cda-b0c7-41135229fb66 | -5.9581 | -46.37457 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 21605541-82c0-3fcb-a8c0-f529b43578e7 | -3.80233 | -40.46628 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5553b567-cb11-3cc2-a7a4-d42ec05bd8e2 | -14.68873 | -41.15212 | 2026-10-07 16:37:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a1cb572f-4aa7-3314-b32b-fc8dbaa167be | -9.93431 | -45.7333 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c0e5ebb0-853f-3c52-8779-e6e5bc70a575 | -5.74235 | -41.67997 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9b4bd51b-b3f5-3d8a-a485-b95f55711734 | -15.7205 | -40.69875 | 2026-10-07 16:37:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 05d0fdaa-e56b-3966-9342-b733edb0156e | -7.77254 | -48.24067 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 31a07bea-1626-31dc-9b46-d3c950507c3b | -3.36257 | -43.33642 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e5f0f5c8-9421-3570-992f-c82cc6152b29 | -4.37175 | -38.52477 | 2026-10-07 16:37:00 | NPP-375 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4d68efe3-f8a2-3971-922e-1acd05f69407 | -3.21573 | -42.81517 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 408ad72f-7425-3d7c-b7a7-f4f3b999e3f6 | -3.40479 | -42.93024 | 2026-10-07 16:37:00 | NPP-375 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 01a51870-4183-30ca-a24f-44d6e401f950 | -5.73965 | -41.70841 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4926b426-1ec3-3d5e-871e-61cbc8f44952 | -6.90061 | -45.89974 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bcb8a2df-b412-3d07-b9e7-29c5dcfa0020 | -5.83984 | -39.69809 | 2026-10-07 16:37:00 | NPP-375 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 252b2005-5a35-34cd-ab29-468cbe7e10f8 | -7.12203 | -44.06426 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46709c35-5bfe-3d23-8148-1dd65758bc68 | -3.55063 | -39.47333 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abb4bb22-e612-391e-be6b-dc6310d0ce4a | -6.60412 | -37.88565 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 22507f3b-1c48-347e-9fd4-3660a85d7e8a | -3.19214 | -42.61837 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 76ad5eff-0d3e-379a-8d16-55757f494220 | -10.51777 | -47.28178 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 88f528a3-87bf-3c59-960c-a8f9efed60da | -7.80967 | -44.58814 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5508490e-8141-342b-8452-4ca37ad631ac | -6.21377 | -52.82756 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| af8a4e9e-64ff-33ac-9ccd-934239201172 | -15.26127 | -39.27927 | 2026-10-07 16:37:00 | NPP-375 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fd5cd36e-873c-32a7-b678-090a5456a3bc | -17.1947 | -43.52161 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 759abb1b-bd03-30da-b627-04b561b7c7c0 | -15.53522 | -41.24697 | 2026-10-07 16:37:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.1 |
| e8d3d253-48ca-3109-b284-3abe56bcca9e | -9.97304 | -43.56622 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2b1456a5-b860-3636-a684-aa357d644c66 | -6.25493 | -53.45805 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 79f237fb-55d1-3b22-a265-9e181403e3a8 | -6.62157 | -37.88305 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 0a854815-414d-3e79-b98f-37c1708144cc | -8.12312 | -37.39869 | 2026-10-07 16:37:00 | NPP-375 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| aa77c489-31c2-3e86-9b0e-52dd37038748 | -6.15368 | -52.65937 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README204.md)
