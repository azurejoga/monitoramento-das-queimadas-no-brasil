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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34338c5e-8e53-359d-b7b0-8eedd650560a | -2.67146 | -49.73486 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e4cc67-78b6-3d79-aa3d-388c2914c48e | -2.66815 | -49.73435 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bffcb4d9-cbc8-3855-9a0d-1553067bcd44 | -2.66341 | -49.80768 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f39cd24-c53a-30f5-8758-90b7d30f5759 | -2.65578 | -49.8347 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58d45dc6-958f-3c70-9d6e-058da763e4f4 | -2.65247 | -49.83419 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a3f24e-199f-3078-8d2c-2cf43d751463 | -2.65193 | -49.83763 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb65a19d-f1ba-3d8a-841f-494a726a491f | -2.64863 | -49.83712 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e20014b-6018-3544-9d99-e174eb7a899c | -2.63862 | -49.98691 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e35b6c-b662-33fe-8fab-b1c4e4ece229 | -2.6176 | -49.77591 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 144e223a-fcb7-3fe3-9024-90b74e473ded | -2.58719 | -49.66494 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cfc139e-24b7-3b96-bf94-5d184988d96a | -2.58507 | -49.76734 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c99a7d1a-a3ea-3ddf-921c-ab3cd8cf5e13 | -2.58177 | -49.76683 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05f08361-1fff-3629-8ff7-4d11094633d8 | -2.58123 | -49.77027 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0daa98a-40c0-3d4f-bfce-a21904a9547c | -2.57792 | -49.76976 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ab935b1-4a4b-3442-9a98-b322456799ef | -2.57286 | -50.06107 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d365d60-0334-3b58-9c9e-14aaf236f004 | -2.55951 | -49.62531 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49170383-b3db-344e-8cb1-e7607fb7a9ca | -2.55897 | -49.62876 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a491676e-5ae8-336c-9fc5-89f32f712334 | -2.54779 | -49.76471 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1868d534-1e5c-31c6-a53c-99be69747f78 | -2.54449 | -49.7642 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7454be78-9983-333c-9f77-c7db96391d08 | -2.54023 | -49.81289 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8569df4e-fac4-3b93-94c1-7d5931ff7e23 | -3.01641 | -50.48214 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 68a93fb5-614c-38a2-967b-90d3518b3cab | -3.01533 | -50.48901 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 031be0fc-d1e1-3a4b-b3d8-4436396d3328 | -3.0098 | -50.48111 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d4c9bd6e-4535-341c-966a-99d2b745a06b | -3.00926 | -50.48454 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e4489eb2-3f32-3100-a91b-359c7329903c | -3.00818 | -50.49141 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1fff65b2-ac78-346f-935a-684c539a2c20 | -3.00562 | -50.48384 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c07b2ff4-2e51-3328-ab07-cce927a46fea | -3.00123 | -50.4902 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 34bfd4cf-9058-37bc-b6d2-f1a3f2af22b3 | -2.99847 | -50.48624 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a7b26f91-9afd-38fd-8a22-7ffcfdfd91a8 | -2.99793 | -50.48968 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| dcf437f2-4664-3251-a7ef-025e2f919d4c | -2.99517 | -50.48573 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 61a81dcd-2061-35e4-9b05-d4d4a4930a96 | -2.9891 | -50.48127 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c1ffb16-8865-3f9b-a452-7c7eebeb0443 | -2.98856 | -50.4847 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8460182f-c90b-3588-97b9-0e14dde19ca2 | -2.98691 | -50.30158 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d2453a-b446-34ee-9f1b-2f8bbaaa213d | -2.98469 | -50.2942 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6623a69-6240-38c0-a83c-79e7c7cbfecf | -2.98415 | -50.29763 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8db170a-4266-3609-8240-ca604507d9ad | -2.98139 | -50.29369 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf462ede-5be4-3b86-becf-d0d63262c8a0 | -2.96856 | -50.41826 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9ead269-c974-379e-9653-c043a77a7b06 | -2.96802 | -50.42169 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14528e85-6ed0-3c9b-ab72-5d9c125df042 | -2.96748 | -50.42513 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a108531e-6023-3cb4-a061-830b2cc68e44 | -2.9658 | -50.41431 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0d980f4-9fc6-3ef0-8fe5-4e80e7089042 | -2.96364 | -50.42805 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 589bbf12-b92b-32c9-93d0-3d2e5b7f1b3c | -2.96227 | -50.52284 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0c18cc5-f6d5-3700-b15a-6696a3a45514 | -2.96196 | -50.41723 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 533858b2-265f-3bb5-9000-4bdf4d8bd40e | -2.96034 | -50.42753 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7ea40a3-ddbf-30aa-a1a0-d0cb54ff55b6 | -2.9598 | -50.43097 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbc8b378-0cd3-35a0-a014-c45359fc5c15 | -2.95896 | -50.52232 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d0a15e9-3180-33cd-876c-7714627896d9 | -2.95842 | -50.52576 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e64884cf-6cb7-3aa7-8384-642950003d99 | -2.95758 | -50.42358 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a871a0c0-2a30-3979-8cee-e595fb66d9ed | -2.95374 | -50.42651 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 689a3a64-75f0-3d1f-851a-ff47949c6627 | -2.95182 | -50.52473 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd3e92e3-68b6-3321-90fb-24c79a4d088a | -2.45032 | -50.25597 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5a3dce2-9bce-3953-b2e7-2258f8f6eb8f | -2.44848 | -50.37519 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2cb9a3c1-45a1-3cbd-95d8-6cb90aa6066d | -2.44794 | -50.37862 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bebe9e19-9686-3a46-b772-b7d9f354e87b | -2.44594 | -50.26231 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e4afa01-fa62-34b4-954b-93fbe6039944 | -2.44518 | -50.37468 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54189afd-03dd-3c2a-bb67-64887fd85c79 | -2.44464 | -50.37811 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5315e509-4686-362f-9b8e-b9336289681b | -2.43778 | -50.29267 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02c2e228-6d98-3378-8000-325a6fcceee0 | -2.43724 | -50.2961 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf2db1d9-da7d-314e-a740-11de6f5c9d5c | -2.41942 | -50.40937 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeaba7f1-91e2-3161-afbe-e1c22f38f6f2 | -2.41666 | -50.40542 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 074a1b7f-05ff-3c3a-9c08-71a19144f5f7 | -2.41612 | -50.40886 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e8c838a-d67f-3087-aa5d-02525a65ccc6 | -2.41336 | -50.40491 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f75920f-bfb6-3ada-ba83-90e8c58f874d | -2.40351 | -50.42448 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea52436c-3f17-3304-99f6-6428ccad7f3e | -2.4002 | -50.42397 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fba09ec7-2828-335f-9d84-20dfbf91aae7 | -2.23483 | -49.68093 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46118bfd-3925-3999-92cd-3c1041bd6120 | -2.2199 | -49.84058 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cea340d-af24-3e8f-abe8-a2f1b3364e09 | -2.2163 | -50.31807 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344ee2a7-ce50-38fe-8c38-e111a2cb9881 | -2.213 | -50.31755 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b05c330a-107e-38dd-93e0-de49553447f4 | -2.20008 | -50.22768 | 2024-10-26 04:42:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67a526aa-2532-32bd-840b-c208949734f8 | -2.16871 | -49.67068 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d1e917e-5378-3eb0-9648-6613e704cc54 | -2.16817 | -49.67413 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ace7a7-da05-3cbe-9269-55390fe550de | -2.70229 | -49.05895 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c805a9-f9c1-3910-bac3-97b0f542590e | -2.70174 | -49.06247 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebbc7c61-e9f0-3cda-b3d4-bf87c3e4a08f | -2.69895 | -49.05843 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20719643-53f3-3d87-b900-d55b27b31724 | -2.6984 | -49.06195 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f63dc2a7-7348-3339-8c75-6fb5b1307d42 | -2.69724 | -49.04734 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21ef9911-6fed-3b2b-8661-ca2517bddd02 | -2.69615 | -49.05439 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78f843ae-a9af-32ef-b539-54511f631d99 | -2.6939 | -49.04682 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a4c0d69-854a-3543-bb1d-048674603c41 | -2.69335 | -49.05035 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92743e6d-5a00-3015-a515-cdc3713a7203 | -2.69056 | -49.0463 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c1ae8c7-ca03-37a3-8788-bba431c8c5b2 | -2.68803 | -49.04568 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c5bce0-1d72-39ab-8507-36c42ccf54f0 | -2.68468 | -49.04516 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faaa3277-0b83-3882-a383-de1510936f78 | -2.62184 | -49.09675 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a8661c-7b56-371e-83d8-6b11ad17bc63 | -2.62125 | -49.07866 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 643afc57-d3e6-3ed8-9e83-940c373605cb | -2.60126 | -49.09718 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67b11bf1-5849-3b40-a3d8-38544855aa4b | -2.60072 | -49.10069 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33f16e3a-685a-36d9-9d57-92ceca69084f | -2.59798 | -49.11826 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 285d2090-e552-36b9-a6dd-08d469cafdb7 | -2.59792 | -49.09666 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 95056b1c-7b84-34c5-b355-8cfbd875da36 | -2.59738 | -49.10018 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c79dbfbf-62d1-33d6-9982-2fc0d3203856 | -2.58517 | -48.96546 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26ce1a26-5129-3615-8dab-41778cd5cf66 | -2.57846 | -48.9427 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 006e24a5-f2cf-3304-8a0b-6c3fcdfd734d | -2.5779 | -48.94624 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c534d9a3-3ce0-390c-8244-472b4dcd544e | -2.56619 | -48.9553 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23463eec-475d-36f5-81c0-7c1b22c9d40a | -2.56469 | -49.11738 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8ce4a3-e9ec-3bee-ba08-d714dc3d8845 | -3.46815 | -49.26718 | 2024-10-26 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ccd91ae-2e4d-3ef8-88dd-650a4847d642 | -3.46481 | -49.26666 | 2024-10-26 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d8d5ccc-ff89-3940-b8ad-32a52b805ca3 | -2.85412 | -49.13276 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29835238-f00d-3969-8ffc-aecf747268ec | -2.85357 | -49.13628 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ef8a38-48fa-3f03-a176-80c152e3935f | -2.82823 | -49.25453 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8f5692f-3c2e-3f0c-8ed9-7f4f5938ad3a | -2.82769 | -49.25803 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README68.md)
