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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a150af7c-0857-326e-8c55-c7b6f0ec6e39 | -4.60732 | -43.91064 | 2025-09-25 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5879ce3-bbd3-39d8-b52e-0243a98079e8 | -5.59863 | -45.36315 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 14b11ad8-0778-397d-8e16-5a8309795661 | -4.42837 | -47.26765 | 2025-09-25 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13635fe8-3721-3298-ad3c-1a57b4f94c0f | -7.2593 | -44.90553 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee2080b9-bb1c-3268-b8d4-6505ded913c8 | -6.73383 | -44.04358 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 888766b9-cd18-3481-bb59-4d6d0974ed42 | -3.21043 | -54.96402 | 2025-09-25 04:32:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c1924d3c-bdb6-3f78-a852-95360ad3b4cc | -3.40179 | -47.49947 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51fae2f-461c-36b1-b1b4-55aa73c872e6 | -5.78571 | -42.55429 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2582d1b2-66f6-3e21-a045-adcc2597d3ad | -5.05175 | -38.07454 | 2025-09-25 04:32:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3283d18f-b904-3b11-96df-a6ac866b3507 | -2.30585 | -48.14649 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcc21b81-188c-3cb6-8b50-1817f86472bd | -4.76802 | -43.25137 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5faa4b72-8f8f-361e-aabd-d3c3d8ef288c | -6.56559 | -42.06297 | 2025-09-25 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0a9163ee-ceb5-395f-8e9a-cf8294e3440f | -4.34633 | -50.50105 | 2025-09-25 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 279215c7-8a36-3e12-9343-85ec11d809f4 | -7.2665 | -43.01944 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1a88a288-2c1f-311f-8ec7-73f0de5adb3e | -3.4384 | -44.48581 | 2025-09-25 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| daf2f160-762d-34be-9efe-06583c454645 | -5.72705 | -42.61306 | 2025-09-25 04:32:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9329c24a-7f68-3692-8033-2ca94d37ea04 | -6.43132 | -46.18565 | 2025-09-25 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42778de7-0ee3-3157-a4f9-4dc18f874e77 | -7.2615 | -44.90683 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ced2f1b8-4731-367f-9faa-6c44749334a2 | -4.03287 | -47.77143 | 2025-09-25 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ec4341b-2c6a-36c6-8b68-70430bca0aa4 | -2.25529 | -47.88451 | 2025-09-25 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9065d129-3189-31f9-b301-f0c49c594678 | -3.83353 | -50.97779 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c832b3ac-8937-375a-a0a5-4957ac2e584d | -4.91044 | -46.8372 | 2025-09-25 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af847d7d-a2aa-30e8-9ba5-c6b391b770e6 | -6.22078 | -42.8802 | 2025-09-25 04:32:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 523502a1-4fe2-3234-b2b1-0ee33c0c8beb | -0.61947 | -47.31235 | 2025-09-25 04:32:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91e5199e-2bd3-3b3c-bc1d-a071f35616d7 | -6.14132 | -42.45461 | 2025-09-25 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99830c07-137d-37ef-a7bc-8ffa56df5433 | -5.73326 | -42.28503 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 459c873d-c3b8-346f-a297-bf69ff0987c5 | -6.55397 | -46.11716 | 2025-09-25 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c53aefb2-e757-3552-a1d1-1bf2e845e415 | -6.41975 | -43.0822 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3096ca7d-294e-3d87-ad14-d23e3318fd8c | -3.33676 | -46.54211 | 2025-09-25 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2e77c55-2e95-3ae2-9c91-95ed170fbf47 | -3.3047 | -42.17684 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fcea928c-14ae-3f6f-b095-2b7f564ee551 | -7.18042 | -42.23534 | 2025-09-25 04:32:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 83576df1-cab4-3e1d-a295-a7bbebfc2822 | -7.31784 | -45.75196 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92b545c0-817b-3855-9ff1-a246fb8d97b8 | -5.86986 | -42.26554 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 86a6f46b-af5e-34a9-88ed-1d78ee88e166 | -4.54583 | -44.02348 | 2025-09-25 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0329a15-51f7-3e17-93f1-840022fcb698 | -6.42617 | -43.09377 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d89957df-2ede-36ee-93b1-56e321b41d20 | -6.41924 | -43.0857 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a8d008f7-eac0-3c9f-9afe-3d3627080a4c | -3.2354 | -46.79843 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 953cc704-8aab-3055-8a0c-6992cef0fedc | -5.93926 | -42.93258 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d77e5c4-2575-3052-b018-6feb399511fc | -5.77756 | -42.55292 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3819ee50-9eea-3958-bc6e-9f5e02f03829 | -4.18101 | -42.96128 | 2025-09-25 04:32:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b51a856d-4f8e-3dff-8c0f-03216190cfab | -3.01426 | -51.35654 | 2025-09-25 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb75673c-94bf-3232-9e4b-9c056c66ff79 | -6.79431 | -41.76165 | 2025-09-25 04:32:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b07a669-6cf8-3fe1-b519-c02121f9e8ca | -6.14544 | -42.45526 | 2025-09-25 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9f921fb7-8341-3dfc-af51-042ab33ab9d6 | -3.30416 | -42.18038 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2d743dfa-3162-38dc-ab66-5a4365ede6d8 | -3.98859 | -47.00807 | 2025-09-25 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75818f1e-4f75-30bf-86e0-3ff90563ae6d | -6.43471 | -46.18616 | 2025-09-25 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 161c8e8c-318e-39da-85a8-84feaa7b39f6 | -5.93877 | -42.93598 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 142e0cfe-a9e6-3e28-af25-6385741c679a | -7.2579 | -43.02172 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65af5ecc-2fd3-33c5-b568-94d7968bc537 | -6.72456 | -43.97324 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 657d3f36-d9e9-38a0-9fcb-99067651da95 | -5.59921 | -45.35931 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 06bcec27-e63d-3a81-a07b-0f5fc4dac992 | -5.73216 | -42.6067 | 2025-09-25 04:32:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c6c85a7f-2eaa-3d6c-926c-8022c1b51bdc | -4.81451 | -45.19782 | 2025-09-25 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e08ebbc5-0138-3094-bb2c-bb2e98b004b7 | -4.73957 | -44.42931 | 2025-09-25 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7c25ce7-143a-363e-8c63-67407fd68ac3 | -7.22704 | -45.17556 | 2025-09-25 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1a51c5b-7890-3770-92e4-09e6cebed709 | -7.29984 | -43.9091 | 2025-09-25 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bf33252-5d8e-3029-846c-512337ada2a4 | -6.91628 | -45.65048 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5ad1d39-acd2-3194-8a32-7f9359d43711 | -6.30807 | -42.53561 | 2025-09-25 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ba038333-53b5-39db-8c52-5c42b124e18d | -6.14013 | -43.45115 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36bb4105-4692-389b-9ced-b4e23304f8b6 | -7.25841 | -43.01817 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b8de62c3-693e-3bc3-a0cb-b10f4d72197d | -7.31726 | -45.75582 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27c0e59f-7b86-3c1f-8b21-fe9ea7497c82 | -5.53094 | -43.87088 | 2025-09-25 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 24c015c1-598d-3954-913f-300a2e76e11b | -7.26213 | -44.90265 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edceb66f-1e84-3ec2-bf56-ed03b218966f | -3.81878 | -50.97551 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a514168-a605-30d0-9b66-0579b02a6942 | -5.76982 | -44.27285 | 2025-09-25 04:32:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68a359ee-0ad6-352c-9fd4-bb07150fae68 | -7.83831 | -43.8017 | 2025-09-25 04:32:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a4a3701-bf47-3c9f-b818-2109f2a8e59c | -6.55103 | -43.83915 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8099fa24-46aa-3417-828e-d0a18cbb2f90 | -3.7387 | -49.0544 | 2025-09-25 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0069f06a-141f-392e-8250-c796440564af | -3.78036 | -41.731 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 981b0b96-899e-34ee-a372-41b934309b0d | -5.76365 | -42.56317 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ac507b6-ac61-3d2a-8fc5-96683731d34e | -7.59515 | -42.32712 | 2025-09-25 04:32:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0a37a154-f5dd-3e27-aac2-555385553a79 | -6.38977 | -42.95242 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47aa38c7-f2fe-3db0-b00c-7aff1a3882dd | -2.92015 | -48.31117 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ec19838c-40c1-3d5c-81cb-135dc185fe57 | -6.42219 | -43.09317 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ffededdc-5083-3223-b3e4-9b36196d8324 | -2.91736 | -48.30713 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac900000-25d3-3728-bd95-332e84d739b4 | -6.68498 | -43.12778 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9448876d-b72e-3b1a-832d-ab94721b3836 | -4.60362 | -43.91007 | 2025-09-25 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57979bc9-033c-30fc-b6fd-334bd03df9ae | -3.2387 | -46.79893 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b7fa1d0-9de5-35ab-b266-71ee52dee553 | -3.37867 | -44.37946 | 2025-09-25 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e669609-18cc-3644-8feb-67e04d6c7263 | -3.78714 | -52.30326 | 2025-09-25 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53ed6b9b-878b-375a-b927-ce5b4282e4be | -5.01733 | -42.79438 | 2025-09-25 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 440cd4a5-2fa1-3ad4-8cc1-93bcd362ba6a | -2.92348 | -48.31169 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| f6ac05bb-1be5-3b63-8dce-1b897d059c09 | -5.06369 | -44.31577 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cd9cbbf-2985-37f0-8856-b5c82b29adab | -5.54453 | -42.80952 | 2025-09-25 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b9724f31-b4f6-326e-b114-52b409201054 | -4.57586 | -41.50409 | 2025-09-25 04:32:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 953b9ee3-67cf-3c33-895e-63d005343e52 | -6.69919 | -43.53118 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 108c477f-e798-3687-9ab0-f99b8dc3437f | -6.42476 | -43.07594 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3ba0b363-6312-30d9-9785-3722529b77a8 | -3.77503 | -41.73801 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b435dfc-63b7-35fc-a53e-f5ef6e357f3e | -4.66957 | -48.15817 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 847f7ad0-0c9c-3341-b8e5-fa86695c3ec8 | -6.07457 | -44.07888 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54e9237f-c3ce-30d5-9306-ac7c635db8d4 | -5.75606 | -42.5582 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 45de772d-cdad-3b93-93f6-d3b16727a799 | -7.19846 | -45.34474 | 2025-09-25 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c98ea53-453c-380b-9b5c-4da3564cef85 | -5.7631 | -42.56685 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3baea8ed-633f-3993-ac47-9603b6e2c9c9 | -6.06629 | -43.57772 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aff329e3-6a90-3567-8ea3-46fb5374cee2 | -6.56501 | -42.06694 | 2025-09-25 04:32:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6a2529a3-fabb-3abb-90d9-bb679442f0df | -6.73214 | -43.9743 | 2025-09-25 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4821dd7-3d98-3e5e-bef1-8a6d3bb4c8aa | -7.28382 | -42.98559 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b9e8d804-d9e3-3af2-b56f-b89a2caf5f4d | -5.16231 | -42.71313 | 2025-09-25 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a13682a0-326e-33e3-a999-e429384f5057 | -2.63863 | -48.04441 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecb8d6e8-4888-3d29-ba56-3f805d595175 | -4.56854 | -48.02205 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0a79e1-ff54-30aa-b2c5-28023af789e4 | -2.19587 | -54.46418 | 2025-09-25 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README16.md)
