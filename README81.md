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
| 5ba806c7-368b-34e9-8694-f14ace3e25c5 | -5.2547 | -55.9105 | 2026-08-31 10:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4a01cd9d-8aaa-3a61-a777-b419fbe30126 | -6.6036 | -58.5972 | 2026-08-31 10:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 91436d77-a659-3a3b-977d-e379f6cc8a4f | -5.2547 | -55.9105 | 2026-08-31 10:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 51ef8c90-ba0c-3408-b1df-981f6ff87c99 | -5.2547 | -55.9105 | 2026-08-31 10:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4d7cba61-d616-3ca8-ae97-7ee7b9e65b54 | -6.6036 | -58.5972 | 2026-08-31 10:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 5e145f65-dd7e-3ec8-a8b5-8a6de2b4fd9a | -19.154 | -57.3978 | 2026-08-31 10:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 797912b4-3138-3d62-a412-77e7f4eaac80 | -5.2547 | -55.9105 | 2026-08-31 10:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0bb9ffd8-c700-3c50-a1a2-5427ceff1a7b | -19.154 | -57.3978 | 2026-08-31 11:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 40007175-b084-3e02-b9c3-b0931f19b93a | -6.622 | -58.5965 | 2026-08-31 11:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e7898154-77c2-3d6f-b8bc-9e15fa52fd5e | -8.7442 | -46.4437 | 2026-08-31 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c487398b-6569-3b45-a342-34c3bd295f6b | -5.2547 | -55.9105 | 2026-08-31 11:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e4630193-183f-39a8-837e-8e54aed941e9 | -6.6036 | -58.5972 | 2026-08-31 11:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 3fb6680e-3e95-3bf7-b0a4-bbe4bf3c8b46 | -8.7442 | -46.4437 | 2026-08-31 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 471e24e5-11c5-36a7-ba85-34dc277e41f0 | -6.1294 | -57.6833 | 2026-08-31 11:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 2f1480c3-04e3-39ca-90c5-f18067de22a2 | -6.6036 | -58.5972 | 2026-08-31 11:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 6b66a353-34b9-3bb1-8a33-70ce446c756d | -19.154 | -57.3978 | 2026-08-31 11:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 46b252d2-1a5b-3a4c-8f4d-1bfd3f3d37fc | -7.9797 | -44.2962 | 2026-08-31 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 20b969a4-b42f-3ee5-ac59-05b04e66db71 | -6.622 | -58.5965 | 2026-08-31 11:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 163b7075-257d-3545-ad8f-8caeb24c320a | -6.1294 | -57.6833 | 2026-08-31 11:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 323c4554-2f25-36bf-8fd4-e0d8338f7d21 | -19.154 | -57.3978 | 2026-08-31 11:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.2 |
| 0984c2b1-75f8-390d-b0ab-95582464f863 | -7.9797 | -44.2962 | 2026-08-31 11:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| a7b73afd-61cc-3915-ac9c-4f75821198bb | -8.7442 | -46.4437 | 2026-08-31 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 357.7 |
| b32feb80-58f9-38c3-ba43-9608867fd899 | -8.7439 | -46.4661 | 2026-08-31 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 467.6 |
| a8e8a139-ca16-305c-b18e-3042823fe8bc | -6.6036 | -58.5972 | 2026-08-31 11:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 61818c8a-8e6d-33aa-af36-0f914a3e84a2 | -8.7439 | -46.4661 | 2026-08-31 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 268.0 |
| ba80d029-13bb-3fc4-9753-1725d3ebb794 | -5.2547 | -55.9105 | 2026-08-31 11:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d345985b-a45b-3f6e-814d-4cddf904692c | -6.6036 | -58.5972 | 2026-08-31 11:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 61317e8a-1d9f-3f13-89ba-61acb5b0a48b | -7.9797 | -44.2962 | 2026-08-31 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| f63d5f0e-dff7-367f-b89d-4e0aa225cf1a | -19.154 | -57.3978 | 2026-08-31 11:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 112c3fd3-c177-31b1-a5a9-01918b364347 | -8.7442 | -46.4437 | 2026-08-31 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 4a9696f4-1385-3141-8188-da3a5ec10f12 | -6.622 | -58.5965 | 2026-08-31 11:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a0a5d9d7-cb18-327f-b6ef-0ac9c086e9fc | -6.1294 | -57.6833 | 2026-08-31 11:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 839848fe-48e3-37da-941e-f9cb4b21c359 | -6.9177 | -55.6967 | 2026-08-31 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a47d8253-1ce7-3041-865e-3ed78222be11 | -7.9797 | -44.2962 | 2026-08-31 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 0e80abe4-a749-3830-a9f1-1bbb821d4872 | -8.7439 | -46.4661 | 2026-08-31 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| bd293b7c-4543-3f54-b430-147bf86bca9d | -19.154 | -57.3978 | 2026-08-31 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 7ce052d0-aad4-30df-a73a-e55c764c5622 | -6.6036 | -58.5972 | 2026-08-31 11:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 0d2c9f51-9a5b-3ba3-9a98-47143df05f60 | -8.7442 | -46.4437 | 2026-08-31 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 8b27a1a3-91e1-3a86-88d7-d376285a38f9 | -13.8563 | -54.0967 | 2026-08-31 11:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| db39d348-f599-3f5a-a668-caf9cfdec572 | -6.9176 | -55.7166 | 2026-08-31 11:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 9a70cda0-4fd0-34b6-95ad-b305d68e7bf6 | -5.2547 | -55.9105 | 2026-08-31 11:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e6b7f55a-8dee-3722-ad74-3a7f88a78daf | -6.9176 | -55.7166 | 2026-08-31 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| f310f469-a661-38c8-923d-aba99280e235 | -7.9608 | -44.2981 | 2026-08-31 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e962e48f-977a-31d7-ae05-5b6a3d4bfff3 | -8.7439 | -46.4661 | 2026-08-31 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 289.2 |
| c08b4b07-121a-3942-afbf-094dff603dff | -6.1109 | -57.684 | 2026-08-31 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 07937079-4acd-30ac-98f4-73e2e0ba62c4 | -8.7442 | -46.4437 | 2026-08-31 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| a828f6d9-ceed-3cb3-b8a6-ae386ec97751 | -6.9177 | -55.6967 | 2026-08-31 11:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 6f109029-b351-37e4-8bff-5f178cae9b3f | -14.4007 | -52.5226 | 2026-08-31 11:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 35835617-97a9-3a83-bea0-6c4ee8b49d99 | -19.134 | -57.4005 | 2026-08-31 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 35468b0b-04bc-344a-9054-f306f70bea73 | -19.154 | -57.3978 | 2026-08-31 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| a71dda2b-7c56-3c8a-99b2-3cb8dbb51a87 | -7.9797 | -44.2962 | 2026-08-31 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 7ffa36e1-7ed4-3c9c-a0db-b6e8b0c19e1f | -7.9605 | -44.3212 | 2026-08-31 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ba7afc1e-56c8-324c-bc2f-f965c7c694eb | -19.134 | -57.4005 | 2026-08-31 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 2eb28ef0-c1a1-340d-ac5f-59f1a6e69c51 | -6.6036 | -58.5972 | 2026-08-31 12:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 3b805f83-14c8-3125-b5a5-78e1fc86dfaf | -6.9177 | -55.6967 | 2026-08-31 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c2762783-70b8-350d-b301-f4d4cddcad82 | -19.154 | -57.3978 | 2026-08-31 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 1dcaa318-1c1b-3d3a-8303-0909f8d6ff32 | -8.7439 | -46.4661 | 2026-08-31 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 06906f2b-1728-387f-82fb-366aa279ca7e | -6.9176 | -55.7166 | 2026-08-31 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e49721ae-541d-3b96-807d-3d375fb6f166 | -14.4007 | -52.5226 | 2026-08-31 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 2ca0544c-cac8-30e1-b8e5-98b459a90338 | -18.27 | -52.7068 | 2026-08-31 12:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d3ed240d-c3a3-3802-bca9-25228ed2120e | -8.7442 | -46.4437 | 2026-08-31 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.8 |
| d98d65f3-d0fb-3a09-a43b-702a13c0d2b7 | -14.4201 | -52.5201 | 2026-08-31 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| edfbfbd4-67aa-3343-9e36-dd4c9bad4d96 | -14.4394 | -52.5176 | 2026-08-31 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 383abc42-2a7f-3c66-9527-5e6543498bd3 | -9.5775 | -47.6224 | 2026-08-31 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c694eac4-62eb-380e-be46-dc9deca3e8e7 | -7.9797 | -44.2962 | 2026-08-31 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 2c638ea5-9094-3244-b85d-a8781a8f374a | -6.622 | -58.5965 | 2026-08-31 12:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| d8831447-6b07-3d1e-bc24-947b3e81465c | -6.1109 | -57.684 | 2026-08-31 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0c563a57-ac9e-3aa7-a7ce-46e69473204b | -14.9858 | -48.1529 | 2026-08-31 12:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 62e527f0-e562-3dbe-b3c9-d0b3250b834b | -7.9605 | -44.3212 | 2026-08-31 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ccff5067-9576-3e5d-bdc5-db579019ff93 | -5.2547 | -55.9105 | 2026-08-31 12:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 37275bd2-36c8-3f1c-9158-fe98c2e377c7 | 2.52079 | -50.85136 | 2026-08-31 12:08:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78d58d22-4cec-3a56-8472-4e607338f35b | -3.53829 | -49.47882 | 2026-08-31 12:08:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9f1e9b2b-ddaa-3b22-9ada-7f6510f7ca88 | -1.62137 | -55.1682 | 2026-08-31 12:08:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9b4b5070-ca6d-3bf4-8ff7-07161e27cfdd | -3.53987 | -49.46746 | 2026-08-31 12:08:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3e477451-e677-3e89-81b3-95f7f3b14a38 | -3.58989 | -48.87884 | 2026-08-31 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7420af5f-cda1-333c-bfff-5c80e3d21fdb | -3.5916 | -48.86632 | 2026-08-31 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6b38d947-3095-3be8-a507-c7658dbb1b81 | -2.55762 | -47.18786 | 2026-08-31 12:08:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 89fec2f1-3ccb-3efc-a428-38f039a2276f | -1.45512 | -54.20304 | 2026-08-31 12:08:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7508882a-556c-33f2-b2ac-f94b204f3f5b | -1.4537 | -54.21281 | 2026-08-31 12:08:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8e6024ed-bd8b-3613-8272-7e81d1fd5aa9 | -2.55983 | -47.17179 | 2026-08-31 12:08:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 80f51d4b-98c4-3b22-a29f-2addcee485c6 | -6.9176 | -55.7166 | 2026-08-31 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c3adc6bc-793e-33a5-85d8-f271ccc3a736 | -8.7439 | -46.4661 | 2026-08-31 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 9e9997d3-79ae-3e88-9ec0-bce9e2ed6c15 | -18.2904 | -52.6818 | 2026-08-31 12:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 376c872a-8e37-362b-9b1d-359381e1e979 | -12.9401 | -45.9241 | 2026-08-31 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 056acda5-3d24-3886-b8fa-c2c0af319c5c | -6.6035 | -58.6166 | 2026-08-31 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 683692a3-4b04-3aba-a0b5-2f312fff26a1 | -8.7442 | -46.4437 | 2026-08-31 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 417ecf8a-6865-32c3-b00b-21fc55321f16 | -5.2547 | -55.9105 | 2026-08-31 12:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 844cfeb6-892a-358a-8b82-c114d81a2c0c | -18.2704 | -52.6851 | 2026-08-31 12:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| c5050b64-f7d8-3cc8-a6c9-b6ab53f297e4 | -18.27 | -52.7068 | 2026-08-31 12:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ea0c46cc-0045-32e6-9de5-866c74d8b0ff | -6.622 | -58.5965 | 2026-08-31 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 6a26aa09-e70c-3b84-94e8-c82c6246e02e | -13.8563 | -54.0967 | 2026-08-31 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 90e43e0f-3cd2-3180-9ee2-69eb9441f71a | -6.9177 | -55.6967 | 2026-08-31 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 52f0fdff-fd29-3203-b210-247672581a07 | -19.1344 | -57.3797 | 2026-08-31 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.3 |
| b63fbef9-7f6e-3c5c-8d58-83df2a9279c6 | -7.9239 | -44.2327 | 2026-08-31 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f9dbf2d8-1494-3f4c-8c61-2d7fc1f0d4ea | -19.134 | -57.4005 | 2026-08-31 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 68fedd95-f6cc-3c7f-97ca-eefb6ad8bd85 | -6.6036 | -58.5972 | 2026-08-31 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| ab225e70-cb8a-3ca1-a156-9ab167148a23 | -14.4394 | -52.5176 | 2026-08-31 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| c51d561b-37fe-31eb-9516-82d29dd02c8a | -12.9405 | -45.9011 | 2026-08-31 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d7f0853d-f3bb-3f98-9199-9c7170d37a22 | -14.4007 | -52.5226 | 2026-08-31 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7de46c31-e8a0-3f65-9d0c-e2678da812be | -14.4201 | -52.5201 | 2026-08-31 12:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |


[Clique aqui para ver as próximas entradas](README82.md)
