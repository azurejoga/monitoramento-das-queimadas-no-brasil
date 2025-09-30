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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a0544ac-b793-3050-800e-3edc011e96d7 | -10.83606 | -45.41156 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de18c8d5-190b-3bfc-80d9-e3118824844f | -9.95915 | -48.80407 | 2025-09-30 03:47:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7b031a6-b238-324c-9b8f-7c7b7900d93b | -9.69382 | -48.24715 | 2025-09-30 03:47:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 449f46d5-3314-3ad6-b905-f84c68f20cd6 | -9.04441 | -46.69879 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8409c9c9-db57-3bc8-9094-b9fec040b810 | -11.43979 | -43.50724 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 328661f0-83b8-3e56-9078-c1ee177574d6 | -11.45112 | -44.97975 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b00e541-782f-36c8-bdd7-51333ea14b87 | -10.19025 | -44.89016 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d4b708a3-21dc-39fd-ae40-7eecafda904b | -8.32809 | -46.22009 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4a43ed7-8bd1-3684-9e72-8c6d0cdcf622 | -9.37224 | -47.58237 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd5bccd8-cf2c-3e0b-b4da-ca8660859bac | -9.82876 | -48.72638 | 2025-09-30 03:47:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 330a9f08-b222-3511-a177-4bc5c8abfc94 | -10.18909 | -44.88236 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0478cb2e-69d3-3357-86d0-93c678fb324f | -8.89368 | -45.03928 | 2025-09-30 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd26ac70-2fdb-36af-afcd-ad9f7220f14e | -11.41755 | -44.90332 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e8ae883-0f75-3eb4-979a-8806df470832 | -10.07145 | -50.22031 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c151707-6143-3fb8-81dd-4fb9f86d7ef6 | -3.85466 | -48.9748 | 2025-09-30 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ccb5abd5-78f0-37dd-aa94-7685ba162efd | -11.35853 | -44.94494 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90e9fd3d-1566-3bbe-bcc5-24aceb36e2d3 | -7.83072 | -47.00282 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3cdd4a51-2c59-3a5f-8bd6-81ce1af2f06e | -8.15744 | -46.38637 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 609d136d-a0f4-3c7c-be36-1dbc309e73d5 | -9.36927 | -47.58723 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f07adfe-a614-3534-8ca3-fd82a018411a | -8.14313 | -46.37376 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d86b0122-f910-374f-ac49-b74632606489 | -10.19229 | -44.90599 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d7385a34-f207-321c-bbb5-4d2a103c2166 | -10.1847 | -44.89423 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 112b9aa4-2696-39c3-b899-2263ce7e0962 | -8.26161 | -45.51221 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80b8d091-3323-3a3d-8210-2e5030e0327e | -7.82585 | -46.99773 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98838459-23b0-3474-b34e-c7b63727893c | -11.51013 | -43.54849 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68807ae0-749f-322c-abe6-20ba67b36f17 | -11.42212 | -44.90425 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d279cf77-8575-3cb0-9fcf-3ccdc53608a6 | -7.47722 | -47.27104 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 080335af-c953-35cf-a34c-d00c24b8bb38 | -4.16082 | -40.00198 | 2025-09-30 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4af3801-4ad3-39b8-b1ac-5ad21392c5aa | -8.96402 | -47.44762 | 2025-09-30 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 999d250d-7f88-3c2a-adc4-c1a4c52593e0 | -7.66441 | -47.42641 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a715ef3-3206-3df8-96ce-481499aa76bf | -11.46154 | -45.00124 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53e6473b-873c-3891-a8c2-1827d644d554 | -7.91949 | -48.18309 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a53f11e9-2337-3e80-b7c2-aeaa2629be8f | -7.51825 | -46.69036 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 682837a5-7237-32d9-8c57-a5e2dc3a62e3 | -7.81535 | -46.99176 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98deb4c1-997a-39df-b961-26497d761a04 | -11.51779 | -43.55407 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be57b5c-8a13-373d-b62a-c8ef01cf9d9c | -10.66096 | -48.54834 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465e5737-645f-33ce-83ca-a74a0dde19d5 | -10.39003 | -48.14915 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ae9add5-a4c8-325c-b445-172da3fd1297 | -5.51013 | -42.72812 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9f7e9206-93c9-3b4a-9350-fe59a571ff3d | -4.62374 | -43.54551 | 2025-09-30 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ebfa8e3d-fefd-31c2-8fc3-30ce43391c10 | -8.50337 | -47.2593 | 2025-09-30 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 126ce31e-5566-38e8-b4a6-e340370963c3 | -10.8468 | -47.95845 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40d39ab8-bd3e-3a40-bf09-fa6922b640ef | -9.05088 | -47.63264 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09107d57-55a2-3b84-a3a9-6ae473812fb8 | -10.65018 | -48.54086 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbda69c1-4fcf-3dbb-996f-847b3ac06fd1 | -10.19569 | -44.89901 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4fb8afe-12ff-32d2-96cb-3bc0ccd929f6 | -9.1258 | -47.64339 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a858807a-b32f-39c5-80a8-17c4e470e5be | -6.45835 | -35.08575 | 2025-09-30 03:47:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ff22b418-f86b-3c08-9cd2-699544ee85ae | -3.18264 | -40.71621 | 2025-09-30 03:47:00 | NOAA-20 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2ffee43-592b-31c4-bb9f-ebac5dce3667 | -9.26897 | -45.69948 | 2025-09-30 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f240c9b6-c11a-3720-8281-5a604d17d065 | -8.15204 | -46.38564 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b49880c-9b27-33a3-aa77-7df2350c4072 | -8.23067 | -45.51044 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 768b0e10-3590-3aad-b0c4-759667a4c0e2 | -10.66016 | -48.55247 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00f3a82a-a303-3996-aafb-eb40104642dd | -5.03989 | -43.61399 | 2025-09-30 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 58e9425d-9824-3d75-baae-7deefb7db644 | -5.41579 | -41.32819 | 2025-09-30 03:47:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6798671-13ab-3f92-9f83-c4d7c745fdbb | -9.93528 | -47.4628 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99fadd30-6ede-398a-9cf3-098bf54ea6d8 | -3.88174 | -42.51168 | 2025-09-30 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a880fc37-76a9-36eb-af65-a8bd61ba7925 | -10.19112 | -44.88524 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e6fe0242-054d-306c-b4aa-eee54861f7ac | -4.07273 | -48.04618 | 2025-09-30 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45352cb2-c2c1-3eb2-9fc0-3e5770ad0892 | -10.75858 | -45.37531 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29601799-fbdc-3578-b346-f15feb767aae | -9.96032 | -48.79797 | 2025-09-30 03:47:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2c23840d-1431-3cde-8a4d-bcc655629b82 | -7.79616 | -48.03397 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b66ae567-43c6-3532-862e-61d91efa0eb3 | -9.02568 | -46.7097 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d189f0e-73e7-33ba-a7a7-c252558120cf | -10.39357 | -49.04546 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5310cdb6-6419-3cf3-b39b-524f7329484b | -10.03557 | -50.19489 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1599c07-8aff-3870-8442-645fc7a7b0d8 | -7.49616 | -46.12629 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5842f1e1-42ec-310a-b3c1-8d1d18fdc8a0 | -3.10375 | -47.01876 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8318880e-4632-327e-97da-07005e501e1d | -8.83035 | -46.18691 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bf87961-a9f3-3c0e-9501-f8dd58b5cffb | -3.81287 | -40.9555 | 2025-09-30 03:47:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6ccf8b6-fabc-36fc-94de-c785cd16c50e | -10.19404 | -44.89608 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a5346910-19e9-32e2-9049-fe46d9a55c3b | -11.46017 | -45.00355 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe42f2d9-618a-3418-9d5a-feada3630794 | -5.34988 | -42.28947 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1196fcf-dfb0-309f-adb2-b9adc3b17249 | -8.23292 | -45.50545 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1437d2e-7ffa-31c2-8d24-28e303a985d4 | -8.5462 | -44.67073 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4188829e-8f5e-302e-8495-0c6317ba45a7 | -11.45981 | -45.01085 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 166564b5-383f-31ae-96f4-a3255bb2a875 | -11.49465 | -43.51371 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 228183f7-334f-3fd4-a7ec-1d11b5f6b5fd | -11.49815 | -43.51833 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30be974d-c966-34c8-b486-83f1feef987f | -11.45927 | -45.00834 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c991858-a14a-3df2-8580-ebced17728ab | -9.44235 | -50.89737 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a46401ed-4650-3e39-887d-46cf0527da25 | -7.29856 | -47.30162 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c6c8a57-0a62-32bf-bede-e776139d6491 | -5.49924 | -42.73923 | 2025-09-30 03:47:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e7adb4e1-1ea9-3de7-84f1-8852253f6e79 | -10.83095 | -47.97956 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f008560b-baec-3fc4-8f2a-077140e6da9a | -7.81465 | -46.99564 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76f931e1-9da7-30a1-a4d4-9a0a9e36cbec | -11.43242 | -44.95182 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1499fa99-7ca1-3cb7-ada0-73f9aa47d6ac | -11.86655 | -41.50185 | 2025-09-30 03:47:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54677660-eed1-31a5-ba46-4f362284b7b8 | -5.32984 | -43.73124 | 2025-09-30 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 80872c5e-4dd0-392b-a68d-27dd1d71fc08 | -8.25132 | -45.54013 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| def5c928-9d17-3b26-a101-2012e7fb1fac | -7.8606 | -45.27941 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2b0bd70-5f1c-3cbd-b1a3-9f3a66d85c26 | -8.23121 | -45.50749 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3ace45c-5ff5-3369-9134-403b48852603 | -9.99331 | -45.40684 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe187d5e-022c-3880-afc7-ea3cad4e0a3b | -9.57763 | -40.35555 | 2025-09-30 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 67ae9701-7f23-3e8b-86ba-aaad0101e15e | -11.04756 | -47.65745 | 2025-09-30 03:47:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4bff319-f7e7-30b3-a187-45422b222273 | -10.10517 | -47.79336 | 2025-09-30 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad08b962-3d97-3942-9735-d33cb329afa0 | -3.85274 | -48.9721 | 2025-09-30 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1892657f-d9cb-36fa-871c-e3be8b78f940 | -3.67666 | -38.93359 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d33d053-f50e-3d9c-bf60-2915ccac4bbc | -5.42349 | -42.29384 | 2025-09-30 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7946cfd4-3dde-3ef2-8cc8-f0747d1367da | -8.06658 | -42.94767 | 2025-09-30 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 546d197e-9530-3710-a950-b2c78877a169 | -7.91604 | -44.61605 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00ca069a-27cc-39c0-8fde-40e00bf235d7 | -11.45017 | -45.05688 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1f853932-0740-3100-8f09-20f851ae22ff | -4.1407 | -44.42572 | 2025-09-30 03:47:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 142e15f8-96a8-3e44-bfee-36a300492f30 | -3.09769 | -47.01773 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e190c7ba-d8f0-3c8b-ac89-d31fbfd68241 | -3.09162 | -47.01677 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README25.md)
