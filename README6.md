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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04bfe255-0238-3bc6-a99b-6a1974fb083e | -17.07066 | -43.69495 | 2026-05-15 04:38:00 | NOAA-20 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1a0d2c8-aeeb-3deb-ac4a-0de547ad4bcb | -14.10654 | -45.28732 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcd9f9f0-de55-3588-849b-a99f7633bc44 | -14.2162 | -45.44227 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1b8c116-6f4e-3009-85a4-5a07814f9282 | -14.9827 | -49.56457 | 2026-05-15 04:38:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d821a98-dde7-36c8-bf15-ea0918c7ba67 | -13.82433 | -49.39517 | 2026-05-15 04:38:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2fb79fc-c4ba-354e-b5e6-043817d674fe | -19.6918 | -54.35306 | 2026-05-15 04:38:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cb4c54a-ee91-39fc-86c4-1a08c9f4166a | -15.64593 | -47.92388 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e48a51bb-33d2-3906-bc7c-666be2afa993 | -14.30634 | -49.2449 | 2026-05-15 04:38:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b436a89-bb6f-3f1b-a660-93442f81785b | -15.64308 | -47.94284 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61d60062-c5b0-3f49-b02e-6aef3479fac2 | -19.68818 | -54.3523 | 2026-05-15 04:38:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42c64b2a-d019-386d-8b1c-aa39ab0f3b61 | -14.98326 | -49.56101 | 2026-05-15 04:38:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31ea78ad-5c23-3b7d-98d0-c178753f5c77 | -14.21042 | -45.45592 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ecccda-38ba-3a06-8532-5087c3dd830a | -15.42634 | -46.32282 | 2026-05-15 04:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 647c1a15-39e0-366b-bf4a-013433d37805 | -13.74032 | -46.50675 | 2026-05-15 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36098faa-f017-3741-930c-b7dbe072ca54 | -15.64822 | -47.93196 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f0e70ff-fe69-3998-b104-4ef8ea6b6e63 | -15.64765 | -47.93575 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc35d552-68d4-33f0-8540-f99b486dfb86 | -15.05533 | -42.95787 | 2026-05-15 04:38:00 | NOAA-20 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14252812-90ac-3808-8701-d7658a34572e | -15.64422 | -47.93525 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d9e37b9-31f7-3c09-a8e3-e51c45868f73 | -14.22198 | -45.42858 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3295aa8-f92c-37ff-a8c4-d119577f4eb2 | -13.95746 | -46.03502 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47170ca7-e18e-30b1-93fe-9e89f86df431 | -14.2307 | -45.44921 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36e2096c-4aa1-389e-b10b-53b8cf4863fd | -16.87901 | -52.42979 | 2026-05-15 04:38:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5089e47-2fa3-3456-aca5-e7aa454c6a09 | -19.20525 | -52.62823 | 2026-05-15 04:38:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45e3c72e-6d70-3d82-a2f6-a00864c1054f | -14.31131 | -47.16635 | 2026-05-15 04:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54041bc0-5775-3011-ac39-2523f5086350 | -16.69825 | -48.80825 | 2026-05-15 04:38:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e98a7898-2029-39ba-be13-3f84c0146ddf | -14.22824 | -45.43918 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c0bb087-0370-3729-924c-b845e454e57b | -13.95809 | -46.03067 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef42841a-8ef1-3855-b184-c19421183aab | -15.30614 | -47.36907 | 2026-05-15 04:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8d24cf88-51cf-3dd4-9c4e-9a567a8d6a4e | -14.20416 | -45.44532 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c7c2a0f-2a2c-3865-a97e-e93ad6611166 | -19.20459 | -52.63215 | 2026-05-15 04:38:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dda7f9e4-15d7-367f-bd28-4cfab62fe02d | -14.98601 | -49.56512 | 2026-05-15 04:38:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73d051c-73cd-3c3d-9e55-79b2db39110d | -14.20169 | -45.43528 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62c126af-9ef7-3f09-a390-83fa51eaba38 | -15.05594 | -42.95321 | 2026-05-15 04:38:00 | NOAA-20 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b8fba09-1e2e-30ab-929b-e34495ecab18 | -14.76205 | -56.59333 | 2026-05-15 04:38:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdadcaa8-bfec-3557-b83f-013e5af093b5 | -14.21421 | -45.45648 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c5a389d-04e6-3805-9606-4e9eb8fb85b3 | -15.05767 | -42.95642 | 2026-05-15 04:38:00 | NOAA-20 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b7e0d67-aace-3442-9384-2c4b44b37be5 | -19.9817 | -47.1989 | 2026-05-15 04:38:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c3c0704-234d-3973-b714-6df37c431f89 | -15.11392 | -43.96633 | 2026-05-15 04:38:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 947e2636-11ef-3418-9d36-bb8c16504cfb | -14.23003 | -45.45396 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ebb87c7-15e7-362a-8564-3b5eceaae4b6 | -15.64365 | -47.93904 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6204ac29-c344-3a22-8bea-89e550f61307 | -14.17806 | -52.86753 | 2026-05-15 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ed5518e-8c88-33a2-a9ce-5bc6611c5462 | -14.22378 | -45.44337 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07308919-218c-3410-b281-c5f64b21eaa9 | -14.2289 | -45.43444 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4efed552-6c4e-3bf2-8c2c-c4e4587a2032 | -14.22624 | -45.45342 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0eb808c4-e253-3230-b909-88d933a887f1 | -9.4765 | -40.3613 | 2026-05-15 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 938b0502-54d1-396d-84fb-6d1d22f82f04 | -9.4578 | -40.3392 | 2026-05-15 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.3 |
| e1261414-c910-3ecf-8911-d6bdcabd4878 | -9.4769 | -40.3365 | 2026-05-15 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 224.7 |
| 8ed020df-0544-3500-ad64-9a26954497e9 | -9.4773 | -40.3116 | 2026-05-15 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 5ee54525-7c90-313c-863e-5d2d3960cc10 | -31.55534 | -52.74662 | 2026-05-15 04:42:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 37f7fdcd-d914-32e2-b27d-0dd5d5e36573 | -9.4769 | -40.3365 | 2026-05-15 05:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 9da7d9a9-4abb-3bea-b419-31bd371af2ff | -9.4765 | -40.3613 | 2026-05-15 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 78f41d1e-8819-31c8-8332-9f27219cad38 | -9.4773 | -40.3116 | 2026-05-15 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 5d15b387-166f-3a1d-b35c-7933aec409f6 | -9.4769 | -40.3365 | 2026-05-15 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 200.6 |
| 5955e857-1861-31c6-a309-563fbee2814e | -9.4769 | -40.3365 | 2026-05-15 05:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 161.0 |
| dad5f439-f574-396d-94bf-da2dbd3437b8 | -10.67302 | -49.6944 | 2026-05-15 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91cd5ef3-0165-31e8-991f-62cdf18aa9ad | -7.63864 | -67.88776 | 2026-05-15 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.0 |
| c9d54580-b893-3710-a10a-9bf6261c44e9 | -9.45646 | -47.81998 | 2026-05-15 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7bcf4d2-d438-362d-82f1-a5d0e32c6f59 | -10.66675 | -49.69356 | 2026-05-15 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57e00178-a66e-3d4d-8cae-83a5c0b9b003 | -10.67241 | -49.69941 | 2026-05-15 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe5d2dc7-4126-342f-870e-038d11ef8142 | -10.67089 | -49.69196 | 2026-05-15 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f277da5-32f6-31a6-953d-ba914dd635d5 | -10.67031 | -49.69699 | 2026-05-15 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6beda663-5c27-3aa6-abbc-096011085fd3 | -7.6441 | -67.88367 | 2026-05-15 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 302a89c7-4e3d-3d6f-bd84-88eb5902ef01 | -14.18811 | -52.88094 | 2026-05-15 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf8b747-b356-300b-b809-54e731289936 | -14.17821 | -52.87272 | 2026-05-15 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff1019e2-5f13-30e3-9768-2258b4850df5 | -12.5496 | -57.21328 | 2026-05-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a7aecb2-946f-3777-8eeb-714814f00db7 | -14.1786 | -52.86939 | 2026-05-15 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f93dae08-f5da-3a01-a225-dab3942a5f40 | -12.54638 | -57.20763 | 2026-05-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11485d28-5fdd-3956-a20d-9eddf08515cf | -14.18771 | -52.88435 | 2026-05-15 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deb033aa-4b56-3290-9210-28967fc0d73f | -12.54569 | -57.2127 | 2026-05-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1e5e1f-5dac-3689-932f-f109aa251152 | -14.17899 | -52.86602 | 2026-05-15 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4adccc9-1d1d-3e78-941d-8b775f68f379 | -9.46728 | -40.33969 | 2026-05-15 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 058fca3b-9503-3b17-995b-a91bbdd188c1 | -9.47088 | -40.31827 | 2026-05-15 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| ccaa88de-fd0d-3962-872b-2edc48874572 | -9.47553 | -40.34866 | 2026-05-15 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| c1fd2533-4173-32eb-b5e9-50095132da54 | -9.47929 | -40.32724 | 2026-05-15 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 345b4de1-b42f-3b21-ad1f-f2f5f15a5247 | -9.46612 | -40.32501 | 2026-05-15 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 2458276d-d076-310d-a06c-a8d9c57b9a2f | -10.1216 | -47.9154 | 2026-05-15 12:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ca5e5362-1e67-3a0d-91ea-158dbb99e15f | -10.1216 | -47.9154 | 2026-05-15 12:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 922c53a3-af12-3090-8761-89e6324cc373 | -10.09731 | -51.64127 | 2026-05-15 12:17:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ce95204-c588-3bcf-a488-0dbdd2dfc45d | -10.12477 | -47.91245 | 2026-05-15 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 51202b12-7344-3f44-bd7a-90625c6c463d | -8.55222 | -45.97581 | 2026-05-15 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 4b6b6846-9b7e-36d5-95e0-c43660c429ff | -8.71842 | -48.32307 | 2026-05-15 12:17:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 094d9264-7b91-3bb0-a80d-85a27ee70fac | -9.48044 | -46.06649 | 2026-05-15 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 991a074a-c66e-39a8-bc87-82bcc5cace5b | -8.72916 | -48.32456 | 2026-05-15 12:17:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3bdd6cda-d781-399f-ad04-acf0ff7a9e73 | -9.47825 | -46.07296 | 2026-05-15 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c7392588-9582-3a81-9d62-621a13dfdd77 | -10.12281 | -47.92786 | 2026-05-15 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 83651789-5b4e-36a7-99e1-adf279fc77f0 | -8.93228 | -45.63922 | 2026-05-15 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 17d69683-763e-358f-b0f9-89c19f6f31ad | -8.72735 | -48.33805 | 2026-05-15 12:17:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 93168df5-9bab-36b0-9601-9762291b9ff9 | -8.96974 | -45.66607 | 2026-05-15 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 37f8ca8f-2293-3465-a8b1-d02e10451678 | -9.47781 | -46.08735 | 2026-05-15 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| be4a8ac8-8772-3937-b901-2fb6837edb68 | -13.3765 | -54.25281 | 2026-05-15 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b58f9435-014e-3d99-9858-4609c060172b | -11.92914 | -43.39131 | 2026-05-15 12:19:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 7829886e-7cbc-392b-8d3a-e9e5383a7bc6 | -12.54465 | -57.21946 | 2026-05-15 12:19:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 9b1e15f3-d990-3f47-9e00-9b2ca55d240b | -13.69942 | -55.68652 | 2026-05-15 12:19:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62cd127b-d4f2-3ebc-a366-53914c7f203b | -12.62151 | -44.52058 | 2026-05-15 12:19:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 73af241a-66a2-3aa9-845f-57ba4682205a | -11.74692 | -44.51199 | 2026-05-15 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 204ce5e7-c29a-331d-8ade-2c4d61bcc620 | -11.74424 | -44.51707 | 2026-05-15 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ba291691-50e3-3242-9d0a-72e58b46cdc7 | -10.1216 | -47.9154 | 2026-05-15 12:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| eddb37c2-656c-3392-8e1b-5a160b639e39 | -31.12202 | -52.89853 | 2026-05-15 12:23:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 115.1 |
| 99cb1984-5bdd-3307-9039-cdc0d3ad5434 | -31.12361 | -52.88339 | 2026-05-15 12:23:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 32.2 |
| 54302b05-1014-3293-ba6e-f878e1a3b44c | -12.6205 | -44.5179 | 2026-05-15 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |


[Clique aqui para ver as próximas entradas](README7.md)
