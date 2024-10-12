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
| a8236617-9e86-32d0-b647-2288d7aa095f | -11.66607 | -52.61982 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d5862c3-a617-320a-8a76-da4006a1dc01 | -11.53786 | -53.86498 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 338f49f1-f4e4-3088-a730-8867c7fcd0f4 | -11.53731 | -53.86861 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c07b2275-680c-3241-9b67-d898d423e39c | -11.53449 | -53.86445 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c03883-0f70-38ba-ab4a-2a45dad183e5 | -11.25524 | -53.27443 | 2024-10-12 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b8e002d-0f3c-3cc0-80ac-06fa9c3a31d4 | -12.96729 | -53.5173 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38a61928-bbc2-3e53-a8cd-caeb3d0792e9 | -12.96385 | -53.51676 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eb3f249-63b9-34fc-a2b1-a80893a1affe | -12.96328 | -53.5206 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a804cb9-f700-331d-925c-01c379ea4481 | -12.96215 | -53.52829 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a0bc459-98a6-3ff5-a4e9-71ecf9bfd2cd | -12.9604 | -53.51622 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15ea4a6f-6628-3443-bb45-7a2e55773217 | -12.95983 | -53.52007 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4662da5-1301-3317-9641-812485b1ed4d | -12.9587 | -53.52775 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 385ec897-5802-3ae4-a297-e8bbb886dee2 | -12.95695 | -53.51569 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf89fe4a-7af3-39da-9cb8-b37548e3896b | -12.95639 | -53.51953 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f8c7a61-20a6-3430-be9b-21cf04e0214f | -12.95583 | -53.52337 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e633acda-618d-3d95-aedf-4869ecf72920 | -12.95526 | -53.52721 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f25b8a4c-286a-3edb-9c88-eb8c1a4a48c9 | -12.9552 | -53.50359 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c57c7ec-8556-33a9-b255-e80b644557a4 | -12.95407 | -53.5113 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e80f9c5-3b6d-3b43-96e5-50f708de5b39 | -12.95351 | -53.51515 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b3472011-e20c-3896-9c72-d718e81544c4 | -12.95294 | -53.51899 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 642abfe2-55ed-3f06-a871-5f015a5ab181 | -12.95238 | -53.52283 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 649caac7-df1b-355d-86f4-3b13bcf06b11 | -12.95232 | -53.49919 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33651bc3-1dc4-3dd7-aac5-e9d814f16655 | -12.95176 | -53.50304 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a716197-540a-3ebc-991d-f584f3ae3356 | -12.95063 | -53.51076 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce5b17fc-6acf-3e8a-bfdf-874fc2e33573 | -12.95006 | -53.51461 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 29cba00b-153e-3307-9038-6688a4650e85 | -12.9495 | -53.51845 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 063b157c-a729-3875-b1dd-90133161cf15 | -12.94894 | -53.52229 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 027c7503-8198-33a0-a7f7-4cac32ec1873 | -12.94838 | -53.52613 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| acc09b4e-ff69-37bd-8105-7c513aa02d1c | -12.94831 | -53.5025 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| daddddb2-563e-3312-87fd-ad6d70773cbe | -12.94775 | -53.50637 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc7f95ba-7354-3d0b-b4d7-c8ba9e87166e | -12.94718 | -53.51022 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a9927080-a076-33d8-92b1-a2cbb5da814e | -12.94662 | -53.51408 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 969a8c44-0312-369b-b916-2722a72b99d9 | -12.89784 | -53.49158 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ab7a26a-916a-3146-afc1-52365b312409 | -12.89441 | -53.51468 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23f78ddf-5b1b-3c3e-acbc-826f91af6fc2 | -12.89384 | -53.51852 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2bb827b9-5c80-3bb2-8b5e-311c233997a7 | -12.89382 | -53.4949 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60111903-2c61-3ce2-9a71-f22f26252b67 | -12.89327 | -53.52237 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4220609-9b1a-38fd-a2fc-83b6a51fd975 | -12.89268 | -53.50258 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa054bc-2c73-3792-bd8a-4e73d54f5134 | -12.89211 | -53.50644 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a87a2f3-c01d-3da6-8d37-63f86bc569bf | -12.89154 | -53.51029 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fa1b563-a3a9-36ca-afac-eac6a250ae08 | -12.89097 | -53.51414 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef93af9c-d84b-3d6f-8f91-8b1edcf36221 | -12.89039 | -53.51799 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f48269cb-d45e-3e0f-bbcc-b924e937114f | -12.88982 | -53.52184 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7436f9c5-4241-37bb-b191-1e84ee79c2ff | -12.8898 | -53.4982 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e54713-b35a-3426-85be-411dde271c7d | -12.88925 | -53.52567 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2687128-9037-39b8-b69a-ac9a71b0f2ed | -12.88924 | -53.50204 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa3bfff8-2cef-3eea-b943-1890418dca16 | -12.88867 | -53.50589 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3cf8570-1e6d-3d9b-b260-59f9e1851bb3 | -12.88809 | -53.50975 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6f9b68e-9757-3717-8d75-e7cce87be054 | -12.88752 | -53.5136 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ece061e3-7fcd-36d2-9a3a-0e5217754d3c | -12.88695 | -53.51744 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c07a551f-fa40-3cef-accb-cace29371ccd | -12.88638 | -53.52129 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06a42407-1fe2-35b4-a8c2-04cc21958adb | -12.88581 | -53.52513 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adf965d1-7532-3440-b110-6bd22b133b5e | -12.88579 | -53.5015 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bd065a5-a6ea-3618-bdfd-6d37a60701cd | -12.88522 | -53.50534 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36a9fc53-5e6a-3e1c-b49b-7dd905f9f26a | -12.88465 | -53.5092 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d64f5019-e715-3333-98b5-c8e62bc9e736 | -12.88408 | -53.51305 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac37fc0b-2d0b-37b7-8b77-3f542c2ad07d | -12.88351 | -53.5169 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df3f1f2a-5bd6-3d8b-bcc3-1d51324742ce | -12.88294 | -53.52074 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3bf8eee-c67a-3e9c-8743-ef4aa5a26987 | -12.88235 | -53.50097 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 276fdd52-7943-329f-8a9a-6150a15e9af5 | -12.88178 | -53.50481 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a87cf68-df15-3506-b781-fb89f365937d | -12.88121 | -53.50866 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39f65628-2ac3-345e-a636-99b44889c6e2 | -12.88064 | -53.5125 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c48555bc-d8b1-3318-8de0-3eee70b1830d | -12.88007 | -53.51635 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c299939e-50f3-3a67-9584-18a80cbadf97 | -12.87833 | -53.50427 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95626a81-0572-31dc-aabf-a60a9b609c2a | -12.87777 | -53.50811 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ce604d-f516-3469-83f4-53870e98dde8 | -12.8772 | -53.51196 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8d1a9bb-3563-32e4-be9b-be867b601e11 | -12.87546 | -53.4999 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 051967d5-e1f8-3475-b226-6aa5750a5b92 | -12.87489 | -53.50374 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 316c8091-2d39-3e3d-bb0c-efa67667669b | -12.87432 | -53.50758 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9545d2dd-6cd8-34d1-a349-3962f35eb249 | -12.87144 | -53.50321 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2902df3-0fac-372e-8e8f-679464c64826 | -12.87088 | -53.50705 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ae37b9-e400-32ad-a872-e3e03c767fe6 | -12.87031 | -53.51087 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| beaa396f-9b85-3606-81f5-9c22c001a5b5 | -12.868 | -53.50269 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f10e1812-e05a-3e6a-a4f1-ec52e35a7a60 | -12.86687 | -53.51035 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f48fef4-bcf3-3e6b-94b0-e71efac86125 | -12.8663 | -53.51419 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82937e52-d9d3-330a-a5e1-34e805649133 | -12.86574 | -53.51802 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 431f56ea-4b3d-34c5-827d-2079d52eee54 | -12.86517 | -53.52185 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c9348ac-446d-3801-a049-205136d6b4b8 | -12.86399 | -53.50599 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6daa0565-c4cd-391f-a8c6-60b324b3924c | -12.86342 | -53.50983 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ceb849f-a531-38e5-ae49-e9bb2b2cddba | -12.86286 | -53.51366 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efba7841-5958-310a-b490-7ed1119b047a | -12.86173 | -53.52132 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5e524db-1bb6-379f-b679-ca5ed3fa872f | -12.86117 | -53.52515 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d35b9e-5abe-34b1-a65a-f35944be5030 | -12.86111 | -53.50163 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0ef8507-f072-334a-b534-3585b1bcdd2a | -12.8606 | -53.52898 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c86ed26e-12fd-3157-9f1a-2a709b80d916 | -12.86054 | -53.50547 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be6993a1-c550-320a-b80f-0035f90f699c | -12.85998 | -53.50931 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c26bf52-a846-31f6-818d-13d8e11fc933 | -12.85941 | -53.51314 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c332a7e-0e4b-3210-b18a-94a04ef1727e | -12.85885 | -53.51697 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5943938c-6479-30fb-a767-28159e9c826f | -12.85829 | -53.5208 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c163952-35e3-3d44-9119-c69325d3e1a7 | -12.85772 | -53.52463 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13922c48-91fc-3f00-a177-8f6c4203d15b | -12.85716 | -53.52845 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b146c13-252f-3f8f-947d-2a49ede3af41 | -12.8571 | -53.50494 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad726f5a-2432-38ff-811e-5949eeeecf33 | -12.85654 | -53.50878 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff78470f-3f43-3a2d-8816-d77c21f5be5d | -12.85597 | -53.51262 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab8e1706-2f10-3fd8-b96a-eb6204ff821f | -12.85541 | -53.51645 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ea109f-b9b4-3559-8880-e2bc449e4c88 | -12.85484 | -53.52028 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc497a39-7785-3693-8187-2e2e7ab7aa38 | -12.85428 | -53.52411 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e628cba-e928-37b0-b897-aaed76422707 | -12.85366 | -53.50441 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9bf7d3c-6a02-37f0-819a-a06d690cf303 | -12.85309 | -53.50824 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c5c641c-e25c-349e-a951-b2b678c282d9 | -12.85253 | -53.51209 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README89.md)
