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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4daba7b8-7354-3f14-89e1-ef6441a5a454 | -7.3208 | -45.9968 | 2025-10-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3fa24df1-dc76-3f6a-bccd-1e317ab206a0 | -13.304 | -48.0798 | 2025-10-05 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ad3b59a2-6584-380f-8b52-8950ce570bde | -7.7301 | -46.3185 | 2025-10-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| cb679ad3-c372-33cd-a549-c86af9ecc03c | -13.3233 | -48.077 | 2025-10-05 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8e475899-e756-3328-80d7-125c761f504c | -13.3036 | -48.1021 | 2025-10-05 00:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bfa62d34-c14a-3505-a28a-9485d79cde6b | -11.4535 | -51.5177 | 2025-10-05 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6d2c3879-8428-3cb3-87c2-2c7d54fb1410 | -5.655 | -43.9013 | 2025-10-05 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| eb92f57a-405b-36bd-b927-8f32b0c0a709 | -15.2351 | -49.2914 | 2025-10-05 00:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 56a5984d-70ef-3279-8066-2a9563fb690b | -7.7885 | -44.5228 | 2025-10-05 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4dd81539-eb27-30b0-bfc4-6bcb7cd7e382 | -4.6318 | -43.1816 | 2025-10-05 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 211.7 |
| ba3f5785-e5a2-3960-b742-08578813fce9 | -22.12706 | -42.91323 | 2025-10-05 00:28:00 | TERRA_M-M | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| cf81ce37-525b-34a9-9244-0d9efc1aafe0 | -21.07156 | -49.08716 | 2025-10-05 00:28:00 | TERRA_M-M | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.1 |
| 69599f75-a957-3553-b1af-5fa4365ee882 | -21.06184 | -49.08857 | 2025-10-05 00:28:00 | TERRA_M-M | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 006f6215-1057-3053-94d2-fc399ae59591 | -21.81996 | -47.39633 | 2025-10-05 00:28:00 | TERRA_M-M | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 00522e34-40d4-35d2-9687-ce424e0e4c80 | -22.12421 | -43.30064 | 2025-10-05 00:28:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 96e69422-13be-31ff-95a4-8f0deba46c46 | -21.81864 | -47.38618 | 2025-10-05 00:28:00 | TERRA_M-M | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 77eb21b7-57dc-3419-b15c-9be8fcacd44f | -22.7028 | -44.45766 | 2025-10-05 00:28:00 | TERRA_M-M | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 204c7b4e-4e6f-3c27-9439-256e4cd621a1 | -7.7301 | -46.3185 | 2025-10-05 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f58e5447-ad9d-3768-bc0b-15be7ac74ef0 | -4.4258 | -43.2408 | 2025-10-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 615aebfa-81bc-39a3-ac44-9066d82e16c1 | -4.3197 | -48.0908 | 2025-10-05 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bbb3fc89-1b6a-3911-accf-4f404fae85f6 | -14.3348 | -47.6981 | 2025-10-05 00:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b62abc39-79b8-31aa-869a-74d8e2252fec | -7.8074 | -44.5209 | 2025-10-05 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9f662c65-5262-374b-a78b-60e12a51f379 | -13.1397 | -50.9169 | 2025-10-05 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| cdb493b8-684f-3807-a808-4fed5487ff8b | -12.573 | -48.1615 | 2025-10-05 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0d53d806-6587-3279-b637-18b6164544d6 | -11.7519 | -44.7461 | 2025-10-05 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5abc0bad-875e-35df-ae90-1c24e2f4b3e2 | -23.003 | -52.7309 | 2025-10-05 00:30:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 187.2 |
| c942e51e-cc56-3ca5-8ddc-e20f5e16048a | -14.6711 | -48.3381 | 2025-10-05 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1395b007-0dfa-3f5d-8efc-d84bb811289f | -23.024 | -52.7265 | 2025-10-05 00:30:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| c8d27386-3b13-3c5b-a620-7742dfbd4647 | -6.4131 | -43.0724 | 2025-10-05 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| ea525c92-be32-38ab-a9b4-053ca5fa7ac0 | -12.4673 | -45.4925 | 2025-10-05 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| cb035fa2-fa9b-3750-b6ce-3064c0db9643 | -11.4535 | -51.5177 | 2025-10-05 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fd6fd6bd-766f-369b-acab-74f099de24bd | -6.4398 | -44.1396 | 2025-10-05 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 334055d6-a6c1-33f7-8a27-394dd9d1302a | -11.8588 | -56.8785 | 2025-10-05 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 444a8527-d8e8-3cc2-86e7-0c306da12b78 | -11.8777 | -56.8769 | 2025-10-05 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| a897d6c4-bcb3-3945-b625-0165c84bc8e1 | -13.1589 | -50.9144 | 2025-10-05 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7f55c6d8-3f45-3c47-a610-b638c4875108 | -12.4665 | -45.5386 | 2025-10-05 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e9675b0a-81a1-37ee-92ce-a0bb715d1bf4 | -4.6504 | -43.2038 | 2025-10-05 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| fcf1194e-0ca8-3d9d-b37f-550a49211d43 | -4.6318 | -43.1816 | 2025-10-05 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 40cf5f34-056d-3621-896a-5a1322e939ff | -6.4396 | -44.1627 | 2025-10-05 00:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| c1117dbd-a24c-384e-8db9-0e8bb30bfd35 | -7.7883 | -44.5458 | 2025-10-05 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ac5b2643-cf3b-306b-94e3-4be37a0167b7 | -5.6548 | -43.9244 | 2025-10-05 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| ae7abb3b-c953-32f8-992d-1c0d94dba7f9 | -8.5384 | -46.3304 | 2025-10-05 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e4f09063-96a2-3f12-af85-a5cdcdb3849e | -13.3036 | -48.1021 | 2025-10-05 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 50d13016-365c-3e25-bf23-12a1c2bf8a65 | -13.1585 | -50.9359 | 2025-10-05 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| af299a90-c20a-3446-8ec5-3c1ab89eedb4 | -23.0024 | -52.7533 | 2025-10-05 00:30:00 | GOES-19 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 3cd37f0a-8060-3160-89dd-b1f139c37d6d | -7.7885 | -44.5228 | 2025-10-05 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b743cfb1-81dc-3f6f-b992-ac17e53ffab6 | -10.8379 | -57.1781 | 2025-10-05 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 6409388e-07af-3286-9277-e28a007ca0b4 | -11.823 | -45.0596 | 2025-10-05 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 817db251-ae56-3778-ad60-5e5aedb05089 | -12.4624 | -44.7298 | 2025-10-05 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 12ec9485-ff9f-38bd-b6e3-4f66ac76a829 | -4.6505 | -43.1805 | 2025-10-05 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 292.1 |
| 41209327-3811-3a52-a68b-66963c1f5b2c | -11.8225 | -45.0827 | 2025-10-05 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9f46911b-4705-3979-bf72-eef1e7d6ffa9 | -15.928 | -48.822 | 2025-10-05 00:30:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 699088c0-8531-3ebd-b8e8-3679fd5b7ca1 | -5.655 | -43.9013 | 2025-10-05 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 6d2c5c91-2e72-3e8e-8213-43175493adbf | -13.1393 | -50.9383 | 2025-10-05 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 265.7 |
| 3e16f8ed-e8cd-312a-9965-58e501d22be4 | -12.4476 | -45.5185 | 2025-10-05 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 335538ac-ab8e-3f68-9eb0-b0604c139a5f | -4.6317 | -43.205 | 2025-10-05 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2275db02-c355-3d0b-803b-ae812464415b | -15.2351 | -49.2914 | 2025-10-05 00:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2d99cea4-b6b7-30ec-8ecb-26e29d41e9e2 | -6.4134 | -43.0489 | 2025-10-05 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| e9d5a4eb-036f-30a8-aa37-40b824f0685d | -4.4445 | -43.2397 | 2025-10-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 147ff4c9-323e-3c3c-9bf5-4e06f009be7b | -19.8482 | -46.5143 | 2025-10-05 00:30:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b4aa97b6-d04b-3b08-97b9-43c207b2bd50 | -4.6507 | -43.1571 | 2025-10-05 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 09ea43b4-9431-3b93-8492-c2f1ab903579 | -8.5387 | -46.3079 | 2025-10-05 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b0afa842-db1e-3bc5-9485-c3051cc0a74c | -6.3943 | -43.074 | 2025-10-05 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 078f7350-444c-3d77-bb22-73545ba97758 | -14.3353 | -47.6755 | 2025-10-05 00:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 85ff478b-43a5-35ed-83c3-258bd99eaddc | -7.1509 | -46.1011 | 2025-10-05 00:30:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c4b1cb97-4c66-3213-987e-0a8d34112a83 | -12.4669 | -45.5155 | 2025-10-05 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 9d542ad0-753b-3580-af4d-96a3d25086d9 | -5.6361 | -43.9258 | 2025-10-05 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7367158e-e82c-35c3-a2cf-7b3b483394c5 | -10.4054 | -45.3931 | 2025-10-05 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ad831a95-32bb-342e-86a4-28ca410ac930 | -7.1512 | -46.0787 | 2025-10-05 00:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 08d68e44-1adc-3057-b579-0544f7cc1e9c | -10.6052 | -54.3584 | 2025-10-05 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c0965953-82f5-3710-9599-c4c0600a6bff | -13.139 | -50.9598 | 2025-10-05 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 24acf8ff-6af8-30ac-ae98-5ac3e4416b1d | -8.4354 | -70.1117 | 2025-10-05 00:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 834f361d-7b24-3034-9628-96643a7b88bb | -15.9084 | -48.8254 | 2025-10-05 00:30:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 73cf057c-00b3-3956-88e0-b943ce37b746 | -8.4353 | -70.13 | 2025-10-05 00:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 11762434-475c-3086-bc1b-36ed35c9ebdf | -5.6363 | -43.9027 | 2025-10-05 00:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 0e2350e4-c22d-3ace-af05-ab71ee0c8cf2 | -5.9226 | -43.3236 | 2025-10-05 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b863f090-c033-3d76-8a30-3b7d180a7eee | -6.3946 | -43.0505 | 2025-10-05 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 468034a6-41fa-36d7-a316-1a4160880c99 | -15.3019 | -47.9428 | 2025-10-05 00:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ed108ea3-75ad-3045-9c85-1387320900c2 | -18.00441 | -45.00609 | 2025-10-05 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f1d397c-2b58-335f-8036-49019cdc1016 | -15.97274 | -43.3285 | 2025-10-05 00:30:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f0fd931-62e2-3e3a-88da-d8a13e90213f | -17.94624 | -57.61068 | 2025-10-05 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 17de7b52-ef9c-38b8-afb9-82b9fd3026a9 | -18.40145 | -42.78745 | 2025-10-05 00:30:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 458c4488-ce8a-3472-9a46-c1fbb14018e7 | -17.97696 | -45.01081 | 2025-10-05 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf3f5817-31a9-3db0-a29c-ff1fcbc05839 | -16.41904 | -43.75045 | 2025-10-05 00:30:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9432a129-8ef5-38bf-9cf6-a667711dc119 | -18.33572 | -45.88997 | 2025-10-05 00:30:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d86ad293-d46c-37bc-b9fd-f433471e86df | -19.51624 | -50.37754 | 2025-10-05 00:30:00 | TERRA_M-M | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| eb842462-3431-3747-92da-62137239900a | -19.9531 | -44.64657 | 2025-10-05 00:30:00 | TERRA_M-M | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2a63ab3f-c503-3e21-a8c8-0b480dba5d86 | -15.96236 | -43.33021 | 2025-10-05 00:30:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a133bab0-2442-3651-8488-623abba6685d | -17.20331 | -44.45677 | 2025-10-05 00:30:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 822e0540-8bfc-3f1e-8683-c53e9d4a2700 | -20.72922 | -49.61676 | 2025-10-05 00:30:00 | TERRA_M-M | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 3ae9c09a-4a3a-3484-94c9-70a920e265c4 | -17.72894 | -44.39917 | 2025-10-05 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3b4eb219-e794-3a3e-b14f-c35234ec5d42 | -19.51472 | -50.3644 | 2025-10-05 00:30:00 | TERRA_M-M | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 55591cd4-09a8-3647-964c-5f5329fe9e4d | -15.96032 | -43.31747 | 2025-10-05 00:30:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e4afad75-c29c-3b63-88fe-5fa06d8687fd | -19.63745 | -45.9691 | 2025-10-05 00:30:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3eee6161-40ed-36ec-885b-47f0710335e8 | -19.78242 | -47.7725 | 2025-10-05 00:30:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| db78ac06-41ac-34dd-b593-0a781deaebce | -15.82207 | -42.61731 | 2025-10-05 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c2cc7361-fae4-3a39-98eb-92ad2f360da0 | -17.94738 | -57.6051 | 2025-10-05 00:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 7d7c0226-2bed-3121-a0c6-5084f3794077 | -18.33438 | -45.88053 | 2025-10-05 00:30:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d629fd96-a64b-32ec-a061-6b57543ded4b | -18.8503 | -44.67909 | 2025-10-05 00:30:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 240534f6-6530-3d34-9275-ebe35aa22cac | -17.57078 | -46.08026 | 2025-10-05 00:30:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README4.md)
