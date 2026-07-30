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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 812607f2-2947-32dc-aeff-028fc5579eca | -10.20831 | -38.54824 | 2026-07-30 03:17:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae32e9d0-7a05-3d8a-adb4-edcd52fece86 | -11.9316 | -43.43784 | 2026-07-30 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5f7a04d8-bc0c-31ed-a569-9f0dd211ac86 | -18.2206 | -42.20584 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8c9107e3-6441-393b-bd37-89602829333a | -13.31624 | -43.59014 | 2026-07-30 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 86d4fac9-7427-363b-83fa-eda07f4be0a6 | -18.21973 | -42.2099 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3edb449e-5d21-3377-899c-b334959df94e | -15.37167 | -42.648 | 2026-07-30 03:19:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 49c04fd8-d95d-3294-ac3c-53bece1ac26d | -11.93343 | -43.43886 | 2026-07-30 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 100bc0d8-4bda-3c39-900d-984f040a2497 | -18.22551 | -42.21036 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bd8bb428-f3b2-3445-8ae5-caa95b969f76 | -18.23126 | -42.21094 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| cd79c1f2-8993-34f8-8549-0c5b1a3cbbd0 | -13.31993 | -43.58917 | 2026-07-30 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 57dc4905-1a08-3f01-be37-f6d646e0807f | -12.82273 | -41.95937 | 2026-07-30 03:19:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6a5ee5c-bcfc-35e0-b0cd-70fb3a10886e | -15.3721 | -42.64804 | 2026-07-30 03:19:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d85360c9-1b0d-3903-9d81-7e0aa8886da9 | -10.93672 | -43.0605 | 2026-07-30 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8019a5a0-c96a-3cd3-960a-ea1f0bd0e4da | -10.93545 | -43.06661 | 2026-07-30 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7bd08d52-74d3-3724-9527-7333d7b14371 | -13.78885 | -44.09146 | 2026-07-30 03:19:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa333d0a-a996-3e10-a33b-1f91f1e82d56 | -18.23041 | -42.2149 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b277384a-ff02-3a58-b51c-9855a5c98376 | -11.92482 | -43.43655 | 2026-07-30 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba823f23-f54b-39a5-8016-71249de6bc22 | -13.31867 | -43.59517 | 2026-07-30 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c22cc794-8acb-361f-8047-3d8af6a80930 | -11.92663 | -43.4377 | 2026-07-30 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a50d1fbf-271d-3f5e-bc23-96808ec58c11 | -18.22634 | -42.20649 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e11a8b7b-7533-32a6-a8c3-2fac32d63603 | -18.22466 | -42.21431 | 2026-07-30 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4bdf3b48-ed97-36ba-944a-a9915afe039d | -12.81659 | -41.95833 | 2026-07-30 03:19:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef7a36ee-3b34-3392-a8a9-a6e0c0127f94 | -13.31494 | -43.59615 | 2026-07-30 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0a434a02-66db-369c-9c84-d8aaec2dace0 | -20.34388 | -40.93768 | 2026-07-30 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83ad2918-e3e4-3ff9-8913-bb9f3fd60d34 | -21.35159 | -44.81479 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 430c2f16-14f3-3534-8d4a-713d87d4c1de | -21.3565 | -44.82151 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.6 |
| e1df7923-d804-3dd4-b6e6-cc4d06df5654 | -20.34946 | -40.9359 | 2026-07-30 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a0a79f3-3dc9-3b87-a906-c5c431e91703 | -21.61477 | -41.20522 | 2026-07-30 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e18c568c-230b-3f2d-847a-f92ccec7f028 | -19.51982 | -43.57076 | 2026-07-30 03:21:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b7c2fec-3aed-3d0e-9cf8-939a200f94a2 | -21.35877 | -44.81184 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| ec211fb2-400c-3fcb-a8f0-1527ba2ea580 | -21.35388 | -44.83266 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| f256a15a-c87a-3670-add7-286856c69320 | -22.28215 | -45.38099 | 2026-07-30 03:21:00 | NOAA-21 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 962ff667-791d-3560-bc7a-8f632f145179 | -21.75498 | -41.2798 | 2026-07-30 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c0d67473-4dd9-3ed0-add5-576310c2c89e | -21.35283 | -44.80947 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4deda79e-ce18-3bf5-bec9-3f6f443fa0f3 | -20.34447 | -40.93486 | 2026-07-30 03:21:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e40e44c-5f7a-3a30-824e-575a508f10b0 | -21.35765 | -44.81658 | 2026-07-30 03:21:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| 72d291ae-2f79-3848-8e7b-ce36e9ea4d24 | -21.49091 | -41.19968 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| c3552a33-b6e9-3b36-8345-9c5e06b03750 | -21.48724 | -41.19249 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 55c3ccbc-b35a-35a2-86ca-5dcdc08146b3 | -19.38638 | -41.44202 | 2026-07-30 03:21:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f18fe50a-c5ee-347b-b595-a01d7b8599c6 | -19.38565 | -41.44553 | 2026-07-30 03:21:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1df7d98e-91bd-331b-a58b-121e49859040 | -20.73057 | -42.04408 | 2026-07-30 03:21:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 430722ee-30c0-3e55-9b2a-70a80da344a7 | -21.49217 | -41.1937 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b186bd2f-79a8-3278-b85b-ef4b2f2deb64 | -21.48102 | -41.19738 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 156ae712-1012-3272-91b8-107426614e38 | -21.48597 | -41.19851 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f974ffba-7cb1-30f6-a51b-9ce33aa21253 | -22.76713 | -43.74018 | 2026-07-30 03:21:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61664b78-3bfc-3eb1-9141-0441ec9d6826 | -21.4143 | -41.1926 | 2026-07-30 03:21:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f5638d49-06fc-3e92-a31d-30737aa50436 | -18.2374 | -42.21 | 2026-07-30 03:40:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 5c3c4575-db73-343d-9085-c4a7c23dd655 | -10.9397 | -43.0593 | 2026-07-30 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2de88534-a5f7-3d36-b73d-18c8681fda4d | -18.2374 | -42.21 | 2026-07-30 03:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 6bdb458e-7ce1-38ed-b15a-706a27990141 | -10.9397 | -43.0593 | 2026-07-30 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0880a39b-cf15-3a2a-92bc-877e6efe2f82 | -4.90566 | -43.47155 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37d9c363-2cd6-3a6b-bbd5-cfd34fcb43f5 | -5.17496 | -35.67473 | 2026-07-30 03:51:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b7f3b64-bf97-3b7a-b2b1-77820b7a9de3 | -5.04473 | -43.26859 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57751c51-2e6b-3949-b427-47effc3e55f1 | -4.03076 | -43.26921 | 2026-07-30 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6426174d-8947-346f-800c-4702f722db39 | -3.17955 | -48.0281 | 2026-07-30 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 274a78be-a8cb-3c85-919a-e057bd2fe3aa | -2.90537 | -40.39449 | 2026-07-30 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9f5d9e25-6cf9-3a8d-aabe-fdeac185523d | -5.90139 | -35.72645 | 2026-07-30 03:51:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fd7a4109-bdc1-3e77-9bd1-f4f7ec06f208 | -5.90859 | -35.72403 | 2026-07-30 03:51:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b218a9cc-ed64-31e5-be7d-075b8b8de314 | -2.90472 | -40.39848 | 2026-07-30 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32e8fbfb-0a4f-3771-b7f8-38a6f953677f | -4.3918 | -47.75713 | 2026-07-30 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f78d6fb3-e379-3137-819e-18b7fe688a1a | -4.36938 | -47.76585 | 2026-07-30 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0928a2f4-e9a8-3c3d-a2ad-5f853c7fe9b4 | -3.04093 | -40.11996 | 2026-07-30 03:51:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0358679-78c1-3a7a-b14f-a6f083366a33 | -5.17164 | -35.67421 | 2026-07-30 03:51:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48b11f18-c177-3e48-bdd9-e69972d1df7b | -3.18067 | -48.02145 | 2026-07-30 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 260679ab-86c2-3d8b-8d13-035233bd6f21 | -5.13887 | -37.65176 | 2026-07-30 03:51:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 269b2ba8-c01e-35bf-8694-a5b7ebe833cf | -4.90869 | -43.47168 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17bf4632-7c64-39fc-88e6-8593d3bb795f | -3.17901 | -48.02188 | 2026-07-30 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8b1105e-7a67-3223-a75e-9432f87577a0 | -3.17783 | -48.02857 | 2026-07-30 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 082aaea3-4208-3058-84e3-8a90f3a6d809 | -5.90804 | -35.7275 | 2026-07-30 03:51:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd3d31f3-232f-3d44-82bc-2e1e06c6a08e | -4.90818 | -43.47472 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28a3fe63-cca8-37d8-b74a-a344e2ad5c16 | -5.04522 | -43.26569 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e02b26d-54dd-3f7a-8ac9-0c1f95674a02 | -4.90512 | -43.47458 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9219bfd4-0e31-3195-8abd-be3eebb673d0 | -5.12416 | -42.79473 | 2026-07-30 03:51:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30fc7634-0af9-3c40-90b5-70eae2a9c70b | -4.90307 | -43.47387 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a488323-b032-3c7a-9aa3-26c56c79343e | -5.90527 | -35.7235 | 2026-07-30 03:51:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c4241725-dcd4-388c-87cf-3f8a9613f0bf | -4.36962 | -47.77177 | 2026-07-30 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 988ada4b-3613-31ac-abe9-907bb174ee5f | -5.04887 | -43.27049 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 993a2b75-c6da-3320-bbef-42eafe647125 | -5.04974 | -43.26951 | 2026-07-30 03:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0284e972-6f51-3bcb-9ff2-46c159432d22 | -4.36829 | -47.77208 | 2026-07-30 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ee03a40-361d-3b92-be3f-5b0378d73bb9 | -4.03024 | -43.27225 | 2026-07-30 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb4b0adb-dd52-3ddd-8811-e14b5165593b | -2.90964 | -40.39519 | 2026-07-30 03:51:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b947dd8c-b9fb-34a4-aab6-d1d979d42301 | -6.18332 | -35.29494 | 2026-07-30 03:51:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a3374890-4f71-39ff-8a5c-eda3544e3032 | -4.46379 | -38.30592 | 2026-07-30 03:51:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49bc515b-2dea-377b-9fab-cd1e38848b89 | -4.38506 | -47.7558 | 2026-07-30 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e76bf458-0675-37ed-8104-d15774e8d151 | -5.90471 | -35.72698 | 2026-07-30 03:51:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 04794e17-5ee4-3e40-9ca8-1d75303813bd | -3.0403 | -40.12382 | 2026-07-30 03:51:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5cc934d-9ce5-353c-a361-24f1b971ef61 | -4.44681 | -37.92895 | 2026-07-30 03:51:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db9b1507-1a2e-34e2-9e7c-433eedc8dca4 | -5.50431 | -35.58492 | 2026-07-30 03:51:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 045105dc-5d4d-37da-8a7c-cc4d20589f54 | -11.92978 | -43.44068 | 2026-07-30 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 187a29f6-31df-3fbc-9a3b-ca736e5de97f | -5.47263 | -45.11717 | 2026-07-30 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b85c941c-dc02-3042-81e5-3a2b17cfdf19 | -5.82588 | -44.14325 | 2026-07-30 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 595ea38f-81f7-3477-91c4-f33c6432c135 | -11.93057 | -43.43625 | 2026-07-30 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 369ad505-c182-3a72-8245-e6326f5779c0 | -5.82119 | -44.13905 | 2026-07-30 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c893a716-1010-3c67-b367-491ca323840f | -6.33903 | -44.60802 | 2026-07-30 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e04a625-fb8a-387d-a14b-064e24c994fa | -7.34088 | -45.85318 | 2026-07-30 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3315abf-2103-3255-829e-a77a222d40a5 | -11.66402 | -43.76103 | 2026-07-30 03:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b493117-6551-32ac-84b3-450ddd97aa73 | -10.19535 | -42.21286 | 2026-07-30 03:53:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c3d3d9d0-5b94-31ed-ad2c-b143be3d9fe4 | -5.82062 | -44.14233 | 2026-07-30 03:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 654a0660-dee5-3839-98c0-9e751757636f | -10.19962 | -42.21366 | 2026-07-30 03:53:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 54e59b64-7e7c-36dd-a768-c052f40fe151 | -10.63197 | -47.4851 | 2026-07-30 03:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)
