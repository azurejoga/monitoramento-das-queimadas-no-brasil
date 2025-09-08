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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3473e443-27dc-3dbf-bede-3649cd290f7a | -22.8385 | -47.14629 | 2025-09-08 04:04:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3b75e180-1c9e-3f3f-9070-1c99f4170da2 | -20.74639 | -43.22568 | 2025-09-08 04:04:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c609f9ff-e002-3001-b0bc-305ff2c38d21 | -18.95532 | -46.80182 | 2025-09-08 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 977d5994-b8d7-3518-8917-dbf019d73979 | -17.39578 | -49.31056 | 2025-09-08 04:04:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 44c8b542-425d-39db-8d70-a0ed56f8d9a3 | -16.53094 | -45.09679 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0f06370-6fd6-3943-8bb0-6fc49805c51c | -17.96564 | -46.89199 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a3384c4-e4cb-3b3b-b54d-44c2d4af7f21 | -17.6209 | -44.82965 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 715bfdc4-4c02-329b-8752-45de7bc13746 | -16.54223 | -45.09462 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f996ce-c0f1-34c9-8231-81e1535a8842 | -22.06802 | -45.1978 | 2025-09-08 04:04:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 333ad2c8-95d5-33ef-be24-e2850820f8eb | -19.45286 | -47.8807 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86ed5267-4c7d-39ab-99f9-21f9055ab7cc | -17.44388 | -50.2252 | 2025-09-08 04:04:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f7764e4-a77b-318b-a9b4-b4f792182823 | -17.64478 | -44.78463 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63148120-459b-314a-8e8f-10b0ad0505f5 | -16.97816 | -45.83094 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e8b1dde-416d-3b97-83f9-fdb998183870 | -15.76505 | -53.56107 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ef2646a-002a-340f-87b0-d07b0ac1331f | -19.82394 | -47.27373 | 2025-09-08 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8749cd77-54a2-30b9-97ac-dab7a516a4a3 | -16.33235 | -52.93639 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5abdc659-f7f3-34d9-95e6-33c4825109ec | -17.538 | -43.74199 | 2025-09-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d00703c2-fcc4-3ecd-8dc6-e83bf1bdf7e3 | -16.91079 | -45.80886 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c134976-2b5e-3c45-be26-2bd79f10f536 | -18.14121 | -43.39709 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5e9a6174-ef54-3def-aa63-00547c163037 | -22.69606 | -46.92813 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 78f01d3d-9e79-3108-b6fc-e29d16d5da67 | -18.14726 | -43.40194 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28a7ba41-da29-32d4-8647-ba69632a66b7 | -16.06164 | -50.48095 | 2025-09-08 04:04:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 267fb23f-2e1f-3f6f-a746-adfac13d998e | -20.92158 | -45.26786 | 2025-09-08 04:04:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce98aa89-6f43-3cf6-b9e3-1013c964a4cc | -21.21775 | -44.33311 | 2025-09-08 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 963171d2-4f52-3e5a-abd6-2e0baa31e9a0 | -18.14061 | -43.4008 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a8a03fa6-ad1a-3bbb-bc55-ac7c283c1f41 | -16.89307 | -45.77957 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef983071-e16d-3e54-901c-6d33f28caceb | -17.57027 | -44.54146 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 975dba22-4082-3f6d-8159-9b2fa6fe495c | -17.15172 | -44.44081 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 914ca6b0-1e70-3d3f-89c6-9a9c7e33d110 | -18.02965 | -47.11922 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 428c36a0-67fd-34ab-b1e4-09b58d39ec1f | -19.38198 | -44.50014 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcd73479-ecbc-3a1a-a887-994ec5cba0be | -17.58315 | -44.52785 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f16a0ec0-6bc3-370f-8da8-903d8170b810 | -17.26042 | -46.70295 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f2e6b96-9475-3614-b6df-21e136df1a39 | -18.02838 | -47.10445 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b8d7abd4-e07f-3452-8db9-99b328fcc218 | -17.65186 | -44.18131 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d635da34-c206-3752-85c0-c499415de727 | -15.27198 | -52.38732 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81f841d5-715b-34d7-9d65-79a0f8974ada | -16.5514 | -45.10484 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68c08495-0c05-3f4e-8f06-bf3a75ff76e3 | -18.65856 | -43.11616 | 2025-09-08 04:04:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e7f00902-2044-3658-b68d-2650fed955da | -17.15582 | -44.43748 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 977a0f9e-a267-3f5b-9feb-ce7f7665921a | -17.68436 | -43.57442 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 524ccec1-56d9-30f6-afc0-2543130cf5b8 | -21.22108 | -44.33372 | 2025-09-08 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c6202375-4337-3169-aad5-6b95dd998307 | -17.33851 | -47.03089 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edd3a8f6-16b1-3dfe-b460-e68677a51b1d | -16.5387 | -45.09397 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d865a17e-3fc4-39f1-9c36-5300a66542c2 | -16.33814 | -52.93713 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6da97f50-4a66-35f5-962d-0665ee1ab132 | -19.40928 | -43.66737 | 2025-09-08 04:04:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae8e9268-95d9-3e2f-bb0b-3a0dbfd3250a | -20.4713 | -43.97295 | 2025-09-08 04:04:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e91e916-94a2-3115-ae91-6fc8a464e4b9 | -17.53525 | -43.73769 | 2025-09-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7909e1a-e1b0-3caf-a4aa-6f89539aa9ef | -19.63355 | -46.58357 | 2025-09-08 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3235b49f-ac8b-3f04-b002-d43fe77dcf14 | -18.36946 | -43.89474 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e09512e7-204e-3304-9f34-3320e54a3414 | -16.89609 | -45.76208 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f1ece8-637c-383b-9ac3-433a1ecd0670 | -15.24496 | -52.36102 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 098355a1-d88c-3071-bd2b-689e2d574a69 | -17.16263 | -44.43887 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c92fbfc-e9d8-385e-9312-b37e1714a722 | -15.23933 | -52.35996 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bba321bf-a8ed-32b0-8f68-b673972c9ece | -19.59924 | -43.6896 | 2025-09-08 04:04:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 104e8b4c-b821-3869-84ee-686faceb9a6a | -15.73891 | -53.53748 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99618649-336d-3d76-8ca9-738bb654797f | -16.54576 | -45.09527 | 2025-09-08 04:04:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4433bcf9-3432-38d3-a4ab-3523c84154c1 | -22.70241 | -46.93398 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4370ed3f-7644-393f-8739-68703fff5297 | -17.58935 | -44.53287 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d3742eb-1c2d-357e-ad5a-1b0027dfc9be | -18.03838 | -44.32767 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 536c6526-3233-3f6a-b082-779dd4ae21f2 | -19.94948 | -40.75362 | 2025-09-08 04:04:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6b964eab-2c8b-3d6b-a486-d7c07aa2316c | -17.58052 | -44.5434 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e0888a1-0faa-3baa-b1e5-2f48bb8519cc | -16.28276 | -45.68386 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b252a0bd-01f8-3c41-8297-e631862e1941 | -17.5386 | -43.73827 | 2025-09-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ceb0e65-13fc-38b7-ad29-25a1c3889001 | -16.90893 | -45.84047 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a858b47c-6737-3a07-863b-64b953d87ae6 | -15.75998 | -53.55563 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b434d32-a0dc-38a7-85e5-68145b5a6f0e | -15.82643 | -52.27269 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf0e6028-84f2-31d7-9b26-e2f04fbcd4d2 | -15.22635 | -52.35341 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61f85cb5-bdf4-3ff4-b768-01db4eb8dbed | -18.04551 | -47.09735 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8c2c672-8432-3303-bdff-25876d2e45bd | -19.37734 | -44.50714 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9c69f7a-999a-3862-9034-c31501553b17 | -16.52033 | -45.11612 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4084fe-6559-3647-8e52-33060d4f279f | -15.76313 | -53.57005 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28204790-df11-335a-83e1-fefa07ea4d8f | -19.20891 | -43.73106 | 2025-09-08 04:04:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eec4d3ad-532b-34d5-a4a1-3707ec4ee0ec | -16.93796 | -45.78235 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3aa1a1b7-2344-3977-be92-d4ce8943f1b2 | -18.02197 | -47.11783 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 522d5c97-7058-3885-8201-34427bcad61e | -17.66755 | -44.1917 | 2025-09-08 04:04:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84dc427b-1214-302e-881a-418e86beffab | -15.96474 | -48.10584 | 2025-09-08 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec1542e5-fd01-3dc3-bc17-7f4285048463 | -17.17011 | -44.43632 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6f1292e-6bdd-3305-8eec-92b08ab61f84 | -16.91143 | -45.84717 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e5b4b1d-81f3-3e9e-a169-41054c90b992 | -17.16538 | -44.44347 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a94cef2-dd30-3d0b-beea-8c188ebdf67b | -16.91101 | -45.80585 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60185e98-74b5-3bb6-a2a6-ff426ccc0cba | -16.27912 | -45.68319 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a5dfd648-6556-3043-82e4-31b19481bea3 | -16.41733 | -47.82237 | 2025-09-08 04:04:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b39c9085-c943-3815-9f7e-1fa6e206015d | -16.89518 | -45.78899 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ddd74b-b5e0-314c-bd60-c8c6d85a9830 | -16.3038 | -45.69232 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 042126af-779b-3f71-9094-0a7f17184092 | -16.29254 | -49.55508 | 2025-09-08 04:04:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bd3dfb11-0020-329a-bad1-343b640104cf | -16.32661 | -52.93537 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f57fc74-0aa4-3deb-a1ae-c2131391e821 | -16.96782 | -44.53338 | 2025-09-08 04:04:00 | NOAA-20 | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3701522a-0196-39a7-aebb-8088d4eac659 | -18.04255 | -47.09185 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de41aa7c-b2bc-3681-a9d2-079691dd7bdb | -17.22472 | -48.2861 | 2025-09-08 04:04:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09a42235-eb2b-39aa-92fc-3ad1edec2bfc | -18.04337 | -47.08733 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac7a0124-068d-3ef6-b3a3-265465d16c91 | -17.21998 | -46.70993 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9733a6c9-8d35-312a-a6ba-755caca3d857 | -19.39695 | -44.51471 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 601b5ad9-dc6b-3c57-9dfd-acff3314771f | -18.35395 | -43.92627 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f368d7cc-0f8f-328b-99f8-0b4a9bf60ef5 | -16.93745 | -45.82781 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44008d90-3fc5-36d4-a669-217ef7dc629f | -18.24003 | -46.62069 | 2025-09-08 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 947a775d-ab5b-35d0-b154-0bd8fd5e45dc | -17.95926 | -42.77263 | 2025-09-08 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f758dfd7-4ef4-3945-8113-96bb7a98ebe0 | -17.94991 | -45.28962 | 2025-09-08 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c01e465-58e2-3368-9d4c-0cb28bad5f33 | -22.69326 | -46.9231 | 2025-09-08 04:04:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 639d34f2-cd28-3f63-a212-02068ec5d8de | -19.59532 | -43.69268 | 2025-09-08 04:04:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a69a7b9-8000-3429-bf5e-e41c57983621 | -16.93434 | -45.78165 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bad7189c-1948-36ea-aec3-d9ca2987c835 | -18.03773 | -44.33151 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README50.md)
