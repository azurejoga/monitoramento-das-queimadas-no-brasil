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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee10977-cd47-3495-bc35-594c1f9526c1 | -20.04482 | -43.77516 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d52ce847-c5b8-3801-afc1-241faa94f3f7 | -17.13518 | -51.67749 | 2026-08-10 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 919ac337-5638-3a0e-ae0f-55637a0ef9a8 | -20.50217 | -54.68653 | 2026-08-10 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb1a5d79-1555-3ebd-85bc-446ec730655b | -22.80317 | -54.69519 | 2026-08-10 04:55:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 3a9ece79-6ce1-3ee2-a3d7-2dea3d39ef4a | -22.79976 | -54.69461 | 2026-08-10 04:55:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| fbef8c07-ce6e-3504-96bc-b44d5ba555dc | -20.50286 | -43.64346 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 34f3ecaa-3046-33d5-9f44-17333bac6bb8 | -20.04599 | -43.76219 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e5b4a9e7-200d-3a18-bc76-09e98fc8717d | -20.50614 | -43.64033 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90c79459-aa8c-36f7-b70a-5fe27475b952 | -17.13143 | -51.67888 | 2026-08-10 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c7dc99d-1909-3b37-9ce5-4c13b7ba128c | -20.50077 | -43.62793 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6f0833a8-81bd-332f-8376-88edfcc28b23 | -20.37506 | -42.90658 | 2026-08-10 04:55:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 979a1c2a-64b9-38e5-aa94-6a3bbdb1e013 | -20.04519 | -43.77106 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| af883740-6b56-326f-bc48-c74c23710925 | -20.50784 | -43.65906 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 79f5639d-c1e8-31db-80cb-611a10180480 | -20.04363 | -43.76653 | 2026-08-10 04:55:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 32a40bba-2bad-3cc5-bd97-4da2b8f7fc4d | -17.71691 | -54.18778 | 2026-08-10 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 796d3bda-e69f-3ebf-80f7-1bf8fcc20ae8 | -20.50031 | -43.63368 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 87ef87d3-1676-3c67-9887-cb3f93c18d54 | -20.37457 | -42.91272 | 2026-08-10 04:55:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fab64ec8-e0f3-3fd9-9ba0-438d0a5a3f29 | -20.50389 | -43.63186 | 2026-08-10 04:55:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 59f5fcce-8779-3ce3-a5b3-c6819a945d2b | -16.73434 | -54.77237 | 2026-08-10 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f3cebf8-5462-34ee-b311-3fd7f3b9a5c3 | -17.71356 | -54.18725 | 2026-08-10 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5beec24f-5c41-3711-a248-7314a3ec5dad | -22.80658 | -54.69576 | 2026-08-10 04:55:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c1a0822a-a1a3-391b-aa45-04f4f9f95e2e | -16.49749 | -54.65553 | 2026-08-10 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce0902f-a6c6-3444-8d56-ff393ae24b9e | -15.039 | -46.5581 | 2026-08-10 05:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 91656784-b961-362f-9e03-5f991c0d5cc1 | -8.9598 | -60.555 | 2026-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e5f43e7c-4b3e-3b70-a3fe-2db1d8c38b43 | -8.9598 | -60.555 | 2026-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fa1efdd1-e4f2-3156-b9e1-3547fb81318e | -14.1458 | -54.001 | 2026-08-10 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| fb24b464-02da-32a3-aad7-a3d11aad17d6 | -14.1455 | -54.0219 | 2026-08-10 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 6a00b037-64de-3578-89db-dff8da16268f | -8.9039 | -60.5769 | 2026-08-10 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3f94ed19-e923-361d-91a0-b5405cbf7bea | -8.9039 | -60.5769 | 2026-08-10 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7b694a40-e512-30f4-8040-4191bd0ec8d0 | 2.04031 | -60.86902 | 2026-08-10 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f16c3099-42f5-3723-b6e9-6878586252ad | 2.35714 | -60.14251 | 2026-08-10 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 998b4f0f-d639-37a9-acf9-6aecf50bbc92 | -1.65044 | -54.46033 | 2026-08-10 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc9b129f-9534-3689-b9ba-a67aa2782414 | -1.63425 | -54.46679 | 2026-08-10 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0db55bac-552b-3ed6-b448-aa79b72615fd | -1.64673 | -54.45978 | 2026-08-10 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8055fca0-92ba-389a-9e6c-e89565d32848 | -2.50441 | -51.81254 | 2026-08-10 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01df016c-ec56-3592-8546-64f62d0403e0 | 1.10089 | -60.51151 | 2026-08-10 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0edcab9f-2fc7-3512-aa4a-344e86388f6e | -2.38063 | -48.22876 | 2026-08-10 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5120e5bb-bd96-37f8-af3f-bf7890c95c15 | -0.85754 | -52.71629 | 2026-08-10 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8d02359-e966-31c4-b1ee-2d70e992a0bc | 0.12464 | -51.17997 | 2026-08-10 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e05d87e-3312-308f-b517-234b02b835e8 | 1.10222 | -60.51269 | 2026-08-10 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88efed32-6540-3bea-8525-4646c7197c5a | -2.50373 | -51.81689 | 2026-08-10 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a0a4b2-dfaf-3fd4-b677-3d3ec3707320 | -1.63864 | -54.46299 | 2026-08-10 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8037b27-8d82-32bc-91b3-d3b5b52aa455 | 1.64372 | -60.14132 | 2026-08-10 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76948796-b90c-3fe4-93c7-c451baaf4525 | -1.65414 | -54.4609 | 2026-08-10 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13bb2d0f-8685-3336-9c82-bcd7294cb689 | -7.53893 | -55.5745 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f38c454-0752-3e8c-9cc3-30e53b52af1f | -6.84315 | -56.40342 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24c9da7-6429-334d-8a1a-b3dcda217172 | -8.96032 | -60.54539 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cce0523b-a617-3c99-bdf0-6256de07cf3d | -6.14847 | -57.7185 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6287a225-29b2-3c83-8668-7029a4c3e343 | -7.54336 | -55.57058 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8eea3e09-452f-3e05-92fe-ffcaaedbc142 | -6.84671 | -56.40398 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e0fb60-544f-305f-b9f7-29fbae8ed33e | -3.9587 | -48.12637 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71bd987b-1f83-3b2b-8ee8-dea4a690b5c4 | -7.55139 | -61.15847 | 2026-08-10 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ee6bd9-ecca-3b82-9e62-2f5de5d40d0e | -8.95695 | -60.59901 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e2eaf7f-472c-3f2a-843b-8b3fc924e402 | -9.3741 | -57.36211 | 2026-08-10 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e8af20f-e526-3676-8a3b-c5532c92f430 | -8.95749 | -60.56306 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9b944185-86be-367f-9cc0-d62fd8bd8d03 | -8.96048 | -60.55598 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a63f7fd5-6c16-3526-95ba-090c081ee2bf | -8.89727 | -60.57508 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b5592d94-203f-3c4c-9bd6-1fd485130fc8 | -6.82636 | -56.44202 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2aae530-057d-3139-a08a-7146b5ccd75d | -8.89336 | -60.57807 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 89eedd74-188e-3750-be9a-3fd85762e5c3 | -6.84254 | -56.40744 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8619a1c1-0090-3cb0-acec-da52767ddf05 | -8.97001 | -60.53939 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0aa6efa-1d1c-3bcc-87a7-49163f164076 | -6.70763 | -58.95694 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1798e0b-74a2-3e9c-95b2-f68f4af7dd22 | -7.69272 | -55.16317 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1da6bb1-ba43-3f09-9046-9c9568576735 | -4.46114 | -47.91456 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dec310c9-d5c7-3428-b682-c2245a03dec4 | -2.12698 | -59.59781 | 2026-08-10 05:27:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d27f1836-6870-3ed2-a6f7-f35084337016 | -6.14454 | -57.72155 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77327c0e-ecaa-3957-b3d5-fc6de6fa929c | -8.98394 | -60.53802 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 506e610a-ec13-3447-88be-25e7de176e05 | -6.24792 | -55.61882 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2734e142-5ed8-37d3-b03d-10e892809698 | -6.12991 | -57.77072 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b99a38c-53c7-3617-a509-b4c6c3507358 | -8.94198 | -60.53151 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ed98fbc-7135-34f1-aa22-114cfcda3aba | -8.96334 | -60.53831 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 049f880d-fc07-3d07-802a-bdc083588a6c | -6.72143 | -58.93423 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0712e739-cc41-35dd-9f97-652c985d6edb | -6.84904 | -56.41254 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7fabd70-d2aa-3af4-9e6a-cf05d52efc2d | -3.93514 | -59.12807 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae971d18-4b96-377f-a8a1-a5dc100a3eb9 | -6.83469 | -56.43508 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f55ad86-f1f5-386c-aff2-fd2521c15113 | -2.97782 | -51.68817 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 22cae68a-ab38-3516-aeb0-92f1940832b2 | -7.57089 | -55.56755 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71db00a9-c920-32f5-bffa-82e65d2ca2ae | -8.94588 | -60.52851 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e2283941-7924-393b-83de-712148c5c2e5 | -8.51186 | -63.36079 | 2026-08-10 05:27:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f8088e3-43b3-324e-9961-a4629a5a0dbc | -8.95361 | -60.59846 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f4807c6-080e-321e-93d8-5e0fb6e9e7e0 | -6.16376 | -57.91436 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76fa61ef-6296-3a00-be6e-e6de6794f708 | -3.96272 | -48.12897 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d5ce202-db9f-3f05-9f2c-404fb41cacbb | -3.31911 | -48.8167 | 2026-08-10 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e732c6ed-e16f-3014-bec2-65a63aef7ca5 | -3.31933 | -48.81799 | 2026-08-10 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6020b182-06ab-3852-bcbf-14b10602430a | -3.48896 | -50.05534 | 2026-08-10 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77efd4b7-8216-3504-8580-a4f2468d932f | -6.14173 | -57.71745 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8b5cc794-9406-3917-bae3-b8850ab10752 | -8.95418 | -60.59492 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6cfe002-bb56-37ff-b497-768ab0624e48 | -3.93237 | -59.12408 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a732f915-27ac-34a7-b113-2613632165bd | -8.95975 | -60.54892 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85688214-b7b6-37ec-8f52-aaa788fa1612 | -8.95991 | -60.55952 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4839752b-0f2a-31e5-89b5-d0e86257a388 | -8.16284 | -61.51936 | 2026-08-10 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187d3e0d-2c1e-37f4-ab06-005d52359ad9 | -8.89784 | -60.57154 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7c3d34fb-bf7e-30d0-b03d-6629a41d0940 | -8.94475 | -60.53559 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 121320be-3c23-3a09-af2d-5b229e8e5caa | -8.96096 | -60.57422 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd4fa77-bbeb-331a-a1c9-4d1bf5d147fa | -4.86477 | -55.82093 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af219fcf-b878-3bd8-a64d-dea94e8049d8 | -8.95805 | -60.55952 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b836cc67-61b8-3eb3-bdc9-582e9d245e61 | -6.41884 | -55.79098 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3548a0a-cbb8-330d-bd97-9847bba7e03b | -8.89287 | -60.55984 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 230f5dd7-e1c9-3db7-a05b-637985f8080a | -3.75619 | -51.60803 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c00f640f-e3e7-3bb2-bfd7-ed7df5de925e | -8.94147 | -60.5133 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
