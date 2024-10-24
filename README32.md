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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9afbba10-0fc0-3c19-adb1-624699681bc6 | -4.06516 | -48.25091 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2bc9c82-2fa1-3e05-bb5d-9ed42f3c66b2 | -4.04964 | -48.1121 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fec3deb-cea8-3100-b58c-cf6cdd8566e7 | -4.04632 | -48.11158 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b83f67f-153c-3cba-a1b8-39d696da4eb7 | -3.93211 | -48.35899 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3205d8fc-a342-36cd-8498-ead58d39a695 | -3.9293 | -48.33677 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b8a84e1-0720-3eea-ae85-bf90c265295b | -3.92875 | -48.34029 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6981279e-d3cf-3d82-8ef7-3f4b3d2db85a | -3.92652 | -48.33276 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5319334f-39ed-3e3e-9c42-0efe8b4478ea | -3.92542 | -48.33977 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4237d26-ad8a-3f73-9e79-cfaa7fe07c91 | -3.91431 | -48.36692 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 654b42ce-cfc1-3095-934a-ef8d50a1b897 | -3.91042 | -48.36992 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21595327-a32a-3276-9726-5f060cae1fb8 | -3.9082 | -48.36235 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| af2f2dde-cd07-3709-a1d9-9708087ad5c9 | -3.89652 | -48.32809 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35abc300-e9c8-37f8-946b-f40d2eea5c0e | -3.88596 | -48.33004 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86407c1e-dade-3f83-a943-cb72f9111f71 | -3.76678 | -47.72668 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3564baf6-cd2a-3ba7-9e4d-3bb2497ffb92 | -3.76624 | -47.73012 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8512708e-5d83-3026-b7de-4f630e3aec6d | -3.72839 | -47.81975 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5789447a-9a6d-366d-b54a-2c3e6366edf0 | -3.72563 | -47.81578 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9020613-1f9d-3848-b273-026fdaf1fdfc | -5.07003 | -48.28884 | 2024-10-24 04:32:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00810853-fea3-3b5f-981d-471843e53148 | -4.98725 | -48.42522 | 2024-10-24 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0254f56-97d2-3433-9a51-acaad89b22db | -4.98451 | -48.46423 | 2024-10-24 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe3a1458-ecfb-37bf-b526-37a75f4bc6d4 | -4.98118 | -48.46371 | 2024-10-24 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aee56533-79b8-36c9-8a2a-7aaa4086e133 | -4.96801 | -49.27907 | 2024-10-24 04:32:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bda46be2-8ae3-3b86-8481-6000c43cdc3a | -4.96461 | -49.27852 | 2024-10-24 04:32:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81f2f8c4-fed1-3cb0-ba4e-198237bf8351 | -4.87379 | -48.56198 | 2024-10-24 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9155f2f5-bedf-352b-b49a-cdd7efa45110 | -4.8211 | -49.14695 | 2024-10-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df012734-77eb-33c6-a78b-a027b9808ae1 | -4.82052 | -49.15059 | 2024-10-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16bbc9cc-09be-3446-b856-f4319465f86b | -4.81713 | -49.15006 | 2024-10-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d9f0a7a-7b8b-36cf-b15f-5402c8683b86 | -4.75554 | -49.09227 | 2024-10-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fab21a4-f56f-30ab-849a-334c4c1f93bd | -4.75479 | -48.43179 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d753f422-160e-3adb-9f61-bce2f5045b8c | -4.75216 | -49.09174 | 2024-10-24 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8593fad3-9ae8-3a98-818f-8a377cee40d7 | -4.7226 | -48.48423 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b6edb7c-c5cc-34be-a973-bde4fd97a4d7 | -4.33954 | -48.62259 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ada5c8b-6b11-3130-bab4-f1b3d8b02df5 | -4.25225 | -49.18929 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61977e59-bb60-3f99-bb36-2a9021a21a50 | -4.24884 | -49.18876 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9db02577-0d05-3061-96cb-8520868dc012 | -4.18174 | -48.59031 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c2310d-284d-3d81-82ae-69d8e7ba68f1 | -4.18118 | -48.59386 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f6ba237-86ad-37d0-a8ae-7707c4de1a90 | -4.17839 | -48.5898 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddea2be6-80d6-33da-a7e0-29f3e82b2d36 | -4.17783 | -48.59333 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb943eb3-70ab-358f-812c-e719e4b2dd3c | -4.17504 | -48.58929 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c391fe-a56a-31f4-ab1f-1c59badd4ec3 | -4.17392 | -48.59636 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0ac2ee8-eae8-33db-b113-aa830d6825a1 | -4.17335 | -48.59993 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57a33f17-dac7-3c4a-adb2-9f56bce5ab8c | -4.17279 | -48.6035 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db26c0c9-4bdb-3a43-928c-438729076cff | -4.11344 | -48.48524 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9465c07a-9796-3ac9-8dfd-2c88c1430f17 | -3.69553 | -49.04229 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fe0f948-66d4-3b93-b423-981c44d4caf6 | -3.69496 | -49.04596 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15d91bc5-1b35-3389-8b17-c042f9dcc3a4 | -4.87801 | -48.21166 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f8cad51-0bcc-3cd2-9584-6bd685dc1967 | -4.8747 | -48.21114 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 195e9682-f53e-325a-bd07-a4082a21679e | -4.87415 | -48.21463 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e341987-05b7-38e9-bfef-688dc61915d9 | -4.87138 | -48.21063 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a20f349-7bbe-35aa-8051-7c0725d4736e | -4.61078 | -47.87827 | 2024-10-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855713a1-2d12-3c93-93f1-19654f3b5576 | -3.98738 | -49.02033 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631cf9a1-2ea6-3a56-ada6-af8c0f3c9724 | -3.97944 | -49.02651 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b86f48-7ed2-38b1-9407-e1a737abb954 | -3.95969 | -48.88954 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1643e60-bcf3-3f96-a902-2c8d72df665f | -3.95631 | -48.88902 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5386ed51-6df9-34ba-ad6b-ab65d7918af8 | -3.93545 | -48.35951 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f4a456-5735-33e3-b965-874cf0350043 | -3.93215 | -48.33735 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a51e1264-10e3-389d-a736-e5fcb6e22bb2 | -3.92597 | -48.33626 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22db6332-4e48-332a-8521-4c488693572b | -3.91594 | -48.31319 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69f2df91-6d4e-3ad3-8450-35da9d175354 | -3.91098 | -48.3664 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e92de634-042b-3402-85bd-f43160b1fdab | -3.90652 | -48.32966 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fb228fa-0dd5-39cc-9988-f37fdc129c57 | -3.90596 | -48.33315 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4678787-46e0-335d-8bb4-39c647447f4b | -3.89707 | -48.3246 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb960b97-9a2d-3951-b0c4-b59f62754089 | -3.83565 | -48.8883 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 185621ff-c716-344b-bcde-9eb132f01ec3 | -3.83117 | -48.87273 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fcb01831-5d23-3a5c-afaa-af391e29cd18 | -3.8306 | -48.87635 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6661cb04-ca8b-3c0b-831a-f110c7d8ef39 | -3.83003 | -48.87998 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 632461c1-7876-371c-8632-63dc482b11d1 | -3.82779 | -48.87219 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34f5595e-dc3e-32bf-a378-1e20b7cf55dd | -3.82722 | -48.87582 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 040eee63-339a-3f4f-9a6a-ac193f43b35f | -3.82665 | -48.87944 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19b4479b-9a9d-3cf1-8416-00fbed22c934 | -3.82441 | -48.87166 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3b71854-7839-3fd5-b7cd-5f81b13fb856 | -3.82327 | -48.87891 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c10dac56-a85c-35e3-8655-f25904baeb9e | -3.81708 | -48.87423 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda2b67e-5eca-33af-b925-83397df83f1e | -3.80553 | -48.96917 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b48214af-5310-380f-8331-017b0f9d1a5a | -5.22831 | -47.95544 | 2024-10-24 04:32:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d6d700af-f7a9-3402-b2a0-361cfe477dbc | -5.22225 | -47.95095 | 2024-10-24 04:32:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c83c856-67c9-3715-bd9c-3f4d1ed78f10 | -4.96677 | -49.35768 | 2024-10-24 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e687594-7cf9-3720-8c20-6c557adc60d3 | -4.96601 | -49.35785 | 2024-10-24 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d253055-0506-3a8b-a2c1-ae5e3e998f1c | -3.24407 | -50.17487 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de1a9268-f8cc-38d3-8f2a-14ce3c5dc8bf | -1.29107 | -48.99311 | 2024-10-24 04:32:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebacb9c-1bc1-310a-b843-07bcde7068b8 | -3.27048 | -50.07873 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e37afb93-03ff-308b-a77a-b36cc9578213 | -3.26692 | -50.07816 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9cb7cc-ec71-3b32-82de-85924b18b7d4 | -3.26234 | -50.15251 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f0a8da-3713-39ed-be35-76b0eda12b82 | -3.25679 | -50.16425 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e68c2c6-31c2-3641-9105-126d54e73afb | -3.25613 | -50.16836 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 10d8d163-4515-38c8-96d5-95c6c653c2f5 | -3.25058 | -50.18006 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5de1b3-fcc1-3ac9-91ea-4b0aae00734c | -3.24993 | -50.18415 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d752f53-60af-30ba-a690-dee60ed37171 | -3.247 | -50.17949 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49d3dc12-9535-3bbc-87fc-911a3590f77a | -3.24634 | -50.18358 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5c7fab1-28c5-3d99-9d1e-e9843afa777d | -3.24619 | -49.75299 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b28dff4b-927f-3060-9a2a-62bbade7ee37 | -3.24568 | -50.18768 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86a74519-4083-32bc-bcc5-d7aea3dd0584 | -3.24341 | -50.17894 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cf0c12d-7556-324b-a57a-63c832f431e0 | -3.23079 | -49.11709 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 868c4308-091a-34d9-8c84-a8fd59d60ca7 | -3.22795 | -49.11284 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5bc8b00-bf9b-3346-aab4-c2acf057cd15 | -3.22747 | -50.16387 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d9f7ea0-c8c0-3ac2-8c2f-3ad53f1fe015 | -3.22736 | -49.11656 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 168c847d-e98a-34d3-8e65-884b71098037 | -3.22681 | -50.16796 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e509739-37cd-3049-80d9-d4519b47d37e | -3.22394 | -49.11602 | 2024-10-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd131902-47c3-3042-8050-da06883dd9cd | -3.22389 | -50.16332 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b388c77c-67dc-319e-a655-84824ba7973b | -3.22323 | -50.16739 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c89673f9-ac0d-351c-a59c-c92d026c44a4 | -3.22031 | -50.16276 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README33.md)
