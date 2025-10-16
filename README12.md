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
| 713f4b31-15c7-3b12-9ec1-af0093c5e876 | -4.38738 | -43.40738 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e5584b6-f8e7-3729-a332-68ed5a8d13c3 | -5.38808 | -42.79628 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6ef5371-9e22-3467-bf39-747a167eaf73 | -5.86949 | -43.84634 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb09498e-e743-3bb4-ab6e-07e8df300ffd | -4.37821 | -43.37835 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc69d6c1-ba4d-3c4b-9850-57661d7c2b6a | -7.15869 | -42.51422 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb1264a5-6ff4-33b8-ba2b-328863c728b6 | -5.24983 | -41.02467 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c727f39f-f249-394a-ace7-e698eecd51d3 | -6.37377 | -41.49148 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 989ee71f-0907-3f46-88c9-4e40420cf251 | -7.46938 | -41.5172 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 623a547e-2613-38c6-9556-95d83ddc30ce | -6.15706 | -40.90326 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4a4e669a-dfd7-3b05-913a-c47796ae293f | -6.16216 | -40.90841 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| e842cba2-cd9c-31b7-b4de-9f78b9b87d03 | -5.8489 | -42.88804 | 2025-10-16 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 92bf4db6-d4f6-3103-b010-a5be20591626 | -6.04744 | -41.94414 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 05268669-47b6-3aa3-bcd4-e0176afad047 | -6.05542 | -41.93554 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 50c2c86c-e004-36d5-9817-c5b734f75b29 | -6.5691 | -42.96418 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6960e2bc-c547-330d-9a65-272cdbbc0b97 | -7.17076 | -42.18941 | 2025-10-16 03:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b208a574-78fa-3f6d-b958-a4f95dfc9286 | -7.3193 | -39.26498 | 2025-10-16 03:25:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf8b37d0-3451-3a06-94d1-c4ac131e511e | -7.1761 | -42.1953 | 2025-10-16 03:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6123a22-487c-3c64-926c-3a6529add7d6 | -6.0483 | -41.93933 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e155605d-9b91-38e6-97a2-ac5f61cb7d2d | -6.05715 | -41.8903 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87e2d005-b5b7-3854-9b72-4cf9aa0d8872 | -4.65743 | -44.12964 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a353750-46f4-3944-a04b-dea9bdf34a42 | -4.36619 | -43.41882 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 856c91f3-a3b7-3ed6-bdd0-e461bbed329a | -6.14105 | -41.77762 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e8b56f4a-9906-3392-b955-b4ae800737df | -6.13741 | -41.7539 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56ad39c5-ffe2-336f-85a9-bf9c8913fb54 | -5.46931 | -42.93852 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 00d3b9c8-1eb2-3266-bb6a-fa874e5e5025 | -3.43213 | -39.64962 | 2025-10-16 03:25:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 491a67d9-5163-363d-af15-222b6267f8ce | -6.36772 | -41.49052 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 86327b89-d2ca-39aa-a335-aad712c5363e | -5.83561 | -42.34153 | 2025-10-16 03:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51028a49-4775-3ca9-b1b9-46e75ee2da09 | -6.13664 | -41.75812 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cfcb93e1-d028-30c1-bcec-7effeb21ecdd | -6.15559 | -40.91158 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| b1a413e3-f1d2-33fe-83c3-4aadb8f96e31 | -4.65413 | -44.10608 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a684da67-82c1-379f-aaf8-a416d8ab2c9b | -5.42502 | -44.23439 | 2025-10-16 03:25:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55c628b-41b4-3630-aac9-0a674359a681 | -4.3804 | -43.40619 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 334c6d1e-f3a0-3e38-8810-8517bce51657 | -7.39233 | -39.70243 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8ee3c493-b33c-30fa-8e20-97ee89bd5d9a | -6.15486 | -40.91036 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 1546af58-d62c-32b8-b790-030e87289f04 | -6.13128 | -41.76104 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df10c916-3a30-3d73-8b2d-259f4d46d31f | -5.25059 | -41.02037 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30f2e1b3-d4e9-3463-bd71-112307e35de5 | -4.35367 | -43.39484 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 08ac1048-28b9-33b2-8a89-bfead39b33ab | -5.47701 | -42.93398 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32155873-30b4-390d-ac29-65e5af5ab57e | -4.39668 | -43.39557 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fae2bc0e-a537-3bda-95b1-e23bb9b28ae9 | -5.87833 | -43.87647 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f962054d-aa0c-3090-b3e3-d06af3102417 | -5.38529 | -42.79661 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32bb6307-026c-39c8-9710-9df79cebc966 | -5.42368 | -44.24169 | 2025-10-16 03:25:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad782083-01f3-34f1-bd40-3cb25250490b | -4.37301 | -43.37951 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe65611-acb1-3e63-b24c-c5fe04c1de1e | -6.36696 | -41.49482 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 287a5ee5-a8cc-3fa9-a524-de9470b466e7 | -5.83462 | -42.34698 | 2025-10-16 03:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 295c55e5-40ee-35eb-9e9f-41d426266702 | -4.65541 | -44.09883 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f6273b6-93f2-325d-bcf1-5efb2b251533 | -5.47195 | -42.93863 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| dc426af4-368b-350e-8de7-2fc42c0906fb | -4.3676 | -43.39735 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| f2124c43-caac-3321-a769-03986bfa2dda | -6.16225 | -40.90287 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 65dd4f30-6049-3b33-ae7a-fef1263dfd6e | -4.66012 | -44.11438 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f5e9b18c-aa62-3984-a739-4ade665944f5 | -4.38515 | -43.3797 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3af59282-5dc1-389a-a267-899b268db70a | -4.66712 | -44.12265 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a06536a8-4611-3fae-89c0-f543bf0bbe78 | -5.8764 | -43.85938 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a9da430-4354-3b17-bc2e-e67b8daf9aa9 | -7.46259 | -41.52088 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ee2cec10-5954-3c32-be01-41b304a8177f | -4.65285 | -44.11331 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07a1c5ed-d045-31a0-adfa-4014c1b93d8d | -7.165 | -42.5155 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c010ce33-29ac-3f52-944d-410be6914246 | -5.44892 | -41.00426 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4d7310eb-c8fb-3810-89ef-b306dc3f61ef | -5.42857 | -40.9812 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8082f1a5-76a7-3e33-a62e-5d36799701b8 | -6.1366 | -41.76687 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 042bebc8-813d-336c-a63a-28dae9bebee1 | -6.38967 | -41.47737 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8922de0a-e107-34f7-954e-47e6d06b9631 | -4.66395 | -44.09267 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| acba5d9c-4911-39f6-bbe5-1fbc50125afa | -4.38396 | -43.38634 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12dd9eb8-b64f-3826-b442-ee3ce2115900 | -7.16593 | -42.49828 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa8d6106-607e-34e5-90bc-5601f9a7cdc6 | -7.00655 | -41.9551 | 2025-10-16 03:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 458f5018-5441-30a2-8d8c-ee47d7316342 | -4.37241 | -43.3707 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99e62047-5547-323d-9647-273f92d7be29 | -5.86382 | -43.88898 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db877a1d-cd76-3da9-8d91-96d7879b6b1b | -4.66858 | -44.10864 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c5da067e-a0cc-388b-a083-a397114e02f2 | -4.35441 | -43.40384 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72836224-e232-3787-9c93-d6f38adde588 | -4.65992 | -44.1212 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84d4b277-7615-3e63-b033-b5239eda557f | -5.38422 | -42.80237 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 119e972b-eab3-380e-b4ff-4dd49cb2ab43 | -7.0358 | -42.73751 | 2025-10-16 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29b6b680-015e-32e1-b399-9236dd2c4848 | -7.25818 | -41.74926 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4fa0f4ee-25f5-3a75-a755-46831f9010fd | -6.15632 | -40.90742 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| bc35794b-ef94-3254-a40b-2dd7dcb051fd | -5.29883 | -41.17915 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c197b901-f42e-3798-84c2-84241cfcce54 | -4.66265 | -44.1063 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 88222e96-bf8e-38f1-8cd1-f68d6a1b4c14 | -7.3976 | -39.70339 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2796f3ee-7c62-3504-abf5-1441b253206e | -5.88307 | -43.8899 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4913b2e9-9874-34b6-b20f-1da5f6f7d0e3 | -6.15562 | -40.90623 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| a4935c59-59e6-395f-b962-7f4050513eff | -7.04218 | -42.73897 | 2025-10-16 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7faf321f-1c33-361b-8e4d-79c8b7a44e12 | -7.16599 | -42.51031 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 258747df-3c90-32ae-b972-33bd5474e765 | -6.37605 | -41.47871 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e8a96a13-071f-3b9e-bc17-b63afb9909fa | -4.66729 | -44.11598 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0cd55171-04bb-340d-a462-d06b0a745449 | -6.07999 | -35.33846 | 2025-10-16 03:25:00 | NPP-375D | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbae1b09-0a2c-39c6-880f-457fcdad6251 | -7.30121 | -41.85976 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0c49389b-ec45-3d39-919c-e3309c96483d | -7.29019 | -41.95243 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8262ba31-8223-36ca-9e58-0908150a7c2b | -4.37579 | -43.39184 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 89f74b2c-1beb-3acf-a6b4-bb6c5553cb47 | -6.44434 | -43.38458 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd3ca083-6480-3205-9e76-6702b37ab95b | -7.18746 | -42.36244 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7dedbf1c-8b06-3b47-b3a1-7f5b756d9c6a | -4.36487 | -43.38503 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 90e171c6-446f-3e25-9347-67e6955e097c | -4.3695 | -43.39973 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5f5d6b42-70e1-3c31-a8dd-f6c56feb012e | -6.13818 | -41.74975 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1d89ccb9-558a-3b55-8118-628316bb0278 | -6.73685 | -42.1558 | 2025-10-16 03:25:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1c66f73f-b788-388e-b208-aef038c4b21f | -6.98548 | -38.44369 | 2025-10-16 03:25:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb1ee8bc-9174-3fba-af65-5e025e4eace7 | -4.39549 | -43.40223 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8caf7398-e3d9-3872-882e-f552499bc290 | -5.298 | -41.18374 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1608daf-d050-37dc-bdb4-03b9bdaab19d | -5.8853 | -43.87793 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b89b46e1-df85-3bac-be03-85edd881e854 | -5.86491 | -43.88297 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| da1f62d3-8898-3f39-b666-bb4d7baa54d3 | -6.13494 | -41.76736 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3a098739-ee3e-3078-8226-63506fd48e49 | -4.35944 | -43.40273 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 66248dc8-6702-3b72-bbcf-d970539c7d18 | -6.3767 | -41.48023 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README13.md)
