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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea34bea-f269-3381-8e5e-249934ca573c | -6.2165 | -42.75965 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f1341f0-b958-39b8-9b57-ca795e88841f | -6.56467 | -44.21674 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51d7452b-3bb1-3a9c-b362-2d1331256e7b | -7.68173 | -44.99298 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 144fd5d3-2a9e-3471-8446-73c97ea8c125 | -5.61545 | -45.0016 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84738b24-6977-3a9d-8593-d48304259d15 | -7.59924 | -42.72968 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 796898b0-6356-38b2-82e3-61420b29b14d | -7.42482 | -44.81044 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fab835b-2648-3ab6-a9f5-4b2180a1f29e | -6.18516 | -43.32961 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d848899a-7052-38b0-ad21-d8e73e8a16de | -7.71879 | -50.28569 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2875f940-3f67-358f-9bfa-67cf97112480 | -6.82497 | -43.04781 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a8ab7c-4d4c-3f66-8720-f0c6c035334c | -6.20906 | -42.76236 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f08871d4-25be-38ad-8a00-4b314589cde7 | -6.53879 | -43.52335 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb09303-e1f5-3581-968c-1b16592d64ba | -5.85912 | -45.61682 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6a84a70-98bf-3881-9380-b61ec176102b | -6.39561 | -45.25617 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0332d3ea-5fa7-3ec5-9e0c-864872675f6f | -6.34595 | -44.46333 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 627da9b2-7586-349d-ab9b-2360d7dce1d2 | -8.34342 | -47.42384 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6aacf2-b899-3476-aae6-59e0ecad2007 | -7.09704 | -44.31431 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5ca7dbe9-71dd-3973-afae-ebdd3bb0c6ca | -6.77777 | -43.78545 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 55ce29cf-1a30-3ba8-bb03-2c18e1527408 | -7.40506 | -49.51875 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15dd5e12-ebe5-3440-a449-f682be86350a | -3.64513 | -48.45 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7dabeb8-d3c7-391c-b70e-36ad651669f9 | -4.87405 | -46.85289 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26d379ae-ba52-3543-9502-0dcb16e9863f | -7.38212 | -43.39221 | 2025-08-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c42cbb6-5a3a-3686-a4e2-2ea7c205f721 | -9.31506 | -40.21623 | 2025-08-30 04:19:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| de09cf7f-490a-3df2-9874-c97238d27ccb | -6.37862 | -44.3407 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e79cb520-b36e-323b-b443-1ad88ee9cc61 | -5.70252 | -45.95746 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8076611-82a0-370b-8136-81109d0676df | -7.62247 | -42.72904 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6a3def6-a592-3a5d-93f1-bd4469688f59 | -7.60967 | -42.73131 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 55ee4f32-81cc-3ea2-ab1c-af5c31329673 | -6.0257 | -42.81551 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f0287b7f-0ccf-3ca7-a17a-96048f84efd3 | -7.12039 | -44.60278 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fbfc8303-fea7-34a7-a145-34b36f117a1a | -6.66387 | -44.38844 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 150a2efa-b22b-3886-9e6d-667dd02069e4 | -6.91644 | -44.38201 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f42821ed-a54e-34e0-a3cf-36011b2ad34b | -7.01492 | -42.02164 | 2025-08-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35cc0d65-6765-3d4f-a8ca-1f0df64da192 | -3.22072 | -46.82831 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80103db5-ed9c-3985-862d-1f8dbaab504f | -6.27884 | -44.48124 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcaf0596-9f05-3024-8902-1ca1efd15f42 | -5.8771 | -50.29344 | 2025-08-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8f891c1-cced-3e6e-b947-35f828322ae0 | -6.5995 | -43.64219 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ad58a75-907b-31e0-a806-2feb62126c07 | -4.14049 | -38.27093 | 2025-08-30 04:19:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a163a83-d199-3afb-81dd-4feb904dda06 | -9.02702 | -40.52511 | 2025-08-30 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 94ec3805-25a1-3750-a833-23632006ba18 | -6.78446 | -43.78648 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1902271-8085-3c7d-965b-f4a9d649007a | -6.78501 | -43.78293 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 82415558-6941-30a2-b7fd-8c1bcda90a29 | -8.17636 | -45.05006 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fca53ed6-4592-356f-acb6-854c9eaf7184 | -7.63577 | -42.66351 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0e7fc52e-6611-3004-9607-6c26b901cd57 | -3.07031 | -49.45866 | 2025-08-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8151bf1d-ff83-3100-83e9-0773b3e70e03 | -6.3089 | -44.41859 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d123c2e9-56b1-3b20-9813-42e7fbf2fab9 | -8.15536 | -42.30672 | 2025-08-30 04:19:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c235eb1-d750-34ca-b791-84b53f4afa07 | -6.36287 | -43.56556 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db528b11-7bf5-3930-9af2-5a08e364da2b | -7.7615 | -45.46306 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1bb8aee-65d5-3faa-bc1a-da3f70a7fae9 | -6.5145 | -44.84323 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a344009-dd97-32de-887a-552e8776c970 | -6.57504 | -43.68943 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001b37f7-d136-33e0-8363-25726f613cbb | -3.73189 | -48.93942 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f876f5-3582-3510-9bbf-fbb8514af50a | -5.75869 | -45.36816 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db20f89-59e9-309a-95ca-b3eaf01a543c | -5.6986 | -45.96049 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4612ed12-34e8-3759-9545-9f81a7b2f461 | -5.55071 | -42.64166 | 2025-08-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9afa0836-6e76-3b79-a379-08d7a26bc1bf | -2.58644 | -51.92321 | 2025-08-30 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 966477fb-9446-331f-adb7-1610ef584390 | -5.54258 | -43.74636 | 2025-08-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9b52f92-412f-3c6a-ace9-8733cbda9ee8 | -3.49282 | -48.94824 | 2025-08-30 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab8d23d-c5bd-3be0-ad0e-de8910d45e7f | -7.59411 | -42.69318 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 82b717e0-4345-3fd3-bbae-533cf0c9fbbb | -7.58249 | -45.12988 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0690bc6-793d-3533-94bd-f0bc3e73f2b4 | -6.69371 | -43.08142 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d045fe0a-c4ef-368e-9f95-33118ab13a84 | -7.10019 | -44.59961 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ab1b0a1-3fa5-3aae-9dc9-ca3329fc2b4b | -6.49909 | -43.54315 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cb764a4-9526-35b2-9c77-ba90534da6b7 | -7.15523 | -45.16428 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 722ad49a-5a66-3125-8ea3-4c11cabff040 | -7.43528 | -44.80853 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b3154d2-0f6c-3d81-ab0b-4adf1a4452b6 | -5.7244 | -51.6837 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4120b908-7482-3f8a-af00-0bf98b7b2f4c | -7.05793 | -43.81783 | 2025-08-30 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a070f89-6a1b-3d5c-a297-918732ca63a5 | -6.48848 | -43.54511 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 746a4e31-fdb8-32d7-a119-9bfd19c5ed5b | -4.65278 | -43.62936 | 2025-08-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b51779-f2b6-344a-93f9-999c9b516ae2 | -7.62472 | -42.66583 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7952756e-3578-39c5-b0c2-db6c450b5ff3 | -6.17675 | -43.33941 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 2ecdba09-d3f2-35be-8329-63ca0832c906 | -6.22719 | -43.82751 | 2025-08-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ada981ba-834e-3cf2-af98-ddcc1b9b6d4b | -6.57169 | -43.68894 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 169f33ef-4fe4-393f-b655-63dde76ff15c | -6.52565 | -44.86261 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12848270-cb32-34ae-92b5-982c191a3272 | -4.10598 | -52.4667 | 2025-08-30 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd84d426-81fe-3918-ae4f-5f98ac5a5876 | -7.59175 | -42.70872 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce8309d1-0f7a-323b-90e3-126e04778b00 | -6.24523 | -41.81787 | 2025-08-30 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65e8d5a4-2bba-33fc-95db-61b325f7cc01 | -7.08315 | -44.29425 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67f1564c-5dac-3970-a794-651ae7b7bf7f | -3.42031 | -49.05104 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c5d1cc0-d0aa-3e8f-a5e5-56c6f32e0c1e | -2.98454 | -48.60717 | 2025-08-30 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0d9686e-7db1-380e-a3f0-93fa7c7b5447 | -8.30635 | -44.91454 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1bfa8af8-5169-3ab6-895b-0c9ad280f894 | -4.41637 | -47.60896 | 2025-08-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c22160b3-af37-34ef-83e9-3bb2b50d5d1f | -5.73075 | -43.9368 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d1b8c5-b794-3b44-a9a4-75dd44880c5f | -6.27545 | -44.45945 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2835d4b1-6484-3963-8502-30e3d0e3ac09 | -5.13796 | -46.23327 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27a928a5-c03a-348d-a9dd-1c25b35c9737 | -6.17015 | -44.17284 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23539619-aa2c-3234-842d-a72981a6b862 | -7.15955 | -45.13666 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e2c78f-8a01-315a-9a67-d1e79e0be624 | -7.61493 | -42.73187 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c827113e-d45e-336e-98de-f811499224a3 | -8.24024 | -45.0784 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f80632a4-27bb-349b-9cec-ce76462c27f7 | -7.0948 | -44.3068 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a19ebebb-f92e-3f3e-9667-f1787f9e1fc2 | -3.3833 | -44.11718 | 2025-08-30 04:19:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8052768-10a3-38c6-b608-02bfe2559e27 | -5.99592 | -44.72259 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9489362f-d73b-34da-b08f-cfdd1afc33c9 | -3.85351 | -49.28909 | 2025-08-30 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76ae0a0f-e2ad-3b03-874f-24782a25909b | -7.60855 | -42.71529 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3feaa5b9-7845-363c-9784-0b9396f5c421 | -7.34598 | -47.53008 | 2025-08-30 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12375f0b-3301-3c29-b495-a9bc671a41cc | -3.09043 | -40.10415 | 2025-08-30 04:19:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94c6aa01-6f7b-3e3b-81b6-e014b411be2f | -5.9245 | -43.34116 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42d3104c-cbd3-3982-8ac5-6b30c3945ab4 | -6.17338 | -43.33887 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be8a87a7-1c93-3e9f-8d86-0ace572510f9 | -6.29487 | -42.79834 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be7fd504-e08e-307c-a1c6-f57fbca18e3a | -5.79598 | -43.73553 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 476ad898-4e0c-36db-926d-c4228e971acd | -7.90779 | -44.78704 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a93d7d0-6393-36cd-896e-6e797624b234 | -6.21363 | -42.75539 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ff46a56-f3eb-3375-9570-8db4cfa858c6 | -7.16841 | -44.46793 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README21.md)
