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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c7ecbe1-f466-3898-bae3-f0d1bb5b6e62 | -2.76802 | -48.65192 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903ad9ae-0f60-3eb8-afae-9343fc3d58ff | -2.75713 | -48.66336 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e19698-5590-35dd-9d75-8723429079dc | -2.75643 | -48.66766 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f386b6ea-952b-3c4d-8937-cbe4a7925548 | -2.73494 | -48.74423 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcb699c2-7a3d-3ec0-9dec-11fd9d6f98bc | -2.73423 | -48.74862 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed5b7b00-cdb5-37cc-a9fa-96022255e5b3 | -2.7335 | -48.75307 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1eaed23-a094-3270-a752-1ba8a2eae93c | -2.73121 | -48.7392 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea89d43c-6ede-3a80-886e-883e61022dcc | -2.73051 | -48.7435 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10f07aa8-ad15-347a-99cc-37df4fc1777f | -2.72979 | -48.74789 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44bbcaf9-f8d4-3a68-bef8-a0124b0cba68 | -2.72907 | -48.7523 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b6dfb74-d14b-3d56-bdb6-2120053d598e | -2.72891 | -48.72538 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7c643f-0367-3295-bd5c-24f6625011a6 | -2.72448 | -48.72467 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ae023fd-f165-396d-a3df-2b4aed68b666 | -2.7172 | -48.74137 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db45a2a2-9c49-319c-94b7-fb4268b3e4e1 | -2.71649 | -48.74574 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 638e3a13-46e6-3a0b-abd0-aff1cdb42040 | -2.71576 | -48.75015 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019d55d4-b137-3f31-8478-30ec19ef1cbc | -2.70688 | -48.6398 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9185aec5-ae12-3028-8f68-bea5f1284fcc | -2.70638 | -48.64187 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 458481c1-f097-3aba-9df2-89cfee6032aa | -2.7062 | -48.64412 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e30b4d24-a105-33b8-a0cd-cb827c14b021 | -2.70567 | -48.64617 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c5b89e8-4c89-3fc6-a587-05b943b882a4 | -2.70552 | -48.64843 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ce12376-2b8e-32ff-b935-e481501a7625 | -2.70198 | -48.64113 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78648d31-a7fb-33e7-8095-395ee968d183 | -2.70179 | -48.64339 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6a2720a-2bb5-3781-8738-438537d47517 | -2.70126 | -48.64546 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a82b7bf9-860b-35de-9d77-e33d3343a00c | -2.70111 | -48.64772 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31f6f7d2-8453-3a89-9331-9cd47d0b250b | -2.67329 | -48.65199 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f8f8cad-3319-3f88-a470-0e9d43a443d0 | -2.66889 | -48.65125 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c726739f-8dc5-317a-8a81-6563385ec442 | -2.66302 | -48.57556 | 2024-11-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1e2ac35-ae7f-3bf7-b992-0fa4bf0b0e74 | -3.95978 | -48.13794 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2b4403d-be02-39e3-85bf-64c36046bc9d | -3.95918 | -48.14166 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 581aca92-6ea8-3ae5-acf0-58c8d2e0e89a | -3.95501 | -48.14097 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3da76fbe-abf0-3221-9927-3ec1945bdd12 | -3.94984 | -48.89886 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0b6ab1b-925f-34de-841c-5f39ead4a2b8 | -3.94498 | -48.36204 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 95154e29-2f31-3eb5-945c-316806c947da | -3.94169 | -48.35851 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cb4a77ee-15f6-3874-a564-3c36595bac33 | -3.94075 | -48.36135 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e27f06aa-2302-3d22-befe-10febbfff8cb | -3.93937 | -48.34587 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3266ab4f-488d-3680-987d-41cd98e1877b | -3.93918 | -48.34475 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bcfa45fb-940a-39c3-8d24-b8e161ad325d | -3.93874 | -48.34981 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bac72808-a0b7-3da7-a23a-35a4f95351fb | -3.93786 | -48.35261 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7b39efc-a039-35cc-83c0-6efeafa4cd16 | -3.93746 | -48.35778 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b92e36a7-2d7a-3495-9fb3-32b8b19c2977 | -3.93719 | -48.3566 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6cf338ed-2d1d-3624-b01c-6f617246e5a1 | -3.93682 | -48.36183 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0addae0c-3ba8-3632-b86d-70e4940bf717 | -3.90947 | -48.36951 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a55218-60f7-3551-9784-354c786cb103 | -3.9091 | -48.92716 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af1b7adf-42a7-3dd1-b581-ab3614b4663a | -3.9077 | -48.9357 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa359835-0ea3-34a3-96fd-378baab5e8dd | -3.90618 | -48.33617 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e072c2b7-067e-389f-a1be-c2a8b5b02025 | -3.90459 | -48.37278 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb277644-6a26-3875-abe0-02d5156ba8cf | -3.88762 | -48.36996 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d941e6e1-9b67-3fce-bf72-0cc82a0bb7dd | -3.81725 | -48.8828 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9d98488-eafb-3485-83e8-e70c9be5bed2 | -3.81654 | -48.88718 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8495f225-fc13-32ad-8adb-fd15785a2075 | -3.76624 | -48.10778 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67525eeb-f8ce-3b3f-af79-418469b38e59 | -4.44423 | -48.17548 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 927d9a10-6719-3fb3-ac41-9c51f015907d | -4.44008 | -48.17479 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce15f21c-3698-3cc2-8f2d-d865db397ff3 | -4.37017 | -49.11144 | 2024-11-02 04:12:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 481c38c2-17e1-3e0e-9f34-11988ec45811 | -4.35909 | -48.61034 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 830d2918-245e-3443-8270-3791139a803b | -4.35843 | -48.61434 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81784eb3-2871-3d95-b352-6e4b00a8edae | -4.35777 | -48.61829 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9bbce2d-5462-3a98-ac4a-06a6b418fbec | -4.35579 | -48.15824 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7538a0d-1d78-3745-8594-be3d22f67600 | -4.35577 | -48.63028 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ce8d688-1597-38f7-bef1-44ce7b76c6a0 | -4.35511 | -48.63422 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 640a6421-be33-39a0-b27b-a5c88d4e25a8 | -4.35445 | -48.63821 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4010e010-b213-3d1b-a5bc-d0740ae43ccb | -4.35349 | -48.61759 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f09e58e-69db-3c24-9cce-3b7192bd2855 | -4.35163 | -48.15761 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc698eca-fb48-30bd-a3d9-9bbc835b477a | -4.35055 | -48.60885 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38973c15-016c-3099-b553-84ecc99debf7 | -4.34747 | -48.157 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee4aaa44-d567-35de-a1af-5827e7dbf174 | -4.34443 | -48.72488 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c97e38-91c1-3a43-89db-7adb7175dab9 | -4.34267 | -48.6034 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82e7f05f-b854-38d3-a7c1-be8606c71514 | -4.33365 | -48.58763 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb5470a4-81e9-3dcb-b537-8f6c9950425f | -4.33237 | -48.59557 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54d13af8-8c03-3758-ab27-e1248ef8c93f | -4.32456 | -48.64416 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6c20dd00-a1be-3c8c-bce3-5633cff7fde0 | -4.32303 | -48.64161 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d8bffad-2526-314a-9ef1-f80c1fbd23f1 | -4.3209 | -48.6395 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f104b23a-bcc0-37f2-b61d-ffd57af42bac | -4.3196 | -48.64759 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bc46846-a0d8-3ee2-aad1-f7df190d73ed | -4.31873 | -48.64095 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3b4966fb-7f9d-31c1-95aa-99fc12956a47 | -4.31595 | -48.64287 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c06916e-410b-3925-866f-349b11380644 | -4.30507 | -48.62843 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dba063e-00ff-3aba-8854-fb5e9c20f861 | -4.30144 | -48.62368 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcc136b6-a019-338a-ad6a-fb5155923019 | -4.30012 | -48.63183 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c122daec-ad2c-3343-bb62-78858c5a8455 | -4.29715 | -48.623 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 185eb767-c656-3c33-80bc-109e31c5f63c | -4.29648 | -48.62709 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da060be1-dd26-354a-8817-83f11fec622a | -4.29582 | -48.63116 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9d194f7-148e-38b6-9098-f5ea1fba4478 | -4.28824 | -48.59676 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96c53f10-74db-3090-952e-668595f37eca | -4.28758 | -48.60079 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13b7db01-0f50-3508-bcae-7cfb412ee0eb | -4.24658 | -48.5566 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c45e68b4-2984-32fd-b134-fd200b7f1f0c | -4.23616 | -48.54734 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 601034f7-a045-3065-a322-8f8c2710ea28 | -4.23445 | -48.55046 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef9c8c14-5e58-35af-9fa2-b34bd01a7bf8 | -4.23298 | -48.7173 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea16b5a2-1ae0-329e-9a4a-c994a83424d5 | -4.23229 | -48.72146 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c88a29ec-9ab9-36f4-a4ed-b839a2e65393 | -4.2257 | -48.55784 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a480849-2169-3e57-a77d-46f9518780e0 | -4.18775 | -47.98901 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15be007c-bc6e-3496-9766-7543aa4d9cbf | -4.12266 | -48.8632 | 2024-11-02 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e135088-f2e1-3b16-8647-f3c6a0f68a74 | -4.10758 | -48.51061 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734b0273-c270-3f37-96f6-59fae513dd4f | -4.06036 | -48.24395 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f27cbfe4-cacb-33d1-8fa6-e2f10040cf3c | -4.05953 | -48.24414 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55cc1f91-ee56-3245-b62c-f28ea171d2e6 | -4.35644 | -48.62629 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad151873-c6a4-3e6f-bb19-83da907d31d1 | -4.35482 | -48.60963 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a42b48b-ab0b-317a-bed5-c29210d49b64 | -4.35415 | -48.61361 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bd52b98-ec81-3dd8-869d-5308d10b763f | -4.35228 | -48.15366 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48a2141f-3f10-339a-9004-96bc2f182772 | -4.35121 | -48.6049 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fd2c9664-777a-3168-884f-0c0eb4c1d28d | -4.34989 | -48.61281 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11d2148e-cccc-3c1e-92c0-a5745e7c2fab | -4.34921 | -48.61684 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README44.md)
