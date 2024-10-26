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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e1ddae-d6e9-3788-9b71-a943c20dea00 | -2.76976 | -49.36707 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b32fb78c-5f36-3159-a626-07ad46f8bc9b | -2.74839 | -49.31022 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 650abc81-8e24-324f-96b8-a429c629da0f | -2.7478 | -49.76794 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d008ea82-f090-39d5-be45-fbfb28c0e02b | -2.74506 | -49.3097 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5eb7616-6a4a-3acd-8b7f-57ae56b37c74 | -2.74452 | -49.31319 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 668b4171-663f-384e-9b61-cc93f13a2513 | -3.73599 | -49.68444 | 2024-10-26 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06213615-89a1-31b3-82ef-4849cb2341b7 | -3.73079 | -49.80449 | 2024-10-26 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e9b6079-eacd-3bf3-84cc-1042514bf808 | -3.70247 | -50.11466 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 531d7d07-c54f-3557-951f-f73854147bd1 | -3.69821 | -50.16335 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e23effd-2204-3d42-8cbe-78633148437d | -3.69767 | -50.16679 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a7e9c8f-d1dc-374c-8940-6acac6336f6e | -3.66396 | -50.12278 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a97295ac-cc04-3892-af55-1cd06edb009e | -3.66119 | -50.11882 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87842f2c-2a3e-317a-a380-5223cb33e065 | -3.65789 | -50.11831 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0066738-d6c1-3d3d-93fc-534ddc91ffeb | -3.65735 | -50.12175 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126c6538-6fca-3038-9613-25da36722bf4 | -3.65627 | -50.12863 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4f0054e-4685-3b4d-b0a5-612e8f542f52 | -3.60209 | -50.58126 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bfa7546-0907-3d85-898f-11d340e74f5c | -3.72802 | -49.8005 | 2024-10-26 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51ab7f91-46e4-384a-86c7-7939766bd403 | -3.72748 | -49.80397 | 2024-10-26 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7c5497-1daf-3c50-a474-78af5a0c1efb | -3.6949 | -50.16283 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54781348-b50d-388a-b92c-3ebb9b5411e5 | -2.24042 | -50.53347 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4335635-0ee6-33d5-8ac0-3000f40fb619 | -3.66672 | -50.12674 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f3a705-ab29-31b9-a350-e6eefa391747 | -3.66342 | -50.12622 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c20de97-8a9d-35b2-97c3-08d9e9260b05 | -3.66065 | -50.12227 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3006712e-6fe3-3e96-a930-a90cb56af1d1 | -3.66012 | -50.12571 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78ff612e-137c-3f95-87c1-5cf639eabafa | -3.65681 | -50.12519 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dcb2aae0-a43b-3d10-8dba-b217b3b86c2b | -3.65405 | -50.12124 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea23859-ed0c-373b-bb45-1ed09f8f9df1 | -3.65351 | -50.12468 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8079fa49-3ae6-3a7d-8a63-ae18aed52ef1 | 2.30845 | -50.76791 | 2024-10-26 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d2deb28-4e1c-3356-995c-3f54807da3c6 | 2.30789 | -50.76428 | 2024-10-26 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 09ac8c9d-08ec-3f27-916d-c797d0c83199 | 2.30733 | -50.8053 | 2024-10-26 04:42:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d0c322e-59ff-379d-ab8b-8a2a0624f9c7 | 1.81224 | -50.46216 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dede232-9ff7-34db-9e37-a38c0baa9f2f | 1.79159 | -50.46173 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5e45882b-c888-3784-b283-508f82864ec9 | 1.79104 | -50.45819 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3dd0629e-cbc7-3365-b4ea-b67a09430653 | 1.78879 | -50.46579 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0854c92a-0fd1-3468-9467-ab4815dc03b6 | 1.78824 | -50.46225 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2322b534-191a-3620-a28a-3ad3bb146351 | 1.78544 | -50.46632 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 05b83ce0-c920-3ba6-8ad5-e374be56cf68 | 1.77929 | -50.4709 | 2024-10-26 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 685dcecc-337e-30f1-86b0-48b04890aafa | 1.24065 | -50.86794 | 2024-10-26 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3c33e544-e985-389c-a7b1-90eb0fbd0e91 | 0.82773 | -50.20543 | 2024-10-26 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cabeec83-7ab7-3b2e-bd1b-34d77bd06e39 | 0.82718 | -50.20196 | 2024-10-26 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae0ef227-716c-3e97-9f8c-912f6698b8d7 | 0.31057 | -50.99911 | 2024-10-26 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64094be5-4df7-3162-b941-98bd7eac6573 | 0.24729 | -50.83747 | 2024-10-26 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72906a20-3e34-3340-9f32-b1956d9c2608 | -0.0968 | -51.3275 | 2024-10-26 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e79e67a-9d90-394c-8c8f-18a1fbe08c31 | -2.24156 | -50.54775 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e826413f-f082-356a-93c4-90eed8ea7b38 | -2.24149 | -50.45921 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7eb1fd8-ca06-3cf0-97ae-93406e2d0d88 | -2.23988 | -50.53691 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 050cce6c-6380-3c37-b556-36a742a6808e | -2.23399 | -50.52852 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbc39cbf-65af-3c3a-9ad2-e29f01f88345 | -2.23345 | -50.53197 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b07f0ba-f7fe-3678-9c98-6aae6fbe1489 | -2.18764 | -50.50016 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50342dfc-1fa4-3a92-8c6e-8d61ce53a0e6 | -2.1871 | -50.5036 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012faa68-7c24-3994-92bc-4630a6005abf | -2.18049 | -50.50257 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1e56690-740c-3e12-956f-8daefc9d5a7e | -1.68037 | -50.46307 | 2024-10-26 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95778e23-2490-30f7-8f32-f0cbc3817a42 | -1.67261 | -50.44775 | 2024-10-26 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df9375d0-606a-3a49-85fc-3754b685b27e | -1.65553 | -50.44862 | 2024-10-26 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf5ca6e2-1c2e-32af-9567-dc62b10a44c3 | -2.23465 | -50.67736 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51306be4-cea5-3261-a37a-a8a93120fcec | -2.23134 | -50.67685 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c519adb0-5c2f-3f09-876b-ea30eca02060 | -2.22919 | -50.71189 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f993bb8-15a1-38e3-a362-3063a2a6a10c | -2.22588 | -50.71138 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aa377d6-499d-3adb-961f-efcb37610265 | -2.22533 | -50.71483 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc83c980-26b7-3a8d-90d7-30afbfb59973 | -2.22202 | -50.71432 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 142f519d-e657-33c3-a3e3-da95538f9805 | -2.22148 | -50.71777 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8f714f-f81b-3fc2-8425-fe12b79b9490 | -2.17201 | -51.05174 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d5d71e-dc8c-3753-b0ae-f6931d59b22f | -2.15378 | -50.88787 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8049bb11-657c-3ae2-acf2-68045763c3d6 | -2.14743 | -50.75543 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e93fc0b-71ed-353e-98e1-0f0e9c2e0e43 | -2.13791 | -50.68663 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5b8b91-e356-341e-807d-807d7828ff71 | -2.12088 | -50.73002 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd17950a-3736-33ce-a6c8-477ea0a9171c | -2.02489 | -50.77885 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 896d331b-56f6-3d1a-a225-212a74c2c428 | -2.01036 | -51.44934 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c12c4ade-8d99-30e7-9c1e-f8f328ab7539 | -1.88373 | -51.15711 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8bb456b-72bd-3029-817a-a117756096e2 | -1.52629 | -51.48846 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 608ed4ee-51a8-3745-a035-21031f72b3a3 | -1.52226 | -50.62553 | 2024-10-26 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0d2ddc2-0ad5-3d55-85c0-f843543bee48 | -1.52025 | -51.11178 | 2024-10-26 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccca5f77-a9f0-3d7d-8f90-fb9945b420a2 | -2.44964 | -50.99469 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a3f52f7-8d30-34e2-bdcb-8563a2dee9b7 | -2.44631 | -50.99417 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcbf146d-6c97-3274-af47-406b5d388d43 | -2.4051 | -50.82381 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 190021f0-bf4c-3b14-8cef-6d88f5689864 | -2.2985 | -50.85333 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b283108-727d-3cbe-bbe9-d8b905e02d8e | -2.29823 | -51.28663 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a4bf59c-8a0c-3d7d-920d-86b6278c3399 | -2.29545 | -51.28259 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2acfc127-2c6a-3e00-b8d1-5f9f224bd4a7 | -2.29489 | -51.28611 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e294c03-ac8e-3ac1-94a0-bed62ddef263 | -2.28729 | -50.77409 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69e173da-3c27-3d32-bdd1-71f364d0056f | -2.28705 | -51.14078 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1412166c-b9d3-3fc1-abee-9ecbc2d91313 | -2.28427 | -51.13676 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37bf68c3-63b2-319e-888e-82ab9777c772 | -2.28426 | -50.66387 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 851f421d-1981-38b2-8d63-b1e2a3adec20 | -2.2815 | -50.6599 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ef68c41-2afc-3313-a9fa-387dd2124513 | -2.27983 | -51.14325 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 032472f8-f1c0-32c3-9b3c-43e64607aaf0 | -2.27734 | -50.77254 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3d6d7f-9649-3171-b8b0-197d01a3ceb7 | -2.26771 | -50.66129 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aac7011-753e-38fa-9084-7fe47a6c3a18 | -2.2644 | -50.66078 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7757ea7f-a07d-373c-b3fc-f81e1380886f | -2.26313 | -51.24865 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6d67149-5412-382e-88b2-c29be3eba402 | -2.26257 | -51.25217 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0344a8e-c7c5-37d3-9152-52e5e3ecf9e5 | -2.26201 | -51.25569 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9bc09fb-da7c-3ad5-832e-de4ab6171fac | -2.24848 | -50.6972 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4bc87b-f041-3b2d-b88c-48fd90d47883 | -2.24802 | -50.74316 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c70cbf91-fa84-3f66-8919-ff89f3adf6f4 | -2.2447 | -50.74265 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32267b77-2630-3b28-a9c7-e36d8334e340 | -2.24139 | -50.74213 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7d1b6c4-f396-373b-9416-e2cc929fb0c7 | -2.20091 | -51.68432 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e989d659-8eeb-334c-b8a7-7f003bf4a55b | -2.15354 | -51.42813 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa5f993a-2e46-361d-a5d1-b2c9678b5224 | -3.22709 | -51.27768 | 2024-10-26 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 254faad4-febe-378f-ac95-fc7fcdad7bba | -3.2005 | -51.03771 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7980eaca-d6c3-3fea-8442-ad76d664d020 | -3.13166 | -50.61317 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README70.md)
