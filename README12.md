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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1d83d0a-7272-37e0-82a7-7d3d1437bb1d | -11.896 | -47.476 | 2025-06-16 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| affc8b49-fd09-3b69-a036-af684f7315b6 | -6.204 | -43.3241 | 2025-06-16 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9c5191ff-1fc8-3350-97e4-930f6be62b74 | -12.2224 | -44.2073 | 2025-06-16 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| f09fc9d4-80f7-3d9e-a70a-c986972a8ff8 | -6.2228 | -43.3226 | 2025-06-16 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 135.4 |
| fa5bf7a3-7f7a-33a1-a3f2-9107094849f0 | -6.6562 | -43.1916 | 2025-06-16 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 1b6a39c3-9eac-3afe-9420-b0829258cb54 | -9.4161 | -48.4286 | 2025-06-16 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 006947ba-e868-3db4-954c-611ff3447f9d | -11.0093 | -50.7597 | 2025-06-16 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 30834c21-95f8-3aba-8894-1b3cab3b8f03 | -6.675 | -43.1899 | 2025-06-16 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 4c89895e-92b7-38fd-8455-24abf4c0db24 | -6.2226 | -43.3459 | 2025-06-16 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0af7e1b9-7a3a-3bfc-9634-56ec60e566eb | -13.9471 | -54.4386 | 2025-06-16 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b80ac3b1-c84c-31f8-bb1e-869f7e877108 | -11.0093 | -50.7597 | 2025-06-16 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| aba9887e-ab67-3676-9ca8-327d54b3aa5e | -13.9471 | -54.4386 | 2025-06-16 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3fae03cd-835e-3681-8b82-1aed6ddd7ba8 | -9.4161 | -48.4286 | 2025-06-16 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 63c813cc-2c5b-3fad-b741-af3b079463c7 | -11.896 | -47.476 | 2025-06-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 69ff41d7-f0f6-3a61-bb97-f26d6624b0c3 | -11.8963 | -47.4537 | 2025-06-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b690790a-2716-3bdf-8cda-b9ac0fc44c71 | -6.675 | -43.1899 | 2025-06-16 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 104.8 |
| d2c3bc59-6906-378e-af11-3ffebd457f71 | -9.3972 | -48.4305 | 2025-06-16 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 0ca6c289-0040-31d7-9d04-62db5cafcb33 | -6.6562 | -43.1916 | 2025-06-16 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 57a2a326-fc2b-32b1-ad52-cd7a583fd1af | -6.204 | -43.3241 | 2025-06-16 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9a6a7628-19cd-3770-ae02-e64703569356 | -14.0166 | -46.1848 | 2025-06-16 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4b701433-7acf-3494-b6ca-4b10bf5944f5 | -10.8696 | -54.2947 | 2025-06-16 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 3cea29bf-69a5-391f-89bf-6e08117f0c9f | -12.2417 | -44.2042 | 2025-06-16 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| b897bf0a-cc21-3b6c-8a67-f9da4184a1fa | -9.4161 | -48.4286 | 2025-06-16 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e7742a76-dfd0-3c15-a70c-1d06b6d521a5 | -6.6559 | -43.215 | 2025-06-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 17d6c9ec-d568-3e44-8bc0-eecfa171b9ad | -6.204 | -43.3241 | 2025-06-16 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| cb9e2e84-9c87-3982-ac6d-80cbf9097fbd | -9.3972 | -48.4305 | 2025-06-16 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b8b04e06-eea6-33f6-b7c4-ccca2de481ac | -6.6562 | -43.1916 | 2025-06-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 913c897b-9e27-3dd7-bb6c-2306c1dc7729 | -6.2228 | -43.3226 | 2025-06-16 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 0c589684-f6c4-3186-b15d-e282f87afc05 | -7.1969 | -43.6087 | 2025-06-16 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| edff1457-a566-366f-9d72-faffc0fee88c | -13.9471 | -54.4386 | 2025-06-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7af1845c-8cc0-3295-ad6e-9d67ab053696 | -6.675 | -43.1899 | 2025-06-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 124.4 |
| b5309810-620c-317d-b0ad-172c81f6f2ed | -13.9663 | -54.4364 | 2025-06-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f7271d3f-3da9-30c1-9cb0-027ac9b067b9 | -6.2226 | -43.3459 | 2025-06-16 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e1e9dc9c-3410-374f-b28e-599ed5cf1f77 | -11.896 | -47.476 | 2025-06-16 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| bed7ede3-7b86-3736-96e7-e8ca90182ba2 | -11.0093 | -50.7597 | 2025-06-16 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5584f904-97f1-3647-aeb7-8b7d98fea711 | -10.8696 | -54.2947 | 2025-06-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| a40ec76a-0dbc-3699-b8e1-38b64b38675a | -6.2226 | -43.3459 | 2025-06-16 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3bef7e7a-a853-3b69-9edc-273a1fef97c1 | -13.9663 | -54.4364 | 2025-06-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1f09723d-d53e-3bac-a595-b98607505f5a | -6.675 | -43.1899 | 2025-06-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 117.8 |
| e1cd4107-47aa-3b08-96eb-0fe584d5e5da | -6.6559 | -43.215 | 2025-06-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 92.7 |
| a3bdfc35-13fe-37a2-b323-85c770ef2b58 | -11.896 | -47.476 | 2025-06-16 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 79b2018b-9fda-37e6-840f-dba8076200b2 | -10.8696 | -54.2947 | 2025-06-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| decc7fef-094f-35d1-9763-06b66a6018a1 | -9.3975 | -48.4086 | 2025-06-16 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7194b47e-f1e7-3adf-90a1-87ade439a877 | -11.0093 | -50.7597 | 2025-06-16 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| d9c27d78-fd2e-3233-9c3c-89344cf2e2dc | -7.0226 | -44.0657 | 2025-06-16 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 56c88d52-516c-34fc-9d0c-a890a573174e | -6.6562 | -43.1916 | 2025-06-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 108.1 |
| fb054fb8-2346-31ba-91d0-7349309a6e58 | -13.9471 | -54.4386 | 2025-06-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3f8756d7-8dac-3b17-9ba5-b4ae83020fef | -9.4161 | -48.4286 | 2025-06-16 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c65658ef-812c-3984-bb34-73c0cfe5b10c | -9.3972 | -48.4305 | 2025-06-16 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| cb253cea-ae6c-3124-9a21-345c95d80596 | -7.1969 | -43.6087 | 2025-06-16 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d76d472a-2491-3cd8-b4a4-59f2f9acba2c | -6.204 | -43.3241 | 2025-06-16 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| af1464f4-3521-370b-8dc2-a5a9c443e621 | -9.3975 | -48.4086 | 2025-06-16 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6cfe6499-c6b9-34bf-849d-c11ba44fb80e | -9.3972 | -48.4305 | 2025-06-16 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4b293678-40a5-3d0e-813d-efd6581c909c | -9.4161 | -48.4286 | 2025-06-16 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 27ab0c71-b0ca-38a9-8145-f0f9a79c661a | -13.9471 | -54.4386 | 2025-06-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| c74d5a77-2220-32f2-a9d5-e84967daef47 | -6.6559 | -43.215 | 2025-06-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 4a78513c-53ee-349f-a020-c6036c86cb32 | -11.0093 | -50.7597 | 2025-06-16 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9f0bc811-3046-32be-929a-88effef13eb5 | -7.0226 | -44.0657 | 2025-06-16 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ff6eb024-d55f-37e0-ada2-89f8723396ea | -13.9663 | -54.4364 | 2025-06-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dc14ac89-d30f-3556-abb7-8ff8dd6eb6e6 | -11.0271 | -44.6423 | 2025-06-16 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 355729ef-1b54-37fa-89fe-8ee5654c6b12 | -10.8696 | -54.2947 | 2025-06-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 544539fd-010b-3548-a6aa-71930ddc772c | -10.8185 | -46.9458 | 2025-06-16 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9678c7dc-6b77-36c6-949f-a77e1fab47d5 | -7.1969 | -43.6087 | 2025-06-16 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 10b46754-9b3c-3d09-abb1-d1698a604c65 | -6.6562 | -43.1916 | 2025-06-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 92.9 |
| cdb1d2e2-74be-3ef6-b770-55d3ab3a4b10 | -6.675 | -43.1899 | 2025-06-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 1994ae41-af61-3a71-a73d-b02f973c47f3 | -11.0093 | -50.7597 | 2025-06-16 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 096b4fb2-97f1-362f-931c-0f50085d20d9 | -9.4161 | -48.4286 | 2025-06-16 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ee1bf92a-9d2c-3df2-998f-21c1b2f1b710 | -11.0275 | -44.6191 | 2025-06-16 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9cfa0783-67a2-3287-b9cc-58ea5a7b793e | -7.0038 | -44.0674 | 2025-06-16 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 8c031142-7d10-3957-a7fd-4ab488664d3d | -9.3975 | -48.4086 | 2025-06-16 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |


