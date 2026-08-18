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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e207a18-33d4-3bec-bc25-c8e38c660f99 | -9.7601 | -46.7141 | 2026-08-18 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 61eeb86a-d8dc-3cea-b173-ab5da974e909 | -6.7123 | -58.9412 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 0c5f494e-73bf-336b-a4e6-aa265c258b02 | -17.0817 | -46.5848 | 2026-08-18 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 6ccfd799-eb82-313e-a87b-6f45759810b3 | -9.4257 | -60.416 | 2026-08-18 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| de222305-7620-31fb-9c79-1eaa005f95a1 | -6.8409 | -59.0326 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 0f6c393f-b847-370a-9ab7-1d8f2385e915 | -17.1016 | -46.5808 | 2026-08-18 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 10c1b4c4-42e6-37f6-a33f-0ca4c838f53a | -6.841 | -59.0132 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 217.5 |
| c37aa541-81cc-3c0b-8934-5d816ad8ce6d | -6.8594 | -59.0125 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 92d4b523-03cd-307b-a69d-cfc9444abd2f | -6.4048 | -54.9441 | 2026-08-18 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 934289a2-b249-3151-b77a-810e280c1ff2 | -17.0811 | -46.6081 | 2026-08-18 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5cc85d02-2149-3f9b-8dee-246b0a735fa8 | -6.7663 | -59.1708 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| a797e724-801b-33ca-ab00-228d302c275c | -6.7477 | -59.1909 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 1cf846b7-930d-3ccf-a05d-452d616d247d | -6.7664 | -59.1515 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 6f5f4f80-70a0-329e-9975-a561ee59a7b2 | -17.101 | -46.604 | 2026-08-18 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| dfd3813b-2334-3907-bf27-d465580b435b | -6.8596 | -58.9931 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 193abc4b-ad42-361f-898f-25e0c407f988 | -6.9516 | -59.028 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 1aa64873-5582-391c-bdac-eefcb16ceef0 | -14.1628 | -52.9323 | 2026-08-18 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 25eb9d00-fdf3-3bf6-881a-3cc15c764d02 | -15.2643 | -56.4901 | 2026-08-18 00:30:00 | GOES-19 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d27ca211-685c-3071-9099-ebfa479c47a5 | -9.4256 | -60.4353 | 2026-08-18 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 3ac87480-4126-3592-92da-24950d269487 | -6.8411 | -58.9939 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b6ed4b67-a6e1-3aaf-99fe-b8763615b844 | -8.2222 | -55.0216 | 2026-08-18 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| da45cf6f-a53f-3ca4-9adb-374c1b2516be | -6.7478 | -59.1716 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 4e39885c-80bd-38f3-aded-bbf4f1196193 | -8.604 | -50.3527 | 2026-08-18 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 404fe35d-017c-3c72-8f19-24c650b5955c | -14.1631 | -52.9113 | 2026-08-18 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| b15be2c5-e887-3366-936b-75281b252a1c | -7.9149 | -61.7288 | 2026-08-18 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b88df67e-0b7e-3cf5-bb99-603fd0c8a100 | -6.8593 | -59.0318 | 2026-08-18 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| df06315f-9a56-373d-95b7-7a0413a17416 | -9.4254 | -60.4545 | 2026-08-18 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| aa262b11-17be-317c-9d33-2aac60cd66d1 | -8.604 | -50.3527 | 2026-08-18 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 98fdd689-a171-3da5-be76-b6f5b799b5c4 | -6.748 | -59.1523 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 63313671-eee7-3d94-9bcf-dd1c2af82d29 | -8.2036 | -55.0228 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5b2a09d1-933b-3df6-83b0-36188ed3b059 | -8.2222 | -55.0216 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5d26a551-78ea-31b3-b927-7b73280d7e77 | -14.2566 | -51.9259 | 2026-08-18 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| bf20c820-a216-376b-a74c-01d84847a64e | -8.185 | -55.024 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 31e16743-abfd-367e-b351-0e5bad3b518a | -17.101 | -46.604 | 2026-08-18 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 43a888ec-c878-3664-9775-acf84e8ca787 | -8.2034 | -55.0429 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 59c280ca-ba9c-3d4f-9839-84d9dacbb367 | -8.222 | -55.0418 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2074eb90-f250-3029-9549-9d590b3fde33 | -6.7477 | -59.1909 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4d573636-581c-391a-8fc1-01e39c27e9df | -6.7663 | -59.1708 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 10bb1281-d2fe-3bb1-8d60-2462f5e94e03 | -6.841 | -59.0132 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.4 |
| 82d3bea6-0024-3bb9-9036-7c5cef9a8ecc | -9.4256 | -60.4353 | 2026-08-18 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 6b2af88f-e3a0-3322-92fc-22d2a021a910 | -14.1631 | -52.9113 | 2026-08-18 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 416eabb1-82e6-33e4-b250-72a285cb3ecd | -14.1821 | -52.93 | 2026-08-18 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 161fb33a-a3a2-38fc-864c-d992c3fbf394 | -17.1021 | -46.5575 | 2026-08-18 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.1 |
| fec1a512-f835-3aa8-b550-6283082e4fd3 | -17.0817 | -46.5848 | 2026-08-18 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 396b1338-d900-3429-8abf-082e18a7e0e0 | -6.4048 | -54.9441 | 2026-08-18 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| ec61a81e-cd69-3e70-b5d5-b9c24568512f | -14.1628 | -52.9323 | 2026-08-18 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b1a1b5cf-8c29-3b0f-8045-c0a7a805b873 | -6.8594 | -59.0125 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| f5d7bc83-8d07-37d7-ac91-2c37f8b07790 | -15.2643 | -56.4901 | 2026-08-18 00:40:00 | GOES-19 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9feffbc8-bc97-3b51-87f9-2537963e9dac | -6.9516 | -59.028 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 82a3397d-dc19-3e14-9780-29a2d4f71a73 | -9.4254 | -60.4545 | 2026-08-18 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 344a94b3-8500-3e20-8dff-7389af08d74a | -6.8409 | -59.0326 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 38dc468b-5839-3809-8773-7a818e561d56 | -6.8411 | -58.9939 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 70c8ad13-5099-3084-8211-56a28c950f94 | -17.1016 | -46.5808 | 2026-08-18 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| df957b23-ea23-3878-a58b-f5a50d601a07 | -14.1824 | -52.9089 | 2026-08-18 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c5ec4311-b865-39f4-9be2-719610ae2b6c | -6.8596 | -58.9931 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a48c2273-b6ab-3846-8540-e9e4457554ee | -17.0811 | -46.6081 | 2026-08-18 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2d9c0485-a857-39e3-9fe7-f0fc71917c3f | -6.7478 | -59.1716 | 2026-08-18 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 247.3 |
| da78a305-26a8-3bab-8d1c-9bbf4a740cc8 | -17.1021 | -46.5575 | 2026-08-18 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 374.7 |
| e9d07a4e-ae75-3b3f-a14e-c9d5023cc710 | -17.1215 | -46.5767 | 2026-08-18 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 3282f612-45c2-3d3d-bcfe-52254cc77b5e | -6.4048 | -54.9441 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 13bfcf0d-9405-3c21-9360-dc7dcc802ee2 | -8.222 | -55.0418 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 6fe8ad76-5caa-3aaf-a2e1-86c175304968 | -8.185 | -55.024 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5bd22bbb-157b-38b5-a9d9-2ce01bfeaf66 | -10.8691 | -44.9646 | 2026-08-18 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d7eb12bd-eb94-367a-bf32-e6b3dd2d37db | -22.0762 | -55.9924 | 2026-08-18 00:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 78.8 |
| df113453-0e53-35ad-a06d-1e8a0a68eb1a | -8.2036 | -55.0228 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 3496749e-737c-3726-ab02-a4cc8710739f | -15.2643 | -56.4901 | 2026-08-18 00:50:00 | GOES-19 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 58bb35b3-a687-34d4-aa8b-65c6640b4b25 | -6.8593 | -59.0318 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e9ced2cc-0a97-3b8d-9790-7a9b7d77cae9 | -14.2566 | -51.9259 | 2026-08-18 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d4f8722-f2f3-32fc-9ac2-8aa1daa5000a | -17.101 | -46.604 | 2026-08-18 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 691ea7fe-2c98-32cf-a14f-534246c20818 | -6.8596 | -58.9931 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 48f798e4-2bd5-3cdf-b77b-3cc2307bc6f3 | -14.1631 | -52.9113 | 2026-08-18 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 173cae34-c04a-3f69-a4b4-cc4da5ec66ad | -14.1821 | -52.93 | 2026-08-18 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2fbd6582-2cc6-3495-acf9-f8a2b6580f5d | -17.1016 | -46.5808 | 2026-08-18 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 297.9 |
| 1705916b-c5ca-3aa7-ba99-a707c1f62553 | -6.841 | -59.0132 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 7f209c56-7a62-3e93-935f-3849f34e2bcb | -9.4254 | -60.4545 | 2026-08-18 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3ad7ca2c-09a3-3636-b036-00fbfa7a49e8 | -6.8594 | -59.0125 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 844b4629-e563-329b-8645-0c215b95ad9a | -9.4256 | -60.4353 | 2026-08-18 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| e01ea00c-205b-345c-8e43-ce8039484a71 | -6.8409 | -59.0326 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 2a3864b3-660b-39aa-a977-6122f5323cfd | -14.1824 | -52.9089 | 2026-08-18 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 055086d9-ad83-3f77-9ff5-9876cd4eca79 | -8.2038 | -55.0027 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 941f1b97-0650-378b-be0d-82fbae63a91e | -8.604 | -50.3527 | 2026-08-18 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 06d7e4a1-a4a3-32e8-9fc9-645fe9330e99 | -17.1221 | -46.5534 | 2026-08-18 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 79c8af50-0fdf-38c3-8489-86fd342f3fdf | -8.5853 | -50.3543 | 2026-08-18 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| e543ace8-1890-359e-95fc-0ae00f2f3d02 | -8.2034 | -55.0429 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| cc426a16-643d-3407-aa1f-d22dc48c03ca | -14.1628 | -52.9323 | 2026-08-18 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 46bba3ec-27d8-3a8c-8e0e-903161d7c979 | -9.4257 | -60.416 | 2026-08-18 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b5d98d81-55f1-35ad-b9f9-574ecb03f4c9 | -8.2222 | -55.0216 | 2026-08-18 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 60ed8b70-1d56-3fc9-ba6a-b52baf613bfc | -6.8411 | -58.9939 | 2026-08-18 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d835f07d-6a5d-3950-b2a5-50222481429a | -8.185 | -55.024 | 2026-08-18 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e276599f-bc0e-35eb-9dfb-2f6ce2c7c6a6 | -14.1824 | -52.9089 | 2026-08-18 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 7b86a81d-305b-351b-85fe-85b76581e620 | -8.604 | -50.3527 | 2026-08-18 01:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 71b3958e-9fa4-3346-83f6-6ca1a9ec254a | -17.1221 | -46.5534 | 2026-08-18 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| eb4f14e4-a5df-356c-a686-b4afbae27810 | -9.4256 | -60.4353 | 2026-08-18 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5f61dfac-dda5-31c6-8f36-04ef7e0ca2aa | -10.85 | -44.9672 | 2026-08-18 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 2287b313-3650-37d8-a426-7e79b8a08673 | -17.1215 | -46.5767 | 2026-08-18 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 326d2fb0-743f-3b5d-a243-b0ce5aae1c28 | -14.1628 | -52.9323 | 2026-08-18 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d9b6bf2b-88ab-3d41-a4bf-5d4d9617ebcc | -17.1021 | -46.5575 | 2026-08-18 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 0184e447-3342-333a-a117-b74c3342de0e | -17.1016 | -46.5808 | 2026-08-18 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 458bd623-f66a-3dcd-be42-9146c1d8e159 | -9.4254 | -60.4545 | 2026-08-18 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fd4a861f-ca1b-3753-bf5e-b992f6d74f69 | -14.1631 | -52.9113 | 2026-08-18 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |


[Clique aqui para ver as próximas entradas](README3.md)
