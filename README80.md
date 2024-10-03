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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be9f4d9e-b062-3b62-b75b-ba58c842ac5f | -6.67696 | -44.52705 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 786623d6-56f8-3f27-8a2e-6c054ff902b5 | -6.6764 | -44.5307 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74833209-462e-39d1-b404-dd0f6264ffa2 | -6.67301 | -44.53017 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 301d1c09-d1e1-37c9-8340-af176d4b294d | -6.67245 | -44.53381 | 2024-10-03 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30d2dbca-5e8e-3509-9151-d80482691a14 | -6.66241 | -44.04295 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5135d3e-3c6f-3055-a619-a30c9cb5d9f0 | -6.62511 | -44.19683 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85454af5-8234-31bd-9776-b7e3b1dc724a | -6.62168 | -44.19627 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe05411b-d8c3-35df-931b-212431db5b5e | -6.58186 | -44.22855 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c050231f-9319-368a-9e74-d80168c2b9e8 | -6.58129 | -44.23229 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a358b593-47dd-306b-9f29-61c544e089cc | -6.57842 | -44.22812 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c281d12-75fe-3323-a1b2-c646bee95d77 | -6.57649 | -44.65459 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 133a216a-0b2a-304b-90e3-55cda52abfa6 | -6.55101 | -44.08479 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d8cfeaf-58f0-3324-a695-e7fdffc43585 | -6.54814 | -44.08043 | 2024-10-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9ac2825-03d9-3042-95d2-b208c4de56a8 | -6.54288 | -44.71622 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88731b3e-9401-3924-9a8c-e55b168bfa3c | -6.54233 | -44.71984 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a90c4c-a08f-39eb-8c8f-32b35e4ccafc | -6.52327 | -45.11268 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9bbcfc7-32b1-3b1e-9946-a97f4c1bef9f | -6.5221 | -44.50384 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55d030e3-6b0e-302a-ada2-86b301d01ece | -6.52153 | -44.50752 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8388d24d-0cd0-3fd6-83f8-d8c669a25b8c | -7.42546 | -45.24052 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08d1aafb-ede3-32b4-824d-0a48c90fa18c | -7.42266 | -45.23645 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b35b927-c395-33ba-848c-66a2313aee5f | -7.41987 | -45.23238 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dadb3c4-d94e-3a08-bf72-68a15aa722f9 | -7.41932 | -45.23594 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19976476-358d-3a33-84d4-c8f65e88b9ed | -3.61088 | -44.78908 | 2024-10-03 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c734800b-8f7e-3d38-9bcc-fe1b69efdcd0 | -3.61034 | -44.79256 | 2024-10-03 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf90b7ab-8c9a-3006-b5a7-3779033f638d | -3.60756 | -44.78857 | 2024-10-03 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cad8fd1a-9d94-3396-9903-2acb307e05ee | -3.60702 | -44.79205 | 2024-10-03 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17ba94a3-08cf-3106-8214-d959807a4f62 | -2.62519 | -44.32469 | 2024-10-03 04:25:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 881d694b-4bda-306d-8de6-c2785321fa3d | -2.62186 | -44.32417 | 2024-10-03 04:25:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 735cb203-0b7e-3800-be49-4ebdd5a9b06a | -4.89851 | -45.73756 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c54e8b96-7633-3f5b-aa04-667b49d21b91 | -4.85583 | -45.79423 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9375339a-0af9-39f5-b6e9-065e22aa5262 | -4.85254 | -45.79372 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bda2f252-a220-3eaa-b68c-2c24d0050a35 | -4.78258 | -45.95515 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4069be96-19b6-307c-9ad6-d5fa3460e3ff | -4.78036 | -45.94778 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5b50045-4e9e-3d53-83d9-2d578a1bdd57 | -4.77982 | -45.95121 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68648cb7-0cf7-3ccb-991d-354a1bf4d6f0 | -4.68438 | -45.88647 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d822d3f-927e-3f3f-a21b-aac57a2458c0 | -4.68385 | -45.88991 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 675c9441-d184-3be2-bc7b-e6b73786288f | -4.68055 | -45.88939 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3bddda17-ab6d-3577-9f3b-029a2cef438f | -4.67779 | -45.88544 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 84a82646-6527-3926-929d-fe8f7cbf90fc | -4.67449 | -45.88493 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 1f195146-b1ff-3c77-a7c2-1ecb36e18d7b | -4.67173 | -45.88099 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fdcda743-4c74-3e4e-b7f4-2289462ac01c | -4.6712 | -45.88442 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3fab7fe3-8ae8-3c0f-b740-276ae586f89b | -4.66844 | -45.88047 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fc1175-6773-32a8-bf26-b19b665e9b5f | -4.6679 | -45.88391 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f668919-dec9-32bb-af90-eadeb79a4727 | -4.47315 | -45.93074 | 2024-10-03 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b486ae32-663a-314c-8ee8-071f6a2eff26 | -4.46986 | -45.93023 | 2024-10-03 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2932bae6-6836-341c-ba71-b4b0b135c9c5 | -5.1034 | -46.16448 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abe515c6-b889-3bf4-a083-b1575ca7d822 | -5.09267 | -46.06073 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f82bd583-5a4b-3eb2-a3cc-a2322b7bed1e | -5.09213 | -46.06417 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7389343e-9e1a-39ec-a46b-2a4511f7d437 | -5.09063 | -46.11671 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 092b161d-8924-3b8b-9d7f-5899261213b0 | -5.09009 | -46.12014 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf0ce4cc-9250-3938-bc8d-53e86f320b89 | -5.08734 | -46.1162 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829211a1-a097-3836-85a2-3cb862ecaede | -5.08679 | -46.11963 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5be8928-9533-3f8d-b4b5-50ec59bcbc5a | -5.08625 | -46.12308 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d728f5bb-a33e-398e-8242-1047805e7db1 | -5.04629 | -45.81336 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a98fa7bd-8355-3048-9ffd-68afd7593b0d | -5.04354 | -45.80941 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31dc2328-8c10-383d-a389-364fdafff836 | -5.043 | -45.81285 | 2024-10-03 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8bd991a-8a2b-3e5b-8ed6-9d6683b011b8 | -6.47848 | -46.07938 | 2024-10-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acbeb4e4-c234-323d-9cb5-081988adc7e8 | -6.47176 | -46.03596 | 2024-10-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adb63fa0-0d07-35b1-a83f-ca57518167d9 | -6.46846 | -46.03545 | 2024-10-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 774756ec-a61d-383b-8ffc-d0086172d45e | -6.35621 | -46.5085 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 655fbe8c-8513-367b-94a2-b570c8fca997 | -6.35463 | -46.30351 | 2024-10-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f99e0b75-7bc9-3b58-bec3-ee021600f974 | -5.97904 | -45.37638 | 2024-10-03 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd459bd-5e12-3cbb-9021-1b421234ff80 | -5.96902 | -46.29168 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2795790-9d73-3cb7-9557-0b9e194063c8 | -5.85102 | -46.23718 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22b4d258-15d6-3b11-a693-eab746e7e50a | -5.84772 | -46.23666 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95011858-82f4-3f37-88d5-f4a9ec12d761 | -5.79712 | -46.451 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a06f7e68-bfbb-31f8-8b3f-1b901ed91237 | -5.78088 | -46.10283 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7675532-6b37-30e9-a5e3-d096268123cd | -5.78034 | -46.10627 | 2024-10-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98abf81e-784b-3740-9c67-010b36f0cd6a | -5.59831 | -46.37323 | 2024-10-03 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8152c16-283b-3a6e-a7b6-fa60fb99b4d4 | -5.40111 | -45.08918 | 2024-10-03 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ca2ea89-e59c-357a-9c4d-7a32af5cbab3 | -7.61983 | -45.52095 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f237ee0c-1779-336b-8be7-49e414df00e0 | -7.60596 | -45.52245 | 2024-10-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8e885c5-51bb-3d27-bec7-0a9f7fb1bd2f | -6.48345 | -46.48269 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b099e205-a3ae-3cec-97d4-04124d539c22 | -6.48124 | -46.47528 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ea181d1-408a-359a-895a-8e0c821a7c0d | -6.48069 | -46.47873 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62c08e04-3e47-36e6-9039-7a5524544b8a | -6.42647 | -46.62563 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b9f3dcd-551d-33ca-96f1-6ec1c29abcbb | -6.66649 | -45.32966 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7fda67f7-a5e2-3603-b73d-addcf4c334ab | -6.66595 | -45.33316 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9fbe31ca-5a86-3368-a76f-66f25a54566a | -6.66316 | -45.32916 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dd4d40d4-274e-3fa3-84c2-5555fb89d823 | -6.66262 | -45.33266 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba3f30f8-a026-3383-bd29-4ccd0aec6936 | -6.65983 | -45.32865 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a368136-a380-36a8-8308-813e5a337d20 | -6.65929 | -45.33216 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9044f5f-4f9e-34bf-b63c-14b80789718b | -6.65875 | -45.33566 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8669fb99-13c0-3768-9f01-56c654f3d9df | -6.65596 | -45.33165 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0243ef23-5976-396d-9600-4a0cdf6321dc | -6.64731 | -45.32325 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e482607-e5b7-3f2e-88e8-aa776176e420 | -6.64676 | -45.32676 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4749bc22-1b59-35cb-8e0c-ea9a54f78b84 | -6.64343 | -45.32625 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40fc6faf-bc87-3eeb-b850-1e4b78690088 | -6.6401 | -45.32574 | 2024-10-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e091fce-e73a-35d7-88a2-2b42c905e587 | -7.40626 | -45.69289 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d2f9126-95ff-3407-8df2-a0d85ed11b9d | -7.37595 | -45.88815 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00a4e4e5-491f-3abd-80ba-000f26c4c9fe | -7.34718 | -45.85517 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b0d6922-4728-3efa-b6fe-cbd50191e305 | -7.34387 | -45.85466 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1f8f76e-2a53-3f25-937c-c10f5469179f | -7.268 | -46.0556 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3802ba05-979d-332f-ae30-2805b5d5d8e7 | -7.26746 | -46.05907 | 2024-10-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9faef4e7-fa5c-32f0-9b89-5ffcb1b97671 | -7.23482 | -45.52602 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2252ff7-d5a3-32be-b0c3-0d383f1226fc | -7.2315 | -45.52549 | 2024-10-03 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81b59ec6-d9a0-3311-b9fd-e9cd72277e63 | -7.21193 | -46.67706 | 2024-10-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ecd03d1-634a-3d04-8820-d9ffa4d33d16 | -7.21138 | -46.68052 | 2024-10-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d168d65-b124-3fb4-8485-dcc76a4ebfaf | -7.21084 | -46.68398 | 2024-10-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20f93d47-23ec-3226-b8e8-d235b5c6fc24 | -7.20754 | -46.68346 | 2024-10-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README81.md)
