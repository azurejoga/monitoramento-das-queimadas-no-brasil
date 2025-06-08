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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3285692e-0b0d-3973-857a-677bada16f72 | -14.03314 | -55.12645 | 2025-06-08 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44144c81-ebf2-3562-a45f-e466dabf8d9d | -12.37554 | -57.40885 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c718e61-1699-32a3-8f6f-b460a840d135 | -12.52842 | -58.34723 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f0137f-788f-3b14-b69b-4b31072309ad | -13.8853 | -56.20606 | 2025-06-08 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75af05ba-c489-3d38-a33b-134b15d28293 | -12.52077 | -58.3672 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4048ef79-8f2a-3c2f-a21b-eb43ad7c071f | -12.52655 | -58.36211 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb86836-e669-3212-8cb6-90277891f6e2 | -12.371 | -57.40141 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 870b2a7d-7505-3d5c-8c68-2b037fc2df4e | -12.37512 | -57.41221 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ae5eb59-3381-3c34-a153-b63a6d8d5eb4 | -12.53197 | -58.35996 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 855bc312-1f0e-36d0-9782-7e90518b06bd | -12.37015 | -57.40814 | 2025-06-08 05:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7e80e10-d28a-3e13-b05a-7bdc994e1259 | -12.52299 | -58.34945 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 235ce038-119e-377c-8048-0bbb223fd002 | -12.5316 | -58.36292 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a54984-d945-361f-9572-dda192284aec | -11.47051 | -61.94452 | 2025-06-08 05:46:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd155ebf-e7b6-3650-aad4-ef67440a7f55 | -12.52151 | -58.36126 | 2025-06-08 05:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5cedf4-6970-3240-a863-23483bb6132a | -13.87937 | -56.20526 | 2025-06-08 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989264be-9ff2-310b-a8f2-c90818011d26 | -9.92148 | -59.90296 | 2025-06-08 06:05:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54d77e11-ba58-3931-acef-a431e30c8d61 | -9.92081 | -59.90854 | 2025-06-08 06:05:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac582960-6a62-34db-b32e-4d3a376d2aa3 | -7.01999 | -44.59581 | 2025-06-08 06:14:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a310cd07-f296-33fa-873b-6d35ca8fceeb | -7.00866 | -44.59806 | 2025-06-08 06:14:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| efaabf14-223a-30c0-9836-24b05aa2a86c | -3.04498 | -49.4367 | 2025-06-08 06:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf17a0c8-1dc2-38b1-b678-c173c7d2b9ae | -11.80111 | -48.08989 | 2025-06-08 06:16:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 14d9f871-6cf9-3981-853d-ab2545615e86 | -9.40555 | -48.45353 | 2025-06-08 06:16:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 3aff2040-dfb0-3809-9212-4338be3af854 | -11.37318 | -56.55268 | 2025-06-08 06:16:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36d73953-b955-3530-8e1c-a86f72fbe391 | -13.47223 | -56.85275 | 2025-06-08 06:16:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 41838e0c-4f88-3feb-a054-eda4731a56a1 | -9.40595 | -48.44833 | 2025-06-08 06:16:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e65e2707-6599-360e-bf66-eea5c282dc1d | -12.36788 | -57.41139 | 2025-06-08 06:16:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9c6f0fee-438c-3aaa-97c7-f86fe565d456 | -9.40811 | -48.43336 | 2025-06-08 06:16:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 0a9f30fa-21fd-3e9b-bbd2-b16b343eea92 | -11.1157 | -54.64548 | 2025-06-08 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e39ec2b6-ea5e-312a-9b53-c1b29fe8c8e9 | -11.11704 | -54.63646 | 2025-06-08 06:16:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f88b9328-c85a-3254-8edc-5ada1b966536 | -12.52415 | -58.344 | 2025-06-08 06:16:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 24ba929b-ac19-3099-96c6-2ec49dd38a72 | -12.36943 | -57.40162 | 2025-06-08 06:16:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 678fbfb1-d86d-3a79-9df6-9a17dfbffab0 | -12.52241 | -58.35478 | 2025-06-08 06:16:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eb45816a-3097-3c06-b625-a9fa395367cd | -9.40867 | -48.42814 | 2025-06-08 06:16:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 78762f74-dccf-3e90-b679-fef635b7c2ee | -10.49407 | -53.66553 | 2025-06-08 06:16:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1fb71771-b540-321a-b7d2-46ec988c853a | -7.0169 | -44.5954 | 2025-06-08 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4c74c2d9-fd89-3085-aa69-23204622fabf | -9.4158 | -48.4504 | 2025-06-08 07:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 62b3d448-ccfb-396a-b75a-225ec12086c9 | -6.2496 | -48.5427 | 2025-06-08 08:10:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d0278388-e178-33b4-ad8d-e7b999f3af2b | -6.2496 | -48.5427 | 2025-06-08 08:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cba89e79-d6e6-346d-b3dd-438baa91a12a | -6.2496 | -48.5427 | 2025-06-08 08:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| da9f8452-c565-370d-bdbb-05d7bc7aafe0 | -7.7269 | -44.17236 | 2025-06-08 11:45:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 3903b260-efc8-3ab4-a3f2-ea31609fc242 | -7.72184 | -43.47364 | 2025-06-08 11:45:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 370692ea-7559-3a9c-a6c4-21de820c69b8 | -6.79942 | -37.67064 | 2025-06-08 11:45:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6629412b-13a0-3f9c-a6b3-19f28568f671 | -7.72534 | -43.45226 | 2025-06-08 11:45:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 9e779765-199f-38b2-862a-ff0ba0465616 | -7.7251 | -43.46779 | 2025-06-08 11:45:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 334d6847-3309-3c44-88e7-2b5bcd07c5ef | -5.95201 | -39.22848 | 2025-06-08 11:45:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e58aa00a-8366-3cda-89b5-fa05b5fa700e | -6.51165 | -45.98504 | 2025-06-08 11:45:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 40f1b989-2167-311e-9fbc-89687f9c8ced | -4.83097 | -37.75433 | 2025-06-08 11:45:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5aac8243-c59d-35b3-9d8a-5402c2ec741b | -7.74077 | -44.17493 | 2025-06-08 11:45:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 0a40cc95-bfbe-3b7a-ad2d-33bac4c3f554 | -12.69514 | -45.04684 | 2025-06-08 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c3e8c171-bbb1-3fa3-963f-18892d6e19c7 | -12.69121 | -45.07014 | 2025-06-08 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5788d065-22a6-3486-93e1-a3d2726ed0b2 | -12.68824 | -45.05271 | 2025-06-08 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| f95a104b-164a-3b14-b0f6-4c81d0c5a4c5 | -15.06594 | -43.80843 | 2025-06-08 11:47:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6aeacfb6-a226-33d7-88ed-05fb327e7af1 | -12.25725 | -44.91435 | 2025-06-08 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 48e67c22-f6e3-3d1f-a458-9e2596171b5a | -13.57823 | -41.56398 | 2025-06-08 11:47:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| beaf8fd4-ded2-3280-8235-7479ce498d89 | -12.53258 | -45.41056 | 2025-06-08 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 635ecee2-512c-3840-9353-947c070e447d | -12.25089 | -44.91935 | 2025-06-08 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7b7d1a4b-09d8-380c-a617-1ca4eea4eb57 | -13.72384 | -41.87313 | 2025-06-08 11:47:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| eea34ecc-384a-3026-b0a3-80abe086028a | -13.57628 | -41.57614 | 2025-06-08 11:47:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 61969de8-ec8c-3a9c-90cb-c3b20812b810 | -13.72589 | -41.86034 | 2025-06-08 11:47:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |


