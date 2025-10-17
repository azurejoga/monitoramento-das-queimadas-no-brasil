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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb70a3fd-fc7b-373f-b194-06650cf6d40d | -12.42703 | -51.30473 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 79ac013b-f9c4-393a-8b16-8cc6e688cc7d | -12.42298 | -51.304 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 00ddf869-4f04-3781-99dd-343fde075321 | -11.47592 | -45.08623 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 61c5b03a-6849-3caf-bf89-8c818f0f24b5 | -12.16874 | -45.06863 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0df401c-a66b-36a9-9087-978460058ed1 | -13.33972 | -47.27749 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f23013e6-54b1-3c85-904c-c75c8bf7a160 | -9.44595 | -56.65157 | 2025-10-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99b52bcd-8264-33b6-a592-8a57305576d3 | -14.15765 | -44.31534 | 2025-10-17 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf558e13-8e1c-3d8f-a663-fa2f07a73aab | -12.91341 | -41.82467 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c141e0e1-3f67-306b-8571-4dbd836be24b | -13.24829 | -47.10422 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7fa11a2-5975-3c40-8471-720dddcb9520 | -11.57679 | -48.56802 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 185ff5b5-3184-3857-8b58-eb4ccf4474bb | -17.43214 | -45.53114 | 2025-10-17 04:21:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fe98d59-1d01-3e15-9192-9aae0fba1bf2 | -11.57502 | -44.05496 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eb9bb4ed-2a15-3a60-a296-d79b26840951 | -11.9731 | -46.56186 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e14ac0d4-296e-3723-9c76-64f3d2ab2d7d | -15.19257 | -49.30921 | 2025-10-17 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beb90086-4636-3ec1-a925-6317707cf5e9 | -18.09378 | -42.44968 | 2025-10-17 04:21:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a0ad7c97-c9ce-3904-83d4-d97d4789946c | -14.93128 | -48.5339 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d45495b-613b-31b0-a9df-bba44f0bd956 | -13.4274 | -48.07887 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b5ecb05-21ae-3256-9ba9-97ccd5689409 | -11.61302 | -48.78679 | 2025-10-17 04:21:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08b45439-3aa9-3b0e-ab07-9904b9e80b04 | -13.39726 | -47.21685 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9d533f7-2a08-3520-940b-2d173bacfd95 | -11.58922 | -44.09895 | 2025-10-17 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5dfa4f9-e484-3823-80b1-d3ef1a67c5a5 | -14.70874 | -48.30606 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35b67ce1-8417-38a0-b543-aafa9d2d2dc2 | -14.91308 | -49.54218 | 2025-10-17 04:21:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89bb981f-892d-30e5-b7bf-e2a1e8fd3c4d | -11.86501 | -49.88766 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c3746b1-8c93-3dbe-9a5e-2ea15339338a | -13.42586 | -47.94007 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c14f73c6-2504-3a71-b0e2-c890eb7c286d | -12.16819 | -45.07222 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 875e8cfd-9f43-34d9-ac03-8caa3cf5ba27 | -14.34468 | -51.44438 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3d314856-2800-3f14-b2b0-d188f630b309 | -14.32011 | -51.47511 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ff52acff-e926-3e88-ae57-6be757cc678d | -12.43107 | -51.30546 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e889da2-9159-34b6-accf-0ec6d247f9d4 | -15.02998 | -48.76686 | 2025-10-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2c1192e-7ce3-3e75-a888-7fb4b27156b3 | -11.50961 | -48.23178 | 2025-10-17 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6dd3804-cadb-3ab6-b887-c844a4244528 | -16.02343 | -43.49459 | 2025-10-17 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88d6a543-e364-3da5-b70c-744d9152b2e2 | -12.45213 | -51.32806 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 871bbeee-edf0-38a8-9a91-d5a4746e5b16 | -13.28865 | -49.58051 | 2025-10-17 04:21:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eafaa494-01eb-3e04-a915-421d88e0f0f9 | -12.44652 | -54.50731 | 2025-10-17 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e43637f-4093-36f0-9be5-5eeda47139b2 | -11.19279 | -51.74966 | 2025-10-17 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d59be07b-9e84-3c31-be45-c906edab5394 | -13.43851 | -47.96887 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f51cf851-e3cc-38d9-805b-70bd82aa688a | -15.78851 | -43.6475 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a865c5d-c11e-3198-ab82-ce069ee9a220 | -15.73892 | -44.61378 | 2025-10-17 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cc39850-6ee5-388d-978e-c2539ccf08ab | -11.51719 | -48.22908 | 2025-10-17 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 304f61cc-8663-3ff5-ac2a-737535119001 | -13.20177 | -48.3173 | 2025-10-17 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f2fbcbd-9b54-3653-86e2-de299f685084 | -13.82736 | -42.34545 | 2025-10-17 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5f48cca-ab11-33ae-a669-13f898eda775 | -16.8086 | -53.93166 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9714e0b-ae32-311e-9057-f5ea00d7de69 | -11.58099 | -48.5646 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb9c3f34-c056-3da1-bc70-2d2d3469139b | -14.34278 | -51.45488 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f448ba76-41cc-32db-82c3-fc7a7db5a133 | -13.3906 | -47.21587 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38efc7fc-c34a-36ee-a41f-1036ebf2d402 | -18.09051 | -42.44393 | 2025-10-17 04:21:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 862f1980-6153-371f-b0cc-dd91e904153f | -19.21553 | -44.11415 | 2025-10-17 04:21:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c966ee87-43bc-31ed-a50c-16ec9bd16e11 | -14.67114 | -47.40476 | 2025-10-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69d25475-6511-3357-9c51-c746bc68faf5 | -12.65634 | -47.89298 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1223ea2-1cf1-3f9f-9fd7-35490072c5e6 | -12.77859 | -44.88169 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 10a8ea00-8884-30fb-8cae-2a17c4895704 | -14.3309 | -51.4527 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c5328c1-d711-31da-bb85-d674ad2de0a4 | -14.35688 | -51.46745 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 61d2fd95-26c6-3c95-b763-1a9d80b25d02 | -14.33037 | -51.43982 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7c71e8d9-8cb1-3e30-8a28-9e6891d33543 | -12.77304 | -44.89561 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f171d8b-4892-3e9e-b36c-6301b9d42ef4 | -13.24322 | -47.11453 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf48958a-e181-3ad0-af39-31633d0f2a30 | -16.35616 | -43.41429 | 2025-10-17 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91acbbe3-f6c4-3b32-ba4f-b9211f6b210c | -12.44386 | -51.30399 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52ff0ff3-a0e0-3b2a-b1d6-ddf54599a21e | -13.48536 | -40.33108 | 2025-10-17 04:21:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ca1bdb8-d88e-3741-9d89-6bb0a9311408 | -11.54822 | -49.92194 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 654b38ee-ba8a-3c62-9567-d036d3d2f044 | -12.14138 | -43.26444 | 2025-10-17 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43665a51-f195-3850-833d-359442077380 | -13.57813 | -48.4866 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08728598-6c60-398f-a583-39160a6808e2 | -12.91431 | -41.82707 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e1fed344-431d-3d9f-9f45-1e73ea37019f | -12.76915 | -44.8987 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b2c89fb-7bd6-36ec-ac2e-2cdf1b404d97 | -13.44215 | -47.94666 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10888e37-d22d-37eb-a726-9637b78ae7ba | -14.41911 | -47.88725 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef48fd5e-78fa-3367-9424-34667ffcf70b | -14.33281 | -51.4422 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 5a184925-0af2-3b4a-bc2d-670b2965c657 | -13.76058 | -43.11869 | 2025-10-17 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2cd3d5af-a818-391f-87e9-3bcc0e74154a | -12.15083 | -49.6799 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8081e4cb-ecc0-3b8e-911b-9cfad647bc32 | -12.95479 | -48.99715 | 2025-10-17 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18e7ab7a-5990-3897-8fb7-2ecc67f23532 | -12.06501 | -47.98034 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7585a75e-46b8-352a-8e74-ff156f5fd815 | -13.75582 | -48.21896 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd33d949-7277-390d-9b0f-b27c2edbb480 | -12.92045 | -41.83028 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da997e83-30f9-38f3-b924-6650750bab4b | -13.42657 | -48.57145 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5350c566-fb5b-3866-a5bc-f5fe1e6c98e4 | -18.25746 | -47.82034 | 2025-10-17 04:21:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cb67f85-ddcb-3f01-b7fc-7f5a0d411b1e | -11.06655 | -47.59538 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bedfdcb2-a340-3839-b332-78b07d308cfb | -14.33486 | -51.45343 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b864fc66-494f-3268-aaae-35cd1b0923df | -13.42984 | -47.93698 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36f2d0f7-4b00-3305-ac9d-8180304ac430 | -11.52451 | -49.1414 | 2025-10-17 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d37de51d-954c-3de0-810e-9a5ddc207b01 | -12.44127 | -51.31858 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb42ae36-087c-3163-a65a-1e72f938b0f9 | -14.33643 | -51.4673 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 86393fa6-f5c2-333d-9c82-2e0cd6ca786e | -18.05482 | -42.47099 | 2025-10-17 04:21:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c0b75b2-c8a5-34c1-9e8c-167a199293cb | -12.83524 | -43.80822 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67af394f-2a26-3149-a72b-a7d2ad2b6c89 | -13.45403 | -44.28796 | 2025-10-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad426db3-ccc3-3232-8738-23584d664e0a | -14.33662 | -51.42124 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47500b0d-4543-3ccf-bed6-13633b2b056e | -14.23381 | -54.90637 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7f1a0b5-b922-3748-918c-49e43fb1d286 | -12.78193 | -44.88222 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 54f2d6af-48cb-3d3f-996f-e86f93dfdef9 | -11.19136 | -51.75776 | 2025-10-17 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de34bf17-41b5-3927-ad0e-cf0b29d48db6 | -13.07804 | -49.34092 | 2025-10-17 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d35c7e-7cde-342f-b73f-334002a899af | -14.32061 | -51.44887 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94f26cdd-8b73-309e-ad7f-74ef7c5a7129 | -13.39393 | -47.21634 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d0d2554-0f0a-3b81-a893-2761e81f5166 | -15.03906 | -52.99109 | 2025-10-17 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09a0be58-39b9-306c-ab74-9dd0f278ad91 | -12.62329 | -43.43448 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 768bb191-1e59-3418-a34f-9b9273ff6922 | -11.58804 | -44.06079 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f7e858a2-1d2e-32dc-9074-7436fe697f2a | -13.9382 | -48.69367 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde45043-0704-34b7-83f0-5972a9a9ad93 | -14.33055 | -51.47712 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 761bdcbd-73f4-3157-ac95-ac0143502dd5 | -12.77025 | -44.89148 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5135c020-4439-38ae-be75-72e8e0beb47b | -12.43382 | -51.31348 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3fdd7bf5-238f-31c6-b34f-28788f34a9d6 | -11.19119 | -49.80098 | 2025-10-17 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 080297ae-622b-3c3f-9577-b84ba78d43cc | -12.91404 | -41.84868 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 228b2af1-ecbc-3503-9eda-e8b9c448d561 | -11.97254 | -46.56539 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README72.md)
