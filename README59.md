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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a8f79eb-f3ec-37e6-b27c-8ab2382b8b9c | -18.0828 | -57.31255 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2cefe600-d1b2-3fa1-9f6e-c06dc66d235c | -18.08275 | -57.33608 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3a2bd3e2-18a3-38d4-b1a1-88e017076394 | -18.08186 | -57.34061 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 65d18c26-fbd0-3ba9-ac81-c4004cc8a165 | -18.08043 | -57.30441 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d3b059d0-28f2-38c5-bff0-3c7ca9a7d669 | -18.08018 | -57.30264 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bb7eeb7f-8808-3824-b567-eca03b66ffe9 | -18.07957 | -57.30893 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d4011827-a237-35fe-b10a-6cccba194f1c | -18.07929 | -57.30714 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e05d3422-99ee-311a-82b6-a10f7eb71b49 | -18.07872 | -57.31346 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4425c2f3-8608-309b-b3a7-a9524b1307a0 | -18.0784 | -57.31164 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bf3b34ea-a18f-361d-a23f-ed145a1b90e3 | -18.07796 | -57.34159 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 38ea30d9-3db7-3185-a7f6-bf3fe2e250c6 | -18.07746 | -57.33969 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 394f1395-910a-3f69-a295-7ed470d521bd | -18.07604 | -57.30349 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d1445d4e-79c4-3439-b7cd-057e424c620e | -18.07579 | -57.30172 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bf793ac6-cb2d-3ede-adc6-303caf577377 | -18.07518 | -57.30801 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1e5095f1-b67b-3dd5-97f7-2fca8b6d5e6e | -18.0749 | -57.30622 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6c34f2b0-868e-3526-901f-eaf5ec86df4b | -18.07432 | -57.31254 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d0f63fc8-a27b-3048-9ff5-8f343dce6e7f | -18.07401 | -57.31073 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e26d65a1-54fc-384d-ba96-1190ea5b0f72 | -18.07355 | -57.34068 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 17f1aa46-f8c8-396c-a916-0f29a28a19f2 | -18.07346 | -57.31705 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| abfcb804-9c52-331a-b6c6-e6e25cd7cef9 | -18.07312 | -57.31524 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| baaa4077-634b-3d5d-8bc7-ba2088aaa622 | -18.07305 | -57.33877 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 31f86dba-1153-3a40-8c1f-5013034afeb5 | -18.0726 | -57.32158 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7df9b9b1-6688-369e-a7c7-22877ad2d07a | -18.07223 | -57.31975 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1fa73a8a-e318-39d1-90c6-a28cf849180a | -18.07216 | -57.3433 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0141ecfe-bb02-3929-8ad4-76ffbc88abf4 | -18.07134 | -57.32426 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 91236486-aace-38f3-8029-e1d88170f02f | -18.07078 | -57.30709 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f8d89331-a20e-381b-b8db-95f8e0ae3031 | -18.06915 | -57.33975 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 587a0419-223a-383e-93d8-7549494a8b29 | -18.06865 | -57.33785 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 562d4d29-3a5e-378f-ab00-11e66fa44976 | -18.0682 | -57.32066 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3fb4fd10-740a-33ba-9986-7b734477c641 | -18.06734 | -57.3252 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c71ef5b0-958e-3ccd-99c1-0dd7adacc8cd | -18.06619 | -57.25932 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a695df00-4b56-33b2-ba86-d985b2f6a276 | -18.06553 | -57.31069 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 164da523-cb54-328f-9cd3-dc66d67dd833 | -17.95462 | -57.22393 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9d3c2395-4297-371a-884c-ead469dec187 | -17.95024 | -57.22301 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f51d53fd-c098-3c54-8c57-f023defd0be3 | -17.93967 | -57.20686 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fa5d5a32-4b7a-3d01-877a-d554e5202e6d | -17.83624 | -57.57262 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| c0156018-673c-36b8-b7cc-c9cfe6aa63d0 | -17.83531 | -57.57734 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 882160e1-127d-3124-88f8-be0ed6789ba1 | -17.83438 | -57.58206 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 04119aed-6185-3571-b757-a377dc2a4709 | -17.83081 | -57.57644 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| ae30f8ba-63f3-3ed6-8aa4-2e65a15cbd0c | -17.82632 | -57.57553 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 33412261-4a9f-3305-9b89-2f5009abf7b0 | -17.82538 | -57.58024 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c454f08c-a40c-3bec-88c7-699924d003fc | -17.82165 | -57.59917 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1099664-6d73-3144-9464-aa13eef39ea1 | -18.06095 | -57.26289 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 47610f10-9178-3108-abc2-ea853663d9db | -18.06027 | -57.31429 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5214c831-7f3d-367c-9184-d48e7e47bfd4 | -18.06009 | -57.26737 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 477b6e8b-4c53-3c37-b3b1-87341043a252 | -18.05657 | -57.26196 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 747df2f6-c14c-3950-9f18-4d8ea0f35e66 | -18.05571 | -57.26645 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| eacd226d-cdee-3579-b613-2c6186928838 | -18.05501 | -57.31788 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| aaa7308a-01de-3fcd-90ac-bc2ecb110fe8 | -18.0532 | -57.3034 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| d09f7be6-c75f-3475-afa0-152011d0560c | -18.05234 | -57.30792 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 14b34dd6-557d-3b1f-bee1-de7ea4ed51c2 | -18.04974 | -57.32149 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 553bc5b9-b255-3f09-86f3-3c2783b8e811 | -18.04794 | -57.30701 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b9012985-a7cb-3f31-a602-89a8e49ab5b1 | -18.03924 | -57.35235 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 57b5408c-82e3-3400-b8c3-53e88ec0b942 | -18.03745 | -57.33779 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e53f6b78-5412-3da4-918b-73a38ac1f53f | -18.03658 | -57.34233 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1032384e-931b-3efe-9019-7e3c71e0bf3b | -17.99957 | -57.25009 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c5ef96b6-dd61-323c-a818-1fda5510a24a | -17.99869 | -57.25457 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1ad42b19-5077-3fcc-96a4-7a2e6dbdd3db | -17.95985 | -57.22038 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e5c9cf80-caa5-32a0-a2f7-7c1f054b2dc6 | -17.959 | -57.22486 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 75fc63c1-48a5-3a62-bf2f-1c2674f7a32a | -17.95814 | -57.22934 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 39f5859c-fb44-345c-8b99-29bf61aa2cf8 | -17.95729 | -57.23381 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 53be517c-5bb9-3911-b788-96cc197478ad | -17.95547 | -57.21946 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dc580b44-5f9f-3896-9adb-af42d53288af | -17.93882 | -57.21133 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e23a656d-b173-3c83-b2c9-1448db8cfc08 | -17.93796 | -57.2158 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9adb6db6-b972-32a4-86b1-134e4a3091cd | -17.93709 | -57.22028 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 00c5901e-bee4-322c-a56c-27b57ffd1232 | -17.93623 | -57.22476 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6ca821f9-44ef-3735-b32a-85db1501cdb6 | -17.93537 | -57.22925 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 49f15c51-083c-334e-a0d9-b1b5811c0692 | -17.9345 | -57.23375 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d19c7457-4961-309b-be0b-689c25a40cd8 | -17.93357 | -57.21489 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ddb534a7-5c48-300d-94cb-4aa5edeecc80 | -17.93012 | -57.23283 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 13d255f2-cfac-3e19-ad0a-221b9490dc45 | -17.92665 | -57.2508 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2b8675ec-1564-3df5-8520-d2250a855bd2 | -17.92487 | -57.2364 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5ec3539-cc81-3cd6-bfdb-c1ec35709306 | -17.924 | -57.2409 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 28c1de34-0b4e-349b-9a24-8ab95a0c4dd1 | -17.92313 | -57.2454 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d7db6c84-93cd-3491-bd23-9866221e755e | -17.92135 | -57.231 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 005e8cfa-1151-3e54-9a96-c1b136f213fd | -17.92048 | -57.23549 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 8fc77c5d-5288-3cb9-9a9d-be43cc61dd9a | -17.91961 | -57.23999 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4a435abc-6b59-3077-97b5-e74ab579209a | -17.87252 | -57.22614 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 49301b3d-d893-3b90-8d8a-6824bdb378dc | -17.87221 | -57.22548 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cc2a4613-bbd2-3725-9195-3543d68bb7fd | -17.87133 | -57.22997 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 03ce2252-85cd-3dbc-9e74-6de76ed9305a | -18.67115 | -57.35461 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 78bf441c-91e5-35c4-a075-362c4317934c | -18.66679 | -57.3537 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| b20a8641-1866-3a91-ad86-0c11f1ba5d1c | -18.66329 | -57.34834 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b48d3868-ed13-30d1-8778-9d98d75d9c53 | -18.66242 | -57.35279 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 9535b602-01eb-357c-aae7-2e49ae761cfc | -18.65893 | -57.34743 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 188638e4-e4d7-31a3-a638-4aff50ad453a | -18.65803 | -57.32875 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0e7bb7e1-c20a-3871-ada4-4bd7d77bc6bb | -18.65717 | -57.33318 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dec9e741-ea82-342c-87ce-6d5888791d58 | -18.65195 | -57.3367 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fb6df729-84bd-36c5-a785-b4ac9b31bf21 | -18.1162 | -57.32893 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 67d98bf8-a3e1-3c9e-b5a9-294e1e1e693e | -18.11533 | -57.33345 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bbe9929f-5214-360a-9f5a-499387e30a13 | -3.93318 | -46.42427 | 2024-10-24 04:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 666f54e0-7617-35c4-b3ea-f60e819863d2 | -3.93816 | -46.42943 | 2024-10-24 04:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c6fe9f81-347a-367a-8a0f-92b3f36c5ed2 | -3.94403 | -46.39378 | 2024-10-24 04:44:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c6bf1818-5bbf-36ec-aadb-d8de3ac77b45 | -4.5595 | -44.01116 | 2024-10-24 04:44:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7c2dadc7-df4b-3a07-b97f-bb0426d9f98f | -4.7646 | -46.39488 | 2024-10-24 04:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 4792c69e-0aca-30c3-a8ca-f4fe10e4951c | -5.58178 | -44.87757 | 2024-10-24 04:44:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 9d32263e-5552-3421-8307-0cfbcbd4860f | -5.61956 | -44.82963 | 2024-10-24 04:44:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 5062d83c-45b5-39ba-b375-d8516f07cf90 | -7.5326 | -45.83628 | 2024-10-24 04:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 31210230-ed89-38fd-97d3-d5a79526beae | -10.36986 | -45.08004 | 2024-10-24 04:44:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 7b92d454-426f-3c4c-b8a0-7001788671ab | -10.60026 | -44.26618 | 2024-10-24 04:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |


[Clique aqui para ver as próximas entradas](README60.md)
