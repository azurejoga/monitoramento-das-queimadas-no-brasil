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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0aee857-e148-364b-ba0d-cf0be5e982d6 | -3.62709 | -55.27985 | 2025-10-21 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3e930f5-c818-36bd-a992-5aee35d8df78 | -2.87376 | -50.72152 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8715c2aa-946f-38f2-bb73-09508bb044f2 | -1.19493 | -49.07663 | 2025-10-21 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7433817d-dc45-3c35-b1e4-b0e45f65c43a | -5.66631 | -49.79352 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5658e0c-beb2-3f7a-8c26-4be0863a2511 | -3.24695 | -48.76801 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e13a205e-58e5-305d-ad3e-0e3a54ce826f | -2.17071 | -53.49012 | 2025-10-21 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a40df86-bf18-3197-b6b0-dd8573c6da28 | -4.27206 | -53.79559 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ee83cc-bb60-37ea-92ee-303952c51b2c | 1.70192 | -55.71843 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57324048-5f8a-38b9-a79c-7396e0dbd139 | -3.30958 | -50.22464 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f31057-c208-3fb9-b1de-e00ec07d6a1b | 1.71999 | -55.72695 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff947159-06e0-3eea-b91d-079a52ac12c6 | -3.09705 | -51.29422 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31cfc758-f2b0-3e3d-9fb1-a496f6db130b | -6.984 | -48.67747 | 2025-10-21 04:44:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fd03e45-0201-38df-9d68-7450afbeb0af | -2.6969 | -49.54764 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e1c346b-b334-3229-90b4-967c3f4c93a5 | -2.86169 | -50.73376 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7930d138-42d5-3f00-8ae7-67233f4d6db3 | -2.73497 | -49.39073 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f4b2c10-993c-3d1a-a97a-a893f8f7fdf6 | -3.11133 | -51.20323 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea7d61a-b359-366f-b400-c424fdde1946 | -2.83787 | -48.10064 | 2025-10-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c662e1f-ddf9-32f3-a9fe-4da04b70133e | -3.5086 | -45.82664 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce3d73cb-99ea-342f-84e3-467a424579d1 | -3.61564 | -52.2885 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d857177-e537-3070-be24-ec2ec1bf5057 | -3.13057 | -52.99776 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e27de9ab-cbf8-324b-817e-8a43f0b57fc1 | -2.71955 | -48.8364 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e22749c2-c22f-3c86-bb82-8407f28d7bc8 | -3.40699 | -46.90234 | 2025-10-21 04:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da38a8f8-89c9-31c5-97c9-ce3ef709fe59 | -3.3266 | -50.22376 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7befeba9-7601-3adf-8892-b9d89a1a2efc | -4.59667 | -49.5841 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40c20c27-67dd-3024-9d05-7262c0cf018a | -3.22304 | -46.78179 | 2025-10-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d0082842-bd0b-3d2e-a67e-4b36d7f55350 | -1.20155 | -49.07766 | 2025-10-21 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d2d70ad-4bdf-36c2-adf8-602c5eb5bc2e | -2.49803 | -49.20853 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0e8401f-75c7-3811-b740-0be19fceeb1d | -2.77276 | -48.02171 | 2025-10-21 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 03836d53-a347-3722-bce7-9ff3de84955b | -4.89311 | -48.97066 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afdee317-c906-301e-a400-a7e44038a14b | -2.79634 | -48.88799 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a85f1aa-c059-36d4-a855-b6377a411a7b | -4.74945 | -44.43759 | 2025-10-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94b88a7a-4c1f-3281-90b1-c90f753ea509 | -1.19824 | -49.07714 | 2025-10-21 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16bd084e-3be8-3db2-98dd-46d6c53e37e6 | -3.33078 | -48.70698 | 2025-10-21 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b03cce1b-1e04-362e-8412-c73e4f8c7f64 | 1.70122 | -55.71398 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bd5b6ea-a75d-38b9-bfd3-544b2ac1d8ab | -2.48105 | -49.25218 | 2025-10-21 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10344929-8edd-3a6b-86c1-0e1dc15669d7 | -2.77334 | -48.01796 | 2025-10-21 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6d23782e-b04e-31c6-8c26-9ef2e77043ff | -2.80217 | -51.3494 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8205fd3-b2e3-3462-8626-d18d4aa8c663 | -3.2475 | -48.76442 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fbd0151-f642-31af-81cd-f21af7e8e20b | -3.85311 | -48.95963 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d54fe320-00a8-3596-bc3c-135084a4fcb3 | -3.96885 | -48.06781 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 235355d9-07ca-3300-9fc3-3e0fd22d7357 | -3.65468 | -50.25796 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cd52488-a5cb-38b6-ac49-fa2793abfeb6 | 1.71085 | -55.69653 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d5b7179-2ee5-31a3-b201-06c1375f3ecf | -3.23715 | -54.7806 | 2025-10-21 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e825a57f-ef17-3996-b410-e9dcf0076900 | -5.70837 | -49.21618 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c36cc43-fb7f-37ef-a17a-7a1f21a511a6 | -3.1341 | -52.99831 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ac2139-ea74-3462-a90e-e911b9506743 | -5.26827 | -50.23369 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7dc6c0d4-ab90-37ed-9f17-8920e2a04cdc | -2.87868 | -50.71169 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e87a9227-b8b2-3af2-b782-b9cee566aaea | -2.25144 | -51.91529 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc38d9b8-d3cd-3572-925b-43eaa99d3990 | -2.86499 | -50.73427 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b94a9e14-c66f-3286-a45c-9d01b0ea41fc | -3.82842 | -52.38564 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca11ce7c-e1a6-33d3-bb77-8226df6bc275 | -3.14957 | -50.15708 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a5bc27c-b33d-323d-9a4b-1125411dcd20 | -6.98341 | -48.68134 | 2025-10-21 04:44:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93cd39fd-2951-35fc-8ce5-8e19a356e0ab | 1.7071 | -55.72226 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40d723d4-7f25-38a8-9c3f-9c931f5e7525 | -5.27157 | -50.2342 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6d98a46-afa2-3994-b70a-272d3659a283 | -2.65032 | -54.89544 | 2025-10-21 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d0974ad-0468-32f7-a904-fc836e225fe5 | -2.86391 | -50.74117 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 332ced79-20fa-351f-973b-4aef8bd290ea | -3.33908 | -49.90606 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f24a345-e551-3189-ba8a-14b73d61567b | 1.71931 | -55.72243 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a55b670e-268d-3cd5-bdf3-dc864df958c4 | -3.25658 | -52.91212 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ed895f-b2e8-3142-b16a-9a719228764e | -3.69341 | -52.59145 | 2025-10-21 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 457e1aa8-9d16-3f32-b595-ea5aeb564e9b | 1.71464 | -55.69142 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cab32b6-319f-312b-bb75-31750c243f3d | -2.86115 | -50.73721 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d00c4272-5cd0-3301-84d4-67c038c9f090 | -3.96942 | -48.06401 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cbaa645-860d-3ba7-a448-05311470bc98 | -2.8743 | -50.71807 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce0dc785-fabc-3f50-9087-c4946d0f88c7 | -3.09186 | -49.50364 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab3fe73f-2ed8-304c-96b9-25d124d0f8e4 | -3.60079 | -55.26521 | 2025-10-21 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eb6e8e8-d7d9-35d1-8e3e-29164a3219e6 | -2.86992 | -50.72445 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd20c16d-42b8-301d-a0c2-80590f50f7d8 | -3.14551 | -50.24767 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec26cb96-f27f-335a-81b4-7a755c481249 | -4.27414 | -48.87276 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f68bafa5-5f5c-330b-9bd3-b3e25d106cc8 | -3.49695 | -45.82486 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b686f57-316e-3297-bb37-0c7c8395d0f5 | -3.6928 | -52.59524 | 2025-10-21 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc2b64cc-77ad-301c-bb02-ac34c28ccd1f | -2.85369 | -49.54778 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b0302b-070c-3b44-ab73-078d3a6262c3 | -6.88973 | -43.62123 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e608cf6d-055f-36e9-856d-13cea55e0ac5 | -3.85256 | -48.96321 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4591702d-fc87-3f56-a187-42322ac269b6 | -3.65068 | -48.97223 | 2025-10-21 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e11caf7f-0a29-353b-916b-2265fc711fd8 | -2.29288 | -47.99273 | 2025-10-21 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bab0127-8912-33b2-9872-b3ec2f68285f | 1.70405 | -55.73197 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e22b110e-19b3-3811-9710-cece7c9f236d | -2.91468 | -54.1599 | 2025-10-21 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de337a64-2e4f-38fd-8093-01ceb803d83f | -3.66371 | -52.11912 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c706c09a-064e-320b-b864-6bc922a43820 | -2.48606 | -49.41611 | 2025-10-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85923006-f99d-3372-99be-9b02548e4dc7 | -2.26102 | -47.88064 | 2025-10-21 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d6507782-f3e8-3180-a05b-e754e0c056f1 | -5.22284 | -49.60566 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58c22b7e-fc5b-3ba3-a230-c48f925ae74a | -3.42492 | -49.48446 | 2025-10-21 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2050c8e-8052-391d-a96c-1f44f091b325 | -3.45658 | -51.64776 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6880a34-ae53-3ee6-98ab-4d05b8a67355 | -2.87707 | -50.72203 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3c60025-8334-3400-bfdf-e36c4512b7fb | -3.84996 | -48.15848 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b23f23cc-c2eb-37e8-aa07-2106cce460af | -2.45072 | -47.18591 | 2025-10-21 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0512fa35-8c28-3361-9c4c-861f73022015 | -2.81343 | -54.37948 | 2025-10-21 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8c16919c-b2be-32d9-9a3d-1086cb7a8d53 | -4.83896 | -43.00567 | 2025-10-21 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3c33837c-626e-3c10-b0f1-e79ed1fd57c5 | 1.71417 | -55.71865 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b56714a-4dee-34f4-a6a2-eb736d08c8e5 | -5.22618 | -49.60616 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5205346c-0106-3ef1-a4c9-e81b3a5b68c7 | -3.14934 | -50.24475 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddef471d-80a8-375a-a621-13c2d4231c38 | -1.76449 | -47.26245 | 2025-10-21 04:44:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad97a7e9-519c-3471-b2d9-d178ba552d8a | -3.58358 | -55.44595 | 2025-10-21 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3b5551e-b971-369e-8f11-130b8ff6baca | -3.10904 | -48.59904 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2bd5a51-bd44-3e4b-b9aa-0b4c8256aa6d | -4.27569 | -53.79615 | 2025-10-21 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 325d6728-147f-3d4c-aa91-1841ac119035 | -2.87814 | -50.71514 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ddc1fe0-2735-3942-9e99-24a118068b7d | 1.70521 | -55.7199 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88cbf9c2-99e2-33ce-95fb-ff7b1f1cfe7a | -3.50158 | -45.82055 | 2025-10-21 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5256daef-e3c4-3aa3-b3e5-8fa9573ac901 | -3.23794 | -54.77575 | 2025-10-21 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
