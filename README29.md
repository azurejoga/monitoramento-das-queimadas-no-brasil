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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29b565bd-f31f-3f29-8463-16b26e6b93e0 | -1.1836 | -53.4956 | 2024-10-28 03:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 8d2653f9-59b9-3156-ba39-9d2bf31fac5d | -2.2662 | -53.8027 | 2024-10-28 03:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d911bbab-cd0f-37f6-9556-1d07bbbc3f84 | -2.2662 | -53.7825 | 2024-10-28 03:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 01e53438-4de3-346b-aeff-25d5265bff35 | -2.2846 | -53.7822 | 2024-10-28 03:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 50495b87-e75c-3e47-9188-31d06b7c5bde | -2.5127 | -51.1821 | 2024-10-28 03:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f30a1cc8-74be-3404-94ee-9c9e4c9e2f05 | -2.6399 | -51.7374 | 2024-10-28 03:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a15c6503-3f1b-3cbf-a45a-dafc5a4160d3 | -2.833 | -49.2413 | 2024-10-28 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e10c4980-635a-3c5f-911d-9d457a9cbd34 | -2.8515 | -49.2408 | 2024-10-28 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 25d3d0e9-4e93-32fc-9779-894920a4c811 | -2.8699 | -49.2615 | 2024-10-28 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8fb64a90-ae58-35ea-8d3c-da07dc2d3e3b | -2.87 | -49.2402 | 2024-10-28 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0128c18a-7948-35b3-a264-c9dff91583f4 | -2.9761 | -50.4821 | 2024-10-28 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 56f6f372-0b18-335e-847a-65915e026e94 | -3.0317 | -50.4176 | 2024-10-28 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 978b2963-e3b5-39ad-95f8-3e59f4467cdb | -3.0317 | -50.3967 | 2024-10-28 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| a2f6376f-6b47-3cf3-9aac-4579ad09c299 | -3.0501 | -50.4171 | 2024-10-28 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 12162e93-e58e-3254-9d6e-8b885151c676 | -4.1201 | -47.3169 | 2024-10-28 03:45:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 823f1d80-fce9-3351-946c-b026c1ea2336 | -4.1387 | -47.3161 | 2024-10-28 03:45:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8eea236b-9946-37d0-b6f2-a9b983be5f8e | -4.12 | -47.3388 | 2024-10-28 03:45:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 5701ffd0-662d-36c2-a6cd-0782b734f292 | -4.7766 | -46.4022 | 2024-10-28 03:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 59d8765b-1c90-3e18-8348-b950a553955d | -9.1757 | -45.2222 | 2024-10-28 03:45:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b6f98b28-6bc9-36d7-8ec7-bfc5559a6fd5 | -9.1946 | -45.22 | 2024-10-28 03:45:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2ea9bd08-617e-38fc-be57-10a59bd6afca | -29.77411 | -51.41604 | 2024-10-28 03:47:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 425e588b-4480-32b8-9f89-c61902dfdbd4 | -29.76977 | -51.41063 | 2024-10-28 03:47:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| fed83b17-5d4e-3418-adb7-ec4360296457 | -29.76887 | -51.41438 | 2024-10-28 03:47:00 | NPP-375D | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 688df6b7-a0a5-3dcf-8ede-4a1e316ffd48 | -28.58705 | -49.444 | 2024-10-28 03:49:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c51ca1b9-5552-3bc9-b5ed-db5ec2647f6e | -28.58225 | -49.4425 | 2024-10-28 03:49:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d109517-a582-3090-81a1-b3a335abf5a4 | -1.9763 | -52.0804 | 2024-10-28 03:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| be2a657b-546f-3ecf-b412-57256900134b | -2.2662 | -53.8027 | 2024-10-28 03:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ad71525d-377b-386a-8264-ca08987189a4 | -2.2662 | -53.7825 | 2024-10-28 03:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 036bfe02-9220-3aa3-9a37-33e73f733489 | -2.2846 | -53.7822 | 2024-10-28 03:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1b1e6604-1ae2-3835-ae7b-f706939228e8 | -2.5127 | -51.1821 | 2024-10-28 03:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| c7a03bd0-8205-3e1a-901f-c1020cf9b1d1 | -2.5311 | -51.1816 | 2024-10-28 03:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0229b5b3-ac4a-3b5a-8307-073232ef781f | -2.833 | -49.2413 | 2024-10-28 03:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| eae73c92-304c-3e83-9e89-32c024482987 | -2.9761 | -50.4821 | 2024-10-28 03:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 75fff3cf-c4bc-366b-b6ae-ff82a6a2c2ff | -2.8699 | -49.2615 | 2024-10-28 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ce814a79-69f8-3b06-a4d6-3bd65cbbec18 | -2.87 | -49.2402 | 2024-10-28 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 657b5911-ebef-36ad-964a-2055d582af87 | -3.0501 | -50.4171 | 2024-10-28 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 60bd8167-0c9e-3108-ac7b-c2683708eda7 | -3.0317 | -50.4176 | 2024-10-28 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3d22056d-9bbb-307b-8043-e5442c99492b | -4.12 | -47.3388 | 2024-10-28 03:55:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 49a6e783-6f57-3a26-8916-12babc02e17e | -4.1201 | -47.3169 | 2024-10-28 03:55:29 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 21f4b9ca-efa3-30bb-8833-a88c9699bf2b | -2.19616 | -50.7594 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0eff64c-f206-370b-9f31-8645ae7287b0 | -3.5669 | -40.61656 | 2024-10-28 04:04:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9592938-c0eb-3373-868e-23353dbfd1d0 | -3.46148 | -41.26531 | 2024-10-28 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71e19893-d546-3c60-9db2-1990efd46843 | -4.1919 | -40.6829 | 2024-10-28 04:04:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c0e2dc8d-2e52-33c6-9038-0137c64ec13e | -3.74069 | -41.23879 | 2024-10-28 04:04:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29d04f1f-2cc1-304a-a344-9692818d0391 | -3.56224 | -41.40114 | 2024-10-28 04:04:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6d64cf2d-99e5-3585-a175-60f6f6de6bb5 | -3.55893 | -41.40062 | 2024-10-28 04:04:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f33ea870-aba5-3de2-8231-379dd6466afd | -3.56169 | -41.4046 | 2024-10-28 04:04:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d0691c5d-7a45-3f82-bb88-91db0e55d503 | -3.55839 | -41.40408 | 2024-10-28 04:04:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2aa3b039-926e-3c8f-b205-bdfabe9ddaec | -3.43997 | -42.02155 | 2024-10-28 04:04:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8e8ac5c-3de9-3bfa-8f53-0814a02533b1 | -3.3924 | -41.61593 | 2024-10-28 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa5a038c-94fb-38a6-8419-58a1254cfcae | -3.39185 | -41.6194 | 2024-10-28 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f44098b8-b637-36d8-abbc-74289d53197e | -3.39075 | -41.62635 | 2024-10-28 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 733391b5-3031-3333-b0e6-d9067db57ae6 | -3.38743 | -41.62583 | 2024-10-28 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf770cc0-79ff-35ff-b017-e2cb76bbeaa9 | -3.32522 | -41.89156 | 2024-10-28 04:04:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd1ab6ae-d4e6-3b46-a48c-c428c1643baf | -4.3644 | -43.0393 | 2024-10-28 04:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 052001ee-7b88-35b9-b5d3-eab1bec67a46 | -4.36097 | -43.03877 | 2024-10-28 04:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e8cec84-6756-3fe5-9e8c-5546c97e9086 | -4.13063 | -42.16967 | 2024-10-28 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 712b2a71-4073-3725-9096-7508da1a35d6 | -4.12729 | -42.16914 | 2024-10-28 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd91f818-f818-3463-a7bc-85c934e9e97c | -3.86943 | -42.44602 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b5223439-716f-3b79-9870-728e916f0abb | -3.84971 | -42.65818 | 2024-10-28 04:04:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0062105f-9165-38e8-9a3c-6537b1682704 | -3.65316 | -42.43853 | 2024-10-28 04:04:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be52b20d-42fc-3953-90ce-81aa741583c9 | -3.64978 | -42.438 | 2024-10-28 04:04:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7fa31312-f548-3612-a266-851a6567b0d3 | -3.61711 | -42.44763 | 2024-10-28 04:04:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d44071f-10f7-3f44-8819-fef27557ce18 | -3.61654 | -42.45124 | 2024-10-28 04:04:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bda83dfb-4496-398c-99c9-f9816b472a0e | -4.48758 | -42.88117 | 2024-10-28 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 939d407a-b782-3d61-b0ad-b3cf13289afa | -4.487 | -42.88483 | 2024-10-28 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e74be3e7-4b9a-3f7a-ae82-92e064a25c51 | -4.48642 | -42.88849 | 2024-10-28 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 473ba34c-4330-31c5-b956-5e4575c13606 | -4.48302 | -42.88795 | 2024-10-28 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e5fb35d-e1d5-3a8f-ad88-136cceb7ff31 | -4.48244 | -42.89162 | 2024-10-28 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d1b4d62-5b6f-3174-aa7e-c52ed2c11590 | -3.07021 | -44.33562 | 2024-10-28 04:04:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52876ec9-e0c5-3117-bb84-868fdb8f2f95 | -4.25898 | -43.23806 | 2024-10-28 04:04:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d19edd15-a953-33fa-87cf-e7849413d19d | -4.21474 | -43.6254 | 2024-10-28 04:04:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e4af387-0693-3901-aa4c-68e75ae96582 | -4.16283 | -43.26964 | 2024-10-28 04:04:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17a9b77a-ee0e-36e4-9748-9660269a38f4 | -4.15877 | -43.27288 | 2024-10-28 04:04:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e405cb90-6a06-34ac-9c94-4dc7581b78a9 | -4.15509 | -43.7046 | 2024-10-28 04:04:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fefd938e-3b9d-360c-85c7-3e3a6c68cf5d | -4.01246 | -43.64376 | 2024-10-28 04:04:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c2e0972-efea-34f3-9074-36910f769d01 | -4.01183 | -43.64769 | 2024-10-28 04:04:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd3644e-5f15-3385-ac63-0ba2458399ea | -4.00757 | -43.60662 | 2024-10-28 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b987444e-586e-3319-8678-0e5fc9811034 | -3.88108 | -43.192 | 2024-10-28 04:04:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 064cea06-f318-373b-be53-73d0dcabf803 | -3.66732 | -43.62727 | 2024-10-28 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327fc07e-7c59-33cf-89b3-cbff3b8528b9 | -3.66379 | -43.62672 | 2024-10-28 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb1c81d6-15b7-30d7-ab60-242560f40273 | -3.64039 | -43.65965 | 2024-10-28 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0589b490-e421-3cb7-8b2e-b0975a9c4b15 | -3.63976 | -43.66362 | 2024-10-28 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b14a149-9cea-3ef0-b9ff-92077d973377 | -4.17338 | -44.11308 | 2024-10-28 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7546ac8-f271-32be-97a1-e5e5a69ce579 | -4.17045 | -44.10835 | 2024-10-28 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e61469c9-8698-39e1-8e3b-57197da4077f | -4.16979 | -44.1125 | 2024-10-28 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bc18982-e3c0-3e94-9b14-8ea1fb84c796 | -3.96225 | -44.22069 | 2024-10-28 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfc29ff0-b46a-3f05-8241-2ca2fdcba431 | -3.88747 | -44.17236 | 2024-10-28 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| feb05aef-35b8-3141-8d47-bad2d4b246bc | -3.54351 | -44.66136 | 2024-10-28 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9caf6fb3-3a93-3565-b221-373cffadb9da | -3.50593 | -45.80003 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 180c9703-4c05-35c2-9091-56a744ddfd22 | -3.50536 | -45.8035 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 498a852f-6821-3d7f-ad74-308e0777c46d | -3.50479 | -45.80697 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| dd5c531e-fa79-3426-9fab-6a1712d34734 | -3.50193 | -45.79937 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 58622e06-04b4-32ed-9b83-43d9c450bbeb | -3.50136 | -45.80283 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| bd2d6f81-0c0b-3f9b-8d4c-3a2f792971a4 | -3.44814 | -45.89477 | 2024-10-28 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c55cfb14-b3a3-3057-bbc3-ba24cfd4a596 | -3.4471 | -45.42353 | 2024-10-28 04:04:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc98b752-6c16-3b11-98c5-51e57b8eb746 | -3.44468 | -45.89056 | 2024-10-28 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e138fe6-ab86-3786-9785-99e727e225cf | -2.90538 | -45.26952 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d266222-b3b2-308a-a0e0-9093a9cb4d12 | -2.90532 | -45.26749 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03cc5e4a-6c72-3ea9-ad07-c8a2a7ed75cb | -2.90141 | -45.26688 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README30.md)
