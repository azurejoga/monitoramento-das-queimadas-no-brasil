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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 735c0d34-015b-36f6-8954-cb1896db288a | -2.76988 | -54.02959 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ad3a65b-0154-3ebc-937a-ff838664ef6f | -1.05359 | -55.24218 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1630250f-532d-3c32-b563-fee00ddc0de6 | -3.0707 | -53.25985 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2821c3e-6673-3edd-887a-31199e6718c1 | -2.80356 | -54.04266 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0b03e99-0bfc-3489-b11c-daff8c80dc1c | -1.49988 | -54.95513 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95f3bce2-526c-33e7-8b5c-37ff9de51583 | -2.86445 | -54.02688 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38c1abe1-f504-38d5-95ef-7e5e58d2cad3 | -3.42764 | -53.89241 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31f743ce-1fa2-37f8-a83a-df18801d40bf | -2.81005 | -54.02392 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8314b91d-4798-3103-b8ca-cab5ff4c7f6c | -2.75798 | -54.12987 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e488737e-4776-3f9d-a3de-8c279852dd3d | -3.73184 | -51.31355 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de6449a2-df93-3ae2-be8d-b398d8535051 | -2.62499 | -54.21854 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c64a3533-5f9b-35af-ba33-6f6c67ab520c | -2.73868 | -54.97694 | 2024-12-01 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8040b1a9-439d-3d3f-a08c-2819a8ae98da | -4.55857 | -45.71062 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72663e92-152f-31aa-bc1e-1c2d5171f66c | -3.02839 | -51.54018 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbb72c12-3dcb-31a6-bda4-453a9c109373 | -3.30482 | -53.86731 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ac1a7550-3697-3ef3-a919-97928ff785a3 | -3.6122 | -54.74411 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1329f7c9-6961-301c-b110-67bca576d6ad | -2.53368 | -54.06099 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1f9468a-11e9-33a9-8805-bf106ef84dc7 | -3.0945 | -53.13236 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 336d4e68-cfbd-3d6d-beba-6be0206c065f | -2.8344 | -51.28258 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81abc17d-bfdd-34bd-8be6-02f17ed9db35 | -3.73742 | -51.83507 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c5de04-a26e-3023-ad68-828d02782418 | -3.1142 | -54.27589 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05b2895a-38e6-3895-902a-0dbd5138d1c4 | -1.32233 | -54.63691 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22295e6d-5c74-3353-a5b9-9355eca08643 | -1.41731 | -55.26234 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 906eac82-63b7-3fec-a1a7-98808f4bf7d8 | -3.14742 | -53.83216 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b468f40-d69f-3511-94f3-560a3b96b36a | -3.252 | -53.92836 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd056c2f-1c89-3553-a9ea-a5cb98a1a364 | -2.89014 | -54.16055 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adf157e9-a0f2-391c-abc1-5e680da76444 | -2.87024 | -54.03569 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62ca5925-6d7f-3b46-9d91-b9a95d87ccaa | -2.98448 | -53.2895 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 246fe823-79d8-3c59-952e-d359239a1a68 | -2.44612 | -54.01653 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f746d9d9-0cc2-387d-bea3-f9c84d469509 | -2.93424 | -54.30288 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c8354e-e9b8-33a5-87a7-c49cda88f580 | -1.74766 | -52.65376 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8fdbd16-8ba5-3da8-973a-a71c2fc677cd | -3.3028 | -50.80354 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f641ace-6e77-3dea-939c-3cfb20bc437c | -1.66527 | -53.77269 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c7ca718-ee60-35f9-901d-8be1a4d2cff4 | -1.44385 | -55.20206 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9dd4c1-e38a-3a10-8651-9aac36082a1a | -3.53878 | -54.086 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 364c31f1-2a03-3405-8328-79b5f5c76840 | -3.46967 | -50.26706 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cbb3ac85-0e8f-364e-9420-10713768cb7f | -4.12388 | -54.20722 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c451483-057f-3071-8ac0-e35fcbac22db | -2.75403 | -54.08621 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dace5839-fb87-3c81-8d25-790af91e3abe | -3.54237 | -50.17596 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df5b9e0-9cad-3898-939d-dbaeb677f90c | -2.5967 | -54.26459 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d905c3-8e7b-367a-9c05-5955ba48de8d | -2.62728 | -54.22664 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 661150f0-9590-3f3e-8842-1680c541e048 | -2.0295 | -55.7766 | 2024-12-01 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebbd04a7-0927-378c-bb03-3dbbd0b797e4 | -3.50672 | -62.7523 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aef0a9b-0ccc-3227-ba2f-c80ec00feb8e | -1.71624 | -52.78154 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 465c55aa-f75f-368b-abb4-164400829ded | -2.69379 | -52.915 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a01fa4e9-809b-38b9-854e-62d44625c6ba | -2.90027 | -53.95693 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 020657c9-c33a-37a7-a205-9574125cc4e2 | -3.2083 | -50.2711 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4b2541c-9df1-39ce-a36c-1bbb440bcbec | -2.97851 | -53.89296 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f078200-b2a2-30ee-b2ba-c362854e9390 | -2.72228 | -54.14039 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c850fc83-2d7f-3b79-83f9-d8debbe6bd0e | -3.11074 | -54.27536 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d742d3ce-0c9a-3cfe-bfbc-fa75e668ac5c | -3.2535 | -50.75595 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92349e52-a65e-3030-bec7-d71b229e3f04 | -3.48349 | -53.81179 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae8445b1-22d4-3981-98ef-e945fad3f219 | -1.66816 | -53.77702 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7195135c-d49b-3d3c-aee0-d577d496cd38 | -6.29099 | -43.84984 | 2024-12-01 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3794cec-afcb-38fe-bd53-2736feb47d9f | -4.20645 | -48.12504 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a534dbf-c048-3a81-b376-32dc74914f47 | -3.26552 | -53.62857 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 12a26142-e58c-3a0a-b16b-b1ff1e1abe1b | -1.62989 | -53.8619 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 626246f8-a66f-331d-8a60-5a806169f708 | -0.18814 | -60.67825 | 2024-12-01 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5783da6-4998-3cb0-96ea-ad3402a1eaac | -3.32741 | -50.19539 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b0c4298-80a5-38f9-a769-7ba70b099a71 | -2.44557 | -53.62233 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52afd953-e94b-3549-92c0-bee3df76fa73 | -3.69561 | -50.16867 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1cffd68-8dc6-36bb-9edd-61aa2596385d | -3.50914 | -53.78699 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46250ed3-af98-36ce-89b6-8dfb10ca392b | -3.22999 | -53.39259 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6eaf4c42-8718-3aba-bd45-c9f3377b4aea | -3.05637 | -52.76661 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 695bc1db-1b8f-3e81-9db4-7b0fd6bed757 | -2.35724 | -53.65405 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c7741b-b3b6-3a3d-be55-f031a30bbd2e | -2.92575 | -51.44897 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d76b4f58-f878-3485-b607-e1c2e8598ed5 | -2.87329 | -53.99258 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d5e5a32-a6fa-375a-b75b-25afb1b88481 | -2.97611 | -53.74704 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3acb3cc-14ca-360e-a689-49c2b4e636c3 | -4.54598 | -43.30139 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4f4ceed4-9079-37c5-a3a9-a8e3d9f7dbe0 | -2.76263 | -54.12276 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc8b9229-0d9b-3f73-90e7-1cb484d6b2a2 | -5.58459 | -45.21114 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e1eaded-a50d-369d-a532-9931f26c9cb3 | -3.32899 | -52.60067 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7767ab-4582-35c1-a40d-fdeb5b2387c8 | -2.84954 | -54.19331 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14c290fc-c63c-3974-aebe-77615a1acb63 | -4.18254 | -47.99263 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5416fc8-e342-3a7d-bfca-6a1a78c470af | -2.56449 | -54.34089 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85bf770-3bea-3801-8121-88ed83663935 | -1.24279 | -53.3508 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba8ebf1-a87b-363c-8485-39af55833a9d | -2.88026 | -53.33512 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fd3a364-3868-3819-b8f2-77b3a3d7d492 | -2.57183 | -51.88373 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7300c2e3-fa29-3a48-8623-499f992b76cb | -1.70798 | -53.24434 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9125e92e-857e-3ba4-a297-c89217ca089c | -3.1039 | -53.80944 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a14fd43-c147-3faa-96dc-7f7ab9b979bf | -2.74443 | -51.75439 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f7ca64e6-5ba6-3591-8584-701c3ee40f3c | -3.28848 | -53.66919 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f8ade26-927d-3a76-a4f7-9412e8df58c2 | -1.72154 | -52.62746 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e112a691-13e9-3292-9205-1fa8c8866f43 | -3.15042 | -59.20514 | 2024-12-01 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd332ee8-6d31-373c-bc70-adc727c5fc50 | -2.29097 | -50.69046 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a1493f-19d4-3d88-89d0-1e3f8422d1d0 | -2.87292 | -53.92477 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ea82abb-e990-38a4-87bc-86725b92f12f | -2.60411 | -53.99752 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ade1f636-feed-363f-9195-af8f28b49b04 | -2.29608 | -60.26795 | 2024-12-01 05:08:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61ffbc79-4c1c-37c8-ab51-7769f994d4ad | -2.36996 | -50.39849 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a3ba42e-5b01-3f79-9efc-2c80bb0b7b6e | -3.14327 | -53.83563 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53f66f8-c04a-33d7-b595-db9b73d86197 | -1.5973 | -52.2803 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 313591da-3d5c-3e0a-a7ef-3450c5462632 | -3.24203 | -53.92291 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4550ef5b-dc10-3535-8c02-7e91f3061ba8 | -3.31762 | -50.02526 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3cb7760-bf0f-3363-bb23-bfa70fd85343 | -1.75485 | -53.64263 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19059a58-1144-3c9c-aa9d-688f64a8ec5a | -3.98111 | -46.64269 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b89d956-8167-3867-ae0e-cc547aade1ed | -3.02786 | -51.54372 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a954a520-3a3e-3ebd-a42b-12f17a7ece54 | -3.31249 | -53.86444 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dea03334-a360-3ae9-bd67-757c97e5951a | -1.9308 | -53.44181 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eac73798-1b9f-3819-8595-5da0eee29081 | -1.40023 | -53.38663 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d484ee89-6e2d-394d-831f-c585552aa610 | -1.75648 | -55.41824 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README89.md)
