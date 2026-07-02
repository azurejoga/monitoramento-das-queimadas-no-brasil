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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bb79c2f-2e9f-3827-99ff-0d7d46f157db | -11.4149 | -56.0525 | 2026-07-02 02:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4e93d5c1-09d5-3f7e-88bf-d83d92141fca | -10.9401 | -43.0355 | 2026-07-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 76583eaf-77e7-304c-8de0-d3d8f0b918b1 | -21.7827 | -56.2762 | 2026-07-02 02:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b3720bc8-3e24-31b4-94e8-2634ab61df65 | -3.5043 | -48.039 | 2026-07-02 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| aa8283af-cd89-3368-b84f-270009b85626 | -11.8007 | -57.0032 | 2026-07-02 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e5eb3429-78f5-3f93-afaf-88d0b42e3cfb | -12.5135 | -48.2802 | 2026-07-02 02:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2aad6b5b-e626-310f-b861-83a9bf954fc5 | -10.9397 | -43.0593 | 2026-07-02 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| dd128972-98b8-358f-bceb-57fb35f20d91 | -21.7823 | -56.2976 | 2026-07-02 02:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 6092339d-a918-39c3-9636-d6fcb490a9cc | -11.4147 | -56.0726 | 2026-07-02 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 929e8a0f-814c-3ed6-a135-4108339eebed | -3.5043 | -48.039 | 2026-07-02 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4b1c6916-fe33-3bd2-af78-964adb9c6f91 | -21.7823 | -56.2976 | 2026-07-02 02:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8091c1c2-862a-3a45-8454-b6b9970b95d8 | -11.4149 | -56.0525 | 2026-07-02 02:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bfc1437a-9e0b-3257-9f43-0a7a2045d646 | -10.9401 | -43.0355 | 2026-07-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ab4207c5-6e62-3d8c-b258-8e4a0a86f531 | -11.8007 | -57.0032 | 2026-07-02 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f50751bf-2696-3e91-b607-236857b5d853 | -12.5135 | -48.2802 | 2026-07-02 02:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f88571bd-cfc7-3a30-9b44-333aed49bb06 | -21.7827 | -56.2762 | 2026-07-02 02:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 70470a56-517e-3fe0-b441-26cd72989f64 | -10.9588 | -43.0565 | 2026-07-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| bcebb1f5-013d-396a-b6ce-ea29f6a788d3 | -10.9397 | -43.0593 | 2026-07-02 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b34a1887-cbd8-3f40-82ae-90a22713d52d | -10.9401 | -43.0355 | 2026-07-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 237f3869-3e71-3dab-98ba-5cf8bd37aa60 | -21.7827 | -56.2762 | 2026-07-02 02:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5c78b236-cef6-37b0-bc03-f6c3b0f15c15 | -11.4147 | -56.0726 | 2026-07-02 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ff64cbc4-1e5b-31dc-98f8-bea7854bb9a2 | -11.8007 | -57.0032 | 2026-07-02 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c78c1da9-332a-365d-997e-092c9bda3048 | -11.4149 | -56.0525 | 2026-07-02 02:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| a7ca583f-7adc-3f0a-be58-d54da2198f7d | -10.9397 | -43.0593 | 2026-07-02 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 01d8b698-e034-34c2-b815-2faa6b5bee2f | -3.5043 | -48.039 | 2026-07-02 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a7d3a534-2b95-38de-9ace-b8529c625743 | -21.7823 | -56.2976 | 2026-07-02 02:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 86967a31-cfd8-3c70-adfb-64ce7c24f109 | -12.5135 | -48.2802 | 2026-07-02 02:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 6e892127-a89b-3d98-9343-98bf4c064291 | -21.7827 | -56.2762 | 2026-07-02 02:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 77.9 |
| bb1e1131-563f-3e8e-bff9-b0ff75473968 | -21.7823 | -56.2976 | 2026-07-02 02:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 84f12640-ef67-3a8a-9cc0-dfaccc6169d1 | -11.4147 | -56.0726 | 2026-07-02 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b93f0242-79b6-3f32-9d31-31b37f22dd46 | -10.9588 | -43.0565 | 2026-07-02 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ae557a17-afd0-3e9a-af89-b420b72b6b49 | -11.4149 | -56.0525 | 2026-07-02 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0f71b1f7-13fc-3306-9b87-e31608ab5067 | -11.4338 | -56.0509 | 2026-07-02 02:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cde6e2be-7a4a-33ab-81bb-8113e45dab24 | -21.7617 | -56.301 | 2026-07-02 02:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 7a425e65-9260-3c7c-b295-0860f133204d | -11.8007 | -57.0032 | 2026-07-02 02:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d493d33f-f340-3be8-b292-ef01b000ceab | -21.7823 | -56.2976 | 2026-07-02 02:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 85.9 |
| fa86706d-745b-337c-975b-7a3370be1080 | -10.9397 | -43.0593 | 2026-07-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4543625e-0d21-326c-9ac1-e7c47c4079c7 | -11.4147 | -56.0726 | 2026-07-02 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b910ef34-14f5-39dc-94a7-c4c4e0034bfa | -3.5043 | -48.039 | 2026-07-02 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0f2ddb85-315d-3406-8ca6-d7c211515012 | -11.4149 | -56.0525 | 2026-07-02 02:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f4c41ac1-2ac8-3e6f-b575-6b25381d0b4b | -21.7827 | -56.2762 | 2026-07-02 02:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 43df3f21-9a28-3b9e-b3c5-e57ac32281a7 | -11.8007 | -57.0032 | 2026-07-02 02:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 83caa092-3916-3e6b-8044-03426c29cdff | -10.9401 | -43.0355 | 2026-07-02 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 05026762-94d3-34b2-8526-837e82e8b9c3 | -12.5135 | -48.2802 | 2026-07-02 02:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 17ca889d-c174-3db1-a052-9cd59ecdc0ff | -11.4149 | -56.0525 | 2026-07-02 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 961f23a6-0c81-3a0f-b719-be017eb51a34 | -21.7827 | -56.2762 | 2026-07-02 02:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8d2df4e4-074e-3289-ae46-902b28bf1c3d | -3.5228 | -48.0383 | 2026-07-02 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0deb1d9b-addb-35bc-8382-cdd7a11d387d | -21.7823 | -56.2976 | 2026-07-02 02:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e158053a-553b-3803-8f43-ca9e57d634a2 | -10.9401 | -43.0355 | 2026-07-02 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2d8026bb-8a1f-3806-afa5-d6dad9917093 | -11.8007 | -57.0032 | 2026-07-02 02:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e05634aa-9bd0-3db5-ae6b-d5aa10569d91 | -11.4147 | -56.0726 | 2026-07-02 02:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3603ed78-935c-3547-af8a-7dd4de12a924 | -11.8007 | -57.0032 | 2026-07-02 03:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e59a7656-3811-35b4-8038-c5571a1e784e | -10.9401 | -43.0355 | 2026-07-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 718f727d-c477-3655-a130-92ba37878cb1 | -21.7823 | -56.2976 | 2026-07-02 03:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 77efcfe6-17b9-3649-bb5a-5f6e9fc5e6c1 | -11.4147 | -56.0726 | 2026-07-02 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b97830a1-1918-33de-babf-a0a5d7d440b6 | -21.7827 | -56.2762 | 2026-07-02 03:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7f1271e5-cde7-3f75-9911-9ecd7cd236b8 | -10.9397 | -43.0593 | 2026-07-02 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a29a7aed-4dfd-352b-ab00-132907216818 | -11.4149 | -56.0525 | 2026-07-02 03:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 270fb758-9aa1-3da3-a65c-fdda30ad0acf | -21.7823 | -56.2976 | 2026-07-02 03:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9b7a9dc9-aabe-357c-a77f-774109793a2f | -12.8746 | -44.3357 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 431.5 |
| 8109b826-8215-3b9a-8b91-61c50059e3f0 | -10.9401 | -43.0355 | 2026-07-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 52dcaa07-eb47-3364-baf5-2b51b2a24d8e | -11.4149 | -56.0525 | 2026-07-02 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2ec06e99-1f0b-31c0-a209-4a3c679eb680 | -21.7827 | -56.2762 | 2026-07-02 03:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3ec3330c-cd97-3aa2-9cc1-48b4f5e973fd | -11.4147 | -56.0726 | 2026-07-02 03:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 93e452f7-73cb-38a0-9f13-c7d937772772 | -12.8548 | -44.3625 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 281.9 |
| b62ba93e-4d55-3e94-917d-8b26cee6e38c | -12.8557 | -44.3154 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f812c990-816f-398e-9ab6-0e552d774538 | -10.9397 | -43.0593 | 2026-07-02 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a9b44fbc-510e-384d-9af0-2864f44bcefe | -12.8359 | -44.3422 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 4039148a-fbde-3eba-b8bb-9c52b2af58e8 | -12.8552 | -44.3389 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 503.7 |
| aff65abb-6774-3783-b5f5-0bbee52287e9 | -12.8741 | -44.3593 | 2026-07-02 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 296.9 |
| 1a16680f-fc11-31dc-977f-9974a714ebac | -11.8007 | -57.0032 | 2026-07-02 03:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 748f7d85-bbc9-31cf-964d-5f51cde784a1 | -11.4147 | -56.0726 | 2026-07-02 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 96733377-1821-3ac9-8871-cf855e6662b0 | -10.9401 | -43.0355 | 2026-07-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b1c88831-696e-35cd-b683-a906ef6c262a | -12.8741 | -44.3593 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 268.3 |
| f07cfb0f-dbe1-36fe-9768-1943e3cde215 | -12.8548 | -44.3625 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 254.8 |
| aec86e86-d05f-3860-89e0-3183ad3ab0d7 | -21.7827 | -56.2762 | 2026-07-02 03:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 485a73ff-aacb-35a3-a203-f688d193a165 | -21.7823 | -56.2976 | 2026-07-02 03:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c7790b09-444f-3c00-856a-6a96db181a32 | -12.8359 | -44.3422 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 645cfd7a-a73e-3015-9881-c3711297fb22 | -12.8746 | -44.3357 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 429.9 |
| ec6998e7-d01a-3cc5-9d26-aeeaa8d03d32 | -11.4149 | -56.0525 | 2026-07-02 03:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3411e52b-7a8f-39c6-aff0-18e478836ffc | -12.8557 | -44.3154 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a3620ec0-799b-3f1a-bf13-7463bc5616ba | -12.8552 | -44.3389 | 2026-07-02 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 499.1 |
| 2fec7b2f-efbe-3a53-8763-da1c413a082e | -10.9397 | -43.0593 | 2026-07-02 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 84954c22-f2e0-3a64-b3d5-39ab40ecc987 | -10.9397 | -43.0593 | 2026-07-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2c1a6001-a8d9-3805-9976-1eadf2951322 | -21.7823 | -56.2976 | 2026-07-02 03:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 59c7987a-c4f7-34ee-aeef-d468b33b30fe | -12.8746 | -44.3357 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 403.7 |
| 9b07e4f1-5ef2-3485-b2eb-d7fbdf9d0e70 | -21.7827 | -56.2762 | 2026-07-02 03:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4e78f807-1707-37b5-ae1e-e895f7c2e7bb | -12.8359 | -44.3422 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 9ac78b97-e976-3529-8486-755bd8b95cb6 | -12.8557 | -44.3154 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 548e383a-b80c-3ea1-96d1-762e0878de98 | -12.8552 | -44.3389 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 497.3 |
| 634ba6ee-4362-383a-830b-956423b8eec0 | -10.9401 | -43.0355 | 2026-07-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f272d005-e24b-3883-8dd8-8f8ca6b819dd | -11.4147 | -56.0726 | 2026-07-02 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8738e10e-1899-396a-bae3-dddca668fb42 | -12.8548 | -44.3625 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 239.7 |
| b407b77e-790e-3a37-a828-4822cbf9e043 | -11.4149 | -56.0525 | 2026-07-02 03:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9bd54e89-9ebc-35cb-bfec-a21ffea185a8 | -12.8741 | -44.3593 | 2026-07-02 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 19d85f55-ae97-3783-afe6-e28ddba75ace | -11.8007 | -57.0032 | 2026-07-02 03:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 20e6acfd-6926-39f0-a058-71a1327f0465 | -12.8557 | -44.3154 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 012857f6-3ff9-3dba-8e72-87661a7fab14 | -11.4149 | -56.0525 | 2026-07-02 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ff8a79ef-b730-3b96-a1b9-f526bcd359a5 | -11.4147 | -56.0726 | 2026-07-02 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 43fc4689-0596-3ddf-aa9f-731fd44ccc52 | -12.8552 | -44.3389 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 425.6 |


[Clique aqui para ver as próximas entradas](README7.md)
