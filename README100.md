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
| 4a2c44dd-f530-3ce5-a543-8d9464293c13 | -19.36964 | -42.57888 | 2024-09-27 04:42:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 91463470-0122-36ec-ae49-3c0c9a0fe07e | -19.27508 | -42.7289 | 2024-09-27 04:42:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 70b78350-77fd-3ebb-b2bf-45a8a4ef766b | -19.27471 | -42.73246 | 2024-09-27 04:42:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 00253392-8918-3994-ba2a-809400cb8f6a | -18.70787 | -42.1059 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 77d271b4-6547-3c40-a34b-867f05a1c9ad | -18.70226 | -42.1057 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| aa9605d6-945c-39d9-aac7-53eb76785383 | -18.69855 | -42.08714 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93707b2c-a7e2-3c36-a997-bf40b79f708c | -18.50089 | -42.21663 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a8ab4451-b54c-3694-916f-5d88efcfb60b | -18.70823 | -42.10241 | 2024-09-27 04:42:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 40e4bfc1-31f3-38fe-a53f-a68f31095ecb | -18.48557 | -42.19961 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c604d320-f183-354c-8199-e95e08c3e123 | -18.48478 | -42.20707 | 2024-09-27 04:42:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| a37d847e-89bc-31de-be4c-52f1b4c48664 | -20.33222 | -42.73196 | 2024-09-27 04:42:00 | NOAA-21 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1eb83ebc-f93a-3338-a1c3-4f2fe3b0d979 | -19.86919 | -42.16852 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a0da353d-a180-32fa-bc66-bb23179ee617 | -19.71821 | -42.39051 | 2024-09-27 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e90ff702-599a-3962-9e71-5bf626977051 | -19.62279 | -42.82013 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 9ec30c23-a4d8-3b78-a210-517e271af9f3 | -19.61642 | -42.82891 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 322f6ffa-9a24-3424-ab7c-22b8237b832d | -19.61608 | -42.8321 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| ea2e0f0c-0d04-3223-a306-925285e81ee8 | -19.61387 | -42.83047 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| d6bb2516-bf3a-3b98-b174-e2b98bfc31bd | -19.60731 | -42.81217 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ca1c6ec0-ae7d-3f5b-baf9-7fcd66045c62 | -19.6069 | -42.81605 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| cbec523b-a683-3555-94cd-c391bf283a0a | -19.60545 | -42.80536 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4190bf88-cdb3-32f4-9f51-94636daae4f1 | -19.60469 | -42.81323 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 8c6498d2-136c-34d5-a060-fa236c0ef62b | -19.87516 | -42.16565 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09e3d625-414c-39ec-a9bb-ffae89f4fecd | -19.79027 | -41.95226 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2e264a03-eff6-3d57-9edd-eb3b053f5256 | -19.74378 | -42.19056 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b311455-7260-3f58-a278-51f25a283c82 | -19.61485 | -42.82053 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 001bf464-30fd-3f38-835f-6ffe4c228dc7 | -19.61452 | -42.82387 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 07ce62e3-9b6d-36ed-9fa5-c99422c1452b | -19.61177 | -42.82146 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 71f8ddb2-9ab3-30c3-932b-46700794e44b | -19.6114 | -42.82498 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| f1036369-bc70-3c14-ba26-60b64d1129be | -19.60815 | -42.80418 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 24fc11fe-73d4-3758-a9cb-808f507eea45 | -19.86982 | -42.16224 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b8d83d32-3a08-31a7-ae3d-0d9760b5e8ea | -19.86257 | -42.17789 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7c63d2b2-0a20-3e4f-b8df-5aac9c851e7b | -19.74935 | -42.19152 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c484e2a8-ab92-3ff6-b530-62bf3dcd4fd0 | -19.67432 | -42.43921 | 2024-09-27 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b164ec82-8a3f-3e01-b3d9-c519d6b41ff0 | -19.63467 | -42.83965 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3ea0b7f9-f3fc-3ef6-9f07-f37ac346480d | -19.63192 | -42.81281 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bcb087a5-e6dd-3559-a938-ede030d4316e | -19.62934 | -42.83874 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7c3354f-e27c-3ee6-a074-d463ae97083e | -19.62054 | -42.81806 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 9c4d51bc-4b11-309b-8805-3c37232accb5 | -19.62017 | -42.82178 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 12315669-b201-3410-8965-9b7dbef40738 | -19.61987 | -42.82479 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| e683b4ca-ffeb-3e1e-8443-7a437bd1ea5c | -19.61926 | -42.83083 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| bc085a93-2929-34c9-b94d-d818890109d2 | -19.61744 | -42.81922 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 28852d92-07ba-3c81-bd3f-65f151d40d80 | -19.61068 | -42.80759 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9f2df313-725e-3acf-b1a2-7deba010d169 | -19.61028 | -42.81171 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a484a1c8-55b2-3e85-b937-e37235434737 | -19.60955 | -42.81913 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0be209f6-2969-339b-a9af-0499af77581c | -19.60773 | -42.80824 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 525793a6-83a8-3cac-8b74-83089f028469 | -19.5984 | -42.63489 | 2024-09-27 04:42:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb0e9927-f26f-36cd-89c0-47db4d3c9394 | -20.12162 | -43.44119 | 2024-09-27 04:42:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4483977c-5342-34d1-8792-46d23d7ffa41 | -20.12123 | -43.44506 | 2024-09-27 04:42:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c1f3253-b7b6-3046-9c6f-db7bacd76b7b | -19.8695 | -42.16544 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f895ea97-f67e-31bf-8335-cae6820562f6 | -19.8622 | -42.18163 | 2024-09-27 04:42:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a66568fb-edfc-3b38-bc32-3e9784627a8e | -19.71268 | -42.38993 | 2024-09-27 04:42:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e6868005-6e38-3b2c-a0b8-b90b706ca90e | -19.62599 | -42.81782 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 818fe329-3d54-3539-a270-3a275a71acd9 | -19.62327 | -42.81556 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d17a31e9-06db-31f4-9c59-7bccfefcd89e | -19.61957 | -42.82779 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 22671c08-2f09-3cd2-b8d8-35a828f955dd | -19.61708 | -42.82261 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8bcdea74-9474-3f93-86df-3590a08ffd79 | -19.61675 | -42.82576 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 1f853544-6e91-3ceb-a15f-91cb0e802c8a | -19.61521 | -42.81694 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 03cb1603-413d-3577-85b7-fcf821e212cf | -19.6142 | -42.82718 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 3dcd6aaa-7bfc-3b3f-83d6-af150d9fba32 | -19.61251 | -42.81443 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 91ad1c11-a308-3469-a302-d8f2e2cf53c1 | -19.61214 | -42.81796 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 99c1ee42-dbc6-3424-89cc-b673a51eca5e | -19.61102 | -42.82852 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 946da746-bd4b-3a7a-ac8b-03429402249b | -19.60991 | -42.81548 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c5b16a86-7ca9-36bc-a6ac-3bf368674840 | -19.60648 | -42.82003 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 1013282f-f81b-3bd2-be64-54b39cb4d1ed | -19.60507 | -42.80928 | 2024-09-27 04:42:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cd338b74-4208-3ba3-a610-666e5ed5ba43 | -19.59873 | -42.6317 | 2024-09-27 04:42:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6712780b-f819-314d-8939-5d6b525e2903 | -19.56507 | -42.69268 | 2024-09-27 04:42:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c003f874-734b-34cc-90d7-0d808ddd5851 | -19.56462 | -42.69712 | 2024-09-27 04:42:00 | NOAA-21 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 97677845-2905-3ac5-8fd6-d9151971a810 | -20.17672 | -43.51521 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d0919cbb-008d-39b9-a71a-977593106433 | -20.17337 | -43.51404 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 8103a3c5-0fbb-3eb2-89c5-fa9459470363 | -20.17151 | -43.51497 | 2024-09-27 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 9012ca41-b695-398c-a287-4164141c0cef | -16.49428 | -43.13161 | 2024-09-27 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3eef4b9-ae6a-3b74-abe2-e7061d167dd1 | -16.0463 | -43.61097 | 2024-09-27 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43d687a-be04-3d7a-b019-cb896bec9ddd | -16.04144 | -43.6103 | 2024-09-27 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4838cc00-b990-36ff-9c9f-bfb72386477d | -16.04079 | -43.61582 | 2024-09-27 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65dd2703-4360-3e6e-9e9d-dbfc089f5dff | -18.00684 | -43.69363 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0af6dd34-9d71-329a-9b30-f2b65cf42368 | -17.95686 | -44.24997 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69bce461-2c7c-3c92-8b56-f174a2724072 | -17.95215 | -44.24739 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f334a6f-b03b-383c-a8de-3653caeb3bb8 | -17.95207 | -44.24934 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9086738-3571-3715-b0fe-b82be97e23d5 | -17.94666 | -44.25275 | 2024-09-27 04:42:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49122b30-39f4-3851-b652-1360a5055906 | -17.82736 | -44.45171 | 2024-09-27 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45eeaa32-b38b-3013-b0da-d2b9cb92949f | -17.82678 | -44.45689 | 2024-09-27 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c34d6b49-1794-3774-9523-ef04bce79b49 | -17.82481 | -44.45607 | 2024-09-27 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 679e6ff8-e7d1-396e-8c28-36464cf39077 | -17.82209 | -44.45605 | 2024-09-27 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ae158f1-724c-3a3b-9b3e-f32bf84a13ec | -17.66194 | -44.40255 | 2024-09-27 04:42:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f281ce86-d23c-3167-b0bd-cdd1de0d6cf1 | -17.52792 | -43.61507 | 2024-09-27 04:42:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df7b0780-5c00-30a6-89c9-0fb438136034 | -17.52298 | -43.61425 | 2024-09-27 04:42:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 039e9f17-d3a5-3a9c-b7c0-274e7e6db028 | -17.0415 | -43.23384 | 2024-09-27 04:42:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f9cb14c-dbc1-3612-9923-61ba62eeeb33 | -17.04114 | -43.23705 | 2024-09-27 04:42:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9834c5d-a693-3093-881e-7bbe808aa985 | -16.68058 | -43.8871 | 2024-09-27 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bac3c30-0b4f-33c0-b701-caeccccea280 | -18.95173 | -43.51639 | 2024-09-27 04:42:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a5b78e6d-bdad-361a-9786-f9ee80fa3861 | -18.36944 | -43.9565 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f270776c-4106-3c41-9ada-94049bfa2bd9 | -18.36881 | -43.96209 | 2024-09-27 04:42:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36e99bd0-1b09-31e8-9e18-4679c70e53cf | -18.2523 | -43.59417 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a078b88-6588-3e8f-b28f-489e8b873a0d | -18.25213 | -43.59415 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d467052-92c5-3651-af7d-c5b29d0fa3bc | -18.25195 | -43.59727 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a42c5e9-9f1d-3d52-b048-d9003a05b680 | -18.25179 | -43.59727 | 2024-09-27 04:42:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62f02273-31aa-385d-8cc2-792e3f810d27 | -18.05685 | -44.34839 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c261fb16-6232-3fbb-8744-b54b61b780bc | -18.05612 | -44.35448 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c363bd4-583e-39cd-b5e5-67ce6cf0251b | -18.0536 | -44.34249 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7cbd3e2-628b-3251-a2e5-597fe3fc2d35 | -18.05278 | -44.34198 | 2024-09-27 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README101.md)
