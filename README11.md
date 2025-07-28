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
| 862058be-34b8-37c1-b585-a4dc47c54beb | -7.29564 | -43.07793 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a901d43d-d261-3b8f-abef-25db0f10e8b0 | -10.54174 | -50.24476 | 2025-07-28 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7fea1f2e-31e5-36bb-8377-fdb9a7f3b2f4 | -7.74908 | -51.11048 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 43de1767-2577-3c46-a979-47314f82a093 | -6.90411 | -52.86492 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8781cc74-ba5c-3b72-a6fe-34c5d96fcaf0 | -6.26104 | -42.8376 | 2025-07-28 04:40:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6bcba67c-b5a9-3610-b52d-85c257a1575e | -6.40691 | -53.35863 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b989faf-cb32-337f-9e14-c187fdffa8c4 | -6.70887 | -43.07537 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc8ace8-7bf4-3699-af88-a59a858752bf | -6.54234 | -56.19279 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4386e01-e625-3611-b3b2-97cc37204a13 | -7.10194 | -44.93205 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9794464c-a354-3b87-a693-16a88b53da66 | -6.2578 | -44.9697 | 2025-07-28 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f022eba-ce47-34d1-8c38-144cbae4f199 | -6.12058 | -43.16081 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e398339-4356-3eca-a777-b06aadad894e | -9.64038 | -48.28411 | 2025-07-28 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bec9203-0882-3852-9fff-a5b355d1afa2 | -7.42217 | -44.71069 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c72eac79-4da6-3dd9-96b3-de24659b76f6 | -7.13014 | -44.68646 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e9d3dec-dbd8-35eb-a0a4-f13cae4d1b62 | -7.74517 | -51.11347 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3d3a111-5ee7-38c4-a048-e370c0687418 | -6.01875 | -44.06791 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b4645db-20ac-34bd-914f-91a288232866 | -6.24014 | -43.70814 | 2025-07-28 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52490543-f606-31e8-8115-40f0fa8667c4 | -7.80844 | -50.77939 | 2025-07-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2fd289e-5317-32f0-9432-1cf8cd09c01c | -7.11112 | -44.91334 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a082636-b1e5-39d0-89dc-1a0efca09202 | -13.13978 | -47.33857 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1487b35f-478b-3410-82dd-fc009736d119 | -10.71698 | -49.48336 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e06a70bf-df7b-3120-943b-944d97b6540a | -6.40319 | -53.35805 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d27a2d5-33e4-3527-a452-eb2bcca087e2 | -8.05437 | -49.9728 | 2025-07-28 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 021385c5-dd21-35ef-83fe-27662fe1368c | -6.23917 | -44.06898 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dead160-3211-3a07-a571-2d7b5d116d18 | -7.35278 | -44.73324 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62c56e58-c331-3b07-b985-c881ed74432b | -6.33826 | -44.35383 | 2025-07-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e0c2843-d749-35ca-9f45-800dd7ba17ee | -6.50121 | -56.20009 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc12e2f8-cba4-3e8d-9496-393dd4744038 | -13.11145 | -47.37715 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6830cd2-2e7a-3987-a2b0-e2628f116a44 | -7.08273 | -44.92452 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fb3d70b4-e43d-399b-abcf-e1b6ba45d196 | -7.53714 | -44.40063 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bd09cfd-42a4-397c-961a-aadbcb246fe5 | -12.67473 | -46.99651 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42f9e77a-7998-38df-a0c6-f182a3e8d521 | -7.29953 | -43.08315 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bf05944-6927-3fc2-b0a4-dc145519f909 | -9.03913 | -45.41484 | 2025-07-28 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9290863b-513f-3417-b734-8b0768240dc6 | -12.15071 | -44.76958 | 2025-07-28 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ea5cd47-892d-3d7b-9ce2-4f52f08df5c3 | -6.54678 | -56.19356 | 2025-07-28 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84edcc4f-f38c-37ba-9cb2-f1722b5c42ec | -7.35171 | -44.71149 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae975fd-049b-356c-b155-78086bbc392f | -9.48431 | -48.31856 | 2025-07-28 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2cae078-c887-337d-acb6-3a435aafd9f8 | -7.08641 | -44.89955 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 202746f3-0550-3f0a-b1b8-fa30273f5ae6 | -6.99154 | -47.08112 | 2025-07-28 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b25b0c7f-6987-31ec-a5cc-b9e5532f6069 | -6.55119 | -41.49984 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14bad660-0817-3fee-940b-aa37d450e720 | -12.71374 | -47.02081 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecce2c3a-2b00-3ed4-97f1-dc33842ca25e | -6.39039 | -43.68803 | 2025-07-28 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddd8b02f-4039-3487-9963-fc606f0d8455 | -7.6951 | -46.04043 | 2025-07-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4721e6d7-2787-3865-8857-f4e6cfb0802b | -6.42238 | -41.14169 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46e92038-490c-38ab-8259-a8611a281d29 | -6.85292 | -43.06334 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb1cdf24-de9b-3117-8e32-06b0884941ac | -9.45077 | -43.19933 | 2025-07-28 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c411a9a-bed0-3e0d-9564-acb768091e4f | -6.47156 | -41.62701 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f66c8751-a183-369e-b649-dba17bb16c6d | -7.91094 | -43.09357 | 2025-07-28 04:40:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 90bfb863-c42d-3a50-9542-4d0f4a8f9f82 | -8.87921 | -48.45218 | 2025-07-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11159baf-4fa4-3d15-ade5-b94d4be86b5e | -7.11067 | -44.92802 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7956243-55c6-3b14-b05d-0a41e7a42bbf | -10.46204 | -47.38274 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4953b4bc-96da-3455-bad6-80c6997961c6 | -6.99172 | -45.61759 | 2025-07-28 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13016e37-0780-3d23-9d3e-2a39baffa526 | -7.56062 | -43.68656 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74e33c47-a9ee-370c-a2e6-b272941a64e5 | -7.50086 | -44.41811 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0171ff8e-5182-31ba-a793-8ded05ce03e1 | -9.92537 | -48.90327 | 2025-07-28 04:40:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34aa22c5-0c67-3d8f-bc79-52f958446667 | -13.11459 | -47.38176 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 666d7ed0-c0d2-394d-91bd-adb72b1665ec | -6.42253 | -44.09068 | 2025-07-28 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b77a3fe7-cd4d-31ab-bab1-664d44b07196 | -9.04925 | -40.24866 | 2025-07-28 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 600c9146-04fc-35f5-acf4-4f37746fc07e | -6.39569 | -43.37569 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd5bd12a-933f-3e1a-9370-41152d7d417f | -9.12602 | -45.86645 | 2025-07-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aba1738-54c7-38b1-9083-8708dcbde39f | -12.70316 | -46.29465 | 2025-07-28 04:40:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbc85e43-b821-3789-9b54-929f156fd543 | -7.21156 | -44.16216 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97732c4c-abaa-3c4d-8297-4a27b8506438 | -10.52318 | -42.55302 | 2025-07-28 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 94620b69-727c-36d7-985b-8e18fc3b3e6d | -6.02452 | -44.05754 | 2025-07-28 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7618b600-e546-3d8a-8a3d-850363dcde84 | -7.5366 | -44.4044 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a779fa5-a40b-3c83-ad73-4c001b03a8c7 | -13.13268 | -47.36156 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5294dd5e-cd70-3fae-abd2-7c68cf95e26e | -13.12768 | -47.36988 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6464ebf5-fbdf-3978-a417-34d3b919e8e0 | -6.63667 | -47.56588 | 2025-07-28 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38158ff2-7b61-33da-8e31-11092e0bdbda | -7.38014 | -43.43765 | 2025-07-28 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 773d02bd-5501-3d47-9f09-473c0c82cff0 | -6.41218 | -41.14027 | 2025-07-28 04:40:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c63266c9-d021-3d33-9ade-c25e7a8df039 | -7.81724 | -44.59242 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0530511-8ce4-301c-9195-8d7906546175 | -7.34772 | -44.70706 | 2025-07-28 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06cbb73a-fc8a-32f8-bc4a-a2072f3b5ee5 | -6.55656 | -41.49777 | 2025-07-28 04:40:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b402253-3246-3cda-a1fd-4e286c983288 | -12.70175 | -47.02387 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90b0377c-0311-3044-b0b8-9cd77394d246 | -12.72258 | -47.01289 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 112f6d11-7fa9-39c9-a243-ba750a303295 | -6.44852 | -53.36081 | 2025-07-28 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2f37c7e-2621-35d7-ac55-2abb21606d4f | -7.54117 | -44.43177 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59c8bee5-24b5-365f-ac1c-e7046be40258 | -6.23586 | -43.7077 | 2025-07-28 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19cb5e73-fa2a-3131-9102-569d1149e790 | -11.35056 | -51.24728 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10692f3e-d29d-3c84-bf41-2222a5590099 | -7.10667 | -44.91602 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4baf95b9-a183-38f6-b4ed-5b720e7a95da | -8.03426 | -46.90535 | 2025-07-28 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9762326-148d-3eda-879f-57ec46b6cd37 | -6.64541 | -43.03882 | 2025-07-28 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 922a6a23-74ff-3421-b9f7-7ae272a2739a | -6.89624 | -52.8679 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6afbbd4-5e0e-316d-b433-d7620e0cf2e1 | -7.66707 | -44.80436 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0f8b4fa-9ad3-3623-b14c-75a15115e1e7 | -7.14535 | -48.20528 | 2025-07-28 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46f5fae5-f969-31df-8971-bd6c476a9e7a | -10.54597 | -49.49327 | 2025-07-28 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 57dbbf4c-fb93-3df4-8558-bc19e0280f4d | -12.6596 | -47.02224 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffb1738e-528c-33de-b15d-c74d5fb8d720 | -10.60555 | -42.92604 | 2025-07-28 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 782f9f64-18ac-3f37-a318-bdaeec7ae8d2 | -6.76224 | -43.00633 | 2025-07-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 015bb5d7-7785-34db-98ab-49368340af67 | -13.11924 | -47.32248 | 2025-07-28 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87d61732-bd43-3c85-9cfe-e08acd544dec | -9.48088 | -48.31804 | 2025-07-28 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09e0d7b6-d19e-39f5-a32b-ae9f02b51a00 | -7.10125 | -44.95424 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f13edc84-4373-33ad-8bb8-f73a70cc709d | -7.41761 | -44.71356 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edaffe1b-4b43-320a-be76-65bd5f10411b | -7.6592 | -44.79584 | 2025-07-28 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a58b468-49ac-3dbe-b4a1-c8f7efec39a5 | -7.81074 | -50.22504 | 2025-07-28 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bda5c0c-d9a8-3650-b5c8-5e7e99f4ac70 | -11.93639 | -44.85871 | 2025-07-28 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dbd1d08-078b-32ac-a0bf-ae8354de7784 | -7.10019 | -44.93302 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24330463-fde8-3b77-9a4f-883b921d08f2 | -6.89263 | -52.86735 | 2025-07-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 414f189d-0c56-3be0-8d5d-4f637f38386f | -7.21217 | -44.16464 | 2025-07-28 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5dc6ecb5-d18a-31d5-a3c1-de2a651f4cf5 | -12.72646 | -46.27179 | 2025-07-28 04:40:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
