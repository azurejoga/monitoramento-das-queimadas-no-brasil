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
| cf7e2a20-bf3d-300f-b5b5-f0730a153dd1 | -20.9925 | -50.0261 | 2025-09-25 00:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 6e5399bc-674e-36a7-83c2-5673498e0d23 | -17.9312 | -55.8548 | 2025-09-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| c9f38599-08ef-320e-bc69-05f137e9ad56 | -23.5941 | -51.7467 | 2025-09-25 00:00:00 | GOES-19 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| d1466d09-1fc8-3edd-87b4-ffb28d4f9c91 | -3.823 | -50.9765 | 2025-09-25 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7191f167-c428-3347-a7c1-3dfaad9ff856 | -6.4131 | -43.0724 | 2025-09-25 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 190.7 |
| b34e9feb-2de1-3b20-a471-b347e3cec319 | -15.9576 | -59.5089 | 2025-09-25 00:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a7abbbf0-718e-347a-a6c9-75fc62a92223 | -2.9291 | -48.3181 | 2025-09-25 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6878fecd-6615-3cd7-b3a0-73a3b7b24d16 | -3.2176 | -54.9632 | 2025-09-25 00:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a53815d2-d99a-3949-84bf-16ee8ee3540d | -20.7127 | -57.8531 | 2025-09-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 55471f42-3454-3924-84be-d9b3e9eaf891 | -20.9931 | -50.0032 | 2025-09-25 00:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 197.5 |
| 96c142e4-bd1b-335e-96d1-8aec4246aa0a | -3.1993 | -54.9636 | 2025-09-25 00:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 9ac3163b-05a0-3849-9caa-8dfcf685f0d3 | -8.4795 | -45.0246 | 2025-09-25 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 5e6f44ae-227f-36b5-a6cf-f110325265f0 | -20.6924 | -57.8559 | 2025-09-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 2902d6cb-2370-3b2f-8347-ef5758b32a20 | -5.6393 | -45.7239 | 2025-09-25 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8f096529-5134-32ee-be29-b40a6f954b5b | -4.8161 | -43.5423 | 2025-09-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ae3ca0f0-25bb-3258-a928-75d0b5450cd2 | -4.7974 | -43.5435 | 2025-09-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| c8a45515-eace-3281-bb4e-c1cea9e48d49 | -6.4319 | -43.0707 | 2025-09-25 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 3787eeac-032c-3ad3-b92a-527fc6311edd | -6.4129 | -43.0958 | 2025-09-25 00:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 39431978-aa1d-3604-a889-20a3f30809f6 | -2.9291 | -48.2966 | 2025-09-25 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a4e380a8-c4bf-3d19-ad1a-2fcce80ff373 | -8.4798 | -45.0018 | 2025-09-25 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 373.5 |
| 1ab9b7ff-3847-3902-aafe-00ca716eeee0 | -4.7976 | -43.5203 | 2025-09-25 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 05ea8d2c-5965-3b86-8658-a8f5606a644c | -17.951 | -55.8522 | 2025-09-25 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.7 |
| d3112f1e-49c1-3717-b570-239505d8d8b0 | -8.461 | -45.0038 | 2025-09-25 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9e62b665-fd97-3492-a805-4ce7eacaa0a3 | -6.4317 | -43.0942 | 2025-09-25 00:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 332.0 |
| c2ae3bca-1f37-3d70-b364-97b8a0c1c7d8 | -8.4801 | -44.9789 | 2025-09-25 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 7b46e712-5223-3c28-a0ca-aaf4bb046a56 | -20.9931 | -50.0032 | 2025-09-25 00:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 281.8 |
| a170ef10-9dd1-349f-9ce2-758b3eef0b40 | -3.823 | -50.9765 | 2025-09-25 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fab4cbc5-d7fd-3a99-a986-577f9ba8ea35 | -2.9291 | -48.3181 | 2025-09-25 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9cbfe162-535b-3b6d-8c40-85445197ffd4 | -6.4131 | -43.0724 | 2025-09-25 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 2c999baa-7cb2-32c2-a800-2d37405aabab | -3.2176 | -54.9632 | 2025-09-25 00:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a6a8cbf3-7f35-35c7-a410-a2ff5c6d6858 | -6.4129 | -43.0958 | 2025-09-25 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 221.5 |
| e873c06f-f8ae-329b-a2f9-643736a24f28 | -2.9106 | -48.2971 | 2025-09-25 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2705c75d-7bc7-38a0-8ab1-d6bcb2320b88 | -20.9925 | -50.0261 | 2025-09-25 00:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.7 |
| d1bdd2da-83bb-3bea-aa65-2fd18848e2aa | -5.0093 | -45.1565 | 2025-09-25 00:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| cce9a37d-9d73-3287-ba50-5212aef38898 | -20.9726 | -50.0077 | 2025-09-25 00:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.6 |
| dd1e11a2-3a98-3736-b7ef-a9edae6b33fc | -17.951 | -55.8522 | 2025-09-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 150801da-c58e-3514-9c30-5c166aec3371 | -6.4319 | -43.0707 | 2025-09-25 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 2fddd644-6f1e-3eef-8f3e-0bf592cedebf | -17.9312 | -55.8548 | 2025-09-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 16f20818-48d4-3abc-9b52-4ee592443e57 | -20.7127 | -57.8531 | 2025-09-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| aa62e2ee-6771-3e93-959c-996889d41721 | -8.4798 | -45.0018 | 2025-09-25 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 1de33d62-4947-390e-b88a-1766c06ba6fa | -20.6924 | -57.8559 | 2025-09-25 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| b77e38d9-0736-3ce8-a063-a370ac0b4173 | -21.0137 | -49.9988 | 2025-09-25 00:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| 5eef9722-5f6e-352e-ac23-1e22c9068c2b | -6.4317 | -43.0942 | 2025-09-25 00:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 0b888f47-4aa0-3a09-88d7-00c4da72e806 | -2.9291 | -48.2966 | 2025-09-25 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2907e326-b2ac-3575-b45e-7f2bb5a7ccd9 | -3.1993 | -54.9636 | 2025-09-25 00:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2e1d653b-0e51-3bd9-99f9-475ccd4035f1 | -5.0091 | -45.1792 | 2025-09-25 00:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 8840f716-6268-3642-8b38-fb10ec0d029c | -4.7972 | -43.5667 | 2025-09-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 1605c12f-fe3c-39b6-ba30-5daae80e5009 | -20.7127 | -57.8531 | 2025-09-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 2fd5eb5a-6c32-3f17-b881-0ca18832494c | -5.0091 | -45.1792 | 2025-09-25 00:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a337d1e1-8d79-3348-827b-a04cc44b352b | -6.4131 | -43.0724 | 2025-09-25 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 2eeb7382-893b-3a82-9aa4-728268fda707 | -3.823 | -50.9765 | 2025-09-25 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 243fe961-422b-39b6-a916-d1f82a930066 | -4.8161 | -43.5423 | 2025-09-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c966dce3-7954-389f-ac40-eb0f5a433e3b | -20.9925 | -50.0261 | 2025-09-25 00:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.6 |
| 1c397138-abfd-351e-b548-94fc95c3ff7e | -6.4129 | -43.0958 | 2025-09-25 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 4558ecc4-ca93-38b6-95f3-acbf76e46c99 | -15.7642 | -59.4872 | 2025-09-25 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| fff25f43-ba4e-31ae-8f21-fca7e24c2bd0 | -4.7974 | -43.5435 | 2025-09-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 2e7973d1-4d3b-31ce-a704-b5f082565879 | -5.0093 | -45.1565 | 2025-09-25 00:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5896c6ae-d053-38bb-bb87-7b2d904aeeb3 | -21.0137 | -49.9988 | 2025-09-25 00:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.9 |
| 19f6be89-2e7f-36e8-a826-09e49b93a635 | -4.7976 | -43.5203 | 2025-09-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b50dab6a-0ebf-36c5-8cb2-481286275a49 | -6.4319 | -43.0707 | 2025-09-25 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 16edc524-6426-3bbe-ac03-7dd265f0b30a | -6.4317 | -43.0942 | 2025-09-25 00:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 0c699177-0096-38f6-9eb4-1493fcdb3071 | -20.9931 | -50.0032 | 2025-09-25 00:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 260.0 |
| 7067f14f-254e-3712-ace9-22f41868ceb7 | -20.9726 | -50.0077 | 2025-09-25 00:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 905110ed-f8a1-3e91-98f2-f4b6aab0f446 | -8.4798 | -45.0018 | 2025-09-25 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 6e0fcbb8-ddb6-3fdb-bffb-2d4908abbeca | -2.9291 | -48.3181 | 2025-09-25 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 2df7f483-ad94-36f8-a0e0-cde156e5f3ad | -2.9291 | -48.2966 | 2025-09-25 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6b9c1113-17e3-3c57-8dc3-8d38249aafad | -3.2176 | -54.9632 | 2025-09-25 00:20:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 060e6541-eda7-3e93-b433-8f09b85e12e0 | -17.9312 | -55.8548 | 2025-09-25 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 2373566f-6368-3988-be91-2871f977578d | -15.7835 | -59.4853 | 2025-09-25 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 29a33525-2e3b-368b-8483-8f0e908f5ced | -15.7838 | -59.4653 | 2025-09-25 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 88734669-8c6b-38b7-a421-d1b469f6416d | -15.7644 | -59.4672 | 2025-09-25 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 39af5b4c-7f57-392b-ad8c-0384eb333eb3 | -21.0131 | -50.0217 | 2025-09-25 00:20:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| 3611111a-4de7-3a53-9cb1-1cb124a1f282 | -20.67006 | -48.82992 | 2025-09-25 00:28:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f6acb1f0-1e41-3c26-911d-322c3987dfea | -20.66864 | -48.81854 | 2025-09-25 00:28:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 4e06daf8-48d0-3665-8ff5-7f7f7a1d7c45 | -22.18319 | -51.97183 | 2025-09-25 00:28:00 | TERRA_M-M | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| cd59667a-a19a-3818-87b0-a3e2ffa5d8b8 | -20.67066 | -48.81247 | 2025-09-25 00:28:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 74c51953-0bdb-34ef-a6f5-ae0302243540 | -20.99383 | -50.0258 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 907dd9ce-bbdb-3dbf-8190-4654d02086c1 | -20.99504 | -50.46374 | 2025-09-25 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ad0e7359-f503-32c2-bd79-77a80b585f07 | -21.01649 | -50.03661 | 2025-09-25 00:28:00 | TERRA_M-M | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 6091b3a1-ebdc-36d9-9e5e-8107841b6cb1 | -20.99791 | -50.01693 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.3 |
| f661ac2d-d8e0-351e-addc-f092269b2aee | -21.01494 | -50.02287 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| bab6fd38-95be-3a11-bf82-09bdf0b2aff5 | -20.99626 | -50.003 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.3 |
| 0c68cca2-f3ec-314e-8f29-ef65dd3c0d2f | -22.64579 | -46.90361 | 2025-09-25 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| e7c9615c-4f53-3d89-855a-8c4e2fe25e43 | -21.29309 | -48.67693 | 2025-09-25 00:28:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 26b9acca-d825-36d1-8898-b561bd1080ff | -20.98413 | -50.465 | 2025-09-25 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| e19ad679-af27-3ffc-9721-ceca73f7c05a | -20.98737 | -50.01838 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.1 |
| 9ff2e043-800e-3319-9ef1-497828982996 | -20.99074 | -49.99808 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.2 |
| 39ffdbfd-0a39-3d45-a081-b4aebddfd975 | -22.00719 | -49.44306 | 2025-09-25 00:28:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e42d9eaa-887a-30e2-bb02-6a73ebd017b8 | -20.98574 | -50.00459 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 192.2 |
| f554990f-7d7c-312c-8842-36785064c4af | -20.67203 | -48.82389 | 2025-09-25 00:28:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a8bf5b4f-1420-3d71-b5c0-647147413ff1 | -21.00283 | -50.01046 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.3 |
| af9420ea-3962-38f0-946c-2d1ad6dfe640 | -20.99228 | -50.01188 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 382.6 |
| 5893f963-bf77-3fb8-811b-7be6cc6ed4cf | -22.18525 | -51.99192 | 2025-09-25 00:28:00 | TERRA_M-M | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| f3578713-98af-30c5-b55c-28da2ce5240c | -21.0044 | -50.02444 | 2025-09-25 00:28:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 3d682650-9583-3152-83ac-c41696fb861d | -6.4129 | -43.0958 | 2025-09-25 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 8632e5e0-ed80-3b1b-bd36-6922fce6fe78 | -21.0137 | -49.9988 | 2025-09-25 00:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.1 |
| aa9ef2df-525b-34ab-8e92-058e4634885b | -20.9925 | -50.0261 | 2025-09-25 00:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 256.4 |
| 5215ec10-b55d-3e8e-a852-e4651ce55fc5 | -20.6924 | -57.8559 | 2025-09-25 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| e4dcd850-5e14-3193-afd9-5367012da8ac | -6.4319 | -43.0707 | 2025-09-25 00:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 267.4 |
| 9712000c-5e16-328f-8ca0-4a00f676d645 | -20.9931 | -50.0032 | 2025-09-25 00:30:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 430.3 |


[Clique aqui para ver as próximas entradas](README2.md)
