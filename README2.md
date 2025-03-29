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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2dbf57-f967-38d2-83f9-a57a706ffbc0 | -11.47207 | -37.92204 | 2025-03-29 04:08:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 52700484-931d-30dd-811d-d88c6250d39d | -9.09226 | -37.3101 | 2025-03-29 04:08:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b57b4f26-b6fc-3e7c-be4a-a0224f1b6a1c | -11.00463 | -40.48174 | 2025-03-29 04:08:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe58d8b5-515f-3fc8-96b7-29bb7c17e491 | -9.07917 | -40.30538 | 2025-03-29 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1a7fbc0-b248-362f-ac83-c9d921cdbf18 | -9.93258 | -37.19788 | 2025-03-29 04:08:00 | NOAA-21 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e78826ac-8d60-3222-946c-279d3caa2ad5 | -13.07748 | -39.22216 | 2025-03-29 04:08:00 | NOAA-21 | SANTO ANTÔNIO DE JESUS | BAHIA | Brasil | 2928703 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ddba61d2-72ff-3031-9d50-813a32f8b99f | -12.32146 | -37.97316 | 2025-03-29 04:08:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 830f92f5-d055-3e4e-ac72-1e71d63c670c | -11.17165 | -39.89808 | 2025-03-29 04:08:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51fbcbb6-1bdb-3ab0-9841-d966a0415d3c | -9.42148 | -37.04896 | 2025-03-29 04:08:00 | NOAA-21 | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b0fd2c9-f9d2-37be-9909-2a3486527f9e | -12.26797 | -39.40359 | 2025-03-29 04:08:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a65dd91-92b1-3d08-9687-ef57628041df | -8.13027 | -43.14259 | 2025-03-29 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5666dee5-dca2-367f-a79e-2473cb84c71c | -8.13696 | -43.14367 | 2025-03-29 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 89cacdf9-bb97-3410-aa20-5d992ca2b61f | -8.12634 | -43.14562 | 2025-03-29 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e5f83910-3806-3527-ad26-6294dbed97ba | -16.72769 | -39.3988 | 2025-03-29 04:10:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc42e824-18bb-3872-a46e-c07dae9d4ff5 | -19.14221 | -51.56682 | 2025-03-29 04:10:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25695472-0de2-392f-801c-b5170763f391 | -18.03464 | -52.89006 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6216a207-c003-3667-b56d-ef574a69d165 | -12.61017 | -52.12217 | 2025-03-29 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da985e35-5a17-3255-aa45-785c8fef3588 | -12.61141 | -52.11566 | 2025-03-29 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5311bde-58bd-310d-a5d5-ec7db337a19a | -18.03549 | -52.88587 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79e03ddf-af06-3902-9776-c3f6c8785b35 | -18.37804 | -47.36326 | 2025-03-29 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc991549-16d5-30b9-80ba-72eb5cfef271 | -18.37877 | -47.35901 | 2025-03-29 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2101d9c1-c7bd-3f6d-85a1-6c2a6f9fc492 | -17.59781 | -43.19839 | 2025-03-29 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 505a25bd-dbd6-3500-98d2-590c13080786 | -12.6154 | -52.12324 | 2025-03-29 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf3e09e3-0ce8-3991-9ad2-f93d2a9e9f6d | -17.502 | -45.17635 | 2025-03-29 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2604c41-2b60-3f07-a9c0-7178c8698eb7 | -20.79496 | -41.12946 | 2025-03-29 04:10:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c914123-dfb8-36bc-9e14-ace060f7f39e | -19.89072 | -48.35369 | 2025-03-29 04:10:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af21fac-91c5-3040-8b0a-8f7f8ee52aa0 | -16.68024 | -43.88419 | 2025-03-29 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4f010ca-bf92-38ec-a43c-f4074be4ed01 | -16.04683 | -41.804 | 2025-03-29 04:10:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27d84882-c780-3ca3-b514-93323858a1f3 | -19.8355 | -40.11386 | 2025-03-29 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 371499e2-0310-3993-8570-d09010e340fe | -18.04187 | -39.92494 | 2025-03-29 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4c67e30f-9abc-3ec0-b98a-cb373f46c32b | -18.03049 | -52.88494 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e37d55c-a024-380d-86c6-7213d05f4606 | -12.61079 | -52.1189 | 2025-03-29 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6138de8-6a9b-3a85-af04-acd708eb3497 | -15.3735 | -39.17535 | 2025-03-29 04:10:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3d4b250-80b8-30b6-92c8-c9af30666709 | -18.03428 | -52.89196 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aefb88a-cf60-329c-be27-3aecaed07050 | -17.75219 | -42.8942 | 2025-03-29 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f29835a-1cba-3976-b546-99779bfe26da | -17.7823 | -42.80769 | 2025-03-29 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d41768c-a0af-3f7b-95e2-a444fde98a6c | -18.02548 | -52.88405 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf53812d-35ae-3431-ab52-b92744164613 | -17.67664 | -42.74142 | 2025-03-29 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fbbee72-f969-31c8-98fe-271ec81018f9 | -15.57078 | -47.85386 | 2025-03-29 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b38e7489-fbb2-3d60-954a-c81d57b5f233 | -17.97418 | -52.83027 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66dda35c-a6e0-3104-937c-f028d0d6c976 | -18.03527 | -52.88702 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf81f13a-09bd-3088-b3f7-993f0914ec32 | -16.34925 | -43.69648 | 2025-03-29 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1e0703-6660-3794-966c-954f9e850c75 | -18.03488 | -52.88892 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 310a9880-f4cd-3398-be27-076d58560848 | -20.41648 | -43.55443 | 2025-03-29 04:10:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f3ade00c-0eac-3a2d-95fa-eb59271dd979 | -18.0309 | -52.88303 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92be7486-4e5e-3a5c-9fba-a83a0d228362 | -13.95959 | -38.95689 | 2025-03-29 04:10:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d8b70256-09bc-365b-b339-b59271b6f2fb | -17.09408 | -43.80278 | 2025-03-29 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58f6002e-9087-3ee3-8d2c-2c4d1a85438e | -12.61602 | -52.11993 | 2025-03-29 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c8a456-231c-33d9-bd50-865f5051bb40 | -17.97359 | -52.83317 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cff0ed8-994b-3e11-bd02-79068ed11bb9 | -19.96951 | -44.2181 | 2025-03-29 04:10:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| acf09e0b-e8e4-35a3-8660-2d80af80224a | -17.67608 | -42.74516 | 2025-03-29 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebba8dc4-e0b0-3e5c-bd5e-908eba4cae46 | -19.8899 | -48.35827 | 2025-03-29 04:10:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1027fcfb-b722-34d8-b552-35d33ba3706a | -18.0259 | -52.88215 | 2025-03-29 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5baf1682-6bc2-336d-8752-6350e4e4b426 | -19.83399 | -40.11248 | 2025-03-29 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a26e439-feef-3519-869a-173bb4624ea0 | -20.58369 | -56.03439 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a29e94f-f673-3434-964a-be3275b4f98a | -23.33932 | -46.7721 | 2025-03-29 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fdfae175-30ab-3728-a058-2bd7cd26f1a1 | -20.58272 | -56.03869 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5d4368a-12b5-3542-8d67-652c8664535b | -23.27899 | -46.60223 | 2025-03-29 04:12:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fafdc257-ea18-30a9-a01d-d0391bc312b7 | -20.44474 | -46.37317 | 2025-03-29 04:12:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09d50e7d-ff58-33a9-8e30-44f94c812c77 | -22.78518 | -43.75675 | 2025-03-29 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21fc107c-6a3e-3fe0-a428-ca7daf8d75d0 | -21.46223 | -57.16229 | 2025-03-29 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10c8609f-9d99-347a-9e04-18e696fce54a | -21.23725 | -56.46747 | 2025-03-29 04:12:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d83a4ba-0ea6-3e66-96b0-ea78fcc59cfc | -20.98894 | -47.36111 | 2025-03-29 04:12:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d197f6e-3a5a-329b-870f-544d10884624 | -19.69913 | -49.86509 | 2025-03-29 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e256c1e8-5339-3529-a15d-b9e5c124c262 | -23.40574 | -46.55593 | 2025-03-29 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7c2086b5-f681-3441-8ba3-4b981862ab37 | -20.57514 | -56.04555 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31a211ff-36f4-3086-8e88-b81c8483db59 | -21.37017 | -48.54891 | 2025-03-29 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 39875a87-243f-334d-b720-4dd62920732e | -21.1969 | -44.93898 | 2025-03-29 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0affba81-4f7e-3816-a7de-04e79f4ae4a4 | -20.13814 | -50.72407 | 2025-03-29 04:12:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93aee10b-44c9-39ca-aa9b-dd04610069da | -22.17597 | -42.12062 | 2025-03-29 04:12:00 | NOAA-21 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7a6cb7f7-1995-3f8c-8d2b-d55553b6aa77 | -22.16227 | -47.37174 | 2025-03-29 04:12:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f728f71b-c33b-3334-b10b-aece50d40382 | -20.57702 | -56.03716 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90f29d2f-8a78-3e50-9976-5ae82d4a5907 | -20.57608 | -56.04134 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 946194aa-5807-31c9-925b-d192daac6fe5 | -22.90432 | -43.75572 | 2025-03-29 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0adc75ba-c7e2-3827-abb8-4986d2a4a4d2 | -22.9015 | -43.75123 | 2025-03-29 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d6c44d36-cf0d-341c-a346-d9308c3e14b6 | -22.53929 | -48.8143 | 2025-03-29 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8297791a-f06a-3c01-b2c7-8fd44a6b6e8a | -25.19113 | -49.32664 | 2025-03-29 04:12:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c376cf25-4441-3f33-a521-f313fc4789fb | -21.48135 | -48.66301 | 2025-03-29 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db5acaed-c0c1-3074-8ee3-ffd03d2af52a | -21.4634 | -57.15734 | 2025-03-29 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d18ffad0-2b1a-3be9-a62c-3348d0c256b8 | -23.63119 | -46.42485 | 2025-03-29 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1340d31b-b21a-3400-a074-86ffbfa197ea | -20.98962 | -47.35712 | 2025-03-29 04:12:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3bbf657-aecd-308f-9171-c084c0cf4834 | -22.67875 | -42.79212 | 2025-03-29 04:12:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6b4fd364-299b-35b1-919a-305330eb2d1a | -21.3693 | -48.55071 | 2025-03-29 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f09128cf-2b13-38f1-9e94-4d90d234ecb4 | -21.13152 | -47.80226 | 2025-03-29 04:12:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb1a0707-19a5-3d59-aabb-907bfd74d7b7 | -22.15885 | -47.37107 | 2025-03-29 04:12:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8db717de-7c4d-3eff-bee1-f6be804164b4 | -20.15727 | -47.33171 | 2025-03-29 04:12:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 564405be-625f-3a33-a0f7-d032ea167d66 | -21.46204 | -57.15924 | 2025-03-29 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4e23750-b67f-39bc-ae9b-7227b6773926 | -22.78003 | -43.04378 | 2025-03-29 04:12:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| efc88043-0488-37d9-8435-7027f13043b4 | -20.73718 | -43.74929 | 2025-03-29 04:12:00 | NOAA-21 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 468fd4e9-f129-3aeb-b9bd-b370223b65ed | -20.58179 | -56.04285 | 2025-03-29 04:12:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51e3a966-8648-3b2a-b6c1-c901550a91ae | -20.1389 | -50.72006 | 2025-03-29 04:12:00 | NOAA-21 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab6d43da-2e1c-3a47-b9eb-9e25256294cf | -21.48581 | -48.65915 | 2025-03-29 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b60fd1eb-d2ad-3f32-91a2-67ea78c65363 | -8.14054 | -43.14381 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9b46c478-a962-32c9-97d3-0c642f230fb4 | -8.13249 | -43.14262 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f11f2fd8-f9bc-3a7b-91d8-a0df592fbde0 | -8.13202 | -43.14309 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ca4faba-748e-383e-b6de-dced888202cf | -8.13652 | -43.14319 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c132bf00-626e-3883-891a-55f536d76921 | -8.13605 | -43.14366 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4250d8cc-4ecc-3bd5-aa4c-b1fadfa0ad82 | -5.79157 | -43.61985 | 2025-03-29 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58d5e8fd-470c-3f86-9bee-d34f03a5030e | -5.99696 | -44.61533 | 2025-03-29 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d7ff946-2225-34aa-ace6-9b8f2815b17a | -5.41641 | -47.56932 | 2025-03-29 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
