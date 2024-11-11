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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd34fd45-1379-38a6-b7fb-c362d1939010 | -3.2244 | -53.0524 | 2024-11-11 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f41ebafe-83ae-333d-89f5-3e88118a32d7 | -3.0295 | -50.9815 | 2024-11-11 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f28d387d-7cce-3af0-bac5-dfed279723bf | -17.2933 | -57.4857 | 2024-11-11 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 3ebd2a94-d480-3c0b-8d38-d9804144d4cf | -2.2297 | -53.6824 | 2024-11-11 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c11dc0ef-a3b9-3c4c-8180-db269c1d388a | -3.1458 | -54.4859 | 2024-11-11 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 901ad36a-8437-3533-9997-ab94a3da0bed | -2.2298 | -53.6623 | 2024-11-11 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| cd02066f-7851-37c4-8831-f68b74684240 | -3.0295 | -50.9815 | 2024-11-11 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 903512f7-fe19-3f5f-8c15-a97111647224 | -17.2737 | -57.488 | 2024-11-11 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| b113a3c3-ab28-38b1-9a8a-d3c0f4d6a548 | -2.189 | -48.3815 | 2024-11-11 02:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d4f4ff08-2ce4-3651-b75b-4614799357d2 | -17.313 | -57.4834 | 2024-11-11 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| cac8f93e-fdeb-340d-991c-85c3407bcc92 | -3.2428 | -53.0519 | 2024-11-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ef9adb9b-24fc-3fc6-8e5e-47472ac72b32 | -2.2075 | -48.3811 | 2024-11-11 02:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| be14b3cc-6caf-3eb6-aa66-b96b765b5f5d | -3.0213 | -53.2607 | 2024-11-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 96975c9d-4f98-34fa-8ccc-91ff75dbeda3 | -2.248 | -53.7426 | 2024-11-11 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 1c69829d-83a1-35ce-9ded-5b3ce77585cb | -17.2933 | -57.4857 | 2024-11-11 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 5da843eb-14da-368a-bcfe-05f7445bb3c8 | -3.2427 | -53.0722 | 2024-11-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 862d4248-473e-30c1-a0b0-6ade18f33ecf | -17.2936 | -57.4652 | 2024-11-11 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 7c71ba6f-019c-398a-b071-d4e511199e7a | -1.3872 | -52.4169 | 2024-11-11 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 03284a96-be09-3302-b8ef-10b319cdf946 | -3.5346 | -45.7061 | 2024-11-11 02:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8e21b1cc-f057-3225-9ce7-b5329146016b | -2.4367 | -51.948 | 2024-11-11 02:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ef91c10c-06c2-3c2f-9664-daea2541b21d | -1.4057 | -52.3758 | 2024-11-11 02:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b222f2d6-37a3-39a2-bf6e-2f7bf8becddd | -2.2297 | -53.6824 | 2024-11-11 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| cda7b0cd-13f5-3633-a6c7-786442aa45af | -3.2244 | -53.0524 | 2024-11-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 153f6369-b40f-321a-9c1d-03d0e967d3ef | -3.0214 | -53.2404 | 2024-11-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4250143c-9018-343b-9357-8afabdf1f2f4 | -2.8508 | -49.432 | 2024-11-11 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 70137ea0-6227-3435-ad69-2f29f3b0cc22 | -1.8425 | -46.582 | 2024-11-11 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5eaac250-1220-3b3e-9426-b02251b2faba | -2.2663 | -53.7422 | 2024-11-11 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b59b5cd2-952b-3990-a01c-5235402d4648 | -3.0295 | -50.9815 | 2024-11-11 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ee7af808-ab48-3598-99bb-9c3c35ef68e6 | -2.8508 | -49.432 | 2024-11-11 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9a5fc431-ecd0-3aa4-85b2-97a1efb7ad5b | -17.2936 | -57.4652 | 2024-11-11 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 38cbff2c-fa41-3e64-be4c-6e5aadbc40e7 | -17.2933 | -57.4857 | 2024-11-11 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 9005a1a2-c6d3-3747-ae06-439ae47de078 | -3.2427 | -53.0722 | 2024-11-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 563230a4-ef63-3278-b2e7-638d116aa7e6 | -2.2075 | -48.3811 | 2024-11-11 03:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| be8d02b2-73c7-33a2-bc5e-7d6a95923c40 | -2.248 | -53.7426 | 2024-11-11 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| a7d13326-6005-3cf4-bd3a-be275a2ee36e | -1.626 | -52.5362 | 2024-11-11 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0d4af914-fd69-33c9-8d9f-2792f9a6e392 | -17.2737 | -57.488 | 2024-11-11 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 8105e49e-8a9a-3c76-a399-f4142808d008 | -1.8425 | -46.582 | 2024-11-11 03:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0172620f-c634-3e83-8ef9-460b85752c57 | -3.1097 | -54.2865 | 2024-11-11 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 32959454-fa3a-35a5-b439-8a3b4113b4bd | -3.5346 | -45.7061 | 2024-11-11 03:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 68eb203f-ae6c-3a26-81d1-4453b7a71d61 | -1.3872 | -52.4169 | 2024-11-11 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b685b6d9-1c81-377b-bf23-742ef53493e0 | -1.6444 | -52.536 | 2024-11-11 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8d875c06-f26e-325a-8e46-b303380efc52 | -3.2244 | -53.0524 | 2024-11-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f52ad999-9b47-3acf-9126-e23498a8b919 | -3.1458 | -54.4859 | 2024-11-11 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 28be9dd5-dddf-39b1-8edf-0ca7d7f5c3ce | -3.2428 | -53.0519 | 2024-11-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f49b0046-e7cd-35f1-abd4-30395173f11e | -2.4598 | -50.3911 | 2024-11-11 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| aa3d7c58-c2e4-32d4-90ee-c9d26017662d | -2.2297 | -53.6824 | 2024-11-11 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0d4f63dd-dd42-350d-a03c-fcead366824b | -1.4057 | -52.3758 | 2024-11-11 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e8e2bc18-708d-35e5-ac21-06b42938a92f | -2.4367 | -51.948 | 2024-11-11 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 37786131-b671-38c0-982a-8805fe006103 | -1.6443 | -52.5564 | 2024-11-11 03:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 514f86bc-827e-3bc4-831a-7035c4d67edc | -2.2663 | -53.7422 | 2024-11-11 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| cfec9eec-68c1-370d-9a7c-63152da795d8 | -3.0213 | -53.2607 | 2024-11-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ab899e8d-aa95-349e-a0f1-fe04f2e6adb7 | -3.0214 | -53.2404 | 2024-11-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4b521f40-c0bc-3681-a91a-aa7559ade76d | -2.189 | -48.3815 | 2024-11-11 03:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b91e28b1-2512-3e0f-ae3c-1bfce442e53d | -2.2298 | -53.6623 | 2024-11-11 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 738d79f6-8303-3c8e-8d64-f532950ed4b6 | -23.9312 | -54.034 | 2024-11-11 03:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| a8f5b10c-d79b-345e-9fc3-c476d8962f05 | -17.313 | -57.4834 | 2024-11-11 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| b8bcc520-108a-32bb-b0e6-7d7ae49acc21 | -2.76 | -49.32 | 2024-11-11 03:00:00 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2887f73-e243-3ffd-94be-ad0db5dc0bde | -2.2259 | -48.4021 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 74fdc0f2-2eb3-3c4d-b061-f52aca2c89e8 | -4.7023 | -46.3842 | 2024-11-11 03:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 27dda1d3-9fc9-32d0-b425-d148d4da21ef | -2.8508 | -49.432 | 2024-11-11 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 339954c8-201c-3eef-bd8e-b1ac918a44d4 | -2.2075 | -48.3811 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3c975a26-270f-3968-9f51-73b97b2df8b9 | -17.2933 | -57.4857 | 2024-11-11 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| 9378fcdd-7c8d-30bd-9d5e-b6a4d02c0ce7 | -1.8425 | -46.582 | 2024-11-11 03:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 83cdf0ce-f17f-324e-9a4a-eaa138a84c2b | -17.2737 | -57.488 | 2024-11-11 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 2332896a-4d3c-3437-86e0-fee1ced3d9ac | -3.2024 | -45.2256 | 2024-11-11 03:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 7c8b4871-563e-3c7a-a31e-83d4a09fc14f | -3.2244 | -53.0524 | 2024-11-11 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9ecefcff-b805-3e83-ad26-d4339d59d585 | -17.2936 | -57.4652 | 2024-11-11 03:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| b2daca7d-6c5e-377f-ab75-b72d6892741a | -3.1458 | -54.4659 | 2024-11-11 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9698f057-7921-3f0a-85c8-02ece0fd8652 | -2.2445 | -48.3802 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5ef44344-3ee8-3984-bc9c-4ffe6df293a0 | -1.4057 | -52.3758 | 2024-11-11 03:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c1fcdf9c-1479-32ee-80d8-fcf55f5c5e25 | -3.1458 | -54.4859 | 2024-11-11 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 365841ea-4f9a-3ae4-be9f-302e524d826f | -3.0214 | -53.2404 | 2024-11-11 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 15edbcb3-d55b-3b38-87b2-6ba827b3a677 | -4.7209 | -46.3832 | 2024-11-11 03:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d4066548-03b7-30d4-8cfd-b8f759ebfc9c | -7.8661 | -45.9247 | 2024-11-11 03:10:00 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 05ef3661-4151-363c-ae3a-6716f7288884 | -2.189 | -48.3815 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 843bc982-66ec-3099-bda3-b2a3562bd192 | -2.4598 | -50.3911 | 2024-11-11 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 48b65549-5e0b-3e9e-9920-eb6d04a2ddc9 | -3.2388 | -45.3818 | 2024-11-11 03:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4ee8700f-17df-3d3e-bfa7-79d3d8053cf5 | -3.221 | -45.2249 | 2024-11-11 03:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 538d14e4-7bca-37b4-92a1-9b6e75655cbf | -2.2444 | -48.4017 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| be1f219b-5f29-3dd2-89d3-32e48f825d06 | -3.5346 | -45.7061 | 2024-11-11 03:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b5d5afcd-d687-3a1a-bc1d-9181847526bc | -2.226 | -48.3806 | 2024-11-11 03:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 893d584f-14ba-34dd-8516-db0c0b8e0526 | -3.0213 | -53.2607 | 2024-11-11 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d8d99b37-35c3-3f2c-a0f2-53e9d6226d00 | -3.5346 | -45.7061 | 2024-11-11 03:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 35248801-d7e2-3363-81e9-3cd14ac0bc3a | -2.2297 | -53.6824 | 2024-11-11 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6bd5ece3-4bd2-397d-9fdc-d72469b872da | -2.2298 | -53.6623 | 2024-11-11 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 82ed2305-522d-3ed2-9840-be4061e8488e | -3.0213 | -53.2607 | 2024-11-11 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 75667222-2d9d-3189-811d-862391efaef2 | -3.1458 | -54.4859 | 2024-11-11 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ff867e2a-4db6-30d7-97d7-e7f94fa44871 | -1.4057 | -52.3758 | 2024-11-11 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 11cf3526-c43f-3d98-80c7-3c876a11aa29 | -2.248 | -53.7426 | 2024-11-11 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 30db647b-2156-3139-b06e-3239773308a0 | -3.221 | -45.2249 | 2024-11-11 03:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2af16ee3-0af6-3b58-b360-35a248c5b5cb | -1.8425 | -46.582 | 2024-11-11 03:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 462466d5-ee6b-36d4-b216-f8a7f5f8f20c | -3.2024 | -45.2256 | 2024-11-11 03:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b0a51a76-48e1-304e-96f1-98d2dc4d91d3 | -17.2936 | -57.4652 | 2024-11-11 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 30e85aff-f740-35d4-9188-3c7082f3e274 | -17.2933 | -57.4857 | 2024-11-11 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.4 |
| f7351667-909e-320a-88e4-2fede5fe059c | -17.2737 | -57.488 | 2024-11-11 03:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 7bfcb7dd-0f79-3de3-a363-241122881b24 | -2.2663 | -53.7422 | 2024-11-11 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6adff455-a36a-3303-938c-272bf93f0c5d | -3.0214 | -53.2404 | 2024-11-11 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8fea2314-1218-3cbf-929a-7273eb3c6a8c | -2.2075 | -48.3811 | 2024-11-11 03:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3f005996-9f42-35f1-8f34-a9ebf24160e6 | -1.8425 | -46.582 | 2024-11-11 03:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c039d37e-6e1d-3098-be43-df6179086946 | -2.248 | -53.7426 | 2024-11-11 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |


[Clique aqui para ver as próximas entradas](README23.md)
