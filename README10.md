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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88566511-c639-3c49-bd76-d03ac290e6f5 | -17.93471 | -47.02291 | 2026-06-23 04:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db61dc85-36a0-38fd-825e-1c11ee26b1bb | -15.43859 | -41.37206 | 2026-06-23 04:08:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 122dd7cc-8095-352a-9233-a70f7c73878a | -19.96452 | -41.62988 | 2026-06-23 04:08:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 963ff58e-6adc-3040-b059-ccb4c9cb31b7 | -16.02762 | -43.41505 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35aad8e1-8ad9-3cdc-a1d9-99bcc62c6093 | -20.3463 | -46.62428 | 2026-06-23 04:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79852ac7-8fab-36a2-a652-91498328594c | -16.19753 | -45.59238 | 2026-06-23 04:08:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca67f9db-dee2-373c-9953-d5d8076fddd1 | -15.80712 | -42.61043 | 2026-06-23 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e72fec96-d250-31c9-b336-0a3cd52962ee | -14.69754 | -48.28237 | 2026-06-23 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 963672af-d3c7-3779-b1ae-25782d0821de | -13.20473 | -48.32167 | 2026-06-23 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 658ffeee-7630-325e-92df-ace84bae93d3 | -15.44191 | -41.3726 | 2026-06-23 04:08:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 48e0f2f7-a455-32f9-aaf3-bbf53771b93e | -16.02702 | -43.41872 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52f3d940-4914-37ba-915c-9beb25813d8c | -19.93655 | -40.79495 | 2026-06-23 04:08:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27cac337-50d5-39c6-95db-3ec2045e8092 | -20.48726 | -46.38068 | 2026-06-23 04:08:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0db0f0a6-4d85-3e1e-9cd9-902fd7f77f02 | -12.91711 | -49.4784 | 2026-06-23 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b62f74e6-c172-3445-a3d2-4fc414fd321d | -16.20114 | -45.59308 | 2026-06-23 04:08:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e9a8135-7ea3-3134-a5be-44a46691db18 | -17.68482 | -47.23953 | 2026-06-23 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eec3b939-3f98-3463-83e3-5bcc0bc04f3b | -20.31775 | -42.00587 | 2026-06-23 04:08:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 530e0dac-24a0-3c0b-9bea-318aa5dba649 | -14.02973 | -43.86684 | 2026-06-23 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8334be2-3ed5-3e23-a569-99409592daed | -14.26863 | -43.16732 | 2026-06-23 04:08:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ef828f80-91e8-3090-880c-bf55a993dd57 | -19.19487 | -39.78936 | 2026-06-23 04:08:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd7dd747-a6bd-3c09-8a2b-c9b5b6fb59f4 | -16.03298 | -43.4156 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| faeee507-2893-3c89-bc4b-eb837d5f2509 | -17.61206 | -46.69685 | 2026-06-23 04:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3652cb89-09b4-3445-a8ca-4695e86ff130 | -14.02908 | -43.87069 | 2026-06-23 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6da91ff-849f-33e7-a614-a68c4175d4e4 | -15.38665 | -40.82468 | 2026-06-23 04:08:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f41ae7f4-3ea5-30c9-8242-823746cc15f0 | -17.83843 | -42.61264 | 2026-06-23 04:08:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a57306d1-b408-3758-b1b0-4bd8b24ae180 | -15.72641 | -41.35249 | 2026-06-23 04:08:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6592b99-20bd-304e-aaa7-fd6a93002939 | -12.87907 | -49.83772 | 2026-06-23 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1bb6c73-f970-364d-a968-df1db13f327b | -12.91227 | -49.47747 | 2026-06-23 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c686b9e5-e42b-3a69-8d75-7484fbceb572 | -20.34278 | -46.62313 | 2026-06-23 04:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b5222ab-c77e-3404-9766-c15fa1c6419a | -19.94289 | -40.77557 | 2026-06-23 04:08:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd0df4ef-5042-3bd8-866b-0b7425761575 | -17.13789 | -46.82347 | 2026-06-23 04:08:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 019df04c-7c52-3d9d-9fdd-ba4e691f013a | -13.98024 | -46.18205 | 2026-06-23 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8fa778c-9d30-35d5-a2b9-3f57a6e098fa | -20.56986 | -44.93918 | 2026-06-23 04:08:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82c01a7e-d1b4-3db9-b774-c1d88ac1b714 | -17.68578 | -47.23436 | 2026-06-23 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3aaf5a87-1754-3a65-aedb-c580fbc0b2b0 | -17.68387 | -47.24472 | 2026-06-23 04:08:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f7aee4-b056-3dbd-8dca-083875862084 | -14.42706 | -42.06089 | 2026-06-23 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 6d86aa11-694e-3002-af27-31f434bd2d15 | -20.35144 | -46.61623 | 2026-06-23 04:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12af0392-8e66-3876-9f92-6892c13aa29d | -15.87442 | -41.95062 | 2026-06-23 04:08:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d5daef8-dcc4-3a30-ba53-cbf52706708f | -14.03252 | -43.87128 | 2026-06-23 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d20c8b5-6ca9-3047-bb8b-070f263a5a42 | -17.9318 | -47.01732 | 2026-06-23 04:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ccac429-17ef-3439-93ad-440aefd9efdc | -13.20303 | -48.31907 | 2026-06-23 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c3f17f8-3131-3cdf-b9c8-4372d65e353d | -20.34712 | -46.61959 | 2026-06-23 04:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 546fa9c6-932e-309a-bf80-3060fa13c8b0 | -19.51855 | -40.43603 | 2026-06-23 04:08:00 | NOAA-20 | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1249fc44-7300-36ad-bdea-3f3773e729f4 | -16.02964 | -43.41502 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 259aba9c-9e45-36c7-a3bb-40aaa0f3e365 | -18.69738 | -42.37428 | 2026-06-23 04:08:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea1556f4-ed06-3406-b3d8-c2f6a92b21b2 | -14.43094 | -42.0579 | 2026-06-23 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| f17f5b6d-8833-3378-a20c-f7a6e3b87348 | -19.88807 | -44.81219 | 2026-06-23 04:08:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6f11a20-a667-33a3-9042-c818a65dfd8f | -19.46279 | -39.84032 | 2026-06-23 04:08:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24b10799-91db-3334-b840-a71e88b089ff | -14.694 | -48.27724 | 2026-06-23 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3001b253-a973-30d0-ad6f-31681b43aa55 | -16.49859 | -43.50332 | 2026-06-23 04:08:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c601d01b-e390-3c3d-9554-0418aa2f4c30 | -20.32968 | -46.63399 | 2026-06-23 04:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddd8b2cc-398a-317d-b03d-73d48397fc46 | -13.5176 | -52.17086 | 2026-06-23 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8cc84b8-ae21-380d-aa0b-455cd38625db | -16.02903 | -43.41869 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99ab6551-8cbd-33a0-9b71-fabbad0556c2 | -17.93089 | -47.02224 | 2026-06-23 04:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 834f633b-f6c9-3307-a89f-3c9bcd96203a | -16.03238 | -43.41928 | 2026-06-23 04:08:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d0335b0-a167-3061-aab0-9362471050e6 | -14.41127 | -44.59316 | 2026-06-23 04:08:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70ee957b-deb3-3de1-86d0-91cfef372ce1 | -12.8552 | -44.3389 | 2026-06-23 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 35e294cc-5dc6-38c3-85e4-d446623993fa | -12.8746 | -44.3357 | 2026-06-23 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 93c271df-8976-37d5-bed0-924d1c6dc7c7 | -12.8741 | -44.3593 | 2026-06-23 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9372da0a-b37a-3077-af8e-c95f0d914637 | -12.8548 | -44.3625 | 2026-06-23 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 6a39c4b1-8b95-314f-9379-6111d270d036 | -21.6687 | -45.54664 | 2026-06-23 04:10:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 83599f07-50f7-3f4a-ba67-632c3af65bb6 | -21.0363 | -46.7868 | 2026-06-23 04:10:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6719a8b2-f4ab-3ad3-8549-922fe1f3bf1e | -22.70189 | -43.36246 | 2026-06-23 04:10:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad47f3fd-5c14-3708-b7a0-d3baa5ad3f31 | -22.02704 | -43.11914 | 2026-06-23 04:10:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3c0f14f5-636b-3b24-abdb-134dab6a81d2 | -12.8746 | -44.3357 | 2026-06-23 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7247fe0a-00cb-3d95-83a1-ae93832bc307 | -12.8548 | -44.3625 | 2026-06-23 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 6db2ba14-ab7f-3b21-8665-bd4b8ab61bfd | -12.8741 | -44.3593 | 2026-06-23 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 46594cf0-bc71-362a-a611-322363920e69 | -12.8552 | -44.3389 | 2026-06-23 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e5a03992-3c8d-3ba3-9955-09ae1c073443 | -12.8741 | -44.3593 | 2026-06-23 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d59ab52b-a46a-35d3-86ce-230c55831a2e | -12.8746 | -44.3357 | 2026-06-23 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 73c4c54e-9b89-35ef-9840-cebb7bd91054 | -12.8548 | -44.3625 | 2026-06-23 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| b3c60a81-6125-375a-a7cd-0ad25911558d | -12.8552 | -44.3389 | 2026-06-23 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9a59eee4-3004-33b2-9190-f3039ac5bdc0 | -12.8741 | -44.3593 | 2026-06-23 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 3a75215f-b9f8-3495-adec-4eacaeaf0d70 | -12.8552 | -44.3389 | 2026-06-23 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 02e344d3-2f96-3dd6-a79b-5eaa18cad889 | -12.8746 | -44.3357 | 2026-06-23 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e8a5143c-47d7-3a3c-a153-a4bfa6429b08 | -12.8548 | -44.3625 | 2026-06-23 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| e0bd0e03-7476-3dd5-933c-a458d0d9de99 | -3.5177 | -48.03197 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f65d1ab-d248-34a0-b45d-4b5cfa26c6a6 | -2.57188 | -47.21426 | 2026-06-23 04:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743284a6-a056-3f74-a06e-a665848e6089 | -4.05593 | -43.24638 | 2026-06-23 04:49:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0593a241-2187-379a-ba2a-4158df77ba13 | -3.50891 | -48.03967 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4db4f2aa-77cc-31c0-8346-4493f2564430 | -3.5133 | -48.03586 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d44263f7-ccc7-37fd-9b21-877d768c7001 | -2.48318 | -47.08381 | 2026-06-23 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b97d21f-66e6-303b-bd58-7bf9102650c1 | -3.50958 | -48.03527 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9e37994-1726-381f-929d-3be3ad13aaab | -2.64587 | -47.97754 | 2026-06-23 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab692bf1-f9a6-3b43-b9e2-7c61dea8799a | -3.8667 | -42.96281 | 2026-06-23 04:49:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2094ed0-93ed-3060-b740-47421f0c5fb0 | -3.51702 | -48.03642 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5740c21-4af5-3f08-a00b-dc22c1b5e265 | -3.51264 | -48.04023 | 2026-06-23 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc81fa27-d475-3d7c-9c3b-f67917c4598c | -3.67235 | -48.99313 | 2026-06-23 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5efd426-270e-3bcf-9ff6-10ede979d318 | -3.67296 | -48.98913 | 2026-06-23 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60aa786a-3b64-37fe-b442-c3491e4ef293 | -3.87196 | -42.96362 | 2026-06-23 04:49:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9a362d9-d878-3b73-b555-3b0d1c790d54 | -3.86622 | -42.96606 | 2026-06-23 04:49:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25f82959-6acb-38c3-996f-3c7a88438a14 | -0.64642 | -50.73696 | 2026-06-23 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e411fbc-7fc5-34a7-87f6-7dab8d78f91e | -3.87148 | -42.96688 | 2026-06-23 04:49:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0e83171-f1e1-3ae8-97f3-0ce915a7af09 | -12.8741 | -44.3593 | 2026-06-23 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 9bb74bfa-36ae-3193-bf79-838ef92403ac | -12.8746 | -44.3357 | 2026-06-23 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 258d1ca6-1346-3874-b4fa-6c4e9dbbb8a0 | -12.8552 | -44.3389 | 2026-06-23 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 08faab0f-c031-35ea-89df-cdb238635be5 | -12.8548 | -44.3625 | 2026-06-23 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 723d1e04-6f34-3eac-a549-319f13b355e9 | -10.57031 | -46.23277 | 2026-06-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 290fb991-40fa-3003-b71c-f1a266989e1c | -8.12727 | -47.8938 | 2026-06-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fab2c30a-579f-31a9-9ca9-6a4aa1434084 | -10.1335 | -52.10649 | 2026-06-23 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
