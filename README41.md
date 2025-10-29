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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0018415e-8467-332d-a65d-f33cc6a19092 | -7.59573 | -45.85324 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05649200-68ac-35ac-8147-a5f117c70575 | -7.34365 | -43.9132 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bb768dfc-d4d2-3c43-85a9-41542ffec97e | -10.98099 | -47.86491 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa6b1ac-742d-35c4-b310-6a1b4eb38898 | -10.52775 | -50.00033 | 2025-10-29 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3622b14-128f-3a98-b713-f11310758f8d | -10.94332 | -47.62204 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 767f3ea7-007d-3a5a-99cf-6ac5af7ceec9 | -6.14545 | -41.68627 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f42e23d5-f141-3e41-93a2-69fac66b2400 | -10.86889 | -46.04506 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea7e88b7-b9b2-3787-bb97-a0ad7dc6ea76 | -7.59836 | -43.5746 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af0b4688-ce57-3d25-87ed-6ff458efb6fc | -7.43859 | -45.12166 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11a17af6-6f64-3768-8b56-759bfc806e99 | -6.49832 | -42.23602 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 003dc20b-a92b-3c72-8d36-08954df9c994 | -9.18148 | -44.57629 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d9637a6-3e5c-30f5-92b9-9703aff399fc | -6.22882 | -42.53261 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ea04cfc6-285e-3b2d-9619-92bc92b6de8b | -6.81124 | -48.64644 | 2025-10-29 04:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecd23cf-5f47-36f7-8f1c-13a7a6029cca | -6.88587 | -45.04453 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a9e51de-f173-3d31-9d2e-ea63a93d6007 | -6.14335 | -42.22478 | 2025-10-29 04:23:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52c01600-59fc-399c-9e0a-6d27643ec7b4 | -6.48653 | -42.2431 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce095778-2001-3b3a-b0a3-9aa2239349e5 | -7.08483 | -44.94067 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 365cf716-cba9-363e-8e59-e980ee3ec4bd | -5.24022 | -45.13596 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac39106-1433-32da-937a-60b7f4c03543 | -10.65027 | -48.00822 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 40dd7320-4a33-3a8f-af70-0d42d115c41f | -10.77037 | -44.62533 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23e005b0-eb4f-3d7b-ad2e-4f7c534863c5 | -10.42862 | -44.99063 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a0a1ffa-0c3d-342a-bf46-b4ca7599f222 | -9.92311 | -47.66691 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378c1a84-d299-3ca1-8b9a-4c8744556946 | -11.26849 | -45.52606 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b75860c0-83e3-3829-b6ba-1943ccde8ca3 | -10.84411 | -47.88598 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c743043-b9ff-35c3-ad56-c7ef466139e9 | -7.27439 | -46.88952 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7a38d71-c5e7-3877-8eba-01428fc5486e | -7.4426 | -46.60913 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f17e7f8-74d2-3a70-a674-da97ddd72449 | -10.42807 | -44.99417 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cf58c7e0-3698-3446-9c06-5d4310d176b2 | -7.69935 | -46.90471 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e811951a-9a9b-301b-8b3b-532f9726171d | -10.51814 | -47.74294 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58214ebd-719c-3706-9a8a-87b6fab87623 | -11.46937 | -43.24028 | 2025-10-29 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 67d84e3e-0736-312d-86ea-70cb45bd8758 | -7.78722 | -46.46614 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79eeea14-649a-34e4-8a04-a1378aca4c04 | -10.97746 | -44.76346 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21cb0165-f4ba-3aa3-b0ce-87c7742f7167 | -8.40459 | -46.92804 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a6ee1d36-3632-3c64-baff-41b3addced2a | -7.98778 | -45.53842 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c6d7986-cb2c-3e36-a541-07bfa6e396ba | -9.39412 | -44.55561 | 2025-10-29 04:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b7e2d98-2ba9-3592-9dd6-69a4bc74c28e | -6.14307 | -41.67758 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a4cb222-0194-34e4-9dd5-eded1505611a | -7.27193 | -46.90452 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fbbc7dc-7c17-3c7c-a597-a3a9489cf72a | -5.75582 | -43.39176 | 2025-10-29 04:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 598accc0-8b87-3120-b360-39632fb60248 | -8.17572 | -45.71916 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49d328e3-317d-32c4-8547-39d5b7c856b3 | -5.33736 | -45.54065 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae5142b4-c132-3f5f-9930-c1a6f0610b42 | -6.53164 | -43.56904 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bff1250-5c1d-3748-b93f-78640dbaadd8 | -5.60967 | -47.11005 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 908b4262-add1-3a90-8405-ab17e4d69a90 | -10.21327 | -45.95354 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd838f33-2a09-39a8-aa6c-fc588aa8962f | -7.31743 | -47.81574 | 2025-10-29 04:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8495a808-896b-3a23-a754-118b757fc81a | -6.47242 | -42.24125 | 2025-10-29 04:23:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a0ef0b6d-a3b9-391a-86ef-c3ac79cf57d7 | -6.12948 | -41.8414 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 48993dab-0047-3b74-912d-4bc43f8cbe4b | -5.46419 | -46.09732 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d2254e4-eebb-3a6f-8b05-ba5967fed904 | -8.9654 | -48.64962 | 2025-10-29 04:23:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30186979-e8a6-3b2e-b3f8-6b30799a00b0 | -7.99955 | -46.20892 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 157ce6a1-80ea-3181-8a0e-a013f38ccc6c | -7.74673 | -45.73354 | 2025-10-29 04:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b025e569-6515-3e8a-aeb0-09fa5a45c82d | -8.61931 | -44.79834 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc7c262-159e-35a2-9e7d-196465a9d9f5 | -7.92956 | -45.49686 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d1a734-7dee-382f-a836-19c6576e8e05 | -7.81689 | -46.41153 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 947813ab-32b0-319c-8f50-33155ab49a56 | -5.70026 | -43.9352 | 2025-10-29 04:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf34131c-0570-38d7-9ac4-b3350f4f0bde | -7.30374 | -44.98997 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76727b56-f6f6-3dbe-b1f9-22a7922a3c0b | -6.64028 | -44.60686 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bea71be4-3efb-3a5b-b2d6-09df957e7298 | -5.49416 | -45.1158 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b2271ba-dafc-308c-b0a7-2c3fe8217947 | -6.11395 | -41.71661 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ec43ba52-3275-32b0-90cf-2b2d0cbecc37 | -4.84427 | -47.53628 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba7b803e-fad3-3ce3-bc7c-24c1025ca866 | -10.56975 | -49.84493 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 651e3918-04d6-3bbd-b5f0-715e7c44d6cc | -11.26129 | -45.52851 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d0ea181-6ede-3029-8bba-b0bd9292bd3f | -5.07206 | -47.10786 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb7df67b-ae71-364d-8eb9-650b283956b4 | -6.17929 | -42.46241 | 2025-10-29 04:23:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 562483cc-d1ac-396a-85c5-7bc6ba05a21d | -9.90599 | -44.91893 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a92e5bbd-db4a-350d-869c-515faa232674 | -10.64718 | -48.09296 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adad1fdb-26cd-3e96-a052-2f44e4331360 | -7.45761 | -45.47097 | 2025-10-29 04:23:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfa185b1-f122-30e4-9a26-430f9ba7d39b | -10.95361 | -47.62369 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca0f0f2d-b2ae-339a-b3be-a0d30a334587 | -6.49014 | -42.24253 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 481f2852-c0fe-317e-9bd4-61e4bd0aa640 | -7.93679 | -45.47294 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3307e3-23d6-32bf-b26f-e824128050d9 | -6.15423 | -41.575 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 855f1da9-9f4f-3408-8cb3-7384a322cf6d | -10.77447 | -45.05303 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0e854f6-a538-3277-97a8-bdb0b23715bb | -10.62065 | -47.88455 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac339d27-0e84-3aec-941b-35ff5a5e7a74 | -7.81806 | -46.40429 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bf3dab4-f1c0-3df3-9277-864a280e20e9 | -11.02595 | -44.64958 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7d0e899-3dc5-3ea3-b418-08638efd0b13 | -8.75961 | -46.51012 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3d5ab1c-b9c9-3c9f-94a1-3ef65d7dabe6 | -8.64151 | -44.80898 | 2025-10-29 04:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da698c2c-33c3-3898-a197-7c5ff6f93a4e | -7.90053 | -45.6786 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fb72c38-f841-3a3c-b6ae-f35220a796bf | -6.96561 | -49.39837 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c004a4e-6d75-34bf-a915-9cb008c28eff | -6.10877 | -42.4481 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 765e54a2-0dfa-3cd9-82ed-b48d3378939a | -10.85671 | -47.89583 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d107b282-a56f-3272-b156-a6d13eb9e22f | -6.10928 | -42.46777 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 330e8106-a75a-3748-93d7-23cb37a92142 | -6.2153 | -41.82967 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93e54e69-bcfe-3b7b-bc61-6147bf19a3ec | -8.21112 | -47.29816 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23615ae3-8c6a-35fb-9ff3-8fcd1bac90d9 | -6.30137 | -41.87875 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 2da7ae68-bf5e-3412-84fd-8469a3c44dd2 | -6.09384 | -41.77589 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47c266ab-80aa-3b20-b397-f9ccd82c286b | -8.45688 | -40.75542 | 2025-10-29 04:23:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba3b5971-1ac0-36c8-ba66-6075a034d4b8 | -7.60518 | -43.5979 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddd92bae-3509-3a5b-8f7a-e28815cfdc7f | -7.89997 | -45.68209 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1158c93-a8cb-3c14-893c-7d3e8ffd713d | -10.50217 | -47.73231 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 433e2ae2-59e7-3a7a-a82c-9a9c5eb28ee3 | -10.38005 | -47.11614 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f433c6ae-b8a4-3aea-9ad0-6bc64753589c | -6.10411 | -42.45524 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7a9af87-735e-3499-ab78-15c34b999067 | -6.1058 | -42.46725 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb464e42-ffc3-3756-a849-e7cc3e68cb8d | -5.65431 | -46.45557 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ddf8a6d-ed6a-3984-8138-4efdf0435a2f | -8.408 | -46.92865 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 76cad673-6543-3276-b157-4094f6c14f06 | -7.97797 | -46.27894 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e6d163a-6037-30b7-8b39-7514b805c17e | -9.88726 | -47.45455 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9cd0e19-06d3-3756-8d59-ef79447f384d | -7.69995 | -46.90097 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27511e9d-9794-3215-bab3-af7badeea505 | -10.95641 | -47.62805 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d50493f-b3b2-31d9-bf60-88887426aeed | -9.90375 | -44.91134 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0387dfd3-2be7-3f63-9498-2b4e062b8a59 | -6.49423 | -42.23927 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
