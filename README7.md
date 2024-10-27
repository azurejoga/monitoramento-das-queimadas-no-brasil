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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4922777-b9ce-396e-802e-eee7409bb656 | -5.1099 | -44.7262 | 2024-10-27 00:14:00 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8653c51-fe71-3e16-ba32-22e918d85541 | -4.0625 | -40.469101 | 2024-10-27 00:14:01 | METOP-B | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f538eff-5168-3414-96c3-86e451e5d97b | -4.0644 | -40.477402 | 2024-10-27 00:14:01 | METOP-B | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| dd3d8238-1da2-3e17-aca2-636b7723e0bd | -5.5461 | -46.976501 | 2024-10-27 00:14:01 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2c4c3f6-e65f-30ae-9ba2-363c96820329 | -5.548 | -46.985298 | 2024-10-27 00:14:01 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 570cb154-7735-3131-825c-ce60f227f0a7 | -4.9833 | -44.481899 | 2024-10-27 00:14:01 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdb29e83-1f50-38a2-b47c-58a31cde5b26 | -4.9735 | -44.4841 | 2024-10-27 00:14:01 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5a3b096-8063-3e26-b5b3-c0f53f726549 | -5.1955 | -45.526699 | 2024-10-27 00:14:01 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 025c16da-a4bb-38e5-afc0-ed50db99af51 | -5.1971 | -45.534199 | 2024-10-27 00:14:01 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7f0bb9-66e0-3701-8935-685bf0257b08 | -4.4274 | -42.517601 | 2024-10-27 00:14:03 | METOP-B | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2deb4c43-031b-3d96-a60f-1ec60a2ac4b8 | -4.416 | -42.512798 | 2024-10-27 00:14:03 | METOP-B | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0fa991e9-31a3-30d6-b163-b25dc231eed5 | -4.4176 | -42.519798 | 2024-10-27 00:14:03 | METOP-B | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7bb4fee3-937f-3354-a4e2-7fe4993f03c4 | -4.7022 | -43.8713 | 2024-10-27 00:14:03 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7449995-8354-3790-9a50-cb934071f7a5 | -5.3931 | -46.793701 | 2024-10-27 00:14:03 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 994ebc93-c201-3866-9a78-fdeb1b756e62 | -5.3949 | -46.802101 | 2024-10-27 00:14:03 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd67318f-4d34-3475-bc50-a3376d0462d3 | -5.3968 | -46.8106 | 2024-10-27 00:14:03 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a668428-6543-33c6-a81b-27030eaad58b | -5.3384 | -46.778801 | 2024-10-27 00:14:03 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b2c8832-7fe2-3c7a-aa3b-23c2e967a434 | -5.3402 | -46.7873 | 2024-10-27 00:14:03 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26f120e8-2446-3a13-ab33-8c54b0219450 | -4.6559 | -43.802601 | 2024-10-27 00:14:04 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c24f47b9-40cf-341f-880d-e08bd6d00fe9 | -5.0057 | -45.413101 | 2024-10-27 00:14:04 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4a5e3a-451b-3052-b505-eb91addf3d4e | -5.0073 | -45.420399 | 2024-10-27 00:14:04 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed5156f-af9f-3fdd-87bb-5a2310f7ccb1 | -5.009 | -45.427799 | 2024-10-27 00:14:04 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e074861-3a6f-3900-a8f6-38360e1d1980 | -5.0205 | -45.5261 | 2024-10-27 00:14:04 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2ea3d33-3090-3ece-8817-d6f6da67f94c | -4.8074 | -44.616001 | 2024-10-27 00:14:04 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db081eb-640a-3abc-9839-d6f0803dae69 | -4.809 | -44.623001 | 2024-10-27 00:14:04 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4e0a2f1-f1a3-3a32-92d2-50099a2dc1d8 | -4.8431 | -44.821999 | 2024-10-27 00:14:04 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 360fb308-0185-3002-a598-8fad6b9ab716 | -4.8447 | -44.829102 | 2024-10-27 00:14:04 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee440403-2cc4-36ba-aff7-b6fd79d923fc | -4.5386 | -43.556198 | 2024-10-27 00:14:05 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bde816f-abbc-32ad-9e40-573de6ea8471 | -4.5401 | -43.563 | 2024-10-27 00:14:05 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5a26a40-dc78-3eb4-9343-d79d95d2c076 | -4.8745 | -45.008801 | 2024-10-27 00:14:05 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e17c8568-6634-3139-b0f2-99d24d7cab54 | -4.8761 | -45.015999 | 2024-10-27 00:14:05 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d574c16b-f81a-3fe5-bbb4-cc68ad7e95a8 | -5.0888 | -46.158901 | 2024-10-27 00:14:05 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d38b70ce-9933-30fc-a248-ce945b7c6eb9 | -4.338 | -43.033001 | 2024-10-27 00:14:06 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff54dad8-001e-3bfc-9ef7-b250876347b3 | -4.7567 | -44.804001 | 2024-10-27 00:14:06 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87449d43-4a69-322a-b179-a460048b90a4 | -4.7583 | -44.8111 | 2024-10-27 00:14:06 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 304c0f0c-e6db-3a86-84b8-a4bc934af436 | -4.9048 | -45.7001 | 2024-10-27 00:14:07 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 80859fc3-bc8f-3ee2-af14-e22654b39ede | -4.3924 | -43.868301 | 2024-10-27 00:14:08 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c790cc27-d66a-35f1-924d-cb9d31c14772 | -4.2117 | -43.614601 | 2024-10-27 00:14:10 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46476242-1dd1-3ac2-81aa-0e3df97fd6d1 | -4.2132 | -43.621399 | 2024-10-27 00:14:10 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bceeab0a-ad76-37a2-a5a0-12e19c20dd40 | -4.7072 | -45.782799 | 2024-10-27 00:14:10 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cae41957-9e4b-3302-8811-f3a50d0d87ec | -3.9104 | -42.374599 | 2024-10-27 00:14:11 | METOP-B | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d65f935f-e9c1-35dd-a769-cd0624b23b3e | -3.912 | -42.381699 | 2024-10-27 00:14:11 | METOP-B | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68b35e25-8d0a-3357-901c-297319acbb40 | -4.579 | -45.391602 | 2024-10-27 00:14:11 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f373f97f-0ba5-30a2-9be7-9c3239f93293 | -4.5806 | -45.398899 | 2024-10-27 00:14:11 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc10a45-c2c8-33e2-8204-21ed2eb1c14d | -4.4412 | -44.866199 | 2024-10-27 00:14:11 | METOP-B | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 711fbcee-9d8d-3194-ad6e-bf3f352083f8 | -4.316 | -44.353199 | 2024-10-27 00:14:11 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8053601d-54d2-302e-87a9-8c81f78ded6a | -4.3175 | -44.3601 | 2024-10-27 00:14:11 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8d54af2-376e-3e7a-9f46-83ee37b4cc59 | -4.4314 | -44.868301 | 2024-10-27 00:14:11 | METOP-B | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 645ef77b-b56d-31fd-bf2a-067ecb3366bf | -4.2757 | -44.311401 | 2024-10-27 00:14:12 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4c6a9c-3656-3709-9bf2-0d6a78034d4d | -4.2773 | -44.318298 | 2024-10-27 00:14:12 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e16b593-2f70-397c-ba4b-d7328f912811 | -4.2788 | -44.325199 | 2024-10-27 00:14:12 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31313bd5-3fc0-30d9-b2f4-64b9a6f137ce | -4.2659 | -44.313599 | 2024-10-27 00:14:12 | METOP-B | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcbb151-01fb-328f-969a-f18d63fc394e | -4.2674 | -44.320499 | 2024-10-27 00:14:12 | METOP-B | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e650e439-6aec-312d-a3c3-e65adb5bd945 | -4.269 | -44.3274 | 2024-10-27 00:14:12 | METOP-B | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec630964-6a69-395e-9041-4752271200c8 | -4.8096 | -46.8494 | 2024-10-27 00:14:12 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a993d747-8206-3a5c-b906-13911f1ae58d | -4.8115 | -46.8578 | 2024-10-27 00:14:12 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24af7b7e-1a08-30cc-a3be-90e040f27d84 | -4.8134 | -46.866299 | 2024-10-27 00:14:12 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae6697fb-a66a-37e8-b428-c620b08be64d | -4.2556 | -44.6353 | 2024-10-27 00:14:13 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfb22950-a5f5-3220-8721-9ce66438db20 | -4.2572 | -44.6423 | 2024-10-27 00:14:13 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5da274ba-4bde-3daf-99e9-fc9c5536c75c | -4.5169 | -45.991402 | 2024-10-27 00:14:14 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e52f8ee-ffb0-3b0d-9387-dde6fba09252 | -4.5186 | -45.9991 | 2024-10-27 00:14:14 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad64e036-87cb-3f03-a9c6-87ec0deadfcd | -4.1106 | -44.218201 | 2024-10-27 00:14:14 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07d0e0b3-b921-3a48-8242-69b8cab0cf8e | -4.1121 | -44.224998 | 2024-10-27 00:14:14 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc3f75a-7834-3507-84b3-f87dff791d54 | -4.4058 | -45.6763 | 2024-10-27 00:14:15 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfed74d8-4f18-3865-842f-5121435cf3ac | -4.425 | -45.947601 | 2024-10-27 00:14:15 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29383536-1e53-3477-8560-802e58ac749e | -4.4267 | -45.9552 | 2024-10-27 00:14:15 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c811595-c957-3326-870f-daa18a84a2f4 | -4.4152 | -45.949799 | 2024-10-27 00:14:15 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8e132a8-d7d9-30cf-8a06-5e633ff94f6b | -4.4169 | -45.957401 | 2024-10-27 00:14:15 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 517abf44-6964-3cfb-afe3-8032c42ebe28 | -4.2749 | -45.5042 | 2024-10-27 00:14:16 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 580ac404-bd4d-3ead-81f8-9f68c16399dd | -4.2765 | -45.5116 | 2024-10-27 00:14:16 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8416f0a-557d-3338-971e-82d273f52481 | -4.3474 | -45.830101 | 2024-10-27 00:14:16 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d08bdfdd-66d9-3035-b516-179144e2f199 | -4.3491 | -45.837601 | 2024-10-27 00:14:16 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38e512e3-3a70-351c-be55-42ae3e43acaa | -4.2651 | -45.506401 | 2024-10-27 00:14:16 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53ef2b64-7395-3389-bde5-3d0a26e97398 | -4.2667 | -45.513699 | 2024-10-27 00:14:16 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7860bb02-d00c-3f5a-aa47-bbfacca6aff8 | -4.1291 | -45.127998 | 2024-10-27 00:14:17 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 747624cf-3c96-3d25-afd8-a8ecd354226f | -4.1307 | -45.135201 | 2024-10-27 00:14:17 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02b400cb-08a7-3c3f-9dd6-62eb225943e6 | -4.1193 | -45.1301 | 2024-10-27 00:14:17 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21ac09b5-ca1d-3691-b32f-8dea65002f84 | -4.1209 | -45.137299 | 2024-10-27 00:14:17 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45dcaa4d-a0c3-3130-b17a-590fec3b9ba3 | -3.949 | -44.232399 | 2024-10-27 00:14:17 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5328012-fe01-3921-b0c6-ac464b96f9f9 | -4.2503 | -45.5788 | 2024-10-27 00:14:17 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3367da5-4f04-3038-a86e-f13c9db89fec | -4.2519 | -45.586201 | 2024-10-27 00:14:17 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 083842e0-2ab0-3630-8360-03846115ebed | -4.2208 | -45.539101 | 2024-10-27 00:14:17 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65a7a65e-13c1-3e9d-9477-692b4f8e52e2 | -4.0087 | -44.8657 | 2024-10-27 00:14:18 | METOP-B | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| debf4303-875c-3c97-9d19-ad3594dc0c02 | -4.3555 | -47.072201 | 2024-10-27 00:14:20 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 953d9fe3-96e2-3927-bd17-5046046ec4ec | -4.064 | -45.527599 | 2024-10-27 00:14:20 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed050cc-3907-3a50-9bf2-9c62ec9c1daf | -4.0656 | -45.534901 | 2024-10-27 00:14:20 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e922d8b1-368e-31b8-8b7c-1f814fd38385 | -3.7569 | -44.202999 | 2024-10-27 00:14:20 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a0fc66b-9d72-3bf8-8c5c-ba97baa461ee | -3.8627 | -44.7659 | 2024-10-27 00:14:20 | METOP-B | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba0a0134-2ebc-3357-b085-a83be2a9778b | -3.8643 | -44.7729 | 2024-10-27 00:14:20 | METOP-B | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 404b8807-7400-336a-afeb-a5f8a2a60503 | -3.9536 | -45.264 | 2024-10-27 00:14:20 | METOP-B | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e69fd9f-2353-3747-846e-2de14d83d34c | -3.9552 | -45.271099 | 2024-10-27 00:14:20 | METOP-B | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81901960-d855-3cf2-8022-775bd617dd5b | -3.685 | -44.341202 | 2024-10-27 00:14:21 | METOP-B | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e54520d6-df25-35a1-aba4-f36e8afbd303 | -3.6865 | -44.348099 | 2024-10-27 00:14:21 | METOP-B | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b71499a3-7e39-3449-9730-cdda6dd978b7 | -3.8549 | -45.098999 | 2024-10-27 00:14:21 | METOP-B | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b23b3a6-a6d2-37a5-939a-9f02acb8e115 | -3.8565 | -45.106098 | 2024-10-27 00:14:21 | METOP-B | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd98c5bf-aa34-3fe4-b24e-4f23a076168e | -4.0587 | -46.011902 | 2024-10-27 00:14:21 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34c4fde3-a38f-3805-b77c-23a9f9e04bbb | -3.422 | -43.402901 | 2024-10-27 00:14:22 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f801a279-d1f1-3207-a949-9079fd7aeaf1 | -3.7164 | -44.572601 | 2024-10-27 00:14:22 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b03875a-d4ac-3d29-8ded-bb4d9a495796 | -3.7179 | -44.579498 | 2024-10-27 00:14:22 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd4e4e7-9727-3708-9b4c-964f358be15d | -3.3708 | -43.313599 | 2024-10-27 00:14:23 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
