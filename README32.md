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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88a5027e-5455-3a61-96d1-eb30a434c2e1 | -8.28379 | -45.41075 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da21efe3-ae40-319c-851d-c9d2bb950022 | -7.71017 | -44.93833 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d195afc-f295-3b21-af55-e65d5afbd3db | -9.82884 | -44.94009 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54d0beac-7011-3e4f-a220-10dab7324769 | -12.51127 | -49.97308 | 2026-09-28 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b17e40f7-9cdc-3aa3-b98d-f5703c4e77bf | -8.6599 | -45.41689 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b670b57-c33c-36d6-8e49-fbbdb7b5f3c2 | -7.88769 | -45.44859 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5abef8c2-3a82-3c4d-bb4d-e2bc2f333dcb | -10.12601 | -45.1351 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a24d20b7-0704-3409-be00-35e0b2bbfbf3 | -11.05528 | -54.19689 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f8540df-fe22-362f-85f9-3b3b16f8797b | -10.11331 | -43.94124 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aabc978c-5c42-3f78-a36f-0f55a18ed34f | -11.10689 | -51.32902 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fc0ac91-94b9-3964-b6fc-494029a1ebf0 | -10.92932 | -50.66941 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47db3769-261e-3ab9-b03d-e81c9f065e1e | -6.0968 | -57.6262 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dea115c6-8d14-3fde-b7db-898f67f91209 | -12.72978 | -47.28727 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d6c3362-a77e-3e58-b01d-7270e8d96b4f | -11.40318 | -45.37378 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531b8e78-f01e-3737-b873-74bb31b1c9d7 | -7.71119 | -39.3469 | 2026-09-28 04:34:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24d98c97-633e-3869-8985-56195a770651 | -7.38088 | -42.11529 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 04dd160d-7d37-380f-ae23-b600121707eb | -12.65913 | -47.3167 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f93bb601-447e-3cfb-bf75-b4056160d9ac | -11.20868 | -44.7819 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5d6872a-6a96-3e23-a899-da164a55754b | -10.38024 | -44.97737 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2016b593-ebcc-3952-8093-15719e28af86 | -7.71144 | -44.92977 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 940f8f9a-9c90-3652-aa23-ae8a27cbdbc7 | -11.10468 | -51.32077 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 405132a0-44a5-36cf-99e9-61e5efbb850c | -8.28284 | -54.71384 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b11dde7-9c3c-37b6-9d60-fb6c1d4d14f1 | -11.18735 | -44.79389 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 0bb3ad0d-1c45-3fe7-b994-6182cba51134 | -9.77606 | -48.21172 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be35a26f-a053-3a98-a077-ad7f08621544 | -8.65781 | -45.41903 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e371ea5f-0b79-364c-b3bf-a0c5a3a51894 | -10.00509 | -50.12807 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6cbb4ec-9fcd-36f3-9bc4-bffb2c23eedb | -6.09618 | -57.62976 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ad7454a-e0df-3c7a-ad0f-c926150074ce | -13.08754 | -48.55925 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065e3a83-7af3-3e9b-9821-239f6618e15e | -11.70336 | -44.54233 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc156e34-422b-3bb2-869d-786bf5d871c0 | -11.44763 | -44.91706 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cb57aba-38d5-3b08-bcf3-dde4358216a0 | -9.94083 | -50.23594 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2b75786-e1df-3b16-9c56-9d166828551f | -11.3528 | -47.43037 | 2026-09-28 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81f27dd5-b8af-366c-80cd-135e3db16e68 | -6.09131 | -57.6253 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61447194-0dc3-3e95-b1d5-a859814070e4 | -6.666 | -55.10358 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5094a9b1-5d14-335b-8d4d-d591c83ab520 | -10.2078 | -49.99243 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1da79e25-7890-31b9-ae11-aa18b56060a7 | -11.12896 | -50.06257 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dfd22ea7-7106-3a0f-8b5d-4b32f751faa0 | -8.10387 | -44.00432 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8629ac0f-a3d0-3ff2-951d-5ce7e68dacc6 | -13.08205 | -47.44159 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 247166e1-6dc2-3597-b803-4de6d7a66114 | -10.42481 | -53.82486 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5030ec8d-649e-3cc6-9121-cb8d3056e020 | -9.08054 | -43.13124 | 2026-09-28 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c69e88f2-e104-391b-a97d-e68bb6312c9a | -7.71466 | -44.90809 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90427117-0a41-3162-ba9e-0ab7da13667d | -8.65429 | -45.35604 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b2b854-0ec0-3820-9b58-71fa0ec5be16 | -10.82384 | -60.74575 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8f16988f-bfe6-30eb-80e6-99a950559b2f | -8.36663 | -45.46026 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f33a908-93ca-354b-b791-e6f18cae599c | -10.21114 | -49.99297 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae142ca-f78b-3d16-a5ab-6d3044817946 | -6.66245 | -55.09571 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47fcf4fd-b435-38c3-ab81-166cf8f5dcb7 | -6.66224 | -55.09814 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3a8aef0-9482-350d-91b0-aed953e5a7c5 | -7.70716 | -44.9335 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3025fa44-c5ae-3140-bdae-da0b065c6987 | -12.69021 | -46.98344 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c9219f4c-b786-3660-9b60-3c3d42130fbd | -8.10315 | -44.00923 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 273a545c-ad70-3454-843c-6170f442880a | -9.16639 | -47.97559 | 2026-09-28 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62bc24b5-149c-3190-97d6-9a534f54f073 | -8.10119 | -44.00567 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b117ead3-5bd8-3b3c-a4db-38110b1ded80 | -7.38267 | -42.10286 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bc20ef8c-8b37-39b1-8bcd-0e45c7f557a5 | -12.10927 | -45.21768 | 2026-09-28 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 04549049-79ea-3b69-9ec4-ef2f83877901 | -7.51853 | -46.61108 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be6d5c00-f4ad-3b04-9b80-ca2c33a8e40c | -11.43583 | -47.41634 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68208194-efd9-35c5-9979-24137d525be4 | -9.82461 | -45.2599 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de7f141f-0e81-3326-862b-978c0c52f084 | -8.66562 | -45.41586 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11efdb69-b523-33fc-b493-a4758ffb2346 | -6.07707 | -57.80541 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ee81fc0-206f-3d3e-a968-8c244b579d9a | -8.96733 | -50.98058 | 2026-09-28 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c36206-1783-37e5-9666-d198979c2fce | -8.89896 | -46.19217 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| addd6fd9-991a-31e9-b827-175f8ecadf9d | -9.68264 | -49.28917 | 2026-09-28 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72c5b256-d12b-3cf5-b93c-84829a5cadaa | -7.45105 | -44.59271 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c42ef0-e55f-3802-b3bc-42c8974bb301 | -7.70652 | -44.93778 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dfa8fb15-9023-3286-8a4c-3ffcfbfc1ea4 | -10.92297 | -50.6872 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f699670c-e626-313d-864d-c2db63855c1c | -10.00116 | -50.13112 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7514ccff-266d-39d5-9ee5-8f5b2616e167 | -13.07518 | -47.4405 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b0ff9f4-23d7-3f32-ad9f-ac0c74a72f29 | -6.70871 | -45.60997 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bdec59c-e521-3289-aaf2-0dbef3d041ee | -6.92703 | -46.50732 | 2026-09-28 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c18146e2-04eb-38a7-a6a2-d21e482cfeff | -9.77752 | -44.83621 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a1c07b5-dba5-3faf-b8dd-779f4c8ce459 | -7.81957 | -55.14342 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05b7b21f-cec9-3ee7-8e38-c85d20062f84 | -11.54737 | -50.51328 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0011a889-05db-3db8-b79b-fc48fb505772 | -6.22211 | -47.44311 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c677f7a-bafd-3631-8328-424efe803dfc | -11.9028 | -47.00442 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f79cc3a9-f8ac-37a1-9ed8-f29423ac6d7e | -11.37705 | -47.43081 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec6391a3-1617-356a-8850-e9ee8cdcb762 | -10.63012 | -46.32792 | 2026-09-28 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| feb1c2e5-2b01-363b-aebc-97a835994448 | -8.28357 | -54.70966 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e520d3c9-a877-3d3b-9e2e-5b61508d89a0 | -11.70617 | -44.54933 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8de1a0ea-6b58-3964-af29-5a763ba3d4cf | -6.06267 | -57.82241 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eff6c526-9516-309c-a06a-74d3a718146c | -9.47049 | -46.4063 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f75920-4536-3e6b-a0b8-4b5152d69516 | -10.94282 | -50.67163 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 605b1415-356c-34eb-aa6c-a916300ece63 | -9.83258 | -44.94069 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aeb604c-c7e4-388d-901e-4d8411ff5f27 | -13.39116 | -44.36623 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f23b9a02-60f3-338a-9cf6-0aa4259541ae | -11.19298 | -44.8096 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b624c8c3-85a1-39bb-b675-b09e5c34ec92 | -7.62662 | -45.52275 | 2026-09-28 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63b4dd2f-472f-3f7a-bac2-56f4d7109c2d | -11.78638 | -48.3364 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8df9d44c-39dc-34df-a63f-a45d8a3c58a7 | -12.70181 | -46.97728 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6654ea4f-69ca-3568-8cae-65e94cb30f45 | -12.69888 | -46.97292 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeba1384-8721-3240-815a-ea5617c84377 | -8.10775 | -44.00488 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e161aea-650f-3f92-bb0d-1c647a635bad | -10.12168 | -45.13884 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f31708b3-39d2-3397-9ae4-d0c85cee44a9 | -7.89127 | -45.4436 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcf3bb7b-63a6-3a45-9e04-6683de9e55eb | -10.82362 | -60.75136 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c9509561-2cd3-3635-b5e8-5d787f67a920 | -10.23116 | -49.9962 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3da2aa7-315b-3f55-98e4-4459184ba2e7 | -11.4432 | -44.92926 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82136f4a-a955-3764-9aba-2e48a3fc2b51 | -10.22335 | -50.00226 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d1565f-adac-385f-b09c-79dd199b1cbc | -11.19612 | -44.81505 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4d3bb963-a6aa-36ba-a026-098bfa3c83b6 | -10.81745 | -60.75016 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b9b152f8-fda6-36b3-8203-6182d6f1ff13 | -8.03863 | -54.89383 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a6290e56-d775-3731-ab6a-7e474964b0dc | -8.66938 | -48.96204 | 2026-09-28 04:34:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdb81953-4e49-3974-a06a-c3c0ae26662d | -11.18982 | -44.80416 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |


[Clique aqui para ver as próximas entradas](README33.md)
