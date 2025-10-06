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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6e7c531-2a03-369d-882d-38dd496c1af0 | -11.48387 | -59.09554 | 2025-10-06 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e78465b1-6583-38f5-bc29-a6d3b866030b | -9.85033 | -62.2316 | 2025-10-06 01:11:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 95d56213-86f1-3524-ad31-d7f701638b4f | -8.47463 | -54.70824 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fd24a524-6c2c-3180-8119-c7c7eb790bf6 | -9.77162 | -53.84979 | 2025-10-06 01:11:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 11683123-c78b-3d05-b283-07d7ef8a20e4 | -9.27028 | -51.8063 | 2025-10-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 18a574e1-b9ba-3242-b37e-b2916183e87f | -12.98751 | -51.04249 | 2025-10-06 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6b4c9343-813c-3e9e-b0ee-c3903d3777f9 | -9.33676 | -54.52648 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 90a00bd1-81d7-3dc3-a6f5-55c0ed6ce3ad | -10.41383 | -50.41784 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f3171129-f5e4-3867-8557-268b568a21f6 | -10.88978 | -50.69099 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| a33f0c7c-59d3-3f6b-8cc9-29ee815fd6b7 | -11.87943 | -57.81682 | 2025-10-06 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 0506809b-18c6-3dff-ac8d-dbb4bdc5fff5 | -10.42815 | -50.41531 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d80bbcee-1f8d-3042-a7ef-5cd4a87b675e | -12.25906 | -49.19834 | 2025-10-06 01:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 98706138-a8dd-3d8d-a1ed-c63b7703e466 | -11.20527 | -54.87347 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 765c1fbe-bf78-3c1f-b46d-dde5fd6638c4 | -8.62699 | -54.96587 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c44159ef-8093-379a-8e59-4c0f5e5b6a72 | -10.40954 | -50.39177 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 422c224d-0b5b-3041-842e-0f6bb5c56c17 | -12.89852 | -54.74655 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 7064d0b1-839e-3852-805c-f359fd27c304 | -8.47265 | -54.69516 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 37768fbf-8868-3f56-b1c2-03e5d42a2051 | -12.90834 | -54.74498 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 980b2fcd-9ae0-3d9c-9093-bbaa7288ada6 | -9.83817 | -61.99116 | 2025-10-06 01:11:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c299e912-baf0-3f37-8a9c-ead62ac1b76c | -10.59739 | -54.36638 | 2025-10-06 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4ca5a704-08e1-3109-a3e7-15c6d9669cbb | -11.43597 | -55.04863 | 2025-10-06 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6a1024ad-64ca-3e46-a5e2-ae8a00676bb3 | -11.01513 | -50.6818 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e16bed2c-3e49-3876-a8c7-bb59d0501800 | -8.12259 | -55.0802 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4639a099-4fa0-37b9-9558-2b9a977a3e6a | -11.92079 | -55.90799 | 2025-10-06 01:11:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cf922db-c239-3ea3-97a9-d2513b994a94 | -12.90661 | -54.73357 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6cf26039-0a2c-3659-8dad-a0a2cc0a1c20 | -11.19351 | -54.86331 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f059a57b-12ac-3fa6-b51f-a3264d05f41f | -10.84937 | -57.17999 | 2025-10-06 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3c55e003-ab2a-3571-8e75-c6ff91f1a5a8 | -8.61667 | -54.96759 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| b54d009f-a635-3450-91ab-211709c8e6cb | -10.31403 | -50.27793 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d21c28f0-854a-3bf4-9a45-c3b02daeedea | -8.48322 | -54.6935 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fcbcc698-1f54-307f-b260-d9054f5057d9 | -10.81639 | -48.83409 | 2025-10-06 01:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 052fe6cf-1957-3daf-a93e-3a5d04f13a94 | -12.40976 | -51.12367 | 2025-10-06 01:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d5037723-723e-34df-8a24-0b214a9bf293 | -11.20352 | -54.86179 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ea7aee97-0092-3752-800e-426ce2874f69 | -11.88068 | -57.82579 | 2025-10-06 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e98c4ae4-49b1-3f15-8595-0fe259b298c6 | -11.51148 | -54.45573 | 2025-10-06 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| dd1cc978-ae01-3378-80fd-8042cefe5208 | -12.38648 | -63.72355 | 2025-10-06 01:11:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 271ed657-b448-349f-8377-d66a29cf2304 | -12.90024 | -54.75784 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 6f598138-b7a6-3eea-8bc3-9fff133b7ced | -9.27349 | -51.81133 | 2025-10-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 73f15470-c461-3674-82b1-a6ca51952463 | -12.792 | -56.96628 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7a495993-811b-3ec3-a0bf-a692ae215307 | -11.41966 | -55.07447 | 2025-10-06 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 65b659a8-8bfe-35c6-beed-8279dafdd902 | -10.98007 | -51.15289 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 74bef458-0ee4-3220-a536-c3bf815054ca | -11.50312 | -54.46972 | 2025-10-06 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c3234f1a-d004-3f24-8700-2840abbf42d2 | -12.79069 | -56.95709 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 247aba70-f418-3206-8299-74b1800d10b5 | -11.44581 | -55.04699 | 2025-10-06 01:11:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ece2f7b7-651c-3586-93dd-d04ab3393bc8 | -10.87589 | -50.69345 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a211034d-f374-393f-bec3-ac51abc815d5 | -11.96089 | -55.25851 | 2025-10-06 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 60a99ec1-48f1-3c2a-ae11-3c18349a4a85 | -9.61658 | -57.20287 | 2025-10-06 01:11:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71bcc1d8-c713-3c90-841e-8e7fc9e9fcc1 | -12.91645 | -54.73203 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 0eb87973-1250-3a37-85f6-2453515f7f58 | -12.94593 | -54.72714 | 2025-10-06 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 71f75e75-1d43-3a94-8ecc-0c59a58e1e38 | -11.87061 | -57.81813 | 2025-10-06 01:11:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 11511527-7c24-3692-b2cf-714203e00f52 | -10.9837 | -51.17508 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c0bbbe0a-adfd-3d8e-a648-3384e12f641d | -11.88267 | -56.86285 | 2025-10-06 01:11:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4212b7b-6c20-3254-bbf5-68e29c1be752 | -11.00994 | -50.68937 | 2025-10-06 01:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7a405fb8-c22f-347c-972f-d01eddf4abc8 | -12.37648 | -63.74273 | 2025-10-06 01:11:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 05890244-f52b-34f3-ac55-6b201847a359 | -1.12687 | -53.06649 | 2025-10-06 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1d508a2f-4e91-35d9-b4fc-5729128c5ae5 | -2.78354 | -54.4201 | 2025-10-06 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4482da0c-9b30-3062-8d51-194feaf26303 | -7.02615 | -62.97486 | 2025-10-06 01:13:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1efacfa0-32d5-38c9-a46f-8922a9db6eb2 | -2.78914 | -54.41253 | 2025-10-06 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 062d115a-f78d-3a66-9332-b1b51d8f3f8a | -7.35537 | -64.66238 | 2025-10-06 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0d2e361a-b179-39b5-8224-25e8e93fdffd | -12.3793 | -63.7294 | 2025-10-06 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 33105bc8-81f1-3712-932e-b8ed36e085db | -18.0008 | -57.5444 | 2025-10-06 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 88c6d46e-600d-34a6-9eb3-bb3b41e79266 | -18.1366 | -53.3946 | 2025-10-06 01:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a8003177-8019-36c9-94a9-723fb7f1aa27 | -10.3162 | -50.278 | 2025-10-06 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 98775f2e-36d1-3281-91f0-5f1a66faeb56 | -14.5438 | -46.9633 | 2025-10-06 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 69a35af5-f664-3807-91f7-ec8b9d35c9aa | -14.5442 | -46.9405 | 2025-10-06 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9eff9cab-b162-3289-a9e9-995a597a3fd2 | -13.2699 | -47.8398 | 2025-10-06 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f43b647a-1ede-3bbc-9f37-0bcf9bf7c5d0 | -7.2281 | -45.8926 | 2025-10-06 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 480459d0-86af-3f35-9f33-2c34ef73f70b | -7.2279 | -45.9151 | 2025-10-06 01:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| bdfd38ba-c4d5-38f1-9402-47d0d19d5eb8 | -5.104 | -42.6343 | 2025-10-06 01:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 50c5a3da-05c1-3aac-8086-29f23f91ee8a | -13.62 | -48.6985 | 2025-10-06 01:20:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 3cdf6fcc-94bf-35cd-98e6-dd5361f0e894 | -5.0855 | -42.6121 | 2025-10-06 01:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7347e53d-bf27-3990-b810-07a5d77bfe34 | -14.6897 | -48.3797 | 2025-10-06 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6b5c1801-4c32-3f49-9d15-7e813c72af62 | -5.0853 | -42.6357 | 2025-10-06 01:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 42507e50-67e8-3dd2-a968-c2e82c9e6cef | -9.3162 | -46.0005 | 2025-10-06 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 57341439-3be7-3d54-a58e-3eef495bcd0f | -17.9803 | -57.588 | 2025-10-06 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 310d4501-8ec2-353c-b37b-d528cb9b1f0c | -5.1042 | -42.6107 | 2025-10-06 01:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| cba3a583-14bf-3727-8b32-c25149fde3ae | -7.2094 | -45.8942 | 2025-10-06 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 8b704c16-3e43-301b-8d9f-4f8754eaf0e8 | -17.981 | -57.5468 | 2025-10-06 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 24ac87a8-d67a-3f50-8ba0-f440a289f0ea | -10.4096 | -50.3538 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| bc101d0d-b62d-366c-9e25-dbe39e717cca | -5.118 | -43.2198 | 2025-10-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 9fd1f0b2-503b-3c35-8978-8a54b367bf49 | -10.3162 | -50.278 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3864e807-4403-3f67-bbb8-7bf96f6bb99e | -11.0037 | -51.1635 | 2025-10-06 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3b934916-7a96-38c9-be3a-4860ac2b6477 | -10.4277 | -50.4159 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 291872f6-dd9e-3232-b28a-0e82624f7bba | -10.4099 | -50.3324 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 727999b4-b34a-3881-9b56-3f13865b11b1 | -14.8828 | -51.4777 | 2025-10-06 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 6017c7b2-b52d-394e-852e-53e26b9ec25b | -14.6897 | -48.3797 | 2025-10-06 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 01027e62-8319-3b9a-b413-3f8417d9d42c | -14.8824 | -51.4992 | 2025-10-06 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 4118881c-fe13-3922-a1d9-316384359ffd | -18.0008 | -57.5444 | 2025-10-06 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 5cf9cf73-5dfe-3792-949d-4b9c24b7020d | -10.4283 | -50.3732 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9f4f14bb-766b-3caf-9b65-726fd8719d3e | -14.9018 | -51.4965 | 2025-10-06 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 697656e9-c1df-3e03-80d1-617cb1d83f5f | -8.4353 | -70.13 | 2025-10-06 01:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7ee3d971-d768-3f9c-b3c4-c862ddccc746 | -18.1366 | -53.3946 | 2025-10-06 01:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f90bc2d9-038c-324b-8ba8-7b767b891ca8 | -10.428 | -50.3946 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 694d5057-1461-3506-a22d-8e6a379fec99 | -14.8634 | -51.4804 | 2025-10-06 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 9e218ed6-934e-3c57-8b09-803fd9439fc2 | -10.4285 | -50.3518 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 834556a3-22db-38c4-8f93-74220206573c | -14.5438 | -46.9633 | 2025-10-06 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a9a7e9e3-02c8-3eed-a0ff-2fb4cbba7de5 | -14.5442 | -46.9405 | 2025-10-06 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ca2bf863-7d33-3102-a4eb-48d976dff683 | -18.1167 | -53.3977 | 2025-10-06 01:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fe47fd38-edef-387a-a8b0-8cce1ba43fde | -17.981 | -57.5468 | 2025-10-06 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| ccc94ce7-0f79-311e-9141-1e59771701e3 | -14.863 | -51.5019 | 2025-10-06 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |


[Clique aqui para ver as próximas entradas](README7.md)
