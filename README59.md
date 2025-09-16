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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1309870c-c547-37a6-89e3-ca022b376b9c | -13.78552 | -54.95548 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1f81c6e-978d-3c15-b707-e241e4a77707 | -14.28207 | -45.99544 | 2025-09-16 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78e5e10f-26fd-3d7f-8f12-e5289928b08c | -16.01884 | -59.24885 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a14348b-8824-3120-9e8f-080cda5d0216 | -14.42106 | -53.36427 | 2025-09-16 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96d6ccb4-4adb-3c4d-8490-11d4377eecae | -13.2848 | -54.23631 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6383448d-2d88-3548-8790-e1685e867fa0 | -15.90192 | -47.3105 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da931c0-a88e-3329-a1d9-254ced832528 | -16.00636 | -59.25101 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fa95c60-704b-3118-ad7d-3f9164043214 | -15.89812 | -49.78378 | 2025-09-16 04:32:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e8db561-0371-3a1f-bef1-41d6b8c3208a | -16.01639 | -59.45289 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c9c6c56-96fe-3e31-92c0-addbb20e5ac0 | -14.54766 | -47.37032 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33f53651-b15f-3d8b-9b83-6567ce18a78f | -18.1692 | -45.19528 | 2025-09-16 04:32:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d20944de-a23b-3e67-8a89-441b0a1b99bb | -16.71699 | -49.23147 | 2025-09-16 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baaef885-905b-3574-9869-d5a514679fcb | -14.51865 | -47.36983 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df6b6f57-b83e-333c-a988-d8d63f75efc0 | -14.54209 | -47.36187 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 92113570-cf92-3a3d-b113-48f7f167f64a | -17.22813 | -44.43585 | 2025-09-16 04:32:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a43a13ea-72ec-31d4-be6e-e6dc2c32d7b5 | -16.28085 | -45.68288 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85266bdc-5ff8-3ba6-af5a-c76e71892d9e | -15.58898 | -47.93763 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27cd0c18-2140-3dbd-861c-aa793b16c284 | -15.9015 | -49.78436 | 2025-09-16 04:32:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17a600e5-9f95-3ffe-ab68-3a8e31297377 | -16.69259 | -49.77584 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 293e7b42-e9e9-3a4f-ba56-7df66eb019e5 | -23.14122 | -49.63772 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dbd5b998-572e-3efa-8bdd-3343b6b1f57a | -23.25939 | -48.28794 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2716801d-7d19-3c85-bd49-076748fe6209 | -22.98058 | -49.95459 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2fc1d27-9712-3caf-ac8c-b248fb44b505 | -23.14849 | -49.63515 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a45ae3b2-6308-3b0e-80b5-186c939094ba | -21.5808 | -46.79934 | 2025-09-16 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a17d5138-2496-3b0a-909c-1fbec305faea | -23.14064 | -49.6415 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7b4f994a-f742-30ba-9ea0-770f15b30c58 | -22.68447 | -48.29915 | 2025-09-16 04:34:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8030891-b7d0-3e4b-812e-47b4af1c97cf | -21.92604 | -48.2505 | 2025-09-16 04:34:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07209214-a1ae-3f7e-abf9-803bbf1fd39f | -23.25997 | -48.28391 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6e20307-6c81-3278-98ff-58f8af31e939 | -21.93957 | -46.56875 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ed1eacdb-3a9f-3d46-829b-14e09a2b1787 | -22.06378 | -45.14854 | 2025-09-16 04:34:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 96d7ab26-c61a-308f-9278-399ed126f236 | -21.58379 | -46.80417 | 2025-09-16 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e0185a7-7084-38d6-9473-251d2d851de2 | -22.21632 | -48.35721 | 2025-09-16 04:34:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67d32dc3-7605-3e81-884b-e50f97e8f2d0 | -22.99019 | -49.937 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e42945c2-3798-32e1-be5a-448a89aca0f4 | -23.39544 | -49.50262 | 2025-09-16 04:34:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f392f1e-5984-31b1-ad2f-e323f0d8d885 | -22.2027 | -48.35482 | 2025-09-16 04:34:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51c9bfed-5564-3fac-a0f0-25d1684b2a0f | -21.93895 | -46.57323 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| ebbda5f4-fab3-39a1-ae4f-e18503bcdbd8 | -21.77068 | -45.4794 | 2025-09-16 04:34:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 335db120-0d8f-3297-b308-fabba72d269d | -22.60622 | -47.65289 | 2025-09-16 04:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2379d2e-087c-3d57-a2e3-18dbb29eaac0 | -22.57026 | -44.74188 | 2025-09-16 04:34:00 | NPP-375D | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9bdb361f-7e3e-3523-a089-11658ebe8a7c | -22.51572 | -47.60552 | 2025-09-16 04:34:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 22d3542f-8877-3486-a378-6cf5c6d71d1f | -23.34382 | -51.06841 | 2025-09-16 04:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 86d1a01e-c745-3b97-a6d8-cf427a2ffea6 | -22.98175 | -49.94707 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a9ba6e4a-5a63-3817-b882-e967cf3c770c | -23.20218 | -49.63303 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 644abc4f-5d36-374d-8eb9-89c1b8e0108a | -22.71577 | -43.23942 | 2025-09-16 04:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29ac0b57-f63c-3492-9f5c-be1cd6971dd6 | -22.17204 | -49.61252 | 2025-09-16 04:34:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e9a4e542-aec3-3d9d-a9ac-ea71caa4f695 | -23.03679 | -45.32918 | 2025-09-16 04:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2066e1dc-793a-3717-a1d9-46551a7d5514 | -22.99234 | -49.94514 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 56b4e4cc-97ea-358a-940f-175f1e13f4ad | -22.71632 | -43.23471 | 2025-09-16 04:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 746a675c-197d-32ae-b144-c2950972bfa9 | -23.25653 | -48.28329 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa96fee9-cb2c-3b48-8e11-fd7545f4755f | -23.4463 | -47.67786 | 2025-09-16 04:34:00 | NPP-375D | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8e5de97a-3099-31ea-b314-2187e348a7a1 | -21.93532 | -46.57263 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8b021d04-b2ed-3792-9bbf-1ad7c08c1293 | -22.0677 | -45.14921 | 2025-09-16 04:34:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 299b9f7a-e160-3dff-9b56-339d699f42a2 | -23.39602 | -49.49881 | 2025-09-16 04:34:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2176f095-3e70-38d4-9e56-167e05cc621a | -22.08375 | -46.65337 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d8133073-a45e-3a33-983a-60dcc07e783b | -23.1644 | -47.63881 | 2025-09-16 04:34:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3487127b-fe99-3cea-8d07-2b3af9129224 | -22.34536 | -47.33638 | 2025-09-16 04:34:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17d483d5-01c1-3466-b7c1-42c2ead1458b | -22.08677 | -46.65839 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b5cc9a8e-7784-3fa0-9cb5-411f0f7a0e4f | -23.13012 | -49.70955 | 2025-09-16 04:34:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 899a3b09-cb41-3d1f-b23a-39c2886f87d3 | -22.60272 | -47.65231 | 2025-09-16 04:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38e94733-5b42-3159-8e9a-d2e80001b92b | -22.23468 | -49.37274 | 2025-09-16 04:34:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f6feed6-e6b2-3c25-8b17-48414ba995c4 | -23.25595 | -48.28734 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a849789e-eff7-3fa2-bca4-d4657e090778 | -22.08679 | -46.65603 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| d5ce56da-52e9-3f99-8760-80a7fcd39b95 | -23.34109 | -51.06398 | 2025-09-16 04:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 328a8a7a-c506-343f-8aef-2cc44e0bd8f0 | -22.68789 | -48.29975 | 2025-09-16 04:34:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9649789c-9e47-3f38-a1da-8b2175e709eb | -22.08316 | -46.65549 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 023eccf0-1dea-3a6a-824d-ff9ac3c924d4 | -23.03751 | -45.32344 | 2025-09-16 04:34:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3b3f8b62-de49-3d55-a785-e1d1a7323687 | -22.08738 | -46.65391 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| aafd8968-3ade-3de9-9dc0-2c3ac8f486ef | -21.58439 | -46.79987 | 2025-09-16 04:34:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 89573144-61c5-3d4b-b121-e118cb3658e6 | -22.99567 | -49.94576 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a61aafc6-b500-38ef-8a81-9d48b909b5b8 | -21.93594 | -46.56815 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e986e795-3557-34a1-8638-db44ec356ba2 | -22.99411 | -49.93385 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f6d4554-c16a-3898-95f6-b2e6951624ef | -22.21291 | -48.35665 | 2025-09-16 04:34:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de9683d0-6ed5-37f0-9640-9abc2eb51c44 | -22.7113 | -43.23883 | 2025-09-16 04:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e2388ce-830e-3207-bedc-d656b0437a4f | -23.44689 | -47.67374 | 2025-09-16 04:34:00 | NPP-375D | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f67cb78a-9015-3ad4-bc78-d897a30efe53 | -21.92205 | -48.25383 | 2025-09-16 04:34:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf30b61-33b1-362d-8427-c602e593856d | -22.21691 | -48.3532 | 2025-09-16 04:34:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f049f3c-dc67-39fa-8419-9b8d287d6803 | -23.12678 | -49.70894 | 2025-09-16 04:34:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d37d3eb1-9420-31df-93a8-954ba2ef846f | -23.39937 | -49.49942 | 2025-09-16 04:34:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0be47512-faf6-3992-bfb6-c451568185c6 | -21.77133 | -45.47445 | 2025-09-16 04:34:00 | NPP-375D | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cddd43eb-3d53-3971-a72c-d02770793de2 | -23.20383 | -50.81971 | 2025-09-16 04:34:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f49f9e2-4a70-3bb6-b162-da27e4d5a172 | -22.36573 | -49.10086 | 2025-09-16 04:34:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f80df11-ee08-38a2-bd4b-043fa83f868b | -23.34048 | -51.06779 | 2025-09-16 04:34:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e8e59a21-a183-377b-a2fc-2583f0db24a6 | -21.92321 | -48.24597 | 2025-09-16 04:34:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3121aa46-d784-3c63-a89a-6ab59448e5ef | -23.79478 | -49.79447 | 2025-09-16 04:34:00 | NPP-375D | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 553365cb-c2cf-37e7-b522-4a9cdfdce5a8 | -22.0638 | -45.15259 | 2025-09-16 04:34:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c6c0de92-33dd-373d-aa88-15ae2405886b | -23.14574 | -49.63072 | 2025-09-16 04:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f59b9439-5326-3c1c-b0bf-81ebe04cb549 | -22.74365 | -46.29689 | 2025-09-16 04:34:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24bfee93-53a8-3a12-bad7-91bbe305448a | -22.08315 | -46.65784 | 2025-09-16 04:34:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 43bebcba-e578-33c4-b831-5b674eec24bb | -22.71185 | -43.23411 | 2025-09-16 04:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04abc29e-43a1-35fe-b6f1-e6f0b636843d | -22.98391 | -49.9552 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 573153b4-f7db-330d-88ab-eff8ac05edf3 | -22.465 | -45.21128 | 2025-09-16 04:34:00 | NPP-375D | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 32932467-8639-39a0-ba0b-e28a55bf82b4 | -23.44337 | -47.67316 | 2025-09-16 04:34:00 | NPP-375D | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7ae8d355-698e-378d-a006-7fd045c5764f | -22.98509 | -49.94768 | 2025-09-16 04:34:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 21165804-6785-3cc9-a1f5-0a11978b497a | -22.5708 | -46.6707 | 2025-09-16 04:34:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 73ca6246-51bb-3a43-882f-4b0549b4fe55 | -23.25165 | -48.2797 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 16e128fa-06b8-391a-9039-61d39873d25b | -22.3341 | -46.5279 | 2025-09-16 04:34:00 | NPP-375D | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5890aba1-0033-306d-bcd9-8a94a8c74316 | -22.26721 | -45.57827 | 2025-09-16 04:34:00 | NPP-375D | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f3394bd0-ee2b-3b89-b05b-df7837b0c682 | -23.05015 | -47.30511 | 2025-09-16 04:34:00 | NPP-375D | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5f7ab8a-703f-3e81-9399-ebeefa13c54e | -22.36215 | -48.75873 | 2025-09-16 04:34:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 012f44dd-3306-3402-83e0-921202adf2c0 | -23.25733 | -48.28897 | 2025-09-16 04:34:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README60.md)
