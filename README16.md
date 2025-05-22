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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81f45438-ad0e-3077-9f3c-6de653bdd23f | -4.29031 | -48.27497 | 2025-05-22 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d01af65f-531e-33ee-8d77-ca87832c75b8 | -10.71327 | -48.81006 | 2025-05-22 04:44:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c277647-1759-39a3-9050-9348e2f1bd1c | -9.96227 | -49.82033 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca15a9e2-b1c2-326e-9e49-43873adf7684 | -11.60807 | -47.62136 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 347f7461-5bae-305e-8164-7d2b2086a702 | -7.80337 | -46.21622 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c70105c7-c29f-3aec-b492-191fe3c6a69d | -9.96056 | -49.80852 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33dc7541-18fd-3c6e-8666-03342555f260 | -11.24407 | -49.49727 | 2025-05-22 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fae16306-a4ef-384c-9dcd-5fff64f58e1f | -7.23745 | -44.71568 | 2025-05-22 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd4a0afd-5d07-34d7-899e-6a9b15b1475a | -10.5957 | -52.85002 | 2025-05-22 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35ec5064-782c-398e-ba11-f35fc92dbe76 | -10.62396 | -51.79202 | 2025-05-22 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16177fb5-a6b8-3e0c-bb21-fee20e6034f8 | -9.95998 | -49.81228 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae96ea4f-6012-306b-bb87-30afff1b0748 | -9.79697 | -48.25952 | 2025-05-22 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8755c3c7-eb2a-3747-a70b-39d56738ead1 | -10.87724 | -45.07667 | 2025-05-22 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b51701a-03e5-3338-86bf-21187b50a46d | -8.62185 | -51.54633 | 2025-05-22 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baa2b4c8-3191-3c5f-bca4-411702537ace | -11.60025 | -47.62029 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 045b011f-5212-34bf-af09-2b112a811432 | -12.0794 | -47.34659 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b12a226-3e1f-339e-8d35-1ac2902eeec8 | -7.23809 | -44.71122 | 2025-05-22 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5807c14-b32a-3303-8f3b-bbd6135a8ffb | -12.07757 | -47.34256 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eee69a3a-b8bb-392b-9831-846983c5611d | -8.75138 | -49.75023 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ae5ae203-4867-3641-8c36-25f28f3a63db | -10.37047 | -47.97776 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7de9e1d-6e0a-3d38-9336-72e5ae54e1a6 | -10.87771 | -45.07408 | 2025-05-22 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 804cc083-acbc-36c0-b29c-c994485bb2b1 | -10.12183 | -58.22155 | 2025-05-22 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd5f79f-6411-3816-acd8-b653b07f3239 | -12.08157 | -47.34315 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b34e684-391d-34fa-a6b5-c7d12d6748d2 | -8.47931 | -49.60707 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f874f778-5dd6-378d-af24-f95562a7c861 | -6.63052 | -55.00993 | 2025-05-22 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0105e70f-5e60-35d8-9ee2-b519c26eddf0 | -11.24465 | -49.49329 | 2025-05-22 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f254620-be46-3938-97e7-161443902414 | -10.38175 | -47.97947 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af48a2f4-7447-3bd9-a38b-d3538641c994 | -9.03365 | -48.93817 | 2025-05-22 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b26f146-9ed4-3f65-b4a9-bd174c0372a6 | -8.90954 | -50.02174 | 2025-05-22 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90fa358a-40b5-3cbf-bc27-d6f74e2bd044 | -7.3915 | -45.93819 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 327dcc52-5cfd-3ba6-ad64-b1c22e64330b | -9.96399 | -49.80905 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e2bf21e-e77a-31dc-911a-bffd7ba98124 | -9.04646 | -47.0153 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d62f8999-fd69-35c1-ba2e-d3f5b9ab03ae | -10.36801 | -47.96803 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4a3ae881-de74-3f98-98a8-78f606075b7e | -10.8779 | -45.07191 | 2025-05-22 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0770bca3-ee25-313b-906b-b9ead68aa771 | -11.55976 | -47.45247 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c9cd5381-8d97-3bfd-b7de-3d5cdb0bc312 | -11.60734 | -47.62446 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d8facce-9d1d-3478-93c9-60ede6fba504 | -11.60417 | -47.62081 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d61f5510-99c9-35c9-8686-ff98757568f7 | -11.57304 | -47.44384 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 11724f02-4a4c-311e-909d-b81be9c83f13 | -9.67479 | -50.95798 | 2025-05-22 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a856844d-d1f6-3669-b83b-9f3434cb3683 | -8.78471 | -49.07653 | 2025-05-22 04:44:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5871c35d-a650-3c68-ab79-7fc63b05605c | -11.64216 | -48.10051 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a43311b8-0b7f-3c38-b0e6-4b24c911e2ba | -10.59961 | -52.84701 | 2025-05-22 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab7a715d-7c4b-3b2e-ade6-6775adcfa33f | -11.57554 | -47.45468 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 97ab76c3-18f6-30f4-8299-2374d1082ae3 | -9.96685 | -49.81334 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bf64e01-8b16-3ba2-8b79-f6db221ae28d | -11.64592 | -48.09892 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1a331ee8-a368-33ac-a562-641a888ba60e | -9.96742 | -49.80958 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d14454c-2f20-3397-a6f5-a430c0f679d9 | -9.96284 | -49.81657 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f3683e3-76ad-35fc-8f76-f4b793c94ed1 | -10.02731 | -48.69609 | 2025-05-22 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 104b78d5-d060-3209-9af0-1e9766364e1d | -10.38264 | -57.64311 | 2025-05-22 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e95ae1b8-fa77-34cf-9845-04e3bd63425a | -7.96937 | -49.69257 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3d3b8cf-2cd3-3319-bb9c-ac395b46a94b | -10.29924 | -57.14261 | 2025-05-22 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8a826ee-fb19-3ea4-9072-b8e60edf51dc | -12.08041 | -47.33956 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2010026-420c-327b-8878-c2858cec9bc9 | -9.04573 | -47.02036 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10297698-829f-3008-9faa-691299c8c916 | -9.33229 | -49.91262 | 2025-05-22 04:44:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8423fd71-1d8e-3891-9f22-8ad8f8a71d4a | -10.03092 | -48.69659 | 2025-05-22 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f616ff3-e33b-3729-8ff4-210475c4bb5f | -10.46545 | -49.14614 | 2025-05-22 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3edd0119-9cee-3f22-8488-9e254bdf9497 | -13.7144 | -57.4789 | 2025-05-22 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d08c9cac-73d5-3d52-a995-e833cb56ab5c | -13.51853 | -43.69493 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac3c3f3d-8090-3fe6-8a23-6e9702257984 | -12.42134 | -54.36033 | 2025-05-22 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9eeb14e-1760-3811-91b0-1feb7bfa1816 | -14.03049 | -55.13595 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de0190d9-c1ed-3cf0-bc93-00e48fde2c53 | -14.03722 | -53.37737 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23ac3807-e9a7-3928-808c-206a681193b7 | -12.29172 | -52.50055 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ca142d0-3a61-398a-8712-652c3fa7518b | -17.35871 | -48.79716 | 2025-05-22 04:46:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0004473-c21e-3277-adbd-ff7cf2e2cf8c | -15.56777 | -47.85406 | 2025-05-22 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af64df11-25da-3280-af90-4ab4f595fb80 | -11.67062 | -54.93901 | 2025-05-22 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1504dd8-c3b4-3ea8-9dba-0a44a9142d30 | -12.68749 | -58.12765 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b21fe90-982c-36eb-ac87-882a17246bfd | -13.531 | -43.68007 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb932e25-0e6a-3c84-b0f2-009c9ce38fc6 | -13.80865 | -52.89412 | 2025-05-22 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2876ed0-f294-3d4d-a2be-ec47ff941b62 | -17.61913 | -54.17554 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f518f94f-7a36-3490-b619-968d617cc60e | -19.11494 | -52.69397 | 2025-05-22 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ead3540c-e99c-3b32-aa14-5cec4c42f0bd | -14.02984 | -55.13988 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcc9194b-79e5-3404-9d73-c7236394ad1b | -17.27127 | -42.65289 | 2025-05-22 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 869448db-81d1-39b5-83ef-4c6b82b50266 | -12.48368 | -57.18762 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4561490a-24f5-3af5-8610-effc23189d54 | -12.29339 | -52.48998 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bfaa4f70-9b45-35e4-81fe-05d7322f3c11 | -12.02837 | -57.10081 | 2025-05-22 04:46:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1772eeb-66db-3ac4-9a8a-93a2d7a23df2 | -13.38614 | -48.45403 | 2025-05-22 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e15cb1e-6fc0-335b-9f28-42a6c336202a | -10.67711 | -57.60174 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bc810ee-ad31-341f-af92-d6de1366830e | -19.11942 | -52.68706 | 2025-05-22 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b7d5b4a-135e-31b0-a8ed-30f8a50a70bc | -14.03058 | -53.37624 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d95ef5a-50a4-3165-8e5b-a8ef8f945172 | -14.05375 | -45.51513 | 2025-05-22 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1ff88e8-4a8e-30b5-9d69-f0c6abd6fc3d | -12.41209 | -54.18044 | 2025-05-22 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76100356-848e-390f-81be-b466c0e38a39 | -19.11606 | -52.68649 | 2025-05-22 04:46:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c79121f-29a7-3805-b75e-d47a84e8fcb1 | -17.61307 | -54.17078 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05bfb9c9-2ba9-3815-99a3-7f67f99af4b3 | -13.51923 | -43.69608 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1477da3c-9924-3976-9eed-ae6b24ba5be2 | -10.68612 | -57.59941 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f804fc0-1c61-31cd-83d7-b98921d43811 | -12.13286 | -54.66393 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ed8050-8b54-3bde-92ec-a24ee5314c91 | -14.05179 | -45.53002 | 2025-05-22 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5025ae8-3a1e-392b-a43a-9c18e6f5ef3d | -18.81169 | -48.52331 | 2025-05-22 04:46:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6eb18ef-ca1d-397d-95a7-e8790cb97996 | -12.1335 | -54.66005 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59eb35a2-1446-3e6a-9ba8-0b24f37ea723 | -11.64646 | -58.26533 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49170f80-452e-3d6f-808c-a01170603997 | -12.29671 | -52.49052 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 788c58d1-3130-39cf-ad6c-7b5b40dc710f | -11.57562 | -54.57253 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dc712df-988b-3f24-a1c3-58744577b405 | -12.47403 | -54.46621 | 2025-05-22 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f708ac1-799c-3ca8-807e-0339595b17e1 | -13.4925 | -55.66694 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5df35ca8-14f0-39e2-b5df-6b7305803e4c | -12.36083 | -49.98077 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bac8ccf6-4394-3752-84a1-30101ad346a9 | -14.01723 | -55.1296 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fdbe350-065c-395f-8cad-7537537bd623 | -12.03477 | -54.97286 | 2025-05-22 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 802b52f4-5e40-3c17-b0b3-253b3be31ac3 | -13.53197 | -43.67796 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a0f9db7b-f7dc-329d-b5a9-719bcbaa5dac | -11.00094 | -56.92226 | 2025-05-22 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dce71b7-fd97-3641-acde-b5eb5c321e0a | -11.10337 | -58.42582 | 2025-05-22 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
