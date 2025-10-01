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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17b8227c-809c-381c-90e8-30344144dd02 | -23.41999 | -49.45779 | 2025-10-01 04:23:00 | NOAA-21 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5872a835-9228-338c-b0cc-57451fb5c891 | -17.9585 | -45.01875 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f390c5a-04d8-3cbe-9e7e-34bacbf98488 | -18.97095 | -47.8751 | 2025-10-01 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d31a7e2c-3fdd-39bb-b025-ac0026f231e9 | -17.86722 | -47.14555 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaec5bbb-f774-367d-9987-5fd9e9b8b1b9 | -18.71565 | -49.16685 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 009e7843-a2f1-3f55-9dc0-2d98a32bf654 | -20.23741 | -43.8833 | 2025-10-01 04:23:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ae193fec-2e1c-3937-a08c-b9d3301eeb6e | -22.25174 | -43.42145 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8d98c72b-4c74-396d-97f7-821ee1b23c69 | -20.68868 | -43.37339 | 2025-10-01 04:23:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3a60b5e7-eab1-394e-883a-7f14e20278eb | -19.69292 | -43.68421 | 2025-10-01 04:23:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 551da0f2-8488-3963-89a6-e854b825ffbd | -22.4122 | -43.16513 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bea7a12e-7078-3a1a-8f99-fe3779c3307d | -22.97943 | -48.3669 | 2025-10-01 04:23:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20663300-08eb-31bd-b45a-c9157dcaf4dd | -22.28617 | -42.55897 | 2025-10-01 04:23:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d1af5a8-d9a2-3be0-9f5b-94f04809e299 | -19.93481 | -43.89276 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1006de57-9135-3b0d-9a91-ce1b7d0ea30a | -18.70352 | -44.33342 | 2025-10-01 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63574d99-19b1-369c-bc8a-ca2392042f61 | -20.88865 | -46.5227 | 2025-10-01 04:23:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7eaa05a7-9301-32af-bcee-e38e311dfe06 | -20.48249 | -43.95306 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 19ff44cd-441d-3751-863d-0509eeca6c69 | -19.83941 | -46.71518 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35c539eb-7ffb-3840-990d-c26a2f4f99de | -22.27491 | -46.71637 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b0f4b522-23d5-3c91-bf83-bb915e5c5e7f | -18.44876 | -48.03436 | 2025-10-01 04:23:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1112b312-9bca-3a60-9c75-011982b0b476 | -23.48907 | -46.76395 | 2025-10-01 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 379fbb02-4b55-3ad9-8de2-3b84636687dd | -18.16462 | -46.1041 | 2025-10-01 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8cf0d9e9-6ee1-3032-a904-dbe22648ed04 | -22.12378 | -44.68706 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eab557cf-9a94-351e-bc81-a6c08d6045b2 | -18.91919 | -43.11627 | 2025-10-01 04:23:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ffb6e68-625f-3103-a484-31d17815afac | -19.85065 | -43.65765 | 2025-10-01 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8c9421ce-7cc6-3174-b191-b8a2471c3e4a | -22.58736 | -46.78205 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 104ee393-6dbb-33ef-bdb8-9a870a44afc0 | -22.26475 | -46.71454 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d5cec1cb-8d3b-37cb-b9ff-03cdbad2c71e | -17.73716 | -46.64167 | 2025-10-01 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dc40384-a6cb-326b-8ef8-bfc5040aa5fc | -20.63122 | -46.22075 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c553f92-afe5-3527-9570-f6f60d189a02 | -22.41727 | -45.11577 | 2025-10-01 04:23:00 | NOAA-21 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5ad3632-db32-30ed-b19e-7eca4fa8a3ed | -19.37812 | -42.78176 | 2025-10-01 04:23:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 37202877-bcce-34fd-854e-786601bd37e7 | -20.48374 | -43.94379 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d21064ba-7f3c-3dc2-b5c6-2042e217cb18 | -19.83054 | -43.08628 | 2025-10-01 04:23:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 958569b0-525a-3f8b-8ae5-e08e6dcc08b7 | -19.63638 | -46.55103 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 593095dc-80f3-3a6b-b4b9-224087af14a4 | -19.71117 | -45.87728 | 2025-10-01 04:23:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1f8644d-a888-342c-9a5e-149af37db04f | -19.64141 | -46.47118 | 2025-10-01 04:23:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f47c7b2-6585-3cc2-b62c-b8836b16bcc1 | -20.11974 | -46.3381 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96a52f52-b00e-3c64-a5fb-cf3dbdc5c278 | -23.19785 | -45.10503 | 2025-10-01 04:23:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5bc4a25e-9a5f-3387-ba59-fc923d7db2ab | -19.32016 | -43.87838 | 2025-10-01 04:23:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd6e4ca4-dffc-3a59-b943-3d4093810740 | -18.71229 | -49.16624 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15d335eb-c435-3fc0-8368-46d5c66de5fb | -19.46729 | -44.28449 | 2025-10-01 04:23:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc4e72e7-4896-3d19-bfad-c9a862bf73ce | -22.35944 | -46.92937 | 2025-10-01 04:23:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03c887bc-e09a-3a64-88e2-c4cb4db124e3 | -20.49706 | -43.9369 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 537159c2-c390-3bd1-8db5-db6b545ea16b | -23.22463 | -49.40206 | 2025-10-01 04:23:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 425ec090-496f-3c06-996c-3e2d86b3f041 | -19.5073 | -41.70494 | 2025-10-01 04:23:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b9e08c37-47d5-31d4-a306-29cc7037e37d | -18.6062 | -43.2673 | 2025-10-01 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 21c3d4b7-5cc5-309f-8c81-a3bbca31a9e7 | -21.04073 | -45.6794 | 2025-10-01 04:23:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71963fda-bd40-361f-8820-d697aa91e9ee | -21.01636 | -45.18072 | 2025-10-01 04:23:00 | NOAA-21 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a527c282-e0d8-3cf4-889a-47b46b790890 | -19.21087 | -44.02899 | 2025-10-01 04:23:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22377ab9-4244-3dd8-879b-c4badc04d504 | -23.36144 | -47.16113 | 2025-10-01 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2c3912cc-ffce-35cb-89a3-17cdc3c12a4c | -18.96765 | -47.87453 | 2025-10-01 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9362e6c-fa13-3c7a-a447-f91fbd9a323f | -22.5885 | -46.79826 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 673a85ca-7531-33cb-af50-936dabb700cb | -22.11665 | -44.68855 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e15ba151-9cfc-39b6-833c-68286a12bb2f | -22.44009 | -48.31372 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fffd915-fef3-3097-8bf1-6369edaa49e1 | -20.62499 | -46.21574 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebe58743-b029-3292-ac42-2983dda15d35 | -23.38501 | -46.41646 | 2025-10-01 04:23:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6afe0706-d29c-3d6c-a091-4e657cc71ab9 | -23.24794 | -46.78684 | 2025-10-01 04:23:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f9cd9caa-349d-3e29-8618-69e44f058e6f | -23.16226 | -48.08339 | 2025-10-01 04:23:00 | NOAA-21 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0ce19b0-01ab-324a-862f-7d2aab2bcef2 | -18.30915 | -46.61203 | 2025-10-01 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b22f97-9a2c-3958-a2bb-aed154bb7562 | -19.88996 | -42.62859 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 295f7f9d-7d3f-3f96-b171-00332ea37a25 | -20.0331 | -44.53924 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 192be74a-add6-3751-8136-7a05ef89ac57 | -21.21997 | -43.92278 | 2025-10-01 04:23:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db3c5be7-2691-3f5c-9bff-de6a294eadc4 | -19.52213 | -43.89925 | 2025-10-01 04:23:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 869fc7cf-4d31-367c-9954-87e2db070db6 | -19.90154 | -44.49312 | 2025-10-01 04:23:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f2e9390-2d98-3990-a540-f7922a4e7a3c | -18.96359 | -43.70905 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 738e091e-72be-34d8-9f75-15e0f0f22b37 | -17.84024 | -46.16269 | 2025-10-01 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a218de-3863-317d-9f3d-67e2f99df36a | -20.28183 | -46.24076 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63aece3a-87cb-3e15-97d1-9f689d1dedbb | -18.31248 | -46.61258 | 2025-10-01 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7334932b-145a-3c33-9394-45d6f4370927 | -20.02947 | -44.5388 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f2830099-3247-3a53-8be4-8ea9df8e3345 | -18.71513 | -43.17429 | 2025-10-01 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a2d7c5a0-4d85-3300-8f6f-f1628232c40d | -23.16558 | -48.08397 | 2025-10-01 04:23:00 | NOAA-21 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fafffcdd-f593-3e36-91da-1cbcac277523 | -19.89429 | -44.49207 | 2025-10-01 04:23:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 367edd30-f6eb-3151-8bd1-beba0f8953cf | -18.7113 | -43.17369 | 2025-10-01 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5f73ff40-21f9-3d40-9d55-40825b4948e6 | -23.58721 | -46.21799 | 2025-10-01 04:23:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a6d5f605-f9e9-3cca-b41f-95d4bcc8b52d | -20.6352 | -46.21733 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d47eb87a-1874-3fd7-9e68-2e58eb24df5d | -20.63179 | -46.21681 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fba7a873-b509-3e6c-bf0f-f4f36686ef9c | -17.97124 | -45.02893 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df3c3e91-262b-39e4-8afa-bd03441726ae | -19.90092 | -44.49769 | 2025-10-01 04:23:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 01e399f5-69a9-3ef5-8505-b1be63fc8981 | -22.26364 | -46.71553 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d7ee72a-d764-3caa-8817-a5b66757376c | -20.48013 | -43.94958 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| b5d9a944-6443-32c3-99de-8a936c699bb6 | -18.61392 | -48.67937 | 2025-10-01 04:23:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73fdd309-c7f3-3859-be63-76c5a42fc6dd | -20.59885 | -45.88632 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3c1e626-1d4a-35c4-8948-924024f2dd8b | -19.86746 | -42.57986 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5da4263a-e09d-3497-8205-d0f82248cf2f | -20.59942 | -45.88235 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ec0860c-56d6-3d82-ae15-5457a00fd702 | -23.17028 | -45.73393 | 2025-10-01 04:23:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a58eaa05-b63f-330d-b1c8-ff95177c325d | -21.68675 | -45.60575 | 2025-10-01 04:23:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa5ddc57-fd4a-37f7-bf56-30c2ff701193 | -22.62724 | -49.05011 | 2025-10-01 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 44792f4e-da36-3d7d-b254-22e6566bbffa | -20.83706 | -43.01743 | 2025-10-01 04:23:00 | NOAA-21 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7552ce32-d05b-3d35-a119-fd229a451d37 | -22.08702 | -46.56225 | 2025-10-01 04:23:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e88fdc10-5eaa-3be5-96b5-f2b2aed10d47 | -20.47288 | -47.37875 | 2025-10-01 04:23:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fc8db71-b5a2-3951-a0e4-ebe49e4bc042 | -20.1218 | -51.80953 | 2025-10-01 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d3b41b2-ebda-30d5-943a-c3b07e3c9ffb | -22.58397 | -46.78148 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 4a0e619d-cbc9-352d-ba46-eb3350ad8d03 | -19.34482 | -43.97658 | 2025-10-01 04:23:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a84786f-0c1d-377c-8aeb-d9dfcf411125 | -20.63804 | -46.22172 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 43b49c19-a578-3488-9663-5b3ed9a8582b | -18.61 | -43.26793 | 2025-10-01 04:23:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 46a09867-5ae3-3f1f-afcf-83b718728cf7 | -20.9675 | -45.80655 | 2025-10-01 04:23:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63590233-29c7-3248-9989-9acf9bd74f1b | -18.32161 | -44.77371 | 2025-10-01 04:23:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4b7bbf4-a8fe-3a94-a76f-10a0c8807037 | -22.26421 | -46.71167 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b58be672-7758-3cc5-aab1-5129848d7246 | -18.89738 | -47.21106 | 2025-10-01 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be5bdae8-4ec2-3672-a0b0-1183502013da | -20.32998 | -45.36469 | 2025-10-01 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5a68334-c526-3596-b8c7-8ddae2cee04f | -22.64672 | -46.75615 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README79.md)
