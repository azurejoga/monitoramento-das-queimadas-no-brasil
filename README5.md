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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c705587-c77a-3423-a267-e99060be8feb | -20.40823 | -54.64043 | 2026-07-20 04:51:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 012b152d-079f-34ef-bda5-44edb806a6f1 | -22.69596 | -48.69062 | 2026-07-20 04:51:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18f7681d-5e0d-3913-b9e3-cd3f53759d59 | -21.13498 | -47.46206 | 2026-07-20 04:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 81de8915-7a0a-3d2e-afef-cc90c177b7aa | -21.40967 | -44.25722 | 2026-07-20 04:51:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ebda3f91-533c-3cda-8b39-0af08cfa394a | -21.99077 | -56.01625 | 2026-07-20 04:51:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38890a14-ca41-39db-8ba2-b37365756ffd | -21.13551 | -47.45747 | 2026-07-20 04:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 873fbfe0-7471-30b6-b76d-b6a3a5af6de2 | -21.13101 | -47.45695 | 2026-07-20 04:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83e9ef55-e2bc-357e-9c64-1681c464f692 | -22.65979 | -43.65402 | 2026-07-20 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e453a2ba-f2e3-3974-bbfb-9645ca0ce94c | -21.60891 | -46.61555 | 2026-07-20 04:51:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| aacfbdae-a31b-30c7-ac59-f772e303f7bb | -23.74482 | -54.56537 | 2026-07-20 04:51:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e648fd09-5a2e-31d8-9f2d-df56b357d19b | -20.00592 | -48.90885 | 2026-07-20 04:51:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd1de279-0c67-3b91-9e91-f5fa1f7cd38c | -21.10411 | -45.79784 | 2026-07-20 04:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ffa7835d-f9b7-371e-8983-6ff575e4ec21 | -20.28424 | -46.4234 | 2026-07-20 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4d00ae2-402c-33a9-8dcc-9b1a44c21a1b | -21.39654 | -45.51126 | 2026-07-20 04:51:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c3ebd093-8381-364e-a801-7dc61014cd0a | -21.13947 | -47.46261 | 2026-07-20 04:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af828c3f-1c55-367a-9c79-20b5b589d0b4 | -19.77415 | -44.29989 | 2026-07-20 04:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d44c4b-2c02-3b9c-93b9-f7eb11190b05 | -21.86874 | -49.24825 | 2026-07-20 04:51:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| db2a04c2-e8e7-3c84-a586-41918f272ee4 | -21.40928 | -44.25463 | 2026-07-20 04:51:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8fc84a89-df98-3017-86b8-1b2d143bf75f | -21.87325 | -49.24505 | 2026-07-20 04:51:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c21b0b20-fd55-3615-ae4b-994d091b9826 | -19.93151 | -44.07019 | 2026-07-20 04:51:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d924590-86f8-3b5d-a8ce-fd9836ef7142 | -21.40893 | -44.25847 | 2026-07-20 04:51:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 92a15453-36cd-30cc-a8d7-090f6c13b79a | -23.30285 | -46.17697 | 2026-07-20 04:51:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d78cbed3-80e2-3b24-a9e3-846685e7eece | -20.28964 | -46.41818 | 2026-07-20 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 413d038d-61f0-3a75-9a70-5cd5239872f6 | -23.18078 | -50.49029 | 2026-07-20 04:51:00 | NOAA-21 | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04b411f4-6796-357e-b206-4cdf91df63b0 | -23.17998 | -50.48708 | 2026-07-20 04:51:00 | NOAA-21 | SANTA MARIANA | PARANÁ | Brasil | 4123907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ff9d550d-4177-33a5-9b83-37b55ee81730 | -22.69645 | -48.68642 | 2026-07-20 04:51:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 473a6c0f-17df-3762-96ec-5420bcd80b6e | -21.61366 | -46.61637 | 2026-07-20 04:51:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d213e6bd-fe90-31df-a158-960b86f1e3e1 | -21.86921 | -49.24442 | 2026-07-20 04:51:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6968819-ab0f-3bb7-9b4e-885765520ff5 | -3.00999 | -49.82789 | 2026-07-20 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0c3d070-90e4-3f2e-8b71-a0ae525a1f32 | -2.79313 | -49.5233 | 2026-07-20 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 406e092c-162a-3373-8698-fa6f92ce8711 | -3.41736 | -49.12391 | 2026-07-20 05:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d94211f-30e2-36f8-b06f-e001f6499fbe | -2.79166 | -49.52162 | 2026-07-20 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d9d2c6c-c5a2-3994-9e23-6953cea7230f | -2.79784 | -49.52401 | 2026-07-20 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 536ee391-822a-3def-af64-db3b7afc6432 | -2.78204 | -49.45905 | 2026-07-20 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f42ff9e8-275c-3fd6-ad4e-76f56d6c85a8 | -2.79637 | -49.52232 | 2026-07-20 05:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f731fe09-c603-3c03-9915-6c6dd2706225 | -2.78599 | -49.46478 | 2026-07-20 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d361922d-4009-33e7-839c-04c8ed13807c | -2.82805 | -48.86517 | 2026-07-20 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 920a060c-9736-3a3b-8c7e-a3fee65c9ff1 | -2.83298 | -48.86591 | 2026-07-20 05:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66689579-71c0-3276-bbf2-d645aa6adf4f | -16.15799 | -57.62031 | 2026-07-20 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 60eee5cf-bc04-31ed-ac7f-d480444dfbbb | -15.46453 | -54.35297 | 2026-07-20 05:23:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdad8519-dfd7-38a7-9217-d89b73e91512 | -10.44711 | -50.21278 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a13ad2-9d7e-3bcb-804d-087246c2318d | -11.39282 | -47.5058 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63b77fd1-35fc-3efc-91e4-0b2bf29335e1 | -7.90908 | -48.26399 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23ec7fcf-13ea-37e4-a5f4-685b8c265085 | -8.93158 | -47.60342 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c79d645-883d-364e-ba87-33e365ea4587 | -9.16494 | -61.40581 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae5598dc-720d-38fa-92c1-3f1f3a759e37 | -16.80605 | -54.591 | 2026-07-20 05:23:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e2234fa-b107-3095-bb03-fb20578927a7 | -9.09906 | -59.40112 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1126aae7-a382-3269-ab78-9f25ff50b503 | -9.0957 | -59.40057 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 005168c6-1c8c-3cb2-ad57-d43a1c654b09 | -16.64674 | -49.53278 | 2026-07-20 05:23:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c046bea6-f037-3a3c-b03e-4b006793f52c | -9.09848 | -59.4047 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95806b54-aa3d-3780-9858-18318e63d03e | -11.38662 | -47.50588 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47e4bff7-902a-3b58-97fa-231d297e1c74 | -6.72029 | -48.11477 | 2026-07-20 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61221302-bccd-3e3c-97d9-e4889ae6a4b0 | -9.28709 | -50.33026 | 2026-07-20 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fcb333d-e708-3d4b-8a87-bbf881d18236 | -8.93369 | -47.60201 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b86d776-a452-30eb-a728-d02e73fefb2e | -10.9054 | -56.36736 | 2026-07-20 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45f4f826-f819-3323-8693-87a2ab703be0 | -7.90956 | -48.26037 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce360a9-06a9-35a7-936a-2e3e66e111e7 | -7.90996 | -48.26154 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91bcacd4-dc6a-304e-88c7-414c588e3acf | -9.87232 | -53.32474 | 2026-07-20 05:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 916bf5f6-db1d-3540-9bf7-8ce3ec80ca54 | -11.38106 | -47.50048 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d6f635-2801-3da1-b10e-b57cacfc4440 | -11.74437 | -57.81 | 2026-07-20 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b4f7d9-4450-3a83-a93e-7a9c53330187 | -11.74716 | -57.81413 | 2026-07-20 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3d10130-6638-3819-af77-2c3602895cd8 | -10.55458 | -56.33089 | 2026-07-20 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a00f2b04-4ca3-37c0-9185-11b22456230b | -9.18339 | -58.06835 | 2026-07-20 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 772c2a14-3710-3fd7-aa05-0a8cb652b854 | -6.72079 | -48.11121 | 2026-07-20 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8e45f9a-ea20-3c9d-a16e-3af25cc6ba2d | -11.17564 | -54.11628 | 2026-07-20 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebbc7730-03db-3a45-804d-84547b5e0c0f | -11.74382 | -57.81358 | 2026-07-20 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 181dfc1f-8bd7-35dd-bc5f-e591b35803e0 | -16.60381 | -54.4971 | 2026-07-20 05:23:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac4e4b1b-50b2-3b11-b9a7-477fdb1e27e3 | -10.45423 | -48.32374 | 2026-07-20 05:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a73c22a-0219-36b7-befc-f53969448573 | -10.68879 | -49.62417 | 2026-07-20 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38f52d1a-a561-3e58-8628-08b80389a0c3 | -10.44131 | -50.21796 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11a8bc7-9def-3d43-8ea6-a5d37fb63860 | -10.80068 | -50.22666 | 2026-07-20 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f998500-50ca-3d98-a103-6638172b56a2 | -7.90945 | -48.26516 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f77c01e-aef6-3319-8cc0-9102e84309d2 | -6.13201 | -55.80823 | 2026-07-20 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dfdc4e6-d8d5-35ac-b8d7-d03ca3fc5d89 | -9.10184 | -59.40526 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901e2f65-22d3-39b9-94a9-f1346600dc1c | -10.80028 | -50.22963 | 2026-07-20 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93062918-1ef2-37e1-abf0-32823b586461 | -10.68353 | -49.62343 | 2026-07-20 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9deac1ad-7719-34b9-8b54-f1cb079637f9 | -11.74102 | -57.80946 | 2026-07-20 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd39185d-1ab7-3a6d-8bb7-36d96859330a | -10.90599 | -56.36347 | 2026-07-20 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80eec149-296d-3544-bd0d-7aa8e398396c | -9.87232 | -53.32511 | 2026-07-20 05:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c098ada5-9393-3925-9e78-d8876535d543 | -11.39161 | -47.50922 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78954fe3-458b-3dba-98d6-53354650d651 | -10.55342 | -56.33859 | 2026-07-20 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573f8732-6a48-369f-a835-e333d5bc4aee | -9.26008 | -59.82931 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1b7ffe-619a-397d-8260-a6c92c4727ff | -11.38601 | -47.50449 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01e0392d-b01c-3de6-b4e4-e572113a10a4 | -7.9146 | -48.26492 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc7d63c4-0f1c-354a-bc08-3d4e40ab9a85 | -8.93745 | -47.60424 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad0ce4d5-48e2-3640-a4eb-4e5af4fb8c70 | -10.46806 | -49.10032 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81d86ebc-790b-3b91-a92b-472be7f608eb | -10.46308 | -49.09595 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a8c2f1a-fbf4-3183-b7c5-28d61e17717f | -11.39226 | -47.51054 | 2026-07-20 05:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3816b75-616e-35a0-876d-c55e808200be | -16.64239 | -49.5345 | 2026-07-20 05:23:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54582710-071a-3171-b7fd-db0568deca3e | -10.55112 | -56.33035 | 2026-07-20 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83075590-e002-3f2e-b30d-0cf14959add4 | -10.43627 | -50.21728 | 2026-07-20 05:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea102b95-48af-3d77-97f5-4f81392fa96e | -10.45245 | -48.32342 | 2026-07-20 05:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29a13e5-8f7e-368a-882b-7626e24fec30 | -9.10243 | -59.40167 | 2026-07-20 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dde842c-1cf7-3c32-9b5a-49bff4a292f1 | -8.93798 | -47.60006 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 604241c9-c60c-30f4-a70c-7f38f4996a40 | -8.93955 | -47.60281 | 2026-07-20 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fa22d82-7ec3-3b1f-808f-a4e33a9903f8 | -7.76941 | -63.85054 | 2026-07-20 05:23:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b5b4c60-23d0-3c87-83c0-80b1ddf9b314 | -7.91508 | -48.2613 | 2026-07-20 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c922c3-6391-3c52-a13e-5aa4a0ab7459 | -6.59457 | -51.70689 | 2026-07-20 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e7a7e2d-a346-3d36-a0fe-887772d5bc5a | -10.90888 | -56.36789 | 2026-07-20 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ae41e38-41f2-3915-a540-716049121273 | -10.55688 | -56.33914 | 2026-07-20 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
