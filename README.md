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
| 7d798f1b-31be-3add-a076-e521b70e18b2 | -8.5933 | -48.0069 | 2026-07-08 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| da5fb4b3-617e-325d-8f3c-c02b8398084f | -12.7562 | -44.4724 | 2026-07-08 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 44fc7a27-3d1c-3811-aca9-47b790c02847 | -6.9326 | -43.7032 | 2026-07-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a4103444-b98b-38c5-bbdb-4bcfc1b15e3f | -5.6701 | -44.3147 | 2026-07-08 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f40978eb-d55b-30bc-a7a2-e262164a2dd6 | -21.8037 | -56.2514 | 2026-07-08 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 811fb109-11e0-3c80-be7d-6b0a2c0c61fa | -9.2258 | -48.5782 | 2026-07-08 00:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 35c6d827-2a8e-35fe-bd46-3f5f733e3cfa | -12.3561 | -47.413 | 2026-07-08 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 327a948a-cf50-323b-9027-5c2d336ef1c7 | -4.3402 | -47.7645 | 2026-07-08 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 75aaffe8-389c-3668-be96-c281ead2e6b5 | -12.7369 | -44.4756 | 2026-07-08 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bc31ba58-055c-31f1-adc0-b0f4207f205a | -21.8033 | -56.2729 | 2026-07-08 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 58be32b0-9bcd-33b3-9c82-5c9faf3bd668 | -9.207 | -48.5801 | 2026-07-08 00:00:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3c68af32-34b2-3b21-a1a3-ad4825d40ac9 | -12.3557 | -47.4354 | 2026-07-08 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 11497af3-9f65-3c3a-b973-170654ac9aa9 | -8.6121 | -48.0051 | 2026-07-08 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0dbb9250-6f5e-353e-9700-709863b1976f | -12.7373 | -44.4521 | 2026-07-08 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 948801df-f8f0-3415-91a5-2a0d3f36d79e | -5.8058 | -43.7975 | 2026-07-08 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e69854da-9133-3bf9-9f2f-3c9fbd12e7bb | -6.4973 | -42.2142 | 2026-07-08 00:00:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 57d62966-e653-36e0-ba4f-4568e236ccfb | -21.0705 | -47.2568 | 2026-07-08 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d838c06e-3748-39c2-881f-9cd69c4f7009 | -6.9514 | -43.7015 | 2026-07-08 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| be841f63-2e8c-341b-9043-2575a9300535 | -21.7827 | -56.2762 | 2026-07-08 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| b7bdffb5-bc52-3ac1-b8a6-3cfce8f429dc | -5.6703 | -44.2917 | 2026-07-08 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5d173f47-8200-38e2-b93c-8de9e7edf202 | -12.7566 | -44.449 | 2026-07-08 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 30d3ea51-7b9c-38e2-9a11-4552de5eac5f | -6.4973 | -42.2142 | 2026-07-08 00:10:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| dc20106b-3bb0-36b4-89ca-3b9e47eba4d4 | -8.6121 | -48.0051 | 2026-07-08 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b7809f32-13d4-381e-92a6-5fc1a5786808 | -8.5933 | -48.0069 | 2026-07-08 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3dda6a03-2e58-3b48-803f-9bbb2415025c | -12.7373 | -44.4521 | 2026-07-08 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 042aef78-5249-39e7-916c-43c9aa82ec3f | -12.7566 | -44.449 | 2026-07-08 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 234.2 |
| e4d59aac-1192-3052-928b-738a17811042 | -9.2258 | -48.5782 | 2026-07-08 00:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 2a449a8c-84db-3fae-ae2e-b6e595075976 | -5.6701 | -44.3147 | 2026-07-08 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| b39457f5-8f8a-3e7f-a3c1-40be33fa450f | -6.9514 | -43.7015 | 2026-07-08 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3734786e-c752-324f-a05b-732463754d6e | -9.207 | -48.5801 | 2026-07-08 00:10:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| fb1f2525-8720-3812-acc1-6b632b966c76 | -13.9589 | -45.2251 | 2026-07-08 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 7ca58385-9872-38fe-9075-025eaa8928e4 | -21.8037 | -56.2514 | 2026-07-08 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 15b68442-fb69-30f1-8eed-8237a12e43a2 | -12.7562 | -44.4724 | 2026-07-08 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 481ca246-8474-3415-bcf0-a05d5ff968ed | -21.7827 | -56.2762 | 2026-07-08 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 47.2 |
| cc8a4860-6d6e-319e-be4d-37110a189cb6 | -6.9326 | -43.7032 | 2026-07-08 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8ef3aa2b-9611-3f18-b1f8-b7259003601a | -21.8033 | -56.2729 | 2026-07-08 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 79b91a00-4e9f-3f22-a66c-54eb9a45cbfd | -12.3561 | -47.413 | 2026-07-08 00:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c5937f17-44a6-3867-b772-2604d16c2a31 | -9.2258 | -48.5782 | 2026-07-08 00:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3d1095ee-c42e-353e-9140-43bc2bd62996 | -12.3561 | -47.413 | 2026-07-08 00:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| a12c85c8-1ec8-3990-ab2d-91bbc067b0f9 | -12.7369 | -44.4756 | 2026-07-08 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ed2d4cda-18c8-3102-a66d-81a2773a211a | -8.5933 | -48.0069 | 2026-07-08 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 08cf1266-a283-3cd5-8fff-661bf95b0a89 | -21.8037 | -56.2514 | 2026-07-08 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b55265cf-e7a9-3a69-824c-0b840e7a7654 | -12.7562 | -44.4724 | 2026-07-08 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1f4a5cae-95cf-3da7-8015-3356605fab32 | -6.9326 | -43.7032 | 2026-07-08 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6f968771-7099-3f0d-8f7d-79726bf3b511 | -12.7566 | -44.449 | 2026-07-08 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| ad1299f6-a1b0-3123-9fa8-8c7603f88591 | -9.207 | -48.5801 | 2026-07-08 00:20:00 | GOES-19 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ab8cf98c-0b99-3450-a434-a4b28f12677e | -5.8058 | -43.7975 | 2026-07-08 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9911f686-ef43-3729-9f40-0f2031bac0dd | -6.4973 | -42.2142 | 2026-07-08 00:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| ddf81251-89a8-3903-8458-4bde22fac67e | -21.8033 | -56.2729 | 2026-07-08 00:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 308bb88d-4741-3e1e-b2de-05b47bbe1094 | -12.7373 | -44.4521 | 2026-07-08 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 8a42086e-76e0-3a68-9ae6-9600765ec770 | -12.7571 | -44.4255 | 2026-07-08 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| fb175f79-46df-397d-9f3d-7b827a76d14a | -5.6701 | -44.3147 | 2026-07-08 00:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f3040179-adc6-3f1d-bf97-ddccc6172bcf | -5.797 | -43.780602 | 2026-07-08 00:27:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2585115-66fa-348a-9a7e-5075cf458638 | -23.1555 | -51.667198 | 2026-07-08 00:27:00 | METOP-B | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61e082b7-b9f9-3e96-afa5-b0ca66817207 | -20.1141 | -53.330601 | 2026-07-08 00:27:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe05017-e843-363e-aa74-0d87936b54a6 | -1.8228 | -54.4762 | 2026-07-08 00:27:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2659ab78-998e-3e84-aaab-5e86f58b5494 | -13.2795 | -54.402302 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f585b480-70e6-3171-a489-817442417ae4 | -9.3658 | -48.806 | 2026-07-08 00:27:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 628314ef-64df-3f89-b17d-c12ce401f20e | -23.157101 | -51.675201 | 2026-07-08 00:27:00 | METOP-B | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f19750e-34d5-344c-8b32-879c32b51b95 | -9.3035 | -51.915901 | 2026-07-08 00:27:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa1d3c6-3815-3cb1-acab-98a995ffbcc0 | -21.7883 | -56.2519 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 93467f14-b257-3f2b-920c-a485266b4c59 | -21.062099 | -47.236198 | 2026-07-08 00:27:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a2561bd2-cb7c-300a-a671-84b8a91f722a | -9.3666 | -44.7043 | 2026-07-08 00:27:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 321df5fb-c6ef-34b0-a712-10a973cc73e1 | -1.8212 | -54.469398 | 2026-07-08 00:27:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92e87e8-8299-3108-9e02-febab9d285cb | -12.3614 | -47.424 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fdb8b2f-7d1b-3a03-ba81-665387341834 | -13.4767 | -49.909599 | 2026-07-08 00:27:00 | METOP-B | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab5b2acc-01fa-3558-b6b3-8bff0a00a7e1 | -6.9123 | -43.690701 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe079635-61aa-34a6-b123-4f2e81b82434 | -12.8434 | -44.372002 | 2026-07-08 00:27:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 35d4c504-a73e-3bf2-bf37-98e76ff7c894 | -8.5954 | -47.998199 | 2026-07-08 00:27:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87d21da3-abc7-341b-ab62-ffdd7b61a3fa | -12.3516 | -47.426399 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 429a7910-17e3-3c79-b41e-6980231f1341 | -5.6581 | -44.297401 | 2026-07-08 00:27:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20fd72ce-3eb0-3dd6-9f7c-f797d6c93cf0 | -13.2893 | -54.4002 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b43d639-240d-3215-a3a3-3ca7ea1b4b54 | -6.4312 | -55.784401 | 2026-07-08 00:27:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d0d0aff-5913-3a36-aa76-02efe3ffce8b | -8.5882 | -48.011101 | 2026-07-08 00:27:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 780855fd-d6f0-3731-baa2-c9902e0e933f | -11.3235 | -54.472301 | 2026-07-08 00:27:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0db6052-5a51-36e8-8b2e-2cc06d8ffaf4 | -13.9541 | -45.201801 | 2026-07-08 00:27:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea096d51-e096-31df-b175-ebd3b2950c20 | -18.0856 | -54.019199 | 2026-07-08 00:27:00 | METOP-B | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0e0c43-1b0c-3233-b2da-498f2d926e92 | -8.1219 | -47.101898 | 2026-07-08 00:27:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb677dc-307b-3c77-85a0-fa0646dfa6ed | -6.9316 | -43.685799 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6df9d99c-512c-30dd-a582-e03dcbed099f | -7.6394 | -50.023102 | 2026-07-08 00:27:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb62d60-6b95-3b25-94d0-cc96ff28cba4 | -14.6011 | -52.058201 | 2026-07-08 00:27:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9b3a83-e05f-3838-bb35-263827ab70bf | -7.6375 | -50.014702 | 2026-07-08 00:27:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59f2a955-3cb7-304b-beb5-91325a59c9a4 | -21.8078 | -56.248001 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| edcb19f9-af98-3a89-81ea-4f352f952222 | -21.773399 | -56.2817 | 2026-07-08 00:27:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 92921fd7-b7f3-317a-b0c4-37b4b66c2eee | -6.4812 | -42.222301 | 2026-07-08 00:27:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7455eee4-d872-33c2-89c7-12a72bb8baf7 | -9.2249 | -48.560398 | 2026-07-08 00:27:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dff40d5-9197-3aeb-be9a-64affb0d4ed1 | -17.5392 | -53.997799 | 2026-07-08 00:27:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a7995322-4bca-3184-b267-010fc0b4835a | -17.2766 | -50.0061 | 2026-07-08 00:27:00 | METOP-B | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 65b8f2ee-69f1-3d0f-9fe0-c2cec992bc0f | -8.5857 | -48.000599 | 2026-07-08 00:27:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a0fb5af-11f6-3bf1-b713-35e3d29d8cc3 | -17.540899 | -54.006199 | 2026-07-08 00:27:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ce9d767a-bdcd-3af9-aa77-f14aea5aa5bc | -8.119 | -47.0896 | 2026-07-08 00:27:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb2b5e5a-4268-34e5-950e-b0e4f691147b | -19.660601 | -50.862202 | 2026-07-08 00:27:00 | METOP-B | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e41695e1-face-3eec-aa13-9bc39bf3d820 | -21.052299 | -47.2388 | 2026-07-08 00:27:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82e69b5d-fc03-34d2-9781-98035f46cf58 | -15.0842 | -49.447399 | 2026-07-08 00:27:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8424370a-ff3e-394e-9ab0-04a256503689 | -12.3565 | -47.4035 | 2026-07-08 00:27:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64edb625-9a5c-340f-b9fd-7f78e09fe268 | -13.5381 | -52.934898 | 2026-07-08 00:27:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a24b4b2a-0016-3935-b527-03716f84ae1e | -11.0373 | -45.817299 | 2026-07-08 00:27:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da109aa5-2916-3fb4-a006-1503724e5386 | -13.5366 | -52.9277 | 2026-07-08 00:27:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 738a6dba-1125-33b4-b19d-ac109c099699 | -6.922 | -43.688202 | 2026-07-08 00:27:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 71b963f7-a076-3925-b037-40cf0324ea40 | -13.291 | -54.408001 | 2026-07-08 00:27:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
