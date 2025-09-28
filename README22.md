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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8679d270-36db-35cd-8245-8b8bc58e57c0 | -13.80431 | -47.92785 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f762ff5-0300-36dd-aa21-ff02d6515f9c | -11.39058 | -46.97323 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f3b3aef-ccf1-36cb-891b-bf8504a3526d | -11.62844 | -44.42423 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 558f4b5f-f749-3bdc-88a0-8386c9ef1401 | -13.61077 | -47.32193 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9526baa4-0e1e-3bde-b7cc-4f7e262c8603 | -13.65189 | -48.07603 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfd35f7a-88c6-3931-9b53-4581ad464365 | -11.98846 | -47.99866 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c06a75fc-f07c-359b-9e28-118017756f83 | -11.72102 | -44.42038 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1f0557a1-c9e1-33f7-a189-1aa8470e9296 | -12.00467 | -47.04028 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77a6ee4c-9d85-3638-bd75-114ac49eef52 | -11.35121 | -45.00355 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79b6b2e4-5550-374a-9f6d-3fbb7c5028e3 | -10.91237 | -44.82249 | 2025-09-28 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 519f00bc-855b-33d5-9c49-9c8f4be079ac | -11.71904 | -44.41656 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49c9fb4f-0ef5-3e86-a84f-a83a0ac1b707 | -15.4352 | -48.23755 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cce326f0-f9f3-36c3-93b8-e975b809a171 | -11.65906 | -45.33635 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb6a41ec-c1f3-3cec-8726-86854d93a873 | -14.53912 | -48.41039 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85d37ef1-e4f1-3917-b828-6aabae6f344c | -13.6192 | -48.07044 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76165f42-d77e-3cc6-b8d5-42ae9520f436 | -13.0107 | -49.46147 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59542315-1865-335c-8849-9758cde6e535 | -15.58392 | -42.41042 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31a9be43-d576-35c5-9684-683f5792ea3b | -15.18342 | -50.09476 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 067c5b00-d005-3e85-9cba-5305bd295064 | -11.50388 | -43.54128 | 2025-09-28 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8824381-230d-323e-81c4-1f7adf095375 | -11.41464 | -46.95148 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea53eb12-5f5d-3638-85aa-2d5587dfbd14 | -12.99111 | -49.44945 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af47d641-20ff-30d9-954f-60712e80c0ea | -10.53854 | -43.62687 | 2025-09-28 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| af27eb61-132e-3218-a00a-b4a533e65445 | -10.54376 | -43.62777 | 2025-09-28 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22fff677-bae0-3954-a199-b046d9a2a0f2 | -14.53793 | -48.41588 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e324e4ff-105d-31c4-9036-c678c44ca96d | -11.99139 | -47.89851 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e7b89a3d-bca2-3aa2-9e9e-8b1f853faa15 | -15.22377 | -48.06165 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b56dad57-b152-367a-bccc-075a091db42d | -11.71838 | -44.42005 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 54876193-a687-3944-b4e6-04fb4ea9f652 | -12.9375 | -45.11524 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6a1b554-9f52-3fc0-afe4-606d2f0c58ee | -9.44706 | -43.70383 | 2025-09-28 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58240e66-f078-317c-a061-2e0502b118fc | -13.56438 | -44.10061 | 2025-09-28 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f4e770-b117-3f84-a43a-0ccf76656bb0 | -11.69022 | -44.42179 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c7e66c-4212-3437-a1d5-87f23dc49fb4 | -10.75389 | -45.39248 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00c88764-deb0-36ce-883e-176785071864 | -13.58195 | -47.3144 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cae2828d-d7b7-3d6a-afae-2e18033ac451 | -15.20462 | -48.05872 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93da3b21-3302-3f44-af55-55d927a0cfc7 | -15.21501 | -48.07154 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87d53af7-ec2b-3cd8-8ac2-7b2e2adce12c | -12.88402 | -47.09201 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d99e3d9-aade-332d-8888-63d6452bae97 | -12.91738 | -45.18829 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa601aaf-ecd6-3260-bbfc-e2927cd98e37 | -11.70294 | -44.41343 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebdf7bf7-0495-3841-bc03-edbd3edd4b04 | -12.92363 | -45.18566 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9947e61-5df2-350f-b95c-cd2a5202d1c7 | -11.99122 | -47.88713 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 21ba46f7-49a8-3080-bd05-951264972524 | -11.36198 | -44.9474 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 594ded55-772a-3eaa-adf0-c452b6617979 | -12.01409 | -47.9094 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3782456-cd05-3b8f-a61e-edce09a206ca | -11.51525 | -46.95508 | 2025-09-28 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a55caaa-4d6d-3adf-ba6c-b8d605ff862d | -11.99908 | -47.88249 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4521eaaf-bc8d-3a99-bfd1-c754bcb94b84 | -9.2157 | -46.77921 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 4ae17ac7-6bcc-38b0-ac18-6b0d45e7b8c6 | -11.99179 | -47.99829 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f77e3c71-dfa0-3738-acc0-74e767fb1cfd | -11.60458 | -45.43469 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edac2497-433a-3183-864b-24810197792d | -12.00776 | -47.0895 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ea10b33-864c-363e-b0b5-2cf718495075 | -11.97624 | -47.08321 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8cff1eea-b1a9-3796-8c02-8139a4c201c2 | -13.60054 | -47.31847 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fce5636-4b86-37c0-a193-d0bf1d72d8a4 | -13.51318 | -47.39434 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 994b95ef-3aba-3449-9a31-4780db490bf9 | -12.94299 | -45.11633 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f05cfec4-b6c2-3912-9422-4e9b0bc37175 | -12.98205 | -49.43975 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b398aec8-dc2a-37fd-81c1-e1c6827d2dd1 | -15.32998 | -47.89217 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df4e52c-0e36-3a05-a1d3-bcdb449f3410 | -12.25617 | -44.09668 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b31a67c0-c232-3956-b3d1-cce98452c0f2 | -11.69361 | -44.4333 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 973211de-1c2c-3460-a978-0fc6e3a89637 | -13.7998 | -47.91742 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47077362-42aa-38a3-9ca7-891bdffb93b5 | -11.99353 | -47.87617 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e50f044a-53ee-3acb-9eea-3cd55ad680bb | -11.64875 | -45.3368 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9219104-eebd-3e52-8d94-8223531924bc | -11.94165 | -47.93936 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ed56e09-0be3-33eb-a203-4f4df8a58337 | -15.33302 | -47.88884 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0b7dcae-7df2-32c9-81d1-45ee7baffa6b | -12.90126 | -45.15401 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67afad92-bd46-325a-b75b-4ac4731736ab | -12.89755 | -45.17264 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5860eb66-5813-3f0a-b00c-64af36cbf8b0 | -11.58037 | -45.49792 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b2ba9d7a-cc1d-3195-ba46-9d6c61718f98 | -9.06956 | -45.54362 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 101af3ac-9130-3d8d-8129-e3336617ab09 | -11.37142 | -45.01955 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c6d5754-eb44-3725-8bfb-4036c0c04c94 | -12.4202 | -44.11596 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56ef71c6-3d69-31f4-bcc5-bf5c5427f168 | -11.71969 | -44.41307 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2becfae8-1930-3ad6-a1e4-8d6cb82de1e4 | -15.19073 | -50.09521 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e10624a2-1cbc-38d7-87b1-590c0a22a8ae | -11.6715 | -44.46162 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e03463b2-7feb-3cbf-bb9c-c23eab45a330 | -12.69376 | -46.87133 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bb7aa52-5906-3f4f-83d0-0606a4d4654e | -11.68956 | -44.42529 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d09891c-ce45-3934-a703-5b783b30f64d | -15.90266 | -46.2176 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 275eae25-038d-331c-8c9c-d0e9d0b98a80 | -15.88377 | -46.20432 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eaa73a33-33b5-305d-ab54-798f9142cfb5 | -13.80493 | -47.92959 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5293ace-679e-3a6f-808c-efcbfa115549 | -15.97357 | -42.01344 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a44f5ab1-82fc-37b9-8229-e3d5879159f6 | -11.36055 | -44.95486 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d540a3e-307f-3417-9fa5-d5f0a65608bf | -13.40444 | -48.16109 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1a66298-613f-3b6e-991e-71f7661ea0ad | -9.67734 | -44.52012 | 2025-09-28 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6b48c9-f0aa-3754-967c-2dfc8946c475 | -11.51646 | -46.94903 | 2025-09-28 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| caf7be09-9051-3a71-9179-9fe81b8def14 | -13.60533 | -48.10368 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 34.8 |
| e6a7a79f-0012-3cf9-9204-cbf918e8da73 | -12.29703 | -45.64473 | 2025-09-28 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acf7c491-899c-3cea-9c2a-0e5b14b025ed | -15.44281 | -48.23303 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a9b31765-25fd-3658-9e37-baefc0551ab3 | -12.97351 | -46.28671 | 2025-09-28 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bbe26c3-ff4b-3e99-8c4a-a2190d13a211 | -14.5367 | -48.4216 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 85795faf-ebc0-350a-8300-7215be34f369 | -13.59268 | -47.32513 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f08a9bcf-9311-3c52-aaef-a157a2ef44e7 | -11.68882 | -44.39984 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 290e81dd-f87c-3607-adaf-d816f81c117e | -10.1189 | -45.6646 | 2025-09-28 03:38:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 52874b5c-5911-3d4d-a83e-5bed028e1cb6 | -12.69346 | -45.475 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| af5a1059-c211-3093-a6a3-546ec1873221 | -11.3595 | -45.05149 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ec1d106-761c-355d-b273-61bf23a7397c | -9.6511 | -62.8526 | 2025-09-28 03:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 74cdd5bc-7a01-3ed0-b20a-c33159373bdc | -4.858 | -42.9566 | 2025-09-28 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d72d8004-7a65-3560-b972-333827d5887c | -16.9667 | -53.6975 | 2025-09-28 03:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 867faaed-447f-353e-a96a-77b2e701fbba | -9.6512 | -62.8336 | 2025-09-28 03:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 92ed2349-ab55-3f63-a0bc-86bc405907d2 | -5.8187 | -44.4413 | 2025-09-28 03:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 37d12943-1c27-3317-afd4-492876641945 | -5.7396 | -42.8461 | 2025-09-28 03:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 52c6e422-da99-3e6b-bf73-d195a3f47e9d | -9.6324 | -62.8534 | 2025-09-28 03:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 73f8c714-39fc-3555-a66b-f6bfef335dde | -12.9918 | -49.4448 | 2025-09-28 03:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ff909808-40e6-3389-953b-39b2ea245e46 | -8.1799 | -46.4104 | 2025-09-28 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| ac30f24b-f5b3-3fe8-8e0c-541d8a4ca2f5 | -5.8149 | -42.8167 | 2025-09-28 03:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |


[Clique aqui para ver as próximas entradas](README23.md)
