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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de42891-3b13-395d-b63c-8e159777df14 | -12.1175 | -50.3135 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 11831004-4ca7-3b7b-a581-0690e3b1baae | -10.7913 | -48.7596 | 2026-09-29 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d8e8dd34-57ff-30f6-b1ff-0680c4d98230 | -11.4119 | -43.415 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 37c883f8-e8b4-36f8-a180-b61113874536 | -11.411 | -43.4625 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| d416f33e-c7d5-31d3-a0ea-bcd43217f91d | -12.6463 | -47.2598 | 2026-09-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| b5da870f-b386-30e0-a103-44cebd58f36d | -8.9823 | -44.1633 | 2026-09-29 13:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2086936a-31d9-346a-b631-e9e9f8116de6 | -12.3679 | -50.1539 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1b486232-3192-307b-88ca-9d7c1188a3d4 | -14.1115 | -46.2834 | 2026-09-29 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 6f76ec1d-7c87-3886-a9a1-3a8f968a4510 | -11.4791 | -49.743 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7c45ec82-8aae-39cf-899d-6758f6f849ed | -11.1583 | -44.7859 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 758f1bb5-2729-3457-a641-c4336314f0a7 | -20.9159 | -57.8246 | 2026-09-29 13:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 7803d643-0e2e-3bbc-aa29-8464360a4bba | -9.9973 | -50.1393 | 2026-09-29 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 005c2526-6de9-33e1-a4c1-4b4898d8d46c | -5.7563 | -45.152 | 2026-09-29 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.8 |
| c65bc3d1-e36d-33d3-bc14-280f4d4f2a79 | -7.3967 | -42.6261 | 2026-09-29 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| b0bf80d6-8d39-3a22-bbed-eee25969984c | -13.1992 | -48.5603 | 2026-09-29 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a3f9d81b-f4ec-3e9e-9d51-47a805cb3420 | -10.3894 | -61.2502 | 2026-09-29 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| fb32b680-27bc-3793-8041-ac9ec04c8340 | -9.9593 | -50.1644 | 2026-09-29 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5153b470-114d-3acb-a407-ae9742f57316 | -12.7421 | -47.2684 | 2026-09-29 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 275.4 |
| 1704c738-2ff1-3f09-9cce-c3a577e86c05 | -11.171 | -50.0366 | 2026-09-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| fb5ef5bd-4067-38f2-8624-8968b32091c2 | -10.3895 | -61.231 | 2026-09-29 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 6eff33a9-9fb8-31ac-bc65-a215bbe47af8 | -11.3743 | -43.3734 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 6909f27d-191c-38a2-b34c-013ec080341e | -15.5154 | -41.3515 | 2026-09-29 13:50:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| e3a4d01e-486e-3850-9a54-5e3f208a41f7 | -12.1734 | -50.3927 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 90c2d0b7-c2c8-3d12-98e3-252c53bd3e5d | -11.1771 | -44.8064 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 282.3 |
| 7a171aca-3d0e-3ae2-b4ee-13430f8e6ca7 | -13.6762 | -45.7822 | 2026-09-29 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 671a0563-96be-30f3-8972-6f1bf1095913 | -8.6451 | -45.3489 | 2026-09-29 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f8ec70d8-4aaa-3838-ba5d-e6ecf70646b8 | -14.1309 | -46.2801 | 2026-09-29 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 066fd31d-c007-3718-ac69-6f1d9c4aa0f8 | -11.0241 | -49.7088 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 924a21d8-93ae-3fa9-9d0a-0462ea2f0d42 | -11.1517 | -50.0603 | 2026-09-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| bea10d37-6941-3342-9c22-132d6905bc6a | -11.9845 | -50.2864 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 33f9e775-f6e9-3aac-9a7f-2bc327c2a8c0 | -12.374 | -46.3972 | 2026-09-29 13:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 64370cae-f692-313c-ac18-710efcec5643 | -10.7916 | -48.7377 | 2026-09-29 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 32f7d8af-18a0-30c0-a287-62ba3870e8a6 | -12.6078 | -47.2653 | 2026-09-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d9576603-5175-3e90-91cf-a5092a61f7a6 | -12.761 | -47.2881 | 2026-09-29 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| fdadfdaf-d1b7-39c3-a8d6-6c3ae9d36af9 | -8.0355 | -42.866 | 2026-09-29 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 149.8 |
| a635b4d8-1d32-30de-8efa-788d2d4a20f7 | -8.9633 | -44.1655 | 2026-09-29 13:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0b871830-8667-32e3-84f2-24f1d5e80aeb | -11.0738 | -48.9012 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 0089879f-67bc-3120-b906-2c5b9d1fc467 | -12.2113 | -50.4096 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 19ad3c95-274f-3fcc-b661-904af60574fc | -11.3739 | -43.3972 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 96a4a70e-a4bf-39d6-8061-133065833aed | -9.9784 | -50.1412 | 2026-09-29 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 96e1964a-a9ab-3136-9307-cc5bc9e28e09 | -12.1362 | -50.3328 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e5d46a7c-0b2c-38a6-b9ea-7814823832cd | -9.9595 | -50.1431 | 2026-09-29 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| db19c366-595a-387b-96c9-0806e68dc1b8 | -12.2877 | -50.4004 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5bfaaf3b-08bb-3cfc-9953-05d033b7b4ee | -11.9803 | -50.5657 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bf7a6c27-515c-3427-84d8-11ae119a488d | -10.2843 | -44.6274 | 2026-09-29 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0a864ea3-a116-3169-89a8-4d9b40f65a36 | -12.1543 | -50.395 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 57b643c5-79c5-3f4b-abbc-326df3b82f43 | -12.2119 | -50.3666 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| c57ee5b2-a31d-3ac3-bb98-344b0171dd20 | -14.5362 | -48.2927 | 2026-09-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 91d9f695-0111-3741-95a3-28e4ca420e8e | -12.288 | -50.3789 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| dc44a515-eae7-383a-893e-82b72ed0280c | -12.7614 | -47.2656 | 2026-09-29 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 492.4 |
| bdaafde9-cb65-3380-8b75-317a56a03562 | -10.2147 | -46.706 | 2026-09-29 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6e135d35-a534-3709-bb4f-c67ad4fcd7dc | -11.1775 | -44.7832 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 561.5 |
| d5380296-4085-3bb6-9df1-11e18ab797d7 | -12.1922 | -50.4119 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4bd6e87a-1377-3117-94c0-28520eab4cae | -8.3614 | -45.424 | 2026-09-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9a3afb89-7a4a-3a96-8471-7d13ebc433bb | -11.4495 | -43.4566 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 562589c6-eb07-389c-b795-3d48aa56f3e1 | -12.1366 | -50.3112 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 86d9e004-25e5-303f-b1cb-7bc59a36f279 | -11.9609 | -50.5894 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0b3fa944-580e-34e4-a27b-9c955f06bd66 | -9.1337 | -49.9656 | 2026-09-29 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dfb466b3-264c-320a-abea-f012b814614b | -11.152 | -50.0388 | 2026-09-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7d1a0e9f-d874-3f20-810e-ca7242f3036d | -8.2293 | -45.4375 | 2026-09-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2dd5b129-1f6c-3aad-bcab-30aab9ab22bb | -12.1925 | -50.3904 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f556de28-fc7e-39af-a8e8-69af2fde2ec0 | -14.5168 | -48.2958 | 2026-09-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c50c05cb-6a94-3889-9b76-02c2106d4fb0 | -10.7255 | -44.4291 | 2026-09-29 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| c46e44b4-0b99-3d33-bfde-8eaf0b73153d | -11.4298 | -43.4833 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 167fcd84-1722-3e17-b108-a37905e02371 | -12.8847 | -44.8015 | 2026-09-29 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| fc298e8e-277a-33f3-a212-2b3774a1a93c | -11.3931 | -43.3942 | 2026-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 1ce3efe4-7c5f-3f34-85f0-d0e86209ad1c | -12.7417 | -47.2909 | 2026-09-29 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1098216f-4afe-3e4f-8f2e-6d7017b509f2 | -11.1327 | -50.0624 | 2026-09-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 54823bf6-0332-3400-859b-43067a81ea01 | -11.9612 | -50.568 | 2026-09-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7d189ee4-2ead-37a3-b74f-e850483c8d2d | -12.6271 | -47.2626 | 2026-09-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 4221e40a-1488-32d9-954d-97655faf52c5 | -13.1799 | -48.5631 | 2026-09-29 13:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| fa5aadaa-42ca-3f35-9205-088de0f82cd9 | -11.6096 | -44.1382 | 2026-09-29 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ee16a932-8f17-33b8-8af5-5392ffed413e | -12.761 | -47.2881 | 2026-09-29 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| cf1a7ca2-5e33-3173-92d6-70c5787d3d6b | -11.9615 | -50.5465 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fad2ee57-e818-3ca3-908d-23b79fc90d17 | -12.374 | -46.3972 | 2026-09-29 14:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| cc9ada08-1a92-32a2-a0e6-dccc2acbe2c7 | -14.1309 | -46.2801 | 2026-09-29 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 44217955-f2ec-392a-81f7-f108db4403ef | -15.3998 | -47.9261 | 2026-09-29 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9209012b-8f43-342f-ae94-05b1b4ead563 | -15.5154 | -41.3515 | 2026-09-29 14:00:00 | GOES-19 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 164.5 |
| 8ec331b9-e63c-3a4d-8efb-6ef405d504a2 | -12.8847 | -44.8015 | 2026-09-29 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| f59ceb23-d8a4-3eac-97dd-ae60029dd9b8 | -12.6271 | -47.2626 | 2026-09-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 4fa9e986-74ce-31aa-899d-dff4e39b9a8d | -11.4119 | -43.415 | 2026-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 426.1 |
| 307796a8-f6af-33a2-b3a6-68fc30ae95e6 | 1.8403 | -55.6244 | 2026-09-29 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 5dedd1a8-a4f5-3e02-9b12-dbd3f513be64 | -12.6463 | -47.2598 | 2026-09-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 83c5a96f-a4e9-39e7-8dd0-d935de395233 | -12.6078 | -47.2653 | 2026-09-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 24ceae59-1494-30df-9c58-29c224d8e5a1 | -11.4981 | -49.7408 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 20164e15-16f2-3ef7-8018-6c0562f634eb | -13.1803 | -48.5409 | 2026-09-29 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 122575d3-3030-3fc6-aa68-27e6c7f8d113 | -14.1115 | -46.2834 | 2026-09-29 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| e3ca7364-d2c2-36ef-8bff-9476b0392a7a | -11.8859 | -50.5125 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b1d53bb4-f826-316f-bc2e-c498139e4acd | -13.1992 | -48.5603 | 2026-09-29 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 6f52b5d3-83f1-3591-bc70-ecb171e45669 | -11.3927 | -43.418 | 2026-09-29 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 3a2f2bc8-d62b-321e-9560-b1cf14c9ce07 | -6.2404 | -41.5912 | 2026-09-29 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| b283546e-e425-3978-88ef-23f802565d07 | -14.5168 | -48.2958 | 2026-09-29 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 44e4928a-96fe-3af8-9b41-f97499de7505 | 1.8403 | -55.6442 | 2026-09-29 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 74f34606-cbff-3510-844d-465a8937d31d | -11.1583 | -44.7859 | 2026-09-29 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| c3bd6b04-e280-30a3-8881-765d434fa7c3 | -9.449 | -45.963 | 2026-09-29 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 246591db-91d6-3d11-9ebd-f855a6ae80b8 | -12.1922 | -50.4119 | 2026-09-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 01b5b82e-210f-373e-bdb6-b6397376ce00 | -15.3807 | -47.9068 | 2026-09-29 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3a61f2d4-5323-3564-8b19-a4382e9061d5 | -10.3894 | -61.2502 | 2026-09-29 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| e1d38e16-f495-3358-b714-b6145ef84eed | -8.38 | -45.4448 | 2026-09-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4dcd5d1e-0d45-3dc5-9c27-8a1a96062579 | -13.3835 | -44.0132 | 2026-09-29 14:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |


[Clique aqui para ver as próximas entradas](README79.md)
