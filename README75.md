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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b5d83b1-11b5-3649-bb8e-3c2cc194142e | -17.85781 | -57.59506 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6ce5c88d-553a-376d-8fb9-2b1c1484aa45 | -17.92536 | -57.6114 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 79341f36-4129-3714-a33b-f4b34a01f29a | -17.85747 | -57.63504 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6fac6df5-e58d-3180-aa19-fdad4b322652 | -18.00119 | -57.59637 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8a863a6c-e1dc-3cee-96c8-9c07aac78b5d | -17.96485 | -57.55465 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 663ed116-a787-35dd-8a7e-b2851ef93938 | -17.95786 | -57.59689 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6bc63c75-8992-3681-99d9-b96e4dd8da79 | -17.95881 | -57.59965 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0e17ad42-533d-3382-b30a-99ccb0f6f0cf | -17.95819 | -57.60429 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fa8fdcd4-34fc-392d-83bc-361c17836466 | -17.93035 | -57.60283 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5aecf319-7530-316e-88a9-a991f7928eaf | -17.85805 | -57.63074 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9efa9e91-8559-3c3a-8eb5-da7fe1d49e2f | -17.88609 | -57.64804 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 876e6458-d77e-37b8-bbb9-a20f855445da | -17.87552 | -57.64197 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f0262eb1-7075-3864-999f-6572349098c7 | -17.86805 | -57.58483 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| b6b73d40-e42b-3572-b9e0-29199e84bd02 | -17.99058 | -57.53371 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| cc1c2b9f-fd7b-3d32-8e37-3d7010c2f318 | -22.36774 | -50.02573 | 2025-10-06 05:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c3f769fa-89d0-3ec3-96ad-05ea47d02019 | -17.97288 | -57.54399 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b6922dd-879e-3b57-94a7-c11de2408a67 | -17.85315 | -57.63894 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2eab4a93-1730-3b33-b15d-414ee16c0401 | -17.95942 | -57.59504 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b84642c8-2d1b-322e-9b2f-c277a879060d | -17.9047 | -57.65087 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2e92c82c-af4b-3fc2-a605-1f73e317f80f | -17.97734 | -57.53947 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 220f7eda-7e1f-3917-bfbd-c14af7224cc2 | -21.70177 | -50.08286 | 2025-10-06 05:21:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 41419ef6-be80-32d3-ab52-5e57b92f1e88 | -17.96338 | -57.61192 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ea5c2aa1-ac0c-37aa-8ba9-5f3313546a9b | -17.96316 | -57.5956 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b7eb30a6-3789-3501-9982-01d99bf56119 | -17.96816 | -57.58676 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e0a7850c-1c88-3868-b8df-4d5f89ead377 | -17.96794 | -57.5794 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| da510883-67c8-37d7-86c7-2b9807084f63 | -17.9766 | -57.5447 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a62242ad-d7c9-3244-965c-640b39496dee | -17.85658 | -57.60387 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c458f2b6-a90d-34fa-ad59-94ab67063ec6 | -17.96748 | -57.56339 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fd98983e-3839-3045-a49b-44eeb1f1be15 | -17.87553 | -57.58586 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c68266d2-0369-30f1-9915-5cb087a9ed0c | -17.94096 | -57.60874 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 091b6180-8811-3726-897a-5772504dbcb3 | -17.97863 | -57.53724 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 488f3b65-0ec4-31d0-8789-a59d5fdce198 | -17.99432 | -57.53434 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 9f2168c4-e483-33c3-97b3-e109b61ae9c1 | -17.97689 | -57.57858 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c357ee7d-1da3-3058-9f10-d663e094ebb0 | -17.85815 | -57.60175 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bda47e4d-7359-3155-a641-10731b5626f4 | -17.98613 | -57.53836 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 4c9f590a-c4d3-3f9b-baa3-4e32a78def6b | -17.96533 | -57.598 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3b3f622f-384b-39e1-a05a-710086ab0b44 | -17.95283 | -57.60563 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 30db4b24-dfa4-32a3-83a4-9898ad0159d4 | -17.99228 | -57.54953 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f0f88479-9113-3067-9995-1991e6bd41dd | -18.00556 | -57.59224 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8dd6d90f-e570-30fd-a612-cb0b1da57b94 | -17.87925 | -57.64249 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7064dc06-3527-3877-857e-3c1c09f14491 | -17.96599 | -57.59334 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 31cc740f-c452-3280-9f1c-d4c7a421e4b2 | -17.92472 | -57.61598 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 155879e5-5660-3bcb-ac63-6e64ed00ba04 | -17.99977 | -57.55063 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 007e5eef-f7dc-3b14-b676-a20bcdcabc32 | -17.88981 | -57.6486 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9dad5aa-7aca-3b9c-a33b-4e2257e846ec | -17.97934 | -57.53195 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 25d692c4-a1d3-3264-9c23-c375163a4021 | -17.97119 | -57.53571 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8b95cc95-17e6-3e43-8f8e-7442025f711a | -17.96861 | -57.55505 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad838e5c-3111-32b9-bb89-9d9e9e9393b3 | -17.86094 | -57.59992 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 56b0ada6-b4ca-3256-acd9-fe84825bdf26 | -17.92974 | -57.60729 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49f6f61f-0d1e-31ca-8f8a-701bed28f34c | -17.96814 | -57.61528 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a0095dde-5832-3200-88f7-4bd9cc307f61 | -17.84819 | -57.63643 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7fd6c295-5995-3c37-9e39-dc07b55da369 | -17.86367 | -57.58908 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 186b54f5-bc24-3a0f-8b42-45507a62fae7 | -18.00042 | -57.54578 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d38aa80b-4d90-3e38-ae77-a19fa4e5ea9a | -17.98987 | -57.53896 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 1ca6fe51-dd45-3b6b-ac12-a7832466972b | -17.9178 | -57.61099 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b1289a45-3166-3f5e-9356-b41113712757 | -17.87434 | -57.59459 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 365dfa2e-d739-3ff2-add3-c28bfc7c9c88 | -17.9617 | -57.54195 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5545530e-9b24-3c6b-a54f-76b49ad2f821 | -17.96617 | -57.53735 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b94b4df5-1429-3eb9-a722-344889b1b8a3 | -17.96753 | -57.59143 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 84144bf1-148c-34be-abea-8f7a35f0af96 | -22.29181 | -49.90855 | 2025-10-06 05:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d786f0a8-a214-305c-a744-af24c05f143d | -17.95722 | -57.60151 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 715a403e-b952-3f9c-8cba-7132314138fa | -17.98934 | -57.59937 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 369901be-f7bd-3ca2-a339-67bbe01c8cb2 | -17.85934 | -57.59294 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| dc299653-46c9-3daf-a3b1-51dabf3ebc27 | -17.96664 | -57.58867 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d523bf75-6669-3921-934a-47fe437a5989 | -17.96627 | -57.57239 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7513b892-79e6-3aca-bb16-c030fe408fb2 | -17.8767 | -57.63336 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bea6e937-9746-3b85-8854-b5734d6f6071 | -17.97315 | -57.57803 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8c432227-cc02-348e-b12d-60c87edbee55 | -17.95756 | -57.60897 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 804dc9be-b091-3358-911d-1df4033bfce9 | -17.97162 | -57.55304 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dd045df1-0a2f-333e-b717-e0db144b63a0 | -17.97294 | -57.55121 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6853c705-a4b6-3d93-9e63-3dc4d4638d66 | -17.97363 | -57.5387 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| ee634ae8-a0d5-3539-b6ed-45737de223d0 | -17.87493 | -57.59026 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 8c0d4220-ac37-3ffe-9e59-b135a570ce3d | -17.99992 | -57.60569 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| aaef1b2a-2d30-3c10-a19f-07c80ecfab38 | -17.94787 | -57.58644 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 73a70d6a-05ca-3b99-a0f4-691427618b79 | -17.96842 | -57.60315 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6ee44832-4d61-36a8-a4b2-fdebc46ae591 | -17.96923 | -57.57021 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6b95f01d-d453-3a5d-bd68-636a7f46d389 | -17.96095 | -57.60207 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ed34e97b-d42c-3053-ac5c-4354e813fe48 | -17.96312 | -57.56745 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0b09ced5-c22c-3a5d-b03e-0502a91fcdf9 | -17.91718 | -57.61548 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 20d604e9-1092-3925-8a28-57f99e0008ce | -17.84562 | -57.6385 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 67c29a9f-c7f4-3bef-b256-75dcdbb51dae | -17.98249 | -57.59362 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| bd5ee63e-c070-3298-a2ea-b04dfa0d027e | -17.99805 | -57.53505 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 65e94276-2cb5-399f-a8d6-fcabb925d4bc | -17.94032 | -57.61337 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fe3e0382-2162-3f21-9eb9-3ce3d803a2ff | -17.87061 | -57.59408 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 8a869f9d-075e-3cff-af24-d7086547358e | -17.84938 | -57.63874 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a031266-d0a6-345b-80dc-878a07255736 | -17.93658 | -57.61284 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ca9d55ca-a230-3259-9953-c687fab40a2d | -17.97421 | -57.54179 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6a0da153-8f41-30cb-859f-19c3d6109114 | -17.98046 | -57.55214 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bba00853-7129-318f-b7d3-04b0a2ed2b9c | -17.99928 | -57.61037 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 056562ed-3dab-3a64-aea6-157beb662add | -18.00301 | -57.61093 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 69036e5e-fe0a-39d3-aa34-e90ff47613bd | -22.07631 | -54.12987 | 2025-10-06 05:21:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b84a4262-9de7-32bd-a746-32e01043947a | -17.9775 | -57.60237 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bd9838b5-db02-36ef-afe3-018e40652097 | -17.97237 | -57.55548 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6f98f63e-d0f8-3155-ae16-b53a26b8ea2a | -17.97812 | -57.59771 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a295abd9-4fa8-3fba-8032-a90f86c42219 | -17.86684 | -57.59381 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 01ce85ba-81a7-3461-b009-efbcf4ad7712 | -17.92657 | -57.60257 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f8dd7396-5c2a-30ce-83b4-3a687aca2689 | -17.95964 | -57.6114 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 441ae3ec-f7a2-3e04-9c26-6bc8d81ebb15 | -17.85688 | -57.63941 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 312d0fa9-449f-3bbf-8893-4a1847a970ed | -17.86743 | -57.5894 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 8dbf138c-629e-3d0b-b736-5e033f073ff7 | -17.98186 | -57.59826 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README76.md)
