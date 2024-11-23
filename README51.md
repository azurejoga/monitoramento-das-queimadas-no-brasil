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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1cb6a4a-b991-3e95-994b-86064019ccfe | -0.26419 | -51.55317 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6971b86-3dd5-36fd-8f0a-5dacc699cec4 | -2.76245 | -54.07782 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c48aa6d-4f49-3b31-aaa4-0de625245082 | -1.62547 | -53.31308 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 543fc1a4-9636-38de-86c2-d458c2266241 | -1.13631 | -51.67912 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f721deda-2135-3198-8914-30656a82828f | -1.72231 | -52.72094 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd1f568b-74c1-363f-989b-20053df3a7ec | -2.38056 | -49.10525 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3fe8af8-c09f-3d07-8bfc-79f679d641f2 | -1.39106 | -55.18679 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b32a8e14-1bc6-33d8-b2ae-874baaa5d701 | -1.73422 | -52.71819 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fb62ff5b-8acb-34ae-8724-d3acc56d2ca8 | -0.88014 | -51.72682 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6844ebd-f5a9-3842-92a2-eb9196715b6b | -1.46328 | -51.11658 | 2024-11-23 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6667dfb4-1ed9-3a36-8813-c7dbdf0a4e70 | -2.20072 | -50.68071 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29f4d02b-4118-3a13-9881-c202ee0fd5fc | -0.90379 | -51.64952 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83f743de-28c8-3450-aa04-e14dad1c1394 | -1.42084 | -54.90591 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 819fbcd5-4a57-3a0a-b49d-2e32de435f82 | -1.62471 | -53.31038 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a50aae0-f811-3de6-932e-25c2378f1c11 | -1.83813 | -54.52218 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d6375ba-c8e2-3fe7-a1e8-64e9dcaa1de1 | -1.13154 | -53.40101 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49e35c17-88f2-3021-9ba3-d4c6839e6b36 | -1.67598 | -52.66552 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c9ceca92-6a4f-32ca-8b77-c16c76eef3b9 | -1.18957 | -51.93245 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 835763bd-93d4-333c-8a2e-2ab8bb098b9c | -1.63235 | -54.98976 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e191e84-b27b-3442-ab9b-af8cab7a2fdf | -1.22012 | -51.73874 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 624b49cb-60ec-356c-8403-521c58e460d3 | -1.60487 | -52.59684 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 70f3277e-067a-32a5-adde-c2737bd630c3 | -1.6398 | -52.70142 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd416749-35d1-30d1-a109-e8ebea620478 | -1.32863 | -54.20975 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b073b698-ab9c-39b1-a720-00ca64255fcc | -0.98518 | -51.72406 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fd6fd2-b4fb-3641-a7e5-5f7c1a18b754 | 1.2235 | -50.72398 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fb9742a-a961-310c-b7ff-da216c100966 | -2.94093 | -48.0186 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35924d83-c4c6-3404-942f-5d4842e829cf | -1.62277 | -52.6109 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fe7e13e-98c7-3782-bdfb-10d19d736408 | -2.7672 | -54.07045 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f4e66e8-03f9-3073-813f-370161ce7dca | -1.424 | -52.81757 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d805e678-6f84-3566-8494-e78844e9eecb | -2.76271 | -45.9336 | 2024-11-23 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2e2dfe0-612e-3060-b6d9-42be4d3ff2c9 | -2.69591 | -46.26998 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c898d3-4065-346a-b2b7-194f8b323e8f | -1.14647 | -53.39926 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce2d8ded-c138-3e13-9127-8807fae4a254 | -2.75159 | -51.88136 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19e0951b-b5a9-304e-88e1-8a302e6cf413 | 1.36583 | -55.93962 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed685372-536e-388f-a234-20d8cc7c4d23 | -2.4569 | -53.70539 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d97d89a4-32ae-3c79-b616-046a1404d174 | -2.0562 | -53.45907 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe4559c1-087a-3947-81e8-dbf797dd53a8 | -1.39331 | -55.19439 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a1d5d63-e260-35a4-b254-255de0abcfae | -1.3138 | -51.75194 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56f5e7f2-40a6-3b32-810d-90d219448210 | -2.16226 | -50.45643 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66a0f70e-025e-34a8-be13-f9dc9dc43335 | -1.04086 | -52.99487 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48d667ea-c274-381f-883d-06f812e15ead | -1.55001 | -54.59351 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3ef9be0-063e-3553-b605-8701facb2777 | -1.22542 | -53.68274 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bdc5a429-b625-3cde-a396-9cff9a846a20 | -2.76306 | -54.07387 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1e655bc-a889-38b7-8bcf-fcb2fea04971 | -1.4429 | -54.4912 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0125dd45-cf28-3b30-afec-b7f3b3519395 | -1.64355 | -52.70201 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7f3de769-2fc0-3395-ac20-c8ae89ec19f3 | 0.06632 | -51.14257 | 2024-11-23 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c8b006-d0be-394b-8d0e-00891604cb3c | -1.20431 | -51.97147 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6396a01b-cfc6-3375-ab8b-f244de0556f4 | -1.73286 | -52.72718 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8a0bc0bd-e10e-3be0-a5fd-46d9d9eb8ac4 | -0.76512 | -51.74285 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1f9759a-d619-3e1a-91b4-1613669a7aee | -0.88092 | -51.72184 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693f91bc-35a7-3c44-9929-2fe21575e56a | -1.7366 | -52.72775 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| db290244-d5f7-31b7-b3cd-8c14056b8d22 | -2.00174 | -49.51214 | 2024-11-23 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 536695a1-83a0-39f0-b655-6da6f54d8ae9 | -1.72912 | -52.72659 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8f739e4a-80ad-34ff-a97e-0b43c7d05c2d | -1.89333 | -53.32132 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 179e26ca-ef2d-3d65-bc9e-278840a2728b | -1.67538 | -53.20458 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 853288ac-3aee-3315-8b89-9e1dc275d325 | -1.2868 | -54.54688 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7f8b30-5e43-31eb-adfc-3007dd3b4059 | -2.58339 | -54.0398 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d58f339-4e77-34c2-a29e-bbfb891efd11 | -1.63803 | -52.40879 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5baff945-a614-3fc3-9997-532470f79eae | -1.45161 | -53.39155 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 013b3774-c8ee-3478-ae0a-7ea4ed445cd7 | -2.99392 | -51.45615 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d35e079c-8315-3aa6-9116-8577667858b5 | -2.8589 | -51.27931 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8430072-8c59-301a-93b3-5064605bb0ab | -1.19568 | -51.76587 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64e5c9f3-fe9b-329d-a19a-fbe5de546cf6 | -2.58632 | -54.04424 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20bfcdd-d31c-39eb-aae8-ddd80dce3c73 | -2.77134 | -54.06703 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdb89da7-5056-307a-a644-79e062d713a0 | -1.70225 | -46.86675 | 2024-11-23 05:10:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4d894c33-9915-346d-83bb-0c625b45c4ee | -2.56151 | -54.06458 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb3895af-65b4-3f37-a830-1dd9d9d0f786 | 1.39009 | -55.92186 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f9a52d1-39c1-3f3c-9045-2f040c60f92e | -3.19033 | -49.06079 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c9a96902-438f-35c4-ad97-1335f7e3cecb | -3.46637 | -48.25142 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0882208e-2e6e-3f86-b804-e061dffe2ad9 | -1.58211 | -53.81388 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97befa8d-1226-3e4d-b41e-72840b807d58 | -2.97055 | -51.42579 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99e88be2-e08a-3541-b281-4184cb1a1e1b | -2.58261 | -53.97488 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4b8a7c0-08e4-3991-9c05-c3c5d7e5e9e6 | -1.24518 | -54.0241 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94367656-704c-34be-a213-577ea2460d4e | -2.55371 | -53.97443 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e63f093c-8e33-3434-90d6-0bc6b548aefa | -0.92368 | -53.1002 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce3903d6-a8bc-3324-b596-6485f0acf9df | -1.62109 | -53.30984 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa450a2d-9723-30e1-90a2-ccf790990602 | -1.24867 | -54.02459 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c88fb37c-4986-313a-9977-9b7218523bf8 | -1.46797 | -51.11352 | 2024-11-23 05:10:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665c62b3-efab-3068-9c69-cc5209205973 | -1.35687 | -52.81858 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea6511a-ccfd-3fe8-aec5-59cbefa7a668 | -2.7474 | -51.8273 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2362419b-0ce4-3577-abcc-d190d8e42fbb | -1.63098 | -52.60752 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 900c2867-52d8-39fc-ad59-2dd42507ca78 | -2.73526 | -54.11403 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6161ff1f-a986-327a-96ec-5f6446507ab3 | -2.76671 | -54.05008 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce06aedf-e1fd-3db2-978c-8b70514d8d9f | -2.54985 | -54.04662 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9d313d6-f68c-32c2-be1e-774723b48c4f | -1.24273 | -51.61088 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cab75f97-b20e-3204-b3c7-8aa29333455b | -1.72143 | -52.71861 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8dd598e7-67e2-30cf-a434-9af28c2fd81d | 0.79716 | -52.00574 | 2024-11-23 05:10:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8578f15b-aaa5-33be-b07c-91046582ff0e | -2.95946 | -51.4431 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9083a6d5-82a4-3a08-b3f8-3fbb9cd3c74d | -1.74732 | -52.37963 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cab00f8a-4e99-3567-82c0-955d8bc0deb4 | -1.48493 | -52.11027 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcb366b4-719e-3598-b4b9-cbd76a8d0dca | -2.73878 | -54.11457 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1902c3f-0467-37f8-8b65-7c335d91f0b8 | -1.51234 | -54.40506 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71119a00-6d5c-3f95-b8ae-6e902fc74dc0 | -1.69574 | -52.76047 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88e7d90a-e2ca-3d29-802b-825128a714e1 | -2.0134 | -51.17077 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2629c52a-cce9-3694-9786-7ad5634ee035 | -1.19644 | -55.69506 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e80e3c-7411-30de-9818-c2bd61e18596 | -2.99542 | -51.45642 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d38c7644-8473-3e4c-a9f8-6f744781fa9e | -1.28833 | -52.26173 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48914893-a4cb-3c62-874b-581f5e18b808 | -1.53044 | -51.6276 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a0c49a-d670-3d9c-878d-80869e734dea | -1.22317 | -51.74082 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7ac3922-3e5b-3db8-9bbb-fc15739f034f | -1.7952 | -48.44371 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README52.md)
