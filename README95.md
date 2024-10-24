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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 338e29de-26de-3a6e-a80d-34c6f4af10a3 | -2.81153 | -51.35341 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c448b1-c004-3fc0-9d30-4b89532f8665 | -2.81109 | -51.35638 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b820c1a-ed52-34d9-a585-e427c7e52b02 | -2.80057 | -51.59885 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a997a8be-b95e-34fb-9f24-534157708d35 | -2.80013 | -51.60178 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1746fcd3-4f7f-39a2-aa0d-69506698e50f | -3.49183 | -51.60007 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc580bf-3f78-35d2-a6d0-47baefa0995a | -3.49113 | -51.59785 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83ccd2f1-00e5-3633-837c-490a635d7afa | -3.47102 | -51.21401 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af2a37ed-d043-3240-beee-4fed7096b2b7 | -3.46718 | -52.10783 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6af504c-062b-3d59-92f3-8f384e9e76db | -3.45232 | -51.58835 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f2176f-06af-3e53-ad2d-a12a74a8d7b8 | -3.45189 | -51.59126 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e16117c-49f2-3b73-979f-681130f83c44 | -3.44728 | -51.5876 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4aa03a35-4629-3910-8df4-c7cd460da27c | -3.3456 | -51.65096 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0a99db4-609f-3e98-b99e-d79a22d3c67f | -3.34516 | -51.65388 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aa7ec55-0e52-397c-bb44-33ca89360b6a | -2.60579 | -51.77567 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40171dac-7cb9-3795-8666-969ffa1b762c | -2.604 | -51.77534 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7437d9e2-6d38-3e0e-a370-e05e22ff8656 | -2.60087 | -51.77496 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4689d08d-f9dd-327c-aad1-4968be0bd558 | -2.58618 | -51.92278 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45afc8f4-6d40-3726-8d41-9c48d099f7fa | -2.5842 | -51.92271 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e7ff6b-07aa-3374-a435-da42a99bda61 | -2.58132 | -51.92199 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fbb25ec-54b9-300b-a7aa-6023e5480e5a | -2.22104 | -51.67287 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c29ebee4-e1e9-39d7-9d6e-498b4e1c2318 | -3.89049 | -50.98715 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbdb08db-e9a0-38aa-a4b6-221ff6eee93d | -3.89002 | -50.9903 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdbe7c92-417c-3c9a-be0c-5a560f5b24ef | -3.88972 | -52.1262 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0255a78-e451-36c4-9e5e-997f9a314634 | -3.86776 | -52.13964 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80accc7b-5a7c-3e39-b690-e300c9580f1f | -3.86284 | -52.13909 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff6c4e55-2dd0-3a67-b596-d4af45ec7e2f | -3.84825 | -51.88535 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 111453e6-5514-345a-a213-108f2b875b22 | -3.8289 | -51.3636 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fbfcb10-ddac-3e81-9b6a-37fd48fb0bae | -3.82418 | -51.35992 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11e0cc88-01f6-3c4d-8052-78b4a809d759 | -3.71205 | -51.14217 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5464f32-841a-312a-9902-83d327315e66 | -3.71158 | -51.14538 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08b7b2ff-8809-3483-afdd-d8e1895cd408 | -3.67789 | -51.93263 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef70ee2d-27d1-345a-aca0-cfd76176ed94 | -3.67667 | -51.9324 | 2024-10-24 05:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6196c7ab-8c2d-3e1a-a656-c750e1efa872 | -4.64471 | -50.92661 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce79862f-3cec-3d46-ad07-278feef4c405 | -4.64421 | -50.92998 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bed10535-b7f8-3a44-8c81-3448c5878fb7 | -4.64086 | -50.91537 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66388fdf-2c42-3c87-b439-6b0f3ef353fb | -4.6125 | -50.92158 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b65d24c-8da2-3913-b6ed-17159bdf050a | -4.60714 | -50.92067 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6f69899-4183-32aa-9052-cfb0866d29bd | 1.00839 | -52.2197 | 2024-10-24 05:21:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f85a1208-2b4c-3dc2-85fd-6a54d6409a2a | -0.08749 | -51.6349 | 2024-10-24 05:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 538e99e6-1a59-328e-88bf-6f5baa53a675 | -0.08669 | -51.64001 | 2024-10-24 05:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d94d13e-7043-3ab3-a661-cfe9d7608f31 | -0.08272 | -51.63417 | 2024-10-24 05:21:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f57ba85-c1ce-3025-8848-b085c9423c2a | -1.59988 | -53.31174 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7ab565e3-5e78-3e4a-a101-a466f3a02c73 | -1.59617 | -53.30697 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 56539edf-71fc-3b27-a76a-0a20b70183c4 | -1.59552 | -53.31112 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4d2116d2-60f6-35d3-8a73-56b00972fec0 | -1.59182 | -53.30632 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 31b7d036-0149-32f6-abda-ee5bca245a31 | -1.59117 | -53.31046 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d3fce709-b32d-35a3-a117-2a70ca7addf3 | -1.59053 | -53.31459 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c5fc741-1e9c-32e2-9485-1b71e557382c | -1.58989 | -53.31871 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46e49ab0-63a8-3979-a451-30b2e2d6c3d9 | -1.58746 | -53.30568 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 90343833-8078-3bbb-a319-ddcd658948b5 | -1.58682 | -53.30979 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b692718a-dd7d-36b1-8d9b-1caf4bec2d59 | -1.58618 | -53.31392 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e162cfdd-fe6d-323b-9aaf-170008a66955 | -1.58554 | -53.31804 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b258c8f-bdd7-35ec-9409-927a13d6a33d | -1.58247 | -53.30914 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e786de0-e028-33cc-9346-80f97826af09 | -1.58183 | -53.31326 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe6c53d9-f101-3ef0-88b8-5c1c5fa83beb | -1.58119 | -53.31736 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22df93a8-dcad-37f5-8e2e-2c5f8c7d4435 | -1.57748 | -53.31261 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b62f4781-8542-3e80-a770-772dce3d7991 | -1.57684 | -53.31673 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce9d6c8b-b76b-30c5-bdf3-5b18b6b06e53 | -1.47515 | -52.95281 | 2024-10-24 05:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c7e5adf-92df-39dc-ba5a-2f3d8e314761 | -2.04476 | -52.03236 | 2024-10-24 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ce81dad-0099-3c2f-a477-d0f0107d0f52 | -3.63045 | -52.2919 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa113d6b-6908-3a66-b5e5-abaaf26e55f8 | -3.62968 | -52.29716 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb298451-fd5f-3f6a-a86c-a84a540b781b | -3.50933 | -52.89755 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17eee919-f148-3089-ad6c-006188b93552 | -3.50839 | -52.89843 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87aeb883-5930-3380-aa90-643772aa23e4 | -3.47206 | -52.79974 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7723130c-155b-3949-b728-913dbddb4921 | -3.22142 | -53.36716 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef2b0d6-efba-3058-b32e-3b14f20be335 | -3.21696 | -53.36661 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd06faae-17fd-3bdb-949d-978d3ef0bf8a | -3.21628 | -53.37098 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78aee18d-2772-32a9-adfa-b7e1abe00fcd | -3.21384 | -52.46085 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c824cef-d590-3769-a3d3-70bc1bfb7467 | -3.10772 | -53.13363 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 73c88148-30ee-34b3-9599-2544f087f708 | -3.07743 | -53.24335 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e44c7cb1-51f3-34d0-b298-e86ff5efd249 | -3.07675 | -53.24787 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 891f7791-6e7a-3692-920c-0b846a12c052 | -3.07608 | -53.25237 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dace4f5d-6e55-3126-b2da-8fe4a7ee654e | -3.07365 | -53.23805 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 316b1e86-2e81-3e59-9386-ce0b8bb32d5c | -3.07297 | -53.24258 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb872279-033d-3664-910d-4b2eb12e8b4a | -3.07229 | -53.24712 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15ac53ca-8d95-3f60-8ae7-966128c03dc6 | -3.07162 | -53.25165 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 157a2803-2f20-3d33-af68-f137547c896a | -3.06404 | -53.24113 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ce94bb2-8ae7-3197-bfc5-520925c3f0de | -2.77893 | -52.10174 | 2024-10-24 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 911d1101-d521-3495-83eb-b0f25e40865d | -2.77811 | -52.10698 | 2024-10-24 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbf94f05-eca5-3fa4-a2b9-af1da1f38998 | -2.7778 | -52.10323 | 2024-10-24 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 586b4f71-2ea1-3894-a4c8-3760140bdcb2 | -2.77702 | -52.10847 | 2024-10-24 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc98ca59-019e-3b22-ad38-2a310aeb1939 | -2.99819 | -53.44296 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 194323c7-5322-372b-9d08-fabff32c7ee5 | -2.99813 | -53.44124 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 452ec493-fba8-30b9-8829-53fe6e9fe27c | -2.84472 | -53.32545 | 2024-10-24 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e25dc0-777b-3a3c-9853-a5a830d22df0 | -2.78802 | -52.92357 | 2024-10-24 05:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2aa7df6-49f7-3215-a7ee-8746d7e7440c | -4.12135 | -53.83759 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fa65c89-50e2-3dd8-a779-47e075b51e8a | -4.01554 | -53.7358 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6245078-d3fc-3e2b-bea3-7d3e915ca0dc | -4.01489 | -53.74006 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f57918-57e1-327f-8fe8-3a32269ee809 | -4.01425 | -53.7443 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319d6cc5-faff-3278-b00c-62789e9a05b1 | -3.92671 | -53.66799 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f8c4b46-217c-30d0-a9b9-91eb73ff850c | -3.92231 | -53.6673 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a94d725-aae1-3b05-b1aa-0b339d0b5061 | -3.90945 | -52.39257 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f478486-db30-3258-b4f6-cd9fcc75f73c | -3.90881 | -52.39482 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0237a2ca-6b7d-3c5e-9ea6-1f3f4052f780 | -3.90867 | -52.39772 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02cade2f-18dc-3d81-b61b-b026bc56bbfc | -3.78787 | -52.38789 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcacecbc-8cfe-3cb2-af80-7d06f44ab0ec | -3.78705 | -52.3933 | 2024-10-24 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfc6671c-c37c-3fa8-935a-b66a4e53a346 | -3.67537 | -52.68801 | 2024-10-24 05:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e51bdc5-c320-356c-84a2-3bf7a375236a | -3.56301 | -53.75359 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72617d0e-9290-3b42-a75d-bb0d2ed4ce52 | -3.56238 | -53.75777 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a27079fa-caca-3d98-b507-298748679e7a | -3.55931 | -53.74864 | 2024-10-24 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README96.md)
