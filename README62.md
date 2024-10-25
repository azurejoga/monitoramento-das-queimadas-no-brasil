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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbbbe127-0963-3ef1-abf0-9a668e5935f6 | -2.66426 | -49.39857 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c217d91c-3b0a-342d-8f80-d651798cc3b6 | -2.6597 | -49.27604 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee5bece7-aae3-360c-8ce5-0b91eedd6a79 | -2.64085 | -49.39491 | 2024-10-25 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7460ccb2-58f2-3d13-accd-119ae67cc1d6 | -2.64077 | -49.24448 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 458b7ec7-fd5f-30f2-b4e5-a7463a1222ca | -2.64021 | -49.24797 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3aa6115-ca36-3615-9136-3fa100fa3211 | -2.63933 | -49.24031 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4584ab6-8567-3043-af1c-2c466b55b19a | -2.63878 | -49.2438 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ec6b21f2-5252-3261-a38a-6f42edbf7999 | -2.63823 | -49.24729 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| abea2b3c-ebcf-3757-87fe-13f1c9c08396 | -2.63599 | -49.2398 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d42ed76c-9b80-3369-b687-9a7a58a298e3 | -2.63544 | -49.24328 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 641bc691-3a82-3012-a444-aa54b5114a09 | -2.63489 | -49.24677 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ec8080d7-9dcc-31d8-8d70-27ecc7534c4c | -2.63156 | -49.24625 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0bb43f0-de47-3e05-be62-861bc4e090b9 | -2.62458 | -49.0954 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7034069c-ff0c-3283-854a-74c9243153a6 | -2.62403 | -49.09888 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d880d1-6a92-388a-980b-30fb329e9191 | -2.61404 | -49.09732 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 569940f5-e237-3bce-a0d0-f3556635afc9 | -2.61126 | -49.09332 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964593e3-0480-3918-be9f-b64d5d009e7b | -2.60793 | -49.0928 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab027e08-71ae-3ad1-89be-5f932242fd2c | -2.23365 | -50.31107 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 705ca512-3601-33cf-b791-d6946d1f3262 | -2.23022 | -50.31053 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4df0b760-f5c3-3eaa-bb6f-e5a062e9e4f9 | -2.9698 | -50.42393 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d20e936c-f20b-3878-b651-1fd5ea8937fc | -2.96922 | -50.42763 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4347f839-7e11-3446-aed8-64b897039f5d | -2.96812 | -50.41233 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e620137b-0980-3034-9b36-537e399ef0f8 | -2.96637 | -50.42339 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0fb6e97-33a6-3835-974a-0ff599955229 | -2.96295 | -50.42286 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f91bbecd-9f8c-3981-acf6-f5ec29cb69ab | -2.96178 | -50.43025 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08346791-75c9-3e20-bd48-1829d7e88275 | -2.96086 | -50.5252 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd4395b-b6eb-3713-bd9a-10d2cfbf01b3 | -2.96027 | -50.52892 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d03662b3-0fe4-3007-a0f5-0e4b3c77e4a6 | -2.95918 | -50.5135 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da334cb-bcaf-3913-900a-2d2bb2fdf1a9 | -2.95801 | -50.52093 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 178b950b-2f99-3718-92aa-11e5b13bad96 | -2.95683 | -50.52838 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e1d8e4-9761-3978-a760-8ffd7131c873 | -2.95536 | -49.54804 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1e5732b-ec9b-31fc-9f01-96135446f26e | -2.95515 | -50.51668 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7385cef-b051-3180-ad92-3632fce40b8e | -2.95054 | -50.52357 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fa6db6f-8ac5-32c3-9881-8000d79ad974 | -2.94995 | -50.52729 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a82967a-7ec8-30e7-a0cd-1e64903b101b | -2.92893 | -50.4821 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 517873f9-bb9b-3a0d-8df2-5ce37a6480eb | -2.8996 | -50.40154 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 676d1b4d-7756-3eb8-87d1-11bcc70ac5f3 | -2.89901 | -50.40524 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac151b7-7a6e-3768-90e2-e5668dc795f3 | -2.89558 | -50.4047 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f2bd610-2b25-3776-bd4d-9acd18fbef79 | -2.88719 | -50.41857 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b7aa6bf-04bf-35e5-a63c-1830615a7632 | -2.88635 | -50.41839 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f43d1ff-4fb4-3b79-a306-19db95275b88 | -2.80808 | -49.61898 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11fa80f5-f806-35c2-89f6-fefe52a19f6c | -2.80751 | -49.62251 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6942921a-8b38-375d-923f-bd6855c15b87 | -2.78246 | -49.48888 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245512e0-a16f-3f74-859a-2f50780a0b7e | -2.78191 | -49.49239 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4295be0b-86e6-3de6-89ad-480c22c82316 | -2.77967 | -49.48484 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4c4665-009a-3182-bab7-b300d58faa39 | -2.76427 | -49.95883 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a869f2ab-3784-39e0-ab91-d0e608bc95da | -2.74566 | -49.7657 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52634fe3-523f-34c0-8485-f17b83d628fb | -2.73666 | -49.8008 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc401e21-4c32-3dad-b0c4-e7a94c4b76d9 | -2.68716 | -49.82961 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09a864c6-1bcd-3999-9782-b91ba95c9a3e | -2.65708 | -49.50901 | 2024-10-25 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8a1fb1f4-1a00-3089-b275-0ee9c6592b3a | -2.65508 | -49.83557 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19a17476-0b95-327c-91ae-3441592cb78a | -2.65441 | -49.83202 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22dc4c40-c08f-34f8-9e95-6f54565a339c | -2.65385 | -49.8356 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9001583d-f83e-367a-9a86-ab9620d3bec3 | -2.64452 | -49.98841 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ece0237-1195-30f1-82ed-e5f33ebb0993 | -2.64113 | -49.98788 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84080b19-fb86-32bc-916f-655503f8e4de | -2.63154 | -49.98268 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48c0daad-f54b-3e4c-a459-e768fc873948 | -2.63073 | -49.98286 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab245a3-e0ac-3c30-9c55-1a28e796119b | -2.62734 | -49.98233 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b287618-1bc4-3c99-8cb5-5d65f9da3292 | -2.62677 | -49.98594 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40599c5-ea53-3334-a611-0beec053ef40 | -2.62405 | -49.78334 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 69e138de-c48b-3140-bfc0-7e5d6d9fb28f | -2.62395 | -49.9818 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3652286-7dc8-3294-9d7a-e8e6c9658d89 | -2.62068 | -49.78281 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a949d83-779f-3674-9463-f2df7356055b | -2.58529 | -49.7663 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3220962-a5c9-3e24-8e14-9287f27347a6 | -2.58192 | -49.76577 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e39d662-b79b-39d7-9f99-7cb6a5bf7f15 | -2.57798 | -49.76881 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b9fa133-db37-3ef4-9bac-29904bfe33c5 | -2.56726 | -49.79271 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a66cada2-c72a-3c7e-85be-b558de622cfd | -2.4473 | -50.3738 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adce442f-b178-38f9-8c0e-687e212edfbd | -2.44672 | -50.37751 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54b847d3-df0a-3e3b-af35-06ea32a9d332 | -2.43897 | -50.29281 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d9084d1-73e1-3d0b-98b5-d0b48f045eee | -2.43839 | -50.29649 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4490844e-f54a-3daf-8e97-cb260b42ca81 | -2.42184 | -50.29016 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6f6d960-795b-3476-adba-528bbb82bed5 | -2.42118 | -49.69679 | 2024-10-25 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d462b01-12de-353a-9e08-eb339ab5941a | -2.41737 | -50.40724 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edeffa68-0440-3aa1-aa91-81ac2ae47a83 | -2.41721 | -49.80957 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65de1f94-1132-380b-9aca-4f1c3fcea752 | -2.41393 | -50.40669 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc094d1-7069-36e8-9226-05519f4e2c22 | -2.41327 | -49.81262 | 2024-10-25 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb098cd8-be4d-3315-96e2-cc3e7de66c02 | -2.41175 | -50.24326 | 2024-10-25 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57d56e58-d3f9-3821-b3d2-229e72ed5813 | -2.40931 | -50.4136 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12ff6d62-03f7-37f0-812c-701ab219b379 | -2.40872 | -50.4173 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acef70f8-a576-31bc-8685-f3cbddc401db | -2.40587 | -50.41306 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bc4b830-d195-3334-bb63-446a7d11ed2e | -2.57156 | -48.93801 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e5a6a9-0f84-349c-86bd-7178f7a0322d | -2.55376 | -49.30563 | 2024-10-25 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f43a4af8-200a-3267-adda-242b4bbe15cc | -2.54581 | -49.05829 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504d9d1d-4ccb-3302-b75e-73db54ed6663 | -2.49822 | -49.12205 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ef04181-7bd8-3980-a256-c8f77f1b367b | -2.49434 | -49.125 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b5075bd-4da2-314a-bcfc-d01fcea1d9d9 | -2.4914 | -49.03557 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77353bfb-182f-3441-8a2b-f1c5c9a9eb74 | -2.47654 | -49.10798 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44a50da6-a7b0-39a6-be57-9ae9f714bd6b | -2.47431 | -49.1005 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b0d419-6894-3a85-886e-5c1c103c0a0f | -2.47376 | -49.10398 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7043f87-537e-3259-96b1-935694750cf1 | -2.47321 | -49.10746 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 116c90dd-7824-360f-9a05-da0682bf392e | -2.47098 | -49.09998 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b12aa92b-4e6e-3073-9f05-b4a00d553286 | -2.47043 | -49.10346 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 06877559-c690-3a33-ab97-eb6feae65063 | -2.4671 | -49.10294 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a1780f1-9fa6-3999-85bb-e930290ae89b | -2.38982 | -49.38447 | 2024-10-25 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2513286-8843-3d4d-aa06-68e20c8917df | -2.37522 | -48.95724 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98d7d376-facc-3e44-8809-df5cc05e5a7c | -2.35859 | -48.93689 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8121fc2-9271-3c81-8ecf-e9f63973a5bf | -2.35581 | -48.9329 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10c16da8-0c68-3090-a5b0-887df916c963 | -2.35527 | -48.93637 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63f0eef6-ea2f-3403-8a7b-9097d39b4adc | -5.00218 | -49.78696 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f20a149-3f2f-3436-be17-36b225de4825 | -5.00163 | -49.79046 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README63.md)
