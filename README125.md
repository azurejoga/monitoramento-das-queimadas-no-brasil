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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33713308-2125-37ee-b0fd-c0e4fb49b622 | -3.70116 | -47.60489 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aac4a2a-4369-34c9-95a2-b79743e32de0 | -3.70061 | -47.60843 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e219c2a7-868f-3ea4-b8ac-fda772a4e257 | -3.70057 | -50.17545 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 659cc756-8bf7-33c6-97db-9163f0c79e37 | -3.6989 | -47.5973 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfb9eae5-915b-35ce-9374-b3015ae75e38 | -3.69835 | -47.60083 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8dbb3da5-d96c-39d4-a24e-d25b2e575fc7 | -3.69759 | -49.84473 | 2024-10-09 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 998784f8-ff5f-3030-96cf-f8674a786148 | -3.69506 | -47.62207 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0347ebf3-b88b-3d45-9974-a6dd2c63d264 | -3.69379 | -50.17438 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c073d82f-2075-30e8-b80b-942e42c6224e | -3.69161 | -50.12221 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 47c0ed68-1b69-3edd-8149-da55302685dc | -3.69104 | -50.12581 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2120754-daae-3b35-95ef-fdf859bc2ddf | -3.6904 | -50.17383 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cf4ff70-555c-3b1f-adf6-4da1ad2d056c | -3.68823 | -50.12167 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 970f394b-c0bb-37cb-a30b-4de9ddc1771c | -3.68766 | -50.12527 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 412967c4-6bf9-3dce-9092-e2cb7db0b2a9 | -3.65615 | -54.29559 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83f58b1f-e0ae-3221-b8bc-19c89f1dc473 | -3.6469 | -52.3003 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f6b9b04-4987-366b-8587-b66a5dd97b57 | -3.63332 | -49.56658 | 2024-10-09 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c3ff24e-b87b-3aec-88d0-129cad300965 | -3.62876 | -51.17685 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65ac3e4-242e-34a5-aaf2-f0eb35c025ae | -3.62048 | -53.51499 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73743264-86f4-39fd-b4b9-e5fe7c1f4f8d | -3.61687 | -53.51691 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481e4926-91eb-3284-bca7-14e3ccd3573a | -3.61648 | -53.51435 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e12749c4-4bd8-38b9-a38d-1f1b4c5b7ceb | -3.59742 | -51.37377 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810d778d-2205-3c66-b5d3-517ff8f4a9ab | -3.59387 | -51.37321 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38da727-8b34-3b3f-8736-34164f3f61f9 | -3.5872 | -50.55906 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 304cc7c3-547f-3feb-af20-467ace71ebcd | -3.58275 | -53.26778 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ec2cefe3-7291-3cb1-86d8-ae874b6987a0 | -3.5784 | -50.3949 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c839fbd7-835c-3bfd-a3c9-2c774b920b2a | -3.56781 | -54.33444 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac2dfab-934f-31da-91ab-ca3df3c1fcf9 | -3.56717 | -54.33837 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d16ba79-8ac5-3357-81c7-c225cb3487ee | -3.56654 | -54.34233 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c3bc84f-8450-30f4-8473-7d88a9ad2d7b | -3.56648 | -50.57848 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bacda3d8-f23b-3260-9e4a-644024eb3687 | -3.56646 | -54.02538 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16f85458-c250-3e3d-a35b-8f2623343a7c | -3.5659 | -54.34629 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12e67bf8-40f8-3d8e-9992-ce0e2720213d | -3.5636 | -54.3336 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02dd2800-4733-3c0f-a327-ff26a1184ddb | -3.56297 | -54.33755 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9bba9488-ae6a-39f7-82de-4ea6b1c72fd8 | -3.56168 | -54.34552 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f3da53-ade7-3e82-a3fc-ba48ce566e76 | -3.55748 | -54.34466 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32d0dbdb-947e-35c9-aade-b97595b57674 | -3.55684 | -54.34858 | 2024-10-09 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b28be3a-3c88-3096-b474-fd50abfb00a0 | -3.54862 | -51.29301 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c526c831-f3bd-3c12-a688-36ba9bcfb657 | -3.5437 | -47.35854 | 2024-10-09 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3505c18b-4bce-3f6b-8621-7d8464832ef5 | -3.54094 | -55.48676 | 2024-10-09 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04a798ab-e851-3a80-9057-c7d20a6d9065 | -3.53962 | -54.05905 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3433ca08-8432-3441-b1ed-a2d6f1d61b81 | -3.53706 | -53.00555 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2aa0004-730d-3941-b57e-ddc2c4a4dde9 | -3.53547 | -54.05835 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd5f7f0d-9fb4-3d2e-9ee1-189f5b9f27ee | -3.50729 | -50.2711 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae18b630-a5c8-3251-9feb-68da864d98b0 | -3.50048 | -50.27002 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdadb487-2006-3b38-9453-0c22ac0b54f5 | -3.4999 | -50.27366 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f2a8ec9-c497-382c-a69c-dfbeb481e101 | -3.49883 | -48.89721 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 827160d7-3770-36f2-865a-384588dd1177 | -3.49547 | -51.17693 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d226898-ea4a-3bbd-8728-6bd6e2f42f32 | -3.49327 | -48.88926 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 037b88e5-bb37-3f7e-9d80-870e136ea4ed | -3.49273 | -48.89272 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dd37422-fd74-3381-8a06-5421a5cd010a | -3.48941 | -48.8922 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 939c2b80-5df0-37ef-90b1-a5fc1c8ca82b | -3.48608 | -48.89168 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0bc66e3-89f2-3618-a7b4-9237543155f0 | -3.48554 | -48.89514 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 449e9de7-0cd3-35c3-9483-eb0d663cbc3c | -3.48521 | -50.80805 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8879596b-d712-3512-bf96-634721857a23 | -3.48461 | -50.81184 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 073ca191-6af7-368b-bb0c-4267d3989206 | -3.48309 | -48.89491 | 2024-10-09 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c05ead7-f547-3bfd-99a1-50e853ba6d58 | -3.48174 | -50.80751 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd484533-7893-3d6e-aa5d-b2b757bc9452 | -3.48114 | -50.8113 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36bda41f-edb0-3fe0-821b-1af653a8b6e5 | -3.4622 | -47.66158 | 2024-10-09 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d113af-6e62-3854-8436-9f4cb87f9e11 | -3.46116 | -47.65804 | 2024-10-09 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cff4124b-27f0-353b-8356-b42538f6a1fe | -3.4606 | -47.66158 | 2024-10-09 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7a8fded-e37f-3c8d-b633-125e6f081ec7 | -3.43439 | -51.53494 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45eb9c1c-5c04-3259-badd-280aef6000af | -3.43223 | -50.32721 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4340289-fef1-342d-9ba5-7d60889c4b6c | -3.4294 | -50.32298 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cf8686d-199e-3ffa-8995-bed8810e3d78 | -3.42061 | -52.07995 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 462a843f-1088-3689-9a2b-4f8881af0267 | -3.41373 | -52.83173 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 339f6cb1-c374-381a-8f2e-7b4ef9cc28af | -3.41118 | -50.32759 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbfe17cf-4171-38dd-82c1-ec144da7e28c | -3.41059 | -50.33128 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63613e44-bb61-3f09-8229-c8bbf8e21d7b | -3.40718 | -50.33073 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67e1922b-362b-32be-81e0-71d42a9db7c0 | -3.40435 | -50.32652 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fa3f47-f808-312f-be56-511551d4483d | -3.40376 | -50.33019 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 89e8c4af-626f-30d4-a9a1-263a127479d3 | -3.33884 | -50.1227 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67d8c731-9d54-3f66-927d-8d4d3d5238f7 | -3.33827 | -50.12632 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b2a17dcc-dcf1-3e60-b74a-2464c7aea5f6 | -3.33545 | -50.12217 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd595894-84b2-32a1-baa0-aede5f5df1c2 | -3.33487 | -50.12578 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 320c9f30-3ab8-3f74-a55c-54b36c6e6648 | -3.33337 | -53.39569 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01016d80-83c6-3ac3-bcde-7047e8e8d0ab | -3.33205 | -50.12163 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03cae9a1-87b7-34cb-bc75-ffdb964cd413 | -3.32937 | -53.39508 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5668dc51-b6d5-3899-b841-c3c45ab6e10e | -3.32811 | -49.14688 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3ada198-1ccd-36c9-81cb-92a6c2ff1948 | -3.32756 | -49.15035 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 996a6d1e-9688-3264-b3b6-d3d3ff6c6b1c | -3.32749 | -53.21519 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c9518b8-6865-3bf1-97b2-e86b9d2665e6 | -3.32701 | -49.15382 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3088c93-e268-3519-9203-f027b350a076 | -3.32669 | -53.22024 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29ea3dfb-fc12-3aef-ae30-fd7f67bf777a | -3.32622 | -53.38932 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02107c7-922a-3ba7-bf37-b320ea800b2e | -3.32619 | -53.21704 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80606046-54ef-3220-980d-d64de2629491 | -3.32538 | -53.39447 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8e82f46-e755-3f2c-88e6-db4d111ddd9d | -3.30872 | -50.46667 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6516ba32-1c8b-33ab-b01b-a2aa2265c739 | -3.30748 | -49.10453 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c1360c-11d9-3f8b-9a62-827667c0fc7f | -3.3047 | -50.46983 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fc4ca53-f873-3521-9958-891959125894 | -3.29425 | -49.14514 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0481dcc-ee64-3af3-9ef3-c8f8140c2956 | -3.2814 | -49.0969 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f46ccfaa-1405-3b3d-9352-dfd4ee0f483c | -3.27807 | -49.09638 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49cba668-1b06-3f88-bcd8-3c83f5459215 | -3.27419 | -49.09933 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2d6610f-80e7-3e28-acd6-bc80c29557b2 | -3.27141 | -49.09534 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c93584c6-a40f-3f8f-9eee-a104e9b71479 | -3.27086 | -49.09881 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f87079b-2017-3135-9af7-0fe46fcc2570 | -3.26202 | -51.23816 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f8962c8-4bc1-3f78-9317-2e8c1b318050 | -3.26138 | -51.24213 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f973ca94-d9d0-3429-a3f5-ed1df0e6dad5 | -3.26087 | -49.09725 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3530fbcb-a7d4-382c-abb6-b229e607d4f8 | -3.26047 | -50.13313 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1be584b6-3990-3160-8f00-32da44b1baf2 | -3.26032 | -49.10072 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f30332-d6ea-3dd0-9939-aabdf7854f78 | -3.25978 | -49.10419 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README126.md)
