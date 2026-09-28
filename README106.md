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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9a8d614-08f5-32fb-a693-eaddd04f7f0d | -14.33517 | -41.3868 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7e81f96d-4a9f-3a35-83e7-90a8906613fa | -13.32166 | -43.94656 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c7d1e34a-67b8-3e5c-8c0d-093cb1f1b3f5 | -11.71425 | -44.5107 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9f66aad6-b034-32af-8ccd-2b40f860acbb | -15.06895 | -40.61315 | 2026-09-28 16:24:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 24166999-f087-353d-91c1-0bb277f971ae | -14.32318 | -44.81409 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 18035e43-9634-361b-b91e-63462677dd25 | -13.55937 | -46.36583 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c07ff09b-5926-347f-90f4-225adef8f4df | -14.54573 | -40.74085 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| aeab9110-817a-3e86-911d-6b099e1a8c28 | -14.38983 | -41.25401 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b5f25660-232d-3e0b-bd87-c28712621538 | -15.68135 | -47.59142 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 072362be-7167-3210-b1e5-14c1c0758a54 | -14.32692 | -44.81359 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0e89d482-8780-3c6f-8232-70843a6c269a | -11.21228 | -44.75748 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ad1c78c-5df8-3961-9ffc-001ec85560a5 | -11.39679 | -45.41616 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9c3f926-ef01-320e-ab38-31fb31590575 | -12.79707 | -54.07518 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 81cfe473-67d3-336c-a887-0baf656221e3 | -12.27331 | -50.41185 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fb8b3cbf-95fa-398b-aafc-147ccba51262 | -12.68064 | -46.97828 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa7db17a-99f9-3734-b87d-3a0290d77c41 | -15.54178 | -47.38106 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 132cdaa7-7e4d-3ae3-8c62-68c50a3ce3e4 | -12.22206 | -50.42818 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e2be1fae-e639-3131-ad51-1301afc97a07 | -12.87651 | -44.81052 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 2be9fb36-0be8-3038-8269-eaaf49be4629 | -11.29305 | -43.54467 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 36b7cdba-a330-325b-9971-a14f21e16d26 | -16.45008 | -43.37558 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 731cbc1e-ea28-3f2a-99de-592c41d32992 | -12.00336 | -44.9644 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 188e99b1-3a38-31c0-9515-1a1dde570064 | -13.47867 | -48.62849 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ca811313-8be8-389c-ba32-a96abcca749f | -11.37734 | -43.42804 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| e6736b21-4f1a-3a5b-b3b5-996c2959f954 | -12.61632 | -45.08066 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| be94fef6-affb-3e9e-8596-3b9e4affce8f | -12.63234 | -47.26422 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 782e395c-53c6-3f91-8b30-4a75878d97e2 | -11.20032 | -44.80159 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 6d1eda9c-3d4c-3354-9fd4-809a81d4e0d2 | -15.09793 | -54.71268 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 36f7cc4e-84d5-31fe-a200-8919ac11bf87 | -15.13657 | -43.62144 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 53.1 |
| df7926e6-e259-3c78-b4cf-4d6aba08df04 | -15.42568 | -39.09597 | 2026-09-28 16:24:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4d6827c5-445e-3ed6-b562-726472c8fc46 | -12.31895 | -50.30525 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9a9ccbef-3071-3bc6-98b2-4995b7f70693 | -12.68896 | -46.97688 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1787da3-d9ab-3c41-a71b-72086af55468 | -15.47189 | -46.13959 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ff44607-82e8-38e2-ab2c-f016f6bc1fdc | -12.97918 | -44.79786 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ef4b295-f280-3e95-aab1-aae4ec568336 | -15.18296 | -46.14397 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ffc67f43-543a-387c-907f-98a7932b2dc8 | -13.4793 | -48.63366 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d42ed85b-616e-3212-91be-849c99f7bcad | -11.39546 | -43.43293 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 749448bd-39d2-3cbd-b70e-44fe8c0a56c0 | -13.48081 | -48.60686 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6a6d2788-8b42-3690-b741-4020bb97bb86 | -11.90489 | -47.00555 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e4f80db7-245b-3e9e-bfb3-ec21cfa42e68 | -14.53853 | -41.2736 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b6d50553-f01f-31ed-a0ca-f574813c5c76 | -14.52658 | -40.86055 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 57fffe15-4709-325a-92a7-083f803de378 | -15.43471 | -47.56519 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac7438c3-0c91-3131-b05e-fdcffb050fd8 | -15.46474 | -46.14898 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c33dda1-1823-35e6-94c3-a3024b637c54 | -13.05148 | -46.91275 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1c2909e-2ecd-3956-9e42-ba19ee5fdf59 | -13.33683 | -39.06054 | 2026-09-28 16:24:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 897612b2-ae37-3a71-9033-aa018b29ba82 | -12.08 | -48.54706 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c2f94a52-cfed-3ad2-b4b6-1762a73cd41b | -13.04925 | -40.45736 | 2026-09-28 16:24:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 710c664e-f600-3b64-9bbf-b4ce76dad8d7 | -13.97667 | -54.0106 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1cbd6d92-831e-3e95-9fe1-1b6ee2cb0eef | -12.06497 | -48.53928 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 54cfbf9b-87de-3649-81e3-aae258377ccb | -13.34911 | -51.32595 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 04d986c8-5d98-3905-91c8-4aaa9871e2bb | -12.8759 | -44.80616 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 15782a00-4458-3805-a3af-292839a11c16 | -12.64124 | -47.26186 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2205e0f5-ca49-3903-a0f3-dcfc41c32f32 | -14.80226 | -45.96102 | 2026-09-28 16:24:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7efc410e-00bd-363a-ae63-f5a9245500be | -11.84717 | -47.77805 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4bcb09d-d117-3aaf-9095-20205f249876 | -12.2176 | -50.43536 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b963513e-fd84-3742-8051-4be1bd8fa111 | -12.31355 | -46.40301 | 2026-09-28 16:24:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4bfb7dd8-4a5a-36a7-b2a0-d085ecff0896 | -16.30549 | -40.1588 | 2026-09-28 16:24:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a1aedb0b-6074-32b8-814f-90858af79e3b | -17.5699 | -52.57863 | 2026-09-28 16:24:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6269d39b-42e0-35fc-b7ad-1b316b44dea3 | -11.49966 | -47.38733 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6c710b45-e176-34fb-934f-82084b9e685c | -12.14433 | -50.36271 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 49c0ed60-3634-3447-b503-4093da3e1a04 | -12.1596 | -50.40001 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e4f9b8b5-55a1-3ada-ba09-e7c1fb0872de | -15.2213 | -46.18949 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c785adbc-d0bc-380b-b47e-ec529ac6a925 | -17.30547 | -44.52127 | 2026-09-28 16:24:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 3794faf4-ed6e-3f3e-ad28-99a08559ecdb | -16.50798 | -42.96254 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6c8d8d24-c039-3f41-ad03-0a52519c57d7 | -13.93798 | -49.07362 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5387e8f5-425f-3ff0-9f32-63fcb1368a4d | -14.11405 | -46.2989 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 86e70265-2717-37ed-9011-3fadc67f840f | -11.71367 | -44.53182 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| c0d15df1-ac39-3791-8f32-f0b2646d1ff8 | -11.39151 | -43.42972 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c9dce07c-58f5-32df-8616-0f67d433c657 | -14.70648 | -44.65348 | 2026-09-28 16:24:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2867a353-113f-30dd-9fbd-33b9fcd4a303 | -14.08438 | -46.32544 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 7390f7b2-5517-3163-a976-a7f4f58a9e64 | -14.40275 | -41.02648 | 2026-09-28 16:24:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7ac6f1d2-209b-3f7a-8563-c532809740bf | -12.10416 | -47.39785 | 2026-09-28 16:24:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 239ebfb1-3e44-3063-8578-d2acce2bd2be | -14.64375 | -40.69469 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8174c811-deb8-33e8-bcec-bac72c310f78 | -12.74862 | -38.16825 | 2026-09-28 16:24:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7a118d12-2d0d-3209-b70b-2735b5eafd7a | -13.36258 | -40.97006 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 24266de1-a05d-35b0-90c7-84832f4e67ab | -13.08944 | -48.56103 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d18447dd-d1b5-377b-997b-7165089001d0 | -15.16961 | -43.57552 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 77.4 |
| b1aba9b2-2025-314c-8008-9924f0b5e84f | -14.56478 | -49.15656 | 2026-09-28 16:24:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2e57c861-a3ed-340c-8a90-69a7aeadf648 | -15.41076 | -47.89471 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 520861b1-e248-3b56-981a-9eacfb0181a9 | -11.42184 | -44.96563 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 73d8c964-f823-37ec-ae0a-f48f7ec2422f | -12.37861 | -50.23309 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c29ad5c8-04c7-37b8-8043-ea5f1ed97204 | -14.19435 | -44.36897 | 2026-09-28 16:24:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb522947-7164-3771-bade-4e4c7dd71f94 | -15.26459 | -47.62617 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 807e1552-da42-31b5-b9b0-dd0fc0cfc293 | -12.61852 | -47.31863 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2e98a91b-f4e0-3653-b9b6-194eedb22ff8 | -12.06458 | -46.4718 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 60ecfb2f-1257-3d53-8ef0-709b1624af95 | -12.88082 | -44.78772 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 40836f4e-34c6-3947-9daf-4b0c477ba835 | -13.08457 | -47.44135 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b901c6d-630b-3b2a-bf76-30a9ee760bc3 | -15.18556 | -46.17123 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e70c6e7f-d96d-3803-ab0b-9ea4002aa0ca | -13.29442 | -41.10036 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1250dccd-657d-3e4b-9f98-c12dc4eee1f3 | -15.18196 | -46.13646 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 38394513-97e4-3adb-a891-8283556983a2 | -15.19013 | -46.17439 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6d6776f4-c006-3607-885b-dcee907be774 | -15.05564 | -54.5958 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4284d9ed-dd22-3310-a69d-78bbd252e9c3 | -11.77186 | -41.15249 | 2026-09-28 16:24:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 49b97fd6-076f-3ff0-802d-a4bb6d0f2353 | -11.95824 | -44.88131 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 2e47637d-abac-39fb-a4e3-c1729d3c5eec | -14.49199 | -45.22956 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ca8923a5-3b21-383a-b57e-0351f4f830d3 | -11.3847 | -43.43074 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 68c93b46-c0c0-3513-8b8a-aeadf52d0222 | -13.98573 | -39.25644 | 2026-09-28 16:24:00 | NOAA-20 | CAMAMU | BAHIA | Brasil | 2905800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5d842574-3f99-3355-b15e-68c62d74ec3e | -14.25254 | -39.9455 | 2026-09-28 16:24:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9ba5d345-9e4c-3460-919e-950af265eaae | -14.92855 | -39.94653 | 2026-09-28 16:24:00 | NOAA-20 | FIRMINO ALVES | BAHIA | Brasil | 2910909 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f28b6f30-1490-3c44-9dfc-c39c51bec913 | -11.45397 | -44.93105 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6569044e-d855-3ddf-a1ff-ca0e7ac2b251 | -13.09862 | -43.51672 | 2026-09-28 16:24:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README107.md)
