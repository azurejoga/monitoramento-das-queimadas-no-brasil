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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 158a97c7-130b-31fd-985a-5fce651840cf | -2.8123 | -45.1725 | 2024-11-23 00:40:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 381.7 |
| abc7c2b9-897e-3a5c-bd1f-e51c0ce3e724 | -4.5402 | -42.93 | 2024-11-23 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2b453230-e99d-366b-bcdb-679811ef8c0a | -6.5054 | -47.0414 | 2024-11-23 00:40:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e36c4f7d-2223-38ad-a26f-637a95ece148 | -3.2544 | -50.1168 | 2024-11-23 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e09ef5bc-e903-3d98-9532-54df4645ae0c | -3.1138 | -53.1163 | 2024-11-23 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 8ac04967-af10-3fff-bd5b-7d12f0063fe6 | -6.4867 | -47.0428 | 2024-11-23 00:40:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 936697ba-9000-3af9-8954-312e83f089f6 | -4.1566 | -54.5767 | 2024-11-23 00:40:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ae70b07b-4b79-3f68-98a4-3752701335bc | -3.4662 | -48.2565 | 2024-11-23 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 55ee963b-9df1-383e-8796-764532560150 | -3.4954 | -49.9191 | 2024-11-23 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f74581c2-9f48-3687-a43b-6ec932897a6d | -3.7539 | -49.9941 | 2024-11-23 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3eb079b5-709d-3d2f-b136-01da872e7853 | -2.6963 | -46.2719 | 2024-11-23 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 22578d2d-75b9-3b9a-9933-ffd485f71c59 | -2.8309 | -45.1493 | 2024-11-23 00:40:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 371.3 |
| 7b3b293a-b046-3db7-8e96-c27e1946162b | -2.8124 | -45.1499 | 2024-11-23 00:40:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 366.5 |
| a9e97568-3a9f-3f01-9189-4772c5107cb5 | -3.2569 | -54.2426 | 2024-11-23 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 33dd19b8-3d7f-3c50-8d10-c7244d2c9fd5 | -4.6085 | -46.5002 | 2024-11-23 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 7b362cd5-c9df-39d9-9d9b-8a4b25bd2546 | -1.7359 | -52.7385 | 2024-11-23 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| bd6534e2-e4bb-3a15-8a03-5d25696e6ccc | -2.8308 | -45.1719 | 2024-11-23 00:40:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 380.2 |
| 3af1b35c-3136-3b3e-8b3c-412cffc74ebb | -3.4663 | -48.2349 | 2024-11-23 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6ff6236b-4437-34d7-b621-db362fb46e30 | -1.1287 | -53.3951 | 2024-11-23 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 18e197c7-2b0f-30a6-b697-3eb3be6504b1 | -4.5216 | -42.9078 | 2024-11-23 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 534a2798-da5d-3df1-af42-fa9bb2cb347d | -4.67 | -45.6722 | 2024-11-23 00:40:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 71e8f7bc-8d23-3cc4-9c4b-1609091c985e | -3.7373 | -46.0322 | 2024-11-23 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 40c59bd9-c24e-35bf-88c1-35fd7c2f6b3a | -3.2385 | -54.2431 | 2024-11-23 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| c1da967a-6be4-3863-8a2e-4f03534c9a5f | -3.7538 | -50.0152 | 2024-11-23 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 7c2f1c1f-a131-36f3-99ba-f29991e53e10 | -3.7186 | -46.0553 | 2024-11-23 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 547dae7e-7906-34a0-88f7-add19a4d5210 | -2.7149 | -46.2713 | 2024-11-23 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e610630c-4593-391c-934c-fb73bf90aa56 | -3.7086 | -51.7888 | 2024-11-23 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 2fca14bc-fa29-3b04-b9a6-3325ffb82bbd | -3.7372 | -46.0545 | 2024-11-23 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 67e78380-dc96-3c34-9692-821de32c91e9 | -3.1814 | -54.321999 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c24a8303-9277-3778-a056-87bf877cc4ab | -2.6997 | -46.268002 | 2024-11-23 00:45:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21a3a06f-a55e-3b8d-a419-ff4af16ba663 | -3.2845 | -53.819698 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc59e1e-16a8-36f6-b1c3-429ca3da0698 | -1.9848 | -53.130901 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bfa03f0-e28d-3c83-b6bf-dde4be4447fc | -3.6844 | -50.102901 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ce8b29-3a0b-3cd6-baaa-04c6a0e73c95 | -1.2016 | -51.767101 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee63dde-513c-381f-97ae-0a6ab37db10e | -3.1115 | -53.099998 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500eb6c5-ca86-3ceb-91a2-88e5b15cc4e2 | -5.7355 | -46.259499 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 205908ac-0982-3590-a156-ac3cbc0a6caf | -1.6707 | -52.653999 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a413e68-986c-36fc-a26a-d6f995ccbe3e | -2.9668 | -51.4212 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3e2c9e-5bd0-3090-9712-bbc662622b77 | -3.0205 | -45.153999 | 2024-11-23 00:45:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52e4d937-6f3b-3fd7-817e-34f6aab6533f | -2.069 | -53.229801 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccf271de-10c4-352b-892b-36d1bf3c5f32 | -2.8272 | -45.1581 | 2024-11-23 00:45:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93d16900-e377-38b7-a639-a9190dee97fa | -4.4149 | -44.101501 | 2024-11-23 00:45:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0daffd8-99cb-3294-80ae-878559a7971e | -1.1258 | -53.3881 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e873a26a-4993-3197-ba66-470513b955a1 | -3.5218 | -53.5014 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a372394-e4a6-3bfa-bd23-4bb19bc86fc3 | -2.1971 | -53.6591 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337db166-2161-3832-b12e-e253a1126fe5 | -2.2326 | -50.507198 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d79dd9-b14d-3d18-bcb9-e03f95d4a73b | 0.7653 | -50.804401 | 2024-11-23 00:45:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3a2c1553-3082-36cb-9281-35239e00d798 | -1.2229 | -51.951599 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21cce788-21af-35ea-98dd-e6aaed94c2c0 | -3.243 | -54.229599 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7d6a995-0e24-3c26-90a9-158a13e92330 | -4.597 | -46.483601 | 2024-11-23 00:45:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68916304-0f34-3cd6-9f72-62119f0784b8 | -0.9051 | -51.640301 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6c4e5b-ddce-39b7-89c6-3fe215cef172 | -4.6006 | -46.498402 | 2024-11-23 00:45:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86701d5b-a100-32f7-a27a-936c733473db | -3.5164 | -53.796902 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b72901-c999-32ca-98c1-bcd87a6cb437 | -0.2615 | -51.526001 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a41086c8-1312-3ed1-8792-fcdac299685b | -1.5652 | -55.8848 | 2024-11-23 00:45:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2857b049-d67f-34a4-acf3-e20ba59ce07c | -1.7895 | -53.633999 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed4cf805-9628-3aa6-a1c6-68c80a58fde5 | -3.1198 | -53.0909 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf74ebf-a209-3765-94ec-92371b152a59 | -1.7557 | -52.665501 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c48dc96f-e98b-38ad-976b-882a359bc5a2 | -1.511 | -52.041 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e21ca1-364d-335e-8c12-c7648bfe043a | -3.2852 | -53.776699 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97d3fb68-4d99-3afe-a4fe-2bc93904226e | -2.85 | -53.9949 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f82212f-dbce-3f8c-abff-cb050106ec44 | -6.5002 | -47.0466 | 2024-11-23 00:45:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b22b78d-cf93-3da7-adee-fa0bee11a0dd | -4.6926 | -45.851101 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfafed39-bdc6-38f6-a250-691ccf5e62d7 | -3.7017 | -51.796398 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20527d2b-91d9-3ed2-b89d-405efc39b871 | -1.2096 | -51.757 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c4e8e5-7c04-3f7f-94b2-5c4f366e17cd | -1.2274 | -51.744701 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04548c70-579c-373f-bbb1-c66c0b582646 | -3.8266 | -48.981998 | 2024-11-23 00:45:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d899a9c1-a1b4-35d4-bcad-5a88e2daecf7 | -0.7629 | -51.739601 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dde445b9-bcdd-3613-8221-696ec0eb4855 | -2.5454 | -53.969501 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca6d09c-db30-3223-98d9-ad9c52b4343e | -2.5952 | -54.373199 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1c8cb6-a6f2-384b-a4ee-6c641a25b7a8 | -3.3171 | -53.2798 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0366d0-730f-32f3-b75b-c1db10562a7f | -2.902 | -54.591599 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a9cfe86-5786-33c1-9469-40e053fd457b | -1.8153 | -52.1563 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2103c76-34f4-31db-9688-864aa9afc467 | -1.0786 | -53.361698 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa49f20d-b48b-3d87-b91d-9e1fee1362e0 | -4.422 | -49.684101 | 2024-11-23 00:45:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e2fbf2-ce82-37f7-b99f-a7ff509a2433 | -2.8916 | -53.039101 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5ee1c9-2439-397b-a519-6ca5f1749116 | -5.1102 | -45.837399 | 2024-11-23 00:45:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9a836a-f7d9-3ae2-b051-52d605e44253 | -1.3872 | -55.185501 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde7c34d-18c2-3f00-83aa-d1277198e282 | -5.1063 | -45.821201 | 2024-11-23 00:45:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc957deb-cb0d-30a0-bacb-ca058fb87870 | -1.6166 | -52.597301 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83be542a-840c-3f6d-a896-f530efed6ac7 | -2.2003 | -50.681198 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0bed8a-2089-33fb-8a89-4f5d98985925 | -1.156 | -53.658699 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b7f36f-322f-332f-98ed-2002dbdafe25 | -3.0787 | -54.552601 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104754a1-0158-3a0d-a3b4-fde33eadbbca | -3.3005 | -53.844898 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f29c703-1376-3207-891d-6a61d55c8cd5 | -1.1175 | -53.397202 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2d973f-c9b8-3c59-90b1-9baed99828db | -0.9069 | -51.6483 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0e2b72-5c19-3df2-acd7-c7f51d8445cc | -0.9167 | -51.646198 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a43fc3-4236-3624-a236-1d948b315c24 | -2.6357 | -54.2784 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8706e508-b483-33da-8be6-6f71008be293 | -5.3698 | -50.8433 | 2024-11-23 00:45:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41396c68-57e0-3713-839d-c9a38a214195 | -1.1273 | -53.395 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf3f82e-3014-3476-a94c-37ff8138797c | -2.6114 | -54.0336 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32b6e13f-4bb1-3571-ba64-62b40f45aeb2 | -2.5819 | -54.0401 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d648c04-bc0f-31c4-b4f8-6ebc1c98f4af | -0.2666 | -51.5942 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7d596567-c66c-32fe-910a-c757da851758 | -1.6593 | -52.694698 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3780ce65-52d0-3ec6-a7dc-aac06f99cceb | -1.2015 | -51.948101 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a38dad6-5813-31e4-93f6-c634622f20fa | -3.0691 | -53.277 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20924519-ef51-32d1-a6a5-bdc730b0c8ac | -3.3112 | -54.486801 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 216fb6a7-89e6-3e02-a22b-fdfdd56926f0 | -3.6385 | -50.216801 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841bcbce-d65c-3fed-bb22-ec1e7a80c4be | -3.8924 | -46.109501 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7d9e6e4-01b2-36f9-a4b2-6ac021908408 | -1.2586 | -51.745998 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
