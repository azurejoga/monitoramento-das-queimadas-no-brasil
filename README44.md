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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d8ca80a-6fc1-3a6b-80a0-9e94835dee7c | -11.6588 | -43.59124 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08658356-18f1-3819-be38-48d09a5eb5eb | -13.02703 | -42.67531 | 2026-10-02 04:17:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 88af184a-da3b-3105-8065-1ce195844115 | -11.76127 | -43.5461 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 344ee5bf-c99e-3c64-ab0c-d053e2c055e0 | -11.74011 | -43.57163 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc1ccc81-6716-3c0f-adfe-898dab20ceb1 | -12.86054 | -43.81165 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51a395cf-7923-33bd-85d1-22ad9f24727b | -13.34813 | -43.86333 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1d891af-e752-3f6a-b9f0-79867a4d4b0d | -11.43404 | -43.40546 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 991695d2-4662-3c87-a73f-fd7ebf3495fc | -11.34787 | -43.36956 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70cde2b8-62f6-38a5-adf7-aa7c498584d0 | -10.70377 | -50.86251 | 2026-10-02 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96de7b85-8897-384a-aadf-09cc3b942410 | -11.41745 | -43.40273 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 782b5c54-9a5a-3d00-8a78-18d3dc53714f | -10.21947 | -45.3078 | 2026-10-02 04:17:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb6d99cf-c47e-3ba6-9dbd-3bce3b3a9779 | -11.75674 | -43.44787 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acd5ae6f-a267-3f2e-92c3-cd7d08760178 | -11.74157 | -43.52146 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 214b5b77-e353-3000-bd5b-c19b7bcc1182 | -11.78776 | -43.57209 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcd2610e-a704-33d0-b407-1e93ee37f517 | -11.74286 | -43.57571 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 269c45f0-0439-3858-81b3-a14fa3caf02e | -11.311 | -43.57729 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eefe587-11fb-3591-89c9-66c5a98659f6 | -10.89676 | -51.1881 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2056f060-0075-3b37-8c90-5bca8a3d1dc8 | -11.21148 | -44.84479 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f84c2438-2581-36cf-9861-643afdedc240 | -10.30292 | -44.63109 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bda38df6-b21d-308f-acb9-00d6d3a61e01 | -11.76669 | -43.57595 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d3220c9-9965-381e-8a97-cd84f96de9aa | -14.873 | -40.7006 | 2026-10-02 04:17:00 | NOAA-20 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| cca266e3-7f6b-3807-9650-7aad632e249b | -11.73021 | -43.44349 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a0ef6fa-c7d9-3ae1-a678-cee4f7ec2dbc | -11.71144 | -43.43316 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8716f8e-21b6-358e-964b-74e2a4f4917f | -11.7739 | -43.57352 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4b05cd-b999-3d81-b180-69bd74c5e395 | -12.72474 | -44.73466 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eed0454-6caf-3646-aeb9-d133095399e1 | -11.71475 | -43.4337 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36d2509b-ad5a-39cb-87d4-5002c091a379 | -11.10745 | -44.60396 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d3ef7a8-e201-37cd-96e8-b9c43c50c132 | -11.13322 | -44.6196 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76076326-31bf-3f4a-b44e-25f99cae2034 | -11.4531 | -43.4121 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68f80ca0-715e-328a-b788-43e5be8df750 | -11.72689 | -43.44295 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06463892-5303-39d2-8296-6ee38d39fa9f | -11.24171 | -45.19764 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4158dbf4-9d60-3021-bf70-f074959157ae | -16.8596 | -40.58187 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5ce84d3-2bf9-3698-9830-cc093c1cdae8 | -12.47684 | -50.5125 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7be68525-8349-368c-8b3f-c30baf6ac511 | -12.98532 | -51.28063 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ee0edf4-2e46-3706-bf59-bd335603775b | -11.65765 | -43.59832 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b79005b9-c4bf-33bd-a138-a464fcc772f7 | -12.72692 | -44.74263 | 2026-10-02 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b5d8f22-a887-3ed7-a0a6-a210b27700de | -11.26541 | -43.56596 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 097fcaf8-af72-3bbc-b426-e5b017e688f6 | -11.46353 | -43.43192 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26e6ef4a-0f85-3467-b0a2-f630fabdcdb4 | -10.09938 | -48.41218 | 2026-10-02 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 226e161b-5bb6-36c1-ac61-a228c81c48df | -11.13009 | -44.61541 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf9d71a7-f2d1-3817-a713-2cfc1762ac4b | -12.53378 | -43.09112 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b41cc755-06ee-3a69-8166-91b9cedea12c | -11.14592 | -44.60635 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 887fb138-6c13-3f25-b6a3-c996e0dca993 | -11.69307 | -43.6114 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 363f9627-d60b-346c-93db-e15ed4281bbb | -11.79382 | -43.57675 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e41f331c-10f3-3cf8-aa08-10d53d08f339 | -11.41802 | -43.3992 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c86913f-96b2-3138-9333-026a569033bf | -11.14314 | -44.60205 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fe7c8963-bc76-390b-9914-8c2c375800b6 | -11.74403 | -43.44215 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32532342-81d0-3249-b818-381c65e2c132 | -14.33051 | -44.74474 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99e144b2-d4fd-36da-bac0-4901151617dd | -11.23595 | -45.2326 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e567f22-ba99-3fc0-957f-ae84dc6779d5 | -13.86024 | -43.6359 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4e693bd-7ade-3100-a177-84f560c32373 | -15.25158 | -46.1706 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0126acd0-e0af-36f7-ad7d-56f995f742eb | -13.85306 | -43.63833 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab56f48-818d-3370-ab48-6dfb7a449de3 | -11.44646 | -43.41101 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e167d991-03b3-3aaa-ae7d-ae905e0c94e8 | -11.10466 | -44.59965 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbd12507-e4a6-3f27-a9e8-84777815dc31 | -11.15708 | -44.62359 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e2e30298-bc25-3847-89e9-b96c760795cb | -11.74343 | -43.57218 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebd10535-98be-3ed8-b8c5-0bc0552fda4b | -11.74735 | -43.4427 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5af3f24-df25-3c46-8c02-4ea69ee37ff4 | -11.7501 | -43.44677 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1657d298-a306-36cf-9462-1419a6b207e2 | -13.85581 | -43.64242 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc754a6b-70ce-309b-8452-043124b3da9d | -11.75283 | -43.57735 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d5cc35ac-1033-3023-a59f-8a410ae53fae | -12.56469 | -43.0673 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed313a7d-69a0-3502-a998-e66db65bafd7 | -16.86021 | -40.57742 | 2026-10-02 04:17:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cf505cc-88cf-3bdb-90ac-4411d75fe05b | -13.78946 | -45.23926 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eb43cbf-44d7-3e85-9a83-46a6258309d0 | -11.71532 | -43.43018 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df70d070-eba8-39ca-b8b7-2525ab5bc06e | -10.51436 | -50.85927 | 2026-10-02 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ce35c53-c672-3869-895b-f3b814e3d4f5 | -10.90877 | -43.84026 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 456866be-6c5f-38bd-bb0f-29dc32a06746 | -11.69421 | -43.60431 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 4c7165c0-a740-3a37-a774-0acb4e2aac18 | -11.70812 | -43.43261 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9750f7-14f8-3187-ae9d-682b20c0637a | -11.14871 | -44.61067 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| c60c50e8-54b7-3c44-8379-b61828ec9b81 | -11.39367 | -43.40243 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f925e89-cf8f-3d19-9bae-108e21fe9da7 | -11.46742 | -43.42894 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 565c1d14-7b10-38f9-98b6-ac18daab4bb5 | -13.35145 | -43.86388 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6118a762-f12c-3efc-8590-d82264cb0d7c | -11.72802 | -43.43589 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07e66fb9-c702-33c6-ac96-e09bfec5bf1d | -10.30511 | -44.63924 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 185d917b-b7a5-3175-b69f-2ba684f9a648 | -11.77616 | -43.55944 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67964c6a-5997-36b1-8ef3-8318c9f328c2 | -11.70838 | -43.51598 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e065be9e-db17-30b8-871a-6842b84167d5 | -12.19019 | -47.11829 | 2026-10-02 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c22bd9-f370-3280-a8ea-566a31ca94bd | -13.33096 | -43.86411 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d3dbfdf9-1c43-3d81-ba52-577c046a11fa | -11.64456 | -43.55258 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0847af56-451f-36c6-b557-617f27ef8a1a | -11.65547 | -43.59069 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e78da67d-b3f6-3cc6-baac-98753fdeddf2 | -15.39938 | -43.00414 | 2026-10-02 04:17:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b7e5cbd-c172-3487-9668-afecac1eec66 | -11.78612 | -43.56107 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f67ff9e-6c38-329c-a9a4-38a32dec5426 | -13.85968 | -43.63944 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f1ae6bc-c463-3612-8277-40b3a8194c43 | -12.51113 | -43.10547 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6176b142-92e2-3d5d-b325-2d74d53656c3 | -11.26672 | -43.51535 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1905a160-7a52-39cd-8150-66f4d6fc0808 | -13.34321 | -43.85154 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62954654-fad4-39ff-82db-3d9ed285e342 | -11.24518 | -45.1983 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 755e8ecf-3a44-3040-85da-21093ac917ef | -11.64779 | -43.57489 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75333c72-0b07-3452-9635-bee14aa4f9a1 | -13.85637 | -43.63889 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e177e90-bee0-3f5a-90e0-15a34f8a1314 | -12.52772 | -43.08651 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ceec9ed7-3057-3f0e-b5d7-61077d43d235 | -11.67095 | -43.60051 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a842ceec-3511-3514-bcce-ec25a6196f45 | -12.51719 | -43.11008 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1b3ee96-6a03-3a56-b120-b489c597905c | -11.72414 | -43.43887 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bca33dbe-d1b2-303f-a0b7-b02858e25370 | -10.26182 | -49.66743 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a3acd647-3e55-3033-8ed0-c434230f93c5 | -12.98772 | -51.28176 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6c34dc44-5a2e-3fa1-a27d-e2f81bfd1e4e | -11.72858 | -43.43237 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 524ed520-b32f-3ad1-a2ac-1d2aec9eeba9 | -10.76253 | -47.70718 | 2026-10-02 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38c647af-8cde-383a-bde2-e0db660a5de6 | -10.6076 | -48.04277 | 2026-10-02 04:17:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d631274f-20e6-3fc7-83cb-763406636d13 | -14.02938 | -41.59779 | 2026-10-02 04:17:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 46020df5-afe2-3fdd-96e9-0c4088f4cba6 | -11.62736 | -41.83183 | 2026-10-02 04:17:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README45.md)
