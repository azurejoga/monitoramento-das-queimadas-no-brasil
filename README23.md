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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faa1dbf1-8e0f-3e73-bae5-6fed17202761 | -21.1273 | -48.59031 | 2025-06-29 04:36:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3439f551-6eaf-37e8-8815-553088e65d85 | -22.93523 | -45.70011 | 2025-06-29 04:36:00 | NOAA-20 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 6786ee51-9ad3-377c-b89f-8c03d2c94b87 | -20.31169 | -45.58201 | 2025-06-29 04:36:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efc2334e-f29c-361b-98b5-9d07b9895e53 | -20.76331 | -46.76875 | 2025-06-29 04:36:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b0ffea72-4c3e-34e0-bb05-5c047064671f | -21.2001 | -56.93447 | 2025-06-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c938938b-2611-3cb3-b515-97d90778388f | -20.51401 | -49.05048 | 2025-06-29 04:36:00 | NOAA-20 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61d68724-9b57-3848-8523-bc11100d69cb | -22.87582 | -47.80174 | 2025-06-29 04:36:00 | NOAA-20 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b6a4986-0407-32eb-818c-9d7f8849c763 | -22.40738 | -46.82402 | 2025-06-29 04:36:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45c57513-fa74-3ca6-b500-0e02f7492de7 | -22.59702 | -48.43766 | 2025-06-29 04:36:00 | NOAA-20 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4a00eda-fbbc-3d09-ae55-5bad272e108a | -21.53437 | -45.46714 | 2025-06-29 04:36:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e1073f84-9062-3abb-8674-f9f3b5cb4824 | -21.19426 | -44.93796 | 2025-06-29 04:36:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d329cc2-e948-31b4-843c-68e23927a5c8 | -22.67827 | -42.85426 | 2025-06-29 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 40b0f84c-06fc-3ec9-86c3-4596acdfc84d | -22.67859 | -42.85112 | 2025-06-29 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1358c4e-4f63-3eee-97b6-d07a477ebe79 | -23.15828 | -48.33665 | 2025-06-29 04:36:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a646f36c-e4ba-3299-bcf1-74ae4baadacf | -21.33861 | -55.62572 | 2025-06-29 04:36:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa7e8287-0f4d-3547-9725-b32c2fd88c79 | -22.69345 | -46.50628 | 2025-06-29 04:36:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dedad0a8-a0a3-3f37-bad3-c57f8e4902ac | -21.19605 | -56.93359 | 2025-06-29 04:36:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79458483-75e4-3b70-bd76-1ed82f635521 | -23.30516 | -46.50032 | 2025-06-29 04:36:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4aeb389d-ff95-376a-9316-63db41e52498 | -21.34627 | -55.64782 | 2025-06-29 04:36:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56870bf-52c4-321f-97f9-cd309cdef338 | -23.40864 | -52.76619 | 2025-06-29 04:36:00 | NOAA-20 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3504b01f-fb25-3074-96ef-aab9ed82d6c8 | -22.40807 | -46.81874 | 2025-06-29 04:36:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f9ae692-f42d-3953-9634-24bf3d80d569 | -22.97164 | -44.03743 | 2025-06-29 04:36:00 | NOAA-20 | MANGARATIBA | RIO DE JANEIRO | Brasil | 3302601 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f5fd5a9-5502-332e-9dfc-711847ffa66a | -21.40491 | -48.4879 | 2025-06-29 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e59e0c1-08b2-346c-abc1-38f2bd949279 | -22.97335 | -44.03856 | 2025-06-29 04:36:00 | NOAA-20 | MANGARATIBA | RIO DE JANEIRO | Brasil | 3302601 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 352e3bae-d09c-3a5e-a9c5-12c1e2c44941 | -21.33771 | -55.63072 | 2025-06-29 04:36:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07cfef37-bbc3-3eb1-b66a-9478ef5bf9b8 | -23.33844 | -46.76975 | 2025-06-29 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b211e85c-782a-333e-b41c-cbb04ddb5c63 | -24.24071 | -50.74028 | 2025-06-29 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e8c725c-167b-36b4-ab69-a4aea265178e | -22.40414 | -46.81824 | 2025-06-29 04:36:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 721603fa-4c04-3a5a-9575-c2b4f693975b | -19.02239 | -57.62073 | 2025-06-29 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49f7e668-7092-332d-94f0-5f46253f7396 | -20.99602 | -51.79395 | 2025-06-29 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 80d38fd8-df5c-36ea-9962-8389045c94ce | -21.01686 | -50.17261 | 2025-06-29 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a5e50e3f-eaf7-3a73-aed8-f3495338ce18 | -21.02021 | -50.17317 | 2025-06-29 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d5c7e2ba-d20a-3c21-9bcb-7dcd26a93e68 | -23.27136 | -51.20748 | 2025-06-29 04:36:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 511dbada-7266-39ef-ba97-9ccbd3456217 | -20.37464 | -45.60251 | 2025-06-29 04:36:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 704d7ca8-d9ac-32e1-b1c7-46b80f406b7f | -23.59287 | -47.43674 | 2025-06-29 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbcd4b4e-fa12-3e8b-8e2b-37e95dfb5a6b | -20.47654 | -53.67402 | 2025-06-29 04:36:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ab0c713-c929-3f3b-81c6-0b0f42c8d9c6 | -20.31065 | -50.18335 | 2025-06-29 04:36:00 | NOAA-20 | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| da538177-7d61-3566-90b7-a3cfa74ff789 | -11.5312 | -52.7678 | 2025-06-29 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7cd3bf94-c6a9-3be5-a3f2-c7445aef5ff8 | -10.9811 | -45.1104 | 2025-06-29 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 6087c678-9aee-34a9-9eaa-f8216f4522a5 | -10.5579 | -52.0289 | 2025-06-29 04:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 47cf5525-a09f-39a8-8260-66879e08e4b6 | -11.5502 | -52.7659 | 2025-06-29 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 89e6b7df-f78f-3c88-967c-cad217e0f9f9 | -11.5499 | -52.7867 | 2025-06-29 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 64e2fab7-6f03-3185-92db-e15b5a064eae | -10.5576 | -52.0499 | 2025-06-29 04:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 01d8c2cf-0a0b-366b-8218-e7e3e7962176 | -11.5309 | -52.7887 | 2025-06-29 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bce84c1b-f1a2-3656-bd51-7fbc975e0015 | -11.5499 | -52.7867 | 2025-06-29 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 1d3d94e7-73a8-3f74-ad55-26f40353ee93 | -10.5576 | -52.0499 | 2025-06-29 04:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 41a3f3e2-ed41-3bd4-92d5-bb7b88049e98 | -11.5312 | -52.7678 | 2025-06-29 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 2781db6b-dfe9-367e-bf8d-659a5612e3f8 | -11.5309 | -52.7887 | 2025-06-29 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8972d779-9c0b-3b9c-bee4-499f92ec5356 | -10.9811 | -45.1104 | 2025-06-29 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 560867a4-c98e-35c9-94ab-e118627089a4 | -11.5502 | -52.7659 | 2025-06-29 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| c6a3345f-83c1-349d-b2cd-93e0f1ab07bd | -11.5312 | -52.7678 | 2025-06-29 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 1f7e1efd-700d-3f95-bfb7-0b84f7c8b4cd | -10.5576 | -52.0499 | 2025-06-29 05:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| fb7095a9-bf6c-3557-bf0f-8bc881f62d08 | -11.5499 | -52.7867 | 2025-06-29 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| dd80b40e-8882-39c6-90f3-484fc96001e1 | -11.5502 | -52.7659 | 2025-06-29 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 06bf8bf2-391e-38b5-987f-5fd83dfe1f7a | -7.18562 | -43.69808 | 2025-06-29 05:06:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 46dfbfae-f564-3a68-9156-c82c637474b6 | -7.18296 | -43.7028 | 2025-06-29 05:06:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4e9d739f-87a5-3e77-b8d3-730045c137d2 | -9.42088 | -47.92655 | 2025-06-29 05:08:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9984139b-90f9-3853-8f5c-d51b01f9a76d | -10.97149 | -45.11078 | 2025-06-29 05:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3cf69517-59de-3e98-ae7f-f3247e1798d6 | -9.42296 | -47.93108 | 2025-06-29 05:08:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2cf30e2a-47cc-34bd-a916-cdaf504ab16d | -11.5502 | -52.7659 | 2025-06-29 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 1b3f9ce5-508f-3dce-8339-9b79ca2c3301 | -11.5499 | -52.7867 | 2025-06-29 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| ceffd36c-f172-30d8-be75-012f78259ec6 | -17.39882 | -42.62432 | 2025-06-29 05:10:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7719b9f9-f50f-3d21-b2f5-0a09cfada9a3 | -11.5502 | -52.7659 | 2025-06-29 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2d5f3a11-9581-3f82-89f6-b7f196a5eb20 | -11.5499 | -52.7867 | 2025-06-29 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7f8cf91e-d21c-3053-aa9c-b4de7cab0f0a | -10.5576 | -52.0499 | 2025-06-29 05:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 322ba378-e9f7-3e06-9424-c6a5841ba270 | -10.04205 | -59.36143 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47bb7a8a-0748-38ed-8c12-88fdfad187dd | -5.3265 | -55.94576 | 2025-06-29 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a96154d8-3ff2-35c8-90c6-d6ec0687b11b | -10.03807 | -54.32942 | 2025-06-29 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9270859-2ef9-3784-9d77-f393a6b0c0bb | -12.06497 | -48.47156 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3305dbe4-323c-3d00-97a1-f93ccdbf06d9 | -11.0232 | -56.27684 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dda1e9aa-b8c5-3676-9451-f082b7ecbf3a | -9.08675 | -59.49163 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 505d64c1-1feb-31e0-9462-4e6a9b0a8fd7 | -11.26684 | -52.74351 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a9b45bc-2380-30b9-858d-afcaa56554f6 | -9.35705 | -58.85224 | 2025-06-29 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c5b431-022f-3750-b5b5-9c842f913ae0 | -11.55426 | -52.79752 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef547d41-dffb-3d19-b386-991682f6cbbe | -11.2717 | -52.74751 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aff26df6-f228-3680-88db-93a5e6f08c1a | -11.0285 | -56.25754 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d03acdaa-9832-3ca9-b7af-08b6b37e7927 | -9.70186 | -56.18292 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f922de67-bcaa-3690-b97b-d01d4000342d | -10.45958 | -58.68152 | 2025-06-29 05:23:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 372d7e9b-f527-3f92-a6b6-6ecb3b7b5336 | -10.16415 | -53.92957 | 2025-06-29 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a0a4676-f0ae-34e9-b97c-2262f2c9a7fb | -9.13661 | -61.44221 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282a30fe-7883-386b-a8ca-cd27184f0065 | -11.03421 | -56.27765 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a939803-d2a7-3cf2-91be-67cae5357fae | -11.2721 | -52.74421 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bda6c481-fd65-3c9f-b461-d210d150eaf7 | -9.09071 | -59.48845 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817600c2-90af-39a5-86fe-fb74e635c1fa | -11.55828 | -52.80807 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9276f64a-6396-397c-936a-a58903987932 | -9.92559 | -59.90081 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4eb91c01-0f56-3198-8d16-e5410aaa9649 | -10.56512 | -52.03769 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92df6da2-fb80-3257-bc55-1865f0122518 | -10.03973 | -59.35326 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d49fe65-264f-32cf-ae9a-a4f960ab0954 | -5.08531 | -48.3567 | 2025-06-29 05:23:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95b5a029-0f10-3c0e-b76b-74348117b4a7 | -11.01561 | -56.24107 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66773482-b067-3b48-90bb-222d1ce3ff63 | -5.32557 | -55.94409 | 2025-06-29 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c2fb302-b18c-36df-878a-b542a41dcdd6 | -11.54375 | -52.79597 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90d08724-665e-3895-8999-93fe8d523e1b | -10.46013 | -58.68233 | 2025-06-29 05:23:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30bce76b-8caf-312f-87bc-9eea949f65dc | -4.32161 | -48.07642 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 36930886-f2d2-3ce8-a1e4-5fc9e6651f69 | -11.02427 | -56.26933 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be6029e6-37f2-32cf-bfb2-f0c711feaceb | -10.03861 | -59.36088 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9dbd383-495a-3609-a154-c8dcab1d50f2 | -11.53609 | -52.77144 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6de19fe8-c4ec-3885-8dbc-582cf5254c9f | -11.02214 | -56.28436 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efac960f-1168-3a1c-8b72-623ce1183a70 | -3.62754 | -47.54397 | 2025-06-29 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18696626-51f1-3ddb-8579-2c2e390c1331 | -9.11029 | -59.05297 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4057993-fd01-30b6-86d6-8191c67d1248 | -11.01614 | -56.2373 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
