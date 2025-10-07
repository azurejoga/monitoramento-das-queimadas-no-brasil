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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70cd8078-88b4-366d-b473-bbd48bf4517c | -10.8916 | -47.1377 | 2025-10-07 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b53ad1bc-f160-3861-b9b7-fc1c20130818 | -6.4355 | -44.5764 | 2025-10-07 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 217f3001-9a98-326f-afaa-24c5b0f51b7c | -9.438 | -56.6608 | 2025-10-07 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 08b9c68f-5c8f-3d1f-869f-5707fceff0c8 | -18.1176 | -53.3548 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3edea2f1-980e-3ec4-83d3-450a36d9021f | -10.8919 | -47.1153 | 2025-10-07 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c74797c0-5b12-3b42-af11-1448de4ead67 | -8.6521 | -46.274 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f126ccdd-6107-33ee-848d-a36b01b47b96 | -8.5198 | -46.3098 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1e7d66a1-5157-3c4c-b72b-bda6dd302e03 | -9.1715 | -59.5599 | 2025-10-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 23c3e25a-c429-3f0a-9b4b-72a38873f80e | -18.157 | -53.37 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0e0f3de9-1243-373b-b090-5c45bc64f7c0 | -18.1172 | -53.3763 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 62f5cdd4-0f9f-3bdd-9b5f-e11ed9b02859 | -14.8835 | -51.4346 | 2025-10-07 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 71344bab-8746-3c33-9837-247b7af60c12 | -14.758 | -46.0335 | 2025-10-07 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f1e9d588-9d49-3b8b-9058-128c0eafbc05 | -22.3128 | -49.8915 | 2025-10-07 00:00:00 | GOES-19 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| aaea9e88-b233-36de-8af2-6b0698f9f28b | -14.8641 | -51.4373 | 2025-10-07 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 45a5daf8-acaf-3797-b8ea-4a07808afa5f | -22.0071 | -49.7321 | 2025-10-07 00:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 8496cac1-2663-3b4f-8e48-611ac97f7804 | -8.6333 | -46.2759 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| abda6636-9441-37ba-b887-fd6532759e2b | -6.4543 | -44.5749 | 2025-10-07 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 29a7f632-0522-3781-ac30-e41aa8097899 | -15.6198 | -52.5715 | 2025-10-07 00:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d02d81be-a984-32bd-bba9-85bf5560c701 | -22.3343 | -49.8635 | 2025-10-07 00:00:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| e276e04a-18c6-3afb-850c-1af65a2adbe1 | -8.633 | -46.2984 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 27c985d7-ab22-380d-ace7-d80b1c8ead95 | -15.6003 | -52.5742 | 2025-10-07 00:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 52274568-eb87-33bd-85f1-592ac702ceb4 | -10.3916 | -50.2916 | 2025-10-07 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 897a0dc5-5cdc-318e-96e4-153747f5b898 | -12.9103 | -54.7352 | 2025-10-07 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ba490d6d-c00b-3adf-9659-f92d4fa44ad0 | -6.2421 | -43.2743 | 2025-10-07 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 394eb188-4dd4-31e0-843a-4e78eea2b058 | -5.8003 | -46.5607 | 2025-10-07 00:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c41bab11-981d-37ed-b3d4-ef076d27efc2 | -22.3337 | -49.8867 | 2025-10-07 00:00:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 7afb9951-4bb7-3547-b783-b217a2a94939 | -8.613 | -44.9189 | 2025-10-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 95efd9fa-e8bc-3c4f-9755-769d9302f1b5 | -10.8731 | -51.0289 | 2025-10-07 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c2c27164-e7bf-3d91-a4ac-bb7a5c68b6cc | -11.7401 | -43.2928 | 2025-10-07 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 186.5 |
| a79fe7aa-f1ec-3746-84f0-dd553700ff1f | -10.3913 | -50.313 | 2025-10-07 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| ab7c2c11-8266-3390-8fc1-70f08f17d19b | -18.1574 | -53.3485 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3e0d5781-c0c7-3b2f-81cf-f983cb50cee2 | -12.4267 | -45.6136 | 2025-10-07 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4d02a9d7-6115-3cb6-8a50-834de8876416 | -5.3999 | -40.9856 | 2025-10-07 00:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| b195d8e7-20a7-340d-b0a8-e974a6df23cd | -4.6873 | -45.8504 | 2025-10-07 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 6654a948-65e5-3f8e-b05f-366c98b832e3 | -20.1001 | -44.1921 | 2025-10-07 00:00:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| c347af37-531d-36ab-bf13-5e251684b8fa | -14.7585 | -46.0104 | 2025-10-07 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 01817b11-0bd9-3bac-9d00-7be42118ca9c | -8.501 | -46.3117 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3e6d4d96-5ce4-3b99-b1d5-78867e11c3c3 | -8.174 | -50.3035 | 2025-10-07 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| f49bac00-df86-39f7-93c6-98be5e305d79 | -14.8832 | -51.4561 | 2025-10-07 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 118f7eff-87a8-3264-ba5b-b5d349af7724 | -6.8703 | -46.0574 | 2025-10-07 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 202d8a78-5928-31d3-bdb2-7e0fef29aab2 | -4.6875 | -45.828 | 2025-10-07 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| cc5a729d-ebf7-307c-8fec-37c93f1783c1 | -8.1927 | -50.3019 | 2025-10-07 00:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c1884f78-b869-37a1-a113-09cb3454f1ad | -21.4993 | -46.005 | 2025-10-07 00:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| c720f324-a6eb-3cbe-ace3-68e82a97f494 | -6.5849 | -44.6327 | 2025-10-07 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cf7672bc-a797-33bb-8f5c-22201a0d02ee | -14.903 | -51.4319 | 2025-10-07 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 02bf40c7-edfc-3cb1-a5d1-bca1e7cd8dcf | -8.6519 | -46.2964 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 001fe511-e533-34a5-bf80-96846cbc63e3 | -8.5007 | -46.3342 | 2025-10-07 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 475ab046-6524-33e2-b6c7-5620cc42f5e9 | -10.4102 | -50.311 | 2025-10-07 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 88a3b1de-8d4a-3fe0-91ad-9235c110a8be | -21.9079 | -44.8726 | 2025-10-07 00:00:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 237db725-ebef-36b7-a68f-f5e28ad654bf | -20.9025 | -48.8338 | 2025-10-07 00:00:00 | GOES-19 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| c42bcc19-e7c6-3e75-8804-795a949828e3 | -13.541 | -42.9835 | 2025-10-07 00:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |
| c6605be1-f90f-3a9b-bcb5-d71c934fe252 | -18.1565 | -53.3915 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 11d0526c-89e0-33b3-a42d-62cb241ff699 | -18.1769 | -53.3669 | 2025-10-07 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7f90d365-500c-3ed4-84ac-ee5a9f2bd5f5 | -6.2609 | -43.2727 | 2025-10-07 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 9fba4864-5ee1-3244-9ab4-bff1fed2c758 | -5.4937 | -43.0761 | 2025-10-07 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0af901bb-9238-3169-a0e0-9af21d682bb4 | -20.1269 | -43.99473 | 2025-10-07 00:09:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3a9caad9-6f1e-30da-a0b2-f8e26f51e1c9 | -18.77881 | -44.61504 | 2025-10-07 00:09:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8f2b8678-9bdd-3ea9-88aa-f1fc653d9f5f | -20.09304 | -44.19122 | 2025-10-07 00:09:00 | TERRA_M-M | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e0118c49-fe4d-310b-942e-fd2819ff859a | -21.90598 | -44.87846 | 2025-10-07 00:09:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.8 |
| af8527ce-e43e-3abf-bce6-2e18c5b1fbdf | -19.54009 | -43.56778 | 2025-10-07 00:09:00 | TERRA_M-M | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f83d518a-ecc1-37d4-a698-53ed813c2393 | -20.42416 | -41.63787 | 2025-10-07 00:09:00 | TERRA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2520f6e7-f6b2-3489-ab59-31bc3c598eb1 | -18.51794 | -43.41988 | 2025-10-07 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d70c46ea-2f50-3312-b24e-13383cba73c8 | -21.47268 | -46.26131 | 2025-10-07 00:09:00 | TERRA_M-M | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 4462a53e-a51a-3d45-b69c-359b0fe890b8 | -18.04204 | -43.1545 | 2025-10-07 00:09:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 017fcc09-30bd-3c0d-8f0c-e3b73a7ee74a | -21.74759 | -44.41062 | 2025-10-07 00:09:00 | TERRA_M-M | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 8c1cb853-24c8-3357-8a9e-e74e8d625c67 | -22.38108 | -49.96175 | 2025-10-07 00:09:00 | TERRA_M-M | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 70c1da12-28e3-3a58-a8c7-41f218486400 | -18.57006 | -44.17924 | 2025-10-07 00:09:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| aa1228b6-0e71-368a-a218-9a8686afcd8c | -20.49604 | -42.72372 | 2025-10-07 00:09:00 | TERRA_M-M | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| 33e4a92c-a164-347a-b76a-8d7b702d1eb5 | -21.61455 | -43.99307 | 2025-10-07 00:09:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 8bb0128e-0d26-302a-aab5-6b20c1746dea | -22.46426 | -44.19146 | 2025-10-07 00:09:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 0d66fa65-bd99-361d-be45-8924c3354f47 | -21.86744 | -42.8858 | 2025-10-07 00:09:00 | TERRA_M-M | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 92cb32c3-fa9e-3ee8-b265-a51e3823e1b8 | -21.37256 | -45.03412 | 2025-10-07 00:09:00 | TERRA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| b523e39c-81c3-3a31-8abb-3c0c6016c02b | -18.05102 | -43.15315 | 2025-10-07 00:09:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.9 |
| c48e35aa-887f-3e31-88ed-1961fb1470f4 | -22.57352 | -44.86321 | 2025-10-07 00:09:00 | TERRA_M-M | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 65a07658-b398-3952-9115-e43a56371a32 | -20.87513 | -43.37902 | 2025-10-07 00:09:00 | TERRA_M-M | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 44105472-1c2a-3baf-9301-7e12c969a156 | -20.83277 | -43.61678 | 2025-10-07 00:09:00 | TERRA_M-M | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 06469342-025b-3d79-b802-c291949df9bb | -22.46473 | -44.18521 | 2025-10-07 00:09:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b7c108ba-cb87-3fbd-b1c8-ef44f51b3f87 | -21.30191 | -45.94649 | 2025-10-07 00:09:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 03bacff4-e823-3bef-8aae-f5e51ab7e519 | -21.61834 | -43.99841 | 2025-10-07 00:09:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| c7d82b8d-1119-3d0e-8544-73b4c7f19901 | -21.61599 | -44.00461 | 2025-10-07 00:09:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 48a40ad8-1458-3020-938f-61f0e3dba785 | -22.01356 | -49.71921 | 2025-10-07 00:09:00 | TERRA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 28d5cfb3-b8cc-3051-871f-55e3665d5f78 | -20.09444 | -44.20271 | 2025-10-07 00:09:00 | TERRA_M-M | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| f17683c2-b071-340c-98ba-22c39f0d44b5 | -22.64318 | -44.5831 | 2025-10-07 00:09:00 | TERRA_M-M | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fc6131e7-878f-31cc-bc39-86cc7842c2dd | -18.40071 | -43.22484 | 2025-10-07 00:09:00 | TERRA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7b1f96b3-4f66-38bf-a7df-79cccd0943be | -21.74909 | -44.42292 | 2025-10-07 00:09:00 | TERRA_M-M | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 63fdff06-848c-3ab0-9a65-b1ba86930396 | -23.05272 | -49.91471 | 2025-10-07 00:09:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| e4174078-0206-38f2-9fc4-3863508cd9aa | -20.98329 | -45.58738 | 2025-10-07 00:09:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45b665bc-934f-3211-82d2-8cfe619e0a21 | -21.90306 | -44.87299 | 2025-10-07 00:09:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.0 |
| 6de0bdd0-37ec-316f-8bd2-2149562e9548 | -19.9525 | -44.62906 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 80787e9b-a479-35cc-a395-0bd42350a5cd | -21.09015 | -44.17934 | 2025-10-07 00:09:00 | TERRA_M-M | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ad2cc5af-7122-31fb-9ca0-ba9dcf3e130b | -23.10577 | -46.17988 | 2025-10-07 00:09:00 | TERRA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| c374d1ce-e968-3017-8f1b-bfcec42d8c37 | -21.48394 | -46.25982 | 2025-10-07 00:09:00 | TERRA_M-M | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| ee0a3c55-1ab2-3433-9087-187943d0e26c | -19.70825 | -44.12424 | 2025-10-07 00:09:00 | TERRA_M-M | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a7b78fc-1186-36b0-8de6-23eed49a7f3d | -21.09853 | -43.84663 | 2025-10-07 00:09:00 | TERRA_M-M | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 376ea79a-9a81-3484-ad75-e369dcae6c3f | -22.70614 | -44.33831 | 2025-10-07 00:09:00 | TERRA_M-M | BANANAL | SÃO PAULO | Brasil | 3504909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 05129bbb-5fc8-374c-88f0-a0083a8121db | -21.0881 | -44.18568 | 2025-10-07 00:09:00 | TERRA_M-M | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 39bd8fa3-9afe-370e-a4b9-63771c2db13d | -18.6007 | -46.8119 | 2025-10-07 00:09:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 281a85c4-9383-3179-9a40-a5eb35440d90 | -19.04465 | -48.14045 | 2025-10-07 00:09:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 156e95f8-77f1-3118-a4cf-6c0438873515 | -19.80194 | -43.53352 | 2025-10-07 00:09:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c77a4a4d-4b44-31eb-b866-b4e9c9bcce5f | -20.93278 | -43.11224 | 2025-10-07 00:09:00 | TERRA_M-M | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |


[Clique aqui para ver as próximas entradas](README2.md)
