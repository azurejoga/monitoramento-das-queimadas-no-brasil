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
| dd12b2c6-a2b8-36f5-9f5c-a724e2e1ee7c | -2.8508 | -53.95805 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b11e00e1-2acb-3880-b797-b1eeb1b4cf93 | -3.96242 | -46.91682 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0f9a0c4-7192-3f0d-a9c3-edd3ad90290b | -2.96992 | -48.00738 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b64cad-6cfa-36f2-abde-5b91d5ca466a | -4.04891 | -48.32998 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4edfd487-4690-30dc-ab07-eba94ba638b9 | -3.84263 | -52.39119 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e10c26b-adfe-38fe-91b4-a45ac7b6d465 | -3.34453 | -46.61327 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 639f774c-9e6d-32f0-9a33-666ce031db8f | -2.90596 | -51.58226 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 729fcfc3-7db9-3c6b-90d2-7c49a8ba5c20 | -2.89972 | -51.37454 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64ff8a6a-4c09-3c62-9358-82d6ab986308 | -3.41329 | -50.24447 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0a49fef4-47e4-3b69-b951-ad4434669ac7 | -2.94147 | -51.58958 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 482aa96f-53a9-337c-80f4-adfa7c3c86f9 | -1.73699 | -52.74896 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d17ca0c1-bb1a-3e82-81c0-713ffa731134 | -2.94651 | -51.58614 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d63aa7ea-a22d-3571-a963-6ca5ae3e120e | -3.28858 | -50.75785 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b496f5ba-2641-3423-a434-471705c27937 | -5.46683 | -38.02685 | 2024-11-28 04:25:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7678869-13c1-3014-9bb6-517983664f20 | -2.82866 | -54.06167 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ca62ce3-d88b-3cf9-ab39-0d1e4aa3df6a | -3.93824 | -48.14097 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dcec3d5-5f3e-36c8-b11b-af7ba5aa0e2d | -4.73309 | -46.55596 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af443411-307a-3448-92ac-104b76f31d5e | -3.05355 | -53.28099 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d95d9052-278b-3144-9ea9-c4936982dcf5 | -3.06761 | -54.41059 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9bddf2e-d489-38ca-916b-1c0196a97052 | -4.99803 | -44.80139 | 2024-11-28 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ece4c051-e6d7-3027-8c27-2d9cf505dfd7 | -14.91549 | -52.87095 | 2024-11-28 04:25:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 591ad74e-ce32-3632-b62a-09e2bf2cb7d1 | -3.98328 | -46.65582 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb9cc850-efb4-3f51-a703-aae458b3a710 | -3.97546 | -46.7266 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66d9dc0a-4a7e-3085-9653-815bbbafad04 | -4.86067 | -42.66859 | 2024-11-28 04:25:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79bf2383-6681-3263-9842-4650a529b0d9 | -1.70283 | -54.72636 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d6f467f-7396-3f2a-9644-07595a1f3283 | -3.22819 | -53.62583 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39f1ee81-31b1-3ae8-af3b-a4a06a6adfff | -3.10368 | -53.81608 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30a06e93-3057-316c-8811-15548618dbe9 | -3.2692 | -50.61753 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b640384-c58c-3f56-8d1f-bd9a340a0213 | -5.07068 | -46.82721 | 2024-11-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56dd046c-449f-3bbb-b6ce-625755c885e3 | -3.31002 | -53.75276 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598c0913-ec3b-3d28-96c6-b40e6e07d60d | -3.40041 | -54.28694 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 904a87c7-e137-390f-999b-78ba7aacb179 | -4.73252 | -46.73112 | 2024-11-28 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da6de954-2d54-3ca2-a964-b6ed6bad7ec5 | -4.05381 | -46.68162 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3e590e-c8c2-3a00-a9b6-0af6eaf12851 | -3.6122 | -50.76561 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d48c62ee-0d10-366c-b212-96d2c868d511 | -3.26623 | -46.44333 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 023a1049-c5a7-3b7b-9673-a25486cecafa | -3.30026 | -45.51669 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b1828d8a-9007-3924-91f5-ab8320689e35 | -2.79004 | -51.74252 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5149f9d-fbc0-391b-b157-4003d8b55bfb | -3.81063 | -46.61046 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b394674-bcd8-3944-9985-9798f1cfb56b | -4.38648 | -43.85635 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9600aaa6-589c-326f-bc75-337af4fa0e5d | -3.96446 | -48.08953 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c3edc9e3-ba96-3585-9a03-1ba1098fb158 | -3.18732 | -48.12383 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcdac599-0217-36a9-af65-b3eb2be3a1eb | -3.97926 | -48.0642 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2626cc1-cfc8-3a33-9791-065303c0516a | -3.2282 | -48.8193 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68d175d-a6a8-3cee-aa3b-e9c1f4315a42 | -2.85195 | -46.868 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bf6bcc9-aaca-3f73-92ab-a6ff703a9705 | -4.91707 | -47.859 | 2024-11-28 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 371275f4-eede-307e-b27c-c4423e54f5a0 | -3.49433 | -44.60506 | 2024-11-28 04:25:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a189150-53f2-3661-8adb-49812fcf85b5 | -2.91565 | -48.32432 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b741ef9-5e1d-3b22-95cc-93ea8485c514 | -3.57996 | -46.34917 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 673de061-5005-3172-a45f-14e314e9e5c1 | -2.24761 | -53.62793 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8c12a74-534c-3401-b8ef-01b548963e37 | -9.61955 | -51.49616 | 2024-11-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b74d617-b9e8-31ff-85a8-4903c7275f4b | -3.38577 | -51.23763 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7448e55-7aa7-3f52-9d3a-3f41b17cb2b4 | -3.26735 | -48.76065 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d60588f-ca51-3a16-8700-663219883c58 | -3.81006 | -46.59247 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9de2f9b6-633f-3690-a674-43af0189145e | -4.13315 | -46.11639 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaff7171-db57-319e-8cb6-ddabcf2e06f0 | -2.8391 | -46.84023 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49d33365-ad20-33ad-990c-e9c10416aa1e | -3.7845 | -46.68916 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a9a0efe-8e0e-398f-95e0-6699f4d8e003 | -3.70489 | -47.12589 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cc2770b-93ee-3d8d-9a39-c7be1f5af14b | -3.68075 | -50.884 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8297a685-0797-38cb-a2d3-e3304bfb691b | -3.46349 | -51.58961 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d150f4e1-4321-3394-ac1e-125b337e937e | -4.6704 | -44.62026 | 2024-11-28 04:25:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dcc302e-49b6-3126-abb1-79cf4cf4cbc3 | -3.1822 | -50.2813 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92defa74-b4d7-388d-8f6f-94214d723244 | -2.83559 | -54.11721 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 64267e4f-b378-32fc-a725-1c14c44ad2a4 | -11.12451 | -45.12503 | 2024-11-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c2ab76a-7885-30b1-ba80-2f3c3ccbf4bc | -1.79094 | -52.74806 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62717641-83fe-3f95-84a8-e2d50fb3de53 | -3.81507 | -46.60397 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08eaba1c-d50b-343a-98e6-f2532abf82d2 | -3.28542 | -50.62018 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdf8b009-55b6-3fa1-96de-0c3ee6bd9622 | -2.232 | -53.69227 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67ab80e5-4ff8-3279-bba2-84d84d560abe | -4.59972 | -49.39231 | 2024-11-28 04:25:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad16acc-515f-3719-9d7a-b1a11a2ad63b | -3.37737 | -50.41483 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3dec26b-42e9-3bcc-a032-e0957ec6df18 | -2.91706 | -48.32117 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 846883a3-5f21-328d-97ca-167112f5712c | -3.53407 | -50.19433 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66972426-a12b-379d-bb39-2f7f13dd2322 | -3.02436 | -54.02054 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ead890e-183b-3355-aef2-f82337ca575a | -3.22253 | -45.38482 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b857d2-f5b3-3464-a4b6-15af9eec66ca | -2.25297 | -53.46728 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 265269e0-b680-37f1-afa8-eaf22c62fe9e | -2.25653 | -53.7534 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55d079ff-51e0-39de-bdec-1edd997251ae | -4.67095 | -44.61671 | 2024-11-28 04:25:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 115b49e1-6270-3ead-bd22-b0f493f94158 | -2.25798 | -53.46809 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aa11f45-6ffb-3c94-9d13-06d044e4d787 | -3.24902 | -46.42267 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901a71c0-68cc-319d-a2cd-735fe15d931a | -4.51701 | -45.72861 | 2024-11-28 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c809cf-ad23-3efa-a869-85d4c42430a1 | -2.18387 | -52.12822 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee83b9f8-1068-3971-8ad8-93e34f77a9ce | -3.27086 | -50.55575 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc37f175-3e7e-3af5-9380-508ae8c41184 | -2.71447 | -47.70635 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b169995-4f5a-3926-aa5b-fcfcdd2fcf32 | -2.91568 | -51.71809 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8a2047e-121c-31b8-a6ed-207e623f1872 | -4.21978 | -48.66398 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01e28934-b73f-35b4-8b88-7d53aa3fd63b | -3.58239 | -50.33865 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f89c5d00-e6b6-360b-a357-f0dd98b9e288 | -1.62634 | -53.87935 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 545b5e6c-bb67-3d64-a9c2-01d5c28bfbec | -3.88283 | -46.66885 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e3bcca6-ce16-369f-9d0a-a4f3f313becd | -2.59134 | -53.96907 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01f53a6e-124f-37bd-8df4-45f8991d8431 | -1.56448 | -55.78978 | 2024-11-28 04:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1554a19-992d-315a-ad01-5295b4c11569 | -3.96247 | -46.89485 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8363bfe-7047-3bf2-9c0d-1c15657b545e | -3.68093 | -49.93321 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ddd1db-a380-3fd4-9fe5-7474c49f7e38 | -3.23336 | -53.93365 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5908bdb-bf29-3cf2-8820-05842b067670 | -1.70342 | -54.72274 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d2fe473-b6e6-3316-bb70-cb3f8da04574 | -2.86264 | -46.86599 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8016ff6b-1cc8-3685-926c-f7e546a19756 | -2.34498 | -53.92189 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9478960-c2d0-35be-9d02-015b224c9327 | -4.38053 | -45.97174 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fff5d5df-e129-3a02-b0f8-cd20ba65ce11 | -3.16618 | -48.43628 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4db58c2-0de2-37a7-8d20-f2d787846392 | -3.30548 | -54.17916 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9e8ed10-2f24-34c7-97a0-52e2f52574db | -2.231 | -55.9017 | 2024-11-28 04:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| babee16f-a350-37ac-a4a5-b5dd44ea4567 | -3.85226 | -47.05712 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README68.md)
