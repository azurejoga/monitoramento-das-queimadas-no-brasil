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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 389910e4-2ddc-3828-a635-d1ac9bd15aad | -10.78176 | -68.48976 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6486145-4b09-3293-884c-f03136be13d9 | -10.76882 | -68.80662 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be83b25d-7e2d-30fb-89df-c75d1913cc65 | -10.71124 | -68.6155 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c86b2e98-fc65-3784-a4d1-f0d826728377 | -10.69464 | -68.63644 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9cb81bf-7330-3c39-896a-40e7797c71d6 | -10.69114 | -68.6318 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a818c36-9581-300e-a7df-75a88bdef861 | -10.66053 | -68.6583 | 2024-10-17 05:29:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ae9bda-03b8-3086-9185-9b3f4b71a014 | -10.65504 | -68.7383 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6326a233-af8a-3a5b-a267-0a968e91d741 | -10.65434 | -68.74223 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2daa7dc8-e699-3f36-82c4-093bd94f2879 | -10.63601 | -68.62605 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d017ce51-a2b3-313f-bb68-cfc2eddc06d8 | -10.63583 | -68.62718 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b348c3-ca53-377c-9872-e668011546c1 | -10.63182 | -68.62534 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc9a8d6c-619c-3528-b5ab-a94e34691fcf | -10.63164 | -68.62646 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6817b93-3eaf-3323-b410-54c6c381aa80 | -10.62912 | -68.56602 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4db2efc5-4e84-3c54-a096-ef204819e16d | -10.57691 | -68.71712 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 707bf73c-382d-3371-a84d-f0d1c153f85e | -10.57622 | -68.72106 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4096786-aeb7-3f2d-a56d-5b0db560d9ad | -10.54718 | -68.56686 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30cff4ac-4e69-3f41-bd13-b1cfadc6e7fa | -10.54232 | -68.56994 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b41aac0-f714-3c57-94a0-6f816d1d95a8 | -10.54163 | -68.57381 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16bd5f27-196f-3f08-9782-9e9afb8bdfb4 | -10.54097 | -68.57339 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb9f10d-36e9-3004-acc1-37e968e41f6d | -10.53745 | -68.57306 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990f0dec-5e15-36fa-9e46-ea88831063e6 | -10.47726 | -68.49451 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed0fc25-1f8e-3112-aa1c-1da9913e76df | -10.4731 | -68.49375 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8020ab81-5262-3dfc-863e-a77460ac7d75 | -10.46284 | -68.72425 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bc0d264-7b3f-371b-aba8-048eec26975b | -10.45746 | -68.85526 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c1205e9-88d4-3d19-8759-8761ba0643d2 | -10.42084 | -68.46964 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 463b7468-2e68-35c4-a746-511b46cb96a1 | -10.39614 | -68.6124 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 334b2ae9-cfb6-367b-b953-31b2be260655 | -10.34832 | -68.83723 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0332d2-c39b-37b4-abd6-bc5ab39bdda5 | -10.29076 | -68.83908 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5b0f59f-b45e-3534-aea3-bb4903892d01 | -10.29004 | -68.84312 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db134926-420a-35f5-a17d-8962cd3b65f3 | -10.28932 | -68.84714 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f951cb26-3474-3a9a-acce-7b53346e3f11 | -10.2886 | -68.85117 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de6778df-7111-31d5-9b4a-86d2ef457f6a | -10.28788 | -68.8552 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67917e23-5172-38f8-a10c-7e6dfa6ae191 | -10.2609 | -68.8181 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ba925a-ceb0-387a-bf87-0ee062b84fb7 | -9.93861 | -68.99223 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 829ef90a-8f31-3582-9665-4f8a232cb42b | -10.75189 | -69.05345 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9baa180d-f948-3c31-8d43-574c280238b1 | -10.7374 | -69.1362 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a509525f-4a29-393c-87e2-0159af27ee88 | -10.62846 | -69.16531 | 2024-10-17 05:29:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9f6dc3c-9dcc-30fe-962c-f9bf1c14f680 | -10.20425 | -69.09296 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9db1271f-b00a-3be0-8b2e-93dd83b0394b | -10.20064 | -69.08795 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c89187-76ba-30c9-86b0-3c478a4f5d1a | -10.1999 | -69.09219 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d95e3e7-b61d-3712-b965-a06f85a52e29 | -9.49358 | -67.71442 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c8f40b0-5cfd-3065-85c8-560e32863753 | -9.49324 | -67.71481 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7bd21c3-ce03-37d0-99bb-d21ec2e071b7 | -9.7817 | -67.68328 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68f99b65-dc48-3a1c-bbe0-95d101deab85 | -9.71209 | -67.57805 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59e4b9d4-d079-3117-be18-55ab48f13d29 | -9.59643 | -67.52403 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41e764b6-8cab-316f-983c-d949f8821cbf | -9.59594 | -67.45519 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0ab51c0-b1b8-3615-9e2b-9a630ef0a01d | -9.59555 | -67.5292 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f873a9a7-163c-3a40-bb5a-21a947f7c1e5 | -10.85932 | -68.26609 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0e44579-3905-3b17-9884-0e496d8fa21e | -10.85525 | -68.26534 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd5e210b-9e37-3c4b-9ee8-e2a4b865f411 | -10.85461 | -68.26897 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32085822-7ab8-3fb0-ae68-010289f3bded | -10.81868 | -68.3534 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e09df92-1b79-35f8-b4f8-0a8748dfd80c | -10.57526 | -68.15149 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d807b11c-5ee1-39e5-b778-df7ebbc24981 | -10.57119 | -68.15078 | 2024-10-17 05:29:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ba8e1d4-05b4-3468-81da-2ee6656a8ab7 | -10.39117 | -67.96382 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bfdfd9e-9e83-31a2-a27a-32ca4912b0d8 | -10.39057 | -67.96733 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7e26a20-7c08-38d4-8d55-b3799516fd60 | -10.36948 | -67.94524 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e811841-94d7-32ce-86de-3c4f4d9ef752 | -10.36887 | -67.94875 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10c66019-07ce-3723-9b1d-1e839a6f187f | -10.36826 | -67.95226 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 340aea1c-5423-3ff9-a1d2-74293302819b | -10.36765 | -67.9558 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69486bdf-5e1e-3454-a5e6-5d58c8620269 | -10.36423 | -67.95155 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbe0a5ab-7994-3da1-98ea-cfdd93ad1c7f | -10.3599 | -68.07265 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb794a37-5fd3-3a53-8529-1c2796ad9087 | -10.35928 | -68.07625 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7389ef17-9670-385c-8125-8c2024787b69 | -10.35741 | -67.94306 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 457341f5-f022-3eca-96fe-51edbd673764 | -10.35679 | -67.94661 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d85ddfae-d849-3c85-888e-b15bf00f7f52 | -10.35584 | -68.07192 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dde6452-ce25-3a06-a4d0-b5e14b7c65a6 | -10.35556 | -67.9537 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbcb2a5-1978-36b6-b1f4-944d8fa15a04 | -10.35494 | -67.95724 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0e84c79-5e80-3d8b-99fb-b7d1a7d93a7b | -10.35462 | -67.98293 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cda6fc4-8917-3c9c-9b6a-f2af0f07a31f | -10.354 | -67.98648 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e00c04f-6056-307e-9bc4-356303ba3e65 | -10.35338 | -67.99007 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a9cc520-f6cc-3efe-9ddd-2df12ba973ca | -10.35276 | -67.94592 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fe776a4-4193-3282-b073-c03461bee80b | -10.35214 | -67.94946 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 187dde6a-d7db-36ab-869f-7d9e9a24193d | -10.35179 | -68.07121 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b888166-bf47-3205-a4bc-c0cda20019e0 | -10.35153 | -67.953 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a2ec986-3c2b-3d97-899e-819c3c06e9c2 | -10.35091 | -67.95653 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64641207-eed6-3d06-b94f-729a1961277a | -10.34996 | -67.98579 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f39c2d9-77fc-3f5d-a15f-97f38ae4bb4c | -10.34934 | -67.98936 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79cb6b67-fad9-3c22-a7d9-04944050007d | -10.34871 | -67.99295 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab85697a-9c69-37b8-b443-7201cf437a0e | -10.3475 | -67.9523 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e48391b-82f6-3291-9264-99d0ee650303 | -10.34688 | -67.95583 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b43452f-64ef-35bb-b57a-f866aef39e7d | -10.3453 | -67.98866 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ba3fb05-527a-3388-9c13-b6f571036807 | -10.34467 | -67.99224 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc9174e1-ec50-34ef-b194-6a3de22d4439 | -10.33416 | -67.95728 | 2024-10-17 05:29:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f278ae04-b6cb-3300-80ec-9599676dbd0b | -10.32617 | -68.07409 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce150305-6454-3cf8-b985-34c46e461786 | -10.32441 | -68.03651 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d93eeca-178d-3dae-8fcf-a5b64956c071 | -10.30523 | -68.02987 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72814000-ba49-3a36-96e8-6f132aa9d994 | -10.3048 | -68.02928 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05ae404-6d5b-33ca-91c5-1e7061e097b3 | -10.15788 | -67.94136 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f00dce74-6b8b-38c5-b617-86e127cb7814 | -10.13884 | -68.29662 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3450839-70bd-3aec-b1be-3a984c65cb7a | -10.1101 | -68.04785 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f219c0-71c8-3763-b13d-9549ab6f7c32 | -10.07486 | -68.06397 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e84865ff-1304-36a6-9dd6-61a1d14d1534 | -10.0714 | -68.05962 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9516898-2994-3ba2-a904-39fe972ea3b4 | -10.07078 | -68.06326 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0987d2d-2934-3f3e-8d39-d73245210af6 | -10.06938 | -67.97347 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b6224f-a4f6-3fea-a1c2-bcbc44e3196d | -10.06876 | -67.97707 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0181c86-4a8b-37bf-ae9f-a6be8a6d955a | -10.06752 | -67.98431 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a96b4973-04e1-3716-ab4d-147b3c6ce185 | -10.06471 | -67.97638 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb866b3b-5261-3e71-901a-73124aa420ce | -10.01598 | -68.38403 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b3dcc8-10f3-386a-8a68-d165e49f26a4 | -9.61318 | -68.55982 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1c7fa6-2fdd-395f-960b-313d217af2c4 | -9.61032 | -68.55119 | 2024-10-17 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
