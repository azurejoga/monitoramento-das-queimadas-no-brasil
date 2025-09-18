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
| 6a511f1d-decc-3a0d-99ce-2bc12765395e | -7.53837 | -44.71986 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca3eb2d9-30e1-3022-be5f-0f747d388c59 | -12.4417 | -49.74069 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4ca565a-14b7-39fe-94c1-23cb28c807e9 | -10.91597 | -47.85047 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f525071-5afc-3f86-8136-e0ab47b0fdc2 | -13.95492 | -42.43105 | 2025-09-18 04:14:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 736a5ef9-2800-33cf-88f0-26dbc69d8c15 | -7.81625 | -46.16721 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e392982-b485-3173-9126-90a55d2709df | -21.57547 | -44.00673 | 2025-09-18 04:17:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d2f9a46-770a-3594-80a7-78f380d946d8 | -18.54661 | -46.05541 | 2025-09-18 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff57ef8b-d3cd-34d4-9f4a-fdc1cc05afcb | -20.01468 | -47.68954 | 2025-09-18 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fb0f92a-beb0-361a-827e-4aa7347e69e5 | -19.77527 | -43.73465 | 2025-09-18 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d10fc97-62bd-3ecf-81f9-2d87e4f34cf1 | -18.13686 | -44.65031 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fef5160d-d2e2-302a-b417-4026ed3ce635 | -19.46242 | -43.79943 | 2025-09-18 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed6bad9-d593-335c-be3c-85c10f84430a | -17.32214 | -42.62987 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e29f04b9-e9a6-3e38-aa7a-ec4dfa55d502 | -18.65342 | -46.85066 | 2025-09-18 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b71f8e1c-399b-314d-aa46-7e538b14bc0e | -21.07111 | -45.61654 | 2025-09-18 04:17:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa6dd2c4-7bf7-3c05-988c-08c209760234 | -17.20297 | -45.91907 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b335d87a-c119-37f7-906e-ddf2c2e526b3 | -17.56772 | -43.78134 | 2025-09-18 04:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df653897-79fd-37e6-aefc-85947f07e70f | -18.1166 | -48.09584 | 2025-09-18 04:17:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 002364b1-1554-3339-89ae-0a09457d3390 | -20.96133 | -49.00093 | 2025-09-18 04:17:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a2f8179-781d-3c69-b992-6aa0a75a37be | -17.33995 | -42.63268 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4fd3d839-93a5-3b81-86b8-a1ece6b3b433 | -19.58939 | -57.77121 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 92a094d9-a845-3dab-ac9d-f1ae56a7c1a0 | -20.44419 | -45.24083 | 2025-09-18 04:17:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| efd1ca24-b153-3877-be1c-1c307d7cafb9 | -17.76317 | -40.18718 | 2025-09-18 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 0ed0c003-9c45-3182-929d-9daa83f9a718 | -17.35185 | -42.62591 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95bc3129-dc3b-3d08-aa4c-8c2c689b42ec | -17.17371 | -45.91031 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c667471f-397e-36e7-bbb0-7ef2fe7e2f0b | -17.49947 | -46.73712 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80298588-909c-3c8d-8454-01441adfd3c9 | -19.0301 | -48.27861 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8025475a-ab85-316d-bb90-b14fe9124de7 | -15.8849 | -43.4598 | 2025-09-18 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| abff04ac-f8c1-3156-9b96-95122473ad1e | -21.40388 | -44.27842 | 2025-09-18 04:17:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf8c81e4-1b22-3092-a69a-e579b36c90c1 | -21.30375 | -48.54597 | 2025-09-18 04:17:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f2be791-4b7c-384b-8a72-df4c9803e21e | -14.64413 | -46.38702 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db2a7e1-6dd7-36c5-8b27-d11f858c1929 | -22.26434 | -45.57988 | 2025-09-18 04:17:00 | NOAA-20 | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3404994-1bc5-31ad-8156-fbf8f6df4c79 | -20.34737 | -48.7914 | 2025-09-18 04:17:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b653d90e-1b5c-3aad-8d63-f9d06c5f5aca | -15.86204 | -47.30382 | 2025-09-18 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 576c7bc0-2c83-3de3-b055-4f6e80e9e667 | -17.16462 | -49.36808 | 2025-09-18 04:17:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4534a1e4-0fed-3ad6-8038-92fd388674f2 | -17.18092 | -45.90785 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 981edae0-3894-31cb-9935-7e2ea7cd79ad | -18.53725 | -46.05005 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebbd02d3-0d26-3e73-b5f4-8e5ad1876ead | -16.6235 | -47.01247 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ce4be44-24d7-3792-9d28-0cef0d1dec02 | -17.34346 | -46.81596 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2516e52b-a975-3f26-bae7-4b463e279fca | -16.69324 | -46.94803 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7fe26ae-1aea-3f7b-a0fe-63b5341b3b66 | -15.70549 | -43.81937 | 2025-09-18 04:17:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c1600fb7-60dc-3c60-92e8-79040bfd9ef5 | -15.85107 | -59.47453 | 2025-09-18 04:17:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3fda02c2-0532-376a-8be1-796c0bc799ca | -17.34828 | -42.62535 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6509605a-f48d-3dde-94e8-5d833961090f | -17.31798 | -42.63353 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dad158d-46c3-3450-8790-9eb14637fa42 | -20.79059 | -49.43548 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e144618-a87f-344a-8225-d710238dbad6 | -17.17702 | -45.91088 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 800400cd-0b11-379e-9f3c-0e2e95bce87c | -16.02789 | -45.16814 | 2025-09-18 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4296a50-66e9-3a95-8cc0-e11e89f78016 | -17.46115 | -44.78926 | 2025-09-18 04:17:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 022ed8a0-821e-3b80-a2ca-2fee9734ac1e | -17.87211 | -39.83622 | 2025-09-18 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d264893-32dc-3313-b16d-f968de7cd98c | -19.58802 | -57.80493 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 89d7e221-907b-3e78-ba1d-0a1ea5a1b1a3 | -19.96519 | -42.11517 | 2025-09-18 04:17:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e5821c67-fe74-31dc-9400-f1ef845ca869 | -18.75398 | -49.32196 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 260d0af7-62b0-30c1-a805-cba4fe8aebd3 | -17.41066 | -46.98444 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 084d4447-9a6d-3a51-9f55-6a531d01ca70 | -16.88552 | -45.77969 | 2025-09-18 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b506c628-6086-3922-ba9d-4a3d7c0e6ccd | -21.06928 | -45.61363 | 2025-09-18 04:17:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36d53e53-2e9a-32e6-b1f1-ef16e0b5da6d | -15.3797 | -44.27372 | 2025-09-18 04:17:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fb54d025-2c2b-3a37-ae67-fa611f8faf8a | -16.02845 | -45.16456 | 2025-09-18 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a70bc4b-f699-3e8b-bf25-11801aa18172 | -17.31858 | -42.62929 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e843b1c-ffda-3197-b49e-dfa2c77cad3b | -15.78613 | -43.34698 | 2025-09-18 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d17fee6-33d9-3c80-b2f5-ab958f262709 | -20.70235 | -47.85713 | 2025-09-18 04:17:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5056effb-31b8-317a-97dd-6afce5d567e7 | -18.64941 | -43.88726 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9266c7f7-3298-3a2f-a6f1-72a3d2011dce | -17.0092 | -45.85624 | 2025-09-18 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93e51bb0-e558-317e-9a0f-b2cdf85bb432 | -20.81182 | -49.43984 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d3245aa-cc39-304d-b99e-1c62a5fc0ef8 | -17.34466 | -46.80859 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28a1878c-c133-3b1a-a67b-d3f8f0e27855 | -16.01238 | -42.36134 | 2025-09-18 04:17:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af7da7ea-c54d-392f-b1a3-27a1f7aeaf44 | -16.22848 | -40.12101 | 2025-09-18 04:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7467663b-6c04-32e5-8dfd-064975e4e4d1 | -18.58113 | -45.0251 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77cbf3e3-cf1a-3086-b8c5-379c1f32a7bd | -15.50041 | -46.28042 | 2025-09-18 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc0520b-5c5d-36ad-b619-1a5ebb5983d8 | -17.06439 | -48.13465 | 2025-09-18 04:17:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85bb0e55-f6bd-3d00-b0cb-92eec0296a47 | -20.6716 | -48.75534 | 2025-09-18 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 06bd4afb-5e9c-301e-bf51-93aaca51ecfd | -21.30375 | -45.20271 | 2025-09-18 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6a8391f1-1094-318b-9461-4e966cf24423 | -18.34446 | -43.29771 | 2025-09-18 04:17:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eb95b916-ba19-375f-8b0e-b773146b493b | -21.57606 | -44.00256 | 2025-09-18 04:17:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14826daa-32fa-3d9d-9f0e-13f1e9f4a210 | -20.53166 | -43.07488 | 2025-09-18 04:17:00 | NOAA-20 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 576b1e63-203b-339a-94cc-d758c7221ecf | -15.40933 | -46.17081 | 2025-09-18 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f466f4fa-dce0-3348-88a9-293526d594c9 | -17.19258 | -45.89875 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4193daf-5ba0-359b-b0e6-a5e2a4456060 | -18.57055 | -45.02719 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72caa127-f551-30eb-8fe7-72940c4e020c | -17.33639 | -42.63213 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6f05035-1e8d-3075-b8e9-a6a630d59fe7 | -18.58057 | -45.02881 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ec1df7c1-e68b-351d-aaab-a891d634e536 | -21.19216 | -50.15455 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d052b56b-400e-3333-843f-557de528e07f | -17.34192 | -46.80432 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a621858-8091-3cbd-879d-b6a9da160ecd | -18.14079 | -44.6471 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6373a5fe-c2a8-326c-bc8b-bbecef988814 | -18.57667 | -45.03196 | 2025-09-18 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 913fad6e-f117-3014-9b9d-fae8f82240be | -19.34087 | -47.93853 | 2025-09-18 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63bef83e-e80b-3468-b9c6-3894e10fe79c | -20.06106 | -50.37161 | 2025-09-18 04:17:00 | NOAA-20 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 555fe6f3-56e8-319e-b8f9-002663ee63ba | -21.52093 | -44.9898 | 2025-09-18 04:17:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5d22471-739a-3134-8005-c1e902bab455 | -17.68116 | -44.14473 | 2025-09-18 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1471a04e-2710-3cb1-b50f-de2ac992d6c9 | -18.36486 | -43.30495 | 2025-09-18 04:17:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb0f6cc9-dc5a-3b0e-9d04-fe4a9b062236 | -20.1767 | -42.1459 | 2025-09-18 04:17:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 887ac63f-e1b8-336d-98b3-6ecdfc031477 | -18.64884 | -43.89112 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f0f6b62-872f-3ca3-bad5-5e89cf443db9 | -19.58324 | -43.99663 | 2025-09-18 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f0bb1b6-3518-31da-a03c-463552c62048 | -21.51697 | -44.9931 | 2025-09-18 04:17:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93729f19-fc20-3a52-8125-7a7b241a3307 | -18.61826 | -47.43122 | 2025-09-18 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356dd996-3818-3ef3-b3e6-3ca426bd3e64 | -17.87666 | -39.8361 | 2025-09-18 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bf4b3e66-4e8e-3f16-83cf-e436b3e88f67 | -21.05317 | -48.84236 | 2025-09-18 04:17:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6b2e23de-99bb-3328-9b51-a20be00fa394 | -22.16817 | -44.74496 | 2025-09-18 04:17:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5082186-0e77-3f75-b709-1b4a4dc06abd | -17.18365 | -45.91203 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c0192ab-5796-39b4-ad09-1d3e0a823950 | -16.28611 | -45.68175 | 2025-09-18 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2489a710-cfa4-3045-bff3-a9e9079e7717 | -14.61996 | -46.38663 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a366e25f-23ec-311a-a976-c209cff8411d | -18.65445 | -43.70661 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 07db7c78-ec43-3278-ba42-ff06f23603df | -15.77432 | -49.79985 | 2025-09-18 04:17:00 | NOAA-20 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README24.md)
