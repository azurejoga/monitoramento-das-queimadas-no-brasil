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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77edad26-626b-30ca-bfa5-318cb46511cd | -17.09661 | -55.96006 | 2026-09-04 04:42:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2b852515-9e92-39a0-8f8a-53eb3dc41ffd | -21.06784 | -48.4586 | 2026-09-04 04:42:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32397e6f-f674-3231-b53d-0c378c31b37d | -21.25775 | -47.35616 | 2026-09-04 04:42:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9570121-8da0-3221-a0b6-ac03ce6f962c | -16.83131 | -49.53062 | 2026-09-04 04:42:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82404cd6-6c95-3f9f-9d12-8b58e4a38689 | -16.65767 | -43.63319 | 2026-09-04 04:42:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65bee691-3a2d-3c7e-92ed-27b98d382310 | -15.90496 | -50.16277 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7be1bb-04db-35b6-b740-de1b0861ef4b | -18.13529 | -51.8038 | 2026-09-04 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fac7392-cb91-384a-aaa9-f0353adfb873 | -15.91271 | -50.15674 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d99c672a-a203-38f9-99c2-5bca2e5adede | -20.97236 | -49.10391 | 2026-09-04 04:42:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8f5e794-f933-3512-aa88-078df66766f3 | -18.13923 | -51.80069 | 2026-09-04 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6324f986-753b-36d6-bfb2-de700d021b4b | -19.35294 | -47.08605 | 2026-09-04 04:42:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9716ba4-f3df-3bfe-9de5-4d4cbb0d0802 | -19.62666 | -46.97062 | 2026-09-04 04:42:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89fcc83e-92d0-36cc-8579-ef7a01fb93fa | -20.97155 | -46.49301 | 2026-09-04 04:42:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe8cce6b-5fc6-3b82-bacb-823638b0b349 | -21.26218 | -47.35188 | 2026-09-04 04:42:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 125b894c-82b2-370b-bdf3-77532a93b81b | -21.26153 | -47.35678 | 2026-09-04 04:42:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c67b5c46-9ef9-399c-9326-c571bfd241d7 | -17.31952 | -49.61681 | 2026-09-04 04:42:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66286527-9705-3d26-9a7f-0240131f37b5 | -15.90939 | -50.15618 | 2026-09-04 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 127f2675-127c-3433-9128-43c26f039f17 | -16.64793 | -49.40028 | 2026-09-04 04:42:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbfe44e0-a1b8-30a9-8e07-c7d16abd140b | -17.09812 | -56.86349 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fb33bf81-d571-35a8-8257-9fe353b4ca23 | -16.66217 | -43.63367 | 2026-09-04 04:42:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca8a4a3c-e280-38ea-9c96-404f4088f02a | -21.72247 | -47.12817 | 2026-09-04 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e470f117-89a7-360e-bd72-5c91339e33e8 | -16.74508 | -47.04314 | 2026-09-04 04:42:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 201b36f5-a401-3607-948f-273e57a67f99 | -17.90878 | -50.39438 | 2026-09-04 04:42:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51bd15d7-9110-3000-b2a2-24320c944a10 | -17.32286 | -49.61737 | 2026-09-04 04:42:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b381c81-be03-3e1b-812d-9594de0c38b3 | -17.09974 | -56.85501 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 672f62bd-9ee1-353e-8900-b008d522443c | -17.10322 | -56.86015 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2fdee455-0536-3b33-bb85-5e7032ac16c3 | -21.042 | -48.46988 | 2026-09-04 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ffccbab-c4bb-371a-9fe7-08673672838f | -17.0973 | -55.95631 | 2026-09-04 04:42:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c84f8a4-aab0-31c8-b640-913c582738d0 | -17.24678 | -44.86457 | 2026-09-04 04:42:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaa6508d-2e83-3f64-bc3a-02e7eead589e | -17.10483 | -56.85167 | 2026-09-04 04:42:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0d10ffb1-6283-3b51-8b76-f677a8f3fd80 | -23.32714 | -52.31182 | 2026-09-04 04:44:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6dde3175-fd26-3a6f-af52-b3054944f8b0 | -21.91157 | -56.99088 | 2026-09-04 04:44:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7430612-8c61-309a-b007-54021e2ccb4b | -23.56714 | -46.83813 | 2026-09-04 04:44:00 | NOAA-20 | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b1c3f423-a2a3-366b-b9f9-82463478fec0 | -23.32774 | -52.30807 | 2026-09-04 04:44:00 | NOAA-20 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be4e68b6-bccd-3d4c-82f4-f27e93b1ea6c | -23.5676 | -46.8343 | 2026-09-04 04:44:00 | NOAA-20 | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c7fd91e-b3e8-3711-92a3-518c726b9fcd | -21.05752 | -55.84141 | 2026-09-04 04:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb729da6-1b9b-36b4-845c-9e367fac9979 | -22.02478 | -49.5703 | 2026-09-04 04:44:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 135aa7f2-2414-3555-aa68-3d11b47edeff | -21.89725 | -55.37334 | 2026-09-04 04:44:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8b43272-0259-31d1-9028-b53dc3c557bd | -23.0861 | -48.61462 | 2026-09-04 04:44:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 941758fc-eace-3d8d-8b16-c57a290a4249 | -22.84585 | -49.34842 | 2026-09-04 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2d66301-9d31-3c31-98ab-7dd9ed0c28eb | -23.27779 | -46.60303 | 2026-09-04 04:44:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 48d8ef0d-aae4-3e6c-a1c9-f9457851d563 | -22.84644 | -49.34425 | 2026-09-04 04:44:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4b10b8c-76c6-359e-8fb8-f0cfc86fa210 | -22.31303 | -54.87286 | 2026-09-04 04:44:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9b18a10-a2bd-3311-810f-b55b0ad1dee1 | -22.31227 | -54.87715 | 2026-09-04 04:44:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55a84b5f-58e1-341c-a337-fb417a1ca548 | -27.14677 | -53.09229 | 2026-09-04 04:44:00 | NOAA-20 | PALMITOS | SANTA CATARINA | Brasil | 4212106 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| eddd90d5-5078-30c4-9ef9-c697a61154b6 | -22.02133 | -49.56975 | 2026-09-04 04:44:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 868ec006-704c-3a37-882d-c9d5c3ebb83a | -22.32013 | -54.87428 | 2026-09-04 04:44:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bd4f949-b906-3429-87bb-3a52ac9af6a8 | -23.08248 | -48.61407 | 2026-09-04 04:44:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ec05e00-0b19-3534-b8be-410f5a606e7f | -29.64853 | -55.28514 | 2026-09-04 04:46:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d950ed49-054d-3be5-8f40-3591b39b4c7f | -7.566 | -61.343 | 2026-09-04 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 14fffdaf-852e-31fe-b498-ba3226c2dcdf | -7.5476 | -61.3437 | 2026-09-04 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| daafd34c-3e0c-3707-8df9-027da054f399 | -8.1126 | -54.7871 | 2026-09-04 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c82cb85f-4f74-3ebc-82a3-f1888f61ba28 | -8.505 | -54.6404 | 2026-09-04 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a1735901-b659-30f3-a714-a0de8b750ecd | -8.5048 | -54.6606 | 2026-09-04 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 189527f9-0d3a-355f-957e-c7cb383500a7 | -8.505 | -54.6404 | 2026-09-04 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 640982b4-5bc7-308a-8061-ca203c6f5f71 | -8.5048 | -54.6606 | 2026-09-04 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7e33ed5b-24d3-320f-a1b8-e7c69b017116 | -7.5476 | -61.3437 | 2026-09-04 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| f76c6257-690c-395b-8571-0dbf5eb94805 | -7.566 | -61.343 | 2026-09-04 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 1c1a5179-c093-3e70-8025-3daf1c376abf | -8.5916 | -67.1788 | 2026-09-04 05:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 04ebff93-211d-3a97-bc45-dff264422753 | -7.566 | -61.343 | 2026-09-04 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| db343f2c-0217-302e-b085-ce3ea596c55c | -8.505 | -54.6404 | 2026-09-04 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7d60c777-208c-30f5-9f51-714d45a9f116 | -8.5048 | -54.6606 | 2026-09-04 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4a490455-3302-375a-a74a-008e867954d7 | -10.51 | -51.3405 | 2026-09-04 05:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| bc05f797-d4c1-3629-8129-ad86cd475430 | -10.5103 | -51.3194 | 2026-09-04 05:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 2f1a3341-f6ef-3392-9f6c-81a2a030a7d4 | -7.5476 | -61.3437 | 2026-09-04 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 35a4511e-ba54-3c83-af40-d17f18b8c038 | -8.6101 | -67.1783 | 2026-09-04 05:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 550e30ce-f0b4-33d7-9d2b-f1adf96a40df | -10.4914 | -51.3212 | 2026-09-04 05:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 48976ef7-2d92-3369-870a-ec26f2c598fc | -7.5476 | -61.3437 | 2026-09-04 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 29026745-fbaf-371c-b746-02864163e517 | -8.6102 | -67.1598 | 2026-09-04 05:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3689774f-88ba-39c4-9e08-6efd7e6ecf46 | -7.566 | -61.343 | 2026-09-04 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 42eb3c67-c393-3975-810a-c2ce96f2af37 | -10.5103 | -51.3194 | 2026-09-04 05:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| b715a987-4ba4-3471-9a69-a9bd241b4aec | -10.51 | -51.3405 | 2026-09-04 05:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 08b19c4e-5d8f-3c43-9125-53f286be4e86 | -8.5916 | -67.1788 | 2026-09-04 05:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7ee45963-8a67-35a8-a5a6-2d803a3e54b0 | -8.5048 | -54.6606 | 2026-09-04 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 67f0f812-2b91-35d4-a4f9-2397534102d3 | -8.505 | -54.6404 | 2026-09-04 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9a4e37b5-585b-3c02-ab72-3b5622a4279a | -6.11826 | -59.94795 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c20066e-eeaa-3cb3-9126-00c70dc7461a | -6.57919 | -59.0055 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d294be-46cc-3028-8986-fee7c651d7c7 | -3.08007 | -61.08575 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4b6c604-909b-3463-9e07-fb7fff0234f0 | -6.67583 | -59.96999 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af4e0926-243c-3b9f-b271-404b3a93e2d6 | -8.11103 | -54.78112 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12762761-6b1b-3608-8eda-98fe4d52fd8c | -2.94678 | -51.29462 | 2026-09-04 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82b43e6e-60c4-3016-8984-8fbf3f855f18 | -7.01675 | -62.9824 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba238a77-ca8f-3a16-b32b-d89beb33242a | -7.73679 | -61.64906 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd7b2e8f-31ef-3743-85a1-5d464df88a1a | -6.15362 | -59.93913 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ffdb249-4988-3654-990a-7bf91842991d | -6.53124 | -59.93702 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 759a1c4e-0ee8-32fe-8421-687fe98a2445 | -8.10987 | -54.78971 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7fdb2f88-bd68-3144-accb-ad976630ae27 | -6.68357 | -59.96402 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7fc5b81e-55a1-39ef-afcb-c1acea236824 | -6.56905 | -58.5662 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae2c096-ae98-3852-8a90-a7c7e1e482d0 | -6.78308 | -58.9566 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af3dbbd0-96f2-37fe-b623-48c57bd434b6 | -6.44036 | -58.15763 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9065569-ec7e-39fc-935b-2bba0bc0c6a1 | -7.0881 | -56.51294 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ccf2a9b-4373-355c-aa9c-9188449ac082 | -7.09579 | -56.51416 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66de6f13-917f-312e-817f-b0ea1d2991ec | -3.34527 | -59.45528 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 699babbb-93d3-3d42-a5d7-0f704a999489 | -10.50034 | -51.33825 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 68cc357c-7e8a-375b-9493-3dcde201a812 | -4.36398 | -47.77433 | 2026-09-04 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 601018cf-4ed8-3bef-a2a1-10fabd7d98ae | 2.37749 | -50.761 | 2026-09-04 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb97d43e-02b4-328b-899a-fbb07c7f7b19 | -3.15956 | -61.1203 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d5eaac9-ff9b-3e52-88da-8b7bdc068e5c | -8.11161 | -54.77689 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fe5eb22-eaaa-3c9d-a0e0-37292b4b5842 | -3.0745 | -61.07765 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef28fa5a-7cbb-39ce-afc7-08c566f6be01 | -3.34249 | -59.45132 | 2026-09-04 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
