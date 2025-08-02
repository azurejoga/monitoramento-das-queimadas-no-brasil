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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4033caf0-f2ac-38a3-93d2-5d32b7593415 | -29.317 | -54.9958 | 2025-08-02 00:00:00 | GOES-19 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 110.7 |
| 3c39ea34-6c23-3a6a-8f93-6e13147e837c | -3.5083 | -47.212 | 2025-08-02 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 2dff32cc-12ca-37a7-bde1-f95930a01c43 | -10.4574 | -46.9677 | 2025-08-02 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e70017ac-3ce6-3bb3-bb25-269d67c1c857 | -29.295 | -54.9779 | 2025-08-02 00:00:00 | GOES-19 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 77.8 |
| 7783a31e-ac90-3327-bf18-50b602a234a8 | -10.457 | -46.99 | 2025-08-02 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| bdc67acc-4b78-3130-8f54-ad9f241e6eea | -9.4648 | -57.8449 | 2025-08-02 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6d20d375-a1cd-3b11-b2c2-22e34d961cb8 | -29.2943 | -55.0013 | 2025-08-02 00:00:00 | GOES-19 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 175.2 |
| 9238f2a3-7aa8-3170-bfe5-e5509df82a8d | -10.5784 | -45.2792 | 2025-08-02 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1ee1d471-b859-36e7-828e-0568cf693ee5 | -10.369 | -55.3114 | 2025-08-02 00:00:00 | GOES-19 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d1bae61e-8691-3d54-8b2a-f822a5c81e97 | -18.7471 | -42.6749 | 2025-08-02 00:00:00 | GOES-19 | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 33e2e7f8-822f-3a29-b929-7c294c2beaa4 | -10.017 | -44.708 | 2025-08-02 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a57fff31-0008-35b1-b21b-f3ce8a1e2892 | -10.5974 | -45.2767 | 2025-08-02 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9ccf66d6-ba5a-3b5d-b447-7f87396b3618 | -10.5784 | -45.2792 | 2025-08-02 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 976d54f6-60d5-30fc-a099-6004119ff87a | -10.055 | -44.7032 | 2025-08-02 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4edae718-b143-3c6d-baf8-702179afb9d3 | -10.036 | -44.7056 | 2025-08-02 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 02a7cfd2-d63e-3825-b425-3d05bc5fad29 | -10.0357 | -44.7287 | 2025-08-02 00:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 25cc0008-45aa-3801-9320-a064ab27d908 | -29.2943 | -55.0013 | 2025-08-02 00:10:00 | GOES-19 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 100.5 |
| 24643aa6-e9b3-3c94-b56e-e612a3cc171c | -3.5083 | -47.212 | 2025-08-02 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 47518f9f-a951-3621-8ef3-d423a2b3f936 | -29.317 | -54.9958 | 2025-08-02 00:10:00 | GOES-19 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 99.9 |
| ca7a716d-1350-3693-b0a7-6243bb33177c | -10.5787 | -45.2562 | 2025-08-02 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 05839b42-5d78-3ac9-a575-cd08635029a2 | -3.5083 | -47.212 | 2025-08-02 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 47e395f0-8909-3e72-84a1-fa1e64533c03 | -10.5784 | -45.2792 | 2025-08-02 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 36d63ac7-397d-3472-a092-36c40aafb52e | -12.6402 | -44.4913 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9bc54cff-6562-3625-86b1-fa7195f59ca0 | -12.6591 | -44.5117 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 266.4 |
| d75906ee-a190-3241-86aa-26a5f4a04a6a | -12.6784 | -44.5085 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 60a76443-9a0d-3d73-8993-cb93a4f674ba | -12.6595 | -44.4882 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 340.4 |
| ae3aefc3-e4d4-3a40-8af5-8fe6d1e4f4b9 | -10.0357 | -44.7287 | 2025-08-02 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 917dcf6d-5d7d-3f8e-a08f-9f5fead7542e | -12.6789 | -44.4851 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 72c832c0-acb9-3cc9-9856-487434b8cfae | -10.036 | -44.7056 | 2025-08-02 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ff1472c9-9f65-3846-be02-bb213654842a | -12.678 | -44.532 | 2025-08-02 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| db59f2e2-8f38-3aea-a217-8ea417daf68f | -15.0894 | -55.2094 | 2025-08-02 00:39:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bc1eeb8-1d88-397d-9122-fb25e2760dff | -21.6178 | -57.937099 | 2025-08-02 00:39:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 34ea117a-39c0-3e30-835c-78833b768256 | -6.5509 | -51.106098 | 2025-08-02 00:39:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e865375f-166c-3c64-95de-bbb27d2855a8 | -13.6762 | -51.949501 | 2025-08-02 00:39:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bcc73f04-556c-3049-a487-45f23c242c29 | -3.4902 | -47.229099 | 2025-08-02 00:39:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05235ab2-f023-35bb-b0b8-6386439a5d86 | -22.615299 | -50.667801 | 2025-08-02 00:39:00 | METOP-B | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8580877-df63-370e-a4e3-d56713d8ebf1 | -7.9888 | -43.143299 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 44a18529-9346-3c27-87ba-53c7e6fddcb0 | -10.4304 | -46.985901 | 2025-08-02 00:39:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf44c8b8-8f27-3fd3-8e04-7b5bcd81abe6 | -21.526899 | -48.7262 | 2025-08-02 00:39:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07fc14dd-a966-3c93-965c-136a4f8c1de5 | -12.0085 | -44.0261 | 2025-08-02 00:39:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0c633b-a68e-3cbb-8f36-c3bd0bbe8b5e | -10.0085 | -44.6954 | 2025-08-02 00:39:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eab87461-fee0-360d-84bf-3d3bdec79eed | -8.5492 | -51.542198 | 2025-08-02 00:39:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00285262-2f41-31ef-a199-d4df10936f08 | -10.3464 | -55.306 | 2025-08-02 00:39:00 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9a6166-a11a-363e-a6a0-c1f3452a36c1 | -13.9753 | -53.940601 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be7314ac-5fce-33b7-9b0b-c7801bbcc3e2 | -12.6394 | -44.4678 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73b82d91-35b3-3cc5-a30c-80f0a1cb4560 | -10.556 | -45.267601 | 2025-08-02 00:39:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fbcfffd-d5ae-365d-95e7-9d095a7e4db0 | -12.6348 | -44.490002 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f87e22b-34e8-3d1d-8d0c-6851b698b1b0 | -5.545 | -43.6147 | 2025-08-02 00:39:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db2c11c6-2c2d-3a2e-b40d-0b8cb3b7b3cc | -3.486 | -47.2113 | 2025-08-02 00:39:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e312057-5888-371d-a1d6-7e62fa3ba15e | -12.6352 | -44.531399 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c97ea6c3-aca8-31a5-974f-de7e439f72df | -12.6449 | -44.528801 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a03643f1-c3c4-3e7c-bd28-53eb9b7d2125 | -16.677999 | -49.393101 | 2025-08-02 00:39:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7df5aff-3d01-3c46-ba8e-c55ad365b78e | -13.9738 | -53.933498 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26f64276-3771-3853-9d08-1ba49cd8ef93 | -10.0095 | -44.739399 | 2025-08-02 00:39:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d567927c-494c-32dd-86cc-d40f85da8e61 | -10.0042 | -44.7187 | 2025-08-02 00:39:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85142247-a4e4-36b7-a8a4-7592460fd15e | -13.964 | -53.935699 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fd596d4-64cc-3ba7-8b3e-f55e1472c522 | -10.3479 | -55.313202 | 2025-08-02 00:39:00 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30d380ee-119b-3961-977d-29313780cccc | -7.9983 | -43.1408 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b4119f0-f2bb-3f34-9466-9fc55ca5d987 | -8.0079 | -43.138302 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db8c1906-c9d1-35fd-ab02-701f7aa9d43d | -18.3195 | -54.286499 | 2025-08-02 00:39:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8b837389-1d1c-3ea5-8783-ca2a000be1e9 | -13.0297 | -47.434101 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 253f97d7-4b24-3d2e-90d9-f6f895647ca5 | -13.9851 | -53.938301 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad7b3796-1a50-39e7-b924-f57e7ff9d19b | -23.870399 | -51.241699 | 2025-08-02 00:39:00 | METOP-B | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8330f39-3bff-370f-ac60-448259d9bde8 | -18.3179 | -54.278702 | 2025-08-02 00:39:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9c05963a-e0ac-3aba-8b15-5a4edb048914 | -7.9962 | -43.172001 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cbb37721-a57a-3c2b-9cb2-057d4b9639fd | -3.5049 | -52.866798 | 2025-08-02 00:39:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8689f6f3-2de3-36fa-9cf5-5797bc9974f8 | -7.9814 | -43.114498 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 78b41b3d-f052-34ef-aa19-d7f1f120c913 | -18.212601 | -45.1591 | 2025-08-02 00:39:00 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 022f7811-7db4-3b8d-a7a4-21ea80020395 | -8.8894 | -47.3419 | 2025-08-02 00:39:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 860aaeb4-da34-3293-a739-bca38f26c3f7 | -12.6932 | -47.788502 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 595009fd-5656-331a-8c9c-8632173901ed | -22.3412 | -54.980801 | 2025-08-02 00:39:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88be3df0-6360-36ae-bb28-c8ead00f1068 | -11.163 | -51.515202 | 2025-08-02 00:39:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94159a83-26e4-30b8-9a72-ae74f9f3c0b3 | -9.9989 | -44.697899 | 2025-08-02 00:39:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 963d2fa4-a3ce-30c9-9c34-394a9bcb99ad | -10.3448 | -55.298901 | 2025-08-02 00:39:00 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b671fef-82a4-3128-91ba-34a125ec3852 | -13.9655 | -53.942799 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbc8d498-f3a7-3dc2-9a84-6f260008f67c | -8.0005 | -43.109501 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da1efbbe-1a31-37b0-abf1-7faa8c3ef0aa | -25.498899 | -52.846401 | 2025-08-02 00:39:00 | METOP-B | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e49e5cb-db24-3a29-948a-3ea5b79f6f6a | -8.0101 | -43.106998 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 375f3f44-3d6b-3a09-b0a5-6077d8a71b8b | -28.728001 | -50.396999 | 2025-08-02 00:39:00 | METOP-B | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f177fd9-81c9-3c19-923f-9ca17c2ec2e2 | -11.3988 | -56.8545 | 2025-08-02 00:39:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a22aacd4-5cdf-31a6-a78b-40d87846a4c5 | -12.6864 | -47.802799 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4fad6c-eb67-315b-aaac-002fac2bfc8f | -22.3475 | -54.960098 | 2025-08-02 00:39:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8f6a0185-912c-36f9-9661-df1100013986 | -21.5249 | -48.717899 | 2025-08-02 00:39:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6855c96a-fc47-37d7-9cd0-bd2c85a52c69 | -25.4972 | -52.8381 | 2025-08-02 00:39:00 | METOP-B | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0a3ff07-6636-3b30-9199-1c5d65474c6c | -12.6297 | -44.470501 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 514f1be9-feb6-31df-9384-38de6d7bc0b3 | -10.0138 | -44.716202 | 2025-08-02 00:39:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3f88afb-4312-3383-bc5d-a6916d561111 | -15.1008 | -55.215 | 2025-08-02 00:39:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25320b5d-d949-320c-9ebf-adcfc48588bf | -10.4268 | -46.9715 | 2025-08-02 00:39:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39b54334-fd4f-388d-9325-74d3a37e5b8e | -8.0057 | -43.169498 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2aef7524-02da-3f6c-8dad-f3b36154aa92 | -6.5488 | -51.097099 | 2025-08-02 00:39:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79ab357-f9f9-38d5-8c8c-ccc73e38754a | -13.9867 | -53.9454 | 2025-08-02 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e5d2fe6-dbb9-3bd4-a0f5-fcd6170873c0 | -12.6441 | -48.094799 | 2025-08-02 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5155c081-dcdc-3e21-946f-130677906391 | -18.216299 | -45.173401 | 2025-08-02 00:39:00 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 483b8736-7744-3223-b589-41dd88177b9d | -8.0197 | -43.1045 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8aeb406-d0a2-3dc5-bf50-fd00ffe50a66 | -25.083 | -49.511501 | 2025-08-02 00:39:00 | METOP-B | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1fb9a10a-7bcd-374b-a665-95ec09ddb489 | -7.9909 | -43.112 | 2025-08-02 00:39:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96fa4336-4a42-3a10-bda0-9a968eb0ca44 | -15.0992 | -55.207298 | 2025-08-02 00:39:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 929e6dd0-1a41-3811-8a24-96f9d972ad8f | -11.2083 | -48.9048 | 2025-08-02 00:39:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba1ae9f-54a5-36c3-815a-3c1b859fe6a6 | -12.6251 | -44.492599 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85b0ac0e-40aa-3e4f-b6f0-4df5683e2144 | -12.6302 | -44.512001 | 2025-08-02 00:39:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
