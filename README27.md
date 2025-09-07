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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16ab6491-36ca-31f8-8680-d1012fba8e04 | -11.00452 | -52.05141 | 2025-09-07 03:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bd44c8db-281a-3c33-bec8-549f3d69611b | -7.32993 | -43.93803 | 2025-09-07 03:57:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 724fa724-268b-360e-8a39-dd81425666d9 | -11.8096 | -48.2388 | 2025-09-07 03:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 890685ee-153c-31dd-8ed4-1c65e1b891ee | -7.74074 | -48.8237 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ab4431a-c6bf-32f1-92e6-82639a96b845 | -6.27026 | -43.49836 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e4be66-0811-351b-a4ee-42d084db96c9 | -11.57007 | -47.74752 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fc35a88-1c8b-3070-8118-f90feb43c578 | -8.35324 | -48.27107 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f4b3c87-889c-3ba0-a802-6b50743e5c53 | -8.30607 | -44.98387 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7faa6dfc-5b46-39e9-b5eb-4f64072661a2 | -7.01525 | -44.97528 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01e21654-aee2-3bbe-88cf-4c39a18e3fae | -8.29892 | -45.389 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 562c335d-ee7a-3c07-ae69-76020a172295 | -11.58837 | -47.73281 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b33d03a-8238-3c58-b6af-783fee1593bc | -12.92449 | -48.03598 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79b2287b-e1cf-37da-950c-576928f7ae98 | -6.52062 | -43.06873 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c33e81ed-85c0-30f1-b49f-957eeb9da143 | -8.11469 | -45.31326 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb972ffb-3b4b-3b9c-b83d-0d8091713ffb | -7.0147 | -44.95224 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6972a7e1-01c5-33b4-9c0f-e7ed0af8ba87 | -8.15202 | -44.86081 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3da8c317-94fb-3f0c-a6d6-c6c49ed47e97 | -12.82559 | -48.01572 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc78dfca-5f11-3c54-a909-76c216cd0a63 | -11.59467 | -47.16187 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a94bbb9d-a118-3c46-ab7b-24d90a74c1a3 | -11.23924 | -46.44377 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56079c25-43dd-38eb-b603-9ce38979e658 | -7.413 | -44.97459 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a45b4cce-5d9a-3aba-ab8f-a40dd0b0ca87 | -6.34125 | -43.80099 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea68d92f-3fef-382c-8692-63e9d2e995be | -11.4099 | -43.63835 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 468b2b0c-b39b-30af-861b-00fdc898b210 | -6.55885 | -42.96138 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3a3c35f-3fff-3bea-b35c-70ae733c0ff8 | -11.39628 | -43.55775 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05ed6da7-f494-3d9a-b304-fdc0cf2c9a87 | -8.68101 | -45.3069 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 702ca092-81e0-3d55-8a51-167ad8ca6f72 | -13.62723 | -40.90734 | 2025-09-07 03:57:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9e2a134f-86aa-302b-ad9c-1a0b0545cc50 | -12.61692 | -44.63044 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96a2d4a7-40ae-37b5-97b0-188e97ed034c | -11.61841 | -47.16101 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12c851d7-a4ad-372b-bd90-0ba0da074419 | -7.34587 | -43.9447 | 2025-09-07 03:57:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b39bd61-dff1-389f-a4d6-b25128de2e49 | -11.15308 | -48.37174 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfa16d42-9ef1-37dd-80ea-b0ec522963f8 | -6.2288 | -43.29607 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8867c34b-cf92-3315-af43-464c7f0fef80 | -11.94106 | -46.66549 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e38eaa0-c81c-3563-899d-20b8bbcfe682 | -8.91309 | -45.82323 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee1d09f1-fa08-3376-8620-08dccb3ddf7f | -6.5605 | -42.9514 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8075c062-c8fe-3c52-b351-563a47565db9 | -9.70955 | -49.49072 | 2025-09-07 03:57:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01d95c96-a2b2-3fc8-809e-ccbe92327833 | -8.49583 | -45.1073 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6cd5c9bc-26eb-3930-b4ba-8dde1a67b3e7 | -8.18378 | -44.78067 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb493d6c-3006-3f55-b42d-bfc146583b61 | -6.19968 | -43.59162 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebe7c7b2-935f-30d2-82de-9a8ecac8a013 | -8.17873 | -44.78409 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17b539c3-419b-39d4-90a3-f8d70688a51c | -10.57912 | -48.47457 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1247071-ca5b-31e6-a10b-da4401319428 | -12.84558 | -47.99089 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11fdb3f7-245c-3e76-98a5-2752c441041b | -7.84739 | -44.93303 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8971314c-70d8-3ee3-a23c-deb11e1c465f | -11.35501 | -45.57734 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a54e832-b171-36ba-bed1-243a60741b08 | -6.24275 | -43.51167 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 390c137a-3c3e-3f47-9a22-85344271cfaf | -6.20276 | -43.3753 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| decc9b10-124e-38c3-a7ef-30396a1200c8 | -12.91249 | -48.07106 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91eaf1c2-0e09-3357-98bb-380d668e3cc0 | -7.67671 | -50.29279 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70711d9c-3383-3c93-9a95-ae9fd305c3ec | -6.20077 | -43.36817 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b33686c4-e5e9-3ab3-853a-39221a1d2753 | -7.45431 | -42.03395 | 2025-09-07 03:57:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85c778e1-06e2-3ab4-985a-21b98588011f | -11.84065 | -47.57032 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d16a9434-9e3a-3cec-9120-9abb3f30277d | -8.93279 | -48.65033 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38853dea-2ff5-30b9-948b-94ac4306121e | -8.34022 | -48.28069 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 14f9df12-b594-3e35-83d5-31d1f04af259 | -7.01683 | -44.96629 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8fa0bdb-0563-39d7-a294-6709b3b26c19 | -12.81939 | -48.02147 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a02e1e5-57a8-3f4f-907f-df76d6999233 | -10.08932 | -48.09464 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f821b2-7c07-315d-8b17-8f1a4235947b | -8.03162 | -44.03637 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 380e6ca0-0639-351c-9aca-4b29891a8208 | -11.31388 | -46.54829 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3207946e-c07f-3684-9e5f-a7c29f33a3fe | -7.28657 | -39.21676 | 2025-09-07 03:57:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 292bfa66-9fea-3eec-a2b4-cbf1f59fb34c | -10.10445 | -48.16003 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 041adfb2-6120-3279-96c7-b84c4484dfea | -10.15054 | -48.74292 | 2025-09-07 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 591c4139-3484-3020-a35f-75b3ba5a3c1c | -6.55739 | -42.94575 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d3401b4-1a9d-310b-bb4b-d6b73e790cca | -11.26223 | -46.39525 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04c76506-d4a4-37c9-afe6-76426b3f5c40 | -8.93205 | -48.65417 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3953e2cf-f298-3fb7-9478-8cd52ace2236 | -6.88381 | -45.60311 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 704583d5-a8a9-36cc-932f-054034fd4094 | -7.63806 | -46.75869 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 827c3b02-57e7-3667-baca-ef8055639a02 | -11.14857 | -48.36686 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb913fba-90e1-3863-8773-f3d5bfe4e92e | -12.01129 | -47.77928 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7181614-0356-3093-9062-fc2a7442476c | -8.18813 | -50.13954 | 2025-09-07 03:57:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21d77952-8d61-3e1d-b6c8-eabb7716b2f9 | -11.82881 | -46.76737 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4005088f-48da-3ce3-a98c-4dbcfcd05a3c | -6.31624 | -43.29544 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0646c73-7957-37ce-9cd8-8a9d82dd274a | -6.89485 | -45.59481 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a12a4a1-b865-358a-84ca-83ca7deb406c | -7.01761 | -44.96183 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30dcaf63-270d-300e-b406-d526228ba10c | -12.82065 | -48.0147 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b05e49fb-87f0-3683-9347-5effab1b3170 | -6.22459 | -43.56966 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f43b9b2b-24e8-305e-9658-aa0176368e23 | -8.48499 | -45.17709 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62c66105-7f56-382d-a155-2994d1218dae | -11.57733 | -47.73662 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e0e01a0-5d47-39f4-afa9-7fec71a638ba | -8.43927 | -47.30532 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb721006-0eb0-3dad-8c98-1df24a0d0017 | -10.78327 | -48.27096 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2cad2c4-fdcc-33b6-83ce-dcce66a7ddbc | -8.91849 | -45.81936 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e20bc45f-3007-3945-bd61-96cdd2c0b900 | -8.01681 | -45.44724 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e42c40a-7955-3767-9fff-260d17bdb21f | -8.29333 | -47.43407 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddd402df-ece9-3b69-b24c-0faa2b713c89 | -6.19554 | -43.37456 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64a1f0ae-518e-3731-a063-34a5edd7762d | -12.80339 | -48.02454 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 7656877b-ee77-3839-848b-074fedc1e39b | -12.62065 | -44.6095 | 2025-09-07 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35b974f1-27cd-3304-8b86-735085b7ff5e | -13.06254 | -48.06852 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 923690be-433c-3679-a6b5-415c97fec07b | -10.34763 | -46.46148 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9b1d2d52-bdbf-3fec-81a4-74b367f2fc3d | -6.20019 | -43.37172 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3227c64e-f905-3651-913f-29e9284a5f86 | -12.93937 | -48.03909 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2a95d23-ae58-37e0-afce-737639be5479 | -7.83784 | -44.93589 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47e0ec61-714f-3eeb-81f5-4aaeef2ee447 | -12.55124 | -48.07937 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7af8fb98-fd42-356d-9522-f50d74b4ecae | -13.39836 | -42.4147 | 2025-09-07 03:57:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63d0802d-2254-3a57-a3d0-976a26991ef8 | -6.387 | -43.00271 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aec2d61f-b220-3a78-b0ff-8d707a703a8e | -10.80734 | -47.73516 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efd64284-16a4-36d6-98b9-c4a2c5918e36 | -7.6126 | -44.67777 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 827be04b-40b9-30af-b145-e0c17adc7826 | -6.83472 | -46.39756 | 2025-09-07 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79631247-ad13-331a-9f92-56caf5166cec | -7.85986 | -47.87143 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42ee5851-dd02-3b60-ac3a-0c553a1c475a | -11.39846 | -43.56782 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63b21098-5a8d-34c3-b380-8bc16a4c7a92 | -6.21848 | -43.53045 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6290a7a7-8873-3bd7-b47c-2fddf84b231e | -7.01316 | -44.96098 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 034a0949-7284-31cb-a5e5-d40350d05b0a | -10.73792 | -48.59949 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
