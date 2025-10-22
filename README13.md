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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aef6389f-eb13-3ee2-86d0-38cb1bcc6efd | -2.77586 | -48.59016 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfb75029-c3cc-31cb-92a0-db036cd96227 | -2.02546 | -56.88275 | 2025-10-22 04:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f02417e0-b5ad-3602-a69b-3a39fcbe1299 | -6.35368 | -47.50059 | 2025-10-22 04:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df04b15a-5235-3836-a159-c7f8ce73c595 | -4.70682 | -48.12675 | 2025-10-22 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e728440f-623a-381a-bc49-66cee1ba420b | -4.14953 | -40.91253 | 2025-10-22 04:53:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0544d6ee-5f6e-3ac5-82b7-b87a1403542c | -3.25465 | -50.12782 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3078601f-c263-34c0-af30-ee1fcd032d5e | -3.40334 | -46.90371 | 2025-10-22 04:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cadc64c-019e-36ed-8caa-4a854d1e4a3f | -4.45968 | -43.23987 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf8e5034-91e2-36b1-9fc7-ecd7a87359ef | -4.00061 | -43.28037 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ed5cd2-1516-3342-a1c4-20acc3b92775 | -6.64047 | -43.60955 | 2025-10-22 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99a659b1-6778-3cb5-bb47-661c11bbcd9c | -2.48285 | -49.25657 | 2025-10-22 04:53:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa917446-099e-3136-af63-b8081c0901e0 | -2.37627 | -47.71989 | 2025-10-22 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db714ec-7108-3e78-90de-066f251d0916 | -3.05551 | -49.56196 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14920819-d4a2-3066-a331-5594c0cfa7ef | -3.56418 | -49.48623 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad7b63f-ca3c-32f1-9c61-f771c61f89c4 | -2.90931 | -48.73759 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d59114c-429e-30e8-9675-c89a1bfa7663 | -1.45437 | -55.50254 | 2025-10-22 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab84c3a0-34e8-3355-bb76-75190840a147 | -4.39741 | -43.30408 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6f70eda-9049-32df-9e0b-819035013dc8 | -5.97276 | -46.60633 | 2025-10-22 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b068544-d4cc-32d0-b807-7318c5e3a32f | -6.52981 | -41.43309 | 2025-10-22 04:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2da79ec-e8bb-3ce3-80e3-c7540bce0911 | -1.8981 | -54.07563 | 2025-10-22 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a4d1c89-57b8-345c-9d7c-c55c37b90a41 | -4.65385 | -49.54734 | 2025-10-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671a5fe8-08cf-3eaa-b176-ac179a6d5328 | -2.27112 | -57.01105 | 2025-10-22 04:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12a5e0f-872e-366c-ad2f-8cd49c64a7cb | -3.02278 | -49.46698 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70e1a0d-48a5-3feb-9582-b43f5f2b6524 | -4.84216 | -50.61945 | 2025-10-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4775acae-6b08-3e4e-9381-d98703e02c90 | -2.95259 | -49.34145 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d9cc3a-c077-390a-8839-9a04553eedfa | -3.26171 | -48.94296 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57613968-ead3-313b-a12a-c827991c96bf | -2.77273 | -48.58625 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3528831f-7ca6-38a9-b422-7da446f57825 | -3.44801 | -41.84625 | 2025-10-22 04:53:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8e196aa-4e5d-3dce-8ebb-381d21171a0f | -2.92548 | -48.30566 | 2025-10-22 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce1d3356-8c4a-38fe-9cd2-e10389965508 | -4.00025 | -43.27991 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 709339ce-2a09-3c52-a6f2-058638d90f1b | -4.6503 | -49.54679 | 2025-10-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f62360f5-39ac-3b87-bdda-93e8ad2dc3b6 | -3.15893 | -49.17255 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e37c87-aab8-350c-8149-455a7fc9af55 | -4.15647 | -40.90825 | 2025-10-22 04:53:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6ee917f6-31b2-3c28-8a0b-117bc5ac96b9 | -2.36707 | -47.65181 | 2025-10-22 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76b246eb-e793-3cb7-b125-6f59dba18850 | -4.44811 | -43.24487 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e4ff85d0-1493-3970-8963-7b2152fe67fb | -1.45347 | -55.5048 | 2025-10-22 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8878b871-c3f2-392f-a178-973169e75b44 | -3.33844 | -50.75162 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b1cbc8-9154-3f64-bd43-6f3204d68780 | -6.63668 | -43.79393 | 2025-10-22 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4051e25-a8ba-329e-9be9-26c8014ac4b8 | -3.9948 | -48.32692 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 167afee5-12d7-3e28-b952-e7dab0248f44 | -1.8714 | -54.49218 | 2025-10-22 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f60f507-bdfb-3e1e-a379-d90580f525a8 | -3.02519 | -49.45152 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da295003-9c50-35fd-97b8-c14b5a8d93db | -6.64092 | -43.6063 | 2025-10-22 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02ac4173-d715-3a21-acae-393594b8fb23 | -3.02047 | -49.45873 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c786475e-af76-3a34-966e-71536cd5b79c | -1.18559 | -49.20742 | 2025-10-22 04:53:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a28aafc9-906e-33d1-b57f-bf29ecd59e01 | -3.33563 | -50.74754 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b62f35e-fae9-37d7-af57-d4e2807c5568 | -3.24779 | -50.12676 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 397adab0-73fa-3314-ab8e-563fb3ee58a6 | -2.93088 | -48.30434 | 2025-10-22 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba71f27e-2c15-36eb-88f5-a90f09177c36 | -3.3855 | -50.27115 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8b45e16-b274-322a-86ea-7f55086c4e5a | -6.64582 | -43.61039 | 2025-10-22 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5bc3873-fe97-3dd9-89fe-c5fdf2295232 | -3.02458 | -49.4554 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64d92aa0-443f-3c80-b3d5-7ea8f95d8734 | -5.44701 | -48.09229 | 2025-10-22 04:53:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c512886-b227-3de9-97fb-d6338dab2569 | -3.0304 | -49.46418 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 294d5915-437f-3db6-8db5-525b0759fef0 | -3.52029 | -49.44332 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f13033-2b87-38b0-86df-b50db7e7c473 | -2.03871 | -56.62141 | 2025-10-22 04:53:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d5ea707-0be8-30bb-be5f-1d5df0b30d92 | -3.99142 | -48.32402 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57656088-353f-34ea-a43c-7568e8a72a85 | -4.44953 | -43.23495 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 574d64db-b0f1-3449-9056-a81386d7a5af | -4.22595 | -47.21621 | 2025-10-22 04:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92222845-69ad-3e56-ba7c-08032d1fcdfb | -4.44906 | -43.23824 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 45fd07d8-d5a1-3d5d-aa16-5991549bd3d6 | -3.01757 | -49.45432 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e533cdd-7cf6-3fde-8d7c-f1274a583205 | -3.02107 | -49.45486 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc6b8bd8-5319-38fe-bcfa-de6463ee1368 | -6.53143 | -44.36098 | 2025-10-22 04:53:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb2922a-1fec-3932-808a-e240d448ee79 | -2.77207 | -48.59044 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065f21b7-c071-3f47-b882-f374ffe0abcb | -3.71092 | -47.63498 | 2025-10-22 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d71015d-845d-3775-9f41-677fee391c1d | -2.38008 | -47.72048 | 2025-10-22 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce23043-a235-3ae0-868a-a3678df662d4 | -3.02749 | -49.45979 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51a558de-5542-37c0-b1a9-1ed0b0930c87 | -3.04169 | -49.52931 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74865c69-9e61-3618-b8d9-75116b8e938e | -6.64627 | -43.60711 | 2025-10-22 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88efb53b-8d74-325e-a683-bad82d31f997 | -3.25064 | -50.13097 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 810fbfb9-4f23-398b-bc5c-22f289f43062 | -3.66575 | -50.28787 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a9d5be2-2f04-3e06-9726-0579a28ee70e | -4.3049 | -48.06239 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3fb267eb-b150-39d8-8a29-af141c150ad7 | -5.9707 | -46.61084 | 2025-10-22 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9645132d-8492-3c9f-b53a-4173b2989301 | -4.45 | -43.23166 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 19b46def-77bd-3fad-959b-4ca743ba2823 | -3.52322 | -49.44778 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7235894-4db7-3c0c-85bb-3d0db5822f74 | -2.25335 | -51.92712 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8b2f4d05-c0d6-343e-9536-a390eacc8536 | -2.47933 | -49.25602 | 2025-10-22 04:53:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4378611-f983-36f6-b6b2-4e1c31a7c398 | -4.44858 | -43.24156 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cb3d8a83-392a-3115-bf81-9fc3b37346ae | -2.90751 | -48.98515 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52a70dbb-3be1-3939-823f-a1c0d95db165 | -3.66975 | -50.28471 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1d4f54e-0d43-3fa4-97b9-8f89f3fba8a5 | -8.99381 | -65.91891 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c034e43c-48f7-3d84-af9a-a0ffcfcc8d09 | -7.93998 | -44.84511 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 921be3bc-74e5-320a-8653-b9ec4bf17889 | -9.01361 | -65.92285 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c3b9b44-cd02-332b-965e-9be179590dd2 | -8.99716 | -65.91967 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2b5bfc96-3f59-3f61-a05f-9b726eb9c3c4 | -9.78037 | -63.8101 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1652bbc2-bf60-381c-8b86-1d77d43a8d50 | -13.45973 | -48.82442 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb19d3a7-3054-3249-88cc-764e08844342 | -13.00346 | -48.77402 | 2025-10-22 04:55:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533c7dd7-e006-3891-ae89-e1744a03dcc8 | -7.49 | -47.03016 | 2025-10-22 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65feea5b-c3ca-3b3e-96a8-de542039e536 | -9.48667 | -65.64278 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fdae43d-36fe-349c-ba3d-1d9cf06ab01f | -9.65123 | -65.2543 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebabba65-c837-3a98-b719-e8723d308c63 | -7.945 | -44.84581 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abf30f51-0a43-3ce5-825b-bf0b8d837b65 | -9.00576 | -65.94542 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4eed3c7d-c325-32b6-8bf6-a9d866750cd7 | -9.9058 | -65.02187 | 2025-10-22 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96daf603-31d1-3101-8c27-0aee56d4e0d3 | -9.00376 | -65.92097 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea6ef9e2-47d4-3f9e-9932-4c208c9dc8e6 | -9.72439 | -67.48122 | 2025-10-22 04:55:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f077283c-ccb8-3f1f-8a9b-ae40ab4bd998 | -8.1947 | -49.67552 | 2025-10-22 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 080bc9a0-f96d-320b-8204-6a0cbb5eeff2 | -7.65857 | -44.59068 | 2025-10-22 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85c56e2a-c9ae-38c9-9a40-6a5ecb82841b | -6.90901 | -45.17988 | 2025-10-22 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3f596a8-c7fd-3318-980a-08b0d39836cb | -9.00261 | -65.92674 | 2025-10-22 04:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dc7787d3-4a44-3614-8058-b7be7d6c43a7 | -12.51021 | -48.58359 | 2025-10-22 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4be6be8c-6575-3cc3-b0d3-1f0ac5b13456 | -13.45921 | -48.82819 | 2025-10-22 04:55:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 393f27bc-9c12-3b5e-8145-f7874e00f3be | -7.0777 | -44.11037 | 2025-10-22 04:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
