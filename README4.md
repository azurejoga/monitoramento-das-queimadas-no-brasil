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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9978770a-2756-3578-9bab-407689aba858 | -10.9593 | -43.0326 | 2026-07-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f1213a43-2e8d-3062-ab10-9e2953627006 | -12.7359 | -44.5225 | 2026-07-03 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9ee698b8-1003-3881-ab08-b20140e04d5d | -10.9401 | -43.0355 | 2026-07-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 08cf8217-550f-3b22-bd51-83b4790f937f | -5.8058 | -43.7975 | 2026-07-03 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 36d5182c-2a25-3898-818e-6e05d3bb1888 | -5.7945 | -45.0586 | 2026-07-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d42d01aa-df7b-3ef0-8595-b5e59d2f19dc | -5.7947 | -45.0359 | 2026-07-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6c16236b-0c28-3983-89b1-f2980b120403 | -10.9401 | -43.0355 | 2026-07-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| d3dd700e-fa23-36b3-904a-ddb1118b092b | -12.7553 | -44.5194 | 2026-07-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3c992bda-3528-30c2-99b5-c4443eac6369 | -10.9397 | -43.0593 | 2026-07-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 3745c237-3afb-3b42-ba49-c75ea77f9fe2 | -5.8058 | -43.7975 | 2026-07-03 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 7f9deb99-2d13-32a3-aee9-e0d4a830a8e7 | -5.8134 | -45.0345 | 2026-07-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3adc69d6-c86a-3eae-b246-9bec4eac01ed | -12.7359 | -44.5225 | 2026-07-03 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2a09b2cc-1e06-3d46-9c41-daac4ac85870 | -10.9588 | -43.0565 | 2026-07-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5c999244-efe1-3a58-a877-3fb1c494280b | -5.7945 | -45.0586 | 2026-07-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bb7d7273-6f79-38d7-952e-95d7cbdea699 | -5.7947 | -45.0359 | 2026-07-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 837916ba-a6cf-3b46-aa3b-08ac696d1d10 | -10.9593 | -43.0326 | 2026-07-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ec5400cd-98ca-3f1c-a467-85c55a869181 | -10.9588 | -43.0565 | 2026-07-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 171e18f0-3eed-34e7-8ccf-fa2a4ef0b4e1 | -10.9397 | -43.0593 | 2026-07-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.5 |
| d806954d-6e17-3a91-a1f1-72715d382904 | -5.8058 | -43.7975 | 2026-07-03 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7637e71b-a8e9-389b-be0d-63e946d4e67f | -10.9401 | -43.0355 | 2026-07-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| d602b7fb-f1ec-3507-8319-b69ea822a8af | -12.7553 | -44.5194 | 2026-07-03 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 58c58941-f26f-383c-8e94-fc2d4b04f4f1 | -5.7945 | -45.0586 | 2026-07-03 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f08740a7-da06-37fa-9440-c641c10a9cf1 | -5.7947 | -45.0359 | 2026-07-03 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c98c9d69-457f-3649-8a34-616eb638c620 | -5.7945 | -45.0586 | 2026-07-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| cfc2b883-6435-3d2d-9b17-7a5f3a1885c8 | -5.8058 | -43.7975 | 2026-07-03 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 0a4e8614-65a7-3f77-ba3f-a9fc6dce66ab | -10.9397 | -43.0593 | 2026-07-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| e811b574-0d03-39a9-9ffc-b58c3055743b | -10.9588 | -43.0565 | 2026-07-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 2739c7a0-1d95-322d-b4c7-c2e5b79136a5 | -5.8134 | -45.0345 | 2026-07-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5c4e12ba-e97e-3755-9dfe-0bab54c849bc | -10.9401 | -43.0355 | 2026-07-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0024b950-4265-3efa-bd22-d0362b1e6d20 | -5.7947 | -45.0359 | 2026-07-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0a9c740d-a772-3abd-b561-3e2a33c8b615 | -12.7553 | -44.5194 | 2026-07-03 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 16ed7433-6e7a-393c-8416-b6f55e4e82c5 | -10.9593 | -43.0326 | 2026-07-03 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f11edcfb-70a0-3e70-ae7a-94d4fa63ef47 | -12.7557 | -44.4959 | 2026-07-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| aebf2360-c683-3fb3-9ebe-9f38f059b8cd | -14.1948 | -58.773 | 2026-07-03 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 612b36af-76a2-3d0c-9d2a-e0a9270ec954 | -12.7553 | -44.5194 | 2026-07-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| fd09c1fb-b840-368d-9be3-40cafad7741e | -5.7947 | -45.0359 | 2026-07-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f31a7d22-4873-34fb-a88a-35345b25f7b6 | -10.9397 | -43.0593 | 2026-07-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 00fb8162-839d-31ad-8317-946109b58dc0 | -12.7359 | -44.5225 | 2026-07-03 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 85c11049-cf60-3a71-b6e2-bf1a9e2c1faf | -10.9588 | -43.0565 | 2026-07-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8d36c22d-860e-3c96-991f-9e8d2e019d8b | -5.8058 | -43.7975 | 2026-07-03 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 50abf37c-db0c-34ed-a161-5264cd24cdd5 | -10.9401 | -43.0355 | 2026-07-03 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 53a212ea-9ef5-3882-bf7b-de07ff119020 | -5.7945 | -45.0586 | 2026-07-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| caf71b46-90ab-3554-867b-e2ef8219e66d | -10.9397 | -43.0593 | 2026-07-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| b2160d6d-0003-376f-a82b-c88d1b8a423e | -21.2287 | -44.1536 | 2026-07-03 02:00:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| fda22706-20aa-372b-8fef-ba22a763bc75 | -10.9588 | -43.0565 | 2026-07-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 06661799-52fe-3584-9822-cfe1953edf9a | -5.8058 | -43.7975 | 2026-07-03 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| aa039ee2-9f11-3ca0-9e68-e8df1fa91c70 | -5.7945 | -45.0586 | 2026-07-03 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| faeb8ed5-ca35-36a5-8ff7-88ce41406e58 | -12.7557 | -44.4959 | 2026-07-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| bd90e850-acc2-3c5e-8dfc-8df9bf62d668 | -5.7947 | -45.0359 | 2026-07-03 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| eee290e8-74b1-3113-bcf0-11b28e9c4a9f | -10.9401 | -43.0355 | 2026-07-03 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 28ed7bef-a8fc-3f8d-8ca0-d10c8e100e1c | -12.7553 | -44.5194 | 2026-07-03 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 7cadd128-75f8-3b17-8070-52fa2dcdbf32 | -5.7945 | -45.0586 | 2026-07-03 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 22df4751-d852-351f-82f7-78159b2c4964 | -10.9397 | -43.0593 | 2026-07-03 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| b6e00dd1-fe99-3e36-aebe-bb85cc466fb6 | -21.2295 | -44.1286 | 2026-07-03 02:10:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.1 |
| 6fd267cd-6b62-35c3-952c-6bcaaedbc0a4 | -12.7557 | -44.4959 | 2026-07-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 13587509-4bb5-37ba-8c92-baff96684eda | -10.9588 | -43.0565 | 2026-07-03 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9839faa9-8227-3fba-8d8b-52599dfbf62c | -12.7359 | -44.5225 | 2026-07-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| de4572fb-fc13-3d21-bda0-d29dde6ce00b | -10.9401 | -43.0355 | 2026-07-03 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 9d3fda5b-35c3-3983-a960-2b25201c709e | -21.2287 | -44.1536 | 2026-07-03 02:10:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.3 |
| 6b360d01-12b1-3ea1-822d-84ffd2c7b559 | -5.7947 | -45.0359 | 2026-07-03 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 14dd8380-933a-31c5-b12f-d63e662a3e16 | -12.7553 | -44.5194 | 2026-07-03 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 7c7d8b9f-0754-3b83-969f-fa0f3111d43c | -10.9401 | -43.0355 | 2026-07-03 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f55da9b9-7fc8-304a-b21d-09db836821a4 | -12.7557 | -44.4959 | 2026-07-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e386de05-5b80-36d8-9365-0de42567741c | -10.9397 | -43.0593 | 2026-07-03 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.8 |
| a8d4c3b6-d15c-33be-89b9-d5c3d219412f | -12.7359 | -44.5225 | 2026-07-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d086d8aa-268f-3ecd-befe-f69e16cd5fd0 | -5.7947 | -45.0359 | 2026-07-03 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 976816fd-9889-3f98-8d23-8a68d9e507d1 | -12.7553 | -44.5194 | 2026-07-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 34242b90-0fc3-3780-9977-4cb5f28588d2 | -10.9588 | -43.0565 | 2026-07-03 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 586ba4ae-0215-3431-b01d-92ce65b9fef1 | -12.7548 | -44.5428 | 2026-07-03 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| f75f3fce-7ac9-3289-b418-3c428c498b57 | -5.7945 | -45.0586 | 2026-07-03 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3a8cdb51-be6e-3ae0-80ad-4213c3c8e142 | -17.3242 | -42.6381 | 2026-07-03 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 2f5a2d9b-4fb6-3aa3-9df9-a229c6359b5e | -5.7945 | -45.0586 | 2026-07-03 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 32f43a73-cd41-3c72-94f3-e548a3d1b1b7 | -10.9397 | -43.0593 | 2026-07-03 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 3e8b8c10-faec-386c-aee1-75f128b0f820 | -12.7557 | -44.4959 | 2026-07-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ffba1adf-8f5f-3366-86c8-bff7a971d2c3 | -12.7553 | -44.5194 | 2026-07-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 81942d40-4e53-37ee-9c0f-e3e8933a71d1 | -12.7548 | -44.5428 | 2026-07-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7d1a4c02-45e2-3eb3-a78b-941580c46a22 | -10.9588 | -43.0565 | 2026-07-03 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3411ab4d-f4c0-3b54-8869-0078c8112d4b | -12.7359 | -44.5225 | 2026-07-03 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f7e9d000-2596-3a04-95af-bc744cae4da2 | -10.9401 | -43.0355 | 2026-07-03 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 92c8dfd7-d360-3d1b-9250-11577802881d | -17.3041 | -42.643 | 2026-07-03 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c0678d1e-94e9-3e26-94b5-3ac1146685eb | -5.7947 | -45.0359 | 2026-07-03 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a9f1233c-0353-3ef9-a700-08acb6009dc9 | -12.7553 | -44.5194 | 2026-07-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 0a82308b-e593-3f1e-8c0f-adb74ad73ab7 | -10.9593 | -43.0326 | 2026-07-03 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9ef08b2e-dc48-3549-88a4-a9a9f4c1ce39 | -10.9588 | -43.0565 | 2026-07-03 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 37cac817-2340-332e-9a42-4e669f484c20 | -12.7557 | -44.4959 | 2026-07-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| dc861fb1-ed1d-3373-83a1-e8e7876dbf82 | -17.3242 | -42.6381 | 2026-07-03 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3fe164c5-f4e4-3608-b631-f5d695fc8593 | -10.9397 | -43.0593 | 2026-07-03 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 7ca10ed5-f665-39f1-aab6-9fc32d166780 | -12.7548 | -44.5428 | 2026-07-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 149d382b-7b3e-33af-b626-6fcd1cf9010a | -12.7359 | -44.5225 | 2026-07-03 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| d2a59145-b88f-360c-bae1-43a6b54ef396 | -10.9401 | -43.0355 | 2026-07-03 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 36ffa578-ed94-3a55-a5f8-aa52ecda42b9 | -5.7945 | -45.0586 | 2026-07-03 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8a14e9e8-d8af-3048-8283-b487bcf1b36d | -12.7359 | -44.5225 | 2026-07-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| cf7a4ab2-1a8a-385a-aec1-67b9afadd9f2 | -5.7945 | -45.0586 | 2026-07-03 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0f73dae0-5d61-3535-b57d-d21166fee7fc | -10.9401 | -43.0355 | 2026-07-03 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 231.6 |
| 80611d70-2a2a-3fcc-a424-4b544810e7cb | -12.7557 | -44.4959 | 2026-07-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| cafe3bb9-1442-335e-8c6c-65971fa27719 | -10.9593 | -43.0326 | 2026-07-03 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a5cdbcb3-c337-348d-9d5d-9aa333af0a6b | -12.7553 | -44.5194 | 2026-07-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| a79a7a29-1c2a-3626-b470-6c708ea8abf0 | -10.9397 | -43.0593 | 2026-07-03 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 267.8 |
| 90dfc5dd-b290-38c1-9860-3507674f84d7 | -10.9588 | -43.0565 | 2026-07-03 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 56351b40-8cba-3624-a205-a6f6a08c58af | -12.7548 | -44.5428 | 2026-07-03 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |


[Clique aqui para ver as próximas entradas](README5.md)
