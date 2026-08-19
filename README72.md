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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81671163-a33f-35d9-b25c-fb3f2471c25b | -9.08 | -65.4163 | 2026-08-19 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 07bcda0e-3627-3927-95e4-13c637bc4dad | -8.5598 | -54.7579 | 2026-08-19 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f26095b2-0d9a-31f9-9682-ed7baf7227f5 | -9.4256 | -60.4353 | 2026-08-19 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 98621c6d-9b1f-3497-b980-38ac7e71139c | -6.0912 | -57.9187 | 2026-08-19 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f15978e2-703d-3b1d-905c-e0795e4cd95e | -5.9198 | -43.6264 | 2026-08-19 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9cc21458-c84a-3d67-965f-03baeaacfb7d | -14.8033 | -46.6453 | 2026-08-19 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5f77b75f-bab0-3c95-9343-92c66cc9a5e3 | -19.7446 | -57.9217 | 2026-08-19 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.2 |
| 577c4063-c9de-37fd-b856-8086a121409f | -9.4254 | -60.4545 | 2026-08-19 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 76f2fa2e-ea8e-3d55-b7f2-8bbcc3632ad4 | -5.4317 | -48.4212 | 2026-08-19 06:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c47b92cd-c043-35c4-8008-5f2c0c6b968f | -8.5785 | -54.7566 | 2026-08-19 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a30e0031-1265-3fd5-8aeb-f9f56834054d | -14.8033 | -46.6453 | 2026-08-19 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8c2908e2-f799-3690-a15f-6235fc3f1df8 | -5.4317 | -48.4212 | 2026-08-19 07:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e64321d2-99cf-3da5-857f-c109146d9486 | -8.5598 | -54.7579 | 2026-08-19 07:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2be58277-3d20-327f-8ec3-b7cad0ebee4a | -6.0912 | -57.9187 | 2026-08-19 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7a03f592-7691-3790-8ff6-4e9898dcbcf3 | -9.4254 | -60.4545 | 2026-08-19 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 01bb3e2f-9d77-3281-b542-ef4c7182e186 | -8.5785 | -54.7566 | 2026-08-19 07:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d3a60680-edff-3cab-b4f3-e5b8fce13ca4 | -5.9198 | -43.6264 | 2026-08-19 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 990b7f7d-9b8a-3b79-80b8-6701af8335dd | -19.7643 | -57.9399 | 2026-08-19 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 377746f9-68c6-3f64-9738-e15052490c92 | -19.7442 | -57.9425 | 2026-08-19 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| aa00452e-9948-3fb9-b31c-fd76de738255 | -9.4256 | -60.4353 | 2026-08-19 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1f3251f9-4ed3-382f-95cd-b5b8c1ae1c01 | -14.8028 | -46.6683 | 2026-08-19 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a55377cf-7214-37a3-a7b5-18d3fc165e43 | -5.9198 | -43.6264 | 2026-08-19 07:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 7a94227d-be81-3a1a-9487-103c141175ec | -19.7643 | -57.9399 | 2026-08-19 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 75a1a55c-d409-3cef-b17b-5257a6d470b4 | -14.8033 | -46.6453 | 2026-08-19 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 613586b3-f86b-3b3a-8e66-9a8c279a1eb4 | -8.5598 | -54.7579 | 2026-08-19 07:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1d6b2134-2bb8-35b6-8b91-a64ab7ce86bf | -14.8028 | -46.6683 | 2026-08-19 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 81566f73-18f4-3473-bfd4-bdb532b863cc | -9.4256 | -60.4353 | 2026-08-19 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f479bfb1-fed0-3d0a-9044-e98e24f03b58 | -9.08 | -65.4163 | 2026-08-19 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1505d2d2-f7f7-3f28-8155-8955fbcdbae6 | -19.7442 | -57.9425 | 2026-08-19 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 7d2f076c-c7cf-376f-b7b6-9c51d7a04426 | -6.0912 | -57.9187 | 2026-08-19 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 156db38e-8a6a-37b7-ad8d-0940e884b76c | -8.5785 | -54.7566 | 2026-08-19 07:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5ed01d8c-0799-3b0a-8a28-6f49410b61c5 | -14.8028 | -46.6683 | 2026-08-19 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 4e2bcfbe-6c2e-35f0-b7c6-e03f34e58cf2 | -14.8033 | -46.6453 | 2026-08-19 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 58266dc8-7383-3228-aaa5-012047ba96f3 | -6.0912 | -57.9187 | 2026-08-19 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b72a7bd9-5898-3b9b-a583-092ffc3e6db6 | -8.5785 | -54.7566 | 2026-08-19 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bfd3ec47-928a-3c45-b55b-859534d55af0 | -8.5598 | -54.7579 | 2026-08-19 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0a07a03a-1cd7-3ae0-9d24-88123d8203f2 | -5.9198 | -43.6264 | 2026-08-19 07:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| adac10d6-37d4-3a39-b8a6-2641624e5fcf | -9.08 | -65.4163 | 2026-08-19 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 1d325262-adef-3545-b852-25269992da22 | -5.4316 | -48.39313 | 2026-08-19 07:24:00 | AQUA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3db1ff55-6a64-3d92-bb58-4e9d11a5f02f | -6.14295 | -57.86071 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4e337761-814b-3090-88ff-9aa61692635d | -8.57118 | -54.68209 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b3756886-0144-351f-9afe-5816c0b2f252 | -7.05197 | -59.83184 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 253a3c91-9b0e-315d-8a16-fbf4560b9f9d | -7.88751 | -61.1807 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 12723898-30d5-32f2-9612-9f315b6dc7bb | -6.75948 | -59.14664 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4753c0cd-3091-36bc-b6b5-605d2907308f | -6.74788 | -59.16326 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32c710a6-0b95-30c8-bae4-9b04136bc755 | -6.83888 | -58.99148 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02c34d74-bb58-3b4c-81d2-62d3e4eb9fb6 | -6.63189 | -59.07582 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ca17e41-c178-37ba-ba33-6929d064b9bc | -6.33991 | -54.89455 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 43925e4a-4ccf-333b-9239-2be17c8b0324 | -6.85245 | -59.02087 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a15e8478-dc8d-30d7-98f8-f1ffac1ce951 | -6.08734 | -57.90936 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f031ee50-40b0-3dd9-9d0a-159966913c5f | -5.49037 | -60.12952 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 04a9bfe0-eb32-38d9-bdc2-17a3664b9aa6 | -6.74049 | -59.03387 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5a3e3d69-d8f0-3f28-a199-46fb2429ffd1 | -8.50733 | -54.85826 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d3c8426e-93a2-38a9-a1a7-d1745032a322 | -7.60562 | -60.95628 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 49d5c2de-5757-30e2-8779-88a57ca96b8d | -7.05052 | -59.84119 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c9a82890-1c28-3300-b8ff-b03bd6436062 | -8.56911 | -54.77222 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fa4603ec-da58-32f9-928f-f91fabd81e80 | -6.69788 | -58.93958 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 16b2ea04-9d88-364d-9e53-0f1fa817073e | -6.34816 | -54.90736 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ec6db436-0160-3333-b646-496840eae37e | -6.34982 | -54.89601 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e6e8e9d9-7643-35a3-8f3e-6242e784912c | -6.00238 | -57.86329 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 302fc779-e468-32e0-bf66-386d083e50b4 | -6.0151 | -57.83834 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 615abf7d-e289-3d4e-85c8-a26567971258 | -6.0037 | -57.85454 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 30e674cb-0543-31d0-aaa9-48fe1c1726fb | -6.80552 | -59.44738 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8034198d-ba74-3414-aeae-c33b83d6ad12 | -6.08602 | -57.91811 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1dcaec43-aeb5-35c1-9011-ab75b28a9f28 | -7.60728 | -60.94586 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8710daf8-739f-307e-b28c-fcf648152c30 | -6.69652 | -58.94848 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 95602067-617c-342f-b678-35db0f22f8de | -6.39225 | -51.74309 | 2026-08-19 07:24:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| a7ea5433-84fe-3c07-8c76-18fbf8da751c | -8.57087 | -54.75976 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 430ca4ad-e719-3809-8d3c-e78ad7e8539f | -8.58124 | -54.76116 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| f9ec5208-228f-3732-88e6-3c9e421442b1 | -6.33826 | -54.90595 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c5701cec-00fa-3137-98b4-10358bef4bf3 | -8.50555 | -54.87056 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3018f34f-6964-3f78-a9f2-c87a5b02cd8d | -6.85992 | -59.03114 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 45daac02-fbde-362f-a9d5-9d624a3e9d20 | -6.74651 | -59.17226 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b0c52546-9baa-3380-ad96-ae99964a3a08 | -5.99363 | -57.86199 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 76417d7a-a4f8-3018-9920-02640413baf3 | -6.87942 | -59.03996 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 84d39ae3-6b28-3f8f-ba44-bb5c4a602b7b | -7.88583 | -61.19133 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 43ca7934-6732-3e09-b42d-7bb27df1e1f1 | -6.10271 | -57.86693 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86eb4468-3146-3b3d-b5dd-d4d290587865 | -3.0973 | -61.2094 | 2026-08-19 07:24:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c970cfdd-a338-3610-a42f-a485a6f1100b | -6.14163 | -57.86946 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 02194da0-370c-3f3b-a400-fbc97460f856 | -6.00635 | -57.83705 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e4d7e04d-d367-3458-a789-2c98d48e9a26 | -7.53212 | -55.57947 | 2026-08-19 07:24:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dea51a0e-6219-3502-853c-039d839e3326 | -5.99495 | -57.85324 | 2026-08-19 07:24:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9568e143-e803-361b-8075-8b46896970d6 | -8.50367 | -54.86471 | 2026-08-19 07:24:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 37d17ff4-648d-3a2a-899d-83d350874d90 | -6.69923 | -58.93072 | 2026-08-19 07:24:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| d7cfcf02-452d-3b4a-93d4-84470afd8820 | -9.39231 | -60.5498 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 93b31884-a90c-330d-a4cd-991a621e5385 | -9.41622 | -60.45566 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3e31c8c4-b0ae-318b-b46d-6f135f552484 | -8.94952 | -60.54776 | 2026-08-19 07:26:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bd665ec3-74ec-3ccd-90b0-c4366aedb1fb | -9.4177 | -60.44615 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 27c2b6cb-1f71-30ca-a4e7-412e53032df4 | -9.39082 | -60.5594 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 44329de1-b0c0-349d-9065-809226827292 | -9.42211 | -60.41761 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fd788858-a8b8-317c-ad2c-e623da1ffd35 | -9.2797 | -56.89383 | 2026-08-19 07:26:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44238a0b-0dca-3019-a3a4-db21ac6316b0 | -14.21572 | -52.89171 | 2026-08-19 07:26:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 730596cc-3595-3735-b9c1-2ffa1b5c9bf7 | -14.21314 | -52.91312 | 2026-08-19 07:26:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0cd2f4c9-348a-3d20-a2df-edb3dd594b8d | -10.90867 | -57.18251 | 2026-08-19 07:26:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cb6f3d72-1c97-3f0b-966e-abc787483af9 | -9.41917 | -60.43663 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a8f43c6a-2386-397d-bd33-8d73f166afa5 | -14.14692 | -52.92274 | 2026-08-19 07:26:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 23c65958-2394-3c35-94bc-a4db64c65e76 | -9.42358 | -60.40813 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 46592fdd-01e1-3243-b7cf-653651cb2932 | -14.20247 | -52.89029 | 2026-08-19 07:26:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 09441346-4ecf-36fc-8b86-436992f74390 | -9.39993 | -60.56086 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4797b101-4c56-324e-8b12-1410a15fd68a | -9.40608 | -60.58153 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README73.md)
