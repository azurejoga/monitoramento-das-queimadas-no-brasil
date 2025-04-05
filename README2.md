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
| 74274aa0-9ff1-3e41-b70f-581be1e6791e | -9.331 | -37.0089 | 2025-04-05 03:36:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 93dd7ca7-cecc-38b2-8f39-01d1cd4ff7a8 | -9.75752 | -36.99607 | 2025-04-05 03:36:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0dba7da8-dd0a-3fdd-8557-7d9fb7d092f1 | -9.74521 | -37.07193 | 2025-04-05 03:36:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c79a1e71-cdf4-3f70-9153-062b03c583f9 | -9.74168 | -37.07134 | 2025-04-05 03:36:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e86bb26-79a1-3d52-bf1a-3120492a89a3 | -8.10313 | -43.12718 | 2025-04-05 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ba2c85d0-905e-35b5-8b0c-ff90cfdfb315 | -15.51507 | -42.6169 | 2025-04-05 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 182a7dbb-947d-30f0-9c67-cb10a145c3a7 | -13.43772 | -41.77768 | 2025-04-05 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cca34608-f8bf-381e-ae27-70499c7f5f2a | -13.04783 | -45.03331 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed7aeb45-85ed-3b16-a91c-095c16aaa17a | -18.04166 | -39.92589 | 2025-04-05 03:38:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dba23327-9e9e-3939-935a-ec243993e5b7 | -13.03981 | -45.0162 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c746a57-0ce4-35cb-acd7-4c3c858e8e43 | -13.04236 | -45.03212 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0336b69-bc12-3774-8de2-25d5312f140a | -14.13414 | -41.69138 | 2025-04-05 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d40ff66f-9166-3d4f-b283-a98be1ef3698 | -15.65412 | -39.18729 | 2025-04-05 03:38:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 42cef5e9-00d5-39f7-b557-314f5012ee7f | -13.04164 | -45.03575 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f88ab4-1ad1-3ac3-b78a-04d03102f2d2 | -16.03693 | -40.81454 | 2025-04-05 03:38:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41892649-e6ae-3a17-8b75-49041e02308f | -16.94882 | -39.2249 | 2025-04-05 03:38:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aaa08cbf-1c75-3282-bbef-b0ae2d2811c0 | -13.43863 | -41.77278 | 2025-04-05 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 60bf781f-a471-30fd-9204-25ec77c568b5 | -18.15037 | -42.48772 | 2025-04-05 03:38:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93a1bf99-d050-3763-b046-3d30ffe23689 | -16.75616 | -40.05582 | 2025-04-05 03:38:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3bb595af-7af3-3b2e-8437-96edd4348a86 | -13.04054 | -45.0125 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90e745d6-3fe3-38b5-8891-89146bb2333a | -17.70768 | -42.02924 | 2025-04-05 03:38:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5faec46d-08b2-3f1e-8b81-d92c1fc2f40a | -13.42849 | -41.77835 | 2025-04-05 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1138198-3fce-3b60-8cbb-3bf3548d2038 | -17.59527 | -43.19981 | 2025-04-05 03:38:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c08e86e-e964-3f0c-a563-aa39fc4b085c | -14.11893 | -41.67659 | 2025-04-05 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8f22eec-4779-3de9-aa99-feac39f12251 | -13.43357 | -41.77554 | 2025-04-05 03:38:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a4c05c24-9eb3-3dd7-a88b-d2226de57468 | -12.8777 | -38.433 | 2025-04-05 03:38:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a6ae6b5-ade7-3d89-85cc-e86bd72e52f4 | -13.0471 | -45.037 | 2025-04-05 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e91c73eb-110f-3277-a1df-4eceeabbf120 | -17.83439 | -42.62765 | 2025-04-05 03:38:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9394adcb-3237-3e9b-b520-10067a8dc944 | -20.8306 | -47.7603 | 2025-04-05 03:40:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 989b53f1-a969-3984-9f26-a611e3c399fa | -20.8512 | -47.7554 | 2025-04-05 03:40:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0bf86677-ab36-3ada-a26f-e1735ffd2147 | -20.83025 | -47.76716 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 144181f4-5f42-3226-a611-003f24cfa92e | -20.83492 | -47.77266 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8977064f-0e06-3303-ba80-2188ac16c79e | -20.83788 | -47.75946 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 876ac175-5901-3adb-a42f-8804cb84ad56 | -20.83323 | -47.75393 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e65ba26f-e825-30ee-a3c3-54d8e00bf986 | -19.83863 | -40.54944 | 2025-04-05 03:40:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c0c597e-ad80-3f1c-af7a-1b5f353b8678 | -20.8359 | -47.7683 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 14f871c2-1f40-3dc1-b18e-a1a49a368daa | -19.63516 | -48.3369 | 2025-04-05 03:40:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9277963f-1893-3626-af56-80769df15017 | -20.83223 | -47.75837 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2b585439-24d2-393e-a39a-4c3de15fc3b5 | -19.38526 | -41.47003 | 2025-04-05 03:40:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9b13ab85-a633-3ff9-b2b3-d51874f580ca | -20.15629 | -47.33539 | 2025-04-05 03:40:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 441c2590-bb13-3149-a439-78b20afba7e9 | -20.83123 | -47.76284 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ce2131ee-b88b-3464-8faf-46fd5387dd66 | -19.63617 | -48.33239 | 2025-04-05 03:40:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| db36d078-be1f-3877-87c7-5eb45b008ac8 | -19.63723 | -48.32772 | 2025-04-05 03:40:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7fecc973-ff4d-37f9-bf10-067b37c46b03 | -20.83689 | -47.76387 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 62159d5c-86d5-396f-800b-faa86dada71f | -19.64209 | -48.33384 | 2025-04-05 03:40:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 376db579-db66-38b4-a218-b6207272b661 | -19.71987 | -40.35402 | 2025-04-05 03:40:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afe2d544-59fc-3f88-b2ff-9bd54a85459a | -20.82663 | -47.75706 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7d7d393f-1ed6-34d2-981f-c605c41c1e22 | -19.84048 | -40.54731 | 2025-04-05 03:40:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6d30d82d-db14-34c2-a6d4-934ed77134de | -19.48693 | -40.87202 | 2025-04-05 03:40:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 846990b2-a17a-3fbe-bad5-9557aa73a8b1 | -19.48232 | -40.87591 | 2025-04-05 03:40:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| c0cc3268-3365-3f8f-870c-76f00524afb1 | -19.71621 | -40.3533 | 2025-04-05 03:40:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac9c17d1-7923-3cd4-8a31-f8363f6d55c4 | -20.83886 | -47.75513 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 95f01e1c-cf83-3119-b8d2-4834b3131a42 | -20.8293 | -47.7714 | 2025-04-05 03:40:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91da3be9-e6d0-3e60-be13-e3cbcd7c4733 | -27.68894 | -48.75293 | 2025-04-05 03:42:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cb7ca5e6-2604-3d4f-ad48-deac5ce3e444 | -20.8512 | -47.7554 | 2025-04-05 03:50:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 70e2733a-2fa7-3fdf-a1f9-86b06bf63529 | -20.8306 | -47.7603 | 2025-04-05 03:50:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 64cb0084-4db7-3c02-8f7b-ac399ef1c84d | -20.8512 | -47.7554 | 2025-04-05 04:00:00 | GOES-16 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 00d1c120-72ae-39bf-82c6-9c6f1380c76c | -20.8306 | -47.7603 | 2025-04-05 04:00:00 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d41e5f1a-d572-3980-a049-a70eb560f4df | -4.60907 | -43.15434 | 2025-04-05 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ce06a2f-b7ce-3fd1-bda1-c4e63e5d52ac | -5.02853 | -38.69025 | 2025-04-05 04:00:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 624091e0-002d-3daf-be93-996f0e005513 | -4.61281 | -43.15495 | 2025-04-05 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cbc9ca-3a68-3086-8b1f-006f8892ca86 | -5.3138 | -43.07996 | 2025-04-05 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b25aa55-7d8c-3179-ab3b-63a98cc233e9 | -4.61039 | -43.15252 | 2025-04-05 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9b66874-44d1-3302-8255-0e6dce760e52 | -10.57062 | -45.14017 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d1707804-97a2-376e-9e90-8f8869e5dfc2 | -10.57916 | -45.13673 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3e6b92d8-2daf-3831-9aaa-87f2b4543c81 | -8.10718 | -43.12773 | 2025-04-05 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c138234c-0819-3ced-a2d0-7b85441f6637 | -7.72889 | -39.66005 | 2025-04-05 04:02:00 | NPP-375D | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 78306b28-87b6-35a0-8a14-e2239825d48c | -10.43227 | -39.51573 | 2025-04-05 04:02:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 845fdd76-1c13-3a79-8e04-f2550fc63339 | -10.57146 | -45.13534 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8ad22254-3696-39e6-aead-dd2c78d4a049 | -10.57531 | -45.13603 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f6a9a5e7-0fe7-37f4-adf3-8420d35202a5 | -9.74581 | -37.06685 | 2025-04-05 04:02:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d0b330d-5b87-3ce9-bc1f-79bb0e36fa93 | -10.57447 | -45.14085 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e25910d6-3e2f-33f5-a55e-bb586abaf93e | -9.75621 | -36.99634 | 2025-04-05 04:02:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7e9dd67-53de-3555-91d0-bcb4e6b56f79 | -9.12598 | -40.19867 | 2025-04-05 04:02:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 62a400ec-b8a9-3f7c-a4a8-7f6a907bff24 | -9.97974 | -37.91095 | 2025-04-05 04:02:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1026be6b-f63f-3dcb-bbb7-ed1c972d60ed | -8.10293 | -43.13121 | 2025-04-05 04:02:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f02382f-10ad-37bf-bd12-3591225c9d50 | -7.90932 | -41.23334 | 2025-04-05 04:02:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dba72c51-10f5-322d-8915-3a0655d594f5 | -6.15704 | -44.42414 | 2025-04-05 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d6fb54f-0597-3e06-ba25-4f93bba96c6c | -9.74516 | -37.07127 | 2025-04-05 04:02:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fd99817b-fcd9-30fe-884e-85432b288bff | -9.74146 | -37.07072 | 2025-04-05 04:02:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17772b89-98fd-36dc-bba5-744be52bada1 | -8.04803 | -41.78329 | 2025-04-05 04:02:00 | NPP-375D | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3565b628-a62f-3492-aeb6-a7d104202fa2 | -10.57833 | -45.14154 | 2025-04-05 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04c4c6f0-538c-36a1-a19f-1eab95877cd9 | -8.61892 | -36.27711 | 2025-04-05 04:02:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6940a43d-f1ca-3518-86a6-fac83b93e0e3 | -5.97196 | -43.75346 | 2025-04-05 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2135dd88-20ee-3408-9b3d-e68459c3ac52 | -5.94081 | -44.35653 | 2025-04-05 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ff49b93-3049-3a21-9242-e3d06f99be2b | -5.94351 | -44.35901 | 2025-04-05 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ed7aee2-ed83-3717-841b-00f048d1bf38 | -9.9762 | -37.91033 | 2025-04-05 04:02:00 | NPP-375D | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bfd73264-811a-38f8-8967-098abb631ee5 | -9.33034 | -37.00959 | 2025-04-05 04:02:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 239e1470-403d-3e85-8598-48d66c5339ff | -19.6284 | -48.32878 | 2025-04-05 04:04:00 | NPP-375D | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2bbf576a-45bb-33e1-9e69-5802ac7fbe5c | -19.38442 | -41.47002 | 2025-04-05 04:04:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02e59b1d-d24e-3ba3-b9dd-949b5e8c1e30 | -17.67686 | -42.74231 | 2025-04-05 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87c51a25-b439-3bbd-9b8c-a25f35ccaee8 | -13.0425 | -45.03807 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e1fbc5-2144-317d-aa99-9271e714e441 | -13.03446 | -45.01811 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d43e8bd-376f-3aff-9a80-4702d90a16cc | -13.0462 | -45.03877 | 2025-04-05 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6cd8a5-ea49-30e9-9b5c-a2e099308c36 | -15.65349 | -39.18661 | 2025-04-05 04:04:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2fe815b6-4ea1-3f28-9973-6e7f64446a04 | -18.15026 | -42.4878 | 2025-04-05 04:04:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3a3d386-6aaa-30be-abbc-4fa7b12f85fa | -14.11968 | -41.67655 | 2025-04-05 04:04:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa120483-ab80-30b6-87ea-1df21c5c0447 | -13.48333 | -44.02954 | 2025-04-05 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a860f4be-2441-37de-9bc3-4c32060c55fa | -13.43171 | -41.78918 | 2025-04-05 04:04:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6065faf-32d3-34d8-b450-655ba70f4f83 | -13.21264 | -53.2492 | 2025-04-05 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README3.md)
