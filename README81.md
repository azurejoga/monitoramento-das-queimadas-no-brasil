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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad8f800-665e-3494-a077-09d4ca91b260 | -16.49479 | -51.96806 | 2025-09-12 04:27:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc0f7f7e-4bfc-3e36-a66f-64eee048e7a9 | -16.48293 | -51.3919 | 2025-09-12 04:27:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7689fa1-f062-3a5c-b2c9-024127f541b5 | -15.69445 | -47.02385 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f92cea8-f9b8-3b3c-a625-6a1a7e5607ca | -15.23238 | -52.83538 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67a822b8-a331-3d52-85d3-92a85b7662f9 | -15.6637 | -47.03518 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 880a4836-864a-31ed-8c01-cf76871c9467 | -11.19049 | -55.08673 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eebd29b8-1090-3216-899f-7438c44c8242 | -16.08263 | -49.31963 | 2025-09-12 04:27:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73d4860a-d1a9-300e-898d-934ad5f297b6 | -12.90454 | -43.57674 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaa4d873-89a5-3a3b-835b-957744a45b5c | -15.11832 | -48.61825 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fca486d-d374-3886-939f-e1f00942038f | -15.53363 | -48.54815 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd1416c8-60c4-3ea4-bdf3-c5e20af64653 | -12.83522 | -47.96025 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62ac26dc-9d1f-3d6f-86e2-e719df6f5b43 | -11.91934 | -50.69249 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72db2d74-3201-35f1-9661-b0881eb5e6ca | -15.09461 | -52.46503 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e32ae7b5-8cae-3aae-bbd3-9582d24d2a11 | -12.9203 | -54.76701 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf04a96-bf16-3882-bc86-e5e70c6ce650 | -18.61688 | -48.25647 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c06e7f4-3ab8-3f0e-a0a5-8952c4d0b3eb | -15.10129 | -48.03738 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15aa6988-8664-387b-8971-8cd937019faf | -12.97696 | -48.00828 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63368fc5-335c-36f8-82c2-8758129c2be6 | -18.34181 | -45.12796 | 2025-09-12 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43be2763-813f-3179-9853-0e88405e8254 | -18.60045 | -47.18519 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 487243d1-2ae8-3f64-9fd6-7df469e112bb | -13.23443 | -51.74213 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5dcfe11-3e3e-3ff2-b955-c7b0fa9463af | -12.24747 | -47.33685 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1de31928-1121-3391-a646-b8a1874a71b6 | -18.76885 | -48.18955 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd14ac35-9ad1-369f-bfbc-5f8d3efb7bc8 | -20.00255 | -44.23663 | 2025-09-12 04:27:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1025c6cd-737e-3223-9ddf-fd19be41a3a9 | -11.201 | -55.0834 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9db58e4-f4cd-363f-a88c-07c6298fa924 | -16.28103 | -45.68539 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ca2c402-1091-32eb-a3cb-1620204592a7 | -16.12565 | -48.34587 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53bf3024-7f1d-3c9a-a807-720edba3eb3c | -17.957 | -45.28199 | 2025-09-12 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d15b39a-aa19-344a-85a8-f308a48abb91 | -14.56289 | -48.75608 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98a951d1-1cc2-39f5-8622-e1652924749c | -12.8533 | -52.97315 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58ec5993-b777-3dc1-8a80-1443052685e0 | -12.97141 | -48.0219 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f151d884-bbd2-3510-8d7e-bcaf725b6a88 | -12.46613 | -53.8331 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f80575-cbfa-3e0a-8eb5-a474e9b4e3e6 | -18.59305 | -47.18789 | 2025-09-12 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9413b2e-759a-336d-807a-5ba3bcab2199 | -17.82212 | -46.72672 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2dd1fd4-cabf-3a4f-b03b-a66011e1fc01 | -12.92507 | -54.79245 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b51b767-e911-3af6-8125-813eec6f88f5 | -17.96008 | -45.28695 | 2025-09-12 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7967b55d-8504-3839-a583-198b1db13207 | -13.90118 | -48.26282 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 39560051-9d5f-3424-8235-c8120db2199b | -17.95197 | -46.9384 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bae4581a-2c88-347b-bd48-2d9364c9971b | -12.55846 | -49.13102 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cc4320b-33aa-3a80-abf1-1ee74f34b47d | -17.78713 | -51.72475 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 451169ee-96b0-34f7-9d86-4198aa78c0af | -12.86062 | -47.95003 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b3ad297d-b951-33b7-ae0c-d9876cbdccad | -17.55286 | -44.54905 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 215e7e43-8f21-3e82-acb2-63cde91116fc | -17.79959 | -42.56956 | 2025-09-12 04:27:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 84af0a48-77f6-3e8b-8012-b93e63df17f5 | -15.70779 | -53.64759 | 2025-09-12 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e7d2caf-4378-37c3-920e-e5d9abeedb71 | -14.38808 | -47.34303 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee26cf2-4856-34c6-8099-671669a960fe | -18.8201 | -46.88143 | 2025-09-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e440576c-4c0c-3c69-b8a0-5daed232f4c3 | -12.96651 | -54.74982 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af42c63e-ac04-300f-b367-24da3773ff80 | -17.95255 | -46.93455 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f4a17fa-c5de-3a98-b186-26369e71edef | -12.89425 | -47.97357 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a3bc47f-5b68-3250-8eaf-cde8019c0bc4 | -15.83109 | -42.59594 | 2025-09-12 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b9321daa-9cae-33b8-8925-b41e4931c968 | -13.91168 | -48.26093 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08560133-a864-34bb-b9bd-41e023cb71d4 | -19.88325 | -41.41379 | 2025-09-12 04:27:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 17630cc2-bb14-39d1-aa71-e78dd75f444f | -12.89812 | -47.97062 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 382be4bb-d9aa-3727-afe3-6f45f3ae5af5 | -18.05078 | -45.43744 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3268d8e-d027-3b19-b8ef-fae28c386e2a | -19.96803 | -46.88337 | 2025-09-12 04:27:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d172ce4c-6b86-36b0-b893-2bd58a5b42a3 | -13.36999 | -41.91885 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf8d0191-3893-3828-9072-a6f734043e6f | -18.76438 | -48.19639 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f978246-74ad-3fee-825c-47f9b4ad7e1b | -12.83908 | -47.9573 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19a34dc3-8b8f-3cbd-bdc7-c5983959f91a | -18.05873 | -45.43418 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04dc7725-3f8f-3abb-8693-5ebc6a8125a2 | -19.75174 | -46.08967 | 2025-09-12 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1511a6c2-d53f-36d9-b4ed-87e3aee4c000 | -18.4493 | -49.56239 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b79a199b-7ff8-3e6c-8fb6-d03c55188889 | -18.99107 | -48.86292 | 2025-09-12 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 411e56b3-adb6-330f-847c-7a42b1506d16 | -17.20471 | -50.15502 | 2025-09-12 04:27:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 483ae3a0-a474-3be5-ab5c-c23039ce2bba | -12.93505 | -47.99408 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88ec4c28-c463-3353-a89b-95ff16a86eec | -15.92413 | -51.79269 | 2025-09-12 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| aea88ad0-9964-36a8-8453-ab9f81e8f8a2 | -15.68435 | -47.04512 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e332c10c-3630-34bc-83b5-5ed405926ca4 | -11.92294 | -50.69312 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 998076f5-a858-38a2-846b-8ac9913edd5b | -20.04072 | -41.7451 | 2025-09-12 04:27:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e640f8b3-a08d-337f-9deb-44f70c4fbe82 | -16.43669 | -49.04282 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2df62ea6-db9f-3965-96f4-84f7b52a2e24 | -18.41017 | -44.45881 | 2025-09-12 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c4bbf4-d0f9-3e50-8437-49779ed68695 | -15.08863 | -48.0097 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6fcbb6-fff8-39dc-8f0e-4d520d514273 | -17.3244 | -46.66789 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da97ebff-fcf4-3b7e-9564-0bfb6927f946 | -11.7808 | -50.56195 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1dbf9d2-c939-3da5-bb3b-2886eb950168 | -13.2779 | -51.72007 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ab49be34-018c-3e74-9188-d02f10bbd240 | -12.85333 | -47.60847 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 538f0524-95b6-3f58-9e20-d2ca48d66a84 | -13.78253 | -46.29079 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18d315dc-a2dd-324a-8b37-4b7e7264ce02 | -15.23745 | -53.83921 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d611ee9f-6e15-3930-b199-960390e03739 | -18.44813 | -49.5697 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 07ff71c1-4d26-341a-a2dd-64bae0dd3b10 | -18.07699 | -52.28657 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06290c27-b44b-34d8-9267-78ee9e7d5ddf | -18.06026 | -50.73561 | 2025-09-12 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6227197b-e8a0-38cd-a39c-746a8bbf7812 | -18.32391 | -49.3277 | 2025-09-12 04:27:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16d0f2b1-cafa-3c01-9d6a-bd72fc40d1cb | -18.0581 | -45.43858 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 633e596f-cc94-3a2b-b7d0-2e6d1298a34a | -11.78796 | -50.56321 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4975602e-efd8-3ff3-9e4f-7c39632c288b | -12.91751 | -54.75661 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3935c48f-6de3-32f6-b6b8-284cf62c510d | -12.8286 | -47.95916 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d911a9e-f676-39de-981a-84623532a7b4 | -15.54217 | -49.74251 | 2025-09-12 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39c4d66d-ea23-3a7b-8dae-dd5d2a5d212c | -12.89536 | -47.96655 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e987a4a-fbbb-3a49-969e-a38d82401db2 | -15.66979 | -47.07319 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68549e8a-1d64-30ac-8e6d-a6ba5fd3466b | -17.91096 | -45.90596 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ca0f874-4937-3d7b-b751-071f1352a74b | -11.96929 | -51.1731 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1804b186-0d49-3242-9e41-d3142c334dae | -19.63605 | -41.58759 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8a3cda5a-219b-33bc-b59e-f4089a87aa99 | -13.24376 | -43.79474 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c19ea85-9664-38fe-b83e-70de54d308a0 | -12.84455 | -52.97531 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d22202d-903e-39b4-af62-d6dec94a68b5 | -16.26179 | -46.78533 | 2025-09-12 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bb25c61-720e-3130-9afa-ab27a1695798 | -17.83554 | -52.05381 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67262461-a05a-3765-b347-2c9891a6a8b9 | -14.28109 | -45.04515 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62c67a7a-3c14-3313-95b0-5fbd46f2410b | -13.90624 | -48.23096 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d905b2b-be24-302b-967f-6a1cb3a6dab4 | -14.77209 | -48.23187 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b767c86e-bd83-3d42-8bad-281fe9cefb86 | -12.4669 | -53.82891 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13571f18-bb54-34a9-8461-50eaf62bcbec | -13.92062 | -47.96795 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b41825d9-9ab1-3d68-bda6-86e03b55325c | -15.81543 | -52.21942 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README82.md)
