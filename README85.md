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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce407d24-fdad-3eca-a3ff-92fbcbedbfaf | -3.81081 | -51.54086 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5dca552-c989-3eed-88e2-2f0e90242e1a | -3.80744 | -51.54033 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5c3a0a7-2789-334c-ba96-b3b4979a1b4b | -3.78961 | -51.17546 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| addee336-3ee1-3d46-be6a-931d5f0e4729 | -3.77169 | -51.85501 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d4043bd-4e30-323b-a8ea-acc08980ee07 | -3.7683 | -51.85448 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8344af0e-19c6-3ca1-8dbb-552d7a09d237 | -3.751 | -51.33162 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89f2bf1a-e587-3647-b3af-5c042948b2b7 | -3.7494 | -51.95225 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3324caa-398e-38a7-a11f-ea29fc742912 | -3.74765 | -51.3311 | 2024-10-14 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b736584b-37df-3855-9d3a-533c775e2ab3 | -3.74731 | -52.24995 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e738444-42e4-37a4-9aed-800d24d44fb7 | -3.74386 | -52.24942 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37a65d0e-a751-33ab-99c1-a47958450e60 | -3.73159 | -51.20567 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b1a4bc6-6dac-3479-8be6-422d049f678f | -3.71523 | -51.79421 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dff2ffe7-681e-3c92-a520-d3f01aad56b5 | -3.71241 | -51.79005 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c89df3de-14a9-329a-8cfa-9d7f94052b0e | -3.71184 | -51.79367 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a3ba39ae-8946-3ea6-b082-eb770e744068 | -3.68529 | -51.17321 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ee039e0-442d-32e9-836a-8e4dcbe222f8 | -3.62104 | -52.01448 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bbbc986-4d47-31fe-8ad5-4a874aeff8d9 | -3.62046 | -52.01817 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fede30d-4327-32b1-bbc8-4c3fdec68241 | -3.55719 | -52.01944 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f91636cf-0f44-3ae3-837e-249a4701a3cf | -3.55319 | -52.02258 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f03a413-03c6-3d36-8ffd-6a6d4e31d154 | -3.54977 | -52.02205 | 2024-10-14 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e115a7b7-8ec6-3962-b7fd-87d0e8c79440 | -6.40915 | -52.70545 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c895ca58-e3aa-380b-96e9-711dbd65a165 | -6.40855 | -52.70915 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9ec44b-3df8-3702-b0c1-b60bac5fbdf9 | -6.40796 | -52.71286 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6e8b05-3770-3b6b-b5fd-5486ce348995 | -6.40513 | -52.7086 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74101d08-a4d7-3047-80c5-8a1a3dbad6c0 | -6.40171 | -52.70803 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 211c5d1a-df9a-330a-bfe7-93797af4664d | -6.34369 | -52.68033 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61038aa8-eaf5-3397-a344-2076b158f219 | -6.09148 | -51.21587 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e16bdf62-9db3-31ef-a373-665d6fd4e0c6 | -6.05935 | -51.22506 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c9f212d-b3fb-3cd8-ac70-098e10b25323 | -5.94136 | -51.2849 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f00d613-357c-39fb-8a3e-257ec96df92c | -8.65142 | -53.05703 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90333b08-4993-3dfd-93d1-f1cd2f42c5ff | -8.65083 | -53.06068 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb4e9535-9409-3f21-a04e-027148020220 | -8.48141 | -53.24271 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44dd18fa-ac83-3d8f-82f8-27892a9950c7 | -8.48081 | -53.24643 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 230aab30-9573-3545-a263-593681aaf416 | -8.47738 | -53.24587 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d2af89c-db71-3f81-86bc-dbb266e88742 | -8.47455 | -53.24162 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4aaea2d0-3356-3fe7-96f7-a3b79d800d60 | -9.0552 | -53.00132 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9592d2bb-59c4-31b9-a635-d302d6e167ec | -9.05182 | -53.00072 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c9a83bd-f8a8-32fd-a19d-775d1a0fbfb7 | -9.05124 | -53.00432 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83059685-a145-3b90-83fb-1776a2471d17 | -9.04785 | -53.00371 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d10cbe7-83ed-3bb0-86d2-63376d2ae608 | -9.04447 | -53.00312 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03f82687-1e71-31ff-a09c-f31e4d6903f0 | -9.0437 | -52.94342 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9268da90-03c8-3f98-87ec-9c5672b5d9a6 | -9.04165 | -52.99902 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3cd0fd-e744-3bcb-b916-49fee0f7bb5e | -9.04107 | -53.0026 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9912a0c-7d9c-3eb5-9a29-662c2654a7e3 | -9.0409 | -52.93922 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7af1f23-215e-357d-af6f-33fe24880c41 | -9.03942 | -52.9913 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12808ed3-3afe-33bd-b989-8114bd14b86f | -9.03883 | -52.99492 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07931290-3257-3d8f-bc1e-b97d34949671 | -9.03825 | -52.99851 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc20b6e6-fb51-30e4-9fd7-f602becf4c4f | -9.03752 | -52.93864 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 671db89e-a44a-3d4d-bf1f-a29b5bdd3bd1 | -9.03618 | -52.96838 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05d35306-d4da-315a-bb52-77a5417eeb34 | -9.03355 | -52.9417 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffde89b6-4b3a-392e-baed-43f24054f44e | -9.03296 | -52.94532 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b23ce4f-f3ec-3865-ab6d-a4143a3c34f1 | -9.03237 | -52.94899 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d94153-48e4-383d-94c6-fbe74ad1e02b | -9.02957 | -52.9448 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7445846-24d1-3ed3-a6e6-b70011128b00 | -8.93584 | -52.11709 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e037b3-1601-3764-b685-852f7069cee0 | -8.93529 | -52.12057 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb5d18b-0a7a-3ded-98d1-b83197529969 | -8.92652 | -52.84638 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19dea928-f568-3aa2-8ea2-d7ba612c649e | -8.92315 | -52.84578 | 2024-10-14 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b7e6f4f-1b3c-3e87-8e08-f9f8f2dbeaf7 | -8.85426 | -53.0333 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83484f64-1fbb-3287-8bf8-a4ca680ebba0 | -8.85266 | -53.02156 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7fd2bf8-82b9-3b5c-aff9-13093593dbc4 | -2.00811 | -53.30001 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37699cbf-e0f6-3eec-a9aa-6deb73235ecf | -1.93769 | -52.10091 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d0861ab-abc5-32ab-92e2-72e9025cebf9 | -1.93709 | -52.10472 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec47faf-8823-3872-a1db-5b97838ef7e2 | -1.93482 | -52.09655 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0db01dac-9266-3b44-a7ef-0f7671756104 | -1.93422 | -52.10035 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b566fe7-2473-329e-9cef-963ff39cc1ca | -1.72172 | -52.52918 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68db17c3-a390-3687-8ccb-d549e2f721f8 | -1.7193 | -52.52572 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35e11622-c53e-3a20-ad15-c1ee026c7a17 | -1.71881 | -52.52466 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9287831-41e0-3900-ab5e-56436eddf04b | -1.71868 | -52.52969 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 864c7005-2399-3473-8d53-e61b720f693c | -1.71817 | -52.52862 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98c0fc19-383b-37a5-9321-f03fe10dcab0 | -1.71575 | -52.52516 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5c37afa-5280-3d55-baae-254e1a2dcaff | -1.71115 | -52.50818 | 2024-10-14 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 520cd61c-58b0-3886-b11b-8b2c1bd352f9 | -1.5241 | -52.06976 | 2024-10-14 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c54a5b24-b52b-38b6-8b55-327ecf1d5ae7 | -1.44944 | -52.2913 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b159f9a3-30b7-3b4d-9b25-64fff49fe42f | -1.35646 | -52.94158 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 103fff5a-c8fd-324f-8f62-1e257d14de53 | -1.35513 | -52.94994 | 2024-10-14 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aab10ada-65c9-37e2-9a2e-f7dcc4bc2d4f | -3.17859 | -53.16503 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b4d1823-c0fc-3b24-91df-4af152a8a57e | -3.10581 | -53.03375 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5348f2b5-ac54-3a69-906d-e95768122c97 | -3.10324 | -53.0499 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55fea372-a58d-3499-b2ef-65e9016e72a0 | -3.10259 | -53.05398 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca238883-1832-3c58-8f67-9a8d75890c3e | -3.10223 | -53.03319 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b82ffbd8-6fb3-3cef-9721-c23023577fea | -3.10159 | -53.03722 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db9ce558-08c6-3817-a175-7bba3c3bf6c1 | -3.10095 | -53.04125 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e226beee-95e2-30e8-92a6-83e0af1e47bb | -3.1003 | -53.04529 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d3a7a3-7f60-3d13-b2b0-ebb9988af8f2 | -3.09965 | -53.04937 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e371f50e-6bb6-3cb5-a42e-73321ead95cb | -3.099 | -53.05345 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66361acf-c2d4-33b1-b209-51a9db882384 | -3.09866 | -53.03263 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6097abdd-69ac-3e49-835a-3ece6b5d1765 | -3.09801 | -53.03666 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47b1c32f-8c18-32ce-b2be-487462463493 | -3.09736 | -53.04071 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13946ea0-c9b4-3415-8e8a-59fae02213a1 | -3.09672 | -53.04477 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d19bffbc-44bc-36bc-9cf6-e2f6a36264c1 | -3.09607 | -53.04884 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69d826dd-2e50-3f84-91f8-34fbcdfc6646 | -3.09443 | -53.03611 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff770ee0-3875-3c15-a9d7-fe4fcdfa8d84 | -3.09378 | -53.04017 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9953076-b4fb-3228-83cc-dd135a6e4d4d | -3.09085 | -53.03557 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a18d9b4f-c2c2-3949-b0a9-de112e6e8ed8 | -3.0902 | -53.03963 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 267a3937-e0dc-3ca1-969a-69064ab2f0ae | -3.08727 | -53.03503 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8250b236-a13c-33c4-b950-a0bc83e83473 | -3.08662 | -53.03907 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd9a2e4-5c09-3b58-b337-8d6be10a609c | -2.98575 | -52.90392 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c044e6b4-5185-392a-9b21-fa202f665068 | -3.42913 | -52.77166 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9041aa96-4d08-37f6-9cb0-9bc4db1373f1 | -3.4285 | -52.77556 | 2024-10-14 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22f3126f-ffa8-348b-b274-bdf28f50fb77 | -3.19497 | -52.20727 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README86.md)
