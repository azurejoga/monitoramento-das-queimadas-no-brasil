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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28855caa-ecf5-3d12-926b-3a9bc33aec34 | -22.75265 | -47.27472 | 2025-09-03 05:16:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aae68130-0bc9-34c0-99ef-ec081605463c | -15.74002 | -53.66428 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c497ac5-938e-3c5a-bd86-ee92c8554710 | -17.94527 | -47.23699 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b345f02-0d25-387a-953f-52a44b91067f | -22.18536 | -48.82881 | 2025-09-03 05:16:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4857ea60-b7c5-3f7f-a34f-149203d3d396 | -16.30635 | -52.96112 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b855370-8cb9-3416-b7f6-e861d39cc0bd | -15.55695 | -48.41529 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddddb297-cb40-3344-b7b8-b6ca61aa633c | -16.54694 | -55.07872 | 2025-09-03 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7c2259af-ed7f-381b-874d-e0a3920bef65 | -15.55238 | -48.40171 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b07dff59-f777-3e8a-a0c0-817797d8b2cb | -15.7369 | -53.68852 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e84eded2-4610-303f-805b-ee15d103f64b | -15.14695 | -52.36168 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c03655f-9e4f-3d12-89f3-402ef0b7dcbf | -15.14759 | -52.35684 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce867fd-f9fd-3af9-b46f-207bbd8c5f91 | -15.54958 | -48.31518 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ac3b8ce1-ea5a-33ed-a3b8-2b57a8ecbd52 | -16.30189 | -45.69281 | 2025-09-03 05:16:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c8ed992-1363-38f4-889d-9bb7bc51823b | -17.5336 | -47.5839 | 2025-09-03 05:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1efed76-a34c-3141-99a9-a0ecb3969e3a | -15.54883 | -48.3786 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95e8d952-0a94-3b8d-a369-6b41816fb812 | -16.07933 | -47.98005 | 2025-09-03 05:16:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f44a2e45-452a-317f-98e8-ea0ee6d79c32 | -17.52712 | -47.58382 | 2025-09-03 05:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cb07987-c263-3174-bdf6-7fa05e6fab9a | -15.74585 | -53.68575 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 47a49fdd-322c-39dd-87d3-6ebd96209c1f | -18.06418 | -45.98918 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c7376035-0b49-322c-bb8b-b183d0cdaf8e | -20.89132 | -50.09864 | 2025-09-03 05:16:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b42cf5ec-01da-3755-a64a-b539f464e992 | -15.59882 | -52.67619 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79b59537-c469-3e35-a547-f75a50bb4018 | -18.06102 | -45.99524 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bdf089b0-93a4-3fe5-b636-dbaece12397f | -15.71674 | -53.64456 | 2025-09-03 05:16:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7946d65f-99dd-3105-86d6-6744dce5dbfe | -15.55738 | -48.41126 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d490f6e2-3312-3257-a1b9-9137eaf8859b | -14.32446 | -60.34132 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d25444e8-6445-3a30-8e74-4171d3b7baf6 | -20.89243 | -50.0964 | 2025-09-03 05:16:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 34b4ae01-cb06-3c78-ad86-0fa8320e7d5c | -15.72097 | -53.6451 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 584f1bf5-19b6-3e89-abab-a53eab72234a | -15.24538 | -53.80308 | 2025-09-03 05:16:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 448961b2-cb41-3d79-b296-0b5136ebe406 | -22.75355 | -47.26186 | 2025-09-03 05:16:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52f8ded0-8695-3cc1-9901-10f5d6f33ed4 | -16.29359 | -52.95444 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83e8e2ae-2696-317b-b412-e722a797d43a | -15.55178 | -48.35115 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7625d848-773f-3403-b3b8-52200e30f987 | -15.59371 | -52.68035 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c061d1d-2234-39d2-81fb-a8973924c503 | -17.53412 | -47.57858 | 2025-09-03 05:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4a2e8f6-8d4f-3b42-9587-20eb1a871c1a | -15.55379 | -48.38864 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 077fb6f7-04a7-379a-809f-9d05d15e317f | -17.54058 | -47.57882 | 2025-09-03 05:16:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39ee9043-2e6a-3d58-9c64-1102c18784a2 | -17.94064 | -47.23007 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b93a027-3b45-3d43-b545-d5090aee18da | -18.06869 | -45.98896 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebef0036-fb51-3199-adf6-21b92197c551 | -15.75059 | -53.6823 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da40ee9b-449d-3cbc-8e88-796edea8d92a | -15.74534 | -53.6897 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a27cc2d-b2fa-374b-a19c-b3545f7905ca | -15.74423 | -53.66497 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0284d313-4098-37b3-820d-3cf9f7a9aec4 | -22.17574 | -48.82096 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7d35baf3-a847-33ca-b744-eb72936bd5cd | -16.30244 | -52.95616 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7b9fb7e-2eb6-310c-af8c-01bdc6087856 | -17.9225 | -47.21124 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f302c8f-eef0-35d3-9f00-90fefd758e6b | -16.39751 | -50.40639 | 2025-09-03 05:16:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59b53431-cdac-3df6-b837-6a97d3e7a053 | -15.59762 | -52.68555 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97725d36-1c06-3324-a5d3-94e054deae36 | -17.94729 | -47.23003 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b070933b-8768-3279-ace9-5e6009b1408f | -22.17869 | -48.83328 | 2025-09-03 05:16:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5655b9af-2e18-3d39-98bc-99a32f974c40 | -15.1513 | -52.36088 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c58bcf28-d2eb-3dd7-83d1-6d912bdec444 | -15.55652 | -48.41921 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e728427f-3773-32c5-9474-c1721230c451 | -15.7215 | -53.64093 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ca187223-ee0d-34af-8fba-695729fb63a6 | -17.95192 | -47.23695 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1a11896-2b2b-3354-a21d-47127a5b2156 | -22.17485 | -48.83123 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 68e37452-a862-30aa-8de0-4051cb7f2def | -15.60273 | -52.6814 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57d0e857-f15f-3420-957a-27c163236c52 | -17.93516 | -47.218 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ffb18cf-f14f-3591-a3b2-0579697b7cc5 | -22.75998 | -47.26895 | 2025-09-03 05:16:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27b830c8-6903-36ae-a5e9-a295ce357522 | -22.7531 | -47.26833 | 2025-09-03 05:16:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c98c65ca-0635-35a5-a990-e4bc720c935b | -18.14403 | -51.74746 | 2025-09-03 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ecbfae41-0e6a-3bb5-8f58-b285e11b8dcd | -14.32505 | -60.33773 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d37701ac-12a7-3eec-8aee-40917b53507d | -17.91434 | -47.21128 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942dc9ca-d408-3b46-8268-ea2583b84311 | -16.30689 | -52.9569 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff3acb21-b7c2-37ea-b655-e7709d945ac5 | -15.54929 | -48.37433 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2cff6b2-6685-3a96-ab5e-facc32f90475 | -15.58295 | -54.32836 | 2025-09-03 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8f62139-9b78-3750-9a61-acbf9a10cad9 | -17.95138 | -47.24289 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4337e1d4-edc0-3aee-b808-2f13faaf83bd | -17.93573 | -47.21202 | 2025-09-03 05:16:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c61fdb96-c964-3745-955d-3327a1e202a9 | -20.89173 | -50.09443 | 2025-09-03 05:16:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d0027d0-f10c-3392-9a7f-1224b544a7c8 | -15.74956 | -53.69022 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 895246db-88e9-3adb-9e6f-6559c5864ac3 | -16.29304 | -52.9588 | 2025-09-03 05:16:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78e4f151-39e1-3502-b253-427ea949b835 | -22.18198 | -48.82173 | 2025-09-03 05:16:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 32d3284b-b51c-3b09-9eb9-1fd388714f6d | -14.84679 | -60.04821 | 2025-09-03 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd2cdd23-9207-3760-a482-e16373fab319 | -15.57988 | -54.32063 | 2025-09-03 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e2c0293-daba-3eed-b99c-4bdab058cb57 | -15.14456 | -52.34017 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c78ed064-8b57-30e5-b11a-ff77b71a2b6b | -15.90461 | -48.17327 | 2025-09-03 05:16:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0ecf7cbe-44df-3b6b-9f32-4e12d41a05dd | -15.72574 | -53.64138 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f8d33d3-67dc-3bdd-9a9d-3fab3fc2a05d | -15.56248 | -48.41993 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfdf967a-822c-3163-b57c-8df8ee9af68c | -18.14336 | -51.75332 | 2025-09-03 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0399902-0f2f-3fe9-a0a9-3dd8078ba7a9 | -15.57938 | -54.32437 | 2025-09-03 05:16:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08a7ca28-9bdc-3508-9086-e20e36f88c96 | -15.54911 | -48.31952 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0faf48fa-d86d-30f2-8dee-adf57dd9783b | -16.07452 | -47.97875 | 2025-09-03 05:16:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc02e732-1c95-351f-b8c3-5adfa03240c2 | -16.95236 | -53.52004 | 2025-09-03 05:16:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c87fb99a-49e8-37e2-aad1-7c05085ed02e | -22.65876 | -50.66586 | 2025-09-03 05:16:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c60e216-a47f-33f2-8011-5c7f6bbde18c | -18.06811 | -45.99586 | 2025-09-03 05:16:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 63ca2902-47bf-3e5c-98df-5f9daa60e4e5 | -15.74845 | -53.66564 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2f378b-b13b-3842-b666-c225495def90 | -20.89197 | -55.14162 | 2025-09-03 05:16:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 052bc43b-d459-343d-a070-e4852f6f979c | -15.71781 | -53.63807 | 2025-09-03 05:16:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54755134-08c4-3839-8f22-cba87b3fa6a9 | -15.5638 | -48.40781 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b699b3-d798-3a1a-aa0c-28ba81cd0d23 | -15.54478 | -48.35994 | 2025-09-03 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5173e702-eb57-39d1-bdba-206168601e29 | -15.14682 | -52.35955 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ac3c967-14f5-358d-9aef-539924df7649 | -15.14343 | -52.34928 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c27ef3b7-efe6-34fb-950f-536599bf88dc | -15.72202 | -53.63683 | 2025-09-03 05:16:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 697e9a82-75c0-3439-a606-76685cbe987f | -22.1791 | -48.82819 | 2025-09-03 05:16:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0e84d619-baaf-3b3a-9602-244615163156 | -22.1811 | -48.83192 | 2025-09-03 05:16:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8b86de0f-135f-370b-85a6-0aeeaa7614ab | -15.28409 | -52.77255 | 2025-09-03 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3f51a67-c5bf-3b67-96ea-41ff16624a5c | -24.41328 | -49.91211 | 2025-09-03 05:18:00 | NPP-375D | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4996d2f3-8ae3-327c-8c24-fe295bae139d | -23.66816 | -55.21731 | 2025-09-03 05:18:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e75896be-4193-39ae-a2d3-cbb006ad0759 | -23.92588 | -48.85754 | 2025-09-03 05:18:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1be2a0b-1bee-3895-82da-e8096c27afa2 | -23.92426 | -48.8603 | 2025-09-03 05:18:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b43d98f-b267-3e00-8e25-5263eb5564a1 | -23.66767 | -55.22158 | 2025-09-03 05:18:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 931e3ac9-6b28-368d-91e8-f5b5208df4e4 | -23.9255 | -48.86293 | 2025-09-03 05:18:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f58ca9a-4c44-3ca5-9138-7d65801a4e85 | -24.4073 | -49.91122 | 2025-09-03 05:18:00 | NPP-375D | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a128d5b7-4802-3c4f-81ca-eee1fd6512fd | -26.71471 | -52.44565 | 2025-09-03 05:18:00 | NPP-375D | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README101.md)
