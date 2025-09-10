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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce34cd5c-5528-3afb-a11a-1357eb2b5b21 | -8.28146 | -47.46363 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 745a3fb1-eb14-3c15-8da0-df3902b651cf | -5.56458 | -45.11586 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f44d185-5a29-3299-b230-f66d11fc756a | -5.74314 | -47.46455 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 93fd1c78-372e-3b5a-8b22-8afb0120c634 | -7.54876 | -44.65511 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40de56c6-17af-32ed-a9f6-aac8642713a9 | -9.45226 | -46.70272 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1b4215c-ccee-35ae-b78b-7592f30ce5c5 | -5.96377 | -45.80779 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc7217dd-5898-321f-ae91-f170b243fb78 | -6.16968 | -42.6486 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee38a6b2-1648-36c2-8878-30a403a59f92 | -6.25536 | -43.40837 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ad534988-72cc-361b-a155-38570faf7e41 | -5.37539 | -45.94739 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 766e6881-025f-3fe4-ad86-7edb7a92b809 | -6.09589 | -44.78061 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ae70836-ceff-35d4-8e73-b9e55fdba751 | -6.56155 | -43.14561 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 636801fd-bba1-3c85-aad1-4a3f06190672 | -7.79109 | -46.09533 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a69cf68a-93e8-3eb7-8425-b457e419a211 | -5.67524 | -43.35147 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20b4b1ba-28c8-3e0e-83ea-917648ec2276 | -7.70607 | -44.84114 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5ac75a2-a883-3fa3-bebe-b455fc0dd661 | -6.77483 | -43.4552 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b214538-147e-3f5c-9bfd-a5a6a3778f69 | -8.05004 | -48.67843 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f3280ffa-9c80-3acd-a070-58034735ab3b | -7.70863 | -44.73917 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c491e3e-5448-32fb-833c-d78660b231f8 | -6.18846 | -42.6586 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c56d8f6e-e1a6-3570-943f-9e7dc9263118 | -8.51533 | -45.70887 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1fbc021-9923-3e43-b1ca-5a7fb3ab1fe5 | -4.50016 | -47.82314 | 2025-09-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a991100-991e-3375-8a1b-7fa280f4daa0 | -5.90528 | -45.79034 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 664ec1a9-c719-3b8d-bdcc-e805fcee1658 | -6.86866 | -43.94217 | 2025-09-10 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3805720-4830-30ae-a8cb-9f86a33e2532 | -7.25985 | -44.45999 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9929b898-7afc-33f9-8041-c92377f00f4d | -6.87982 | -47.89854 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5bfa271-2457-307a-9667-e16a269546e9 | -5.63085 | -42.61355 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d060e560-50d1-36ce-9cc2-721bc9840c93 | -5.62291 | -42.83846 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20be9077-ae60-3a5f-9569-1390bafe9f1b | -7.54771 | -48.21663 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 982fc776-353e-3d9c-8177-34a2febeb577 | -6.25505 | -46.11884 | 2025-09-10 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a2f3ab8-eb78-3f91-bb10-95f80c77522f | -7.38571 | -48.17429 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3595a34a-31c7-3b3f-8422-5bb6e318fbaf | -7.76038 | -50.76273 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 637b72d1-2317-3995-9647-3a35f4ff75b3 | -7.73866 | -50.7312 | 2025-09-10 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 260837e3-39fe-3c62-acf0-45a78a24b1d0 | -5.41746 | -43.45544 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77d407d4-65f0-35cc-a082-08a7522eaedc | -9.06932 | -46.97247 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4025824-ccbf-33c6-aec1-85ae3cfb2f37 | -7.10863 | -43.88753 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709d5803-a8ec-3148-badb-14ba836b5972 | -5.86487 | -45.30127 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f41d1bb1-018b-373f-9bc1-f879669c0f48 | -9.08829 | -47.05814 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88945c54-4d94-341e-8757-d7daeb4e81e6 | -5.64684 | -42.61959 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d9fe54af-5a33-370b-8741-442deb4bfa83 | -6.85836 | -47.93098 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c331164-4a7b-36cc-95ed-719b403f41c3 | -5.66702 | -43.90066 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97fba424-368a-322d-83a8-653d6c1f2d35 | -8.05927 | -48.67273 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 726ad20d-63ab-3846-bc54-31876b4f778b | -6.3501 | -42.60203 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49806a26-a60c-3a62-b04a-454653296e49 | -6.52164 | -42.92012 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201cd673-d26b-3e75-9024-8521c02b8437 | -7.56325 | -44.65012 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d839043-2c8a-32e6-8b05-1d3f4c28012f | -8.16484 | -46.07067 | 2025-09-10 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cdff5a-819a-3b7f-b782-235abd958b30 | -5.64577 | -42.62651 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 80099c7f-5c16-3f95-83a8-232265986f09 | -8.34619 | -45.05412 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57d72ff1-1e92-303f-bb41-580b4d5699da | -4.48167 | -48.11456 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b05f965-c4e1-3ae7-9a50-058e4afff75a | -5.90247 | -43.66039 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155f3ec5-c9a6-3ca6-9e26-bd128051ca57 | -5.12319 | -44.66863 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1f57a1b6-249b-3d7c-ad98-16fe5736c562 | -9.06725 | -46.98489 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5004795-b42f-3ccc-897a-b4c4b2cdc790 | -8.42724 | -49.11678 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8298ba1-94d3-3988-8851-e05b2d776f1a | -5.64461 | -42.61215 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b045994-9b3b-34cb-9af8-43b16ffe11c9 | -7.27634 | -44.56777 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a831e2c-ce32-3e71-b360-cda3866134ee | -8.49784 | -45.66341 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e822e02a-655c-35f4-b461-3a7333b35ca7 | -6.46339 | -44.11641 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704faff3-b62c-3773-9ffd-28bc2d4c74f3 | -9.45091 | -46.71085 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f828c83b-741a-3647-bc6e-8a02163546fe | -6.25475 | -46.11773 | 2025-09-10 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59501734-c78d-3d0f-966b-47806f47efaa | -6.17883 | -43.39581 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d41a5be8-adb6-383a-8d1a-0966106804ea | -9.15888 | -45.57199 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84aaa087-74d4-3ba0-96eb-d91681b4ad2f | -7.77799 | -50.77127 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aae4c0c9-40ec-3558-bb5e-1c4d1177a8e0 | -6.25482 | -43.41182 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4c7ed94d-04fd-3b03-8c73-326d89d1d5dc | -6.20523 | -43.39991 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20488dce-e6ea-3561-b8bc-954269cc6e5f | -6.41513 | -44.40103 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6c1316a-ebed-3fa2-9203-1b741733b001 | -5.93802 | -42.7822 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9f31b8a2-f120-3622-ac26-a880fb214e6b | -5.71803 | -45.4117 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b22deb0-0a29-39c2-9860-318b3d044864 | -6.85121 | -44.91087 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 421dbbf7-5e77-33a3-865e-7e17dae3b8a8 | -5.41085 | -43.45441 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1db028f-ee61-3494-98cd-0557f173e734 | -6.20853 | -43.40043 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 587b0c63-fdb1-32f4-b213-4ede48282a2c | -7.56494 | -45.23791 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54ffe143-86ef-384b-95f4-ba0df38f9199 | -5.19662 | -43.0392 | 2025-09-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aedf3f1-840d-3b1b-bbdc-89f60f0e250a | -6.85225 | -47.91965 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1451c464-af79-395f-8505-a0055cb2464d | -5.40129 | -45.92238 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf834fc-d2c5-3cd2-860f-530e88102307 | -8.42183 | -49.12366 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a4ae459-e9eb-3579-bc54-1dc8c359ff64 | -5.42197 | -42.81766 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 164c5f0a-f0ec-3e55-9665-027248a179fa | -8.49725 | -45.66711 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ccc0cf3-0c77-3e04-be47-887fd4203c4f | -7.70961 | -44.77597 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 279acb53-0ca5-33a2-b00d-7ca47091e937 | -9.00859 | -49.53265 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c722dcfa-5262-36d4-a377-b14fdb3fbecf | -6.20496 | -43.50943 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8ef1f85-e395-361a-8da3-5d998424249d | -7.66812 | -50.26668 | 2025-09-10 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8dc49b8b-7c01-3f8d-b7b7-5ae5c5806452 | -6.16503 | -43.376 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f650dec-a35a-37d1-a5a8-9fbbe0026f85 | -9.44183 | -46.72183 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f1a4d23-5787-3843-a0b4-f4aeff851757 | -6.21687 | -45.63037 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03e19bbb-ce31-389f-bcdd-1139be5f4135 | -9.21711 | -50.52618 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b820dc3-4ade-3ba6-aa30-29ae592a4897 | -6.58485 | -44.01442 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abf41247-33f6-3e3b-92e3-2233d6ea8683 | -5.64631 | -42.62306 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9218c5d0-d902-3540-b6d5-9e2460d1e893 | -5.71506 | -45.42237 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8d9afb4-96e1-31c8-9aad-c8846cf43209 | -4.48655 | -42.9272 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c583b0e0-9d71-3349-b35b-ab3bd43ece44 | -5.7204 | -45.41142 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcf78aa4-1ccb-3abd-aab3-57d4ccaa6761 | -5.74141 | -45.28221 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 746094e6-b870-30f4-9815-e1945ed33012 | -8.38411 | -47.99057 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b4d33e6-2f96-3be2-a139-f364bf4d1045 | -8.38211 | -45.02309 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efa6998c-4036-3a46-aa61-277712244b0d | -9.0519 | -50.48262 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c8457ef-b630-3efe-a53b-083ea84b5ce0 | -6.21225 | -43.35513 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8277fb9-f9e9-3215-93b3-86c2ef7e8d4f | -4.85887 | -45.66235 | 2025-09-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d69c240-7820-36cc-98a9-98abc66b09e5 | -6.23128 | -46.24483 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d798f503-5995-309c-aab5-715262358afc | -7.86195 | -46.25685 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e09ef727-ab67-375d-a49b-1e1eef568d96 | -7.88788 | -46.25619 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ee7143-33fc-3654-ad8c-27bb6d4444d9 | -8.48131 | -47.29744 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60e5004d-36d8-3ad1-91c2-2f6486951c5c | -7.57383 | -44.64817 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b738e7f9-ccd9-3f9a-ba70-d42cac157903 | -5.72635 | -45.39672 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
