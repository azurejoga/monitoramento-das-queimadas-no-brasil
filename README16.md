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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84183cf2-4cd1-3625-b996-5e244c05d301 | -8.44189 | -43.86593 | 2025-11-08 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d880071c-633a-3f8f-9cee-591443ad13ca | -11.96227 | -44.35033 | 2025-11-08 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c603de69-4275-350a-a4fc-64553614bc34 | -10.51449 | -42.42731 | 2025-11-08 04:08:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b53018d-a356-336f-a657-40db4a170017 | -11.19903 | -53.82913 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6adc043-d406-3563-bee9-ae6b7033e833 | -8.3281 | -46.25562 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b35373c-2652-32ff-9ff5-d59f5e8795e7 | -8.99652 | -37.53615 | 2025-11-08 04:08:00 | NOAA-21 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 045e4229-fc86-3af5-b5cb-70e88258f6ba | -7.46592 | -46.63774 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89da4b63-1f9d-3d68-84ae-bcd4e4b58b1b | -9.15994 | -51.30753 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80055c66-c2a2-31ce-8e37-463687627cea | -7.55341 | -45.86035 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c371c3b-6e34-330e-bb8c-f1dbab3245e0 | -7.04248 | -46.98602 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34959478-f74b-3f6e-988e-5de6153effdf | -10.99464 | -53.99156 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0687191-d28d-3a0d-8246-1ca3a1d85191 | -9.97557 | -44.63113 | 2025-11-08 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fec2464c-4cd5-3664-b2d2-2310a7f787c4 | -9.22238 | -45.18667 | 2025-11-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2056502-3605-3806-b93b-8dbf0c3add60 | -9.04453 | -47.00021 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54910531-9099-3bdf-a523-8d648db5518b | -8.06555 | -47.12345 | 2025-11-08 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b95f28b7-f829-347e-a283-ab7409289d6b | -7.79824 | -46.6516 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48886606-d2ce-3bfb-83ba-ff374259db42 | -11.66965 | -43.89478 | 2025-11-08 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92ea576d-83de-3d9e-9122-dc82031d3593 | -9.86928 | -36.55847 | 2025-11-08 04:08:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de399c62-61cc-379d-ac60-2bf633285003 | -7.31778 | -47.38159 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bfca8c4-0b5a-38f2-8544-b11ee68bb76f | -8.32728 | -46.26053 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c91d3af6-5cc5-3e07-ab65-70c9c7c131d3 | -9.09212 | -44.32199 | 2025-11-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 897870b6-eb43-391b-8eb7-5a01f69fcbc2 | -7.03657 | -46.98164 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5482c4fd-3543-3d53-b4f9-0272c2a48707 | -11.19778 | -53.82877 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83818371-6dda-3e26-8daa-441d7b97bf89 | -9.13917 | -51.30044 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c06a268-fe09-3698-99ab-ce79aeba7dba | -9.04795 | -47.0044 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661f69c6-7e77-38f7-9d42-b13b8c32e9c4 | -7.78894 | -48.52749 | 2025-11-08 04:08:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55b53a9e-bcba-328c-b448-65adf69848a6 | -7.04009 | -46.98604 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b6b66c95-49e7-38c9-892f-796985512535 | -11.19811 | -53.83367 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30624431-1051-333c-be74-e43647b99c2c | -11.673 | -43.89534 | 2025-11-08 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2792243b-3919-35be-9750-fb376e04cfff | -7.54376 | -47.38281 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2c8cc4-d982-38a2-a5ee-43aa66314e1d | -9.16056 | -51.30416 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19800f0e-8d78-3994-b651-380fe5f0a4c6 | -8.75493 | -44.23256 | 2025-11-08 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54ad97d9-ddd2-3a81-a50a-acfd29089e59 | -9.90646 | -47.41619 | 2025-11-08 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73e8ee7d-c134-30f1-81c4-7859e87ab843 | -7.79424 | -46.65094 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17534c01-3b4c-35bd-8dbb-d0652a9d0f3f | -13.88954 | -48.65437 | 2025-11-08 04:08:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9891cc6b-d9dd-37ad-a38e-3f18ef0b1e24 | -7.55804 | -45.85624 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3c97c86-66be-32eb-a2b5-4469d6503e9c | -8.48609 | -40.68548 | 2025-11-08 04:08:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e0a11c62-97e3-3356-97c1-28da78848982 | -10.98948 | -53.98551 | 2025-11-08 04:08:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 854e8d41-4355-32ba-949a-198bf64cbc5a | -7.4849 | -45.92525 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4113f2e-78d9-3d3d-8dcb-ff5d5f0b41f6 | -8.6339 | -41.18113 | 2025-11-08 04:08:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68502f82-198b-3ade-966f-2d9273b0d1e3 | -7.57175 | -45.86815 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95b7718c-f7ca-39ed-9c35-c3908b638d97 | -8.92831 | -44.20043 | 2025-11-08 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bc648d4-981d-3702-ac83-2a4745fb768f | -8.4447 | -43.87027 | 2025-11-08 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c62bf194-cb8b-32ba-9f1c-9e0bb1712f65 | -9.73262 | -48.77822 | 2025-11-08 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f8e095a-d37b-38e8-bcc5-e778b4b3c2fd | -8.49241 | -44.7298 | 2025-11-08 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79101a97-e468-3a1b-92ab-ea4c9a04b211 | -8.63336 | -41.18463 | 2025-11-08 04:08:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4223b1a-8af2-303b-ad2f-21213005a81f | -7.322 | -47.38232 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a8b2c8d-2e4b-369f-b9d9-029f219478de | -9.13383 | -51.2995 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2f3a9db-f6c9-3166-92c2-eb65d47e383a | -11.69027 | -44.14221 | 2025-11-08 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16ec799b-2aae-3dbf-b100-578d18c2bc42 | -8.33197 | -46.25626 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d2e17c1-8673-3dc4-ab47-5b6b79894a2e | -7.04071 | -46.98228 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64d6f77a-b543-3159-8e5c-2fc07ca8a797 | -9.04332 | -47.00731 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a8b8691-bc52-31e5-aec5-adb21415b14b | -7.78623 | -46.6496 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a832b8-ef29-31f7-b2f7-ee56455efe13 | -7.79483 | -46.64743 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86f884d-e839-3f23-b33b-c526a259c62c | -10.2331 | -44.80547 | 2025-11-08 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4736713b-4967-37c5-85f4-873d38a2683a | -11.68629 | -44.14533 | 2025-11-08 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7801436c-e9c6-3568-a6a1-b4abfcfe58cc | -9.14452 | -51.30138 | 2025-11-08 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1b7a1f9-d6d5-3b08-8446-36e2b3debdfd | -7.03418 | -46.98475 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 381a2f53-a886-3937-8981-58d080d1a753 | -9.32434 | -47.82714 | 2025-11-08 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27f36e3f-c8fa-356a-be6a-7322663bb769 | -7.7881 | -48.53227 | 2025-11-08 04:08:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1522e8c1-ba5b-3d02-8eff-ea3f7a130048 | -10.3675 | -49.87348 | 2025-11-08 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9822bffa-3ba7-3750-bdfc-d2e543b985fa | -9.12361 | -40.09982 | 2025-11-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a74a9310-645e-3c48-adf7-b317a6b17bec | -10.75697 | -44.80094 | 2025-11-08 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eebb8057-d2a6-3a4e-9606-939c1598b196 | -8.48951 | -44.72519 | 2025-11-08 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a035d50b-d9b8-3863-8513-e01f748e08a0 | -9.04915 | -46.99734 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6406498-d3c0-3e3b-bddb-2373c426f6e9 | -7.3171 | -47.38551 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b9347e4-738d-33ca-bf58-7ed759ac2113 | -9.05317 | -46.99799 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 509c8feb-71ea-3758-95dc-2851e36ce83f | -7.5504 | -47.24411 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bec095f-758e-32e8-a7bd-3f933cf6d3c3 | -11.69365 | -44.14277 | 2025-11-08 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91474237-17db-30c2-9df8-6dcdc7c954ef | -8.7444 | -48.3185 | 2025-11-08 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf6f5ae-fd23-3401-a84d-138416337c0c | -8.90262 | -47.82522 | 2025-11-08 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e5a5bf1-8b53-379c-92d9-ae598c79eabf | -9.04393 | -47.00375 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7641a44d-887b-3ccb-a318-801fee7cf77b | -9.05377 | -46.99444 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd3e91d2-80a8-3d9c-821d-77697b2b0bc0 | -10.361 | -47.33304 | 2025-11-08 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75f3c9f3-bda1-3c41-8f68-8c2d94a2cdde | -9.09559 | -44.32255 | 2025-11-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 119f1e81-c900-33de-8788-937bab98b8c0 | -14.28113 | -49.37939 | 2025-11-08 04:08:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0732d717-23e7-3b3f-976f-1ecb72d29f9c | -9.50185 | -45.08187 | 2025-11-08 04:08:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f5fc28f-2c1d-3ae1-aa8f-832ebf526afe | -10.57545 | -49.25136 | 2025-11-08 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce5b79bf-3c9a-300a-a7ed-4348e2e70e60 | -7.42556 | -46.6562 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f391fe1-3356-3c9f-8137-c1a93f89ea9c | -10.99606 | -44.85568 | 2025-11-08 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3f8b58c-c93a-382b-8ef9-6354df098436 | -9.46439 | -47.87165 | 2025-11-08 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d988e12f-63ab-3887-8f10-e4ee77bdc7c0 | -8.44127 | -43.86972 | 2025-11-08 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6601f83b-f8a7-3f45-92eb-e6611bdc6b44 | -9.7633 | -55.61818 | 2025-11-08 04:08:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47273d8e-62c6-3fa2-a539-abcd54006b9b | -9.09621 | -44.31867 | 2025-11-08 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ba0a5bc-71ad-328c-8401-4d3b48852a84 | -7.48874 | -45.92587 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e70a6e30-ecd5-3810-9e4f-1e04b5a27da9 | -11.09574 | -45.19358 | 2025-11-08 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc2f4140-bc37-3ee5-85bd-10c6a04b68da | -7.03898 | -46.98164 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| badda12e-f416-393d-b803-1a48a552a050 | -9.04855 | -47.00087 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2382a0b8-3993-31de-a3ef-5be3d5b6db64 | -9.04734 | -47.00797 | 2025-11-08 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54820d2d-56df-3a9d-bd08-7cfb19d506ad | -7.53043 | -47.38461 | 2025-11-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cb28340-62ba-3670-bb72-538fa81c6c32 | -8.07377 | -47.12484 | 2025-11-08 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9732e623-a682-362b-a9af-9494ea522fa8 | -9.1242 | -40.09933 | 2025-11-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 771eb9a4-e92d-3ce7-a5a6-11e008af0a70 | -7.79364 | -46.65445 | 2025-11-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdf031b7-cfed-3205-a84e-831d6a8c7570 | -8.90616 | -47.83002 | 2025-11-08 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b450395f-cb3f-33b6-88f0-9d5b7a424248 | -3.639 | -43.6544 | 2025-11-08 04:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fdeb52ba-7b81-3996-9cc0-db97731dd217 | -15.18885 | -49.52075 | 2025-11-08 04:10:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55bb85fd-17fb-3bfd-8b1d-c0bf6b4ccdfa | -16.09343 | -49.39309 | 2025-11-08 04:10:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce3e4ad1-091c-3262-b7a7-a250675a0418 | -17.87844 | -52.39617 | 2025-11-08 04:10:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c7b1f13-4537-3630-ad63-1112cdb2f3a0 | -17.62404 | -49.33953 | 2025-11-08 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b288b3a-bbac-3dbc-8c7a-a9ce7beef48c | -14.6745 | -51.89402 | 2025-11-08 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)
