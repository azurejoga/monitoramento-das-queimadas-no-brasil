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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa3cec54-ed56-3b91-a5b6-edded8efc19b | -18.83902 | -46.4461 | 2026-09-03 04:59:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebb6140f-d2d0-3219-a681-8bc6253cd79f | -14.49745 | -59.83868 | 2026-09-03 04:59:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c2036a0-48ed-3c86-9914-de558342d411 | -15.0802 | -51.45451 | 2026-09-03 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c5d9b50-a351-389e-97bc-b5354b9af9bc | -11.31784 | -56.3684 | 2026-09-03 04:59:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93995663-7ead-368c-b8e2-87972650444f | -13.58123 | -47.88326 | 2026-09-03 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebcd87d8-d9e5-3da4-b8ca-69bbd866486c | -18.16858 | -51.80072 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 903b602b-ad72-3862-91ab-8cc7745aa762 | -17.13112 | -55.92566 | 2026-09-03 04:59:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 437a49bd-0bc8-3f08-9253-a80f9960a0cb | -17.07917 | -56.845 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 50241582-f734-3b8d-9ec2-1c916bd158ce | -18.82747 | -47.59937 | 2026-09-03 04:59:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7be23f90-20a9-399c-8004-4987a0085266 | -13.37577 | -51.34822 | 2026-09-03 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ffdec22-84b1-3f5c-b622-86859d91f6c6 | -14.05295 | -48.40552 | 2026-09-03 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a1d50a3-9b54-38ea-a4d3-36abe8cd934f | -17.08556 | -56.8694 | 2026-09-03 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ab781083-b557-3767-90b4-5126fd30e991 | -18.13647 | -51.81443 | 2026-09-03 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92b6ac6f-7caa-3a4a-a7a4-4b3958704462 | -6.7648 | -59.4408 | 2026-09-03 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 8669cc29-1348-376a-8cc8-cca3c302b070 | -8.0924 | -50.9642 | 2026-09-03 05:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 063701f8-2811-3295-822e-d31bc20a20c9 | -11.3346 | -50.5325 | 2026-09-03 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 2de95d62-8ed3-3936-97f7-7ce0700e2d25 | -8.4677 | -54.6429 | 2026-09-03 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 357727d9-afb4-3b81-a9a6-34d95a8f3320 | -6.6541 | -59.4452 | 2026-09-03 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 590b717e-2ddc-3f2d-9722-c299b8582e00 | -11.3156 | -50.5346 | 2026-09-03 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 494194c8-ce7b-3f9a-9d4f-b0a4bf7c0cb6 | -6.3052 | -56.0442 | 2026-09-03 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| c5584b8c-7280-3147-8892-3a303c638763 | -6.3237 | -56.0434 | 2026-09-03 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 9bbbd3b9-8ae0-31c8-9d4a-370b4d84003f | -6.6698 | -59.9443 | 2026-09-03 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3f36a8f3-c020-32c3-8dd1-7131afd8facc | -11.316 | -50.5132 | 2026-09-03 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 59cb5072-50bd-3182-adb6-5b2cbc75bca4 | -6.6357 | -59.4459 | 2026-09-03 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 9f555cc8-7728-3b3b-8ee7-4386bb1077b2 | -11.297 | -50.5153 | 2026-09-03 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ee2713a8-5788-32e1-9ba5-90ba43eafae0 | -11.335 | -50.5111 | 2026-09-03 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| bdb616e6-64b3-37f7-9e60-61f230f18899 | -6.6883 | -59.9436 | 2026-09-03 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| c9d4f631-c844-3957-91f8-6aa1eb9d54bd | -7.566 | -61.343 | 2026-09-03 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 534b528c-722b-310f-9ce5-c8a388c3f214 | -20.14395 | -54.69221 | 2026-09-03 05:01:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b32ccc4-8035-3aed-9d5f-e585c2cc7f16 | -19.09939 | -57.3616 | 2026-09-03 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f319b0f3-73cc-303e-b9a0-40f0c5d720c1 | -18.783 | -48.91613 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03418500-a3d5-37c0-9f40-4d0c14f37c31 | -25.38334 | -52.11571 | 2026-09-03 05:01:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 26e0ffe9-bd56-360f-9d72-e1e42ae6dd32 | -19.35544 | -47.09438 | 2026-09-03 05:01:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42285043-8a1e-31bc-a01b-2ca98b77f358 | -18.2346 | -55.39682 | 2026-09-03 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 733801de-e84b-3035-b7b3-9ce17e58f85a | -21.8953 | -55.37322 | 2026-09-03 05:01:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d1baa794-6ff9-3928-84c4-42c4bbebfb09 | -20.86371 | -57.71178 | 2026-09-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bbc144d5-ab76-3ecb-99a8-2e4077e5df19 | -19.09137 | -57.36795 | 2026-09-03 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a1c7eb4b-728c-3047-aad4-0ef391067854 | -20.44249 | -53.7754 | 2026-09-03 05:01:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a7c2d03-d442-3223-a59d-f3d1a4d1f2cf | -20.81956 | -57.66395 | 2026-09-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 85675db5-1f27-3833-8998-c64da00dbedf | -21.68967 | -56.52246 | 2026-09-03 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 145aa593-caf4-39da-9835-93acb6123d7e | -21.05725 | -55.83776 | 2026-09-03 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ecaeb24-e63b-3bba-be44-91161fc899d3 | -20.4448 | -53.77282 | 2026-09-03 05:01:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6289be1-009f-3029-abbb-f19bdee6b6a8 | -22.42994 | -49.76834 | 2026-09-03 05:01:00 | NOAA-20 | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74530ea4-b57c-323f-940c-2ef5d079f904 | -18.7791 | -48.91093 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2ecb0ce-fd20-3cfb-a782-b4752c9ff05c | -19.09497 | -48.49349 | 2026-09-03 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 379f40d8-dbd6-3a9e-81e4-2e7e7650c075 | -18.77798 | -48.92007 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 135f72b1-7e3a-3136-9468-9db99870b0fd | -18.78244 | -48.92066 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e61f9af-6e39-305b-a73b-795755394021 | -18.77408 | -48.91487 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0210fa37-1240-3793-b9a7-0115c76f722a | -19.08799 | -57.36732 | 2026-09-03 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7d3d5c0d-5ffd-3111-a666-bf91fd3faf31 | -18.77854 | -48.91552 | 2026-09-03 05:01:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f20de27-fafd-329e-93ec-f2aa6826fa44 | -18.23402 | -55.40045 | 2026-09-03 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 65adf37f-1f34-3168-9d99-c1e8f437cf70 | -19.09473 | -48.49088 | 2026-09-03 05:01:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1578c903-701c-3f23-98a7-404f40e12e69 | -22.43438 | -49.76891 | 2026-09-03 05:01:00 | NOAA-20 | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| de9b092a-dac4-3d7e-a1d6-1a8c8457de03 | -21.89865 | -55.37381 | 2026-09-03 05:01:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2319110-f871-3acb-b365-d2d39aab9e00 | -27.03057 | -52.66726 | 2026-09-03 05:04:00 | NOAA-20 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa48b600-a944-33dc-afaa-b986295acfde | -31.34092 | -54.07079 | 2026-09-03 05:04:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 3ba1133c-7344-31d2-9acf-5a38c6559f2e | -6.6357 | -59.4459 | 2026-09-03 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 5eb697e1-7a44-3da5-ac46-cd552e92c5cc | -11.3346 | -50.5325 | 2026-09-03 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e55e4473-6727-3c0c-8834-34ca877bb305 | -6.6541 | -59.4452 | 2026-09-03 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| f495adb9-a72b-3726-9699-1f75078f09c9 | -8.0737 | -50.9656 | 2026-09-03 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 41d30571-8388-38f8-a2bd-7ce9035d3b37 | -6.3052 | -56.0442 | 2026-09-03 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b87246bf-08b8-3f5e-b697-c41eb35f9699 | -8.0924 | -50.9642 | 2026-09-03 05:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f85c9bf6-cfc5-3473-829e-0a1167394474 | -11.3156 | -50.5346 | 2026-09-03 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f775c19b-381f-3f40-b554-912fbb1494a2 | -6.6883 | -59.9436 | 2026-09-03 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f3ca4cd0-4e9b-377d-81e7-02cffe713ae4 | -6.3237 | -56.0434 | 2026-09-03 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 36347294-6831-3265-bec6-2ee4830181f9 | -6.6882 | -59.9628 | 2026-09-03 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 76901194-dcf7-3d1e-88fb-c84dce37bf1b | -6.6698 | -59.9443 | 2026-09-03 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| bb9cf247-7434-3de7-acb5-f111d040bf3f | -11.297 | -50.5153 | 2026-09-03 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 553565c1-5a28-3cfc-968d-f12bdaa1d859 | -11.316 | -50.5132 | 2026-09-03 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| ae1be088-8e92-3d4e-b65c-677273bd8f8e | -11.3156 | -50.5346 | 2026-09-03 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7124346b-7942-39c8-a07a-a42ec7b7fdab | -6.6541 | -59.4452 | 2026-09-03 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| e931c8b4-fd60-35ce-a1f1-a19db96a1348 | -11.316 | -50.5132 | 2026-09-03 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ca2e5027-166f-3320-8045-cf64ccedf9c1 | -6.6698 | -59.9443 | 2026-09-03 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 062b8c1a-9ae8-3eae-b6ec-0375755f5eb9 | -8.0922 | -50.9852 | 2026-09-03 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b063f28b-8a46-39a0-9f50-cd64b51cd12d | -6.3052 | -56.0442 | 2026-09-03 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1d76b9e8-3116-3e9d-b81e-e14194076b93 | -6.6883 | -59.9436 | 2026-09-03 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8624c28f-6031-30b3-86d3-a86e22cc8157 | -8.0924 | -50.9642 | 2026-09-03 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 7cf78bca-df9e-3e84-b611-25e471531cc1 | -6.3237 | -56.0434 | 2026-09-03 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8dabd986-4281-3585-b861-81ae5472d08b | -6.6357 | -59.4459 | 2026-09-03 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 4a65b37b-ed30-3362-ae2e-a2e5a3e74e86 | -8.0737 | -50.9656 | 2026-09-03 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 594d162b-7511-3200-b6bd-656c2ba38703 | -8.0735 | -50.9866 | 2026-09-03 05:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 66a47e40-78fc-348a-b25f-1b12afe1ef0e | -11.3156 | -50.5346 | 2026-09-03 05:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c51a24e0-f8e4-3a18-afb1-9247c43f5b59 | -8.6132 | -62.5739 | 2026-09-03 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 779058a7-7e3d-372b-958a-0f08987b53f4 | -8.5948 | -62.5557 | 2026-09-03 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f092232e-e80a-39bb-9c77-6f7038f5d6ec | -6.6357 | -59.4459 | 2026-09-03 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c966dfc2-f99a-3406-9e51-18c374b4360f | -8.0924 | -50.9642 | 2026-09-03 05:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| be8ed300-9ba4-3715-8f5a-ee1865cd0f3b | -6.6882 | -59.9628 | 2026-09-03 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 06b058ec-9550-39bc-ad58-6cad3fc93c73 | -11.0006 | -45.0847 | 2026-09-03 05:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0304bea8-663c-3d9b-91d9-3542cbf3fadb | -7.566 | -61.343 | 2026-09-03 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 95cf79c9-c4c9-3b55-9b40-673cae98fab0 | -6.3237 | -56.0434 | 2026-09-03 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 92c57851-30ab-3af3-b42c-830321e6de35 | -11.316 | -50.5132 | 2026-09-03 05:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0f497385-1bc5-3406-b098-6fa7b79e635d | -8.5916 | -67.1788 | 2026-09-03 05:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 267e0f44-e8c7-39f1-9b74-0ed3a3a8f811 | -6.6883 | -59.9436 | 2026-09-03 05:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3b670267-a419-3c0f-abe8-c5307537e421 | -6.3052 | -56.0442 | 2026-09-03 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 87dd93ac-ba98-3f1c-8e80-a5939b7207e3 | -8.6133 | -62.555 | 2026-09-03 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| eeca05a3-34a0-35de-9b18-70239191c1c7 | -12.4033 | -44.8089 | 2026-09-03 05:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3275eea2-fb1a-3448-8706-a84eff57fd77 | -6.6541 | -59.4452 | 2026-09-03 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 69b2dede-e985-305b-9c1f-9f48dd1ed02a | -11.0006 | -45.0847 | 2026-09-03 05:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e5765b66-1a10-3182-8ba9-c7a41bd579c4 | -8.0737 | -50.9656 | 2026-09-03 05:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| df37b711-494e-39bd-b23b-37b7f9196f34 | -6.6883 | -59.9436 | 2026-09-03 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |


[Clique aqui para ver as próximas entradas](README43.md)
