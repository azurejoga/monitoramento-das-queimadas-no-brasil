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
| 21e76347-84aa-3167-b164-ad1499ee8743 | -4.2605 | -48.697 | 2024-11-23 05:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 208179d6-c858-3087-8b0b-f3e56fe093c8 | -1.7359 | -52.7385 | 2024-11-23 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2d800e47-f5c2-39c3-9170-ac87c2dcc586 | -2.7655 | -54.05802 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926685be-bf27-3264-81a2-6a6a5b910c3a | -1.44739 | -53.39511 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba85c41-66c9-356f-85f7-9505a7f70b33 | -2.15168 | -50.91763 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7f6f91c4-be87-3eec-9686-95af596b6324 | -1.76386 | -52.69972 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b336f25-7c19-3411-be0f-93395fd51ee6 | -1.79212 | -53.64724 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8b59a20-58b1-3b5c-952a-98867e5f1404 | -1.19265 | -51.96969 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8c2cfe5-4178-3f02-8c4d-a02687de2e69 | -1.78523 | -53.62681 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e84270c0-da1e-386e-8ebd-bada022ff63d | -0.26053 | -51.57532 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63e04478-e679-33f5-ba79-745af41c2a97 | -1.25002 | -51.75014 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0482ee4-2345-3fde-b9ac-fa69cc9b744e | -3.16164 | -50.58396 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05297605-2a37-38f0-9ef1-0a569af829cb | -2.161 | -53.62963 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0eada71-698d-3782-a3ef-75dcab5c5a44 | -1.28738 | -54.54319 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b503eb20-e531-3052-b778-da78698c7526 | -1.21528 | -51.73958 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a9ca3c2-18c4-3f33-b8c8-7fe1b8309284 | -1.96286 | -48.38679 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61674571-92a3-3dfd-b474-043df86932ac | -2.24264 | -53.6618 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0dc5c05-c09f-3844-859c-775da08f8f4d | -1.67668 | -52.661 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| efa39aa1-277d-3cd6-acda-caa69289166d | -1.24228 | -54.01981 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ac278f-4891-357c-ae07-c35bc4fb6b24 | -1.72741 | -52.71253 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8566fb6-2881-3664-a8d9-1cbfab83e358 | -0.97023 | -51.71659 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62ecc35d-86f6-3d61-9f57-e7712acc6b6b | -1.25609 | -53.32199 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b73c8619-f3a1-34ab-a89f-7800504bcff1 | -2.76196 | -54.05748 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76d5fdd-aa72-3c72-8a06-c81952e68388 | -1.37483 | -55.18068 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32d01d79-7d68-310d-8d96-58650928843e | -2.73729 | -47.54022 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f481bbf8-f35e-34d7-aca5-3d78e962bf78 | -2.23008 | -50.51698 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2442cfa0-f7fc-3776-8d8a-2a0f8981028e | -1.98577 | -53.13347 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 483a8a11-90d6-3fc6-b6a4-23bfbd8e3ad1 | -2.58047 | -54.0354 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24405c16-042f-3b66-90cf-1da846ab1075 | -3.46518 | -48.25003 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c09901ef-7406-3cf1-92cf-bb5ae509936d | -2.56855 | -54.06569 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b32f110-7821-3d64-87c4-5958c11dc8b7 | -1.63369 | -52.69127 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9da6977e-2a6d-3833-a2e5-f8f4e56a2550 | -2.22673 | -50.39167 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50743d7c-f065-326d-8fbc-c388f30204c0 | -1.43958 | -54.51281 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1323abc-1653-365b-b360-7c2e0c14104d | -2.06808 | -53.23272 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4eaba2a7-c3f4-39f9-af93-3f76f02285b5 | -1.65921 | -52.69982 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93de2544-1f14-35c0-a02e-eade2a19d4d5 | -2.70385 | -45.98181 | 2024-11-23 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79a73165-f786-3d52-bd16-09b8dc2bdf9d | -2.20541 | -53.67418 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe93a827-1032-3638-8454-c9aec755b11f | -2.58923 | -54.0487 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d89f33d-5f34-3dcc-88a2-2b42c93ab12e | -1.20795 | -54.03441 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be3847ee-219e-3c62-9110-de06728d1518 | -1.10146 | -53.18868 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93bba4a2-21a0-317a-bb24-0877f8f20abc | -1.29733 | -51.73164 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86909ca0-0700-375d-aea6-cb6401ccdde6 | -1.19635 | -51.94519 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c21e6432-dacc-3869-8c38-04492d9a3792 | -2.77077 | -48.60632 | 2024-11-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ed40182-bd45-3950-97b8-e085ecc9c782 | -2.16982 | -54.46421 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a582ba-996e-3d7a-b43d-2e7515741908 | -1.11491 | -53.38998 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abe7ac23-a9dd-34bd-bac2-3a8d2ed23d4e | -1.72299 | -52.71645 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c255ec8-02e2-38db-ae6d-9a338803274e | -1.56056 | -53.5325 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 788b1a66-ed28-3528-8da0-f84331454e3b | 0.95171 | -52.10058 | 2024-11-23 05:10:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a68d56-42dc-30b8-a42a-c39e0102bb2e | -1.43391 | -52.67831 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34eb44f4-8f8f-3be8-95e5-50ce12f20311 | -1.28169 | -54.53477 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f4250d-51f4-315f-8897-d8e83e038a29 | -2.69689 | -46.26868 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09c37c06-b95c-319a-bb24-e645e4640a11 | -1.1429 | -53.39869 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50a14d2e-a59e-3431-8c5f-050b6d18aa6b | -2.06413 | -53.2332 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bdcbad16-0ef9-36ed-98a5-ba0650cebc5d | -1.46382 | -52.68286 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 452e0fff-cc70-3af3-bef3-930ac5ac664d | -2.74746 | -45.97544 | 2024-11-23 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c03837-2598-3e97-ba45-e829101820e2 | -3.0719 | -49.20023 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e184e1f3-b27b-3023-9eed-3edfb21c2e36 | -1.62972 | -53.30946 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 564211c6-b958-3c99-a683-0e184e1bf8cd | -2.68391 | -52.06744 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fc0b8ebf-4c58-3db2-b04d-93790bf6e14f | -1.11659 | -53.40286 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 456373d3-3eef-3475-b8f0-3711d83b43a2 | -1.67223 | -52.66494 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f21e03c3-88f6-34f6-a796-61ba35006096 | -1.96787 | -48.38755 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d60b289b-80ac-3d15-bb6d-e5754a827bc5 | -1.78793 | -53.65619 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21ba06a4-252c-3f2b-9191-56747b41580d | -3.46565 | -48.24684 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bbbfbd1-65e6-332c-9fe5-4d0556f9acf5 | -2.91006 | -53.06392 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 216fa940-7901-3435-8e69-e7cf46ee9a1a | -1.44802 | -53.39101 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261faf6a-cd53-30fc-8833-47f6e08cac59 | -3.34431 | -45.16814 | 2024-11-23 05:10:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 57d729c4-1234-3a89-8a4f-f4dee4a7ae46 | -1.45521 | -53.39212 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9bec9fda-7989-300b-81f8-59e564b6d5ac | -1.40739 | -54.53902 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c191c09d-9b8a-3fc5-a4fe-4b7db8b036ed | -1.75398 | -54.5215 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79f9ec7c-62e9-3f2a-883e-03649fd78e35 | -2.5419 | -53.98065 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f72c03a-b6cc-33e0-b58f-82ccacfbca39 | -1.6305 | -52.60543 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 705f373f-0784-3e3b-afc6-4dca472ec75c | -1.08335 | -53.64158 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb35b45e-2ac4-3984-a8f3-68c8df6611a2 | -1.60543 | -52.41806 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37b9cc70-871d-365f-a631-f84f7b9f5978 | -3.05286 | -51.54076 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f365ef-6242-3faa-90ff-40c372c02c2c | -1.62602 | -52.60939 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 502723c4-4e32-3483-84e7-6cb860b6c1f6 | -1.60182 | -54.64278 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e5e70e-8e25-3ac3-93c5-00f243eff02a | -1.76317 | -52.70423 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 957c2aef-becd-31e6-a58d-dc652dcdd958 | -2.5294 | -54.01511 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c370020-3a79-3a36-8735-508218e60c36 | -2.89721 | -53.04804 | 2024-11-23 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b905427-d775-3bf0-bcbb-42dc68c5301f | -0.05213 | -51.23677 | 2024-11-23 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c736fc5d-796e-35d9-a032-330afd351be5 | -2.50838 | -54.15276 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5247e4c7-dd32-32e2-a681-8276952e6bc6 | -1.95042 | -51.04231 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c33a94e-d0a9-3ca0-b8c0-c3a381e44f34 | -1.52698 | -51.62353 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5c8086ef-33bf-37e4-8a17-8ca6d130d984 | -1.57858 | -53.81333 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8988332-d39c-3de5-9e18-57ff9c522a26 | -1.3955 | -54.50285 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1608b55-8575-3ca8-b2ea-802a20e7d517 | -0.80894 | -51.61277 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17e0a6a8-9cdc-312e-a6f4-c5454f061183 | -0.81939 | -51.4896 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b75c9765-5285-3dae-8f63-65974d7f00b8 | -1.67362 | -52.65591 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 142f91e0-dc5e-3256-8fcb-924120ff44ea | -1.20513 | -51.75347 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a766558-b261-3e10-92b7-5fe5871a78e2 | -2.68921 | -45.66291 | 2024-11-23 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73e752e8-afb3-36f8-a7db-dde235301d8d | -1.78207 | -53.64702 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5832273c-685d-3118-95b3-90f608190cf0 | -2.95479 | -51.44608 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31cd11dc-c9ba-3179-914b-d91ec7a0dc2c | -1.21559 | -51.79111 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81c7e049-9db8-3204-b128-bc9729aabdf1 | -3.15607 | -45.21917 | 2024-11-23 05:10:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13959a8b-2351-3cf2-afe4-2793fc0b1477 | -1.62702 | -53.31927 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856bfac8-9bf5-3b12-9de9-3bdf6ac56d6b | -1.22711 | -51.74143 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df92e3e8-0a2c-3e35-b00a-abb3f7fc4067 | -1.14027 | -51.67973 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba7d4798-a079-3956-87e0-c3aeceb763fc | -3.46682 | -48.24821 | 2024-11-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6064407c-8c25-328e-afac-8edc9988d930 | -1.40364 | -54.473 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc491e11-d45f-3c09-86f1-e3deb19debf3 | -1.62341 | -53.31871 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README47.md)
