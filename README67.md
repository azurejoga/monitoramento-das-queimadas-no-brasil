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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25a8d7f9-3e60-3144-9991-fed63ffd1dc4 | -13.08609 | -57.12455 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71e3453b-d05f-38c9-bf05-13fe274c175c | -14.78275 | -48.13758 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 067ecbda-bbd0-3bdb-99fb-21e11a1f6c85 | -11.09557 | -52.02554 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3ccdcc4-8520-3c19-8a54-176357a373fa | -15.58293 | -54.31902 | 2025-09-04 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6f6af99-6398-3dd4-9dd7-8274ad7720a8 | -14.59688 | -48.02398 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a09988b9-a7a6-3c25-b217-c14f7cde2415 | -12.90058 | -48.03824 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81417d62-3600-30e3-8ae3-1860857b52fe | -15.0455 | -50.07747 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac09909e-0b91-317e-ba19-4d277773e8c6 | -14.56803 | -49.13897 | 2025-09-04 04:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d47501c-11aa-3e65-a931-88153862f72a | -10.70252 | -49.02132 | 2025-09-04 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e555cffe-c1ef-3b9e-ad42-b618d9ea0721 | -10.4977 | -53.64808 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57dacf93-dfc0-30b1-9fcb-929021c78e3a | -11.31724 | -55.22443 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f2faa1-9699-3895-ab1b-82e23ddd0de9 | -11.20879 | -55.07389 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca03f883-b4b5-3418-b1b0-dc0051583792 | -11.73045 | -47.74649 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4cb3968-c93d-3135-83bb-dd27392f63dc | -13.43893 | -46.92883 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37fc734a-27f7-3280-9e65-63081bfca0bf | -11.58539 | -52.10736 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be097a90-7bbe-3908-93e7-b200c6a8f3b8 | -18.56377 | -44.02874 | 2025-09-04 04:55:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d0deef0-4493-3a48-aaaa-91a5ecfe7b44 | -14.81559 | -48.33087 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98be0a55-b6ad-3a0c-ab50-ad35b40f7fc5 | -12.50005 | -53.83846 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78598358-3685-3f40-a309-8e2b9ad36734 | -11.58887 | -47.75929 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a1eb019-49e3-333a-bd30-e6b2c25058a8 | -10.46057 | -53.62408 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d77c50-a7f9-339f-be57-c5c71b6b7221 | -14.5936 | -48.01442 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88cf7e8c-3d5d-3187-b9a7-6c392e7af13b | -11.67671 | -52.17027 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b48fc8a-debc-357d-a097-897e820396f1 | -15.17508 | -52.39031 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eb992c1-1710-367e-b48e-d60d3b49653b | -14.75235 | -48.13501 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6010baf-cab0-3933-affd-89f029257548 | -12.91639 | -56.93043 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d3846cb-eb6c-3b60-9cf0-970fa27a5f5c | -11.8578 | -52.42424 | 2025-09-04 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94f20e2f-443c-3ddd-8bb6-4a592be84757 | -14.58572 | -53.02724 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f00236c5-984a-3fa1-9a1a-063c049922a2 | -14.81319 | -48.21308 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0776a99c-1574-37c9-83b6-f20e8d4eb4f3 | -15.60736 | -52.88523 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d4e1d3a-ad79-333a-9771-5a5e00a2a9ed | -10.47055 | -53.62569 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb59857-d010-3ed1-adbb-8ac92ecc8c5e | -15.46358 | -53.00586 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fcbc986-93b7-3f6a-8520-9371b47724d7 | -14.57556 | -53.02562 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b23fce8f-caef-3829-8c18-128b2638f7af | -11.6314 | -52.19344 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f04745-7c70-3f20-b80a-ab01c3013432 | -12.48895 | -53.8439 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 765803eb-e763-3dec-946a-e6d0b21e2d4b | -15.61877 | -52.87928 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06f7f394-8bf3-301f-bd78-103dd54b37a1 | -11.53383 | -54.49078 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8c03b74-0980-3c5f-8e27-b7d2075ec08b | -15.75541 | -49.97748 | 2025-09-04 04:55:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51026ab9-6de1-31b1-9f04-a042b7d441eb | -14.56345 | -49.14205 | 2025-09-04 04:55:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf7680cd-12ca-3eb9-80bb-29b3ed607cb5 | -15.2476 | -53.8027 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c1b5a28-328e-33bd-abe9-84c638a667d0 | -10.48163 | -53.64188 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 902430e7-780d-348d-9ea5-8b7aedcbd8e1 | -10.46722 | -53.62515 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a951744d-4dd0-38c1-b54d-1c255bfefa8c | -17.17889 | -46.23071 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28cf0011-f3ce-354e-9b95-b1dfc8732bf8 | -15.17968 | -52.38316 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4dae212-718b-3e19-81f3-83399fe16464 | -14.77968 | -48.13086 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78c0915a-13b2-361c-b322-093a68616ef1 | -11.88474 | -51.53211 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cec0cfa-5f64-3306-93dd-41368d0c50f8 | -15.05592 | -48.36627 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c8f00ca-c8e9-3840-b5bb-0729d207e790 | -11.63877 | -52.1908 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7b41f83-f001-3054-a77a-3a342925af69 | -11.733 | -47.74467 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67d86180-01f3-3e65-a42d-d6c94d76fabe | -13.8101 | -56.57393 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483daa0b-0286-398c-b5e6-f4e5118ba0e4 | -14.57351 | -48.03889 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5bedbc6-c415-3793-bf78-3ccb59a046ea | -14.90338 | -49.6279 | 2025-09-04 04:55:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a58cdfe4-f09f-3bf8-af91-8f7b70dc9a4e | -11.7778 | -47.3266 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26858eeb-bf90-3803-9b24-b30d6b04d896 | -12.48382 | -48.08047 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 972ac4d3-c7b6-3d65-b7d2-99364292f9e3 | -16.55453 | -55.10751 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9286594f-9816-3163-88fc-da22396ee434 | -13.30985 | -51.76742 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a3a8454-c6e1-342a-ab15-852ff9929fb2 | -11.23884 | -44.96231 | 2025-09-04 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa1d39a9-1032-36ec-837f-2f1a437d9601 | -15.73825 | -53.63392 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b335289-b932-3383-bf5e-66620921c94e | -10.96825 | -49.74755 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c312203-620b-368c-866c-4555d4185082 | -10.97069 | -49.75725 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c0dccb3-5d3a-382b-9f8a-508a3f3d5906 | -15.06177 | -50.04638 | 2025-09-04 04:55:00 | NPP-375D | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 072e955d-68c9-3721-afe0-918d5be87648 | -11.68357 | -52.21671 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dea71bd-1568-31ef-9380-3657c0e9be8c | -14.58863 | -48.01825 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7ef4f7b-57ea-338c-bca6-7f55817066ea | -10.09435 | -54.77274 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c8a9d55-6de9-3c84-b843-04bfdebce03a | -10.49438 | -53.64754 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad1dd3c6-0682-34e4-b0dc-ebcb1ae6d43f | -12.48604 | -48.0641 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c645f24-b60f-3430-9b47-5377c7e32a9e | -13.44149 | -46.9314 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8676a038-2384-395a-a9eb-293200b19ea3 | -10.49493 | -53.64403 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af33dcde-88ab-315d-8528-5d7973579425 | -14.78768 | -48.13392 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e0c9364-e21b-3816-8a85-2f145d32c218 | -15.56772 | -53.96203 | 2025-09-04 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 619afce5-69f9-30fd-9635-c7aaa044e063 | -13.50813 | -50.80911 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd70a461-cd76-3b4d-8f0c-da9a748d3d0f | -15.30636 | -52.75395 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55fee7ee-4b40-3843-a511-d583154fa72f | -16.30928 | -52.96389 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5914bdd0-fff2-376a-ac00-9a9f247057b8 | -10.98881 | -49.76463 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43b9d1d-6baf-3507-acce-d38a17849f5b | -11.88242 | -51.54762 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 784aec9c-a509-31e4-bc9d-67f6c51a908c | -15.54909 | -48.38391 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9afa37f4-a6e0-3626-a246-1029971cbd97 | -11.96207 | -45.77703 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2afc0cee-995a-3d27-b0ec-c7e345cc3ad0 | -12.97307 | -54.77534 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daf74f19-ac3b-3def-baae-d71a6a7f6522 | -12.49172 | -53.84798 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 248cc17f-6835-313d-91d8-b91135eff809 | -13.9956 | -49.55405 | 2025-09-04 04:55:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f18683c-48bb-3898-8afe-cafb8e9bfb25 | -11.64329 | -52.18391 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e774b5f-f44c-344c-ae7e-5e751e83f393 | -14.5829 | -53.023 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38e4a6ea-6496-3648-af26-27c7508d7616 | -14.81941 | -48.33534 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 48895137-b0e1-38f3-9850-53ea861420aa | -12.45764 | -48.0815 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1c5c96d-ad81-3428-b0d6-c99c1d1a072f | -12.86237 | -48.01704 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21b398f0-f2f4-31e0-be10-729174269a63 | -11.58483 | -52.11107 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 18a9ce55-4957-3c11-b7c1-70ad4860ed84 | -12.48951 | -53.84036 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d37ec1-b650-3e24-8a5e-f6be3081acce | -15.04749 | -50.06324 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d00404ca-da59-37eb-94e4-f8216659be73 | -11.64613 | -52.18814 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0219607-f87a-385b-a4ed-01780245a90f | -14.78381 | -48.12917 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37e91be8-440e-3912-afb0-a490af537fe4 | -17.16894 | -46.22625 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00bd68fa-c2c7-3c59-87aa-6aaf8d33bda1 | -11.19686 | -55.01929 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f946cfce-4db9-3e5c-ac57-b44814fc8de3 | -14.21074 | -48.08033 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 093359b5-6ed7-31fb-ba88-328680cfcc21 | -14.81809 | -48.2096 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84ce3a88-bcbd-3658-8373-406f4075546f | -11.59464 | -47.78086 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c3817ae9-f738-3632-970f-cc83666bb0fe | -11.865 | -51.52111 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bbab71a3-2ed6-3563-a79b-6960979e6fde | -15.30694 | -52.77343 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c06422-4a41-3a42-8583-934a00fef816 | -14.58808 | -48.02266 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 595e99bf-d38f-32c0-b30d-1710ccac5e06 | -12.89681 | -48.03362 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a15689d-a426-302c-93b9-44f164e9bb27 | -12.494 | -48.0695 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a67f272-e130-3a78-a1a6-ec6a7150a711 | -11.59857 | -47.75253 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README68.md)
