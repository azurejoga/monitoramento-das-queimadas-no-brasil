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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f50abd2-3991-3dfb-8b4e-a9c9c984fc3f | -13.05711 | -51.34544 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c765e90-76aa-3fc4-be12-59dcbdb6f59c | -13.05656 | -51.34906 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a04768b-f5f9-3bf5-908b-30c86eb8c105 | -13.05591 | -51.30814 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b994733d-9380-32e3-942d-9e689562e249 | -13.05556 | -51.4007 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 72dc26fd-bc63-3a42-b7ea-9d1068c29ffa | -13.05541 | -51.33403 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ee577fa-fed9-33ab-b964-98f5dc1d6211 | -13.05536 | -51.31178 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14b14589-ca95-3c63-819b-42bfc527084a | -13.05501 | -51.40432 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d0c875c9-dfa3-35e7-a17e-7925aa4cf211 | -13.05486 | -51.33766 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40b220b0-27c9-3741-b179-a8d921e8af37 | -13.05481 | -51.3154 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ece6d15-af0a-333d-a1f3-588ac8068241 | -13.05431 | -51.34128 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa198c81-75b5-3237-83d4-09949c2903ac | -13.05426 | -51.31902 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b3b067e-d29e-3929-8bbb-71e96abc893e | -13.05371 | -51.32264 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 039fa03f-0833-399a-b960-22c951abb4d5 | -13.05331 | -51.39295 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b5df455-bb67-3f35-9cc6-99d9a16bc6dc | -13.05316 | -51.32626 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e3bb6f2-fd02-3d07-ae79-baba80bb165a | -13.05277 | -51.39656 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00a22449-a909-3b5e-a157-437111f966fb | -13.05261 | -51.32989 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1e63041-2386-353d-9589-80c1b6d69da0 | -13.05206 | -51.33351 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34499f0d-fb65-314d-b7b5-99f9c9648ad1 | -13.05167 | -51.40379 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e20b9e16-6e4f-3e69-9910-ac722035b161 | -13.05112 | -51.40739 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d53131d4-b83b-329d-8753-4992c494c797 | -13.04778 | -51.40686 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f6469b9-7efe-3988-96a1-a997d8a78a92 | -13.03983 | -51.34639 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9993c2b-64d4-3f16-88b5-4c71914e07e4 | -13.03868 | -51.33139 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b4ed878-645f-3b1b-a10c-b96945d718c5 | -13.03704 | -51.34225 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4005b479-e8d2-3fb6-9665-2cc2a5d23487 | -13.02443 | -51.27391 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a47840e6-9427-341d-8dd8-d7ead55126a5 | -12.99999 | -51.36641 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3717ea83-bc62-35fd-a74d-fd9aaf3881b6 | -12.93216 | -51.40735 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df35860e-0d84-31c2-b18a-00a44dab02ac | -12.92882 | -51.40682 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 416b87f8-9177-3cca-8b3d-c2bcc749b692 | -12.90262 | -51.29159 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8be6c0e-a1ef-38bc-84a5-c9749e01317a | -12.90207 | -51.29521 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58e4fb95-3d78-3b49-8c30-eb9a9c6439e5 | -12.89817 | -51.2983 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba761280-57ae-3264-96eb-ac7a10b69b8e | -12.89764 | -51.32414 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1a3fdb5-f3a1-3f57-af53-e00f50e86dc4 | -12.89429 | -51.32361 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88949993-6bbc-3fae-9331-49eb55f21535 | -12.89261 | -51.31224 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262909db-d925-3a67-89d5-2f9150d58a56 | -12.89095 | -51.32307 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb1e901d-0499-38f2-bdad-4109e5ffae8f | -12.8904 | -51.32669 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 187ba0d1-b1dd-303f-8e4b-435ea5eb29d5 | -12.88706 | -51.32616 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 222f6a42-eafe-364d-8a61-7d65808e7960 | -13.01188 | -51.50809 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 83e54236-be06-3cc0-8953-b9aa6dde1b23 | -13.00909 | -51.50397 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d4263f27-a2b0-3079-8433-24d891cff6df | -13.00854 | -51.50756 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ba046003-d4aa-3124-a967-4784d992598c | -13.00576 | -51.50343 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ad20a53a-1ad6-3d76-a6d4-340fa5f5fad6 | -12.98405 | -51.5371 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30964c4a-feea-3dce-8427-68466e1752c0 | -12.97182 | -51.52781 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9e565cc5-ad97-3bd0-aa33-5ebea8f45a3d | -12.96904 | -51.52369 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 002843e0-1249-36ae-a8de-0a1111fd0919 | -12.96849 | -51.52728 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 12a01218-0533-3ba3-8bed-9135d930c2e0 | -12.96794 | -51.53087 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f17e015f-e263-3670-8427-426944aeaf53 | -12.96739 | -51.53445 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5cfdb1d0-e95d-32c7-8df0-15352890b9bb | -12.96626 | -51.51957 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3d02f34e-13c5-3396-8caf-f90e5be0f914 | -12.96571 | -51.52316 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 08df7ea6-1447-338e-9575-1a3884652891 | -12.96516 | -51.52674 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 65702834-bfb6-33cb-bfb2-fd1ae8ac3075 | -12.96461 | -51.53033 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c52e036d-4be2-36b4-9575-5f81c9aa2312 | -12.96458 | -51.50827 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1ba9320-dd29-361d-95a6-815635ce5179 | -12.96406 | -51.53392 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 879f2297-cf46-3460-b2d9-e60fb7b087a6 | -12.96403 | -51.51186 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88cc3098-d022-34c5-a0bf-05b5ee05c076 | -12.964 | -51.4898 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20170544-d494-36d3-9ebc-baa65ea20ad7 | -12.96351 | -51.53751 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae9e470b-471c-3d37-8c89-458e469ce4a4 | -12.96348 | -51.51545 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d6064a-c1b2-3a6d-8bc1-bf3d4c9c0fe4 | -12.96238 | -51.52263 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 20ae6de1-393d-380e-8045-3d869ec3edb1 | -12.96183 | -51.52621 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 131222e4-a6ee-3520-a142-298d28a43638 | -12.96128 | -51.5298 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0a2a7bfc-80e0-33bc-8b25-bebbc431daf4 | -12.96073 | -51.53339 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aef83fd-8418-38fd-b493-11ee70425e37 | -12.96012 | -51.49286 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a76caea-aca9-3e41-ba9d-1d016ad5187a | -12.95905 | -51.5221 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7decbc02-b1ab-3ce0-aa20-65cdadeebc78 | -12.9585 | -51.52568 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 18863bee-adb4-38d2-81fc-e091c9c0a599 | -12.9574 | -51.53286 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bde51464-e12f-3738-b6e6-72ac01fbc86e | -12.95678 | -51.49233 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 017836ed-a4df-307e-97bc-c027ead4f446 | -12.95627 | -51.51798 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a65a63e1-d741-3169-8eae-2095ed44cdac | -12.95572 | -51.52157 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 83c4810e-649d-3d4a-befa-4e492a9a88d6 | -12.95294 | -51.51745 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 84b7f827-6d14-39cc-a94d-9c4d082f5e7f | -12.95239 | -51.52104 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c4b5d20a-e2b1-3580-879d-3de48ab24c6b | -12.94902 | -51.49845 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 28c1ccc2-2755-388d-b3f5-612e55dd144e | -12.94847 | -51.50203 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c252cf9a-00f3-31b6-88ff-5eb8832e123f | -12.94569 | -51.49792 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ca4664a7-f638-30c8-b951-d63f102090b2 | -12.94514 | -51.5015 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46c826eb-ed7a-3df2-a416-c406ef3d247e | -12.73354 | -51.94863 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cb07b59-b583-34d6-93e8-5bb639508017 | -12.73187 | -51.93749 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cdf36a0-8fd6-3f05-b427-291d726988c7 | -12.73133 | -51.94103 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68f2e679-7846-35e8-b9d9-f3fc9e6e8f0c | -12.72911 | -51.93342 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c62cdfd4-1353-32c5-81ca-34d031bd9c63 | -12.72635 | -51.92935 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9005372f-2248-3694-8f23-d97edd29f982 | -12.72368 | -51.99047 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ddb1be0-2e5b-37b2-b55f-cc03bb2f5020 | -12.72358 | -51.92528 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d5d35c9-2b93-341e-950d-bfc28222644b | -12.72147 | -51.98287 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a616a4a-99b8-31c9-a3b6-faa13a62f008 | -12.72136 | -51.91767 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54b6b354-5e52-3c46-8c46-697b22d6539b | -12.72092 | -51.9864 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23318096-798f-3d1e-b1f3-f36ca38e8a8f | -12.72082 | -51.92121 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a30ebee-9c0b-3f9c-bfaa-454a9555c00e | -12.71437 | -52.02873 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63e95b79-763d-338b-871d-0a6c0bd2f1f1 | -12.71382 | -52.03225 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f9921c-a037-3d8f-b03b-920e6411dea9 | -15.67628 | -52.5095 | 2024-10-02 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 85aa66c5-60fa-3a58-9c79-767addee8d68 | -12.87541 | -54.01159 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 116bf64b-5d56-3821-ba1d-2bd336dd3043 | -12.87481 | -54.01525 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a370dbfd-f926-33f6-b64b-84b52879de68 | -12.87422 | -54.01891 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 409cb256-7dfc-30ed-a461-ac8584345034 | -12.87362 | -54.02258 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f24c453-ed49-36e9-87ae-5d75a917c455 | -12.86965 | -54.02569 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44a93046-8ebe-33d9-8e74-6f5ac2fbcaf0 | -12.86568 | -54.0288 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d586f1e-c564-3016-8c3b-643a5bb02d89 | -12.75914 | -54.01419 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c92257eb-6df1-3f6f-bd23-b4fdd954d67f | -12.75876 | -53.99527 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2228b57-285b-3eaf-ad8a-6d38b7149c8e | -12.75816 | -53.99894 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 726051c1-f6ff-3abf-ae4e-da4153f574a2 | -12.75756 | -54.00261 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4716d1a7-9e62-325b-8a76-23d5a18e9f4d | -12.75697 | -54.00628 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 496238cd-3bf2-357d-a8c3-a02da19d31e9 | -12.75637 | -54.00995 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f08e398-5abe-341a-8c61-f23cf9692461 | -12.75457 | -54.02098 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README101.md)
