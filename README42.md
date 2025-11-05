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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a6c5173-9840-3789-9a4d-7f45f5e1a07a | -5.9222 | -43.3703 | 2025-11-05 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 915ad7e4-ad35-3381-83fd-aa325e52900e | -6.701 | -40.8206 | 2025-11-05 14:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 211ddf87-7225-3a57-935a-fcbf8ff5fadf | -4.5934 | -43.3239 | 2025-11-05 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 69bed70a-dd2d-3eac-bc3d-13ed859d67cc | -8.5209 | -44.7455 | 2025-11-05 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c73921c9-6458-37a4-90fc-5f48f0a9b697 | -5.5112 | -41.1464 | 2025-11-05 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 9b91be51-9b50-3027-9bad-fe51a02498bb | -4.5143 | -38.9509 | 2025-11-05 14:00:00 | GOES-19 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 135.9 |
| 8f309c41-78fe-3a08-a5c5-cc2b0d741880 | -4.7815 | -43.1721 | 2025-11-05 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 77a8e3e8-2beb-360f-a356-dcb666d5412a | -6.108 | -41.651 | 2025-11-05 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| d437a114-873e-3b43-bf27-265d6f5e23f7 | -6.1083 | -41.627 | 2025-11-05 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 41ea9bcd-0c86-3373-9f89-a7bab0db1506 | -1.2084 | -49.1476 | 2025-11-05 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a1011069-60df-3c78-b0b3-970c1ab2076c | -7.3134 | -44.9572 | 2025-11-05 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d54409f3-583c-30f4-b725-3f6a10659eb9 | -6.0735 | -43.2414 | 2025-11-05 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 108.2 |
| f5af1ea8-2736-3209-a997-ad281be366dc | -3.29 | -42.6448 | 2025-11-05 14:00:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c54ae7e5-2edd-3702-add0-6984588d4a87 | -3.5833 | -43.6108 | 2025-11-05 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e3a27f02-8041-3c1a-a915-4b09a8746a71 | -4.3872 | -43.406 | 2025-11-05 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 4462d66d-8c3a-31c8-980d-eb8497a8df71 | -3.3319 | -53.8385 | 2025-11-05 14:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c499539e-f9c4-372c-9815-9dc05466843a | -5.9236 | -41.2814 | 2025-11-05 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| b8640faf-8f39-3bf9-acdd-b7dce3ea3ce9 | -9.9578 | -44.8537 | 2025-11-05 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ce21f247-e660-35a0-8336-426c6c55a2d8 | -6.0461 | -44.1484 | 2025-11-05 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 8f89bf46-fe32-3516-b90e-2a9e8b4f334c | -3.1763 | -42.978 | 2025-11-05 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9cbf12ab-6358-3081-ba4f-11384c894872 | -5.9234 | -41.3056 | 2025-11-05 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 131daf13-6dba-35b6-a866-7b787b7f9e48 | -19.0323 | -57.5174 | 2025-11-05 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 126.0 |
| db0ff738-6cc6-3a6a-962f-b77860138f70 | -6.1271 | -41.6253 | 2025-11-05 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| eb5ab456-6703-3296-b2f4-f07d992b6f93 | -7.0695 | -44.9335 | 2025-11-05 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e2497bfb-8f6f-322c-85b0-d0bfbee5b2f0 | -3.2299 | -43.4414 | 2025-11-05 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| bf47eb02-d731-3b78-8c4d-56d9b29b2c36 | -4.0949 | -42.4152 | 2025-11-05 14:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 0cb9e548-d87a-35dc-b5ab-929cd5640ac5 | -3.9219 | -43.1525 | 2025-11-05 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ff59b682-80ba-38af-9c8e-b851fbb6aad8 | -7.1784 | -41.9576 | 2025-11-05 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 928199dc-fe2f-3e24-ae1f-ffcd3fa82719 | -3.8856 | -42.9909 | 2025-11-05 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| eff57749-b728-38a2-a760-70801cda5f02 | -3.3135 | -53.839 | 2025-11-05 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 5ff02468-1d14-351e-87ce-579f0e3728a5 | -6.0735 | -43.2414 | 2025-11-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 163.3 |
| 0f524129-dcc8-3f6a-8d45-937b1954713c | -3.9469 | -42.1631 | 2025-11-05 14:10:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 937a874d-43d4-3428-b400-58d65b6d8a4c | -10.1136 | -44.6033 | 2025-11-05 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 51b01ce9-0f99-3c5f-b76c-29db47889137 | -6.1459 | -41.6237 | 2025-11-05 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 03e05ea1-8831-3fd4-a4f0-580223677f34 | -6.1836 | -41.6203 | 2025-11-05 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 8bdd08b8-7a38-3b08-8bdf-8775053338b7 | -5.9234 | -41.3056 | 2025-11-05 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 149.2 |
| 2afa3fb3-5df6-3a4b-9eac-80ace1195946 | -3.29 | -42.6448 | 2025-11-05 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ead9a0d2-6310-3a8a-b762-039eb944df79 | -9.8821 | -44.8402 | 2025-11-05 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 09cd4b4c-b9e2-312e-84ad-c9caf87cc892 | -3.6603 | -43.1891 | 2025-11-05 14:10:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ad764466-b36b-3575-b9e4-b1d494d6cdf0 | -3.5833 | -43.6108 | 2025-11-05 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6942912a-9517-3c41-88d6-ba391ca2bf55 | -5.9229 | -41.354 | 2025-11-05 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| 20800dbe-2fcd-3b79-862f-e90e4cf15aa1 | -4.3872 | -43.406 | 2025-11-05 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a92cfbf8-bb16-3918-af2d-c1485468d67e | -6.1834 | -41.6444 | 2025-11-05 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| c1c4a11c-2ed3-3ba0-97fe-168e56a2b2a7 | -7.0693 | -44.9563 | 2025-11-05 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9cc6aec8-9166-35c9-b22f-05558bcabff3 | -4.7815 | -43.1721 | 2025-11-05 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 722cb321-4c53-308a-98c7-aab674301789 | -5.9222 | -43.3703 | 2025-11-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 68.3 |
| e4dba920-130a-3b43-bc4f-204c92cc2ba9 | -1.2085 | -49.1264 | 2025-11-05 14:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ad573a8d-5271-3b91-9bfe-ff5e7831d37c | -6.0733 | -43.2648 | 2025-11-05 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 167.1 |
| eb3184c7-1ad5-3c58-9f56-64009af1842f | -5.5112 | -41.1464 | 2025-11-05 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 03aec407-5887-35a8-8ec5-82793d26f216 | -3.1763 | -42.978 | 2025-11-05 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 29e2b36b-6847-3a2c-957b-cbe9016c0c31 | -6.701 | -40.8206 | 2025-11-05 14:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 39022820-1e38-3750-90a6-d838128d5b7b | -7.1079 | -44.8617 | 2025-11-05 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 18600892-e307-3424-bd98-489294fd73a8 | -9.9198 | -44.8585 | 2025-11-05 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2600b072-c211-38d3-b143-92d9947e6ea5 | -5.9227 | -41.3781 | 2025-11-05 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| b1dc0185-4235-381c-8ed3-3a750d616300 | -7.0695 | -44.9335 | 2025-11-05 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 65173826-90c1-3c77-9f81-731690c83de6 | -19.0323 | -57.5174 | 2025-11-05 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| 79c98610-80cb-3144-bdf7-4b7220a87eae | -5.941 | -43.3688 | 2025-11-05 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 64.1 |
| cffb4a6d-495d-3161-9595-6be7669457eb | -7.0698 | -44.9107 | 2025-11-05 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e7eb57f6-0be6-35e4-8998-9f39e72bb224 | -10.285 | -44.581 | 2025-11-05 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1b8fcc7d-0186-3da9-9723-15fd9b02cc52 | -6.1271 | -41.6253 | 2025-11-05 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| c8118e61-14de-35de-b554-91441d69a5cf | -5.9222 | -43.3703 | 2025-11-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 66.4 |
| b49e502f-23e5-3e51-86e8-262fbcb2ed02 | -5.1744 | -40.9788 | 2025-11-05 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 133.2 |
| 18574400-86de-3632-86ac-70766e399737 | -7.1291 | -41.3365 | 2025-11-05 14:20:00 | GOES-19 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| bd2e5be5-b879-3640-b81b-43346ed38599 | -3.7359 | -43.0453 | 2025-11-05 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5b4e6d46-6956-3131-8dc6-3c3a9f433b30 | -6.1469 | -41.5273 | 2025-11-05 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 559b7cba-cb2f-3b2a-90cc-6de42851ddb8 | -5.4155 | -43.4552 | 2025-11-05 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ca7aabb3-5208-3096-8743-76d7b1167df9 | -3.1763 | -42.978 | 2025-11-05 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3395879d-358e-3efc-92ab-571e3354891c | -6.0461 | -44.1484 | 2025-11-05 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 5187519b-41cd-30df-ad24-8e1879855816 | -6.1459 | -41.6237 | 2025-11-05 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 693679e5-ac16-3696-9e0c-2ddeafb94e04 | -6.701 | -40.8206 | 2025-11-05 14:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| a737045b-ea30-3eb6-8b80-5f6789166bc3 | -4.0949 | -42.4152 | 2025-11-05 14:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| b9f5fe0e-4f96-3956-b94f-6332f691f1b8 | -12.7764 | -43.4547 | 2025-11-05 14:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9a816630-827b-37e1-8526-400c6a48cb6a | -3.5833 | -43.6108 | 2025-11-05 14:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4b451ddc-f10a-3459-aa4e-6f230d6da6b3 | -6.1836 | -41.6203 | 2025-11-05 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 432fca15-37c1-3feb-b284-2a6b3a89a3c0 | -3.9219 | -43.1525 | 2025-11-05 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 352fbe2d-0e1d-3e80-85e1-5f31493f73b7 | -5.9229 | -41.354 | 2025-11-05 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| cb6784e7-f524-352f-b46c-6781207cd3ce | -12.8534 | -43.4653 | 2025-11-05 14:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 62b064cc-b44f-3fe1-bc93-4856f4ff42e9 | -3.2299 | -43.4414 | 2025-11-05 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 53b32d0f-bf97-3f7b-9eba-b017a61bbe46 | -3.6603 | -43.1891 | 2025-11-05 14:20:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 21d0c7cb-2c9c-3393-ae4c-978bc73e4042 | -12.8539 | -43.4414 | 2025-11-05 14:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 010aa1d7-4bb0-310f-bb33-4fabc2f58b46 | -19.0519 | -57.5356 | 2025-11-05 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 132.4 |
| 13f9f115-10b9-3ab9-813f-ddd331b7fc28 | -5.9234 | -41.3056 | 2025-11-05 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 155.4 |
| 3c390930-61c2-3afa-9b5a-e47b9391dee8 | -6.5415 | -45.2282 | 2025-11-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 655bfb0e-c2f3-3397-97c8-d1e0ecbea9bf | -19.0323 | -57.5174 | 2025-11-05 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 140.0 |
| c36c0a99-0993-3473-a008-a619f27a02f9 | -5.941 | -43.3688 | 2025-11-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 4245f042-125e-3755-a833-83ecbfb2f529 | -5.5112 | -41.1464 | 2025-11-05 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| a6b2363b-31f2-33cf-a0ef-1319a0dda764 | -10.1136 | -44.6033 | 2025-11-05 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 107bf51f-6aa2-3450-807e-309e5c444eea | -6.1281 | -41.529 | 2025-11-05 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 8ece78cb-408b-3dd5-8584-4e390e7a4aca | -6.4632 | -41.883 | 2025-11-05 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| f95e2f72-2e65-3727-a117-6130983582c6 | -3.29 | -42.6448 | 2025-11-05 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e4fdf145-0fc2-39cd-905b-8fe1ebf6f0fb | -4.3872 | -43.406 | 2025-11-05 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 02a883f6-d6cf-3b81-a30d-e8cb740befa7 | -5.9231 | -41.3298 | 2025-11-05 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 3329d2bd-1860-322b-a509-499ed1abb083 | -3.1952 | -42.9305 | 2025-11-05 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8bff44cc-7f03-31d0-bcfc-0f063a72bf00 | -19.0323 | -57.5174 | 2025-11-05 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 145.9 |
| 7771ec73-f634-32b5-bb0f-44d4475a20f8 | -5.9234 | -41.3056 | 2025-11-05 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 3e5d9cd1-7a56-31b1-9c1f-c095592ed55e | -3.8856 | -42.9909 | 2025-11-05 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 33878063-a818-3c19-83ee-6ca64c0083b4 | -5.9222 | -43.3703 | 2025-11-05 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 69.9 |
| d0d7ff00-a298-34be-8d26-d49ec08c0a40 | -3.0078 | -43.1018 | 2025-11-05 14:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 880c6e16-1ab0-3eb3-8608-28b426a0a518 | -1.2453 | -49.1472 | 2025-11-05 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c8eaba82-84f8-32ed-91c6-0039503103e7 | -9.9014 | -44.8147 | 2025-11-05 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |


[Clique aqui para ver as próximas entradas](README43.md)
