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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b605d049-b636-3f80-bfa7-ac0debafa1af | -8.01891 | -44.14286 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ba92999-a623-3f2f-bc41-8a7a42226778 | -11.23221 | -44.96157 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b22e74a-35a7-3382-b8f9-4ad45fbd34c5 | -9.8232 | -47.81524 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bee88664-32fb-395a-a6d6-84ad9d267513 | -8.04289 | -44.13952 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85b410ac-fdbf-3e4c-84e4-ab2d00040122 | -7.63671 | -46.55667 | 2025-09-04 03:36:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f72a37c-f488-3c0e-aa3d-b328850e06c6 | -9.38452 | -40.30425 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2d625c32-f968-30bd-b802-75aa84c0929a | -11.96507 | -45.78384 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a9ebd38-fd55-3152-a3c5-1946f475b0cd | -7.54784 | -45.72548 | 2025-09-04 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33c998b1-8323-37ab-b508-124fdc7a7aee | -6.87091 | -45.20024 | 2025-09-04 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c33ba4e-2bcd-33a5-9597-6a33f6f06f71 | -8.60609 | -40.31341 | 2025-09-04 03:36:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a1a1918-10fb-3b04-8094-443ed7c12f54 | -6.78415 | -44.0912 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ea485acd-83f9-3a9a-aa3f-63dcb0fd32eb | -6.83771 | -46.39977 | 2025-09-04 03:36:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f50d8b01-9053-39e4-8c40-825727951fc5 | -8.0525 | -44.13394 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 652122ed-2571-356b-9522-b1bfc10446e0 | -8.03118 | -45.3791 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| adcccfd2-87e4-34a3-a4f9-1c4654653d0f | -10.97972 | -46.84626 | 2025-09-04 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7c0d4ca0-e900-3a13-83c6-7c141206969b | -6.78566 | -44.08709 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b1134226-bde6-3566-9069-d639147e6966 | -9.63972 | -46.12256 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e9e70cd-5bc0-3d62-9e5a-5413f431ca90 | -11.05628 | -45.40661 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee56172e-91ba-369d-bbfa-e2956e00f8a5 | -8.02652 | -44.06945 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5a81f86-aa31-3eb6-9b5b-290390f5291f | -8.03643 | -45.38458 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0c0906b9-b004-39e9-a70e-9225507f14e7 | -11.7834 | -47.33096 | 2025-09-04 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a80d88b6-2e7e-3b40-9959-99774b266a1f | -6.5472 | -43.91441 | 2025-09-04 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca11bf45-046b-37da-86c2-f9145a7a5ace | -9.39453 | -40.31364 | 2025-09-04 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b57f4370-a765-3682-bf74-bf5dc2a22f13 | -8.01606 | -44.12654 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d4c605f-9cd1-37d2-b6c2-aaff97ab9f3f | -6.02364 | -46.68076 | 2025-09-04 03:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a6c9b01-85a9-34df-8a7f-b8386bbf45c6 | -8.02499 | -44.04605 | 2025-09-04 03:36:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 011e2f5b-de5d-3720-a317-395a1ee0df2f | -11.38724 | -43.56729 | 2025-09-04 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a086468-7ca5-39cb-8cb0-6133441f572f | -11.05184 | -45.40151 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cff1f82d-8bff-3186-ba6c-0b75c04dcce3 | -6.87266 | -45.19062 | 2025-09-04 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e253d17f-8684-3a81-b214-a51248ed1dae | -6.88476 | -45.56875 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96560560-ea02-335b-85ff-2584204a9b66 | -17.16229 | -46.25255 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15ceff9c-343c-30cb-bf27-d273cc08000f | -17.61222 | -46.64355 | 2025-09-04 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e59038e7-69b1-3f7b-9d76-50cb5bfd3d6f | -13.58127 | -48.13012 | 2025-09-04 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83a29a92-645f-3da8-b841-24e527ff70d2 | -13.0051 | -42.46923 | 2025-09-04 03:38:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fb283f59-ab3d-3a2b-b77e-b0c22ceb0878 | -14.59754 | -48.00874 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acf80fa9-e827-3488-b6d4-7ba8588eaa3c | -12.49797 | -48.0653 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e86c197-eb3d-311c-8de1-0e2e5789c738 | -16.30734 | -45.69391 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d9879cf-380e-3fa6-ad74-e185356d721c | -16.30557 | -45.69398 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d04cf74-4062-3df3-9f4b-86db4e179a2f | -15.03563 | -48.1035 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93a6bd62-730f-3731-907d-4d4da8aad806 | -15.04105 | -50.07015 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a3d9911-e49e-35f2-a0af-048425ba5c05 | -13.45926 | -46.83391 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 079cc146-ff26-392b-b718-ef332515a068 | -14.53825 | -48.06682 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cbf9ecee-0efc-3f61-a5b6-d900ee66807c | -12.89279 | -48.03826 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8417695c-6d09-3144-a8f4-c480d35676a4 | -19.23852 | -48.68242 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caddd9b7-a9b3-3088-b62e-35877002219d | -13.3024 | -46.8238 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e866c1ed-be8f-37a7-a69d-f9b87d93c8ea | -12.4703 | -48.0812 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2fed762e-9d2a-3b8c-8945-9347ee0b9daf | -15.53207 | -48.34037 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e3127450-7c18-35a5-bb62-82cb5481e9d3 | -17.1566 | -46.25159 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17d5cc81-dc51-399a-adc9-f924572c1c6a | -15.02394 | -48.10261 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6292d2c7-f58a-39d0-bb25-716c7c24f699 | -13.85488 | -47.98249 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a953228-0d78-3fa3-bc3b-e2bece3529aa | -15.0431 | -50.06122 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca6138a6-c3fe-3264-b4af-5263f4547cf0 | -17.17167 | -46.26265 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c0c01825-03dd-3eda-8590-d9355932048a | -16.30274 | -45.68905 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fbce408-94f3-363f-a573-15343f0f417d | -17.17778 | -46.23299 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f883207b-41a0-389e-aea6-8c32eae70b8a | -16.30094 | -45.68912 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 388dccb2-f6a2-3fd9-9582-17f66235d7ef | -14.28256 | -45.22794 | 2025-09-04 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ae54502-7d7d-3950-9126-c5f323f0fa93 | -15.54439 | -48.40623 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c005ca3b-771c-3e7b-9e49-f5be44387b92 | -17.16307 | -46.24879 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3121483b-fa9a-3db4-a791-aa9231dfc924 | -14.81937 | -48.23256 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d99a53a3-2afc-312f-bf0a-bacbc09fc262 | -12.46118 | -48.07518 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ea77dea-f314-3fa7-b9af-a5075616bc4a | -14.59434 | -48.02376 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17eb6e4e-3f2d-3e50-acff-4318d7ff2263 | -17.1722 | -46.25914 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41eb4fa7-105b-3d5e-84d6-6f4464c49e8d | -17.17784 | -46.23266 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 448baa91-82bf-3894-a1fe-3f410489edc7 | -17.16853 | -46.25008 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6927ed69-f9da-381b-9a9d-0cd5343301b8 | -17.16593 | -46.26165 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 596ab7b1-55f1-3afd-987d-cdb1438f355e | -14.81786 | -48.2403 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6c3532f-1aca-3c58-98b6-057ecf96f7ee | -13.74755 | -46.9444 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7d9b276-8aa3-38a4-a5d1-fd7e881156a5 | -14.5551 | -48.05083 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99c82b03-0b2b-3e70-8b5f-ebf932a38412 | -15.01487 | -50.0392 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9aacda75-f89b-3a95-81da-f958a072a497 | -14.82027 | -48.35356 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac3921be-1075-31b9-b180-ea3ee9e8613c | -14.81087 | -48.21061 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c79d1ab-0ce1-3d3c-b0f9-899668c17688 | -12.89781 | -48.04699 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5a638aa-f40b-33b1-b6a0-2adb02bf057b | -18.32337 | -50.98464 | 2025-09-04 03:38:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1dfd1291-39fc-3173-b7e6-427ca3a66075 | -12.47953 | -48.08691 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 530cee0c-ab77-392d-9413-5758d68bdcf9 | -16.46844 | -46.8668 | 2025-09-04 03:38:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec1c10e5-5ded-307c-975f-157ffd082d00 | -16.30509 | -45.70467 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89a21aaa-6ef7-3177-9004-6c3c1ea3497f | -15.54181 | -48.38743 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdffec69-7fe4-3b06-b7ed-6a5d4dfaa805 | -12.49938 | -48.05859 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2276c35-daad-3e33-a485-8f729862164f | -15.19048 | -48.01756 | 2025-09-04 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25632038-7d18-304a-9d06-07ab09c997fe | -14.81759 | -48.20913 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 257616e8-2347-3f9d-addb-ec7bd4b524f3 | -17.97476 | -47.12327 | 2025-09-04 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c7e3e14-3b53-3eb6-a5e5-02a00c14eeb2 | -17.05243 | -46.44639 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe50ea36-b6c3-395c-9206-feef23ac181f | -12.95531 | -48.068 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ddd7871-8fd0-3074-a5b8-ba9e17451782 | -14.57079 | -48.04013 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed02f601-5814-34f4-9f4e-d1e5319e8bc0 | -18.68443 | -48.18832 | 2025-09-04 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74e1602d-902f-33da-b875-0900d23e2c7d | -15.02901 | -50.0901 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fb09703-b56c-39b5-b05b-6a4c197881b3 | -18.68765 | -48.18246 | 2025-09-04 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89b69466-cf85-3d41-a894-8f651a4e05f9 | -17.17686 | -46.2642 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cf14c83b-a985-3583-9c13-b54293b54432 | -19.23132 | -48.68594 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f0ac45c-ae2d-3b41-8542-b6229eec696f | -13.44247 | -46.94374 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1938536-03f2-32a3-baff-03d8ee400045 | -13.86141 | -47.98351 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5796617-a682-31bb-a971-8735c6dbe473 | -15.18878 | -48.01581 | 2025-09-04 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01cc6286-6511-3b8d-bbf5-8ce79b999d40 | -12.89411 | -48.04303 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7be280d7-cbc9-3d91-a217-c3d81d9ad8c1 | -16.29556 | -45.68797 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d557c081-1c3c-3407-aa78-3c0e4fb79a91 | -14.32651 | -42.95309 | 2025-09-04 03:38:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 66cc658c-d788-3be6-a76e-18512f2f5e2e | -14.77878 | -48.13912 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77c647a0-238a-3931-95d5-c6911f9a902e | -15.02839 | -48.10617 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 056a03c3-10ef-3192-bcbd-c0fb6fea6cb7 | -12.45213 | -48.08503 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92a6e139-333a-3956-82ba-df5962a4d910 | -19.2537 | -46.53739 | 2025-09-04 03:38:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b8c0654-18a5-3278-a99a-ad6ae2422509 | -17.1714 | -46.26291 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
