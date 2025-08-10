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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67463c7-2de9-37e6-914d-c1abd4658a73 | -5.41105 | -44.42701 | 2025-08-10 03:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01221fd3-a44c-3613-9b87-b32ab1392b68 | -9.49907 | -46.2957 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a8c0235-93eb-322e-9207-e268ca243311 | -7.34657 | -44.59523 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb69908-a6db-3a47-be95-bfd7bf64c1ca | -11.7491 | -45.026 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f950db9e-a824-3687-a186-3d73c7164a66 | -8.11013 | -47.4412 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd4e64d5-034b-3b8c-ad57-d5079c925db6 | -6.55342 | -42.76795 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| dfeea68b-7284-30ea-b87e-36787dc74477 | -9.86719 | -44.70489 | 2025-08-10 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c06047d-9633-359b-9944-516619c15292 | -7.13089 | -39.46749 | 2025-08-10 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69d63257-41ee-3793-a2d5-8729fe19f347 | -12.65007 | -44.51124 | 2025-08-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa6e553e-cfaf-3ade-98ab-d59aa327e618 | -9.66066 | -46.75525 | 2025-08-10 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 026d63c8-b2ae-3745-a511-f8c3392554ae | -7.16182 | -44.06727 | 2025-08-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| df452bec-889d-337a-9080-e365b34dfe2e | -5.2052 | -45.61867 | 2025-08-10 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 316227df-c091-38e7-b2fc-96ea2207f847 | -6.55645 | -42.77327 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 575a07be-0e52-3d83-9c03-446fd31f8614 | -5.47679 | -44.70532 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f5c6db8-a366-361c-accc-b4d5ba4c3852 | -8.98034 | -45.68682 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3360540-fa7a-3a23-831a-8d56f4c0cc69 | -8.12188 | -47.43391 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2c3692c-7c75-342a-816f-fc0cea5ec18e | -11.48509 | -50.28036 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b29fdeb6-f031-3c50-af76-bb1ad774042b | -7.59865 | -44.41899 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f9e5cc4-0558-34d7-a479-8cde4cded890 | -6.6119 | -43.38017 | 2025-08-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 953e7bb2-2431-3e84-b848-c8a8bb49591a | -9.49157 | -46.28458 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba6c9aad-3b46-39d4-aed2-f81c3780c651 | -7.60982 | -39.96648 | 2025-08-10 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 54dfb08c-26b9-385e-9a49-2f2cc10fe2a2 | -6.2258 | -48.45293 | 2025-08-10 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bf0ee1a-50d3-3d0d-ad00-f284523bc312 | -7.73092 | -45.53492 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dc5128b-92ff-3ed5-9242-43360f4e24de | -7.8812 | -45.56039 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 941d64ea-f052-3e53-ad5c-6e4d55f4ef95 | -12.57724 | -41.28184 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9063c454-65f9-32eb-aa3d-78f1fe125fcf | -6.57826 | -44.57258 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcc10d10-727f-3e82-9be5-427986be2ef1 | -11.93308 | -41.43753 | 2025-08-10 03:55:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f28e1416-7ee5-3ef7-a962-aec88506baea | -11.36879 | -50.53624 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aae875b3-8144-3481-9f97-52445b12da9a | -6.67969 | -44.73358 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e44680e9-1dac-31df-ba7b-05345ea834b9 | -7.42946 | -43.99153 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe4d42d7-0ab7-36c8-9c5b-800a6a064bd3 | -5.41034 | -44.4312 | 2025-08-10 03:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 901bfe49-7b95-3a4b-b8db-dad8cd9e9bb9 | -7.96183 | -44.783 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58223970-7984-3f92-a6fe-9e36e5ab4978 | -8.77453 | -46.41225 | 2025-08-10 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f14539a-5d52-3ca8-b449-ef44a7c6ea25 | -6.55566 | -42.77795 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 30ef9108-3974-3276-91bf-de40c6c55bf5 | -7.41664 | -43.99316 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7dc4b37-ecbc-38bc-89d8-fef23ed7db2e | -6.55048 | -42.76896 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| abc996c0-589f-3679-9542-0fdc57fc0503 | -6.60796 | -43.37934 | 2025-08-10 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8751b76a-8990-3bad-97aa-88e69107db99 | -6.58101 | -44.57297 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8073db03-472e-30de-a93c-e5a42637215d | -8.87845 | -44.78813 | 2025-08-10 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e28b255-8fe4-3070-9b97-6bf198b89353 | -8.32363 | -44.98385 | 2025-08-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93b6980e-913c-306b-b263-ad4b63d0ae98 | -6.69595 | -35.29209 | 2025-08-10 03:55:00 | NOAA-21 | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 731c7793-aceb-3e0f-86d0-57c89506a17f | -6.58171 | -44.5689 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c58627e6-13bf-3434-8506-432431b19a75 | -6.19217 | -46.10029 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e57f12f7-4f65-391d-8d89-3f778490a225 | -6.54577 | -42.76671 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4f2ce6b3-8dc7-3191-8ee8-d7cd27b86475 | -6.19699 | -46.10094 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46dc0eeb-5f9d-387e-aa4d-ddc4f38bb56e | -6.0585 | -43.74407 | 2025-08-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73e5c445-2bce-3196-8749-8094928a630a | -11.42964 | -50.58967 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b6deb6cc-8bb8-3eed-bb1b-9f7590ac6b90 | -7.34093 | -44.60263 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42cf5019-e43e-30fa-98ba-d806064d3803 | -7.88967 | -43.54211 | 2025-08-10 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 80932c11-52fc-36dc-9272-830d87510ca9 | -6.97229 | -43.72708 | 2025-08-10 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3b4b133-25bf-3b54-bbc0-5d778e8e1a76 | -9.49366 | -46.29956 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecb88d44-3f2d-335f-986e-5da916ca8a04 | -7.54039 | -44.00298 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c844a25-06d3-36b6-8666-9966dd72f7c7 | -9.65877 | -46.76557 | 2025-08-10 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa22ad7-3424-3b61-a2a8-33dfed2bbbb8 | -4.94023 | -45.44677 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1d25802-3a01-34e7-a811-63392780fd63 | -6.19426 | -45.44345 | 2025-08-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e3772669-2b99-37c8-8fca-ff32923544b2 | -8.50166 | -44.7532 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10a48dd7-3d39-3ccd-8299-798bdfc4c250 | -11.73141 | -45.00774 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9fbd6f-57c2-301d-9bc9-7d6f3162ae76 | -6.949 | -44.55761 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4b9527fe-1b31-363f-be55-252a784145f1 | -5.91793 | -46.4749 | 2025-08-10 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba2cafd-a9cc-3954-9ed2-95dd8880fb4b | -8.50232 | -44.75252 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02742df9-eb55-3c84-b4fb-1e8c25df3331 | -8.51116 | -41.43197 | 2025-08-10 03:55:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7821e290-a01e-3f59-b16d-4957b68f8b10 | -7.43008 | -43.98781 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 741e0f8b-ce4b-3dc4-812c-604ca04e5b3a | -11.74848 | -45.02954 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccae1f8b-98fb-3e30-9120-fb0940377f57 | -9.52421 | -45.40215 | 2025-08-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e32139f8-1d5d-3957-b4fb-213100e6c1ff | -12.01984 | -47.51129 | 2025-08-10 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ceebd84-ecff-3177-a93c-6f7f7cc15220 | -8.9155 | -44.25487 | 2025-08-10 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9decacd1-452d-3cf3-94f2-a11e2c2d0aec | -9.49533 | -46.29006 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c73b7519-aaed-31ad-8f31-93872f45ea3a | -7.70091 | -45.53541 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac478657-3be1-372a-8aaf-122a5c2bd862 | -6.06372 | -44.89845 | 2025-08-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 671f1433-5921-37a5-82ce-1705b5cc3453 | -7.59446 | -44.41838 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7e11598-0912-3871-aba8-927a02ca39c6 | -6.98979 | -44.79969 | 2025-08-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43e2e908-52dc-3ebf-a58f-746451c98567 | -12.50561 | -40.82148 | 2025-08-10 03:55:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffe6e6af-2e58-317f-8d46-e88ea8129025 | -8.50163 | -44.75645 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc654db9-1eb9-3eae-ac88-3309dab66346 | -5.52377 | -44.33548 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93ffdd1b-9be2-3951-8018-3de7dceb14f0 | -6.98548 | -44.79884 | 2025-08-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dd56512-5af3-36c7-8348-d9b13ae64b3d | -10.34258 | -44.90394 | 2025-08-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f81389f-08f7-31ee-bb79-78228c56051f | -11.4853 | -50.28189 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 906a7da6-c1ea-37a1-b8a4-0996dc617554 | -8.11627 | -47.43605 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa574623-f174-3f4a-8066-56ef355ab553 | -6.67536 | -44.73287 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28a50e76-d7a6-395c-bf47-961b93387c04 | -8.9819 | -45.68436 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19900472-caf1-399d-828e-d7c16252a2eb | -11.43744 | -50.59006 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1d4b6e-2e96-350f-945d-f6c4d1869297 | -7.1577 | -44.06662 | 2025-08-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 26ed195d-10b8-3bf5-be38-22ead77e4564 | -6.55123 | -42.76432 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| db3a6d05-978e-39ba-9e12-ba482303173c | -8.98398 | -45.69202 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa2fd49d-a60a-33f6-854b-8cf70b5fbb68 | -6.95459 | -44.55043 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 37b3f6d1-b9e9-395b-b684-0f9dd5399f87 | -7.42072 | -43.99382 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36786d88-9d2d-3706-ba69-6d8570174c99 | -10.46233 | -47.95039 | 2025-08-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e088002c-98d0-33d4-9c59-ef30f076bf6c | -9.5745 | -48.44572 | 2025-08-10 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f46da70-d06b-3699-ae72-6393084d03b7 | -7.39683 | -39.67852 | 2025-08-10 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b8f7f396-0ac5-3220-b583-964342dc5f41 | -6.83437 | -41.05227 | 2025-08-10 03:55:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8a977407-ceb2-3deb-9257-f0f9f0afe3bd | -6.19183 | -46.10348 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 131c4d95-5571-3a86-8f86-cb99ca1af34e | -8.1168 | -47.43307 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00180f9d-78d6-3e54-ad07-0c6c4837ba6d | -11.74261 | -44.96822 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57774790-afb4-3138-aa14-7025b40c9f53 | -6.55355 | -42.77427 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 263a3325-4bf3-355e-9670-d1eb788c8345 | -11.76335 | -47.48243 | 2025-08-10 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af07af37-b37c-342e-b0de-b579ff279041 | -11.38383 | -50.55256 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbe50b6f-5dae-3731-bcd9-06c6039c1b35 | -7.87671 | -45.55964 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21af2cb3-a50d-36c7-bb21-15a19973167c | -7.5951 | -44.41463 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392c0da0-10f6-3fe2-9d2c-2e4829f9942e | -11.36964 | -50.53196 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b6647c26-0023-38a2-bc1d-0a115878b526 | -12.64921 | -44.51625 | 2025-08-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README10.md)
