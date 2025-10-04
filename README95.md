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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d66c8e4-6066-36ef-9c45-5a0ab895cf2e | -15.79524 | -46.26434 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85421595-8bcd-327d-ba7f-9b039e568d64 | -16.02544 | -50.84464 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c7f1f0-7933-37f7-a0dc-2f835c843d5d | -22.45138 | -44.42138 | 2025-10-04 04:17:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0cf4271-09c3-3e02-90b5-2bf61ffeb25b | -16.01365 | -50.94167 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61a74542-5cb2-3a9d-b693-106eac7f6bda | -18.17216 | -53.35449 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b6d34c8-88b1-3e17-ac39-c973c25de06f | -15.34356 | -47.82475 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef72ae07-cba6-3646-a347-d7961c346442 | -14.93516 | -49.97261 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2151e480-8e3b-3596-8f04-0bff1c6e6d71 | -14.57815 | -52.48655 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34e956f2-40a2-3cc9-a372-7f97f2dee3dd | -18.45437 | -49.44714 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1527611-423f-3982-9461-88d5e51dabf0 | -15.70528 | -46.2751 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c04e40a7-6114-31c0-9dc4-b2f04131a25c | -15.5944 | -52.49096 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 399ea1ea-03c3-31d1-9544-4ba727e9da8e | -22.2866 | -46.7218 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce33efb9-4370-351c-94f4-6afed3f6b729 | -16.02687 | -50.94 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 618a3bef-8d38-3c3c-a252-ef69e347558a | -14.988 | -49.95263 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68150e0d-a04e-3d73-8b2a-a4daf5891b40 | -14.98509 | -49.96919 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2456cea2-715f-3ba2-9b60-d2fa8b187aee | -19.94841 | -44.71709 | 2025-10-04 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23dfed87-925c-3e1c-875f-14318c99311c | -15.53287 | -46.8142 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 701a5022-4b5b-3868-a334-f78d24ce1be2 | -21.68989 | -50.0718 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 85688ad1-1bdd-3537-8e3b-1c5ee1ad6896 | -20.41489 | -44.13583 | 2025-10-04 04:17:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6fad2fb2-cacd-301b-bde9-44d93bfa61ac | -15.59799 | -52.48829 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff02bc07-0dcf-3abf-ac45-427df0bf6205 | -15.22338 | -56.81632 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2a87921-f895-3582-a6ad-9766e10ca839 | -18.23401 | -53.37228 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376a0453-38fd-33c3-a9d7-fea7253eef05 | -16.35462 | -43.41803 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74be8e3a-31aa-33b9-aedb-74331affb1ed | -22.07598 | -43.09247 | 2025-10-04 04:17:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9d459a4-6c17-3dd1-8ce8-4c6630e3f7a1 | -15.72535 | -46.27865 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8db1ee4-2a85-390f-9cd2-0d1b6a658305 | -21.07154 | -46.90524 | 2025-10-04 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40558d1d-22c4-33fa-917f-fae6f5da7ba3 | -20.29799 | -46.73018 | 2025-10-04 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9515d0ee-a870-33a4-ace0-3a0d3c87f2b6 | -22.76064 | -45.30176 | 2025-10-04 04:17:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9c87c2ec-22f7-3f9b-b914-d3d6c5b39d2f | -19.49743 | -43.62946 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38f7302e-680d-399c-8805-976d8b72b6cd | -15.61843 | -46.93386 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbccc880-83f2-3266-9d24-fc963bb08818 | -15.56179 | -46.9584 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 357c2aa0-31c8-33fc-87e5-9aabe2c0085e | -16.82043 | -46.73262 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b272685-c9a5-3ebc-9c1a-af444434f3ea | -15.25648 | -48.05723 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a47c9a-8a67-3435-ac95-60fc216bf77c | -15.71258 | -46.27248 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be18e72e-747f-31e7-aa61-ef3dd1d5a577 | -19.69501 | -47.9666 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d4fc72-745a-34fa-9cbd-111c79a6b890 | -17.5821 | -44.49276 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7641186-d5d4-398b-a653-3f65115b8735 | -22.28271 | -46.72491 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46eb59b7-76ec-3ac6-9911-e322abe64539 | -22.28095 | -46.73607 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1db2429a-37a7-3288-b3e6-ee4f23e108f3 | -16.02127 | -50.94691 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd118257-cb14-33eb-b4b6-0a80e20fe3d3 | -15.52577 | -46.83617 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd451244-64cd-37da-af03-bc3503db6b2c | -21.34081 | -44.9931 | 2025-10-04 04:17:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0e7c2143-ca65-3475-b9b7-c0c656b4000d | -20.12906 | -43.98697 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b4493382-8f2b-3b7f-a0fa-6205e4efc58d | -16.01169 | -50.92923 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15e15017-d668-3d17-a14f-d66d2e74d010 | -15.62121 | -46.93824 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a87b978-f407-300f-8a7a-ff16950b97ef | -18.17114 | -53.35979 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b2549dc-984f-3f43-a7d5-3e5e4e86bccb | -22.07537 | -43.09701 | 2025-10-04 04:17:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 219fc941-46a8-38ab-97ef-267a77ec21ab | -15.57234 | -48.18381 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57fa0fb7-bf9e-3e54-9009-3009666910dc | -20.06828 | -43.75577 | 2025-10-04 04:17:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf3d829c-aa71-3605-a265-66dcbc2c4cee | -19.13487 | -43.14406 | 2025-10-04 04:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76388ec0-70f3-371a-bc65-e421be496e48 | -19.58034 | -48.02119 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbfb91ed-f9c4-30c1-a464-d2fdc0062eac | -16.28811 | -45.24443 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b538baed-8547-3b3f-83d8-c4fbf2c66495 | -15.21601 | -56.85094 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d050b6e-dcab-31c3-8466-141f1d6c8ff3 | -18.17478 | -53.35274 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b935d10c-1ee6-3b85-8f0b-a8101a9fe798 | -19.77838 | -43.56209 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee109fef-9742-30d3-8260-6ca30ba1872f | -21.69511 | -50.06356 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87aba9d5-2a74-305f-8d80-e3a007aa0fe1 | -17.61723 | -44.46469 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbdc5eec-4c39-373e-b056-725022fd8662 | -15.60471 | -52.47855 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b85b8e79-e068-3ee4-b7df-b45d0e632083 | -19.50661 | -43.61516 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 296f631f-3c54-35d7-b428-a9dfb4615cf3 | -18.27835 | -45.91013 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e61c40f-2d50-3e56-a96b-2e750f9ffe0b | -20.72162 | -49.61309 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 31f22b67-6025-3095-9455-43639315fde1 | -22.28446 | -46.71376 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 13b77b67-14f0-3b56-8dc4-c127da2660f1 | -15.23852 | -49.29382 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 971da952-eb10-31f1-8b28-973c528aee10 | -15.53041 | -46.82919 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac73dbf6-c548-3694-9c13-2d05a9344aa0 | -20.51753 | -47.53566 | 2025-10-04 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03ff8449-5b0b-354e-8938-8b0b51041fbf | -17.5654 | -44.4898 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f5de7a7-f664-32e8-8a00-935278ee0d94 | -14.74404 | -54.64048 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 523d4dcb-b531-39cb-917b-43bc035dee55 | -15.33487 | -47.33322 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b42177c4-e8da-30e0-94ee-252929c9b547 | -15.21313 | -56.8344 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ff1a27e-ae81-392e-90f4-521ea8f0ced3 | -22.2825 | -46.74783 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8283f85-603f-3e84-af9f-547234f9e5f7 | -18.27561 | -45.90593 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3eb5d78-cd74-3894-8bd2-17c3c0b30334 | -16.02276 | -50.93899 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d1f93db-404b-3070-bf09-a2f3819f1bcc | -18.63607 | -50.67881 | 2025-10-04 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 58b2846f-1028-35cb-81dc-5395f1c2cecd | -15.52969 | -46.83609 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7428bbb3-4357-3c5b-901e-166111362c25 | -16.34003 | -42.38466 | 2025-10-04 04:17:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b030b39-eb3f-3394-8138-6d99f43cf323 | -15.59067 | -52.48533 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0998f7c9-680a-3698-adad-2ecabf290ebf | -15.73663 | -46.26527 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e07cfc-e036-3fbb-b000-acd3e0957b4d | -20.13976 | -46.42337 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80808b1c-2906-3c8a-a6ad-7486810f1ab4 | -21.69191 | -50.08155 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1b3a4384-fa0d-3360-958f-a9de62f964e1 | -21.31223 | -45.18369 | 2025-10-04 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 571aa856-65aa-3ac1-aef5-1954052c2dfb | -16.09424 | -51.06603 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1dec396-fda6-3799-8a59-5d6b09ccac5f | -19.35186 | -43.78665 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a14e06e5-142e-3fda-ae15-8ae54ccda43f | -21.68265 | -50.07033 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd381bcc-5edc-340f-8e7b-055c092092ae | -21.62092 | -47.39884 | 2025-10-04 04:17:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cb63313-e64a-369f-980c-3ed11be46d9d | -22.37231 | -47.05783 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e36603cf-82c6-3803-8798-0ee420c9adc3 | -22.36899 | -47.05722 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7987d4b6-ad82-3d36-a738-a3ac338ac0a4 | -19.81852 | -46.06977 | 2025-10-04 04:17:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50fe2f8f-25a9-38bf-a39b-2b1c35c2c9ea | -20.27277 | -43.7896 | 2025-10-04 04:17:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8e4583b-84f7-3b71-83be-717ea5c4d701 | -22.76403 | -45.30232 | 2025-10-04 04:17:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1dc84145-3fd8-36bf-9b0f-39fa7fef4417 | -16.94011 | -52.67417 | 2025-10-04 04:17:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e247ec24-9612-3e85-8132-4e0357a5206e | -18.45205 | -49.44365 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ac93527-0dab-360a-a1a6-af78950f2f8a | -15.6925 | -46.26906 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be4f45f5-966a-35c3-98ab-655a40028d4e | -15.61782 | -46.93758 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2b04ab2-e811-339a-b5ae-44858f9b1571 | -16.38836 | -52.16986 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84b2bb11-1bcf-3bab-9417-fba15fbb3f82 | -16.81281 | -49.25728 | 2025-10-04 04:17:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c68523-525b-37c6-a9c3-3cd44af8e127 | -17.99191 | -51.63918 | 2025-10-04 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3cbcfab-5ac5-3491-be39-6b3de14eebe1 | -15.53621 | -46.81795 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf9777a5-506f-3ea1-b1eb-e8df0befa1b6 | -16.09349 | -51.07016 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 392fbc3e-d771-3bc1-9f57-0642e9ebee44 | -16.01151 | -50.92164 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f778e714-4fc6-3332-92ff-a15ce507ddcd | -19.97332 | -43.71215 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb05e5ee-17e6-3dae-8090-c6947540a11a | -18.23024 | -53.36677 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README96.md)
