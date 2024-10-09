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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 297096d2-7af9-35cd-85f5-b1909a0317c9 | -20.65018 | -45.89417 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b11dd4bf-8098-3493-82ce-3300de55167a | -20.64153 | -45.9039 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 680d8259-6548-3e46-afb4-c805ba817df1 | -20.64063 | -45.9066 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f965901b-d773-3d56-8f77-96a35be4313d | -20.63667 | -45.92339 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8c3b92f5-ede4-3ec8-bf41-5b0bcdae83ef | -20.63651 | -45.92589 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 82866f4e-c1f4-3e0b-b672-4cc97270611b | -20.63531 | -45.92913 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c0e756fe-f27b-301e-94b5-97cfdf9f2306 | -20.63528 | -45.93126 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| be96cccf-5ae1-3a82-b0cb-4db3e913ee5a | -20.63426 | -45.90762 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6a19b166-5b6d-36b5-8606-1d6c269bd652 | -20.63421 | -45.93593 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dc06e8b2-273d-3675-98e8-177a2e4549ed | -20.63419 | -45.9339 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 75ce6aa4-13b7-3ff5-92a0-1d1419d44f67 | -20.63331 | -45.91034 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a5c3fdae-1440-3edd-a747-239d3fb8bbf5 | -20.63315 | -45.91245 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cf2e7398-983f-3f4b-bb84-6c2639ff140d | -20.63304 | -45.93878 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f93070a-34fd-3a30-b575-0f77a2b1b637 | -20.63291 | -45.94162 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b64fac9d-4760-358f-8f61-27adbd41cfae | -20.632 | -45.9159 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9560c194-52f7-3dd7-9f0f-e8d8e0ac7e1f | -20.63177 | -45.91848 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 79fda066-f28d-3212-a014-d7d8b9cf83e6 | -20.63154 | -45.94513 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e1959276-7232-3d9a-bb45-4bc377d62548 | -20.63056 | -45.922 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b4c92d67-52f1-3e61-be52-c5a2f1b88b79 | -20.63036 | -45.92465 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3977e14-3ae7-3fe2-bcfe-158a35c503e0 | -20.49329 | -47.43751 | 2024-10-09 03:25:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6f1b7f0-84df-3ca5-abf2-ad65f30fc28e | -20.49 | -47.43547 | 2024-10-09 03:25:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4699c046-39d2-3712-8c11-cad410d9b79c | -20.4884 | -47.442 | 2024-10-09 03:25:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c99ea6c1-812e-3b2c-a8e2-fae7e8878a64 | -20.40819 | -48.84031 | 2024-10-09 03:25:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d54cf87-64da-39a8-a686-12e53af0a01e | -20.39213 | -45.39994 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cbfb4912-6fff-38b1-814d-e75004d514e7 | -20.38617 | -45.39858 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fbfb7ecb-7255-3e5f-b1d9-734371178435 | -20.36568 | -48.72821 | 2024-10-09 03:25:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dade50f3-814d-35f7-935c-060f5debb3db | -20.36383 | -48.73563 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 137e26ea-6c71-3dde-a833-bfbe108dd162 | -20.36029 | -45.32043 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 826f4f0f-e7b5-37f2-9081-ad9c46e405df | -20.35832 | -45.31627 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ff8fef3b-47f0-3b70-a6ce-df6802720b73 | -20.3573 | -45.32081 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ab8b8548-4d5e-3bb6-8963-5c801d246e8b | -20.35686 | -48.73323 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e2b25f2-2eb7-32f4-a610-89b7b3dbc6c1 | -20.35634 | -48.77518 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4a28411-a809-3c28-89ad-d6593ae8d1b3 | -20.35448 | -45.31857 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3e819c03-17e4-31d8-a1bb-36b6cc228130 | -20.35447 | -48.78248 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46119b20-dcfc-39c6-ad9d-03e182287dd0 | -20.35438 | -48.77343 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6429059-4df9-3af4-9f28-da5dbda3ebe4 | -20.35342 | -45.32314 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| dae0882a-fc20-32bc-873f-ded687322e4a | -20.35257 | -48.7899 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4906635-d1e6-3c33-a67d-a18bd422c8d8 | -20.35255 | -48.78079 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c9e932-4e71-3144-be4c-935d047d12dd | -20.3507 | -48.78818 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c50c77a3-1029-350f-8d0c-21d54e7515eb | -20.35043 | -45.32365 | 2024-10-09 03:25:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1dd6ed67-d54b-3b48-8835-7e1a34d76c1d | -20.34988 | -48.73088 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 081a39e7-9731-39c0-83eb-6fa678ff5d51 | -20.34486 | -48.72067 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9757996d-297a-3914-ba17-cce71d27617f | -20.34291 | -48.72845 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 40ca2647-3620-312b-9950-7d4e826f68bd | -20.34101 | -48.73605 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 17978edf-c0a7-371e-825d-8e9c0da66c8e | -20.33589 | -48.72625 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1098dfbb-2584-3a9a-bcbb-14a9fb74d3bf | -20.33392 | -48.73409 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9454ace7-a73b-36ea-948a-580351c9c1e6 | -20.3321 | -46.21843 | 2024-10-09 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d443f2de-53c5-356a-93f6-1672ea76406e | -20.32877 | -48.72449 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f4f4127c-39fa-3491-9aec-66c2e2be4562 | -20.3268 | -48.73228 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c9ca5233-1bda-39cc-9c8c-b8d18c654079 | -20.32618 | -48.72561 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a1461436-b98e-3d95-b830-9b9342c2d678 | -20.3243 | -48.73328 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b27486e8-16fe-31b6-9b6c-746c2a98f42d | -20.32246 | -48.74073 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bf798dc2-997e-32ca-a209-990d0aca9bda | -20.32165 | -48.72269 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 89d4ec99-5535-31f3-ba6a-f9f5e336ed7e | -20.31966 | -48.73055 | 2024-10-09 03:25:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ee378738-19a1-3ff2-b203-09d8e41c8ac8 | -20.26757 | -41.36367 | 2024-10-09 03:25:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bfcfc62f-9a40-3596-b53f-5f64e4cf22fc | -20.23228 | -42.89725 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40294dbe-e7e4-354a-855c-b07a6f578417 | -20.22849 | -42.89714 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 210d8996-3337-31b0-b846-014c70b0cdcd | -20.22779 | -42.90038 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 04574a22-34ca-301e-8dad-b98c00c40aed | -20.22709 | -42.90363 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f18f3aa-e76f-37e5-a1d2-eb4920aa61c3 | -20.22655 | -42.89895 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b2f80b5-f7a5-3b51-b904-31022c03c11a | -20.22589 | -42.90213 | 2024-10-09 03:25:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 06a8cfaf-0111-3edf-a1bf-2093c85515fe | -20.22503 | -47.32813 | 2024-10-09 03:25:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9d60165-00db-3615-ad76-dc4183fdd286 | -20.22386 | -47.33295 | 2024-10-09 03:25:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 480894d9-19b2-3a06-9c15-93e7ba78d03e | -22.81104 | -48.43029 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c835e737-2ded-3521-a353-c0bab2b4dc18 | -23.13247 | -49.8157 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 490414c2-48ad-35e8-b5f9-5002b02a4d41 | -23.13079 | -49.82196 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ed8ca6be-fb8b-3503-a364-7f9356601ae1 | -22.81923 | -48.42607 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d51c367-47a1-3347-af31-7dc73e04b57a | -22.81601 | -48.43884 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51791ea4-a695-3c4b-b651-4d3cf42a7316 | -22.81244 | -48.42476 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 90fc1577-9882-3e12-860e-357f7cb49463 | -22.80557 | -48.45192 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75c54c14-3e2c-37a9-8bef-37fa2da1869b | -22.80438 | -48.42844 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45f85d2d-5027-3282-9be1-ace8edee7903 | -22.8024 | -48.43626 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 169448b2-9803-38f9-b2e9-38dccfebe1ee | -22.79919 | -48.44891 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d579efc9-e356-394d-9dc9-2d4c4548daee | -22.79565 | -48.43473 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 55cc6edb-64b4-3ccb-961b-9ce0ca924c39 | -22.79407 | -48.44096 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46cd3d8d-a719-3dc7-9acf-33015ad8d88a | -22.79269 | -48.44638 | 2024-10-09 03:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d94fc07-c1f7-3adb-a947-7bb2e0c7c264 | -22.75308 | -47.00818 | 2024-10-09 03:25:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d686c346-05fc-3d76-bb60-19a291e2e9ce | -22.75179 | -47.01354 | 2024-10-09 03:25:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5f25cf6c-ac3e-381c-a9be-7df6569dfa73 | -22.43022 | -45.49308 | 2024-10-09 03:25:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d70db25a-79bd-304c-bbdb-d9174408431d | -22.30453 | -41.88229 | 2024-10-09 03:25:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a98bbf83-4b1e-372a-8fb6-a52e6a47f912 | -22.30229 | -41.88218 | 2024-10-09 03:25:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 108a79ec-7adb-3e74-a22c-a3f72e8f1884 | -22.28401 | -46.81567 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09535791-89a3-39d4-b3f3-55db208f6b20 | -22.28125 | -46.81131 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f715f839-574f-3417-a7ae-93fcd0bba7dd | -22.28007 | -46.8163 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8b5a8e6-a2a3-3b84-9177-1f7e57379e77 | -22.2789 | -46.80964 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93ed2840-29ca-3cc2-86bb-dd6a8440f440 | -22.27885 | -46.82142 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1adcd3f-b352-3c53-aac8-ff1672fa635b | -22.27772 | -46.81446 | 2024-10-09 03:25:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccf2d6e4-d852-3cbc-8e86-c57fb5b7748d | -22.22333 | -43.05909 | 2024-10-09 03:25:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 783ffcfb-db67-3f4a-90d1-cd9e604c167c | -22.22261 | -43.06246 | 2024-10-09 03:25:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d51f140-f461-38ed-a786-e5c62fbae4f1 | -22.18963 | -48.15894 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 31510b73-7494-3c25-979d-b6fa1550a771 | -22.18797 | -48.16556 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 11631e81-aedc-3c33-92b9-f2c2ecbb4883 | -22.18751 | -48.15838 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c652ea1c-aa34-37b9-af03-355e80f59a69 | -22.18588 | -48.16503 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b2e5cb5a-c348-3d1c-8d4a-fdb7a40ffd88 | -22.18145 | -48.16322 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a50c3c9-ec7e-3e5e-a0a7-4ea7ba770fdc | -22.17976 | -48.16989 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5effb20f-374b-32a2-9ef1-b4b135458b70 | -22.17938 | -48.16258 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d6e38b15-03ba-3171-93eb-7f584a38093c | -22.17772 | -48.16933 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee298698-c574-34d8-bcc9-c01a938ff1a5 | -22.17495 | -48.16079 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b325225-587f-3681-972f-863819414c0f | -22.17387 | -48.09868 | 2024-10-09 03:25:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47761ed-cf7d-3546-a851-f9749321886b | -22.17323 | -48.1676 | 2024-10-09 03:25:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README64.md)
