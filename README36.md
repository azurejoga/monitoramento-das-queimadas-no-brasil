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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75e0cf4e-6474-3d2d-bf8b-7019ebf851d4 | -2.04306 | -50.79229 | 2025-08-16 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1e7fe94-43e6-34eb-bcac-065d49265307 | -2.54411 | -47.72216 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 724e70bc-7c9f-3144-a721-d5263b9ccbc2 | -2.37668 | -47.66405 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37edc347-8a60-35a7-9f8a-e8673ed61822 | -2.44618 | -47.3322 | 2025-08-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cf7f1b6-2c67-31c8-b5b6-7fbea4be9819 | -2.38332 | -47.66508 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d78306c8-3663-384f-882f-7b89dcd3fcec | -2.48973 | -47.57193 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7887fad8-7c92-34c1-b384-135f3a22e435 | -2.38 | -47.66457 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 564bd600-29b0-30a2-8cb1-92c84d99c980 | -2.47287 | -47.20609 | 2025-08-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccc93bd6-433b-3562-9e9d-0d14c8dc4b83 | -2.49028 | -47.56848 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21aa6918-ffed-34bb-b385-477821ae49c2 | -2.38603 | -47.62652 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cb52b5d-a0a9-3139-8a89-3b2a5a913a5c | -2.46951 | -47.76377 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171cf1bd-c574-3c7f-9f05-93a5c158c37c | -1.97628 | -48.71908 | 2025-08-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35b6d966-18ee-3243-bcc9-47b6265ce5b0 | -2.37613 | -47.66751 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dcb7397-40aa-37bc-b35c-62dd0fd909b9 | -2.48642 | -47.57141 | 2025-08-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74cdcd45-2766-302c-a7d3-19ad4f11bda9 | -7.9149 | -61.7288 | 2025-08-16 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2c186c15-4a86-3203-ab94-7fe8381499c4 | -14.9438 | -54.7166 | 2025-08-16 04:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ff6ede6d-956f-3746-b4bb-8f734efb249f | -14.9441 | -54.6959 | 2025-08-16 04:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3af91ada-8f2e-36a2-b8ff-812abd049e1a | -8.9893 | -61.7024 | 2025-08-16 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 01313d70-3fde-3a93-b983-6485b6b0fce4 | -14.9628 | -54.7351 | 2025-08-16 04:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c403314a-4595-3de6-8845-54d4e8feffc1 | -14.9632 | -54.7143 | 2025-08-16 04:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 70f4859f-ad19-33d2-85c7-42cc95823d28 | -14.9435 | -54.7374 | 2025-08-16 04:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 62dd48d9-4ee7-3a84-8813-18ff28ac0221 | -8.9708 | -61.7033 | 2025-08-16 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 40d96ca0-7a50-392b-bbc2-c8645ca15704 | -6.545 | -43.0373 | 2025-08-16 04:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 2116c90d-c429-3f86-9a0c-c071e5c024da | -6.5638 | -43.0357 | 2025-08-16 04:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 82832379-f0e8-3a4d-b402-79fb25bfc521 | -9.1708 | -59.6568 | 2025-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8cdcb20d-8656-3769-92eb-99e25fb2acd0 | -8.9706 | -61.7224 | 2025-08-16 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 627ace1f-a0a9-3d7f-abea-bd918991c590 | -9.1709 | -59.6374 | 2025-08-16 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 160e28d1-74a7-38f3-b267-802308e8225e | -6.0807 | -59.9465 | 2025-08-16 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a9b1f0cc-d6b6-3785-a18d-45f9c8426e58 | -8.9709 | -61.6842 | 2025-08-16 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 29e2a9bd-3c77-38ab-a681-cae8dc58b7eb | -7.9148 | -61.7478 | 2025-08-16 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| eafa1830-336b-3459-8282-acd1a2e8c18a | -6.65647 | -58.82624 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2a5e0b1-966b-3c1f-90b7-d132bc3aabaa | -8.19449 | -45.02545 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37b276a0-7515-3ac9-8d51-716a5a38da43 | -4.9215 | -43.25675 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c164df91-6416-33b6-9102-a6feefbfe3a5 | -6.55115 | -43.02631 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1d5bb1f-8c16-3c7e-ac24-32dbb10befc7 | -6.67088 | -43.76929 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4366919e-7deb-32c7-b3cd-d710a4cf35c2 | -9.80419 | -48.53653 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d2264c2-d7e9-3f82-9ee8-fb711d4a485a | -3.98869 | -43.24218 | 2025-08-16 04:32:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b7a3e1bc-977b-3217-8747-69e202320089 | -8.37883 | -47.00473 | 2025-08-16 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a567246e-f2c8-3d42-acdd-2026c410579d | -7.82563 | -61.33254 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49a85148-91f6-376a-a22d-e580bf9b62ff | -9.20967 | -45.33186 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38888eb6-4e48-3bb8-b5fc-ff2ed5995c6d | -6.11426 | -45.92434 | 2025-08-16 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| facf8081-d2db-3383-8fac-31af955f8d4b | -5.75311 | -46.67017 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4259e33-5652-31b2-8897-b9ca499e0e9c | -6.69936 | -58.82536 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8524a3-f967-311e-bcab-7d248d2d17c0 | -5.26175 | -50.76189 | 2025-08-16 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afd5580e-068f-3f51-b95f-1bf1ec78b840 | -8.18957 | -45.03335 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6099956e-5e32-36db-bf11-e3a526c9bac6 | -6.55516 | -43.02691 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bbda1e4b-3412-3da1-ad85-69a4eb295b77 | -8.74728 | -48.92791 | 2025-08-16 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8700274-8b07-3a0a-9a22-7104e7de9b85 | -3.42831 | -49.04841 | 2025-08-16 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8e82af1-c3fd-3577-b867-f63c1990279a | -6.93893 | -59.53552 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7761eb95-d150-3995-913b-f885e50fab6c | -6.93804 | -59.54036 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02a38f85-1e9b-33cb-960c-51d5ed4db44a | -4.22747 | -47.21735 | 2025-08-16 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e54bafe-a1b5-33c5-9649-321d96a6d348 | -7.54894 | -45.42004 | 2025-08-16 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ede243c5-cfb9-3106-bb9c-55326f4455d9 | -6.94768 | -59.52239 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d33a40-a139-3e25-a19e-a4a31814503f | -9.99032 | -48.54086 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ec9d89e-c05b-35c6-aae9-ad7c6b5455aa | -7.39154 | -44.90146 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40f7fe31-cda0-39f0-bc1a-0dc183a44229 | -6.69271 | -58.82849 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3195ace6-0526-32f3-bc97-bde124d8d7df | -9.20604 | -45.33131 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05d25a12-c2c3-3203-a67d-c9a96b343a1c | -6.11769 | -45.92485 | 2025-08-16 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 712b60fd-33d3-3b7a-aa92-4734687dccf9 | -9.85819 | -47.81857 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4697c5f-225c-3a0a-835b-6cacd2bfbcab | -6.55662 | -43.02773 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a36c462d-8e56-3d69-bb7f-847f3fb4f80c | -7.01122 | -44.31364 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4439f8f1-46aa-3359-bd70-a861ae6cf58a | -9.36462 | -47.98325 | 2025-08-16 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b051b809-6772-3d8e-95b5-1bfd9050f4b1 | -3.73645 | -53.98186 | 2025-08-16 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e7b2d9c-d49a-31f6-8e98-e3d31f15cfd1 | -8.16839 | -45.0258 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef0b587-9876-36de-9eae-2e2b65166b6d | -7.52414 | -61.33332 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2f6f15a-371c-37bd-831c-83ffe421772d | -8.18785 | -45.0201 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90edf857-6cd7-3192-bc91-915ba1e331e1 | -5.56608 | -52.04888 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7a2671-29ed-3139-bf4e-1b78dd921628 | -8.18294 | -45.02803 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 619bf159-b53a-3621-bf98-4cf4aace58ab | -9.80824 | -49.22089 | 2025-08-16 04:32:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ac31e2-586f-35d3-b02a-8fab570dea58 | -6.67161 | -43.76451 | 2025-08-16 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 31f507cc-0503-3a29-9aa4-2bc535bd0546 | -7.52978 | -61.34082 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cbb5b97-bd42-3547-a131-0583a304583e | -6.94243 | -59.51639 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fadb9e01-bbaf-3223-8a44-b485faf50467 | -5.1948 | -46.09154 | 2025-08-16 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ea9d929-04f8-31d5-8197-08c944356631 | -5.71855 | -49.0235 | 2025-08-16 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24834091-2c30-3467-8c4b-deff4b44cb7f | -7.53547 | -50.53083 | 2025-08-16 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a753324-3e1c-3294-8ecb-5927e2ed4e76 | -2.66449 | -48.55513 | 2025-08-16 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e707f1ab-ca50-3138-b643-65fad91d442d | -5.876 | -50.14631 | 2025-08-16 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b4e55e-c56d-3d2a-9963-e75dbc9f5cc4 | -5.86491 | -59.91413 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d15de0d-cab2-3435-b21f-79aa9a9089bd | -9.69791 | -46.26882 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0800975f-d8bf-3356-9160-3cc328869998 | -7.39643 | -44.89354 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f28e58-4b98-3505-9ac7-8edc46145e75 | -7.40453 | -44.86412 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| badedf58-7c2c-3df4-9ac4-10c3ab42b017 | -5.62704 | -51.29815 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cadbc22-e5f6-3a7d-bbb2-c7f655f64caf | -6.60481 | -42.74982 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ae3caa31-c9bf-34e7-8747-8832169831f5 | -7.5221 | -61.31429 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d3a8e7b7-ca8a-379b-9072-c2d60534154c | -8.19385 | -45.02969 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eb9f048-950d-3824-868f-7c2580629451 | -9.36794 | -47.98378 | 2025-08-16 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 07fb1ad3-464d-3e1e-bb26-f08fc3faaa4e | -2.91134 | -48.30231 | 2025-08-16 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3f7f2bd-39a3-3762-b321-9bae31347dea | -2.5826 | -51.91157 | 2025-08-16 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f19110e7-3bb8-3db6-9b68-2848e8c24cb2 | -7.58751 | -45.16373 | 2025-08-16 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c008673-2515-395f-8c56-4ad1cf9f5455 | -7.98116 | -43.96967 | 2025-08-16 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4fcdf398-8f17-3004-888a-f2c6e49f1c25 | -9.86044 | -47.82615 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d53b1e6c-a574-3a51-8499-b22ef1602b46 | -5.19818 | -46.09206 | 2025-08-16 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b5fe43d-7b8d-3349-8903-62a34a97a091 | -6.75364 | -47.78543 | 2025-08-16 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e8d3380-db74-31ba-9a95-18aecd0ec261 | -7.90979 | -61.74154 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5897ba32-a7d5-30ca-9a34-c5e4f69d5307 | -9.26265 | -44.55623 | 2025-08-16 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62c3b7af-a26e-3dd1-8bdc-b2a4340fd2a5 | -7.4193 | -44.91441 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 698200d9-61aa-355e-95c0-d06fa008553f | -4.22801 | -47.21391 | 2025-08-16 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0c07737-dc5e-3689-a83c-3feecebcd3b9 | -6.61706 | -42.75172 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a6fc0528-39b6-3a4a-a852-f1bdd5b13c03 | -7.06952 | -59.23711 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f32d927f-91d6-343d-a318-ebc14edc0baf | -7.44471 | -46.13009 | 2025-08-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README37.md)
