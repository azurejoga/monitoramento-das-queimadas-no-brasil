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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f53f59-f928-3673-b507-1419a29d8927 | -10.6983 | -48.6393 | 2025-09-12 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 92867478-e145-3149-85f7-a34d783f9c77 | -10.1216 | -47.9154 | 2025-09-12 13:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8028e18d-a2dc-32b6-a140-0499e8ef56df | -6.6837 | -44.142 | 2025-09-12 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4a6a5891-afd3-3899-8ae9-db93bd2a3a80 | -9.673 | -47.5459 | 2025-09-12 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 7f75c7c5-895e-3e27-8475-3f4979fdd2e5 | -9.5324 | -54.6277 | 2025-09-12 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5950ddaf-5056-311f-a500-af1021289941 | -8.8768 | -51.111 | 2025-09-12 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 279f832c-bb7d-3708-9d7a-4d50ea750505 | -9.5137 | -54.6292 | 2025-09-12 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f851b815-a0b1-374d-83f3-a53eac3299c3 | -8.4705 | -47.2712 | 2025-09-12 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8f0c4442-9a3a-36e2-b9b4-bff5d43b4814 | -9.0373 | -47.1041 | 2025-09-12 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 210.3 |
| acde64ba-abe3-3079-8497-f83272d223e9 | -15.1169 | -52.4705 | 2025-09-12 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e597e4a3-68d9-31e4-922a-e6f016bf256f | -9.6733 | -47.5238 | 2025-09-12 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 61c170ad-672a-3b03-8990-7625b3c5b4d2 | -7.5452 | -44.4086 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| e4d5910b-53af-3e58-bcc8-3b5266b65309 | -11.377 | -50.2281 | 2025-09-12 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| dc8710a3-ad1e-37ee-8e95-456f43dc9be1 | -6.3278 | -42.2294 | 2025-09-12 13:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 6d187ca2-ccbc-3286-9973-21f822099e47 | -12.9101 | -54.7558 | 2025-09-12 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 583bb0f9-d871-3d94-aa3c-b146f303c55d | -7.5232 | -44.6862 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 81f56c3e-35aa-3222-910d-919faec0a7a1 | -9.4804 | -46.4321 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| a36d0d56-fd4b-3f33-8b87-d53c441ffe73 | -11.771 | -50.5686 | 2025-09-12 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6e1f89b8-e292-398b-9bc1-8a77326e4e7e | -11.809 | -50.5642 | 2025-09-12 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6f9edb53-30d9-3cf7-898f-e8b2c55fdfee | -6.8372 | -45.6333 | 2025-09-12 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d7d7b876-51db-3b8a-8620-8159d2df3f27 | -8.8768 | -51.111 | 2025-09-12 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 2c6fdcbd-2762-3657-aa87-52ca74a98d67 | -9.4993 | -46.4299 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d9a049c9-8917-37a1-8c04-70e467c20bf9 | -8.4143 | -47.2545 | 2025-09-12 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f0c2c0f3-f22d-3347-90b6-6528d6af1259 | -10.3507 | -50.5303 | 2025-09-12 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 2947daf5-db44-3080-916d-60c65a6404a5 | -8.9374 | -46.0869 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 8f94a81c-6dd9-3d50-87cf-8947d7b1aabf | -12.5598 | -44.6677 | 2025-09-12 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b66aa295-864f-3305-87a2-d204e4ee3cee | -7.5227 | -44.7321 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6d48256d-eada-3562-b9da-8719826c5b7c | -10.679 | -48.6633 | 2025-09-12 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5f9075d8-eb0d-3f42-b870-f42e187ab931 | -8.956 | -46.1074 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 330.8 |
| 66b271f7-afd0-3d1f-8a08-a449d47f2104 | -6.1735 | -42.6221 | 2025-09-12 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| df337e89-2e42-30af-91ed-20ceafdad97a | -11.79 | -50.5664 | 2025-09-12 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 408e7048-14d9-3641-b0e1-858c43210d69 | -10.4438 | -50.6272 | 2025-09-12 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| a421d771-0bba-3300-9ad2-3c84d448fe76 | -7.8536 | -45.3839 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 711bba8d-baa7-3055-87d9-5226512ccee1 | -11.6567 | -50.5817 | 2025-09-12 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 60b279e7-5275-35e2-b8c7-83f3d163ca4b | -8.4893 | -47.2694 | 2025-09-12 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 7cb83996-3d6c-31df-8b8e-9f03a56972a3 | -6.3092 | -42.2072 | 2025-09-12 13:50:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| c4fdf49e-3bb0-310b-bc21-5e6634612117 | -14.4588 | -47.3174 | 2025-09-12 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f91401f9-97f1-3af4-98f6-0497fa79095e | -10.0754 | -47.1686 | 2025-09-12 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2a807eb0-d602-3883-8312-535846d06644 | -8.9749 | -46.1054 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 028c5c3c-6eee-311d-9893-dd8fb53c5990 | -10.7172 | -48.6371 | 2025-09-12 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3fad6684-d743-3849-8fb0-7096f1718b2b | -9.673 | -47.5459 | 2025-09-12 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 272.5 |
| a1a8945f-773b-3973-b8af-380192cd6a2a | -10.1133 | -47.1642 | 2025-09-12 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 28ccfbf3-6c3f-32ee-b227-475c32b9e208 | -11.9332 | -51.1683 | 2025-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| e005b12b-b137-3573-8429-f23b5caa3379 | -19.1522 | -50.7565 | 2025-09-12 13:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| b769f832-6ce0-3e7c-a997-7f1b8fff93a6 | -11.9904 | -51.1618 | 2025-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4092bbf1-f4ae-38c9-a52f-c454c99473f3 | -7.542 | -44.6844 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| bf606cfa-79f7-3e1c-89a0-2e85a4287c14 | -14.5132 | -53.8949 | 2025-09-12 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 2bf21095-77a9-3a47-a8f3-3f924008ab6a | -8.8899 | -49.945 | 2025-09-12 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0729d7e7-07f5-39e9-affa-e72833ab8e4e | -13.2798 | -51.7312 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 695435b8-39c5-3c73-bbda-35892890849b | -8.9371 | -46.1094 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 73419672-3f35-39ef-b3be-024d74bed164 | -10.8781 | -45.5826 | 2025-09-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7393af39-acab-3235-b121-89452d4a491e | -6.3226 | -53.4553 | 2025-09-12 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3ed9cade-26e8-3ce1-982d-9089a503a50e | -8.4331 | -47.2527 | 2025-09-12 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 478a202e-98a5-3288-8dbc-1a0df1282739 | -10.6979 | -48.6612 | 2025-09-12 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 84245b26-36a9-3f7c-9013-fd24027d4657 | -7.5641 | -44.4068 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5e752cd2-c657-3e4e-949a-f1de6d1e5bb3 | -10.3504 | -50.5516 | 2025-09-12 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6e76f62a-c536-333e-a530-0d44fc797166 | -13.2801 | -51.7099 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 260.5 |
| e3f2e86e-d254-3362-8456-34dc7fef18e5 | -10.4249 | -50.6291 | 2025-09-12 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8a904989-cdb0-31a0-b39f-9dfc65809c36 | -10.4441 | -50.6059 | 2025-09-12 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 210.9 |
| c2d19573-dba9-368e-824d-b5ca32f8e97d | -14.2732 | -45.053 | 2025-09-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| bf727b2a-c524-3336-84af-ea28a4938022 | -7.5643 | -44.3838 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c8aa338c-2cca-369e-83e3-12eb890216e5 | -12.9292 | -54.7538 | 2025-09-12 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 210.9 |
| e46deaf4-6778-3411-81b9-1ad07fd3ae16 | -11.1064 | -51.9748 | 2025-09-12 13:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| a310ee7a-efe7-3dd4-a9e7-d471196dac1a | -13.1838 | -51.7429 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5d225ab7-597f-317e-88f3-ed575d0b2487 | -11.4285 | -43.5544 | 2025-09-12 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 1d4d5a23-6c64-317a-b854-a81f34bb7ea6 | -10.1405 | -47.9133 | 2025-09-12 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 12ca9e44-616e-3c9c-80c5-f417f6c867e0 | -8.9368 | -46.132 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 251e376d-c1db-3fe4-822d-27bf9f8ec0f1 | -21.6194 | -46.7875 | 2025-09-12 13:50:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| 966cdae8-145f-37f1-ada6-f1549c2eaa6c | -15.5819 | -54.7637 | 2025-09-12 13:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 094d83f5-d14e-3118-b725-4b034c77ed18 | -14.2727 | -45.0765 | 2025-09-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 1715a1d9-10c4-346b-9b11-52ebcea05dea | -11.9329 | -51.1896 | 2025-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 54db27d1-ea06-381d-9504-52aa4c8e4411 | -11.9713 | -51.164 | 2025-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f14929f4-e5ac-30d3-9f91-33b52a69cca4 | -6.8184 | -45.6349 | 2025-09-12 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f56bc0c9-5335-36f9-8ac1-0e2828aa4f93 | -9.0748 | -47.1224 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 167295e9-b61f-3ee8-81f7-edab9f38dae0 | -11.5422 | -50.6161 | 2025-09-12 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| a5615d06-112d-31fd-a45e-2141a1a0c7d3 | -9.77 | -46.0163 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| acdeb252-bbf7-38c9-8617-2175b34a5efe | -15.1169 | -52.4705 | 2025-09-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f8003dca-428e-342f-ada3-b7e6edfb5394 | -11.429 | -43.5307 | 2025-09-12 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 77c1ad4e-fa64-36b9-8d3b-be325152565f | -9.0376 | -47.0819 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| dc2372da-feb0-3ef5-a6b3-f24c7526b4c6 | -8.2085 | -45.5981 | 2025-09-12 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 961a5998-9d2c-35bb-b836-50af302c38b8 | -9.5324 | -54.6277 | 2025-09-12 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ed5900c4-89dd-348d-b3d3-8bb7931c3f12 | -14.1907 | -46.2012 | 2025-09-12 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 4829e595-7a55-3846-8d36-7093eee9d1c6 | -11.5425 | -50.5947 | 2025-09-12 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 647e948e-a25b-3894-bc61-525c4b188545 | -12.9098 | -54.7763 | 2025-09-12 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3673051c-772c-36a3-97c4-bf07abe19095 | -14.1717 | -46.1815 | 2025-09-12 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| d437ea08-a931-3f55-8998-af05e3131ac8 | -9.057 | -47.0355 | 2025-09-12 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 37bf8c01-f873-307e-bee8-8d58b72ebb79 | -7.321 | -49.6468 | 2025-09-12 13:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f7c72db9-7add-3580-8fee-aef7ad3e4c97 | -8.9563 | -46.0849 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 14998411-9b5a-35f5-b7f7-8e6c146c3b40 | -10.0717 | -46.116 | 2025-09-12 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f3bcb78d-0dfe-397a-a063-e90bfe086cd2 | -6.6837 | -44.142 | 2025-09-12 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| adb32549-8254-3899-85e0-5a55efd452e0 | -10.8785 | -45.5597 | 2025-09-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c93552e0-afd9-3fd2-aa55-c2dc66bc5f47 | -9.0759 | -47.0335 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0784bfa6-2782-3853-a0d7-4b86ce9dbce5 | -9.72 | -46.8749 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 09baec80-1c27-3f40-aadd-ec7beca62c9a | -11.4208 | -48.5756 | 2025-09-12 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 17e3008f-9467-3515-97fb-a901955acaf3 | -14.5128 | -53.9158 | 2025-09-12 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8667d00b-e983-3213-bc7f-acad3c60af85 | -9.7197 | -46.8972 | 2025-09-12 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| bfa1e737-9604-3c2d-9b97-89ea0bfd9c62 | -15.0246 | -50.1148 | 2025-09-12 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d76d14e0-7e12-30b6-a87d-9487c88345f3 | -9.5137 | -54.6292 | 2025-09-12 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 4f67b5db-ea89-34d2-a684-342715140632 | -9.6733 | -47.5238 | 2025-09-12 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 30cfaa40-150f-340d-8415-cc710c54d459 | -7.5455 | -44.3856 | 2025-09-12 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |


[Clique aqui para ver as próximas entradas](README133.md)
