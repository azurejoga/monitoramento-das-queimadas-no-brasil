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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a4d235-4944-3721-bcb0-e729eb7fb8f7 | -6.00947 | -43.79229 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e178f76-73e5-3c04-9c65-c6165f2d799a | -5.64389 | -43.95612 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba178eb8-2b57-3384-989d-81be803e2a8b | -7.63789 | -45.43571 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b97e7601-f83c-3326-b989-1c4cd9b66489 | -5.82934 | -43.87814 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bc559ac-a673-3fe0-b363-809e68b593a2 | -9.94559 | -43.58986 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f704551-5886-3cb0-ac46-64d8f2dbef35 | -9.80451 | -45.94398 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be61d860-838b-3348-b3c6-ccc1ee43cb0b | -3.098 | -47.0114 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| aa095abf-6474-3b04-9945-b6d6b53a7dbb | -8.56539 | -44.70696 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08da3c17-7cda-32d3-b7c1-0a614479bf81 | -6.05895 | -44.43492 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02c15d62-5456-3f54-a0d2-fee2077670cd | -5.64426 | -43.90997 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 869c010a-8e97-3ac8-b267-5b7bd4f57f67 | -8.96031 | -50.327 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8875cb0a-ce67-3758-8e6e-437aa83c4648 | -8.15368 | -45.90017 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e66f14f5-544b-3c21-8977-0ddcb0e14ce5 | -8.52355 | -44.66819 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4084811-a24b-39c1-b2f5-966b3f0def47 | -5.15384 | -43.71567 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0864a5f1-f120-3b65-a0fa-090cc22c9361 | -4.31201 | -48.09048 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51f632ab-36cf-3036-84c3-b3595c7612f4 | -5.50694 | -42.72397 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cb759ac4-c328-33e4-bff3-1e07466e9969 | -6.67492 | -43.91008 | 2025-10-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 263e66b0-d1a8-32b0-88c1-98e1a4cf9d70 | -7.30485 | -42.87086 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0e7a04e-4559-315a-8999-3156c0a515d2 | -9.25732 | -45.72421 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48ea443-f6c7-3c88-81a2-1df5ffe842c2 | -7.15991 | -50.5455 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a39b5ede-4f02-3a19-bf84-e4a75e224519 | -6.03261 | -43.59828 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b273e135-b85f-3d6c-a5d6-1d9221cb9eed | -3.88221 | -42.51969 | 2025-10-01 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1272dec-6ac9-3e8f-9bad-dd0449bf16de | -9.89793 | -45.93456 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72b5d931-3b84-38da-956c-6ba1773e727c | -7.56557 | -46.78345 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5458e70a-e97b-38c5-826d-33b377da7502 | -8.16282 | -44.12005 | 2025-10-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7344243-a7ba-3402-8d10-8297476836bc | -6.39873 | -41.75744 | 2025-10-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b611f278-665d-34db-9a72-c137d474f623 | -5.88667 | -43.68386 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa135c56-5319-3225-8f68-f04ff73c3402 | -7.7796 | -45.72513 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cfcb51b-0259-36f2-a6c3-1d5a0e5ea6ea | -8.57768 | -44.75871 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56b24254-cede-3d0e-857d-c7a1564a3716 | -5.61966 | -43.23026 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0e9800c0-16a0-3f3f-a97c-ae0960724b23 | -5.62247 | -43.23436 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3f0d8005-c0f9-350c-8aef-7ac19493aacb | -8.21826 | -45.79243 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cd80eba-fa63-3786-9597-2692873316e8 | -5.96194 | -43.28271 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b2e4ea76-fca3-36f8-a7fe-5ec76c6c57a0 | -5.95961 | -42.94932 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e297ac1-1e4d-3f92-9bf2-60ba14d23ede | -5.2983 | -43.13665 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d70f2b92-0482-3ff9-9bfc-801b8af74a99 | -6.40573 | -42.81006 | 2025-10-01 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87d439d8-c107-3b00-9955-aea27dfa2edd | -6.23244 | -44.15149 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 527bf545-67f5-3ec3-bbee-b2e0857b935e | -5.46822 | -43.06744 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdb69705-207f-33d8-a597-befdb1e15521 | -9.93159 | -43.6833 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a99672ed-86e4-3f80-b249-7b42013af1b3 | -5.70175 | -42.66303 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a3894899-2492-36e1-9239-22d0591a614a | -9.92931 | -43.67532 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6792eaee-05b8-3382-83ea-b31871ac5f6f | -5.79083 | -43.29274 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 607ee43e-bed8-35d3-82a2-7bd8f26a4f83 | -5.24907 | -42.89734 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34ea6241-dbcc-3458-8fa9-d4899e3feb33 | -6.39012 | -43.39557 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01ee337a-93f9-3d3a-8b23-36a45184211b | -5.71074 | -42.88237 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ad3d081-b23f-36b1-a63e-9c53396ab701 | -7.56293 | -46.77197 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04236db0-7876-3b70-b254-4103deefd2e2 | -6.31035 | -43.47476 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1739475a-1ead-3732-8c11-694887a0c6a1 | -9.9354 | -43.61127 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13ddf245-eb3b-3965-a0b1-b5c132a80651 | -4.11836 | -48.79953 | 2025-10-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09e5898b-b96a-35be-b885-4573fc334c72 | -8.5886 | -44.73193 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edd4fe3c-ccde-3426-bc4e-2f22d13a0532 | -4.52609 | -43.79131 | 2025-10-01 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1ecb4ae-4e0c-34cd-8dd2-67844c4eac19 | -5.7348 | -43.96302 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f23354d9-c112-3c0c-981d-aae6ffa0f9fa | -9.94503 | -43.59362 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c3a1a50-21de-3945-b013-10494ef520c9 | -2.30301 | -48.14272 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d35e46cc-7e1c-3f4c-a39e-d309b97b7a19 | -7.47215 | -47.27565 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 172e2029-df7f-318c-9879-bf733126f21b | -7.15905 | -50.5417 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd46f6ec-75b0-3c26-81a2-f9b73e34efbc | -5.32384 | -42.77108 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2823ef5c-0068-334c-aa22-29cbc98f57af | -6.75224 | -50.92469 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce556b9-6cbe-39a0-9118-1aae50e5fbf9 | -3.1058 | -47.00844 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c27398de-d40b-33e4-b1b2-58c2f54ddcb0 | -9.93098 | -43.66413 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1c39437-6094-3820-b288-19c28fc40240 | -5.81245 | -42.88267 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 488ca62f-ffee-39e2-9f23-d3effa044b12 | -9.44136 | -45.48299 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65172e7c-8290-3892-bea3-8480f098a4c7 | -6.55094 | -43.94135 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3de8d655-7854-38af-bf3c-b1d59084646f | -5.7243 | -42.8844 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 704a6f5e-6c3c-30be-b5d8-4047e29a889b | -8.94571 | -51.68417 | 2025-10-01 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b668486b-258a-3e32-a844-764bdfdae6a4 | -6.1208 | -43.22587 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ffc71940-ab97-3a53-b28a-d2cb3e309586 | -8.52301 | -44.67167 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edef4c8f-29ba-3bd7-b523-106701477a12 | -5.82597 | -42.86237 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49d79279-dee5-39a4-873a-47625461947a | -9.93836 | -43.66145 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49d46b93-d5a7-318d-9662-abd36a3571c1 | -3.42166 | -51.22827 | 2025-10-01 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b1e360e-1443-3569-a9c8-be1e0df8ef44 | -5.7943 | -43.06914 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b90a8272-200b-3d14-8c24-f17a1b9ba40b | -5.94845 | -45.87564 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dd28b5d-93d0-3098-afb9-95ce589cfa4f | -9.26446 | -45.7004 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfc3b864-5c98-3b0e-8c62-a6130b635801 | -7.76246 | -46.77767 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10b54bd4-9cef-38a0-a131-0a12c823802a | -5.72825 | -42.88125 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 748a6c5d-4e0c-39a9-a008-20d462b24444 | -8.56008 | -44.76311 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf345317-229d-336c-92ac-eee8f732ea68 | -9.94289 | -43.65449 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f465ab93-5412-318c-8c80-cae4dae379ea | -9.9412 | -43.6657 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b10ee4c4-af0d-339f-95c5-ab48e0530b7e | -5.50473 | -42.76131 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e472b17-1ec0-39be-8cd6-1709ef02155b | -9.13401 | -50.77671 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ac0ff1-40fb-3629-99f4-03b7b4910af1 | -5.63826 | -43.92685 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17bb9ef9-739b-37b2-ac83-3354abce5395 | -8.5564 | -44.65563 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bc25af1-711b-3e9c-a7ed-58ded597ca1b | -5.50298 | -42.72714 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 07b677fa-23dd-3c79-b78b-14f51aa2a717 | -7.63241 | -45.44903 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3433ad44-40aa-3037-b8b7-26c17813028c | -7.79213 | -42.50749 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e397c73b-eb9d-3f21-ac43-992b3029a6ee | -9.32713 | -45.68896 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c1341d4-f63c-3899-8557-e5890c8cc58e | -7.55895 | -46.7751 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3be3768f-d259-32c6-9fcd-f337a2e827b4 | -5.72881 | -42.87762 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cd69ea99-f71d-3422-9e27-622e5dc873fe | -5.70736 | -42.88184 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fa1ad8cb-2c1c-3632-a7f7-6b2a9301d226 | -6.258 | -43.65881 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 33e9164a-7e24-36d1-a803-9bceb02cddd3 | -5.72282 | -42.68911 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6cda1ddd-b333-3bbb-922c-2f730227d327 | -11.8485 | -48.0373 | 2025-10-01 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 28793eab-894c-3099-8fcd-837fece56d95 | -9.3089 | -54.5229 | 2025-10-01 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ab931e8c-d60f-3944-99eb-0955445560bc | -11.8482 | -48.0595 | 2025-10-01 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1674ab52-831e-3905-98fa-24523229007f | -16.2562 | -50.9275 | 2025-10-01 04:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 220d76f5-80f7-3a67-9011-3c8c4d355e01 | -11.37916 | -45.07285 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 281c133c-d6b1-3ae5-9313-d10ad25464ad | -10.48377 | -55.62122 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91cbaf68-85eb-3d08-b84c-48e0e80624f1 | -14.79186 | -45.78664 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 020af558-09e9-3d4d-b82f-60c2880c8985 | -18.42239 | -39.79684 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fef11d4-69fe-3d96-b71d-36282bd136e4 | -15.75682 | -43.71925 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README44.md)
