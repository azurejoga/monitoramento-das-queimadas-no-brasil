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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e8e6892-bbb0-33e3-ad10-e9e833c6c7c6 | -29.62575 | -56.64519 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| df15dcf3-bc2a-3c80-9b2b-e1e78c12f855 | -29.61408 | -56.65931 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| fd3e29ff-cc39-3fd4-9d29-6a8a3ea7b4c2 | -29.63689 | -56.63742 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| e17a3c5e-c3f6-30fc-8ca3-587096a36e76 | -29.61795 | -56.65936 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 8795caa3-fa88-3bc5-a4c6-22d1c7b8ff54 | -29.61349 | -56.65803 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 795e6101-0680-35b8-8b0a-1a7bb000094f | -29.62416 | -56.65674 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| ff09a6d2-3b1f-37f0-8ddb-f2f3b40dbae2 | -29.61637 | -56.64901 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 84b681b3-269c-3bdd-86cd-3f2a9e306e56 | -29.63243 | -56.63615 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| 3b1af707-d1d2-3e9c-9b1e-4af186f8dde9 | -29.63879 | -56.63359 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 84bef5ff-bc5c-3daf-8fa6-0166c512bf2b | -29.64657 | -56.6413 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 9e38998a-ed37-3ebe-82c6-a560c4b99140 | -30.39442 | -53.95602 | 2025-02-06 04:21:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f5086b80-c063-3aba-84e7-a706f075f8bf | -29.63423 | -56.65415 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| c3b29115-a2a3-34d4-a03d-05cca5830140 | -29.62128 | -56.6439 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 7c44be4a-50e5-3030-a5f6-7bc22140e8e6 | -29.61523 | -56.65414 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 813190f7-7d38-34df-b486-a1b5e183d5c4 | -29.61969 | -56.65545 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| b41d1ab7-128c-3917-8806-2c768eaa3650 | -29.63765 | -56.63872 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 9d265dd5-81e9-3bff-863f-29986a6e1688 | -29.63537 | -56.64901 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 57b6b2a7-d06d-3848-9e0c-ccf955f3b1fd | -29.63433 | -56.63231 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 08131568-9438-36be-bb8c-6ddb0103727a | -29.64324 | -56.63487 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| da8cc88a-7aa2-3472-a328-bcf42389cef3 | -29.64211 | -56.64 | 2025-02-06 04:21:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 646b880d-dd7a-3c0f-9806-4432349dc1aa | -10.65633 | -44.498 | 2025-02-06 05:03:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 08f613da-979a-3a12-bfa2-9af86c6a4e02 | -10.65697 | -44.49251 | 2025-02-06 05:03:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b96ac579-3a8c-3120-b2e0-1bd761dc96d7 | -8.12056 | -43.13878 | 2025-02-06 05:03:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6001544e-ccc7-3f2f-aa72-17769e2d1274 | -12.8466 | -43.82112 | 2025-02-06 05:05:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e24ed6f0-58ea-39de-939c-0e27e7bac5a6 | -12.49233 | -43.78744 | 2025-02-06 05:05:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5349fdd7-4dd5-3273-a3fa-bdf526bad415 | -16.68129 | -43.8855 | 2025-02-06 05:05:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f387ffae-c8e9-3317-a444-b9dfdd7acb43 | -12.85347 | -43.82206 | 2025-02-06 05:05:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25071c2d-5852-35ae-bcd4-fbf73632ff20 | -11.58408 | -47.63395 | 2025-02-06 05:05:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc88da2d-c4dc-3e6a-bfc6-abce0f3a271b | -9.20858 | -62.40415 | 2025-02-06 05:05:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d612f729-1e2c-344b-8a0e-c8312d35ecc1 | -12.983 | -51.27187 | 2025-02-06 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf817d2-624c-3f80-be66-3a53d350ac09 | -13.05013 | -57.09495 | 2025-02-06 05:05:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a01553f-2a72-3d14-8635-1634eb07da5c | -11.58365 | -47.63741 | 2025-02-06 05:05:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eb32f55-69aa-3785-b16c-9eb0c716547e | -18.60904 | -44.25593 | 2025-02-06 05:08:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b65d8b61-66fa-31d7-a662-00a99b523974 | -19.96077 | -53.96499 | 2025-02-06 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aac65bf-9b18-3d05-9e28-a30db7f18bdd | -29.64226 | -56.63367 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| a4c88685-17bd-3902-af36-bc5bef7fb9dc | -29.64542 | -56.63968 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 8.2 |
| 38164acc-74fc-3934-8561-c7fb8056bc56 | -29.63646 | -56.64921 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 3d3d64cd-7c32-3193-9eec-0bf98a3fc366 | -29.62566 | -56.64195 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 5741d4a9-6389-3e14-af6a-11afb23b1cff | -29.62948 | -56.64257 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 34c9687f-a0a6-37e9-8e1d-f42d9e4d7a4f | -29.62118 | -56.64673 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 56b0afa1-af7b-3617-8321-b938b587025b | -29.91345 | -54.35903 | 2025-02-06 05:10:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| b9dd2e48-141d-3641-ad7d-bd39efce5c5d | -29.63461 | -56.63244 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 507373d6-0737-3241-b27e-a20a181e95b9 | -29.64822 | -56.63573 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.8 |
| 2326a2c5-ec7c-3ad6-80c2-97ded63c5955 | -29.6444 | -56.63512 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.8 |
| 366b77ce-f0a9-33c4-be24-e51fa3795685 | -29.61988 | -56.65749 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 7b4e279e-af8b-3de9-a631-344c397660ab | -29.6476 | -56.64112 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.8 |
| 136698eb-911b-3b02-9783-b8f3020a56ec | -29.61606 | -56.65689 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| ef920343-d615-39ca-99b4-ebcd001eabaa | -29.64608 | -56.63428 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| f890f12f-2999-32be-a4d8-ecb62bd64f50 | -29.91782 | -54.35969 | 2025-02-06 05:10:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| bc62d017-e295-3b61-861b-8cbad2196ec6 | -29.6333 | -56.64321 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 644c0fdf-b5cd-3f75-97c0-d505c6553ebb | -29.63843 | -56.63306 | 2025-02-06 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 606186c9-b1e3-32f1-938f-d6129ef8bfa3 | -12.492 | -43.78419 | 2025-02-06 05:25:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8c0f7965-bced-38be-b4de-7bf515b889ce | -16.85618 | -40.8198 | 2025-02-06 05:25:00 | AQUA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 58813e89-7e44-39b4-8f35-f94a13a5d02c | -29.63837 | -56.64256 | 2025-02-06 05:29:00 | AQUA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| b656a4f7-e3d5-30c4-98dd-ca3dd4a747a8 | -29.64291 | -56.62093 | 2025-02-06 05:29:00 | AQUA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 14.8 |
| 893270a9-a755-3796-ab0d-b3985a9da005 | -29.64018 | -56.63573 | 2025-02-06 05:29:00 | AQUA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 17.7 |
| 4ba87a2f-d615-3920-9bac-a26536da60c4 | 2.28117 | -61.22876 | 2025-02-06 05:29:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 178b5fdd-05ac-3bc6-a116-7c098d520047 | -9.13235 | -62.48196 | 2025-02-06 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03f7965d-f5ec-37ed-8762-77dcbb801193 | -9.1318 | -62.48547 | 2025-02-06 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b11ec6e1-545a-3d23-827c-f065e8c97e73 | -11.90561 | -63.877 | 2025-02-06 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ace728c-c161-31d8-9e27-6c7db6c785e6 | -29.62843 | -56.64128 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| f767475c-5363-3ad9-8dca-dfe1f92e9775 | -29.62053 | -56.6434 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 05d94b65-0b4d-3559-8387-009602fd0baa | -29.62623 | -56.64396 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 35be2f13-1093-305a-9ae4-5051047edaa2 | -29.6202 | -56.64784 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 06b75f40-cc77-3c76-b469-0dd6cc6d9da6 | -29.64044 | -56.63371 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 5f2ccdf7-dd66-3598-a3fc-5cd4188afbb8 | -29.62242 | -56.64511 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 82d56bbf-6e5e-31f2-893d-e2437832600d | -29.63473 | -56.63312 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 968a7974-dc61-3897-bcf1-eabdedb61e53 | -29.64583 | -56.63869 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 4619bc13-9b79-34f1-b897-e2aa306bc03f | -29.63412 | -56.64192 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| a29e6bdd-0fe1-3c86-bfef-939979598b32 | -29.64614 | -56.63426 | 2025-02-06 05:35:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 1c058af4-74b2-3283-b043-ce975b30fbb2 | -9.13061 | -62.48426 | 2025-02-06 05:54:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51147546-bde1-34e7-83d4-c4ede9f2ead6 | -11.90301 | -63.87756 | 2025-02-06 05:54:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7dd0938-a456-3fce-a72e-a2b804a2bde3 | -29.6307 | -56.6325 | 2025-02-06 07:10:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 96.6 |
| 8ebef460-9961-341f-bef1-ff9332727f1c | -12.05 | -45.07 | 2025-02-06 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8999ea6-7289-350b-8f40-958162886792 | -29.6307 | -56.6325 | 2025-02-06 12:30:00 | GOES-16 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 154.6 |


