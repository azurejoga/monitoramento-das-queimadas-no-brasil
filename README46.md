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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa4f2113-1c4c-329e-9f0e-ea43fc1ae1f7 | -19.90046 | -44.95263 | 2024-10-07 03:38:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8092fbf1-9cff-3379-8c9a-661242ab5453 | -19.86525 | -44.09932 | 2024-10-07 03:38:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82cf567e-a589-33d5-8c1b-b8d60529f328 | -19.8617 | -44.09299 | 2024-10-07 03:38:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7bf8847-6965-32a9-a949-39cd10c7f862 | -19.86067 | -44.09816 | 2024-10-07 03:38:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a258aa4b-139f-3c71-b31f-0c909b0d5025 | -19.82327 | -43.7879 | 2024-10-07 03:38:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69b22198-af0d-3faa-a1b7-444be03d603b | -19.82221 | -43.7933 | 2024-10-07 03:38:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93015baf-640a-3639-aa06-5bdcee86eefa | -19.81869 | -43.7872 | 2024-10-07 03:38:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05d41063-74eb-3d72-b07f-90cfeffd3d82 | -19.94198 | -44.09208 | 2024-10-07 03:38:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a278714-5d80-3b00-aa16-b282a06fc95d | -19.91791 | -44.50337 | 2024-10-07 03:38:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91341c24-d61d-3d3a-86ee-af0da27b0416 | -20.34493 | -44.68451 | 2024-10-07 03:38:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04f8f8e0-4d13-36b2-86aa-28b8aba03559 | -20.34381 | -44.68991 | 2024-10-07 03:38:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6ff1ae5-6978-3550-b0f6-8bc8a636a95f | -20.34019 | -44.68348 | 2024-10-07 03:38:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9cbb7087-601b-3109-a8a6-e4aa7d72b4d1 | -20.33905 | -44.68897 | 2024-10-07 03:38:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c45ca3d3-de76-3c65-9cb1-5968d002ea03 | -20.72213 | -43.83262 | 2024-10-07 03:38:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75d96182-4174-3e85-9a9b-ff79761ccc89 | -20.72136 | -43.82936 | 2024-10-07 03:38:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 266e1be0-9690-3f19-8e23-ae4916911f89 | -20.72045 | -43.83403 | 2024-10-07 03:38:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d614d48-e0ab-38c3-936e-be362c6b098c | -20.66747 | -44.03285 | 2024-10-07 03:38:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1736714e-b5e4-39a3-8dc3-2a530cd6ab1c | -20.66674 | -44.03588 | 2024-10-07 03:38:00 | NPP-375D | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe77cbc3-dd2a-3a4c-b2c4-b56a54b2aa5e | -20.62564 | -43.98248 | 2024-10-07 03:38:00 | NPP-375D | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fbea8be1-a161-340f-bcf5-891a69691a17 | -20.48767 | -43.65281 | 2024-10-07 03:38:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59e1cdbd-f881-3f26-9968-0cd7a3cae70f | -20.42186 | -43.75056 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c39ed614-d008-35cd-9bc5-3d3b9f9cca26 | -20.41734 | -43.74988 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5548092f-55aa-3582-9976-384284b5adde | -20.41646 | -43.75426 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d0f5d95b-b94a-3257-86e6-4d7141b8d74b | -20.39298 | -43.91726 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6fdb4ae6-0d54-3531-83b1-896a7d121abe | -20.39212 | -43.92151 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51f16f1d-0de6-3825-a7e2-a8d94396cc1b | -20.38846 | -43.91633 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 93c49f42-c21b-3347-89e8-f1ce45c54a8e | -20.38381 | -43.88891 | 2024-10-07 03:38:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a01008b5-d9de-3141-9101-a1bb63f0dfa8 | -20.30161 | -43.61224 | 2024-10-07 03:38:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| baa6b3d9-12e9-385c-b329-5e47ebd9fa4c | -20.13855 | -43.86497 | 2024-10-07 03:38:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a17a0235-463c-360a-b4c4-b077200644a1 | -20.13498 | -43.85919 | 2024-10-07 03:38:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4f0b7af5-f28b-3c6b-9882-a9aaa9a8efa3 | -20.13395 | -43.86445 | 2024-10-07 03:38:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 80b462e5-e590-3607-b252-3b557e8e7531 | -20.10195 | -44.22034 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 469c1baa-5fff-31f3-8ee1-35c72c545b50 | -20.10047 | -44.21696 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e7d1e54-f95a-313f-bf01-bdd470e099a4 | -20.0995 | -44.22173 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 173e9b49-9d97-39e0-b0df-ad838cfe40c8 | -20.09723 | -44.21981 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 935538e8-e8d4-377b-9284-0220d36c6ada | -13.84396 | -44.63052 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fba3b0c4-beaa-39fc-a71f-16cc2676fc5f | -13.47269 | -44.50117 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee3fec83-14bb-3bff-a31d-c48b8dbba235 | -14.6865 | -45.13865 | 2024-10-07 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ce75bb2-4cf5-386b-8527-ffed7371204c | -14.68581 | -45.14211 | 2024-10-07 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3faacca8-feb1-3849-8c8b-5c06ee08d442 | -14.67717 | -45.12866 | 2024-10-07 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7079b780-bc05-3872-830e-52e8f8387603 | -14.67648 | -45.13213 | 2024-10-07 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13ca6617-1f58-3fea-b0ca-0e9b3021f904 | -13.85866 | -44.5944 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f32b1df-1128-3292-92a3-52320bc86458 | -13.85331 | -44.59342 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2166652e-4a71-3285-b038-cfc5069ba0d5 | -13.85262 | -44.59686 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622a1769-dc1d-3a52-a652-c7ac352cf86f | -13.85071 | -44.59552 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f11cbd2e-21c1-39dd-bbe4-d65cb9e5a1f4 | -13.85005 | -44.59896 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bb6e5c2-7745-3754-844f-4a3462fb43ff | -13.84726 | -44.59594 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ed143b07-6602-3b8c-9b96-f897dd602c61 | -13.84561 | -44.63185 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73af61e8-df20-3f6e-93c9-37acc7209d36 | -13.8433 | -44.63398 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c8f09306-614e-3bce-99b8-d7830ba2eee5 | -13.84263 | -44.63743 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 28b69767-7ad7-3360-818d-828742b8d07b | -13.84027 | -44.63075 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7ee338a1-9cc2-3b9b-a4bb-4ec8296a37a5 | -13.83958 | -44.63422 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e380a23-65fa-34b6-9962-2b3228d2dd35 | -13.83795 | -44.63288 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e8eae4ad-79ce-3195-b37b-d6f85f50f3b1 | -13.83216 | -44.64347 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ed2ab1c-99f2-374c-b220-fe7d91c513d2 | -13.83126 | -44.63876 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b61fef8-d3f5-37ba-af18-1b21b1f0dcb6 | -13.8306 | -44.64218 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e439d1d9-3c08-3da2-b3d7-a403a00434ac | -13.83003 | -44.61644 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb91bbbf-5085-3c6e-85aa-11ef31d04c2a | -13.82994 | -44.64559 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc1d6c3c-171a-33ad-882c-00a22eea55cc | -13.82934 | -44.61999 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 642ad7d0-faae-334c-80c0-3f1e5fd69f9b | -13.82681 | -44.64239 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0324b64-1d36-3ecc-bb37-9d253011915a | -13.82642 | -44.61673 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b2bfae-df85-309b-9192-c370086b4b38 | -13.82571 | -44.62026 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4f026e4-66a6-3583-9135-02e2d6943b30 | -13.82525 | -44.64109 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ace571c-eed6-3bdb-9f65-ec90eb7b90c9 | -13.825 | -44.6238 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f959e41b-dae5-333b-b190-ba55186dd770 | -13.82428 | -44.62732 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e588ed0-4327-362e-9ed0-e035bab258bb | -13.82333 | -44.62235 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdef4f61-1bbe-3460-a7a0-92474c7b4b26 | -13.82264 | -44.6259 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0dbd248-a7d6-3781-bf3b-5fb4e0b8dd22 | -13.82214 | -44.63793 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f8fa8c-4a7c-33da-840c-6b0d2b35d988 | -13.82195 | -44.62945 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9f62d37-793c-30af-aab4-3c9fca92978e | -13.82126 | -44.63301 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5493ef6-c97a-3682-bc87-7170035d2350 | -13.82057 | -44.63657 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fce2b1a9-22a6-39e0-912e-a4869f4f3e98 | -13.8199 | -44.64001 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3c6158a-abcd-3b70-9ad8-efee9df58a5a | -19.1999 | -45.01497 | 2024-10-07 03:38:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4418f30f-e043-397f-a35a-949e7d1f203a | -19.0169 | -45.52706 | 2024-10-07 03:38:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46c297a7-d4e7-3b1d-abe4-f9b380911a11 | -19.01624 | -45.53022 | 2024-10-07 03:38:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5db04a4-f8d7-380f-bd73-b592bd8f6995 | -19.86984 | -46.46655 | 2024-10-07 03:38:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d676596-0c74-332b-8c3c-34242d215fc7 | -19.86518 | -46.46216 | 2024-10-07 03:38:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2934d787-b530-3897-a289-dd1872ee985b | -19.76219 | -45.32001 | 2024-10-07 03:38:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e19150a-4720-346c-aa0d-e6b7f83b634f | -19.76207 | -45.32639 | 2024-10-07 03:38:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba1b424d-83c4-38c0-ad8a-c5ad59aab14d | -19.76088 | -45.32622 | 2024-10-07 03:38:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7f924b3-f284-343a-8a5e-ca5d4b055655 | -19.75844 | -45.31306 | 2024-10-07 03:38:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 238eceb9-c74d-3237-b8d7-ceeded7693a6 | -20.59959 | -46.00484 | 2024-10-07 03:38:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1610950-60e8-34b0-9eec-54de1283fba4 | -20.59827 | -46.0042 | 2024-10-07 03:38:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e84c5fe0-e162-3f43-aba6-11dd3db3a74c | -20.5976 | -46.0074 | 2024-10-07 03:38:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc1a7b1a-e6b9-3c4c-ab27-ef6b6071047e | -13.23377 | -45.58097 | 2024-10-07 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 273d391c-e8a2-3e15-984b-d09600b71fd1 | -14.11813 | -45.5323 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 382f914c-3c67-3568-b913-0fb5bc0ebaaa | -14.11737 | -45.53603 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08de82bc-a7eb-32c1-963b-3196f421d989 | -14.1166 | -45.53981 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb6b255a-079f-3b99-8b9d-24c2a15cb276 | -14.11333 | -45.52708 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e015d1e-49cd-380a-a347-eabe1df0b10e | -14.10931 | -45.51805 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 144acc11-16e8-36c7-885f-f0568a3d4a7b | -14.10855 | -45.5218 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bdcbbbc-6f0f-3440-927e-f3ca135d92c5 | -14.10775 | -45.5257 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2622a82-050b-3cb3-8d5c-1028add6b8c2 | -14.10375 | -45.51658 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1cc3ecf-1802-35f6-a9cb-584b6e1e01d6 | -14.08094 | -45.47312 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcbdf465-c0b5-364a-bac2-a8bd97220442 | -14.07613 | -45.46798 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1989d299-e072-3c83-b219-2fda6edd1996 | -14.07538 | -45.47174 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c3ff407-6e03-3aad-9fa2-9b417ee17c75 | -14.07132 | -45.46278 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcbb390c-5311-32e8-bbf1-24f1139530c9 | -14.06431 | -45.52718 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39717f39-3254-3aed-99f8-2dadb0c57e65 | -14.06353 | -45.53109 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d282f6a-5260-3a92-8fbd-4534542c2678 | -14.05792 | -45.52979 | 2024-10-07 03:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README47.md)
