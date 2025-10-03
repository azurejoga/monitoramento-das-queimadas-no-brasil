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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af0d0afc-513b-3b6b-997e-c2ecfa2aa0c0 | -14.607 | -46.7249 | 2025-10-03 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 275852c0-9835-3533-86f3-9eebdf29da30 | -8.8543 | -46.6781 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| eedbf144-4cb2-3b68-a2fa-c03e798fcae8 | -9.3357 | -45.9532 | 2025-10-03 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2014cd43-2928-3949-8544-de485c4d5a08 | -18.9471 | -48.501 | 2025-10-03 13:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 23cbea5e-1c76-313d-a495-07240b8400dc | -7.2845 | -44.18 | 2025-10-03 13:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e6261425-e4fc-3ede-83d7-7f5571801bd6 | -13.7862 | -51.2833 | 2025-10-03 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ddfa218f-c00c-3acd-94c0-8b090b075891 | -11.1444 | -43.3845 | 2025-10-03 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 128.8 |
| d35d56df-5461-39ab-a1d1-063a2690e7e6 | -13.7858 | -51.3047 | 2025-10-03 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 8f9673ba-389a-3d57-8155-857249b812ed | -12.5305 | -47.2988 | 2025-10-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2b7b587b-b5aa-3faf-81e6-15cfb386596e | -12.6319 | -46.9923 | 2025-10-03 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a448c968-4f0a-37e5-88ff-c649b556151a | -10.297 | -50.3013 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d909ca14-c7f5-35aa-864e-818328c4f801 | -8.5389 | -47.8368 | 2025-10-03 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 65b23208-d7eb-360b-9966-e0c1426ca317 | -10.9294 | -51.0654 | 2025-10-03 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5eab6a7d-b9ed-3b29-aced-d18e73354074 | -14.6497 | -44.7499 | 2025-10-03 13:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 78e34378-2900-3f78-8c85-381dc24d1d73 | -7.2913 | -45.2548 | 2025-10-03 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b558bc9b-3951-3954-aa66-2876784a0b19 | -14.0032 | -44.961 | 2025-10-03 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 251.0 |
| d0bfa3aa-454b-374d-ba96-88bf66735bec | -9.9182 | -43.7212 | 2025-10-03 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 225.5 |
| c6a88921-bd52-361b-8694-d30b0f278cb6 | -8.6908 | -47.7126 | 2025-10-03 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a0e43ff2-03e0-3a80-aca1-0e48ba5cc851 | -7.7496 | -46.2496 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 178f36b8-63a8-3ef9-8729-35b840357c91 | -10.0906 | -50.2154 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b4d8e50c-1e09-30dc-aad0-8ddb8ab7201d | -7.7494 | -46.272 | 2025-10-03 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 2cb5fd26-a808-395d-b19f-808110770ef5 | -12.7627 | -50.5567 | 2025-10-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| cf6aeab9-89dc-3673-b0ea-8dcd73b5dab2 | -17.6338 | -44.4385 | 2025-10-03 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 127.8 |
| dd20f14c-b05f-36b4-9057-a2fbb4198051 | -12.7435 | -50.5591 | 2025-10-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| b523cef1-e694-3051-b8b2-1ded90eeb6ed | -10.1092 | -50.2349 | 2025-10-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5ae6f5cc-a03c-3b86-a804-4660d37294c5 | -8.1699 | -44.1608 | 2025-10-03 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 299ee579-db83-37b3-a734-52aec96f9ed6 | -13.7673 | -51.2643 | 2025-10-03 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 24d54a8a-a236-343d-8498-bb90e95f4d33 | -13.3611 | -48.1159 | 2025-10-03 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7754c5d6-1926-3cb0-93af-10e69be0425e | -14.3675 | -46.102 | 2025-10-03 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a2ae5e23-d7a0-30b0-b9f8-2fc75c026f50 | -14.2939 | -45.9076 | 2025-10-03 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b4e2c2a7-d2c6-3d40-ad10-98751b082049 | -13.3422 | -48.0965 | 2025-10-03 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 2a0dc30c-491e-3d23-ab57-1649dd538567 | -17.6331 | -44.4626 | 2025-10-03 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 262.3 |
| d85eb6b9-e33c-36b6-9bdf-8ab86753b95b | -10.9294 | -51.0654 | 2025-10-03 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 53c874f1-08f5-33f6-95f5-2ddde3067fe5 | -14.367 | -46.1251 | 2025-10-03 13:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 91916235-cfa4-3164-8720-475a63d58a4f | -6.6416 | -42.7934 | 2025-10-03 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| ed0aad03-ed6f-3a5b-ae92-186fc391d5c3 | -9.9186 | -43.6978 | 2025-10-03 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 7036dadb-f48b-36df-9e9f-cfc61553de4e | -8.1728 | -47.0119 | 2025-10-03 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a94bb41a-c4e0-3036-9869-bd15657c9a60 | -14.6497 | -44.7499 | 2025-10-03 13:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 504b4d63-c011-33f0-9d8a-9a0fc7ec01f9 | -13.3221 | -48.1439 | 2025-10-03 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 422fe5a8-ddaf-38d4-a31e-ab6d1845f57e | -14.0037 | -44.9376 | 2025-10-03 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 7b884ac7-a9b1-363d-a660-dbd5e78ed379 | -7.7494 | -46.272 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| b7b1d912-3a98-3548-a902-af6ff93bca5a | -8.8543 | -46.6781 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2dc42dfb-d4ff-35c8-a6b9-5c77db2bdff1 | -7.2845 | -44.18 | 2025-10-03 13:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d6d5d355-785d-39a3-8a46-f3f0144df27a | -9.8772 | -47.8103 | 2025-10-03 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| ad53ed42-9d88-3265-b8d0-ef24b2a3a01d | -7.3101 | -45.2531 | 2025-10-03 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 80911fa5-212c-31dc-84f3-f2300a352a3e | -9.9394 | -43.5777 | 2025-10-03 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 4bc51518-1c6f-3f24-bfc8-11580ff87830 | -9.9035 | -45.9553 | 2025-10-03 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0e07da34-4d33-3fab-a56b-fc2fdaccb437 | -8.1917 | -47.0101 | 2025-10-03 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7a788135-3e56-392c-b8aa-8928d6645d48 | -7.7684 | -46.2479 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 29b5c4f4-5136-3e6c-8efc-b8bbb19613f0 | -16.7717 | -43.9601 | 2025-10-03 13:30:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 28229783-0328-3747-8d2b-6754a12f8488 | -11.1275 | -47.8634 | 2025-10-03 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7d7fa9dc-5a31-3f5b-b6a6-fe63b51912a1 | -14.2367 | -44.9428 | 2025-10-03 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 7fc1068e-9d7e-35a7-ba95-b6f7c41031e4 | -17.6338 | -44.4385 | 2025-10-03 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1ce41e4e-05f5-396e-9422-73901f45f093 | -7.7499 | -46.2272 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ab059188-e963-3823-bcb9-19f0620c0f4b | -8.8729 | -46.6985 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 4e727b60-c1ef-37d2-99c8-35a896de92a8 | -12.1215 | -43.4453 | 2025-10-03 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ce5db232-4494-310c-bb15-f6945211c632 | -11.9159 | -46.3044 | 2025-10-03 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 9959d23d-ce8e-3bc3-9ea6-b81544eef1ff | -11.9151 | -46.3499 | 2025-10-03 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 58a96ce6-f08d-3e57-aca7-a8218e2ba973 | -8.5599 | -44.6494 | 2025-10-03 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 39634e55-1994-306a-97db-c5ba9f1e9623 | -7.7682 | -46.2703 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| cb346963-ed35-3ff1-97d4-06cd9ceaf46e | -14.607 | -46.7249 | 2025-10-03 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 69623348-c02a-356a-a36b-31ce90a61d66 | -9.3547 | -45.951 | 2025-10-03 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 88c36cd9-f9fd-3cfa-88fe-f430c2586998 | -11.8818 | -44.9815 | 2025-10-03 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f2602c26-be7a-3524-afd2-8a10a3bff6f8 | -13.7673 | -51.2643 | 2025-10-03 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8ebb2536-b685-3abc-9171-6a603b97313f | -10.948 | -51.0846 | 2025-10-03 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 15b959dd-49f8-35c7-8153-59b194b7e503 | -18.9673 | -48.4968 | 2025-10-03 13:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 329.1 |
| c7c37e1e-7310-3cd1-8977-755ba3f32f33 | -13.2165 | -50.9071 | 2025-10-03 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c8142872-b6f5-3c6b-b1b9-2fa15c9be7e4 | -8.9118 | -46.6052 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2acc604c-af97-37e1-b5cd-7fec9eb2cc58 | -8.5959 | -44.7833 | 2025-10-03 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c04c303a-332e-32a7-a24d-e40b0f4807e5 | -11.1444 | -43.3845 | 2025-10-03 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 4802beb7-7619-36b7-a6a2-53e1bc984b35 | -7.2913 | -45.2548 | 2025-10-03 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7600ff1c-bb0e-388a-b955-d85ff55ac069 | -13.8055 | -51.2807 | 2025-10-03 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e9a10f25-3f14-3734-9809-d6cc58c0b4b7 | -14.0227 | -44.9576 | 2025-10-03 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| bc604882-cc2a-3a20-af24-e6a147c0ce07 | -6.6787 | -42.8372 | 2025-10-03 13:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 2944aab9-e354-311f-b087-ff9a0d86568a | -10.326 | -48.1781 | 2025-10-03 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ac9209f1-9f2d-3441-8811-f0ed88e1b094 | -6.679 | -42.8136 | 2025-10-03 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| d7864270-3a63-3133-991e-4bafe15b4988 | -10.9554 | -46.7044 | 2025-10-03 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| cdfa8be0-e164-36d1-bde1-59f72f0df381 | -18.9667 | -48.5198 | 2025-10-03 13:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 115.3 |
| e3373b57-c947-31db-8767-22152a2bc889 | -12.1088 | -45.1554 | 2025-10-03 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e5a0cc3f-628d-3056-a6d1-0cd92edbd017 | -13.3418 | -48.1188 | 2025-10-03 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 296.8 |
| a9f8f82a-75ff-37b2-ac1a-1b69fa62103f | -14.2172 | -44.9463 | 2025-10-03 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 81d52e9c-1829-33d0-a081-7aacfbdb3cf4 | -9.9182 | -43.7212 | 2025-10-03 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 195.4 |
| 86a74b70-b7c9-3387-a7e0-070acfeebca6 | -14.0032 | -44.961 | 2025-10-03 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 52920b29-2bf8-3419-b642-9cdfd5e3a04d | -8.6908 | -47.7126 | 2025-10-03 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| bf5fa6ff-a4e5-377a-80d6-611a16b28ab3 | -14.2167 | -44.9698 | 2025-10-03 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 834c06f5-0369-3af5-ad36-ef8a33966305 | -10.0278 | -44.0108 | 2025-10-03 13:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 762693cb-7133-31ae-a124-8085ca2a8526 | -9.8769 | -47.8324 | 2025-10-03 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9834f0e3-e590-3a49-9548-ebf7454a852c | -11.9155 | -46.3272 | 2025-10-03 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 415.1 |
| 377fdd02-6b80-3ac1-9341-22fa65658b2e | -10.345 | -48.176 | 2025-10-03 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 426b16ff-46e8-3eeb-9302-0c687ea02a63 | -7.7687 | -46.2255 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 06976b7d-77a9-3546-bbb6-a8560fcb48ef | -10.9483 | -51.0634 | 2025-10-03 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d5673543-2de2-3775-9f1c-d9afa902b838 | -6.6604 | -42.7917 | 2025-10-03 13:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 8a8867b3-d174-3484-87ee-e9506d021846 | -8.995 | -47.4624 | 2025-10-03 13:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 6be0f0a7-f0e0-31f9-ae3f-54d8cc941a8b | -11.1271 | -47.8856 | 2025-10-03 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1c6b5572-f51d-3ef9-a84d-77889f321c6f | -7.7496 | -46.2496 | 2025-10-03 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| eb010dd0-be01-3794-9dc8-892e239c3970 | -9.4548 | -45.5545 | 2025-10-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c2aa55e2-468b-3bd0-9766-3842b3283279 | -9.3386 | -45.7493 | 2025-10-03 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fd11b35c-9541-3ca8-a2d2-3cfb7738ecaa | -11.8294 | -51.7725 | 2025-10-03 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9763c199-bddd-3263-8f10-ecdef7b3c536 | -12.6131 | -46.9725 | 2025-10-03 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 95a61287-5708-35e3-b326-7da31554ea14 | -16.023 | -50.8553 | 2025-10-03 13:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |


[Clique aqui para ver as próximas entradas](README149.md)
