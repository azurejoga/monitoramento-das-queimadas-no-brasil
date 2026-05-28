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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49095dfc-aab1-331c-a1b8-f9fae8c57d8a | -9.60408 | -58.34034 | 2026-05-28 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd63beb-55a8-3ab6-beb6-57c03ff8b2da | -10.48113 | -48.91299 | 2026-05-28 05:14:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cde91adc-b303-399c-973e-ae86bbb6d869 | -9.44108 | -48.89046 | 2026-05-28 05:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2c8dfe3-8578-3c76-ba8e-6c5b99d5ce0e | -10.47696 | -48.9066 | 2026-05-28 05:14:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70d1d5db-39bd-3330-a756-9d91401738ef | -12.33033 | -47.90063 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fdc66f9-9752-36c5-aecd-a38a40b57602 | -11.07471 | -55.05378 | 2026-05-28 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 070bc466-fad6-3c98-b69c-721ef1ffd5e8 | -11.58686 | -47.45523 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b113134e-16dc-39e6-ac4e-03e83282f62e | -11.29974 | -54.0279 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa1a37e1-3d1b-3903-a583-552cbf95822d | -11.96895 | -47.38127 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a9f1018-d665-3019-a0bc-438eef84ccac | -7.35556 | -46.21611 | 2026-05-28 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db659fd4-db2d-3091-8c97-b7bef2078b78 | -8.67839 | -48.30756 | 2026-05-28 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 117be7c7-12f1-3df6-8987-37a8349883fe | -11.45168 | -55.11369 | 2026-05-28 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4218a405-9c87-3273-a450-877cf15981e5 | -9.34604 | -45.47405 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14fd0b29-5eb9-3fa6-8d56-98e5bcb5f054 | -10.62443 | -46.9099 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 03846e60-f944-36ca-bbd7-f800294da3c5 | -5.79486 | -45.13262 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82fa12f9-d7af-3948-bd1f-760ecef161dd | -10.87394 | -53.73759 | 2026-05-28 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33cd75c0-9d04-3bea-82ee-7685526f2056 | -10.14233 | -52.40208 | 2026-05-28 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f5363da-e6ef-3293-83aa-2c8d7d406d44 | -12.33074 | -47.89723 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb37cd3-6c90-3c7b-8991-41f8fba49dce | -7.0075 | -45.00831 | 2026-05-28 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 351fee91-96f4-3864-ba77-d76bcf860834 | -11.59941 | -47.44512 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25623e34-f0f5-3be2-baaa-4b540a12944c | -12.32346 | -47.90023 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8961f13c-b1f1-3eef-b1d6-5318004e919e | -11.59337 | -47.44824 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3dd19710-75fd-3a2b-bf4d-99f8c879b534 | -9.38761 | -48.44037 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| baef8911-3047-3876-8bca-5d580ce7d964 | -7.62137 | -51.68019 | 2026-05-28 05:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb3c2c87-7f43-30a3-b530-3128ff6223ac | -10.77874 | -46.90939 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f3bc89-2d39-3913-80e7-782cf715a32c | -11.28152 | -53.97082 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ef8ab07-6e3b-3abc-81a8-ccf350d53594 | -11.56364 | -54.53057 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfb63d8b-1b76-395e-8e8e-02eae2e0c132 | -11.29552 | -54.03152 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06ee93fe-dd47-3a3d-9a97-f63ea7ef2ab9 | -6.52913 | -55.06661 | 2026-05-28 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4630e3d-5e13-3914-b6fb-0e3253faad15 | -7.00936 | -44.9944 | 2026-05-28 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d3b4c05-fd11-3d65-a941-f160ea7f9cfc | -9.33992 | -45.47324 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc85a522-5a31-37f0-a095-097c8d43aa8c | -5.48768 | -45.1184 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ab04dc9-5ff5-3267-8191-1e1eb7800134 | -9.34747 | -45.4682 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57729425-6762-39d3-aec3-af6ccbb3ebcf | -9.71509 | -50.41197 | 2026-05-28 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98175683-b75b-3321-9792-6b94e7bc62de | -12.68649 | -44.78303 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beacb2bf-b767-36fb-abf2-3e0782601ceb | -12.32892 | -47.90084 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27f20307-4d0c-31f1-9f0d-d5f1b622ce7f | -10.71002 | -56.04317 | 2026-05-28 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9491d230-c352-3e8b-9b1a-9c39f90649a6 | -7.35167 | -46.21395 | 2026-05-28 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b259ec40-9ee9-39bf-acef-59026328b52b | -7.01365 | -45.00887 | 2026-05-28 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 422f26eb-961c-3a4d-a683-55f1142a39f4 | -12.32488 | -47.90001 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 152f4baa-30e7-379a-b284-07215b30fffc | -11.59238 | -47.4562 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3c9a225-2eba-3ec0-85b4-b48dbaf1da13 | -11.16646 | -46.81185 | 2026-05-28 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23c1e825-307c-3c66-b1f9-924857a2c627 | -9.94135 | -48.0194 | 2026-05-28 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa1ba4ec-bbd7-3b23-ba0e-fc913e809c74 | -8.22499 | -49.67687 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ea20d38-79c3-3b8f-8a2a-7a15c3e279c2 | -7.86252 | -61.48952 | 2026-05-28 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a315985-1e8a-3e77-81be-2c3024676ef8 | -11.975 | -47.37828 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bd03c49-6b4f-38bc-8465-93a24e336c2e | -10.13453 | -52.4009 | 2026-05-28 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ba29feb1-5c23-3a8f-962a-c907c117c10f | -10.61876 | -46.90916 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bc828a2f-c2ce-37c2-96b4-09b8c88fbb7c | -5.80199 | -45.12492 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76ba565-3cbe-33bc-93eb-45cfec060579 | -5.48173 | -45.11767 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edd98306-e33f-383e-896c-73c5cc0ae7fd | -9.05363 | -46.30655 | 2026-05-28 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49e0ce7f-5f15-3562-ba72-2b2100d9d630 | -12.3239 | -47.89683 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a017a93-4f60-34e8-b089-1fbb202b2ce5 | -7.71292 | -45.93751 | 2026-05-28 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88f2b3b-c45f-3210-8e9b-b12c964ec4a4 | -11.59847 | -47.45261 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94ef48df-57aa-3d0a-982e-83311cea3de6 | -8.21948 | -55.10139 | 2026-05-28 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb6ebfb0-480e-3aac-bf0d-4c1826da4361 | -11.2779 | -53.97028 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c535e690-928e-3e42-a7ba-8c8eb1ce2472 | -10.70947 | -56.04675 | 2026-05-28 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762c76d6-b3da-34df-b21e-cde314529c69 | -11.07816 | -55.05431 | 2026-05-28 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2004d8d6-1f50-34c3-bfb7-fc8a1878603e | -10.61927 | -46.90515 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33cf54ba-cad6-317d-8c4b-cd47bcb770a1 | -9.14371 | -51.28981 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e437f4-10b1-3022-8375-58e0afcb3790 | -10.70611 | -56.04621 | 2026-05-28 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04ffc192-42c2-3e94-8aa5-546cbefcb327 | -8.72629 | -48.33178 | 2026-05-28 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e925de28-d5a8-30e6-93fd-2059cc5c1f59 | -9.36035 | -45.46496 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 259f0653-eb1b-3561-bf0f-503b79608abe | -9.34685 | -45.47292 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af2b02ab-84d5-32fe-a57b-935f72f76e95 | -11.98984 | -47.15812 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45ebda33-bcd4-353f-b20a-cbf7897d5f46 | -9.35947 | -45.46613 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01b7f2c8-992a-3fad-9d00-58dda9eebf9e | -5.20436 | -56.04773 | 2026-05-28 05:14:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ca99e6e-123b-30f4-8578-b21daa1d830a | -10.65618 | -49.73318 | 2026-05-28 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec516743-f0cf-34b3-a19b-262dfbedebca | -7.5991 | -46.46458 | 2026-05-28 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a75b3ee-004b-3136-9380-0e5a2abd53cf | -9.34662 | -45.46932 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6d1f21c-3c80-3bcf-94d9-25f93849e433 | -11.16694 | -46.80808 | 2026-05-28 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecbc9727-f5a6-3adc-9946-223fc0bac8a6 | -10.04476 | -55.2505 | 2026-05-28 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b81d97ea-2af2-37bd-b011-627dee998722 | -9.14476 | -51.28245 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 285d3f8f-92e0-3c40-88bc-91fbea72e6c3 | -8.30526 | -49.40412 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 859245aa-7739-3680-ba9d-3ac3890aafba | -9.14943 | -51.27936 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a4234c2-bf26-3bc7-a43c-0cdda7dd5289 | -11.46728 | -52.918 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 900cb584-2201-323e-a7ea-036d360d4f95 | -9.35275 | -45.4701 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ca27bda-b6b1-36c4-83a3-e3a36e12a27d | -7.86191 | -61.4931 | 2026-05-28 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 304da463-a6a6-3062-832e-463e5941ee51 | -11.46275 | -52.92224 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26e69ac-f687-3fad-a6fd-5cbb7abf32a4 | -12.32935 | -47.89743 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9ff0092-792c-34b1-a1da-88a4779d66df | -5.79188 | -45.13714 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01e00a35-7c5e-3f0b-bb93-3c23f4641c91 | -11.44284 | -52.92418 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844830f7-13a0-3102-80d2-da9428b4bf36 | -7.59962 | -46.46083 | 2026-05-28 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fb8b9a8-9a72-3532-83b8-4043a81b6bcd | -7.00811 | -45.00373 | 2026-05-28 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3936aef6-3bd9-3782-a392-567bdefdd206 | -6.99434 | -42.87511 | 2026-05-28 05:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8cbc8669-290a-3370-98f6-bb6337177dce | -11.29852 | -54.03625 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d77e7225-01b7-3821-880c-63bb97323739 | -5.79907 | -45.1295 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e41cf56-364b-34dd-9254-eaeaa3710859 | -11.59176 | -47.46112 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a6f0daa-0bb9-3b2b-a8f6-b1af7994d68c | -11.2749 | -53.96555 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4552b1d6-2b6e-3a86-817c-39a67139d537 | -9.44426 | -48.88662 | 2026-05-28 05:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a75ce55d-ce66-3444-beae-2ab35757191e | -9.39119 | -48.44158 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39bbc205-a5cd-355b-8105-33b79516f750 | -8.12 | -49.56598 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73e82581-cdb4-3c46-b5cc-ab49a0bc2c90 | -10.61774 | -46.91706 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc90627e-d17f-3df8-a53b-387eb1221056 | -9.14424 | -51.28613 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f9cc646-7a1f-3dcf-9e82-a1a40221b22b | -9.36007 | -45.4613 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a782c32f-f60b-3878-b3dc-d9b556117784 | -10.03046 | -59.3515 | 2026-05-28 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b906cf9-b360-3f17-ad48-836b7538218b | -10.63112 | -46.90279 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a239b73-d722-36ea-8e3e-e0b8c8ce9249 | -5.95885 | -43.49065 | 2026-05-28 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4aec87fc-2fe3-309a-90bf-f74200bcf1b4 | -8.52709 | -51.57867 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2e39a01-d36a-3116-b873-892b63740df3 | -5.10118 | -46.9472 | 2026-05-28 05:14:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
