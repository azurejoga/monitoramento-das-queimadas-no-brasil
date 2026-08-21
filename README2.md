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
| 67ae39e2-2780-3332-aa76-c6a16040ead5 | -7.2649 | -47.4505 | 2026-08-21 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6a0e59a-48f0-3049-8263-cf6def2be33a | -13.5858 | -51.649502 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e06b904-54c8-3864-8c3c-f2ce36825c18 | -14.7145 | -47.136101 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de94e5a5-1e6a-3851-af4d-5c42ae86c358 | -6.2356 | -55.417198 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72be7f42-a448-30f4-849b-10e9283507a3 | -6.2277 | -55.474602 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81b763b9-c7b3-3989-a4ec-20a0b49fa8be | -10.8117 | -51.001499 | 2026-08-21 00:14:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f907950-13cc-331a-ab17-fb40014318e8 | -4.9371 | -55.763401 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb350804-9091-3857-8279-03d0f671d23b | -6.2533 | -55.404099 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e340e9ea-8e69-3dbc-9438-bd3058f3415e | -13.4004 | -54.364498 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| faa75711-b519-34f6-9876-6bfd74bf5771 | -8.5768 | -54.774101 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24984416-ceb3-3abf-a8d5-5773bb4c6c47 | -12.8467 | -48.428101 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f66dc5c2-4a80-30c9-97c7-45677d9dd301 | -11.2002 | -55.0331 | 2026-08-21 00:14:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6877d5d4-c8d7-3208-8f63-18c5893c062a | -5.1641 | -47.9408 | 2026-08-21 00:14:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52e7b531-d3ea-32f7-9a19-3912c655ef93 | -7.256 | -49.901299 | 2026-08-21 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ca44c7-c757-3431-9e86-1011477aad5d | -18.687 | -47.487301 | 2026-08-21 00:14:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62ff185f-9d17-3196-817b-5254fe3b3947 | -7.3606 | -45.812 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 223fd073-8092-33dc-93ed-c50d71cb830c | -6.2377 | -55.379902 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66daa817-906c-3e08-8a5a-8d32dfb0a9cf | -5.8184 | -55.7132 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5dccabc-0c2b-3f8f-b04e-5b4460c8a436 | -6.3322 | -44.065601 | 2026-08-21 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35ef6929-d56c-3547-be10-f402360d8248 | -6.6347 | -53.359001 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb289b0b-6a8f-3982-948d-52090406de69 | -6.2337 | -55.408401 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d71a3de-6879-30ff-806f-6c9bc2c4fbea | -14.3452 | -51.8885 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8feb10ad-bf4e-3193-9e3e-061dcbff4a81 | -6.2179 | -55.4767 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7479e57a-0bb0-3fa6-b846-4f79d8ac9629 | -7.267 | -47.459702 | 2026-08-21 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdb7a74e-a1e4-3227-b35d-7b0c0a05e309 | -3.9534 | -43.091301 | 2026-08-21 00:14:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41811691-8430-3f96-ae3a-eecfa63b71e3 | -14.5275 | -52.995602 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91cff379-0ab9-313c-b8f1-751fad6c768b | -13.4024 | -54.3741 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60b9c190-b9b7-3f22-8013-2b5e9a2d74ad | -5.9988 | -57.816299 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae2f621-bdda-380a-ba54-1bd8eada7d2e | -6.3748 | -54.928398 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c193f685-6ca7-3c31-b610-48209057dd3c | -10.7157 | -44.763401 | 2026-08-21 00:14:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51c9216a-3773-30f7-92b4-44500024fdad | -10.2714 | -50.290901 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0da9593c-1d8d-3724-847e-6ac93f42fe56 | -4.0885 | -42.507 | 2026-08-21 00:14:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ae78103-a447-3168-b577-06e7103d1cd8 | -8.5866 | -54.771999 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffac683-bfdd-3ff8-a507-e0eb7a087348 | -10.7369 | -50.3456 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f355667-ad1d-3c20-8e18-a040e55742c2 | -10.3121 | -50.288898 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fce0d41a-8c7d-3772-a1b0-288c3fbd74e2 | -15.2161 | -53.809399 | 2026-08-21 00:14:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09843b24-1451-3ba0-a4e2-4ad4ca774866 | -7.7687 | -61.1152 | 2026-08-21 00:14:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d512ac9-2d6a-31f3-9265-09e2ccf18c02 | -18.6469 | -43.163101 | 2026-08-21 00:14:00 | METOP-B | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b5c67e7-82e0-3a18-bd22-aa569895df32 | -7.3508 | -45.814301 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df31e4fb-3c89-3d9a-a575-3fb50296704d | -10.8043 | -50.2789 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb66dd02-802e-37c9-bbe1-5eaf639e5937 | -10.5304 | -50.8022 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 000aeef8-5142-3123-aa21-49eee1485030 | -2.1117 | -47.1129 | 2026-08-21 00:14:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a40afdc-c51f-33eb-bc4e-2ad56bdc3697 | -8.0529 | -50.096199 | 2026-08-21 00:14:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a958c74b-707c-3179-bb41-de1fde0687a8 | -11.3582 | -47.221699 | 2026-08-21 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1080775b-8729-313e-8350-f605c9b54d54 | -18.649799 | -43.174702 | 2026-08-21 00:14:00 | METOP-B | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 436f5d67-3e2f-3881-a913-5c4b42e4af4d | -18.053801 | -44.407101 | 2026-08-21 00:14:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5c137d7-f874-357f-b09c-233e0b4249ca | -6.954 | -52.806 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b6c510-33b0-3dec-9d87-5bde0cee0362 | -10.7436 | -50.329399 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1878e5-b82e-370a-9a78-183defdc4678 | -7.3548 | -55.6623 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf2738c-5bcf-3a2d-8064-ff0eceb3e602 | -12.9001 | -53.191898 | 2026-08-21 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2a747ca-71bb-3bc5-ad78-a1cb0c5edb53 | -8.5038 | -54.8633 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb8fb24-86e4-335a-a6a0-79e8a4a92bba | -10.7216 | -44.787399 | 2026-08-21 00:14:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7587e6f-d8ee-39a0-8708-60708281502e | -14.7126 | -47.128101 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a709b221-3030-3b52-9246-ec402b4fb52d | -14.5765 | -52.984901 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10400a7d-979e-3725-8213-e5e5660b76c3 | -19.691999 | -46.915501 | 2026-08-21 00:14:00 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0152100-a1a2-3f22-99d9-7f00d6dd5c72 | -14.4566 | -45.615501 | 2026-08-21 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6972559-d6ab-39e2-9a9f-301d494400a2 | -6.6363 | -53.366299 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10ec5f82-cc4a-3739-b2bb-38e696aa50cf | -13.5842 | -51.642101 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5c48bbef-0166-313b-99d0-a618bd8b90c7 | -7.556 | -55.550499 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18768b5-b2f7-3c1d-bb5e-7fcdbe38186e | -6.1152 | -53.058701 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6859ca-86cc-32bb-920a-b3c2a1b2a0c5 | -11.6617 | -48.344501 | 2026-08-21 00:14:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed4489bc-809d-353e-8cc2-e2019a38bc26 | -18.9737 | -47.024399 | 2026-08-21 00:14:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95770e72-5481-306f-bfcb-717ef27804ae | -14.3289 | -51.908199 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab02ffa-87f3-3f0a-a594-cadb24097630 | -10.6309 | -51.6236 | 2026-08-21 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2e97ff-1838-32a5-bc7f-6aca32afcc4a | -15.7585 | -47.765701 | 2026-08-21 00:14:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dfeb69d4-56dc-3261-97f2-ff488cfff3ed | -6.6884 | -58.896801 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1291cfe9-3e9e-3d4e-8dcf-ae3a3b3967f6 | -10.6278 | -51.609501 | 2026-08-21 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8228fef-e02b-3712-9fad-0c89c5022967 | -8.601 | -54.696098 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f451c42-8e3f-31c6-b679-a69fbfce6d33 | -14.7261 | -47.141701 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2a2b49-1b66-3c56-917b-6f9aa38e7066 | -18.202299 | -50.732899 | 2026-08-21 00:14:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44d61efa-b8f4-372c-9e4a-26500e5695cb | -12.5027 | -47.833698 | 2026-08-21 00:14:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 902a555a-1e90-37bb-8a68-870df62f097e | -12.7777 | -48.397301 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1092c663-1b62-34ac-83af-e01c88fa3886 | -6.2478 | -48.657501 | 2026-08-21 00:14:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1dbb11-8f7a-30fa-b667-c23a91a475f8 | -4.9538 | -56.2584 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703f967f-66ed-3b41-bcb7-883180c73a38 | -8.087 | -51.659199 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91ccb48b-a792-39e9-8b1b-7d34691d5d43 | -6.8619 | -59.429401 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbb676b7-8033-3ea0-bdde-93a7d74041d1 | -8.4959 | -54.874199 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f407edb0-67d2-385d-80b5-86482eef75cd | -14.3273 | -51.9006 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2704b93f-87b7-360e-aa26-c38aa1bd3084 | -10.1688 | -54.2677 | 2026-08-21 00:14:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c77bccc-396d-3e7e-aad8-aae85ad5024c | -7.2527 | -49.886799 | 2026-08-21 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd1167d-9a51-3f96-a9ed-9b22180ed948 | -14.3501 | -51.9114 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 898e3a4a-41a9-3f14-8c88-0d8fd8b402b8 | -13.4417 | -51.790401 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51286adc-9a2b-3676-a176-875121be6391 | -6.8944 | -55.712101 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3db582-cd80-3530-831d-c8668a09541c | -6.4595 | -43.5341 | 2026-08-21 00:14:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2973f3ad-c8f8-35d3-8edd-803d2c310199 | -12.2456 | -43.149601 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 892f30e9-5045-348f-b0ff-40c1cbc17ca4 | -10.8231 | -51.006199 | 2026-08-21 00:14:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6d6653-28be-35a1-a1d6-a365059c211a | -18.017401 | -44.596699 | 2026-08-21 00:14:00 | METOP-B | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6afc2a0d-375f-31d9-9605-56984b4b819d | -8.6626 | -54.6017 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5006718-5824-3704-9b64-c05bf57f7869 | -6.1769 | -55.429901 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7fa6c0-c456-3d79-88aa-59a2fe26da6c | -6.2061 | -55.469898 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbb13b5c-8dc6-31ba-b45c-3272ce0d74ec | -6.7138 | -59.064701 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1798e4fe-824c-3932-a3e5-6986b1a64344 | -11.1816 | -54.0224 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebacdc88-7495-337b-999a-5d9bf48d08a3 | -6.112 | -57.677898 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcbd7e6f-9025-3d6e-9ae6-de4f347ab46d | -8.6243 | -54.709202 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6361891f-c9ca-3d5d-bdca-29444e512805 | -3.9486 | -43.113602 | 2026-08-21 00:14:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a3e641-2048-3ae0-bc24-889f9af0b435 | -8.5885 | -54.7808 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7299756-d8f9-3cf5-a5ae-2c5e277cc39a | -10.3203 | -50.279701 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0008f1e-3b5a-3393-97af-52a331d3d23e | -4.9635 | -56.256302 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e13ab21f-07ed-3b5c-808d-2cd89bc7eb39 | -9.3588 | -40.4081 | 2026-08-21 00:14:00 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c39b3fda-60d8-3758-8af0-c6526ebafe93 | -12.7327 | -48.470901 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
