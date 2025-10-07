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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec3b8ae-fd01-3ba4-a56b-2697f8eef7a0 | -12.0203 | -47.78491 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01ea01d9-20dd-3ee8-b332-e8d160a2fe21 | -10.43527 | -50.40154 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4685dc42-c047-3236-b9bc-b6600c3eb777 | -14.28565 | -45.84444 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67a6e0e0-9f98-3531-9384-ac267764303e | -8.17857 | -50.30633 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6c63498-3df4-3ca4-90dd-d64626a076fd | -11.02603 | -51.15086 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eda8a463-78f2-3162-99fb-ea5b7385de64 | -11.9483 | -46.42716 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63e75092-f602-3065-824a-13810f1fb4f4 | -12.89125 | -54.75539 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eba4326b-89b1-32c7-8c68-a76d6c02b666 | -8.34531 | -49.65855 | 2025-10-07 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ef29ef3-37a6-3f07-b5a1-e8f5220f7b0f | -12.93834 | -46.79449 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aadd7813-79d7-33ae-8b5f-52cb8308a6fc | -10.42042 | -50.2812 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9768112-dce4-3a87-952e-563ba6ae1881 | -9.14938 | -61.23707 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb85f6a1-51dd-33a9-81f7-d6e2710a416c | -12.40481 | -50.2734 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94cec7ca-5d9c-3796-8a35-0bd0d98cd1ae | -12.99312 | -46.78912 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3211f01-f438-3d15-8560-227177e0791f | -14.91859 | -46.81626 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f70238f-2316-3512-8a5c-da35567f25e4 | -13.31148 | -47.77062 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8f37ab3-7e58-393d-98b1-03258ded8612 | -14.73805 | -46.03816 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0182dd50-a29f-3619-90b7-e06dffa77d5f | -12.0153 | -47.78251 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3df40eb1-c5a3-32d3-81f6-577251775432 | -11.74404 | -43.29355 | 2025-10-07 04:57:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ade9f8f2-a526-35fa-804d-0a0ca8fe2ac1 | -14.73498 | -46.01576 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1f52f8a0-580b-3388-8a45-941eb170591e | -15.35619 | -47.30954 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 803834cb-0625-30a7-9678-c9f8cf3b3c95 | -15.02143 | -47.55904 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 765b8d6c-1b47-31b2-ba68-e1f14f8613c0 | -14.76749 | -46.02732 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8877ef5e-592e-352a-93cc-71e002b9fb91 | -11.94894 | -45.48642 | 2025-10-07 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d7da38e-3b20-36e7-b744-e79ce3dc99e6 | -14.90714 | -46.83042 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e22e3fc-0e38-3651-9092-b9d816a6f695 | -10.36387 | -44.98295 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d91e233d-fa03-396b-b465-0726a80c4d2b | -14.69899 | -48.3898 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceeeb7ed-bbad-3880-8ade-c260110f536d | -9.09072 | -47.9609 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 438d4608-cacd-371d-a7cb-c4cd21272ba0 | -13.70682 | -48.07473 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 257fd5d3-353c-3067-9d36-6d9172f0a223 | -9.27928 | -48.32291 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec5e4cee-1cfe-3580-928b-41299475cd96 | -13.97066 | -53.89134 | 2025-10-07 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e061476-753e-3566-a533-e569063879e7 | -9.6077 | -57.14483 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d1ed8f2-4b1c-381e-bc57-e87b63272c56 | -13.38505 | -47.53864 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bca4f0eb-f0ec-36d5-888e-8fb09adc4f22 | -10.21859 | -57.6834 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae5db9f-7eac-326a-9f16-3c0c29f84902 | -9.61618 | -57.20211 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6388f41e-8e4a-33f3-95b5-935c5c247bc6 | -14.66389 | -48.40071 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00cbf146-b30a-358a-9423-64c81c0611b7 | -6.7245 | -58.58776 | 2025-10-07 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62fc1a5-1f1a-3115-8cc2-5c2f0001b2e2 | -10.42719 | -50.31836 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 1fe7d2e3-a769-3f1c-9239-ebafd128ebc5 | -10.45727 | -50.41494 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1a381091-909f-3783-963f-6611630dea3a | -10.41392 | -45.38888 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2ecce14-f3b2-3375-a74b-c8f4657f5349 | -10.9164 | -47.07048 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cd5772a6-cc0f-3988-af71-e5b96face4e2 | -10.67058 | -54.69398 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3ad5f61-cfcf-3cca-9021-eed3a8d04c48 | -12.01864 | -47.79374 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 331e790b-2d76-3313-915d-4a06b3c62297 | -11.88453 | -44.95717 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51a1d55a-263b-30d7-915d-5095ebdd8ba9 | -9.1414 | -58.93869 | 2025-10-07 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3e07d2c-d2ef-3c3b-b1b9-419aae6a9190 | -15.27864 | -46.34542 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f362272d-6102-3ee2-b902-a6f974cf4d11 | -12.90732 | -54.73969 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 382d153c-988c-363c-adfd-b228142ec215 | -13.28739 | -47.8064 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfea1388-8223-367b-a03d-ac1c1e0aa7c8 | -9.84514 | -51.37738 | 2025-10-07 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6325727a-1945-3315-9aa0-673149c3a1ac | -13.85775 | -43.99058 | 2025-10-07 04:57:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eec7358c-bb07-3f2d-8c3c-89950f373dad | -12.90344 | -54.74273 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cc4d3de6-0073-37d6-825a-3ebc7d58715f | -10.43136 | -50.40097 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 817f496c-09e4-3d4e-9947-967a2986debf | -9.02167 | -50.69364 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07c2b9e5-5b5f-3a87-b248-9abba5d21dd8 | -11.15161 | -54.8754 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c044b01c-ec3e-37ae-84c9-1eca0c84413c | -7.46367 | -63.62085 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8216b738-040f-3aa0-82ba-e3cd68c04253 | -14.6686 | -48.40148 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5c6b998-6a50-3de5-b0d5-cf674f868a9c | -11.04384 | -50.92118 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2cab3b45-a468-3a91-b533-cf1af727f856 | -15.02192 | -47.55513 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a243c3ee-e7d8-3a3d-8aff-bdf67f580894 | -11.86379 | -56.88538 | 2025-10-07 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45ebe55c-9610-3b71-9972-b7f3812b4914 | -10.39228 | -45.38384 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47632ae1-7094-3f97-9a3a-5a37a0e7946d | -14.70372 | -48.39056 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f9a1f7d-86c2-3f77-a166-30fcd6527901 | -14.92022 | -46.80188 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1547545-d2bf-3962-94d2-a0eb78547db6 | -14.60145 | -52.49001 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da7f4a5-822d-3004-bf4b-52fbdd0a53f0 | -12.25506 | -47.85196 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bafc9c71-d187-37ae-b571-b551f83e7009 | -11.0066 | -52.31275 | 2025-10-07 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95bf3f96-aab0-3216-8bc1-137ad40c4583 | -9.03381 | -50.58652 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6c4ce8d-9289-3d80-a9a9-c014996bf646 | -13.73776 | -47.9433 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 482f16ce-1696-34b3-89e8-df2e80cd47f4 | -15.35669 | -47.30535 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce4fabe-7a4c-3467-9b53-32f59fca652b | -14.91272 | -46.86768 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df3f7b76-e199-3cf6-92ec-dfc6ea4afa16 | -11.22689 | -47.77214 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0846019f-98fa-3eed-8784-39fb405414da | -14.93529 | -46.8111 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87b999bf-9c7f-3874-8a68-920afe7c7258 | -11.05667 | -50.9063 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b04e68a-1e22-37f3-aa22-44ad6d71ae85 | -12.89846 | -54.7529 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9d8041c-7c84-3c3b-8e0f-a6929df601ae | -10.37503 | -50.29337 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d0db769-6ce2-382a-95b9-43be79d9dc26 | -10.39769 | -51.60543 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d09ec1-ab1e-38e8-a60b-4fa9eb149ae1 | -10.50278 | -51.50039 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38582bdb-c144-3c7c-bca9-3e6eb609ea24 | -9.06569 | -54.53428 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd832478-8f6e-305d-af4b-a307a841ed3b | -11.64542 | -46.87919 | 2025-10-07 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8c80ca6-e558-3b60-9052-e552bfb98eb3 | -12.28431 | -51.36679 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7462e983-64a7-34c9-9b59-15325fe56e0a | -10.55146 | -54.86913 | 2025-10-07 04:57:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48b01dbe-ff28-34f3-ae24-3f56705673e7 | -9.73783 | -48.08113 | 2025-10-07 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba6b28d-0ce0-3161-a15a-0b784856b931 | -11.74345 | -43.29875 | 2025-10-07 04:57:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1ec1fc52-2234-307b-876c-47ce5dbb6479 | -14.86645 | -51.45343 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e39b4803-ad90-33d3-873b-e0fa63108478 | -10.996 | -49.5835 | 2025-10-07 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ab7d6ab-8895-3c86-be2d-f05dcdd4fb1e | -10.41899 | -50.29134 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0556429d-52f2-317b-9dc7-e6f6741380be | -15.49746 | -46.8337 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b64c14f-780e-3e2a-9b3f-e537d8667a87 | -11.1233 | -47.22143 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03d84183-ff27-35a8-b46d-41cb5058711f | -9.97944 | -48.0205 | 2025-10-07 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b07a3b5-38b7-3960-994c-3ea8aa6ce261 | -14.82882 | -52.93077 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c947a80a-ae18-3d5d-9418-411fafd4c802 | -9.89441 | -60.16275 | 2025-10-07 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d469df3-67f6-35eb-90ef-003974cea5dd | -9.40385 | -49.37203 | 2025-10-07 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75ffc524-8ac0-3127-8b60-7446b7b8fd37 | -9.14693 | -60.62442 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 094c038c-2665-329a-aa9a-3b328b7fbdb0 | -14.75977 | -46.04526 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b6920db-d446-30a1-861e-7e311ddda538 | -11.84686 | -44.92021 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d46e782-3f98-37ef-86f7-06c7268501e0 | -10.7361 | -56.59783 | 2025-10-07 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf65a7e1-914b-32ce-a284-8fe968854b31 | -15.16883 | -52.77303 | 2025-10-07 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e102fcc-4bb3-3df6-a6f8-7237ec9efab1 | -13.32675 | -48.0387 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 379dfd1d-32d2-380c-841b-479d2546025c | -12.97682 | -46.78045 | 2025-10-07 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc9ec384-d22f-3adc-83fd-df871af0a58b | -7.61791 | -61.34866 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cbbffe43-0f12-34a7-b4bc-5b189c866134 | -14.53469 | -46.63876 | 2025-10-07 04:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d8105ea-1231-3916-ab8e-2b989cb9170c | -10.52969 | -58.03509 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README93.md)
