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
| 9baf62e6-1362-37b3-a81f-6d67044e35a2 | -11.591 | -47.4496 | 2026-05-29 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1a3f065f-4a81-34e8-a576-d7117dcb91f8 | -6.4021 | -44.1658 | 2026-05-29 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f3efbe07-bce2-306c-9270-2f0268c1ed20 | -6.4021 | -44.1658 | 2026-05-29 00:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| eebba80d-f191-3f19-95fc-0e25c897d68e | -11.591 | -47.4496 | 2026-05-29 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 59525cc6-fa74-31d8-992a-aaf84eeb25d6 | -11.591 | -47.4496 | 2026-05-29 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4eb3ad2b-e743-3c59-9b90-51b320c78f04 | -11.5914 | -47.4273 | 2026-05-29 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 00299994-cdd5-3448-99cc-6a6d38edaa4d | -11.591 | -47.4496 | 2026-05-29 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3654079f-4ddb-3ce1-8782-49647cb02b38 | -11.591 | -47.4496 | 2026-05-29 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f9d85bbf-84c9-3d8a-a529-da6f82e3b9c5 | -6.4021 | -44.1658 | 2026-05-29 00:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9a015794-c49d-39d8-8987-fd23368edf78 | -21.81281 | -53.08606 | 2026-05-29 00:45:00 | TERRA_M-M | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d74b77d0-7870-32f2-93a6-b6bd7ad72446 | -21.40227 | -48.71759 | 2026-05-29 00:45:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 766de883-e66a-3010-bc68-e40ef61e1991 | -15.17464 | -54.8491 | 2026-05-29 00:48:00 | TERRA_M-M | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ab01786e-b0e3-3cc6-b868-2fa38af5784f | -16.17566 | -58.47644 | 2026-05-29 00:48:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.0 |
| fb22d194-f2c0-3e9d-9602-05ac436f823f | -14.64606 | -54.52276 | 2026-05-29 00:48:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aa82394a-93e9-3f48-9269-0c7feca910bb | -18.46657 | -54.71802 | 2026-05-29 00:48:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 077a891a-dc8a-3d98-8abe-cf9f64564bc8 | -18.2361 | -54.59556 | 2026-05-29 00:48:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 91e06929-f2f4-37d6-9f6b-2a0accb6f9b8 | -14.44537 | -48.90088 | 2026-05-29 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 5daaf0ca-20d0-3969-b1ca-96edaca4b08c | -18.46513 | -54.70813 | 2026-05-29 00:48:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 9fb7a01f-0b87-3473-95fd-ce4e8d549b94 | -15.90489 | -50.55248 | 2026-05-29 00:48:00 | TERRA_M-M | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 61a40984-9423-36eb-8695-6a44e4aa66ed | -20.73437 | -54.83632 | 2026-05-29 00:48:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d2fe522-203b-356b-905e-a858fe2ea88e | -20.73298 | -54.82671 | 2026-05-29 00:48:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba608367-18fe-353c-ab94-df004e124e7e | -15.82653 | -58.62018 | 2026-05-29 00:48:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 231ce8b3-56af-389e-bf66-fc4a55b751af | -15.78664 | -58.66177 | 2026-05-29 00:48:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| e9aeef25-2ed7-3500-9c1e-2d80b1730588 | -15.79976 | -58.6198 | 2026-05-29 00:48:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 64ad366d-1b5e-37af-822a-27ba7e7272cc | -11.591 | -47.4496 | 2026-05-29 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 53a0fe92-3ac8-3b26-beef-96a4d928e5a9 | -6.4021 | -44.1658 | 2026-05-29 00:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 81b30a45-d925-3ac8-a26e-7dab54464b8d | -11.77729 | -52.5126 | 2026-05-29 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 918609b2-3d60-37bb-afcf-7d1fcd91c346 | -11.44573 | -55.11258 | 2026-05-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4ab51297-f85e-38d4-a9d5-c1e896ee780a | -7.33842 | -49.87112 | 2026-05-29 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 3074cb9d-3950-37ae-8d4e-7436853c786d | -12.99048 | -57.78523 | 2026-05-29 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2548d057-8719-3a79-ac94-6bb7a6f700bf | -11.59407 | -47.43408 | 2026-05-29 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 3a20f761-58d1-32b1-9b31-c4b52d3d1ae4 | -11.5613 | -54.59032 | 2026-05-29 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e21715ec-b801-3e55-b704-f5f2a25fa933 | -11.78883 | -52.51064 | 2026-05-29 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f9378289-5d69-3880-bc01-dd0ad428f2d5 | -13.63599 | -55.75116 | 2026-05-29 00:50:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dceda96c-1fbb-3302-a919-5703a927045b | -11.60154 | -47.47554 | 2026-05-29 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 831ac083-76ce-3c74-ba3e-1509aab5dda2 | -12.98925 | -57.77623 | 2026-05-29 00:50:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d4caeed-1b44-36b5-92ca-a59be01edeaa | -13.63738 | -55.76083 | 2026-05-29 00:50:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e533573b-1445-3a00-a17c-25147c8c9896 | -11.79143 | -52.52675 | 2026-05-29 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2255f381-8874-3bbb-a251-bd9b95c1a492 | -11.78085 | -52.51756 | 2026-05-29 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 44887802-5389-3122-9d60-ca113f45112b | -13.18162 | -52.71227 | 2026-05-29 00:50:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 595ded8e-f37e-3cef-8ff4-a992cc92656c | -12.68767 | -54.58302 | 2026-05-29 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 314537d3-ee4e-38bd-bc2d-2ba6ae32a23d | -11.55955 | -54.57881 | 2026-05-29 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1fd436c6-aa2b-31e3-9ff4-d7f0a35e7fca | -11.30238 | -54.03658 | 2026-05-29 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 57876323-daa3-30b6-909c-6028303e0906 | -12.72097 | -54.19338 | 2026-05-29 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 14cc01be-cec3-3902-a96e-d3ad57e37848 | -11.59214 | -47.4426 | 2026-05-29 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 19483c9f-248b-3522-9715-aca27d9aab68 | -11.79239 | -52.51559 | 2026-05-29 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| dc894a7d-56ce-31a7-b23f-54a5542e078d | -6.57772 | -51.11929 | 2026-05-29 00:50:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| b55e256e-181a-34db-9204-4ffd7accfb74 | -10.13537 | -52.39742 | 2026-05-29 00:50:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 68995b5e-351c-324f-a933-76f1255d98ad | -11.6257 | -56.855499 | 2026-05-29 00:52:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f368b600-5441-3bc3-9be8-214e42dc56e2 | -10.1291 | -52.393398 | 2026-05-29 00:52:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f948e241-8e03-355e-8c24-d75dfe20bf41 | -18.462 | -54.705101 | 2026-05-29 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f7b4e129-206e-3fa4-8c17-f268055e0f81 | -20.7311 | -54.822601 | 2026-05-29 00:52:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c8737820-be43-3d99-8620-c92f0308dcf9 | -11.7799 | -52.511299 | 2026-05-29 00:52:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f79a9afa-154d-34b0-ac87-a7f488d7965d | -13.181 | -52.700401 | 2026-05-29 00:52:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 163881d1-9bc6-3af4-b263-7b0843f0522b | -11.6355 | -56.853199 | 2026-05-29 00:52:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd0ad35-76a7-384a-a6c1-434cd6abd8e6 | -11.3016 | -54.027599 | 2026-05-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a85d338-f86a-362a-800a-9a86f12a5f74 | -11.7896 | -52.508801 | 2026-05-29 00:52:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8509ab-15b3-3f8c-9c7c-1db2d3af9035 | -11.5563 | -54.572899 | 2026-05-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07cee92e-2e05-39b9-b9a4-ef3306152212 | -12.3681 | -54.1647 | 2026-05-29 00:52:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 370030c1-65a9-3905-a63a-75bc2373a2b4 | -11.5953 | -47.458599 | 2026-05-29 00:52:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b7130b2-6ed1-3b72-a173-b4391cf5b0dc | -18.460199 | -54.697201 | 2026-05-29 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5b190a-f72e-3094-9d43-a22f32158149 | -11.5978 | -47.429199 | 2026-05-29 00:52:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| badeba15-1b31-3e3d-832d-84c2dc4580c8 | -8.6841 | -48.305698 | 2026-05-29 00:52:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b807229-d11a-39e2-861e-af7f5bc3fe43 | -14.6551 | -54.5201 | 2026-05-29 00:52:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5f9215b-84fe-3abf-8716-a8b22bd65a09 | -11.5787 | -47.4347 | 2026-05-29 00:52:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12843adc-a82f-35a2-9454-fa7de4b983f3 | -11.566 | -54.570499 | 2026-05-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abc12a4c-49cc-342c-a2d0-89c0d6c9a927 | -11.5882 | -47.4319 | 2026-05-29 00:52:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8e93fc8-9aaa-3dc6-87e2-0e56907f73a0 | -21.3943 | -48.702301 | 2026-05-29 00:52:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6e775bd5-d103-3bf8-9fcc-5866aa4e09bc | -14.653 | -54.511501 | 2026-05-29 00:52:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c126dd10-e7c1-3699-a58d-d9e417c0cdc3 | -18.4718 | -54.702599 | 2026-05-29 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1f95b873-22a6-3a13-860f-ee8dea91a7d2 | -12.3658 | -54.1553 | 2026-05-29 00:52:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0c3036f-4221-3c48-8ad6-54151f87cab2 | -11.591 | -47.4496 | 2026-05-29 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 4e359462-f238-3575-a9d1-b19c6c9b8d9a | -11.591 | -47.4496 | 2026-05-29 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 25b28752-d13e-39b0-818b-c4ae3b9b683a | -11.6101 | -47.4471 | 2026-05-29 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 441141fe-ebc5-3fbf-9f58-79801b39e77d | -11.591 | -47.4496 | 2026-05-29 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| fc5e0b89-679f-3ab2-8178-b6bea5c6bcf3 | -16.1655 | -58.4842 | 2026-05-29 01:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.7 |
| 13992ce6-f690-304b-9a23-d5c06c8a9be7 | -11.591 | -47.4496 | 2026-05-29 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 805ba989-306e-32fc-9042-e29be71d49f5 | -11.591 | -47.4496 | 2026-05-29 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1bc70f84-2c90-349d-a381-ad39982e4c56 | -11.591 | -47.4496 | 2026-05-29 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2c44cdb5-0319-3eb6-ab40-ea424554003e | -11.591 | -47.4496 | 2026-05-29 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| faec6df5-e214-3aad-96f4-9326dc49fda0 | -11.591 | -47.4496 | 2026-05-29 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a9a7b295-4190-3f01-8904-1e033d17f5d9 | -11.591 | -47.4496 | 2026-05-29 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b823a5f0-5d1b-3c62-896f-c5a3174bc120 | -11.591 | -47.4496 | 2026-05-29 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| bb5af1eb-e3fa-3757-8f56-823643bfb338 | -11.591 | -47.4496 | 2026-05-29 02:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 050c864f-bb5b-34bb-a648-4403557fd067 | -11.6101 | -47.4471 | 2026-05-29 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8c21cfd0-e3f7-3e7b-bed3-b28a963d53a0 | -11.591 | -47.4496 | 2026-05-29 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| bcb23fc2-d548-343a-a262-8e4a2f5ad670 | -11.591 | -47.4496 | 2026-05-29 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3744af4f-3285-3486-9c5b-872ce82e46e9 | -11.591 | -47.4496 | 2026-05-29 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9bf74b99-3b08-3954-863a-e48cdda85495 | -11.79151 | -40.08254 | 2026-05-29 03:15:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9944cdb-5ffe-39be-bf42-5398fbcfdd79 | -11.79564 | -40.08381 | 2026-05-29 03:15:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d0cfa3b8-e08d-3647-bce4-965f4b9277f6 | -11.79028 | -40.08838 | 2026-05-29 03:15:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 378e6c5f-df81-3de7-8243-ed7b20f1dd9e | -11.79817 | -40.08392 | 2026-05-29 03:15:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6d747fd8-9210-3b38-97ab-72ee66d5e00f | -11.591 | -47.4496 | 2026-05-29 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7414d642-28cb-3c73-84ed-c57c50133f72 | -11.591 | -47.4496 | 2026-05-29 03:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e45f6e3a-29bd-337e-99c0-9381edf98e0f | -5.95459 | -43.48983 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f789945-5edb-3454-b686-3afec67b594b | -6.75811 | -45.02063 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4945f861-4979-354c-b370-79da02397c7e | -5.94925 | -43.48377 | 2026-05-29 03:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab1390b9-f9c2-3f77-a136-9009364e6eeb | -6.03573 | -44.0058 | 2026-05-29 03:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42aede8b-0f4e-345c-8e16-5afc850634ce | -6.39437 | -44.16681 | 2026-05-29 03:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fc937dab-9196-31f1-95ca-0a24034939a6 | -6.76625 | -45.02731 | 2026-05-29 03:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
