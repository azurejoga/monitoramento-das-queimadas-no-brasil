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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0aaefd8-99ba-3bb9-af81-8d2a2562f721 | -14.97559 | -47.09661 | 2025-10-18 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd80e3c6-e562-3468-8ef8-a0f44759f6a7 | -10.91435 | -47.8657 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81091b61-9847-3e5b-8dc5-987c6d2330cd | -15.05082 | -48.73763 | 2025-10-18 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbb4fb96-73be-3bd5-a31d-f2053f7e9553 | -12.60978 | -52.81413 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 291b1aaa-5a7f-38c1-905e-98ed97807eee | -13.25086 | -48.5447 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54c2a810-1e91-3db3-91e5-3d2aaa640f0f | -15.51135 | -50.38746 | 2025-10-18 04:32:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87640870-5129-35d3-be54-f9d8808f4356 | -14.93362 | -46.71011 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 927f0356-7fbb-3773-9845-2a0e55b93b84 | -13.92353 | -45.60042 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 633c695d-1de5-302c-872f-e5899dcc950d | -13.739 | -48.32925 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b19cdb9-8887-3561-ae50-fd33d8b4efe8 | -13.06718 | -49.33015 | 2025-10-18 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74cfd29b-1c23-35d0-bc6f-016f908b0a18 | -14.91734 | -46.72678 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fc74a78-9d2b-3d6c-b6eb-d5163f80fc57 | -10.44007 | -49.47782 | 2025-10-18 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee519ea8-9aac-3245-8f88-3b0a11826cc5 | -13.40471 | -48.58451 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7488bc53-d5c4-3c84-a107-d06770f5da9e | -15.78278 | -41.33132 | 2025-10-18 04:32:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2acedb1f-8d19-3e1c-9319-a14cd5ddb96f | -13.43561 | -47.98359 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4fb513-1b93-3056-9cc5-f2d4da289074 | -10.62222 | -48.01728 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2ccddaa-2f90-3e1e-96b1-94db6221cc25 | -12.60576 | -52.81337 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e57c87d0-9182-3999-8a39-7d2ce6e6b06d | -16.4277 | -42.6328 | 2025-10-18 04:32:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7412bd-f2c9-376e-a9a1-bc26eee49b00 | -12.91407 | -48.58002 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4340de72-f1c4-32e3-bd83-49b8ae44f709 | -10.99627 | -47.90054 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a92c6ae-7f67-3d6f-9fb6-fe8ab8dd832b | -13.63496 | -44.41766 | 2025-10-18 04:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f8ef958-15d4-3490-a466-2ef499c475f8 | -16.59249 | -42.43275 | 2025-10-18 04:32:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da9a51bd-7dd3-335c-bcfc-a2415b54e08b | -13.93052 | -48.67938 | 2025-10-18 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5677fb6-a197-302f-a27b-4dae05f9f833 | -11.40825 | -44.26542 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23336d7-8f99-388e-af8b-7c185b8465d3 | -13.51486 | -48.00033 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b091c63a-8ff1-3bcf-9f29-352655e7434f | -10.53638 | -49.54943 | 2025-10-18 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac6931fa-7448-35fa-8ce6-38ad821d2525 | -14.92625 | -46.7128 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f607bb2-6543-35dc-a32a-7873651de02d | -12.91073 | -48.57946 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d24e4ce6-3ad3-30cf-9461-d349b0383319 | -11.36329 | -45.25777 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e65e7262-1f94-355e-bfdf-04a8ed1324db | -13.41595 | -47.98092 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 288076db-84f1-3f85-aa9e-b91f1c0a25ac | -14.887 | -52.39803 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26788f32-9313-37f9-b1de-41c86000ff4d | -16.07263 | -42.55589 | 2025-10-18 04:32:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9f52f6a-cee0-3821-a3db-dd6c2ed723ea | -14.09534 | -43.6316 | 2025-10-18 04:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 045e7251-6cb3-39df-8e00-004b5855eae2 | -12.80177 | -48.6461 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a051d0ea-e817-3948-9a3b-b8bbd87c654b | -12.74781 | -48.63022 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04388165-3ead-3eba-ba84-e1618ff8244d | -13.03424 | -46.94742 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16711b67-f23a-3923-a37b-f08daa62c838 | -18.09448 | -42.45013 | 2025-10-18 04:32:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e669cd38-2067-3e78-b643-aeb74d99a348 | -14.5524 | -49.27549 | 2025-10-18 04:32:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| daeb7656-56d7-386c-a029-087f930f2c2a | -13.76589 | -48.24617 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd4b1773-156a-3b96-8340-7de74b03859e | -10.93495 | -47.84368 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc772e4f-867a-3e8a-b97b-857a8c78ffcc | -17.49684 | -43.46646 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c42c1d29-a262-3cb7-b657-c6a7dd81328d | -10.92296 | -47.98322 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c064555-ef89-3801-afa5-1077658c99d3 | -11.6126 | -44.0875 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b4d5034a-f39f-3854-8df0-88ea12d2b048 | -11.37923 | -44.25837 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9cc8d32-5477-322b-8f67-905d927c4d50 | -13.41357 | -48.59337 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0035f436-3fce-34dd-b033-9474328771e5 | -12.70373 | -48.62653 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6474344f-24e8-3bf9-b8ba-da2fa1868fdc | -14.90894 | -52.40682 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6bfe4e4e-e2df-3b59-93a4-1ab589eb1b56 | -13.76871 | -48.2284 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 359b0a98-9be8-30ff-8c2d-48eff09c84c7 | -13.48778 | -47.95581 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea91caa1-34a0-3a57-a410-cda7898cd2d3 | -16.237 | -43.50833 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 033e80d0-97dc-3f71-8e2a-1c20074e664f | -16.81468 | -41.22446 | 2025-10-18 04:32:00 | NPP-375D | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cff348e-bb03-3e1e-b1d5-def04e928bba | -11.60349 | -44.07277 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba76ccb5-a910-3f0f-b756-0dbd68e617a0 | -11.40278 | -44.27762 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed1a8b92-c554-3ad2-9c10-97300cd6bff2 | -16.58552 | -45.67592 | 2025-10-18 04:32:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6cc228d-7ac8-3470-a527-69564baa4279 | -12.15516 | -45.08422 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6a4d0106-db2c-3cf0-af0c-51385a6527b7 | -13.72698 | -48.11232 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb004b5e-69f0-39cc-b20c-046d6837797d | -11.48778 | -44.02639 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a482fd6-1534-3a7d-a433-aa5d396e6499 | -17.09114 | -44.09661 | 2025-10-18 04:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff0d55e6-685d-3092-87ac-ef900a92dbab | -17.84664 | -42.62041 | 2025-10-18 04:32:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c770c334-ca2c-3ef1-8658-dceb5c5b29c7 | -15.55706 | -42.34698 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bc88fab-a430-37f7-860d-0377e74d4faa | -11.37057 | -44.29171 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c12f64d1-7f2f-3a65-bdbd-603a45375ed4 | -13.44568 | -47.91972 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c9997b4-ce0c-370f-97bf-13fd6df569ba | -12.91294 | -48.58704 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25065104-4c42-307c-8567-c3344ec9e756 | -12.70039 | -48.62595 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33fdb8e5-d9f0-31b9-a98c-5b1fed2bd0aa | -11.35501 | -47.28376 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef87b85b-cef9-313f-9d9b-efe13654c775 | -12.96566 | -47.94273 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa49d017-8abd-3b2a-90ca-d497edfaee7d | -13.61636 | -43.95869 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e84b605f-db49-3d34-9f61-4cfe8a05b90e | -15.46681 | -43.20176 | 2025-10-18 04:32:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f081f456-d768-396c-a7b8-4dd619e15881 | -10.5329 | -49.54885 | 2025-10-18 04:32:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5cd7e2a-c71a-34d7-b95d-24cfa9830196 | -13.45731 | -47.93256 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c083182-9e1c-3dda-98a3-046140f9700c | -11.94269 | -44.24116 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a17441a6-e8be-3c79-b493-b452fc8042d3 | -11.36221 | -47.30297 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0f6573-6610-3b49-8c43-0afbf3203e02 | -18.39897 | -41.83371 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfb4a01b-9726-32c9-abe2-98762d110e98 | -11.00124 | -47.91225 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a67b43e9-aea9-3985-bf33-5f911517bac9 | -11.49086 | -44.23439 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7df0c09a-61f8-3f61-a691-f0ffdbd24c48 | -10.81159 | -54.6092 | 2025-10-18 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbe594b4-304a-383d-852f-a2167751242d | -12.99353 | -47.29656 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d83d2e9-8f37-3d2a-a29d-2ca69d1b9cb6 | -10.99968 | -47.87921 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43eeb39b-baf5-396d-b26c-6ea39b98639e | -13.61701 | -43.95399 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4138516a-79ef-3333-9c02-d1872c14d2fc | -13.4417 | -47.98823 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b6fa80-7053-31f1-bb5c-07a410dac64c | -10.827 | -47.84075 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d89eb14-b584-312d-96b1-8389a3245df9 | -14.94099 | -46.7074 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6cb95f93-9835-366e-bf11-cc48f8e1bedd | -15.5714 | -42.12917 | 2025-10-18 04:32:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86d62230-dfaa-3f0d-b6fa-77ca4dd138d7 | -12.65647 | -54.7773 | 2025-10-18 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8948a9ce-0aca-3b12-87b7-0c33b7f80620 | -11.48169 | -44.01651 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 734c0802-ba18-3b58-abb7-793bad6abd1f | -11.60045 | -44.06787 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e595844-b850-31fc-a27b-23632d3d1638 | -17.96065 | -41.97776 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ed58169a-0cd8-31c1-aa5c-785306e35baf | -12.65084 | -43.45186 | 2025-10-18 04:32:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ec56eee-7f4a-31db-a03a-f689d4f10dd7 | -15.4708 | -42.88435 | 2025-10-18 04:32:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82bec23c-0201-3963-9a3c-29873e17b8ea | -11.36771 | -44.26097 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe54f219-0947-3d0e-a7c3-a6f48ca5a0de | -12.60915 | -52.81771 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e4d6ae5-7427-3d83-882e-2782b211e121 | -15.78595 | -43.65135 | 2025-10-18 04:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0ff4b0d-0dd1-3b1e-947c-c1b1c6d6c282 | -12.3056 | -47.25919 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e78c4cad-9c0c-3161-90e6-d97ab95f3f15 | -11.20309 | -47.83325 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 318d9ec0-400a-3e33-8ae8-9316d6c3b4a2 | -11.36094 | -44.28161 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89d6fbbb-7422-303a-9c30-13e0082dc28d | -12.5919 | -43.01944 | 2025-10-18 04:32:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33ce3113-29b7-3d58-a008-7e946d9ab41d | -11.37545 | -45.27156 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61f138d5-2e95-3046-a768-5c355dc0b5ca | -14.93702 | -46.71065 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e661448c-2caf-3c10-a1c5-4c05561b9603 | -15.09283 | -44.00251 | 2025-10-18 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b26e761-ed66-3fd9-bbc0-7cd7366dafc1 | -10.99911 | -47.88276 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README64.md)
