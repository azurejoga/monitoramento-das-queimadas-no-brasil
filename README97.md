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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5830c6f0-2c5e-3919-870d-dfaf6e34dae5 | -20.4526 | -46.45469 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1884b7d5-8182-3e9e-8e1a-7e4d4f4f25f5 | -17.28726 | -46.11246 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fbd2c67-b6fa-3bbd-82b7-0bc0d4bfda4f | -17.30678 | -48.72992 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 382f6ccb-9a3d-3da1-9c69-9906442350d0 | -19.98924 | -46.89892 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87d80b6f-21d9-3588-ab1e-37c12de079a7 | -18.85812 | -46.83791 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e2b7333b-11c1-34ea-bd6c-9b41301e9072 | -17.43897 | -49.22234 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9667ac5-12e6-3b7e-a181-566ce8c4813b | -20.09963 | -46.91071 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b57ba87b-3f79-339c-98a1-d3415e9c92b7 | -21.0682 | -46.1394 | 2025-09-13 05:01:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6ab5c64-f291-3333-9e4b-0e11b48e7046 | -17.28222 | -47.25134 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c55a4e04-d234-3b63-be7e-f7f510891d31 | -16.87063 | -49.33765 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0ec886b-831d-301e-80e7-370c0f72d4fb | -17.95166 | -45.26746 | 2025-09-13 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd9c23d9-da90-34b9-9f33-8518819bb5c4 | -18.12996 | -51.71668 | 2025-09-13 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c94a049-75e1-3af0-a7ac-32005528d121 | -18.13727 | -48.4536 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 476e88fd-9456-3f25-9922-dc7caaaaa031 | -21.00565 | -44.85638 | 2025-09-13 05:01:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b52b77a5-60a2-3ab6-9c44-9f7045fb3a86 | -18.60471 | -47.1923 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1e603a0-fa4a-3e76-aa3e-400a54d0f305 | -17.28834 | -46.10211 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18100d6e-7fb1-33e8-9a0e-2d1abb134083 | -20.08223 | -46.91204 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 675ab0a1-0e42-377f-826c-db83b9220941 | -16.60847 | -49.46833 | 2025-09-13 05:01:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 44c1a27f-f224-322c-a336-d42c30436da0 | -17.99873 | -46.94136 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| efb24c17-08d2-3898-9b9b-5b5fc6e5789e | -17.1315 | -48.48411 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3b51d75-50a7-31d7-a09a-6d503b6f0fda | -16.53147 | -51.75139 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eaa6960a-bae7-3a2a-843c-08554f9d8c0a | -17.4459 | -49.24527 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df93f86b-c90d-3083-aa08-d00f5ddb6656 | -16.49513 | -51.9934 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6065403f-ee72-3e51-b649-30f97b078658 | -16.34147 | -51.52904 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a04d7bb2-22db-3204-a5a3-30b3c2becf35 | -16.52649 | -51.78816 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 790400a3-8f7a-36df-8ed2-18f4d0724887 | -17.29103 | -47.2441 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db76bed1-e827-3526-b5ec-a3b308e90300 | -16.79169 | -51.35894 | 2025-09-13 05:01:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e8c3164-5209-37b1-ae53-00af0011e7bb | -17.43365 | -49.22669 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2bac63e-ccc2-339b-83c7-eadb3e395ced | -17.41044 | -48.22075 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 180f3c23-c501-3d2d-abd7-9d9b03e60a1f | -19.65351 | -45.86998 | 2025-09-13 05:01:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf47f61-966e-3446-bbb9-f763bb9e943a | -21.6128 | -46.80851 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 98d381cb-fbe6-3b89-822c-059ecd47360c | -18.2274 | -52.19194 | 2025-09-13 05:01:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 631bdd5d-bb16-3ef2-978f-7dbdc36f842a | -20.45481 | -46.44273 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31802220-5983-3592-8232-917f2d82d20c | -16.341 | -51.53257 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4edc32ad-89d0-3415-9bf1-d6dd03b66241 | -17.42231 | -49.24165 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7cf98a3-e590-3351-b975-00c8fb65a09e | -23.89125 | -51.3591 | 2025-09-13 05:01:00 | NOAA-21 | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ffe0fe4-16bb-36c7-a621-c24ded3a0d83 | -19.16438 | -46.66169 | 2025-09-13 05:01:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb14c37e-d45e-35ed-8e95-7635fb4f7dc8 | -16.35794 | -51.50906 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef6144c-8c12-3612-9ca7-3b8478c87795 | -20.09431 | -46.906 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e73cef2a-bc60-325d-af92-ea99edd47bf9 | -20.79539 | -56.95439 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 986d8a1e-e314-3f0d-a1a0-6adf9d647a8f | -20.64467 | -48.6907 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30d852b-4886-3049-81ea-01ca4f580ebf | -19.34553 | -56.70326 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 94e9a286-dd37-38a1-b602-1f204965657e | -17.30063 | -48.74022 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e88210d-2bb0-3577-863b-d30c8d4c0255 | -17.23808 | -50.22911 | 2025-09-13 05:01:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6eb93b9d-d9d6-385b-b3f0-b80c3ce05cec | -17.28838 | -47.24508 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8630f145-b131-379a-91e2-6115521fec68 | -18.89281 | -47.0553 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db76a79e-c523-3b4c-b408-320c56d8c537 | -17.54986 | -44.55199 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e64b696d-f1aa-3979-8e94-adb2cabd7427 | -18.82291 | -49.58034 | 2025-09-13 05:01:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7cdd8831-4648-3e0d-8192-34503efa69dd | -17.54316 | -50.51159 | 2025-09-13 05:01:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff0c1bf8-823f-30a4-8a79-f734685b3f0e | -17.40541 | -48.21982 | 2025-09-13 05:01:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07c70809-cbd0-35d7-8157-70467fc0becb | -22.26016 | -49.56487 | 2025-09-13 05:01:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d287e86-bed7-3182-a7af-8daea59d668c | -16.51407 | -55.18363 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0028279e-e54c-3806-be8f-4656609d985b | -18.97521 | -48.59761 | 2025-09-13 05:01:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 038181a6-dc5b-3348-9f3e-0eef529dd5eb | -21.00539 | -44.85981 | 2025-09-13 05:01:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 83f87a80-fdbe-3a68-bc6e-1f8e7efdaee7 | -17.0979 | -48.85347 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f31903c-f2f6-3b76-8650-910b973f2883 | -22.16296 | -47.37257 | 2025-09-13 05:01:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b9c5130f-685b-327d-86bd-5188181e16f0 | -17.28264 | -46.10044 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81d93054-213b-3bf4-a83d-74e9a8e7896e | -20.64918 | -48.69744 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88fd5ea9-4a0e-3358-bcbc-b50f5c6bf48d | -17.36188 | -42.70553 | 2025-09-13 05:01:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 37ad2d54-0399-37ec-ada8-52645352a36e | -17.28493 | -47.25034 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a8dc21e-884e-32d9-af0f-ef1925548544 | -17.41572 | -49.25718 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22f49af4-95f6-3402-9b09-49d3a61a284d | -16.49657 | -55.13864 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cc09e288-fd68-3f2e-9105-9192e16dae7d | -17.86618 | -51.70729 | 2025-09-13 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 37f2ee0f-6082-3b92-8536-3cff54440445 | -21.6232 | -46.82417 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c41ba5c7-c343-35ea-a987-5fa9749c6558 | -16.52355 | -51.75027 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8484e5b2-2a90-3dbc-88c5-a7c7f1f178ba | -21.07175 | -48.9356 | 2025-09-13 05:01:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a9caeac6-c056-3205-89c7-054de94166b6 | -20.44671 | -46.45412 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18b44142-abdb-3cdf-843a-35c71d97aa65 | -17.38671 | -52.92614 | 2025-09-13 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a5258ff-e601-3c4c-8afa-90882c5e746c | -23.34582 | -47.19677 | 2025-09-13 05:01:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b945cb9d-7b0c-3b9b-a0da-79d81619358b | -21.57955 | -48.42565 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71af3729-a869-33b6-b24e-33da02c8897d | -22.18523 | -49.61407 | 2025-09-13 05:01:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d52f0f29-0c5f-3939-a8cd-ee303e6b9bfb | -16.50327 | -55.11654 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 39d92226-c51b-3d2f-bdb7-d3c66a4381c3 | -17.30125 | -48.73484 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87c4de68-44c7-39c3-ad14-e4740aabc6b3 | -17.2876 | -47.25205 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6552d908-3d6b-310a-81d2-63125bdf842b | -18.18097 | -45.2061 | 2025-09-13 05:01:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 285d5975-761b-35c1-a2d8-70d0b7d1861d | -17.3625 | -42.69828 | 2025-09-13 05:01:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e5a6acd1-2116-3f04-9ccf-97b3a29e662b | -17.29513 | -48.74492 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| faa36cc5-670a-3cc1-aa4c-4e07d39fb929 | -19.33561 | -45.11614 | 2025-09-13 05:01:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e3cd57c-d9e1-3509-83dc-6b46beb1fb12 | -16.55278 | -55.13222 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 144df9d0-b285-3ac8-bda7-5a9f57055099 | -22.33451 | -47.40721 | 2025-09-13 05:01:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e5fdca2a-52e1-354d-a10b-9104d140b888 | -19.99217 | -46.9028 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e321374-363f-36ed-b47c-9fe3b20169ce | -18.85336 | -46.82821 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c28eb58-f500-39fb-ab16-0826aea04d9c | -20.44798 | -46.45195 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 463e807e-7b91-3b04-b03f-dbc7250a5f2f | -17.41036 | -49.26205 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bb15429-a1f1-3502-9480-9a9f8dfda77b | -17.34044 | -46.66735 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fc6a6b8-b4ca-3a74-a034-0a75d095aaf5 | -16.36152 | -51.51302 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb3c416-5d8f-3d09-a6fe-d041e9f6874d | -16.60842 | -49.46467 | 2025-09-13 05:01:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a17e2fd-189f-3083-9079-857130e90f47 | -16.53615 | -51.74671 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5400b979-d01a-30c7-824c-2178727a9bbb | -20.4489 | -46.44226 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bff7d09-28b3-3672-b731-81774984fa5a | -16.36728 | -51.53159 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4676ec8-623a-3e9b-80c2-27ce70ac215b | -18.9887 | -48.42139 | 2025-09-13 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a4e51eb-e34a-3b28-bf62-1d9f11c37e86 | -20.4484 | -46.44752 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86019796-d323-3cb5-b453-3e03be7338a0 | -20.44214 | -46.45088 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597fa22f-015b-313f-8a20-af3994a9ef8d | -20.0852 | -46.94232 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53a2f8f5-4182-3424-999f-4ee93924a2af | -16.34452 | -51.53673 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4da7a7fb-b797-39a8-9a01-69720b5d189c | -16.4865 | -51.99453 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a604b63-1f0d-3ad4-bccd-fa06c6f57a7c | -20.37132 | -50.12386 | 2025-09-13 05:01:00 | NOAA-21 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 871db292-7297-32ba-ab67-62eb461711d9 | -17.41695 | -49.24647 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dadbf50d-7c93-3435-978c-38733d09e12b | -18.60505 | -47.18904 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be48cee1-4fd5-3f36-b2d9-c80ba18aba27 | -17.14359 | -48.50954 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README98.md)
