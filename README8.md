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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e31a7721-55a8-3df2-a755-39ce3d8f4825 | -11.0524 | -55.7649 | 2026-06-30 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ab49be3-f551-3797-add6-382c31520569 | -10.21697 | -42.50637 | 2026-06-30 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a85534e-44e5-342c-b77d-f94f56ff7f53 | -10.94553 | -43.03992 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| cebc95d0-58ed-361b-858e-8776b12eaa3d | -10.94262 | -43.03544 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 662a9a81-c351-331c-9221-6279f13e8af5 | -12.45307 | -58.48932 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed41a18e-7cc6-3a6d-9ffd-f86b9d0927db | -10.55108 | -56.33927 | 2026-06-30 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c2c2ad1-e942-39ea-ba33-8c6060115866 | -14.20393 | -57.43627 | 2026-06-30 04:21:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5fd3248-2faa-3bd7-baa4-fd9ffe6beccf | -12.51113 | -48.27063 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 32f871b2-0f96-3504-8b5d-a41997152e70 | -9.81566 | -46.47279 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a29772f-3943-3487-94b0-8df11125deda | -13.93338 | -53.94093 | 2026-06-30 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bdcc043-eb11-3cb5-8ea8-bb774246e567 | -12.6085 | -57.89274 | 2026-06-30 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28902ff0-146a-3ab8-aa66-a59fbffaac2d | -12.44543 | -58.49375 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1200dd82-2158-3e40-8076-976b044afec1 | -12.52176 | -48.29234 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 969b7bfe-d4fa-3967-8214-936feb62fff9 | -11.21559 | -54.33693 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547759ef-3320-3984-949a-35097ab1209f | -13.72246 | -47.86816 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31851c2d-69d6-3f1e-91ea-d8764df36d4c | -10.29051 | -47.59639 | 2026-06-30 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca171b8b-c20c-3dd8-85a8-f0d1894c5345 | -10.93504 | -43.03835 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8239f348-8e9b-3219-9097-61444b1af5c4 | -12.44663 | -58.48798 | 2026-06-30 04:21:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 549f5d5e-45fb-3261-98da-935c27ef7f26 | -14.24656 | -43.16223 | 2026-06-30 04:21:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b089500a-cf31-3d2f-a462-1c598ab81e81 | -9.15658 | -58.29407 | 2026-06-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11a8f1ea-979e-383f-b094-011e468ba061 | -12.85083 | -44.39439 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a92169d-5f47-31dc-a3ab-334ecfd57d7b | -9.32497 | -58.01908 | 2026-06-30 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5f5aa25-f3bb-3f42-b031-4f47a98b6beb | -13.25664 | -56.79309 | 2026-06-30 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23d0fa9a-f297-3796-a24d-813b2e93e17b | -12.27057 | -51.4193 | 2026-06-30 04:21:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 628f0a9b-38ee-3224-bc83-1c52c03f602b | -10.77259 | -54.10983 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4d4d068-6085-3c69-a9c2-17c1d653dc47 | -13.2418 | -51.56879 | 2026-06-30 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c18861da-8eaf-3fca-9c13-f6eaea900152 | -11.89204 | -57.12492 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0d83dee-11ab-33a4-a234-026e24cf8ee7 | -9.4492 | -50.84058 | 2026-06-30 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b25ad1a-6d69-3a04-8378-e020ae239062 | -9.75103 | -49.02659 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dd4cc9f-fa2c-37e2-9e68-6ad1c372143e | -11.89625 | -57.13512 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d7d26bf-fcdc-301e-9b93-c410222bd359 | -8.70942 | -50.71304 | 2026-06-30 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fa22eba-f13d-3dfe-affb-5362f5c2cfb9 | -10.78285 | -54.10533 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 202bb7a1-7470-3b61-9cd1-7c3fa949a194 | -12.84926 | -44.3949 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53708a0a-dec5-34c6-ae6f-cca72fbbbb71 | -12.20059 | -52.86814 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d57addaf-2d73-33cd-9877-f4f87737aa0f | -10.93096 | -43.04176 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 887a0d35-8c16-35c8-a87d-7e4c9a094afc | -9.81623 | -46.46923 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20da29c3-d6da-39a8-86a6-d013071d1f7f | -10.9043 | -56.85685 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b74d7f59-7d49-35d5-82fd-93e77bfd903b | -10.78229 | -54.1083 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5154d13c-59eb-385a-a522-8ca44eea08d7 | -9.60673 | -56.93387 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b56b3dfb-12db-34f7-ac0d-c8841ff37c0a | -11.88603 | -57.1238 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01c7a602-e970-32c3-b69b-4f79d2ab7c02 | -9.14864 | -58.29892 | 2026-06-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bea8bf0-e89a-3071-98ba-0ce930cf4a06 | -9.60595 | -56.93366 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ac2b9296-5ac7-3b60-b5c3-a06071497fd4 | -10.94495 | -43.04387 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e84434dc-23d8-3668-91d1-9c448965838d | -11.7669 | -47.33986 | 2026-06-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8ccca4-ec10-3d50-8a84-196d1d571d7d | -11.89116 | -57.12937 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| add53a08-48ac-33e9-a646-90e7fadc2771 | -11.21671 | -54.33095 | 2026-06-30 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be201567-7073-3909-ac57-a374609e0e09 | -13.71448 | -47.87466 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7a9cc2c-9e6b-3121-bd84-652ab2df2de4 | -11.78456 | -47.57382 | 2026-06-30 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6025be6-0b2c-3b19-b4d1-f6c795efa1f3 | -10.69475 | -49.61089 | 2026-06-30 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0c033417-fdc0-3027-86c3-52d1a6e64988 | -11.93306 | -57.7095 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 797d4913-0ab4-37f2-b052-a47f5e604704 | -10.90909 | -56.85294 | 2026-06-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c4a4f0b-309c-3bae-9392-ebe5736efc27 | -10.12901 | -52.40412 | 2026-06-30 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e52df07-3677-366a-861e-bdbabc408127 | -10.93562 | -43.03439 | 2026-06-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2a4aff1a-cb2c-3099-aba2-30dd40aca378 | -13.70773 | -47.87354 | 2026-06-30 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bce7068d-bec2-34bf-8c9f-32f99286272d | -14.27783 | -47.41732 | 2026-06-30 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50a777ce-d8f3-3221-b855-a00d29bf3607 | -14.6311 | -54.46492 | 2026-06-30 04:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc756e87-dd3f-38a4-9885-482518c836b8 | -9.60337 | -56.91785 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 967493a3-4f16-39c4-a19a-5220f152d5d7 | -11.9216 | -43.3972 | 2026-06-30 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ccac84db-e937-35f0-80e7-6aacd8f4f74a | -12.85905 | -44.33877 | 2026-06-30 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a65673e-ccd5-3f57-b891-1baa7db1efdf | -9.60692 | -56.9287 | 2026-06-30 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c4505a9d-db3f-3be6-8995-bc1725fff083 | -12.44788 | -44.75505 | 2026-06-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bc95c3-4182-36dd-890a-7bd0a5deff24 | -12.66997 | -56.38518 | 2026-06-30 04:21:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b9d0c00-44c4-3187-8df8-1197461290c5 | -9.75029 | -49.03104 | 2026-06-30 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 577d8069-c406-3489-ad2c-66efa1675b44 | -12.20142 | -52.86347 | 2026-06-30 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 63b0bb94-98b9-389f-b6cc-c320a84bc62d | -12.51049 | -48.2745 | 2026-06-30 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a2cfb145-75a1-3a5b-8ee8-ec143897f394 | -11.89024 | -57.13397 | 2026-06-30 04:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eab1f948-4cc2-3e65-b47a-b6d3d1ee99c9 | -17.71121 | -46.79073 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 200518be-dd65-3e30-b8c1-566168552dc6 | -20.96875 | -49.74614 | 2026-06-30 04:23:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 991eec0e-723c-36d4-8b67-12b65d48f91c | -17.71176 | -46.78712 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d2d54b2-cb33-3998-ac1e-09d530b51fdd | -17.71342 | -46.77629 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9ef7095-feb1-3f15-b525-24cf869a3c9c | -22.80778 | -49.34032 | 2026-06-30 04:23:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c23513b6-08cf-3285-b34d-863cbd95e786 | -17.70543 | -46.78201 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b43c254b-6f69-3a3e-8369-d848f7b74a67 | -18.24187 | -53.8472 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a8dfee0-9ec0-34f8-b088-f667600d8338 | -17.12682 | -49.965 | 2026-06-30 04:23:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 741c7925-2529-3716-ac47-75a72fc2494b | -18.24855 | -53.84256 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c6e4e61-7075-3b80-85b6-c63118db6870 | -19.72274 | -44.54132 | 2026-06-30 04:23:00 | NOAA-21 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19c6952c-27af-3603-9fbe-c4abb5b15b1e | -17.71287 | -46.7799 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fadabfa-82ec-30df-b8c3-7ba877f00818 | -19.032 | -46.18756 | 2026-06-30 04:23:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c484b130-4cfa-349b-ae97-e54c793cc636 | -17.6088 | -44.60505 | 2026-06-30 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579ba1a3-5cc7-30d4-bdc1-1da78cfc2446 | -19.74036 | -44.00084 | 2026-06-30 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a7a66e2-63ad-33bb-8030-b2bc9b04ce66 | -19.46779 | -44.7651 | 2026-06-30 04:23:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 607b9838-55fa-3ba9-aca5-3d70577f0d6a | -21.31926 | -48.53709 | 2026-06-30 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8412d8e-d55c-374b-b44c-a8e5ff1972bb | -18.24425 | -53.84158 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4b44221-e8fe-3fd5-9cb0-f6f8eef697ad | -20.40144 | -48.76243 | 2026-06-30 04:23:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 902660c9-ed1d-3d18-85eb-ca6f02cc8503 | -17.70599 | -46.7784 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee2d70e-08ad-35f0-8d77-3d981c7a51ad | -21.31867 | -48.5408 | 2026-06-30 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c948bf9-21be-3475-8d3d-c66dcfe9720b | -17.71232 | -46.78351 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d149c606-7bdd-3a35-9a23-c13e6fb3696e | -20.04944 | -41.68985 | 2026-06-30 04:23:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dd6146cb-57c8-39ee-ae26-11f51fba8406 | -17.59607 | -52.49723 | 2026-06-30 04:23:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e67dfee7-18a1-3c86-b7a9-dcf48dba4155 | -17.70846 | -46.78656 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ad15da07-be5f-313a-97a3-0978b184f206 | -17.70956 | -46.77934 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8930054a-b9ca-316c-aef0-5f8fdd674551 | -18.24356 | -53.83817 | 2026-06-30 04:23:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b38c388a-af5d-389c-ac6b-884864de0947 | -20.78561 | -42.75581 | 2026-06-30 04:23:00 | NOAA-21 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8510c9a0-8012-3368-9933-157197f32025 | -17.43945 | -47.16229 | 2026-06-30 04:23:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8955b60d-0c2f-3aa1-995e-0cdbe6724814 | -17.61401 | -46.6926 | 2026-06-30 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b987fc96-2261-3d7a-9bab-78e117dd16b5 | -15.3775 | -59.28684 | 2026-06-30 04:23:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0eebac7-da70-3c3e-b651-287bc36c40b7 | -15.37114 | -59.28526 | 2026-06-30 04:23:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb007500-db13-317c-8fb9-8ac0cf9512c7 | -20.97278 | -49.74289 | 2026-06-30 04:23:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 525dcbf0-98f2-31f8-a7c4-76c22c2d3789 | -16.19314 | -59.32963 | 2026-06-30 04:23:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9292257b-467b-345e-b0e6-bf75a35008db | -20.78161 | -42.75523 | 2026-06-30 04:23:00 | NOAA-21 | CAJURI | MINAS GERAIS | Brasil | 3110202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README9.md)
