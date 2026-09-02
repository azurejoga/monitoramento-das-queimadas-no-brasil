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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86414459-9a9b-3b6a-a2c0-12b8019807bb | -10.7428 | -50.8727 | 2026-09-02 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 51afc44e-e2be-350f-bf96-69331f9a1ffc | -11.315 | -50.5774 | 2026-09-02 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| cd163ccc-ca1f-362d-bc28-fce9f52dcd43 | -7.219 | -60.689 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e0aa4526-07b7-30e7-8a30-50a914d290cb | -9.6682 | -46.523 | 2026-09-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b61a1714-3a40-3c9c-a91f-2db51b76106c | -13.9664 | -58.6736 | 2026-09-02 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 290.5 |
| 887f9423-853a-30b8-acde-a5a0a487bfaf | -10.7242 | -50.8534 | 2026-09-02 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f3c75b56-63e4-38d3-8d71-5631a2f77292 | -9.4159 | -45.6271 | 2026-09-02 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7f2a2ce5-e2fa-3acd-b044-b63781fc7ca1 | -5.9635 | -57.6899 | 2026-09-02 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b99661fd-4582-3f10-9097-e685863d31af | -10.0815 | -46.7441 | 2026-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4c3c90ca-d64f-3558-9c19-e38920cee1c3 | -12.0933 | -47.1138 | 2026-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 8ff7b01f-1dff-3984-8bda-800fd0d76ecf | -10.6964 | -46.242 | 2026-09-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a94f79e8-fb2d-39b9-a237-1f71f62da850 | -9.139 | -51.1307 | 2026-09-02 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ac1e3712-35e5-38f7-b800-1ec932a29f28 | -6.8568 | -59.4757 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| eda5763b-e732-3a59-b66a-639fb4fab30a | -11.2857 | -45.1602 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3924c9a8-8a84-3c96-bda9-1d22ddcc3058 | -6.6764 | -58.7686 | 2026-09-02 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 62b3d0cf-fd8a-307d-ae33-a7c6b6968003 | -10.3196 | -50.0211 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 26e34a15-5e18-32ea-9da8-854db1616652 | -11.3771 | -45.4 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 331.4 |
| eda19526-0366-3968-bc6b-8154ab840670 | -8.446 | -62.6752 | 2026-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d9b04eef-83fb-36c5-8cb1-2f7f3eeba665 | -1.0182 | -53.7189 | 2026-09-02 14:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 323f1081-3870-3561-b73f-9ae4b58d1827 | -10.6967 | -46.2193 | 2026-09-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c38f5fd4-3bf9-3cec-8b99-7a6033586500 | -11.3579 | -45.4027 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| d8b57653-351d-3d19-b634-fd1435a16288 | -10.3007 | -50.023 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| a4c9d353-37a1-340f-9cc5-02927e86402f | -11.3431 | -45.1521 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 0e42d402-d17c-3184-a78e-99668ebf7e22 | -11.1824 | -50.5706 | 2026-09-02 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 60132e5b-1ae0-3d45-b8f2-8668dc4af1c5 | -8.7817 | -46.4623 | 2026-09-02 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 89f5ac37-5493-3de2-90b6-abb6a8984ac3 | -10.2209 | -50.3517 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a2904051-d73a-3ddf-8644-8fc497615b0d | -12.0936 | -47.0913 | 2026-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 163cfa01-29d7-3def-88e2-ed9c82f36de3 | -11.5479 | -45.4676 | 2026-09-02 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 25f3d8cf-4615-381b-a5f8-6b9e91b99367 | -6.7832 | -59.4401 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| dfdb2246-d99f-370e-a479-a58929314d8e | -10.3199 | -49.9996 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 175150ba-f895-36a0-bafe-45b2bc005616 | -11.3044 | -45.1805 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| bf126a7a-2582-3557-9bbc-1526dfddd1c4 | -10.442 | -46.7235 | 2026-09-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8bac87ad-bbcc-396b-8863-320b86a83a66 | -10.1008 | -46.7195 | 2026-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c6ae32c2-977a-321c-9716-95b464f9e946 | -17.0878 | -56.8534 | 2026-09-02 14:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| d94748bc-d060-3d25-acb0-c309a2123224 | -9.2144 | -47.99 | 2026-09-02 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| c3df186e-5c85-3900-97b5-b561a5a3ca14 | -8.4644 | -62.6934 | 2026-09-02 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d07ad85a-cbf4-3cc6-aa1a-b3d6cc74c7dc | -13.0708 | -45.1429 | 2026-09-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ec44274a-6d77-3c84-8b1b-32816dddc3ce | -6.6765 | -58.7492 | 2026-09-02 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| b904adf1-b615-3f53-b4fb-1fc63393028f | -9.139 | -51.1307 | 2026-09-02 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| de422bab-d225-3506-ae22-97d7a0709a7a | -10.1134 | -45.8621 | 2026-09-02 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 331c7fcf-3b23-3b0d-a01d-2414ba6f80c5 | -6.1413 | -55.6748 | 2026-09-02 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d47bd77d-79c2-3903-bbf5-ea3718db1a77 | -7.3486 | -60.6074 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 1fcbe7f6-9f9a-34d0-8b86-64c95d09efed | -11.1824 | -50.5706 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 822dce30-44e9-3b6c-bd3d-3d500564a8ff | -10.7009 | -47.1835 | 2026-09-02 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3f3b61cb-b044-3168-ba65-56324bb612d3 | -6.3894 | -45.4664 | 2026-09-02 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| caf4a992-96df-385c-abee-edbd1d7162d0 | -9.2144 | -47.99 | 2026-09-02 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2f6d0b05-c5ac-39b9-ad59-cd3ceb5d696c | -3.6215 | -60.566 | 2026-09-02 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a0c5a52c-dfab-359e-b1be-aac8e427eb34 | -3.2361 | -61.2359 | 2026-09-02 14:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b91972f1-d309-33a7-8951-3001a257ca67 | -12.0936 | -47.0913 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 622fc2d5-481c-3cb2-959d-a2c4771cc814 | -11.1939 | -46.0865 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f930311b-10a2-3334-9037-b988e4a526b1 | -17.0878 | -56.8534 | 2026-09-02 14:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.8 |
| 4d5395bc-09f0-3a7b-bc55-7cd360f32ae5 | -5.5833 | -60.1924 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 15a2c9c7-22f2-3ef3-b2c0-d905d6de0bb1 | -11.2669 | -45.1398 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 01cd8f84-7971-3d4f-bb38-b4afaf8cd427 | -6.8183 | -59.7658 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2f9b481b-95cd-384f-bebf-e2713572821f | -10.0815 | -46.7441 | 2026-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| c5fe7e8c-4cb0-3f1a-8f4f-e415fd28d60b | -6.6542 | -59.426 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f302cb27-4a05-32b0-a7fd-8a5ffdbd8eb8 | -3.2361 | -61.217 | 2026-09-02 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| fd9a4e0c-9292-3944-b71f-856af79b9846 | -11.0437 | -49.6635 | 2026-09-02 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 397a32ce-02d3-364f-ae81-d70da01ab382 | -11.6434 | -50.1976 | 2026-09-02 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d9049fac-8278-3002-bcb9-9511c9ea0eb7 | -10.7199 | -47.1812 | 2026-09-02 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 5e35ede1-ab59-36fa-97f8-03b79e37aa17 | -10.0638 | -46.6566 | 2026-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 8a23295c-e436-3caf-9dc4-6bb3a898fae7 | -3.3688 | -59.4079 | 2026-09-02 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2afacd6d-4dfc-3843-8943-33c14ac432ec | -3.2455 | -47.9187 | 2026-09-02 14:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 597b526c-f209-3819-a686-63583f4d13ec | -6.7648 | -59.4408 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6fb8f41a-e604-37ec-a775-4f0baa630104 | -13.9853 | -58.6919 | 2026-09-02 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| ded1a170-57de-3f58-9ea7-6f4c638d3026 | -11.3579 | -45.4027 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| dfedd4bc-1c35-3690-be54-6a66efbb7346 | -2.9447 | -60.9002 | 2026-09-02 14:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d9c61c40-d2ab-3e1d-8015-3bcfbe81979e | -12.0933 | -47.1138 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8d497a8c-aa3b-363c-b173-47976e669238 | -9.6633 | -48.2721 | 2026-09-02 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a49f28cc-e52a-3d8d-9bf0-eedf6ec5da7b | -11.1634 | -50.5727 | 2026-09-02 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d0ecccaf-a199-384f-b3c5-f2133c8c9eee | -6.7832 | -59.4401 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e7ee0e2a-1f67-3cd6-838e-d72be312691f | -10.442 | -46.7235 | 2026-09-02 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7ae024e1-d804-3d6e-903f-67b1689d86c3 | -9.6848 | -48.0728 | 2026-09-02 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f82e82f4-61ca-3ac3-a8e0-95d1a3b2801e | -9.1719 | -59.5017 | 2026-09-02 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4693a5a4-7c02-325d-a5e9-6f29646a5403 | -13.5724 | -59.7362 | 2026-09-02 14:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7fb91a62-7a88-3bc1-8dae-b69c0aef0904 | -12.1128 | -47.0886 | 2026-09-02 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a175e8a9-c750-385b-b772-d27ab690939a | -7.3671 | -60.6067 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| db9eb69f-6ece-31d4-92b3-e18da9114ec9 | -6.6764 | -58.7686 | 2026-09-02 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 890c464a-868a-3147-ace7-ce37e1c3dc77 | -10.3959 | -49.9703 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| fd0b64d2-ea46-3a53-9ea2-381889822ca6 | -6.6541 | -59.4452 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 710d649d-f888-352d-851b-0d6a0cbf156d | -6.8422 | -41.6791 | 2026-09-02 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 364d8a35-d504-395c-b91c-814a0752cbb9 | -10.0635 | -46.6791 | 2026-09-02 14:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ce76cca0-9629-36b1-8d63-97a9c82e7808 | -9.4159 | -45.6271 | 2026-09-02 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 37a399d5-f2db-342a-816a-73b2a0acd2eb | -7.3672 | -60.5875 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0cf48335-04f8-3e63-ac1a-5d96fa42c936 | -10.3196 | -50.0211 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 1e5ce615-121f-38f9-944c-fd1c92232f62 | -10.0944 | -45.8644 | 2026-09-02 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 485c5dc1-c292-3d99-944c-131118780cca | -7.2005 | -60.6897 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c8cb3651-bf22-3a79-b742-f7a5011204de | -10.4334 | -49.9878 | 2026-09-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 81baf449-9fcf-3fb0-b421-b9938796267f | -6.8568 | -59.4757 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| fbf247d6-be43-303e-9a6b-7333ecb8ee95 | -7.5326 | -60.7147 | 2026-09-02 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 02f7e2e8-9eb0-33dc-bc8a-c28ffb9b0c9f | -6.6949 | -58.7485 | 2026-09-02 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 0fd4b8d5-c872-37e6-bc37-38c0fc2b3f08 | -13.0708 | -45.1429 | 2026-09-02 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 95c299cb-f04e-3063-a272-9eabac0f6626 | -3.3871 | -59.3883 | 2026-09-02 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d9e24883-4dd6-33c1-b66a-51148c2e582d | -13.9662 | -58.6936 | 2026-09-02 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 306.6 |
| fd970ccd-48b6-3d1d-a7a2-77ff07fbf1f0 | -8.7613 | -62.5869 | 2026-09-02 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 148a3521-9a6a-353e-a18b-dc9ea8bbc35a | -6.6358 | -59.4267 | 2026-09-02 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 181fa999-59a8-335a-925d-165d1b7bf193 | -12.1132 | -47.0661 | 2026-09-02 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3233ef2f-c958-3054-93b9-9ea1c846a5fb | -3.6216 | -60.547 | 2026-09-02 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c9ee8f6b-166a-346a-af6f-4f53a75e7259 | -11.1935 | -46.1092 | 2026-09-02 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 8ab3a232-5347-3acc-bb4f-db346ad47666 | -9.1533 | -59.5027 | 2026-09-02 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README77.md)
