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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4118b5be-83a3-365a-a2a7-13c7df965132 | -2.56293 | -46.5456 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e813b318-ce22-3fd5-b33e-3554cfcd6f64 | -2.09179 | -50.3428 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1669303-6a92-3ada-b5c9-a8cc237e05f6 | -2.1359 | -48.76417 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6282caf-add3-3d57-ab64-1e69580fae77 | -3.0646 | -53.28426 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc03157b-35c2-313a-ba7d-b1608e99584c | -1.57578 | -54.08064 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfa71d7c-66af-351f-bd58-903a01423125 | -0.93992 | -51.71973 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38f4c83-c4d3-387c-9c61-9ab170521653 | -2.72548 | -51.74073 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 780c197a-aa16-3dca-b67c-442ad8f97a66 | -2.38822 | -48.92949 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be14df17-6926-3b32-9c37-592e326d282c | -1.29312 | -52.22187 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc16f87a-da7e-3725-a73d-502871b1e373 | -2.85358 | -51.58884 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 564f9055-caa3-3493-8d7c-18b81cd4f4b6 | -0.04347 | -51.24241 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc20dc7e-d0dd-383d-ac78-63a59cf46a92 | -1.78757 | -53.58375 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e01e3d13-71ef-3891-930a-5ff379d14c38 | -0.05462 | -51.25089 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac95363e-cb14-380b-bb5a-fbf6208e9398 | -3.54657 | -50.40881 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e74a731-1f6c-3f93-9131-02c4ae829a98 | -2.58792 | -51.71861 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 427d1050-68fe-3a15-8607-4de09435d4dc | -3.58663 | -43.63406 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1216670d-6e20-37d9-962f-b068007e6f89 | -1.6563 | -52.69375 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f26a69c0-2d89-3c19-a231-ccaec5e8f166 | -1.4543 | -52.66431 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8473f02c-e4e3-375d-9c32-ebb2bf1188de | -2.22757 | -48.38159 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 733921e2-481d-3625-b7bb-6827befa6477 | -2.1805 | -52.12829 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce921627-7824-3c9e-9b79-cd6a7e51eb15 | -1.32114 | -55.45358 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0066dd65-589a-3d75-b346-0a4a0b018ca2 | -2.20217 | -50.54548 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 571bfac5-253f-3a26-8fc2-04be36b818a9 | -2.7195 | -46.08692 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f227f20-3704-3b54-9cbb-13a257f3bd81 | -3.22921 | -46.44033 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861ace63-832d-33bc-8f33-d828809fb22a | -2.41879 | -48.8265 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f08cb172-031b-3a26-be3b-70b1e3a5c469 | -4.72554 | -43.2506 | 2024-11-21 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06989e8a-d02d-3290-b188-bff91f38fe17 | -2.76418 | -52.1178 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f934f6c7-62d6-33c6-a2f3-ae873bc130e5 | -1.22643 | -51.74226 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd572239-0b8b-3b41-b382-d8d24058ce18 | -0.90475 | -51.72914 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1949792c-9141-3a41-b088-cc50d0b8b918 | -2.95854 | -51.40945 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b69bbc9-307f-3710-a423-9196f4790ede | -2.87632 | -45.25881 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aee2c6a9-0719-3eeb-b4ba-52f039fa1b19 | -2.68082 | -49.19951 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0abe33f5-5ecb-355c-a654-634901c34df9 | -3.30585 | -51.29206 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc5bda9a-513d-3446-bfc7-bf3121dafcab | -3.95018 | -46.7198 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc25381-2e09-3d4d-83d1-442c9071f686 | -1.20369 | -51.77966 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30ceb328-28c1-321a-9a63-3bd1b3acc256 | -3.29766 | -50.35667 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf3fd3ee-a7f0-3da0-b9c5-a28b2e129a18 | -2.67007 | -46.2326 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 147805f8-ff74-3973-94ad-d14793b3c508 | -3.0409 | -52.4357 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d158ba86-9282-39d8-a36a-a16f32bab9ef | -2.60964 | -46.24815 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fac4f5c-1689-3838-9e9d-0bcc11c47979 | -3.43808 | -50.36273 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a436e50b-630b-3014-9943-8833ea38f9f3 | -3.24802 | -46.42904 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f412959-b520-3747-bfd6-d5d65215ab3b | -3.25066 | -50.55713 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 682bdffa-7371-3614-8507-395af0e27404 | -3.27963 | -50.2584 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f4509ae-d741-37cf-a363-c6c29bffa17d | -4.22434 | -44.08807 | 2024-11-21 04:29:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbdf9546-bca2-3e6c-b8aa-84cc4479f1fa | -2.92389 | -48.33022 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e2306d-7422-3de9-a66d-58ea257064f8 | -2.71769 | -47.97401 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee0540f9-6bbe-34ed-8e48-f9e5d7404a16 | -2.28288 | -48.49482 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a41d442-a81f-31ce-9a6e-3a6e1afc47b0 | -2.00753 | -48.75598 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e516e45c-a85a-3adf-bc4a-1f5259fabb74 | -2.61782 | -48.19138 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a497c4-ca4c-3609-8f7a-04a10e3b0547 | -2.16531 | -51.97142 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3dbcd1-e3db-3885-a429-c1e2077e3d27 | -2.57246 | -49.19894 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137d8ec9-bc5d-3e42-a44d-c437e7bf1fdb | -3.11007 | -53.17344 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e771b23-860b-3fbd-b931-fcda53c8a41d | -3.7825 | -46.66915 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06f732bb-c69b-3ed4-b675-1b59b4dc05c4 | -2.89078 | -48.27728 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 603518b2-33e4-3d0f-9c51-56501219c216 | -3.47186 | -50.01097 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7ea13e4-b2bd-31a3-acf9-a5601cf6f45d | -2.65988 | -46.14556 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c819eb99-e75f-3b2f-a491-cd26be9c6dd4 | -0.24981 | -51.03793 | 2024-11-21 04:29:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b7ef02d6-a69e-3d14-ba66-f17a0aa33a85 | -3.74441 | -47.35988 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fba25ab4-a0ff-3c91-be74-700806c6ae2d | -0.42508 | -51.56532 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7ce4e2-3734-3b7c-b72a-941c1fb2758b | -2.62908 | -46.25469 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d99947-bf47-34f8-bb01-ed6bf05b699a | -2.62951 | -51.92353 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e10ec7a-3128-33a7-8f86-6cb5eb2399b2 | -3.07054 | -51.2579 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe1b1c2f-df80-3eaf-8074-a80ee9bf5c1a | -3.33818 | -50.49784 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a889d857-a6eb-3c39-8e57-ae402d9edb9b | -2.33962 | -53.92712 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 432c7883-2d63-3629-9e63-6eb12d5183ef | -1.64829 | -46.96024 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4d80dc-dab2-3c09-9b10-c6ec7abe440d | -3.34494 | -45.16437 | 2024-11-21 04:29:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12a097c7-6729-312a-b952-933e90f29eaa | -0.79749 | -51.78087 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb10a876-5fff-36d0-b463-2c25a924cd0e | -2.26658 | -48.42125 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d48c2478-8661-39db-863d-d485c37238bb | -1.20831 | -51.75056 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3d21463-2301-3131-bcee-c9b534bfe3fa | -1.22251 | -51.79393 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62bd8e31-4917-3c56-af8d-fdedd8778a4c | -1.25487 | -51.76473 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 084d48fd-85af-3a8a-a9d8-8053ceabd996 | -3.72239 | -47.67213 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbb1d030-9e4e-32ce-8b6a-ab2513ba02a7 | -2.43923 | -46.53708 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d51e9f5-73e0-3b35-8e13-51d3bb02f6ac | -0.81153 | -51.6106 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ac2087a-ab81-3e71-b1c1-79a213703f52 | -2.54226 | -48.17976 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 256f3a3a-5972-356e-80c6-b65efbc8dc36 | -2.56836 | -49.20224 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 363141df-2a02-34f1-9748-2f3d8dfc4d5e | -3.28241 | -48.79897 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0036a55-43f5-319c-b11a-74f7261a2bb9 | -3.12601 | -45.44885 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3deeace1-e777-3fe0-b279-efed1185c217 | -2.69772 | -46.22618 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40f26380-fb6b-3234-8e6a-9295e64efe78 | -3.18801 | -46.55101 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 046d957f-2a02-39bd-83da-12ae0b658c3e | -1.7307 | -52.70149 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 331ad2d8-85b8-3c7f-9f0b-f916ce8274e0 | -3.54101 | -50.443 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| faf1a97f-d4ec-30ea-a0af-7f28cdfb05ca | -2.66778 | -48.66685 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c177478-e8ec-3fd0-ad40-220780aca455 | -2.79347 | -52.55132 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50d50df2-478f-3d5b-9391-363d1a53cb54 | -2.70371 | -47.97545 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de857cff-b41a-3c0c-bc50-056f75311e26 | -1.14779 | -53.51675 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0869cab2-e380-363a-9752-30675ac2e40c | -4.25122 | -46.11454 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 416a1400-047f-30fb-a5aa-d24c25eca081 | -1.1882 | -53.72594 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b23bf9f-ca1b-36c2-b0b6-f498bd67bfe4 | -3.04213 | -49.46796 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49795ec8-d67f-3935-b0fd-8ab3ad30020e | -2.72284 | -46.08744 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72bef987-df8c-36d0-8e6e-fa94459003de | -0.25226 | -48.51374 | 2024-11-21 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9de6c463-26ff-3f1f-be0c-92b8a0e757ca | -2.40649 | -49.0606 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb10bcc-23d6-3114-8fe0-c05e718cda1e | -0.90772 | -51.73708 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 344120c3-4cb4-3e10-b74d-1796d979156f | -3.22631 | -43.26904 | 2024-11-21 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0f70433e-b890-3bf0-815a-024c18fac6a6 | -2.69724 | -46.25101 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77f63165-45ba-3ac1-b9ab-a38251842a8c | -0.03961 | -51.24134 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4c246a2-d906-3613-9b32-276b26468bb0 | -2.63955 | -46.23143 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68f92da5-1ed9-3827-880c-4bc0644357da | -3.25805 | -50.6303 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ef32e3e-9a75-3f50-801d-bcfbdd02a0c6 | -3.25436 | -50.55773 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0a2c3f9-a031-3194-b098-d51206dec325 | -2.57124 | -49.20663 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
