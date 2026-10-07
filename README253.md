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

## Dados Diários - Página 253

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef68011a-24c7-3cfc-9b33-381d44b5eec5 | -11.619 | -43.6196 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3b97f2f0-4cb1-3b21-97cf-0213e6fbc4b9 | -5.9584 | -43.5072 | 2026-10-07 18:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2021e541-c3fb-37de-8307-1dfa10b00dbd | -6.3353 | -43.3365 | 2026-10-07 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 67a149b1-e1ed-3b8f-98e6-0f9531cecf1b | -5.9649 | -40.914 | 2026-10-07 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 159.7 |
| 75ba7224-8cb9-3635-8086-cf3c3dde01cf | -5.0325 | -49.7687 | 2026-10-07 18:50:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1cb53a9f-eba5-3dba-abb5-6e5b1f3b0865 | -1.801 | -57.1161 | 2026-10-07 18:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 054933d4-0b92-35ca-8f56-d1c302fb08fd | -6.3165 | -43.3381 | 2026-10-07 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8f5aac90-840e-3145-8329-45542ee3cbf0 | -11.6946 | -43.6787 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1e2a7cd5-a40a-39ab-b653-730c9e0c717e | -1.8011 | -57.0967 | 2026-10-07 18:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a5aca927-f273-3ec4-ad44-ec391357e987 | -3.5311 | -54.6357 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| a1bd6b16-26d2-3859-aace-37d934912772 | -3.4763 | -50.0673 | 2026-10-07 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 35099620-2c6f-36dc-9d66-c4259ee82876 | -3.5873 | -54.3739 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 92fa5454-f993-3941-9c4f-6c86ef34baf8 | -9.1362 | -65.3022 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 73c5d59a-ad3c-3f5f-ad7b-4e3351354b57 | -5.5148 | -42.8164 | 2026-10-07 18:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| ac84c8a5-9edd-3f05-89d4-6bb5de268eac | -6.9925 | -45.1223 | 2026-10-07 18:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f2ea7b80-89b6-3687-9f99-2aa3e49d7b47 | -5.496 | -42.8178 | 2026-10-07 18:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 6422792f-ebbf-3aad-9f49-7560df593c4a | -8.5552 | -67.0315 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 4358d854-dc70-3e74-8a4c-2963937676c1 | -3.2398 | -53.8813 | 2026-10-07 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9b1f781b-0ea2-3d8b-b864-ca072a66c6aa | -3.2137 | -42.953 | 2026-10-07 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 343.3 |
| fe4c43b9-877b-313d-b2ee-030a955269cf | -5.2473 | -50.9149 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 0d8fe9fc-bbdd-385c-abdf-9ae9f6f2edb9 | -2.1361 | -54.4671 | 2026-10-07 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9e9e4b83-be24-3fdc-9472-25633d1dcfbe | -11.8127 | -43.5184 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a302684d-55eb-3b84-8db5-5b001966398d | 1.7121 | -55.6261 | 2026-10-07 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8166ac8c-677a-314f-82b7-dae6e90b9ec2 | -9.5468 | -64.8196 | 2026-10-07 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| ac5721cf-26e2-32c4-9f1d-578cec7a0861 | -6.5794 | -41.5841 | 2026-10-07 18:50:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 29676da0-deef-37e8-821a-20f467329a60 | -9.9589 | -43.5516 | 2026-10-07 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| c31a2863-3765-3a1f-956f-7c5b81a6167a | -3.55 | -54.4952 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e2c1812c-2c28-3b4f-84b1-684e08c5b2a4 | -2.8411 | -58.3414 | 2026-10-07 18:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c520e70a-c9db-302c-b750-e815bd733b0b | -7.3085 | -73.0269 | 2026-10-07 18:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e425e10e-38e3-3ce5-99b3-b7d8ab89cb86 | -11.7335 | -43.649 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7049bb42-3b42-3859-b22b-cff465a75f7f | -9.8061 | -64.9979 | 2026-10-07 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d4b82d51-bb4e-38e6-9880-167e68f51377 | -9.1363 | -65.2835 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8ce64ea4-f270-3740-8750-eca028299100 | -7.9178 | -70.9245 | 2026-10-07 18:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 113.1 |
| ba0f63e7-39ea-37e6-af9d-45e7da581c0d | -5.9647 | -40.9383 | 2026-10-07 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 246.4 |
| 9f004a26-b1e5-3d68-9b72-b5e1109703d5 | -6.1431 | -52.6481 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| dd0c1149-7f9f-34f8-bc72-698acf24d231 | -8.5368 | -67.0135 | 2026-10-07 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 56eef5aa-de2f-32cb-b553-99319d27a452 | -3.5127 | -54.6562 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 28e3e180-471e-31b1-b398-fea423074b59 | -9.9787 | -43.502 | 2026-10-07 18:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 212.9 |
| ab68d20c-438d-3b83-aa09-fce801adaaa1 | -1.1094 | -54.1601 | 2026-10-07 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 1efef22b-64a9-361f-bebd-3df5e899524b | -13.3865 | -43.8708 | 2026-10-07 18:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 91b8c5ab-77a2-3f54-abac-82afba3b2d6e | -4.0947 | -52.0635 | 2026-10-07 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 4fc4aa19-da49-3f3e-97cd-ab4efc46f43d | -6.3351 | -43.3598 | 2026-10-07 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a00cb14b-381b-33e6-a7c2-5d21ea1c3373 | -6.1615 | -52.6676 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 10f60454-fc85-3e7a-b4af-ff27a25f9c50 | -3.5127 | -54.6362 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 5220acf6-6a11-3f11-8696-03f664fa9277 | -11.6181 | -43.6669 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| cd07eb69-7130-3fc8-9bf9-ec9bfb70b896 | -5.9772 | -43.5057 | 2026-10-07 18:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 218.6 |
| babaedae-400b-3b67-85c9-f39f1c642cb0 | -3.8037 | -47.4839 | 2026-10-07 18:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0501b19e-941b-3e1e-b7f5-784e86637fa3 | -8.9082 | -49.986 | 2026-10-07 18:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 00b5f972-267d-36a3-b267-d6b94cd90eca | -7.6802 | -70.0677 | 2026-10-07 18:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 9f6a27c7-35a3-3ce8-893d-5ee2136950b2 | -3.476 | -54.6172 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 34653a0e-4b42-3e4c-bef0-ac9e013995dc | -3.195 | -42.9772 | 2026-10-07 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 3f1764c9-d9a4-386a-8206-cf16e0529990 | -5.7659 | -42.0389 | 2026-10-07 18:50:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 136.2 |
| 33b76d3f-0a73-376b-814a-c7b758eb81e5 | -11.8503 | -43.5598 | 2026-10-07 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 56014d25-f346-37ab-a791-0af428b83822 | -3.7301 | -55.4662 | 2026-10-07 18:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a397dacd-dcbf-3b16-85b1-92742478d36a | -16.0101 | -43.5966 | 2026-10-07 18:50:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a265b20e-bf70-38a8-9139-fd35448447d9 | -3.1951 | -42.9538 | 2026-10-07 18:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 3865d2d1-a6dd-3be2-82be-b026b165c3a0 | -2.8411 | -58.3607 | 2026-10-07 18:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ef284b36-15fd-32f4-ab08-938bc0227082 | -9.3395 | -65.4451 | 2026-10-07 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 88103a07-c99f-30f2-9de9-c0b825ec1720 | -6.5852 | -53.0331 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 3c7b287b-dee3-3d87-9426-f4482ad694d6 | 1.8768 | -55.7227 | 2026-10-07 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 4275f397-01c1-3a29-8da2-27d57e11edfe | -1.1278 | -54.1199 | 2026-10-07 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 093dfc0f-effb-396d-a664-613cf85c812a | -6.6599 | -52.9675 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 0346bee5-a1b6-3be4-a331-56efb20cc58d | -6.1937 | -42.4785 | 2026-10-07 18:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 182.0 |
| d5e23219-9640-32b0-a345-516a1183bca1 | -6.6037 | -53.0321 | 2026-10-07 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 01ac124b-7f60-3551-9a77-afedaf04ad1f | -3.5862 | -54.6541 | 2026-10-07 18:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 433.6 |
| 5dcde9b4-a517-31ea-a3d3-e3936dc28d63 | -12.8312 | -45.5739 | 2026-10-07 19:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ccc3659c-319a-3e5c-b64b-64f590284446 | -4.2657 | -54.8729 | 2026-10-07 19:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ef8e62ca-932c-3aa7-9552-2929a516020e | -3.203 | -53.8823 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| db3e46f6-253a-34e0-9039-3206a7e59b19 | -3.7872 | -50.7483 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 862dc8c6-8087-30a2-b9f9-a83ed82b5da3 | -6.6039 | -53.0116 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 9d1ccef0-2691-36f2-a715-69ce2012c29c | -9.3381 | -65.7442 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8fcd7a07-da34-3544-bcb4-f4e18af88ac8 | -3.295 | -53.8597 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 468437d2-dfbc-3a65-8c0f-c77951c01ba9 | -3.269 | -51.0575 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 262.5 |
| 33e61982-2886-34a9-a0a7-7417902c9358 | -5.9584 | -43.5072 | 2026-10-07 19:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8fd47f7a-0893-3a3a-82d1-f08439fbd3b8 | -3.1788 | -50.5388 | 2026-10-07 19:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d2fa9569-5ed1-3f38-b78f-2c9e7a267923 | -6.6224 | -53.0105 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 5a17ae6d-4313-3ef5-bce9-f7a6ea6a93f2 | -3.328 | -50.1775 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1572019e-f8ba-3b9c-8bff-26acd2a2d873 | -7.3996 | -45.6523 | 2026-10-07 19:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 454b4577-e325-3c59-918e-24548b1a1ee6 | -3.2136 | -42.9764 | 2026-10-07 19:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 5932b8a0-17ac-3931-a2f0-0104264b6149 | -3.7654 | -44.3611 | 2026-10-07 19:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3a6b4dd7-bf3b-36b6-9234-92e78a56b1a8 | -9.9601 | -45.9712 | 2026-10-07 19:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 97f76839-a7dd-3e9d-a6de-563e02fac893 | -3.8973 | -44.1255 | 2026-10-07 19:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| acf9aebd-2277-3b29-95b6-9575fa0840d4 | -11.6181 | -43.6669 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 81576eeb-6289-377a-9aeb-cfae847debcf | -3.3134 | -53.8592 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 9022c6eb-9d09-3af5-b9af-b55a1f76bed1 | -11.6177 | -43.6906 | 2026-10-07 19:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 404740b2-b541-34af-ae77-09a9556a2925 | -3.5876 | -54.2937 | 2026-10-07 19:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7fb6ef93-1e35-3fa1-9e55-2e19b2571404 | -4.1223 | -54.0158 | 2026-10-07 19:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 256401e3-31fd-362c-96aa-6b3cb8a29f4f | -5.839 | -53.8246 | 2026-10-07 19:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 27b67ad0-fd2a-3d35-80f0-83ca63f22643 | -12.1436 | -43.2992 | 2026-10-07 19:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f1974c22-0c6c-3f5f-820b-dd53d1cd9d2e | -4.3045 | -50.77 | 2026-10-07 19:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c5ee2c33-ea87-328c-a668-13bb029779ea | -5.372 | -44.1751 | 2026-10-07 19:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| e61f7242-f2df-3a8e-bb33-95529304f341 | -3.4762 | -50.0883 | 2026-10-07 19:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 1e393f87-21b3-32a0-b3fc-afc547a6a6dc | -7.6583 | -72.3144 | 2026-10-07 19:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 98.5 |
| ddce5998-a1a3-33ef-bb42-be3b065bbe86 | -9.3394 | -65.4638 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2bb841e8-bb59-30ec-b3de-bc929601b242 | -6.8952 | -43.6833 | 2026-10-07 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 540.2 |
| b6e66d8b-6770-3caa-9693-85105592687e | -6.914 | -43.6816 | 2026-10-07 19:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e908b36b-93e2-3bd3-a629-ae249a9fe6f0 | -4.3044 | -50.7909 | 2026-10-07 19:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ef5c6874-d1b2-3f53-9425-1e8738ac811b | -3.6197 | -55.5089 | 2026-10-07 19:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5b3c5aa2-436b-3389-888c-fd7d210cddbb | -6.5852 | -53.0331 | 2026-10-07 19:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 7cd29f8d-135d-36f8-885d-8b3b75934a19 | -9.3566 | -65.7436 | 2026-10-07 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |


[Clique aqui para ver as próximas entradas](README254.md)
