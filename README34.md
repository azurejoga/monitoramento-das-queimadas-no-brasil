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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cd9e4df-11e3-31b5-9973-233c41fe833d | -7.48278 | -42.13824 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85d3d1fa-4b85-3803-9652-5b35f1d91076 | -15.02161 | -41.6507 | 2025-10-16 03:49:00 | NOAA-20 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 110159ad-1b32-3b04-a79a-61973ae0e383 | -7.48688 | -42.13895 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7858096-062f-344a-9f17-041ba2df3214 | -13.04189 | -43.22186 | 2025-10-16 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ff7f67d-ffe9-391e-a70a-bf7d440a334b | -8.25495 | -44.09432 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b9a905a-ae46-3feb-8c28-d0f1a49fd717 | -8.19821 | -43.32284 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8985c647-3786-3839-807e-b5422ff49522 | -7.27822 | -41.96474 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd175828-0d45-3052-bd37-b8116f11bb79 | -7.94959 | -44.13641 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5de8807-821e-345a-ab59-8484acbb1fd1 | -15.08927 | -42.12469 | 2025-10-16 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c41a210-95ee-3846-9a7a-7dc110e9fef1 | -7.00911 | -41.95369 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 93da54c0-6b6e-33d0-95b5-f5febcbacb1f | -17.07445 | -43.78641 | 2025-10-16 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3571da5e-b4d6-3fd6-9620-d0b9c64ed97b | -8.24573 | -43.33543 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4680227e-6da2-35cb-8561-cc72e95a37ac | -8.19832 | -47.00914 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01ba1b63-11b3-301b-b5ea-c90c87a0e97a | -7.57546 | -42.69061 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9731314f-51ca-3cc2-a8f4-64572504f70b | -7.34306 | -43.86964 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a196b00a-a38a-3f0f-8cb1-0f1f3bfe8a53 | -6.4947 | -47.22874 | 2025-10-16 03:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c7e7e44-4aa8-3ba6-a35f-7e92fc843846 | -7.27943 | -41.95757 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abcf0268-d50c-38a6-9682-66de0c2f64e4 | -13.27427 | -42.40884 | 2025-10-16 03:49:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1d66288-7d16-3ef6-bdce-ae6f0089930d | -7.94785 | -44.14616 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0f183b4a-abc7-3107-a385-79593bc18a9d | -8.25244 | -44.10884 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80094ff2-5665-3894-9581-d89a641b89f6 | -7.67683 | -42.55463 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2880aed1-9c94-3b4d-951b-fd050563b390 | -8.48287 | -36.69864 | 2025-10-16 03:49:00 | NOAA-20 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 76757d15-6c7c-3e37-98b0-29043d6e4c57 | -6.9483 | -41.56504 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 892f511c-cc41-32c9-bab5-f609ac6807c7 | -12.23952 | -49.3904 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0ffc83d-294b-3100-b71f-35e9c9bff71a | -8.46412 | -44.19229 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5facb0e5-4ae3-3a71-a91a-799bf0b7771d | -17.65155 | -48.33626 | 2025-10-16 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e12b5498-de8a-3409-9e63-c381016e3f91 | -7.07751 | -41.94205 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a6761672-0229-3ea2-ac3c-906098e6f429 | -14.75463 | -42.39215 | 2025-10-16 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dd03f266-f734-36b6-bcbc-0ef7032fc037 | -14.88452 | -42.13691 | 2025-10-16 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c91116f-e595-3356-b74b-5558bd9fc4cb | -7.4727 | -42.14791 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd5c1f52-5824-3114-b3b2-1af055539837 | -7.39265 | -39.69394 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab38e743-13c5-3872-972c-ed7127466d8e | -7.48028 | -42.15303 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 713c5236-e2a9-39d4-96ec-f63a0cdc31f3 | -13.99065 | -41.79145 | 2025-10-16 03:49:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4225c818-e335-32dc-826d-0cf23667f186 | -7.66211 | -42.59181 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d61c681-cc45-3228-a84b-3f2b6c513c3d | -8.26394 | -43.36095 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8731f84d-a91e-3141-91c1-f4b8fea3712d | -7.46699 | -41.51527 | 2025-10-16 03:49:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 225e247b-84b3-339c-8cd3-3cb2d3022f55 | -7.38932 | -44.74923 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 75e97e56-7e83-3a20-90a4-387758265bff | -6.90928 | -41.85035 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9fd958c-31b7-33ce-80be-67538769d615 | -7.95888 | -44.13815 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c11723e7-f618-38c7-8d88-3fa6772d0b13 | -8.5578 | -44.58964 | 2025-10-16 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98cc4f58-ce5d-3db3-9e62-059248271547 | -7.94872 | -44.14128 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4cc55fe6-486b-373f-8c36-fd5694438d90 | -6.82823 | -42.77486 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7b6e513-9956-3fe4-9e34-ac4f99456383 | -8.2545 | -44.06947 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ba589b-2303-3464-b15d-f3f960604fa9 | -15.58072 | -42.38674 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6af0efd8-80d0-3869-90ae-efd74b39730b | -15.96716 | -43.01624 | 2025-10-16 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 59d405b6-364b-34af-81c1-92d3b8eaddf2 | -8.19435 | -47.01221 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a092362-b1cf-3b88-a215-586f0b4ea305 | -6.40456 | -45.35711 | 2025-10-16 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae674167-f7cb-3f77-9684-12a689294ca9 | -7.67532 | -42.56587 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cbe5a4c5-9721-3f79-8cff-b680fc3e6375 | -7.03271 | -41.81084 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18d3e563-f53c-3d78-a530-2ad0af47f53b | -7.2725 | -42.94906 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5e96657-d356-3fe7-ad53-cec7efda4f59 | -15.36344 | -39.85081 | 2025-10-16 03:49:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32c68bfb-2b05-3613-af44-53f05e67db7e | -6.11215 | -47.29213 | 2025-10-16 03:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f504acf1-8d59-369f-8086-2cd0bce80ace | -13.96102 | -41.72289 | 2025-10-16 03:49:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d3c922c9-9cba-3539-b1fd-082cf9dbdf79 | -18.47144 | -46.83689 | 2025-10-16 03:49:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c2df55f-c95f-3eb4-a05b-294500d45b7b | -8.45954 | -44.19119 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 092acebf-a983-3e93-b9e2-5f4aecd637f8 | -15.59233 | -42.40745 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b609047-2a8d-38bc-9be2-01c597d490a4 | -15.15765 | -41.28212 | 2025-10-16 03:49:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 700a9a95-19df-3fb0-b6af-b6cdc7ad4232 | -13.56265 | -43.56374 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d8c4146-5d4b-3f16-b08c-d11d44ca271a | -7.34787 | -43.86231 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1e5bc71c-7318-3b39-bd40-21ac1c1f097b | -8.46687 | -44.19586 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 59ab72f0-2bda-3546-bc62-4adea1ae66d2 | -7.93889 | -44.12748 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77793dac-4123-3b79-9fa5-00f758d474ac | -18.58296 | -47.47079 | 2025-10-16 03:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56e2fd19-497a-3bfd-84ae-6bfd00e9a558 | -7.28098 | -42.95766 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| acf9eae0-0e7b-360d-82a3-dbf32dc6c31b | -15.9663 | -43.021 | 2025-10-16 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| fc055b38-f0bc-343a-b9b7-b67dc5c1d260 | -8.29371 | -44.96917 | 2025-10-16 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0673ef32-513c-3127-b524-30c185652560 | -13.27674 | -44.4808 | 2025-10-16 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb281e19-a25b-3e5a-a5db-e85e3712900c | -6.62525 | -46.83526 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d6fc5d3-a8e5-3cd7-8e0a-7933583444f7 | -7.16586 | -42.49742 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 97445839-4835-3e81-a589-a43e40faa917 | -6.94885 | -41.5617 | 2025-10-16 03:49:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3136b774-c60d-3b3a-94c2-f6c937766ed7 | -7.26054 | -41.74532 | 2025-10-16 03:49:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| caa8bd7c-11fc-3665-a8cc-484361decb6b | -15.59392 | -42.39833 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 20beba80-9278-30b8-a758-3c1a219c71db | -7.53333 | -44.28594 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e841aa9b-d87b-3766-a618-679c47edd019 | -19.02908 | -47.51846 | 2025-10-16 03:49:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f6a7d1e-0045-3094-ab73-d900a49b28c6 | -6.53469 | -44.69215 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f3e6707-fbcc-3e0b-afdb-6b934ebed534 | -8.19129 | -47.01566 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ddabdb7e-184e-35ac-a9f7-5890c2c8a973 | -7.54066 | -42.06899 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79758f85-eb50-3aac-bccf-674987bd05f1 | -7.67255 | -42.37514 | 2025-10-16 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbd7b1ff-11ed-38a7-ae25-dc9ce59df58e | -8.24134 | -43.33467 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2f24ac35-a7ac-33f8-ad8e-adf036bea4dc | -8.46587 | -44.18216 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f1f0df80-12cb-382b-9851-73fb20b4589d | -7.2073 | -43.6433 | 2025-10-16 03:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47179c5e-7f89-32ba-aad7-9b9639011dd4 | -7.13724 | -44.38629 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1fba12f-17b2-375e-8a7f-d7e10ff8a0c0 | -7.60925 | -46.47737 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49db7ea0-839f-37a7-9004-aedc826765ec | -8.55398 | -44.58354 | 2025-10-16 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d14fcf6b-295b-3be0-8825-3f17c48a3805 | -8.46965 | -44.18793 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f376b048-11dc-303b-929c-0ef8627daf94 | -8.29512 | -43.4136 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3f59298-9f65-3b75-bb5f-297775e9615b | -7.54245 | -42.71078 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 24c47003-b1f0-32f9-bb27-62fceb604ae7 | -16.53339 | -42.37333 | 2025-10-16 03:49:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76ec966f-4dda-326f-887e-f0cd9596a4c1 | -7.39129 | -44.74925 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8dff62a6-a31b-33da-b6c7-3a77422f9658 | -13.71972 | -44.00047 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f96255bf-7477-3981-a353-e3d8843d1443 | -6.94537 | -47.74363 | 2025-10-16 03:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a65425b-75b6-3414-8d7e-6a974a9556bc | -7.93424 | -44.12665 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 60e90fa2-c711-3329-a0eb-580ca88ec152 | -14.0117 | -42.14822 | 2025-10-16 03:49:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 82662147-74fd-36b5-90e2-2e7bae279f68 | -13.89779 | -45.57198 | 2025-10-16 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff98d08a-1da7-3134-b96f-b3c124062d01 | -6.45616 | -44.57825 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d45b6a74-6d5d-39bf-952c-3f88cb0501f9 | -17.61065 | -46.68365 | 2025-10-16 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcabb9d7-4045-3e1a-aa03-da6bf1491a6d | -6.90522 | -41.84964 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5dc16dca-adfd-30fd-b269-be1b20940561 | -8.40252 | -46.26488 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a512d4a9-fb38-3939-be06-9295e9efbc85 | -17.20934 | -47.65247 | 2025-10-16 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a44a019-1e5c-38a1-b3a5-a98fb4b4de4e | -8.07208 | -45.43164 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f16cf8-57de-3204-8422-d1187e71f09c | -7.94966 | -43.27021 | 2025-10-16 03:49:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README35.md)
