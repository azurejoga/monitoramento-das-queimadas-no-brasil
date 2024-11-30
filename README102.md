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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a40f480-7a88-3f26-87fe-fb23cbaa9a8f | -3.32932 | -50.21492 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 33d31778-d820-3e75-8a1b-6e0bc309179f | -3.05182 | -54.0472 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f561427-7aea-3371-abca-268a46d17b68 | -3.73389 | -53.37074 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07b48c66-4e84-3bf3-8f3a-7435cc802449 | -2.37371 | -50.40217 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 794a054e-af14-3e06-b851-e31cc2e781d7 | -1.34255 | -52.54571 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04916308-87a5-3f99-aa99-d4c42c5830e9 | -2.79889 | -53.12098 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dd631be-da7e-3921-bf6c-a9b87fcb9d2c | -2.73421 | -47.98766 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8baf7fb6-1e0a-31e9-9730-242bd791253a | -5.22792 | -44.91235 | 2024-11-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee794b8b-3431-3c26-b5e5-985affafdb70 | -3.688 | -47.13881 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f41b1eda-f77c-3253-a816-b7bd11beec71 | -1.5582 | -51.26457 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41acf3cf-dc1e-3b42-977e-0eef6f68f3cb | -1.14077 | -53.6119 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f192342-4ed8-360d-8c18-ede046fb817c | -3.97963 | -41.52357 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0672c01b-0346-3a2a-a11a-c39c445d12da | -3.12068 | -53.76146 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7899a38-3cfb-3e02-aeb9-abb19a5c26f0 | -3.32914 | -54.13338 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4d8abaa-5c79-3108-a766-26e137035b2c | -2.11504 | -50.34096 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6b7422db-eb9a-3189-9c4d-379e1617fe99 | -1.72481 | -52.48288 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6623149-0b16-39eb-8ed1-1bb6881d0806 | -1.14176 | -53.80161 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001e003e-75af-3fae-aacd-2a8c6024abf4 | -2.44796 | -53.97523 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1690d5f-05e3-3e34-b304-919bbdf69f2c | -2.38105 | -47.88366 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd13cfb7-3e48-3108-877e-977b724da0c8 | -2.76792 | -48.55225 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f9e805e-92a8-3728-aa25-51f2518efd89 | -2.6033 | -54.0814 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 318d284a-3541-3ae3-9eb3-750e676b63e8 | -2.60695 | -54.21045 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9177df13-70c3-3bb9-a983-699e4afba7c6 | -2.59821 | -54.26604 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfc4e7e0-1d01-3c3c-be83-86954e6a0ddd | -0.99912 | -51.72039 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1d9c1ec-081b-36b7-8665-a195360ca9e4 | -2.7849 | -52.98626 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceb4087c-8884-3b88-83e2-075dddf164a0 | -2.06155 | -51.18779 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 517760df-9c38-3668-ac72-85527ed854a5 | -0.95315 | -53.20008 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5197c93-b2ca-3bf4-8873-e6523269e1d9 | -1.1964 | -51.74898 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3906a3a8-305d-3c40-b7e2-620c9eb68b98 | -1.21486 | -53.5549 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f1c5d9d-d610-358a-8d62-758087f6857a | -2.5792 | -55.99044 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50459466-d199-3402-9bfc-efc74ed86911 | -4.37394 | -50.88003 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4bad222-a184-3c74-9153-abe569f0221e | -2.80208 | -54.06263 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50004fc4-3080-32aa-8188-628f271103cb | -4.08779 | -51.11526 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71788b33-26b5-31a6-9077-ad408d05a8ab | -3.28751 | -53.27793 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b4d436-6782-37ad-a331-1a8444936315 | -3.31178 | -53.70342 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a0f9bc2-574f-3d4f-9c0d-80f7c4057def | -1.65669 | -52.72643 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3365b2a8-cc3d-322b-81fc-afd89fbfd663 | -1.71192 | -52.63505 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a85e7b1a-1372-34e2-8d35-53d6be619f05 | -1.39286 | -53.62573 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 980d8cd3-eb3d-3778-94f3-de091487918f | -1.82968 | -54.52895 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8df8ee39-7160-30bd-a1a2-ea1865f6f554 | -2.59188 | -53.97948 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bda49285-c35e-36f2-ba8f-e36dc41e1860 | -1.55754 | -51.26882 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bf79483-8bab-3ebd-8373-99e2ba21b23b | -2.31515 | -49.07204 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f382b0-593d-36db-ab3e-2752d86145ef | -2.19672 | -53.78156 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1f6515-7f44-385a-9320-e6b47cf22ba1 | -2.02043 | -50.77612 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a81c9d62-8d5a-3cd8-9fd9-4d81ca92d487 | -1.34885 | -51.9787 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2759a8d4-be0c-38a0-a8d0-f4c1821965fb | -3.36334 | -50.40402 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b3fc91d-9e80-3423-9c20-25f73fc81a9e | -3.08182 | -54.56921 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52898c53-bda0-35b6-8d2d-b8a7817b2b16 | -2.77107 | -55.34044 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dc55257-3b63-3468-8939-0659f44ce443 | -2.44407 | -53.9782 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb7e170-d020-3157-983d-6ee38cf615ad | -2.89937 | -54.15636 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1752b733-79dc-3a3c-8ea6-7784bd011c7d | -3.1006 | -53.26813 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c423b3-d7c4-3a60-89be-17aaacb3c44f | -1.10587 | -53.38662 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 470c88db-6399-31bb-a92b-c8b456ef9ae1 | -2.73414 | -54.13451 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b23bac1-997c-3b0a-9935-923332954ed7 | -2.48767 | -54.02074 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41ee57fd-7971-3d55-9cff-01796348d43b | -2.04696 | -54.69294 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e7dfbbb-68ef-31c3-b85f-e677bb8792fc | -1.83445 | -46.30483 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41aa5c27-f255-363e-aa82-a54ac65a421e | -1.57842 | -53.84423 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e879eb-f75c-3044-bbc0-b0748e91186a | -4.41391 | -50.82633 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25b47b81-93e3-397a-a68f-16f16ec23bca | -3.85755 | -54.08125 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aa83de0-4dbe-345e-987a-1bfe494a1dc4 | -3.11596 | -53.25929 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96e07222-1ec1-3ce5-83c9-5d7491dc82fe | -2.63805 | -49.90805 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3455df-6c91-3d03-9925-cc2452476b62 | -2.78372 | -52.99382 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f59e33b-20d5-3574-a6e3-6a1fdbc6f5a2 | -2.8875 | -51.58297 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ecd4b67-b0be-3aad-9654-f90f9ba0d236 | -3.93655 | -52.15155 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d7c62b-c3cc-3c14-aeac-f5d477148e3f | -2.04635 | -54.6752 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9673b01-23c1-3182-8772-a76abc1eef3d | -1.4037 | -53.40344 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee9f44a2-1374-3bf9-ae6b-df9c790405e2 | -2.46242 | -46.57315 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e98a44d-46ec-36a1-ad64-f4a7dd14452c | -4.08457 | -54.34367 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 737b8a23-8708-37c8-8287-0f839474eb97 | -4.19893 | -50.68927 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f36937b-5fd6-3f68-b4ae-c64227a4fa27 | -0.27428 | -51.63223 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3443a7e6-8a1b-38fa-ae78-929fa331a434 | -2.69552 | -52.9124 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad8c3372-6cdf-3c83-8190-c60b92d6c9c4 | -3.83947 | -46.52364 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f62f512a-1904-3622-bdb0-e20f5c596918 | -1.35363 | -51.97138 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e0d6fa-aa2a-36e3-813f-a5236fbbef8a | -3.24709 | -54.09563 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10163c22-921c-33b3-a09b-f3caad93b83a | -2.53278 | -54.03847 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d7ef7d8-0091-36d5-92af-cf3502cd310b | -3.10407 | -54.03419 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be4d7974-0fa3-3dae-a19d-c7960187cadf | -1.31853 | -51.75438 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11f7420e-0724-3e1c-93d8-ec64166ee5c3 | -1.68087 | -47.84703 | 2024-11-30 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab9255b7-8bdb-3a25-94d6-3aa3b81b0e37 | 1.97279 | -60.91928 | 2024-11-30 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7991528b-6689-3aca-b6ec-74e0c982f5ba | -1.75155 | -52.65266 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c428ea9-8064-3cbd-9468-501220846a66 | -1.19569 | -53.86683 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ff7865d-6b42-3d2a-b104-33b2db836d45 | -2.35776 | -55.8795 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c6719d-f7bb-375d-a4de-534c4958e5af | -2.97525 | -53.28648 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16af26e4-488d-38ed-8387-7b20fc3bd49b | -1.76189 | -53.63948 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90d48126-5ead-33cc-a3a5-431c549ba828 | -2.92388 | -54.17446 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec34d42-5ca3-36b5-8bbc-fa37241a5002 | -1.21345 | -55.89827 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a464f3f7-107e-311b-81d6-3cbb37dcb6ee | -1.35388 | -54.62734 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f4a5055-32c2-3a9b-9e52-6178c43d1b51 | -4.08922 | -51.11759 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3f5d2f8-376a-3e27-ae0f-2dc8beac2558 | 1.19208 | -55.95798 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e263c75-9c76-34ec-87e8-2704bac4bcba | -4.98483 | -47.853 | 2024-11-30 05:01:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e6396e2-3f5f-36fb-86ac-cb55dbd1ac35 | -3.34691 | -50.23343 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76db22b4-1d10-30bb-8700-106a74426ef8 | -3.10243 | -54.04474 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91004c25-adc8-3a4a-9485-af6ddca68949 | -2.74013 | -54.07466 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e848ed49-21a4-39f9-a5fe-db93f1369ee6 | -3.61273 | -49.98915 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21efd29d-df32-3bf4-9d35-de2c846581a0 | -1.32323 | -51.67656 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9446e0f2-a800-3d6f-b9e6-43490504dde1 | -1.14764 | -53.69902 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8f7f533-e1a0-3b45-bd82-866a55188fe7 | -3.76246 | -50.17497 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74f9bf0f-b939-3428-86d4-0214d944c12e | -2.86049 | -54.03942 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d986116-344f-3737-8a6f-bb43164ad74a | -1.32186 | -54.63646 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9525b226-194a-36e4-b4a7-b3e4b83a7f53 | -2.44176 | -50.99495 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README103.md)
