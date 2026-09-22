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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 807cbd71-56bf-36eb-ae36-002786bfb6e0 | -8.2557 | -55.296799 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c516be9-2fd8-3706-9ce5-fdc13f833e8e | -3.2169 | -61.047298 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57e0d409-2624-3806-ace4-af95e13c098b | -6.445 | -59.9683 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3797f733-dc4d-3eed-a382-965ca2034b7a | -6.7404 | -59.413601 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eea1dd1c-0611-3a05-9ea9-f8a4aa591c10 | -3.2876 | -57.854801 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6021748a-d819-38b4-b50d-fbbc58bdcbc6 | -3.0496 | -61.263599 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6993708-7954-3b59-a9a2-dc6c3bdea69e | -6.4274 | -55.621101 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d437c6b-6c5c-379a-bccc-5b8843d67fe6 | -10.6012 | -53.9646 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35615efe-f9b5-3590-a649-848f81df0f40 | -7.2352 | -55.596298 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ecd9092-eee6-3b5c-aeb5-3a0eb0cee11e | -6.1586 | -57.708199 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480fa393-03c0-3e72-8770-62dde570d4bd | -9.5467 | -65.672501 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e876d2b8-940e-37ed-b371-f8dbd9369080 | -6.0435 | -57.832802 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d306d28f-b141-35a5-8174-aa4d929937a4 | -3.3368 | -59.856899 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b113c9b-31ac-3599-94ec-0b4097567db8 | -3.0612 | -61.2239 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35093ca7-dbfc-30c8-afda-06d3a9d77cac | -8.6077 | -54.624401 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6767b2-9e03-360e-90bd-8bb2502bd9af | -3.3956 | -59.259602 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07fb4d13-ce75-3567-a0ca-7545a4f58073 | -6.1858 | -57.780102 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6b91827-ec5b-3220-bf5d-69b2b4811ac1 | -3.6807 | -60.594799 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a83ad81-25e0-3357-80cd-29f6903e7bf3 | -12.7791 | -54.0396 | 2026-09-22 00:57:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a78624af-0368-3521-b714-aac88cb17f04 | -3.335 | -59.849098 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c142ee0-787d-3f6e-8de7-6cea141b0d53 | -6.1193 | -59.942101 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05101f6b-5b2f-336e-b5bd-2775e51004db | -3.3647 | -61.289101 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ba86a61-7e39-3c2a-95cb-bda3129c54a6 | -6.0294 | -57.816601 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c39096-1b62-3b46-bb7b-8d2bb7fe70db | -9.1388 | -67.918999 | 2026-09-22 00:57:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 109fdf27-7517-323b-a511-152543653819 | -6.6829 | -58.452301 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6ebc72-e722-36dc-99aa-1dc8a1146b85 | -3.0892 | -61.1656 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c914e432-5439-3a99-9161-92c8e2eccab2 | -6.1334 | -59.8689 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fea677f-6819-3a2a-b8ce-60158f31e036 | -6.0619 | -57.867298 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3042d5ac-06e0-3287-8e26-801fce87b38e | -6.6197 | -59.9207 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b88d409-f56f-3850-af25-ff6393646ea8 | -6.618 | -59.913399 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfd00e9d-501e-3736-81d6-5ea62381a244 | -3.1104 | -60.7155 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0359db03-146b-36e0-a67f-0c2384071c63 | -3.6445 | -58.8643 | 2026-09-22 00:57:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb35b142-c75e-3a13-82e2-e87fc54c75e6 | -6.4615 | -59.9953 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5808c4f-9cd4-3c61-ba8a-d03d09582120 | -13.2858 | -51.761299 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 527c4a68-4237-3a6d-8634-11b1032d8fbd | -6.1308 | -59.947201 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b587d5c-c4f9-33b8-8b4b-45c58bf55cdd | -4.4006 | -55.231499 | 2026-09-22 00:57:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3671406-d27e-3c2c-93b8-73a88e55df04 | -3.2756 | -57.847 | 2026-09-22 00:57:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d53d993-de17-34e7-a94a-7d205ad620f7 | -8.2459 | -55.299198 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 251e3c2f-3139-32ce-8bcd-d170a7c47f5c | -11.3092 | -54.030102 | 2026-09-22 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f913224-eabb-3b7f-880e-73452742b51b | -2.8541 | -60.902699 | 2026-09-22 00:57:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4aaeb8c3-779a-3241-9001-f0ba448a03ba | -9.2862 | -58.912102 | 2026-09-22 00:57:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b23f1c9-0a86-31a2-932e-ad0eac392558 | -4.9527 | -55.825401 | 2026-09-22 00:57:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870c601e-1162-3dca-b861-9ac93ef74fef | -8.598 | -54.626801 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67fa7f2-60f5-374e-b3ae-4e439b67ff68 | -2.7843 | -59.874401 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 866614e0-3c35-385a-807c-6b561a31612e | -5.4324 | -60.2295 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87b7aef4-f681-3643-916b-a9db8cf7971a | -11.319 | -54.027599 | 2026-09-22 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81296dfa-b328-34fc-b6aa-90b7e89637ac | -6.0802 | -57.637501 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72dee797-6edd-3437-9e0a-2db415f6a945 | -3.0582 | -54.4156 | 2026-09-22 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0374480e-fe06-33c6-b972-9db844503f8a | -5.7544 | -56.515701 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0ad946e-c60f-3f3e-b46f-dbfee5d68ce1 | -6.0998 | -57.6329 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18d702c7-aa75-3b64-bbf0-6cd3e8aa586f | -7.3907 | -55.214901 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0405e75f-ba36-3c5b-81d4-5e47f7087e9b | -3.7726 | -60.726601 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b327c40-963c-3733-a55e-ffcbcbaa84a3 | -3.395 | -59.5266 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7437265-fc90-3b19-bcbb-4f8c76598bd7 | -6.7145 | -55.0588 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3481a279-307e-36b8-828d-15b2856fcd02 | -3.4124 | -60.187199 | 2026-09-22 00:57:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85ef9db9-a46b-36f6-a9d3-05ce9528850e | -12.9212 | -51.037601 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8072f563-4eaf-33d9-8054-44a72a6ab175 | -12.1448 | -61.1591 | 2026-09-22 00:57:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a38eae7-4714-368a-85ac-b7c91b9a5a77 | -10.2134 | -53.898998 | 2026-09-22 00:57:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e446336-19ec-3ddb-9ca4-47a61e463d2d | -5.9816 | -57.700298 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7356f68f-3399-31d2-b3d2-3f0f45b69849 | -3.0544 | -61.284698 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3827f9a5-9464-3674-83e9-d051dc0456bd | -3.4863 | -59.565102 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c363c822-64f0-3ce1-8f8d-35da25c336e6 | -7.5937 | -57.6712 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c008550-d42d-3c35-8c25-5b9ab07f750f | -3.2899 | -57.8647 | 2026-09-22 00:57:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 932d14a2-f2cf-3977-8e00-c4948296fcb6 | -10.5915 | -53.966999 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de888bae-b00e-358a-8961-af903f4a7882 | -6.706 | -58.996399 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8a58f72-1fdf-3582-970e-0c59e1a7fc18 | -7.3287 | -55.5994 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc050c9-ff24-387e-9a58-261bdf1ce619 | -3.9361 | -59.638699 | 2026-09-22 00:57:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d92e335-5a02-311b-bc7b-d80d2dda646f | -6.4663 | -59.9711 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1dc0e3b-6b0d-3802-8705-dd56b4ed8137 | -3.6791 | -60.587502 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5dec2bf-b8b4-311d-b492-5af1d7ac8418 | -6.066 | -57.620899 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67062b0-8028-37c9-96e5-9c887f85ec60 | -7.3066 | -55.208099 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78bb8df-1d80-3bd7-b3d5-ae475f850369 | -10.5852 | -53.983299 | 2026-09-22 00:57:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28c6afdd-e1e9-3822-bd39-c66b0ab93e21 | -13.2711 | -51.784199 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f47762b-2fbb-3a1b-91d3-896280d95827 | -9.4011 | -65.903198 | 2026-09-22 00:57:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14ae442e-6e5e-3454-9788-7a94af779095 | -5.9412 | -59.974899 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09659865-03b8-3a6f-a0aa-32e3c84fd433 | -6.7082 | -59.453098 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4320554-486d-3ba9-ab32-4bb581eabd36 | -3.4071 | -61.2943 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6675a2-d633-38d2-979b-7bf068569488 | -5.9089 | -55.692101 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d52508-750d-3436-b5e0-606231f6f6ca | 1.5482 | -55.729599 | 2026-09-22 00:57:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4e09d8-aa7a-32c0-9b55-897bdb022acf | -13.2762 | -51.764 | 2026-09-22 00:57:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90f11a20-48eb-3058-9b9d-76e37f3b268a | -6.2793 | -57.738899 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3ea625-1cb2-37aa-af72-f0351236882e | -3.3386 | -59.8647 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5362f3f-c35d-39f8-86f1-8be8ff074c3c | -11.3159 | -54.056801 | 2026-09-22 00:57:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d819c84f-aac5-3a35-a570-b2beda8d97fb | -6.121 | -59.949501 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8a8cf7-3b25-3fa6-bc70-6bbf6288464a | -6.7306 | -59.415901 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1035b9b1-41b0-31a0-81c0-84d012a52a73 | 1.5546 | -55.8834 | 2026-09-22 00:57:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3a4e52-5776-3941-8105-5d3aa23b259f | -3.8966 | -60.592098 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89896c8e-155b-356c-8e18-644bb7832c10 | -6.8826 | -59.852901 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb29f9e4-af58-3448-a13f-5b067acc2952 | -6.3484 | -59.951801 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4acd392d-4d57-34a2-bf5b-4072b5e0a5c4 | -4.2205 | -63.068501 | 2026-09-22 00:57:00 | METOP-B | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc2331b1-40fb-36b3-a45b-9b465e29d3f0 | -9.5664 | -66.0084 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d57c3613-700e-3076-b4c1-0b14e48cb894 | -8.1476 | -54.808701 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| becdf69f-7930-31ff-aa39-83eab1535e28 | -6.3095 | -60.006901 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a99bea68-d47d-3f00-b5ca-85f4af968036 | -6.7528 | -59.110001 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8ec1972-54ac-3163-91cf-b70d09946d99 | -3.6839 | -60.5634 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab3d8ea8-7bf5-32a3-b621-d3c29c1dbb45 | -3.7743 | -60.733799 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 925c07a2-890f-36ec-a607-134a69885bb0 | -6.0891 | -57.675098 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5145b91e-1b94-35bf-9995-df212cb7af56 | -3.0542 | -54.398499 | 2026-09-22 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f394cd6-8f73-324f-a38a-6c584577ad7a | -7.0802 | -61.081699 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64ef8180-9173-3f16-a721-e4ba49e918b1 | -6.3465 | -57.762001 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
