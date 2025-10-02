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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f62a669-e9bc-32d8-a96a-cd71de19bb49 | -8.6035 | -50.3952 | 2025-10-02 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9946e3be-c8ff-3b83-aaa1-07b572b0b83e | -22.5735 | -46.7755 | 2025-10-02 00:30:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.4 |
| 0cf234e9-5ac5-3e15-9f5f-cc979e72073c | -14.426 | -46.0919 | 2025-10-02 00:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e4dd94fb-3ee7-3652-a86b-4659fc0eee4f | -5.9856 | -44.6118 | 2025-10-02 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 06462e09-ff07-3967-a456-22132a6396d6 | -5.9858 | -44.589 | 2025-10-02 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| e027e2fb-5274-3d0b-b7c7-3130979e4f28 | -15.2547 | -49.2883 | 2025-10-02 00:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| fa64d41c-efea-3e26-a86f-7864afb26afa | -7.7755 | -42.5152 | 2025-10-02 00:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| ce3acc1b-62ec-3f63-8d6b-a7e509c2331e | -10.8428 | -46.6064 | 2025-10-02 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c2376fc7-b13f-3061-91c9-0776fd3c937b | -11.175 | -47.2581 | 2025-10-02 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c48c4b42-9b64-36d3-ad7f-0b2ff5321fc9 | -21.3995 | -47.2463 | 2025-10-02 00:30:00 | GOES-19 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 981c9383-2536-3b84-b8da-a61f8f310109 | -8.6223 | -50.3936 | 2025-10-02 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 76d3707d-cfb2-36b5-9753-7a0cee7511b6 | -14.4255 | -46.115 | 2025-10-02 00:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| e8d3c529-a311-39bc-ba16-01b89f2059ed | -10.8424 | -46.6289 | 2025-10-02 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f5bd954f-0d7e-3560-a4fb-161190ba9095 | -22.5525 | -46.7811 | 2025-10-02 00:30:00 | GOES-19 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.7 |
| a39b23b2-270a-36b2-a8f2-59801fd85cb4 | -15.5508 | -48.1701 | 2025-10-02 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5c7bdaef-ea4f-3668-845f-aaefe125bcef | -4.8596 | -45.2109 | 2025-10-02 00:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e26e421d-4199-3c17-8f6d-718f72e58f4c | -12.4207 | -54.3536 | 2025-10-02 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9fff9e78-5428-3842-88ca-05363365f885 | -6.7213 | -44.1387 | 2025-10-02 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 429ed0c8-f68c-3529-b0b2-c6383f1745cb | -14.407 | -46.0722 | 2025-10-02 00:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a16487cb-6204-38f0-adb2-7bb75b1054d1 | -5.986 | -44.5661 | 2025-10-02 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c103b5c5-a169-33a9-baa5-da985fbab39f | -18.1317 | -42.387 | 2025-10-02 00:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 032fe66a-6671-3c64-bbb5-3949dcd871f4 | -13.1546 | -47.8345 | 2025-10-02 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7803f73e-9165-39c7-8de7-0dfc2fc8f2ab | -14.4065 | -46.0953 | 2025-10-02 00:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| faa1535d-c2f0-39ad-8aa2-901107b60fd5 | -21.4202 | -47.2412 | 2025-10-02 00:30:00 | GOES-19 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| c34b1a66-6623-3ada-877a-e94d1ac29f92 | -10.8237 | -46.6088 | 2025-10-02 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ca661a08-9ce1-34ea-be99-55833b525612 | -15.2542 | -49.3104 | 2025-10-02 00:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c1ec4283-1e6e-39e9-ac74-1bf64ee99b34 | -9.6511 | -62.8526 | 2025-10-02 00:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ab0e3917-14b3-386c-8b37-09b7594c8091 | -6.2411 | -45.3198 | 2025-10-02 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 751fa909-a10b-38d3-9467-326ea986c5c3 | -13.0119 | -45.1988 | 2025-10-02 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6685ee4e-c580-3dd0-81f2-184cf074286d | -16.0421 | -50.874 | 2025-10-02 00:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2b7c0204-5225-38dd-86aa-1e7e6d232aec | -15.2738 | -49.3073 | 2025-10-02 00:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 051d702d-0baa-3629-bce1-8949470403c3 | -13.0114 | -45.222 | 2025-10-02 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| db3ea2e6-cb65-39cf-9a57-bb13e033c20c | -13.8637 | -51.2517 | 2025-10-02 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0a1f75b1-2189-3c51-93a8-df1e8499bfc7 | -15.2742 | -49.2852 | 2025-10-02 00:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 08337e5d-3db3-38df-866b-de5a19a4e2cb | -8.5748 | -49.6095 | 2025-10-02 00:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4a3a3e8b-fc7e-3087-8c30-1cfda7a4df8b | -6.2408 | -45.3424 | 2025-10-02 00:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 06c01a37-a547-31a2-9749-ed646335c4f7 | -5.9858 | -44.589 | 2025-10-02 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6913d8d4-0d60-38f2-a993-605529bb5f7c | -13.8637 | -51.2517 | 2025-10-02 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a6898623-9c00-39b5-b058-faa54f8aa0f5 | -4.841 | -45.212 | 2025-10-02 00:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4f5ec8d2-5e10-3caa-81ed-4f71a2a28b91 | -8.5748 | -49.6095 | 2025-10-02 00:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 84725f2d-f5ce-3b1e-ba2a-f33dcd443358 | -12.4207 | -54.3536 | 2025-10-02 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 1633d2fc-7ce7-306d-b2a7-6ee6089976a1 | -22.5518 | -46.8053 | 2025-10-02 00:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| e64ad775-3b4a-35cd-851b-d916aeeb0453 | -13.1546 | -47.8345 | 2025-10-02 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 44e43bca-672f-3127-9f20-8eec1e285024 | -14.426 | -46.0919 | 2025-10-02 00:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bfe3dfa2-092a-3135-a182-b7cebae631e2 | -7.7752 | -42.539 | 2025-10-02 00:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 206.4 |
| a781a611-42b9-3030-bb7f-2118eeb5d820 | -7.7944 | -42.5132 | 2025-10-02 00:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| b2393dd7-9f00-31b6-844c-f558dc92f65f | -16.0421 | -50.874 | 2025-10-02 00:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 62eb6551-fed9-34de-9ab5-5f664b362951 | -7.7755 | -42.5152 | 2025-10-02 00:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 34e23a25-02ac-3371-a0cb-5c097d04008f | -6.2408 | -45.3424 | 2025-10-02 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 7fa58d97-b8f6-3986-b899-7cb7dfe0f2ce | -7.7563 | -42.541 | 2025-10-02 00:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| e5907143-7fff-3efd-99fb-b0ef2aa04bfb | -14.2121 | -46.1058 | 2025-10-02 00:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2c3069de-266e-31a1-b48d-a7ea63fcf8e8 | -22.5735 | -46.7755 | 2025-10-02 00:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| 4e451ce7-53f1-3f8b-8ff0-40475738f029 | -5.986 | -44.5661 | 2025-10-02 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5e09c3ee-8663-3079-a49d-66d0c84c5660 | -14.407 | -46.0722 | 2025-10-02 00:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| cca72815-875a-389f-9077-930d9849630e | -15.2547 | -49.2883 | 2025-10-02 00:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f98bdd3e-72f0-348f-96ba-28075e5484ec | -7.7941 | -42.5369 | 2025-10-02 00:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 70f19ff9-ceac-3fde-880c-3ba763ed8d87 | -22.5525 | -46.7811 | 2025-10-02 00:40:00 | GOES-19 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.0 |
| 646ce104-24b5-3054-b948-abba67d40e45 | -12.2777 | -45.3603 | 2025-10-02 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 37ef6088-87eb-34c3-a9dd-8a86b0a85c61 | -6.7213 | -44.1387 | 2025-10-02 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 83239ae3-83a9-3f3a-b3de-b8afb847b7db | -14.4065 | -46.0953 | 2025-10-02 00:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 379f44a1-1877-32bb-a5ca-063b391b21a5 | -6.2411 | -45.3198 | 2025-10-02 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| bda04121-4f18-3635-8153-1827951b1988 | -22.5728 | -46.7997 | 2025-10-02 00:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| 7f0ae28a-e236-3266-971d-fb362473cd41 | -5.8469 | -43.3995 | 2025-10-02 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| e7dc3deb-fc76-30c2-9e2a-b613e1ceaab3 | -6.0046 | -44.5875 | 2025-10-02 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| fb706dac-18db-3b3e-817e-2e3385355850 | -17.5356 | -40.163 | 2025-10-02 00:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 9b03d04c-a54f-3314-8413-5f4981753101 | -8.6223 | -50.3936 | 2025-10-02 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8c6df231-b635-343f-b52e-912226d1f580 | -7.7752 | -42.539 | 2025-10-02 00:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 289.8 |
| f01e0afd-0544-3dd5-ad0e-3f9042338226 | -7.7755 | -42.5152 | 2025-10-02 00:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 163.1 |
| 592eb056-d75a-3e91-b93b-1510935c3fbf | -13.1546 | -47.8345 | 2025-10-02 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1be0a7b9-55b9-327c-baf6-4e5d9c76d6df | -13.8637 | -51.2517 | 2025-10-02 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| facc1a7d-7079-3a71-9317-f17f4f29476b | -14.426 | -46.0919 | 2025-10-02 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d93e5ab7-747c-34eb-b04f-0a5fa637717e | -22.5525 | -46.7811 | 2025-10-02 00:50:00 | GOES-19 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.6 |
| 841255b2-4828-3df6-b214-440371641fa6 | -5.9858 | -44.589 | 2025-10-02 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d2cb78cf-bff2-34d6-8717-da8f18ab921a | -14.9924 | -46.9091 | 2025-10-02 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5f727618-180d-3d30-abdb-8a4f7e9843d6 | -6.2411 | -45.3198 | 2025-10-02 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| f1f72669-413a-3ace-a1ea-321c54886dcb | -5.9671 | -44.5904 | 2025-10-02 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c1d86c28-1b04-384e-8480-3d7bd690fdfc | -5.9856 | -44.6118 | 2025-10-02 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 581f9dfb-4e07-326b-9fd5-f71f5d20acf6 | -6.0048 | -44.5647 | 2025-10-02 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 664fde85-98d7-37a6-9293-d09301218c01 | -12.2777 | -45.3603 | 2025-10-02 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 09ea2742-0800-323c-8fd3-2ef1722657e6 | -22.5518 | -46.8053 | 2025-10-02 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.4 |
| e0e6b68b-f78e-33f6-9346-a5db08932bd2 | -22.5728 | -46.7997 | 2025-10-02 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 88e34198-5b1b-3852-b251-35ba5b52feee | -5.986 | -44.5661 | 2025-10-02 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 70021f77-ef3e-3a46-ad9a-024c07f9c48f | -12.4737 | -47.2621 | 2025-10-02 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 28399c67-9549-3e2e-9b62-e4946f8295ae | -14.9728 | -46.9125 | 2025-10-02 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ec866818-bccd-3c8d-9292-fc71857086f0 | -10.8237 | -46.6088 | 2025-10-02 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 439c9a8e-bd90-3bce-9909-d0f9944a1ff3 | -14.4255 | -46.115 | 2025-10-02 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f3bb8f49-5384-3f63-bfb5-8de7c94c5e72 | -14.4065 | -46.0953 | 2025-10-02 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6b6f8e56-a50a-3cfa-8310-bfa0b0b3ad1f | -14.407 | -46.0722 | 2025-10-02 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 43f25661-8211-3818-97f9-bb82e9f47201 | -6.7213 | -44.1387 | 2025-10-02 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5993c1c9-b02b-39b5-8e7d-6965294cc132 | -6.2408 | -45.3424 | 2025-10-02 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3688aafb-d1fa-33b4-91ee-60bcc5fdcdf6 | -22.5735 | -46.7755 | 2025-10-02 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.8 |
| 6a3a75d9-ba0d-3b39-aab3-720351151270 | -6.6955 | -48.7062 | 2025-10-02 00:50:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a60da2df-d33b-3f67-9539-4cd184274910 | -7.7944 | -42.5132 | 2025-10-02 01:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 5194510a-44c2-30cd-a5fb-f150ea6fe7b3 | -6.2408 | -45.3424 | 2025-10-02 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 164462a6-fa49-3e3e-bac4-f512217535f9 | -10.8424 | -46.6289 | 2025-10-02 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 7c6c7516-8c39-33e2-a04d-528fc61e018f | -6.0046 | -44.5875 | 2025-10-02 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 71545c4c-7f3b-325b-aec0-5ff0718bd66d | -5.9858 | -44.589 | 2025-10-02 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| ce3ea4eb-9e59-3be0-a817-03bea41ad807 | -22.5735 | -46.7755 | 2025-10-02 01:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.0 |
| 997cdcc9-e8f9-310f-8b2a-9f26f5f3716b | -22.5525 | -46.7811 | 2025-10-02 01:00:00 | GOES-19 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.5 |
| 9753280c-42a9-3291-836d-d46575c8263a | -5.986 | -44.5661 | 2025-10-02 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |


[Clique aqui para ver as próximas entradas](README12.md)
