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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6143672-bcfc-3a16-8c5f-78c40ca14696 | -13.3175 | -51.769 | 2026-09-19 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 0eb5eb92-f42b-3a2a-940a-99e109bfe037 | -9.0361 | -48.7053 | 2026-09-19 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0cf08701-34ea-3899-a0f5-01b8725c8aa0 | -13.3171 | -51.7902 | 2026-09-19 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a01f3c2b-27ad-35d2-96d1-83e2ab9a9ebf | -6.277 | -41.6841 | 2026-09-19 12:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 1bd88238-05fa-3111-98fd-ce483e09645f | -10.567 | -51.3137 | 2026-09-19 12:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 392.3 |
| d854ce6e-0fcc-3ebc-8b15-84fa53b79af3 | -11.8742 | -47.6348 | 2026-09-19 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| d533bbe0-9b83-3fcd-919a-b09acd5e621b | -12.1339 | -46.9734 | 2026-09-19 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| d4476418-6948-30cb-9999-3fe8ccdc60c9 | -11.949 | -50.1186 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| fbfe17da-aa53-3e08-9296-c668d9cc8af6 | -12.1531 | -46.9707 | 2026-09-19 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 01f7e7e6-0af4-388e-861c-8e3c6361278c | -11.949 | -50.1186 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 8e5a10a7-8934-3b8b-bca1-929ed162ffdd | -12.5032 | -50.0508 | 2026-09-19 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 54df8cfd-be24-385a-a71a-df89968f8e9e | -9.0361 | -48.7053 | 2026-09-19 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6f991b5e-605c-3bec-be58-be046abcc963 | -12.2688 | -49.1907 | 2026-09-19 12:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 00fe661d-a81e-31f0-a496-96c11ae14033 | -4.5585 | -42.9758 | 2026-09-19 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 12135b78-a58e-3756-abf0-7fbd24eda678 | -3.3494 | -59.8097 | 2026-09-19 12:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 56f9455a-a07d-3696-b136-a0510fc0791e | -11.1038 | -49.4406 | 2026-09-19 12:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 6c8f9638-24cc-3942-b32f-da12f676ba65 | -6.2773 | -41.66 | 2026-09-19 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| df3666ca-88b8-3e55-8215-a46fde041609 | -11.234 | -48.3571 | 2026-09-19 12:50:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| d6fd6e20-1192-3b61-9f65-1dd1d58d3a8b | -11.1035 | -49.4623 | 2026-09-19 12:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 01e4d8cb-ae53-3b22-8eae-b594e1fbda8d | -5.6408 | -43.392 | 2026-09-19 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e655e780-7641-310d-a209-e3e1f44cad07 | -13.3175 | -51.769 | 2026-09-19 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b84122b5-04cb-3d6f-b2f8-69e00da01350 | -7.1169 | -44.0339 | 2026-09-19 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d8e7d300-56ff-3237-9dd9-c7a2efa972ed | -12.6892 | -45.9629 | 2026-09-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| dfadfcb7-da91-3253-9e1e-28884909e758 | -12.1336 | -46.9959 | 2026-09-19 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ded4dd9c-cec0-3fb7-9caf-397098c47bb8 | -8.9811 | -50.1712 | 2026-09-19 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5cd3afd5-d6d6-38cf-b704-24cbfa81e4af | -13.3171 | -51.7902 | 2026-09-19 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d82e71be-487a-3a36-99be-68a75246e4bd | -11.0062 | -48.3407 | 2026-09-19 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4eadd0da-64f9-3d44-ac18-94068f3af36d | -7.7629 | -46.7389 | 2026-09-19 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8a0b0756-f8ca-36b8-a1c2-a0b096891387 | -12.4841 | -50.0532 | 2026-09-19 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 0f0d9161-00b2-3bff-b133-9a021e66da01 | -3.331 | -59.8292 | 2026-09-19 12:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5ae1de8f-c935-309c-aa6d-96a4eb3e8f19 | -12.0082 | -49.9822 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4d68e177-4d6f-36a3-8d8c-cf24d7ca1f0e | -10.2163 | -46.5937 | 2026-09-19 12:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b8674319-feb6-3e9d-ad66-adf397613a2b | -12.0273 | -49.9799 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5ed68cab-5066-36b9-9c89-bd69818f5e41 | -10.8466 | -50.2009 | 2026-09-19 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c414235d-a339-3f51-b9db-2b67f8f4e2f8 | -11.9112 | -50.1016 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 7693dd87-98d0-36bb-9194-da54f92eb5a3 | -9.0358 | -48.727 | 2026-09-19 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 2c6b3c8a-fa66-364d-a8eb-6af735fff82c | -9.0355 | -48.7487 | 2026-09-19 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f3ce3142-0a5d-3bf6-94f7-0725bb0ce561 | -12.0076 | -50.0254 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ad7cd1de-6498-345b-90ff-60e9375ce230 | -6.2585 | -41.6617 | 2026-09-19 12:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 337.1 |
| 6def701e-619f-3abd-9108-def4a6b8573e | -11.1228 | -49.4384 | 2026-09-19 12:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ab988fbc-8579-3e5a-9c43-c3f2d6bebc5e | -10.5667 | -51.3349 | 2026-09-19 12:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7bef366b-ba38-38fb-a6b8-a1e1614b80e1 | -11.3604 | -44.1521 | 2026-09-19 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 4fbc96a3-97dc-33a2-aa27-f06c4185b03c | -8.7919 | -48.6851 | 2026-09-19 12:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 5bee7d7b-b6ca-342a-a1e4-e890f23df3cb | -9.2377 | -46.2119 | 2026-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 155fac10-a545-3103-8805-b37bb0c8740e | -11.0608 | -49.7909 | 2026-09-19 12:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c8c20d31-7ef3-3b18-8920-fbeb5c3c017f | -3.3311 | -59.8101 | 2026-09-19 12:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| d6c9697f-8495-3464-8b72-98287da5cc5e | -12.027 | -50.0015 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| ec43121c-e2df-3c74-b1d6-0efd6d7d0a59 | -10.7133 | -50.258 | 2026-09-19 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8bd4ea33-9e56-3361-9796-c99c65d0da4f | -8.7731 | -48.6868 | 2026-09-19 12:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 1e082697-19d9-3040-8e0d-07e0c5f2a5d2 | -11.318 | -51.7218 | 2026-09-19 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 55177f8a-b0c5-3c9d-a0b0-b90881906ff9 | -12.1339 | -46.9734 | 2026-09-19 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 3e283877-073c-3328-ae20-92ff75ab93a9 | -9.0096 | -44.9209 | 2026-09-19 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f061cec7-30d7-3efe-91eb-707600857913 | -11.083 | -48.2875 | 2026-09-19 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6da18080-0663-39dd-91b7-83bb3e9953a4 | -10.8282 | -50.1601 | 2026-09-19 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 9756005f-d8ff-3a95-a5be-1b577111da41 | -11.7823 | -49.8152 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2330fb36-bd43-3450-8cc1-45845810cf10 | -6.277 | -41.6841 | 2026-09-19 12:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 5854d07f-d624-3414-9b7a-4430d821e91e | -6.2582 | -41.6858 | 2026-09-19 12:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 392.0 |
| c6749734-41a0-3300-ba75-e7895c5c28f9 | -11.9299 | -50.1209 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1dc95c5f-60d8-3010-a06f-b0aad616282d | -10.5481 | -51.3156 | 2026-09-19 12:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6959ee5a-f5ec-360d-b87d-0a52376b5ab6 | -12.2883 | -49.1664 | 2026-09-19 12:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| dbb169ad-28fe-3d5c-9221-98f0fdbefd59 | -11.1369 | -54.0251 | 2026-09-19 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 2d636e58-1581-3016-8e9d-7effc95de62b | -11.9487 | -50.1402 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 780cb11f-63b6-3e18-8398-0e7f42c37cdb | -10.567 | -51.3137 | 2026-09-19 12:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 2f282e58-0355-320f-8bb9-bcbf08677a59 | -12.7085 | -45.96 | 2026-09-19 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.9 |
| dab04ada-0c92-36a8-b3e3-8674915c81da | -11.9109 | -50.1232 | 2026-09-19 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 4d81e3cd-b431-3c58-bde5-90892e4b5c99 | -10.6703 | -50.6465 | 2026-09-19 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 68f822b6-b182-3964-a190-a1a4a928f4a2 | -9.2567 | -46.2098 | 2026-09-19 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e4477a3a-be8c-36b9-b753-b5333dc48740 | -10.8469 | -50.1795 | 2026-09-19 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 3971740a-ac52-371e-a40e-1d4709c41594 | -5.6596 | -43.3906 | 2026-09-19 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| c7a83b8e-9b03-3734-8929-b5469f36026f | -12.2879 | -49.1883 | 2026-09-19 12:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| cf059b38-4da9-3f3e-93fa-db9977cceb8b | -10.8279 | -50.1815 | 2026-09-19 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 10e6f458-b2b9-3d50-a812-d34fef685c6e | -12.1535 | -46.9482 | 2026-09-19 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 31953c5e-c0b2-383b-b9d2-a01bf3f1ed9e | -13.0173 | -46.9352 | 2026-09-19 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2fb4f4a9-aacb-347f-b875-37426faab59c | -12.027 | -50.0015 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 10ec580b-aa73-3410-a7b2-07c6ad88af67 | -6.2236 | -45.1853 | 2026-09-19 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2a8c7837-69c1-3dbf-91db-a2689bf92540 | -11.9109 | -50.1232 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 90d4b81b-243a-3fa0-b953-41f82e6f6ea4 | -13.2414 | -51.7359 | 2026-09-19 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 8ae0bdb7-37ec-3822-b259-eaea5c2c7550 | -12.0267 | -50.0231 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b5040fdc-2f10-3cff-8446-9beebd8e856f | -9.3815 | -45.381 | 2026-09-19 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 70295ff8-625d-32ac-8422-7773be59d8e4 | -6.2585 | -41.6617 | 2026-09-19 13:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| f34b6573-cd49-3b62-86b8-d2027a3b6607 | -7.1169 | -44.0339 | 2026-09-19 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| cf164c53-261a-3f15-aee7-c74d528e8de7 | -12.4841 | -50.0532 | 2026-09-19 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| a2343b23-43e3-30ec-8945-1aa5a1cb75b9 | -11.234 | -48.3571 | 2026-09-19 13:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e12f63d9-e130-39f2-85c9-bcf817514286 | -3.3494 | -59.8097 | 2026-09-19 13:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 5f334292-4205-3a0c-80e9-6b64f1fd2daa | -10.5667 | -51.3349 | 2026-09-19 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c5e15450-731c-36d9-aab7-fbc14bfdff5c | -11.1228 | -49.4384 | 2026-09-19 13:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 94b7db25-25eb-3971-a479-77f3b037d53c | -12.7085 | -45.96 | 2026-09-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 269.8 |
| 0052601f-d1d1-3b6a-ad72-d8644a50950b | -11.318 | -51.7218 | 2026-09-19 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| fe35b062-723e-3503-9b9f-05c5dceb2861 | -11.0065 | -48.3187 | 2026-09-19 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b85e4415-134a-3cfb-a151-299c27f1c6af | -11.9487 | -50.1402 | 2026-09-19 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3bae6439-2d9d-3b1c-ba87-9c7e97ebae6e | -7.7629 | -46.7389 | 2026-09-19 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| efc8859b-7bfc-31a5-8bae-567975942b4f | -3.3311 | -59.8101 | 2026-09-19 13:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 76500a15-e773-3974-8dce-edc880467be0 | -11.2987 | -51.7449 | 2026-09-19 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3e945a84-ccae-34fc-876b-fe70fc2c42c6 | -12.604 | -50.9191 | 2026-09-19 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 6a061b79-0ae9-3395-88a2-caca8417a7e3 | -12.1531 | -46.9707 | 2026-09-19 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| b505ed3a-b930-3900-9e15-e36e0e70bb7b | -11.1035 | -49.4623 | 2026-09-19 13:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 60bfa188-1eaf-3fae-bc15-f4db8dfb90dd | -9.257 | -46.1873 | 2026-09-19 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 093a4326-2a0c-3219-9f31-81a48c7f6614 | -6.2582 | -41.6858 | 2026-09-19 13:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| eaac18d3-c583-3493-b720-39540fb3484c | -13.2222 | -51.7382 | 2026-09-19 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0adf33d4-726a-3a76-8d0c-ecc63c8ae7f7 | -9.0087 | -44.9897 | 2026-09-19 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |


[Clique aqui para ver as próximas entradas](README107.md)
