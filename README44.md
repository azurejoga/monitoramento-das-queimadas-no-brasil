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
| 630d1e83-9b8d-3961-b474-4da8e25bb6bd | -12.83947 | -48.07618 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 156a7e9b-03fc-364c-82bb-08d4901a5c72 | -15.69731 | -45.42342 | 2025-09-01 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 999d51b9-be09-33fb-a087-451cd04b923b | -13.16217 | -45.28169 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84625aa8-b739-36ea-8123-cf03fce1747d | -15.6221 | -47.86055 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae223fe5-8573-3b1e-a847-ce2525be97b2 | -14.82492 | -46.73845 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3c16de8-3df6-3eb3-b2d5-10e94cc55462 | -15.63117 | -46.81176 | 2025-09-01 04:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89f8bca5-4517-36e6-a31e-a0b7866f9630 | -18.1237 | -44.99033 | 2025-09-01 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b94b76ae-5eef-301f-bf71-42261d9890b1 | -12.60112 | -48.17709 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9417d1fa-32cf-371f-8e36-c5fbf44c5d12 | -14.04363 | -44.55708 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fdd8238-e74d-362d-b11d-b5e323d7baa0 | -14.75346 | -46.76228 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9bff71d0-df7a-3511-9960-a95e00e3544b | -16.50697 | -55.0324 | 2025-09-01 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd43c7bc-f923-3fb6-b48a-d605764a37f2 | -13.68862 | -46.91921 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f456ebc6-8fbc-3b07-bb4f-68168b2c61c1 | -11.96345 | -51.36752 | 2025-09-01 04:12:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c887f2a9-356a-37f3-a0f9-5ba4637e20b1 | -17.61005 | -46.67386 | 2025-09-01 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d09ed6-7d2d-3b5c-a28a-6bab467b1d64 | -13.69651 | -46.92246 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fe5fadc-f2bf-3669-adc2-1b0e639fd80b | -11.83622 | -51.47012 | 2025-09-01 04:12:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7a38ab-3a63-3d62-8de6-330d6925ed1d | -13.48628 | -46.99493 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f4fead6-0241-37e4-8bf8-a2357611e7bb | -15.7275 | -48.95749 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63089736-5ec8-33e4-9ad8-5c612abfe37c | -13.32946 | -46.85031 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f67022-97f2-3d4f-8320-554416c77a4a | -13.98923 | -44.52874 | 2025-09-01 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f3ba1c5-9795-3df3-8f35-fe8a9c3fc258 | -15.99918 | -43.4203 | 2025-09-01 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c4ade14-281d-34e6-81ed-c9b6b037e6e5 | -13.49171 | -46.98606 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b34d0fe-d701-3454-88f8-41beb1505c05 | -15.70209 | -48.96446 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 82890c37-d8ed-3757-985f-8548f5229c69 | -13.37563 | -46.32025 | 2025-09-01 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbdc2f4d-8f95-3eb1-882e-3f3972970678 | -15.69922 | -45.412 | 2025-09-01 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc08268-eb1a-323a-8b15-2b1e49fab0d9 | -12.56997 | -48.21 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7422f5f-e0be-325a-a66d-a63a7a75e88a | -13.65189 | -46.93127 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 348edd16-9028-3b8b-8dae-4421e807551b | -15.3241 | -46.11073 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 256ae01d-0817-3639-a999-3798c4caa4a9 | -14.78334 | -46.76365 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2897911e-abf5-348d-9969-1f001f9cc5da | -12.57883 | -48.2078 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20523ac3-bf90-3a57-86b9-b33fdcea277e | -12.94348 | -48.09904 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ecbdb07-1903-3982-98f2-069157b460e9 | -14.79226 | -46.73345 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01355dd6-09d4-3346-b9ef-d96f47e4be34 | -16.15601 | -49.63446 | 2025-09-01 04:12:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3978fa81-2520-3158-ad7e-c4002b425524 | -18.11565 | -48.5424 | 2025-09-01 04:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b38ba10e-d0b4-39aa-8269-79173cdefd47 | -13.31942 | -46.86383 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dc48131-c75e-388a-bf0c-72c6e7cd0356 | -14.75785 | -46.75865 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8bd39d87-696f-32a3-a9f3-c1eac45718c7 | -12.62973 | -57.00866 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd5093ea-7212-37eb-a9fb-15dfe20ec958 | -13.68217 | -46.86704 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6325d14a-70ff-32e7-bb00-9b2aacef8166 | -17.16363 | -46.08813 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cf3ab98-6496-39b0-98e4-2ec879ba6473 | -17.60723 | -46.6691 | 2025-09-01 04:12:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f9b4de7-89d6-3d72-bb28-6cfc07b56df0 | -15.59051 | -48.35265 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e2acece-bccf-3894-8e64-857c751521cf | -17.20221 | -46.07023 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18cf4c9a-1671-346a-b248-cc635798a70e | -15.6912 | -48.95458 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d63bd3e-2d52-3971-87bd-796121566b58 | -13.68887 | -46.92205 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f661c87-a844-3537-8263-8138244c2423 | -12.80513 | -48.08133 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36f73e2b-da47-3bdc-ad7f-8549fa2a2b52 | -12.61285 | -48.19896 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03a6c0ea-6ea8-3b36-9b78-e60c87a232e0 | -13.37637 | -46.31596 | 2025-09-01 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebbfdea4-cd1b-3c1e-8eda-d2c0ce41d8b7 | -12.64146 | -48.20444 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16d3d1d5-f431-30a2-b1ed-a7285aafd129 | -15.59135 | -48.32501 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 329b7b88-9b36-3a4f-bd13-68df081bd425 | -13.48977 | -46.93101 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7f36116-7b6d-367f-83a5-9cd70d6be51b | -12.02276 | -49.71472 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f93fe4af-e24c-3538-810c-600ab07c2106 | -16.96805 | -49.31217 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94dc698b-0555-3f67-af3c-e8d84b5d936d | -13.39394 | -47.05759 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f7402e1-b2dd-3ecb-82c7-eb40f82e7ad1 | -18.11656 | -48.5374 | 2025-09-01 04:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4283e394-17b2-3c72-8289-207c3adff32d | -15.73145 | -48.98174 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2fa2f4a-625d-3f10-a2d0-02829f9e67b8 | -13.98957 | -44.54776 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8adb9f1-401d-33d6-bf7b-d0d394f35220 | -15.29946 | -52.79198 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99343d7c-5a4e-3161-a21a-cf92e2733ae0 | -15.59053 | -48.19334 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c6e95551-0ea3-3a72-b587-22cdca70cc2d | -13.70028 | -46.9229 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dfc5169-210d-32d1-86ff-c33ca9e78fa1 | -12.40977 | -46.45785 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 224f8c69-10e4-346c-8865-1e8386e3975c | -14.04497 | -44.59145 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fbab5e4-6a7b-3ddb-b222-5728dd3f44b5 | -17.16432 | -46.08397 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f2971bb-2f9d-3ff5-acba-0d17eb7447bd | -14.0446 | -44.5724 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d1a5cd8-ef7c-3fa9-a043-41be7eae472e | -16.411 | -45.64939 | 2025-09-01 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5db1bbe1-d7a4-3947-b046-72ca1e1be89a | -14.22553 | -48.05968 | 2025-09-01 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f5d7fe-32bb-39e7-9829-1e55b0f4a8b0 | -15.69266 | -48.94648 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c731e2f5-e601-35ef-ae20-bd65af85287c | -18.53095 | -45.02324 | 2025-09-01 04:12:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57524704-c378-3b1e-8fe6-02daa8576c21 | -13.70073 | -46.89859 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d382cff2-46ac-35e0-9d7f-de1fef815008 | -15.69046 | -48.95871 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85b325cf-f639-3477-b634-2dfec850d76e | -11.52142 | -54.47773 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c7dc4fa-288f-3c66-8d55-1e05c0167f50 | -15.69858 | -45.41581 | 2025-09-01 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 158572c5-ebff-3acd-a6d7-ed3b01ed0abc | -12.79175 | -48.08598 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c1337a7-3b91-3e52-aba5-8a43cb0f92ed | -12.87758 | -48.16708 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5281ac5c-9841-3efb-8aca-c8566cf06458 | -15.58849 | -48.34112 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 63ddd80d-d1d5-32e7-a1db-f08e274cf6f8 | -11.84084 | -51.47392 | 2025-09-01 04:12:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b988ee8-9282-385e-83bf-94ca58f3cb8b | -12.94389 | -48.09989 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bf84703-d227-3e79-8f57-f8aaf17c3eb3 | -13.47118 | -42.47972 | 2025-09-01 04:12:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 063de02b-a95f-3943-bebe-db9a2316f922 | -13.38096 | -47.06499 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1f7f734-a2fc-30d8-a8b9-14da7936e441 | -10.87177 | -55.76774 | 2025-09-01 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90d21197-bf57-3bd5-a303-f4d3d79e6a80 | -13.29263 | -46.90676 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37223c55-4b42-3b22-9a1b-d862f6014fc6 | -15.69524 | -48.90896 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52a0f5af-4730-35f4-a9eb-11756648c1f5 | -12.58359 | -48.2048 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe23c648-7bb2-3c29-ad16-369b7ba07c2a | -15.22564 | -53.80006 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22cd0259-f802-36d8-a6dd-d4f940ed6dce | -14.74767 | -46.75224 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c717343f-180b-3abc-b0f4-1f14b7f0dae8 | -15.70082 | -48.92466 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d88de808-f9bc-35f6-8f06-6d24f8ae1450 | -15.22167 | -53.791 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3898653-8486-3067-a51b-a83ed01e08c2 | -17.16291 | -46.07113 | 2025-09-01 04:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8217d37-5374-3b3b-b370-a2419320d7ab | -12.6041 | -48.20845 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd649696-2648-3816-a804-afdac082ad33 | -14.77318 | -46.75702 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 707819b4-4f86-3717-b035-e2910cf007d3 | -12.57063 | -48.2063 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53840bbb-8083-3f62-a3e8-c6e32750947b | -15.21966 | -53.78714 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53b8556f-3284-36a4-b58e-6e30c7c22fba | -16.07998 | -43.61783 | 2025-09-01 04:12:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ee0e2c-e337-3925-907c-0c76ae6d265f | -13.17608 | -45.28409 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be875389-5439-3bd6-9f36-760dcf3191d5 | -15.73005 | -48.98931 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b9d8242a-8e47-306f-85bd-1652aeeaa4a3 | -12.78298 | -48.08825 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d91327f-3e5f-3fc0-a99e-b7df7bb29c12 | -13.52255 | -46.98699 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3dc4bbac-f5cb-35d1-a89d-2f6a4845e3f0 | -13.6927 | -46.92221 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 306a13ba-3630-3fd0-a301-eb66d6b4bb46 | -15.58248 | -48.32919 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb78d7c5-4e86-3971-bb82-1d5d4d73172c | -12.56181 | -44.78961 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0550fa1b-073d-3d20-870f-8d1cc13f8c71 | -13.3546 | -44.62474 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
