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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23045054-df0a-3a08-9326-23296a9396f0 | -11.78419 | -45.57086 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81e0b021-04e2-3d00-8e6e-0c885d1aa4f4 | -11.39975 | -44.95914 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e625ef61-4c5d-369d-903b-a8ba75f165f9 | -10.28565 | -45.23069 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e64fc6-28a3-3c78-98ed-121b36fa34f8 | -11.69855 | -44.39414 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e4064a-e7b5-33d5-9c37-c7538ceeb939 | -10.39108 | -46.17058 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 68c910ef-26d9-3f17-964f-9eb7f0d53200 | -11.64558 | -44.43096 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 451858bc-7143-3c9e-8ba9-eaa14633c8e3 | -8.2819 | -44.94556 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e633f7f-792d-3cd4-b85e-40836569b853 | -8.69006 | -44.03906 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78dd9ed9-0023-38d4-90a9-e666b6af53c7 | -11.82972 | -46.62382 | 2025-09-25 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce652e94-1d88-31d3-93e8-f0911049c9ad | -8.28915 | -44.94696 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0597f7a-34d2-33ec-b667-38559db3afa8 | -8.13307 | -44.13894 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e34181-9c2e-34c0-9f35-1d2575611cc1 | -8.78265 | -43.03428 | 2025-09-25 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a1ace5e4-d14d-34e7-a62c-8be80ac1dfcf | -11.53429 | -43.65529 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c71093-5dd3-3540-a591-180f528ef9d0 | -11.78964 | -45.58524 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 167e2cde-f1ff-3680-bed6-07089e408efa | -10.10728 | -45.32669 | 2025-09-25 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c331e6ee-4b75-3f95-afe0-ce876277e6e3 | -10.84496 | -44.80796 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6c7f827-a0d3-35c7-8e5f-a1dced0b28e9 | -11.67281 | -44.4089 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f433b40a-22d6-36e7-b1a2-17da1da4c816 | -12.53914 | -45.80569 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab36116a-8ffb-3866-93a6-78a8f8f35b03 | -11.64428 | -45.35343 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e44017ad-7298-3464-86f7-57231ff50aff | -8.19758 | -43.59592 | 2025-09-25 04:34:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 338d4ac8-c635-3bad-a359-0840abc269e5 | -11.63927 | -45.34991 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e510e2fd-115d-3513-8e59-c6babb1aa7ab | -10.79539 | -45.37689 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb25eed-2636-3968-8c42-6ae5b9e91226 | -11.48063 | -43.52277 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40047a8d-7214-3c0c-8915-532411f60691 | -10.8454 | -44.80635 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33903481-3940-353b-b8b2-079a934ff9c5 | -11.62525 | -44.31797 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50906c0d-f94e-33eb-bbae-ecac3e73484f | -10.11646 | -45.3151 | 2025-09-25 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70d2115c-6806-324c-b27a-239b0db0fea7 | -8.49329 | -45.00867 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a896ea1-9885-38ad-b49f-3aa95659a771 | -11.63991 | -45.34534 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a1baf2a-ac99-3396-9cc5-88f242402791 | -10.59353 | -44.07827 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e199f5d9-5317-395e-8459-b07c4cd0c03c | -11.64298 | -45.35054 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48abe880-0164-3dda-9034-3bcea9e711bb | -11.40907 | -44.97549 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 091265a5-70ea-3fc9-ae51-f26e66f7e301 | -12.54409 | -45.79743 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30e0e467-9eaa-3d8f-815c-3c24013fb86c | -11.67745 | -44.4015 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae464f0e-e91f-3ead-aada-793d59336532 | -10.39926 | -46.18811 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ac8664a-a666-34b2-95e8-09084a0db80a | -8.47867 | -45.00675 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58f113bf-69ee-36b7-bcd5-9d8e541814af | -12.409 | -44.75986 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8855d0c-6be7-3252-bbee-fdb61fb9e9c8 | -9.76287 | -45.91682 | 2025-09-25 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5fc0fd3-eb24-31ad-afbb-915aeafe401d | -11.43352 | -44.93949 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fb28e15-4c92-3ede-bd3d-22ce3ee5b3cb | -8.19004 | -46.38121 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e28ed9a-8e79-3798-b264-8321832b0473 | -8.49267 | -45.0129 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9f21e74-0d38-39eb-820e-b8ec53e9653f | -13.83961 | -45.61664 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21dd03c7-831a-3c18-bd1a-e7487f5f5419 | -11.40424 | -44.95472 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb30bb20-f373-3515-8892-6e1c396c8e79 | -11.69208 | -44.38272 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 186f0c51-5b75-3957-b56d-b760fae2fb81 | -11.78305 | -44.87574 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee1d3dda-ad72-3555-9134-dade650777ac | -7.95692 | -48.11456 | 2025-09-25 04:34:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85caa86a-4f15-3149-9273-bffa0d394104 | -11.49515 | -43.54079 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8d07f8d-b747-3db3-8cc1-500991ec8b00 | -11.78585 | -44.91091 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee5dbc80-257a-3392-be4c-ce952f3ec572 | -11.41803 | -44.96678 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448bcbaf-5058-38d1-8f79-464a4ad0a4cb | -12.31314 | -44.21079 | 2025-09-25 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fac6fa93-3330-322e-bc69-f6c25aba3919 | -11.01813 | -44.33371 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e657691c-8c0a-3740-9b83-61dda31bed14 | -11.04008 | -45.8862 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7a19226-99b2-3230-8616-577d80f6989c | -11.41286 | -44.97603 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2cd7759-b17e-3a51-81b4-8d55689e7fd0 | -14.3428 | -44.49632 | 2025-09-25 04:34:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95985c65-0b55-368a-b1ee-3b20ae56e49c | -11.43036 | -44.93446 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1a39eb57-c450-3d14-9f73-2e2a447c0e29 | -10.83825 | -44.8289 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d05b71fb-a4f8-340b-bf01-9f25b473f27d | -10.5928 | -44.08344 | 2025-09-25 04:34:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50e81e40-c95f-3b3a-a970-49d87ea84171 | -15.77469 | -59.49529 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7658ed2f-cc11-3a0f-bacd-457e1a8662cd | -20.08391 | -54.62135 | 2025-09-25 04:36:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4b3478d-68ce-3851-b7e6-809621c3d577 | -16.84634 | -50.51508 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19349287-08b7-3774-8e98-3b67c12b863a | -21.00286 | -50.02839 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4cbe437c-3fe9-369a-ba8c-d815133d0112 | -20.99895 | -50.00836 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 57ee50df-7a5d-3e03-b7f3-e8d6063c5a7d | -17.93607 | -55.86864 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 00de529a-52f0-38b3-adca-058462ab0cfa | -15.91871 | -59.34945 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3484f0fb-d5b3-3874-b0f4-393bed6e4917 | -15.76936 | -59.49301 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 479cb3f5-4e35-30f0-bf45-24e0aa27a0a5 | -16.8469 | -50.5115 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ad842ec-d1fe-3425-91e7-91582ccb7fb8 | -17.93546 | -55.84962 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c0664189-3511-3257-97a7-e4b64639d900 | -20.99783 | -50.01591 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 0b7e573c-d3eb-348a-8615-3abe5ca58a37 | -21.01404 | -50.02253 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4eb8fb14-b6da-352b-8b75-743a743e5ea7 | -16.85463 | -50.50545 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae5b565-b4d1-3648-980a-4d7e15e26f76 | -15.88008 | -59.34909 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 810edb93-a344-364f-9885-9529c9097562 | -20.82258 | -45.95059 | 2025-09-25 04:36:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b300156-9ecd-32b9-a0fe-afa120521b11 | -20.97602 | -50.02383 | 2025-09-25 04:36:00 | NOAA-21 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8d8d4e3a-9673-32b7-aea4-e697ab004f66 | -16.8535 | -50.51261 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4f1036e8-02b8-3a62-b3e3-c6c73b6291ff | -15.96722 | -59.51168 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3b41583c-fcd3-3692-94e0-d294e8149f40 | -15.76042 | -59.48466 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4d43a9a1-d98c-3c90-bcb2-be1fa501f1c1 | -15.76202 | -59.47664 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a92d4a4f-2996-31fb-9d54-f36cac643537 | -20.9872 | -50.01798 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9a46262c-3f8a-33da-843a-0bb4786803ff | -16.8502 | -50.51205 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0358a445-95a3-3a54-9cf1-cb2d37640117 | -18.1834 | -53.33419 | 2025-09-25 04:36:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb451344-b5e9-3390-812d-2089c3415aba | -15.77394 | -59.49729 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2c85eac4-4188-3be5-9943-265edefef14d | -16.84908 | -50.51921 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1d278ee-956a-3530-b2a8-2db646761bdd | -20.97825 | -50.03198 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ac0a0f1-2323-3e27-b321-c7028525803f | -15.90882 | -59.39769 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c01dd535-79e7-3e30-9cff-10a121626549 | -21.00956 | -50.02954 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b207cbef-d8ac-328b-8945-add33335acf2 | -20.99503 | -50.01157 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 179ef5a4-7fde-3f3a-95c4-06636b564097 | -15.79781 | -59.48747 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7e23a797-bebe-38c8-b918-dcd103587b51 | -20.66732 | -48.82189 | 2025-09-25 04:36:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| fa3ab1af-129d-3458-8daf-460bd841fe44 | -15.87488 | -59.34805 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 322b1c33-083f-3bef-8025-e9419a243573 | -17.15 | -49.47178 | 2025-09-25 04:36:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2db85fc-ff6e-3842-8a37-2ad6f0a88af0 | -15.76207 | -59.50381 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 48879362-718a-30bf-a4c1-2143f46e58cc | -15.8293 | -59.60238 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78b02aee-5d8d-382c-9bf4-5a26021fdbd8 | -21.01012 | -50.02575 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6dc3e4c7-11f2-34b4-97d5-a50c15361ebf | -17.22783 | -52.40479 | 2025-09-25 04:36:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3eb1ccd-8f00-3dac-bf1a-2e7e0328b45b | -17.93343 | -55.86055 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 3272669e-b91b-3f41-9de0-3cb6f69b131b | -15.90845 | -59.39674 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 545fe503-9285-3c13-b9f0-50ca55cd97b3 | -16.85406 | -50.50903 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 29b575f6-9eb5-350f-8b11-3adf7dbe4dbe | -21.00174 | -50.0127 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ded6bad0-396b-3d10-b646-b433a28e3e2a | -21.00621 | -50.02896 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7613843d-00ae-3910-9706-8fa78f95793e | -15.89031 | -59.4063 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5299551b-ead3-399f-bbdc-0942e7806e52 | -15.76873 | -59.4978 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README24.md)
