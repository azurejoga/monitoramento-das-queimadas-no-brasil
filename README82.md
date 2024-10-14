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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48b0148f-3308-3a66-9c76-47b21734b27c | -3.29151 | -49.09689 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48fc2c5e-40b6-3616-8146-c4713371418b | -3.29096 | -49.10043 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79191deb-4f0f-3101-9c18-402b00086479 | -3.2876 | -49.09992 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1dfcc5b-e7ea-3e7c-8386-c0a1a3606e1d | -3.2859 | -49.08877 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7fc1503-f495-3560-a8ab-bc3a86ab698f | -3.28254 | -49.08825 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce9df68a-60ae-3749-848e-5ee73b69620b | -3.28199 | -49.0918 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da38277d-f017-31ea-ab4e-2f1a09e81d27 | -2.63933 | -49.52296 | 2024-10-14 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cb6786b3-0e9d-3f49-a455-3649a148321d | -2.63879 | -49.52642 | 2024-10-14 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ccad33eb-46b9-35d8-8099-d2d34f63b479 | -2.61514 | -49.7425 | 2024-10-14 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccd6b568-1d31-3aec-ab85-703855fa4ce6 | -2.57578 | -49.75702 | 2024-10-14 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27c0d44c-22db-387b-8cf9-9a115b91eaee | -2.51482 | -49.90659 | 2024-10-14 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c509e026-9fed-3060-99ca-e76f9f983818 | -2.42576 | -50.27779 | 2024-10-14 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a843b257-15d0-3d0b-981f-2381d1d96ca8 | -2.40533 | -50.29937 | 2024-10-14 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af088ade-b92e-356a-bdf4-9408b7581aed | -2.40397 | -49.7516 | 2024-10-14 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f06acd7-9656-3152-ba21-cd02a76288ba | -2.40342 | -49.75505 | 2024-10-14 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1225ba30-c47c-33c9-aa1a-fd2aae10d063 | -2.384 | -50.41289 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 355c6899-419e-3065-af4b-752ac81f8443 | -2.38008 | -50.39456 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6dc689e8-9fdb-3d2c-8df1-979845fe2172 | -2.37772 | -50.39426 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54da5bd3-f15c-324b-bcab-847b0ba1ec12 | -3.32129 | -50.46037 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 914afb78-4ded-374b-8e2e-223995946aa8 | -3.32075 | -50.46382 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 332d710e-1080-388d-9540-f5724b46ee1d | -3.31797 | -50.45985 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fd27941-ea38-3a31-b251-7d3ab53d7464 | -3.31743 | -50.46331 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4adf85b0-d848-379c-8f91-030b0a746dd0 | -3.3141 | -50.46279 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3e3271d-d920-3731-b4de-7a6481e14a2e | -3.31356 | -50.46624 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c04cd2c-e35e-3e6e-8778-5633b96eb58b | -3.18978 | -50.45766 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52fc4aef-cd8c-3261-8245-594ba725908a | -3.18646 | -50.45714 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66895c5d-eb71-33cb-b766-aa81aeef5b11 | -3.18591 | -50.4606 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93bbcca-f753-3c14-9004-77baf7636a0b | -3.18259 | -50.46008 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 862d053e-0333-371a-9b98-1357c485bfd5 | -3.18204 | -50.46354 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbf989aa-2236-35a1-b506-fd8af1eb2a45 | -3.17927 | -50.45956 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 743f1e7d-8cfe-33c3-a9a6-0b92493279b3 | -3.17872 | -50.46302 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a4b107-3d34-3e41-aa73-501152aadc32 | -3.17594 | -50.45905 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de0769bc-adba-3197-b005-a1776c68db8a | -3.1754 | -50.4625 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 659bd186-7a64-3336-bdc4-4d61ce07b25d | -3.17485 | -50.46596 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbff6260-179e-3688-8214-821d5532b01c | -3.17431 | -50.46941 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e24a73f-d4c0-3af0-ba3c-f46d970b9b22 | -3.17376 | -50.47287 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75b9d16c-e4ee-326f-8562-023f875d7026 | -3.17208 | -50.46198 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43480221-07ac-3053-8481-411cd99ee31d | -3.17153 | -50.46544 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20d7a6ec-de0f-3054-b948-49dc541fd4ec | -3.17098 | -50.46889 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d25297f2-8847-374f-9219-aac6549b2add | -3.17044 | -50.47235 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea88d2f8-eda6-35f1-8376-269e405579fe | -3.16989 | -50.4758 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5adfa9ac-b6c6-3625-8a24-fc9c5466cc44 | -3.16935 | -50.47926 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d489342b-ad75-3190-a36f-75c5b8cc0011 | -3.16875 | -50.46146 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcdb8bfb-b75c-3c2c-a34e-0eb0f57f2332 | -3.16821 | -50.46492 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1bef38c1-3aab-3aa7-b8af-7299253b80a1 | -3.16766 | -50.46837 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9624e34-aad8-3ed4-9c95-0f85e93761ac | -3.16712 | -50.47183 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd1d6d8c-080f-3be8-b7d6-ae3dd9e88f4b | -3.16657 | -50.47529 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa9382e9-b4b6-3184-b486-559b19d1e1cd | -3.16603 | -50.47874 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66ffd70f-c251-3c5d-bd6e-076c7c6fe8f8 | -3.16488 | -50.4644 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 975841e6-d8a1-398a-b3ba-07dce13f5976 | -3.16434 | -50.46786 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5edabb0-3cb2-3640-978c-a24af72e986f | -3.16205 | -50.43918 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c93cbf42-b219-3af3-ba45-fa4460d58bab | -3.15486 | -50.44159 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b1a1763-0b75-34ab-ac46-37bff27f404b | -3.15154 | -50.44107 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dddcc43-e768-32df-bc73-bb16e54ee158 | -3.151 | -50.44453 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aeba621f-e337-3e35-a549-0ae075921251 | -3.37698 | -50.3418 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 029e51f0-de7c-308c-b523-d1edbf0ecad6 | -3.37366 | -50.34128 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a6417f8a-e295-3235-983c-f00d5b23efac | -3.36865 | -50.32989 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 309d98e2-2898-375f-9c62-b1ef24646124 | -3.3681 | -50.33334 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 528fa98a-4549-3628-9992-876eec5dae1a | -3.36587 | -50.32592 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e52221c-239b-33c8-82fa-cdd2c92cd006 | -3.36533 | -50.32937 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f3d513d-510a-3685-bd90-c57f673c30b3 | -3.36478 | -50.33282 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61a65351-ee86-325c-a2ee-b21bbcc3e21c | -3.36175 | -49.92207 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d269fe5b-a64a-3b0b-8c25-775abe45b252 | -3.3612 | -49.92553 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3db702-dc67-3892-9777-678be4087fb6 | -3.33802 | -50.31087 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1668c019-f177-3a4b-ab10-d1c7808b165a | -3.33748 | -50.31433 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1593b4c5-8360-31b6-b855-32573a1e2f63 | -3.3347 | -50.31036 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08921ecb-641f-3bc4-b3a7-2245ab9fcb76 | -3.33416 | -50.3138 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513d1def-4207-3834-ad58-a1e0e439ef7a | -3.33362 | -50.31726 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7b2e2af-4fd3-32d2-adac-b6a080cbdd28 | -3.33084 | -50.31329 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a879d94-cf55-3acc-9e92-7e305ce8f2b2 | -3.3303 | -50.31674 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bafc7c-c09f-3912-94b4-29bb610c3eab | -3.32752 | -50.31277 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d329c49d-b6dd-3d97-b931-e643030e6ae5 | -3.32697 | -50.31622 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3211a302-441f-3db0-a398-94fb9bec4f83 | -3.32643 | -50.31968 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da33571-0d44-3d38-bd03-4aed8a40fbda | -3.32365 | -50.3157 | 2024-10-14 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bd2f3ed-5a86-3852-8d6a-cd485daa33b0 | -3.32249 | -49.93366 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11557321-4633-3fe9-b6fe-354d9df99530 | -3.21014 | -49.52936 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7572ccaf-db55-3abc-bccf-d45c59cba7f7 | -3.11224 | -49.46458 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb63296d-30c7-3b13-98b2-68089859a6bd | -3.10647 | -49.39225 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 919a6a02-71bf-3aa3-bfd2-0b4d3b1cefcc | -3.07631 | -49.51961 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbd0afc7-495f-3efb-a920-c5da22fe3a92 | -3.07244 | -49.52257 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b44ffc2-14a6-300e-ab1a-dedd285e1ee7 | -3.06483 | -49.57122 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54b50c9a-3983-30a0-b65c-3031ad301594 | -3.05905 | -49.37364 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 687a51b8-8bbd-3862-a5a7-72cd81b03b0c | -3.0585 | -49.37713 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c9e38c9-0798-3633-8d8d-7bac3f1ccf18 | -3.05626 | -49.36963 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7c7461b-8332-3a51-a5d8-da6178844f6f | -3.05571 | -49.37312 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b1073c9-cc4f-3216-b983-c81c5312eeae | -3.05517 | -49.37661 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4798a901-11f7-3900-baac-53c855b7498b | -3.03279 | -49.54076 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f359ddb4-21dd-3fcc-8aca-1b3e82bf006d | -3.03224 | -49.54423 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31c4ac98-3449-33c0-b1f0-1ab4655c36de | -2.99461 | -50.30003 | 2024-10-14 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355608da-6349-3187-9ba7-2d83847058f4 | -2.99057 | -49.52709 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e615a0c3-b058-3fb3-907e-cb7a19a76cb8 | -2.98724 | -49.52657 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c815fdcd-37d6-3ab8-a01c-5ea83f2b5e33 | -2.96753 | -49.35608 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3df2a3fd-3c96-3abc-a866-3f8120ec49d4 | -2.96474 | -49.35207 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ebf1a7c-10bf-38c2-b701-11bc48d96aec | -2.80591 | -49.52004 | 2024-10-14 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1631fc-1c3b-361c-90be-c7d7bff6852b | -2.78731 | -49.42105 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d25f0e41-edb6-3f13-a280-e44cb15266e6 | -2.78676 | -49.42453 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 262c4dbc-d322-3e5d-99c0-71507133a682 | -2.78343 | -49.42402 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0024f0a-2884-3dbf-8971-a77b19e74faf | -2.78064 | -49.42002 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f47004b-0600-3ce0-a26b-9a2b4c8dc222 | -2.7801 | -49.4235 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22235393-297c-36d1-b28a-349da805ed06 | -2.77731 | -49.4195 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README83.md)
