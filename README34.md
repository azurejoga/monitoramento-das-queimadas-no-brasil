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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b461c03-5846-3c11-bac2-2f2b9e54332d | -7.9241 | -44.13235 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f5e0f26d-ad49-3cb2-80da-0fb6ac80ffcf | -12.74187 | -50.67806 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a410e35d-86cd-3940-93a0-8723eeaa98bb | -7.90306 | -44.99757 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6397795f-473f-304e-8f30-a702aa509d6c | -12.83044 | -50.64461 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 70784a49-f322-3e18-8af0-b1aaccddcd78 | -12.80679 | -50.65338 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27e376e2-dcfc-316c-bbfc-b17e2919b326 | -7.15087 | -42.51752 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 016be191-9e09-36b9-8d32-a2edca59a2df | -12.8634 | -50.64614 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1bfb5628-df86-3d84-bdd1-38e0ec36db4d | -11.52234 | -43.52368 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00fac999-0b60-39be-a8a1-596170ddd2f6 | -7.03368 | -44.86732 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ddcb110-2bb8-3bc8-ac80-35945253508a | -7.2952 | -41.96365 | 2025-10-14 04:25:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5862fb03-d462-3b6a-807b-874e6204125a | -7.53447 | -42.69868 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 684ecb9c-7248-3b01-8230-f116f7f0b54a | -6.85206 | -47.63605 | 2025-10-14 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2abb216-659e-3a10-b494-473d5a0008bb | -10.23758 | -39.95124 | 2025-10-14 04:25:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8d92613-c45d-3837-9623-a120a98aff4a | -8.43557 | -46.20027 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8007f4eb-5f1a-33f8-8825-85a3679e02eb | -7.92469 | -44.12852 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fd2ed23-9397-3770-9292-e8c5c6f5c736 | -7.56233 | -42.68934 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0f9b9d6a-bbaf-39f7-8fbd-98bc162bdabb | -11.52017 | -43.52548 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac3a839d-f0c4-3b62-9619-544c69f9a1c3 | -12.85911 | -50.64969 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 480d31ec-d5d1-319c-9334-39ab09f932f9 | -12.8462 | -50.63877 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9ad295ca-1064-36cb-b6bb-786a568cb0cd | -12.85052 | -50.6568 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81716451-429a-34b7-bdb1-b1ff66d8b1fe | -7.92704 | -44.11316 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38f47850-226d-36e0-a32f-dc9cd433bc6e | -12.73108 | -50.65447 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caadcdf8-53fb-3492-930f-895005c929b7 | -7.92528 | -44.12468 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 42dbaf72-cec4-3263-ae52-d2ff5a3000b0 | -7.45435 | -45.95932 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b59f545-f2c1-320b-92d0-af905f59bc7c | -7.2022 | -45.48793 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d450317e-7db4-3289-83db-f6d693c65864 | -8.43222 | -46.17838 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3730e1c-deb9-39ee-8e06-3fef0c58bec3 | -12.81324 | -50.63725 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 506eccbc-04c6-36bd-8be3-70fe2586e542 | -12.84978 | -50.6394 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f45ec9d7-e20a-3ad2-bd83-0fdccb054cd0 | -11.52053 | -43.50965 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b2e4413-69e8-363f-af5b-06a6ac2824c5 | -12.63686 | -43.44608 | 2025-10-14 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a9a9c6c-3bdc-3bcc-bae7-313c3953dcaa | -7.94261 | -44.12734 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2f0513c9-fe30-3f43-8c33-7b179c5560f2 | -11.74818 | -43.2894 | 2025-10-14 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 6d2d40b0-9dee-3743-8c4f-74217939b0d8 | -7.30703 | -46.67788 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6fde5e05-d935-3200-99af-405e98008228 | -12.68349 | -38.55348 | 2025-10-14 04:25:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b343a4ff-f31f-3323-9590-3fdd291397ec | -12.81396 | -50.65464 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bc908c4-45aa-3233-a985-47a999f7f7bf | -6.34619 | -52.07339 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 382df2d8-2666-3281-975c-53d42cb77d77 | -8.43059 | -46.18881 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8747b273-e4a2-3fc2-8607-83a0a0b7e0e5 | -12.79848 | -50.64912 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5e0a9458-13d4-3df9-86f2-af412ae69bca | -7.1559 | -42.50923 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9fea2771-3ee8-31f4-a751-9f6c1929cce4 | -7.93626 | -44.12244 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55a428a8-7603-38d6-87dc-1bca87c6ca80 | -12.82686 | -50.64397 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d75aaa75-ad25-3d57-86d5-115b95f46f79 | -12.83763 | -50.66748 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7caad7d1-3831-331a-a054-545553561218 | -7.94202 | -44.13118 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bcd7fd8b-a32d-38bd-90b2-79d49694488d | -12.79172 | -50.65504 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3f3ed647-23d0-38c0-b7d8-f03bbc18ee84 | -7.53141 | -42.69375 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a9893ec4-614c-342b-aa60-34326469a34b | -9.08738 | -47.95824 | 2025-10-14 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 108c99b6-2e3e-390d-a666-145c703b9b7c | -8.44048 | -46.16898 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12cd815d-6e02-35ea-a3ee-e86debf7a5e3 | -13.03907 | -43.22392 | 2025-10-14 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22fa00b8-e4e6-35c9-949f-7bc848c890b4 | -12.82399 | -50.63915 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ecaac1f-3617-3973-91f1-70f309a72ca6 | -10.20951 | -48.07662 | 2025-10-14 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b20ab2f2-75d6-3a6f-a1dc-b8e5cadd60f2 | -7.75783 | -44.73396 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7a55a4af-d87f-3c73-a8c8-81c8ff8a98b2 | -7.92933 | -44.12138 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de011a13-ba0b-3882-9281-61f6c36f53e6 | -12.24213 | -49.36129 | 2025-10-14 04:25:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eab4b40-f9fa-3ea0-b982-32fe35c439da | -7.23246 | -45.31649 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc625b1-f0b3-3380-9180-f9a1a7296ecb | -13.83111 | -42.42311 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 982ff379-f62b-3af0-8e28-6562bd434122 | -7.93973 | -44.12297 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fb13e9e-a8c3-387b-8d1f-7c86298433c0 | -6.96343 | -46.85132 | 2025-10-14 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da97571-677a-372e-9159-d5588a64925d | -6.86517 | -48.27722 | 2025-10-14 04:25:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 620b7a03-5b36-3f3f-b2e3-c9bc00e98c97 | -8.43779 | -46.20774 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65c659ed-4441-3722-9433-d49b96f20899 | -12.79675 | -50.64729 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e898173d-cc58-3446-85df-55fb8a7d1ea6 | -7.91377 | -47.20098 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8be3683f-7fac-376b-a370-b6c01be38fb4 | -8.4367 | -46.2147 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78a383ef-00eb-3171-95c5-d35edf954e79 | -12.62616 | -44.12482 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3379f5-a2b7-3673-ac0a-7069e9b13201 | -7.91484 | -44.98835 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35222377-70db-3535-a61c-85ad151fede7 | -11.52116 | -43.50515 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a2cbe51-202f-3b2a-9da8-8de1a654c07b | -7.94608 | -44.12787 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7d00c968-a0d4-3b34-8913-c160d593159f | -7.38417 | -44.06808 | 2025-10-14 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90f9acbe-7daf-34ae-bc52-ebecc4f6ad46 | -8.93078 | -39.90565 | 2025-10-14 04:25:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 79e21036-a70a-35ca-bb24-d2ccfdb113b5 | -7.55732 | -42.69764 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4496e593-58a3-3113-84e5-ea086ba1917d | -7.91597 | -45.00331 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8507ec9-6bd6-33fe-b964-51dede13ed90 | -12.85049 | -50.63522 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| be9f8a0a-1df7-35cd-af4d-e499882ca44d | -9.9915 | -36.38057 | 2025-10-14 04:25:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a109a35-5d0e-3650-81eb-1cdbc2696a73 | -12.80106 | -50.64373 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8113121d-16ca-39d7-8a30-310a542a3e55 | -12.83331 | -50.64944 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 073120dc-2664-37e4-a647-26833f46dff9 | -7.53496 | -42.70516 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c6719c73-0763-3189-9d48-b444f224509d | -12.79961 | -50.65211 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e55bffbd-56e9-3f32-8d1b-bbc5c840395e | -12.04738 | -54.24809 | 2025-10-14 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e71395c-c338-3d1b-94f3-c9d4e7b7e229 | -7.64044 | -42.57335 | 2025-10-14 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 65a92f2b-65ee-39f2-968c-8d37d8ecb281 | -12.82328 | -50.64334 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e78e3bb-df76-3d49-9663-48765bd4c984 | -12.79603 | -50.65148 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36ec7ce6-e5ff-3267-83cc-1c3bdbc53d15 | -8.45368 | -46.14965 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d5b01b-aa7a-3f8d-87c6-69e3a341239f | -7.62737 | -47.83735 | 2025-10-14 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f262f406-f050-3cea-b5d2-95d02b693360 | -7.16013 | -46.53323 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f71eb2f-2a81-3a48-893d-bc6e45bb5762 | -7.74864 | -45.72791 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7baefceb-303a-38c8-b892-219c93edba71 | -7.56363 | -42.68049 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6fc0b4c4-bce6-3e8b-ba0d-ded2d025d222 | -11.41941 | -44.05518 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac3e5710-8750-3249-bb6d-ea0763a8fef2 | -7.75444 | -44.73344 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7c1e5c42-9860-3418-b249-5c4724fbe7bf | -7.94032 | -44.11913 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcd5194a-3067-3c22-81c6-6ed90fa41dea | -7.7536 | -45.71795 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44f897ae-6a95-3bb9-8f0e-ec9cd21633a1 | -12.86269 | -50.65033 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5b392c0f-2cd5-324d-832a-5ce93d372af8 | -12.79778 | -50.65332 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8551bb77-1164-3048-a69c-c852126cf7e3 | -12.82184 | -50.65172 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d8be95f-0a92-3305-ad0a-f977cc86b5f3 | -7.08561 | -43.70446 | 2025-10-14 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d2cbab13-6d14-390d-8caf-71aba7d52993 | -7.49185 | -45.1282 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af9cfd9d-f90f-3633-93dd-121f11ae7da0 | -8.44056 | -46.21174 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6fe9ce77-7347-396d-bc41-8a6ed127667f | -7.01672 | -46.36531 | 2025-10-14 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20b60993-4615-39b8-ac5a-de58b1a8aef2 | -7.9328 | -44.12191 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c9e8880-82a4-3bfd-b420-8464daa65fba | -12.84478 | -50.64715 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98930908-2d14-3775-9a8a-bc09612b2c30 | -8.44706 | -46.14861 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a60ebb0-7481-31c4-bf88-1e7073751395 | -7.20275 | -45.48443 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README35.md)
