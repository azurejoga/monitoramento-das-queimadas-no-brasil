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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e9998f-34e2-3303-ad0b-72012c3e9128 | -18.30256 | -42.36664 | 2026-09-28 16:22:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a2231428-aa14-3b56-a669-1566635e2e07 | -18.12291 | -44.38637 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f3b0455-8861-3314-b07c-518420dad8cc | -17.10535 | -39.51759 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 73a99def-f80f-3c18-9d6c-82a81418bef0 | -21.00474 | -44.06283 | 2026-09-28 16:22:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d77d4ba3-fce6-3bcc-9113-246aead8a987 | -21.28809 | -41.04306 | 2026-09-28 16:22:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0333f30e-0f70-3dc2-b8c4-1c29c257b86d | -19.15808 | -43.82588 | 2026-09-28 16:22:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e1c24ff8-71e0-3ccc-a242-a276d33c3553 | -23.10542 | -50.91668 | 2026-09-28 16:22:00 | NOAA-20 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 65d09022-a612-34f1-82bf-7809428595e4 | -19.41599 | -48.44444 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e79cd64e-7e30-3801-a326-8d35d51daf5f | -21.48295 | -45.15806 | 2026-09-28 16:22:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3bb87b3a-da2a-34a0-a1d5-7cb6f9ae5951 | -18.42773 | -43.98342 | 2026-09-28 16:22:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73115e54-1cd0-3aab-812c-6d8bfead64c8 | -19.51318 | -42.0206 | 2026-09-28 16:22:00 | NOAA-20 | SÃO DOMINGOS DAS DORES | MINAS GERAIS | Brasil | 3160959 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 666bc129-109d-31f3-b6e3-a2d023f11107 | -18.21802 | -42.50983 | 2026-09-28 16:22:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 42b5f2ae-5703-37d4-a989-ceea48bc7014 | -20.99964 | -47.06624 | 2026-09-28 16:22:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 799f2834-4a17-358f-b5b7-6b0508f870b5 | -17.02534 | -41.35603 | 2026-09-28 16:22:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b6c057f2-8977-3653-a068-1713803b7101 | -18.79423 | -46.46925 | 2026-09-28 16:22:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 367e9a97-72d2-394b-8f52-503313cbaeca | -17.92139 | -43.68034 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb997426-fbc6-3e9a-ab70-a050db1f27fa | -18.39655 | -42.546 | 2026-09-28 16:22:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 21fbfb3f-4f7b-3d45-87a0-c6232831c633 | -19.41567 | -48.44152 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2e19a88d-5e1f-389c-829a-f5af6824a402 | -23.11623 | -52.34982 | 2026-09-28 16:22:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 48ac67b8-374a-3b51-9985-dab9e0a0b6f2 | -17.82649 | -44.38546 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9bac6fc0-fae1-3343-a639-e4732b28ec56 | -19.23249 | -40.26794 | 2026-09-28 16:22:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 3277d6c1-61c8-3146-bca6-6979e14df711 | -21.85614 | -46.0629 | 2026-09-28 16:22:00 | NOAA-20 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4b367dc1-27a6-37e9-b5ee-9d91c66cff41 | -19.24532 | -46.62602 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 065e73ce-9c29-387d-bb4e-23cfec20b867 | -19.27719 | -44.11874 | 2026-09-28 16:22:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f559128f-72a8-3fb4-9ad8-98ebce270432 | -20.77041 | -51.31269 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| cb169fdc-fd48-39e6-90cb-180df3a2eb9d | -18.87163 | -46.6671 | 2026-09-28 16:22:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d1861114-73a2-3b3c-935d-83497112ecc9 | -18.51468 | -42.08783 | 2026-09-28 16:22:00 | NOAA-20 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 18c84909-a301-3c59-83ea-670171164a09 | -18.78005 | -47.3188 | 2026-09-28 16:22:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 504517e1-57a8-30e2-ab45-331321d0c7cd | -19.41489 | -48.44277 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8866118f-daaf-3eb3-bd40-5dd850071b97 | -18.83301 | -43.61888 | 2026-09-28 16:22:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 729a98c1-5cbb-3e6b-bd09-a703f60b1b56 | -18.08985 | -43.69036 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e86dba5a-00e7-374c-953d-275687cea318 | -21.40296 | -45.16544 | 2026-09-28 16:22:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5b82c8f-688a-387f-bec0-8442b21c0893 | -17.94297 | -47.00273 | 2026-09-28 16:22:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2252c4df-6d1f-3aee-ac85-4e4ec5072d1d | -18.76936 | -45.10438 | 2026-09-28 16:22:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ac444f20-a71d-3d0e-8e42-3b02beaed1cd | -17.89439 | -45.05692 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9f16026f-b2e4-3b82-af03-009b82a4d89b | -21.21623 | -46.70495 | 2026-09-28 16:22:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 6157e495-536a-3c9b-80d8-9ef3f3a3d295 | -19.75819 | -42.04855 | 2026-09-28 16:22:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| a24230c3-ff08-3991-94f8-1216ab540c50 | -18.34565 | -42.30755 | 2026-09-28 16:22:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2ccae835-8faf-3e62-8596-73d547ed4686 | -21.2363 | -45.62077 | 2026-09-28 16:22:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 55cc9a03-d55d-3732-b391-ec36f795527d | -17.28055 | -41.17641 | 2026-09-28 16:22:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 926e977e-3624-3853-a419-967929d4ba17 | -22.16094 | -47.36509 | 2026-09-28 16:22:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9f0d4521-2e63-37a3-96a3-7ea9faa2e690 | -17.72058 | -42.1789 | 2026-09-28 16:22:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7357cae8-bf0c-3a38-b265-b9884094329b | -19.77321 | -42.05447 | 2026-09-28 16:22:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e5d479e8-0f90-32e1-bd57-69a4d91d9bec | -17.85715 | -42.76077 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 50aada8f-61a3-3f0c-bc50-32924d1de48f | -20.17506 | -41.44053 | 2026-09-28 16:22:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7750c899-b2d4-323c-877d-3ad42a52e5c7 | -20.46091 | -46.22163 | 2026-09-28 16:22:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50c63e93-43f9-346f-b5f5-517ba0d8d5a5 | -19.9164 | -40.74099 | 2026-09-28 16:22:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 3871ae21-ba41-3717-8977-cc273b3893de | -18.09053 | -43.68873 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4844dff9-bcb3-30ea-96ac-93bc164c5017 | -21.54124 | -45.61045 | 2026-09-28 16:22:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 29ac82ec-df18-3bb2-98af-35373ef2c391 | -17.14961 | -39.41201 | 2026-09-28 16:22:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cfb723b6-3775-313a-be6c-ac555e8d226b | -23.13663 | -50.91858 | 2026-09-28 16:22:00 | NOAA-20 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 9155c8c0-862c-3463-9991-9d1a61a61941 | -23.58986 | -51.57704 | 2026-09-28 16:22:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 2e3967b5-3b98-36c4-ab56-119bba596ec9 | -20.53381 | -44.05519 | 2026-09-28 16:22:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6310f4c8-64b3-39e5-be63-012087e4fbdc | -18.09674 | -44.3646 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| a8f9e8ad-1df9-38f7-b7a8-4be89c1bb03a | -21.75036 | -46.11306 | 2026-09-28 16:22:00 | NOAA-20 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3295af36-9861-3d59-a2bb-23373e87457f | -18.71967 | -49.12911 | 2026-09-28 16:22:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b63418a0-393f-3d34-9012-263731acf72e | -20.06004 | -41.93795 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1f252822-4982-3d03-bc47-ebba7c8a207b | -18.24318 | -49.59167 | 2026-09-28 16:22:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 57dd4e40-3325-3262-b4e4-2af5ec4cf785 | -20.45507 | -50.00617 | 2026-09-28 16:22:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2d92e8b-d77b-3e20-92ad-1b5304230dcb | -17.82607 | -44.44088 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 546b6dd7-1008-362f-9d1b-f415403d6ac1 | -23.13083 | -45.74083 | 2026-09-28 16:22:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e67f2b86-0abf-3fa4-bdbe-ca53a8ee95b1 | -18.12482 | -44.37117 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cafc8d40-eb2c-3a29-babd-47ee5d81cc0c | -17.58053 | -42.27552 | 2026-09-28 16:22:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f8ebb1bb-feaf-3bb3-b7f3-4994bcf0bb8c | -21.33496 | -45.67875 | 2026-09-28 16:22:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c18d6494-8acc-3b87-8c61-19c23cb926d5 | -18.1082 | -44.39301 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e6078a0f-a6bb-3fed-8751-72e8c23d3e38 | -18.67975 | -48.62218 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ffcee748-8b74-3959-aeb5-ec4a5eab2748 | -18.10822 | -44.36324 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73d463b9-9731-3414-bf97-35d23af82370 | -20.95413 | -44.889 | 2026-09-28 16:22:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a1ac87bd-60cc-35dc-a94e-ffa38f949189 | -19.87702 | -40.65953 | 2026-09-28 16:22:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 05e34708-dbb2-3faf-af0b-40a6d280d044 | -19.859 | -41.97131 | 2026-09-28 16:22:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6afeb019-f1ef-3a90-8dda-ea893a2aec9b | -21.21882 | -43.99106 | 2026-09-28 16:22:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cf5e3816-8f48-322e-8608-fd66c7f0981f | -20.76983 | -51.30905 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| b128c842-266d-3ac7-b1fd-c973c13935fc | -21.62141 | -44.40109 | 2026-09-28 16:22:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a60dd429-e9b8-3cf6-a0dc-1456bd7e256c | -21.63948 | -46.3714 | 2026-09-28 16:22:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e6feb963-9269-3723-81b3-eb10c2ac988a | -19.06214 | -40.443 | 2026-09-28 16:22:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 41c6aeda-cd56-3cc5-81ea-7752ee29df00 | -19.88684 | -43.95461 | 2026-09-28 16:22:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 17026985-f255-3d8a-b61f-06f9cc55537a | -18.71122 | -43.2145 | 2026-09-28 16:22:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b174ab6f-5155-36ce-b2af-1d5ce935e290 | -19.41535 | -48.43859 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 53895331-446d-36c2-9041-6b592fa4bf26 | -19.24477 | -46.62131 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 13c8ad18-c08f-3527-878e-f8b8d9402604 | -18.77433 | -45.1113 | 2026-09-28 16:22:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96ce76c2-5068-3e9c-a632-2652dddee9fd | -20.31924 | -43.16156 | 2026-09-28 16:22:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f4591ad8-53f1-384d-9c84-ffb760b199ce | -17.79104 | -41.72221 | 2026-09-28 16:22:00 | NOAA-20 | POTÉ | MINAS GERAIS | Brasil | 3152402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc930a27-3ecb-39c8-8841-bbfc3d480dbd | -20.0479 | -48.04839 | 2026-09-28 16:22:00 | NOAA-20 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b392ddf1-0e9b-3157-9a17-d7cfabe02081 | -17.67238 | -42.01254 | 2026-09-28 16:22:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 840774be-c01c-30a3-850d-3b11ad032445 | -17.83095 | -44.3898 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ae3e791f-cfd4-324e-859b-f7c980a4be08 | -17.81332 | -44.43275 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c751b2ca-30b5-3d47-a2a9-27dc5ec609b5 | -18.43899 | -43.98187 | 2026-09-28 16:22:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aec42a97-add5-320f-a883-a47a72cc16eb | -23.11577 | -52.3435 | 2026-09-28 16:22:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| b668660f-c687-3ea5-b68f-9d8a8d1e91d7 | -23.32125 | -50.91049 | 2026-09-28 16:22:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 49dbf7a0-65aa-37c1-b704-94c8c5b24486 | -19.54667 | -45.26837 | 2026-09-28 16:22:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c75afccb-bdb0-32df-a28f-be8f3cd2884d | -16.78733 | -39.41505 | 2026-09-28 16:22:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fe125259-d26f-3657-b2fc-23022fe07cf9 | -19.40953 | -48.44041 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2eefc592-dc6a-3daa-a33b-5fb464981717 | -18.53034 | -42.397 | 2026-09-28 16:22:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6d521dfd-db62-31d0-b10c-99b7ca3feb17 | -18.00958 | -44.02668 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5ae6f541-470f-39be-8ed2-a308ee6ffe41 | -18.9778 | -48.09863 | 2026-09-28 16:22:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d54ae4fe-6748-362b-802d-b3ed34504736 | -19.25882 | -40.73908 | 2026-09-28 16:22:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3b094ed8-fa9e-3a56-bb0f-d46583df5248 | -21.04995 | -45.75036 | 2026-09-28 16:22:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b2b9dcd1-ec4d-3398-a1fb-82d823e9c086 | -21.7958 | -45.52605 | 2026-09-28 16:22:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c2d1146c-b796-32d8-9187-b28b0848be36 | -18.72002 | -49.13242 | 2026-09-28 16:22:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 73175f9e-e53b-3b20-a538-14734e351b7f | -18.68294 | -48.61769 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README93.md)
