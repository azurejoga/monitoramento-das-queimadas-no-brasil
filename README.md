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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6989195-875f-369e-a51e-02313934e673 | 2.2524 | -60.2081 | 2026-03-16 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e9f62254-1a56-39e2-bed6-1baf121e2d02 | 3.1458 | -60.8023 | 2026-03-16 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bb0cebdb-45df-321a-9cab-779492b9f41e | 1.2125 | -60.1611 | 2026-03-16 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fd452b09-eada-346c-8f6f-4200f6ea9d8d | 2.2524 | -60.1891 | 2026-03-16 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 76204277-cfb9-32a4-9355-7e940975dda9 | 3.1275 | -60.8026 | 2026-03-16 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 93fd5d3c-848b-39d6-a5fb-9b9c8f1892f7 | -11.78016 | -47.09537 | 2026-03-16 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 543f942e-cde1-3eae-8cae-bbd2b0a07dec | -6.98521 | -47.07193 | 2026-03-16 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0fef9ab1-6327-39ca-b4cf-aa9aa79f2da0 | -6.98649 | -47.08134 | 2026-03-16 00:03:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 113c7557-51f4-3ef2-b6cf-3f814835a808 | 2.2524 | -60.2081 | 2026-03-16 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e44ca1ea-5acb-3ff9-a670-b2f99f6cfea7 | 3.1275 | -60.8026 | 2026-03-16 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 11900def-6398-36a9-a35b-f1c5acdb3d02 | 2.2524 | -60.1891 | 2026-03-16 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4d16611c-6068-30e5-b62d-ca134e66ae0c | 1.2125 | -60.1611 | 2026-03-16 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8ff4a283-7136-379c-8890-b87d9d4490e7 | 3.1458 | -60.8023 | 2026-03-16 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3ed1c2da-7dd0-3c48-a175-56d61c88b780 | -9.4289 | -40.709 | 2026-03-16 00:14:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 26ab4ea3-1883-3187-848b-3ebee2b9eda2 | -10.648 | -36.943501 | 2026-03-16 00:14:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a47a7189-7da2-3f76-a76f-dfd9bbc93cdd | -10.0191 | -36.303398 | 2026-03-16 00:14:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 5d15d3e0-84c4-32e4-b9f4-7ab543eef936 | -9.4305 | -40.7159 | 2026-03-16 00:14:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 300b2ded-50ae-3185-b16f-181d78eca20f | -10.6459 | -36.9347 | 2026-03-16 00:14:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba921ed9-a3bb-3dc9-9c68-353438bfd31c | -10.0214 | -36.313 | 2026-03-16 00:14:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 2f0425a6-4e8e-39e6-a1b9-e1a34fefd320 | 2.2524 | -60.2081 | 2026-03-16 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c2a85676-eb84-38b4-be9c-ee638eac16b0 | 2.2524 | -60.1891 | 2026-03-16 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 131.5 |
| b00081e0-cd50-39eb-bfd2-018be58ea276 | 1.2125 | -60.1611 | 2026-03-16 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5b97afb7-9579-39eb-8b0a-b4e6a3859f06 | 3.1276 | -60.7836 | 2026-03-16 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1b82a9d9-825b-3790-8fee-dcd74e716973 | 3.1275 | -60.8026 | 2026-03-16 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 72ba713b-a0cb-39a5-b8bc-608d87fc98b6 | 2.2524 | -60.2081 | 2026-03-16 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 25555b62-fcad-3d0b-99a6-ca84e395b345 | 3.1458 | -60.8023 | 2026-03-16 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f84f644d-586b-3d79-8dbe-e928730abd6b | 1.2125 | -60.1611 | 2026-03-16 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e50b132b-04a0-315f-90ef-69a9a0272900 | 3.1275 | -60.8026 | 2026-03-16 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f209fe15-8ef4-3e85-b76d-9606073f867d | 2.2524 | -60.1891 | 2026-03-16 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 415c3b87-dbdc-373c-951d-57e72abfb469 | 3.1276 | -60.7836 | 2026-03-16 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e35e7db8-0806-3fa5-a1f5-e625a450d25b | 3.1276 | -60.7836 | 2026-03-16 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 2fc280ce-b6c7-3ecf-ba04-0032894d0585 | 2.2524 | -60.1891 | 2026-03-16 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3320aba9-6eff-3ac8-921f-0e6db0716ee3 | 2.2524 | -60.2081 | 2026-03-16 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 7c55839f-d2e1-3ba0-8025-57aff8f04d5d | 3.1275 | -60.8026 | 2026-03-16 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 5b248b78-d017-3df1-8e06-508df8c689d2 | 3.1458 | -60.8023 | 2026-03-16 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ab32caab-43e9-3e9c-9fc7-ee75bc672e51 | 1.2125 | -60.1611 | 2026-03-16 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 005814a4-ff6d-3d03-82b6-f8e7a95088a2 | 1.2125 | -60.1611 | 2026-03-16 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 28fa1ff8-9895-3b83-a58a-e95697bb8676 | 3.1276 | -60.7836 | 2026-03-16 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 80c5cca4-ec34-360e-b602-3f98534d7847 | 3.1275 | -60.8026 | 2026-03-16 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5fac94da-14c3-33e7-a4f9-4bfa7123877c | 2.2524 | -60.2081 | 2026-03-16 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d12e025c-4af1-3f98-92b1-26c20acd8329 | 2.2524 | -60.1891 | 2026-03-16 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.2 |
| e65b9feb-e253-3a30-a609-1c295c4f8d09 | 1.2125 | -60.1611 | 2026-03-16 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 56181f78-2e03-30e3-a333-a9af685822e3 | 2.2524 | -60.2081 | 2026-03-16 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 02326d5b-25dc-3151-817e-4fef668cd09b | -10.0072 | -36.3004 | 2026-03-16 01:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| b49704b7-f0c1-3dbc-863b-7833ef23eb10 | 2.2524 | -60.1891 | 2026-03-16 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 9d5c240b-c860-3a1a-8f2b-b669a72f20de | 3.1275 | -60.8026 | 2026-03-16 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b650a371-1cf2-35a2-838b-328cf2465139 | 3.1276 | -60.7836 | 2026-03-16 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| add95d75-2dd9-3ffc-9e76-5b897c0c65c2 | -10.0265 | -36.2969 | 2026-03-16 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 8ecfcc25-43ec-303e-ab6a-2ba2597840ad | 3.1276 | -60.7836 | 2026-03-16 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6be6fddd-60f4-3db9-932b-7ee6dc1ad2e0 | 2.2524 | -60.1891 | 2026-03-16 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ab7fed9e-8924-347f-85ef-54c53ffeb8cb | 3.1275 | -60.8026 | 2026-03-16 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 57d70e52-cd64-3cc3-9dcf-68748b53e1b1 | 2.2524 | -60.2081 | 2026-03-16 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 14a44b36-25ad-3513-87ef-e2bd4815d4fc | 3.1317 | -60.805901 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b9b179a7-ada1-3c52-ab16-4be613bd6ac8 | 2.2555 | -60.202202 | 2026-03-16 01:17:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cdc426eb-a31f-3bca-87cd-70dda07df377 | 2.2591 | -60.186001 | 2026-03-16 01:17:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 89f6ba22-7922-30f0-b26b-1fafcfaa7fe6 | 1.9907 | -61.431599 | 2026-03-16 01:17:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cfb1b59e-d7f3-3307-b6d9-1067f92a14c3 | 3.1385 | -60.775501 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9eef035d-e0d6-3a07-b05f-e75cb458c6d7 | 3.0962 | -60.7822 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 50fdb32d-175c-3e62-84f6-cb8791b164ac | 3.0928 | -60.797401 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 56a95728-358b-3624-b250-e7a5dc1bdc40 | 3.1351 | -60.790699 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 055623fa-6d15-37ff-af67-597b838315c7 | 2.2494 | -60.1838 | 2026-03-16 01:17:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 127821e0-90b3-3791-b171-70561462872c | 1.2142 | -60.155998 | 2026-03-16 01:17:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 42cc241a-e15a-3638-a1e4-8cdaed0050d5 | 3.1056 | -60.832001 | 2026-03-16 01:17:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 06f483c6-3fec-3941-9e52-daceeb05af9a | 2.2524 | -60.1891 | 2026-03-16 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| fd201793-9923-36de-a105-85067de5f828 | 3.1275 | -60.8026 | 2026-03-16 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.9 |
| d29858ef-37fc-3d83-8a75-0167f14bd07a | 3.1276 | -60.7836 | 2026-03-16 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| eed35c21-c2b2-3e34-b6e8-1fb729bcd37a | 2.2524 | -60.2081 | 2026-03-16 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 44eaee8e-3c74-3e55-bfb3-4241f8819caf | 3.1275 | -60.8026 | 2026-03-16 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| eba6a999-3949-3eb3-ba1c-1eb44ec7e833 | -10.0087 | -36.2192 | 2026-03-16 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 130.0 |
| ca27e5cf-f06c-37dc-b443-cc5207b14eac | 3.1276 | -60.7836 | 2026-03-16 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| ce87d00a-83d8-3610-9227-94e74c8d265e | 3.1458 | -60.8023 | 2026-03-16 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8e59fd2e-834e-3aca-a4c9-515e7e6eaed6 | 3.1275 | -60.8026 | 2026-03-16 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7c89f9c5-0c04-3765-bd9e-d87a2f881fd9 | 3.1276 | -60.7836 | 2026-03-16 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a86773a1-660e-3f5e-8985-ffc08e04926e | -10.0087 | -36.2192 | 2026-03-16 01:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 0103ec5c-f165-3a98-9d2c-639522923856 | 3.3548 | -60.369598 | 2026-03-16 01:52:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fdf43500-d8ad-3f2e-aa8d-b775ce470bcf | 3.1275 | -60.8215 | 2026-03-16 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8a1ccbe5-6340-34a8-8bf1-b4c770ddb657 | 3.1275 | -60.8026 | 2026-03-16 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 1bb6d0bd-37c5-3dad-8cd3-b54d39afe61a | 3.1275 | -60.8026 | 2026-03-16 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0914f3e0-5467-3e8e-93df-d87af1646519 | 3.1458 | -60.8212 | 2026-03-16 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 86463d8f-8c72-398e-9442-db9e99c8bcba | 3.1458 | -60.8023 | 2026-03-16 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 157f6e57-1f06-3554-997f-88c97dc9a2ea | 3.1275 | -60.8215 | 2026-03-16 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a44d5351-207e-34f1-99aa-20e1c4fff93a | 3.1275 | -60.8215 | 2026-03-16 02:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| cfb942e0-d8cb-32d7-9b05-10f8dce371d0 | -10.00431 | -36.21033 | 2026-03-16 03:19:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| f667a614-78a9-3627-8e4a-1edc58a175f6 | -7.83402 | -35.16832 | 2026-03-16 03:19:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28189dff-a478-3f9b-86a8-72b9c771442d | -20.22763 | -46.66576 | 2026-03-16 03:23:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c2ab8b-9467-37e5-9b8a-40e6bdb51fef | -6.98762 | -47.07402 | 2026-03-16 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48e775d7-fed6-3afe-9e3d-47dea688f36c | -6.987 | -47.07766 | 2026-03-16 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8141718f-b885-3650-b98b-3646e7dc6111 | -5.56932 | -46.33343 | 2026-03-16 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35893037-acc0-3f8c-940d-f55c1c35a698 | -6.9911 | -47.0784 | 2026-03-16 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d858096b-684c-30f3-9534-b13d0a2328aa | -7.57601 | -40.25846 | 2026-03-16 04:08:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e181241-8343-38ee-8a91-5cf6603f0781 | -8.16517 | -43.16372 | 2026-03-16 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9157f3e3-0c53-3819-8f97-617f7de6a461 | -11.77869 | -47.09373 | 2026-03-16 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 999b16d1-5521-3f14-9ef1-bf6f5ab35d92 | -11.78334 | -47.08961 | 2026-03-16 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 434566d1-8fd3-3283-8ac6-3c9421557148 | -11.77953 | -47.0889 | 2026-03-16 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ddb6521-38f9-3424-8155-2ed549fc1d85 | -11.78251 | -47.09443 | 2026-03-16 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3de15e3-e030-324d-a763-51969ab1fb88 | -20.23677 | -46.64659 | 2026-03-16 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72f129d8-68e6-3054-bd67-0cb5ad4620bf | -20.23008 | -46.66545 | 2026-03-16 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f8e65d-c4a0-36e4-82fe-5520adea51e7 | -20.23347 | -46.66611 | 2026-03-16 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb6fd7f9-40ca-3917-b4c0-4f67730e0659 | -20.59781 | -51.61106 | 2026-03-16 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5a94aca-3c4c-3021-a082-c8bbe7b1918c | -28.87049 | -50.65708 | 2026-03-16 04:14:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
