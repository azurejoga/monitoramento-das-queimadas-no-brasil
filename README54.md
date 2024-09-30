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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5befacc9-d679-3503-9c9a-18cdf18e304b | -20.31091 | -46.6652 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5186b06-c870-3fe6-b7c8-4b6266e42ea1 | -20.31031 | -46.66974 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7d376af-c250-32a5-91c3-2b7ee44f9c87 | -20.30707 | -46.66489 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3d535e0-c92b-3393-b1c7-b977a7f487ad | -20.30643 | -46.66974 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c65d80f3-2b63-3033-9ab5-3099bbb78251 | -21.86318 | -48.37103 | 2024-09-30 04:34:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4122728a-4236-3391-953a-d0863ddace7d | -21.86259 | -48.37535 | 2024-09-30 04:34:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c89bc36-eb68-36f5-98c7-a03d36840987 | -21.86201 | -48.37965 | 2024-09-30 04:34:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 873f1269-9039-3dea-a91c-7e972a8ef7f5 | -21.85963 | -48.37042 | 2024-09-30 04:34:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23c539b7-350b-3bd7-af5a-4ffd49a17afa | -21.85904 | -48.37473 | 2024-09-30 04:34:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58b89560-b3b4-3ca0-b774-53fc0a9ada3b | -21.62597 | -47.78486 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1e5aa13-c811-35fa-b6bb-234d009f23f5 | -21.62536 | -47.78939 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7c8338a1-5047-32e1-8cf0-2b278d86f771 | -21.62476 | -47.79391 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 246e5b9e-b81c-3b89-b10e-28d9f894a1b7 | -21.62293 | -47.77979 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55879a43-9d9e-3e82-8594-d46a2778236d | -21.62232 | -47.78434 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 66120b04-8758-3458-8aad-93eb504ba956 | -21.62171 | -47.78889 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac5355bd-b120-31d8-9585-6ac6d73a8b5e | -21.6211 | -47.7934 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3a86957-7075-3713-a092-f41c589b9663 | -21.6205 | -47.7979 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3785aeff-2e51-32e3-91c2-f2fc048a6986 | -21.6199 | -47.8024 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8e43f72-736a-3f8c-88bf-70edf1b43ab4 | -21.6193 | -47.8069 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc70b7f-9335-3d54-b01d-a2a02ea07dc4 | -21.61928 | -47.77925 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655c347f-a1c4-37ef-ad05-1e3812ebfa12 | -21.61746 | -47.79285 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7462d8ef-c58e-3879-b771-85a89c896a4e | -21.61686 | -47.79735 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c8cb1b3-561d-38c3-abfe-15ea9b7b2596 | -21.61625 | -47.80185 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c940afa-abbc-3530-b353-5f0a71cfc24a | -21.61565 | -47.80634 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f79c655d-5fdc-361a-aabe-d653f2da1f62 | -21.61562 | -47.77874 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9ea3b40-07c7-31c9-97b5-93fdfa5d190d | -21.61505 | -47.81084 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ab25798f-41b3-357b-af15-5ba5795844ea | -21.61502 | -47.78326 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41dd2b34-dbf0-3193-a60b-c76f1e637214 | -21.61381 | -47.79229 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b33fbcb-fd5c-32d3-a01e-b82e2539dadf | -21.61376 | -47.73677 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e129fc-d181-342f-a341-33e9116d8321 | -21.61321 | -47.79679 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa8289be-bda3-3e82-ab9d-ee3e5fb4b296 | -21.61261 | -47.80129 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ef66b98-0e3a-3756-b9eb-a01e60a4f48e | -21.61201 | -47.80579 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8740aef5-9e28-3244-a3f0-ad954b0891dd | -21.6114 | -47.81031 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d7b7a769-b386-344c-ac9e-7722069e487d | -21.61077 | -47.78722 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7a44bc6-8a36-3611-af63-5f98c9633a31 | -21.61071 | -47.73167 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38fec7e1-edbc-3985-918c-c5a889fb28fb | -21.61017 | -47.79172 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acd6efbe-4e8b-38bb-b43f-d980e501fd87 | -21.6101 | -47.73625 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 329afb75-fa9c-3430-b86d-edee3bda9d98 | -21.60896 | -47.80074 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a0169a8-e810-30b4-950d-5b141f339da5 | -21.60836 | -47.80527 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9298dd3a-c809-362a-9155-f84a2a879d6f | -21.6071 | -47.73352 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2135cf57-96a3-38f0-8660-0cba97c6ed10 | -21.60644 | -47.73574 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fedca39-d1d3-375f-9e63-ef20e29f2f30 | -21.60282 | -47.73754 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e393e51-8db7-3680-8a0f-39fbe895291a | -21.60278 | -47.73523 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a21be1b-4c32-3805-a323-be040554ee7d | -21.5955 | -47.73648 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efeb6297-79a0-3de7-b2b7-8ca02625ef22 | -21.59184 | -47.73598 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe9cccf-02b3-3cac-a52c-929ecafe95be | -21.59122 | -47.74046 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a84c3509-2044-3afe-88de-032a34501523 | -21.59061 | -47.74494 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 197d1303-a4a2-3798-8144-f7cd3aeb7686 | -21.58999 | -47.74942 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5299a78a-6323-396f-9b9a-50ddf4241752 | -21.58938 | -47.75389 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eac66b6-3bca-39f9-a97d-54377f189d8d | -21.58818 | -47.73546 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b79a956-1cc3-3de8-aadf-116e0683cb63 | -21.58573 | -47.75334 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b297f66c-d136-38e6-9f52-58305b8485fc | -21.58511 | -47.75783 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa7ed624-91b0-3dbb-8e33-a4f4844482dd | -21.58441 | -47.78998 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3865c5e7-9300-35e4-8012-f9b18f6b329a | -21.58379 | -47.79453 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24fea181-6478-3e77-86bc-961c2a246b40 | -21.57045 | -47.78324 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 029f3f7f-1084-3a72-a4ca-84b79bcda16c | -21.5668 | -47.78272 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6a0b44-d56c-378c-9aee-abb97aa949e9 | -21.56253 | -47.78677 | 2024-09-30 04:34:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0b5509-c536-3b9b-a007-5be978a22a5e | -21.25681 | -47.6526 | 2024-09-30 04:34:00 | NOAA-20 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 443bc0f4-9529-3678-b586-90b81e586b1f | -21.25315 | -47.65206 | 2024-09-30 04:34:00 | NOAA-20 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9f49ce-86b2-3441-ad90-5dd36bfb192d | -21.509 | -48.06927 | 2024-09-30 04:34:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6876342-dd0a-3043-bcf7-1aef6f546459 | -22.64264 | -47.61082 | 2024-09-30 04:34:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6d9f5628-0554-382c-a5ab-fb6859bd0d92 | -22.54733 | -47.4567 | 2024-09-30 04:34:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3eec2818-7cd9-35e7-8b4c-9809db39750c | -15.97072 | -47.23517 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a6c4b9-f692-35bd-9a22-72784622176d | -15.92023 | -48.32331 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80d9f16a-3a13-3bb0-96d6-4d9fa3ace9d5 | -15.71058 | -48.32138 | 2024-09-30 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c44b9f75-fbab-3ed7-8c7f-baabe61f1fba | -15.66475 | -47.30341 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62143a5d-08ac-351a-8e3f-8d20e487af31 | -15.56993 | -47.85479 | 2024-09-30 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 005ed4f1-e557-3374-86f6-80dd74f8f40f | -15.38941 | -47.43841 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e6bff04-1f01-33a8-bed9-9ad1a7ca44ef | -15.38595 | -47.43779 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3442cf07-bf1e-382c-9884-149242f1a030 | -15.38249 | -47.43718 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58ab8ed0-d335-3b1a-91c9-c36e83f13fbb | -15.37557 | -47.43586 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70b4324c-5a4a-30fe-a379-3ce6e947c7d1 | -15.37441 | -47.43246 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e43e845-0ab9-3649-ba6e-2b37f7383485 | -15.3738 | -47.43656 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 940f8283-41d9-3abe-a282-6bbb818f8029 | -15.37212 | -47.4352 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8c599bf-55e5-30e7-bc1d-458ca0e3b679 | -15.36923 | -47.44345 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cbc4725-e375-318c-88d7-b18a0590f37d | -15.36866 | -47.44733 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a7de41-4789-36d9-a5ed-51ea80d2d38d | -15.33263 | -47.49898 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4d9b70d-8b17-3cda-be6d-3080c2fab7a2 | -15.33206 | -47.50289 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44fa1226-8b7d-359c-8105-d48623c70fbd | -15.32859 | -47.50237 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 263a9fbe-3a12-3f93-aa99-ebc984b6bdeb | -15.32801 | -47.50632 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 8fe1c6ee-6c3a-3224-a11a-63a778169438 | -15.32513 | -47.50185 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9cb331e7-239a-38e1-aff0-d9b5f4db83ec | -15.32455 | -47.50579 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1d0b22d6-4c05-3858-9f47-2a09cd53b108 | -15.32166 | -47.50133 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c95954b6-6feb-3932-95a7-ea42d29e986f | -15.32108 | -47.50526 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be087947-2694-3983-84ed-50b589e861b7 | -15.3182 | -47.5008 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae356bce-4520-3a87-8383-7abda80ad7d5 | -15.31474 | -47.50027 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f4e2c67-8439-3689-934d-561ee7a5677d | -15.30565 | -47.46556 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5f80ad2-48ed-3ba0-b805-2cf580b9a5dc | -15.30378 | -47.50259 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6762176c-582b-33eb-bb49-43009f86cbb8 | -15.29409 | -47.47187 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c186c83-bc35-33ad-ba7b-ab6501873a29 | -15.29349 | -47.47601 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b055080-319b-3fd3-bb50-64a8764ef926 | -15.29229 | -47.48426 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d72dadba-ae87-37ad-a3c0-d7c611632837 | -15.29169 | -47.48836 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a5f2904-e5f2-314f-b74f-e5e9f7d396a4 | -15.29005 | -47.47526 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 943eab3e-2fdf-3140-9292-234f5728647c | -15.28767 | -47.49163 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa2dd0ee-ccb6-3db0-887c-4afd5c1cc2d4 | -15.28707 | -47.49575 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b847b17-5547-3d8f-abfc-279d14c2d3a5 | -15.2865 | -47.49966 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e731e116-0f1a-38c8-aab1-a8ae4e8883a0 | -15.28594 | -47.50354 | 2024-09-30 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9601f761-092f-394c-90f0-4382ff0bfac8 | -15.26748 | -47.91444 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 712bb07c-3184-3000-ac45-11ffd3400206 | -15.23725 | -47.57758 | 2024-09-30 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61ca6c77-8779-310e-b152-4a3f80dedb8a | -17.38063 | -48.82605 | 2024-09-30 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README55.md)
