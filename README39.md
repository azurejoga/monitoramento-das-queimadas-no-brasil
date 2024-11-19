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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6889e0d3-a057-3383-8f4e-e58518e8a505 | -1.24682 | -51.60995 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c284006-113b-3a33-9086-1b42ab706d1e | -2.9027 | -53.05356 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3108ab40-e733-3c93-8791-300f279f4d5b | -2.96377 | -51.41255 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea89a7c7-40cd-33d6-a889-589f4b45021d | -3.61596 | -55.31643 | 2024-11-19 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48520e87-eac9-311f-9547-313925d79a18 | -2.75295 | -54.0202 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79ce276c-bb83-3e24-8e6e-9dccca75c5f8 | -2.73803 | -54.11613 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27de5330-5643-3513-a0de-37d50d2a0b43 | -2.9618 | -51.45207 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e8e5f49-a36a-3354-83e6-2a9d66dbe43c | -2.54299 | -47.33253 | 2024-11-19 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdbdafda-48f1-3f23-89f7-ad8617e8badb | -3.48222 | -48.25107 | 2024-11-19 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 383f4c44-4c2e-3e9b-9067-be99bd88e77b | -3.36722 | -54.10588 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2efef416-bad5-3f6e-bc76-d14f16c359fe | -2.59095 | -53.99253 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ee2e5a7-0af1-33e7-9a81-1f1a94892f41 | -1.67321 | -53.10347 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34257ee4-57f3-346d-80d7-71e1a3c91f75 | -2.60517 | -51.78906 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 687cd2e2-0b52-38cc-b46d-0291e48ea574 | -1.95278 | -54.45388 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a5dc760-6462-375c-a5c0-763ccf7f475a | -1.84239 | -46.28184 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4b0030-7426-330b-92b6-c10300f8c550 | -2.87575 | -51.47483 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77a3eacd-dc34-3f3e-b8e6-d3141e99068b | -2.16674 | -51.9687 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1292b7d7-ea11-3a24-8e89-cc0e465a5eb6 | -4.38708 | -47.76417 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71aa4d26-7bd2-3be2-814a-2f12597c53a4 | -3.55167 | -51.52683 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7754654b-0dc2-3470-87f2-641dc467b072 | -3.09923 | -51.31689 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c94b6e-6b46-32e8-a07e-f94c4b143670 | -3.06783 | -53.28748 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7fda56f-b24a-3ab5-af8e-0af3b3a68c8a | -1.37531 | -52.08366 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4f3eb8e-7b50-34ea-a05f-843884ff5d88 | -3.09515 | -51.31623 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b5a496-6cc7-3522-8ab0-89c8cd7a9651 | -1.25287 | -52.05317 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40885c3b-0184-37c7-a33d-c8f8ab15b37b | -3.70768 | -51.84109 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ba4acf-fa79-32fc-96b8-5d1b111e6cd7 | -1.21154 | -51.7631 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e058b196-099e-3a13-b2e0-1eb5f0fbf5ee | -2.74984 | -54.06313 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 373d1c96-3ca6-32b3-bf45-1d77f7699422 | -3.28612 | -54.1179 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61a89910-a68b-3964-af83-004f8db32b80 | -3.36118 | -50.82047 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 669e6989-6404-3e80-95cc-7f05d3293ae9 | -1.62416 | -55.14475 | 2024-11-19 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3af4eb02-699d-3cce-acea-3d386aa5bf62 | -3.7395 | -51.33296 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e28160-e6fc-34fb-ba8d-7e4f81fa1bc9 | -1.91528 | -53.33907 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a32c22e-b89a-3c03-a290-98fd2dfbea1f | -2.66465 | -51.71611 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9aed70a7-2d35-3fba-890f-bb496b7e59c2 | -4.06385 | -50.0042 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 358f4f2a-53ad-3d64-8ffe-a5062bf9b306 | -3.50776 | -54.7107 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f4f5a78-b2af-3aaa-b1eb-4ce9e45be066 | -1.48738 | -52.10127 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 169a3e6e-7991-3171-889f-832ea8630bbb | -3.6102 | -54.74844 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4e12ea6-fb85-32a3-9163-adea39bb8270 | -4.06 | -49.99904 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8fabd92-53eb-3dc0-af88-09c941859e63 | -3.11525 | -53.70764 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd1c93ab-f2b9-3ea6-8264-3127d1e39804 | -3.47114 | -48.25597 | 2024-11-19 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ded56007-fbe4-3bfe-aaad-070fa60e1472 | -2.72399 | -53.97587 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3654c84d-bead-3be2-b5e1-15ed7896f05d | -4.55898 | -48.009 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 945badca-7cea-360c-811a-d847c13c4c8c | -2.28713 | -53.63343 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0bced781-55c6-38b6-9f33-90d7efaada6b | -5.97866 | -45.36276 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e878255a-1527-3830-9e95-ab8bd4cdcea6 | -3.30928 | -53.36453 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6c0dc31-2054-3312-b151-419d8cc2a734 | -1.16235 | -46.75158 | 2024-11-19 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72853939-e1c1-380f-98e7-9549ac4c59d3 | -2.58513 | -51.71777 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 572bb1e4-f170-3e4d-93ed-e0b28f440a8d | -1.37883 | -52.08173 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a048570c-93b0-37a4-b2e2-4a355c7c53e2 | -1.62265 | -53.29737 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a18bfc4-85b1-3b14-8d6c-aba3f07c15a9 | -3.51209 | -53.79708 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dd6e65b3-c0a1-30ac-98c1-7a4909cd645b | -1.58391 | -53.79694 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d833a03e-40dd-3a4c-bbee-93901ae5583a | -3.05714 | -54.40302 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb86727-ef4c-3c66-8a43-58da63119298 | -4.94544 | -47.80278 | 2024-11-19 05:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05019953-a46b-324f-ade1-8ceb43f5528c | -3.57513 | -54.54955 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fed0fa0-4a72-3c79-bacd-b1952adb1b74 | -4.95077 | -47.80373 | 2024-11-19 05:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2faf631-169f-307b-a3db-843bf0706797 | -1.61675 | -53.28842 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e9ec22e-44d3-3009-a059-61113450899a | -3.9008 | -52.41058 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92662953-e2cf-3d52-a112-e3f94f74e55c | -1.38473 | -51.99971 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff04bb79-1be1-3585-a7bb-8bea48325c3d | -3.79595 | -50.25929 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56fa8e4d-c816-3aa3-bf73-47ed1b9d4e39 | -3.03774 | -49.47101 | 2024-11-19 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c8afcc8-1edb-35b9-b6a2-cfa34621b3a6 | -1.05268 | -52.44246 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 911bea93-a45c-3b17-9a38-d284493ce2ce | -2.25752 | -50.46321 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f99197e-5940-3a38-a6a2-cb4217ccfd10 | -4.55759 | -48.01841 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 99dde7b2-1793-3fe1-a210-cafe9d49edcb | -3.59677 | -53.99594 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 844ed925-8e29-3178-b0a5-7fa5d62479c3 | -3.04621 | -54.40514 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 482ef877-eb49-3f2e-aafe-3ee9327be5e5 | -4.37985 | -47.77626 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ef1d79-c09a-3b2f-bd76-5db3f58ff18f | -1.78848 | -53.59353 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d325357-c32a-38e0-a4fb-02d4ca79468f | -4.56376 | -48.01294 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5ada235-2827-30a3-aff7-3bbac9388429 | -3.04679 | -54.4014 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 907e318f-9e30-308f-a0b6-b6a069259cfc | -1.99678 | -45.34583 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43324c59-5493-37ae-83a8-83b824574fd3 | -3.98911 | -49.91349 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66d771fb-7811-354a-9c3d-d2579a29be0c | -3.48949 | -53.99192 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b77378a6-c9e2-3bf0-969e-6491fe1bb01a | -1.65652 | -52.53289 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e6e498-1c61-32c1-9af6-672a8c605f5b | -4.57996 | -48.01209 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 278c8332-8b48-3a85-9b63-d9d181bb94e1 | -4.55281 | -48.01453 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 9075252b-9b14-3629-9714-de16f88fe9da | -1.73176 | -52.69846 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fee1534f-1c90-35a5-a549-abbdd528ca56 | -1.63877 | -52.67281 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5200c5b1-bb7a-3447-a3c1-7deb3f2fca32 | -1.92052 | -53.35226 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ab4ab7-f806-3c43-8d60-531eb52799d1 | -1.6261 | -52.40359 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c851eba6-5647-32e7-8a05-351b652c13b2 | -3.05655 | -54.4068 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bceb577f-95b9-3019-abf3-4e568fb5cbb2 | -1.70388 | -52.14846 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a61cc32-744a-3927-a886-541c0f00676b | -3.7636 | -51.92778 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c38b2497-6700-30b2-83bc-f672f70b9731 | -1.39688 | -47.45191 | 2024-11-19 05:08:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c987b60c-5505-3ef0-b90d-6bc8d198c714 | -3.60992 | -54.2131 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ebd25c-b3e5-339b-9530-4deaa6bfb777 | -5.1698 | -45.71556 | 2024-11-19 05:08:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8b47fb34-e0e8-3778-a624-ff3805cf4516 | -2.21577 | -53.79097 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8947c10b-42c8-3ecb-aedc-4f2c23b20d83 | -1.2051 | -51.76987 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39c4092e-458d-3077-a078-6f55e2fd7a5a | -1.04619 | -51.74335 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f181b2b6-7e5a-3565-97d0-9f757206c141 | -2.89903 | -53.05301 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b4a693e-7966-3d23-a8d4-364152644ea3 | -2.77235 | -52.59749 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 286daa79-b83f-3b9a-9b01-70c7f3b1d96e | -3.99298 | -49.91886 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6030e3f1-be20-316c-9905-7c9401d8791f | -4.38998 | -47.78114 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 987f514b-602f-3f7d-8468-d74624870eaf | -3.76757 | -51.92835 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca02cc7-37b2-390c-8d2d-16f20f3ea471 | -3.58568 | -53.72202 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b56ae0-3f41-3ec8-adbe-51d87f39c488 | -0.9417 | -51.71926 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802c987f-bfc8-3061-8068-b55993709d86 | -1.57419 | -53.74444 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e351c200-a308-37df-acf0-e8698dd68787 | -3.05918 | -51.33282 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b34ade88-80c8-3ccc-8089-98b9fbda72d8 | -1.6381 | -52.67714 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f5e2ed5-aae8-3ebb-b83e-ee1dcb476c1b | -1.58271 | -53.80465 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6118838-276e-3247-88b0-213296493911 | -3.50397 | -54.03832 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
