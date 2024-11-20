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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2365ce86-ca3e-36aa-95fc-c427bc09a86f | -1.0513 | -51.741798 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b008c74e-07a6-34b2-ab60-ad1a81b32165 | -2.188 | -53.6698 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673f93be-dfba-313d-9bfe-88abcd4afdf9 | -1.1989 | -51.756599 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbfd1b9-f1db-3944-8616-fe7082d04cf9 | -2.5605 | -54.076599 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8b1618-7cb5-3e8c-b1e0-96529be64c9e | -1.0534 | -51.750999 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 08972b3c-800b-3258-8e63-4ca5e98473d8 | -1.243 | -53.373699 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a929a6a9-8f93-3885-be7d-aa3ab469b93b | -1.5348 | -52.272301 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 039f5600-a707-30d6-8d26-6ff778dd88f3 | -1.0947 | -51.751301 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 49874aff-0f8f-3c19-9c3c-5246d7c55539 | -0.896 | -51.738098 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 74fa09a5-65ca-33c8-bcf2-e0c230903547 | -1.4647 | -51.970001 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9524ff4b-6ddc-3915-9a0a-71d1b72b0aae | -1.3095 | -52.4119 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94fe20d2-54f1-39ad-b497-7ffe5dc2243e | -1.0443 | -53.093498 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf72043e-42ad-3fdf-a073-d96eeb3e4bf4 | -2.05 | -53.429501 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b0a1905-84ce-30a9-a48c-c65f28d60201 | -2.6173 | -54.278099 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7afd28-3cb4-3d0d-b2ea-18cbd6c45c91 | -1.4429 | -52.676701 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1b18dd-4722-3444-8ecb-73ffba885ffc | -1.0394 | -51.734798 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9516b7-f9d7-37b7-b8f0-f79635fc47f6 | -1.1891 | -51.758801 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f02e1a-a5f2-3941-ab4e-5671f2535604 | -0.3001 | -51.565399 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 02f260ac-cac2-376e-af6d-bc37773e407b | -0.933 | -51.7201 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5c692a92-f0b5-3986-9ba4-cdb322aab1bd | -1.1934 | -51.777 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dbebeac-738a-33b1-9cfb-c6a052f0663e | -1.0415 | -51.743999 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 440cba38-f4bc-3691-95d5-3ea627080e35 | -1.2074 | -51.792999 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f28fa567-e367-3d6f-8188-0e311409f83c | -0.9577 | -51.7822 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3ec4fd-9c6f-3e6a-b7ea-f483e3b74dfd | -1.1893 | -53.6777 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b007e2ee-ee0a-3af3-a48c-c2317167bcf4 | -1.8556 | -56.3983 | 2024-11-20 01:04:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56191ecc-e3a1-34fb-aa59-492adc3f3698 | -1.7144 | -52.692001 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 423bc930-1ea4-3b5d-8e94-46dc9f660e85 | -1.1416 | -53.515701 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c52602a4-4216-33bd-baec-82d8fd9b19eb | -1.8815 | -50.971001 | 2024-11-20 01:04:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40d28eee-514e-39e6-9bad-678acebfbd59 | -1.6384 | -52.675201 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d510fd20-9429-374c-904e-74cf10a0d924 | -1.5328 | -52.263802 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8e6066-32ef-3f73-b08e-033750adb516 | -0.8947 | -51.7771 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 25382061-cf08-3e63-966d-def708bc32e4 | -0.9568 | -51.7341 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8271c4e0-452a-3031-b563-8f86eb015e8e | -2.3302 | -54.779598 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8d40d7-f689-38cc-806c-1cd28c1b1eb1 | -2.549 | -54.071701 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89674c92-ac0b-33cb-a946-fd071309a526 | -1.2412 | -53.3661 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f32d5a0-ffd5-3742-b0d7-c698401449e9 | -1.0926 | -51.7421 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 786e7e7a-015f-31b1-bb8a-38e76d31f3f9 | 0.377 | -53.8162 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a3182f-9c5c-3e35-9611-f13f96ff5f4f | -1.6286 | -52.677399 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aedfaaa0-c670-3ce6-a2e2-1128cd8129cd | -2.3334 | -54.793301 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d84dbb7-d5c5-35ba-a71e-057eca38826d | -1.5973 | -52.408401 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794af16b-6da5-37b1-b0e6-1db2db4d234d | -1.2957 | -52.263599 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54fe0bfc-ba79-37a0-a656-b525cb4e49c1 | -1.2053 | -51.783901 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dada28-ab94-32bc-ac19-15f30674c2a9 | -1.2011 | -51.765701 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3b4c7a7-8eab-34ed-ba17-641cc7847abe | -1.1288 | -51.6759 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41742d4e-e8fd-3fcf-9a68-e0d56d337d0b | -2.1777 | -55.058498 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c53808e-c044-38a8-a879-2895b05b2053 | -0.0956 | -51.4375 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cc24fe52-a0a2-37f7-8009-ad988e0cbf28 | -1.2164 | -51.743 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd778b6-2634-3a90-a6eb-ebfc17be7539 | -1.2066 | -51.745201 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7c91ae-7cac-3eff-83e4-2c48bc969f51 | -1.1331 | -51.694302 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71206c44-abf6-3e14-8d97-c51130bec652 | -1.2521 | -51.763699 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f97d3b4-b5e6-3b69-afc8-cb617e3cf9d2 | -1.6967 | -52.4818 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acf1f4b6-80b8-3279-8bd9-fd44c7a0e387 | -1.8694 | -50.963299 | 2024-11-20 01:04:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce03fc10-6478-3644-8a0e-f5872b4b5371 | -1.251 | -53.363899 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5058ae8-9fa5-3819-96be-a5f5f67dffde | -1.2283 | -51.749901 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95166ae6-1f97-36ea-83b1-dc7b7b7fa22e | 1.5499 | -55.897999 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9a4721c-9f9d-3b81-8d27-0ff9e9ed83b0 | -2.0483 | -53.4221 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 761ccec5-aa8d-3736-afe2-2a63a03e8235 | -2.585 | -54.004002 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71a567c6-be5e-312d-90a4-2ae900d80f21 | -1.2172 | -51.790699 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab93a07-f381-32a7-89e8-c03bdafc6d6f | -1.6268 | -52.6693 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eebec78b-83d9-3ca3-b15c-b608215bf78e | -2.4402 | -53.689499 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23347fc7-d11b-3f70-8cc4-716be6923b32 | -2.6157 | -54.271198 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e90f09-b8ae-37ce-b946-ed492e375398 | -1.1955 | -51.786098 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175d6ce1-b56b-3818-a120-808ab263a1bb | -2.5261 | -54.554501 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9e116c-241e-31bc-a899-b4a91f15a3d5 | -0.2694 | -51.388 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| baa08191-9088-32c0-af60-82dc54929afb | -1.441 | -52.668598 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f789c392-415e-3f0d-994b-95cc685f8194 | -2.5523 | -53.996498 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee821fc-d488-3f0b-bbaa-d4eaa272838c | -1.6305 | -52.685501 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8128f016-c54a-39de-a54d-3c00119e61cb | -0.1818 | -51.632401 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 87d202bd-b305-3610-9cd4-8fe0b89bafff | -0.1795 | -51.622799 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bcac79bc-8b74-3ca8-a5a1-6d45afb68e4f | -2.5866 | -54.011101 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed7b6c7-caba-3aa4-9541-ea24b23f0edb | -1.4312 | -52.670799 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d11b45c-4fcf-3604-a04d-18f2c92e7a58 | -1.1301 | -53.510399 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b78951-a962-36f2-a148-d232991dfdf4 | -2.2615 | -53.630199 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31559c15-bbfa-37ec-96ae-0fd822303f7a | -1.3212 | -52.239799 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818a86de-75ed-32b3-844a-203436befc16 | -0.9428 | -51.717899 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 408f6fe7-6932-3672-904a-5ed8f93a2231 | -0.9351 | -51.729301 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 175305f8-5fe7-3fd7-86e6-d2e5a61ec0e3 | -2.5507 | -53.989399 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3a4cb3b-728c-3672-adac-af6fed241e0f | -2.0517 | -53.437 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7dbaf3-4378-32e5-a275-3307ad48734a | -2.614 | -54.264198 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef76836-25f4-3ec2-b5a4-ac1b86d58a16 | -1.6272 | -52.626598 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6907e7d9-2e91-3ded-81d1-c62f09a50b55 | -0.9547 | -51.724899 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 851c1951-d5ff-341f-bdd2-b2ff0d4ab47b | -1.3075 | -52.4035 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4eaa93-4376-3cca-9383-b4c286a041e9 | 1.5483 | -55.9048 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb6948b1-6e96-33c6-a683-82aeb8cffa8e | -2.549 | -53.982201 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0370ea68-1445-368c-94fe-1f476fcd9096 | -0.9158 | -51.645802 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e37db12-c882-3982-9a18-71dab584f64d | -1.6986 | -52.490002 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bfa8e1d-3d5b-3d86-a2fe-71639ea29211 | -1.6366 | -52.667099 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d538dd82-b045-3a19-9132-bdb48bd57f97 | -1.2151 | -51.781601 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6bdd91-6339-398f-8364-b551399d7873 | -2.5245 | -54.010101 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeea813e-210f-367c-8ff1-72a8b1bb5449 | 1.537 | -55.9095 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d52cca8-4257-36e5-85d0-fc71eab1a52e | -1.1876 | -53.6703 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c01a4fc-6cbc-3723-9c47-c1fad374fd1b | -1.2517 | -53.411598 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e5b198-d7e5-3d95-85e5-05b18e6e7470 | -0.8939 | -51.728901 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e8eb701f-f7dd-3b10-8aff-7e3fe4230a03 | -1.8792 | -50.961102 | 2024-11-20 01:04:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfab07b1-a122-35b0-96c4-f62338810a37 | -1.5029 | -52.090099 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1175492f-bd5f-3bd7-92aa-c9988555d44f | -2.5409 | -53.9916 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fec7d43-21cd-368a-95b5-0ddaccb4517a | -2.2421 | -53.680599 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1fa1d82-3f13-3c18-86b6-39a6d2649e1e | -0.8968 | -51.786301 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e72251fc-9792-3470-b297-4ada765ced2d | -1.3193 | -52.409599 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6feec97e-78cb-32f4-945d-3799995aa5e5 | -0.2943 | -51.495602 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
