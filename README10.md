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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03d6c7c1-4895-381e-ab2a-bbd4e12d6e86 | -20.33863 | -46.55546 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea1ad966-4705-3671-b0be-a3fd09cc8b04 | -22.72356 | -42.08936 | 2025-08-22 03:34:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd4f319b-5fa0-3f8b-8020-5a8aa0d78106 | -20.08647 | -46.1271 | 2025-08-22 03:34:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 491bbc3c-b79a-3307-a17a-1172b993f3c7 | -20.40594 | -40.8411 | 2025-08-22 03:34:00 | NOAA-21 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 297a01bb-98a5-3742-9d01-38ab0af0ce60 | -18.59791 | -39.88619 | 2025-08-22 03:34:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b99b884a-0cb6-3558-954a-b84c76b39c64 | -19.58742 | -46.36588 | 2025-08-22 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4f1fada-fb00-3b7b-9ea4-be01c3c9bc2a | -19.58756 | -46.36278 | 2025-08-22 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc2e3a61-f4b9-3e37-9b8c-d9d882fc283a | -22.77875 | -47.08957 | 2025-08-22 03:34:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed2c111a-ed9d-3618-98ca-2a3c7b00f4b4 | -22.19441 | -42.87001 | 2025-08-22 03:34:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 966ecc18-f94b-3e84-aff5-3458dd8605b6 | -22.78504 | -44.78931 | 2025-08-22 03:34:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 734ab32c-8242-3372-bd38-1f09049c6fa2 | -22.7853 | -47.08686 | 2025-08-22 03:34:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e1b5ddf-3fd6-393a-ad26-dc3d5e5723f5 | -20.33938 | -46.55211 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cc04fbf-ff2c-322b-a356-3e86115b9479 | -20.43451 | -46.50869 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 241879ba-d82f-397f-8fc8-dbbcc3dc503d | -18.28306 | -45.52281 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae977774-6a73-3275-949f-a09f2eeb1dcd | -20.24313 | -46.6027 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 23d3b046-5ecf-3676-b7f3-5f529f64cce1 | -23.21061 | -44.90307 | 2025-08-22 03:34:00 | NOAA-21 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a60fd9ca-f606-3e2d-8a6b-5b7a0dedc82d | -22.07502 | -47.32477 | 2025-08-22 03:34:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0f0b78f2-6261-33cb-931e-ab4c014705fa | -18.9398 | -41.48926 | 2025-08-22 03:34:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6478c2a3-9d5d-33c8-8f13-648a978d671f | -20.2355 | -46.60974 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af51e932-a8d6-3d6b-a1b9-8b72560dd035 | -18.26761 | -45.53989 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b3f28d3-cb6f-3eac-b0c6-12db4c8af323 | -21.41172 | -47.97137 | 2025-08-22 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b5893f2-c610-32e6-9de4-23d591b11a3d | -20.35161 | -48.3452 | 2025-08-22 03:34:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c9c4a3a-af12-39c5-86cc-45a856a6d224 | -23.29279 | -47.47314 | 2025-08-22 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 26a97b0f-3fa2-3f04-b5cf-473cc485b6c6 | -20.30322 | -46.63157 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a76bf5-7dc7-3259-84e0-0659ed64899e | -22.55744 | -42.13367 | 2025-08-22 03:34:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1c75ed75-5c64-31a5-8b20-ad4f6b907bbb | -22.6995 | -43.74496 | 2025-08-22 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1089113f-4d86-36c6-be1b-2bd546df84a7 | -20.26554 | -46.69228 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b05d1f-684c-3cae-95f3-5148776ab1b9 | -22.5572 | -49.76781 | 2025-08-22 03:34:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b4b794b2-6ef5-3957-9773-8a67ff4aba89 | -20.24209 | -46.6073 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 59c9b104-7ac6-3584-b816-e4cb2a183098 | -22.78592 | -44.79272 | 2025-08-22 03:34:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4ba30baa-8d60-3212-93d9-06787af4db93 | -23.29948 | -47.47029 | 2025-08-22 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| a0b87519-347e-33e1-aaad-4b7fff796587 | -21.41056 | -47.97636 | 2025-08-22 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7b0e21d-3fd6-3aa7-8f7a-ce33af1b7555 | -23.29381 | -47.46882 | 2025-08-22 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ab17d050-6fec-3b38-abc0-08863e42f6d7 | -20.30227 | -46.6359 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a553a3c-c297-3be6-8e9a-86cef789bea0 | -23.5872 | -45.68339 | 2025-08-22 03:34:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3163008-cf80-3d9b-9448-e0b82a240a15 | -21.41165 | -47.97164 | 2025-08-22 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e282bd5-9054-3aa0-b92e-1119bc893c6e | -17.34969 | -48.17278 | 2025-08-22 03:34:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a605e9b-ffcb-39a3-b573-49685778af19 | -23.29847 | -47.47461 | 2025-08-22 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| d1f2a2b9-4a64-3c5a-8e62-af61c26c882f | -18.75241 | -43.84524 | 2025-08-22 03:34:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eacc492c-fc20-3b4e-a4fd-44066ff05c85 | -17.39232 | -44.25447 | 2025-08-22 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d8f0e5a-c173-3fa0-b6eb-ddae124ec157 | -22.89924 | -43.49261 | 2025-08-22 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ed5d198-bb89-3d5d-b707-7b42e3491e02 | -16.78277 | -47.66639 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77ec9961-b277-3c32-8a6f-d97c831abdf9 | -22.72771 | -42.09028 | 2025-08-22 03:34:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 24d9d08b-986c-3aa0-897a-9381ac7bfe8b | -19.48164 | -44.26749 | 2025-08-22 03:34:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22c5bdec-bd75-389d-8250-55a840056be5 | -18.87808 | -45.01926 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1d35a9c3-3668-314a-9199-88203535241b | -20.43974 | -46.50579 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5599e341-6d4f-3d08-a588-e23697285c3f | -21.59558 | -48.98779 | 2025-08-22 03:34:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d65d1e1c-f5d6-39ed-b1ab-61b2cfad179e | -18.8827 | -45.02404 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b3344921-8f8f-33eb-bc97-1ae21190bb1b | -20.08409 | -46.12561 | 2025-08-22 03:34:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a41a5c3-9838-30e5-aa0a-3bdcb3af04f0 | -21.32011 | -44.87408 | 2025-08-22 03:34:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c05078b6-4b6b-3eeb-b3ae-b39eb426f92d | -20.43674 | -46.49891 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a481f2b-2ceb-3276-a957-34b9b01fce3b | -22.19071 | -42.87015 | 2025-08-22 03:34:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 08c2dfc4-44a8-37b5-abf9-2004fc5d1169 | -23.03466 | -50.07023 | 2025-08-22 03:34:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4952dcc5-074a-383b-8c92-8a738dc68aea | -18.27359 | -45.51238 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7dce87-494d-3998-b98a-07a4844210ba | -16.7855 | -47.65413 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17c90558-1673-3537-aea5-fa1573e45ec0 | -17.60916 | -46.69689 | 2025-08-22 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e21ef23-ed93-3920-a5fe-2350fe3568d4 | -20.35791 | -48.34691 | 2025-08-22 03:34:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3aedf04-b2ba-33c5-bbb4-e4cad34dbb9c | -20.35994 | -46.51424 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85ac3011-25a8-3eed-89ce-23bb4f05ae75 | -22.717 | -42.10072 | 2025-08-22 03:34:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6c4ce7f-cd53-3dd1-85f0-f2d700f0fd83 | -20.0832 | -46.12954 | 2025-08-22 03:34:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a856bbe9-23a1-3e5c-8b51-94f31417a3b0 | -20.22982 | -46.60808 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 291094fd-993d-3bfd-b606-18ed85d11aef | -18.939 | -41.49354 | 2025-08-22 03:34:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 568bec3c-f961-368d-a201-7002f9a6fc23 | -20.2714 | -46.69326 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9829f4da-dfb9-3ca6-bc75-d7f248d72a2b | -20.36674 | -46.51069 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5a8d1ca-36bb-3af9-b294-150a11c2eabb | -18.27107 | -45.52398 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f251d7cd-a35a-3997-98a2-5999525a44f7 | -22.1951 | -42.87114 | 2025-08-22 03:34:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67266046-2f95-3066-a76e-1462650344a3 | -20.2729 | -46.57759 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a93dbbd-205f-31e3-876a-4ca5c314abd7 | -19.93651 | -44.57539 | 2025-08-22 03:34:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5fc1fa83-7a4c-340b-8e2c-7f32721033d8 | -21.42994 | -45.96838 | 2025-08-22 03:34:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e706b92d-8604-3a4a-a731-83da16c4b943 | -20.7539 | -41.88821 | 2025-08-22 03:34:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cc53e98c-4397-3103-9038-579162cc9db0 | -16.78312 | -47.65863 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 738ff3cb-c2f1-3585-8d41-3e06454cb88d | -18.61655 | -44.26595 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7faf8df0-b6c1-3e33-8cf5-b9bb75f5111e | -21.41059 | -47.97609 | 2025-08-22 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e9e1a32-5b94-3dca-b477-0b0d9ac8f89c | -18.75184 | -43.84798 | 2025-08-22 03:34:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8d55ca1-18c1-3deb-98d4-c6497dc2cb59 | -22.66669 | -43.65315 | 2025-08-22 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4ae56c80-c902-3934-a4a3-adf29637192a | -22.69362 | -43.72692 | 2025-08-22 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ac5b681d-c9c3-351c-be47-6a22f5070d73 | -20.4334 | -46.50741 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53436957-2b30-3084-990e-759bb530cdde | -18.29193 | -45.50893 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f33750dc-625b-3be6-82e4-e131d34127cc | -18.79624 | -41.45886 | 2025-08-22 03:34:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8c0d3cc1-91a6-3c81-9130-4b789cd3efc4 | -16.7892 | -47.66824 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2d24a25-a6ef-3714-99aa-252925d128c8 | -20.26636 | -46.6886 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5c20010-9aac-3760-85ed-d39c3725f548 | -20.36076 | -46.51058 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cef4322-bfdb-3247-aad5-4bce136f64a4 | -20.24283 | -46.65803 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b068146-2d06-38aa-a55e-5410f8360f27 | -20.148 | -42.13934 | 2025-08-22 03:34:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2998eaf7-bdf0-3ebb-ba2e-ac21ccb29025 | -18.75125 | -43.85082 | 2025-08-22 03:34:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5422f9dc-8d4c-3cba-b91a-785a9cf6b321 | -18.26113 | -45.54266 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6aafd68-2ed8-3907-9def-a38e1b904623 | -21.89828 | -48.16838 | 2025-08-22 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 293fd22d-ff50-3f6d-b53c-512be733f209 | -18.88416 | -45.01708 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| fbee87f5-2203-3783-9933-5f63ffd26ba2 | -19.58661 | -46.36712 | 2025-08-22 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0580d39b-12c4-33e2-8765-b5d93826dcba | -23.4768 | -46.22449 | 2025-08-22 03:34:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a1a0ba47-440c-31a0-9e33-ab0e2ae6c99c | -18.28345 | -45.54817 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a184f12-d2d4-379b-bfd7-5b3cd056edef | -18.87733 | -45.02283 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ce216009-2d7e-3080-a624-8ea6a78bbf7e | -18.6158 | -44.26324 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1d69dd83-abcc-392b-85c9-16fcfa607233 | -19.89905 | -41.96906 | 2025-08-22 03:34:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 016be914-5b2e-31d1-9eef-1c0d159dc66d | -20.43565 | -46.50372 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4444e82-8257-316d-82d5-33bfd5d18f3e | -18.6224 | -44.26374 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c87cc5c7-ffad-31db-9988-664a947bdb11 | -22.66213 | -43.652 | 2025-08-22 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 51ef41e3-9870-3072-b0d3-fa8d3d95fb2b | -20.26774 | -46.57369 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0046c51c-ed74-3605-9d9c-ef904c15e992 | -17.39834 | -44.25196 | 2025-08-22 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66b2bf55-d052-3d93-bd2d-35495df78142 | -20.30198 | -46.63719 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
