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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 834a710f-033d-34b9-a020-3fd98874c7e6 | -12.95964 | -46.99455 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4bc20fa6-924d-3e54-b10a-27f786de5bc2 | -14.31046 | -51.56636 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02172186-68f2-3e56-bac5-c3f005794a60 | -14.31678 | -51.5579 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47980416-fed4-3389-b594-ce233c580804 | -16.31435 | -43.09827 | 2025-10-13 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac1a679b-e4a6-3abb-b7be-95cf6caf4d5e | -12.95572 | -46.99759 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf67a0f0-2387-32a8-8f3b-61ae58bc83d2 | -16.19809 | -43.67469 | 2025-10-13 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b4d81c3-0632-3fce-b042-9a9e47ef866e | -15.85385 | -56.76451 | 2025-10-13 04:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a933e9-0146-3b66-9623-03a3b2982551 | -13.75124 | -45.64884 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5097bb0f-fa15-35ec-aad9-620f0b105c78 | -13.85693 | -45.48477 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83351d91-eaac-3b83-b53d-4986aec78a3b | -15.85925 | -56.76579 | 2025-10-13 04:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 906341f0-b3c5-35c2-8cb7-5f715946d4dd | -13.86419 | -45.48225 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f68df8-0a2b-36aa-83a9-341c6f4b3e5e | -13.84745 | -45.54626 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb32aac9-f868-3cb5-b51e-2d2c6309a21a | -16.12378 | -53.98022 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aba1e7ac-df6d-3115-b476-04ea66f30fbc | -13.84407 | -45.50126 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b803c51a-b37c-32d6-9c49-2571492c7a1b | -14.2433 | -51.52612 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 693c5d45-c4dd-39c5-811b-ae4266669f6e | -12.94789 | -47.00363 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dff5c14d-8a8d-39f5-91b2-cf2483d2b598 | -13.67575 | -43.056 | 2025-10-13 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ce32c72-b073-3895-98cb-596951f06bc8 | -13.8636 | -45.44136 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a78254d-148c-391e-aff0-ff92616d7332 | -13.75569 | -45.64221 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c74cbe5b-1597-38b3-90ae-daa4c5e06423 | -11.74802 | -54.72321 | 2025-10-13 04:25:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18a373b8-aecf-3345-b741-bf1cf9d5dfda | -14.26704 | -51.50874 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49fb9ad3-0a62-3e2b-85e2-696d76a1a62c | -17.32088 | -53.81079 | 2025-10-13 04:25:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f1fe238-1053-3fe8-88aa-2854c5828aa4 | -16.47733 | -49.67942 | 2025-10-13 04:25:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e367f2f5-7c03-322f-a416-f5916e1cc0ff | -14.91403 | -48.48468 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11a4c057-c277-3c04-aa36-5176bcd4a209 | -17.88071 | -45.00806 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f58c20d2-8344-3b5b-a507-e4d08b83e810 | -13.43358 | -47.90343 | 2025-10-13 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc3be00-4509-371f-a94a-ba0c5ccbd00a | -14.44552 | -47.95617 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dbb487e-20cf-3c7c-9e00-0e0d54da0ce8 | -13.85526 | -45.5179 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70d050db-3aa0-3090-9a1f-8a1202c04c18 | -16.12104 | -53.9699 | 2025-10-13 04:25:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 952336de-df67-387e-a670-cf8b30a65c59 | -13.75514 | -45.6458 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d1e57b8-8e27-377c-9663-1e8df6619ad0 | -17.17499 | -43.09892 | 2025-10-13 04:25:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94f79f66-dbd1-3ecb-996a-2006b56f2210 | -13.84521 | -45.53849 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9b456c0-357f-31b8-8380-54739ba063a4 | -13.76238 | -45.64333 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e45136a9-16ef-342a-89fe-8e9257d24f61 | -14.91124 | -48.48028 | 2025-10-13 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da89efee-7db9-345d-abe2-3d1fc05eb977 | -12.75161 | -50.65892 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f2c5b1-a204-3ba6-8e1e-40c4d16b55b9 | -12.15746 | -53.6306 | 2025-10-13 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670e7adc-57c3-3096-b708-1714eb80f472 | -13.87872 | -45.4772 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 414b13cd-6f40-3eac-9b0b-c69f7751691b | -16.34935 | -42.39415 | 2025-10-13 04:25:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d4bf772-b3a5-3435-b381-50e487f37297 | -13.75068 | -45.65244 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f72079c-00f1-3367-b506-d7f435917706 | -16.48153 | -49.67603 | 2025-10-13 04:25:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02272f25-fd0b-3a00-bb44-541c58bbffc5 | -13.3321 | -47.10504 | 2025-10-13 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 884c885a-a8ac-3e7c-87b6-ce885e144053 | -14.31375 | -51.55184 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1b225ff-60da-348b-bef5-fb18e862336f | -13.85916 | -45.49255 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ad96a5d-10e7-3368-be94-b7d73c926232 | -12.74385 | -50.65751 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fdb3ad5-f8e3-3b24-8173-4be76f4065dc | -13.32876 | -47.10443 | 2025-10-13 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf81b866-2b30-3dcd-8519-bdf32a79e5a0 | -13.85972 | -45.48893 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0338d21c-6d8c-3580-aa50-fa4eb9d85b61 | -14.21633 | -51.51554 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 21f17354-931d-3818-9790-de55b6109f3f | -15.80016 | -42.51092 | 2025-10-13 04:25:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 150c1038-2623-3d12-883d-4035e8d46b08 | -13.83906 | -45.53379 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b8d1757-3fc3-3e4e-be36-c3221c297a47 | -13.86084 | -45.4817 | 2025-10-13 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dcfda81-8599-3bb6-a511-324939928bcc | -12.95514 | -47.00121 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0b66069-7825-342d-a51f-55df90e86b3b | -15.56776 | -47.90781 | 2025-10-13 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5fb6502-e09e-3f2e-b059-0bddbdb162ac | -14.22032 | -51.51629 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f7beb4c3-adbc-367b-ac32-244d7fa452fe | -14.27501 | -51.51025 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fbb16f1-2bb1-3409-988a-9418e524971f | -17.89644 | -45.02289 | 2025-10-13 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dd360f0-b4ac-3b11-ae8d-ef8e9f65b665 | -13.41576 | -47.21455 | 2025-10-13 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba84455-d3d8-385d-bc5f-0fe28e52834e | -14.31632 | -51.55648 | 2025-10-13 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e80dc3a-5acb-30dc-aed8-05a7064284ca | -12.93089 | -47.04511 | 2025-10-13 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48e9c5fc-f168-315e-b3a2-9e9b71376532 | -19.90063 | -54.17549 | 2025-10-13 04:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fda1aae-d02f-378c-b8c8-e605cd7d6485 | -20.83955 | -42.80861 | 2025-10-13 04:27:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7db0ebb6-4ec7-3211-8ea3-b0e80ceb27b7 | -20.84767 | -42.80982 | 2025-10-13 04:27:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef1b4329-7012-325a-b587-402d045097e7 | -20.84361 | -42.80922 | 2025-10-13 04:27:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 325eb5da-a590-3cc8-a021-7cca83f5aa7f | -19.89824 | -54.1741 | 2025-10-13 04:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b8d0cf1-18c2-3de1-b395-fcbdfb3c9769 | -20.84005 | -42.80475 | 2025-10-13 04:27:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de64c128-c234-31aa-abd6-28c894ce5b2b | -21.08667 | -42.93536 | 2025-10-13 04:27:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f9e5e4f-3947-346b-ada3-13c2dbba2eac | -30.82859 | -52.32702 | 2025-10-13 04:29:00 | NPP-375D | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 4e48c6cd-ec30-35c8-9b11-4ab78d884c43 | -2.5239 | -47.7899 | 2025-10-13 04:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c80a5c1a-6c37-3f82-a106-3b80d4d44d4d | -17.3384 | -53.7922 | 2025-10-13 04:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 2015f7fe-9e0c-3a88-a684-a30fe81b70bb | -14.3212 | -51.5333 | 2025-10-13 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4ebed986-9c60-3761-9b27-65074ddde09c | -14.3019 | -51.5359 | 2025-10-13 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 134ffa3e-0f3a-3fee-9e94-29a230680491 | -16.1207 | -53.9625 | 2025-10-13 04:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5175f028-8246-3cf3-8935-1cd57be8530e | -7.4863 | -44.621 | 2025-10-13 04:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a3f862b4-0a16-3f12-aaa3-7b9fe19208ae | -10.8093 | -43.9744 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 333.3 |
| c1a9b147-0591-3adc-90af-f2ae32374df4 | -7.4863 | -44.621 | 2025-10-13 04:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5fcbb594-ef3d-38f8-93eb-5b348c6756af | -10.7906 | -43.9537 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5fccda57-e266-33c3-a0e2-8604d943c17c | -10.8097 | -43.951 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 9c9ff7c5-377d-3476-9bf1-c886b1f7e989 | -10.809 | -43.9979 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| f85ab6f7-3964-3200-822b-ca29e2370d58 | -10.8281 | -43.9952 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6a54a422-72ae-3c53-bb24-2b0629c0ae71 | -10.8285 | -43.9717 | 2025-10-13 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 71d63b55-390a-34b4-9b26-51df20d4d918 | -2.45972 | -49.03552 | 2025-10-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d0240c-54de-3674-98af-2b15baec576a | -2.53556 | -47.80681 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bfd34ad0-0af2-3cda-9218-40546bf59185 | -2.14416 | -47.5114 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82a23c06-33c5-3dc0-ac88-a6a1119aa5d5 | -2.2518 | -47.87109 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb38fe02-e160-36ec-95c5-67812ed40633 | -2.53616 | -47.80305 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 18e4f9ea-0515-3145-854b-ceab60d78d4c | -2.25122 | -47.87483 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0d4d1a2-1930-3604-81cf-53dbc6fdb691 | -2.2656 | -47.85029 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56dbfa23-9656-3ca4-9107-9f3013be0f8a | -2.72174 | -49.7889 | 2025-10-13 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed0c7e5-2cab-3c74-816c-a885fadd3e5e | -1.25165 | -49.05043 | 2025-10-13 04:42:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c7194df-3e83-3f88-85fe-bd9f9c742165 | -1.90036 | -51.01133 | 2025-10-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 074ba65b-df84-3173-b4d4-7a6052478b8e | 1.89174 | -55.7584 | 2025-10-13 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9fc0b3-8659-3edb-84f6-42bf850ecaa5 | -2.44232 | -48.99676 | 2025-10-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b143b3-ea07-357c-b990-ae2972916174 | -2.53881 | -47.80223 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ea49274f-617f-312e-906e-31784bc63379 | 0.6904 | -51.46055 | 2025-10-13 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d2a1161-6fa3-3a8e-b767-a7ed9b13f1bd | -1.89757 | -51.00727 | 2025-10-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b5bb2e6-90f5-3cc7-88cb-00147fb57a30 | -2.52985 | -47.79826 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f24e910b-90f8-36d9-87d0-a56f8846d21d | -2.5342 | -47.80926 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50529a5a-4db2-35a5-b7a7-6c97c3ea8f0f | -2.54285 | -47.79895 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c43cb109-e061-3114-a7f2-fb345eaab0b1 | -2.52866 | -47.80577 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8c17b4a9-dc0d-3e81-bf55-1c135ef73a01 | -1.51123 | -47.72133 | 2025-10-13 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80f9051c-8d95-3317-8778-661bfdb30a94 | -2.44566 | -48.99727 | 2025-10-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
