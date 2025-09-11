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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c22cc82-cd4f-3dcc-bbc3-f2c96fa3a5a5 | -19.45698 | -43.71277 | 2025-09-11 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7a9d546-e295-3746-9588-a683d0600757 | -14.13953 | -45.41598 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a749bb00-00c7-3a33-acca-bb5cc2abc150 | -14.40811 | -47.31945 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b661805-bc2f-3ba9-bc3e-542729f8c2b1 | -17.83065 | -46.74163 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e68b791-250d-3a9e-b1bd-2ab9701373ec | -13.01222 | -48.72033 | 2025-09-11 03:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d31cd4-c28e-3861-970a-6c12a4fe42b4 | -17.71017 | -44.43863 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78d6a767-a350-3ef4-87c5-3546705e48e2 | -15.57047 | -54.76009 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 431b541e-aeef-36e5-8ffa-5a061c3af898 | -18.3469 | -44.36258 | 2025-09-11 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f4db3ef-6e39-3b80-9529-e8024799bf0f | -15.62865 | -47.53615 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03954637-fd4f-3fee-9ad3-cd4449e17593 | -20.24329 | -43.57581 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a63827c9-1caa-3d36-8749-748be617a7e6 | -17.19905 | -50.1539 | 2025-09-11 03:57:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42c9ea92-1c13-3f4f-909b-bae7c87bcdc9 | -20.70198 | -46.06803 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bc16827d-d170-3366-a6cd-83329d146d1b | -18.07034 | -45.43124 | 2025-09-11 03:57:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7c0586a-f376-3276-8323-f908d9cb5b83 | -14.41096 | -47.32922 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0489d42-37cc-3a65-b305-db3eb49c22cf | -17.80115 | -44.40641 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e09202-5fad-3376-abca-04c0480bf8a0 | -17.25398 | -46.08646 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11f6607-6e7c-3919-81c6-16f353e15963 | -16.60818 | -49.77969 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 143e5b83-1e98-3a3d-bf22-7ffcaea9d522 | -20.54471 | -47.6762 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dda05e48-b7b5-3802-9628-8179610ccb6d | -17.8491 | -44.21257 | 2025-09-11 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06159f50-6bce-3f4e-bef6-cc706abe9be8 | -15.11803 | -52.40193 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db1a93ac-4b42-360c-9a91-9f69fbd1f592 | -16.56978 | -49.73342 | 2025-09-11 03:57:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 172a842e-0484-3951-919c-9fd1b15cde0c | -20.5768 | -47.68814 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f7178b5-83a2-3956-ac4c-925e43dd1e7e | -16.88531 | -45.75696 | 2025-09-11 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f17bf3-a6b4-3a33-a7c3-118a670170de | -12.96953 | -46.73106 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4d7b996-d249-351a-b973-6b61b3e5a9fb | -18.16212 | -48.10153 | 2025-09-11 03:57:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b0f96e5-907f-3d0d-8cf4-e50389dd8b1b | -20.07332 | -47.52946 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da2e28a2-2d78-3086-bcf7-65c13b1a14a4 | -16.17767 | -48.68433 | 2025-09-11 03:57:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5de956c0-f4a9-32c3-aace-0164eb7ee233 | -13.04959 | -47.16648 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ac1def2-a067-3b47-9baf-6f6b14dfee71 | -19.66455 | -45.26733 | 2025-09-11 03:57:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee920612-ec04-3752-a59c-aa2f10afbb0b | -12.96427 | -46.7346 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 361ad243-3649-3991-a72d-0275c3bd35cc | -19.48177 | -44.32174 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03900a34-ba03-3833-8a73-b9588859bc6c | -19.96269 | -44.15038 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 619148fd-0f06-320a-830e-b4adcddaa757 | -19.48189 | -44.31853 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eed80003-f171-39df-af9d-576e27e31a32 | -15.87611 | -54.93588 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 66bd8e54-32d2-3b9a-80c2-e944668d5085 | -15.2277 | -44.01768 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a1b0bd-950d-3853-b0c1-e804851f1795 | -17.83204 | -46.73406 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec227283-7174-3605-8364-4a01b77a284a | -14.13932 | -45.39372 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7858b52-5ba3-300e-a59c-ad33386daf71 | -17.24606 | -46.08485 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b68c7694-a173-31e5-b9bd-b3b8c2b86c01 | -20.36861 | -46.66069 | 2025-09-11 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9b56282-3ba0-3c72-8d06-89f78d6936c5 | -15.75258 | -49.95575 | 2025-09-11 03:57:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55293d45-20f2-3f3c-a559-27fba389995c | -16.08731 | -47.35112 | 2025-09-11 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 610e4d76-2a3a-34b1-9558-54283f8e565e | -19.36963 | -43.26807 | 2025-09-11 03:57:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14843819-37ce-33bd-abb2-ff5b2fbe255b | -19.23727 | -48.0009 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2429e723-bc3f-3634-a77a-eb0776fc30ec | -18.33252 | -42.82101 | 2025-09-11 03:57:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e0b776e6-565b-3a44-a470-cd55c5e63ff7 | -14.56716 | -48.76955 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 524f2671-946f-32d8-8821-2992d6e81971 | -14.94337 | -50.11026 | 2025-09-11 03:57:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b93caa46-e54b-38af-a27e-2c511a506e4c | -12.972 | -46.71769 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 101f1bc5-0c6a-3525-b327-741dda99a969 | -19.96809 | -46.87899 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f01a24bc-a849-3751-afb8-4185e1c9b108 | -14.30707 | -45.03644 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6c3a016-d5b3-37f9-aec1-2648f2ea4240 | -15.11693 | -52.40706 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86aebaed-78d7-3d10-97a1-9d1004776be6 | -14.53462 | -42.47679 | 2025-09-11 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e8fdaf9-6e4b-3a56-b55e-4986352ec860 | -19.25534 | -48.00782 | 2025-09-11 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 51334ee7-fd5b-31f8-bf17-4592470a5705 | -17.07408 | -43.1922 | 2025-09-11 03:57:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef7b7097-d5ca-384c-b9f7-8141046465f6 | -14.39983 | -47.31378 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9856a130-b079-30b7-b7ef-57ef2bb50a73 | -13.85937 | -43.81897 | 2025-09-11 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cffff6cb-8284-3ece-bf9b-7f3e6a4f7048 | -18.5885 | -42.78025 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11adbbb8-87cb-3d7f-b796-b1ff829b9f5e | -15.21798 | -44.05227 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 955d7793-4221-3be1-8108-5fa71446a510 | -18.5036 | -47.3046 | 2025-09-11 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c6fe589-77e8-33f7-9ec7-3e6f66f7fff5 | -18.48807 | -41.19747 | 2025-09-11 03:57:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8af8f3f7-a2cb-333b-832f-b4ac60b38a44 | -17.72605 | -44.43286 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f8d4a9a-6415-3162-9cfa-aea516409830 | -17.82727 | -46.73695 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d88b6eac-36fc-3954-aca1-447ea20e7531 | -16.61818 | -49.41305 | 2025-09-11 03:57:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5072d88-9d87-38c0-80e5-cb83d4141327 | -13.84816 | -47.35202 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce2de963-83db-39dd-9b09-fa7e0836254e | -17.32089 | -46.67742 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2322bf8c-b6a8-3145-988b-771139d87f80 | -13.65125 | -46.99168 | 2025-09-11 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fc6f64a-b51a-3be7-82ce-e47c94ea665b | -18.00572 | -47.99526 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07a43f9b-c1cc-3d60-bbe0-256b77bb8e72 | -20.07047 | -45.2935 | 2025-09-11 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4ad5934-073e-39e2-bb55-664f6f9e6a7a | -19.99746 | -47.63342 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6149fc3e-f503-3416-8f44-3d0b5e5daa19 | -20.70393 | -46.07851 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c5d8753-1195-3d5d-a1ec-026e6bdce20e | -12.87797 | -47.95975 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8022a4c5-8ae6-3e8c-ac53-4530b1a12ab3 | -20.01981 | -41.77776 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DO MANTIMENTO | MINAS GERAIS | Brasil | 3163607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe382e5b-61cf-3e20-bee5-861a16f3bd3a | -15.22755 | -44.04035 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18b3eabd-0295-3f52-b200-b510f49cbe78 | -16.60938 | -49.77364 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 811547e9-a576-3d38-9894-7d1f7553096f | -19.7555 | -47.18479 | 2025-09-11 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52fb821c-6178-32af-8b41-42da9e6956aa | -17.84767 | -44.22096 | 2025-09-11 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dda26ec-c207-3b2e-8bfd-815eaefab385 | -20.08417 | -45.98796 | 2025-09-11 03:57:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90dea406-8da6-37b4-9e73-ed8f88e6e35f | -15.32584 | -49.55527 | 2025-09-11 03:57:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3f69f09-91dc-33c6-8ddd-09a4378769ba | -20.33843 | -46.60495 | 2025-09-11 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3029a7d9-9ee8-3c89-8345-65894a1f915a | -15.8703 | -54.9358 | 2025-09-11 04:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ff1c8f39-f03a-3b1a-9f58-cc1ae2b1147e | -22.5888 | -51.8985 | 2025-09-11 04:00:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 0d8c072d-7911-351b-9089-55f84635bef1 | -15.8898 | -54.9333 | 2025-09-11 04:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 76328652-edc2-31e1-b611-d3e984113600 | -19.2415 | -48.0033 | 2025-09-11 04:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1a1ada35-efc6-30d7-bb06-c53412f77e63 | -23.33624 | -47.32194 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0629d80-3eee-3856-a7da-558b2afd32d3 | -23.63933 | -51.67334 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7f4a4b27-091c-3011-aa27-9356965c723b | -22.56214 | -46.04481 | 2025-09-11 04:00:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b942d0d-65c7-3a7e-af0f-dfee88b94caa | -23.63417 | -51.6711 | 2025-09-11 04:00:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 693ffba2-d611-3dce-9455-40505c738d48 | -22.8432 | -47.46483 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0ad369f5-b466-3dee-b097-44ca67b38744 | -21.34464 | -45.79478 | 2025-09-11 04:00:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4573b793-55f7-3551-a42b-47c300e4b0b3 | -23.60139 | -46.9729 | 2025-09-11 04:00:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4aad135-a435-32de-b88e-ee2f151088da | -21.29279 | -47.0877 | 2025-09-11 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b9487744-64bf-3ffb-ab8c-8a6c0ecfa80d | -22.51838 | -48.55496 | 2025-09-11 04:00:00 | NOAA-21 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d7121860-5ca1-3d9a-9d03-c3f0d9d594cb | -22.70282 | -46.33312 | 2025-09-11 04:00:00 | NOAA-21 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bac7e9cc-4b4d-3917-a736-65720faa63ad | -22.59829 | -51.88619 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| a7686a88-bd76-3141-b511-91c5681dd2bf | -23.33138 | -47.32637 | 2025-09-11 04:00:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a03ca73-199c-3d15-8b98-918d806cd739 | -22.59681 | -51.89303 | 2025-09-11 04:00:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| da11626d-5b79-3e7b-903b-f5ff81c40210 | -21.43214 | -45.47264 | 2025-09-11 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d3f9712c-ce27-3f77-9857-3405b31081cf | -22.70196 | -46.33784 | 2025-09-11 04:00:00 | NOAA-21 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 92dabeb2-7ff7-3b5c-9ae3-a494e6d8a9c8 | -22.84501 | -47.47261 | 2025-09-11 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 816ac3ea-177b-3ee8-b8a7-cd0e1b76ad31 | -22.8251 | -46.43214 | 2025-09-11 04:00:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a75825b9-b36f-3cd3-b6ea-74967e18c97e | -21.40665 | -44.15016 | 2025-09-11 04:00:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
