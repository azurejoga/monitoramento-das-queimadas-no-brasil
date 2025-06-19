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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f50cd8b-9e73-333d-badb-4bed8e275426 | -8.1229 | -43.116402 | 2025-06-19 00:02:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37e9ade1-6b1c-3126-aad3-0488579784de | -8.1253 | -43.127701 | 2025-06-19 00:02:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8dcb784d-0624-3f98-9d4e-71b495d6fdf7 | -7.1504 | -44.0555 | 2025-06-19 00:02:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b2be2157-9817-3296-89e1-f21d4f31268d | -6.2358 | -44.641201 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd977341-61b9-3ff8-b4f6-0d87fa7801c3 | -13.5632 | -42.913399 | 2025-06-19 00:02:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41ea393c-4a4d-34d8-987f-bd1562532ca8 | -7.2268 | -43.087002 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8aba2e57-47e8-31c7-9271-60f22bd221c7 | -10.6354 | -49.442501 | 2025-06-19 00:02:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fba86af7-01d7-364a-bc0c-8c0e4855b4c4 | -6.8505 | -45.553699 | 2025-06-19 00:02:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6ba4754-d78b-336d-81df-f2e6919a6184 | -4.7604 | -47.548599 | 2025-06-19 00:02:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e53f8e5c-3308-371a-837d-bfbdc6f266e3 | -6.2884 | -44.2253 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5324805a-bc47-356f-92cb-2d28450a5e58 | -8.0692 | -43.104198 | 2025-06-19 00:02:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ad0c14d-6617-3f4e-ada7-081331b6f553 | -7.2463 | -43.082802 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 006d6460-6613-3564-94f9-7e6bfee7b77a | -12.2662 | -44.598202 | 2025-06-19 00:02:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4c17b74-c9e7-3b4f-aeb4-1bb505621406 | -7.2245 | -43.076099 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61e1d24f-7fe9-3ba3-a72b-4cb3b7c46e5f | -3.081 | -40.0784 | 2025-06-19 00:02:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ea31029d-65f9-389f-8ab9-502571b5b16a | -9.5516 | -40.352901 | 2025-06-19 00:02:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a06e0a5c-0187-36d2-abfe-58e9a7949a1b | -7.2389 | -43.095798 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b19d69b-0d65-30ed-b4e2-71e8bd364b42 | -3.08066 | -40.07914 | 2025-06-19 00:03:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3f69af1c-f668-3c23-b296-5cbd1d01a182 | -3.02943 | -49.41444 | 2025-06-19 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 0bb3e6c0-096f-3192-b226-253371f101a5 | -4.77304 | -47.57838 | 2025-06-19 00:03:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 269a33e6-209c-3bf1-9480-aefa5f22f5d6 | -3.04067 | -49.44157 | 2025-06-19 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6f401409-ec6a-39c5-b653-305dd757cd8b | -3.03414 | -49.44912 | 2025-06-19 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 836ead80-e450-3575-9147-544e9655a4d5 | -4.76971 | -47.55291 | 2025-06-19 00:03:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 288c9e77-513c-3898-a213-53dc9448a28c | -8.1267 | -43.1154 | 2025-06-19 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| d564333d-610c-39c4-a204-64e4650644a1 | -16.305 | -58.2474 | 2025-06-19 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 50dee157-86e6-328d-b4d1-0f0d2574a777 | -11.9329 | -58.7588 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1af9a1aa-cd2b-3898-87dc-c82e21bd5595 | -11.5366 | -56.9847 | 2025-06-19 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 6830050a-d6ee-32ef-afe7-70eb4166b275 | -11.9707 | -58.756 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 224.2 |
| f19535fe-ad17-371b-856c-7c6037227646 | -13.9733 | -58.1144 | 2025-06-19 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| de00a9c4-0529-34ea-8f6e-a6a638fa9a4f | -16.3047 | -58.2676 | 2025-06-19 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 5f0cf99d-3993-36b0-b8c1-412f6853fcf3 | -14.4467 | -48.9063 | 2025-06-19 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1725b140-d0d3-36ca-a8da-15ae6edb4e8b | -11.9331 | -58.739 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 62915e3a-bf04-347c-af48-c2b979ee57f9 | -10.6489 | -49.4483 | 2025-06-19 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d0660eeb-a877-3019-9837-cff6bccdaef2 | -7.2408 | -43.0664 | 2025-06-19 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| dc12761c-6ac5-3395-b93d-77e9c7e189a9 | -8.1264 | -43.139 | 2025-06-19 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 0608ef4c-5b13-3797-9609-b52004e265de | -11.952 | -58.7376 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 281.0 |
| d965c8cf-0b95-3d11-9af7-f64479dfdafe | -11.9518 | -58.7574 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 324.7 |
| 17ae99a3-ccf7-37ef-8167-dee0143a32a4 | -13.5784 | -59.2026 | 2025-06-19 00:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 182ce125-f784-344d-a2a6-e21deec463ed | -7.2405 | -43.0899 | 2025-06-19 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 197.4 |
| 91cb973f-da32-382f-a712-c6182bb65024 | -4.7686 | -47.5686 | 2025-06-19 00:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3250077c-301a-3bde-91b1-5cb7e9a99242 | -11.9709 | -58.7362 | 2025-06-19 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 25e4f268-ed35-39ff-ba1a-4e6c3f6077b0 | -10.0972 | -52.7376 | 2025-06-19 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 52a58e35-163f-3712-a9cc-9dc1f32245d2 | -11.952 | -58.7376 | 2025-06-19 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 328.4 |
| be14d536-319c-3fc1-aa2d-cf82465a81bc | -4.7686 | -47.5686 | 2025-06-19 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 57cd92fd-693f-386c-b2dd-07b87d012dad | -10.6489 | -49.4483 | 2025-06-19 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2c6c96c5-f364-3ca0-89d6-caa0dd73f892 | -16.3047 | -58.2676 | 2025-06-19 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 44ac7bba-5dac-33bf-bcea-0ea6b02c8736 | -8.1267 | -43.1154 | 2025-06-19 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| b8e9de98-e351-37f1-b7ae-8a729dba7b6b | -11.9518 | -58.7574 | 2025-06-19 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 9544dfbb-87ff-3340-a9ce-93f75e149ff1 | -11.9709 | -58.7362 | 2025-06-19 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 247fcc45-5ec6-309c-825f-1b2ecdbd82a5 | -13.9924 | -58.1127 | 2025-06-19 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ffa90e4b-0521-3fba-8744-aa6076693ca0 | -11.9329 | -58.7588 | 2025-06-19 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| b7e64ef2-896d-3fc5-87e3-9f24da5c371d | -4.7872 | -47.5676 | 2025-06-19 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8b5ef0ba-3229-35d6-861b-bed3c2eb513c | -14.4467 | -48.9063 | 2025-06-19 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0c884dd0-d943-34c2-abf5-ef741342cc6d | -14.4277 | -48.8871 | 2025-06-19 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 9dd5d25d-eef9-3e0b-969f-f4e05f12ce6e | -8.1264 | -43.139 | 2025-06-19 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 2ebb9d7f-963f-32c4-9248-fa0533d542ed | -7.2408 | -43.0664 | 2025-06-19 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 60a3ee2f-83dc-3f03-86a6-41008cb89c45 | -11.9707 | -58.756 | 2025-06-19 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 137.2 |
| d9de206e-5348-34fe-81d9-78356f441f39 | -10.6486 | -49.47 | 2025-06-19 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ab525921-65ec-35db-9de1-166b708c6cea | -10.0972 | -52.7376 | 2025-06-19 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1edfd71d-9e96-32ef-bcf0-d68276681341 | -14.4471 | -48.8841 | 2025-06-19 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d93f4bc2-84f2-3609-9146-b988a4358541 | -14.4273 | -48.9093 | 2025-06-19 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 73a29652-b0df-3188-a6f7-9a16b7f11b40 | -16.305 | -58.2474 | 2025-06-19 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 8302c2c9-2543-3494-b726-a84329b12da1 | -7.2405 | -43.0899 | 2025-06-19 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 212.7 |
| f0e0ed7e-9ec9-3d24-b3fe-40ad3479887d | -7.2217 | -43.0917 | 2025-06-19 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| af9993df-0fdd-366b-83eb-8d99f484ca02 | -10.6489 | -49.4483 | 2025-06-19 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 214f1d04-1a49-3cb5-817f-6d4ebe7b1e6a | -16.3047 | -58.2676 | 2025-06-19 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 537e835b-1c05-3e54-b2d1-e52bd70af7c9 | -4.7686 | -47.5686 | 2025-06-19 00:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 74813907-428f-3d7e-9c2e-49c234d5c716 | -8.1267 | -43.1154 | 2025-06-19 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 11b748fc-2755-30f1-9890-18166868be98 | -11.952 | -58.7376 | 2025-06-19 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 67cd69cc-f66f-3c5b-a88f-a5a52b1733f6 | -11.9518 | -58.7574 | 2025-06-19 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 317d8151-7c9b-3744-a5c1-3a6bee855f06 | -7.2219 | -43.0682 | 2025-06-19 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| c65c9e0c-7d88-387c-90da-04e428e7937c | -11.9707 | -58.756 | 2025-06-19 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 3d9c3134-e825-3d6e-a0e1-ce52349bd79e | -10.0972 | -52.7376 | 2025-06-19 00:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8915efef-b132-39d6-929f-b74ef16e9698 | -11.9329 | -58.7588 | 2025-06-19 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bed77e9d-d55c-3753-9f09-4f80ab4eb956 | -7.2405 | -43.0899 | 2025-06-19 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.9 |
| 809c42bf-0c3a-3705-b745-b35c265d01d4 | -16.305 | -58.2474 | 2025-06-19 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 26aa08f0-bdce-3677-83e0-d5a5990785ee | -8.1264 | -43.139 | 2025-06-19 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 4f4a907b-400d-39f3-ab38-dceac8b298a4 | -11.5177 | -56.9862 | 2025-06-19 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7e6d1f71-0ff7-30cd-8c43-2a294f02c9d4 | -7.2408 | -43.0664 | 2025-06-19 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 01507162-801c-3e31-88ae-7dee35298b3e | -11.9709 | -58.7362 | 2025-06-19 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| ba780fb3-d1c8-3f70-99c4-9f7e59c8363c | -7.2217 | -43.0917 | 2025-06-19 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 85d37db7-33ad-31b5-b714-0dbd45b585ac | -12.2727 | -44.5967 | 2025-06-19 00:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 71d2a393-a2ee-3bb9-944c-3570aa90eaff | -4.7686 | -47.5686 | 2025-06-19 00:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 164980b8-33e6-3091-b1ec-7da959934508 | -10.6489 | -49.4483 | 2025-06-19 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2c72687d-a298-3fcf-b8b7-8144b8ebe5df | -8.1267 | -43.1154 | 2025-06-19 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 14a743cf-328f-340b-96d0-5cf3fb99fa70 | -11.9329 | -58.7588 | 2025-06-19 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2986d2b0-a860-3ce8-a6ef-70cb03e4f0eb | -16.3047 | -58.2676 | 2025-06-19 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| bc6235a8-6143-3b5f-a605-9a57e33c339a | -16.305 | -58.2474 | 2025-06-19 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 0355cfec-3812-3eb1-bf70-b58273fd81ef | -11.9518 | -58.7574 | 2025-06-19 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 314.4 |
| e57f6465-f781-336f-bf0f-fc3a791849f0 | -11.9707 | -58.756 | 2025-06-19 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2c06ad10-787f-3fb0-802c-fa2f3de5cbef | -11.952 | -58.7376 | 2025-06-19 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 347c21aa-a021-3fa0-9709-5c074d080b42 | -7.2405 | -43.0899 | 2025-06-19 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 233.9 |
| 9bfda27f-46f7-3c8f-9804-8e2fc9bad595 | -8.1264 | -43.139 | 2025-06-19 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| a414ed0e-a2e3-37f1-8d6e-8f75ab0c59a5 | -4.7872 | -47.5676 | 2025-06-19 00:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 673bf870-e7db-36c6-bd27-9a1a8d7b684c | -10.0972 | -52.7376 | 2025-06-19 00:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9bd7dd30-07d5-3e80-9303-556819bbff02 | -11.9709 | -58.7362 | 2025-06-19 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 1cb0ad01-4530-3b68-b208-c40afadd8ca7 | -7.2217 | -43.0917 | 2025-06-19 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 8909d518-7fef-38e6-aebd-7a06411abb24 | -7.2408 | -43.0664 | 2025-06-19 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 93546528-09cd-32c9-9d6e-deeb5aea46e2 | -20.016899 | -45.733898 | 2025-06-19 00:47:00 | METOP-B | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c7f4e3ee-0c0b-3a5c-8a3b-11281aedfba7 | -10.0968 | -52.7285 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
