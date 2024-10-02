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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c854056d-771b-35ed-b444-e1ceb4cf20e2 | -21.3661 | -55.6807 | 2024-10-02 02:57:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 05884d84-9e1d-3efe-b755-7f6642b92c84 | -21.6275 | -50.796 | 2024-10-02 02:57:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 4a740f7b-f481-32a2-8f0a-c7b30b588db4 | -22.677 | -43.7014 | 2024-10-02 02:57:09 | GOES-16 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 613b8b83-5e69-343f-8df0-deb3cdfb9dcf | -22.9014 | -45.0779 | 2024-10-02 02:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.9 |
| ccc42ef0-0a17-3dcb-a815-f235368032cd | -22.9006 | -45.1029 | 2024-10-02 02:57:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| df87f49a-954d-33ed-afa1-b0a3da1e9cb6 | -23.175 | -49.5943 | 2024-10-02 02:57:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.4 |
| 89009925-445f-328c-b02f-f2af0a9e8719 | -22.37 | -49.34 | 2024-10-02 03:03:17 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8045d71b-6e5e-3c20-943c-20c242e35a90 | -22.37 | -49.28 | 2024-10-02 03:03:17 | MSG-03 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 319d79dc-27d6-319e-b496-8308df8c6ad6 | -16.59 | -58.26 | 2024-10-02 03:03:52 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9e60123-efa2-3042-b777-fb74c3efa1db | -7.44114 | -35.06089 | 2024-10-02 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1ba6dfa9-9660-3e31-a09d-2797ef5c21e4 | -7.44267 | -35.06043 | 2024-10-02 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1b7d3281-70e7-31fe-8326-6f81fd706f35 | -7.37676 | -35.2159 | 2024-10-02 03:04:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6af27f54-1e30-3096-963a-537982b6c985 | -7.37134 | -35.21523 | 2024-10-02 03:04:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5254b6a1-cf5f-3eb2-a1cc-2111d569d306 | -7.07367 | -39.15207 | 2024-10-02 03:04:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8679242d-81f6-3823-ab0d-3ed12198470c | -5.20647 | -37.62781 | 2024-10-02 03:04:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a2320ab4-e319-3281-bd32-96c0095a1e13 | -3.128 | -49.4235 | 2024-10-02 03:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7ff74dc0-0de1-3410-9153-c11d87925fcb | -3.1465 | -49.4229 | 2024-10-02 03:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6cd26fde-1b66-3284-8e87-717ffbc0ca14 | -6.1301 | -47.2664 | 2024-10-02 03:05:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0162e722-e05a-3916-aa5a-04706853bde1 | -8.4643 | -62.7124 | 2024-10-02 03:05:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d8e7fd97-a66e-32f7-b2db-2969e923826b | -10.82444 | -37.16624 | 2024-10-02 03:06:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6b67eaf-e34a-3b55-84a4-3235cf4bdb9d | -9.57455 | -40.34644 | 2024-10-02 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ed313042-67dd-3992-8520-b56f4cf2fabe | -9.46346 | -40.36828 | 2024-10-02 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ebbc610-9611-3d5d-b30d-6869781dc501 | -9.45638 | -40.36687 | 2024-10-02 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3cb656d-2794-3630-9648-ede52caf955e | -9.42933 | -40.31799 | 2024-10-02 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a88df9db-ad15-373e-ba73-ef1e2c852ab7 | -12.72156 | -40.22585 | 2024-10-02 03:06:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6d743e47-968d-356b-a9bf-7ebac6abafd2 | -8.69288 | -36.23834 | 2024-10-02 03:06:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a05dafc3-9ba5-3432-9ef7-679afb98d4df | -8.68724 | -36.23745 | 2024-10-02 03:06:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 08ea472b-4c91-3273-8e43-c84b96912e2c | -10.0799 | -46.8561 | 2024-10-02 03:06:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b3ff7a55-1358-313d-8703-feb8876ee3de | -9.9367 | -64.9179 | 2024-10-02 03:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ccc98887-9615-38c3-a765-02bd71ea8483 | -9.9368 | -64.8991 | 2024-10-02 03:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a2c187ae-8394-3f4c-89e5-d963c58e9ed7 | -9.9553 | -64.9172 | 2024-10-02 03:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 64cef221-9e85-34dc-bb38-16ef6eebfdcb | -9.9554 | -64.8984 | 2024-10-02 03:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8f99a77b-d466-3c22-90bb-8353650552d3 | -11.6742 | -65.0172 | 2024-10-02 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| db38194b-344e-31fe-9634-7589a1a38228 | -11.6743 | -64.9983 | 2024-10-02 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9b083998-0384-3648-b680-ffaa084b5560 | -12.2946 | -47.6446 | 2024-10-02 03:06:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 021411de-5dd0-3482-9eff-5440a6070887 | -12.6484 | -63.1214 | 2024-10-02 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 157763b9-cc05-3a51-8f99-17e425aadee1 | -12.6486 | -63.1022 | 2024-10-02 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 493cc5dd-d1b8-3692-9ee0-38a6d128b165 | -12.7054 | -63.0798 | 2024-10-02 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 0be5df90-445f-305f-aa3f-f8a4b7f8e47f | -12.9574 | -51.5369 | 2024-10-02 03:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d5a4974e-ed76-38bd-96b9-7e79929a6f4d | -12.9766 | -51.5345 | 2024-10-02 03:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1c511e4e-98c1-33a5-80d2-fc6729746e23 | -12.8593 | -62.7826 | 2024-10-02 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d1475eda-74af-35d4-b360-ad203e1147b6 | -13.2177 | -48.6019 | 2024-10-02 03:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 423d4987-7314-328e-9585-a9ab1dda62c1 | -13.198 | -48.6267 | 2024-10-02 03:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 542422de-8332-3d47-bf6d-2b182671d344 | -13.1984 | -48.6046 | 2024-10-02 03:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| aa5cfa37-b441-36c5-bc37-b1077674a4a5 | -13.2173 | -48.624 | 2024-10-02 03:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 02fa430b-0141-3c1e-ac64-241345b2d87e | -13.093 | -51.4352 | 2024-10-02 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f74445d6-0e20-3389-9e75-d0e7348a1103 | -13.1118 | -51.4542 | 2024-10-02 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ff2c23b6-384c-3121-8693-cfd92bd8f78b | -13.1122 | -51.4329 | 2024-10-02 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 227.4 |
| cae6138f-7681-32ee-8424-64a07fea1251 | -13.1125 | -51.4115 | 2024-10-02 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3d7fe535-33e3-3684-a50a-e4c2185ce3e3 | -13.1314 | -51.4305 | 2024-10-02 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e1fc70e9-75fd-3618-aa69-ca790b048009 | -14.5699 | -44.8351 | 2024-10-02 03:06:27 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 222f0e0b-0377-39bf-aeaa-4eed101154a5 | -16.4533 | -57.4392 | 2024-10-02 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| bfc8058e-2c43-31e3-ba62-5752c821c0ec | -16.6124 | -57.2375 | 2024-10-02 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 4521dde2-d02b-3ba5-a201-77bc4d5c0063 | -16.6127 | -57.217 | 2024-10-02 03:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 4166feaa-82af-380f-96bc-be000f137c74 | -16.7452 | -57.4878 | 2024-10-02 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 38348d12-77f9-3765-928a-fa9cba249e1b | -16.7455 | -57.4674 | 2024-10-02 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 9cecbb47-115c-30c9-9cee-99d989deaae2 | -16.7461 | -57.4265 | 2024-10-02 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| b8a044f6-dee7-3f01-a52c-b64ae79fd1dc | -16.6319 | -57.2352 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 2a25d581-3c6e-34f2-acf7-c6087a0f84a4 | -16.6322 | -57.2147 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 531540b8-f939-3cfc-9d18-9f089eb65e82 | -16.6518 | -57.2125 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 604c1443-58ff-38d1-8046-d2539e0218ea | -16.6717 | -57.1897 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| fda97418-8954-33f6-a350-c2dd7849bfc7 | -16.6884 | -57.3718 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| be4c7249-3765-306b-9586-a63fbcaf98df | -16.6887 | -57.3513 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 69d08f69-e502-3964-99aa-816af7cee3a1 | -16.6909 | -57.208 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| a9cb4da4-5f04-35cd-9bed-e9ccfb499a90 | -16.6912 | -57.1875 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.2 |
| 9f7fb338-43d9-3bb8-b00b-7e92867bdf7c | -16.6916 | -57.167 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 1757860d-a1ea-3bbe-9647-81cc27fea87e | -16.7063 | -57.4718 | 2024-10-02 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 55835788-671f-39f0-9206-1bf3f9e27cd8 | -16.7108 | -57.1852 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| fdc2477d-4200-351e-852d-7f153dbe0764 | -16.7265 | -57.4287 | 2024-10-02 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 8b50786c-3fb3-3681-8328-cc039ab71734 | -16.7111 | -57.1647 | 2024-10-02 03:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 8f090992-e9ad-33a0-a25d-43641b567e97 | -16.8292 | -55.9152 | 2024-10-02 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 72199bf0-1ef5-380e-a479-372ca6dd738f | -16.8295 | -55.8945 | 2024-10-02 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 1c9d4b95-b073-306e-b057-1825e936e390 | -16.8695 | -55.848 | 2024-10-02 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 28284c35-995e-31ee-861a-2cfc27f8c861 | -16.8698 | -55.8272 | 2024-10-02 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| f3fac6e8-c799-3d19-8d30-4c47a9e7cefe | -16.8891 | -55.8455 | 2024-10-02 03:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 16be5c77-3c4a-36d7-a2a4-9d5c456f704b | -17.1577 | -56.1844 | 2024-10-02 03:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| bd97947a-b975-3bd4-acaa-d0e189ef258e | -17.1581 | -56.1637 | 2024-10-02 03:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 210ab48a-a28f-33ac-bf3b-bb462c7900d8 | -17.1971 | -56.1795 | 2024-10-02 03:06:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 36f8eb3b-b234-3c35-a90f-90181b13a5f1 | -17.1974 | -56.1587 | 2024-10-02 03:06:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| a5ac443a-5e28-33c2-9ea7-8896dfbb6864 | -17.2167 | -56.177 | 2024-10-02 03:06:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| f82d0676-f7c2-3f14-b7bf-1a79fc422afd | -17.2171 | -56.1562 | 2024-10-02 03:06:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.1 |
| e2e04547-ecce-3278-acc5-f7c38845f5f8 | -21.3451 | -55.7056 | 2024-10-02 03:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2213be55-be94-3c2b-8484-bbc637ea786b | -21.3456 | -55.6841 | 2024-10-02 03:07:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 45a9cc64-90ec-3e4f-80af-218557d57187 | -21.3661 | -55.6807 | 2024-10-02 03:07:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 20ba2f26-b5b8-3707-aea3-6b978481c9b7 | -22.9014 | -45.0779 | 2024-10-02 03:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 55212e4f-96ba-3b5b-8da8-243a165c5527 | -23.175 | -49.5943 | 2024-10-02 03:07:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 439146d2-06e0-39f2-a063-cd1cb1f6a0a6 | -18.06924 | -42.61732 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| a6b025a8-4d55-3cdd-bf3b-370429885a15 | -18.07012 | -42.61071 | 2024-10-02 03:08:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 010e91db-ac0b-399c-ab5f-d53e2c750f2a | -18.51452 | -42.22792 | 2024-10-02 03:08:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 59ded9a7-215f-3583-8a50-051b95dd2483 | -18.5156 | -42.22332 | 2024-10-02 03:08:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c3e73ade-f1df-31cd-851a-bb1c380ee6ea | -18.51649 | -42.22945 | 2024-10-02 03:08:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 13726ebf-c1b2-38f3-9323-3e58b1f07502 | -18.51761 | -42.22478 | 2024-10-02 03:08:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 70683281-fa7f-3b35-84d9-4e9f916945be | -18.52108 | -42.23013 | 2024-10-02 03:08:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2fa21162-29f8-326e-a561-fada4624fb8d | -18.52165 | -42.23749 | 2024-10-02 03:08:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2de554b9-9ee9-30db-9684-693dbedb9a5d | -19.24434 | -40.62976 | 2024-10-02 03:08:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0eefedf6-ea43-3fd9-a444-59d361d6b6e2 | -19.24555 | -40.62444 | 2024-10-02 03:08:00 | NOAA-21 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cda189ec-9713-3458-941c-ab3d1009039d | -19.438 | -43.06 | 2024-10-02 03:08:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0eea6974-ddb7-35a8-89c9-5966f5050514 | -19.44506 | -43.06094 | 2024-10-02 03:08:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 48f7451e-fbd9-3209-8673-db53924e45ca | -19.51153 | -42.87686 | 2024-10-02 03:08:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 30b453bc-d80f-32cd-8455-d63a821b7ee3 | -19.54871 | -40.22285 | 2024-10-02 03:08:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
