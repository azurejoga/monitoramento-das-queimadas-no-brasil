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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 725e9d3e-104b-3faf-b978-5f37ecf16e4b | -2.2526 | -51.93545 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73825855-e0a0-343e-8ffe-117bfdf56f79 | -2.24759 | -51.9307 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49f01dae-3376-3bb8-941a-fc0d4d460b51 | -2.24697 | -51.93448 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8b86015-5a77-37f4-a10f-fb36f2404bff | -2.23773 | -50.45314 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 019adc87-f2ae-3c58-bfcf-6c2aca29fa4f | -2.23263 | -50.45236 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c508c4bd-f6f7-35dd-b26e-457eb47cf125 | -2.2319 | -51.88551 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be987d71-facd-3e66-91ae-a8c377884f77 | -2.23165 | -50.45828 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3be8774-b87d-3989-8ad9-e7653048176d | -2.23128 | -51.88929 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce862a44-803c-3d58-b96b-85705cd405bd | -2.22704 | -50.45448 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b8d3caa-4a3f-3da2-bfe6-f5c8b9773fe5 | -2.22655 | -50.45745 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f66614cf-eb8f-376e-bf71-8545c192b4eb | -2.22629 | -51.88458 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8819ba37-146f-321c-9324-fa2678be7051 | -2.22605 | -50.46042 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be59dfce-18c4-3468-ab95-f2c552554cbc | -2.22566 | -51.88835 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db68e60-4207-3870-9527-b9e2129aacc2 | -2.22193 | -50.45367 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a460e5b-066c-3269-8752-5e4c331830f7 | -2.22144 | -50.45663 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01e5dd88-4931-3a58-badd-4ddce11f54d2 | -2.22095 | -50.45961 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b87cbbd-d804-3474-8407-0563a9fcc23c | -2.22045 | -50.46258 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c453d6b1-2114-36dc-9e2e-2752641bdeaa | -2.22004 | -51.88745 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8062d3c8-4ef5-3a30-bb93-09edb24fae90 | -2.21123 | -50.45501 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 630769fb-6b5e-3006-ac03-04d4821cbe4f | -2.20973 | -50.46399 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c658513-d905-3926-8610-19f3cbb104d5 | -2.20924 | -50.46695 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab009ef6-ba59-3be6-bd16-888513acc42c | -2.20865 | -50.45366 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6c4cb1a-91a3-3ef7-b067-3946157374a0 | -2.20817 | -50.45666 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b6ebb6c-f38d-3b53-9f5d-19c3dbe046e2 | -2.2077 | -50.45965 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 015e4836-a6f4-3343-9122-eaf420fe0ec2 | -2.20722 | -50.46263 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb4a77f2-7595-3133-95f7-054bd43c4e9e | -2.20675 | -50.4656 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ce77e1e-db1e-356e-9cac-6f04aef63d98 | -2.20514 | -50.46009 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4741debd-c770-33b4-b711-bf3cd16dbc83 | -2.20464 | -50.46307 | 2024-10-21 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5764b78-29ec-3e7f-8295-2bff82c38904 | -2.19175 | -49.13204 | 2024-10-21 04:12:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e9c26c4-32c6-338a-9baa-d836e061a116 | -2.16493 | -50.70079 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0d1c925-98e3-371a-a8bb-caa40e535fd7 | -2.16416 | -50.70005 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26125c7b-018b-3a59-bef6-48da7e1a1c17 | -2.16367 | -50.70316 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47917d6d-6567-3d97-87bf-115fcd0cb167 | -2.14922 | -47.05895 | 2024-10-21 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cf437ab-54b2-309e-ab05-a2f827177ad7 | -2.07268 | -46.83754 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58e665b8-006e-3d0c-9647-41f9477dfa9b | -2.07185 | -46.84269 | 2024-10-21 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd6e632c-b5d7-3af0-8a9a-9dc3093282fb | -2.05907 | -46.89646 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1109983b-1a75-3455-bb6e-582e44cd1b21 | -2.05851 | -46.89993 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d77baa2d-7ec5-303d-bd99-04bdda1e3ee5 | -2.05506 | -46.89582 | 2024-10-21 04:12:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| acb776b8-336b-3089-94b7-1eb8dd2ccc5e | -2.03887 | -48.40784 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b46c8e6-17fe-3255-92da-9f0c6f97b25f | -2.02049 | -52.12391 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e38fc89c-44cc-3460-af6f-3ad58bd55b65 | -2.0202 | -46.21301 | 2024-10-21 04:12:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d3bd3b2-57da-3d70-bd5c-a79b7ee4fd67 | -2.01986 | -52.12784 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb1723ca-22cd-36e2-a775-377593912cf0 | -2.01853 | -46.21009 | 2024-10-21 04:12:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e713780c-7c28-35ce-b4fc-b9421aaa1013 | -1.99059 | -52.12701 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e59bf012-c260-3f6f-84d0-ae66f82e08e4 | -1.98994 | -52.13097 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddca17f9-d9d5-3150-8843-d6ef40dec93b | -1.93897 | -52.11128 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba1cefd1-2918-3925-a789-d0b35108a440 | -1.93533 | -52.10556 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b5d6f3f-3426-321e-8c8b-bdafc5661308 | -1.93468 | -52.10943 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9bc39e21-8b12-3b34-9a79-786b6cd201e9 | -1.9345 | -52.10251 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c10d784c-d119-30e9-80ef-7424d7223993 | -1.93403 | -52.11333 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5edd5d60-653a-34f9-b5bd-7c715a0b12bf | -1.93388 | -52.10639 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e8f6066-eff1-3514-9af4-366004aaa63a | -1.93325 | -52.11029 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d7f1e90-6c20-313c-9ebe-ccac6c1d0551 | -1.93262 | -52.11421 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14bfb543-d4b8-3a91-b940-da2e0cf7e657 | -1.92963 | -52.10449 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ae2d05e-47b5-3213-b0da-df973c1022c4 | -1.92897 | -52.10841 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44395b91-bc39-331c-ba17-f2d1d0f7f756 | -1.92817 | -52.10534 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b1db818-7cab-3211-a7e8-2591e18baffb | -1.92753 | -52.10928 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23ba1b2a-7dbd-380a-b9ea-7574eabdc359 | -1.88968 | -50.02056 | 2024-10-21 04:12:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18f4c7e0-7002-3200-a666-714409d18f4c | -1.79254 | -48.42908 | 2024-10-21 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25f29ae3-265f-3fe8-98c4-92dfc443839e | -1.78869 | -52.05564 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 728c758d-1353-31af-b5ed-e0718340556f | -1.67115 | -50.46661 | 2024-10-21 04:12:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0083036d-82b3-3a2d-b75b-914ec089dac8 | -1.67067 | -50.46966 | 2024-10-21 04:12:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 222267db-6378-36c0-8ed3-28117183ecdd | -1.64513 | -46.13691 | 2024-10-21 04:12:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd721c9-5b15-31e5-bcdd-9f40d6a7bb84 | -1.63765 | -52.64416 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e514f66-aad9-3a07-8411-e69d9d09b8c6 | -1.63693 | -52.64849 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41f737e2-66df-35e2-88e9-62db432bb5d0 | -1.6362 | -52.65282 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 454ab4a8-0a4d-3f68-bb3a-eb0af8aede39 | -1.63496 | -52.64331 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2383d0aa-bdaa-366c-97f0-9b1bf4aff23e | -1.63427 | -52.64764 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd612e8-f600-3de0-8c04-1e1e0cccfd9a | -1.6317 | -52.64317 | 2024-10-21 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d495d8db-c280-33d4-8e4a-0c64033e6ea3 | -1.53101 | -47.16442 | 2024-10-21 04:12:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e73c7b1-e35f-338f-96a4-418c28272671 | -1.48444 | -48.96643 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83934d26-15d5-31d9-b179-de4183c38896 | -1.48235 | -48.96479 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e7bfdb1-11dc-3e0a-880c-4ef380a8b1ff | -1.48057 | -48.96087 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59362066-64aa-3098-a4c0-29506adb6226 | -1.47978 | -48.96569 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90766458-29e0-3a1a-af5c-55968ddd374b | -1.47769 | -48.96404 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf5af1bf-a8fa-356c-8988-6fc277a3e63d | -1.47592 | -48.96012 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 021afc62-7ced-30d9-a789-02f0abe65adc | -1.46913 | -48.95765 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8fbd978-57ae-3351-911c-4a0f30b13b43 | -1.46661 | -48.9586 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0932f6df-e589-317c-be53-e68bf1c5fb46 | -1.46448 | -48.95688 | 2024-10-21 04:12:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2007efb6-237d-363e-b380-854956416896 | -1.20441 | -53.63947 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca128643-7a58-3066-91bd-c3938672e83d | -1.20367 | -53.644 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9380700-14dc-3e8f-89d7-6b5f9afd2f04 | -1.19881 | -53.63367 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12dceecd-efa4-3fc8-bbc7-50457b58c1ff | -1.19803 | -53.63847 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32f87590-9442-3843-b0b5-7e886c789ebb | -1.19728 | -53.64306 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a76fbb1-8a30-3ae5-9b70-ebc4a20767d4 | -1.19238 | -53.63299 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c8f5bc3-3bc9-3727-92fe-91ff40a61f7b | -1.19159 | -53.63781 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dfa2d85a-aaba-3265-9d10-4e81f686ed6a | -1.1908 | -53.64261 | 2024-10-21 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3b642ca-803b-3765-9cff-b448abda6bcd | -1.18769 | -53.62165 | 2024-10-21 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2da89505-33aa-3944-898a-a001338bdcc3 | -1.18682 | -53.62696 | 2024-10-21 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bff97660-1c65-366f-97b9-45ab14029d50 | -0.18048 | -51.53971 | 2024-10-21 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4bba9ef-c8c9-30a2-a416-91105137b13e | -0.17988 | -51.54354 | 2024-10-21 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c935cb2-1302-30a5-9cc1-c949aaa91ed2 | -9.90341 | -42.10131 | 2024-10-21 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 030ed698-fdf0-3f54-a3a3-c972504e505c | -9.90285 | -42.105 | 2024-10-21 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2062c58e-2ec9-37ab-8154-b8c769da8a25 | -10.90123 | -40.53692 | 2024-10-21 04:14:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1f14a293-a5d3-3489-9926-bb95e4ae771d | -10.2853 | -36.30466 | 2024-10-21 04:14:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 68357a9a-37e4-3dbb-a1b8-4bc465085f9c | -8.7532 | -49.78796 | 2024-10-21 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a352a2-917d-3e90-a6f9-b59dbb28aeba | -8.74882 | -49.78724 | 2024-10-21 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f5ae58c-b4cf-35ce-b348-89ff9e22f4f6 | -7.49419 | -46.94065 | 2024-10-21 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bbac983-b631-36ef-b558-669bda9592ce | -7.04147 | -46.98133 | 2024-10-21 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec8f6e8c-3f9b-3b5a-8fdb-b161a182386b | -7.03348 | -50.24226 | 2024-10-21 04:14:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README32.md)
