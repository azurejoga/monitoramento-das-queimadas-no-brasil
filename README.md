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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49046468-05db-32ce-9b15-b216d2b92a94 | -7.7885 | -44.5228 | 2025-10-05 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 51bfecff-5032-3704-b395-103c03473b82 | -10.3864 | -45.3955 | 2025-10-05 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 0248bf77-a741-33b2-85b4-07aa9a437a67 | -12.4669 | -45.5155 | 2025-10-05 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 29380215-598b-3c24-945e-185d9a9dda79 | -7.1512 | -46.0787 | 2025-10-05 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| dfa88d32-c62b-3c8d-a954-e45091e00c38 | -5.655 | -43.9013 | 2025-10-05 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e0bab950-1319-363b-b446-62d2bf70fb23 | -4.6504 | -43.2038 | 2025-10-05 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| eae76fac-1667-3d39-b279-64cfbd32a104 | -7.3208 | -45.9968 | 2025-10-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 47c76632-71dc-3648-99bd-0f302a811148 | -4.6317 | -43.205 | 2025-10-05 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fafb24fd-c3d3-3fde-89d7-6cf699148415 | -11.8588 | -56.8785 | 2025-10-05 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f9b3b609-26f1-3294-927e-3417449bb203 | -6.1536 | -44.6675 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 5cdc5f15-bb59-3548-84d1-7ac193f369b5 | -11.0101 | -50.6958 | 2025-10-05 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3413242c-0619-31d5-9c78-21e8b0138fc0 | -14.6902 | -48.3574 | 2025-10-05 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 11f8a500-f29a-32b1-afa3-de04665ff6c1 | -11.7519 | -44.7461 | 2025-10-05 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 413cf08f-202e-3150-81d1-669506e36912 | -13.139 | -50.9598 | 2025-10-05 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 03f84100-cffd-3ce6-ab93-1141b3e4543f | -11.4535 | -51.5177 | 2025-10-05 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2fa0ad74-0f4a-3aa5-b488-67005e6ecc37 | -7.8074 | -44.5209 | 2025-10-05 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 8b000971-9d74-3d92-8107-54b113cf6434 | -10.4054 | -45.3931 | 2025-10-05 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9a598397-a3ea-36ab-9760-ffc0c15c1990 | -10.5863 | -54.36 | 2025-10-05 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6418849d-47a0-381f-a737-79253ab65591 | -13.1161 | -43.847 | 2025-10-05 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d917c01c-9e7b-33da-9eac-b20448502c7a | -21.0587 | -49.0977 | 2025-10-05 00:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 4f3ef5e4-adaa-3b0e-b5ed-b5611f91dda1 | -8.4354 | -70.1117 | 2025-10-05 00:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2f31b568-ea6d-350a-b4b0-17f200f07d6d | -7.786 | -49.8457 | 2025-10-05 00:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 99a4326d-6dcf-3061-99e4-5dc799346fae | -14.6906 | -48.335 | 2025-10-05 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| fc954efd-8411-327a-835e-f11cc4af46a9 | -5.6548 | -43.9244 | 2025-10-05 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| c6dd1802-748e-3b06-834e-870afe7db781 | -4.6318 | -43.1816 | 2025-10-05 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 9ba32f9b-b0a4-36c3-88fb-45a2ae23ad70 | -6.4134 | -43.0489 | 2025-10-05 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| bc6a0e6d-f38d-3801-b899-f04435837f44 | -15.2351 | -49.2914 | 2025-10-05 00:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0c17b7a8-91c8-39ad-84b9-59ab04d32938 | -12.4673 | -45.4925 | 2025-10-05 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 3ec26351-3170-3a18-85d0-5d30059822a9 | -5.6361 | -43.9258 | 2025-10-05 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7902e9da-1050-3e0e-b5ea-80673337332e | -10.4592 | -57.5029 | 2025-10-05 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 39bca1eb-ddf8-3611-a9b2-5c0f97a24760 | -4.6507 | -43.1571 | 2025-10-05 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 03003136-ce40-3d55-b1bc-e7b89fb98b80 | -4.4445 | -43.2397 | 2025-10-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| d6a342e3-69de-33a6-bcb0-dc844e586c28 | -8.5387 | -46.3079 | 2025-10-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| dcc2e0c8-400f-307d-b8fa-d1f25e1f8372 | -6.3943 | -43.074 | 2025-10-05 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5fd4302f-03d8-32a7-a9f8-d8833b19b838 | -6.1351 | -44.6461 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 3b186361-d870-3f79-a19f-7e5945f92f42 | -15.928 | -48.822 | 2025-10-05 00:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| daac9e13-cbae-3e9e-8ad0-341fe3d60634 | -7.1699 | -46.0771 | 2025-10-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 4bc3b6ae-061a-3213-ba63-a37632b9a5f1 | -8.5956 | -46.2798 | 2025-10-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d097a84b-9117-3cde-9739-a5acaae1c059 | -10.8379 | -57.1781 | 2025-10-05 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 697fa021-a888-3df4-9904-8f69e671a8a7 | -6.4131 | -43.0724 | 2025-10-05 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 224554a8-c898-3e97-a96f-9f2b62aa841c | -2.3012 | -47.9906 | 2025-10-05 00:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 89c5c21e-3f8f-3dfd-925b-5ad6b6811e3b | -6.3946 | -43.0505 | 2025-10-05 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a10c942d-6921-34bb-916d-b6f8af04a80c | -6.4396 | -44.1627 | 2025-10-05 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 5ac1fc7e-6b98-3f2f-8f2f-7cc4113ca329 | -13.1582 | -50.9574 | 2025-10-05 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7bac6906-9cc1-3fd5-8c60-a87cdd28138a | -6.4398 | -44.1396 | 2025-10-05 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 80bd56e4-abbb-3d70-8629-9e85579a978f | -8.4353 | -70.13 | 2025-10-05 00:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 46ec7748-768f-3c02-9ad7-ad6e0f6bc93a | -21.08 | -49.0699 | 2025-10-05 00:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| ac8d50a2-840a-30e4-a6dc-18cba141cdfc | -14.6707 | -48.3605 | 2025-10-05 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 3890eda2-8cfa-3aea-a479-f4a31d1b3274 | -8.4169 | -70.1303 | 2025-10-05 00:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f5c8ec99-9d93-3acc-8654-79a0e046cb13 | -6.154 | -44.6217 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 096f9807-0da4-38bf-8a4c-f6315e870069 | -4.6505 | -43.1805 | 2025-10-05 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 419.8 |
| 09abd008-4eaa-312c-99d3-6e326e6b3a82 | -5.6363 | -43.9027 | 2025-10-05 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 51a29500-defe-33d5-b5b5-4077ff9e3ba9 | -7.7883 | -44.5458 | 2025-10-05 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a9a85f18-5575-3ec8-be12-137e034a1cba | -10.6052 | -54.3584 | 2025-10-05 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0e4425cb-d7a5-3abd-a831-5d729397ca52 | -6.4584 | -44.1611 | 2025-10-05 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 3bcdf1be-e431-3933-b8c1-7ed314d8aa86 | -6.1726 | -44.6432 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e8857871-e520-3ebe-b4e0-300b9b0e63fb | -6.1349 | -44.6689 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| d71056bb-2b75-3456-834f-227235810deb | -11.8777 | -56.8769 | 2025-10-05 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 21285cf0-ef86-3c09-8892-c63276b02b78 | -14.6711 | -48.3381 | 2025-10-05 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2eae2a37-7137-38ab-af7c-0e0b467e3c75 | -11.0288 | -50.7151 | 2025-10-05 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 0c1f053a-9c31-3b6c-98a3-d09e70d468ba | -19.503 | -50.377 | 2025-10-05 00:00:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 071c3ed5-b285-3a61-a2cb-a2d4f0d0aba0 | -6.1538 | -44.6446 | 2025-10-05 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 261.4 |
| a9d2e2fc-8b68-336a-b49a-5f0129f7002d | -21.0594 | -49.0746 | 2025-10-05 00:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 0eb14295-9e35-3dad-9d22-c0afd6f43012 | -4.4446 | -43.2164 | 2025-10-05 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 58c14192-4cba-3377-810f-19c21292899e | -21.0793 | -49.0931 | 2025-10-05 00:00:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.4 |
| 975b1704-87de-332f-8a2f-cc669b8993dd | -4.3197 | -48.0908 | 2025-10-05 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 4b092d25-a016-323f-858e-0e1baea65994 | -2.6883 | -48.3899 | 2025-10-05 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 680122ef-e7d5-30bc-bd82-c8adb4b07083 | -11.823 | -45.0596 | 2025-10-05 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 0c16a047-5501-3cc1-9658-9495d64a3200 | -6.4586 | -44.1381 | 2025-10-05 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5ced603a-8b5e-31f3-b860-a1313c2a4f76 | -11.0291 | -50.6937 | 2025-10-05 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 72e855b1-792f-3102-aed8-0c99125019eb | -12.895 | -47.3134 | 2025-10-05 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7bb00644-b0af-39b2-9a9a-fbb6f342f88b | -7.321 | -45.9743 | 2025-10-05 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| f4bb7986-d1b4-3bf7-b896-17be46321041 | -15.9084 | -48.8254 | 2025-10-05 00:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4cc755ed-4419-3a34-92ad-4ffbca7129a4 | -13.3233 | -48.077 | 2025-10-05 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9e5aa570-8765-353a-b5ba-07463dd908e2 | -5.9226 | -43.3236 | 2025-10-05 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 45412680-c4ba-3b35-bd94-1cb3583cc719 | -13.3233 | -48.077 | 2025-10-05 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6b1059f0-4c2e-3229-87f3-d1568f2377b4 | -6.4131 | -43.0724 | 2025-10-05 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 02bcca64-ee57-36d0-b254-f4a699614fe9 | -4.6505 | -43.1805 | 2025-10-05 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 380.9 |
| b51a8728-04e3-3e7c-97af-cade90ba66c6 | -6.4584 | -44.1611 | 2025-10-05 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f0dfecd1-f32f-3fcb-878a-2bfd7cbbba97 | -7.1512 | -46.0787 | 2025-10-05 00:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c2c68879-5b1f-394c-813d-48308540de44 | -14.6906 | -48.335 | 2025-10-05 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 12e43ba1-8fe5-30a8-8d06-827753ffca6a | -14.6711 | -48.3381 | 2025-10-05 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 5bdbc39e-e0a5-3758-a7cf-5c0da4832bd1 | -15.3019 | -47.9428 | 2025-10-05 00:10:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d9eeacc9-2302-3e93-9c45-6f6cddcff86d | -12.4665 | -45.5386 | 2025-10-05 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 138a9b8e-9889-38fd-8b62-70cd1a293adf | -6.4134 | -43.0489 | 2025-10-05 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 487c8299-b1b4-3f43-a19a-64d3bc0020db | -10.3864 | -45.3955 | 2025-10-05 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0460c853-63e9-31d5-b06a-14529465cecd | -13.3229 | -48.0993 | 2025-10-05 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 18b4f972-66b6-3df2-b815-a4c81c3d62bc | -14.9352 | -46.8507 | 2025-10-05 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 728d19d9-f058-3250-92b4-0183149166f7 | -8.4199 | -46.7885 | 2025-10-05 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 623cf99b-d65f-39d8-9ccd-559af74aa512 | -6.4586 | -44.1381 | 2025-10-05 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 077dc778-4061-326d-9b64-b6a5b26c94fd | -6.1538 | -44.6446 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 309.5 |
| 5c8150c8-b9fe-3ce8-8f6d-f367dd1272fa | -12.4476 | -45.5185 | 2025-10-05 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c9e3cd08-0626-358c-8c77-f310336c61b0 | -13.139 | -50.9598 | 2025-10-05 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 278.9 |
| 910712b8-2239-3167-ba3e-1ca5dff31b7c | -8.4353 | -70.13 | 2025-10-05 00:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2da262c7-4412-36e9-8eab-7b5402efed8a | -11.823 | -45.0596 | 2025-10-05 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9f56b741-4175-316c-b63e-317e6e0a493c | -15.2351 | -49.2914 | 2025-10-05 00:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| aa90c339-5217-35b3-9f30-3bcf28a3ad69 | -13.1161 | -43.847 | 2025-10-05 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e39209fc-4eeb-318b-a844-26bdb03973c5 | -4.4445 | -43.2397 | 2025-10-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 69733c09-05a8-3646-a3f9-4e94b33917d4 | -7.1509 | -46.1011 | 2025-10-05 00:10:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 1c32f7ef-adf5-3c8c-8251-a60919a88e87 | -7.786 | -49.8457 | 2025-10-05 00:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |


[Clique aqui para ver as próximas entradas](README2.md)
