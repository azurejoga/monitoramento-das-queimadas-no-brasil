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
| 4eec6c1c-1c6d-3586-9dcd-3dd5fba932c2 | -17.38793 | -42.65929 | 2025-02-25 04:10:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b32350d-79d0-312a-ba96-fbf93ebada4c | -12.55625 | -44.74178 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34a0a6a1-ec2e-356a-bacb-b3f1685d039c | -19.68128 | -44.05029 | 2025-02-25 04:10:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40a3961c-19ff-35ea-a9d6-6a071d2c23c6 | -16.35 | -43.69737 | 2025-02-25 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65755c6c-a01a-38bd-a278-0e922bd26323 | -15.58229 | -44.94708 | 2025-02-25 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9735e4c1-ba39-399b-8d6a-76ed34fc01a8 | -12.55286 | -44.74121 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7441694b-7caf-3f24-b5a7-b4a82fac6dad | -12.66798 | -44.50893 | 2025-02-25 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184a7e56-ee8d-3f23-894a-22dceb122e28 | -12.86867 | -44.83547 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a978bb00-7717-31fb-bc38-759467247542 | -17.78053 | -42.80227 | 2025-02-25 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64f5b449-ab1a-3b94-a91e-4c79414ce516 | -13.40727 | -43.02677 | 2025-02-25 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64e4ab6e-d621-3794-8b8c-d6032db7eec4 | -14.83461 | -45.19305 | 2025-02-25 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1740a94-431d-3ec2-b3de-7427b1f57576 | -19.96871 | -44.21532 | 2025-02-25 04:10:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9cfb8d2a-b5eb-3384-bece-9b2b4d91b8e5 | -12.55926 | -44.72311 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 692b81b5-0304-372d-8f70-65ecf56a88d9 | -17.78279 | -42.81026 | 2025-02-25 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bde1b17-5af9-3c4b-98ca-439ab641f792 | -12.55467 | -44.73 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cebbc460-dfe4-346c-9cbb-04207483bed8 | -15.89074 | -43.45623 | 2025-02-25 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 25b5637a-a57e-30f4-a7ca-0303ebaa9b4b | -12.55406 | -44.73374 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 238cf09c-502d-3aba-92bd-2108a2c86686 | -15.88963 | -43.46337 | 2025-02-25 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6993cc33-add3-3fbc-a161-9eeb7c1c63c7 | -12.5569 | -44.673 | 2025-02-25 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 370f6ca2-2080-3f0e-95fa-d4fc5e06543b | -12.55587 | -44.72254 | 2025-02-25 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 918f10aa-ec84-360c-96c0-166506076716 | -20.01929 | -45.60196 | 2025-02-25 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89ff754a-9321-36bc-84b4-51ea1369a4c3 | -20.01597 | -45.60136 | 2025-02-25 04:12:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2df68f0-adf9-32f3-b037-1fe18772c7f8 | -23.59314 | -47.44029 | 2025-02-25 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 51ffe858-d951-3f60-9c0a-14a62d366713 | -22.89297 | -42.71566 | 2025-02-25 04:12:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 026c2aee-605d-34d0-a393-44d38c46ea81 | -22.46383 | -42.66127 | 2025-02-25 04:12:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00bc13c0-1ec2-35dc-b7cc-e7a94d04b470 | -23.0154 | -45.02409 | 2025-02-25 04:12:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0746b956-0bc4-378f-8ea2-42388ca8d6a0 | -22.53984 | -48.81388 | 2025-02-25 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aabe3022-3320-3340-9e0f-c3a3f2ccdfa0 | -20.43854 | -44.09815 | 2025-02-25 04:12:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 163fb747-b894-397e-81ed-b3da0380082b | -20.37607 | -45.60452 | 2025-02-25 04:12:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03cd1455-a3fe-3d05-bc7e-582d9257eae9 | -23.40562 | -46.55733 | 2025-02-25 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| baebee1d-ad50-3a18-99a1-8e7f405ad07e | -21.86705 | -43.08049 | 2025-02-25 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 363e0449-119f-3717-aa0f-f4c7beda4c7d | -21.56251 | -45.76306 | 2025-02-25 04:12:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b782e856-fab2-3d0a-8f49-323a342e6ea3 | -23.98422 | -48.91859 | 2025-02-25 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dfb8347-44b9-37f8-bd93-6cf10fbba22d | -21.317 | -44.21962 | 2025-02-25 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0769adf-8b3f-33fd-8fad-ac970ee403fe | -22.74889 | -43.27441 | 2025-02-25 04:12:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00325ee9-f38f-3f6f-ab62-1681be44c0c6 | -22.70691 | -43.63766 | 2025-02-25 04:12:00 | NOAA-21 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca796f73-a580-32ad-80c2-96e05e1dfe02 | -23.63106 | -46.4272 | 2025-02-25 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eb5b6840-3150-33a0-bb20-94b24e8f2020 | -22.7873 | -43.75863 | 2025-02-25 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e2dd843-9bf7-38f1-a63e-8474d99f114c | -21.18311 | -44.27297 | 2025-02-25 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79417be2-32cb-3c85-a65b-f84207414c30 | -20.5502 | -45.93737 | 2025-02-25 04:12:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41f8062d-b61e-3cd5-bdbe-64b56a42f41c | -22.89649 | -42.71616 | 2025-02-25 04:12:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c03bb6b9-2863-30f9-a4cf-75bd04219eba | -22.90306 | -43.75708 | 2025-02-25 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b1389c53-8c78-30a0-9c27-8dfc1070d1d1 | -21.8285 | -44.4972 | 2025-02-25 04:12:00 | NOAA-21 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d3a72b73-1fc2-3ccb-bce0-74ceead42cd7 | -20.31178 | -45.58146 | 2025-02-25 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f6088d8-0efc-3c6e-84ea-6e88e0d94728 | -23.34039 | -46.77407 | 2025-02-25 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b30f868-ba8f-35ee-88ae-f431bb09ccfc | -20.54749 | -45.93298 | 2025-02-25 04:12:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 740f5fcd-c6fa-3d09-93c9-251d62dd44a6 | -20.98549 | -43.03248 | 2025-02-25 04:12:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e3180338-e0d6-34b9-8a09-77595d1f4c47 | -20.54687 | -45.93676 | 2025-02-25 04:12:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea961737-fae8-3380-aa0f-9de8954f05f1 | -22.81943 | -43.34248 | 2025-02-25 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b1ea5cf-e133-378f-a528-be39fc67bfcb | -21.87105 | -43.07702 | 2025-02-25 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18099821-085c-346c-b4a1-a05e2215b11e | -21.87162 | -43.07301 | 2025-02-25 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d933e6fe-b32f-3e50-8091-96beab1a056e | -21.19621 | -44.9389 | 2025-02-25 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15180ca6-20be-3ea5-9d37-26ea7442dbdf | -22.89591 | -42.72039 | 2025-02-25 04:12:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8f9046a3-71b4-34be-9dbc-4c40f652e3aa | -20.54416 | -45.93236 | 2025-02-25 04:12:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba006cdb-144d-3043-986b-8dc4952e0796 | -21.86761 | -43.07648 | 2025-02-25 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2049d07b-8886-3257-a1db-b041bfe44806 | -21.86819 | -43.07246 | 2025-02-25 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21bfb728-1cd1-3da8-840d-bff8924d8630 | -28.58955 | -49.44303 | 2025-02-25 04:14:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3fe11661-72a0-3808-8aea-f283f8fc3bf0 | -28.89932 | -50.89499 | 2025-02-25 04:14:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3595718e-ad96-39c1-9a97-a8b9e1b5eba3 | -25.6169 | -49.35111 | 2025-02-25 04:14:00 | NOAA-21 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8997db30-0921-3ff3-b04c-28b4bf0d8f8b | -30.15044 | -51.87837 | 2025-02-25 04:14:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| c2b9b7e7-cdca-39b3-aee1-3b0a1e2173af | -15.8949 | -43.4766 | 2025-02-25 04:20:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0c72b993-5d3f-3ab4-9c20-a036d6ddcce7 | 2.7249 | -61.2627 | 2025-02-25 04:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 554441a1-862e-3cd9-b826-febb8d6b6f9e | 2.7431 | -61.2813 | 2025-02-25 04:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 72eb326d-5942-363e-baf2-29eb99c1111b | 2.7432 | -61.2624 | 2025-02-25 04:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0392b489-833d-38e9-9849-79d29bf2d461 | 2.7249 | -61.2816 | 2025-02-25 04:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1139fd85-96b4-3205-a25f-57a5866f56ac | -15.8955 | -43.4523 | 2025-02-25 04:20:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 168.2 |
| c7ae0bb5-c908-3423-9841-6f20bf892af0 | -15.8757 | -43.4566 | 2025-02-25 04:20:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 73561b37-794e-3ecc-bff6-105794ac2130 | -15.8949 | -43.4766 | 2025-02-25 04:30:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fbea1159-74ae-3831-812b-df265f94ea99 | 2.7432 | -61.2624 | 2025-02-25 04:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 36ce3f45-ee1d-36d1-b2c6-b3fe9be31ce9 | -15.8757 | -43.4566 | 2025-02-25 04:30:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 99906526-9bf0-3957-8e55-80e9128646fb | 2.7249 | -61.2816 | 2025-02-25 04:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 59705820-3690-3836-82d2-188f30adb67d | -15.8955 | -43.4523 | 2025-02-25 04:30:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 6cbeda5f-9cae-38c9-8c7c-9085eefb73f6 | 2.7249 | -61.2627 | 2025-02-25 04:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| abd4873c-fd23-3b48-b86f-1db05c97c936 | 2.7431 | -61.2813 | 2025-02-25 04:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a85fe2c7-768b-3705-9842-2705b0ce1ee2 | -7.0755 | -35.11068 | 2025-02-25 04:31:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 95f6c148-5a8f-33da-b233-30b81118888f | -2.79813 | -54.14752 | 2025-02-25 04:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4d1c692-d01b-352b-879e-2fb3cdb0e86c | -7.07679 | -35.10959 | 2025-02-25 04:31:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b38b8dcb-66cb-3c02-b0d2-53665dd3e2b0 | -8.06736 | -34.97503 | 2025-02-25 04:31:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a20326d2-afa3-347e-9585-892052f0f027 | -7.07639 | -35.10399 | 2025-02-25 04:31:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ba2547da-089d-3f17-a777-51f39e2d3b61 | -7.07764 | -35.10291 | 2025-02-25 04:31:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c3db07b1-81c7-32eb-ae3a-75b8f704801c | -8.94104 | -44.24046 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a969cebb-326e-383e-b86a-80a89f1023c8 | -10.989 | -45.09515 | 2025-02-25 04:33:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58d35bb8-e4f1-36ca-b292-cc262a70deb4 | -8.37473 | -43.96897 | 2025-02-25 04:33:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e71a31b-2692-360e-a2cd-73e88fdff911 | -8.11496 | -43.1376 | 2025-02-25 04:33:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fa682453-c079-3597-886c-256573afc69f | -13.29436 | -44.62874 | 2025-02-25 04:33:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae80f3e3-4643-34e0-bf58-406d454f7035 | -13.29673 | -44.62518 | 2025-02-25 04:33:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf0840ba-7695-347c-b0d2-99d3b79c14dd | -8.11442 | -43.14122 | 2025-02-25 04:33:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 42987788-4d13-3732-8e7c-af566befeac6 | -12.55716 | -44.73798 | 2025-02-25 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea3324dc-018d-3e6c-8995-96847ee1302a | -8.72721 | -44.01596 | 2025-02-25 04:33:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 659f09b0-dfb8-3ae5-8568-b2067f37decc | -12.55141 | -44.72161 | 2025-02-25 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63a116fc-c899-38ab-bcce-92f1e36e8615 | -8.94248 | -44.23761 | 2025-02-25 04:33:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0280652-cf92-300b-8d11-ccef0518d5bf | -8.14055 | -44.46372 | 2025-02-25 04:33:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a538c3e5-8cee-3445-a9d6-fea90ab2f0a9 | -10.52931 | -42.43988 | 2025-02-25 04:33:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce391301-4f33-3688-9290-308a688b81ce | -12.55927 | -44.72277 | 2025-02-25 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ee2cfe8-cbd9-3cfb-b23f-6075853d2b27 | -8.1411 | -44.46152 | 2025-02-25 04:33:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8219026c-11c0-3dbf-9c13-54c5945900ab | -9.40675 | -40.3117 | 2025-02-25 04:33:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3df54669-84a3-3655-b8d9-c2c93f9510a8 | -13.29511 | -44.62345 | 2025-02-25 04:33:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e22a8d-1198-3945-a4e5-cb8eed4f924f | -12.55323 | -44.73739 | 2025-02-25 04:33:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2b63cf9-4e66-34c3-b53f-9d6a8316baac | -7.05947 | -44.35117 | 2025-02-25 04:33:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8ba9d58-8b2c-3792-a4a5-f4889dd12f66 | -9.40636 | -40.31464 | 2025-02-25 04:33:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README4.md)
