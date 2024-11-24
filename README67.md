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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 869c054d-7bba-3858-afa1-ee1fbceaae88 | -7.82238 | -44.18991 | 2024-11-24 04:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eee5becb-f465-320d-b13c-54b716519504 | -7.32228 | -46.58305 | 2024-11-24 04:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0fa5337-dba3-3a0a-b59f-3d340ddfe475 | -7.688 | -42.98441 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| acffabd1-86af-372f-8680-d24bbe8bb751 | -6.9924 | -46.31676 | 2024-11-24 04:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ad158b0-e852-3f2c-8cce-cb71647667ed | -7.68535 | -49.12029 | 2024-11-24 04:55:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb995274-0926-39b8-bc04-bfdf35f6a7d6 | -7.57085 | -49.40406 | 2024-11-24 04:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44c91250-6fac-3c7b-b082-749fe33fc7ec | -6.64955 | -55.33776 | 2024-11-24 04:55:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49994974-c3a7-31ef-ac87-aa50d49824cc | -6.6894 | -48.86578 | 2024-11-24 04:55:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1b3644d-3fc6-373c-a636-243f8bf5b95d | -8.0516 | -47.08521 | 2024-11-24 04:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9be965ae-d3a5-331f-a292-ae7f1a1f5662 | -7.69599 | -42.98343 | 2024-11-24 04:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 94d501a1-141a-329b-824b-1072ab8f68a6 | -7.56713 | -49.4035 | 2024-11-24 04:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82fa5acd-be69-3ed6-8e36-86db32d9e494 | -20.32249 | -48.81952 | 2024-11-24 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bae113a6-9f52-349d-b82b-915bffa53654 | -7.71556 | -45.67218 | 2024-11-24 04:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 579ecc90-2221-3d78-a190-98cc7b0edfac | -8.05592 | -47.08595 | 2024-11-24 04:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7995f048-7933-3469-9c4a-2d3b1770bef0 | -8.93732 | -44.2536 | 2024-11-24 04:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11ce91da-9212-3a63-b193-c3ca75d7c050 | -19.06383 | -53.46725 | 2024-11-24 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d87cad-d666-3021-899a-d1e7c9860063 | -21.12167 | -50.58701 | 2024-11-24 04:57:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 55045743-3b2c-3cbb-94f3-1ce54a3d7422 | -22.78909 | -52.6541 | 2024-11-24 04:57:00 | NOAA-21 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e2e2fcbe-23b5-3054-8a2f-7b61cc4a3569 | -23.47042 | -47.51748 | 2024-11-24 04:57:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 76e5b100-64f4-3827-bacb-15dcd67f126d | -20.22679 | -55.97168 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 18fe98c2-73d2-3c44-800e-3e0d844a3f34 | -20.72211 | -53.54387 | 2024-11-24 04:57:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b240f741-2f81-36c9-97bf-5dcad2cf62e6 | -20.23399 | -55.96917 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9e0127a0-8e91-3542-a683-55e87d4c1a70 | -23.59541 | -47.43978 | 2024-11-24 04:57:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca0bf1a6-4c74-3ce3-82aa-6485bcde6d8c | -20.22736 | -55.96801 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 89ec04e9-46a6-336d-a2b0-9666110f6afb | -23.07116 | -47.42692 | 2024-11-24 04:57:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 34548a3d-a549-378e-a1ef-f06d936b6d53 | -20.42536 | -55.29786 | 2024-11-24 04:57:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d41d863a-177e-3a08-820d-2b7a588817c0 | -23.00646 | -46.59932 | 2024-11-24 04:57:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d9b2af12-c8ad-3138-89c1-2a3de4c8a412 | -23.47181 | -47.51606 | 2024-11-24 04:57:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3282c53-d9ee-3648-b8f4-5d934233d79c | -21.22605 | -50.4712 | 2024-11-24 04:57:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b872b87-dfaa-3346-bf45-85355d23baca | -23.47149 | -47.51961 | 2024-11-24 04:57:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c5360c61-75c0-3570-bdd0-c562158ef9ad | -23.00723 | -46.5993 | 2024-11-24 04:57:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f3494d94-9598-3645-87a9-7fd7478519cc | -20.72153 | -53.54806 | 2024-11-24 04:57:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df721084-e7c6-3955-98fa-c3b23a4f4373 | -22.17244 | -55.73302 | 2024-11-24 04:57:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c86deb9a-8f8e-389d-9e5c-cc3eaa24e23d | -20.22839 | -55.98326 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 090a7ce2-c934-3a46-a053-d548ed9ef1d0 | -24.80928 | -51.901 | 2024-11-24 04:57:00 | NOAA-21 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67d78b20-678f-3256-9065-c0cef81f2f87 | -23.07468 | -49.80658 | 2024-11-24 04:57:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c05301ff-a28c-3f4b-a274-e25e1ba2a2f8 | -20.23067 | -55.96859 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 40aee8f3-474f-3edc-9249-fddfec0e0a68 | -20.23456 | -55.9655 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| adf87d97-1d79-35ca-9c2f-308e8f7ac75e | -21.32138 | -55.94793 | 2024-11-24 04:57:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4b62d9e-0f71-3fd9-a099-eb3bf8e1dabc | -21.32081 | -55.95163 | 2024-11-24 04:57:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b66ace3c-d17e-374d-a40a-f972826af4bd | -23.07147 | -47.42357 | 2024-11-24 04:57:00 | NOAA-21 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 566975d6-5eac-3e41-8865-c5c93585732f | -20.22622 | -55.97535 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 17f1f446-b254-363c-99a6-f24fa7751329 | -20.22451 | -55.98635 | 2024-11-24 04:57:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 425fbb57-c17f-3eab-985f-c8d6c6535d60 | -27.43303 | -53.9614 | 2024-11-24 04:57:00 | NOAA-21 | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9656688c-b2b5-3e12-86a4-63116d8c4aa7 | -21.31806 | -55.94734 | 2024-11-24 04:57:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7355e7c7-58ee-37c1-b253-d81d1c16c9ab | -28.14618 | -55.59383 | 2024-11-24 04:59:00 | NOAA-21 | GARRUCHOS | RIO GRANDE DO SUL | Brasil | 4308656 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| dcbbea12-bfd1-3a87-ae68-2b388db78b92 | -6.2744 | -35.1686 | 2024-11-24 05:00:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| b298b171-a575-30d0-89eb-4c221eb6e980 | -6.2557 | -35.1434 | 2024-11-24 05:00:00 | GOES-16 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| 816112a5-2115-30f5-b1c1-6bc0a94c90f3 | -6.2553 | -35.1708 | 2024-11-24 05:00:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 153.4 |
| 832a8688-9882-3663-a72f-2222a21032ac | -3.0355 | -49.4476 | 2024-11-24 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5578b4be-40e9-3d9a-80e7-f9b326d2f7d4 | -3.5159 | -53.8132 | 2024-11-24 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5a989c60-8155-3f81-8004-349e9d547f6a | -3.5159 | -53.8132 | 2024-11-24 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a2c9edb0-32a0-3025-8c3d-eeb97c5a6411 | -0.25766 | -51.63315 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 572c3348-6242-36b4-9e55-5f8d7d046d13 | -3.67929 | -50.11978 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55221fe9-cb72-301e-8629-8af6b08dc027 | -3.13311 | -52.98532 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b3d4dc9-76d6-35a3-a13e-0b623b4ef2b0 | -1.42453 | -53.38135 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c0a2e25-daeb-325a-a5e2-a4f47f4647eb | -2.61874 | -54.25772 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0adc64d-a2a2-3f8a-a48e-bc582bd46462 | -2.00556 | -56.41651 | 2024-11-24 05:14:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46ba467c-3f32-3a8d-9fd8-3c1973423ec8 | -3.04853 | -52.75851 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0f9fa15-7ecf-3177-9fdd-4cebeb1698a6 | -2.56073 | -54.33192 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5bd78b4-3122-34bb-b627-c2f845f6d3b6 | -3.38897 | -50.31989 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d1a68e4-10ae-32a9-8e6a-4977643035e7 | -1.11844 | -53.58146 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02df2ff4-3c3b-3946-96c8-9ac913dce063 | -0.28277 | -51.61259 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2588e122-d28f-3823-8c02-753bcd039f43 | -1.83666 | -46.64429 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| adf90e82-25cc-3b08-a757-46f847624853 | -1.36748 | -52.54747 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4830f726-46b6-3102-b97d-abfd14d60be6 | -1.95212 | -49.52839 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d1daea-404f-3975-841c-40ecd113a546 | -3.00071 | -52.51284 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b828280d-3f02-3d53-96c3-54ed587c231f | -1.13019 | -53.70674 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ad9e1d2-2894-35c3-9578-1d968b473576 | 0.41321 | -50.85248 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60635433-4f16-311c-ab23-e0d9fe3a5ff9 | -1.21541 | -51.73813 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d879a0bf-fe35-3fe5-a5a0-81745a907c76 | -0.96854 | -51.71424 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbe83ad7-f8c7-3ac0-9345-48ad71716a70 | -2.8221 | -52.95787 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3debab21-6c2b-31bc-8b7d-634be8feabf4 | -1.30085 | -51.73723 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64c6e7ad-6da3-35f7-bd75-febda1471ae1 | -3.18014 | -54.31898 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e62ea73-1a93-3262-b72c-bb5fed59c649 | -3.10508 | -53.97247 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 038cfdb8-b668-33c3-a1fa-ecc5d36bd5b2 | -2.615 | -54.25716 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0e96f1c-f062-388f-8f4b-d92e9d241940 | -0.2492 | -51.57467 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba8dd92e-7b46-3913-bfa4-ba32eb3c5f2b | -2.44978 | -49.09384 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4dcfe37a-2f30-3b77-a859-7c37432327ca | -3.49226 | -52.00512 | 2024-11-24 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1ad9a2-4c66-3552-9a69-7299a2ef89bf | -0.90999 | -51.73542 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bd36709-5585-3b62-a991-0b281d80d88b | -2.20849 | -53.66533 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54a3aa60-5c65-3235-a262-3b9958ba43ca | -1.04329 | -51.74233 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d200e09-f91c-387b-a374-9f856c029a6a | -2.84553 | -53.98796 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88510cdc-5fd2-3195-b6c0-fd5a5a9b97c7 | -1.60494 | -46.88506 | 2024-11-24 05:14:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3aaddfb5-894e-3885-a907-0ca39646c535 | -3.03244 | -49.45539 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84241d97-8ce3-318a-bd73-85da635a0a09 | -1.11695 | -53.40043 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e49246f-f01f-3ab0-a5f0-148ae99101d4 | -2.145 | -50.92204 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c70347cc-2a3f-3660-82c7-d469577bbbc4 | -1.69332 | -52.61503 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d73e65b9-e836-33d3-bd71-ad2bbc846d29 | 0.0488 | -51.7211 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59e4e173-78f6-3ffb-9280-0dff95b3d38a | -2.61861 | -54.25471 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73345725-a75a-301e-9bdd-72f533acdccf | -0.57517 | -51.72738 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d8d3300-30e8-3c12-9720-c9d925e4028e | -2.2178 | -46.38727 | 2024-11-24 05:14:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c15d37ae-a27b-36a3-9aa7-fdd78fcf12fa | -2.24454 | -50.47178 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3169038c-d7fc-3994-abc2-574b07071640 | -1.05452 | -53.1627 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1f06ebd-e8d5-3640-b5a8-a9e7532b145e | -2.1637 | -53.77869 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b0b7f12-375b-3037-96d1-c424b053dfd6 | -3.02355 | -54.05729 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa36928f-e886-331b-9306-7af1554ce4e0 | -1.94428 | -49.52205 | 2024-11-24 05:14:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9033fca-55b6-30ec-abb5-9f859e60eec7 | -2.85653 | -51.27776 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57de7f16-8467-3aba-babf-eeca1678f5e1 | -2.56392 | -54.06158 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0e41698-c6e5-3c36-a261-7824725520a3 | -1.40196 | -54.26019 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README68.md)
