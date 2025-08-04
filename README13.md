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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78609687-1738-3488-bb9e-47b528e0802d | -21.87782 | -46.13671 | 2025-08-04 04:12:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 851dd909-1578-3c70-b433-39ce8abaf124 | -21.92134 | -46.07505 | 2025-08-04 04:12:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 859ed249-fd5c-3711-9d4f-771637e3049f | -22.51406 | -46.30679 | 2025-08-04 04:12:00 | NOAA-21 | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7de58c59-55af-34ad-abec-569e9c5bfc95 | -18.9218 | -52.48012 | 2025-08-04 04:12:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d7d01f8-4103-3aea-806e-32836e50a457 | -18.98295 | -44.52763 | 2025-08-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 516f3ce1-b652-308b-84cf-bab2e1b38913 | -19.3321 | -44.15989 | 2025-08-04 04:12:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6224cff0-76db-3281-9e27-bcb900a2d10c | -19.9422 | -43.62671 | 2025-08-04 04:12:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e4dc9bd-46d5-3d0b-a284-022d826793c0 | -18.95313 | -46.27455 | 2025-08-04 04:12:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13b5ab72-e6bf-3758-a6a2-33c654a201ee | -20.72069 | -47.29074 | 2025-08-04 04:12:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 048cc349-6dd1-3c62-b500-82e53271b3fb | -22.69916 | -47.44878 | 2025-08-04 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1055bd22-772f-3340-923a-ea13f7042b55 | -22.78983 | -42.1112 | 2025-08-04 04:12:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87697395-8f9b-3101-a8d1-fc1f4c1cb23f | -18.74343 | -43.92295 | 2025-08-04 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42c20d5f-7c73-3cb5-9ea4-4ccbb29e8182 | -22.56244 | -42.16649 | 2025-08-04 04:12:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9e4c5d3c-043e-3707-b9dc-28f6895871a4 | -19.10062 | -43.60515 | 2025-08-04 04:12:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58160717-f0de-3de4-a332-20a42077b548 | -20.30985 | -42.61521 | 2025-08-04 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO GRAMA | MINAS GERAIS | Brasil | 3160108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71194b63-588d-36e9-a5e5-a9a18d41f2c0 | -21.25709 | -43.98504 | 2025-08-04 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aeed8ac8-f2a1-3f04-92f9-24c0d02ba5a2 | -20.32306 | -42.89098 | 2025-08-04 04:12:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c342857-4dec-3d1f-a334-2a31b0f82447 | -23.21415 | -46.60735 | 2025-08-04 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cdef66bb-3344-3382-aa79-d8109eab7a5e | -20.0286 | -42.43225 | 2025-08-04 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 115f99c4-bc42-39ce-b790-cbe28b0f202c | -20.08432 | -44.01356 | 2025-08-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 993fe5cb-a0dc-3cf7-afba-20c6baaf322a | -21.92255 | -46.06757 | 2025-08-04 04:12:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 05b9d1c8-0d35-3e73-a6eb-0b2af4703f9e | -21.88175 | -46.13361 | 2025-08-04 04:12:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 78e02a9a-d830-3f65-9e42-4e9c81e2514d | -20.72001 | -47.2948 | 2025-08-04 04:12:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f033512-0fa2-3a6a-916e-369753a6f203 | -19.70898 | -49.29944 | 2025-08-04 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6927d378-9c24-3852-996b-777adb94fac3 | -18.92286 | -52.47491 | 2025-08-04 04:12:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95e0f177-0501-3962-b2e6-bd66cf6862bb | -20.09488 | -44.01147 | 2025-08-04 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5301b945-02ea-303b-8254-a3a571c06000 | -18.99725 | -46.91196 | 2025-08-04 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a912fb33-3039-35b6-a611-6a773d3c1b27 | -22.57148 | -42.15422 | 2025-08-04 04:12:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf8beff5-b735-3909-a45e-73b7d125e45a | -22.91916 | -43.70941 | 2025-08-04 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 506c95c0-64e9-31ee-9f6d-ddce2e986124 | -19.62266 | -43.17954 | 2025-08-04 04:12:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a1ae4414-9e5f-3d07-bf25-25dd5ca71802 | -21.92587 | -46.06819 | 2025-08-04 04:12:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d059ca37-c596-3700-94f2-281a05b9472e | -21.24192 | -46.13396 | 2025-08-04 04:12:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d99ee82-975e-3aa6-98bd-c48ce6d9626f | -19.99407 | -44.42915 | 2025-08-04 04:12:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e6d9795-a630-3dd6-b301-a23141b6f94e | -23.25514 | -46.03259 | 2025-08-04 04:12:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| db93d27e-319f-3ca6-8a97-60a21bc828ca | -21.93458 | -46.2048 | 2025-08-04 04:12:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7322df50-b992-3254-bea7-6420be71269d | -23.55664 | -47.43562 | 2025-08-04 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eeeb5021-76ba-3735-8860-6ada3aaf7b5a | -22.46565 | -43.84313 | 2025-08-04 04:12:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a2aace3d-1b2d-3160-a551-af874c4c3ebc | -23.90689 | -47.50598 | 2025-08-04 04:12:00 | NOAA-21 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ffe5feb-94de-3b60-b76c-27e9b44f8c86 | -20.3202 | -42.88651 | 2025-08-04 04:12:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 61553c2b-a924-318a-b47e-1ede1996ff81 | -22.98654 | -45.42685 | 2025-08-04 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19caa035-6c0b-3430-8596-ff77271b9058 | -19.62322 | -43.17575 | 2025-08-04 04:12:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73704f5f-f271-39e8-b2b4-c045734405b1 | -22.56605 | -42.16706 | 2025-08-04 04:12:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a2a6233c-9508-3916-ad6a-ed3618b83060 | -22.56004 | -42.15697 | 2025-08-04 04:12:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b6e67a0e-fbfe-3210-b173-306b51720f21 | -18.81015 | -44.67661 | 2025-08-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1235a494-e5f9-3e92-a40d-0672dfdd231b | -22.50285 | -44.5677 | 2025-08-04 04:12:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6aa8e0e7-3782-39cc-9116-6fd83047ff11 | -23.72124 | -47.47876 | 2025-08-04 04:12:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c76b4b78-f7ac-34c2-9a0c-87c9052aabb0 | -21.82268 | -46.56149 | 2025-08-04 04:12:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 519f569c-dc75-342c-bab9-816b4681ca86 | -21.93519 | -46.20103 | 2025-08-04 04:12:00 | NOAA-21 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2643503a-2680-3f47-bba9-4ce9b408b2d8 | -20.32649 | -42.89156 | 2025-08-04 04:12:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0682458d-4b66-38a8-bcdb-5bc190a34bd9 | -21.74371 | -43.44358 | 2025-08-04 04:12:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4533f90d-c6d0-3c4e-8bbc-4c85f1679d79 | -19.53363 | -42.66412 | 2025-08-04 04:12:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0129c22e-1398-3796-acf1-1d3ccf60cbe3 | -21.25766 | -43.98128 | 2025-08-04 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 025ed340-bbe9-336a-b78e-18962f32aa34 | -19.45609 | -42.54688 | 2025-08-04 04:12:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c49b4d88-f418-3644-a154-a6cdcf0a1d26 | -18.63285 | -46.4432 | 2025-08-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 274cb773-d4b2-370a-9d63-90e03b190c08 | -19.33154 | -44.16354 | 2025-08-04 04:12:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afcfd41f-126e-3e57-a7d5-5d98f0c0ad50 | -20.00204 | -45.39761 | 2025-08-04 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb8666e9-5187-34e2-9fa8-21bdf2b77946 | -21.56002 | -47.25649 | 2025-08-04 04:12:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd69b93-8f00-32b5-817c-ff4915c533b2 | -22.56305 | -42.16201 | 2025-08-04 04:12:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 319944d2-2f5b-3a84-9de0-363b27088082 | -18.98021 | -44.52343 | 2025-08-04 04:12:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d61245f5-0507-3ad9-925b-a5cc4114c548 | -19.80656 | -42.39482 | 2025-08-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ca3a822f-49ee-3faa-94e1-751312d7a58f | -21.25374 | -43.98448 | 2025-08-04 04:12:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eae62b72-25fb-3d94-894a-8f0c948a6def | -22.30762 | -47.62275 | 2025-08-04 04:12:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b104941-7394-3d34-bf8d-cbdb224f62c7 | -20.2571 | -41.83606 | 2025-08-04 04:12:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f02c5f5f-2a4b-3c0e-b43e-688810bd0dd9 | -13.0535 | -56.8947 | 2025-08-04 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 726ef735-ed4d-3941-afbd-13623d4455d7 | -7.994 | -43.1534 | 2025-08-04 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 033aa4b7-c0d0-3a49-962f-ff7aed94a33b | -8.3803 | -46.9478 | 2025-08-04 04:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 01d9f45c-3c41-32dd-81bf-8d0f80e4c82f | -8.0129 | -43.1513 | 2025-08-04 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 3f1c8044-bbc3-3049-957b-3d676e2c3df8 | -7.994 | -43.1534 | 2025-08-04 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 73e7c79b-0659-3e76-ad2e-b01d7fa68eea | -8.0129 | -43.1513 | 2025-08-04 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| bf182503-2145-3ece-b183-d0e08ef4b89d | -8.0132 | -43.1278 | 2025-08-04 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 1ca40574-7866-3706-a268-7631a849171e | -13.0535 | -56.8947 | 2025-08-04 04:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6bb77429-ecb9-389f-bf01-8bb7469b3410 | -7.99612 | -43.15848 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 1c7263e4-6358-3b8f-89b8-c7fcf6762e2d | -8.00217 | -43.14508 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| f9ca46b2-1227-35b8-b50c-ec06dcdb6f7c | -6.95506 | -44.50443 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e319c0df-3f6b-34d5-a0f2-70e785c7cefb | -7.1953 | -44.49251 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e85820-842c-36af-abff-9b7bf09dddca | -6.32983 | -45.63407 | 2025-08-04 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ee6cf6c-0a2f-3958-b040-14071a4cad9f | -8.01633 | -43.13276 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 05077360-8c50-3157-ac6a-84ed5ce788ba | -4.12197 | -47.64832 | 2025-08-04 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e238046-453f-3fb8-9da2-67e6f6fba2ad | -6.64583 | -59.11244 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c59f0eb5-6685-3e7d-b845-f2501fa58e92 | -6.65392 | -59.1021 | 2025-08-04 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02a83343-46fb-3f13-b81b-f17b7772b82b | -7.95196 | -43.90496 | 2025-08-04 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e9701b9-8754-3a5a-a212-5e9c6874b702 | -5.8785 | -43.7429 | 2025-08-04 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c6841bf-bfa2-3d8d-9380-10d0831f963a | -8.38229 | -46.94389 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d4be993-5c71-3157-8f13-092a97074f12 | -8.73617 | -46.40997 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29dac441-c551-3c41-a575-d95fbe1391b8 | -6.60752 | -44.04679 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4b4c3ab-5b5e-3753-a26d-52340fc02905 | -8.3684 | -46.91632 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05d1cafd-3ca2-30db-ac9e-4e85e1886632 | -6.5569 | -43.92067 | 2025-08-04 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 137d037e-6245-30df-b805-8a7b54002de2 | -9.39176 | -45.50702 | 2025-08-04 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0f2ea0a-9bf0-3e0f-9c57-c3c3899615cf | -7.56261 | -44.89427 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc8305b7-dc13-34de-973e-e05f93cdfaf6 | -3.91164 | -49.08257 | 2025-08-04 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec7355a-5f4d-3d8f-946c-cbe4dd329d49 | -5.284 | -44.88419 | 2025-08-04 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65d858af-5caf-382a-84fb-82b619b69b00 | -7.1996 | -44.48893 | 2025-08-04 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08f74a37-f735-3460-8065-aa1878baec12 | -8.38731 | -46.93365 | 2025-08-04 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29cc5c66-daca-3c46-960f-b92bce54bbdc | -7.07845 | -44.37471 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4709d33-7152-3547-8344-c16154b973a0 | -8.0274 | -43.14166 | 2025-08-04 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96f7c3a6-5d10-3ff0-a067-2a9314a0df32 | -7.52331 | -45.03224 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 499389a3-7bad-37c6-800c-e15535074613 | -6.8565 | -41.70467 | 2025-08-04 04:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4af7093a-0f75-32b9-ac7c-a270157fe6d9 | -8.74188 | -46.41849 | 2025-08-04 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bf4e922-4f00-327d-b156-fa7f6dcd41c5 | -7.09156 | -44.36301 | 2025-08-04 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf6d2575-6c37-3f31-acd1-668de38a865b | -7.69144 | -45.13057 | 2025-08-04 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
