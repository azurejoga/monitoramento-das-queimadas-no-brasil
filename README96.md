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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c36235-3984-36c7-8646-f7befa12b24a | -8.0988 | -45.3371 | 2025-09-06 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 7bfb11fa-0afa-3855-bfb4-6d48e78773d2 | -6.267 | -53.4582 | 2025-09-06 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 062bebe2-2fd3-3b2c-ac5d-1097c2d24a21 | -15.3258 | -52.7182 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d347a12f-de7e-3b54-b794-d86b0b29e42d | -6.1944 | -53.2585 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 8e6cbf95-d7f7-37ae-bb38-140dc6800c6d | -6.6954 | -44.829 | 2025-09-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 623c6482-a1fe-3f77-9316-187dab9af64d | -16.307 | -58.1055 | 2025-09-06 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| a9b923f6-96ed-37b9-b844-991a7b8cb61d | -6.1848 | -43.3724 | 2025-09-06 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 29c592c8-151d-347d-9216-7ed85d185698 | -11.0245 | -45.9502 | 2025-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| f0c4dcb0-7348-3aa6-9a6a-36d92abd1577 | -5.4579 | -42.8911 | 2025-09-06 14:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 34e12113-12be-3d5b-b28e-85a8c43e52db | -9.9785 | -51.6436 | 2025-09-06 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e770a891-77ff-3b7b-9ba7-530e22d588c2 | -15.7182 | -53.5954 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 6d3448bc-9fae-3f6a-82e6-da534b6d5eba | -13.0047 | -54.8076 | 2025-09-06 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 441a2bff-56e5-358a-8303-56d96270ab8c | -13.8403 | -46.2828 | 2025-09-06 14:20:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 04b2258c-1db8-326a-bb28-c21563432db3 | -6.4021 | -46.0944 | 2025-09-06 14:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 17739345-893a-3aea-8416-a23c7434f623 | -13.3003 | -51.6436 | 2025-09-06 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2a5dba72-fa85-36c1-be9f-d0979042c200 | -6.7419 | -51.975 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f67412a2-cb61-3a9f-b3a5-f0f4449373f0 | -10.2373 | -50.5417 | 2025-09-06 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8b22b636-f2d5-3019-b394-085b83763ae3 | -6.5138 | -42.4266 | 2025-09-06 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| a6d8da86-a4ee-3230-a40b-ea1c9d75644c | -7.0132 | -44.9385 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e71e77fb-c336-3c2d-afac-defe00365d7e | -10.2184 | -50.5436 | 2025-09-06 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7aaca0ee-ed41-3fcd-821d-cbab2382d9c0 | -8.0223 | -45.4354 | 2025-09-06 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 70351c90-8807-307c-9388-d8b41edc2fad | -7.8593 | -44.9053 | 2025-09-06 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b4974b68-64f4-3c76-b8bf-dd2c98898a44 | -7.6881 | -50.2991 | 2025-09-06 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 56012f04-e11f-3862-9206-99c56a7c08da | -13.8597 | -46.2796 | 2025-09-06 14:20:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 06a066fe-3495-3def-8caa-82d097257e6c | -10.1453 | -55.1674 | 2025-09-06 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 23cd63f6-b82e-3aff-9eaa-cb9a342cab1c | -8.4828 | -62.7116 | 2025-09-06 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9aa14077-e10e-3f88-9a75-25d9dfda3b19 | -8.099 | -45.3144 | 2025-09-06 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f0991386-5f33-335e-8fda-5b96c5f0a2a6 | -15.3067 | -52.6995 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 256.4 |
| 1800f613-107f-3055-9a93-0891e0964877 | -6.2418 | -43.2976 | 2025-09-06 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5c601ba3-7d72-3436-96c6-6c61793db963 | -5.7504 | -43.7091 | 2025-09-06 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c34108fe-f8c5-35ff-9703-879b3b875158 | -15.7381 | -53.5717 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 4b41dd4c-6f3b-3aae-bcc4-8eed547c04cf | -9.3753 | -62.3518 | 2025-09-06 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 452b0556-d4f9-3b75-a723-5b30798dce70 | -6.0948 | -44.9455 | 2025-09-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7ade0ef8-7482-3f8d-ab7a-9b86593b55ee | -13.8006 | -52.7454 | 2025-09-06 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 5a85ac34-2d9f-3090-aef0-7030181ab54d | -15.719 | -53.5532 | 2025-09-06 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 822b06fe-c8ff-3a6d-8403-411a96d69fd8 | -9.4623 | -60.5104 | 2025-09-06 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8d31fae0-cea2-3acf-be28-011941a4396a | -6.2296 | -42.641 | 2025-09-06 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| e90ddf3e-dd99-39f9-8e7a-857dd19444b5 | -11.2651 | -46.3938 | 2025-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| bee00889-009d-3011-80f2-432275c3dd9c | -6.8465 | -52.8337 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b46bc8db-5681-3194-8562-caee2e70219a | -8.4323 | -47.3191 | 2025-09-06 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6b69b433-fbff-37b8-8bbe-4b7edb414be1 | -7.0129 | -44.9613 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 378.3 |
| f875caa4-6c3d-3621-8a04-90482e5edb8b | -5.7183 | -45.2226 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f891ddfa-0f6f-3413-b63d-b4630a944f8b | -6.0043 | -46.7018 | 2025-09-06 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 62ed9b1c-bb06-3f43-9c9e-cd62a107336b | -13.0353 | -48.0521 | 2025-09-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8047f163-5145-37cc-b483-70a50592fff2 | -5.8877 | -45.0972 | 2025-09-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 6bafa6bc-2e6f-3c0a-b08e-86fd1de210ba | -8.8658 | -47.2545 | 2025-09-06 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 4a43c896-c292-3552-a0b3-f30e3b864de4 | -9.4495 | -62.3675 | 2025-09-06 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 279617c3-db06-300b-bba2-8b9af89735c4 | -5.7298 | -43.9189 | 2025-09-06 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 307.6 |
| d7d3e96c-f6e7-3f90-8563-96f7c62e2621 | -3.3442 | -42.994 | 2025-09-06 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0e779ff9-2d5e-311f-8ea2-94bd7179ffdd | -12.8636 | -47.9877 | 2025-09-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 58d54a3e-49e1-38fc-b446-35a7d6d5c2ef | -13.3195 | -51.6413 | 2025-09-06 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 6c771c22-1423-3825-aede-6cd42d5f1401 | -13.5732 | -48.1068 | 2025-09-06 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 755d7d87-8485-3d13-8d0f-a61de69cffd3 | -8.1179 | -45.3125 | 2025-09-06 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f025f75c-e538-34f3-8c40-9a6e5bd8b9b1 | -9.4497 | -62.3485 | 2025-09-06 14:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5015f63d-332a-3f96-9e54-aaed88613003 | -16.3345 | -52.9387 | 2025-09-06 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 15a0ad4c-bb43-3200-a02d-b5484e849aa3 | -5.5697 | -45.1198 | 2025-09-06 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7ad54c6b-c271-396b-b4da-fe16370fe2bf | -7.3838 | -50.9116 | 2025-09-06 14:20:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 221ba4b6-cf92-359c-b07b-a99f50e61d01 | -14.8297 | -48.1784 | 2025-09-06 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 24f104cc-e531-3434-a066-2a65aef2f6c3 | -5.641 | -45.5214 | 2025-09-06 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7873b1fd-fb84-3c87-a9a9-22d7d92f0ebf | -10.5937 | -44.331 | 2025-09-06 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8bf5e2e4-0f10-3975-8de5-4b4e9f60ba85 | -6.8466 | -52.8132 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5bc64e75-84e9-30e4-b375-2deff4806a37 | -6.1945 | -53.2381 | 2025-09-06 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 91e26026-b546-316b-af00-272849763892 | -13.0044 | -54.8282 | 2025-09-06 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| b9d5cf72-4b78-3cdb-bab0-251765b691d3 | -4.8011 | -43.054 | 2025-09-06 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e3732e3b-5180-348e-846e-f183654d0d3d | -11.2295 | -46.2403 | 2025-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 0c5ad30e-ab99-39ff-a617-7d9bfc017c90 | -6.2672 | -53.4379 | 2025-09-06 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 21e08bf1-735a-3295-9929-23ad1c91e29e | -4.4568 | -44.1413 | 2025-09-06 14:20:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 512.2 |
| eda5e0b6-3c58-3321-92b3-270a0ec5ddad | -6.2034 | -43.3942 | 2025-09-06 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b6238356-e9e1-35a3-bcd5-443a1475b551 | -6.2301 | -42.5937 | 2025-09-06 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| a2e6ab93-8657-35ce-903d-2fcc2bc94fa7 | -9.4621 | -60.5297 | 2025-09-06 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0a955c1d-568f-3bb0-a36f-c8d3475302fa | -5.8877 | -45.0972 | 2025-09-06 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 1fc40c6d-0f35-30ba-ab8f-7aa640c9faa2 | -10.3324 | -46.445 | 2025-09-06 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 01cf5f66-2878-3c6d-ae9d-c0c30a75c438 | -13.0047 | -54.8076 | 2025-09-06 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 07dddd04-a012-3680-ba04-6828784f9a38 | -10.5937 | -44.331 | 2025-09-06 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ef5bada9-800b-33fa-9e31-0b45b369de5a | -9.4623 | -60.5104 | 2025-09-06 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1fa3e71b-7219-3371-9073-b601236960a9 | -7.0129 | -44.9613 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 07cd96ba-f3ed-3536-8dab-e8c688e20bd2 | -6.1679 | -43.1869 | 2025-09-06 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 62.2 |
| c5a429c0-62b9-3757-906f-2d955b814072 | -6.8095 | -52.8154 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| d0098704-956b-376d-bba2-3c9c64f4dc34 | -4.8011 | -43.054 | 2025-09-06 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 92f6aa23-de9c-33fc-ba88-5451a71b5170 | -7.9252 | -63.2608 | 2025-09-06 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| dbf72f3d-2892-364a-b255-13fc918ab703 | -15.7182 | -53.5954 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 50611502-0e95-3a30-b665-1ee58588c076 | -15.7381 | -53.5717 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 43f5c150-f13f-3445-ab3f-7a4631f6298f | -6.7233 | -51.9762 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| fa2bbac0-3334-3075-9d37-8829d9128be3 | -13.3195 | -51.6413 | 2025-09-06 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 303935d5-3ab3-363e-8cfd-0610372071b9 | -11.0051 | -45.9755 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 4741bed8-46b2-3dcd-b3e1-bb63b5da521d | -13.0044 | -54.8282 | 2025-09-06 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 7eb5ceb9-eedf-31c0-99dd-e02d0b91fb75 | -6.2672 | -53.4379 | 2025-09-06 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a250aec8-4d5c-302a-99a8-e91674b74f5e | -15.6991 | -53.5769 | 2025-09-06 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| bd76b34c-3697-3da4-a1f3-b105ee2768e6 | -5.5697 | -45.1198 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0252ebdb-c2b5-3c9a-b817-bb1ee9132891 | -7.0132 | -44.9385 | 2025-09-06 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b8139556-c6c8-3bc4-b438-a98ca7e4a66f | -7.6505 | -46.7268 | 2025-09-06 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 000333a0-b397-3eba-adaf-394280b1382f | -9.0781 | -62.3458 | 2025-09-06 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4ca5bc1d-71c6-3e47-998f-2e91a8b7eae5 | -14.4359 | -48.4644 | 2025-09-06 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1c02ff18-a9d7-3b41-ae16-ee9d32db9090 | -7.8593 | -44.9053 | 2025-09-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 77dd99bb-78c9-3c44-ac6b-e4e4b951a453 | -7.3838 | -50.9116 | 2025-09-06 14:30:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 47b09d64-0da8-31f6-8bdf-c66ed974498a | -11.0242 | -45.9729 | 2025-09-06 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 370dd0ac-7b18-3683-a82a-c95da35e35a2 | -12.272 | -50.1872 | 2025-09-06 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 66c8e963-1518-3d23-96af-f2180cce9a22 | -12.8636 | -47.9877 | 2025-09-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 72c548d0-bf92-39a1-a942-89412b8214fc | -5.73 | -43.8958 | 2025-09-06 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 17195504-03a5-3dfc-acb5-f5daf3294802 | -15.3064 | -52.7208 | 2025-09-06 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 234.7 |


[Clique aqui para ver as próximas entradas](README97.md)
