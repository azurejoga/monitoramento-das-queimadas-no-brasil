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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5812058c-1c8b-39b6-89f6-ad5512973efc | -16.86697 | -55.85215 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e70d7fd3-c05d-39c2-8302-1f5bc0b9c026 | -16.85147 | -55.88686 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7dbf1032-b698-315c-8db5-a1438f0c50f7 | -16.82189 | -55.90286 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fd315246-9523-3c4c-96b4-e5f24a751da7 | -16.81621 | -55.90488 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7f1a8cf9-efd7-36b9-9839-9e05babc43b0 | -16.69406 | -55.9185 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 08d38a89-1ae4-3efc-bed8-fd35befceafa | -16.68517 | -55.90997 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8898cbd5-8ffb-3af0-b78b-22784b0d950a | -16.68194 | -55.87346 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0311a26-569b-319e-9741-21bc94a33223 | -16.68069 | -55.87967 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8a13d331-9e92-3eed-b22b-23db318689b2 | -16.67628 | -55.90147 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7d4ca244-7c62-35cb-aced-b0902caa38a9 | -16.67565 | -55.9046 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4f20f0b1-35b0-3924-9cff-79ace8fc7fde | -16.67562 | -55.87854 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7c08a7c0-73df-328f-869a-205e7f45410a | -16.64393 | -55.90409 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| b70a6a26-59a8-3cb2-b285-25238eae8143 | -16.63694 | -55.91235 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 25e566b2-c9d5-39ae-9265-970a42bc011b | -16.61977 | -55.91836 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 56fdf954-21a5-39ee-9402-f3b14e6f27bb | -16.61816 | -55.91425 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 331f753c-b6ea-35c8-b34e-92b54d0fa64a | -16.61244 | -55.91629 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a450e269-6570-3dc3-819b-cb3339b25551 | -16.6112 | -55.92258 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0079dba7-96a7-3a7c-8cc6-77f6e71f2349 | -17.08873 | -56.67999 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 639833ac-0911-3eee-a6c6-ca3dfcfbd2c8 | -17.06016 | -56.68429 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 1d1e39f2-2c2a-3fd6-bace-a5325e3bdfc9 | -17.03757 | -56.68634 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0112550e-ce8d-3f1a-b962-4f00d18cf7f9 | -17.03228 | -56.68513 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 93511060-5ab7-3794-9be1-b3863843f440 | -16.95967 | -56.61708 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b948dabd-89d2-362f-8768-6538f385b237 | -16.95439 | -56.61588 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fb81c0bb-5eea-3dc2-b514-5ba900618b7f | -16.95368 | -56.61931 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c58d1b04-8f74-3c3e-a1e2-e3b863d9ad8c | -16.95297 | -56.62275 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 299aa74e-ba80-36eb-8a54-cee2e866dc04 | -16.94627 | -56.6284 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a4943d99-970a-32c5-8ff2-a562dcfa12fa | -16.93713 | -56.61914 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ba6ff75f-dcd8-3a64-a2ca-30925765316d | -16.93642 | -56.62257 | 2024-10-06 04:21:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dab80b86-45d1-3da8-a9ea-bf20dc6a58ef | -19.69739 | -56.49445 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4fe821c4-05c4-36bd-8e61-dff3d656c54b | -19.6626 | -56.4624 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 809c8859-7403-3733-a789-023da71dcd82 | -19.66245 | -56.46244 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f1a8348d-7122-36a7-bad6-dcb0e1c0cae4 | -19.65763 | -56.46122 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bb599fbe-2d4a-3f59-b546-773bbd73872f | -19.65749 | -56.46127 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8e78214b-10af-393c-a988-7b9d0ae5f95a | -19.6564 | -56.46727 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7c2d8f7d-90ce-3874-a7c8-a301cfa48112 | -19.65578 | -56.47029 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b4a9451b-0185-3bcb-b0a8-773ec3a4f73e | -19.65516 | -56.47332 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af9eddab-3128-3216-8e2a-1c98847d005b | -19.64087 | -56.4922 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4164a00d-1fa6-3ef1-941e-81d6551172fe | -19.64024 | -56.49524 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e0da4331-3b99-384c-b54b-18e4fa13ef16 | -19.5853 | -56.53341 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5ac16a27-bdf2-3054-b115-6898205a5239 | -19.58031 | -56.53225 | 2024-10-06 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0db3198f-a229-333b-be71-72886fae8e96 | -20.2752 | -56.9343 | 2024-10-06 04:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b722410-889b-3de4-a35a-0edd1240a0ef | -21.40825 | -57.25199 | 2024-10-06 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab2e6e4a-14ad-3bba-bbe5-056346db3823 | -21.40749 | -57.25558 | 2024-10-06 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fe66ff5f-a69d-3ed0-8443-e39836ba9541 | -21.40422 | -57.24607 | 2024-10-06 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79c50da9-6eb4-317b-9ef9-d90b0228f4ee | -21.40346 | -57.24963 | 2024-10-06 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d30490f1-3177-34fd-902e-e7c1423a6345 | -21.4027 | -57.25317 | 2024-10-06 04:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f60f32bf-c58d-392a-b7fa-4e8ff5032f36 | -16.59346 | -57.22149 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 07bfc131-accd-3279-85a6-7eefa392bae8 | -16.53622 | -57.22536 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fca901a3-3e97-3c33-8d0e-58485be72bd8 | -16.52755 | -57.23923 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 590d8007-d2e5-304f-b50f-8e95481e7a14 | -16.51651 | -57.23658 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4049141b-3e52-321a-89fe-6a0b22575ab8 | -16.51572 | -57.24036 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3b5cfde9-ceac-3a4e-b46d-d32685031961 | -16.51493 | -57.24418 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dff1820e-b5aa-36b4-8e23-ca2cbaab505e | -16.51412 | -57.24803 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5b83ed3c-c767-339c-9802-9b9b309d634a | -16.51022 | -57.23897 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2014f9cd-ed0d-3a89-a25b-a142b601f25c | -16.50309 | -57.24529 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aea08df3-1a95-3f9d-9368-f050a9179b96 | -16.50142 | -57.25329 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 49b9e2ef-6fa5-352e-925d-6896ff04c154 | -16.50059 | -57.25723 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ed05f554-7739-31ba-9482-63ab67c77561 | -16.49345 | -57.26362 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4f736b77-9415-3175-9e2f-0b31c3d0ee08 | -16.49264 | -57.26745 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e6ef6c02-e1e1-3143-b54e-f0e6e745badf | -16.48712 | -57.26609 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1b18a38c-a803-3e7d-a8ca-8dcbef22ef41 | -16.46556 | -57.28561 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0312ed3d-e478-31af-b944-62952216f626 | -16.4626 | -57.28079 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9e12425e-ca7b-3841-ad54-36b7c05b6262 | -16.46179 | -57.28473 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d9d5d4c7-0acb-3368-b9ea-1e17d741e444 | -16.46084 | -57.2804 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cf7c401e-cc1f-37c7-b7c0-cbc6644f78da | -16.44907 | -57.31844 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9cc68bbe-c71a-31e1-8bcc-f7ddd1d5bd8b | -16.44704 | -57.31796 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d5521e5-d02e-3a66-9e33-2ce5a61fd269 | -16.44514 | -57.28083 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d9a803b6-0010-3fdf-a18a-272d77d225c8 | -16.4451 | -57.30941 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 309efb5f-8012-3d07-97e2-670e7c56efa3 | -16.44351 | -57.31715 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| be8b89d6-9e15-35ae-abe0-f4b3ed512049 | -16.44336 | -57.28048 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 86b2b840-fed3-3b94-b40d-f20ddbe6b805 | -16.44312 | -57.30897 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 19f43488-dd55-311a-8d53-d71d9ef842ec | -16.44229 | -57.31284 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 65bf7c58-5ac9-307d-90ae-a00fb088f03f | -16.4396 | -57.27954 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af0998ba-40d3-3ca8-ab12-1ad206dc33b8 | -16.43717 | -57.29131 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 68010888-b8c1-3766-b370-21395fb1e6f9 | -16.43243 | -57.28608 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 04f685b8-7ff7-3d64-b7ca-e344decf15cc | -16.40841 | -57.3458 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14f63f9b-a2f3-34ec-83ee-4b917aabcb3c | -16.4076 | -57.34972 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| aba40dc0-f76d-3de3-a5b0-3f44489c81de | -16.40665 | -57.38251 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ef6c173b-eb2b-30a3-aacd-0be03c2326fa | -16.40203 | -57.34839 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7ec9c9dc-deb9-39c0-9bb7-4e7296feb576 | -16.40121 | -57.35233 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b8faf1dc-457d-3658-bc86-eee4fec6e2ee | -16.40106 | -57.3812 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7baf4ef0-ec75-3823-862b-e99d4fb8cb0e | -16.38037 | -57.36804 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 64294dcb-eaec-3ec2-8d9b-d6805ad594ef | -16.37955 | -57.37199 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5db389f6-f9bc-3c9e-988f-8df388763bdd | -16.37789 | -57.37989 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 93b6d9ca-8d74-36d9-9c54-b90f31eea580 | -16.37314 | -57.3746 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e4998aa1-5ee1-3289-af8c-13cc66b27e04 | -16.62275 | -57.1645 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d490c0b3-424f-3751-8b93-98b2fe800957 | -16.61726 | -57.16323 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1207879c-2cd1-33a3-b544-7c2910fe1e7f | -16.61177 | -57.16196 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c7e4d2ae-319f-3c1d-bf1b-66f079493a41 | -16.57326 | -57.15776 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5ab603d3-ab47-3447-97f0-f353d8553a22 | -16.56615 | -57.16435 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 872b26a0-c687-346a-b511-19c59780b5c7 | -16.56425 | -57.2228 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 459fd690-9d94-30be-ad1d-ccd43b141cc8 | -16.56067 | -57.21898 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| c4a8b9ac-2827-39da-96c5-65132412eb1e | -16.55594 | -57.21389 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 04600794-bf76-36dd-9862-d5bf64004ad1 | -16.55516 | -57.21771 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 15902521-862a-37b9-9848-568ab4ea44d2 | -16.54174 | -57.22664 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8bcf8b85-4540-3c15-9614-36467ad3bb0b | -16.54095 | -57.23046 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6bbf3df7-ebf9-3d36-8430-79830c258d86 | -16.53858 | -57.2419 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6e632d04-48d3-3bb9-9b11-d8a4e346e8b0 | -16.53701 | -57.22153 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 66e5f251-61d9-3c3e-845b-0f281d2a3c99 | -16.52202 | -57.23796 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3534403d-3099-35bb-b422-d29b5717308c | -16.50942 | -57.24278 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README85.md)
