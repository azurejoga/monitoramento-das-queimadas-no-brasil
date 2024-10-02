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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff79eef4-5803-3bc3-8e94-34fe412cb6d7 | -15.33921 | -46.74088 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8645173b-c7ed-3909-8ccd-880434c487df | -15.33542 | -46.7359 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c881e261-f7da-3fb0-a0f1-d57be432f42e | -15.33487 | -46.74019 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5df0d6b-b654-3f32-96b1-7c96d731d665 | -15.33215 | -46.72675 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5143947-450e-30be-8d8d-c5aafd751df5 | -14.15376 | -46.9786 | 2024-10-02 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c372de6-ce10-3cab-8e31-dfb4f4d27eb7 | -14.15323 | -46.9826 | 2024-10-02 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086dce9c-efea-31b4-947c-b211c5ff8551 | -14.14902 | -46.98203 | 2024-10-02 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d83d29b-61ce-3b24-a4d4-a9b176a465ab | -14.02944 | -47.9253 | 2024-10-02 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c56d1429-71f6-3370-b513-fe2f9035d43e | -13.74795 | -48.16755 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0be99bb-3301-39a7-8df2-360a01dbae49 | -13.74476 | -48.16198 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad97927a-46b7-3ec2-ab1e-72bde0264461 | -13.74411 | -48.16674 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 495303ab-0a35-3a90-8034-849f7e7427d2 | -13.74158 | -48.1563 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b40d0deb-1ace-3f5c-be08-ae55a7795e94 | -13.21245 | -48.60399 | 2024-10-02 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 623d0693-3b05-37ba-a34a-6f5a953aa946 | -13.19746 | -48.51477 | 2024-10-02 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aa91b82-fcb4-38f0-8af8-5a5a768f3c61 | -15.36978 | -51.55738 | 2024-10-02 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c33bd827-edf5-3be7-9fa2-fb7cd1d27725 | -15.36697 | -51.55313 | 2024-10-02 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4d8e1e7-4b16-326b-8bc4-49d497b0c687 | -18.52504 | -42.23556 | 2024-10-02 04:49:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 83b853fa-e546-3a6d-acbb-c26c9aa6d28d | -18.52463 | -42.23994 | 2024-10-02 04:49:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5a9d40e4-0f8f-3654-8bea-32cf62a8a48e | -18.34558 | -43.04847 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7a2b90d0-1b8d-3240-839d-f9c4c2514bdb | -18.34359 | -42.77109 | 2024-10-02 04:49:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 81d5c80a-2130-30d0-9c97-0585414742a3 | -18.33978 | -43.04803 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e35c96a6-68a5-3fb1-982b-c900d0b44394 | -18.33444 | -43.04301 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 419e825e-e572-3a25-9499-a978b011f92d | -18.32725 | -43.05664 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1f5811de-a96f-372f-a0cd-33cb9f3adb22 | -18.32687 | -43.06043 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| bb6b2f88-d3a6-3103-97dd-de7f0cf2fa03 | -18.19679 | -43.00738 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 878a0e89-0543-34c6-8642-8040d73cece9 | -18.07168 | -42.61021 | 2024-10-02 04:49:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9cb83215-086f-3344-9ac9-abb0e457eb9e | -18.06531 | -42.61413 | 2024-10-02 04:49:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 67056914-40c2-32ef-b038-591a36bb72b6 | -18.06484 | -42.61886 | 2024-10-02 04:49:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 67d00711-3ad8-352a-89c9-fb0bbf112655 | -18.05888 | -42.61862 | 2024-10-02 04:49:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1e9f8b17-3ef1-34a6-8042-2ae94cd3723d | -14.39333 | -43.27658 | 2024-10-02 04:49:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7014e6a4-ee56-3a1c-8b09-d747c338571f | -15.44668 | -43.62176 | 2024-10-02 04:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 491d4927-00f6-3d70-a10b-fbc4ebdce151 | -17.63332 | -43.25414 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d6df5ff-c6f8-3854-8fe2-e142d217411b | -17.63292 | -43.25787 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 791f5818-2526-3742-9563-5e6f10237b69 | -17.63098 | -43.25315 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f02d8c8-517f-350c-b320-2bcaf84b1d26 | -17.6306 | -43.25682 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b24f8dd-f763-3dcf-8e50-ab29e1494e42 | -17.92401 | -44.33475 | 2024-10-02 04:49:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e20a419-6b03-3776-a17d-c01c40b463fe | -17.91871 | -44.33419 | 2024-10-02 04:49:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77d20e88-3fa1-34ff-bbbf-39f21e44a654 | -18.3871 | -44.01258 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07efcf94-90eb-3b04-a46a-836e6f0edc62 | -18.3868 | -44.01563 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdfdcbd2-a6c9-36dd-8b49-0efdae93906c | -18.38647 | -44.01879 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0abd6aba-8cf5-3e23-9beb-ae4a2f4c2249 | -18.38611 | -44.02235 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b9552c7-4c19-381e-b39d-91a36c0cf461 | -18.38533 | -44.01129 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa3333aa-c797-3337-a40b-332cdb268223 | -18.38501 | -44.01421 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a653ce1-b674-3eff-94b9-00532a189fbc | -18.38469 | -44.01722 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18506379-25f7-35ab-8e4d-a6bde3b584e1 | -18.38435 | -44.02033 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa85122a-8b80-3f7c-9839-d9a87f4099b3 | -18.3819 | -44.00972 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a836119-0654-3b75-8138-c7eaddf200d7 | -18.35678 | -44.02103 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9574bb6c-7702-39e1-8785-08499d3a2df5 | -18.35579 | -44.0303 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 190fcc7c-5230-3f5b-9cf2-5360be3c2ecd | -18.35135 | -44.02038 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f13891b-17de-3427-8aca-65ddbf29041b | -18.35103 | -44.02341 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1f38132b-ab00-34c5-9abe-72a90a2854c1 | -18.3507 | -44.0265 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0ac59c25-4ab0-38bc-9764-ac11954ed795 | -18.35036 | -44.02971 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 93023e72-a4ff-30df-b291-9726b2f73998 | -18.34557 | -44.02304 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17279fd3-e33b-3637-bed1-214dc63b3d60 | -18.34524 | -44.02614 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b3c1d2b-caa5-3a34-8790-98eada115723 | -18.34491 | -44.02933 | 2024-10-02 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fb242fc-2df3-39c6-b9a3-741b3465e8a4 | -18.20812 | -43.95304 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 340654c1-d184-3567-b7e1-d2b10f83a5dd | -18.20267 | -43.95248 | 2024-10-02 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b261499f-1b2c-33de-bf4e-bdad28f5afaa | -18.33255 | -43.23426 | 2024-10-02 04:49:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 88f548e3-a21a-3be7-98b9-a4b4c6744f9d | -18.33203 | -43.23938 | 2024-10-02 04:49:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6a3ba163-2413-3247-b657-a0c0b4720d3e | -18.3262 | -43.23995 | 2024-10-02 04:49:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ce991afa-2235-3959-9654-3d0a8105b2bc | -18.32568 | -43.24508 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1820172f-0588-372b-b4c1-6b179fa009e5 | -18.32524 | -43.24946 | 2024-10-02 04:49:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2f20e985-0698-3972-b09c-2e6810abb46d | -13.11199 | -43.50206 | 2024-10-02 04:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8124c497-5449-35a8-a1cc-5ac0bb817bfa | -12.99081 | -44.72574 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f354f17-8d15-3d5a-9354-526685ede807 | -14.8587 | -45.11021 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cf24789-8743-3413-93da-ae7ba58e9968 | -14.85818 | -45.11037 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 122e7f84-2fff-33b2-ade3-ae7e398868c4 | -14.56936 | -44.83647 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24100090-0b79-3d2b-82d9-38ac23b9f5aa | -14.56818 | -44.82471 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c39c6e-f205-3643-9666-43f4d21f35f6 | -14.56678 | -44.83581 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a794e678-9c06-3fab-b62e-a2c775404a98 | -14.56609 | -44.84134 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5d52c24-d140-3ed3-8773-ad7b029e2e55 | -14.56446 | -44.83585 | 2024-10-02 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| add9878b-1998-3439-b97a-3231f7b0e3e7 | -17.96247 | -45.69455 | 2024-10-02 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b848d254-f116-3284-a2e0-a4b2080d29f8 | -17.55819 | -45.00307 | 2024-10-02 04:49:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cd2e910-916a-3053-8e40-0e6d06cc61b7 | -17.55315 | -45.00244 | 2024-10-02 04:49:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079a4775-0679-3314-ad59-e72287f182f2 | -15.90502 | -50.1395 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d867feee-8177-3a2e-b53f-cac42f155cd3 | -13.17422 | -46.30797 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6839e86d-030d-3604-bba2-c5e6259bfa17 | -13.17369 | -46.31192 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ae17080-fe4b-383f-ab36-3c3cf2e949b1 | -13.16938 | -46.31115 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ab196b3-c1fc-349c-8006-23f1fda86e68 | -13.1673 | -46.32668 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff35c45-674c-36f7-89f8-07a6586ea3a5 | -13.16675 | -46.33075 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 057cad6f-2d87-3ba2-9dd7-d40e4740f9b6 | -13.16241 | -46.33019 | 2024-10-02 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 29f07b18-d857-37b5-a0cf-926dc34326a2 | -14.65334 | -45.91853 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0a53927d-adc4-3477-ade5-c1982c066ae7 | -14.65281 | -45.91557 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa9f9ada-59f6-3dc0-b2ae-731995b55dd7 | -14.6522 | -45.92031 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c2f3e00-6c40-3029-b7e5-3c809f677c43 | -14.64879 | -45.9179 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b24a0b4-29b3-3ad0-86e8-cf0daead07ce | -14.44031 | -45.71679 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 108d05c8-8a48-3829-8dc0-1a6223d9e987 | -14.43634 | -45.71127 | 2024-10-02 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46a27ce3-d62e-3051-99b5-e865889b7481 | -15.32727 | -46.73033 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79d586ec-0a68-3e04-9b88-e3fa684e71bc | -15.32674 | -46.73456 | 2024-10-02 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1bfa0e9-ca04-3958-a8eb-3e2fafa58f87 | -18.08585 | -46.14412 | 2024-10-02 04:49:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71fcd651-5e20-3e0d-8465-09c5c6102925 | -17.97865 | -46.61859 | 2024-10-02 04:49:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc16b248-69a5-3ccd-ae1a-49c7516ee1c9 | -17.97806 | -46.62349 | 2024-10-02 04:49:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 848f31c6-4fb3-3419-8c55-388e653c3ca3 | -17.59175 | -46.95953 | 2024-10-02 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da5762ec-8a10-3c70-8a5f-fbd0b7fe43f4 | -17.48712 | -47.00975 | 2024-10-02 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18fac8e5-181b-34df-a3d5-992596840407 | -16.08557 | -50.41507 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb67f77e-351a-3f24-955f-663b031d4a35 | -12.4787 | -47.50406 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da70c6ee-54f7-392a-99fa-a56a07b899f1 | -12.47546 | -47.49828 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84cf8623-e33d-3a0b-a404-6ae666ff036e | -12.47474 | -47.50348 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22a21e99-e44b-326d-a0fe-53b62404d931 | -12.29451 | -47.64462 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b42d4269-3e8f-3ddb-82b5-673dd955b656 | -12.29381 | -47.64968 | 2024-10-02 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README95.md)
