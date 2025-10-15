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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 829fb364-24e0-3d7e-8718-8ad639ab232e | -7.01562 | -41.95481 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0b0bb29-8716-3333-9258-1bbe3f042332 | -4.76897 | -45.74068 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7fe295dd-5849-327f-adf6-6ea968c1ec83 | -3.83507 | -44.55244 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12e9087b-a6cf-3006-9abc-5e6b0501f38f | -5.91177 | -42.65046 | 2025-10-15 04:06:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60ac7558-84c3-3a14-8481-af90e356ef75 | -5.51524 | -43.86497 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14818b67-0383-31b1-a4e6-25da5e8aad6e | -6.58079 | -42.95755 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7d73da4-3bae-3a5f-b6e8-b65e12530929 | -5.42812 | -44.21802 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd1134bb-2ce4-39a4-9d2c-570417691845 | -9.37988 | -44.61433 | 2025-10-15 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43651732-5630-3a99-808e-cdec539bc354 | -4.76981 | -45.73557 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a9dbc75b-3c9e-367f-8063-d48b1cc00727 | -5.38393 | -43.22461 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22646d5f-b47a-3299-a27e-37b3c20fbcbe | -6.91274 | -42.23867 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 414b079a-a9fc-3f56-823c-4b8badf80a19 | -8.45243 | -46.20063 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b257d7a3-6669-384f-8085-32884abb3be0 | -2.86129 | -49.16756 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 977b62f4-fbab-3668-a4db-913e45bb67dd | -7.49152 | -42.14498 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1aedfa2a-3713-373b-b7ac-3542e96b42ee | -7.50489 | -43.05983 | 2025-10-15 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e02afac-3b63-32ec-87c8-993a41c00a38 | -7.00181 | -41.99892 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6bc670d3-fcc5-30e9-8d73-4629fc06ac5b | -5.16546 | -45.17094 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40f71ac1-0c70-388a-9d3b-bcfaf6458344 | -5.49232 | -43.78343 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62fd3850-9eca-3f25-94a6-949fe63477aa | -5.98541 | -42.91183 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4ee11cd7-6a5d-318d-9ae5-bd9a9707e52a | -4.14079 | -42.21011 | 2025-10-15 04:06:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c00cf9ad-1d61-34b4-b98e-ba7e8c531b5d | -8.21752 | -44.05217 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c673844-fb8d-388e-83c9-cca31fc43da1 | -5.9222 | -42.82286 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0b3a5741-14d9-393c-80a0-3a71c5023d2c | -7.94676 | -44.13673 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56b48179-c7f9-346b-a5df-e3b917319d8e | -5.43395 | -44.22751 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b8f72689-4b3f-3420-a30b-9863a2b22f3b | -6.22313 | -42.49455 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1a6f2021-1b57-37de-8e16-529edd69abf0 | -6.17603 | -41.72147 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4bf5ed88-69e9-33a5-b1fa-b9b1d06d80e1 | -7.07526 | -41.96426 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70e413d6-4a7e-3563-9840-976c943c732c | -3.07312 | -49.51687 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c96d7a61-ed5c-3884-b8ec-4ae240f02be8 | -4.11095 | -48.02611 | 2025-10-15 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b3cee9bd-3a48-3abb-8059-d0c7827b1e6e | -4.49369 | -44.72734 | 2025-10-15 04:06:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bc1d198-4690-3850-affc-16f54f9ffe28 | -6.02998 | -43.39513 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e5ef124-df26-333f-9ea5-a93489261d89 | -5.33558 | -42.56346 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 207a954b-8e7f-3a55-8b85-b986e602d6f1 | -5.61645 | -48.26511 | 2025-10-15 04:06:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e48f5798-2ddd-363d-9016-6d165cc87f17 | -5.87833 | -42.79329 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 12a923a2-f00d-347e-8de7-4f1d7df34d79 | -6.12592 | -44.27768 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56aa3cc1-8a0c-3db9-a910-5429c26d3e28 | -6.45883 | -41.8872 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0924e06e-5343-3793-8221-13f9995a17ff | -5.9517 | -42.31662 | 2025-10-15 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25021dfd-9acd-3f7b-95f9-4e5a30416a8a | -5.91146 | -42.82479 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3ce0df27-99d1-3db1-b92b-4ae7d82e56ae | -4.89587 | -43.46327 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bb410443-7b08-32bc-8d9d-900faacfd779 | -4.64821 | -43.1337 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 02957abb-79d4-32dc-844a-4288a16ef56b | -8.73283 | -43.86227 | 2025-10-15 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63e0163b-5c37-3fe7-aef8-560feb84fa9c | -6.2542 | -44.02322 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a21d86ea-7a0e-32c5-834f-2ab629cb9291 | -5.67629 | -44.25591 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ea3207-aa9d-3423-9525-9902e85fe3a6 | -6.52422 | -42.20197 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe56569e-ab02-3e93-b6f1-ba70d794cdbd | -4.98821 | -43.44643 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8db57dac-e25f-3600-96ec-0236a9c504dc | -4.65981 | -43.12777 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a28f2588-39eb-39b5-9537-1bc087a6fa9c | -5.32624 | -42.90987 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff925098-8d9e-3dd2-8f59-d43cefb47770 | -5.88731 | -42.88842 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93a853e1-bf3b-3f96-9c42-2ca4bb068078 | -5.90234 | -42.83832 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55243961-6654-3d24-927d-318a3d1e808f | -6.18984 | -42.59559 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b83e94d-27b2-3f17-80b6-6fc4cef909b2 | -6.45995 | -41.8375 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d3c87bce-0fe5-31f4-98e9-54b4dc902055 | -6.17689 | -42.61191 | 2025-10-15 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0b8afc05-7d02-3872-8b3c-2fa02b2554fd | -5.87919 | -42.83092 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e8f5c0d2-bfef-3fca-a847-42c5575af322 | -8.20773 | -44.00319 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7e017bf-25db-3ddb-bfa7-ec783bc34c74 | -6.15616 | -41.71832 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11862e01-d621-3ef6-af1e-62251f09b937 | -6.9985 | -41.99839 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60c93a0e-5d0b-3ecd-be25-07cde3eadc59 | -4.83947 | -42.77297 | 2025-10-15 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc789878-2d2f-38b3-b55a-f672cac57a54 | -7.08461 | -41.94796 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f98dd59-f409-32b2-ba92-69d690e45d40 | -8.21594 | -44.04006 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b7c1ba-13f4-38f3-a454-b4bc9685b138 | -5.46986 | -44.64655 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee107db5-0c4e-3216-81bf-260e3f80b81a | -6.22304 | -47.03741 | 2025-10-15 04:06:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51e9201f-46c9-33b5-8d20-0b2a17e2a7e2 | -7.57256 | -42.70277 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62eead1f-a979-37e6-a4ec-15e4e2f3a837 | -8.22228 | -44.08863 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78be958c-f1a4-3552-a8a2-4fbb4db7daf1 | -5.86308 | -43.86564 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ecd0e97-6077-3776-ab2e-805b31d25d44 | -5.43891 | -44.21986 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 87b0d93d-abb2-3bba-94cb-1e104784027d | -4.25213 | -45.58485 | 2025-10-15 04:06:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d43eb357-1112-3d77-a42a-37b7fd1370ba | -5.34283 | -40.52061 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2b97b72-f526-3617-8126-d5216277f826 | -7.08133 | -41.94741 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da72e091-115d-3dab-9464-0f28782c5a23 | -5.90352 | -42.83096 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bbc08d5f-d755-3cf3-84c1-b254f9eae518 | -5.48972 | -43.79929 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c07cff-685c-33f0-a1b2-872733f13484 | -6.7796 | -42.13545 | 2025-10-15 04:06:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a4c4532-0632-30ac-99fd-bfa8844b5bd3 | -6.24039 | -41.55073 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7cbc02d4-31fa-3eaf-997f-94861f17e723 | -5.5647 | -42.99688 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8aab116f-8b03-37ae-8ff6-98652dd469af | -4.39956 | -43.61864 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14245425-817f-35ca-9208-3d8e1ba3c90a | -5.35079 | -43.40667 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29698be4-7c64-311c-87e9-4144b96a14e9 | -5.00422 | -44.49465 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f2de8a1-cb3e-3b7f-99ba-41f88e9c1ccd | -6.52754 | -42.20253 | 2025-10-15 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 56218772-c373-35c4-94b5-0c5e332afa04 | -5.33327 | -42.57795 | 2025-10-15 04:06:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f76e092b-a246-3a4e-a5b0-5faad70493cb | -7.51448 | -42.95736 | 2025-10-15 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9fc0b0a3-4536-32df-b239-c15088df0e0f | -9.11506 | -44.67944 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d64800-2335-35fd-bae1-a3162e65dab8 | -2.94666 | -49.33727 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1241d0e-068d-36c2-8693-e71be6134753 | -5.41663 | -44.22041 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 412af61a-bcd7-317b-a8db-fcf1b50c2e62 | -7.07637 | -41.95731 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c20d2a78-c72c-3ecd-bbf1-39e6ef01660a | -4.87572 | -45.77675 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f7eb2bc-1e2f-3424-8d70-534864806d36 | -4.30683 | -48.23722 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48eed477-20d0-3cb4-a3bc-748b05f13d16 | -5.44108 | -44.29698 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17716889-6936-32f4-8909-27ab2a96dbbf | -5.61162 | -42.72589 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58c102c4-a183-34c5-aeba-a50342cef7df | -5.15055 | -45.69653 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33cbc914-041a-3c77-a9b8-a9247eed5fb6 | -7.5657 | -43.89499 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af38737-dbb7-3c16-80ff-bd75c7953704 | -8.45484 | -44.19357 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 324125e0-6b35-3de8-83cb-3dbb2b7b14d6 | -7.5636 | -42.71589 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 927233ed-dc30-3092-9178-17a85f73f989 | -4.79196 | -45.32956 | 2025-10-15 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2437ba90-e773-35e0-8721-ad0ef4a97fea | -5.95798 | -42.86625 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2018b192-9af0-33bb-b5a3-ad86857da168 | -5.95618 | -42.31007 | 2025-10-15 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| faaca30c-74d7-3299-8fa1-cba2b164dde5 | -5.65112 | -45.87828 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aeb2c511-3bd8-3746-8f50-e1dd924631bf | -5.58876 | -44.74498 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed70d641-c4fe-3dbd-8d12-664d13a4c9ba | -6.76623 | -42.81178 | 2025-10-15 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2047bf72-5fbc-3cc5-8e62-94212d2428ff | -5.32002 | -42.90503 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6457f6a-313a-3cab-8fd1-aaca4371c578 | -4.39892 | -43.62263 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feeb955f-5005-32ff-b885-2a4699d4a5e9 | -4.89522 | -43.4672 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README31.md)
