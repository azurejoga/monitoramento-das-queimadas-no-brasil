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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c7e2eb7-375a-39d0-ac5f-d495c389351d | -5.65632 | -45.14325 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b6393b-66af-3bd5-8570-2c24d4e52b04 | -8.07628 | -47.32512 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca65b49b-58a5-3d18-9670-281371a82386 | -3.69833 | -49.5466 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92f533b8-6289-338e-aa9c-7425938c2641 | -8.1758 | -45.0688 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d71f45e4-8d5e-3f8e-9541-15383f6c9692 | -8.21971 | -49.56601 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a2f725e8-bbe4-357a-995b-d5a12979445a | -3.82568 | -54.1143 | 2025-08-25 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0fcee12-3e31-3b14-9d71-6cce65897e0a | -3.73292 | -48.92953 | 2025-08-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71079614-0730-3e6d-acec-3cb28e34d267 | -6.9178 | -43.77415 | 2025-08-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c18ad94-5f34-398c-b94e-6c4799ce1397 | -6.14007 | -44.39208 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbd8408f-fe45-31df-b453-7b08f3cdde4d | -3.42886 | -49.04655 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a03024ad-cd8c-3dd8-af6e-e77463f71b3b | -6.44555 | -44.60526 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eda84c5-f7f5-33a2-b295-f0d59a76e15c | -3.59132 | -49.42622 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b5b05b6-e532-3a8b-b6e5-26703b960f50 | -8.53291 | -48.845 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d42b71a-7558-38f7-b5b6-69167e2a99d1 | -7.67388 | -45.39677 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e01be9e4-bb25-38c6-8e23-0bef459a7c20 | -5.10498 | -43.20657 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3e412d3c-1da8-370d-8c29-ae48332c4c7a | -6.41363 | -44.68415 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b512b37a-fb85-3891-9068-0cc4de7fb7bd | -7.20805 | -49.61365 | 2025-08-25 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e959765-79b7-306f-bf09-e3612d22745f | -6.3127 | -43.76998 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf99814c-e918-3cbf-8ee1-ea6dc5f6d07f | -8.0633 | -49.69332 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1315cd94-3c1a-3f2e-9b23-ff6602d317bd | -6.43284 | -44.56246 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 083b7a8c-eca8-312a-8bd3-86bb11e2c0ce | -8.80376 | -47.31078 | 2025-08-25 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb1fa0ff-d7fd-31ee-a6a0-61e2ad67c00e | -6.0389 | -46.63976 | 2025-08-25 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 797c912b-b5d5-3cff-8616-616a2a7bc3cb | -8.06124 | -45.01754 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70bf2c34-c6b8-3903-ba23-bd1f4cbf786f | -6.4993 | -43.1232 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf556925-5678-31c3-b67a-85224e44acf8 | -6.43005 | -44.55838 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec6315a4-023a-3cc4-890e-926a0d6fec41 | -7.60889 | -45.2313 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0ca3bda-0a04-3d9f-ae8d-2d8b36562557 | -7.84819 | -49.99947 | 2025-08-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 340be308-ebc4-335d-88f5-a44cfd924fc2 | -6.50585 | -42.95075 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c973b5a5-ae03-3e3d-9ad5-a3e313acedfa | -7.65962 | -45.39845 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5adcad93-6a86-3437-88bc-2bd181c21e47 | -4.29209 | -48.26525 | 2025-08-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b61e86d2-ec70-3f05-a240-0de03a1dec0e | -7.47561 | -45.01623 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a5437dc-f97f-3d4b-863d-d9b127b2f933 | -7.47224 | -45.01563 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1318065b-63b5-3972-9742-ff6170d24b03 | -8.38286 | -47.99578 | 2025-08-25 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce475aa8-4546-3533-a52c-3b3d6f1878c8 | -6.14572 | -51.75581 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c960110-aec7-3cf0-a519-ecb48045fc94 | -9.53102 | -40.31491 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a545102-88d9-3d9b-9ecb-e6c868769ba7 | -6.04257 | -43.99451 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba0f8e63-e55f-3fc2-b737-a8ea273db1dd | -5.63171 | -43.44853 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95a69567-1acf-3ed5-a9ca-782e171c2c73 | -7.31815 | -44.53267 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d5eaae0-2109-3042-a8d1-8cbe36919a42 | -6.43733 | -44.55581 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62fab2a2-fa65-31f7-ac2d-8665f0d3a8ca | -7.07443 | -44.63564 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d37500e5-2bac-31e2-8051-7dd824a74073 | -7.17672 | -45.16674 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1eca08b-fe1d-3b48-96e9-0335a8e85f56 | -7.93949 | -45.9296 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8985e663-9eef-3aa8-9791-efd238a99f86 | -5.70151 | -43.11399 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b7cc4bc2-9365-3e6b-b71a-162911cdadf6 | -4.1754 | -40.72139 | 2025-08-25 04:14:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5cb1007d-bc0c-3bd8-ab8b-3343da0e6740 | -7.30862 | -44.53135 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57b1878b-c922-3efc-b2aa-ffb4e4637cac | -6.03207 | -44.21224 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a80e64-63ab-3023-a5a1-3b11656401bd | -4.68217 | -43.08288 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c6f7066-39e8-3976-b24e-430a2500911c | -5.66095 | -45.1363 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95578b3d-d178-3934-8681-a5fc3f928363 | -6.4362 | -44.56297 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62aa4d53-55af-3d36-b57d-e71161859cfd | -8.06472 | -49.68494 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 471f09ea-5421-3b15-bfa9-207071e7a867 | -7.30554 | -43.66546 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7da4fe09-e65a-32b5-ac96-98702ae6bd7f | -6.79783 | -44.31933 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6874e46f-f891-3536-b059-0d458c48bcee | -5.6414 | -45.14856 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 722f3ee7-9c84-36a0-a1a1-95ab4488d7ed | -6.29409 | -43.86668 | 2025-08-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14b98f29-799c-35c0-b518-1843358e987e | -4.77371 | -45.32983 | 2025-08-25 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c4bd816f-bd8c-30f8-880f-efbc4376840d | -6.68099 | -44.4129 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3328cbd7-b3f3-3029-9a33-ec566558de75 | -7.65762 | -42.67073 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c4d899e-2b08-372d-b899-654517f7ee10 | -6.3083 | -43.77639 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52f3d06c-75e0-395c-9a44-3788714fd798 | -7.33094 | -44.5383 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 288b02f2-c8bb-3607-bcdf-188026881d8b | -8.90883 | -48.12741 | 2025-08-25 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 769f178d-a7cb-35f3-8d50-5e5e9ac71b81 | -5.73553 | -45.39589 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f18ffdff-a0bf-35ac-8c44-a37c3d93f27d | -6.87719 | -45.65522 | 2025-08-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35e98794-c3dc-34c8-b700-5244207c2f37 | -6.05643 | -44.7907 | 2025-08-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dee05e6-adc8-3958-924a-f9222f7afeeb | -5.73793 | -46.15304 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d584beb1-a1cb-3943-b2f7-fea4c86d5b58 | -5.62786 | -43.45147 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41aaf3c2-9029-39e2-999b-8e78030335bc | -6.89359 | -47.931 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7acff10-ca9d-3b28-8fde-dd5e47c29ac8 | -8.54202 | -48.86473 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2512a424-678e-35c4-a33d-56b5b9fe3b4f | -8.54442 | -48.85046 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24c0f36d-8650-351d-bf01-3fc3773214f8 | -7.09526 | -44.6285 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e98674bc-3d9f-3bf4-93b9-97a9ee4af667 | -6.12891 | -44.37587 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d9c3148-23c4-35ef-a10e-58ed5250994f | -6.02706 | -44.22231 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd45db8e-1c53-3c52-86d5-7bc4168a2346 | -7.92367 | -45.89548 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecf38a3f-3c6d-3e4e-9876-8bec9e9750cb | -6.21162 | -44.98719 | 2025-08-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ced09336-f61e-3cbd-a2f2-cf9a2f50e122 | -7.89408 | -45.90261 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938ce41f-9d0e-3702-892b-2a0338596aa9 | -6.91725 | -43.77761 | 2025-08-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b22a49b-05d2-3078-b26a-588636883906 | -6.90511 | -44.41268 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6642476d-f646-3b81-87a8-bf49d2d6b35c | -8.38531 | -44.94829 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c96b4bbf-2f6c-32fb-ac60-1c1c0163c7f9 | -7.80878 | -46.62536 | 2025-08-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c748c599-0049-3bd0-9e87-69935476c027 | -6.22453 | -44.11325 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19e66cd5-a510-3899-8282-ba5d7175c2a7 | -6.24481 | -43.74871 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67f42881-9b20-3a4e-854e-10ed4cb6e0f0 | -3.9387 | -55.75587 | 2025-08-25 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b0e609ad-703b-3f2c-9d1e-ba3d600cc243 | -4.96598 | -55.82107 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85498fec-51d4-3de3-96af-532c846d2cf6 | -8.05012 | -47.33135 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e1577d6-57f5-3882-93c4-8c9360242144 | -6.45416 | -43.71406 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b60fe7f4-fa43-3021-8eb9-53b1660b44ab | -3.42465 | -43.96112 | 2025-08-25 04:14:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f410ecb9-d3c8-3b0a-b942-25f21a9a1065 | -3.45091 | -43.34204 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e61614f3-2812-31c8-9a0a-80282ef07c10 | -6.05305 | -44.79015 | 2025-08-25 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8842d83c-96c7-3bcb-a4a5-59ac65089837 | -6.32257 | -47.65602 | 2025-08-25 04:14:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fac8b33-b751-3e41-84f7-ee932393c3ae | -6.45449 | -44.61393 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 76435cbc-76f3-3e0d-be41-4fdfad6ade54 | -5.80965 | -44.99599 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acbaab53-fd75-37aa-9182-5af6ca157db2 | -7.54105 | -45.22058 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f622286-a2a1-349e-b079-191b08f60d68 | -5.52941 | -41.28941 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0296b28c-2172-346b-b16c-6145b785184b | -7.28753 | -44.47013 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd0051b6-ac7f-38f9-8059-b72ae489d443 | -6.32803 | -42.49614 | 2025-08-25 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17c1f843-85f9-397f-a5c8-c1f78b06a5b6 | -6.32417 | -42.49911 | 2025-08-25 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0add16f-a97f-341d-9742-00dc7a83c11b | -6.05625 | -44.44444 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da5e6838-da00-39d3-90c7-b9ac7b20e51d | -6.43397 | -44.55531 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abd3a191-38d2-3dc6-8307-fa438881242c | -3.42891 | -49.05142 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 380ffb30-6534-3690-ae95-3a9200630c14 | -8.06185 | -47.30597 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8785eab2-a7f5-34e3-b191-1e24373390f6 | -2.26305 | -47.85347 | 2025-08-25 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
