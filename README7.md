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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ea68a87-a817-390d-add0-2a627ce1663f | -10.7524 | -46.185501 | 2024-10-05 00:22:36 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c441833a-880d-3bde-b5e3-3bcdfee01b22 | -10.7151 | -47.710899 | 2024-10-05 00:22:42 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8abf816-52d3-37b4-bfaf-d98e7a688a31 | -10.7178 | -47.723701 | 2024-10-05 00:22:42 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c66a061-9eb8-3023-99aa-e22b69166bb9 | -10.7054 | -47.712898 | 2024-10-05 00:22:42 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdaf9754-8f9d-386a-86b0-38490b4728d0 | -10.7081 | -47.7257 | 2024-10-05 00:22:42 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf3c075c-21a7-3723-b705-1b409b6e7442 | -10.5896 | -48.0383 | 2024-10-05 00:22:45 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 887e5eb7-e709-39c3-8348-eb3a860f893d | -10.5924 | -48.051701 | 2024-10-05 00:22:45 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 475a537d-ee2c-349e-9b30-49ed66ecb9e8 | -8.9718 | -40.8377 | 2024-10-05 00:22:46 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9a2fbe2d-ee61-30e0-b2e3-9eac4fc8db06 | -8.9734 | -40.844799 | 2024-10-05 00:22:46 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f9ccf28d-418f-3d61-9474-d851ddf9f366 | -8.9751 | -40.851799 | 2024-10-05 00:22:46 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 49aec3a8-fc1b-3cf3-a1b2-320a1693250e | -10.1308 | -46.338799 | 2024-10-05 00:22:47 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a546dde3-e787-3f20-9ed5-5937a6335f78 | -10.133 | -46.349098 | 2024-10-05 00:22:47 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52ee87e5-bdd1-3a32-bb2f-a4405a9faece | -8.6894 | -40.8657 | 2024-10-05 00:22:50 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2c0c4a1e-4952-366b-8207-941f94379625 | -8.691 | -40.8727 | 2024-10-05 00:22:50 | METOP-C | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 867c5612-be26-322c-9e21-08672fd67f7a | -10.2325 | -47.691601 | 2024-10-05 00:22:50 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dab42159-1ab0-3da0-849b-99a2eda0cdd4 | -10.2351 | -47.704201 | 2024-10-05 00:22:50 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c457b34-95c4-3196-b4bc-ca15076d6dd8 | -9.2315 | -43.483299 | 2024-10-05 00:22:51 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e91f715-f496-3862-814c-7a52e18b62a2 | -9.2577 | -43.5084 | 2024-10-05 00:22:51 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64880ff8-9b3d-3586-afb3-cf20e753e0d2 | -9.2479 | -43.510502 | 2024-10-05 00:22:51 | METOP-C | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e78074c5-a435-3953-afbb-b7540b717750 | -8.7185 | -41.576302 | 2024-10-05 00:22:52 | METOP-C | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4709e069-c508-3d83-939f-3a683491068d | -8.7201 | -41.583199 | 2024-10-05 00:22:52 | METOP-C | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d998653-ab0a-3a69-a2b9-24419c43bac8 | -9.8339 | -46.720299 | 2024-10-05 00:22:53 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0a25538-16a6-3dc4-9bc9-7ec5134ba522 | -8.3329 | -41.153702 | 2024-10-05 00:22:57 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c290f48-b475-3ca8-8cd1-02c14202dc42 | -8.3231 | -41.155998 | 2024-10-05 00:22:57 | METOP-C | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ee7f520-cdc9-34bf-bad7-ee835cf2ed79 | -8.3247 | -41.162899 | 2024-10-05 00:22:57 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8691fe92-cb44-3fa6-8271-2ca107ce410e | -8.1493 | -41.341999 | 2024-10-05 00:23:01 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a666cf44-9545-3d68-9b37-c6f84c8e48b2 | -8.1509 | -41.3489 | 2024-10-05 00:23:01 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9cb68dbe-ecc0-3103-9cf6-17a93e55c20c | -8.9946 | -45.2029 | 2024-10-05 00:23:01 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8095b6a-4d9d-37bf-958d-7c002f651ecd | -8.6417 | -44.0676 | 2024-10-05 00:23:03 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34b8912e-1330-3257-b9c7-432fdfe1d1db | -8.6434 | -44.0751 | 2024-10-05 00:23:03 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b2da0dc-bcee-326b-88d5-2cb8729c2975 | -8.6319 | -44.069698 | 2024-10-05 00:23:03 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e5ffb15-f63b-3292-bc72-1b58f7259365 | -8.6336 | -44.077301 | 2024-10-05 00:23:03 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9d18cef-96e6-3f95-8f45-7aede34befd6 | -8.764 | -44.8064 | 2024-10-05 00:23:03 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b034f4bf-e3ad-3670-b445-fe75751f621f | -8.7658 | -44.814602 | 2024-10-05 00:23:03 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 439d993f-52b3-3bc2-b320-b4af61f18fa8 | -8.7676 | -44.8228 | 2024-10-05 00:23:03 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1720e53a-cec7-3435-98ba-91fa169c88e6 | -7.8973 | -41.1432 | 2024-10-05 00:23:04 | METOP-C | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 14a81165-be56-3f56-badd-a766c1f838d0 | -8.5616 | -44.077301 | 2024-10-05 00:23:04 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66fb7323-c3d3-3845-8d2a-75a3a885a118 | -8.5633 | -44.0849 | 2024-10-05 00:23:04 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e74f53b7-2bc5-30f8-82f1-a86937c1f42f | -8.565 | -44.0924 | 2024-10-05 00:23:04 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7e934c2-34cb-3b63-8a5d-57931eb6cc3d | -8.5535 | -44.087002 | 2024-10-05 00:23:04 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c399831e-3e72-3083-94b7-e011dc115710 | -8.3609 | -43.638 | 2024-10-05 00:23:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80282c95-27e8-3ae6-85af-682b61c3817c | -8.3625 | -43.645302 | 2024-10-05 00:23:06 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df182858-959c-3a76-93f3-e9af90d00d6e | -8.3641 | -43.652599 | 2024-10-05 00:23:06 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8df7f9c3-83b7-3284-ba55-41a25f664066 | -8.3658 | -43.659901 | 2024-10-05 00:23:06 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7849b072-5a1a-3834-8e4b-34d3c1a9a430 | -7.9398 | -42.4557 | 2024-10-05 00:23:08 | METOP-C | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 376234fc-5731-3e81-8b7f-f101a5529e2d | -8.7361 | -46.797901 | 2024-10-05 00:23:11 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53ac2d61-47f8-3d70-9cef-f2c1b0a1f2aa | -8.152 | -44.4081 | 2024-10-05 00:23:12 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 720993cf-0729-3c01-89ca-e455dc2dc8c8 | -8.5972 | -46.4855 | 2024-10-05 00:23:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f76d84c-4fd8-363d-a1ed-639cf6b33074 | -8.5993 | -46.495499 | 2024-10-05 00:23:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59a90c3b-a426-332b-9ef3-9ea74b40297e | -8.5874 | -46.487598 | 2024-10-05 00:23:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3d9ee7e-10c2-3f4d-8901-84735e96926f | -8.5895 | -46.497601 | 2024-10-05 00:23:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| baeede99-0aaf-3f31-b730-b58371f5ebcf | -8.5797 | -46.499699 | 2024-10-05 00:23:12 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 618b605b-b7d1-3136-9c59-67dd5f8feb0f | -7.6238 | -42.425201 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ccb772e-49d6-36bf-aa72-a816152cb2cf | -7.6419 | -42.413898 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e163120-afd7-35f6-83f1-f538457d67c1 | -7.7864 | -43.097099 | 2024-10-05 00:23:13 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f44f972-ae4b-3b92-a3bc-5336e0f15485 | -7.788 | -43.104099 | 2024-10-05 00:23:13 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad0b6fcf-dc2d-3ab5-b4aa-4277286b9471 | -7.7896 | -43.111099 | 2024-10-05 00:23:13 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0aba799c-7a2a-3975-8323-9d9cb529a994 | -7.6223 | -42.418301 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3893eff9-045b-393c-acbb-0bb542f246a7 | -7.6172 | -42.441299 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 09ba8b32-81eb-3f3c-a4e4-14dc330c058e | -7.625 | -42.4757 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b91fdb93-151b-3547-b88d-c8b61d546b2f | -7.6266 | -42.482601 | 2024-10-05 00:23:13 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b23f7ece-dae5-3230-957a-15d1bf8d2ef9 | -7.7589 | -43.066299 | 2024-10-05 00:23:13 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e551592d-4547-3beb-a955-cbe8ef077f8d | -8.8553 | -48.3144 | 2024-10-05 00:23:14 | METOP-C | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf2d5569-b064-3e99-92a2-e3dfb9b2266c | -8.858 | -48.327599 | 2024-10-05 00:23:14 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f36762e2-39c7-3715-aa46-1c41c81289c4 | -8.4091 | -46.2794 | 2024-10-05 00:23:14 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea9d6bba-aff4-34c5-84dc-d6c1760ec044 | -7.7443 | -43.047401 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37e0ec7b-1388-3e9d-a74a-2e40702fa5d9 | -7.7459 | -43.054501 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f391c312-9100-3836-9694-9715b87e704d | -7.7491 | -43.068501 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79063624-9bc1-36d0-affa-fa4af9a8bc32 | -7.7507 | -43.0755 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6388dbc7-b72d-3473-b584-7998d55437ff | -7.7361 | -43.056702 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4b108b4-f8f7-3fbe-b6fa-0849a9bac895 | -7.7377 | -43.063702 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 54aaf28a-b317-38ef-9e86-40a017a1cca9 | -7.7393 | -43.070702 | 2024-10-05 00:23:14 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53306cc0-786a-389a-8cd2-37c2efefd42e | -7.6959 | -42.970001 | 2024-10-05 00:23:14 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2339b4bc-afb2-357c-bcb3-e5c3310c5e12 | -7.6975 | -42.977001 | 2024-10-05 00:23:14 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75dc6148-f83d-3e7e-9aec-077a172f34be | -7.6877 | -42.979198 | 2024-10-05 00:23:14 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 242c4607-85c6-3b2f-8d62-0e710250d2dc | -8.3916 | -46.293301 | 2024-10-05 00:23:15 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ead7659a-f748-30fb-8db4-6be61a9f2282 | -8.3819 | -46.295399 | 2024-10-05 00:23:15 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7320c865-5a8d-30ad-ad46-bfc8e07bb47a | -8.384 | -46.305 | 2024-10-05 00:23:15 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5adf59ae-15ab-3d63-8cc5-1826a8600aa9 | -8.4868 | -47.303101 | 2024-10-05 00:23:17 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f51f98d-f616-30f8-b16a-1a68221ac899 | -8.9708 | -49.788898 | 2024-10-05 00:23:17 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88d7db5a-0d4e-3149-8f65-d73524ef553c | -8.9743 | -49.805698 | 2024-10-05 00:23:17 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf085b7-7b82-35aa-b3c4-065c8275dc98 | -7.6224 | -43.694901 | 2024-10-05 00:23:18 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c1d3572-5f93-35c8-bf28-8c03f0273569 | -7.6241 | -43.702099 | 2024-10-05 00:23:18 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2390866e-73ff-361c-bb26-19f4063265b8 | -8.9611 | -49.790901 | 2024-10-05 00:23:18 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02981954-5aa2-340b-b5d1-c33d0e1ae7df | -8.9646 | -49.807701 | 2024-10-05 00:23:18 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba2799f3-433e-3f78-998d-35a5a0935e6a | -8.6511 | -49.0849 | 2024-10-05 00:23:20 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd5ce207-534a-35d8-9ee4-a284962d074d | -8.6383 | -49.072102 | 2024-10-05 00:23:20 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71eedccb-3769-30e8-8504-11fd12c21b41 | -8.6414 | -49.086899 | 2024-10-05 00:23:20 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f5d75b4-6d2f-37b1-b0cc-76543b95d752 | -8.6445 | -49.1017 | 2024-10-05 00:23:20 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5da61bae-7b4c-3a44-bd0f-a745f93eff71 | -8.7909 | -49.948799 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5974f7e-e2f9-3920-9db1-00aa6e0f6857 | -8.7777 | -49.9338 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b06d6126-da01-362c-9400-cbdc6909dd4f | -8.7812 | -49.950802 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbb150b-7a6e-3bac-bd27-2eebacfbdc9d | -8.7847 | -49.967899 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f89b7633-ce5b-323a-862d-b51c9a6eb8a4 | -8.768 | -49.935799 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6180fd62-34a7-35ae-a188-7573fc38b9ce | -8.7715 | -49.952801 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a95482-6114-3ec6-9a20-abb9746376c8 | -8.7582 | -49.937801 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d231be-1ad7-3265-a1a5-4f88b69c6014 | -8.7618 | -49.9548 | 2024-10-05 00:23:21 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0468f0-84d5-3df3-91e1-a9729b5feaee | -7.1183 | -42.604099 | 2024-10-05 00:23:22 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86b21d56-9b70-36ac-a8ef-b5f9b853957b | -7.1199 | -42.611 | 2024-10-05 00:23:22 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68248e59-e848-3adf-8927-296168ec9dbf | -7.7377 | -45.4133 | 2024-10-05 00:23:22 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
