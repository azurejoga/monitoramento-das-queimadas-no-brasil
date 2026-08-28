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
| 2b150d37-9c36-3ba8-8d00-a231a914f421 | -11.5659 | -45.5338 | 2026-08-28 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4c3980e5-3c91-373a-bec5-0458cc09bb08 | -11.269 | -54.0334 | 2026-08-28 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 2a803dbf-fdcc-3924-9bcb-cec2774ef348 | -14.1645 | -52.8269 | 2026-08-28 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 343.4 |
| 3cd35b54-2a4c-3f40-a7f6-f6dfe2030bc3 | -5.9245 | -52.1251 | 2026-08-28 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 14b5da43-727c-3b3b-8214-7f10a84a81e0 | -10.4082 | -61.23 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 8ba9f13a-6b2a-3cb4-8421-24b5d13e0b4b | -10.3708 | -61.232 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ecbf7554-5e7d-315a-9dda-33502cf8c3f2 | -10.3894 | -61.2502 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 223.5 |
| b5a1d1e4-3bce-378d-a5ee-35a892fd9f2f | -7.2474 | -45.846 | 2026-08-28 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 0887e32b-e6cb-3fd2-b76f-0065a3264ff8 | -11.2879 | -54.0317 | 2026-08-28 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 197.1 |
| e7f78515-fd46-31c8-ae19-90e064f69776 | -4.8397 | -45.3926 | 2026-08-28 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e7d3a608-75e2-37e3-89dc-c89fdd5551d1 | -8.5783 | -54.7768 | 2026-08-28 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 13d93b5b-83b6-3f08-afcf-c4368f4f122c | -14.8631 | -52.5893 | 2026-08-28 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2a0f8535-70d2-312f-86a4-534f456d6044 | -15.5403 | -41.9175 | 2026-08-28 01:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| ee52bc13-a605-3120-ac47-014eec3e8283 | -14.8627 | -52.6106 | 2026-08-28 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 0299d23f-04c9-321c-adbf-a1cea04a715b | -10.4981 | -64.5005 | 2026-08-28 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7dcd225a-f4eb-3e69-aa51-76a7d7c2444f | -11.7357 | -54.5227 | 2026-08-28 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2bb44a73-4a02-358f-92a1-f456bccabd94 | -12.4305 | -43.3944 | 2026-08-28 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 182.5 |
| e8d8d1d9-625a-3c96-ae00-49461ca636e0 | -10.3707 | -61.2513 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e31fff20-c63d-3f09-9e49-c9e4de3f110b | -8.5968 | -54.7957 | 2026-08-28 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| d75e3946-193d-3d6a-88d4-33ac074c9fa1 | -7.2661 | -45.8443 | 2026-08-28 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 319.0 |
| d46acb79-b30c-3ed9-8e3b-0f28566b155d | -7.2659 | -45.8668 | 2026-08-28 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 581.2 |
| cd041c91-d352-379f-9d24-7a8e9d09c4f8 | -10.7596 | -54.0384 | 2026-08-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 42d27889-d512-3d21-a454-25c5fd6fe198 | -12.4494 | -43.415 | 2026-08-28 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| dd992d47-7d3d-3f1e-86b7-54dd190b9d34 | -12.4107 | -43.4214 | 2026-08-28 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 32acbde2-1d43-31f6-8ade-de8ea26c35e4 | -7.2657 | -45.8893 | 2026-08-28 01:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f13fa7c9-d8d3-3f58-92d0-a3f2518feeaf | -10.3895 | -61.231 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 200.7 |
| 3ac2b82a-4e38-35f8-a7a8-c623f55f4424 | -14.1649 | -52.8058 | 2026-08-28 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 30a691f3-9af5-31ae-b4da-87400524f234 | -10.4081 | -61.2492 | 2026-08-28 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 37dba795-b18c-3de5-94be-7855b41e3881 | -6.5322 | -55.2577 | 2026-08-28 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c7e340c0-84e9-3241-b3d9-199baa62875d | -11.2317 | -53.9958 | 2026-08-28 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e72a2468-e559-37e4-b2bc-3554802d1c58 | -11.8239 | -47.2178 | 2026-08-28 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d9fb9b4c-22cf-392b-afda-f7fa307d3503 | -6.1656 | -57.7988 | 2026-08-28 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| ab719284-bad0-306c-84cf-3e1502f445b7 | -7.2471 | -45.8685 | 2026-08-28 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 398.0 |
| 5b8fe342-d64a-3d07-abdf-95e06ba31e66 | -14.1838 | -52.8245 | 2026-08-28 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 325.2 |
| db6cc3a2-645a-38f7-854b-1ed42495ccef | -8.5969 | -54.7755 | 2026-08-28 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 7eeb8735-1156-310a-b2ba-2c305f5b0b7c | -4.8583 | -45.3915 | 2026-08-28 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2de2aa7f-5a8f-33de-aa97-a0641dd2f0ae | -11.2693 | -54.0129 | 2026-08-28 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| f51f0e5c-03d4-3509-82c1-16da62db1fe2 | -12.43 | -43.4182 | 2026-08-28 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 9c87522c-a93a-3dc4-8135-4f02a714bdcc | -14.1841 | -52.8034 | 2026-08-28 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 9a99c3f7-931d-3ace-b046-17351e73a8f1 | -6.1472 | -57.7995 | 2026-08-28 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6258fb3c-5d1d-38bb-91e6-85bc07cb7a0b | -6.1657 | -57.7793 | 2026-08-28 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 66686ef5-4de3-3680-b8c8-735b8459395a | -11.2882 | -54.0111 | 2026-08-28 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| a87a1e45-c849-3298-938c-d461abdc7deb | -13.4698 | -57.046101 | 2026-08-28 01:36:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6e5fbb1-7e93-334b-ae5e-c344dbf33bb9 | -8.6312 | -66.540199 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e997f1b-de94-3944-9ed4-1d1e808cd75d | -14.1748 | -52.819 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd585a56-1b82-3757-ae67-e4501af221a7 | -8.5922 | -70.192703 | 2026-08-28 01:36:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4d834aa0-2a69-33dd-a021-f229072b01f5 | -6.2686 | -53.122898 | 2026-08-28 01:36:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebfb639-a53d-3347-b559-db1714d3cdb7 | -11.7243 | -54.534698 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d614e45a-6d79-3214-8c0e-e41b6700b6f0 | -6.7544 | -55.6931 | 2026-08-28 01:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ccc073-55a6-30b3-b44b-aaeaa0215abc | -6.7506 | -55.6777 | 2026-08-28 01:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef1ae86-0e83-3101-af69-12ca19c811f5 | -6.1734 | -57.7976 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a5790e1-69ad-38b6-bed5-e0e0304aaed0 | -6.2359 | -55.4673 | 2026-08-28 01:36:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76d48c23-dda9-30bd-b96e-3e9b05fb7b66 | -16.151501 | -58.604698 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95ad6dc6-64d5-3f63-8b81-d107addb80a8 | -14.4152 | -52.5933 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a200100f-5dfd-3125-a868-6bd39eca5984 | -9.6128 | -55.127399 | 2026-08-28 01:36:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4168809b-43d3-3875-93ba-99b262cd1e55 | -11.2143 | -53.995602 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca12324-8d80-3197-b4bf-00254eb96077 | -11.2714 | -54.016899 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 338b7ba8-5173-3422-bd44-3370add6fdb4 | -10.5056 | -64.497704 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50835e99-3dd9-3af1-a372-c132f74d6ba4 | -9.6089 | -55.112202 | 2026-08-28 01:36:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7e151e9-de21-374f-8472-b2d3e1558bff | -6.9428 | -58.946602 | 2026-08-28 01:36:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5b2840-b497-36a7-8738-649b585b0f71 | -8.5912 | -54.796101 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 770ff131-e258-3a6c-95b5-d7f356dabb1f | -14.869 | -52.625 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a333169-5403-3eb1-90ae-340a3117fdee | -9.8244 | -63.007801 | 2026-08-28 01:36:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 82425599-9078-3acf-a4ac-23b083929407 | -10.3811 | -61.240398 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f86eca32-faf3-368a-89c8-6fbf7a0304ca | -21.0431 | -57.851601 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9a945263-bb8f-348f-b320-b941b2a82190 | -9.8476 | -65.011398 | 2026-08-28 01:36:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb909634-ab4c-36e1-8774-f927e9337577 | -10.7473 | -54.0266 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4fdf6d7-0988-3aac-8d44-dc35bf774060 | -9.9737 | -53.9464 | 2026-08-28 01:36:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 474d37d1-f7aa-3b5d-9b3c-34e1032a06a5 | -11.2337 | -53.990601 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98555931-19cb-311f-86ab-74f39c1faf95 | -6.7603 | -55.675301 | 2026-08-28 01:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c734a3-176e-3493-b801-03baf357b387 | -11.2811 | -54.014301 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93ed6e88-ff7b-3764-8570-2aa0d771386c | -14.1844 | -52.816299 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0806f4c-4890-3c27-954c-0935a7f6ab50 | -13.4795 | -57.043598 | 2026-08-28 01:36:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd4fe958-8f1c-34f9-9079-cc8d4ef7fec8 | 2.0223 | -61.464199 | 2026-08-28 01:36:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ccb28edf-e1af-38b3-ae6a-97ae8d34507e | -9.5408 | -66.765099 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edf5f85a-dce1-3419-9eab-79091e527057 | -22.052601 | -56.077499 | 2026-08-28 01:36:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 430c5165-c35a-3687-b300-ed53008cbf62 | -16.1576 | -58.586498 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 405da03e-471f-3ed0-984b-375c351b152a | -10.4974 | -64.5075 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64c50b3c-1253-3b23-a06a-e5f52d47516d | -6.1539 | -57.8022 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 978ac2d5-623e-3b5d-947c-ff59ce790fa5 | -16.1478 | -58.588902 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d40c5ab6-6141-30e1-9f74-34e07e5e9d70 | -11.2854 | -54.0312 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 088fea9d-bedb-3369-8135-0fbd6d9c332a | -8.9841 | -65.430298 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c399a9be-4992-38d8-a50a-3294bb750ff8 | -8.5953 | -70.207802 | 2026-08-28 01:36:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3b05e873-befc-3e50-a1ed-8192250b8505 | 2.0203 | -61.473 | 2026-08-28 01:36:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d18dcbf1-b730-36fe-8eff-f92aa3534510 | -10.7614 | -54.041302 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3431ea1-3e93-34ae-8980-61cb0d13faee | -8.8846 | -66.905403 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0a4a0f2-df78-3d0b-8e31-bccab23f6cbf | -8.6391 | -66.529099 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6735c194-65db-32f0-9b67-7e94bf120d3d | -15.8389 | -56.447399 | 2026-08-28 01:36:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5730756-a52e-3eb9-8c90-6db8622c82ed | -9.6225 | -55.124901 | 2026-08-28 01:36:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| baf580d7-b74a-3ecc-b2d3-75f4777da074 | -8.641 | -66.538002 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26774b11-4c49-3ceb-ad0d-a9e10226e367 | -8.8825 | -66.896004 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc1ee89-9fe2-3ca8-984d-cb92850c516b | -8.8727 | -66.898102 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34cc075b-8ac5-3484-819e-f03fb4174f0a | -10.3535 | -64.460297 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd94f60b-8e1b-3782-a7b0-79e0fa8a8b62 | -8.9956 | -65.435997 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1bdc6a7-0b03-37d4-b8e6-5112ae46ce9a | -10.4958 | -64.499901 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c4e388e-0631-3f84-be82-e22fe4f94776 | -6.5292 | -55.2384 | 2026-08-28 01:36:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efc9f753-633f-3f24-8493-a4764d8f5674 | -11.6612 | -50.4646 | 2026-08-28 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6353255f-ce6b-323d-8d95-34f6f081faf7 | -10.3893 | -61.230999 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5dcda8d-3ad8-30d4-b6b9-4e308c35df30 | -6.8362 | -55.607399 | 2026-08-28 01:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12d1dbd1-660d-339f-8f9f-66691d52173d | -14.9028 | -52.595798 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
