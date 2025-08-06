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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0c45315-eb5f-39ef-8d55-6ea94caa59fc | -12.9931 | -44.89326 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d646e3a-204a-3ef5-8a4c-6070429d257c | -12.71975 | -48.08101 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac4d22a5-2a59-36bd-a742-43c614fe1214 | -12.66395 | -48.1219 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 584faaad-78ab-3bb9-a901-363d4de71e00 | -12.71634 | -48.08045 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4eb99a5-d3ae-3672-9645-113b4a37f010 | -12.99928 | -44.89795 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b892c3-99e9-3337-a0e5-c226e3093006 | -13.69319 | -50.76811 | 2025-08-06 04:21:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5c59af-0b81-35da-8923-abe5018a54fe | -12.66859 | -48.11502 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de1ddde1-7a84-36d4-b5bf-20c637b6fc8d | -16.34046 | -50.34892 | 2025-08-06 04:21:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f69bd18b-e64b-3ef2-affb-6133af5379b2 | -16.3433 | -50.35398 | 2025-08-06 04:21:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9bbf7e1-fa14-377f-98a3-8ff48e0ff139 | -16.33687 | -50.34823 | 2025-08-06 04:21:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e4b7866-296d-314b-aa37-212628a44c4e | -15.3394 | -49.75274 | 2025-08-06 04:21:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b44076f3-93ed-3ee5-9218-5053c883c573 | -10.22034 | -59.41996 | 2025-08-06 04:21:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f21d9a9d-f18c-316b-bc1d-ade879f03718 | -12.66177 | -48.11385 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9231e9d7-edf9-3ffe-8978-61db793cb0a9 | -12.53437 | -47.17131 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68a0fbce-884e-33a4-9368-3c4d26c8e14e | -12.67633 | -48.13185 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ec36e0c-8d0f-347c-b252-0b2d53258a3f | -12.65495 | -48.1127 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b46caca6-856c-39c0-bb98-bd89f6bb45c2 | -12.983 | -44.89167 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e67fa065-4eb9-36e2-bf44-5c4f3f170179 | -12.71233 | -48.08356 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5d6bd9c-34a5-349f-80a6-5d3e97573be2 | -12.97456 | -44.87905 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3fa80f1-40a5-311d-be66-8a410e313826 | -12.72595 | -48.08591 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f25ace2-cc8a-367b-9c6c-ba649f914223 | -14.71094 | -47.85715 | 2025-08-06 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37290cd6-6cc0-333b-a4ea-6cae912d7ed2 | -12.65432 | -48.11649 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb12a54d-3a03-388d-8be9-1dac7b92c4bb | -13.05097 | -56.86338 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a3d4b01-687d-326d-b94b-f96392825274 | -12.70952 | -48.07935 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3d5216f-062a-330e-b6b9-01b0892e2908 | -13.49695 | -47.73166 | 2025-08-06 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1838fe2f-77ed-3294-ae32-a36186566137 | -14.79002 | -42.43816 | 2025-08-06 04:21:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9242f95f-ba8c-3f75-a0ed-50af65e38a63 | -13.06318 | -56.86174 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a69d5b08-06c9-3885-a977-be41c3787e63 | -12.66518 | -48.11444 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f92e2f07-12c5-3584-9313-c8e7402384ea | -13.07453 | -56.86436 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a22e0521-3982-36fa-b68e-c63b16773b7d | -17.83197 | -55.10402 | 2025-08-06 04:21:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c128cf42-d831-355e-92ae-a6efd8c25d14 | -13.06807 | -56.867 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8fefa938-b4b9-3367-bc6a-f9a48a0065bd | -18.84374 | -50.13261 | 2025-08-06 04:21:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef8a1122-e8e2-3ef2-b3b8-fd6f0fb9b53d | -12.97064 | -44.8822 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b80cca4-1fd5-3973-b010-39e3496f0e80 | -13.06238 | -56.86571 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 18615758-4b36-3fb9-909c-0bb370077401 | -12.53713 | -47.17546 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62b58a94-7820-3621-a904-e153993f7e3f | -13.04365 | -56.87025 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c51ded45-9303-3788-b7d2-9225f3a67b02 | -12.98973 | -44.89274 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a560f2c-9119-34cd-b062-38d34c290ea4 | -14.71153 | -47.85352 | 2025-08-06 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f6af384-1321-3c1f-9bbd-b9e695c9b17d | -13.8604 | -44.12582 | 2025-08-06 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dd2b4d4-1d8a-39fc-829a-e18b9a34bd25 | -12.97682 | -44.88692 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 417c486c-5e15-3074-b87e-38948cbd9be4 | -13.05017 | -56.86735 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68af1a01-b6a5-3e2f-b9f9-967672ed570e | -12.98692 | -44.88856 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a88615f-6117-38b1-a345-e20e40276fef | -12.72315 | -48.0816 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c38329a-9ce1-3550-83b1-164761c9c076 | -12.99647 | -44.89378 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e769cd8a-da8e-378d-9126-d65937413212 | -12.97738 | -44.88325 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 378dc923-a37c-30b2-8b94-b19578a039c3 | -12.71675 | -46.39003 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af6d10d8-7c25-35a5-a991-d6427795b474 | -12.99422 | -44.88594 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b94d9df-b9ec-3c5a-b302-c6a7e6a0714d | -13.04937 | -56.87133 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c2793fb-f00a-36c0-beac-8e1279e9e5e4 | -12.51769 | -47.16858 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ce784ea-9eb4-33ae-9bbb-10705dc4574f | -12.7146 | -47.79385 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77a9c75b-14c7-3c57-955f-dadecbe77571 | -16.25289 | -39.04893 | 2025-08-06 04:21:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ef52ce1d-091d-3f1a-a4ed-9e9eec3eb249 | -13.07294 | -56.87235 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eae8a410-c789-3ea7-85e0-7e3de3969be8 | -13.07374 | -56.86835 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 63f6b617-4661-3f02-889c-5157181dab63 | -12.72998 | -46.3922 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68449211-9aa0-32f4-9ffc-501111906b8b | -12.52378 | -47.17327 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9ab2b0a-8091-3599-9844-680471f5d090 | -12.52102 | -47.16914 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38c01fea-d07c-3120-ad8a-77a7be41f4e3 | -12.53771 | -47.17184 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29a75754-1094-3f35-b6e8-b1f1605f586c | -16.72706 | -49.40315 | 2025-08-06 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c7f8c4b-7123-3e1a-a100-69512eba34fa | -12.72934 | -48.08656 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba0fc41a-1556-3805-b48a-66c7a07c1f5b | -12.52436 | -47.16969 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71ad3d51-d656-33b9-9370-0342f32c3747 | -15.70053 | -48.96969 | 2025-08-06 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ad4b5f-549e-3402-bccb-1730d1fbd2e0 | -12.65773 | -48.11704 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba7dcdbd-3616-39de-8b54-16adaf660dff | -15.69022 | -48.96811 | 2025-08-06 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56611e38-48e5-30a2-9b26-17a176d6af95 | -13.49634 | -47.73534 | 2025-08-06 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d41958d2-5a0f-3123-a9c1-80e4827be254 | -16.79902 | -48.95176 | 2025-08-06 04:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7bc80bba-9dba-3b8c-83f9-268968cf19b1 | -12.97119 | -44.87852 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71638b67-14da-3a23-9cc7-bc2f7de19782 | -13.05589 | -56.86846 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9891b468-9407-37ff-981a-424a591a4060 | -15.70916 | -49.79886 | 2025-08-06 04:21:00 | NOAA-20 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2066160d-38e7-3869-b61f-8e01cb4a3638 | -13.65107 | -47.60056 | 2025-08-06 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 085cdf7d-38ce-3c21-a365-f7e142a36c31 | -12.72723 | -46.38813 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22899134-6015-3f52-9b0e-4a63fdfda6c4 | -12.672 | -48.11559 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b632e24-8fff-3687-b6af-e40fc82d3590 | -13.05749 | -56.86052 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 498edd50-e120-30f7-a0b5-215f39b538aa | -12.73273 | -46.39626 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cba4871b-c3fc-35cc-adfa-29538ee28593 | -15.69366 | -48.96859 | 2025-08-06 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9dab2e5-632e-3f3c-bd1c-064b7af6d6da | -13.25612 | -46.99436 | 2025-08-06 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f145c9b-3b30-30f6-b5be-31200e42e4ed | -11.32082 | -55.22648 | 2025-08-06 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cd96060-6615-3eb6-a014-01ae1da5d7c0 | -13.72552 | -53.16616 | 2025-08-06 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 335c4e55-a6ec-3240-9b78-9739b62f1f20 | -12.99591 | -44.89743 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94397c63-ee83-36c3-ab42-00971baf4ad5 | -12.70209 | -48.12457 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af8ffe9-0d12-3375-b002-0cdb9911633a | -13.94601 | -54.07141 | 2025-08-06 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a8446c8-0abc-3343-a520-cc59bfb5feae | -13.65167 | -47.59686 | 2025-08-06 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40396a3a-f8b1-341e-bf33-5e3662dc937f | -13.04283 | -56.8743 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed68abd-31ca-38bf-aa60-08225b53da99 | -12.54046 | -47.17603 | 2025-08-06 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d5ac302-3e84-31f0-8f0c-2f30c933002d | -12.99366 | -44.8896 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b169f0f2-e1bc-34fa-b327-b220d9a369aa | -12.71564 | -46.39708 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4fc781b-28f0-3e05-bec6-f755269bc28a | -12.72392 | -46.38759 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4597da81-19cd-326d-af0c-fdef7d88b8ff | -13.06079 | -56.87368 | 2025-08-06 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c98eaf4-8531-318b-806b-5f59070388ef | -16.34406 | -50.3496 | 2025-08-06 04:21:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b2a6001-70cd-375f-b300-d8b1680ff514 | -12.71344 | -46.38949 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c98da74e-183c-3cb2-bded-d3c917cdaedf | -12.65836 | -48.11327 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46661280-7992-3048-9dd6-56d3014d8cd1 | -13.82494 | -49.37673 | 2025-08-06 04:21:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53613700-358a-32fa-871e-e3feb4d26a90 | -11.37572 | -54.33338 | 2025-08-06 04:21:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7273fb3-ff71-3f68-bf46-21c8f5858cf4 | -13.94131 | -54.07055 | 2025-08-06 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3ea260e-33f1-3d9a-bb6e-258694361c4c | -16.25355 | -39.04337 | 2025-08-06 04:21:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c3f20ac4-7be6-3438-a93b-461bd3911637 | -12.73054 | -46.38868 | 2025-08-06 04:21:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a4afa9-fb34-3b2a-9129-b2d21d114305 | -13.93661 | -54.06966 | 2025-08-06 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c6d317c-7fe1-343a-86ab-880c17962d7d | -12.6509 | -48.11592 | 2025-08-06 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9afa57-4043-34bc-a2c3-b64be47c79d5 | -12.99029 | -44.88908 | 2025-08-06 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db1f47af-0fda-3722-ba22-64213d9427e0 | -11.32209 | -55.21979 | 2025-08-06 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d55f1bf3-8b7d-3d52-a6e7-d3a218a810bc | -13.76327 | -42.57592 | 2025-08-06 04:21:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
