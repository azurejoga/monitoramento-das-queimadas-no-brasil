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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62b20c56-51d2-322a-a741-86a9fb55e151 | -4.48118 | -44.73246 | 2024-11-01 04:06:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1fc3b1-8e51-3db9-9a19-2c8b3c6f3cb3 | -4.3762 | -46.01543 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96d18c84-8c17-3feb-8a4b-775bcad7174a | -4.37218 | -46.01461 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c33ee81-b8bc-3113-a75b-883cbaa8fc60 | -4.36815 | -46.01379 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9100cc3f-97d8-3ad1-844e-2e0289c017df | -4.31011 | -45.63383 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 929679dc-ec77-37af-8813-038496747967 | -4.26593 | -45.7527 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 299f0697-066b-35a9-b075-432477522986 | -4.26489 | -45.75098 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f59efa62-f4c8-30bf-b24c-6b9dcde92496 | -4.26365 | -45.74179 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f89246e-9ced-3729-b161-6ab21dd54dfd | -4.16268 | -45.09549 | 2024-11-01 04:06:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c73e75-7ecb-38ce-9588-8991d095273d | -4.08919 | -45.66262 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b196364-7b6e-3e57-9306-a4d224864edc | -4.05037 | -46.07609 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4af4aab9-107f-3e86-ba45-a79e44b99622 | -4.04629 | -46.07538 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 83e09ad6-2ff9-3f6c-853c-4f4e8052adce | -4.04567 | -46.07917 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| aa214b71-57e4-3ce6-8716-de4c76eb5365 | -4.01827 | -44.82375 | 2024-11-01 04:06:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9abedf60-cbe0-32bf-9c11-37e115d33200 | -3.97939 | -45.30716 | 2024-11-01 04:06:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75c26d8c-5506-36bb-95d7-9b56f5ed9d9d | -3.90383 | -44.93578 | 2024-11-01 04:06:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d239b77b-d364-3c61-986e-a18adf5ec9d8 | -3.71612 | -46.01189 | 2024-11-01 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc997ac-f5b4-35bb-952e-dbf20a74ae11 | -5.42507 | -46.36009 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6c4c68b-97a6-3957-b915-8e28590ed5d6 | -5.42448 | -46.36362 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fd96d9e-4b57-3f16-9f99-32e0b43195c1 | -5.33951 | -45.1086 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57d386ad-cda8-38c0-81da-79a89292c11f | -5.33931 | -45.11079 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a4c77f-cb8a-398b-9c8a-857598a572c4 | -5.33572 | -45.10802 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 995e3d6e-f342-3375-aa3f-f9460745b418 | -5.33552 | -45.1102 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70ba8a31-9bda-32c9-b7be-7898d042d6a1 | -5.33497 | -45.11254 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e839d8c5-7795-3326-a185-84c9af25bcff | -5.28802 | -45.13985 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4ce7837-6d18-3b33-9391-d613e6de7667 | -5.24473 | -45.8683 | 2024-11-01 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b49acc3a-2b50-3624-b926-aac17c601e7d | -5.23354 | -44.90526 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0b141db-1f02-304f-8078-73c165edf96a | -5.21432 | -46.02637 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d45cde09-a7af-322c-84d8-a3732e3e0e5f | -5.15299 | -46.11658 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aefd1eb7-ede4-3010-ade4-39d3e96f1785 | -5.15243 | -46.12 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89aea3ee-d5d3-3778-a845-54db19e0ac1c | -5.12821 | -46.09108 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b58319e5-0a8f-3b2e-8ebd-4c719c1dfa72 | -5.12763 | -46.0946 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d222120e-a4dc-39c0-ba13-986fab32cdf9 | -6.35125 | -46.33858 | 2024-11-01 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f30d170-2a52-3d02-bc4f-1d1cd275d0f0 | -6.29717 | -46.04239 | 2024-11-01 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59b09ab2-885d-3765-90a9-e32629b950ad | -6.05757 | -45.79678 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d87f76b0-0008-30b1-bc98-42d50f1e4540 | -6.05678 | -45.80161 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a760cf3d-9ef4-33c1-8f79-da0c2e5e8e94 | -6.05367 | -45.79613 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f5d7a0d-a54a-3349-bfa6-9509b63be843 | -6.05288 | -45.80099 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b53ba404-f78c-32b3-a5d5-457a1aa71d8c | -6.05126 | -45.81082 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80f05fa4-ea00-379c-a0ac-f5960f19856b | -6.04816 | -45.80531 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f28865d-16eb-3688-bcc2-98b6d9029ff3 | -5.83993 | -46.23898 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df147f4a-d2c7-3818-a2a9-9a3ecf9a9f4a | -5.83871 | -46.44668 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f3722d7-28d4-3d41-8b83-ec72004196c9 | -5.83811 | -46.45031 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dde545fb-3867-3979-94c3-19b7c9d1819e | -5.687 | -46.30704 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b32cd06d-4ec3-3190-bc93-0d45f5dec629 | -5.67962 | -46.32861 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59377ef2-792b-34aa-a951-b9d1111fa4b3 | -5.67927 | -46.32805 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c8722a6-428d-35cc-a6dd-5f27011f41f7 | -5.66705 | -45.20734 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f310b1-beae-34e3-bdd9-7bb6e7700378 | -5.60034 | -46.18133 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbdcb0c2-a21f-3d9b-9590-94c99e517c68 | -5.59989 | -46.4071 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bffe235-7ca9-30b5-b6d0-0de9bf4a5d68 | -5.59973 | -46.1849 | 2024-11-01 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dccaef92-536e-312b-bcee-03963fa88794 | -5.59399 | -45.20751 | 2024-11-01 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7ff9f345-5210-3257-a91a-fd61fe0d9e86 | -7.56112 | -45.53387 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06000da7-67be-3125-9415-46503aaefded | -7.55889 | -45.52415 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d211d913-5ce5-37ef-b356-78ae4ff14a99 | -7.55813 | -45.52867 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48c55931-d78c-3adc-9629-55018980359d | -7.55736 | -45.53321 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cc317e6-ad1f-38aa-b03b-39bee54cae73 | -7.5559 | -45.519 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55fd10e0-568e-31a4-a4b7-9bfc28095222 | -7.55514 | -45.52351 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 349a247e-10f4-3b93-9ae0-8326e33750a8 | -7.55438 | -45.52803 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27d8545-c982-3b9a-b34e-529e3029a126 | -7.55361 | -45.53256 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d54c7f86-fe1a-3816-81a7-eaf2b2c503cb | -7.55215 | -45.51837 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 313bcb69-1d24-3e7e-ba9e-9d46c3d57946 | -7.55139 | -45.52288 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9886d1f0-f5ec-3659-adbe-a46294dc7a26 | -7.55062 | -45.5274 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f10e9b39-f957-3681-aebd-f119d78fa71a | -7.40899 | -45.56516 | 2024-11-01 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9daaa0e9-1de4-3bb6-87cf-c43d343f191f | -7.40824 | -45.56974 | 2024-11-01 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f5b708-c550-3200-bd8a-7edca2eadd04 | -7.28401 | -45.41077 | 2024-11-01 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07bbad95-34fe-3b38-bded-76aba8b8f0a7 | -7.28326 | -45.41528 | 2024-11-01 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c68fca-e8be-3c3a-87f5-46d843f1b24e | -7.23194 | -45.77098 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd0e433-d054-3032-a793-69044edf8dbc | -7.23116 | -45.77567 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94b81960-a5c7-31f7-99fa-bb62a8cfa189 | -7.23038 | -45.78035 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff22c085-fd2c-383a-b6c6-784c629014f2 | -7.22812 | -45.77032 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5583133-d90a-3884-a683-034202b381c1 | -7.22733 | -45.77501 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d27f779a-d22e-3820-8755-cfa3c6b8c95d | -7.22655 | -45.77971 | 2024-11-01 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61f685aa-0d0d-39f0-b176-d8aab9d57c5a | -7.18277 | -46.32238 | 2024-11-01 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdd996b7-530e-334f-b797-e95f054332e0 | -7.18191 | -46.32739 | 2024-11-01 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61360c44-1b12-35cf-adff-474b3d98e68a | -7.18108 | -46.31971 | 2024-11-01 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0274b59a-9cdc-3605-b65b-368988971abd | -7.18026 | -46.3247 | 2024-11-01 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4bbed71-cf57-3661-8078-e8e103c02a02 | -7.17942 | -46.32977 | 2024-11-01 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a54890-12bd-36da-be06-1c3c2ba610ee | -6.72706 | -46.35236 | 2024-11-01 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de204a30-9b96-30fd-8442-764411da8910 | -2.00991 | -46.3821 | 2024-11-01 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dda99ad-5b40-34bc-a8e9-45e0c8cc4f0c | -1.96662 | -46.42273 | 2024-11-01 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 354f5aa1-df5d-3b11-8687-c0af18e7d319 | -1.96597 | -46.42685 | 2024-11-01 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db5683e-c512-3ab6-80ba-8fc471dcca99 | -1.7393 | -46.71796 | 2024-11-01 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd17587e-25f1-3dcd-9904-01edc803d52c | -1.73675 | -46.71519 | 2024-11-01 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c46e4beb-2313-3e75-93c6-528f8f78a501 | -2.07869 | -47.1307 | 2024-11-01 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53a0c49d-2ac2-38c3-a192-4a48a6c99ff2 | -2.07417 | -47.12994 | 2024-11-01 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 28d1076e-c6fc-39cb-8558-0fca57d8d20f | -1.55267 | -46.26059 | 2024-11-01 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cad10cf8-f073-36ef-bd7e-0e179f375f36 | -2.92538 | -46.77629 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa515337-fd79-38a8-acc7-9c973231f8fa | -2.92469 | -46.78048 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 284f7a4b-012a-3f45-936c-515fe5fbebb3 | -2.67977 | -46.73567 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61df83b5-512d-3a97-8065-fe2913384de6 | -2.67911 | -46.73985 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5506f0d-8331-3287-a964-576cc2dd425b | -2.67673 | -46.72668 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c209efc-d31b-3852-aad4-0691dfe9b8c7 | -2.67607 | -46.73085 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06956af5-788d-36c4-abce-1278e62bf379 | -2.6754 | -46.735 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94300994-de77-3c4d-8682-6379ceff4f60 | -2.42342 | -46.71047 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e01da793-e8f1-31aa-8ff4-fb19cced9734 | -2.42111 | -46.69709 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fbbd47c-61ea-3935-9efa-19a6cf071c56 | -2.41905 | -46.70972 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 124e0017-f780-35ae-a807-0742862b674d | -2.41674 | -46.69636 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88ca0a9a-9718-3f1a-94be-d20d667aaa9a | -2.41237 | -46.69563 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00188ccf-b0b3-3f70-8c6c-f38597c4167b | -2.40993 | -46.46697 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a63616c-be2a-303a-b5f9-084332767ef9 | -2.40823 | -46.46735 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
