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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2d9c682-5902-3f0d-a7b5-40218d020277 | -8.68981 | -49.92617 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc7340b-009c-3910-baa0-ec9d1e8e6b60 | -8.68926 | -49.92963 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6ace701-14cb-343f-88bf-20e2e0248396 | -8.68375 | -49.92167 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cedd91d3-ca14-32fc-a796-608299ea84aa | -8.68045 | -49.92114 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 532bde01-3c7f-37db-98c6-ec288a4a4042 | -8.65405 | -49.93457 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b70fed1-e55a-3062-948f-8097af09f378 | -8.59104 | -50.07729 | 2024-10-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90fcad22-3108-3700-8961-3a7d1365b01f | -8.53478 | -48.77707 | 2024-10-13 04:40:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c402a7-4e64-3a5d-a0c1-0384393f074a | -8.53144 | -48.77653 | 2024-10-13 04:40:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11c435c-13a5-3dfa-af3e-c4c1c2e4a47e | -8.5281 | -48.776 | 2024-10-13 04:40:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30fa1ee8-d631-3a49-933b-4b669880e28d | -8.33566 | -49.97233 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af1e890f-0cc9-3737-9508-d8991c6593e7 | -10.5572 | -49.95006 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d6c35db-2715-3b99-8d3f-010529bdff08 | -10.54121 | -49.94394 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0280735-33c6-39f3-8d2a-8cbb6547063a | -10.5302 | -49.94936 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e53bc52-501f-36f9-9534-0c2c044b4e99 | -10.52966 | -49.95286 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1af1ff97-1a28-3435-94e1-3d345e96d7cc | -10.52911 | -49.95636 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4de894e6-b154-39f1-bee8-8b2e7edb7583 | -10.52581 | -49.95583 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be472336-76c4-317e-a2e4-be1997b5a1ed | -10.52526 | -49.95933 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b57faaac-42e1-3415-8c2c-3c43c403e116 | -10.5225 | -49.95531 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e49543fa-4147-3057-951a-c659e0063a83 | -10.52196 | -49.9588 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a42149b2-d8fe-38a0-b133-934c5b098737 | -10.51979 | -49.9728 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2a6b5fc-c044-343a-9602-fca6d0016047 | -10.51865 | -49.95828 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b57d3d88-87c1-395e-9922-b7b6b195f5b0 | -10.51811 | -49.96178 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a98b20b1-1f86-3fa2-9df9-dc6ad188a6b4 | -10.51594 | -49.97577 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e136bded-3284-3370-b86b-7bb3712e7f36 | -10.51535 | -49.95775 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1338f2dc-3861-3d90-91bd-e801c9a20c8a | -10.5148 | -49.96125 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 807010ca-f270-31cf-bf23-648215a0b0e6 | -10.5115 | -49.96073 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93a53192-b651-3b34-8674-17ea720389a7 | -10.48892 | -49.95009 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11ad6902-b021-3259-9a9f-aab20cc84817 | -10.48837 | -49.95359 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aceac274-2d9c-3b57-a686-56c4cc1fab21 | -10.48506 | -49.95307 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df04c770-ca21-3d79-ad5c-22b917361969 | -10.48452 | -49.95656 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fea87d93-44d0-3d82-9d88-1f49a3d8b489 | -10.48121 | -49.95604 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00a92623-1a61-39a3-bd2d-de20386aa413 | -10.45644 | -49.96284 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd0d86e2-f2c2-3dc4-a27b-2e525620ce28 | -10.45461 | -49.36033 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2922594-f53a-3d4c-9341-95b6ca986d1e | -9.96208 | -50.08033 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd7eea32-2902-31cb-b38b-bc3af3aa6d37 | -9.94553 | -50.05629 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a854b10-c98d-35d3-a88c-756f8125615d | -9.94125 | -50.05866 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b33d1c01-9174-34be-b4e0-7b6da9929699 | -9.90551 | -50.07081 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 821b0952-94c1-349f-b85e-4733957bfa27 | -9.88846 | -50.07167 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cfa1dc1-34ca-34a8-8065-d0e58d2ed9bf | -9.88144 | -50.15969 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c59b084d-e961-3407-90ff-d551ed6313ef | -9.87814 | -50.15917 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3001769c-ac35-397d-bd78-a718152436e8 | -9.87484 | -50.15865 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b842c32-85ca-3276-84c5-bd562988a1e8 | -9.86824 | -50.15759 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5da7edb6-9345-376d-8e67-2a3a6bb5e229 | -9.79481 | -50.06046 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0fc8cff-ccf8-3de6-8212-3b6f5f2c2417 | -9.77511 | -50.12149 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beaf1ea7-350c-3fb9-a48b-a5b1a5aa04ec | -9.77507 | -50.10011 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed61b2b1-3da9-331a-a4d3-afc3c3d36aa8 | -9.77344 | -50.11053 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1873733b-2907-3a78-aa8c-859861fd0eb9 | -9.77289 | -50.11401 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5926df6-313b-3b1f-8a81-7ab1f14d54b8 | -9.77126 | -50.12444 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8abbc75-0530-3aaf-a362-8dc124968f77 | -9.75069 | -50.44907 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae22ada2-f8dd-3098-b465-773e3609196c | -9.62476 | -48.98617 | 2024-10-13 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddefa664-495f-34c8-8417-1172dbf0c524 | -9.62341 | -49.12819 | 2024-10-13 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc9dad4-d12f-3d02-a7f4-19aa937e25a0 | -9.62196 | -48.98209 | 2024-10-13 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56bf73d4-0e0b-324b-8125-e368b685f577 | -9.62141 | -48.98565 | 2024-10-13 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4eeaccf4-1bc5-3afb-b982-314301443eed | -9.58309 | -50.0867 | 2024-10-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4045887a-ce09-3def-a171-6d8815ea1af5 | -9.54862 | -50.22011 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a0a4c5b-1989-395e-8241-bedf5600960a | -9.54587 | -50.21611 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd379b4f-61fd-3f77-a3c0-84871cb784d9 | -9.54532 | -50.21959 | 2024-10-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ee74cc7-542b-3863-9cd8-bdf0fe10050f | -11.92319 | -50.80919 | 2024-10-13 04:40:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c59e9217-be44-3ab7-9352-52dc26fa3157 | -7.20929 | -42.28047 | 2024-10-13 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc99d050-de9d-350b-9e03-78ec4e9692b4 | -11.37081 | -50.03361 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20ed1a27-ef04-3f7e-af0c-4c7e1853ffb1 | -11.15427 | -49.69549 | 2024-10-13 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5879e1fb-b518-3e32-8144-0cbc6f82df59 | -10.80428 | -50.56607 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aeb3657-5fc6-3a96-ad92-98703c48d66c | -10.79768 | -50.56501 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd387451-0429-375e-aab8-5acdf8ee364d | -4.41032 | -49.76105 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9848f43-361e-31cd-a615-b2270a4d15f3 | -4.40848 | -50.57221 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b8abbd1-aa39-3193-ac80-fc814b3f409e | -4.4081 | -49.75359 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55f595a9-dc6a-326a-b9fc-6db0f884a67f | -4.40791 | -50.57582 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d64c191-0781-36a4-91ae-badafddf8a50 | -4.40755 | -49.75705 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71047672-4a06-335f-9bda-7a7bb3d17e39 | -4.407 | -49.76052 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89b9f5ae-de0f-330e-8d40-65a42cad2ff6 | -4.40646 | -49.764 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f73d5642-c48f-3eb1-81d1-7339e2515c67 | -4.4051 | -50.57169 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91340067-3aac-3bff-a903-ac239e117940 | -4.40478 | -49.75307 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c67772f3-3fd6-3460-ab2a-9c0948ffbbcf | -4.40453 | -50.5753 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e62322a-c631-3c68-a7d3-cbe8d16aca64 | -4.40423 | -49.75653 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13491983-e939-354a-ab78-fcf4114130d7 | -4.40369 | -49.76001 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 853df7e2-c4c4-3686-b81b-5f4146f7aa15 | -4.40314 | -49.76347 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c38b4277-3e38-3ad6-8524-4441edb9ee42 | -4.40146 | -49.75255 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99a0e29c-2be8-3d75-ad7f-d34ab97d4c6d | -4.40092 | -49.75602 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5a28b4d-faa8-3d98-a39a-9146e0c605a3 | -4.40037 | -49.75949 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3422c698-7d2c-33fa-9d14-e3bb2d1b4d2c | -4.39982 | -49.76296 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 191563a9-8ab3-393f-acf5-51bb0abe0a02 | -4.3976 | -49.7555 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98bd6b69-c7bc-32a3-8205-8a4b1dc62647 | -4.39705 | -49.75897 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0b2f07d-aba9-311c-92fd-a116a7b11fcf | -4.37454 | -50.80944 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd35f357-7ec0-3875-8292-ef7c5a150885 | -4.36492 | -50.80416 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f21b323-b602-363a-a22e-2a4bc4dacba6 | -4.36152 | -50.80362 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c39c85b-d59c-3a54-ba9c-1dfb86ab76ce | -4.36094 | -50.80729 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c405876-0610-36b9-a74e-822e5c6cb963 | -4.36035 | -50.81097 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b1f9ffe-7812-3faf-a122-92339a55b044 | -4.35753 | -50.80676 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1259166-2c90-3fd0-a686-f5c1897cf3a8 | -4.26989 | -50.60639 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| adf56d7c-bb82-352e-97bf-a257bd3a4fd7 | -4.25924 | -50.58612 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b254df-9ca2-3f87-8857-3e66570a8bbf | -6.72097 | -50.96766 | 2024-10-13 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d2425c2-ff72-3696-9a6e-bfe2758b148b | -7.95225 | -50.48014 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a30447a8-03a4-3c67-b76e-b0c869677c36 | -7.85385 | -50.30741 | 2024-10-13 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d0540a-0518-3fec-a93f-b613ee0fe976 | -7.80982 | -50.19667 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 856c7b6b-3467-3278-8c20-d9c388c6d22e | -7.80652 | -50.19615 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c12f929-7b59-386b-8234-243ddec0f0ed | -7.79445 | -50.27251 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d2918d8-1bce-3162-83b3-bb2cfd9bfa09 | -7.79333 | -50.23674 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c181457b-3e36-3a17-a819-a97fa903d416 | -7.77567 | -50.17702 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb573aee-8560-3598-9450-56c3a64d1079 | -7.67947 | -50.24709 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbf1208f-e64c-3826-ad3a-d34ab5b943ae | -7.67892 | -50.25056 | 2024-10-13 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
