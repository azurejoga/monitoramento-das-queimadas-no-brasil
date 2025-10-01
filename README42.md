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
| a87a241f-84fe-31a7-bc12-c9bfacece2f8 | -6.44754 | -44.45448 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dca9ba1-e6e0-3390-a7d7-fd0768a30ba9 | -7.55161 | -46.28072 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3e75adf-5485-3f34-b896-f3cb2fb12f35 | -5.88935 | -45.88101 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24a2544f-5709-3227-b778-17abac214707 | -8.22157 | -45.79295 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6141ba01-47ab-323b-83f3-53af560e6bb5 | -9.01324 | -46.72112 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d437411c-e780-3bb2-b187-3a977de429c7 | -6.91908 | -46.2123 | 2025-10-01 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67c95049-1f57-37e8-8c6f-162d808cd1fc | -6.06781 | -42.67977 | 2025-10-01 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b97f9272-c0d9-38da-8ed8-8dc1959d4fd8 | -7.02496 | -44.46003 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6869768c-6f98-3f7a-b97f-885e091e0c9d | -5.85563 | -43.40075 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 767cd6d1-4f2c-3686-8168-b41e51f9c720 | -5.47776 | -43.0726 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c4acd3b-c6a0-3aa1-8999-7d2cd89bbd44 | -5.83224 | -43.92487 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2c31a62-3383-39a4-a81f-4615a956b21a | -5.76891 | -42.86512 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4908d253-b7b6-3dbf-a9c7-23548f5dc095 | -5.85898 | -43.40126 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| dbf56f5b-859f-3985-a388-5611f787252b | -7.09547 | -45.55146 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea8cf8ca-7cab-38ef-a2ce-cdf0842e3b73 | -5.64041 | -43.91294 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 993be7a9-7b0c-3ef6-bde7-e3fa937a2b94 | -3.75611 | -41.03859 | 2025-10-01 04:19:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa21ee5c-b443-35f1-b847-e036891e8311 | -7.84379 | -50.24313 | 2025-10-01 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e4c9764-b072-356b-8534-03029bcf03ec | -7.06618 | -46.84827 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cc0fa0-9ef2-32e9-9ce7-9ce0d7390595 | -7.82299 | -50.24323 | 2025-10-01 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 165d2fe8-be27-3710-b0e1-cdd830d32470 | -8.72339 | -47.98423 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d989e85e-9ad2-3cbe-ac6c-3c92c1700fb8 | -8.92355 | -49.83727 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 477b7f52-0a27-3959-8b67-1077c2c15620 | -7.02281 | -44.47383 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b2920c8-d848-370c-9055-647bfd772514 | -9.93154 | -43.6604 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b232f61d-bcb3-3e41-963e-0189a2ca5618 | -5.73437 | -42.81872 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f030b56-c2d2-312f-ac03-7980dea745e3 | -3.42088 | -51.23306 | 2025-10-01 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38df94b8-5f5f-327b-9273-0e9c80fde413 | -8.58476 | -44.7349 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 583d2f1e-026c-32db-8e07-cc239be0d350 | -4.80511 | -45.33354 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f8bd212-67d2-3714-84c4-0c631357a9ef | -6.28462 | -43.66304 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a437585d-aca7-382d-8f74-00317bcb44f6 | -5.63988 | -43.91643 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 0ad829c6-c4a9-3098-a4e4-78049f8f372c | -6.57254 | -43.44593 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85bd7bd5-cd68-34fc-ad11-b25bd551b4c9 | -8.5385 | -44.70271 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 779f810c-3265-30c4-b789-aabb41a8535b | -7.11225 | -45.0789 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab9a8d58-6eb3-324d-9c14-d17cbf95a7f4 | -8.75114 | -45.93145 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac919c8-5f23-333b-a3de-188650f814af | -8.73626 | -45.91834 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ba21886-efea-3500-af0a-6707374bb247 | -6.24022 | -43.06639 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d8b71a4-b6ef-3a77-9a85-9b9c8048c799 | -9.47931 | -45.49968 | 2025-10-01 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 13f7c4dd-9174-3d03-83b8-e63b3d0c3ab3 | -5.6455 | -43.9457 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c65e240c-e337-3545-b0c4-31182feab34e | -8.75445 | -45.93198 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73f487d2-aad3-36f2-b9a5-a080ca0d8153 | -4.04094 | -54.13764 | 2025-10-01 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5967cac1-5c50-3e80-b6dc-d0a83b69ecfe | -5.61577 | -43.23328 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 197c75e4-2103-31ad-b051-b48dfe579c39 | -7.09266 | -49.16607 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31fde355-c9f9-3227-a879-e8ac06bc9f51 | -5.9129 | -43.90961 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c97f6f1-66a9-3864-901d-38a1814dcafb | -4.81436 | -43.27275 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40b5badd-4b76-39ea-a123-3bb37b767cb2 | -8.23129 | -45.5167 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 426073d3-b044-3c06-8a22-3577f73aa4cc | -6.53473 | -45.2237 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7892742c-3ebc-325b-ad85-f6cc1b48d6fa | -5.82677 | -43.93822 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8092d9-8f95-314d-85dd-d860fba4d2b1 | -5.90744 | -45.03546 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70a69e46-64b4-3da7-93b0-fbf5defe6df3 | -7.47561 | -47.2762 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0793963a-2261-3df4-acb5-69083114f093 | -2.61533 | -50.91868 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 513af2ba-9b91-323b-88ef-0518f71a9e0f | -5.42212 | -43.18873 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17515364-61b8-3736-a0db-32e710431ab5 | -8.90606 | -47.62051 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f65dfbf6-cd76-3684-8901-d8ea73664bf2 | -5.99788 | -44.56642 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c6aeaae-2f94-3870-8ee5-934549da18de | -9.77402 | -46.22227 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5acc8f8d-2fe9-38a9-90ae-edc0612e349e | -6.33066 | -43.02824 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9accde80-1694-32ef-8bce-4902335d9659 | -4.22708 | -40.80336 | 2025-10-01 04:19:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38da7173-cc74-3bd4-9aed-26f6dc79166a | -9.8067 | -45.93008 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7561702e-9b39-356c-b2ef-d0479e290083 | -7.20915 | -39.96567 | 2025-10-01 04:19:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60a70d0d-e67a-3e88-bbe1-4e41b6446d8c | -7.46912 | -46.45884 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 474e6e53-f89a-34d8-8885-950996598cc2 | -9.4485 | -45.48057 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af31d75b-4de6-3462-93b8-55f9b8b246e1 | -8.38432 | -48.65096 | 2025-10-01 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9373ddf1-bfd7-3ff6-aa23-5966f07006b3 | -3.45869 | -50.09337 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9720c74b-b7d1-363c-8239-9f2aa22c9208 | -7.05655 | -46.42177 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde4f243-e4fb-3a8a-b946-380d5d03986e | -8.55101 | -44.64402 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0231f366-845c-3962-8489-2c9a394c6cf7 | -9.47829 | -45.54928 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6735817-80f0-398d-a84f-3bca5d41763f | -5.76721 | -42.92087 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a6c1f7d0-fc14-3d76-b0b4-b500fb2b2f5d | -5.27656 | -43.16611 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79bf94ad-3a21-3267-8bde-9f8e20897e98 | -5.76947 | -42.86148 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b193a14d-bea1-35e6-bdc7-013708ead06a | -7.05031 | -43.27853 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7f23b00-4c6c-3e8a-88a2-d8d07eaf3dfa | -6.1106 | -42.65192 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e8eea2dd-cb37-397d-85b6-c19b22f1568b | -6.47801 | -44.21498 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb34b7cf-6888-3085-9026-81684e651352 | -6.05855 | -42.44369 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| fad3761f-c4c4-31e6-a566-e606794a9422 | -5.82653 | -42.85872 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4df1ca87-989c-3d07-be2a-e34733b0c20b | -6.71259 | -44.56295 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a531ef9e-3f03-3fd7-89f6-4147d00df0c6 | -7.87119 | -43.89343 | 2025-10-01 04:19:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a8339be-8f9b-3152-896f-c2a9bf75270a | -5.4127 | -41.33475 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 66d091dc-2245-31fb-9307-f16f9adce164 | -6.10892 | -43.45822 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 162b4367-bd60-347a-b92a-fc9a37a44d6d | -8.74726 | -44.23251 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77afd2a9-5200-3e45-befd-aff6e4b109b2 | -9.31506 | -45.72269 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02b2e851-6ba1-3fea-bbdc-b28cb4a53b2c | -5.95366 | -43.31437 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 422878d5-67ba-3772-9db8-aa1903a3230a | -7.72195 | -44.9426 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7095b996-94cf-3fa7-8b85-c9dd4c58fc88 | -4.40092 | -50.84285 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52b79961-7598-318a-9ea4-58010b45671e | -5.62697 | -42.83198 | 2025-10-01 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| be66e6e2-ccea-3dc1-87b0-dc10e01af9ba | -5.88774 | -43.67685 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbc9ec89-0489-3062-b3f3-f28b4084ae85 | -6.10487 | -43.12754 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 156d6372-ac95-3cae-8ffd-6aa78a8212e4 | -6.10824 | -43.12808 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4fc65d54-8104-3406-9b5e-5424c987b628 | -5.8293 | -42.81783 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3d847c5c-fac2-33b5-9e44-2d31baa7ba2c | -8.901 | -45.04116 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee3d9949-34bd-3793-b20c-923236db08d2 | -5.83583 | -43.94743 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 954c24bf-e233-398f-af46-5cbd0a3cd8a4 | -5.63773 | -43.93032 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 527c223d-72b2-313f-adf4-fdbd76532b06 | -5.89779 | -43.30522 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ce03efa-dd85-3979-9532-8aaac2549b05 | -5.64315 | -41.24687 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 958fb03a-15e6-3a2d-bb07-5310e7f5c6ff | -5.47048 | -43.07516 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ac8e7f1-6315-3cff-a052-1b441c6e813d | -2.88996 | -47.84401 | 2025-10-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8f6774f-f61a-3bde-b4c2-dcda9bac2f13 | -7.09106 | -49.17564 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27a7fdd1-da73-35f9-9242-5d3b92507345 | -6.41137 | -44.64291 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72d5ece3-58c9-3cc3-9c9b-bec3639619be | -5.82015 | -43.93719 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59b7e4d3-8d97-334e-8945-d00a7bb79f17 | -5.95124 | -45.85792 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11e6258d-8a86-357a-b624-3a28223add9b | -7.16594 | -41.70765 | 2025-10-01 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cf5f54b3-a9fb-3347-a2c6-c67ea0e40970 | -8.3363 | -50.86306 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70079ab5-eee8-3c7b-b8dc-afbb421dea08 | -5.9401 | -45.86343 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
