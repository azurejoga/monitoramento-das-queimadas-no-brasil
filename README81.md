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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14512733-ddce-358d-8d49-33882a347f8f | -13.9919 | -54.0189 | 2026-08-29 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e9c44cf7-cdd1-3525-8f29-f06e7147581f | -12.2093 | -50.5386 | 2026-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1cba5c87-3b3c-3071-b2a7-8e27e34f1263 | -11.2314 | -54.0164 | 2026-08-29 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 32bc7d62-00e8-3062-b137-25e6eb6d188b | -7.3663 | -55.1734 | 2026-08-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 46280a7f-409c-3cf2-a3e8-84b261efce64 | -11.1913 | -51.292 | 2026-08-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 13588188-cf33-3a25-841f-421d121f5c0a | -11.7167 | -54.5244 | 2026-08-29 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ce2f7f0c-09bf-33bf-8777-9e21cd24cb6d | -8.7991 | -62.4715 | 2026-08-29 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a8a8aa07-fec7-384c-beff-2945d4f24e75 | -5.8895 | -57.7513 | 2026-08-29 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6e6cf4bd-cbb5-396f-9d3a-993ed2290994 | -8.7767 | -49.9977 | 2026-08-29 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bdaa519a-f978-3e48-a9ca-635e1832f3c5 | -11.7028 | -47.6129 | 2026-08-29 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| dfe8964c-aa44-390f-8a79-b3a2cbfd04e2 | -8.5966 | -54.8159 | 2026-08-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2840f13d-1091-3d1f-9e8e-ec174caf2de2 | -7.4734 | -61.4037 | 2026-08-29 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 119d7224-7228-3598-b49b-f92370075976 | -8.9428 | -63.2797 | 2026-08-29 14:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 6b11aadd-92a5-37e7-a1d9-57ef03742694 | -14.4 | -52.565 | 2026-08-29 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e243ccc2-9d51-3507-aeb0-24327bdc791d | -7.5478 | -61.3056 | 2026-08-29 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 16253825-b3d0-3747-8d28-4a0bd2288260 | -7.5662 | -61.3049 | 2026-08-29 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 170.8 |
| d974ee71-74a2-3254-9041-3fa66d0f6e8d | -11.0054 | -49.6893 | 2026-08-29 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b01da829-434a-3cb1-b780-36e13656df12 | -11.0244 | -49.6872 | 2026-08-29 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 926f6d71-0fc4-3560-a220-af33107c3392 | -8.799 | -62.4905 | 2026-08-29 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 60bb35c3-b8d2-304f-afe4-4d0959aba315 | -12.3811 | -48.1877 | 2026-08-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 145a202a-082d-3862-b97e-ffdae2325436 | -11.0057 | -49.6677 | 2026-08-29 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| bae6e19c-d9cf-380f-a576-a3d655ceeafd | -14.419 | -52.5837 | 2026-08-29 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7171a690-a514-361a-8cb7-5f2e51f38d38 | -10.8804 | -50.4965 | 2026-08-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8d3f0d9c-d21e-34e9-aa0d-57546d7f4949 | -8.1482 | -47.5218 | 2026-08-29 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d0c4f118-a1af-3be1-ba96-bb5d60f976c8 | -10.5404 | -50.4683 | 2026-08-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ed6a4759-e6f9-3dbd-a2ea-e538b506898a | -11.1639 | -45.5897 | 2026-08-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2194014a-2658-3d53-9836-71e4b21569df | -10.9673 | -51.0614 | 2026-08-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 1ccf3ac8-543d-3e08-ac01-9d7a7a0ccae9 | -11.269 | -54.0334 | 2026-08-29 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 76f28890-34c0-38ce-9af6-010f9a165ef2 | -5.8895 | -57.7513 | 2026-08-29 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| edf76ea1-ab58-31fa-aaf5-70ee50a0bd6e | -10.8425 | -50.5005 | 2026-08-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1f1041b1-d18f-3b77-a1d4-e4070ee57df5 | -12.2284 | -50.5363 | 2026-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 35fb7acb-c1e5-3725-bb45-943a42fa545d | -12.2093 | -50.5386 | 2026-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 96d984f3-fd91-3873-9124-e494fb7dc6ec | -11.0057 | -49.6677 | 2026-08-29 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 50eabf23-8aa6-3c99-87f2-fef0f45cecf7 | -13.9915 | -54.0397 | 2026-08-29 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a056037f-0b48-39d7-a62f-a8967b7f10f1 | -6.6317 | -43.73 | 2026-08-29 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| c61e6be2-ffeb-35c3-a538-f471cd13393c | -6.1656 | -57.7988 | 2026-08-29 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 909af343-9389-3f7d-8859-f53af0c40fb5 | -6.9872 | -59.2582 | 2026-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 151f7cd8-4ba8-375a-9664-bdd1cbe7768b | -11.0247 | -49.6656 | 2026-08-29 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4754b1c4-6304-3769-b9b6-da0dfef1119c | -6.6129 | -43.7317 | 2026-08-29 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2629802a-a35d-34c8-b39f-2c759cd4614c | -5.8894 | -57.7708 | 2026-08-29 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 52419c28-75c3-3181-8c48-9927af35dc00 | -8.5968 | -54.7957 | 2026-08-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 99fb07f1-61fa-3626-9071-a4f21212430f | -10.3391 | -49.9762 | 2026-08-29 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f9450b1b-9b2d-3dd5-95a2-8cfeb598556d | -6.8387 | -59.4186 | 2026-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ddcd68f2-238f-3f38-9d55-7f181119ce6c | -10.4795 | -64.4824 | 2026-08-29 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| dca9327d-2346-3d0b-a43c-574e50c6ee47 | -6.6315 | -43.7533 | 2026-08-29 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b552dc20-fd5c-39a7-915e-44e4918684e8 | -6.1657 | -57.7793 | 2026-08-29 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c8f05435-0154-3a6d-a47f-7340729fd2fc | -8.7772 | -49.955 | 2026-08-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 915fe443-f75a-35ee-8e97-d65f60e6578c | -8.7769 | -49.9763 | 2026-08-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 93d95a1d-a2cc-3242-931d-50b8bccd2e9f | -11.7167 | -54.5244 | 2026-08-29 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 288fd7c1-ba78-320f-995d-f70fe9fc3184 | -14.4 | -52.565 | 2026-08-29 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| af9e1697-5daa-323a-a3c8-8eb88cc09363 | -10.4794 | -64.5012 | 2026-08-29 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 13ea9d26-ff29-3719-96ff-1632c88c101b | -11.1726 | -51.2728 | 2026-08-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5a8fa2ce-8e16-3eca-8c74-a50ec58d2056 | -6.8018 | -59.4201 | 2026-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8cdc0dc9-8805-3818-8bec-6a34f805c418 | -11.2503 | -54.0146 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6c94a82d-e9dd-3e35-98ab-153a130635b3 | -9.9708 | -53.9419 | 2026-08-29 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| a5346d46-bb2b-3a3d-9f40-7a995fcc7800 | -12.9027 | -45.8612 | 2026-08-29 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 14760b8f-723c-39db-b12a-00a1203f927c | -7.5139 | -55.2851 | 2026-08-29 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 6d96a354-e998-323e-b181-055b2ac2a5f9 | -7.4734 | -61.4037 | 2026-08-29 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1a5edbd8-4ba0-30b6-8279-94f4f6595bf1 | -10.8232 | -50.5239 | 2026-08-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 52dd26c7-58ee-3605-a4b8-5e6b7740198c | -11.5039 | -46.9471 | 2026-08-29 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e372d458-03c3-37c4-9fed-719a1528f2a5 | -8.9613 | -63.279 | 2026-08-29 14:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e787f7c4-d25c-3645-ad8f-a541a331db4e | -8.5969 | -54.7755 | 2026-08-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ecbd008c-5d19-3b72-a25b-ce54d4bd9a03 | -8.7767 | -49.9977 | 2026-08-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b9af2183-4a17-3f52-8898-7e18ec6c2efb | -11.0054 | -49.6893 | 2026-08-29 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 1b58871d-55c4-3f97-bff0-b9d599a8a100 | -8.948 | -62.3894 | 2026-08-29 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d1880a5b-2f83-3e50-a8b9-900cbba99c9c | -8.9428 | -63.2797 | 2026-08-29 14:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 66c248e0-aa61-3faa-bb61-4265c56114da | -11.1723 | -51.294 | 2026-08-29 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 18aa3fd6-a92e-3c4e-a102-c22444d43a00 | -13.9919 | -54.0189 | 2026-08-29 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 9c5c1c01-dead-3a0c-a52c-ff34c506b59b | -8.8184 | -49.6308 | 2026-08-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 29082200-d7c8-3f64-bea6-688416c4da22 | -8.7764 | -50.019 | 2026-08-29 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 77c9d14f-cd68-3791-90b3-8d4166baf079 | -11.2103 | -51.2899 | 2026-08-29 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d3f7cf8e-1bd1-323b-b372-27f37045dce5 | -7.5662 | -61.3049 | 2026-08-29 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 172.4 |
| d627ff6a-2179-3439-a1af-e96ce1803e55 | -6.8571 | -59.4179 | 2026-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 53ebd0cb-af55-3213-b5f3-9e49e62070a2 | -11.2314 | -54.0164 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 412269f5-d5c5-3e1f-aefd-86f39ffba4f7 | -10.4609 | -64.4831 | 2026-08-29 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4892f313-809c-3fc0-a470-f3ab717547a0 | -12.1902 | -50.5409 | 2026-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d45b18e3-82e7-3c50-8bcb-560962f8c871 | -11.7165 | -54.5449 | 2026-08-29 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e81e0535-84fe-365b-afae-05f223bc3ee4 | -11.2489 | -45.0732 | 2026-08-29 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 990ec4e6-1c74-3620-a2a5-8082bd18320e | -12.1899 | -50.5623 | 2026-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 1d295bef-f695-3407-b915-35be5326837f | -11.1441 | -50.5961 | 2026-08-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0c8abe2c-c2d6-376e-a8a8-e7a423320ed8 | -9.971 | -53.9214 | 2026-08-29 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e1064153-aa3c-3c26-b497-a2f350912933 | -7.5478 | -61.3056 | 2026-08-29 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 755731a7-7549-3546-9892-c861817c054a | -13.8563 | -54.0967 | 2026-08-29 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a68750bd-48bb-31a7-a2ae-04e563108ccd | -11.2317 | -53.9958 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 944ddd18-b196-3178-800f-2972fc3c4dc8 | -10.7791 | -53.9752 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 358fbdb1-c1ab-3543-b524-d05e99d927da | -11.6975 | -54.5467 | 2026-08-29 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 114dc9f1-8e11-316c-bc02-01f5ecb4f155 | -11.2693 | -54.0129 | 2026-08-29 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 7bea31c0-74e3-3099-8b00-40dee73dc9e6 | -8.5966 | -54.8159 | 2026-08-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 6acd4cc1-0781-3b66-a212-8b2805aebad5 | -9.6022 | -55.128 | 2026-08-29 14:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 79319d43-3a9d-35fc-be09-3f90748e4380 | -7.0057 | -59.2575 | 2026-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0d7fa603-ea60-3a70-80ec-dccadbd4955d | -10.8235 | -50.5026 | 2026-08-29 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 42e6b1e8-09f2-383d-8322-28574025aa46 | -10.7407 | -54.0401 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2034d9a3-bf2b-3afe-b5af-17f3c8e01566 | -9.2094 | -51.5444 | 2026-08-29 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| aff4099f-b400-3645-9624-51e923bf937b | -10.7596 | -54.0384 | 2026-08-29 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 25251be1-1a62-3bf9-bb51-2bb918b86b39 | -8.116 | -45.4715 | 2026-08-29 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| aca5728b-9333-38af-b652-9dad1dd133ef | -11.0244 | -49.6872 | 2026-08-29 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| efefd029-b50e-3834-800f-db6282503627 | 2.2375 | -50.7515 | 2026-08-29 14:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 14e88a27-33f8-3d84-a6e1-67629711cd85 | -10.7596 | -54.0384 | 2026-08-29 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| ebfc27af-e368-32ef-89ea-896d39db0f4b | -8.7764 | -50.019 | 2026-08-29 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 183411f5-aada-3e28-876f-613d60516617 | -11.0057 | -49.6677 | 2026-08-29 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |


[Clique aqui para ver as próximas entradas](README82.md)
