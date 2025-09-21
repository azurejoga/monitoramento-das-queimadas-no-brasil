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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f3b34b-d7b5-34a2-a8d8-3e3e76bca275 | -6.94681 | -44.76461 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b3a8882-aa68-38c7-89e5-47e2427e1272 | -2.73584 | -49.55132 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7bf975f-c25e-3ea1-8ff8-3126b7dd4e05 | -3.60079 | -47.52729 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13fa27de-9c0f-3b0e-be25-e6ae970037cd | -3.0863 | -51.39498 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a310e4b9-9395-3b13-9dca-c57c4db2a4dc | -3.60139 | -47.52324 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dab1bb67-abf0-3ec4-99b1-d0b18331c3bf | -3.65109 | -54.06252 | 2025-09-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7db2450-33eb-3d6b-b70d-f7744bdae65c | -2.69501 | -59.42441 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ce528fa-9c54-3923-9db9-f816dea1afaa | -5.34523 | -45.00885 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d59c035-96e7-3426-9555-15192acb87dd | -5.75467 | -44.203 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aeb68e41-847a-3791-9477-f7a038791afa | -4.9681 | -49.50469 | 2025-09-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cd2112d-661a-3a20-8584-483b6b4ce0e0 | -5.56598 | -51.7977 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b02f0ef7-fc02-35d1-a5f2-944242044086 | -5.52561 | -43.86198 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1635fa47-3e01-3727-8a9c-c05776d84052 | -2.74109 | -49.55011 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e5afe0-fef8-3b0f-b3b0-93fd10b22a3f | 1.4007 | -56.07331 | 2025-09-21 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc85f493-611e-3443-a161-a2d3f96611b3 | -3.36778 | -50.39728 | 2025-09-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9389e4f-3544-3c71-aaea-8a42efece4d0 | -7.91863 | -44.11014 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d5ad6c4-5c72-32e8-992a-b2d322bf68a3 | -2.74028 | -49.54742 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9db22c92-927d-3d31-9b96-71e2d8944c38 | -5.56703 | -42.14363 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4519901b-9731-3ef9-beb4-2b5c59a7ba49 | -4.29681 | -48.27394 | 2025-09-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e91ca5-23c3-34a9-956e-b3feaf3cf205 | -6.19142 | -44.05265 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa213cd-95b2-37c0-b9ab-37d252e1a6fe | -5.60169 | -51.49314 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e10e11ac-b08e-30f3-b435-52531d23e66c | -3.76002 | -54.81483 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7274b32e-8ebf-3efa-8a5f-ed07a7efac96 | -5.56253 | -51.79716 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e0fc000-fe76-3fb3-afa4-3e6388f5eedb | -3.59338 | -47.51784 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e3743a7-db94-3df7-a4f6-3a5bb7130520 | -5.51885 | -43.86893 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 74379a4b-68e7-3257-aa23-f4abd58472b5 | -3.51723 | -47.21041 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfa8fad6-2439-3205-bce7-072ebe7f5c1e | -3.88798 | -52.40664 | 2025-09-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85a1bbde-fe93-3b64-b745-c242470c2c46 | -2.80339 | -58.34852 | 2025-09-21 04:55:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d23d25f3-9e1c-3ed6-a84a-1a79e3ff9e4e | -6.34463 | -44.68351 | 2025-09-21 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af684123-5d9f-37ed-866e-2eeb930f8bf6 | -6.2471 | -45.32982 | 2025-09-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 779df4a1-797d-3a6c-8b8c-8a9bb2bc9c40 | -4.37022 | -56.02557 | 2025-09-21 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0404df97-23b0-3252-9998-b065ec5d7b6f | -2.30295 | -48.39187 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e23c9996-31ee-3f89-be0b-3b5a30dae7bf | -3.29538 | -51.6036 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87441d84-a1dd-39d0-a795-6a5f7b9cb9fe | -2.69226 | -59.4225 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd4e8c8d-ed8a-3cd4-9bc6-9b65fe75c7e6 | -3.51349 | -47.2055 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e91b3f20-b9f9-37f3-9e21-8871f486602a | -5.42986 | -45.50479 | 2025-09-21 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea26b598-5815-3b59-949c-1852125d39ab | -3.75666 | -54.81431 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4d55b751-c11f-3f22-b977-b1862ba865f3 | -2.61361 | -46.85594 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b8d2879-f65e-3ea2-9867-382b2468da97 | -2.80283 | -58.35204 | 2025-09-21 04:55:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 186fabf5-657c-3d68-b482-765674fa5df0 | -7.47532 | -46.66315 | 2025-09-21 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d57783a-d0ca-38a9-9573-3187708e70c8 | -3.86189 | -43.09664 | 2025-09-21 04:55:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a670338c-39ad-393a-a11d-625d9c4dd221 | -5.64906 | -51.4644 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7f046c8-a472-33b7-b652-0c4c6140afaa | -3.59038 | -43.91247 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ec6497-07da-3055-a27f-301aa846d7eb | -5.38751 | -50.53354 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e5a164e-d20f-3ba6-8b26-033c2fb29166 | -5.52452 | -43.86994 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a4b6703-5fbb-30fc-a9d2-c7d91825c5e2 | -7.92443 | -44.11095 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2189981-074e-3453-8b71-403582706079 | -4.41656 | -47.96778 | 2025-09-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f414fdfb-4e9d-358b-9377-5acd28a70846 | -7.92032 | -44.09767 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa13894a-6c2a-332e-bf3d-4cf11369ff87 | -3.64908 | -58.16348 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11030c89-41c4-3d65-8aca-3b0a9cca96e0 | -3.46019 | -51.21485 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0ad113b-c563-345f-b8c2-fd9197036812 | -4.46213 | -50.49984 | 2025-09-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 261d2c4c-02eb-35fa-bd45-1a846230592a | -5.47369 | -45.38124 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9448c82-15bf-3805-bf13-6dc82ed97156 | -4.06275 | -55.56147 | 2025-09-21 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88b50ac5-2961-398f-b79a-cc25b1c44ca3 | -5.57908 | -42.15038 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| cf279570-6772-3642-9579-e754eee95404 | -6.44887 | -45.69555 | 2025-09-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b136be-a63f-373d-8274-f79ced80744f | -1.86191 | -47.98412 | 2025-09-21 04:55:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ffeddc-f55d-3776-9fa5-f02a084f9fc2 | -5.26919 | -45.05294 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8323ebf6-ce58-35b0-8aaa-b8572fa4c58b | -1.12517 | -54.14155 | 2025-09-21 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6c40268-dfc6-3413-981a-36f9c2567b12 | -0.95115 | -47.36008 | 2025-09-21 04:55:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc843e4-5444-30c5-9a0c-407126f9f64a | -3.30813 | -48.71113 | 2025-09-21 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9facca-6b86-3ae5-a836-fae0e3336116 | -7.92499 | -44.10679 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7dc1a2eb-9da3-3e0a-af42-300dd7421d95 | -10.41482 | -47.8567 | 2025-09-21 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9f4f1f1-4e43-30cf-87e2-20c760d60542 | -12.41788 | -45.10807 | 2025-09-21 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b32f525-cc3e-3123-a084-be7fdaf0f57d | -12.08355 | -44.79846 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aa2666a-2a0c-3a4a-95da-2abef1ae1073 | -7.94336 | -44.10461 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a90de6d6-b975-3d83-82e2-5781d59f6bcc | -14.43616 | -47.57817 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83039914-e25b-37c8-a018-978618b3a69a | -11.49236 | -43.5878 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42924c45-2eba-342e-89fd-e62ef165a16b | -14.6199 | -48.27285 | 2025-09-21 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36816884-85a5-3ef0-a0e8-d4da5c71eca5 | -14.45357 | -46.50499 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f272a1f7-3d9f-37cf-8219-45f681d1085c | -14.25671 | -44.38271 | 2025-09-21 04:57:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68454515-5ee0-38f2-b73a-3fec5ecbdd2a | -9.41944 | -44.70736 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a152542-88d2-3ebe-be03-01e59aa0006f | -11.49807 | -43.59354 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61497472-4c6e-37dc-b094-75dab3c3058d | -7.9439 | -44.10044 | 2025-09-21 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9e891ee-9b6f-33e6-9934-47fb222d6a7a | -12.71816 | -46.85873 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 253fcb29-840b-3254-a0f8-d3cd55ce1499 | -10.78338 | -47.33394 | 2025-09-21 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 249a90c1-093c-3060-8727-92ec2dfb4f3c | -9.0845 | -49.64415 | 2025-09-21 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a365dbf-7970-3517-b88e-932a765e7546 | -10.1553 | -64.73786 | 2025-09-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5578aa40-5d93-3333-b8c8-10d2627c10a3 | -12.71943 | -46.84823 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7ffae2a9-4376-3ad7-b8a7-fe1e12090c8f | -11.29478 | -47.51756 | 2025-09-21 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffcc10eb-fd44-313b-b77d-2fe3aa35b18e | -9.63102 | -57.85024 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd9adb0d-5771-3d78-98fb-6af001248330 | -10.16076 | -64.73897 | 2025-09-21 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7baeb4c8-be40-31d7-b8a3-4e14c2919bb3 | -14.43651 | -47.57539 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aac3c54e-8666-3e17-a66a-a449ece89082 | -11.48778 | -43.57206 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad3d5da5-a0ff-3c53-8ce1-750a8eb7a706 | -12.25018 | -49.17406 | 2025-09-21 04:57:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fd0bd4d-4bc7-33e6-893e-c52535c4386f | -8.98513 | -65.45178 | 2025-09-21 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c667546-7f63-3353-a14b-5b0760b96eda | -9.16288 | -44.62381 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 44e8b9a0-7a09-375d-8759-8147acea6150 | -11.48836 | -43.5669 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78e69557-b33c-3580-8485-f4d031e2082d | -8.98256 | -48.94678 | 2025-09-21 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8281a16e-e5e1-3a5a-89c2-5aba072e913d | -10.29552 | -46.08486 | 2025-09-21 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80130600-516b-35be-9dec-c73b05a5e7ba | -12.08221 | -44.85495 | 2025-09-21 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c0f794-6b4b-3d8a-b1f8-e656e5a031ec | -9.48831 | -57.92099 | 2025-09-21 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf62832-7ec2-3a8e-a525-6a8720add8c7 | -9.42566 | -44.70409 | 2025-09-21 04:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1fd58824-1c7e-38bb-9017-adace489df72 | -12.31931 | -44.84995 | 2025-09-21 04:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed4486d6-73d8-31b4-b542-b5e626a9562c | -9.16459 | -44.62805 | 2025-09-21 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f567991-047b-3d06-b296-376f25b5abb1 | -11.49523 | -43.58657 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dfa5fa9-50ca-3007-83eb-9759f4e21b9b | -14.44217 | -47.5652 | 2025-09-21 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67bd97ec-83a0-3bf5-84af-7d054accf235 | -14.4521 | -46.51789 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 726002f4-e095-3da1-92b4-71684480b19d | -12.71475 | -46.84363 | 2025-09-21 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68a66537-29ae-3311-a28e-057d97d5c6c1 | -14.46954 | -46.50925 | 2025-09-21 04:57:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac66d588-bc55-3847-9686-d079deeb5119 | -11.48447 | -43.57012 | 2025-09-21 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
