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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45f40b3d-aa21-37a7-b9ec-9a68b2f29934 | -14.62038 | -48.00704 | 2025-02-07 04:48:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2df9d76a-ce54-3d77-90b6-639c6a9a11b2 | -13.48237 | -52.94553 | 2025-02-07 04:48:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db19d3d-6524-3dd9-b10e-3b5306bfe661 | -20.19774 | -46.65966 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 594085e0-a045-3317-b2fd-4c9ae7872275 | -15.16926 | -45.63301 | 2025-02-07 04:48:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c7db46b-de3c-321e-9a8b-d37fdfb671f7 | -20.4958 | -44.14668 | 2025-02-07 04:48:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 94c834a0-b7dd-3917-9d5f-896fe101e0f6 | -20.49543 | -44.15045 | 2025-02-07 04:48:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d668654-0fb4-37ce-98d7-eab3513e5ef0 | -17.46626 | -40.86189 | 2025-02-07 04:48:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 232a6f48-d9c3-3b92-aa24-e33d7c37f8fa | -14.62126 | -48.00574 | 2025-02-07 04:48:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7528cbc0-f829-303b-80b3-a75637c38c39 | -20.20071 | -46.67538 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73f2088a-2a32-3b73-b192-a398efe6ba1f | -23.33828 | -46.77139 | 2025-02-07 04:50:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f9f0161b-3f34-323a-a09c-fced7d1e62b2 | -21.36363 | -49.18924 | 2025-02-07 04:50:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7b1af60b-bf15-342c-99eb-bfdd3f772671 | -20.91889 | -55.55176 | 2025-02-07 04:50:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 93d65219-49af-3568-8690-4a48e639f463 | -20.7631 | -46.77097 | 2025-02-07 04:50:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbab6cec-668d-38c1-94c2-f7de66f87ae4 | -22.53909 | -48.8122 | 2025-02-07 04:50:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90a8bf53-995f-340b-b119-eb2e652c8956 | -28.3477 | -49.46135 | 2025-02-07 04:53:00 | NOAA-21 | LAURO MÜLLER | SANTA CATARINA | Brasil | 4209607 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9549b3f-47ba-32e5-b361-7ab371042b8d | -6.0377 | -46.25827 | 2025-02-07 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ad28802-adb2-31c6-a18f-1b010ac22ba0 | -11.45333 | -52.92186 | 2025-02-07 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ae97b7b-b467-3250-b3b0-73284c3e7bb2 | -10.00239 | -48.49789 | 2025-02-07 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f56ee64-0957-3948-ac7a-09428e7f5695 | -10.00286 | -48.49415 | 2025-02-07 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30e91bfe-927b-30c4-b49c-1b33d062ce59 | -11.97069 | -63.842 | 2025-02-07 05:14:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d84eda36-5000-3bc8-9704-9d8df340b3ea | -12.40106 | -63.97953 | 2025-02-07 05:14:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c428335-3649-3ee6-814c-32fa07dd74e2 | -12.40057 | -63.97959 | 2025-02-07 05:14:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6abc21db-a1cc-317c-b7ab-30e6cbde7af7 | -20.19941 | -46.66533 | 2025-02-07 05:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3e82a2a-7ded-3108-9106-0ecbdbb04fd8 | -20.19889 | -46.67196 | 2025-02-07 05:14:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11c7a452-6fd8-34f5-8b32-3685818a5633 | 0.93407 | -60.54572 | 2025-02-07 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ba09b3d-84b3-3edd-a24d-7356542fc33f | -11.97035 | -63.84319 | 2025-02-07 05:35:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d850d48-33ac-324e-ab03-76f3c5e57711 | -12.40295 | -63.98076 | 2025-02-07 05:35:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 387e6968-bdd4-33ab-951d-9084205a66b9 | -5.16634 | -37.86227 | 2025-02-07 12:10:00 | TERRA_M-T | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 941123b3-29eb-3903-96cd-4ee81e1c157a | -10.61712 | -43.33243 | 2025-02-07 12:12:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a99961ca-f6ce-36fc-8869-d5766a963c74 | -12.55575 | -44.67079 | 2025-02-07 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5940aba7-4556-3e70-8084-e3e0bb29cdcb | -14.25939 | -42.27222 | 2025-02-07 12:12:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 00a5367b-51db-3b51-ba57-55b8ed7ae54a | -11.982 | -45.07293 | 2025-02-07 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2cd458cf-693e-3668-a0a6-258dd9456161 | -13.9033 | -42.43539 | 2025-02-07 12:12:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f31cb76f-25ed-336a-89ed-6a3532fa3163 | -20.20318 | -46.67505 | 2025-02-07 12:14:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b5bb56cf-fc5f-36d3-9b1c-d591c5416696 | -17.6727 | -44.45228 | 2025-02-07 12:14:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5acd4146-9b04-3bd3-985f-077e300faa1a | -18.06329 | -42.79393 | 2025-02-07 12:14:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c963ce85-26ba-3dcb-ab5b-909956b5cc73 | -18.07217 | -42.79528 | 2025-02-07 12:14:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f1c48a63-8c6e-3bc5-8ae1-64389844bac5 | -17.66511 | -44.44114 | 2025-02-07 12:14:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5e7fe2ce-14b3-30fa-b84e-706aa71fde6e | -20.20172 | -46.66862 | 2025-02-07 12:14:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 13e61ddd-bd2e-3a86-ba50-d7e51a384106 | -20.20507 | -46.66348 | 2025-02-07 12:14:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a5f069ed-8f63-37fd-a3c0-f457da6b148c | -20.15119 | -46.67187 | 2025-02-07 12:14:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cc9f66cf-bdbb-3643-8c24-c2f1e75852ae | -17.80745 | -42.31999 | 2025-02-07 12:14:00 | TERRA_M-T | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3dfce051-0af2-3394-8692-4dd8f5a89f63 | -20.20104 | -40.31208 | 2025-02-07 12:14:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 010c5ddb-6ae4-3a4d-8a20-e6287d9a3021 | -17.67415 | -44.44258 | 2025-02-07 12:14:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |


