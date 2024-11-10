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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ea0bfb-193c-3d8f-9258-5804abe3a40b | -6.22242 | -55.64408 | 2024-11-10 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25b03e87-664c-318f-88b2-b932f2141ea5 | -4.34792 | -49.82185 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39e197d2-d810-3331-b235-7c561384d5a3 | -6.28755 | -47.35057 | 2024-11-10 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cfbfeb0-a20d-3cf7-83a7-5f2bd8bee474 | -3.05659 | -48.03605 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c181e8a-3c59-3712-a1cf-08164c763635 | -3.42364 | -53.0553 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f99492ea-b070-339d-a884-54c639238631 | -8.38398 | -44.14174 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae976f9a-93c9-31e3-9462-5f6087c716e1 | -2.15882 | -50.51185 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27d50bad-7e8c-3c3f-be15-0be1b989b0f3 | -3.74783 | -49.89796 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1740611a-e1c6-3a3c-a581-fe97d90b0fbc | -3.10567 | -53.33125 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13438480-352c-3a6a-bcd7-6338216dd78d | -4.41461 | -50.08569 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee2e725-933b-30b9-b7d7-b4c04fa154bf | -2.4269 | -50.41053 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91adf739-dbcc-3e27-b9a1-b59e05c283d2 | -6.46301 | -40.78038 | 2024-11-10 04:38:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc95d684-8492-3542-a968-dfb4dbe1ae07 | -3.96194 | -48.12686 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71a67b27-fd75-3ec3-9ae5-1b41e06fb722 | -3.95241 | -49.39787 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63cd1839-7b8e-325d-95d5-3934630f7274 | -3.23235 | -45.38387 | 2024-11-10 04:38:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0341c40e-20d9-3103-93a3-0509a6b1fcd9 | -3.70208 | -49.64496 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75ea167c-9277-3273-8450-bb103df3fbdd | -2.1144 | -52.12319 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06576296-dcbd-3c64-936d-8901cdbcd6e7 | -3.0694 | -53.90702 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec516bb6-8cae-3445-95b7-5ce40fef3693 | -4.23973 | -48.0197 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7732adb2-d235-336d-8c8c-650d4792460b | -4.56099 | -49.37947 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d338b42-f4dc-38ff-bf1d-2f381cf9300c | -2.14631 | -50.7678 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1eaf5d69-3e0e-306a-93cd-9e8da25f070e | -3.75562 | -51.01507 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c77b76e4-a98f-3397-a15b-fd2673953202 | -3.96656 | -48.18459 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5c131d2-efdc-3c53-9cf2-9b0600890cb2 | -2.94706 | -49.5053 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be17e75f-8902-3ab2-8529-48864be68f4b | -3.08999 | -51.11637 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e384b38-f53d-3b44-b0f4-db415085fd9a | -3.3616 | -49.68901 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4735fb16-c6ba-3cf4-a609-73075c9c31c4 | -3.26505 | -46.31728 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03a87bcc-423e-3602-8621-1649bab4421a | -3.02451 | -51.00727 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53072e4c-519d-3064-81f5-2d31a0620a1a | -4.12689 | -46.9263 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8322ce5-03b5-33f9-a17d-3f034293604b | -3.15403 | -51.30318 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 018ce533-7312-3c75-b0ef-bea9c310b683 | -3.9565 | -48.16164 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e65ef240-a68e-3215-aeee-76ab694fde4c | -4.20695 | -48.03255 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d092a5-7cfa-32ed-8246-8c71f22681f7 | -3.21858 | -50.28695 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38085279-10e3-3180-abf9-6362dbf89ca0 | -2.73788 | -51.89488 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d410990-1f02-344f-8983-4043c5b92bbc | -3.23625 | -50.2636 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39a4d676-9152-385a-b823-b6772de9dede | -2.91973 | -49.50462 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99ee6658-daa8-3e30-87c8-e110b778a42e | -1.56716 | -54.58512 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ef377ab-fe54-34ee-9757-c4ee8224fb17 | -8.84958 | -47.70164 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea714665-2062-3f46-b7dc-626560e08629 | -2.9106 | -49.23814 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 009a86db-1630-33c0-b4e5-3666ba520b18 | -3.61826 | -48.93702 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96f6f84b-c9c4-3146-a96a-c7ce07ade3e2 | -2.15728 | -50.50838 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a01cd87-bfd4-3f9c-b1a8-22e8064accf4 | -3.34955 | -54.12403 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8e2b677-1e8c-38be-a97d-f0ff610f1ce8 | -2.97133 | -49.35122 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65e2fbf7-dbf1-33d9-99fb-a7a70e4ec231 | -2.86964 | -51.47484 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83052e6-8af9-3108-a048-008c0fd1d7d6 | -2.68008 | -48.64175 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed807ba6-e219-3ec9-8f30-b75446c1b433 | -3.96812 | -48.99577 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1ca73cb-3dfb-3831-bb86-20be1fdfc8d9 | -2.21335 | -50.77439 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e06c4b88-895c-3cf6-8a33-ed9489e98ca3 | -2.6439 | -51.87759 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78feaa17-e14b-3c15-afc8-1898b52917de | -3.14759 | -54.48338 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b602c72-922d-3651-95a9-dfbfe36ce9ba | -2.23365 | -53.7881 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1486e057-059c-30fa-843a-37fc1da4c620 | -3.59993 | -50.23849 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e23bb502-71ae-360a-b804-28ba19482ef6 | -5.46307 | -48.30622 | 2024-11-10 04:38:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a4a1ed-a415-39bd-94ba-dfe70aa6224a | -2.86232 | -49.27 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0638b936-17b8-3c03-8d37-83eea89cf7fb | -2.06826 | -53.2919 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30738019-c8a4-33d3-a37a-56c53b80cceb | -6.31567 | -44.27892 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 573142c5-7f7b-3188-8907-0213467ad145 | -2.23304 | -53.79188 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fb0fb03-333a-317e-9280-e923e0adc4d4 | -3.07182 | -50.57455 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b71a370-5db3-3858-a03e-dc3c294dea66 | -3.52875 | -49.98013 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3aacaea-2926-31b0-901b-8fe90d77a3ef | -2.83847 | -49.82179 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e613d0a1-1889-300f-890b-8bc684f2ae14 | -3.21575 | -50.28276 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b0d0804a-5501-3a17-a028-31d84e5ed6e4 | -3.87316 | -51.98199 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba5d90cc-57eb-318d-b62e-fbe2cbf49366 | -3.95542 | -48.16858 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f44a85f9-821d-3b15-ba39-8795f1710c2c | -3.62352 | -47.52085 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaea563d-9c63-3098-aa9d-15b18a49206d | -3.55361 | -49.98444 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe1662b9-0238-38dc-92d2-3da13af7ee46 | -3.16732 | -49.09297 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351b1926-cc4d-3f38-93c5-9b288c27060e | -2.75576 | -49.14933 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06c38d13-f601-3b08-b8e3-1d48deac9931 | -3.34417 | -50.35498 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1f829cb-09c8-3302-960d-2899075e1e1e | -3.2322 | -50.28909 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f4a84195-806d-399f-9165-d18e40f21b6c | -2.58691 | -48.20367 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e069244-f510-362b-980a-a414c0955295 | -2.62075 | -51.29771 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30cb2023-5357-31f0-ad26-0e957a113b4a | -2.92307 | -49.50514 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fbc87e1-e0e5-3604-a525-4dd26c859551 | -3.52525 | -50.53405 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b68282fb-875d-34f6-9f6b-c4ef8853a29f | -3.33457 | -52.12585 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4eaba05-cd94-39aa-a535-6df95a77fe46 | -3.6161 | -51.21174 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b627e6ac-28ef-3121-80dd-22c255cdcdfc | -3.48533 | -54.58603 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dff22649-24dd-3914-b5f1-cb5d47728a8e | -3.32825 | -54.17545 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aae8b23-6eab-32e5-bb2b-3b7f8bade32c | -4.18501 | -50.4261 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c2dcd72-aeb8-3b79-b7c4-d31e3b8a1744 | -6.45159 | -42.74422 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87f40aee-b3d1-37ad-98ef-a2a612c18cc1 | -4.38069 | -48.17438 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f15d9f0b-5598-39c2-8981-ac6d3baa1f44 | -7.9758 | -50.03485 | 2024-11-10 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75bc9663-2395-3bbf-9e36-d5b75455d6b3 | -3.19639 | -50.29469 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4851d741-e493-3020-96f9-8c9b4fd8ab1d | -3.45227 | -51.60302 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 439822c0-3c57-3e62-9e7e-9694bae367ed | -3.61766 | -48.91925 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d2797ef-d936-3a28-9ce1-73ffae1ea062 | -2.48808 | -48.80981 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ee97d18-9923-3784-8845-80eddbc9e2d3 | -4.37142 | -48.58176 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2294240d-9473-3003-86b8-e0e388305e7a | -3.95643 | -48.14027 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b04c4d47-140c-33ad-812f-97d90a1e55f3 | -3.01422 | -47.95841 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7d74d5d-2eb6-3107-8e4b-20125ab6632a | -5.13686 | -47.7085 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23325489-d7a9-3e70-8272-4c1710b272dc | -3.02345 | -48.07351 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cefb61e-0358-3cca-9d83-875e70ef1d47 | -6.27301 | -44.53943 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 700a9770-1a8e-39bb-853b-fde19dc8b01d | -2.94202 | -49.49372 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70ef3cbf-6932-394b-9456-1f6952c37aaf | -2.91864 | -47.85401 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c90ab6-b0bb-37a5-9654-c037bfd9fbda | -4.05849 | -48.3127 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d94dc6f4-f728-3137-9c19-cced5ef89eb7 | -5.94513 | -44.76125 | 2024-11-10 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14388a83-94d5-3a22-a63d-9ae9369247c5 | -2.46425 | -50.39734 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac93adc-3bdd-3a71-9a98-bb557b33c555 | -4.13086 | -46.83975 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6da2f8e4-b4be-3261-9e88-32effa73518d | -3.24745 | -46.47809 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97004523-5154-3a7d-989e-efeb08a8be19 | -2.3071 | -53.81854 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c68ac6-c30a-32c0-a71f-9868b2a094c1 | -4.27645 | -48.19358 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a026ded-3f9e-3243-8c0c-032ab8dd433b | -2.21866 | -50.76339 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README102.md)
