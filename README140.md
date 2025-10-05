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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e1e7656-14f9-3e31-aab6-e4e00adde413 | -15.50709 | -46.85017 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4910e50-0e96-331f-a6c9-c96da060c3f1 | -14.01305 | -44.93011 | 2025-10-05 05:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bbe5b160-0b8e-36c6-8135-0c2ae01f6025 | -15.59345 | -52.51136 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37456a8c-5dea-3495-b62b-7f7d31eadde3 | -17.95993 | -57.56923 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4c2eeea5-db57-3942-ace9-6a2779c32693 | -13.37902 | -47.54958 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fec1a2a-2fc0-3efc-9184-8d1a84743c35 | -14.74408 | -54.62088 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e88796a-c5e3-37fc-ba6e-a67ede51fbed | -14.29992 | -52.92495 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 790ca4a1-8505-3b98-adb4-7a8affd8a8ad | -15.50323 | -46.84887 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7ada7ed-b41f-33b5-8909-32814b535c84 | -14.33209 | -47.66776 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6bd604c-3481-3929-9518-f451fdae0db9 | -10.10155 | -65.03694 | 2025-10-05 05:16:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e94f879-4a4d-3493-b9e0-854e3c04e698 | -13.72806 | -48.07596 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e0ae26dc-61a7-3834-8814-5469434f044c | -13.13667 | -50.89512 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bc977a7-ca90-3701-9f5d-c99a4c6ca7d6 | -15.31735 | -56.93385 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31d863be-9862-3156-a83b-92d6213164ba | -16.79965 | -54.11273 | 2025-10-05 05:16:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f47033-876a-38bd-a4f0-0d0a5d171917 | -18.15572 | -53.32457 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cac8722-c503-32d3-b25f-780eb06eefef | -10.83776 | -57.17268 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65fc1f98-d748-37ba-ab0a-135af938c61d | -11.39498 | -55.17271 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a8a8fe0-3c18-3fd9-b2e5-ce951b0ec061 | -17.91774 | -57.61271 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c63e341-38bf-3101-b2c2-87a63a67718e | -12.97991 | -51.00798 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98f6a5df-1e47-3cf1-946f-41d0dfcf0238 | -13.26215 | -47.81367 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fa871c7-6bf4-3771-b2a9-be44a6753422 | -14.5689 | -52.46409 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 069ff6b2-40fe-31c7-9d36-4524297a35d5 | -13.12455 | -47.97913 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6177a58a-5d94-3439-b8c7-6c4519299e65 | -13.09647 | -47.85214 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4a4b8cd-e5c7-394b-80b1-84ba590aa969 | -16.36616 | -51.46915 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d3576f7-c240-3a84-9870-14acea969f95 | -16.03782 | -50.94785 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 385323b3-0d2c-3039-8d8f-c93cd2abfd3a | -13.25994 | -47.61848 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc6ad8d3-9a9c-39a7-b876-96a04e02877f | -11.50105 | -54.46256 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecf7f6d9-7bcc-38ae-8605-cedd525bfb44 | -14.94569 | -46.85104 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e422b42-cd4a-3c95-90dd-dd4a349edc40 | -16.14969 | -57.57895 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c04b653-58fa-354b-832c-ccea8c971b95 | -13.47677 | -47.28193 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5005bc07-b70c-3f33-8589-4fb39617061e | -14.67578 | -48.35751 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0530710b-9c6a-338c-b145-d675fb5ce5b7 | -17.89909 | -57.63976 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e42e6f86-852c-3b3b-88a8-c8d374b21fa6 | -10.66234 | -58.76388 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e6934a8-2bf0-3727-916e-56bfab9205ac | -12.92881 | -54.72575 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe28aa8a-1c3f-3999-a35a-5b744fa20d0b | -15.98398 | -50.91769 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61e01ae6-519c-37a4-afc8-c368bab263c4 | -12.60347 | -48.12429 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8f15f2a-a17f-3e99-915b-250651cece5c | -16.34659 | -51.45993 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f850387c-c916-37e2-956b-6e3f5ac79e06 | -15.91196 | -48.83231 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 675d560a-2bab-3b96-9779-dc5c1be420d2 | -17.95863 | -57.55334 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4f013000-d868-3724-97dd-f3d4fcd35fa2 | -18.14434 | -53.34233 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d20d4dd5-b73b-3d3e-8a7b-166d92e213ac | -13.142 | -50.8968 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63d5e4db-518c-395a-8408-1ca8ec337b76 | -17.11309 | -48.92437 | 2025-10-05 05:16:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01d8df91-6c04-3fce-b594-72600101e9b3 | -14.68501 | -48.34835 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1f1f6b6a-b56b-3f99-b8bd-82ee90deea38 | -12.30975 | -55.12331 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b036dc16-7d89-3618-a1b5-15cb43aef2f8 | -14.75476 | -54.65974 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf25f8df-63e8-32e4-a7e7-ac774310e6ed | -17.97188 | -51.15023 | 2025-10-05 05:16:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8c5d643-a6d8-31a2-ab78-f20d751a0b71 | -15.98652 | -50.92122 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8ad1cad9-5553-36a0-bb81-e86e20fce970 | -15.22731 | -49.29424 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cfbd42ac-779f-3843-bf51-f58103e2efc2 | -12.3102 | -55.14619 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 805d2034-14a4-3f2b-b1f1-ba189da8ed16 | -14.68232 | -48.35319 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d0933cf-0f97-3449-ae82-1e77a83f4b85 | -19.01967 | -50.60457 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 79f41b0c-dc63-3fb6-91c6-a370f88b28c7 | -18.17026 | -53.36558 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94e9f240-c754-32d8-8e8d-fd6a66f47913 | -10.83664 | -57.17993 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7de96a2-812e-3c78-87c0-4b42c0f3a24f | -12.97145 | -51.03482 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cfa11357-5ebe-346e-9e03-18c870ced522 | -13.13815 | -50.88382 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce35d6f9-93d7-3973-8050-ecb78da2345c | -18.19409 | -53.35725 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 394aa37d-43f4-30ac-acdb-5a994f30d3ee | -17.95703 | -57.58929 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0978e848-f0b7-3aa1-a882-3d72a815e2de | -13.08362 | -47.91147 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bc44e23-3ce1-3dbe-99eb-013cbc3842a5 | -15.78249 | -49.09222 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6352acd9-b1a3-39e1-9971-331ccbc81a6b | -13.10578 | -47.93108 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a0c844-24df-38ec-81a4-05f84651f840 | -16.38643 | -52.15932 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| afba7711-0739-35dd-a59c-60dc6f42e0a3 | -13.45933 | -47.29104 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aed6341e-2421-348d-9f25-9775416eb3c4 | -13.34281 | -47.5932 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91d3ecdd-026c-3c42-bf08-e6b9d250ce5f | -14.75154 | -54.65395 | 2025-10-05 05:16:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aea0733-94a4-37da-8906-3de79c3db699 | -19.01493 | -50.59704 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1e5515a6-d2b9-34de-8a9c-f58bfbd3cfd1 | -14.67673 | -48.36934 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f3ebe364-db08-3562-89ab-27b77815cd1d | -10.84013 | -57.18753 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95fab86-2512-34e9-9022-9b23377d4a8b | -15.22587 | -56.79721 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57b0b56d-3dac-3473-9be9-cf6691d03c15 | -12.45047 | -44.74259 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf242044-0b43-3f00-8633-a8aff7315360 | -16.36504 | -51.47423 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44ad763f-95ed-3759-bff6-127be1cd718b | -15.58607 | -52.49534 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12f96684-0d70-370a-8af6-e8682857f8a7 | -17.94414 | -57.60386 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cc43d6d5-134a-3c50-866d-e1db78892658 | -14.67904 | -48.34762 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9d40d67-7fb9-36b6-a89b-9c90afe98cd2 | -14.69009 | -48.35742 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 79dbe014-2022-3294-80d5-f0ffec418c78 | -14.94449 | -46.85096 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc84986d-a8a9-393a-b26c-1ce26cbc0a25 | -16.3519 | -51.4614 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fe8e527-bf9c-37a6-823c-f5fbfb08c3b7 | -16.07336 | -51.08484 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b318ac2c-4246-372d-9a9f-309aa99fb4ca | -15.23697 | -49.31063 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f951899-0aad-3b4e-a3cb-247fc428b314 | -12.26451 | -55.12094 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc44781f-da67-3a91-8289-1457df71c817 | -14.31884 | -47.6739 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e00733-896d-3572-8f6a-c63e11e81ba9 | -14.3366 | -47.68357 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 823aaa0a-2949-3d40-81cb-9de317569dfa | -14.68296 | -48.29401 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81292c64-7607-366d-9452-d64bba1a5fb7 | -15.9402 | -48.99328 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67799b62-61b9-38ff-918b-7ba24dbb60ad | -13.3188 | -48.07242 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6fdc085-0eda-3e6a-b3ee-3a4494394a96 | -12.60074 | -48.12498 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83abe3c5-62a5-3aba-937d-328712a8ab0c | -12.31633 | -55.15611 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d46a7dd4-d00b-3a79-becd-5449c1a19fda | -18.25073 | -53.34293 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e95ec779-703b-3e1a-a83f-9bed04ff39fc | -17.89208 | -57.63866 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 755379f1-b7ab-36b5-9d20-680544858bfc | -12.30278 | -55.14506 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb81cf05-d855-3b35-a8e2-429ef1dd0eaa | -13.72997 | -51.30782 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2f7c100-8792-3bf1-a090-0a8d78ff3e9a | -15.58229 | -52.49126 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1234c849-e830-305e-9e36-a565c746587d | -11.95285 | -51.47302 | 2025-10-05 05:16:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74244b55-d44f-3b08-8d09-77479e7fc1a5 | -16.38116 | -52.1623 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f5093746-b47b-3e55-acc3-659c0c8f4609 | -16.0075 | -50.84848 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10b15b4a-efe5-3172-98f3-52b565d7b83c | -13.49634 | -47.27793 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54c08f2a-1f53-3f88-8eb7-d89401aa06a1 | -21.68823 | -48.41882 | 2025-10-05 05:18:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b064fcb-f814-326f-933d-314ad28800e2 | -22.37022 | -46.88832 | 2025-10-05 05:18:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 587752ff-6a1e-358d-81b1-0769209d721c | -22.37077 | -46.881 | 2025-10-05 05:18:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afa28f34-5f2f-3776-9497-a26e5bfc5c99 | -21.68132 | -48.42403 | 2025-10-05 05:18:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 930d4f9a-543a-3c10-8b05-fcd3b4ee8f32 | -21.82678 | -47.39601 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README141.md)
