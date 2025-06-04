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
| a849b4d5-d737-3655-ae21-7244a4eca8ad | -7.8863 | -46.1856 | 2025-06-04 00:11:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3c6a9f8-6c0a-3d46-8e81-daca7192a44b | -10.6069 | -44.764301 | 2025-06-04 00:11:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a6660f53-7d26-34fb-989a-5807d269ea6f | -4.8145 | -45.254002 | 2025-06-04 00:11:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86412cab-fe4e-3db5-a773-478d8059322b | -4.2447 | -47.574699 | 2025-06-04 00:11:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61c47cf-266d-33a4-bd19-fb5957bcbc45 | -7.2375 | -43.127899 | 2025-06-04 00:11:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb2cc49b-f7bb-3436-a543-830381738e7d | -6.9602 | -42.9052 | 2025-06-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| cda519d7-9402-30f2-aca5-d9f31d4f031c | -10.6247 | -44.767 | 2025-06-04 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4c713942-7f14-3a3b-b717-8d10be4ab81a | -7.2211 | -43.1388 | 2025-06-04 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 760226a1-b57f-3720-be39-b2861108833e | -4.8033 | -45.2594 | 2025-06-04 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 93373690-3b49-3918-b00b-bc97b84d5a92 | -7.0169 | -44.5954 | 2025-06-04 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f4d294e2-64eb-3dd4-95d0-c6ace95ce8de | -7.0169 | -44.5954 | 2025-06-04 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fcab5426-629c-3281-ac72-1d51482de924 | -10.6247 | -44.767 | 2025-06-04 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| b0bb96ae-c160-3dba-852b-74d18705a9c1 | -7.2211 | -43.1388 | 2025-06-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 58ebdec8-829e-30b0-9a84-d77929981e67 | -6.9602 | -42.9052 | 2025-06-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 1bfba5e3-638f-31ee-afa9-66e986c9c864 | -6.9791 | -42.9034 | 2025-06-04 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| cee25b07-170f-36c0-a855-334f75504afd | -6.9602 | -42.9052 | 2025-06-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 72e1c9e1-b061-35d8-b0ce-eeaf10c6f58f | -7.0169 | -44.5954 | 2025-06-04 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fabec2b0-6399-3d83-8589-e15b2d0aa3b1 | -10.6056 | -44.7696 | 2025-06-04 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 01abf9ad-cf25-3e62-b953-4038f0e1eebc | -6.9791 | -42.9034 | 2025-06-04 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| a7c48496-d87a-3bd7-ab38-cac995c5db03 | -11.8365 | -51.2854 | 2025-06-04 00:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 95b0e0e6-e435-3279-a473-acb74439cc3e | -8.7606 | -49.7643 | 2025-06-04 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c9c92ff6-2dd4-30c8-b008-0348b9b4bda6 | -6.9791 | -42.9034 | 2025-06-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| fe3b6cba-1170-3ae2-9eba-9bfb28a78b48 | -7.2211 | -43.1388 | 2025-06-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 4a049166-8a1f-35ed-9493-94acf40975b7 | -7.0169 | -44.5954 | 2025-06-04 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c7ea616f-b6ef-335a-9902-afc40a65c322 | -6.9602 | -42.9052 | 2025-06-04 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| f23967b0-91d7-3114-b51c-d5df84fd1392 | -14.0235 | -55.1138 | 2025-06-04 00:55:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd9c4e45-b913-31e1-993e-3d29076020ee | -15.2744 | -51.470699 | 2025-06-04 00:55:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f60a8edf-1e6b-3b30-98e8-fe8c81ea007a | -10.7004 | -57.648201 | 2025-06-04 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef5febd-cadf-3fbe-9796-ac9fa27fe8c3 | -11.8353 | -51.282101 | 2025-06-04 00:55:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48951bb4-8c7b-3f12-bfda-990bf5e6bcc0 | -11.9152 | -58.669399 | 2025-06-04 00:55:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 118cc365-4c29-3b76-ac82-752d246b1e7e | -13.9678 | -56.777401 | 2025-06-04 00:55:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dea34888-d754-3d35-b9d2-16671e6ad85a | -10.6988 | -57.641201 | 2025-06-04 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36b15a80-9bca-371b-8915-7626cfa999b2 | -11.9045 | -54.792999 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0590ec4-089b-3982-9721-a79dcb08f235 | -15.2772 | -51.482101 | 2025-06-04 00:55:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f57e14d8-0a44-3e8d-ab41-f34ae927903a | -11.8385 | -51.2953 | 2025-06-04 00:55:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37548da9-239d-3497-a413-18e0bd7a51d7 | -10.5012 | -53.6591 | 2025-06-04 00:55:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a840ae0c-493e-3ae6-a208-ca880240086c | -13.1024 | -52.020901 | 2025-06-04 00:55:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38bab9ae-1d14-38f4-8e55-5c043091de56 | -11.81 | -57.3577 | 2025-06-04 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7bf5ea-a7d3-39e6-960b-fd8a58a1ab26 | -8.906 | -50.0373 | 2025-06-04 00:55:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb4c7e5-fabb-3649-aa21-29d299d15540 | -11.3896 | -56.5453 | 2025-06-04 00:55:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa3dfe89-82f3-3b7c-8d4c-8f05fa4b4b23 | -11.9181 | -54.807098 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16885e2d-6427-3460-9eaa-f555aaf4a8c1 | -10.0763 | -55.543301 | 2025-06-04 00:55:00 | METOP-B | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 381c12de-5464-32df-a8c7-821796c31d46 | -13.1494 | -56.804199 | 2025-06-04 00:55:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d01423b-961d-3ae0-b645-310bf16303d3 | -11.5576 | -56.422298 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0f1589f-ff7d-3c0f-b981-e9707fd29e43 | -13.918 | -54.6581 | 2025-06-04 00:55:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e70ee839-d436-3064-ac3a-e75ddb40fd9b | -12.6531 | -54.109798 | 2025-06-04 00:55:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce39ac4b-2fc3-3417-9ea9-b0fdc435e7aa | -10.4989 | -53.6493 | 2025-06-04 00:55:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2571e6ea-fc3b-306d-898a-86e28e94bdef | -11.9201 | -54.8153 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4b7d9ae-e303-3067-b5c5-9cba05bf729e | -11.9279 | -54.804699 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03c00ef0-81d0-3b7b-8cba-b83bba523d02 | -14.0368 | -55.1269 | 2025-06-04 00:55:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6563e1f6-4de8-317e-92d6-64739494acab | -11.9026 | -54.784698 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4221c60-1cba-3e2e-b6e9-2a4924af840c | -11.8482 | -51.2929 | 2025-06-04 00:55:00 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b008e5fc-5e24-3753-80fc-39fda12cde1b | -12.6552 | -54.118599 | 2025-06-04 00:55:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b39ffa4-a27f-3bf2-abab-3f5056af3462 | -11.5674 | -56.419998 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78db365b-1f85-3a06-bd8a-cd27f85e07e9 | -14.0253 | -55.121498 | 2025-06-04 00:55:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55609321-e8fe-327b-9d82-a7cb6fda4aec | -11.9124 | -54.782398 | 2025-06-04 00:55:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36d48df3-fd34-3ce5-8f7c-f72cb5f1aa36 | -11.8084 | -57.3507 | 2025-06-04 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df711ab8-4be1-3ffe-8cda-7871462102e9 | -14.027 | -55.1292 | 2025-06-04 00:55:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24dedc4a-dc49-3487-9f39-c931586180f8 | -11.9038 | -56.402599 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf70b3c-69e6-37f9-9013-d19d7bc01cfb | -11.5593 | -56.4296 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f64ed46f-373c-36d7-af96-de71a6f86f54 | -12.5222 | -57.1791 | 2025-06-04 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50f4d25e-64d2-39c1-b823-ec2c7784a857 | -11.5658 | -56.4128 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e807e96-1f8c-3059-b579-29a23b0e2e82 | -8.9104 | -50.055 | 2025-06-04 00:55:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb866ffd-8e28-36c1-8492-64944ddfbfee | -11.5641 | -56.405499 | 2025-06-04 00:55:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c944eb5c-f043-3d86-8482-6ec7450fbcfc | -14.0386 | -55.134602 | 2025-06-04 00:55:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96dfa432-0d81-3d81-b77e-23e3a28a7adf | -7.2211 | -43.1388 | 2025-06-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| d260ba4a-f497-3b28-844a-654e2bf37021 | -7.9116 | -50.3666 | 2025-06-04 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| af0321ad-5817-323d-b329-59b775a1a9bc | -7.0169 | -44.5954 | 2025-06-04 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 69bef17c-2f9a-32d4-ba43-65390710800e | -7.2023 | -43.1406 | 2025-06-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| d45bccb2-c4c2-3480-9454-36626e409451 | -6.9602 | -42.9052 | 2025-06-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| a5a0c924-1dfe-30ac-9cf9-5999a5e29443 | -6.9791 | -42.9034 | 2025-06-04 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 68e356e4-2ff1-39da-b321-cff71a8fa594 | -6.9602 | -42.9052 | 2025-06-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 37d34bcf-126d-339e-b5d3-575240b986f4 | -7.0169 | -44.5954 | 2025-06-04 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7b872709-f0e2-313f-8f94-800a8ae8c442 | -6.9791 | -42.9034 | 2025-06-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 5c7054aa-ffa1-3952-92b4-e0d47010ef3c | -7.9116 | -50.3666 | 2025-06-04 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b7e0b585-41e1-3819-84a2-e1d4e2f17d5b | -7.2211 | -43.1388 | 2025-06-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| bda6aa95-7722-32e6-a7ad-b3461accfd45 | -7.0169 | -44.5954 | 2025-06-04 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e31f2d8c-ee3b-3a96-8d0f-ad2455bb84a0 | -7.9116 | -50.3666 | 2025-06-04 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e027e259-0b81-3d3b-931b-c7eaa274332f | -6.9791 | -42.9034 | 2025-06-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 287f376c-e97a-3ee1-a90a-43d0b5e2b678 | -6.9602 | -42.9052 | 2025-06-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| b3286370-9ddb-3924-9d81-53d1f2d614d5 | -8.7606 | -49.7643 | 2025-06-04 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| c6460fbd-7832-310b-835c-6ba17aa84d7d | -6.9791 | -42.9034 | 2025-06-04 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| d55617a3-b4dd-3d18-9ade-deddb793ed96 | -7.9116 | -50.3666 | 2025-06-04 01:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 25f16927-4646-398a-84c6-4333f8db5b15 | -7.0169 | -44.5954 | 2025-06-04 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8af26421-20d0-3df5-b125-ddc9ce168a1f | -6.9602 | -42.9052 | 2025-06-04 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 3b0fa631-1721-388f-b6a3-dda1df34f57c | -16.40149 | -58.18026 | 2025-06-04 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2968c95e-0ecc-3660-a047-77da51c48832 | -11.84235 | -51.3039 | 2025-06-04 01:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 42c316c7-3c07-35fc-a246-9bb0ffc7475e | -9.6255 | -62.81915 | 2025-06-04 01:37:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6a1c999-d34e-3641-a092-e4975912ea82 | -11.84141 | -51.30925 | 2025-06-04 01:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 17239b27-d2d5-3ac6-871c-109f979ba7f8 | -9.62427 | -62.81022 | 2025-06-04 01:37:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c976224b-2762-3eec-873a-f71ba8d1b781 | -11.56261 | -56.42467 | 2025-06-04 01:37:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 40fed0b0-6385-3629-90dc-aa8e86254a75 | -14.02522 | -55.13816 | 2025-06-04 01:37:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 80f645c9-7b47-326b-b14c-eef7725e0cc4 | -9.60243 | -63.25947 | 2025-06-04 01:37:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f89379d7-c62c-3ee1-ae81-c01ebaf03f23 | -14.02194 | -55.11867 | 2025-06-04 01:37:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2c06e256-9107-351a-a78b-2a6af43b8506 | -11.90121 | -54.78733 | 2025-06-04 01:37:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 7be4fece-57cc-3007-b7fd-d768b1a3527a | -10.69438 | -57.6485 | 2025-06-04 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4b61ef2f-116d-38f9-b780-a70e878d2c0f | -10.49041 | -53.66276 | 2025-06-04 01:37:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8538522d-c750-3296-a24b-dc5197771d2d | -11.90486 | -58.67675 | 2025-06-04 01:37:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63ea175f-4c83-369a-be46-b3d219e02fb5 | -11.8033 | -57.35783 | 2025-06-04 01:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 67c20a46-5205-3960-be42-e9d31ef6d8d4 | -11.55083 | -56.42671 | 2025-06-04 01:37:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |


[Clique aqui para ver as próximas entradas](README3.md)
