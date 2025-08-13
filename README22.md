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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a748938-5973-3036-845a-9909649ced47 | -18.06046 | -46.01994 | 2025-08-13 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c6e8574-599c-3c39-94ae-ff4045ffc93d | -17.74685 | -48.92049 | 2025-08-13 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c9b71f-4146-3e6a-b9fa-6504541468a0 | -16.30189 | -52.92123 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8aac964f-06ef-33e6-a295-4f4cbc984f2d | -17.62362 | -44.49855 | 2025-08-13 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ce37e9b-a603-3ec7-ba6c-bdf35755aadb | -16.4019 | -50.88963 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd2f8e14-16cf-3964-ac9f-8b93beaa30db | -19.2973 | -48.42801 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a349cbae-ce2f-3307-b232-a6350588c0aa | -18.54654 | -46.06266 | 2025-08-13 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e5a576c8-8c27-3df2-83e4-82920f70d390 | -16.29307 | -52.9121 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9304347-65fb-3453-8f95-18772eb4c190 | -16.3111 | -52.92306 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e097bbc7-32c5-30b8-9fd2-90f30ad0a385 | -19.29666 | -48.43283 | 2025-08-13 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01705945-7ede-304f-917a-522203d0f632 | -16.29248 | -52.91578 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0b28785-4223-37d2-a058-200e1eaf2e10 | -13.87634 | -45.56058 | 2025-08-13 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 174f8f4d-f7c5-3036-8a08-dcb6a1a1d42b | -18.13419 | -53.82995 | 2025-08-13 04:42:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc2f5969-acbd-36b6-a032-9aa1f0b30176 | -16.96603 | -48.42025 | 2025-08-13 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ddb9de0-c035-3315-a8f8-f7e6d7b311f9 | -16.307 | -52.91074 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c645bfc9-368e-39ec-be77-d3c0d28aaac4 | -15.55434 | -43.15254 | 2025-08-13 04:42:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 688db66c-7667-382d-a36b-a4c16ade475a | -18.53404 | -46.05664 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83639e78-edc0-3c63-a270-c52ace42f18b | -18.5297 | -46.05602 | 2025-08-13 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22dba214-6948-37a4-8bba-90881588e2b3 | -16.73852 | -47.60809 | 2025-08-13 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a87c49c-2fdf-369e-93e2-a344f42c60dc | -16.29581 | -52.91637 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5729adb8-0068-361e-9a8f-ff2814b01da6 | -14.01518 | -52.04979 | 2025-08-13 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08e2cd31-229c-3bd3-9948-26b91465c65d | -14.03132 | -46.35936 | 2025-08-13 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc35d4d9-a5d5-3be1-9a13-1c79f936cc15 | -16.29189 | -52.91947 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a6bbb07-bd46-35c0-8fe0-023fea876219 | -16.30248 | -52.91753 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9307ad8f-50d2-3f2b-95b0-5ed3596560a3 | -16.39523 | -50.88847 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98f2e98f-44f7-3b95-b71b-ffd346c20d52 | -16.30897 | -52.91512 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f4b168b0-8ddc-307b-a862-f59c56c467ff | -16.91492 | -48.14837 | 2025-08-13 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57d507dd-812d-3ea4-8c77-20e6fba0e7c7 | -18.54218 | -46.06219 | 2025-08-13 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 2017f8cd-7d35-3a53-8ef1-ed2e3f83fadb | -16.3123 | -52.91568 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 997cf6b8-b50d-30b9-b0f7-e5d01cb2c80a | -16.87099 | -52.1651 | 2025-08-13 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d923d10e-3a59-357d-9c38-c43c5fc32554 | -18.54707 | -46.05829 | 2025-08-13 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 066d8d20-ec68-3aa4-b658-3dff672346ac | -15.20564 | -50.84943 | 2025-08-13 04:42:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| db0f2a74-15c0-32fb-85f8-433f6205b86e | -16.3958 | -50.88477 | 2025-08-13 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1bcd0482-4e67-3a01-892d-e280079b6c55 | -15.55361 | -43.15875 | 2025-08-13 04:42:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| da4b41ba-c381-3dec-8669-89711be20707 | -16.30582 | -52.91809 | 2025-08-13 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64e2560b-d199-3155-a3cd-bf68c70f0892 | -17.61359 | -46.70348 | 2025-08-13 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eea117d0-c16e-307d-b972-79dbd8bc2065 | -13.88054 | -45.56113 | 2025-08-13 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9ca0865-ae9d-3aa4-ad18-bd4f874a160b | -16.91287 | -48.14535 | 2025-08-13 04:42:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9d4ae2f-2441-3604-a09e-6261c9404007 | -18.86728 | -47.26904 | 2025-08-13 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dce23563-46bf-3b49-95ae-649490702ebc | -22.38872 | -45.48014 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 66d1a397-391b-38d3-afee-954829047753 | -22.24616 | -42.84275 | 2025-08-13 04:44:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| faccac06-8e63-36f7-94c4-bb120f8d40e8 | -22.38795 | -45.47943 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f3650104-8b38-3f7a-ad8c-c78aa35cb06f | -22.38852 | -45.47426 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 70e69e69-3b38-3ce6-8fb5-32ded9459ba9 | -21.81393 | -49.89069 | 2025-08-13 04:44:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 278fd022-1876-31f3-922e-cba5cb6cc37d | -22.70165 | -43.34943 | 2025-08-13 04:44:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3a7ad52-cd9d-3abc-8513-0abe8f05e44b | -22.68843 | -47.30712 | 2025-08-13 04:44:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f6e8a5-6306-39f8-9586-8a949a20fbf8 | -22.42768 | -48.56145 | 2025-08-13 04:44:00 | NOAA-21 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fad3fb71-d7f2-3f72-8015-e38de4e37f17 | -19.73166 | -45.59997 | 2025-08-13 04:44:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f6be7bb-2a70-37b7-bc22-a1f3d5b9a35a | -19.75957 | -46.435 | 2025-08-13 04:44:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f51f3a7a-5337-3537-b739-bb93e22e505a | -19.76387 | -46.43562 | 2025-08-13 04:44:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0f357ac-6e04-3776-8d2a-e75c69c0604b | -21.76186 | -46.59335 | 2025-08-13 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bf4bdb58-5918-3e09-a938-f85e8febbeaf | -20.85883 | -49.06939 | 2025-08-13 04:44:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9fc7baca-ec16-3fe3-9716-027a681ff5ea | -22.29442 | -54.8194 | 2025-08-13 04:44:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 413d3e54-c31e-3dd6-97c9-2b43ad7129d3 | -23.75369 | -55.41842 | 2025-08-13 04:44:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2954f2d-8666-3196-a3a2-374c29093171 | -21.76237 | -46.58886 | 2025-08-13 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eb44fc40-0cac-3f98-9556-3c1f313ccaae | -20.54531 | -49.31973 | 2025-08-13 04:44:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a00131d-e6f6-33f9-9389-481a1d171629 | -26.28875 | -49.86241 | 2025-08-13 04:44:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2245f793-6a89-3899-9f56-c2c847012d54 | -26.28928 | -49.8658 | 2025-08-13 04:44:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91112c2a-50a0-39dc-9fed-b69d8bdde4e6 | -24.82282 | -51.74037 | 2025-08-13 04:44:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c835dd2f-1e53-3975-a224-5c61980b071a | -22.08807 | -46.58978 | 2025-08-13 04:44:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35855c20-8061-3b34-a107-6908337f205e | -22.71212 | -43.23874 | 2025-08-13 04:44:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| efd5c0df-afa7-3bb1-8f43-e9ae94112e80 | -22.384 | -45.47933 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7a127ad0-6508-375e-a6d6-7c197a022073 | -22.38926 | -45.47493 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ff7153a2-e735-39aa-bcd1-4d17076c8c55 | -21.75664 | -46.60013 | 2025-08-13 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 767cfb46-4b09-3b0d-9e15-0145097dbb16 | -22.7524 | -47.197 | 2025-08-13 04:44:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7413b168-960b-36aa-ab64-e1ed2c5e0a33 | -19.99516 | -44.39945 | 2025-08-13 04:44:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30ed1639-7ee9-3332-b2b7-73dbcae98f34 | -23.22562 | -51.66107 | 2025-08-13 04:44:00 | NOAA-21 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59262fc7-7a88-3d26-bd5d-006baf6c55fd | -20.09099 | -47.44625 | 2025-08-13 04:44:00 | NOAA-21 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 188aebd8-eaad-3e7e-bfd6-1b0965397ee0 | -19.88499 | -44.61383 | 2025-08-13 04:44:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fb4793f6-a111-35a8-9e93-70049e3b42be | -25.17519 | -53.91591 | 2025-08-13 04:44:00 | NOAA-21 | CÉU AZUL | PARANÁ | Brasil | 4105300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b34ec29f-6b2e-3e93-9e87-afb62806e9dc | -19.87641 | -46.3927 | 2025-08-13 04:44:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bfa518a-a31a-31d8-83a5-903a42aa6c52 | -22.21096 | -54.79954 | 2025-08-13 04:44:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bbccf6c6-8dc4-3d0c-a1d4-cabfd6d27ee9 | -20.47796 | -53.67746 | 2025-08-13 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a1b6b3-c25b-3619-bc3e-26130b6858e0 | -23.61555 | -51.64869 | 2025-08-13 04:44:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2f54185-f38e-37f9-b4a1-385248d8bcab | -21.81032 | -49.89012 | 2025-08-13 04:44:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a20b5e5-823e-3cb7-b425-473b484f54fc | -22.38322 | -45.47867 | 2025-08-13 04:44:00 | NOAA-21 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fc8f9f50-2aab-36e7-8d55-21ba05bbc141 | -23.58609 | -46.80482 | 2025-08-13 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b95e610-e556-331e-9446-aea2ab68baab | -19.6842 | -49.61754 | 2025-08-13 04:44:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 98062c23-8239-3a12-8e14-e643f4b2572c | -22.13159 | -49.66124 | 2025-08-13 04:44:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1a4e84c-ebdf-3569-b183-4719bdd798f1 | -20.8893 | -55.90915 | 2025-08-13 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f584e667-48ef-3512-a36f-4c5bafade3be | -20.78663 | -54.79335 | 2025-08-13 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c648310-5930-3ae2-8e2c-23670bdb8ade | -22.25175 | -42.84365 | 2025-08-13 04:44:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c0a0581b-c2b9-3020-bd12-4e5c32e0cedf | -21.65274 | -46.53075 | 2025-08-13 04:44:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d55b44e4-e0f4-3d28-94ea-2546c21cdd55 | -20.00008 | -44.40024 | 2025-08-13 04:44:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 270eff59-ee23-36f0-9d37-f06fa9eb0585 | -22.75288 | -47.19271 | 2025-08-13 04:44:00 | NOAA-21 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6233d79-08c2-37ba-8902-b2d9f8e38e85 | -20.14275 | -57.06728 | 2025-08-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aff69370-16d9-34e3-a59d-5dd1134481c4 | -22.71252 | -43.238 | 2025-08-13 04:44:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e097ea0b-8d8f-3911-b8f0-c5d0fc83f91e | -19.88016 | -44.61287 | 2025-08-13 04:44:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 287b4542-8757-3e79-a06a-05b2e29e0877 | -28.04008 | -55.20364 | 2025-08-13 04:46:00 | NOAA-21 | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fca47415-93d3-33f2-9614-47ee6e1ee32a | -28.59939 | -50.43597 | 2025-08-13 04:46:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14ee4a6f-d948-3604-818d-2128ed8c6bb8 | -27.83119 | -50.30582 | 2025-08-13 04:46:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e619f5a8-389d-399e-b7bb-2bdc7f32681f | -27.11639 | -50.5729 | 2025-08-13 04:46:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1010c00b-b842-36ac-8241-091cee040b3d | -18.5499 | -46.0606 | 2025-08-13 04:50:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2da879d0-471f-3d9a-9cb9-d8d5b7990b6b | -18.5505 | -46.0369 | 2025-08-13 04:50:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 553c5ce5-0a77-39bf-af97-24721c4b80a9 | -16.3153 | -52.9201 | 2025-08-13 04:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| fda5650e-f499-3c68-9d30-50c5948d47ac | -2.9108 | -48.254 | 2025-08-13 04:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 09e6eeef-502d-3eec-93e5-462ab45e1055 | -16.3153 | -52.9201 | 2025-08-13 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9f32f4f1-f7b7-38a5-9198-646706fd3d6b | -18.5499 | -46.0606 | 2025-08-13 05:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 3001bfc1-09d0-3cc0-a2b2-836093e25aa4 | -2.9108 | -48.254 | 2025-08-13 05:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| db5b8137-4277-3b37-971f-7e59245730f2 | -3.07937 | -48.85212 | 2025-08-13 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
