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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea1e38f-2e50-3696-8b7d-8e86790f7d71 | -3.4541 | -43.3618 | 2025-08-24 13:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4b9f17bd-b34e-353d-b27e-fbcc64f0e841 | -8.527 | -48.8609 | 2025-08-24 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 95ea03e4-70bf-30c4-acbc-236a55434a20 | -8.7375 | -45.4981 | 2025-08-24 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c574d20d-c5a6-3770-a451-f3c298a18d12 | -11.5921 | -46.2363 | 2025-08-24 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 284.1 |
| c830e040-ef7d-33c4-9d0d-809472fbbe55 | -10.9145 | -50.7698 | 2025-08-24 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ae9fdb42-4bcb-3cfa-ab31-e63aa721e66b | -8.4833 | -49.4032 | 2025-08-24 13:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7fd86e42-1823-3b29-a90c-160611b97603 | -10.4774 | -46.8982 | 2025-08-24 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| cac4cace-43a5-3d4e-9156-7efd9a998f47 | -7.318 | -44.5451 | 2025-08-24 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 07af4373-55a2-3551-b9be-2b412a3c628b | -6.4357 | -44.5535 | 2025-08-24 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 275.0 |
| 6ac6b7ce-2bfa-3fd4-83bc-fef2b37c4a09 | -8.5458 | -48.8592 | 2025-08-24 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 130.3 |
| f2833a5b-acdd-3410-9507-ad9b2b84f3b5 | -10.4164 | -47.1732 | 2025-08-24 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| dd3376dc-a4fc-384e-903a-a11b109bbf97 | -8.546 | -48.8376 | 2025-08-24 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 8f2b9afa-ceec-331c-ba86-b8ef30635dd8 | -7.185 | -44.6719 | 2025-08-24 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 10ea0ebd-a9d6-30a9-b278-d80891cda26a | -10.4777 | -46.8758 | 2025-08-24 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d9b502a5-59be-3ffb-b9f5-c73a41cd450d | -15.112 | -48.6459 | 2025-08-24 13:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0e87b9ee-a293-341d-8423-b798fc254087 | -10.4584 | -46.9005 | 2025-08-24 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 6bc891b8-c224-3fe0-9856-1631c0cdf2e4 | -11.6112 | -46.2337 | 2025-08-24 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 900dc751-1ef0-3e74-b38e-ee66ab909653 | -6.436 | -44.5306 | 2025-08-24 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 08bb1a2b-f031-3742-9343-674f2f0079ea | -5.4181 | -60.1784 | 2025-08-24 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d8f22776-05b5-308c-bb8d-2039f9f925ef | -8.4833 | -49.4032 | 2025-08-24 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 606722f0-4a7b-302f-8b75-0ee73528322d | -10.478 | -46.8534 | 2025-08-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 548e2c43-a21e-32fd-bf84-eb62f271ebec | -9.0787 | -65.7151 | 2025-08-24 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2072d981-02c8-36cf-880a-d97a6354bdc6 | -8.5458 | -48.8592 | 2025-08-24 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 53a14e7c-b8eb-3a57-8bfd-9cfae34c91bb | -10.6006 | -50.2058 | 2025-08-24 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 97ebeee6-0a6a-36e6-94bb-af01d3649be0 | -11.5921 | -46.2363 | 2025-08-24 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a66b7532-4a3b-34ff-8d86-489d5beffccb | -5.4364 | -60.1779 | 2025-08-24 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 634e7071-150d-3b4e-843e-71a1af106323 | -7.9447 | -63.0528 | 2025-08-24 13:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8724a14e-3638-363f-8d35-c008439e5a69 | -8.7769 | -49.9763 | 2025-08-24 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| ca2c02cd-e514-33c3-925a-aa3d3261c0a6 | -8.7582 | -49.978 | 2025-08-24 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 23fac5e9-d86f-356c-ab29-15727b205095 | -6.4357 | -44.5535 | 2025-08-24 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 456.1 |
| b02b44c1-ceab-3d3c-aebc-e456f3c1ddbc | -6.3431 | -44.4465 | 2025-08-24 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 9507ead9-4108-31cb-b992-25de2a5abcbb | -8.527 | -48.8609 | 2025-08-24 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 5675849c-ad85-31b9-beb9-6d3e3af7a3ae | -5.4365 | -60.1588 | 2025-08-24 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 766a4961-9d23-3795-b359-749043e40810 | -5.663 | -45.136 | 2025-08-24 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 99a716cd-84d6-3e23-a1df-e0784d3ef48f | -10.4774 | -46.8982 | 2025-08-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 672f28f7-3af4-322b-a5f9-9c8f2eeae4e5 | -14.2968 | -52.9788 | 2025-08-24 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6f5806db-dba6-33df-811a-36058a0060f8 | -10.4584 | -46.9005 | 2025-08-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 78248468-9b10-31ba-9ff6-0b2bfdb07512 | -11.7356 | -51.6984 | 2025-08-24 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ce74ffda-0bcc-3241-9ff2-b8d6093b6248 | -8.0685 | -49.6524 | 2025-08-24 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e928a551-a157-3b0d-9dbf-b21800ae7ce4 | -8.7375 | -45.4981 | 2025-08-24 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4663cfbe-6890-3053-a0db-4fec1451f839 | -13.4393 | -47.0287 | 2025-08-24 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 29e82fbe-f4e2-30d1-b117-bad8eefd8552 | -9.8208 | -46.4383 | 2025-08-24 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a4c4bd93-841b-3441-b02e-a158849247d7 | -14.331 | -58.6013 | 2025-08-24 13:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| de757ec9-5705-31fb-ab17-9e26f6071387 | -8.7378 | -45.4753 | 2025-08-24 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 17a33c71-df38-37be-bec9-63801e30e836 | -5.678 | -41.3987 | 2025-08-24 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 4e273cd9-7ffd-3d22-aad9-963db1becae0 | -10.4777 | -46.8758 | 2025-08-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 187.3 |
| fc82b12c-19c3-3754-8ea2-92316d191ddb | -15.112 | -48.6459 | 2025-08-24 13:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 05db1ebc-8a89-3263-8f98-0d3d343a54de | -15.1115 | -48.6682 | 2025-08-24 13:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 97fd2777-5522-36dc-b6cd-40d45220bb24 | -10.8075 | -46.4308 | 2025-08-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 608faa1f-779e-3ec5-8f3e-5e1b4df5e6cc | -13.5162 | -47.0393 | 2025-08-24 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bbc26f2a-2b38-3a2c-90f2-da64e9fc9c3d | -10.9145 | -50.7698 | 2025-08-24 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ca09d5b3-a39a-3150-b632-6c42c601afb8 | -5.6628 | -45.1586 | 2025-08-24 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a8ed952e-f9f7-3e22-ade1-d6cc84fe50b6 | -11.5251 | -50.4898 | 2025-08-24 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 65e4335f-04d7-3302-8f2e-a79112ab0ca0 | -8.0275 | -45.0027 | 2025-08-24 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0e2a27b0-1443-3089-9655-cc024772ddaa | -8.0464 | -45.0008 | 2025-08-24 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 29a05eb6-3925-32c3-90ea-ce629c51374f | -10.6006 | -50.2058 | 2025-08-24 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3b293144-dd7e-33ae-8f74-01dcf1405489 | -5.6628 | -45.1586 | 2025-08-24 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 5e26f972-81de-32c6-8a0e-955ed52eb834 | -11.5251 | -50.4898 | 2025-08-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 5ae7e81a-713b-3bab-8ec6-c1f3b5905462 | -8.5458 | -48.8592 | 2025-08-24 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a5d498d2-9439-3402-820f-a77434a9339c | -6.436 | -44.5306 | 2025-08-24 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| e9766ead-322f-34f3-b641-50d4d7f8e23f | -10.4777 | -46.8758 | 2025-08-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 29d706e0-e4a1-394d-9c3c-26e978ec9d76 | -11.6112 | -46.2337 | 2025-08-24 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1e925faa-9bed-3d14-a688-573eb035808b | -14.331 | -58.6013 | 2025-08-24 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 87c580c4-813d-3bfb-9bbf-4bf1a0436139 | -7.318 | -44.5451 | 2025-08-24 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 2d9ff4f7-3049-313c-98cf-db7f00662e25 | -15.6561 | -52.7153 | 2025-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e7b0fbb8-4d8f-3ab3-b95f-9e0121053394 | -11.5254 | -50.4683 | 2025-08-24 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 1d037e74-7c04-3a32-8619-d06473c4ae63 | -8.527 | -48.8609 | 2025-08-24 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a6b45689-6366-3888-a406-3b5c8abcb4f4 | -6.4547 | -44.529 | 2025-08-24 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9ae26cfe-ce8c-3045-88ee-f1c40fd0294f | -5.4365 | -60.1588 | 2025-08-24 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 49b5d6b7-7333-3fed-84a7-b74dc6eb7f95 | -8.0685 | -49.6524 | 2025-08-24 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 16c490e5-dbc0-34b3-9a67-0bdb3610a0ae | -6.1963 | -44.1134 | 2025-08-24 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 5338bc60-6bcd-3c44-b0d6-cd52ad082a2b | -8.4833 | -49.4032 | 2025-08-24 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 825a485b-a99e-3f15-818c-7ef422af3f42 | -10.9145 | -50.7698 | 2025-08-24 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 6b69bebb-7a81-38d3-90fe-f338a2f76ef2 | -5.4181 | -60.1784 | 2025-08-24 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4b511b4b-0479-31d5-95e6-1db5dd3d0e68 | -5.663 | -45.136 | 2025-08-24 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 80eb996c-9fdd-3a51-b90a-33f6c2576722 | -15.6565 | -52.694 | 2025-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b6895e66-878d-3c3d-935c-cc3a8bed5e6a | -9.8208 | -46.4383 | 2025-08-24 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 78751f74-f3d9-3037-88df-3c273a1b79e5 | -5.678 | -41.3987 | 2025-08-24 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| c4941166-bd3d-3b85-b47e-31bc60d5b065 | -6.4357 | -44.5535 | 2025-08-24 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 412.6 |
| d6ca962f-da59-3f06-8a67-cf347a28b1d6 | -10.4587 | -46.8781 | 2025-08-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d20eb112-b811-3a8d-8f07-ffe618972c3c | -9.5702 | -48.1724 | 2025-08-24 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a2a9b180-cc41-3844-abe3-a12ec2149b27 | -12.7463 | -48.1153 | 2025-08-24 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 61b54efa-f2dc-342f-a149-08a60a35d661 | -11.7356 | -51.6984 | 2025-08-24 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 35624698-e253-3349-8575-84491e398fdf | -7.9263 | -63.0535 | 2025-08-24 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a2edf0da-266e-3919-bc46-583d2b88a551 | -8.7375 | -45.4981 | 2025-08-24 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 261c1411-787b-3ff1-8570-31de0c8f3832 | -9.0787 | -65.7151 | 2025-08-24 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bedeb690-c8da-3259-9303-b003bca1a8b8 | -7.9446 | -63.0717 | 2025-08-24 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cbba2ac2-f0d7-3226-a905-6a373acfac81 | -11.5921 | -46.2363 | 2025-08-24 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d08122ea-db4a-3532-83b4-c621c5e80c65 | -11.9867 | -61.0214 | 2025-08-24 13:50:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 0194c670-5988-3ea9-b330-73afe7f0ae72 | -8.7378 | -45.4753 | 2025-08-24 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| d6f6cf5f-e5cd-337a-a2e5-88829d19db54 | -12.6748 | -47.8143 | 2025-08-24 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5d2c5688-d815-357d-a584-5a3465b8ca78 | -6.3431 | -44.4465 | 2025-08-24 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 6b7adaf1-1b63-3919-ae39-d05f47f1cf09 | -10.4774 | -46.8982 | 2025-08-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| e53af8a8-8702-3930-ada6-96ea85c816ff | -5.4364 | -60.1779 | 2025-08-24 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3ca11f67-eaf8-32cf-9e23-60fbd47dff45 | -7.9447 | -63.0528 | 2025-08-24 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 8cb068fa-0ec9-3bb6-8233-6b022c73bc8d | -11.1013 | -44.7708 | 2025-08-24 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 2bfbc59b-efd0-322b-9143-6c05802ed9c2 | -10.4584 | -46.9005 | 2025-08-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 280.5 |
| e7a5f3f2-b0e0-3111-bfea-d6869bc21c13 | -8.7769 | -49.9763 | 2025-08-24 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 57500c14-ee55-32ad-82bc-ce0dd6d7bef3 | -10.8075 | -46.4308 | 2025-08-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 58e8e16e-667b-31f1-9b57-fde067b785ca | -11.5251 | -50.4898 | 2025-08-24 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |


[Clique aqui para ver as próximas entradas](README93.md)
