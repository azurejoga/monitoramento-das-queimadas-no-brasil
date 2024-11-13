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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ddb5551-7741-3b83-b468-f7323913e67d | -2.5552 | -53.99474 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2eecdff-5791-39f8-acd6-12e8dbea5eae | -3.09908 | -54.30227 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0776a177-56df-3cdd-a0ee-c5d3851b4d30 | -1.44093 | -55.4585 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f92d7df5-682a-3da5-812f-147bccd50d0d | -1.71658 | -52.45648 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8e8cb29-11db-3c27-9758-5fbad68279d5 | -1.57864 | -53.73593 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f60bc161-9f7e-36c9-a3b9-0eb27b7c785c | -3.98242 | -56.24221 | 2024-11-13 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04535669-4bfc-3da2-829a-42b611b4fded | -1.79426 | -53.85756 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86224f15-b1be-3d15-aee4-a3fd425df24d | -3.97452 | -50.93568 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a5a9b09-d21e-3866-a3b0-1c36e5ca00c2 | -4.92704 | -44.65486 | 2024-11-13 04:57:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09a1b697-cccb-3708-81d9-df49ed914ae4 | -1.34801 | -51.39601 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eede3644-0faf-3ef6-bf2c-fdaa339e402a | -4.40022 | -50.68882 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f88f4b5-5fbf-3765-a02a-b04c32025f88 | 0.63889 | -50.58651 | 2024-11-13 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99d6e3d6-a05f-3e50-8070-21eee4053bfa | -2.54967 | -53.98684 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c0db42d-e9c7-3c9f-89fb-0440e7129948 | -4.29716 | -48.59748 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4981ed7a-747c-34b2-9e6f-539bb894bd72 | -4.11436 | -54.22926 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d1b3c70-6664-3a12-aa6f-516f35988497 | -3.95036 | -48.17679 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6ab39d09-7ab9-372f-aec1-812148d23793 | -2.24466 | -53.654 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ef6419-cec6-3a21-9558-69067a655acd | -2.33493 | -50.57471 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dd1f061-51be-34ca-9b1b-270f25e4da9d | -4.48408 | -44.56072 | 2024-11-13 04:57:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9063d0c1-7f8b-35a3-be8b-2fe616c454dd | 0.81892 | -51.87469 | 2024-11-13 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe356d2a-b43b-3f40-b586-c9a246f5139c | -1.384 | -51.57321 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d20ce48b-cbaf-3419-ad9d-7f288a2afad5 | -1.89208 | -54.62245 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9561dbdd-7400-32fb-a13a-944f69c37f6f | -2.59474 | -48.2016 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc77880-813c-3985-832b-a496095a91c5 | -3.62418 | -51.49449 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d64a3448-44df-3cb6-a7e6-b5aee791cf43 | -1.65584 | -52.62849 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 037b035a-a9d3-3287-b795-b104ea8cd0a7 | -2.98117 | -51.34127 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7701a72-60d2-3544-8d09-5b3e40c986f1 | -1.97816 | -53.13809 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32c88d50-54ab-3997-ad41-adb48f85a291 | -4.1156 | -51.10411 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b797245a-dc96-35b5-b4d1-a5c0279734b4 | -4.1149 | -54.22581 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e34e79f5-405c-3b89-878f-374707f83620 | -2.34588 | -48.59797 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03acfc7a-9508-3859-844f-040c9c89b072 | -2.58943 | -54.01412 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62de38e3-732e-3abd-9101-ba4bc4fa0cd3 | -3.05298 | -50.33907 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014d3978-648a-3347-894f-c3f339544f7c | -1.22578 | -51.78173 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f02934c9-6f42-3502-802a-a0b6d2de397d | -2.61812 | -49.2339 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84704fd7-079c-350c-95d1-94fbb739bcbc | -1.42252 | -51.11759 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e573fe2a-13d4-37be-b57e-721f87309988 | -3.41274 | -54.90676 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc522fae-c941-32b0-b106-d0a3d9b201bd | -3.06899 | -50.33617 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 552be7ed-e738-3e42-af51-4918418cda35 | -2.92107 | -54.13686 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa2eed6c-0426-3d75-bf96-fb9436c24e81 | -2.24849 | -49.32035 | 2024-11-13 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34b24ea8-317f-379a-a1b5-456e550732b4 | -2.77346 | -54.73096 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5001082a-c37d-32f8-9b16-f2fb2f6e119e | -4.26343 | -48.19404 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10d1c779-04dd-37d4-b5b0-aadd462a0a0b | -2.90654 | -49.25711 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9af2473c-979a-3636-9932-debe2f2efe5c | -2.11759 | -50.6913 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d7d0839-5060-3e4e-9ee9-8c1225fea1c8 | -3.02614 | -50.97985 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d55db953-f6ef-37e7-a261-5aa698634589 | 0.90732 | -50.1451 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ec35fa3-ae5e-3a78-9306-8690a217b1d7 | -1.44153 | -55.45474 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0793deb3-779a-3925-8879-3cd74a3e8893 | -2.2401 | -51.82217 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4562b9d8-c15d-3fae-b63f-7705ce5dde8e | -3.05727 | -50.3354 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b68af835-145d-3372-9be7-9a3632a641bd | -2.24252 | -53.66772 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 340cbe5d-5dd8-32da-902c-8183c4f015ef | -2.99311 | -51.03107 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 3c10d9ad-0c17-35d8-83ad-86b7b22bb7ba | -2.99662 | -51.03162 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5aa0deef-e71f-3ed7-9a6a-8a0ae8f6958c | -1.55992 | -51.18405 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85c8f64-ddcf-3df2-8fb6-9c7d7b9cc5de | -2.99893 | -51.03999 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3406d6ac-0f85-3da4-911d-392c6c973ba2 | -3.40924 | -50.31381 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c78b6ea0-02b0-3560-a279-b374c4e15e6a | -3.2644 | -53.70134 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c39229c-35fb-36ac-a316-4b412a7aff0e | 3.37649 | -61.202 | 2024-11-13 04:57:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b507ac5e-28a0-385b-aac0-e90e0147276d | -2.98717 | -53.97424 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2dee9d0-0756-3af1-a506-6cb5be7a872c | -1.41391 | -52.95829 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19bcdfea-7843-3937-91f8-447c17405a9b | -3.08833 | -51.07252 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb6bbfec-faa0-30e2-a8fd-a630ba7fd459 | -1.28945 | -52.46878 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1b2e354-7e97-323b-a9c7-b46788646406 | -0.98594 | -51.77802 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a26228f9-c899-3279-ab05-23e793a5d965 | -2.28482 | -53.52673 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6e3f49-d338-3dee-9ef5-f7d727331d39 | -4.04118 | -56.11003 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7263acd-ea13-39aa-9471-f4ec4dae8875 | -3.97748 | -50.94025 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f98cef8-17d2-362f-8c0b-dde56a14cb7a | -2.25673 | -50.5186 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15088ebc-3078-3f54-9cfc-ec9ac751e538 | -3.65926 | -54.65739 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94b2f081-1ade-3766-b8ab-ad169045a035 | -3.06024 | -50.3402 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eda5fa35-e009-3bae-a5a5-33c784aaf9a3 | -0.38411 | -51.75098 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0dba029-5bc1-398c-9ef6-fd1992f92388 | -3.40084 | -51.60043 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755c8046-7b0e-34b7-b3d5-7b416973a558 | -3.66314 | -54.65442 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24206961-ed6c-3880-b5b9-0e4d7803db67 | -4.11767 | -54.22976 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccf3241f-a849-3080-8fc2-4628557dda7a | 1.05918 | -60.59718 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7c6a3917-41ec-3e7d-b181-f15c89e06c2d | -1.03424 | -48.84544 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0ec2693-068a-3c08-90f0-6b212b12017d | -2.65287 | -49.43887 | 2024-11-13 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4539e832-dce5-31f0-9a71-61b958a40a60 | -1.41965 | -51.11329 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fe9906b-81e7-3fce-9e22-89b2a230ee68 | -1.58344 | -50.44267 | 2024-11-13 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08f561af-a414-34d1-80e5-b7ce673f382a | -2.78328 | -50.29278 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd619e9b-d9a0-3674-9c2e-39e65f770b3e | -2.46838 | -50.38977 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 661ad261-970d-31f4-8a1f-e78a0cbe8b55 | -1.41331 | -51.11302 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4916243-0cc8-31cd-9415-5841b3ee554d | -2.93987 | -48.3119 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61ffd424-33da-30fe-baa5-e5270d22d76a | -3.79856 | -52.09476 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c93ba11c-b561-3599-8b71-a4f9e89ec32f | -2.37192 | -48.52048 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa4f32f-4244-3c68-93ea-9f981f9e3a21 | -3.80013 | -50.96486 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b966a781-f50d-31f9-85c0-99fdbb24bfa4 | -4.02446 | -49.00771 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb81591e-639e-36a2-87f6-ea752b6525a0 | -3.06496 | -53.25837 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce708f9f-dc02-3429-a12e-83328785019b | -2.72894 | -54.94906 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae364c0b-dd62-350c-82a0-f932a62fed35 | -2.46283 | -53.9763 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d359f253-e8ea-37f8-9b57-d9e2e99103f6 | -3.76255 | -54.64903 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e781c029-ace2-3f98-8ea1-efbbd367d41e | -3.21522 | -50.3826 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea02fbc6-5e6d-3d22-98f8-b2ca447f9450 | -2.94705 | -51.04442 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19fb4f45-d0eb-3ff8-91b3-3f940b3efcea | -1.61911 | -52.23024 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ea8aa95-2467-369e-97b8-61081012aa0d | -2.82381 | -53.99826 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f85e8b92-eee8-3ce8-b6be-47b25f441897 | -1.41961 | -51.11784 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d691bf2-a8d3-3f53-aa88-747b189212f0 | -3.34442 | -54.19257 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32566262-a1d6-3f6b-bb76-d2e2ab82ea2f | -2.55035 | -54.02576 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4618190-4021-3a6d-ba5f-ae94ae16403d | -3.11387 | -53.70895 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fee11e0-5b55-3d93-b808-58fd04f5d966 | -2.61464 | -54.3546 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ce71f92-d64d-3a3c-914a-f7b320f40a7d | -4.6075 | -50.91213 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5662e991-deae-31de-937e-5127c613e653 | -2.83474 | -53.97175 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd206f37-4884-34a5-a88d-ed9af1958fc0 | -2.59346 | -48.1824 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
