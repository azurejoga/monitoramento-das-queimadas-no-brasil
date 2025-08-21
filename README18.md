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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f46726-4d0f-384c-a6de-f2841937a17b | -15.50956 | -48.04673 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb23f522-3c85-3ab6-be3d-6c29396ea20e | -15.37469 | -39.1754 | 2025-08-21 03:51:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6a8de51d-ff5e-3f79-8356-dd919ddd9270 | -18.6683 | -46.97507 | 2025-08-21 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cd031dd-8f71-3cef-98c5-67f47665e062 | -14.86104 | -47.94474 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b3deb08-1e65-3f26-8f6b-b253f14db331 | -14.85661 | -47.96121 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e7d1d6d1-0527-3fc6-bfa0-3e7d4cdc62de | -16.10467 | -48.00461 | 2025-08-21 03:51:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc146ba3-abf1-3033-95c6-bc0c627cf869 | -14.90032 | -48.07218 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e98a23b-1935-3a69-8c2a-784dd0141829 | -13.49272 | -47.06079 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27aadb3d-e221-32dd-9c3b-7e44b37d26b5 | -16.5084 | -46.73518 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be8231c7-8fcb-3f02-8296-4d2fe33601b3 | -14.8547 | -47.94956 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e88bd6c-d9d9-3d40-a780-609a89efde84 | -14.84517 | -47.93717 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8db9d5a6-d956-3df1-8ca4-405cbd1191cc | -14.4721 | -48.36627 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c88c44a-14e5-366f-84d9-1e8cc8a2c0c5 | -14.85261 | -47.95992 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d5eb1206-2bd4-3688-93b7-7b3852e55ae0 | -19.93001 | -43.60986 | 2025-08-21 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d0cae64-8017-34bb-a751-1a63cda85797 | -14.84715 | -47.93377 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62e03cf1-11d4-3c21-9df8-afcff121116a | -14.85345 | -47.94982 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fddc788-2023-3bf9-ac1c-888a4668ae53 | -13.59 | -47.01104 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8600c461-3e1a-3f7b-aa99-2a12be2bb2a9 | -14.84897 | -47.94527 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7895563b-1f31-30d5-ae81-1289fd9e9e6b | -14.85667 | -47.93982 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 41a5aa3d-d087-395b-a97d-0bc6b535c4be | -14.88639 | -48.06062 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d5f8d2a-69d2-3e9f-92ef-9b510f9bdfee | -13.48443 | -47.0498 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31ce9018-a72b-3c57-892b-5459825e367b | -15.9349 | -46.92751 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc39b3a7-96f6-345b-a974-08913211c722 | -14.88064 | -48.06235 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 256f83d1-95dd-3a86-81ab-0c0204dae5c7 | -16.09965 | -48.00337 | 2025-08-21 03:51:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 167f10db-afbe-3752-951c-327b8fc7532d | -20.05958 | -45.38758 | 2025-08-21 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc0f28e-c78c-3f2d-b515-a6fcb4e00dd9 | -14.84643 | -47.93071 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c653683-7d7a-34e6-8883-fcaacb26a4bf | -15.88429 | -49.01523 | 2025-08-21 03:51:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 737bb89f-1c52-3799-b86d-6a17c6acb8ac | -16.21514 | -42.36712 | 2025-08-21 03:51:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5baff60d-7d07-3a21-8aa7-5d8aedd52536 | -15.15219 | -41.28629 | 2025-08-21 03:51:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf0f6761-84cb-3ff8-93e1-1e73fdcdcc95 | -16.00451 | -43.70863 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9113f5a1-74b8-3de9-b7cb-45d8dd40c24f | -13.38246 | -47.50127 | 2025-08-21 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 833af55f-6f87-33fe-92b6-7cea663e5afe | -14.8533 | -47.95649 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 590c2073-b404-37ed-8750-89928a74eb4e | -13.53835 | -47.0379 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1fd4aa7-7034-3d8a-ab78-6bb3b9165b33 | -14.85537 | -47.94623 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a2e1bdd-44cf-3346-a372-a4df450f360f | -16.31822 | -47.11982 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cce5d7bf-ee33-3115-8f24-b8a3c2865a36 | -13.38913 | -47.49439 | 2025-08-21 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acac5d88-75a3-33b3-a66b-0ee78151e1c3 | -16.10404 | -48.00779 | 2025-08-21 03:51:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 111c54c3-d0d6-3bd6-930f-2b5cf6cf90a3 | -14.85277 | -47.95334 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f7c1cd78-6c09-3bf0-bf25-7c7e764c5866 | -15.05016 | -42.46771 | 2025-08-21 03:51:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4fd69bfb-15d9-3d68-a42f-66a05c47b0fe | -18.29822 | -45.5232 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85844763-c888-3a82-b862-6ccc849bfcfe | -17.58111 | -42.27097 | 2025-08-21 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9eac011d-0b0e-3f47-ab04-b91330f5c921 | -20.08247 | -46.13435 | 2025-08-21 03:51:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8c084c1-e24e-3211-9638-f419763f402e | -13.55049 | -47.05547 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ea3491f-876a-3459-b4fb-edca591067d0 | -14.47151 | -48.36921 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 681b2da1-a805-3c72-80f2-52a0afd62d56 | -13.55505 | -47.03178 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72825cd2-ae3a-3e5d-aac6-e57145678731 | -18.29336 | -45.52615 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb5c36a3-2a77-3a0a-98c0-140a0f2f68ca | -14.84508 | -47.94401 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45524da6-7ad8-306a-962c-eca6969cc4fb | -13.63105 | -46.88334 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7833dbd1-065f-39c3-9621-dffbfcce3ac1 | -14.85476 | -47.94307 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f5b088f3-55d8-3e24-bcf6-61eeca57dc3b | -20.22799 | -41.33799 | 2025-08-21 03:51:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4a42fc8-1bfa-3763-a40c-210ee561665c | -19.81089 | -41.90221 | 2025-08-21 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1113aefa-b93c-3a02-b264-d92e5e578de3 | -14.4701 | -48.3762 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85ffdaa9-c2c9-345a-8225-3076d73ae419 | -17.82289 | -44.42556 | 2025-08-21 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8fad964-a8e5-3e3a-aae1-f00ab4c56701 | -20.74665 | -43.48361 | 2025-08-21 03:51:00 | NOAA-21 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dcf15ea1-d204-30fd-9ddd-67f5c8bf833b | -17.81897 | -44.42486 | 2025-08-21 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fccc1fb-6dfe-3a9c-a2d5-4cc9f871ea92 | -14.93144 | -40.92111 | 2025-08-21 03:51:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 32f67f63-8684-3729-9594-b5d310333965 | -14.50329 | -45.95395 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f22b3236-712f-3082-8ae7-4f5cf923c4e0 | -13.49594 | -47.0693 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6b62877-e24d-362e-8e73-95600c8842ae | -14.85537 | -47.93991 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7713f281-6a8c-3e25-b7a2-cafe0129ee45 | -15.50507 | -48.04251 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ee247d9-925a-3a11-9e3a-f2f9ff68ac27 | -14.49684 | -45.96298 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba9eed65-6122-30de-bdac-0978b33a1125 | -18.30083 | -45.53214 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61e8a369-340a-3b67-8d91-4612d04b829f | -14.12512 | -45.38528 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e823c8c-0ee2-34af-9e58-04758dd3f1df | -21.31681 | -44.69657 | 2025-08-21 03:51:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c7639a1c-cd95-3d63-a37e-102468b385a6 | -14.85979 | -47.94481 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c2943151-c222-3efc-874e-45cb4f103d63 | -14.49414 | -45.95234 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd5bb520-d511-3e3a-bbbe-d153879959c4 | -18.28849 | -45.52913 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 966935a9-ecb1-3fa2-8ef4-db6b8fc3d14e | -17.59934 | -44.43108 | 2025-08-21 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1ed75e4-1281-3961-b672-175e043dd6b3 | -18.388 | -49.35546 | 2025-08-21 03:51:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7e0b2073-324d-3d69-8dac-126bbd5e4fc7 | -17.57689 | -42.27444 | 2025-08-21 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3b011c17-023f-3d98-9fcb-447bd1dfe2b7 | -19.78023 | -48.01435 | 2025-08-21 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fff2e69-5189-3c76-b679-75ac2a96086a | -18.28925 | -45.52511 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa2b60dc-2fe2-36ae-aafb-1ba42caae1f3 | -15.43171 | -46.71495 | 2025-08-21 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38531b09-ea9b-3a9c-80f7-f6c368228785 | -14.12593 | -45.38081 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02c713bd-418b-3446-b766-8ad4626545ad | -14.86043 | -47.9415 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 96d1191e-53d5-3ba9-a7db-4f002e49e707 | -15.32018 | -41.99275 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5d5c39a3-1a47-3ebe-8168-cd606b0bf3e8 | -15.8638 | -48.77359 | 2025-08-21 03:51:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de17edab-4699-30af-901f-2f55a392cd4b | -18.29076 | -45.51716 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b03fdf6c-039c-3bbe-b448-4dbc60ef3f74 | -19.29223 | -48.43763 | 2025-08-21 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 157c4693-afc4-3ca7-822e-9b13d5d7192d | -18.28664 | -45.5162 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecb804b9-c554-3897-b5b2-d6dffaee8fef | -19.77551 | -48.01332 | 2025-08-21 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af767b5a-8db5-30c0-9915-575a354d01ae | -15.7483 | -49.96161 | 2025-08-21 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ad3047d-a87e-33eb-9557-b94e7b47350a | -13.49658 | -47.06783 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4a268a7-2299-3933-ac88-a385ecb3b71c | -15.50821 | -48.05343 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c42bf9c2-be4a-3436-986f-80d94e7448c8 | -13.47888 | -47.05177 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4caa3d88-22a7-349b-b0db-682cb5d46f9a | -14.85092 | -47.93521 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76b6e73b-9fbf-3a6c-9f7c-0c1fef1c3585 | -13.54163 | -47.04769 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0faf3e5-8cf7-384e-8574-04906d7026dd | -13.38854 | -47.49749 | 2025-08-21 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cebc525-fde4-3231-88be-b47875291c90 | -14.89503 | -48.07159 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 221453fa-107a-3eea-a8fc-0251f86a89db | -14.8579 | -47.95455 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6428e372-8559-3948-bad6-f6940c9a57f7 | -15.31734 | -41.98794 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a78968d-8264-3992-aaec-3bef77eb8637 | -19.09358 | -46.6889 | 2025-08-21 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d016a63-0583-35af-bf2c-876c8cc0ca10 | -15.50572 | -48.03927 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d3523a-0f27-3c3e-8d10-b260dcf69668 | -14.85225 | -47.93511 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c86a337-19e9-31c5-83a7-35069c4790ee | -19.96013 | -44.85873 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abf4853b-1a58-3dc8-8016-8c2ae468f061 | -17.58391 | -42.27573 | 2025-08-21 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e75201e3-09bd-35c7-8b3d-439ccfbac656 | -15.74247 | -49.96129 | 2025-08-21 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edaf956f-9b3f-35da-960d-3506c2a6e82c | -20.05888 | -45.39128 | 2025-08-21 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea4bd79a-b418-3e90-91f1-8e83649b3803 | -16.51401 | -46.73114 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc62b71a-9ad6-3073-849a-f1fb1db917f0 | -14.8465 | -47.93702 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
