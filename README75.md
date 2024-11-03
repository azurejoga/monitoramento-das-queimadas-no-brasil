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
| f46a3216-826f-33e5-9f9e-8266880bf9a8 | -2.29006 | -48.45625 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c08c13f0-8d9f-30eb-9364-2629430e05e4 | -2.24226 | -48.82561 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b740391-056a-3d39-aa59-63f9a2f62056 | -2.23238 | -48.5366 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7b37dc2-d6ee-3955-bada-08ebdb3c9a9c | -2.14362 | -48.54433 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f71667a-e77c-3a7e-958a-780d982ea787 | -2.11969 | -48.76296 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f67b9820-5f11-330a-943b-b324fa9654df | -2.1189 | -48.7681 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a270b8db-d659-3af8-8ce4-832cc2de671c | -2.98355 | -48.52947 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 45d1870e-1d26-3037-abcb-993c4ea17e01 | -2.98271 | -48.53505 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ebbacb18-30a7-33f0-881f-48b2ef9c1281 | -2.9786 | -48.52871 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2bcdabf0-b556-33e2-a967-ce2149992525 | -2.97776 | -48.53429 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a7e978b5-10f5-3182-ab53-3a68b482defd | -2.79809 | -48.68591 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38f53667-df2c-3908-9bdb-2928c38f37e3 | -2.7569 | -48.57817 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6e3ee88-d7c6-396c-a6a4-54cb44567eaf | -2.73638 | -48.58065 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50a60f50-4088-3141-932e-857fb57bdb0b | -2.73555 | -48.58619 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f2c8c19-aa20-35f8-9444-83983cceec6e | -2.73312 | -48.70246 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f05a99a-5dd9-32e9-8317-df06031ac4bb | -2.73232 | -48.70781 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e75e11e7-762c-3a68-8d73-04a415e47fb7 | -2.73151 | -48.71317 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14f741e0-5437-3a30-b090-657e8dd4e267 | -2.66695 | -48.39884 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea800211-9d75-38e3-aa37-57601302ff98 | -2.66611 | -48.40438 | 2024-11-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 053b864c-064f-3955-bd45-f4f75d1c336c | -2.63367 | -48.61989 | 2024-11-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03120420-a8cc-3561-ab8b-113a747587d6 | -2.23645 | -48.54279 | 2024-11-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57c95ccb-4c96-3df1-9c78-0599723f4c63 | -3.85978 | -48.25585 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95f743d8-aa1e-3759-9b9d-4e2dafb5f394 | -3.85422 | -48.25808 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3567e8e-2ce3-362b-b8e5-1a18649fbab2 | -3.84183 | -48.92154 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4b27679-8ea2-3a2c-8bee-d72598861bdf | -3.83922 | -48.92237 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09addcb4-2a76-31af-9242-8a7f5fe67424 | -3.79632 | -48.10602 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c13879b-52fb-3f28-95e0-5d1c7644fd38 | -3.79161 | -48.10212 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b9cc30c-cd33-3ec6-a188-ef97ce3c4130 | -3.79116 | -48.10519 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6b59c97-64ec-347c-bf63-d28d67d98062 | -3.65092 | -48.84772 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51363de7-4bca-38e0-be91-64ea719bb26a | -3.65011 | -48.85326 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba4f8823-d36c-32b0-83ae-77566ad78ede | -3.63985 | -48.83966 | 2024-11-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d3bb825-527d-3770-b898-d38bfd14cca4 | -4.59608 | -47.97214 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 453200dc-d23e-393d-9aaf-c4730a1c2c91 | -4.59129 | -47.96803 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6cfbcb27-02be-35b5-8621-78a68eb63294 | -4.59087 | -48.93807 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d192147-0423-3c49-8961-549580ca0acc | -4.59083 | -47.97116 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 75b2b798-dff3-3c9e-a688-5c27138c5f04 | -4.59038 | -47.97426 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61374b5f-48c4-3961-ac77-755565f9350a | -4.59024 | -48.93725 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68098b00-4745-3520-b3b8-80c57bce5da3 | -4.58603 | -47.96713 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35bdf272-47c6-3085-8ec3-cab2556485a4 | -4.58592 | -48.93735 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f736bce-441b-3e37-aeed-fdef2e77c238 | -4.58557 | -47.97024 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d7ff56-279e-3b0c-bf40-21e2190d840a | -4.44566 | -48.60269 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7583772-ddca-3f22-9ca7-8a2fe3d854a8 | -4.44524 | -48.60563 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dc6557d-c419-3285-993a-ec89d42a7cec | -4.43248 | -48.47836 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7f3fb83-dd73-3449-a48b-f64ee8bc2567 | -4.43024 | -48.47604 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 533976dd-6671-3369-8c99-595d238bd4ea | -4.42739 | -48.47757 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 808f55a9-aab0-3078-acf5-93a4aedd6508 | -4.42166 | -48.03258 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ad3fcc7-f8bf-3867-bdea-7877be20dded | -4.3117 | -48.4113 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27bff235-49c6-3069-9a57-ad2bcde4f807 | -4.31126 | -48.41426 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f0ec6ff-263b-3254-be83-a05028e5732e | -4.17955 | -48.11893 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e9ff3a5-4854-3f54-bbfe-eb5a3d1bd5db | -4.07277 | -48.00772 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c3f1119-380f-37e3-aef6-d2ba5f2a9b17 | -4.07266 | -48.00607 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a20e8a5e-c20c-3ccf-8399-e2dc7c2ba61f | -4.06888 | -47.99804 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a679aacf-efc0-3db3-92cb-471e2dd1be4f | -4.06843 | -48.00108 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db95c76b-961f-3c22-9eba-5b178d89daf7 | -4.06827 | -47.99943 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efd1c790-2805-35ae-be60-62af1f4046dc | -4.06797 | -48.00415 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546fca99-6919-328e-b962-a238be8a52e5 | -4.06783 | -48.00249 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e4a6007-3931-3114-a059-8ecd0873f0c7 | -4.0675 | -48.00725 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1808c3cb-8b45-3023-8fbc-c60738aa2b80 | -4.06228 | -48.50994 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f64b157-2a89-3453-82f8-e310876c2024 | -4.06142 | -48.51578 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c61f56a-e244-3b1e-b113-69f908fd1664 | -4.70481 | -48.68145 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c7582c-1c86-3ccd-a38b-7c71e7c82861 | -4.7044 | -48.68428 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70a743f-28b7-35d4-b9b2-c6593596f771 | -4.68922 | -48.78637 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e08ed01-8761-3370-b6a2-526efb2bb6c8 | -4.68917 | -48.78705 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a493b899-8449-3bf8-bc90-d2dc41d98096 | -4.68838 | -48.79202 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a95955d7-cb09-32bd-9622-b0cf6328578e | -4.59167 | -48.93248 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3687ef8-c191-3235-be46-0431d59be5e6 | -4.5853 | -48.93652 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5155f6fd-cdb4-3cae-b817-f162e315ddd9 | -4.5086 | -48.87374 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 038b50f6-03ef-347b-b249-e48dc1f0b1dc | -4.42979 | -48.47904 | 2024-11-03 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54b2be39-297d-37bc-800f-fe080b58ece1 | -4.36217 | -48.99462 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49664a8f-9434-3781-b3b4-8141281a7cd4 | -4.35916 | -48.99094 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da53e63c-ecc4-3902-9769-7dd1d55dba85 | -4.35727 | -48.99387 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2948010-381f-3bb2-a08c-e4900cf08b52 | -4.06184 | -48.51291 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6337bff3-c14d-3622-8c0a-6e4f45ead623 | -4.0568 | -48.51214 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3a59a28-344f-3a5b-b897-850c36c550ee | -3.86022 | -48.25285 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8751ea04-78f9-335b-b617-4f4288bcba9a | -3.79678 | -48.10291 | 2024-11-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b42c1fc7-c08c-3c2f-9c44-cbcf3b5f670b | -3.67065 | -48.91724 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adbf9df6-97ce-3c7c-99ce-bcfb94b2274a | -3.65209 | -48.94152 | 2024-11-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bf3bc07-20b5-311b-98cb-255ae4f42708 | 0.2575 | -49.82571 | 2024-11-03 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8805620-1d65-3fe1-9196-87252ee44ac6 | 0.25687 | -49.82164 | 2024-11-03 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0941e6d-9b6f-3733-b41f-a3d05db9e26b | -0.11626 | -49.78826 | 2024-11-03 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8416d5eb-becd-3f51-8e87-3a5cdeccb3ca | -0.1156 | -49.79241 | 2024-11-03 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbca86fe-521d-344b-bdb5-28af19a829df | -2.19587 | -49.06412 | 2024-11-03 05:08:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78093bf8-272a-32c7-94fd-52c70fafffd4 | -2.14158 | -48.84189 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74da7e5e-d65c-30c8-9cb8-cbcca9d82613 | -2.05386 | -50.28377 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9b1f712-d782-3bf6-b968-d5bab7404b56 | -2.05323 | -50.28785 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2afcaeb7-de3b-3f1a-aed9-0c6df57a03f5 | -2.04891 | -50.28718 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b114025f-0ae2-3230-86f7-1436f9dfda1d | -2.01923 | -50.27843 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b81488bb-3743-316b-a8a6-b5627ba98bd2 | -2.01861 | -50.27596 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39b871fa-9cdf-3f1a-ba94-e6d3ea4089fc | -2.01796 | -50.28003 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb7fb59-2b37-3e9d-8061-4c66458f0500 | -1.99223 | -50.10216 | 2024-11-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7d3f75b-ba31-3851-9ea7-e71fa47578e5 | -1.90854 | -49.70587 | 2024-11-03 05:08:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2c0494-5951-3fd0-ba82-07f0dd6aece0 | -2.19538 | -49.06271 | 2024-11-03 05:08:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3551530e-b976-38c4-b609-d691f6127c3f | -2.1946 | -49.06768 | 2024-11-03 05:08:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18828fb2-1e4c-34fc-9320-f73dd6549f62 | -2.1553 | -48.88081 | 2024-11-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d4a7107f-9766-3dce-8969-ac3623b2cb6d | -2.02807 | -49.13644 | 2024-11-03 05:08:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b00c94b5-7910-3676-a966-b9ab92e8535c | -3.53382 | -50.11846 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a24be409-443b-36f1-9c92-7199f51dd71e | -3.52788 | -50.11557 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| add61588-e1f7-31f3-a36e-6064f2f213eb | -3.52008 | -49.17269 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24ec1af9-6ef1-3bac-9c5e-7709b1787a6e | -3.51932 | -49.1778 | 2024-11-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7243557c-6c30-3662-b296-48e951493948 | -3.47465 | -50.1346 | 2024-11-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README76.md)
