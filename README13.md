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
| 33d3ea23-eaaa-392f-bea4-4f86ffa35980 | -20.12609 | -42.47702 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 9c9966e9-21a7-3a2b-a147-e3751083463c | -19.57771 | -41.65791 | 2025-09-22 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e256388-0cd3-322c-ab01-d442d0aab565 | -14.32599 | -47.79826 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b95d302a-3b20-3f9c-8f7b-7a0281f6120b | -22.00493 | -43.31295 | 2025-09-22 03:51:00 | NOAA-21 | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba5e5079-f991-34ea-b10b-99a3f8a23f9c | -20.51733 | -46.54402 | 2025-09-22 03:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c2d26e0b-0bc2-3b31-8267-1de92a5df159 | -18.88008 | -43.25052 | 2025-09-22 03:51:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7518c20c-ac9c-33b7-9c67-6ccc11d0ae20 | -19.7093 | -42.0725 | 2025-09-22 03:51:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7b39c15-b24a-3c03-bb6b-e00f0dbcfb41 | -17.93058 | -43.92678 | 2025-09-22 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66fd176f-1fbc-3577-84a0-111d692f8f9a | -18.67211 | -44.03293 | 2025-09-22 03:51:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7afefeb8-2a40-320c-aed0-7f76d9db4a8c | -17.05035 | -44.9063 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2be0b7a-4eb4-3eea-aadc-fac487f83051 | -18.05118 | -43.84171 | 2025-09-22 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 701a12c8-447e-3ed2-b6de-4948ca8d6c82 | -20.75861 | -43.36045 | 2025-09-22 03:51:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 236f8b0d-d266-3f01-b79b-264f5b584419 | -17.0535 | -44.90734 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d35e09d0-8d19-3b76-8098-9b9e34ef1311 | -15.541 | -44.32249 | 2025-09-22 03:51:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da1a30dc-faae-3910-b1e9-e2f28a3100a1 | -20.16362 | -42.15426 | 2025-09-22 03:51:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 90e2c493-346e-395d-a3a9-dbe06f849289 | -18.35839 | -43.71324 | 2025-09-22 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26b236ca-a3d2-3014-9527-6300c72f793f | -15.15665 | -49.58314 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1bad94b9-f92e-3c7e-8efa-62a5558af28c | -18.87348 | -43.35053 | 2025-09-22 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86e67075-00b7-30fc-9c80-4e74ab08a1ca | -14.97748 | -44.41869 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af8719e-c710-3773-83d1-a93aa6083105 | -15.09646 | -43.83522 | 2025-09-22 03:51:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59d691e0-992b-3b27-90ff-69586ae3a5cc | -18.35984 | -43.71184 | 2025-09-22 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47856f14-1de0-3d23-b874-d909feb4672d | -18.54508 | -43.84877 | 2025-09-22 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7fa729-b00a-3e25-8c40-1d4f971912d5 | -17.69274 | -41.52852 | 2025-09-22 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c069d5e0-2964-39e7-8ff4-94cca2a74847 | -18.98793 | -44.2293 | 2025-09-22 03:51:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96489490-6a5f-37ab-afea-a794da9a7e6f | -19.27854 | -43.74136 | 2025-09-22 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 549d32f9-9291-34c3-a90a-6ef93bf5df24 | -21.96871 | -43.29242 | 2025-09-22 03:51:00 | NOAA-21 | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1bf20eff-32f4-36d5-8fc4-cdc8441523dd | -17.13804 | -45.91502 | 2025-09-22 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbb8100c-213c-3b87-8162-e2f7dec06db5 | -19.31383 | -43.75766 | 2025-09-22 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa4114a3-e4fe-3fb7-b3f0-c8b7b82e822e | -21.62988 | -47.48968 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0e4e72f-3109-345e-be54-55e1e43e38e3 | -14.44505 | -46.52234 | 2025-09-22 03:51:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a7ab8027-3b2e-3bba-93e9-062b2ac918ab | -14.33873 | -47.79383 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fff664c3-76e4-3cd2-ad15-006e88c23fab | -17.67555 | -44.08519 | 2025-09-22 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ff471aa-e2a2-38e1-b8b4-5b627f04b30c | -16.22743 | -46.65543 | 2025-09-22 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e6ef8c4-a912-3a01-a95d-2ed364aeca2b | -18.05029 | -43.84664 | 2025-09-22 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b04e301-72b4-30f3-b01a-19359a83bdc2 | -17.62509 | -42.60857 | 2025-09-22 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 474716fe-fa60-3d39-bafb-98abad627c12 | -19.87833 | -42.44904 | 2025-09-22 03:51:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 54724e23-3c69-34c7-8709-012d125a6301 | -16.39872 | -42.25398 | 2025-09-22 03:51:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e3c8915-00b7-3414-be3f-31613d601cdf | -19.84069 | -42.21021 | 2025-09-22 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 47d7e0aa-1a32-3820-9375-e3dddf9b6c90 | -17.563 | -44.92513 | 2025-09-22 03:51:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7b46122-99b5-3b77-b3fe-81c666ee8ad7 | -20.67322 | -42.28448 | 2025-09-22 03:51:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 91423b6a-3c87-3b98-8d1c-52bf767bed03 | -17.2709 | -43.44984 | 2025-09-22 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 056adcb4-9bcf-30b6-a6bf-42cfa6bafb3f | -14.97818 | -44.41489 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f922f841-7d03-34e6-9c14-02df4d4c7175 | -17.42628 | -42.36864 | 2025-09-22 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 34715202-5ffc-31ae-a0a2-7aa91c986574 | -15.1558 | -49.58717 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 630d2704-2dd0-336e-905e-d34832281a81 | -21.13927 | -46.33508 | 2025-09-22 03:51:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 775be4b5-4cb7-39a2-b14c-c0144322ab70 | -17.05923 | -44.90403 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5091b23a-3ac2-3ba8-b649-d310ad52d768 | -15.55147 | -41.01358 | 2025-09-22 03:51:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6849b887-bdbb-37f4-9df4-128c6167eb91 | -17.92211 | -43.93014 | 2025-09-22 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 318e1cbc-ea50-3910-b878-08672d99048b | -17.05104 | -44.9025 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53346891-b2a3-349e-ba86-5713a56a9c7d | -17.76159 | -44.38937 | 2025-09-22 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe2fe624-cf3f-3bb1-b951-be169a00a3f3 | -15.93695 | -42.18719 | 2025-09-22 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 018643f4-6e70-3b08-be85-b65b6d91e9cd | -18.40235 | -42.86409 | 2025-09-22 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94e9c5d6-d163-3a08-ae78-46b9b2f17c7c | -14.44875 | -46.52886 | 2025-09-22 03:51:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 69911212-bce0-3cca-8d10-2148956e5c0e | -20.66915 | -42.28772 | 2025-09-22 03:51:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a45f07f8-5b76-363a-b180-b4c7196fe3bc | -20.61609 | -46.07628 | 2025-09-22 03:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e6f7b04-63f4-3b73-a5db-c837d98dc77f | -19.22384 | -43.75706 | 2025-09-22 03:51:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f34ea40c-45fc-3ae9-acec-6f6a417f0039 | -17.40127 | -44.28065 | 2025-09-22 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f92c9dce-3fbd-3c45-9335-9d90ce27a845 | -19.84479 | -42.20691 | 2025-09-22 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 091bdf77-6345-3af7-ad9d-56afdadc91ad | -20.36965 | -41.10373 | 2025-09-22 03:51:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f36fdda-6508-315c-8881-b0ddacf7fc9a | -20.58637 | -45.74504 | 2025-09-22 03:51:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee326bef-4f48-39dd-a5b9-2c8ee311b3fe | -18.74936 | -43.88435 | 2025-09-22 03:51:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b634432e-6ce2-37ff-9c95-eb3e6242824a | -20.8654 | -42.80897 | 2025-09-22 03:51:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7e3fa02b-87ee-3703-89cd-388619f262a8 | -17.05855 | -44.90783 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7815f554-a75b-339c-948d-8a120137c6ca | -16.73711 | -43.021 | 2025-09-22 03:51:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11672e14-5a47-3c5b-a912-063c48b2eb2e | -18.87063 | -43.34542 | 2025-09-22 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 075f631d-e693-3271-b5a4-10308be4cfee | -19.27773 | -43.74588 | 2025-09-22 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f85565a-a61f-3aef-bce8-4121e3fb9433 | -19.9235 | -42.36473 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a249abd0-1a91-305a-8380-517ff69d0b17 | -16.31537 | -43.03759 | 2025-09-22 03:51:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e040ee3-e6d2-33e3-b650-e2977d5c78c5 | -17.6708 | -44.08943 | 2025-09-22 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12f5d07e-3f40-30a8-b00f-6e8a96584f29 | -17.16708 | -45.95278 | 2025-09-22 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4919cce1-42de-3294-8d6f-75b275becb46 | -18.50472 | -42.69855 | 2025-09-22 03:51:00 | NOAA-21 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 71230d47-6a1b-3bb9-ad65-368a5542b6bf | -19.84546 | -42.20296 | 2025-09-22 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 29382a1d-1b69-359c-aa20-10c89f349c62 | -14.62067 | -49.75137 | 2025-09-22 03:51:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e8995dd-4fdb-343b-a2e3-e7317be0394c | -21.37161 | -46.17348 | 2025-09-22 03:51:00 | NOAA-21 | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 293d952f-505e-39cb-8447-ec5695396fe2 | -20.12753 | -42.48946 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9e2a22e7-5f9f-3e0f-a397-964be21c8125 | -20.60783 | -46.07459 | 2025-09-22 03:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67337e7f-1720-3740-82ec-d5b19b5f9f8a | -14.35678 | -47.78425 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9abf227-ccbd-373d-a57f-ddcfa9de0196 | -21.60535 | -44.73054 | 2025-09-22 03:51:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2779b733-89c4-3510-82bc-66bbe18c50bc | -20.67256 | -42.28841 | 2025-09-22 03:51:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d38e76f9-2bc3-30d6-a73a-15e90199add6 | -18.40166 | -42.85643 | 2025-09-22 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b4745cc7-5862-31ad-af1a-0384045d3d7a | -15.93266 | -42.19072 | 2025-09-22 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d9d9e6a-3f9f-3905-92b5-b27ee00c79e5 | -14.33283 | -47.7964 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8989528-d655-37f7-99bf-e8a84f2617aa | -17.43508 | -44.79934 | 2025-09-22 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da543bda-7f5d-3264-84aa-bdbe213006ab | -19.14037 | -44.61486 | 2025-09-22 03:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b4c455-03f0-35b8-a734-3332a5eaade1 | -20.86888 | -42.80962 | 2025-09-22 03:51:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e759baea-a157-3033-b550-ff90176e242c | -21.01689 | -45.80373 | 2025-09-22 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c379744c-ce8f-3cae-a51e-5e35adbcc8d8 | -15.09474 | -44.93963 | 2025-09-22 03:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8371faa0-3f33-34b1-806f-1f15d5baca2e | -21.0162 | -45.80743 | 2025-09-22 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfc10cc5-0b2a-3c75-94ba-4e044c4e975e | -22.70166 | -43.35085 | 2025-09-22 03:51:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fa9ead9f-f961-370b-b328-8da3f8050b56 | -14.98231 | -44.41557 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8beb9712-245d-304a-b771-4fde2d81e74b | -19.44079 | -45.17677 | 2025-09-22 03:51:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bffa170-81e6-3cb9-bd3d-506062cd070e | -20.53269 | -44.03719 | 2025-09-22 03:51:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b30309f0-4add-35d4-a9fa-e3e9abb36509 | -14.61475 | -49.75059 | 2025-09-22 03:51:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06f76195-48e4-3235-ba6d-65ef54c20232 | -19.81673 | -46.39352 | 2025-09-22 03:51:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 129d3429-6189-3e1d-ad3d-9d6b48bfabb5 | -17.10539 | -42.50121 | 2025-09-22 03:51:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 773f975b-e77c-3134-977f-e9103bd40e7b | -20.16318 | -42.15715 | 2025-09-22 03:51:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d7f9bdc8-f976-3e04-843d-b6a0340e10a1 | -15.09551 | -43.84048 | 2025-09-22 03:51:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2253dcf3-da78-38f6-8278-bc13bb1bb378 | -18.87009 | -43.34743 | 2025-09-22 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9ccc03d3-1993-3bff-9caa-71d76ee21f6f | -17.13887 | -45.91067 | 2025-09-22 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35b49b31-7f1e-3463-8d1a-ce881fd41478 | -14.97538 | -44.43012 | 2025-09-22 03:51:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
