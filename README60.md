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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26a5654b-2195-3684-a827-54d1d608ef2e | -1.22643 | -51.74202 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c72ac71-e99a-31a8-ab58-2cc217dfa931 | -0.86965 | -51.88896 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1f82e10-4990-34c6-88f4-b355f8014163 | -1.99276 | -53.14008 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f135ec1-c04b-359e-ac8b-0cbd4ec307b6 | -11.99024 | -57.19802 | 2024-11-22 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41bbe829-9471-39d9-ba4c-f289707c74bd | -1.72622 | -52.71002 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ffc4a87-f91c-3404-bad3-11dfbef7d272 | -1.84721 | -53.69447 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3430aff-244f-3c3a-a42a-4a216c870f5a | -1.20111 | -51.95652 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41f0f5b1-cf47-3bb5-9ddb-2f502c6722d0 | -2.0789 | -50.32076 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b96d73bc-cfc2-3e85-9032-830ca14022e7 | -0.87288 | -51.88808 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2578591e-8053-3189-82ec-ec016b35b8fe | -1.19988 | -51.9467 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64ba5157-7c51-34c9-bd90-0b96a53acd50 | -1.19574 | -51.95565 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85f40ed3-46a6-3819-9e82-19b5f1e03859 | -1.39062 | -52.34187 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a269e9-0c79-3bbf-bb13-5ab09255018a | -1.2277 | -51.74112 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 691fad29-668b-390c-9059-0b8e53653a2d | -1.22718 | -51.74464 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dec642bc-dfe5-329d-9abc-31b97b0f037c | -1.79282 | -53.63645 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77bd4f2f-6f47-356b-b86f-1288826c2e61 | -1.74605 | -52.3743 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55fcdecb-9de7-3382-9d8d-e663d8f7921d | -1.8119 | -52.15879 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| bf77d39f-1914-301f-8673-d3596ce8835c | -2.50358 | -48.99612 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4d10771-8ab3-39e1-b973-f255119ad404 | -2.35325 | -48.55583 | 2024-11-22 05:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30f68702-fde9-39e1-b5d3-dbeb75cf8144 | -1.72875 | -52.7072 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2630bf10-7631-3c8c-8c59-82f5fc8d4d98 | -0.91225 | -51.73592 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5b349e4-c9cd-3b66-a3da-9f88fc99f1ef | -1.25999 | -53.36777 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9fc38920-1bec-3c4a-b753-5445a8b1d3ac | -1.19291 | -51.95605 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d810ecd9-93f0-3ce4-a18b-2cab49c60729 | -1.61376 | -53.26971 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1e443fc6-23f0-32b6-9ae8-a77b3d9f9318 | -1.62673 | -52.41573 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b3cfcca-a6d9-3820-b61c-bbd2cefc10ea | -1.15224 | -53.59103 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9d3c70e-0cff-37b5-9741-98ae83bcba89 | -2.16046 | -53.79549 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e54ae2cb-d43f-33dd-aeba-93af527d2cb2 | -1.61299 | -53.27468 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 61f38fda-91a0-30c5-83ea-9ae769c23373 | -1.59473 | -53.80777 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d0ddfa92-372d-3872-b9b3-d0958e548097 | -1.18751 | -51.93696 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a04884b-7d57-3369-b088-9360d7181248 | -1.25596 | -53.3614 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 781cda9b-dade-349e-aeb3-fd1b0ee446bb | -1.34165 | -52.24189 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ccf3f0-5bf2-37f7-8f26-5cc48576fdd3 | -1.60213 | -53.2132 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 072561cd-353f-37d3-a575-e416e3187f96 | -1.19344 | -51.95265 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24926e8f-b795-37b3-98c7-9e0c5882c86a | -1.58981 | -54.70668 | 2024-11-22 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afb4711c-bb3d-3089-81d2-e804d15a0773 | -1.26403 | -53.37401 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 800e9e16-93c2-35f1-84df-2b6b80b94364 | -0.93715 | -51.7184 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1dc8bf-b0b2-3856-9fea-c765243e0da3 | -1.78881 | -53.63041 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffd219d6-21c9-3ea0-bff9-ee4d96d646d4 | -1.19625 | -51.95224 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0820ab4a-ee50-3c5c-b2a1-79d56e572e65 | -1.11825 | -53.39447 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 11d157d8-02ee-366c-9432-0425ba0414e1 | -1.07401 | -53.36906 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9c0e6e78-b3e8-3722-9ff2-de31ccd9f9bd | -1.50699 | -53.13029 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a500de2-8ece-3afb-9e1d-954c5e54aa4d | -2.20147 | -53.65591 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 111ca2f7-5971-37b1-b4c3-f84dfe00eab5 | -1.74259 | -52.39693 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3bd2092f-a187-3f73-a5d7-cf3cac897fd4 | -2.21903 | -53.7352 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9bc657db-1e77-3358-b007-31b154cdb3ec | -0.30543 | -51.48253 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511e6ce6-02d0-3667-ba64-0e8858f9533e | -13.24438 | -50.88477 | 2024-11-22 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44bb9650-9afa-356d-9af1-d73ec188376f | -2.50274 | -49.00193 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4ad24bc-309c-3e53-8c91-bab446a3ad17 | -1.80934 | -52.16108 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dadd1d1-8f4f-37bb-a4f0-f22d3140aeaf | -1.54275 | -55.52127 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ef96c60-39e4-3bb3-a16c-360ea4bda112 | -2.22467 | -53.73072 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8de868ff-336e-31ca-b164-63d1c4e66cec | -1.22153 | -51.73764 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6859d0e4-ca47-37d7-8c0e-1521ed093118 | -1.14926 | -54.17846 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d98e42b1-9062-3462-988f-026d0d7873c5 | -1.07772 | -53.36576 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8b209ef8-a793-3e3a-a1d1-92777ebc779e | -2.49613 | -49.00085 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 120f3a6c-d1a0-3f6a-b870-56248d07faa1 | -13.25721 | -50.89255 | 2024-11-22 05:31:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 227d8b21-d65b-39f1-aa71-a62cb0b6113d | -0.87237 | -51.89149 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2da0370e-b294-3d98-a07c-ad01f281c92e | -1.21498 | -51.7438 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4535450-3ae0-3ba4-95eb-bfe405d13fc6 | -0.77542 | -51.76971 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94d60a6e-5e56-38e3-a9b6-0ed48394a164 | -1.19037 | -51.95481 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bc09039c-a4dc-3238-aea2-a474137d0533 | -1.1886 | -51.94842 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a22fd34c-9992-3994-b03e-1c51e58b1ca6 | -1.20535 | -53.69102 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53856f7b-0b6e-3a00-80da-22d397cbb94a | -2.4981 | -49.00182 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75702189-da06-3d0c-aaa5-3ac88bd6a6cb | -1.63296 | -52.41014 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eef6908-2d07-3851-a209-24bfe525e49f | -1.63304 | -52.66388 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af19794a-a267-3adb-afa8-1409f0bef971 | -1.15414 | -53.67249 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d008ac6-656e-3730-84d4-22b2794f3d41 | -1.19775 | -51.96029 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ecc122ba-e0dd-3e63-b435-8068527c9cbf | -0.92259 | -51.74107 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fddd84f5-e088-35ea-a93a-2bca88759fb5 | -0.306 | -51.47897 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7574bd-dccd-3767-bd19-4f594229a13e | -1.22698 | -51.73851 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86ea2c93-65b0-35ad-8c2e-25652da4b95a | -1.0521 | -51.74099 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1c3ba8-708a-38c9-9b98-a7b7e1dec694 | -1.22098 | -51.74117 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66e4d426-c28a-37b5-9d6d-6b5f9afc6b38 | -1.27303 | -52.98211 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c38d4b5a-73ae-3e1b-8213-c917e2e784c8 | -1.76678 | -55.32481 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97bf3e62-d569-31e9-a89f-43c6192dc747 | -0.92311 | -51.73761 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23f73ec3-1a78-3426-8b9c-01da8ce58698 | -2.16125 | -53.79026 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 77b04729-fab8-3df9-ac4a-a4b804a5fbc4 | -1.71839 | -52.48503 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2e5c1d3-36d6-3cc0-8d71-c17b7c012ecf | -1.20869 | -54.03139 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a535e00-9854-382c-87bd-d5bae9b2003c | -1.6532 | -52.67022 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90a34516-628e-32ba-ac33-ca40f341e6f4 | -1.96396 | -52.99214 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 615ab2a1-b468-3974-9695-5a027d2acef9 | -0.95347 | -51.72097 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ece074a3-d1f8-3675-966d-f807b20b5846 | -1.25286 | -51.75949 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a01b833-0f2f-3b6b-adf6-f6e4c90e790d | -1.63771 | -52.41417 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13ba19d1-06b8-3789-9262-ae886889d591 | -0.95944 | -51.71835 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf6f8372-622c-32d5-b746-d24b8466ca4a | -1.63855 | -52.62674 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb962fa0-d59d-31dd-bdf3-6933ad04af38 | -1.96352 | -52.99506 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 307f5204-f1a1-350e-bb09-9c659dda9b40 | -2.21984 | -53.73 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a296c14c-4942-360e-9d2d-2b55eaa4c077 | -1.77355 | -53.60084 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e25afa70-133c-3a56-af25-3cd4a680a5d2 | -1.14067 | -51.68127 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc279aa0-0530-37d7-bdb1-9c110346d9fc | -2.50559 | -48.99706 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e28c64d-f18b-3ff9-ac9a-86b34e1fa7e4 | -1.14736 | -53.39951 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713df15d-2d62-3a63-9c32-e2ab25d524c6 | 0.96565 | -59.57478 | 2024-11-22 05:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db75cc3a-4084-3e12-84cd-884ffd8fa904 | -1.07487 | -53.36357 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f1f4d1b2-c8eb-3144-9fbd-b82472570848 | -1.57942 | -52.92731 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5262f3e-a6a5-35a8-9e91-0c4fbc6e2ff5 | -2.07853 | -50.31496 | 2024-11-22 05:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa3a0215-7009-3256-a787-6c081492a2fc | -1.20648 | -51.95738 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 615dac59-8c5d-35e4-8b3d-f82268f270c6 | -1.6335 | -52.66078 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88bc3004-c047-3508-9de4-cac336a3e735 | -2.19742 | -53.64983 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55c16205-705d-3775-a1a8-8c48ad7d2c51 | -1.14073 | -53.66608 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df9eabc-55a9-31fd-aaac-5c4c80a857e4 | -1.18701 | -51.94035 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README61.md)
