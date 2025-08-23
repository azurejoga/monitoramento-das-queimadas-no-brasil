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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c2a50b8-014b-3646-90b1-48fe00bea2dc | -5.7431 | -57.5814 | 2025-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 92bc158b-88d1-3219-8280-2d6e2139fd87 | -9.9495 | -60.1754 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 6a27b12a-d3d1-30d2-bd77-0c8890612007 | -17.5779 | -46.5756 | 2025-08-23 01:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6de75780-4663-3462-b082-24e5a3672b1b | -9.518 | -60.5268 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 550010c7-f01c-32e9-a32f-48bfee22f265 | -9.1897 | -59.6171 | 2025-08-23 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 28cdf469-6c0c-3396-816c-83c5dca9750d | -17.2751 | -46.777 | 2025-08-23 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 225503a4-8103-3f24-ae47-d1aef687e2fc | -9.9681 | -60.1743 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| e986ddc0-7c91-301f-9a0f-8c1335773097 | -17.2757 | -46.7538 | 2025-08-23 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f10a109c-668f-38ef-8d67-7d9b6efd9f7d | -17.5785 | -46.5523 | 2025-08-23 01:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0155bfbd-0e46-3564-b417-a228ab58ebee | -9.5177 | -60.5653 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 32564467-01b0-383f-b0ca-3cc43d6c7742 | -9.5365 | -60.5451 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 97b6a9cb-68c6-3721-a791-64ea90480df6 | -9.968 | -60.1937 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 425.2 |
| dfffa1d9-7f8c-3f34-9365-dbc61c71751d | -9.5181 | -60.5075 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9eef80b4-b936-3d8c-8cc6-a4c49c55d7c4 | -5.7429 | -57.6009 | 2025-08-23 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 4c2829f8-34fd-33a1-a101-75170655353c | -9.9492 | -60.2141 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| aaa8b22b-4905-32a9-84bd-c6aed6da72f0 | -7.813 | -63.5656 | 2025-08-23 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| fcc78a66-94e7-3607-8ed3-ccbe79d9cc65 | -9.5179 | -60.5461 | 2025-08-23 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| e88a25d6-0a3f-3bfd-801a-000d8ce923e6 | -7.8131 | -63.5468 | 2025-08-23 01:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2f420b73-7d19-3b9f-80ad-6ebe48d68591 | -7.0164 | -44.6413 | 2025-08-23 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2a98adaf-e1f8-31dd-abd8-65ae87a2d9b3 | -5.7431 | -57.5814 | 2025-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 9f0eb376-62b7-34d9-a139-bc36d5fcc90d | -20.097 | -47.7676 | 2025-08-23 02:00:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 8096bcd2-3e31-332f-a811-bb95f85a025d | -17.2751 | -46.777 | 2025-08-23 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2448bcd1-631c-3993-863d-dd294efc2e54 | -14.37 | -52.06 | 2025-08-23 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| bb5eacc5-a3dc-363b-b8c5-bfa68d37f5a4 | -9.968 | -60.1937 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 318.1 |
| 43c9cfa7-ce8c-33d7-b79d-42d5266304dd | -17.5979 | -46.5715 | 2025-08-23 02:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a27af4b2-04ce-3acb-8f21-b26f1ef4bd82 | -9.5179 | -60.5461 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 44c739b8-3a92-38ab-bec2-e3c8c0782464 | -6.6041 | -44.5853 | 2025-08-23 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 941282f5-5ed5-3005-ba35-d2246ec4f3bf | -5.7429 | -57.6009 | 2025-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| f239cbf7-8f31-3a43-98a1-06700403893e | -6.3887 | -45.5342 | 2025-08-23 02:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2bee23c2-91fe-3d24-a42c-b032824f9e5e | -18.9885 | -46.9233 | 2025-08-23 02:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 26d3684d-8c36-3f13-b405-978b00a66c21 | -9.518 | -60.5268 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| e6d13e31-12a5-3b6c-a4df-f682ca35993a | -9.1897 | -59.6171 | 2025-08-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9f5fd851-6d6c-33e4-8976-acb0362286a3 | -9.1895 | -59.6364 | 2025-08-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| cb4a4181-cc81-37c9-a6e0-ae5b2d2d4910 | -5.7614 | -57.6002 | 2025-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 62251e9a-cf02-32c9-8783-29edbf9a2280 | -5.7615 | -57.5807 | 2025-08-23 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a0df57e6-d8cc-3990-8cab-bda254d8a4b8 | -8.8921 | -62.4297 | 2025-08-23 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d1ebc285-a352-3a22-a74a-a40f663ad178 | -18.9683 | -46.9278 | 2025-08-23 02:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 903caeed-ae25-36f3-b283-75416738bef6 | -9.9681 | -60.1743 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| c78f8073-2934-3d40-bbfb-e19ae30bfcf9 | -7.8131 | -63.5468 | 2025-08-23 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1e535a71-9418-3e60-9936-f3eedb3e7b52 | -9.4449 | -47.6585 | 2025-08-23 02:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c180bc6c-4c69-31b3-a0c6-aac72139d603 | -7.0352 | -44.6396 | 2025-08-23 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 36641e34-03db-3607-b379-6d4426dd579e | -3.4439 | -49.051 | 2025-08-23 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 53dcf064-987c-3b17-9303-1c3391301968 | -9.5177 | -60.5653 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 43ae5e5e-1fd4-3faa-80fd-5c15ff649d0c | -9.5181 | -60.5075 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 53080c4a-97db-33a0-844c-f21808d1099a | -9.9493 | -60.1947 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 445.0 |
| f65028aa-2348-3c10-974c-05944cd51a0e | -6.6044 | -44.5624 | 2025-08-23 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 040fb2f0-0fdd-357c-811b-c25d7e9c672b | -7.813 | -63.5656 | 2025-08-23 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 5bfce2b9-7c93-3f0a-90aa-989e843b33ad | -12.9921 | -45.2252 | 2025-08-23 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 27ff2a58-10e0-31bb-9c92-64b847ffdf1f | -9.5366 | -60.5258 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e8877689-ad57-3873-8a5d-0acea3fe39ff | -17.5985 | -46.5481 | 2025-08-23 02:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 5d5b97d2-c639-3f74-801d-066e1cb973f7 | -17.2757 | -46.7538 | 2025-08-23 02:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 050e3e18-2870-33a5-88bc-f25999337c05 | -14.6706 | -54.9142 | 2025-08-23 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5e7ab1e1-bd6f-38d3-b13b-9af78aaabbfa | -9.1712 | -59.5987 | 2025-08-23 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 9b3eda0e-5cf8-38e7-ae55-c16829b8a820 | -9.9495 | -60.1754 | 2025-08-23 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 218.3 |
| d205d74a-d36a-3690-b1cb-a06456a4c0b0 | -17.5979 | -46.5715 | 2025-08-23 02:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6da63f24-994f-3c57-a673-ece81d7400b5 | -9.5179 | -60.5461 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 12aa7c2e-ce9e-30ee-917b-e3382a8110ed | -17.2757 | -46.7538 | 2025-08-23 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 6a9b1ae4-ba29-3222-91b6-4377056f2752 | -9.518 | -60.5268 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| e140a3f3-fc9c-3759-a308-d525b87e0dca | -9.9493 | -60.1947 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 378.4 |
| d8a6fdcb-a120-33c1-90b3-4e6ee1c842b5 | -5.7431 | -57.5814 | 2025-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ac4f298b-4f06-3de4-8231-d4368ae84b35 | -6.6041 | -44.5853 | 2025-08-23 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8ef47986-60c3-3886-b94e-6218f629af63 | -9.9681 | -60.1743 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 521acdbf-6778-312d-8297-8c448d3ce22f | -7.8131 | -63.5468 | 2025-08-23 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 93fa5677-0edf-3d8e-be34-f1fda998121c | -9.5366 | -60.5258 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2d86d918-272d-3bce-b914-829f3f9fdf65 | -9.5177 | -60.5653 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 3c0d9a49-5616-361b-af22-e9eb73f9619e | -9.9492 | -60.2141 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0cb17cbe-328b-3bbb-a700-aa17c3e37b87 | -5.7615 | -57.5807 | 2025-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| df83ced5-52bc-343a-8ab1-018537977a4c | -8.8921 | -62.4297 | 2025-08-23 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| de03eb3d-9760-3a8a-a7f8-8cfad7be8a37 | -9.1897 | -59.6171 | 2025-08-23 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e488af73-6f28-38c2-9952-1cb0c06ea2b0 | -9.5181 | -60.5075 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 175694e4-c69a-392e-9722-e67ab3def6d4 | -17.5785 | -46.5523 | 2025-08-23 02:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 486066d1-1814-329c-8882-642fb5638108 | -5.7614 | -57.6002 | 2025-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bd86dd3d-f1ef-332f-840d-7a81912260d0 | -7.0164 | -44.6413 | 2025-08-23 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b391c073-ea7e-35a9-89d2-9129c36f1257 | -17.5985 | -46.5481 | 2025-08-23 02:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d07534eb-31af-3643-b8f0-46dc0554789a | -7.0352 | -44.6396 | 2025-08-23 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0db2120c-2724-37e8-aee1-8dedaa23504d | -6.6044 | -44.5624 | 2025-08-23 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 0e4750fa-fc9d-3656-ae9a-8dbb24c35194 | -12.9921 | -45.2252 | 2025-08-23 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ffb2d26e-85b8-30bc-a306-d6d06ef208c3 | -9.968 | -60.1937 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 7ed405f4-6cf8-337a-8ff6-d613f126e1d7 | -5.7429 | -57.6009 | 2025-08-23 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ef3e8bf9-e667-3165-9695-a91fea9b353d | -9.9495 | -60.1754 | 2025-08-23 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 219.9 |
| 33d2c821-3e82-39a4-bd37-1a03c735b4d8 | -7.813 | -63.5656 | 2025-08-23 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 0b79e64e-871a-3120-b239-ce1ae1ae3cfd | -17.5985 | -46.5481 | 2025-08-23 02:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 48c131e7-d5dd-389c-a590-d15af4857cae | -9.5181 | -60.5075 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5f537754-6ece-31ab-87d2-974f7dadef94 | -7.8131 | -63.5468 | 2025-08-23 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3cd46b5c-f3bb-36f1-99ae-d1087a07329c | -9.9681 | -60.1743 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| dbc9bf16-65d4-3ced-a666-02fb0cccdfd6 | -8.5944 | -62.6126 | 2025-08-23 02:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8904f9d9-06ea-3c09-84de-daca9e22c0dc | -6.6041 | -44.5853 | 2025-08-23 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 72e2b8ba-adc3-3a23-ab69-350cefdb1af5 | -17.5979 | -46.5715 | 2025-08-23 02:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4d690407-9c43-3680-aa0a-efcca51dc0af | -17.5785 | -46.5523 | 2025-08-23 02:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5590c1c0-61ac-33a3-a9fa-b80d2ff74ffd | -9.9495 | -60.1754 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 4eae2bff-a9a5-36c5-b56d-4776b74421cc | -12.9921 | -45.2252 | 2025-08-23 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 11381910-c5d8-3f41-bb4e-674e95655213 | -9.518 | -60.5268 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 800d77ad-28b8-3bff-858f-00702ce40764 | -9.5179 | -60.5461 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 1aeafd9f-a16a-3b28-839f-3ea714f5b7f3 | -7.0164 | -44.6413 | 2025-08-23 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b791de8b-2768-3036-9c33-ca6a76519c22 | -6.6044 | -44.5624 | 2025-08-23 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b2bad9f3-fc89-36a3-ad04-b309df1d340a | -5.7614 | -57.6002 | 2025-08-23 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 69fc40ae-4091-3451-bbb4-9ab6053ad3f5 | -9.1897 | -59.6171 | 2025-08-23 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 26add070-55a0-3bfe-bb9d-1a4390a60e57 | -8.8921 | -62.4297 | 2025-08-23 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ca6bd448-169e-3482-a6db-1d02268e8cf9 | -9.5177 | -60.5653 | 2025-08-23 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 96adc3c8-2f61-3b53-be52-f8293fa9f644 | -7.0352 | -44.6396 | 2025-08-23 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README11.md)
