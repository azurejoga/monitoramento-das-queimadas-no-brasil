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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43b29a3e-e58e-378e-949e-b71cda8d6f40 | -15.3974 | -52.69276 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c320145-73ba-324f-b6b4-35fc9fb3a827 | -12.89872 | -45.84803 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e145f288-4717-3400-bdbb-4c9c34e14c45 | -14.30255 | -52.90542 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a9c7648-1fdf-32e6-a6c3-4a6a1edf0e0f | -17.79305 | -39.70294 | 2026-08-31 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dd340a4f-f2fb-332e-9710-3472ee8abafe | -14.57844 | -54.11997 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ae7ef32-3236-3056-aae3-c361de6272d5 | -12.9413 | -45.91761 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7614c417-a110-3ea2-91c1-ef141e5a8944 | -15.63669 | -50.08842 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 022bd480-f4c7-3c1c-a315-55a64b9f7e54 | -13.83219 | -54.02573 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed54dea1-bd94-3fd4-a57d-f884ddd71cf5 | -13.63493 | -51.84113 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 828395e6-37e9-3711-a288-d3968278a95f | -18.68972 | -40.72352 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 893152bf-24c9-3203-a4e8-6fc966640e10 | -12.94767 | -45.92287 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11ffef78-71f4-36be-b29d-0c30920d993b | -15.67128 | -45.93813 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fc462dd6-efb1-309d-8b0d-a998bacf537a | -15.40523 | -52.70693 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd295559-685e-394e-9a43-acca8fa52eb3 | -13.38844 | -51.80679 | 2026-08-31 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e663126-7175-375b-9c1b-aaeccf092c07 | -15.55132 | -56.28483 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af4e7fee-c2d5-3ff2-a534-380abf392ad4 | -13.96615 | -54.40405 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f77cd5a-1859-306f-b50c-99c542299062 | -16.35602 | -51.00965 | 2026-08-31 04:17:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6b8c27a-610f-30b4-9425-7d61878dc3c2 | -12.80531 | -46.46268 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb62d8d3-9d7d-3a35-a287-3fcd3dd6d8f0 | -15.67519 | -56.28218 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc736d04-ae3e-3270-91aa-c3587ec7ffcc | -14.45325 | -42.64943 | 2026-08-31 04:17:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e98a0301-ce54-356a-b75b-94bffd552f51 | -22.04797 | -56.08835 | 2026-08-31 04:17:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa7859f3-7926-302d-a366-306cbdf067a6 | -15.40791 | -52.70566 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21c3bfc3-ae88-3896-87cb-1b38eb6de706 | -14.13885 | -52.80327 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f9468b-5fd9-34a0-a24c-8ba882064546 | -18.28481 | -52.68106 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74b9a225-67fe-3987-9787-55d7152e2937 | -14.39077 | -52.54607 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f51b4b8a-ee67-39cd-8b52-7804b822ddf6 | -14.13094 | -52.81551 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39556114-d35b-38dc-a1a3-d180f36d7a2a | -15.62655 | -50.09504 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4c9c1d0-b7e8-3a0e-80c3-0d757f6822f7 | -14.89816 | -44.80519 | 2026-08-31 04:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89bc6c8e-89da-3719-8069-86198c9d1ffc | -16.57516 | -50.40442 | 2026-08-31 04:17:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 093e61b0-3279-37c8-9b8a-94cce57ba837 | -14.58299 | -54.08845 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59a9bd70-2019-3c4e-b10e-89e112a08e17 | -15.02434 | -48.16496 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d774315-a096-37ef-9d92-5ca59196017d | -16.28479 | -42.58062 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a7b15e-a02a-37fb-8eb2-ed375825ad19 | -15.90265 | -42.39903 | 2026-08-31 04:17:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 18120dce-08fc-38f2-a5d3-e7678acc0066 | -15.88459 | -46.02711 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc17eef1-bfa7-3b0e-996a-da67b6a52c5b | -14.42139 | -56.27226 | 2026-08-31 04:17:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c80cc46e-837c-320d-8a78-03e6d348c507 | -12.91452 | -45.90451 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7772acfb-45db-3076-b55a-aa1b570a255e | -14.44332 | -52.5237 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cbd9743e-529f-3b32-97b4-e2ef813cb877 | -12.92261 | -45.85633 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4cd32d1-56eb-322c-924d-9e5e9266bbd1 | -17.5361 | -44.61255 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92036108-6dfc-3457-82c3-ae8f76c9d3f0 | -14.39164 | -52.56867 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac4a68d9-d813-3c77-a627-4ba08bd8ddd5 | -14.19338 | -45.30899 | 2026-08-31 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ee58fa0-ca84-3bc6-89e4-f4df7fc99a27 | -17.5053 | -44.22911 | 2026-08-31 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70b8f3b8-1d7e-34c4-a41b-29e730ccccb0 | -15.02523 | -48.15992 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1329e518-4ad3-3178-b00c-751b8a99f182 | -15.63002 | -50.10023 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f3611b-3d0a-31df-912e-8303f7db1fba | -22.04696 | -56.09282 | 2026-08-31 04:17:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bae873f-e830-338d-bf25-82db1b2895b6 | -15.19716 | -46.24755 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5238863e-18ae-3afb-9115-7b0ecf56fb7c | -15.06523 | -48.00053 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d11c47f-56e5-382d-9f94-6e32a74e5e0a | -14.17119 | -52.88168 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 908c5a78-d5a7-3640-8b27-8fb98edd28de | -14.26976 | -52.88319 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc158b85-d3bf-3459-9ac6-398cd2089ccb | -15.66212 | -45.91306 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c39b1d4b-a832-32bb-8e5b-a8d6f49adb6d | -16.28535 | -42.57691 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eae9260-7a84-343a-a498-ad36a4d3cff2 | -14.59803 | -54.11105 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4c2f7f7-b9af-3ba3-adda-d72907b9ec72 | -15.19157 | -46.23821 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b783dbf-56cb-3266-9b02-d25aee6fbb94 | -19.32597 | -46.0667 | 2026-08-31 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b2dd7ab-b1ab-345b-9b58-0d1d3b3329c8 | -14.60052 | -54.09911 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fbd0bb7-ffbb-3ea4-b541-0edf7df4b840 | -14.23256 | -52.8495 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ea3cd2e-4de8-30d3-b7af-c340b1d1e716 | -18.27433 | -52.70781 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 792513b7-098d-367a-9c11-eb6038cebb2f | -14.19601 | -46.56243 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fb35f89-493c-3048-894c-09eab8af8822 | -14.4369 | -52.52923 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e684589-221b-3eac-81ca-3454e9734dc0 | -12.91317 | -45.91255 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cb6ee048-0847-3915-9395-174bf09bcc1c | -12.89939 | -45.84406 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee85ac58-4bb7-381a-879c-ae4463a3bce4 | -15.61791 | -56.42099 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1be7c0a-41a2-369d-9e57-53b0176ab1e0 | -14.22587 | -52.85559 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b581c48-6626-3812-ae85-e9d6270e17a4 | -15.667 | -45.92625 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa33dd3e-de93-3d14-94ce-8e75dc45a803 | -17.2484 | -42.80163 | 2026-08-31 04:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5dc066d-4127-337d-b202-6100dff22a91 | -15.70767 | -39.89656 | 2026-08-31 04:17:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02dda87a-38d2-3ad8-bd44-3208bff32a0c | -15.12278 | -53.58658 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dcacbdc-bd3b-3035-87b3-32ae72c20c0c | -14.39596 | -52.54687 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41bba93b-ca4a-33c0-9901-1f11e437a4ca | -13.84995 | -54.08987 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15910786-dfff-3e17-9035-a651f47d931d | -18.52486 | -42.85217 | 2026-08-31 04:17:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9e409383-c29b-3489-8f6d-d981439fb9b0 | -13.38497 | -41.3274 | 2026-08-31 04:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 773854cb-fe4c-3773-b02c-7e9691715a02 | -14.30461 | -52.89519 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98af7674-f7b9-3a15-bbac-b633c2b761c0 | -19.95273 | -42.30436 | 2026-08-31 04:17:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3bd20f8-00bc-3682-818f-96a52c6b3cdb | -14.57878 | -53.07821 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3be3c9f-45d8-3f25-83de-ea2716b7e50b | -13.06329 | -45.18069 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0dc319f-3cfd-3c4f-9ddd-aad009287b22 | -14.41063 | -52.52688 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82f77e23-8505-34bf-915b-832d1c374ebb | -13.84063 | -54.01956 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e7148ba-4d3c-3092-95d5-ef0f083736a6 | -14.17256 | -52.8749 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35a2a927-cbad-37fe-b96a-4124678ccb64 | -13.19544 | -44.07367 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 266eb8ca-26de-388e-a950-5857d08e8cb3 | -14.57949 | -54.08673 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf833844-39c9-3f13-b1ac-e70c9553f030 | -14.60196 | -54.12058 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf6f36a-6674-3215-a48e-649eaaeab99f | -16.27526 | -42.57514 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b6d3cb-50da-3f1e-a454-2123034241fc | -14.39847 | -52.53424 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 751ec59d-af29-3772-ab69-b622b206f8d6 | -16.28199 | -42.57633 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4494b0c2-72d3-3fa0-bce3-374bc62110af | -12.94783 | -45.94365 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72efca06-a577-3f9f-987f-b51b87a6e7f9 | -14.40938 | -52.53321 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e766c33a-f836-399e-ad12-bad1d4ea6cc6 | -14.57164 | -54.11544 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 127883fc-166e-3840-b197-d781b4348901 | -14.46765 | -53.35646 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38673149-fcc6-3d73-8f27-c16471749b04 | -14.17186 | -52.87835 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b042ef49-940b-397e-b0af-56ef2cc1c406 | -14.57672 | -53.0776 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e70719e7-f457-395a-aad8-d15dafd29a42 | -13.83417 | -54.02199 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c670b87a-9fbe-3650-941d-fcdc07c647db | -14.39532 | -52.55012 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b919511a-802f-322c-b5c8-c1991d87b3ab | -14.17896 | -52.87796 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07e3e200-b09f-39ef-924a-9d9ab3ce08be | -14.74462 | -44.64469 | 2026-08-31 04:17:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f910870-d54e-3068-b44e-942b0437875c | -15.66572 | -45.93399 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b5e8726-1c4f-3a52-b2a5-c1f487a3ac8d | -15.20685 | -46.23286 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d7dad5c-b3c4-3f94-b62a-9a37ec0a3f32 | -14.30713 | -52.90994 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac4c40dc-5a2f-3bb9-8763-d31836fa7fcc | -20.46703 | -44.41384 | 2026-08-31 04:17:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e96ffd9a-9524-3e4a-8447-71d34f12ba2d | -12.94917 | -45.9356 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c980ca-a000-3c4a-a3a4-0eebb7a31304 | -14.19956 | -52.87731 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
