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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8edac13b-c150-3063-b430-7337a60608c8 | -21.87338 | -42.03347 | 2026-09-01 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 340e4632-501f-3d70-881d-b9ef0945f13b | -19.89157 | -47.89927 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a23b0c7-4d72-3466-bece-c73e5668b228 | -18.25764 | -52.74395 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd4f8849-7543-33fd-9bfc-f5286cf3bfae | -18.2549 | -52.73975 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| be5a40ba-3ce6-39d6-8a97-c92daa13667e | -19.91055 | -47.90712 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 39a385c7-2516-3786-9768-4b5565f7c7fa | -19.89808 | -47.91083 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 984d2875-b212-3045-afbf-ef62b2602f8a | -21.45426 | -43.91398 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56d4eebf-533c-3536-967a-b23bafe1db7f | -18.25548 | -52.73612 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a812842b-0fa8-3143-b883-1c1929a780cb | -18.25924 | -52.7554 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3ae8937-a7b8-34d6-8515-a5f2d5cce56a | -19.90337 | -47.90069 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57c94551-28c4-3c9d-950a-93ee29e13038 | -19.90269 | -47.906 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e8bb96f6-d329-396b-85b3-401b6a3a01df | -19.83275 | -47.9215 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e0b81c7-a538-31a1-b60c-1fe7bd358fd0 | -19.83206 | -47.92677 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60abb0a4-d00b-3c5a-a282-dfca44e0b538 | -20.37769 | -46.56332 | 2026-09-01 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f74907f-3347-3fd6-91d6-243c49164c37 | -19.10241 | -57.40364 | 2026-09-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 27d2cacb-6a5a-31d8-aa97-f777c02dd0fa | -19.89877 | -47.90543 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aa89c56c-05ce-3ef9-94ad-a94202af7324 | -21.45943 | -43.9147 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1e288dd2-4636-3e99-949d-d50697eaa79a | -28.85228 | -55.98945 | 2026-09-01 04:46:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| ad9b1872-06f2-3508-aa4e-0e19212653b0 | -10.3577 | -49.9957 | 2026-09-01 04:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| d992542c-db44-3bac-b000-dab1a7fce838 | -7.571 | -60.4643 | 2026-09-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7f55a282-076d-3ce3-86a8-c38d95393cf8 | -7.5709 | -60.4835 | 2026-09-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 4f3343a5-c0f5-3e07-a238-51ec7cb6ccef | -7.3487 | -60.5883 | 2026-09-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 062f2c6a-905c-35cd-82a8-71749cabdd27 | -7.5894 | -60.4827 | 2026-09-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0f1d924b-ef75-3269-8a6c-f133ee63ee1c | -8.279 | -54.9174 | 2026-09-01 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6afeb521-0fb1-3ce0-bd6f-bb7c73f0785f | -10.3574 | -50.0171 | 2026-09-01 04:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| ba2b4c06-97bb-3633-8d7c-f492a31e4f7c | -7.5895 | -60.4636 | 2026-09-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3f15f298-f53d-3d2f-98fc-e73634b60949 | -11.296 | -50.5794 | 2026-09-01 04:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 05ec6e52-32e1-3a36-b89d-0aad28889bdd | -7.3487 | -60.5883 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0baddca6-c72b-3ff8-be1c-6bbb43d1ba0c | -16.0547 | -54.3908 | 2026-09-01 05:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 99ac2fc7-019c-3777-9a55-68c6a47330d4 | -7.5895 | -60.4636 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 489faa2b-ddeb-3f28-b9b7-26ceb846aadb | -11.2963 | -50.5581 | 2026-09-01 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3b053f6e-7620-3f5e-8be5-aec3e9e4f131 | -7.5709 | -60.4835 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 94baa9d9-7335-3adf-8872-fec0267687cb | -10.3574 | -50.0171 | 2026-09-01 05:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 64883c6c-ee8f-3660-9439-6efe8d64787a | -11.315 | -50.5774 | 2026-09-01 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| de751747-f250-3a6d-9d87-9b25de86f35c | -10.3577 | -49.9957 | 2026-09-01 05:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f041710b-1f15-3b20-a6f2-b2510f480084 | -11.296 | -50.5794 | 2026-09-01 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| d19a865e-85b5-39e6-8f3f-e964930d76f0 | -7.571 | -60.4643 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fb856342-17d7-3f57-bbdf-49bd61f21394 | -7.5894 | -60.4827 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 78dcb50d-dea4-3026-b7ed-27735f2c06d4 | -7.3488 | -60.5691 | 2026-09-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 672abc18-38d0-35ec-9451-aa960cf4c8bf | -7.5895 | -60.4636 | 2026-09-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 3a8a2d95-029b-3dad-9874-15cd6eda671b | -7.3488 | -60.5691 | 2026-09-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 63c82eaa-7634-32d4-b382-be28b5fb794e | -11.2963 | -50.5581 | 2026-09-01 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 3fef5ed3-73c2-3e51-a27f-2f698caa3309 | -7.3487 | -60.5883 | 2026-09-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 38b4f52e-0baa-350a-8d0a-164e65f09fac | -18.1609 | -49.5832 | 2026-09-01 05:10:00 | GOES-19 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 48dd4413-b957-3625-a4dc-2c2f1490d461 | -11.296 | -50.5794 | 2026-09-01 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 74eb7af9-7220-3f9a-bfc2-21f98b3b71b0 | -11.3153 | -50.556 | 2026-09-01 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a2c0d62d-e69a-37d7-8525-739c982ec439 | -11.315 | -50.5774 | 2026-09-01 05:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| dff139bd-b535-3699-a7a5-21f725bbdda7 | -7.571 | -60.4643 | 2026-09-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 4fbcf917-ab3b-36b6-a2b0-4a6c61882e5e | -3.85584 | -44.04797 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7096c83-dd05-347e-be4e-099b8a6d6a44 | -3.16092 | -48.06895 | 2026-09-01 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086a5e0a-a20c-3600-8bc4-e91aedb1f675 | -1.44378 | -54.23537 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 933db1d0-5167-3f05-94c9-eafd1d03d74d | -2.73949 | -49.29424 | 2026-09-01 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f4982cb-68a7-3d6b-a15e-888cac387fa1 | -3.87365 | -44.05529 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69c34842-89b2-3a36-a249-e8ca773f7082 | -3.87013 | -44.07897 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7a09751-1a17-3d2f-8687-eda6e4d610c6 | -2.02965 | -48.78035 | 2026-09-01 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e41bca1f-7817-3104-b027-d6ac98664e19 | -1.9623 | -48.38041 | 2026-09-01 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ced9e4a-d4d9-3171-88b3-b1b67a09acd3 | -3.36963 | -49.16507 | 2026-09-01 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6756c4a5-0d00-3c02-809f-67b135a49422 | 0.97419 | -59.39479 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd6af3d-d379-3dec-b011-c18395d02396 | -1.41454 | -54.61261 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f17e4c9b-0a45-3411-9ba8-073583093ebe | -3.864 | -44.07794 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4efcf7d4-699f-341c-b231-4e39ec555e27 | -1.47259 | -54.22563 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2201f2f0-3a79-3424-a27b-d84fa361940c | -1.66446 | -55.14635 | 2026-09-01 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e28782bb-c094-3027-9da0-579c289cf58a | -1.25082 | -55.70118 | 2026-09-01 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85618f36-3c6e-33fc-a5da-d80a1fba777f | -2.73584 | -49.28967 | 2026-09-01 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4194315-f04e-3b28-b649-4de47ff042b7 | -1.46373 | -54.23846 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d19eb4c-2f19-3838-84ad-b1e4b9525cb9 | 0.97475 | -59.39841 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 095d547d-192f-3f82-a76a-3d430a4d1be6 | 2.51571 | -50.85507 | 2026-09-01 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57bb41c0-b270-38dc-97cf-5ccc4bc2cd3c | -3.87085 | -44.07417 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf6884f1-8150-303c-a12e-a8297b25e3ff | -1.01907 | -53.72721 | 2026-09-01 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f6afe66-0c42-36f3-aa59-13e0972f5e95 | 2.51865 | -50.85041 | 2026-09-01 05:14:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 648c12cb-3e7a-3fee-b9c1-fd10fa4dfee1 | 0.31468 | -60.44546 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20ca0c0d-4983-38e6-af7a-607365cbcc6a | -3.86889 | -44.04488 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 673b117a-8805-398e-bdf3-17751aa5bfea | -3.87433 | -44.05066 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b909511a-fb4f-382e-a251-61b0d95eeea4 | -3.18694 | -48.02392 | 2026-09-01 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 15a1f7d4-3307-3852-aad4-aa32a8d8d052 | -3.85856 | -44.07221 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cea9723-0399-32d0-b598-3ba6fd0df0e7 | -1.46868 | -54.20728 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 942ccb6d-b15e-32cf-97bf-815e07e35863 | 0.19319 | -60.50151 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553393c0-1037-3668-bed4-f2e4e2195087 | -1.62064 | -55.16779 | 2026-09-01 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74a1e1f1-4023-3e4a-81e7-056ead7a9f3e | -2.71913 | -47.0559 | 2026-09-01 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b17c44f4-6faf-33a2-9c67-688e3dc9d0a6 | -1.44539 | -54.20368 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 258a7b1a-86f2-3aa3-afa8-9896107bdb04 | 1.09454 | -50.9738 | 2026-09-01 05:14:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 400fbadd-121d-393e-810b-12ca58fd9d59 | -2.79954 | -49.5785 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae47db6e-3944-3358-b6a1-94e8defbaf93 | -1.46813 | -54.21075 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b32ed374-3ba9-3540-ac8b-623e0bda9881 | 0.01071 | -60.59673 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f14d25-f955-3e65-b9f6-9b954260e49c | -2.71837 | -47.05495 | 2026-09-01 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 321ad0d4-67e2-36a8-82c4-b4c4e50bab3b | -2.85617 | -49.54448 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbd2030d-926f-3f36-b74d-005a738f617c | -2.85661 | -49.54359 | 2026-09-01 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 299dcb6d-437e-3a7b-9a36-efee731308ae | -3.85713 | -44.08188 | 2026-09-01 05:14:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29663e41-177c-385e-a6a2-7296a9e464e2 | -1.03897 | -47.55499 | 2026-09-01 05:14:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7697d3f-62f5-386f-b180-c2bb5d81b7fc | -1.62396 | -55.16831 | 2026-09-01 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 759c2c11-e665-3900-aaae-fd93369cf43e | 0.97885 | -59.39776 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f04f904b-3c09-3c96-8c69-cf864f9dcabb | 0.91378 | -51.98864 | 2026-09-01 05:14:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c512286-7ca4-38d4-9808-ce3c5d04891c | -1.46816 | -54.23205 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961759ca-8cc6-34c7-b9e5-d3aecdc05f88 | 0.97717 | -59.38689 | 2026-09-01 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71f527ae-9a23-3c56-a6b6-be51408ffa4c | -1.44872 | -54.2042 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2331cdc-4056-333e-886b-e09f2db46f0c | 0.01138 | -60.60095 | 2026-09-01 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ddd4a5b-0dec-34f3-9bfc-14c594ebfd59 | -1.46706 | -54.23897 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945bf62e-3e21-3c18-8971-642ad583664c | -1.44487 | -54.22844 | 2026-09-01 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 828679e5-75d7-30b0-a896-74b5036ddd34 | -2.7208 | -48.8045 | 2026-09-01 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0452c466-d09a-330e-84d3-9271bf6b36a4 | -2.5011 | -48.13625 | 2026-09-01 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README52.md)
