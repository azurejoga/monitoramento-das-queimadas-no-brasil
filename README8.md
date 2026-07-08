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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 904a986a-4202-3a8f-b775-ee86b3e190a5 | -10.92933 | -43.0568 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0928fc3e-5d67-3811-a334-fe30697b573a | -14.73398 | -47.14818 | 2026-07-08 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 283022a4-3840-3f25-bd55-0bf2a0faad77 | -12.35104 | -47.42112 | 2026-07-08 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ee3efd4-582b-3255-9d93-e0f2395ef214 | -12.78974 | -44.46072 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| daca033f-da22-3292-b807-e78b0e4f56a6 | -12.85242 | -44.39166 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ea35b5a-40fe-3d0d-a7da-fce12eba3f2e | -12.79062 | -44.45636 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 47f02d9a-058b-3cba-b979-8b2cb7164b1c | -13.27576 | -45.17019 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c2dcbb5-f3c0-3409-a043-372e021f886d | -10.92592 | -43.04424 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68482f8f-baa0-3e85-8849-1597b0b2680f | -13.27474 | -45.17511 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 493c34b3-b615-3966-9f34-7c236f3f7e16 | -13.28087 | -45.17622 | 2026-07-08 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19ffc86a-7238-3edc-b280-a2e85ebf977a | -10.94589 | -43.05212 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b0c3269d-74e3-3712-8347-07726028f53d | -12.35534 | -47.42185 | 2026-07-08 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd166de3-580d-3977-908d-19001c80ddf8 | -10.94107 | -43.04723 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1a3ff6c-0229-393a-9dbb-80f2cb48c49b | -10.92375 | -43.05571 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d6951d81-7190-3fa8-b7f2-25403bb6fd35 | -12.78031 | -44.4771 | 2026-07-08 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b52e6e4-36e1-3564-a836-1f2486b03686 | -9.37299 | -44.72297 | 2026-07-08 03:32:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ee0cb14-bbfc-3681-91ae-d3c75f68eca0 | -10.94664 | -43.04832 | 2026-07-08 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| af5feedf-8ddb-3473-a741-f8b7f914020f | -15.76953 | -43.23876 | 2026-07-08 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3756e6e0-9178-39c8-a0e7-ec1d380e6e9c | -13.95948 | -45.21765 | 2026-07-08 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78a96802-b991-34fe-b621-13fedb913dc7 | -13.82256 | -44.05571 | 2026-07-08 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f5862b8-1169-3bd5-a1a5-aeceb05cdbc3 | -19.08806 | -40.08143 | 2026-07-08 03:34:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2415d9ed-8e0d-3efe-98d0-651f5554eb5a | -21.36281 | -49.16896 | 2026-07-08 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 52554b11-959a-38a3-9aec-3eab08f44298 | -20.39702 | -41.5931 | 2026-07-08 03:34:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fc29eff2-e974-369b-8f1c-b1c9c7e918e9 | -19.63582 | -47.58229 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b057aec-10c2-35ba-805a-1f09d6074408 | -21.42739 | -47.07627 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5318922f-79aa-3381-a9d3-e86d1f303513 | -19.09204 | -40.08224 | 2026-07-08 03:34:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b39b33ff-c1a8-30f1-a590-3147223fdf57 | -21.42838 | -47.072 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 932b9b95-a8b9-301d-a9ef-71c28a7b5b43 | -18.74285 | -46.9182 | 2026-07-08 03:34:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43460172-c07d-35dc-a02a-1e8e359c10d9 | -21.06484 | -47.25249 | 2026-07-08 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c8a1e67-cef2-3782-a43d-98d157e69526 | -21.36424 | -49.16318 | 2026-07-08 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e0b12d5e-92a4-3014-9ed6-ec54ecc9b5a8 | -21.4178 | -47.06437 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7532c659-f528-324f-8c48-84ed6dbbbf85 | -19.67451 | -43.13305 | 2026-07-08 03:34:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 528c16f1-2a3c-3e9a-91e6-338c6b8b7eaf | -21.41923 | -47.06667 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be9ec1c7-77f3-3fa1-8816-9c91c1eaadbc | -21.03876 | -46.79048 | 2026-07-08 03:34:00 | NOAA-21 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60b83248-1af5-317d-881b-57cff0b9aeaf | -21.42027 | -47.06205 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ece0e2-97b8-3add-97b6-d53ed351e253 | -19.09137 | -40.08588 | 2026-07-08 03:34:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 06150f8f-414a-3507-bf6b-518f05bdc898 | -19.68299 | -43.92536 | 2026-07-08 03:34:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c852b135-c489-3089-adb9-eb8e0ed9493e | -22.29173 | -46.85792 | 2026-07-08 03:34:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 200f8aaf-32b7-3f58-87bb-7bcea1b8198a | -21.41446 | -47.06046 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 200ea8fd-88e9-36f0-95e7-4f51e31247d4 | -21.17499 | -44.70329 | 2026-07-08 03:34:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26eae2d7-b254-3a37-8f29-c7e7db9aa6c6 | -21.17702 | -44.70422 | 2026-07-08 03:34:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 264251ba-21da-3cbd-8223-daa0c1e7d88d | -20.95921 | -48.64564 | 2026-07-08 03:34:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06f8aa6f-33ea-30cb-b6c4-b140db3f4d81 | -22.29071 | -46.8624 | 2026-07-08 03:34:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45186cd2-a49e-39ea-ae31-5260f53171c8 | -19.09535 | -40.08672 | 2026-07-08 03:34:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cbc8ff49-ed8a-32b9-86ce-99c5015ea481 | -19.73267 | -45.30776 | 2026-07-08 03:34:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab83a676-c296-3016-8086-98455d3e5541 | -19.62216 | -47.58447 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96cc7a3b-4d80-3ebc-92ef-f311e89b8dcb | -19.63462 | -47.58753 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ce18f10-9873-302c-b7d6-65d61a9cab1a | -19.63761 | -47.59013 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82a5d34c-42c7-3fb7-a2e3-aaf3cfaafaa2 | -21.06365 | -47.25764 | 2026-07-08 03:34:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81a25fd1-610c-3a69-8d76-ff12526d3038 | -21.36648 | -49.16541 | 2026-07-08 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 1d6da53b-44f5-3291-9093-f073ac33662a | -21.37073 | -49.16518 | 2026-07-08 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 95a81bc8-7c81-307e-9ff6-76edce5a653f | -19.63258 | -47.58353 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a7b198-3067-36ca-9dcc-9ac4cd2b9dbf | -17.98516 | -40.04972 | 2026-07-08 03:34:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a70b0a99-73bd-377c-911b-af5e4e3d3f5c | -21.3651 | -49.1712 | 2026-07-08 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6b07ab2a-aa76-3e9e-b2ed-8188499eff20 | -19.63136 | -47.5887 | 2026-07-08 03:34:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2daa867b-abf8-3c1a-b303-1460af5b0c7c | -19.08739 | -40.08507 | 2026-07-08 03:34:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e7f48eb6-f01e-3e83-9774-8da0e7cb0f69 | -20.9657 | -48.64708 | 2026-07-08 03:34:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 803cb6c4-0bca-3573-9613-e824fef7ca96 | -21.41887 | -47.05976 | 2026-07-08 03:34:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f2513aa-b148-3b6b-843d-cacc230be114 | -21.57143 | -41.26989 | 2026-07-08 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e8d70506-e2ae-33ed-9741-abcd5ae4afbd | -18.3711 | -39.95849 | 2026-07-08 03:34:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b3378d25-efd3-335f-b8c3-89d7eccc19be | -19.67339 | -43.13853 | 2026-07-08 03:34:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c477da3e-1272-3427-bbac-e46eea89da0e | -19.63346 | -47.59262 | 2026-07-08 03:34:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acd0ba91-bdc1-39a4-aeb6-bc7c577058c9 | -20.0369 | -44.27502 | 2026-07-08 03:34:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 995a7314-04ca-363c-b5c3-0dca115cc94a | -20.08454 | -42.18277 | 2026-07-08 03:34:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29f98a3c-e770-361f-98c2-09fe9bfccef7 | -19.63885 | -47.58489 | 2026-07-08 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d120f3da-ea2e-3040-92e6-b366988adb60 | -21.8033 | -56.2729 | 2026-07-08 03:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 3cc48f09-ca45-343c-b9a1-f394411e9fe1 | -12.7746 | -44.5162 | 2026-07-08 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| da899961-c271-3439-b167-e34409af41fb | -12.7953 | -44.4426 | 2026-07-08 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 521bddac-c4e4-3484-b967-102e01dcbd93 | -12.7741 | -44.5396 | 2026-07-08 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b7425dde-ebff-30be-8d5c-e798059d90a2 | -12.7566 | -44.449 | 2026-07-08 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| a44ae901-6918-3274-bda6-8ec158345940 | -9.2258 | -48.5782 | 2026-07-08 03:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 95226efb-6938-3b2b-9d33-ed3c1f85dade | -12.7953 | -44.4426 | 2026-07-08 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| ed891e54-971c-34ef-a365-59e61ae3c641 | -12.7553 | -44.5194 | 2026-07-08 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| edd240b0-84a4-33b1-bc78-2cd8234ea8eb | -12.7741 | -44.5396 | 2026-07-08 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c25503ac-33eb-315b-80b3-653b27922feb | -9.2258 | -48.5782 | 2026-07-08 03:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6b61fad5-7a5f-3f55-92cc-bf38b3c7a3ef | -12.7548 | -44.5428 | 2026-07-08 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 63005955-c85b-36ca-a801-fbb426b3ff89 | -12.7566 | -44.449 | 2026-07-08 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b8756198-1a93-3f4e-9eb1-4fd37b483358 | -9.2258 | -48.5782 | 2026-07-08 04:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0fc35f95-e463-3e38-8e46-1c4c11d72e01 | -12.7548 | -44.5428 | 2026-07-08 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 89f6400d-103d-38bf-b5e1-55ccf712df70 | -12.7553 | -44.5194 | 2026-07-08 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b792e52d-c14b-35b3-ab06-5aed2f7af0c6 | -12.7953 | -44.4426 | 2026-07-08 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c4e2ded4-fab4-3ca9-9717-520b7f488040 | -12.776 | -44.4458 | 2026-07-08 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 772d29f2-fdc6-324b-bba7-b71ab9228781 | -5.33865 | -44.71262 | 2026-07-08 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 53ffb884-1792-386e-87cd-0f46582f90a2 | -5.50377 | -44.08189 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96b06d39-c093-349f-9a3b-989bff6707ac | -3.51342 | -48.04129 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ed58137-a8dd-3561-b620-7dc98ff12470 | -3.50771 | -48.04025 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96b2e191-e781-377c-a54f-ea6fffef2737 | -4.57569 | -48.03223 | 2026-07-08 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7afc024-59fe-3bf3-b572-567952f7abf4 | -4.18794 | -47.84608 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27431dbf-206a-30c1-828e-4a28e8a3f28a | -4.83061 | -44.06085 | 2026-07-08 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1735f134-835e-32fb-80dc-d6903647afb2 | -4.18591 | -47.8442 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| becd7f7d-c008-3c65-9d7e-25408d55a360 | -3.51445 | -48.03953 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e86e5cba-16a5-3fdf-88fc-07c69ebd6ef5 | -4.83248 | -44.06363 | 2026-07-08 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 607ad42b-789f-3e77-ae0e-92241cc943cd | -3.50874 | -48.03849 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29d80923-b18c-332e-a69c-a5791a485097 | -3.49046 | -48.03789 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66f114f1-6336-3e41-8330-ed75eb24e138 | -5.30492 | -43.06238 | 2026-07-08 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df4bc849-53b2-3761-91ff-ca0f8781647c | -5.50866 | -44.07868 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff08657-e7ba-309f-baf9-5f4af98a1474 | -5.47902 | -44.07383 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dc9460f-bbd4-321a-836e-7e0e806c987b | -3.49624 | -48.03847 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda8c200-86ee-3c76-abb7-bc4f1c104600 | -5.47858 | -44.10175 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24b59b85-fba9-3594-90c0-6e36b6a71aee | -4.18231 | -47.84538 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README9.md)
