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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9379d2d3-4a6f-3aac-8b33-963e16e06a89 | -15.6782 | -52.7341 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c77b209-5c48-3d6e-921c-21b7ae8728f7 | -14.3364 | -51.907501 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0fc87c1-84de-3a0d-8283-04da0c54f353 | -21.382799 | -48.7957 | 2025-08-28 00:51:00 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0f8df3ba-1960-37f0-b847-12b2c3658a18 | -12.8161 | -48.1399 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ae3ac7-801b-360f-a0b9-2bad1dae00ce | -13.7606 | -51.9016 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96d7293c-f119-3534-94ba-3b301ef043f0 | -13.5351 | -46.929798 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c6397d7c-aafe-3a53-ae4d-43d1a9b8759c | -11.3358 | -43.553001 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c04fb80-1428-3534-861a-ca315d789e99 | -11.8118 | -46.812901 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68615638-dc62-3326-bb3e-a2ee7594bfe5 | -4.8021 | -47.2584 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bbe5efc1-082b-308a-9a3f-cf0c43fd0abb | -19.0602 | -42.129002 | 2025-08-28 00:51:00 | METOP-C | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a5f9e46-7028-39c6-9ea5-03f93ad2eac0 | -12.9671 | -44.578602 | 2025-08-28 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f83a81fe-0d50-353c-9c09-bcc66ca5df46 | -9.6103 | -40.325401 | 2025-08-28 00:51:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 822ff49b-632c-3300-a386-8bdbec597dc2 | -13.635 | -48.242901 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a91f6beb-128d-3828-8295-980d35b1e898 | -6.4446 | -44.561798 | 2025-08-28 00:51:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8061ae-bccf-3098-a954-c0a723641046 | -3.286 | -52.510201 | 2025-08-28 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e45fe807-2060-3abd-9df2-bc40ff8107d4 | -7.2662 | -45.355099 | 2025-08-28 00:51:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28fce240-30ca-37e4-a847-9d46ddb3c44a | -21.6833 | -49.0513 | 2025-08-28 00:51:00 | METOP-C | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0c46e19b-e56f-3638-bf4a-9d39eee2b2b9 | -12.8046 | -48.134998 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28309adc-81f6-340a-b927-ac491131cbb8 | -12.7999 | -48.159199 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51c7bc19-e999-3928-ab10-7ac9878afc51 | -11.2223 | -55.041698 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a97376c-0a96-3e25-a543-110177b8ecf3 | -7.0642 | -44.355801 | 2025-08-28 00:51:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb7b8f0a-b5e2-3a5c-a035-406fdb7d1a9a | -13.4423 | -46.8437 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 138799bd-fd7f-3ef6-95e5-d29335be067a | -6.1647 | -44.0485 | 2025-08-28 00:51:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3e85e4f-a038-3b61-8c59-54cfe0c6bb18 | -3.9909 | -47.886501 | 2025-08-28 00:51:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d04a92de-127b-3dea-aac9-1bd1bbf21296 | -10.5429 | -46.6931 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be39c797-e18f-36cb-982a-e6b3c573b9f4 | -5.2003 | -46.069801 | 2025-08-28 00:51:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b94e34c4-38ac-3cf7-b4f6-e191aa6091f4 | -4.7945 | -47.27 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd63808-62aa-3990-ad6c-096382ea8081 | -11.2321 | -55.0397 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7faf098d-35e3-3c0b-90c6-b216a8ab3fe9 | -13.0793 | -46.3176 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7b7d88d0-3d11-3997-a09f-75c3d5b89486 | -13.5239 | -46.8825 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01e32136-0ef7-37fa-9da2-cad2367208da | -17.5474 | -46.625198 | 2025-08-28 00:51:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed39688-7939-35cd-9704-c63a65c7c0a8 | -12.8259 | -48.1376 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51893e09-1a5f-3d26-b03e-a26403dcd07a | -3.4249 | -49.040199 | 2025-08-28 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd589e9-48cf-38ad-84f0-c4a8688bb2c7 | -6.8809 | -43.609798 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eda7fe41-9ed4-3b32-8c74-769d8287e940 | -21.384399 | -48.8032 | 2025-08-28 00:51:00 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77f86e44-34e1-38bb-840e-aaafd535ee94 | -13.3901 | -51.755001 | 2025-08-28 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e845cf4-d6a2-3f89-9482-6da60584cdf2 | -9.7794 | -49.8778 | 2025-08-28 00:51:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dae1e78b-1317-3ce8-a11d-fa632d6ff086 | -13.7623 | -51.9095 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01ee2f3f-d061-35d4-9f1f-63b955776f04 | -5.1977 | -46.058899 | 2025-08-28 00:51:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8da498e-e7b6-38a0-b661-cbb09fa3c62f | -21.1401 | -45.888401 | 2025-08-28 00:51:00 | METOP-C | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4b9d488-8824-3dee-9af8-ca9aa36b0e81 | -12.7948 | -48.137299 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce7c97e9-f1f9-3e4e-83be-6b4555cf1bdc | -15.6486 | -49.763199 | 2025-08-28 00:51:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f33e5bbb-c8ec-373f-94c1-5bd8173309d5 | -3.7809 | -45.041901 | 2025-08-28 00:51:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e455b688-8e2d-3aff-945d-73656eaafbbe | -9.4818 | -51.935501 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335aeaaa-92a6-3d82-bd4b-de8e2879e124 | -13.4326 | -46.846001 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49a2dd65-b2af-32bd-8865-2aee6842658c | -15.1837 | -52.326401 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11e7a77f-9910-3959-a7b9-38a7c1b9dd88 | -13.7491 | -51.896 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5939131-e920-317b-acbf-43f757cdd7f8 | -13.4411 | -46.969398 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 602e9c0c-b079-36b8-a7ed-10b905e53ac1 | -4.7923 | -47.2607 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74ff60ca-face-3084-8a77-936290ffcc2f | -15.6454 | -49.748901 | 2025-08-28 00:51:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a98b6f8a-050e-311b-989a-196bf10d85a2 | -13.449 | -46.959099 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d0a514f-4b2b-3e4c-8d0a-7bdf65de2311 | -12.7199 | -48.170502 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 265ebcf0-5e4a-3e65-84f2-f77dcd2062b6 | -9.4654 | -51.9543 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 572e9601-e666-3b54-bace-20f583fc88e3 | -12.782 | -48.171101 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da037f63-2005-3cca-8e9b-755585f91733 | -12.7314 | -48.175499 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6438dc59-9dd0-3162-9604-27413fc33d10 | -17.5555 | -46.6152 | 2025-08-28 00:51:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53335313-c5dc-3b2b-8f2d-f3cc82985f76 | -20.119301 | -44.332401 | 2025-08-28 00:51:00 | METOP-C | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd563b17-ab66-34f5-9a25-26118d3526a5 | -2.4484 | -47.109798 | 2025-08-28 00:51:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e54dd7c-c07c-3c49-851d-df7d1235d2b1 | -13.6236 | -48.238098 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1b0fee3-bfc2-3492-9349-435141e364ac | -8.9059 | -47.326199 | 2025-08-28 00:51:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb5f1a1-4151-3239-812f-b43b9c92d654 | -6.3273 | -43.745098 | 2025-08-28 00:51:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aeac04b0-edee-3a9b-b8a9-0e36bb4e5097 | -6.8869 | -43.5924 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| befe403d-84d8-3909-85ef-01ee024d183c | -14.3462 | -51.9053 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 990d240c-fe64-3309-a4fb-93032f662166 | -6.8906 | -43.607399 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee75dd62-c64f-37a1-a52c-5c17dfdb7866 | -12.8063 | -48.1423 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29f99329-e8c3-34b4-b534-69546af7308f | -3.4267 | -49.0481 | 2025-08-28 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 636cf991-b8d9-340c-9d28-dc345e29fa8a | -12.6791 | -48.172501 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7dde8e-a286-3dfe-b759-449c9a6eab53 | -9.4556 | -51.956501 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a472e3-0cdb-3fe0-99df-d1cf78892c4e | -13.4289 | -47.0056 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7fac7ba-6748-343b-af42-926730c71739 | -4.7901 | -47.251301 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90185a44-382c-37eb-92bf-81347c26f030 | -12.0676 | -46.6278 | 2025-08-28 00:51:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 259ca7f3-56c5-3001-af8a-bad3e939671f | -9.3158 | -57.673698 | 2025-08-28 00:51:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c612411c-0f41-3be0-a389-804b84dc7235 | -7.3381 | -59.627499 | 2025-08-28 00:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae65bf3-5b86-3665-9226-7a688d766924 | -13.9947 | -46.339001 | 2025-08-28 00:51:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 575bc8de-e4b0-31e7-99b9-c8b31aa3abd3 | -7.7035 | -44.608299 | 2025-08-28 00:51:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 14571b6c-f85f-3f0c-90b9-db9c2a3a0d96 | -11.806 | -46.7882 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41b4b3ed-81be-3b3c-b5de-1837ef7ef5e5 | -13.0773 | -46.3092 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ebd260b-00ca-39b3-b163-50626ed85764 | -9.4119 | -60.5676 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4044e086-ea4e-3461-a2ec-3192cd78b181 | -13.5216 | -46.9165 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8130bf7b-95a8-351a-a392-5cd52573219d | -15.647 | -49.7561 | 2025-08-28 00:51:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f2b058a-9241-3fb9-a69a-0585ba138c9f | -12.9547 | -44.570599 | 2025-08-28 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80d3b220-b7d3-33d9-91b6-ccace8ec09ed | -6.4381 | -44.5774 | 2025-08-28 00:51:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d86d73fd-4485-3e8e-868f-5f17553f5dd5 | -9.0081 | -48.727699 | 2025-08-28 00:51:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 45b426bd-2979-3d97-85a3-9f2c467f7e47 | -9.6066 | -40.350601 | 2025-08-28 00:51:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 665c3d15-31f8-3571-9ed1-ea25b06c44d4 | -12.8178 | -48.147202 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02f74355-3f94-3f24-a65e-abc2c6f24f90 | -21.0117 | -47.372799 | 2025-08-28 00:51:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 336c7da9-e6d0-39d1-a890-206b9514d0fe | -11.3163 | -43.5168 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 535c909a-549a-367a-8deb-e32ddf13b1ea | -10.7092 | -47.0877 | 2025-08-28 00:51:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76aacea9-9d18-3825-8abc-d9ec47afe7f6 | -6.4349 | -44.564201 | 2025-08-28 00:51:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 768ff7df-02b3-38d8-82c6-22b764c1b4e6 | -18.463301 | -49.7019 | 2025-08-28 00:51:00 | METOP-C | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07020b8a-c2e6-3ed9-a426-0ac35deac0a1 | -15.6311 | -52.753799 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b045e739-5ffa-365f-bc3f-6eaf0c45d4d3 | -3.4231 | -49.032398 | 2025-08-28 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0df4fb6b-0e63-32fa-a19a-2e67b8fce1e9 | -9.4932 | -51.940601 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84de6a7a-3df6-315f-8c14-194f87e5c8b9 | -10.4769 | -57.935101 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0673f8-e31c-3e2b-bbd0-c1e622d24286 | -13.4442 | -46.851601 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47558f7b-c00d-3834-a70a-4761668bd1b1 | -13.4374 | -46.953701 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cafcbe9e-a95f-379f-b8a1-8c053f331b7a | -17.777599 | -48.495899 | 2025-08-28 00:51:00 | METOP-C | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 310184c2-724b-34c5-9e0b-da70cc79f779 | -12.8209 | -48.115799 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb01436-177d-3027-b89f-da3dfc05789a | -13.4313 | -46.971802 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5182de3-77ad-3794-9b63-9106d73000eb | -6.5725 | -47.371101 | 2025-08-28 00:51:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
