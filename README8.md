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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ad95fb5-0e56-3051-a254-b2ad09640aa1 | -3.81775 | -41.01189 | 2025-09-18 04:12:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 748d3d21-17f8-3692-9489-f194d5ac633c | -6.63357 | -45.51351 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fa31f28-4bad-3302-a4a4-dc3c08fead34 | -6.20396 | -45.11837 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa97051b-f3ae-3f2f-85af-164aaa298947 | -5.80763 | -45.88251 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d55a337-c518-3565-8764-df59336ef70d | -5.79723 | -44.87876 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64050037-3d65-3be0-bf51-bc95e114ada9 | -5.54387 | -44.97003 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 632687d9-992c-36ab-8be9-614f326cd5e5 | -6.64125 | -44.66628 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0da47fe-c43b-3f1f-b409-2a74b1d8cb08 | -4.59183 | -43.38908 | 2025-09-18 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ddb06a4-961d-33bf-8f9c-3b961e2727b8 | -6.99406 | -44.76677 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ff8f7d4-393a-31f0-94a9-41e89081e818 | -6.41423 | -43.35802 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e84aa7-78ba-3659-ac5b-2a0be572f883 | -5.8881 | -45.7258 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a487b0-06f7-3ff3-a329-80f3fc2d1469 | -6.26867 | -45.12898 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 608c979d-9bc1-3764-a011-4cd4e5dd7f65 | -2.641 | -48.04336 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cddab1ae-e699-329e-883d-6ecff3160673 | -3.60731 | -52.6287 | 2025-09-18 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6f67c56-ef28-3594-9bfb-8b6f403f514a | -4.75187 | -42.5926 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c80c992-2b91-376e-a3dc-9b0ab71e38f4 | -5.07869 | -41.1732 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b6bbb40-a608-399e-ae96-605fcd81e5f9 | -5.84386 | -43.67645 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f147ad1b-347a-3665-b59f-97db552a4c87 | -6.5498 | -43.59602 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d78e7c5-f27e-3b10-b76c-2377db69c1be | -6.215 | -44.28877 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 727e8ee7-c041-3b3a-9b83-43e914e23db8 | -3.88273 | -47.59713 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68216354-33c9-3d5c-b584-411ed0ecaefb | -7.06792 | -44.35136 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee5024d4-dba5-3e30-ab81-aa4b61c92063 | -6.68189 | -46.30274 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2141dcc-0a1b-39a8-87db-627a622e9a05 | -5.78023 | -43.90736 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cc628a7-448b-3d56-a8a4-3c93c4f66641 | -6.03785 | -43.56783 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b572de5-78b6-30de-9a73-302d89db9206 | -5.98365 | -45.85199 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9f908ad-147d-3738-9a68-a0cb7e13cc78 | -5.65813 | -45.04541 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b38f78ec-138a-3106-bba7-9bb4fd300e39 | -6.29899 | -42.38506 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ad1f08d-7acc-394b-99ee-e6e4afd1e03d | -5.89164 | -45.72638 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7abf53b-9bff-3b6c-b60d-1a405741417e | -6.99112 | -44.45197 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2890c1c9-d30c-370d-b6ce-c549f3ed7f07 | -2.73452 | -49.40265 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 683e823a-56aa-3ca2-b943-ed33327d0114 | -6.479 | -45.72344 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4851e19-86f9-3ab4-8844-68ac638ceadd | -2.29505 | -48.1437 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d7a1686-2be0-3565-9ac6-a0f7f43378d0 | -4.8278 | -41.58881 | 2025-09-18 04:12:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd43912e-2099-3f54-a343-5382138b2bfa | -3.25713 | -48.46138 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ec9b285-7d3f-3f72-8d82-44da514f95f5 | -6.80699 | -45.62105 | 2025-09-18 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a8c6b00-1f8c-3a9a-a63a-f62bb98b3f4d | -5.81006 | -45.91215 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 793c719e-0e0b-37e8-b184-ac21892c2ea1 | -5.8237 | -45.91852 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26bc0a5d-11e0-3f41-8182-9b899954eb04 | -6.61307 | -45.63792 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de222ee2-06b8-3980-a145-4482cf2d9c49 | -6.61054 | -43.57724 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32cf41bb-9f87-3b86-8818-40ecfbb7ca2b | -6.58038 | -43.0364 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc7f5c69-5e30-3ba0-af6a-c41957228cc0 | -6.94524 | -35.1803 | 2025-09-18 04:12:00 | NOAA-20 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0ac60ac3-bfd1-31c3-a58f-d72d8f910d12 | -5.79624 | -45.71227 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59ea227d-97d7-3698-bc24-43cf259331d9 | -4.88534 | -44.96423 | 2025-09-18 04:12:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be988d80-df2d-3a1a-ae58-16adf3082b78 | -2.70917 | -54.95856 | 2025-09-18 04:12:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b869b0f2-f0bf-32fb-bd03-c63c6054fd24 | -6.55698 | -43.59359 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4a95aa6-8687-3bd6-902c-d90d2bd16ea7 | -5.21575 | -45.18024 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed281ed6-7fb1-3c21-ae5e-7429c23550b0 | -4.69465 | -41.96307 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b02fbc8c-d30d-31e0-9799-da074e40a57a | -5.82302 | -45.92261 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62b66c30-b62e-33f7-ad45-c32dc254134f | -7.05787 | -42.00519 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c0e77ca-fcf2-3fd8-9e8a-0e77a6ccc414 | -4.72601 | -46.49666 | 2025-09-18 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdd6a39e-a61d-37d2-8f74-0f760023203f | -5.67254 | -45.04385 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cb83c62-3307-37de-8e5f-2579fd495cba | -5.76567 | -46.15309 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61e53966-1ef0-30f0-b064-3d2374203dbb | -6.61021 | -45.63347 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10a9ebb1-b140-37d3-afd1-a52c21f0a83e | -5.53365 | -42.17574 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a518d684-2887-38e1-8a8f-ebec50041170 | -5.8029 | -45.91104 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7596128a-f3a0-3b60-af99-8c37bf1a5302 | -6.68843 | -46.30809 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 82d74462-17a0-3b35-8b97-7fdd214fcf77 | -5.81431 | -45.90863 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d3c2332-6677-30a4-a1db-4cbb2cfe7ef1 | -6.54648 | -43.59549 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a3b5d00-991d-305f-8d99-66eaaded15bf | -0.90291 | -47.5451 | 2025-09-18 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db00dad7-156a-36f4-a7d2-8acd8ae15ebf | -5.80399 | -45.70932 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c7d0940-989c-33d9-9726-4cc287cd8cbd | -6.26692 | -43.06515 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 433a8fc2-1c7c-31a5-8a84-949b853dbf7f | -5.81789 | -45.90921 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e743d395-0b74-32b2-91ef-c0e6478797a8 | -5.89047 | -45.64436 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0f9adce-36f5-3700-acd2-4a9f3545d833 | -7.27362 | -40.17583 | 2025-09-18 04:12:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8442769e-8188-373a-9c42-d6be0d5e8206 | -5.59607 | -45.36171 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fdfe9e-d39c-32a0-8f83-01fd72d17a0b | -4.81117 | -43.29182 | 2025-09-18 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a8c61c-9fb1-3d8d-8cbc-10c4e0edef28 | -6.60667 | -43.58017 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9495d8c3-bcbb-3b62-9444-2293a6a2b9de | -6.47836 | -45.72736 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1352b459-a79c-30ed-a085-bdf9a441ebf5 | -3.89739 | -40.81923 | 2025-09-18 04:12:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 212e6c0b-40da-347d-b5ca-8f51369ec58e | -5.21513 | -45.18407 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d07da58-98fc-38de-9b04-ffbe7a1e5436 | -6.38184 | -42.65788 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0660988-765a-3652-aeaa-f4a8cf46e6b9 | -3.5169 | -44.03382 | 2025-09-18 04:12:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f21d5c71-11b8-3dab-9a29-d355f27d8ae9 | -7.05851 | -41.66687 | 2025-09-18 04:12:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ab63310-d762-327f-b85b-4054ca6728ee | -6.68481 | -46.3075 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5b025c0a-7f70-3770-864c-6e498382d462 | -6.14868 | -45.99301 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90c0b437-4f7a-3ff0-82b9-86659f959232 | -6.72328 | -44.1514 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ea5e0d4-4e9a-3272-9868-6bc3b5ceaa4f | -5.88975 | -45.89577 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0111102e-c741-356c-a5d7-01c5ae969159 | -5.76901 | -44.83622 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60bb8801-2894-363d-9846-514dde3a25a1 | -6.40983 | -43.36443 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b34b0b3-90d2-36e3-9238-99aa500a9a04 | -3.04883 | -47.01103 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddcdcbad-bbfb-3d4c-8ba0-99d80ee1f83b | -6.17823 | -44.4961 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafb6c56-d0a2-3a1e-90bd-a9176d2fa897 | -6.92265 | -44.81488 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3b04724-b499-34b2-878c-2ea4ee2bc51f | -4.61797 | -47.41659 | 2025-09-18 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6619e72d-07e6-39f7-9a53-a455ede8cb70 | -3.79245 | -44.4147 | 2025-09-18 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d78e4a20-f224-3014-acf6-b400f3f6bcc3 | -6.36437 | -44.42209 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b6ed188-9acc-3ef9-8ed9-f81dc519f6af | -3.48857 | -39.59081 | 2025-09-18 04:12:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ced168eb-143e-360e-b827-403ac4107064 | -6.39979 | -44.00526 | 2025-09-18 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd0e3cf-c2db-3d2d-9b84-2524cc3e7b59 | -6.2693 | -45.12517 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7e9fe0f-30fb-38a4-96e6-5bd8c7cb61d5 | -6.5013 | -46.00958 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9277ee52-38e9-302d-b030-ca6cc3bb815e | -3.32026 | -48.70831 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 323db0ee-6cf7-35fc-b26a-116a36c4e8de | -6.63184 | -45.51433 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d90b65d-b2db-359a-b894-d0f0aa9c6a94 | -6.98554 | -44.44387 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3360836e-8334-3bad-8f20-c8e4aa57ebc4 | -6.47963 | -45.71951 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e113a13b-5d66-31e8-a963-1c44af380d3f | -4.71336 | -46.1294 | 2025-09-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed5a6bd8-14e3-3d63-a5be-6598b95f08b5 | -6.40151 | -43.33117 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 140d3e58-d361-3268-bf57-445f775c00f4 | -5.86608 | -45.88363 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecdf3d03-0771-3a2c-9e8f-39e80b51ed42 | -6.43528 | -44.37845 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38745c47-3e97-385f-9352-8457e8a15007 | -3.19642 | -54.98273 | 2025-09-18 04:12:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7873d16b-2452-327f-aedc-5074688ec80d | -6.16279 | -43.68068 | 2025-09-18 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bfdd4540-933a-3ca0-bd25-6ef142fcbae9 | -5.77689 | -43.90684 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README9.md)
