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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e00cf30-f294-3bc6-881b-bbb7b4105043 | -18.3308 | -43.23912 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e07f7953-9920-3058-b897-637b3d75dcf7 | -18.32737 | -43.23839 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| bde01dfe-db0d-3412-9172-3cd29ecf5023 | -18.32673 | -43.24215 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 82d1f3cb-e7c9-3f48-809e-f294168ec078 | -18.32541 | -43.24988 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c5dc52d3-91a1-3e48-85d1-f508455ebfeb | -18.32395 | -43.23764 | 2024-10-02 03:55:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3f4d3089-6af8-376f-abaa-1051e4f9ed69 | -18.3233 | -43.24146 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 57c267d0-49f9-3c9a-b5c0-4020dc0e81b2 | -18.32197 | -43.24926 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d79e63bc-6246-3223-a5e4-7f2d3997aa23 | -19.77125 | -43.94438 | 2024-10-02 03:55:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b0b99f6-36bd-3d6b-8e05-af365221bcc9 | -19.74376 | -44.2519 | 2024-10-02 03:55:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4d5501b-6bf1-3bfa-aa0e-da78fb735dff | -19.62303 | -44.10872 | 2024-10-02 03:55:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07fce06a-a345-3855-bdda-11057679f352 | -19.62162 | -44.11687 | 2024-10-02 03:55:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62cfe886-a185-343e-81a8-32904c0c8505 | -19.61953 | -44.10802 | 2024-10-02 03:55:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b03a98ce-ea2d-3303-8e76-78871ce85bee | -19.61882 | -44.11209 | 2024-10-02 03:55:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fddfd5e7-a127-363e-ac63-951df757f12a | -19.61602 | -44.10733 | 2024-10-02 03:55:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf7a30d5-8206-32bd-9f03-1188d4c17c49 | -19.6125 | -44.10666 | 2024-10-02 03:55:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d551f7c-9a42-35e8-b10f-95a8a441ae95 | -19.61036 | -44.119 | 2024-10-02 03:55:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ec1a9e6-d5a3-331f-b276-ffb68ee5cd48 | -19.60684 | -44.11836 | 2024-10-02 03:55:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b731976-d162-3093-85b6-b677d30e0243 | -19.51164 | -44.12323 | 2024-10-02 03:55:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fb79170-30a2-3b9d-ad8a-ea4121f56ed9 | -20.05887 | -43.76571 | 2024-10-02 03:55:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b57f419e-c9d7-32d5-bb14-3d6e42d47198 | -20.05819 | -43.76973 | 2024-10-02 03:55:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 188e9c21-58b7-3c94-8853-ad53a967b685 | -20.01901 | -44.52878 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fdcd5497-fdf9-3c5e-8675-0176257d6099 | -20.01471 | -44.53233 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc923946-1365-3e47-aa8d-baaedbcedf0f | -20.01338 | -44.51883 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f65c4c6d-97d8-3314-8e5d-8fb19c818d42 | -20.01265 | -44.52305 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| aa81b393-6d9b-305d-b398-c0b9c3250e8b | -20.00984 | -44.51804 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c8565934-1a76-3f98-bbd3-bd6d53e90d08 | -20.0091 | -44.52226 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2052fe92-4e72-337b-85ce-93441c71f762 | -20.0089 | -44.54455 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dad773d6-3773-3d0f-be9f-12a80beba0c5 | -20.00629 | -44.51727 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c267c63f-bdb4-3abb-9541-8edd8611fb5e | -20.00555 | -44.52149 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 827f74ef-71c3-3600-abad-5e94e6b0c3e6 | -20.00535 | -44.5438 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e749a4c2-1712-31f6-a023-46530063d813 | -20.00484 | -44.10556 | 2024-10-02 03:55:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 69af9b54-406e-3ee5-99d5-9a3f42b2f175 | -20.00199 | -44.52082 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| dce97302-ab4b-39ab-9e6f-fbab6dc1c2d4 | -20.00124 | -44.52514 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d7224a66-4a23-3d42-9759-0b094a25e153 | -20.00048 | -44.52947 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e590e5fb-132e-393b-9a9a-97cb27d64fa0 | -19.99973 | -44.5338 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 695220f9-9ea5-386f-be2a-842bf7364bbf | -19.9969 | -44.5289 | 2024-10-02 03:55:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 27e43a52-a99c-3333-b73c-15ebf5136f9f | -19.85256 | -43.89571 | 2024-10-02 03:55:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3314a09c-2e9b-3b5a-a558-38ee3e8b6948 | -19.79493 | -43.63892 | 2024-10-02 03:55:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77cdb405-b397-3c6d-a412-c32ac7b74302 | -19.79353 | -43.64711 | 2024-10-02 03:55:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400a05cc-e937-3fd2-9493-52be4b89943a | -19.99133 | -43.54054 | 2024-10-02 03:55:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bc9b9672-99db-3b77-8205-015f6f8e46d7 | -19.99004 | -43.54818 | 2024-10-02 03:55:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80549f79-bab5-3398-adac-ae68e7219520 | -19.86722 | -43.50531 | 2024-10-02 03:55:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 815de062-f5df-35cd-81a6-3018edd56145 | -20.89963 | -43.8201 | 2024-10-02 03:55:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4e61d04-8d53-35ea-95af-099e220b1398 | -20.81464 | -43.67804 | 2024-10-02 03:55:00 | NOAA-20 | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c866ab7f-1e30-3574-bf4c-a5d874cbf61c | -20.50965 | -44.02275 | 2024-10-02 03:55:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc9abc8a-edc4-3f68-869f-f38ff996be25 | -20.29959 | -44.03963 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75c26ab1-9411-37c8-998a-94039f8107ab | -20.29684 | -44.03474 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1f06adce-154b-3de5-ade7-f3cfd50f19f7 | -20.29337 | -44.03404 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 777d675c-2a7f-3f91-9188-db98bda4a291 | -20.29265 | -44.03823 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 78f11370-d1b4-31a5-a7aa-8dabfd55ce4a | -20.23317 | -44.23583 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5549ea95-0d6e-32bd-8b53-f94640a0f9df | -20.22966 | -44.23515 | 2024-10-02 03:55:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e2697bf4-bc4d-3d0a-91f6-e026672252fb | -21.5643 | -43.96369 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e2baaf1-e018-3b0e-978c-52581062c598 | -21.56372 | -43.96174 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cf2e4cb5-064c-389a-90e5-76adc73efd2f | -21.56303 | -43.96575 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0f57af9c-84db-3183-8745-65fc04477530 | -21.56155 | -43.959 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ae648de-2eef-390d-94e0-cab5a61cff1a | -21.55813 | -43.95828 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| de8635fb-ddf6-316c-b970-10f94c52b2c8 | -21.54992 | -43.96498 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 01d67092-f023-3446-87b6-8e7c07776a92 | -21.46667 | -44.58123 | 2024-10-02 03:55:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| f0354824-d209-32e9-a593-1d35229cb068 | -21.46317 | -44.58047 | 2024-10-02 03:55:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2be9ca3f-a4a0-3d14-ad44-053defd2629c | -21.18152 | -44.27319 | 2024-10-02 03:55:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30c182ab-60ae-390c-b9d4-f7c60a681354 | -20.97268 | -44.41343 | 2024-10-02 03:55:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cddc6634-276d-3e8a-893d-8344872df3a9 | -14.85786 | -45.10912 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d2583e9-721e-3521-844a-92039bfb6567 | -14.84267 | -45.19342 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e58c1a80-3148-3e06-b928-e833824a3e09 | -14.56814 | -44.83595 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e7708cc5-979e-3835-aa6a-393c44309dc5 | -14.56792 | -44.81476 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95d51e45-7e55-352f-a1f1-4c6977a7c048 | -14.56722 | -44.84108 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 896ffcf4-eb38-3315-aae4-073e6dc62f52 | -14.567 | -44.81985 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45f89f77-dfd7-3dd6-9744-c435a064e5ec | -14.56517 | -44.83007 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86e1933d-5c2b-3ed4-94e6-78d5875757a3 | -14.56424 | -44.83519 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9ad39e6a-d356-3a10-968c-123a53976f4c | -14.56332 | -44.84032 | 2024-10-02 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 07390731-3093-39e1-a9ba-c19a4125d352 | -13.71117 | -44.66792 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83d3edb8-3fd3-3593-8abb-dc8cc627043a | -13.71045 | -44.67012 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd74db99-3888-3bb4-84d5-445449646867 | -13.71029 | -44.67302 | 2024-10-02 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a820cca7-0b1e-3857-8daa-b129487c2e5a | -15.76461 | -44.65464 | 2024-10-02 03:55:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 843cf9d3-7a5e-3ae4-ba98-758238bfd0c8 | -17.96013 | -45.69482 | 2024-10-02 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e0bcd867-058e-31b7-839e-af01db3a9d19 | -17.5582 | -45.00386 | 2024-10-02 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80c274b2-d7dc-34dd-876d-ddcbcfb28da7 | -17.55443 | -45.00312 | 2024-10-02 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69c1ca0f-c13a-3ad8-9fc4-f45275608868 | -17.38191 | -44.85553 | 2024-10-02 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a47fbea1-8e91-32e5-b86e-180bb74b1f47 | -17.37906 | -44.85274 | 2024-10-02 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fbe1991-2d13-31b6-8193-7ed1551491ca | -17.37817 | -44.85472 | 2024-10-02 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 129ffa3c-9bdb-3e5a-a357-b64618434fc4 | -19.51004 | -45.07622 | 2024-10-02 03:55:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf61a7d-1d6a-3a2d-9f4e-5acad8badaca | -19.39467 | -46.39946 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a1b1dc2-ab2d-3581-b003-ee098b2d7961 | -19.39235 | -46.40044 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f10a0c8f-7fc6-383c-a206-a64d429d3c70 | -19.39071 | -46.39863 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a31834-de79-3ba0-bb6c-af71944557b2 | -19.38839 | -46.39962 | 2024-10-02 03:55:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5285f3e-6ecb-377e-b7a7-359813f11a72 | -18.91935 | -46.07867 | 2024-10-02 03:55:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ba54325-00c6-3295-b3d5-edae13fc8e99 | -20.98784 | -45.57516 | 2024-10-02 03:55:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf472c6c-9d92-39e4-be34-e2c557e4f431 | -20.31207 | -45.58475 | 2024-10-02 03:55:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d7dfd07-3937-394e-8ec2-8b7c80aa882c | -20.86476 | -45.25735 | 2024-10-02 03:55:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d3154728-15f5-3abd-a77a-380b4853558f | -20.86193 | -45.25203 | 2024-10-02 03:55:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d0974d25-116d-34da-8f3b-cf1a2b042a81 | -20.36827 | -45.36028 | 2024-10-02 03:55:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0df882a3-10f1-35bf-b8cb-8c719da7a6a4 | -20.53214 | -46.27292 | 2024-10-02 03:55:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0f83c73-d54c-3ba9-9ca9-117642cc54c7 | -20.52926 | -46.26684 | 2024-10-02 03:55:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92f11bf4-45a3-3f46-a38a-12806d94d2b5 | -20.52829 | -46.27205 | 2024-10-02 03:55:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e818ace-d4d1-38f9-a2b2-7116b9095a23 | -20.52729 | -46.27742 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 481678a7-1e45-3e60-bea2-dfc06228421b | -20.52631 | -46.2827 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95c804ec-fdc7-36a6-a637-c9536fa6a062 | -20.52537 | -46.26623 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65da6523-acea-3050-94b1-fbb3022b1297 | -20.52443 | -46.31439 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10c094a3-c121-3fc2-91ff-481abdf169c9 | -20.5244 | -46.27141 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 81a5414e-18d7-392c-a18f-08789d49d39f | -20.52353 | -46.31922 | 2024-10-02 03:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README71.md)
