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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5658854d-2bad-3f11-9320-41721d947554 | -2.80701 | -53.98546 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15ac39dd-6813-34cf-a572-396d747e7d22 | -2.79888 | -54.1021 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca30757c-7352-36f2-90a6-26282c11643a | -2.76152 | -54.03547 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53eb81ed-aa72-358a-9c47-e4b5f1201227 | -2.67171 | -54.02514 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d72aace-4252-3de6-8e7c-d7493c4fa73b | -2.57902 | -54.01421 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14c5ff9b-72b6-3988-8ee8-108f5d7fe4de | -2.57568 | -54.01369 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88fe9d16-ad69-3024-850c-2a6d69d5f3c4 | -2.56178 | -54.01509 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8d73fe82-e215-3c1c-b4ba-9db99a37a538 | -2.41959 | -53.8035 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf78c792-89b0-353f-bfaa-e7792e5b2afd | -2.31272 | -54.06906 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d45c2b8-9f69-301f-9b68-e9b02d67b0d0 | -3.65363 | -54.21804 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 994186f2-6fb4-3809-a9fe-81a2102de7fb | -3.65308 | -54.22153 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d3752c-6551-38dc-ba7a-1a5ca345cb16 | -3.65085 | -54.21402 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 465fbd44-f4f1-37dc-b21b-ce8a549270cc | -3.6503 | -54.21751 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b941833-7a9e-34cc-9ee4-09392934a426 | -3.64975 | -54.22099 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a7bf62a-3f56-3634-b3f9-20a832b9a823 | -3.48617 | -54.46143 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84927a75-ba42-3c0f-9315-2209e6e0d30e | -3.4444 | -54.12835 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf1848e8-ea16-3519-8bea-dc0c524ab9b8 | -3.42225 | -54.18208 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ce4d37b-ec95-3c6d-ba11-d7d1b9353a4b | -3.42072 | -54.27843 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda51f27-8826-39c6-8c77-47c051192938 | -3.42016 | -54.574 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e703d7a-e56d-394d-8f0e-0abccfb55a42 | -3.41738 | -54.27791 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 706febf7-d986-31d3-b6b1-f432e0ee88bf | -3.4168 | -54.57347 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9264f7b0-fec7-3a09-a581-272eef001e94 | -3.58987 | -54.66612 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fa57f81-8d8b-31e3-b750-dba456c32154 | -3.56178 | -54.75663 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6199d572-d7eb-3da4-aa2d-c78eaf2a1d93 | -3.54325 | -54.74272 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05ea3f76-691e-302d-a57f-de1e8777d12b | -3.54045 | -54.73861 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 293bfbcf-ed20-3153-b0d2-7a1f5480ddaf | -3.53988 | -54.74218 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 064db9ef-5082-3d34-9d56-269425ac2c44 | -3.53708 | -54.73807 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36d2719f-a1fd-347c-9255-2165c961d2c5 | -3.48569 | -54.68266 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a25bed56-feb9-338f-a694-2b49c96f680a | -3.48289 | -54.67856 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58318900-a594-3d2f-8d62-9c2d83472588 | -3.48233 | -54.68211 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c97f8d2-ef5f-3c43-a1cc-0161d7fa1689 | -3.47952 | -54.67801 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aada9b31-44ba-3410-ae69-2dcd55fd2fc4 | -3.47896 | -54.68157 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5404f15-f208-3b7e-a036-8d2302c04501 | -3.46266 | -54.74115 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85b98cfe-acd8-3a9c-a72a-df8df3de5dcd | -3.42229 | -54.66892 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4c368a6-b283-33e3-944c-0a0a75ef7daf | -2.27798 | -54.87981 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9e6b325-ee59-3657-9b08-3051eec0af5b | -2.17833 | -54.49383 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66eb8518-1835-36f1-995e-569ca71c007e | -2.14221 | -54.9 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa89bde3-a2ed-37bb-9b20-808308617055 | -2.99846 | -54.10122 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df043976-f8c6-3be1-b4e7-1ecbef8af0cf | -2.99512 | -54.1007 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41d690f9-cc83-3f34-b654-f465929d1a80 | -2.94179 | -54.1998 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01715455-44b9-363b-a251-3aa542d56b0e | -2.94123 | -54.2033 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6f1626f-5c85-3a47-af99-828021c94fba | -3.10513 | -54.17492 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43fcc6c5-a08c-330f-8456-dddf073c7bc8 | -2.85867 | -54.59237 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bb6aad3-16c2-324f-ac9c-56438fdfec2d | -2.8581 | -54.59592 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e365e7b7-f199-3074-9bd2-6e5db2439a2c | -2.81084 | -54.44967 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc8ef26-c80f-355c-b114-ca4c634bb0b3 | -2.79833 | -54.1056 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ec32e5f-f290-39f7-8dac-38d6824b199f | -2.73603 | -54.15321 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fad0ee01-d461-3666-987f-a59c29e0c82a | -2.73268 | -54.15269 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a787e8-0438-3c3a-9106-0c034d81d840 | -2.64322 | -54.65033 | 2024-10-24 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f23536-4ff5-38e0-89a6-8d4ea4815d13 | -2.60606 | -54.54945 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d600d9b4-0fe2-327e-8ea2-3da90f075da0 | -2.57321 | -54.22501 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bf3c947-0a33-34af-b4f3-cb279edf2086 | -2.49992 | -54.6911 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c4ec52b-64a4-3736-91d7-9eedec3e5f05 | -2.48845 | -54.13993 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b190afb3-94c9-32d3-8d87-0489be382013 | -2.4851 | -54.13942 | 2024-10-24 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 267e6295-5a1e-3f38-9817-008383e580d1 | -2.44419 | -54.58314 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e5eb4f2-5cd4-3f01-9e22-6afe415bdd98 | -2.41825 | -54.28046 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6e8d38e-eca5-31d0-a0a2-9183f8904b87 | -2.41769 | -54.28399 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cfbe4342-25c6-3cb3-a0d6-a33da21917ee | -3.11067 | -54.1615 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e196af3c-f064-362d-9edd-cc15f692adb7 | -3.11012 | -54.16498 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb2a36f2-5bc2-3ae8-878a-a2ccc7526185 | -3.10957 | -54.16846 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14d7c86c-ce70-387b-b513-a5520d70ad6d | -3.10898 | -54.15052 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a4c1311-7ec2-3ede-9fd0-c2166ed5faf5 | -3.10843 | -54.15401 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 70b60ce0-e1c7-338d-8ff7-c13452b6bca2 | -3.10788 | -54.15749 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d511f3e6-e518-3d36-80b6-280c82cb9fc9 | -3.10733 | -54.16097 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 312b3b35-3767-3306-baa2-c67436deda91 | -3.10678 | -54.16446 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e687182-8a5d-3528-bf55-86e5486cfa44 | -3.10623 | -54.16794 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3dad235a-1aed-35d9-9c1b-13cce10acd8d | -3.1062 | -54.14651 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac421a3-09af-3f3a-8c62-2a2ec9fb2eab | -3.10568 | -54.17142 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dd3eeff-2b6f-3210-b51e-51186396f093 | -3.10565 | -54.15 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 238b852d-2942-33ae-aae4-eba1a4409fec | -3.10509 | -54.15349 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d3b58e8b-7af3-3068-8769-210b1e4117fe | -3.10458 | -54.17842 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48817dfc-49a9-3d0d-85f8-9eff9bf0b3f3 | -3.10454 | -54.15697 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e1bc01f-33d2-355e-a7fb-d9932db1a6e5 | -3.104 | -54.16045 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86960076-bd1c-3c20-b71f-3f3f9d6150e7 | -3.10345 | -54.16394 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b8a8551-5a85-3d40-aa30-40bc81aefc2c | -3.1029 | -54.16742 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d78ef9d-370a-3b83-a103-4a3b53343847 | -3.10234 | -54.1709 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc67dcf-a382-3954-89bb-98bd10d84654 | -3.10231 | -54.14948 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6037ebf-c389-301e-9525-85fe4ebc861a | -3.10179 | -54.1744 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d873e031-5fd3-30c9-a8d9-473bedf05c03 | -3.10176 | -54.15297 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8b703b9-1c1e-383b-9e90-76b78e87ab39 | -3.10124 | -54.17789 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f56ac2a-08a8-3637-9a21-6216fe7e2242 | -3.10121 | -54.15645 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae3dd9e-0c0c-3b6e-8dd0-c11d1b4431a7 | -3.10066 | -54.15993 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e793c7-d577-3f89-b41b-baecf1b955af | -3.10011 | -54.16341 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7debb187-1ed0-329e-b5e4-82141b96a1e5 | -3.09956 | -54.16689 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05f9236-44f4-389b-b70d-26e32bfbe1b2 | -3.09901 | -54.17038 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c3cc8da-45f8-38be-870b-a1093c1412dd | -3.09897 | -54.14896 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0b715f0-758f-3d6b-abf5-925406dc3bdc | -3.09845 | -54.17387 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68eacb4-3ed3-3286-a10e-c9b15e57d798 | -3.09842 | -54.15245 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e035feb-4927-3208-96d0-c2fbce82f600 | -3.0979 | -54.17736 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e188d4b1-4290-3662-ae5e-4183edc25bbb | -3.09787 | -54.15593 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5219f343-892a-39f4-acd5-8faa583c12aa | -3.09732 | -54.15941 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab01a4db-b334-39fa-98f7-bb74573765d7 | -3.09622 | -54.16637 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa08d820-a7af-31a6-b755-2a38c2b44e70 | -3.09567 | -54.16985 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2adae35a-edad-32b7-b097-ef18d99d9261 | -3.09563 | -54.14843 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f52523c-53b7-3d00-b4f3-d1451c4c5ca5 | -3.09511 | -54.17334 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cba70ee4-05f5-364e-93b7-f4d23a67ae84 | -3.09508 | -54.15192 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b66113d-558b-34b6-955c-ee282be8787d | -3.09453 | -54.15541 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79a11cd0-e461-3e83-a4fd-242401301346 | -3.09398 | -54.15889 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5a0bf72-e278-336c-8711-a2861b1c3046 | -3.09343 | -54.16237 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fffcb22-38a4-3113-bd9e-e0c632cf5cdd | -3.09288 | -54.16586 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README71.md)
