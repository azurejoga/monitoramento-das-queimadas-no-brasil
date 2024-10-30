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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcba1f0e-1817-3e62-96d3-8aef6f0a9a4a | -2.96303 | -48.63292 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd98fa74-0be7-3da8-b62a-c84312beade1 | -2.94513 | -48.06887 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecf50487-4e5a-3ae4-9492-1d1bbd4a2213 | -2.93593 | -48.0259 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 334219e4-c368-37e2-aaf1-8a276f2f762f | -2.93306 | -48.02161 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 625d16fe-a034-3dc4-8955-0f75b5309711 | -2.93247 | -48.02538 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad4e4d2b-60e3-3569-b1ac-c806c1294822 | -2.9136 | -48.61087 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fa26749-24bd-3698-a8b2-6a4cc6547a97 | -2.91078 | -48.60673 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68289428-f727-3c7e-96ab-facfabc7441f | -2.90738 | -48.6062 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30a5f919-0d62-3809-adc9-405f7f1b65a4 | -2.85348 | -48.46087 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b08b065-0b99-3f3e-90f2-fc454ae7e912 | -2.80018 | -48.66771 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aca9f185-d4be-3884-b7ed-162d8df0aa93 | -2.77534 | -48.64913 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afe32a00-7c6f-39c8-9587-ab86bd496399 | -2.76864 | -48.71435 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00bc9d0e-f227-3c55-a6a7-3a24534fa2cb | -2.72702 | -48.73726 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e3fa6c-4fac-3df4-9269-42e2469ef2eb | -2.72646 | -48.74084 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef7d94ef-c9fb-3358-9f52-4bd59bc29b72 | -2.7209 | -47.74443 | 2024-10-30 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b42fded1-a352-3b86-a9c1-b4dac603c2ca | -2.7038 | -48.6347 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6f1688f-bcc4-3e56-918a-f5f7f722acd9 | -2.69985 | -48.63779 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3805af51-a076-3879-98e8-287992187337 | -2.69646 | -48.63726 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c8f929f-9d67-3077-8d18-98dc43e6b7dc | -2.6959 | -48.64085 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e3f06ff-a151-3f5c-b201-47633a00ed4d | -2.69139 | -48.64751 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9cc8a1b-b7cd-3d19-8e82-31609c52b057 | -2.65168 | -48.50087 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d2096b-92ff-3865-aeb5-407b449b7644 | -2.61658 | -48.32359 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd2b4dd1-7b8e-3e83-b0c8-12c0c3b96ca8 | -2.60974 | -48.3675 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c8a4935-2336-3fd1-bbe9-2eb3bfbeacde | -2.60635 | -48.2542 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ff36db7-0931-3e8f-a255-d3d230bf8c24 | -2.60577 | -48.2579 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9af10eba-a83f-3246-8196-af8fb3c193a4 | -2.60423 | -47.93386 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56627772-ec60-35b1-9043-e8f7f06d6fb2 | -2.57736 | -48.39617 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fca78a50-c791-3c1b-b1e3-910067cb4688 | -2.54073 | -47.51212 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 172307f3-f82c-33f1-ac2b-17ecbadb6bc3 | -2.54012 | -47.51603 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd30b398-7bd6-3f6f-816c-3f8c095a0393 | -2.5372 | -47.5116 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34462421-801f-3d89-b3d2-a44c401c9a4e | -2.51688 | -47.45638 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e2d565-088a-3438-95e9-723183d514f1 | -2.51456 | -47.44798 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb35a91d-b470-3162-80d3-9a0464a60e05 | -2.49638 | -48.06776 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a96d7458-b7f0-3c43-b5b8-dfc4f0920bbc | -2.49294 | -48.06721 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b12ce834-1871-3547-90ca-79cc89f48e0c | -2.45111 | -48.48858 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654ea813-9b66-3a39-bd9e-149ff75297bd | -2.4494 | -48.47719 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31fc27e7-3bdf-3fbf-b628-8225cf989d91 | -2.44189 | -48.77018 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64018bd9-177b-3d42-b179-059f65948353 | -2.44133 | -48.77374 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d072cd3-2c7a-36dc-a663-ef06f42663be | -2.43701 | -48.51233 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64cf657b-3abd-31d5-bfa2-9530532d4730 | -2.41003 | -48.54925 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1ad2649-3961-3fd5-a702-8de966c110bd | -2.40664 | -48.54873 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b4c9efc-6711-32fe-9be1-e354f7f70ab8 | -2.388 | -48.57903 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53ed16ff-099b-391e-be79-1eac361a6cae | -2.32513 | -48.75978 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f8740b3-25e1-3117-8b96-8850deea4f84 | -3.05997 | -48.94899 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca4ca9e-020d-335e-9bdc-4cbcf0717686 | -2.99997 | -48.95042 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28381b68-5f8b-34e6-a683-d3217608c548 | 1.675 | -55.8634 | 2024-10-30 04:44:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1ad56434-ea05-3a63-8ac3-ac6a85cda7aa | 1.6751 | -55.8437 | 2024-10-30 04:44:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 21af8179-4c37-3f85-9844-baa5ee8ed6c9 | -2.833 | -49.2413 | 2024-10-30 04:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 20589eb5-cb61-3152-b253-dd02c6ad895f | -3.1786 | -50.6016 | 2024-10-30 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f9a83984-3a66-3914-b395-0e96f2f454c0 | -3.1787 | -50.5807 | 2024-10-30 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 5eb2fa72-626c-36eb-927d-0367edd51a52 | -3.1601 | -50.6021 | 2024-10-30 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 0b3ff53b-0d6a-3052-bc31-83be6ffccc58 | -3.1602 | -50.5812 | 2024-10-30 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a8ec4733-24fa-30f1-93a7-23a7d6606a58 | -3.0734 | -54.167 | 2024-10-30 04:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 45d33807-e200-3659-87cf-d4ad7beb12d8 | -3.1097 | -54.2865 | 2024-10-30 04:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2c5e4333-4bdb-38be-aa47-954f2149169f | -3.1098 | -54.2665 | 2024-10-30 04:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| bc1d8a37-8482-37cf-813b-56c5ef976dde | -3.1281 | -54.266 | 2024-10-30 04:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 36fdd0af-56ef-3657-b4a7-17076494b757 | -3.2534 | -50.3689 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 5720e11f-ecea-37c2-b215-fb683d2365e2 | -3.2535 | -50.3479 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| ba1d4ab4-aae6-3e29-87c5-af876cbe004d | -3.2535 | -50.3269 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 4393d4e9-161b-3844-8b47-88965f046391 | -3.2718 | -50.3683 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b19f9b2b-7743-3827-8a6b-fa3a1576b622 | -3.2719 | -50.3473 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 1c4ea845-f9a7-3a7f-a538-69964bd394aa | -3.272 | -50.3263 | 2024-10-30 04:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 7d51fc2c-493e-3f55-9ac4-409d455dafca | -3.5818 | -47.3621 | 2024-10-30 04:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 5a2f7290-eb2b-3a4a-a0e2-b21d32c32d6d | -3.5817 | -47.384 | 2024-10-30 04:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 2dd1a102-d334-3cf1-ac09-dac504f6bb7a | -3.5632 | -47.3629 | 2024-10-30 04:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| abbe6ca7-356d-31d7-9922-a8676cc40985 | -3.5631 | -47.3847 | 2024-10-30 04:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d1f23dbc-bb4f-373d-b294-e4ac2f1840a9 | -3.9486 | -48.1291 | 2024-10-30 04:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| ebd824ce-11c3-3bf1-9315-cb5461783dc9 | -4.0682 | -50.0029 | 2024-10-30 04:45:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 803deeac-11c4-3447-86f9-4790b70fbb9a | -4.0681 | -50.024 | 2024-10-30 04:45:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3c42e184-93c2-3f2d-b37d-37ace5a50a10 | -3.9671 | -48.1283 | 2024-10-30 04:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1382565f-93d6-3bf3-8eb6-05c1bd926e13 | -4.0867 | -50.0021 | 2024-10-30 04:45:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a74b4767-4d9f-3202-90f6-3558bb2a075f | -4.2496 | -50.6677 | 2024-10-30 04:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e7f26d50-4120-31ea-9185-d52b372e480a | -4.2563 | -43.4368 | 2024-10-30 04:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 71e27b84-1c4f-3915-b50d-ae989df64f0f | -4.2749 | -43.4357 | 2024-10-30 04:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 136b8998-93a9-3c86-9389-3dd0e004723e | -4.2681 | -50.6669 | 2024-10-30 04:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 03759486-aa7c-302a-96e6-0b16badb4b37 | -5.9788 | -45.3621 | 2024-10-30 04:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1e5d05ef-b078-3cd0-9ba8-3130d4d827ae | -6.8592 | -59.0511 | 2024-10-30 04:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a245fee6-674a-32d6-b385-d5e1980edd0a | -9.34598 | -49.54265 | 2024-10-30 04:46:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 028201ef-bfe9-31b1-9054-a8690337cb80 | -9.04923 | -50.00403 | 2024-10-30 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a41960b-139f-34a7-a7a0-6201ba2b9d12 | -9.04867 | -50.00768 | 2024-10-30 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88c2ec05-eb47-3925-8637-bf4726dd74e7 | -9.04812 | -50.01134 | 2024-10-30 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 884b4f7b-4956-313d-bb66-bca0cae9cb35 | -8.84836 | -49.85771 | 2024-10-30 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19372f9-77bd-3c5e-9972-39dcc57f97df | -9.94362 | -48.96134 | 2024-10-30 04:46:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e52ceabf-c61b-34d4-b312-b98ebcfa555f | -9.73753 | -48.92017 | 2024-10-30 04:46:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a645e87b-1d57-3411-acd0-db93f878369d | -9.73041 | -48.91912 | 2024-10-30 04:46:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a00e9c95-d39e-3376-9233-b0cdd2fff59c | -10.37216 | -49.92599 | 2024-10-30 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0aab4d9-7dc5-31d7-b2c1-a4b7ac785366 | -10.33804 | -49.64547 | 2024-10-30 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1898ac59-b0e0-3470-a05b-c0dcfab1e29d | -10.33457 | -49.64493 | 2024-10-30 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a32b58ba-60c5-353b-b554-3a6454dc1e3f | -10.33399 | -49.64877 | 2024-10-30 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee00da6b-e8de-3ce2-b758-5cdb1d6899ab | -10.20096 | -49.14556 | 2024-10-30 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac333e4b-751f-3232-b0be-a5b406c3eddd | -10.19683 | -49.14901 | 2024-10-30 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f8f29de-be92-3835-82f7-4953310ebd10 | -11.91468 | -50.76238 | 2024-10-30 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff5b5d51-8bbc-3ff4-9f0f-c5d98d4d6043 | -11.2202 | -52.73554 | 2024-10-30 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99a25ef4-c7f6-3000-9afe-d32ebec10bce | -15.11991 | -59.02457 | 2024-10-30 04:46:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfb45b20-03ae-39dd-8009-e7b784f68545 | -10.37985 | -58.75964 | 2024-10-30 04:46:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a67d592-f4dd-3e67-a476-f00b53435d4a | -9.93282 | -60.49045 | 2024-10-30 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb38a1e3-2416-3bee-9199-52590f2c24fa | -9.92768 | -60.48938 | 2024-10-30 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95c79012-2435-31e7-9c7a-50df986da1cb | -10.45162 | -61.28016 | 2024-10-30 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b63dbc9e-e9f5-373e-bd09-bf3f7186490b | -10.45002 | -61.28041 | 2024-10-30 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cda26fee-96d7-3d60-be42-b50b3b9cddce | -10.44625 | -61.27906 | 2024-10-30 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README76.md)
