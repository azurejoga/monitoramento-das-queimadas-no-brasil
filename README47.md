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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ece2785-1f79-3a68-a809-f0987a18b84f | -6.24028 | -47.27602 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb133e0f-a03d-3706-b43c-bdacc681f654 | -1.23657 | -51.74648 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6df70826-0172-3932-a337-b7c83ebe98cb | -3.78136 | -41.61024 | 2024-11-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6c6405d0-71db-3dc6-b70c-2c891931c408 | -2.70412 | -47.97518 | 2024-11-20 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcdc96d7-cf1b-3fe0-b721-26f221f43944 | -1.64601 | -52.6416 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1995625-3ab3-3264-b63e-c7566c52dce4 | -3.2927 | -53.85999 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc9ab270-d11e-346e-84ef-3e3ad2c5061c | -4.11078 | -51.05041 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dfa8ae8-61e8-3e29-adde-f900f9a36d9e | -1.96355 | -49.55346 | 2024-11-20 04:50:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd0d0a1-7c7d-3bdf-8683-1a230d166f19 | -2.57402 | -48.43501 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d1584cb-5dce-3b4d-bb86-42cf5e05979a | -1.78934 | -53.58958 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b62f011-705a-3f05-b7a8-e1c4e60bc8a3 | -2.35336 | -48.60553 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 209655d2-5b89-37af-ae42-380c87ce0fb4 | -2.70989 | -51.99831 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcfc0e94-2000-3eb2-b6a1-f870b170583c | -2.57535 | -49.07697 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ba35453-9777-3c23-ae0b-34726a112d98 | -2.22868 | -53.61707 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03a8cbfd-c228-3f26-b88f-7c9702255b0a | -2.6319 | -54.28621 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d986e16c-998c-3521-94af-3975e057596f | -1.42425 | -46.80158 | 2024-11-20 04:50:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a62837cf-fecf-389e-913e-c4cae3a4b657 | -3.78544 | -49.3635 | 2024-11-20 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509840f5-0860-36f3-b98f-bd6de51dc8e4 | -3.82318 | -52.25784 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e35a68d-6ca6-3a88-9d78-be3ee204595b | -1.89986 | -53.33046 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6da2b18-fd03-3958-8436-2dcf538d4824 | -2.09378 | -53.34093 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb4f726-828e-38cc-837f-d80e20bb0226 | -5.25154 | -43.83466 | 2024-11-20 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d07691f6-943c-3d47-92a6-d9905b36a4b9 | -0.90191 | -51.72599 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 202f0db7-912f-37c1-9642-29906a30fb58 | -9.18708 | -44.73544 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec645fe-140a-31e0-af0b-78e05068eb16 | -5.69775 | -45.84657 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 480b7083-bb72-348d-9da6-ecaaac7b9507 | -3.06446 | -54.40345 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc9874b7-4f38-395a-a537-de16c76724aa | -2.686 | -46.23003 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac2afd0a-223a-3488-90a6-bae223742476 | -3.28017 | -53.83549 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07ab9db2-2ea6-309f-979e-e47b216219cc | -1.14278 | -51.69648 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93841842-4fd8-3828-b9da-0e4eca539af7 | -2.57005 | -49.20318 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81db5087-21eb-327e-8337-b370cf95e63d | -2.92344 | -53.06317 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2b78948-83f9-33b3-9242-871503a5c437 | -3.81242 | -47.80694 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20709f7a-f893-30f8-9061-961472fe0bba | -2.55569 | -47.28699 | 2024-11-20 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0df7903b-a13a-31bd-b915-ec6596d03c80 | -1.47623 | -52.52102 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca010700-3833-3006-ba31-d275653da62a | -1.94166 | -50.6464 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe47584-fc4c-3658-8027-9630aeaf4850 | -5.69586 | -45.8438 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73cdb45a-59a0-3fa7-b195-127abc77dbea | -4.21571 | -50.69697 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eeb8d0e-06da-3cdd-9277-b116d2a7a30f | -2.90036 | -53.05583 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bece47b-136f-3bde-8617-c7a8307f24c6 | -1.24827 | -51.78017 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62dcea02-4605-3fc1-ad57-0322723c0c82 | -2.69771 | -51.36777 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c607be82-7d3a-33cc-aa7a-c2d5cc08183e | -1.85684 | -54.28147 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| ff5a0acb-abb1-3ea1-83be-5edac6c3de05 | -0.88142 | -51.72635 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7b7c6ea-d6f2-33c4-9c96-b8ab6e7b826e | -1.31343 | -47.80124 | 2024-11-20 04:50:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e61ae1-dc36-3e73-a31c-25dbfbdf9068 | -1.41565 | -54.91999 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0bad7f4-c139-3ea1-bbb5-e8604c243e5c | -1.69816 | -52.35666 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22973a35-12ac-38b8-88f7-172d5056aec2 | -2.26258 | -48.81372 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0395a33-0945-3019-baa4-7b92737dbe7c | -2.17178 | -48.40854 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8df055f6-e5a0-3f22-982e-e0be572e9069 | -3.13642 | -49.13039 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aff01cb4-ea14-3c36-afa6-02c4b2606295 | -1.5662 | -50.42317 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ec6e2d0-a660-3f50-bc9f-642aafc71c19 | -2.25284 | -53.67875 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cb7c158-3f13-3b83-a34f-88eddf4fef8b | -2.74274 | -54.04197 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7136fc77-bf7f-3ea4-a91d-fb246270c211 | -1.93507 | -52.99878 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fda700e7-abe0-3671-bb5a-834f9083bdbf | -1.65677 | -52.53065 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb29582-b76a-383d-8ed1-ffdbea01d4ec | -5.25934 | -43.83924 | 2024-11-20 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 899ef44b-131e-369f-b1fe-601b8e70ec6c | -1.88741 | -50.96881 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8cbb9efe-6629-3d3a-8ab8-e6dadb5d0dfb | -2.59343 | -47.78865 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ae06712-29e1-3e0d-8c11-fcaffe2653ee | -3.78515 | -44.06055 | 2024-11-20 04:50:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 681a7c5e-4be7-38bc-87da-d69d5e97e489 | -3.80548 | -47.80117 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3a80754-bc5a-3347-a0a8-5dea71796074 | -0.93084 | -51.64537 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f9b8864-ff47-31fa-bed0-e6d329c40034 | -3.79869 | -51.14523 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470a84ec-55f9-39da-9070-fe6b3f4c1c76 | -0.94651 | -51.71861 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a93222-0a63-3fda-a4e8-14d682bb4308 | -1.38988 | -52.42741 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 455cded3-e595-31ca-b17c-1d4da60f7cab | -3.05602 | -48.5016 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4cce08b-6560-3e59-92d5-6b8fa64e285f | -2.42291 | -49.10612 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7148825e-eb86-3489-928d-97f953997d12 | -1.6019 | -54.64049 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85f7099f-71c3-3e0f-a48c-2f078137ddfc | -3.52891 | -54.67757 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97e05c3d-5539-3018-96c8-f87f2a6f20de | -2.86714 | -54.4796 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b43387-4f89-3e6a-9337-c6217d566a81 | -2.85875 | -53.97278 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85495846-00b0-3c4c-9de3-b0c84b2e6252 | -1.48961 | -51.15042 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad4f70a-e175-3f6d-8c21-ea811acab8f8 | -4.01588 | -51.01017 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b087668d-e993-3930-b8ee-e0088feec589 | -3.36261 | -54.09625 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60c4fe79-7861-3667-b9ee-1b21b62adc07 | -4.15041 | -43.97432 | 2024-11-20 04:50:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44d90005-97c8-3259-893e-6e46d04d323a | -2.94451 | -48.33187 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0873cde-05f5-3a3b-a25d-a3091e0dbfd7 | -4.99258 | -46.9246 | 2024-11-20 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81d75652-9549-3216-9a91-c5728f7793de | -3.11194 | -54.28471 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e423f9b-d3e4-3ce5-a515-b5504e385dc0 | -2.92987 | -48.32964 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9430ebd0-277b-3a1f-ac65-e0e2e3a49fc5 | -4.39051 | -47.75706 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6538ee65-7d16-3ed2-877b-5197ca4674ca | -2.13951 | -48.56713 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 05f709f1-6c9d-38e0-b8f4-dc4d872da06b | -2.92921 | -48.33388 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06a7ab05-b365-38e3-9111-2cab514fb25b | -2.88889 | -41.75775 | 2024-11-20 04:50:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 077cd799-df43-3857-bbd0-dd878a79bb2d | -1.20053 | -51.7621 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36d97b9-e6ba-3fce-8715-4d57be202f64 | -4.05323 | -54.37589 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e644cf-0e62-3623-a8ea-baac3ed200ea | -1.97167 | -46.42829 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1148980-df1b-3d0d-ad2c-06698150be99 | -2.74496 | -54.11781 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b287df8-a7df-3d77-b7cf-70be49aebe22 | -0.97976 | -51.72378 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 589849ff-f7a9-3dac-b504-b6c5a676427a | -3.76774 | -51.6833 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824955a5-32b8-3097-9442-746b11a4931d | -2.75838 | -54.0563 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fbcd67b-8d74-36de-ac3c-f696016c22c9 | -3.10828 | -53.74697 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee2a1d37-e5f4-393f-ba5e-e4ec12639c24 | -2.1421 | -52.3758 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 964416f1-6a46-32ee-841f-b214cd37513e | -2.68486 | -46.23747 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57fd94a8-2172-3e11-baba-8ba13f66a24b | -4.45043 | -46.58617 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df63b18f-1d21-3b88-84b1-fd47e1c925c4 | -2.55183 | -47.28636 | 2024-11-20 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28328c71-e842-3dde-87ed-b3c306df58ea | -2.79959 | -51.79316 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af54c7d4-d1b3-3bb0-aa5c-2a8095b849ee | -2.33114 | -51.28562 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c2569bd-e969-3586-b47b-f6d217987b9c | -1.64876 | -52.68944 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6bb1cf3-47d0-3729-9936-6fa9cd4f8af6 | -2.84685 | -54.00236 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76924e26-1511-3c4a-ac36-2589dcdaa288 | -3.01347 | -51.01221 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a35754-86a3-3c17-bc79-7b260770e73b | -1.63304 | -52.67968 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5effd0bd-78b3-3f79-9594-a580fed47ece | -2.83363 | -46.67435 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ed00eb7-f5a8-3c33-9901-00d2aff1648f | -1.63921 | -52.6843 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 467c0dc9-7835-330f-9288-8fb5325f2e54 | -1.26641 | -53.40883 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README48.md)
