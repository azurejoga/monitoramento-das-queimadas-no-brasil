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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90205402-474a-331f-afb7-0caa3ae63813 | -9.077 | -66.0881 | 2026-10-05 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| dc3591da-c53e-35dd-9987-235a2a13092f | -9.7313 | -65.0757 | 2026-10-05 18:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| a7eb2a55-4352-3621-b59e-3025f6e9b238 | -5.9606 | -41.3507 | 2026-10-05 18:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 668.1 |
| a5ab0014-5ed5-3e22-8dff-1f7edc5f4f26 | -9.2199 | -67.3852 | 2026-10-05 18:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| da2dd343-365d-33fa-b81e-003bb981c023 | -9.3494 | -67.4374 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| bba8298f-1cfa-32f3-80d4-9df7a24c9eaa | -9.0429 | -65.4361 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 5779243d-8325-3fce-ab45-fc5c3955b01e | -9.1334 | -65.9 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 4843e22f-a062-3cd2-aa4c-12c89434685b | -9.1257 | -67.8322 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 00713081-a66b-34bb-86c9-24ebdf26d8a2 | -9.1333 | -65.9186 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| e56b5c63-a527-39a4-95e8-5dc998032227 | -9.899 | -65.0132 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 59271651-91ea-3859-87b7-f8d848f20d80 | -2.5353 | -65.8819 | 2026-10-05 19:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f5dfe1a6-5221-3737-86df-f2099a4eafc0 | -9.1076 | -67.7215 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bba93b46-3291-3956-a7b8-09b72dc9d01a | -9.1072 | -67.8141 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 154.4 |
| b55f5803-2626-30cb-ad94-8e6b184aca08 | -6.4279 | -43.4686 | 2026-10-05 19:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 676c0c55-e6d3-3057-90de-9509d46b75d4 | -5.5311 | -41.0236 | 2026-10-05 19:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 79aa3959-29c6-3df3-86c9-2e6751a89d06 | -4.8081 | -42.1577 | 2026-10-05 19:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 182.9 |
| 1623053c-5466-3de3-9df1-05b83765a5b1 | -9.1428 | -68.2387 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0500fbb1-05a0-3cd7-96ca-559c9c3f79b8 | -4.8083 | -42.134 | 2026-10-05 19:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 189.4 |
| e0bcd4a1-2e7f-3e40-905a-45beadb0b9d2 | -9.3431 | -64.7143 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a0fba4cf-7cd7-348d-b7b8-b1bb907a2f51 | -8.6214 | -69.5026 | 2026-10-05 19:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 307b76d5-c335-30c1-9767-483acab47f77 | -9.1613 | -68.2568 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 7b5f3421-6a3a-3c4b-badc-0619003852c2 | -8.852 | -66.7827 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 44a69f2e-a8e8-39ac-96e5-3ce23abc525e | -9.1253 | -67.9432 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ee27c0f1-46f5-3f45-a219-8f193110774a | -9.006 | -65.4 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d9965b94-d58f-3d93-9ef6-c5a744dc2f3a | -5.9417 | -41.3524 | 2026-10-05 19:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 0b94f5b3-4a6a-356b-883f-115154c73e73 | -8.8704 | -66.8007 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a433ed82-8347-37fc-8872-7829baeb6f92 | -9.0769 | -66.1068 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 46d3f1d3-db6b-3220-ab66-7fd6b0805c59 | -9.5004 | -66.7831 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 71d17770-c3cb-3fcf-9f89-24dbc8da058e | -9.077 | -66.0881 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 71f00c11-3e0a-3829-930e-b03f0792df7a | -9.6672 | -66.834 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 054d6049-72d8-3910-afcc-bb89bd67c52e | -7.47 | -42.8078 | 2026-10-05 19:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 9f9594d2-c868-356b-b4af-a47f5464ae0a | -8.593 | -66.8081 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.0 |
| 0460fa43-cb06-3d0a-83ce-32f93099cb96 | -4.5091 | -42.0584 | 2026-10-05 19:00:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 6b5959dc-e010-3321-a813-9393c9b3316a | -8.3526 | -62.8302 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 3edb45bb-a5e7-3c0a-83f6-b81280241581 | -8.6115 | -66.8076 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.5 |
| b8af4e7d-713c-3cc6-adf9-15df39a78593 | -9.4819 | -66.7836 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 62aad974-705d-3424-a53f-b61712ba8dd5 | -9.4565 | -64.3344 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 21d70ea9-dc02-3b53-a224-54a4cd1b6474 | -9.9175 | -65.0313 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5c22e31a-8cac-3ff9-8db7-5cc034050ec3 | -8.4354 | -70.1117 | 2026-10-05 19:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 92ef6926-3505-3784-bc70-2f07e4e5d2b7 | -9.2828 | -65.6526 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2b0450a9-be36-38bd-9e7d-7c7e2d61fcf3 | -5.9606 | -41.3507 | 2026-10-05 19:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 379.1 |
| 5827ab46-0fc8-34b9-9b60-8520fab844f1 | -9.2366 | -67.885 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7bba61dc-2b34-3540-9b96-4a30458648d8 | -9.1244 | -68.2021 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 1c77cef1-43c8-36f9-b526-f53724a0d3c7 | -8.3341 | -62.8309 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 91e57069-3984-3b96-82f7-514f6768ac8b | -9.3015 | -65.6333 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5824ad20-a737-3087-b003-55b785f14e9e | -9.1076 | -67.703 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 210c8e0f-27c5-3811-9741-8b1172fdacf1 | -8.6293 | -66.9926 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2250f177-4eb4-3d8d-a024-3e8a740cde6d | -9.1259 | -67.7581 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3ccaaa8a-870c-3304-918b-8e8c5641f9df | -5.3985 | -39.1078 | 2026-10-05 19:00:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 140.1 |
| a334bf7a-5d45-3984-86de-67cb44ae48a6 | -8.8519 | -66.8012 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| cc697828-39a1-31e9-82d7-e0fa223758f1 | -8.8696 | -67.0049 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 497b5d8c-661c-3870-a2a6-34e6e7853094 | -9.1438 | -67.9428 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 39418e33-68f0-3795-b240-c0c12c5664b1 | -9.1243 | -68.2391 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1177e995-6bb6-3228-9bab-10feb7caa03b | -8.2674 | -71.1215 | 2026-10-05 19:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 27422ee1-f1e5-3fe7-ad33-1c6f8cfc7f39 | -12.1385 | -63.1688 | 2026-10-05 19:00:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b0dfb13b-e43d-36a4-9bcf-b24a31cf26e9 | -5.1305 | -43.9844 | 2026-10-05 19:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8394cf1a-4390-3f8f-8368-4777048dc1bf | -9.0614 | -65.4355 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c19c6b55-f352-34f8-a77b-4e1702178793 | -8.871 | -66.6521 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8304ba59-9011-332d-9a26-eef177d11def | 3.5254 | -51.5057 | 2026-10-05 19:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b52c996f-1e29-3dc3-a554-c15188e803a8 | -8.5183 | -67.0139 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 2d84d884-447a-345f-85f9-d03a78708296 | -5.9603 | -41.3749 | 2026-10-05 19:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 400.8 |
| d2a883de-b4d2-3a86-8118-b781735d5cda | 1.5106 | -55.6285 | 2026-10-05 19:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a2374367-0b01-39f4-b611-fc225ec71dbf | -9.4751 | -64.3336 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 141540a5-1e49-317c-9968-8db474880363 | -9.2365 | -67.9035 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6d3c34e2-df78-31d7-a27a-56d779bd05a0 | -9.3014 | -65.652 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| a7502077-e7d1-34c8-b883-9a9af835d676 | -9.1075 | -67.7401 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a59cb52a-1cb7-31b0-81ba-1461b39759ed | -10.3503 | -68.0234 | 2026-10-05 19:00:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3cf42c28-9aa1-35bb-93c7-eadbc9e0f1af | -5.9155 | -44.0894 | 2026-10-05 19:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9e111847-ea1d-31ec-a380-3385a6c09c76 | -9.1168 | -65.4711 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| cf07af3e-6f42-3fee-b167-032d61918d75 | -9.2199 | -67.3852 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4aa61f4d-f50c-3729-8942-5dc5a3b90f8e | -9.1427 | -68.2572 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b0f647b4-2dcd-39ef-9d7a-a5938108586e | -4.509 | -42.0822 | 2026-10-05 19:00:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 5daf6e5f-6fcb-3579-a518-00e230552451 | -9.1072 | -67.8326 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 024ebb3f-4a9e-3e63-843a-df817c470bd4 | -9.0982 | -65.4904 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 20fc2ec5-71a8-3102-bbdd-170f235d1943 | -9.1257 | -67.8137 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 80939c04-f68f-3c78-9f52-bc7e8de21c8e | -8.5929 | -66.8266 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 4da4675d-06cf-3ed7-9d1e-91ad6824f6c1 | -9.4958 | -63.9562 | 2026-10-05 19:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| b0ed807c-70c3-3e02-bf44-da8dbc79b0f1 | -8.8895 | -66.6516 | 2026-10-05 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9a4c0b4f-c5ef-3216-92b2-2176bc51c027 | -9.2367 | -67.8665 | 2026-10-05 19:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 21f6d905-4ec0-3a1d-a14d-a7f324de26f3 | -9.0045 | -65.7174 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3dffe555-1b45-37c5-8d57-82a165205ed9 | -9.1076 | -67.7215 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 70739822-a7b4-33c5-ab7f-fc2013b77d7c | -9.1072 | -67.8141 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 127.4 |
| dd9b7997-4ec2-3394-8c20-98d0528580c3 | -10.3503 | -68.0234 | 2026-10-05 19:10:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a57b4ce1-a04d-3282-a01e-64eb8eed8456 | -8.8696 | -67.0049 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ab4178b7-e589-3594-a109-52f806535f66 | -4.509 | -42.0822 | 2026-10-05 19:10:00 | GOES-19 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| b9eeba4e-0610-3988-b959-9dfe3be2fa2c | -9.1075 | -67.7401 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fc9f019e-d09f-3f7d-aeb4-0d0ccec9fff3 | -8.593 | -66.8081 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 190.3 |
| d5dc6e94-a4a0-333e-8fc1-ffd2655bcd66 | -4.8083 | -42.134 | 2026-10-05 19:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| b27393bc-fc2f-3895-aebc-685e562f03a1 | -9.1076 | -67.703 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 40ca65ec-ca38-3ea0-b430-d2c82e1d6666 | -8.852 | -66.7827 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7499a6c8-ad75-355f-a425-2ddc123ce340 | -5.9155 | -44.0894 | 2026-10-05 19:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 474f6f51-58c8-331d-9435-c032faf83fb8 | -9.1257 | -67.8137 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 11bee93d-a95d-390e-8f17-625418400a39 | -9.1426 | -68.2941 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 622ec449-0e6c-3e11-83c4-15ce854c304a | -2.5535 | -65.8634 | 2026-10-05 19:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f7c0ff6e-0d8a-39ae-b087-cc2a2f65e560 | -9.1257 | -67.8322 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 397e2701-6932-36ac-b91d-30016d4aa9d7 | -8.3341 | -62.8309 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.7 |
| c028fbb1-04ad-36aa-a126-45e0b432f9ee | -9.0614 | -65.4355 | 2026-10-05 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| fa99bf37-8aba-3b56-9169-20eabdb92c4d | -5.9603 | -41.3749 | 2026-10-05 19:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 250.1 |
| e6eb11ec-2589-3591-a22f-ada9696cd933 | -9.3494 | -67.4374 | 2026-10-05 19:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bfe769a5-4c34-3380-83ae-5694767d7dab | -9.9175 | -65.0313 | 2026-10-05 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |


[Clique aqui para ver as próximas entradas](README166.md)
