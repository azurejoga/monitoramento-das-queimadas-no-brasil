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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 913a9fda-1884-3f7f-84fb-02b5252396b9 | -1.4944 | -54.2563 | 2026-09-05 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8bca04c9-be83-3c84-8df6-4d72fc5b725f | -7.2158 | -43.6069 | 2026-09-05 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 922e7caa-2a60-385c-a68d-32bd8ed13058 | -11.2764 | -45.7113 | 2026-09-05 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 6fa66ed6-6da6-3864-be25-0f12eea78316 | -3.5407 | -48.1673 | 2026-09-05 15:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| a0d8f4b8-de22-37c5-ad0a-fc2bd1d4ff92 | -1.4761 | -54.2565 | 2026-09-05 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 694e2885-5392-37b3-b063-9a7e688d149f | -7.6765 | -46.0771 | 2026-09-05 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 85d1d8f1-b084-32d2-96b0-437654b3d8d9 | -3.3688 | -59.4079 | 2026-09-05 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0f338731-a594-3981-83e8-e534804b2e48 | -4.667 | -55.6152 | 2026-09-05 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 29bb54a1-8b84-3606-afde-39ac2634c34e | -3.5592 | -48.1666 | 2026-09-05 15:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| f50de1a8-6320-3e53-9477-ac2e655ecc20 | -3.4269 | -58.3104 | 2026-09-05 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 06f20460-c1ab-36b4-a794-e1f0971457f4 | -3.1816 | -61.1235 | 2026-09-05 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ffb93542-552e-33e0-859f-88c2cc551ae5 | -1.4944 | -54.2563 | 2026-09-05 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 07f968c6-d28c-3605-8773-04afae488bca | -6.1107 | -57.723 | 2026-09-05 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 946dcee8-e22e-3854-899b-f669a1275f33 | -17.6202 | -44.2011 | 2026-09-05 15:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 58b4a176-1fac-3a65-8dfc-1403dc266a1f | -5.1802 | -56.0518 | 2026-09-05 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 53ca2458-427e-3ce4-8165-4ccaec0e8ad4 | -3.7828 | -61.7545 | 2026-09-05 15:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 9f7aee87-301a-3273-8fc4-214f8691cf90 | -8.7817 | -46.4623 | 2026-09-05 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4183fd61-59e9-3666-b96d-7979f5b0c1e7 | -4.9238 | -55.8041 | 2026-09-05 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0022ef3b-38da-3fbe-9841-de0dd24ca3c5 | -17.6202 | -44.2011 | 2026-09-05 15:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| faeb1613-8a28-3f1c-9558-0f53be3c3b02 | -6.1107 | -57.723 | 2026-09-05 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b4eb4ff8-3afc-3ced-a6c3-7f7cd695f8fd | -3.1816 | -61.1235 | 2026-09-05 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2222b025-45d7-3001-b1ad-89c47dd760f9 | -3.5406 | -48.1889 | 2026-09-05 15:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 330.2 |
| 040016ff-0385-35d0-bc0d-807a35e2a92d | -5.3462 | -56.0256 | 2026-09-05 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 639.6 |
| 5d79e153-95ca-390d-8579-6f79d2406492 | -5.3093 | -56.0271 | 2026-09-05 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f8308718-c3cc-3f0a-a7dd-4f30f9d638da | -3.7828 | -61.7545 | 2026-09-05 15:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 6d9895cb-a02b-3a34-a648-c70f7de764be | -10.0527 | -46.1183 | 2026-09-05 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 1f7d2f9c-5ba8-3bc0-8ee9-1d2298b746fb | -3.4269 | -58.3104 | 2026-09-05 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6cb4611f-f24f-3db1-995b-25daa47a1d53 | -3.1462 | -60.6506 | 2026-09-05 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 01375938-213c-3c26-a4d4-a8984a06453d | -1.4761 | -54.2565 | 2026-09-05 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 43678647-40dd-3bd1-bbcb-e1797029812e | -5.3094 | -56.0073 | 2026-09-05 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8fec9d44-6f84-3d1d-91e4-1c8c7d64ffd6 | -9.0097 | -69.422 | 2026-09-05 15:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ffb14d2c-cb5c-3d98-b716-dd1ea376ea88 | -5.35 | -56.04 | 2026-09-05 15:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1122e83-ee1b-39c3-a7e8-cc205f2226b1 | -5.35 | -55.98 | 2026-09-05 15:15:00 | MSG-03 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 499e2dc7-c992-374c-a967-7acfdcb7929d | -1.476 | -54.2765 | 2026-09-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0a33c9be-6af5-32c7-8768-bc2844db9706 | -5.3462 | -56.0256 | 2026-09-05 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 609.4 |
| ee089836-b5e0-3339-843c-364f77b6bfbb | -3.7828 | -61.7545 | 2026-09-05 15:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| ab921613-7440-35d2-b20e-8b4fed7f98ae | -5.3093 | -56.0271 | 2026-09-05 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c07e58ed-8c4e-39de-adff-c59903c9ec6e | -3.3688 | -59.4079 | 2026-09-05 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0912278c-ae34-3d47-a50e-923dd14d217a | -1.4761 | -54.2365 | 2026-09-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1d44a70b-e1e5-3cd7-b40c-41d31eca89c1 | -17.6202 | -44.2011 | 2026-09-05 15:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 372a1eef-5c2f-3235-b862-55c4eee09318 | -1.4935 | -54.8155 | 2026-09-05 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2b3f8157-f9e8-3575-83bd-546350f38e03 | -11.2764 | -45.7113 | 2026-09-05 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4ef377e6-e08b-3520-bf50-863b1be20bb4 | -5.346 | -56.0454 | 2026-09-05 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 420.3 |
| 69d87093-e687-3cc4-9284-612d80ef86e8 | -1.4944 | -54.2563 | 2026-09-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a1aca958-d4a2-3c80-8345-5c142643d75b | -5.3094 | -56.0073 | 2026-09-05 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3b034499-33c8-3178-97bf-c477ca252fcd | -3.1633 | -61.1427 | 2026-09-05 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 409a644a-edb4-39ee-b417-93cc9f0f38a5 | -1.4761 | -54.2565 | 2026-09-05 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 251fb023-89b3-32a0-a864-d5dbc76cf008 | -9.0097 | -69.422 | 2026-09-05 15:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2f5994ae-07b5-3545-9af2-e98051178334 | -1.4752 | -54.8157 | 2026-09-05 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3ffc3ecf-277d-30e5-b2de-2365585aed3a | -3.4269 | -58.3104 | 2026-09-05 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1679635c-8566-3b0d-9897-26fb05cadf00 | -3.1816 | -61.1235 | 2026-09-05 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1ac71df3-9c2d-3bac-b5a1-febe7eb31298 | -5.3094 | -56.0073 | 2026-09-05 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 58da7c0b-a629-357c-9a7f-3adfc3528d5f | 0.9568 | -60.6559 | 2026-09-05 15:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b2f5a0f4-8854-3728-bb5b-a7c989794cbd | -20.7728 | -57.8865 | 2026-09-05 15:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 553fc572-af30-32be-a5a4-0ddd858596b6 | -3.7828 | -61.7545 | 2026-09-05 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 95a18fb6-0805-30af-87b9-6d72c8598d02 | -1.4761 | -54.2565 | 2026-09-05 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| bf00a5c5-c09a-3f43-b673-0c46f9fc05ba | -3.4002 | -61.3276 | 2026-09-05 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e14906e1-849e-335b-9014-0e289d17a5e2 | -1.4752 | -54.8157 | 2026-09-05 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 0676085c-5aac-3f04-ab11-1aee2f6e2375 | -5.1984 | -60.0321 | 2026-09-05 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 74d8da87-5875-3df1-a714-137cfb08feba | -3.1816 | -61.1235 | 2026-09-05 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 355af019-ba1e-3829-8762-f4997e07ebdf | -3.3688 | -59.4079 | 2026-09-05 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 3bb74daf-4d15-3472-97b6-b18eb9742e46 | -5.291 | -56.008 | 2026-09-05 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d0d5c3c2-9513-3b30-9fa5-e07aa1e2af37 | -3.387 | -59.4266 | 2026-09-05 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a532176a-c6fd-31d4-ad09-0bb194fb0a72 | -1.4944 | -54.2563 | 2026-09-05 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 758b631c-0858-364d-8364-f3d959c94d58 | -11.2764 | -45.7113 | 2026-09-05 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| cb8e9b74-fede-3fa8-8505-b2b2c0b0addc | -5.3093 | -56.0271 | 2026-09-05 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e8525a35-f610-30fc-8082-d77f5b0c51eb | -3.7827 | -61.7733 | 2026-09-05 15:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 262.0 |
| 3effbd0d-44af-3e14-8c73-dcc29605b0e5 | -3.1462 | -60.6317 | 2026-09-05 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2f89dd95-21a3-3372-8b18-fd3ea467c33c | -9.0097 | -69.422 | 2026-09-05 15:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 8cc831f8-63bf-3cad-819b-be8753af9d38 | -3.1816 | -61.1235 | 2026-09-05 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7b4f0dbe-3c79-3173-8d07-0ce419b7f568 | -9.0097 | -69.422 | 2026-09-05 15:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 43d70705-e1cd-33f9-9afc-372caa182fb3 | -4.667 | -55.6152 | 2026-09-05 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 3c841af6-fb8e-3967-8746-b189201e1a55 | -11.5479 | -45.4676 | 2026-09-05 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 25f75bc2-6727-3e7d-ae16-a085bfb896c9 | -3.4269 | -58.3104 | 2026-09-05 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 62816a0e-4131-3be3-98d2-469d80018a52 | -1.476 | -54.2765 | 2026-09-05 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 175ec6f9-dbfe-342d-bc3e-dc6fee271117 | -1.4761 | -54.2565 | 2026-09-05 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| cf4d5fdb-7c4f-386d-92fd-18edce956083 | -6.1107 | -57.723 | 2026-09-05 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a19cd8b3-9bf6-3b93-a84a-2d19ee9fe056 | -3.7828 | -61.7545 | 2026-09-05 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 190.8 |
| 32ec85cf-35b8-38fe-b0e1-4fe5c09690d8 | -5.291 | -56.008 | 2026-09-05 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 07d63987-0e79-3c81-94b3-b5a74601560a | 0.9568 | -60.6559 | 2026-09-05 15:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5612c485-ce5a-3f13-8c2c-38348ac50135 | -3.3688 | -59.4079 | 2026-09-05 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d58ad4ff-1eba-3daf-bc0b-039796ad58c7 | -4.1308 | -56.3237 | 2026-09-05 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1afe629c-d394-3307-8bd9-95cc6417fdd2 | -1.4752 | -54.8157 | 2026-09-05 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 69faf947-3cd6-3d0a-87bc-6ecee3dd8323 | -1.4944 | -54.2563 | 2026-09-05 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 7856137b-bb7a-3e9a-b2ed-8b6ba89e2c22 | -1.4761 | -54.2365 | 2026-09-05 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 10261c91-c5ae-36a6-8ab2-f7d8f8aa1ba1 | -4.4855 | -55.0848 | 2026-09-05 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |


